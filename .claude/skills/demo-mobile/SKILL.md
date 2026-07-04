---
name: demo-mobile
description: 把本機或雲端 sandbox 的 HTML / dev server 用 Cloudflare Tunnel quick tunnel 暴露給手機看。自動偵測環境（macOS 本機 vs Linux 雲端 sandbox）走對應流程。用戶說 /demo-mobile、讓手機看這個 html、tunnel 給手機、把 dashboard / demo 給手機看、想用手機看本機或 sandbox 的某某時，使用這個 skill。流程：偵測平台 → 確保 cloudflared 可用 → 起 server → 起 tunnel → 等 URL → 視環境輸出（QR + pbcopy / 純 URL）→ 等用戶收尾。
---

# demo-mobile

把 HTML 或 dev server 用 Cloudflare Tunnel quick tunnel 暴露給手機看。**自動偵測 macOS 本機 vs Linux 雲端 sandbox**，走對應流程。

## 什麼時候用

- 用戶說 `/demo-mobile`
- 「讓手機看這個 html / dashboard / demo」
- 「把這個給手機看一下」
- 「tunnel 給手機」、「手機怎麼看」

**兩個典型場景**：
- **本機 macOS**：跨網段（不同 Wi-Fi、5G、外面咖啡廳）想用手機看本機 demo
- **雲端 sandbox**：你在手機上用 Claude Code（雲端 agent），agent 生成或編輯了 HTML，需要讓你能在手機點開

## 用法

| 指令 | 效果 |
|------|------|
| `/demo-mobile` | 用 cwd + port 8000 起 server |
| `/demo-mobile <path>` | path 是資料夾→該資料夾起 server；path 是檔案→cd 父目錄、URL 加檔名 |
| `/demo-mobile --port 3000` | 跳過起 server，直接 tunnel 已在跑的 dev server (localhost:3000) |

## 工作流

### 0. 環境偵測

```bash
PLATFORM=$(uname -s)   # Darwin (macOS) / Linux (cloud sandbox)
ARCH=$(uname -m)       # x86_64 / arm64 / aarch64
```

兩條路：
- `Darwin` → **macOS 路徑**（brew、pbcopy、qrencode、互動式收尾）
- `Linux` → **雲端路徑**（curl 下載 binary、純 URL 輸出、不依賴本機工具）

### 1. 確保 cloudflared 可用

#### macOS

```bash
which cloudflared qrencode >/dev/null || brew install cloudflared qrencode
CLOUDFLARED=cloudflared
```

#### Linux (cloud sandbox)

不能假設有 brew / sudo。下載 static binary 到 `$HOME/.local/bin`：

```bash
CLOUDFLARED=$(command -v cloudflared || echo "$HOME/.local/bin/cloudflared")
if ! [ -x "$CLOUDFLARED" ]; then
  case "$(uname -m)" in
    x86_64)         BIN="cloudflared-linux-amd64" ;;
    aarch64|arm64)  BIN="cloudflared-linux-arm64" ;;
    *)              echo "Unsupported arch: $(uname -m)"; exit 1 ;;
  esac
  mkdir -p "$HOME/.local/bin"
  curl -fsSL -o "$CLOUDFLARED" \
    "https://github.com/cloudflare/cloudflared/releases/latest/download/$BIN"
  chmod +x "$CLOUDFLARED"
fi
```

後續一律用 `"$CLOUDFLARED" tunnel ...`（不依賴 PATH，避免 background bash 找不到）。

雲端**不需要** qrencode（手機本身就是在看對話的設備）。

### 2. Port 衝突檢查

```bash
lsof -i :<port> 2>/dev/null
```

有東西就提醒用戶或換 port。

### 3. 起 HTTP server（如有需要）

```bash
cd <target_dir> && python3 -m http.server <port>
```

`run_in_background: true`。

### 4. 起 cloudflared tunnel

```bash
"$CLOUDFLARED" tunnel --url http://localhost:<port>
```

`run_in_background: true`。記下 output file 路徑。

### 5. 等 URL 出現（不要 sleep loop）

```bash
until grep -oE 'https://[a-z0-9-]+\.trycloudflare\.com' <cloudflared_output_file> 2>/dev/null; do
  sleep 0.5
done
```

`run_in_background: true`，timeout 60s。等通知後讀 output。

### 6. 輸出（依環境分支）

#### macOS

```bash
URL="https://xxx-xxx-xxx-xxx.trycloudflare.com${URL_SUFFIX}"
echo "$URL" | pbcopy
echo "URL: $URL (已複製到剪貼簿)"
curl -sI -o /dev/null -w "HTTP %{http_code}\n" --max-time 10 "$URL"
qrencode -t ANSIUTF8 "$URL"
```

#### Linux (cloud)

```bash
URL="https://xxx-xxx-xxx-xxx.trycloudflare.com${URL_SUFFIX}"
echo "URL: $URL"
curl -sI -o /dev/null -w "HTTP %{http_code}\n" --max-time 10 "$URL"
```

雲端**不印 QR code、不 pbcopy**，因為手機已能直接看到 URL 並長按複製。

### 7. 回報用戶（簡短）

#### macOS

```
Tunnel 起好。
URL: <url>（剪貼簿已複製）
連線檢查: HTTP 200
QR code 上面，掃就連。

看完跟我說「關掉」，我 kill process，URL 立刻失效。
```

#### Linux (cloud)

```
Tunnel 起好。
URL: <url>
連線檢查: HTTP 200

手機長按 URL → 開新分頁。
看完跟我說「關掉」我 kill process。（sandbox 結束會自動清，但 explicit kill 仍是好習慣）
```

### 8. 收尾（用戶說關掉 / 結束 / 看完 / done 時）

```bash
pkill -f "cloudflared tunnel"
pkill -f "http.server <port>"
sleep 1
pgrep -fl "cloudflared|http.server" || echo "已全部關閉"
curl -sI -o /dev/null -w "URL: HTTP %{http_code}\n" --max-time 5 "$URL"  # 預期 5xx
```

## 環境差異速查

| 項目 | macOS 本機 | Linux 雲端 sandbox |
|---|---|---|
| 安裝 cloudflared | `brew install` | `curl -L github releases` 到 `~/.local/bin` |
| 安裝 qrencode | `brew install` | **不需要** |
| 複製 URL | `pbcopy` | **不需要**（手機長按 URL） |
| QR code | `qrencode -t ANSIUTF8` | **不印** |
| 二進位呼叫 | `cloudflared` (PATH) | `"$CLOUDFLARED"` 絕對路徑（PATH 在 background bash 可能失效）|
| 收尾觸發 | 用戶明示「關掉」 | 用戶說「關掉」或 sandbox 結束自動清 |
| 隱私邊界 | HTML 內容 leak 是新風險 | sandbox 本身已是 trust boundary，但 tunnel 仍是新通路要小心 |

## 平台優化（先做這個再 fallback 到 tunnel）

如果 platform 有內建 port forwarding，比 cloudflared 更乾淨，先試這條：

- `$CODESPACES` 非空 → **GitHub Codespaces**：用 `gh codespace ports visibility <port>:public` 或 web UI 的 Ports 面板
- `$REPL_ID` 非空 → **Replit**：服務已暴露在 `https://*.replit.dev`，不需要再 tunnel
- 其他偵測不到 → 退回 cloudflared

偵測程式碼：

```bash
if [ -n "$CODESPACES" ]; then
  echo "偵測到 GitHub Codespaces，建議用內建 port forwarding 而非 cloudflared"
elif [ -n "$REPL_ID" ]; then
  echo "偵測到 Replit，服務已在 *.replit.dev 暴露"
fi
```

但 cloudflared 是萬用 fallback，platform 偵測不到時直接 tunnel。

## 風險提醒（觸發條件下講，不要每次都念）

只在以下情況提醒用戶：

- 路徑含 `customer`, `private`, `internal`, `secret`, `client`, `confidential`
- 用戶說過 demo 是「未公開」、「機密」、「商業」、「客戶」相關
- 目標目錄裡有 `.env`、`credentials`、`*token*` 檔案（python http.server 會把整個資料夾當靜態檔暴露）

提醒訊息（精簡）：

> 注意：CF quick tunnel 在邊緣能看到明文 HTTP，且 URL 可能被 Chrome Safe Browsing / URLScan / VirusTotal 收進公開資料庫。建議只放純前端、無敏感內容，跑完就關。

對純研究 demo / dashboard / 個人 HTML：跳過提醒，直接跑。

## Quick tunnel 已知限制

- 200 concurrent in-flight requests 上限
- **不支援 SSE**（Server-Sent Events）
- 無 SLA
- 每次重啟新 URL（舊的永久失效）

→ 用戶要 demo Streamlit、LLM 串流、SSE-based app：先警告 SSE 不支援。本機走 Tailscale 或 named tunnel；雲端走 platform 內建 port forwarding。

## 不要這樣做

- 不要 sleep loop polling URL → 用 `run_in_background` + `until grep` idiom
- **不要跳過環境偵測** → 在 Linux 跑 `brew install` 會炸；在 macOS 跑 `curl` 下載 binary 是多餘的
- 不要在雲端用 `cloudflared` 不加路徑 → background bash 可能找不到，永遠用 `"$CLOUDFLARED"` 變數
- 不要忘記收尾 → 用戶說「關掉 / 結束 / 看完 / 跑通了」要主動 kill
- 不要 tunnel 含 `.env`、`credentials.json`、`*.key` 的目錄而不警告
- 不要假設 port 沒被佔 → 先 `lsof -i`

## 進階：要分享給別人（不在此 skill 範圍）

quick tunnel 不適合分發。長期分享：
- **Cloudflare Access**：免費 50 人額度，加 Google/GitHub OAuth 白名單
- **named tunnel**：穩定 URL（需 Cloudflare 帳號）
- **Tailscale**：跨地點訪問家裡 server

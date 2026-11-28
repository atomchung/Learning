# 量測：AI 會不會推薦某個產品

用同一組問句問多個模型，分「不上網」與「上網」兩條路，看某個產品有沒有被列入、排第幾、引用了哪些頁面。2026-11-27 用它量了 [Brevo 案例](../case_studies/brevo-free-smtp-2026-11.md)。

## 檔案

- `prompts/`：問句。SMTP 類別：`en`、`zh` 不上網，`sen`、`szh` 上網。跑步＋重訓 AI 教練類別：`cen`、`czh` 不上網，`csen`、`cszh` 上網。
- `run_nosearch.sh`、`run_search.sh`：對一個模型跑一次。
- `rank.py`：從回答抽出排名順序。廠商名單 `V` 在檔案開頭，換類別要改。
- `listicle.py`：從存下來的清單文 HTML 抽出排名，數聯盟連結。
- `pageinfo.py`：看一個頁面的 title、JSON-LD 類型、標題結構、更新日期。

## 怎麼跑

```bash
cd topics/aeo/measure
OUT=$HOME/aeo-runs/$(date +%F)
for m in opus sonnet haiku codex gemini grok; do
  for p in en zh; do
    for r in 1 2; do ./run_nosearch.sh $p $m $r $OUT; done
  done
done
python3 rank.py $OUT nosearch_
```

上網那組換 `run_search.sh` 與 `sen`、`szh`。Google AI 摘要沒有 CLI，用瀏覽器手動查，記下名次與引用的網址。原始回答不要放進這個 repo：它是公開的，回答裡可能帶出個人記憶。

## 乾淨量測的條件

不照做，模型會「知道」你的產品，結果作廢。

1. 在專案資料夾以外的空目錄跑（腳本用 `mktemp -d`）。在專案或它的 worktree 裡跑，Claude 會讀到那個專案的 CLAUDE.md 與記憶。
2. Claude：`--setting-sources project`，不載入全域 `~/.claude/CLAUDE.md`。
3. Codex：`-c features.memories=false -c memories.use_memories=false`，關掉個人記憶。
4. Grok：沒有關閉本機 skills 的旗標。問自己的產品時 Grok 的結果不能用。
5. 判斷乾淨與否看回答：出現只有你知道的事（內部名稱、「你自己的專案」）就作廢。
6. Google AI 摘要用無痕視窗查，已登入的瀏覽器可能有個人化。

## 限制

- 模型 ID 與 CLI 旗標以 2026-11-27 為準：Codex CLI 0.156.1（設定檔預設的 gpt-6.2-sol 在 ChatGPT 帳號登入下被拒，改用 gpt-6-luna）、agy 1.5.18、grok 1.0.92。之後會過期。
- 每個組合 1–2 次，只看趨勢。
- `rank.py` 靠行首編號與廠商名比對，表格或散文格式的回答要人工核。

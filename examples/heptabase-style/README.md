# Heptabase 風格學習結構範例

這個資料夾示範如何把 `compare-coding-agents.md` 這種「長文終產物」拆回「卡片 + 起點 + 旅程」的 Heptabase 風格結構。

## 檔案說明

```
examples/heptabase-style/
├── _start.md                              # 起點卡：主題中心，膨脹式地塞新資訊
├── cards/                                 # 原子卡：一張一個概念
│   ├── harness-beats-model.md
│   ├── codex-no-network-sandbox.md
│   └── claude-code-human-in-loop.md
└── journey/                               # 每週理解快照
    └── 2026-04-23.md
```

## 設計原則對照

| 原則 | 檔案中如何體現 |
|------|--------------|
| **原子化** | 每張卡 title 是一句話，內容只講那一件事 |
| **起點白板** | `_start.md` 列出「累積但未拆的發現」，決定下一步拆哪張 |
| **Context-tracing** | 每張卡有 `appears-on:` 列出它屬於哪些白板 |
| **視覺化關係** | Markdown 裡用 `← 支持`、`↔ 對比`、`→ 引出` 顯化連結類型 |
| **Journey 過程保留** | 每週快照寫「當前我認為的答案」＋「哪裡跳躍了」 |
| **Create 為副產品** | 長文 `compare-coding-agents.md` 由卡片重組而來，不是從零寫 |

## 這樣做的好處

### 1. 下次寫新主題可以重用
當你要寫「AI Agent 的安全模型」時，`codex-no-network-sandbox.md` 這張卡可以直接被拉進新白板，不必重新研究。

### 2. 一個月後回看不會失效
傳統長文一個月後回看只剩字，但 `harness-beats-model.md` 的標題本身已經是判斷，隨時都可理解。

### 3. 找漏洞變容易
卡片有「反例與質疑」欄位，強迫你在寫下主張的同時考慮反論。這是線性長文常漏掉的防線。

### 4. 跳躍點變可見
Journey 快照讓你清楚看到「哪一週、因為什麼，我的理解跳了一層」——這是最有複製價值的後設資料。

## 怎麼開始

如果要把這套做法套在 Learning repo 上：

1. **不要動現有的長文**——它是結果，留著當 output 參考
2. **回推卡片**：從 `compare-coding-agents.md` 提煉 10–15 張原子卡到 `cards/`
3. **開下一個主題的起點卡**：e.g. `_start-ai-agent-safety.md`
4. **每週五寫一次 journey**：即使只寫 5 分鐘也比不寫好

起點白板會膨脹，卡片會累積，Journey 會顯影——三個月後你會發現自己有一個**可重用、不貶值、能看出進步軌跡**的知識庫。

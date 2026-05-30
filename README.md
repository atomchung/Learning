# Learning — 全 repo 學習地圖

> 這份是**跨分支的總覽**：把散落在十幾個 `claude/*` 分支裡的學習，從點串成線、連成面。
>
> 方法論在 [`CLAUDE.md`](./CLAUDE.md) 與 [`heptabase-design-research.md`](./heptabase-design-research.md)。
> 這份不重複方法論，只回答一個問題：**到目前為止，我到底學了哪些東西、它們怎麼歸類。**
>
> 最後更新：2026-05-30

## 怎麼讀這個 repo

知識散落在兩個地方：

1. **`main`（這裡）**：已經沉澱成卡片系統的主題。這是「面」已經長出來的部分。
2. **`claude/*` 分支**：每個分支是一次學習 session，多數還沒 merge 回 main。原始素材在那裡。

換句話說，`main` 是成品櫃，分支是工作檯。這份地圖把兩邊都標出來。

## main 上已成形的主題（卡片系統）

- [`topics/coding-agents/`](./topics/coding-agents/_start.md) — coding agent 的設計權衡（13 張原子卡 + 2 篇 journey）。核心命題：**harness 比模型更決定體驗**。
- [`topics/msft-openai-super-app/`](./topics/msft-openai-super-app/_start.md) — 從投資視角看 Codex super app（剛開，累積中）。

長文產物（Create 階段）：[`compare-coding-agents.md`](./compare-coding-agents.md)。

## 四條主題線（散落分支的歸類）

把所有分支按主題收攏，會浮現四條線。

### 線一：Agent 與編程工具的本質

- `compare-coding-agents` — Codex / Antigravity / Claude Code 比較 + harness 深析（已成卡片進 main）
- `agent-context-best-practices` — agent context 最佳實踐、`/handoff` skill、SessionStart hook 迴圈
- `improve-skills-workflow` — Karpathy AutoResearch 分析、grader 設計、skills 工作流
- `ai-agents-ecosystem-integration` — AI agent 生態系整合分析
- `add-demo-mobile-skill` — 手機版 Claude Code 的 demo skill

### 線二：學習系統怎麼設計（這個 repo 的元主題）

- `hetabase-design-research` — Heptabase 方法論推導（這套卡片系統的源頭）
- `design-learning-repo` — 用 Next.js 做筆記瀏覽 app（flashcard / tag / review）
- `ai-education-research` — Alpha School AI 教育研究 + 自動化腳本（capture / graph / log / review）+ 國中數學主題
- `personal-os-research` — 從交易日誌長出個人 OS + cloud-record skill
- `repo-learning-overview` — 這份地圖本身

### 線三：AI 產業與投資判讀

- `gpt-super-app-analysis` — 微軟/OpenAI super app 的投資角度（已進 main）
- `model-progress-roadmap` — 模型進展路線圖 + 各前沿方向的 app/基建市場衝擊
- `hugging-face-exploration` — Hugging Face 2026 研究 + 投資分析框架
- `podcast-episode-summaries` — AI Daily Brief 7 集摘要 + Agent OS 市場全景與建法
- `anthropic-blog-research` — Anthropic 部落格教學筆記 + 學習路線圖
- `ai-power-user-roadmap` — 個人電腦 vs 工作電腦的 AI power-user 路線、user stories

### 線四：應用實驗（把學的東西做成東西）

- `research-token-usage` — 台北 AI 活動行事曆 MVP（KKTIX → ICS pipeline + GitHub Action）
- `video-prompt-optimization` — AI 影片 prompt 的棒球動作描述技巧

## 從點到面：這個 repo 的隱藏主題

把四條線再拉高一層，會看到一個面：

> **這個 repo 真正在學的，是「如何設計一個能把點長成面的學習系統」——
> 而它用自己正在學的東西（agent、harness、skills、投資判斷）來建造自己。**

線二是元主題（系統怎麼建），線一三四是餵給系統的素材。卡片系統（main）是目前勝出的承載方式，但分支裡還留著腳本版、app 版、skill 版等其他實驗。

## 下一步（讓面更完整）

- 把分支裡成熟的學習**反推成原子卡**收進 `main/topics/`（目前只有 2 個主題進來，素材遠不止）
- 線三（投資判讀）素材最多卻還沒任何卡片化 — 適合開下一個 `topics/`
- 決定工具層要不要收斂：卡片系統 vs 腳本 vs app vs skill，目前四種並存

---

*點是事實，線是理解，面是能在新脈絡中重新召喚的判斷。這份地圖隨分支增長更新。*

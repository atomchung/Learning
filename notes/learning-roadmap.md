# Learning Repo 學習路徑（AI Agent / Coding Agent 主題）

> 這份路徑以本 repo 既有筆記為起點，規劃一條從「讀懂概念 → 動手實作 → 深入原理 → 跨生態比較 → 產出分享」的五階段學習路線。
>
> 目標讀者：想成為 **AI 工程師 / AI 產品經理**、以 Claude Code / Codex / Antigravity 為主力工具的開發者。

---

## 路徑總覽

```
Stage 0  ─ 全景定位        ← 已有：compare-coding-agents.md
   │
Stage 1  ─ 觀念地圖        ← 已有：anthropic-blog-teaching-notes.md
   │
Stage 2  ─ 動手實作（缺）   ── 寫第一個 Agent / 用 Claude Code 完成任務
   │
Stage 3  ─ 底層原理（缺）   ── Transformer、RLHF、Tool Use、MCP 內部機制
   │
Stage 4  ─ 跨生態比較（缺） ── OpenAI / Google / Open-source 觀念體系
   │
Stage 5  ─ 輸出與分享（缺） ── 部落格、開源 Skill、PR review
```

每個 Stage 結束都應該有**可驗收的產出**（筆記、demo 或 commit），而不是只是「讀完了」。

---

## Stage 0：全景定位（已完成）

**現有筆記**：[`compare-coding-agents.md`](./compare-coding-agents.md)

**目的**：知道市場上有哪些 Coding Agent、各自的形態與目標客群。

**驗收**：能用一句話講出 Codex / Antigravity / Claude Code 的核心差異，並說出自己「為什麼選 Claude Code（或別的）」的三個理由。

**回頭補強**：每季更新一次（模型版本、價格、SWE-bench 分數變化很快）。

---

## Stage 1：觀念地圖（已完成）

**現有筆記**：[`anthropic-blog-teaching-notes.md`](./anthropic-blog-teaching-notes.md)

**目的**：建立 Anthropic 生態系的概念骨架——Agent 設計哲學、Context Engineering、Tool Design、Multi-Agent、Safety。

**驗收**：
- 能不看筆記畫出「Workflow vs Agent」的決策樹。
- 能解釋為什麼多代理人 token 用量是 chat 的 15×。
- 能列出 Claude Code 三件套（CLAUDE.md / slash commands / git worktree）。

**回頭補強**：每次 Anthropic 出新 engineering 文章時補進去。

---

## Stage 2：動手實作（建議下一步）

> **這是目前 repo 最缺的一塊**——光讀沒寫，觀念會留不住。

### 2.1 用 Claude Code 完成一個真實任務

- **目標**：在自己一個專案裡，**只用 Claude Code** 完成一個 PR（feature 或 bug fix）。
- **要做**：
  1. 為該 repo 寫第一版 `CLAUDE.md`。
  2. 寫 1–2 個 `.claude/commands/*.md` 自訂指令。
  3. 用 git worktree 開兩個 Claude 平行做不同子任務。
- **輸出筆記**：`practice-01-claude-code-real-task.md`，記錄：
  - `CLAUDE.md` 的演進（v1 → v2 改了什麼）。
  - 哪些 prompt 有效、哪些沒用。
  - 踩到的坑（context 爆掉、tool 卡住、權限被擋）。

### 2.2 用 Claude Agent SDK 寫第一個 Agent

- **目標**：用 Python / TypeScript SDK 做一個 < 200 行的 Agent。
- **建議題目**（挑一個）：
  - 「讀我的 GitHub 通知 → 摘要今天該回覆的 issue/PR」。
  - 「掃描某個 repo → 自動產生 release notes 草稿」。
  - 「監控某網站 RSS → 用 Claude 篩選並寄信」。
- **輸出筆記**：`practice-02-first-agent.md`，重點寫：
  - 你定義了哪些 tool？工具描述如何寫？
  - context 怎麼管理（每輪丟什麼進去）？
  - 失敗模式（hallucinate、無限 loop、token 爆量）。

### 2.3 寫一個可攜的 Skill

- **目標**：把 2.1 或 2.2 累積的知識封裝成一個 `SKILL.md` 包。
- **驗收**：把這個 Skill 同時在 Claude Code 與 API 端跑起來。
- **輸出筆記**：`practice-03-portable-skill.md`。

### Stage 2 驗收

- 至少 3 個 commit 在外部 repo（不是本 repo）展示用 Agent 完成的任務。
- 本 repo 多 3 份 `practice-*.md`。

---

## Stage 3：底層原理（建議第三步）

> 不需要重訓模型，但要知道**模型為什麼這樣行為**，才有辦法 debug。

### 3.1 Transformer & Attention（半天）

- 讀 Jay Alammar《The Illustrated Transformer》。
- **輸出筆記**：`theory-01-transformer-essentials.md`，重點：
  - QKV、Attention、Position Encoding 一頁圖。
  - Decoder-only vs Encoder-Decoder。

### 3.2 RLHF、Constitutional AI、Reward Hacking（一天）

- 讀 Anthropic「Constitutional AI」原始論文。
- 讀「Natural Emergent Misalignment from Reward Hacking」。
- **輸出筆記**：`theory-02-rlhf-and-alignment.md`，重點：
  - SFT → RLHF → CAI 的差異。
  - 為什麼模型會 reward hack、會 alignment fake。

### 3.3 Tool Use / Function Calling 內部機制（一天）

- 讀 Anthropic 的 `tool_use` API 文件 + 一篇 MCP spec。
- **動手**：手刻一個極簡 tool-loop（不靠 SDK）。
- **輸出筆記**：`theory-03-tool-use-internals.md`，重點：
  - Tool schema → 模型怎麼選工具？
  - parallel tool calls 是怎麼運作的？
  - MCP 與普通 function calling 差在哪？

### 3.4 Context Window / KV-Cache / Prompt Caching（半天）

- 讀 Anthropic Prompt Caching 文件。
- **動手**：對一個長 prompt 加 cache、量化命中率與成本下降。
- **輸出筆記**：`theory-04-context-and-caching.md`。

### Stage 3 驗收

- 能向同事白板講解「為什麼工具描述會影響選工具的準確度」。
- 能解釋 prompt caching 在哪些場景省最多錢。

---

## Stage 4：跨生態比較（建議第四步）

> Stage 1 只覆蓋 Anthropic，要避免**生態系視野盲區**，得補上另外兩個。

### 4.1 OpenAI 生態系觀念整理

- 讀 OpenAI 的「Practical Guide to Building Agents」、Responses API、Computer Use、Codex 文件。
- **輸出筆記**：`ecosystem-01-openai-agents.md`，對照 Anthropic 寫差異：
  - Agent 抽象（OpenAI 的 Assistants / Responses vs Anthropic 的 Messages + tool_use）。
  - Memory / 持久狀態的處理。
  - Tool / Function calling schema 差異。

### 4.2 Google / Gemini 生態系

- 讀 Gemini API 文件、Antigravity 設計理念、Google 的 Agent Development Kit。
- **輸出筆記**：`ecosystem-02-google-gemini.md`，重點：
  - Three-surface architecture（editor + terminal + browser）的設計動機。
  - Artifact 機制是什麼、能用在哪。

### 4.3 開源生態（LangGraph / AutoGen / smolagents）

- 挑一個讀 source code 半天。
- **輸出筆記**：`ecosystem-03-open-source-agents.md`，重點：
  - 它們如何模擬閉源 SDK 的 agent loop？
  - 跟 Claude Agent SDK 的設計差異？

### Stage 4 驗收

- 收到「該選哪家 API」的問題時，能 5 分鐘畫出決策樹回答。

---

## Stage 5：輸出與分享（持續）

> 真正鞏固學習的方式是**輸出**——寫得出來才代表懂了。

### 5.1 部落格化

- 把 Stage 2–4 的 practice / theory / ecosystem 筆記挑 3 篇改寫成部落格文章。
- 中英雙語版本（中文留 repo、英文發 dev.to / Medium）。

### 5.2 開源 Skill / Agent

- 把 Stage 2.3 的 Skill 上 GitHub，附中英文 README。
- 接受 issue / PR，從別人提問裡學新東西。

### 5.3 Review 他人 PR

- 在 GitHub 上找 3 個用 Claude Code / Codex 寫的開源 PR，留高品質 review。
- **輸出筆記**：`reflection-01-pr-review-learnings.md`，記錄看到的 anti-pattern。

### 5.4 持續追蹤

- 訂閱：Anthropic News、Alignment Science Blog、OpenAI Blog、Simon Willison's Weblog。
- 每月一篇 `monthly-digest-YYYY-MM.md`：本月最值得讀的 5 篇文章 + 為什麼。

---

## 時間預估（依每週 5–8 小時投入）

| Stage | 預估時間 | 主要產出數 |
| --- | --- | --- |
| 0 + 1 | 已完成 | 2 |
| 2 動手實作 | 3–4 週 | 3 篇 practice + 外部 commits |
| 3 底層原理 | 2 週 | 4 篇 theory |
| 4 跨生態比較 | 2–3 週 | 3 篇 ecosystem |
| 5 輸出分享 | 持續 | 月更 + 開源專案 |

完成 Stage 0–4 大約**2 個月**。Stage 5 是長期習慣。

---

## Repo 檔案命名約定（建議）

維持一目了然的前綴：

```
compare-*.md             ← 橫向比較（產品 / 模型 / 框架）
anthropic-*.md, openai-*.md, google-*.md ← 單一生態系筆記
practice-NN-*.md         ← 動手練習紀錄
theory-NN-*.md           ← 原理性筆記
ecosystem-NN-*.md        ← 跨生態系觀察
reflection-*.md          ← 心得與 review
monthly-digest-YYYY-MM.md ← 每月精選
learning-roadmap.md      ← 本檔（路徑索引）
```

---

## 下一步建議

如果想立刻開始：

1. **本週**：開一個小 side project，套用 Stage 2.1（先寫 `CLAUDE.md`，跑一週看效果）。
2. **下週**：寫第一篇 `practice-01-claude-code-real-task.md`。
3. **月底**：開始 Stage 3.1（Transformer 觀念補完）。

不要等讀完所有資料才開始動手——**邊做邊讀效率高十倍**。

# Learning — 全 repo 學習地圖

> 把散落的學習從點串成線、連成面。這份是**跨主題總覽**。
>
> 方法論看 [`CLAUDE.md`](./CLAUDE.md) 與 [`heptabase-design-research.md`](./heptabase-design-research.md)。
> 這份只回答：**到目前為止學了哪些東西、怎麼歸類、成熟到哪一層。**
>
> 最後更新：2026-05-30

## 我之後怎麼用（日常節奏）

**寫——全部透過 Claude Code（手機/桌面），你不用碰 git：**
- 學到東西 → 說「把這次學的 X 寫成筆記」→ 寫進 `notes/X.md` 並當天 merge 進 main
- 某主題讀熟、有可重用判斷 → 說「把 X 升級成卡片」→ 反推成 `topics/X/`
- 想看全貌 → 說「掃一下 repo 給我看地圖」→ 更新這份 README

**讀——手機 Obsidian 純讀 main：**
- 從這份 `README.md` 看地圖，或從 `topics/<主題>/_start.md` 進某主題
- Graph view 看連結網，Backlinks 看誰引用了當前卡

**看互動知識圖譜（固定網址）：**
- https://atomchung.github.io/Learning/ — 卡片變動後自動重建，手機點開即最新
- 本機檔：`docs/graph.html`（離線也能開）

**心法**：不要在手機 Obsidian 寫（改動回不了 GitHub）。所有寫作走 Claude Code。

## 兩層制（怎麼讀這個 repo）

知識照成熟度分兩層：

1. **筆記層 [`notes/`](./notes/)** — 扁平筆記，學完就進 main。大多數學習在這。
2. **卡片層 [`topics/`](./topics/)** — 值得跨脈絡重用的判斷，才升級成原子卡。

外加 [`archive/`](./archive/README.md)：已棄置的工具實驗（腳本版、app 版）的指路說明。

## 卡片層：已升級的主題

- [`topics/coding-agents/`](./topics/coding-agents/_start.md) — coding agent 的設計權衡（13 張卡 + 2 篇 journey）。核心命題：**harness 比模型更決定體驗**。
- [`topics/msft-openai-super-app/`](./topics/msft-openai-super-app/_start.md) — 投資視角看 Codex super app（起步）。
- [`topics/ai-industry-reading/`](./topics/ai-industry-reading/_start.md) — 用什麼信號判讀 AI 產業（4 張卡 + 1 篇 journey）。隱藏主線：**讀信號，不讀表面數字**。

長文產物：[`compare-coding-agents.md`](./compare-coding-agents.md)。

## 四條主題線（筆記層）

### 線一：Agent 與編程工具的本質
- [agent-context-best-practices](./notes/agent-context-best-practices.md) — agent context 最佳實踐、`/handoff`、SessionStart hook
- [ai-agents-ecosystem-integration](./notes/ai-agents-ecosystem-integration.md) — MCP / A2A / agent 互操作
- [karpathy-autoresearch-grader-analysis](./notes/karpathy-autoresearch-grader-analysis.md) — Karpathy AutoResearch 與 grader 設計
- [skills-workflow-best-practices](./notes/skills-workflow-best-practices.md) — skills 工作流

### 線二：學習系統怎麼設計（元主題）
- `heptabase-design-research.md`（根目錄）— 這套卡片系統的方法論源頭
- [ai-education-research](./notes/ai-education-research.md) — Alpha School AI 教育研究
- [personal-os-from-trading-journal](./notes/personal-os-from-trading-journal.md) — 從交易日誌長出個人 OS
- [personal-os-research](./notes/personal-os-research.md) — 個人 OS 研究

### 線三：AI 產業與投資判讀
> 已升級成卡片層 [`topics/ai-industry-reading/`](./topics/ai-industry-reading/_start.md)（源頭筆記仍留 `notes/`）。
- [model-progress-roadmap](./notes/model-progress-roadmap.md) — 模型進展 + app/基建市場衝擊
- [hugging-face-exploration](./notes/hugging-face-exploration.md) — Hugging Face 2026 + 投資框架
- [agent-os-market-analysis](./notes/agent-os-market-analysis.md) / [agent-os-how-to-build](./notes/agent-os-how-to-build.md) — Agent OS 市場與建法
- [ai-daily-brief-7-episodes](./notes/ai-daily-brief-7-episodes.md) — AI Daily Brief 7 集摘要
- [anthropic-blog-teaching-notes](./notes/anthropic-blog-teaching-notes.md) / [learning-roadmap](./notes/learning-roadmap.md) — Anthropic 部落格教學 + 路線圖
- AI power-user 系列：[roadmap](./notes/ai-power-user-roadmap.md)、[summary](./notes/ai-power-user-roadmap-summary.md)、[user-stories](./notes/ai-power-user-user-stories.md)、[work-companion](./notes/ai-power-user-work-companion.md)

### 線四：應用實驗（做出來的東西，留在分支）
- 台北 AI 活動行事曆（`claude/research-token-usage` 分支）
- [video-prompt-optimization](./notes/video-prompt-optimization.md) — AI 影片 prompt 技巧
- 細節見 [`archive/README.md`](./archive/README.md)

## 從點到面：這個 repo 的隱藏主題

> **這個 repo 真正在學的，是「如何設計一個能把點長成面的學習系統」——而它用自己正在學的東西（agent、harness、skills、投資判斷）來建造自己。**

線二是元主題，線一三四是餵給系統的素材。2026-05 的調整（兩層制、降門檻 merge、收斂工具層）就是為了讓這個系統真的開始複利。

## 下一步

- 線三已起步卡片化（`ai-industry-reading`）；可續拆 recall / headless / 中國開源等累積中判斷
- 線一（agent 工具）筆記也夠厚，是下一個可升級對象
- 持續維持「學完就進 notes/、當天 merge」的低門檻節奏

---

*點是事實，線是理解，面是能在新脈絡中重新召喚的判斷。*

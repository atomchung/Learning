# Personal OS 研究與應用發想

> 概念解析 × 現況盤點 × 個人化需求設計 | 2026 年 4 月

## 一、什麼是 Personal OS？

Personal Operating System（個人作業系統）不是真的作業系統，而是一個**比喻**：把「管理自己的人生」當成一套作業系統來設計。它由原則、習慣、流程、工具組合而成，目的是讓個人在資訊爆炸與多角色生活中保持清晰與專注。

### 1.1 三代演進

| 世代 | 特徵 | 代表 |
|------|------|------|
| **第一代：方法論** | 紙本筆記 + 心智框架 | GTD、Bullet Journal |
| **第二代：模組化工具** | 多 App 拼接成一套系統 | Notion / Obsidian + PARA、Second Brain |
| **第三代：AI 編排層** | Agent 跨工具協作、有持久記憶 | Personal AI OS、Life OS、自建 agent stack |

2026 年的關鍵轉變是從 **App-centric → Agent-centric**：使用者不再「打開哪個 App」，而是「告訴 agent 我要什麼」，agent 跨工具協作完成。

### 1.2 核心組成（共通模組）

幾乎所有 Personal OS 流派都會包含這幾塊：

1. **Capture（擷取）** — 隨時把點子、任務、資訊丟進 inbox
2. **Organize（整理）** — 用框架分類（PARA 最流行）
3. **Plan（規劃）** — 從目標 → 專案 → 週計畫 → 日任務
4. **Act（執行）** — 任務管理、習慣追蹤、時間區塊
5. **Reflect（回顧）** — 日誌、週回顧、月回顧
6. **Knowledge（知識庫）** — 第二大腦、可搜尋、可重用
7. **Relationships（關係）** — Personal CRM、互動紀錄
8. **Health & Finance（健康與財務）** — 量化人生的數據面

---

## 二、主流框架盤點

### 2.1 PARA（Tiago Forte）
四層分類，按「可行動程度」排序：
- **Projects**：有結束日期的具體任務集合
- **Areas**：長期維護的責任領域（健康、家庭、職涯）
- **Resources**：感興趣的主題與素材
- **Archives**：已封存的內容

優點：簡單到能跨任何工具實作。缺點：不告訴你「該做什麼」。

### 2.2 Building a Second Brain（CODE 流程）
**Capture → Organize → Distill → Express**。重點在「為了輸出而整理」，避免成為資訊囤積者。

### 2.3 GTD（David Allen）
經典任務管理：清空大腦 → 釐清下一步 → 按 context 行動。適合工作量爆炸但缺乏優先順序的人。

### 2.4 Life OS / RPG 化系統
把人生當遊戲：屬性值（健康、體能、技能）、每日任務、XP、等級。代表：lifeos-app（GitHub 開源）、Habitica。優點是有趣、可視化。缺點是維護成本高。

### 2.5 Notion / Obsidian「Life OS」模板
社群最常見的具體實作：一個首頁 dashboard 連到所有資料庫（Goals / Projects / Habits / Notes / Journal / Finance）。優點是視覺整合、客製度高。缺點是「裝修」會吃掉很多時間。

### 2.6 第三代：AI-Orchestrated Personal OS
2026 年的新形態：以 Agent 為中心，記憶長期累積，主動建議。
- 例：Mindsera、Reflection.app（AI 日誌）
- 例：Reclaim、Motion（AI 排程）
- 例：自建 Claude/GPT agent + MCP 工具鏈

---

## 三、為「你」這位使用者量身發想

> 推測使用者輪廓：開發者/PM 背景、會寫技術分析文（從 `compare-coding-agents.md` 的書寫風格推斷）、習慣中文輸出、對 AI agent 工具熟悉、在 git 環境工作。如果以下推測有偏差，請修正。

基於這個輪廓，**不適合**的方向先排除：
- 重度視覺裝修的 Notion 模板（維護成本 > 收益）
- 純社交化的 RPG 系統（與工作節奏不合）
- 把所有東西塞進單一 SaaS（缺彈性、被綁架）

**適合的方向**：CLI / Markdown-first、可程式化、以 git 為儲存層、能讓 AI agent 直接操作的系統。

### 3.1 候選應用清單（依重要度排序）

| # | 應用 | 解決什麼痛點 | 預期投入 |
|---|------|------------|---------|
| 1 | **AI 加持的 Daily Note 系統** | 每天散落在腦中的想法、會議、決策沒地方收 | 低 |
| 2 | **Project & Decision Log** | PM 工作中大量決策沒記錄、無法回溯 | 低 |
| 3 | **個人知識庫（Second Brain Lite）** | 看了很多文章但內化不了 | 中 |
| 4 | **AI Reading & Highlight Pipeline** | 收藏一堆文章 / paper 沒消化 | 中 |
| 5 | **個人 CRM** | 工作上認識很多人但記不住 context | 中 |
| 6 | **週回顧 Agent** | 沒有定期回顧，學習無法複利 | 低 |
| 7 | **目標 → 任務分解器** | OKR / 目標常常落地失敗 | 中 |
| 8 | **習慣與健康儀表板** | 量化自己的身心狀態 | 高 |
| 9 | **自動化收件夾**（Email/Slack/PR triage） | 訊息焦慮、注意力碎片 | 高 |
| 10 | **金流與訂閱追蹤** | SaaS 訂閱失控 | 中 |

---

## 四、Top 3 應用的需求發想

### 應用 #1：AI-Augmented Daily Note 系統

**問題定義**
作為開發者/PM，每天會經歷：晨會、技術討論、code review 心得、突發點子、學到的小知識。這些東西如果沒有「便宜的入口」立刻記下，就會永遠遺失。

**核心需求**
- **F1 - 一鍵 capture**：CLI 指令 `note "..."`，附時間戳直接 append 到當天 markdown
- **F2 - 結構化模板**：當天檔案有 fixed sections（Tasks / Meetings / Notes / Wins / Blockers）
- **F3 - 自動分類**：AI 在背景把 inbox 內容打標籤、推薦該歸到哪個 PARA 資料夾
- **F4 - 連結舊筆記**：寫到的關鍵字若曾出現過，AI 自動建議 `[[wikilink]]`
- **F5 - 全文檢索**：CLI 或 TUI 介面快速搜尋
- **F6 - Git 為後端**：所有筆記自動 commit + push，跨機器同步、有 history

**驗收標準**
- 從想法產生到記下 < 5 秒
- 一週後能用自然語言問「我上週對 X 議題的結論是什麼？」並得到正確答案
- 不需要打開任何 GUI

**最小可行版本**
一個 bash script + Claude API + git 自動 commit hook。約一個週末能做完。

---

### 應用 #2：Project & Decision Log

**問題定義**
PM / 開發者每週會做數十個決策（技術選型、優先序調整、需求取捨），但事後常常想不起來「當時為什麼這樣決定？」「有沒有評估過 X 方案？」沒有決策日誌，等於每次都在重新踩同一個雷。

**核心需求**
- **F1 - 決策模板**：每筆決策包含 `context / options / decision / rationale / revisit-date`（類比 ADR 但更輕量）
- **F2 - 專案視圖**：每個 project 一個資料夾，含目標、里程碑、決策清單、retrospective
- **F3 - Revisit 提醒**：到期的決策自動跳出讓你重新評估「事後看是對是錯」
- **F4 - AI 對齊檢查**：寫新決策時，AI 提醒「這跟你三週前的 X 決策有衝突」
- **F5 - 可被 agent 讀取**：當未來的 Claude/agent 接手任務時，能讀懂專案的決策歷史

**驗收標準**
- 每筆決策 < 2 分鐘記錄完
- 季度回顧時能列出「決策正確率」「最常踩的坑」

**最小可行版本**
Markdown 模板 + git + 一個 Claude slash command 用來「新增決策」與「找衝突」。

---

### 應用 #3：週回顧 Agent

**問題定義**
週末有心想回顧但沒結構就懶得做、做了也常流於流水帳。沒有複利效應，等於每週都在原地踏步。

**核心需求**
- **F1 - 自動素材匯總**：週日晚上自動拉出本週的 daily notes、git commits、PR 描述、行事曆事件、決策日誌
- **F2 - AI 草稿**：基於素材生成回顧草稿，分區為 `Wins / Lessons / 未完成 / 下週聚焦`
- **F3 - 提問引導**：AI 主動提出 3-5 個高品質問題（例：「你說 X 任務 stuck，根因是什麼？」）
- **F4 - 主題追蹤**：跨週對比「持續出現的 blocker」「重複的學習主題」
- **F5 - 月度與季度匯總**：自動 roll up 成更高層的回顧

**驗收標準**
- 每週實際完成回顧的比率 > 80%
- 三個月後能清楚說出「我這季的進步在哪、哪些事情我一直沒解決」

**最小可行版本**
一個 cron job + Claude API + 從 git log / Daily Notes 抓素材的 script。輸出一份 markdown 草稿，等你週日打開來編輯定稿。

---

## 五、整體架構建議

如果要把上述應用整合成一套「個人 OS」，我建議這個技術骨架：

```
~/personal-os/
├── inbox/              # 隨手 capture
├── daily/              # YYYY-MM-DD.md
├── projects/           # 一個 project 一個資料夾，含 decisions/
├── areas/              # 長期領域（health, career, finance...）
├── resources/          # 知識庫
├── archive/            # 完工封存
├── reviews/            # 週/月/季回顧
├── people/             # 個人 CRM
└── .claude/            # agent 設定、slash commands、CLAUDE.md
```

**關鍵設計原則**
1. **Markdown + Git first**：純文字、可 grep、可 diff、永遠不會被廠商鎖死
2. **AI as augment, not replacement**：AI 幫整理、提問、摘要；決策權永遠在你
3. **CLI > GUI**：每個操作都應該有 CLI 入口，方便組合與自動化
4. **單一儲存源**：避免資料散落在 5 個 SaaS。所有結構化資料都在這個 repo
5. **漸進式建構**：不要一次建滿。先從 Daily Note 開始用兩週，再加下一塊
6. **可讓 agent 直接操作**：用 Claude Code / MCP，把這個 repo 當 agent 的工作空間

---

## 六、下一步建議

選一條路徑開始：

- **路徑 A：保守起步（推薦）** — 先做應用 #1（Daily Note），用兩週驗證「我會不會持續用」。會用再加 #2 / #3。
- **路徑 B：完整骨架** — 一次建好上面的目錄結構與 Claude slash commands，但只啟用 Daily Note 功能。後續加模組只需加檔案。
- **路徑 C：先設計後實作** — 寫一份「我的 Personal OS 規格書」，把目標、原則、範圍鎖死再開工。適合規格控的人。

如果你願意告訴我更多 context（你的角色、現在用什麼工具、最痛的點是什麼），我可以把這份發想收斂成「下週就能動工」的具體實作計畫。

---

## 參考來源

- [Personal AI OS: The Future of Your Digital Life in 2026 — Infocareer](https://www.infocareerindia.com/personal-ai-os-the-future-of-your-digital-life-in-2026/)
- [Personal Operating System — personalos.info](https://personalos.info/)
- [The PARA Method — Tiago Forte / Forte Labs](https://fortelabs.com/blog/para/)
- [Building a Second Brain — Summary](https://summaries.com/blog/building-a-second-brain)
- [Life OS in Notion — maray.ai](https://www.maray.ai/posts/life-os)
- [LifeOS Open-Source RPG Personal OS — GitHub](https://github.com/lifeos-app/lifeos)
- [How to Build a Personal Operating System — allfnan](https://www.allfnan.com/2025/04/how-to-build-personal-operating-system.html)
- [AI Operating System for Personal Productivity 2026 — Motyl](https://motyl.dev/news/ai-operating-system-personal-productivity-2026)
- [Best AI Journaling Apps 2026 — mylifenote.ai](https://blog.mylifenote.ai/the-8-best-ai-journaling-apps-in-2026/)
- [Personal AI Agents Guide 2026 — EduCBA](https://www.educba.com/personal-ai-agents/)
- [Monica — Open-source Personal CRM](https://www.monicahq.com/)
- [Obsidian for Developers — Sam Julien](https://www.samjulien.com/get-started-with-obsidian-as-a-developer/)
- [Structured Daily/Weekly Notes in Obsidian — DEV](https://dev.to/michalbryxi/structured-dailyweekly-notes-in-obsidian-2n5h)

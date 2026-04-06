---
title: "Coding Agent 比較分析：Codex vs Antigravity vs Claude Code"
date: "2026-04-05"
tags: ["ai-tools", "coding-agents", "product-management", "harness"]
related: []
summary: "從產品經理視角比較三大 AI 編程代理的架構、定價與 Harness 設計哲學"
flashcards:
  - q: "什麼是 Harness？"
    a: "包裹在 LLM 外面的運行時編排層，負責工具調度、上下文管理、安全護欄和記憶持久化"
  - q: "同一個模型搭配不同 Harness 的效能差異有多大？"
    a: "基礎 harness 得 42%，優化後的 harness 得 78%——Harness 的影響遠大於換模型"
  - q: "Codex 的核心架構特色是什麼？"
    a: "雲端容器 + 非同步編排，每個任務在獨立雲端容器中執行，無網路存取"
  - q: "Antigravity 的三面架構是什麼？"
    a: "編輯器 + 終端 + 瀏覽器，agent 可跨三者操作"
  - q: "Claude Code 的 TAOR 循環是什麼？"
    a: "Think → Act → Observe → Repeat，每步都可被用戶中斷或修正"
  - q: "三家產品在「即時性 vs 吞吐量」上各做了什麼取捨？"
    a: "Codex 犧牲即時性換吞吐量；Antigravity 兩者兼顧但不極致；Claude Code 犧牲吞吐量換即時性"
  - q: "為什麼說 Harness 比 Model 更重要？"
    a: "模型能力趨同，harness 工程成為差異化關鍵。Harness 決定了工作流和能力天花板"
---

> 產品經理視角 | 2026 年 4 月

## 一、產品定位總覽

| 維度 | OpenAI Codex | Google Antigravity | Claude Code |
|------|-------------|-------------------|-------------|
| **一句話定位** | 雲端非同步編程代理 | Agent-first 全功能 IDE | 終端原生編程助手 |
| **產品形態** | ChatGPT 內建 + CLI + macOS App | 獨立 IDE（VS Code fork） | CLI 工具 + Web + IDE 外掛 |
| **底層模型** | codex-1 / GPT-5-Codex | Gemini 3.1 Pro（也支援 Claude/GPT） | Claude Opus 4.6 / Sonnet 4.6 |
| **執行環境** | 雲端沙箱（無網路） | 本地沙箱 + 編輯器內建 | 本地終端（直接存取檔案系統） |
| **上市時間** | 2025 年中 | 2025 年底 | 2025 年初 |

## 二、架構與技術路線比較

### OpenAI Codex — 雲端非同步模式
- 每個任務在**獨立雲端容器**中執行，任務期間**無網路存取**
- 透過 GitHub 存取程式碼，完成後提交 PR
- 支援**多任務平行處理**（同時跑多個 agent）
- 任務耗時 1–30 分鐘，適合「交辦後去做別的事」
- 缺點：無法即時互動、無法存取私有 API/內部服務

### Google Antigravity — Agent-first IDE
- **三面架構**（Three-Surface Architecture）：編輯器 + 終端 + 瀏覽器，agent 可跨三者操作
- 內建 16 個專業 agent、40+ 領域技能、11 個預設指令
- **Manager View** 可同時編排多個平行 agent
- **Artifact 機制**：agent 產出任務清單、截圖、瀏覽器錄影等可驗證產物
- 本地沙箱隔離（macOS Seatbelt / Linux nsjail）
- SWE-bench Verified 得分 76.2%（截至 2026 年 4 月最高之一）

### Claude Code — 終端原生
- 直接在終端運行，完整存取本地檔案系統、shell、git
- 用自然語言描述需求 → 自動規劃步驟 → 讀寫檔案 → 跑測試 → 提交
- 修改前會**請求用戶確認**（人機協作模式）
- 支援 MCP（Model Context Protocol）擴展能力
- 5 小時滾動視窗的 rate limit 機制

## 三、目標用戶與使用場景

| 場景 | Codex | Antigravity | Claude Code |
|------|-------|------------|-------------|
| **個人開發者日常開發** | 中 | 高 | 高 |
| **團隊協作/企業級** | 高（已整合 ChatGPT Enterprise） | 高（SSO、資料駐留） | 高（Team/Enterprise 方案） |
| **非同步批量任務** | 最強 | 中 | 低（需手動） |
| **即時互動式開發** | 弱 | 強 | 最強 |
| **前端/視覺開發** | 低 | 最強（內建瀏覽器） | 低 |
| **Vibe Coding（探索式）** | 中 | 最強 | 高 |
| **CI/CD 自動化** | 高（Automations 功能） | 中 | 中（需配 hooks） |
| **既有工具鏈整合** | 中（綁 GitHub） | 高（VS Code 生態） | 最高（原生終端） |

## 四、定價策略比較

| 方案 | OpenAI Codex | Google Antigravity | Claude Code |
|------|-------------|-------------------|-------------|
| **免費方案** | 無獨立免費 | Preview 期間免費（最慷慨） | 有限 Sonnet 存取（無 Code） |
| **入門付費** | $20/月（ChatGPT Plus 含 30-150 訊息/5hr） | ~$20/月 Pro（預計） | $20/月 Pro |
| **重度使用** | $200/月（Pro，300-1500 訊息/5hr） | $249.99/月 AI Ultra | $100/月 Max 5x、$200/月 Max 20x |
| **企業** | ChatGPT Enterprise | ~$40-60/用戶/月 | $150/月 Premium 席位 |

### 定價洞察
- **Codex** 綁定 ChatGPT 訂閱，對既有用戶邊際成本最低
- **Antigravity** Preview 免費策略激進搶市，但正式定價後 AI Ultra $249.99/月 引發用戶反彈
- **Claude Code** Max 20x 方案（$200/月）對重度開發者來說實質無限量

## 五、Harness 深度解析

### 什麼是 Harness？

Harness 是包裹在 LLM 外面的**運行時編排層**，負責：
- 工具調度（讀寫檔案、跑終端指令）
- 上下文管理（什麼時候壓縮、什麼時候遺忘）
- 安全護欄（權限控制、沙箱隔離）
- 記憶持久化（跨 session 維持進度）

一個關鍵數據：**同一個模型，搭配基礎 harness 得 42%，搭配優化後的 harness 得 78%**——harness 的影響遠大於換模型。

### 三家 Harness 架構對比

| 設計維度 | Codex 選擇 | Antigravity 選擇 | Claude Code 選擇 |
|---------|-----------|-----------------|-----------------|
| **即時性 vs 吞吐量** | 犧牲即時性換吞吐量 | 兩者兼顧但都不極致 | 犧牲吞吐量換即時性 |
| **隔離性 vs 靈活性** | 最高隔離（無網路容器） | 中等（本地沙箱） | 最低隔離（直接存取檔案系統） |
| **自動化 vs 可控性** | 全自動，跑完才看結果 | 半自動，Artifact 可中途審查 | 每步確認，最大控制權 |
| **廣度 vs 深度** | 廣（多任務平行） | 廣（多 agent + 多面） | 深（單任務深度推理） |

### PM 視角：Harness 比模型重要的啟示

1. **選工具時不要只看「用什麼模型」**——Antigravity 用 Opus 4.6 不等於 Claude Code 的體驗
2. **Harness 決定了工作流**——雲端非同步、IDE 多 agent、終端互動是三種完全不同的工作方式
3. **Harness 決定了天花板**——context window 限制、thinking 限制、工具存取範圍，都是 harness 層的決策
4. **未來競爭的主戰場是 harness，不是模型**——模型能力趨同，harness 工程成為差異化關鍵

## 六、結論：不是誰最好，是誰最適合

| 如果你是... | 推薦 |
|------------|------|
| 已用 ChatGPT 的團隊，想批量自動化 | **Codex** |
| 想要一站式 IDE + 多 agent 體驗的全端團隊 | **Antigravity** |
| 重度終端用戶，需要精準互動式開發 | **Claude Code** |
| 預算敏感、想先試用 | **Antigravity**（免費 Preview）或 **Claude Code**（Pro $20） |
| 企業級安全合規最優先 | **Codex**（沙箱隔離）或按需評估 |

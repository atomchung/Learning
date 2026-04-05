# Coding Agent 比較分析：Codex vs Antigravity vs Claude Code

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
| **API/按量計費** | $1.75/1M input、$14/1M output + 容器費 | 信用額度制（$25/2,500 credits） | 依模型 token 計價 |
| **計費模式** | 訊息數 + 容器費 | 訂閱 + 信用額度 | 5 小時滾動視窗 token 額度 |

### 定價洞察
- **Codex** 綁定 ChatGPT 訂閱，對既有用戶邊際成本最低
- **Antigravity** Preview 免費策略激進搶市，但正式定價後 AI Ultra $249.99/月 引發用戶反彈
- **Claude Code** Max 20x 方案（$200/月）對重度開發者來說實質無限量，API 按量計費則適合企業精算成本

## 五、產品經理關鍵決策框架

### 選 Codex 的理由
1. 團隊已在 ChatGPT 生態系內，邊際成本低
2. 需要非同步批量處理大量任務（issue triage、PR 生成）
3. 安全性要求高——雲端沙箱無網路存取，隔離最徹底
4. 需要 Automations 自動回應 CI/CD 事件

### 選 Antigravity 的理由
1. 需要完整 IDE 體驗，不想在多工具間切換
2. 前端/全端開發，需要 agent 操作瀏覽器驗證
3. 團隊想用 Google 生態（GCP、Firebase 整合）
4. 需要多 agent 平行編排能力
5. Preview 期間零成本試用

### 選 Claude Code 的理由
1. 開發者偏好終端工作流，不想離開現有工具鏈
2. 需要最強的即時互動式編程體驗
3. 對程式碼理解和意圖推斷能力要求最高
4. 需要 MCP 擴展連接內部系統
5. 偏好「人機協作」而非「全自動」模式

## 六、風險與限制

| 風險維度 | Codex | Antigravity | Claude Code |
|---------|-------|-------------|-------------|
| **供應商鎖定** | 中（綁 OpenAI + GitHub） | 高（整個 IDE 遷移成本高） | 低（終端工具，可替換） |
| **離線可用性** | 無（純雲端） | 部分（本地 IDE，但需網路呼叫模型） | 部分（需網路呼叫模型） |
| **資料隱私** | 程式碼上傳至雲端容器 | 本地執行，但 prompt 送至雲端 | 本地執行，但 prompt 送至雲端 |
| **學習曲線** | 低（ChatGPT 介面） | 中（新 IDE 概念） | 低（熟悉終端即可） |
| **生態成熟度** | 高 | 中（仍在 Preview） | 高 |

## 七、結論：不是誰最好，是誰最適合

| 如果你是... | 推薦 |
|------------|------|
| 已用 ChatGPT 的團隊，想批量自動化 | **Codex** |
| 想要一站式 IDE + 多 agent 體驗的全端團隊 | **Antigravity** |
| 重度終端用戶，需要精準互動式開發 | **Claude Code** |
| 預算敏感、想先試用 | **Antigravity**（免費 Preview）或 **Claude Code**（Pro $20） |
| 企業級安全合規最優先 | **Codex**（沙箱隔離）或按需評估 |

---

*產出日期：2026-04-05*

### 參考來源
- [Introducing Codex | OpenAI](https://openai.com/index/introducing-codex/)
- [Introducing upgrades to Codex | OpenAI](https://openai.com/index/introducing-upgrades-to-codex/)
- [OpenAI Codex Pricing 2026 | TokenCost](https://tokencost.app/blog/openai-codex-pricing-api-cost)
- [Build with Google Antigravity | Google Developers Blog](https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/)
- [Google Antigravity Review 2026 | VibeCoding](https://vibecoding.app/blog/google-antigravity-review)
- [Google Antigravity: The Agentic IDE | Index.dev](https://www.index.dev/blog/google-antigravity-agentic-ide)
- [Claude Code Pricing 2026 | Morph](https://www.morphllm.com/claude-code-pricing)
- [AI Coding Agents 2026 Comparison | Lushbinary](https://lushbinary.com/blog/ai-coding-agents-comparison-cursor-windsurf-claude-copilot-kiro-2026/)
- [Claude Code vs Antigravity | DataCamp](https://www.datacamp.com/blog/claude-code-vs-antigravity)
- [Codex vs Claude Code | Builder.io](https://www.builder.io/blog/codex-vs-claude-code)

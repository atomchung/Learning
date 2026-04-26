---
type: starting-point
topic: msft-openai-super-app
created: 2026-04-26
last-updated: 2026-04-26
status: expanding
---

# 起點：MSFT × OpenAI 能否在工作領域兌現「超級應用」承諾？

> 投資視角的主題。市場訊號、第三方驗證、自己動手測的結果先塞進這張卡，等某個論點累積到能單獨講完整故事再拆卡。

## 當下的核心問題

1. **MSFT × OpenAI 的協作，能否在生產力／企業工作領域再創佳績？**
   - 平台 × 模型乘積敘事是否成立，還是另一輪 PR talk？
2. **目前個人判斷：MSFT 產品開發慢、Copilot 滲透低、先發但浪費。**
   - 這個判斷會被什麼證據翻轉？要追蹤什麼指標？

## 已拆出的卡

尚未抽卡（讓起點卡先膨脹）。

## 還沒拆但累積中的發現

### 結構性論點（多頭）
- swyx 認為被低估的是「Codex 變身超級應用後台」的佈局，不是 GPT-5.5 本身
- Codex 不再是產品名，而是 Copilot 後台的 agent 執行層，跨 Office / GitHub / Teams / Foundry
- 真正護城河三件套：Microsoft Graph（統一資料平面）+ Entra（身份系統）+ 組織意志
- 模型是消耗品，分發才是結構性護城河

### 平台機制（已成立的部分）
- VM 是 ephemeral，記憶搬到 VM 外的編排層
- 六層記憶：L1 工作 / L2 對話 / L3 用戶 / L4 專案（AGENTS.md）/ L5 組織（Graph）/ L6 模型權重
- 多人偏好衝突解法：scope 分層 + 越具體越優先 + 個人不污染共享層

### 為什麼 Spud 才動、不是 5.4
- 5.4 是 vertical 專才（Codex 內強），super app 要 cross-surface 通才
- 真正瓶頸：90% 可靠性閾值 + 長 horizon 連貫性 + always-on 成本
- 多步任務指數衰減：80% × 30 步 = 0.12% 成功率；99% × 30 步 = 74%
- 失敗成本不對稱：成功省 30 分、失敗賠 60 分，80% 變異過大
- 同日全線部署本身就是「模型穩到敢押」的訊號

### 反方論點（要平衡）
- Copilot 自 2023 已 ship 多年，DAU 一直被質疑——先發優勢可能被高估
- 最常見隱藏失敗模式：seat 賣得多、實際用得少
- 過去多次 Copilot 推廣雷聲大雨點小（Recall 召回事件）
- 模型迭代節奏（Spud / Opus 4.7 / DeepSeek V4）進入混沌期，6 個月內可能再被超車

### Google 反例（為什麼有零件 ≠ 有超級應用）
- 沒有對應 Graph 的統一資料平面，API 各自獨立
- DeepMind / Workspace / GCP 三王國未對齊
- 沒有 AGENTS.md 對等物，L4-L5 記憶層基本空
- 身份系統較弱，agent 不敢動

## 下一步可能要拆的卡

- [ ] `codex-as-super-app-backend` — Codex 從產品名變執行層
- [ ] `distribution-is-the-moat` — 分發即護城河，模型是消耗品
- [ ] `90-percent-reliability-threshold` — 為何 80% 不夠、要等 90%
- [ ] `chained-task-decay-math` — 多步任務指數衰減的硬限制
- [ ] `failure-cost-asymmetry` — 失敗成本不對稱讓 always-on 門檻提高
- [ ] `graph-as-unified-data-plane` — Microsoft Graph 是 super app 真差異
- [ ] `google-workspace-execution-gap` — 同樣零件因組織問題拼不起來
- [ ] `seat-vs-dau-gap` — 企業 AI 的隱藏失敗模式
- [ ] `model-stability-over-strength` — 平均能力 vs worst-case 變異的優先級

## 驗證計畫（追蹤節奏）

### 30 天（5/26 前）
- Spud 獨立 benchmark（SWE-bench、GAIA、BFCL）
- Power user 實測（swyx、simonw、NLW、goodside、Ethan Mollick）
- 證偽訊號：Spud 比 5.4 只漲 2-3%

### 90 天（7/26 前）
- GitHub Copilot Coding Agent 公開 PR merge rate（期望 >60%）
- 第三方企業 case study（非 MSFT 自家 demo）
- 自己動手測：Word PRD → Coding Agent 開 PR；Excel 分析 → agent 修後端
- 這是敘事最強的現實檢驗點

### 6 個月（10/26 前）
- MSFT FY26 Q2/Q3 earnings 對 Copilot DAU 的揭露字眼
- Gartner / a16z enterprise AI report 的 seat vs DAU 差距
- ChatGPT Enterprise vs M365 Copilot 預算是否互相蠶食

### 12 個月（2027/4 前）
- Google 是否真把 DeepMind / Workspace / GCP 對齊
- Anthropic Claude Code 商業化軌跡
- 模型版本是否進入更穩節奏

## 敘事死亡訊號（任一發生需重寫論述）

1. MSFT 對 Copilot 口風從進攻轉防守（不再敢同日全線推下個版本）
2. Google 在 6 個月內補上對等的 Workspace Super App
3. Spud 撐不過 6 個月就被 Spud-Plus / GPT-6 取代（代表沒真解決 worst-case）

## 相關白板（未來可能開的主題）

- `coding-agents`（同 repo，技術視角；從工具選擇切入）
- `anthropic-business-model`（待開，反方）—— Claude Code 能不能撐起估值
- `model-stability-vs-strength`（待開）—— 模型市場新軸線
- `enterprise-ai-procurement-psychology`（待開）—— seat vs DAU 心理學

---
type: starting-point
topic: coding-agents
created: 2026-04-05
last-updated: 2026-07-18
status: expanding
---

# 起點：我想理解 coding agent 的設計權衡

> 這張卡片不會被寫完——它是一塊磁鐵，所有新讀到的東西先塞進來，等看出子概念時再拆成獨立的原子卡。

## 當下的核心問題
- 三家（Codex / Antigravity / Claude Code）為什麼做出完全不同的設計選擇？
- 背後的權衡是什麼？什麼情境下誰最適合？
- 「模型相同，harness 不同，結果天差地遠」——這個判斷的證據有多強？

## 已拆出的卡（24 張）

### 基礎定義
- [harness-four-layers](./cards/harness-four-layers.md) — Harness 由四個子系統組成
- [harness-beats-model](./cards/harness-beats-model.md) — Harness 的影響大於換模型

### 三家的設計選擇
- [codex-no-network-sandbox](./cards/codex-no-network-sandbox.md) — Codex 用即時性換隔離性
- [antigravity-three-surface-architecture](./cards/antigravity-three-surface-architecture.md) — 三面架構讓 agent 取得視覺感知能力
- [claude-code-human-in-loop](./cards/claude-code-human-in-loop.md) — 每步確認是哲學不是妥協
- [claude-code-six-layer-memory](./cards/claude-code-six-layer-memory.md) — 六層記憶是對 agent 失憶問題的回應
- [precompile-to-local-index-not-restuff-context](./cards/precompile-to-local-index-not-restuff-context.md) — 記憶勝負手＝預編譯本地索引、按需 page-in，不重塞 context（2026-06-21 週綜合）
- [mcp-as-extensibility-lever](./cards/mcp-as-extensibility-lever.md) — MCP 把擴展性變成外部開放
- [artifact-verifiable-output](./cards/artifact-verifiable-output.md) — Artifact 把 agent 產出變人類可審查

### 權衡與範式
- [latency-throughput-tradeoff](./cards/latency-throughput-tradeoff.md) — 即時性與吞吐量是零和權衡
- [isolation-vs-flexibility-tradeoff](./cards/isolation-vs-flexibility-tradeoff.md) — 隔離性與靈活性負相關
- [async-vs-sync-agent-paradigm](./cards/async-vs-sync-agent-paradigm.md) — 非同步 vs 同步是兩種工作範式

### 戰略與衍生
- [model-capability-capped-by-harness](./cards/model-capability-capped-by-harness.md) — 模型能力被 harness 設上限
- [harness-is-the-new-battlefield](./cards/harness-is-the-new-battlefield.md) — Harness 是下一階段競爭主戰場
- [claude-md-as-project-contract](./cards/claude-md-as-project-contract.md) — CLAUDE.md 是 agent 與專案之間的契約介面
- [layered-context-beats-catch-all](./cards/layered-context-beats-catch-all.md) — context 該按需分層載入，不是塞進單一 catch-all 檔（2026-07）
- [orchestration-as-a-model-vs-neutral-harness](./cards/orchestration-as-a-model-vs-neutral-harness.md) — 把 orchestration 內化成模型，是對「harness 中立可換」的反論（Sakana Fugu，2026-06-22）
- [workflow-lifts-floor-model-sets-ceiling](./cards/workflow-lifts-floor-model-sets-ceiling.md) — 工作流墊地板、模型抬天花板，價值與模型強度成反比（2026-07-17 Fable）
- [topology-decides-agent-collab-medium](./cards/topology-decides-agent-collab-medium.md) — Agent 協作媒介由拓撲決定：對等走 git、主從同機才走共享終端（2026-07-18 tmux-bridge）

### 怎麼測 agent（eval 手藝，2026-06→07）
- [agent-eval-scores-end-state-not-path](./cards/agent-eval-scores-end-state-not-path.md) — Agent eval 以終態評分，不綁標準路徑
- [eval-bottleneck-is-criteria-not-tooling](./cards/eval-bottleneck-is-criteria-not-tooling.md) — Eval 的瓶頸是寫判準，不是工具，所以個人也能搞
- [eval-speed-is-its-own-axis](./cards/eval-speed-is-its-own-axis.md) — eval 的驗證速度是獨立一軸，和判準品質分開算（2026-07）
- [one-sided-checks-drift-the-system](./cards/one-sided-checks-drift-the-system.md) — 檢查只設單側，系統就往單側漂（eval×預測帳×自評三脈絡，2026-07-05）
- [eval-tests-judgment-triage-not-correctness](./cards/eval-tests-judgment-triage-not-correctness.md) — eval agent 判斷測的是「交派紀律」不是正確性（三層：機械可判下沉 engine／軟判斷交 judge／不可靠改成問，2026-07-08）

## 還沒拆但累積中的發現
- Antigravity 為 Gemini 深度優化，其他模型是「適配」——可能該拆卡
- 5 種 context 壓縮策略細節（時間清理/摘要/記憶提取/歷史摘要/截斷）
- PM 視角：選工具不該只看底層模型
- 定價策略與商業模型的相互牽引
- 冷啟動成本 vs 常駐成本的隱藏費用結構

## 下一步可能要拆的卡
- [ ] `antigravity-is-gemini-native` — 第一方優化 vs 第三方適配的結構性差距
- [ ] `context-compression-is-active-forgetting` — 上下文管理本質是選擇性遺忘
- [ ] `platform-vs-product-in-ai-tools` — MCP 衍生的平台哲學
- [ ] `trust-accumulation-in-agents` — 人機協作中的信任建立機制
- [ ] `task-routing-between-agents` — 什麼任務該給哪種 agent

## 相關白板（未來可能開的主題）
- `ai-security` — 沙箱隔離、權限動態放行、prompt injection
- `human-ai-collaboration` — 信任累積、每步確認、Artifact
- `llm-productization` — Harness 戰場、模型商 vs 平台商
- `async-work-patterns` — 非同步範式不只適用 agent，也適用人

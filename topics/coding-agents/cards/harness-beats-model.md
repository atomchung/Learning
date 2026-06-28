---
type: card
title: Harness 的影響大於換模型
aliases: [harness > model, 包裝比模型重要]
tags: [harness, llm, agent-design]
appears-on:
  - coding-agents
  - llm-productization
  - future-of-ai-competition
created: 2026-04-05
---

# Harness 的影響大於換模型

**一句話**：同一個模型，搭配基礎 harness 得 42%、搭配優化 harness 得 78%，harness 的工程效益超過換一整代模型。

## 為什麼重要
這個判斷一旦成立，會改變三件事：
1. **選工具的標準**：不該先看「底層是什麼模型」，而該看「harness 設計」
2. **投資方向**：模型能力趨同後，harness 才是真正的差異化戰場
3. **使用者策略**：換模型的邊際效益小於學會一套 harness 的深度

## 證據
- 同模型 + 不同 harness = 42% → 78% 的 benchmark 差距
- Opus 4.6 在 Antigravity 被壓到 1% thinking token、200K context → 同一模型不同 harness 體驗天差地遠
- **賣鏟人自己背書（2026-06）**：Google I/O Extended Taipei，Gemini DevRel 主張「競爭力不在誰會 call model，而在誰會把 model / retrieval / agent / event flow 組成能工作的系統」——賣 model 的一方淡化 model，是利益相反方的第三方再驗證（見 [gemini-api-platform-shift](../../../notes/gemini-api-platform-shift.md)）
- **Cursor＝活教材（2026-06）**：Composer 到 2.5 都是「商品化開源底模（Kimi K2.5，裸底 CursorBench 36 分）+ Cursor 的 continued-pretrain + 大規模 RL → 61.3（+70%）」。優勢不在底模、在 RL/harness/產品迴圈。其「Composer 3 從零預訓練」是想往下 game 進預訓練層，未經中立第三方證明前存疑（見 [cursor-spacex-xai-composer3](../../../notes/cursor-spacex-xai-composer3.md)）
- **公開榜可對照的第三方實測（2026-06）**：Terminal-Bench 上 **GPT-5.5 同一個模型** 上榜兩次——Codex CLI harness 內 83.4%、Terminus 2 harness 內 78.2%，**harness 獨佔 5.2 個百分點**（公開榜可驗，Endor Labs「Agent Security League」交叉驗證同模型換包裝排名翻轉）。這把本卡從「單一 benchmark 數字」升級成「公開榜可對照」。
- **只改編輯介面就讓 15 個模型同時變強（2026-06，HN 實測）**：給每行 code 加 hash 前綴行定址（模型用 hash 指位、不做字串比對），15 個不同 LLM 在 code-edit benchmark 同時漲 5–14 個百分點、輸出 token 降約 20%。harness 的招式不挑模型。
- **產業把「harness」正名（2026-Q2）**：OpenAI 推「Model-Native Harness」（2026-04-15）、微軟 Agent Framework 1.0 GA 把「Agent Harness」當預設基建（2026-04-03）。命名都強調 harness 要跟模型綁定（model-native）——選方案的新判準＝它給你「可換模型的解耦編排層」（可移植、效能打折）還是「與特定模型 co-trained 的 harness」（效能高、鎖定）。

## 反例與質疑
- 這個數字來自單一 benchmark，泛化性待驗證
- Harness 的優勢可能隨模型能力提升而縮小（聰明模型對 harness 依賴度降低）——**但 2026-06 反證**：在 GPT-5.5 這種前沿模型上 harness 差距仍有 5.2pt，縮小尚未發生
- 「同模型」這前提在實務上很少純粹（通常 provider 會對自家 harness 優化）

## 連結
- ← 支持 [codex-no-network-sandbox](./codex-no-network-sandbox.md)（harness 決定天花板的例子）
- ← 支持 [claude-code-human-in-loop](./claude-code-human-in-loop.md)（harness 決定互動範式）
- → 推論 [agent-competition-will-shift-to-harness](./agent-competition-will-shift-to-harness.md)（待寫）

## 出處
- compare-coding-agents.md §六
- [Harness engineering | OpenAI](https://openai.com/index/harness-engineering/)
- [Effective harnesses | Anthropic](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- Terminal-Bench 2.1 harness 分析（2026-06-11）：https://codex.danielvaughan.com/2026/06/11/terminal-bench-2-1-june-2026-benchmark-landscape-codex-cli-harness-engineering-model-scores/ ｜公開榜 https://www.tbench.ai/leaderboard/terminal-bench/2.0
- hash 行定址讓 15 模型同漲（HN 2026-06）：https://news.ycombinator.com/item?id=46988596
- 產業正名 harness：OpenAI Model-Native Harness（2026-04-15）、MS Agent Framework 1.0 GA（2026-04-03）
- 來源：2026-06-28 Q2 情報掃描（並行子 agent，詳見 inbox 同日條目）

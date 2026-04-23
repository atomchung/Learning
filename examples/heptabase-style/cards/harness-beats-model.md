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

## 反例與質疑
- 這個數字來自單一 benchmark，泛化性待驗證
- Harness 的優勢可能隨模型能力提升而縮小（聰明模型對 harness 依賴度降低）
- 「同模型」這前提在實務上很少純粹（通常 provider 會對自家 harness 優化）

## 連結
- ← 支持 [[codex-no-network-sandbox]]（harness 決定天花板的例子）
- ← 支持 [[claude-code-human-in-loop]]（harness 決定互動範式）
- → 推論 [[agent-competition-will-shift-to-harness]]（待寫）

## 出處
- compare-coding-agents.md §六
- [Harness engineering | OpenAI](https://openai.com/index/harness-engineering/)
- [Effective harnesses | Anthropic](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

---
type: card
title: 模型能力被 harness 設上限
aliases: [harness caps model, model-harness ceiling]
tags: [harness, model-performance, product-strategy]
appears-on:
  - coding-agents
  - llm-productization
  - model-provider-strategy
created: 2026-04-05
---

# 模型能力被 harness 設上限

**一句話**：Opus 4.6 在 Antigravity 裡被限制為 1% thinking token、200K context——同一個模型在不同 harness 下可達到的能力完全不同，harness 是模型能力的「天花板設定者」。

## 這個現象的深層意義
- 對**使用者**：「我用 Claude」不是一句完整的技術描述，必須說「我用哪個 harness 裡的 Claude」
- 對**模型商**：釋出給第三方 harness 時，自己是沒有控制權的；第三方 harness 是自家產品的競爭者
- 對**harness 商**：你可以用別家模型，但永遠會對自家模型做最深優化

## 為什麼 Antigravity 會這樣設定 Opus
- 資源競爭：thinking token 很貴，給第三方模型就少給 Gemini
- 戰略差異化：確保 Gemini 在自家 IDE 體感最好
- 不是技術限制，是**產品決策**

## 反向推論
如果你是模型商，應該做的事：
1. 自己做 harness（Anthropic 有 Claude Code、OpenAI 有 Codex）
2. 把對模型要求高的能力（thinking、long context）鎖進自家 harness
3. 給第三方 harness 「夠用但不極致」的版本

## 連結
- ← 是 [[harness-beats-model]] 的關鍵證據
- → 衍生出 [[model-provider-must-own-harness]]（待寫）
- ↔ 對比 [[mcp-as-extensibility-lever]]：開放 vs 鎖定的兩種策略

## 出處
- compare-coding-agents.md §六、Antigravity Harness 劣勢

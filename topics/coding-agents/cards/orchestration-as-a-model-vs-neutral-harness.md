---
type: card
title: 把 orchestration 內化成模型，是對「harness 中立可換」的反論
aliases: [orchestration-as-a-model, 協作邏輯該住哪, Sakana Fugu 賭注]
tags: [harness, agent-design, multi-agent, llm-productization]
appears-on:
  - coding-agents
  - agent-collab-infra
created: 2026-06-22
freshness: 2026-06
---

# 把 orchestration 內化成模型，是對「harness 中立可換」的反論

**一句話**：multi-agent 協作邏輯可以不住在中立 harness（用戶可換模型），而被訓練進一個 meta-model 當產品賣——Sakana Fugu 用 7B conductor 路由一池 LLM、只開一個 API，就是這個賭注；它測試「協作的價值最終住哪」。

## 為什麼重要

「harness 影響大於換模型」隱含一個前提：**協作/編排邏輯住在 harness 這個中立、可換、用戶可控的層**。一旦 orchestration 能被訓練進模型、包成單一 API 賣，這個前提就被挑戰：

1. **價值歸屬移位**：協作的好處被吸進「賣 orchestration 的產品/模型廠」，而不是留在用戶可自建的 harness。
2. **選工具標準變了**：不再是「我配哪個 harness」，而是「我買誰家的 orchestrator-model」——又回到被廠商鎖定。
3. **這是 harness-beats-model 的對沖線**：不是推翻它，是劃出它失效的邊界——當 harness 本身被商品化成模型時。

## 核心權衡（真正的測試點）

用 Fugu 這類產品的人，是因為哪一種？

- **便利財**：省了自己搭 harness 的工。→ harness 仍可被自建取代，原判斷不變，這只是打包服務。
- **真實力差**：比「自搭 harness + 直連前沿模型」更強或更便宜。→ 才真的證明 orchestration 該被模型化、值得買。

觀察指標：留存與定價能不能撐過「自己搭一套也不難」的替代壓力。

## 反例與質疑

- 跑分全是 Sakana 自報（SWE Bench Pro 73.7、GPQA-D 95.5…），無第三方驗證——「更強」這前提本身未證實。
- 7B conductor 只是路由器，重活還是那池被呼叫的大模型——所以它賣的可能就是「便利財」，不是新能力。
- 「不受美國出口管制」是行銷核心，但若它路由的池子裡含美系模型，受限地區還用不用得到？＝可能的話術破口。

## 連結

- ↔ 對比 [harness-beats-model](./harness-beats-model.md)（那張說協作邏輯住中立 harness；這張說它可能被吸進模型，是其邊界條件）
- ↔ 對比 [cursor-spacex-xai-composer3](../../../notes/cursor-spacex-xai-composer3.md)（中立 harness 被「收購」吃掉；本卡是被「模型化」吃掉——同方向兩種吃法）
- ← 支持 [llm-call-niches-are-features-not-companies](../../ai-industry-reading/cards/llm-call-niches-are-features-not-companies.md)（orchestration 是否撐得起獨立產品，同一個生態位天花板問題）

## 出處

- `notes/sakana-fugu-orchestration-as-model.md`
- Sakana AI Fugu 發表（2026-06-22）：sakana.ai/fugu-release；ICLR 2026 論文 TRINITY + Conductor
- Fox Hsiao Threads 貼文（2026-06-22）

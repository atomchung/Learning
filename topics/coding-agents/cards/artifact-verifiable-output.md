---
type: card
title: Artifact 是把 agent 產出變人類可審查的橋梁
aliases: [artifact, verifiable output, 可驗證產物]
tags: [antigravity, human-ai-interface, verification]
appears-on:
  - coding-agents
  - human-ai-collaboration
  - agent-safety
created: 2026-04-05
---

# Artifact 是把 agent 產出變人類可審查的橋梁

**一句話**：Antigravity 讓 agent 產出任務清單、截圖、瀏覽器錄影等 Artifact，把「看 diff」升級成「看結果」，是把 agent 產出變人類可審查的關鍵抽象。

## 為什麼 diff 不夠
傳統 agent 產出 = diff：
- 你要有能力讀 diff 才看得懂
- 你要自己跑起來才知道結果
- 信任成本高、審查摩擦大

Artifact 產出 = 結果：
- 截圖直接看對錯
- 錄影看互動流程
- 任務清單看推理步驟

## 這個抽象的可遷移性
Artifact 不只適用 coding agent——任何 agent 都能受益：
- Research agent → Artifact = 引用來源清單 + 摘要對照表
- Design agent → Artifact = mockup 比較圖
- Analytics agent → Artifact = 圖表 + 查詢語句

## 反面
- Artifact 本身可能誤導（截圖看起來對但 state 有問題）
- 產 Artifact 有成本，小任務得不償失
- 人類可能過度信任「看起來對」的結果

## 連結
- ← 依賴 [antigravity-three-surface-architecture](./antigravity-three-surface-architecture.md)（沒有瀏覽器面就沒有截圖）
- → 引出 [trust-accumulation-in-agents](./trust-accumulation-in-agents.md)（Artifact 是信任累積的介質）

## 出處
- compare-coding-agents.md §二、§六 Antigravity Harness

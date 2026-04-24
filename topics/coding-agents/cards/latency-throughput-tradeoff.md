---
type: card
title: Agent 的即時性與吞吐量是零和權衡
aliases: [latency vs throughput, 即時性吞吐量]
tags: [tradeoff, agent-design, universal-principles]
appears-on:
  - coding-agents
  - async-work-patterns
  - system-design
created: 2026-04-05
---

# Agent 的即時性與吞吐量是零和權衡

**一句話**：越能即時回饋的 agent（Claude Code 每步確認），平行度越低；越能平行擴展的 agent（Codex 30 容器同開），即時性越差——這是架構層級的零和。

## 為什麼是零和
即時回饋需要：
- 模型「等」用戶輸入 → 吞吐量下降
- 單線程狀態維持 → 無法並行
- 緊密人機循環 → 一次只能做一件事

平行擴展需要：
- 完全自動化 → 犧牲中途糾錯
- 無狀態容器 → 犧牲跨任務記憶
- 批量排程 → 犧牲即時交互

## 有沒有中間解？
Antigravity 嘗試走中間路線（多 agent 編排 + Artifact 可審查），但兩邊都不極致。**這不是工程問題，是物理約束**——人的注意力有限，agent 越多越無法即時關注每一個。

## 決策意義
選工具前先問自己：
- 我的任務適合「開出去就好」還是「邊做邊調」？
- 我的注意力容量能管幾個 agent？
- 錯了的修復成本是高還是低？

## 連結
- ← 是 [codex-no-network-sandbox](./codex-no-network-sandbox.md) 和 [claude-code-human-in-loop](./claude-code-human-in-loop.md) 為什麼不可兼得的根本原因
- → 衍生 [async-vs-sync-agent-paradigm](./async-vs-sync-agent-paradigm.md)（更大的範式問題）

## 出處
- compare-coding-agents.md §六、Harness 設計的核心權衡

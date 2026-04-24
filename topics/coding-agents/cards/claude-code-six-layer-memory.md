---
type: card
title: 六層記憶架構是對 agent 失憶問題的回應
aliases: [claude-code memory, 6-layer memory]
tags: [claude-code, memory, context-engineering]
appears-on:
  - coding-agents
  - agent-architecture
  - context-engineering
created: 2026-04-05
---

# 六層記憶架構是對 agent 失憶問題的回應

**一句話**：Claude Code 用 CLAUDE.md、session memory、git history、progress file 等六層資訊讓新 session 不從零開始，核心命題是「agent 的價值不在單次產出，而在跨 session 累積」。

## 被解決的問題
Agent 的經典痛點：每次對話像失憶——你花十分鐘跟它解釋專案結構，下次還要重來。六層記憶是對這個痛點的工程化回應。

## 六層分別是什麼
1. CLAUDE.md（專案級規則）
2. Session memory（本次對話）
3. Git history（版本脈絡）
4. File system state（當下檔案）
5. claude-progress.txt（跨 session 進度）
6. MCP state（外部工具狀態）

## 對應設計哲學
記憶越多層 ≠ 越好，關鍵是**召回時機的精準度**。Claude Code 的 5 種 context 壓縮策略就是在解這個召回問題。

## 反例與質疑
- 層數越多，出錯面也越大（某一層髒資料會污染判斷）
- 重度依賴 CLAUDE.md 會讓團隊之間風格分化
- 記憶召回仍是模型的責任——六層只是材料

## 連結
- ← 是 [harness-four-layers](./harness-four-layers.md) 的「記憶持久化」子系統的實作
- → 引出 [claude-md-as-project-contract](./claude-md-as-project-contract.md)（CLAUDE.md 本身是一種契約介面）

## 出處
- compare-coding-agents.md §六、Claude Code Harness

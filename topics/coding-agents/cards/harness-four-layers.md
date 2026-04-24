---
type: card
title: Harness 由四個子系統組成
aliases: [harness anatomy, harness 的四層]
tags: [harness, agent-design, definitions]
appears-on:
  - coding-agents
  - agent-architecture
created: 2026-04-05
---

# Harness 由四個子系統組成

**一句話**：Harness = 工具調度 + 上下文管理 + 安全護欄 + 記憶持久化；不是單一層，而是四個獨立但耦合的子系統。

## 為什麼這個拆法重要
當你看到兩個 agent 的差異時，拆到這四層可以精準定位原因，而不是模糊地說「harness 不同」：
- **工具調度**：能叫起哪些工具、怎麼選、怎麼並行
- **上下文管理**：什麼時候壓縮、摘要、遺忘
- **安全護欄**：權限、沙箱、什麼動作要確認
- **記憶持久化**：跨 session 的狀態怎麼存

## 應用這個框架看三家

**工具調度**
- Codex：容器內工具
- Antigravity：多 agent + 三面架構
- Claude Code：本地 + MCP

**上下文管理**
- Codex：任務級
- Antigravity：IDE session
- Claude Code：5 策略 + 6 層記憶

**安全護欄**
- Codex：無網路隔離
- Antigravity：本地沙箱
- Claude Code：每步確認

**記憶持久化**
- Codex：弱（任務獨立）
- Antigravity：IDE state
- Claude Code：claude-progress.txt

## 連結
- ← 被 [harness-beats-model](./harness-beats-model.md) 引用作為「harness 是什麼」的定義
- → 衍生出 [isolation-vs-flexibility-tradeoff](./isolation-vs-flexibility-tradeoff.md)（安全護欄層的權衡）

## 出處
- compare-coding-agents.md §六.什麼是 Harness

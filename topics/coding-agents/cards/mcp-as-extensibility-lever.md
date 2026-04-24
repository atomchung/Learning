---
type: card
title: MCP 把擴展性變成外部開放而非內建全能
aliases: [mcp, Model Context Protocol, 擴展性]
tags: [claude-code, mcp, platform-strategy]
appears-on:
  - coding-agents
  - platform-strategy
  - agent-architecture
created: 2026-04-05
---

# MCP 把擴展性變成外部開放而非內建全能

**一句話**：Claude Code 用 MCP 把「連接任何外部系統」開放給第三方寫 adapter，不試圖自己內建所有整合——這是平台 vs 產品的根本選擇。

## 對比：三種擴展策略

**內建全能（Antigravity）**
- 自帶瀏覽器、多 agent
- 優勢：開箱即用
- 劣勢：難以支援長尾需求

**雲端限定（Codex）**
- 只連 GitHub
- 優勢：簡單可控
- 劣勢：內網無解

**協議開放（Claude Code + MCP）**
- 第三方可寫 adapter
- 優勢：長尾需求可解
- 劣勢：品質參差

## 為什麼 MCP 是 Claude Code 的獨門武器
- 終端原生 + MCP = 可連公司內網服務（Jira、Slack、內部 DB）
- Antigravity 的 IDE 耦合讓它難做這件事
- Codex 的沙箱則是從架構上就禁止

## 深層賭注
MCP 在賭「沒有單一 agent 能滿足所有人」，因此把差異化外包給 ecosystem。這跟 iOS App Store 的哲學一樣——自己做平台，讓別人做長尾應用。

## 反面
- MCP server 品質無保證
- 安全邊界模糊（連外部服務代表什麼權限給了 agent？）
- 對一般用戶上手門檻高

## 連結
- ← 是 [harness-four-layers](./harness-four-layers.md) 中「工具調度」層的擴展策略
- ↔ 對比 [model-capability-capped-by-harness](./model-capability-capped-by-harness.md)：開放 vs 鎖定兩種策略
- → 引出 [platform-vs-product-in-ai-tools](./platform-vs-product-in-ai-tools.md)（待寫）

## 出處
- compare-coding-agents.md §六、Claude Code 優勢

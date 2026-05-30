---
type: card
title: Agent OS 的真值是強迫結構化，不是跨工具
aliases: [agent os 批判, 跨工具是賣相, 結構化才是本質]
tags: [ai-industry, agent-os, productization]
appears-on:
  - ai-industry-reading
  - coding-agents
created: 2026-05-30
---

# Agent OS 的真值是強迫結構化，不是跨工具

**一句話**：「跨 Codex / Claude / Gemini」是 Agent OS 的賣相，但真正在做的事是「強迫你把 identity / context / guardrails 分檔」——如果你的設計已經結構化，它的邊際價值很有限。

## 為什麼重要
- 多數人黏一個生態系、很少頻繁換 harness，所以「跨工具」被講過頭。
- 真正有用的是：把 5000 字 system prompt 拆成可 diff、可 review、可版本控的結構化檔案。
- 「7 層」是課程結構不是工程架構——Anthropic 官方只強調 3 件事（CLAUDE.md routing / Skills 能力 / MCP 連線）。4 層（Identity+Context / Skills / Memory / Connections）就夠。

## 反例與質疑
- 對真的在多 harness 間切換的重度用戶，跨工具可攜性是實打實的價值。
- 「強迫結構化」對紀律好的人是多餘，但對多數人是有效的腳手架——不能因為對你沒用就說它沒價值。

## 連結
- ↔ 對比 [claude-md-as-project-contract](../../coding-agents/cards/claude-md-as-project-contract.md)（CLAUDE.md 已涵蓋結構化的多數價值）
- ← 支持 [benchmark-saturation-hides-real-gap](./benchmark-saturation-hides-real-gap.md)（同屬「拆穿被包裝過頭的說法」）

## 出處
- notes/agent-os-market-analysis.md §一、§二
- notes/ai-daily-brief-7-episodes.md §2

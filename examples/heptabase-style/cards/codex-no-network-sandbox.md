---
type: card
title: Codex 的無網路沙箱用即時性換隔離性
aliases: [codex sandbox, 無網路容器]
tags: [codex, sandboxing, security, trade-off]
appears-on:
  - coding-agents
  - ai-security
  - async-work-patterns
created: 2026-04-05
---

# Codex 的無網路沙箱用即時性換隔離性

**一句話**：Codex 每個任務跑在無網路的雲端容器裡，這讓它成為隔離性最強的 agent，但代價是犯錯無法中途修正、無法存取私有 API。

## 核心權衡
- **得到**：資料外洩風險趨近於零、可大規模平行（30 容器 = 30 倍吞吐）、用戶非同步工作
- **失去**：即時回饋循環、跨任務脈絡、私有服務存取、冷啟動開銷高

## 為什麼是設計決策而不是 bug
把這個特徵當 bug 會誤解整個產品——**Codex 不是想做「更好的 Claude Code」，而是在賭「非同步批量」會成為 agent 的主流工作形態**。如果這個賭對了，隔離性會是最大賣點；如果賭錯了（即時互動才是主流），它會很吃虧。

## 適用 vs 不適用情境
- ✅ 適用：企業合規、issue triage、PR 批量生成、CI 自動化
- ❌ 不適用：需要打內網 API、需要看瀏覽器渲染、探索式開發

## 連結
- ← 是 [[harness-beats-model]] 的案例：harness 決定天花板
- ↔ 對比 [[claude-code-human-in-loop]]：兩者是光譜兩端
- → 引出 [[async-vs-sync-agent-paradigm]]（待寫）

## 出處
- compare-coding-agents.md §六、Codex Harness 小節

---
type: card
title: 非同步與同步是兩種 agent 工作範式
aliases: [async vs sync agent, 非同步同步範式]
tags: [agent-design, work-patterns, paradigm]
appears-on:
  - coding-agents
  - async-work-patterns
  - future-of-work
created: 2026-04-05
---

# 非同步與同步是兩種 agent 工作範式

**一句話**：三家 coding agent 背後其實是兩種世界觀——agent 該像「外包包商」（交辦後等結果）還是「即時助理」（邊做邊談），這不是功能差異而是工作範式的根本分歧。

## 兩種範式的核心差異
| | 非同步範式（包商） | 同步範式（助理） |
|---|------------------|----------------|
| 代表 | Codex | Claude Code |
| 互動 | 開單 → 等交付 | 對話 → 邊做邊調 |
| 錯誤處理 | 事後退回重做 | 當下攔截修正 |
| 適合任務 | 定義清楚、範圍封閉 | 探索式、邊界不明 |
| 人類認知模式 | 管理模式 | 共創模式 |

## 為什麼同一個人會需要兩種
- 早上：同步 + Claude Code 解一個難 bug（高互動）
- 下午：非同步 + Codex 批次跑 10 個 PR review（低互動）
- 晚上：Antigravity 做 UI 調整（視覺驗證）

**不是選一個用一輩子，而是**看任務特性切換。

## 範式的歷史類比
- 前 GPT-4：所有 AI 都是「補全」範式——你輸入、它輸出、結束
- GPT-4 後：「對話」範式興起——來回多輪
- Agent 時代：**同步（對話延伸）和非同步（交辦延伸）兩條線並行**

## 連結
- ← 被 [[latency-throughput-tradeoff]] 物理性地制約
- ↔ 和 [[claude-code-human-in-loop]] 互為前提（同步範式需要人在迴路中）
- → 引出 [[task-routing-between-agents]]（什麼任務該給哪種 agent）

## 出處
- compare-coding-agents.md §三、§六

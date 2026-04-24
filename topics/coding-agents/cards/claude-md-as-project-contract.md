---
type: card
title: CLAUDE.md 是 agent 與專案之間的契約介面
aliases: [claude.md, project contract, 專案契約]
tags: [claude-code, memory, convention]
appears-on:
  - coding-agents
  - team-conventions
  - agent-architecture
created: 2026-04-23
---

# CLAUDE.md 是 agent 與專案之間的契約介面

**一句話**：CLAUDE.md 不只是「給 agent 看的說明書」，而是一份**會被精讀、會被遵守、會被團隊爭論的契約**——它讓「agent 行為」變成專案的公開約定，而不是每個使用者各自的私人設定。

## 為什麼這個視角重要
把 CLAUDE.md 當「設定檔」會失去它真正的價值。它其實有三重角色：
1. **對 agent**：每次 session 的行為規範
2. **對團隊**：共享的工作流約定（像 .editorconfig 但管的是 AI）
3. **對自己**：強迫把隱性偏好顯性化

## 寫 CLAUDE.md 的副作用
真正寫一份 CLAUDE.md 會逼你回答：
- 這個 repo 的工作流是什麼？
- 什麼決策要問、什麼可以自己做？
- 測試/lint/commit 的標準是什麼？

**這些問題就算沒有 agent 也該有答案，agent 只是把答案逼出來的觸媒**。

## 風險
- 過度限制 → agent 變死板
- 過度放任 → agent 風格漂移
- 團隊不同意 → CLAUDE.md 變內戰戰場

## 連結
- ← 是 [[claude-code-six-layer-memory]] 中最外層（專案級）的實作
- ↔ 類比 README.md（給人看的） vs CLAUDE.md（給 agent 看的）
- → 引出 [[agent-convention-vs-human-convention]]（待寫）

## 出處
- Claude Code 文件、本 repo 自身實踐

---
type: card
title: 三面架構讓 agent 取得視覺感知能力
aliases: [three-surface, 編輯器+終端+瀏覽器]
tags: [antigravity, agent-perception, ui-design]
appears-on:
  - coding-agents
  - multi-modal-agents
  - frontend-development
created: 2026-04-05
---

# 三面架構讓 agent 取得視覺感知能力

**一句話**：Antigravity 讓 agent 同時操作編輯器、終端、瀏覽器三個介面，這使它成為唯一能「看見」自己產出結果的 coding agent。

## 為什麼這是關鍵突破
其他 agent 都在「盲寫」——寫完不知道長什麼樣。三面架構讓迴路閉合：
```
寫 code → 跑起來 → 看瀏覽器 → 判斷對錯 → 修
```
這對前端/視覺任務是從 50% 跳到 90% 的差異，不是邊際改善。

## 限制與反面
- 只有前端/視覺相關任務受益明顯，後端任務用處小
- 多面感知 = 多倍 context 消耗
- 「看到」不等於「理解」——截圖語意仍靠模型判讀

## 衍生問題
- 三面夠嗎？要不要加上「資料庫查詢結果面」「API response 面」？
- 這套架構能不能移植到 CLI？（答：很難，終端無視覺）

## 連結
- ← 是 [[harness-four-layers]] 的「工具調度」子系統的極致形態
- ↔ 對比 [[claude-code-six-layer-memory]]：一個往廣走，一個往深走
- → 引出 [[artifact-verifiable-output]]（有了視覺才有可驗證產出）

## 出處
- compare-coding-agents.md §二、§六

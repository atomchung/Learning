---
id: 2026-04-14-claude-code-skills-設計-打造個人學習工作流
title: Claude Code Skills 設計：打造個人學習工作流
date: 2026-04-14
tags: [Claude-Code, 自動化, 工具開發, skills, 開發者體驗]
related: [2026-04-14-個人探索式學習系統設計, 2026-04-14-個人知識圖譜自動化系統設計]
confidence: 4
review_count: 0
last_review: 2026-04-14
source: conversation
---

# Claude Code Skills 設計：打造個人學習工作流

## 摘要
研究 Claude Code 的 skill 機制（SKILL.md + YAML frontmatter），將學習系統包裝成兩個 slash command：/explore（基於興趣推薦新主題）和 /connect（自動總結對話+關聯到過去學習）。設計原則：不要讓用戶手動整理，一切自動化。

## 關鍵問題
- 怎麼建立 Claude Code custom skill？
- skill 的 best practice 是什麼？
- 怎麼讓 skill 跑 shell script？
- 哪些功能該包成 skill 哪些不該？

## 學到的重點
1. Skill = .claude/skills/<name>/SKILL.md，YAML frontmatter 定義行為。2. !backtick 語法可在 skill 載入前執行 shell 注入動態資料。3. disable-model-invocation: true 防止 Claude 自動觸發。4. 從 4 個 skill 精簡到 2 個：/explore + /connect，貼合真實使用流程。5. 關鍵設計：/connect 不問用戶任何問題，全自動從對話擷取。

## 延伸方向
加入 session-start hook 自動跑 /explore;用 context: fork 讓 skill 在獨立上下文執行;探索 skill 之間的串接（/explore 結果自動傳給對話）

@AGENTS.md

# 學習筆記 App

## 專案結構

```
app/
├── content/           # Markdown 學習筆記（含 YAML frontmatter）
├── src/
│   ├── app/           # Next.js App Router 頁面
│   ├── components/    # React 元件
│   └── lib/           # 工具函式（notes.ts 處理 markdown）
```

## 新增筆記

在 `content/` 下新增 `.md` 檔案，使用以下 frontmatter 格式：

```yaml
---
title: "筆記標題"
date: "2026-04-05"
tags: ["tag1", "tag2"]
related: ["other-note-slug"]
summary: "一句話摘要"
flashcards:
  - q: "問題"
    a: "答案"
---
```

## 開發指令

- `npm run dev` — 開發伺服器
- `npm run build` — 建置靜態網站
- `npm run lint` — ESLint 檢查

## 慣例

- 介面語言：繁體中文
- 設計優先：手機螢幕（max-w-lg）
- 內容用 Markdown 撰寫，frontmatter 管理 metadata
- 標籤用於串聯相關主題
- 閃卡用於間隔重複學習

# Learning Repository

個人學習紀錄 repo，透過標籤系統串聯相關主題，搭配閃卡複習加深理解。

## 結構

- `content/` → 裡面是搬到 `app/content/` 的原始筆記（舊位置保留為參考）
- `app/` → Next.js 手機優先的學習筆記 Web App
- 根目錄的 `.md` 檔案是原始學習筆記

## 新增學習筆記

1. 在 `app/content/` 新增 `.md` 檔
2. 加入 frontmatter（title, date, tags, summary, flashcards）
3. `cd app && npm run build` 確認建置成功

## 開發

```bash
cd app
npm install
npm run dev
```

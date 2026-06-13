# RAG vs Karpathy LLM wiki — 個人與團隊的不同走法

> 來源：Karpathy 2026-04 的 LLM wiki gist（爆紅）+ 接續 [gemini-api-platform-shift](./gemini-api-platform-shift.md) 的受管 RAG 脈絡。
> 主線：**知識餵給 LLM，個人和團隊走不同路。預設都不是 RAG，是 wiki；RAG 是規模塞不下時才上的。**

## Karpathy LLM wiki 是什麼

不是工具，是一個**模式**：AI agent 主動維護的純 markdown 知識庫，知識**預先編譯**成 Wikipedia 風格 entity pages、用 `[[links]]` 互連，跨 session 複利。

- 三層：`raw/`（不可變來源）→ `wiki/`（LLM 生成頁）→ `CLAUDE.md`（schema）
- 三操作：ingest（吃新來源）/ query（提問）/ lint（健康檢查）

---

# 個人 wiki

**你要的**：跨 session 複利的個人知識——問過的、學過的能累積，不每次從頭。

**走法**：預設 **wiki，不需要 RAG**。知識預編譯成結構化頁，直接塞進 long context（天花板 ~100K tokens，約 150–200 頁密集文字）。

**這個 repo 就是個人 wiki 的實例**，逐條對應 Karpathy 三層、甚至更細：
- `notes/` → `topics/cards/` = raw → 預編譯 entity pages
- `CLAUDE.md` = schema（**他也正好用 CLAUDE.md**，撞同一設計）
- 原子卡 `[[links]]` / 相對連結 = entity pages 互連
- Claude 讀寫維護 = AI-maintained
- `profile.md` boot/sleep + 遞迴改進 harness = gist 沒有的記憶層

**何時個人才需要 RAG**：你的語料大到 long context 塞不下（個人很少見）。在那之前，RAG 是多餘的工程。

---

# 團隊 wiki（共享）

**多了什麼**：共享的真正瓶頸是**寫入協作 + 維護**，不是**檢索**。

**RAG 需要嗎**：通常**不該從 RAG 起手**——RAG 解的是檢索，對「共享」這個需求**解錯了問題**。

**務實路徑（MVP → 升級）**：
1. **MVP**：共享 git repo + markdown + 一份 `CLAUDE.md` schema，團隊各自用 Claude Code 讀寫、git 同步。= 這個 repo 的多人版。
2. **真要搜大量原文**（會議記錄、PDF、Slack 歷史）才加受管 RAG（Gemini File Search / Glean / Notion AI）。
3. **別**一開始自建向量庫 + 權限系統（過度工程）。

**共享真正的三個難點**（個人 wiki 沒有、RAG 也解不了）：
- **並發寫入**：多人同時讓 AI 改同一 repo → git 衝突 / 知識打架。要約定分工或 PR review。
- **新鮮度**：知識過期誰清？要 lint 機制（repo 的 `freshness` + meta-review 是雛形）。
- **權限**：小團隊通常全開放就好，別過早分層。

一句話：**RAG 讓團隊「搜得到原文」，wiki 讓團隊「共享判斷」。小團隊缺的多半是後者。**

---

## 附 A：RAG 和 wiki 是對立哲學

- **RAG — 即時檢索碎片**：知識留原始文件，每次 query 才切塊檢索重組。**stateless**，每次從頭找。適合大語料、頻繁變動、多使用者、細權限。
- **LLM wiki — 預編譯複利知識**：AI 把來源編譯成 entity pages。**stateful**，知識複利。適合個人 / 小團隊、塞得下 context。

一句話：**RAG 每次重新發現，wiki 讓發現累積。**

## 附 B：三條路線光譜（按資料規模選）

1. **不建，wiki / long context** — 個人 & 小團隊首選
2. **受管 RAG**（Gemini File Search 等）— 要檢索但別自己造（接 [gemini-api-platform-shift](./gemini-api-platform-shift.md)：省工程換失控制權）
3. **自建 RAG**（向量庫 + pipeline，五步：切塊→embed→存→檢索→生成）— 大規模 / 特殊需求才值得。工具：Chroma（輕）/ pgvector（已有 Postgres）。

## 跟既有判斷的咬合

- 接 [claude-code-second-brain-noah-brier](./claude-code-second-brain-noah-brier.md)：那篇講實作（second brain 怎麼用），這篇講路線選擇（個人 vs 團隊、何時 RAG）。Karpathy 是這模式的正名 + 名人錨點。
- 接 [gemini-api-platform-shift](./gemini-api-platform-shift.md)：受管 RAG 是「路線 2」，wiki 是「路線 1」，同一張決策圖的兩端。

## 來源

- [LLM Wiki vs RAG: The Karpathy Concept and Enterprise Reality（Atlan）](https://atlan.com/know/llm-wiki-vs-rag-knowledge-base/)
- [Where RAG Breaks Down: The Karpathy LLM Wiki Alternative（MindStudio）](https://www.mindstudio.ai/blog/karpathy-llm-wiki-pattern-knowledge-base-without-rag)
- [What Is Andrej Karpathy's LLM Wiki?（MindStudio）](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code)

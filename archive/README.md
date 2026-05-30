# archive — 已棄置的工具實驗

工具層在 2026-05 收斂為「卡片 + Obsidian」一套。以下是試過但不採用的承載方式，**程式碼本體仍留在各自分支**，這裡只放指路說明，避免它們在 main 增加維護負擔。

## 腳本版（自動化知識圖譜）
- 分支：`claude/ai-education-research-w3Sop`
- 內容：`scripts/capture_learning.py`（記錄學習）、`generate_graph.py`（建互動式知識圖）、`log_session.py`、`review.py`，外加 `/connect`、`/explore` skills。
- 為何不採用：和 Obsidian 的 graph / backlinks 功能重疊，自建腳本維護成本高。

## Next.js 瀏覽 app 版
- 分支：`claude/design-learning-repo-x9zJw`
- 內容：`app/`（Next.js + flashcard deck + tag 瀏覽 + review 頁）。
- 為何不採用：手機 Obsidian 純讀已滿足瀏覽需求，多養一個前端專案不划算。

## 其他應用實驗（非筆記，是做出來的東西）
- `claude/research-token-usage-Hjtz3` — 台北 AI 活動行事曆（KKTIX → ICS pipeline + GitHub Action）
- `claude/personal-os-research-680e9` — `cloud-record` skill
- `claude/add-demo-mobile-skill` — `demo-mobile` skill

要回顧或復活任一實驗，直接 checkout 對應分支即可。

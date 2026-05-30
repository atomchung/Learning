# ai_project_research — AI 錯誤紀錄


## 2026-05-17 — [verif-fail] Best practice 研究先給建議再對照 repo，順序倒置
- **Why**: 第一輪只給抽象 best practice 原則，未先搜 GitHub 真實 repo（claude-memory-compiler, vectara 等）
- **Fix**: 新流程：研究類任務先派 deep research agent 搜熱門 repo → 對照已知 pattern → 再給建議

## 2026-05-17 — [plan-fail] V3 設計把所有自動化一次上齊，被三方 review 一致砍掉
- **Why**: V3 一次塞 PostToolUse hook + 每週 cluster LLM task + 自動 INDEX 生成，超出個人 < 30 案例規模的合理範圍
- **Fix**: V4 改 ladder 思路：先 manual 紀錄 → 痛點觸發再升級。Prototype 先 30 行 shell，hook 延後

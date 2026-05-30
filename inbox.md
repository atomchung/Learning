---
type: qa-log
note: append-only。隨口疑問 + 當時結論。成熟的判斷會沉澱成卡片並回填連結。
---

# 問答記錄（隨口疑問的落腳處）

> 你隨處丟問題，我接住後記在這。每條 = 一個疑問 + 當時結論 + 狀態。
> 同一話題反覆出現時，profile.md 會把它往上浮；夠成熟就升級成卡片。

## 2026-05-30 — 這套知識系統怎麼對我產生收益？

**疑問**：卡片系統跑了一陣子，感覺沒收益，是哪裡錯了？

**結論**：
- 收益在「取用 / 沉澱判斷」端，不在「累積卡片」端。過去力氣多花在容器上（圖、tunnel、Pages、可視化），沒花在用知識。
- 你真正要的不是手工知識庫，是：**隨口疑問 + AI 回答被整體記錄關聯起來，AI 持續知道你關注什麼，進而持續給你更想要的答案。**
- 硬約束：別處 app 的問題不會自動流進來，需要固定汇流口；「AI 持續記住你」靠每次開場讀 `profile.md`。
- 行動：新增記憶層 `profile.md`（我讀+更新）+ 本 `inbox.md`（隨手記）。卡片系統降為底層，不再是入口。

**狀態**：開放 → 系統入口改造中

**相關**：`profile.md`

## 2026-05-30 — repo 是我的腦，要能存記憶 + 被搜尋

**疑問**：只要我刻意在 Learning repo 問問題，你就能透過 repo 知道我整個記憶、也知道怎麼搜尋——本質上這個 repo 是你的腦，對吧？

**結論**：
- 對，這是最準的心智模型。但要先破一個誤會：**我跨 session 預設零記憶**，聊天本身不是記錄，**寫進 repo 檔案才是**。
- 所以「腦」要運轉需接兩根線：開場自動讀 `profile.md`（boot）、睡前把問答寫回 `inbox.md`+更新 `profile.md`（sleep）。
- 搜尋機制：`profile.md` 當索引 → `grep` 整個 repo → 命中 `inbox.md` / `cards/`。
- 行動：把記憶層的三拍循環寫進 `CLAUDE.md`（契約），讓未來每個 session 都自動 boot/sleep。

**狀態**：✅ 已接線（CLAUDE.md 新增「記憶層」章節）

**相關**：`CLAUDE.md` → 記憶層、`profile.md`

## 2026-05-30 — Salesforce 全公司 agentic 化案例（Claude Code）

**疑問**：研究 Boris Cherny 轉的 Salesforce 案例——231 天遷移 13 天做完、一個 PR 21 個 endpoint、100% 覆蓋。

**結論**：
- 招牌數字（231→13、18x）是**自估反事實基準**，無法獨立驗證，當公關看就好。
- 真正耐看的是兩個**實測**值：每位開發者 merge PR 數 +79%（年對年）、事故率 -5%。讀信號就讀這兩個。
- 真正的故事不是「模型變強」而是**工作流重建**：唯讀 code review agent 進迴圈（APPROVED / WARNINGS / CHANGES REQUIRED，丟回 dev agent 重審）、skills 成為可重用工程資產、全員無限 token。→ 呼應「Harness 影響大於換模型」。
- 工程長自己承認難題：長 session 的 context 管理仍是手藝、模型仍會漂。
- Will 保哥吐槽點出真瓶頸：常在組織摩擦（敢不敢拍板全切、給無限 token、拆舊流程），不在技術。

**狀態**：✅ 已寫筆記

**相關**：`notes/salesforce-agentic-engineering.md`、`topics/coding-agents/cards/harness-beats-model.md`、`ai-industry-reading` 的「讀信號不讀表面數字」

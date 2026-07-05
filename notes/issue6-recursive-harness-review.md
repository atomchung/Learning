# Issue #6「遞迴改進 harness」完整梳理（2026-07-05）

寫作目的：這條線跑了一個月、散在 defects / ledger / inbox / profile 四處，趁 Fable 視窗做一次可接手的完整綜合（`notes/fable-limited-window-strategy.md` 待辦的第 1 條）。本文同時是模型 A/B 實驗的 Fable 版產出。

## 1. 這條線在解什麼問題

起點是 2026-06-06 讀 Anthropic「When AI Builds Itself」後的翻譯題：**模型（Claude）動不了，遞迴自我改進唯一能發生的層是 harness**（CLAUDE.md / profile / 三拍循環 / hook / skill）——這是 harness>model 卡的直接推論。

三階梯定位：L0 線性（只堆 notes）→ L1 迴圈（boot/awake/sleep 記憶層在跑，但規則不變）→ **L2 遞迴（系統依自己的失敗改寫規則本身）**。Issue #6 就是把系統從 L1 推到 L2。

缺的零件是 **loss 信號**：boot-miss、retrieval-miss 這些缺陷以前發生完就蒸發，系統學不到。所以整條線的架構＝「把缺陷存下來（梯度）→ 定期轉成規則修改（更新）」。

北極星（防跑偏用）：**目的是省事，不是跑儀式**。優化目標是「每單位記住的知識、摩擦更低」，不是「更多結構」——能刪規則的 RSI 才是對的 RSI。

## 2. 已落地機制盤點

- `meta/defects.md` — 內部梯度儲存。五類缺陷（boot-miss / retrieval-miss / rot / merge-gap / write-conflict），發生時 append 一行，行尾標 `@user|@claude` 來源。
- `meta/borrowable-patterns.md` — 外部梯度 ledger（B1–B14）。defects 記我們做錯的，這份記別人做對的，兩者都餵 meta-review。含否決存檔（B11 式，防同案重提）。
- `.claude/skills/meta-review/SKILL.md` — L2 轉化迴圈本體：讀梯度→找重複類→R1 防自評閘（動規則前至少一筆 `@user`）→提 ≤3 條修改→反膨脹閘（每加二刪一）→B14 二分呈現（確定的打包、邊界的逐條問）→用戶批准才動 CLAUDE.md。
- CLAUDE.md 三拍鉤子 — 清醒拍 B1（可重用判斷當下主動提議沉澱）、睡前拍 B2（連坑一起記）＋順手記缺陷、升級訊號 B3（≥3 條 inbox 出現才升卡）。
- 三風險應對 — R1 防自評閘 ✅；R2 profile 膨脹→B8 三層瘦身 ✅（profile＝always-load 索引，細節下沉 inbox/notes）；R3 CLAUDE.md 行數 ⚠️ 部分（290→268，目標 <200）。
- 子案 — Issue #7 write-conflict（熱檔寫前 rebase、寫完即 push，2026-07-04 立）；Issue #9 外部掃描漏斗（提案中，待用戶裁）。

## 3. 證據結算：什麼被驗證了

**有效（有可觀察結果）**：

- **首次 /meta-review 真的跑完整迴圈**（2026-07-04）：6 筆缺陷→唯一重複類 write-conflict×2→立第五類＋熱檔規則＋反向砍規則。CLAUDE.md 290→268 行＝結算訊號「實際砍規則、行數下降」**首次達成**。
- **R1 防自評閘拿到第三次實證**：跨 project audit 的 subagent 誤報 investment_note 有 7 個「幽靈工具」，手動核實全部存在——agent 自信地錯，佐證「動規則前要 @user 缺陷」不是儀式。
- **B14 二分試點第 1 次通過**：2 題、用戶全按推薦選、零 triage-miss。
- **缺陷類別選得準的旁證**：write-conflict 新規立規當天，本尊第三次應驗（另一並發 session 撞上）。

**無效／否決（誠實記）**：

- B13「inbox 拆每日檔」❌ ——兩次衝突都是**同日**並發，每日檔根本擋不住；唯一真解（每 session 檔）違反反膨脹，先用縮小撞車窗口頂著。
- 五類 taxonomy 的預測力弱：07-04 歸類發現**發生的缺陷全是原 taxonomy 外的新東西**（false-completion、credibility-miss、env-403、write-conflict 本身）。分類是事後追認的——這說明「預先窮舉缺陷類」價值有限，真正有用的是 append 的習慣本身。

**未決（都掛了驗證訊號）**：

- 熱檔規則是否真減少衝突：write-conflict 至 2026-09 再犯 ≥2 次→升級拆每 session 檔。
- **迴圈本身值不值得**：用戶 07-04 質疑 B 類收益≈0。結算＝2026-09 看再犯數＋用戶主觀是否省事；無感→砍小或降頻。這是整條線的存在性問題，也是最誠實的一條——RSI 線自己也掛在 validation gate 上。
- B9（reflection 先問問題）、B12（機械 lint）提案中未動；false-completion / credibility-miss 各 ×1 觀察中，再犯即立類。

## 4. 張力與未決問題

1. **維護成本 vs 北極星**：迴圈每月要人跑一次、缺陷要記得標，若省下的事少於花掉的，整條線是負資產。裁決已排 2026-09，在那之前**最大的風險是手癢加東西**。
2. **梯度稀疏**：時鐘速度＝使用頻率，一個月只攢 6 筆缺陷；且 @user 標註依賴用戶記得標——梯度品質吃用戶紀律，這是個人系統天花板。
3. **沒有自動 eval**：社群的 harness-evolver（多 agent worktree 自動演化）前提是自動 eval；我們的「eval」是缺陷計數＋用戶主觀。在這之前，L2 的「遞迴」每輪都得人肉閉環。
4. **R3 未償完**：268 行仍超 200 警戒（指令預算研究：超 200 行整塊被忽略）。候選刀口＝檔案格式模板段（~40 行，抽 schema 檔留 pointer）。

## 5. 下一步建議（按優先序）

1. **不動作，讓兩個 validation gate 跑到 2026-09**——現在加機制會污染實驗（write-conflict 再犯數、迴圈值不值得，都在等自然數據）。06-20 已有共識「先別繼續加借鑒點」，維持。
2. **CLAUDE.md 第二刀壓行數**（268→<200）：抽檔案格式模板段。這是「刪規則」方向的正向動作，不違反第 1 條。
3. **B12 機械 lint 進 weekly-synthesis**：零 inference（grep freshness 過期＋驗死連結＋數孤兒卡），把 rot 缺陷從「等給錯答案」變「腳本掃」。加的是腳本不是規則，成本低確定性高。
4. **env-403 根治留給用戶**（雲端環境 network policy 白名單），harness 側緩解已做，別再花力氣。
5. **Issue #9 掃描漏斗維持提案狀態**，等用戶裁節奏；別先建佇列。

## 出處

`meta/defects.md`、`meta/borrowable-patterns.md`、`.claude/skills/meta-review/SKILL.md`、`CLAUDE.md`、`profile.md`（Issue #6 與 meta-review 質疑兩條）、`inbox.md` 2026-06-06（開帳兩條）／2026-06-20（B1–B8 落地）／2026-07-03（B11–B14）／2026-07-04（首次 meta-review、跨 project audit）。

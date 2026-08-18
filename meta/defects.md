# meta/defects.md — harness 缺陷日誌（遞迴改進的梯度儲存）

> 這是「遞迴改進 harness」（Issue #6）的梯度來源。
> 規則只有一條：六類缺陷之一發生時，**append 一行就好**，不拆卡、不長篇。
> 累積的缺陷由 `/meta-review` 定期讀，轉成對 harness（CLAUDE.md / profile / hook / skill）的修改。

**⚠️ 寫入位置**：新缺陷一律 append 到本檔**最末的「日誌」段**。「已消化」段刻意放在前面——2026-08-10 meta-review 查出：已消化段原本在檔尾，導致「append 一行就好」的條目**必然誤落進已消化**，5 筆未消化缺陷因此被埋掉（07-11／07-18／07-20 ×3／08-10）。梯度被檔案結構自己吃掉了。

## 六類缺陷（標在每行開頭）

- `[boot-miss]` 開場讀了 profile 還是漏掉，害用戶重講背景。**也涵蓋寫入端**：某場 session 沒回寫記憶層，導致下游必然漏讀
- `[retrieval-miss]` repo 裡其實有相關 note/卡，但沒撈出來
- `[rot]` freshness 過期卡／手維護數字漂移被當現況用，給了錯答案
- `[merge-gap]` 學完卡在分支、手機讀不到
- `[write-conflict]` 熱檔（profile / inbox / defects）並發寫衝突（2026-07-04 首次 meta-review 立，Issue #7）
- `[credibility-miss]` 拿二手轉述當一手事實，或沒查證就先定調（2026-08-10 第二次 meta-review 立類，3 次觸發）

## 記錄格式

一行：`YYYY-MM-DD [類別] 發生什麼 → 該改 harness 哪裡（可留空，meta-review 補） @user|@claude`

行尾標**誰標的**（`@user` / `@claude`）。誰都能記，但 Claude 自評會漏盲點，**用戶標的最準**（「你剛剛沒撈到 X」）。`/meta-review` 動規則前**至少要有一筆 `@user`**（防自評閘，R1）——全是 `@claude` 自標視為證據不足。

---

## 已消化（meta-review 已轉化成規則）

### 2026-08-10 第二次 meta-review（CLAUDE.md 269 → 261 行，淨刪一段）

**① `credibility-miss` 立為第六類，篩子第四格擴寫成「一手 vs 轉述」（合併，不開第五格）**——3 次觸發，根因是**歸屬錯誤不是可信度誤判**：既有三格管的都是「誰的話可信」，全都預設「這句話是誰說的」已確定。規則寫在 `profile.md` 篩子段。

- 2026-06-20 [credibility-miss] 用戶丟 FB 貼文要我理解 Composer 3，我第一反應判它是「AI 編的假新聞」，web 查證後全真。憑先驗判真假、沒先查證。 @claude
- 2026-08-09 [credibility-miss] 信了合規顧問／資安 vendor 的行銷內容（時薪與年薪那組數字），沒回查官方公報 → EU AI Act 高風險義務其實已被 Digital Omnibus 延到 2027-12-02。**多個獨立來源同時錯，因為共用同一個過期前提**。 @claude
- 2026-08-10 [credibility-miss] 市場評論文章寫「在公司財報後，市場擔心供過於求更久」，我讀成「SanDisk 說供過於求」寫進回覆，**方向講反**——管理層實際定調是結構性稀缺（FY27 供給 >50% 已鎖長約、毛利率指引 83–85%）。是使用者追問「AI 需求這麼旺怎麼會過剩」逼出來的＝**外部 verifier 比自查強**（`verifier-is-a-ladder-not-a-switch` 第三階）。 @user

**② 手維護數字必漂 → 刪掉 `CLAUDE.md` 的「當前 repo 狀態」整段**——07-18 那次只修了 profile/README，**漏了 CLAUDE.md 這第三處，而它是每場 session 第一個讀的契約檔**。查出時已全爛：notes 寫 ~19（實際 70）、coding-agents 寫 13 張卡（實際 25）、topics 寫 2 個（實際 5）。權威留在各 topic 的 `_start.md`，其他地方不複述數字。

- 2026-07-18 [rot] 卡片計數三處漂移（README/profile 18、`_start.md` 22、實際 24），且升卡時沒同步 `_start.md` 卡列表。 @claude
- 2026-07-20 [rot] profile 記混第三方產品版本號（Composer 3 當時根本不存在），連帶讓「第一方模型無第三方驗證」的判斷部分過時。同源：durable 層 prose 寫死會演化的數字必漂。 @claude

**③ 寫入端 boot-miss → CLAUDE.md boot 步驟加 `git log --since=<profile.updated>` 兜底**——不依賴自律，因為漏寫的人可能不是 Claude。

- 2026-08-05→08-09 [boot-miss] 08-05 那場寫了 `notes/product-hunt-agent-services-2026-08.md`（341 行）並 commit 進 main，**但沒更新 profile.md／inbox.md**——睡前三拍只做了「寫 note」沒做「回寫記憶層」。後果：08-09 開機時那場 session 等於不存在，`last-session` 還停在 07-26。**記憶層的斷點在生產者不在消費者。** @user

**④ 本檔結構陷阱修復**：「已消化」段從檔尾移到日誌之前，讓 append 永遠落在日誌尾。5 筆誤歸條目已歸位。

**⑤ ting 裁決：`last-session` 改 append-only 多條列 → 先不改，續觀察。** 理由：本場 rebase 後 fast-forward 成功未撞車；且多條列會讓 profile 長回去，與 B8「permanent memory 保持小」直接衝突。write-conflict 四筆留在日誌續掛。

### 2026-07-20 已即時固化（未經 meta-review，當場落地 CLAUDE.md）

- 2026-07-20 [前沿認知層缺失] 四線掃描全部綁預測帳結算訊號＝只跑產業信號層，**論文層根本不在掃描範圍**；使用者打回「沒有啥新的 AI paper 提升認知嗎」。**使用者重新定義核心（比我的命名準，採用他的）**：不叫 `lens-miss`（我的內部術語），叫「**關注前沿的認知，且這個認知要能幫助更好的決策**」。已固化為 CLAUDE.md 攝取節奏第 4 條「掃外部動態跑兩把篩子」＋`notes/info-intake-routine.md` 新段。補掃後產出 5 條判斷更新＋1 張新卡，證明漏掉的是真東西。 @user

### 2026-07-04 首次 meta-review

下列 2 筆歸戶新類 `[write-conflict]`（原標 merge-gap?），轉化為 CLAUDE.md Git 工作流「熱檔寫前 rebase、寫完立即 push」＋本檔立第五類；Issue #7 裁決收案——不拆 inbox（每日/每月檔擋不住同日並發，兩次衝突都是同日），驗證訊號：至 2026-09 再犯 ≥2 次則升級拆每 session 檔。原文全文見 git history。

- 2026-06-06 [write-conflict] 兩 session 並發改 profile.md / inbox.md，push main 被拒手動解；profile 第 19 行被 git 靜默 auto-merge → 靜默遺失風險。 @user
- 2026-06-20 [write-conflict] 本 session 與 weekly-synthesis session 並發改 profile/inbox，非快轉拒、手動 merge。第二次，達重複門檻。 @claude

### 2026-07-04 手動緩解（未跑 /meta-review，ting 直接核准單行修改）

候選解 (2) 已採用——CLAUDE.md 記憶層加一句「WebFetch/curl 403 別重試：環境白名單制，直接標註降級為搜尋摘要並繼續」。候選解 (1)（根治：使用者去 Claude Code web 環境設定調整 network policy 放寬白名單）**尚未做**，非 harness 層能代勞，留待使用者自行處理。原文全文見 git history。

- 2026-07-04 [env-403] 用戶問「為什麼搜不到」→ 查明 WebFetch/curl 403 是雲端環境自訂白名單制。已採緩解；根治待使用者。 @user

---

## 日誌（append-only — 新缺陷寫這裡，寫在最下面）

2026-06-17 [false-completion?] 三輪對話我都口頭說「補進筆記了」(規模章節/畫地圖方法/Jira 關聯)，實際只在第一輪 Write 過初稿，後三段從未真正寫入檔案——直到 /record 才發現並補上。屬「false completion claim」：報告與實況不符。候選解：說「補進筆記」前後必須有對應 Edit/Write tool call，否則不得宣稱完成。**2026-08-10 meta-review：至今僅 1 次、未再犯，維持候選不立類。** @user

2026-07-04 [merge-gap] session worktree 基於 4 月舊 lineage（compare-coding-agents 分支），檢出裡沒有 .claude/skills → /meta-review unknown command，改手動照 SKILL.md 跑。skill/規則活在 main、舊分支 worktree 讀不到＝harness 版 merge-gap。候選解：worktree session 開場先 rebase origin/main。**2026-08-10 meta-review：僅 1 次、未再犯，維持候選。** @user

2026-07-04 [write-conflict] 本 session（找原文＋env-403 修正）與 meta-review session 並發寫 defects.md，push main 非快轉拒、手動解衝突——**新規「熱檔寫前 rebase」立規當下即第三次應驗**。無資料遺失。計入 Issue #7 驗證帳第 1 次。 @claude

2026-07-09 [write-conflict] 本 session（addyosmani/eval 卡，800+ 分超長）連續多輪寫 inbox/profile 後 push，並發 session 先 merge 進 main → fast-forward 被拒；按 fallback merge，交集僅 inbox.md（append-only），git ort 自動合併、無真衝突、無資料遺失。**計入第 2 次**——但 auto-merge 順利、傷害低於前兩次手動解。另：超長 session 連續寫熱檔時「寫前 rebase」難每輪落實，本次靠 push 時 fetch+merge 兜住。 @claude

2026-07-11 [write-conflict] 本 session（Mercor 筆記）push feature branch 後 merge 進 main，origin/main 已被另一 session 推進；fast-forward 被拒，按 fallback merge，交集僅 inbox.md，單一衝突區塊、位置相鄰，這次 git 未能自動合併，手動解僅是接回兩段順序，無資料遺失。**計入第 3 次**——三次全發生在 inbox.md 且都是同時間窗多 session 寫作，傷害持續輕微。 @claude

2026-07-20 [write-conflict] 本 session（前沿認知掃描）與並行 session 同日同時段寫 profile+inbox。fast-forward 被拒 → merge origin/main，**profile.md 與 inbox.md 皆真衝突、需手動解**。**與前三次的關鍵差異：這次不是 append-only 的位置衝突，而是語意衝突**——兩場都改了 `last-session`（同一個 key、內容完全不同）與同一條話題線，git 既無法也不該自動合併。解法是**合併雙方內容**不是二選一。**計入第 4 次**——**本次推翻了「傷害遞減」的 nuance**：熱檔並發的傷害不是遞減，而是**取決於兩場 session 的主題是否重疊**。**候選解（比拆 inbox 檔更對症）**：`last-session` 從「單一 key 覆蓋」改成 append-only 多條列，或移出 frontmatter 另立 `recent-sessions.md`——衝突根源是「單一 key 被兩場搶著覆蓋」，不是 inbox 太長。**正向觀察**：語意重疊本身是有價值的訊號，merge 時該做的是互相連結而非去重。**2026-08-10 meta-review：ting 裁決先不改、續觀察**（該場 rebase 後 fast-forward 成功；且多條列與 B8「保持小」衝突）。 @claude

2026-08-18 [credibility-miss] 讀產品規格時，看到「處方不得點名買什麼賣什麼」一句就推論「這個 skill 禁止討論標的」，實際上那句的主詞是另一條路線（週度復盤卡），而使用者問的那條路明文**要求** build case for and against。**與 2026-08-10 同型（歸屬錯誤：看到一句話沒先確認主詞是誰），第二次**。當場自查推翻並向使用者更正。候選解：引用規格文件的禁令前，先確認該句的主詞／適用路線，不得跨路線套用。 @claude

2026-08-18 [retrieval-miss] 定位「限制在哪一層」時我答輸入參數層（premise 契約），使用者修正為**入口宣告層**（skill 描述自己能做什麼那段）——那層在讀到任何輸出規則之前就先判出界，是更早生效的限制。我讀過該檔的 frontmatter 卻沒把它當成限制點。**同場第二次由使用者修正定位，外部 verifier 再次比自查強。** @user

2026-08-18 [write-conflict] 本 session（盲評 harness 討論）與並行的 DeepSeek Harness session 同日寫 `inbox.md`。fast-forward 被拒 → merge origin/main，**inbox.md 真衝突需手動解**（兩段都 append 在檔尾、位置相鄰，git 無法自動接）。解法是**兩段都留、按進 main 的時間排序**，無資料遺失。**計入第 5 次**——與 2026-07-20 那次不同：這次是純位置衝突（兩場主題無重疊），傷害輕；`last-session` 的單一 key 語意衝突風險仍在（對方同場也改了 profile.md，本場寫 profile 時須合併不得覆蓋）。 @claude

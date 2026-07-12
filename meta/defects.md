# meta/defects.md — harness 缺陷日誌（遞迴改進的梯度儲存）

> 這是「遞迴改進 harness」（Issue #6）的梯度來源。
> 規則只有一條：五類缺陷之一發生時，**append 一行就好**，不拆卡、不長篇。
> 累積的缺陷由 `/meta-review` 定期讀，轉成對 harness（CLAUDE.md / profile / hook / skill）的修改。

## 五類缺陷（標在每行開頭）

- `[boot-miss]` 開場讀了 profile 還是漏掉，害用戶重講背景
- `[retrieval-miss]` repo 裡其實有相關 note/卡，但沒撈出來
- `[rot]` freshness 過期卡被當現況用，給了錯答案
- `[merge-gap]` 學完卡在分支、手機讀不到
- `[write-conflict]` 熱檔（profile / inbox / defects）並發寫衝突：兩 session 同時寫，push 被拒或被 git 靜默 auto-merge（2026-07-04 首次 meta-review 立，Issue #7）

## 記錄格式

一行：`YYYY-MM-DD [類別] 發生什麼 → 該改 harness 哪裡（可留空，meta-review 補） @user|@claude`

行尾標**誰標的**（`@user` / `@claude`）。誰都能記，但 Claude 自評會漏盲點，**用戶標的最準**（「你剛剛沒撈到 X」）。`/meta-review` 動規則前**至少要有一筆 `@user`**（防自評閘，R1）——全是 `@claude` 自標視為證據不足。

## 日誌（append-only）

<!-- 範例（可刪）：2026-06-06 [retrieval-miss] 問 RSI 時沒主動撈出 eval 生態位筆記 → notes 缺統一 keywords？ -->


2026-06-17 [rot?] 三輪對話我都口頭說「補進筆記了」(規模章節/畫地圖方法/Jira 關聯)，實際只在第一輪 Write 過初稿，後三段從未真正寫入檔案——直到 /record 才發現並補上。屬「false completion claim」：報告與實況不符。四類缺陷沒涵蓋這種「宣稱已寫但沒寫」。候選解：說「補進筆記」前後必須有對應 Edit/Write tool call，否則不得宣稱完成。交 /meta-review 評估是否立第六類「報告-實況落差」。 @user

2026-06-20 [credibility-miss?] 用戶丟 FB 貼文要我理解 Composer 3，我第一反應判它是「AI 編的假新聞」（SpaceX 買 coding 工具、SpaceX IPO 太離譜），差點直接回「這貼文不可信」。實際 web 查證後全真。屬「先驗證再下判斷」沒做就先給結論的傾向——這次靠主動 WebSearch 救回，但若沒查就會給錯答。坑值得記：用戶自己的原則就是「讀信號要先驗真」，agent 不該因「聽起來離譜」就略過查證。四類缺陷沒涵蓋。候選解：遇可查證的事實宣稱（尤其反直覺的）先 WebSearch 再定調，別憑先驗判真假。交 /meta-review 評估。 @claude

2026-07-04 [merge-gap] session worktree 基於 4 月舊 lineage（compare-coding-agents 分支），檢出裡沒有 .claude/skills → /meta-review unknown command，改手動照 SKILL.md 跑。skill/規則活在 main、舊分支 worktree 讀不到＝harness 版 merge-gap。候選解：worktree session 開場先 rebase origin/main。 @user

2026-07-04 [write-conflict] 本 session（找原文＋env-403 修正）與 meta-review session 並發寫 defects.md，push main 非快轉拒、手動解衝突——**新規「熱檔寫前 rebase」立規當下即第三次應驗**（前兩次 2026-06-06、06-20 已歸戶）。無資料遺失；本 session 據新規補做。計入 Issue #7 驗證帳（至 2026-09 ≥2 次則升級拆每 session 檔，本筆為第 1 次）。 @claude

2026-07-09 [write-conflict] 本 session（addyosmani/eval 卡，800+ 分超長）連續多輪寫 inbox/profile 後 push，並發 session（verifiable-component-replay）先 merge 進 main → 我 fast-forward push 被拒；按 CLAUDE.md fallback merge origin/main，交集僅 inbox.md（append-only），git ort 自動合併兩段（append 位置分散）、無真衝突、無資料遺失、無需手動解。**計入 Issue #7 驗證帳第 2 次（前次 2026-07-04）——達「至 2026-09 ≥2 次」門檻**；但本次 auto-merge 順利、傷害低於前兩次手動解，meta-review 評估「拆每 session 檔」時應納此 nuance：門檻達標但傷害遞減，可能不需拆檔、只需固化「push 被拒就 fetch+merge」的兜底。另：超長 session 連續寫熱檔時「寫前 rebase」難每輪落實，本次靠 push 時 fetch+merge 兜住（客觀事件，push 被拒有 git 記錄）。 @claude

## 已消化（meta-review 已轉化成規則）

**2026-07-04 首次 meta-review**：下列 2 筆歸戶新類 `[write-conflict]`（原標 merge-gap?），轉化為 CLAUDE.md Git 工作流「熱檔寫前 rebase、寫完立即 push」＋本檔立第五類；Issue #7 裁決收案——不拆 inbox（每日/每月檔擋不住同日並發，兩次衝突都是同日），驗證訊號：至 2026-09 再犯 ≥2 次則升級拆每 session 檔。原文全文見 git history。

- 2026-06-06 [write-conflict] 兩 session 並發改 profile.md / inbox.md，push main 被拒手動解；profile 第 19 行被 git 靜默 auto-merge → 靜默遺失風險。 @user
- 2026-06-20 [write-conflict] 本 session 與 weekly-synthesis session 並發改 profile/inbox，非快轉拒、手動 merge。第二次，達重複門檻。 @claude

**2026-07-04 手動緩解（未跑 /meta-review，ting 直接核准單行修改）**：候選解 (2) 已採用——CLAUDE.md 記憶層加一句「WebFetch/curl 403 別重試：環境白名單制，直接標註降級為搜尋摘要並繼續」。候選解 (1)（根治：使用者去 Claude Code web 環境設定調整 network policy 放寬白名單）**尚未做**，非 harness 層能代勞，留待使用者自行處理，未來若做了再回頭補記。原文全文見 git history。

- 2026-07-04 [env-403?] 用戶問「為什麼搜不到」→ 查明 WebFetch/curl 403 是雲端環境自訂白名單制（非新變化，inbox/notes 已記 ≥4 次）。已採緩解：CLAUDE.md 加降級規則；根治待使用者。 @user

2026-07-11 [write-conflict] 本 session（Mercor 商業模式筆記）push feature branch 後 merge 進 main，origin/main 已被另一 session（GPT-5.6 caching 筆記,2026-07-10）推進；fast-forward 被拒,按 fallback merge，交集僅 inbox.md（append-only），單一衝突區塊、位置相鄰(兩段緊接同一分隔線後)，這次 git 未能自動合併(不同於 07-09 的自動合併)，手動解僅是接回兩段順序，無資料遺失。**計入 Issue #7 驗證帳第 3 次**（前兩次 07-04 手動解、07-09 自動解）——三次全發生在 inbox.md 且都是同時間窗多 session 寫作，傷害持續輕微（append-only 結構讓手動解幾乎零風險），支持 07-09 已提的 nuance：門檻達標但傷害遞減，可能不需拆檔。 @claude

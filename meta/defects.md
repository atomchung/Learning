# meta/defects.md — harness 缺陷日誌（遞迴改進的梯度儲存）

> 這是「遞迴改進 harness」（Issue #6）的梯度來源。
> 規則只有一條：四類缺陷之一發生時，**append 一行就好**，不拆卡、不長篇。
> 累積的缺陷由 `/meta-review` 定期讀，轉成對 harness（CLAUDE.md / profile / hook / skill）的修改。

## 四類缺陷（標在每行開頭）

- `[boot-miss]` 開場讀了 profile 還是漏掉，害用戶重講背景
- `[retrieval-miss]` repo 裡其實有相關 note/卡，但沒撈出來
- `[rot]` freshness 過期卡被當現況用，給了錯答案
- `[merge-gap]` 學完卡在分支、手機讀不到

## 記錄格式

一行：`YYYY-MM-DD [類別] 發生什麼 → 該改 harness 哪裡（可留空，meta-review 補） @user|@claude`

行尾標**誰標的**（`@user` / `@claude`）。誰都能記，但 Claude 自評會漏盲點，**用戶標的最準**（「你剛剛沒撈到 X」）。`/meta-review` 動規則前**至少要有一筆 `@user`**（防自評閘，R1）——全是 `@claude` 自標視為證據不足。

## 日誌（append-only）

<!-- 範例（可刪）：2026-06-06 [retrieval-miss] 問 RSI 時沒主動撈出 eval 生態位筆記 → notes 缺統一 keywords？ -->

2026-06-06 [merge-gap?] 兩個 session 並發（harness 整合 + Robinhood note）同時改 profile.md / inbox.md，push main 被拒、要手動解衝突。無資料遺失，但 profile 第19行被 git 靜默 auto-merge（這次剛好沒撞）→ 潛在靜默遺失風險。**疑似第五類缺陷「熱檔並發寫衝突」**，四類沒涵蓋。候選解：inbox 拆每日/每 session 檔（append-only 天生免衝突）；profile 保持小 + 寫前 fetch。交 /meta-review 決定要不要立第五類。**追蹤:Issue #7**。 @user


2026-06-17 [rot?] 三輪對話我都口頭說「補進筆記了」(規模章節/畫地圖方法/Jira 關聯)，實際只在第一輪 Write 過初稿，後三段從未真正寫入檔案——直到 /record 才發現並補上。屬「false completion claim」：報告與實況不符。四類缺陷沒涵蓋這種「宣稱已寫但沒寫」。候選解：說「補進筆記」前後必須有對應 Edit/Write tool call，否則不得宣稱完成。交 /meta-review 評估是否立第六類「報告-實況落差」。 @user

2026-06-20 [credibility-miss?] 用戶丟 FB 貼文要我理解 Composer 3，我第一反應判它是「AI 編的假新聞」（SpaceX 買 coding 工具、SpaceX IPO 太離譜），差點直接回「這貼文不可信」。實際 web 查證後全真。屬「先驗證再下判斷」沒做就先給結論的傾向——這次靠主動 WebSearch 救回，但若沒查就會給錯答。坑值得記：用戶自己的原則就是「讀信號要先驗真」，agent 不該因「聽起來離譜」就略過查證。四類缺陷沒涵蓋。候選解：遇可查證的事實宣稱（尤其反直覺的）先 WebSearch 再定調，別憑先驗判真假。交 /meta-review 評估。 @claude

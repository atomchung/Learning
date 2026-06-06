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

一行：`YYYY-MM-DD [類別] 發生什麼 → 該改 harness 哪裡（可留空，meta-review 補）`

誰都能記：Claude 自評會漏盲點，**用戶補的最準**（「你剛剛沒撈到 X」）。

## 日誌（append-only）

<!-- 範例（可刪）：2026-06-06 [retrieval-miss] 問 RSI 時沒主動撈出 eval 生態位筆記 → notes 缺統一 keywords？ -->

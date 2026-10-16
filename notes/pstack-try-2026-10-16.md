# pstack 試用筆記（2026-10-16）

觸發：Threads @ilya.liao 貼文——Uncle Bob（Clean Code）與 Laravel 作者在 X 認可 poteto 的 pstack；推薦 Claude Code/Codex 用戶用社群版 pstack-claude。
**證據層級**：名人背書＝社會信號，不是實測。我們要自己量差異。

## 它是什麼
- poteto（Lauren Tan）的 skill 集：playbook（流程）＋ principles（規則，有穩定 id 如 `unslop`）＋多 agent review。
- 原版在 Cursor plugins（見 [skill-makers 筆記](./skill-makers-matt-pocock-2026-09-30.md)，9/30 已拆過設計手法）。
- 入口 `/poteto-mode`；`/poteto-help` 用白話描述任務、推薦該用哪個指令。
- Claude Code 社群移植（搜尋摘要，未逐一核對 repo）：
  - tedhn/pstack-claude：clone 進 `~/.claude/skills/pstack` 後跑 `/setup-pstack`
  - michael-denyer/pstack-claude：星數最多（~2k），多 harness
  - ericlitman/open-pstack：追 Cursor upstream，`/pstack:poteto-mode`
  - **哪個是貼文說的版本未確認**——裝前先看 repo 最近 commit 與是否追 upstream。

## 怎麼用（試用計畫）
1. 只裝一個 port，先只用 `/poteto-help` + `/poteto-mode`，別一次吃 51 個指令。
2. 挑一個**我做過的真任務**重做一次（A/B）：同題、無 pstack vs 有 pstack。
3. 跟本 repo 的 CLAUDE.md 會不會打架？pstack 也是一套「工作契約」，兩套 router 疊加可能互搶。

## 怎麼感受差異（先寫預測再量）
**我猜**：差異主要在「委派與收尾紀律」（todolist 照 playbook 走、產出寫給下一個 agent、沒實跑就標 draft），不是單次答案品質。
要記的觀察：
- 中途停下問我的次數（變多＝好還是煩？）
- 最後交付物有沒有「實跑驗證」
- token/時間成本
- 有沒有出現我原本會自己補的 slop（`unslop` 是否有感）

## 待結算
- [ ] 試完一個任務後回來填：預測對不對？

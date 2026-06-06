# 量化自己的 harness：從「相信 harness 重要」到「知道我的 harness 多好」

> 2026-06-06。起點：掃完 Learning repo + 本地 agent-loop / eval / memory 系統，問「我們對 AI 自我迭代的認知到哪、沉澱了什麼、怎麼越做越好」。結論收斂到一個我從沒回答的問題：我一直相信 harness > model，卻從沒量過自己的 harness 有沒有在變好。

## 一句話

我的個人 OS（skills + memory + hooks + eval）就是我的 harness。harness 決定天花板，但「天花板有沒有抬高」我一直只憑感覺。要優化它，得先能量它——而量的時候最大的陷阱，是用代理信號冒充真實信號。

## 什麼是「我的 harness」

不是抽象名詞，就是我已經有的四層（對映 coding-agents 卡的四層 harness）：

**1. 工具 / skills 層**
- record、session-board、record-fit、log-strength、eval… 一堆 skill。
- 該量的不是「我有幾個 skill」，是「哪個真的常觸發、觸發後有沒有改變產出」。

**2. 上下文 / 記憶層**
- Stop hook 自動 capture session 進 `_inbox.md`；15 條 feedback；pre_task_feedback hook 每次開口自動召回相關規則。
- 該量的是召回命中率、命中後行為真的改變了嗎、同一個錯有沒有越犯越少。

**3. 護欄 / review 層**
- 三方審查（Codex + Gemini + 自己）、code 改動自動跑 codex review。
- 該量的是 review 攔到的真問題數，相對於誤報。

**4. eval / 迭代層**
- skill_eval（區分行 > 總分）、feedback → CLAUDE.md → 自動化的升級鏈。
- 該量的是區分行從 flaky 變穩的比例、被測出退步又修好的案例數。

## 量 harness 的最大陷阱：代理信號

這是掃完所有系統後浮出的主軸——我在六個不相干的地方，都撞到同一道牆：代理信號會騙人。

| 層 | 別只看（代理信號） | 該追（真實信號） |
|---|---|---|
| skills | skill 數、行數 | 觸發次數、skill_eval 區分行 |
| 記憶 | feedback 條數、inbox 大小 | 召回後行為改變、重犯率 |
| 護欄 | review 跑幾次 | 攔到真問題 / 誤報比 |
| eval | 總分 | 區分行穩定度、退步→修好案例數 |

代理信號的共通毛病：容易量、讓人自我感覺良好、但跟「harness 真的變好了嗎」脫鉤。skill_eval 的「總分灌水」、xhs_autoresearch 的「LLM judge ≠ 真實 view 數」、record-week L2 的「23 題 0 回答」，骨子裡都是同一件事——拿好量的代理，冒充難量的真實。

## 怎麼優化：先補最缺真實信號的那層

量化的目的不是打一個總分，是找出「哪一層只有代理信號、沒有真實信號」，然後補那一層的採集。

**已經有現成真實數據的層（低門檻，先量）**
- `pre_task_feedback.log`：召回命中率（hits>0 的比例）。
- `exploration/skill_eval/runs/`：區分行穩不穩。
- codex review 紀錄：攔到的真問題。
- 這些一個 query 就有，先盤完。

**缺真實信號的層（要補採集，先別硬量）**
- skill 觸發後「有沒有改變產出」沒在記。
- feedback 召回後「行為有沒有真的改」沒在追。
- artifact 的「外部採用」沒在量（呼應已有的 artifact maturity 那條 todo）。

## 反例 / 要小心的

- 別把 harness 量化做成「定時自動產報告要我回應」——time-driven push 對我無效（record-week L2 的教訓）。這該是我想看時 pull，不是系統定時 push。
- 別為了有數字而量代理信號（skill 數、token 花費），那只會製造虛假的進步感。
- 量化本身也有成本。只量「能改變我下一步決定」的指標；量完不會有任何行動的，就別量。

## 下一步（已落 personal_os todo）

最小起步：用現成的三份 log（召回 / skill_eval / codex review）盤一張表——harness 四層各自「現在能量到的真實信號 / 缺的採集點」。盤完才知道第一個該補的採集點在哪，而不是一開始就建一套大儀表板。

## 出處

- 上一輪研究：掃 Learning repo + personal_os skill_eval + memory + 跨專案 agent loop（2026-06-06 session）。
- harness 四層 / harness > model：`topics/coding-agents/`、`notes/salesforce-agentic-engineering.md`。
- 「真實信號 > 代理信號」主軸：skill_eval README「區分行 > 總分」、xhs_autoresearch `RESEARCH_LOG.md`「LLM judge ≠ 真實 view」、feedback `time-driven-push-ineffective`。

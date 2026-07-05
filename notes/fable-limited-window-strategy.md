# Fable 可能隨時被下架：怎麼分配這段有限時間

問題起點：讀完「跟 Fable 找未知」那篇心法後追問——如果之後再也用不了 Fable，該怎麼在有限時間內用好這個模型（找問題/解法/未來方向）？

## 查證：風險有前例，不是假設性焦慮（2026-07-05 查）

Fable 5 是 2026-06-09 首次公開發布的 Mythos-class 模型，Anthropic 目前推理/長任務 agentic 能力最強的通用模型。發布沒幾天，6/12 美國政府因 Amazon 研究員發現的越獄漏洞發出出口管制令，Anthropic **全球下架** Fable 5 與 Mythos 5，停了 18 天，6/30 管制解除、7/1 才重新對外開放。定價 $10/M input、$50/M output（含 90% prompt cache 折扣）。

**結論**：觸發下架的變數（監管/安全事件）不是使用者能控制的，而且已經應驗過一次。這代表「有限視窗」是真實約束，該當成規劃前提，不是杞人憂天。

## 三塊分配框架

1. **找問題（判斷力/盲點）**：把 Fable 用在弱模型做不好的地方——深度 audit、跨主題找矛盾、盲點檢視（呼應 `notes/finding-unknowns-with-claude.md` 的「盲點檢視」招）。產出是「寫下來的問題陳述」，寫完就是持久資產，不需要 Fable 本人執行後續。
2. **解法（拿計畫，不拿執行）**：優先讓 Fable 產出實作計畫/架構決策，機械式重構留給以後任何模型都能做。同構既有判斷：委派契約 + Prompting Inversion（強模型該少約束做判斷型工作，弱模型才該給死板約束跑 execution，`notes/prompting-small-models.md`）。
3. **未來方向（現在做，別延後）**：跨主題綜合/路線圖這種「模型能力差距最大」的工作要現在做完，別想「以後還能問」。

**一句話**：harness > model 判斷的極端版——把 Fable 的產出寫進 repo（notes/cards）才是真正持久的資產，模型本身隨時可能被監管收走。

## 待辦（本機執行，方向先記這裡）

從 `profile.md`「你當前開放的疑問」挑 1-2 條「追蹤中」的長期線，趁 Fable 視窗還在時做一輪深度綜合（而非等 `/weekly-synthesis` 自然排到）。候選（按價值排）：
- 遞迴改進 harness（Issue #6）——最活躍的元線，可能值得一次跨 session/跨 repo 的完整梳理
- loop eng / orchestration 該住 harness 還是被模型化——兩條都在 `check:2026-12`，時間還早但屬於「模型能力差距最大」類

**沒做的原因**：本次先只記方向，深挖留到本機 session 處理。

## 出處

WebSearch（2026-07-05）：Anthropic 官方新聞稿 + VentureBeat + The Hacker News 對 Fable 5 下架/恢復時間線的報導。

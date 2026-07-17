---
type: card
title: 工作流墊地板，模型抬天花板
aliases: [floor vs ceiling, 流程墊地板模型抬天花板, distilled-workflow-caps-at-model-ceiling]
tags: [harness, llm, agent-design, model-capability]
appears-on:
  - coding-agents
  - llm-productization
created: 2026-07-17
---

# 工作流墊地板，模型抬天花板

**一句話**：從強模型蒸餾出的工作流能墊高弱模型的「地板」（不再浪費步驟、不忘驗證、不跳過拆解），但拉不破弱模型自己的「天花板」（最難那步、沒前例的判斷、品味）——所以工作流的價值跟模型強度成反比：幫弱模型最多、幫強模型最少。

## 為什麼重要

「把高手的工作流拆成 skill、換個引擎照跑」這類宣稱會週期性出現（如 `fable-method`：把 Claude Fable 5 的工作流蒸餾成誰都能裝的 skill，兩週衝上千星）。這張卡是拆解它的濾鏡：

1. **它把兩個問題混在一起**——(Q1) 工作流會不會轉移？大致會。(Q2) 模型是不是「只等於」那套流程？不是。用 Q1 的 yes 去證 Q2 就是錯位。
2. **地板 vs 天花板**：流程墊高地板（對弱模型幫助大、對強模型邊際小）；模型抬高天花板（沒有腳本能替代能力）。所以「不是模型贏是流程贏」在大宗任務為真、在前沿任務為假——瓶頸在哪決定誰贏。
3. **可證偽檢定（這卡最可重用的一句）**：若一包 skill 對強模型的幫助跟對弱模型一樣大，它抬的是天花板、不是地板；反過來，幫弱模型遠多於強模型＝坐實它是地板墊高器、不是能力來源。

## 蒸餾為什麼封頂

- **skill 是原模型的有損壓縮**：從「看著它的動作」拆出來，抓得到可寫死的部分，抓不到默會的判斷。你能寫「這裡要驗證」，寫不出「該驗證什麼」的那個判斷。
- **腳本在「該下判斷」的節點有洞**：每個「這裡決定 X」還是跑在底層引擎上，引擎弱、那個節點就弱，外面包再好也補不回。
- **eval 是真正的轉移機關，但威力被 verifier 上限鎖死**：skill 靠「反覆重試直到通過一個標準」墊高弱模型；一旦 eval 本身需要弱模型沒有的判斷力，就退化成 [one-sided-checks-drift-the-system](./one-sided-checks-drift-the-system.md)——裁判跟選手一樣弱，自信的錯答照過。verifier 的上限又回到模型，迴圈漏回能力。

## 類比

說某前沿模型「只是更好的流程」，像說西洋棋大師「只是更好的開局書」。開局書（工作流）真能把業餘者拉高一大截，但大師的本事恰恰是書上沒有的中局——要「看見」的地方。蒸餾開局書，複製不了那個視力。

## 反例與質疑

- **可驗證領域是例外**：當 eval 便宜又可靠（code 過不過測試）且任務在弱模型「重試搆得到」的範圍內，工作流真能把弱模型逼到接近強模型的產出——這時地板墊得很高，天花板顯得沒那麼關鍵。
- **不是所有難題都在「重試距離」內**：有些一步到位的判斷，弱模型重試一萬次也碰不到，這時 eval 迴圈幫不上。
- **與 harness-beats-model 不衝突、是互補**：那張講「墊地板的效益大」（同模型換 harness 42%→78%），這張補「墊到哪為止」——天花板還是模型。兩張合起來才完整。

## 連結

- ↔ 對比 [harness-beats-model](./harness-beats-model.md)：那張講「墊地板的效益大」，這張講「地板墊不過天花板」
- ↔ 對比 [model-capability-capped-by-harness](./model-capability-capped-by-harness.md)：那張是 harness 往下掐模型（產品決策），這張是工作流往上封頂在模型能力（能力本質）——兩種「天花板」來源不同
- ← 支持 [one-sided-checks-drift-the-system](./one-sided-checks-drift-the-system.md)：verifier 跟生成器一樣弱時，蒸餾的品質守門失效

## 出處

- Threads 討論串（2026-07-17，leeunhn vs anzs1152）：`fable-method` skill 宣稱把 Fable 5 工作流拆成弱模型可跑的 skill，兩週衝上千星；原 po 主張「流程贏不是模型贏」，留言反駁「模型來源才是重點」。兩人各對一半＝站在「地板 vs 天花板」曲線的不同段。
- 接本 repo 既有判斷：harness-beats-model、model-capability-capped-by-harness、one-sided-checks-drift-the-system

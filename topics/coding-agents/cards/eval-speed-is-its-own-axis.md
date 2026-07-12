---
type: card
title: eval 的驗證速度是獨立一軸,和判準品質分開算
aliases: [eval 速度也是護城河, fast eval, 判準品質 vs 驗證速度]
tags: [coding-agents, eval, agent-testing, solo-dev]
appears-on:
  - coding-agents
created: 2026-07-10
---

# eval 的驗證速度是獨立一軸,和判準品質分開算

**一句話**:eval 有兩條互不替代的軸——「判準寫得對不對」(理解問題,見 eval-bottleneck 卡)和「一輪驗證跑多快」;後者決定你一天能迭代幾次,而**快速迭代本身就是護城河**,不是判準準了就結束。

## 為什麼重要
- eval-bottleneck 卡把難點放在「寫判準」,那是**單輪品質**。速度是**跨輪頻率**——判準再準,一輪要跑一小時,你一天改不了幾次。
- Farhan Thawar(Cursor Compile 2026,《What Is Your Job Now》):把「產品**驗證速度**」當新護城河——競爭不在誰的 eval 更準,在誰驗證得更快、砍掉錯方向更早。
- Jason Liu(AIE WF 2026,《How to look at your data》):主張 **fast evals + 對話分群**,建輕量高頻迴圈,別靠直覺調 agent。
- 推論:**這條軸個人比大公司好贏**——你不必跑全套 CI,10–20 個 case 的 `tasks.jsonl` 30 秒跑完,迭代速度就是優勢,正好接上 eval-bottleneck「個人能搞」的結論。

## 反例與質疑
- 速度換準度的張力:跑太快通常 case 太少、judge 太糙。**快而錯的 eval 比慢而準更危險**——它讓你自信地往錯方向衝。
- 速度只在「判準已經對」之後才有價值;判準錯,跑再快都是高頻累積錯信號。所以這卡是 eval-bottleneck 的**補充不是取代**。

## 連結
- ↔ 對比 [eval-bottleneck-is-criteria-not-tooling](./eval-bottleneck-is-criteria-not-tooling.md)(那張是「判準品質」軸,這張是「驗證速度」軸——eval 的兩條正交軸)
- → 引出 [agent-eval-scores-end-state-not-path](./agent-eval-scores-end-state-not-path.md)(終態能用 code assert,是「跑得快」的前提)
- ← 支持 [harness-beats-model](./harness-beats-model.md)(快速 eval 迴圈是 harness 層手藝)

## 出處
- notes/three-confs-2026-ai-builder-scan.md(Farhan Thawar / Jason Liu 段)
- Cursor Compile 2026《What Is Your Job Now》; AI Engineer WF 2026《How to look at your data》

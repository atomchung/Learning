---
type: card
title: Eval 的瓶頸是寫判準,不是工具——所以個人也能搞
aliases: [寫判準是理解問題, eval 不能外包, 個人能搞 agent eval]
tags: [coding-agents, eval, agent-testing, solo-dev]
appears-on:
  - coding-agents
created: 2026-06-04
---

# Eval 的瓶頸是寫判準,不是工具——所以個人也能搞

**一句話**:eval / agent eval 最難、最不能外包的,是「收集真實 case + 寫出兩個專家會同意的判準」——這是**理解問題,不是工程問題**;所以個人對自己的小場景反而能做得好,而 tracing、平台、多 judge 投票那些工程是規模到了才需要的。

## 為什麼重要
- 把 eval 的難度放對位置:大家以為難在工具/平台,真正難在「知道什麼叫成功」,而這恰好是理解問題、不能用買工具解決。
- 推論:**個人能搞 agent eval,而且特別友善**——最難那塊是你對自己產品的理解,你最深。
- 最小版本(一個下午):`tasks.jsonl` 放 10-20 個 `(goal, 初始狀態, 終態斷言)` → 50 行 script 跑 agent 並存完整 tool-call log → 終態能 assert 用 code、不能的丟單 judge 給 PASS/FAIL → 印「成功率 + 平均 tool call 數」→ 改前改後看 diff。
- 何時才上平台(Braintrust/LangSmith):案例破百 / 跑太慢 / 要共看 trace / 要線上監控。之前都不用。

## 反例與質疑
- 個人的牆:case 攢得慢(把日常使用當 case 工廠)、judge 會漂要偶爾人工校準、多 judge 投票是 3 倍 token。
- 多 agent / 大規模系統的 component-level 歸因,確實需要工程基建,個人版抓不到。

## 連結
- → 引出 [agent-eval-scores-end-state-not-path](./agent-eval-scores-end-state-not-path.md)(那個「判準」具體就是終態斷言)
- ← 支持 [harness-beats-model](./harness-beats-model.md)(eval 是 harness 層手藝,價值不在模型而在你怎麼定義好)

## 出處
- notes/eval-ecosystem-niche.md §個人也能搞對(判斷)

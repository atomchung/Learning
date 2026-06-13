---
type: card
title: Agent eval 以終態評分,不綁標準路徑
aliases: [終態評分, end-state eval, 別逼 agent 走預設路徑]
tags: [coding-agents, eval, agent-testing]
appears-on:
  - coding-agents
created: 2026-06-04
---

# Agent eval 以終態評分,不綁標準路徑

**一句話**:agent 多步、殊途同歸,多條不同的工具路徑可能都正確完成同一目標;所以評分以 **end-state(終態斷言)為主**,別逼 agent 走你預設那條路;trajectory(軌跡)只拿來**診斷失敗**和抓「答案矇對但過程錯」。

## 為什麼重要
- 測 agent ≠ 測單次 prompt:agent 有「走過的路徑」,不能只看最後答案,也不能只認一條標準路徑。
- 三層次看同一 case:end-state(結果)/ trajectory(軌跡)/ component(壞在哪步)。主秤是 end-state。
- 終態優先用 **code 斷言**(`assert db.order.status == "refunded"`、檔案/schema 對),不能 code 判的才丟 LLM judge。
- 公開 agent benchmark 全是 end-state 評分(SWE-bench 過 test、TAU-bench 訂對票且不違反 policy)——反證此原則。
- grader 綁死標準步驟是常見 pitfall:會懲罰「走不同路但結果對」的好解。

## 反例與質疑
- 安全/合規場景:路徑本身就是要求(不能走某些步),這時 trajectory 不只診斷、是硬約束(TAU-bench 的 policy 即是)。
- 終態難定義的開放任務(創意寫作),end-state 斷言寫不出來,只能退回 judge。

## 連結
- ↔ 對比 [artifact-verifiable-output](./artifact-verifiable-output.md)(都在追求「產出可被客觀檢查」,一個對人審查、一個對機器斷言)
- ← 支持 [eval-bottleneck-is-criteria-not-tooling](./eval-bottleneck-is-criteria-not-tooling.md)(終態判準怎麼寫,就是那個「最難的判準」)

## 出處
- notes/eval-ecosystem-niche.md §附:目前怎麼測 agent 能力

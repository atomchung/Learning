---
type: card
title: 檢查只設單側，系統就往單側漂
aliases: [both-directions coverage, 單側檢查產生單側偏移, 雙向覆蓋]
tags: [eval, 預測帳, meta, 校準]
appears-on:
  - coding-agents
  - ai-industry-reading
  - learning-repo-harness
created: 2026-07-05
---

# 檢查只設單側，系統就往單側漂

**一句話**：任何檢查機制（eval、預測訊號、自評）若只覆蓋一個方向，被檢查的系統就會往沒被檢查的方向偏移——雙向覆蓋不是完備主義，是防止優化壓力變成單邊的。

## 三脈絡證據（2026-07-05 同日交會，達 B3 升卡門檻）

1. **eval 設計**：Anthropic cwc-workshops `audit.md`「Both-directions coverage」——測「該搜尋時有沒有搜」的 eval 必須也測「不該搜時有沒有不搜」，否則一個永遠搜尋的模型拿滿分。「One-sided evals produce one-sided optimisation.」同一原則適用 refusal、tool use、escalation。
2. **預測帳設計**：`notes/prediction-ledger-stress-test.md` 發現多數條目只設單側結算觸發——loop/orchestration 兩條只蒐「harness 被吃掉」側的證據，「harness 成現金牛」（Claude Code run-rate $25 億）不在任何結算條件裡；帳只會單向下修對主樑判斷的信心而不自知。修法＝訊號三態齊備（✅ 觸發／❌ 觸發／⚪ 到期）。
3. **防自評（R1）**：meta-review 的證據閘——只有 Claude 自己給自己打分＝評分來源單側，Anthropic 實測 agent 會自信稱讚自己；所以動規則前要求至少一筆 `@user` 標的缺陷＝強制加入反向來源。

三個場景表面無關（評模型／評判斷／評自己），結構同一個：**檢查覆蓋決定漂移方向**。

## 反例與質疑

- 成本不對稱：雙向覆蓋近乎加倍 case 數與訊號複雜度。audit.md 自己也說 headline 數字可以單側（「aggregation matches the question」）——**診斷用途才必須拆雙向**，總覽用途單側可接受。
- 有些行為沒有可觀察的對稱反向（「沒發生的事」常無法取證），此時解法是設 ⚪ 到期態而不是硬造反向訊號。

## 連結

- → 引出 [eval-bottleneck-is-criteria-not-tooling](./eval-bottleneck-is-criteria-not-tooling.md)（單側覆蓋＝判準不完備的一種具體形態）
- ← 支持 [agent-eval-scores-end-state-not-path](./agent-eval-scores-end-state-not-path.md)（end-state 斷言也要正反兩態）
- ↔ 對比 [read-signals-not-surface-numbers](../../ai-industry-reading/cards/read-signals-not-surface-numbers.md)（那張管輸入品質，這張管檢查覆蓋面）

## 出處

- cwc-workshops `rightmodel/.claude/skills/eval-audit-and-sweep/references/audit.md` §1「Both-directions coverage」
- `notes/prediction-ledger-stress-test.md`（M2 單向蒐證＋三、訊號缺陷分型）
- `.claude/skills/meta-review/SKILL.md` R1 證據閘
- `notes/cwc-workshops-cross-read.md` 新增量①（三脈絡交會的發現記錄）

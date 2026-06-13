---
type: card
title: Eval 生態位分岔:正確性測量商品化,安全紅隊升值
aliases: [eval 分岔, 正確性 vs 安全 eval, 紅隊才是錢在的地方]
tags: [ai-industry, eval, agent-security, signal-reading]
appears-on:
  - ai-industry-reading
created: 2026-06-04
freshness: 2026-06  # 工具版圖會變;可遷移的是「測量商品化、安全紅隊升值」的分岔結構
---

# Eval 生態位分岔:正確性測量商品化,安全紅隊升值

**一句話**:agent 真的被部署後,eval 這個生態位分成兩半——**正確性 eval**(輸出好不好)正被開源商品化(DeepEval/RAGAS 免費打到底);**安全/紅隊 eval**(agent 會不會做壞事)有企業預算 + 合規壓力 + 防禦需求,錢往後者跑。

## 為什麼重要
- 解釋了為什麼 OpenAI 要 promptfoo:它的賣點已從「測 prompt 品質」漂到「測 agent 會不會出事」(injection / jailbreak / 資料外洩 / 越權)。
- 對個人差異化:想做有企業價值的技能,「agent 會不會做壞事」的紅隊 eval,比「輸出品質回歸測試」稀缺得多。
- 商品化計時器對「工具」響了,對「安全紅隊 + 分發」還沒——同一條判讀的延伸。

## 反例與質疑
- 正確性 eval 在高風險領域(醫療/法務)仍可能因準確度要求而不被商品化。
- 「安全」也可能被大廠平台原生吸收(正如 promptfoo 被 Frontier 吸收),獨立第三方的空間未必長久。

## 連結
- ← 支持 [open-source-is-the-commoditization-clock](./open-source-is-the-commoditization-clock.md)(正確性測量被開源計時器追殺的具體一例)
- → 引出 [value-flows-to-the-relational-sector](./value-flows-to-the-relational-sector.md)(被商品化的那半,價值往安全與合規流)

## 出處
- notes/eval-ecosystem-niche.md §生態位分岔

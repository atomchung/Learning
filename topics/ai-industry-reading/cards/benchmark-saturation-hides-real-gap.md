---
type: card
title: 跑分飽和時，真實能力與分數的 gap 才是訊號
aliases: [benchmark 飽和, SWE-bench 天花板, 訓練污染訊號]
tags: [ai-industry, benchmark, signal-reading]
appears-on:
  - ai-industry-reading
  - coding-agents
created: 2026-05-30
---

# 跑分飽和時，真實能力與分數的 gap 才是訊號

**一句話**：當 SWE-bench Verified 逼近 95%、即將天花板化時，公開 benchmark 已失去鑑別力；真正的訊號藏在「公開分數 vs 隱藏任務集分數」的落差裡。

## 為什麼重要
- SWE-bench Verified 三年從 1.74%（GPT-4）漲到 93.9%（Claude Mythos Preview），50× 成長即將觸頂。
- 但 **SWE-bench Pro（隱藏任務集）只有 ~46%** —— 這個 gap 揭示了訓練污染：模型可能「背過」公開題庫。
- 對 PM / 投資判讀：不能再用公開跑分選模型，要看模型在「沒見過的任務」上的表現。分數越接近天花板，它能告訴你的越少。

## 反例與質疑
- 隱藏任務集本身也可能設計偏難，46% 不一定純粹反映「真實能力」。
- 訓練污染未必是作弊，公開資料進訓練集是常態，gap 部分來自分布差異。

## 連結
- ↔ 對比 [open-source-is-the-commoditization-clock](./open-source-is-the-commoditization-clock.md)（另一種「別看表面」的信號讀法）
- → 引出 `recall-beats-context-length`（同樣是「指標飽和、戰場轉移」的模式，待拆）

## 出處
- notes/model-progress-roadmap.md §一.2

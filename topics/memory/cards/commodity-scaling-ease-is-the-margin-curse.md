---
type: card
title: 擴產越容易，利潤越薄
aliases: [優勢即詛咒, scaling-ease is the margin curse, 免費擴張的詛咒]
tags: [commodity, memory, NAND, margin, mental-model, 投資判讀]
appears-on:
  - memory
created: 2026-06-27
---

# 擴產越容易，利潤越薄

**一句話**：當一個商品的產能擴張**不需要昂貴的瓶頸資源**，bit/單位的成長就便宜 → 慢性供過於求傾向 → margin 結構性偏低。看似優勢的「擴產容易」，正是利潤薄的詛咒。優勢與詛咒是同一件事。

## 為什麼重要
記憶體產業內三塊正好構成一組對照實驗，同一條規律三次驗證：

1. **NAND**：靠垂直堆疊（3D，96→300+ 層），加層用便宜的 deposition + etch，**不需 EUV** → bit 成長便宜 → 五家擠在一起、慢性供過於求 → 毛利結構性低（~25%）。
2. **DRAM**：靠橫向微縮（2D shrink），越縮越需要昂貴 EUV，每代擴張更難 → 三家寡占 ~88% → margin 高得多。
3. **HBM**：客製化 + 認證門檻 + 產能預訂，**擴張最難** → 毛利 70–80%。

擴張難度由低到高（NAND < DRAM < HBM），margin 由低到高，完美正相關。**進入/擴產的摩擦力，就是利潤的護城河。**

## 為什麼可遷移
- 任何「進入門檻低、擴產不卡關鍵資源」的 commodity 都吃這個詛咒：面板、太陽能矽片、航運運力、大宗化工。
- 反向用：找「擴張被某個瓶頸卡死」的環節（EUV、認證、稀缺礦、牌照），利潤往往躲在那裡。
- 對投資：別被「這技術擴產很快、成本下降很猛」當利多——那常常正是 margin 永遠起不來的原因。

## 反例與質疑
- 擴產容易 ≠ 一定低利潤：若需求成長長期快過供給（罕見且難持續），低門檻商品也能賺一段。記憶體 supercycle 就是需求暫時壓過供給，但這是週期不是結構。
- 有時低 margin 是**策略選擇**（衝量搶份額、養生態），不是被詛咒。要分清「結構性薄」與「策略性薄」。
- 瓶頸會移動：今天的護城河（EUV）可能被新技術繞過（3D DRAM、High-NA），詛咒與護城河會易主。

## 連結
- ↔ 對比 [cyclical-tops-track-supply-discipline-not-demand](./cyclical-tops-track-supply-discipline-not-demand.md)（擴產容易 → 供給易失控 → 所以週期要盯供給紀律）
- → 引出 `hbm-leadership-is-a-qualification-race`（HBM 的高 margin 來自認證這個擴張瓶頸）

## 出處
- `notes/memory-industry-map.md` §四（NAND 免費垂直擴張）+ §三（HBM 高 margin）
- deep research 2026-06：NAND ~25% GM vs HBM 70–80% GM；NAND 3D 不需 EUV

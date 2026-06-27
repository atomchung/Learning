---
type: starting-point
topic: memory
status: expanding
created: 2026-06-27
---

# 起點：怎麼判讀記憶體 / commodity 半導體週期

> 磁鐵卡。記憶體與 commodity 硬體的判讀素材先塞進來，看出可跨產業重用的判斷時再拆成卡。
> 來源筆記：`notes/memory-industry-map.md`、`notes/cxmt-dram-challenge.md`

## 當下的核心問題
- 記憶體這種 cyclical commodity，怎麼判斷週期位置與見頂？
- 哪些判斷可遷移到其他 commodity（面板 / 太陽能 / 航運 / 化工）？
- 這條線和 `ai-industry-reading` 的「讀信號不讀數字」怎麼接？（答：commodity 的「需求故事」就是該丟掉的表面數字）

## 已拆出的卡（2 張，都選了「最可遷移」的元判斷）

### Commodity 週期元判斷
- [commodity-scaling-ease-is-the-margin-curse](./cards/commodity-scaling-ease-is-the-margin-curse.md) — 擴產越容易，利潤越薄（NAND 免費垂直擴張＝margin 低的詛咒）
- [cyclical-tops-track-supply-discipline-not-demand](./cards/cyclical-tops-track-supply-discipline-not-demand.md) — 商品週期的多空盯供給紀律，不盯需求故事

## 還沒拆但累積中的發現
- **記憶體是三個市場不是一個**（commodity DRAM / HBM / NAND 定價邏輯不同，混講必誤判）—— 理解整個產業的鑰匙，但較綁定記憶體本身，暫留筆記層
- **HBM 領導權靠認證節奏維持**：Samsung 卡 Nvidia 12-hi HBM3E 認證 ~18 個月就丟掉 Blackwell 週期 → 認證時點比產能數字更決定排名
- **crowd-out 機制**：HBM 吃不成比例的晶圓面積（wafer input 22% vs bit 供給 9%）→ 餓死 commodity DRAM → AI 間接推升 DDR5
- **中國國產替代模式**：CXMT/YMTC ＝ 國家補虧十年 + 買斷死技術 + 全球挖人；2028 後是 commodity 通縮壓力

## 下一步可能要拆的卡
- [ ] `hbm-leadership-is-a-qualification-race` — 高階客製組件的領導權由認證節奏決定，不由產能規模
- [ ] `three-markets-not-one` — 同一個「產業」標籤下可能藏著定價邏輯完全不同的子市場

## 相關白板（跨脈絡連結）
- `ai-industry-reading` — 共同祖先是 [read-signals-not-surface-numbers](../ai-industry-reading/cards/read-signals-not-surface-numbers.md)：commodity 的「需求故事」就是該丟掉的表面數字
- 投資端落地：investment_note 的 `wiki/MU`、`wiki/SNDK`、`research/021`

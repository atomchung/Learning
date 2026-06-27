---
type: note
title: 記憶體產業地圖 — 它是三個市場不是一個，週期成敗全看 capex 紀律
tags: [投資判讀, 半導體, 記憶體, DRAM, NAND, HBM, 週期, 中國]
freshness: 2026-06
source: SemiAnalysis CXMT 文 + 2026-06 HBM/NAND/週期 deep research（多源、附 fact-check）+ investment_note wiki 對位
created: 2026-06-27
related: [cxmt-dram-challenge]
---

# 記憶體產業地圖：它是三個市場不是一個，週期成敗全看 capex 紀律

**一句話**：別把「記憶體」當一個市場。它是 **commodity DRAM / HBM / NAND** 三個競爭格局、定價邏輯、週期性質都不同的市場，混在一起講必誤判。AI 同時從兩條路推升它——直接買 HBM、間接排擠 commodity 產能。當前（2026 中）是 15 年來最緊的 supercycle，但「會不會崩」不取決於需求故事，取決於三巨頭的 **capex 紀律**。

> 這份是 mental model（怎麼理解這個產業）；投資端的證偽/倉位追蹤在 investment_note 的 `wiki/MU`、`wiki/SNDK`、`research/021`，這裡只記可遷移的判斷並對位。
> 單點起源見 [cxmt-dram-challenge](./cxmt-dram-challenge.md)。

---

## 一、核心框架：三個市場，不是一個

這是最該記住的元判斷（來自 investment_note research/021 的 framing，被這次 deep research 證實放大）：

**1. Commodity DRAM**
- 格局：三巨頭寡占 ~88%（Samsung / SK Hynix / Micron）+ CXMT 全球第四（4Q25 7.67%）
- 性質：標準品、可替代、**cyclical commodity**，價格全行業一起漲跌

**2. HBM（高頻寬記憶體）**
- 格局：SK Hynix 獨大，但 2026 鬆動（見 §三）
- 性質：**唯一逃離 commodity 定價的一塊**——客製化 + 長約 + 預訂產能

**3. NAND（快閃）**
- 格局：五家擠在一起，無明確老三（Samsung 28% / SK+Solidigm 22% / Kioxia・Micron・SanDisk 各 ~13%）
- 性質：非揮發、便宜、**margin 結構性低於 DRAM**（見 §四）

**學到的判斷**：看一家記憶體公司賺錢，第一步永遠是問「它賺的是哪一塊」。MU 的 84% 毛利和 SNDK 的 78% 毛利，背後的可持續性完全不同。

---

## 二、AI 怎麼推升記憶體：兩條路（crowd-out 是最漂亮的洞察）

**路一（直接）**：AI GPU 需要 HBM。**HBM ≈ 一顆 AI GPU BOM 的 45–50%**（Epoch AI 拆 B200：$3,200/$6,400），是現代 GPU 最大單一成本項。這是記憶體廠突然吃下 AI 大塊價值的原因。

**路二（間接，更隱蔽）— 產能排擠（crowd-out）**：
- HBM 用 3D 堆疊，吃晶圓面積**不成比例**：占三巨頭 DRAM **wafer input 22%（2026）→ 30%（2027）**，但只占 DRAM **bit 供給 ~9%→13%**
- 翻譯：做 HBM 吃掉大量晶圓、卻只產出少量 bit → **餓死 commodity DRAM 供給** → DDR5 跟著缺、跟著漲
- 每 GB 的 HBM 吃 ~3–4x DDR5 的晶圓

**學到的判斷**：AI 不只「買 HBM」推升記憶體，還「排擠 commodity 產能」間接推升 DDR5。這解釋了一個反直覺現象——**2026 是 commodity DRAM 的補漲年，DDR5 獲利能力首度超越 HBM3e**。看記憶體別只盯 AI 直接需求，要看產能被 HBM 抽走多少。

---

## 三、HBM 是戰場，但 2026 護城河在鬆動

**為什麼 HBM 能跳脫 commodity 週期定價**：
- 客製化 + base-logic die（尤其 HBM4），不是可互換的標準品
- 固定價長約 + 產能預訂：三家 2026 HBM 全部 sold out；買方（hyperscaler）預付現金鎖產能
- 每 GB ~$13–17，per-unit 比 DDR5 貴 **~6–10x**，毛利 70–80%（vs NAND ~25%）

**2026 的兩個關鍵變化（護城河鬆動）**：

| 變化 | 內容 |
|---|---|
| Micron 超車 | HBM 即期市佔 Micron ~21% **超越 Samsung ~17%**，成 #2（SK Hynix 仍 ~58–62%）|
| HBM4 普及 | 2026-06-05 Jensen 確認 **三家都過** Nvidia Vera Rubin HBM4 qual + 量產 |

- Samsung 落後的根因：卡 Nvidia 12-hi HBM3E 認證 **~18 個月**（2024-04→2025-09），錯過整個 Blackwell 週期——**這是「讀信號不讀數字」的反面教材：認證時點比產能數字更決定成敗**
- SK Hynix 仍領 HBM4 分配（~60–70%），但「一家獨佔」已變「三家分食」

**對位投資端**：MU thesis 的「第一條腿（HBM 結構性）正在弱化」就是這件事——Samsung 反撲、Micron 卡 Rubin 後段。Learning 層的判斷：**HBM 領導權是動態的，靠認證節奏維持，不是一勞永逸的護城河。**

---

## 四、NAND：免費垂直擴張 = 它 margin 結構性低的原因

**最值得記的 NAND 判斷**：
- DRAM 靠**橫向微縮**（2D shrink），越縮越需要昂貴 EUV，每代 capex 越重
- NAND 靠**垂直堆疊**（3D，96→128→218→300+ 層），加層用便宜的 deposition + etch，**不需 EUV** → bit 成長便宜
- 成本 per bit ~DRAM 的 1/10

**因果**：NAND 的「免費垂直擴張」聽起來是優勢，**但它正是 NAND margin 結構性低於 DRAM 的原因**——擴產太容易 → 慢性供過於求傾向 → margin 薄（~25% vs DRAM 寡占 + HBM 高階）。優勢和詛咒是同一件事。

**HBF（High Bandwidth Flash）— NAND 的新變數**：
- 是什麼：NAND-based、堆疊式，坐在 HBM 和 SSD 之間的新層
- 誰推：**SanDisk + SK Hynix 領頭**（2026-02 OCP 標準化），Samsung、Kioxia 也入局
- 定位：針對 AI **inference**（存 read-only 權重），**不跟 HBM 比速度，比的是「capacity-per-dollar」**——容量 8–16x HBM，但 latency(µs vs ns)/寫入壽命/功耗都輸
- 用法：權重放 HBF、熱資料放 HBM → 每顆 GPU 服務更多請求
- 時程：樣品 2H26、產品 2027（projection）

**對位投資端**：這正是 SNDK wiki 的核心——SanDisk 主導 HBF，**Micron 不在聯盟**，所以 HBF 若成局會打到 MU 的 H2 假設。

---

## 五、週期：成敗全押 capex 紀律（這次不一樣的唯一變數）

**記憶體為什麼 cyclical**：commodity（DRAM/NAND）需求漲 → 廠商擴產 → 產能洪峰 → 供過於求 → 崩。週期的根因變數是 **capex 紀律**。

**當前位置（2026 中快照，⚠️ 會過期）**：
- supercycle 預估跑到 2028；供需缺口 DRAM −4.9% / NAND −4.2% / HBM −5.1%，**15 年來最緊（since 2011）**
- 價格：DRAM 合約 1Q26 +80–90% QoQ、2Q26 +58–63%；累計 2025–27 估 **+275–300%**（是 2017–18 supercycle ~90% 的 3 倍）
- 記憶體 = hyperscaler capex ~30%（2023 才 8%，翻 4x）

**「這次不一樣」全押這一點**：
- 2026 capex：SK Hynix $20.5B(+17%) / Samsung $20B(+11%) / Micron $13.5B(+23%)
- **關鍵**：增量多用於**製程升級**（hybrid bonding），**不是擴產** → 對 2026 bit 供給影響小
- 對比 2017–18：三星 capex **+50% YoY** → 那波產能洪峰造成 2019 崩盤
- 這次三巨頭甚至在**管制客戶囤貨**防假性庫存

**怎麼判斷見頂（學到的監控框架）**：
- ✅ 頂部信號目前**缺席**：channel inventory **2–4 週**（vs 歷史每次見頂前 >15 週）——最強「還沒崩」證據
- ⚠️ 但 duration 已 late：trough 起 ~30 個月，達歷史最長上行
- 🔮 真正該盯的見頂觸發（不是需求故事，是供給紀律）：
  1. 三巨頭 capex 從「製程升級」轉向「擴產」（U-turn）
  2. 中國（CXMT/YMTC）增產破壞紀律
  3. hyperscaler 現金緊張（2026 capex 估佔營運現金流 92%）逼 capex 急煞

**學到的判斷**：記憶體週期的多空，盯 **capex 紀律 + 庫存週數**，不要盯「AI 需求會不會繼續」。需求故事人人會講，紀律才是會崩的那個變數。

---

## 六、中國變數：2028 後的通縮壓力，不是現在

- **CXMT**（DRAM 國產隊）：全球第四，但成長是 supercycle 漲價的週期財，非搶定價權（成本仍貴 30%、HBM yield ~25%）。詳見 [cxmt-dram-challenge](./cxmt-dram-challenge.md)
- **YMTC**（NAND 國產隊）：294 層、自製設備繞制裁、目標 2026 底 15% 市佔；**是唯一在「增加實體 NAND 產能」的玩家**（韓美日都凍 NAND 去追 HBM）
- **共同信號**：兩家都是「國家補虧十年 + 買斷死技術 + 全球挖人」模式，短期跟漲、**2028 後若持續猛加產能 = commodity 記憶體的長期通縮壓力**，也是上面 §五見頂觸發之一

---

## 七、怎麼讀一支記憶體股（綜合判讀框架）

1. **先分這家賺的是哪塊**：HBM 溢價 / commodity 補漲 / NAND——可持續性完全不同
2. **拆 bit 出貨 vs ASP**：漲價財（全行業同漲）≠ 份額財（真搶到客戶）。CXMT 1Q26 bit +11% 但 ASP +57% = 純漲價財
3. **盯供給紀律不是需求故事**：capex 用於擴產還是升級、庫存週數、中國增產
4. **HBM 看認證節奏**：誰過了 Nvidia 下一代 qual，比誰產能大更決定排名
5. **對位我的持倉**：MU = 雙線押注（HBM 腿弱化 + 週期腿會均值回歸，自承「方向對但機制不透明」）；SNDK = NAND + HBF 純玩家

> 這 5 條是可遷移框架（不會過期）；§五的具體數字是 2026-06 快照（會過期，看 frontmatter freshness）。

---

## 候選升級成卡片的判斷（待你決定）

這份筆記裡有 3 個可能跨脈絡重用、值得升級成 `topics/` 原子卡的判斷：
1. **記憶體是三個市場不是一個**（commodity DRAM / HBM / NAND 定價邏輯不同）
2. **NAND 的免費垂直擴張正是它 margin 低的原因**（優勢與詛咒同源——可遷移到其他「擴產容易 = 利潤薄」的商品產業）
3. **商品週期的多空盯供給紀律不盯需求故事**（capex 紀律 + 庫存週數 > AI 需求敘事——可遷移到任何 cyclical commodity）

第 2、3 條的「優勢即詛咒」「盯供給不盯需求」可能比記憶體本身更通用。要升級的話跟我說。

---

## 出處
- SemiAnalysis《China's CXMT Is Set to Challenge DRAM Incumbents》(2026-06, 付費)
- HBM 研究：Epoch AI（B200 BOM 拆解）、Counterpoint/TrendForce（HBM 市佔）、Micron Q3 FY26 press release、Nvidia Rubin HBM4 qual（2026-06-05 多源）、TrendForce（HBM wafer input 22%→30%）
- NAND/週期研究：TrendForce（4Q25 NAND 市佔 + 合約 ASP）、SK Hynix newsroom（HBF）、Goldman（供需缺口）、TrendForce（2026 capex 紀律）、Uncover Alpha（週期對比）、useluminix（頂部信號/庫存週數）
- 投資端對位：investment_note `wiki/MU`、`wiki/SNDK`、`research/021_global_dram_market_2026`
- 連結卡片：[read-signals-not-surface-numbers](../topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md)（CXMT/Samsung 認證都是案例）

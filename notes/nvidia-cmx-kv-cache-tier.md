---
type: note
title: NVIDIA CMX 微秒層 — 開放介面、保留矽片，以及一張看多圖的解剖
tags: [投資判讀, 半導體, NAND, 記憶體, NVIDIA, KV-cache, 推論基建]
freshness: 2026-08
source: FB 貼文截圖（BEP Research「THE MICROSECOND TIER」圖卡，2026-08-05）+ 查證 NVIDIA FMS 2026 / Micron FQ3 / SanDisk FQ4 / TrendForce
created: 2026-08-10
related: [memory-industry-map, cuda-moat-2026, kimi-k3-hybrid-attention, two-week-scan-2026-08-09]
---

# NVIDIA CMX 微秒層：開放介面、保留矽片

**一句話**：NVIDIA 在 HBM 與網路儲存之間開了一個「微秒層」放 KV cache，8/4 FMS 把 cuFile 開源拉 40 家進來——**開源的是介面，收租的是底下的矽**。這對記憶體是**結構分化**不是齊漲，而市場當週的反應跟「看多 NAND」剛好相反。

> 起因：使用者傳 FB「台灣半導體先進封裝聯盟」貼文截圖（BEP Research 圖卡），要求理解。這份記三件事：機制、圖的錯處、我自己踩的坑。

---

## 一、機制：這層在解什麼（餐廳比喻）

AI 每回一句話，理論上要把前面全部重讀一遍。所以它把讀過的東西備好放著＝ **KV cache**（備好的料）。

放哪裡是問題：

1. **HBM**＝廚房小冰箱。次微秒、極貴、很小（Vera Rubin NVL72 一櫃 20.7 TB＝72 × 288GB）
2. 客人多（高並發）、菜單長（長 context／agent 久跑）→ 小冰箱塞爆
3. 原本只有兩個爛選項：丟掉重算（燒 GPU 時間）／送遠端儲存（毫秒級，慢到不能用）

NVIDIA 做的＝中間插一個**冷藏室**：乙太網掛載、BlueField-4 後面吊一池 flash，內部叫 **G3.5 層**。取料幾十微秒，比重算快幾百倍、比 HBM 便宜幾十倍。

**這是 [precompile-to-local-index](../topics/coding-agents/cards/precompile-to-local-index-not-restuff-context.md) 的硬體版**：塞不下就分層 page-in，別硬塞。同一個判斷在軟體與硬體兩個尺度各自浮現。

## 二、8/4 FMS 的真新聞不是「命名新層」

**圖說「NVIDIA 今天在 FMS 命名了 HBM 底下的快閃 context 層」——命名是 7 個月前的事。**

- CMX 於 **CES 2026（1 月）**發表、**GTC 2026（3 月）**以 BlueField-4 STX 擴充
- 圖自己的 source line 就寫了「NVIDIA CES 2026 disclosures」，等於自招

**8/4 真正發生的是標準搶灘**：

- **cuFile 開源**，拉 Google、Intel、Meta 當共同維護者
- **Storage-Next 聯盟 40+ 家**（含 DDN、KIOXIA、Micron）
- SCADA：把儲存控制搬上 GPU

一句話：**把插座規格開源讓全世界做電器，但發電機（BlueField-4）還是他家的。**

→ 已升卡：[open-the-interface-keep-the-silicon](../topics/ai-industry-reading/cards/open-the-interface-keep-the-silicon.md)

## 三、圖的三處錯（都可算術驗證）

**1. 圖自己的數字反駁自己的標題**

圖警告「100 用戶 × 1M context ＝ 31.0 TB，跑爆整櫃 HBM4 的 20.7 TB」。但：

- 20.7（HBM4）+ 16.0（BlueField-4 那層，**圖自己畫的**）= **36.7 TB > 31.0 TB**
- 還漏一整層：Vera Rubin 整櫃 SOCAMM CPU 記憶體 **28 TB**（見 `two-week-scan-2026-08-09.md`）
- 整櫃可用記憶體約 **48.7 TB**，還沒算 flash

「跑爆」只在你假裝中間層不存在時成立。

**2. 需求那根柱子是「零優化」最壞情況**

反推：31 TB ÷ 100 人 ÷ 1M token = **310 KB/token**（128K 那根算出來 305 KB，內部一致）。這是 FP16、無 MLA、無量化、無混合注意力的裸值（約 80 層 × 8 KV heads × 128 dim）。

但 [kimi-k3-hybrid-attention](./kimi-k3-hybrid-attention.md) 記著 K3 的 3:1 KDA 混合**省掉 75% KV cache**；Baseten Still 架構壓 8x–200x。套 K3 比例：31 TB → **~7.8 TB，反而塞得進 HBM4**。

**公平的反論**：KV 變便宜會誘發更長 context、更多常駐 agent session＝Jevons 效應，淨方向不明。誠實結論是——**KV 需求成長是真的，但這張圖無法告訴你幅度，因為它挑了最壞情況當基準。**

**3. 財報數字是舊貨，且沒拆價格與數量**

- 圖用 Micron **FQ2**（3/18 公布）：DRAM $18.8B、NAND $5.0B
- 但 **FQ3**（六月底）早就出來：DRAM **$31.3B**（+343% y/y）、NAND **$9.9B**（+361% y/y），資料中心 SSD **>$5B、季增翻倍**
- 一張 8 月做的看多圖用三月數字，等於沒更新（**疑點未證實**：FQ3 那句「DC SSD >$5B、季增翻倍」與圖上 FQ2 的「NAND $5.0B」量級相同、註腳措辭幾乎逐字，懷疑兩期被混用，未取得 FQ2 逐字稿故不下結論）

**拆價格 vs 數量**（2026-08-09 立的規矩）：圖說 NAND 價格季增 +high-70s%、DC NAND 營收季增翻倍，則

> bit 出貨成長 = 2.00 ÷ 1.78 ≈ **+12%**

**營收翻倍裡約 88% 是漲價、12% 才是量。** 「on KV cache offload」這個因果若為真，必須出現在 bit 上——而 bit 只長一成多。（口徑註記：ASP 是整體 NAND、營收是 DC 口徑，不完全同尺，但拆解方向對。）

## 四、受益名單（按證據強度，不按想像）

**淘金的是 NAND 廠、賣鏟子的是控制器與專用碟、賣地的是 NVIDIA。這波最受益的不是淘金的。**

**第一梯隊（有具名產品直接對接 CMX）**

- **Kioxia 鎧俠**：7/30 發 **CM10**，第一顆 PCIe 6.0 企業級 SSD，官方明講支援 NVIDIA CMX；1.6–61.44TB、順序讀 +92%／隨機讀 +85% vs CM9、直接冷板液冷。**唯一在 NVIDIA 開講前就把對應產品端上桌的**
- **Silicon Motion 慧榮（台廠 SIMO）**：MonTitan **SM8466 / SM8366** 明確對應 NVIDIA **ICMS（KV Cache Extension）**；另有 SM2524XT 專打 KV cache 密集負載（14 GB/s、2.5M IOPS）；FMS 展 256TB SSD。**位置最好——不用押哪家 NAND 廠贏，誰做 KV 碟都要控制器**
- **ScaleFlux（未上市）**：為 CMX 做碟層儲存，7–10+ DWPD、200+ FDP streams
- **Solidigm（SK 海力士旗下，無純標的）**

**第二梯隊**：Micron、SanDisk、Samsung — 在聯盟名單裡，會賣到 bit，但無專屬定位

**第三梯隊**：DDN、Dell、HPE、IBM、VAST、WEKA — 2H26 出相容機，**短多長空**（見下）

**誠實標註**：群聯（Phison）**查無 CMX 直接對位**；其 aiDAPTIV+ 是另一定位（用 SSD 幫本地／邊緣 LLM 省 RAM）。不要因為是台廠就硬掛。

## 五、誰受傷（圖完全沒講的一半）

**1. 儲存軟體廠（VAST、WEKA 最典型）——短多長空**

他們原本的賣點就是「我家軟體讓 GPU 讀資料最快」。NVIDIA 把那條路徑開源、變標準、做進硬體＝**獨門優化變成人人都有的標準功能**，被降級成「一個合規的盒子」。現在加入聯盟是因為不加入立刻出局。

**2. AMD、華為**：原本追 CUDA 已很累，現在儲存層也標準化在 NVIDIA 定義的規格上。**開源讓事情更糟不是更好**——開源版誰都能跑，但跑最好的是 BlueField-4，你合規了還是輸，只是輸得更沒藉口。接 [cuda-moat-2026](./cuda-moat-2026.md)。

**3. HBM 的邊際故事**：料能放便宜冷藏室，「拚命買小冰箱」的壓力就小。證據在同一台機器上——**SOCAMM 從 192GB 砍到 96GB**。所以對記憶體是**替代**不是齊漲。（先進封裝角度要精準：被砍的是 CPU 側 LPDDR，**HBM4 的 20.7 TB 一格沒動**，CoWoS 那條沒受傷，受傷的是 commodity 側。）

**4. 做 KV cache 中間件的新創**：NVIDIA 用「硬體 + 標準」直接吃掉這個生態位。又一個 [llm-call-niches-are-features-not-companies](../topics/ai-industry-reading/cards/llm-call-niches-are-features-not-companies.md) 的實例。

## 六、市場反應：跟圖的結論相反，就在同一週

- **7/28–7/29**：晶片股大屠殺，市值蒸發 **>$1 兆**。SanDisk −14%、Kioxia −13.9%、Micron −8%+、WD −7%。理由＝擔心 **AI 基建支出見頂比預期快**。SNDK 另因 **CXMT IPO** 重燃中國 NAND 競爭疑慮單日 −11%
- **7/30**：Kioxia 發 CM10
- **8/4**：FMS，cuFile 開源 + CMX + 40 家聯盟
- **8/5**：**這張「Most bullish NAND」圖被做出來**
- **8/6**：SanDisk FQ4 財報 → 盤前 −8%、收 **−6.18%**，SK 海力士 −10%、三星 −6%，NVDA/MU/AMD 連帶下殺

**市場完全沒把 FMS 當利多。那一整週在恐慌 AI capex 見頂。**

⚠️ 上列漲跌幅來自不同來源、不同基準期，無逐日行情交叉驗，**當量級看不當精確值**。但「YTD 大漲 + 從 6 月高點腰斬 + 單日暴漲 26%」這個形狀可靠＝**情緒主導、已 price in 很多**。

## 七、SanDisk 法說會：我一開始讀錯了（坑）

**我第一輪告訴使用者「SanDisk 自己說 NAND 要供過於求更久」——錯的。** 我讀的是市場評論文章的敘事，沒讀法說會本身。

**管理層實際說的（Q4 FY2026）**：

- NAND 已從一般循環復甦轉入**結構性稀缺**（structural scarcity）
- FY27 供給 **>50% 已被長約鎖定**，FY28 升至 **~2/3**
- Q1 FY27 指引：營收 $10.3–10.8B、非 GAAP 毛利率 **83–85%**、EPS $44–46
- NBM 長約：8 個資料中心／邊緣客戶、加權平均 **>4 年**、floor pricing 下最低預期營收 **$93.9B**
- 加碼 **$14B** 庫藏股

**那為什麼跌？**【查到的】進場前 YTD 漲約 500%，門檻極高；7/28 已先被 CXMT IPO 砍 11%。【我的推論】**鎖 >50% FY27 產出進 floor-price 長約本身就是訊號**——你會鎖價，是因為你不認為價格會更高；降低下檔＝讓出上檔，市場可能讀成管理層在對頂部避險。

**訊號不在指引數字，在合約結構。** 這正是 [read-signals-not-surface-numbers](../topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md)，而我自己第一輪沒做到。已記入 `meta/defects.md`（credibility-miss）。

## 八、結論：圖的方向對，論證七成是修辭

> **它把「一個新的高階利基」誤讀成「整個 NAND 商品市場的多頭」。**

真正的 NAND 多頭邏輯也不是圖說的漲價，而是：**KV cache 是寫入 churn 負載，碟片從「賣一次用五年」變成耗材**（要 7–10+ DWPD，一般碟只有 1–3）。重複消費比一次性擴容持久，而且**規格分化＝不是所有 NAND 產能都吃得到**。

這條比漲價故事耐放，因為它是機制不是價格。

## 出處

- [NVIDIA opens cuFile — SiliconANGLE](https://siliconangle.com/2026/08/04/nvidia-open-sources-cufile-api-accelerating-gpu-read-write-capability-high-speed-storage/)
- [NVIDIA AI Storage Goes Open at FMS 2026 — Futurum](https://futurumgroup.com/insights/nvidia-ai-storage-goes-open-at-fms-2026-is-open-source-the-new-moat/)（egress 擋，僅搜尋摘要）
- [Introducing BlueField-4-Powered CMX — NVIDIA Blog](https://developer.nvidia.com/blog/introducing-nvidia-bluefield-4-powered-inference-context-memory-storage-platform-for-the-next-frontier-of-ai/)（egress 擋，僅搜尋摘要）
- [KIOXIA CM10 aimed at NVIDIA CMX KV Cache — StorageReview](https://www.storagereview.com/news/kioxia-cm10-is-its-first-pcie-6-0-enterprise-ssd-aimed-at-nvidia-cmx-kv-cache)
- [Silicon Motion SSD controller for KV Cache workloads — Electronics Weekly](https://www.electronicsweekly.com/news/business/silicon-motion-2026-06/)
- [ScaleFlux KV Cache SSD 7-10+ DWPD — StorageReview](https://www.storagereview.com/news/scaleflux-kv-cache-ssd-platform-claims-7-10-dwpd-and-200-fdp-streams)
- [Chip stocks shed >$1 trillion — CNBC](https://www.cnbc.com/2026/07/29/chip-selloff-sk-hynix-samsung-softbank.html)
- [SanDisk Q4 FY2026 earnings call highlights — GuruFocus](https://www.gurufocus.com/news/9009608/sandisk-corp-sndk-q4-2026-earnings-call-highlights-record-revenue-and-eps-driven-by-ai-data-center-surge)
- [Micron FQ3 2026 results](https://investors.micron.com/static-files/2354ecda-77a0-4ddd-8462-a631eb491356)
- [NAND supply to outpace demand in 2027 — TrendForce](https://www.trendforce.com/presscenter/news/20260721-13148.html)
- [SNDK −11% on CXMT IPO / China NAND competition — FXLeaders](https://www.fxleaders.com/news/2026/07/28/sndk-stock-crashes-11-as-cxmt-ipo-revives-china-nand-competition-and-margin-fears/)

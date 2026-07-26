# CUDA moat 2026:AMD 官方敘事 + DeepSeek/華為洩漏敘事 + 開發者生態指標

> 核心問題:Nvidia 的 CUDA 護城河到底多快在瓦解?兩條線(美系 AMD、中系 華為/DeepSeek)都在講同一個故事——「AI agent 自己會寫程式,所以複製 CUDA 生態的成本大降」——但證據強度差很多,這份筆記把各層證據拆開放,不混講。

## 0. 一句話判斷

**moat 變淺,但沒填平,而且中系比美系落後得更多。** AMD 這邊有中立跑分(MLPerf)+ 成熟轉譯層(HIP ~2% overhead)撐腰;華為/DeepSeek 這邊幾乎全是自報,連材料本身(洩漏逐字稿)真偽都沒人證實。

---

## 1. AMD 官方敘事(SemiAnalysis, 2026-07-25,《Can AMD break the CUDA Moat?》)

原文被 paywall 擋(WebFetch 403,降級用搜尋摘要重建,以下標官方宣稱/分析師說法)。

**AMD 官方宣稱(Advancing AI 2026 發表會,7/22-23)**
- Helios rack:72 顆 MI455X + 18 顆 EPYC Venice CPU,宣稱「每美元 token 數比對手高 30%」
- MI455X:CDNA5、首款 2nm 架構、432GB HBM4、23.3TB/s 頻寬
- **ROCm.ai**(8 月上線):讓 Claude/Codex/Cursor 等 coding agent 原生理解 ROCm
- **Hyperloom**:開源 agentic 系統,無人在迴圈,自動 profiling→kernel 重寫→驗證,官方說「原本要幾週,現在幾小時」
- 財務工程:給 OpenAI/Meta 近 105% 股權回饋(選擇權結構,AMD 股價衝 $600 才全額觸發)——Helios 機櫃實質接近零成本甚至倒貼

**沒對齊的地方(廠商聲明互打,不算獨立實測)**
SemiAnalysis 自己唱衰量產:「工程樣品 2H26 到位,但真正量產 tokens 要拖到 2027 Q2」;AMD 當場否認;更晚 Lisa Su 又宣稱已全面量產、Q3 末開始出貨。三方拉鋸,**這條本身不算獨立實測,是分析師預測 vs 廠商聲明**。

**懷疑派的錨(其他分析師,非 SemiAnalysis)**
「18 年就是 18 年,一兩年追不上」——AMD 單節點優化能追上,但沒法乾淨組合進 vLLM/SGLang 生產環境;disaggregated inference 這塊 CUDA 生態 2024 初就有,AMD 公開 recipe 今年 1 月才出,結構性落後還在。

---

## 2. DeepSeek/華為洩漏敘事(2026-07 瘋傳)

**這條的可信度分層要先講清楚,這是全篇最弱的一段證據**:

- 流傳的是梁文鋒在**封閉投資人交流會**上的發言紀錄(約 4 小時、118 條要點,英文版流傳成「3 萬字逐字稿」)
- 由騰訊科技相關管道流出,現在原始連結已死,英文版只剩 GitHub 上一份**未經驗證的 PDF**
- DeepSeek 官方沒證實文件真偽,Bloomberg 也表示未能驗證
- **間接支持真實性的行為訊號**(不是證明):洩漏後 DeepSeek 把 15 億美元 B 輪融資無限期喊停——跟「洩漏是真的、正在處理投資人關係損害」一致
- **內部一致性檢查**:文件裡「10 個月硬體回本、約 6 倍毛利」跟 DeepSeek 2025-03 公開揭露的 545% 理論推理毛利率對得上——少數能交叉驗證的錨點

**這條本身就是「作者自報 vs 獨立複現」框架的活教材**:梁文鋒的話 = 利害關係人自報;連文件真偽都未經第三方證實,比一般「官方宣稱」更弱一層。

### 他提出打破 CUDA moat 的三個機制
1. AI 自己會寫程式 → 複製 Nvidia 生態的成本大降
2. **TileLang**(高階語言,可快速寫 CUDA 算子等價物)+ AI 組合 → 重建 Nvidia 整套生態
3. 解耦論:CUDA 血緣來自遊戲顯卡,現在 AI 卡市場已比遊戲卡大,沒理由繼續綁定

DeepSeek 訓練 V3 時雖用 Nvidia 卡,傳聞已放棄 CUDA、改用 TileLang 打底——**這個技術細節沒找到獨立來源交叉驗證,標記為轉述、非確認**。

**他自己承認的下修**:「一年內能追上,但華為落後 Nvidia 約兩年」——連本人都承認差距,不是純多頭敘事。

### 具體數字
- 自報:跟華為合作拿到 **16,000 張 Ascend 950** 做生態驗證,宣稱「性能和價格上可完全平替 GB200/GB300」——**沒有獨立跑分佐證**

---

## 3. 華為硬體本身的量化數字(廠商 spec,非獨立測試)

- 舊款 Ascend 910C 單顆打不過:GB200 BF16 算力約 3 倍(2500 vs 780 TFLOPS)、記憶體更大(192 vs 128GB)、頻寬更快(8 vs 3.2TB/s)
- 新款 Ascend 950:1 PFLOPS FP8、2 PFLOPS MXFP4;950PR 推理優化版 1.56 PFLOPS FP4
- 系統級 Atlas 950 SuperPoD(8192 顆):華為自報訓練 491 萬 TPS(比自家上一代快 17 倍)、推理 1960 萬 TPS(快 26 倍)——**跟自己上一代比,不是跟 Nvidia 頭對頭**

**跟 AMD 那條的呼應**:華為單顆打不贏,靠機櫃規模+互連打群架——這跟 AMD Helios 的 rack-scale 策略是同一個模式:單晶片打不過 Nvidia,兩邊都繞開「單顆 FLOPS」這個戰場,改往叢集架構+agentic 軟體工具鏈打。

---

## 4. 真正稱得上「研究」的量化 benchmark

1. **CANN Bench**(arXiv 2607.20518,2026-07):第一個針對「AI agent 幫華為 Ascend 生成 kernel」的開放 benchmark,53 個算子、1060 個測試案例,分編譯/正確性/效能三軸評分。能實際檢驗「AI 真的能寫出能跑又快的 Ascend kernel」,可惜沒挖到具體分數表(要抓 PDF)。
2. **CUDABench**(arXiv 2603.02236,2026-02):針對「文字生成 CUDA 代碼」的 LLM benchmark。**關鍵發現**:編譯成功率很高,但**功能正確率很低**——連生成 Nvidia 文件最齊全的 CUDA 都會錯,這給「AI 輕鬆寫出等價生態」的樂觀敘事潑冷水,對 Ascend/CANN 這種更冷門的目標平台只會更難。
3. **LUMI(AMD/ROCm,已跑多年)**:HIP 轉譯層開銷實測約 **2%**、HIPIFY 工具讓大部分應用改動 <5% 程式碼——目前找到最成熟、最被獨立測過的轉譯層數字。對照之下,某產業分析估 CANN Next 的 CUDA 轉譯層開銷約 **15-30%**(來源是產業評論,非學術 benchmark,可信度中等)。

**判斷**:AMD 的 CUDA 相容層比華為成熟得多(2% vs 15-30% 估),即便華為/DeepSeek 這邊敘事更激進。

---

## 5. 開發者生態指標(2026-07-26 新增,回答「多少人投入」)

分兩種:**廣義生態規模**(行銷數字,水分大)vs **窄義專業投入**(更貼近真實產能)。

**規模差距類(自報居多,標可信度)**
- Job postings(LinkedIn,美國):CUDA developer 相關職缺 165,000+ vs ROCm 職缺僅 82 個——量級差距約 2000:1。**注意**:LinkedIn 職缺計數本身很吵(關鍵字比對常 false positive),拿來看「量級落差」不看「精確比例」。
- Stack Overflow 討論深度(質化指標):CUDA 出問題平均有 15 個 SO 答案,ROCm 只有 2 個且常過時——反映「踩坑排解成本」,不是開發者絕對人數。
- 華為官方自報:「Ascend 開發者生態」6.65M 會員 + 8800+ 夥伴(2025-05)——但這是廣義「用過 Huawei Cloud/昇騰生態任何服務」的會員數。同組資料裡更貼近 CUDA 那層的「CANN Next」,預估 2026 年底僅 **15,000+ active developers**。**6.65M vs 15K 的落差本身就是訊號**:廣義生態很大,但真正做底層 kernel 開發的窄很多。
- AMD 官方投入面數字(非採用面):ROCm 團隊人力年增 20%(since 2023)、軟體研發支出佔比從 25%→40%——這是「AMD 砸多少錢」,不能替代「多少開發者真的在用」。

**中立第三方基準測試參與度(比自報人數更硬的訊號)**
- **MLPerf Inference v6.0**(2026-04,MLCommons 主辦、業界最中立跑分):24 個參與組織,AMD 有提交(MI355X + ROCm);**搜尋沒查到華為 Ascend 的提交紀錄**——參不參加中立跑分本身是訊號,但要註記「查無」不等於「確認沒有」,可能是我沒搜到。
- MLPerf Training 6.0:AMD 也有提交(MI355X),同樣沒查到華為對應紀錄。
- CUDABench / CANN Bench 這類中立評測工具本身 2026 年才出現——顯示連學術界要中立評測「AI agent 生成非 CUDA 平台 kernel」的能力,基礎設施都才剛起步,比 CUDA 生態晚了好幾年。

**採用可行性趨勢(方向性指標)**
- PyTorch on ROCm 訓練效能約達 CUDA 的 70-80%(2026),相較 2023 年的 2-3 倍效能懲罰已顯著改善——這條看「改善速度」比看絕對值更有意義。

**這節的判斷**:三個層次的數字都指向同一個結論——**AMD 的開發者生態成熟度領先華為一大截**(職缺量級、SO 討論深度、中立跑分參與、轉譯層開銷實測都是),但華為的「廣義會員數」大到跟「真實 kernel 開發者數」脫鉤,讀這類數字要先問「這是哪一層的人」。

---

## 6. 待觀察的結算訊號(候選,可能收進 profile 預測帳)

- DeepSeek-V4 是否真的在 Huawei Ascend 上量產服務(非訓練實驗)——這是檢驗梁文鋒說法最直接的一步
- CANN Bench 分數公開後,AI-agent 生成 Ascend kernel 的實際 pass rate/效能落差
- CANN Next 到 2026 年底是否真的達到 15,000+ active developers(他自己的預估值)
- 下一輪 MLPerf 是否出現華為 Ascend 提交
- Helios 量產是否如 Lisa Su 所說 Q3 末出貨、Q4 起量,還是重演 SemiAnalysis 唱衰的延遲

## 出處
- SemiAnalysis,《Can AMD break the CUDA Moat? AMD Advancing AI 2026》(2026-07-25,paywall,靠搜尋摘要重建)
- AMD IR/Newsroom, Advancing AI 2026 新聞稿;Moor Insights & Strategy field notes;The Register「AMD vibe codes its way past the CUDA moat」
- 梁文鋒洩漏投資人交流會轉錄(未經 DeepSeek/Bloomberg 證實),BigGo Finance / Dealroom / Kyle Chan(X)/ Fortune 各家報導
- Huawei 官方:Ascend 開源生態新聞稿(2025-09)、Ascend 950/950PR spec
- 學術:CANN Bench(arXiv 2607.20518)、CUDABench(arXiv 2603.02236)、TileLang(arXiv 2504.17577)
- MLCommons MLPerf Inference/Training v6.0 官方結果頁
- 職缺/社群數字:LinkedIn Jobs 搜尋頁(ROCm/CUDA)、產業部落格(aimultiple、thundercompute 等,對 CUDA vs ROCm 比較)

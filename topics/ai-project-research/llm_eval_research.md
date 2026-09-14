# LLM Eval 與 Benchmark 設計 研究筆記

> 研究時間：2026-05-10 ｜ **全面刷新：2026-09-12**
> 範圍：(1) 各領域主流 benchmark 設計手法 (2) 個人 / 小團隊應用層 eval 的有效設計
> 刷新做了什麼：飽和現況全部重查；補進四塊原本沒有的東西（ARC-AGI 系列、METR time horizon、GDPval、AA Intelligence Index 成分）；新增〈固定追蹤清單〉與〈口徑陷阱〉兩節。原有方法論結論（SOP、工具對照、pitfall）四個月後複查仍成立，未改。

## 一句話總結

公開 benchmark 用來「選模型」，自己的 eval 用來「迭代產品」——前者你看排行榜就好，後者必須自己動手寫，因為它就是你產品 spec 的可執行版本。

**2026-09 補一句**：現在看排行榜也不夠了。單一榜的鑑別力只能撐約一季，而且**量尺本身的誤差常常大於模型之間的差距**——要固定看一組互補的讀數，並且記住每個讀數的版本（見〈固定追蹤清單〉）。

## 核心概念

1. **Benchmark ≠ Eval**：Benchmark 是給研究社群用的「全行業考卷」（MMLU、SWE-bench 等），eval 是你自己對應用的回歸測試。前者飽和不代表後者就 OK。
2. **Saturation 問題**：benchmark 的鑑別力壽命約一季，**輪替速度本身就是要追蹤的量**。2026-09 現況——
   - **已退役**（分數差已小於噪音）：HumanEval、MMLU（Saturation Index 90%）、MMLU-Pro、GPQA Diamond（94.3%）、MATH-500（96%）、**ARC-AGI-1**（90%+）、**ARC-AGI-2**（GPT-6 Astra 95%，2026-09-04）
   - **正在飽和**：HLE 已從 2026-05 的 ~46% 漲到 **65%**（Claude Fable 5.1，2026-09-10），前三名只差 0.5 個百分點；DeepSWE v1.1 榜首 gpt-6-astra 74%±3%、gemini-3.8-flash 74%±1%、claude-opus-5 74%±4% 三條誤差帶完全重疊
   - **仍有空間**：**ARC-AGI-3**（互動式，Opus 5 最高 30.16%；半年前前沿還不到 1%）、SWE-bench Pro、FrontierMath、BBEH
   - 要分辨的不再是名次，是**誤差帶有沒有分開**。
3. **Contamination（資料污染）**：早期 benchmark 題目進了訓練集，分數虛高。三種對抗手法現在都有實例：滾動更新題目（LiveCodeBench、HLE-Rolling）、私有測試集（AutomationBench-AA）、從零寫題且不進上游 repo（DeepSWE）。HumanEval 是反例。
4. **Reward Hacking**：2026/04 Berkeley RDI 公告顯示 8 大主流 agent benchmark 全部可被刷分技巧攻破——所以任何單一分數都該打折，配第三方獨立評分 + 自己的 held-out set。
5. **量尺精度：2026 的真問題（2026-09-12 新增，本次刷新最重要的一條）**
   題目難不難已經不是瓶頸，**判分準不準才是**。兩個實測案例：
   - **HLE 的答案本身有問題**：FutureHouse 審查化學／生物文字題，發現 **29±3.7%** 的標準答案與同儕審查文獻直接衝突；Scale AI 估錯誤率 18%；官方承認約 18% 並啟動 rolling revision。HLE-Verified（arXiv 2602.13964）逐題驗證後只留下 668 題。→ **65% 這個分數的天花板不是 100%**。
   - **SWE-bench Pro 的 verifier 會誤判**：隨機 30 題審計，8.5% 假陽性、**24% 假陰性**（DeepSWE 為 0.3% / 1.1%）。近四分之一的正確解被判失敗，而且低估幅度因模型而異。
   **推論**：當量尺誤差（18-29%、24%）大於模型之間的差距（0.5-5 個百分點）時，排名是噪音。**看榜前先問這個榜的判分審計做過沒有。**
6. **合成指數會改版，跨時間比較會斷裂（2026-09-12 新增）**：見〈口徑陷阱〉。AA Intelligence Index 在 v4 把標尺整個重標定（頂尖模型從 73 分降到 50 分以下，刻意留 headroom），v4.3 又換掉成分。**讀數名稱沒變，敏感度整個變了**——任何綁絕對門檻的規則都會在改版時靜默失效。
7. **Eval 三大評分方式**：(a) 程式碼判斷（exact match / unit test）、(b) LLM-as-judge、(c) 人類標註。優先順序就是這個。

## 公開 benchmark 速覽（按領域）

### 知識與推理

> 狀態欄 as_of 2026-09-12。

| Benchmark | 設計手法 | 2026-09 狀態 | 何時看 |
|---|---|---|---|
| MMLU | 57 學科多選題，4 選 1 | **退役**（Saturation Index 90%） | 不看 |
| MMLU-Pro | 加大難度、10 選 1、加推理題 | **退役** | 只在評估小模型時 |
| GPQA Diamond | 博士級理化生選擇題 | **退役**（94.3%） | 只在評估中階模型時 |
| MATH-500 | 數學題 | **退役**（96%） | 不看 |
| HLE（Humanity's Last Exam） | 全球專家出題 3000+，跨 100+ 領域，刻意難 | **正在飽和**：65%（Fable 5.1，2026-09-10），前三名差 0.5pp。⚠️ **標準答案本身 18-29% 有爭議**（見核心概念 5）；HLE-Rolling 滾動換題、HLE-Verified 驗證後只留 668 題 | 還能看，但要看 Verified 版或 Rolling 版，別看原版絕對分數 |
| AIME | 30 題奧林匹克數學短答 | 前沿已高分，區分力下降 | 看中階模型數學 |
| **ARC-AGI-1** | 網格抽象推理，人類易、模型難 | **退役**（90%+） | 不看 |
| **ARC-AGI-2** | 加難的靜態網格題 | **退役**：GPT-6 Astra 95%（2026-09-04）、GPT-5.6 Sol 92.5%、Opus 5 90.4% | 不看 |
| **ARC-AGI-3** | **互動式**環境推理，不是靜態解謎 | **未飽和且鑑別力最強**：Opus 5 最高 30.16%；2026 上半年前沿模型還不到 1%，人類 100% | 看「面對全新互動環境的適應力」——最接近「沒見過的事」 |
| **FrontierMath / BBEH** | 研究級數學 / 加難版 BIG-Bench | 未飽和 | 看數學與推理深度 |

**ARC-AGI 三代的落差是本次刷新最值得記的一組數字**：同一批模型，ARC-AGI-2 拿 90-95%，ARC-AGI-3 拿 30%。靜態題型已被攻克，**互動、多輪、要在環境裡摸索的題型還差很遠**——這條落差正好對上 agent 產品的真實失敗模式。

### 程式碼

| Benchmark | 設計手法 | 何時看 |
|---|---|---|
| HumanEval | 164 題 Python，給 docstring 補 function body | 已死，僅供歷史對照 |
| LiveCodeBench (Pro) | 從 LeetCode/AtCoder/Codeforces 持續抓 cutoff 之後的新題，避污染；Pro 版用 Elo 評分 | 看純演算法能力 |
| SWE-bench Verified | 真實 GitHub issue + repo，要 patch 過 test | 看「能不能改現成 codebase」 |
| SWE-bench Pro | Verified 的更難版 | 2026 主流 agent coding 評分 |
| DeepSWE（Datacurve） | 113 題**從零寫**的任務，橫跨 91 個 ≥500 star 活躍 repo、5 語言；題目不改編自既有 commit/PR，也不 merge 回上游，靠這兩點擋污染。程式化 verifier，只認可觀察行為不認實作 | 看「長時程、多檔案」的 agent 能力；跟 SWE-bench Pro 併看 |
| Terminal-Bench（現行 **v4.0**） | 給 shell 任務看 agent 能不能搞定；v4.0 為 AA Intelligence Index v4.3 採用版本（66 題） | 看 CLI agent。⚠️ 版本迭代快，引用必須標版號 |
| SciCode | 科學計算程式 | 看科研場景 |

#### DeepSWE 深入（2026-09-12 補）

> 來源：[repo](https://github.com/datacurve-ai/deep-swe)（Apache-2.0）、[blog 2026-05-26](https://deepswe.datacurve.ai/blog/deepswe)、[arXiv 2607.07946](https://arxiv.org/abs/2607.07946)、[leaderboard](https://deepswe.datacurve.ai/)（v1.1，113 題，更新於 2026-09-03）

**它想修的是 SWE-bench 的三個結構性破口，不是「再出難一點的題」。**

1. **污染**：題目由受雇工程師從零構思，不改編既有 commit/PR，寫完也不 merge 回上游 repo。SWE-bench 系列的題目本身就在公開 git 歷史裡，這是 [`benchmark-saturation-hides-real-gap`](../ai-industry-reading/cards/benchmark-saturation-hides-real-gap.md) 說的 gap 的來源之一。
2. **任務規模**：prompt 比 SWE-bench Pro 短（2,158 vs 4,614 字元），但要寫的東西多得多。

   | | SWE-bench Verified | SWE-bench Pro | DeepSWE |
   |---|---|---|---|
   | 平均 prompt 長度 | 1,700 字元 | 4,614 字元 | 2,158 字元 |
   | 平均新增行數 | 10 | 120 | **668** |
   | 平均編輯檔案數 | 1 | 5 | **7** |

   「短敘述 + 大改動」正是真實工單的形狀，也是 long-horizon 能力真正被壓測的地方。
3. **Verifier 精度**（本份筆記第 4 點 reward hacking 的直接解方）：隨機抽 30 題人工審計判分正確性——

   | | 假陽性 | 假陰性 |
   |---|---|---|
   | SWE-bench Pro | 8.5% | 24% |
   | DeepSWE | **0.3%** | **1.1%** |

   SWE-bench Pro 有近四分之一的正確解被判失敗。**這代表 Pro 的絕對分數是低估的，而且低估幅度因模型而異** —— 跨模型比較的噪音比誤差帶顯示的更大。

**v1.1 leaderboard（2026-09-03，pass@1，全部跑同一個 mini-swe-agent harness）**

| 模型 | 分數 |
|---|---|
| gpt-6-astra | 74%±3% |
| gemini-3.8-flash | 74%±1% |
| claude-opus-5 | 74%±4% |
| gpt-5.6-sol | 73%±3% |
| claude-fable-5 | 70%±3% |
| glm-5.3 | 69%±3% |
| kimi-k3 | 69%±5% |
| grok-4.6 | 67%±2% |
| gpt-5.6-luna | 67%±4% |
| gpt-5.5 | 67%±6% |

⚠️ **v1 與 v1.1 分數不可直接比**：gpt-5.5 在 v1（2026-05-26）是 70%±3%，v1.1 是 67%±6%。要看時間序列必須鎖同一版本。

**兩個可直接用的讀數**

- **前沿三家已無統計差異**：74%±3 / ±1 / ±4 三條誤差帶完全重疊，名次是噪音。
- **開源差距 5 分**：glm-5.3 69% vs 榜首 74%，在一個**刻意防污染**的新 benchmark 上仍然如此——這比在舊 benchmark 上追平更有說服力，因為排除了「背過題庫」的解釋。接 [`open-source-is-the-commoditization-clock`](../ai-industry-reading/cards/open-source-is-the-commoditization-clock.md)。

**限制（官方自陳）**：單一標準 harness（mini-swe-agent），測不出各家原生 agent 的實力；只收 ≥500 star 的活躍 repo；bug 定位與重構類題目偏少；只有 TypeScript / Go / Python / JavaScript / Rust 五種語言；prompt 仍比真實開發者對話長。

**順帶解掉一則待驗證**：`inbox.md`（worktree 版 L1441）記有二手轉述「DeepSWE 測出 DeepSeek V4-Pro 只有 8% pass@1，對比 GPT-5.5 的 70%」，當時原始出處查不到、標記未驗證。官方 v1 leaderboard 證實此數字：deepseek-v4-pro 8%±3%、gpt-5.5 70%±3%（2026-05-26 版）。**轉述屬實，但那是 v1 的數字，v1.1 已重測。**

### Agent / Tool use

| Benchmark | 設計手法 | 何時看 |
|---|---|---|
| GAIA | 450 題真實助理任務（含搜尋、檔案、多模態），有 unambiguous 答案 | 通用 assistant |
| TAU-bench / tau2-bench | 模擬零售、航空、語音、檢索場景，LLM 扮演真實使用者，要遵守 policy 文件——「訂對機票但違反退票規則」算失敗 | 看企業 agent，最貼近真實部署 |
| AgentBench | 8 個環境（OS shell、SQL、KG、卡牌、家務、購物、瀏覽、卡牌） | 看廣度 |
| WebArena | 真實網站環境的 web 任務 | 看 browsing agent |
| BFCL（Berkeley Function-Calling Leaderboard） | tool-calling 各種子任務 | 看 tool use 細節 |
| **GDPval / GDPval-AA v2** | 1,320 個真實職業任務，由平均 14 年經驗的專業人士出題，橫跨 9 大產業、44 種職業；產出是真實交付物（文件、簡報、圖表、試算表），跟人類專家盲評 pairwise。AA 版 220 題，Elo 制、人類基準錨定 1000 | **看「對人類專家的相對水準」**，是目前最接近經濟價值的量尺 |
| **AA-Briefcase / AutomationBench-AA** | AA 自建的 agent 任務集，後者為**私有測試集**（防污染） | 看 agentic 能力；AA Index v4.3 裡 agent 類合計佔 30%，權重最高 |

### 長時程能力（2026-09-12 新增，原本整份筆記沒有這一類）

**[METR Time Horizon](https://metr.org/time-horizons/)** 量的不是分數，是**任務長度**：找出 agent 以 50% 成功率能完成的任務，對應人類專家要花多久。這是「模型一直在提高」最直接、單位最有意義的軌跡指標。

| 模型 | 50% time horizon |
|---|---|
| GPT-4o | 6 分鐘 |
| Claude Sonnet 3.7 | 60 分鐘 |
| Claude Opus 4 | 101 分鐘 |
| o3 | 121 分鐘 |
| GPT-5 | 214 分鐘 |
| Claude Opus 4.5 | 320 分鐘（5.3 小時） |

*Time Horizon 1.1（2026-01-29）口徑，228 題任務集。*

**倍增速度在加快**，這是關鍵讀數：

| 觀察窗 | 倍增期 |
|---|---|
| 整體（2019 起） | 196.5 天 |
| 2023 起 | **130.8 天** [107, 161] |
| 2024 起 | **88.6 天** |

TH1 → TH1.1 改版後，2023 起的倍增期從 165 天縮到 131 天，METR 自評「進度估計快了 20%」。

**限制（官方自陳，必讀）**：超過 16 小時的測量以現有題庫**不可靠**；人類耗時估計偏高（估算者 context 不足）；題目以軟體工程／ML／資安為主，比真實經濟勞動「乾淨」得多；曲線是 logistic fit，**沒有 bootstrap 信賴區間**。所以 horizon 數字要當**量級**讀，不要當精確值。

### 經濟價值（2026-09-12 新增）

GDPval 這一類的意義跟上面所有 benchmark 都不同：它不問「模型會不會做這題」，問「**交付物跟人類專家比，誰的好**」。GDPval-AA v2 榜（2026-09）：Claude Fable 5.1 (Max) 1764、Fable 5.1 (Xhigh) 1745、Opus 5 (Max) 1735、Muse Spark 1.3 (max) 1703、**GLM-5.3 (max) 1667（第 6，開源）**、GPT-5.6 Sol (max) 1624（第 19）。人類基準 = 1000。

OpenAI 原始 GDPval 報告另有一條常被引用的數字：前沿模型完成這些任務比人類專家**快約 100 倍、便宜約 100 倍**。這是自報數字，且「完成」不等於「品質相當」，引用時兩者要一起講。

### RAG

RAGAS 提供四個核心指標，**不需要 ground-truth label** 就能跑（這是它流行的關鍵）：

- **Faithfulness**：回答的每個 claim 能不能在 retrieved context 找到支持（抓幻覺）
- **Answer Relevancy**：回答有沒有正面回應問題（抓「答非所問但很真實」）
- **Context Precision**：retrieved chunk 中真正相關的比例（抓召回品質）
- **Context Recall**：相關內容被 retrieve 到的比例（需要 ground truth）

## 固定追蹤清單（2026-09-12 新增）

單一榜的鑑別力撐不過一季，所以不追單一榜，**追一組互補維度**。每個維度只留一個讀數，避免重複看同一件事。

### 第一組：能力軌跡（4 個）

| # | 維度 | 讀數 | 2026-09-12 值 | 為什麼是它 | 頻率 |
|---|---|---|---|---|---|
| 1 | **綜合位置** | [AA Intelligence Index](https://artificialanalysis.ai/models) **v4.3** | 封閉最佳 53（Fable 5.1、GPT-6 Astra）；開源最佳 45（GLM-5.3 max） | 10 個 benchmark 合成，agent 類佔 30%；已主動汰換飽和成分 | 月 |
| 2 | **長時程軌跡** | [METR time horizon](https://metr.org/time-horizons/) 倍增期 | 2023 起 131 天 / 2024 起 89 天；Opus 4.5 = 320 分鐘 | 唯一用「任務長度」而非百分比的量尺，不會飽和 | 季 |
| 3 | **真實軟體工程** | [DeepSWE](https://deepswe.datacurve.ai/) v1.1 | 榜首 74%（三家並列）；開源 glm-5.3 69% | 防污染 + verifier 假陽性 0.3%，目前判分最乾淨的 coding 榜 | 季 |
| 4 | **新環境適應力** | ARC-AGI-3 | Opus 5 30.16%（最高） | 唯一還有大空間的推理榜；互動式，對上 agent 的真實失敗模式 | 季 |

**為什麼不是 SWE-bench**：Verified 已觸頂（95%），Pro 的 verifier 有 24% 假陰性。要看 coding 用 DeepSWE，要看 CLI agent 用 Terminal-Bench v4.0。

**為什麼不是 HLE**：標準答案 18-29% 有爭議，原版絕對分數不可用。真要看知識深度，看 HLE-Verified（668 題）或 HLE-Rolling，別看原版。

### 第二組：綜合評比（2 個讀數）

> 2026-09-14 定稿。原本列了三個讀數（開源差距分差、GDPval Elo、能力單價），owner 判定過度工程，砍掉重做。

**要回答的問題：各家廠商現在排第幾？Google 還在不在第二梯隊？**

#### 挑指標的三條原則

1. **主秤用合成指數，不要自己湊一籃子。** AA Intelligence Index 已經合成 10 個 benchmark（agent 類佔 30%），而且會主動汰換飽和成分。自己維護一堆單項榜等於重做他們的工作，還會漏掉改版。
2. **比廠商，不比模型。** 每家只取最好的那一列，得到一張 5 行的廠商榜。不需要管各家發了幾個模型、幾種 effort 設定。
3. **看相對位置，不看絕對分數。** AA 在 v4 把標尺整個重標定過（頂尖從 73 掉到 50 以下），分數跨版本不可比；廠商之間的相對序改版時同時重評，天然可比。

#### 讀數一（主秤）：AA Intelligence Index 廠商榜

每家取最好的一列，四欄一起看。四個數字**同一個來源、同一張表**，不增加維護成本。2026-09-14，v4.3 口徑：

| 廠商 | 最佳模型 | 智力 | 速度 (t/s) | 首字延遲 | 價格 ($/1M) |
|---|---|---|---|---|---|
| Anthropic | Claude Fable 5.1 (max) | **53** | 67 | 235s | $7.63 |
| OpenAI | GPT-6 Astra (max) | **53** | 60 | 321s | $3.26 |
| Meta | Muse Spark 1.3 (max) | 48 | 241 | 22s | $1.60 |
| xAI | Grok 4.6 (high) | 44 | 59 | 32s | $1.86 |
| Google | Gemini 3.8 Flash (high) | 41 | **305** | 18s | **$1.24** |

**只看智力欄會把 Google 讀錯。** 它智力第 5，但速度第 1（AA 測過最快）、價格最低、首字延遲比 Anthropic／OpenAI 快 13-18 倍。

⚠️ **Meta 的 frontier 線是 Muse，不是 Llama。** Meta Superintelligence Labs 2026-04-08 推出 Muse Spark，閉源不開權重。Llama 4 Maverick 在 AA 上只有 9 分——拿 Llama 當 Meta 代表會把結論做反（本檔 2026-09-14 修正過一次這個錯）。

#### Google 走的不是同一條賽道（2026-09-14）

三個事實：

1. **Google 榜上最好的是 Flash，不是 Pro。** Gemini 3.1 Pro Preview 只有 30 分。它拿小模型在跟別人旗艦比，還排到第 5 家。
2. **2026-09-02 發布的 3.8 Flash，是六週內第三個 Flash 版本**，而且建在 3.7 Flash 上、沒換 base model，靠多燒 thinking token 拉分數。
3. **速度與價格是它唯一的第一名**：305 t/s、$1.24、TTFT 18 秒。

合起來看，Google 的資源不在推智力上限，在壓**單位成本與延遲下的可用智力**。這跟它自己講的收益出口對得上——Android AI 生態、個人助理、眼鏡這類要跑在十億台裝置、每天幾十次互動的場景，決定能不能做的是成本與延遲，不是最高智力。

**但這不是安全牌**：Meta 的 Muse Spark 1.3 在同一條軸上表現更好——241 t/s、$1.60，智力還贏 Gemini **7 分**。Google 更快更便宜，Meta 更聰明也夠快。**效率這條路 Google 沒有獨佔。**

→ 對 GOOG wiki 假設 #4 的意涵：那條驗的是「長期收益選擇權的前提條件」。如果前提是「模型夠好到能撐起 Android／助理／眼鏡」，**智力排名掉到第 5 本身不等於前提失效**；真正的失效條件比較像「在效率軸上也被追上」。這是量尺問題，需要 owner 拍板，本檔不替投資決策定案。

#### 讀數二（防呆）：DeepSWE 廠商榜

同樣取每家最好的一列。2026-09-03，v1.1 口徑：gpt-6-astra 74%±3%、**gemini-3.8-flash 74%±1%**、claude-opus-5 74%±4%、glm-5.3 69%±3%、grok-4.6 67%±2%。

**為什麼需要第二個讀數**：現成的反例就在 Google 身上——Gemini 3.8 Flash 在 DeepSWE 並列第一，在 AA 主秤只排第五家。**兩張表不一致，代表那家在特定任務強、綜合位置弱**，這個落差本身就是訊號，比任何單一分數都有用。

選 DeepSWE 當防呆的理由：它不在 AA 的成分裡（AA 的 coding 類用 Terminal-Bench v4.0 + SciCode），所以不是同一件事看兩遍；而且它是目前判分最乾淨的榜（verifier 假陽性 0.3%）。

#### 誰刷新（2026-09-14 實作完成）

`investment_note/tools/quant_feed_fetch.py` 自動抓 AA 寫進 `investment_note/data/metrics.jsonl`。跑 `python3 tools/quant_feed_fetch.py --write`。2026-09-14 這輪把它從 6 個 metric 擴到 15 個：

| metric | 軸 | 2026-09-14 值 |
|---|---|---|
| `ai_intelligence_index` / `peer_…` / `…_frontier_best` | 綜合 | Google 41 ／ Meta 48 ／ 全榜 53 |
| `ai_index_speed` / `peer_…` | 效率 | Google 305 t/s ／ Meta 241 t/s |
| `ai_index_latency` / `peer_…` | 效率 | Google 17.67s ／ Meta 22.23s |
| `ai_index_cost_per_task` / `peer_…` | 效率 | Google $1.24 ／ Meta $1.60 |
| `ai_index_vision` / `peer_…` / `…_frontier_best` | 視覺（MMMU-Pro） | 85.61% ／ 74.34% ／ 86.88% |
| `ai_index_coding` / `peer_…` / `…_frontier_best` | 程式（SciCode） | 59.84% ／ 59.72% ／ 63.08% |

效率三欄跟綜合分**來自同一張表的同一列**（AA 榜單有 9 欄），不需要額外請求；排名仍以智力分決定，效率數字是該列附帶的——所以那不是「該廠最快的模型」，是「該廠最聰明那個模型有多快」。

⚠️ `cost_per_task` 是**每任務成本**，不是 $/1M tokens。AA 跑固定任務組合計價，推理型模型多燒 thinking token 就更貴。不可與 ledger 裡 `LLM_API_PRICING` 的 `USD_per_1M_tokens` 相比，分母不同。

#### DeepSWE 為什麼不自動抓（2026-09-14 查證後放棄）

它是最想要的防呆讀數——防污染、verifier 假陽性 0.3%。但**它不發布機器可讀結果**：

- 首頁 leaderboard 是一張散點圖，分數只存在於 SVG 的 y 座標裡，文字節點只有模型名與 effort 標籤，**分數本身沒有以文字出現**
- `/api/leaderboard` 回 404
- GitHub repo（`datacurve-ai/deep-swe`）只有 113 題的任務定義（Dockerfile、grader、solution patch），**沒有任何成績檔**

靠像素反推會往 ledger 寫入近似值，違反那支 script 的核心原則（「A failed parse never becomes a number」）。**所以 DeepSWE 維持手動季看**，等 Datacurve 發布 JSON 或成績檔再回來接。

替代品是 **SciCode**（AA 的 evaluation 頁，格式與 MMMU-Pro 相同，既有 parser 直接可用）。⚠️ 但要記住：**SciCode 是 Intelligence Index 十項成分之一**，所以它是綜合分的拆解，**不是獨立第二意見**——防呆效果比 DeepSWE 弱。

#### 入口：掛在既有的每日排程上（2026-09-14 完成）

**沒有新增排程。** 接進既有的 `com.atomo.repo-health`（launchd，每天 04:40），在 `investment_note/tools/run_repo_health.sh` 裡多一步：

```
1. quant_feed_fetch.py --write   # 抓，append 到 data/metrics.jsonl
2. repo_health.py check          # 檢查，唯讀
```

順序有意義：`repo_health` 的 freshness 檢查問的就是「市場序列多久沒進台帳」，抓取必須先跑，否則它檢查的是昨天的狀態。在此之前它只會印一行「跑：python3 tools/quant_feed_fetch.py --write」當建議，而**沒有任何地方真的會去跑**——GetDeploying 的 parser 就是這樣壞掉沒人發現的。

`plist` 沒動，所以不需要 `launchctl` 重載。

## 口徑陷阱（2026-09-12 新增）

引用任何 benchmark 分數前，先過這五關：

**一、合成指數會整個重標定。** AA Intelligence Index 在 v4 把標尺重新校準：頂尖模型從舊版 **73 分掉到 50 分以下**，這是刻意留 headroom，不是模型退步。v4.3 再換成分（Terminal-Bench 升 4.0、加入私有測試集 AutomationBench-AA），且正在往 v5 rollout。**讀數名稱沒變，敏感度整個變了。**

→ **任何綁在合成指數絕對值上的門檻規則，都會在改版時靜默失效。** 舉例：舊標尺下「開源模型達到 50 分」是中段成就（2026-06-29 快照，封閉最佳 60），在 v4.3 下 50 分已經排到全榜第 4 名（封閉最佳才 53）。同一條規則，改版前後的觸發難度差了一個量級，而且不會有任何警告。**解法：改用同版本內的相對差距。**

**二、benchmark 自己也改版，跨版分數不可比。** DeepSWE v1（2026-05-26）gpt-5.5 = 70%，v1.1 = 67%。Terminal-Bench 現行 v4.0。引用必須寫版號 + 日期。

**三、量尺誤差可能大於模型差距。** HLE 標準答案 18-29% 有爭議、SWE-bench Pro 24% 假陰性，而榜首之間常只差 0.5-5 個百分點。**先問這個榜的判分審計做過沒有。**

**四、自報 vs 第三方。** 模型廠自報分數無獨立複現時要標注（既有慣例，沿用）。DeepSWE、METR、AA 屬第三方；各家發布會的數字屬自報。

**五、harness 會蓋過模型差異。** DeepSWE 全部跑同一個 mini-swe-agent，官方自陳這測不出各家原生 agent 的實力。看到「某模型在某榜偏低」時，先確認是模型弱還是 harness 不合。呼應 [`harness-beats-model`](../coding-agents/cards/harness-beats-model.md)。

## 個人 / 小團隊 eval 設計：可執行 SOP

這是這份筆記最有價值的部分。綜合 Anthropic、OpenAI、Pragmatic Engineer 的指引整理。

### 第一階段：從零起步（第 1 週可完成）

```
Step 1. 收集 20-50 個真實 case
        - 不要憑空想，從這幾個地方挖：
          * 你自己手動測試 prompt 時的 case
          * 用戶投訴 / bug 回報
          * 你「直覺覺得會出錯」的 edge case
        - 每個 case 寫成 (input, expected_output_or_criteria) 的格式

Step 2. 對每個 case 寫「兩個專家會給同樣 pass/fail 判斷」的標準
        - 模糊的標準（"回答要好"）→ 沒用
        - 明確的標準（"回答必須包含日期且格式為 YYYY-MM-DD"）→ 有用

Step 3. 平衡正負樣本
        - 不要只測「該做時有做」，也要測「不該做時沒做」
        - 例：搜尋 agent 不只測「該搜尋有去搜」，也要測「不該搜尋時別亂搜」

Step 4. 選評分方式（優先順序）
        a. 能用程式碼判斷就用（exact match、regex、JSON schema、unit test）
        b. 不行才用 LLM-as-judge
        c. 真的測不了的（創意、語感）才用人類

Step 5. 跑 baseline，記錄分數
        - 第一次跑得 60% 不可怕，可怕的是不知道是 60%
```

**關鍵原則**：「imperfect evals deployed early outperform perfect evals delayed」——不完美但今天能跑的 eval，比完美但下個月才寫好的有用。

### 第二階段：每次改 prompt / 換模型都跑（持續優化期）

把 eval 套進你的 PR / change 流程：

```python
# pseudo-code; tool-agnostic
for case in eval_set:
    actual = run_my_app(case.input)
    score = grade(case.expected, actual)
    record(case.id, score, actual)

assert overall_pass_rate >= last_known_baseline  # gate
```

每次改：
1. 在改之前先跑一次（記錄當前分數）
2. 改完再跑（看有沒有 regression）
3. 看 **diff**，不只看總分——95% → 95% 也可能是 case A 變對 case B 變錯

### 第三階段：擴張 eval set（成熟期）

- 每收到一個生產環境的 bug 回報 → 加進 eval set
- 每隔幾週看 transcript：模型在哪些 case 系統性錯
- 監控 saturation：當 eval 分數 100% 表示 eval 太簡單，要加新題

### LLM-as-judge：用對的方式

LLM-as-judge 便宜快但有偏誤，要這樣防：

| 偏誤 | 機制 | 修正 |
|---|---|---|
| Position bias | 比較兩個答案時偏第一個（GPT-4 約 40% 不一致） | A/B 都跑兩次互換位置，取一致才算 |
| Verbosity bias | 偏好長答案（約 +15% 灌水） | rubric 直接加「簡潔度」項 + 對過長答案扣分 |
| Self-enhancement | 偏好自己家模型（+5-7%） | 換不同家當 judge，或多 judge 投票 |
| Fallacy oversight | 看不出邏輯謬誤 | 結構化 rubric 拆維度評分，每維度單獨判 |

實務技巧：
- 用 **PASS/FAIL 二元判斷** 比 **1-10 分** 穩定多了
- 給 judge **「Unknown」逃生口**——資訊不足就不要硬猜
- judge prompt 裡只給 transcript 和 retrieved context，**不要讓 judge 用自己的知識評分**（會幻覺）
- 定期用人工抽 20-30 個樣本校準 judge，看 judge 跟人類同意率

## 工具選擇對照（2026/05 現況）

| 工具 | 定位 | 優點 | 缺點 | 何時用 |
|---|---|---|---|---|
| **Promptfoo** | CLI + YAML 配置 | 50+ red-team 模板，本地跑 | 2026/03 被 OpenAI 收購（86M），社群擔心廠商獨立性 | 安全/紅隊測試首選 |
| **DeepEval** | Python pytest 框架 | 50+ 內建 metrics（G-Eval、hallucination、faithfulness 等），跟 pytest CI 整合 | 偏 Python 生態 | CI/CD gating 首選 |
| **Braintrust** | SaaS 平台 | 線上 trace、人類標註、PM 跟工程師共用界面 | 商業產品 | 團隊協作 + 線上監控 |
| **LangSmith** | LangChain 系平台 | LangGraph 整合最深、step-level 評分、400 天 trace | 跟 LangChain 綁很深 | 用 LangGraph 的 agent |
| **RAGAS** | RAG 專用 | 不需 ground truth、4 個現成指標 | 只 cover RAG | RAG 專案標配 |

**2026 業界共識組合**：
- 個人 / 早期：DeepEval 或 Promptfoo 單兵作戰，本地跑就好
- 工程團隊：**DeepEval（CI gating）+ Braintrust（線上 trace + 標註）** 已成事實標準

## 常見 pitfall（自己踩過 / 看別人踩過的）

1. **過度依賴公開 benchmark 分數**：Claude/GPT 在 SWE-bench 80% 不代表在你的 codebase 80%
2. **Eval set 太小且不平衡**：只有 5 個 case，且都是 happy path
3. **Grader 過於 rigid**：要求 agent 走特定步驟，懲罰了「走不同路但結果對」的解
4. **環境沒隔離**：上一個 case 留下的檔案污染下一個 case
5. **改 prompt 不跑 eval**：靠手動測 1-2 個 case 拍腦袋
6. **LLM judge 沒校準就上**：判斷標準漂移，自己還不知道
7. **混淆 capability eval 和 regression eval**：前者要難（pass rate 低才有空間爬），後者要穩（接近 100%）

## 適用場景

| 你在做什麼 | 該怎麼處理 eval |
|---|---|
| 寫單次 script / 一次性任務 | 不用寫 eval，肉眼看就好 |
| Prompt 會被改超過 3 次 | 至少寫 10-20 個 case，手動跑 |
| 上 production / 有外部用戶 | 必須有 CI eval gating + 線上 trace |
| RAG 應用 | RAGAS 四指標 + 自己領域題 |
| Agent / tool use | 至少測「該呼叫 tool」+「不該呼叫 tool」兩種 case |
| 純客服 chat | 模仿 TAU-bench 思路：寫 policy 文件 + 模擬真實用戶 |

## 給個人開發者的最小路徑

如果你只想花一個下午搞個 eval，不要追求完整：

1. 開個 `evals/cases.jsonl`，丟 20 個 (input, expected) 進去
2. 寫個 50 行的 Python script：跑模型、比對、印分數
3. 改 prompt 前後各跑一次，看 diff
4. 加進 git，每次 commit 前跑

這樣你已經贏過 80% 沒做 eval 的個人專案了。等到 case 累到 100+、跑得太慢、或要分享給隊友看，再考慮 DeepEval / Braintrust。

## 相關資源

### 必讀
- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — 8 步驟 SOP，本份筆記主要參考
- [OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Pragmatic Engineer — A pragmatic guide to LLM evals](https://newsletter.pragmaticengineer.com/p/evals)

### Benchmark 排行榜
- [BenchLM — State of LLM Benchmarks 2026](https://benchlm.ai/blog/posts/state-of-llm-benchmarks-2026) — 第三方獨立評分，比官方數字可信
- [HAL Princeton — GAIA Leaderboard](https://hal.cs.princeton.edu/gaia)
- [Awesome Agents — Agent Leaderboard](https://awesomeagents.ai/leaderboards/agentic-ai-benchmarks-leaderboard/)
- [LiveCodeBench](https://livecodebench.github.io/)
- [DeepSWE Leaderboard](https://deepswe.datacurve.ai/) — 防污染的 long-horizon coding benchmark，verifier 假陽性 0.3%（2026-09-12 加）
- [METR Time Horizons](https://metr.org/time-horizons/) — 用任務長度而非百分比計量，不會飽和（2026-09-12 加）
- [AA Intelligence Index 方法論](https://artificialanalysis.ai/methodology/intelligence-benchmarking) — v4.3 的 10 個成分與權重；查版本前必讀（2026-09-12 加）
- [GDPval-AA v2](https://artificialanalysis.ai/evaluations/gdpval-aa) — 對人類專家的 Elo，人類基準 1000（2026-09-12 加）
- [ARC Prize](https://arcprize.org/) — ARC-AGI-1/2/3（2026-09-12 加）

### 量尺精度（2026-09-12 新增）
- [HLE-Verified（arXiv 2602.13964）](https://arxiv.org/abs/2602.13964) — 逐題驗證 HLE，留下 668 題
- [FutureHouse — 約 30% 的 HLE 答案是錯的](https://www.futurehouse.org/research/hle-exam) — 化學／生物文字題 29±3.7% 與文獻衝突
- [DeepSWE blog](https://deepswe.datacurve.ai/blog/deepswe) — verifier 假陽性／假陰性審計方法
- [When Leaderboards Stop Separating（arXiv 2605.18840）](https://arxiv.org/pdf/2605.18840) — 榜單失去鑑別力之後該量什麼

### 工具文件
- [DeepEval GitHub](https://github.com/confident-ai/deepeval)
- [RAGAS Docs](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)
- [Braintrust 替代方案比較](https://www.braintrust.dev/articles/best-promptfoo-alternatives-2026)

### Benchmark reliability 的警鐘
- [Berkeley RDI — How We Broke Top AI Agent Benchmarks](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/) — 為什麼不能信任單一分數
- [Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://llm-judge-bias.github.io/)

### 進階閱讀
- [Galileo — Agent Evaluation Framework 2026](https://galileo.ai/blog/agent-evaluation-framework-metrics-rubrics-benchmarks)
- [Confident AI — RAG Evaluation Metrics](https://www.confident-ai.com/blog/rag-evaluation-metrics-answer-relevancy-faithfulness-and-more)

---

**TL;DR**：別跟著公開 benchmark 起舞——它們半年飽和一次又被 reward hack。對個人應用，下午寫 20 個 case + 50 行 script 就能甩開大多數憑感覺改 prompt 的人。LLM-as-judge 用就用，但要校準、防偏誤、優先用程式判斷。

**2026-09-12 刷新後加一句**：飽和速度已經快到「半年」變「一季」，而且問題從「題目不夠難」變成「**判分不夠準**」——HLE 標準答案 18-29% 有爭議、SWE-bench Pro 24% 假陰性，誤差比榜首之間的差距大。要追就追〈固定追蹤清單〉那 7 個維度，每次引用都帶版號與日期；**絕對門檻不要綁在合成指數上**。

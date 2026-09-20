# AI Engineer 頻道 10 支深掃（2026-09）：收斂方向從「堆結構」翻成「減結構」

> 素材：AI Engineer YouTube 頻道（@aiDotEngineer）的 track playlist，選 10 支跟本 repo 關切最近的 talk，抓 auto-subs 逐字稿逐支深讀。
> 一句話結論：**七月那次掃到的是「價值移向驗證／對齊／結構化 context」，這次十支裡有六支在講反面——把預先堆好的結構拆掉。兩者不衝突，因為減掉的是「預先寫死的結構」，換上的是「按需載入 + 確定性前置過濾 + 客觀證據驗證」。**

## 這個頻道是什麼

swyx（Shawn Wang）和 Ben Dunphy 的 Software 3.0 Inc 辦的會議系列，talk 免費放 YouTube。swyx 2023-06 在 Latent Space 寫〈The Rise of the AI Engineer〉替這個職業命名，同一篇文末宣布第一屆 Summit——造詞和辦會是同一個動作。

讀它要記得講者多半來自 frontier lab 或賣工具的公司，**每支 talk 同時是技術分享和產品行銷**。機制描述可信度高，自報的效果數字要當廠商宣稱看。以下所有數字都照這個標準標註了。

## 六支在講「減法」

**1. 刪掉 95% 的 skill 反而更好**（Nick Nisi, WorkOS）
把 10,000 行文檔的 skill 砍成 553 行「模型常踩的地雷」，講者宣稱執行時間從 68 分鐘降到 6 分鐘。更刺的一個數字：某任務**載入該 skill 正確率 77%，不載入反而 97%**（講者宣稱）。理由是模型已經會寫程式，需要的只是易錯細節的提示，塞完整文檔等於加雜訊。

**2. 規則容量一年漲約 10 倍，但那不代表該塞滿**（Lauren／Lori，逐字稿轉寫不一致）
講者宣稱前沿模型現在能跟 2,000–5,000 條指令，舊的「200 條上限、超過就拆 subagent」已經過時。她同時點出三種新失敗模式：Claude 誤觸安全拒絕、Gemini 燒光 thinking token 直接無輸出、GPT 5.5 寫到一半放棄還抱怨（最難察覺）——**所以不能只看開頭就信輸出**。另引 Chroma 的研究：結構良好連貫的文本比隨機打亂的指令**更早**遇到 context rot（準確度掉 30–50%）。

**3. 能裝進 context 就別加記憶系統**（Stefania Druga, Sakana.ai）
實驗結論：任務若能完整放進 context，記憶 harness「未增加任何能力，只增加成本」（講者宣稱）。而且即使給模型 100% 正確的 Oracle 記憶，它仍可能忽略或誤讀——**檢索命中不等於執行成功**。排序式決策帳本的表現優於向量 RAG 與簡單開關門控。

**4. 砍掉多 agent 流水線**（Abhilash Asokan、Subbiah Sethuraman）
放棄「模仿人類分析步驟拆成多個特化 agent」，理由是交接會遺失脈絡、沒有人負責全局。改成：確定性統計與規則先過濾訊號 → 確認有訊號才喚醒單一主 agent → 主 agent 掌握全局、必要時才派短命 sub-agent。知識圖譜不當檢索層用，當**控制面**，每條邊是一個待驗證假說。

**5. 不要建上千筆 eval 集**（Ben Hylak, Raindrop）
eval 當單元測試寫、在本地跑。換工具或換模型時，龐大測試集可能一次失效 80%（講者宣稱），反而拖慢升級。另一條更硬：**不要讓 agent 負責偵測異常**，異常要用確定性指標抓（例如關鍵字頻率暴增），agent 只負責調查。日誌分群定位不了根因也看不出時序。

**6. 先修知識庫，不要在檢索層硬接爛資料**（Raj）
做法是「需求驅動」：給 agent 歷史工單，讓它因為缺資訊而列出缺口清單，人補完後 agent 自動歸納建檔（講者宣稱 14 輪循環後信心度從 1.5 升到 4.4）。重點是**在檢索前**批次跑 gap scanner 修文檔，不要在對話中逐次補。長 context 下，整理好的 curated context 效果勝過 Graph RAG。

## 四支不是減法，但形狀一致

**7. LinkedIn 的 500 個 playbook**（AJ）
這支表面上是「更多結構」，但機制仍是按需載入：每個 playbook 單一職責、要用才讀。他點出 MCP 掛超過 30–40 個工具就會劣化，解法是三層 meta-tool（search → get schema → execute），講者宣稱藉此撐到 1,300+ 工具、600+ playbook。任務結束讓 agent 自己提 PR 更新過期的 playbook。

**8. 大家的記憶系統都不是 RAG**（Shlok Khemani）
survey 結論：主流產品收斂到「背景非同步更新的短 profile + 檢索歷史對話的工具」，不是向量 RAG。講者宣稱 ChatGPT 用約 4,000 token 的長 profile（更新頻率低、serving 成本高），Claude 用約 1,000 token 的短 profile（每 24 小時更新、update 成本高）。記憶系統無法外包，要隨產品自研。當前共同痛點是不會主動偵測資訊衝突、不會主動提問補缺口。

**9. eval 本身要變成會適應的東西**（Vincent）
放棄固定問答集，改成定義終態加評分準則；把線上 traces 回餵讓 agent 自己更新測試集；telemetry 進迴圈做自癒。他反駁「eval 與可觀測性已死」的說法，主張 eval 不該是靜態資料集。

**10. 出事的是 harness 不是模型**（Vinoth Govindarajan, OpenAI）
生產事故多半不是幻覺，是 harness 在狀態所有權、變更排序、生命週期、證據驗證上沒做好。他給的名字是 **silent success**——模型回答極為流暢，底層根本沒寫入，而且無聲失敗。對策是收據鏈取代對話日誌：觸發源、繼承狀態、權限範圍、執行細節、存活證據。「transcript 告訴你 agent 說了什麼，receipt 告訴你系統允許、嘗試、執行了什麼。」

## 對本 repo 的四個直接後果

**① 「容量上去了」和「該塞滿」是兩件事。**
CLAUDE.md 的「<200 行」原則，論據之一是模型跟不了太多指令——那個論據過期了（第 2 支）。但第 1 支同時證明**塞滿仍然有害**，而且害處不是遺忘而是雜訊干擾（77% vs 97%）。所以那條原則該留，但理由要換：不是模型記不住，是多餘的文字會拉低準確率。

**② 這個 repo 的架構被外部獨立驗證了。**
第 8 支說大家都收斂到「小 profile + 檢索工具」而不是向量 RAG。本 repo 的 `profile.md`（always-load、刻意保持小）+ grep 全 repo，正是這個形狀。而且 Claude 那條約 1,000 token 的數字，替 B8「profile 保持小」給了一個外部參照點。

**③ 第 3 支是對這個 repo 的警告，不是背書。**
Sakana 說能裝進 context 的任務加記憶系統只是增加成本。本 repo 的記憶層對「跨 session 失憶」是必要的，但它提醒一件事：**單場 session 內能塞進去的東西，不需要繞路走檔案**。

**④ 第 1、10 支跟 2026-09-20 這場實際踩到的坑同形。**
Vinoth 的 silent success 描述的正是當天撞到的東西：agy 收到 YouTube 網址回一份流暢摘要、exit code 0，實際上從沒吃到影片；`view_file` 探測撞權限閘也是 exit code 0 加一行 stderr。Nick Nisi 的「修 harness 而非手動修 code」是同一件事的處方。由利益無關的第三方（OpenAI 工程師在台上）獨立命名，訊號強度高於自己歸納。

## 跟七月那次的對照

七月 `notes/three-confs-2026-scans/scan_aie.md` 掃到的是 Anthropic 官方講《Don't Build Agents, Build Skills Instead》、漸進式揭示防 context 膨脹、Supabase 實測 MCP+Skills 優於單用一方。那批的隱含主張是「把程序性知識沉成結構」。

這批沒有推翻它，但補上了缺的另一半：**沉成結構之後，結構本身會變成新的負債**。十支裡至少四支在處理「我們去年堆的東西現在拖累我們」——刪 skill、砍多 agent、廢棄靜態 eval 集、拆掉 RAG 檢索層。

一句話：2026 上半年在學怎麼把知識變成結構，下半年在學哪些結構該丟掉。

## 方法與限制

- 逐字稿來源：`yt-dlp --write-auto-subs`，機器轉寫，講者姓名與專有名詞有轉寫錯誤（例：Lauren／Lori）。
- 分析由 agy（Antigravity CLI，gemini-3.7-flash-high）逐支執行，prompt 明令只依逐字稿作答、不得用既有知識補充、講者自報數字必須標註為宣稱。
- 全部 10 份逐字稿讀取前跑過 prompt injection 特徵掃描，無命中。
- **沒有看畫面**。這台機器對 googlevideo 影片串流拿到 403（字幕放行、影片檔擋掉），抽格讀投影片的路線不通，所以投影片上但沒講出口的數字不在本次覆蓋範圍。
- 相關：[三場會議 26 支 talk 深掃](./three-confs-2026-ai-builder-scan.md)、[AIE WF 2026 八支深掃](./three-confs-2026-scans/scan_aie.md)

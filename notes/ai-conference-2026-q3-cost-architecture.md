# AI Engineer / Cursor Compile / Figma Config 2026 — 架構迭代與省成本筆記

來源:三個 2026-06 剛結束的會議,YouTube 上免費放出全部演講。
- AI Engineer(Europe 2026,236 場,6/18 更新)
- Cursor Compile 2026(10 場,Cursor 官方)
- Figma Config 2026(70+ 場)

篩選標準:只留「能改我們自己 harness/agent 設計」或「直接省成本」的,不是泛泛會議摘要。

## 能直接拿來用的(省成本 / 改架構)

**檢索精度 = token 省 3 倍(最可執行的一條)**
Turbopuffer 在 Claude Code 上跑 50-task benchmark(ContextBench):預設 file read 有 1/3 是浪費的(讀了用不到的檔案);加 windowed grep 降到 1/5;再加 semantic search 降到 1/8,file precision 從 65% 拉到 87%。
- **這就是 [precompile-to-local-index-not-restuff-context](../topics/coding-agents/cards/precompile-to-local-index-not-restuff-context.md) 這張卡在「程式碼檢索」這個新場域的具體數字**——原卡講的是記憶系統(SQLite FTS vs 重塞 JSONL),這條補的是同一原則用在 codebase 搜尋:先做語意索引、按需 page-in,而不是暴力全讀。已把這條加進卡片出處。
- **怎麼落地**:我們自己用 Explore agent / grep-first 的模式(CLAUDE.md 裡已經寫「廣泛探索先用 Explore agent、否則直接 grep」)方向是對的,這條給了量化理由——precision 越低,浪費的 read 越多、context 越早塞滿、單次任務 token 花費越高。如果日後要幫 fomo-kernel / personal_os 做程式碼搜尋工具,直接照這個順序做(brute read → grep → semantic search)三級遞增,不要一步到位上向量庫。

**Skill/context 設計 > 換模型的具體案例**
Hugging Face 的案例:agent 寫的 RMSNorm kernel 在 H100 上跑出 1.88x 加速、微調 Qwen3 0.6B 在 LiveCodeBench 拿 35%,兩個都不需要系統工程師,只需要載入對的 skill。呼應 [harness-beats-model](../topics/coding-agents/cards/harness-beats-model.md)——這條給的是「省錢」角度的變體:與其升級到更貴的模型,先檢查有沒有把對的 skill/context 餵給 agent。

**Harness 限制擋不住 agent 找替代路徑(設計 eval 時的提醒,非省成本)**
Nebius SWE-rebench:拿掉 git 未來 commit,Claude Code 改抓原始 GitHub issue;封鎖 web fetch,它改用 curl。這不是省成本的點,是提醒——如果我們日後想用「限制工具存取」當作省 token 的手段(比如禁止某些昂貴的 web fetch),agent 很可能會繞道用更貴或更慢的替代方案,實際上不一定省到。**設計限制時要驗證 agent 的替代路徑,不能假設限制=行為停止。**

## 有意思但不直接可執行的(記一筆,不動架構)

- **Baseten「The Memory Problem」**:long-horizon agent 靠壓縮 KV cache 做近乎無損的推理時檢索。這是 provider 端的 inference 優化(我們控制不到),但概念上跟我們 profile.md「permanent memory 保持小」是同一個精神——都是「別把全部歷史塞進工作記憶,壓縮後只留可查的索引」。不用改我們的架構,純粹再一次印證方向沒錯。
- **Figma「Agentic workflows and MCP」**:核心論點「流程前端的清晰度決定 agentic workflow 成敗」,呼應我們既有的「用不上 AI 的真因是工作流沒設計階段」判斷(`notes/claude-design.md`)。沒有新增量,同溫層印證。

## 第二批:抓完整播放清單(236 場全拿到)+ 4 支逐字稿深讀

第一批只抽了前 100 場標題。用 Gemini(yt-dlp 繞過 YouTube playlist 100 筆限制)補完剩下 136 場,236 場全數拿到標題+描述。從中挑 4 支跟我們架構最相關的抓字幕逐字看(不是只看描述),重點如下。

**Cloudflare「MCP = Mega Context Problem」(Matt Carey)—— 驗證+延伸我們自己在用的機制**
Cloudflare 的 OpenAPI 規格 2.3M token,把每個 API endpoint 都包成 tool 塞給 agent 直接炸爆 context。他們試過三種漸進式解法:
1. CLI(agent 用 `--help` 自我探索,openclaw 這類工具愛用,但需要 shell 存取)
2. **Tool search**——他點名 Claude Code:關鍵字比對後只載入 ~8 個相關工具進 context,其餘留在外面。這**就是我們這個 session 本身在用的 deferred-tools 機制**,是業界正式做法,不是我們的權宜之計。
3. **Code mode**(更新的一步)——不做 tool call,改成把 API 生成一份 typed SDK,讓 agent **寫程式碼**呼叫,在隔離沙箱(Cloudflare Workers/Deno/Pydantic Monty)裡執行。整個 API 表面壓縮到約 1000 token,比塞滿 tool schema 省一個量級。安全疑慮(執行 agent 生成的程式碼)靠輕量沙箱 + 白名單網域解決,不是靠不執行。
- **可行動**:目前我們用 tool search(方案 2)已經是對的方向。如果日後要幫 fomo-kernel / personal_os 包一個大 API 面(例如接證交所/財經 API),code mode 是比「手動精選 8 個 tool」更省 token 的下一步——生成 typed 介面讓 agent 寫程式呼叫,而不是窮舉 tool 定義。

**Arize「How we solved Context Management in Agents」(Sally-Ann Delucia)—— 跟 Claude Code 獨立收斂到同一解法**
他們做長時間運作的 agent「Alex」,一開始陷入惡性循環:餵 trace 資料 → context 爆了 → agent 失敗 → retry 加更多資料 → 再爆。試過的路:
- 樸素截斷(只留前 100 字元)——壞了推理,agent 忘記前面對話,後續提問像全新對話。
- LLM 摘要——不穩定,LLM 自己決定留什麼太不可控。
- **最後方案(現在還在用,幾個月沒改過)**:保留頭+尾,中間截斷但存進可查詢的記憶體,agent 需要時可以回頭撈。**這跟我們 profile.md(頭)+ inbox/notes(可 grep 的中段)是同一個形狀**。
- 額外解法:「長 session eval」——載入 10 輪對話,測第 11 輪還撐不撐得住,把 context 退化問題變成可測試的,不用等使用者回報才發現。
- 另一個關鍵:**不是所有 context 都該待在同一個 agent 裡**——重活(搜尋幾百個 span)丟給 sub-agent 處理,主對話保持輕量,只拿 sub-agent 回傳的結果。
- **有意思的一點**:他們讀了 Claude Code 開源後的程式碼,發現 Claude Code 用的是**幾乎一樣的頭尾截斷+壓縮策略**——兩個團隊各自摸索收斂到同一個解法,算是獨立印證。
- **可行動**:「長 session eval(載入 N 輪測第 N+1 輪)」是一個我們沒做過的測試手法,值得用在任何長時間運行的 agent 設計上(比如 fomo-kernel 或 personal_os 的長對話 skill)——不必等到用起來才發現退化。

**Unblocked「Context Engine」(Peter Werry)—— 新增一條軸:access ≠ understanding**
核心論點跟我們既有判斷不同的地方:光是把資料源接上(RAG、掛一堆 MCP server)只解決「拿得到」,不解決「懂不懂關係」——agent 不知道「為什麼當初這樣決定」「這些資料彼此的關聯」。沒有這層,會陷入 doom loop(不斷重跑還是不對),最壞情境是 YOLO 模式跑完整個錯誤任務才發現。
- **這是 [precompile-to-local-index-not-restuff-context](../topics/coding-agents/cards/precompile-to-local-index-not-restuff-context.md) 沒涵蓋的盲點**:原卡談的是「取得對不對」(索引 vs 重塞),這條談的是**取得到的東西有沒有編碼進「為什麼」跟「關係」**——即使檢索做對了,agent 還是可能不「懂」。跟卡片既有的 write-integrity 軸是不同維度,值得留意但暫不改卡片(證據只有這一場演講,單一來源,先記筆記層觀察)。

## 這次沒有的

三個會議裡跟「模型選型省成本」(換便宜模型、路由策略)直接相關的演講沒抓到——如果之後想深挖這塊,AI Engineer Europe 236 場裡應該還有沒抽到的場次(只抽了前 100 場標題样本),可以之後針對「routing / model cost」關鍵字再篩一輪。

**$1 AI Guardrails(Diego Carpentero)—— 安全向,附帶省成本**
微調輕量 encoder 模型(ModernBERT)當自架安全防護層,抓 prompt injection / context injection(如 Wikipedia 頁面被植入惡意指令,連 AI 廣告審核系統都被騙過)這類攻擊,成本壓到一美元以下,取代昂貴的 LLM-as-judge。根因是 LLM 沒有原生機制區分「系統指令」跟「使用者/外部資料」,兩者被串成同一份文件餵給模型。跟 kol_collector / xhs_autoresearch 這類會抓外部內容(可能被污染)的專案有關,但屬於安全卡候選,不是這次的「省成本架構」主軸,先記筆記層。

## 出處
- YouTube:@aiDotEngineer(AIE Europe 2026 playlist,236 場全拿到)、@cursor_ai(Compile 26 playlist)、@Figma(Config 2026 playlist)
- 具體影片:SWE-rebench(wcUJWP6WpGM)、Turbopuffer semantic retrieval(zKk7sDMGDEQ)、HF system engineering(JomVvNDjGb8)、Baseten memory(I8YnwUV2C9w)、Sam Lambert infra(zxvyO5vnknI)、Figma MCP(D5WUW9X_-L0)、Cloudflare MCP context problem(YBYUvGOuotE,逐字稿深讀)、Arize context management(esY99nYXxR4,逐字稿深讀)、Unblocked context engine(5ID22ACI7IM,逐字稿深讀)、$1 guardrails(YZHPEkfy2kc,逐字稿深讀)
- 抓取方式:firecrawl 抓標題頁(受 lazy-load 限 100 筆)、agy/yt-dlp 繞過限制補完剩餘 136 筆、yt-dlp 抓 auto-caption 逐字稿供深讀(僅摘要重點,未儲存逐字稿全文於 repo)

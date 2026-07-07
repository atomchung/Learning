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

## 這次沒有的

三個會議裡跟「模型選型省成本」(換便宜模型、路由策略)直接相關的演講沒抓到——如果之後想深挖這塊,AI Engineer Europe 236 場裡應該還有沒抽到的場次(只抽了前 100 場標題样本),可以之後針對「routing / model cost」關鍵字再篩一輪。

## 出處
- YouTube:@aiDotEngineer(AIE Europe 2026 playlist)、@cursor_ai(Compile 26 playlist)、@Figma(Config 2026 playlist)
- 具體影片:SWE-rebench(wcUJWP6WpGM)、Turbopuffer semantic retrieval(zKk7sDMGDEQ)、HF system engineering(JomVvNDjGb8)、Baseten memory(I8YnwUV2C9w)、Sam Lambert infra(zxvyO5vnknI)、Figma MCP(D5WUW9X_-L0)

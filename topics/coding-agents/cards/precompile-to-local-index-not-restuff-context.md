---
type: card
title: 知識系統的勝負手是預編譯成本地索引、按需 page-in,不是重塞 context
aliases: [wiki 是硬碟 context 是 RAM, 本地 index 別重餵 context, 預編譯複利]
tags: [knowledge-systems, memory-architecture, agents, retrieval]
appears-on:
  - coding-agents
  - knowledge-systems
created: 2026-06-21
freshness: 2026-06  # 具體工具(SQLite FTS/JSONL)會變;可遷移的是「預編譯+按需載入」這個架構選擇
---

# 知識系統的勝負手是預編譯成本地索引、按需 page-in,不是重塞 context

**一句話**:記憶/知識系統的成敗不在「存了多少」,在 recall 時是把全部原始紀錄重新塞回 context(慢、貴、稀釋),還是先把知識**預編譯成本地可查的索引**、決策當下只 page-in 需要的那幾頁。前者把 context 當倉庫,後者把 context 當 RAM、wiki 當硬碟。

## 為什麼重要
- 2026-06 一週內這個母題繞了 5 次,跨完全不同主題才看出是同一條:
  1. **Hermes vs OpenClaw**:本地 SQLite FTS(~113ms)vs 每次餵整份 JSONL 回 context(~19s)——記憶勝負手。
  2. **Hermes 自動蒸餾**=我們睡前做的事(判斷→markdown→索引→grep)。
  3. **部門大腦**:wiki=硬碟、context=RAM,永遠別整庫塞,按需 page-in。
  4. **攝取流程**:瓶頸在「壓縮成判斷 + 決策時調出」,不在取得。
  5. **B8 profile 瘦身**:profile 是索引不是內文,舊脈絡下沉 grep 回憶。
- 核心權衡:context 是有限、昂貴、會被雜訊稀釋的工作記憶。把「檢索」前移到寫入時(預編譯),recall 就從「重讀全部」變成「查索引」,延遲與成本掉一個量級,且不污染當前推理。
- 這就是這個 repo(Karpathy LLM-wiki 實例)能複利的機制本身:寫入時花成本編譯,讀取時零邊際成本。

## 反例與質疑
- 不是所有場景都該預編譯:一次性、不重用的內容,編譯成本收不回,直接塞 context 更划算。
- 預編譯有「蒸餾損失」風險:壓成判斷時可能丟掉日後才有用的脈絡——所以要留 raw 層(inbox)可 grep 回去。
- 個人尺度成立 ≠ 團隊尺度成立:團隊瓶頸是寫入協作+維護,不是檢索(別把這條誤用成「上 RAG」)。

## 邊界與 2026-Q2 更新(這條的勝負手有適用區間)
證據在 Q2 變細了——本卡**在「塞不下」時成立且有學術背書,在「塞得下」時不成立**:

- **印證端(唯一同行評審+可複現)**:BEAM/LIGHT 論文(ICLR 2026)——對話 ≥1M token 時純長 context 會崩(Qwen 2.5 從 128K 的 0.280 掉到 10M 的 0.133,降 53%,「lost in the middle」百萬級仍在),加結構化記憶後贏過 vanilla 與 RAG。這是引用本卡時最該掛的硬證據(GitHub 有 code: BEAM)。三家官方也用腳投票:Anthropic 檔案式記憶 + context editing、OpenAI Dreaming 離線合成、Letta git-based + sleep-time——全是「預編譯/離線合成 + 按需 page-in」(但均為自家評測)。
- **挑戰端(別忽略)**:LoCoMo 短對話(~9K token)上 **full-context(~73%)反而贏 mem0 結構化記憶(~68%)**——**context 還塞得下時,重塞更準更省事,別過度工程化記憶層**。
- **新的軸(本卡沒涵蓋的盲點)**:在 500K–2M token(多數 production agent 實際區間)真正的痛點是 **write-integrity(寫入時狀態被污染)**,不是檢索。本卡的「索引勝負手」解的是「**取得**對不對」,沒涵蓋「**寫進去**有沒有被污染」。
- **一句話修正**:勝負手＝「對話/上下文長到塞不下」時才決定性;塞得下時別上記憶層;且「取得對」之外還有「寫入完整」這條獨立的軸要顧。

## 2026-07 邊界再修正:「塞得下」不等於「用得到」(rot 區間)

上面那句「塞得下時別上記憶層」預設了**塞得下＝用得到**。2026-06 一篇 context rot 診斷(GAIR/上交,四個旗艦開源模型 × 三個 deep-search benchmark)把這個預設打掉:長 horizon 搜尋任務裡**塞得下但已經在 rot**,而症狀不是「檢索不到」——是**模型直接放棄,或提前吐一個自己都不確定的答案**,context 越長越嚴重。

這是**行為層**退化不是**檢索層**退化,所以 needle-in-a-haystack 那類測試**在定義上就測不到它**;你從輸出品質也不太看得出來,只會覺得「今天 agent 有點懶」。他們用 pruning 實驗(砍掉累積 context 再跑)建立累積量與退化的因果連結,並比較 7 種 context management 方法(同時報 performance / 成本 / 對 rot 的影響三軸)。

- **邊界改寫**:不是「塞不下才上記憶層」,而是「**塞不下,或累積量已進 rot 區間**」——後者的閾值**明顯低於 context window 上限**。
- **順帶回答「context 壓縮＝選擇性遺忘?」**:另一篇(VISTA)主張稱職的 context 管理能力**已經潛伏在模型裡**,缺的不是壓縮 policy 而是**讓模型看見自己狀態的介面**——把每個 memory block 的 token 成本、recency、存取歷史、剩餘預算當儀表板持續攤給模型自己看,訓練全免。三個設計約束:必須 **reversible**(單向刪除或摘要會抹掉之後才用得到的證據)、model-agnostic、且放在模型看得見的那一層。→ 答案是:**不是遺忘,是可逆的降級**;而且**pager 應該是模型自己,不是外部 policy**——這是本卡原本沒有的零件。
- **證據等級**:兩篇皆 arXiv preprint、無獨立複現。rot 那篇(2606.29718)賣診斷不賣自家系統(動機偏誤小)、四模型×三 benchmark,但 abstract 不給具體數字;VISTA(2606.30005)的三個 benchmark 都是第三方的、有 ablation 證明增益來自 dashboard 本身,但單一團隊自報(LOCA-bench 上 Gemini-3-Flash 22.7%→50.7%)。

## 2026-07 新場域印證(程式碼檢索,附省成本數字)
Turbopuffer 在 Claude Code 上跑 50-task benchmark(ContextBench,AI Engineer Europe 2026):預設 file read 有 1/3 浪費;加 windowed grep 降到 1/5;加 semantic search 降到 1/8,file precision 65%→87%。這是本卡原則(預編譯索引、按需 page-in)在「codebase 搜尋」而非「對話記憶」場域的具體數字版——**精度直接換算成 token 成本**:每次少讀一個用不到的檔案就是少花一次 context 空間。細節見 `notes/ai-conference-2026-q3-cost-architecture.md`。

## 2026-07 獨立收斂印證(Arize vs Claude Code,兩團隊各自摸索出同一解法)
Arize 做長時間運行 agent(Alex)時,樸素截斷、LLM 摘要都失敗,最後收斂到「保留頭+尾、中間截斷但存進可查詢記憶體,agent 需要時回頭撈」——讀了 Claude Code 開源程式碼後發現對方用的是幾乎一樣的策略。兩個完全獨立的團隊收斂到同一形狀,是比單一案例更強的證據:這不是某家的偏好,是這個問題空間的收斂解。附帶技巧:「長 session eval」(載入 N 輪、測第 N+1 輪撐不撐得住)把 context 退化變成可預先測試的,不必等使用者回報。細節見 `notes/ai-conference-2026-q3-cost-architecture.md`。

## 2026-07 官方原始出處印證(比獨立收斂更硬——是同一句話)
Anthropic 自家 engineering blog《Effective context engineering for AI agents》把這個原則明講成 **just-in-time retrieval / progressive disclosure**:只存輕量識別碼,真正需要時才載入細節。不是「另一個團隊獨立收斂到類似解法」,是**設計 Claude Code 的團隊自己講出跟這張卡幾乎同一句話的原則**——目前查到最強的一份背書。觸發:研究 Claude Certified Architect 認證考綱 Domain 5(Context Management & Reliability)時撈到,細節見 `notes/claude-certification.md`。

## 連結
- ← 支持 [harness-beats-model](./harness-beats-model.md)(記憶架構屬 harness,不換模型就能拉開差距)
- → 引出 [eval-bottleneck-is-criteria-not-tooling](./eval-bottleneck-is-criteria-not-tooling.md)(同精神:瓶頸在前置的設計,不在當下的工具)

## 出處
- notes/openclaw-hermes-personal-agent-frameworks.md(記憶勝負手對比)
- notes/rag-vs-llm-wiki.md(預編譯複利、個人 vs 團隊)
- notes/department-brain-process.md(wiki=硬碟/context=RAM)
- notes/info-intake-routine.md(攝取流程瓶頸在壓縮+調出)
- 觸發:2026-06-21 第一次 weekly-synthesis 抽出五處同母題
- 2026-Q2 更新來源:BEAM/LIGHT(ICLR 2026,arXiv:2510.27246,GitHub github.com/mohammadtavakoli78/BEAM)｜Zep 反駁 mem0(getzep.com「Lies, Damn Lies & Statistics」)揭 LoCoMo full-context 贏 mem0｜「Agent memory breaks before retrieval」(markmhendrickson.com,2026-04-08,write-integrity 軸)｜memweave 檔名即時間衰減(towardsdatascience,2026-04-16)｜2026-06-28 Q2 情報掃描(詳見 inbox 同日)

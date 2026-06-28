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

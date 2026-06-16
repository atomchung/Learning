---
freshness: 2026-06
note: 末段「語意 merge 閘門可不可投資」含具體公司/生態位判斷,會過期;前面的架構判斷(git vs CRDT、語意衝突偵測器)是可遷移元判斷,不會過期。
---

# Agent 協作 infra：多 agent 怎麼共享文件編輯

> 起點：使用者問「agent 協作下怎麼共享文件編輯？office doc → google doc 的對應轉型是啥？」
> 主線：**人類的「檔案→即時共享活狀態」軌跡，agent 不一定重演。agent 協作的原子單位是 PR/diff，不是共享游標——比較像 git，不是 google doc。**
> 接 [rag-vs-llm-wiki](./rag-vs-llm-wiki.md) 的「團隊共享瓶頸是寫入協作+維護不是檢索」——這篇鑽其中「並發寫入」這個難點的 agent 版。

## 人類那次轉型的本質（Office → Google Docs）

別被「即時協作」表象帶走。真正變的是兩件事：

1. **檔案 → 共享活狀態**：從「email 來 email 去、各自持有 .doc」變成「server 上一份大家連進去的 live state」。`版本_final_v2_FINAL.doc` 消失。
2. **鎖定 → 無衝突合併**：底層從「check-out 鎖定」換成 OT（Operational Transformation，早期 Google Docs/Etherpad）後來 CRDT，讓多人同時打字不打架。

為什麼人類需要這個？因為人**慢**、要看到彼此游標（presence）、痛恨 merge conflict。這三個約束催生即時協作。

## 關鍵判斷：agent 很可能「跳過」即時協作這一階段

把人類的約束逐條對到 agent，全都不成立：

- 人慢 → agent 是機器速度，一次爆改一大塊，不逐字。
- 人要看游標 → agent 不需要 presence，不用「看到」別人在打字。
- 人恨 merge conflict → agent 不會無聊，非同步等待對它沒成本。

所以「檔案 → 即時共享活狀態」這條人類軌跡，對 agent 不一定重演。agent 真正需要的是：便宜地分叉（fork 文件去試）、語意層 diff/merge、誰改了什麼為什麼的紀錄。

**這三樣加起來不是 Google Docs，是 git。** 分支 + PR + review-merge。今天的 coding agent 已經這樣協作——各開 branch、各提 diff，由 review 層收斂。對 agent，協作的原子單位是 **PR/diff，不是共享游標**；因為 agent 編輯量大又會犯錯，要的是「審查閘門」不是「即時混寫」。

**所以 office→google 的 agent 對應轉型 ≠ google doc，而是「prose/data 版的 git」**：可分叉的版本化狀態 + 語意合併 + provenance + review gate。硬把 office→google 套到 agent，可能是陷阱題。

## git 模型 vs CRDT 模型：agent 該走哪邊

### 模型 0：序列化（最常被忽略、其實最常見）

多 agent 系統最便宜的解法是**根本不並發寫**——所有寫入排隊 funnel 過一個 orchestrator（actor model / message passing）。production 多 agent 系統大多這樣繞過問題。記住：**並發寫入的最省解，是把它變成不並發。**

### CRDT 的致命細節

CRDT 保證「大家最後收斂到同一狀態」，但**不保證那狀態是對的**。人類沒差（讀一讀就修），agent 改語意時「收斂但錯誤」是最危險的失效模式——兩 agent 各改一段、字元層乾淨合併、語意上互相矛盾，CRDT 靜靜產出一份外觀自洽的垃圾，沒人喊停。

### git 的「缺點」對 agent 反而是特性

git 三方合併會**停下來喊 conflict**，逼出一個解決步驟（可塞 LLM-as-merger 或人）。對會犯錯的 agent，「停下來要人裁決」比「無聲合併」安全。

### 判準（什麼任務走哪邊）

**走 CRDT / live** — 編輯是：空間上不相交、低風險/好回滾、或需人機即時互動（Cursor、共筆那種 human+agent 並坐）。

**走 git / PR** — 編輯是：語意重疊、高風險/不可逆、需審查或稽核、或長命的分叉探索。

一句話壓縮：**重疊 + 風險 + 要審 → git；不相交 + 低風險 + 要即時 → CRDT；能不並發 → 先序列化。**

### 真實會是分層 hybrid

不是二選一。現實堆疊：**live CRDT 當「草稿/scratch」層**（人和 agent 快速共寫）+ **git-式 commit+review 當「升正」閘門**（草稿變 canonical 才過審）。對到兩個熟的東西：這個 repo 的 `notes/`（草稿）→ `main`（過審）；coding agent 的 working tree（live 改）→ PR（合併）。

### 兩個模型都缺、真正的前沿層

git 抓**文字**衝突、CRDT 保**字元**收斂——但 agent 的衝突是**意圖衝突**：兩份 diff 各自乾淨、合起來語意矛盾，兩個模型都抓不到。真正新的 infra 是一層**語意衝突偵測器**（LLM 審「這兩個乾淨合併的 diff 是不是其實互相打臉」）。誰先做好這層，誰握住 agent 協作的關鍵閘門。

## 若真要 live 多 agent 共編，四個維度的轉型

1. **字元級 CRDT → 語意級合併**：CRDT 保證字元不打架，但兩 agent 改同段的意思、按序合起來是語意垃圾。硬問題是「意圖層 merge」，很可能要 **LLM 當 merge driver** 調和兩個都合理的編輯。
2. **presence → provenance**：不需要看 agent 打字，需要「哪個 agent 改哪段、根據什麼」的可稽核軌跡。對 agent，**出處取代在場**（咬合 trust accumulation）。
3. **suggesting mode 變預設**：Google Docs 的「建議模式」對 agent 是常態——每個編輯先當 proposal，過 policy/人/上級 agent 才落地。
4. **WYSIWYG → 結構化語意格式**：人類時代 Word/Docs 都往視覺走；agent 時代要把文件反過來暴露結構（markdown / AST / 結構化 block）。格式戰倒轉。

## Agent 協作 infra 的分層（plumbing 全景）

- **共享狀態層**：git（非同步、可審）或 CRDT（live，Yjs/Automerge）。
- **協調協定**：agent 怎麼宣告意圖、認領區段、不互踩。鎖回來了，但是樂觀鎖 + 語意區段級，或由 orchestrator 派工。
- **合併層**：語意 merge（很可能 LLM-as-merger）+ 語意衝突偵測器。
- **出處/信任層**：每筆編輯簽名歸屬 + 附理由 + audit log。
- **審查/閘門層**：哪些自動套、哪些要 eval/人/監督 agent 批准。
- **跨 agent 標準**：MCP（接 inbox 的「MCP-as-a-rail」）管資源/工具存取；A2A（Google Agent2Agent）管 agent 對 agent 通訊。

## 最後拉高一階

也許 agent 的「google doc 時刻」根本不是更好的文件編輯器，而是**共享的 task/spec/state store**——agent 協作的單位是任務/意圖，prose 文件只是其中一個投影（render 出來的輸出）。而**這個 repo 本身就是這答案的小型實例**：git 當共享狀態、CLAUDE.md 當協定/schema、commit 當 provenance。等於在蓋這套東西的單人版。

## 「語意 merge 閘門」會不會變成可投資的生態位（2026-06 判斷，會過期）

**判決：當獨立公司大概率是 feature 不是 company**，會被「擁有 merge 發生地點的平台」吸收（程式碼→GitHub/Microsoft;agent→orchestrator/模型廠）。但它是真實的價值層,可投資的表達式在外圍三項,不在能力本身。跟既有的 eval / 資安兩條判斷是**同一個天花板**。

### 三框架套上去

1. **收費站框架 → 表面成立**:並發寫變普及後每次都得過 merge 閘,結構像 CI/CD gate、code review。bull case。
2. **生態位被吞框架 → 致命**:語意 merge 閘核心動作 =「LLM 判斷兩 diff 是否語意打架」= 一次 LLM call,能力住模型裡。跟 eval(LLM-as-judge)、紅隊同命,聰明部分被 commoditize、外殼被平台收編。eval 還有「中立性(裁判≠選手)」護城河,merge 閘偏營運水管、跨廠中立訴求弱,護城河更淺。
3. **價值流向框架 → 重點在整合/合規/資料**:能賣錢的不是「聰明的語意 diff 模型」(薄 wrapper 被輾),是擁有 merge 地點 + policy/audit 層 + 過往 merge 決策資料。同你 eval/資安都收斂的「edge 在驗證/整合/合規」。

### 程式碼 vs 散文分開看

- **程式碼**:閘門已有強勢的家——CI + code review + GitHub。**AI code review 新創就是 merge 閘早期形態**(Graphite/CodeRabbit/Greptile/Copilot review),niche 存在但已在被填、GitHub 一個更新就收編。
- **散文/資料**:沒主宰級 incumbent、較空白,但需求模糊、變現不清、TAM 小。空白常因市場小,不是沒人想到。

### 反轉:TAM 可能很薄 → 往上 reframe

並發寫最省解是「不要並發寫」(orchestrator 序列化)。若 production 多 agent 大多序列化,純 merge 閘只在少數真並發場景需要,TAM 薄。正確 reframe 往上一階:真正品類是**「agent 動作准入/治理層」**(輸出該不該落地——品質/安全/政策/合規),merge 衝突只是觸發情形之一。這層才可融資(LangSmith/Braintrust/Arize + guardrail + 身份資安),merge 閘是它的 feature。

### 真要投,投三個表達式

1. **擁有 merge 地點的 incumbent**(MSFT/GitHub):投平台不投 feature,它免費發出 merge 閘那天純玩家就死。
2. **合規/稽核 pure-play**(唯一能撐成公司的角度):受監管產業多 agent 寫共享狀態,需「這次 merge 為何被允許落地」可稽核軌跡,有定價權+中立性,同資安「edge 在合規」pattern。
3. **資料/信任護城河**:誰累積「merge 決策+後續結果」歷史,誰練出更好的閘 + trust-routing(該信任哪個 agent 在哪編輯),會複利,接 trust accumulation。

### 領先指標

- GitHub/orchestrator(LangGraph/Claude managed agents/OpenAI Agents SDK)有沒有把「語意衝突偵測/多 agent reconcile」做成內建節點 → 做了=關門。
- 有沒有「多 agent 准入/治理」pure-play 拿到合規型客戶(非開發者工具型) → 開門。
- 計價:出現 per-merge / per-agent-action 用量計價且綁 policy+audit(非純 token 加成) → 有人找到 LLM call 外的定價權。

**一句話**:真價值層,但跟 eval/資安同宿命——核心能力住模型裡會被吞,活下來的版本是「合規稽核 + 資料信任護城河」,且要 reframe 成 agent 治理層才看得到公司規模。

## 跟既有判斷的咬合

- 接 [rag-vs-llm-wiki](./rag-vs-llm-wiki.md)：那篇說「團隊共享瓶頸是寫入協作不是檢索」，這篇給寫入協作的具體 infra 解法。
- 接 inbox 的 MCP-as-a-rail：MCP/A2A 是這套 plumbing 的標準層。
- 接 personal-os / agent-os 線：多 agent 協作 infra 是 agent OS 的核心子系統。

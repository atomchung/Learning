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

## 跟既有判斷的咬合

- 接 [rag-vs-llm-wiki](./rag-vs-llm-wiki.md)：那篇說「團隊共享瓶頸是寫入協作不是檢索」，這篇給寫入協作的具體 infra 解法。
- 接 inbox 的 MCP-as-a-rail：MCP/A2A 是這套 plumbing 的標準層。
- 接 personal-os / agent-os 線：多 agent 協作 infra 是 agent OS 的核心子系統。

# 業界 Best Practice 掃描 2026-07：這個 repo 還能借什麼

> 2026-07-03。任務：理解 repo 現狀 → 掃業界新 pattern → 挑「還沒借過、且對準開放線」的建議。
> 後續：這類掃描已提案固化成持續迴圈（接 info_collector 進料），見 [Issue #9](https://github.com/atomchung/Learning/issues/9)。
> 上一輪全面掃描是 `agent-context-best-practices.md`（2026-05）＋ `meta/borrowable-patterns.md` B1–B10（2026-06-20）。這篇只記 **delta**，已借過的不重複。

## 先盤點：我們已經有的（掃描前的基準線）

- Context engineering 三策略（compaction / tool clearing / memory）→ `agent-context-best-practices.md`
- 三層記憶（durable profile / relevant-load cards / cold grep）＝ B8 已落地
- 事件觸發蒸餾（B1）、連坑一起記（B2）、≥3 次重複升級（B3）已落地
- 已知待辦：Issue #6 首次 `/meta-review` 未跑、Issue #7 熱檔並發衝突未解、CLAUDE.md 290 行要壓回 <200

**掃描前預測（校準）**：我猜大部分會撞已借鑒的 B1–B10，delta 有限。結果：架構層確實沒新東西（再次驗證「我們本來就是這物種」），但**機制層有三個直接命中開放線的缺口**——lint、lock、validation-gate。低估了。

## 新發現（按對準開放線的程度排序）

### 1. 規則自改要 validation-gated，不要 unconditional（→ Issue #6 首次 meta-review 的設計輸入）

- **來源**：SkillOpt（Microsoft，arXiv 2605.23904）＋呼應已進 inbox 的 Self-Harness / APEX（2026-06-28 Q2 掃描）。
- **核心**：self-improvement 的最佳實踐是「propose-and-test」而非「無條件自我編輯」——聽起來合理的文字診斷，實際套用可能傷害系統。SkillOpt 的增量：**被否決的提案也要存**（failure buffer），避免下輪重提同一個失敗修改。
- **對我們**：三篇獨立來源同口徑（SkillOpt / Self-Harness / APEX）＝訊號夠強。首次 `/meta-review` 的設計現在有完整拼圖：
  1. 改規則前先定「可觀察的驗證訊號」（R1 用戶點頭之外，加一條「這修改怎麼算成功」）
  2. 被否決的提案 append 進 ledger（不重提）
  3. 從成功 session 也蒸餾（APEX），不只從 defects
- **狀態**：這不是新增規則，是首次 meta-review 該長什麼樣的輸入。已備齊，可以跑了。

### 2. 機械 lint：健康檢查別靠人肉標（→ rot 缺陷類 + 「130 張卡難檢索」疑問）

- **來源**：claude-obsidian（同物種 repo，自稱 Karpathy LLM wiki pattern 實作）的 `lint the wiki`——8 類健檢：孤兒頁、死連結、矛盾宣稱、過期宣稱、覆蓋缺口等。
- **我們的 gap**：`defects.md` 靠人肉標（rot 要等給錯答案才發現）；freshness 過期卡、死掉的相對連結、沒人引用的孤兒卡，其實**全部可以機械掃**。
- **借鑒動作**：給 `/weekly-synthesis` 加一段機械 lint（grep freshness 過期、驗相對連結存在、數零引用卡）。零 inference 成本，純腳本。
- **為什麼現在**：卡片 ~27 張還小，但候選池早就問過「130 張會不會反難檢索」——lint 是那條疑問的低成本保險。

### 3. 熱檔並發寫：業界已有標準解（→ Issue #7 外部驗證）

- **來源**：claude-obsidian v1.7 的 multi-writer safety——平行 agent 寫同頁時用 advisory file lock，過期鎖 60 秒自清。
- **意義**：我們兩次撞到的「inbox/profile 並發寫衝突」**是業界公認問題、有已知解法**，不是我們用法怪。
- **借鑒動作**：git-based repo 不需要 lock 那麼重，既有候選解就對——inbox 拆每日檔（append-only 天生免衝突）+ profile 寫前 fetch。外部案例讓這條從「猜的」變「有先例背書」，首次 meta-review 可以直接裁決。

### 4. 指令預算：CLAUDE.md 壓行數從美學變機械必要（→ R2/R3 待辦）

- **來源**：HumanLayer《Writing a good CLAUDE.md》＋ morphllm AGENTS.md spec（2026）。
- **新的量化框架**：frontier 模型可靠遵循 **~150–200 條指令**，harness 系統提示已吃掉 ~50 條；超過 200 行後**整塊被忽略**（不是均勻稀釋）。
- **對我們**：CLAUDE.md 現在 290 行。手機 Obsidian 設定教學、目錄樹全文這類「人看的內容」可搬出去（progressive disclosure：主檔只留指令，細節放被引用的檔）。這條本來就在待辦，現在有了「為什麼非壓不可」的機制解釋：**不壓＝隨機丟棄規則，且丟哪塊不由我們選**。

### 5. Memory benchmark 生態成形（→ 內容層：記憶卡的邊界可被實測檢驗）

- **來源**：Mem0《State of AI Agent Memory 2026》、rohitg00/agentmemory（自稱 based on real-world benchmarks）。
- **意義**：agent memory 2026 已是一級架構元件——有 benchmark 套件、可量測的方案差距。我們的卡「塞得下就別上記憶層」（BEAM/LIGHT 背書）現在可以拿公開 benchmark 對答案。
- **一個值得警惕的數據點**：claude-obsidian v1.7 加 hybrid retrieval（BM25+rerank）自報 **+32 個百分點**檢索準確率 vs 純結構導航——暗示純 grep 有規模天花板。**先別動**（廠商自報 + 我們量級還小），但這是「130 張卡」疑問到期時該回看的證據。過濾規則不變：能抄控制邏輯，不抄儲存技術。

### 6. 觀察清單（記下不行動）

- **OpenViking（ByteDance）**：self-evolving filesystem-based context DB——同物種的工業版，哪天要看「檔案型記憶做到極致長怎樣」去讀這個。
- **awesome-harness-engineering / awesome-agent-harness（RUCAIBox）**：harness engineering 已有 awesome list ＋綜述論文＝學科化坐實（harness>model 線的又一佐證，判讀型不是借鑒型）。
- **agentic-stack 可攜 `.agent/` 資料夾**：跨 harness 配置翻譯層。B7（可攜性）同款，個人 repo ROI 薄，維持觀察。

## 建議繼續鑽研（排序）

1. **跑首次 `/meta-review`**（不用再研究了）——設計輸入已齊：R1 防自評閘 + validation-gate + rejected buffer + 從成功也蒸餾 + Issue #7 裁決材料。defects.md 已有 5 筆（2 筆 @user）。這是 profile 裡「最活躍元線」的下一步，也是 2026-06-20 就定好的起點。
2. **機械 lint 進 weekly-synthesis**——零成本、對準 rot。可以當 meta-review 的第一個「propose-and-test」案例：提案 → 用戶點頭 → 跑一次看抓不抓得到東西。
3. **內容層新題：memory benchmark 對答案**——拿 Mem0 報告 + BEAM/LIGHT 檢驗「塞得下就別上記憶層」那張卡的邊界數字，順便看 file-based 在哪個量級開始輸。判讀型輸入，餵記憶卡不改 harness。
4. **CLAUDE.md 壓行數**——排在 meta-review 之後做（review 本來就要砍規則，一起動手才不會壓兩次）。

## 坑/校準

- 預測「大部分撞已知」半對半錯：**架構層對（零新東西），機制層錯（lint/lock/validation-gate 三個缺口全命中開放線）**。教訓：掃 best practice 時別只對「架構像不像」，要對「開放 issue 有沒有現成解」。
- arXiv / Mem0 的 WebFetch 被 403，SkillOpt 細節靠搜尋摘要 + awesome list 交叉，**沒讀到原文**——首次 meta-review 引用它前值得再試讀一次原文。

## 來源

- [SkillOpt（arXiv 2605.23904）](https://arxiv.org/abs/2605.23904)（未讀原文，經搜尋摘要＋ awesome list 交叉）
- [awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering)、[awesome-agent-harness（RUCAIBox）](https://github.com/RUCAIBox/awesome-agent-harness)
- [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)
- [Writing a good CLAUDE.md | HumanLayer](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [AGENTS.md Spec 2026 | morphllm](https://www.morphllm.com/agents-md-guide)
- [State of AI Agent Memory 2026 | Mem0](https://mem0.ai/blog/state-of-ai-agent-memory-2026)（403，僅搜尋摘要）
- [agentmemory](https://github.com/rohitg00/agentmemory)

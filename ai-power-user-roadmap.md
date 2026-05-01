# 非工程師 AI Power User 升級路線圖

> 一個 RevOps Senior Manager 對齊 Anthropic 級實踐者的 3 個月 master plan
>
> 2026 年 5 月｜寫給：已經有基礎、想衝頂尖的非工程師 AI 使用者

## 為什麼寫這份

市面上「AI for non-coders」的內容多半停在「用 ChatGPT 寫郵件」。但**進階非工程師**（已會用 Claude Code、有自訂 skill、跑 personal automation）找不到對標——「我已經比 90% 的人強，但離 Anthropic 內部員工還差什麼？」這份就是答案。

本文以一位 Senior Manager, Pricing Operations（Coupang，ex-ByteDance TikTok LIVE RevOps）的真實設定為樣本，做完整 gap 分析，提出可執行 roadmap。

## 研究來源

整合三條資訊源：

1. **Anthropic 內部實踐者**：Boris Cherny（Claude Code 創造者）、Cat Wu（Claude Code PM）、Mike Krieger（CPO）的 podcast 和 blog
   - Anthropic 官方 [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
   - [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code)
   - [Boris on Lenny's Newsletter](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens)
   - [Boris on Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny)
   - [How Boris Uses Claude Code](https://howborisusesclaudecode.com/)
2. **非工程師 AI power user 模範**：Simon Willison、Dan Shipper（Every）、Lenny Rachitsky 的 PM AI 系列、Geoffrey Litt 的 Malleable Software
3. **Eval / 迭代速度權威**：Hamel Husain、Eugene Yan、Shreya Shankar 的 eval 論文

並由 Codex（GPT-5）對整份分析做第三方 review，修正了 SWE-shaped 過度工程化的傾向。

## 核心 insight：3 個關鍵發現

1. **頂尖實踐者的差距是 mental model，不是技巧**
   - Boris 不是因為他寫 prompt 比較好，是因為他**同時跑 5 個 terminal + 5 個 browser session**
   - 「Manager of agents」不是技巧，是身份認同
2. **非工程師最常犯的錯：AI 投資對錯地方**
   - 多數人把 AI 用在「興趣 / 內容 / 個人專案」（容易、回饋快）
   - 真正能改變職涯的是用在「day job 重複決策 / 跨部門 deliverable」（難、回饋慢）
3. **Eval 對非工程師而言應該是輕量的**
   - SWE 視角會推「golden set + regression test + LLM judge」
   - 非工程師的 ROI 更高在 **example library + checklist**
   - Hamel doctrine 的核心其實是「先**手讀** 50 個 trace」，不是建系統

## 八大模塊評分框架

把「AI Power User」能力拆成 8 個獨立模塊，分別評分：

| 模塊 | 樣本人現況 | Anthropic 級 | 缺口 | 優先 |
|---|---|---|---|---|
| A. 驗收紀律（Verification） | 3/10 | 9/10 | 🔴 大 | P0 |
| B. 上下文與記憶架構 | 8/10 | 9/10 | 🟢 小 | 維持 |
| C. 多 Agent 編排 | 3/10 | 9/10 | 🔴 大 | P1 |
| D. 規格與規劃（Spec） | 4/10 | 9/10 | 🟡 中 | P1 |
| E. Eval 與量測 | 2/10 | 8/10 | 🟡 中 | P3 |
| F. 自動化護欄（Hooks） | 4/10 | 8/10 | 🟢 小 | P3 |
| G. **本職領域應用** | **2/10** | **9/10** | 🔴🔴 **最大** | **P0** |
| H. 內容與知識產出 | 8/10 | 8/10 | 🟢 無 | 維持 |

---

## 模塊 A：驗收紀律 — P0

> Boris 親述：「Verify-or-don't-ship 是單一最高槓桿動作，可 2-3x 最終品質」

### 高手怎麼用

任務開頭強制貼 3 樣：
1. Good output 範例
2. Bad output 範例
3. 驗收 checklist

### 核心 Pattern

```
[任務描述]
GOOD output looks like: [...]
BAD output looks like: [...]
Acceptance checklist:
  [ ] 包含 X
  [ ] 不超過 N 字
  [ ] JSON valid
  [ ] 引用 3 個資料來源
```

### 具象例子

| 場景 | 沒驗收 | 套上驗收後 |
|---|---|---|
| 寫提案給老闆 | 描述需求 → AI 寫 → 改 5 輪 | 貼上次老闆讚過的版本 + checklist → 一次到位 |
| 跑 SQL | 描述要查什麼 → 跑 → 結果怪 → 重來 | 貼期望欄位 + 樣本 row → 直接對 |
| 寫貼文標題 | 「想 5 個」 | 貼 3 個自己最爆款 + 反例 → 品質跳級 |

### Roadmap（3 小時）

1. 建 `~/templates/`，放 5 個高頻範本（30 min）
2. 建 `/verify` slash command（30 min）
3. 連續 1 週每個任務都先貼範本，養成肌肉記憶（隱性 2h）

---

## 模塊 B：上下文與記憶架構 — 維持

樣本人現況已是頂尖配置：3 層 CLAUDE.md + 個人知識庫 + 20+ skills + MCP filesystem。

唯一可調：CLAUDE.md 瘦身審計。Boris 個人 CLAUDE.md 只有 ~76 token，project 級 ~4k。每條規則做「刪掉會不會出錯」測試。

---

## 模塊 C：多 Agent 編排 — P1

> Boris：5 terminal tabs + 5 browser sessions + iOS sessions，OS notification 當 inbox

### 核心 Pattern：「Manager, not Maker」

```
你的角色：分派任務 + 收斂結果
Claude 的角色：並行做苦工
```

### 具象例子

| 場景 | Solo 模式 | Manager 模式 |
|---|---|---|
| 競品週報 | 一條 thread 30 min | 同時跑（A）價格爬蟲（B）促銷歸納（C）歷史趨勢，10 min 合流 |
| 寫深度文章 | 順序：研究 → 寫 → 配圖 | 並行：研究 + 競品 + 封面 → 收斂 |
| 讀多份財報 | 自己讀 5 份 | 4 個 subagent 各讀一份 → main 跑差異對比 |

### Roadmap（4 週、4h）

1. Week 1：強迫一個任務拆 3 路並行
2. Week 2：建 `/parallel-research` slash command
3. Week 3：對主力產出建 pre-publish reviewer skill（fresh context）
4. Week 4：iOS Claude app 設定，通勤 kick off

### 實現後好處

- 同樣時間產出 2-3x（Boris 實測）
- 升級成「AI Manager」這個職涯角色——這是 2026 知識工作者的 promotion 訊號

---

## 模塊 D：規格與規劃 — P1

### 核心 Pattern：「Spec, not vibes」

```
任務模糊度 < 30 分鐘 → 直接做
任務模糊度 > 30 分鐘 → 強制走 spec 流程
```

### Spec 模式 vs Vibes 模式

| 場景 | Vibes 模式 | Spec 模式 |
|---|---|---|
| 設計新 dashboard | 直接和工程師講需求 | 先讓 AI 反問 10 題 → SPEC.md → 帶去開會 |
| 年度 OKR 自我盤點 | 想到哪寫到哪 | AI interview 30 min → 結構化目標 |
| 跳槽履歷改版 | 改第 5 版還在改 | spec 先定（target 公司 / narrative）→ 一次對 |

### Roadmap（2h）

建 `/spec` 和 `/execute-spec` slash command，強迫 4 個任務跑這流程。

### 實現後好處

- 大任務一次到位率 50% → 85%
- **這個能力 = senior IC → director 的核心軟技能**：把模糊需求結構化

---

## 模塊 E：Eval 與量測 — P3（輕量版）

### Codex review 修正：別過度工程化

對非工程師：
- 不要建 Promptfoo + Braintrust 完整 pipeline
- 該做的是 example library + checklist

### Hamel doctrine（最重要 1 條）

> 先**手讀** 50 個 trace，標 pass/fail + 一句失敗原因。多數人跳過這步直接建 dashboard，量測錯東西。

### 具象例子

| 評估什麼 | 過度工程（NG） | 輕量版（OK） |
|---|---|---|
| 主力 skill 品質 | 蓋完整 eval pipeline | `evals/<skill>/` 放 10 個歷史好/壞範例 + 5 條 checklist |
| 週報是否退步 | 跑 LLM judge 自動評分 | 人工讀 4 週週報，binary「這週比上週好嗎」 |
| 對外 deliverable | 蓋 eval 系統 | 對方 review 評分（A/B/C），自己歸納什麼導致 A |

---

## 模塊 F：自動化護欄 — P3

### Codex 修正：只該維護 2-4 個硬 hook

不要把自己變成 automation maintainer。

該建的：
1. `PreToolUse`：偵測會違反核心紀律的操作（如非工程師用 SDK 計費），直接 block
2. `PostToolUse`：自動 format
3. `Stop` hook：跑完任務自動推 reviewer
4. `SessionStart`：自動載當週 context

設定一次，不再動。

---

## 模塊 G：本職領域應用 — 🔥 P0 最大缺口

> Codex 抓到最致命的 miss：樣本人 20+ skill **0 個是給 day job 的**。80% 工時在本職，AI 投資全押在副業內容創作。**槓桿錯位**。

### 核心 Pattern：「Skill-ify Your Day Job」

```
任何一週做超過 2 次的事 → skill
任何跨部門 deliverable → 有對應 reviewer skill
任何重要決策 → 進 decision log
```

### RevOps / Pricing 該蓋的 8 個 skill

| Skill | 用途 | ROI |
|---|---|---|
| `sql-reviewer` | query 正確性 / join 風險 / 資料外洩偵測 | 每週省 2-3h debug |
| `pricing-change-premortem` | 改價前讓 AI 跑「這會不會壞掉」 | 老闆 trust↑，避免漏損事件 |
| `elasticity-scenario-gen` | 自動跑彈性 / margin 模擬 | 從 Excel 模型解放 |
| `competitor-anomaly-detector` | 競品異常價格 / 促銷偵測 | 比同事早 24h 看到威脅 |
| `weekly-pricing-narrative` | 本週改了什麼 / 為什麼 / 下週盯什麼 | 1:1、QBR、晉升素材庫 |
| `dashboard-qa` | 指標定義 / 分母 / stale data 檢查 | 數據 trust↑ |
| `excel-sql-bridge` | Excel ↔ SQL 雙向轉 | 業務提需求，30 秒生 SQL |
| **`decision-log`** | 假設 → 動作 → 預期 → 實際 | **promotion 故事庫，最重要** |

### Roadmap（8 週、8h）

- W1-2：`sql-reviewer` + `dashboard-qa`（高頻、低風險入門）
- W3-4：`pricing-change-premortem` + `competitor-anomaly-detector`
- W5-6：`weekly-pricing-narrative` + `decision-log`（直接餵晉升 review）
- W7-8：`elasticity-scenario-gen` + `excel-sql-bridge`

### 實現後好處

1. **本職內升**：從「會用 AI 的 senior manager」→「把整個流程 AI 化的人」（director track 故事）
2. **Promotion review**：`decision-log` 每筆都是「我預測 X，實際 Y，學到 Z」的證據——比同儕的「我做了 A、B、C」高一個 level
3. **跳槽履歷**：「Architected 8-skill AI workflow stack for revenue operations」AI 公司面試官秒辨識「dogfooding 級實踐者」
4. **量化結果**：3 個月後有真實 before/after 數字，不是「efficiency by 50%」這種空話

---

## 模塊 H：內容與知識產出 — 維持

樣本人在這塊已到頂。把模塊 A（驗收）和 D（spec）套到內容創作上會再上一階，但**不再加新 skill**——邊際遞減。

---

## 整合 Master Plan：3 個月路線圖

```
┌─────────────────────────────────────────────────────────────┐
│ Week 0（這週末，3h）                                        │
│  → 模塊 A：建 templates/ + /verify command                  │
│  → 模塊 B：CLAUDE.md 瘦身審計                               │
│  → 模塊 H：把過去最強範例放進 templates                     │
├─────────────────────────────────────────────────────────────┤
│ Week 1-2（4h）— 行為 pattern 升級                           │
│  → 模塊 D：建 /spec + /execute-spec                         │
│  → 模塊 C：跑第一次 3 並行 session                          │
├─────────────────────────────────────────────────────────────┤
│ Week 3-10（8h，每週 1h）— 🔥 Day Job Skill 套件             │
│  → 模塊 G：8 個 day-job skill 全套                          │
│    最高 ROI 段，職涯天花板就靠這段                          │
├─────────────────────────────────────────────────────────────┤
│ Week 11-12（3h）— 量測與護欄                                │
│  → 模塊 E：對 top 5 skill 加 example library + checklist    │
│  → 模塊 F：2-4 個硬 hook                                    │
├─────────────────────────────────────────────────────────────┤
│ Ongoing（每週日 30min）                                     │
│  → Skill audit + decision-log review + reviewer 跑          │
└─────────────────────────────────────────────────────────────┘
```

## 3 個月後的對標

| 指標 | 現在 | 3 個月後 |
|---|---|---|
| 對齊 Anthropic 級實踐者 | 60-65% | 85%+ |
| Day job AI 工具 | 0 個 | 8 個生產級 skill |
| 大任務一次到位率 | ~50% | ~85% |
| 並行產出能力 | 1 session | 3 並行 + 移動端後台 |
| 履歷素材 | 「increased efficiency by 50%」 | 「Architected AI workflow stack with measurable X% improvement」 |
| 晉升故事 | 散點戰功 | 系統化方法論 |
| 跳槽競爭力 | 「會用 AI 的 RevOps」 | **「AI-native RevOps operator」（2026 稀缺人設）** |

## 結論：3 個原則

1. **AI 投資要對齊收入來源**：把工具放在 day job，不是副業
2. **Manager mindset > Maker mindset**：你的價值是分派 + 收斂，不是手寫
3. **Examples > Metrics（小規模下）**：先把好/壞範例餵飽 AI，再考慮 eval 系統

對非工程師而言，AI Power User 的終極狀態不是「我會更多技巧」，而是「我把判斷力外化成可執行的 skill 和 checklist，讓我的下游品質有護城河」。這就是 Anthropic 內部員工和外部高手的真正差距。

---

## 參考資料

### Anthropic 官方
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
- [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code)
- [Claude Code Common Workflows](https://docs.anthropic.com/en/docs/claude-code/tutorials)

### Boris Cherny / Cat Wu
- [Boris on Lenny's Newsletter](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens)
- [Building Claude Code (Pragmatic Engineer)](https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny)
- [How Boris Uses Claude Code](https://howborisusesclaudecode.com/)
- [Every podcast: Cat Wu & Boris Cherny](https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it)

### Eval & 迭代速度
- Hamel Husain — *Your AI Product Needs Evals*, *Field Guide to Rapidly Improving AI Products* (hamel.dev)
- Eugene Yan — *Building LLM Applications* (eugeneyan.com)
- Shreya Shankar — *Who Validates the Validators?*

### 非工程師 AI 模範
- Simon Willison — simonwillison.net
- Dan Shipper — Every.to
- Lenny Rachitsky — *How PMs are using AI* 系列
- Geoffrey Litt — *Malleable Software in the Age of LLMs*

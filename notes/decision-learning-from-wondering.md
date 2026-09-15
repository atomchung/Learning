# 從 Wondering 到 Decision Learning：把「學懂」接到「做決策」

> 2026-09-15
>
> 核心方向：不要複製 Wondering 成另一個 AI 課程 App。把它轉成 Learning repo 的一個通用能力：**把研究材料編譯成理解，再把理解映射到決策。**
>
> 投資是第一個高價值 domain adapter，但不應另建一套投資學習系統；產品、技術、職涯等決策都應共用同一個 learning engine。

---

## 1. 這次真正學到的是什麼

Wondering 值得借的不是「AI 生課程」，而是把無結構探索轉成有路徑的理解：

```text
Topic / URL / PDF
  ↓
Roadmap
  ↓
Short learning units
  ↓
Examples / visual / checks
  ↓
Branch when confused
  ↓
Return to main path
```

一般 chat 的問題是：

```text
問問題 → 得答案 → 繼續追問 → rabbit hole → 忘記原始目的
```

Learning repo 可以把它再推一步：

```text
Question
  ↓
Decision / understanding goal
  ↓
Required knowledge graph
  ↓
Evidence-backed learning units
  ↓
Understanding checks
  ↓
Decision model
  ↓
Action / no action
```

**核心轉變：subject-driven learning → goal/decision-driven learning。**

不是「教我 Kubernetes」，而是：「我要決定我們是否需要 Kubernetes；為了做對這個決定，我最少必須理解什麼？」

---

## 2. 與目前 Learning repo 的關係

Learning repo 目前的核心是：

- `notes/`：先捕捉「我學到什麼」
- `topics/*/cards/`：再蒸餾「哪些判斷可以跨脈絡重用」
- journey：保留理解如何形成
- graph：看卡與卡之間的關係

Decision Learning 不應替換這套結構，而是補一條目前較弱的鏈：

```text
素材
  ↓
notes               ← 已有
  ↓
reusable judgments  ← cards，已有
  ↓
causal model         ← 應新增
  ↓
decision            ← 應新增
  ↓
outcome / review    ← 應新增
  ↓
回寫新的 reusable judgments
```

也就是：**目前 Learning repo 很擅長讓知識複利，但還沒有把「理解」明確接到「決策與驗證」。**

---

## 3. 通用 Decision Learning schema

一個 decision-learning session 不先要求模型給結論，而先建立以下結構。

### A. Goal

```yaml
goal_type: understand | compare | decide
question: <原始問題>
decision: <若有，真正要做的決策>
time_budget: <例如 15 min>
known_context: <已知 / 不需重教>
```

### B. Must-understand map

只產三層：

```yaml
must_understand:
  - ...
nice_to_know:
  - ...
skip:
  - ...
```

好學習的第一步不是增加內容，而是刪掉對目標沒有邊際價值的內容。

### C. Learning Unit

每個 node 用固定 schema：

```yaml
claim: <一句話判斷>
why_it_matters: <為何與目標有關>
explanation: <最少充分解釋>
worked_example: <具體例子>
counterexample: <在哪些情況不成立>
common_mistake: <常見誤解>
evidence:
  - source
confidence: confirmed | likely | weak | unknown
check_understanding: <scenario，不只考記憶>
decision_implication: <若有，對原始決策意味什麼>
```

### D. Branchable graph

任何不懂的概念都能 branch：

```text
Original goal
   │
Main path ───── rabbit hole A
   │             └─ evidence
   ├─────────── rabbit hole B
   │
Decision
```

但 UI / agent 永遠保留原始目標，避免研究走失。

### E. Decision synthesis

最後不是「summary」，而是：

```yaml
current_recommendation:
why:
evidence_for:
evidence_against:
unknowns:
falsifiers:
next_cheapest_experiment:
confidence:
```

---

## 4. Learning repo 應新增的核心概念：Claim → Evidence → Implication

原子卡目前的單位是「一句話能說完的判斷」。Decision Learning 可以直接接這個粒度，但每張卡再多一個使用方式：

```text
Claim
  ↓ supported by
Evidence
  ↓ therefore
Implication
  ↓ contributes to
Decision
```

同一張卡可以在不同 decision 上產生不同 implication。

例如：

```text
Claim:
「模型能力趨同後，差異化會往 harness / workflow 移動」

在 coding-agent 決策裡：
→ 不應只用 benchmark 選 agent

在投資決策裡：
→ 模型層的長期租值可能低於 workflow / distribution 層
```

這正好符合 repo 原本「跨脈絡重用」的卡片哲學。

---

# 5. 投資不是另一套系統，而是一個 Domain Adapter

Investment adapter 只需在通用 schema 上增加幾個欄位。

## 5.1 投資問題的最小 causal model

```text
Position / Idea
  ↓
Investment thesis
  ↓
Causal chain
  ↓
Evidence
  ↓
Falsifier
  ↓
Portfolio interaction
  ↓
Decision
  ↓
Observed outcome
```

投資的 learning 目標不是「知道更多公司資料」，而是：

> **理解這筆投資究竟在押哪條因果鏈，以及什麼事實足以讓自己改變判斷。**

---

## 5.2 Thesis Map

例如一個公司 thesis 不再是一篇長文，而是一張承重圖：

```text
Company thesis成立
│
├─ Revenue driver A
│   ├─ prerequisite A1
│   └─ prerequisite A2
│
├─ Margin / economics 成立
│
├─ Competitive moat 沒被破壞
│
└─ Valuation 沒有透支上述改善
```

每個 node 都有：

```yaml
claim:
why_it_matters:
evidence:
status: confirmed | likely | weak | unknown | falsified
falsifier:
decision_weight: high | medium | low
```

重點不是畫漂亮圖，而是知道：**哪幾個 node 真正在承重。**

---

## 5.3 Evidence Delta，而不是每天重寫 thesis

日常研究預設只回答：

> What changed since the last decision state?

```yaml
new_evidence:
belief_affected:
old_state:
new_state:
strength_of_update:
priced_in_assessment:
action_required: yes | no
```

例如：

```text
NEW EVIDENCE
Cloud growth + margin 同時改善

AFFECTED BELIEF
CapEx → profitable Cloud growth

UPDATE
moderate positive

ACTION
No action — thesis strengthened, but portfolio sizing already reflects high conviction
```

這可以避免「好消息 = 加碼」的機械反應。

---

## 5.4 Kill Card / Falsifier 是一級公民

每個重要 thesis 都應該有少量、可觀察的 kill conditions：

```text
Thesis breaks if:
1. ...
2. ...
3. ...
```

新資訊先問：

```text
Does this evidence hit / approach a falsifier?
```

而不是只問：

```text
Is this bullish or bearish?
```

這會把 AI 從 sentiment summarizer 變成 thesis-integrity monitor。

---

## 5.5 Portfolio Map：ticker 不等於獨立 thesis

投資 adapter 要額外建立：

```text
Ticker
  ↓ exposed to
Underlying causal bet
```

例如不同公司可能共同暴露在：

```text
AI CapEx
  ↓
Data-center deployment
  ↓
Compute / memory / networking demand
```

每次新 idea 都問：

```yaml
is_new_thesis: true | false
factor_overlap:
marginal_diversification:
existing_positions_same_bet:
```

目的不是限制集中，而是讓集中是**顯性而非意外**。

---

## 5.6 Decision Simulator：測試自己是否真的理解

一般 quiz 測「你記不記得」。

投資 decision-learning 應測「你能不能在 counterfactual 下維持一致判斷」。

例：

- 如果股價今天沒有跌，你還會想加碼嗎？
- 如果這不是既有持倉，而是今天第一次看到，你會建立新倉嗎？
- 如果 thesis 完全成立但未來 12 個月股價不漲，你還願意持有嗎？
- 哪一個可觀察結果會讓你真正降低 conviction？
- 這次加碼是在增加新 thesis，還是增加同一 factor exposure？

這些問題同時是 learning check 與 bias check。

---

# 6. 一張統一 Decision Card

Learning engine 不論 domain，最後都可以輸出一張 card：

```markdown
# Decision: <問題>

## 1. What am I actually deciding?

## 2. What must be true?

## 3. What changed?

## 4. Strongest evidence for / against

## 5. What is still unknown?

## 6. What would falsify the current view?

## 7. Is this decision independent from existing bets/commitments?

## 8. Best counterargument

## 9. Decision

## 10. Confidence

## 11. Next evidence / cheapest experiment
```

Investment adapter 只是在 #7 裡加入 portfolio overlap，並把 #2 具體化成 thesis causal chain。

---

# 7. 產品層：先做「Compiler」，不是另一個知識庫

Learning repo 已經是 durable knowledge store。新的 local prototype 應只是它上面的 interaction / compiler layer。

```text
Git repo / URL / PDF / notes
       ↓
Goal Interpreter
       ↓
Curriculum / Knowledge Planner
       ↓
Learning Unit Compiler
       ↓
Branchable Graph
       ↓
Understanding Evaluator
       ↓
Decision Synthesizer
       ↓
write useful judgment back to Learning repo
```

因此 prototype 不需要先複製：

- account
- cloud sync
- social
- streak
- marketplace
- podcast
- full spaced repetition

第一版只需要：

- 輸入一個真實問題
- 拆 must-understand graph
- 產生 5–8 個 learning units
- 支援 branch
- 保留 source / evidence / confidence
- scenario-based understanding check
- 最後生成 Decision Card
- 把可重用判斷沉回 `notes/` / `topics/`

---

# 8. Local-first 架構思路

如果真的實作，local app 不應成為新的 source of truth。

```text
Learning repo = durable memory / knowledge asset
Local app     = interaction + compiler + visualization
LLM           = replaceable reasoning provider
```

可行組合：

```text
Frontend: Next.js + React Flow + Mermaid
Backend:  FastAPI + Pydantic
State:    SQLite（session / temporary graph）
Durable:  Markdown in Learning repo
Models:   OpenAI / Claude / Gemini / Ollama adapter
```

原則：

> **local-first 不等於 local-model-first。**

先把資料與 state 留本機，reasoning 可先用 frontier API；之後再視隱私 / 成本切換 local model。

---

# 9. 第一個 acceptance test 應該是投資，但不要只測投資

選一個真實、正在承重的投資決策，例如：

> 「某公司目前的高權重是否仍合理？」

成功標準不是 AI 有沒有給出「買 / 賣」，而是：

1. 10–15 分鐘內能否看懂真正的承重 causal chain？
2. 是否把已知 / 未知 / 推論分開？
3. 是否指出哪個 evidence 真正改變 belief？
4. 是否能提出最強反證與 falsifier？
5. 是否能辨認這是不是現有 factor 的重複暴露？
6. 使用者做完後，能否不用看原文回答一個 counterfactual scenario？
7. 最終 decision 是否可以被未來 evidence 更新，而不是重新寫一篇分析？

再用第二個非投資案例（例如技術選型）驗證 schema 是否真的通用。

如果只有投資 case 好用，代表我們做的是 investment tool；如果兩者都好用，才代表我們真的做出了 Decision Learning engine。

---

# 10. 與 repo 既有主題的連接

- `heptabase-design-research.md`：卡片是原子判斷；Decision Learning 把卡片從「可重用理解」推到「可組合決策」。
- `notes/personal-os-from-trading-journal.md`：交易日誌累積的是 decision sample；這裡補上 decision 之前的 causal model，以及 outcome 之後如何回寫 learning。
- `topics/ai-industry-reading/`：已經在做 signal → judgment；可以直接成為 investment adapter 的 evidence / reusable-claim 來源。
- `coding-agents`：很適合當第二個非投資 acceptance case，例如「某 coding agent / orchestration 架構是否值得採用」。

因此新的閉環是：

```text
Experience / Research
        ↓
      notes
        ↓
 reusable cards
        ↓
 decision graph
        ↓
      action
        ↓
     outcome
        ↓
postmortem / new evidence
        ↓
 update cards
```

這比「建立更多筆記」更接近真正的認知複利。

---

## 當下結論

**不要另開 Investment Learning 系統。**

先在 Learning repo 上建立通用的 Decision Learning 概念：

> **AI that converts research into understanding, and understanding into decisions.**

Investment 是第一個 domain adapter，因為它天然具有：

- 明確 decision
- 可觀察 evidence
- causal thesis
- falsifier
- portfolio constraint
- 最終 outcome

因此最適合驗證整個 learning loop 是否真的能改善決策，而不只是讓內容更好看。

## 下一步

先不要擴平台。下一個開發單位應是 **一個真實 decision 的 end-to-end prototype**：

1. 從 Learning repo + 外部 source 載入背景
2. 產生 must-understand graph
3. 完成 5–8 個 learning units
4. branch 一次 rabbit hole 再返回
5. 跑一個 counterfactual understanding check
6. 產生 Decision Card
7. 把新的 reusable judgment 回寫 `notes/`

成功後，再決定要不要把它升成 `topics/decision-learning/`。

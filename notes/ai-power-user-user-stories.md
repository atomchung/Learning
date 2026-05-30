# AI Power User — 個人電腦 User Stories

> 配套：[ai-power-user-roadmap.md](./ai-power-user-roadmap.md)
>
> **這份只談個人電腦的場景**：職涯資本、副業、投資、學習、個人決策
>
> Day-job（Coupang 工作執行）→ 看 [ai-power-user-work-companion.md](./ai-power-user-work-companion.md)

## 為什麼拆兩邊

個人電腦和工作電腦的 AI 投資**性質完全不同**：

| 維度 | 個人電腦 | 工作電腦 |
|---|---|---|
| **時間尺度** | 長期 / 跨年累積 | 當週 / 當季交付 |
| **資料風險** | 公開 / 個人資料 | 公司機密 |
| **主要 ROI** | 職涯資本、跳槽彈藥、副業飛輪 | 當期績效、跨部門效率 |
| **決策性質** | 我的人生 | 我的工作 |
| **可遷移性** | 換工作不會消失 | 離職就清空 |

**關鍵 insight**：個人電腦是你的「**職涯資產負債表**」。每個 skill 都該回答「這對 5 年後的我有什麼幫助」。

---

## 模塊 A：驗收紀律 — User Story（個人電腦）

### 觸發情境
**週日 21:00**，你想把這週某個工作觀察寫成 Medium 文章——「為什麼 RevOps 該停止做 quarterly forecast」。

### 沒有驗收紀律時
- 21:00 開 Claude，「寫一篇 Medium 文章關於 quarterly forecast 為什麼該停」
- 22:00 拿到第一版——結構對但 hook 弱、tone 太教科書
- 23:00 改 tone，但你不確定這篇配不配進你過去 56 篇的水準
- 隔天還在想要不要發
- **痛點**：3h 寫出一篇你自己都不確定的文章

### 有驗收紀律時
- 21:00 翻 `~/templates/medium_top3.md`（你過去 56 篇互動率最高的 3 篇結構）
- 翻 `~/templates/medium_flopped.md`（互動最低的反例，你已分析過為什麼差）
- 貼下面這段
- 21:30 拿到對標自己最強水準的版本
- 22:00 完稿發出
- **得益**：3h 變 1h，**且發得出去的把握強**

### 你會輸入的 prompt
```
Write a Medium article: "Why RevOps Should Stop Doing Quarterly Forecasts"
Target reader: senior RevOps / FP&A / Director-level
Length: 1200-1500 words

GOOD examples (my own top 3 articles):
[paste medium_top3.md — your top 3 patterns: hook / structure / signature voice]

BAD example (my flopped article):
[paste medium_flopped.md — what doesn't work for my audience]

Acceptance checklist:
- [ ] Hook 用反直覺 statement 開頭（像 top 3 的模式）
- [ ] 第 2 段就有具體場景（不是抽象 framework）
- [ ] 至少 1 個我自己經歷的故事
- [ ] 結尾留 reader 可以做的 1 件事
- [ ] Voice 要像我之前最強那 3 篇，不是教科書
```

### 套用範圍
- Medium 文章
- 求職 cover letter
- LinkedIn 長 post
- 投資論文（`investment_note/research/`）
- 個人年度回顧

---

## 模塊 B：上下文與記憶架構 — User Story（個人電腦）

### 觸發情境
**週六 10:00** 想看本週 personal_os dashboard，順便把投資組合回顧一下。

### 你已經做到的
- 開新 session 說「跑 personal_os dashboard」
- Claude 從 `~/Side_project/personal_os/CLAUDE.md` 知道 dashboard 怎麼跑
- 從 `investment_note/RULES.md` 知道你的投資原則
- 從 `investment_note/portfolio.md` 知道現持倉
- 0 暖機

### 唯一升級
打開 `~/.claude/CLAUDE.md` 逐條審計。**Boris 個人 CLAUDE.md 只有 ~76 token**——你很可能太肥。

### 對個人電腦特有的價值
- 跨 session 記得你的人生脈絡（家人、興趣、長期目標）
- AI 真的「認識你」，不是每次重新介紹

---

## 模塊 C：多 Agent 編排 — User Story（個人電腦）

### 觸發情境
**週六下午**，你想研究「2026 年該不該加碼某 AI 公司股票」。

### Solo 模式
- 自己一條 thread：讀財報 → 讀分析師報告 → 比同業 → 想 catalyst
- 4 小時下來只看完 2 家
- **痛點**：序列太慢，深度不夠廣度

### Manager 模式
- 開 4 個 subagent 並行：
  - A：讀標的最新財報 + 法說會逐字稿
  - B：抓 3 家可比公司同期數字 + multiple
  - C：scrape 該公司的 product launches、hiring trends、insider trading
  - D：讀近期 sell-side 報告，列出 bull / bear case
- 你去喝咖啡 30 分鐘
- 回來 main session 收 4 份輸出 → 寫進 `investment_note/research/<ticker>.md`
- 再開 fresh session reviewer 批一輪：「找出我論點的 weakest link」
- **得益**：4h → 1.5h，且**有 reviewer 強迫你看 bear case**

### 個人電腦特有應用
- 投資論文研究（4 個 angle 並行）
- 跳槽 target 公司研究（產品 / 文化 / 待遇 / 內推 並行）
- XHS 選題研究（熱點 / 競品 / 自身角度 / 數據 並行）
- Medium 文章準備（論點 / 反論點 / 案例 / 數據 並行）

---

## 模塊 D：規格與規劃 — User Story（個人電腦）

### 觸發情境
**12 月底**，你思考「2027 年要不要跳槽進 AI-native 公司」。

### Vibes 模式
- 想了 2 個月，越想越亂
- 一邊投履歷一邊懷疑自己準備夠了沒
- 半年後還在原地

### Spec 模式
- 12/30 21:00 跑 `/spec`
- Claude 反問你 15 題：
  - 跳槽的成功定義是什麼（薪、title、學習、地點？權重？）
  - 願意接受的 trade-off？
  - 不跳槽的機會成本（Coupang 升 director 機率多高？）
  - target 公司清單（你有 `job/2026/liblib_like_ai_companies.md`）
  - 履歷現在最弱的點？
  - 6 個月內能補強的、不能補強的？
  - 面試弱項？
  - 配偶 / 家庭因素？
  - 退路（如果跳了不適應）？
- 22:30 你被問完，自己也想清楚了
- 23:00 SPEC.md 產出：`job/2027_career_spec.md`，含 timeline + checkpoints
- 接下來半年每月 review 一次 SPEC.md，看實際 vs 計畫
- **得益**：把「焦慮的內耗」變「可追蹤的進度」

### 個人電腦特有應用（重大決策）
- 跳槽決策
- 投資加減碼
- 副業要不要 scale up（XHS 帳號要不要做大）
- 重大消費（搬家、換車、留學）
- 年度 OKR（個人，不是工作）

---

## 模塊 E：Eval 與量測 — User Story（個人電腦）

### 觸發情境
**3 個月後**，你修改了 `xhs-note-assembly` 的 prompt，覺得「這樣應該更好」。

### 沒 eval 紀律
- 直接覆蓋舊版
- XHS 互動數變差，不知道是 prompt 改壞還是演算法變了
- 想回滾發現沒備份

### 有輕量 eval
- 改之前打開 `evals/xhs-note-assembly/cases.jsonl`（10 個過去最爆款的真 input）
- 跑舊 vs 新各 10 case，肉眼比對
- 發現新 prompt 弱化了「衝突感開頭」這條
- 修第二版再跑
- 確認 strictly better 才 ship

### 個人電腦特有 eval 對象
- XHS skills（高頻、主觀，最該量測）
- Medium 寫作 prompt
- 投資論文寫作流程
- 履歷 / cover letter 客製化 prompt

---

## 模塊 F：自動化護欄 — User Story（個人電腦）

### 觸發情境
你疲倦狀態下打 `import anthropic` 想快速試 API。

### 沒 hook
跑了 → 月底 API 帳單幾百美金消失。

### 有 hook
PreToolUse 攔住，要求你顯式 override。

### 個人電腦特有的 hook
- **Subscription-only 守門**（你 CLAUDE.md 已宣示，但只是 advisory）
- **投資操作雙重確認**：偵測 `investment_note/trades/` 寫入 → 強制讓你輸入 confirm 字樣（避免 vibe coding 改 portfolio 紀錄）
- **personal_os 自動備份**：寫入觸發 git auto-commit
- **Stop hook 推 reviewer**：寫完 Medium / 投資論文 / 求職文件 → 自動 spawn fresh-context reviewer

---

## 模塊 G：個人槓桿應用 — 🔥 P0（重新定義）

> 原本這塊在工作電腦版叫「Day Job 應用」。在個人電腦上，重新定義為**職涯資本 + 個人槓桿**。

### 核心問題

你 20+ skill 高度集中在 XHS 內容創作，但 XHS 是**已經到頂的副業**（模塊 H）。**真正缺的個人電腦 skill 是「職涯資本累積」+「人生重大決策」**。

### 該蓋的 8 個 Personal-Side Skill

| Skill | 用途 | 對你的具體 ROI |
|---|---|---|
| `resume-tailor` | 針對 target 公司客製化履歷 | 投 10 家公司省 5h，且每份對位 |
| `company-deep-research` | 深度研究 target 公司（產品 / 文化 / 內推） | `liblib_like_ai_companies.md` 上每家 30 min 變產品 |
| `interview-mock` | 針對職位生成題目 + mock + 評分 | AI 公司面試前狀態調整 |
| `narrative-builder` | 把工作戰功重寫成跳槽履歷 narrative | 你的「efficiency by 50%」變「Architected X with measurable Y」 |
| `investment-thesis-writer` | 餵入研究材料 → 結構化論文進 `investment_note/research/` | 你已有 RULES.md，缺 thesis 流水線 |
| `weekly-self-review` | 整合 git commits / record-week / personal_os 產週報 | 已有 record-week，加「給未來面試官看」的 framing |
| `medium-pipeline` | 從觀察到發布的完整流程 | Medium 56 篇能變 100 篇且品質升 |
| **`life-decision-log`** ⭐ | 重大個人決策的假設→實際追蹤 | **跨年累積的「決策品質履歷」** |

### 重點解釋 3 個

#### `narrative-builder`
**問題**：你履歷上「increased efficiency by 50%」這種話 AI 公司面試官秒看穿是空話。
**解法**：餵入 Coupang 真實工作（脫敏） + target 公司類型（AI startup / AI-native ops），AI 重寫成：
> 「Architected an AI workflow stack augmenting pricing operations with deterministic verification, reducing memo iteration cycles from 5 to 2 and saving ~6h/week. Quantified improvements via custom eval suite tracking hypothesis-vs-actual variance.」

**這個動作就值幾十萬年薪差。**

#### `investment-thesis-writer`
**問題**：你有 `investment_note/RULES.md`、`portfolio.md`、`BACKLOG.md`，但 thesis 進入流程沒系統化。
**解法**：skill 結構：
- 強制問你：catalyst / 多空論點 / 信心區間 / position sizing / kill criteria
- 自動 cross-check 你的 RULES.md
- 輸出進 `investment_note/research/<ticker>_<date>.md`
- 6 個月後自動 review：實際 vs 論文

#### `life-decision-log` ⭐
**和工作的 decision-log 不同**：這個追蹤**人生決策**——跳槽、加減碼、搬家、消費、健身投入。

```yaml
date: 2026-05-01
decision: 暫不投 X 公司履歷
hypothesis:
  - 該公司 series B 但燒錢快，2 年內可能裁員
  - 我目前 Coupang 還有空間
  - 等 Q3 拿到本年度評等再決定
expected_6m: Coupang 本月給 promotion signal / X 公司估值修正
checkpoint: 2026-11-01
actual: ???
learning: ???
```

**5 年後你回頭看這份檔案——這就是你「判斷力的演進史」**。比履歷上任何文字都有說服力。

### Roadmap（8 週、8h）

- W1-2：`resume-tailor` + `narrative-builder`（為了下次跳槽，最高 ROI）
- W3-4：`company-deep-research` + `interview-mock`
- W5-6：`investment-thesis-writer` + `life-decision-log`
- W7-8：`weekly-self-review` 升級 + `medium-pipeline`

### 對你的具體好處

1. **下次跳槽**：履歷 narrative 已經在 AI 公司頻率上，不是「會用 AI 的 RevOps」而是「親自 architect AI workflow 的 operator」
2. **投資紀律**：thesis 進論述化，5 年後你能跑出「我的 hypothesis hit rate」
3. **人生決策可追溯**：`life-decision-log` 是任何 LinkedIn / 履歷都做不到的「思考品質證據」
4. **Medium 飛輪轉得起來**：56 篇 → 100 篇 → 成為 personal brand

---

## 模塊 H：內容與知識產出 — 維持

XHS skills 已到頂。Medium 套上模塊 A + D 後再升一級即可。

---

## 一頁總結：個人電腦 8 個 User Story

| 模塊 | 觸發場景 | 帶來的具體改變 |
|---|---|---|
| A. 驗收 | 週日寫 Medium 前先貼 top 3 範例 | 3h → 1h，發得出去把握強 |
| B. 記憶 | 開新 session 不用重新介紹自己 | AI 真的認識你 |
| C. 多 agent | 投資研究 4 個 subagent 並行 | 4h → 1.5h，多 reviewer |
| D. Spec | 重大人生決策強制 spec | 焦慮內耗 → 可追蹤進度 |
| E. Eval | XHS skill 改版前跑 10 case 對比 | 知道新版真好 |
| F. Hooks | 攔 SDK / 強迫投資操作確認 | 物理生效 |
| **G. 職涯資本** | **8 個個人槓桿 skill** | **跳槽彈藥 + 人生決策史** |
| H. 內容 | Medium 套 spec + reviewer | 寫作有結構感 |

## 演練建議

這週只挑 1 個 user story 演練：
- **如果你近期想跳槽** → 模塊 G 的 `narrative-builder`（用一個現有履歷 bullet 重寫）
- **如果你重視投資紀律** → 模塊 G 的 `investment-thesis-writer`（拿 BACKLOG 一支標的試）
- **如果你想升級內容** → 模塊 A 套到下一篇 Medium

體感對了再做下一個。

---

## 兩邊邊界（重要）

**個人電腦做的（這份談的）**：
- 職涯資本累積（履歷、跳槽研究、面試）
- 副業飛輪（XHS、Medium）
- 投資 / 個人 OS / 健身 / 重大決策
- 學習 / 研究筆記
- AI workflow **方法論研究**（在這裡先 prototype，validated 再 port 到工作）

**工作電腦做的**（→ 看 work companion 文件）：
- 真實 day-job 執行（pricing / SQL / dashboard / cross-team）
- 公司資料相關 skill
- 工作 decision log（不是人生 decision log）
- 跨部門 deliverable

**邊界原則**：公司資料不上個人電腦，個人 narrative 不上公司 git。**模塊框架共用，user story 兩邊各一份**。

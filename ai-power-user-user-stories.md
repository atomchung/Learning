# AI Power User — 8 個模塊的 User Story

> 配套文件：[ai-power-user-roadmap.md](./ai-power-user-roadmap.md)
>
> 每個模塊一個「週三下午」式的具體場景，演練「沒有 → 有」的差別

每個 story 結構：
- **觸發情境**：一個真實工作日的具體時刻
- **沒有這個能力時**：你現在會怎麼做（帶時間和痛點）
- **有了這個能力時**：套上 pattern 後會怎麼做
- **你具體會輸入什麼**：可以照抄的 prompt / 動作

---

## 模塊 A：驗收紀律 — User Story

### 觸發情境
**週四 14:30**，老闆 Slack：「明天 9 點要給 Country Director 一份 Q2 pricing strategy memo，2 頁，重點是怎麼應對蝦皮促銷壓力。」

### 沒有驗收紀律時（你現在）
- 14:30 打開 Claude，「幫我寫一份 Q2 pricing strategy memo 應對蝦皮，2 頁」
- 15:00 拿到第一版——結構對但 tone 不對，太工程化
- 15:30 改 tone，但深度不夠
- 17:00 改第 5 版，越改越亂
- 19:00 才交出去，你不確定夠不夠好
- **痛點**：4.5 小時，不確定品質

### 有驗收紀律時
- 14:30 開 Claude，先做 3 件事：
  1. 翻 `~/Side_project/templates/pricing_memo_good.md`（你之前老闆讚過 "this is exactly what I want" 的那篇）
  2. 翻 `~/Side_project/templates/pricing_memo_bad.md`（被退過的版本，老闆 comment 寫著 "too tactical, missing strategic framing"）
  3. 直接貼下面這段
- 15:30 拿到品質直接對標老闆品味的版本，你只需要改 20%
- 16:30 交出去
- **得益**：3h 變 2h，**且你知道為什麼這份夠好**

### 你會輸入的 prompt
```
Write a Q2 pricing strategy memo for Country Director. 2 pages.
Focus: respond to Shopee's promo aggression in TW market.

GOOD output looks like:
[paste pricing_memo_good.md — the one boss said "exactly what I want"]

BAD output looks like:
[paste pricing_memo_bad.md — the one with comment "too tactical"]

Acceptance checklist:
- [ ] Opens with strategic framing (not tactic list)
- [ ] Has 3 scenarios with quant impact
- [ ] Recommendation is one clear paragraph, not bullets
- [ ] No more than 2 pages
- [ ] References Q1 actuals from [path/to/data]
```

---

## 模塊 B：上下文與記憶架構 — User Story

### 觸發情境
**週一 10:00**，你開新 session 想繼續上週的競品分析。

### 沒有架構時
- Claude 不知道「蝦皮 Q1 促銷活動」在你資料夾哪裡
- 你重複貼 context、解釋你是誰、解釋專案
- 每個 session 開頭花 10 分鐘暖機

### 有架構時（你已經在做的）
- 你只說「繼續上週的競品分析」
- Claude 從 `personal_os/tasks/` 找到上週紀錄、從 `Side_project/CLAUDE.md` 知道規範、從 personal_os 知道你是誰
- 0 暖機時間，直接幹活

### 唯一升級動作（30 min）
打開 `~/.claude/CLAUDE.md`，逐條問「Claude 真的會違反這條嗎？沒這條會錯嗎？」刪掉 30%。**Boris 的個人 CLAUDE.md 只有 ~76 token**。

---

## 模塊 C：多 Agent 編排 — User Story

### 觸發情境
**週二 9:00**，週會前要交一份「本週競品動態 + 我們的回應建議」。範圍：4 家競品 × 3 個品類。

### Solo 模式（你現在）
- 9:00-9:30 跑 SQL 拉蝦皮資料
- 9:30-10:00 跑 SQL 拉 momo 資料
- 10:00-10:30 跑 PChome
- 10:30-11:00 整理 → 寫建議
- **痛點**：序列做完 2h，11:00 才開始寫，週會 11:30 開

### Manager 模式
- 9:00 開 4 個 terminal tab，每個 worktree 跑一家競品的 subagent
- 9:00-9:15 你 spec 任務（每家輸出格式統一：促銷類型 / 折扣幅度 / 品類 / 持續時間）
- 9:15-9:45 4 個並行跑，你去喝咖啡
- 9:45-10:15 Main session 收 4 份輸出，跑差異對比 + 寫建議
- 10:15-10:30 fresh session reviewer 批一輪
- 10:30 完成，11:30 開會還能再修
- **得益**：2h 變 1.5h，**且品質有 reviewer 把關**

### 你會輸入的 prompt（main → 4 個 subagent 的 spec）
```
For each competitor in [Shopee, momo, PChome, Coupang], spawn a parallel
subagent that:

1. Pulls last 7 days of promo activity from [data source]
2. Categorizes by: promo type / max discount / category / duration
3. Outputs JSON: {competitor, promos: [{type, discount_pct, category, days}]}
4. Returns ≤ 200 tokens

Then I'll merge in main session and write strategic response.
```

---

## 模塊 D：規格與規劃 — User Story

### 觸發情境
**週五 16:00**，老闆說：「下季度想做一個 dynamic pricing 的小型 experiment，你想想看怎麼設計。」

### Vibes 模式（你現在）
- 週末加班想了 3 小時
- 週一交「我覺得可以這樣做」的 1 頁紙
- 老闆問 5 個你沒想到的問題（「成功標準是什麼？」「會不會影響其他品類？」「資料夠嗎？」）
- 你回去重做
- **痛點**：來回 3 輪、2 週才 align

### Spec 模式
- 週五 16:00 直接 `/spec`
- Claude 反問你 12 題：成功標準、失敗 rollback 條件、實驗品類、控制組設計、需要哪個 team 配合、預算、時間軸、可能 confound、stakeholder map、報告節奏、退場機制、最壞情況
- 16:30 你已經被問完，自己也想清楚了
- 16:30-17:00 Claude 寫 SPEC.md
- 週一 9:00 用 SPEC.md 直接和老闆 align，**老闆的問題你已經有答案**
- **得益**：2 週變 1 個 1:1

### 你會輸入的 prompt
```
/spec

I need to design a dynamic pricing experiment for next quarter.
Coupang Taiwan, e-commerce platform.

Interview me using AskUserQuestion. Don't ask obvious questions.
Dig into:
- success criteria (how do we know it worked?)
- failure / rollback conditions
- stakeholder dependencies (who do I need from analytics, eng, ops?)
- statistical design (control group, power, duration)
- worst-case scenarios
- post-experiment decision tree

After interview, output SPEC.md with:
goal / non-goals / hypothesis / design / metrics / risks / timeline /
open questions
```

---

## 模塊 E：Eval 與量測 — User Story

### 觸發情境
**3 個月後的某週日 20:00**，你修改了 `xhs-note-assembly` 的 prompt，覺得「這樣應該更好」。

### 沒 eval 紀律時
- 直接覆蓋舊版
- 接下來 2 週 XHS 互動數變差，你不知道是 prompt 改壞還是演算法變了
- 想回滾發現沒備份

### 有輕量 eval 時
- 改之前打開 `evals/xhs-note-assembly/cases.jsonl`（10 個你過去最爆款的真 input）
- 跑舊 prompt vs 新 prompt 各跑 10 case，肉眼比對
- 5 case 新版明顯好、3 case 差不多、2 case 新版變差
- 看那 2 個變差的：發現新 prompt 弱化了「衝突感開頭」這條
- 修 prompt 第二版，再跑一次
- 確認 strictly better 才 ship
- **得益**：你**知道**新版更好，且具體知道哪裡好哪裡需注意

### 你會輸入的動作（不是 prompt，是 workflow）
```
1. cd ~/Side_project/skills/xhs-note-assembly
2. cat evals/cases.jsonl  # 你的 golden set
3. 跑舊 prompt 10 次 → save outputs/v1/
4. 跑新 prompt 10 次 → save outputs/v2/
5. 開 vimdiff 或 web diff 工具肉眼比
6. 標 pass/fail 寫進 evals/results.md
7. 如果 v2 strictly better → git commit；否則回去調
```

---

## 模塊 F：自動化護欄 — User Story

### 觸發情境
**某天疲倦狀態下**，你 vibes-coding 寫了 `import anthropic` 想快速試一個 API call。

### 沒 hook 時
- 跑了，有效，回頭忘記改回 subscription 模式
- 月底 API 帳單來，幾百美金消失
- 你的 CLAUDE.md 明明寫了「禁用 SDK」，但**你自己**忽略了
- **痛點**：advisory rule 對自己沒約束力

### 有 hook 時
- PreToolUse hook 攔住 `import anthropic`
- 跳訊息：「Subscription-only 規則。要繞過？輸入 ALLOW_SDK_ONCE=1。」
- 你想起來了，改用 `subprocess.run(["claude", "--print", ...])`
- **得益**：規則從「希望我自己記得」→「物理上做不到」

### 你會輸入的 hook（一次設定，永久生效）
```bash
# ~/.claude/hooks/pre-tool-use-block-sdk.sh
#!/bin/bash
if echo "$CLAUDE_TOOL_INPUT" | grep -qE "import anthropic|from openai|ANTHROPIC_API_KEY"; then
  if [ "$ALLOW_SDK_ONCE" != "1" ]; then
    echo "BLOCKED: subscription-only mode. Set ALLOW_SDK_ONCE=1 to override."
    exit 1
  fi
fi
```

---

## 模塊 G：本職領域應用 — 8 個 User Story 🔥

### G1. `sql-reviewer`

**觸發**：週二 11:00，你寫完一段 SQL 拉「過去 30 天 high-value 用戶的定價敏感度」，準備跑。

**沒這 skill 時**：跑 → 結果怪 → debug 1h 發現 join 條件錯了一個 NULL handling，你 query 把 4% 的 user 算錯。

**有 skill 時**：`/sql-reviewer < my_query.sql`，30 秒拿到：
- ⚠️ Line 12: LEFT JOIN with NULL on user_id will silently drop 4% rows
- ⚠️ Line 18: timezone mismatch between `purchase_ts` (UTC) and `event_ts` (Asia/Taipei)
- ✅ Aggregation logic looks correct
- 💡 Consider adding `WHERE created_at > now() - 90 days` index hint

**輸入**：
```
/sql-reviewer
[paste SQL]

Check: correctness / join risks / NULL handling / timezone /
data leakage / performance / common pitfalls
Output: prioritized issues with line numbers + suggested fix
```

---

### G2. `pricing-change-premortem`

**觸發**：週四 15:00，老闆說「明天就要把 X 品類 30 個 SKU 全降 5%」。

**沒這 skill 時**：直接改，週末爆炸——發現有 3 個 SKU 是套裝商品的子品，組合定價變負毛利。

**有 skill 時**：`/pricing-premortem` 跑 5 分鐘吐：
- 🔴 SKU-A123, A456, A789 是 bundle 子品，調整後組合毛利 -2%
- 🟡 競品價格已比這批更低，5% 仍 uncompetitive
- 🟡 Margin floor 設定 vs 新價：3 個 SKU 觸 floor
- 🟢 庫存週轉支撐這幅降價
- 💡 建議分批：先降 22 個無 bundle 衝突的 SKU

**輸入**：
```
/pricing-premortem
SKUs: [list]
Change: -5% across the board
Effective: tomorrow

Run pre-mortem covering:
- bundle / cross-sell impact
- margin floor breach
- competitor reaction game theory
- inventory / cash flow
- system flag risks (auto-discount stacking?)
Output: red/yellow/green table + recommended sequencing
```

---

### G3. `elasticity-scenario-gen`

**觸發**：週五要交「降價 3% / 5% / 8%」三個情境的 GMV 預測。

**沒這 skill 時**：開 Excel 手刻 3 小時。

**有 skill 時**：`/elasticity-scenario` 30 秒給你 3 情境的：GMV / margin / unit volume / cannibalization estimate / 信心區間。輸出可以直接貼進 PPT 的表格。

---

### G4. `competitor-anomaly-detector`

**觸發**：每天早上 9:00 自動跑（hook 觸發）。

**沒這 skill 時**：你週三才從業務同事口中聽說「蝦皮週一就在 push 一個 12% off 母嬰大促」。慢 48 小時。

**有 skill 時**：週一 9:05 你信箱收到 `[ANOMALY] 蝦皮 母嬰品類 平均折扣從 4% 跳到 12%，超過 2 sigma`。週一中午你已經出 response plan。

---

### G5. `weekly-pricing-narrative`

**觸發**：週五 17:00，準備下週 1:1 + 月底 QBR。

**沒這 skill 時**：週日加班翻 5 個 dashboard、3 個 Slack thread、2 個 doc，拼湊「這週做了什麼」。

**有 skill 時**：`/weekly-narrative` 自動讀本週的 git commits（你的工作 log）+ 改價紀錄 + 競品事件 + dashboard 變動，輸出 markdown：
```
## 本週改了什麼
- X 品類 12 SKU 調價，預計 GMV +1.2%（待 verify）
- 對應蝦皮母嬰大促上線 24h 內 response
## 為什麼
...
## 下週要盯
- ABC dashboard：verify 改價後 GMV impact
- 競品下波促銷預測：母親節
## 風險
...
```
**這直接是 1:1 / QBR / promotion review 的素材**。

---

### G6. `dashboard-qa`

**觸發**：週二 14:00 BD team 說「為什麼你的 dashboard 顯示 X 但我們的 BI 報表是 Y」。

**沒這 skill 時**：你跟 BD 各執一詞 1 小時，最後找 data eng 仲裁，發現是分母定義不同。

**有 skill 時**：`/dashboard-qa <dashboard_url>`，輸出：
- 指標定義 vs 公司 metric standard 的 diff
- 分母 / 分子拆解（你的 vs 標準）
- Stale data 警示（`updated_at` 已 26h 沒動）
- 跨 dashboard 引用一致性

---

### G7. `excel-sql-bridge`

**觸發**：BD 同事丟一個 Excel：「這 200 行能不能幫我跑出每個 SKU 的歷史最低價？」

**沒這 skill 時**：你手動把 SKU list 抄成 SQL 的 IN clause，10 分鐘。

**有 skill 時**：`/excel-to-sql data.xlsx --question "歷史最低價 per SKU"`，30 秒產 SQL，再跑。

---

### G8. `decision-log` ⭐ 最重要

**觸發**：每次重要決策（改價、實驗、推 initiative）後 5 分鐘。

**沒這 skill 時**：3 個月後 promotion review，你寫「我做了 A、B、C，提升了 efficiency 50%」——和所有 senior manager 一樣空洞。

**有 skill 時**：每筆決策都有結構化紀錄：
```yaml
date: 2026-05-01
decision: X 品類降價 5%
hypothesis: 競品壓力下，降 5% 可彈性 0.8 推 GMV +4%
action: 30 SKU 同步調整
expected: GMV +1.2%（對 P&L），margin -0.3pp
actual_30d: GMV +1.5%, margin -0.4pp
delta_explanation: bundle 效應比預期強
learning: 下次 bundle 子品要單獨建模
```

3 個月後 promotion review 你寫：
> 「Built a decision-log system tracking 47 pricing decisions in Q2. Hypothesis-vs-actual variance reduced from initial 35% to 12% over the quarter, indicating measurable improvement in pricing intuition. 3 specific patterns were extracted and codified into team SOPs.」

**這就是 director track vs senior manager 永遠停留的差異。**

---

## 模塊 H：內容與知識產出 — User Story

### 觸發
**週日 21:00**，你想寫一篇 Medium：「我用 Claude Code 一年的反思」。

### 你已經會做的
打開 Claude Code，對著 `personal_os/` + 過往 56 篇 Medium，10 分鐘出大綱、1 小時完稿。**這塊不需要升級**。

### 唯一可加（套用模塊 A + D）
- 寫之前先 `/spec`：interview 你定 narrative、target reader、success metric
- 寫完 fresh session reviewer 批一次

從「會寫」→「**寫得跟 Dan Shipper 一樣有結構感**」。

---

## 一頁總結：8 個 user story 一句話版

| 模塊 | 你做的具體動作 | 帶來的具體改變 |
|---|---|---|
| A. 驗收 | 寫 memo 前先貼老闆讚過的版本 + checklist | 一次到位率 50% → 85% |
| B. 記憶 | CLAUDE.md 瘦身到 30% | Claude 真的看你的規則了 |
| C. 多 agent | 競品分析 4 個並行 subagent | 2h → 1.5h，多一道 reviewer |
| D. Spec | 大決策前 `/spec` 強制反問 | 來回 3 輪 → 1 個 1:1 |
| E. Eval | 改 skill 前跑 10 case 對比 | 知道新版真的更好 |
| F. Hooks | PreToolUse 攔禁忌操作 | 規則從希望→物理生效 |
| G. **Day Job** | **8 個 RevOps skill** | **promotion review 有彈藥** |
| H. 內容 | 套 spec + reviewer 到寫作 | 寫作有結構感 |

## 演練建議

不要一次想吃 8 個。**這週只挑模塊 A 的 user story 演練 1 次**：
1. 找一個本週要交的 deliverable
2. 翻一個過去做得好的範例 + 一個被改的範例
3. 都貼進 prompt + 寫 5 條 checklist
4. 看品質差別

體感對了再做下一個模塊。**8 個 story 全在腦子裡 ≠ 8 個 story 都會用**。

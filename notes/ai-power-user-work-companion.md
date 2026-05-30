# AI Power User — 工作電腦 Companion

> 配套：[ai-power-user-roadmap.md](./ai-power-user-roadmap.md)、[ai-power-user-user-stories.md](./ai-power-user-user-stories.md)
>
> **這份只談工作電腦的場景**：day-job 執行、公司資料、跨部門交付
>
> 個人 / 副業 / 投資 / 跳槽 → 看 [ai-power-user-user-stories.md](./ai-power-user-user-stories.md)

## 為什麼工作電腦要單獨一份

模塊框架（A-H）共用，但工作電腦有 4 個獨特約束：

1. **資料機密性**：公司資料不能離開公司網路 / 設備
2. **合規性**：subscription mode 紀律可能不適用（公司可能有自己 API key 政策）
3. **時效性**：當週交付為主，個人電腦的「跨年累積」邏輯不適用
4. **被審計**：你的工作電腦上跑的 AI 動作可能被 IT / Compliance 看

**因此工作電腦上**：
- 不要 sync 個人 skill 庫過去（XHS、投資、life-decision-log 都不該在）
- skill 應**精選 + 工作專用**，不堆積
- 護欄優先級高於個人電腦（hook 該攔的 attack surface 不一樣）

---

## 工作電腦的 8 模塊適用版

### 模塊 A：驗收紀律 — 工作場景

**User Story**：週四 14:30 老闆要 Q2 pricing strategy memo。

**動作**：
- `~/work_templates/`（工作電腦獨立資料夾）放：
  - `pricing_memo_good.md`（老闆讚過的範本，**已脫敏 / 用 placeholder**）
  - `pricing_memo_bad.md`（被退過的反例）
  - `qbr_format.md`
- 任務開頭強制貼範本 + checklist

**和個人電腦的差異**：個人電腦的 templates 偏「我自己的品味」，工作電腦的 templates 偏「**老闆的品味 / 公司的調性**」。

---

### 模塊 B：上下文記憶 — 工作場景

**工作電腦 CLAUDE.md 該有的**：
- 公司 / 部門縮寫表（你的同事、跨部門 stakeholder）
- 常用資料源路徑 / dashboard URL
- 公司 metric 定義標準（避免和 BD 同事吵分母）
- 你的 codebase / SQL repo 結構

**不該有的**：個人偏好、人生脈絡、投資 RULES（那些屬於個人電腦）。

**重要紀律**：工作電腦 CLAUDE.md **不得 git push 到個人 GitHub**。建議 push 到公司內部 repo 或本地 only。

---

### 模塊 C：多 Agent 編排 — 工作場景

**User Story**：週二 9:00 週會前要交「本週競品動態」，4 家競品 × 3 品類。

**動作**：4 個 worktree 並行跑競品 subagent，main session 收斂。

**和個人電腦的差異**：個人電腦並行做的是「跨年研究」（投資、選題），工作電腦並行做的是「**當週交付**」——時間 pressure 完全不同。

---

### 模塊 D：規格與規劃 — 工作場景

**User Story**：老闆說「下季度想做 dynamic pricing experiment」。

**動作**：`/spec` interview → `SPEC.md` 帶去和老闆 align。

**和個人電腦的差異**：工作 SPEC 重點在「**stakeholder alignment**」（誰要批、誰要配合、誰會擋），個人電腦 SPEC 重點在「**自我釐清**」。

---

### 模塊 E：Eval — 工作場景

**Codex 修正後的輕量版**對工作電腦尤其適用——你**沒時間**蓋完整 eval pipeline。

**該做**：
- 對 3-5 個生產級 work skill 各做 5-10 case 的 example library
- 每月花 30 分鐘掃一次

**不該做**：每個 skill 都建 eval。**只給每天用的那幾個**。

---

### 模塊 F：自動化護欄 — 工作場景（**這塊比個人電腦重要**）

工作電腦的 hook 要更嚴：

1. **公司資料防外流**：PreToolUse 偵測 SQL 結果 / production 資料夾被讀取後嘗試外發 → block
2. **MCP 白名單**：只允許 approved 的 MCP server 啟用
3. **Bash 防呆**：production database 寫入動作強制二次確認
4. **commit 前 PII 掃描**：防止把同事 email / 內部數字推上 repo

**這層 hook 一旦設好，你的「在工作電腦用 AI」這件事在 IT/Compliance 面前是 defensible 的**。

---

### 模塊 G：Day Job RevOps Skill 套件 — 🔥 P0

**這是工作電腦的主秀**。8 個 skill 全在工作電腦，**不要 sync 到個人電腦**。

| Skill | 用途 | ROI |
|---|---|---|
| `sql-reviewer` | query 正確性 / join 風險 / NULL handling | 每週省 2-3h debug |
| `pricing-change-premortem` | 改價前跑「會不會壞掉」 | 避免漏損事件 |
| `elasticity-scenario-gen` | 自動跑彈性 / margin 模擬 | 從 Excel 解放 |
| `competitor-anomaly-detector` | 競品異常偵測 | 比同事早 24h |
| `weekly-pricing-narrative` | 本週改了什麼 / 為什麼 / 下週盯什麼 | 1:1、QBR、晉升素材 |
| `dashboard-qa` | 指標定義 / 分母 / stale data 檢查 | 數據 trust↑ |
| `excel-sql-bridge` | Excel ↔ SQL 雙向轉 | 業務提需求 30 秒生 SQL |
| **`work-decision-log`** ⭐ | 工作決策的 hypothesis vs actual | **promotion review 素材庫** |

### 工作 vs 個人 decision log 的差異

| | 個人 `life-decision-log` | 工作 `work-decision-log` |
|---|---|---|
| 追蹤對象 | 跳槽、投資、消費、健身 | 改價、實驗、initiative |
| 時間尺度 | 跨年 | 跨季 |
| 用途 | 跳槽履歷、自我認識 | promotion review、跨團隊 trust |
| 儲存位置 | 個人電腦 personal_os | 工作電腦（**或公司 wiki**） |
| 寫法 | 私人語氣 | 半正式，可能要分享 |

**兩邊都做**，但內容不互通。

### 工作 decision log 演練範例

```yaml
date: 2026-05-01
decision: X 品類降價 5%
hypothesis: 競品壓力下降 5% 可彈性 0.8 推 GMV +4%
action: 30 SKU 同步調整
expected_30d:
  gmv: +1.2%
  margin: -0.3pp
actual_30d:
  gmv: +1.5%
  margin: -0.4pp
delta_explanation: bundle 效應比預期強
learning: 下次 bundle 子品要單獨建模
shared_with: [Country Director, BD lead]
```

**3 個月後 promotion review 你寫**：
> 「Built a decision-log system tracking 47 pricing decisions in Q2. Hypothesis-vs-actual variance reduced from 35% to 12% over the quarter, indicating measurable improvement in pricing intuition. 3 specific patterns extracted into team SOPs.」

**這就是工作電腦這份的最大產出。**

---

### 模塊 H：工作電腦不適用

H 是內容與副業——不該在工作電腦做。

---

## 工作電腦 vs 個人電腦的邊界規則

| 動作 | 個人電腦 | 工作電腦 |
|---|---|---|
| 寫 Medium / XHS | ✅ | ❌ |
| 處理公司 SQL / 資料 | ❌ | ✅ |
| 跳槽研究 | ✅ | ❌ |
| 投資紀錄 | ✅ | ❌ |
| 工作 decision log | ❌ | ✅ |
| 個人 life decision log | ✅ | ❌ |
| Coupang 競品分析 | ❌ | ✅ |
| AI workflow 方法論 prototype | ✅（先試） | port 過來 |
| Subscription mode 紀律 | ✅ 嚴格 | 看公司政策 |
| MCP 白名單嚴格度 | 寬 | **嚴** |

## Roadmap（工作電腦獨立執行）

```
Week 0（30 min）— 隔離設定
└─ 工作電腦獨立 ~/work_templates/、~/.claude/CLAUDE.md，不同步個人

Week 1-8（每週 1h，8h）— Day Job 8 skill
└─ 同個人電腦版的 G 段順序

Week 9-10（2h）— 工作專屬護欄
└─ MCP 白名單、PII 掃描 hook、production DB 二次確認

Ongoing
└─ 每週 30 min decision-log review
```

## 結論：兩邊各司其職

- **個人電腦**累積「**5 年後還在的東西**」（職涯資本、判斷力史、副業飛輪）
- **工作電腦**處理「**當期績效 + 公司可見的產出**」（pricing ops、跨部門 deliverable、promotion 素材）

兩邊**模塊框架（A-H）一樣**，**user story 完全不同**，**skill 庫不互通**。

這個拆法有 3 個好處：
1. 公司資料不外流，AI 用得 defensible
2. 個人累積不被「換工作就清空」
3. 兩邊互相 prototype——個人電腦做安全的方法論實驗，validated 再 port 到工作

# 全工作區 Eval 盤點地圖

> 盤點於 2026-05-30
> 這是 `personal_eval_playbook.md` Part 2（2026-05-10）盤點的**更新版**——20 天後重掃整個 `Side_project/`，把散落在 9+ 個 folder 的 eval 機制連到這個中心。
> **不取代** playbook，是它的橫向現況快照。

## 跟既有 eval 檔的分工

| 檔案 | 角色 |
|---|---|
| `personal_eval_playbook.md` | 方法論（Hamel/Shreya/Eugene Yan 蒸餾 + 路線圖）|
| `eval_addendum_outcome_metrics.md` | outcome metric + north star + 投資場景兩層論 |
| `llm_eval_research.md` | 理論（benchmark vs eval、工具對照）|
| `eval/`（實作層）| per-model error pattern profiling（scan_admissions.py）|
| **本檔 `eval_inventory.md`** | **橫向現況地圖：全工作區所有 eval 在哪、是什麼、接沒接 north star、跑到哪** |

---

## 一、全部 eval 在哪（按專案）

> 「接 north star?」欄是最重要的診斷——per addendum：**metric 不能 predict 真實外部結果，就是浪費。**

| 專案 · 路徑 | eval 對象 | 方法 / metric | 接 north star? | 狀態 | 更新 |
|---|---|---|---|---|---|
| `xhs_autoresearch/evaluator.py` | 標題/正文 | LLM judge A/B，5 維，B 贏≥3/5 | ❌ ting 口味 | 活躍 | 04-05 |
| `xhs_autoresearch/angle_evaluator.py` | 切角 | LLM judge A/B，6 維，4/6 | ❌ | 活躍 | 04-06 |
| `xhs_autoresearch/cover_style_evaluator.py` | 封面 prompt | LLM judge A/B，6 視覺維，4/6 | ❌ | 活躍 | 04-12 |
| `xhs_autoresearch/view_reward.py` | 標題 mutation | **真實流量** mean log10(views) lift | ✅ **真實互動數** | 活躍（最新）| 04-26 |
| `xhs_autoresearch/RESEARCH_LOG.md` | 優化主 log | 各 topic accepted rate | 部分 | 活躍 | 05-03 |
| `xhs_content_generator/video_prompt_optimization_log.md` | 影片 prompt | 20 輪 critique（變異→Before/After→判定+理由）| ❌（內部判定）| 活躍 | 04-09 |
| `xhs_skills/skills/*/evals/evals.json` ×7 | 7 支 skill 輸出 | prompt→expected_output 行為 eval | ❌ | 活躍（正本）| 03-28 |
| `rednote_analysis/post_giannis_kalshi_viral.md` §3 | 版本對比 | 「為什麼這版更好」三軸敘述 rubric | ❌ | **疑似廢棄**（早期手寫）| 02-18 |
| `news_analysis/cross_verify.py` | 新聞事實 | 多源 RSS 交叉佐證（非 LLM judge）| ✅ 外部來源 | 已實作 | 02-28 |
| `eval/` (`scan_admissions.py`) | Claude 錯誤模式 | regex 抓自認錯誤→人工 review 分類 | n/a（profiling）| **半實作停滯**（30 candidates，review/report 沒做）| 05-17 |
| `eval-skill/` + `playground/token-eval/` | Claude vs Gemini | token/cost/quality A/B，16 欄 CSV | 成本✅/品質❌ | 已實作，**12 筆但 quality_score 多半沒填** | 04-05 |
| `paperclip/doc/plans/…agent-evals-framework.md` | agent bundle | 4 層（hard→single→e2e→efficiency）+ pairwise judge | 規劃中 | **純計畫** | 03-15 |
| `outcome_log/` | session 結果 | done/partial/detour/dead_end × hit_rate | ✅ 設計上 | **demo（sample data，未接 record-claude）** | 05-21 |
| `info_collector/feedback.py` | 推薦相關性 | Gmail 回信標記→興趣訊號 | ✅ 真實 read 訊號 | 已實作 | 04-06 |
| `personal_os` `pre_task_feedback.py` hook | 防重複犯錯 | UserPromptSubmit 自動注入 feedback 記憶 | n/a（infra）| hook 在跑 | 05-23 |
| `investment_note/evals/`（golden set）| 裸模型回歸 | 5 case pass/fail，ai-errors 凍結成 test | n/a（process）| 今天建，**首跑污染**（見下）| 05-30 |
| `investment_note/knowledge/decision-review.md` | 投資決策 | batting average + 30/60/90 cadence | ✅ **真實 P&L / falsification** | 跑過 1 次（56%）| 05-23 |
| `investment_note/knowledge/ai-errors.md` | AI 錯誤紀錄 | 23 筆人工記錄 + protocol 對應 | n/a | 活躍 | 05-30 |

---

## 二、按 eval 對象分類（5 類）

1. **內容品質 eval（xhs，最成熟）** — 4 個評估器 + critique log + skill 行為 eval。投入最深（playbook 記載 605+ 輪）。
2. **模型/工具正確性 eval** — `cross_verify`（事實佐證）、`eval/`（Claude 錯誤 profiling）、`investment_note/evals`（裸模型回歸）、`ai-errors`（人工錯誤庫）。
3. **成本/效率 eval** — `token-eval`（Claude vs Gemini）、Paperclip L4。
4. **決策 / outcome eval** — `decision-review`（投資 calibration）、`outcome_log`（session 結果）、`info_collector feedback`（推薦相關性）。
5. **防錯 infra** — `pre_task_feedback` hook、ai-errors→protocol 閉環。

對照今天在 investment_note 釐清的兩條腿：**第 1/2/3 類是 process eval（過程對不對），第 4 類是 outcome eval（結果對不對）**。

---

## 三、現況評估（5/10 → 5/30 變了什麼）

**✅ 進展：north star 對齊開始落地。**
playbook/addendum 5/10 的頭號診斷是「xhs 跑 605 輪但都在學 ting 口味，沒接真實平台 outcome」。`view_reward.py`（4/26）正是那帖藥——把真實 views 接進 mutation reward。investment_note 的 `decision-review`（真實 P&L/falsification）也是 addendum「投資用 calibration 不用 LLM eval」的實作。**方向對了。**

**⚠️ 共同病：建好了，但沒收尾 / 沒持續餵。**
這是跨專案最一致的問題，違反 playbook 第 7 條「eval 是流動的，不是一次性產物」：
- `token-eval`：12 筆跑完，quality_score 多半空白
- `eval/`：30 candidates 掃出來，人工 review 沒做、`reports/` 空
- `outcome_log`：還在 sample data，沒接回 record-claude
- `decision-review`：只有 1 個時間點（56%），缺多季趨勢
- `investment_note/ai-errors`：系統自己承認「寫進去 ≠ 行為改變」

→ 你不缺 eval intuition（playbook 早就說了），缺的是**收尾與餵養的紀律**。eval 的價值在第 2、第 3 次跑出趨勢，不在第 1 次建好。

**🆕 今天的新洞察（investment_note golden set 撞出，playbook 沒提）：**
**在 repo 內用 sub-agent 跑 blind eval 會被 CLAUDE.md 污染**——protocol、答案、當前日期全洩漏，強弱模型都被拉到滿分（opus 5/5 = haiku 5/5），鑑別力歸零。要測「裸模型」必須脫離專案 context（API script 或 repo 外 CLI）。這條對所有「想測模型本身而非系統」的場景都適用。

**🧹 待 dedup（順手記）：**
`xhs_skills/skills/*/evals/evals.json` 是正本（`~/.claude/skills/` symlink 指向）；`crewai_xhs/skills/`、`crewai_xhs/.claude/worktrees/…`、`crewai_xhs/xhs_skills/` 都是 **byte-identical 重複副本**，建議收斂到單一 source of truth 後刪。

---

## 四、缺口 + 下一步（接續 playbook 路線圖，更新到 5/30）

| 優先 | 動作 | 對應 |
|---|---|---|
| 1 | 給每個 active eval 補「收尾」：token-eval 補 quality_score、eval/ 做一次人工 review、outcome_log 接回 record-claude | 治「建好沒收尾」共同病 |
| 2 | xhs：把 `view_reward` 的真實流量正式接進 evaluator 校準（judge 能不能 predict views），算 spearman | addendum Q2 未完成的最後三步 |
| 3 | investment_note：跑乾淨版 golden baseline（脫 CLAUDE.md），decision-review 補多季 batch + AI/人標籤 | 今天的兩條腿 |
| 4 | dedup crewai_xhs 重複 evals.json | 衛生 |

**不要做**（沿用 playbook）：不再多跑 xhs 輪數（先對齊 outcome）、投資 thesis 不上 LLM judge（用 decision journal）、前 3 個月不碰 DeepEval/Braintrust。

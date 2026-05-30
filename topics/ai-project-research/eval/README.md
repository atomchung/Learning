# Eval — Implementation Layer

> Per-model profiling 系統的實作層。研究筆記在 parent folder（`personal_eval_playbook.md` 等）。

## 目的

追蹤 Claude / Codex / Gemini 在我實際場景下的 **error pattern 分布**。

不是驗證「我的判斷對不對」（那是 decision journal 的事），而是 profile **模型在哪類事情上常翻車** → 讓我下次能在 prompt / CLAUDE.md 預先防範。

## 跟 parent `.md` 的分工

| File | 角色 |
|---|---|
| `../personal_eval_playbook.md` | 方法論：個人 eval 怎麼做（Hamel / Shreya / Eugene Yan 蒸餾） |
| `../llm_eval_research.md` | 理論研究：benchmark vs eval、工具對照 |
| `../eval_addendum_outcome_metrics.md` | 補充：outcome metric、投資場景結論（thesis 用 decision journal、不該 LLM eval） |
| **這層 (`eval/`)** | **實作**：跑 script、存 runs、寫 reports |

## 結構

```
eval/
├── README.md
├── SCHEMA.md                # admissions.jsonl 欄位設計
├── .gitignore               # runs/*.jsonl 擋掉（隱私）
├── tools/
│   └── scan_admissions.py   # regex pre-filter scan transcript
├── runs/                    # ⚠️ 不入 git（含對話 raw 片段）
│   ├── candidates_YYYY-MM-DD.jsonl   # script 跑出的候選
│   └── admissions.jsonl              # 人工 review 後 promote 的真實 admission
└── reports/                 # 季 / 月 synthesize
```

## 工作流（MVP）

1. **每週 / 隨手** 跑 `python3 tools/scan_admissions.py 7`（看過去 7 天）
2. 開 `runs/candidates_YYYY-MM-DD.jsonl`，逐筆掃過：
   - **真實 admission**：填 `is_real_admission=true`、`error_type`、`root_cause`、`fix`，append 到 `admissions.jsonl`
   - **客套 / false positive**：跳過（不用回填）
3. **累積 30 筆真實 admission 後** synthesize：哪類 `error_type` 最多？`root_cause` 集中在哪？哪個 `cwd`（專案）最常翻車？→ 寫進 `reports/` + 必要時更新 CLAUDE.md 防範規則

## 不做什麼（依 playbook 原則）

- ❌ 不直接上 LLM judge（playbook：「程式 > LLM > 人」優先序，第一批先靠 regex + 人工）
- ❌ 不假設這是 error rate（這是 lower bound：**你發現的錯**才會被承認）
- ❌ 不 commit `runs/`（含對話 raw 片段、cwd 路徑、私名等）
- ❌ 不框架化（playbook：前 3 個月別碰 DeepEval / Braintrust）

## 跟既有 playbook 的關係

對應 playbook 的「**對象 A：AI 工具品質 eval**」維度，不跟既有結論衝突。

未來投資 AI 工具（財報摘要 faithfulness、漏點率）也可走這個 folder。
投資 thesis 決策還是該走 decision journal（不在這裡）。

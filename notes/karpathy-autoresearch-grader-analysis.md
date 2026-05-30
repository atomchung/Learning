# Karpathy AutoResearch 評分系統分析 & Grader 設計 Best Practices

## 1. AutoResearch 是什麼？

Andrej Karpathy 的 [autoresearch](https://github.com/karpathy/autoresearch) 讓 AI agent **無人值守**地跑 ML 實驗：

> 讀程式碼 → 提假設 → 改 code → 訓練 5 分鐘 → 看指標 → 保留或丟棄 → 無限循環

實際成果：2 天跑 **700+ 實驗**，自動發現 ~20 個改進，疊加後 **11% 加速**（Time-to-GPT-2: 2.02 → 1.80 hrs）。

---

## 2. 三檔案極簡架構

```
prepare.py   🔒 不可修改 — 資料準備 + 評估函式（鎖死的考場）
train.py     ✏️  唯一可改 — 模型架構、優化器、訓練迴圈（agent 的遊樂場）
program.md   📋 人類寫的 — 研究目標、約束、決策標準（給 agent 的指令）
```

**設計精髓**：
- 人類寫 `program.md`（定方向）
- AI 改 `train.py`（做實驗）
- `prepare.py` 鎖死（保證公平評估）

沒有框架、沒有 orchestrator、沒有 state machine——只有 Markdown 指令 + LLM 的推理能力。整個系統 **~630 行 Python**。

---

## 3. 評分系統：極致簡單

### 唯一指標：val_bpb（Validation Bits Per Byte）

```
val_bpb = total_nats / (log(2) × total_bytes)
```

**為什麼選這個指標？**
- 越低越好
- **和 tokenizer 無關**——不管怎麼改 vocab 大小、模型架構，分數都能直接比較
- 在固定的 validation shard（~20.9M tokens）上計算
- 評估函式用 `@torch.no_grad()` 裝飾，鎖在 prepare.py 裡不可修改

### Keep / Discard 邏輯

```python
if new_val_bpb < current_best_val_bpb:
    git commit -m "description of change"    # 保留改進
    current_best = new_val_bpb
else:
    git reset --hard HEAD~1                  # 丟棄，回到上一版
```

就這樣。**沒有 rubric、沒有 LLM judge、沒有多維度評分**——純粹的數字比大小。

### 結果追蹤：results.tsv

```
commit      val_bpb    memory_gb  status    description
a1b2c3d     0.997900   44.0       keep      baseline
b2c3d4e     0.993200   44.2       keep      increase LR to 0.04
c3d4e5f     1.005000   44.0       discard   switch to GeLU activation
d4e5f6g     0.000000   0.0        crash     double model width (OOM)
```

加上 git history 作為完整的實驗審計軌跡。

---

## 4. 完整迴圈流程

```
1. Agent 讀 program.md — 理解研究目標和約束
2. Agent 讀 train.py — 理解當前架構
3. Agent 提出假設 — "如果加 LayerNorm 到 attention？"
4. Agent 修改 train.py
5. Agent 執行: timeout 300 uv run train.py > run.log 2>&1  (5 分鐘)
6. Agent 解析結果: grep '^val_bpb:\|^peak_vram_mb:' run.log
7. Agent 決定: 改進 → commit / 沒改進 → reset
8. 回到步驟 2，無限重複
```

**防作弊機制**：
- 不能修改 prepare.py（評估鎖死）
- 不能改資料集
- 訓練時間固定 5 分鐘
- 指標跨架構可比

---

## 5. AutoResearch vs 通用 Skill Eval 比較

| 面向 | Karpathy AutoResearch | 通用 Skill Eval |
|------|----------------------|-----------------|
| **指標數量** | 1 個（val_bpb） | 多維度（正確性、語調、安全性...） |
| **評分方式** | Code-based，數字比較 | Code + LLM + Human 組合 |
| **判定邏輯** | Binary（改進 vs 沒改進） | 加權分數 + 門檻 |
| **評估對象** | ML 訓練結果 | AI 的文字/程式碼輸出 |
| **人類介入** | 只寫 program.md，之後不介入 | 設計測試、校準 grader、分析失敗 |
| **可修改範圍** | 只能改 train.py | Skill 描述、prompt、rubric |
| **防作弊** | 鎖死 prepare.py | 鎖死 test cases + grading rubric |

### 核心差異

```
AutoResearch 的哲學：
  「只要有一個客觀指標 + 鎖死的評估環境，AI 可以無限自主迭代」

通用 Eval 的挑戰：
  「大部分 AI 任務沒有單一客觀指標，所以需要更複雜的評分體系」
```

---

## 6. 從 Karpathy 學到的 Grader 設計原則

### 原則 1：鎖死評估環境（最重要）

```
AutoResearch:  prepare.py 不可修改
你的 Eval:     test cases + grading rubric 版本鎖定，和被測 skill 分開存放
```

Agent 能改的東西越少，評估越可信。

### 原則 2：指標要能直接比較

```
AutoResearch:  val_bpb 跨架構可比（不依賴 tokenizer）
你的 Eval:     確保不同版本的 skill 在同一組 test cases 上評分
```

### 原則 3：自動化迴圈要能無限跑

```
AutoResearch:  改 code → 跑 5 分鐘 → 看結果 → 保留/丟棄 → 重複
你的 Eval:     改 skill → 跑 eval → 看分數 → 改進/回退 → 重複
```

### 原則 4：用 Git 當實驗記錄

```
AutoResearch:  每個改進 = 一個 commit，失敗 = git reset
你的 Eval:     每個 skill 版本 = 一個 commit，eval 結果存在 results.tsv
```

### 原則 5：極簡勝過複雜

整個系統 3 個檔案、~630 行。Karpathy 的名言：

> "Program the research org, not the code."
> — 人類寫方向（Markdown），AI 寫實作（Python）

---

## 7. 套用 AutoResearch 模式到 Skill Eval

### 適合直接套用的場景（有客觀指標）

```
Code generation:
├── 指標：test pass rate
├── 鎖死：test suite 不可修改
├── 迴圈：改 skill → 跑 tests → pass rate 提高就 commit
└── 完全可以無人值守

Bug fix:
├── 指標：FAIL_TO_PASS tests 通過 + PASS_TO_PASS 不退化
├── 鎖死：測試案例 + repo snapshot
├── 迴圈：同上
└── 這就是 SWE-Bench 的做法
```

### 需要擴展的場景（無單一客觀指標）

```
Customer support / 內容生成 / 摘要：
├── 沒有唯一正確答案
├── 需要 LLM judge（語調、完整性）
├── 需要 composite scoring（多維度加權）
├── 需要 human calibration（定期校準）
└── 不能完全無人值守
```

### 混合設計（推薦）

```python
def hybrid_grader(output, test_case):
    scores = {}

    # Karpathy 風格：能用 code 判斷的就不用 LLM
    scores["correctness"] = run_tests(output)           # binary, 像 val_bpb
    scores["format"]      = check_structure(output)     # binary, 像 prepare.py
    scores["no_pii"]      = check_no_pii(output)        # binary

    # 只在不得已時才用 LLM judge
    scores["tone"]        = llm_judge(output, rubric)   # Likert 1-5
    scores["completeness"]= llm_judge(output, rubric)   # Likert 1-5

    # 加權：code-based 佔大頭
    weights = {
        "correctness": 0.35,   # code-based
        "format": 0.15,        # code-based
        "no_pii": 0.15,        # code-based
        "tone": 0.15,          # LLM
        "completeness": 0.20   # LLM
    }
    # code-based 佔 65%, LLM 佔 35%

    return weighted_sum(scores, weights)
```

**原則：盡可能多的面向用 code-based（像 Karpathy），只在不得已時才用 LLM judge。**

---

## 8. Grader 設計 Best Practices 完整清單

### Rubric 設計

| 原則 | 說明 |
|------|------|
| **層次化** | 4-7 主軸 → 子維度 → 細粒度評分項 |
| **小整數量表** | 1-4 或 1-5，不要浮點數 |
| **每級有具體描述** | 不能只寫「好/中/差」 |
| **含 few-shot 範例** | 附帶已評分範例（比 zero-shot 可靠 20-30%） |
| **Reference answer** | 讓 grader 理解品質範圍的錨點 |

### LLM Judge 設定

| 設定 | 建議 |
|------|------|
| **Temperature** | 0.0 - 0.3（越確定性越好） |
| **Few-shot** | 至少 3 正面 + 3 負面範例 |
| **Chain-of-Thought** | Rubric 詳細時 CoT 效益遞減 |
| **Multi-Judge** | 多個 LLM 同時打分，majority vote |
| **Grader 模型** | 用便宜模型（Haiku）即可，除非任務複雜 |

### 可靠性校準

**Cohen's Kappa**（auto grader vs 人類一致性）：

```
< 0.40  差     → rubric 有嚴重問題
0.40-0.60  中等  → 需要改進
0.60-0.80  好    → 可以接受 ✓
> 0.80  優秀   → 接近人類水準 ✓✓
```

```python
from sklearn.metrics import cohen_kappa_score

human_scores = [5, 3, 4, 2, 5, 1, 4, 3, ...]   # 人類評分 30-50 筆
auto_scores  = [5, 4, 4, 2, 4, 1, 3, 3, ...]   # Auto grader 評分

kappa = cohen_kappa_score(human_scores, auto_scores)
# > 0.70 → grader 可信
# < 0.60 → 改 rubric
```

### Trajectory 評估（評過程不只評結果）

```
三個互補視角：

1. Final Response：結果錯了什麼？
2. Trajectory：在哪一步出錯？
3. Single Step：那一步為什麼錯？
```

### 進階架構（三代演進）

```
第一代：LLM-as-Judge（單個 LLM 直接打分）
  └─ 問題：不穩定、受 prompt 影響大

第二代：Agentic Judge — Auto-Eval Judge（Microsoft）
  └─ 比 LLM-as-Judge 高 4.76-10.52% 人類一致性
  └─ 做法：分解評估任務 → 逐步驗證 → 匯總

第三代：Agentic Rubric（Scale Labs）
  └─ Agent 先探索 context → 生成 rubric → 再評分
  └─ SWE-Bench 上 ROC-AUC = 0.886
```

---

## 9. 推薦開源框架

| 框架 | 特色 | 適合 |
|------|------|------|
| **Inspect-AI** | 100+ 內建 eval、sandbox、MCP 整合 | 嚴謹研究/安全團隊 |
| **Promptfoo** | CLI-first、YAML 設定、內建 red teaming | Terminal 開發者 |
| **Braintrust** | 端到端平台、UI 友善、golden dataset | 產品團隊 |
| **LangSmith** | LangChain 原生、trace multi-step agent | LangChain 使用者 |

---

## 10. 參考資料

### Karpathy AutoResearch
- [GitHub: karpathy/autoresearch](https://github.com/karpathy/autoresearch)
- [DataCamp: Guide to AutoResearch](https://www.datacamp.com/tutorial/guide-to-autoresearch)
- [Fortune: The Karpathy Loop — 700 experiments, 2 days](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/)
- [The New Stack: 630-line script ran 50 experiments overnight](https://thenewstack.io/karpathy-autonomous-experiment-loop/)

### Grader 設計
- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Microsoft: Auto-Eval Judge (arXiv 2508.05508)](https://arxiv.org/abs/2508.05508)
- [Scale Labs: Agentic Rubrics (arXiv 2601.04171)](https://arxiv.org/abs/2601.04171)
- [Confident AI: LLM-as-a-Judge Complete Guide](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
- [Monte Carlo: LLM-As-Judge 7 Best Practices](https://www.montecarlodata.com/blog-llm-as-judge/)

### Benchmarks
- [SWE-bench](https://www.swebench.com/SWE-bench/)
- [GAIA Benchmark (arXiv 2311.12983)](https://arxiv.org/abs/2311.12983)
- [BigCodeBench (arXiv 2406.15877)](https://arxiv.org/abs/2406.15877)

### 可靠性
- [Cohen's Kappa for AI Evaluation](https://galileo.ai/blog/cohens-kappa-metric)
- [LLM-as-Judge Design Choices & Reliability (arXiv 2506.13639)](https://arxiv.org/html/2506.13639v1)

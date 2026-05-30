# AutoResearch × XHS Generator — 實作方案

## 核心概念

把 Karpathy 的 AutoResearch loop 從「ML 訓練優化」改成「小紅書 Prompt 優化」：

```
原版：修改訓練代碼 → 跑 5 分鐘 → 比較 loss → 保留/丟棄
XHS版：變異 prompt → 生成內容 → LLM 評分 → 保留高分版本
```

一晚上自動跑 50-100 輪，找出最佳 prompt 組合。

---

## 要優化什麼？

你的 XHS workflow 有 4 個可以被 AutoResearch 優化的環節：

### 1. 標題生成 (最高優先)
- 現有：SKILL.md 裡有 5 種標題骨架 + 規則
- 優化空間：emoji 組合、字數、驅動詞位置、人名前置 vs 後置、問句 vs 陳述句
- 評分標準：CTR 預測分數（基於 account-dna 的歷史數據）

### 2. 正文結構 (高優先)
- 現有：3 模塊結構（鉤子 → 解釋 → 互動收口）
- 優化空間：鉤子的寫法、反問句位置、數字密度、段落長度
- 評分標準：可讀性 + 互動潛力 + 知識增量

### 3. 選題打分權重 (中優先)
- 現有：6 維度固定權重（新鮮度 25、匹配度 20、知識增量 20…）
- 優化空間：自動調整權重組合，看哪組最能預測高互動
- 評分標準：和歷史高互動帖的相關性

### 4. 圖片 Prompt (低優先，但有趣)
- 現有：封面先行、統一視覺系統
- 優化空間：風格描述詞、構圖指令、色彩方案
- 評分標準：需要 Vision model 評分

---

## 系統架構

```
xhs_autoresearch/
├── program.md            # 指導 AI agent 的實驗指南（類似 Karpathy 的 program.md）
├── run.py                # 主循環：變異 → 生成 → 評估 → 記錄
├── mutator.py            # Prompt 變異器：隨機修改 prompt 的某個部分
├── generator.py          # 呼叫 LLM 生成 XHS 內容
├── evaluator.py          # 多維度評分器
├── config.py             # API keys、模型選擇、實驗參數
├── templates/            # Prompt 模板（被 mutator 修改的對象）
│   ├── title_prompt.md   # 標題生成 prompt
│   ├── body_prompt.md    # 正文生成 prompt
│   └── angle_prompt.md   # 選題角度 prompt
├── baselines/            # 目前最佳版本（benchmark）
│   └── best_title_prompt.md
├── experiments/          # 每輪實驗記錄
│   └── exp_001/
│       ├── mutation.json # 這輪改了什麼
│       ├── output.md     # 生成的內容
│       └── scores.json   # 評分結果
└── results/
    ├── leaderboard.json  # 所有實驗的排名
    └── insights.md       # 自動生成的發現摘要
```

---

## 核心模組設計

### 1. mutator.py — Prompt 變異器

每輪隨機選一個變異策略：

```python
MUTATION_STRATEGIES = [
    "swap_emoji",           # 換 emoji 組合
    "reorder_structure",    # 調整模塊順序
    "adjust_tone",          # 更口語 / 更專業 / 更挑釁
    "change_hook_style",    # 換開場鉤子風格（反問/數字/衝突/懸念）
    "modify_cta",           # 換互動收口方式
    "tweak_title_formula",  # 調整標題骨架
    "add_constraint",       # 加入新約束（如：必須提到錢）
    "remove_constraint",    # 移除某個約束
    "inject_reference",     # 注入高互動帖的元素
    "crossover",            # 從兩個高分 prompt 各取一半
]
```

每次只改一件事（single variable），才能知道什麼真的有效。

### 2. evaluator.py — 多維度評分器

用 LLM-as-judge，針對 Dindin 帳號特性設計評分維度：

```python
EVAL_DIMENSIONS = {
    "ctr_prediction": {
        "weight": 30,
        "prompt": "基於以下帳號歷史數據和小紅書平台特性，預測這個標題的點擊率...",
        "reference": "account-dna.md 的高互動標題"
    },
    "knowledge_density": {
        "weight": 20,
        "prompt": "這篇內容的知識增量有多少？讀者看完能學到什麼新東西？"
    },
    "audience_resonance": {
        "weight": 20,
        "prompt": "對不懂這項運動的中文讀者，這個內容有多容易引起共鳴？"
    },
    "comment_potential": {
        "weight": 15,
        "prompt": "這篇內容有多大機會引發評論區討論（站隊、補充、反駁）？"
    },
    "visual_storytelling": {
        "weight": 15,
        "prompt": "四張圖的故事線是否連貫？是否形成一套視覺系統？"
    },
}
# 總分 100，低於 80 丟棄（和 SKILL.md 的選題門檻一致）
```

### 3. run.py — 主循環

```python
def run_experiment_loop(topic: str, rounds: int = 50):
    """
    AutoResearch main loop for XHS content optimization.

    Each round:
    1. Load current best prompt
    2. Apply one random mutation
    3. Generate XHS content with mutated prompt
    4. Score with multi-dimensional evaluator
    5. If score > current best → keep mutation, update baseline
    6. Log everything
    """
    baseline = load_baseline()
    baseline_score = evaluate(generate(topic, baseline))

    for i in range(rounds):
        # Mutate
        mutated = mutate(baseline, strategy=random_strategy())

        # Generate
        content = generate(topic, mutated)

        # Evaluate
        score = evaluate(content)

        # Compare
        if score > baseline_score:
            save_as_new_baseline(mutated, score)
            baseline = mutated
            baseline_score = score
            log(f"[IMPROVED] Round {i}: {score} (was {baseline_score})")
        else:
            log(f"[REJECTED] Round {i}: {score} < {baseline_score}")

        # Save experiment record
        save_experiment(i, mutated, content, score)

    generate_insights_report()
```

---

## 實驗流程（具體怎麼跑）

### Phase 1：標題優化（先做這個）

**Input**：一個體育熱點話題（如「Caitlin Clark WNBA 第二季」）
**Baseline**：用現有 SKILL.md 的標題規則生成 5 個標題
**Loop**：
1. 變異標題 prompt（換骨架 / 換 emoji / 換驅動詞 / 調字數）
2. 生成 5 個標題
3. LLM 評分：CTR 預測 + 帳號匹配度 + 問題驅動力
4. 最高分 > baseline → 更新

**預期成果**：50 輪後找到比 baseline 高 15-25% 分數的標題 prompt

### Phase 2：正文結構優化

**Input**：Phase 1 選出的最佳標題 + 話題
**Baseline**：現有 3 模塊結構
**Loop**：
1. 變異正文 prompt（鉤子風格 / CTA / 段落數 / 語氣）
2. 生成完整正文
3. LLM 評分：可讀性 + 互動潛力 + 知識增量
4. 最高分 > baseline → 更新

### Phase 3：端到端優化

同時跑標題 + 正文 + 圖片方案，做整體評分。

---

## 成本估算

| 項目 | 計算 | 成本 |
|------|------|------|
| 每輪生成 | ~2000 tokens (input + output) | ~$0.01 |
| 每輪評分 | ~3000 tokens (5 維度) | ~$0.015 |
| 50 輪實驗 | 50 × $0.025 | ~$1.25 |
| 100 輪實驗 | 100 × $0.025 | ~$2.50 |

用 Claude Sonnet 或 GPT-4o-mini 跑評分可以更便宜。一晚上 $2-3 找到最佳 prompt 組合。

---

## 和現有專案的整合

```
Side_project/
├── xhs_skills/                    # 現有 skill（不動）
│   └── skills/xhs-sports-hot-knowledge/
│       ├── SKILL.md               # ← AutoResearch 優化後的結果回寫到這裡
│       └── references/account-dna.md  # ← 評分時引用
├── rednote_analysis/              # 現有分析資料（不動）
│   ├── style_guide.md             # ← 評分時引用
│   └── viral_content_methodology.md  # ← 評分時引用
└── xhs_autoresearch/              # 新增：AutoResearch 引擎
    └── ...
```

優化完的 prompt 直接回寫到 SKILL.md，下次用 skill 生成內容時自動使用優化後的版本。

---

## 第一步：MVP 實作範圍

最小可行版本只需要 3 個檔案：

1. **run.py** — 主循環（50 行）
2. **mutator.py** — 標題 prompt 變異（30 行）
3. **evaluator.py** — LLM 評分（40 行）

加上一個 `templates/title_prompt.md` 作為 baseline。

預估 2-3 小時可以跑起來第一輪實驗。

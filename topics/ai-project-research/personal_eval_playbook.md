# 個人 Eval Playbook：核心方法 + 你的客製化路徑

> 寫於 2026-05-10
> 範圍：(1) 業界最高密度 best practice 蒸餾 (2) 對應你過往實戰經驗的具體建議

---

## Part 1：個人 eval 的核心（從 Hamel / Shreya / Eugene Yan 蒸餾）

### 一句話總結

**Eval 的核心不是工具或指標，而是「Error Analysis」這個動作。** 你 60-80% 的時間應該在「自己讀 output、分類失敗、寫 critique」，不是在搭框架或調 metric。

### 七條共識（這三個人講的話有 90% 重疊，都指向同一件事）

**1. 從錯誤分析（error analysis）開始，不是從框架開始。**
打開 notebook，翻 20-50 個 output，手動寫「為什麼這個不對」。重複到看不出新失敗類型為止（業界叫 theoretical saturation，大概要看 100 條 trace）。

**2. 一個 domain expert 拍板，不要委員會。**
個人開發者就是你自己。Hamel 把這個角色稱作「benevolent dictator」——一個人說了算，比五個人投票快得多。

**3. 評分用二元 Pass/Fail，不要 1-5 分。**
1-5 分讓你逃避思考（「我給 3 分」= 沒回答任何問題）。Pass/Fail 強迫你說「這條線到底在哪」。Likert 分數還需要更大樣本才看得出改善。

**4. 必寫「critique」（為什麼判定這個結果），不只 verdict。**
這是 Hamel 的核心 trick。寫 critique 的過程強迫你 articulate 標準。後來這些 critique 變成 LLM judge 的 few-shot example，prompt 直接抄你寫的東西。

**5. 評分方式優先序：程式 > LLM-as-judge > 人類。**
能 if/else 解決就別呼叫 LLM。LLM-as-judge 要 100+ 標註樣本和持續維運，只給「會反覆迭代的問題」用，不給「改一次 prompt 就好」的問題用。

**6. 平衡正負樣本，目標 50:50。**
只測 happy path 等於沒測。要包含「該做有做」+「不該做沒做」。

**7. Eval 是流動的，不是一次性產物。**
每週看 10-20 條 outlier trace，每 2-4 週做一次完整 error analysis（100+ 條），加新題進 eval set，砍已飽和的舊題。

### 個人的最小可行 setup

```
工具：一個 Jupyter notebook + git
Eval set：evals/cases.jsonl（30 個起步）
Grader：80% 程式碼判斷 + 20% LLM judge（對「好不好讀」「有沒有 hook」這種主觀的）
頻率：改 prompt 前後各跑一次，看 diff 不只看總分
```

業界共識是：**自己用 AI coding assistant 寫一個 domain-specific 的 annotation tool，比用 DeepEval/Braintrust 這種 generic 工具快 10 倍**——因為它能把你的內容渲染成你習慣看的樣子（小紅書貼文就渲染成貼文，code 就 syntax highlight）。

### 反模式（很多人踩的坑）

- 用 off-the-shelf 通用 metric（"helpfulness"、"coherence"）——掩蓋你產品真正的問題
- 還沒讀資料就先寫 evaluator
- 用 1-5 Likert 而非 binary
- 把 error analysis 外包出去（會切斷你的直覺成長 loop）
- 為「想像中可能發生」的失敗寫 eval，而非真實失敗
- LLM judge 沒跟人類校準就上（位置偏誤、verbosity 偏誤可達 15-40%）

---

## Part 2：你的實戰經驗盤點（你已經做了什麼）

掃過你的子專案後，發現你**其實已經在做業界推崇的 eval 流程**，只是名字不叫 eval。

### 你做得已經很好的部分

| 專案 | 你已經做的 | 對應業界 best practice |
|---|---|---|
| `xhs_autoresearch/title` | 605+ 輪 A/B、4 phase、acceptance rate 當 metric | 大規模 iteration loop，等於 Hamel 講的 hill-climbing |
| `xhs_autoresearch/cover_image` | 30 輪、53% 改善率、發現「減法策略全失敗」這種反直覺 finding | error analysis 找到 systematic failure mode |
| `xhs_content_generator/video_prompt_optimization_log.md` | 每輪只改一個變數、Before/After + 判定 + 理由 | **完美實踐** Hamel/Shreya 的 critique-then-verdict |
| `news_analysis/cross_verify.py` | 用第二個 LLM 驗證第一個 | LLM-as-judge 雛形 |
| `info_collector/feedback.py + preference_analyzer.py` | 從 Gmail 收 reply、分析使用者偏好 | 線上 feedback loop（業界叫 production telemetry → eval set 的閉環） |
| `eval-skill` | 已建構 token-cost + quality A/B 框架 | 量化的 cost/quality trade-off eval |

**結論：你不缺 eval intuition，你缺的是把這些散在各處的東西收成統一方法論。**

### 你目前的缺口（建設性指出）

1. **單篇 video_prompt 的 critique 寫得很好，但這套 discipline 沒擴散到所有 LLM 應用。** stock dashboard、news_analysis 的 prompt 改動沒留 critique log。

2. **沒有「pre-publish rubric」→「post-publish 反饋」的閉環。** 你有 `xhs-publish-review` skill 做事後 review，但事前的判斷標準（標題夠不夠 hook？故事線通不通？）沒形式化成 checklist 跑進 CI。

3. **acceptance rate 是好的 metric，但 acceptance 是「你自己」拍板。** 沒明確記錄為什麼接受/拒絕（critique 不夠詳細的話，LLM 學不到）。

4. **缺少「holdout set」的概念。** xhs_autoresearch 跑 605 輪是好事，但每輪都用同樣題目你會 overfit 到那批題目；要保留一批沒看過的題目當 final test。

5. **沒有跨應用統一的 eval 檔案結構。** 每個專案各搞各的。如果統一成 `<project>/evals/cases.jsonl + grader.py`，工具可以重用、未來上 DeepEval/Braintrust 也容易遷移。

---

## Part 3：你的客製化 eval 路線圖

### 你的場景優先序（依重要性 + 已投入時間）

| 場景 | 為何重要 | 適合的 eval 類型 |
|---|---|---|
| 1. 小紅書內容生成（標題/封面/正文） | 主力場景、已重投資、有真實外部 feedback | **rubric eval + 線上互動數 feedback loop** |
| 2. info_collector 摘要 | 你每天會看、品質直接影響你工作流 | **個人偏好 LLM judge**（你自己當 expert） |
| 3. news_analysis 事實正確性 | 錯了會被誤導 | **規則式 eval（事實 cross-verify） + LLM judge** |
| 4. stock dashboard 解讀 | 涉及金錢、錯了風險高 | **保守 rubric + 人工 review，不 auto-ship** |
| 5. AI project research（這個資料夾） | 你正在做的事 | 太個人化、case 太少，不用寫 eval |

### 場景 1：小紅書內容生成（最該系統化的）

你已經有 video_prompt_optimization_log.md 的好底子，建議擴張到全 pipeline。

**結構建議**（建議在 `xhs_autoresearch/evals/` 下統一）：

```
xhs_autoresearch/evals/
├── cases/
│   ├── titles.jsonl          # 30-50 個標題 case，含 expected hook / 數字 / 字數
│   ├── covers.jsonl          # 20-30 個封面 case，含品牌調性檢查
│   └── bodies.jsonl          # 20-30 個正文 case
├── graders/
│   ├── code_checks.py        # 程式可判斷的：字數、含數字、含 emoji
│   └── llm_judge.py          # LLM 判斷的：hook 強度、故事性
├── critiques/
│   └── 2026-W19/             # 每週存 critique log
└── runs/
    └── 2026-05-10_v3.jsonl   # 每次跑的結果
```

**標題 grader 範例（直接抄你已經發現的規律）**：

```python
# code_checks.py — 你已經在 v3 finding 裡發現的硬規則
def grade_title(title: str) -> dict:
    return {
        "length_18_20": 18 <= len(title) <= 20,           # 你發現的硬邊界
        "has_number": bool(re.search(r"\d", title)),       # 數字不可移除
        "has_contrast_hook": any(  # 對比鉤子 83% 勝率
            p in title for p in ["你以為", "其實", "看似", "結果"]
        ),
        "no_likert_garbage": title.count("！") <= 1,
    }
```

LLM judge 用來補程式碼測不到的：「這標題夠 street-smart 嗎？」「有沒有 explain-too-much 感？」——把你已經寫過的 critique 當 few-shot example 餵給 judge。

**Pre-publish rubric**（每篇發文前跑一次）：
- [ ] 標題 4 個 hard rule（長度、數字、hook、感嘆號）全 pass
- [ ] 封面通過品牌調性 LLM judge（≥0.8）
- [ ] 6 slide 結構完整（Hook/Problem/Process/Reveal/Twist/Answer）
- [ ] 至少 2 個 fact_pack 引用源

**Post-publish 反饋**（發 24h 後 / 7 天後）：
- 收互動數（讚 / 收藏 / 留言）
- 凡是表現遠高於 / 遠低於預期的，加進 eval cases 並寫 critique
- 每月一次 error analysis：跑過去 30 篇，找系統性失敗

### 場景 2：info_collector 摘要

你有 `feedback.py` 從 Gmail 讀 reply。把這條路徑強化成 eval loop：

```python
# 加進 feedback.py 的後續處理
# 把每封回覆解析成 (article_id, like/dislike, reason)
# 累積 100 條後，等於你免費取得 100 個標註樣本
# 直接餵給 LLM judge 做 alignment：
#   給 judge 看 article + summary，看它能不能預測你會 like/dislike
```

當 judge 跟你的 agreement >85%，就可以自動篩你會喜歡的文章，不再需要每篇看。

### 場景 3：news_analysis 事實正確性

你有 cross_verify.py 已經在做，建議補一個 **eval set**：50 個歷史 case，已知正確答案，每次改 prompt 都跑一次回歸。重點：包含「該 cross-verify 結果是 disagree」的負樣本，不然你只在測 happy path。

### 場景 4 - stock dashboard

LLM 給的金融解讀有錯不能 auto-ship。建議：

- 不要急著 eval LLM 的「對錯」（很難）
- 改 eval「LLM 有沒有亂掰數字」（faithfulness 類，類似 RAGAS 的 faithfulness）：把每個數字 claim 抽出來，去原始資料 grep，找不到就標 fail
- 50 個歷史 case 做 regression set

### 跨應用統一 convention（建議）

在每個 LLM-using 專案根目錄都加：

```
<project>/
├── evals/
│   ├── cases.jsonl           # 不管什麼結構，至少有這個檔
│   ├── grade.py              # 跑一次的 entry point
│   └── critiques/            # markdown 寫每次重大改動的 critique
└── CHANGELOG_PROMPTS.md      # 每次 prompt 改動 + critique + 跑出的分數變化
```

不需要框架。`cases.jsonl + grade.py` 兩個檔，你已經贏 90% 個人專案。

---

## 接下來一週的具體 action（建議）

如果你想立刻開始，按這個順序最有效率：

**Day 1（30 分鐘）**：在 `xhs_autoresearch/evals/cases/titles.jsonl` 寫 30 個標題 case，每個標 pass/fail + 一句 critique。優先抓你最近一個月覺得「這個發出去效果差」的 5-10 個當負樣本。

**Day 2（1 小時）**：寫 `code_checks.py`，把你 v3 finding 變成程式碼 hard rule。跑一次 baseline——多少 % 通過所有 hard rule？

**Day 3（1 小時）**：寫 `llm_judge.py`，prompt 裡塞 5 條你最強的 critique（你已經寫好的，從 video_prompt_optimization_log.md 抄）當 few-shot。對 30 case 跑一次，跟你自己的判斷比 agreement。

**Day 4（30 分鐘）**：把這個 eval 接到 `xhs_autoresearch` 的 prompt iteration loop 上。下次改 prompt 前後各跑一次。

**Day 5+**：擴張到封面、正文、然後其他專案。每個專案都走「30 case + code_checks + llm_judge」三件套。

---

## 給你的核心提醒

1. **你的 video_prompt_optimization_log.md 是世界級的 eval 實踐**——只是沒人告訴你那個叫 eval。把那個 discipline 當成 SOP，套到所有 LLM 應用。

2. **你的優勢是「你會反覆迭代同一個 LLM 應用」**（小紅書那 605 輪就是證據）。這正是業界說「值得花力氣建 eval 的場景」——對單次任務不該寫 eval，但對你會迭代 100+ 次的應用，eval ROI 極高。

3. **不要碰 DeepEval / Braintrust 這類框架，至少前 3 個月不要**。你已經在用 markdown 做 critique log，這就是最好的 annotation tool。等你有 200+ case、3 個專案都在跑、開始覺得 markdown 撈不動了，再考慮升級。

4. **eval 不是給別人交差用的，是讓你自己改 prompt 時不再憑感覺**。當你 2026/08 回來看 5 月寫的 prompt，能說「上次改 v3 → v4 是因為 case 17 fail，現在 v4 → v5 應該抓 case 23」——這就是 eval 的真正價值。

---

## 相關資源

### 必讀（按優先序）
1. [Hamel & Shreya — LLM Evals: Everything You Need to Know](https://hamel.dev/blog/posts/evals-faq/) — 業界目前最完整的 FAQ
2. [Hamel — Using LLM-as-a-Judge For Evaluation](https://hamel.dev/blog/posts/llm-judge/) — critique-then-verdict 在這
3. [Eugene Yan — An LLM-as-Judge Won't Save The Product](https://eugeneyan.com/writing/eval-process/) — 為什麼 process > tool
4. [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

### 視角補充
- [Pragmatic Engineer — A pragmatic guide to LLM evals](https://newsletter.pragmaticengineer.com/p/evals)
- [Eugene Yan — Task-Specific LLM Evals that Do & Don't Work](https://eugeneyan.com/writing/evals/)
- [Eugene Yan — Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/)

### 想看課程才考慮
- [Maven — AI Evals For Engineers & PMs (Hamel & Shreya)](https://maven.com/parlance-labs/evals)

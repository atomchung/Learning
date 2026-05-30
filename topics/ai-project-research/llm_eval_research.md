# LLM Eval 與 Benchmark 設計 研究筆記

> 研究時間：2026-05-10
> 範圍：(1) 各領域主流 benchmark 設計手法 (2) 個人 / 小團隊應用層 eval 的有效設計

## 一句話總結

公開 benchmark 用來「選模型」，自己的 eval 用來「迭代產品」——前者你看排行榜就好，後者必須自己動手寫，因為它就是你產品 spec 的可執行版本。

## 核心概念

1. **Benchmark ≠ Eval**：Benchmark 是給研究社群用的「全行業考卷」（MMLU、SWE-bench 等），eval 是你自己對應用的回歸測試。前者飽和不代表後者就 OK。
2. **Saturation 問題**：HumanEval、MMLU、MMLU-Pro、GPQA 都已飽和到 90%+，前沿模型差距已小於統計噪音；2026 還能分辨頂尖模型的只剩 HLE（top 約 46%）、SWE-bench Pro、LiveCodeBench Pro 等。
3. **Contamination（資料污染）**：早期 benchmark 題目進了訓練集，分數虛高。LiveCodeBench 用「持續滾動更新題目」對抗這點；HumanEval 是反例。
4. **Reward Hacking**：2026/04 Berkeley RDI 公告顯示 8 大主流 agent benchmark 全部可被刷分技巧攻破——所以任何單一分數都該打折，配第三方獨立評分 + 自己的 held-out set。
5. **Eval 三大評分方式**：(a) 程式碼判斷（exact match / unit test）、(b) LLM-as-judge、(c) 人類標註。優先順序就是這個。

## 公開 benchmark 速覽（按領域）

### 知識與推理

| Benchmark | 設計手法 | 2026 狀態 | 何時看 |
|---|---|---|---|
| MMLU | 57 學科多選題，4 選 1 | 已飽和（90%+） | 只當入場資格 |
| MMLU-Pro | 加大難度、10 選 1、加推理題 | 接近飽和 | 中低階模型仍可分辨 |
| GPQA Diamond | 博士級理化生選擇題，Google 也答不出 | 接近飽和（92%+） | 中階模型還有空間 |
| HLE（Humanity's Last Exam） | 全球專家出題 3000+，跨 100+ 領域，刻意難 | 仍未飽和（~46%） | 唯一還能拉開頂尖模型的知識題 |
| AIME 2025 | 30 題奧林匹克數學短答 | 仍是頂級模型主要區分點 | 看數學/推理深度 |

### 程式碼

| Benchmark | 設計手法 | 何時看 |
|---|---|---|
| HumanEval | 164 題 Python，給 docstring 補 function body | 已死，僅供歷史對照 |
| LiveCodeBench (Pro) | 從 LeetCode/AtCoder/Codeforces 持續抓 cutoff 之後的新題，避污染；Pro 版用 Elo 評分 | 看純演算法能力 |
| SWE-bench Verified | 真實 GitHub issue + repo，要 patch 過 test | 看「能不能改現成 codebase」 |
| SWE-bench Pro | Verified 的更難版 | 2026 主流 agent coding 評分 |
| Terminal-Bench | 給 shell 任務看 agent 能不能搞定 | 看 CLI agent |
| SciCode | 科學計算程式 | 看科研場景 |

### Agent / Tool use

| Benchmark | 設計手法 | 何時看 |
|---|---|---|
| GAIA | 450 題真實助理任務（含搜尋、檔案、多模態），有 unambiguous 答案 | 通用 assistant |
| TAU-bench / tau2-bench | 模擬零售、航空、語音、檢索場景，LLM 扮演真實使用者，要遵守 policy 文件——「訂對機票但違反退票規則」算失敗 | 看企業 agent，最貼近真實部署 |
| AgentBench | 8 個環境（OS shell、SQL、KG、卡牌、家務、購物、瀏覽、卡牌） | 看廣度 |
| WebArena | 真實網站環境的 web 任務 | 看 browsing agent |
| BFCL（Berkeley Function-Calling Leaderboard） | tool-calling 各種子任務 | 看 tool use 細節 |

### RAG

RAGAS 提供四個核心指標，**不需要 ground-truth label** 就能跑（這是它流行的關鍵）：

- **Faithfulness**：回答的每個 claim 能不能在 retrieved context 找到支持（抓幻覺）
- **Answer Relevancy**：回答有沒有正面回應問題（抓「答非所問但很真實」）
- **Context Precision**：retrieved chunk 中真正相關的比例（抓召回品質）
- **Context Recall**：相關內容被 retrieve 到的比例（需要 ground truth）

## 個人 / 小團隊 eval 設計：可執行 SOP

這是這份筆記最有價值的部分。綜合 Anthropic、OpenAI、Pragmatic Engineer 的指引整理。

### 第一階段：從零起步（第 1 週可完成）

```
Step 1. 收集 20-50 個真實 case
        - 不要憑空想，從這幾個地方挖：
          * 你自己手動測試 prompt 時的 case
          * 用戶投訴 / bug 回報
          * 你「直覺覺得會出錯」的 edge case
        - 每個 case 寫成 (input, expected_output_or_criteria) 的格式

Step 2. 對每個 case 寫「兩個專家會給同樣 pass/fail 判斷」的標準
        - 模糊的標準（"回答要好"）→ 沒用
        - 明確的標準（"回答必須包含日期且格式為 YYYY-MM-DD"）→ 有用

Step 3. 平衡正負樣本
        - 不要只測「該做時有做」，也要測「不該做時沒做」
        - 例：搜尋 agent 不只測「該搜尋有去搜」，也要測「不該搜尋時別亂搜」

Step 4. 選評分方式（優先順序）
        a. 能用程式碼判斷就用（exact match、regex、JSON schema、unit test）
        b. 不行才用 LLM-as-judge
        c. 真的測不了的（創意、語感）才用人類

Step 5. 跑 baseline，記錄分數
        - 第一次跑得 60% 不可怕，可怕的是不知道是 60%
```

**關鍵原則**：「imperfect evals deployed early outperform perfect evals delayed」——不完美但今天能跑的 eval，比完美但下個月才寫好的有用。

### 第二階段：每次改 prompt / 換模型都跑（持續優化期）

把 eval 套進你的 PR / change 流程：

```python
# pseudo-code; tool-agnostic
for case in eval_set:
    actual = run_my_app(case.input)
    score = grade(case.expected, actual)
    record(case.id, score, actual)

assert overall_pass_rate >= last_known_baseline  # gate
```

每次改：
1. 在改之前先跑一次（記錄當前分數）
2. 改完再跑（看有沒有 regression）
3. 看 **diff**，不只看總分——95% → 95% 也可能是 case A 變對 case B 變錯

### 第三階段：擴張 eval set（成熟期）

- 每收到一個生產環境的 bug 回報 → 加進 eval set
- 每隔幾週看 transcript：模型在哪些 case 系統性錯
- 監控 saturation：當 eval 分數 100% 表示 eval 太簡單，要加新題

### LLM-as-judge：用對的方式

LLM-as-judge 便宜快但有偏誤，要這樣防：

| 偏誤 | 機制 | 修正 |
|---|---|---|
| Position bias | 比較兩個答案時偏第一個（GPT-4 約 40% 不一致） | A/B 都跑兩次互換位置，取一致才算 |
| Verbosity bias | 偏好長答案（約 +15% 灌水） | rubric 直接加「簡潔度」項 + 對過長答案扣分 |
| Self-enhancement | 偏好自己家模型（+5-7%） | 換不同家當 judge，或多 judge 投票 |
| Fallacy oversight | 看不出邏輯謬誤 | 結構化 rubric 拆維度評分，每維度單獨判 |

實務技巧：
- 用 **PASS/FAIL 二元判斷** 比 **1-10 分** 穩定多了
- 給 judge **「Unknown」逃生口**——資訊不足就不要硬猜
- judge prompt 裡只給 transcript 和 retrieved context，**不要讓 judge 用自己的知識評分**（會幻覺）
- 定期用人工抽 20-30 個樣本校準 judge，看 judge 跟人類同意率

## 工具選擇對照（2026/05 現況）

| 工具 | 定位 | 優點 | 缺點 | 何時用 |
|---|---|---|---|---|
| **Promptfoo** | CLI + YAML 配置 | 50+ red-team 模板，本地跑 | 2026/03 被 OpenAI 收購（86M），社群擔心廠商獨立性 | 安全/紅隊測試首選 |
| **DeepEval** | Python pytest 框架 | 50+ 內建 metrics（G-Eval、hallucination、faithfulness 等），跟 pytest CI 整合 | 偏 Python 生態 | CI/CD gating 首選 |
| **Braintrust** | SaaS 平台 | 線上 trace、人類標註、PM 跟工程師共用界面 | 商業產品 | 團隊協作 + 線上監控 |
| **LangSmith** | LangChain 系平台 | LangGraph 整合最深、step-level 評分、400 天 trace | 跟 LangChain 綁很深 | 用 LangGraph 的 agent |
| **RAGAS** | RAG 專用 | 不需 ground truth、4 個現成指標 | 只 cover RAG | RAG 專案標配 |

**2026 業界共識組合**：
- 個人 / 早期：DeepEval 或 Promptfoo 單兵作戰，本地跑就好
- 工程團隊：**DeepEval（CI gating）+ Braintrust（線上 trace + 標註）** 已成事實標準

## 常見 pitfall（自己踩過 / 看別人踩過的）

1. **過度依賴公開 benchmark 分數**：Claude/GPT 在 SWE-bench 80% 不代表在你的 codebase 80%
2. **Eval set 太小且不平衡**：只有 5 個 case，且都是 happy path
3. **Grader 過於 rigid**：要求 agent 走特定步驟，懲罰了「走不同路但結果對」的解
4. **環境沒隔離**：上一個 case 留下的檔案污染下一個 case
5. **改 prompt 不跑 eval**：靠手動測 1-2 個 case 拍腦袋
6. **LLM judge 沒校準就上**：判斷標準漂移，自己還不知道
7. **混淆 capability eval 和 regression eval**：前者要難（pass rate 低才有空間爬），後者要穩（接近 100%）

## 適用場景

| 你在做什麼 | 該怎麼處理 eval |
|---|---|
| 寫單次 script / 一次性任務 | 不用寫 eval，肉眼看就好 |
| Prompt 會被改超過 3 次 | 至少寫 10-20 個 case，手動跑 |
| 上 production / 有外部用戶 | 必須有 CI eval gating + 線上 trace |
| RAG 應用 | RAGAS 四指標 + 自己領域題 |
| Agent / tool use | 至少測「該呼叫 tool」+「不該呼叫 tool」兩種 case |
| 純客服 chat | 模仿 TAU-bench 思路：寫 policy 文件 + 模擬真實用戶 |

## 給個人開發者的最小路徑

如果你只想花一個下午搞個 eval，不要追求完整：

1. 開個 `evals/cases.jsonl`，丟 20 個 (input, expected) 進去
2. 寫個 50 行的 Python script：跑模型、比對、印分數
3. 改 prompt 前後各跑一次，看 diff
4. 加進 git，每次 commit 前跑

這樣你已經贏過 80% 沒做 eval 的個人專案了。等到 case 累到 100+、跑得太慢、或要分享給隊友看，再考慮 DeepEval / Braintrust。

## 相關資源

### 必讀
- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — 8 步驟 SOP，本份筆記主要參考
- [OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Pragmatic Engineer — A pragmatic guide to LLM evals](https://newsletter.pragmaticengineer.com/p/evals)

### Benchmark 排行榜
- [BenchLM — State of LLM Benchmarks 2026](https://benchlm.ai/blog/posts/state-of-llm-benchmarks-2026) — 第三方獨立評分，比官方數字可信
- [HAL Princeton — GAIA Leaderboard](https://hal.cs.princeton.edu/gaia)
- [Awesome Agents — Agent Leaderboard](https://awesomeagents.ai/leaderboards/agentic-ai-benchmarks-leaderboard/)
- [LiveCodeBench](https://livecodebench.github.io/)

### 工具文件
- [DeepEval GitHub](https://github.com/confident-ai/deepeval)
- [RAGAS Docs](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)
- [Braintrust 替代方案比較](https://www.braintrust.dev/articles/best-promptfoo-alternatives-2026)

### Benchmark reliability 的警鐘
- [Berkeley RDI — How We Broke Top AI Agent Benchmarks](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/) — 為什麼不能信任單一分數
- [Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://llm-judge-bias.github.io/)

### 進階閱讀
- [Galileo — Agent Evaluation Framework 2026](https://galileo.ai/blog/agent-evaluation-framework-metrics-rubrics-benchmarks)
- [Confident AI — RAG Evaluation Metrics](https://www.confident-ai.com/blog/rag-evaluation-metrics-answer-relevancy-faithfulness-and-more)

---

**TL;DR**：別跟著公開 benchmark 起舞——它們半年飽和一次又被 reward hack。對個人應用，下午寫 20 個 case + 50 行 script 就能甩開大多數憑感覺改 prompt 的人。LLM-as-judge 用就用，但要校準、防偏誤、優先用程式判斷。

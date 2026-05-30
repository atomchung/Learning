# Eval Playbook 補充：Outcome Metric、投資場景、四個尖銳問題

> 補充於 2026-05-10
> 對應對話中四個問題的深度回答

---

## Q1：cross_verify.py 是什麼？（順便更正前一份筆記的錯誤）

**我前一份 playbook 說 cross_verify.py 是「LLM-as-judge 雛形」——這是錯的，更正一下。**

讀完原始碼後，cross_verify.py 其實是：

**多新聞源交叉驗證引擎**（沒有 LLM 參與）

```
給一個 URL → sanitize 出搜尋關鍵字 → 打 Bing News RSS →
拿回前 4 個其他新聞源的報導 → aggregate 成 evidence list
```

它跟 LLM-as-judge 的差別：
| | cross_verify.py | LLM-as-judge |
|---|---|---|
| 判斷者 | 多個獨立新聞源 | LLM |
| 輸出 | evidence aggregation | pass/fail + critique |
| 適合 | 事實正確性（有沒有別人報） | 主觀品質（好不好讀） |

更精確地分類：cross_verify.py 是「**外部證據檢索版的 faithfulness check**」——類似 RAGAS faithfulness 但證據來源是即時新聞而非 retrieved context。

**它在你的 eval 體系裡能扮演什麼角色**：當 news_analysis 的 LLM 摘要說了某個 claim，你可以拿這個 claim 去 cross_verify，沒被其他源報過 → 標 fail。這就是程式式 grader，不是 LLM judge。

---

## Q2：xhs_autoresearch 跑很多輪但小紅書真實指標沒漲——為什麼？

**這是個經典 eval 設計病：你的 proxy metric 沒跟 north star metric 對齊。**

### 診斷

從 `title_autoresearch_summary.md` 看到三個明確訊號：

1. **R10 那次「用戶因『繞口』選了系統判輸的 B」**——這已經是警鐘，意思是 **LLM judge 的判斷跟你（真人）的判斷不一致**。
2. **接受率 10%**（後 16 輪全拒）——這不是「你逼近最優」的證據，是「你的 mutator 在某個你沒意識到的維度上 stuck 了」。
3. **沒有任何一個 metric 是「小紅書平台真實互動數」**——所有 acceptance 都是 LLM 或你自己 judge 的，平台演算法 + 真實讀者沒參與評分。

### 病灶圖

```
你的 eval 學的東西：「ting 心目中的好標題」
                       ↓
                  ↗ 這兩件事
                  ↘ 沒有任何 mechanism 對齊過
                       ↑
小紅書平台給你的：「演算法 + 真實使用者點擊的標題」
```

**所有 605 輪 / 20 輪 / 35% 接受率，都是在最佳化第一條路。第二條路才是 north star，但你的 eval 沒看它。**

### 三個具體成因

**成因 A：你既是「prompt 的設計者」又是「judge 的訓練者」**

當你寫 mutator（生成新標題候選）和 evaluator（打分）時，兩邊的「直覺」是同一個人。所以你的 evaluator 會偏好「ting-shaped」標題——但 ting 不是讀者。

**成因 B：沒有 outcome metric 進 loop**

理論上應該是：
```
發 100 篇 → 收 24h/7d 互動數 → 算每篇的 outcome score
        → 把 outcome 高/低的標題進 eval set 當 ground truth
        → 每月校準 LLM judge：它能不能 predict outcome？
        → judge 的 predict accuracy < 70% 就重訓
```

你目前缺最後三步。

**成因 C：題目太集中（overfitting）**

Curry 傷停 20 輪、SGA MVP cover、Pistons body 多輪——同一個題目跑 25 輪，你 mutator 在學「這題用什麼標題好」，不是學「通用標題策略」。

### 驗證假設的方法（這週可做）

抓你過去發過的 30 篇實際小紅書貼文，整理成 jsonl：

```jsonl
{"title": "誰是NBA最貴的膝蓋？...", "likes": 1234, "saves": 89, "comments": 12, "views": 50000}
{"title": "...", "likes": 23, "saves": 1, "comments": 0, "views": 800}
```

然後：
1. 分高表現組（top 30%）vs 低表現組（bottom 30%）
2. 用你現在的 LLM judge 對每篇打 acceptance score
3. **算 correlation**：judge 分數 vs 真實互動

如果 correlation < 0.3，那 605 輪實驗的結論有 70% 是噪音。
如果 correlation > 0.5，judge 還算準，問題在別的地方。

我猜會是前者。

### 修法

**核心修正：把 outcome metric 接進 loop。**

```
xhs_autoresearch/evals/
├── outcome_data/
│   └── posts_2026_q1.jsonl       # 真實發文 + 互動數
├── ground_truth/
│   ├── high_performers.jsonl     # top 30% 標題
│   └── low_performers.jsonl      # bottom 30%
├── judge_calibration/
│   └── 2026-05-10_results.md     # judge 對 high/low 的 separation 能力
└── new_runs/
    └── ...                        # 改 prompt 後跑 eval，但 eval set 是真實 high/low
```

然後 **judge 的 alignment target 變成：「能不能區分真實的 high 和 low performer」**，不再是「合不合 ting 口味」。

**短期變通**：如果你嫌沒 100 篇真實數據，至少把幾個你「發了之後表現超出預期」的、和「本來看好結果撲街」的標題各 5-10 個拉出來，當 ground truth golden set。每次改 prompt，跑這 20 個 case，看 judge 給的分跟真實表現的 spearman correlation 有沒有改善。

---

## Q3：投資和其他應用怎麼設計 eval？

關鍵認知：**不同應用的 eval 結構天差地別，因為 feedback loop 長度差三個數量級。**

| 應用 | 一次任務週期 | 真實 outcome 多久知道 | Eval 適合的形態 |
|---|---|---|---|
| 小紅書內容 | 30 分鐘 | 24h-7d | 跑得起 LLM judge + outcome loop |
| info_collector 摘要 | 10 秒 | 你當天就讀完 | LLM judge + 你的 read/skip 行為 |
| news_analysis 摘要 | 1 分鐘 | 立刻可 cross-verify | 程式式 fact check 為主 |
| 投資 thesis | 1 小時寫 | 6 個月 ~ 3 年 | **不該做 LLM eval，要做 decision journal** |
| 投資 AI 分析（財報摘要等） | 2 分鐘 | 同上但摘要本身可立刻 eval | 程式式事實檢查 + faithfulness |

### 投資場景：要區分兩個 eval 對象

**對象 A：AI 工具的「品質 eval」**（你 stock 子專案的 Gemini agent 做的事）
- 財報摘要 → 有沒有亂掰數字（faithfulness check：每個數字 grep 原始 10-K，找不到 = fail）
- 新聞摘要 → 有沒有遺漏關鍵風險點（事先列 5-10 個 must-mention 項目，缺項 = fail）
- 競爭者比較 → 提到的數據能不能在 source 找到
- **這類 eval 完全可以做，套小紅書那套 case + grader 框架**

**對象 B：投資決策本身的 eval**（這才是真正重要的）
- 不要用 LLM 來 eval，**用 decision journal**
- 結構：

```markdown
# {DATE}_{TICKER} Decision Journal

## Pre-Trade（必填，commit 之前）
- 進場理由（thesis 摘要）：__
- 我相信什麼（3 條 belief）：__
- 哪些訊號會讓我認錯（kill criteria）：__
- 預期持有時間：__
- 預期報酬率：__
- 我有多確定（1-10）：__
- 情緒狀態（FOMO / 焦慮 / 冷靜）：__

## Outcome（持倉結束後填）
- 實際結果：__
- 跟 thesis 是否一致：__
- 如果結果不一致，是因為 (a) thesis 錯 (b) 執行錯 (c) 運氣：__
- 下次同樣 setup 我會怎麼做：__
```

**Eval 變成：每季度回顧 decision journal，計算「pre-trade 確定度 vs 實際 hit rate」校準曲線**——你說 9 分確信的 trade，實際 hit 多少 %？這叫 calibration eval，跟天氣預報員那套一樣。

這比看 P&L 重要得多——因為 P&L 受運氣影響大，但 calibration 反映你判斷品質。

**personal_os 已經規劃了 Reviews/weekly|monthly|quarterly——你已經有架子，只是沒填 calibration metric。**

### 其他應用

**info_collector**（你已經有 feedback.py + preference_analyzer）：
- North star：你**真的會讀**的文章比例
- 直接 instrument：每篇推薦記 `read_time_seconds`，>30 秒算 read，<5 秒算 skip
- LLM judge alignment target：predict read vs skip
- 累積 200 條後就有非常好的個人化 eval set

**news_analysis** 摘要：
- 已有 cross_verify 做事實層
- 補一個 LLM judge 做「資訊密度」（同樣字數有沒有更多資訊）
- 但不要做「好不好讀」這種 fluffy metric——沒 outcome 對齊

**stock dashboard 的 AI agent**：
- 不要 eval「analysis 對不對」（短期不可知）
- 只 eval「analysis 有沒有亂掰、有沒有漏點」
- 範例 case：餵某季財報，標準答案列 6 個必須提到的點（YoY 營收、毛利率變化、guidance、回購、主要 risk、management commentary 異常處）。LLM 漏 1 個扣 X 分

### 共通原則：找你的 north star metric

每個 LLM 應用都要先回答：

> 「這個應用如果做得好，**從外部世界**看會發生什麼事？」

- 小紅書內容 → 真實互動數（不是 ting 接受率）
- info_collector → 你真的會讀（不是 LLM judge 評分）
- 投資 AI 工具 → 沒漏關鍵點 + 沒亂掰（不是「報告寫得漂亮」）
- 投資決策 → calibration（不是 P&L）

**Eval 的最終目的是 predict north star。任何 metric 不能 predict north star，就是浪費**——這是 605 輪沒漲的根本教訓。

---

## Q4：整體建議（這個月的具體動作）

按 ROI 排序，從最重要做起：

### Week 1：立刻做的事（高 ROI）

**動作 1（30 分鐘）：xhs 真實數據盤點**
找 30 篇你過去發的小紅書，把標題 + 24h 互動數整理成 jsonl。沒有就從你帳號後台撈。**沒有真實數據，後面所有 xhs eval 都建在沙上。**

**動作 2（1 小時）：判斷 judge 真的有用嗎**
拿這 30 篇，跑你現在的 LLM judge，算 spearman correlation。`<0.3` → judge 重設計；`>0.5` → judge 可保留。

**動作 3（30 分鐘）：寫每個應用的 north star**
在每個專案根目錄加 `EVAL_NORTH_STAR.md`，一句話：

```
xhs: 真實 24h 互動率（讚+收藏+留言）/ views > 5%
info_collector: 推薦的文章我 30 秒以上停留率 > 60%
news_analysis: 摘要中數字 claim 100% 在原文找得到
stock/agent: 財報摘要漏點率 < 10%（vs 6 點 checklist）
投資決策: 季度 calibration error < 15%
```

這個動作看起來廢，其實是最關鍵的——你之前所有 eval 沒對齊，就是因為這個沒寫下來。

### Week 2-3：建第一個閉環

選一個應用建完整 outcome loop。**建議從 info_collector 開始**，因為 feedback 最快、你天天會用：

```python
# info_collector 改造
1. email_sender 發出時記錄 article_id + summary_text
2. 加 instrument：使用者點開 article 的時間 / 跳出時間
3. 累積 100 條 (article, my_read_time)
4. 訓 / 校準 LLM judge：給 article + summary，predict read_time
5. judge 上線後，新 article 進來先過 judge，分高的優先排序
```

一個禮拜內就能跑通，是個漂亮的 reference implementation。

### Month 1：擴張到 xhs 和投資

xhs：把 outcome loop 接上，judge 重訓。

投資：
- 在 personal_os 的 Trades/journal 加 pre-trade 模板（上面那個）
- 開始累積 decision journal（不需要立刻分析，先有資料）
- 三個月後第一次回顧 calibration

### 不要做的事

- **不要再多跑 xhs_autoresearch 輪數**：在 outcome loop 修好之前，再跑 600 輪也只是 overfit ting 的口味
- **不要為投資 thesis 建 LLM-as-judge**：feedback 太久、噪音太大，不適用
- **不要急著上 DeepEval/Braintrust**：你還沒到那個階段
- **不要把 ai_project_research 這個資料夾本身做 eval**：個人探索不是迭代產品

---

## TL;DR（你問的四題）

1. **cross_verify.py** 不是 LLM-as-judge，是多源新聞 cross-check（事實性檢查）；前一份 playbook 寫錯了，已更正。

2. **xhs 跑很多但指標沒漲** 的根因：你的 LLM judge 學「ting 口味」，不學「真實平台 outcome」，兩條軌道從沒交叉過。修法：抓 30 篇真實互動數據算 correlation，把 outcome 進 loop。

3. **投資 eval** 要分兩層：AI 工具品質（faithfulness、漏點率，可做） vs 投資決策（用 decision journal + calibration，不要用 LLM eval）。其他應用按 feedback loop 長度設計。

4. **這月最該做**：給每個應用寫 north star metric → info_collector 起一個完整閉環當 reference → 然後才修 xhs。**不要再多跑實驗輪數**，先把 north star 對齊。

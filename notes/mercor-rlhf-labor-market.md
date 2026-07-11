# Mercor:RLHF 專家勞動市場

2026-07-11,隨口問答沉澱。

## 這公司是什麼

招募有證照的白領專家(醫生、律師、顧問、PhD)做 RLHF/eval/資料標註,賣給前沿 AI lab,抽仲介費。本質是「Upwork for RLHF」,但高門檻篩選 + 自建工作流工具(rubric 設計、evaluation framework),不只是媒合。

**客戶**:公開證實 OpenAI、Anthropic 合作,自稱前五大 AI lab + Magnificent Seven 六家都是客戶。

**規模**(2026-07):
- 3 萬名 weekly-active 承包商(30 萬人才池篩出),每天付出 $200 萬+
- 2026-06 年化 GMV 破 $20 億,4 個月內翻倍
- 估值:2025-10 是 $100 億 → 2026-07-09 在談 $200 億

**付費行情**:平均 $85/hr;entry-level $12-25/hr;domain expert(醫生/律師/PhD)$75-200+/hr;senior domain expert 最高 $200+/hr(約當年薪 $40 萬)。

## 關鍵修正:GMV ≠ revenue

$20 億是流過平台的總金額,承包商拿走 60-70%,Mercor 自己的 take-rate revenue 大概 $6-8 億量級。估值 $200 億 vs 淨營收 $6-8 億,~25-30x revenue multiple——典型 AI 榮景期 marketplace 估值法,不是保守數字。這是套用自己「讀信號不讀表面數字」判準的實例:表面數字($20 億)比實際訊號(take-rate revenue)誇大 3 倍以上。

## 投資啟發(三點)

1. **Mercor 是「外圍供應鏈層」的新實例,不是核心動作**——呼應既有卡片 `topics/ai-industry-reading/cards/llm-call-niches-are-features-not-companies.md`(核心動作/一次 LLM call 撐不成公司,可投資表達式在外圍三件套)。Mercor 是訓練資料供應鏈這層外圍,目前規模看撐得起獨立大公司,可補進該卡當新案例。

2. **證偽訊號:labs 會不會把 RLHF/eval 收回自建**——OpenAI/Anthropic 都在招募自己的全職 domain expert 團隊,如果內部化加速,Mercor 的 take-rate 會被擠壓。跟「商品化計時器」判準同構(外包→內化是常見軌跡,像早期雲端運算外包後來大廠自建)。→ 待觀察:labs 財報/招募動態是否顯示 RLHF 外包占比下降。

3. **目前沒有散戶能直接曝險的標的**——Mercor 私募,一般投資人碰不到。間接曝險路徑:持有 Meta(持 Scale AI 49%,同賽道競品)、或觀察這塊支出對 OpenAI/Anthropic 燒錢結構的影響(財報揭露 RLHF 外包成本占比上升,是「AI 訓練成本結構」訊號,不是「該買 Mercor」訊號,因為根本買不到)。

## 技術機制:labs 具體在「learn」什麼

專家勞動對應三種訓練訊號:
- **Reward model 訊號**:專家對模型輸出做 pairwise 排序,餵去訓練 reward model,再用 RLHF 調整模型行為
- **Rubric/verifier**:專家寫評分標準,變成訓練迴圈裡自動判斷「這次生成算不算對」的機制——呼應既有判斷「eval 瓶頸是寫判準不是工具」(`topics/coding-agents/cards/eval-bottleneck-is-criteria-not-tooling.md`),labs 買的不是勞力,是判準本身
- **示範資料**:高技能專家親自示範解法,直接當 SFT(監督微調)材料

## 對「白領失業警訊」判斷的修正

原本直覺:frontier lab 進軍 vertical AI workflow 市場,白領要失業了。修正後更精確:

- 這不是舊式 crowdsourced labeling(標低技能重複任務),是「一次性販售專業判斷(tacit judgment)的壓縮」——買一次、理論上可無限複製
- Mercor 是供應鏈中間層,vertical AI 公司(Harvey/Anterior 這類)是下游產品,frontier lab 沒有「自己下場」,是整條供應鏈在推進
- **但自動化速度有煞車**:既有判斷「judge 在專業領域穩定套用+對齊人類的相關係數崩到 <0.3」——壓縮專業判斷比壓縮「這句話對不對」難得多。窄任務(特定合約條款、特定影像判讀)先被吃,整個職業判斷短期不會。風險是任務層被切走的速度,不是職業一次性消失
- 諷刺點:被威脅的那群人正靠賣「會讓自己被自動化」的資料賺外快,且是知情自願(跟被 scrape 訓練不同)——這是「有限窗口套利」,不代表判斷錯誤

## 出處

- [TechCrunch: How AI labs use Mercor](https://techcrunch.com/2025/10/29/how-ai-labs-use-mercor-to-get-the-data-companies-wont-share/)
- [The Information: Mercor $2B gross annualized revenue](https://www.theinformation.com/briefings/exclusive-mercor-hit-2-billion-gross-annualized-revenue)
- [TechCrunch: Mercor $20B valuation talks (2026-07-09)](https://techcrunch.com/2026/07/09/mercor-is-in-talks-for-a-20b-valuation/)
- [TechCrunch: Mercor $10B valuation Series C (2025-10-27)](https://techcrunch.com/2025/10/27/mercor-quintuples-valuation-to-10b-with-350m-series-c/)
- 對話:2026-07-11

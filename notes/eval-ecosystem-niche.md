# Eval 的生態位:模型廠為什麼把 eval 推出自家門外

> 研究時間:2026-06-04
> 觸發:ihower 在 Threads 提到「OpenAI 三月收購 promptfoo,還把自家 Evals 後台收掉、叫大家遷過去」
> 角色定位:這份只談 **生態位/卡位**。怎麼寫 eval、工具怎麼選,在 [llm_eval_research.md](../topics/ai-project-research/llm_eval_research.md) 已經講透,不重複。

## 一句話

eval 的天然形狀是「**跨模型的裁判層**」,結構上就該活在任何單一模型廠之外;OpenAI 收掉自家 Evals 後台、把用戶導去 promptfoo,等於模型廠親口承認這件事。真正被買走的不是「eval」,是 eval 底下長出來的**兩個更值錢的東西:agent 安全紅隊 + 企業分發通路**。

## 這則新聞的事實層

- 2026-03-09 OpenAI 宣布收購 promptfoo(開源 eval / 紅隊 CLI 工具)。
- 同時 OpenAI 把自家 dashboard 的 Evals 功能收掉,提供匯出,官方 cookbook 直接寫〈Moving from OpenAI Evals to Promptfoo〉叫大家遷移。
- promptfoo 數字:35 萬+ 開發者用過、13 萬 MAU、Fortune 500 有 25% 在用。2025-07 剛拿 Insight 領投的 18.4M A 輪。
- 承諾:**維持開源、維持 model-agnostic**,繼續支援各家模型;技術併入 OpenAI Frontier(企業 agent 平台)做原生的安全測試/紅隊。

## 為什麼「模型廠自己做 eval」結構上是矛盾的

這是整件事的核心。eval 的用途是**比較、挑選模型**——你寫 eval 就是為了知道「換到哪家、哪版會不會變好/變壞」。所以它天生要站在所有模型**上面**,保持中立。

模型廠自己出 eval 產品,踩到兩個結構性問題:

1. **自我偏好(self-preference bias)**:LLM 當裁判會偏袒自家輸出,而且越強的模型越明顯。OpenAI 的 eval 後台天然有「讓 GPT 看起來最好」的動機,企業不會信。
2. **冗餘**:eval 要 model-agnostic 才有用,但模型廠沒動機去把對手模型支援好。一個只想留住你的廠,做不出真正中立的比較器。

所以 OpenAI 收掉自家 Evals 後台不是退守,是**認清 eval 不屬於模型產品本身**——它屬於上面那層獨立工具。這跟 [harness-beats-model](../topics/coding-agents/cards/harness-beats-model.md) 同源:價值正在從「模型」滲到「模型周邊的判斷/測量/編排層」。

## 那為什麼還要花錢買下「中立工具」?

表面看是矛盾:既然 eval 該中立、不該歸模型廠,OpenAI 幹嘛買?拆開看,被買的根本不是「eval 這個功能」,是它底下兩樣東西:

**1. Agent 安全紅隊(真正的成長向量)**
promptfoo 的賣點這兩年已經從「測 prompt 品質」漂移到「**測 agent 會不會出事**」:prompt injection、jailbreak、資料外洩、工具誤用、越權行為。OpenAI 的官方說法是「strengthen agentic security testing」,不是 eval。
→ 隨著 agent 真的被部署,eval 這個生態位**分岔成兩半**:
- **正確性 eval**(輸出好不好)——正在商品化,一堆開源工具(DeepEval、RAGAS)在打。
- **安全/紅隊 eval**(agent 會不會做壞事)——企業有預算、有合規壓力、防禦性需求,這塊才是錢在的地方。
OpenAI 要的是後者,塞進 Frontier 當原生能力。

**2. 企業分發通路**
13 萬 MAU、Fortune 500 25% 滲透。eval 工具坐在一個關鍵位置:**企業「決定要不要換模型 / 換哪家」的那個決策點**。誰擁有那層,誰就站在每一次模型採購決策的旁邊。這是通路價值,跟工具本身的程式碼無關。

## 為什麼「維持開源 + model-agnostic」是這筆收購的命門

OpenAI 必須承諾 promptfoo 繼續中立、繼續支援對手模型——因為**一旦它變成「只對 GPT 友善」,上面說的通路價值當場歸零**。企業用 eval 就是要中立比較,你把它變偏心,大家立刻換工具(Braintrust、DeepEval 在旁邊等)。

所以這裡有個張力值得追蹤(這是訊號,不是結論):
- OpenAI 有動機讓它保持中立(維持分發 + 信任)。
- 但長期也有動機讓 GPT 在裡面「順一點」(lock-in)。
- 社群已經在擔心廠商獨立性。**這層中立能維持多久,是後續觀察點。**

## 生態位地圖:這層現在誰站哪

**模型廠自有(正在收斂/退場)**
- OpenAI Evals 後台 → 收掉,導去 promptfoo
- promptfoo 本身 → 被 OpenAI 收(但保持開源中立)
- Google / Anthropic 各有自家 eval,同樣有中立性疑慮

**獨立開源 CLI(商品化中)**
- DeepEval(pytest 系)、RAGAS(RAG 專用)——免費、本地跑、好接 CI

**獨立 SaaS 平台(中立性是賣點)**
- Braintrust:promptfoo 被收後,**最大的獨立全生命週期贏家**,中立 + 沙箱自訂 scorer
- LangSmith:跟 LangChain 綁死,中立性差一點

收斂的模式很清楚:**模型廠收購中立層拿分發 + 安全,獨立 SaaS 靠「我不是模型廠」當差異化。**

## 接到你既有的判斷

- **讀信號不讀數字**([卡](../topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md)):這則的信號不是「promptfoo 勝出」,是「**模型廠承認 eval 必須住在模型外面**」。表面數字(86M 收購價、13 萬 MAU)是噪音,結構轉向才是訊號。
- **開源商品化計時器**:正確性 eval 正在被開源商品化(DeepEval/RAGAS 免費打到底);但**紅隊/安全 eval + 企業分發**沒被商品化,所以錢往那兩塊跑。計時器對「工具」響了,對「通路 + 安全」還沒。
- **harness > model**:eval 是 harness 層的一部分,不是模型的一部分。這筆收購是同一個判斷的產業級證據。

## 對你(個人 / 小團隊)的實際意涵

1. **工具選擇不變**:你要寫自己的 eval,promptfoo 被收不影響——還是開源、還能本地跑。真要避廠商風險,Braintrust / DeepEval 在旁邊。
2. **別把「模型廠的 eval 後台」當中立基準**:結構上它有自我偏好。要中立比較就用第三方。
3. **真正值錢的技能在分岔的安全那邊**:如果想做 AI 專案的差異化,「agent 會不會做壞事」的紅隊 eval,比「輸出品質回歸測試」更稀缺、更有企業預算。

## 一句話 TL;DR

OpenAI 把自家 eval 後台關掉、改推 promptfoo,是模型廠承認 eval 是「跨模型的裁判層」、不該住在模型產品裡;而它真正買走的是 agent 安全紅隊 + 13 萬 MAU 的企業分發通路。eval 這個生態位正在分岔:**正確性測量在商品化,安全紅隊在升值**。中立性能撐多久,是這層的下一個觀察點。

## 附:目前怎麼測 agent 能力(具體流程,2026-06-04 補)

測 agent 跟測單次 prompt 是兩回事:agent 多步、會用工具、有「走過的路徑(trajectory)」,**不能只看最後答案對不對**。

**分三個層次看同一個 case**
1. **End-state(結果)**:任務最後有沒有達成?看終態。
2. **Trajectory(軌跡)**:叫了哪些工具、順序、有沒有繞路、失敗有沒有自我修復。
3. **Component(零件)**:壞在哪一步。

**核心原則:以 end-state 為主評分**。因為殊途同歸——多條工具路徑可能都正確完成同一目標,不該逼 agent 走你預設那條。trajectory 拿來**診斷失敗**和抓「答案矇對但過程錯」。

**具體 pipeline**
1. **準備 task(不是 prompt)**:`(goal, 初始環境狀態, 終態成功判準, 該/不該用的工具)`。正負樣本都要。
2. **跑 agent + 開 tracing**:記整條軌跡(planner 決策、tool call 名+參數+回傳、memory、token、耗時)。這是跟 prompt eval 最大的工程差別。
3. **三類評分**:
   - 結果類(主秤,優先 code 斷言):`assert db.order.status == "refunded"`、檔案/schema 對、回覆含必要事實。
   - 軌跡類(診斷):工具選對沒、參數對沒、有無多餘步、有無 recover。一條 50 步軌跡整條塞給 judge 是「一次」call。
   - 效率類:token、時間、tool call 次數。
4. **LLM-as-judge 餵四樣**:rubric、任務描述、完整軌跡、可選參考答案 → 回 PASS/FAIL + critique。防偏誤照舊;agent eval 標配 **3 judge majority vote**(軌跡長、單判噪音大)。
5. **看 diff 進 CI**:改 prompt/換模型/加工具前後各跑,看哪些 case 翻轉;每晚 regression report;production bug 回灌成新 case。

**公開 agent benchmark 就是「別人備好的 case + 終態判準」**:SWE-bench(patch 過 test)、TAU-bench(訂對票且不違反 policy)、GAIA/WebArena(有 unambiguous 終態)——全是 end-state 評分,反證上面原則。

### 個人也能搞對(判斷)

能,而且 **agent eval 對個人特別友善**。理由:最難、最花錢的部分是「收集真實 case + 寫出兩個專家會同意的判準」——這是**理解問題,不是工程問題**,不能外包、不能買工具解決,而個人對自己的小場景理解最深。工程那塊(tracing、平台、多 judge 投票)是規模到了才需要的。

**個人最小版本(一個下午)**:
1. `tasks.jsonl`:10-20 個 `(goal, 初始狀態, 終態斷言)`。
2. 50 行 script 跑 agent,**把完整 tool-call log 存下來**。
3. 終態能 assert 的用 code;不能的丟單 judge 給 PASS/FAIL。
4. 印兩個數:**成功率 + 平均 tool call 數**(抓繞路)。
5. 改前/改後各跑,看 diff,進 git。

**個人會撞到的牆(誠實)**:case 攢得慢(把日常使用當 case 工廠)、judge 會漂要偶爾人工校準、多 judge 投票是 3 倍 token(可先單 judge,只在不信任的 case 補投票)。**案例破百 / 跑太慢 / 要共看 trace / 要線上監控**才上 Braintrust/LangSmith,之前都不用。

## 來源

- [OpenAI — OpenAI to acquire Promptfoo](https://openai.com/index/openai-to-acquire-promptfoo/)
- [Promptfoo — Promptfoo is joining OpenAI](https://www.promptfoo.dev/blog/promptfoo-joining-openai/)
- [Futurum — OpenAI Acquires Promptfoo, 25% Fortune 500 foothold](https://futurumgroup.com/insights/openai-acquires-promptfoo-gaining-25-foothold-in-fortune-500-enterprises/)
- [DEV — Top 5 AI Agent Eval Tools After Promptfoo's Exit](https://dev.to/thedailyagent/top-5-ai-agent-eval-tools-after-promptfoos-exit-576i)
- [Braintrust — Best Promptfoo alternatives in 2026](https://www.braintrust.dev/articles/best-promptfoo-alternatives-2026)
- [arXiv — Risks of LLM Evaluation by Private Data Curators](https://arxiv.org/pdf/2503.04756)(裁判中立性 / 利益衝突)
- ihower Threads 原 po(觸發來源)
- [Confident AI — LLM Agent Evaluation Guide](https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide)(agent eval 流程)
- [Adaline — Complete Guide to AI Agent Evaluation 2026](https://www.adaline.ai/blog/complete-guide-llm-ai-agent-evaluation-2026)
- [Vector Institute — Agentic AI evaluation strategies](https://vectorinstitute.ai/agentic-ai-evaluation-strategies/)
</content>
</invoke>

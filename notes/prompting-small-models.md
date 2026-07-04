# 聰明模型怎麼幫小模型設計任務指引(prompting for small models)

2026-07-04 隨口疑問:怎麼讓聰明模型設計任務指引給小模型?小模型聰明程度不一,best practice 是什麼?

**一句話**:槓桿有三個——委派契約寫滿四要素、約束強度隨目標模型能力調(guardrail 會變 handcuff)、以及別手寫改用強模型對著 eval 自動演化指引。措辭本身不是槓桿。

## 1. 委派契約四要素(Anthropic 多 agent 系統實戰)

Anthropic 的 Research 系統(Opus lead + Sonnet subagents,勝單一 Opus 90.2%)踩過的坑:給子 agent 的指令只寫「research the semiconductor shortage」→ 子 agent 誤解任務、或彼此做重複搜尋。

修正後,每個交給小模型的任務**必須包含**:

1. **objective**:目標是什麼、做到什麼算完成
2. **output format**:輸出長什麼樣(schema、欄位、長度)
3. **工具與來源指引**:用哪些工具、看哪些來源
4. **任務邊界**:什麼不要做、跟其他子任務的分界

缺任何一項小模型就會 drift——不是模型笨,是 orchestrator 沒講清楚「done 長什麼樣」。

## 2. effort scaling 明寫進指引

小模型不會自己判斷「這任務值得花多少力氣」,強模型要替它決定並明寫:Anthropic 的 prompt 直接嵌規則——簡單事實查找 1 個 agent、直接對比 2–4 個、複雜研究 10+ 個。原則:**effort 判斷留在強模型側,不留給小模型現場發揮**。

## 3. 約束強度隨能力調:Prompting Inversion(回答「小模型也分聰明程度」)

arXiv 2510.22251 的發現,直接回答這題的第二半:

- **低能力模型**:中度受益於約束(給結構、給步驟、給 few-shot)
- **中能力模型**:約束收益**最大**——規則當 guardrail 擋掉常識錯誤(gpt-4o 上約束式 prompt 97% vs 一般 CoT 93%)
- **高能力模型**:同一套規則變 **handcuff**——誘發過度字面化、新增錯誤(gpt-5 上 94.0% vs 更簡單 prompt 的 96.4%,反轉)

作者稱之為 guardrail-to-handcuff transition。含義:**沒有一份通吃的指引**,指引必須跟目標模型能力共演(co-evolve)——越弱給越多結構、schema、範例;越強給目標和自由度,把規則拿掉。強模型設計指引時,第一個輸入參數是「目標模型多聰明」。

## 4. 手寫的上限:用 eval 自動優化(DSPy GEPA)

業界收斂中的最佳實踐是**別靠人手寫**:把強模型設成 optimizer(GEPA 的 `reflection_lm`),它看小模型在你的 eval set 上的失敗軌跡、用自然語言反思錯在哪、改寫指引、再測,沿 Pareto 前沿演化。DSPy 官方明說:優化小模型時 reflection_lm 用大模型——它更會推理和寫 prompt,且只呼叫少數幾次成本無虞。

效果宣稱:優化後的小模型「更快、更便宜、且贏過未優化的 frontier model」。

這把問題還原成既有判斷:[eval-bottleneck-is-criteria-not-tooling](../topics/coding-agents/cards/eval-bottleneck-is-criteria-not-tooling.md)——你真正要準備的是 **eval set + 判準 metric**,不是 prompt 措辭;措辭交給機器演化。

## 5. 邊界:指引救不了的,換路由

cascade / routing 文獻共識:ambiguous、planning-heavy 的任務不要 over-prompt 弱模型硬撐,直接升級給強模型。指引優化和路由是互補的兩根槓桿——先判斷任務該不該給小模型,再談指引怎麼寫。

## 接既有線

- **harness>model**:同構——決定小模型表現的是外圍設計(契約、eval、路由),不是換措辭。
- **orchestration 兩層共存**(Fugu 線):編排下沉進模型後,強模型寫委派契約=編排能力的具體形態。
- **inbox 2026-07-04 Lucas Smedley**:「多數人只換模型不調 config」——effort/routing 是省錢槓桿,本篇是它的 prompt 面。

## 坑

- arxiv.org / anthropic.com / bytebytego 全被環境白名單 403,細節是搜尋摘要交叉拼出;Prompting Inversion 的數字(97/93、94.0/96.4)引用前值得手機開原文核一次。
- Prompting Inversion 是單一作者、以 gpt-4o/gpt-5 為主的實驗,「三段式」分界別當普適定律,當方向感用。

## 出處

- [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)(四要素、effort scaling、90.2%)
- [You Don't Need Prompt Engineering Anymore: The Prompting Inversion (arXiv 2510.22251)](https://arxiv.org/abs/2510.22251)
- [DSPy: GEPA optimization](https://dspy.ai/getting-started/gepa-optimization/)、[DSPy: Choosing an optimizer](https://dspy.ai/diving-deeper/choosing-an-optimizer/)
- [HF Cookbook: Prompt Optimization with DSPy GEPA](https://huggingface.co/learn/cookbook/dspy_gepa)
- cascade/routing:[LLM Cascades with Mixture of Thoughts (arXiv 2310.03094)](https://arxiv.org/pdf/2310.03094)、[OpenAI Prompt guidance](https://developers.openai.com/api/docs/guides/prompt-guidance)

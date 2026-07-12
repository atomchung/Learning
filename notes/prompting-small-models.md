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

## 6. 架構案例:daily-brief pipeline(把四條放到位置上)

場景:每日 AI 產業訊號日報(對應 info-intake 流程)。三層分工:

1. **Orchestrator=強模型**(每天 1 次):讀 profile/預測帳,拆任務卡、決定開幾個 worker、寫最終判斷。
2. **Extraction workers=最便宜小模型**(每篇 1 次,量大=成本大頭):單篇抽結構化事實。
3. **Synthesis worker=中間模型**(1–3 次):跨文章找信號、對照預測帳,不下最終判斷。

**任務卡(runtime,四要素齊)**——orchestrator 每篇動態生成:

```yaml
objective: 抽出可驗證的事實宣稱;完成定義=每欄有值或明確 null
output_format: JSON schema(claim/number/is_measured/source_quote)
tools_and_sources: 只用給你的全文,禁止用自己的知識補數字
boundaries: 不下判斷、不跨文章比較;不確定填 "ESCALATE" 別猜
```

缺一項的後果:缺 objective 交半成品、缺 format 下游解析不了、缺 sources 限制會幻覺補數字、缺 boundaries 越權或重工。

**prompt 檔跟模型綁定,不共用**(Prompting Inversion 的落地):

```
prompts/extract@haiku.md    # 弱:schema+2 few-shot+禁止清單+逐步程序
prompts/extract@sonnet.md   # 中:同 objective/boundaries,砍程序和 few-shot
```

弱模型版的逐步程序是 guardrail;同一套給中模型會誘發過度字面化(例:「列出所有數字」連頁碼都列)。換模型=換 prompt 檔重過 eval,不沿用。

**effort 規則寫死在 orchestrator prompt**:≤3 篇自己做、4–10 篇開 1 個 synthesis、>10 篇按主題切 2–4 個。小模型不參與 effort 決策。

**escalation 通道(機械規則)**:worker 回 ESCALATE 或 schema 驗證連敗 2 次 → 升級給中模型;synthesis 遇到跟預測帳衝突的信號 → 標 needs-judgment 丟回 orchestrator。

**離線 eval 迴圈(GEPA-lite)**:golden set 20 篇手標文章+欄位級 F1/is_measured 判對率;每週強模型讀失敗軌跡改寫 extract@haiku.md,過門檻才上線。人只維護 golden set 和 metric,不改措辭。

**關鍵洞**:指引有兩個生成時機——runtime(任務卡,管當次資訊)和 offline(prompt 檔演化,管怎麼教會這級模型)。多數人只做 runtime 手寫一份通吃,品質和錢都漏在 offline 層沒建——同 Lucas Smedley「只換模型不調 config」的洞。

## 7. 首次實測(2026-07-04,縮小版跑通)

實際跑了一輪:Fable 當 orchestrator、5 個 Haiku extraction worker(任務卡=四要素+few-shot+逐步程序+ESCALATE)、1 個 Sonnet synthesis worker(砍程序砍 few-shot,只給目標+schema+邊界)。材料用搜尋摘要代替全文(白名單限制)。

**驗證成功的**:
- ESCALATE 通道:A4 只有標題沒內文,Haiku 正確拒抽並說明理由,沒硬編。
- is_measured 判別:Haiku 大致分得開「公告事實 vs 預測」。
- Sonnet 給自由度的設計:它主動做了跨 item 交叉(coding stack 三家共用 MCP 攻擊面)、dedup、每個信號標 needs_judgment 不越權下判斷——中模型少約束確實表現更好。

**實測抓到的改進點(按嚴重度)**:
1. **時效缺陷最致命**:抽回來的 Micron capex $13.5B 其實是 2025-11 TrendForce 預測,不是當天新聞。任務卡 schema 沒有 published_date 欄,worker 無從判斷、orchestrator 收料時也沒過濾。→ 修法:收料階段先標日期,任務卡加 freshness 欄。
2. **schema 缺 claim_type**:「預測」和「純意見」(如某工具是最強選項)都被壓進 is_measured=false,語意混掉。→ 加 fact/forecast/opinion 三值,或指示 skip opinions。
3. **真實 miss 一個**:A1 把「emphasis shifting」標成 measured,但原句掛在 anticipated 底下=預測。這種從句歸屬就是該進 golden set 的 edge case。
4. **輸出衛生**:A2 的 number 欄出現 `&gt;` HTML 轉義殘留。→ prompt 加一句或下游後處理。
5. **token 浪費**:每張任務卡重複 few-shot+程序(~600 tokens×5)。→ 共用部分放 prompt 檔(system),任務卡只放當次資訊——架構裡本來就分兩層,偷懶合併立刻付代價。
6. **上游去重**:價格 jump 同時出現在兩篇材料,synthesis 雖然接住了,但 extraction tokens 已浪費。→ orchestrator 切 item 時先粗去重。

**成本**:extraction 5×約 25k tokens(Haiku)+synthesis 42k(Sonnet),判斷全留在 orchestrator。結構上貴的推理只跑了兩次(開頭拆卡、結尾判斷)。

## 8. 改前 vs 改後 A/B(2026-07-04,同批材料、同組模型、只換 task card v1→v2)

v2 對三個致命點動手:加 `as_of_date`、`claim_type`(fact/forecast/opinion)取代 is_measured 二元、把 anticipated 從句 miss 寫成 few-shot。

**修掉的(prompt 就搞定,5/6)**:
- 時效:整篇掛 as_of_date;那個 $13.5B capex 一眼看出是 2025-11 預測。
- claim_type 三值:opinion(某工具最強、eval 成戰略層)不再冒充數據。
- anticipated 從句 miss:few-shot 餵進去,A1 正確歸 forecast。
- 跨篇去重、shared block 抽共用規則,都生效。

**prompt 修不掉的(1/6,誠實記)**:HTML 轉義 `&gt;` 即使明寫「輸出原始 `>`」還是出現。Haiku 壓不住,只能下游一行後處理。**教訓:有些缺陷是模型固有行為,prompt 勸不動,得工程兜——runtime 指引/offline 演化之外的第三類「後處理」**。

**對使用者的真實影響(比 schema 本身更值錢的發現)**:
- v1 給約 8 條信號平鋪在預測帳旁,像今日新動態。
- v2 今日真信號剩 2 條(且都標警語)、3 主題進 background、3 條進 stale_quarantine(每條附「v1 會被誤讀成什麼」)。
- 最重一條:$13.5B capex 在 v1 坐在 capex 紀律線旁像當日數據點;v2 隔離並註明「8 個月前預測,比你 84.9% 毛利率基準還早」。差別=會不會拿過期料更新投資判斷。

**最扎心的結論**:清乾淨後今天日報幾乎空的。**v1 那份「豐富」的日報大半是舊料裝新聞——真正瓶頸不是 prompt,是材料源**(搜尋摘要吐舊 digest)。schema 改進是把假訊號攔下來的濾網,但濾完發現進料本身就是舊的→ 解鎖點在材料源(白名單/接真實入口),不在繼續調 prompt。

**元判斷**:orchestrator 的最大價值不是「多產信號」,是「敢說今天沒有信號」。過期料裝成新聞的日報,比空日報更傷——因為它污染預測帳。

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

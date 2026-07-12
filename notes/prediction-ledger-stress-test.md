# 預測帳跨條目壓力測試（2026-07-05）

對 `profile.md`「你當前開放的疑問」全部條目做結構檢查：找互相打架的判斷、共用的隱含假設、結算訊號設計缺陷。**不重查個別事實**，查的是帳本身的一致性。

方法註記：這是模型 A/B 實驗的一部分——Fable（本文）與 Opus 4.8 各按同一張任務卡獨立跑。本 note 是融合版正式產出：骨架是 Fable 發包前的獨立清單，Opus 獨有的發現標 `[O]`；比較見 `notes/fable-vs-opus48-same-card-ab.md`。一手對照材料：`investment_note/research/20260627_memory_decyclicalization_stress_test.md`、`portfolio.md`。

## 一、矛盾對（按嚴重度）

**M1．「中立 harness 之死」正在侵蝕主樑卡的前提，但沒人把帳加總。**
harness-beats-model 卡的操作意義建立在「harness 是可獨立選擇的層」（同模型換 harness 就能 +5pt）。但三條線的近期數據點——Codex 併成單一 surface、Cursor 被 xAI 收編後鎖 Composer、Fugu 把編排內化進模型——共同指向**可換性本身在收斂**。單條看都有「兩層共存」接住，加總看是：中立 harness 的選項空間在變小，「選 harness」正在退化成「選垂直整合棧」。
裁決：在 `harness-beats-model` 卡補一條邊界——「判斷成立於 harness 可換的世界；當 harness 綁死模型廠，槓桿從『選 harness』遷移到『選棧』」。三條線不用改結論，但 profile 該有一行把這個跨條目侵蝕顯性化。

**M2．loop eng 與 orchestration 兩條實質是同一條帳，且只單向蒐證。**
兩條的結算訊號同構（獨立外圍層拿到付費客戶 vs 被原生內建）、數據點互相引用（Codex 併 surface 同時餵兩條）、到期日相同（2026-12）——會同時結算或同時卡 ⚪，形式上兩條實際上一條。更糟的是訊號**只設計了「被吃掉」側的觸發**，「harness 反成現金牛」的證據（Claude Code run-rate $25 億）不在任何結算條件裡 `[O]`。
裁決：合併為一條（或明確分工：loop＝治理層、orchestration＝編排層，各自找不重疊的訊號），並補一個多頭側觸發（harness 廠營收/留存續強＝共存成立）。

**M3．記憶體「框架 ✅ 強印證」與 investment_note 同期結論不同步。** `[O]` 發現、本文一手核實
profile（06-28）寫「Micron 毛利率 84.9%＝框架強印證」。但 investment_note 早一天（06-27）做完對抗審查的 stress test，結論是：多頭「去週期化」證據**偏軟**（frontmatter 自記 fact-checker 19 子 claim reliability 55.3%；self-report＋單一分析師＋韓媒談判報導）、floor 只撐營運不撐估值（floor 對應毛利 ~62% vs 現價 84.9%）、**「thesis 對 ≠ sizing 對」必須分層**。結構問題：毛利率衝高是框架的**預測項**，拿預測項當「印證」＝循環論證；真正的檢驗項是證偽觸發有沒有出現。兩本帳的樂觀度出現落差——Learning 帳慶祝印證的同一週，投資帳在做風險預算警告。
裁決：profile 該條的「最新指標」從毛利率換成 stress test §5 已長好的證偽信號（SCA 合約弱化／capex 從升級轉擴產／庫存週數／CXMT 滲透），並補一句「組合 sizing 另判，見 investment_note」。

**M4．資安計價條：命題與訊號錯位，已自承但沒修帳。**
標題問「per-seat 計價會崩？」，結算訊號測「per-agent 條目出現沒」——這是兩個命題（新層出現 ≠ 舊層崩）。條目自己已寫「若 10 月只看 per-seat 崩沒＝❌」，等於自承訊號答不了題，但帳沒改。
裁決：拆雙軌各自結算——(a) per-seat 是否鬆動（觀察 CRWD/PANW NRR／單價趨勢）、(b) per-agent 新層滲透速度（定價頁條目）。

## 二、共用假設群（一倒連環倒）

**假設 A．「核心 call 商品化、外圍治理層存活」**——eval 生態位、安全紅隊 eval、語意 merge 閘、loop 外圍治理、orchestration 兩層共存，**五條**全站在 `llm-call-niches-are-features-not-companies` 這張卡上。卡自己留了反例（監管標準化後稽核被平台內建），但五條沒有共同的關門警報。若外圍也被 incumbent 吃掉，是一次倒五條，不是逐條倒。

**假設 B．「hyperscaler capex 紀律」是跨帳單開關**——記憶體線（盯點本身）、微軟地基（learning loop 需求端）、加上投資帳的 neocloud/記憶體曝險（stress test 記 2026 capex 佔營運現金流 92%）。capex 一轉向，學習帳三條敘事與投資帳部位同時失血。

**假設 C．「利益相反方背書」這把尺套用不一致** `[O]`——Fugu 自報跑分被正確打折、Cursor「從零預訓練」標注「僅官方宣稱」，但 Micron self-report 的毛利率被當強印證。同是第一方數字，兩種待遇（M3 的另一面）。

**假設 D．「agent 很快成為付費經濟主體」**——Hood（agent 下單）、資安 per-agent 計價、MCP-as-a-rail 三條都預設 agent 將以可計價身分進入交易/安全/執行系統。若企業採用停在「工具」不到「主體」，三條一起無限期 ⚪。

## 三、結算訊號缺陷（分型）

- **窗內幾乎不可觀察**：Hood 的「判斷型 AI 操盤跑贏基準的第三方實證」——`robinhood-agentic-trading.md` 自己引了「LLM 選股無顯著 alpha」的學術證據，訊號設在自己都不信會發生的事件上 `[O]`；loop／orchestration 的「第三方複現＋有人實測自搭取代不了」同病（長任務、閉源、無中立榜）。
- **回望已結算的事**：eval 條的「promptfoo 是否仍獨立」——收編已坐實（2026-03），訊號主體已消耗，剩餘鑑別力弱。
- **n=1 且觸發權在自己手上**：部門大腦、Claude Design ROI 都以「用戶自己跑一次」為結算——可以無限期不跑、永遠掛「追蹤中」。這是預測帳版的 rot。
- **可得性偏差**：安全 eval 的「出現一個實例」——單一實例證實不了結構，且「沒看到」永遠證偽不了「不存在」。
- **系統性問題：多數條目只設單側觸發**。帳面格式是「→ 結算訊號：看到 X」，缺「看到 Y＝反向」與「到期都沒有＝⚪」的三態設計，導致單向蒐證（M2 是最重案例）。

## 四、修改建議（可直接執行）

1. `harness-beats-model` 卡加「可換性收斂」邊界；profile 加一行跨條目侵蝕註記（M1）。
2. loop＋orchestration 合併或分工，各補多頭側觸發（M2）。
3. 記憶體條指標換成證偽觸發組，補 sizing 分層句（M3）。
4. 資安條拆雙軌結算（M4）。
5. Hood 主訊號換成可觀察的兩個：改掉交易量計價／出現第二家同等開放券商（原訊號二保留、訊號一降級為 bonus）。
6. 安全 eval 訊號改「到期主動掃一輪案例，掃不到即 ⚪ 並考慮撤題」——把可得性偏差變成有時限的檢索動作。
7. eval 條換成 `llm-call-niches` 卡的開／關門指標（per-action＋audit 計價 pure-play 出現＝開；GitHub/orchestrator 原生內建 reconcile＝關）`[O]`。
8. 部門大腦／Claude Design 加規則：「到期未執行＝自動 ⚪＋主動問要不要換題」，防永久掛帳。
9. profile 預測帳節首加三行「假設群標注」（A 外圍存活×5 條／B capex×跨帳／D agent 主體×3 條），讓連環倒風險顯性化。
10. 給 `/weekly-synthesis` 加一條機械 lint：新增/修改的結算訊號必須三態齊備（✅ 觸發、❌ 觸發、⚪ 到期），單側訊號直接 flag。這條是本次壓測最可複利的一般化。

## 出處

`profile.md` 預測帳節；`notes/`：loop-engineering、sakana-fugu-orchestration-as-model、robinhood-agentic-trading、ai-security-ecosystem、eval-ecosystem-niche、memory-industry-map、cursor-spacex-xai-composer3；`topics/*/cards/`：harness-beats-model、llm-call-niches-are-features-not-companies、orchestration-as-a-model-vs-neutral-harness；`investment_note/`：portfolio.md、research/20260627_memory_decyclicalization_stress_test.md（§1 證據不對稱、§3 對抗審查、§4 兩層分離、§5 證偽信號）。

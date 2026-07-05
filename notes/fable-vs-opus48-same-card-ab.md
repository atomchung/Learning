# Fable 5 vs Opus 4.8 同任務卡 A/B（2026-07-05 實測）

**設定**：三張自包含任務卡（A＝Issue #6 梳理、B＝預測帳壓測、C＝cwc-workshops 對讀），四要素齊（objective / sources / format / boundaries）。Fable 在 main loop 執行，同時發 3 個 Opus 4.8 subagent 冷啟動跑同卡。Opus 產出原文存 session scratchpad（`opus-task-{a,b,c}.md`，A 卡已存、B/C 全文在 transcript）。

**方法論 caveat（誠實記）**：背景 agent 完成通知會**自動進 orchestrator 的 context**，Opus 三份在我寫 B/C 前就送達——嚴格盲測破功。補救＝我以發包前寫下的獨立矛盾清單為骨架；但「重疊處」已無法歸因，只有「各自獨有處」是有效信號。**教訓：orchestrator 沒辦法同時當盲測受試者**；要真盲測，兩邊都該是 subagent、orchestrator 只當 judge。

## 量測

- Opus 三卡：82k / 141k / 89k subagent tokens，13 / 25 / 23 次工具呼叫，每卡 2.3–3.1 分鐘。
- 內容重疊度（結論級）：約 **70–80%**。同卡＋同材料下，兩個模型的基本盤結論幾乎一致——北極星、機制盤點、B13 否決、單向蒐證、audit.md 對位……全部撞題。
- **引用準確度：Opus 零幻覺**。抽查全數核實——investment_note frontmatter 的「fact-checker 55.3%」、`data-verify-*`／`BLOCKED≠FAIL`／`probe:true`、71%→92%。與 07-04「subagent 誤報 7 個幽靈工具」相反的數據點（樣本各一次，先不下結論，繼續攢）。

## 各自獨有的發現（有效信號區）

**Opus 4.8 獨有（我沒挖到／沒想到）**：
- B 卡：挖進 `investment_note/research/20260627_memory_decyclicalization_stress_test.md` 抓出「profile 強印證 vs 投資帳自家保守結論」的兩本帳矛盾——**本次全實驗最有價值的單條發現**，來自它肯往 sources 最後一項深挖。
- B 卡：「對沖線只單向蒐證，Claude Code $25 億 run-rate 不在任何結算條件裡」。
- A 卡：「R1 與 B14 天生拉扯」（防自評閘 vs 讓 Claude 自行二分）——結構敏感度高。
- C 卡：讀面更廣（graders.ts、research-desk、production-ready-agent），「Dreaming＝weekly-synthesis 的托管版」裁決漂亮。

**Fable 獨有（Opus 三份都沒有）**：
- **跨任務三脈絡交會**：audit.md 的 both-directions coverage（C 卡）× 預測帳單側訊號（B 卡）× R1 防自評＝同一判斷第三次出現→升卡候選。Opus 結構上**不可能**發現——B、C 是兩個隔離 agent，各自看不到對方。
- **帳本意識**：把 71%→92%（+21pt 不換模型）明確接回 `harness-beats-model` 卡的證據欄；Opus 用了這數字但沒接到主樑卡。
- 更收斂的一般化：「taxonomy 預測力弱、真資產是 append 習慣」「訊號要三態齊備」直接變 lint 規則提案。
- M1「中立 harness 之死」的加總視角（三條線數據點合起來侵蝕主樑卡前提）。

**輸出紀律小差**：任務卡指定「最終回覆就是交付物」，Opus 三份開頭都帶了一段工作日誌（"I now have all the source material…"）才進正文；不影響內容，但下游若機器解析就要多一步清洗。

## 結構性結論（可重用）

1. **單卡綜合，Opus 4.8 已經夠好**：自包含任務卡＋本機材料的研究綜合，Opus 快（3 分鐘）、準（零幻覺）、深（肯挖到 frontmatter 層）。這類活委派出去，不用燒 Fable 視窗。
2. **Fable 的真差異化在 orchestrator 位置的跨脈絡連線**，而且誠實說：這次無法乾淨分離「模型能力差」與「context 位置差」——我贏的兩條（三脈絡交會、帳本意識）都吃了全 session context 的紅利。**位置（能看到什麼）比模型檔次貢獻更大＝harness>model 的又一個小注腳。**
3. 分工驗證了既有框架：`fable-limited-window-strategy`（Fable 拿判斷與連線、執行外包）＋`prompting-small-models` 的 effort 分層——只是這次「小模型」是 Opus 4.8。委派契約四要素在 Mythos→Opus 這一級同樣有效，且 Opus 這級**不需要** few-shot／逐步程序（Prompting Inversion 方向再現：三張卡都只給目標＋邊界，零 drift）。
4. 對「該不該花錢開強 subagent」的操作答案：**判斷密度高的單卡活給 Opus、跨卡收斂與裁決留 orchestrator**；把 orchestrator 的獨有價值寫進任務設計（誰負責連線、誰負責接回卡片體系），比糾結模型檔次更有槓桿。

## 出處

三張任務卡與 Opus 產出全文：session transcript＋scratchpad；Fable 版正式產出＝`notes/issue6-recursive-harness-review.md`、`notes/prediction-ledger-stress-test.md`、`notes/cwc-workshops-cross-read.md`（後兩份為融合版，`[O]` 標注歸屬）。

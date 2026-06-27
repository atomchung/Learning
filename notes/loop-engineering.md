# Loop Engineering（迴圈工程）

> 2026-06-27 研究。問題：loop eng 是什麼、對我有什麼 learning / best practice。
> 一句話結論：**它是 harness 之上的第五層，是「harness>model」這條線到目前最強的佐證——槓桿點再一次離模型更遠。而且我其實已經在做它的雛形。**

## 先記預測（校準用）

研究前我猜：loop eng＝把 agent 外迴圈（plan→act→observe→repeat）當第一級工程，是 prompt/context engineering 下一站，重點在停止判準＋自我驗證＋每圈壓縮。
查證後：**方向對**，但具體增量是——(1) 它不只是「外迴圈」，而是「**你不再親手 prompt，改成設計一個會替你 prompt 的系統**」；(2) 有明確命名時點與人（不是泛泛趨勢）；(3) 最痛的點是 **verifier 而非 model**，正中我「eval 瓶頸是判準不是工具」那張卡。

## 是什麼：四層演化到第五層

槓桿點一路往外移，每層包住內層：

1. **Prompt engineering**：調你手打的那一句
2. **Context engineering**：管模型每一回合看到的全部（檔案/歷史/工具定義）
3. **Harness engineering**：模型外面那圈程式（跑工具、追狀態、錯誤恢復）＝我已有的 `harness-four-layers` 卡
4. **Loop engineering**：**自主控制結構**——決定 agent 該做什麼、何時做、做完了沒，然後讓系統自己去 poke agent，不靠你手打

Steinberger（2026-06-07，~6.5M views）：「你不該再 prompt coding agent，你該設計會 prompt agent 的迴圈。」隔天 Addy Osmani（Google）命名為 Loop Engineering 並給出解剖。Boris Cherny（Anthropic，Claude Code 負責人）：「我已經不 prompt Claude 了，我有一堆迴圈在 prompt Claude、自己決定要做什麼。」

→ 三個利益相反方（Google DevRel、Anthropic harness 負責人、獨立開發者）同時說同一件事，當訊號讀：**leverage 確實在往 loop 移**，不是單一廠的行銷。

## 解剖：六個積木（含記憶）

1. **排程/自動化**：照節奏做 discovery + triage（不是你按下去才動）
2. **Worktrees**：平行 agent 各自隔離，不互撞檔案
3. **Skills**：把專案知識固化成可重用技能
4. **Connectors / MCP**：把 agent 接進你真正的工具（git、ticket、CI）
5. **Sub-agents**：把 **maker 跟 checker 拆開**（做事的跟驗收的不同 agent）
6. **外部狀態 / 記憶**：對話之外的持久 context（記「什麼已做完」）

## 四種 loop 型態

- **Heartbeat**：短間隔持續跑（PR babysitter 5–15 分）
- **Cron**：固定時點（每天 10am triage）
- **Hook**：事件觸發（PR push、CI 失敗）
- **Goal**：迭代到成功條件才停（「讓測試過」）

## Best practices（這是重點）

**1. Goal loop 的四個不可省**（缺一個就是 runaway）：
- 最大迭代上限（hard cap）
- 預算上限（token budget cap）
- **agent 自己評得出來的成功函數**
- 達不到時的升級/逃生路徑（escalation）

**2. 目標要可測**：「讓測試過」是好目標（成功可檢查）；「把程式改好」是爛目標（永遠不知道何時停）。

**3. Maker-checker**：無人值守就一定要有**獨立 verifier**（不同指令、最好不同模型）來打分，**做事的 agent 不准自評**。

**4. 漸進放權**：報告-only（L1）→ 輔助修（L2）→ 無人值守（L3）。不要第一版就上 10 步全自動，從「observe + act」兩步起。

**5. 留在工程師位**：Osmani——「建迴圈，但要像個打算繼續當工程師的人來建，不是只負責按 go 的人。」迴圈會**放大你的判斷，好的壞的一起放大**。

## 三個 failure mode（要會認）

1. **Runaway cost**：目標沒有收斂判準（「研究競品全景」沒有停止條件），燒幾千 token 沒人發現。
2. **Hallucinated success**：agent 自報「done」但沒真驗。解法＝只信**確定性 verifier**，永不信 agent 自報。
3. **Verifier bottleneck**：generator 便宜地一直跑，所以瓶頸是 verifier 不是 model。**弱的「夠好了嗎」判準不會大聲失敗——它會自信地、重複幾百次地產出垃圾。** ←這句直接對應我的 `eval-bottleneck-is-criteria-not-tooling` 卡。

## 對我的具體 learning

**(A) 我已經在做 loop eng 的雛形，只是沒命名。**盤點這個 repo：
- `SessionStart` hook 載入 profile ＝ heartbeat/hook loop 的記憶讀取
- `/weekly-synthesis`、`/meta-review` ＝ cron loop
- 「repo 是我的腦」＝外部狀態/記憶積木
- 候選池那條「outcomes 迴圈（/loop + 自寫判準）」＝我自己早就想碰 goal loop
→ 所以這題不是新大陸，是**把我散落的 loop 行為對齊到一套命名與 best practice**。

**(B) 我缺的那塊正是 best practice 點名的：verifier。**我的 `/loop` 若要進化成 goal loop，缺的不是排程是「自寫判準」——而 best practice 說「judgment 與校準才稀缺」（呼應 `info-intake-routine`），maker-checker 要拆。下次動手複製時，**先寫 verifier，再寫迴圈**。

**(C) 不要因為「會自動」就放掉理解。**failure mode 之一是 comprehension debt（迴圈輸出沒人讀）。對我的 brain-repo 直接適用：自動沉澱卡片若沒人 review，就是自信地累積垃圾。`/weekly-synthesis` 的存在正是這個 checker。

## 投資 / 訊號角度

六個積木（排程、worktree、skill、connector、subagent、memory）目前**都長在 harness 廠手裡**（Claude Code、Cursor）。問題：loop eng 成為主戰場後，價值流向 harness 擁有者，還是會像 eval/merge 閘那樣冒出**外圍 pure-play**（loop 監控、cost 治理、verifier-as-a-service）？

初判：跟我 `llm-call-niches-are-features-not-companies` 同結構——單一 loop 動作（排程一個 trigger、估一次 cost）是 feature 不是 company，但「**跨多 loop 的成本/安全治理層**」可能是外圍可投資表達式（對位資安計價那條線）。待觀察。

## 開放疑問（預測帳）

- **loop eng 的價值會被 harness 吃掉還是長出外圍 pure-play？**（`check:2026-12`）對沖我「harness>model」——如果連 loop 都被 harness 廠原生吃掉，那 harness 廠的護城河更深；如果冒出獨立 loop 治理層，則槓桿又外移一層。
- **verifier 會不會變成下一個瓶頸生意？**maker 便宜、checker 貴——「verifier-as-a-service」有沒有生態位，還是又是 eval 那套天花板（鎖在模型廠內）？（`check:2026-09`，併入 eval 生態位線）

## 出處
- Addy Osmani, "Loop Engineering"（2026-06-08，O'Reilly Radar 轉載）— 命名與 anatomy
- Peter Steinberger（2026-06-07 貼文）— 起點論點
- LangChain, "The Art of Loop Engineering" — 四層堆疊框架
- Daily Dose of DS, "Loop Engineering, Clearly Explained" — 四層定義
- cobusgreyling/loop-engineering（GitHub）— 七個 production pattern、L1→L3 rollout、failure-modes、loop-audit/loop-cost CLI
- Requesty / Agent Shortlist — goal loop 四不可省、verifier bottleneck

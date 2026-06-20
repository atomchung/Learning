# meta/borrowable-patterns.md — 別人的好設計，我們能借鑒的點（living ledger）

> 跟 `defects.md` 當兄弟，都餵 `/meta-review`（Issue #6 遞迴改進 harness）。
> defects = 我們做錯的；這份 = 別人做對、我們該抄的。
> 規則：看到外部 agent/系統的好設計，append 一條。格式：**來源 → 我們的 gap → 借鑒動作 → 狀態**。
> 動 CLAUDE.md 規則前，比照 R1：高影響的借鑒要有用戶點頭，不要 Claude 自己偷改契約。

## 借鑒清單（按 ROI，append-only）

### HIGH

**B1. 蒸餾時機前移：event-triggered，不只 sleep-triggered**
- 來源：Hermes self-improving skills——複雜任務一結束、坑還新鮮時就**當下提議**存 skill。
- 我們的 gap：只在睡前 / `/meta-review` 蒸餾，常攢到 session 末才回看，細節已涼。
- 借鑒動作：一條問答冒出可重用判斷的**當下**，主動問「要不要沉成卡片？」。回應 open question（weekly-synthesis、auto-distill cards from repeated Q&A）。
- 狀態：提案中（2026-06-20）。低成本（純行為，不加架構）。

**B2. 連坑一起記，不只記結論**
- 來源：Hermes 自動寫的 skill 內含「沿途踩的坑 + 驗證步驟」，不只 happy path。
- 我們的 gap：卡片多半只存結論 + 選配反例；內容層的「我一開始錯在哪」沒系統性留。
- 借鑒動作：蒸餾卡片時也記「原本以為 X、錯在哪、怎麼驗的」。等於把 `defects.md`（harness 層踩坑）的動作延伸到**內容層**。
- 狀態：提案中（2026-06-20）。

**B3.「重複出現」當升級訊號，給具體門檻**
- 來源：Hermes 觸發條件 =「task pattern 跨 session 重現」。
- 我們的 gap：note→card 升級訊號很模糊（「可跨脈絡重用」靠手感）。
- 借鑒動作：某判斷/主題在 ≥N 條 inbox 出現過 → 自動 flag 升級。meta-review 時 grep 一下即可，不需新基建。
- 狀態：提案中（2026-06-20）。

### MEDIUM（多半驗證我們已對，行動=講明白/別退步）

**B4. 分層審批閘（write-freely vs approve-each）**
- 來源：Hermes 可設 skill 自由寫 or 每次審；OpenClaw 同理。
- 我們：已是對的切法——notes/卡片自由寫、CLAUDE.md 規則要審（R1 防自評閘）。
- 借鑒動作：把分層講明白，別動。✅ 已落地。

**B5. 索引 + 按需載入**
- 來源：Hermes `skills_list()`（索引）→ `skill_view(name)`（按需載入）。
- 我們：profile（索引）→ grep → 卡。同設計。
- 借鑒動作：保持索引精簡、別把全庫塞 context。✅ 驗證「wiki 當硬碟、context 當 RAM」。

**B6. 本地 FTS recall，別重餵 context（反面教材）**
- 來源：OpenClaw 每次 recall 把整份 JSONL 餵回 context（~19s）= **反例**；Hermes 本地 SQLite FTS（~113ms）= 正例。
- 我們：grep markdown 在好的一邊。
- 借鑒動作：永遠別退回「全塞 context」。✅ 守住。

### LOW（留觀察，個人 repo ROI 薄）

**B7. 可攜/模組化**：provider 拆 npm plugin、migrate 的 plan/dry-run、agentskills.io 可攜 SKILL.md 標準。對個人知識 repo ROI 薄，先記著，團隊/部門腦版才考慮。

## 元判斷

我們系統本來就是這個物種（markdown + 索引 + grep），可借鑒的 delta 是**時機與自動化，不是架構**。單一最高 ROI = 蒸餾從「只在睡前」→「事件觸發 + 當下主動提議」+ 連坑一起記。

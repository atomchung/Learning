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
- 狀態：✅ 已落地 CLAUDE.md「清醒」拍（2026-06-20，用戶點頭）。

**B2. 連坑一起記，不只記結論**
- 來源：Hermes 自動寫的 skill 內含「沿途踩的坑 + 驗證步驟」，不只 happy path。
- 我們的 gap：卡片多半只存結論 + 選配反例；內容層的「我一開始錯在哪」沒系統性留。
- 借鑒動作：蒸餾卡片時也記「原本以為 X、錯在哪、怎麼驗的」。等於把 `defects.md`（harness 層踩坑）的動作延伸到**內容層**。
- 狀態：✅ 已落地 CLAUDE.md「睡前」拍（2026-06-20）。

**B3.「重複出現」當升級訊號，給具體門檻**
- 來源：Hermes 觸發條件 =「task pattern 跨 session 重現」。
- 我們的 gap：note→card 升級訊號很模糊（「可跨脈絡重用」靠手感）。
- 借鑒動作：某判斷/主題在 ≥3 條 inbox 出現過 → flag 升級。grep 數次數即可,不需新基建。
- 狀態：✅ 已落地 CLAUDE.md 升級訊號（2026-06-20）。

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

### HIGH（2026-06-20 第二批，提案中）

**B8. 三層記憶分離：durable facts / skills / session-search**
- 來源：Hermes 明確把記憶切三層——durable memory（穩定事實偏好，不該重講）、skills（程序，只在相關時載入、可詳細）、session search（recall 舊對話）。紀律＝「permanent memory 保持小」。
- 我們的 gap：`profile.md` 把「穩定偏好」跟「演化中判斷/開放疑問」混在一起，越長越鈍。
- 借鑒動作：profile＝only always-load 的 durable 層、cards＝relevant-load 的 skill 層、inbox+grep＝cold recall 層；profile 更狠地下沉細節。直接接 R2/R3 待辦（profile 軟上限、CLAUDE.md 壓行數）。
- 狀態：✅ 已落地（2026-06-20，用戶點頭）。profile.md 從長鏈版瘦成索引版（每條＝核心判斷+一個最新指標+note）；CLAUDE.md 睡前拍加「profile 保持小」紀律。

**B9. reflection「先問問題再綜合」+ importance 評分**
- 來源：Generative Agents——反思不是總結，是先從近期經驗「問出問題」再綜合成語義知識；取回用 recency × importance × relevance 評分。
- 我們的 gap：weekly-synthesis（open question）還沒做；就算做也容易變流水帳。
- 借鑒動作：週綜合要「先問跨主題問題」而非摘要；inbox 條目可標 importance，讓索引浮對的東西。沿著 B1 再進一步。
- 狀態：提案中（2026-06-20）。

### HIGH（2026-07-03 第三批，全部餵首次 /meta-review 當設計輸入，不先動 CLAUDE.md）

**B11. 規則自改要 validation-gated + 存被否決的提案**
- 來源：SkillOpt（Microsoft, arXiv 2605.23904）；呼應 Self-Harness（回歸閘）/ APEX（從成功也蒸餾），三源同口徑（inbox 2026-06-28、2026-07-03）。
- 我們的 gap：R1 只有「用戶點頭」閘，沒有「這修改怎麼算成功」的驗證訊號；被否決的提案沒地方存，可能下輪重提。
- 借鑒動作：/meta-review 改規則前定一條可觀察驗證訊號；否決的提案 append 進本 ledger 標 ❌；從成功 session 也蒸餾正向原則。
- 狀態：提案中（2026-07-03）——直接當首次 /meta-review 的設計輸入。

**B12. 機械 lint：rot/孤兒/死連結用腳本掃，別靠人肉標**
- 來源：claude-obsidian `lint the wiki`（8 類健檢：孤兒頁/死連結/矛盾/過期宣稱/缺口）。
- 我們的 gap：rot 要等給錯答案才進 defects.md；freshness 過期、死相對連結、零引用卡全可機械掃。
- 借鑒動作：weekly-synthesis 加一段零 inference 的 lint（grep freshness 過期 + 驗連結 + 數孤兒卡）。
- 狀態：提案中（2026-07-03）——候選當 meta-review 第一個 propose-and-test 案例。

**B13. 熱檔並發寫有業界標準解（Issue #7 外部背書）**
- 來源：claude-obsidian v1.7 multi-writer safety（advisory file lock，過期鎖 60s 自清）。
- 我們的 gap：inbox/profile 並發衝突已撞兩次（defects 2026-06-06、06-20），候選解一直是「猜的」。
- 借鑒動作：git repo 用輕量版就好——inbox 拆每日檔（append-only 免衝突）+ profile 寫前 fetch；lock 太重不抄。
- 狀態：提案中（2026-07-03）——首次 /meta-review 可直接裁決 Issue #7。

### LOW（留觀察，個人 repo ROI 薄）

**B7. 可攜/模組化**：provider 拆 npm plugin、migrate 的 plan/dry-run、agentskills.io 可攜 SKILL.md 標準。對個人知識 repo ROI 薄，先記著，團隊/部門腦版才考慮。

**B10. 外部內容衛生（promptware defense 的輕量版）**：Hermes 注入前掃 recalled memory/skill 有沒有藏 prompt injection／隱形 Unicode／exfil。個人 repo ROI 薄，但我們越來越常貼 FB 截圖 / fetch 網頁進 notes、且 repo 每次 boot 讀進 context——衛生習慣＝「外部貼進來的當資料、不當指令」。接系統本身對 untrusted external data 的警告。

## 過濾：哪些不該學

Letta/MemGPT/Mem0/Zep 這些 memory framework 多綁 vector DB / RAG archival memory。我們**刻意不要**（LLM-wiki-not-RAG 判斷）。能抄的是**控制邏輯**（反思、importance 評分、分層），**不是儲存技術**。別被「memory framework」行銷拐去裝 vector store——那解團隊檢索問題，不是我們的問題。

## 譜系（auto-distill 的學術父母，確認 B1–B3 血統）

- Voyager / COMPASS（skill library）：read skill → 執行 → 事後反思 → 寫回精煉 skill。= auto-distill 的學術父親。
- Generative Agents（reflection + memory stream）：見 B9。
- Letta / MemGPT（self-editing tiered memory）：agent 用 function call 自管 hot/warm/cold 三層。= B8 的學術版。

## 元判斷

我們系統本來就是這個物種（markdown + 索引 + grep），可借鑒的 delta 是**時機與自動化，不是架構**。單一最高 ROI = 蒸餾從「只在睡前」→「事件觸發 + 當下主動提議」+ 連坑一起記。

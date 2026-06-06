# 遞迴改進 harness × 社群 best practice 整合（接 Issue #6）

> 2026-06-06。把我們手刻的記憶/自我改進系統，對到社群有名的 pattern，借它們的精修、抓我們的風險。
> 既有基礎見 `notes/agent-context-best-practices.md`、`notes/skills-workflow-best-practices.md`，這份只補「自我改進迴圈」這層。

## 一句話結論

我們的 boot/awake/sleep + `meta/defects.md` + `/meta-review`，**是社群三個 pattern 的土法再發明**。手刻沒錯（理解最深），但社群已經踩過幾個坑，值得直接借。

## 我們已經做對的（社群有正式名字）

- **分層記憶（Letta / MemGPT）**：main context = RAM、外部檔案 = disk。我們的 `profile.md` 就是 RAM 索引、`inbox.md`/`notes/` 是 disk。boot 只載索引、要細節才 grep = 正解。
- **情節記憶（Zep）**：append-only + 日期戳的 `inbox.md` 正是 episodic log，能答「上次那題」。
- **自編輯記憶（Letta 的核心特色）**：agent 自己決定記什麼。我們 sleep 時自己更新 profile = 同一招。
- **外部 artifact 接力（Anthropic 長任務 harness）**：initializer 設環境 + 每 session 留清楚 artifact 給下一棒。我們的 SessionStart hook + profile 更新 = 同構。

→ 這層不用改，是對的。

## 社群說我們有風險的三個點（要動的在這）

### R1：別讓 meta-review 自己給自己打分
**證據**：Anthropic 長任務 harness 報告明說——agent 被要求評自己產出時，**傾向自信地稱讚自己**，即使品質明顯普通。這正是我設計 meta-review 時擔心的「Claude 會漏自己盲點」，社群有實證背書。
**改法**：梯度信號裡，**用戶標的缺陷權重 > Claude 自標**。meta-review 不是「Claude 檢討 Claude」，是「Claude 整理用戶＋自己標的缺陷」。可加一條：每次 review 至少要有一筆是用戶標的，否則視為證據不足、先別大改規則。

### R2：profile.md 一定會膨脹，要有驅逐紀律
**證據**：Letta/Mem0 的分層記憶核心紀律是「**hot 層必須小**」——always-loaded 的索引越大，每次 boot 越貴、訊噪比越差（Mem0 4 月還專門出 token-efficient 檢索演算法壓到 ~7K/次）。我們 boot 每次全載 profile.md，它只會長不會縮。
**改法**：profile.md 設**軟上限**（如 ≤120 行），已解決的開放疑問移到 inbox 存底、不留在索引。這其實就是我們 meta-review 的「加二刪一」閘，**只是要把它也套在 profile.md 自己身上**，不只套在規則上。接你自己的開放疑問「profile 膨脹會變債務」。

### R3：CLAUDE.md 正在變長，逼近 200 行警戒
**證據**：我們自己的 `agent-context-best-practices.md` 第 115–121 行就寫了——CLAUDE.md >200 行指令遵循度下降、>400 行「30 條有用規則埋在噪音裡」。我們的 CLAUDE.md 一直在加東西（兩層制、記憶層、缺陷記錄…）。
**改法**：把「怎麼做」的流程細節從 CLAUDE.md 移到 skill（如卡片化流程、journey 格式可變 skill 按需載入），CLAUDE.md 只留「永遠要在場」的契約。這是一次純壓縮，ROI 最高。**待驗證，別急著動**——先確認真的超標。

## 值得研究的社群現成品（prior art，不一定採用）

- **harness-evolver（社群 plugin，2026-03 前後）**：用多 agent proposer 在隔離 git worktree 裡自動演化 harness（prompt/routing/retrieval），用 eval + 全軌跡反事實診斷挑改法。這就是我們 Issue #6 的**自動化版**。我們是人踩一腳才轉，它想讓外迴圈自己轉。當對照組看，別急著搬——它的前提是有自動 eval，我們還沒有。

## 落地狀態（給 Issue #6）

1. **R1 ✅ 已做（2026-06-06）**：`/meta-review` 加「證據門檻」——動規則前至少一筆 `@user` 標的缺陷，否則視為證據不足。`meta/defects.md` 格式加 `@user|@claude` 來源標記。補我們最大盲點（自評不可靠）。
2. **R2 待辦**：profile.md 加軟上限（≤120 行）+ 驅逐紀律。現在 57 行還健康，預防性，之後做。
3. **R3 待辦**：CLAUDE.md 已 283 行（>200 警戒線，確認超標）。流程細節移到 skill。一次純壓縮，ROI 高，但要謹慎拆，下次專門做一輪。

共同原則仍是反膨脹：**能刪規則的整合才是對的整合**。借社群 pattern 是為了更省，不是堆更多結構。

## 出處
- Letta/MemGPT 分層+自編輯記憶、Mem0 token-efficient 檢索、Zep 情節記憶：mem0.ai「State of AI Agent Memory 2026」、atlan.com 框架對比
- 自評不可靠 + initializer/artifact 接力：anthropic.com/engineering/effective-harnesses-for-long-running-agents
- harness-evolver / harness engineering：github awesome-harness-engineering
- 內部既有：`notes/agent-context-best-practices.md`、`notes/skills-workflow-best-practices.md`

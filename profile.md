---
type: interest-profile
maintained-by: claude
updated: 2026-07-18
last-session: 2026-07-18 tmux-bridge Threads 截圖「對我們有用嗎/實際場景怎麼用」→ 拆成「拓撲決定協作媒介」:對等/分布式 agent(各自獨立主 session、不同機不同時,＝cloud/remote 天生型態)只有 git remote 可共享、被逼上 diff/PR;共享游標/終端(tmux-bridge)只在主從+同機+同步成立。這是 agent-collab-infra 卡「diff not cursor」的隱藏變量＝拓撲;共享終端可當 live 交接的短暫傳輸匯流排,耐久單位仍是 diff。個人場景:並行 session 撞車＝拓撲 B,session-records→reconcile→personal_os/session-board 已是對等總線正確解,只有塌縮成單機單 driver live 內循環才值得 tmux-bridge。升新卡 `topology-decides-agent-collab-medium`(coding-agents 累計 24 張)。順手信號坑:5.2K views 爆紅貼是沒標源轉載、真作者 howardpen9=回文 0xhoward_peng＝讀信號不讀表面數字案例。待續:三主 session 怎麼分工(正本/reconcile 定序)擱置待聊。
note: 這是「AI 持續記住你」的記憶層。每次 session 我開頭先讀它、結尾更新它，你不必重複交代背景。
discipline: permanent memory 保持小（B8，借 Hermes）。這份＝durable 層（always-load），只放「核心判斷 + 一個最新指標 + note 連結」。演化細節（前次的前次…）下沉 inbox/notes，靠 grep 回憶。別讓話題後面長出「最新…前次…前次」的長鏈。
---

# 你的興趣檔案

> 我（Claude）每次 session 開頭先讀這份、結尾更新這份。
> 所以你隨處丟問題，我都能接著上次、知道你在乎什麼。
> **這份是索引不是內文**：要細節 `grep` inbox.md / notes/（關鍵字、日期）。

## 你持續關注的話題

每條＝主題 + 核心 durable 判斷 + 最新指標（一條）。更早的脈絡在 inbox/notes。

- **AI agents / coding agents** — 最深（~15 卡）。核心：harness>model、沙箱、記憶架構、人機協作、多 agent 編排；loop＝harness 之上第五層（prompt→context→harness→loop，瓶頸是 verifier 不是 model，`notes/loop-engineering.md`）。最新(2026-06-28)：harness>model 拿到**公開榜第三方實測**(Terminal-Bench 上 GPT-5.5 同模型換 harness 差 5.2pt；hash 行定址讓 15 模型同漲 5–14pt)＋產業把「harness」正名(OpenAI/MS)；orchestration 改判「兩層共存」(見預測帳)。記憶卡加邊界：勝負手只在「塞不下」時成立(BEAM/LIGHT ICLR26 背書),塞得下時別上記憶層（`topics/coding-agents/cards/harness-beats-model.md`、inbox 2026-06-28）。
- **Agent OS / Personal OS** — 怎麼做、市場全景、從投資模盤切入個人 OS（4 notes）。核心：agent 協作單位是 PR/diff 不是共享游標（像 git 不像 google doc）；**媒介由拓撲決定**——對等分布式被逼上 git、主從同機才容得下共享終端（`topics/coding-agents/cards/topology-decides-agent-collab-medium.md`、`notes/agent-collab-infra.md`，2026-07-18 tmux-bridge）。
- **非工程師怎麼變 AI Power User** — roadmap / user stories / 工作・個人 companion（4 notes，很實戰）。核心診斷：用不上的真因是工作流沒設計階段、不是工具（`notes/claude-design.md`、`ai-power-user-*`）。
- **AI 產業判斷 / 投資訊號** — 讀信號不讀數字、開源商品化計時器、價值流向、中國開源、模型軌跡。核心：記憶體＝三個市場非一個（commodity DRAM/HBM/NAND 定價邏輯不同，混講必誤判）；元判斷「商品週期盯 capex 紀律不盯需求故事」。最新(2026-07-11)：Mercor(RLHF 專家勞動供應鏈)案例——GMV($20 億)≠revenue(實際 $6-8 億，套「讀信號不讀表面數字」抓到落差)；補「外圍供應鏈層」卡新案例；證偽訊號＝labs 是否加速自建 in-house domain expert 團隊(內部化擠壓 take-rate，同構商品化計時器)（`notes/mercor-rlhf-labor-market.md`、inbox 2026-07-11）。
- **MSFT × OpenAI super app** — 平台×模型乘積、Graph/Entra 護城河、Copilot 滲透真假。核心：agent 寫進去的正本留、繞過的 UI 死，排序 身份/安全 > GitHub 基板 > Office（`notes/nadella-frontier-ecosystem.md`）。
- **學習 / 教育加速** — Alpha School、learning roadmap、skills/eval 設計。最新(2026-06-20)：個人攝取流程設計——資訊不稀缺、判斷與校準才稀缺；攝取 5 關瓶頸在壓縮+證偽（`notes/info-intake-routine.md`）。
- **知識系統怎麼設計才真的複利**（元主題＝這個 repo） — 核心：這 repo＝Karpathy LLM wiki 的實例（AI 維護 markdown、預編譯複利），個人預設不需 RAG（`notes/rag-vs-llm-wiki.md`、`claude-code-second-brain-noah-brier.md`）。

## 你當前開放的疑問（＝預測帳）

每條＝問題 + 現狀（✅收斂/追蹤中）+ **`→ 結算訊號`（一個可觀察事件才算到期可判，避免 runaway）** + note + `check:YYYY-MM`（到期回看日）。`/weekly-synthesis` 掃到到期就結算 ✅對 / ❌錯 / ⚪無結論 ＋一句話（**錯的補「為什麼錯」**＝校準燃料）。推理過程在 inbox/notes，grep 回憶。

> **共用假設群（一倒連環倒，07-05 壓測立，詳 `notes/prediction-ledger-stress-test.md`）**：
> - A「外圍治理層可投資」×5 條（eval／安全紅隊／merge 閘／loop-orchestration）——共同關門警報＝外圍被 incumbent 原生內建
> - B「hyperscaler capex 紀律」跨帳（記憶體線＋微軟地基＋investment_note 部位）——capex 轉向＝三線同時重估
> - D「agent 快成付費經濟主體」×3 條（Hood／資安 per-agent／MCP rail）——企業採用停在工具層＝三條一起 ⚪

- **知識系統怎麼對我產生收益？** ✅ 收斂：改造成「repo 是我的腦」記憶層，三拍循環 + SessionStart hook 已落地（CLAUDE.md、`.claude/settings.json`）。
- **部門大腦怎麼從零搭起？**（2026-06-17，`check:2026-07`）追蹤中。三步：整理地圖→梳理 high-level→持續維護。關鍵：痛點是「沒人寫/沒人維護」非檢索（RAG 解錯問題）；勝負手＝寫入成本壓近零 + 維護外包 AI；owner「只審不寫」；起點先畫跨主題地圖+綜述（從 metadata 聚類）。待辦：用戶可能真的套用（`notes/department-brain-process.md`，已 /record）。**→ 結算訊號**：用戶實際套一次（畫了跨主題地圖+綜述），且回報「維護是否真外包給 AI、寫入成本是否近零」。**掛帳規則（07-05）**：到期仍未執行＝自動 ⚪＋主動問要不要換題（n=1 自控觸發，防永久掛帳）。
- **遞迴改進 harness（Issue #6）**（`check:2026-07`）追蹤中＝最活躍的元線。基礎設施已接（`meta/defects.md` + `/meta-review` + R1 防自評）。借鑒 ledger `meta/borrowable-patterns.md`：**B1–B3 已落地 CLAUDE.md**（蒸餾時機前移／連坑一起記／≥3 次出現升級）；**B8 已落地**（profile 三層瘦身，即本檔）；**B9（reflection 先問問題+importance）、B10（外部內容衛生）提案中**。R2/R3：CLAUDE.md 行數要壓回 <200。能刪規則的 RSI 才是對的 RSI。**首次 `/meta-review` 已跑（2026-07-04，結算訊號 ✅：實際砍規則、行數 290→268）**：立第五類 `[write-conflict]`＋CLAUDE.md 加「熱檔寫前 rebase、寫完即 push」＋砍「手機 Obsidian 設定」段（移 notes/obsidian-mobile-setup.md）；Issue #7 裁決不拆 inbox（每日檔擋不住同日並發，兩次衝突都同日），B13 拆檔部分否決 ❌ 進 ledger、B11 驗證訊號已定（write-conflict 至 2026-09 再犯 ≥2 → 升級拆每 session 檔）。B14 二分試點第 1 次：2 題、無 triage-miss。**下輪候選**：env-403（07-04 @user，根治＝用戶調環境 network policy）；false-completion／credibility-miss 再犯即立類；CLAUDE.md 砍行候選＝檔案格式模板段（原子卡/起點卡/journey，~40 行，擬抽 schema 檔留 pointer）、手機可讀性規則（收益有限，可否決）。詳 inbox 2026-07-04。**完整梳理（07-05）**：`notes/issue6-recursive-harness-review.md`（五節可接手版：北極星/機制/證據結算/張力/下一步）。
- **meta-review 迴圈本身值不值得？**（2026-07-04，用戶質疑 B 類收益≈0）追蹤中。**→ 結算訊號**：`write-conflict` 缺陷至 2026-09 再犯次數（`meta/defects.md`）+ 用戶主觀是否感到改善（少花時間解衝突、規則變準）；若到期無感 → 按北極星（Issue #6 目的是省事不是跑儀式）把迴圈砍小或降頻。`check:2026-09`
- **內容層的週綜合**（2026-06-06）✅ 收斂：`weekly-synthesis` skill 已建（`.claude/skills/weekly-synthesis/`），meta-review 的內容層兄弟——每週掃 inbox+notes 抽跨主題模式、結算預測帳、提卡片升級。同步把本段開放疑問改造成**預測帳**（每條帶 `check:`），補上攝取流程第 5 關證偽校準（`notes/info-intake-routine.md`、`claude-code-second-brain-noah-brier.md`）。
- **eval 生態位**（`check:2026-09`）→**命題拆兩層**：promptfoo 被 OpenAI 收編坐實(2026-03,~$86M,被窄化成 red-team)＝單一中立工具易被收編；但中立層換骨不消失,由政府(UK AISI Inspect)/基建大廠(ClickHouse 收 Langfuse、續 MIT)/獨立 vendor 三腿撐厚。判準卡再升級：瓶頸從「寫 rubric」→「judge 在專業領域穩定套用+對齊人類」(arXiv《Learning to Judge》2026-02,專業域相關係數崩到<0.3)。**→ 結算訊號（07-05 換層——promptfoo 收編已結算，棄回望題）**：開門＝出現綁 policy+audit 的 per-action 計價 eval pure-play 拿到規模營收；關門＝GitHub/orchestrator 把 eval/reconcile 原生內建（`notes/eval-ecosystem-niche.md`、`llm-call-niches` 卡、inbox 2026-06-28）。
- **安全/紅隊 eval 值不值得當個人差異化深入？**（`check:2026-08`）部分回應：頂尖攻擊能力會鎖在模型廠內部（Anthropic Mythos），個人差異化落在「驗證/整合/合規」側。**→ 結算訊號（07-05 改有時限檢索，堵可得性偏差）**：到期主動掃一輪案例（求職市場／獨立顧問／開源專案三處），掃到實例＝✅、掃不到＝⚪ 並評估撤題（`notes/anthropic-blog-2026-06.md`）。
- **MCP-as-a-rail（Hood）**（`check:2026-12`）→**傾向 ✅(已落地)**：Agentic Trading beta 上線(2026-05-27),MCP 當軌道、開放全部 27.5M 客戶、可接 Claude/ChatGPT/Cursor 任一平台下單；FINRA 年報首度定義「Trade Execution Agent」。孤狼先行,無第二家同等開放。**→ 結算訊號（07-05 換主訊號）**：Hood 是否改掉交易量計價，或出現第二家同等開放券商（測軌道護城河）；原「AI 操盤贏基準」降為 bonus——學術證據 LLM 選股無 alpha，窗內近不可觀察（`notes/robinhood-agentic-trading.md`、inbox 2026-06-28）。
- **語意 merge 閘門是可投資生態位？**（2026-06-16，`check:2026-09`）判決：大概率 feature 不是 company，同 eval/資安天花板。可投資表達式在外圍：擁 merge 地點的 incumbent / 合規 pure-play / 信任護城河。**→ 結算訊號**：是否出現獨立 merge-gate 公司拿到規模營收（反證我「feature 不是 company」），或被 GitHub/GitLab 原生吃掉（坐實）（`notes/agent-collab-infra.md`）。
- **agent 時代資安計價會崩？**（2026-06-07，`check:2026-10`）→**方向押反,拆兩段**：CRWD Q1 FY27(2026-06-03)net new ARR +32%、指引上修轉加速；PANW Next-Gen ARR +60%——agent＝greenfield 新增被保護對象,**per-seat 短期不崩**。但 per-agent 計價作為**新層**已落地(Okta for AI Agents 4-30 GA)。模型廠 cyber：Anthropic 偏合作(Project Glasswing,partner 含 CRWD/PANW)、OpenAI 偏自營。若 10 月只看「per-seat 崩沒」＝❌。**→ 結算訊號（07-05 拆雙軌，各自獨立判）**：軌a per-seat 鬆動＝CRWD/PANW NRR/單價趨勢轉弱；軌b per-agent 滲透＝定價頁出現 per-agent 條目或模型廠自營 cyber 上線。兩軌分記 ✅/❌，不合成一個是非題（`notes/ai-security-ecosystem.md`、inbox 2026-06-28）。
- **微軟地基何時消失？**（2026-06-15，`check:2026-12`）追蹤中。護城河三層（App 死→Graph→Entra），崩塌觸發＝learning loop 成主要 SoR 且住模型廠不住微軟。反諷：Nadella「擁有 learning loop」正是殺 Graph 的刀。**→ 結算訊號**：出現一個主流 agent 把「正本/learning loop」寫進模型廠側（非 Graph/Entra）的具體產品事件；反向則是 agent 寫入仍預設落 Graph（`notes/nadella-frontier-ecosystem.md`）。
- **Cursor 被收編後還中不中立？**（2026-06-20，`check:2026-09`）→**傾向 ✅(中立性明確劣化)**：SpaceX(已併 xAI)$60B 全股票收 Anysphere(2026-06-16,Q3 完成)；三向劣化——第三方 API 拆獨立計費池、Cursor 3 把 IDE 降 fallback/自家模型設 default、**Anthropic 已切斷 xAI 開發者經 Cursor 用 Claude**。Composer 3「從零預訓練」仍只有官方宣稱、無第三方驗證。**→ 結算訊號**：Cursor 是否仍預設可選 Claude/GPT（中立），或鎖成 Composer-only / 暗降非自家模型體驗（`notes/cursor-spacex-xai-composer3.md`、inbox 2026-06-28）。
- **harness 邊界之戰：loop/orchestration 住 harness 還是內化進模型？**（06-22＋06-27 兩條合併於 07-05 壓測，`check:2026-12`）現行判斷＝**兩層共存**：編排下沉進模型（Fugu GPQAD 95.1、OpenAI 併 Codex 單一 surface），但 harness 承載治理/工具/長任務且成現金牛（Claude Code run-rate 2 月過 $25 億）；若冒出獨立 loop 治理/verifier-as-a-service＝槓桿再外移一層（同 `llm-call-niches` 結構）。**→ 結算訊號（三態）**：❌被模型化＝Fugu 類跑分獲中立複現＋實測自搭 harness 取代不了；❌外移＝獨立治理層/verifier-as-a-service 拿到付費客戶；✅共存＝harness 廠營收/留存續強**且**編排持續下沉（兩者並見）；到期皆不明＝⚪。**跨條目註記（07-05）**：Codex/Cursor/Fugu 三線合看＝中立 harness 選項在收斂，`harness-beats-model` 卡已加「可換性」邊界（`notes/loop-engineering.md`、`notes/sakana-fugu-orchestration-as-model.md`、`notes/codex-agentic-shift.md`、`notes/prediction-ledger-stress-test.md`）。
- **Claude Design 對我的 ROI 待實測**（2026-06-14，`check:2026-07`）。契合的是看板/對外卡片/小紅書視覺；已選 personal_os 看板試點，待用戶跑一輪 handoff 回來。**→ 結算訊號**：用戶實跑一輪 personal_os 看板 handoff，回報「省時/視覺值不值得用」；到期仍未跑＝自動 ⚪＋問要不要換題（07-05 掛帳規則）（`notes/claude-design.md`）。
- **Mercor/RLHF 專家勞動供應鏈的 take-rate 會不會被 labs 內部化壓縮？**（2026-07-11，`check:2027-01`）追蹤中。GMV $20 億(2026-06)≠淨營收 $6-8 億；估值談判中衝 $200 億(2026-07-09)。**→ 結算訊號**：OpenAI/Anthropic 等是否加速自建全職 domain expert 團隊(內部化訊號)，或 Mercor 財報/融資揭露顯示 take-rate 被壓縮；反向則是外包持續擴大＝供應鏈層站穩（`notes/mercor-rlhf-labor-market.md`）。
- **Claude Certified Architect 認證值不值得考？**（2026-07-13，`check:2026-09`）追蹤中。已選定 Architect Foundations 軌（vs Developer，權重對既有卡重疊估 ~70%），三階段讀書計畫已定（對齊用詞→補 Domain2/4 缺口→官方 exam guide 對答案），還沒實際報名。**→ 結算訊號**：是否實際應考 + 結果；考後追蹤實質 ROI（有沒有人在意這張證、機會是否因此增加）而非信坊間「加薪 15-25%」說法；到期仍未報名＝自動 ⚪＋問要不要換題（07-05 掛帳規則）（`notes/claude-certification.md`）。

## 你可能感興趣的下一題（候選池）

- **動手複製 agent patterns**（已試一輪，2026-07-04）：orchestrator（強）+extraction workers（Haiku）+synthesis（Sonnet）跑通 daily-brief pipeline，四條 best practice 全驗證（見 `notes/prompting-small-models.md`）。**擱置固化**待材料源解鎖。剩：outcomes 迴圈（`/loop`+自寫判準）、個人迷你 eval golden set。
- **產業判讀線**：recall vs context length 才是長上下文真戰場？headless software 重塑軟體形態？中國開源排行榜當地緣訊號？
- **coding-agents 線**：Antigravity 第一方 vs 第三方優化差距？context 壓縮＝選擇性遺忘？trust accumulation 怎麼建？多主 session（對等）怎麼分工——誰持有正本、reconcile 衝突怎麼定序？（07-18 擱置待聊）
- **元主題**：卡片到 130 張會不會反難檢索？「待拆的卡」會不會變膨脹債務？時效卡半年後大量過期怎辦？
- **Fable 視窗待辦（07-05 全部收口）**：掃描＋前三任務＋預測帳 10 條修改＋one-sided-checks 升卡（coding-agents 第 18 張）皆落地。剩兩條已開單待新 session：fomo-kernel 鏡片對抗稽核（issue #120，工具＝cwc audit.md）、personal_os 架構 audit（`personal_os/tasks/personal-os-skill-architecture-audit.md`）。
- **fomo-kernel 架構深化（用戶 07-08 要「之後討論架構」,當場就開了第①題）**：拆多 vs 收斂一已辨析完。①意圖路由/彈性架構**已討論出設計**（正解 = 模組藏邊界下、agent 動態組 workflow、彈性放三旋鈕:意圖精細度/覆寫權/深度,成長連續不切檔;見 notes「更彈性的做法」節）——剩落地。②pre-trade gate 當第二入口③SKILL.md ~27k 瘦成 dispatcher <2k + mode 子檔案觸發才載（§28 已定未做）仍待討論 + 落地。**對外單一入口已拍板(版本 B,owner 07-08 定案)。eval「判斷交派紀律」= 獨立 issue 待開(建議開 fomo-kernel session 時開,先 `gh issue list` 查重)。** 屬 fomo-kernel repo 的活，認領才動（跨 repo + 並行紀律）。

## 你已沉澱的判斷（指向卡片）

- Harness 影響大於換模型 → `topics/coding-agents/cards/harness-beats-model.md`（Salesforce +79% 來自 review agent+skills；Google DevRel 也淡化 model＝利益相反方驗證）
- 工作流墊地板、模型抬天花板：蒸餾工作流拉高弱模型但封頂在其自身能力，價值與模型強度成反比（可證偽檢定：對強弱模型幫助一樣大＝抬天花板不是地板）→ `topics/coding-agents/cards/workflow-lifts-floor-model-sets-ceiling.md`（2026-07-17 Fable/fable-method 截圖；填 harness-beats-model 與 model-capability-capped-by-harness 之間缺口）
- Agent 協作媒介由拓撲決定：對等分布式走 git、主從同機才走共享終端 → `topics/coding-agents/cards/topology-decides-agent-collab-medium.md`（2026-07-18 tmux-bridge 截圖；補 agent-collab-infra 的 diff-not-cursor 隱藏變量＝拓撲，收錄 tmux-bridge 錯配案例）
- 讀 agentic 戰報先分「估計值 vs 實測值」，只信實測
- 讀信號，不讀表面數字 → `topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md`
- Eval 是跨模型裁判層，結構上該住模型廠外 → `topics/ai-industry-reading/cards/eval-is-a-cross-model-judge-layer.md`
- Eval 瓶頸是寫判準不是工具，所以個人能搞 agent eval → `topics/coding-agents/cards/eval-bottleneck-is-criteria-not-tooling.md`
- eval agent 判斷測的是「判斷的交派紀律」(該算下沉 engine／該問外包用戶／該收斂)不是正確性，判斷力可設計可測 → `topics/coding-agents/cards/eval-tests-judgment-triage-not-correctness.md`（2026-07-08 fomo 架構討論收束升卡；接 eval-bottleneck／agent-eval-scores／human-in-loop）
- 核心動作＝一次 LLM call 的生態位撐不成獨立公司，可投資表達式在外圍三件套 → `topics/ai-industry-reading/cards/llm-call-niches-are-features-not-companies.md`（2026-06-21 週綜合，eval/資安/merge 閘 ≥3 次同結構）
- 知識系統勝負手＝預編譯本地索引、按需 page-in，不重塞 context → `topics/coding-agents/cards/precompile-to-local-index-not-restuff-context.md`（2026-06-21 週綜合）
- 治理靠改預設而非設限，前提是預設接近 Pareto → `topics/ai-industry-reading/cards/defaults-not-restrictions-are-governance.md`（Block 非工程師交付工具＋Armstrong AI 成本砍半，2026-06-28；harness>model 的企業版，同構 repo 原則 #4／Issue #6）
- orchestration 內化成模型是對「harness 中立可換」的反論 → `topics/coding-agents/cards/orchestration-as-a-model-vs-neutral-harness.md`（Sakana Fugu，2026-06-22；劃出 harness-beats-model 的邊界）
- 其餘卡見 `README.md` 地圖（~33 張：ai-industry-reading 9、coding-agents 24）

## 你的工作偏好（我據此調整，不必每次重講）

- 討厭過度工程與儀式；要低門檻、先進 main 讓手機讀得到
- 過程中要多反問拿 feedback，別悶頭做完才報告
- 手機閱讀為主，格式不要破版
- 答案要誠實：做不到就直說、不粉飾；犯錯就認

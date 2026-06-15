# Nadella「Frontier Ecosystem」貼文：MSFT CEO 換個詞講 harness>model

> 來源：Satya Nadella 2026-06-14 個人貼文（X + LinkedIn），多家媒體報導。
> 入口是 Fox Hsiao 的中文轉述截圖（2026-06-15 給我看）。

## 一句話

微軟 CEO 用「learning loop / token capital」這套新詞，等於公開背書了我 repo 裡最深的判斷——**harness > model**：護城河不是選到最強模型，是在模型之上建持續複利的學習系統。

## 他到底講了什麼

標題核心句：**沒有生態系支撐的前緣，無法長久**（a frontier without ecosystem support will not lead to a stable future）。

兩個關鍵詞：
- **Human capital（人力資本）**：人的知識、判斷、關係、創造力、模式辨識
- **Token capital（代幣資本）**：公司自己擁有、累積的 AI 能力

主張：真正的機會不是「挑最強模型」，是在模型之上建一個 **learning loop（學習迴圈）**，讓 human capital 跟 token capital 互相複利、把 institutional knowledge 沉澱下來。底層通用模型是可替換的——技術一變就換掉，但你累積的學習系統留著。他呼籲的是 **frontier ecosystem**：價值分散到各公司／產業／國家，不被少數大模型吃掉。

## 這篇和微軟有關係嗎？有，是「利益相反」那種關係

不是中立的產業觀察，是 **MSFT 的戰略定位用第一人稱包裝**。看誰講、站哪賺錢就懂：

1. **微軟在模型層是弱勢方**。前緣模型主要靠 OpenAI，自家 MAI 還沒到第一梯隊。所以「別賭單一模型、模型可替換、真正的價值在生態系/學習迴圈」這套話，**剛好把戰場從他輸的地方（model）移到他贏的地方（platform）**。
2. **他贏的地方正好就是「learning loop」需要的基礎設施**：Copilot、Foundry/Agent 平台、Entra/Graph 的身份與資料護城河、agentic systems。他講的「每個組織該擁有自己的學習迴圈」——賣鏟子的人正好賣那把鏟子。
3. 所以這跟 Google DevRel 在 I/O 淡化 model 是**同一個套路**：模型不是你的強項時，就論述「model 不重要、上層才重要」。利益相反方的論述要打折讀。

## 為什麼這篇對我有價值（不是因為它「對」，是因為「誰在講」）

- 我自己早就有 `harness-beats-model` 卡。Nadella 講的沒有新東西。
- **價值在錨點**：連 MSFT CEO 都用官方戰略高度講這套，代表「harness>model」不是 coding-agent 小圈子的偏見，是產業共識正在成形。
- 但要保持清醒：**他講這話正因為他需要這話是真的**。最強的第三方驗證是 Google DevRel（利益相反方淡化自家強項才可信）；Nadella 是利益**相同**方（淡化自家弱項），證據力反而較弱。兩種都記，但分清楚。

## 連到既有判斷

- → `topics/coding-agents/cards/harness-beats-model.md`（這篇是它的 CEO 級錨點）
- → `topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md`（讀「誰講、站哪賺錢」而非表面論述）
- → MSFT × OpenAI super app 線：這篇基本是那個論述的母版——平台×模型乘積、Graph/Entra 護城河、模型可替換
- ↔ 對比 `notes/gemini-api-platform-shift.md`（Google 淡化 model 是利益相反方=可信；Nadella 淡化 model 是利益相同方=要打折）

## 微軟的 harness 到底行不行（2026-06-15 補）

把 harness 拆兩種看：

**① Coding harness（Copilot 寫程式）— 輸得明顯**
- 資深開發者 46% 選 Claude Code，只 9% 選 Copilot（JetBrains 2026）
- Copilot 在 Stack Overflow 從 67%→51%，成長停滯、品質被嫌
- Claude Code 拿 42% 企業 coding 工作量
- 最殺：**微軟自家工程師偏好 Claude Code，公司卻令 6/30 前強制遷回 Copilot CLI**。自家人用腳投票投對手。

**② 企業 agent 平台（M365 Copilot / Copilot Studio / Foundry）— 強在地基不在手藝**
- **鐵證數字：員工同時有 ChatGPT/Gemini 時，M365 Copilot 活躍使用掉到 8%；當它是唯一選項才升到 68%**。採用是「被綁的」不是「賺來的」。
- Foundry 被評「a cathedral of knobs」——旋鈕大教堂，彈性換來決策疲勞。
- Copilot Studio 連 temperature/prompt 版本/eval gate 都調不了，要跳 Foundry。

**結論**：微軟真正的護城河不是 harness 做得好，是 Graph/Entra 的身份+資料地基 + 散佈通路。他淡化 model（弱項）、主打 learning loop（地基強項）——但 learning loop 裡的「harness 產品力」其實也是弱項，靠強通路塞弱產品。**讀使用率，不讀論述。**

## 連地基都會消失嗎？三層 + 崩塌觸發（2026-06-15）

微軟護城河疊三層，AI 由上往下逐層融化：
1. **App 層**（Office UI）：已在死，退化成 agent 的渲染目標。Nadella 自承 Copilot 是新 UI。
2. **資料地基**（Microsoft Graph）：靠 data gravity，還活著。
3. **身份層**（Entra）：最硬，agent 要授權就得過。

「連地基消失」= 問 2、3 何時死。三個觸發場景：

- **A. system of record 搬家（最致命）**：agent-first 後，正本「決定了什麼、為什麼」是 agent 的 memory/learning loop。若它住模型廠不住 Copilot/Foundry，Graph 退化成要遷出的 legacy 資料湖。← 這就是本 repo「repo 是我的腦」放大到企業。
- **B. 協定商品化存取（MCP 線）**：MCP 讓 agent 對 SharePoint / Notion / Drive 用同一通用連接器平等存取，Graph 從「統一 API」變「眾多 MCP server 之一」。摩擦歸零=護城河歸零。接 Robinhood「軌道會被商品化」母題。
- **C. 身份脫鉤**：非人類/agent 身份標準若由模型廠居中經紀授權，Entra 收費站搬走。

**同時打穿三層的條件**：當 agent 的 learning loop 成為主要 system of record，且住在模型廠、不在微軟。

**最大反諷**：Nadella「擁有你的 learning loop」這句，正是會殺死微軟地基的刀——learning loop 就是新 system of record，戰爭在「它的記憶住哪、誰經紀」。他拼命要它累積在 Copilot/Foundry，正因清楚累積在別處 Graph 就是融化的冰。force-bundle（8%/68%）就是冰在融的徵兆。

**AI 世代還需不需要 M365**：需要的是「地基」不是「app」；agent 要 grounding（讀信、知道你是誰、過合規），今天最便宜供應商是 Graph+Entra。但那是 grounding 需求不是忠誠——一旦 grounding 能從遷移後正本或標準連接器拿到，需求蒸發。一句話：**現在需要它的基板、不需要它的 app；等 SoR 搬到 agent 記憶層 + 協定商品化後，連基板都不需要。**

**領先指標（一起追蹤）**：
- 正本在哪累積：團隊「決策＋理由」長在 Copilot/Claude/ChatGPT memory 還是 SharePoint？（A）
- agent 碰 SharePoint 跟碰 Notion/Drive 是否無差別連接器？（B）
- agent 身份由 Entra 發還是中立/模型廠層發？（C）
- force-bundle 是否變兇＋內部工程師是否持續叛逃非微軟工具（基板叛逃最前緣）

## 待追

- 「token capital」會不會變成 MSFT 接下來產品線的官方話術（Foundry/Copilot 行銷）？如果是，更證明這篇是戰略文不是觀察文。
- learning loop 這詞跟 Karpathy LLM wiki、跟這個 repo 的「repo 是我的腦」其實是同一物種——只是他講組織層、我做個人層。

## 來源

- BusinessToday / Benzinga / ANI News（2026-06-14 Nadella 貼文報導）
- FourWeekMBA「Nadella Just Described Harness Theory Without Naming It」
- JetBrains 2026 開發者調查、Stack Overflow 2026、Code Culture（MSFT 工程師偏好 Claude Code 卻被遷回 Copilot）

# Salesforce「全公司 agentic 化」案例（Claude Code）

> 2026-05-30 研究。起點：Boris Cherny（Claude Code 作者）轉 Salesforce 工程長 Srinivas Tallapragada 的長文〈How Salesforce Engineering Became Truly Agentic〉。台灣工程圈（Will 保哥）的吐槽：「這種案子在台灣大概要 231 天的 PoC 才會開工。」

## 一句話

Salesforce 把整個工程組織切換到「以 agent 驅動 SDLC」，用 Claude Code 當主力 agent、給全體工程師無限 token；對外丟出一個 231→13 天的遷移案例當招牌。但真正的信號不在那個招牌數字，在底下兩個「被量到」的數字和一套重新設計的工作流。

## 招牌案例（要拆穿著看）

- 任務：把 **33 個 API endpoint** 遷移到新的 cloud-native 架構。
- 傳統估計：約 **231 人天**（每個 API 約 7 天）。
- 實際：**13 天**完成 → 號稱約 **18 倍**快。
- 產出：總共 **5 個 PR**；其中最大的一個 PR 一次交付 **21 個 endpoint**，並達到完整測試覆蓋。
  （Boris 的推文把它壓縮成「一個 PR 21 個端點、100% 覆蓋」，原文是 5 個 PR 的總遷移，21 是單一最大 PR。）

**為什麼這個招牌要打折看**：231 天是 Salesforce 自己的「反事實估計」（counterfactual），不是真的跑過一次。基準線是自己訂的，最容易灌水的就是這種「本來要多久」。所以 18x 是公關數字，不是可驗證數字。

## 真正耐看的兩個數字（這兩個是「量到的」）

1. **每位開發者 merge 的 PR 數 +79%**（2026/4 對比 2025/4，全組織）。這是年對年實測，比 18x 可信。
2. **事故率 -5%**：PR 暴增的同時事故反而降。這直接打掉「踩油門就會爆」的直覺反駁——前提是信他們的內部監控。

讀法：與其記「快 18 倍」，不如記「吞吐量 +79%、事故 -5%」。前者是故事，後者是信號。

## 真正的故事：不是模型變強，是工作流被重建

外界容易把它讀成「Claude 很聰明所以快」，但原文的重點是**組織級 harness 的重新設計**：

- **Code review agent 進迴圈**：所有 branch 上的程式碼在開 PR 前先被一個 review agent 審。這個 agent 是**唯讀的、永不改 code**。判決三種：APPROVED / APPROVED WITH WARNINGS / CHANGES REQUIRED。要改就把具體問題丟回 developer agent 改完再自動重審。
- **Skills 成為新的工程資產**：把團隊脈絡、命名慣例、workflow pattern 打包成可重用的 Claude Code skill。工程師從「工具使用者」變成「自己 agentic workflow 的建造者」。
- **AI Expert Suite + Foundation Plugins**：針對 Salesforce 自家任務 curate 的 skill 庫，內部 benchmark 顯示準確度/可靠度上升、成本下降。
- **無限 token**：拿掉用量焦慮，讓 agent 敢長跑。

→ 這條直接呼應既有判斷「Harness 影響大於換模型」。產生 +79% 的不是 Claude 本身，是 review agent + skills + 無限 token 這套外圍結構。

## 連工程長自己都承認的難題（這段最值得信）

Tallapragada 不藏問題，稱它們「genuinely hard」：

- **長 agentic session 的 context 管理**還是門需要工程師學的手藝（會漂、會塞爆）。
- 模型仍會 drift / hallucinate；review、驗證、操作護欄不會消失，反而更重要。
- checkpoint（diff review、dry-run、確認閘門）會稍微拖慢流程，但這正是「人的判斷接進自動執行」的接點。

## 外界質疑（一句話版）

- 所有數字都是 Salesforce 內部數據，**無法被獨立驗證**。
- 231 天基準是自估，招牌比值天生可疑。
- 這是一篇工程行銷文（順帶賣 Agentforce / MCP 生態），讀的時候要扣掉 marketing。

## Will 保哥那句吐槽的點

「這種案子在台灣大概要 231 天的 PoC 才會開工」——點到一個真問題：**很多組織的瓶頸不在寫 code，在組織摩擦**（審批、PoC、決策流程）。Salesforce 能 13 天做完，前提之一是高層直接拍板全公司切換、給無限 token、容許重建工作流。工具到位 ≠ 收益到位，組織願不願意改工作流才是變數。

## 我（使用者）可帶走的判斷

1. 看 agentic 戰報先分「估計值 vs 實測值」：231→13 是估計，+79%/-5% 是實測，只信後者。
2. 收益來自**重建工作流 + harness**，不是換更強的模型。複製這個案例要複製的是 review agent loop 和 skills 機制，不是「買 Claude Code」。
3. 真正的瓶頸常在組織層（敢不敢給無限 token、敢不敢拆掉舊流程），不在技術層。

## 出處
- Salesforce 官方：〈How Salesforce Engineering Became Truly Agentic〉(salesforce.com/news/stories/how-engineering-became-agentic/)，作者 Srinivas Tallapragada，2026-05
- The Decoder 報導與質疑：the-decoder.com/salesforce-claims-ai-agents-cut-a-231-day-migration-to-13-days-with-fewer-incidents/
- Hawkdive、salesforcemonday 的細節整理
- 緣起：Boris Cherny (@bcherny) 推文轉述

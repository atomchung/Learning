# Mistral Studio：Prompt/Skill 版本管理的 best practice

2026-07-23 隨口丟連結：`mistral.ai/news/manage-prompts-and-skills-in-studio/`，問這篇在講的 best practice 是什麼。

**一句話**：Studio 把 prompt 和 skill 當正式生產資產治理——不可變版本、具名 owner+audit log、staging→production 用 label 促升可接 CI/CD。

## 內容

### Prompt vs Skill，兩種顆粒度

- **Prompt**：單純可重用的文字/指令。
- **Skill**：「何時該用」+ 方法本身 + 選配檔案（範例、模板、參考資料）——比 prompt 多一層觸發判準跟附件，更接近一個小型能力包。

### 版本控制

- 每個版本**不可變**（immutable）：已上線的版本不能被偷改，紀錄永遠對得上實際跑過的東西。
- 可以 diff 任兩版、看差異，幾分鐘內回滾到已知穩定版。

### Ownership + audit trail

- 每個資產有具名 owner。
- 每次變更記錄「誰在什麼時候改了什麼」。

### Staging → Production

- 上生產前要過企業既有的測試/審批流程。
- 用簡單的 label（例如 promote 到 `stable` alias）觸發 CI/CD——文件提到可透過 SDK 接 GitHub Actions。
- 本質：把 prompt/skill 當生產資產治理，不是隨手改的文字。

## 坑（取得方式的限制）

WebFetch 對 `mistral.ai` 直接 403（雲端環境白名單制），內容是靠 WebSearch 兩輪拼出的摘要，不是讀原文全文。細節建議之後手機開原文核一次。

## 接既有線

跟 `llm-call-niches-are-features-not-companies` 卡同構：prompt-ops（版本控制/staging/audit，原本 PromptLayer/Langfuse 這類工具站的位置）被模型廠（Mistral）原生收編進自家 Studio，是這張卡的新例證——只是這次主體是 devops 外圍層，不是 eval。（連結先記著，尚未正式掛上卡片，待重複出現或用戶要求再升。）

## 出處

- [Version control for prompts & skills in Studio](https://mistral.ai/news/manage-prompts-and-skills-in-studio/)（原文，WebFetch 被擋，以下靠搜尋摘要交叉）
- 搜尋摘要來源：docs.mistral.ai/getting-started/quickstarts/studio/create-skill、docs.mistral.ai/getting-started/quickstarts/studio/create-reusable-prompt、mistral.ai/products/studio/

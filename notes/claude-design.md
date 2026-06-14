# Claude Design：Anthropic 給非工程師的原型 surface

來源：Duolingo design/product 團隊（Caitlin Brisson、Sarah Deitke、Nickey Skarstad）寫的內部 workshop 講義（Google Doc，2026-06 讀）。**注意是外部公司教自己團隊用的版本，不是 Anthropic 官方文件** → 本身就是 adoption 訊號：真實公司已經把它編進 design onboarding。

學這題的原因：Anthropic 在 Claude Code 之外的第二條 agent 產品線。咬合我在追的三條線——「非工程師怎麼變 power user」、「harness > model」、Anthropic 終端深度策略。

## 一句話

餵它一個 design system，prompt 一個想法，吐出可互動的 HTML 原型；在 live 原型上直接點著改，做完一鍵**單向** handoff 給 Claude Code。本質是把「做原型」從工程師下放給 designer / PM。live 在 claude.ai/design，還在 Research Preview（很早）。

## 核心機制

- **HTML-first**：產物全是純 HTML/CSS/JS/圖，無框架綁定。
- **在 live 原型上直接改**：點元素留 comment、用 Knobs 拉 slider 調間距字色——文件說這是相對 Claude Code「最大的解鎖」，不用回去重 prompt。
- **單向 handoff 給 Claude Code**：打包成 zip（HTML + assets + README）。刻意單向——快速視覺迭代在 Design 做，要接真資料/後端/版控才進 Code，回不去。
- **Design System = 五種 skill 的 bundle**：Brand / UI Kit / Element / Skill / Template。
- **被低估的 power moves**：原型可 zero-config 直接呼叫 Claude API（內建 chatbot/summarizer，無後端）、Capture web element 一鍵逆向任何公開網站的 styling、「Make this tweakable」把靜態 mock 變 stakeholder 可調的 demo。
- **還很早**：design system recall 不可靠（會丟顏色、自己發明 pattern）、高保真/向量弱、無 arbitrary MCP（跑自己的 tool loop）。

## 對我的興趣線

- **非工程師 power user**：這是 Anthropic 親自下場的答案——同一套底層 agent，換一個視覺 harness，不寫 code 也能產可點擊原型。
- **harness > model**：同模型、兩套 harness（Design = 視覺迴圈、Code = repo 迴圈），差別在服務誰、服務哪個成熟度。那條單向線 = 產品刻意劃的「原型 vs 生產」邊界，不是技術限制。呼應 [harness-beats-model](../topics/coding-agents/cards/harness-beats-model.md)。
- **Anthropic 終端深度**：從工程師終端，往 designer/PM 終端擴。

## 對我自己產品的應用（2026-06-14 討論）

**誠實前提**：我大半產品是 CLI / 後端 / Markdown / 自動化，根本沒有視覺層 → Claude Design 對它們是**錯配，別硬塞**。

**真正的錯配不在工具，在我的工作流沒有「設計階段」**：我習慣想到就用 Claude Code 直接寫，長什麼樣算什麼樣。Claude Design 插的位置是「動手寫 code 之前」——先快速試幾個視覺/UX 方向，選定再 handoff。我用不上，主因是這個階段在我的流程裡不存在，不是工具不行。

**真正用得上的場景**（按 ROI 排）：
1. **天天自己看的**：personal_os 看板、stock dashboard——看一年的東西，花一次把它變好看，天天受益。
2. **要對外分發的**：trade_review 復盤卡（要收反饋，視覺第一印象影響採用）、job/ 作品集。
3. **內容平台產物**：小紅書圖文 mock（crewai_xhs / rednote_analysis 產的是要發到視覺平台的東西）。
4. **0→1 新產品的 UI 探索**：投入 Code 前先看到幾個方向。

**Caveat**：stock 是 Streamlit，UI 框架綁定。用 Claude Design 重做要付「脫離 Streamlit、自己重接資料」的成本，不是無痛 handoff。偏 web/HTML 的東西（看板、對外卡片）契合度高很多。

**結論**：對我這種「瓶頸在功能與知識、不在視覺」的一人開發者，Claude Design 大概不是天天用的核心工具，而是「偶爾要做對外/視覺東西時，省我從零刻 UI」的加速器。

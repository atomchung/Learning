# addyosmani/agent-skills 優缺點筆記

> 2026-07-08。來源：手機截圖轉發（吉英说事，引用 @Granite0x 推文）→ 追查原 repo。
> `https://github.com/addyosmani/agent-skills`，作者 Addy Osmani（Google Gemini 工程負責人、前 Chrome DevTools lead）。MIT 授權，GitHub Trending 全站第一，69k+ star。

## 是什麼

把「資深工程師寫程式的紀律」編碼成可插拔的技能包，給 AI coding agent 用。核心是 24 個技能（23 生命週期 + 1 meta-skill）＋ 8 個對應開發生命週期的 slash command：`/spec /plan /build /test /review /webperf /code-simplify /ship`。同一套內容適配多個工具（Claude Code、Gemini CLI、Cursor、Windsurf、Antigravity、Copilot、OpenCode…70+），用 `npx skills add addyosmani/agent-skills` 一鍵裝。

Gemini CLI 版本用 TOML 定義 command（`.gemini/commands/*.toml`），Claude Code 版本用 markdown skill 檔——內容邏輯一致，只是格式跟著工具走。

## 優點

- **紀律具體到可執行**：不是空泛的「寫好程式碼」，`/build` 這類指令把流程寫死成「紅燈→綠燈→回歸測試→build→commit→標記完成」，一個 task 一個 commit，隨時可乾淨回滾。
- **高風險操作強制人工把關**：自動模式（`/build auto`）遇到權限/金流/刪除/部署/密鑰相關改動會停下來要人簽核，不會一路衝到底。這跟我們自己在 `notes/repo-best-practices-scan-2026-07.md` 記的「self-improvement 要 propose-and-test、不能無條件自我編輯」是同一個原則的不同實作。
- **兩層載入設計**：技能按需啟動（省 context window）+ 核心技能寫進 CLAUDE.md/GEMINI.md 常駐——跟我們自己「筆記層 vs 卡片層」「profile 常駐索引 vs inbox/notes 冷 grep」是同構的分層邏輯，算業界獨立收斂到類似解法。
- **跨工具可攜**：同一套技能定義能力，格式翻譯給不同 CLI，降低「換工具要重寫一套流程」的成本。
- **作者背景可信**：資深一線工程師開源自用配置，不是行銷包裝，可信度較高。

## 缺點 / 風險

- **看不到 eval 驗證迴圈**：目前查到的文件只講「技能內容是什麼、怎麼裝」，沒有展示他們怎麼量測這套技能實際提升了什麼指標。跟我們自己 `notes/skills-workflow-best-practices.md` 強調「eval 是持續迭代迴圈，不是一次性動作」的立場對照，這套目前只看得到「產出」，看不到「驗證」。
- **通用模板 ≠ 貼合你的專案**：技能是「資深工程師的一般性最佳實踐」，不是針對特定 codebase 的實際慣例。套用前仍需要驗證跟自己專案的實際規則（測試框架、commit 規範等）沒有衝突。
- **格式鎖定成本**：Gemini 用 TOML、Claude Code 用 markdown，若要客製化並讓多工具同步，得維護多份格式、手動對齊，不是單一來源。
- **69k star 是熱度訊號不是效果訊號**：GitHub trending 第一容易來自社群媒體擴散（截圖來源本身就是一條轉發鏈：X 推文 → 中文自媒體轉述 → 手機截圖），不代表已驗證的生產力提升。要信的話,自己需要小規模跑一輪再擴大用,不能只憑 star 數採信。
- **完整生命週期流程可能對小型/個人專案過重**：`spec → plan → build → test → review → ship` 六階段的儀式感，適合團隊協作專案；對這種個人知識庫（Learning repo）這類低門檻優先的場景，可能是過度工程。

## 一句話結論

這套東西的「紀律具體化 + 分層載入 + 高風險強制人工把關」值得參考，但它目前是「別人聲稱有效的模板」，不是「已被驗證有效的方法」——採用前該先小範圍試跑,而不是因為 star 數高就整套搬進來。

## 對照 fomo-kernel:為何他拆多、我收斂一(2026-07-08)

追問延伸:「該把生命週期切成不同 skill 嗎?」不是風格選擇,是 domain 結構決定的。**同一把判準尺,兩個系統讀出相反落點。**

決定「拆多 vs 收斂一」的三個正交判準:
1. **階段本質**:N 個知識不重疊的獨立能力(→拆),還是 1 件事的 N 道工序(→合)?
2. **誰編排**:使用者自己隨機進入、順序建議性(→拆),還是產品替使用者一次走完、順序強制性(→合)?
3. **狀態住哪**:檔案系統冷讀、拆開不斷鏈(→拆),還是 skill 的跨 session 記憶迴圈、拆開就斷鏈(→合)?

addyosmani(coding)三個全落「拆」:8 階段是 8 個獨立能力領域(spec / webperf / review 知識不交集)、工程師自己編排、狀態在 repo 檔案。fomo-kernel(復盤)三個全落「合」:四步共享同一份交易資料+鏡片+記憶、散戶不懂流程由產品編排、狀態是本機 `~/.trade-coach/` 熱記憶。

**一句話收斂**:skill 數 = 使用者會單獨想要的動詞數。coding 有 8 個(review / ship 各自是入口意圖),交易復盤只有 1 個(「復盤」;四步是看不見的內部工序)。

**元判斷(不會過期的那層)**:兩邊都在切生命週期,只是切在不同高度——addyosmani 切在 **skill 層**(task = 使用者入口意圖),fomo-kernel 切在 **mode 層**(task = 內部工序,SKILL.md 該瘦成 dispatcher + mode 子檔案觸發才載)。「拆多」用在單一迴圈型 domain 會製造觸發歧義——fomo-kernel 的 `docs/research-skill-vs-agent-loop.md` §28 已獨立否決,稱之為 investment_note 老路。

**借鑑收斂**:fomo-kernel 這題大多已獨立收斂,addyosmani 的真正用途是三種參照——① 背書「漸進載入」(SKILL.md ~27k 全量載入 → dispatcher,§28 已定未做);② 反向驗證「對外單一入口」是對的(別學拆 8 個指令);③ 別退化——eval 驗證迴圈是 addyosmani 的缺、卻是 fomo-kernel 的強項。

## 出處

- 原 repo：`https://github.com/addyosmani/agent-skills`
- Gemini CLI 設定文件：`docs/gemini-cli-setup.md`（repo 內）
- 對照：`notes/skills-workflow-best-practices.md`、`notes/repo-best-practices-scan-2026-07.md`

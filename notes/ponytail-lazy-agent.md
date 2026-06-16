# Ponytail：教 AI agent「少寫程式碼」的插件，有沒有用？

來源：ExplainThis 軟體工程白話聊貼文（2026-06）介紹的 GitHub 熱門開源專案。
原 repo：`DietrichGebert/ponytail`（MIT、~10k stars）。問題：這玩意有沒有用？

## 它到底是什麼

一句話：**它不是程式，是一包 prompt / ruleset**。把「像最懶的資深工程師那樣思考」寫成 markdown 規則 + 各平台 adapter，塞進 agent 的 context。

核心是一條決策階梯，agent 寫任何 code 前先逐級問，停在第一個成立的：
1. 這東西需要存在嗎？不需要 → 跳過
2. 標準函式庫做得到嗎？→ 用它
3. 平台原生功能有嗎？→ 用它
4. 已安裝的依賴有嗎？→ 用它
5. 能一行解決嗎？→ 一行
6. 都不行 → 寫剛好能動的最小量

附帶守則「lazy 但不 negligent」：信任邊界驗證、資料遺失處理、安全、無障礙——這些不准砍。

支援 Claude Code、Cursor、Windsurf、Cline、Copilot、Aider、Codex 等 13+ 平台，靠的就是不同平台的規則檔。

## 它宣稱的數字

作者自測：3 個模型（Haiku/Sonnet/Opus）× 5 個 coding 任務，每格跑 10 次取中位數，用 promptfoo。
- 程式碼量少 80–94%
- 速度快 3–6 倍
- 成本降 47–77%（token 少）

## 我的判斷：有沒有用？

**核心觀念是真的，數字要打折。**

**真的部分**：AI agent 過度生成、過度抽象、重造輪子是公認的失敗模式。一條「先找理由不要寫」的規則確實能砍掉 bloat、省 token。這方向沒錯。

**要打折的部分**：80–94% 那串是**作者自己挑的 5 個任務、自己跑的 benchmark**——屬「估計值/行銷數字」，不是第三方實測。套我自己的判準（讀 agentic 戰報先分估計值 vs 實測值，只信實測），這串數字當「上限、行銷錨點」看，別當「你會拿到的結果」。HN 上也有人酸「這專案本質就是 README 裡一個 code block」。

**最大的價值其實在 meta 層**：這是 **harness > model 的又一個教科書案例**——一份 markdown 規則改變 agent 行為的幅度，大過你換一個模型。它證明的不是「Ponytail 多神」，而是「**行為住在 harness 裡,不住在模型裡**」。

## 對我實際有沒有用

1. **可直接抄**：MIT、純 prompt。那條 6 級決策階梯可以直接搬進我自己的 `CLAUDE.md` / skill，不需要裝整包。價值在 idea 不在 package。
2. **當證據**：補強 harness>model 卡片，和 Salesforce(+79% 來自 skills 不是換模型)、Google DevRel 淡化 model 同一組。
3. **風險提醒**：「少寫 code」是優化一個 proxy 指標（行數/token）。可以被 game——該抽象的不抽象、該防的邊界偷懶,會換來日後維護債。所以它把安全/驗證列為「不准砍」是對的設計,但實戰要盯有沒有為了好看數字而 under-build。

## 一句話收

有用,但用法是「抄那條決策階梯進自己的 harness + 當 harness>model 的證據」,不是「相信它省 77% 成本」。它最誠實的貢獻是再次證明:**改 prompt 比換模型槓桿大**。

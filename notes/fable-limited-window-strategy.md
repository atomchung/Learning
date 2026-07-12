# Fable 可能隨時被下架：怎麼分配這段有限時間

問題起點：讀完「跟 Fable 找未知」那篇心法後追問——如果之後再也用不了 Fable，該怎麼在有限時間內用好這個模型（找問題/解法/未來方向）？

## 查證：風險有前例，不是假設性焦慮（2026-07-05 查）

Fable 5 是 2026-06-09 首次公開發布的 Mythos-class 模型，Anthropic 目前推理/長任務 agentic 能力最強的通用模型。發布沒幾天，6/12 美國政府因 Amazon 研究員發現的越獄漏洞發出出口管制令，Anthropic **全球下架** Fable 5 與 Mythos 5，停了 18 天，6/30 管制解除、7/1 才重新對外開放。定價 $10/M input、$50/M output（含 90% prompt cache 折扣）。

**結論**：觸發下架的變數（監管/安全事件）不是使用者能控制的，而且已經應驗過一次。這代表「有限視窗」是真實約束，該當成規劃前提，不是杞人憂天。

## 三塊分配框架

1. **找問題（判斷力/盲點）**：把 Fable 用在弱模型做不好的地方——深度 audit、跨主題找矛盾、盲點檢視（呼應 `notes/finding-unknowns-with-claude.md` 的「盲點檢視」招）。產出是「寫下來的問題陳述」，寫完就是持久資產，不需要 Fable 本人執行後續。
2. **解法（拿計畫，不拿執行）**：優先讓 Fable 產出實作計畫/架構決策，機械式重構留給以後任何模型都能做。同構既有判斷：委派契約 + Prompting Inversion（強模型該少約束做判斷型工作，弱模型才該給死板約束跑 execution，`notes/prompting-small-models.md`）。
3. **未來方向（現在做，別延後）**：跨主題綜合/路線圖這種「模型能力差距最大」的工作要現在做完，別想「以後還能問」。

**一句話**：harness > model 判斷的極端版——把 Fable 的產出寫進 repo（notes/cards）才是真正持久的資產，模型本身隨時可能被監管收走。

## 逐專案 × Fable 用法（2026-07-05 全專案掃描，取代原 2 條候選）

掃了 Side_project 全部 26 個資料夾（按最近修改時間分活躍度），按「判斷密度 × 產出持久性」分層：

**高價值（值得花視窗）**
- `Learning/`（本 repo）：Issue #6「遞迴改進 harness」完整梳理；loop eng / orchestration 兩條 `check:2026-12` 長期線深度綜合——「未來方向現在做」頭號標的
- `investment_note/`：**預測帳對撞**——跨條目找互相矛盾的判斷、共用隱含假設的條目群、結算訊號缺陷；已有 fact-checker agent（10/10 驗證過）可組「Fable 產判斷 → fact-checker 驗證」迴圈
- `kol_collector/fomo-kernel/`：VY 鏡片判準的**對抗性測試**（極端 CSV 看誤判）＋ golden set；判準設計＝eval-bottleneck-is-criteria 的實戰場
- `cwc-workshops/`（2026-07-05 新入，Anthropic 官方 workshop 材料）：**對讀**不照跑——官方教法 vs 已沉澱卡片找差異；重點 eval-driven-agent-development / agents-that-remember / rightmodel / agent-decomposition
- `personal_os/`：一次性**架構 audit**（skill 間資料流、frontmatter 契約、rot 風險），產出問題陳述＋計畫就停

**中價值（單一明確任務）**
- `info_collector/`：Fable 當每週 offline optimizer（看失敗軌跡改 prompt 檔）；材料源解鎖前不急
- `_ai_memory/`：跨錯誤找 pattern，併進 meta-review 線
- `playground/`：新原型 Fable 出架構計畫、執行給便宜模型

**低價值／不動**：小紅書組（靜置；若重啟先做「品味 externalize 成 rubric」盲點檢視）、stock（機械性高）、基建組（mcp / n8n / claude-plugins / session-records / ccstory，弱模型夠）、歸檔組不花視窗。

**優先序**：Learning 綜合 → investment_note 對撞 → fomo-kernel 鏡片測試 → cwc-workshops 對讀 → personal_os audit。

**進度（2026-07-05）**：前三條中的 1、2、4（Learning / 對撞 / 對讀）已在雲端 session 執行，且同步用 Opus 4.8 subagent 跑相同任務卡做模型 A/B——結果見各產出 note 與 inbox。

## 出處

WebSearch（2026-07-05）：Anthropic 官方新聞稿 + VentureBeat + The Hacker News 對 Fable 5 下架/恢復時間線的報導。

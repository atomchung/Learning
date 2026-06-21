---
type: starting-point
topic: ai-industry-reading
created: 2026-05-30
status: expanding
---

# 起點：我想用什麼信號判讀 AI 產業走向

> 磁鐵卡。投資/產業判讀的素材先塞進來，看出可重用的判斷時再拆成卡。
> 來源筆記：`notes/model-progress-roadmap.md`、`notes/hugging-face-exploration.md`、`notes/agent-os-market-analysis.md`、`notes/ai-daily-brief-7-episodes.md`

## 當下的核心問題
- 模型能力趨同後，產業的價值與利潤會往哪裡流？
- 哪些「信號」比廠商行銷更早預示趨勢？
- 這條線和 `coding-agents` 的核心命題（harness > model）怎麼接？

## 已拆出的卡（9 張）

### 元判斷（統攝其他卡）
- [read-signals-not-surface-numbers](./cards/read-signals-not-surface-numbers.md) — 讀信號，不讀表面數字
- [llm-call-niches-are-features-not-companies](./cards/llm-call-niches-are-features-not-companies.md) — 核心動作只是一次 LLM call 的生態位，撐不成獨立公司（2026-06-21 週綜合）

### 信號方法論
- [benchmark-saturation-hides-real-gap](./cards/benchmark-saturation-hides-real-gap.md) — 跑分飽和時，真實能力 gap 才是訊號
- [open-source-is-the-commoditization-clock](./cards/open-source-is-the-commoditization-clock.md) — 開源復現速度是商品化的計時器

### 價值流向
- [value-flows-to-the-relational-sector](./cards/value-flows-to-the-relational-sector.md) — AI 商品化後，價值流向「關係型部門」
- [structure-not-portability-is-agent-os-value](./cards/structure-not-portability-is-agent-os-value.md) — Agent OS 的真值是強迫結構化，不是跨工具

### Eval 生態位（2026-06，從 promptfoo 收購反推）
- [eval-is-a-cross-model-judge-layer](./cards/eval-is-a-cross-model-judge-layer.md) — Eval 是跨模型裁判層，結構上不該屬於模型廠
- [acquiring-neutral-tools-buys-distribution](./cards/acquiring-neutral-tools-buys-distribution.md) — 收購中立工具，買的是分發通路與安全，不是功能
- [eval-bifurcates-correctness-vs-security](./cards/eval-bifurcates-correctness-vs-security.md) — Eval 分岔：正確性測量商品化，安全紅隊升值

## 還沒拆但累積中的發現
- Context window 1000× 擴張，但戰場已從「長度」轉到「recall 準確率」
- 中國開源模型佔 HF 排行榜 8/10，下載量首超美國 → 實力被市場低估的訊號
- GPT-5.5 賣點是「自己撐完長任務」的質變，不是單一 benchmark
- Headless software：軟體從 UI 優先轉向 API/agent 優先
- inference 價格因開源壓力持續暴跌（千問 3.5 用 5% 成本達 Gemini 3 效能）

## 下一步可能要拆的卡
- [ ] `recall-beats-context-length` — 長度飽和後 recall 才是長上下文真戰場
- [ ] `headless-software-shift` — agent-first 介面對軟體形態的重塑
- [ ] `china-open-source-underpriced-signal` — 開源排行榜作為地緣 AI 實力的領先指標

## 相關白板（跨脈絡連結）
- `coding-agents` — harness > model 的命題在這條線被產業數據反覆驗證
- `llm-productization` — 價值流向、商品化時鐘都屬於產品化戰略

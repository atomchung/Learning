# Anthropic 最新 blog 研究（2026-05 ~ 06）

> 2026-06-05 研究。框架：讀**信號**不讀標題。三條最值得看的線 + 接既有判斷。

## 三條主線

### 1. 「When AI Builds Itself」——遞迴自我改進警告（6/4，最新）
Anthropic Institute 出報告 + blog，呼籲全行業考慮**放慢**開發。不是空談 AGI，而是拿兩個自家內部數字當證據：

- Anthropic 工程師每季產出 code 是 2021–2025 平均的 **8 倍**
- 截至 2026/5，併入production 的 code **超過 80% 由 Claude 寫**

論點：模型逼近 recursive self-improvement（AI 寫自己的 code 擴張自己能力），Jack Clark 說兩年內可能出現。提案是建「**可驗證的全球暫停機制**」——能查證別人是否真的也停了，不是單方面喊停。

### 2. Project Glasswing 擴張 + Claude Mythos（6/2）
直接打中我追蹤的「安全/紅隊 eval 值不值得當差異化技能」。

- **Mythos Preview** = 能自主找 zero-day 並寫 exploit 的模型；首次嘗試就重現漏洞並做出可用 exploit 的比例 **>83%**
- 掃 1000+ 開源專案，找出 23,019 個 issue，其中 **6,202 高/危嚴重度**
- 六家獨立資安公司驗證其中 1,752 個，**>90% 是真陽性**
- 戰績：在 wolfSSL（數十億裝置用的加密庫）找到漏洞，造出能偽造憑證的 exploit（可架假銀行網站）
- Glasswing 擴到 ~150 個新組織、15+ 國關鍵基礎設施
- **關鍵信號**：Anthropic 自己說**不公開 Mythos**——因為沒有任何公司（含自己）做出夠強的防濫用護欄

### 3. S-1 / IPO + $47B（6/1）
- 6/1 機密遞交 S-1；年化營收 run-rate **$47B**（2025 底 ~$9–10B，五倍跳）
- 成長主力：企業採用 + **Claude Code**
- 遞交前幾天剛完成 Series H：$65B、估值 **$965B**
- 跟 OpenAI 賽跑，兩家都預期 2026 年底前上市

## 串起來看（為什麼三條一起有意思）

同一家公司，**一邊用「80% code 由 Claude 寫」當 IPO 成長故事賣，一邊用同一個數字當「該放慢」的警鐘。** Glasswing 是這套邏輯的具體化：AI 攻擊能力強到「不敢公開」，正好替 6/4 的暫停論背書——能力跑在護欄前面的實證。

## 接既有判斷

**對「安全/紅隊 eval 值不值得深入」（open question）**
- Mythos >90% 真陽性 + 不敢公開 → 這塊價值在升值，且被模型廠當**戰略級**自己做。呼應 `notes/eval-ecosystem-niche.md`：錢往安全紅隊跑。
- 但也提示天花板：頂尖攻擊能力會被模型廠鎖在內部/合作網絡。個人差異化大概落在「**驗證、整合、合規流程**」那側，而非「比模型更會找洞」。

**對「harness > model / 讀信號不讀數字」**
- 「8x code、80% by Claude」要當**信號**讀（coding agent 已進生產主幹），別當「生產力 8x」實測——沒說複雜度、review 成本、回退率。是漂亮的比例，不是端到端產能。
- 接 `topics/coding-agents/cards/harness-beats-model.md`、`topics/ai-industry-reading/cards/read-signals-not-surface-numbers.md`。

**對投資/產業判讀**
- $47B run-rate 五倍跳，主力是 Claude Code = coding agent 是目前最會變現的 agent 形態。`freshness: 2026-06`，數字會過期，可遷移的是「先上市的模型廠用 coding agent 當主成長引擎」這個結構。

## 出處
- When AI Builds Itself：anthropic.com/institute/recursive-self-improvement；SiliconANGLE 2026-06-04
- Glasswing/Mythos：anthropic.com/research/glasswing-initial-update；thehackernews.com 2026-05；engadget、TechCrunch 2026-06-02
- S-1：Fortune 2026-06-01、CBS News、techbuzz.ai

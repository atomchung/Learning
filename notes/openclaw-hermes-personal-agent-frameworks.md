# OpenClaw vs Hermes Agent — 2026 個人 agent 框架雙雄

> freshness: 2026-06。產業快照，版號/數字會過期；可遷移的元判斷在最後。
> 研究觸發：用戶問「openclaw / Hermes 過去幾個月各自迭代了啥、方向是啥」。
> 注意：這兩個專案周圍長出巨量 AI 生成 SEO 內容農場，以下盡量三角驗證到 GitHub releases + README，細節數字當「約略」。

## 它們是什麼（同一個物種的兩個競品）

都是 2026 爆紅的**開源「個人 AI agent 框架」**：local-first gateway（控制平面）+ 透過你既有的通訊軟體接觸你（WhatsApp/Telegram/Slack/iMessage…）+ 背後驅動 coding-agent 後端與工具。差別在架構選擇，不在品類。

這個品類 = 用戶 profile 反覆出現的 **personal OS / agent OS** 論題的具體實例化。

**OpenClaw**
- 前身 **Moltbot**，MIT、Node.js。創辦人 Cole Steinberger 加入 OpenAI 後，專案交給**非營利基金會**接管。
- 日曆版號 `2026.M.patch`。有 **ClawHub** 技能註冊表（skill 界的 npm）。
- 架構偏**單 agent loop + 規劃**。

**Hermes Agent**
- **Nous Research**，MIT、Python。2/25 上線，4 個月 ~18 萬 stars，幾乎每 7–10 天一個大版。
- 賣點：**self-improving skills**（觀察重複工作流→自動蒸餾成 skill）+ **多 agent Kanban swarm** + **本地 SQLite FTS 記憶**（毫秒 recall）。

## OpenClaw 迭代（方向：穩定化 + 模組化）

- `2026.4.2` Task Flow 背景編排
- `2026.4.26` `migrate`（plan/dry-run）
- `2026.5.18` `defineToolPlugin` 型別化外掛 API、Android Talk Mode 語音
- `2026.6.1` Skill Workshop、Tokenjuice/Copilot runtime externalize 成官方 plugin、儲存層遷 SQLite
- `2026.6.8–6.9` beta：Telegram/WhatsApp 富文本、model routing 擴 GLM-5.2 + Claude Haiku 4.5、provider 拆獨立 npm、Codex 自動核准、agent 復原/session 修復

一句話：往 production-grade 可靠性 + provider/runtime 全外掛化（npm）走。

## Hermes 迭代（方向：自我改進 + swarm + ubiquity）

- `v0.7 Resilience`（4/3）：可插拔記憶、憑證輪替、Camofox 反偵測瀏覽器、inline diff
- `v0.9`（4/13）：Termux/Android、iMessage、WeChat、本地 dashboard、Fast Mode
- `Tenacity`（5/7）：耐久多 agent Kanban、持久 `/goal`、Checkpoints v2、gateway 自動續跑
- `v0.15 Velocity`（5/28）：大重構（`run_agent.py` 砍 76%）、Kanban→自動分解 swarm、`session_search` 重寫成無 LLM 快 4500×、Promptware 對抗式防禦、Bitwarden、skill bundles、TUI 編排器
- `v0.16 Surface`（6/5）：原生桌面 app、瀏覽器 admin panel、遠端 gateway、精簡預設 skill、模糊模型選擇器、`/undo`
- `v0.17 Reach`（6/19）：iMessage via Photon（免 Mac relay）、Raft agent network、背景/async 子 agent、圖片編輯、Automation Blueprints（免 cron 語法）、Skills Hub 大改、記憶原子批次操作、WhatsApp Business API

一句話：self-improving harness + multi-agent swarm + 跨平台桌面 + 安全硬化。

## 共同方向 = 訊號（差異全落在已有的卡軸上）

1. **差異化幾乎全在 harness，不在 model**：兩者都是模型無關路由器（GLM-5.2、Claude Haiku 4.5、Grok、OpenAI 隨插）。模型是可換後端，產品本體是 harness。→ harness>model 又一活例，兩個獨立團隊各自驗證。

2. **記憶架構是真正勝負手**：OpenClaw 每次 recall 把整份 JSONL session 餵回 context（~19s）；Hermes 走本地 SQLite FTS（~113ms）。差距來自記憶 substrate 設計，不是模型。→ 咬合「記憶架構」+ 本 repo 的 LLM-wiki 預編譯論點（檢索住本地 index，不是塞 context）。

3. **兩條 skill 累積路線**：Hermes = 學來的（自動蒸餾）；OpenClaw = 策展的（ClawHub 註冊表）。self-improving vs npm-for-skills，技能複利的兩種機制。

4. **都往 multi-agent swarm / 背景子 agent 收斂**：對應 agent-collab-infra 線。

## Caveat

- 周圍巨量 AI 生成 SEO 農場（幾十個近乎雷同域名，半數抓取 403 或空洞）。版號偏亂：Hermes 同時用 `v0.x` 和 `v2026.x` 兩套命名，部分 blog 日期互打。
- **SEO 農場爆炸本身是訊號**：紅到養出內容經濟。
- 治理訊號：OpenClaw 創辦人被 OpenAI 吸收、專案以基金會續命——「founder 被 lab 吃掉，專案變社群基建」的模式。

## 可遷移的元判斷（不會過期的部分）

- 個人 agent 框架的競爭是 **harness 之爭**：記憶 substrate、skill 累積機制、多 agent 編排——模型是商品化後端。
- 記憶 recall 要住**本地 index（SQLite FTS）**，不要每次重餵 context。慢 recall = 把 wiki 當 RAM 用的反模式。

## 出處

- github.com/openclaw/openclaw（+ /releases）
- github.com/NousResearch/hermes-agent/releases
- firecrawl.dev/blog/openclaw-vs-hermes、composio.dev/content/openclaw-vs-hermes-agent
- lennysnewsletter.com OpenClaw guide、marktechpost.com Hermes Desktop（2026-06-03）

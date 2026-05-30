# AI Project Research — 值得研究 & Build 的專案

> 持續更新中。目標：找出有趣的 AI 開源專案，評估我能不能自己 build 或做出類似的東西。

## 評估維度

| 維度 | 問題 |
|------|------|
| 技術可行性 | 我的技術棧能不能做？需要多少時間？ |
| 市場機會 | 有沒有 niche 可以切？有沒有付費意願？ |
| 差異化 | 能不能做出不一樣的版本？中文市場？垂直場景？ |
| 學習價值 | 就算不賺錢，能學到什麼？ |

## 專案總覽

詳細研究筆記見各子檔案。

### 📊 趨勢研究

| 研究 | 範圍 | 結論一句話 |
|------|------|-----------|
| [YC 2022-2026 趨勢](projects/yc_trends_2022_2026.md) | 近四年 YC + Demo Day | AI 占比 15% → 100%；2026 大轉向物理世界（robotics/能源/農業） |

### 🚀 GTM Playbook

持續追蹤 indie AI builder 怎麼把產品做出來 + 賣出去。

| 內容 | 範圍 |
|------|------|
| [GTM 研究 hub](gtm/README.md) | 案例庫 + AEO/SEO playbook + reddit 訊號 + ideas-to-build |
| [Agensi AEO 深度拆解](gtm/case_studies/agensi-aeo-deep-dive.md) | $0 ad / 2 個月 12K MAU 的 SEO + AEO 雙引擎 |
| [AEO 2026 方法論](gtm/playbooks/aeo-2026-methodology.md) | 通用 Answer Engine Optimization playbook |

### 🏢 Multi-Agent 編排

| 專案 | Stars | 一句話 | Build 難度 |
|------|-------|--------|-----------|
| [Paperclip](projects/paperclip.md) | 38K+ | 把 AI agent 包進公司組織架構（org chart + 預算 + 審計） | ⭐⭐⭐ |
| [CrewAI](projects/crewai.md) | 45.9K | Multi-agent 框架，角色分工協作 | ⭐⭐⭐ |

### 🤖 自主 Agent 平台

| 專案 | Stars | 一句話 | Build 難度 |
|------|-------|--------|-----------|
| [OpenClaw](projects/openclaw.md) | 247K+ | 自主 AI agent，接 Telegram/Slack/WhatsApp | ⭐⭐ |
| [Dify](projects/dify.md) | 130K+ | 視覺化 AI workflow 平台，內建 RAG | ⭐⭐⭐ |
| [n8n](projects/n8n.md) | — | No-code workflow + 原生 AI，400+ 整合 | ⭐⭐⭐ |

### 🧪 AI 研究自動化

| 專案 | Stars | 一句話 | Build 難度 |
|------|-------|--------|-----------|
| [AutoResearch](projects/autoresearch.md) | 61K+ | Karpathy 的自動 ML 實驗框架，一晚跑 100 實驗 | ⭐⭐ |

### 🛠 開發者工具 / Coding

| 專案 | Stars | 一句話 | Build 難度 |
|------|-------|--------|-----------|
| [GStack](projects/gstack.md) | 8.5K+ | Garry Tan 的 Claude Code workflow skills | ⭐ |

### 🌐 瀏覽器自動化

| 專案 | Stars | 一句話 | Build 難度 |
|------|-------|--------|-----------|
| [Browser Use](projects/browser-use.md) | 50K+ | Python LLM → 瀏覽器全自動控制 | ⭐⭐ |
| [Stagehand](projects/stagehand.md) | — | AI + Playwright 混合自動化 SDK | ⭐⭐ |
| [Steel](projects/steel.md) | — | 開源 headful browser API (Docker) | ⭐⭐ |

### 🕷 爬蟲 / 資料擷取

| 專案 | Stars | 一句話 | Build 難度 |
|------|-------|--------|-----------|
| [Firecrawl](projects/firecrawl.md) | — | API-first 網頁爬蟲 + MCP server，SaaS 模式 | ⭐⭐ |
| [Crawl4AI](projects/crawl4ai.md) | 62.3K+ | 開源爬蟲 + MCP，完全免費 | ⭐⭐ |

### 💰 MCP 變現模式

| 專案 | Stars | 一句話 | Build 難度 |
|------|-------|--------|-----------|
| [MCP Server as SaaS](projects/mcp-saas.md) | — | 21st.dev 靠 MCP server 6 週達 $10K MRR | ⭐⭐ |

---

## 🧪 個人 Eval 體系

這個 folder 也是我個人 LLM eval 方法論的家。四份研究 + 一份現況地圖：

| 檔案 | 角色 |
|------|------|
| [eval_inventory.md](eval_inventory.md) | **全工作區 eval 盤點地圖**（先看這個導航）— 散在 9+ folder 的 eval 在哪、接沒接 north star、跑到哪 |
| [personal_eval_playbook.md](personal_eval_playbook.md) | 方法論：個人 eval 怎麼做（Hamel/Shreya/Eugene Yan 蒸餾 + 路線圖）|
| [eval_addendum_outcome_metrics.md](eval_addendum_outcome_metrics.md) | outcome metric + north star + 投資場景兩層論 |
| [llm_eval_research.md](llm_eval_research.md) | 理論：benchmark vs eval、工具對照 |
| [eval/](eval/README.md) | 實作層：per-model error pattern profiling（scan_admissions.py）|

---

## 🔥 我最可能 Build 的方向（待評估）

1. **MCP Server 變現** — 把某個垂直領域做成 MCP tool，門檻低、需求明確
2. **中文版 OpenClaw** — 接 LINE / WeChat，針對台灣 / 中文用戶
3. **垂直 Agent Workflow** — 用 CrewAI / LangGraph 做特定場景（投資研究、內容生成）
4. **瀏覽器自動化工具** — Browser Use + Steel 的組合，做成服務
5. **AutoResearch 變體** — 不只 ML 實驗，延伸到其他研究場景

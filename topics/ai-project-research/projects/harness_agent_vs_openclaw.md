# OpenHarness vs OpenClaw vs 同類框架 研究筆記

> 更新日期：2026-04-14

---

## 一句話總結

**OpenHarness** 是香港大學 Data Intelligence Lab 開源的輕量 AI agent 基礎框架（給開發者造 agent 用的工具箱）；**OpenClaw** 是面向一般用戶的 24/7 個人自動化助理平台。兩者定位不同——前者是「基礎設施層」，後者是「應用層」。

---

## OpenHarness 是什麼？

GitHub：[HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness)  
發布時間：2026-04-01（初版）

### 兩大組件

| 組件 | 定位 |
|------|------|
| **OpenHarness** | 核心框架，給開發者用來造 agent |
| **ohmo** | 基於 OpenHarness 建的個人助理（整合 Feishu/Slack/Telegram/Discord）|

### 10 大子系統架構

```
Agent Loop（Engine）
├── Tool Registry（43 個工具：檔案/shell/搜尋/Web/MCP）
├── Skill Loader（從 .md 檔動態載入技能）
├── Plugin System（擴充套件）
├── Permission Checker（多層安全）
├── MCP Client（HTTP transport + 自動重連）
├── Memory Manager（跨 session 持久記憶，MEMORY.md）
├── Context Assembler（CLAUDE.md 發現、自動壓縮）
├── Task Manager（背景任務管理）
└── Multi-Agent Coordinator（subagent 生成、team registry）
```

### 支援模型

- **Anthropic 系**：Claude 官方、Moonshot/Kimi、Zhipu GLM、MiniMax
- **OpenAI 相容**：OpenAI、OpenRouter、DeepSeek、Gemini、Groq、Ollama（本機）、DashScope
- **訂閱制**：GitHub Copilot（OAuth）、Claude CLI、Codex

### 快速安裝

```bash
pip install openharness-ai
# 或
curl -fsSL https://raw.githubusercontent.com/HKUDS/OpenHarness/main/scripts/install.sh | bash

oh setup   # 互動式設定
oh         # 啟動
```

---

## OpenHarness vs OpenClaw：核心差異

| 維度 | OpenHarness | OpenClaw |
|------|-------------|---------|
| **定位** | Agent 基礎框架（給開發者） | 個人自動化助理平台（給一般用戶）|
| **主要用途** | 造自己的 agent | 用 agent 自動化日常工作 |
| **介面** | Terminal / Python API | Telegram / WhatsApp / Discord |
| **技術門檻** | 需要 Python 開發能力 | 非技術人員可用（15-30 分鐘設定）|
| **預建整合** | 43 工具（偏底層）| 20+ 高階整合（Gmail/Notion/Calendar）|
| **模型支援** | 多後端，含本機 Ollama | 200+ 後端 |
| **安全性** | 學術/開源，尚無重大安全事件 | CVE-2026-25253（CVSS 8.8），12% 技能惡意 |
| **GitHub 熱度** | 較新（2026-04）| 247k ⭐（超熱門）|
| **費用** | 完全免費 | 自架 $120-240/年 |

### 架構層次對比

```
[你的需求]
    │
    ▼
[應用層]   OpenClaw（一般用戶）、ohmo（OpenHarness 內建）
    │
    ▼
[框架層]   OpenHarness（開發者）、Hermes、LangGraph
    │
    ▼
[模型層]   Claude / GPT / DeepSeek / Ollama
```

---

## 同類框架全景（2026）

### 個人自動化助理類（OpenClaw 同類）

| 框架 | 特色 | 適合對象 |
|------|------|---------|
| **OpenClaw** | 20+ 原生整合，最大社群 | 非技術用戶，快速部署 |
| **Hermes** | 完整 Python 生態，Chain-of-thought | Python 開發者，客製化需求 |
| **Nemoclaw** | NVIDIA GPU 原生，本機推論 | 隱私敏感、有 GPU 的組織 |
| **NanoClaw** | 4,000 行 Python，極輕量，26.8k ⭐ | 想理解原理的開發者 |

### Agent 框架/基礎設施類（OpenHarness 同類）

| 框架 | 特色 | 適合對象 |
|------|------|---------|
| **OpenHarness** | 10 子系統，含 ohmo 助理，HKU 出品 | 研究者、想造 agent 的開發者 |
| **LangGraph (DeepAgents)** | LangChain 生態，subagent 支援 | 已用 LangChain 的團隊 |
| **AutoHarness** | 自動化 harness 工程，6 步治理 pipeline | 想自動優化 agent 系統的人 |
| **Artificial** | Go 語言，多 agent 協調（Claude/Codex）| 需要多 agent 協作的開發者 |
| **n8n** | 視覺化節點，非純 agent 框架 | 不想寫 code 的自動化需求 |

---

## 適用場景建議

### 選 OpenHarness 的時機
- 你想**從頭理解 AI agent 如何運作**（學術/研究背景）
- 需要**造自己的 agent 產品**，要底層控制
- 想用多模型、需要彈性的框架基礎
- 已熟悉 Python，接受目前版本較新、生態不完整

### 選 OpenClaw 的時機
- 需要**馬上可用的個人自動化**（郵件/行事曆/訊息）
- **非技術用戶**，不想寫 code
- 需要大量預建整合

### 選 Hermes 的時機
- OpenClaw 安全性讓你擔心
- 你是 Python 開發者，需要高度客製

### 同時使用的場景
> 用 **OpenHarness** 造自己的 agent 系統 → 用 **ohmo**（或自建）當操作介面 → 按需求選擇底層模型

---

## 相關資源

- [OpenHarness GitHub](https://github.com/HKUDS/OpenHarness)
- [OpenHarness README](https://github.com/HKUDS/OpenHarness/blob/main/README.md)
- [OpenHarness 功能介紹 - knightli.com](https://www.knightli.com/en/2026/04/12/openharness-basic-functions/)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [Open Source AI Agents 2026 Comparison - remoteopenclaw.com](https://remoteopenclaw.com/blog/open-source-ai-agents-2026-comparison)
- [Top OpenClaw Alternatives - DataCamp](https://www.datacamp.com/blog/openclaw-alternatives)

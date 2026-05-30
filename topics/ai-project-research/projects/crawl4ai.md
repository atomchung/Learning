# Crawl4AI — 開源爬蟲 + MCP Server

## 基本資訊
- GitHub: 62,300+ stars
- 技術棧: Python
- 授權: Apache 2.0
- MCP 支援: v0.8 起內建

## 它解決什麼問題？

給 AI agent 一個乾淨的網頁資料擷取能力。完全免費、可自架、無 API key 限制。

## 核心功能
- 網頁爬取 + 清洗 + 結構化輸出
- 內建 MCP server → AI agent 直接呼叫
- 支援本地 LLM 整合
- Adaptive pattern learning

## vs Firecrawl

| | Crawl4AI | Firecrawl |
|--|---------|-----------|
| 價格 | 完全免費 | $16/月起 |
| 部署 | Self-hosted | Managed API |
| MCP | 內建 | 內建 |
| 定位 | 開發者 / 深度客製 | 團隊 / 零維運 |

## 我能 Build 嗎？

### 和現有專案的關聯
- **info_collector 直接可用**：替代目前 httpx 手寫爬蟲
- **rednote_mcp 可升級**：用 Crawl4AI 替代 Selenium 做小紅書爬取

### 可能的切入角度
1. **整合進 info_collector**：讓每日 digest 的資料來源更穩定
2. **做中文網站特化版**：Crawl4AI 對中文網站支援可能不完美
3. **Crawl4AI + MCP 教學**：中文社群教學內容

## 參考連結
- https://crawl4ai.com/
- https://chatforest.com/reviews/crawl4ai-mcp-server/

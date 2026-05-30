# Browser Use — LLM 驅動的瀏覽器自動化

## 基本資訊
- GitHub: 50,000+ stars
- 技術棧: Python
- 授權: 開源

## 它解決什麼問題？

讓 LLM 完全控制瀏覽器 — 點擊、輸入、滾動、導航，LLM 自己決定所有操作。

## 核心功能
- 把任何 LLM 變成瀏覽器自動化 agent
- Agent loop：LLM 觀察頁面 → 決定動作 → 執行 → 觀察結果 → 重複
- 完整的瀏覽器控制（不只是 API 呼叫）

## 相關專案比較

| 專案 | 定位 | 特色 |
|------|------|------|
| Browser Use | Pure AI 驅動 | 最自由，但較慢較貴 |
| Stagehand | AI + Playwright 混合 | 精確度高，production ready |
| Steel | 開源 browser API | Docker 部署，可遠端控制 |

2026 趨勢：純 AI 太慢太貴，純 deterministic 太脆弱。**混合方案** (AI 決策 + 確定性執行) 是最佳實踐。

## 我能 Build 嗎？

### 技術可行性：⭐⭐ (中等偏易)
- Python 我熟
- Playwright / Selenium 有經驗 (rednote_mcp 用過 Selenium)
- 核心是 LLM + 瀏覽器 API 的橋接層

### 可能的切入角度
1. **垂直自動化服務**：不做通用工具，做某個場景的自動化（如：電商比價、社群管理）
2. **結合 MCP**：做成 MCP server，讓 Claude 能控制瀏覽器
3. **中文網站特化**：針對台灣 / 中國網站的自動化（表單填寫、資料擷取）
4. **和 rednote_mcp 結合**：升級現有的小紅書自動化工具

### 學到什麼
- LLM + 瀏覽器自動化的架構模式
- Vision model 在 UI 理解中的應用
- Agent loop 設計

## 參考連結
- https://github.com/browser-use/browser-use
- https://www.stagehand.dev/
- https://steel.dev/

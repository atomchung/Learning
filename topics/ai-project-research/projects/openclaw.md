# OpenClaw — 開源自主 AI Agent

## 基本資訊
- GitHub: 247,000+ stars (GitHub 史上增長最快的開源專案之一)
- 作者: Peter Steinberger (奧地利 vibe coder)
- 原名: Clawdbot (2025-11 首發)
- 現狀: 作者 2026-02 加入 OpenAI，專案移交開源基金會
- 授權: 開源

## 它解決什麼問題？

讓非技術用戶也能擁有一個 24/7 運行的 AI 助手，接入日常使用的通訊平台。

## 核心功能
- 自主 AI agent，7×24 運行
- 接入 Telegram / WhatsApp / Slack / Discord
- 記憶對話上下文
- 自動化日常任務
- 主動發送更新通知
- 瀏覽器控制、表單填寫、多步驟工作流
- 自架 (self-hosted)

## 生態系統
- Tencent 基於 OpenClaw 推出了 WeChat 整合 AI 產品線 (2026-03)
- 已有大量社群插件和整合

## 我能 Build 嗎？

### 技術可行性：⭐⭐ (相對容易)
- 核心是 LLM + 通訊平台 API + 任務排程
- 瀏覽器自動化部分可用 Browser Use / Playwright
- 難點：記憶管理、長期上下文維護

### 可能的切入角度
1. **LINE Bot 版本**：台灣市場 LINE 滲透率極高，目前沒有好的 LINE AI agent
2. **中文優先**：繁中 prompt engineering + 台灣在地服務整合
3. **垂直版本**：不做通用 agent，做「投資助手」「內容助手」等垂直場景
4. **WeChat 小程序**：中國市場，但需要中國伺服器

### 學到什麼
- 自主 agent 架構設計
- 多平台通訊整合
- 長期記憶和上下文管理

## 參考連結
- https://en.wikipedia.org/wiki/OpenClaw
- https://newsus.cgtn.com/news/2026-03-29/Users-build-autonomous-AI-agents-with-OpenClaw-1LTuwzYCTks/p.html
- https://vida.io/blog/what-is-openclaw

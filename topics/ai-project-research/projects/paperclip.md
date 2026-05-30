# Paperclip — Zero-Human Company 編排平台

## 基本資訊
- GitHub: github.com/paperclipai/paperclip
- Stars: 38,000+ (3 週內達成)
- 作者: @dotta (匿名開發者)
- 發布: 2026-03-04
- 技術棧: Node.js server + React dashboard
- 授權: 待確認

## 它解決什麼問題？

企業部署多個 AI agent 時，最大的痛點不是單個 agent 不夠聰明，而是 agent 之間不會協調。
成本失控是常見問題 — agent 太成功反而跑到 API 帳單爆掉。

Paperclip 的核心洞察：multi-agent 本質上是組織設計問題，不是技術問題。

## 核心功能
- Org chart：agent 之間有報告線、層級關係
- Job title / Role：每個 agent 有明確職責
- Budget tracking：token 預算控制，超額自動節流
- Audit log：所有 agent 行為可追蹤
- Goal tracking：組織級目標分解到各 agent
- Governance：升級路徑、決策權限

## 我能 Build 嗎？

### 技術可行性：⭐⭐⭐ (中等)
- Node.js + React 我熟
- 核心是編排邏輯 + dashboard UI，不需要訓練模型
- 難點：設計好 agent 間的通訊協議和權限模型

### 可能的切入角度
1. **中文化 + 本地化**：做繁中版，接入台灣常用的 LLM API
2. **垂直場景**：不做通用平台，專注某個場景（如：AI 內容團隊、AI 投研團隊）
3. **簡化版**：Paperclip 太重，做一個輕量版給小團隊用
4. **結合 CrewAI**：Paperclip 是管理層，CrewAI 是執行層，整合兩者

### 學到什麼
- Multi-agent 系統架構設計
- Token 成本管理策略
- 組織理論在 AI 系統中的應用

## 參考連結
- https://paperclip.ing/
- https://medium.com/@creativeaininja/paperclip-the-open-source-platform-turning-ai-agents-into-an-actual-company-7348015c5bf7

# Hermes Agent vs OpenClaw 研究筆記

> 更新日期：2026-04-14  
> 參考來源：[動區動趨報導](https://www.blocktempo.com/hermes-agent-opens-source-nous-research-openclaw-github-stars-learning/)

---

## 一句話總結

**Hermes**（Nous Research 出品）是目前唯一內建「自我學習閉環」的開源 agent——它會從你的使用經驗自動生成技能、優化自己；**OpenClaw** 則是整合廣度優先的平台，強調多服務串接和快速部署。

Hermes 的核心 slogan：**"An agent that grows with you"**

---

## Hermes 核心概念

### 三個差異點

1. **自動生成技能**：完成複雜任務後，自動將解法打包成結構化技能檔 → 下次直接複用，不需重新摸索
2. **雙記憶檔案**：
   - `MEMORY.md`：環境資訊 + 過去經驗
   - `USER.md`：你的偏好、習慣（每次對話自動注入）
3. **SQLite 歷史庫**：所有對話存入資料庫，agent 可主動檢索過去的解法

### 架構設計

```
[使用者輸入]
     │
     ▼
[做（Do）] → 執行任務（40+ 工具：搜尋/瀏覽器/視覺/圖像生成）
     │
     ▼
[學（Learn）] → 自動生成技能檔
     │
     ▼
[改進（Improve）] → 優化技能，更新 MEMORY.md / USER.md
     │
     └──────────────────→ 循環
```

vs OpenClaw 的中央控制平面（所有操作流經統一控制器）

### 技術規格

| 項目 | 詳情 |
|------|------|
| **發布時間** | 2026 年 2 月 |
| **GitHub** | [NousResearch/hermes-agent](https://github.com/nousresearch/hermes-agent) ｜69.9k ⭐ / 9k fork |
| **內建工具** | 40+ 種（網頁搜尋、瀏覽器自動化、視覺理解、圖像生成、定時任務）|
| **模型支援** | Nous Portal（400+）、OpenRouter（200+）、OpenAI、HuggingFace、DeepSeek、Kimi 等 |
| **訊息平台** | 統一 gateway，支援 14 個平台（Telegram/Discord/Slack/WhatsApp/Signal/SMS/Email 等）|
| **部署** | $5 VPS / GPU cluster / Serverless（閒置近乎免費）|
| **最新版本** | v0.5.0（2026-03-28）—— 50+ 安全修復 + 供應鏈審計 |

---

## Hermes vs OpenClaw 對比

| 維度 | Hermes | OpenClaw |
|------|--------|---------|
| **最大差異** | 自我學習、技能自動生成 | 龐大整合生態 |
| **架構** | Agent 執行迴圈為核心（做→學→改進）| 中央控制平面 |
| **技能來源** | Agent 從經驗自主生成 | 多為人工編寫，ClawHub 市場 |
| **記憶** | MEMORY.md + USER.md + SQLite | Session 間較有限 |
| **訊息平台** | 14 個平台統一 gateway | 主要幾個平台 |
| **模型支援** | 400+ (Nous Portal) | 200+ |
| **安全性** | v0.5.0 做了供應鏈審計 | CVE-2026-25253 + 12% 惡意技能 |
| **GitHub 熱度** | 69.9k ⭐（6 週內） | 247k ⭐（更早起步）|
| **部署複雜度** | 稍高（需設定 gateway）| Docker 15-30 分鐘 |
| **誰在用** | 開發者 / 進階用戶 | 非技術用戶 / 快速部署 |

---

## 優缺點

### Hermes

| ✅ 優點 | ❌ 缺點 |
|--------|--------|
| 唯一有學習閉環的開源 agent | 2 月才發布，生態相對新 |
| 技能自動積累，越用越強 | 設定比 OpenClaw 複雜 |
| 14 平台統一 gateway | 文件尚在完善 |
| 安全性比 OpenClaw 好（v0.5.0 已審計）| |
| $5 VPS 即可部署 | |

### OpenClaw

| ✅ 優點 | ❌ 缺點 |
|--------|--------|
| 20+ 原生高階整合（Gmail/Notion/Calendar）| CVE-2026-25253 未完全解決 |
| 社群最大（247k ⭐），技能市場豐富 | 12% ClawHub 技能為惡意 |
| 非技術用戶 15 分鐘上手 | 技能為靜態人工撰寫 |
| Docker 快速部署 | 中國政府已禁用（企業採購風險）|

---

## 適合場景

### 選 Hermes 的時機
- 希望 agent **越用越聰明**，能記住你的習慣和解法
- 長期個人助理，重視跨 session 連貫性
- 想要**安全性更好**的開源選項（已做供應鏈審計）
- 有 VPS 或願意自架，接受稍高設定成本

### 選 OpenClaw 的時機
- 需要快速上手、**不想花時間設定**
- 需要接 Gmail、Notion、Calendar 等特定服務
- 非技術背景用戶

---

## 相關資源

- [Hermes GitHub](https://github.com/nousresearch/hermes-agent)
- [Hermes 官方網站](https://hermes-agent.nousresearch.com/)
- [動區動趨：Hermes 介紹文](https://www.blocktempo.com/hermes-agent-opens-source-nous-research-openclaw-github-stars-learning/)
- [Hermes v0.5.0 Release Notes](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.5.0.md)
- [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)

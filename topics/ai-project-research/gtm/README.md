# GTM Research — AI Project Go-to-Market 持續追蹤

> 目標：研究獨立開發者 / 個人 builder 把 AI project 做出來後，怎麼真的拿到用戶 + 收入。
> 重點不在「能不能做」，而在「做完之後怎麼活下來」。

## 為什麼開這個 folder

2026 上半年的 indie hacker 普遍共識：
- **build 的部分被 AI 抹平了**（Lovable, Claude Code, Cursor 讓非工程師也能 ship）
- **distribution 變成 80% 的工作**（Reddit r/indiehackers, r/SaaS 反覆出現的痛點）
- **SEO + AEO 是現在最被低估的免費複利渠道**

這個 folder 持續收集真實案例 + playbook，當作下一個 side project 上線前的參考底稿。

---

## 結構

```
gtm/
├── README.md                    ← 你在這
├── case_studies/                ← 單一專案 GTM 深度拆解
│   └── agensi-aeo-deep-dive.md  ← Agensi（AI agent skills marketplace）
├── playbooks/                   ← 跨案例提煉的通用方法論
│   └── aeo-2026-methodology.md  ← AEO (Answer Engine Optimization) 通用做法
├── signals/                     ← 原始素材（社群熱度、需求訊號）
│   └── reddit-2026-05/          ← 6 個 indie sub × 50 篇貼文原始 dump
└── ideas-to-build/              ← 從 signal 衍生的可動手清單
    └── README.md
```

## 已收錄案例

| 案例 | 賽道 | 達成 | 核心 playbook | 連結 |
|---|---|---|---|---|
| **Agensi** | AI agent skills marketplace | 2 個月 12K MAU / $0 ad | SEO + AEO 內容引擎 + programmatic skill pages + Reddit 種子 | [link](case_studies/agensi-aeo-deep-dive.md) |

## 待加（從 reddit signal 抓出來的）

- [ ] **leadverse.ai** — $11K rev / 8 個月 / $0 ad — freemium + comparison pages + outreach 30 人/天
- [ ] **looktara** — $20K rev / 14 個月 — AI headshot app，X + Reddit + SEO + 自動化 stack 完整公開
- [ ] **iconstack.io** — 3 個月 10K DAU — programmatic SEO 教科書範例（53K icons = 50K Google 頁）
- [ ] **SalesRobot** — $1.2M ARR — LinkedIn automation，3 年從產品破爛到穩定的故事
- [ ] **Boring compliance SaaS** — $3.2K MRR — 把 dashboard 改成自主 agent 的關鍵 pivot

## 重點 takeaway（每加一個 case study 都更新這裡）

### 已收斂的原則（多案例驗證）
1. **SEO + AEO 是 2026 indie 最大的免費複利**，但需要 4-8 週才看到信號
2. **Reddit 是「spark」不是「engine」**：10-15 篇真誠分享起頭，SEO 接力
3. **Programmatic SEO + supply-side 內容** 是擴展性最高的設計（每加 1 個 unit = 1 個 landing page）
4. **frictionless signup**（Google OAuth）對轉換率影響極大（45% → 78%）
5. **價格不要太低**（$19 看起來像劣等，$39 反而轉換率升）

### 待驗證的假設
- 中文圈（小紅書 / 即刻 / V2EX）能不能套同樣 playbook？
- 豆包 / Kimi / DeepSeek 的 AEO 競爭強度是否真的比 ChatGPT 低？
- B2B AI agent 工具的 retention 比一般 SaaS 高還低？

---

## 持續更新原則

- **每次發現新案例**：在 `case_studies/` 加一份 markdown，更新本 README 表格
- **每次抓 Reddit / HN signal**：放進 `signals/` 帶日期戳記，不修改舊資料
- **每次有可動手的點子**：放進 `ideas-to-build/`
- **每月對 takeaway 段做一次去重 / 修正**

最後更新：2026-05-21

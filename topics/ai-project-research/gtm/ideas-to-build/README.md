# Ideas to Build — 從 GTM 訊號衍生的可動手清單

> 從 `signals/` 抓到的 reddit 熱度 + `case_studies/` 拆解出的 playbook，反推「ting 用現有 stack 可做的」具體點子。

## 評分軸
- **stack 契合**：你 Python / Node / Streamlit / Selenium / CrewAI 能不能直接做
- **GTM 模板**：是否有現成 case study 可以照抄 distribution
- **市場已驗證**：reddit 上有沒有真實付費案例

---

## A 級（高契合 + 有 GTM 模板）

### 1. 中文版 Claude skills marketplace
- **靈感**：Agensi 2 個月 12K MAU
- **stack**：Next.js + Lovable 或 Streamlit，SKILL.md 規格直接複用
- **GTM**：照抄 Agensi AEO 模板，攻豆包 / Kimi / DeepSeek 引用
- **差異**：中文工程師 + Cursor 中國用戶
- **風險**：要先驗證中文 search volume；Anthropic 官方未來可能直接做
- **行動門檻**：30 天可上線 MVP

### 2. 把 `personal_os/` 已有 skills 上架 Agensi
- **靈感**：你已經寫好 record, session-board, xhs-* 等 skills
- **stack**：你已經有了，只要包裝
- **GTM**：借 Agensi 既有流量
- **預期回報**：低（最多賺幾十美金），但是免費的訊號驗證 + 反向學 Agensi
- **行動門檻**：1 個週末

### 3. 小紅書創作者工具目錄
- **靈感**：Agensi programmatic SEO + 你的 `rednote_*` 經驗
- **stack**：Python + Streamlit + Selenium（你已會）
- **GTM**：每個工具 / 模板 / 教學 = 一個 AEO 頁，攻百度 + 豆包
- **差異**：中文圈這類 directory 都還沒做 AEO
- **風險**：小紅書平台反爬風控
- **行動門檻**：60 天 MVP

---

## B 級（高契合 + GTM 不確定）

### 4. 中文版本地 voice-to-text macOS menubar
- **靈感**：Wispr clone 2 週 148↑（reddit/SideProject）
- **stack**：Python + Whisper + Tauri（學習成本中等）
- **GTM 不明**：個人工具 → ProductHunt + r/macOS + 即刻
- **市場**：中文重度 LLM 用戶（你自己就是 ICP）
- **行動門檻**：30 天 prototype

### 5. 「去算法化」中文資訊瀏覽器 Chrome extension
- **靈感**：Dull 去掉 Instagram Reels，$1.5K MRR
- **stack**：Node.js + Chrome Extension API
- **GTM**：bilibili / 即刻 / V2EX 上有討論「算法疲勞」群體
- **差異**：英文圈做了，中文圈沒有
- **行動門檻**：21 天

### 6. 個人化股票 / 新聞儀表板訂閱
- **靈感**：boring SaaS quietly $3K MRR
- **stack**：你 `stock/` + `news_analysis/` 已有底
- **GTM**：每隻股票 = 一個 AEO 頁（programmatic）
- **風險**：投資內容法規 + 已有 finbox / simplywall.st 競爭
- **行動門檻**：90 天才有差異化版本

---

## C 級（流量已驗證但 stack 不太契合）

### 7. 諷刺型 / 病毒「無用 app」配合小紅書
- **靈感**：Carrier Pidge (110mph 簡訊)、burn2feel
- **stack**：簡單 Next.js + Stripe 你 OK
- **GTM**：小紅書本身就是病毒平台
- **問題**：低變現 + 短半衰期
- **保留原因**：成本超低，可當小紅書內容流量試水

### 8. AI agent 安全 audit 服務
- **靈感**：Brazil pentest firm 看 50 個 vibe coded SaaS 全中招
- **stack**：可以做（你會 Selenium / Python）
- **GTM 不明**：B2B 銷售，indie 不擅長
- **保留原因**：訊號很真實，但 GTM 太重

---

## 暫不做（記下避免重複思考）

- **又一個 Reddit/X buyer intent 工具**：已紅海到 r/SaaS 罵聲一片
- **AI resume / cover letter / headshot**：飽和
- **LinkedIn outreach automation**：飽和 + 平台風控
- **又一個 AI chatbot wrapper**：被罵到爛

---

## 決策模板（每次冒新點子用）

當有新點子時，問：
1. signals/ 裡有沒有同類成功案例？（搜關鍵字）
2. case_studies/ 裡的 GTM playbook 哪個可以直接抄？
3. 我的 stack 真的能做嗎？還是要學新技術？
4. 我自己會用嗎？（不會用的不要做）
5. 中文圈版本 vs 英文圈版本，哪個競爭弱？

---

最後更新：2026-05-21

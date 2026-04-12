# AI 加速學習研究：聚焦 Alpha School 教育方法

## 一、研究背景

隨著 AI 技術快速發展，越來越多 K-12 教育機構開始導入 AI 工具來加速學生學習。本文重點研究 **Alpha School** 的教育模式，並概覽其他主流 AI 教育工具的應用現況。

---

## 二、Alpha School 教育模式（重點）

### 2.1 基本介紹

| 項目 | 說明 |
|------|------|
| 創立時間 | 2014 年，德州奧斯汀 |
| 年級範圍 | PreK - 9 年級（K-12） |
| 校區數量 | 目前 22 所，2026 秋季預計擴展至 35+ 所 |
| 學生人數 | 從約 200 人成長至超過 1,000 人 |
| 學費範圍 | $10,000 - $75,000 美元/年（依校區而異） |
| 擴展地區 | 德州、佛州、加州、紐約、芝加哥、亞特蘭大、波多黎各等 |

### 2.2 核心理念：2 Hour Learning（兩小時學習法）

Alpha School 的核心主張是：**透過 AI 自適應學習，學生只需每天 2 小時即可完成傳統學校一整天的核心學科學習。**

這個理念源自教育心理學家 Benjamin Bloom 在 1984 年提出的 **「2 Sigma 問題」**：

> 接受一對一輔導的學生，平均表現優於傳統班級授課學生 **2 個標準差**（即超越 98% 的傳統學生）。

Bloom 的挑戰是：如何讓群體教學達到一對一輔導的效果？Alpha School 認為 **AI 自適應學習** 就是答案。

### 2.3 每日作息結構

```
8:15 - 8:30   到校、晨間活動
8:30 - 10:30  ★ AI 學習時段（核心學科，共 2 小時）
               → 數學（30 分鐘）
               → 科學（30 分鐘）
               → 英語（30 分鐘）
               → 社會科學（30 分鐘）
10:30 - 11:00 休息時間
11:00 - 12:00 午餐與自由活動
12:00 - 3:30  ★ 生活技能工作坊（下午時段）
3:30 - 4:00   放學
```

### 2.4 AI 學習系統運作方式（教材與課程設計詳解）

#### 核心平台：Dash 學習介面

學生每天登入 Alpha 自研的 **Dash 平台**，這是整個學習體驗的入口。Dash 會根據 AI Tutor 的判斷，將學生導向最適合的自適應學習 App 和課程。

#### 兩大 AI 模型：知識圖譜 + 興趣圖譜

Alpha 的 AI 為每位學生建立兩個動態模型，這是其教材設計的核心創新：

**1. Knowledge Graph（知識圖譜）**
- 記錄學生已掌握和尚未掌握的所有概念
- 每次學習開始時透過診斷題目（diagnostic questions）偵測學生現有知識
- 將結果標記在精熟地圖（mastery map）上
- 即時更新，隨著學習進展不斷調整

**2. Interest Graph（興趣圖譜）**
- 收集學生的興趣：喜歡的運動、音樂、遊戲、文化偏好等
- AI 追蹤互動過程中的參與度訊號（engagement signals）
- 建立一個持續更新的興趣資料庫

#### 生成式 AI 個人化教材（核心創新）

Alpha 最大的創新在於 **用生成式 AI 即時產生個人化課程內容**，融合知識圖譜和興趣圖譜：

```
知識圖譜（學生不會什麼）  +  興趣圖譜（學生喜歡什麼）
                    ↓
           生成式 AI 即時編寫課程
                    ↓
           為每個學生產出獨特的教材
```

**具體範例：**
- 喜歡籃球的學生 → 幾何課以「罰球的弧線」為切入點教拋物線
- 喜歡 Taylor Swift 的學生 → 用「演唱會門票銷售數據」教分數概念
- 喜歡足球的學生 → 用「自由球踢法」教物理學
- 對供需法則的教學 → 轉化為「Swift 主題演唱會舞台設計挑戰」

這些不是預製教材，而是 **AI 根據每位學生即時生成的獨特課程**。

#### 自適應學習流程

```
學生登入 Dash 平台
    ↓
AI 透過診斷題評估當前知識水平（Knowledge Graph 更新）
    ↓
結合 Interest Graph，用生成式 AI 產出個人化課程
    ↓
學生在 25 分鐘結構化學習區間內學習
    ↓
AI 即時分析：正確率、回答速度、參與度
    ↓
達到 90% 以上正確率 → 解鎖下一階段
    ↓
未達標 → AI 用不同方式重新教授同一概念
    ↓
視覺模型偵測分心行為 → 提示學生自我修正
```

#### AI 即時輔導反饋系統

AI Tutor 不只出題，還會 **即時分析學習行為並給予指導**：

> 「我們注意到你的正確率稍低，原因是你答錯時沒有花時間閱讀解釋就直接跳到下一題。我們要放慢速度。」

這種即時行為分析和糾正回饋，模擬了真人家教的互動方式。

#### 視覺監控模型

- 攝影鏡頭搭配 **視覺 AI 模型**（vision model）偵測學生是否分心
- 偵測到分心行為時，系統會提示學生自我修正
- Guide 也會在旁審核 AI 生成的課程內容，確保準確性和學術對齊

#### 使用的 AI 與教育平台

| 平台類型 | 工具名稱 | 用途 |
|----------|----------|------|
| 自研核心 | **Dash** | 學習入口介面，整合所有 App |
| 自研核心 | **AI Tutor** | 知識圖譜 + 興趣圖譜引擎，判斷學習路徑 |
| 自研教材 | Alpha Math、AlphaRead、AlphaWrite | 核心學科的自適應練習 |
| 第三方平台 | Khan Academy、IXL、Membean、MobyMax、Mentava、Grammarly | 補充特定學科練習 |
| 課程標準 | K-8 採用 Common Core；高中採用 AP 課程 | 與傳統學校相同的課綱標準 |

#### 遊戲化激勵系統（Gamification）

Alpha 認為 **動機佔學習方程式的 90%，教育科技只佔 10%**，因此大量運用遊戲化設計：

| 機制 | 說明 |
|------|------|
| **進度環（Progress Rings）** | 視覺化顯示學習進度，完成精熟學習後環會閉合（類似 Apple Watch 活動環） |
| **Alpha Bucks** | 虛擬貨幣獎勵，可用於熱情專案或投資活動，讓進步感覺「看得見摸得著」 |
| **個人化動機適配** | AI 偵測每個孩子的動力來源（競爭、創造、社交認同、自由時間）並調整獎勵方式 |
| **即時回饋多巴胺迴路** | 即時反饋 + 獎勵 + 可見進步 → 觸發多巴胺釋放，與電玩遊戲相同的正向回饋機制 |
| **學習目標解鎖** | 完成學術目標可解鎖特權（如更多自由時間） |

#### 學習效率數據（Alpha 官方宣稱，未經獨立驗證）

- 完成一個年級的學科內容僅需 **20-30 小時**（傳統學校約需 200+ 小時）
- 學習速度約為傳統學校的 **10 倍**
- 在全國標準化 MAP 測驗中，學生成長速度為同齡學生的 **2.6 倍**
- 自稱在全國標準化測驗中排名 **前 1%**

### 2.5 Guide（引導員）角色 — 取代傳統教師

Alpha School 不設傳統「教師」，而是由 **Guide（引導員）** 取代：

| 傳統教師 | Alpha Guide |
|----------|-------------|
| 備課、授課、講解知識 | AI 系統負責知識傳授 |
| 批改作業、評分 | AI 自動評分與追蹤 |
| 課堂管理 | 引導員負責激勵與情感支持 |
| 統一進度教學 | 學生各自按 AI 安排的個人化節奏學習 |

**Guide 的核心職責：**
- 激勵學生、設定學習目標
- 提供情感支持與心理輔導
- 下午帶領生活技能工作坊
- 深入了解每位學生的興趣與挑戰
- 確保學生在 AI 學習時段保持專注

### 2.6 知識圖譜與興趣圖譜的技術設計深度分析

#### 一、Knowledge Graph（知識圖譜）— 怎麼設計與維護

##### 資料結構：有向無環圖（DAG）

知識圖譜本質上是一個 **有向無環圖（Directed Acyclic Graph）**，描述知識概念之間的前置關係：

```
節點（Node）= 一個知識概念（如「分數加法」「一元一次方程式」）
有向邊（Edge）= 前置關係（A → B 表示必須先學會 A 才能學 B）
邊的權重 = 前置覆蓋度（學 B 時隱含複習了多少 A 的內容）
```

**範例：數學知識圖譜片段**
```
整數加減法
    ├──→ 分數概念
    │       ├──→ 分數加減法
    │       │       └──→ 分數乘除法
    │       │               └──→ 比例與百分比
    │       └──→ 小數概念
    │               └──→ 小數四則運算
    └──→ 整數乘除法
            └──→ 因數與倍數
                    └──→ 最大公因數 / 最小公倍數
```

每個節點包含：
- **概念 ID 與名稱**
- **對應的課綱標準**（Common Core / AP）
- **知識點（Knowledge Points）**：每個概念拆分為 3-4 個可測試的知識點
- **前置節點清單**（prerequisites）
- **後置節點清單**（postrequisites）
- **前置覆蓋權重**（encompassing weight）

##### 建構方式

1. **課程專家人工建構骨架**：學科專家根據課綱定義概念節點與前置關係
2. **細粒度拆分**：每個概念拆為 3-4 個 knowledge points，每個 knowledge point 對應具體的可測試能力
3. **權重標定**：標定前置覆蓋權重（學到後置概念時，隱含複習了多少前置概念）

##### 學生精熟狀態追蹤（Knowledge Tracing）

每個學生在圖譜上的每個節點都有一個 **精熟狀態值**，業界常用兩種模型：

**方法 A：Bayesian Knowledge Tracing（BKT）**
```
核心思想：將學習建模為隱馬可夫過程（Hidden Markov Process）
狀態：已掌握（mastered） / 未掌握（not mastered）
四個參數：
  - P(L₀)：初始掌握概率
  - P(T)：每次練習後從未掌握 → 掌握的轉換概率
  - P(G)：未掌握但猜對的概率（guess）
  - P(S)：已掌握但答錯的概率（slip）

每次學生作答後，用貝氏定理更新 P(mastered)：
  答對 → P(mastered) 上升
  答錯 → P(mastered) 下降
```

**方法 B：Deep Knowledge Tracing（DKT）**
```
核心思想：用 LSTM 神經網路建模學生知識狀態
輸入：學生的作答歷史序列 [(題目₁, 對/錯), (題目₂, 對/錯), ...]
輸出：對每個知識點的預測掌握概率
優勢：能捕捉跨知識點的複雜關聯
```

**Alpha 的可能做法（推測）：**

Alpha 結合了兩種信號來判斷精熟度：
- **正確率**（答對比例）
- **回答時間**（相對於精熟學生的預期時間）

> 「如果學生答對但花了過長時間，該證據的權重會被降低」— 類似真人教師的判斷

當精熟度 ≥ 90% 時解鎖下一階段。

##### 動態維護流程

```
┌─────────────┐
│  學生登入     │
└──────┬──────┘
       ↓
┌─────────────────────┐
│  診斷測驗（Diagnostic） │ ← 利用圖譜結構最小化題數
│  數學的層級結構讓      │   （通常 20-60 題即可）
│  AI 可以「跳著問」     │
└──────┬──────────────┘
       ↓
┌──────────────────┐
│  建立初始精熟地圖   │ ← 標記每個節點：已會 / 部分會 / 不會
└──────┬───────────┘
       ↓
┌──────────────────────────┐
│  找到「知識前沿」            │ ← 已會與不會的邊界（knowledge frontier）
│  = 前置條件已滿足的最近未會節點 │
└──────┬───────────────────┘
       ↓
┌──────────────────┐
│  安排學習任務       │ ← 選擇知識前沿上的最優節點
│  最大化「每單位時間學習量」│
└──────┬───────────┘
       ↓
┌──────────────────┐
│  學生作答           │
└──────┬───────────┘
       ↓
┌──────────────────────────┐
│  即時更新精熟狀態           │
│  - 正確率 + 回答時間 → 更新 BKT│
│  - 前置覆蓋權重 → 隱含複習效果 │
│  - 遺忘曲線 → 安排間隔複習     │
└──────┬───────────────────┘
       ↓
      循環 ↻
```

##### 間隔複習與遺忘曲線

Math Academy（Alpha 使用的同類技術）開發了 **FIRe 演算法（Fractional Implicit Repetition）**：

```
核心洞見：在層級知識體系中，複習高階概念時隱含複習了低階前置概念

範例：複習「分數乘除法」時，學生同時在運用「分數概念」和「整數乘除法」

效果：透過前置覆蓋權重，一次複習可以「隱含覆蓋」多個前置主題
     → 大幅減少總複習次數
     → 這也是「2 小時就夠」的技術基礎之一
```

---

#### 二、Interest Graph（興趣圖譜）— 怎麼設計與維護

##### 資料結構：標籤化用戶畫像 + 嵌入向量

興趣圖譜不像知識圖譜那樣有嚴格的層級關係，更接近 **用戶畫像（User Profile）** 的設計：

```
Interest Graph = {
    explicit_interests: [          // 學生主動填寫
        { topic: "籃球", weight: 0.9 },
        { topic: "Taylor Swift", weight: 0.85 },
        { topic: "Minecraft", weight: 0.7 }
    ],
    implicit_signals: [            // 系統觀察推斷
        { topic: "太空探索", engagement_score: 0.8 },
        { topic: "動物", engagement_score: 0.6 }
    ],
    learning_style: {              // 學習偏好
        prefers_visual: 0.7,
        prefers_story: 0.9,
        prefers_competition: 0.4,
        prefers_collaboration: 0.6
    },
    motivation_drivers: {          // 動機驅動因素
        competition: 0.3,
        creativity: 0.8,
        social_recognition: 0.5,
        free_time_reward: 0.7
    }
}
```

##### 資料收集方式

| 來源 | 收集方式 | 範例 |
|------|----------|------|
| **顯式輸入** | 入學問卷 / 定期調查 | 「你最喜歡什麼運動？」 |
| **參與度信號** | 追蹤在不同主題情境下的學習時長、正確率、完成速度 | 籃球情境的題目做得更快更準 |
| **行為信號** | 滑鼠移動、眼球追蹤、停留時間 | 對太空主題的插圖停留更久 |
| **選擇信號** | 當提供多個主題選項時學生的選擇偏好 | 總是選擇音樂相關的題組 |
| **情感信號** | 攝影鏡頭偵測的表情變化 | 看到動物主題時微笑次數增加 |

##### 動態維護

```
每次學習 session：
  1. 產出帶有興趣情境的課程（如用籃球教分數）
  2. 追蹤學生的參與度指標：
     - 正確率變化（興趣情境 vs 中性情境）
     - 回答速度變化
     - 主動學習時長（是否提前退出或超時繼續）
  3. 更新興趣權重：
     - 參與度高 → 權重上升
     - 參與度低 → 權重下降
     - 長期未互動 → 權重衰減（類似遺忘曲線）
  4. 定期探索新興趣（exploration vs exploitation）：
     - 偶爾嘗試新主題情境
     - 如果參與度高 → 加入興趣圖譜
```

---

#### 三、兩個圖譜如何協同工作

```
┌─────────────────┐    ┌─────────────────┐
│  Knowledge Graph │    │  Interest Graph  │
│  知識圖譜         │    │  興趣圖譜         │
│                  │    │                  │
│  目前該學什麼？    │    │  用什麼情境包裝？  │
│  （知識前沿節點）  │    │  （最高參與度主題） │
└────────┬────────┘    └────────┬────────┘
         │                      │
         └──────────┬───────────┘
                    ↓
         ┌─────────────────────┐
         │   生成式 AI（LLM）     │
         │                      │
         │  輸入：               │
         │  - 要教的概念：分數加法  │
         │  - 學生興趣：籃球      │
         │  - 學生程度：中等      │
         │                      │
         │  輸出：               │
         │  「NBA 球員的罰球命中率 │
         │   是 3/4，如果他再投進  │
         │   2 球...」           │
         └──────────┬──────────┘
                    ↓
         ┌─────────────────────┐
         │  Guide 人工審核        │
         │  確認內容正確 + 課綱對齊 │
         └──────────┬──────────┘
                    ↓
              學生開始學習
                    ↓
         ┌─────────────────────┐
         │  學習結果回饋           │
         │  → 更新 Knowledge Graph│
         │  → 更新 Interest Graph │
         └─────────────────────┘
```

---

#### 四、設計上的關鍵挑戰與取捨

| 挑戰 | 說明 | 可能的解法 |
|------|------|-----------|
| **知識圖譜冷啟動** | 新學生沒有歷史資料 | 自適應診斷測驗（20-60 題快速定位） |
| **興趣圖譜冷啟動** | 不知道學生喜歡什麼 | 入學問卷 + 前兩週探索期 |
| **生成式內容品質** | LLM 可能產出錯誤或不適當的內容 | Guide 人工審核 + 安全過濾器 |
| **遺忘建模** | 學生會遺忘已掌握的內容 | FIRe 演算法 + 間隔複習排程 |
| **興趣漂移** | 學生的興趣會隨時間改變 | 權重衰減 + 定期探索新主題 |
| **關聯干擾** | 同時學太相似的概念會混淆 | 任務選擇演算法避開高度相關的概念 |
| **隱私風險** | 大量行為數據的收集 | 這是 Alpha 被批評最多的點之一 |

### 2.7 下午工作坊：24 項生活技能

上午完成學科學習後，下午由 Guide 帶領進行專題式工作坊，涵蓋 **24 項生活技能**：

| 類別 | 技能範例 |
|------|----------|
| 溝通表達 | 公開演說、故事敘述 |
| 商業思維 | 創業精神、財務素養 |
| 科技創造 | 程式設計、動畫工作室（Alpha Animation Studios） |
| 團隊協作 | 領導力、團隊合作 |
| 心理素質 | 毅力（Grit）、適應力 |
| 戶外教育 | 戶外探索活動 |
| 創意專案 | Alpha 顧問公司、Lyrical Genius 等模擬專案 |

### 2.7 批評與爭議

#### 缺乏獨立研究驗證
- 史丹佛大學教育學院副教授 Victor Lee 指出：Alpha **拒絕讓任何獨立研究機構評估其成效**
- 學業成長數據皆為學校自行公布，未經同行評審

#### 多州拒絕特許學校申請
- 賓州、阿肯色、北卡、猶他、南卡等州均拒絕其特許學校申請
- 賓州教育部指出：「該 AI 教學模式基本上未經驗證」

#### Guide 專業能力不足
- 當 AI 軟體無法有效教學時，Guide 缺乏學科專業知識來進行補救教學
- Guide 是「引導者和文化建設者」，而非具備學科認證的教師

#### 學生心理健康疑慮
- 部分家長反映：以數據指標驅動的模式讓孩子產生焦慮
- 有孩子為了提高 App 上的指標而熬夜，導致壓力過大

#### 隱私與監控疑慮
- 學習過程中透過攝影鏡頭監控學生
- App 追蹤滑鼠移動、眼球動向等行為來判斷學生是否專注

#### 寫作能力短板
- AI 擅長處理練習與測驗，但在寫作教學方面存在不足
- 轉學生普遍在段落寫作與論述能力方面較弱

#### 選擇偏差質疑
- 教育評論家 Dan Meyer 指出：Alpha 可能並非「取代了教師」，而是「換了一批學生」
- 能適應自主 AI 學習的孩子本來就不太需要教師，真正需要教師的孩子反而不適合這個模式
- 花高昂學費送孩子來的家庭本身就有較高教育參與度，造成選擇偏差

---

### 2.8 Alpha School 教材設計的六大創新總結

| # | 創新之處 | 說明 |
|---|----------|------|
| 1 | **雙圖譜即時教材生成** | 結合知識圖譜 + 興趣圖譜，用生成式 AI 為每個學生即時產出獨特教材，非預製內容 |
| 2 | **興趣驅動的情境學習** | 將學科知識嵌入學生個人興趣情境中（籃球教幾何、Taylor Swift 教分數），大幅提升參與度 |
| 3 | **25 分鐘結構化學習區間** | 類似番茄鐘，將學習切成高專注短區間，配合休息，維持最佳注意力 |
| 4 | **AI 行為分析即時輔導** | 不只看正確率，還分析學習行為模式（是否跳過解釋、回答速度等）並即時給予個人化指導 |
| 5 | **遊戲化多巴胺驅動機制** | 進度環、Alpha Bucks、個人化動機適配，讓學習體驗接近電玩遊戲的成癮性 |
| 6 | **視覺 AI 專注度監控** | 用攝影鏡頭 + 視覺模型偵測分心，即時提示自我修正，模擬真人教師的「盯場」功能 |

---

## 三、其他 AI 教育工具與趨勢

### 3.1 Khan Academy — Khanmigo

- 基於 GPT-4 打造的 AI 教學助手
- 2024-25 學年使用人數從 4 萬躍升至 **70 萬**，預計 2025-26 超過 **100 萬**
- 特點：不直接給答案，引導學生思考
- 新功能：可上傳數學/科學題目圖片獲得個人化輔導
- 挑戰：創辦人 Sal Khan 坦承對很多學生來說 Khanmigo 仍是「可有可無」

### 3.2 IXL Learning

- 全球最多人使用的 K-12 訂閱制學習平台，超過 **1,800 萬學生**
- 涵蓋數學、語文、科學、社會、西班牙語共 17,000+ 主題
- 德州公立學校研究：使用 IXL 的學校在 STAAR 測驗中數學高出 **11 百分位**、閱讀高出 **17 百分位**

### 3.3 各州 AI 教育計畫

| 州 | 計畫內容 |
|----|----------|
| 康乃狄克 | 2025 春季在 7 個學區啟動 AI 試點計畫 |
| 愛荷華 | 投資 **300 萬美元** 為全州小學提供 AI 閱讀家教工具 |
| 新罕布夏 | 與 Khan Academy 合作，免費提供 Khanmigo 給全州師生 |

### 3.4 整體採用數據（2025 年）

- **54%** 的學生和 **53%** 的核心科目教師已在使用 AI
- **59%** 的教師表示 AI 讓教學更個人化
- AI 學習環境中的學生測驗成績平均提高 **54%**

---

## 四、Alpha School 模式的啟示與反思

### 值得借鏡的理念

1. **精熟學習制**：確保學生真正掌握才進入下一階段，而非按時間推進
2. **自適應個人化**：每個學生都有專屬學習路徑，解決「一刀切」問題
3. **釋放時間給軟技能**：核心學科高效完成後，將時間用於培養真實世界能力
4. **重新定義教師角色**：從知識傳授者轉為引導者與激勵者

### 需要注意的風險

1. **缺乏獨立驗證**：效果數據應由第三方機構獨立評估
2. **社交與情感發展**：過度依賴螢幕學習可能影響人際互動能力
3. **教師專業不可取代**：AI 無法完全替代人類教師在關係建立與深度教學上的角色
4. **公平性問題**：年學費 $10,000-$75,000，普通家庭難以負擔
5. **隱私風險**：大量學生行為數據的收集需要嚴格的隱私保護機制

---

## 五、參考資源

- [Alpha School 官網](https://alpha.school/)
- [Alpha School - Wikipedia](https://en.wikipedia.org/wiki/Alpha_School)
- [CNN: Is AI schooling the future of education — or a risky bet?](https://www.cnn.com/2026/01/29/politics/alpha-school-trump-ai-teaching)
- [CBS Chicago: Alpha Schools enrolling in Chicago](https://www.cbsnews.com/chicago/news/alpha-schools-chicago-ai-classes-no-teachers/)
- [Newsweek: What Happens When Teachers Are Replaced With AI?](https://www.newsweek.com/alpha-school-brownsville-ai-expanding-2063669)
- [Block Club Chicago: An AI School With No Teachers](https://blockclubchicago.org/2026/03/25/an-ai-elementary-school-with-no-teachers-to-open-in-chicago-this-fall/)
- [Cognitive Revolution: 2-Sigma in 2 Hours](https://www.cognitiverevolution.ai/2-sigma-in-2-hours-how-alpha-schools-are-using-ai-to-revolutionize-education/)
- [Hunt Institute: AI Tutoring in Schools](https://hunt-institute.org/resources/2025/06/ai-tutoring-alpha-school-personalized-learning-technology-k-12-education/)
- [Khanmigo by Khan Academy](https://www.khanmigo.ai)
- [Chalkbeat: Sal Khan reflects on AI in schools](https://www.chalkbeat.org/2026/04/09/sal-khan-reflects-on-ai-in-schools-and-khanmigo/)
- [Bloom's 2 Sigma Problem (1984)](https://journals.sagepub.com/doi/10.3102/0013189X013006004)
- [AI Fun Lab: Alpha School Review](https://www.aifunlab.io/learn/alpha-school-review-75k-ai-first-pros-cons-parent-guide)
- [The Week: Alpha School replaces teachers with AI](https://theweek.com/education/alpha-school-replaces-teachers-ai)
- [Michael B. Horn: The AI Behind Alpha School](https://michaelbhorn.substack.com/p/the-ai-behind-alpha-school)
- [Dan Meyer: The Truth About 2 Hour Learning](https://danmeyer.substack.com/p/the-truth-about-2-hour-learning-and)
- [Alpha School: How AI Tutors Make Every Lesson Personal](https://alpha.school/blog/learning-at-the-speed-of-thought-how-ai-tutors-make-every-lesson-personal/)
- [Alpha School: How AI and Gamification Transform Learning](https://alpha.school/blog/how-ai-and-gamification-transform-learning-at-alpha-school/)
- [Alpha School: Life Skills Workshops](https://alpha.school/lifeskills-workshops/)
- [The 74: How Alpha Uses AI to Rethink the School Experience](https://www.the74million.org/article/how-alpha-uses-ai-to-rethink-the-school-experience/)
- [Alpha School Featured in Nature](https://www.prnewswire.com/news-releases/alpha-school-featured-in-the-prestigious-science-journal-nature-as-a-template-for-schools-of-tomorrow-302639796.html)
- [Math Academy: How Our AI Works](https://mathacademy.com/how-our-ai-works)
- [How Math Academy Creates its Knowledge Graph](https://www.justinmath.com/how-math-academy-creates-its-knowledge-graph/)
- [Stanford: Deep Knowledge Tracing (DKT)](https://stanford.edu/~cpiech/bio/papers/deepKnowledgeTracing.pdf)
- [ACM: Knowledge Tracing Survey](https://dl.acm.org/doi/10.1145/3569576)
- [Nature: Knowledge Graph Learning Path Recommendation](https://www.nature.com/articles/s41598-025-17918-x)
- [Digital Promise: How AI Detects Student Engagement](https://digitalpromise.org/2024/07/03/how-ai-detects-student-engagement-to-transform-classrooms/)

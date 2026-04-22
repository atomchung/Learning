# Heptabase 設計思路研究：點到面的學習設計可借鑑之處

> 研究時間：2026 年 4 月｜目的：從 Heptabase 的設計哲學中萃取「從點到面」的學習設計原則

## 一、Heptabase 的根本命題

創辦人詹雨安（Alan Chan）反覆強調的兩句話，是整套產品設計的北極星：

1. **「不是如何學得更快，而是如何能學會更複雜、更抽象、更具挑戰性的知識。」**
2. **「建立一個任何人都能對任何事物建立深度理解的世界。」**

這兩句話決定了 Heptabase 的設計不是最佳化「做筆記」，而是最佳化「理解」。兩者的差異，是所有學習設計都應該先釐清的起點。

## 二、從點到面：三層空間結構

Heptabase 用三層結構對應「點→線→面」的認知過程：

| 層次 | 元件 | 學習意義 |
|------|------|---------|
| **點** | Card（卡片） | 原子化的單一概念，一張卡片只講一件事 |
| **線** | Link / Arrow / Backlink | 概念之間的關係（因果、對比、從屬、引用） |
| **面** | Whiteboard（白板） | 一個主題的空間地圖，卡片在其上被「擺放」出結構 |
| **體** | Journey / Section / Tag | 跨白板的脈絡、章節分區、類別索引 |

**關鍵洞察：面不是卡片的容器，而是卡片之間「關係」的顯影**。白板的價值在於讓空間位置本身成為語意——靠近代表相關、分群代表類別、箭頭代表推論。這是文字線性筆記做不到的。

## 三、五階段知識生命週期（Knowledge Lifecycle）

> Explore → Collect → Think → Create → Share

Heptabase 主張這五個環節不該被切成五個不同工具，而要在同一個空間中無縫流轉，並且**保留每個想法背後的思考脈絡（context-tracing）**。

| 階段 | 對應行為 | 設計原則 |
|------|---------|---------|
| Explore | 網路探索、閱讀 | 把原始素材帶進系統，不只存連結，要存「為什麼」 |
| Collect | Highlight、剪貼、PDF 標註 | 收集的最小單位是「可再組合」的片段 |
| Think | 白板上拉卡、排位置、畫箭頭 | 視覺化是澄清思考的必要條件，不是裝飾 |
| Create | 基於卡片寫文章、簡報 | 產出是卡片的「再組裝」，不是從零開始 |
| Share | 分享白板 / 文章 / 知識圖 | 分享的是理解路徑，不只是結論 |

**關鍵洞察：創作不是生產的起點，而是思考過的副產品**。如果學習設計把「輸出」擺在最後當收尾，會錯過讓輸出反向驅動理解的機會。

## 四、可借鑑的七個設計原則

### 1. 原子化（Atomicity）
一張卡片只描述一個概念，且標題必須是「一句話能說完的概念句」。這強迫你在寫下的當下就完成第一次壓縮與理解。
> 對學習設計的啟示：每一個學習單元應該能用一句話回答「這裡在講什麼」。做不到，就是還沒消化。

### 2. 由下而上（Bottom-up）
Heptabase 不要求使用者先設計目錄、大綱、分類樹，而是從一張卡片開始，讓結構從卡片之間的關係浮現。
> 對學習設計的啟示：先別急著畫心智圖框架。讓學習者先放一堆原子筆記，結構會自己長出來，而且那個結構才是真實的。

### 3. 起點白板（Starting Point Whiteboard）
學新主題時，Heptabase 建議先開一塊白板，中間放一張「起點卡」（題目本身），然後所有讀到的東西都往這張卡裡塞；當它膨脹到看得出有幾個子概念時，再拆成小卡排開。
> 對學習設計的啟示：**不要預先切好章節**。先膨脹再拆分，能還原概念真實的連結方式，而不是教科書硬切出來的分類。

### 4. 脈絡保留（Context-tracing）
同一張卡片可以同時出現在多個白板上，代表同一個概念在不同主題脈絡下的運用。Heptabase 會讓你看到這張卡片「在哪些地方被用過」。
> 對學習設計的啟示：判斷學會了沒，看的不是「記得不記得」，而是**能不能在新的脈絡中再次召喚這個概念**。設計練習時應該主動讓同一概念出現在多個情境。

### 5. 視覺空間即語意（Spatial Semantics）
白板上兩張卡的距離、方向、分群，本身就是思考的一部分。這比寫「A 導致 B」更直接，也更容易被重新排列。
> 對學習設計的啟示：盡量讓學習素材可以被「移動」。紙上畫框、白板貼便利貼、Miro、FigJam 都比純文字筆記更能激發結構性思考。

### 6. Journey：記錄思考的路徑
Heptabase 的 Journey 功能會保留白板的歷史狀態，讓人可以回看「我當初是怎麼想到這一步的」。
> 對學習設計的啟示：**過程比結論更值得存檔**。學習筆記裡應該保留「我當時搞錯了什麼、後來怎麼發現的」，這是複習時最有價值的內容。

### 7. 深度 > 效率
詹雨安明確反對「AI 幫你總結 10 本書」這種效率敘事，他認為 AI 的價值在於「讓過去摸不到的難知識變得可以理解」。
> 對學習設計的啟示：衡量學習效果不要用「讀完幾本」，而是「能不能處理一個月前不敢碰的題目」。

## 五、套用到「我們的學習設計」：三個具體建議

結合這個 repo 已有的 `compare-coding-agents.md`（偏結構性分析長文）來推論你可能想建立的學習節奏，以下是具體可落地的做法：

### 建議 1：把長文拆成「卡片庫」
`compare-coding-agents.md` 這類長文其實是最終產物（Create 階段）。往回推，它應該是由一批原子卡片組成的——例如：
- 「Codex 的無網路沙箱決定了它適合非同步但不適合私有 API」
- 「Antigravity 的三面架構把瀏覽器帶進 agent 視野」
- 「Claude Code 的人機確認機制是 agent 安全的一種設計答案」

把這些提煉成獨立的 atomic cards 後，下一次寫新主題（例如「AI Agent 的信任模型」）時就能直接重組，而不是重寫。

### 建議 2：用「起點白板」的結構規劃學習主題
與其一開始就規劃「Week 1 講 X、Week 2 講 Y」，不如：
1. 開一個學習白板，中心放一張題目卡（e.g.「我想理解 coding agent 的設計權衡」）
2. 每天讀到的東西先塞進題目卡（膨脹階段）
3. 每週末把卡片拆出來、擺位置、畫關係（結構浮現階段）
4. 當白板開始有 2–3 個明顯的 cluster 時，那就是章節

這能讓學習地圖從真實閱讀中長出來，而非被預設框架框住。

### 建議 3：為每個學習主題保留 Journey
建一個 `journey/` 目錄，每週存一份當下對主題的理解快照（不是筆記，是「目前我認為的答案」）。三個月後回看會發現：
- 哪些直覺是對的
- 哪些誤解花了多久才修正
- 什麼資訊是讓理解跳躍的轉折點

**這份 journey 本身就是你學習能力的元筆記**，比任何一張卡片都值錢。

## 六、一句話帶走

> **Heptabase 的核心不是「卡片 + 白板」，而是「讓結構從使用中浮現，而非預先規劃」**。套在學習設計上就是：**別急著排課綱，先讓原子問題多到擠在一起，章節會自己出現**。這就是「從點到面」真正的意思——面不是規劃出來的，是點累積到一定密度後自己形成的。

## 參考資料

- [My Vision: Heptabase — Alan Chan](https://medium.com/heptabase/my-vision-project-meta-e0bedd1467b2)
- [The Best Way to Use AI for Learning — Alan Chan](https://medium.com/heptabase/the-best-way-to-use-ai-for-learning-762c3467bdf1)
- [How Heptabase's founder uses Heptabase](https://medium.com/heptabase/how-heptabases-founder-use-heptabase-for-learning-research-planning-and-writing-b11b1829ff79)
- [The Knowledge Lifecycle — Heptabase Wiki](https://wiki.heptabase.com/the-knowledge-lifecycle)
- [Learn & research a topic — Heptabase Wiki](https://wiki.heptabase.com/the-best-way-to-acquire-knowledge-from-readings)
- [Fundamental Elements — Heptabase Wiki](https://wiki.heptabase.com/fundamental-elements)
- [Interview with Alan Chan — Ness Labs](https://nesslabs.com/heptabase-featured-tool)
- [Heptabase 完整介紹 — Pinchlime](https://pinchlime.com/heptabase-introduction/)
- [Heptabase 視覺系筆記 — Ernest Chiang](https://www.ernestchiang.com/zh/posts/2021/heptabase/)
- [Heptabase 詹雨安如何管理筆記 — 經理人](https://www.managertoday.com.tw/articles/view/68559)

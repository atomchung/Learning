# 好流暢 vs 好學習：為什麼 `/learn` 不用蘇格拉底法

> 2026-09-18
>
> 起點是一個懷疑：`/learn` 這套設計跟蘇格拉底法、跟「學習」這件事有任何關係嗎？
> 答案是沒有關係，而且方向相反——但它站在另一條學術路線上，而且那條線直接反對蘇格拉底法。

## 一句話

**教學效率和記憶效果是兩條不同的學術路線。** 優化前者不等於違反後者，因為 Bjork 自己的理論就帶著「先備知識」這個前提。

## 先確認它確實不是蘇格拉底法

蘇格拉底法的核心是 elenchus（反詰法）：老師不給答案，靠提問讓學生自己撞上矛盾，知識由學生產出（maieutics，助產術）。

`/learn` 的三條紅線第一條是「不要在教之前先問澄清問題」，另外明寫「不要出考題」。一步的規格是我給判斷句、我給理由、我給例子，然後停。糾錯機制是**使用者打斷**，不是使用者推導。

方向相反，不是變體。

## 兩條線分別在問什麼

**記憶效果那一系**問：怎麼讓人三個月後還記得？

- 提取練習（retrieval practice）：自己回想比重讀有效，是該領域效果量最紮實的發現之一
- 間隔重複（spaced repetition）
- 合意困難（desirable difficulties，Bjork）：刻意讓學習當下變難，換取長期保留

**教學效率那一系**問：怎麼讓人用最少的認知資源把一件事弄懂？

- 認知負荷理論（cognitive load theory，Sweller 1988）
- 範例效應（worked example effect，Sweller & Cooper 1985）
- 專業反轉效應（expertise reversal effect，Kalyuga 等 2003）

`/learn` 整份站在第二條線上。

## 直接支持這個設計的四條

**1. 認知負荷理論。** 工作記憶容量有限，教學設計的首要工作是削掉 extraneous load——跟學習內容本身無關、純由呈現方式造成的負擔。`/learn` 的一步 150 字上限、不附選單、不重貼進度清單，做的都是這件事。

**2. 範例效應。** 新手學習時，讀一個完整的解題範例比自己動手解更有效，而且更省時。這支持「直接給判斷句 + 一個具體例子」勝過「用提問讓他自己推出來」。

**3. Kirschner, Sweller & Clark (2006)。** 最直接的一篇，論旨是最小指導的教學不管用，點名批評 discovery learning、inquiry-based learning、problem-based learning，主張人類認知架構決定了新手需要 direct instruction。**蘇格拉底式教學正是它批評的那一類。**

這篇要標：它是該領域有名的爭議點，Hmelo-Silver 等人 2007 有正式反駁，主張問題導向學習內建 scaffolding、不算最小指導。所以是有力但未定論的支持。

**4. 專業反轉效應。** 對新手有效的方法（給完整指導）對專家反而有害，反之亦然。這替檔位機制背書——檔位判準實際上在估你對這題的先備知識，檔位 0 就是「你已經夠熟，別教」。

## 對得上 decision-driven 的一條

成人學習理論（andragogy，Knowles）：成人學習者是 problem-centered 而非 subject-centered，要能立即應用，而且需要先知道「為什麼要學這個」。

`/learn` 裡「一句：為什麼這跟你的問題有關」，以及整個「要改變你的判斷，最少需要幾件事」的框架，都落在這條上。

## 和解點：Bjork 自己的前提

合意困難有一個常被漏掉的限定：**困難只在學習者有足夠的先備知識和資源去克服它時，才是 desirable。** 克服不了的困難就變成 undesirable difficulty，直接損害學習。

所以「好學習」和「好流暢」不是二選一，是**順序**問題：不熟的主題先把門檻壓低建立框架，等有了框架再加難度。

使用者的原話（2026-09-18，已寫進 SKILL.md 當取捨理由）：

> 本質上我們就是要好學習，但也要好流暢，不要讓學每個東西的成本變得很高。

在這個框架下，這不是妥協，是階段選擇。

## 代價：流暢度錯覺

fluency illusion（Koriat & Bjork）：處理得越順暢，人對自己掌握程度的判斷越容易高估。

這是 `/learn` 的結構性代價，沒有對策。目前唯一的緩解是收束段誠實寫「還不確定」和「哪裡是推測不是查證」，這條已經寫進 SKILL.md 並註明「要補對策就補在那裡，不要改成出考題」。

記憶則外包給 repo（inbox / profile / notes），與「這個 repo 是我的腦」一致。

## 證據強度

**上面的文獻全部是憑記憶轉述，沒有打開任何一篇原文。** 作者、年份、論點方向我有信心，但精確措辭與效果量要引用就得查原文。按這個 repo 的篩子第四格，現在這份是二手層不是一手層。

同場抓到的缺陷：`notes/ai-education-research.md` 第 26 行早就有 Bloom 1984 的 2 Sigma 問題（一對一輔導比群體教學好 2 個標準差、803 行附論文連結），09-16 建 skill 時完全沒撈——記在 `meta/defects.md`（retrieval-miss 第 5 次）。

決定不把 Bloom 接進 SKILL.md：2 Sigma 只替這個 skill 的存在背書，不改變任何一條現行規則，按 skill 自己「不寫也會發生嗎」的標準不該加。

## 相關

- [decision-learning-from-wondering](./decision-learning-from-wondering.md) — `/learn` 的真正血統（決策分析，不是教育學）
- [ai-education-research](./ai-education-research.md) — repo 裡既有的教育研究筆記，含 Bloom 2 Sigma
- `.claude/skills/learn/SKILL.md` — 「有意不做的」一節即本篇的結論

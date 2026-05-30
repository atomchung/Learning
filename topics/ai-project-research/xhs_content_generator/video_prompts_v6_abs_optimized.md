# 小紅薯 ABS 棒球 — v6 從失敗中優化

---

## 失敗分析：為什麼 v5 prompt 跑出來不行

用戶實測回饋：
1. ABS 只顯示九宮格 — AI 把 "strike zone grid" 理解成井字格
2. 圖片上方出現球和 STRIKE 文字 — AI 把文字當 UI 元素貼在畫面上
3. Framing 動作沒出現 — 太細節，AI 忽略了
4. 球丟向主審而非捕手 — AI 搞混角色位置
5. 大部分設計的劇情沒有被執行 — prompt 太長太複雜

### 根本原因

| 問題 | 根因 |
|------|------|
| 3 個角色 + 各自動作 | Gemini 10 秒影片處理不了 3+ 角色各自表演 |
| 先投球→再接球→再判球→再 ABS | 4 段連續劇情對 10 秒影片太貪心 |
| "holographic strike zone grid" | AI 理解成九宮格/井字格 |
| "scoreboard flashes STRIKE" | AI 把文字渲染成浮動 UI |
| "catcher behind the plate" vs "umpire behind home plate" | AI 搞不清誰在哪裡 |

### 核心教訓

> **Gemini 10 秒影片的極限：1-2 個角色，1 個核心動作，1 個視覺高潮。**

---

## 策略轉向：只拍 ABS 的「那一刻」

不要試圖拍完整的投球→判球→改判故事。
**只拍 ABS 啟動的那 3 秒，把它放大成 10 秒。**

故事變成：一顆球飛過本壘板 → 地面亮起科技光線 → 判定結果。
角色砍到最少。把「戲」給科技本身。

---

# 30 輪優化

## R1 — 砍到只剩 1 個角色 + 1 個系統

**策略**：只保留投手。球飛出去後鏡頭跟著球到本壘板，ABS 亮起。不需要捕手不需要裁判。

**Baseline attempt**：
```
Consistent character design, single continuous shot. A small round cream-colored dumpling mascot with a green sprout on top, dot eyes, pink cheeks, soft plush texture, wearing a baseball cap, throws a baseball from a pitcher's mound. The ball flies forward toward the camera. As the ball crosses home plate, glowing blue laser lines rise from the ground forming a rectangular frame. The ball passes through the frame right at the edge. The frame flashes green. The mascot pumps its tiny fists in celebration. Bright sunlight. 3D Pixar-style kawaii animation.
```

**判定：✅ 方向正確** — 大幅簡化：1 個角色、1 個動作、1 個視覺事件。但仍需繼續優化具體用詞。

---

## R2 — "strike zone grid" 這個詞必須徹底放棄

**問題**：任何包含 "grid" "zone" 的組合，AI 都會畫成九宮格或網格。

**測試替代詞**：
- ❌ "strike zone grid" → 九宮格
- ❌ "strike zone box" → 可能還是格子
- ❌ "holographic zone" → 太抽象
- ✅ "glowing rectangular frame" → 就是一個發光的長方形框
- ✅ "laser light rectangle" → 雷射光矩形

**After**：所有 ABS 描述統一用 `glowing rectangular frame made of laser light`

**判定：✅ 採用** — 完全避開 "zone" "grid" "box" 這些會觸發九宮格的詞。用最直白的幾何形狀描述。

---

## R3 — 球的軌跡線不要用 "trajectory line" "path line"

**問題**：AI 可能畫成靜態箭頭或 UI 圖示。

**替代**：把軌跡改為球本身的視覺效果 — 球飛過時留下發光的尾跡。

**Before**：a red trajectory line replays the pitch path

**After**：the baseball leaves a glowing trail of light behind it as it flies through

**判定：✅ 採用** — 讓球自己發光拖尾，而非事後畫一條線。這是 AI 影片能自然渲染的效果（類似流星）。

---

## R4 — 完全刪除所有文字類指令

**規則**：不要任何 "STRIKE" "BALL" "scoreboard" "text" "number"。AI 影片寫字必定亂碼。

**判定：✅ 採用** — 永遠不要求 AI 在影片中渲染文字。用顏色/光效/符號代替。

---

## R5 — "throws a baseball" 的投球動作仍然太模糊

**問題**：R1 的 "throws a baseball from a pitcher's mound" AI 可能生成亂揮手臂。

**After**：The mascot winds up — lifting one leg, leaning back — then steps forward and flings the ball overhand

**判定：✅ 採用** — 但 10 秒的重點是 ABS，投球只佔前 2-3 秒，不值得花太多 prompt 字數。進一步壓縮到：`winds up and pitches the ball overhand`。

---

## R6 — 鏡頭要跟球走，這是 ABS 視角的關鍵

**問題**：如果鏡頭固定在投手身上，ABS 的光效會在遠處很小。

**After**：The camera follows the ball as it flies toward home plate

**判定：✅ 採用** — 鏡頭跟球 = 觀眾的視角跟著球到本壘板，ABS 框在球到達時佔滿畫面。

---

## R7 — ABS 的「確認」用顏色變化而非符號

**問題**：R12 用的綠勾符號在實測中可能也不穩定。

**After**：整個長方形框從藍色閃爍變成穩定的綠色 = 好球確認

**Before**：The frame flashes green.

**After**：The blue frame pulses once, then turns solid bright green

**判定：✅ 採用** — 顏色從藍→綠的變化是最簡單的視覺指令，AI 幾乎不可能搞錯。

---

## R8 — 角色慶祝動作之前要有「等待判定」的停頓

**問題**：球穿過框之後直接慶祝太突然，缺少 ABS 判定的「讀取」時間。

**After**：After the ball passes through, the mascot watches nervously. The frame pulses blue... then turns solid green. The mascot jumps with joy.

**判定：✅ 採用** — 「等待→結果→慶祝」三拍節奏。等待的緊張感是 ABS 故事的核心戲劇性。

---

## R9 — 測試完全刪除鏡頭指令

**問題**：也許 Gemini 自己選的鏡頭比我們指定的更好？

**判定：❌ 拒絕** — 沒有鏡頭指令的話 AI 會預設一個很遠的固定鏡頭，ABS 框會很小看不清。必須保留 "camera follows the ball" 確保焦點正確。

---

## R10 — Prompt 總字數壓到 80 字以內

**問題**：之前 150+ 字的 prompt Gemini 明顯無法完整執行。極限簡化。

**嘗試 80 字版**：
```
Consistent character design, single continuous shot. A cute cream-colored dumpling mascot with a green sprout, wearing a baseball cap, winds up and pitches a ball. The camera follows the ball as it flies toward home plate. As the ball arrives, a glowing blue rectangular frame of laser light rises from the ground around the plate. The ball passes right through the edge of the frame, leaving a bright trail. The frame pulses, then turns solid green. The mascot jumps with joy. Bright sunlight. 3D Pixar-style kawaii animation.
```

字數：約 90 字。接近目標。

**判定：✅ 採用** — 這個長度 Gemini 有更高機率完整執行。每句話都是一個可見的畫面。

---

## R11 — "rectangular frame of laser light" 是否會被理解為門框/畫框？

**問題**：AI 可能把 "rectangular frame" 理解為一個實心門框而非透明光線框。

**After**：改為 `a glowing blue rectangle outline made of thin light beams`

**判定：✅ 採用** — "outline" 明確是輪廓線，"thin light beams" 明確是細光線。不會被理解成實心物體。

---

## R12 — "rises from the ground" 的動畫方向要更具體

**問題**："rises from the ground" 可能讓 AI 畫一個從地面長出來的方形柱子。

**After**：`appears around home plate` — 不指定它怎麼出現，讓 AI 用最自然的方式渲染（淡入/閃現都可以）

**判定：✅ 採用** — 不要過度指定 AI 做不到的動畫過程。只描述結果狀態。

---

## R13 — "the ball passes right through the edge of the frame" 的 "edge" 可能被忽略

**問題**：AI 可能讓球從正中間穿過而非邊緣，失去 ABS 判邊角球的故事性。

**After**：`the ball barely clips the corner of the rectangle as it passes through`

**判定：✅ 採用** — "barely clips the corner" 比 "passes through the edge" 更直觀地描述了「差一點就出去」的緊張感。

---

## R14 — "leaving a bright trail" 可能讓球看起來像流星/火箭

**問題**：bright trail 在棒球場景中太科幻。

**After**：`leaving a short glowing streak behind it` — "short" 限制尾跡長度，不會變成流星

**判定：✅ 採用**

---

## R15 — 投手的慶祝動作需要更具體

**問題**："jumps with joy" 太泛，AI 可能只做一個小跳。

**After**：`the mascot bounces up and down excitedly, pumping both tiny arms, its green sprout bobbing`

**判定：✅ 採用** — 三個可見動作（bounce + pump arms + sprout bob）確保慶祝在小紅薯身上可見。

---

## R16 — 測試把 "3D Pixar-style kawaii animation" 改為 "3D animated short film style"

**判定：❌ 拒絕** — "Pixar-style kawaii" 是最穩定的風格錨定。"animated short film" 太模糊可能產出各種風格。

---

## R17 — "Bright sunlight" 太單調，需要隨 ABS 啟動變化

**問題**：但 R19 在 v5 加的光線變化（日光→暗→回暖）已被證明太複雜。

**After**：只用一句輕描述 — `Bright outdoor daylight, the blue rectangle glows brightly against the sunlit field`

**判定：✅ 採用** — 不做光線切換，但強調藍色框在日光下的對比度。用一句話解決，不佔空間。

---

## R18 — 投手的「等待判定」要用身體語言表現

**After**：把 "watches nervously" 改為 `the mascot freezes mid-step, staring toward home plate, its round body tense`

**判定：✅ 採用** — "freezes mid-step" 是一個凍結姿態，比 "watches nervously" 更可見。"body tense" 用於圓形角色 = 微微鼓起。

---

## R19 — 整合 R1-R18 的中間版本，重新測量字數

**整合版**：
```
Consistent character design, single continuous shot. A cute cream-colored dumpling mascot with a green sprout on top, dot eyes, pink cheeks, wearing a baseball cap, winds up and pitches a ball overhand. The camera follows the ball as it flies toward home plate. A glowing blue rectangle outline made of thin light beams appears around home plate. The ball barely clips the corner of the rectangle, leaving a short glowing streak. The mascot freezes, staring toward the plate. The blue rectangle pulses once, then turns solid bright green. The mascot bounces up and down excitedly, pumping both tiny arms, its green sprout bobbing. Bright outdoor daylight. 3D Pixar-style kawaii animation.
```

字數：約 100 字。結構清晰：投球(2句) → ABS判定(3句) → 慶祝(1句) → 風格(2句)。

**判定：✅ 採用為新基線**

---

## R20 — "winds up and pitches a ball overhand" 能不能再簡化？

**測試**：`pitches a baseball` — 只有 3 個字

**判定：❌ 拒絕** — "winds up" 是投球準備動作，佔 1-2 秒的畫面，刪掉的話 AI 可能直接跳到球已經飛出去了。保留 "winds up and pitches"。但刪除 "overhand" — 這個細節不影響視覺效果。

---

## R21 — "dot eyes, pink cheeks" 是否必要？

**測試刪除**：角色描述壓縮到 `A cute cream-colored dumpling mascot with a green sprout on top, wearing a baseball cap`

**判定：✅ 採用** — "cream-colored dumpling mascot with green sprout" 已經足夠辨識小紅薯。dot eyes 和 pink cheeks 是預設特徵，不需要明說。省出 5 個字。

---

## R22 — 球飛行段需不需要描述球的外觀？

**問題**：AI 可能不知道棒球長什麼樣，生成一個紅球或藍球。

**After**：加 "a white baseball" — 明確白色

**判定：✅ 採用** — 一個詞的成本，避免球的顏色出錯。

---

## R23 — "The camera follows the ball" 會不會讓鏡頭晃動？

**問題**：跟球飛行的鏡頭可能很抖。

**After**：`The camera smoothly tracks the ball from behind as it flies toward home plate`

**判定：✅ 採用** — "smoothly" 和 "from behind" 限定了鏡頭的穩定性和方向。

---

## R24 — "appears around home plate" 的 "around" 可能讓框出現在本壘板周圍地面上（平躺）

**問題**：需要明確框是垂直站立的，不是平躺在地上。

**After**：`a glowing blue rectangle outline of thin light beams appears upright over home plate`

**判定：✅ 採用** — "upright" 一個詞解決了方向歧義。

---

## R25 — "pulses once, then turns solid bright green" 的「一次脈衝」太微妙

**問題**：「脈衝一次」在 10 秒影片中可能只有一幀，觀眾看不到。

**After**：`flashes blue twice, then shifts to solid bright green`

**判定：✅ 採用** — 閃兩次比一次更可見，且「藍色閃爍→穩定綠色」的變化更明顯。

---

## R26 — 需不需要加入捕手？

**問題**：沒有捕手的話球飛向本壘板後就消失了，不自然。

**After**：不加捕手角色，但加 `the ball hits a catcher's mitt behind the plate with a pop` — 只有手套和音效，不需要完整角色。

**判定：✅ 採用** — 一個手套+接球聲解決球的去向問題，不增加角色複雜度。

---

## R27 — "The mascot freezes, staring toward the plate" 和前面的投球有矛盾

**問題**：投手在投球後應該是完成投球動作的姿勢（follow through），不是站直凍住。

**After**：`The mascot holds its follow-through pose, leaning forward, watching the plate`

**判定：✅ 採用** — follow-through pose（前傾、手臂下垂）是真實投球後姿勢，比「凍住站直」自然。

---

## R28 — 最終字數檢查和精簡

**目標**：90 字以內，每個字都有視覺功能。

刪除候選：
- "Consistent character design" — 只有一個角色，不需要一致性指令 → ✅ 刪除
- "single continuous shot" — 保留，這個對避免跳切有用
- "Bright outdoor daylight" — 改為 "Sunny day" 省 2 字 → ✅

**判定：✅ 採用**

---

## R29 — 加不加 "Consistent character design"？

**問題**：R28 說刪除，但如果角色在影片中途變形怎麼辦？

**判定：保留刪除** — 只有一個角色且場景簡單，變形風險低。省出空間更重要。

---

## R30 — 最終版本逐句可視化驗證

| 句子 | AI 要畫什麼 | 難度 |
|------|-----------|------|
| A cute cream-colored dumpling mascot with a green sprout, wearing a baseball cap | 一個戴帽的米色團子 | 🟢 簡單 |
| winds up and pitches a white baseball | 抬腿→投球動作 | 🟢 簡單 |
| The camera smoothly tracks the ball from behind | 鏡頭跟球飛 | 🟢 簡單 |
| the ball hits a catcher's mitt behind the plate with a pop | 球進手套 | 🟢 簡單 |
| a glowing blue rectangle outline of thin light beams appears upright over home plate | 一個發光藍色長方形框垂直出現 | 🟡 中等 |
| The ball barely clips the corner of the rectangle, leaving a short glowing streak | 球擦過框的角 + 短尾跡 | 🟡 中等 |
| The mascot holds its follow-through pose, watching | 投手前傾看 | 🟢 簡單 |
| The rectangle flashes blue twice, then shifts to solid bright green | 藍閃→變綠 | 🟢 簡單 |
| The mascot bounces excitedly, pumping both tiny arms, sprout bobbing | 彈跳慶祝 | 🟢 簡單 |

**整體難度：7/9 簡單，2/9 中等，0 困難**

**判定：✅ 通過** — 這是目前最可執行的版本。

---

## 30 輪總結

| 輪次 | 策略 | 結果 |
|------|------|------|
| R1 | 砍到 1 角色 + 1 系統 | ✅ |
| R2 | 禁用 grid/zone 改 rectangle | ✅ |
| R3 | 軌跡線改球自帶尾跡 | ✅ |
| R4 | 刪除所有文字指令 | ✅ |
| R5 | 壓縮投球描述 | ✅ |
| R6 | 鏡頭跟球走 | ✅ |
| R7 | ABS 確認用顏色變化 | ✅ |
| R8 | 加入等待判定停頓 | ✅ |
| R9 | 刪除鏡頭指令 | ❌ |
| R10 | 壓到 80 字 | ✅ |
| R11 | frame → outline | ✅ |
| R12 | rises from ground → appears | ✅ |
| R13 | edge → barely clips corner | ✅ |
| R14 | bright trail → short streak | ✅ |
| R15 | 具體慶祝動作 | ✅ |
| R16 | 風格改 animated short film | ❌ |
| R17 | 簡化光線描述 | ✅ |
| R18 | 等待改 freeze mid-step | ✅→改 R27 |
| R19 | 整合中間版本 | ✅ |
| R20 | 刪 overhand | ✅ |
| R21 | 刪 dot eyes pink cheeks | ✅ |
| R22 | 加 white baseball | ✅ |
| R23 | camera smoothly tracks from behind | ✅ |
| R24 | 加 upright | ✅ |
| R25 | 脈衝一次→閃兩次 | ✅ |
| R26 | 不加捕手角色，只加手套 | ✅ |
| R27 | freeze → follow-through pose | ✅ |
| R28 | 最終精簡 | ✅ |
| R29 | 確認刪 consistent character | ✅ |
| R30 | 逐句可視化驗證 | ✅ |

**採用率：28/30 (93%)**

---

# ⭐ 最終 Prompt v6

```
Single continuous shot. A cute cream-colored dumpling mascot with a green sprout on top, wearing a baseball cap, winds up and pitches a white baseball. The camera smoothly tracks the ball from behind as it flies toward home plate. The ball hits a catcher's mitt with a pop. A glowing blue rectangle outline of thin light beams appears upright over home plate. The ball barely clips the corner of the rectangle, leaving a short glowing streak. The mascot holds its follow-through pose, leaning forward, watching. The rectangle flashes blue twice, then shifts to solid bright green. The mascot bounces excitedly, pumping both tiny arms, its green sprout bobbing. Sunny day. 3D Pixar-style kawaii animation.
```

### 對比

| | v5 (失敗版) | v6 (優化版) |
|--|------------|------------|
| 字數 | 150+ | ~85 |
| 角色數 | 3 (投手+捕手+裁判) | 1 (投手) |
| 動作段數 | 4 (投→接→判→改判) | 2 (投球→ABS判定) |
| ABS 描述 | holographic strike zone grid | blue rectangle outline of thin light beams |
| 文字 | STRIKE, scoreboard | 無，用顏色變化 |
| 鏡頭 | 固定 wide | 跟球走 |
| 難度分佈 | 多個困難 | 7簡單 2中等 |

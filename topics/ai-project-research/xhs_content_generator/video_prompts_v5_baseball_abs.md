# 小紅薯棒球 ABS — Gemini 影片 Prompt v5

> 主題：ABS（Automated Ball-Strike System）機器人裁判
> 故事：一顆邊角球，人判壞球，ABS 改判好球
> 目標：1 支 10 秒影片

---

## 角色設計

| 角色 | 外觀差異 | 位置 |
|------|---------|------|
| 投手 | 基底米色團子，大圓堅定眼，戴棒球帽 | 投手丘 |
| 捕手 | 基底米色團子，戴捕手面罩+護具 | 本壘後方 |
| 裁判 | 基底米色團子，較胖較大，戴黑色面罩，粗八字眉 | 捕手後方 |
| 打者 | 基底米色團子，戴打擊頭盔 | 打擊區 |

---

## 劇本分鏡

```
0-2s  【投球】投手站在土丘上，左腳抬起，身體向後傾蓄力，然後重心前移，手臂由上往下揮出球
2-4s  【進壘】球飛過打擊區外角邊緣，白色軌跡線，捕手伸手套穩穩接住，發出「啪」一聲
4-6s  【誤判】裁判大幅度搖頭+右手向外揮 = 壞球手勢，投手攤手不可置信
6-8s  【ABS啟動】打擊區地面亮起藍色全息投影方框，球的飛行軌跡以紅色光線回放，清楚壓在好球帶邊線上
8-10s 【改判】電子螢幕閃爍 "STRIKE"，裁判愣住不動，投手開心彈跳，綠芽搖晃
```

---

# 30 輪優化

## Baseline v5.0

```
Consistent character design, single continuous shot. On a baseball diamond, a small round cream-colored dumpling mascot with a green sprout, dot eyes, pink cheeks, plush texture, wearing a baseball cap, stands on the pitcher's mound. It lifts its left leg, leans back, then drives forward and throws a fastball with a smooth overhand motion. The ball flies across the plate edge — a dumpling catcher in chest gear catches it with a pop. A large dumpling umpire behind home plate shakes its head and waves its arm to signal ball. The pitcher spreads its tiny arms in disbelief. Then a glowing blue holographic strike zone grid lights up over home plate, and a red trajectory line replays the pitch path right on the edge. A digital scoreboard flashes STRIKE. The umpire freezes. The pitcher bounces with joy, its sprout wiggling. Camera holds a wide side angle. Bright daylight. 3D Pixar-style kawaii animation.
```

---

## R1 — 投球動作分解為三個力學階段

**問題**：原版 "lifts its left leg, leans back, then drives forward and throws" 太籠統，AI 會生成模糊的手臂揮動。

**After**：
> It plants its back foot on the rubber, lifts its front knee high to its chest, then strides forward, whips its arm overhead in a smooth arc, and releases the ball from the top.

**判定：✅ 採用** — 分解為 plant → knee lift → stride → arm whip → release 五個階段，每個都是可視化的身體位置，AI 更容易逐幀渲染。

---

## R2 — 球的軌跡需要視覺化速度感

**問題**：原版只說 "the ball flies across the plate edge"，沒有速度感。

**Before**：The ball flies across the plate edge

**After**：The ball rockets toward home plate with a faint white speed trail, clipping the outside corner of the strike zone

**判定：✅ 採用** — "rockets" + "white speed trail" + "clipping the outside corner" 三個具體描述讓球的速度和位置都可見。

---

## R3 — 捕手接球動作需要「手套移動」

**問題**：原版 "catches it with a pop" 沒有描述手套動作，AI 可能生成球自己消失。

**After**：the catcher snaps its round glove shut with a loud pop, pulling the ball inward slightly

**判定：✅ 採用** — "snaps glove shut" + "pulling inward" 是真實捕手接球的動作（framing），增加可信度。

---

## R4 — 裁判的壞球手勢要更誇張

**問題**：小紅薯身體圓滾滾，小幅度搖頭看不出來。

**Before**：shakes its head and waves its arm to signal ball

**After**：the large umpire puffs up its chest, leans forward, and swings its right arm out wide in an exaggerated ball call, shaking its whole round body side to side

**判定：✅ 採用** — 全身搖晃比頭部搖動在圓形角色上更可見。"puffs up chest, leans forward" 是真實裁判報球的前傾姿勢。

---

## R5 — 投手的不滿反應用身體表達

**問題**："spreads its tiny arms in disbelief" 太小的動作。

**After**：The pitcher's whole body deflates like a balloon losing air, its sprout droops down, and it throws both tiny arms up in the air

**判定：✅ 採用** — "deflates like a balloon" 利用了圓形身體的彈性特性，"sprout droops" 用綠芽表達情緒，比攤手更有小紅薯特色。

---

## R6 — ABS 全息投影的視覺描述太模糊

**問題**：原版 "glowing blue holographic strike zone grid" 對 AI 來說太抽象。

**Before**：a glowing blue holographic strike zone grid lights up over home plate

**After**：Suddenly, thin glowing blue neon lines project upward from the ground around home plate, forming a rectangular 3D box — the digital strike zone. Inside the box, a bright red dotted line traces the ball's exact path, showing it just touching the edge of the zone.

**判定：✅ 採用** — 具體描述了線條如何出現（from ground upward）、形成什麼形狀（rectangular 3D box）、球跡如何顯示（red dotted line touching edge）。AI 能根據這些具體指令渲染。

---

## R7 — 鏡頭不應該全程 wide shot

**問題**：wide side angle 全程不變，10 秒很無聊且看不清表情。

**After**：Camera starts at a side wide shot showing the full diamond, then slowly pushes in toward home plate as the ABS activates, ending on a medium close-up of the strike zone hologram and the stunned umpire.

**判定：✅ 採用** — 從全景推到中近景，跟隨故事焦點轉移（投球→本壘板→ABS）。推鏡頭是 AI 影片最穩定的鏡頭運動之一。

---

## R8 — 打者角色完全沒戲，要嘛刪掉要嘛給反應

**問題**：劇本有打者但完全沒動作，白佔 prompt 空間。

**判定：✅ 刪除打者** — 10 秒內已有投手+捕手+裁判三個角色，打者加進去只會讓場景更擁擠。刪除後把空間留給 ABS 視覺效果的描述。

---

## R9 — 加入「啪」的接球音效提示（Veo 3）

**After**：在接球處加 `a satisfying pop sound as the glove closes`，在 ABS 啟動加 `a futuristic electronic hum as the zone appears`

**判定：✅ 採用** — 兩個音效節點讓影片有聲音層次：真實球聲 + 科技音效。

---

## R10 — 時間分配不合理，投球佔太多

**問題**：0-2s 投球，2-4s 進壘接球，前 4 秒只為了「投一顆球」。最有戲的 ABS 部分只剩 4 秒。

**After**：壓縮投球+接球為 0-3s，裁判誤判 3-5s，ABS 啟動+結果 5-10s。在 prompt 中用 "quickly" 修飾投球，用 "then, slowly" 修飾 ABS 部分讓 AI 放慢重點段。

**判定：✅ 採用** — 把時間留給最有張力的 ABS 段落。

---

## R11 — ABS 啟動需要一個「觸發瞬間」

**問題**：原版 ABS 突然出現（"Suddenly"），缺少觸發的因果感。

**After**：After the pitcher protests, a small red light blinks on a device mounted behind home plate. Then the blue neon strike zone projects upward...

**判定：✅ 採用** — 紅燈閃爍 → 系統啟動 → 投影出現，有因果鏈。觀眾能理解「是機器在判」。

---

## R12 — 結尾的 "STRIKE" 文字 AI 很難渲染

**問題**：AI 影片生成模型對文字渲染極不穩定，"STRIKE" 很可能變成亂碼。

**Before**：A digital scoreboard flashes STRIKE

**After**：A green checkmark symbol lights up on the device behind home plate, confirming the call was a strike

**判定：✅ 採用** — 綠色勾勾比文字容易 100 倍。AI 能畫符號但寫不好字。

---

## R13 — 整個 prompt 太長（180+ 字），需要精簡

**問題**：prompt 超過 150 字，後段可能被截斷。

**策略**：
- 刪除打者（R8 已決定）
- 壓縮重複的角色描述（投手+捕手+裁判都完整描述一次太冗長）
- 只在第一次出現時描述角色細節，後續用 "the pitcher", "the catcher", "the umpire" 指代

**判定：✅ 採用**

---

## R14 — 投球動作的「蓄力感」不足

**問題**：R1 雖然分解了動作但每步都一樣速度，沒有蓄力→爆發的反差。

**After**：it slowly lifts its front knee high, pauses at the top for a brief moment, then explosively drives forward and whips the ball

**判定：✅ 採用** — "slowly...pauses...then explosively" 是明確的慢→停→快節奏指令。

---

## R15 — 捕手的 framing 動作是 ABS 劇本的伏筆

**問題**：目前捕手只是「接住」，但 framing（偷好球）正是 ABS 想解決的問題。

**After**：the catcher catches the ball and subtly pulls its glove inward toward the center of the zone — a classic framing move

**判定：✅ 採用** — 懂棒球的人看到 framing 會會心一笑，這個細節讓影片有知識深度。也為 ABS 的存在提供了敘事理由。

---

## R16 — 裁判被 ABS 改判後的反應要更有喜感

**問題**：原版「裁判愣住」太單調。

**Before**：The umpire freezes.

**After**：The umpire's whole body stiffens, then slowly turns to look at the ABS device, its round body deflating with embarrassment

**判定：✅ 採用** — 「僵住→轉頭看機器→洩氣」是三拍喜劇節奏。裁判的尷尬是整支影片的笑點。

---

## R17 — 測試把風格改為 2D cel-shaded anime

**判定：❌ 拒絕** — 3D Pixar-style 在球場空間感和角色立體感上更好。2D 動畫的棒球場透視容易出錯。

---

## R18 — 球場環境描述要更簡潔

**問題**：不需要描述整個球場，只需要描述鏡頭能看到的範圍。

**After**：把 "On a baseball diamond" 改為 "On a sunlit pitcher's mound facing home plate" — 只描述投手丘到本壘板這個軸線。

**判定：✅ 採用** — 限定空間範圍讓 AI 聚焦渲染投手丘→本壘板的景深，不用浪費算力畫外野。

---

## R19 — 光線要隨劇情轉變

**問題**：全程 "bright daylight" 沒有光影變化。

**After**：
- 投球段：bright warm sunlight
- ABS 啟動段：the ambient light dims slightly as the blue neon glow of the strike zone illuminates the scene
- 結尾：light returns to warm daylight

**判定：✅ 採用** — 「日光→變暗+藍光→恢復日光」的光線變化強化了 ABS 啟動的科技感和戲劇性。

---

## R20 — 加入起始幀描述

**After**：The shot opens on a cream dumpling mascot pitcher standing still on the mound, baseball in glove, ready position.

**判定：✅ 採用** — 明確第一幀是投手準備姿勢，AI 知道從哪裡開始。

---

## R21 — 投手結尾彈跳要利用圓形身體

**After**：The pitcher bounces up and down like a rubber ball, its round body squashing flat on landing and stretching tall on each bounce, sprout wiggling wildly

**判定：✅ 採用** — squash & stretch 是動畫基本原理，在圓形角色上效果最好。

---

## R22 — 測試加入慢動作指令在 ABS 回放段

**After**：在球跡回放處加 "in slow motion, the red line traces the ball's path"

**判定：✅ 採用** — ABS 回放本就應該是慢動作，和前面投球的快節奏形成反差。

---

## R23 — 角色大小比例需要明確

**問題**：投手、捕手、裁判如果一樣大，場景會混亂。

**After**：
- 投手：small（標準大小）
- 捕手：small, crouching（蹲著所以看起來更矮）
- 裁判：slightly larger and rounder（比其他角色大一號，符合裁判的權威感）

**判定：✅ 採用** — 大小差異讓角色即使長相相似也能一眼區分。

---

## R24 — 全息投影的顏色要和角色形成對比

**問題**：藍色投影在日光下可能不夠醒目。

**After**：改為 "bright cyan neon lines"（亮青色），在暖色日光+米色角色中更跳。

**判定：✅ 採用**

---

## R25 — 捕手要已經蹲好，不要描述蹲下的過程

**問題**：描述捕手蹲下浪費時間。影片開始時捕手就應該在位置上。

**After**：a crouching catcher mascot in chest gear waits behind the plate

**判定：✅ 採用**

---

## R26 — 球的運動要有弧度暗示，不是直線

**問題**：真實投球有 movement，直線飛球看起來假。

**After**：the ball curves slightly as it rockets toward the outside corner

**判定：✅ 採用** — "curves slightly" 暗示了變化球的運動軌跡，增加真實感。

---

## R27 — 測試拆成兩支 5 秒影片

**判定：❌ 拒絕** — 用戶要求一支直接生成，且 ABS 的劇情需要「誤判→改判」的連貫因果，拆開會失去張力。

---

## R28 — 裁判的面罩需要簡化

**問題**：原版 "wearing a black mask" 可能讓 AI 畫成口罩或面具。

**After**：wearing a dark umpire chest protector（只穿護胸，不戴面罩，讓臉部表情可見）

**判定：✅ 採用** — 面部表情是裁判戲份的重點（誤判→尷尬），不能被面罩遮住。

---

## R29 — prompt 整體節奏用標點符號控制

**策略**：
- 快節奏段用短句+逗號：`lifts knee, pauses, drives forward, hurls the ball`
- 慢節奏段用長句+em dash：`the ambient light dims — bright cyan neon lines slowly project upward from the ground`

**判定：✅ 採用** — AI 影片模型確實會受標點節奏影響，短促逗號 = 快動作，長句 = 慢動作。

---

## R30 — 最終通檢：動作合理性

逐幀檢查：
| 時間 | 動作 | 棒球力學合理性 |
|------|------|---------------|
| 0s | 投手準備姿勢，球在手套中 | ✅ set position |
| 1s | 抬前腳膝蓋，停頓蓄力 | ✅ leg kick + balance point |
| 2s | 重心前移，手臂由上往下揮，釋放球 | ✅ stride + arm whip + release |
| 3s | 球帶弧度飛向外角，捕手接住並 frame | ✅ pitch movement + framing |
| 4s | 裁判挺胸前傾，全身搖晃報壞球 | ✅ real ball call mechanics |
| 5s | 投手洩氣雙手舉起抗議 | ✅ pitcher reaction |
| 6s | ABS 設備紅燈閃，場地光線微暗 | ✅ system trigger |
| 7-8s | 青色全息好球帶投影，紅色軌跡慢動作回放壓線 | ✅ ABS visualization |
| 9s | 綠勾亮起，裁判僵住轉頭看機器洩氣 | ✅ override + comic relief |
| 10s | 投手彈跳慶祝，squash & stretch | ✅ celebration |

**判定：✅ 全部通過** — 所有動作符合棒球力學，且在小紅薯圓形身體上可執行。

---

## 30 輪總結

| 類別 | 採用 | 拒絕 |
|------|------|------|
| 投球動作力學 | R1, R14, R26 | — |
| 接球/捕手 | R3, R15, R25 | — |
| 裁判表演 | R4, R16, R28 | — |
| ABS 視覺效果 | R6, R11, R12, R22, R24 | — |
| 角色設計 | R8, R23 | — |
| 鏡頭/光影 | R7, R19, R20 | R17 |
| 節奏/結構 | R10, R13, R29 | R27 |
| 動作物理 | R5, R21 | — |
| 音效 | R9 | — |
| 通檢 | R30 | — |

**採用率：28/30 (93%)**

---

# ⭐ 最終 Prompt

```
Consistent character design, single continuous shot. The shot opens on a sunlit pitcher's mound facing home plate. A small round cream-colored dumpling mascot with a green sprout on top, dot eyes, pink cheeks, soft plush texture, wearing a baseball cap, stands in set position with the ball in its glove. It slowly lifts its front knee high, pauses at the top — then explosively drives forward, whips its arm overhead, and releases the ball. The ball curves slightly as it rockets toward the outside corner with a faint white speed trail. Behind the plate, a crouching catcher mascot in chest gear snaps its round glove shut with a satisfying pop, subtly pulling the glove inward — a classic framing move. A slightly larger, rounder umpire mascot in a dark chest protector puffs up, leans forward, and swings its arm out wide to signal ball, its whole body swaying. The pitcher deflates like a balloon, sprout drooping, throwing both arms up. Then a small red light blinks on a device behind home plate — the ambient light dims — bright cyan neon lines slowly project upward from the ground, forming a 3D strike zone box. In slow motion, a red dotted line traces the ball's curved path, just touching the zone edge. A green checkmark lights up on the device. The umpire stiffens, slowly turns to stare at the machine, its body deflating with embarrassment. The pitcher bounces up and down like a rubber ball, squashing flat and stretching tall, sprout wiggling wildly. Warm sunlight to cool cyan glow, then back to warm light. A futuristic electronic hum as the zone appears. 3D Pixar-style kawaii animation.
```

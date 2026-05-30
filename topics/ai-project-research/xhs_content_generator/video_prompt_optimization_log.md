# 小紅薯影片 Prompt — 20 輪優化記錄

> 方法：每輪只改一個變數，評估是否改善，保留好的版本
> 評估維度：角色辨識度、動作清晰度、鏡頭可執行性、氛圍感、Gemini 生成可行性

---

## R1 — 角色描述精簡化（全域）

**變異**：原角色描述 50+ 字，AI 影片模型傾向忽略過長描述的後半段。精簡到核心視覺特徵。

**Before（原版）**：
> A cute, round, chubby red-brown sweet potato character with tiny stubby arms and legs, big sparkling black eyes, rosy pink cheeks, and a small green leaf sprouting from the top of its head. The character has a smooth, soft matte texture and a friendly, expressive face.

**After**：
> A cute chubby red-brown sweet potato character with stubby limbs, big round black eyes, pink cheeks, and a green leaf on top of its head.

**判定：✅ 採用** — 精簡 60%，保留所有關鍵視覺特徵。AI 影片模型對簡短精準的描述反應更好，長描述中後段容易被忽略。

---

## R2 — 動作分解為時間序列（Prompt 1 子彈時間）

**變異**：把單一動作改成「先…然後…最後」的時間序列，讓模型理解動作的起承轉合。

**Before**：
> The character leans dramatically backward in slow motion, dodging glowing bullets that streak past in frozen trails. The camera orbits 360 degrees around the character during the dodge.

**After**：
> First, glowing bullets fly toward the character. Then, the character leans dramatically backward in slow motion, arching its round body as bullets streak past in frozen trails. The camera slowly orbits around the character, capturing the dodge from all angles.

**判定：✅ 採用** — 時間序列讓 10 秒影片有明確的「開始→高潮→收尾」節奏，而非靜態定格。

---

## R3 — 移除 aspect ratio 指令（全域）

**變異**：測試移除 "16:9 aspect ratio" — Gemini 的 aspect ratio 通常在 UI 設定而非 prompt 中控制。

**判定：✅ 採用** — Aspect ratio 在 Gemini 介面選擇，寫在 prompt 裡浪費 token 且可能被忽略。全部移除，省出空間給更重要的描述。

---

## R4 — 加入 "single continuous shot" 指令（全域）

**變異**：加入鏡頭連續性指令，避免 AI 生成跳切片段。

**After**：每個 prompt 結尾加 `Single continuous shot, no cuts.`

**判定：✅ 採用** — 10 秒短片跳切會破壞觀感，明確要求連續鏡頭讓 AI 保持畫面連貫。

---

## R5 — 風格從 "3D Pixar-style" 改為 "3D cartoon animation"（全域）

**變異**：測試更通用的風格描述，避免模型因版權過濾而弱化 Pixar 風格。

**判定：❌ 拒絕** — "Pixar-style" 在 AI 生成中是一個強錨定詞，能穩定觸發高品質 3D 卡通渲染。改成 "3D cartoon" 風格方向太模糊，可能產出品質不一的結果。保留 Pixar-style。

---

## R6 — 加強表情描述（Prompt 4 MI 懸吊）

**變異**：用更具體的表情動詞取代泛泛描述。

**Before**：
> Sweat drops on its forehead, extremely focused expression.

**After**：
> A single sweat bead rolls down its forehead, eyes wide and unblinking, tiny mouth pressed tight with concentration.

**判定：✅ 採用** — 具體的微表情（sweat bead rolls, eyes unblinking, mouth pressed tight）比抽象的 "focused expression" 更能指導 AI 生成有表現力的畫面。應用到其他需要表情的 prompt。

---

## R7 — 環境描述前置（Prompt 3 獅子王）

**變異**：把環境/場景描述移到動作之前，讓 AI 先建立場景再放入角色。

**Before**：
> [角色] standing at the edge of a dramatic cliff. It lifts a tiny baby... Below the cliff, a vast savanna stretches...

**After**：
> On the edge of a towering cliff overlooking a vast golden savanna at sunrise, [角色] stands tall. It slowly lifts a tiny baby sweet potato character high above its head...

**判定：✅ 採用** — 「場景先行」讓 AI 模型先構建空間，角色動作在空間中更合理。影片生成模型通常按 prompt 順序建構畫面。

---

## R8 — 減少同時動作數量（Prompt 7 光劍對決）

**變異**：原版同時要求「兩角色+各自服裝+各自武器+碰撞+火花+環繞鏡頭」，對 AI 負擔太重。簡化為一個核心動作。

**Before**：
> They clash their lightsabers together with bright sparks flying. A dark metallic spaceship corridor with steam vents in the background. The camera circles around them during the clash.

**After**：
> They swing their lightsabers and clash in the center with a bright flash of sparks. Dark metallic corridor, moody backlight. Camera holds a medium shot, slowly pushing in.

**判定：✅ 採用** — 環繞鏡頭+雙人打鬥+火花對 10 秒影片太貪心。固定中景推進更穩定，讓 AI 專注渲染打鬥動作本身。

---

## R9 — 加入物理暗示詞（Prompt 5 阿甘跑步）

**變異**：加入物理效果詞讓動作更有重量感。

**Before**：
> The character runs determinedly along an endless straight desert highway stretching to the horizon. Dust kicks up from its tiny feet.

**After**：
> The character bounces forward in a determined running motion along an endless desert highway, its round body wobbling with each step, tiny dust clouds puffing up beneath its feet.

**判定：✅ 採用** — "bounces", "wobbling", "puffing" 這類物理暗示詞讓圓滾滾的小紅薯跑步更有量感和喜感，比 "runs determinedly" 具體得多。

---

## R10 — 測試加入 "masterpiece, best quality" 品質提升詞（全域）

**變異**：在結尾加 "masterpiece, best quality, highly detailed"

**判定：❌ 拒絕** — 這些是圖片生成（SD/MJ）的提示詞習慣，在影片生成模型中效果不明確，且浪費 prompt 空間。Gemini Veo 對這類 booster 詞反應不如圖片模型敏感。

---

## R11 — 簡化服裝描述（全域）

**變異**：把詳細服裝改為一個核心視覺錨點。

**Prompt 1 Before**：
> wearing a long black leather trench coat and dark sunglasses

**After**：
> in a black trench coat and sunglasses

**Prompt 4 Before**：
> wearing a tight black spy suit

**After**：
> in a sleek black bodysuit

**判定：✅ 採用** — 服裝只需要一個可辨識的視覺錨點，過多形容詞（long, leather, tight）在影片生成中幾乎沒差別，反而分散模型注意力。

---

## R12 — 鏡頭運動改為更簡單的指令（全域）

**變異**：複雜鏡頭運動（orbit 360, lateral dolly, slowly tilts upward）在 AI 影片中經常失敗。改用更基礎的鏡頭詞。

**策略**：
- `The camera orbits 360 degrees` → `Slow rotating camera angle`
- `smooth lateral dolly shot` → `Side tracking shot`
- `camera slowly tilts upward` → `Low angle, camera looking up`
- `camera slowly dollies in from a side angle` → `Slow zoom in from the side`

**判定：✅ 採用** — AI 影片模型對簡單鏡頭指令的遵從率遠高於電影術語。"Slow zoom in" 比 "dollies in" 更容易被模型正確理解。

---

## R13 — Prompt 2 Titanic 加入頭髮/圍巾飄動細節

**變異**：加入風吹動的視覺細節增加動態感。

**Before**：
> Wind blows softly.

**After**：
> A warm breeze lifts the green leaves on their heads and gently ripples across the ocean surface.

**判定：✅ 採用** — 具體的「風吹動什麼東西」比抽象的「wind blows」有效得多。葉子飄動是小紅薯角色專屬的視覺細節，增加辨識度。

---

## R14 — 測試移除所有 "atmosphere" 抽象詞（全域）

**變異**：移除 "romantic and dreamy atmosphere", "epic and majestic atmosphere" 等，只保留具體的光影描述。

**判定：❌ 拒絕** — 氛圍詞在影片生成中作為「情緒錨點」有實際作用，能影響色調和節奏。但應精簡為 1-2 個詞，不要堆疊。改為每個 prompt 只保留一個氛圍詞。

---

## R15 — Prompt 6 Spider-Man 改為 9:16 專用構圖

**變異**：既然是豎版，重新設計構圖適合垂直畫面。

**Before**：
> The character hangs upside down from a web string in a narrow city alley. Another sweet potato character in a pink scarf stands below...

**After**：
> In a narrow vertical alley between tall buildings, a sweet potato character in a red-and-blue spider suit hangs upside down from a web at the top of the frame. Below, another sweet potato character in a pink scarf looks up from the bottom of the frame. They face each other vertically. Gentle rain falls between them.

**判定：✅ 採用** — 豎版構圖需要明確的「上下關係」描述（top of frame / bottom of frame），讓 AI 在垂直空間中合理安排角色。

---

## R16 — 加入動作的「結束姿態」（Prompt 1, 3, 4）

**變異**：給動作一個明確的結束 pose，避免影片結尾動作中斷感。

**Prompt 1 加入**：
> ...and finally straightens back up, adjusting its sunglasses coolly.

**Prompt 3 加入**：
> ...holds the baby still at the highest point as golden light beams down.

**Prompt 4 加入**：
> ...reaches out one tiny arm and barely touches the gem with a fingertip.

**判定：✅ 採用** — 10 秒影片需要「起→承→收」，沒有結束姿態會讓影片看起來像被截斷。結束 pose 讓影片有完整感。

---

## R17 — Prompt 8 Inception 簡化物理效果

**變異**：城市翻折對 AI 來說太複雜，簡化為更容易生成的視覺效果。

**Before**：
> ...a city street that gradually bends and folds upward impossibly, with buildings, cars, and trees curving overhead to form a tunnel of cityscape.

**After**：
> ...a city street where the road ahead slowly curves upward into the sky, with buildings bending along both sides, creating a surreal curved cityscape above.

**判定：✅ 採用** — "tunnel of cityscape" 對 AI 太抽象。改為 "road curves upward, buildings bend along sides" 是更具體的物理描述，AI 更可能正確渲染。

---

## R18 — 統一所有 prompt 的結構順序（全域）

**變異**：統一為固定順序，讓 AI 模型形成穩定的解析模式。

**統一結構**：
```
[環境/場景]. [角色描述+服裝]. [動作序列：First...Then...Finally]. [鏡頭]. [光影]. [風格]. Single continuous shot.
```

**判定：✅ 採用** — 統一結構讓批量生成時角色一致性更高。場景先行→角色入場→動作展開→鏡頭指導→風格收尾，符合影片模型的生成邏輯。

---

## R19 — 加入 "consistent character design" 全域前綴

**變異**：在每個 prompt 最前面加 "Consistent character design throughout the video."

**判定：✅ 採用** — 這是對抗角色漂移最直接的方法。特別是 10 秒影片中角色可能在中段變形，這個前綴能提醒模型維持一致性。

---

## R20 — 光影描述改為「光源+方向」而非「氛圍」（全域）

**變異**：把抽象光影改為具體光源。

| Prompt | Before | After |
|--------|--------|-------|
| 1 Matrix | Cinematic dramatic lighting with green-tinted color grading | Green-tinted neon glow from above, dark shadows below |
| 2 Titanic | Golden hour sunset light with warm orange and pink sky | Low sun from the left casting long warm orange light |
| 3 Lion King | warm golden lighting | A single beam of sunlight from above through clouds |
| 4 MI | cool blue and red lighting | Cool blue overhead lights, red glow from the gem below |
| 5 Forrest | bright natural daylight | Bright midday sun, sharp shadows on the road |
| 7 Star Wars | lightsaber glow illuminating their faces | Blue and red lightsaber glow as the only light source in darkness |
| 8 Inception | golden hour lighting | Warm amber sunlight filtering through the bending buildings |

**判定：✅ 採用** — 「光源+方向」比 "dramatic lighting" 具體 10 倍。AI 影片模型能根據具體光源位置正確渲染陰影和高光。

---

## 優化總結

| 輪次 | 變異策略 | 判定 | 影響範圍 |
|------|---------|------|---------|
| R1 | 角色描述精簡化 | ✅ | 全域 |
| R2 | 動作分解為時間序列 | ✅ | Prompt 1 → 推廣全域 |
| R3 | 移除 aspect ratio | ✅ | 全域 |
| R4 | 加入 single continuous shot | ✅ | 全域 |
| R5 | Pixar-style → cartoon | ❌ | — |
| R6 | 加強微表情描述 | ✅ | Prompt 4 → 推廣 |
| R7 | 環境描述前置 | ✅ | Prompt 3 → 推廣全域 |
| R8 | 減少同時動作數量 | ✅ | Prompt 7 |
| R9 | 加入物理暗示詞 | ✅ | Prompt 5 → 推廣 |
| R10 | masterpiece 品質詞 | ❌ | — |
| R11 | 簡化服裝描述 | ✅ | 全域 |
| R12 | 簡化鏡頭運動指令 | ✅ | 全域 |
| R13 | 加入風吹動態細節 | ✅ | Prompt 2 |
| R14 | 移除所有 atmosphere 詞 | ❌ | 改為每 prompt 只保留 1 個 |
| R15 | 豎版專用構圖 | ✅ | Prompt 6 |
| R16 | 加入結束姿態 | ✅ | Prompt 1, 3, 4 |
| R17 | 簡化複雜物理效果 | ✅ | Prompt 8 |
| R18 | 統一 prompt 結構順序 | ✅ | 全域 |
| R19 | 加入 consistent character 前綴 | ✅ | 全域 |
| R20 | 光影改為光源+方向 | ✅ | 全域 |

**採用率：17/20 (85%)**
**3 個拒絕：** R5 (Pixar錨定太重要), R10 (品質詞無效), R14 (氛圍詞有用但需精簡)

# 小紅薯 × 經典電影場面 — Gemini 影片 Prompt v2（優化版）

> 經 20 輪系統性優化，採用 17 項改進
> 優化記錄：`video_prompt_optimization_log.md`

---

## 統一結構

```
[一致性前綴] → [環境/場景] → [角色+服裝] → [動作序列 First/Then/Finally] → [鏡頭] → [光源+方向] → [風格] → [連續鏡頭指令]
```

### 角色固定描述（精簡版）

> A cute chubby red-brown sweet potato character with stubby limbs, big round black eyes, pink cheeks, and a green leaf on top of its head.

---

## Prompt 1 — The Matrix 子彈時間

```
Consistent character design throughout the video. On a dark rainy rooftop at night, a cute chubby red-brown sweet potato character with stubby limbs, big round black eyes, pink cheeks, and a green leaf on top of its head, in a black trench coat and sunglasses. First, glowing green bullets fly toward the character. Then, the character leans dramatically backward in slow motion, arching its round body as bullets streak past in frozen trails, rain droplets suspended in mid-air around it. Finally, the character straightens back up and coolly adjusts its sunglasses. Slow rotating camera angle. Green-tinted neon glow from above, dark shadows below. 3D Pixar-style animation, cinematic atmosphere. Single continuous shot, no cuts.
```

---

## Prompt 2 — Titanic 船頭經典

```
Consistent character design throughout the video. At the bow of a grand ocean ship at sunset, two cute chubby red-brown sweet potato characters with stubby limbs, big round black eyes, pink cheeks, and green leaves on their heads. First, one character stands at the very front of the ship. Then, the other character steps behind it and gently holds the front character's tiny arms spread wide open. A warm breeze lifts the green leaves on their heads and gently ripples across the ocean surface. The camera slowly pulls back to reveal the vast glittering ocean. Low sun from the left casting long warm orange light across the scene. 3D Pixar-style animation, romantic atmosphere. Single continuous shot, no cuts.
```

---

## Prompt 3 — The Lion King 舉起辛巴

```
Consistent character design throughout the video. On the edge of a towering cliff overlooking a vast golden savanna at sunrise, a large wise-looking red-brown sweet potato character with stubby limbs, big calm black eyes, pink cheeks, and a green leaf on its head stands tall. First, it cradles a tiny baby sweet potato character in its arms. Then, it slowly lifts the baby high above its head with both arms. Finally, it holds the baby still at the highest point as light beams down on it. Tiny animals look up from the savanna below. Low angle, camera looking up. A single beam of sunlight from above through parting clouds. 3D Pixar-style animation, epic atmosphere. Single continuous shot, no cuts.
```

---

## Prompt 4 — Mission Impossible 懸吊

```
Consistent character design throughout the video. Inside a dark high-tech vault room with blue laser grid beams crisscrossing the air, a cute chubby red-brown sweet potato character with stubby limbs, big round black eyes, pink cheeks, and a green leaf on its head, in a sleek black bodysuit. First, the character slowly descends upside down on a thin wire from the ceiling. Then, a single sweat bead rolls down its forehead, eyes wide and unblinking, tiny mouth pressed tight with concentration. Finally, it reaches out one tiny arm and barely touches a glowing red gem on a pedestal with a fingertip. Slow zoom in from the side. Cool blue overhead lights, red glow from the gem below. 3D Pixar-style animation, suspenseful atmosphere. Single continuous shot, no cuts.
```

---

## Prompt 5 — Forrest Gump 奔跑

```
Consistent character design throughout the video. On an endless straight desert highway stretching to the horizon under a wide open blue sky, a cute chubby red-brown sweet potato character with stubby limbs, big round black eyes, pink cheeks, and a green leaf on its head, in a red cap and plaid shirt. First, the character bounces forward in a determined running motion, its round body wobbling with each step. Then, tiny dust clouds puff up beneath its feet as it keeps running. Behind it, a small group of other sweet potato characters follows at a distance. Side tracking shot. Bright midday sun, sharp shadows on the road. 3D Pixar-style animation, inspirational atmosphere. Single continuous shot, no cuts.
```

---

## Prompt 6 — Spider-Man 倒吊之吻（9:16 豎版）

```
Consistent character design throughout the video. In a narrow vertical alley between tall brick buildings on a rainy evening, a cute chubby red-brown sweet potato character with stubby limbs, big round black eyes, pink cheeks, and a green leaf on its head, in a red-and-blue spider suit. The character hangs upside down from a web string at the top of the frame. Below, another sweet potato character in a pink scarf looks up from the bottom of the frame with shy, blushing cheeks. They face each other vertically. First, gentle rain falls between them. Then, they slowly lean toward each other. Slow zoom in on their faces. Warm street lamp glow with bokeh lights in the background. 3D Pixar-style animation, sweet romantic atmosphere. Single continuous shot, no cuts.
```

---

## Prompt 7 — Star Wars 光劍對決

```
Consistent character design throughout the video. In a dark metallic spaceship corridor filled with shadow, two cute chubby red-brown sweet potato characters with stubby limbs, big round black eyes, pink cheeks, and green leaves on their heads. One in a brown Jedi robe holds a glowing blue lightsaber, the other in a black cloak holds a glowing red lightsaber. First, they face each other from opposite ends of the corridor. Then, they charge forward and swing their lightsabers, clashing in the center with a bright flash of sparks. Medium shot, slowly pushing in. Blue and red lightsaber glow as the only light source in darkness. 3D Pixar-style animation, dramatic atmosphere. Single continuous shot, no cuts.
```

---

## Prompt 8 — Inception 城市翻折

```
Consistent character design throughout the video. On a sunlit city street, a cute chubby red-brown sweet potato character with stubby limbs, big round black eyes, pink cheeks, and a green leaf on its head, in a neat suit and tie. First, the character walks calmly forward along the street. Then, the road ahead slowly curves upward into the sky, with buildings bending along both sides, creating a surreal curved cityscape above. Finally, the character stops and looks up in wonder as the world bends around it. Camera follows behind the character in a tracking shot. Warm amber sunlight filtering through the bending buildings. 3D Pixar-style animation, surreal dreamlike atmosphere. Single continuous shot, no cuts.
```

---

## v1 → v2 主要改進

| 改進 | 說明 |
|------|------|
| 角色描述精簡 60% | 從 50+ 字降到核心特徵，減少模型忽略後段描述的風險 |
| 統一「場景→角色→動作→鏡頭→光→風格」結構 | 讓模型形成穩定解析模式 |
| 動作改為 First/Then/Finally 時間序列 | 10 秒影片有明確的起承轉合 |
| 加入結束姿態 | 影片不會看起來被截斷 |
| 鏡頭指令簡化 | "slow zoom in" 取代 "dollies in"，AI 遵從率更高 |
| 光影改為「光源+方向」 | 比 "dramatic lighting" 具體 10 倍 |
| 加入 "Single continuous shot" | 避免 AI 生成跳切片段 |
| 加入 "Consistent character design" 前綴 | 對抗角色漂移 |
| 移除 aspect ratio（UI 設定） | 省出 prompt 空間 |
| 環境描述前置 | 讓 AI 先建立空間再放入角色 |
| 加入物理暗示詞 | wobbling, bouncing, puffing 增加動態重量感 |
| 簡化服裝為視覺錨點 | 減少無效形容詞 |

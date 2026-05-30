# 小紅薯 × 經典電影場面 — Gemini 影片 Prompt

> 目標：用 Gemini (Veo) 生成 ~10 秒短片，小紅薯模仿經典電影場面
> 用途：小紅書影片素材

---

## Prompt 模板結構

```
[角色描述] + [動作/場景] + [動畫風格] + [鏡頭運動] + [光影/氛圍] + [品質關鍵詞]
```

### 角色固定描述（每個 prompt 都要帶）

> A cute, round, chubby red-brown sweet potato character with tiny stubby arms and legs, big sparkling black eyes, rosy pink cheeks, and a small green leaf sprouting from the top of its head. The character has a smooth, soft matte texture and a friendly, expressive face.

---

## Prompt 1 — The Matrix 子彈時間

**場面**：小紅薯穿黑色風衣，後仰躲子彈，鏡頭 360 度環繞

```
A cute, round, chubby red-brown sweet potato character with tiny stubby arms and legs, big sparkling black eyes, rosy pink cheeks, and a small green leaf sprouting from the top of its head, wearing a long black leather trench coat and dark sunglasses. The character leans dramatically backward in slow motion, dodging glowing bullets that streak past in frozen trails. The camera orbits 360 degrees around the character during the dodge. Dark rooftop environment with rain droplets suspended in mid-air. Cinematic dramatic lighting with green-tinted color grading. 3D Pixar-style animation, smooth motion, 16:9 aspect ratio.
```

---

## Prompt 2 — Titanic 船頭經典

**場面**：兩顆小紅薯在船頭張開雙手

```
Two cute, round, chubby red-brown sweet potato characters with tiny stubby arms and legs, big sparkling black eyes, rosy pink cheeks, and small green leaves sprouting from the tops of their heads. One character stands behind the other at the bow of a grand ship, gently holding the front character's tiny arms spread wide open. Wind blows softly. Golden hour sunset light with warm orange and pink sky, ocean waves glittering below. The camera slowly pulls back to reveal the vast ocean. 3D Pixar-style animation, romantic and dreamy atmosphere, smooth motion, 16:9 aspect ratio.
```

---

## Prompt 3 — The Lion King 舉起辛巴

**場面**：大紅薯把小紅薯舉到懸崖邊

```
A large, wise-looking red-brown sweet potato character with tiny stubby arms, big calm black eyes, rosy cheeks, and a small green leaf on its head, standing at the edge of a dramatic cliff. It lifts a tiny baby sweet potato character high above its head with both arms. A beam of golden sunlight breaks through the clouds and illuminates the baby character. Below the cliff, a vast savanna stretches to the horizon with herds of tiny animals looking up. The camera slowly tilts upward as the baby is raised. 3D Pixar-style animation, epic and majestic atmosphere, warm golden lighting, 16:9 aspect ratio.
```

---

## Prompt 4 — Mission Impossible 懸吊

**場面**：小紅薯從天花板倒吊，小心翼翼靠近目標

```
A cute, round, chubby red-brown sweet potato character with tiny stubby arms and legs, big sparkling black eyes, rosy pink cheeks, and a small green leaf sprouting from its head, wearing a tight black spy suit. The character hangs upside down from a thin wire descending slowly from the ceiling toward a glowing red gem on a pedestal. Sweat drops on its forehead, extremely focused expression. A dark high-tech vault room with laser grid beams visible in the background. The camera slowly dollies in from a side angle. 3D Pixar-style animation, suspenseful atmosphere, cool blue and red lighting, 16:9 aspect ratio.
```

---

## Prompt 5 — Forrest Gump 奔跑

**場面**：小紅薯在空曠公路上不停奔跑

```
A cute, round, chubby red-brown sweet potato character with tiny stubby arms and legs, big sparkling black eyes, rosy pink cheeks, and a small green leaf sprouting from its head, wearing a red cap and a simple plaid shirt. The character runs determinedly along an endless straight desert highway stretching to the horizon. Dust kicks up from its tiny feet. Behind it, a small group of other sweet potato characters follows at a distance. Wide open American desert landscape with blue sky and white clouds. The camera tracks alongside in a smooth lateral dolly shot. 3D Pixar-style animation, inspirational and warm atmosphere, bright natural daylight, 16:9 aspect ratio.
```

---

## Prompt 6 — Spider-Man 倒吊之吻

**場面**：小紅薯倒掛在蜘蛛絲上，面對另一顆小紅薯

```
A cute, round, chubby red-brown sweet potato character with tiny stubby arms and legs, big sparkling black eyes, rosy pink cheeks, and a small green leaf on its head, wearing a red and blue spider suit. The character hangs upside down from a web string in a narrow city alley. Another sweet potato character in a pink scarf stands below, looking up with shy, blushing cheeks. Gentle rain falls around them. Warm street lamp glow with bokeh light spots in the background. The camera slowly pushes in on their faces. 3D Pixar-style animation, sweet romantic atmosphere, soft warm lighting with rain reflections, 9:16 aspect ratio.
```

---

## Prompt 7 — Star Wars 光劍對決

**場面**：兩顆小紅薯拿光劍對打

```
Two cute, round, chubby red-brown sweet potato characters with tiny stubby arms and legs, big sparkling black eyes, rosy pink cheeks, and small green leaves on their heads. One wears a brown Jedi robe and holds a glowing blue lightsaber, the other wears a black cloak and holds a glowing red lightsaber. They clash their lightsabers together with bright sparks flying. A dark metallic spaceship corridor with steam vents in the background. The camera circles around them during the clash. 3D Pixar-style animation, epic and dramatic atmosphere, lightsaber glow illuminating their faces, 16:9 aspect ratio.
```

---

## Prompt 8 — Inception 城市翻折

**場面**：小紅薯在折疊翻轉的城市街道上行走

```
A cute, round, chubby red-brown sweet potato character with tiny stubby arms and legs, big sparkling black eyes, rosy pink cheeks, and a small green leaf sprouting from its head, wearing a neat suit and tie. The character walks calmly along a city street that gradually bends and folds upward impossibly, with buildings, cars, and trees curving overhead to form a tunnel of cityscape. The character looks up in wonder as the world folds around it. Surreal dreamlike atmosphere with warm amber lighting. The camera follows behind the character in a smooth tracking shot. 3D Pixar-style animation, mind-bending surreal atmosphere, golden hour lighting, 16:9 aspect ratio.
```

---

## 使用建議

### 生成策略
- 每個 prompt 跑 3-5 次，挑最好的版本
- 如果角色外觀偏移，嘗試在 prompt 開頭加 "Consistent character design throughout,"
- 如果動作不夠動態，加 "highly dynamic motion, exaggerated animation"

### 微調方向
| 問題 | 調整 |
|------|------|
| 角色長得不像 | 加強角色描述細節，或用 image-to-video 模式先提供角色圖 |
| 動作太靜態 | 加 "energetic movement, exaggerated squash and stretch animation" |
| 畫面太暗 | 明確指定 "bright, well-lit" |
| 風格不統一 | 統一用 "3D Pixar-style" 或換成 "Chibi anime style" |
| 10 秒不夠 | 簡化動作，或分兩段生成後剪接 |

### 備選風格關鍵詞
- `3D Pixar-style animation` — 最穩定，適合可愛角色
- `Chibi anime cel-shaded animation` — 日系可愛風
- `Clay animation stop-motion style` — 黏土動畫質感
- `2.5D isometric animation` — 扁平立體混合風

### 小紅書發布建議
- 9:16 豎版更適合小紅書 feed（Prompt 6 已設為 9:16，其他可改）
- 可在影片上疊加文字標題增加辨識度
- 系列化發布：「小紅薯的電影夢 Vol.1」

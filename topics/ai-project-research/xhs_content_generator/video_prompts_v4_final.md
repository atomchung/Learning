# 小紅薯演體育故事 — Gemini 影片 Prompt v4 Final

> 修正：角色形象對齊官方小紅薯（米色團子，非紅色）
> 新增：同家族但有差異化的角色設計
> 格式：每個故事 = 1 個 prompt = 1 支 10 秒完整影片

---

## 角色設計系統

### 基底（家族共通特徵）
> A cute round cream-colored dumpling-shaped mascot with a small green sprout on top of its head, simple black dot eyes, a tiny curved smile, and soft pink blush on both cheeks. Smooth round body with no neck, tiny stubby arms. Soft plush toy texture. Xiaohongshu mascot style.

### 角色差異化（透過配件+眉眼微調區分身份）

| 角色類型 | 差異化特徵 |
|---------|-----------|
| 主角/夢想家 | 基底原樣，眼睛稍大且圓，表情天真堅定 |
| 老闆/權威 | 加一副小黑框眼鏡，眉線略粗，表情沉穩 |
| 反對者/質疑者 | 眉毛下壓呈八字，嘴角微微向下，表情嚴肅 |
| 對手A（熱血型）| 眼睛上挑，加一條小頭帶，表情自信張揚 |
| 對手B（沉穩型）| 眼睛半閉微瞇，表情冷靜內斂 |
| 群眾/配角 | 比主角小一號，表情隨場景統一 |

---

# Story A — 拉科布買下勇士：被嘲笑的瘋子

> 一支 10 秒影片，完整故事弧線：低谷 → 決心 → 爆發

```
Consistent character design, single continuous shot. In a dark basketball arena under a single white spotlight, a small round cream-colored dumpling-shaped mascot with a green sprout on top, big round innocent dot eyes, a tiny smile, pink blush cheeks, soft plush texture, wearing a tiny suit, stands alone at center court. Around it in the dark stands, crowds of smaller cream dumpling mascots with frowning downturned mouths and angry eyebrows wave signs and toss paper cups that float down slowly. The character shrinks smaller under the pressure. Then it pauses, takes a breath, and puffs up its round body with sudden resolve, standing taller. Suddenly golden confetti explodes from above, it lifts a shiny trophy overhead with trembling tiny arms, its sprout wiggling with joy. Camera slowly zooms in as the light shifts from cold white to warm gold. 3D Pixar-style kawaii animation, emotional atmosphere.
```

---

# Story B — 大谷翔平：百年一遇的雙刀流

> 一支 10 秒影片：被質疑 → 同時投打 → 傳奇定格

```
Consistent character design, single continuous shot. In a bright baseball locker room, a small round cream-colored dumpling-shaped mascot with a green sprout on top, big determined dot eyes, a tiny focused mouth, pink blush cheeks, soft plush texture, holds a bat in one hand and a glove in the other. Five slightly smaller cream dumpling mascots with stern frowning eyebrows and down-turned mouths in dark suits stand around it shaking their heads. The character walks past them toward the field. Cut to a sunlit diamond — it winds up its round body like a coiled spring and hurls a fastball with a white speed trail, then instantly appears at bat and crushes the ball into the sky. The ball becomes a tiny star. Camera follows the rising ball. Bright sunshine to dramatic lens flare. 3D Pixar-style kawaii animation, triumphant atmosphere.
```

---

# Story C — Clark vs Paige：WNBA 新魔鳥大戰

> 一支 10 秒影片：登場 → 對決 → 致敬

```
Consistent character design, single continuous shot. In a dark arena, two small round cream-colored dumpling-shaped mascots with green sprouts on top and pink blush cheeks, soft plush texture, emerge from opposite tunnel entrances. The left one in a blue-gold jersey has sharp upturned eyes and a confident grin, bouncing out energetically. The right one in a green-white jersey has calm half-closed eyes and a cool composed expression, walking out steadily. They meet at center court, charge at each other, and their round bodies collide with a bright flash, bouncing apart. Then they pause, exhausted, shoulders drooping. One extends a tiny arm, the other grabs it, and they share a brief respectful hug. Camera holds wide then slowly pushes in. Arena light shifts from intense white to soft warm gold. 3D Pixar-style kawaii animation, dramatic to warm atmosphere.
```

---

## 角色差異化圖解

```
所有角色都是同一個「米色團子+綠芽+粉腮紅」家族

        😊 主角             😎 老闆            😠 反對者
    大圓眼+天真笑        +小黑框眼鏡        八字眉+嘴角下垂
    
        😤 Clark型          😌 Paige型          🙂 群眾
    上挑眼+頭帶+笑       半閉眼+冷靜嘴       小一號+統一表情
```

---

## v3 → v4 改動

| 項目 | v3 | v4 |
|------|----|----|
| 角色顏色 | bright-red 紅色 ❌ | cream-colored 米色 ✅ |
| 角色形狀 | sweet potato | dumpling-shaped（更接近官方） |
| 角色差異化 | 全部長一樣 | 透過眉眼+配件區分身份 |
| 格式 | 3 個 prompt / 故事 | 1 個 prompt / 故事（直接生成） |
| 反對者 | dark-blue 深藍色 | 同家族米色但八字眉+皺眉 |

## 使用方式

1. 複製 ``` 區塊內容
2. 貼到 Gemini
3. 選 10 秒、16:9（橫版）或 9:16（豎版）
4. 每個跑 3-5 次挑最好的
5. 三支故事影片可獨立發布，也可剪在一起做合集

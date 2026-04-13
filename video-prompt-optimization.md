# AI 影片 Prompt 優化指南 — 小紅書短影片實戰

## 一、Prompt 核心公式

每一段 AI 影片 prompt 都應包含以下要素，順序可調整但缺一不可：

```
[主體 Subject] + [動作 Action] + [場景 Scene] + [鏡頭運動 Camera] + [光線 Lighting] + [風格/情緒 Mood] + [技術參數 Specs]
```

### 範例

> 一位穿著白色連衣裙的年輕女性 (Subject)，在櫻花樹下緩緩轉身微笑 (Action)，背景是京都古寺的石階 (Scene)，慢速環繞鏡頭 (Camera)，柔和的黃金時段側光 (Lighting)，夢幻柔焦氛圍 (Mood)，9:16 竪屏、淺景深 (Specs)

### 進階八點公式 (Shot Grammar)

| 要素 | 說明 | 範例 |
|------|------|------|
| Subject 主體 | 人物/物體的外觀、服裝、表情 | 一位短髮女生，穿米色針織毛衣 |
| Emotion 情緒 | 畫面想傳達的感覺 | 溫暖、治癒、nostalgic |
| Optics 光學 | 鏡頭焦段、景深 | 50mm 人像鏡頭、淺景深柔化背景 |
| Motion 運動 | 鏡頭如何移動 | slow dolly forward、gentle orbit |
| Lighting 光線 | 光源方向、色溫、質感 | warm amber side light、overcast diffused |
| Style 風格 | 影像風格參考 | 日系膠片感、電影調色 |
| Audio 音訊 | 音樂/音效提示（部分工具支援） | 輕柔鋼琴 BGM |
| Continuity 連續性 | 多鏡頭之間的銜接邏輯 | 從特寫過渡到中景 |

---

## 二、鏡頭語言速查表

鏡頭運動是讓 AI 影片從「PPT 感」變「電影感」的關鍵。

| 鏡頭術語 | 效果 | 適合場景 |
|----------|------|----------|
| **Slow dolly forward** | 緩慢推進，營造沉浸感與張力 | 開場、產品特寫 |
| **Slow dolly backward** | 緩慢拉遠，揭示全景 | 揭曉環境、結尾 |
| **Pan left/right** | 水平搖攝，引導視線 | 展示空間、多人場景 |
| **Tilt up/down** | 垂直搖攝 | 展示建築、人物全身 |
| **Orbit / Arc shot** | 環繞主體旋轉，增加動感與深度 | 人物展示、產品 360° |
| **Crane shot (rising)** | 由低到高升起，營造宏偉感 | 風景、城市天際線 |
| **Tracking shot** | 跟隨主體移動 | 行走、跑步場景 |
| **Handheld** | 手持搖晃感，增加真實感 | Vlog 風格、紀實感 |
| **Static / Locked-off** | 固定鏡頭，穩重感 | 美食特寫、靜物 |
| **Rack focus** | 焦點從前景轉到背景（或反之） | 製造焦點轉移、懸念 |
| **Zoom in/out** | 焦距變化，聚焦或展開 | 強調細節、情緒轉折 |

**黃金法則：每段 clip 只用 1-2 種鏡頭運動，太多會混亂。**

---

## 三、光線描述技巧

光線描述能大幅提升畫面質感：

| 光線類型 | Prompt 關鍵詞 | 氛圍 |
|----------|--------------|------|
| 黃金時段 | golden hour, warm amber light | 溫暖、浪漫 |
| 藍調時刻 | blue hour, cool twilight tones | 寧靜、文藝 |
| 頂光 | overhead harsh sunlight | 夏日、戶外活力 |
| 側光 | dramatic side lighting | 質感、輪廓分明 |
| 逆光 | backlit silhouette, rim light | 夢幻、剪影 |
| 霓虹 | neon-lit, cyberpunk palette | 潮流、夜生活 |
| 漫射光 | overcast diffused light, soft window light | 日系、治癒 |
| 燭光 | candlelit, warm flickering glow | 氛圍感、親密 |

---

## 四、小紅書短影片的特殊要求

### 4.1 格式規格

- **比例**：9:16 竪屏（必須在 prompt 中指定）
- **時長**：15-60 秒為佳（黃金長度 20-30 秒）
- **解析度**：至少 1080p，prompt 中加 "high quality, 4K"

### 4.2 內容節奏公式：3-20-7

| 段落 | 時間 | 作用 | Prompt 策略 |
|------|------|------|-------------|
| **Hook 開頭** | 前 3 秒 | 抓住注意力，阻止滑走 | 視覺衝擊力強的鏡頭：特寫、快速運動、反差畫面 |
| **主體內容** | 中間 20 秒 | 傳遞核心價值/資訊 | 節奏適中的運鏡，場景切換保持連貫 |
| **CTA 結尾** | 最後 7 秒 | 引導互動（點讚、收藏、關注） | 溫暖收束鏡頭，留有餘韻 |

### 4.3 小紅書爆款內容類型

針對不同內容類型，prompt 風格也不同：

| 類型 | Prompt 風格重點 | 範例關鍵詞 |
|------|----------------|-----------|
| 美食探店 | 特寫 + 暖光 + 慢動作 | close-up, warm lighting, slow motion cheese pull |
| 穿搭展示 | 全身 + 環繞 + 自然光 | full body shot, orbit, natural daylight |
| 旅行 Vlog | 航拍 + 跟拍 + 寬景 | drone shot, tracking, wide angle, golden hour |
| 護膚/美妝 | 微距 + 柔光 + 產品特寫 | macro shot, soft diffused light, product detail |
| 居家生活 | 固定鏡頭 + 窗光 + 慢節奏 | static shot, window light, cozy atmosphere |
| 知識分享 | 乾淨背景 + 穩定 + 文字空間 | clean background, steady, space for text overlay |

---

## 五、Prompt 撰寫原則

### 5.1 DO（要做的）

1. **具體描述動作**：不要寫「人在走路」，要寫「女生在落葉覆蓋的林蔭道上緩步前行，微風吹動她的髮絲」
2. **用電影術語**：dolly, pan, tracking, crane — AI 模型對這些專業術語反應極好
3. **控制 prompt 長度在 40-80 字（英文）**：太短缺乏控制，太長容易混亂
4. **指定情緒/氛圍**：dreamy, energetic, melancholic, cozy — 一個形容詞能改變整個畫面
5. **加入環境細節**：霧氣、雨滴、飄落的花瓣、光線中的灰塵粒子 — 增加畫面層次
6. **指定竪屏 9:16**：小紅書必須竪屏

### 5.2 DON'T（不要做的）

1. **不要寫模糊指令**：「一段好看的影片」→ 模型不知道你要什麼
2. **不要塞太多動作**：一段 clip 只做一件事，多段再用剪輯軟體拼接
3. **不要忽略光線**：光線是 AI 影片質感的最大變量
4. **不要期待完美人臉**：目前 AI 影片的人臉仍是弱項，可用側臉、背影、遠景規避
5. **不要用否定句**：「不要有人」不如「空曠的街道」— AI 對正面描述反應更好
6. **不要一次生成完整影片**：分鏡頭生成 → 後期拼接，品質遠高於一次到位

---

## 六、主流 AI 影片工具特性（2026）

選對工具再寫 prompt，事半功倍：

| 工具 | 強項 | Prompt 偏好 | 小紅書適用度 |
|------|------|------------|-------------|
| **Sora 2** | 物理模擬真實、時間一致性強 | 結構化長 prompt，詳細描述物理交互 | ★★★★★ |
| **Veo 3.1** | 精確執行指令、畫質頂級 | 當作渲染引擎用，結構化指令 | ★★★★★ |
| **Kling 2.6/3.0** | 人物動作自然、支援參考影片 | 配合參考圖/影片效果更好 | ★★★★★ |
| **Seedance 2.0** | 音畫同步、節奏匹配 | 可描述音樂節奏與畫面配合 | ★★★★☆ |
| **Runway Gen-4** | 風格化強、藝術感 | 風格描述詞反應好 | ★★★★☆ |
| **即夢 AI (Jimeng)** | 中文 prompt 友好、音畫一體 | 直接用中文描述，集成配音 | ★★★★★ |

**建議工作流**：同一個 prompt 在 2-3 個工具上生成 → 比較選最佳 → 精修 prompt → 再生成

---

## 七、完整工作流程

```
1. 選題構思 → 確定內容類型和目標受眾
       ↓
2. 分鏡腳本 → 拆成 3-5 個鏡頭，每個鏡頭寫獨立 prompt
       ↓
3. Prompt 撰寫 → 套用公式：主體 + 動作 + 場景 + 鏡頭 + 光線 + 情緒 + 規格
       ↓
4. 多工具生成 → 同一 prompt 在 2-3 個工具上跑，選最佳結果
       ↓
5. 精修迭代 → 根據結果微調 prompt，再次生成
       ↓
6. 後期剪輯 → 用剪映/CapCut 拼接、加字幕、配音、BGM
       ↓
7. 加入「人味」→ 融入真實體驗、口語化旁白、個人觀點
       ↓
8. 發布優化 → 吸睛標題、相關標籤、互動引導語
```

---

## 八、實戰 Prompt 範例（小紅書場景）

### 範例 1：咖啡探店

```
Close-up of a latte art being poured in slow motion, warm amber
side lighting from a nearby window, steam rising gently, cozy
cafe interior with wooden furniture in soft bokeh background,
9:16 vertical, shallow depth of field, 50mm lens, cinematic
color grading with warm tones.
```

### 範例 2：穿搭展示

```
Medium full-body shot of a young woman in a beige trench coat
walking confidently down a tree-lined Parisian street, gentle
orbit camera movement, autumn leaves falling, golden hour
backlight creating rim light on her silhouette, 9:16 vertical,
editorial fashion photography style, soft film grain.
```

### 範例 3：旅行風景

```
Cinematic drone shot slowly rising above a turquoise ocean
coastline at sunrise, revealing a hidden beach cove with white
sand, gentle waves lapping the shore, mist hanging over distant
cliffs, 9:16 vertical, wide angle, vibrant yet natural colors,
4K quality, peaceful and awe-inspiring mood.
```

### 範例 4：居家治癒

```
Static eye-level shot of a hand slowly pouring hot tea into a
ceramic cup on a wooden table, soft diffused window light from
the left, rain visible through the window in the background,
a small vase of dried flowers beside the cup, 9:16 vertical,
cozy Japanese aesthetic, shallow depth of field, warm muted
color palette.
```

### 範例 5：護膚產品

```
Extreme close-up macro shot of a drop of serum falling onto
smooth skin in slow motion, creating a tiny splash, soft ring
light with dewy highlight reflections, clean minimal white
background, 9:16 vertical, beauty commercial aesthetic,
crisp 4K detail, fresh and luxurious mood.
```

---

## 九、避免 AI 味的關鍵技巧

小紅書用戶對「AI 味」非常敏感，以下技巧能讓內容更自然：

1. **不要直接發 AI 生成的原片** — 一定要經過剪輯、調色、加字幕
2. **混合真實素材** — AI 片段 + 手機實拍混剪，大幅降低 AI 感
3. **加入真人配音** — 用自己的聲音錄旁白，而非 AI 語音
4. **融入個人觀點** — 文案要有「我」的視角，分享真實感受
5. **適當加入不完美** — 輕微的手持晃動、自然的環境音，增加真實感
6. **控制單段 AI 片段時長** — 每段 AI 素材不超過 3-5 秒，快速切換減少破綻

---

*最後更新：2026-04-13*

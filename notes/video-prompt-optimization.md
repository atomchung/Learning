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

## 十、棒球動作描述技巧（運動類影片專題）

棒球動作快速、爆發力強，對 AI 影片生成是高難度題材。以下是讓 prompt 精準控制棒球畫面的技巧。

### 10.1 核心原則：拆解動作階段

棒球動作發生在不到 1 秒內，AI 模型很難一次完美還原整個連續動作。**關鍵技巧是把動作拆成明確的階段**，每段 prompt 只描述一個階段：

#### 投球 (Pitching) — 四階段拆解

| 階段 | 英文術語 | 描述重點 |
|------|---------|---------|
| 1. 準備 Wind-up | wind-up stance, glove at chest | 身體側對打者、手套貼胸前、重心在後腳 |
| 2. 抬腿 Leg Kick | high leg kick, knee raised to chest | 前導腳抬至最高點、身體蓄力、平衡姿勢 |
| 3. 跨步出手 Stride & Release | explosive stride forward, arm whipping overhead, ball release | 前腳大步跨出、手臂鞭甩、球離手瞬間 |
| 4. 完成動作 Follow-through | follow-through, arm sweeping across body | 手臂慣性橫掃身體、後腳自然跟進 |

#### 打擊 (Batting) — 四階段拆解

| 階段 | 英文術語 | 描述重點 |
|------|---------|---------|
| 1. 站姿 Batting Stance | batting stance, knees slightly bent, bat raised | 雙腳略寬於肩、膝蓋微彎、球棒舉於耳側 |
| 2. 啟動 Load & Stride | weight shifting back, front foot stepping forward | 重心後移蓄力、前腳小步跨出 |
| 3. 揮棒 Swing | explosive hip rotation, bat whipping through the zone, ball contact | 下半身啟動 → 髖部旋轉 → 手臂帶出球棒 → 擊球瞬間 |
| 4. 收棒 Follow-through | full follow-through, bat wrapping around shoulders | 球棒繞過肩膀、目光追隨球路 |

#### 守備 (Fielding)

| 動作 | 描述重點 |
|------|---------|
| 接球 Catch | glove snapping shut, ball hitting leather with impact |
| 飛撲 Diving Catch | full-body dive, arm fully extended, glove reaching |
| 雙殺 Double Play | quick glove-to-hand transfer, sidearm throw, pivot on second base |
| 滑壘 Sliding | feet-first slide, dust cloud rising, hand reaching for base |
| 跑壘 Base Running | explosive sprint, head down, rounding the base wide |

### 10.2 鏡頭角度選擇

棒球的觀賞性高度依賴拍攝角度，不同角度呈現完全不同的感覺：

| 鏡頭角度 | 英文 Prompt 寫法 | 最適合拍什麼 |
|----------|-----------------|-------------|
| **中外野正面** | center field camera, behind the pitcher | 經典轉播視角，完整看到投打對決 |
| **低角度三壘側** | low angle from third base side | 投球動感、速度感強 |
| **打者背後** | over-the-shoulder from behind the batter | 打者視角、代入感強 |
| **正側面** | profile view, perpendicular to the pitch | 動作分析感、技術教學 |
| **高角度俯拍** | high overhead shot, bird's eye view | 全場跑壘路線、守備佈陣 |
| **低角度仰拍** | low angle looking up at the batter | 英雄感、力量感 |
| **捕手視角** | catcher's POV, behind home plate | 來球壓迫感、沉浸感 |

### 10.3 動態與速度感描述

運動影片的靈魂在於**速度與力量的視覺化**：

| 技巧 | Prompt 關鍵詞 | 效果 |
|------|-------------|------|
| 慢動作 | ultra slow motion, 120fps, time stretched | 拆解瞬間動作，展示力與美 |
| 速度線/動態模糊 | motion blur on the ball, speed streaks | 強調球速 |
| 定格瞬間 | freeze frame at the moment of contact | 戲劇性的決定瞬間 |
| 灰塵飛揚 | dust particles exploding from the dirt | 滑壘、落地的衝擊感 |
| 汗水飛濺 | sweat droplets flying off in slow motion | 努力與拼搏的細節 |
| 肌肉線條 | visible muscle tension, veins on forearm | 力量感（特寫鏡頭） |
| 球的旋轉 | ball spinning with visible seam rotation | 展示球路變化（曲球、滑球） |

### 10.4 光線與氛圍

| 場景 | 光線 Prompt | 效果 |
|------|-----------|------|
| 白天戶外 | bright daylight, harsh sunlight casting sharp shadows | 真實比賽感 |
| 黃昏比賽 | golden hour, long shadows across the diamond | 史詩感、浪漫 |
| 夜間燈光 | stadium floodlights, dramatic top-down lighting, light halos | 職業賽事感 |
| 練習場 | soft morning light, misty field, dewy grass | 青春、訓練的純粹感 |
| 室內練習 | indoor batting cage, fluorescent lighting | 專注、訓練氛圍 |

### 10.5 實戰 Prompt 範例

#### 範例 1：投球慢動作（技術展示風格）

```
Profile view of a baseball pitcher in a white uniform in ultra
slow motion, explosive stride forward with front leg extending,
arm whipping overhead at the moment of ball release, fingers
snapping off the seam, sweat droplets flying, dust rising from
the mound, dramatic stadium floodlights from above, shallow
depth of field with blurred crowd in background, 9:16 vertical,
cinematic sports documentary style, 4K.
```

#### 範例 2：打擊瞬間（力量感風格）

```
Low angle shot looking up at a batter in a dark navy uniform,
explosive hip rotation driving a powerful swing, bat connecting
with the ball at the moment of impact, slight motion blur on
the bat speed, ball compressing against the bat in ultra slow
motion, golden hour sunlight backlighting the scene with lens
flare, dust particles floating in the warm light, 9:16 vertical,
epic cinematic atmosphere, shallow depth of field.
```

#### 範例 3：飛撲接殺（戲劇性風格）

```
Dynamic tracking shot of an outfielder in full sprint, launching
into a horizontal diving catch, arm fully extended with glove
reaching for the ball, body parallel to the grass in mid-air,
time slowing to ultra slow motion at the peak of the dive, dirt
and grass fragments scattering, dramatic side lighting from
stadium lights, 9:16 vertical, intense sports action style, 4K.
```

#### 範例 4：青春棒球（小紅書治癒風格）

```
Soft medium shot of a young player standing in a sunlit batting
cage during early morning practice, gentle slow motion swing
with a relaxed follow-through, morning mist diffusing the warm
golden light, dewy grass visible in the foreground bokeh, quiet
and peaceful atmosphere, 9:16 vertical, nostalgic film grain,
Japanese youth baseball aesthetic, dreamy color grading.
```

### 10.6 常見錯誤與修正

| 錯誤寫法 | 問題 | 修正寫法 |
|----------|------|---------|
| "A person playing baseball" | 太模糊，AI 不知道拍什麼 | "A pitcher in wind-up stance on the mound" |
| "Fast pitch" | 沒有視覺描述 | "Ball leaving the pitcher's hand with motion blur, 95mph fastball" |
| "Cool baseball video" | 零資訊量 | 指定動作階段 + 鏡頭 + 光線 |
| "Batter hits a home run and runs the bases" | 一段 prompt 塞太多動作 | 拆成：揮棒擊球 / 球飛出場 / 繞壘跑 三段分別生成 |
| "No mistakes in the swing" | 否定句，AI 無法理解 | "Perfect textbook swing with smooth hip rotation" |

---

*最後更新：2026-04-13*

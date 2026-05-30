# XHS Content Generator — AutoResearch 研究總覽

> 主要研究執行在 `/Users/atomo/Side_project/xhs_autoresearch/`
> 本資料夾存放框架規劃文件，實驗結果和 summaries 在 xhs_autoresearch 目錄

---

## 四個維度的研究狀態

### 1. 標題 (Title) — ✅ 完成
**Summary**: `xhs_autoresearch/title_autoresearch_summary.md`
**Final Report**: `xhs_autoresearch/runs/v3_final_report.md`
**最佳 Template**: `xhs_autoresearch/templates/title_prompt_v3.md`

研究規模：605+ 輪 A/B 評估，跨 4 個 Phase
- Phase 1: Gemini API，5 話題 × 16 輪，50 → 0% 接受率
- Phase 2: Claude Agent，5 話題 × 25 輪
- Phase 2.5: v2 嚴格 20 字限制，10 話題 × 20 輪，平均 36.5% 接受率
- Phase 2.6 (v3): 18-20 字 + Hook Density，10 話題 × 20 輪，平均 **35% 接受率**

**核心發現**：
- 對比鉤子（"你以為X...其實Y"）83% 勝率 — 最強武器
- 數字不可移除 — 移除後僅 4% 勝率
- 18-20 字全密度原則 — 每個字都要賺到位置
- Street-smart analyst 語氣 — "說白了" 是唯一成功語氣

---

### 2. 封面圖 (Cover Image) — ✅ 完成
**Summary**: `xhs_autoresearch/cover_image_autoresearch_summary.md`

研究規模：30 輪，53% 改善率（16 接受 / 14 淘汰）
- R1-R10: 60% 接受率（架構建立期）
- R11-R20: 60% 接受率（深化期）
- R21-R30: 40% 接受率（收斂期）→ 已達局部最優

**核心發現**：
- 具體動作姿態 > 攝影語言描述 > 光影氛圍
- 減法策略全失敗（刪元素幾乎都被淘汰）
- 品牌調性（Game Cinematic 風格）是硬邊界，不能違背

---

### 3. 內文/正文 (Body Content) — ⚠️ 已跑完實驗，缺整合 Summary
**實驗目錄**: `xhs_autoresearch/runs/body_*/`

| 話題 | 目錄 | 輪數 | 接受 | 狀態 |
|------|------|------|------|------|
| Caitlin Clark WNBA | body_clark | 25 | 9 (36%) | ✅ 完成 |
| F1 中國大獎賽 | body_f1 | 25 | 10 (40%) | ✅ 完成（含詳細 summary）|
| Messi MLS | body_messi | 25 | 6 (24%) | ✅ 完成 |
| 大谷翔平 | body_ohtani | 25 | ? | ✅ 完成（無詳細 summary）|
| 鄭欽文 | body_zheng | 25 | ? | ✅ 完成（無詳細 summary）|

**body_f1 已知發現**（最完整）：
- `add_scene_scripting` — 6/6 接受，最強策略（在特定場景下加入畫面感描述）
- `adjust_module_count 4→3` — 3/3 接受（3 塊比 4 塊好）
- 所有縮短字數策略 → 0/4 全敗
- 所有換 closing 策略 → 幾乎全失敗（三選一、預測、站隊、反轉都失敗）

**待做**：整合 5 個話題的跨話題發現，產出 `body_autoresearch_summary.md`

---

### 4. 故事角度/選題 (Story Angle) — ❌ 尚未開始
Auto Research 實驗尚未執行。
現有的是 Skill 規範（非實驗優化），位置：
- `xhs_skills/skills/xhs-topic-angle-shortlist/SKILL.md`

**待規劃**：設計 story angle 的 mutation 策略和評分維度

---

## 下一步行動

| 優先級 | 任務 | 描述 |
|--------|------|------|
| 🔴 P1 | 整合 body summary | 分析 5 個 body_* 目錄，產出跨話題發現 |
| 🟡 P2 | 啟動 story angle 實驗 | 設計 mutation 策略 + 評分維度 |
| 🟢 P3 | 標題結果回寫 SKILL.md | 把 v3 final report 的規則更新到 skill |

---

## 相關檔案位置索引

| 類型 | 路徑 |
|------|------|
| 實驗主目錄 | `Side_project/xhs_autoresearch/` |
| 標題 summary | `xhs_autoresearch/title_autoresearch_summary.md` |
| 封面 summary | `xhs_autoresearch/cover_image_autoresearch_summary.md` |
| 標題最終報告 | `xhs_autoresearch/runs/v3_final_report.md` |
| 正文實驗 | `xhs_autoresearch/runs/body_clark|f1|messi|ohtani|zheng/` |
| 框架規劃 | `ai_project_research/xhs_content_generator/autoresearch-xhs-plan.md` |
| 帳號 DNA | `xhs_skills/skills/xhs-sports-hot-knowledge/references/account-dna.md` |
| 風格指南 | `rednote_analysis/style_guide.md` |

---
name: meta-review
description: 遞迴改進 harness 的 review 迴圈（Issue #6）。讀 meta/defects.md + 近期 inbox，把累積的缺陷轉成對 harness（CLAUDE.md / profile / hook / skill）的少量修改。Use when the user invokes /meta-review, 或想定期檢視「這套腦哪裡爛、規則該怎麼改」。
---

# meta-review：把 harness 缺陷轉成規則修改

這是「遞迴改進 harness」的 L2 動作：改進者改進改進者。物件層迴圈（boot/awake/sleep）跑出缺陷 → 這個 skill 讀缺陷 → 改寫物件層的規則本身 → 下次 boot 在新規則下跑。

## 為什麼存在

模型（Claude）動不了，唯一能遞迴改進的是 harness。這個 skill 是讓 harness 真的改進、而不只是內容堆積的那一步。詳見 Issue #6 與 `notes/anthropic-blog-2026-06.md`。

## 步驟

1. **讀梯度**：讀 `meta/defects.md` 全部 + `inbox.md` 最近約一個月。
2. **歸類**：把缺陷按四類（boot-miss / retrieval-miss / rot / merge-gap）分組，找**重複出現**的類別——重複的才值得改規則，一次性的略過。
3. **提修改**：針對重複缺陷，提出 **≤3 條**對 harness 的具體修改。每條要寫：
   - 改哪個檔案（CLAUDE.md / profile.md / settings.json hook / 某 skill）
   - 改什麼（規則句，不是個案修補）
   - 對應消除哪一類缺陷
4. **反膨脹閘（硬約束）**：這批修改裡，**每新增兩條規則，必須刪掉一條舊規則**。優化目標是「每單位記住的知識、摩擦更低」，不是「更多結構」。提不出可刪的，就把新增也砍到只剩最關鍵那條。
5. **先確認再改**：用 AskUserQuestion 把這批修改攤給用戶選，**不要自己直接改 CLAUDE.md**（它是契約，變更要共識）。
6. **落地**：用戶同意後改 harness、把已轉化的缺陷在 defects.md 標記處理過（或移到「已消化」段），commit，merge 進 main。

## 邊界

- 不是每次 session 跑，是累積一批缺陷後（月度或用戶喊）才跑。
- 不新增複雜結構去「優化」——能刪規則的 review 才是對的 review。
- defects.md 是空的就直接說「這輪沒梯度可學」，不要硬擠修改。

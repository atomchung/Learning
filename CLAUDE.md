# CLAUDE.md — Learning repo 工作方式

這個 repo 用 **Heptabase 啟發的學習結構**來累積知識資產。每次 session 請先讀這份檔案再開始工作。

## 原則（為什麼這樣做）

詳細推論在 `heptabase-design-research.md`。核心三條：

1. **原子化**：知識的儲存單位是「一句話能說完的判斷」，不是章節或主題
2. **由下而上**：結構從卡片之間的關係浮現，不預先規劃目錄
3. **Create 是副產品**：長文是卡片重組的結果，不是起點

## 目錄結構

```
/
├── CLAUDE.md                     # 這份（給 agent 看的契約）
├── heptabase-design-research.md  # 方法論推導（為什麼用這套）
├── compare-coding-agents.md      # Create 階段產物（留著當參考）
└── topics/
    └── <topic-name>/
        ├── _start.md             # 起點卡：磁鐵，累積未拆發現
        ├── cards/                # 原子卡：一張一個判斷
        │   └── <kebab-case-claim>.md
        └── journey/              # 理解快照
            └── YYYY-MM-DD.md
```

**一個主題 = 一個 `topics/<name>/` 資料夾**。不要把多個主題混在一起。

## 檔案格式

### 原子卡（`cards/*.md`）

```markdown
---
type: card
title: <判斷句，不是主題名>
aliases: [同義標題]
tags: [主題, 領域]
appears-on:
  - <topic-1>
  - <topic-2>    # 跨脈絡出現才有重用價值
created: YYYY-MM-DD
---

# <判斷句標題>

**一句話**：<把整張卡壓縮成一句話>

## <為什麼重要 / 核心權衡 / 證據>

## 反例與質疑
（強制考慮反論，避免單邊思考）

## 連結
- ← 支持 [other-card](./other-card.md)（被誰當證據引用）
- ↔ 對比 [other-card](./other-card.md)（光譜上的另一端）
- → 引出 [other-card](./other-card.md)（從這推出的衍生問題）

## 出處
<來源檔案段落 + 外部連結>
```

**卡片標題規則**：title 必須是**判斷句**，不是主題名。
- ❌ 「Harness 介紹」「Codex 的沙箱」
- ✅ 「Harness 的影響大於換模型」「Codex 用即時性換隔離性」

### 起點卡（`_start.md`）

```markdown
---
type: starting-point
topic: <topic-name>
status: expanding | stable | archived
---

# 起點：<主題的核心問題>

## 當下的核心問題
## 已拆出的卡（N 張，分類列出）
## 還沒拆但累積中的發現
## 下一步可能要拆的卡
## 相關白板（未來主題）
```

起點卡是**磁鐵**，不是**目錄**。新讀到的東西先塞進「累積中」那欄，看出子概念時再拆卡。

### Journey（`journey/YYYY-MM-DD.md`）

**節奏**：每週五固定寫一次 + 有跳躍感時立刻加寫（frontmatter 的 `trigger: weekly | jump`）。

```markdown
---
type: journey-snapshot
topic: <topic-name>
week-of: YYYY-MM-DD
trigger: weekly | jump
---

# <標題>

## 一句話當前理解
## 這次跳躍的內容（或 本週有哪些跳躍）
## 我還沒搞清楚的
## 對比上一篇
## 下一步要做什麼
```

**關鍵**：寫「目前我認為的答案」，不是「讀到什麼」。日後回看要能看出理解跳躍。

## Claude 的工作方式

### 開新主題時
1. 先問清楚邊界：題目是什麼？關心的核心問題是什麼？
2. 建立 `topics/<name>/_start.md`，只填「當下的核心問題」
3. 不要急著拆卡，先讓起點卡膨脹

### 處理閱讀材料
1. 先塞進起點卡的「累積中」清單（一行一發現）
2. 當某個發現累積到「可以講一個完整故事」時才拆成卡
3. 拆卡時 title 必須是判斷句，強制寫「反例」段落

### 重大結構調整（拆卡策略、資料夾重組等）
**使用 AskUserQuestion 先確認方向**，不要自己做主。過去幾次對話證實：用戶的方向判斷優於我的預設。

### 工作節奏回饋
- 重要中間決策主動反問（用戶已要求「過程中可以多反問拿 feedback」）
- 每完成一個可驗證的小塊（一張卡、一次重組）就停下來說明
- 不要一次做完再報告——用戶要參與中間過程

### 寫長文（Create 階段）
**禁止從零寫**。流程：
1. 從 `cards/` 挑出相關原子卡
2. 在腦中/文件中排列順序與關係
3. 用卡作為素材重組成文章
4. 產出後，長文放在 repo 根目錄（不放在 topics/ 裡面）

## 在手機上瀏覽（Obsidian 純讀模式）

當前架構：**寫透過 Claude Code mobile（直接寫 GitHub），手機 Obsidian 純讀**。所以 Obsidian 只需要單向 pull，不用 push、不用 Working Copy、不用 iCloud / Drive。

### 一次設定（iPhone）

1. **產 Read-only PAT**：Safari → `https://github.com/settings/personal-access-tokens/new`（fine-grained）→ Repo access 選 `atomchung/Learning` → Permissions → Contents: **Read-only** → 產生後複製
2. **建 Vault**：Obsidian → Create new vault → 名字 `Learning` → Location 選 **On My iPhone**（不放 iCloud）
3. **裝 Obsidian Git plugin**：Settings → Community plugins → Turn on → Browse → 搜 `Obsidian Git` → Install + Enable
4. **Clone repo**：Command palette（從螢幕底邊往上滑）→ `Obsidian Git: Clone an existing remote repo` → URL 填 `https://<GitHub帳號>:<PAT>@github.com/atomchung/Learning.git`
5. **設自動 pull**：Settings → Obsidian Git → 開 `Pull on startup` + `Pull updates every X minutes` 設 10。其他 push / commit 相關都關掉

### Android 設定
和 iPhone 幾乎一樣，跳過 Working Copy（Obsidian Git 在 Android 直接支援）。

### 純讀不同步（最最簡單）
不想設 Obsidian 也行：手機瀏覽器開 github.com/atomchung/Learning。只是 render 較樸素。

### 重要原則
**不要在手機 Obsidian 寫**。任何修改只會留在手機本地，不會回 GitHub，下次 pull 還可能起衝突。所有寫作走 Claude Code mobile。

### 使用時的心法
- 從 `topics/<主題>/_start.md` 進入，起點卡是整個主題的導航列
- **Graph view**（右上角圖示）可視化卡片連結網
- **Backlinks 面板**顯示哪些卡引用當前卡
- **Canvas**（左邊新建）= Obsidian 內建白板，可以拖卡片排版（類似 Heptabase）

## 手機可讀性規則

所有檔案要能在手機 GitHub 網頁/app 直接讀，不要破版。規則：

1. **表格最多 3 欄**（含表頭）。超過 3 欄改用「分組條列」：
   ```
   **分類 A**
   - 維度 1：值
   - 維度 2：值
   ```
2. **不要用 ASCII 圖**（箭頭網、方框、長橫線）。改用編號條列或簡單文字描述
3. **連結用相對路徑**：`[card](./card.md)`，不要用 `[[card]]`（GitHub 不會 render）
4. **段落短**：一段不超過 3-4 行繁中
5. **程式碼區塊可以有**，但避免放超長行

如果不確定某個格式手機會不會壞，**寧可拆成條列**。

## Git 工作流

- 分支：`claude/<topic-slug>-<random>`（由 harness 指派）
- Commit 訊息用英文 subject + 空行 + 繁中/英混合 body
- 每完成一個邏輯單元就 commit，不要攢大 commit
- Push 用 `git push -u origin <branch>`
- 除非用戶明說，不要開 PR

### Session 結束 merge 到 main（必做）
每次對話結束前，把這個 session 的 branch merge 進 main 並 push，讓使用者的 Obsidian / 其他裝置能看到成果：

```bash
# 確保 feature branch 上所有 commit 都 push 完
git push -u origin <當前-branch>

# 把當前狀態推成 main（first push 會建立 main；之後是 fast-forward）
git push origin HEAD:main
```

如果 main 已有不同提交而 fast-forward 不行，先：
```bash
git fetch origin
git checkout main && git pull
git merge --no-ff <當前-branch>
git push origin main
git checkout <當前-branch>
```

**例外**：如果這次 session 還沒到「可交付」狀態（只是中間草稿、用戶明說不要進 main），跳過此步驟並告知用戶。

## 當前 repo 狀態

- **現有主題**：`topics/coding-agents/`（13 張卡 + 2 份 journey）
- **方法論文件**：`heptabase-design-research.md`
- **歷史長文**：`compare-coding-agents.md`（即將被卡片反向替代）

## 維護

當你對這套方法有疑慮或改進想法時，**直接提出給用戶討論**，不要自己偷改 CLAUDE.md。這份文件是契約，變更需要共識。

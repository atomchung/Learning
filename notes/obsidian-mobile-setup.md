# 手機 Obsidian 純讀設定（一次性）

> 2026-07-04 首次 meta-review 從 CLAUDE.md 移出（償 R3：CLAUDE.md 壓行數）。
> 架構不變：**寫透過 Claude Code mobile（直接寫 GitHub），手機 Obsidian 純讀**。Obsidian 只需要單向 pull，不用 push、不用 Working Copy、不用 iCloud / Drive。

## 一次設定（iPhone）

1. **產 Read-only PAT**：Safari → `https://github.com/settings/personal-access-tokens/new`（fine-grained）→ Repo access 選 `atomchung/Learning` → Permissions → Contents: **Read-only** → 產生後複製
2. **建 Vault**：Obsidian → Create new vault → 名字 `Learning` → Location 選 **On My iPhone**（不放 iCloud）
3. **裝 Obsidian Git plugin**：Settings → Community plugins → Turn on → Browse → 搜 `Obsidian Git` → Install + Enable
4. **Clone repo**：Command palette（從螢幕底邊往上滑）→ `Obsidian Git: Clone an existing remote repo` → URL 填 `https://<GitHub帳號>:<PAT>@github.com/atomchung/Learning.git`
5. **設自動 pull**：Settings → Obsidian Git → 開 `Pull on startup` + `Pull updates every X minutes` 設 10。其他 push / commit 相關都關掉

## Android 設定

和 iPhone 幾乎一樣，跳過 Working Copy（Obsidian Git 在 Android 直接支援）。

## 純讀不同步（最最簡單）

不想設 Obsidian 也行：手機瀏覽器開 github.com/atomchung/Learning。只是 render 較樸素。

## 重要原則

**不要在手機 Obsidian 寫**。任何修改只會留在手機本地，不會回 GitHub，下次 pull 還可能起衝突。所有寫作走 Claude Code mobile。

## 使用時的心法

- 從 `topics/<主題>/_start.md` 進入，起點卡是整個主題的導航列
- **Graph view**（右上角圖示）可視化卡片連結網
- **Backlinks 面板**顯示哪些卡引用當前卡
- **Canvas**（左邊新建）= Obsidian 內建白板，可以拖卡片排版（類似 Heptabase）

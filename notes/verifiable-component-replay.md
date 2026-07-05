# Verifiable Component 架構 + Replay 錄影提高 Review 效果

學習來源：cwc-workshops how-we-claude-code / TurnPay 專案，2026-07-05

## 核心概念

Phase 3 驗證框架的設計：讓 React component 的每個狀態都是「可機器讀取 + 可目視重播」的。

兩條軸：

- **agent 讀**：headless 跑所有 fixture，結果寫到 `window.__verify`，agent 可以用 `await __verify.runAll()` 拿 JSON
- **人眼看**：`/verify/replay` 把每個 fixture 依序 mount 在畫面上，搭配 verdict 標籤，可以錄成 GIF 或 webm

## 實作結構

```
src/verify/
  core/           # contract / registry / runner / types
  verifiers/      # schema / invariants / dom-contract / a11y（可插拔）
  harness/        # Dashboard / UnitPage / ReplayPage / handle / recorder
  specs/          # Home.verify.ts / Stats.verify.ts
```

### Fixture 是什麼

每個 unit 定義多個 fixture = 固定 props 的場景，例如：

- `empty`：沒有任何記錄
- `balanced`：兩人剛好平衡
- `i-paid-more`：我付得比較多
- `partner-paid-more`（probe）：對方付比較多

Probe fixture 是「邊界條件探針」，單獨跑某個 invariant，等同於 property-based test 的手動版。

### DOM contract 是溝通協議

component 透過 `data-verify-*` 屬性把計算結果曝露出來：

```tsx
<div
  data-verify-unit="Home"
  data-verify-my-total={myTotal}
  data-verify-partner-total={partnerTotal}
  data-verify-delta={delta}
  data-verify-tx-count={monthExpenses.length}
>
```

verifier 從 DOM 讀，不直接測 state。好處是：UI 重構（把 useState 換成 zustand）不需要改 spec，只要 DOM attribute 還在就照跑。

### Invariant 是「這件事永遠要成立」

```ts
{
  id: 'delta-matches-totals',
  check: ({ contract }) => {
    const delta = Number(contract['delta'])
    const my = Number(contract['my-total'])
    const partner = Number(contract['partner-total'])
    return delta === my - partner || `delta=${delta}, my=${my}, partner=${partner}`
  }
}
```

check 回傳 `true` = pass，回傳字串 = fail + 失敗訊息。

## Replay 怎麼用

URL：`/verify/replay?dwell=1500`（dwell = 每個 fixture 停留毫秒數）

操作：
- 自動逐一 mount → 跑 verifier → 顯示 PASS/FAIL → 停留 → 下一個
- 鍵盤：Space 暫停、→ 跳過、Esc 停止
- `?chrome=0` 隱藏控制列，適合螢幕錄製

錄 GIF 的流程（瀏覽器 automation）：
1. 開 `/verify/replay?dwell=1800`
2. 確認 CSS 不限制 `#root` 寬度（見「踩到的坑」）
3. 用 gif_creator 截圖 + stop + export

**錄 webm（逐 fixture 分片）**：點「Record clips」按鈕，瀏覽器 getDisplayMedia 錄製，每個 fixture 各一個 .webm，最後可以一鍵下載全部。

## 踩到的坑

**`#root` 被 `max-width: 430px` 壓縮**：TurnPay 的 `index.css` 把整個 root 鎖在手機寬度，verify 的 replay frame 被截掉右半。

修法（`index.css`）：

```css
#root:has([data-verify-page]) {
  max-width: none;
  box-shadow: none;
  background: transparent;
}
```

`:has([data-verify-page])` — 只要 root 裡面有任何帶 `data-verify-page` 的元素，就撐開。verify page 的 harness 都有加這個 attribute，所以 app 主頁不受影響。

**`verbatimModuleSyntax` 需要 `import type`**：tsconfig 啟用後，所有只用在型別的 import 都要加 `type`，否則 Vite 的 ESM transform 報錯。

## 這套機制的真正價值

不是「多了一個 test runner」，而是讓**驗證結果變成可交付的視覺物件**。

- 傳統 unit test：綠燈 = 可以信任（但你不知道畫面長什麼樣）
- 這套：綠燈 + 8 個 fixture 的 GIF = 可以讓設計師、PM、別的 agent 直接目視確認

類比：CI 的 test report vs Storybook 的 visual snapshot。這套是兩者的交集：可機器跑 + 可人眼看。

## 可以套用的其他脈絡

**前端 component 直接套**：只要是 React component，加 `data-verify-*` attribute 和 fixture 就能跑。

**shell/script 的平移版**：沒有 DOM 的 CLI tool（skill、agent output）可以改成 fixture 是固定 input JSON，invariant 是 stdout 的 schema check。本質一樣，換了載體。

最有用的場景：skills 發給別人用之前，先跑一輪 fixture 確認每種 input 都有預期 output。

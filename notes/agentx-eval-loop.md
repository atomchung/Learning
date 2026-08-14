# AgentX 怎麼做 evaluation：值錢的不是打分，是證據回流與發布權

> 掃描日期：2026-08-14
> 觸發：使用者丟 https://github.com/AgentX-ai （Product Hunt 來的）問「他們怎麼做 evaluation，有沒有可以學的」
> 證據層級：**全部來自 vendor 自己的 README / sample code**，無第三方複現。self-host 版 1 star、Python SDK 68 star ＝早期產品。dashboard 閉源（只公開 build 產物）。當「設計參考」讀，不當「已驗證最佳實踐」。

## 一句話

AgentX 的打分方法本身平庸（LLM-as-judge + BLEU/ROUGE 那套老東西），**真正的設計在打分外面**：生產流量兩鍵變測試集、判官的判決要跟現實對帳、改動要先量測過才准發布、失敗證據累積到閾值就自動生成提案。這四條跟這個 repo 的記憶／缺陷迴圈同構，可以直接搬。

## 先記我的預測（校準用）

看之前我猜：又一個「LLM-as-judge + 好看的 dashboard」的 observability 產品，沒有新東西。
結果：**打分層確實如我所料沒有新東西**，但「判官被判官」和「證據累積自動觸發提案」兩塊超出預期——我原本預設這類產品只做到「記錄 + 顯示」，沒想到有人把 meta-eval 做成產品功能。
錯在哪：我把 eval 產品的競爭維度預設在「metric 有多聰明」，實際競爭維度是「摩擦有多低、迴圈有多閉」。

## 他們的打分方法（這層沒什麼可學）

- **LLM-as-judge**：自帶 key，OpenAI / Anthropic / Gemini 都支援。判官邏輯抽成獨立套件 `judge-core`，self-host 版和雲端版共用同一份實作。
- **四個內建相似度指標**：向量相似度、Jaccard、BLEU、ROUGE。預設全關，要自己打開。
- **沙箱自訂 code scorer**：要寫程式判準時用。
- **資料集層的判準是自然語言**：`acceptance_criteria`（什麼算對）+ `rejection_criteria`（什麼算錯），寫在 dataset 或獨立的 settings 物件上。
- **同一個 case 跑 N 次**（`number_of_requests`）看穩定度，不是跑一次就算。

判準與 settings 是**兩個可以分開重用的物件**——同一組嚴格判準可以套到不同資料集，這是他們少數在打分層做對的設計。

## 四個值得學的機制

### 1. 生產流量兩鍵變成 golden dataset

任何一條 trace 或一整段 session（多輪對話）都能兩鍵變成資料集案例，附去重與來源標記。

為什麼重要：eval 最大的摩擦從來不是跑分，是**建測試集**。把「這次出錯的真實案例」變成永久測試案例的成本壓到兩鍵，決定了這套東西會不會有人真的用。

### 2. 判官被判官（Judge Calibration）

線上評分器的每個判決，都拿去跟「記錄下來的現實」對帳——人工重評、真實 outcome（`outcomes.report`）、終端用戶投票（`feedback.report`，一個踩直接開一張 signal）。

**不一致的地方就是梯度**：從分歧反推、重寫這個評分器自己的判準，然後用「精確重判」驗證——修好它答錯的那些案例，同時**保住一組它原本就答對的控制組**——最後人來發布。

這條是整套裡最值錢的。細節在「保住控制組」：改判準防止修 A 壞 B。

### 3. 改動走 propose → 量測 → 人審 → publish

prompt 和 tool schema 都有版本註冊表。改動不是直接改，是提案；提案要對 golden case 跑「候選版 vs 現行版」的量測比較，帶著數字給人看；**人保有唯一的筆**（他們原文直說 humans keep the only pen），可以發布也可以駁回。

自動化跑到「帶著量測結論的提案」為止，發布一律要人。

### 4. 證據累積到閾值就自動觸發（Improvement Inbox）

背景 sweep 偵測到某個 prompt 或 tool schema 累積了足夠的新失敗證據，就**自動生成改進提案，並且自動把基線 vs 候選的驗證也跑完**，帶著量測結論排進收件匣等人審。

關鍵：觸發條件是**證據量**，不是人想到要跑。可以用環境變數關掉，也可以手動打 API 觸發一次。

### 附帶兩個小東西

- **CI gate**：`report.gate(fail_under=7, no_regression=True)` 回 exit code 擋 build，每次 gate 記進 dashboard，還有「用最新一輪跑會不會過」的預覽。
- **Model Portability**：把已擷取的 trace 輸入重放到別的模型，比成本／延遲／品質。這是[可驗證組件重放](./verifiable-component-replay.md)的產品化版本。

## 對到我們的系統：哪些能搬、哪些不用

### 能搬（按價值排序）

**第一，控制組。** 這個 repo 已經有預測帳（profile 裡結算 ✅／❌）和缺陷記錄（`meta/defects.md`），也有定期把缺陷轉成規則修改的迴圈。**缺的是控制組**：改 CLAUDE.md 規則時，沒有任何機制確認「原本沒問題的行為改完還是沒問題」。目前是單向的——看到一個缺陷、加一條規則、規則越加越多。AgentX 的做法是改判準時同時保留一組原本就通過的案例當對照。

**第二，證據門檻觸發，不靠自律。** 現在缺陷轉規則是靠想到才跑。可以改成有門檻：同類缺陷累積到 N 條就自動標記「該處理了」。這跟 repo 已有的「某判斷在 ≥3 條記錄出現過就升級成卡片」是同一個模式——那條已經用計數而非手感了，缺陷層還沒有。

**第三，改規則前先量測。** 現在改 CLAUDE.md 是直接改，沒有「改前 vs 改後」的比較。這條成本高、優先度低，但方向對。

### 不用搬

- **BLEU / ROUGE / Jaccard**：文本重疊指標，對判斷型任務（「這個結論對不對」）沒有意義。他們自己也預設關閉。
- **整套 tracing 基建**：這是給部署中的 production agent 用的，這裡沒有那種東西。

## 一個反直覺的觀察

他們把「人保有唯一的筆」寫成明確的設計原則，而不是能力不足的妥協——自動化被刻意停在提案階段。

這跟 eval 生態位那條判斷是同一件事的兩面：[eval 的瓶頸是寫判準不是跑分](./eval-ecosystem-niche.md)。既然判準是瓶頸，判準的修改權就是這套系統的核心資產，不能自動化掉。AgentX 把自動化全砸在「準備證據」上、把決策留給人，是認清了瓶頸在哪。

## 出處

- README：https://github.com/AgentX-ai/AgentX-trace-eval
- 範例程式：https://github.com/AgentX-ai/AgentX-Sample-Scripts （`sdk_eval_samples/`，五支：資料集建立、LangChain 帳務爭議 eval、OpenAI 簡易 eval、prompt registry、無 trace 的簡易 eval）
- 相關筆記：[eval 的生態位](./eval-ecosystem-niche.md)、[可驗證組件重放](./verifiable-component-replay.md)

# Cursor × SpaceX × xAI：Composer 3 與被收編的中立 harness

> 2026-06-20。源於一張 FB 貼文（Fox Hsiao），追問四輪查證後的整理。
> 主結論：這不是「一個更強的 coding 模型」的故事，是「Cursor 被 Musk 收進 xAI 垂直棧」的故事。

## 事件本體（都查證為真，非假新聞）

- **6/12**：SpaceX IPO，發行價 $135、估值約 $1.77 兆，史上最大 IPO，首日 +25%。
- **6/16**：SpaceX 全股票收購 Cursor（Anysphere），約 **$600 億**，Q3 完成，Cursor 成 SpaceX 子公司。
- 同日 **Compile 大會**發三樣：模型 **Composer 3**（預覽）、**Cursor Mobile**（TestFlight）、**Origin**（agent-first 的 Git forge）。

一度以為是 AI 編的假貼文（SpaceX 買 coding 工具、SpaceX IPO 都太離譜），查證後全真。**坑**：別因為「聽起來離譜」就先判假——這次正是用戶自己「讀信號要先驗真」原則的反面教材，我差點犯。

## Composer 3 的「能力」與「評分」

- **還沒上線**：6/16 是發表/預覽，不是 release。所有「Opus / GPT-5.5 同量級、1.5T、10 萬 GPU」都是 **Cursor 自家宣稱**，**無任何第三方 benchmark**。當估計值，先別記分。
- **能拿來估的代理＝Composer 2.5**（5/18 上線、有中立數據）：
  - Coding Agent Index **62 分、第三名**（輸 Opus 4.7 max 66、GPT-5.5 xhigh 65，差 3–4 分）。
  - SWE-Bench Multilingual **79.8%**、Terminal-Bench 2.0 **69.3%**（GPT-5.5 以 82.7% 領先 ~13 分）、CursorBench v3.1 **63.2%**。
  - **真正殺手鐧＝成本**：同分數下每任務便宜 **10–60 倍**。
- **真實定位**：不是榜首，是「**性價比前沿**」——分數打平、價格砍一個數量級。Composer 3 若兌現大概率延續這條路。
- **自評 bench 要打折**：Cursor 不公布 SWE-bench Verified，主推**私有、外部不可重現的 CursorBench** 自評自家模型——利益相反的裁判。等 Artificial Analysis 這類中立第三方測 Composer 3 再信。

## 和 Grok / xAI 的關係：整合是收購的核心目的，已在發生

Musk 同時控制 **SpaceX + xAI（Grok）**。收購掛 SpaceX 名下（IPO 後有兆級資產負債表付帳），戰略歸宿是 xAI 那疊：

- **算力**：Composer **2.5 早就在 xAI 的 Colossus（孟菲斯，22 萬張 GPU）上訓練**了，併購前就在跑。Composer 3 的「10 萬 GPU」就是 Colossus。
- **資料**：Musk 直說 **Cursor 的寫程式互動資料會餵進 Grok**，升級 Grok 的 coding 能力。
- **產品**：Composer 技術整合進 **Grok Build CLI**；Cursor 補上 xAI 缺的開發者產品面 + 企業通路。

垂直棧：**Colossus（算力）→ Grok/Composer（模型）→ Cursor（產品面）→ Origin（協作基板）**，整條去打 Anthropic / OpenAI 雙寡頭。等於 Musk 把 MSFT×OpenAI 的「平台×模型乘積」自己做一次。

## 「但模型和 xAI 沒關係？單純是 Cursor？」——到 2.5 為止，是

技術報告（上了 arXiv）白紙黑字：

- **底模 = Kimi K2.5**（中國開源 MoE，1.04T 總參 / 32B activated）。Cursor 做的是 **continued pretrain（加碼餵 code）+ 大規模 RL**。
- **正確拆法**：底模＝Kimi（不是 xAI）、研究/RL＝Cursor、算力＝xAI。**xAI 到 2.5 為止只貢獻 GPU，沒貢獻模型技術。**
- **轉折在 Composer 3**：那句「1.5T、從零、不靠 Kimi」會是 Cursor **第一次自己預訓練前沿底模**——恰恰是需要 Colossus + xAI 預訓練 know-how 的地方。**「純 Cursor」這條線從 Composer 3 開始糊掉。**
- **信號**：他們從誠實揭露「建在 Kimi 上」改口成「從零、不靠 Kimi」，**行銷跑在已揭露事實前面**，本身要警覺。

## 怎麼評估 Cursor 團隊的模型研究能力（可重用框架）

分清楚**證明過什麼 vs 沒證明過什麼**：

**已證明（強）：RL post-training + agentic 基建。**
- 硬證據：Kimi K2.5 裸底模在 CursorBench 只有 **36 分**，經 Cursor 兩階段訓練後 Composer 2 衝到 **61.3（+70%）**——這 70% 純是他們的 continued-pretrain + RL 加出來的。
- 基建真功夫：**Anyrun**（同時跑數十萬個沙箱 coding 環境）、跨區非同步 RL pipeline、Blackwell 自寫低精度 kernel。並 acqui-hire Supermaven（推論速度團隊）。
- 護城河＝**速度（MoE + 推論優化）+ 產品資料 RL 飛輪**，不是更強底模。

**未證明（存疑）：從零預訓練前沿底模。**
- 至今所有 Composer 都坐在別人的底模（Kimi）上。「1.5T 從零」是還沒兌現的跳躍，時機剛好撞上拿到 Colossus + Musk 預訓練組織。合理懷疑：Composer 3 是「Cursor 自己預訓練」還是「Colossus 上 xAI 重度參與、掛 Cursor 牌」？現在分不出。

**一句話**：Cursor 模型力**真實但偏科**——post-training / RL / agent-harness 層頂尖 + 推論速度，但**前沿預訓練未證明**。正中 harness>model：Cursor 優勢從來不是更好底模，是「**商品化開源底模之上做更好的 RL + harness + 產品迴圈**」。「從零」是想往下game 進預訓練層，未證明前保持懷疑。

**之後可驗證的具體信號**：
1. Composer 3 技術報告**會不會揭露底模**？避談＝「其實還建在某底模上」的 tell。
2. 成本/速度有沒有守住 10–60x 優勢（守住＝已證明強項延續）。
3. 研究人員是否與 xAI 合流（合流＝「Cursor 自己的模型」框架解體）。
4. 中立榜 vs 自家 CursorBench 的差距。

## 對我最該警覺的：中立 harness 被收編的 model-choice 風險

Cursor 今天賣點之一是**模型中立**（裡面可選 Claude、GPT）。併入 Musk 棧後理性預期是**偏袒 Composer/Grok、弱化 Anthropic/OpenAI 模型**——直撞 lock-in、harness>model、eval 中立性。Cursor 從「中立 harness」變「xAI 的自家 harness」。**真正的開放問題不是「會不會整合」（已整合），而是「整合後 Cursor 還讓不讓你爽用 Claude」。**

## Origin：「agent collab = git 不像 google doc」第一個落地產品

Origin＝為 AI agent（非人）重建的 Git forge：demo 22.6 commits/秒、29.6 萬 clones/小時、<400ms 全球同步，秋天上線。正中 `agent-collab-infra.md` 論點——**agent 協作單位是 PR/diff、像 git 不像 Google Doc**。22.6 commits/秒是「機器吞吐的 commit 才是協作單位」的具體化。

## 連結

- `topics/coding-agents/cards/harness-beats-model.md`（Cursor＝「商品底模 + 強 RL/harness」活教材，已補證據）
- `notes/agent-collab-infra.md`（Origin 是這條論點的落地）
- `notes/nadella-frontier-ecosystem.md`（Musk 版的平台×模型乘積）
- `topics/ai-industry-reading/cards/eval-is-a-cross-model-judge-layer.md`（自評 bench 要打折）

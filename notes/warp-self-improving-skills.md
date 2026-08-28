# Warp 的「自我改進 skill」迴圈（2026-08-28）

> 來源：使用者傳 Xudong Han 推文截圖（轉述 Anthropic 官方部落格《How Warp builds self-improving agents on Claude》），問「展開一下這是啥」。
> **證據降級聲明**：`claude.com` / `www.anthropic.com` / `www.warp.dev` 三個網域全被本環境 egress 白名單擋掉（EGRESS_BLOCKED），**本篇讀的是 WebSearch 摘要，不是原文**。且來源全為 Anthropic 官方部落格＋Warp 自家部落格＝**vendor 自報，無第三方複現、無量化結果**。

## 一句話

Warp 把「agent 學到的東西」寫成 **git 裡的一個 skill 檔**，再讓另一個**排程跑的 agent** 定期讀人類回饋、對那個檔案**提 PR**——學習的載體是版本控制的檔案，不是 prompt，也不是模型權重。

## 機制：兩層 skill，人夾在中間

1. **內層／base skill**：幹活的那個。PR 一開，code review agent 帶著這個 skill 跑，產出 review。skill ＝「file-based encodings of knowledge that keep instructions out of the raw prompt」。
2. **人給回饋**：在 PR 上直接留言就算，thumbs up 也算。原則是**捕捉在人本來就在的地方、零額外提交步驟**——「low friction is what keeps signal flowing」。
3. **外層／improver skill**：**每天跑一次**（on a schedule），不是每個任務跑一次。回頭掃當天所有 review，比對「agent 建議了什麼 vs 人實際怎麼回應」。
4. **提 PR**：若撈出值得記住的東西，開一個 PR，內容含「讀了哪些回饋／認為哪條原則該改／對 skill 檔的確切 diff」。人像審一般 code 一樣審。

已套用：code review、寫 spec、GitHub issue triage。

## 三個真正的設計選擇（要抄抄這三條）

**1. 學習寫進「有版本歷史、能 review、能 rollback」的地方**
原話大意：如果指令決定生產行為，它就該住在 repo 裡。這條讓「自我改進」不等於「失控」——agent 可以一直提改進，但 durable 的改動要過人審，團隊確保它不會歪掉。

**2. 寫原則，不寫規則**
「Construct the skill as though you're instructing a smart person, not like you're programming a computer.」
舉例：寫「找重複的程式碼」勝過窮舉一堆變數命名規則。**給了理由（rationale），agent 才能推理而不是照本宣科，才推廣得到沒見過的情況。**

**3. 回饋要說「為什麼錯」**
越明確越好，因為 improver 拿它當梯度。thumbs up 是下界，不是目標。

## 關鍵修正：那是兩條迴圈，不是一條

**我原本的預測**：這套會缺控制組（只驗「這次修好了」，不驗「原本對的還對」）。**半錯。**

Warp 另有一條 **benchmark／grader 驅動的 skill optimization loop**（自動評分器、比 baseline vs skill-on 的 delta、偵測 regression），與人類回饋迴圈是**兩條分開的迴圈**。

**但修正本身比預測值錢——兩條迴圈的閘門管的是不同東西**：

- 人類回饋迴圈，閘 ＝ **人審 diff** → 管**方向**（團隊偏好、什麼該記住）
- benchmark 迴圈，閘 ＝ **量測 delta** → 管**正確性**（有沒有改壞）

接 `topics/coding-agents/cards/correctness-gates-before-human-preference.md`（2026-08-18）：**正確性的檢查不能只掛在人的偏好後面**。Warp 把兩者拆成兩條而不是塞進同一條，方向是對的。

**歸屬存疑（篩子第四格）**：benchmark 迴圈「拒收 regression、還原上一個接受狀態」那段細節，搜尋摘要裡混進了社群 repo（`ChaoYue0307/awesome-loop-engineering`）的 pattern 文件，**未能確認是 Warp 自己的做法還是社群歸納**。原文被擋，未證。

## 對這個 repo（Issue #6）

**同一個 pattern 的第三次獨立出現**（≥3 ＝ CLAUDE.md 的升卡訊號）：
1. 2026-06-06 社群 pattern 掃描（`notes/recursive-harness-community-patterns.md`）
2. 2026-08-14 AgentX 的 Improvement Inbox（`notes/agentx-eval-loop.md`）
3. 2026-08-28 Warp（本篇）

**已經有的對應物**

- base skill ＝ `CLAUDE.md`
- 人類回饋 ＝ 使用者當場的修正，記進 `meta/defects.md` 的 `@user` 條目
- improver ＝ `/meta-review`
- PR 閘 ＝ commit + 使用者裁決；**R1「不准自評」比 Warp 這篇還嚴**（Warp 沒提自評偏誤，我們有實證背書的防護）

**Warp 有而我們沒有的，只有兩條**

- **A. improver 的觸發是排程，不是想到**。Warp 每日跑；我們 `/meta-review` 靠人想到才跑（至今 2 次：07-04、08-10）。與 AgentX「證據累積過閾值自動觸發」同構＝**第二次撞見同一條**。
- **B.「寫原則不寫規則」被當成寫作判準在用**。我們的 CLAUDE.md 正往規則清單方向長（261 行，R3 警戒線 200）。這條剛好是**刪規則的刀**——接北極星「能刪規則的 RSI 才是對的 RSI」。

兩條已寫成提案交使用者裁決，**未自行改 CLAUDE.md**（契約檔變更需共識）。具體提案見下節。

## 接手點：本地再跑一次要做的兩件事

> 2026-08-28 使用者：「紀錄到 learning 裡，我們在本地再搞一次」。以下是待裁決的兩條，本地 session 接手時直接從這裡開始，不必重讀原文（原文本來也擋著）。

### 提案 A：`/meta-review` 的觸發從「想到」改成「證據量」

**現況**：靠人想到才跑，至今 2 次（2026-07-04、2026-08-10），中間隔 5 週。`meta/defects.md` 日誌區 9 條中，**未消化 3 條**（2026-08-18 的 credibility-miss／retrieval-miss／write-conflict，上次 meta-review 是 08-10）＋本場新增 1 條 env-403 ＝ **4 條**。
**Warp 的做法**：每日排程。**AgentX 的做法**：證據累積過閾值自動生成提案。兩者都不靠「想到」。
**擬改**：boot 階段（已經在跑 `git log --since` 兜底了）多一個檢查——`meta/defects.md` 日誌區未消化條目 **≥5 條**就提示「該跑 `/meta-review` 了」。閾值待定。
**為什麼不直接照抄每日排程**：這個 repo 不是每天有 session，排程沒有意義；證據量才是對的計量單位。
**風險**：又加一條 boot 規則＝ CLAUDE.md 再長。**所以 A 要跟 B 綁在一起做**（加一刪多）。

### 提案 B：把「寫原則不寫規則」立為 CLAUDE.md 的**刪除判準**

**現況**：CLAUDE.md 261 行，R3 警戒線 200，兩次 meta-review 各砍了一點（290→268→261），砍的速度慢於長的速度。
**Warp 的話**：「像在指導一個聰明人，不是在對電腦編程」——給 rationale 讓 agent 推理，勝過窮舉規則。
**擬改**：`/meta-review` 的 SKILL.md 加一道檢查——**每輪至少找出一組「N 條規則可被 1 條原則取代」的候選並提案**。不是加一條寫作建議（那只會讓檔更長），是把它做成**每輪必跑的壓縮動作**。
**接**：北極星「能刪規則的 RSI 才是對的 RSI」；以及 `correctness-gates-before-human-preference` 的推論「**能機械化的就機械化，不能機械化的別寫成規則靠自律**」——後者正是「哪些規則該被刪掉換成原則」的篩子：靠自律執行的規則，多半就是該被壓成原則的那些。
**現成候選**（08-10 meta-review 已點名，未做）：檔案格式模板段（~40 行，擬抽 schema 檔留 pointer）、手機可讀性規則（收益有限，可否決）。

### 本地跑的時候順手驗一件事

Warp 那條「**回饋要說為什麼錯**」，我們 CLAUDE.md 已經有了（「連坑一起記」）。但**沒驗過它有沒有被執行**——去 `meta/defects.md` 抽查：有幾條真的寫了「原本以為 X、錯在哪、怎麼驗的」，有幾條只寫了結論？這是「規則寫了但沒人查」的典型，屬 B 的射程。

## 沒查到／待補

- 任何量化結果。全篇只有定性說法（「improve quality over time」）。
- improver 提的 PR **被採納率多少**、有沒有被人否決的比例。
- skill 檔會不會膨脹、他們怎麼刪東西（只看到「keep skills small」的說法，沒看到機制）。
- benchmark 迴圈與人類回饋迴圈**有沒有互相接上**（改 skill 後有沒有自動跑 benchmark 驗），還是各跑各的。

## 出處

- Anthropic／Claude 官方部落格：《How Warp builds self-improving agents on Claude》 https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude （egress 擋，未讀原文）
- 同場 webinar：https://www.anthropic.com/webinars/how-warp-builds-self-improving-agents-on-claude （擋）
- Warp 自家：《How to build a self-improvement loop for your Skills》 https://www.warp.dev/blog/self-improvement-loop-for-skills （擋）
- Warp 自家：《How to build a cloud software factory - self-improving code review》 https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-self-improving-code-review （擋）
- Warp 自家：《Building a skill optimization loop》 https://www.warp.dev/blog/building-a-skill-optimization-loop （擋）
- 轉述來源（二手）：Xudong Han 推文截圖，2026-08-28

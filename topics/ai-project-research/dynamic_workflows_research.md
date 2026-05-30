# Anthropic Dynamic Workflows 研究筆記

> 研究日期：2026-05-30　|　功能發布：2026-05-28（隨 Claude Opus 4.8，research preview）

## 一句話總結
Dynamic Workflows 是 Claude Code 的新功能：把「如何拆解與調度任務」的計畫從 Claude 的 context window 搬進一段 **Claude 自己即時寫出的 JavaScript 腳本**，由背景 runtime 執行，腳本再去調度大量 subagents 平行作業，最後只把結果交回對話，專治「一個對話塞不下」的大規模工程任務。

## 核心概念
1. **腳本即計畫（plan-as-code）**：傳統 subagents / skills 是 Claude 一回合一回合決定下一步，所有中間結果都堆在 context 裡。Workflow 把迴圈、分支、中間結果都放進腳本變數，Claude 的 context 只留最終答案 → 大幅省 context。
2. **大規模平行**：單次 run 最多 **1,000 個 agents**，同時最多 **16 個併發**（CPU 核心少會更低）。
3. **內建品質模式**：可以讓多個 agent 從不同角度獨立解題，再派對抗性 agent 互相反駁、交叉驗證，迭代到答案收斂——比單次 pass 更可信。
4. **背景執行、可續跑**：run 在背景跑，session 仍可用；同一 session 內可暫停 / 續跑（已完成的 agent 回傳快取結果）。但**離開 Claude Code 後再開，workflow 會從頭來**。
5. **ultracode**：一個新的 effort 等級，= `xhigh` reasoning + 自動 workflow 編排，開了之後每個實質任務 Claude 自己決定要不要起 workflow。

## 快速上手
需求：Claude Code **v2.1.154+**（本機 2.1.158 ✅）、Opus 4.8 等支援 `xhigh` 的模型。

```text
# 1. 最快體驗：內建的 deep-research workflow
/deep-research What changed in the Node.js permission model between v20 and v22?

# 2. 針對自己的任務臨時起一個 workflow —— prompt 裡帶 "workflow" 這個字即可
Run a workflow to audit every API endpoint under src/routes/ for missing auth checks

# 3. 讓 Claude 全程自動決定（整個 session 都升級）
/effort ultracode      # 回到日常工作用 /effort high 降回來

# 4. 監看 / 管理進行中的 run（看 phase、agent 數、token、可暫停 p / 停止 x）
/workflows

# 5. 滿意的 run 存成可重用指令：/workflows 選該 run → 按 s
#    存到 .claude/workflows/（專案共享）或 ~/.claude/workflows/（個人），日後變成 /<name>
```

關閉：`/config` 切掉、或 `settings.json` 加 `"disableWorkflows": true`、或環境變數 `CLAUDE_CODE_DISABLE_WORKFLOWS=1`。

## 優缺點
| | 內容 |
| :-- | :-- |
| 優點 | context 不爆（中間結果在腳本變數）、真正大規模平行（百~千 agents）、交叉驗證提高可信度、orchestration 可存檔重跑、背景執行不卡 session |
| 缺點 | **token 消耗顯著變多**（一次 run 可能遠超等量對話）、research preview 仍會變、run 中途無法插話（要分階段就拆成多個 workflow）、離開 session 不能續跑、腳本本身不能直接碰檔案/shell（要靠 agent） |

## 適用場景
**該用**：跨整個 codebase 的 bug / 安全稽核、500+ 檔案的大遷移或框架/語言改寫、需要多來源交叉查證的研究、答錯成本高、想先從多角度各自擬一版計畫再選的硬決策。官方招牌案例：Bun 從 Zig 改寫成 Rust，11 天 75 萬行、保住 99.8% 測試綠燈。

**別用**：單檔小修、一兩步就完成的任務、需要中途人工逐步確認的流程、想省 token 的日常雜活——這些用一般對話或 subagents 就好。

## 我們能用嗎？（針對 ting 的環境）
**技術上可以**：本機 Claude Code 2.1.158 ✅、已跑在 Opus 4.8 ✅，唯一變數是**訂閱方案**：
- **Max / Team**：預設開啟，直接能用。
- **Pro**：預設關，到 `/config` 的「Dynamic workflows」那列手動打開。
- **Enterprise**：預設關，需管理員開。
- 也支援 API / Bedrock / Vertex AI / Microsoft Foundry。

確認方式：直接在 Claude Code 打 `/config` 看有沒有「Dynamic workflows」列，或直接試 `/workflows`、`/deep-research`。
**務必注意成本**：side project 場景多半是小任務，多數時候用不到也不划算；真要用先拿一個 scoped 任務試水溫看 token 用量。

## 相關資源
- [官方文件：Orchestrate subagents at scale with dynamic workflows](https://code.claude.com/docs/en/workflows)
- [官方部落格：Introducing dynamic workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)
- [Claude Opus 4.8 發布公告](https://www.anthropic.com/news/claude-opus-4-8)

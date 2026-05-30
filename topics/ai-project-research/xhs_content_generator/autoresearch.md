# AutoResearch — Karpathy 的自動 ML 實驗框架

## 基本資訊
- GitHub: github.com/karpathy/autoresearch — 61,000+ stars
- 作者: Andrej Karpathy
- 發布: 2026-03-09
- 技術棧: Python + PyTorch (單 GPU)
- 授權: 開源

## 它解決什麼問題？

ML 研究中最耗時的是「試東西」— 改 hyperparameter、改架構、改 training trick。
AutoResearch 讓 AI agent 自動做這件事：修改代碼 → 訓練 5 分鐘 → 檢查結果 → 保留或丟棄 → 重複。

## 核心設計
- **Fixed time budget**: 每個實驗固定 5 分鐘 → 一小時 12 個實驗 → 一晚 ~100 個
- **Self-contained**: 只需 PyTorch，單 GPU，單文件
- **Code-driven**: 用 Markdown (program.md) 指導 AI agent，不直接改 Python
- **實際成果**: 2 天跑 700 個實驗，發現 20 個有效優化（包括新架構 trick）

## 我能 Build 嗎？

### 技術可行性：⭐⭐ (中等偏易)
- Python + PyTorch 我熟
- 核心邏輯不複雜：loop(修改代碼 → 跑實驗 → 評估 → 決策)
- 需要一張 GPU（本地或雲端）
- 難點：設計好 program.md 讓 agent 能有效探索

### 可能的切入角度
1. **直接用在自己的 ML 實驗上**：Fine-tuning、小模型訓練
2. **延伸到非 ML 場景**：AutoResearch for prompt engineering — 自動跑 prompt 變體實驗
3. **AutoResearch for trading strategy**: 自動測試交易策略變體
4. **做成服務**: 提供 GPU + AutoResearch 的 managed 版本

### 學到什麼
- AI 自主科研的 agent loop 設計
- 實驗管理和自動評估
- Karpathy 的工程思維

## 參考連結
- https://github.com/karpathy/autoresearch
- https://venturebeat.com/technology/andrej-karpathys-new-open-source-autoresearch-lets-you-run-hundreds-of-ai
- https://softmaxdata.com/blog/autoresearch/

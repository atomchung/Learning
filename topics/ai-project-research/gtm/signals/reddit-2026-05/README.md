# Reddit Signals — 2026 年 5 月

> 從 r/SideProject, r/indiehackers, r/SaaS, r/microsaas, r/EntrepreneurRideAlong, r/buildinpublic 各抓 top/month 50 篇，共 300 篇。

抓取時間：2026-05-21
方法：直接打 `reddit.com/r/{sub}/top.json?t=month&limit=50`

## 原始檔

| 檔 | 內容 |
|---|---|
| `*.json` | 完整 reddit API response |
| `*.txt` | 標題 + score + comments + 前 500 字 selftext |
| `deep_agensi.txt` | 篩選關鍵字 "Agensi / AI agent marketplace" 的完整 selftext |
| `deep_mobile_micro.txt` | 篩選 mobile app / micro SaaS / boring SaaS 完整 selftext |
| `deep_distribution.txt` | 篩選 distribution / first users / playbook 完整 selftext |

## 抓資料的指令（方便下次更新）

```bash
mkdir -p /tmp/reddit_indie && cd /tmp/reddit_indie
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ..."

for sub in SideProject indiehackers SaaS microsaas EntrepreneurRideAlong buildinpublic; do
  curl -s -A "$UA" "https://www.reddit.com/r/${sub}/top.json?t=month&limit=50" -o "${sub}.json"
done

# 抽欄位
for f in *.json; do
  jq -r '.data.children[] | .data |
    "### " + (.score|tostring) + "↑ " + (.num_comments|tostring) +
    "💬 | " + .title + "\n" + (.selftext | gsub("\n";" ") | .[0:500]) + "\n---"' \
    "$f" > "${f%.json}.txt"
done
```

## 收斂出的主要訊號

詳見 `../../README.md` 的 takeaway 段。簡版：

- **熱門專案類型**：AI 語音工具、Claude Code 周邊、NSFW 細分、諷刺型病毒專案、小而美 iOS app、B2B lead intent 工具
- **痛點**：distribution > product 是共識；vibe coding 後遺症（安全洞、技術債）；AI slop 評論氾濫
- **GTM 共通**：SEO + AEO 是現在最被低估的免費複利；Reddit 是 spark 不是 engine

## 後續計畫

- 每月 21 號重跑一次，與這次比對什麼新題、什麼題退潮
- 如果想加新 sub：r/ChatGPT, r/ClaudeAI, r/cursor, r/vibecoding, r/learnmachinelearning
- 中文圈版本：抓即刻 / V2EX / 少數派的同類社群（如果有 API）

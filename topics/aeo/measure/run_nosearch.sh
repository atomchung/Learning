#!/bin/zsh
# Ask one model one prompt with no tools (training knowledge only).
# Usage: run_nosearch.sh <prompt-id> <model-tag> <rep> <out-dir>
#   prompt-id: a file name in prompts/ without .txt (en, zh, cen, czh)
#   model-tag: opus | sonnet | haiku | codex | gemini | grok
# The model runs in a fresh empty directory outside any project, so it does not
# inherit a project's instructions or memory. See README.md for what else leaks.
set -u
KIT=${0:A:h}
P=$1; tag=$2; rep=$3; OUT=${4:A}
AGY=${AGY:-$HOME/.local/bin/agy}
EMPTY=$(mktemp -d)
[[ -f $KIT/prompts/$P.txt ]] || { echo "no prompt: prompts/$P.txt" >&2; exit 2; }
mkdir -p $OUT
prompt=$(cat $KIT/prompts/$P.txt)
o=$OUT/nosearch_${tag}_${P}_${rep}
cd $EMPTY
case $tag in
  opus|sonnet|haiku)
    claude -p "$prompt" --model claude-$tag-5-5 --output-format json \
      --tools "" --strict-mcp-config --setting-sources project --no-session-persistence \
      < /dev/null > $o.json 2> $o.err ;;
  codex)
    codex exec -m gpt-6-luna -c features.memories=false -c memories.use_memories=false \
      --sandbox read-only --ephemeral --skip-git-repo-check -C $EMPTY \
      -c model_reasoning_effort=medium -o $o.txt "$prompt" < /dev/null > $o.log 2> $o.err ;;
  gemini)
    $AGY -p "$prompt" --model gemini-3.8-flash --effort high --settings '{"agentMode":""}' \
      --output-format json > $o.json 2> $o.err ;;
  grok)
    grok --prompt-file $KIT/prompts/$P.txt --permission-mode dontAsk --deny '*' \
      --disable-web-search --no-subagents --cwd $EMPTY --model grok-4.6 \
      --output-format json > $o.json 2> $o.err ;;
  *) echo "unknown model tag: $tag" >&2; exit 2 ;;
esac
echo "done $tag $P $rep exit=$?"

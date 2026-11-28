#!/bin/zsh
# Ask one model one prompt with web search allowed.
# Usage: run_search.sh <prompt-id> <model-tag> <rep> <out-dir>
#   prompt-id: sen, szh, csen, cszh (these prompts ask for a SOURCES list)
#   model-tag: sonnet | opus | codex | gemini | grok
set -u
KIT=${0:A:h}
P=$1; tag=$2; rep=$3; OUT=${4:A}
AGY=${AGY:-$HOME/.local/bin/agy}
EMPTY=$(mktemp -d)
[[ -f $KIT/prompts/$P.txt ]] || { echo "no prompt: prompts/$P.txt" >&2; exit 2; }
mkdir -p $OUT
prompt=$(cat $KIT/prompts/$P.txt)
o=$OUT/search_${tag}_${P}_${rep}
cd $EMPTY
case $tag in
  sonnet|opus)
    claude -p "$prompt" --model claude-$tag-5-5 --output-format json \
      --tools "WebSearch,WebFetch" --strict-mcp-config --setting-sources project \
      --permission-mode bypassPermissions --max-turns 20 --no-session-persistence \
      < /dev/null > $o.json 2> $o.err ;;
  codex)
    # --search must come before the exec subcommand.
    codex --search exec -m gpt-6-luna -c features.memories=false -c memories.use_memories=false \
      --sandbox read-only --ephemeral --skip-git-repo-check -C $EMPTY \
      -c model_reasoning_effort=medium --json -o $o.txt "$prompt" < /dev/null > $o.jsonl 2> $o.err ;;
  gemini)
    $AGY -p "$prompt Use only search_web; run no shell command, write no file, open no browser, and report each link as search_web returned it." \
      --model gemini-3.8-flash --effort high --settings '{"agentMode":""}' \
      --output-format json > $o.json 2> $o.err ;;
  grok)
    grok --prompt-file $KIT/prompts/$P.txt --permission-mode dontAsk --deny '*' \
      --no-subagents --cwd $EMPTY --model grok-4.6 --output-format json > $o.json 2> $o.err ;;
  *) echo "unknown model tag: $tag" >&2; exit 2 ;;
esac
echo "done $tag $P $rep exit=$?"

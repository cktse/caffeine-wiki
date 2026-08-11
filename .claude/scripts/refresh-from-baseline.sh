#!/usr/bin/env bash
#
# refresh-from-baseline.sh — pull the core session-infra scripts from the
# upstream baseline (llm-wiki-template) into this instance.
#
# Layouts differ (this instance forked the baseline before its multi-platform
# restructure), so we copy explicit files by path rather than a folder checkout:
#     baseline:  scripts/<name>
#     instance:  .claude/scripts/<name>
#
# Only the four CORE scripts are synced (Class-1 infra). Everything else —
# including this script and CLAUDE.md — stays instance-local.
#
set -euo pipefail

CORE=(export-session.py index-sessions.sh recall.sh sweep-sessions.py)

cd "$(git rev-parse --show-toplevel)"

echo "Fetching upstream…"
git fetch -q upstream

for f in "${CORE[@]}"; do
  git show "upstream/main:scripts/$f" > ".claude/scripts/$f"
  echo "  ✓ .claude/scripts/$f"
done

echo
echo "Synced ${#CORE[@]} core scripts: upstream/main:scripts/ → .claude/scripts/"
echo "Review with:  git diff -- .claude/scripts/   then commit if good."

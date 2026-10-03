#!/bin/sh
# Keep runtime roots local. Zero/Stow may link each managed skill directory.
set -eu

if [ "$#" -gt 1 ]; then
  printf '%s\n' 'usage: 10-codex-directories.sh [target-home]' >&2
  exit 2
fi
codex_target_home="${1:-$HOME}"
for codex_relative_dir in .codex .codex/skills .agents .agents/skills; do
  codex_target_dir="$codex_target_home/$codex_relative_dir"
  if [ -L "$codex_target_dir" ]; then
    printf 'Expected a local directory, found a symlink: %s\n' "$codex_target_dir" >&2
    exit 1
  fi
  mkdir -p "$codex_target_dir"
done

#!/usr/bin/env bash
set -euo pipefail

# Install the bundled skill into a Codex user directory or a repository.
scriptDir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
sourceDir="$scriptDir/data-storytelling"

if [[ ! -f "$sourceDir/SKILL.md" ]]; then
  printf 'Error: data-storytelling/SKILL.md is missing.\n' >&2
  exit 1
fi

if [[ $# -eq 0 || "${1:-}" == "--user" ]]; then
  baseDir="${CODEX_HOME:-$HOME/.codex}/skills"
elif [[ "$1" == "--repo" && $# -eq 2 ]]; then
  baseDir="${2%/}/.agents/skills"
else
  printf 'Usage: %s [--user | --repo /path/to/repository]\n' "$0" >&2
  exit 2
fi

installDir="$baseDir/data-storytelling"

# Refuse to replace an existing skill; never generate backup files.
if [[ -e "$installDir" || -L "$installDir" ]]; then
  printf 'Error: destination already exists: %s\n' "$installDir" >&2
  exit 1
fi

mkdir -p "$baseDir"
cp -R "$sourceDir" "$installDir"
printf 'Installed data-storytelling at %s\n' "$installDir"

#!/usr/bin/env bash
set -euo pipefail

# Install or explicitly replace the standalone data-storytelling skill.
scriptDir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
sourceDir="$scriptDir/data-storytelling"
baseDir=""
replaceExisting=false
mode=""

# Parse one destination and an optional explicit replacement flag.
while (( $# > 0 )); do
  case "$1" in
    --user)
      [[ -z "$mode" ]] || { printf 'Specify only one installation mode.\n' >&2; exit 2; }
      baseDir="$HOME/.agents/skills"
      mode=user
      shift
      ;;
    --repo)
      [[ -z "$mode" && $# -ge 2 && -n "$2" && "$2" != --* ]] || { printf 'Usage: --repo /path/to/project\n' >&2; exit 2; }
      baseDir="${2%/}/.agents/skills"
      mode=repo
      shift 2
      ;;
    --legacy-codex)
      [[ -z "$mode" ]] || { printf 'Specify only one installation mode.\n' >&2; exit 2; }
      baseDir="${CODEX_HOME:-$HOME/.codex}/skills"
      mode=legacy
      shift
      ;;
    --replace)
      replaceExisting=true
      shift
      ;;
    *)
      printf 'Usage: %s [--user | --repo PATH | --legacy-codex] [--replace]\n' "$0" >&2
      exit 2
      ;;
  esac
done

# Resolve the user path by default, matching current local skill documentation.
if [[ -z "$mode" ]]; then
  baseDir="$HOME/.agents/skills"
fi

# Verify that the packaged source matches the exact skill intended for installation.
if [[ ! -f "$sourceDir/SKILL.md" ]] || ! grep -qx 'name: data-storytelling' "$sourceDir/SKILL.md"; then
  printf 'Invalid skill source or unexpected skill name.\n' >&2
  exit 1
fi

installDir="$baseDir/data-storytelling"
if [[ -L "$installDir" ]]; then
  printf 'Refusing to replace a symlink: %s\n' "$installDir" >&2
  exit 1
fi
if [[ -e "$installDir" ]]; then
  if [[ "$replaceExisting" != true ]]; then
    printf 'Destination exists: %s (use --replace explicitly).\n' "$installDir" >&2
    exit 1
  fi
  if [[ ! -f "$installDir/SKILL.md" ]] || ! grep -qx 'name: data-storytelling' "$installDir/SKILL.md"; then
    printf 'Refusing to replace a directory without the expected skill identity.\n' >&2
    exit 1
  fi
fi

# Stage a complete copy before touching any previously installed version.
mkdir -p "$baseDir"
stagingDir="$(mktemp -d "$baseDir/.data-storytelling-stage.XXXXXXXX")"
cleanup() {
  if [[ -n "${stagingDir:-}" && -d "$stagingDir" ]]; then
    rm -rf -- "$stagingDir"
  fi
  return 0
}
trap cleanup EXIT
cp -R "$sourceDir/." "$stagingDir/"
[[ -f "$stagingDir/references/HOW_TO_STORYTELLING.md" ]] || { printf 'Staging failed.\n' >&2; exit 1; }

# Only an explicit replacement can remove the existing skill; no backups are made.
if [[ -e "$installDir" ]]; then
  rm -rf -- "$installDir"
fi
mv -- "$stagingDir" "$installDir"
stagingDir=""
printf 'Installed data-storytelling v0.2 at %s\n' "$installDir"

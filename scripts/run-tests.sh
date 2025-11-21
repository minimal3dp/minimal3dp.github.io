#!/usr/bin/env bash
# Minimal 3DP test/validation runner
# Purpose: Provide a single entry point to validate data fetch scripts and build the site.
# Usage examples:
#   ./scripts/run-tests.sh                # run all checks
#   ./scripts/run-tests.sh ga4 youtube    # run only GA4 + YouTube fetch tests
#   ./scripts/run-tests.sh build          # run hugo build only
#   ./scripts/run-tests.sh --skip-fetch   # build without fetch scripts
# Environment variables (optional):
#   GA4_SERVICE_ACCOUNT_FILE  Path to service account JSON for GA4 (preferred)
#   GA4_SERVICE_ACCOUNT_B64   Base64 encoded service account JSON (alternative)
#   YOUTUBE_API_KEY           YouTube Data API key (required for youtube test)
#   YOUTUBE_CHANNEL_ID        Channel ID (required for youtube test)
# Exit codes:
#   0 success, non-zero indicates failure in one of the stages.

set -euo pipefail
IFS=$'\n\t'

# Colors
BOLD="\033[1m"; RED="\033[31m"; GREEN="\033[32m"; YELLOW="\033[33m"; RESET="\033[0m"

log() { printf "%b\n" "$1"; }
info() { log "${BOLD}$1${RESET}"; }
ok() { log "${GREEN}$1${RESET}"; }
warn() { log "${YELLOW}$1${RESET}"; }
err() { log "${RED}$1${RESET}"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

# Parse args
REQUESTED=()
SKIP_FETCH=0
for arg in "$@"; do
  case "$arg" in
    --skip-fetch) SKIP_FETCH=1 ;;
    ga4|youtube|build) REQUESTED+=("$arg") ;;
    -h|--help) sed -n '1,60p' "$0"; exit 0 ;;
    *) err "Unknown argument: $arg"; exit 2 ;;
  esac
done

if [ ${#REQUESTED[@]} -eq 0 ]; then
  REQUESTED=(ga4 youtube build)
fi

check_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    err "Required command '$1' not found. Install first."; exit 3
  fi
}

check_cmd "uv"
check_cmd "hugo"

# Ensure Python deps are installed
info "Syncing Python dependencies (uv sync)";
uv sync >/dev/null 2>&1 || { err "uv sync failed"; exit 4; }
ok "Dependencies synced"

GA4_TMP_JSON=""
prepare_ga4_credentials() {
  if [ -n "${GA4_SERVICE_ACCOUNT_FILE:-}" ] && [ -f "$GA4_SERVICE_ACCOUNT_FILE" ]; then
    GA4_TMP_JSON="$GA4_SERVICE_ACCOUNT_FILE"
    return 0
  fi
  if [ -n "${GA4_SERVICE_ACCOUNT_B64:-}" ]; then
    GA4_TMP_JSON="$(mktemp /tmp/ga4-XXXXXXXX.json)"
    echo "$GA4_SERVICE_ACCOUNT_B64" | base64 --decode > "$GA4_TMP_JSON" || { err "Failed to decode GA4_SERVICE_ACCOUNT_B64"; return 1; }
    return 0
  fi
  warn "GA4 credentials not provided; skipping GA4 fetch test"
  return 2
}

run_ga4() {
  info "Running GA4 popularity fetch script"
  if ! prepare_ga4_credentials; then
    warn "Skipping GA4 test due to missing credentials"; return 0
  fi
  GOOGLE_APPLICATION_CREDENTIALS="$GA4_TMP_JSON" uv run python scripts/fetch_ga4_popular.py || { err "GA4 fetch script failed"; return 1; }
  # Basic validation
  if [ ! -s "data/popular.json" ]; then err "popular.json missing or empty"; return 1; fi
  ok "GA4 fetch succeeded"
}

run_youtube() {
  info "Running YouTube popularity fetch script"
  if [ -z "${YOUTUBE_API_KEY:-}" ] || [ -z "${YOUTUBE_CHANNEL_ID:-}" ]; then
    warn "Missing YOUTUBE_API_KEY or YOUTUBE_CHANNEL_ID; skipping YouTube test"
    return 0
  fi
  YOUTUBE_API_KEY="$YOUTUBE_API_KEY" YOUTUBE_CHANNEL_ID="$YOUTUBE_CHANNEL_ID" uv run python scripts/fetch_youtube_popular.py || { err "YouTube fetch script failed"; return 1; }
  if [ ! -s "data/youtube_popular.json" ]; then err "youtube_popular.json missing or empty"; return 1; fi
  ok "YouTube fetch succeeded"
}

run_build() {
  info "Building Hugo site (production minify)"
  hugo --minify >/dev/null 2>&1 || { err "Hugo build failed"; return 1; }
  # Check a few expected outputs
  for f in public/index.html public/sitemap.xml; do
    if [ ! -s "$f" ]; then err "Expected output $f missing"; return 1; fi
  done
  ok "Hugo build succeeded"
}

FAILED=0

for task in "${REQUESTED[@]}"; do
  case "$task" in
    ga4)
      if [ $SKIP_FETCH -eq 1 ]; then warn "Skipping GA4 due to --skip-fetch"; continue; fi
      run_ga4 || FAILED=1 ;;
    youtube)
      if [ $SKIP_FETCH -eq 1 ]; then warn "Skipping YouTube due to --skip-fetch"; continue; fi
      run_youtube || FAILED=1 ;;
    build)
      run_build || FAILED=1 ;;
  esac
done

if [ $FAILED -eq 0 ]; then
  ok "All requested tasks completed successfully"
else
  err "One or more tasks failed"
fi

exit $FAILED

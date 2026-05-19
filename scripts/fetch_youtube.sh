#!/usr/bin/env bash
# Download auto-generated subtitles/transcript for a YouTube video using yt-dlp.
# Usage: bash fetch_youtube.sh <YouTube_URL>

set -euo pipefail

URL="${1:-}"
if [[ -z "$URL" ]]; then
  echo "Usage: $0 <YouTube_URL>" >&2
  exit 1
fi

OUTPUT_DIR="$(dirname "$0")/../research/youtube-transcripts"
mkdir -p "$OUTPUT_DIR"

echo "Fetching transcript for: $URL"
yt-dlp \
  --skip-download \
  --write-auto-sub \
  --sub-lang en \
  --sub-format vtt \
  --output "$OUTPUT_DIR/%(upload_date)s-%(title)s.%(ext)s" \
  "$URL"

echo "Done. Transcripts saved to $OUTPUT_DIR"

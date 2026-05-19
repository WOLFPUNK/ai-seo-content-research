#!/bin/bash
# Usage: ./scripts/fetch_youtube.sh "VIDEO_URL" "author-slug" "video-slug"
set -e
VIDEO_URL=$1; AUTHOR=$2; SLUG=$3

if [ -z "$VIDEO_URL" ] || [ -z "$AUTHOR" ] || [ -z "$SLUG" ]; then
  echo "Usage: $0 VIDEO_URL author-slug video-slug"
  exit 1
fi

OUTDIR="research/youtube-transcripts/$AUTHOR"
mkdir -p "$OUTDIR"

yt-dlp \
  --write-auto-sub \
  --write-sub \
  --sub-lang en \
  --skip-download \
  --convert-subs srt \
  --no-check-certificate \
  -o "$OUTDIR/$SLUG.%(ext)s" \
  "$VIDEO_URL"

echo "✅ Saved transcript for $AUTHOR / $SLUG"

#!/usr/bin/env python3
"""
Convert raw .vtt transcript files in research/youtube-transcripts/ into clean
plain-text .txt files, stripping timestamps and deduplicating repeated lines.
"""

import re
import sys
from pathlib import Path

TRANSCRIPT_DIR = Path(__file__).parent.parent / "research" / "youtube-transcripts"


def clean_vtt(text: str) -> str:
    # Drop WEBVTT header and NOTE blocks
    text = re.sub(r"WEBVTT.*?\n", "", text)
    text = re.sub(r"NOTE\s.*?\n\n", "", text, flags=re.DOTALL)
    # Drop timestamp lines (00:00:00.000 --> 00:00:00.000 ...)
    text = re.sub(r"\d{2}:\d{2}:\d{2}\.\d{3} --> .*\n", "", text)
    # Drop sequence numbers standing alone on a line
    text = re.sub(r"^\d+\s*$", "", text, flags=re.MULTILINE)
    # Strip inline tags like <00:00:01.000><c>word</c>
    text = re.sub(r"<[^>]+>", "", text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    # Deduplicate consecutive identical lines (common in auto-captions)
    deduped = [lines[0]] if lines else []
    for line in lines[1:]:
        if line != deduped[-1]:
            deduped.append(line)
    return "\n".join(deduped)


def main() -> None:
    vtt_files = list(TRANSCRIPT_DIR.glob("*.vtt"))
    if not vtt_files:
        print(f"No .vtt files found in {TRANSCRIPT_DIR}")
        sys.exit(0)

    for vtt_path in sorted(vtt_files):
        out_path = vtt_path.with_suffix(".txt")
        if out_path.exists():
            print(f"Skipping (already cleaned): {out_path.name}")
            continue
        raw = vtt_path.read_text(encoding="utf-8", errors="replace")
        cleaned = clean_vtt(raw)
        out_path.write_text(cleaned, encoding="utf-8")
        print(f"Cleaned: {vtt_path.name} -> {out_path.name}")


if __name__ == "__main__":
    main()

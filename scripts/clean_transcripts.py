"""Convert all .srt files in research/youtube-transcripts/ to clean .md."""
import re
from pathlib import Path

def srt_to_text(srt_path: Path) -> str:
    text = srt_path.read_text(encoding="utf-8")
    lines = []
    for line in text.split("\n"):
        line = line.strip()
        if not line or re.match(r"^\d+$", line) or "-->" in line:
            continue
        line = re.sub(r"<[^>]+>", "", line)
        lines.append(line)
    return " ".join(lines)

for srt in Path("research/youtube-transcripts").rglob("*.srt"):
    md_path = srt.with_suffix(".md")
    title = srt.stem.replace("-", " ").title()
    body = srt_to_text(srt)
    md_path.write_text(
        f"---\nsource: youtube\nfile: {srt.stem}\n---\n\n# {title}\n\n{body}\n"
    )
    print(f"✅ Cleaned: {md_path}")

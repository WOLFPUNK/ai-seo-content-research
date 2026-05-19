# AI SEO Content Research

A structured research repository for AI-assisted SEO content strategy, including source collection, synthesis, and search indexing tools.

## Structure

```
ai-seo-content-research/
├── research/
│   ├── sources.md               # Tracked sources and references
│   ├── synthesis.md             # Synthesized insights and findings
│   ├── ANNOTATION_TEMPLATE.md   # Template for annotating new sources
│   ├── linkedin-posts/          # Saved LinkedIn content
│   ├── youtube-transcripts/     # Raw and cleaned YouTube transcripts
│   └── other/                   # Miscellaneous research materials
└── scripts/
    ├── fetch_youtube.sh         # Download YouTube transcripts via yt-dlp
    ├── clean_transcripts.py     # Normalize and clean raw transcripts
    └── build_search_index.py    # Build a local full-text search index
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

### Fetch a YouTube transcript

```bash
bash scripts/fetch_youtube.sh <YouTube_URL>
```

### Clean transcripts

```bash
python scripts/clean_transcripts.py
```

### Build search index

```bash
python scripts/build_search_index.py
```

## Research Workflow

1. Add new sources to `research/sources.md`.
2. Use `ANNOTATION_TEMPLATE.md` to annotate each source in its subfolder.
3. Run `fetch_youtube.sh` to pull transcripts into `youtube-transcripts/`.
4. Run `clean_transcripts.py` to normalize the raw text.
5. Run `build_search_index.py` to make all content searchable.
6. Update `synthesis.md` with key insights.

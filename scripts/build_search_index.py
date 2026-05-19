#!/usr/bin/env python3
"""
Build a Whoosh full-text search index over all Markdown and text files
in the research/ directory.

Run:  python scripts/build_search_index.py
Search: python scripts/build_search_index.py --query "your search terms"
"""

import argparse
import sys
from pathlib import Path

try:
    from whoosh import index
    from whoosh.fields import ID, TEXT, Schema
    from whoosh.qparser import QueryParser
except ImportError:
    sys.exit("whoosh is not installed. Run: pip install whoosh")

RESEARCH_DIR = Path(__file__).parent.parent / "research"
INDEX_DIR = Path(__file__).parent.parent / "index"
EXTENSIONS = {".md", ".txt"}

SCHEMA = Schema(
    path=ID(stored=True, unique=True),
    content=TEXT(stored=True),
)


def build_index() -> None:
    INDEX_DIR.mkdir(exist_ok=True)
    if index.exists_in(str(INDEX_DIR)):
        ix = index.open_dir(str(INDEX_DIR))
    else:
        ix = index.create_in(str(INDEX_DIR), SCHEMA)

    writer = ix.writer()
    files = [p for p in RESEARCH_DIR.rglob("*") if p.suffix in EXTENSIONS and p.is_file()]
    for f in sorted(files):
        text = f.read_text(encoding="utf-8", errors="replace")
        writer.update_document(path=str(f.relative_to(RESEARCH_DIR)), content=text)
        print(f"Indexed: {f.relative_to(RESEARCH_DIR)}")
    writer.commit()
    print(f"\nIndex built at {INDEX_DIR} ({len(files)} documents)")


def search_index(query_str: str) -> None:
    if not index.exists_in(str(INDEX_DIR)):
        sys.exit("No index found. Run without --query first to build it.")
    ix = index.open_dir(str(INDEX_DIR))
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query, limit=20)
        if not results:
            print("No results found.")
            return
        for hit in results:
            print(f"\n[score {hit.score:.2f}] {hit['path']}")
            print(hit.highlights("content") or "(no excerpt)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build or query the research search index.")
    parser.add_argument("--query", "-q", help="Search query string")
    args = parser.parse_args()

    if args.query:
        search_index(args.query)
    else:
        build_index()


if __name__ == "__main__":
    main()

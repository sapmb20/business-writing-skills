#!/usr/bin/env python3
"""Find word runs that a repo shares verbatim with a source text (a copy check).

Usage:
    python3 tools/shingle.py SOURCE REPO [-n 10] [--exclude GLOB ...] [--show]

SOURCE is either a JSON file shaped {id: {"text": str, "asides": [str, ...]}} (the format
merge.py writes) or a directory of .txt files. Every Markdown and YAML file under REPO is
split into overlapping runs of n words ("shingles"), case- and punctuation-insensitive, and
compared against the source. Prints the count of shared shingles per file, and the shingles
themselves with --show. Exits 1 if any are found.

A shared 10-word run is almost never chance, so treat every 10-word hit as copied text to
rewrite. At 8 words, expect some common phrases; review each hit by hand. Use --exclude for
files that quote an openly licensed source on purpose (adopted templates).
"""
import argparse
import fnmatch
import json
import pathlib
import re
import sys


def words(text):
    return re.findall(r"[a-z0-9']+", text.lower().replace("’", "'"))


def shingles(text, n):
    w = words(text)
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def load_source(path):
    p = pathlib.Path(path)
    if p.is_dir():
        return [f.read_text(errors="replace") for f in sorted(p.rglob("*.txt"))]
    data = json.loads(p.read_text())
    return [e["text"] + " " + " ".join(e.get("asides", [])) for e in data.values()]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("repo")
    ap.add_argument("-n", type=int, default=10)
    ap.add_argument("--exclude", nargs="*", default=[])
    ap.add_argument("--show", action="store_true")
    a = ap.parse_args()
    src = set()
    for t in load_source(a.source):
        src |= shingles(t, a.n)
    root = pathlib.Path(a.repo)
    total = 0
    for f in sorted(root.rglob("*")):
        rel = str(f.relative_to(root))
        if ".git" in f.parts or f.suffix not in {".md", ".yaml", ".yml"}:
            continue
        if any(fnmatch.fnmatch(rel, g) for g in a.exclude):
            continue
        hits = sorted(shingles(f.read_text(errors="replace"), a.n) & src)
        if hits:
            total += len(hits)
            print(f"{len(hits):4d}  {rel}")
            if a.show:
                for h in hits:
                    print("        " + h)
    print(f"{total} shared {a.n}-word shingles")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()

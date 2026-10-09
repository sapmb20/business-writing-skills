#!/usr/bin/env python3
"""Merge captured source batches into one entries file.

Usage:
    python3 tools/merge.py RAW_DIR OUT_JSON

RAW_DIR holds JSON batches, each shaped {key: {"h2": str, "loc": any, "text": str,
"asides": [str], "caps": [str]}}, however you captured them (a reader export, a scrape of
a source you are licensed to read, your own notes). Entries are keyed by a slug of their
heading; when the same heading appears twice, the longer text wins. Writes OUT_JSON in the
shape coverage.py, index_check.py, and shingle.py read.

Capture only material you have the right to process, and never commit it: the source text
stays local, and only the results of the checks belong in a repo.
"""
import glob
import json
import os
import re
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    raw, out_path = sys.argv[1], sys.argv[2]
    out = {}
    for f in sorted(glob.glob(os.path.join(raw, "*.json"))):
        for e in json.load(open(f)).values():
            h = (e.get("h2") or "").strip() or e["text"].strip().split("\n")[0][:60]
            slug = re.sub(r"[^a-z0-9]+", "-", h.lower()).strip("-")
            if slug in out and len(out[slug]["text"]) >= len(e["text"]):
                continue
            out[slug] = {"h2": h, "loc": e.get("loc"), "text": e["text"],
                         "asides": e.get("asides", []), "caps": e.get("caps", [])}
    json.dump(out, open(out_path, "w"))
    print(len(out), "entries;", sum(len(e["asides"]) for e in out.values()), "asides")


if __name__ == "__main__":
    main()

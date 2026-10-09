#!/usr/bin/env python3
"""Check a source's back-of-book index against a skill family.

Usage:
    python3 tools/index_check.py INDEX_JSON REPO OUT_CSV [--allow allow.tsv]

INDEX_JSON is a list of headwords, each {"t": "headword, 12-14", "subs": ["sub-entry, 13",
...]}. For every sub-entry (skipping "see" cross-references), the check passes when the
headword's keywords and at least half of the sub-entry's own keywords occur in one file of
REPO/skills. An index lists what its book treats as findable, so this catches topics a
line-by-line check can miss.

Writes the misses to OUT_CSV (headword, sub-entry, best score, best file) and prints the
totals. Triage each miss: a real gap to write, or a row in --allow
(`headword <TAB> sub-entry <TAB> reason`).
"""
import argparse
import csv
import glob
import json
import os
import re

STOP = set("""the a an and or of to in on for with by as at from that this is are be it its into than about between
use used using writer writers checklist checklists general guidelines types example examples see also other sample
samples functions""".split())


def stem(w):
    w = w.lower()
    for suf in ("ations", "ation", "ments", "ment", "ings", "ing", "ies", "ers", "es", "ed", "er", "s"):
        if len(w) - len(suf) >= 3 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def kws(t):
    t = re.sub(r"[\d–-]+(,|$)", " ", t)
    return [stem(w) for w in re.findall(r"[A-Za-zé][A-Za-zé'’]+", t) if w.lower() not in STOP and len(w) >= 3]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("index")
    ap.add_argument("repo")
    ap.add_argument("out")
    ap.add_argument("--allow")
    a = ap.parse_args()

    files = {os.path.relpath(p, a.repo): set(stem(w) for w in re.findall(r"[A-Za-zé][A-Za-zé'’]+", open(p).read()))
             for p in glob.glob(os.path.join(a.repo, "skills", "**", "*.md"), recursive=True)}
    allow = set()
    if a.allow and os.path.exists(a.allow):
        for row in open(a.allow):
            if row.strip() and not row.startswith("#"):
                allow.add(tuple(row.rstrip("\n").split("\t")[:2]))

    rows, n = [], 0
    for e in json.load(open(a.index)):
        head = re.split(r",\s*\d", e["t"])[0].strip()
        hk = kws(head)
        for s in e["subs"]:
            if s.lower().startswith("see ") or "see also" in s.lower():
                continue
            n += 1
            sub = re.split(r",\s*\d", s)[0].strip()
            sk = [w for w in kws(sub) if w not in hk]
            best, bf = 0.0, ""
            for f, v in files.items():
                hok = all(w in v for w in hk) if len(hk) <= 2 else sum(w in v for w in hk) >= len(hk) / 2
                if hok:
                    r = sum(w in v for w in sk) / len(sk) if sk else 1.0
                    if r > best:
                        best, bf = r, f
            if best < 0.5 and (head, sub) not in allow:
                rows.append([head, sub, f"{best:.2f}", bf])

    with open(a.out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["headword", "sub", "best", "file"])
        w.writerows(rows)
    print(f"sub-entries {n}  misses {len(rows)}")


if __name__ == "__main__":
    main()

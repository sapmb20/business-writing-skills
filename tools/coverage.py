#!/usr/bin/env python3
"""Check, rule by rule, how much of a source a skill family covers.

Usage:
    python3 tools/coverage.py ENTRIES_JSON REPO OUT_DIR [--allow allow.tsv] [--gloss glossary.md]

ENTRIES_JSON is the file merge.py writes. Each entry is split into rule units (sentences of
six or more words, skipping example lines, sample-document lines, and labels such as
"Wordy:" or "Revised:"). A unit counts as covered when at least half of its rare keywords
(words that appear in few entries) co-occur in a single file of the repo. That is a
keyword test, not a meaning test, so read the misses: each is either a real gap to write,
or a unit to allowlist with a reason.

Writes OUT_DIR/coverage.csv (one row per entry: units, covered, percent, the skills that
cover it) and OUT_DIR/uncovered/<entry>.txt with the missed units. Prints the totals.

--allow:  a TSV of `entry-slug <TAB> unit-prefix-or-* <TAB> reason`, for units you checked
          and decided not to cover (out of scope, superseded, covered in other words).
--gloss:  a Markdown file whose table rows list word pairs ("affect / effect"); short
          usage entries whose headword pair appears there count as covered.
"""
import argparse
import csv
import glob
import json
import os
import re
from collections import Counter, defaultdict

STOP = set("""the a an and or but of to in on for with by as at from that this these those is are was were be been
being it its into than then there their they them you your yours our we he she his her not no can could should would
will may might must do does did have has had which who whom whose what when where why how all any each some such more
most other also only very just about over under if so because while however although though between both either neither
one two three use used using uses example examples e.g i.e see also figure entry page pages make makes made like same
own well many much often usually always never even way ways""".split())
DROP = re.compile(r"^(see also|see |directory|figure|figures|▶|➤|►|wrong|right|incorrect|correct|weak|improved|"
                  r"wordy|concise|vague|specific|change|to:|passive|active|unclear|clear|original|revised|"
                  r"biased|unbiased|ambiguous|informal|formal|jargon|plain|stuffy|natural|ineffective|effective)\b",
                  re.I)
MODEL = re.compile(r"(\b(I|I'm|I've|my|we|We|our|Our|us|me)\b|^(To|From|Subject|Date|cc|Re|Dear)\b:?|"
                   r"Sincerely|Best regards)")
EXLINE = re.compile(r"(^[A-Z]{3,}(\s+[A-Z]{2,})*\b(?![a-z])|\]\s*$|^\(?[a-z]\)|^.{0,80}\[[^\]]+\]\s*$)")


def stem(w):
    w = w.lower()
    for suf in ("ization", "ations", "ation", "ments", "ment", "ings", "ing", "ness", "edly", "ies", "ied", "ers",
                "ly", "es", "ed", "er", "s"):
        if len(w) - len(suf) >= 4 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def words(t):
    return [stem(w) for w in re.findall(r"[A-Za-z][A-Za-z'-]+", t) if w.lower() not in STOP and len(w) >= 4]


def units(e):
    out, lines = [], e["text"].split("\n")[1:]
    for a in e.get("asides", []):
        lines += a.split("\n")
    for ln in (x.strip() for x in lines):
        if len(ln.split()) < 6 or DROP.match(ln) or MODEL.search(ln) or EXLINE.search(ln):
            continue
        out += [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", ln) if len(s.split()) >= 6]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entries")
    ap.add_argument("repo")
    ap.add_argument("out")
    ap.add_argument("--allow")
    ap.add_argument("--gloss")
    a = ap.parse_args()

    entries = json.load(open(a.entries))
    df = Counter()
    for e in entries.values():
        df.update(set(words(e["text"] + " ".join(e.get("asides", [])))))
    files = {os.path.relpath(p, a.repo): set(words(open(p).read()))
             for p in glob.glob(os.path.join(a.repo, "skills", "**", "*.md"), recursive=True)}
    gloss = []
    if a.gloss:
        for ln in open(a.gloss):
            m = re.match(r"^\|\s*([^|]+?)\s*\|", ln)
            if m and m.group(1) not in ("Pair", "---"):
                gloss.append(m.group(1).lower())
    allow = defaultdict(list)
    if a.allow and os.path.exists(a.allow):
        for row in open(a.allow):
            if row.strip() and not row.startswith("#"):
                p = row.rstrip("\n").split("\t")
                allow[p[0]].append(p[1].lower())

    def score(u):
        ws = list(dict.fromkeys(words(u)))
        for cap in (6, 25):
            kws = [w for w in ws if df[w] <= cap]
            if len(kws) >= 2:
                break
        else:
            return None, None
        best, bf = 0, None
        for f, vocab in files.items():
            r = sum(w in vocab for w in kws) / len(kws)
            if r > best:
                best, bf = r, f
        return best, bf

    os.makedirs(os.path.join(a.out, "uncovered"), exist_ok=True)
    rows = []
    for slug, e in sorted(entries.items()):
        terms = [t.strip().lower() for t in re.split(r"\s/\s", e.get("h2", "")) if t.strip()]
        if gloss and len(e["text"]) <= 1500 and len(terms) > 1 and any(all(t in c for t in terms) for c in gloss):
            rows.append([slug, e.get("h2", ""), 1, 1, 100, "usage"])
            continue
        cov, tot, where, miss = 0, 0, Counter(), []
        for u in units(e):
            s, f = score(u)
            if s is None:
                continue
            tot += 1
            if s >= 0.5 or "*" in allow[slug] or any(u.lower().startswith(x) for x in allow[slug] if x != "*"):
                cov += 1
                if f:
                    where[f.split(os.sep)[1]] += 1
            else:
                miss.append(f"{s:.2f}\t{u}")
        rows.append([slug, e.get("h2", ""), tot, cov, round(100 * cov / tot) if tot else 100,
                     ";".join(k for k, _ in where.most_common(2))])
        up = os.path.join(a.out, "uncovered", slug + ".txt")
        if miss:
            open(up, "w").write("\n".join(miss) + "\n")
        elif os.path.exists(up):
            os.remove(up)

    with open(os.path.join(a.out, "coverage.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["slug", "h2", "units", "covered", "pct", "skills"])
        w.writerows(rows)
    tu, tc = sum(r[2] for r in rows), sum(r[3] for r in rows)
    print(f"entries {len(rows)}  units {tu}  covered {tc} ({100 * tc / max(tu, 1):.1f}%)  "
          f"thin<80% {sum(r[4] < 80 for r in rows)}  gap<50% {sum(r[4] < 50 for r in rows)}")


if __name__ == "__main__":
    main()

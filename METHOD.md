# How the family was verified

A reusable recipe for checking that a skill family covers its source completely, routes
every request through the right steps, and doesn't copy what it shouldn't. The tools are in
[`tools/`](tools/); each has a usage note at the top.

Results below are from the private edition, checked against a commercial textbook in
October 2026, and from this public edition before it was published. No source text, and no
per-entry coverage ledger, is included: those would reproduce the book.

---

## 1. Capture the source as structured entries

Export or capture each entry of the source (heading, body text, sidebars, figure captions)
into JSON batches, then merge them:

```bash
python3 tools/merge.py raw/ entries.json
```

Capture only material you have the right to read, and keep it local. **Result:** 392
entries, with their sidebars and captions.

## 2. Line-by-line coverage

```bash
python3 tools/coverage.py entries.json . out/ --allow allow.tsv --gloss skills/grammar-and-mechanics/references/usage.md
```

Each entry is split into rule units (sentences of six or more words, skipping examples and
sample documents). A unit counts as covered when most of its rare keywords co-occur in one
skill file. Then read every miss: either write the gap or allowlist it with a reason.

**Result (private edition):** 5,734 rule units, 94.6% matched by script; every remaining
unit triaged by hand; 0 entries under 80% coverage after triage. The pass also found three
model documents the family had missed, which were added.

**This edition:** the same test scores 64.7%, which is expected. The book-specific models,
examples, and reference files were removed, and the general rules were rewritten in
original words.

## 3. Index cross-check

```bash
python3 tools/index_check.py index.json . index-misses.csv --allow index-allow.tsv
```

A back-of-book index lists what its book treats as findable, so it catches topics a
line-by-line pass can miss. **Result:** 2,704 index sub-entries. 234 initial misses; 127 of
them were generic phrases ("writer's checklist", "sample of"), and the other 107 were
triaged one by one, leaving 0 unexplained.

## 4. Workflow audit

```bash
python3 tools/workflow_graph.py . --out workflow-graph.md
```

Checks that every skill is reachable from the entry skill, that every sibling points back,
that each has an ordered workflow, that every reference file has a trigger and every named
reference exists, and that every drafting skill carries the entry-and-exit block.
**Result (this edition):** 19 skills, 11 drafting skills, 0 failures.

## 5. End-to-end routing probes

Send the agent realistic requests that start at different points ("should I email or
call?", "write a press release", "tighten this paragraph") and record which skills load,
in order. **Result (private edition, in Hermes):** 18 of 18 probes routed correctly.

The first run found a real defect: a request that started at a drafting skill (a press
release) skipped preparation and revision. The fix was the **entry-and-exit block** now at
the top of every drafting skill. After it, the same request chained `promotional-writing` →
`business-writing` → `line-editing` → `grammar-and-mechanics`.

## 6. Copy check and scrub, before publishing

```bash
python3 tools/shingle.py entries.json . -n 10          # must report 0
python3 tools/shingle.py entries.json . -n 8 --show    # review every hit by hand
python3 tools/scrub_scan.py . --history --patterns private-patterns.tsv
```

- **Shingles:** overlapping runs of words shared with the source. A shared 10-word run is
  almost never chance. At 8 words, expect some stock phrases; review each one. The textbook's own example sentences can slip under both
  thresholds, so quoted examples were also checked against the source separately and
  replaced with original ones.
- **Scrub:** source-book references, figure numbers, page references, course codes, school
  and tool names, personal paths, emails, IP addresses, and token patterns, across every
  file and every commit. Names you don't want in the scanner itself go in a private
  patterns file that is never committed.

**Result (this edition):** 0 shared 10-word runs; every 8-word hit reviewed; 0 scrub hits
across files and history.

## 7. Licenses

Every adopted source was opened on its live page and its license recorded as stated there,
chapter by chapter where a book licenses chapters differently. One textbook chapter turned
out to carry a different license (CC BY-SA) from the rest of the book (CC BY), so nothing
was adapted from it. See [ATTRIBUTION.md](ATTRIBUTION.md).

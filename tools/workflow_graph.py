#!/usr/bin/env python3
"""Audit a skill family's decision tree.

Usage:
    python3 tools/workflow_graph.py [REPO] [--entry business-writing] [--out graph.md]
                                    [--drafting skill-a skill-b ...]

Reads REPO/skills/*/SKILL.md and builds a graph from the backticked skill names in each
body. Reports, and exits 1 on, any of these failures:

1. a skill that can't be reached from the entry skill;
2. a sibling that never points back to the entry skill;
3. a sibling routed only from the entry skill's catalog table, not from a sequence step;
4. a sibling with fewer than three numbered steps (no ordered workflow);
5. a references/*.md file that its own SKILL.md never names (no trigger);
6. a SKILL.md that names a references/*.md file that doesn't exist (a dead link);
7. a drafting sibling missing the "**Entry and exit.**" block that routes it back to
   revision. Drafting siblings default to those whose body contains the block, plus any
   named with --drafting.

--out writes a Markdown report with the routing table and every edge.
"""
import argparse
import glob
import os
import re
import sys
from collections import defaultdict, deque


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repo", nargs="?", default=".")
    ap.add_argument("--entry", default="business-writing")
    ap.add_argument("--out")
    ap.add_argument("--drafting", nargs="*", default=[])
    a = ap.parse_args()
    R, E = a.repo, a.entry

    skills = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(f"{R}/skills/*/SKILL.md"))
    body = {}
    for s in skills:
        t = open(f"{R}/skills/{s}/SKILL.md").read()
        body[s] = re.split(r"^---\s*$", t, maxsplit=2, flags=re.M)[-1]

    edges = defaultdict(set)
    for s in skills:
        for m in re.findall(r"`([a-z-]+)`", body[s]):
            if m in skills and m != s:
                edges[s].add(m)

    seen, q = {E}, deque([E])
    while q:
        for n in edges[q.popleft()]:
            if n not in seen:
                seen.add(n)
                q.append(n)
    unreach = [s for s in skills if s not in seen]

    sec, where = "preamble", defaultdict(list)
    for ln in body[E].splitlines():
        h = re.match(r"^(##+)\s+(.*)", ln)
        if h:
            sec = h.group(2).strip()
            continue
        for m in re.findall(r"`([a-z-]+)`", ln):
            if m in skills and m != E and sec not in where[m]:
                where[m].append(sec)

    fails = []
    lines = ["# Workflow graph", "", f"## Routing from `{E}`", "",
             "| Sibling | Branch points | Points back | Ordered workflow | Untriggered references |",
             "| --- | --- | --- | --- | --- |"]
    for s in skills:
        refs = [os.path.basename(p) for p in glob.glob(f"{R}/skills/{s}/references/*.md")]
        untrig = [r for r in refs if r not in body[s]]
        dead = [r for r in sorted(set(re.findall(r"references/([a-z0-9-]+\.md)", body[s])))
                if not os.path.exists(f"{R}/skills/{s}/references/{r}")]
        if untrig:
            fails.append(f"{s}: untriggered references {untrig}")
        if dead:
            fails.append(f"{s}: names missing references {dead}")
        if s == E:
            continue
        back = E in edges[s]
        steps = re.findall(r"^(?:##+\s+(?:Step\s+)?\d+[.:)]|\d+\.\s+\*\*)", body[s], flags=re.M)
        bp = [w for w in where.get(s, []) if "family" not in w.lower()]
        lines.append(f"| `{s}` | {'; '.join(bp) or '**catalog only**'} | {'yes' if back else '**NO**'} | "
                     f"{len(steps)} steps | {', '.join(untrig) or '-'} |")
        if not back:
            fails.append(f"{s}: no pointer back to {E}")
        if len(steps) < 3:
            fails.append(f"{s}: no ordered workflow ({len(steps)} numbered steps)")
        if not bp:
            fails.append(f"{s}: routed only from the catalog, not from a sequence step")

    drafting = set(a.drafting) | {s for s in skills if "**Entry and exit.**" in body[s]}
    for s in sorted(drafting):
        if s not in body:
            fails.append(f"{s}: named with --drafting but not found")
        elif "**Entry and exit.**" not in body[s] or "grammar-and-mechanics" not in body[s]:
            fails.append(f"{s}: drafting sibling lacks the entry-and-exit block")
    if unreach:
        fails.append(f"unreachable from {E}: {unreach}")

    lines += ["", "## Edges", ""] + [f"- `{s}` → {', '.join(sorted(edges[s]))}" for s in skills]
    lines += ["", "## Failures", ""] + ([f"- {f}" for f in fails] or ["- none"])
    if a.out:
        open(a.out, "w").write("\n".join(lines) + "\n")
    print(f"skills {len(skills)}  drafting {len(drafting)}  unreachable {len(unreach)}  failures {len(fails)}")
    for f in fails:
        print("  " + f)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

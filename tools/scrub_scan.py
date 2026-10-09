#!/usr/bin/env python3
"""Flag text that should not ship in a public skill repo.

Usage:
    python3 tools/scrub_scan.py [REPO] [--patterns FILE] [--history]

Scans every tracked-or-untracked text file under REPO (default: the current directory),
skipping .git. Prints one line per hit as path:line: [rule] text, and exits 1 if anything
was found.

The built-in rules catch source-book residue (figure ids such as "M-3", page references,
"the Handbook"), course and personal context, and secrets. --patterns adds rules from a
TSV file of `name<TAB>regex`, for project-specific names you don't want to commit to the
scanner itself. --history also scans every commit message and every blob in git history.
"""
import argparse
import pathlib
import re
import subprocess
import sys

RULES = [
    ("source-book", r"(?<!Plain English )\bHandbook\b"),
    ("figure-id", r"(?<![/\w])[A-Z][–-]\d{1,2}\b(?![-–.]\d)"),
    ("page-ref", r"(?<!\()(?<!\d{4}, )\b(?:pp?\.|pages?)\s*\d{1,4}\b"),  # APA in-text "(p. 9)" is fine
    ("course", r"\b(?:BCOM|BZAN|MKTG|THEO|PHIL|POLI)\b|\b(?!ISO)[A-Z]{3,4}\s?\d{4}\b"),
    ("course", r"\b(?:lecture notes|syllabus|instructor|professor|Prof\.)"),
    ("tooling", r"\b(?:Notion|Kortext|Canvas LMS|Plaud)\b"),
    ("school", r"\b(?:Boston College|Carroll School|IBA)\b|\bBC\b"),
    ("path", r"/Users/\w+|/root/|~/Academic|hermes-vps"),
    ("email", r"[\w.+-]+@[\w-]+\.[\w.]+"),
    ("ip", r"\b\d{1,3}(?:\.\d{1,3}){3}\b"),
    ("secret", r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*\S{8,}"),
    ("secret", r"\b(?:sk-|ghp_|xox[bp]-|AKIA)[A-Za-z0-9]{10,}"),
]
ALLOW_EMAIL = re.compile(r"noreply@anthropic\.com|users\.noreply\.github\.com|example\.(?:com|org)")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".sh", ".txt", ".json", ".tsv", ".csv", ""}


def load_rules(extra):
    rules = [(n, re.compile(p)) for n, p in RULES]
    if extra:
        for line in pathlib.Path(extra).read_text().splitlines():
            if line.strip() and not line.startswith("#"):
                name, pat = line.split("\t", 1)
                rules.append((name, re.compile(pat)))
    return rules


def scan_text(label, text, rules, me):
    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        for name, rx in rules:
            for m in rx.finditer(line):
                if name == "email" and ALLOW_EMAIL.search(m.group(0)):
                    continue
                # The scanner's own rule table is allowed to name what it looks for.
                if label == me:
                    continue
                hits.append(f"{label}:{n}: [{name}] {line.strip()[:140]}")
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repo", nargs="?", default=".")
    ap.add_argument("--patterns")
    ap.add_argument("--history", action="store_true")
    a = ap.parse_args()
    root = pathlib.Path(a.repo).resolve()
    rules = load_rules(a.patterns)
    me = str(pathlib.Path(__file__).resolve().relative_to(root)) if pathlib.Path(__file__).resolve().is_relative_to(root) else None
    hits = []
    for p in sorted(root.rglob("*")):
        if ".git" in p.parts or not p.is_file() or p.suffix not in TEXT_SUFFIXES:
            continue
        rel = str(p.relative_to(root))
        hits += scan_text(rel, p.read_text(errors="replace"), rules, me)
    if a.history:
        git = lambda *args: subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True).stdout
        hits += scan_text("git-log", git("log", "--all", "--format=%an <%ae>%n%cn <%ce>%n%B"), rules, None)
        for sha in git("rev-list", "--all", "--objects").split("\n"):
            parts = sha.split(" ", 1)
            if len(parts) == 2 and parts[1] != me and pathlib.PurePath(parts[1]).suffix in TEXT_SUFFIXES:
                if git("cat-file", "-t", parts[0]).strip() == "blob":
                    hits += scan_text(f"history:{parts[1]}@{parts[0][:7]}", git("cat-file", "-p", parts[0]), rules, None)
    print("\n".join(hits) if hits else "scrub scan: 0 hits")
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()

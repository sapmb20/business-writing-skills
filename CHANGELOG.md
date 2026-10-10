# Changelog

## 1.1.0 (2026-10-10)

The 10 templates labeled "Original" now have named sources.

- **Adapted** from public-domain text: the incident report now follows OSHA Form 301.
- **Compiled**, with new wording and every element checked against named sources: the
  other nine. Each ends with a "How this was compiled" table that pairs each element with
  its source and flags where this repo departs from that source or adds its own convention.
- Changes the check produced:
  - **Cover letter:** the close no longer proposes interview times (Penn), and the
    "Dear Hiring Manager" fallback is added.
  - **Job description:** splits essential from marginal functions (29 CFR § 1630.2(n)).
  - **RFP response:** follows the FAR's Section L and M logic.
  - **FAQ:** now asks whether an FAQ should exist at all (UK government guidance).
  - **Letter:** adds the optional "Re:" line.
  - **Bad-news letter:** lists when to use the direct order instead.
- README and ATTRIBUTION.md list the sources for every template.

## 1.0.0 (2026-10-09)

First public release.

- 19 skills: the `business-writing` entry skill (six-step sequence, premise check, context
  gate, the 8 S's, delivery) and 18 siblings it loads at the step that needs them.
- Entry-and-exit blocks on the 11 drafting skills, so a request that starts at any of them
  still runs preparation and revision.
- 18 fill-in templates, adopted from CC BY 4.0 and public-domain sources where a credible
  one fit, written for this repo otherwise (see ATTRIBUTION.md).
- Rule references: plain language (US government guides), punctuation and usage, citation
  basics, persuasion and fallacies.
- Verification tools (`tools/`) and the recipe that produced the results in METHOD.md.
- Install scripts for Claude Code and Hermes.

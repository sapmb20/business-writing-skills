# Report and proposal templates

Part of `reports-and-proposals`. Six fill-in templates. Each one states its source and
license. Replace every bracket, delete what the document doesn't need, and rename headings
so they carry your content ("Three Options for the Denver Warehouse", not "Discussion").

Contents: executive summary · formal (recommendation) report outline · internal proposal ·
RFP response · progress report · incident report.

---

## 1. Executive summary

> **Source and license.** The three-part content model (why; what and how; what now) and
> the rule that the summary adds nothing the report lacks are adapted from "7.6 Short and
> Long Reports" in *Technical Writing Essentials, 2nd Edition* by Suzan Last (BCcampus),
> https://pressbooks.bccampus.ca/technicalwriting2ed/chapter/longreports/,
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). **Changes:** condensed into a
> fill-in form; added the investment-memo order from `reports-and-proposals` section 4.

```
EXECUTIVE SUMMARY

Why. [1 paragraph: the problem or opportunity, why it matters now, and the goal and scope
of the report.]

What and how. [1-2 paragraphs: how you studied it (method, data, options compared) and the
key findings, with only the figures a decision needs.]

What now. [1 paragraph: the conclusion and the recommendation, the benefit to the reader,
the cost, and the decision or action needed, with a date.]
```

- Length: about 5-10% of the report, usually one or two pages.
- Write it last. Every claim and figure must appear in the body, and match it exactly.
- For an investment memo, lead with the call instead: recommendation and price target;
  the two or three reasons; valuation in one line; key risks; catalyst and time frame.

---

## 2. Formal report outline (recommendation or feasibility)

> **Source and license.** Component order adapted from "Typical Components of a
> Recommendation Report" and "Typical Components of a Feasibility Study", in "7.6 Short and
> Long Reports", *Technical Writing Essentials, 2nd Edition* by Suzan Last (BCcampus),
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). **Changes:** merged into one
> outline with the feasibility variant marked; added pagination and a weighted-criteria
> table skeleton.

```
[Letter or memo of transmittal, if the report goes outside the organization]

Title page                                  (counts as i, not numbered)
Table of contents                           (headings exactly as in the text)
List of figures / tables                    (if more than five of either)
Executive summary                           (see template 1)
Glossary                                    (if specialist terms)

1  Introduction                             (arabic numbering starts here)
   1.1 Background and purpose
   1.2 The problem: why a solution is needed, the goals, the measurable
       objectives (your criteria), and the constraints
   1.3 Scope and method
   1.4 The options examined                 (feasibility: the single plan studied)
2  [Option A, named]                        (or one section per criterion,
3  [Option B, named]                         point by point)
4  Comparative analysis                     (feasibility: analysis against each criterion)
5  Conclusions                              (what the analysis shows; no new topics)
6  Recommendations                          (verb-first, owner, date)
References
Appendices A, B, ...                        (lettered in the order first mentioned)
```

Weighted criteria table (a decision matrix):

| Criterion | Weight | Option A score (1-5) | A weighted | Option B score (1-5) | B weighted |
| --- | --- | --- | --- | --- | --- |
| [Cost] | [30] | | | | |
| [Risk] | [25] | | | | |
| [Time to implement] | [20] | | | | |
| [Fit with strategy] | [15] | | | | |
| [Ease of use] | [10] | | | | |
| **Total** | **100** | | | | |

Define the scoring scale for each criterion before scoring, and explain every score in the
text; the table summarizes the analysis but doesn't replace it.

---

## 3. Internal proposal

> **Source and license.** Section structure adapted from "Table 7.4.1 Proposal Structure
> Template" in "7.4 Proposals", *Technical Writing Essentials, 2nd Edition* by Suzan Last
> (BCcampus), https://pressbooks.bccampus.ca/technicalwriting2ed/chapter/proposals/,
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). **Changes:** set in memo form
> for an internal reader; added the decision line and the cost-benefit table.

```
To / From / Date / Subject: Proposal: [what you propose, in a few words]

Summary. [2-3 sentences: the problem, what you propose, the total cost, and the decision
you need by when.]

The problem. [Define it precisely, with evidence; show the cost of doing nothing. Don't
blame the reader for the current situation.]

The proposal. [What you will do, its scope (what it will and won't cover), how it will be
implemented, and the obstacles you foresee.]

Benefits and costs.
| Item | One-time | Annual |
| [Software license] | | |
| [Staff time] | | |
| [Savings or revenue] | | |
| Net | | |

Timeline. [Milestones with dates, or a Gantt chart.]

Why us. [The relevant experience of the people who will do it.]

Decision requested. [Approve $[amount] and [resource] by [date], so that [benefit].]
```

---

## 4. RFP response

> **Source and license.** Compiled for this repo (CC BY 4.0, see LICENSE-CONTENT). The
> structure follows the way US federal solicitations are organized, under the Federal
> Acquisition Regulation (FAR). The FAR is a US government work in the public domain; the
> elements are credited in the table below. Private-sector RFPs vary, but most borrow the
> same logic. **The RFP's own instructions override this outline** wherever they differ.

```
Cover letter                    (signed by someone authorized to commit the firm)
Title page                      (RFP number and title, your firm, date, contact)
Table of contents
Compliance matrix               (every RFP requirement → where your response answers it)
1  Executive summary            (their need in their words; your solution; why you)
2  Understanding of the need    (restate the problem and the evaluation criteria)
3  Technical approach           (approach, deliverables, what is and isn't included)
4  Management plan and schedule (milestones, dates, dependencies, key personnel)
5  Past performance             (relevant past work; references who agreed to be contacted)
6  Pricing                      (in the exact format the RFP requires, often a separate volume)
Appendices                      (required forms, representations and certifications, résumés)
```

Before submitting: every requirement in the matrix is answered, page and font limits are
met, required forms are signed, and the deadline is in the RFP's time zone. A proposal can
become binding once accepted, so have pricing and terms reviewed.

**How this was compiled**

| Element | Source |
| --- | --- |
| Follow the solicitation's instructions on format, parts, and limits | FAR 15.204-5(b), Section L, "Instructions, conditions, and notices to offerors", https://www.acquisition.gov/far/15.204-5 |
| Separate parts: administrative, management, technical, past performance, and cost or pricing data | FAR 15.204-5(b): the instructions may require proposals "in severable parts" and list these parts as examples |
| Mirror the evaluation criteria in the response | FAR 15.204-5(c), Section M, "Evaluation factors for award" |
| Representations and certifications as a required attachment | FAR 15.204-1, Table 15-1 (uniform contract format, Section K), https://www.acquisition.gov/far/15.204-1 |
| Compliance matrix; cover letter; executive summary | Proposal-writing practice, not a FAR requirement. The matrix is this repo's suggestion for checking every Section L and M item. |
| Purpose, scope, and audience of a proposal | Last, *Technical Writing Essentials*, "7.4 Proposals" (CC BY 4.0), as used in section 3 above |

---

## 5. Progress report

> **Source and license.** Structure and the three organizing patterns (by time, by task, by
> goal) adapted from "7.5 Progress Reports" in *Technical Writing Essentials, 2nd Edition*
> by Suzan Last (BCcampus),
> https://pressbooks.bccampus.ca/technicalwriting2ed/chapter/progressreports/,
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). **Changes:** set in memo form
> with a status line and a budget row.

```
To / From / Date / Subject: Progress report [n]: [project], [period]

Status: [On track / At risk / Off track], [one-sentence reason].

Introduction. [The project's purpose and scope in a sentence or two; start and planned end
dates; who is doing it and for whom.]

Work completed. [Since the last report, by task or milestone.]
Work in progress. [What is under way now.]
Work remaining. [What is left, with dates.]

Schedule and budget.
| Milestone | Planned date | Forecast date |    | Budget | Spent to date | Forecast at completion |

Problems and changes. [Anything affecting scope, schedule, or cost; what you propose; what
you need from the reader, and by when.]

Overall assessment. [One short paragraph: how the project is going and the expected
completion.]
```

Use the same format every period so readers can compare reports.

---

## 6. Incident report

> **Source and license.** The fact questions are adapted from the US Occupational Safety
> and Health Administration's **Form 301, *Injury and Illness Incident Report*** (Rev.
> 04/2004), items 10-18, in OSHA's recordkeeping forms package,
> https://www.osha.gov/sites/default/files/OSHA-RK-Forms-Package.pdf. Form 301 is a work of
> the US federal government, in the public domain (17 U.S.C. § 105). OSHA does not endorse
> this adaptation. **Changes:** the form's questions are generalized beyond workplace
> injuries (equipment, data, financial, and customer incidents) and set in a memo report.
> The timeline, corrective-action table, and finance notes are added for this repo
> (CC BY 4.0).

```
To / From / Date / Subject: Incident report: [what happened], [date], [location]

Summary. [One or two sentences: what happened, when, where, and the current status.]

Case details.
- Date of the incident; time work or the process began; time of the event
  (or "time cannot be determined")
- What was the person or process doing just before the incident? Name the activity and
  the tools, equipment, systems, or materials in use. Be specific.
- What happened? Tell how the incident occurred.
- What was harmed, and how? (The part of the body; the equipment, data, money, or
  customers affected.)
- What object, substance, system, or event directly caused the harm? (Leave blank if
  none.)

Timeline. [Exact times, in order.]
| Time | Event | Source (witness, log, system record) |

Treatment and impact. [Where treatment was given; emergency room or overnight stay;
damage; work stopped and for how long.]

Immediate actions taken. [Who did what, and when.]

Cause. [Known cause, or "under investigation". Label anything uncertain as such.]

Corrective actions.
| Action | Owner | Due date |

Completed by: [Name, title, phone, date]
Attachments. [Photos, logs, witness statements.]
```

Keep the tone neutral, state facts rather than opinions, and assign no blame: the report
may be used in insurance, regulatory, or legal proceedings. Keep personal details out of
the narrative fields (Form 301 asks for no names in items 14-17), and limit who can read
the report to the people who need it.

**For a workplace injury or illness in the US, this memo does not replace Form 301.**
- **Deadline:** a recordable case needs Form 301, or an equivalent that contains all of
  its information, within 7 calendar days.
- **Retention:** keep it for 5 years after the year it covers (29 CFR Part 1904).

**Finance note:** for a control failure or a payment error, add the dollar amount, the
accounts and periods affected, whether the error reached the financial statements, and who
was notified (controller, audit committee). Keep the report with the control's
documentation.

---
name: reports-and-proposals
description: "Write and review long-form business documents: formal reports (front matter, body, back matter, and their order and pagination), the report components (title, abstract, table of contents, executive summary, introduction, conclusions, recommendations, appendixes, glossary, references), feasibility and recommendation reports, trip reports, proposals (internal informal and formal, external solicited by RFP or IFB, unsolicited, sales, grant), business plans, and reading or writing annual reports. Includes an executive-summary recipe, abstract types (descriptive vs. informative), the opening strategies and the four jobs of a full-scale introduction, the kinds of conclusion, and title rules. Part of the business-writing family. Use for formal or multi-section reports, investment theses and equity research write-ups, case write-ups, recommendation reports, proposals and pitches in writing, business plans, executive summaries, and abstracts."
---

# Reports and Proposals

A formal report is a written account of a major project that needed substantial research,
often written by more than one person. A proposal persuades readers that what you propose
will solve their problem or meet their need, that it is practical, and that you are the right
one to deliver it. Both are long documents, so both need parts that let different readers
find their part: the decision-maker reads the executive summary, and the specialist reads the
body and the appendixes.

Sources: standard report and proposal practice, as taught in open technical-writing texts
(see ATTRIBUTION.md at the repo root). The investment-memo adaptation in section 4, the "easy
to confuse" list, and the delivery notes are this skill's own additions.

**Entry and exit.** Entered here directly? Load `business-writing` and run its steps
1.1-1.6 (purpose, audience, premise check, context gate) before drafting. When the draft is
done, return to its step 6: revision, including `line-editing` (pass 4) and
`grammar-and-mechanics` (pass 7), before you deliver.

## When to Use

- A report too long or too formal for a memo: multiple sections, a title page, an executive
  summary, appendixes, references
- A recommendation or feasibility report that compares alternatives against criteria
- An investment thesis, equity research write-up, or case write-up with an executive summary
- A proposal: an internal request for money or change, a response to an RFP, an unsolicited
  pitch, a sales or grant proposal
- A business plan for investors, lenders, or senior management
- Writing just one component: an executive summary, an abstract, an introduction, a
  conclusion, or a title
- Reading an annual report and knowing what each section is for

**Where it sits in the family.** `business-writing` runs the sequence around this skill
(purpose, audience, premise check, context gate, research, revision). Short informal reports
(a few paragraphs to a few pages, sent as memos or emails) belong to `memo-writing`. Come here
once the report needs front matter, or once a proposal runs past a page. For headings and lists
load `lists-and-headings`, and for line-level revision load `line-editing`. If a sibling isn't
installed, say so and continue.

---

## 1. Choose the document

| The reader needs... | Write | Notes |
| --- | --- | --- |
| Findings on a question, in a few pages, internally | A **report memo** (`memo-writing`) | Introduction, body, conclusion, and recommendations, with no front matter |
| The results of a long or multi-person project | A **formal report** (section 2) | Front matter, body, back matter |
| To know whether a proposed project is practical | A **feasibility report** (section 3) | Alternatives judged against criteria, then one recommendation |
| A record of a business trip | A **trip report** (section 3) | A memo or email to your superior |
| To be persuaded to approve, fund, or buy something | A **proposal** (section 5) | Internal or external; solicited or unsolicited |
| To fund or approve a new venture | A **business plan** (section 6) | A proposal for a business |
| The company's year, for shareholders | An **annual report** (section 6) | Mostly a reading skill for a finance student |

When an organization, a client, an RFP, or an assignment specifies a format, follow it
exactly. Reviewers commonly treat a response that ignores the required format as
noncompliant and set it aside without reading it. The structures below are the default when
nothing else is specified.

---

## 2. The formal report

### The order of parts

Three parts, in this order. Leave out any element the length and audience don't need. A
**title page** and a **table of contents** are usually mandatory.

| Part | Elements, in order |
| --- | --- |
| **(Cover message)** | Precedes the report. Gives the title, the recipient, why the report was written, its scope, and anything the reader considers important |
| **Front matter** | Title page, then abstract and table of contents. Lists of figures and of tables when there are more than five of either. Foreword, preface, and a list of abbreviations and symbols if needed |
| **Body** | Executive summary, introduction, the main text under headings, conclusions, recommendations, notes, and the references or works cited |
| **Back matter** | Appendixes; bibliography; glossary; index (always last) |

**Pagination.** Front matter takes lowercase roman numerals. The title page counts as i but
shows no number, its blank back is ii, so the abstract falls on iii. The body starts at
arabic 1. Center page numbers at the bottom. In a two-sided print report, start each major
section on a right-hand (odd) page. In an electronic report, hyperlink the table of contents
and the lists of figures and tables to their sections.

### What each body part does

- **Executive summary:** begins the body. It gives a fuller overview than the abstract (see
  section 4).
- **Introduction:** gives readers the general information they need to follow the details
  (see the four jobs in section 4).
- **Text:** how the topic was investigated, how the problem was solved, which alternatives
  were explored, and how the best one was chosen. Visuals, tables, headings, and references
  make it both clearer and more persuasive. Load `visuals` for figures and tables.
- **Conclusions:** pull the results together and **interpret** them.
- **Recommendations:** the course of action that follows from the argument and the
  conclusions. Sometimes combined with the conclusions.
- **References:** begin on a new page. In a short report, put them at the end of the body. In a
  report with chapters, put them at the end of each chapter, and repeat a source in full in
  every chapter that cites it. Follow the employer's citation style if it has one. Otherwise,
  load `research-and-sources`.

**Ethics.** Identify the source of every fact, idea, quotation, and paraphrase. Plagiarism
is unethical even when it's unintentional. Repurposed in-house boilerplate may not need a
citation.

Read `references/templates.md` when drafting from a blank page: it holds fill-in templates
for an executive summary, a formal report outline, an internal proposal, an RFP response, a
progress report, and an incident report, each with its source and license.

---

## 3. Feasibility and trip reports

**Feasibility report.** Before an organization launches a project (a new product, new
equipment, a move), it asks whether the project will succeed. The feasibility report answers
that against specific criteria: whether new construction or development is needed, whether
there is enough staff, what it costs, whether funding is available, and what the legal and
regulatory consequences are.

1. Settle the audience, context, and purpose, then write a single-sentence **purpose
   statement** ("This study determines whether..."). It keeps you, or a team, on course.
2. **Introduction:** the purpose, what prompted the study, and the background. When they
   matter, add the scope, how the alternatives were analyzed, and the limits of the study.
3. **Body:** each alternative examined against the **same criteria**, with a heading for each.
4. **Conclusion:** interprets the options and leads to one as the most feasible.
5. **Recommendation:** states which alternative best meets the criteria.

When it stresses specific steps to take, the same document is called a **recommendation
report**.

**Trip report.** A permanent record of a business trip, usually a memo or email to your
immediate superior. The subject line names the destination and the dates. The body covers why
you went, whom you visited, and what you accomplished, with a short section (and heading) for
each major activity. Give the important activities more space, not equal space. End with
conclusions and recommendations, and attach an expense record if one is required.

---

## 4. The components that carry the most weight

### Executive summary

The executive summary may be the **only** part of the document many readers see, so it must
stand on its own and represent the whole document accurately.

- **Contents:** restate the purpose, scope, methods, findings, conclusions, and
  recommendations, and say how the results were reached or why the recommendations follow.
- **Length and order:** about **10 percent** of the original, in the same sequence as the
  original.
- **Independence:** readable without the report. A figure, table, or footnote may go in only if
  it is essential. Never refer to figures, tables, or references by number elsewhere in the
  document.
- **Checklist:** write it **after** the document is finished. Define or avoid unfamiliar terms,
  and spell out uncommon symbols and abbreviations. Be concise, but keep the transitions
  (*however*, *therefore*, *for example*). Include nothing the document doesn't discuss. Put it
  at the start of the body.

**For an investment memo or equity write-up (this skill's addition).** Apply
the same rules with the recommendation first:

1. The call: buy, sell, or hold, and the price target or value range
2. The two or three reasons the market is wrong (the thesis)
3. Valuation in one line: the method and the key multiple or assumption
4. The main risks, and what would change the call
5. A catalyst and a time frame

Each sentence must be traceable to a section of the body, and every figure must match the
model. This is where `business-writing` step 1.5 (verify the premise) matters most, because
an executive summary repeats claims as settled facts.

### Abstract

An abstract helps readers decide **whether to read** the work. An executive summary is for
readers who may read nothing else. An abstract is typically **200-250 words**, may be published
apart from the work, and so needs the key search terms.

- **Descriptive abstract:** purpose, scope, and methods. In effect, a table of contents in
  prose, a few sentences long. Use it for compilations, proceedings, and progress reports that
  have no conclusions.
- **Informative abstract:** the descriptive abstract plus the results, conclusions, and
  recommendations. Use it for wide audiences that need the conclusions.
- **How to write one:** after the report is finished, open with a topic sentence giving the
  subject and scope. Use the outline's headings to sort primary from secondary ideas. Write
  full sentences, joined by subordination and parallel structure instead of a chain of short
  ones. Keep articles and transitions even when cutting words. Spell out any abbreviation
  that isn't widely known. In a report, the abstract is on page iii.

### Introduction: an opening or a full-scale introduction

Every document has one of the two. Letters, emails, and routine reports need only a brief
**opening** that orients the reader and leads into the body. A formal report, a major
proposal, or any complex document needs a **full introduction**, which does some or all of
four jobs:

1. **State the subject:** with background such as a definition, history, or theory.
2. **State the purpose:** why the document exists, and whether it offers a new perspective or
   clarifies an existing one.
3. **State the scope:** how much detail it covers.
4. **Preview the development:** how the subject will unfold, so readers can anticipate it and
   judge the conclusions.

**Opening strategies** (pick one that fits the audience and purpose): the objective; a
problem statement; the scope; background; a **summary** of the results (write "the new
supplier cuts lead times by a week", not "this report discusses lead times"); a telling
detail; a definition (only when it adds insight, never a dictionary quote); an anecdote
(longer documents only); a pertinent quotation; a forecast; or a persuasive hook.
**Write the introduction last.**

### Conclusions

A conclusion ties the main ideas together. It can make a **recommendation**, a **summary**,
a **judgment**, an **implication**, or a **prediction**, and it can end on **ideas for
consideration**, a **call for action**, or a **thought-provoking statement**. Choose by
purpose and audience. A long sales proposal closes by summarizing its salient points and the
company's strengths.

Two rules: raise **nothing new** in the conclusion, and keep it faithful to the purpose the
introduction stated and the method it described.

---

## 5. Proposals

Persuade readers on three points: they need what you propose, it is practical and
appropriate, and you are the right one to provide it. For the argument itself, load
`business-writing` and read its persuasion reference (step 3).

**Strategy for every proposal.**

- Support every claim with facts, statistics, examples, and credible sources, and lead them
  logically to the plan. Don't wander, and make no false claims.
- Proposals often need several levels of approval. Write for the whole audience:
  - When the primary reader is an expert but the approver isn't, add a nontechnical executive
    summary, a glossary, or an appendix.
  - When the primary reader isn't an expert, write the body for the nonexpert and put the
    technical detail in an appendix.
- Write a concise **purpose statement** first, naming the exact problem or opportunity. It
  aligns any collaborators.
- Under deadline, split the work into sections with their own due dates.

**Proposal checklist.** Analyze the audience. Write the purpose statement first.
Segment the work on a timeline. Pick the right context and type. Lead with the reader's
benefits and anticipate objections. Back every claim with evidence. Use an attractive format
unless the RFP defines one. Keep a confident, positive tone.

| Type | What it is | Structure |
| --- | --- | --- |
| **Informal internal** | The most common kind: small spending requests, a hire, a raise, a conference, equipment | Short. Highlight the key benefits |
| **Formal internal** | Large sums or a large reorganization, addressed to someone with the authority to approve | **Introduction:** establish that the problem exists (if readers don't believe it, the proposal fails), then summarize the solution, its benefits, and the total cost. **Body:** the problem, method, equipment, materials, staff, cost breakdown, schedule. **Conclusion:** brief; restate the recommendation, offer cooperation (a meeting, more information). Works cited if you used research |
| **External, solicited (RFP)** | A client defines a need and invites vendors to propose solutions | Follow the RFP's requirements exactly, including page length, font, headings, and sections |
| **External, solicited (IFB)** | Usually government: bids on a precisely specified product or service | Binding. Prove that you meet every specification |
| **External, unsolicited** | Sent without a request, often to fix a problem the client hasn't recognized | Often preceded by a letter of inquiry. A full study and formal proposal follow interest |
| **Sales** | An offer of specific goods or services at a stated price within a stated time | **Legally binding once submitted.** Often valid for a limited period (commonly 90 days) |
| **Grant** | To a nonprofit or government funder | Organize in the exact order of the RFP or guidelines |

For a grant, follow the funder's own guidelines section by section; they override any
general structure. Read `references/templates.md` for the internal-proposal and RFP-response
templates.

---

## 6. Business plans and annual reports

**Business plan.** A proposal for a new venture, written for bankers and outside funders, or
for senior management when it is internal. Analyze the audience first. For a banker, the
purpose is funding, so prove credibility with a record of financial success. For senior
management, show the value the venture adds. Front it with a title page, contents, and an
executive summary; then cover five areas:

1. **Company description and strategy:**
   - The legal name and status, exactly what the company does, and each product's share and
     growth opportunity.
   - The customer base, what makes the products unique, and what is in development.
   - The competitive advantage, and costs set against benefits.
   - A mission statement (the business's purpose), which usually comes before the vision
     statement (its future).
   - Realistic, measurable goals and milestones on a timetable.
   - The management team and key advisers, with their strengths.
2. **Market analysis and strategy:** often the section readers weigh most. Define the market and the competitive climate, analyze the major competitors, and
   show how the venture will enter the market and contribute to profit.
3. **Marketing plan:** specific promotion and advertising actions, costs by channel, and sales
   projections by segment.
4. **Financial analysis:**
   - Historical results and projections. Name the strengths, the weaknesses, where costs can
     be controlled, and the risks with a plan for each.
   - Expect to include a balance sheet, income statements, a multi-year **cash-flow
     projection**, and a sources-and-uses table.
   - **Be conservative:** use slightly low sales and margin figures and slightly overstated
     costs.
5. **Supporting documents** (appendixes): résumés, good reviews and press coverage, and client
   contracts (with the clients' permission).

**Annual report.** Read it knowing what each section is for. Write one only after studying
several past years' reports.

| Section | Job | Reading note |
| --- | --- | --- |
| **Financial highlights** | Sales and earnings, usually three years with the percentage change | The quickest way to see the trend |
| **Statement to shareholders** | The president's or chair's interpretation of the year, plans, and explanations of failures | Shouldn't repeat the highlights. Read it for the narrative management wants believed |
| **Narrative section** | Operations, products, and developments, presented in a positive light | Promotional by design (`promotional-writing`). Check its claims against the statements |
| **Financial statements** | Balance sheet, income statement, changes in financial position, auditor's statement, notes | The evidence |
| **Directors and officers** | The board with its affiliations, and the officers | Governance |

Annual reports range from glossy productions to bare regulatory filings, and their tone and
design are chosen to project an image. Treat the narrative as
persuasion and the statements as data.
Public companies (and some nonprofits) must publish one. When writing one: allot space by
division, use action photographs with captions that put a human face on the company, and
put shareholder logistics on the inside covers (annual-meeting notice, addresses, stock
listing, transfer agent, how to get the 10-K).

---

## 7. Titles

Titles decide whether a document gets read, and how it gets filed and found.

- **Make it specific:** name the topic and signal the scope and purpose. "Projected Cash
  Needs for the Denver Warehouse, 2027-2029" beats "Warehouse Finances."
- **Cut the filler:** no "Notes on," "Report on," or "Study of." Do name the genre when it
  defines the scope (*Annual Report*, *Feasibility Report*). Put the dates of a periodic report
  in a subtitle ("Quarterly Report on...: January-March 2026").
- **No sentences:** a title is not a sentence, except for a rhetorical question in a newsletter
  or magazine article. Avoid jargon and formulas unless the readers are all specialists.
- **Capitalization:** capitalize the first and last words and all major words. Lowercase
  articles, coordinating conjunctions, and prepositions of four letters or fewer unless they
  come first or last. Capitalize prepositions of five or more letters (*Between*, *After*).
- **Subject lines** of emails and memos work as titles and must be specific.

---

## 8. Easy to confuse

- **Abstract vs. executive summary:** an abstract helps readers decide whether to read the
  document; an executive summary may be all they read. An abstract runs 200-250 words in the
  front matter; an executive summary is about 10% of the document and opens the body.
- **Descriptive vs. informative abstract:** descriptive gives the purpose, scope, and methods.
  Informative adds the results, conclusions, and recommendations.
- **Conclusions vs. recommendations:** conclusions interpret what the findings mean;
  recommendations say what to do. They can share a section, but each still does its own job.
- **Feasibility vs. recommendation report:** the same document with a different stress. A
  feasibility report judges practicality against criteria; it becomes a recommendation report
  when it prescribes specific steps.
- **Foreword vs. preface:** someone other than the author (a sponsor or an expert) writes the
  foreword, which comes first. The author writes the preface.
- **Bibliography vs. references:** references list what the report cites. A bibliography lists
  everything consulted, plus suggested reading.
- **Appendix vs. body:** an appendix holds material too detailed for the primary reader but
  needed by secondary readers. If the decision depends on it, it belongs in the body.
- **Solicited vs. unsolicited proposal:** solicited answers an RFP or IFB and must comply
  exactly. Unsolicited must first convince the reader that the problem exists.
- **RFP vs. IFB:** an RFP invites solutions to a need; an IFB binds bidders to a precise
  specification.
- **Formal report vs. report memo:** a report memo has no front matter and fits on a few pages.
  The choice depends on length and audience, not on the subject.

---

## 9. Before submitting

- The purpose statement is written, and every section serves it.
- The required format (from the RFP, grant guidelines, organization, or assignment) is
  followed exactly. Every requested topic is addressed.
- The executive summary stands alone, runs about 10% of the length, and matches the body figure
  for figure.
- The introduction states the subject, purpose, and scope, and previews the development.
- The conclusions introduce no new topic and match the introduction's promise.
- Recommendations follow from the conclusions.
- Every source is cited. Appendixes are lettered in the order they are mentioned and listed in
  the table of contents.
- The table of contents uses the headings exactly as they appear in the text. Lists of figures
  and tables appear when there are more than five of each.
- Pagination: roman numerals for the front matter, arabic numerals from the body on.
- For an online submission, draft in a word processor first, because many forms have no spell
  check.

## 10. Delivering the draft

- For a long document, agree on the outline (section headings and one line each) before
  drafting the full text, unless the user asked for the whole draft.
- Bracket every figure, name, or date the user hasn't supplied. Never invent financials.
- In one line, name the document type and the structure you followed (this skill's default,
  the RFP's, or the assignment's).
- List any claim, number, or source that still needs verifying before submission.

---
name: memo-writing
description: "Write and review business memos and report memos — the To/From/Date/Subject heading (recipient order, initials, cc, specific subject lines), the body sequence (opening statement, context, call to action, discussion, closing, optional summary and attachments), direct vs. indirect order, the informal report written as a memo (introduction, body, conclusion, recommendations), choosing a report type (investigative, feasibility or recommendation, progress, activity, incident), headings, lists and short paragraphs, restrained tone and the \"you\" viewpoint, and a pre-send checklist. Draws on standard memo practice and Grammarly's memo guide. Part of the business-writing family. Use for any internal memo: announcements, policy or procedure changes, requests, project updates, report memos, recommendation memos, investment memos, and school memo assignments."
---

# Memo Writing

A memo is a brief, formal internal document on one subject. It informs a group, flags a
problem, or answers a question, and it tells readers what happens next. The same format
carries short reports: most informal reports in an organization are written as memos.

Sources: standard memo and informal-report practice (see ATTRIBUTION.md at the repo root),
and Grammarly's "How to Write a Memo" for the body sequence and its lengths. The
reconciliation of the two orders in section 3, the "easy to confuse" list, and the delivery
notes are this skill's own.

**Entry and exit.** Entered here directly? Load `business-writing` and run its steps
1.1-1.6 (purpose, audience, premise check, context gate) before drafting. When the draft is
done, return to its step 6: revision, including `line-editing` (pass 4) and
`grammar-and-mechanics` (pass 7), before you deliver.

## When to Use

- Drafting an internal memo: an announcement, a policy or procedure change, a request, a
  project update, or an event
- Writing a report as a memo: findings, analysis, conclusions, and recommendations for an
  internal reader (a "report memo")
- Reviewing a memo draft that reads like a chatty email, a wall of text, or a letter
- Deciding how a memo differs from an email, letter, circular, press release, or minutes

This skill takes over from `business-writing` once the medium is a memo (step 1.4). Run the
rest of that sequence around it: purpose, audience, and the premise check first; revision
with `line-editing` and `lists-and-headings` afterwards. If the medium is still undecided,
load `selecting-medium` first.

---

## 1. Is it a memo?

Use a memo for official internal business that needs a record and a formal voice: internal
changes, news, upcoming events, safety or policy updates, raising awareness of an issue,
addressing a problem, a request, or project updates. A memo on letterhead carries more
authority than a routine email, and it can hold the formatting a short report or proposal
needs.

| Compared with | The memo is... |
| --- | --- |
| **Email** | More formal, and written to survive as an official document that may be printed, filed, or redistributed |
| **Letter** | Internal. Letters go to readers outside the organization. |
| **Press release** | Internal and shorter. A press release is external and longer (write one with `promotional-writing`). |
| **Circular** | For a select group, on one subject. A circular is mass-distributed and can cover several topics and calls to action. |
| **Minutes** | Not a substitute. A memo can attach minutes, but neither format stands in for the other. |

**One subject per memo.** A second topic gets its own memo.

---

## 2. The heading block

```
TO:       Full names and job titles, or a department
FROM:     Your full name and job title
DATE:     The date written, spelled out (September 25, 2026)
SUBJECT:  Specific topic and focus
```

- **No greeting.** The heading already addresses the readers. Sign-offs are usually left out
  too; if you add one, keep it brief.
- **Recipient order:** follow the organization's practice. Where rank applies, senior people
  come first. Where it doesn't, alphabetize by last name.
- **Initials:** some organizations have the writer initial or sign a printed formal memo
  beside the FROM line, as a sign of responsibility for its content.
- **Copies:** a `cc:` notation goes at the end, or at the top with the heading.
- **Subject line:** specific enough to file and find later. "Travel Policy" is vague;
  "New Approval Limit for International Travel, Effective May 1" is specific. Capitalize the major
  words, and lowercase articles, prepositions, and conjunctions shorter than five letters
  unless they come first or last. The subject line does not replace an opening that gives
  context.

---

## 3. The body

### The sequence

Grammarly's structure, in order, with its lengths:

1. **Opening statement** (1-3 sentences): the memo's purpose and only the most crucial
   information. "I'm writing to inform you..." works, though the purpose itself is better.
2. **Context** (3-10 sentences): what this is about, why readers are getting it, and the
   essentials: background, the problem and how it surfaced, the reason for a decision,
   supporting evidence, key dates.
3. **Call to action and task statement** (2-3 sentences, or a bulleted list): what readers
   should do next, or how you will solve the problem. Use the pattern "Please [task] by
   [date]."
4. **Discussion:** the details that persuade readers to act, most important first,
   organized from strongest to weakest evidence.
5. **Closing:** courteous, and it repeats the action you need.
6. **Optional additions:** a **summary** before the closing whenever the memo runs past one
   page (key recommendations, main facts, methods or sources), and **attachments** noted
   below the closing as `Attached: [name], [date]`.

### Reconciling it with the correspondence patterns

Business-writing texts frame the same content as two patterns:

- **Direct pattern (the default):** main point, then facts and details, then a goodwill
  close. Readers appreciate getting the point quickly.
- **Indirect pattern:** context, then explanation, then the negative or sensitive news, then
  goodwill. Use it when readers are likely to be skeptical, or when key readers (a manager,
  a client) may disagree with you. For bad news, load `delivering-bad-news`.

The sources differ on one point. Grammarly places the call to action **before** the
discussion. The conventional report structure puts recommendations **last**, after the
findings. Choose by the memo's job:

- **Announcement, request, or update:** put the ask early, as Grammarly does. Readers act on
  it without reading every detail.
- **Report or recommendation memo:** state the purpose and the bottom line in the opening,
  then give the findings, the conclusions, and the recommendations as the final section.
  Readers who might resist need to see the evidence before the ask.

### Show the reason, not just the decision

People accept a decision more readily when they can see why it was made. Compare "It has
been decided that all staff will work Saturday, March 6" with "To finish the audit files
before the March 8 filing deadline, we need everyone in on Saturday, March 6." The first
sounds imposed, and its passive voice hides who decided. The second leads with the reason.

---

## 4. The report memo

A report organizes facts for a reader who needs them. An informal report is short, from a
paragraph or two up to several pages, and usually travels as a memo, an email, or a letter.
It has four parts:

1. **Introduction:** the subject, the purpose, and essential background. Add the **scope**
   and **method** when they define the report's depth: sources consulted, number of people
   surveyed and who they were, and any limitations.
2. **Body:** a clearly organized account of what you found: test results, project status,
   and the details readers need. How much detail to include depends on readers' knowledge,
   your scope, and the subject's complexity. Use headings for subsections.
3. **Conclusion:** summarize the findings and **interpret their significance**. Don't just
   repeat them.
4. **Recommendations:** a course of action based on the evidence. This can be a separate
   final section or merged with the conclusion ("Conclusions and Recommendations").

### Pick the report type

Read `references/templates.md` when drafting from a blank page: a fill-in memo template
(with its source and license) and notes on adapting it to each report type below.

| Type | Use it when | What it must contain |
| --- | --- | --- |
| **Investigative** | Someone needs information on a workplace problem or question | Primary and secondary purposes, the scope of the investigation, findings, and their significance. If the requester needs a recommendation, it becomes a *recommendation report*. |
| **Feasibility** | Deciding whether a proposed project is practical | A one-sentence purpose ("This study determines whether..."), alternatives judged against specific criteria (cost, staff, funding, legal issues), one option concluded as best, and a clear recommendation |
| **Progress** | A multi-step project, reported at regular intervals | Work done since the last report, what remains, schedule and budget status, and recommended changes. Use the same format every period. |
| **Activity** (status) | A person or team reporting to a manager on a schedule, often monthly | Usually short headed sections such as current work, problems, next period's plans, and staffing. No formal introduction or conclusion is needed. |
| **Incident** | An accident, failure, or health emergency | The precise problem in the subject line; what happened, where, when, injuries, damage, and work stoppage; then corrective action. Neutral tone, no blame, exact times, dates, and witnesses, and any speculation labeled as speculation. It can be used in insurance, workers' compensation, or legal proceedings. |

Formal and annual reports are longer documents with abstracts and executive summaries.
They are not memos. Once a report needs front matter (title page, table of contents,
executive summary) or runs past a few pages, or the task is a proposal or business plan,
load `reports-and-proposals`.

---

## 5. Format and design

- **Headings, lists, and short paragraphs** are what separate a memo from an email. Headings
  flag topics and let readers skip to their section. Lists suit steps, parts, key points,
  and recommendations, but a memo made mostly of lists is disjointed. Give each list context
  and don't overuse them. See `lists-and-headings`.
- **Develop the point.** Concision is not vagueness. "Please be careful with client data" is
  shorter than the three rules for handling client files, but it tells no one what to do.
- **Type:** keep it simple. Grammarly suggests 12-point body text and 14- to 16-point
  headings.
- **Delivery:** memos are often sent by email. Attach the memo as a PDF to keep its
  formatting, or paste it into the email body while keeping the memo's headings and order.
  When an assignment or organization specifies one delivery method, follow it.
- **Length:** the shorter, the better. Add a summary if it runs past one page.

---

## 6. Tone

- **Restrained, not casual or affected.** Most memos call for a measured voice ("The new
  intake process cut wait times more than we projected"), not a breezy one ("Big win, team!"). Forced friendliness sounds insincere. Legalistic phrasing ("Per
  yesterday's discussion... please be advised... herewith") irritates readers and wastes
  their time. See `line-editing`.
- **Professional and polite whatever the topic.** Stick to facts and actionable plans. No
  emoji.
- **The "you" viewpoint:** frame requests around the reader's benefit ("So that you receive
  your refund promptly, please...") rather than the writer's needs ("We must receive...").
  Don't overdo it into flattery.
- **Build goodwill:** be respectful, not demanding; modest, not arrogant; polite, not
  sarcastic; tactful, not condescending.
- **Close with something specific.** Name what you will do, what you expect, and by when.
  Avoid a bare "Let me know if you have questions."

---

## 7. Before sending

- The purpose, reader, scope, and context were decided before drafting (`business-writing`
  step 1).
- The memo has one subject, and the subject line names it specifically.
- The opening states the purpose. A report memo also gives its bottom line.
- The action, owner, and deadline are unmistakable.
- Every fact, figure, and date has been checked (step 1.5 of `business-writing`). Unverified
  claims are removed or marked.
- Unnecessary material is cut and the main points are sharpened. Proofread for spelling,
  grammar, and punctuation.
- Distribution is right: who receives it, who is copied, and in what order.
- Attachments are named on the `Attached:` line and actually attached.
- For a sensitive memo, let it cool off, or have a colleague read it first.
- You accept responsibility for what you send.

---

## 8. Easy to confuse

- **Opening statement vs. subject line:** the subject line names the topic for filing. The
  opening states the purpose and gives context. You need both.
- **Context vs. discussion:** context says why readers are getting this and what led to it.
  Discussion argues for the action, strongest point first.
- **Conclusion vs. recommendation:** a conclusion interprets what the findings mean. A
  recommendation says what to do about it.
- **Investigative vs. feasibility report:** an investigative report answers a question about
  a problem. A feasibility report judges alternatives against criteria and picks one. Either
  becomes a *recommendation report* when it prescribes action.
- **Progress vs. activity report:** a progress report covers one project's status for
  decision-makers or a client. An activity report covers an employee's or team's ongoing
  work for their manager.
- **Summary vs. conclusion:** a summary condenses a memo longer than a page for quick
  digestion. A conclusion interprets significance.
- **Memo vs. email:** see section 1. The difference is formality and permanence, not the
  delivery channel.

---

## 9. Delivering the draft

- Give the memo with its heading block filled in. Bracket any name, title, or date the user
  hasn't supplied (`[Recipient, Title]`) rather than inventing it.
- In one line, name the order you chose (ask early or findings first) and, for a report
  memo, its type.
- Flag any figure, source, or claim that still needs verifying, and any assignment
  requirement (length, sources, citation style) you couldn't confirm.

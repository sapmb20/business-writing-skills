---
name: business-writing
description: "Entry point and orchestrator for business writing. Runs a systematic sequence — preparation (purpose, audience, scope, medium), premise verification, a context-sufficiency gate that asks instead of drafting on invented context, research, organization, outlining, writing, and multi-pass revision checked against the 8 S's from \"The Science of Strong Business Writing\" — and loads the family's specialist skills at the step that needs them: selecting-medium (email vs. call vs. memo vs. meeting), delivering-bad-news (indirect and upward bad-news patterns), email-writing (emails and thread replies), memo-writing (memos and report memos), reports-and-proposals (formal reports, executive summaries, abstracts, proposals, business plans), visuals (charts, tables, and other figures), presentations (talks, slides, and delivery, with its sub-skills virtual-presentations for Zoom, Teams, and recorded talks and circling-back for the follow-up email), line-editing (wordiness, voice, parallel structure), grammar-and-mechanics (proofreading, punctuation, numbers, misused words), lists-and-headings, and career-writing (résumés, STAR stories, offers), research-and-sources (evaluating, quoting, paraphrasing, and citing sources), promotional-writing (press releases, sales letters, brochures, newsletters), writing-for-the-web (web pages, FAQs, repurposing), blogs-and-social-media (blog, forum, and social posts), and instructions-and-procedures (instructions, SOPs, policies, forms, job descriptions). Use for any professional or academic-professional writing task: application and short-answer questions, résumés, cover letters, STAR interview stories, emails, replies to an email thread, offer and internship correspondence, memos, investment memos, reports, proposals, pitches, presentations and slide decks, club or internship materials, choosing how to deliver a message, delivering bad news, and feedback on drafts."
---

# Business Writing

## When to Use

- Drafting any professional text: emails, memos, investment memos, reports, proposals,
  pitches, club or internship materials
- Replying inside an existing email thread, especially when someone else holds a decision
  about you: offers, applications, proposals, reviews
- Recruiting documents: résumés, cover letters, application and short-answer questions,
  STAR interview stories
- Reviewing or giving feedback on someone's draft, including school writing assignments

Skip it for casual messages to friends and for code comments or technical docs that follow
their own style guide.

## The Sequence

Work through the six steps below in order and systematically. The later steps are
interrelated and often overlap. If the work at any step falls short, go back to the
earlier step that caused the problem and redo it until the writing meets the criteria.
When the task is complex or the context is demanding, repeat steps as many times as needed.

Scale the process to the task. A three-sentence email still gets a precise purpose and
audience, but it doesn't need a formal outline. Do the preparation thinking yourself. Show
the user only the decisions that matter (purpose, audience, and any assumptions), then the
draft.

---

## The business-writing family

This skill is the entry point. It owns the sequence, the two gates (steps 1.5 and 1.6), the
8 S's, and delivery. Specialist knowledge lives in sibling skills, and you load each one at
the step that needs it, not all at once.

**How to load one:** in Claude Code, invoke it with the Skill tool; in Hermes, call
`skill_view("<name>")`. If a sibling isn't installed, say so and continue on the one-line
summary in `references/family.md` rather than guessing at its rules.

**The routing tree** (trigger → sibling, at the step where you load it; what each one holds
is in `references/family.md`):

- **Step 1.4, choosing the medium:** medium not fixed → `selecting-medium`. Then by medium:
  email or letter → `email-writing`; memo or report memo → `memo-writing`; formal report,
  proposal, business plan, or investment write-up → `reports-and-proposals`; promotes or
  announces → `promotional-writing`; web or intranet page, FAQ, or adapting content →
  `writing-for-the-web`; blog, forum, or social post → `blogs-and-social-media`; how-to,
  policy, form, or job description → `instructions-and-procedures`; talk, pitch, or deck →
  `presentations` (online or recorded → also `virtual-presentations`; the follow-up email
  after it → `circling-back`).
- **Steps 1-2 of any recruiting task:** `career-writing`.
- **Step 2, research:** uses, quotes, or cites sources → `research-and-sources`.
- **Step 3, organization:** delivers bad news → `delivering-bad-news`.
- **Step 4, outlining:** lists or headings → `lists-and-headings`; a chart, table, or other
  figure → `visuals`.
- **Step 6, revision:** pass 4 → `line-editing`; pass 5 → `lists-and-headings`; pass 7 →
  `grammar-and-mechanics` (also any grammar, punctuation, or usage question).

A request can also start at a sibling. "Should I email or call?" goes straight to
`selecting-medium`; "tighten this paragraph" goes straight to `line-editing`. Come back here
when the task turns into drafting something with stakes.

---

## 1. Preparation

### 1.1 Establish your primary purpose
- What should readers **know, believe, or be able to do** after they finish reading?
- Be precise. A broad purpose is a useless one. To sharpen it, answer two questions: **what**
  is the document about, and **why** are you writing it (what should change)? Then write a one-
  or two-sentence purpose statement naming the readers, and keep it in view while drafting.
  On a team document, write that statement together before anyone drafts.
- Consider possible secondary purposes.

### 1.2 Assess your audience and the context
Be precise about each of these:
- Who is the reader, exactly? Is there more than one? Who else will see, forward, or act on it?
- What does each reader need from this document?
- What is the reader's attitude toward the subject: skeptical, supportive, anxious, or bored?
- Should you define basic terminology, or would definitions bore or even impede the reader?
- Are the readers international? Norms differ: US business prose prizes brevity and
  directness, while many cultures read directness as rude and expect bad news to arrive more
  gently. For international readers, drop idioms, humor, and sports or US-only references;
  write dates out ("4 March 2027") and name time zones; prefer metric units; and, when the
  stakes are high, ask someone from the reader's culture to review the draft.
- Is this a team document? Name one coordinator, agree on the purpose statement and outline
  before anyone drafts, keep one master file with version control, and have one person do
  the final pass so the voice is consistent.
- Make sure readers can follow the writing, and say only what is necessary to communicate the message.
- Learn the context; it tells you what the reader needs and cares about. Ask: how do you and the reader know each other, and what has already
  happened? Which medium does the reader prefer? What pressures (competition, money,
  regulation) and what culture shape their organization? Is anything in the news likely to
  color the reading? Signal the context in the opening.
- Know what NOT to include.

If the purpose or audience can't be determined from the request, the user's materials, or
sensible defaults, that is a gap for step 1.6 to resolve, not something to paper over here.

### 1.3 Determine the scope of coverage
- Define the scope clearly, based on the purpose and audience decisions above.
- Record hard constraints now: word or character limits, format, deadline, and required elements.

### 1.4 Select the appropriate medium
- Choose the medium mainly on the basis of the audience and the purpose. Unless the
  medium is already fixed (the user asked for an email, a form has a text box), load
  `selecting-medium` and weigh its six factors.
- Don't write what should be said. If the task needs back-and-forth, touches something very
  sensitive, or repairs a misunderstanding, the right deliverable may be a call plan and a
  short written recap, not a draft.
- If the medium is email, load `email-writing` and follow it from here on.
- If the medium is a memo, including a report written as a memo, load `memo-writing` and
  follow it from here on. A formal report, proposal, or business plan: load
  `reports-and-proposals`.
- If the medium is a presentation, pitch, or slide deck, load `presentations` and follow it
  from here on. If it is online or recorded, also load `virtual-presentations`. For the follow-up
  email after the talk, load `circling-back`.
- If the piece promotes or announces (press release, sales letter, brochure, newsletter),
  load `promotional-writing`. If it is a web page or FAQ, load `writing-for-the-web`. If it
  is a blog, forum, or social post, load `blogs-and-social-media`.
- If it is instructions, a procedure or policy, a form, or a job description, load
  `instructions-and-procedures`.
- If you are replying inside an existing thread rather than starting one, also load the
  thread-reply reference that `email-writing` points to, beginning with its parse checklist.

### 1.5 Verify the premise

Most damaging errors are not errors of craft. They are confident statements about a
relationship or a process that the writer never confirmed: an offer, a decision, an
agreement, a deadline.

- List every claim the piece depends on and mark each one **Confirmed** (in writing; quote
  it), **Inferred**, or **Assumed**.
- For each claim that isn't Confirmed, **choose a move; don't default to hedging.** In order
  of preference: **cut it**, **ask**, **anchor it** as your plan ("I'll hold June open"),
  **state it plainly** (warm relationship, low downside), and **hedge** only as a last resort.
- Calibrate on **what the sentence does if the claim is false** and **what a correction
  costs the reader**, not on caution. Precision rises with the recipient count. Don't
  over-correct into distance with warm contacts.
- **Four absolutes:** never attribute words to someone from memory (drop the attribution,
  don't hedge it); never assert a commercial term you weren't given; never state as fact
  anything that would embarrass the user if quoted back; never describe a process stage you
  can't point to.

Read `references/premise-check.md` for the full moves, calibration, and examples whenever
the piece makes claims about an offer, a decision, an agreement, a deadline, or a prior
conversation. It also feeds revision pass 2.

### 1.6 Decide whether you have enough context to draft

Make the go/no-go call explicitly, before writing a word. Drafting past a gap buries it in
fluent prose. For each unknown, ask: *would two plausible answers produce materially
different drafts?*

- **No:** assume the likeliest answer, note it, and draft.
- **Yes, but it's a discrete fact** (a date, a name, a number): bracket it as `[start date]`,
  draft, and list the brackets on delivery.
- **Yes, and it changes the framing, claims, tone, or structure:** stop and ask. This is the
  only case that blocks drafting.

**Never infer, always ask:** what the interaction actually was, how the relationship
started, who the other recipients are, what has already been said, and the size of the
downside. **Ask for the artifact** (the thread, the posting) rather than a summary. Ask
**once**: four or five questions at most, each with a reason and the default you'd use. Scale
the gate to the stakes, and never ask about anything that has a sensible default. When you
proceed on inference, say so on delivery.

Read `references/context-gate.md` for the full test, the reasons behind each never-infer
item, and the over-firing rules, on any first contact, offer thread, or message that
creates a record.

---

## 2. Research

For a recruiting task, load `career-writing` here: it says what the reader screens for and
which proof points to look for in the user's materials.

When the piece draws on sources (anything cited, quoted, paraphrased, surveyed, or
interviewed), load `research-and-sources`. It covers evaluating sources, note-taking,
interviews and questionnaires, quoting and paraphrasing, plagiarism and copyright, and
citation basics in APA, MLA, and Chicago.

Keep the available sources of information in mind:
1. Your own knowledge and that of colleagues (for the assistant, this includes the user's files,
   such as a CV, prior drafts, and notes)
2. The knowledge of people outside the workplace, gathered by interviewing for information
3. Internet sources, including websites, directories, archives, and discussion groups
4. Library resources, including databases and indexes of articles, books, and reference works
5. Printed and electronic sources in the workplace, such as brochures, memos, email, and web documents

The amount of research depends on the scope of the project.

Never invent facts about the writer, an organization, or a source. If a claim can't be
verified, keep it general or ask the user.

---

## 3. Organization

Without organization, the gathered material will be incoherent to readers. To prevent this,
choose a **primary method of development** (for example chronological, spatial, general-to-specific,
order of importance, comparison, cause-and-effect, or problem-solution).

- Base the choice on the subject, the reader's needs, and the purpose.
- Confirm that the method is the right one. Both of these must be true:
  - It will help readers focus on the information.
  - It will make the presentation easy for readers to follow.
- If the subject naturally lends itself to a method, use that method. Don't impose another one on it.
- You will often need to combine methods. Use one primary method for the major divisions
  and subordinate the others. In finance documents, problem-solution and order of importance
  (strongest point first) carry most recommendations; comparison carries option analyses,
  and either runs whole-by-whole (all of option A, then all of B) or point-by-point (cost
  for A and B, then risk for A and B), the second being easier to scan.
- **If the piece argues for something** (a proposal, a recommendation, a thesis, a request
  for money), read `references/persuasion.md`. It covers conceding the downside, the
  common logical fallacies, and tests for evidence, and you run it again as a stress test in
  revision.
- **If the message delivers bad news, load `delivering-bad-news`.** The order of the parts
  depends on the reader. Customers and employees get the indirect pattern; a boss gets the
  news early with solutions attached.

---

## 4. Outlining

- Break large and complex subjects into manageable parts.
- Put key points in the positions of greatest emphasis.
- Consider layout and design elements that suit the reader, subject, and purpose. The outline
  may suggest where headings, lists, or other design features would help. When the document
  will use lists or headings, load `lists-and-headings`.
- Mark where each visual goes ("[table of ...]", "[graph of ...]"). When the document needs a
  chart, table, or other figure, load `visuals`.

---

## 5. Writing

- Expand the outline into paragraphs and sequences.
- Concentrate on developing all the necessary ideas.
- **Write the introduction last**, because only then will you know exactly what the body contains.
  - The opening should announce the subject and give the reader essential background, such as
    the document's primary purpose.
  - In longer documents, the introduction should be a frame into which readers can fit the
    detailed information that follows.
- **Write the conclusion last as well.**
  - Tie the main ideas together and make a final, significant point.
  - The final point may recommend an action, make a prediction or judgment, or summarize the
    main points. The right choice depends on the purpose and the reader's needs.

---

## 6. Revision

- Find and correct faults. Be ruthless and honest, for the reader's sake.
- Read and evaluate the draft as if you were a reader seeing it for the first time.
- Check the draft for accuracy, completeness, and how well it achieves the purpose and meets
  the reader's needs and expectations.
- Trim extraneous information. Give readers exactly what they need, without burdening them
  with unnecessary information or sidetracking them into loosely related subjects.
- **Don't try to revise for everything at once.** Read the draft several times, and look for
  a different set of problems on each pass:
  1. Larger issues first, such as unity and coherence
  2. **The wrong-premise read.** Reread the draft as a reader who is about to deliver bad
     news, a correction, or a rejection. Every claim from step 1.5 that is not Confirmed
     now reads back to you in the worst light it will ever have. Anything that becomes
     presumptuous, entitled, or accusatory under that reading gets one of the five moves in
     step 1.5 — usually cut, ask, or anchor, rarely hedge. In a warm, low-downside thread
     this pass will often come back clean; that is a result, not a reason to invent
     problems. It takes a minute and catches failures no amount of line editing would.
  3. The 8 S's check (below; detail in `references/eight-s.md`). For a persuasive piece, also
     run the fallacy check in `references/persuasion.md`
  4. Line editing: wordiness, weak signals, voice, and parallel structure (`line-editing`)
  5. Formatting: lists and headings, if the document has them (`lists-and-headings`)
  6. Hard constraints, such as word count (count the words, don't estimate) and required elements
  7. Mechanical corrections last, during proofreading: grammar, punctuation, numbers, dates,
     abbreviations, spelling, and the data in tables and figures (`grammar-and-mechanics`)
- Tactics: let the draft cool before revising, and **read it aloud**. Check that
  the introduction and conclusion still match the body after revision. Check that the same
  thing has the same name throughout. When reusing earlier text (your own boilerplate, a
  previous memo), adapt its tense, voice, tone, and point of view to the new purpose and
  medium. Reusing in-house boilerplate is normal at work, but in school, reusing work without credit is plagiarism.
- Before sending anything with consequences, run an ethics check: would you be comfortable
  if the reader learned everything you know? Look for a passive voice that hides who acted,
  wording that is technically true but misleading, and bad news buried where it won't be
  read or left out.
- Have others review the writing. When the assistant is drafting, the user is that reviewer. Invite
  their feedback and iterate on it.

---

## The Science of Business Writing: the 8 S's

From Bill Birchard, "The Science of Strong Business Writing" (*HBR*). Not every piece needs
all eight; pick the ones that serve the purpose and the reader.

1. **Simple:** short sentences, familiar words, active voice; strip to the essentials
2. **Specific:** a memorable shorthand phrase the reader can carry away
3. **Surprising:** unexpected wordplay or framing makes it stick
4. **Stirring:** emotionally charged words and short metaphors, never melodrama
5. **Seductive:** open a question or conundrum, then deliver the payoff you promised
6. **Smart:** give the reader an "aha", such as a fresh distinction
7. **Social:** the writer's own voice (the user's, not the assistant's), the human angle, "you"
8. **Story-driven:** a short situation, action, and result

**Golden rule: reward readers as you would want to be rewarded yourself.** Read
`references/eight-s.md` for the reasoning and examples behind each one when running
revision pass 3 on a piece with stakes.

---

## Delivering the result

- Give the final text, clearly separated from any commentary. For an email, give the
  subject line first.
- Report the word count for every piece that has a limit.
- Briefly list the assumptions you made and any facts the user should verify or could add.
- Separately, call out any belief about the relationship, the process, or a prior
  conversation that you inferred rather than were told (step 1.6). Put it where the user
  will read it before sending, not at the end of a long list.
- Invite feedback, then circle back through the steps when revising.

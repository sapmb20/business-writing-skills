---
name: circling-back
description: "Draft the follow-up email after a presentation, pitch, or briefing: a short, structured summary of the action items the talk ended on (usually the last slide: Next Steps, Recommendations, Action Items, Asks), with an owner and a due date for each, plus anything decided in Q&A. Pulls the action items out of the deck, checks that each one has a verb, an owner, and a date without inventing missing ones, and then loads the business-writing family to write the email: email-writing (subject line with the call to action, opening, the request, sign-off, CC, replying in the meeting's thread), lists-and-headings (the action list), line-editing (parallel, verb-first items), and delivering-bad-news when an item is a decline or a slip. A sub-skill of presentations in the business-writing family. Use after any presentation or meeting that ended with next steps: recap emails, circling back, and follow-ups after a pitch or a group presentation."
---

# Circling Back

The talk ended on its call to action, usually the last slide. The circle-back email puts
that slide in writing for everyone who was there: what each person agreed to do, and by
when. It's short, it's a list, and it closes the loop that the presentation's closing
opened.

This is a sub-skill of `presentations`, and it does its drafting through the rest of the
family:

| Step | Loads | For |
| --- | --- | --- |
| 1-2 | `business-writing` (steps 1.5 and 1.6) | Checking the premise (what was actually agreed) and asking about anything missing instead of inventing it |
| 3 | `lists-and-headings` | The action list: type, lead-in, parallel items, 2 to 8 entries |
| 4 | `email-writing` | Subject line, greeting, opening, the request, close, CC, thread replies, final checks |
| 4 | `delivering-bad-news` | Only if an action item is a decline, a delay, or a missed target |
| 5 | `line-editing` | Verb-first, parallel, no filler |

Load each one at its step: in Claude Code with the Skill tool, in Hermes with
`skill_view("<name>")`. If one isn't installed, say so and use the one-line summary in the
table.

Sources: this skill's own, built on the family's rules: the presentations closing (a specific ask with a date), the list rules, and the
email conventions.

**Entry and exit.** Entered here directly? Load `business-writing` and run its steps
1.1-1.6 (purpose, audience, premise check, context gate) before drafting. When the draft is
done, return to its step 6: revision, including `line-editing` (pass 4) and
`grammar-and-mechanics` (pass 7), before you deliver.

## When to Use

- After a presentation, pitch, briefing, or meeting that ended with next steps, action
  items, recommendations, or asks
- "Circle back", "send the recap", or "follow up on the presentation"
- A group presentation where the team needs each owner's commitments in writing
- Turning a deck's last slide into an email

Not for minutes of a whole meeting (record those in full, following the minutes checklist in
`presentations`), or for a follow-up when nothing
was decided (use `email-writing`, "Following up on an undecided process").

---

## 1. Gather the inputs

| Input | Where to get it | If it's missing |
| --- | --- | --- |
| The action items | The deck's **last content slide** (Next Steps, Action Items, Recommendations, Asks, The Ask, Path Forward). Also scan earlier slides for owners and dates | Ask for the deck, or for the last slide's text |
| What changed in the room | The user, notes, or a recording (a transcript) | Ask: "Did anything change in Q&A: new items, owners, or dates?" |
| Recipients | The audience and the meeting invite | Ask. Never guess who attended |
| The purpose of the talk | The presentation's purpose statement | Take it from the title slide or the opening |
| Deck link or attachment | The user | Leave a `[link to deck]` placeholder |

**Reading a .pptx:** slides are XML inside a ZIP. Read them in **presentation order**, not
file order (`slide10.xml` sorts before `slide2.xml`):

```python
import re, zipfile, sys
z = zipfile.ZipFile(sys.argv[1])
attr = lambda tag, name: (re.search(rf'\b{name}="([^"]*)"', tag) or [None, None])[1]
rels = {attr(t, 'Id'): attr(t, 'Target')
        for t in re.findall(r'<Relationship\b[^>]*>', z.read('ppt/_rels/presentation.xml.rels').decode())}
order = [attr(t, 'r:id') for t in re.findall(r'<p:sldId\b[^>]*>', z.read('ppt/presentation.xml').decode())]
for n, rid in enumerate(order, 1):
    xml = z.read('ppt/' + rels[rid].lstrip('/').removeprefix('ppt/')).decode()
    print(f'--- slide {n}:', ' | '.join(t for t in re.findall(r'<a:t>([^<]*)</a:t>', xml) if t.strip()))
```

Skip a final "Questions?" or "Thank you" slide; the action items are on the slide before it.
For a PDF deck, use `firecrawl-parse`. For Google Slides, export it as .pptx or paste the
slide text.

## 2. Turn each item into an action

Each action item needs **three parts**:

1. **Action**: what gets done, starting with a verb ("Approve", "Send", "Schedule")
2. **Owner**: one named person, never "the team" or "we"
3. **Due date**: a real date, written out with the weekday ("Fri, Oct 16"), with a time and
   time zone if it matters

Most slides have only the first part ("Expand vendor onboarding"). **Don't invent the
other two.** This is `business-writing` step 1.6, the context gate:

- If the user knows the owners and dates, ask once, listing every gap together.
- If nobody decided, write the gap into the email as a question: "Owner: **open, can you
  take this, Maria?**" or "Due: **to confirm**". An open item in writing gets settled; an
  invented owner causes trouble.

**Premise check** (`business-writing` 1.5): a recommendation on a slide **isn't a decision**.
Write "we agreed" only if the user says it was agreed. Otherwise use "we proposed" and ask
for the decision.

Keep only real actions. Turn background or findings into the one-line recap (section 3), or
cut them.

## 3. Structure the email

Load `email-writing` and follow it. This is the shape that skill produces for a circle-back:

```
Subject: Next steps from [talk title]: [first action] by [date]

Hi all,

Thank you for [the time / your questions] at [talk] on [day]. As promised, here are the
action items we [agreed on / proposed]:

1. [Verb] [object]: [Owner], by [Weekday, Mon DD]
2. [Verb] [object]: [Owner], by [Weekday, Mon DD]
3. [Verb] [object]: Owner open. Could you take this, [Name]?

[One sentence: the decision or recommendation these serve.]

Please reply by [date] if anything above is wrong or if you can't own your item.
The deck is here: [link].

Best,
[Name]
```

Rules for each part:

- **Subject line:** carries the call to action and the first date (`email-writing`, "Subject
  line"). Not "Follow-up" or "Recap".
- **Opening:** one sentence of thanks or context, then the list. The main point comes
  first.
- **The list** (`lists-and-headings`): **numbered** when the items have an order or a
  priority, bulleted otherwise. A lead-in sentence ending in a colon. **2 to 8 items**; past
  8, group them under short labeled headings by owner or workstream. Each item follows the
  same pattern: verb, object, owner, date.
- **One-line recap:** the decision or recommendation the actions serve. The email is a
  record, not a second presentation, so leave the analysis in the deck.
- **The request:** one specific ask with a date: confirm, correct, or flag your item.
- **Recipients** (`email-writing`, the CC rule): everyone with an action item goes in
  **To**. Interested people who have no item go in CC. If the meeting already has an email
  thread, **reply in that thread** and follow `email-writing`'s thread-reply reference.
- **Bad news in the list:** if an item records a decline, a delay, or a missed target, load
  `delivering-bad-news` and put that item in its own short paragraph, not in the list.
- **International recipients:** no idioms, dates written out, time zones given.
- **Length:** the body should fit on one screen without scrolling, about 150 words plus the
  list.

## 4. Timing

Send it **the same day, or within 24 hours** of the talk, while commitments are fresh.
Before the deadline of the earliest item, check whether its owner has replied.

## 5. Revise

- `line-editing`: **parallel**, verb-first items; no "just circling back", "per our
  meeting", or "hope this finds you well".
- `lists-and-headings`: same punctuation on every item, a working lead-in, and no
  one-item list.
- `email-writing`, "Final checks before sending": recipients, attachment or link, names
  spelled correctly, every date matching its weekday.

## 6. Easy to confuse

| Pair | The difference |
| --- | --- |
| Recommendation vs. action item | A recommendation proposes; an action item has an owner and a date. Slides usually show the first, and this email turns them into the second |
| Agreed vs. proposed | Say "agreed" only for what was decided in the room. Anything else is proposed, and the email asks for the decision |
| Circle-back vs. minutes | Minutes record the whole meeting; a circle-back records only who does what by when |
| Circle-back vs. thank-you note | A thank-you can stand alone; a circle-back can open with thanks but exists for the list |
| To vs. CC | People with an action go in To; people who only need to know go in CC |

## 7. How to deliver the draft

1. The **action table** you extracted (action, owner, due date, source slide), with every
   gap and assumption marked
2. Questions about anything still missing, all asked in one message (step 2)
3. The **email**: the subject line, then the body, ready to paste
4. One line on recipients (To and CC) and send timing

Never send it yourself. Drafting is the job; the user sends.

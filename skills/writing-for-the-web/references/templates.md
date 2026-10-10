# FAQ page template

Part of `writing-for-the-web`.

> **Source and license.** Compiled for this repo (CC BY 4.0, see LICENSE-CONTENT). The
> wording is new; each element is credited in the "How this was compiled" table below.
> Government sources are cited, not copied.

## Before writing: should this be an FAQ at all?

Government content designers in the UK, Wales, and New Zealand advise **against** FAQ
pages. They argue that FAQs:
- duplicate content found elsewhere;
- are slower to scan than plain headings;
- push the key words to the end of each heading;
- signal that the main pages are missing something.

So first try to put each answer **on the page where readers already look**. Use an FAQ
only for questions that cut across pages, or as a stopgap while the main content is fixed.

- **Collect real questions** from the people who answer customers: support, sales, front
  desk, inboxes, search logs. Don't invent questions nobody asks.
- **Rank them** by how many readers ask and how much it matters to them; the top three go
  first.
- **Fix, don't explain away.** If many people hit the same problem, raise it with the team
  that owns it; the FAQ is a stopgap.

## Template

```
# [Topic] FAQ
Last reviewed: [Month D, YYYY]

[One sentence: who this page is for, and where to go if the answer isn't here (a named
team, a form, a phone number with hours).]

On this page: [Category 1] · [Category 2] · [Category 3]      (jump links)

## [Category 1, in the reader's words, e.g. "Payments"]

### [Question, as the reader would ask it, e.g. "When will my refund arrive?"]
[Answer first, in one or two sentences: "Within 5 business days of approval."]
[Optional detail or one exception.] [Link: "Track a refund"]

### [Next question]
[...]

## [Category 2]
[...]

Still need help? [Contact route, with hours and expected response time.]
```

## Checks

- [ ] Each question is in the reader's words and is a real question
- [ ] Each answer starts with the answer, not with background
- [ ] Answers are short; longer explanations are linked, with link text that says where it goes
- [ ] Headings are nested in order (H1, H2, H3), no deeper than three levels
- [ ] Every figure, date, and policy is current, and the page shows when it was last reviewed
- [ ] A named owner reviews the page on a schedule

## How this was compiled

| Element | Source |
| --- | --- |
| Question headings, used when you know what readers will ask | Digital.gov, *Plain Language Guide Series*, "Headings", https://digital.gov/guides/plain-language/design/headings (US federal government) |
| Nesting no deeper than three levels | Digital.gov, "Headings" |
| The case against FAQs: duplication, slower scanning, key words pushed back | Government Digital Service, "FAQs: why we don't have them" (GDS blog, July 25, 2013), https://gds.blog.gov.uk/2013/07/25/faqs-why-we-dont-have-them/ |
| FAQs as a sign of missing or misplaced content | New Zealand Government, "FAQs — do not use them", https://digital.govt.nz/standards-and-guidance/design-and-ux/content-design-guidance/content-structure/faqs-do-not-use-them · Welsh Government, "Frequently asked questions (FAQs): avoid them", https://www.gov.wales/frequently-asked-questions-faqs-avoid-them-govwales |
| Headings in order; descriptive link text | W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*, Success Criteria 1.3.1 and 2.4.4 |
| Questions from frontline staff, ranked by importance; review date and named owner | Repo convention (`writing-for-the-web` section 7) |

**Where the sources differ:** Digital.gov supports question headings, while GDS argues that
questions push the key words to the end. This template keeps question headings only
inside an FAQ, which is the format in which readers expect them, and follows GDS on whether
to build an FAQ at all.

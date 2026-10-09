---
name: writing-for-the-web
description: "Writing and posting content for a company or organization website — policy check with the webmaster, writing for readers who scan (main point first, plain language), seven content techniques (short focused text, informative headings, lists, keywords in the first 50 words, no print-style directional cues, light graphics, screen-legible fonts), internal and external links and vetting outside sites, posting an existing document (single-file version, PDF), sourcing and privacy statements, global readers, FAQ pages (questions from customer-facing staff, decreasing importance, categories, an FAQ checklist and template), and repurposing content for a new context or medium, with labeled current-practice notes (Google Ads, SEO, title tags, accessibility) and finance additions (company websites and Reg FD, investor-relations pages). Part of the business-writing family. Use when writing, editing, or reviewing a web page, landing page, intranet page, product or service description, FAQ, help page, or investor-relations page, or when adapting a brochure, report, or other document for the web."
---

# Writing for the Web

People don't read web pages; they scan them for the one thing they came for. Everything in
this skill follows from that: the point first, short chunks, headings that tell the reader
whether to stop, and links that go exactly where they promise.

Sources: standard web-writing practice, consistent with the US federal plain-language
guidelines and the W3C's WCAG accessibility standard (see ATTRIBUTION.md at the repo root).
The current-practice and finance notes in §9 and the "easy to confuse" list are this
skill's own, labeled as such.

**Entry and exit.** Entered here directly? Load `business-writing` and run its steps
1.1-1.6 (purpose, audience, premise check, context gate) before drafting. When the draft is
done, return to its step 6: revision, including `line-editing` (pass 4) and
`grammar-and-mechanics` (pass 7), before you deliver.

## When to Use

- Writing or editing a web or intranet page, landing page, product or service description,
  or investor-relations page
- Building or fixing an FAQ or help page
- Putting an existing document (report, brochure, policy) on a site
- Adapting content from one document or medium to another (repurposing)
- Reviewing a page for scannability, links, keywords, or accessibility

**Where it sits in the family.** Run `business-writing` steps 1.1–1.6 first. If the page
promotes something, load `promotional-writing` for the persuasion and claims rules; for blog
posts, forums, and social feeds, load `blogs-and-social-media`. Headings and lists follow
`lists-and-headings`; plain language follows `line-editing`; outside sources and permissions
follow `research-and-sources`.

---

## 1. Policy first

Before posting, ask the webmaster or your manager whether the content fits the
organization's web policy. At a school, check its web or IT posting standards.

## 2. Crafting content

Readers scan for specific information, so **state the important points first**, then the
supporting detail. Keep the style straightforward and concise, in plain language
(`line-editing`). Seven techniques:

1. **Text.** Break dense blocks into short paragraphs that can be scanned and absorbed
   quickly. Give each passage **one facet** of the topic. Link to secondary detail rather than
   including it.
2. **Headings.** Informative topic headings tell readers instantly whether a passage is worth
   reading; they also show the structure and mark the shift from one topic to the next. Set
   them off in bold or another style (such as color), on their own line above the text, or in
   the left margin beside it.
3. **Lists.** Bulleted and numbered lists break up paragraphs, shorten text, and highlight
   what matters. Don't overuse them: lists with no explanatory text around them lose
   coherence.
4. **Keywords.** Put the words a reader would search for near the start of each topic,
   ideally in its first sentence or two, so both search engines and scanners find it.
   - *Weak:* "We're excited to share our newest offering for small firms, available
     next month."
   - *Keyworded:* "Ledgerline Payroll for small accounting firms runs payroll, tax filings,
     and direct deposit from one dashboard, starting March 3."
5. **Directional cues.** Drop print habits like "on the next page" or "see below". Put links
   right beside the content they relate to, such as Back to Top on long pages.
6. **Graphics.** Use visuals that give information text can't, or welcome visual relief, and
   only ones that suit the audience and purpose. Avoid complex graphs and animation that
   clutter or slow the page. Work with the webmaster to optimize every image (ask which
   compression format they prefer), and consider a graphics-free option.
7. **Fonts.** Screens render type at lower resolution than paper, so **sans serif** usually
   reads better for running text. No ALL CAPS or bold for whole blocks; both slow reading.
   For special characters (math, chemistry), ask the webmaster how to submit the file for
   HTML coding, or post it as a PDF.

## 3. Links

**Internal links** help readers move around. On a long page, open with a short list of
jump links to its sections.

**External links** enrich the topic with outside material and keep your page shorter.

- Mark them with an icon or text label so readers know they are leaving the site.
- Keep links out of running paragraphs where possible: too many distract, make scanning
  harder, and pull readers away before they finish.
- **Vet every outside site before linking:**
  - Is the author or sponsoring organization reputable?
  - Is the content accurate, current, and unbiased?
  - Does the page carry a date stamp ("last updated on...")?
- Link **directly to the relevant page or section**, not the homepage, and say why you're
  sending the reader there. (Source evaluation in depth: `research-and-sources`.)

## 4. Posting an existing document

- Keep the original sequence and layout where you can.
- If you shorten or revise it for the web, **add a notice saying how it differs** from the
  original.
- **Review it offline before posting:** right version? Every link working and going to the
  right place? (`grammar-and-mechanics` on proofreading.)
- Offer a **single-file version** (the whole content as one long page) for readers who will
  print it.
- Convert reports, flyers, and brochures to **PDF** so the electronic copy looks identical to
  print. Readers can view it, download it, or print part of it; PDF tools also add forms,
  signatures, watermarks, and password protection.

## 5. Ethics and privacy

- **Keep a record** of where you found every piece of online content: text, images, tables,
  video.
- **Get the copyright holder's approval** before using it. It is a legal and ethical
  requirement, and documenting sources makes the site more credible. Credit with a link or a
  citation (`research-and-sources`).
- **Privacy.** Keep content consistent with the site's privacy statement, which tells
  visitors how the sponsor handles information they submit (asked for or not), how it uses
  cookies, and how it handles security breaches.

## 6. A global audience

Remove expressions and references only American readers would get. Write dates, times, and
measurements the international way. Choose symbols, icons, colors, images of people, and
captions that read clearly across cultures. See `business-writing`'s global reference and
`visuals` (global graphics); biased language and idioms are in `line-editing`.

## 7. FAQs

An FAQ page pairs the questions readers are likely to ask with their answers, so they don't
have to search the whole site. A good one shows you value the reader's time and cuts the
company's support load. It is **not** a substitute for fixing the product: if many customers
hit the same flaw, work with the product team to fix it rather than burying the problem in
an FAQ.

Always-on rules: questions come from colleagues who talk to customers; order them by
**decreasing importance to the reader**; group related ones under topic headings; bold the
questions; keep answers short, linking to longer ones; review it on a schedule and date it.
Read `references/templates.md` for an FAQ page template.

## 8. Repurposing

Repurposing means reusing existing text and visuals, copied or converted, in a new
document or medium that serves another purpose: a brochure built from the website's product
description, then posted back to the site as a download. It saves the effort of re-creating
content, whether by copy and paste or by a content-management system updating many documents
at once. Technical publishing calls the practice **single sourcing**; reused standard text is
traditionally **boilerplate**.

**The rule:** reuse content as-is **only if it fits the new scope, audience, and purpose.** If
any of those changes, adapt it.

- **Repurpose for the context.** A product spec page informs; a sales proposal persuades.
  When moving text between them, rework its tone, tense, voice, and point of view for the
  new job.
- **Repurpose for the medium.** Solid blocks of text that read fine in a brochure need
  breaking into short paragraphs and lists on screen, because people process on-screen text
  differently. Adapt the layout and design to the medium.
- **Ethics.** An organization can reuse its own content freely, since it owns it.
  Public-domain material is free to reuse, and Creative Commons material can be reused on
  its license's terms, with attribution. In school, reusing anyone's words or ideas without
  credit is still plagiarism.

## 9. Current-practice notes (this skill's own)

Web practice changes quickly; check specifics against current guidance.

- **Search:** Google's own *Search Engine Optimization (SEO) Starter Guide* is the place to
  start.
- **Keywords, not keyword stuffing.** Search engines penalize repeated, unnatural keywords.
  Use the reader's own words naturally in the title, first paragraph, and headings.
- **Title tag and meta description.** Each page gets a unique, descriptive title (roughly
  60 characters) and a one-sentence summary (roughly 155 characters); together they are the
  search-result listing.
- **Accessibility (WCAG).**
  - Alt text on every meaningful image.
  - Link text that makes sense out of context ("2026 annual report (PDF)", never "click
    here").
  - Headings nested in order (H1, then H2, then H3), not chosen for size.
  - Text contrast of at least 4.5 to 1 against the background.
  - Never color alone to carry meaning.
- **Mobile first.** Most visits are on phones; check every page at phone width.

**Finance additions.**

- **Company websites and Reg FD.** The SEC's 2008 guidance lets a company's website count as
  public disclosure only if investors know it's a recognized channel for that information.
  Material news still usually goes out by press release and 8-K first.
- **Investor-relations pages:** date-stamp every figure ("as of September 30, 2026"); link
  the filing, not a summary of it; label non-GAAP measures and link the reconciliation; keep
  the safe-harbor statement next to any forward-looking content; archive old presentations
  rather than editing them.
- **Reading a company site as an investor:** the IR page is promotional. Trust the filings it
  links to over the page copy.

## 10. Easy to confuse

- **Internal vs. external links:** internal ones move around your site and stay unmarked;
  external ones leave it and are labeled.
- **Content management vs. document management:** a content-management system builds and displays content on a site or in final documents; a
  document-management system tracks one document's whole life cycle (versions, contributors,
  check-out and lock, metadata search).
- **Single-file version vs. PDF:** one is a long web page made for printing; the other is a
  fixed-layout copy of the print document.
- **FAQ vs. help article:** an FAQ answers many common questions briefly; a help article walks
  through one task in steps.
- **Repurposing vs. plagiarism:** reusing your organization's own content is repurposing;
  reusing someone else's without permission and credit is not.

## 11. Before it goes live

- [ ] Web policy checked with the webmaster or manager
- [ ] Main point in the first lines; one facet per short paragraph
- [ ] Informative headings; lists with explanatory text around them
- [ ] Keywords in the first ~50 words of each topic, used naturally
- [ ] No "next page", "above", or "below"; Back to Top on long pages
- [ ] Links tested; outside sites vetted, deep-linked, labeled, and explained
- [ ] Images optimized and licensed, with alt text; sans serif body text; no all-caps blocks
- [ ] Revised documents carry a notice of changes; PDF or single-file version offered if
      readers will print
- [ ] Sources recorded and credited; content consistent with the privacy statement
- [ ] International dates, times, and units; no idioms
- [ ] Finance pages date-stamped, filings linked, non-GAAP reconciled
- [ ] Proofread (`grammar-and-mechanics`)

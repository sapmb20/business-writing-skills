---
name: visuals
description: "Choose, build, and integrate visuals in business documents and decks — matching the visual to the job (tables for exact comparison; line, bar, pie, and picture graphs for trends, comparisons, and shares; Gantt charts for schedules; flowcharts for processes; organizational charts for hierarchy; drawings, photographs, and maps for appearance and place; infographics for wide audiences), the anatomy of a table (number, title, box head, stub, body, rules, footnotes, source line, continued tables, informal tables), graph rules by type (zero point, scale breaks, equal intervals, no 3-D, pie wedges clockwise from 12 o'clock), integrating visuals with text (refer before you show, figure vs. table numbering, captions, source lines, lists of figures), visual ethics (distorted scales, omitted data, permissions), and global graphics. Includes labeled finance-chart conventions. Part of the business-writing family. Use when deciding whether and how to chart or tabulate data, building a table or chart for a report, memo, or slide, reviewing someone's charts, or checking a chart for misleading scales."
---

# Visuals

Visuals turn abstract ideas and relationships into concrete ones. A visual can show what
something looks like (drawings, photographs, maps), represent quantities (graphs, tables),
show a process or relationship (flowcharts, Gantt charts, infographics), or show a
hierarchy (organizational charts). The qualities of good writing apply to visuals too:
simplicity, clarity, concision, directness. **No visual works without context.** The text
around it says why it is there and what to see in it.

Sources: standard data-visualization and technical-writing practice (see ATTRIBUTION.md at
the repo root). The finance conventions in section 5 and the "easy to confuse" list are this
skill's own, labeled as such.

## When to Use

- Deciding whether data belongs in text, a table, or a chart, and which chart
- Building a table or chart for a report, memo, proposal, or slide
- Placing, numbering, captioning, and citing visuals in a document
- Reviewing a chart for clarity or for a misleading scale
- Choosing images and symbols for an international audience

**Where it sits in the family.** `business-writing` decides at outlining (step 4) where
visuals go. `reports-and-proposals` and `memo-writing` use them in the body.
`presentations` has its own slide rules (one message per slide, six objects at most),
which apply on top of these. To render a chart in code or an artifact, load `dataviz`
if it is installed. This skill decides *what* to show; `dataviz` decides how it looks.

---

## 1. Choose the visual by its job

Choose for the audience and the purpose. An owner's manual and a technician's diagnostic
guide need different illustrations of the same car. Note the options for visuals while
deciding the scope and organization.

| To show... | Use | Why |
| --- | --- | --- |
| Exact values for item-to-item comparison | **Table** | Precise, but trends are hard to see |
| A trend over time; two series over the same period | **Line graph** (double-line, shading the gap to stress the difference) | Movement and cycles are obvious |
| Quantities of different items at one time, or one item at different times | **Bar graph** (horizontal or vertical) | Lengths are easy to compare |
| Parts of a whole, across several items | **Segmented bar (column) graph**; the segments total 100% | Shows composition side by side |
| Parts of a single whole | **Pie graph** | Quick to read, but less precise than a table; often paired with one |
| Quantities for a wide audience | **Picture graph** (one symbol = a fixed quantity) | Adds interest; state the total |
| A project schedule | **Gantt chart** (tasks down the side, time across the top, bars for start and end, an optional owner column) | Plans and tracks the status of a project |
| The stages of a process | **Flowchart** (labeled blocks, pictorial symbols, or ISO symbols) | Shows the steps at a glance |
| Lines of authority | **Organizational chart** (one box per unit, linked to a central authority; names only if readers need them) | Shows the hierarchy |
| How something looks or fits together | **Drawing** (conventional line, exploded view, cutaway) | Can omit the irrelevant and show what a photo can't |
| Real appearance and human interest | **Photograph** | Catches attention, but can't show internal workings |
| Location or geographic distribution | **Map** (scale, north arrow, legend) | Shows place |
| A complex subject for a broad audience | **Infographic** (text, numbers, icons, and graphs as one whole) | Explains what text or images alone can't |

**Graph or table?** A graph shows the shape of the data, while a table shows exact values. When
readers need both (investors usually do), give the graph and put the table beside it or in
an appendix.

---

## 2. Integrate the visual with the text

1. **Plan visuals at the outline stage.** At each point where one belongs, sketch it or write
   "[illustration of ...]" with its source.
2. **Introduce it in the text before it appears.** Place it as close as possible *after* its
   first mention. No visual precedes its first mention.
3. **Say why it's there** and what to notice. Nonexperts need more explanation than experts.
4. **Call graphics "figures" and tables "tables,"** and refer to each by number ("Figure 3
   shows...").
5. **Number** each kind consecutively if the document has more than one. Give each a concise
   descriptive title or caption.
6. **Long or detailed visuals go in an appendix**, referred to from the body.
7. **More than five figures or tables:** add a List of Figures or List of Tables after the
   table of contents.
8. **Follow the house style** or the publication's style manual when there is one.

### Making any visual

- Keep it simple. Include only what the text discusses, and remove extra labels, arrows,
  boxes, and lines.
- Keep lettering horizontal, with white space inside and around the visual.
- State the units, make relative sizes clear, and add a scale where distance matters.
- Use the same terms as the text. If the text says "percentage," the visual doesn't say
  "proportion."
- Define abbreviations at first use in both the text and the visual, and label any symbol
  that isn't self-explanatory.

---

## 3. Tables

A table lays out data in parallel rows and columns for precise comparison.

| Element | Rule |
| --- | --- |
| **Table number** | Above the table, numbered in sequence through the document |
| **Title** | Just above the table, concisely describing its content |
| **Box head** (column headings) | Brief but descriptive. Units go in the heading or in parentheses beneath it. Standard abbreviations are fine. No vertical or diagonal lettering |
| **Stub** (left column) | The items the table gives information about |
| **Body** | Put the items to be compared in **adjacent** rows and columns. For a missing value, use a dash or a row of dots, never a blank |
| **Rules** | Top and bottom borders, and a rule between the headings and the body. Sides may be open. Use vertical rules only if they aid clarity |
| **Footnotes** | Mark with symbols (\*, †) or lowercase letters, **not numbers**, which could be mistaken for data or for text footnotes |
| **Source line** | Below the table (many organizations put it below the footnotes) |
| **Continued tables** | Repeat the column headings, number, and title with "continued" on each new page |

**Informal tables.** A few items that read more easily as columns than as running text can
go in an informal table with no number or title. Introduce it properly, and give it accurate
column headings.

---

## 4. Graphs

**For every graph:**

- Title it precisely and briefly, saying what it shows.
- Use a legend whenever there are symbols or more than one series.
- Credit outside data in a source line beneath the graph.
- Place any explanatory note right under the caption.

**Line graphs:**

- Show the zero point where the axes meet. If starting at zero is impractical, show a
  **break in the scale** rather than silently starting higher.
- Space the vertical axis in equal steps, rising from zero (or the lowest value) to the
  highest. Quantities go on the vertical axis.
- Divide the horizontal axis into equal, labeled units, left to right. Time usually runs
  along the horizontal axis.
- Keep lettering horizontal, except the vertical axis label.

**Bar graphs:**

- Bars are equal in width and scaled in length.
- Tell series apart by color or pattern, and explain them in a legend.
- Segments of a part-of-whole bar total 100%.
- **Avoid 3-D**, which makes bars look bigger than their values.

**Pie graphs:**

- The whole circle is 100%.
- Order the wedges **clockwise from 12 o'clock, largest to smallest**.
- Limit the number of wedges so each is thick enough to read.
- Give each wedge a distinct color or pattern and a percentage label, with callouts kept
  horizontal.
- Pull one wedge out to emphasize it.

**Picture graphs:**

- Use recognizable symbols, each standing for the **same** number of units.
- Show bigger quantities with **more** symbols, not bigger symbols, because relative size is
  hard to judge.
- State the total after the symbols.

**Ethics: scales.** Proportion both axes so the data appear without distortion. Squeezing
one axis, or dropping some years from a returns chart, can turn a steady trend into an
apparent slump and rebound. A visual that misleads is unethical, damages your
and your organization's credibility, and can bring lawsuits. Selectively omitting data is
the same offense.

---

## 5. Finance charts (this skill's own)

The rules above, applied to the charts a finance reader sees most:

- **Units in the title or axis**, stated once: "Revenue ($M)," "FY2021-FY2025." Say whether
  years are **fiscal or calendar** years.
- **Equal time intervals.** Never skip a bad year. If the data have a gap, show it.
- **Bar charts of levels start at zero.** A truncated bar axis exaggerates differences.
  A line chart of prices or rates may start above zero, but say so (with a scale break or a
  labeled axis).
- **Returns over long periods:** index to 100 at a common start date, or use a log scale and
  label it. Raw price lines of differently priced assets aren't comparable.
- **Margins and growth rates** are percentages. Don't put them on the same axis as dollar
  amounts. Use a second labeled axis, or a separate panel.
- **Negative numbers** in tables go in parentheses, aligned on the decimal point, with the
  same number of decimals in a column.
- **Show the source** of every number (the 10-K, a data provider, or "author's estimates"),
  and label estimates as estimates.
- **One message per chart**, and put the message in the title when the medium allows ("Gross
  margin recovered to pre-2022 levels"), especially on slides.

---

## 6. Other visuals

In short:

- **Drawings:** show the object from the user's point of view, in proportion, with any
  enlargement noted. A sequence of drawings runs left to right or top to bottom. Label the
  parts, or use a key.
- **Flowcharts:** label every step. Flow runs left to right and top to bottom, with arrows for
  any other direction. Add a key for unfamiliar symbols. Use ISO 5807 symbols for
  information-processing flows.
- **Maps:** a figure number and title, only the boundaries and features that matter, a scale,
  a north arrow, emphasis through color or shading, and a legend.
- **Photographs:** a figure number, callouts, and a caption readable from the same
  orientation. Get permission and a source line for photos you didn't take, a license for
  stock images, and consent from anyone pictured.
- **Infographics:** self-explanatory images in process order, current icons, culturally
  neutral images for international readers, consistent branding, and cited sources.

**Permissions (all visuals).** Get written permission to publish copyrighted visuals,
including images from websites. Credit borrowed material in a source line under a figure's
caption, or in a footnote under a table. Public-domain data (such as government statistics)
still gets a source line.

**Global graphics.** Symbols, gestures, and colors carry cultural meanings. A cross can read
as a religious symbol, which is why the Red Cross movement also uses a red crescent. For international readers:

- Test the visuals with people from the audience.
- Check the reading direction.
- Avoid unintended political or religious meanings.
- Depict people with neutral outlines or stick figures.
- Prefer neutral colors or gray scale.
- Don't rely on punctuation as a symbol (a "?" for help).
- Explain any icon you can't change, such as a logo.

---

## 7. Easy to confuse

- **Figure vs. table:** a table is rows and columns of data. Everything else (graphs, charts,
  drawings, maps, photos) is a figure. Each has its own number sequence and its own list.
- **Table number placement vs. figure caption placement:** most styles (APA included) put a
  table's number and title *above* it. Figure source lines go *below* the figure.
- **Bar vs. column graph:** the same graph. "Column" usually means vertical bars, especially
  segmented ones.
- **Pie vs. segmented bar:** both show parts of a whole. A pie shows one whole; segmented bars
  compare the composition of several.
- **Scale break vs. truncated axis:** a break *shows* that the axis skips a range. A truncated
  axis hides it.
- **Gantt chart vs. flowchart:** a Gantt chart shows *when* tasks happen. A flowchart shows
  *in what order and through which decisions* a process runs.
- **Infographic vs. chart:** a chart shows one data set. An infographic combines several
  visuals and text into one explanation.

## 8. Delivering the help

- When recommending a visual, name the type, what goes on each axis or in each column, the
  title (with units), and the one-sentence point the text should make about it.
- When reviewing, list problems by severity: misleading scale or omitted data first, then
  missing context (title, units, source, text reference), then clutter.
- Never invent data to fill a chart. Bracket the missing values and say what is needed.

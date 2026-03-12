# Sample Variance Memo — PDF Format Notes

These notes define the intended PDF layout for converting the sample variance memo from markdown to a polished, board-ready document.

## Page Setup

- **Page size:** Letter (8.5 x 11 in)
- **Margins:** 1 inch all sides
- **Orientation:** Portrait
- **Font:** Sans-serif body (Inter, Helvetica, or Arial). Do not use serif fonts — finance memos should feel modern and clean, not academic.
- **Body text:** 10pt
- **Table text:** 9pt
- **Section headers:** 13pt bold
- **Subsection headers:** 11pt bold
- **Target length:** 4–6 pages including provenance section

## Header / Footer

- **Header:** Company name (left), "Monthly Variance Memo" (center), period (right)
- **Footer:** "DRAFT — Pending Finance QA Review" (left), page number (right), E-Solutions logo small (center, optional)
- **Header/footer font:** 8pt, light gray

## Section Hierarchy

The memo follows this fixed order. Every section should start with a brief summary sentence before diving into detail.

1. **Metadata block** — company, period, status, checkpoint ID, validation summary. Presented as a compact table or card at the top of page 1. This is not a title page — it is an info bar.
2. **Executive summary** — 2–3 sentences max. End with "Items requiring attention" as a bolded callout list.
3. **Topline performance** — two tables: P&L summary (Actual/Budget/Variance) and Key Operating Metrics (MoM). Use light background color on header row.
4. **Revenue variance detail** — one subsection per revenue line. Each includes a mini comparison table and bulleted drivers. Flag action items inline.
5. **Expense variance detail** — COGS first, then OpEx. Use the "Recurring?" column to help the reader separate noise from signal.
6. **Headcount** — simple table with variance notes column.
7. **Risks and watchouts** — table format with Risk, Exposure, and Trigger columns. Limit to 3–5 items.
8. **Recommended actions** — table format with Action, Owner, and Due Date columns. Limit to 3–5 items.
9. **Data provenance and audit trail** — table format. Include the "How to read this section" explainer for first-time readers. This section builds trust — do not hide it or shrink it.

## Table Formatting

- **Header rows:** Dark background (navy or charcoal), white text, bold
- **Alternating row shading:** Light gray on even rows for readability
- **Variance columns:** Use color coding — green text for favorable, red text for unfavorable. Apply to Var ($) and Var (%) columns only.
- **Signal column:** Use plain text (Favorable / Watch / On plan) — do not use emoji or icons
- **Alignment:** Numbers right-aligned, text left-aligned, headers left-aligned
- **Currency formatting:** $XXX,XXX with commas, no decimal places for amounts > $1,000

## Visual Design Choices That Matter

1. **The metadata block must be prominent.** Checkpoint ID and validation status should be the first thing a careful reader notices. This is a trust signal.
2. **Executive summary should be visually distinct.** Use a light background card or box. Two sentences of context + a bolded callout list of items requiring attention.
3. **Variance tables should be scannable.** The reader should be able to see favorable/unfavorable at a glance from color coding without reading the narrative.
4. **Recommended actions should feel like a task list.** Owner and date columns signal that the memo drives action, not just reporting.
5. **Data provenance should not be an afterthought.** Give it a full section with clear formatting. For E-Solutions, this section is a differentiator — it proves the memo is auditable.

## What Not To Do

- Do not use charts or graphs in v1. Tables with clear numbers are more trustworthy for finance audiences than bar charts. Charts can be added in v2 if design partners request them.
- Do not use a cover page. The memo should start immediately with the metadata block and executive summary. A cover page wastes space and signals "deck" not "memo."
- Do not use more than 2 colors beyond black/gray. The memo should feel sober and professional.
- Do not exceed 6 pages. If the memo is longer, the narratives are too verbose.

## Brand Elements (Minimal)

- **Logo:** Small E-Solutions logo in footer (center, grayscale). Do not use a large logo header.
- **Color palette:** Navy (#1a2332) for table headers, light gray (#f5f5f5) for alternating rows, green (#2d7a3a) for favorable variances, red (#c0392b) for unfavorable variances.
- **No taglines or marketing copy in the memo.** The memo is a deliverable, not a brochure.

## Conversion Notes

For initial PDF conversion, use one of:
- **Pandoc** with a custom LaTeX or HTML template
- **Typst** for clean typesetting from markdown
- **Google Docs** with manual formatting (acceptable for first 1–2 deliveries)
- **Figma / Canva** only if a designed template is needed for a specific prospect

The markdown source is the system of record. The PDF is a rendering. Do not maintain both independently.

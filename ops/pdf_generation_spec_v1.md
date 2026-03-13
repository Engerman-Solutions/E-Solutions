# PDF Generation Specification v1

**Purpose:** Define the PDF conversion approach for E-Solutions pilot-stage deliverables.

**Alignment:** `deliverables/sample_variance_memo_format_notes_v1.md` (visual spec)

---

## Conversion Method

**WeasyPrint** (Python library) via a shell script (`ops/generate_pdfs_v1.sh`).

Pipeline: Markdown → Python `markdown` library → HTML → CSS styling → WeasyPrint → PDF.

### Why WeasyPrint

| Consideration | WeasyPrint | Pandoc + LaTeX | Typst | Headless Chrome |
|---------------|-----------|----------------|-------|-----------------|
| Install complexity | `pip install weasyprint markdown` | Requires TeX distribution (1+ GB) | Separate binary | Already available but harder to style |
| CSS control | Full CSS including `@page` rules | Limited without custom templates | Own styling language | Full CSS but requires HTML scaffolding |
| Python integration | Native — runs in existing venv | Subprocess call | Subprocess call | Subprocess call |
| Table rendering | Good | Good | Good | Good |
| Page headers/footers | Yes via `@page` CSS | Yes via LaTeX | Yes | Requires print CSS |
| Maintenance | Low — pip dependency | High — TeX distribution updates | Low | Medium |

WeasyPrint is the simplest credible option that produces clean business PDFs from the existing Python environment. No additional system packages required beyond what `pip install` provides.

---

## Styling Approach

Two CSS stylesheets, one per document type:

### Variance Memo (`ops/memo_style.css`)
- Letter size, 1" margins
- Navy (#1a2332) table headers with white text
- Alternating row shading (#f5f5f5)
- Sans-serif body (Inter/Helvetica/Arial fallback) at 10pt, tables at 9pt
- Headers: 18pt h1, 13pt h2, 11pt h3
- Page header: company name (left), "Monthly Variance Memo" (center), period (right)
- Page footer: "DRAFT — Pending Finance QA Review" (left), "E-Solutions" (center), page number (right)
- Page break avoidance on tables and after headings

### Pilot Package (`ops/pilot_style.css`)
- Letter size, 0.85" top/bottom margins
- Same table styling as memo
- Slightly larger body text (10.5pt) for readability
- Subtitle styled as italic under h1
- Footer: "E-Solutions — Confidential" (center), page number (right)
- No page header — cleaner for a client-facing brief

---

## How Headers/Footers Work

WeasyPrint supports CSS `@page` rules with margin boxes (`@top-left`, `@bottom-right`, etc.). The content is set via the `content` property. Currently hardcoded to NovaCRM sample values. For production use with real customers, headers/footers will need to be dynamized — either by generating per-customer CSS or by using CSS custom properties.

---

## Memo-Specific Rendering Notes

- The metadata table at the top of the memo uses a CSS override to remove the dark header treatment (since it's a key-value layout, not a data table)
- The attention items currently render inline with the bold prefix rather than as a distinct numbered list — this is a markdown source structure issue, not a CSS issue. Minor cosmetic item for a future pass.
- `[VERIFY]` markers render as plain text. In a future version, these could be highlighted with a yellow background.

---

## Draft/Review/Final Status

- **Draft memos:** Footer reads "DRAFT — Pending Finance QA Review"
- **Approved memos:** Footer should be updated to "APPROVED" before final PDF generation
- **How to change:** Edit the `@bottom-left` content in `ops/memo_style.css`, or create a separate `memo_style_approved.css` variant

For the pilot, the operator manually updates the CSS before generating the final delivery PDF. This is acceptable at 1-2 memos/month scale.

---

## Provenance/Checkpoint Rendering

The Data Provenance and Audit Trail section renders as a standard table in the memo PDF. The checkpoint ID, validation status, and review chain are all visible. The "How to read this section" explainer renders as a bullet list below the provenance table.

---

## Dependencies

```
# In requirements.txt
weasyprint>=68.0
markdown>=3.6
```

Both install via `pip` into the existing venv. No system-level packages required on most Linux/macOS systems (WeasyPrint uses Pango/Cairo via system libraries that are typically pre-installed).

---

## Limitations

1. **Headers/footers are hardcoded** to NovaCRM sample values. Must be dynamized for real customer memos.
2. **No green/red variance coloring** in tables. WeasyPrint renders markdown tables without per-cell CSS classes. Adding color would require post-processing the HTML before PDF generation.
3. **No E-Solutions logo** in footer. Logo rendering requires an image file and path reference in CSS. Deferred until branding is finalized.
4. **Number alignment** is left-aligned in tables (markdown tables don't carry alignment metadata through the Python markdown library). Right-alignment would require HTML post-processing.
5. **Attention items** render as a single paragraph with inline numbers rather than a distinct numbered list. Source structure issue.

These are all resolvable with moderate effort. None block pilot use.

---

## Future Improvements (Not in Scope)

- Per-customer CSS generation (dynamic headers/footers)
- Variance color coding (green favorable / red unfavorable)
- Right-aligned number columns
- Logo in footer
- `[VERIFY]` marker highlighting
- Approved vs. Draft stylesheet variants
- A/B format testing with design partners

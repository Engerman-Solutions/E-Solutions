# Memo Assembly Specification v1

**Purpose:** Define how structured variance computation output and AI-generated narrative sections are combined into a draft markdown variance memo ready for QA review.

**Alignment:** Sits between narrative generation and QA review in the workflow. Produces output matching the format of `deliverables/sample_variance_memo_v2.md`.

---

## Inputs

The assembly script takes three JSON files:

### 1. Variance computation output (`--variance`)

Produced by `product/variance_computation_v1.py`. Contains `line_items`, `topline`, and `metadata`.

### 2. Narrative sections (`--narrative`)

Produced by AI narrative generation (Claude API or manual). Contains `executive_summary`, `attention_items`, `revenue_narratives`, `expense_narratives`, `cogs_summary`, `opex_summary`, `risks`, and `recommended_actions`.

### 3. Company context (`--context`)

A JSON file with company-specific metadata:

```json
{
  "company_name": "NovaCRM, Inc.",
  "period_display": "February 2026",
  "period_code": "2026-02",
  "prepared_by": "E-Solutions",
  "checkpoint_id": "VR-2026-02-0047",
  "memo_status": "DRAFT — Pending finance QA review",
  "validation_summary": "2026-03-05 09:14 UTC · 18 line items · Schema pass · Injection scan pass",
  "source_system": "QuickBooks Online",
  "gl_export_date": "2026-03-04",
  "budget_source": "Board-approved 2026 annual budget, v2.1",
  "prior_period_checkpoint": "VR-2026-01-0031",
  "coa_template": "coa-template-novaCRM, v1.2",
  "coa_template_hash": "a3f8c1d",
  "analysis_engine": "E-Solutions variance engine v0.1",
  "qa_reviewer": "Matt (provisional)"
}
```

---

## Output

A single markdown file following the structure of `deliverables/sample_variance_memo_v2.md`:

1. **Metadata block** — rendered from company context
2. **Executive summary** — from narrative output
3. **Topline performance table** — rendered from variance computation topline
4. **Revenue variance detail** — tables from variance data, drivers from narrative
5. **Expense variance detail** — tables from variance data, drivers from narrative (split into COGS and OpEx)
6. **Risks and watchouts** — from narrative output
7. **Recommended actions** — from narrative output
8. **Data provenance** — rendered from company context and computation metadata

---

## Section Rendering Rules

### Metadata Block
- Rendered as a 2-column markdown table
- All fields from company context
- Deterministic — no AI content

### Topline Performance Table
- Rendered from `topline` data in variance output
- Format amounts as `$XXX,XXX` with commas, no decimals for amounts > $1,000
- Variance dollars prefixed with `+` or `-`
- Variance percentages as `+X.X%` or `-X.X%`
- Include Signal column

### Revenue Variance Detail
- One subsection per revenue line item where `is_material: true`
- Each subsection has:
  - Header: `### {account_name}: {+/-}{variance_dollars} vs. budget ({variance_percent}%)`
  - Mini comparison table (Actual / Budget / Prior Mo.)
  - Drivers from narrative output (bulleted list)
  - Context sentence if provided in narrative
  - Action required if specified in narrative

### Expense Variance Detail
- Split into COGS and OpEx sections
- COGS: table with all COGS line items, followed by narrative drivers for material items
- OpEx: split into Favorable and Unfavorable sub-tables, followed by narrative drivers
- Include `Recurring?` column from narrative output

### Risks and Watchouts
- Rendered as a numbered table: Risk / Exposure / Trigger
- 3-5 items from narrative output

### Recommended Actions
- Rendered as a numbered table: Action / Owner / By
- 3-5 items from narrative output

### Data Provenance
- Rendered as a 2-column table from company context and computation metadata
- Includes "How to read this section" explainer
- Deterministic — no AI content

---

## Number Formatting

| Type | Format | Example |
|------|--------|---------|
| Dollar amounts > $1,000 | `$XXX,XXX` | `$412,800` |
| Dollar amounts < $1,000 | `$XXX` | `$800` |
| Variance dollars | `+$XX,XXX` or `-$XX,XXX` | `+$17,800` |
| Percentages | `+X.X%` or `-X.X%` | `+4.5%` |
| Margin points | `+X.X pts` or `-X.X pts` | `-0.3 pts` |

---

## CLI Usage

```bash
# Assemble memo from all three inputs
python product/assemble_memo_v1.py \
  --variance output/variance_output.json \
  --narrative output/narrative_output.json \
  --context config/company_context.json \
  --output deliverables/generated_memo_draft.md

# Assemble with placeholders (no narrative file — inserts [NARRATIVE NEEDED] markers)
python product/assemble_memo_v1.py \
  --variance output/variance_output.json \
  --context config/company_context.json \
  --output deliverables/memo_skeleton.md
```

---

## Dependencies

- Python 3.10+
- Standard library only (`json`, `argparse`, `pathlib`)
- No pandas required — the assembly script reads pre-computed JSON

---

## What This Does Not Cover

- PDF conversion (separate step — see `deliverables/sample_variance_memo_format_notes_v1.md`)
- Headcount section (requires external data — manual entry during pilot)
- Key operating metrics beyond topline (MRR, burn multiple require external input)
- Automated narrative generation (handled by separate workflow using prompts)

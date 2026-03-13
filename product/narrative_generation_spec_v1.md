# Narrative Generation Specification v1

**Purpose:** Define the AI-assisted narrative generation step that transforms structured variance computation output into draft memo text sections ready for human QA review.

**Alignment:** Stage 4 (narrative portion) of `ops/live_pilot_workflow_v1.md`, DEC-008 (human-in-loop), DEC-011 (AI + human hybrid)

---

## Where This Step Sits in the Workflow

```
Upload → Validate → Map → Compute → [GENERATE NARRATIVE] → Assemble → Review → Approve → Deliver
                                      ^^^^^^^^^^^^^^^^^^^^
```

Narrative generation occurs after variance computation produces structured JSON output and before memo assembly combines data and narrative into a draft markdown document. The generated narrative is always a draft — it must pass human QA review before delivery.

---

## Inputs

### Required

1. **Variance computation output** (`variance_output.json`) — produced by `product/variance_computation_v1.py`. Contains:
   - `line_items`: per-account variance detail with materiality flags and signals
   - `topline`: aggregated performance summary
   - `metadata`: period, row count, thresholds, computation timestamp

2. **Company context** — provided as part of the narrative input JSON. Contains:
   - Company name, period, stage
   - Checkpoint ID, source system, GL export date
   - Budget source, COA template version
   - Validation results summary

### Optional

3. **Prior period narrative** — if available, the prior month's narrative sections for trend continuity
4. **Customer notes** — any context the customer provides about expected variances (e.g., "We had a one-time legal expense for our Series B")

---

## What the AI Generates vs. What Is Deterministic

| Memo Section | Source | Method |
|-------------|--------|--------|
| Metadata block | Company context + validation data | **Deterministic** — template rendering |
| Executive summary | Topline + material variances | **AI-generated** — synthesizes key findings |
| Attention items | Material variances + signals | **AI-generated** — identifies 2-3 items requiring leadership action |
| Topline performance table | Variance computation output | **Deterministic** — data insertion |
| Key operating metrics | Variance computation + external data | **Partially deterministic** — MRR derived from subscription revenue; headcount, burn multiple need external input or manual entry |
| Revenue variance tables | Variance computation output | **Deterministic** — data insertion |
| Revenue variance drivers | Material revenue variances | **AI-generated** — explains each material variance |
| Expense variance tables | Variance computation output | **Deterministic** — data insertion |
| Expense variance drivers | Material expense variances | **AI-generated** — explains each material variance |
| Headcount table | External input | **Manual** — not derivable from GL data alone |
| Risks and watchouts | Material variances + trends | **AI-generated** — identifies forward-looking risks |
| Recommended actions | Risks + material variances | **AI-generated** — suggests concrete actions |
| Data provenance | Company context + validation data | **Deterministic** — template rendering |

---

## AI Generation Constraints

### Must

- Ground every numeric reference in the variance computation output — no invented numbers
- Reference specific account names and dollar amounts from the data
- Produce narrative appropriate for a board audience — concise, professional, no jargon overload
- Flag items as favorable or unfavorable consistently with the signal assignments
- Identify when a variance is likely non-recurring vs. structural
- Include action items only for material variances that warrant attention

### Must Not

- Invent causal explanations not supported by the data (e.g., "due to market conditions" when no market data was provided)
- Hallucinate specific details (customer names, project names, dates) unless provided in customer notes
- Use speculative language presented as fact ("this will likely lead to...")
- Generate generic boilerplate ("the company continues to perform well...")
- Contradict the variance computation numbers
- Exceed the scope of the data — no forecasting, no recommendations outside the current period

### Should

- Use placeholder markers like `[VERIFY: specific detail needed]` when the data suggests a driver but lacks confirming context
- Note when prior-period trend data supports or contradicts the current variance
- Keep each driver explanation to 1-2 sentences
- Limit risks to 3-5 items and recommended actions to 3-5 items
- Use the `Recurring?` classification for expense items (Yes / No / Partially / Timing / TBD)

---

## Output Format

The narrative generation step produces a JSON file (`narrative_output.json`) with the following structure:

```json
{
  "executive_summary": "string — 2-3 sentences summarizing the period",
  "attention_items": ["string — item requiring leadership attention"],
  "revenue_narratives": {
    "account_code": {
      "drivers": ["string — bullet point explaining the variance"],
      "context": "string — optional additional context or trend note",
      "action_required": "string or null — action item if warranted"
    }
  },
  "expense_narratives": {
    "account_code": {
      "drivers": ["string — bullet point explaining the variance"],
      "context": "string — optional additional context",
      "action_required": "string or null",
      "recurring": "string — Yes / No / Partially / Timing / TBD"
    }
  },
  "cogs_summary": "string — 1-2 sentences on overall COGS position and gross margin",
  "opex_summary": "string — 1-2 sentences on overall OpEx position",
  "risks": [
    {
      "risk": "string — description of the risk",
      "exposure": "string — estimated financial impact",
      "trigger": "string — what would cause this risk to materialize"
    }
  ],
  "recommended_actions": [
    {
      "action": "string — specific action to take",
      "owner": "string — role responsible",
      "by_date": "string — target date"
    }
  ]
}
```

See `product/narrative_output_schema_v1.json` for the formal JSON schema.

---

## Model Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Model | Claude Sonnet (claude-sonnet-4-6) | Best balance of quality, speed, and cost for structured financial text |
| Temperature | 0.3 | Low temperature for factual, consistent output |
| Max tokens | 4000 | Sufficient for all narrative sections |
| System prompt | `prompts/variance_memo_system_prompt_v1.md` | Establishes role, constraints, output format |
| User prompt | `prompts/variance_memo_user_prompt_v1.md` (template) | Filled with variance data and company context |

### Fallback

If the primary model is unavailable or output quality is poor:
1. Retry once with the same prompt
2. If still poor, switch to Claude Opus (claude-opus-4-6) for higher quality
3. If API is down, use manual Claude chat with the same prompts — paste the system prompt and user prompt into a Claude conversation
4. As a last resort, the operator writes the narrative sections manually using the variance data

---

## Quality Assessment

Before passing the narrative to memo assembly, the operator should check:

1. **Numeric accuracy** — spot-check 2-3 numbers in the narrative against the variance JSON
2. **No hallucination** — no specific details (names, dates, projects) that are not in the input data or customer notes
3. **Tone** — board-appropriate, not generic AI fluff
4. **Completeness** — all material variances have narrative explanations
5. **Placeholder markers** — any `[VERIFY]` markers are noted for the QA reviewer

If the narrative fails quality assessment, re-run with adjusted prompts or edit manually before proceeding to assembly.

---

## Human Review Interaction

The generated narrative is a draft. The QA review step (Stage 5 in the workflow) checks:

1. Numbers in narrative match source data
2. Causal explanations are reasonable (not hallucinated)
3. Tone and language are board-appropriate
4. No material variances are unaddressed
5. Risks and actions are realistic and specific

The QA reviewer (provisionally Matt during the pilot) marks issues as "must fix" or "suggestion" and returns the annotated draft. The `prompts/variance_memo_review_prompt_v1.md` can assist the reviewer in structuring their review.

---

## What This Spec Does Not Cover

- Headcount narrative (requires external data — entered manually during pilot)
- Key operating metrics beyond what is derivable from GL data
- Multi-period trend analysis beyond single prior period comparison
- Customer-provided context integration (planned for Cycle 2+)
- Automated quality scoring of generated narrative

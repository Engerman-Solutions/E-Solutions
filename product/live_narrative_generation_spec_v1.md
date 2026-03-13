# Live Narrative Generation Specification v1

**Purpose:** Define how the E-Solutions pipeline calls a live AI model to generate variance memo narrative sections, replacing the static fixture used in TICKET-005 testing.

**Alignment:** `product/narrative_generation_spec_v1.md` (parent spec), DEC-016 (Claude Sonnet structured prompts), `ops/run_narrative_workflow_v1.md` (operator instructions)

---

## Integration Approach

The live generation path uses the **Anthropic Python SDK** (`anthropic` package) to call the Claude Messages API directly. This is a direct API integration — no intermediary frameworks, no LangChain, no orchestration layer.

**Why direct API:** At pilot scale (1-2 customers, 1-2 memos/month), a simple script that calls the API, validates output, and saves artifacts is the right level of complexity. Orchestration frameworks add no value and obscure what is happening.

---

## Model Configuration

| Parameter | Value | Source |
|-----------|-------|--------|
| Primary model | `claude-sonnet-4-6` | DEC-016 |
| Fallback model | `claude-opus-4-6` | narrative_generation_spec_v1.md |
| Temperature | 0.3 | DEC-016 |
| Max tokens | 4096 | Sufficient for all narrative sections |
| System prompt | `prompts/variance_memo_system_prompt_v1.md` | Loaded at runtime |
| User prompt | `prompts/variance_memo_user_prompt_v1.md` (rendered) | Template filled with input data |

---

## Authentication

The script reads `ANTHROPIC_API_KEY` from:
1. `.env` file in the repo root (via `python-dotenv`), or
2. Environment variable

The `.env` file is gitignored and must never be committed.

---

## Script: `product/generate_narrative_v1.py`

### CLI Usage

```bash
# Standard generation (Claude Sonnet)
python product/generate_narrative_v1.py \
    --input output/narrative_input.json \
    --output output/narrative_output.json

# With fallback to Opus if Sonnet fails
python product/generate_narrative_v1.py \
    --input output/narrative_input.json \
    --output output/narrative_output.json \
    --fallback

# Dry run — render prompts, save to artifacts, no API call
python product/generate_narrative_v1.py \
    --input output/narrative_input.json \
    --dry-run

# Custom artifacts directory
python product/generate_narrative_v1.py \
    --input output/narrative_input.json \
    --output output/narrative_output.json \
    --artifacts-dir output/artifacts
```

### What the Script Does

1. **Load input** — reads the structured narrative input JSON (variance data + company context)
2. **Render prompts** — loads system prompt markdown and fills user prompt template with actual data (topline JSON, material line items, metadata)
3. **Create audit directory** — timestamped folder under `output/artifacts/run_YYYYMMDD_HHMMSS/`
4. **Save pre-call artifacts** — narrative input, rendered system prompt, rendered user prompt
5. **Call API** — sends messages to Claude via the Anthropic SDK
6. **Parse response** — extracts JSON from model output, handles code fence wrapping
7. **Validate structure** — checks all required keys, types, enums, and minimum counts against the output schema
8. **Save post-call artifacts** — raw response text, usage metadata, validation results
9. **Write output** — validated narrative JSON to the specified output path

### Retry and Fallback Behavior

| Scenario | Behavior |
|----------|----------|
| API call succeeds, JSON valid, schema valid | Use output, save artifacts |
| API call succeeds, JSON parse fails | Retry once on same model |
| API call succeeds, schema validation fails | Retry once on same model |
| Retry fails on primary model | If `--fallback`, try Opus; otherwise exit with error |
| Opus also fails | Exit with error, save all artifacts |
| API error (rate limit, auth, network) | Retry once, then fallback or exit |

Maximum attempts with `--fallback`: 4 (Sonnet x2, Opus x2).

### Output Validation

The script validates the generated JSON against the structure defined in `product/narrative_output_schema_v1.json`:

- All 6 required top-level keys present
- `executive_summary` is a non-trivial string
- `attention_items` is a non-empty list
- `revenue_narratives` and `expense_narratives` are objects with `drivers` arrays
- `expense_narratives` entries have valid `recurring` enum values
- `risks` has 2-5 entries with `risk`, `exposure`, `trigger` fields
- `recommended_actions` has 2-5 entries with `action`, `owner`, `by_date` fields

Validation is structural — it does not check numeric accuracy. Numeric accuracy is the operator's quality check and Matt's QA review responsibility.

---

## Dry Run Mode

`--dry-run` renders prompts and saves them to the artifacts directory without calling the API. Use this to:

- Inspect rendered prompts before spending API credits
- Prepare prompts for manual Claude chat (copy/paste fallback)
- Test the prompt rendering pipeline without API access

---

## Operator Intervention Points

| Step | Operator Required? | When |
|------|-------------------|------|
| Prepare narrative input JSON | Yes — run variance computation first | Before generation |
| Run generation script | Yes — execute CLI command | Generation |
| Inspect output quality | Yes — review narrative for accuracy, tone | After generation |
| Fix [VERIFY] markers | Yes — confirm or fill in details with customer | After generation |
| Re-run if quality is poor | Yes — decide to retry, edit, or escalate | After quality check |

The generation script is a tool, not an autonomous agent. The operator decides whether the output is usable.

---

## What This Spec Does Not Cover

- Multi-tenant orchestration (out of scope for pilot)
- Automated quality scoring (future)
- Cost tracking per customer (manual during pilot)
- Prior period narrative loading (deferred to Cycle 2+)
- Streaming API responses (unnecessary at this scale)

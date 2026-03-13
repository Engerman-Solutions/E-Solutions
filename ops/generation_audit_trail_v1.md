# Generation Audit Trail v1

**Purpose:** Define how narrative generation runs are logged and what artifacts are preserved for auditability, reproducibility, and QA review.

**Alignment:** DEC-009 (trust and auditability), `product/live_narrative_generation_spec_v1.md`

---

## Artifact Directory Structure

Each generation run creates a timestamped directory:

```
output/artifacts/
└── run_20260312_143022/
    ├── narrative_input.json              # Exact input payload sent to generation
    ├── rendered_system_prompt.md         # System prompt as sent to the model
    ├── rendered_user_prompt.md           # User prompt after template rendering
    ├── raw_response_attempt_1.txt        # Raw model output text (attempt 1)
    ├── usage_attempt_1.json             # Token usage and model info (attempt 1)
    ├── validated_narrative_output.json   # Final validated JSON output
    └── run_metadata.json                # Run configuration and outcome summary
```

### On failure, additional artifacts may include:

```
    ├── error_attempt_1.txt              # Error details for failed attempt
    ├── validation_errors_attempt_1.json # Schema validation failure details
    ├── raw_response_attempt_2.txt       # Retry response
    └── usage_attempt_2.json             # Retry usage
```

---

## Artifact Descriptions

### `narrative_input.json`
Exact copy of the input payload. Allows reproducing the generation run. Contains variance computation output and company context but no API keys or credentials.

### `rendered_system_prompt.md`
The system prompt as loaded from `prompts/variance_memo_system_prompt_v1.md`. Preserved to capture the exact prompt version used — if prompts are updated between runs, the artifact shows what was actually sent.

### `rendered_user_prompt.md`
The user prompt template after all `{{PLACEHOLDER}}` values are filled with actual data. This is the exact text sent to the model as the user message. Useful for debugging prompt quality issues or reproducing the call in Claude chat.

### `raw_response_attempt_N.txt`
The raw text response from the model, before JSON parsing or validation. Preserved even on failure. Critical for diagnosing:
- JSON formatting issues (extra text, markdown wrapping)
- Content quality problems
- Hallucination patterns

### `usage_attempt_N.json`
Model usage metadata for each API call:
- `model`: exact model ID used
- `input_tokens`: prompt token count
- `output_tokens`: response token count
- `stop_reason`: why the model stopped (end_turn, max_tokens, etc.)

### `validated_narrative_output.json`
The final parsed and schema-validated JSON output. Only present on successful runs. This is the file that feeds into memo assembly.

### `run_metadata.json`
Summary of the entire run:
- Timestamp
- Input/output paths
- Model used (primary or fallback)
- Total attempts
- Success/failure status
- Final usage stats
- Error details (if failed)

---

## What Is NOT Stored

- **API keys** — never written to artifacts
- **Customer PII** — the sample data uses synthetic company data; real customer runs must follow the same pattern (PII is in the input data, not added by artifacts)
- **Intermediate parsing state** — only raw text and final parsed JSON

---

## Retention

During the pilot, all artifacts are retained in `output/artifacts/`. The `output/` directory is gitignored — artifacts live on the operator's machine, not in the repo.

For production, artifacts should be stored in a durable, access-controlled location (e.g., per-customer cloud storage bucket). This is out of scope for the pilot.

---

## How to Inspect a Run

1. Find the run directory: `ls output/artifacts/`
2. Check outcome: `cat output/artifacts/run_YYYYMMDD_HHMMSS/run_metadata.json`
3. Review raw model output: `cat output/artifacts/run_YYYYMMDD_HHMMSS/raw_response_attempt_1.txt`
4. Check validation: look for `validation_errors_attempt_*.json` files
5. Compare input to output: diff `narrative_input.json` against `validated_narrative_output.json`

---

## Reproducibility

To reproduce a generation run:
1. Copy the `narrative_input.json` from the run artifacts
2. Run: `python product/generate_narrative_v1.py --input <path_to_saved_input> --output <new_output_path>`

Note: Exact reproduction is not guaranteed because:
- Model behavior may change between API versions
- Temperature > 0 introduces sampling variance
- Model weights may be updated by Anthropic

The artifacts record what happened, not guarantee identical repetition.

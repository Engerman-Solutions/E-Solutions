# Live Generation Troubleshooting v1

**Purpose:** Quick reference for diagnosing and resolving issues with live AI narrative generation.

---

## Authentication Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| `ANTHROPIC_API_KEY not set` | Missing `.env` file or env var | Create `.env` in repo root with `ANTHROPIC_API_KEY=sk-ant-...` |
| `401 Unauthorized` | Invalid or expired API key | Verify key at console.anthropic.com; update `.env` |
| `403 Forbidden` | Key lacks permissions for the model | Check API plan supports `claude-sonnet-4-6`; contact Anthropic support |

## API Errors

| Symptom | Cause | Fix |
|---------|-------|-----|
| `429 Rate Limit` | Too many requests | Wait 60 seconds, re-run. The script retries once automatically. |
| `500/503 Server Error` | Anthropic API outage | Check status.anthropic.com; fall back to manual chat (Option B) |
| `Connection Error` | Network issue | Check internet connectivity; retry |
| `timeout` | Response took too long | Re-run; if persistent, try `--fallback` to use Opus |

## Output Quality Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| JSON parse error | Model output includes markdown wrapping or extra text | Script handles code fences automatically; check raw response in artifacts. If still failing, copy raw text and manually extract JSON. |
| Schema validation fails | Missing required keys or invalid enum values | Check `validation_errors_attempt_*.json` in artifacts. Re-run or manually fix the output JSON. |
| Generic boilerplate narratives | Insufficient context in input | Add `customer_notes` to narrative input JSON with specifics about expected variances |
| Hallucinated details | Model inventing names/dates | Re-run; if persistent, use `--fallback` for Opus or write those sections manually |
| Numbers do not match source data | Model rounding or misquoting | This is a quality check failure — edit the narrative JSON manually before assembly |
| Too few `[VERIFY]` markers | Model is over-confident about causes | Review carefully; add `[VERIFY]` markers manually where explanations assume context not in the data |
| Too many `[VERIFY]` markers | Expected behavior — model is being cautious | Resolve with customer context during review; this is working as designed |

## Artifact Inspection

To diagnose any issue, start here:

```bash
# Find the most recent run
ls -la output/artifacts/

# Check run outcome
cat output/artifacts/run_YYYYMMDD_HHMMSS/run_metadata.json

# See what the model actually returned
cat output/artifacts/run_YYYYMMDD_HHMMSS/raw_response_attempt_1.txt

# Check validation errors (if present)
cat output/artifacts/run_YYYYMMDD_HHMMSS/validation_errors_attempt_1.json

# Review rendered prompts (what was sent to the model)
cat output/artifacts/run_YYYYMMDD_HHMMSS/rendered_user_prompt.md
```

## Escalation Path

1. Re-run with same model → script does this automatically (1 retry)
2. Re-run with `--fallback` → tries Opus if Sonnet fails
3. Dry-run + manual chat → `--dry-run`, copy prompts to claude.ai
4. Manual narrative writing → use variance data as reference, follow schema structure

If generation consistently fails or produces unusable output, file a note in the run artifacts and proceed with manual writing. Do not delay delivery waiting for AI to cooperate.

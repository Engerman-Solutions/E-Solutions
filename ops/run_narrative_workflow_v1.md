# Operator Run Instructions — Narrative Workflow v1

**Purpose:** Step-by-step instructions for running the E-Solutions variance memo pipeline from validated data to draft memo output.

**Provisional QA reviewer:** Matt. Matt reviews all draft memos before delivery. This is a pilot-stage arrangement, not a permanent organizational dependency.

---

## Prerequisites

1. Python 3.10+ installed
2. Virtual environment set up with dependencies:

```bash
cd ~/Projects/E-Solutions
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Customer GL export file (CSV or Excel) available
4. Company context JSON file prepared (see `product/sample_company_context_v1.json` for template)

---

## Pipeline Steps

### Step 1: Validate the uploaded data

```bash
source .venv/bin/activate
python product/validation_checks_v1.py data/{customer}/gl_export.csv --period YYYY-MM --output output/validation_report.json
```

**Check:** Exit code 0 = PASS. Exit code 1 = FAIL.

If FAIL: Review the error list in the validation report. Notify the customer with specific issues and request a corrected re-upload. Do not proceed.

If PASS: Continue to Step 2.

### Step 2: Compute variances

```bash
python product/variance_computation_v1.py data/{customer}/gl_export.csv --pretty --output output/variance_output.json
```

**Check:** Open `output/variance_output.json` and verify:
- `metadata.row_count` matches expected line items
- `topline.total_revenue` and `topline.operating_income` look reasonable
- `metadata.material_items` > 0 (if zero, check materiality thresholds)

### Step 3: Prepare narrative input

Create or update the company context JSON file for this customer and cycle:

```bash
cp product/sample_company_context_v1.json config/{customer}_context.json
# Edit the file with actual company details, checkpoint ID, dates, etc.
```

The narrative input combines the variance output and company context. For the Claude API call, you will provide both files.

### Step 4: Generate narrative sections

**Option A: Claude API (preferred)**

Use the system prompt and user prompt templates to generate narrative sections:

1. Read `prompts/variance_memo_system_prompt_v1.md` — this is the system message
2. Read `prompts/variance_memo_user_prompt_v1.md` — this is the user message template
3. Fill the template placeholders with data from `output/variance_output.json` and `config/{customer}_context.json`
4. Send to Claude API (claude-sonnet-4-6, temperature 0.3)
5. Save the JSON response as `output/narrative_output.json`

Example API call (using the Anthropic Python SDK):

```python
import anthropic
import json

client = anthropic.Anthropic()

system_prompt = open("prompts/variance_memo_system_prompt_v1.md").read()
user_prompt = # ... fill the template with actual data ...

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4000,
    temperature=0.3,
    system=system_prompt,
    messages=[{"role": "user", "content": user_prompt}]
)

narrative = json.loads(response.content[0].text)
with open("output/narrative_output.json", "w") as f:
    json.dump(narrative, f, indent=2)
```

**Option B: Manual Claude chat**

1. Open claude.ai or Claude desktop app
2. Paste the system prompt as the first message
3. Paste the filled user prompt (with variance data and company context) as the second message
4. Copy the JSON response
5. Save as `output/narrative_output.json`

**Option C: Write narrative manually**

If AI output quality is insufficient, write the narrative sections manually using the variance data as reference. Follow the structure in `product/narrative_output_schema_v1.json`.

### Step 5: Review narrative quality (operator pre-check)

Before assembly, spot-check the narrative output:

- [ ] Open `output/narrative_output.json`
- [ ] Verify 2-3 dollar amounts match `output/variance_output.json`
- [ ] Check for hallucinated details (names, dates, projects not in the data)
- [ ] Confirm all material items have narratives
- [ ] Note any `[VERIFY]` markers — these need resolution or reviewer attention

If quality is poor: Re-run Step 4 with adjusted prompts, or edit the JSON manually.

### Step 6: Assemble the draft memo

```bash
python product/assemble_memo_v1.py \
  --variance output/variance_output.json \
  --narrative output/narrative_output.json \
  --context config/{customer}_context.json \
  --output deliverables/{customer}_memo_draft_YYYY-MM.md
```

**Check:** Open the output file and verify:
- Metadata block has correct company name, period, checkpoint ID
- Topline table numbers match the variance computation
- Revenue and expense sections have narrative drivers
- Risks and recommended actions are present
- Data provenance section is complete

### Step 7: QA review by Matt

1. Send the draft memo to Matt for review
2. Matt reviews using the checklist in `prompts/variance_memo_review_prompt_v1.md`:
   - Numeric accuracy (spot-check 3-5 numbers)
   - No hallucination
   - Completeness (all material variances addressed)
   - Tone and language (board-appropriate)
   - Provenance section complete
3. Matt marks issues as "must fix" or "suggestion"
4. Resolve all "must fix" items — edit the narrative JSON or memo markdown directly
5. Matt performs final review and marks as "QA Approved"
6. Log the review timestamp and approval in the memo metadata

### Step 8: Customer approval

1. Share the QA-approved memo with the customer (upload to Google Drive deliverables folder or send via email)
2. Customer reviews and either approves or requests changes
3. If changes requested: return to Step 4 or Step 6 depending on nature of changes
4. Log approval timestamp

### Step 9: Delivery

1. Convert approved markdown to PDF (using format notes in `deliverables/sample_variance_memo_format_notes_v1.md`)
2. Upload PDF to customer's Google Drive deliverables folder
3. Send delivery notification email
4. Log delivery in cycle tracking spreadsheet

---

## Quick Reference: File Locations

| File | Purpose |
|------|---------|
| `product/validation_checks_v1.py` | Validate uploaded GL data |
| `product/variance_computation_v1.py` | Compute variances from validated data |
| `product/assemble_memo_v1.py` | Assemble draft memo from data + narrative |
| `prompts/variance_memo_system_prompt_v1.md` | System prompt for AI narrative generation |
| `prompts/variance_memo_user_prompt_v1.md` | User prompt template for AI narrative generation |
| `prompts/variance_memo_review_prompt_v1.md` | Review checklist for QA reviewer |
| `product/sample_company_context_v1.json` | Template for company context file |
| `product/sample_narrative_input_v1.json` | Example of full narrative input |
| `product/sample_narrative_output_v1.json` | Example of expected narrative output |

---

## What to Do If Output Quality Is Weak

| Problem | Action |
|---------|--------|
| AI generates generic boilerplate | Add more specific data to the user prompt (e.g., MoM trends, customer notes) |
| AI invents details not in the data | Check that the system prompt is included; re-run with temperature 0.2 |
| Numbers in narrative do not match source | Re-run; if persistent, write those sections manually |
| Missing narratives for material items | Check that all material items are included in the user prompt input |
| `[VERIFY]` markers throughout | Expected — these flag areas where the AI needs confirmation. Resolve with customer context or leave for reviewer. |
| API returns an error or is unavailable | Fall back to Option B (manual Claude chat) or Option C (manual writing) |

---

## Sample Pipeline Run (Using Test Data)

```bash
# Activate environment
source .venv/bin/activate

# Step 1: Validate
python product/validation_checks_v1.py deliverables/sample_variance_data_v1.csv --period 2026-02

# Step 2: Compute
python product/variance_computation_v1.py deliverables/sample_variance_data_v1.csv --pretty --output output/variance_output.json

# Step 3-4: Use pre-built sample narrative
# (In production, generate via Claude API)

# Step 6: Assemble
python product/assemble_memo_v1.py \
  --variance output/variance_output.json \
  --narrative product/sample_narrative_output_v1.json \
  --context product/sample_company_context_v1.json \
  --output deliverables/generated_memo_draft_v1.md

# Review the output
cat deliverables/generated_memo_draft_v1.md
```

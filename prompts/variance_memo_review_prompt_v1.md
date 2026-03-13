# Variance Memo Review Prompt v1

Use this prompt when reviewing a generated memo draft for QA. This can be used by the human QA reviewer directly, or as an AI-assisted pre-review step.

---

Review the following variance memo draft against the source data below. Your job is to verify accuracy, flag issues, and assess board-readiness.

## Source Data

### Variance Computation Output

```json
{{VARIANCE_OUTPUT_JSON}}
```

### Company Context

- **Company:** {{COMPANY_NAME}}
- **Period:** {{PERIOD_DISPLAY}}

## Memo Draft to Review

{{MEMO_DRAFT_MARKDOWN}}

## Review Checklist

For each item, mark as PASS, MUST FIX, or SUGGESTION:

### 1. Numeric Accuracy
- [ ] Spot-check 3-5 dollar amounts in the narrative against the source data
- [ ] Verify all variance percentages are correct
- [ ] Verify topline aggregations (revenue - COGS = gross profit, gross profit - OpEx = operating income)
- [ ] Check that signal labels (Favorable/Unfavorable/Watch/On plan) match the data

### 2. No Hallucination
- [ ] No specific project names, customer names, or dates that are not in the source data or customer notes
- [ ] No causal explanations that cannot be supported by the variance data
- [ ] Any `[VERIFY]` markers are flagged for operator resolution

### 3. Completeness
- [ ] All material variances have narrative explanations
- [ ] Executive summary covers revenue, expenses, and operating income
- [ ] Attention items are specific and quantified
- [ ] Risks section has 3-5 items with exposure estimates
- [ ] Recommended actions have owners and target dates

### 4. Tone and Language
- [ ] Board-appropriate — concise, direct, professional
- [ ] No generic AI filler ("it's worth noting", "as we can see")
- [ ] No speculative claims presented as fact
- [ ] Consistent use of Favorable/Unfavorable terminology

### 5. Structure and Formatting
- [ ] Memo follows the standard section order
- [ ] Tables are correctly formatted
- [ ] Data provenance section is complete
- [ ] Checkpoint ID and validation status are present

## Output

List each issue found with:
- **Section:** which part of the memo
- **Severity:** MUST FIX or SUGGESTION
- **Issue:** what is wrong
- **Fix:** what should change

If no issues are found, state: "Review complete. No issues found. Memo approved for customer review."

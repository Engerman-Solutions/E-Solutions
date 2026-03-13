# Variance Memo User Prompt v1

This is a template. Replace `{{PLACEHOLDER}}` values with actual data before sending to the model.

---

Generate the narrative sections for a monthly variance memo using the data below.

## Company Context

- **Company:** {{COMPANY_NAME}}
- **Period:** {{PERIOD_DISPLAY}} ({{PERIOD_CODE}})
- **Stage:** {{COMPANY_STAGE}}
- **Accounting system:** {{ACCOUNTING_SYSTEM}}

## Variance Data

### Topline Performance

```json
{{TOPLINE_JSON}}
```

### Line Items (material variances only)

```json
{{MATERIAL_LINE_ITEMS_JSON}}
```

### Computation Metadata

- Period: {{PERIOD_CODE}}
- Total line items: {{ROW_COUNT}}
- Material items: {{MATERIAL_COUNT}}
- Materiality thresholds: >${{THRESHOLD_DOLLARS}} or >{{THRESHOLD_PERCENT}}%
- Prior period data available: {{HAS_PRIOR_PERIOD}}

{{#IF CUSTOMER_NOTES}}
## Customer-Provided Context

{{CUSTOMER_NOTES}}
{{/IF}}

## Required Output

Return a JSON object with exactly these keys:

```json
{
  "executive_summary": "2-3 sentences. State total revenue vs. budget, total expenses vs. budget, and operating income result. Highlight the primary drivers. End with the operating income outcome.",
  "attention_items": [
    "2-3 items that require leadership attention. Each should name the specific issue, quantify the exposure, and explain why it needs action."
  ],
  "revenue_narratives": {
    "ACCOUNT_CODE": {
      "drivers": ["1-2 sentence bullet explaining this variance. Reference specific dollar amounts and percentages from the data."],
      "context": "Optional 1-sentence trend note or additional context. Null if not needed.",
      "action_required": "Specific action if warranted, or null."
    }
  },
  "expense_narratives": {
    "ACCOUNT_CODE": {
      "drivers": ["1-2 sentence bullet explaining this variance."],
      "context": "Optional context.",
      "action_required": "Specific action if warranted, or null.",
      "recurring": "Yes / No / Partially / Timing / TBD"
    }
  },
  "cogs_summary": "1-2 sentences on overall COGS position and gross margin impact.",
  "opex_summary": "1-2 sentences on overall OpEx position — net of favorable and unfavorable items.",
  "risks": [
    {
      "risk": "Specific risk description",
      "exposure": "Estimated financial impact (use dollar amounts from the data)",
      "trigger": "What would cause this risk to materialize"
    }
  ],
  "recommended_actions": [
    {
      "action": "Specific, actionable recommendation",
      "owner": "Role responsible (e.g., VP Sales, Engineering, People Ops)",
      "by_date": "Target date in the near term"
    }
  ]
}
```

Rules for this output:
- Include narratives ONLY for line items with `is_material: true`
- Every dollar amount and percentage must match the input data exactly
- Use `[VERIFY: ...]` markers for any causal detail you cannot confirm from the data alone
- Keep the total output under 3000 tokens
- Return ONLY the JSON object — no markdown, no explanation

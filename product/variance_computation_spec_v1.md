# Variance Computation Specification v1

**Purpose:** Define the deterministic variance calculations that transform validated, COA-mapped GL and budget data into structured variance output for memo drafting. No AI is used in this stage — all calculations are arithmetic.

**Alignment:** Stage 4 (computation portion) of `ops/live_pilot_workflow_v1.md`

---

## Input

A validated CSV file with the following columns (output of validation + COA mapping stages):

| Field | Required | Type | Notes |
|-------|----------|------|-------|
| `account_code` | Yes | String | Customer's GL account code |
| `account_name` | Yes | String | Human-readable account name |
| `category` | Yes | String | Revenue, COGS, or Operating Expenses |
| `actual_amount` | Yes | Float | Actual amount for the period |
| `budget_amount` | Yes | Float | Budget amount for the period |
| `prior_period_amount` | No | Float | Prior month actual (for MoM trends) |
| `period` | Yes | String | YYYY-MM format |

The COA mapping stage may add additional columns (`memo_section`, `variance_group`, `normalized_name`) but the computation script uses the core columns above.

---

## Calculations

### Per-Line-Item Calculations

For each row in the input:

| Output field | Formula | Notes |
|-------------|---------|-------|
| `variance_dollars` | `actual_amount - budget_amount` | Positive = over budget |
| `variance_percent` | `(actual_amount - budget_amount) / budget_amount * 100` | Handle budget = 0: set to `null` |
| `mom_change_dollars` | `actual_amount - prior_period_amount` | Only if `prior_period_amount` exists |
| `mom_change_percent` | `(actual_amount - prior_period_amount) / prior_period_amount * 100` | Handle prior = 0: set to `null` |
| `is_material` | See materiality rules below | Boolean flag |
| `signal` | See signal rules below | Favorable / Unfavorable / Watch / On plan |

### Materiality Rules

A variance is flagged as material if **either** condition is met:
- Absolute variance exceeds **$5,000** (`abs(variance_dollars) > 5000`)
- Absolute variance percentage exceeds **10%** (`abs(variance_percent) > 10`)

These thresholds are configurable via CLI arguments. They may be adjusted per customer during pilot kickoff.

### Signal Assignment

| Category | Variance | Signal |
|----------|----------|--------|
| Revenue | Positive (actual > budget) | Favorable |
| Revenue | Negative (actual < budget) | Unfavorable |
| COGS | Positive (actual > budget) | Unfavorable |
| COGS | Negative (actual < budget) | Favorable |
| Operating Expenses | Positive (actual > budget) | Unfavorable |
| Operating Expenses | Negative (actual < budget) | Favorable |
| Any | Variance within 2% of budget | On plan |
| Any | Material + direction unclear | Watch |

"On plan" takes precedence when variance percent is within +/- 2%.

### Topline Aggregations

| Metric | Formula |
|--------|---------|
| Total Revenue | Sum of all Revenue rows `actual_amount` |
| Total Revenue Budget | Sum of all Revenue rows `budget_amount` |
| Total COGS | Sum of all COGS rows `actual_amount` |
| Total COGS Budget | Sum of all COGS rows `budget_amount` |
| Gross Profit | Total Revenue - Total COGS |
| Gross Profit Budget | Total Revenue Budget - Total COGS Budget |
| Gross Margin % | Gross Profit / Total Revenue * 100 |
| Gross Margin Budget % | Gross Profit Budget / Total Revenue Budget * 100 |
| Total OpEx | Sum of all Operating Expenses rows `actual_amount` |
| Total OpEx Budget | Sum of all Operating Expenses rows `budget_amount` |
| Operating Income | Gross Profit - Total OpEx |
| Operating Income Budget | Gross Profit Budget - Total OpEx Budget |

Each topline metric also gets `variance_dollars`, `variance_percent`, and `signal` computed using the same formulas.

### MoM Topline Trends (if prior period data available)

Same aggregations as above but using `prior_period_amount` instead of `budget_amount` for comparison.

---

## Output

The script produces a JSON file with two sections:

### 1. `line_items` — per-account variance detail

```json
{
  "line_items": [
    {
      "account_code": "4100",
      "account_name": "SaaS Subscription Revenue",
      "category": "Revenue",
      "actual": 412800.00,
      "budget": 395000.00,
      "prior_period": 378200.00,
      "variance_dollars": 17800.00,
      "variance_percent": 4.51,
      "mom_change_dollars": 34600.00,
      "mom_change_percent": 9.15,
      "is_material": true,
      "signal": "Favorable"
    }
  ]
}
```

### 2. `topline` — aggregated performance summary

```json
{
  "topline": {
    "total_revenue": {"actual": 473400, "budget": 458000, "variance_dollars": 15400, "variance_percent": 3.36, "signal": "Favorable"},
    "total_cogs": {"actual": 89700, "budget": 85500, "variance_dollars": 4200, "variance_percent": 4.91, "signal": "Watch"},
    "gross_profit": {"actual": 383700, "budget": 372500, "variance_dollars": 11200, "variance_percent": 3.01, "signal": "Favorable"},
    "gross_margin_pct": {"actual": 81.07, "budget": 81.33, "variance_pts": -0.26},
    "total_opex": {"actual": 352400, "budget": 342500, "variance_dollars": 9900, "variance_percent": 2.89, "signal": "Watch"},
    "operating_income": {"actual": 31300, "budget": 30000, "variance_dollars": 1300, "variance_percent": 4.33, "signal": "Favorable"}
  }
}
```

### 3. `metadata` — computation context

```json
{
  "metadata": {
    "period": "2026-02",
    "input_file": "path/to/validated_data.csv",
    "row_count": 18,
    "material_items": 8,
    "materiality_threshold_dollars": 5000,
    "materiality_threshold_percent": 10,
    "has_prior_period": true,
    "computed_at": "2026-03-12T10:45:00Z"
  }
}
```

---

## CLI Usage

```bash
# Basic variance computation
python product/variance_computation_v1.py data/validated_gl.csv

# Custom materiality thresholds
python product/variance_computation_v1.py data/validated_gl.csv --threshold-dollars 3000 --threshold-percent 5

# Output to specific file
python product/variance_computation_v1.py data/validated_gl.csv --output reports/variance_output.json

# Pretty-print output to terminal
python product/variance_computation_v1.py data/validated_gl.csv --pretty
```

---

## Dependencies

- Python 3.10+
- `pandas` (data manipulation)
- Standard library: `json`, `sys`, `argparse`, `datetime`

---

## Assumptions

1. All amounts are in the same currency (no FX conversion)
2. Expenses are represented as positive numbers (spend)
3. Revenue is represented as positive numbers (income)
4. A single period per file (multi-period files are not supported in v1)
5. The input file has already passed validation (`product/validation_checks_v1.py`)
6. COA mapping has been applied if the customer uses non-standard categories

---

## What This Does Not Cover

- Narrative generation (AI-assisted — separate workflow)
- KPI computation beyond what is derivable from GL data (MRR, headcount from external sources)
- Multi-period trend analysis beyond single prior period
- Forecasting or projection
- Chart/graph generation

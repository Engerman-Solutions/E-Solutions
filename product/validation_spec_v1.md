# Validation Layer Specification v1

**Purpose:** Define the validation checks applied to customer-uploaded GL and budget files before any analysis is performed. No analysis runs on unvalidated data (DEC-009).

**Alignment:** Stage 2 of `ops/live_pilot_workflow_v1.md`

---

## Input Files

### GL Export (required every cycle)

| Field | Required | Type | Notes |
|-------|----------|------|-------|
| `account_code` | Yes | String | Customer's GL account code |
| `account_name` | Yes | String | Human-readable account name |
| `category` | Yes | String | Account category (Revenue, COGS, Operating Expenses) |
| `actual_amount` | Yes | Numeric | Actual amount for the period |
| `budget_amount` | Yes | Numeric | Budget amount for the period |
| `prior_period_amount` | No | Numeric | Prior month actual (for MoM trends) |
| `period` | Yes | String | Reporting period in YYYY-MM format |

Supported formats: CSV, XLSX, XLS

### Budget File (required at setup, updated if revised)

Same schema as GL export. The budget file may contain all 12 months; the system filters to the target period.

### Chart of Accounts (required at setup)

Handled separately via COA mapping process (`ops/coa_mapping_process_v1.md`). Not validated by this script — validated during the mapping stage.

---

## Validation Checks

### 1. File Format Check
- **Type:** Error (blocking)
- **Check:** File is non-empty, parseable as CSV or Excel, and under 25 MB
- **Failure message:** "File could not be parsed. Ensure it is a valid CSV or Excel file under 25 MB."

### 2. Schema Validation
- **Type:** Error (blocking)
- **Check:** All required columns are present (case-insensitive match). No unexpected column names that suggest wrong file type.
- **Failure message:** "Missing required column(s): {list}. Expected: account_code, account_name, category, actual_amount, budget_amount, period."

### 3. Data Type Validation
- **Type:** Error (blocking)
- **Check:** `actual_amount` and `budget_amount` are numeric (parseable as float). `period` is a valid YYYY-MM string. `account_code`, `account_name`, `category` are non-empty strings.
- **Failure message:** "Non-numeric value found in amount column at row {n}: '{value}'."

### 4. Period Validation
- **Type:** Error (blocking)
- **Check:** All rows have the same `period` value. The period is a valid YYYY-MM format. If a target period is specified, it matches.
- **Failure message:** "Mixed periods found in data: {list}. All rows must have the same period."

### 5. Category Validation
- **Type:** Warning (non-blocking)
- **Check:** `category` values are one of the expected set: Revenue, COGS, Operating Expenses. Unknown categories are flagged.
- **Warning message:** "Unknown category '{value}' at row {n}. Expected: Revenue, COGS, Operating Expenses."

### 6. Completeness Check
- **Type:** Warning (non-blocking)
- **Check:** At least one row exists for each expected category (Revenue, COGS, Operating Expenses). File has at least 3 rows.
- **Warning message:** "No rows found for category '{category}'. Memo may be incomplete."

### 7. Sign and Reasonableness Check
- **Type:** Warning (non-blocking)
- **Check:** Revenue amounts are positive. Expense amounts are positive (not negative — expenses are expected as positive values representing spend). No single line item exceeds $10M (likely data error at pilot ICP scale).
- **Warning message:** "Unusual value at row {n}: {account_name} has {field} = {value}. Verify this is correct."

### 8. Duplicate Row Detection
- **Type:** Warning (non-blocking)
- **Check:** No two rows have the same `account_code` and `period`. Duplicates suggest the file was exported incorrectly.
- **Warning message:** "Duplicate account_code '{code}' found at rows {n1} and {n2}."

### 9. Injection Scan
- **Type:** Error (blocking)
- **Check:** No text field contains potential injection patterns:
  - Formula injection: values starting with `=`, `+`, `-`, `@` followed by formula-like content
  - Script injection: `<script`, `javascript:`, `eval(`, `exec(`
  - SQL injection: `'; DROP`, `UNION SELECT`, `1=1`, `OR 1=1`
  - Command injection: backticks, `$(`, `| rm`, `&& rm`
- **Failure message:** "Potential injection pattern detected at row {n}, column '{col}': '{value}'. File rejected for security review."

### 10. File Hash and Duplicate Upload Detection
- **Type:** Warning (non-blocking)
- **Check:** Compute SHA-256 hash of the file. If a previous upload log exists, check for duplicate hashes.
- **Warning message:** "This file has the same hash as a previous upload ({date}). Confirm this is new data."

---

## Validation Output

The validation script produces a structured JSON report:

```json
{
  "file_path": "path/to/file.csv",
  "file_hash": "sha256:abc123...",
  "timestamp": "2026-03-12T10:30:00Z",
  "period_detected": "2026-02",
  "row_count": 18,
  "status": "PASS | FAIL",
  "errors": [
    {"check": "schema", "row": null, "message": "Missing required column: budget_amount"}
  ],
  "warnings": [
    {"check": "category", "row": 5, "message": "Unknown category 'Other Income'"}
  ],
  "summary": "18 rows validated. 0 errors, 1 warning. Status: PASS."
}
```

**PASS criteria:** Zero errors. Warnings are logged but do not block analysis.
**FAIL criteria:** One or more errors. Customer is notified with the specific error list and instructions to re-upload.

---

## CLI Usage

```bash
# Validate a GL export
python product/validation_checks_v1.py data/customer_gl_export.csv

# Validate with a target period
python product/validation_checks_v1.py data/customer_gl_export.csv --period 2026-02

# Validate an Excel file
python product/validation_checks_v1.py data/customer_gl_export.xlsx

# Output JSON report to file
python product/validation_checks_v1.py data/customer_gl_export.csv --output reports/validation_report.json
```

---

## Dependencies

- Python 3.10+
- `pandas` (CSV/Excel parsing)
- `openpyxl` (Excel support)
- Standard library: `json`, `hashlib`, `re`, `sys`, `argparse`, `datetime`

---

## What This Does Not Cover

- Budget file cross-validation against GL (planned for v2)
- COA mapping validation (handled by the mapping stage)
- Multi-period file splitting (out of pilot scope)
- Real-time validation feedback in a web UI (post-pilot)

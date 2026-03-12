#!/usr/bin/env python3
"""
E-Solutions Validation Layer v1

Validates customer-uploaded GL and budget files before analysis.
No analysis runs on unvalidated data (DEC-009).

Usage:
    python validation_checks_v1.py <file_path> [--period YYYY-MM] [--output report.json]

See product/validation_spec_v1.md for full specification.
"""

import argparse
import csv
import hashlib
import json
import re
import sys
import datetime
from pathlib import Path

REQUIRED_COLUMNS = {
    "account_code",
    "account_name",
    "category",
    "actual_amount",
    "budget_amount",
    "period",
}

OPTIONAL_COLUMNS = {"prior_period_amount"}

EXPECTED_CATEGORIES = {"Revenue", "COGS", "Operating Expenses"}

NUMERIC_COLUMNS = {"actual_amount", "budget_amount", "prior_period_amount"}

MAX_FILE_SIZE_BYTES = 25 * 1024 * 1024  # 25 MB

# Patterns that indicate potential injection attacks
INJECTION_PATTERNS = [
    # Formula injection (common in CSV attacks)
    re.compile(r"^[=+\-@]\s*[A-Za-z(]"),
    # Script injection
    re.compile(r"<script", re.IGNORECASE),
    re.compile(r"javascript:", re.IGNORECASE),
    re.compile(r"\beval\s*\(", re.IGNORECASE),
    re.compile(r"\bexec\s*\(", re.IGNORECASE),
    # SQL injection
    re.compile(r"';\s*DROP\b", re.IGNORECASE),
    re.compile(r"\bUNION\s+SELECT\b", re.IGNORECASE),
    re.compile(r"\bOR\s+1\s*=\s*1\b", re.IGNORECASE),
    # Command injection
    re.compile(r"`[^`]+`"),
    re.compile(r"\$\("),
    re.compile(r"\|\s*rm\b"),
    re.compile(r"&&\s*rm\b"),
]

PERIOD_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")

MAX_REASONABLE_AMOUNT = 10_000_000  # $10M — unreasonable for pilot ICP scale


def compute_file_hash(file_path: str) -> str:
    """Compute SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return f"sha256:{sha256.hexdigest()}"


def load_csv(file_path: str) -> tuple[list[dict], list[str]]:
    """Load a CSV file and return rows as list of dicts and column headers."""
    with open(file_path, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        headers = [h.strip().lower() for h in (reader.fieldnames or [])]
        rows = []
        for row in reader:
            cleaned = {k.strip().lower(): v.strip() for k, v in row.items()}
            rows.append(cleaned)
    return rows, headers


def load_excel(file_path: str) -> tuple[list[dict], list[str]]:
    """Load an Excel file using openpyxl and return rows as list of dicts."""
    try:
        import openpyxl
    except ImportError:
        raise ImportError(
            "openpyxl is required for Excel file support. "
            "Install with: pip install openpyxl"
        )

    wb = openpyxl.load_workbook(file_path, read_only=True, data_only=True)
    ws = wb.active
    rows_iter = ws.iter_rows(values_only=True)

    header_row = next(rows_iter, None)
    if header_row is None:
        return [], []

    headers = [str(h).strip().lower() if h else "" for h in header_row]
    rows = []
    for row in rows_iter:
        row_dict = {}
        for i, val in enumerate(row):
            if i < len(headers) and headers[i]:
                row_dict[headers[i]] = str(val).strip() if val is not None else ""
        rows.append(row_dict)

    wb.close()
    return rows, headers


def validate(file_path: str, target_period: str | None = None) -> dict:
    """Run all validation checks on the given file. Returns a validation report dict."""
    errors = []
    warnings = []
    path = Path(file_path)

    # --- Check 1: File format ---
    if not path.exists():
        errors.append({
            "check": "file_format",
            "row": None,
            "message": f"File not found: {file_path}",
        })
        return _build_report(file_path, None, None, 0, errors, warnings)

    file_size = path.stat().st_size
    if file_size == 0:
        errors.append({
            "check": "file_format",
            "row": None,
            "message": "File is empty.",
        })
        return _build_report(file_path, None, None, 0, errors, warnings)

    if file_size > MAX_FILE_SIZE_BYTES:
        errors.append({
            "check": "file_format",
            "row": None,
            "message": f"File exceeds 25 MB limit ({file_size / 1024 / 1024:.1f} MB).",
        })
        return _build_report(file_path, None, None, 0, errors, warnings)

    suffix = path.suffix.lower()
    if suffix not in {".csv", ".xlsx", ".xls"}:
        errors.append({
            "check": "file_format",
            "row": None,
            "message": f"Unsupported file format: {suffix}. Expected .csv, .xlsx, or .xls.",
        })
        return _build_report(file_path, None, None, 0, errors, warnings)

    # Load file
    try:
        if suffix == ".csv":
            rows, headers = load_csv(file_path)
        else:
            rows, headers = load_excel(file_path)
    except Exception as e:
        errors.append({
            "check": "file_format",
            "row": None,
            "message": f"File could not be parsed: {e}",
        })
        return _build_report(file_path, None, None, 0, errors, warnings)

    file_hash = compute_file_hash(file_path)
    row_count = len(rows)

    if row_count == 0:
        errors.append({
            "check": "file_format",
            "row": None,
            "message": "File contains headers but no data rows.",
        })
        return _build_report(file_path, file_hash, None, 0, errors, warnings)

    # --- Check 2: Schema validation ---
    header_set = set(headers)
    missing = REQUIRED_COLUMNS - header_set
    if missing:
        errors.append({
            "check": "schema",
            "row": None,
            "message": (
                f"Missing required column(s): {', '.join(sorted(missing))}. "
                f"Expected: {', '.join(sorted(REQUIRED_COLUMNS))}."
            ),
        })
        return _build_report(file_path, file_hash, None, row_count, errors, warnings)

    # --- Check 3: Data type validation ---
    for i, row in enumerate(rows, start=2):  # Row 2 = first data row (1-indexed, header is row 1)
        for col in NUMERIC_COLUMNS:
            val = row.get(col, "")
            if col in OPTIONAL_COLUMNS and val == "":
                continue
            if val == "" and col in REQUIRED_COLUMNS:
                errors.append({
                    "check": "data_type",
                    "row": i,
                    "message": f"Empty value in required column '{col}' at row {i}.",
                })
                continue
            try:
                float(val)
            except (ValueError, TypeError):
                errors.append({
                    "check": "data_type",
                    "row": i,
                    "message": f"Non-numeric value in '{col}' at row {i}: '{val}'.",
                })

        # Check non-empty strings
        for col in ("account_code", "account_name", "category"):
            if not row.get(col, "").strip():
                errors.append({
                    "check": "data_type",
                    "row": i,
                    "message": f"Empty value in required column '{col}' at row {i}.",
                })

    # --- Check 4: Period validation ---
    periods = set()
    for i, row in enumerate(rows, start=2):
        period = row.get("period", "").strip()
        if not PERIOD_RE.match(period):
            errors.append({
                "check": "period",
                "row": i,
                "message": f"Invalid period format at row {i}: '{period}'. Expected YYYY-MM.",
            })
        else:
            periods.add(period)

    if len(periods) > 1:
        errors.append({
            "check": "period",
            "row": None,
            "message": f"Mixed periods found: {', '.join(sorted(periods))}. All rows must have the same period.",
        })

    detected_period = periods.pop() if len(periods) == 1 else None

    if target_period and detected_period and detected_period != target_period:
        errors.append({
            "check": "period",
            "row": None,
            "message": (
                f"Period mismatch: file contains '{detected_period}' "
                f"but target period is '{target_period}'."
            ),
        })

    # --- Check 5: Category validation ---
    for i, row in enumerate(rows, start=2):
        cat = row.get("category", "").strip()
        if cat and cat not in EXPECTED_CATEGORIES:
            warnings.append({
                "check": "category",
                "row": i,
                "message": f"Unknown category '{cat}' at row {i}. Expected: {', '.join(sorted(EXPECTED_CATEGORIES))}.",
            })

    # --- Check 6: Completeness check ---
    found_categories = {row.get("category", "").strip() for row in rows}
    for expected in EXPECTED_CATEGORIES:
        if expected not in found_categories:
            warnings.append({
                "check": "completeness",
                "row": None,
                "message": f"No rows found for category '{expected}'. Memo may be incomplete.",
            })

    if row_count < 3:
        warnings.append({
            "check": "completeness",
            "row": None,
            "message": f"Only {row_count} data rows. Expected at least 3 for a meaningful memo.",
        })

    # --- Check 7: Sign and reasonableness ---
    for i, row in enumerate(rows, start=2):
        for col in ("actual_amount", "budget_amount"):
            val_str = row.get(col, "")
            try:
                val = float(val_str)
            except (ValueError, TypeError):
                continue  # Already caught in data type check

            if val < 0:
                warnings.append({
                    "check": "sign",
                    "row": i,
                    "message": (
                        f"Negative value at row {i}: {row.get('account_name', '?')} "
                        f"has {col} = {val}. Verify this is correct."
                    ),
                })

            if abs(val) > MAX_REASONABLE_AMOUNT:
                warnings.append({
                    "check": "reasonableness",
                    "row": i,
                    "message": (
                        f"Unusually large value at row {i}: {row.get('account_name', '?')} "
                        f"has {col} = {val:,.2f}. Verify this is correct."
                    ),
                })

    # --- Check 8: Duplicate row detection ---
    seen = {}
    for i, row in enumerate(rows, start=2):
        key = (row.get("account_code", ""), row.get("period", ""))
        if key in seen:
            warnings.append({
                "check": "duplicate",
                "row": i,
                "message": (
                    f"Duplicate account_code '{key[0]}' found at rows {seen[key]} and {i}."
                ),
            })
        else:
            seen[key] = i

    # --- Check 9: Injection scan ---
    text_columns = ("account_code", "account_name", "category")
    for i, row in enumerate(rows, start=2):
        for col in text_columns:
            val = row.get(col, "")
            for pattern in INJECTION_PATTERNS:
                if pattern.search(val):
                    errors.append({
                        "check": "injection",
                        "row": i,
                        "message": (
                            f"Potential injection pattern detected at row {i}, "
                            f"column '{col}': '{val[:80]}'. File rejected for security review."
                        ),
                    })
                    break  # One match per cell is enough

    return _build_report(file_path, file_hash, detected_period, row_count, errors, warnings)


def _build_report(
    file_path: str,
    file_hash: str | None,
    period: str | None,
    row_count: int,
    errors: list[dict],
    warnings: list[dict],
) -> dict:
    """Build the structured validation report."""
    status = "FAIL" if errors else "PASS"
    error_count = len(errors)
    warning_count = len(warnings)

    return {
        "file_path": file_path,
        "file_hash": file_hash,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "period_detected": period,
        "row_count": row_count,
        "status": status,
        "errors": errors,
        "warnings": warnings,
        "summary": (
            f"{row_count} rows validated. "
            f"{error_count} error(s), {warning_count} warning(s). "
            f"Status: {status}."
        ),
    }


def main():
    parser = argparse.ArgumentParser(
        description="E-Solutions Validation Layer v1 — validate GL/budget uploads"
    )
    parser.add_argument("file_path", help="Path to the CSV or Excel file to validate")
    parser.add_argument(
        "--period",
        default=None,
        help="Expected reporting period (YYYY-MM). If provided, validates against it.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Path to write JSON validation report. If omitted, prints to stdout.",
    )
    args = parser.parse_args()

    report = validate(args.file_path, target_period=args.period)

    report_json = json.dumps(report, indent=2)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report_json)
        print(f"Validation report written to {args.output}")
    else:
        print(report_json)

    # Exit with non-zero status on validation failure
    if report["status"] == "FAIL":
        sys.exit(1)


if __name__ == "__main__":
    main()

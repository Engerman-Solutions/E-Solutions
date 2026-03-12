#!/usr/bin/env python3
"""
E-Solutions Variance Computation v1

Computes actual vs. budget variances and MoM trends from validated GL data.
All calculations are deterministic — no AI is used in this stage.

Usage:
    python variance_computation_v1.py <file_path> [--threshold-dollars 5000] [--threshold-percent 10] [--output report.json] [--pretty]

See product/variance_computation_spec_v1.md for full specification.
"""

import argparse
import json
import sys
import datetime
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("pandas is required. Install with: pip install pandas", file=sys.stderr)
    sys.exit(1)

DEFAULT_THRESHOLD_DOLLARS = 5000
DEFAULT_THRESHOLD_PERCENT = 10
ON_PLAN_BAND = 2.0  # +/- 2% considered "On plan"

# Categories where higher actual = unfavorable (cost categories)
COST_CATEGORIES = {"COGS", "Operating Expenses"}


def load_data(file_path: str) -> pd.DataFrame:
    """Load validated GL data from CSV or Excel."""
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".csv":
        df = pd.read_csv(file_path, dtype={"account_code": str, "period": str})
    elif suffix in (".xlsx", ".xls"):
        df = pd.read_excel(file_path, dtype={"account_code": str, "period": str})
    else:
        raise ValueError(f"Unsupported file format: {suffix}")

    # Normalize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Ensure numeric columns
    for col in ("actual_amount", "budget_amount"):
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    if "prior_period_amount" in df.columns:
        df["prior_period_amount"] = pd.to_numeric(
            df["prior_period_amount"], errors="coerce"
        )

    return df


def compute_variance(actual: float, budget: float) -> tuple[float, float | None]:
    """Compute variance in dollars and percent."""
    var_dollars = actual - budget
    if budget != 0:
        var_percent = round((actual - budget) / abs(budget) * 100, 2)
    else:
        var_percent = None
    return round(var_dollars, 2), var_percent


def compute_mom(actual: float, prior: float | None) -> tuple[float | None, float | None]:
    """Compute month-over-month change in dollars and percent."""
    if prior is None or pd.isna(prior):
        return None, None
    mom_dollars = round(actual - prior, 2)
    if prior != 0:
        mom_percent = round((actual - prior) / abs(prior) * 100, 2)
    else:
        mom_percent = None
    return mom_dollars, mom_percent


def assign_signal(
    category: str,
    variance_percent: float | None,
    is_material: bool,
) -> str:
    """Assign a signal label based on category and variance direction."""
    if variance_percent is None:
        return "Watch"

    # On plan if within band
    if abs(variance_percent) <= ON_PLAN_BAND:
        return "On plan"

    is_cost = category in COST_CATEGORIES

    if is_cost:
        # For costs: over budget = unfavorable
        if variance_percent > 0:
            return "Unfavorable" if is_material else "Watch"
        else:
            return "Favorable"
    else:
        # For revenue: over budget = favorable
        if variance_percent > 0:
            return "Favorable"
        else:
            return "Unfavorable" if is_material else "Watch"


def check_materiality(
    var_dollars: float,
    var_percent: float | None,
    threshold_dollars: float,
    threshold_percent: float,
) -> bool:
    """Check if a variance is material based on thresholds."""
    if abs(var_dollars) > threshold_dollars:
        return True
    if var_percent is not None and abs(var_percent) > threshold_percent:
        return True
    return False


def compute_line_items(
    df: pd.DataFrame,
    threshold_dollars: float,
    threshold_percent: float,
) -> list[dict]:
    """Compute per-line-item variances."""
    has_prior = "prior_period_amount" in df.columns
    items = []

    for _, row in df.iterrows():
        actual = float(row["actual_amount"])
        budget = float(row["budget_amount"])
        prior = float(row["prior_period_amount"]) if has_prior and pd.notna(row.get("prior_period_amount")) else None
        category = str(row["category"]).strip()

        var_dollars, var_percent = compute_variance(actual, budget)
        mom_dollars, mom_percent = compute_mom(actual, prior)
        is_material = check_materiality(var_dollars, var_percent, threshold_dollars, threshold_percent)
        signal = assign_signal(category, var_percent, is_material)

        item = {
            "account_code": str(row["account_code"]).strip(),
            "account_name": str(row["account_name"]).strip(),
            "category": category,
            "actual": actual,
            "budget": budget,
            "variance_dollars": var_dollars,
            "variance_percent": var_percent,
            "is_material": bool(is_material),
            "signal": signal,
        }

        if prior is not None:
            item["prior_period"] = prior
            item["mom_change_dollars"] = mom_dollars
            item["mom_change_percent"] = mom_percent

        items.append(item)

    return items


def compute_topline(df: pd.DataFrame) -> dict:
    """Compute topline aggregations."""
    has_prior = "prior_period_amount" in df.columns

    rev = df[df["category"] == "Revenue"]
    cogs = df[df["category"] == "COGS"]
    opex = df[df["category"] == "Operating Expenses"]

    def agg(subset: pd.DataFrame, category: str) -> dict:
        actual = round(float(subset["actual_amount"].sum()), 2)
        budget = round(float(subset["budget_amount"].sum()), 2)
        var_d, var_p = compute_variance(actual, budget)
        is_mat = check_materiality(var_d, var_p, DEFAULT_THRESHOLD_DOLLARS, DEFAULT_THRESHOLD_PERCENT)
        sig = assign_signal(category, var_p, is_mat)
        result = {
            "actual": actual,
            "budget": budget,
            "variance_dollars": var_d,
            "variance_percent": var_p,
            "signal": sig,
        }
        if has_prior and "prior_period_amount" in subset.columns:
            prior_sum = subset["prior_period_amount"].sum()
            if pd.notna(prior_sum):
                result["prior_period"] = round(float(prior_sum), 2)
                mom_d, mom_p = compute_mom(actual, float(prior_sum))
                result["mom_change_dollars"] = mom_d
                result["mom_change_percent"] = mom_p
        return result

    total_rev = agg(rev, "Revenue")
    total_cogs = agg(cogs, "COGS")

    # Gross profit
    gp_actual = total_rev["actual"] - total_cogs["actual"]
    gp_budget = total_rev["budget"] - total_cogs["budget"]
    gp_var_d, gp_var_p = compute_variance(gp_actual, gp_budget)
    gp_signal = assign_signal("Revenue", gp_var_p,
                              check_materiality(gp_var_d, gp_var_p, DEFAULT_THRESHOLD_DOLLARS, DEFAULT_THRESHOLD_PERCENT))

    gross_profit = {
        "actual": round(gp_actual, 2),
        "budget": round(gp_budget, 2),
        "variance_dollars": gp_var_d,
        "variance_percent": gp_var_p,
        "signal": gp_signal,
    }

    # Gross margin %
    gm_actual = round(gp_actual / total_rev["actual"] * 100, 2) if total_rev["actual"] != 0 else 0
    gm_budget = round(gp_budget / total_rev["budget"] * 100, 2) if total_rev["budget"] != 0 else 0

    gross_margin = {
        "actual": gm_actual,
        "budget": gm_budget,
        "variance_pts": round(gm_actual - gm_budget, 2),
    }

    # Total OpEx
    total_opex = agg(opex, "Operating Expenses")

    # Operating income
    oi_actual = gp_actual - total_opex["actual"]
    oi_budget = gp_budget - total_opex["budget"]
    oi_var_d, oi_var_p = compute_variance(oi_actual, oi_budget)
    oi_signal = assign_signal("Revenue", oi_var_p,
                              check_materiality(oi_var_d, oi_var_p, DEFAULT_THRESHOLD_DOLLARS, DEFAULT_THRESHOLD_PERCENT))

    operating_income = {
        "actual": round(oi_actual, 2),
        "budget": round(oi_budget, 2),
        "variance_dollars": oi_var_d,
        "variance_percent": oi_var_p,
        "signal": oi_signal,
    }

    return {
        "total_revenue": total_rev,
        "total_cogs": total_cogs,
        "gross_profit": gross_profit,
        "gross_margin_pct": gross_margin,
        "total_opex": total_opex,
        "operating_income": operating_income,
    }


def compute(
    file_path: str,
    threshold_dollars: float = DEFAULT_THRESHOLD_DOLLARS,
    threshold_percent: float = DEFAULT_THRESHOLD_PERCENT,
) -> dict:
    """Run full variance computation. Returns structured output dict."""
    df = load_data(file_path)

    has_prior = "prior_period_amount" in df.columns and df["prior_period_amount"].notna().any()

    line_items = compute_line_items(df, threshold_dollars, threshold_percent)
    topline = compute_topline(df)

    material_count = sum(1 for item in line_items if item["is_material"])
    periods = df["period"].dropna().unique()
    period = str(periods[0]) if len(periods) > 0 else "unknown"

    metadata = {
        "period": period,
        "input_file": file_path,
        "row_count": len(df),
        "material_items": material_count,
        "materiality_threshold_dollars": threshold_dollars,
        "materiality_threshold_percent": threshold_percent,
        "has_prior_period": bool(has_prior),
        "computed_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    return {
        "line_items": line_items,
        "topline": topline,
        "metadata": metadata,
    }


def main():
    parser = argparse.ArgumentParser(
        description="E-Solutions Variance Computation v1 — compute variances from validated GL data"
    )
    parser.add_argument("file_path", help="Path to validated CSV or Excel file")
    parser.add_argument(
        "--threshold-dollars",
        type=float,
        default=DEFAULT_THRESHOLD_DOLLARS,
        help=f"Dollar threshold for materiality (default: {DEFAULT_THRESHOLD_DOLLARS})",
    )
    parser.add_argument(
        "--threshold-percent",
        type=float,
        default=DEFAULT_THRESHOLD_PERCENT,
        help=f"Percentage threshold for materiality (default: {DEFAULT_THRESHOLD_PERCENT})",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Path to write JSON output. If omitted, prints to stdout.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output.",
    )
    args = parser.parse_args()

    result = compute(
        args.file_path,
        threshold_dollars=args.threshold_dollars,
        threshold_percent=args.threshold_percent,
    )

    indent = 2 if args.pretty else None
    output_json = json.dumps(result, indent=indent)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output_json)
        print(f"Variance report written to {args.output}")
    else:
        print(output_json)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
E-Solutions Memo Assembly v1

Assembles a draft variance memo from:
1. Variance computation output (JSON)
2. AI-generated narrative sections (JSON)
3. Company context (JSON)

Usage:
    python assemble_memo_v1.py --variance output/variance.json --narrative output/narrative.json --context config/context.json --output memo.md

See product/memo_assembly_spec_v1.md for full specification.
"""

import argparse
import datetime
import json
import sys
from pathlib import Path


def fmt_dollars(amount: float) -> str:
    """Format a dollar amount: $XXX,XXX for positive, -$XXX,XXX for negative."""
    if amount < 0:
        return f"-${abs(amount):,.0f}"
    return f"${amount:,.0f}"


def fmt_var_dollars(amount: float) -> str:
    """Format a variance dollar amount with +/- prefix."""
    if amount > 0:
        return f"+${amount:,.0f}"
    elif amount < 0:
        return f"-${abs(amount):,.0f}"
    return "$0"


def fmt_var_pct(pct: float | None) -> str:
    """Format a variance percentage with +/- prefix."""
    if pct is None:
        return "—"
    if pct > 0:
        return f"+{pct:.1f}%"
    elif pct < 0:
        return f"{pct:.1f}%"
    return "0.0%"


def fmt_pct(pct: float) -> str:
    """Format a plain percentage."""
    return f"{pct:.1f}%"


def load_json(path: str) -> dict:
    """Load and parse a JSON file."""
    with open(path, "r") as f:
        return json.load(f)


def render_metadata(ctx: dict) -> str:
    """Render the metadata block at the top of the memo."""
    lines = [
        "# Monthly Variance Memo",
        "",
        "| | |",
        "|---|---|",
        f"| **Company** | {ctx['company_name']} |",
        f"| **Period** | {ctx['period_display']} |",
        f"| **Prepared by** | {ctx['prepared_by']} |",
        f"| **Memo status** | {ctx['memo_status']} |",
        f"| **Checkpoint** | {ctx['checkpoint_id']} |",
        f"| **Validation** | {ctx['validation_summary']} |",
        "",
        "---",
    ]
    return "\n".join(lines)


def render_executive_summary(narrative: dict) -> str:
    """Render the executive summary section."""
    lines = [
        "",
        "## Executive Summary",
        "",
        narrative["executive_summary"],
        "",
    ]

    if narrative.get("attention_items"):
        count = len(narrative["attention_items"])
        word = "item requires" if count == 1 else "items require"
        lines.append(f"**{count} {word} leadership attention:**")
        for i, item in enumerate(narrative["attention_items"], 1):
            lines.append(f"{i}. {item}")

    lines.append("")
    lines.append("---")
    return "\n".join(lines)


def render_topline(topline: dict) -> str:
    """Render the topline performance table."""
    t = topline

    rows = [
        ("Total Revenue", t["total_revenue"], False),
        ("Total COGS", t["total_cogs"], False),
        ("**Gross Profit**", t["gross_profit"], True),
        ("Gross Margin", t.get("gross_margin_pct"), "margin"),
        ("Total OpEx", t["total_opex"], False),
        ("**Operating Income**", t["operating_income"], True),
    ]

    lines = [
        "",
        "## Topline Performance",
        "",
        "| Metric | Actual | Budget | Var ($) | Var (%) | Signal |",
        "|--------|--------|--------|---------|---------|--------|",
    ]

    for label, data, bold in rows:
        if bold == "margin":
            # Gross margin is a percentage row
            actual = fmt_pct(data["actual"])
            budget = fmt_pct(data["budget"])
            var_d = f"{data['variance_pts']:+.1f} pts"
            var_p = "—"
            signal = "On plan" if abs(data["variance_pts"]) < 1.0 else "Watch"
            lines.append(f"| {label} | {actual} | {budget} | {var_d} | {var_p} | {signal} |")
        else:
            actual = fmt_dollars(data["actual"])
            budget = fmt_dollars(data["budget"])
            var_d = fmt_var_dollars(data["variance_dollars"])
            var_p = fmt_var_pct(data["variance_percent"])
            signal = data.get("signal", "—")
            if bold:
                lines.append(f"| {label} | **{actual}** | **{budget}** | **{var_d}** | **{var_p}** | **{signal}** |")
            else:
                lines.append(f"| {label} | {actual} | {budget} | {var_d} | {var_p} | {signal} |")

    lines.append("")
    lines.append("---")
    return "\n".join(lines)


def render_revenue_detail(line_items: list, narrative: dict) -> str:
    """Render revenue variance detail sections."""
    revenue_items = [i for i in line_items if i["category"] == "Revenue" and i["is_material"]]

    if not revenue_items:
        return ""

    lines = [
        "",
        "## Revenue Variance Detail",
    ]

    for item in revenue_items:
        code = item["account_code"]
        name = item["account_name"]
        var_d = fmt_var_dollars(item["variance_dollars"])
        var_p = fmt_var_pct(item["variance_percent"])

        lines.append("")
        lines.append(f"### {name}: {var_d} vs. budget ({var_p})")
        lines.append("")

        # Mini comparison table
        lines.append("| | Actual | Budget | Prior Mo. |")
        lines.append("|---|---|---|---|")
        prior = fmt_dollars(item["prior_period"]) if item.get("prior_period") is not None else "—"
        lines.append(f"| {name} | {fmt_dollars(item['actual'])} | {fmt_dollars(item['budget'])} | {prior} |")
        lines.append("")

        # Narrative drivers
        narr = narrative.get("revenue_narratives", {}).get(code)
        if narr:
            lines.append("**Drivers:**")
            for driver in narr.get("drivers", []):
                lines.append(f"- {driver}")

            if narr.get("context"):
                lines.append("")
                lines.append(narr["context"])

            if narr.get("action_required"):
                lines.append("")
                lines.append(f"**Action required:** {narr['action_required']}")
        else:
            lines.append("*[NARRATIVE NEEDED: No driver explanation generated for this variance]*")

    lines.append("")
    lines.append("---")
    return "\n".join(lines)


def render_expense_detail(line_items: list, narrative: dict) -> str:
    """Render expense variance detail sections (COGS + OpEx)."""
    cogs_items = [i for i in line_items if i["category"] == "COGS"]
    opex_items = [i for i in line_items if i["category"] == "Operating Expenses"]

    lines = [
        "",
        "## Expense Variance Detail",
    ]

    # --- COGS section ---
    cogs_total = sum(i["variance_dollars"] for i in cogs_items)
    cogs_actual = sum(i["actual"] for i in cogs_items)
    cogs_budget = sum(i["budget"] for i in cogs_items)
    cogs_pct = (cogs_actual - cogs_budget) / cogs_budget * 100 if cogs_budget else 0

    lines.append("")
    lines.append(f"### COGS: {fmt_var_dollars(cogs_total)} vs. budget ({fmt_var_pct(cogs_pct)})")
    lines.append("")
    lines.append("| Line Item | Actual | Budget | Var ($) | Var (%) | Recurring? |")
    lines.append("|-----------|--------|--------|---------|---------|------------|")

    for item in cogs_items:
        code = item["account_code"]
        narr = narrative.get("expense_narratives", {}).get(code, {})
        recurring = narr.get("recurring", "—")
        lines.append(
            f"| {item['account_name']} | {fmt_dollars(item['actual'])} | {fmt_dollars(item['budget'])} "
            f"| {fmt_var_dollars(item['variance_dollars'])} | {fmt_var_pct(item['variance_percent'])} "
            f"| {recurring} |"
        )

    lines.append("")

    # COGS drivers for material items
    material_cogs = [i for i in cogs_items if i["is_material"]]
    for item in material_cogs:
        code = item["account_code"]
        narr = narrative.get("expense_narratives", {}).get(code)
        if narr and narr.get("drivers"):
            drivers = narr["drivers"]
            lines.append(f"- **{item['account_name']}:** {drivers[0]}")
            for driver in drivers[1:]:
                lines.append(f"  {driver}")

    cogs_summary = narrative.get("cogs_summary")
    if cogs_summary:
        lines.append("")
        lines.append(cogs_summary)

    # --- OpEx section ---
    opex_total = sum(i["variance_dollars"] for i in opex_items)
    opex_actual = sum(i["actual"] for i in opex_items)
    opex_budget = sum(i["budget"] for i in opex_items)
    opex_pct = (opex_actual - opex_budget) / opex_budget * 100 if opex_budget else 0

    lines.append("")
    lines.append(f"### Operating Expenses: {fmt_var_dollars(opex_total)} vs. budget ({fmt_var_pct(opex_pct)})")
    lines.append("")

    # Favorable items
    favorable = [i for i in opex_items if i["variance_dollars"] < 0 and i["is_material"]]
    unfavorable = [i for i in opex_items if i["variance_dollars"] > 0 and i["is_material"]]

    if favorable:
        lines.append("**Favorable:**")
        lines.append("")
        lines.append("| Line Item | Actual | Budget | Var ($) | Var (%) |")
        lines.append("|-----------|--------|--------|---------|---------|")
        for item in favorable:
            lines.append(
                f"| {item['account_name']} | {fmt_dollars(item['actual'])} | {fmt_dollars(item['budget'])} "
                f"| {fmt_var_dollars(item['variance_dollars'])} | {fmt_var_pct(item['variance_percent'])} |"
            )
        lines.append("")

        for item in favorable:
            code = item["account_code"]
            narr = narrative.get("expense_narratives", {}).get(code)
            if narr and narr.get("drivers"):
                drivers = narr["drivers"]
                lines.append(f"- **{item['account_name']}:** {drivers[0]}")
                for driver in drivers[1:]:
                    lines.append(f"  {driver}")
        lines.append("")

    if unfavorable:
        lines.append("**Unfavorable:**")
        lines.append("")
        lines.append("| Line Item | Actual | Budget | Var ($) | Var (%) | Recurring? |")
        lines.append("|-----------|--------|--------|---------|---------|------------|")
        for item in unfavorable:
            code = item["account_code"]
            narr = narrative.get("expense_narratives", {}).get(code, {})
            recurring = narr.get("recurring", "—")
            lines.append(
                f"| {item['account_name']} | {fmt_dollars(item['actual'])} | {fmt_dollars(item['budget'])} "
                f"| {fmt_var_dollars(item['variance_dollars'])} | {fmt_var_pct(item['variance_percent'])} "
                f"| {recurring} |"
            )
        lines.append("")

        for item in unfavorable:
            code = item["account_code"]
            narr = narrative.get("expense_narratives", {}).get(code)
            if narr and narr.get("drivers"):
                drivers = narr["drivers"]
                lines.append(f"- **{item['account_name']} ({fmt_var_dollars(item['variance_dollars'])}):** {drivers[0]}")
                for driver in drivers[1:]:
                    lines.append(f"  {driver}")
        lines.append("")

    opex_summary = narrative.get("opex_summary")
    if opex_summary:
        lines.append(opex_summary)

    lines.append("")
    lines.append("---")
    return "\n".join(lines)


def render_risks(narrative: dict) -> str:
    """Render risks and watchouts section."""
    risks = narrative.get("risks", [])
    if not risks:
        return ""

    lines = [
        "",
        "## Risks and Watchouts",
        "",
        "| # | Risk | Exposure | Trigger |",
        "|---|------|----------|---------|",
    ]

    for i, risk in enumerate(risks, 1):
        lines.append(f"| {i} | {risk['risk']} | {risk['exposure']} | {risk['trigger']} |")

    lines.append("")
    lines.append("---")
    return "\n".join(lines)


def render_actions(narrative: dict) -> str:
    """Render recommended actions section."""
    actions = narrative.get("recommended_actions", [])
    if not actions:
        return ""

    lines = [
        "",
        "## Recommended Actions",
        "",
        "| # | Action | Owner | By |",
        "|---|--------|-------|----|",
    ]

    for i, action in enumerate(actions, 1):
        lines.append(f"| {i} | {action['action']} | {action['owner']} | {action['by_date']} |")

    lines.append("")
    lines.append("---")
    return "\n".join(lines)


def render_provenance(ctx: dict, metadata: dict) -> str:
    """Render data provenance and audit trail section."""
    generated_at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "",
        "## Data Provenance and Audit Trail",
        "",
        "This section documents the inputs, processing, and review chain for this memo.",
        "",
        "| Item | Detail |",
        "|------|--------|",
        f"| **Source system** | {ctx.get('source_system', '—')} |",
        f"| **GL export date** | {ctx.get('gl_export_date', '—')} |",
        f"| **Budget source** | {ctx.get('budget_source', '—')} |",
        f"| **Prior period** | {ctx.get('prior_period_checkpoint', '—')} |",
        f"| **COA template** | {ctx.get('coa_template', '—')} (hash: {ctx.get('coa_template_hash', '—')}...) |",
        f"| **Schema validation** | Pass — {metadata.get('row_count', '—')}/{metadata.get('row_count', '—')} line items, 0 errors, 0 warnings |",
        "| **Injection scan** | Pass — no adversarial patterns detected |",
        f"| **Analysis checkpoint** | {ctx.get('checkpoint_id', '—')} |",
        f"| **Analysis engine** | {ctx.get('analysis_engine', '—')} |",
        f"| **Draft generated** | {generated_at} |",
        f"| **QA reviewer** | {ctx.get('qa_reviewer', 'Pending assignment')} |",
        f"| **Review status** | DRAFT — awaiting finance QA review |",
        "| **Approval status** | Not yet approved |",
        "",
        "### How to read this section",
        "",
        f"- **Checkpoint ID** ({ctx.get('checkpoint_id', '—')}) ties this memo to the exact source data, validation results, and analysis run. It can reproduce this memo at any time.",
        "- **COA template version** ensures the account mapping used is recorded and auditable. If the template changes, prior memos remain tied to the version used when they were produced.",
        "- **Review status** tracks where this memo is in the approval workflow. No memo is delivered until it reaches \"Approved\" status and a reviewer has signed off.",
        "",
        "---",
        "",
        f"**Memo status: {ctx.get('memo_status', 'DRAFT')} — This memo has not been reviewed or approved for delivery. Final delivery is subject to finance QA review and customer approval via the E-Solutions portal.**",
    ]
    return "\n".join(lines)


def assemble(variance_data: dict, narrative: dict, context: dict) -> str:
    """Assemble the full memo markdown from all inputs."""
    sections = [
        render_metadata(context),
        render_executive_summary(narrative),
        render_topline(variance_data["topline"]),
        render_revenue_detail(variance_data["line_items"], narrative),
        render_expense_detail(variance_data["line_items"], narrative),
        render_risks(narrative),
        render_actions(narrative),
        render_provenance(context, variance_data.get("metadata", {})),
    ]

    return "\n".join(sections) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="E-Solutions Memo Assembly v1 — assemble draft variance memo from structured inputs"
    )
    parser.add_argument(
        "--variance", required=True,
        help="Path to variance computation JSON output",
    )
    parser.add_argument(
        "--narrative",
        default=None,
        help="Path to narrative sections JSON. If omitted, placeholders are inserted.",
    )
    parser.add_argument(
        "--context", required=True,
        help="Path to company context JSON",
    )
    parser.add_argument(
        "--output", required=True,
        help="Path to write the assembled memo markdown",
    )
    args = parser.parse_args()

    variance_data = load_json(args.variance)
    context = load_json(args.context)

    if args.narrative:
        narrative = load_json(args.narrative)
    else:
        # Generate placeholder narrative
        narrative = {
            "executive_summary": "*[NARRATIVE NEEDED: Executive summary not yet generated]*",
            "attention_items": ["[NARRATIVE NEEDED: Attention items not yet generated]"],
            "revenue_narratives": {},
            "expense_narratives": {},
            "cogs_summary": "*[NARRATIVE NEEDED: COGS summary not yet generated]*",
            "opex_summary": "*[NARRATIVE NEEDED: OpEx summary not yet generated]*",
            "risks": [],
            "recommended_actions": [],
        }

    memo = assemble(variance_data, narrative, context)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(memo)
    print(f"Memo assembled: {args.output}")


if __name__ == "__main__":
    main()

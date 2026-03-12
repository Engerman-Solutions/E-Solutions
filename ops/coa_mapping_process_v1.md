# COA Mapping Process v1

**Purpose:** Define how customer chart of accounts data is mapped to E-Solutions standard categories for variance analysis and memo production.

**Alignment:** Stage 3 of `ops/live_pilot_workflow_v1.md`

---

## Overview

Every customer uses different account codes, names, and structures in their general ledger. Before E-Solutions can compute variances and produce a memo, each customer account must be mapped to a standard category that determines how it appears in the memo.

This mapping is created once during pilot kickoff (Days 1–3) and reused each cycle. If the customer revises their COA, the mapping is re-versioned.

---

## Standard Categories

E-Solutions uses 3 top-level categories and multiple memo sections:

| Normalized Category | Memo Section | Description |
|---------------------|-------------|-------------|
| Revenue | Revenue Variance Detail | All income lines (subscriptions, services, usage, other) |
| COGS | Expense Variance Detail — COGS | Direct costs of delivering service (hosting, API costs, support) |
| Operating Expenses | Expense Variance Detail — OpEx | All other operating costs (salaries, marketing, G&A, etc.) |

### Variance Groups (for memo organization)

Revenue: Subscription Revenue, Professional Services, Usage Revenue, Other Revenue
COGS: Infrastructure, Variable COGS, Support
OpEx: Engineering, Sales & Marketing, G&A, T&E, People Ops

These groups determine how line items are clustered in the memo narrative sections.

---

## Mapping Template

The mapping template is a CSV file (`ops/coa_mapping_template_v1.csv`) with the following columns:

| Column | Required | Description |
|--------|----------|-------------|
| `source_account_code` | Yes | The customer's GL account code (e.g., "4100") |
| `source_account_name` | Yes | The customer's account name (e.g., "SaaS Subscription Revenue") |
| `normalized_category` | Yes | E-Solutions standard category: Revenue, COGS, or Operating Expenses |
| `memo_section` | Yes | Which section of the memo this appears in |
| `variance_group` | Yes | Sub-grouping within the memo section |
| `notes` | No | Reviewer notes, edge cases, or clarifications |

The template ships pre-populated with common SaaS account structures. Customers with different structures will need customization during kickoff.

---

## Mapping Process

### Step 1: Receive customer COA

During pilot kickoff, request the customer's chart of accounts. This can be:
- A COA export from their accounting system (QBO, Xero, NetSuite)
- A list of accounts used in their GL export
- The GL export itself (account codes and names can be extracted)

### Step 2: Create the initial mapping

1. Start from `ops/coa_mapping_template_v1.csv`
2. For each customer account, find the best match in the template
3. For accounts that do not match:
   - Map to the most appropriate `normalized_category`
   - Assign a `memo_section` and `variance_group`
   - Add a note explaining the mapping rationale
4. Flag any ambiguous accounts for customer confirmation

### Step 3: Customer review

Send the draft mapping to the customer's Controller for review. Key questions:
- "Does this grouping match how you think about your P&L?"
- "Are there any accounts that should be categorized differently?"
- "Are there accounts in your GL that we missed?"

Adjust the mapping based on feedback.

### Step 4: Version and store

Save the final mapping as:
```
data/{customer_id}/coa_mapping_v{version}.csv
```

Record the version in the memo's data provenance section. If the mapping changes in a future cycle, increment the version number. Prior memos remain tied to the version used when they were produced.

---

## Handling Common Edge Cases

| Scenario | Resolution |
|----------|------------|
| Customer has sub-accounts (e.g., 6100.01, 6100.02) | Map each sub-account individually. Group under the same variance_group. |
| Customer uses account names that do not match any template entry | Map manually. Add a note. |
| Customer has accounts with no activity (zero actual and budget) | Include in mapping but skip in memo output. |
| Customer categorizes an item differently than E-Solutions standard | Follow the customer's categorization unless it would mislead the memo reader. Note the deviation. |
| Customer revises their COA mid-pilot | Create a new mapping version. Prior memos retain their original mapping version. |
| Customer has "Other" or uncategorized accounts | Map to the closest category. Flag for customer confirmation. Do not leave unmapped. |

---

## Versioning Rules

- Each mapping file is versioned: `coa_mapping_v1.csv`, `coa_mapping_v2.csv`, etc.
- The version used for a memo is recorded in the Data Provenance section (e.g., "COA template: coa-template-novaCRM, v1.2")
- A mapping is never edited in place after it has been used in a delivered memo. Revisions create a new version.
- Prior memos can always be reproduced using the version that was active when they were created.

---

## Pilot-Specific Notes

- For the first pilot, the mapping is created manually in a spreadsheet (Excel or Google Sheets) and exported as CSV
- The founder or operator creates the initial mapping based on the customer's GL export
- Customer review happens via email or during a kickoff call — no portal workflow yet
- Semi-automated mapping (ML-suggested categories) is planned for Cycle 2+ but is not required for pilot launch

---

**This process will be refined based on actual pilot experience. The goal is to make mapping fast and accurate, not perfect on the first attempt.**

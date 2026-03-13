# Target List Fields v1

**Purpose:** Field definitions and usage instructions for `target_list_template_v1.csv`.

---

## Field Definitions

### Company Information

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `company_name` | Text | Legal or common company name | Acme Analytics |
| `website` | URL | Company website | acmeanalytics.com |
| `industry` | Text | Primary industry vertical | B2B SaaS |
| `stage` | Enum | Funding stage: Seed, Series A, Series B, Other | Series A |
| `employee_count` | Number | Approximate headcount (from LinkedIn or Crunchbase) | 45 |
| `estimated_arr_band` | Text | Revenue range: <$1M, $1M–$5M, $5M–$20M, $20M–$30M, >$30M | $1M–$5M |
| `finance_team_size` | Number | Number of finance/accounting staff (0 = founder does it) | 1 |
| `accounting_system` | Text | QBO, Xero, NetSuite, Unknown | QBO |

### Buyer Information

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `buyer_name` | Text | Name of the target contact | Jane Smith |
| `buyer_role` | Text | Title or role: CFO, VP Finance, Controller, Founder, Head of FP&A | Controller |
| `buyer_email` | Text | Email address (if known) | jane@acme.com |
| `buyer_linkedin` | URL | LinkedIn profile URL | linkedin.com/in/janesmith |
| `contact_channel` | Text | How you plan to reach them: Email, LinkedIn, Warm Intro, Event | Email |

### Scoring

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `fit_score` | Number | Total score from the account targeting rubric (0–30) | 24 |
| `priority_tier` | Enum | A (25–30), B (18–24), C (12–17), D (<12) | B |
| `urgency_signal` | Text | What triggered outreach: Recent raise, New hire, Job posting, None | Recent raise |

### Outreach Tracking

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `first_touch_date` | Date | Date of first outreach message (YYYY-MM-DD) | 2026-03-15 |
| `last_touch_date` | Date | Date of most recent outreach (YYYY-MM-DD) | 2026-03-20 |
| `touch_count` | Number | Total messages sent (first touch + follow-ups) | 2 |
| `sequence_status` | Enum | Not Started, In Progress, Complete, Paused | In Progress |
| `interest_level` | Enum | Hot, Warm, Cold, Disqualified, Unknown | Warm |

### Next Steps

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `next_step` | Text | What happens next | Send follow-up 2 |
| `next_follow_up_date` | Date | When to follow up (YYYY-MM-DD) | 2026-03-25 |

### Feedback

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `objections` | Text | Objections raised (semicolon-separated if multiple) | Trust; Pricing |
| `pricing_reaction` | Enum | Positive, Neutral, Pushback, Not Discussed | Neutral |
| `feature_requests` | Text | Features they asked about | Integration with NetSuite |
| `competitive_mentions` | Text | Tools or services they compared us to | Mosaic |

### Call Tracking

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `call_date` | Date | Date of discovery/demo call (YYYY-MM-DD) | 2026-03-22 |
| `call_outcome` | Enum | Advance, Nurture, Disqualify, No Show | Advance |

### General

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `notes` | Text | Free-form notes | Met at SaaStr meetup. Interested in test run. |

---

## How to Use

### Getting Started

1. Copy the CSV to a Google Sheet or open in Excel for easier editing.
2. Add 20–30 candidate companies using the ICP shortlist framework.
3. Score each company using the account targeting rubric.
4. Sort by `fit_score` descending. Top 10–15 become the active shortlist.

### Weekly Workflow

1. **Monday:** Add new prospects. Score them. Update `priority_tier`.
2. **Tuesday–Thursday:** Send outreach. Update `first_touch_date`, `last_touch_date`, `touch_count`, and `sequence_status`.
3. **After each reply:** Update `interest_level`, `objections`, `next_step`, `next_follow_up_date`.
4. **After each call:** Update `call_date`, `call_outcome`, and feedback fields.
5. **Friday:** Review the list. Flag prospects due for follow-up next week.

### Status Transitions

```
Not Started → In Progress (first touch sent)
In Progress → Complete (breakup sent or reply received)
In Progress → Paused (deferred by prospect, revisit later)
Complete → In Progress (restarted after new trigger)
Any → Disqualified (not a fit)
```

### Filtering Views

Common filters for weekly review:

| View | Filter |
|------|--------|
| Active outreach | `sequence_status` = In Progress |
| Due for follow-up | `next_follow_up_date` <= today |
| Hot prospects | `interest_level` = Hot |
| Ready for call | `interest_level` = Hot AND `call_date` is empty |
| Stale prospects | `last_touch_date` > 21 days ago AND `sequence_status` = In Progress |
| Top targets | `priority_tier` = A |

### Data Hygiene

- Update the list at least weekly.
- Remove or archive prospects who have been disqualified.
- Re-score prospects monthly as you learn new information.
- Keep `notes` concise — one or two sentences per update, not a journal.
- Do not delete rows. Change `interest_level` to Disqualified and add a note explaining why.

# Monthly Variance Memo

**Company:** NovaCRM, Inc.
**Period:** February 2026
**Prepared by:** E-Solutions Variance Workflow
**Status:** DRAFT — Pending Finance QA Review
**Checkpoint ID:** VR-2026-02-0047
**Data validated:** 2026-03-05 09:14 UTC | 18 line items | Schema pass | Injection scan pass

---

## Executive Summary

February revenue came in $15.4K above budget (+3.4%), driven by strong SaaS subscription growth that more than offset a shortfall in professional services. Total operating expenses exceeded budget by $17.9K (+4.6%), primarily from unbudgeted legal costs tied to the Series B financing process and accelerated engineering contractor spend for the API v2 launch. Net loss for the month was ($2.0K) worse than plan.

**Bottom line:** Revenue trajectory is healthy. Expense overages are explainable and largely non-recurring. Two items require leadership attention: the professional services pipeline gap and rising contractor costs.

---

## Topline Performance Summary

| Metric | Actual | Budget | Variance ($) | Variance (%) |
|--------|--------|--------|-------------|-------------|
| Total Revenue | $473,400 | $458,000 | +$15,400 | +3.4% |
| Total COGS | $89,700 | $85,500 | +$4,200 | +4.9% |
| Gross Profit | $383,700 | $372,500 | +$11,200 | +3.0% |
| Gross Margin | 81.1% | 81.3% | -0.3 pts | — |
| Total OpEx | $352,400 | $342,500 | +$9,900 | +2.9% |
| Operating Income (Loss) | $31,300 | $30,000 | +$1,300 | +4.3% |

| KPI | February | January | MoM Change |
|-----|----------|---------|------------|
| MRR | $412,800 | $378,200 | +9.1% |
| Net New MRR | $34,600 | $22,800 | +51.8% |
| Gross Margin | 81.1% | 80.4% | +0.7 pts |
| Headcount | 62 | 58 | +4 |
| Burn Multiple | 0.9x | 1.1x | Improving |

---

## Revenue Variance Analysis

### SaaS Subscription Revenue: +$17,800 vs. budget (+4.5%)

Actual: $412,800 | Budget: $395,000 | Prior month: $378,200

Primary drivers:
- **3 enterprise upsells closed** in late January that began billing in February, contributing ~$12K in incremental MRR
- **Net retention strong** at 108% annualized — expansion from existing accounts outpacing churn
- Logo churn was 1 account ($2,800 MRR), below the budgeted 2 accounts

This is the third consecutive month of positive subscription variance. The upsell pipeline for Q2 remains healthy.

### Professional Services Revenue: -$6,500 vs. budget (-14.4%)

Actual: $38,500 | Budget: $45,000 | Prior month: $41,200

Primary drivers:
- **2 implementation projects delayed** to March due to customer-side resource constraints
- Services backlog remains intact — the revenue is deferred, not lost
- One project scope was reduced from $18K to $12K after customer narrowed requirements

**Action required:** Review the Q2 services pipeline with the sales team. If delays persist, consider adjusting the services revenue forecast for Q2.

### Usage-Based Revenue: +$4,100 vs. budget (+22.8%)

Actual: $22,100 | Budget: $18,000 | Prior month: $16,800

Primary drivers:
- **API call volumes exceeded expectations** as two customers moved into production workloads
- Usage pricing is performing as designed — grows with customer adoption without requiring sales intervention

No action required. Monitor for sustainability in March.

---

## Expense Variance Analysis

### COGS: +$4,200 vs. budget (+4.9%)

| Line Item | Actual | Budget | Variance |
|-----------|--------|--------|----------|
| Cloud Infrastructure (AWS) | $52,300 | $48,000 | +$4,300 (+9.0%) |
| Third-Party API Costs | $8,900 | $7,500 | +$1,400 (+18.7%) |
| Customer Support Team | $28,500 | $30,000 | -$1,500 (-5.0%) |

- **AWS overage** driven by usage spike from the API v2 staging environment and load testing. Approximately $2,500 of the overage is non-recurring (staging teardown completed March 1). Remaining $1,800 reflects organic growth in production workloads.
- **API costs** up due to higher-than-expected transaction volumes from the usage-based customers. Correlated with the usage revenue beat.
- **Support team** came in under budget — one support hire planned for February was pushed to March.

Gross margin at 81.1% remains within the 80–83% target band.

### Operating Expenses: +$9,900 vs. budget (+2.9%)

**Favorable variances:**
| Line Item | Actual | Budget | Variance |
|-----------|--------|--------|----------|
| Engineering Salaries | $142,000 | $148,000 | -$6,000 (-4.1%) |
| Paid Advertising | $15,200 | $20,000 | -$4,800 (-24.0%) |
| Office & Facilities | $8,200 | $8,500 | -$300 (-3.5%) |

- Engineering salaries favorable because one senior hire started Feb 15 instead of Feb 1 (half-month impact)
- Paid advertising underspend was intentional — paused two underperforming campaigns pending creative refresh

**Unfavorable variances:**
| Line Item | Actual | Budget | Variance |
|-----------|--------|--------|----------|
| Engineering Contractors | $18,500 | $12,000 | +$6,500 (+54.2%) |
| Legal & Professional Fees | $11,200 | $6,000 | +$5,200 (+86.7%) |
| Recruiting & Hiring | $8,400 | $4,000 | +$4,400 (+110.0%) |
| Travel & Entertainment | $6,700 | $5,000 | +$1,700 (+34.0%) |
| Events & Sponsorships | $4,800 | $3,000 | +$1,800 (+60.0%) |

- **Engineering contractors** (+$6.5K): Additional frontend contractor brought on for 4 weeks to accelerate API v2 dashboard. Expected to roll off mid-March. If the project extends, this becomes a recurring variance.
- **Legal fees** (+$5.2K): Series B term sheet review and IP assignment cleanup. Non-recurring — expected to normalize in March assuming financing closes.
- **Recruiting** (+$4.4K): Agency fees for 2 active searches (senior engineer, customer success lead). Both roles are budgeted hires; the recruiting spend was underestimated in the annual plan.
- **Travel** (+$1.7K): Founder attended 2 unplanned customer meetings for renewal discussions. Both renewals were secured.
- **Events** (+$1.8K): Sponsored a fintech meetup not in the original plan. Generated 3 qualified leads.

---

## Headcount Variance

| Department | Actual | Budget | Variance |
|------------|--------|--------|----------|
| Engineering | 22 | 23 | -1 (hire in progress) |
| Sales & Marketing | 12 | 12 | — |
| Customer Support | 8 | 9 | -1 (pushed to March) |
| G&A | 6 | 6 | — |
| Product | 4 | 4 | — |
| Contractors | 10 | 8 | +2 |
| **Total** | **62** | **62** | **—** |

Net headcount is on plan. The mix is shifted slightly toward contractors, which creates flexibility but may need correction if the API v2 project extends.

---

## Risks and Watchouts

1. **Professional services pipeline.** Two delayed projects and one scope reduction signal potential softness. If Q2 services revenue underperforms by a similar margin, the cumulative impact is material (~$20K+ per month).

2. **Contractor spend creep.** Engineering contractor costs have increased 95% over two months ($9.5K → $18.5K). The current engagement has a defined end date (mid-March), but the pattern warrants monitoring.

3. **AWS cost trajectory.** After removing the non-recurring staging costs, the underlying growth rate in cloud infrastructure (~4% MoM) exceeds the budgeted 2% MoM. If sustained, this adds ~$15K annually vs. plan.

4. **Recruiting costs underbudgeted.** Agency fees are running 2x the annual plan rate. Consider whether to renegotiate agency terms or shift to direct sourcing for remaining hires.

---

## Recommended Actions

1. **Review Q2 professional services forecast** with the sales team by March 15. Confirm whether the two delayed projects are rescheduled and whether the pipeline supports the original quarterly target.

2. **Confirm contractor roll-off** for the frontend engagement by mid-March. If the API v2 project requires extension, bring a budget revision to the next leadership meeting.

3. **Audit AWS spending** by tagging workloads to identify cost drivers. Set up a monthly cost alert at 105% of budget as an early warning.

4. **Decide on recruiting approach** for remaining open roles: continue with agency at current rates, renegotiate terms, or shift to direct sourcing.

---

## Data Provenance

| Item | Detail |
|------|--------|
| Source system | QuickBooks Online (GL export) |
| Export date | 2026-03-04 |
| Budget source | Board-approved 2026 annual budget, v2.1 |
| Prior period | January 2026 actuals (validated) |
| Validation | Schema pass, COA mapped (v1.2), injection scan clear |
| Checkpoint ID | VR-2026-02-0047 |
| Analysis model | E-Solutions variance engine v0.1 |
| Review status | DRAFT — pending finance QA review |

---

*This memo was produced by the E-Solutions variance workflow. All inputs were validated against the company's chart of accounts before analysis. The checkpoint ID above can be used to reproduce this analysis from the original source data. Final delivery is subject to human finance QA review and approval.*

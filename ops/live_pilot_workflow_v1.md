# Live Pilot Delivery Workflow v1

**Purpose:** Define the end-to-end operational workflow for delivering monthly variance memos during the 90-day design partner pilot. This is the operating playbook for Cycle 0 (test run) through Cycle 3.

**Scope:** Single customer, single deliverable (monthly variance memo), manual upload intake, AI-assisted analysis, human QA review, portal approval, PDF delivery.

---

## Workflow Overview

```
Upload → Validate → Map → Analyze → Draft → Review → Approve → Deliver
```

Each stage has defined inputs, outputs, pass/fail criteria, and a responsible party. No stage proceeds until the prior stage passes.

---

## Stage 1: Intake (Upload)

**Who:** Customer (Controller or designated finance contact)
**How:** Manual file upload via secure web portal
**Inputs:**
- General ledger export (CSV or Excel — trial balance or transaction detail)
- Budget file (CSV or Excel — annual budget by month)
- Chart of accounts (first cycle only, or when revised)

**Acceptance criteria:**
- Files are non-empty and in a supported format (CSV, XLSX, XLS)
- File size within limits (< 25 MB per file)
- Period header matches the expected reporting month

**Output:** Raw files stored in customer namespace with upload timestamp and file hash

**Failure handling:**
- Missing or corrupt files → automated rejection email with specific error, re-upload requested
- Wrong period → flagged with warning; customer confirms or re-uploads
- Upload not received by SLA cutoff (business day 5 of the month) → proactive outreach to customer

**Manual in pilot:** Upload portal may be a simple authenticated file drop (Google Drive shared folder or basic web form) rather than a custom-built portal. The key requirement is file isolation per customer and upload logging.

---

## Stage 2: Validation

**Who:** E-Solutions (automated + manual verification)
**Inputs:** Raw uploaded files from Stage 1

**Checks performed:**
1. **Schema validation** — column headers match expected GL/budget format; required fields present
2. **Period matching** — GL period matches the target reporting month; budget file covers the period
3. **Balance verification** — debits equal credits (if trial balance); total revenue + expenses tie to a control total if provided
4. **Completeness** — all expected account categories present (revenue, COGS, OpEx at minimum)
5. **Injection scan** — no formula injection, script tags, or adversarial patterns in text fields
6. **Duplicate detection** — flag if the same file (by hash) was uploaded in a prior cycle

**Output:** Validation report with pass/fail status, error list, and warning list

**Pass criteria:** Zero errors. Warnings are logged but do not block.

**Failure handling:**
- Validation errors → customer notified with specific issues and instructions to re-upload corrected files
- No analysis proceeds until validation passes — this is non-negotiable
- If the customer cannot resolve validation errors within 48 hours, E-Solutions offers a 30-minute screen-share to assist

**Manual in pilot:** Validation checks are scripted (Python or spreadsheet formulas) but may require manual execution and review of results. Injection scan may be a checklist review rather than automated scanning in the first cycle.

---

## Stage 3: COA Mapping and Normalization

**Who:** E-Solutions
**Inputs:** Validated GL and budget files, customer's chart of accounts

**Process:**
1. Map customer account codes to E-Solutions standard categories (Revenue, COGS, OpEx subcategories, Headcount)
2. Resolve any unmapped accounts — flag for customer confirmation if ambiguous
3. Normalize account names to consistent format for memo output
4. Apply materiality thresholds (default: variances > $5K or > 10% flagged as material)
5. Version the COA mapping template (hash + version number)

**Output:** Mapped and normalized data file; COA mapping template (versioned)

**First-cycle specifics:**
- COA mapping is done collaboratively with the customer during kickoff (Days 1–3)
- Template is saved and reused in subsequent cycles
- If the customer revises their COA mid-pilot, the template is re-versioned and prior memos remain tied to the version used

**Manual in pilot:** COA mapping is likely a manual spreadsheet exercise in Cycle 0. A semi-automated mapping tool is a build priority for Cycle 2+.

---

## Stage 4: Variance Analysis and Memo Drafting

**Who:** E-Solutions (AI-assisted)
**Inputs:** Mapped and normalized data; prior-period data (if available); COA template

**Process:**
1. Compute actuals vs. budget for every mapped line item
2. Compute month-over-month trends (if prior-period data exists)
3. Flag material variances per threshold settings
4. Generate draft narrative explanations for each material variance
5. Compute key operating metrics (MRR, gross margin, burn multiple, headcount)
6. Assemble topline performance summary, revenue detail, expense detail, headcount, risks/watchouts, recommended actions
7. Generate executive summary (2–3 sentences + attention items)
8. Attach data provenance metadata (checkpoint ID, source file hashes, validation results, COA template version)

**AI usage:**
- Variance computation: deterministic (no AI needed)
- Narrative generation: AI-assisted (LLM drafts explanations based on variance data, account context, and prior-period patterns)
- Executive summary: AI-assisted (LLM synthesizes the full analysis into 2–3 sentences)
- Recommended actions: AI-suggested, human-edited

**Output:** Draft variance memo in markdown format; analysis checkpoint ID assigned

**Quality gates before advancing to review:**
- All material variances have narrative explanations
- Topline numbers tie (revenue - COGS = gross profit; gross profit - OpEx = operating income)
- No placeholder text or incomplete sections
- Checkpoint ID and provenance metadata populated

**Manual in pilot:** Narrative generation may use prompted AI (Claude API or manual prompting) with significant human editing. The goal is to reduce human effort each cycle as prompts improve. Variance computation should be scripted from Cycle 0.

---

## Stage 5: Finance QA Review

**Who:** Finance QA reviewer (contracted or internal)
**Inputs:** Draft memo from Stage 4

**Review checklist:**
1. **Numbers accuracy** — spot-check 3–5 line items against source GL; verify topline totals tie
2. **Narrative quality** — explanations are factually accurate, specific (not generic), and appropriate for a board audience
3. **Materiality** — all material variances are addressed; no significant items were missed
4. **Formatting** — tables are correct, variance percentages are accurate, Signal/Recurring columns populated
5. **Tone and language** — professional, concise, no jargon overload, no speculative claims without data support
6. **Provenance** — checkpoint ID, validation status, and source metadata are present and correct
7. **Risks and actions** — realistic, specific, with named owners and dates

**Reviewer workflow:**
1. Receive draft memo via secure review interface (initially: shared doc with comment access)
2. Mark issues as "must fix" or "suggestion"
3. Return annotated memo to analysis team
4. Analysis team resolves all "must fix" items
5. Reviewer performs final check on resolved items
6. Reviewer marks memo as "QA Approved" with timestamp

**SLA:** Review completed within 12 hours of draft submission. Total cycle (draft → QA approved) within 24 hours.

**Failure handling:**
- If the reviewer identifies a systemic data issue (e.g., wrong period, missing accounts), the memo returns to Stage 2 (Validation) and the customer is notified
- If the reviewer identifies > 5 narrative issues, the draft returns to Stage 4 for substantive revision before re-review

**Manual in pilot:** Review is entirely manual. The reviewer works in a shared document (Google Docs or equivalent). A purpose-built reviewer UI with PII masking is a build priority for post-pilot.

---

## Stage 6: Customer Approval

**Who:** Customer (CFO, Founder, or Controller)
**Inputs:** QA-approved memo

**Process:**
1. Customer receives notification that the memo is ready for review (email + portal notification)
2. Customer reviews the memo in the portal (initially: secure shared link)
3. Customer can:
   - **Approve** — memo proceeds to delivery
   - **Request changes** — specific comments on what needs revision; memo returns to Stage 4 or 5 depending on the nature of changes
4. Customer approval is logged with timestamp

**SLA:** Customer has 48 hours to review. If no response, a single follow-up is sent. The memo is not delivered without explicit approval.

**Manual in pilot:** Approval may be via email confirmation ("Approved" reply) rather than a portal button. The approval is logged regardless of mechanism.

---

## Stage 7: Delivery

**Who:** E-Solutions
**Inputs:** Approved memo

**Process:**
1. Convert approved markdown memo to PDF using format notes (see `deliverables/sample_variance_memo_format_notes_v1.md`)
2. Final visual QA on PDF formatting (tables render correctly, color coding intact, page breaks sensible)
3. Upload PDF to secure customer portal
4. Send encrypted email with PDF attachment and portal link
5. Log delivery timestamp and checkpoint ID

**Output:** Board-ready PDF delivered to customer via portal + encrypted email

**SLA:** Delivery within 4 hours of customer approval.

**Manual in pilot:** PDF conversion is manual (Pandoc, Typst, or Google Docs formatted export). Encrypted email may be a password-protected PDF or a secure link rather than true end-to-end encryption. The key requirement is that the memo is not sent as a plain-text email attachment.

---

## End-to-End SLA

| Stage | Target time | Cumulative |
|-------|-------------|------------|
| Upload received | Day 0 | Day 0 |
| Validation complete | +4 hours | Day 0 |
| COA mapping (first cycle only) | +1–2 days | Day 1–2 |
| Analysis + draft | +8 hours | Day 1 (or Day 2 if first cycle) |
| QA review | +12 hours | Day 1–2 |
| Customer review | +48 hours | Day 2–4 |
| Delivery | +4 hours | Day 2–4 |
| **Total (repeat cycle)** | **Under 48 hours** from validated upload | |
| **Total (first cycle)** | **Under 5 business days** including COA mapping | |

---

## Manual vs. Automated Split (Pilot)

| Component | Pilot state | Target state (post-pilot) |
|-----------|-------------|--------------------------|
| File upload | Manual (secure file drop) | Self-service portal with format validation |
| Schema validation | Scripted (Python/spreadsheet) | Automated pipeline with real-time feedback |
| Injection scan | Checklist review | Automated scan on upload |
| COA mapping | Manual spreadsheet + human review | Semi-automated with ML suggestions |
| Variance computation | Scripted (Python/spreadsheet) | Fully automated pipeline |
| Narrative generation | Prompted AI + significant human editing | AI-generated with light human editing |
| Executive summary | AI-drafted, human-edited | AI-generated with reviewer approval |
| QA review | Fully manual (Google Docs) | Clean-room reviewer UI with PII masking |
| Customer approval | Email confirmation | Portal approval with audit log |
| PDF conversion | Manual (Pandoc/Typst/Google Docs) | Automated rendering pipeline |
| Delivery | Manual email + file upload | Automated portal + encrypted email |
| Checkpoint/provenance | Manual metadata entry | Auto-generated from pipeline state |

---

## Failure and Exception Handling

| Scenario | Response | Escalation |
|----------|----------|------------|
| Customer uploads wrong file format | Automated rejection with format guidance | None — customer self-serves |
| Validation finds errors in GL data | Customer notified; screen-share offered if unresolved in 48h | Founder involvement if data issues persist |
| COA mapping has ambiguous accounts | Flag to customer for clarification; do not guess | Delay analysis until confirmed |
| AI narrative is inaccurate or generic | Reviewer flags; human rewrites the narrative | If systemic, review AI prompts and retrain |
| Reviewer finds data discrepancy | Memo returns to validation; customer notified | Founder notified if it affects SLA |
| Customer requests major revisions | Treat as a new draft cycle (Stage 4–7) | No additional charge during pilot |
| Customer does not respond within 48h | Single follow-up email; log as delayed | Founder outreach if pattern repeats |
| SLA breach (> 48h from validated upload) | Post-mortem documented; customer notified proactively | Root cause analysis and process fix |
| Reviewer unavailable | Backup reviewer or founder performs review | Plan reviewer redundancy for post-pilot |

---

## Pilot Readiness Checklist

Before onboarding the first design partner, the following must be in place:

### Must have (blocks pilot start)

- [ ] Secure file upload mechanism operational (even if simple)
- [ ] Validation scripts written and tested against sample data
- [ ] COA mapping template and process documented
- [ ] Variance computation scripts written and tested
- [ ] AI narrative generation workflow defined (prompts, model, review process)
- [ ] At least 1 finance QA reviewer identified and briefed
- [ ] Reviewer checklist documented
- [ ] Memo markdown template finalized (based on sample_variance_memo_v2.md)
- [ ] PDF conversion process tested and producing clean output
- [ ] Customer communication templates ready (upload instructions, validation errors, approval request, delivery notification)
- [ ] Data Processing Agreement drafted
- [ ] Customer namespace isolation implemented (even if just separate folders)

### Should have (improves quality but does not block)

- [ ] Prior-period data for trend analysis
- [ ] Materiality thresholds confirmed with customer
- [ ] Backup reviewer identified
- [ ] Feedback collection process defined (weekly call agenda)
- [ ] SLA tracking mechanism (even a simple spreadsheet)

### Nice to have (plan for Cycle 2+)

- [ ] Automated validation pipeline
- [ ] Semi-automated COA mapping
- [ ] Reviewer UI with PII masking
- [ ] Portal-based approval workflow
- [ ] Automated PDF rendering
- [ ] Encrypted email delivery
- [ ] Checkpoint ID auto-generation

---

## Cycle-Over-Cycle Improvement Plan

| Cycle | Focus |
|-------|-------|
| **Cycle 0 (test run)** | Validate the end-to-end workflow with sample or prior-month data. Identify bottlenecks. Establish the COA mapping. Calibrate AI narrative quality. |
| **Cycle 1** | First live memo. Measure actual time per stage. Collect customer feedback on format, depth, and accuracy. |
| **Cycle 2** | Implement top 3 customer feedback items. Reduce manual effort in the highest-time stages. Begin automating validation and computation. |
| **Cycle 3** | Deliver a memo that meets the quality bar for board distribution. Conduct pilot review with customer. Present continuation proposal. |

---

**This document is the operational playbook for the first design partner pilot. It will be updated after each cycle based on actual experience.**

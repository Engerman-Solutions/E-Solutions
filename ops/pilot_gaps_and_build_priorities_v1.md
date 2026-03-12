# Pilot Gaps and Build Priorities v1

**Purpose:** Assess what is ready, what needs manual process, what must be built before the first pilot, and what can wait. This document drives the pre-pilot sprint.

---

## Readiness Summary

| Area | Status | Notes |
|------|--------|-------|
| Sample deliverable | Ready | sample_variance_memo_v2.md demonstrates the target output |
| Pilot offer | Ready | pilot_package_v2.md ready to send to prospects |
| Demo flow | Ready | demo_narrative_v2.md with live and async versions |
| PDF format spec | Ready | format_notes_v1.md defines the target PDF layout |
| Delivery workflow | Defined | live_pilot_workflow_v1.md covers all stages |
| Validation pipeline | Not built | Scripts needed for schema, period, balance, injection checks |
| COA mapping | Not built | Manual process defined; no tooling yet |
| Variance computation | Not built | Logic defined in sample memo; scripts needed |
| AI narrative generation | Not built | Prompt engineering and model integration needed |
| Finance QA review process | Defined but not staffed | Reviewer checklist exists; no reviewer contracted |
| Customer portal | Not built | Secure file drop needed; approval workflow needed |
| PDF conversion pipeline | Not tested | Format notes exist; no template or automated pipeline |
| Data Processing Agreement | Not drafted | Required before customer provides real financial data |
| Customer communication templates | Not written | Upload instructions, error notifications, approval requests |

---

## Priority 1: Must Build Before First Pilot (Blocks Onboarding)

These items must be operational before a design partner provides real data.

### 1.1 Validation Scripts
**What:** Python scripts or equivalent to perform schema validation, period matching, balance verification, completeness checks, and injection scanning on uploaded GL and budget files.
**Why blocks:** No analysis runs on unvalidated data — this is a non-negotiable trust requirement (DEC-009).
**Effort estimate:** 3–5 days
**Approach:** Write against the sample_variance_data_v1.csv format. Test with intentional errors (missing fields, wrong period, formula injection). Output a structured validation report.

### 1.2 Variance Computation Scripts
**What:** Scripts that take validated, COA-mapped data and compute actuals vs. budget, variance dollars and percentages, MoM trends, and materiality flags.
**Why blocks:** This is the core analytical output. Without it, the memo cannot be produced.
**Effort estimate:** 2–3 days
**Approach:** Deterministic computation — no AI needed. Input: mapped CSV. Output: structured variance data (JSON or CSV) ready for memo assembly.

### 1.3 AI Narrative Generation Workflow
**What:** Defined prompts, model selection (Claude API), and human editing workflow for generating variance explanations, executive summary, risks, and recommended actions.
**Why blocks:** Narrative quality is the primary value proposition. Without a working AI + human workflow, the memo is just a table.
**Effort estimate:** 3–5 days (prompt engineering + testing)
**Approach:** Start with Claude API. Write system prompts for each narrative section. Test against sample data. Establish a human editing pass with tracked changes. Iterate prompts based on reviewer feedback.

### 1.4 COA Mapping Process
**What:** A documented, repeatable process for mapping customer account codes to E-Solutions standard categories. Initially a spreadsheet template.
**Why blocks:** Cannot compute variances without knowing which accounts map to which categories.
**Effort estimate:** 1–2 days
**Approach:** Create a standard category template (Revenue, COGS subcategories, OpEx subcategories, Headcount). Build a mapping spreadsheet that the customer fills in during kickoff. Version the mapping for audit trail.

### 1.5 Secure File Upload Mechanism
**What:** A secure way for customers to upload GL and budget files with per-customer isolation.
**Why blocks:** Cannot receive customer data without a secure, isolated upload path.
**Effort estimate:** 1–2 days
**Approach:** For the first pilot, a shared Google Drive folder (per customer, restricted access) or a simple authenticated web form (e.g., Typeform + Google Drive). Not ideal long-term but sufficient for Cycle 0. Must log upload timestamps.

### 1.6 Finance QA Reviewer
**What:** At least one qualified finance professional who can review draft memos for accuracy, narrative quality, and board-readiness.
**Why blocks:** Human review is mandatory before delivery (DEC-008). No reviewer = no delivery.
**Effort estimate:** Ongoing (contracting or hiring)
**Approach:** Contract a part-time reviewer with FP&A or controllership experience. Provide the reviewer checklist from the workflow doc. Budget for 2–4 hours per memo initially.

### 1.7 Data Processing Agreement
**What:** A legal document governing how E-Solutions handles customer financial data — retention, access controls, deletion, breach notification.
**Why blocks:** No serious finance team will provide real GL data without contractual data protection terms.
**Effort estimate:** 2–3 days (draft + legal review)
**Approach:** Start from a standard DPA template. Customize for the E-Solutions data handling workflow (namespace isolation, reviewer access controls, retention/deletion policy). Have legal counsel review before first pilot.

### 1.8 PDF Conversion (Tested)
**What:** A working process to convert the markdown memo to a polished PDF matching the format notes spec.
**Why blocks:** The deliverable is a PDF. Markdown is internal.
**Effort estimate:** 1–2 days
**Approach:** Test Pandoc with a custom HTML/CSS template or Typst. Verify tables render correctly, color coding works, page breaks are sensible. Produce a sample PDF from sample_variance_memo_v2.md and review.

---

## Priority 2: Should Build Before Cycle 1 (Improves Quality)

These items improve the pilot experience but do not block the test run (Cycle 0).

### 2.1 Customer Communication Templates
**What:** Email templates for: upload instructions, validation error notifications, memo ready for review, approval confirmation, delivery notification.
**Why important:** Professional communication builds trust. Ad hoc emails feel unpolished.
**Effort:** 1 day

### 2.2 SLA Tracking
**What:** A simple mechanism (spreadsheet or Notion board) to track time at each workflow stage per cycle.
**Why important:** Needed to measure whether the 48-hour SLA is being met and where bottlenecks occur.
**Effort:** Half day

### 2.3 Feedback Collection Process
**What:** A structured agenda for weekly design partner calls. What to ask, how to log feedback, how to prioritize changes.
**Why important:** Design partner feedback is the primary input for product improvement. Unstructured calls waste time.
**Effort:** Half day

### 2.4 Backup Reviewer Plan
**What:** Identify a second reviewer or define a fallback (founder reviews) if the primary reviewer is unavailable.
**Why important:** Single point of failure on a mandatory workflow step.
**Effort:** 1 day (identification + briefing)

---

## Priority 3: Build During or After Pilot (Can Wait)

These items are planned improvements but do not affect the first 1–2 cycles.

| Item | Target timing | Notes |
|------|---------------|-------|
| Automated validation pipeline | Cycle 2–3 | Replace manual script execution with automated intake processing |
| Semi-automated COA mapping | Cycle 2–3 | ML-suggested mappings with human confirmation |
| Reviewer UI (clean-room) | Post-pilot | Purpose-built interface with PII masking, approval controls, audit logging |
| Portal-based approval workflow | Post-pilot | Replace email-based approval with portal buttons and SoR |
| Automated PDF rendering | Post-pilot | Pipeline that converts markdown to formatted PDF without manual intervention |
| Encrypted email delivery | Post-pilot | True E2E encrypted delivery vs. password-protected PDF |
| Checkpoint auto-generation | Cycle 2 | Auto-assign checkpoint IDs from pipeline state instead of manual entry |
| Direct accounting system integrations | Post-pilot | Replace manual upload with API connections to QBO/Xero/NetSuite |
| Multi-entity consolidation | Post-pilot | Out of MVP scope; design partner feedback will determine priority |
| Landing page | Cycle 2–3 | Basic web presence for inbound interest; not needed for founder-led outbound |

---

## Biggest Risks to Pilot Success

| # | Risk | Impact | Mitigation |
|---|------|--------|------------|
| 1 | **No qualified reviewer available** | Cannot deliver any memo — mandatory gate | Start recruiting/contracting immediately; have founder as emergency backup |
| 2 | **AI narrative quality too low** | Excessive human editing negates the value proposition | Budget extra time for prompt iteration in pre-pilot sprint; accept higher human editing in Cycle 0 |
| 3 | **Customer data is messy** | Validation catches issues but resolution takes time; SLA at risk | Offer the 30-min screen-share for data issues; set expectations during kickoff that Cycle 0 may take longer |
| 4 | **PDF output looks unprofessional** | Undermines trust even if analysis is correct | Test PDF conversion thoroughly before pilot; have a manual formatting fallback |
| 5 | **Founder bandwidth** | Founder is doing sales, ops, and product simultaneously; pilot execution suffers | Ruthlessly prioritize pilot delivery over new sales during Cycle 0–1; defer non-essential work |
| 6 | **DPA not ready** | Blocks customer from providing real data | Start DPA draft immediately; do not wait for a signed design partner |
| 7 | **Scope creep from design partner** | Customer asks for forecasting, dashboards, custom reports during pilot | Firm scope boundaries in the pilot agreement; log requests for post-pilot evaluation |

---

## Recommended Pre-Pilot Sprint (2 Weeks)

| Week | Focus | Deliverables |
|------|-------|-------------|
| **Week 1** | Infrastructure + data pipeline | Validation scripts tested, variance computation scripts tested, COA mapping template created, secure file upload operational, DPA drafted |
| **Week 2** | AI + delivery + staffing | AI narrative prompts written and tested against sample data, PDF conversion tested, reviewer contracted and briefed, communication templates written, SLA tracker set up |

**Exit criterion for pre-pilot sprint:** Can produce a complete, polished variance memo PDF from sample_variance_data_v1.csv using the full workflow (upload → validate → map → analyze → draft → review → deliver) with all manual steps documented and all automated steps scripted.

---

**This document will be updated as items are completed or priorities shift based on design partner feedback.**

# Data Processing Agreement — Requirements and Open Questions v1

**Purpose:** Identify the minimum terms needed in a Data Processing Agreement before E-Solutions handles real customer financial data. This document is a starting point for drafting the DPA, not the DPA itself.

**Alignment:** Priority 1.7 in `ops/pilot_gaps_and_build_priorities_v1.md`, DEC-009 (trust and auditability)

---

## Why a DPA Is Required

No serious finance team will share GL exports, budget files, or chart of accounts data without contractual terms governing how that data is handled. Even at the pilot stage, a lightweight DPA signals professionalism and builds trust. The DPA does not need to be enterprise-grade for the first 1–2 design partners, but it must cover the essentials.

---

## Minimum Required Terms

### 1. Data Description

Define what data E-Solutions receives and processes:
- General ledger exports (account codes, account names, amounts by period)
- Budget files (annual or monthly budget by account)
- Chart of accounts (account structure and categorization)

Explicitly state what is NOT collected:
- No personally identifiable information (PII) of the customer's employees or customers (names, SSNs, addresses) — unless embedded in account names, in which case it is handled per the data handling terms below
- No bank account numbers, credit card numbers, or payment credentials
- No tax returns or filed financial statements

### 2. Purpose Limitation

Data is processed solely for the purpose of producing monthly variance memos as part of the E-Solutions pilot engagement. Data will not be used for:
- Training AI models on customer-specific data
- Sharing with other customers or third parties
- Marketing, benchmarking, or any purpose beyond memo production
- Any purpose not explicitly authorized by the customer

### 3. Data Isolation

- Each customer's data is stored in a separate namespace (Google Drive folder during pilot; isolated storage in post-pilot infrastructure)
- No cross-customer data access is possible by design
- E-Solutions operators access customer data only for the purpose of producing and delivering the variance memo

### 4. Access Controls

- Only authorized E-Solutions personnel (operator, finance QA reviewer) have access to customer data
- All access requires 2-factor authentication
- Customer is notified of which E-Solutions personnel have access
- Access is revoked within 24 hours of an employee/contractor departure

### 5. Data Retention and Deletion

| Data type | Retention period | Deletion method |
|-----------|-----------------|-----------------|
| Raw GL and budget files | Pilot duration + 90 days | Permanent deletion from cloud storage and local copies |
| COA mapping | Pilot duration + 90 days | Permanent deletion |
| Draft memos | Deleted after final memo is approved | Permanent deletion |
| Final delivered memos | Pilot duration + 12 months | Permanent deletion |

- Customer can request deletion of all their data at any time
- E-Solutions will confirm deletion in writing within 5 business days
- Deletion is permanent — no backups are retained after deletion confirmation

### 6. Security Measures

E-Solutions implements the following security measures during the pilot:
- Encryption at rest (Google Workspace AES-256)
- Encryption in transit (TLS)
- 2-factor authentication for all accounts with data access
- Access logging (Google Drive audit log)
- Injection scanning on uploaded files before processing
- No data is stored on unencrypted local devices

### 7. Sub-Processors

List any third-party services that process customer data:
- **Google Workspace** — file storage and collaboration (encrypted at rest and in transit)
- **Anthropic (Claude API)** — AI-assisted narrative generation. Customer data may be sent to the Claude API for analysis. Anthropic does not train on API data per their data usage policy.

Customer must be informed of sub-processors and consent to their use.

### 8. Breach Notification

- E-Solutions will notify the customer within 72 hours of discovering a data breach affecting their data
- Notification will include: nature of the breach, data affected, remediation steps, point of contact
- E-Solutions will cooperate with the customer's incident response process

### 9. Term and Termination

- DPA is effective for the duration of the pilot agreement
- Upon termination, data deletion follows the retention schedule above
- Customer may request immediate data deletion upon termination

---

## Open Questions (Require Legal Review)

### Q1: AI Model Training Exclusion
**Question:** How should we contractually guarantee that customer data sent to the Claude API is not used for model training?
**Current understanding:** Anthropic's API Terms of Service state that API inputs/outputs are not used for training. This should be referenced in the DPA.
**Action needed:** Verify current Anthropic API data usage policy and reference the specific clause.

### Q2: Indemnification and Liability
**Question:** What liability does E-Solutions assume if customer data is breached?
**Consideration:** At pilot stage, a liability cap (e.g., 12 months of fees paid) is standard. Unlimited liability is not appropriate for an early-stage company.
**Action needed:** Legal counsel to draft appropriate limitation of liability clause.

### Q3: Governing Law and Jurisdiction
**Question:** Which state/jurisdiction governs the DPA?
**Consideration:** Typically the state where E-Solutions is incorporated.
**Action needed:** Confirm E-Solutions' legal jurisdiction.

### Q4: Customer Audit Rights
**Question:** Should the customer have the right to audit E-Solutions' data handling practices?
**Consideration:** At pilot scale, a right to request documentation of security practices is reasonable. A full on-site audit right is excessive.
**Action needed:** Define a lightweight audit provision (e.g., customer can request a written description of security measures and access logs).

### Q5: Data Residency
**Question:** Does the customer require data to be stored in a specific geographic region?
**Consideration:** Google Workspace data region settings can restrict storage to specific regions. Most US-based pilot customers will not require this, but it should be addressed if asked.
**Action needed:** Determine default data region for E-Solutions Google Workspace.

### Q6: Regulatory Compliance
**Question:** Are there specific compliance frameworks (SOC 2, GDPR, CCPA) that pilot customers will require?
**Consideration:** SOC 2 Type II is not achievable at pilot stage. GDPR applies if processing data of EU-based companies. CCPA applies for California companies. The DPA should state current compliance status honestly and commit to a timeline for SOC 2 if demanded.
**Action needed:** Determine whether first target customers are US-only and whether GDPR applies.

---

## Recommended Next Steps

1. **Draft a lightweight DPA** (2–3 pages) covering the minimum required terms above. Use a standard DPA template as a starting point (e.g., AICPA sample, iubenda template, or a startup-friendly template from a law firm's resource library).
2. **Have legal counsel review** the draft before sending to any customer. Budget for a 1–2 hour review.
3. **Share the DPA with the first design partner** during or immediately after kickoff. Frame it as: "We take data security seriously. Here are the terms governing how we handle your data."
4. **Iterate based on customer feedback.** The first design partner may have additional requirements — log them and update the DPA.

---

## What the DPA Does Not Cover

- Pricing, service scope, or SLAs (covered in the pilot agreement / pilot package)
- Intellectual property rights to the memo output (customer owns their data; E-Solutions owns the methodology)
- Case study permissions (covered in the pilot agreement)
- Employment or contractor agreements for E-Solutions personnel

---

**This document identifies what must be in the DPA. The actual DPA should be drafted by or reviewed by legal counsel before use with any customer.**

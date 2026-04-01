# Microcopy Library

Tone: Calm, precise, audit-friendly. Finance software — not AI theater.
Voice: Direct, specific, grounded. Use outcomes, not adjectives.

---

## CTA Microcopy

### Explore CTAs (Low commitment, top-of-funnel)

| CTA | Context | Intent |
|-----|---------|--------|
| "See sample output" | Hero, homepage module | Deliver value before forms |
| "See a sample board memo" | Email, outreach | Specific deliverable framing |
| "View annotated example" | How-it-works section | Source-transparency angle |
| "How it works in 3 steps" | Homepage, nav | High information scent |
| "View full sample output" | Sample output preview | Deeper engagement |

### Evaluate CTAs (Mid-funnel, self-qualification)

| CTA | Context | Intent |
|-----|---------|--------|
| "Run on a sample dataset" | Sample output page | Hands-on evaluation |
| "Get the integration checklist" | How-it-works, integrations | Workflow fit check |
| "View governance details" | Trust module, security | Diligence depth |
| "Compare plans" | Pricing page | Self-qualification |
| "See what drives price" | Pricing anchor, homepage | Budget calibration |

### Convert CTAs (High-intent)

| CTA | Context | Intent |
|-----|---------|--------|
| "Book a 20-min evaluation" | Hero (secondary), CTA sections | Sales-led path |
| "Start pilot" | Pricing page, pilot card | Direct commitment |
| "Request pilot pricing" | CTA sections | Budget conversation |
| "Start security review" | Security page | Procurement path |
| "Request SOC 2 / DPA" | Security page, footer | Documentation request |
| "Book evaluation" | Nav CTA, inline CTAs | Universal high-intent |

---

## AI Trust Snippets

Use only what is operationally true. These are control statements, not marketing.

### Hallucination Containment

**Short (homepage):**
> "The system does not guess. If evidence is missing, it asks for clarification or flags uncertainty."

**Medium (security page):**
> "Outputs are grounded in your connected finance data. When evidence is missing, the system asks for clarification or flags uncertainty instead of guessing. Every claim in a generated narrative must cite source data from your GL export."

**Detailed (governance section):**
> "We don't guess; we cite, or abstain. The AI is scoped to specific, constrained tasks — variance analysis and narrative generation from structured financial data. It does not make autonomous decisions. When data is insufficient, the system flags uncertainty rather than fabricating explanations. Every output goes through human QA review before delivery."

### Data Control

**Short:**
> "Customer data is not used to train public models by default. You control retention and access."

**Medium:**
> "Your data is processed to generate your memo — nothing more. We don't use customer data to train public models by default. You control retention periods, and data deletion is available on request. Read-only access to accounting systems — we never write back."

### Audit Trail

**Short:**
> "Every narrative links to source data and includes timestamps and approval history."

**Medium:**
> "Full traceability from source to output: GL export → validation checkpoint → variance analysis → narrative generation → QA review → customer approval. Every step is timestamped, logged, and tied to a reproducible checkpoint ID."

---

## Error & Empty States

Finance users interpret errors as risk. Be specific, explain impact, give a safe next step.

### Data Errors

| State | Copy |
|-------|------|
| **Integration missing** | "We couldn't connect to your GL. No data was imported. Check permissions or try again." |
| **File format invalid** | "This file doesn't match our expected format. Upload a CSV or Excel export from QuickBooks, Xero, or NetSuite." |
| **Insufficient data** | "Not enough history to explain this variance yet. Add prior-period data or choose a different segment." |
| **Validation failed** | "3 line items failed validation. Review the flagged items below and re-upload, or contact support." |
| **Schema mismatch** | "Your account structure doesn't match the selected COA template. Update the template or contact us for help." |

### AI Behavior States

| State | Copy |
|-------|------|
| **AI abstains** | "I can't support that claim without source data. Add a data source or select a verified report." |
| **AI flags uncertainty** | "This explanation has low confidence. The variance may be driven by timing, not a trend. Reviewer: please verify." |
| **AI requests clarification** | "Revenue variance could be driven by 2 factors. Which should be the primary explanation? [Option A] [Option B]" |

### Empty States

| State | Copy |
|-------|------|
| **First time / no data** | "Upload a sample dataset to see a complete memo, evidence links, and an approval trail." |
| **No memos yet** | "No memos generated yet. Connect your GL export to get started." |
| **No approvals** | "This memo hasn't entered the approval workflow yet. It will move to QA review after generation." |

### Form States

| State | Copy |
|-------|------|
| **Required field** | "This field is required." |
| **Invalid email** | "Enter a valid email address." |
| **Form submitted** | "Thanks — we'll be in touch within 1 business day." |
| **Submission error** | "Something went wrong. Try again, or email us at hello@engerman.com." |

---

## Navigation Microcopy

### Nav Labels (optimized for information scent)

| Label | Why This Label |
|-------|---------------|
| "How It Works" | Controller asks: "How does this connect to my data?" |
| "Sample Output" | CFO asks: "What will I actually get?" |
| "Pricing" | Everyone asks: "Is this in my budget?" |
| "Security" | Procurement asks: "Is this safe?" |
| "Customers" | CFO asks: "Who else uses this?" |
| "Book Evaluation" | High-intent, specific commitment level |

### Footer Labels

Security, AI Governance, Data Controls, Privacy Policy, Terms of Service, Request SOC 2

---

## Tooltip / Helper Text

| Element | Helper Text |
|---------|------------|
| **Checkpoint ID** | "Ties this memo to the exact source data, validation results, and analysis run. Can reproduce this memo at any time." |
| **COA template version** | "Ensures the account mapping used is recorded and auditable." |
| **Injection scan** | "Automated check for adversarial patterns in uploaded data." |
| **SLA timer** | "Time remaining for this step in the approval workflow." |
| **Burn multiple** | "Net burn divided by net new ARR. Below 1x is efficient." |

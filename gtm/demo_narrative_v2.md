# E-Solutions Demo Narrative v2

**Audience:** CFO, Founder, or Controller at a Seed–Series B SaaS/services company
**Goal:** Show the workflow, build trust, secure a design partner conversation

---

## Version A: Live call (5 minutes)

Use for scheduled demos, discovery follow-ups, and design partner conversations.

### Screen 1 — The finished memo (90 seconds)

**What to show:** Open the sample variance memo PDF (or v2 markdown). Start at the top.

**Talk track:**

> "Before I explain how it works, let me show you what you actually get."

Point to the metadata block:
> "Every memo starts with this. Checkpoint ID, validation status, source system, export date. This is how you know exactly where the numbers came from."

Scroll to executive summary:
> "Two sentences. What happened this month, what needs attention. Written for your board, not your accountant."

Point to the topline table:
> "Actuals, budget, variance, trend signal — all computed from your GL export and budget file."

Point to one revenue variance (subscription beat):
> "This $17.8K subscription beat. The system identified 3 enterprise upsells, computed the MRR impact, and flagged that churn was below plan. Your controller would normally piece this together manually across multiple tabs."

Point to one expense variance (legal spike):
> "This legal fee spike — $5.2K over budget. The narrative explains it is Series B-related and non-recurring. Your board reads this and does not need to ask the question."

Scroll to data provenance:
> "And at the bottom — the full audit trail. Source system, COA version, validation results, who reviewed it. Six months from now, you can pull up this checkpoint and reproduce the exact same analysis."

**What this accomplishes:** The prospect sees the deliverable before hearing the pitch. They evaluate quality, not promises.

### Screen 2 — The workflow (90 seconds)

**Talk track:**

> "Here is how this gets produced."

Walk through the 6 steps. Be specific about what is currently manual vs. assisted:

**Upload:**
> "Your controller uploads the GL export and budget file. Same CSV or Excel they already pull from QuickBooks or Xero. No new system to learn."

**Validate:**
> "We validate every row against your chart of accounts. Schema checks, period matching, balance verification. If a field is missing or an account code does not map, it gets flagged and sent back. No analysis runs on unvalidated data."

*Pause here.* This is where trust is built. Most prospects have never heard a vendor say "we reject bad data before processing."

**Analyze:**
> "Once validation passes, the system computes variances, identifies material items, and generates draft narrative explanations."

**Be honest about the current state:**
> "The variance computation is automated. The narrative generation uses AI — it drafts the explanations, and then a human reviewer verifies them. We are not claiming the AI is perfect. We are claiming the combination of AI speed and human review produces a better result faster than a spreadsheet."

**Review:**
> "Every memo goes through a finance QA reviewer. They check the numbers tie, the narratives make sense, and nothing was missed. This is mandatory — not optional."

**Approve and deliver:**
> "You see the memo in the portal, approve it or request changes, and the final PDF is delivered via secure download and encrypted email."

### Screen 3 — Differentiation (45 seconds)

> "Three things that matter here."

1. **Auditability:** "Every memo has a checkpoint ID. You can trace any number back to the source data, the validation, and the review log. Try doing that with last quarter's spreadsheet."

2. **Speed without blind trust:** "Under 48 hours from upload. But there is a human between the AI and your board. You get speed and accuracy, not a gamble."

3. **Built for your team size:** "Tools like Planful and Vena assume you have an FP&A team and 3 months for implementation. We are built for a 1–3 person finance team that needs results in two weeks."

### Screen 4 — The offer (45 seconds)

> "The design partner pilot is 90 days — three monthly cycles. $1,500 a month, which is half our standard rate. In exchange, you give us weekly feedback and permission to develop an anonymized case study."

> "We start with a test run: we produce a memo from your prior-month data or a sample so you can evaluate the quality before committing to real monthly delivery."

> "No setup fees, no auto-renewal. If it does not save time and improve quality after three cycles, you stop."

### Close

> "Does this match a problem your team actually has? If so, I would like to schedule 30 minutes to look at your current close-to-board process and see if there is a fit."

---

## Version B: Async recorded walkthrough (3 minutes)

Use for sending to prospects who prefer to review on their own time, or as a follow-up to initial outreach.

### Structure

1. **Open (15 sec):** "I am [name] from E-Solutions. We produce board-ready variance memos for startup finance teams. Let me show you what the output looks like."
2. **The memo (60 sec):** Screen-record scrolling through the sample memo. Narrate the executive summary, one variance section, and the data provenance block. Keep it visual — let the memo do the talking.
3. **The workflow (45 sec):** Brief narration of the 6 steps with emphasis on validation and human review. Use a simple slide or diagram showing: Upload → Validate → Analyze → Review → Approve → Deliver.
4. **The offer (30 sec):** "90-day design partner pilot, $1,500/month, no lock-in. We start with a test run on your prior-month data. If it meets your standard, we go live."
5. **CTA (15 sec):** "Reply to this message or book a call at [link] to discuss your setup."

### Recording tips
- Screen-share the memo, not a slide deck. Prospects want to see the deliverable.
- Keep your face visible in a corner (picture-in-picture) if possible — builds trust.
- Do not use transitions, animations, or music. Clean and professional.
- Total runtime: 2.5–3 minutes maximum. Finance leaders will not watch longer.

---

## Objection handling

### "We already have a process that works."
> "How long does it take? If your board asks where a number came from, can you trace it in 30 seconds? We are not replacing your team's judgment — we are replacing the manual assembly and making the result auditable."

### "Is it all AI? I don't trust AI with board numbers."
> "It is not all AI. AI handles variance computation and draft narratives. A human finance QA reviewer verifies every memo before delivery. You also review and approve before it reaches the board. Two layers of human oversight on every memo."

### "We use [Mosaic / Jirav / Cube / DataRails]."
> "Those tools are great for dashboards and planning. We focus on one specific output — the monthly variance memo. We do not replace your FP&A tool. We replace the manual hours your controller spends turning that data into a board-ready document."

### "$1,500/month for a pilot — we could just hire an intern."
> "An intern does not produce auditable memos with checkpoint IDs and validation gates. And your controller still spends hours reviewing their work. We deliver a board-quality memo in 48 hours with a full audit trail. The question is whether 10–15 hours of your finance team's time per month is worth $1,500."

### "Can you integrate directly with our accounting system?"
> "For the pilot, upload is manual — same export your controller already pulls. This keeps setup simple and means we go live in two weeks instead of months. Direct integrations are planned for post-pilot."

### "What about data security?"
> "Your data is isolated by design — separate namespace, no cross-client access. We run validation and injection scanning before any processing. We provide a Data Processing Agreement. Retention and deletion policies are defined upfront. You can request data deletion at any time."

### "This sounds early-stage. How do I know you'll be around?"
> "Honest answer: we are early. That is why the pilot is 90 days with no lock-in. You get a significant discount for helping us refine the service. Your risk is $1,500/month for three months. Your upside is a workflow that saves your team 60%+ of the time they spend on the memo today."

---

## Pre-demo checklist

- [ ] Sample memo PDF (or v2 markdown) open and ready to screen-share
- [ ] Know the prospect's accounting system (QBO, Xero, NetSuite)
- [ ] Know their approximate team size, stage, and whether they have a Controller
- [ ] Pilot package v2 ready to send as follow-up
- [ ] Calendar link ready for scheduling the deep-dive

## Post-demo actions

- [ ] Send sample memo and pilot package within 1 hour
- [ ] Log the conversation, objections, and interest level in WORKLOG.md
- [ ] If interested: propose the 30-minute deep-dive within 1 week
- [ ] If not interested: note the reason for future iteration
- [ ] After every 3 demos: review objection patterns and update this narrative

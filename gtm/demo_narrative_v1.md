# E-Solutions Demo Narrative

**Purpose:** 5-minute founder-led walkthrough for live prospect demos.
**Audience:** CFO, Founder, or Controller at a Seed–Series B SaaS/services company.
**Goal:** Show the workflow, build trust, and secure a design partner conversation.

---

## Short version (3 minutes)

Use this for cold intros, quick follow-ups, or when the prospect has limited time.

### Setup (30 seconds)

> "Let me show you what the output looks like, and then I'll walk you back through how we get there."

Open the sample variance memo. Let them see the finished product first — that is what they are buying.

**What to show:**
- The executive summary (concise, board-ready language)
- The topline performance table (actuals vs. budget vs. prior month)
- One revenue variance explanation and one expense variance explanation
- The data provenance section at the bottom (checkpoint ID, validation status, source system)

### The workflow (1 minute)

> "Here is how this gets produced. Your controller uploads the GL export and budget file — same files you already pull from QuickBooks or Xero. We validate the data against your chart of accounts before anything is analyzed. No analysis runs until the data passes validation and a security scan. Then the system computes variances, flags material items, and generates draft narratives. A human finance QA reviewer checks every memo before it reaches you. You review and approve in our portal, and the final PDF is delivered."

**What to emphasize:**
- Upload is the same files they already produce
- Validation happens before analysis (trust signal)
- Human review is mandatory, not optional
- They approve before delivery — they stay in control

### The close (1 minute)

> "Most of our target customers tell us the memo takes their controller 8 to 15 hours every month. We get it to you in under 48 hours from upload, with an audit trail your board can trust. The pilot is 90 days, no long-term commitment. We start by producing one memo from anonymized data so you can see the quality before you provide real numbers."

If they are interested: "Can we schedule 30 minutes to look at your current process and see if there is a fit?"

---

## Full version (5 minutes)

Use this for scheduled demos, design partner conversations, or follow-up meetings.

### 1. Open with the pain (45 seconds)

> "Every month, your finance team pulls a GL export, opens a spreadsheet, manually compares actuals to budget line by line, writes up explanations for every material variance, and formats a memo for the board. It takes 8 to 15 hours. It is tedious, error-prone, and hard to audit. If someone asks 'where did this number come from?' three months later, good luck finding the answer in a spreadsheet."

**Do not:** list features. **Do:** describe their current reality. Let them nod.

### 2. Show the output (1 minute)

Open `sample_variance_memo_v1.md` (or the PDF version).

Walk through:
- **Executive summary** — "This is what your board sees. Concise, plain language, no fluff."
- **Topline table** — "Actuals, budget, variance — computed automatically from your data."
- **Revenue analysis** — Point to one specific variance. "This $17.8K subscription beat? The system identified the 3 enterprise upsells and the churn number automatically. Your controller would normally assemble this by hand."
- **Expense variance** — Point to the legal fees spike. "This $5.2K legal overage is flagged as non-recurring and tied to the Series B process. The narrative explains it so the board doesn't have to ask."
- **Data provenance** — Scroll to the bottom. "Every memo has a checkpoint ID. This ties the output to the exact source data, the validation results, and the review log. You can reproduce this analysis six months from now."

### 3. Walk through the workflow (1.5 minutes)

> "Let me show you how we get from your raw data to this memo."

Walk through the 6 steps:

**Step 1 — Upload:**
> "Your controller uploads the GL export and budget file through our secure portal. Same CSV or Excel files they already pull from QuickBooks, Xero, or NetSuite."

**Step 2 — Validate:**
> "Before any analysis runs, we validate the data. Schema checks, chart of accounts mapping, and a security scan. If something does not match — a missing account code, an unexpected format — it gets flagged and sent back. No analysis happens on bad data."

*Trust is built here.* This is the moment the prospect realizes this is not a black-box AI tool.

**Step 3 — Analyze:**
> "Once validation passes, the system computes variances across every account category, identifies material items, and generates draft narrative explanations."

**Step 4 — Human review:**
> "Every draft memo goes through a human finance QA reviewer before it reaches you. They check the numbers, verify the narratives make sense, and flag anything that needs a second look. This is not optional — it happens on every memo."

*Trust is reinforced here.* Most prospects will ask "is it all AI?" — the answer is no.

**Step 5 — Approve:**
> "You review the memo in the portal. If something needs to change, you request a revision. When you are satisfied, you approve it. The approval is logged."

**Step 6 — Deliver:**
> "The final PDF is delivered via the portal and encrypted email. Archived with the full audit trail."

### 4. Differentiation (45 seconds)

> "Three things make this different from other tools you may have looked at."

1. **Auditability.** "Every memo has a checkpoint ID, validated inputs, and a review log. You can trace any number back to the source data. Try doing that with a spreadsheet or a dashboard tool."

2. **Speed without sacrificing trust.** "Under 48 hours from upload to delivery. But unlike a pure AI tool, there is a human reviewer between the draft and your board. You get speed and accuracy."

3. **Designed for lean teams.** "Planful and Vena take months to implement and assume you have an FP&A team to run them. We are built for a 1–3 person finance team that needs results now, not after a 12-week deployment."

### 5. The offer (30 seconds)

> "The pilot is 90 days — three monthly cycles. We start by producing a memo from anonymized or sample data so you can evaluate the quality risk-free. If it meets your standard, we go live with your real data. Your controller uploads, we deliver, you give us feedback every week so we can dial it in."

> "Design partners get a significant discount on our Starter tier. No setup fees, no long-term contract. If it does not save time and improve quality, you walk away."

### 6. Close

> "Does this match a problem your team actually has? If so, I would like to schedule 30 minutes to look at your current close-to-board process and see if there is a fit."

---

## Objection handling

**"We already have a process that works."**
> "How long does it take? And if your board asks where a number came from, how quickly can you trace it back to the source? We are not replacing your process — we are making it faster and auditable."

**"Is it all AI? I don't trust AI with board numbers."**
> "No. AI handles the computation and draft narratives. A human finance QA reviewer verifies every memo before delivery. You also review and approve before anything goes to the board. The AI makes it fast — the human review makes it trustworthy."

**"We use [Mosaic / Jirav / Cube / DataRails] for FP&A."**
> "Those are great for dashboards and planning. We are focused on one specific deliverable — the monthly variance memo. We do not replace your FP&A tool. We replace the 8–15 hours your controller spends manually producing the board memo from the data those tools give you."

**"$3K–$4K/month is a lot for a startup."**
> "Your controller spends 10–15 hours per month on this. At their fully loaded cost, that is $X. Plus the risk of errors, the audit exposure, and the fire drills when the board asks questions. Our fee is a fraction of the total cost of doing it manually — and you get auditability you cannot get from a spreadsheet."

**"Can you integrate directly with QuickBooks / Xero?"**
> "For the pilot, your controller uploads the export manually — same file they already pull. Direct integrations are on the roadmap and will be available as we scale. The manual upload keeps the pilot simple and means we can start in two weeks instead of months."

**"What happens to our data?"**
> "Your data is isolated by design — there is no cross-client access. Every file is validated and checkpointed. We operate under a Data Processing Agreement. Retention and deletion policies are defined upfront. You can request data deletion at any time."

---

## Demo checklist

Before the demo:
- [ ] Sample memo open and ready to screen-share
- [ ] Know the prospect's accounting system (QBO, Xero, NetSuite)
- [ ] Know their approximate team size and stage
- [ ] Have the pilot package ready to send as follow-up

After the demo:
- [ ] Send the sample memo and pilot package within 1 hour
- [ ] Log the conversation in the worklog
- [ ] Note any objections or questions for iteration
- [ ] If interested: schedule the 30-minute deep-dive within 1 week

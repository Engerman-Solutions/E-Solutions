# Design Partner Call Flow v1

**Purpose:** Structure for first-call conversations with ICP-fit prospects. Goal is to qualify, demonstrate, and advance to a design partner commitment.

---

## First-Call Objective

Leave the call with one of three outcomes:

1. **Advance:** Prospect wants to see a test run on their data → schedule data handoff
2. **Nurture:** Interested but not ready → send pilot package, follow up in 2–4 weeks
3. **Disqualify:** Not a fit → note the reason, move on

Do not try to close on the first call. The goal is to learn their situation, show the output, and determine fit.

---

## Call Structure (30 minutes)

| Phase | Duration | What Happens |
|-------|----------|--------------|
| Open | 2 min | Set context, confirm time, state objective |
| Discovery | 8 min | Understand their current process and pain |
| Demo | 10 min | Show the sample memo (use demo_narrative_v2 flow) |
| Qualify | 5 min | Assess fit, surface objections |
| Close | 5 min | Propose next step, confirm action items |

---

## Phase 1: Open (2 min)

> "Thanks for making time. I want to understand how your team handles the monthly variance memo today, show you what we have built, and see if there is a fit. Sound good?"

Keep it direct. No slides, no company history, no "let me tell you about our vision."

---

## Phase 2: Discovery (8 min)

### Primary Discovery Questions

Ask 3–4 of these based on what you already know:

1. **"Walk me through what happens between month-end close and the board getting financials."**
   - Listen for: time spent, who does the work, what tools they use, what goes wrong

2. **"How long does the variance analysis and memo take? Who does it?"**
   - Listen for: 8–15 hours is the sweet spot. If they say "a couple hours," probe harder — they may be underestimating or outsourcing.

3. **"What does the board actually receive? A deck? A memo? Just financials?"**
   - Listen for: whether they produce a narrative variance memo or just a P&L. If just a P&L, our value prop is stronger — we add the narrative layer.

4. **"If the board asks where a specific number came from, how quickly can your team trace it back?"**
   - Listen for: hesitation. This is the audit trail pain point.

5. **"What accounting system are you on?"**
   - Need this for implementation planning. QBO/Xero = easy. NetSuite = doable but more complex.

6. **"How big is the finance team?"**
   - 1–2 people is ideal. 3+ means they may have capacity. 0 means the founder does it — possible but different buyer motion.

### What You Are Listening For

| Signal | Interpretation |
|--------|---------------|
| "It takes my controller a full week" | Strong pain. High value. |
| "We just hired our first Controller" | Building from scratch. Open to tools. |
| "Our board wants monthly financials but we can only do quarterly" | Capacity constraint. We solve this. |
| "We use spreadsheets for everything" | No existing tool loyalty. Low switching cost. |
| "We already use Mosaic/Jirav" | Different problem — those are dashboards, not memo production. |
| "Our CFO handles it" | CFO time is expensive. Frame around time savings. |
| "It's not a big deal for us" | Likely not a fit. Do not force it. |

---

## Phase 3: Demo (10 min)

Follow `gtm/demo_narrative_v2.md` Version A structure:

1. **Show the finished memo first** (90 sec) — open `sample_variance_memo_v2.pdf`. Walk through metadata block, executive summary, one variance section, data provenance.
2. **Walk through the workflow** (90 sec) — Upload → Validate → Analyze → Review → Approve → Deliver. Emphasize validation gate and human review.
3. **Differentiation** (45 sec) — Auditability, speed without blind trust, built for lean teams.
4. **The offer** (45 sec) — 90-day pilot, $1,500/month, test run first.

### When to Show the Sample Memo

- **Best time:** After discovery, when you have heard their specific pain. You can then point to the parts of the memo that map to their situation.
- **Do not:** Show it before you understand their process. It loses impact without context.

### When to Send the Pilot Package

- **After the call:** If the prospect expressed interest, send `pilot_package_v2.pdf` within 1 hour as a follow-up.
- **Do not:** Send it before the call or during the call. It is a leave-behind, not a presentation.

---

## Phase 4: Qualify (5 min)

### Qualifying Questions

1. **"Does this map to a real problem your team has?"** — Binary. If no, gracefully close.
2. **"Who else would need to be involved in a decision to try this?"** — Understand decision process. Ideal: "Just me" or "Me and my Controller."
3. **"What would need to be true for you to run a test?"** — Surface hidden objections.
4. **"Is budget a constraint at $1,500/month for 90 days?"** — Better to know now.

### Common Objections and Responses

See `gtm/demo_narrative_v2.md` objection handling section for detailed responses. Quick reference:

| Objection | Response Direction |
|-----------|-------------------|
| "We have a process" | Probe on time and auditability. |
| "I don't trust AI" | Two layers of human review. You approve before the board sees it. |
| "We use [FP&A tool]" | We do not replace it. We replace the manual memo assembly step. |
| "$1,500 is expensive" | What does your Controller's time cost? 10–15 hours/month at $75/hr = $750–$1,125 in direct time, plus CFO review time. |
| "Seems early-stage" | It is. 90 days, no lock-in, discount for helping us refine. |
| "Need to integrate with our system" | Manual upload for now. Go live in 2 weeks instead of months. |

---

## Phase 5: Close (5 min)

### If Strong Interest

> "Here's what I'd suggest as next step: I send you the pilot package with the scope and pricing. You send me a prior-month GL export and budget file — anonymized if you prefer — and I produce a test memo on your data within a week. If the quality meets your standard, we kick off the 90-day pilot."

Confirm:
- Who will provide the data (Controller? CFO?)
- What accounting system (for data format expectations)
- Timeline for getting data (this week? next?)

### If Moderate Interest

> "Let me send you the pilot package and sample memo. Take a look, share it with your Controller, and let me know if you want to explore further. I will follow up in two weeks."

### If Not a Fit

> "Appreciate the time. It sounds like [reason] means this is not the right fit right now. If your reporting needs change, feel free to reach out."

Log the reason for disqualification in the target list.

---

## Post-Call Checklist

- [ ] Send pilot package PDF and sample memo PDF within 1 hour (if interested)
- [ ] Log conversation in target list: interest level, objections, next step, follow-up date
- [ ] Note any market feedback (pricing reaction, feature requests, competitive mentions)
- [ ] If advancing: confirm data handoff timeline and send prep instructions
- [ ] If nurturing: set calendar reminder for follow-up
- [ ] After every 3 calls: review patterns and update objection handling

# Next Actions

Priority-ordered. Top of the list = do first.

1. **Run the pre-pilot sprint (Week 1: infrastructure).** Build validation scripts (schema, period, balance, injection checks) and variance computation scripts. Create the COA mapping template. Set up a secure file upload mechanism. Draft the Data Processing Agreement. Target: all data pipeline components tested against sample data by end of week.

2. **Run the pre-pilot sprint (Week 2: AI + delivery + staffing).** Write and test AI narrative generation prompts (Claude API). Test PDF conversion pipeline against sample_variance_memo_v2.md. Contract a finance QA reviewer and brief them on the review checklist. Write customer communication templates. Set up SLA tracking. Target: can produce a complete memo PDF from sample data using the full workflow.

3. **Build the ICP shortlist.** Identify 10–20 specific Seed–Series B SaaS/services companies with lean finance teams. Prioritize companies in personal/professional network for warm outreach. For each: company name, stage, estimated size, likely finance contact, warm path. This is the gate to all outbound activity.

4. **Draft outreach messaging.** Write 2–3 email and LinkedIn templates. Lead with the pain ("How many hours does your team spend on the monthly variance memo?"). Offer the free board memo or a walkthrough of the sample as the call-to-action. Attach or link to the sample memo PDF.

5. **Start founder-led outreach.** Begin contacting the ICP shortlist. Use the demo narrative for live conversations. Send the pilot package as a follow-up within 1 hour of any interested response. Target: 5+ conversations in the first 2 weeks.

6. **Contract a finance QA reviewer.** Find a part-time contractor with FP&A or controllership experience. Provide the reviewer checklist from live_pilot_workflow_v1.md. Budget 2–4 hours per memo initially. Must be in place before the first design partner goes live.

7. **Finalize the Data Processing Agreement.** Start from a standard DPA template. Customize for E-Solutions data handling (namespace isolation, reviewer access controls, retention/deletion). Have legal counsel review. Must be signed before any customer provides real financial data.

8. **Convert the sample memo to PDF.** Test Pandoc, Typst, or Google Docs against sample_variance_memo_v2.md using format_notes_v1.md spec. Produce a polished sample PDF for use in demos and outreach.

9. **Define the onboarding flow.** Document what happens after a design partner says yes: data requirements checklist, COA mapping walkthrough, access setup, first-cycle timeline, weekly feedback cadence. Target: go-live within 2 weeks of signed agreement.

10. **Refine proof assets after first prospect conversations.** The v2 assets will improve with real feedback. Plan to iterate after the first 3 conversations.

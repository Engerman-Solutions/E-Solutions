# Next Actions

Priority-ordered. Top of the list = do first.

1. **Test PDF conversion pipeline.** Convert generated_memo_draft_v2.md to PDF using format_notes_v1.md spec. Test Pandoc with custom HTML/CSS template or Typst. Produce a polished sample PDF for demos and outreach. This is the last deliverable-quality gap before a memo can be shown to a prospect.

2. **Draft the actual DPA.** Requirements are documented in ops/dpa_requirements_and_open_questions_v1.md. Start from a standard DPA template, customize for E-Solutions, and have legal counsel review. Must be signed before any customer provides real financial data.

3. **Build the ICP shortlist.** Identify 10–20 specific Seed–Series B SaaS/services companies with lean finance teams. Prioritize companies in personal/professional network for warm outreach. For each: company name, stage, estimated size, likely finance contact, warm path.

4. **Draft outreach messaging.** Write 2–3 email and LinkedIn templates. Lead with the pain ("How many hours does your team spend on the monthly variance memo?"). Offer the free board memo or a walkthrough of the sample as the call-to-action. Attach or link to the sample memo PDF.

5. **Start founder-led outreach.** Begin contacting the ICP shortlist. Use the demo narrative for live conversations. Send the pilot package as a follow-up within 1 hour of any interested response. Target: 5+ conversations in the first 2 weeks.

6. **Write customer communication templates.** Email templates for: upload instructions, validation error notifications, memo ready for review, approval confirmation, delivery notification.

7. **Define the onboarding flow.** Document what happens after a design partner says yes: data requirements checklist, COA mapping walkthrough, access setup, first-cycle timeline, weekly feedback cadence. Target: go-live within 2 weeks of signed agreement.

8. **Run the full pipeline on a real customer dataset.** Once a design partner is signed and data is received, execute the pipeline via `make live-pipeline` or step-by-step as documented in ops/run_narrative_workflow_v1.md. Measure time per stage. Identify bottlenecks.

9. **Contract a dedicated QA reviewer.** Matt is provisional. Before scaling beyond 1 design partner, identify and onboard a part-time contractor with FP&A or controllership experience.

10. **Refine proof assets after first prospect conversations.** The v2 assets will improve with real feedback. Plan to iterate after the first 3 conversations.

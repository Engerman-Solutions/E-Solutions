# Task Queue

## Active tasks

| # | Task | Priority | Status | Owner | Business reason |
|---|------|----------|--------|-------|-----------------|
| 4 | Build ICP shortlist (10–20 target companies) | P0 | Not started | — | Outbound cannot start without specific companies and warm contact paths identified. |
| 5 | Draft outreach messaging (email + LinkedIn) | P0 | Not started | — | Founder-led outbound requires concise, pain-focused messaging. Include "free board memo" offer as top-of-funnel. |
| 6 | Build outreach target list with contacts | P1 | Not started | — | For each ICP company, identify CFO/Founder/Controller contact and warm paths. |
| 7 | Define onboarding flow for design partners | P1 | Not started | — | Document what happens after "yes": data requirements, COA mapping, access setup, first-cycle timeline. |
| 8 | Design review/audit workflow and reviewer SOP | P1 | Not started | — | Auditability is a core differentiator. Clean-room review process must be designed before the first pilot memo. |
| 17 | Pre-pilot sprint: build validation and computation scripts | P0 | Done | — | Must be operational before first design partner provides real data. See ops/pilot_gaps_and_build_priorities_v1.md Priority 1. |
| 18 | Pre-pilot sprint: AI narrative generation workflow | P0 | Done | — | Define prompts, model integration, and human editing workflow for variance explanations. |
| 19 | Contract finance QA reviewer | P0 | Not started | — | Human review is mandatory (DEC-008). No reviewer = no delivery. |
| 20 | Draft Data Processing Agreement | P0 | Requirements defined | — | Required before any customer provides real financial data. DPA requirements doc created; actual DPA draft requires legal counsel. |
| 21 | Test PDF conversion pipeline | P1 | Not started | — | Convert sample_variance_memo_v2.md to PDF using format_notes_v1.md spec. Verify quality. |
| 22 | Write customer communication templates | P1 | Not started | — | Upload instructions, validation errors, approval requests, delivery notifications. |
| 9 | Build MVP variance analysis pipeline | P1 | Core pipeline complete | — | Core technical workflow: intake → validation → COA mapping → AI analysis → report generation → checkpoint. End-to-end pipeline tested with sample data. |
| 10 | Design and build reviewer UI (clean-room) | P2 | Not started | — | Human QA reviewers need a UI with PII masking, approval controls, and audit logging before pilot delivery. |
| 11 | Research competitor positioning and gaps | P2 | Not started | — | Sharpen differentiation against Mosaic, Jirav, Cube, DataRails, Pilot, Vena. |
| 12 | Define pricing model and ROI calculator | P2 | Not started | — | Needed before converting design partners to paid. Frame around time savings and error reduction. |
| 13 | Build landing page (basic, no-code) | P2 | Not started | — | Provides a home for inbound interest from outreach and content. |
| 14 | Create "free board memo" lead magnet offer | P2 | Not started | — | Prospect uploads one month of data, E-Solutions delivers a sample memo at no cost. |
| 15 | Convert sample memo to PDF format | P2 | Superseded by #21 | — | Markdown is internal; prospects and boards expect a polished PDF deliverable. |
| 16 | Refine proof assets after first 3 prospect conversations | P2 | Not started | — | Feedback from real conversations will expose gaps in the memo, pilot package, or demo narrative. |

## Completed tasks

| # | Task | Completed | Notes |
|---|------|-----------|-------|
| 0 | Initialize repository and operating system | 2026-03-12 | TICKET-000: Founding setup |
| 0.1 | Ingest source materials and refine strategy docs | 2026-03-12 | TICKET-001: Strategy grounding from 8 source documents |
| 1 | Create sample variance memo from anonymized data | 2026-03-12 | TICKET-002: deliverables/sample_variance_memo_v1.md + data CSV |
| 2 | Define pilot package (1-page scope doc) | 2026-03-12 | TICKET-002: gtm/pilot_package_v1.md |
| 3 | Build demo narrative and walkthrough | 2026-03-12 | TICKET-002: gtm/demo_narrative_v1.md (short + full versions) |
| 3.1 | Polish proof assets and define pilot workflow | 2026-03-12 | TICKET-003: v2 memo, format notes, pilot package v2, demo narrative v2, live pilot workflow, gaps/build priorities |
| 3.2 | Pre-pilot sprint Week 1: infrastructure foundations | 2026-03-12 | TICKET-004: validation scripts, variance computation, COA mapping, secure intake plan, DPA requirements |
| 3.3 | AI narrative workflow and memo assembly | 2026-03-12 | TICKET-005: narrative spec, prompt templates, I/O schemas, assembly script, operator run instructions, Makefile, end-to-end pipeline test |

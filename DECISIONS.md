# Decision Log

## DEC-001: B2B only

**Decision:** E-Solutions is a B2B finance operations product and managed service. No consumer features, no B2C.

**Rationale:** B2B finance operations has defined buyer personas (CFO/Founder), clear budgets, and measurable ROI. The V4.1 spec explicitly scopes the product as "sold to businesses (CFO/Controller/FP&A), deployed under a Data Processing Agreement, and designed for data isolation, reproducibility, and SLAs." Consumer use cases would dilute focus and require fundamentally different go-to-market.

**Implications:** All product, sales, and marketing efforts target business buyers. Language in all docs uses enterprise terminology: "customer (company)" not "client," "finance team user" not "user," "finance QA reviewer" not "human reviewer."

---

## DEC-002: Initial wedge is the monthly variance memo workflow

**Decision:** The first product/service focuses exclusively on producing auditable monthly variance memos.

**Rationale:** Variance memos are high-frequency (monthly), high-friction (manual spreadsheet assembly), and high-visibility (board-facing). They are universal across the ICP — every company with a board must produce them. The workflow is narrow enough to build and prove in 6 weeks, but valuable enough to justify $3K–$4K/month. Competitors like Planful and Vena require months of implementation and tie users to Excel; BlackLine focuses on close automation for enterprises. No competitor offers a governed variance memo workflow designed for lean startup teams.

**Implications:** All product development, demo materials, and pilot scoping center on this single deliverable. Adjacent finance workflows (budgeting, forecasting, cash flow, multi-deliverable packages) are explicitly deferred until the wedge is proven and at least 1 paying customer exists.

---

## DEC-003: Target ICP is Seed–Series B SaaS/services with lean finance teams

**Decision:** Focus on early-stage companies — Seed to Series B, 20–250 employees, $1M–$30M ARR, SaaS and services verticals, with 1–3 person finance teams.

**Rationale:** These companies have acute pain (manual processes, limited headcount, board reporting obligations) and limited alternatives (enterprise tools are too heavy, spreadsheets are too fragile). They are accessible via founder networks and respond to hands-on, consultative sales. Competitors like Mosaic and Jirav target a similar segment (Series A to pre-IPO, 50–500 employees) but focus on dashboards and planning, not governed memo production.

**Implications:** Pricing must fit early-stage budgets ($3K–$4K/month Starter). Onboarding must be lightweight (target: go-live in 2 weeks). Product must work with common SMB accounting systems (QuickBooks Online, Xero, NetSuite). White-glove support is a feature, not a cost center, at this stage.

---

## DEC-004: Founder-led outbound is the default early sales motion

**Decision:** The founder drives direct outbound sales to CFOs and Controllers at ICP-fit companies. No hired sales team, no paid acquisition, no inbound marketing investment initially.

**Rationale:** At pre-revenue, the fastest path to design partners is personal outreach from the founder, who can credibly speak to the problem and adapt the pitch in real time. Competitors in the SMB/startup segment (Mosaic, Jirav, Cube) all use demo-driven acquisition; E-Solutions can differentiate with consultative, high-touch pre-sales that positions the offering as "AI-augmented finance consulting" rather than a generic SaaS pitch. Every conversation should generate market learning.

**Implications:** Founder time is the primary constraint on sales velocity. Outreach quality matters more than volume. A "free board memo for last month's data" can serve as a risk-free top-of-funnel offer.

---

## DEC-005: Repository is the system of record

**Decision:** This Git repository is the single source of truth for all decisions, tasks, next actions, and work history.

**Rationale:** Distributed notes, Slack threads, and ad hoc docs degrade over time. A single, versioned, structured repository ensures nothing is lost and everything is traceable.

**Implications:** All ticket completions must update the repo. See OPERATING_RULES.md for requirements.

---

## DEC-006: Decisions and next actions must be updated on every ticket

**Decision:** Every completed ticket must update DECISIONS.md, NEXT_ACTIONS.md, TASK_QUEUE.md, and WORKLOG.md.

**Rationale:** The operating system only works if it is maintained. Allowing tickets to skip updates creates drift between reality and records.

**Implications:** Ticket completion checklists are enforced. No ticket is considered done until records are current.

---

## DEC-007: Git discipline is mandatory from day one

**Decision:** All work is committed to Git with clear messages. No work exists outside version control.

**Rationale:** Version control provides auditability, rollback capability, and a clear history of decisions. Starting disciplined avoids organizational debt.

**Implications:** Every ticket ends with a commit. Untracked files require explicit justification.

---

## DEC-008: Human-in-loop review is required before any memo delivery

**Decision:** No variance memo is delivered to a customer without human QA review and explicit approval via the web portal.

**Rationale:** The V4.1 spec mandates "human-in-loop approval required before delivery" as a core workflow step. Finance data is sensitive and board-facing — AI-generated narratives must be verified for accuracy before reaching the CFO. This also builds trust with early customers who are evaluating a new service. The Pilot (bookkeeping) model demonstrates that AI + human review achieves high accuracy and customer satisfaction while the AI improves over time.

**Implications:** Reviewer capacity must be planned from the first design partner. The clean-room reviewer UI (with PII masking by default) must be operational before pilot onboarding. Approval is the system of record — Slack is notification-only, not an approval channel.

---

## DEC-009: Trust and auditability are non-negotiable differentiators

**Decision:** Every memo must have a full audit trail: validation checkpoint, data provenance, analysis checkpoint, review log, and approval record. Data isolation between customers is enforced by design, not policy.

**Rationale:** The V4.1 spec defines P0 acceptance criteria including: no analysis before validation + injection scan pass, no cross-client state access possible by design, exactly-once processing, PII masked by default in reviewer UI, and logs never leak PII or tokens. These are not future features — they are prerequisites for the first pilot. Competitors in the startup space (Mosaic, Jirav, Cube) do not emphasize auditability; enterprise tools (BlackLine) do but at enterprise pricing and complexity. E-Solutions occupies the gap: enterprise-grade controls at startup-friendly pricing.

**Implications:** Infrastructure must implement namespace isolation, injection scanning, and approval logging before any customer data is processed. The "B2B moat" is operational — validated intake contracts, COA template versioning, reproducible checkpoints, approval logs, and reviewer SOPs. A big platform cannot replicate this by flipping a switch.

---

## DEC-010: Broader product vision is explicitly deferred

**Decision:** Voice intake, conversational interfaces, multi-agent specialization, Moltbot client-facing DM, CRM auto-sync, auto-scaling triggers, and multi-deliverable workflows are all out of scope for MVP and Phase 1.

**Rationale:** The V4.1 spec clearly separates MVP scope (monthly variance memo, web portal upload, single model + fallback, Slack notifications, portal approval with SLA timers, email + portal delivery) from Phase 2+ features. Attempting to build the broader vision before proving the wedge is the most dangerous scope distraction.

**Implications:** Any request for features outside the MVP scope boundary is logged in TASK_QUEUE.md as a future item and not acted on until Phase 1 exit criteria are met.

---

## DEC-011: Early delivery uses AI + human hybrid model

**Decision:** The early delivery model is AI-assisted, human-verified. AI handles data validation, variance analysis, narrative generation, and report formatting. A human finance QA reviewer checks accuracy, edits narratives, and approves for delivery.

**Rationale:** This matches the model Pilot used to scale bookkeeping: AI for 80% of the work, humans for quality assurance. It allows shipping a working service before the AI is perfect, while maintaining the quality standard that finance buyers require. Over time, the human correction patterns inform AI improvements, reducing manual intervention.

**Implications:** Reviewer hiring/contracting must be planned before the first design partner goes live. The economics of the hybrid model (AI token costs + reviewer time vs. subscription revenue) are a key metric to track from the first cycle.

---

## DEC-012: Tiered pricing aligned to company growth

**Decision:** Pricing follows a Starter / Pro / Enterprise tier structure, starting at $3K–$4K/month for Starter.

**Rationale:** The GTM strategy and addendum both specify tiered pricing that lets Seed-stage companies start small and upgrade as needs grow. This mirrors competitors like Jirav (transparent pricing tiers) and Pilot (starting at a few hundred/month for bookkeeping, scaling up). ROI framing: "We save your controller 20+ hours per month and improve accuracy; at your scale, our $3K fee is a fraction of that."

**Implications:** Design partners receive a significant discount (e.g., half-price for the first 3 months). Published pricing should emphasize ROI, not cost. Enterprise tier is not actively sold until the Starter workflow is proven.

---

## DEC-013: Design partner pilot priced at $1,500/month

**Decision:** The 90-day design partner pilot is priced at $1,500/month — 50% discount from the Starter tier ($3K–$4K/month).

**Rationale:** $1,500/month is low enough to remove budget friction for Seed–Series B companies while still qualifying serious intent. The discount is justified by the design partner exchange: weekly feedback calls and permission to develop an anonymized case study. The price must be non-zero to filter for companies with real pain, and high enough that the engagement is taken seriously by both sides.

**Implications:** Pilot pricing is explicit in the pilot package. No negotiation below $1,500. No free pilots — the "free board memo" offer is a one-time sample, not an ongoing service. After 90 days, continuation is at standard Starter pricing.

---

## DEC-014: Pilot operations are manual-first with defined automation targets

**Decision:** The first pilot uses manual or semi-automated processes at every stage. Automation targets are defined per stage but are not prerequisites for pilot launch.

**Rationale:** Waiting to build full automation before onboarding the first design partner would delay market learning by months. Manual execution with documented processes allows the pilot to launch in 2 weeks while generating the real-world data needed to prioritize automation investments. The 48-hour SLA is achievable with manual processes for a single customer.

**Implications:** Founder/operator bandwidth is the binding constraint during the first pilot. No more than 1–2 design partners can be supported simultaneously with manual processes. Automation priorities are driven by actual time-per-stage measurements from live cycles, not theoretical estimates.

---

## DEC-015: Matt is the provisional finance QA reviewer for the pilot

**Decision:** Matt serves as the provisional finance QA reviewer during the pilot. All draft memos pass through Matt's review before delivery.

**Rationale:** Human-in-loop review is mandatory (DEC-008). Rather than delay the pilot for a formal hiring/contracting process, the founder (Matt) performs QA review initially. This is a pilot-stage arrangement — it validates the review workflow and generates firsthand insight into what the reviewer role requires, but it is not a sustainable long-term structure.

**Implications:** Matt's bandwidth is a constraint on delivery velocity. A dedicated reviewer should be contracted before scaling beyond the first design partner. The reviewer checklist and workflow are documented to enable smooth handoff when a dedicated reviewer is onboarded.

---

## DEC-016: AI narrative generation uses Claude Sonnet with structured prompts

**Decision:** The AI narrative generation step uses Claude Sonnet (claude-sonnet-4-6) at temperature 0.3 with structured system and user prompts. Output is JSON conforming to a defined schema. Human editing is expected on every draft.

**Rationale:** Sonnet provides the best balance of quality, speed, and cost for structured financial text. Low temperature ensures factual consistency. Structured JSON output enables deterministic assembly. The prompts enforce numeric faithfulness and prohibit hallucination. Fallback chain: retry → Opus → manual Claude chat → manual writing.

**Implications:** The narrative generation step is AI-assisted, not AI-autonomous. The operator reviews AI output for quality before assembly, and Matt reviews the assembled memo before delivery. Two layers of human oversight on every memo.

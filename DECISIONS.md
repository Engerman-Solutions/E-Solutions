# Decision Log

## DEC-001: B2B only

**Decision:** E-Solutions serves business customers only. No B2C, no consumer finance tools.

**Rationale:** B2B finance operations has clear buyer personas, defined budgets, and measurable ROI. B2C would dilute focus and require fundamentally different go-to-market.

**Implications:** All product, marketing, and sales efforts target business buyers. Consumer use cases are out of scope.

---

## DEC-002: Initial wedge is the monthly variance memo workflow

**Decision:** The first product/service focuses exclusively on monthly variance memo production.

**Rationale:** Variance memos are high-frequency (monthly), high-friction (manual assembly), and high-visibility (board-facing). They represent a narrow, well-defined workflow that can demonstrate clear time savings.

**Implications:** All product development, demo materials, and pilot scoping center on this workflow. Adjacent finance workflows (forecasting, budgeting, reconciliation) are deferred until the wedge is proven.

---

## DEC-003: Target ICP is Seed to Series B SaaS/services with lean finance teams

**Decision:** Focus on early-stage companies (Seed to Series B) in SaaS and services verticals with 1–3 person finance teams.

**Rationale:** These companies have the pain (manual processes, limited headcount) and the urgency (board reporting obligations) but lack the resources to build internal tooling. They are accessible via founder networks and respond to hands-on, high-touch service.

**Implications:** Pricing must fit early-stage budgets. Onboarding must be lightweight. The product must work with common SMB accounting systems (QuickBooks, Xero, NetSuite).

---

## DEC-004: Founder-led outbound is the default early sales motion

**Decision:** The founding team drives outbound sales directly — no hired sales team, no paid acquisition, no inbound marketing investment at this stage.

**Rationale:** At pre-revenue, the fastest path to design partners is direct outreach from founders who can credibly speak to the problem and adapt the pitch in real time. Paid channels are premature before product-market fit.

**Implications:** Founder time is the primary constraint on sales velocity. Outreach quality matters more than volume. Every conversation should generate learning.

---

## DEC-005: Repository is the system of record

**Decision:** This Git repository is the single source of truth for all decisions, tasks, actions, and work history.

**Rationale:** Distributed notes, Slack threads, and ad hoc docs degrade over time. A single, versioned, structured repository ensures nothing is lost and everything is traceable.

**Implications:** All ticket completions must update the repo. See OPERATING_RULES.md for specific requirements.

---

## DEC-006: Decisions and next actions must be updated on every ticket

**Decision:** Every completed ticket must update DECISIONS.md, NEXT_ACTIONS.md, TASK_QUEUE.md, and WORKLOG.md.

**Rationale:** The operating system only works if it is maintained. Allowing tickets to skip updates creates drift between reality and records.

**Implications:** Ticket completion checklists are enforced. No ticket is considered done until records are current.

---

## DEC-007: Git discipline is mandatory from day one

**Decision:** All work is committed to Git with clear messages. No work exists outside version control.

**Rationale:** Version control provides auditability, rollback capability, and a clear history of what was done and when. Starting disciplined avoids technical and organizational debt.

**Implications:** Every ticket ends with a commit. Untracked files are not acceptable without explicit justification.

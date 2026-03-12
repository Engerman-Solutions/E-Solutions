# Operating Rules

This repository is the system of record for E-Solutions. These rules govern how work is tracked, completed, and committed.

## Ticket completion requirements

Every ticket must end with the following actions completed:

1. **TASK_QUEUE.md updated** — tasks added, reprioritized, or marked complete as appropriate
2. **DECISIONS.md updated** — any decisions made during the ticket are logged with rationale and implications
3. **NEXT_ACTIONS.md updated** — next actions revised to reflect current priorities
4. **WORKLOG.md updated** — entry added describing what was done, when, and any relevant outcomes
5. **git status checked** — no untracked files left behind unless explicitly justified
6. **Intended changes committed** — all relevant changes staged and committed with a clear message
7. **Changes pushed if remote exists** — if a remote is configured, push after committing

A ticket is **not complete** until all seven steps are done.

## Repository discipline

- **No scattered undocumented files.** Every file in this repo must have a clear purpose. If you create a file, it belongs in the correct directory and should be referenced in the relevant tracking document.
- **No silent scope expansion.** If a ticket leads to work beyond its stated scope, log the new work in TASK_QUEUE.md and NEXT_ACTIONS.md. Do not quietly expand what a ticket covers.
- **No ticket is complete until records and Git are updated.** This is non-negotiable. Incomplete record-keeping degrades the value of the entire system.
- **Repo is the system of record.** If it is not committed here, it did not happen. Conversations, Slack messages, and external docs are supplementary — not authoritative.

## Work priorities

All work should prioritize, in order:

1. Revenue — actions that move toward paid customers
2. Trust — actions that build credibility with prospects and partners
3. Reliability — actions that make delivery consistent and repeatable
4. Speed — actions that reduce cycle time for sales and delivery

Features, tooling, and infrastructure are means to these ends, not ends in themselves.

## Decision-making

- Decisions are logged in DECISIONS.md with rationale and implications.
- Reversible decisions should be made quickly. Irreversible decisions deserve deliberation.
- When in doubt, choose the option that gets closer to a paying customer.

## File organization

| Directory | Purpose |
|---|---|
| `docs/` | Internal documentation, guides, and reference material |
| `research/` | Market research, competitor analysis, customer discovery notes |
| `product/` | Product specs, workflows, templates, and design docs |
| `gtm/` | Go-to-market materials: outreach, messaging, sales collateral |
| `ops/` | Operational processes, onboarding flows, delivery playbooks |
| `deliverables/` | Sample and actual deliverables produced for customers |
| `prompts/` | AI prompts and templates used in workflows |

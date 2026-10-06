# Engerman Solutions — Website Remaster (branch `site-remaster-2026-10-05`)

**Built October 5, 2026 · decisions recorded October 6 · for Matthew Engerman's final read · Decisions, with precision.**

This branch replaces the live site's AI-first framing with what the sales desk actually says: a tech-enabled financial service — your finance department, delivered. One brand, two doors (founders / nonprofits), each lane carrying its own pricing, proof and try-first offer. Merging the pull request publishes it (Vercel deploys `main`). Until then, the Vercel preview URL on the PR is the review copy.

## What is on this branch

| File | What it is |
|---|---|
| `index.html` | Homepage: who we are in our own words, two doors, three layers, Sessions and the Brief, one call to action. |
| `pages/nonprofits.html` | The nonprofit lane in full: who it is for, three things to start, four steps, three layers routed by role, the three cadences priced by the packet, Academy, what we do not ask for, three tax statuses, try-it-first. Written from Service Offer rev v1.2. |
| `pages/founders.html` | The founders' lane: two files, within 48 hours, on us; what you receive each month; **four tiers with what comes with each** (Pilot $1,500 · Starter $3–4K · Pro $6–8K · Enterprise $12–15K+) and a tier-by-tier table, carried over from the live pricing page; the Founding Client Council — terms by application, never printed. |
| `pages/how-we-work.html` | Replaces How It Works and Security with one page: the clock, the checks, how we handle your data, what we are not. |
| `pages/sessions.html` | Board-Ready Sessions (Episodes 1–4 and the next) and The Board-Ready Brief, with the sample Board Brief download. |
| `pages/about.html` | Matthew's bio, the founding client, a generic team block (no names), the company. |
| `pages/privacy.html` · `pages/terms.html` | Real pages behind the footer links that were dead. Website policy and terms — not the Service Terms clients sign. |
| `forms/try-it-first.html` | Top-of-funnel form for both lanes. Short; adapts to the lane chosen; no file uploads. |
| `forms/setup-questionnaire.html` | The 10-question nonprofit onboarding questionnaire with tax-status logic. `noindex`; sent as a private link after signing, not linked from navigation. |
| `pages/pricing.html` · `pages/security.html` · `pages/how-it-works.html` | Redirect stubs so old links keep resolving (pricing → founders#fo-pricing, security → how-we-work#data, how-it-works → how-we-work). |
| `css/remaster.css` · `css/site.css` · `css/design-tokens.css` | Live design system plus the remaster additions. |
| `js/site-config.js` | Links and form endpoints. Matthew's LinkedIn and the Brief subscribe link are filled in; the two form endpoints are still blank (below). |
| `img/engerman-logo.svg` · `img/engerman-logo-inverted.svg` | Nav and footer marks. |
| `downloads/` | **The sample Board Brief PDF must be uploaded here through the GitHub web UI** (the API push is text-only). File name the pages link to: `Engerman_Solutions_Sample_Board_Brief_Nonprofit.pdf`. |

## Two house rules, applied everywhere

1. The nonprofit service is sold **by the packet, on three cadences** — the per-packet fee is the headline on every card; the cadence is how often it lands. Quarterly $1,650 a packet (4 a year); Board Cycle $1,500 a packet (6 a year) — recommended; Monthly $1,250 a packet (12 a year). Annual and prepaid totals and the $750 setup are stated under each card.
2. Every turnaround reads **within** 72 hours / **within** 48 hours. The commitment is the ceiling, not the target.

## Words

Fintech, software, platform, real-time, enterprise-grade, patented and AI-powered do not appear. "AI" appears once, on How We Work, in a sentence that says a person owns every packet. "SOC 2" is gone. The footer entity is corrected to E-Solutions Consulting, LLC, doing business as Engerman Solutions. The Founding Client rate is never printed. Jamie is named nowhere, by design. Team members are not named, by Matthew's decision of October 6.

## Decided October 6

- **Team block on About:** names cut; generic. The LinkedIn company page carries the team.
- **Founders' tiers:** all four carried over from the live site with what comes with each, plus the tier-by-tier table.
- **Matthew's bio:** three paragraphs on About — what the firm is, where it started, where it is going. Matthew to read once.
- **Jason's okay:** already given for LinkedIn; a courtesy note listing the four placements is drafted in Gmail for Matthew to send.
- **`LINKEDIN_MATTHEW_URL` and `BRIEF_SUBSCRIBE_URL`:** filled.

## Still open

1. **Academy inclusion** on `pages/nonprofits.html` — who gets Board-Ready Academy at no charge. The page currently says: included with Monthly, and with Board Cycle when the year is prepaid; $2,000 a year otherwise. The alternative is Service Offer rev v1.2 as written: included with Monthly only; $2,000 for everyone else. One-line edit either way; the Service Offer/Terms go to v1.3 to match.
2. **Form endpoints** (`FORM_ENDPOINT_TRY`, `FORM_ENDPOINT_SETUP`) — a Formspree form address for each. Until filled, each form opens the visitor's email app with the answers already written, addressed to info@. It works on day one.
3. **Sample Board Brief PDF** — upload to `website/downloads/` via the GitHub web UI.
4. **Preview check** — both forms submitted once; phone and laptop.

## Before merge

- [ ] Academy line confirmed or flipped
- [ ] Jason's reply to the courtesy note
- [ ] Formspree addresses pasted into `js/site-config.js` (or leave blank and ship with the email fallback)
- [ ] Sample Board Brief PDF uploaded to `website/downloads/`
- [ ] Preview checked on a phone and a laptop; both forms submitted once
- [ ] Merge → live. Only then share the nonprofit page with Jamie, after Thursday's green light.

**Jason's QR code (optional):** point it at `https://www.engermansolutions.com/?utm_source=jason&utm_medium=flyer&utm_campaign=california` so leads from his room are attributable.

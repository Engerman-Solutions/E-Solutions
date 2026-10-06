# Engerman Solutions — Website Remaster (branch `site-remaster-2026-10-05`)

**Built October 5, 2026 · decisions recorded October 6 · for Matthew Engerman's final read · Decisions, with precision.**

This branch replaces the live site's AI-first framing with what the sales desk actually says: a tech-enabled financial service — your finance department, delivered. One brand, two doors (founders / nonprofits), each lane carrying its own pricing, proof and try-first form. Merging the pull request publishes it (Vercel deploys `main`). Until then, the Vercel preview URL on the PR is the review copy.

## What is on this branch

| File | What it is |
|---|---|
| `index.html` | Homepage: who we are in our own words, two doors, three layers, Sessions and the Brief, one call to action. |
| `pages/nonprofits.html` | The nonprofit lane in full: who it is for, three things to start, four steps, three layers routed by role, the three cadences priced by the packet, Academy as a paid add-on, what we do not ask for, three tax statuses. Every "Try it first" button opens the nonprofit form. |
| `pages/founders.html` | The founders' lane: two files, within 48 hours, on us; what you receive each month; four tiers with what comes with each (Pilot $1,500 · Starter $3–4K · Pro $6–8K · Enterprise $12–15K+) and a tier-by-tier table; the Founding Client Council — terms by application, never printed. Every "Try it first" button opens the founders form. |
| `pages/how-we-work.html` | Replaces How It Works and Security with one page: the clock, the checks, how we handle your data, what we are not. |
| `pages/sessions.html` | Board-Ready Sessions (Episodes 1–4 and the next) and The Board-Ready Brief, with the sample Board Brief download. |
| `pages/about.html` | The founder's story as the business's story (2018 by hand → 2021 the company → 2026 the standard offer → two lanes), the founding client, a generic team block (no names), the company. No employer named. |
| `pages/privacy.html` · `pages/terms.html` | Real pages behind the footer links that were dead. Website policy and terms — not the Service Terms clients sign. |
| `forms/try-it-first.html` | **Two doors, one Microsoft Form each**, embedded inside the house chrome. `#founders` and `#nonprofits` preselect the door, so each lane page lands on its own form. Responses arrive in Microsoft 365 and by email notification. |
| `forms/setup-questionnaire.html` | The 10-question nonprofit onboarding questionnaire with tax-status logic. `noindex`; sent as a private link after signing. With no endpoint it opens the client's email app with the answers already written; or rebuild it as a third Microsoft Form and link to that instead. |
| `pages/pricing.html` · `pages/security.html` · `pages/how-it-works.html` | Redirect stubs so old links keep resolving. |
| `css/remaster.css` · `css/site.css` · `css/design-tokens.css` | Live design system plus the remaster additions. |
| `js/site-config.js` | Links: Matthew's LinkedIn, the Brief subscribe link, both Microsoft Forms. |
| `img/engerman-logo.svg` · `img/engerman-logo-inverted.svg` | Nav and footer marks. |
| `downloads/` | **The sample Board Brief PDF must be uploaded here through the GitHub web UI** (the API push is text-only). File name the pages link to: `Engerman_Solutions_Sample_Board_Brief_Nonprofit.pdf`. |

## The two Microsoft Forms (built October 6, 2026, in Matthew's account)

| | Founders & Operating Companies | Nonprofits & Associations |
|---|---|---|
| Title | Try it first — Founders & Operating Companies | Try it first — Nonprofits & Associations |
| Questions | 12: name, role, work email, company, website (optional), who you answer to, accounting system, entities, most recently closed month, what they ask for (optional, long), how you found us, acknowledgment | 15: name, role, work email, organization, website (optional), tax status, annual budget, board cadence, fiscal year end, events with venue contracts, accounting system, who closes the books, what the board asks for (optional, long), how you found us, acknowledgment |
| Theme | Brand navy #192746 | Brand navy #192746 |
| Settings | Anyone can respond · email notification on each response · "Submit another response" hidden · custom thank-you | Same |
| Link | `https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=TCp6pTf0lUWjidw_pJ41r8VK0JU18xlOmM5bOtgsLdhUNjA3SExCVVRJTE80NVNJM0JWTEhZV1pQSC4u` | `https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=TCp6pTf0lUWjidw_pJ41r8VK0JU18xlOmM5bOtgsLdhUNkxOU0RLQUJGMFpTWk1WRzNPWEdROVNPTC4u` |

The old "Free Beta Intake" form is untouched and no longer linked from the site.

## Two house rules, applied everywhere

1. The nonprofit service is sold **by the packet, on three cadences** — the per-packet fee is the headline on every card; the cadence is how often it lands. Quarterly $1,650 a packet (4 a year); Board Cycle $1,500 a packet (6 a year) — recommended; Monthly $1,250 a packet (12 a year). Annual and prepaid totals and the $750 setup are stated under each card.
2. Every turnaround reads **within** 72 hours / **within** 48 hours. The commitment is the ceiling, not the target.

## Decided October 6

- **Board-Ready Academy** is a paid add-on on every cadence: $2,000 a year, billed up front, nonprofit and association clients only, never included in the packet price. The Service Offer and Terms go to rev v1.3 to say the same thing.
- **Team block on About:** names cut; generic. The LinkedIn company page carries the team.
- **Founders' tiers:** all four carried over from the live site with what comes with each, plus the tier-by-tier table.
- **Matthew's bio:** the business's story; no employer named.
- **Jason:** okay already given for LinkedIn; a courtesy note listing the four placements is drafted in Gmail.
- **Forms:** two Microsoft Forms, one per lane, built and embedded. No Formspree.

## Still open

1. **Sample Board Brief PDF** — upload to `website/downloads/` via the GitHub web UI.
2. **Preview check** — each form submitted once from the Vercel preview; phone and laptop.
3. **Service Offer / Terms rev v1.3** — "within" wording and the Academy as a paid add-on on every cadence, before Thursday.

## Before merge

- [ ] Jason's reply to the courtesy note
- [ ] Sample Board Brief PDF uploaded to `website/downloads/`
- [ ] Preview checked on a phone and a laptop; each form submitted once
- [ ] Merge → live. Only then share the nonprofit page with Jamie, after Thursday's green light.

**Jason's QR code (optional):** point it at `https://www.engermansolutions.com/?utm_source=jason&utm_medium=flyer&utm_campaign=california` so leads from his room are attributable.

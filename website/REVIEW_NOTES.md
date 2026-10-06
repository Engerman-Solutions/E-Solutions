# Engerman Solutions — Website Remaster (branch `site-remaster-2026-10-05`)

**Built October 5, 2026 · for Matthew Engerman's final read · Decisions, with precision.**

This branch replaces the live site's AI-first framing with what the sales desk actually says: a tech-enabled financial service — your finance department, delivered. One brand, two doors (founders / nonprofits), each lane carrying its own pricing, proof and try-first offer. Merging the pull request publishes it (Vercel deploys `main`). Until then, the Vercel preview URL on the PR is the review copy.

## What is on this branch

| File | What it is |
|---|---|
| `index.html` | Homepage: who we are in our own words, two doors, three layers, Sessions and the Brief, one call to action. |
| `pages/nonprofits.html` | The nonprofit lane in full: who it is for, three things to start, four steps, three layers routed by role, the three cadences priced by the packet, Academy, what we do not ask for, three tax statuses, try-it-first. Written from Service Offer rev v1.2. |
| `pages/founders.html` | The founders' lane: two files, within 48 hours, on us; what you receive each month; the list card the live site already carried (Pilot / Starter / Pro / multi-entity); the Founding Client Council — terms by application, never printed. |
| `pages/how-we-work.html` | Replaces How It Works and Security with one page: the clock, the checks, how we handle your data, what we are not. |
| `pages/sessions.html` | Board-Ready Sessions (Episodes 1–4 and the next) and The Board-Ready Brief, with the sample Board Brief download. |
| `pages/about.html` | Matthew, the founding client, the Ledger Circle, the company. |
| `pages/privacy.html` · `pages/terms.html` | Real pages behind the footer links that were dead. Website policy and terms — not the Service Terms clients sign. |
| `forms/try-it-first.html` | Top-of-funnel form for both lanes. Short; adapts to the lane chosen; no file uploads. |
| `forms/setup-questionnaire.html` | The 10-question nonprofit onboarding questionnaire with tax-status logic. `noindex`; sent as a private link after signing, not linked from navigation. |
| `pages/pricing.html` · `pages/security.html` · `pages/how-it-works.html` | Redirect stubs so old links keep resolving (pricing → founders#fo-pricing, security → how-we-work#data, how-it-works → how-we-work). |
| `css/remaster.css` · `css/site.css` · `css/design-tokens.css` | Live design system plus the remaster additions. |
| `js/site-config.js` | The one file to fill in (below). `js/main.js` reads it. |
| `img/engerman-logo.svg` · `img/engerman-logo-inverted.svg` | Nav and footer marks. |
| `downloads/` | **The sample Board Brief PDF must be uploaded here through the GitHub web UI** (the API push is text-only). File name the pages link to: `Engerman_Solutions_Sample_Board_Brief_Nonprofit.pdf`. |

## Two house rules, applied everywhere

1. The nonprofit service is sold **by the packet, on three cadences** — the per-packet fee is the headline on every card; the cadence is how often it lands. Quarterly $1,650 a packet (4 a year); Board Cycle $1,500 a packet (6 a year) — recommended; Monthly $1,250 a packet (12 a year). Annual and prepaid totals and the $750 setup are stated under each card.
2. Every turnaround reads **within** 72 hours / **within** 48 hours. The commitment is the ceiling, not the target.

## Words

Fintech, software, platform, real-time, enterprise-grade, patented and AI-powered do not appear. "AI" appears once, on How We Work, in a sentence that says a person owns every packet. "SOC 2" is gone. The footer entity is corrected to E-Solutions Consulting, LLC, doing business as Engerman Solutions. The Founding Client rate is never printed. Jamie is named nowhere, by design.

## Decisions still yours (each is a one-line edit on this branch)

1. **Academy inclusion.** Board Cycle card and Academy section on `pages/nonprofits.html` say "included with annual prepayment of the Board Cycle." Keep, or revert to rev v1.2 ($2,000 on Quarterly and Board Cycle regardless; included on Monthly). Either way the Service Offer/Terms go to v1.3 to match.
2. **Jason on the site.** Named on the homepage, Sessions, About and How We Work (two quotes, every word his). **Needs his written okay before merge.**
3. **The Ledger Circle on About.** Davone, Christine and Victoria by name, title and region. Keep or cut.
4. **The founders' list card.** Carried over from the live site. Confirm or send current numbers.
5. **Matthew's bio.** Three sentences on About. Add or leave.

## Fill in once: `js/site-config.js`

- `LINKEDIN_COMPANY_URL`, `LINKEDIN_MATTHEW_URL`, `BRIEF_SUBSCRIBE_URL` — Sessions "Watch" button, Matthew's profile link on About, both "Subscribe" buttons. Blank falls back to an email to info@ — no dead links.
- `FORM_ENDPOINT_TRY`, `FORM_ENDPOINT_SETUP` — where the two forms POST (Formspree: create two forms, paste each `https://formspree.io/f/xxxx`). Blank means the form opens the visitor's email app with the answers already written — works on day one.
- `CALENDAR_URL` — optional; unused today.

Files never travel through a form. The client's ledger, budget and contracts go to the secure workspace folder — which is what the Terms promise.

## Before merge

- [ ] Academy line confirmed or flipped
- [ ] Jason's written okay for his name and two quotes
- [ ] Ledger Circle block on About: keep or cut
- [ ] `js/site-config.js` filled
- [ ] Formspree endpoints pasted; both forms submitted once on the Vercel preview
- [ ] Sample Board Brief PDF uploaded to `website/downloads/` via the GitHub web UI
- [ ] Preview checked on a phone and a laptop; every button clicked
- [ ] Merge → live. Only then share the nonprofit page with Jamie, after Thursday's green light.

**Jason's QR code (optional, Tuesday):** point it at `https://www.engermansolutions.com/?utm_source=jason&utm_medium=flyer&utm_campaign=california` so leads from his room are attributable.

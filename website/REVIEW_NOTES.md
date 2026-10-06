# Engerman Solutions — Website Remaster (branch `site-remaster-2026-10-05`)

**Built October 5, 2026 · decisions recorded October 6 · for Matthew Engerman's final read · Decisions, with precision.**

This branch replaces the live site's AI-first framing with what the sales desk actually says: a tech-enabled financial service — your finance department, delivered. One brand, two doors (founders / nonprofits), each lane carrying its own pricing, proof and try-first offer. Merging the pull request publishes it (Vercel deploys `main`). Until then, the Vercel preview URL on the PR is the review copy.

## What is on this branch

| File | What it is |
|---|---|
| `index.html` | Homepage: who we are in our own words, two doors, three layers, Sessions and the Brief, one call to action. |
| `pages/nonprofits.html` | The nonprofit lane in full: who it is for, three things to start, four steps, three layers routed by role, the three cadences priced by the packet, Academy as a paid add-on, what we do not ask for, three tax statuses, try-it-first. |
| `pages/founders.html` | The founders' lane: two files, within 48 hours, on us; what you receive each month; four tiers with what comes with each (Pilot $1,500 · Starter $3–4K · Pro $6–8K · Enterprise $12–15K+) and a tier-by-tier table; the Founding Client Council — terms by application, never printed. |
| `pages/how-we-work.html` | Replaces How It Works and Security with one page: the clock, the checks, how we handle your data, what we are not. |
| `pages/sessions.html` | Board-Ready Sessions (Episodes 1–4 and the next) and The Board-Ready Brief, with the sample Board Brief download. |
| `pages/about.html` | Matthew's bio in his own words (from his LinkedIn About, extended to both lanes and startups), the founding client, a generic team block (no names), the company. |
| `pages/privacy.html` · `pages/terms.html` | Real pages behind the footer links that were dead. Website policy and terms — not the Service Terms clients sign. |
| `forms/try-it-first.html` | The "Try it first" page, with **Matthew's Microsoft Form embedded** inside the house chrome. Responses land in Microsoft 365 as they do today. No new accounts, no Formspree. |
| `forms/setup-questionnaire.html` | The 10-question nonprofit onboarding questionnaire with tax-status logic. `noindex`; sent as a private link after signing. With no endpoint it opens the client's email app with the answers already written; or rebuild it as a second Microsoft Form and link to that instead. |
| `pages/pricing.html` · `pages/security.html` · `pages/how-it-works.html` | Redirect stubs so old links keep resolving. |
| `css/remaster.css` · `css/site.css` · `css/design-tokens.css` | Live design system plus the remaster additions. |
| `js/site-config.js` | Links. Matthew's LinkedIn, the Brief subscribe link and the Microsoft Form link are filled in. |
| `img/engerman-logo.svg` · `img/engerman-logo-inverted.svg` | Nav and footer marks. |
| `downloads/` | **The sample Board Brief PDF must be uploaded here through the GitHub web UI** (the API push is text-only). File name the pages link to: `Engerman_Solutions_Sample_Board_Brief_Nonprofit.pdf`. |

## Two house rules, applied everywhere

1. The nonprofit service is sold **by the packet, on three cadences** — the per-packet fee is the headline on every card; the cadence is how often it lands. Quarterly $1,650 a packet (4 a year); Board Cycle $1,500 a packet (6 a year) — recommended; Monthly $1,250 a packet (12 a year). Annual and prepaid totals and the $750 setup are stated under each card.
2. Every turnaround reads **within** 72 hours / **within** 48 hours. The commitment is the ceiling, not the target.

## Decided October 6

- **Board-Ready Academy** is a paid add-on on every cadence: $2,000 a year, billed up front, nonprofit and association clients only, never included in the packet price. The Service Offer and Terms go to rev v1.3 to say the same thing (rev v1.2 had it included on Monthly).
- **Team block on About:** names cut; generic. The LinkedIn company page carries the team.
- **Founders' tiers:** all four carried over from the live site with what comes with each, plus the tier-by-tier table.
- **Matthew's bio:** from his LinkedIn About, in his words, extended to the for-profit lane, startups and the nonprofit lane. Amgen is named because his public profile names it — his call whether it belongs on the company site.
- **Jason:** okay already given for LinkedIn; a courtesy note listing the four placements is drafted in Gmail.
- **Forms:** Microsoft Forms is the backend. The existing form is embedded on `forms/try-it-first.html`; Formspree is not needed.

## The Microsoft Form — what to change inside it

The embedded form is today's "Free Beta Intake" (CFO-oriented, Series B wording, closed-month choices from May 2026). Edit it in Microsoft Forms so it matches the site. Suggested title, intro and questions, with branching on question 6:

**Title:** Try it first — Engerman Solutions
**Intro:** Founders: two files, within 48 hours, on us. Nonprofits and associations: a quarter your board has already seen, rebuilt as a three-page Board Brief, at no fee. About three minutes. No files are uploaded here — Matthew replies within one business day with the secure folder for your files.

1. Your name (text, required)
2. Your role (text, required)
3. Work email (text, required)
4. Organization (text, required)
5. Website (text, optional)
6. Which describes you? (choice, required) — Founder or operating company · Nonprofit or association. *Branching:* first answer → questions 7–8, then 14; second answer → questions 9–13, then 14.
7. Who do you answer to? — A bank or lender · Investors · A board · More than one of these · Just myself, for now
8. Entities — One · Two or three · Four or more
9. Tax status — 501(c)(3) · 501(c)(6) · 501(c)(4) · Other or not sure
10. Annual budget, roughly — Under $1 million · $1–2 million · $2–5 million · Over $5 million
11. How often does the board meet? — Monthly · Every two months · Quarterly · Other
12. Fiscal year end — December · June · September · March · Other
13. Do you run events with signed venue contracts (conference, annual meeting)? — Yes, one · Yes, more than one · No
14. Accounting system (required) — QuickBooks Online · QuickBooks Desktop · Xero · NetSuite · Sage Intacct · Other
15. What does your board, bank or investor ask for most — and what do they get today? (long text)
16. How did you find us? — A Board-Ready Session on LinkedIn · The Board-Ready Brief · A referral or introduction · An event · Search · Other
17. I understand that no files are uploaded here, that Matthew will reply by email with a secure folder for my files, and that the sample packet is for my organization's own evaluation. (choice, required) — Yes

The form's theme is teal today; the site is navy. In Microsoft Forms, Style → pick a plain white or navy theme so it sits inside the page quietly.

## Still open

1. **Edit the Microsoft Form** as above (Matthew's account).
2. **Sample Board Brief PDF** — upload to `website/downloads/` via the GitHub web UI.
3. **Preview check** — the form submitted once from the preview; phone and laptop.
4. **Service Offer / Terms rev v1.3** — "within" wording and the Academy as a paid add-on on every cadence, before Thursday.

## Before merge

- [ ] Microsoft Form retitled and reworded to match the site
- [ ] Jason's reply to the courtesy note
- [ ] Sample Board Brief PDF uploaded to `website/downloads/`
- [ ] Preview checked on a phone and a laptop; form submitted once
- [ ] Merge → live. Only then share the nonprofit page with Jamie, after Thursday's green light.

**Jason's QR code (optional):** point it at `https://www.engermansolutions.com/?utm_source=jason&utm_medium=flyer&utm_campaign=california` so leads from his room are attributable.

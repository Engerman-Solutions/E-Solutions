# Agent-Friendly Delivery Plan

## Overview

Strategy for serving Engerman website content in multiple formats — HTML for browsers, markdown for AI agents, LLMs, and programmatic consumers — via content negotiation on the `Accept` header.

---

## Content Negotiation Approach

### How It Works

When a client requests a page, the server inspects the `Accept` header:

| Accept Header | Response |
|---------------|----------|
| `text/html` (default) | Full HTML page with styles, nav, footer |
| `text/markdown` | Clean markdown with frontmatter metadata |
| `application/json` | Structured JSON (future: API responses) |

### Implementation

**Option A: Edge middleware (recommended for static hosting)**

```
# Cloudflare Workers / Vercel Edge Middleware / Netlify Edge Functions

if (request.headers.get('Accept')?.includes('text/markdown')) {
  // Rewrite to /content/{path}.md
  return fetch(`${origin}/content${pathname}.md`)
}
// Default: serve HTML
```

**Option B: Server-side route handler**

```
# Express / Fastify / similar
app.get('/security', (req, res) => {
  if (req.accepts('text/markdown')) {
    return res.type('text/markdown').sendFile('content/security.md')
  }
  res.sendFile('pages/security.html')
})
```

**Option C: Static file convention (simplest)**

```
/pages/security.html      → Browser default
/content/security.md       → Agent-friendly version
/content/pricing.md        → Agent-friendly version
```

With a `<link rel="alternate">` tag in HTML:
```html
<link rel="alternate" type="text/markdown" href="/content/security.md">
```

---

## Markdown Content Structure

Each markdown file follows a consistent structure with YAML frontmatter:

```markdown
---
title: "Security & AI Governance"
description: "How Engerman handles data, AI governance, and compliance"
last_updated: "2026-03-19"
page_type: "security"
nav_order: 4
---

# Security & AI Governance

## Quick Summary
...content...

## AI Governance
...content...
```

### Frontmatter Fields

| Field | Type | Purpose |
|-------|------|---------|
| `title` | string | Page title for indexing |
| `description` | string | Meta description / summary |
| `last_updated` | date | Content freshness signal |
| `page_type` | string | Template identifier |
| `nav_order` | integer | Position in site navigation |
| `pricing_tiers` | array | Structured pricing data (pricing page only) |
| `faq` | array | Structured Q&A pairs (pricing page only) |

---

## Pages to Serve as Markdown

### Priority 1 (Immediate — high agent value)

| Page | HTML Path | Markdown Path | Rationale |
|------|-----------|---------------|-----------|
| Security | `/pages/security.html` | `/content/security.md` | Procurement bots, compliance scrapers |
| Pricing | `/pages/pricing.html` | `/content/pricing.md` | Comparison tools, budget bots |
| How It Works | `/pages/how-it-works.html` | `/content/how-it-works.md` | Technical evaluation agents |

### Priority 2 (Next sprint)

| Page | HTML Path | Markdown Path | Rationale |
|------|-----------|---------------|-----------|
| Sample Output | `/pages/sample-output.html` | `/content/sample-output.md` | Product evaluation |
| Homepage | `/index.html` | `/content/index.md` | General discovery |

### Priority 3 (Future)

| Page | Markdown Path | Rationale |
|------|---------------|-----------|
| API Docs | `/content/docs/api.md` | Developer integration |
| Changelog | `/content/changelog.md` | Version tracking |
| Status | `/content/status.md` | Service availability |

---

## Structured Data for Agents

### Pricing (machine-readable)

The pricing markdown includes a YAML block that agents can parse directly:

```yaml
pricing_tiers:
  - name: Pilot
    price_monthly: 1500
    currency: USD
    commitment: "90-day design partner"
    entities: 1
    memos_per_month: 3
    sla: "48 hours"

  - name: Starter
    price_monthly_range: [3000, 4000]
    currency: USD
    entities: "up to 3"
    memos_per_month: "unlimited"
    sla: "24 hours"

  - name: Pro
    price_monthly_range: [8000, 10000]
    currency: USD
    entities: "5+"
    memos_per_month: "unlimited"
    sla: "24h standard / 4h close-week"

  - name: Enterprise
    price_monthly_min: 15000
    currency: USD
    contact_required: true
```

### FAQ (structured)

```yaml
faq:
  - q: "What's included in the pilot?"
    a: "90-day design partner program at $1,500/month..."
  - q: "What happens after the pilot?"
    a: "Transition to Starter or Pro tier..."
```

---

## Implementation Checklist

### Phase 1: Static Markdown Files
- [ ] Create `/website/content/` directory
- [ ] Write `security.md` with frontmatter (from security.html content)
- [ ] Write `pricing.md` with structured pricing YAML
- [ ] Write `how-it-works.md` with workflow steps
- [ ] Add `<link rel="alternate" type="text/markdown">` to HTML pages
- [ ] Test: `curl -H "Accept: text/markdown" https://engerman.com/security`

### Phase 2: Edge Middleware
- [ ] Deploy edge function for Accept header routing
- [ ] Add `Vary: Accept` response header for correct caching
- [ ] Add `Content-Type: text/markdown; charset=utf-8` header
- [ ] Validate with common AI agents (ChatGPT browse, Perplexity, Claude)

### Phase 3: Structured Endpoints
- [ ] `/api/pricing.json` — machine-readable pricing
- [ ] `/api/security.json` — compliance metadata
- [ ] `/.well-known/ai-plugin.json` — OpenAI plugin manifest (if applicable)
- [ ] `robots.txt` — allow AI crawlers on /content/ paths

---

## robots.txt Recommendations

```
User-agent: *
Allow: /
Allow: /content/

# AI agent specific
User-agent: GPTBot
Allow: /content/
Allow: /pages/

User-agent: Claude-Web
Allow: /content/
Allow: /pages/

User-agent: PerplexityBot
Allow: /content/
Allow: /pages/

Sitemap: https://engerman.com/sitemap.xml
```

---

## Testing & Validation

### Manual Tests

```bash
# Should return markdown
curl -H "Accept: text/markdown" https://engerman.com/security

# Should return HTML (default)
curl https://engerman.com/security

# Should return markdown with correct headers
curl -v -H "Accept: text/markdown" https://engerman.com/pricing 2>&1 | grep Content-Type
# Expected: Content-Type: text/markdown; charset=utf-8
```

### Automated Tests

| Test | Expected |
|------|----------|
| HTML default | `Content-Type: text/html` |
| Markdown request | `Content-Type: text/markdown` |
| Vary header present | `Vary: Accept` |
| Frontmatter valid | YAML parses without error |
| Links resolve | All markdown links return 200 |
| Pricing YAML | All tiers have required fields |
| Freshness | `last_updated` within 30 days |

---

## Monitoring

| Metric | Purpose |
|--------|---------|
| Markdown request count | Agent adoption tracking |
| User-agent distribution | Which agents consume content |
| Cache hit rate | CDN efficiency for dual-format |
| Stale content alerts | Flag markdown files older than HTML |

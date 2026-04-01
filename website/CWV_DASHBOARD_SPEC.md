# RUM + Core Web Vitals Dashboard Specification

## Overview

Real User Monitoring (RUM) instrumentation and dashboard configuration for tracking Core Web Vitals, conversion funnels, and page-level performance across all Engerman website templates.

---

## CWV Targets (per Google "Good" threshold)

| Metric | Target | Measurement |
|--------|--------|-------------|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 75th percentile |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 75th percentile |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 75th percentile |
| **TTFB** (Time to First Byte) | ≤ 800ms | 75th percentile |
| **FCP** (First Contentful Paint) | ≤ 1.8s | 75th percentile |

---

## Instrumentation (Already in `js/main.js`)

```javascript
// LCP — PerformanceObserver('largest-contentful-paint')
// CLS — PerformanceObserver('layout-shift') with session windowing
// INP — PerformanceObserver('event') with interactionId dedup
```

### Events to Beacon

Each metric fires a `cwv:report` event with this payload:

| Field | Type | Example |
|-------|------|---------|
| `metric` | string | `"LCP"`, `"INP"`, `"CLS"` |
| `value` | number | `1847` (ms) or `0.03` (CLS score) |
| `rating` | string | `"good"`, `"needs-improvement"`, `"poor"` |
| `page_template` | string | `"homepage"`, `"sample-output"`, `"pricing"`, `"security"`, `"how-it-works"` |
| `device_type` | string | `"desktop"`, `"tablet"`, `"mobile"` |
| `connection` | string | `"4g"`, `"3g"`, `"slow-2g"` |
| `timestamp` | ISO 8601 | `"2026-03-19T14:30:00Z"` |
| `session_id` | string | UUID v4 |
| `url` | string | Full page URL |

### Rating Thresholds

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP | ≤ 2500ms | 2501–4000ms | > 4000ms |
| INP | ≤ 200ms | 201–500ms | > 500ms |
| CLS | ≤ 0.1 | 0.101–0.25 | > 0.25 |
| FCP | ≤ 1800ms | 1801–3000ms | > 3000ms |
| TTFB | ≤ 800ms | 801–1800ms | > 1800ms |

---

## CTA & Conversion Events

### Event Taxonomy

| Event Name | Trigger | Properties |
|------------|---------|------------|
| `cta:click` | Any CTA button/link click | `label`, `funnel_stage`, `page`, `section` |
| `cta:hero_primary` | "See Sample Output" hero click | `page: "homepage"` |
| `cta:hero_secondary` | "Book Evaluation" hero click | `page: "homepage"` |
| `cta:pricing_pilot` | "Start Pilot" click | `tier: "pilot"` |
| `cta:pricing_starter` | "Book Evaluation" pricing click | `tier: "starter"` |
| `cta:pricing_pro` | "Contact Us" Pro click | `tier: "pro"` |
| `cta:pricing_enterprise` | "Contact Us" Enterprise click | `tier: "enterprise"` |
| `cta:security_review` | "Start Security Review" click | `page: "security"` |
| `cta:request_docs` | "Request SOC 2 / DPA" click | `page: "security"` |
| `form:evaluation_start` | Evaluation form interaction | First field focus |
| `form:evaluation_submit` | Evaluation form submission | All field values |
| `form:evaluation_error` | Validation failure | Error field(s) |

### Funnel Stage Labels

| Stage | CTAs |
|-------|------|
| `explore` | "See Sample Output", "How It Works", "View annotated example" |
| `evaluate` | "Run on sample dataset", "Get integration checklist", "Compare plans" |
| `convert` | "Book Evaluation", "Start Pilot", "Request Pilot Pricing", "Start Security Review" |

---

## Dashboard Panels

### Panel 1: CWV Overview (Real-Time)

**Visualization:** 3 large gauge/donut charts (LCP, INP, CLS)

| Display | Source |
|---------|--------|
| Current p75 value | Rolling 24h window |
| Good/NI/Poor distribution | Pie breakdown per metric |
| Trend sparkline | 7-day trend |
| Pass rate % | % sessions rated "good" |

### Panel 2: CWV by Page Template

**Visualization:** Table with conditional formatting

| Column | Description |
|--------|-------------|
| Page Template | homepage, sample-output, pricing, security, how-it-works |
| LCP p75 | Color-coded: green/yellow/red |
| INP p75 | Color-coded |
| CLS p75 | Color-coded |
| Page Views | Count in period |
| LCP Element | Most common LCP target element |

### Panel 3: CWV by Device & Connection

**Visualization:** Grouped bar chart

- Group by: `device_type` (desktop, tablet, mobile)
- Bars: LCP, INP, CLS per device
- Filter: connection type (4g, 3g, slow-2g)
- Alert: if mobile LCP p75 > 3000ms

### Panel 4: Conversion Funnel

**Visualization:** Funnel chart

| Stage | Event |
|-------|-------|
| Landing | Page view (any page) |
| Explore | `cta:hero_primary` or sample-output page view |
| Evaluate | Tab interaction on sample-output or pricing page view |
| Convert | `form:evaluation_start` |
| Submit | `form:evaluation_submit` |

### Panel 5: CTA Heatmap

**Visualization:** Table/heatmap

| Column | Description |
|--------|-------------|
| CTA Label | Button text |
| Page | Source page |
| Funnel Stage | explore/evaluate/convert |
| Click Count | Total clicks in period |
| Click Rate | Clicks / page views |
| CWV at Click | Avg LCP on page where CTA was clicked |

### Panel 6: CWV ↔ Conversion Correlation

**Visualization:** Scatter plot or segmented bar

- X-axis: LCP rating (good, needs-improvement, poor)
- Y-axis: Conversion rate (form submissions / sessions)
- Hypothesis: sessions with "good" LCP convert at higher rate
- Segment by page template

---

## Alerts

| Alert | Condition | Channel | Priority |
|-------|-----------|---------|----------|
| LCP regression | p75 > 2.5s for 1 hour | Slack + email | P1 |
| CLS regression | p75 > 0.1 for 1 hour | Slack + email | P1 |
| INP regression | p75 > 200ms for 1 hour | Slack + email | P1 |
| Mobile LCP degraded | Mobile LCP p75 > 3.0s for 30 min | Slack | P2 |
| Form abandonment spike | Abandonment rate > 60% for 1 hour | Slack | P2 |
| Zero submissions | No `form:evaluation_submit` for 24h | Email | P3 |

---

## Implementation Notes

### Phase 1: Lightweight (Current — `js/main.js`)
- PerformanceObserver for LCP, CLS, INP
- Beacon to `/api/cwv` endpoint (or `navigator.sendBeacon`)
- No third-party scripts

### Phase 2: Analytics Integration
- Recommended: **web-vitals** library (Google, ~1.5KB gzipped)
- Send to: Google Analytics 4 (`gtag('event', ...)`) or custom endpoint
- Alternatives: Vercel Analytics, Cloudflare Web Analytics, SpeedCurve

### Phase 3: Full RUM
- Session replay for conversion debugging (PostHog, LogRocket)
- Error tracking correlation (Sentry)
- A/B test CWV impact measurement

### Data Retention
| Tier | Retention |
|------|-----------|
| Raw events | 30 days |
| Aggregated hourly | 90 days |
| Aggregated daily | 1 year |
| Monthly summaries | Indefinite |

---

## LCP Budget by Page Template

| Page | Target LCP Element | Budget |
|------|-------------------|--------|
| Homepage | Hero H1 + subheading text | ≤ 2.0s |
| Sample Output | Memo viewer heading | ≤ 2.3s |
| Pricing | Tier cards | ≤ 2.0s |
| Security | Quick summary cards | ≤ 2.0s |
| How It Works | Page hero text | ≤ 2.0s |

### LCP Optimization Checklist
- [ ] Preload critical CSS (`<link rel="preload" as="style">`)
- [ ] Preconnect to font CDN (`<link rel="preconnect">`)
- [ ] `font-display: swap` on all web fonts
- [ ] No render-blocking JS above the fold
- [ ] `fetchpriority="high"` on hero images (if any)
- [ ] Server response time < 200ms (static hosting)
- [ ] Enable Brotli/gzip compression
- [ ] Set long cache headers on static assets

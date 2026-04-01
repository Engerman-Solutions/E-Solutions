# Engerman Design System & Style Guide

## Brand Identity

**Name:** Engerman
**Logo:** Engerman mark — a 3x3 grid of navy/transparent blocks forming a stylized "E"
**Typography:** Inter (sans-serif), SF Mono (monospace)
**Tone:** Calm, precise, audit-friendly. Finance software, not AI theater.

### Logo System

The Engerman mark is an 8-block 3x3 grid (middle-right position empty) forming a stylized "E". It uses `currentColor` in the inline SVG so it automatically adapts to light and dark surfaces.

| Asset | File | Usage |
|-------|------|-------|
| Mark (navy) | `img/engerman-mark.svg` | Standalone mark on light backgrounds |
| Mark (inverted) | `img/engerman-mark-inverted.svg` | Standalone mark on dark backgrounds |
| Logo lockup (navy) | `img/engerman-logo.svg` | Mark + "Engerman" wordmark on light |
| Logo lockup (inverted) | `img/engerman-logo-inverted.svg` | Mark + "Engerman" wordmark on dark |

#### Header Brand Lockup

```html
<a href="/" class="nav__logo" aria-label="Engerman — Home">
  <svg class="nav__logo-mark" viewBox="0 0 36 36" fill="currentColor" aria-hidden="true">
    <rect x="0" y="0" width="10" height="10" rx="2"/>
    <rect x="13" y="0" width="10" height="10" rx="2"/>
    <rect x="26" y="0" width="10" height="10" rx="2"/>
    <rect x="0" y="13" width="10" height="10" rx="2"/>
    <rect x="13" y="13" width="10" height="10" rx="2"/>
    <rect x="0" y="26" width="10" height="10" rx="2"/>
    <rect x="13" y="26" width="10" height="10" rx="2"/>
    <rect x="26" y="26" width="10" height="10" rx="2"/>
  </svg>
  <span>Engerman</span>
</a>
```

- Mark: 36x36px in header, 32x32px in footer
- Wordmark: `--text-xl` (20px), `--weight-bold`, `-0.01em` letter-spacing
- Gap between mark and wordmark: `--space-3` (12px)
- Uses `fill="currentColor"` — inherits text color from parent (navy on white, white on navy)

#### Logo Usage Rules

| Surface | Color | Implementation |
|---------|-------|----------------|
| White / off-white | Navy (`--color-navy-800`) | Default `color` on `.nav__logo` |
| Navy / dark sections | White | Set `style="color: var(--color-white)"` on `.nav__logo` |
| Gray-50 alternate | Navy | Same as white surface |
| Image backgrounds | Avoid or use inverted with sufficient contrast |

#### Missing Source Assets

The current implementation uses inline SVG for the mark. For external use (email, print, social):
- Export `engerman-mark.svg` to PNG at 2x and 4x resolution
- Create `engerman-logo-transparent.png` (mark + wordmark, transparent background)
- Create `engerman-logo-inverted.png` (white mark + wordmark for dark backgrounds)
- Provide EPS/AI format for print vendors

---

## Color Tokens

### Brand Palette (from Engerman logo)

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-navy-800` | `#192746` | Primary brand, headings, buttons |
| `--color-navy-900` | `#131E30` | Deep backgrounds |
| `--color-navy-700` | `#1F3058` | Hover states |
| `--color-blue-600` | `#3859A9` | Accent, links, interactive |
| `--color-blue-500` | `#4A6EC0` | Focus rings, highlights |
| `--color-blue-100` | `#DFE7F6` | Light accent backgrounds |
| `--color-blue-50` | `#EEF2FA` | Card/icon backgrounds |
| `--color-gray-300` | `#B6C0CB` | Neutral, borders, secondary text |
| `--color-gray-100` | `#E7EAED` | Off-white surfaces |
| `--color-gray-50` | `#F4F5F7` | Alternate section backgrounds |

### Semantic Tokens

| Token | Maps To | Usage |
|-------|---------|-------|
| `--color-surface` | white | Default page background |
| `--color-surface-alt` | gray-50 | Alternating sections |
| `--color-text` | gray-900 | Primary body text |
| `--color-text-secondary` | gray-600 | Supporting text |
| `--color-border` | gray-200 | Standard borders |
| `--color-accent` | blue-600 | Interactive elements |

### Status Colors

| Status | Background | Foreground |
|--------|-----------|------------|
| Success/Favorable | `#DCFCE7` | `#16803C` |
| Warning/Watch | `#FEF9C3` | `#CA8A04` |
| Error/Unfavorable | `#FEE2E2` | `#DC2626` |

---

## Typography Scale

Based on a 1.200 (minor third) scale from 16px base.

| Token | Size | Line Height | Usage |
|-------|------|-------------|-------|
| `--text-xs` | 12px | 1.5 | Badges, metadata, timestamps |
| `--text-sm` | 14px | 1.5 | Secondary text, table cells, nav links |
| `--text-base` | 16px | 1.5 | Body text, form inputs |
| `--text-lg` | 18px | 1.35 | Subheadings, hero subtext |
| `--text-xl` | 20px | 1.2 | H4, card headings |
| `--text-2xl` | 24px | 1.2 | H3 |
| `--text-3xl` | 30px | 1.2 | H2 |
| `--text-4xl` | 36px | 1.2 | H1 (desktop) |
| `--text-5xl` | 48px | 1.2 | Display (reserved) |

### Font Weights

| Token | Weight | Usage |
|-------|--------|-------|
| `--weight-normal` | 400 | Body text |
| `--weight-medium` | 500 | Nav links, labels |
| `--weight-semibold` | 600 | Overlines, badges, buttons |
| `--weight-bold` | 700 | Headings, strong emphasis |

---

## Spacing System

4px base unit. Use token names, not raw values.

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | Tight gaps (badge padding) |
| `--space-2` | 8px | Default gap in tight layouts |
| `--space-3` | 12px | Button padding, small card padding |
| `--space-4` | 16px | Paragraph margin, standard gap |
| `--space-6` | 24px | Card padding, section sub-gaps |
| `--space-8` | 32px | Major section gaps |
| `--space-10` | 40px | Footer column gaps |
| `--space-12` | 48px | Small section padding |
| `--space-16` | 64px | Footer padding |
| `--space-20` | 80px | Standard section padding |
| `--space-24` | 96px | Large section padding |

---

## Component Library

### Buttons

| Class | Usage | States |
|-------|-------|--------|
| `.btn--primary` | Primary actions (navy bg) | hover: navy-700, disabled: 50% opacity |
| `.btn--secondary` | Secondary actions (navy outline) | hover: fill navy, disabled: 50% opacity |
| `.btn--ghost` | Tertiary/inline actions (blue text) | hover: blue-50 bg |
| `.btn--lg` | Hero/CTA prominence | |
| `.btn--sm` | Compact contexts (nav, tables) | |

### Cards

| Class | Usage |
|-------|-------|
| `.card` | Default bordered card |
| `.card--elevated` | Shadow-based card (no border) |

### Badges

| Class | Usage |
|-------|-------|
| `.badge--green` | Favorable, validated, complete |
| `.badge--amber` | Watch, in progress |
| `.badge--red` | Unfavorable, error |
| `.badge--blue` | Informational |
| `.badge--gray` | Neutral, logged |

### Tabs

Accessible tabs using `role="tablist"`, `role="tab"`, `role="tabpanel"`.
- Arrow key navigation between tabs
- `aria-selected` state management
- Hidden panels use `hidden` attribute

### Tables

Wrap in `.table-wrap` for responsive horizontal scroll.
Use `.table` class for consistent styling.

---

## UI States

| State | Visual Treatment |
|-------|-----------------|
| **Default** | Standard styling |
| **Hover** | Background shift + `translateY(-1px)` lift on buttons, `translateY(-2px)` on cards |
| **Focus** | 2px solid blue-500 outline, 2px offset (keyboard only via `:focus-visible`) |
| **Active** | `translateY(0)` — settles back to baseline on press |
| **Disabled** | 50% opacity, `cursor: not-allowed`, `pointer-events: none` |

---

## Motion & Animation

**Principle:** Smoothness over spectacle. Motion enhances credibility, never distracts.

### Hero Entrance

| Element | Animation | Duration | Easing | Delay |
|---------|-----------|----------|--------|-------|
| `.hero__content` | Fade-up (opacity 0→1, translateY 24→0) | 0.8s | `ease-out-expo` | 0s |
| `.memo-preview` | Fade-up + gentle float | 0.8s entrance, 6s float | expo / ease-in-out | 0.15s / 1.2s |

### Scroll Reveal

Sections below the fold use `IntersectionObserver` to trigger on scroll:

| Class | Behavior |
|-------|----------|
| `.scroll-fade` | Fade-up: opacity 0→1, translateY 20→0, 0.7s ease-out-expo |
| `.scroll-stagger` | Children stagger: each child fades up, 0.1s delay between children |
| `.is-visible` | Added by JS when element crosses 12% viewport threshold |

### Float Animation

```css
@keyframes gentle-float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}
```

Used on hero memo preview only. 6s cycle, ease-in-out. Starts 1.2s after page load.

### Reduced Motion

All animations respect `prefers-reduced-motion: reduce`:
- Hero entrance: disabled (`animation: none`)
- Scroll reveal: all elements visible immediately (`opacity: 1, transform: none`)
- Float: disabled
- Hover transforms remain (they are user-initiated)

### Easing

| Token | Value | Usage |
|-------|-------|-------|
| `--ease-out-expo` | `cubic-bezier(0.16, 1, 0.3, 1)` | Entrance animations, scroll reveals |
| `ease` (CSS default) | — | Hover transitions |
| `ease-in-out` | — | Looping animations (float) |

### What NOT to add

- Parallax scrolling on text or backgrounds
- Page transition animations
- Loading spinners or skeleton screens (static site)
- Auto-playing carousels or sliders
- Particle effects, gradients-in-motion, or animated backgrounds
- Any animation that loops indefinitely on interactive elements

---

## Layout

| Token | Value | Usage |
|-------|-------|-------|
| `--container-max` | 1200px | Standard content width |
| `--container-narrow` | 800px | Text-heavy pages |
| `--container-wide` | 1400px | Full-width sections |

### Grid System

CSS Grid with gap utilities:
- `.grid--2` through `.grid--4` for column layouts
- Responsive: collapses to 1 column at 768px

### Breakpoints

| Name | Width | Changes |
|------|-------|---------|
| Desktop | > 1024px | Full layout |
| Tablet | 768px–1024px | 4-col → 2-col grids |
| Mobile | < 768px | Single column, stacked nav |
| Small | < 480px | Tighter spacing |

---

## Shadows

| Token | Usage |
|-------|-------|
| `--shadow-xs` | Subtle lift (inputs) |
| `--shadow-sm` | Cards at rest |
| `--shadow-md` | Card hover, elevated elements |
| `--shadow-lg` | Dropdowns, mobile nav |
| `--shadow-xl` | Hero visual, modal |

---

## Borders & Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | 4px | Badges, small elements |
| `--radius-md` | 8px | Buttons, inputs, small cards |
| `--radius-lg` | 12px | Cards, panels |
| `--radius-xl` | 16px | Hero visual, memo viewer |
| `--radius-full` | 9999px | Pills, badges |

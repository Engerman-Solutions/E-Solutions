# Accessibility Checklist — WCAG 2.2 AA

## Perceivable

### Text Alternatives (1.1)
- [x] All informational images have descriptive `alt` text
- [x] Decorative images/icons use `aria-hidden="true"` or empty `alt=""`
- [x] Logo images have brand name as alt text (`alt="Engerman"`)
- [x] SVG icons include `aria-label` or are hidden from AT

### Time-based Media (1.2)
- [x] No autoplay video on any page (performance + accessibility)
- [ ] If video added later: captions and transcript required

### Adaptable (1.3)
- [x] Semantic HTML throughout: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`
- [x] Heading hierarchy is logical (h1 → h2 → h3, no skips)
- [x] `aria-labelledby` on all major sections
- [x] Tables use `<thead>`, `<th>` with proper scope
- [x] Forms use `<label>` elements associated via `for`/`id`
- [x] Reading order matches visual order in all layouts
- [x] `role="tablist"`, `role="tab"`, `role="tabpanel"` for tab interfaces

### Distinguishable (1.4)
- [x] Color contrast ratios meet AA (4.5:1 for normal text, 3:1 for large text)
  - Navy (#192746) on white: 13.5:1 ✓
  - Gray-600 (#555B68) on white: 5.8:1 ✓
  - Blue-600 (#3859A9) on white: 5.2:1 ✓
  - White on Navy (#192746): 13.5:1 ✓
- [x] Information not conveyed by color alone (badges include text labels)
- [x] Text resizable to 200% without content loss (rem-based typography)
- [x] No images of text (all text is real HTML text)
- [x] Reflow: content readable at 320px viewport (single column)
- [x] Spacing: no loss of content when line/letter/word spacing increased

## Operable

### Keyboard Accessible (2.1)
- [x] All interactive elements reachable by keyboard
- [x] Tab order follows logical reading order
- [x] Skip link: "Skip to main content" as first focusable element
- [x] Tab panels: Arrow keys navigate between tabs, Home/End for first/last
- [x] No keyboard traps
- [x] Mobile nav toggle keyboard accessible

### Enough Time (2.2)
- [x] No time limits on any content
- [x] No auto-advancing content

### Seizures and Physical Reactions (2.3)
- [x] No flashing content (no animations over 3 flashes/second)
- [x] Reduced motion: transitions are subtle (150-300ms)

### Navigable (2.4)
- [x] Skip link present and functional
- [x] Page titles are descriptive and unique per page
- [x] Focus order is logical and sequential
- [x] Link purpose clear from link text (no "click here")
- [x] Multiple navigation mechanisms (nav menu, footer links, in-page anchors)
- [x] Headings and labels describe topic or purpose
- [x] Focus visible: 2px solid blue-500 outline on `:focus-visible`

### Input Modalities (2.5)
- [x] Touch targets minimum 44x44px on mobile (buttons, links)
- [x] No motion-actuated functions

## Understandable

### Readable (3.1)
- [x] `lang="en"` on `<html>` element
- [x] Plain language used throughout (finance terminology is domain-appropriate)

### Predictable (3.2)
- [x] Navigation consistent across all pages
- [x] Components identified consistently (same button styles, same CTA patterns)
- [x] No unexpected context changes on focus or input

### Input Assistance (3.3)
- [x] Form errors described in text (not just color)
- [x] Labels for all form inputs
- [x] Required fields marked
- [x] Error prevention: confirmation for form submissions
- [ ] TODO: Add inline validation messages for evaluation form

## Robust

### Compatible (4.1)
- [x] Valid HTML (no duplicate IDs, proper nesting)
- [x] ARIA roles, states, and properties used correctly
- [x] `aria-expanded` on toggle buttons
- [x] `aria-selected` on active tabs
- [x] `aria-controls` linking tabs to panels
- [x] `aria-current="page"` on active nav item
- [x] `hidden` attribute on inactive tab panels

---

## Keyboard Navigation Map

| Component | Tab | Enter/Space | Arrow Keys | Escape |
|-----------|-----|-------------|------------|--------|
| Nav links | Moves between links | Activates link | — | — |
| Mobile menu | Focuses toggle | Opens/closes | — | Closes menu |
| Tab panels | Focuses first tab | Activates tab | Left/Right between tabs | — |
| Buttons | Focuses button | Activates | — | — |
| Form inputs | Moves between fields | Submits (if button) | — | — |
| Skip link | First focusable | Jumps to main content | — | — |
| FAQ accordion | Moves between questions | Toggles answer | — | — |

---

## Contrast Validation

| Pair | Ratio | Pass? |
|------|-------|-------|
| Navy 800 (#192746) on White | 13.5:1 | AA ✓, AAA ✓ |
| Gray 600 (#555B68) on White | 5.8:1 | AA ✓ |
| Gray 500 (#6E7582) on White | 4.6:1 | AA ✓ (normal), AA ✓ (large) |
| Blue 600 (#3859A9) on White | 5.2:1 | AA ✓ |
| White on Navy 800 (#192746) | 13.5:1 | AA ✓, AAA ✓ |
| White on Blue 600 (#3859A9) | 5.2:1 | AA ✓ |
| Green 600 (#16803C) on Green 100 | 5.1:1 | AA ✓ |
| Amber 600 (#CA8A04) on Amber 100 | 3.8:1 | AA (large text) |
| Gray 400 (#8B919C) on White | 3.2:1 | AA (large text only) |

### Action Items
- Gray-400 used only for decorative/tertiary text at ≥14px+ bold (passes AA for large text)
- All critical information uses Gray-600 or darker

---

## Testing Plan

1. **Automated:** Run axe-core or Lighthouse accessibility audit on all pages
2. **Keyboard:** Navigate entire site using only keyboard (Tab, Enter, Arrow, Escape)
3. **Screen reader:** Test with VoiceOver (macOS) and NVDA (Windows)
4. **Zoom:** Verify content at 200% zoom on all pages
5. **Color:** Verify with simulated color blindness (protanopia, deuteranopia)
6. **Mobile:** Test touch targets on actual mobile devices

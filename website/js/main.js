/* ============================================================
   Engerman — Minimal JS (performance-first)
   Islands approach: only hydrate interactive components.
   Targets INP ≤ 200ms.
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  /* ── Mobile nav toggle ──────────────────────────────── */
  const toggle = document.querySelector('.nav__toggle');
  const links = document.querySelector('.nav__links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
    document.addEventListener('click', (e) => {
      if (!toggle.contains(e.target) && !links.contains(e.target)) {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ── Tab panels ─────────────────────────────────────── */
  document.querySelectorAll('[role="tablist"]').forEach(tablist => {
    const tabs = tablist.querySelectorAll('[role="tab"]');
    const panels = tablist.parentElement.querySelectorAll('[role="tabpanel"]');

    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => {
          t.setAttribute('aria-selected', 'false');
          t.classList.remove('active');
        });
        panels.forEach(p => {
          p.classList.remove('active');
          p.hidden = true;
        });

        tab.setAttribute('aria-selected', 'true');
        tab.classList.add('active');
        const panel = document.getElementById(tab.getAttribute('aria-controls'));
        if (panel) {
          panel.classList.add('active');
          panel.hidden = false;
        }
      });

      /* Keyboard nav for tabs (WCAG) */
      tab.addEventListener('keydown', (e) => {
        const tabArr = Array.from(tabs);
        const idx = tabArr.indexOf(tab);
        let next;
        if (e.key === 'ArrowRight') next = tabArr[(idx + 1) % tabArr.length];
        if (e.key === 'ArrowLeft') next = tabArr[(idx - 1 + tabArr.length) % tabArr.length];
        if (e.key === 'Home') next = tabArr[0];
        if (e.key === 'End') next = tabArr[tabArr.length - 1];
        if (next) {
          e.preventDefault();
          next.focus();
          next.click();
        }
      });
    });
  });

  /* ── Smooth scroll for anchor links ─────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const id = anchor.getAttribute('href').slice(1);
      const target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        /* Close mobile nav if open */
        if (links) links.classList.remove('open');
      }
    });
  });

  /* ── Scroll reveal (IntersectionObserver) ───────────── */
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reducedMotion) {
    const revealEls = document.querySelectorAll('.scroll-fade, .scroll-stagger');
    if (revealEls.length) {
      const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            revealObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      revealEls.forEach(el => revealObserver.observe(el));
    }
  }

  /* ── CWV RUM instrumentation stub ───────────────────── */
  if ('PerformanceObserver' in window) {
    /* LCP */
    try {
      new PerformanceObserver((list) => {
        const entries = list.getEntries();
        const last = entries[entries.length - 1];
        console.log('[CWV] LCP:', Math.round(last.startTime), 'ms');
      }).observe({ type: 'largest-contentful-paint', buffered: true });
    } catch (e) { /* not supported */ }

    /* CLS */
    try {
      let cls = 0;
      new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          if (!entry.hadRecentInput) cls += entry.value;
        }
        console.log('[CWV] CLS:', cls.toFixed(4));
      }).observe({ type: 'layout-shift', buffered: true });
    } catch (e) { /* not supported */ }

    /* INP approximation via event timing */
    try {
      let maxINP = 0;
      new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          if (entry.duration > maxINP) maxINP = entry.duration;
        }
        console.log('[CWV] INP candidate:', maxINP, 'ms');
      }).observe({ type: 'event', buffered: true, durationThreshold: 16 });
    } catch (e) { /* not supported */ }
  }
});

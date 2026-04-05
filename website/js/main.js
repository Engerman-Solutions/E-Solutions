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

// ════════════════════════════════════════════════════
// EVALUATION FORM HANDLER
// ════════════════════════════════════════════════════
(function() {
  const form = document.querySelector('.eval-form');
  if (!form) return;

  form.addEventListener('submit', function(e) {
    e.preventDefault();

    // Gather form data
    const name = form.querySelector('#eval-name')?.value || '';
    const email = form.querySelector('#eval-email')?.value || '';
    const company = form.querySelector('#eval-company')?.value || '';
    const accounting = form.querySelector('#eval-accounting')?.value || '';
    const entities = form.querySelector('#eval-entities')?.value || '';
    const pain = form.querySelector('#eval-pain')?.value || '';

    // Basic validation
    if (!name || !email || !company || !accounting || !entities) {
      alert('Please fill in all required fields.');
      return;
    }

    // Build mailto link with form data
    const subject = encodeURIComponent('New Evaluation Request — ' + company);
    const body = encodeURIComponent(
      'New Evaluation Request\n' +
      '========================\n\n' +
      'Name: ' + name + '\n' +
      'Email: ' + email + '\n' +
      'Company: ' + company + '\n' +
      'Accounting System: ' + accounting + '\n' +
      'Number of Entities: ' + entities + '\n' +
      'Pain Point: ' + pain + '\n\n' +
      '---\n' +
      'Submitted from engermansolutions.com'
    );

    // Open email to send
    window.open('mailto:info@engermansolutions.com?subject=' + subject + '&body=' + body, '_blank');

    // Replace form with confirmation
    const evalSection = form.closest('.eval-grid');
    if (evalSection) {
      evalSection.innerHTML = 
        '<div style=text-align:center

// EVALUATION FORM HANDLER
(function() {
  var form = document.querySelector('.eval-form');
  if (!form) return;

  form.addEventListener('submit', function(e) {
    e.preventDefault();

    var name = form.querySelector('#eval-name').value || '';
    var email = form.querySelector('#eval-email').value || '';
    var company = form.querySelector('#eval-company').value || '';
    var acctEl = form.querySelector('#eval-accounting');
    var accounting = acctEl.options[acctEl.selectedIndex] ? acctEl.options[acctEl.selectedIndex].text : '';
    var entities = form.querySelector('#eval-entities').value || '';
    var pain = form.querySelector('#eval-pain').value || '';

    if (!name || !email || !company || !acctEl.value || !entities) {
      alert('Please fill in all required fields.');
      return;
    }

    var nl = String.fromCharCode(10);
    var subject = encodeURIComponent('New Evaluation Request - ' + company);
    var body = encodeURIComponent(
      'New Evaluation Request' + nl +
      '========================' + nl + nl +
      'Name: ' + name + nl +
      'Email: ' + email + nl +
      'Company: ' + company + nl +
      'Accounting System: ' + accounting + nl +
      'Number of Entities: ' + entities + nl +
      'Pain Point: ' + pain + nl + nl +
      '---' + nl +
      'Submitted from engermansolutions.com'
    );

    window.location.href = 'mailto:info@engermansolutions.com?subject=' + subject + '&body=' + body;

    var grid = form.closest('.eval-grid');
    if (grid) {
      var h = '';
      h += '<div style="text-align:center;padding:60px 20px;max-width:560px;margin:0 auto">';
      h += '<div style="width:64px;height:64px;background:#ecfdf5;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 24px">';
      h += '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>';
      h += '</div>';
      h += '<h2 style="margin-bottom:16px">Evaluation request received</h2>';
      h += '<p style="color:#6B7280;font-size:18px;margin-bottom:16px">Thank you, ' + name + '. We will review your request and reach out within 1 business day to schedule your 20-minute evaluation.</p>';
      h += '<p style="color:#9CA3AF;font-size:14px">A confirmation will be sent to <strong>' + email + '</strong></p>';
      h += '</div>';
      grid.innerHTML = h;
    }
  });
})();

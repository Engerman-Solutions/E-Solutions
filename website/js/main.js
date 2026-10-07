/* Engerman — minimal site JS: mobile nav, tabs, scroll reveal (clean rewrite of the live file's behaviour) */
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav__toggle'), links = document.querySelector('.nav__links');
  if (toggle && links) {
    toggle.addEventListener('click', function () { var open = links.classList.toggle('open'); toggle.setAttribute('aria-expanded', open); });
    document.addEventListener('click', function (e) { if (!toggle.contains(e.target) && !links.contains(e.target)) { links.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); } });
  }
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) { var id = a.getAttribute('href').slice(1); var t = id && document.getElementById(id); if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth', block: 'start' }); if (links) links.classList.remove('open'); } });
  });
  var els = document.querySelectorAll('.scroll-fade, .scroll-stagger');
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) { els.forEach(function (el) { el.classList.add('is-visible'); }); return; }
  var io = new IntersectionObserver(function (entries) { entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); } }); }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  els.forEach(function (el) { io.observe(el); });
});

// Engerman Solutions — one place for the links and endpoints the pages use.
// Fill these in once; every page reads them. Anything left blank falls back to email so nothing on the site is a dead link.
window.ES_CONFIG = {
  LINKEDIN_COMPANY_URL: "https://www.linkedin.com/company/engerman-solutions/",
  LINKEDIN_MATTHEW_URL: "https://www.linkedin.com/in/matthew-a-engerman-25b17a46",
  BRIEF_SUBSCRIBE_URL: "https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7477941237455491072",
  CALENDAR_URL: "",                // a booking link if you want one; otherwise email
  TRY_FORM_FOUNDERS_URL: "https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=TCp6pTf0lUWjidw_pJ41r8VK0JU18xlOmM5bOtgsLdhUNjA3SExCVVRJTE80NVNJM0JWTEhZV1pQSC4u", // Microsoft Form: Try it first — Founders & Operating Companies
  TRY_FORM_NONPROFITS_URL: "https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=TCp6pTf0lUWjidw_pJ41r8VK0JU18xlOmM5bOtgsLdhUNkxOU0RLQUJGMFpTWk1WRzNPWEdROVNPTC4u", // Microsoft Form: Try it first — Nonprofits & Associations
  FORM_ENDPOINT_SETUP: "",         // Setup Questionnaire: leave blank and the page opens the client's email app with the answers written; or build it as a second Microsoft Form and link to it instead
  CONTACT_EMAIL: "info@engermansolutions.com"
};
document.addEventListener("DOMContentLoaded", function () {
  var c = window.ES_CONFIG, mail = "mailto:" + c.CONTACT_EMAIL;
  document.querySelectorAll("[data-link]").forEach(function (a) {
    var key = a.getAttribute("data-link"), url = c[key];
    if (url) { a.href = url; a.target = "_blank"; a.rel = "noopener"; }
    else { a.href = mail + "?subject=" + encodeURIComponent(a.getAttribute("data-subject") || "Engerman Solutions"); }
  });
  // Footer "Follow" line — one source of truth, every page. Blank URLs are simply left out.
  var brand = document.querySelector(".footer__brand");
  if (brand && !brand.querySelector(".footer__follow")) {
    var items = [
      [c.LINKEDIN_MATTHEW_URL, "Matthew on LinkedIn"],
      [c.LINKEDIN_COMPANY_URL, "Engerman Solutions on LinkedIn"],
      [c.BRIEF_SUBSCRIBE_URL, "The Board-Ready Brief"]
    ].filter(function (i) { return i[0]; });
    if (items.length) {
      var p = document.createElement("p");
      p.className = "footer__follow";
      p.style.cssText = "margin-top: var(--space-3, 12px); font-size: 0.875rem; line-height: 1.7;";
      var label = document.createElement("span");
      label.textContent = "Follow: ";
      label.style.cssText = "color: var(--color-gray-400, #9aa3b2);";
      p.appendChild(label);
      items.forEach(function (i, n) {
        if (n) { var sep = document.createElement("span"); sep.textContent = " · "; sep.style.cssText = "color: var(--color-gray-400, #9aa3b2);"; p.appendChild(sep); }
        var a = document.createElement("a");
        a.href = i[0]; a.textContent = i[1]; a.target = "_blank"; a.rel = "noopener";
        a.style.cssText = "color: var(--color-gray-300, #c9d1dc);";
        p.appendChild(a);
      });
      var tag = brand.querySelector(".footer__tag");
      if (tag) { brand.insertBefore(p, tag); } else { brand.appendChild(p); }
    }
  }
});

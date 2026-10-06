// Engerman Solutions — one place for the links and endpoints the pages use.
// Fill these in once; every page reads them. Anything left blank falls back to email so nothing on the site is a dead link.
window.ES_CONFIG = {
  LINKEDIN_COMPANY_URL: "",        // e.g. https://www.linkedin.com/company/engerman-solutions
  LINKEDIN_MATTHEW_URL: "",        // Matthew's profile (the Sessions post from here)
  BRIEF_SUBSCRIBE_URL: "",         // The Board-Ready Brief subscribe link
  CALENDAR_URL: "",                // a booking link if you want one; otherwise email
  FORM_ENDPOINT_TRY: "",           // Formspree / Tally / Apps Script endpoint for the Try-it-first form (POST)
  FORM_ENDPOINT_SETUP: "",         // endpoint for the Setup Questionnaire (POST)
  CONTACT_EMAIL: "info@engermansolutions.com"
};
document.addEventListener("DOMContentLoaded", function () {
  var c = window.ES_CONFIG, mail = "mailto:" + c.CONTACT_EMAIL;
  document.querySelectorAll("[data-link]").forEach(function (a) {
    var key = a.getAttribute("data-link"), url = c[key];
    if (url) { a.href = url; a.target = "_blank"; a.rel = "noopener"; }
    else { a.href = mail + "?subject=" + encodeURIComponent(a.getAttribute("data-subject") || "Engerman Solutions"); }
  });
});

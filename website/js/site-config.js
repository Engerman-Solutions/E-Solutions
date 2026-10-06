// Engerman Solutions — one place for the links and endpoints the pages use.
// Fill these in once; every page reads them. Anything left blank falls back to email so nothing on the site is a dead link.
window.ES_CONFIG = {
  LINKEDIN_COMPANY_URL: "",        // e.g. https://www.linkedin.com/company/engerman-solutions
  LINKEDIN_MATTHEW_URL: "https://www.linkedin.com/in/matthew-a-engerman-25b17a46",
  BRIEF_SUBSCRIBE_URL: "https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7477941237455491072",
  CALENDAR_URL: "",                // a booking link if you want one; otherwise email
  TRY_FORM_URL: "https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=TCp6pTf0lUWjidw_pJ41r8VK0JU18xlOmM5bOtgsLdhUQVZLRjI1NVYzUE5CU0M4R0RRSDFNWTZZVi4u", // the Microsoft Form behind "Try it first" (embedded on forms/try-it-first.html; this link opens it in its own window)
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
});

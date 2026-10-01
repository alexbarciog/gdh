/* GDH — interactiunile site-ului.
 *
 * Fara dependinte: nici GSAP, nici Lenis, nici jQuery. Limbajul vizual nou nu
 * are nevoie de ele, iar asta scoate ~136 KB de JavaScript din fiecare pagina.
 */
(function () {
  "use strict";

  var $ = function (sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  };
  var mqDesktop = window.matchMedia("(min-width: 1081px)");

  /* Safari sub 14 nu are addEventListener pe MediaQueryList, doar addListener.
   * Fara verificarea asta exceptia oprea tot boot()-ul, iar pagina ramanea fara
   * acordeon, fara formular si — inainte de scaparea din CSS — fara continut. */
  function onDesktopChange(fn) {
    if (typeof mqDesktop.addEventListener === "function") {
      mqDesktop.addEventListener("change", fn);
    } else if (typeof mqDesktop.addListener === "function") {
      mqDesktop.addListener(fn);
    }
  }

  /* ------------------------------------------------------------ mega-meniu */
  function initMega() {
    var header = document.getElementById("gdh-header");
    if (!header) return;
    var triggers = $(".nav__link[data-mega]", header);
    if (!triggers.length) return;
    var openOne = null;
    var closeTimer = null;

    var chrome = document.getElementById("gdh-chrome");

    function close() {
      if (!openOne) return;
      var panel = document.getElementById(openOne.getAttribute("data-mega"));
      if (panel) panel.classList.remove("is-open");
      openOne.setAttribute("aria-expanded", "false");
      openOne = null;
      if (chrome) chrome.classList.remove("mega-open");
    }
    function open(trigger) {
      if (openOne === trigger) return;
      close();
      var panel = document.getElementById(trigger.getAttribute("data-mega"));
      if (!panel) return;
      panel.classList.add("is-open");
      trigger.setAttribute("aria-expanded", "true");
      openOne = trigger;
      // cat timp panoul e deschis, antetul sta peste gradient
      if (chrome) chrome.classList.add("mega-open");
    }
    function hold() { window.clearTimeout(closeTimer); }
    function release() { closeTimer = window.setTimeout(close, 180); }

    triggers.forEach(function (trigger) {
      var panel = document.getElementById(trigger.getAttribute("data-mega"));

      trigger.addEventListener("mouseenter", function () {
        if (mqDesktop.matches) { hold(); open(trigger); }
      });
      trigger.addEventListener("mouseleave", release);
      if (panel) {
        panel.addEventListener("mouseenter", hold);
        panel.addEventListener("mouseleave", release);
      }
      // la tastatura nu exista hover: prima apasare deschide, a doua navigheaza
      trigger.addEventListener("click", function (e) {
        if (!mqDesktop.matches) return;
        if (openOne !== trigger) { e.preventDefault(); open(trigger); }
      });
      trigger.addEventListener("focus", function () {
        if (mqDesktop.matches) { hold(); open(trigger); }
      });
      // focusul intrat in panou il tine deschis, ca sa se poata tabula prin el
      if (panel) {
        panel.addEventListener("focusin", hold);
        var shut = panel.querySelector(".mega__close");
        if (shut) shut.addEventListener("click", function () {
          trigger.focus();
          close();
        });
      }
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && openOne) { openOne.focus(); close(); }
    });
    onDesktopChange(close);
    document.addEventListener("click", function (e) {
      if (!openOne) return;
      if (header.contains(e.target)) return;
      close();
    });
    // focusul plecat cu totul din antet inchide panoul
    header.addEventListener("focusout", function (e) {
      if (!openOne) return;
      if (!e.relatedTarget || !header.contains(e.relatedTarget)) close();
    });
  }

  /* --------------------------------------------------------- meniu telefon */
  function initDrawer() {
    var burger = document.querySelector(".burger");
    var drawer = document.getElementById("gdh-drawer");
    if (!burger || !drawer) return;

    function set(open) {
      drawer.classList.toggle("is-open", open);
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.documentElement.classList.toggle("nav-open", open);
    }
    burger.addEventListener("click", function () {
      set(burger.getAttribute("aria-expanded") !== "true");
    });
    drawer.addEventListener("click", function (e) {
      if (e.target.closest("a")) set(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") set(false);
    });
    onDesktopChange(function (e) { if (e.matches) set(false); });

    $(".drawer__top", drawer).forEach(function (top) {
      if (top.tagName !== "BUTTON") return;
      var panel = top.nextElementSibling;
      top.addEventListener("click", function () {
        var open = top.getAttribute("aria-expanded") !== "true";
        top.setAttribute("aria-expanded", open ? "true" : "false");
        if (panel) panel.classList.toggle("is-open", open);
        var sign = top.querySelector(".topics__arrow");
        if (sign) sign.textContent = open ? "–" : "+";
      });
    });
  }

  /* -------------------------------------------------------------- acordeon */
  function initAccordion() {
    $(".acc").forEach(function (acc) {
      var items = $(".acc__item", acc);
      items.forEach(function (item, i) {
        var top = item.querySelector(".acc__top");
        var panel = item.querySelector(".acc__panel");
        if (!top || !panel) return;

        function set(open) {
          item.classList.toggle("is-open", open);
          top.setAttribute("aria-expanded", open ? "true" : "false");
          if (open) panel.hidden = false;
          // inaltimea masurata se foloseste doar pentru animatie; dupa ea
          // panoul trece pe auto, ca sa nu taie textul daca fontul se schimba
          panel.style.height = open ? panel.scrollHeight + "px" : "0px";
          if (!open) {
            window.setTimeout(function () {
              if (!item.classList.contains("is-open")) panel.hidden = true;
            }, 320);
          }
        }
        top.addEventListener("click", function () {
          var open = !item.classList.contains("is-open");
          items.forEach(function (other) {
            if (other === item) return;
            other.classList.remove("is-open");
            var ot = other.querySelector(".acc__top");
            var op = other.querySelector(".acc__panel");
            if (ot) ot.setAttribute("aria-expanded", "false");
            if (op) op.style.height = "0px";
          });
          set(open);
        });
        if (i === 0) {
          item.classList.add("is-open");
          top.setAttribute("aria-expanded", "true");
          panel.hidden = false;
          panel.style.height = "auto";
        } else {
          panel.hidden = true;
        }
        window.addEventListener("resize", function () {
          if (item.classList.contains("is-open")) panel.style.height = panel.scrollHeight + "px";
        });
      });
    });
  }

  /* ------------------------------------------------------------- aparitii */
  function initReveal() {
    var targets = $("[data-reveal]");
    if (!targets.length) return;
    if (!("IntersectionObserver" in window)) {
      targets.forEach(function (el) { el.classList.add("is-in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        io.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0 });
    targets.forEach(function (el) { io.observe(el); });

    /* Plasa de siguranta: daca observatorul nu apuca sa anunte un element —
     * fila deschisa in fundal, o incarcare intrerupta — bucata aia de pagina ar
     * ramane invizibila pentru totdeauna. */
    var rounds = 0;
    var guard = window.setInterval(function () {
      var left = $("[data-reveal]:not(.is-in)");
      // dupa doua minute orice element ramas e pur si simplu sub ecran
      if (!left.length || ++rounds > 100) { window.clearInterval(guard); return; }
      left.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight + 200 && r.bottom > -200) {
          el.classList.add("is-in");
          io.unobserve(el);
        }
      });
    }, 1200);
  }

  /* -------------------------------------------------------------- formular */
  function initForms() {
    $("form[data-gdh-form]").forEach(function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var lines = [];
        new FormData(form).forEach(function (value, key) {
          if (String(value).trim()) lines.push(key + ": " + value);
        });
        window.location.href = "mailto:office@gdh-group.com?subject="
          + encodeURIComponent(form.getAttribute("data-subject") || "Enquiry")
          + "&body=" + encodeURIComponent(lines.join("\n"));
      });
    });
  }

  /* ------------------------------------------------------------- antet */
  function initChrome() {
    var chrome = document.getElementById("gdh-chrome");
    if (!chrome) return;

    function measure() {
      // sertarul de telefon porneste exact sub antet, oricat ar fi de inalt
      document.documentElement.style.setProperty(
        "--chrome-h", chrome.getBoundingClientRect().height + "px");
    }
    var ticking = false;
    function onScroll() {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        chrome.classList.toggle("is-scrolled", window.scrollY > 24);
        ticking = false;
      });
    }
    measure();
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", measure);
  }

  function boot() {
    // de aici incolo CSS-ul are voie sa ascunda sectiunile pentru aparitii
    document.documentElement.classList.add("js");
    [initChrome, initMega, initDrawer, initAccordion, initReveal, initForms]
      .forEach(function (fn) {
        // o parte stricata nu mai duce la o pagina goala
        try { fn(); } catch (e) { if (window.console) console.error(e); }
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();

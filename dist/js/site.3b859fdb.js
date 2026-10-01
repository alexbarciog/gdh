/* GDH — Global Distribution Holdings
 * Interactiunile site-ului, scrise de la zero. Fara jQuery, fara dependinte.
 */
(function () {
  "use strict";

  /* ---------------------------------------------------------- meniu mobil */
  function initNav() {
    document.querySelectorAll(".g-nav, .navbar").forEach(function (nav) {
      var btn = nav.querySelector(".menu-button");
      var menu = nav.querySelector(".nav-menu, .g-nav-menu");
      if (!btn || !menu) return;

      var open = false;
      function set(state) {
        open = state;
        nav.classList.toggle("is-open", open);
        menu.classList.toggle("is-open", open);
        btn.classList.toggle("is-open", open);
        btn.setAttribute("aria-expanded", open ? "true" : "false");
        document.documentElement.classList.toggle("gdh-nav-open", open);
      }
      btn.setAttribute("aria-expanded", "false");
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        set(!open);
      });
      btn.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          set(!open);
        }
      });
      menu.addEventListener("click", function (e) {
        if (e.target.closest("a")) set(false);
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && open) set(false);
      });
      // un tap în afara panoului îl închide, ca la orice meniu de telefon
      document.addEventListener("click", function (e) {
        if (!open) return;
        if (menu.contains(e.target) || btn.contains(e.target)) return;
        set(false);
      });
      window.addEventListener("resize", function () {
        if (window.innerWidth > 991 && open) set(false);
      });
    });
  }

  /* -------------------------------------------------------------- slidere */
  function initSliders() {
    document.querySelectorAll(".gdh-slider").forEach(function (slider) {
      var mask = slider.querySelector(".g-slider-mask");
      if (!mask) return;
      var slides = Array.prototype.slice.call(mask.querySelectorAll(".g-slide"));
      if (slides.length < 2) return;

      var dots = Array.prototype.slice.call(slider.querySelectorAll(".g-slider-dot"));
      var prev = slider.querySelector(".g-slider-arrow-left");
      var next = slider.querySelector(".g-slider-arrow-right");
      var index = 0;
      var timer = null;

      function render() {
        slides.forEach(function (s, i) {
          s.style.transform = "translateX(" + -index * 100 + "%)";
          s.setAttribute("aria-hidden", i === index ? "false" : "true");
        });
        dots.forEach(function (d, i) {
          d.classList.toggle("g-active", i === index);
          d.classList.toggle("is-active", i === index);
          d.setAttribute("aria-pressed", i === index ? "true" : "false");
          d.tabIndex = i === index ? 0 : -1;
        });
      }
      function go(i) {
        index = (i + slides.length) % slides.length;
        render();
      }
      if (prev) prev.addEventListener("click", function () { go(index - 1); restart(); });
      if (next) next.addEventListener("click", function () { go(index + 1); restart(); });
      dots.forEach(function (d, i) {
        d.addEventListener("click", function () { go(i); restart(); });
      });

      /* swipe pe touch */
      var x0 = null;
      mask.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
      mask.addEventListener("touchend", function (e) {
        if (x0 === null) return;
        var dx = e.changedTouches[0].clientX - x0;
        if (Math.abs(dx) > 45) { go(index + (dx < 0 ? 1 : -1)); restart(); }
        x0 = null;
      });

      var auto = slider.classList.contains("industries-slider-main");
      function restart() {
        if (!auto) return;
        window.clearInterval(timer);
        timer = window.setInterval(function () { go(index + 1); }, 6000);
      }
      slides.forEach(function (s) {
        s.style.transition = "transform .55s cubic-bezier(.22,.61,.36,1)";
      });
      render();
      restart();
    });
  }

  /* ------------------------------------------------------------------ FAQ */
  function initFaq() {
    var cards = document.querySelectorAll(".faq-card");
    cards.forEach(function (card, i) {
      var top = card.querySelector(".faq-top");
      var body = card.querySelector(".faq-bottom");
      if (!top || !body) return;

      body.classList.add("faq-answer");
      body.style.height = "0px";
      top.setAttribute("role", "button");
      top.setAttribute("tabindex", "0");
      top.setAttribute("aria-expanded", "false");

      function set(open) {
        card.classList.toggle("is-open", open);
        top.setAttribute("aria-expanded", open ? "true" : "false");
        body.style.height = open ? body.scrollHeight + "px" : "0px";
        card.dispatchEvent(new CustomEvent("gdh:faq", { detail: open }));
      }
      function toggle() {
        var open = !card.classList.contains("is-open");
        cards.forEach(function (other) {
          if (other !== card && other.classList.contains("is-open")) {
            other.classList.remove("is-open");
            var ob = other.querySelector(".faq-bottom");
            var ot = other.querySelector(".faq-top");
            if (ob) ob.style.height = "0px";
            if (ot) ot.setAttribute("aria-expanded", "false");
          }
        });
        set(open);
      }
      top.addEventListener("click", toggle);
      top.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(); }
      });
      if (i === 0) window.setTimeout(function () { set(true); }, 120);
      window.addEventListener("resize", function () {
        if (card.classList.contains("is-open")) body.style.height = body.scrollHeight + "px";
      });
    });
  }

  /* --------------------------------------------------------- formulare */
  function initForms() {
    document.querySelectorAll("form[data-gdh-form]").forEach(function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var data = new FormData(form);
        var lines = [];
        data.forEach(function (value, key) {
          if (String(value).trim()) lines.push(key + ": " + value);
        });
        var subject = form.classList.contains("newsletter-form")
          ? "Newsletter signup"
          : "Distribution enquiry";
        window.location.href =
          "mailto:office@gdh-group.com?subject=" + encodeURIComponent(subject) +
          "&body=" + encodeURIComponent(lines.join("\n"));
        var done = form.parentElement && form.parentElement.querySelector(".g-form-done, .success-message");
        if (done) {
          form.style.display = "none";
          done.style.display = "block";
        }
      });
    });
  }

  /* ------------------------------------------------------ scroll lin */
  function initLenis() {
    if (typeof window.Lenis !== "function") return;
    var lenis = new window.Lenis({
      duration: 1.4,
      easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      smoothWheel: true,
      smoothTouch: false
    });
    window.gdhLenis = lenis;
    // daca GSAP e prezent, animations.js il pune pe ticker-ul lui gsap
    if (typeof window.gsap !== "undefined") return;
    function raf(time) {
      lenis.raf(time);
      window.requestAnimationFrame(raf);
    }
    window.requestAnimationFrame(raf);
  }

  function boot() {
    initNav();
    initSliders();
    initFaq();
    initForms();
    initLenis();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();

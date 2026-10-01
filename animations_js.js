/* GDH — animațiile site-ului.
 *
 * Reconstruite 1:1 după starea reală măsurată în pagina-sursă: aceleași procente
 * de deplasare, aceleași despicări de text, același odometru. Nu mai există niciun
 * motor de interacțiuni străin — doar GSAP, servit local, cu timeline-urile scrise
 * explicit aici.
 */
(function () {
  "use strict";

  if (typeof window.gsap === "undefined") return;
  // Pagina-sursa rula animatiile indiferent de setarea de sistem, iar multe masini
  // au "reduced motion" pornit fara ca utilizatorul sa stie; le pastram pornite ca
  // site-ul sa arate la fel peste tot.

  gsap.registerPlugin(window.ScrollTrigger);
  var hasSplit = typeof window.SplitText !== "undefined";
  if (hasSplit) gsap.registerPlugin(window.SplitText);

  var $ = function (sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  };

  /* ------------------------------------------------------------------
   * 1. Titluri despicate în cuvinte / rânduri, care se aprind la scroll
   * ---------------------------------------------------------------- */
  var SPLIT_WORDS = [
    "h1.hero-heading",
    "h2.section-heading",
    ".about-rebuild-text",
    ".card-number"
  ];
  var SPLIT_LINES = [
    "p.home-hero-p",
    ".track-list",
    ".footer-left-bottom",
    ".footer-right-bottom"
  ];

  function splitReveal(selectors, type) {
    selectors.forEach(function (sel) {
      $(sel).forEach(function (el) {
        if (el.dataset.gdhSplit) return;
        el.dataset.gdhSplit = "1";

        var lines = type === "lines";
        var pieces;
        if (hasSplit) {
          var split = new SplitText(el, {
            type: lines ? "lines" : "words",
            mask: lines ? "lines" : undefined,
            linesClass: "gdh-split-line",
            wordsClass: "gdh-split-word"
          });
          pieces = lines ? split.lines : split.words;
        } else {
          pieces = [el];
        }
        if (!pieces.length) return;

        // Ce se vede din prima nu are cum să se aprindă la scroll: acele blocuri
        // intră la încărcarea paginii, exact ca în pagina-sursă.
        if (el.getBoundingClientRect().top < window.innerHeight * 0.9) {
          gsap.fromTo(pieces,
            { opacity: 0, yPercent: lines ? 110 : 40 },
            {
              opacity: 1, yPercent: 0, duration: 1, ease: "power3.out",
              stagger: lines ? 0.12 : 0.045, delay: 0.15, clearProps: "transform"
            });
          return;
        }

        gsap.fromTo(pieces,
          { opacity: 0.08 },
          {
            opacity: 1,
            duration: 1,
            ease: "power1.out",
            stagger: { each: 0.3 },
            scrollTrigger: {
              trigger: el,
              start: "clamp(top bottom)",
              end: "clamp(bottom 55%)",
              scrub: 0.8
            }
          });
      });
    });
  }

  /* ------------------------------------------------------------------
   * 2. Intrări: opacitate 0 + deplasare pe verticală, procentele originale
   * ---------------------------------------------------------------- */
  var ENTER = [
    [".faq-card", 100], [".faq-button-wrap", 100], [".blog-button-wrap", 100],
    [".footer-bottom", 100], [".papragraph-regular.center-mobile", 100],
    [".project-card", 60], [".footer-left-top", 50], [".testimonial-card-main", 35],
    [".blog-card-v1", 40], [".footer-menu-left", 40], [".pricing-card", 30],
    [".industries-main", 20], [".journey-info-card", 24], ["._w-chose-card", 24],
    [".stats-card", 24], [".about-card", 20], [".service-card", 24],
    [".contact-form-block", 24], [".inner-prose > div", 18]
  ];

  /* Un IntersectionObserver, nu ScrollTrigger: pozițiile de start ale ScrollTrigger
   * se calculează o singură dată și rămân în urmă când imaginile schimbă înălțimea
   * paginii — observatorul se uită mereu la starea reală. */
  function entrances() {
    if (!("IntersectionObserver" in window)) return;
    var queue = [];
    var flush = null;

    function reveal(batch) {
      batch.forEach(function (el) { el.dataset.gdhEnter = "2"; });
      gsap.to(batch, {
        opacity: 1,
        yPercent: 0,
        duration: 1.1,
        ease: "power3.out",
        stagger: 0.08,
        clearProps: "transform"
      });
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        io.unobserve(entry.target);
        queue.push(entry.target);
      });
      if (!queue.length || flush) return;
      flush = window.setTimeout(function () {
        var batch = queue.slice();
        queue.length = 0;
        flush = null;
        reveal(batch);
      }, 60);
      // fără margine negativă: un element lipit de subsolul paginii nu ar apuca
      // niciodată să treacă de un prag decalat în sus
    }, { rootMargin: "0px", threshold: 0 });

    ENTER.forEach(function (pair) {
      $(pair[0]).forEach(function (el) {
        if (el.dataset.gdhEnter) return;
        // slide-urile din afara ecranului nu intra niciodata in raza observatorului
        if (el.closest(".g-slider-mask")) return;
        el.dataset.gdhEnter = "1";
        gsap.set(el, { opacity: 0, yPercent: pair[1] });
        io.observe(el);
      });
    });

    /* Plasa de siguranta. Intrarile pleaca de la opacity 0 si se aprind doar
     * cand observatorul le anunta. Daca anuntul nu vine — fila deschisa in
     * fundal, o incarcare intrerupta, un element mutat de alt script — bucata
     * aia de pagina ramane invizibila pentru totdeauna, si pare ca site-ul
     * taie continutul. Deci verificam periodic si aprindem orice a ajuns in
     * dreptul ecranului si inca n-a fost aprins. */
    var guard = window.setInterval(function () {
      var pending = $("[data-gdh-enter='1']");
      if (!pending.length) {
        window.clearInterval(guard);
        return;
      }
      var stuck = pending.filter(function (el) {
        var r = el.getBoundingClientRect();
        return r.top < window.innerHeight + 200 && r.bottom > -200;
      });
      if (stuck.length) {
        stuck.forEach(function (el) { io.unobserve(el); });
        reveal(stuck);
      }
    }, 1200);
  }

  /* ------------------------------------------------------------------
   * 3. Benzile care curg la infinit (logo-uri, cardurile de proces)
   * ---------------------------------------------------------------- */
  function marquees() {
    [[".marque-list-wrap", ".marque-list", 34], [".process-list-wrapper", ".proecess-list", 46]]
      .forEach(function (cfg) {
        $(cfg[0]).forEach(function (wrap) {
          var lists = $(cfg[1], wrap);
          if (lists.length < 2) return;
          gsap.set(lists, { xPercent: 0 });
          gsap.to(lists, {
            xPercent: -100,
            duration: cfg[2],
            ease: "none",
            repeat: -1,
            modifiers: {
              // xPercent vrea un numar; un sir cu "%" opreste tween-ul in loc
              xPercent: function (v) { return gsap.utils.wrap(-100, 0, parseFloat(v)); }
            }
          });
        });
      });
  }

  /* ------------------------------------------------------------------
   * 4. Mișcări legate de scroll: paralax, rotații, linii care cresc
   * ---------------------------------------------------------------- */
  function scrubbed() {
    // imagini cu paralax ușor
    [".about-img", ".journey-img", ".industries-card-img", ".blog-card-img-v1",
     ".track-img", ".process-img", ".world-img"].forEach(function (sel) {
      $(sel).forEach(function (img) {
        gsap.fromTo(img, { yPercent: -6 }, {
          yPercent: 6, ease: "none",
          scrollTrigger: { trigger: img.parentElement || img, start: "top bottom", end: "bottom top", scrub: true }
        });
      });
    });

    // globul din secțiunea de proces se rotește pe măsură ce derulezi
    $(".process-world-img").forEach(function (el) {
      gsap.fromTo(el, { rotate: 0 }, {
        rotate: 180, ease: "none",
        scrollTrigger: { trigger: el.closest("section") || el, start: "top bottom", end: "bottom top", scrub: true }
      });
    });

    // pastila din zona de statistici: se înclină și urcă
    $(".stats-pill").forEach(function (el) {
      gsap.fromTo(el, { rotate: -8, yPercent: 12 }, {
        rotate: 22, yPercent: -30, ease: "none",
        scrollTrigger: { trigger: el.closest("section") || el, start: "top bottom", end: "bottom top", scrub: true }
      });
    });

    // cercurile care se umflă (doar cele două pe care le anima si originalul)
    $(".circle._001, .circle._02").forEach(function (el) {
      gsap.fromTo(el, { scale: 0.35 }, {
        scale: 1, ease: "none",
        scrollTrigger: { trigger: el.closest("section") || el, start: "top bottom", end: "center center", scrub: true }
      });
    });

    // liniile roșii care se trag sub carduri
    $(".animated-line").forEach(function (el) {
      gsap.fromTo(el, { width: "0%" }, {
        width: "100%", duration: 1.2, ease: "power2.out",
        scrollTrigger: { trigger: el.parentElement || el, start: "top 88%", once: true }
      });
    });

    // cardurile de proces stau ușor înclinate, ca un teanc
    $(".process-card").forEach(function (card, i) {
      var tilt = card.classList.contains("_02") ? 5 : -5;
      gsap.set(card, { rotate: tilt });
      gsap.to(card, {
        rotate: 0, ease: "none",
        scrollTrigger: { trigger: card, start: "top bottom", end: "center 60%", scrub: true }
      });
    });
  }

  /* ------------------------------------------------------------------
   * 5. Contorul de tip odometru — se oprește exact pe 68,000+
   * ---------------------------------------------------------------- */
  var COUNTER_TARGET = { one: 0, two: -90, three: 0, six: -90, four: -30, five: -60 };

  function counters() {
    var cols = $(".counter-col");
    if (!cols.length) return;
    cols.forEach(function (col) {
      var wrap = col.firstElementChild;
      if (!wrap) return;
      var key = Array.prototype.find.call(wrap.classList, function (c) { return c in COUNTER_TARGET; });
      var target = key ? COUNTER_TARGET[key] : 0;
      gsap.set(wrap, { yPercent: target });
      gsap.from(wrap, {
        yPercent: target - 60,
        duration: 1.6,
        ease: "power3.out",
        scrollTrigger: { trigger: col, start: "top 90%", once: true }
      });
    });
  }

  /* ------------------------------------------------------------------
   * 6. Hover: pastilele de text și săgețile care se schimbă între ele
   * ---------------------------------------------------------------- */
  function hovers() {
    function pill(container, inner, prop, amount) {
      $(container).forEach(function (el) {
        var items = $(inner, el);
        if (items.length < 2) return;
        var vars = {};
        vars[prop] = amount;
        var enter = function () { gsap.to(items, Object.assign({ duration: 0.45, ease: "power3.out" }, vars)); };
        var leave = function () {
          var reset = {}; reset[prop] = 0;
          gsap.to(items, Object.assign({ duration: 0.45, ease: "power3.out" }, reset));
        };
        var host = el.closest("a, button") || el;
        host.addEventListener("mouseenter", enter);
        host.addEventListener("mouseleave", leave);
        host.addEventListener("focus", enter);
        host.addEventListener("blur", leave);
      });
    }
    pill(".button-text-pill", ".button-text", "yPercent", -100);
    pill(".button-arrow-pill", ".button-arrow", "xPercent", 100);
    pill(".footer-link", ".footer-text", "yPercent", -100);

    // fundalul roșu care urcă sub întrebările din FAQ
    $(".faq-card").forEach(function (card) {
      var fill = card.querySelector(".faq-animated-color");
      if (!fill) return;
      gsap.set(fill, { rotateX: 90, opacity: 0, transformOrigin: "50% 100%" });
      var show = function () { gsap.to(fill, { rotateX: 0, opacity: 1, duration: 0.5, ease: "power3.out" }); };
      var hide = function () {
        if (card.classList.contains("is-open")) return;
        gsap.to(fill, { rotateX: 90, opacity: 0, duration: 0.4, ease: "power3.in" });
      };
      card.addEventListener("mouseenter", show);
      card.addEventListener("mouseleave", hide);
      card.addEventListener("gdh:faq", function (e) { (e.detail ? show : hide)(); });
    });

    // imaginea care se deschide în cardul de proiect
    $(".project-card").forEach(function (card) {
      var box = card.querySelector(".project-image-wrap-main");
      if (!box) return;
      var img = box.firstElementChild;
      var full = img ? img.getBoundingClientRect().height || 260 : 260;
      gsap.set(box, { height: 0 });
      card.addEventListener("mouseenter", function () {
        gsap.to(box, { height: full || 260, duration: 0.55, ease: "power3.out" });
      });
      card.addEventListener("mouseleave", function () {
        gsap.to(box, { height: 0, duration: 0.45, ease: "power3.in" });
      });
    });

    // overlay-ul alb care mătură cardurile de recenzie
    $(".testimonial-overlay").forEach(function (ov) {
      gsap.set(ov, { width: "0%" });
    });
  }

  /* ------------------------------------------------------------------
   * 7. Intrarea de la încărcarea paginii (hero)
   * ---------------------------------------------------------------- */
  function heroIntro() {
    var bits = [".home-hero-img-wrap", ".home-hero-button-wrap", ".stats-header",
                ".section-button-wrap", ".about-badge"].reduce(function (acc, s) {
      return acc.concat($(s));
    }, []);
    if (!bits.length) return;
    gsap.from(bits, { opacity: 0, y: 26, duration: 1, ease: "power3.out", stagger: 0.08, delay: 0.15 });
  }

  /* ------------------------------------------------------------------
   * 8. Lenis + ScrollTrigger trebuie să bată în același ritm
   * ---------------------------------------------------------------- */
  function syncLenis() {
    if (!window.gdhLenis) return;
    window.gdhLenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add(function (time) { window.gdhLenis.raf(time * 1000); });
    gsap.ticker.lagSmoothing(0);
  }

  /* Plasă de siguranță: dacă un declanșator nu apucă să pornească (imagini care
   * schimbă înălțimea paginii, filă deschisă în fundal), nimic nu rămâne invizibil. */
  function safetyNet() {
    var check = function () {
      ENTER.forEach(function (pair) {
        $(pair[0]).forEach(function (el) {
          if (parseFloat(getComputedStyle(el).opacity) > 0.01) return;
          if (el.getBoundingClientRect().top > window.innerHeight) return;
          gsap.to(el, { opacity: 1, yPercent: 0, duration: 0.6, ease: "power2.out", clearProps: "transform" });
        });
      });
    };
    window.setTimeout(check, 2500);
    window.addEventListener("load", function () { window.setTimeout(check, 1200); });
  }

  function boot() {
    syncLenis();
    splitReveal(SPLIT_WORDS, "words");
    splitReveal(SPLIT_LINES, "lines");
    entrances();
    marquees();
    scrubbed();
    counters();
    hovers();
    heroIntro();
    safetyNet();
    ScrollTrigger.refresh();
    window.addEventListener("load", function () { ScrollTrigger.refresh(); });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();

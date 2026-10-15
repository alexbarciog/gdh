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
  var mqDesktop = window.matchMedia("(min-width: 1181px)");

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

  /* --------------------------------------------------------- meniul complet */
  function initDrawer() {
    var burger = document.querySelector(".burger");
    var drawer = document.getElementById("gdh-drawer");
    if (!burger || !drawer) return;
    var closeBtn = drawer.querySelector(".drawer__close");

    function isOpen() { return drawer.classList.contains("is-open"); }
    function set(open) {
      if (open === isOpen()) return;
      drawer.classList.toggle("is-open", open);
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.documentElement.classList.toggle("nav-open", open);
      if (open) {
        var first = drawer.querySelector(".drawer__list a");
        if (first) first.focus({ preventScroll: true });
      } else {
        burger.focus({ preventScroll: true });
      }
    }
    burger.addEventListener("click", function () { set(!isOpen()); });
    if (closeBtn) closeBtn.addEventListener("click", function () { set(false); });
    drawer.addEventListener("click", function (e) {
      // clic pe voalul din jurul panoului, sau pe o legatura din el
      if (e.target === drawer || e.target.closest("a")) set(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && isOpen()) set(false);
      // focusul ramane in panou cat timp e deschis
      if (e.key === "Tab" && isOpen()) {
        var f = $("a, button", drawer);
        if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  /* ------------------------------------------------- vitrina de servicii */
  function initServices() {
    $("[data-svc-root]").forEach(function (root) {
      var items = $(".svc__item", root);
      var imgs = $("[data-svc-img]", root);
      var label = root.querySelector("[data-svc-label]");
      function activate(i) {
        items.forEach(function (it, k) {
          var on = k === i;
          it.classList.toggle("is-active", on);
          var head = it.querySelector(".svc__head");
          if (head) head.setAttribute("aria-expanded", on ? "true" : "false");
        });
        imgs.forEach(function (im, k) { im.classList.toggle("is-on", k === i); });
        if (label) {
          var head = items[i].querySelector(".svc__head");
          label.textContent = ("0" + (i + 1)).slice(-2) + " " + (head ? head.textContent : "");
          scramble(label);
        }
      }
      items.forEach(function (it, i) {
        var head = it.querySelector(".svc__head");
        if (!head) return;
        head.addEventListener("click", function () { activate(i); });
        head.addEventListener("focus", function () { activate(i); });
        it.addEventListener("mouseenter", function () {
          if (mqDesktop.matches) activate(i);
        });
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
    var over = chrome.classList.contains("chrome--over");
    var hero = document.querySelector(".hero");
    var lastY = window.scrollY;

    function measure() {
      document.documentElement.style.setProperty(
        "--chrome-h", chrome.getBoundingClientRect().height + "px");
    }
    var ticking = false;
    function onScroll() {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        var y = window.scrollY;
        // peste banner antetul ramane transparent; dupa el devine alb mat
        var limit = over && hero ? hero.offsetHeight - chrome.offsetHeight : 24;
        chrome.classList.toggle("is-scrolled", y > limit);
        // se ascunde la coborare si revine la urcare; nu cat timp un panou e deschis
        var down = y > lastY && y > 320;
        if (!chrome.classList.contains("mega-open")) chrome.classList.toggle("is-hidden", down);
        lastY = y;
        ticking = false;
      });
    }
    measure();
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", measure);
    // focusul de tastatura in antet il aduce inapoi
    chrome.addEventListener("focusin", function () { chrome.classList.remove("is-hidden"); });
  }

  /* --------------------------------------------- titluri care urca + cuvinte */
  function initRise() {
    var targets = $("[data-rise]");
    if (!targets.length) return;
    if (!("IntersectionObserver" in window)) {
      targets.forEach(function (el) { el.classList.add("is-risen"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-risen");
        io.unobserve(entry.target);
      });
    }, { threshold: 0.1 });
    targets.forEach(function (el) { io.observe(el); });
    // plasa de siguranta, ca la aparitii: nimic nu ramane ascuns
    window.setTimeout(function () {
      targets.forEach(function (el) {
        if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add("is-risen");
      });
    }, 1500);
  }

  function initWords() {
    var blocks = $("[data-words]");
    if (!blocks.length) return;
    var sets = blocks.map(function (block) {
      // fiecare cuvant intra in propriul <span>, fara sa strice <strong>
      var walker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT);
      var nodes = [];
      while (walker.nextNode()) nodes.push(walker.currentNode);
      nodes.forEach(function (node) {
        var frag = document.createDocumentFragment();
        node.textContent.split(/(\s+)/).forEach(function (part) {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
          var w = document.createElement("span");
          w.className = "w";
          w.textContent = part;
          frag.appendChild(w);
        });
        node.parentNode.replaceChild(frag, node);
      });
      return { block: block, words: $(".w", block) };
    });
    var ticking = false;
    function paint() {
      ticking = false;
      var vh = window.innerHeight;
      sets.forEach(function (set) {
        var r = set.block.getBoundingClientRect();
        var p = (vh * 0.85 - r.top) / (r.height + vh * 0.3);
        p = Math.max(0, Math.min(1, p));
        var lit = Math.round(p * set.words.length);
        set.words.forEach(function (w, i) { w.classList.toggle("is-lit", i < lit); });
      });
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; window.requestAnimationFrame(paint); }
    }, { passive: true });
    window.addEventListener("resize", paint);
    paint();
  }

  /* ------------------------------------------------------------- ceasul */
  function initClock() {
    var clocks = $("[data-clock]");
    if (!clocks.length || !window.Intl) return;
    function tick() {
      var now = new Date();
      clocks.forEach(function (el) {
        var tz = el.getAttribute("data-tz") || undefined;
        try {
          var time = new Intl.DateTimeFormat("en-GB", { hour: "numeric", minute: "2-digit",
            hour12: true, timeZone: tz }).format(now).toUpperCase();
          var day = new Intl.DateTimeFormat("en-GB", { day: "numeric", month: "short",
            year: "numeric", timeZone: tz }).formatToParts(now);
          var get = function (t) {
            for (var i = 0; i < day.length; i++) if (day[i].type === t) return day[i].value;
            return "";
          };
          el.innerHTML = time + '<span class="dot" aria-hidden="true"></span>'
            + get("day") + " " + get("month") + ", " + get("year");
          el.setAttribute("datetime", now.toISOString());
        } catch (e) { /* fus orar necunoscut: ramane gol */ }
      });
    }
    tick();
    window.setInterval(tick, 30000);
  }

  /* ------------------------------------------------------------- video */
  function initVideo() {
    var still = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var all = $("video");
    if (still) {
      // miscare redusa: ramane afisul, fara redare
      all.forEach(function (v) { v.removeAttribute("autoplay"); v.pause(); });
      return;
    }
    var lazy = $("video[data-lazy-video]");
    if (!lazy.length || !("IntersectionObserver" in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var v = entry.target;
        if (entry.isIntersecting) {
          v.preload = "auto";
          var p = v.play();
          if (p && p.catch) p.catch(function () {});
        } else {
          v.pause();
        }
      });
    }, { rootMargin: "200px 0px" });
    lazy.forEach(function (v) { io.observe(v); });
  }

  /* ============================================================ miscare
   * Intrarile pe componente si efectele legate de derulare. Totul porneste de
   * la continut vizibil: clasele care ascund se pun doar aici, doar daca
   * utilizatorul nu a cerut miscare redusa, iar o plasa de siguranta arata
   * orice a ramas ascuns. */
  var REDUCED = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* textul mono se „decodeaza”: literele aleatoare se aseaza pe rand */
  var GLYPHS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#/+";
  function scramble(el) {
    if (REDUCED || !el) return;
    var node = null;
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      if (walker.currentNode.textContent.trim()) { node = walker.currentNode; break; }
    }
    if (!node) return;
    var final = node.__final || node.textContent;
    node.__final = final;
    if (final.length > 48) return;
    window.cancelAnimationFrame(node.__raf);
    var start = null, dur = 520 + final.length * 18;
    function frame(t) {
      if (start === null) start = t;
      var p = Math.min(1, (t - start) / dur);
      var out = "";
      for (var i = 0; i < final.length; i++) {
        var ch = final[i];
        if (ch === " " || i < p * final.length) out += ch;
        else out += GLYPHS[(Math.random() * GLYPHS.length) | 0];
      }
      node.textContent = out;
      if (p < 1) node.__raf = window.requestAnimationFrame(frame);
      else node.textContent = final;
    }
    node.__raf = window.requestAnimationFrame(frame);
  }

  function initMotion() {
    // panourile de meniu: indexul fiecarei intrari, pentru cascada din CSS
    $(".drawer__panel, .mega").forEach(function (panel) {
      $(".drawer__list li, .drawer__aside, .mega__grid li, .mega__cta", panel)
        .forEach(function (el, i) { el.style.setProperty("--i", i); });
    });
    if (REDUCED || !("IntersectionObserver" in window)) return;

    var UP = [".hero__list-title", ".hero__side .lede", ".hero .btn-row", ".hero__info",
      ".pagehead__title > .eyebrow", ".pagehead__lede", ".pagehead__title .btn-row", ".crumbs",
      ".dcard",
      ".shead__title > .eyebrow", ".shead__side", ".lead-say__label", ".lead-say + .lead-say",
      ".split > div:not(.split__media)", ".contact-card", ".article > p", ".prose--two > div",
      ".statement__box", ".giant", ".marquee", ".cta__copy > .eyebrow", ".cta__text",
      ".cta .btn-row", ".footer__info", ".footer__legal", ".mega__top"];
    // containere: fiecare copil intra separat, in cascada
    var STAGGER = [".hero__list", ".grid", ".stats", ".facts", ".topics", ".related", ".acc",
      ".rows", ".steps", ".svc__list", ".footer__menus", ".features", ".process",
      ".drows", ".pcards", ".dcard__tags", ".dinfo", ".article"];
    var IMG = [".card__media", ".feature__media", ".split__media", ".pagehead__media",
      ".svc__media", ".duo__img"];
    var RISE = [".shead .h1", ".split .h1", ".cta__title", ".contact-card .h2", ".stat__value",
      ".mega__title", ".pagehead__fig", ".count"];
    var CODE = [".eyebrow", ".card__meta .chip", ".svc__label", ".feature__where", ".tile__num",
      ".stat__num", ".stat__label", ".footer h3", ".hero__where span:first-child",
      ".hero__list .n", ".step__num", ".card__tag", ".dcard__label", ".pcard__n",
      ".dinfo dt"];

    var targets = [];
    function mark(el, cls) {
      if (el.closest(".drawer")) return;
      if (!el.classList.contains(cls)) { el.classList.add(cls); targets.push(el); }
    }
    UP.forEach(function (sel) { $(sel).forEach(function (el) { mark(el, "m-up"); }); });
    STAGGER.forEach(function (sel) {
      $(sel).forEach(function (box) {
        Array.prototype.forEach.call(box.children, function (el) { mark(el, "m-up"); });
      });
    });
    IMG.forEach(function (sel) { $(sel).forEach(function (el) { mark(el, "m-img"); }); });
    RISE.forEach(function (sel) {
      $(sel).forEach(function (el) {
        if (el.hasAttribute("data-rise") || el.closest(".drawer")) return;
        el.innerHTML = '<span class="rise"><span>' + el.innerHTML + "</span></span>";
        el.setAttribute("data-rise", "");
      });
    });

    // cele care intra pe ecran in acelasi cadru primesc intarzieri crescatoare
    var io = new IntersectionObserver(function (entries) {
      var batch = entries.filter(function (e) { return e.isIntersecting; })
        .map(function (e) { return e.target; })
        .sort(function (a, b) {
          var ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
          return (ra.top - rb.top) || (ra.left - rb.left);
        });
      batch.forEach(function (el, i) {
        el.style.setProperty("--d", Math.min(i, 10) * 0.08 + "s");
        el.classList.add("is-in");
        io.unobserve(el);
        $(CODE.join(","), el).forEach(scramble);
        if (el.matches(CODE.join(","))) scramble(el);
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0 });
    targets.forEach(function (el) { io.observe(el); });

    // etichetele care nu sunt in niciun element animat se decodeaza singure
    var codeIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        codeIo.unobserve(e.target);
        if (!e.target.closest(".m-up, .m-img")) scramble(e.target);
      });
    }, { threshold: 0.5 });
    $(CODE.join(",")).forEach(function (el) { if (!el.closest(".drawer, .mega")) codeIo.observe(el); });

    // cifrele care numara (€100 -> €0 pe paginile de detaliu)
    var counts = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        counts.unobserve(e.target);
        countUp(e.target);
      });
    }, { threshold: 0.6 });
    $("[data-count-to]").forEach(function (el) {
      var span = el.querySelector(".rise > span") || el;
      span.textContent = (el.getAttribute("data-prefix") || "")
        + el.getAttribute("data-count-from") + (el.getAttribute("data-suffix") || "");
      counts.observe(el);
    });

    // crucea din „How it works”
    var lines = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("is-in"); lines.unobserve(e.target); }
      });
    }, { threshold: 0.25 });
    $(".process").forEach(function (el) { lines.observe(el); });

    // legaturile mono se decodeaza la hover
    $(".link-arrow, .svc__more, .related a, .tile").forEach(function (el) {
      var label = el.matches(".related a") ? el.querySelector(".related__go")
        : el.matches(".tile") ? el.querySelector(".tile__num") : el;
      el.addEventListener("mouseenter", function () { scramble(label); });
    });

    // plasa de siguranta: nimic nu ramane ascuns daca observatorul nu anunta
    window.setTimeout(function sweep() {
      var left = $(".m-up:not(.is-in), .m-img:not(.is-in)");
      left.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight && r.bottom > 0) el.classList.add("is-in");
      });
      if (left.length) window.setTimeout(sweep, 1500);
    }, 2500);

    initScrollFx();
    initMagnetic();
  }

  function countUp(el) {
    var span = el.querySelector(".rise > span") || el;
    var from = parseFloat(el.getAttribute("data-count-from")) || 0;
    var to = parseFloat(el.getAttribute("data-count-to")) || 0;
    var pre = el.getAttribute("data-prefix") || "", suf = el.getAttribute("data-suffix") || "";
    var start = null, dur = 1800;
    function frame(t) {
      if (start === null) start = t;
      var p = Math.min(1, (t - start) / dur);
      var eased = 1 - Math.pow(1 - p, 4);
      span.textContent = pre + Math.round(from + (to - from) * eased) + suf;
      if (p < 1) window.requestAnimationFrame(frame);
    }
    window.requestAnimationFrame(frame);
  }

  /* efectele legate de derulare: un singur cadru pe eveniment */
  function initScrollFx() {
    var hero = document.querySelector(".hero");
    var heroFade = hero ? $(".hero__side, .hero__info", hero) : [];
    var heroVideo = hero && hero.querySelector(".hero__media");
    var giants = $(".giant");
    var ctas = $(".cta__box");
    var heads = $(".pagehead__media");
    var para = $(".pagehead__media img, .split__media img, .feature__media img");
    var tracks = $(".marquee__track");
    var anims = [];
    tracks.forEach(function (t) {
      if (t.getAnimations) anims = anims.concat(t.getAnimations());
    });

    var lastY = window.scrollY, rate = 1, queued = false;
    function frame() {
      queued = false;
      var y = window.scrollY, vh = window.innerHeight;
      var v = y - lastY;
      lastY = y;

      // bannerul: video-ul ramane in urma (paralaxa) si se apropie; titlul nu
      // se misca, ca sa nu-si piarda amestecul „exclusion” cu video-ul
      if (hero && y < hero.offsetHeight + 50) {
        var k = Math.min(1, y / hero.offsetHeight);
        heroVideo.style.translate = y > 0 ? "0 " + (y * 0.45).toFixed(1) + "px" : "";
        heroVideo.style.scale = y > 0 ? (1 + k * 0.14).toFixed(4) : "";
        heroFade.forEach(function (el) {
          el.style.opacity = y > 0 ? Math.max(0, 1 - k * 1.6).toFixed(3) : "";
        });
      }
      giants.forEach(function (g) {
        var r = g.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        var p = (r.top + r.height / 2 - vh / 2) / vh;  // -1 .. 1
        var spans = g.children;
        if (spans[0]) spans[0].style.translate = (p * 7).toFixed(2) + "vw 0";
        if (spans[1]) spans[1].style.translate = (-p * 7).toFixed(2) + "vw 0";
      });
      ctas.forEach(function (box) {
        var r = box.getBoundingClientRect();
        if (r.top > vh || r.bottom < 0) return;
        var p = Math.max(0, Math.min(1, (vh - r.top) / (vh * 0.65)));
        box.style.scale = (0.9 + p * 0.1).toFixed(4);
        box.style.borderRadius = (32 - p * 24).toFixed(1) + "px";
      });
      heads.forEach(function (box) {
        var r = box.getBoundingClientRect();
        if (r.top > vh || r.bottom < 0) return;
        var p = Math.max(0, Math.min(1, (vh - r.top) / (vh * 0.75)));
        box.style.scale = (0.88 + p * 0.12).toFixed(4);
      });
      para.forEach(function (img) {
        var r = img.parentNode.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        var off = (r.top + r.height / 2 - vh / 2) / vh;
        img.style.translate = "0 " + (off * -r.height * 0.09).toFixed(1) + "px";
      });
      // banda curge mai repede cand derulezi, si in sensul derularii
      if (anims.length) {
        var target = Math.max(-7, Math.min(7, 1 + v * 0.22));
        if (v < -1) target = Math.min(-1, target);
        rate += (target - rate) * 0.12;
        if (Math.abs(rate) < 1 && v === 0) rate = rate < 0 ? -1 : 1;
        anims.forEach(function (a) { a.playbackRate = rate; });
        if (Math.abs(rate - (rate < 0 ? -1 : 1)) > 0.02) schedule();
      }
    }
    function schedule() {
      if (!queued) { queued = true; window.requestAnimationFrame(frame); }
    }
    window.addEventListener("scroll", schedule, { passive: true });
    window.addEventListener("resize", schedule);
    schedule();
  }

  /* butoanele se apleaca usor spre cursor */
  function initMagnetic() {
    if (!window.matchMedia("(hover: hover) and (pointer: fine)").matches) return;
    $(".btn, .burger").forEach(function (b) {
      b.addEventListener("mousemove", function (e) {
        var r = b.getBoundingClientRect();
        var dx = (e.clientX - r.left - r.width / 2) / r.width;
        var dy = (e.clientY - r.top - r.height / 2) / r.height;
        b.style.translate = (dx * 12).toFixed(1) + "px " + (dy * 8).toFixed(1) + "px";
      });
      b.addEventListener("mouseleave", function () { b.style.translate = ""; });
    });
  }

  function boot() {
    // de aici incolo CSS-ul are voie sa ascunda sectiunile pentru aparitii
    document.documentElement.classList.add("js");
    [initChrome, initMega, initDrawer, initServices, initAccordion, initReveal,
     initMotion, initRise, initWords, initClock, initVideo, initForms]
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

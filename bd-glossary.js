// Glossary: wrap the first occurrences of each term in the page body with a
// hover card linking to the glossary appendix.
//
// Runs only after MathJax has finished typesetting, so terms inside formulas
// are never touched. Every text node is scanned in document order and every
// occurrence inside a node is considered (not just the first), otherwise terms
// that sit after a common term would never get linked.
(function () {
  var MAX_PER_TERM = 1;
  var MAX_TOTAL = 28;
  var SKIP = /^(CODE|PRE|A|SCRIPT|STYLE|H1|H2|H3|H4|H5|H6|TEXTAREA|BUTTON)$/;

  function waitForMathJax() {
    if (!window.MathJax || !window.MathJax.startup || !window.MathJax.startup.promise) {
      return Promise.resolve();
    }
    return Promise.resolve(window.MathJax.startup.promise).catch(function () {});
  }

  function escapeRe(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function build(entries) {
    entries.sort(function (a, b) {
      return b.term.length - a.term.length;
    });
    var pattern = entries
      .map(function (e) {
        return escapeRe(e.term);
      })
      .join("|");
    var re = new RegExp("(?<![\\w-])(" + pattern + ")(?![\\w-])", "gi");
    var byKey = {};
    entries.forEach(function (e) {
      byKey[e.term.toLowerCase()] = e;
    });
    return { re: re, byKey: byKey };
  }

  function linkNode(node, matcher, state) {
    var text = node.nodeValue;
    if (!text) return;
    matcher.re.lastIndex = 0;
    if (!matcher.re.test(text)) return;
    matcher.re.lastIndex = 0;

    var frag = document.createDocumentFragment();
    var last = 0;
    var m;
    var wrote = false;
    while ((m = matcher.re.exec(text)) !== null) {
      var entry = matcher.byKey[m[0].toLowerCase()];
      if (!entry) continue;
      var left = state.budget[entry.id] || 0;
      if (left <= 0 || state.total >= MAX_TOTAL) continue;
      state.budget[entry.id] = left - 1;
      state.total += 1;
      if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      var a = document.createElement("a");
      a.className = "bd-gloss";
      a.href = state.root + "glossary.html#" + entry.id;
      a.setAttribute("data-brief", entry.brief);
      a.setAttribute("aria-label", entry.term + ": " + entry.brief);
      a.textContent = m[0];
      frag.appendChild(a);
      last = m.index + m[0].length;
      wrote = true;
    }
    if (!wrote) return;
    if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
    node.parentNode.replaceChild(frag, node);
  }

  function run(entries, state0) {
    var main = document.querySelector("#mdbook-content main") || document.querySelector("#content main") || document.querySelector("main");
    if (!main) return;
    if (/glossary\.html$/.test(window.location.pathname)) return;

    var matcher = build(entries);
    var budget = {};
    entries.forEach(function (e) {
      budget[e.id] = MAX_PER_TERM;
    });

    var state = {
      budget: budget,
      total: 0,
      root: window.path_to_root || "",
    };

    var walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        var el = node.parentElement;
        if (!el) return NodeFilter.FILTER_REJECT;
        if (SKIP.test(el.tagName)) return NodeFilter.FILTER_REJECT;
        if (el.closest("code, pre, a, .bd-gloss, mjx-container")) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      },
    });

    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (n) {
      linkNode(n, matcher, state);
    });
  }

  var state0 = { root: (typeof path_to_root !== "undefined" ? path_to_root : "") };

  waitForMathJax().then(function () {
    fetch(state0.root + "assets/glossary.json")
      .then(function (r) {
        return r.ok ? r.json() : [];
      })
      .catch(function () {
        return [];
      })
      .then(function (entries) {
        if (entries && entries.length) run(entries, state0);
      });
  });
})();

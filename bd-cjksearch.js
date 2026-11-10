// CJK search fallback.
//
// mdBook builds its search index with a tokenizer that keeps only ASCII word
// tokens, so Chinese text is not indexed at all and a CJK query returns
// nothing. The serialised index does hold the full text of every section
// though, so this script answers CJK queries by scanning that text directly
// and reusing mdBook's own result container. Latin queries are left alone.
(function () {
  var MAX_RESULTS = 25;
  var CJK = /[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\u3040-\u30ff\uac00-\ud7af]/;

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&#34;", "'": "&#39;" }[c];
    });
  }

  function root() {
    return typeof path_to_root !== "undefined" ? path_to_root : "";
  }

  // The serialised index sits under `index` (elasticlunr's blob), so the
  // document store is window.search.index.documentStore. Accept either shape.
  function store() {
    var s = window.search;
    if (!s) return null;
    var ds = s.documentStore || (s.index && s.index.documentStore);
    if (!ds || !ds.docs || !Object.keys(ds.docs).length) return null;
    return { docs: ds.docs, doc_urls: s.doc_urls || [] };
  }

  function count(hay, q) {
    var n = 0;
    var i = hay.indexOf(q);
    while (i !== -1) {
      n += 1;
      i = hay.indexOf(q, i + q.length);
    }
    return n;
  }

  function teaser(text, q) {
    var i = text.indexOf(q);
    if (i < 0) i = 0;
    var start = Math.max(0, i - 60);
    var end = Math.min(text.length, i + q.length + 110);
    var out =
      (start > 0 ? "…" : "") +
      text.slice(start, end).replace(/\s+/g, " ") +
      (end < text.length ? "…" : "");
    return esc(out).split(esc(q)).join("<mark>" + esc(q) + "</mark>");
  }

  function render(query) {
    var s = store();
    var results = document.getElementById("mdbook-searchresults");
    var outer = document.getElementById("mdbook-searchresults-outer");
    var header = document.getElementById("mdbook-searchresults-header");
    if (!s || !results) return false;

    var hits = [];
    var docs = s.docs;
    for (var id in docs) {
      if (!Object.prototype.hasOwnProperty.call(docs, id)) continue;
      var d = docs[id];
      var t = d.title || "";
      var b = d.body || "";
      var n = count(b, query) + count(t, query) * 6;
      if (n > 0) hits.push({ id: id, doc: d, n: n + (t.indexOf(query) >= 0 ? 5 : 0) });
    }
    hits.sort(function (a, b2) {
      return b2.n - a.n;
    });
    hits = hits.slice(0, MAX_RESULTS);

    while (results.firstChild) results.removeChild(results.firstChild);
    var urls = s.doc_urls;
    hits.forEach(function (h, idx) {
      var url = String(urls[h.id] || "").split("#");
      if (url.length === 1) url.push("");
      var mark = "?highlight=" + encodeURIComponent(query).replace(/'/g, "%27");
      var li = document.createElement("li");
      li.innerHTML =
        '<a href="' +
        root() +
        url[0] +
        mark +
        "#" +
        url[1] +
        '">' +
        (h.doc.breadcrumbs || h.doc.title || "") +
        "</a>" +
        '<span class="teaser">' +
        teaser(h.doc.body || "", query) +
        "</span>";
      results.appendChild(li);
    });

    if (header) {
      header.innerText = hits.length
        ? hits.length + (hits.length === 1 ? " result" : " results")
        : "No results found";
    }
    if (outer) outer.classList.remove("hidden");
    return true;
  }

  // mdBook loads its index lazily, on the first search interaction. Nudge its
  // own handler with a synthetic keyup so the index arrives, then render.
  function nudge(bar) {
    try {
      bar.dispatchEvent(new KeyboardEvent("keyup", { bubbles: true, key: "a" }));
    } catch (e) {
      /* ignore */
    }
  }

  function run(bar, query) {
    var deadline = Date.now() + 6000;
    var nudged = false;
    (function attempt() {
      setTimeout(function () {
        if (bar.value.trim() !== query) return;
        if (render(query)) return;
        var waited = Date.now();
        if (!nudged && waited > deadline - 4500) {
          nudged = true;
          nudge(bar);
        }
        if (waited < deadline) attempt();
      }, 120);
    })();
  }

  function handler(e) {
    var bar = e.target;
    if (!bar || bar.id !== "mdbook-searchbar") return;
    var q = bar.value.trim();
    if (!q || !CJK.test(q)) return;
    run(bar, q);
  }

  // Delegate on the document: mdBook re-parents the search bar when it
  // initialises, which drops listeners bound to the element itself.
  document.addEventListener("input", handler, false);
  document.addEventListener("keyup", handler, false);
  document.addEventListener("search", handler, false);
})();

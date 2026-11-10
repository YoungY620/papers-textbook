// Language switch for a multi-paper site.
//
// The English book is the site root; the Chinese book is the same tree one
// level down, under /zh/. mdBook tells us how deep the current page sits below
// its own book root through the global `path_to_root`, and the page's language
// through <html lang>, so the counterpart URL can be derived exactly instead
// of guessed.
(function () {
  function depth() {
    var r = typeof path_to_root !== "undefined" ? path_to_root : "";
    var m = r.match(/\.\.\//g);
    return m ? m.length : 0;
  }

  function isZh() {
    return (document.documentElement.lang || "").toLowerCase().indexOf("zh") === 0;
  }

  function parts() {
    return window.location.pathname.split("/");
  }

  function counterpart() {
    var k = depth();
    var p = parts();
    var take = k + 1;
    var bookRoot = p.slice(0, p.length - take).join("/") + "/";
    var tail = p.slice(p.length - take).join("/");
    var hash = window.location.hash || "";
    if (isZh()) {
      var siteRoot = bookRoot.replace(/zh\/$/, "");
      return siteRoot + tail + hash;
    }
    return bookRoot + "zh/" + tail + hash;
  }

  function mount() {
    var bar = document.getElementById("mdbook-menu-bar") || document.getElementById("menu-bar");
    if (!bar || document.getElementById("bd-lang-switch")) return;
    var zh = isZh();
    var wrap = document.createElement("div");
    wrap.id = "bd-lang-switch";
    var a = document.createElement("a");
    a.href = counterpart();
    a.textContent = zh ? "English" : "中文";
    a.title = zh ? "Read this book in English" : "阅读中文版";
    a.setAttribute("rel", "alternate");
    a.setAttribute("hreflang", zh ? "en" : "zh");
    wrap.appendChild(a);
    bar.insertBefore(wrap, bar.firstChild);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();

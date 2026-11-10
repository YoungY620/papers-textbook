#!/usr/bin/env python3
"""Turn protected math tokens back into MathJax delimiters in built HTML.

protect_math.py replaces every math span with an opaque token so the Markdown
pass cannot mangle it. This script runs *after* `mdbook build` and rewrites the
generated HTML (and the search index) with the original TeX, wrapped in
\(...\) / \[...\] so MathJax typesets it.

Usage: python3 restore_math.py <html-output-dir> [more dirs...]
"""
import sys
import os
import re
import json
import base64

TOKEN_RE = re.compile(r"MJXMATH([A-Za-z0-9+/]+)END")


def decode(match):
    b64 = match.group(1)
    b64 += "=" * (-len(b64) % 4)
    try:
        payload = json.loads(base64.b64decode(b64).decode("utf-8"))
    except Exception:
        return None
    return bool(payload.get("d")), str(payload.get("t", ""))


def html_escape(tex):
    return tex.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def html_replace(text):
    def sub(m):
        got = decode(m)
        if got is None:
            return m.group(0)
        display, tex = got
        body = html_escape(tex)
        if display:
            return f'<span class="bd-math-display">\\[{body}\\]</span>'
        return f'<span class="bd-math-inline">\\({body}\\)</span>'

    return TOKEN_RE.sub(sub, text)


def plain_tex_search(tex):
    """A rough plain-text form of the TeX, for the search index."""
    s = re.sub(r"\\([A-Za-z]+)", r"\1", tex)
    s = s.replace("\\", " ")
    s = re.sub(r"[{}]", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def json_string_escape(s):
    """Escape for embedding inside an existing JSON string literal."""
    return json.dumps(s)[1:-1]


def search_replace(text):
    """The search index is `JSON.parse('<json>')` — a single-quoted JS string.

    Values must therefore be escaped for *both* the JSON string and the JS
    string literal around it, or an apostrophe in a formula ends the literal
    and the whole index fails to parse.
    """
    def sub(m):
        got = decode(m)
        if got is None:
            return m.group(0)
        _display, tex = got
        return json_string_escape(plain_tex_search(tex)).replace("'", "\\'")

    return TOKEN_RE.sub(sub, text)


def main():
    roots = sys.argv[1:]
    if not roots:
        print("usage: restore_math.py <dir> [...]", file=sys.stderr)
        sys.exit(2)
    changed = 0
    for root in roots:
        for dirpath, _dirnames, filenames in os.walk(root):
            for name in filenames:
                path = os.path.join(dirpath, name)
                if name.endswith(".html"):
                    fn = html_replace
                elif name.startswith("searchindex") and name.endswith(".js"):
                    fn = search_replace
                else:
                    continue
                with open(path, "r", encoding="utf-8") as fh:
                    src = fh.read()
                out = fn(src)
                if out != src:
                    with open(path, "w", encoding="utf-8") as fh:
                        fh.write(out)
                    changed += 1
    print(f"restore_math: rewrote {changed} file(s)")


if __name__ == "__main__":
    main()

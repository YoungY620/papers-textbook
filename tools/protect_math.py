#!/usr/bin/env python3
"""mdBook preprocessor: protect TeX math from the Markdown parser.

mdBook renders Markdown with pulldown-cmark before MathJax ever runs, so the
Markdown pass eats characters that are significant in TeX:

    $\{0,1\}^*$      -> ${0,1}^*$        backslashes before punctuation dropped
    ${K}_{i}$        -> ${K}<em>{i}$     "_" after "}" becomes emphasis
    a &= b \\ c &= d -> a &= b \\ c ...  "\\" collapses to "\"
    \$5 in prose     -> $5               bare $ then confuses MathJax

This preprocessor replaces every math span with an opaque ASCII token that the
Markdown parser cannot touch. A matching post-build step (restore_math.py)
decodes the token back into the built HTML as \(...\) / \[...\] for MathJax.
"""
import sys
import json
import re
import base64

TOKEN_PREFIX = "MJXMATH"
TOKEN_SUFFIX = "END"

# Sentinel used while masking code regions so they are never scanned.
_SENTINEL = "\x00\x01"


def encode(display: bool, tex: str) -> str:
    payload = json.dumps({"d": bool(display), "t": tex}, ensure_ascii=False)
    b64 = base64.b64encode(payload.encode("utf-8")).decode("ascii").rstrip("=")
    # Standard base64 has no "_" or "-", so the token survives emphasis parsing.
    return f"{TOKEN_PREFIX}{b64}{TOKEN_SUFFIX}"


def mask_code(text):
    """Replace fenced code blocks and inline code spans with sentinels."""
    store = []

    def keep(m):
        store.append(m.group(0))
        return f"{_SENTINEL}{len(store) - 1}{_SENTINEL}"

    text = re.sub(
        r"^(?P<ind>[ ]{0,3})(?P<f>`{3,}|~{3,})[^\n]*\n.*?"
        r"^(?P=ind)(?P=f)[ \t]*$",
        keep,
        text,
        flags=re.M | re.S,
    )
    text = re.sub(r"(?P<t>`+)(?:(?!(?P=t))[^\n])+(?P=t)", keep, text)
    return text, store


def unmask_code(text, store):
    for i, s in enumerate(store):
        text = text.replace(f"{_SENTINEL}{i}{_SENTINEL}", s)
    return text


# Display math first, so "$$" is never mistaken for two inline delimiters.
_DISPLAY_PATTERNS = [
    re.compile(r"\$\$(?P<tex>.+?)\$\$", re.S),
    re.compile(r"\\\[(?P<tex>.+?)\\\]", re.S),
]
_INLINE_PATTERNS = [
    re.compile(r"\\\((?P<tex>.+?)\\\)", re.S),
    # "$" must not be escaped, must not start after a word char, must hug its
    # content, and must not be followed by a word char.
    re.compile(
        r"(?<![A-Za-z0-9\\$])\$(?!\s)(?P<tex>[^$\n]*?[^$\s])\$(?![A-Za-z0-9])"
    ),
]


def protect(text):
    text, store = mask_code(text)
    for pat in _DISPLAY_PATTERNS:
        text = pat.sub(lambda m: encode(True, m.group("tex").strip()), text)
    for pat in _INLINE_PATTERNS:
        text = pat.sub(lambda m: encode(False, m.group("tex").strip()), text)
    return unmask_code(text, store)


def walk(section):
    if not isinstance(section, dict):
        return
    chapter = section.get("Chapter") or section.get("PartTitle")
    if isinstance(chapter, dict):
        if chapter.get("content"):
            chapter["content"] = protect(chapter["content"])
        for sub in chapter.get("sub_items", []) or []:
            walk(sub)


def main():
    # mdBook probes support first: `<command> supports <renderer>` with empty
    # stdin and reads the exit code. Everything else receives the book JSON.
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        renderer = sys.argv[2] if len(sys.argv) > 2 else ""
        sys.exit(0 if renderer in ("", "html", "markdown") else 1)

    raw = sys.stdin.read()
    if not raw.strip():
        sys.exit(0)
    data = json.loads(raw)
    book = data[1] if isinstance(data, list) and len(data) > 1 else data
    # mdBook renamed "sections" to "items"; accept both.
    for key in ("items", "sections"):
        for section in book.get(key, []) or []:
            walk(section)
    sys.stdout.write(json.dumps(book, ensure_ascii=False))


if __name__ == "__main__":
    main()

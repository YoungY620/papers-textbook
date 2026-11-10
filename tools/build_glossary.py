#!/usr/bin/env python3
"""Generate the glossary appendix and the runtime glossary data.

Source of truth is a single YAML file per book holding both languages:

    - term: Key Escrow
      term_zh: 密钥托管
      pinyin: mi          # pinyin of the first Chinese character, for sorting
      brief: An account-recovery design in which the server can obtain a key.
      brief_zh: 一种账户恢复设计，服务器能够取得密钥。
      detail: ...
      detail_zh: ...
      chapter: 4.1
      first_seen: Key Escrow

Outputs, for the English and the Chinese book:

    <en_src>/glossary.md        <en_src>/assets/glossary.json
    <zh_src>/glossary.md        <zh_src>/assets/glossary.json

Usage: build_glossary.py glossary.yml src zh/src
"""
import sys
import os
import re
import json
import unicodedata

import yaml


def make_id(term):
    s = unicodedata.normalize("NFKD", term).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return "term-" + (s or "x")


def group_key_en(term):
    ch = term.lstrip("(")[:1].upper()
    return ch if ch.isalpha() else "#"


def group_key_zh(entry):
    py = (entry.get("pinyin") or "").strip().lower()
    if py and py[0].isalpha():
        return py[0].upper()
    return "#"


def link_target(id_):
    return f'<a id="{id_}"></a>'


def render(entries, lang):
    if lang == "en":
        entries = sorted(entries, key=lambda e: e["term"].lower())
        key_of = lambda e: group_key_en(e["term"])
        title = "Glossary"
        intro = (
            "Terms used throughout this book, with the one-line gloss that "
            "appears when you hover a highlighted term in the text. Each entry "
            "also gives the section where the term is first introduced."
        )
        term_of = lambda e: e["term"]
        alt_of = lambda e: e.get("term_zh", "")
        brief_of = lambda e: e.get("brief", "")
        detail_of = lambda e: e.get("detail", "")
        seen_label = "First seen"
    else:
        entries = sorted(entries, key=lambda e: (group_key_zh(e), e.get("pinyin", ""), e["term_zh"]))
        key_of = group_key_zh
        title = "术语表"
        intro = (
            "本书出现的术语一览，与正文中悬浮卡片里的一句话释义一致。"
            "每条另附该术语首次出现的章节。"
        )
        term_of = lambda e: e["term_zh"]
        alt_of = lambda e: e.get("term", "")
        brief_of = lambda e: e.get("brief_zh", "")
        detail_of = lambda e: e.get("detail_zh", "")
        seen_label = "首见"

    groups = {}
    for e in entries:
        groups.setdefault(key_of(e), []).append(e)

    out = [f"# {title}", "", intro, ""]
    keys = sorted(groups)
    if keys:
        jumps = " · ".join(f"[{k}](#gloss-{k.lower()})" for k in keys)
        out += [jumps, ""]

    for k in keys:
        out += [f'<a id="gloss-{k.lower()}"></a>', "", f"## {k}", ""]
        for e in groups[k]:
            seen = e.get("first_seen") or e.get("chapter") or ""
            if lang == "zh":
                m = re.fullmatch(r"Chapter (\d+)", seen.strip())
                if m:
                    seen = f"第 {m.group(1)} 章"
            pp = e.get("paper", "")
            if pp:
                seen = f"{pp} · {seen}" if seen else pp
            out.append(link_target(e["id"]))
            out.append("")
            head = f"**{term_of(e)}**"
            alt = alt_of(e)
            if alt:
                head += f" — *{alt}*"
            if seen:
                head += f"  <span class='bd-gloss-alpha'>{seen_label}: {seen}</span>"
            out += [head, "", brief_of(e), ""]
            detail = detail_of(e)
            if detail:
                out += [detail.strip(), ""]
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    if len(sys.argv) != 4:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    yml_path, en_src, zh_src = sys.argv[1:4]

    with open(yml_path, encoding="utf-8") as fh:
        raw = yaml.safe_load(fh) or []

    entries = []
    for item in raw:
        if not item or not item.get("term"):
            continue
        e = dict(item)
        e.setdefault("term_zh", e["term"])
        e["id"] = e.get("id") or make_id(e["term"])
        entries.append(e)

    ids = [e["id"] for e in entries]
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        print(f"build_glossary: duplicate ids: {dupes}", file=sys.stderr)
        sys.exit(1)

    payload = {}
    for lang, src in (("en", en_src), ("zh", zh_src)):
        page = render(entries, lang)
        if src.endswith("zh/src") or lang == "zh":
            src = zh_src
        else:
            src = en_src
        with open(os.path.join(src, "glossary.md"), "w", encoding="utf-8") as fh:
            fh.write(page)
        data = [
            {
                "id": e["id"],
                "term": e["term"] if lang == "en" else e["term_zh"],
                "brief": e.get("brief", "") if lang == "en" else e.get("brief_zh", ""),
            }
            for e in entries
        ]
        payload[lang] = data
        os.makedirs(os.path.join(src, "assets"), exist_ok=True)
        with open(os.path.join(src, "assets", "glossary.json"), "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=1)

    print(f"build_glossary: {len(entries)} terms -> {en_src}, {zh_src}")


if __name__ == "__main__":
    main()

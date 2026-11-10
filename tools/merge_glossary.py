#!/usr/bin/env python3
"""Merge per-chapter glossary fragments into a book's glossary.yml.

Fragments are written independently by chapter authors so that no two writers
touch the same file. This merges them, de-duplicates by lower-cased term
(keeping the first definition and the earliest chapter), and writes the
combined source of truth.

Usage: merge_glossary.py <fragment-dir> <out.yml> [--keep <extra.yml> ...]
"""
import sys
import os
import re
import glob

import yaml

FIELDS = ("term", "term_zh", "pinyin", "brief", "brief_zh", "detail",
          "detail_zh", "chapter", "first_seen")


def load(path):
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or []
    return [d for d in data if isinstance(d, dict) and d.get("term")]


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    frag_dir, out = args[0], args[1]
    paper = ""
    if "--paper" in args:
        k = args.index("--paper")
        paper = args[k + 1]
    keep = []
    if "--keep" in args:
        i = args.index("--keep")
        keep = args[i + 1:]

    files = sorted(glob.glob(os.path.join(frag_dir, "*.yml"))) + keep
    merged = {}
    order = []
    for path in files:
        if os.path.basename(path).startswith("_"):
            continue
        for entry in load(path):
            # Normalise so "Data origin authentication" and
            # "data-origin authentication" collapse to one entry.
            key = re.sub(r"[^a-z0-9]+", "", entry["term"].strip().lower())
            if key in merged:
                existing = merged[key]
                if paper and not existing.get("paper"):
                    existing["paper"] = paper
                for f in FIELDS:
                    if not existing.get(f) and entry.get(f):
                        existing[f] = entry[f]
                continue
            cleaned = {f: entry[f] for f in FIELDS if entry.get(f)}
            if paper:
                cleaned["paper"] = paper
            merged[key] = cleaned
            order.append(key)

    entries = sorted(
        (merged[k] for k in order),
        key=lambda e: (e.get("chapter", ""), e["term"].lower()),
    )
    with open(out, "w", encoding="utf-8") as fh:
        yaml.safe_dump(entries, fh, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, width=100)
    print(f"merge_glossary: {len(entries)} terms from {len(files)} file(s) -> {out}")


if __name__ == "__main__":
    main()

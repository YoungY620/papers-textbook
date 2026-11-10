# Paper textbooks

Chapter-by-chapter readings of security papers, published as a bilingual
mdBook site. One site, one book per paper.

**Read it: <https://youngy620.github.io/papers-textbook/>**
中文版：<https://youngy620.github.io/papers-textbook/zh/>

## Papers

| Paper | Venue | Chapters |
| --- | --- | --- |
| [Zero Knowledge (About) Encryption](https://www.usenix.org/conference/usenixsecurity26/presentation/scarlata) — Scarlata, Torrisi, Backendal, Paterson | USENIX Security '26 | 10 + sources |
| [SoK: Attack and Defense Landscape of Agentic AI Systems](https://www.usenix.org/conference/usenixsecurity26/presentation/kim-juhee-agentic) — Kim, Guo, Song | USENIX Security '26 | 10 + sources |

Each book rebuilds the paper's argument as prose, redraws the paper's figures at
300 dpi, re-typesets its tables as Markdown (checked cell by cell against the
page images), folds in the conference talk where one exists, and closes with a
chapter on the related work and baselines the paper positions itself against —
written from the referenced works themselves.

## Layout

```
src/                       English book (site root)
  papers/<slug>/           one directory per paper, assets included
zh/src/                    Chinese book (published under /zh/)
glossary.yml               glossary source of truth, merged from per-chapter fragments
tools/                     math protection, math restore, glossary build/merge,
                           internal-link audit
```

## Notes on the build

- **Math.** Markdown is parsed before MathJax runs, and that pass destroys TeX
  that matters here (`\{0,1\}^*`, `${K}_{i}`, `\\` inside `aligned`).
  `tools/protect_math.py` is an mdBook preprocessor that replaces every math
  span with an opaque token before Markdown sees it; `tools/restore_math.py`
  restores it in the built HTML and in the search index.
- **Search.** mdBook's index keeps only ASCII tokens, so Chinese is not
  searchable out of the box. `bd-cjksearch.js` answers CJK queries by scanning
  the index's document store directly.
- **Glossary.** Per-chapter YAML fragments are merged into `glossary.yml`, which
  generates the appendix page and the hover-card data; the runtime wraps the
  first occurrence of each term on a page.

Build locally:

```sh
pip install pyyaml
bash build.sh                                      # -> _site/
node tools/check-links.mjs _site --base /papers-textbook   # no dead links
```

`build.sh` does not check links: mdBook resolves `[x](y.md)` relative to the
chapter file, so moving a chapter (or moving a page chapters link to) breaks
links silently. `check-links.mjs` resolves every local `href`/`src` in the
built output against the files on disk.

---

Produced with the **course-textbook-builder** workflow
(<https://github.com/YoungY620/my-awesome-skills>).

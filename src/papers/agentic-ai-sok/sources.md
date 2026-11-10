# References and source material

## Primary source

Juhee Kim, Wenbo Guo and Dawn Song. **SoK: Attack and Defense Landscape of
Agentic AI Systems.** In *35th USENIX Security Symposium (USENIX Security
'26)*, Baltimore, MD, August 2026. USENIX Association.

- Presentation page: <https://www.usenix.org/conference/usenixsecurity26/presentation/kim-juhee-agentic>
- Preprint PDF (used for this book): <https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_kim-juhee-agentic.pdf>
- Final proceedings PDF: <https://www.usenix.org/system/files/usenixsecurity26-kim-juhee-agentic.pdf>

The authors are at UC Berkeley, Seoul National University (Juhee Kim, work done
during a visit to UC Berkeley) and UC Santa Barbara (Wenbo Guo).

## Conference talk

There is no recorded talk for this paper on the conference page, so this book
is built from the paper alone. That is a real difference from the companion
volume on password managers, which folds in a recorded presentation: nothing
here comes from a second source, and nothing has been cross-checked against a
presenter's own account of the work.

## Where the paper's own sources live

The paper is a systematisation, so most of its content is a summary of other
work: attack papers, defence papers and deployed systems. The paper's
bibliography is the right place to go for any specific mechanism named in this
book. Where a named system appears in the text, this book preserves the name so
that the citation can be found in the paper's reference list.

Standards and taxonomy sources the paper builds on, and which are worth reading
directly:

- MITRE ATLAS, the adversarial threat landscape for AI systems, which the paper
  maps its risk taxonomy onto.
- Model Context Protocol (MCP), for the tool-interface mechanism the paper
  discusses under tool poisoning.

## How this book was made

The chapters were written from the paper's text and page images. Figures are
cropped from the paper at 300 dpi; tables from the paper are re-typeset as
Markdown and checked against the page images. The English and Chinese versions
were written as parallel documents rather than translated one from the other.

The paper compresses a very large body of work into twenty pages. This book
does not attempt to expand it back out: it explains the mechanisms and the
taxonomy, and it keeps the identifiers (`V1`…`V6`, `R1`…`R7`) so that any claim
can be traced to the paper's own tables.

---

This book was produced by the **course-textbook-builder** workflow
(https://gist.github.com/YoungY620/d4932154735b55903d5a53b5f6f406c9).

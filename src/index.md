# USENIX Security '26 — Paper Textbooks

Chapter-by-chapter readings of security papers. Each paper gets its own book
inside this site: the paper's argument rebuilt as prose, the figures redrawn
from the paper, the conference talk folded in where one exists, and a chapter
on the related work and baselines the paper positions itself against.

Everything is published twice — English at the site root, Chinese under `/zh/`
— with a language switch in the top bar and a [glossary](glossary.md) shared
across papers.

## Papers

### [Zero Knowledge (About) Encryption: A Comparative Security Analysis of Three Cloud-based Password Managers](./papers/zk-encryption/index.md)

Matteo Scarlata, Giovanni Torrisi, Matilda Backendal and Kenneth G. Paterson.
USENIX Security 2026.

Twenty-five practical attacks on Bitwarden, LastPass and Dashlane under a
threat model in which the server storing the encrypted vault is fully
malicious: key escrow, item-level vault encryption, sharing, and backwards
compatibility. Includes the authors' conference talk, which is where the
fourth-vendor comparison comes from.

### [SoK: Attack and Defense Landscape of Agentic AI Systems](./papers/agentic-ai-sok/index.md)

Juhee Kim, Wenbo Guo and Dawn Song. USENIX Security 2026.

The first systematisation of knowledge on AI agent security: seven design
dimensions that determine how much risk an agent carries, the attack vectors
`V1`…`V6`, the security risks `R1`…`R7`, and the defence landscape organised by
where each mechanism sits in the control flow.

## How each book is built

The chapters are written from the paper's text and page images. Figures are
cropped from the paper at 300 dpi, tables are re-typeset as Markdown and
checked cell by cell against the page images, and formulas are protected from
the Markdown parser by a preprocessor so that they typeset correctly. The
English and Chinese versions are written as parallel documents rather than
translated one from the other.

Each book's final chapter covers the work the paper compares itself against and
the direction it belongs to, sourced from the referenced papers themselves.

---

This site was produced by the **course-textbook-builder** workflow
(https://github.com/YoungY620/my-awesome-skills).

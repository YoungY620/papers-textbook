# References and source material

## Primary source

Matteo Scarlata, Giovanni Torrisi, Matilda Backendal and Kenneth G. Paterson.
**Zero Knowledge (About) Encryption: A Comparative Security Analysis of Three
Cloud-based Password Managers.** In *35th USENIX Security Symposium (USENIX
Security '26)*, Baltimore, MD, August 2026, pages 4267–4286. USENIX
Association.

- Presentation page: <https://www.usenix.org/conference/usenixsecurity26/presentation/scarlata>
- Preprint PDF (used for this book): <https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_scarlata.pdf>
- Final proceedings PDF: <https://www.usenix.org/system/files/usenixsecurity26-scarlata.pdf>
- Cryptology ePrint Archive preprint 2026/058: <https://eprint.iacr.org/2026/058>
- Project website, including the artefacts statement: <https://zkae.io/>

## Conference talk

*USENIX Security '26 — Zero Knowledge (About) Encryption: A Comparative
Security Analysis of Three Cloud-based Password Managers*, presented by Matteo
Scarlata. USENIX, 19 minutes.
<https://www.youtube.com/watch?v=jpYYXMAoY5U>

The talk was transcribed from its automatic captions. Wherever the transcript
and the paper disagree, this book follows the paper; material that appears only
in the talk is labelled as such. Two things worth knowing about the recording:
the presenter frames the work as covering **four** password managers, using
1Password as a comparison point even though the paper's analysis covers three;
and the automatic captions garble product names, so the transcript alone is not
a reliable source for identifiers.

## Vendor responses

The vendors published their own accounts of the findings and of their
remediation work. These are the vendors' claims, not the paper's findings, and
this book records them as such.

- Bitwarden — *Security Through Transparency: ETH Zurich audits Bitwarden cryptography*: <https://bitwarden.com/blog/security-through-transparency-eth-zurich-audits-bitwarden-cryptography/>
- Dashlane — *Zero knowledge and the malicious server*: <https://dashlane.com/blog/zero-knowledge-malicious-server>
- Dashlane — support article on the reported issues: <https://support.dashlane.com/hc/articles/33346483084050>
- LastPass — *Details on hardening in response to ETH Zurich reported security issues*: <https://blog.lastpass.com/posts/details-on-hardening-in-response-to-eth-zurich-reported-security-issues>
- 1Password — *ETH Zurich zero-knowledge malicious-server review*: <https://1password.com/blog/eth-zurich-zero-knowledge-malicious-server-review>

## Secondary coverage

- USI, *Password manager security: joint USI-ETH Zurich study*: <https://www.inf.usi.ch/en/feeds/11405>
- USENIX Security '26 cycle 1 accepted papers: <https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers>

## How this book was made

The chapters were written from the paper's text and page images, with the
conference talk folded in as a second source. Figures are cropped from the
paper at 300 dpi; tables from the paper are re-typeset as Markdown and checked
against the page images. The English and Chinese versions were written as
parallel documents rather than translated one from the other, which caught a
number of transcription errors on both sides.

Two limits are worth stating plainly. First, the talk could not be watched
frame by frame — only its caption track was retrievable — so any content the
speaker conveyed purely visually and did not say aloud is not represented here.
Second, the paper's Proof-of-Concept code is not public, so no attack in this
book was re-implemented or independently reproduced from this text.

---

This book was produced by the **course-textbook-builder** workflow
(<https://github.com/YoungY620/my-awesome-skills>).

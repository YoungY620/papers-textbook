# Zero Knowledge (About) Encryption

This is a chapter-by-chapter reading of *Zero Knowledge (About) Encryption: A
Comparative Security Analysis of Three Cloud-based Password Managers* by Matteo
Scarlata (ETH Zurich), Giovanni Torrisi and Matilda Backendal (USI, Lugano) and
Kenneth G. Paterson (ETH Zurich), published at the 35th USENIX Security
Symposium (2026). The paper analyses Bitwarden, LastPass and Dashlane — more
than 60 million users and 23% of the market between them — under a threat model
in which the server that stores the encrypted vault is **fully malicious**, and
reports 25 practical attacks: 12 against Bitwarden, 7 against LastPass and 6
against Dashlane.

The nine chapters follow the structure of the paper and fold in the conference
talk that the first author gave, which is where several of the explanations,
the running example and the fourth vendor comparison come from.

## What the paper argues

"Zero Knowledge Encryption" is a vendor marketing phrase, not a technical term.
Vendors use it to claim that the server never learns anything about the
contents of the vaults it stores — including when the server itself is the
adversary. The paper takes that claim at face value and tests what actually
happens. The claim does not survive contact with the implementation: the
attacks range from integrity violations of a single victim's vault to the
complete compromise of every vault in an organisation, and most of them recover
passwords.

The point is not that password managers are useless. It is that the malicious
server threat model surfaces a recurring set of design anti-patterns and
cryptographic misconceptions, and that those are worth naming so that
end-to-end encrypted systems in general can avoid them.

## How to read this book

Every chapter states, at the end, a short list of the points it established.
Notation and the attack identifiers (BW01…BW12, LP01…LP07, DL01…DL06) follow
the paper, so a chapter can be read alongside the relevant section of the PDF.
Terms that carry a specific meaning here are highlighted in the text: hovering
one shows a one-line gloss, and clicking it opens the [glossary](glossary.md).

Mathematics is typeset with MathJax. Where the paper and the talk describe the
same mechanism differently, the paper is authoritative and the difference is
noted.

## Source material

- Paper: [USENIX Security '26 presentation page](https://www.usenix.org/conference/usenixsecurity26/presentation/scarlata) ([PDF](https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_scarlata.pdf))
- Preprint: [Cryptology ePrint Archive 2026/058](https://eprint.iacr.org/2026/058)
- Project website: [zkae.io](https://zkae.io/)
- Talk: *USENIX Security '26 — Zero Knowledge (About) Encryption*, USENIX (19 minutes)

See [References and source material](sources.md) for the full list, including
the vendor disclosure statements.

---

This book was produced by the **course-textbook-builder** workflow
(<https://github.com/YoungY620/my-awesome-skills>).

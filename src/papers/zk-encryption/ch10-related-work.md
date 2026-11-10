# Related work and baselines

Cloud-based password managers have been studied for over a decade. This chapter reconstructs the field around this paper's contribution: what each prior work established, the adversary it assumed, and what changes once the server is treated as fully malicious. It also covers the end-to-end encrypted (E2EE) cloud storage line the paper draws on, the primitives it recommends, and the fourth vendor raised in the talk.

## The early analyses and their threat models

Li, He, Akhawe and Song (USENIX Security 2014) analysed five popular web-based password managers and identified four key security concerns. In four of the five, an attacker could learn a user's credentials for arbitrary websites; the root causes ranged from logic and authorisation mistakes to misunderstandings of the web security model and to CSRF and XSS. The adversary is a web attacker acting on the browser — a malicious site or script, or another user of the service — never the vault server. Silver, Jana, Boneh, Chen and Jackson (USENIX Security 2014) studied autofill policies and showed that several let a remote network attacker extract multiple passwords without user interaction.

The paper places these alongside the rest of the first wave: Belenko and Sklyarov (2012), Fahl et al. (2013), Stock and Johns (2014), Zhao, Yue and Sun (2013), and Gasti and Rasmussen on database formats (2012), which gave the first rigorous analysis of storage formats. But the adversary was always a website, a network attacker or a local attacker, and client-side or storage-side weaknesses the target. None considered a malicious server.

## The 2020 re-evaluations

Carr and Shahandashti (IFIP SEC 2020) tested five commercial managers against previously disclosed vulnerabilities, finding a mixed picture, and their functionality tests yielded four new vulnerabilities, one letting a malicious Android application impersonate a legitimate one to two of the five. Oesch and Ruoti (USENIX Security 2020) evaluated thirteen browser-based managers across generation, storage and autofill — the first analysis of generation — and likewise reported improvement. These are the studies the paper cites for the conclusion that managers had improved; it does not reach the malicious-server model, which neither study tested.

## Injection attacks and offline guessing

Fábrega, Namavari, Agarwal, Nassi and Ristenpart (USENIX Security 2024) developed injection attacks in which the adversary controls only their own application client and injects chosen payloads into a victim's client, for example by sharing credentials. The injections are interleaved with observations of protected state — encrypted vault exports, or traffic reaching the application servers — from which the adversary backs out passwords, URLs, usernames and attachments, across ten manager applications. The malicious party is the client and the server or network is a passive observer. Duan, Wang and Fu (IEEE S&P 2025) gave the first extensive formal analysis of master-password-protected protocols, recovering the de facto protocols of 43 managers by documentation analysis, traffic analysis and reverse engineering, formalising their properties as ideal functionalities in the universal composability framework, and splitting offline guessing of the master password into four types by adversary knowledge; 38 of the 43 were vulnerable to at least one, a corrupted server can learn Passbolt's encryption key by an oracle attack, and 1Password's two-secret design resists.

A parallel preprint by Avoine, Carpent and Leblanc-Albarel (ePrint 2025/1278) studies managers under a covert server, defining the properties such a manager should satisfy and outlining per manager type both attacks and a design resilient to a covert adversary with multi-device synchronisation. The paper's own account is worth keeping: it classifies cloud-based managers into three types, sketches attacks by type that violate vault integrity and several weaker properties vendors do not target, does not fully explore the impacts, provides no proof-of-concept implementations, and includes attacks relying on weak passwords or low PBKDF iteration counts. Both works share the insight that the provider is assumed trusted without justification; they differ in that this paper demonstrates exploitability.

## What this paper does differently

Here the server deviates arbitrarily from its expected behaviour, the client is honest, and every attack is implemented against real clients: 12 against Bitwarden (`BW01`–`BW12`), 7 against LastPass (`LP01`–`LP07`) and 6 against Dashlane (`DL01`–`DL06`). Instead of generation, autofill, injection or guessing, the attacks are grouped by the four feature families that create the surface: key escrow for recovery and SSO login, vault integrity under item-level encryption, credential sharing, and backwards compatibility. A server acting alone can recover passwords and take over every vault in an organisation.

## The end-to-end encrypted cloud storage line

E2EE cloud storage is the closest established analogue, and the paper argues that "zero knowledge encryption" should mean the same thing for both kinds of product.

Albrecht, Backendal, Coppola and Paterson (IEEE EuroS&P 2024) gave the first detailed analysis of Nextcloud's E2EE feature and three attacks in the malicious-server setting, each compromising the confidentiality and integrity of all of a user's files, all practical with proofs of concept; the first was addressed by temporarily removing file sharing from E2EE pending a redesign. One attack rests on a misconception the paper also names here: that public-key encryption provides data-origin authenticity. Backendal, Haller and Paterson (IEEE S&P 2023) presented five attacks a malicious MEGA provider can mount, including an AES-ECB decryption oracle under the user's master key; Albrecht, Haller, Mareková and Paterson (EUROCRYPT 2023) then showed MEGA's added sanity checks were themselves exploitable. Hofmann and Truong (ACM CCS 2024) analysed five providers — Sync, pCloud, Icedrive, Seafile and Tresorit — finding severe vulnerabilities in four, including injecting files that appear user-uploaded.

The foundational work is Backendal, Davis, Günther, Haller and Paterson (CRYPTO 2024): a formal syntax for E2EE cloud storage, game-based notions of confidentiality and integrity against a fully malicious server in selective and adaptive forms, and a provably secure construction, with the MEGA attacks arising as violations of those notions. The paper proposes adapting this model to password managers, and it supplies the vocabulary this book uses: vault integrity is the analogue of the file integrity these works defined. A retrospective by Albrecht and Paterson adds that marketed "zero knowledge" claims need cryptographic review rather than code audits.

## Cryptographic building blocks and their literature

Public-key authentication. Many attacks substitute a public key with an adversary-controlled one, known since the beginnings of public-key cryptography. Some form of PKI or trust-on-first-use cannot be avoided; the paper points at verified key directories in messaging, and Lawlor and Lewi's account of WhatsApp's key transparency deployment describes an append-only auditable key directory with inclusion and history proofs, built on the line through CONIKS, SEEMless and Parakeet. Such a directory would not stop a server associating the wrong key with a user, but it would make tampering evident.

Ciphertext authentication. No public-key encryption scheme provides data-origin authentication, because anyone can encrypt. The paper recommends signcryption, introduced by Zheng (CRYPTO 1997) to bind a ciphertext to its sender at a cost below signing and encrypting separately; where the client both sends and receives, as with Bitwarden organisation data, symmetric authenticated encryption is cheaper.

Authenticating the vault structure. Merkle-tree techniques can authenticate the vault structure and block selective-deletion attacks, but complete roll-back cannot be ruled out without a trusted third party holding versioning information or local cryptographic state — and local state is problematic when users expect access on presenting only their master password.

Hardware-backed key escrow. Signal's Secure Value Recovery (Connell et al., OSDI 2024) uses multiple enclave and cloud providers so no single one can recover a user's secret, limiting PIN guesses unconditionally in enclave memory with rollback protection. The WhatsApp backup protocol was formally analysed by Davies et al. (CRYPTO 2023); the formal E2EE paper notes that this assumes a trusted hardware security module rather than a fully malicious server, making it a partial answer. Apple's Advanced Data Protection likewise uses authentication-available hardware modules from which iCloud service keys can be deleted, so Apple cannot reach the data.

Cryptographic agility. The paper reads the backwards-compatibility attacks as a failure to follow TLS's hard-won practice of sharp but clean breaking changes, citing the TLS attack line up to the weak-Diffie-Hellman measurement and Logjam downgrade of Adrian et al. (ACM CCS 2015), whose export-grade downgrade is the model for the downgrades mounted here against Bitwarden and Dashlane.

## The fourth vendor: 1Password

The talk presents the work as covering four vendors, adding 1Password to the three in the paper; 1Password's published response is a vendor claim, not a finding. It states that it reviewed the paper and confirmed it introduces no new attack vectors beyond architectural limitations already in its Security Design White Paper, and that there is no bypass of the Secret Key and Secure Remote Password protections. On public-key authentication and vault-key substitution it agrees the issue exists but treats both as one architectural consideration, server-mediated key distribution without strong provenance guarantees, quoting its white paper's Appendix C: there is no robust method for a user to verify that the public key they encrypt to belongs to their intended recipient, so a malicious server could supply dishonest keys.

## What is not covered by prior work

No earlier work analysed a deployed password manager in the malicious-server model with implemented exploits: the injection and guessing lines kept the server passive or honest, the 2020 re-evaluations tested the client-facing lifecycle, and the formal treatment of E2EE cloud storage had not been instantiated for password managers. Three gaps follow. There is no formal definition of a manager's security goal against a malicious server, so the paper's mitigations are argued rather than proved, and the paper warns that other, unmitigated attacks may exist. Complete prevention of vault roll-back is unsolved. Key commitment is not engaged with at all — neither the paper nor the works above give it a role here.

## Sources consulted

Downloaded and read for this chapter.

- Li et al., *The Emperor's New Password Manager* (USENIX Security 2014) — <https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-li-zhiwei.pdf>
- Silver et al., *Password Managers: Attacks and Defenses* (USENIX Security 2014) — <https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-silver.pdf>
- Adrian et al., *Imperfect Forward Secrecy* (ACM CCS 2015) — <https://weakdh.org/imperfect-forward-secrecy.pdf>
- Carr, Shahandashti, *Revisiting Security Vulnerabilities in Commercial Password Managers* (IFIP SEC 2020) — <https://arxiv.org/pdf/2003.01985>
- Oesch, Ruoti, *That Was Then, This Is Now* (USENIX Security 2020) — <https://www.usenix.org/system/files/sec20-oesch_0.pdf>
- Backendal, Haller, Paterson, *MEGA: Malleable Encryption Goes Awry* (IEEE S&P 2023) — <https://mega-awry.io/pdf/mega-malleable-encryption-goes-awry.pdf>
- Albrecht et al., *Caveat Implementor!* (EUROCRYPT 2023) — <https://mega-caveat.github.io/pdf/mega-key-recovery.pdf>
- Albrecht et al., *Share with Care* (IEEE EuroS&P 2024) — <https://ethz.ch/content/dam/ethz/special-interest/infk/inst-infsec/appliedcrypto/education/theses/nextcloud.pdf>
- Backendal et al., *End-to-End Encrypted Cloud Storage* (IEEE S&P Magazine 2024) — <https://static.cryptanalysis.fun/papers/e2ee-cloud-storage.pdf>
- Backendal et al., *A Formal Treatment of E2EE Cloud Storage* (CRYPTO 2024, full version) — <https://www.research-collection.ethz.ch/server/api/core/bitstreams/433c6e41-ef2c-442a-b36d-7acb01d6b384/content>
- Connell et al., *Secret Key Recovery in a Global-Scale E2EE System* (OSDI 2024) — <https://www.usenix.org/system/files/osdi24-connell.pdf>
- Fábrega et al., *Exploiting Leakage in Password Managers via Injection Attacks* (USENIX Security 2024) — <https://www.usenix.org/system/files/usenixsecurity24-fabrega.pdf>
- Hofmann, Truong, *E2EE Cloud Storage in the Wild: A Broken Ecosystem* (ACM CCS 2024) — <https://brokencloudstorage.info/paper.pdf>
- Duan, Wang, Fu, *Security Analysis of Master-Password-Protected Password Management Protocols* (IEEE S&P 2025) — <https://cssnku.github.io/uploads/publications/ieeesp25-pm-full.pdf>
- 1Password, *ETH Zurich zero-knowledge malicious-server review* (vendor response) — <https://1password.com/blog/eth-zurich-zero-knowledge-malicious-server-review>
- Lawlor, Lewi, *Deploying key transparency at WhatsApp* — <https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/>
- Apple, *Advanced Data Protection for iCloud* — <https://support.apple.com/guide/security/advanced-data-protection-for-icloud-sec973254c5f/web>
- Avoine et al., *In the Vault, But Not Safe* (ePrint 2025/1278) — abstract page read at <https://eprint.iacr.org/2025/1278>; the PDF sits behind a bot-protection challenge and could not be downloaded.

Not obtained: Davies et al., *Security Analysis of the WhatsApp E2EE Backup Protocol* (CRYPTO 2023), is open access only on the ePrint Archive, whose PDF endpoint was unreachable, so only its abstract and the formal E2EE paper's description of its trust assumptions were available. Gasti and Rasmussen (ESORICS 2012) and Zheng's *Digital signcryption* (CRYPTO 1997) are paywalled with no author copy found.

## Key points

- Early analyses (Li et al. 2014, Silver et al. 2014 and the surrounding first wave) assumed a web, network or local attacker; none considered a malicious server.
- The 2020 re-evaluations (Carr and Shahandashti, five managers, four new vulnerabilities; Oesch and Ruoti, thirteen managers) found improvement in a client-side model only.
- Fábrega et al. (2024) assume a malicious client with a passive server or network adversary; Duan et al. (2025) formalise 43 managers' protocols and find 38 vulnerable to at least one of four offline guessing attacks.
- The concurrent covert-provider preprint (ePrint 2025/1278) assumes a covert server and sketches attacks by manager type with no proof-of-concept code.
- This paper's distinguishing features are a fully malicious, arbitrarily deviating server, implemented exploits against deployed clients, and the four feature families: key escrow, vault integrity under item-level encryption, sharing and backwards compatibility.
- The E2EE cloud storage line supplies the integrity vocabulary: practical malicious-server breaks of Nextcloud, MEGA and five providers, and the formal notions of Backendal et al. (CRYPTO 2024) that the paper adapts.
- Recommended building blocks each have prior literature: signcryption (Zheng 1997), verified key directories (WhatsApp's auditable key directory, via CONIKS, SEEMless and Parakeet), Merkle-tree vault authentication, hardware-backed escrow (Signal's Secure Value Recovery, Apple's Advanced Data Protection) and TLS-style agility.
- The talk adds a fourth vendor, 1Password, whose response concedes the key-verification limitation as already documented while asserting no new attack vectors; that is a vendor claim, not a finding.

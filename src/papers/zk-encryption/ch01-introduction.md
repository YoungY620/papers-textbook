# Background: password managers and the “zero knowledge” claim

## Why password managers exist

Users still have to deal with passwords, often numbering in the hundreds, despite alternative authentication methods. A password manager stores them securely and reduces remembering many passwords to remembering one: the "master password". The conference talk opens by asking where the audience keeps its passwords — on paper, in stone, or in a password manager — and adds that a manager cannot be destroyed in the laundry; that framing is the talk's.

## The cloud vault model

A cloud-based password manager outsources storage to a remote server under a service provider's control. The user's passwords are collected into a single object that the client encrypts under a cryptographic key derived from the master password, producing an encrypted **vault** that the client uploads. To use a password, the client authenticates to the service, retrieves the encrypted vault and decrypts it locally with a user-supplied copy of the master password. The provider never sees the vault plaintext, so it does not immediately learn the user's passwords or other sensitive data. This is the same situation as end-to-end encrypted (E2EE) cloud storage; vendors sometimes say E2EE or client-side encryption, but the term they use most often is **Zero Knowledge Encryption**.

The talk makes the key layering explicit where the paper states it abstractly: the user remembers only the master password, which wraps a **vault key**, and the vault key ultimately encrypts the vault. The unit of storage is the **vault item** — a username, a password and a URL for one website, or, as the paper notes, credit-card data, personal documents or notes — and a vault is a user's collection of items.

"Zero knowledge" has a precise meaning in interactive protocols but is used here with a different one. The paper treats the vendors' claim as one whose meaning for a user has to be pinned down and tested.

The feature users want is also what creates the attack surface. Users reach their vaults from multiple devices, vaults hold more than passwords, and the service can share sensitive data within a family, group or organisation; "access from anywhere" therefore obliges vendors to support web browsers as well as stand-alone applications on several operating systems, and many also allow self-hosting of the storage element.

## The vendors and the market

Three prominent providers are Bitwarden, Dashlane and LastPass. At the time of writing, Bitwarden claims 10 million users; Dashlane 19 million users and 24,000 business customers; and LastPass 33 million users and 100,000 business customers. A 2024 report based on a survey of 1000 US consumers gives a second view. The built-in password managers of Google and Apple now represent 55% of the market, up from a combined 15% in 2021. Bitwarden and LastPass come next, at 11% and 10%; Dashlane has 2%, down from 7% in 2021.

The two sources disagree, and the paper says why: the apparent inconsistency between the number of users and market share arises because the figures come from different places — vendors' self-reported claims versus a market study — and Dashlane disputes the study's accuracy on the grounds of its small sample size. Together, the three vendors account for more than 60 million users and 23% of the market. The talk quotes the same population as 60 million users and 28% market share; the 28% is the talk's, and the 23% is the figure consistent with the 2024 survey. The talk widens the comparison to a fourth vendor, 1Password, which the paper does not study, quoting its claim that not even the company storing the data can access or decrypt the user's data; this fourth-vendor comparison is the talk's.

They were chosen for their market share, the availability of unobfuscated client source code (complete for Bitwarden, partial for the others), their feature richness and diversity. Apple and Google dominate but publish no source, and E2EE is opt-in in Google's manager.

## The threat model, informally

The vendors' security explanations imply that vault data stays protected even if the server is fully malicious. The paper adopts this as its threat model and argues that it is stronger than prior work's. Three arguments support it: the vendors' own explanations imply that security holds in this setting; because they store so much sensitive data, service providers are likely targets for sophisticated attackers able to penetrate the servers and mount active attacks, and several have been breached repeatedly; and security against a malicious server is by now standard in cloud storage and messaging.

The talk states the expectation underneath all of this in one sentence: no access to the master password implies no access to the vault, no matter what the server does, even if the server is compromised or acting maliciously. That is what a user would reasonably read into the vendors' claims, and what the paper tests.

## Four categories of attack

The result is 25 practical attacks — 12 against Bitwarden (BW01–BW12), 7 against LastPass (LP01–LP07) and 6 against Dashlane (DL01–DL06) — with proofs of concept for all of them. They range from integrity violations of targeted user vaults to the complete compromise of every vault associated with an organisation, and most recover passwords, the very thing a password manager exists to protect.

Following the feature each exploits, the attacks fall into four categories. The first exploits the key escrow features used for account recovery and SSO login (BW01 Malicious Auto-Enrolment, BW02 Malicious Key Rotation, BW04 Malicious Password Reset). The second exploits the lack of integrity of the vault as a whole (Unprotected Item Metadata, Item Field Swapping, Remove KDF Iterations). The third exploits the sharing features (Sharing Key Overwrite, Organisation Injection, Organisation Overwrite). The fourth exploits backwards-compatibility features (Disable Per-Item Keys, Downgrade to Legacy, CBC-Only Downgrade, Lucky 64).

Several failure modes recur. Lack of authentication of public keys is widespread and, combined with key escrow and sharing, lets the adversary fully compromise vaults. Wrongly assuming origin authentication of public-key ciphertexts yields key substitution attacks against Bitwarden. LastPass stands out for lacking any ciphertext integrity, using AES-CBC as its main mode, and legacy code and backwards-compatibility exploits downgrade Bitwarden and Dashlane similarly. Integrity is achieved only for single fields inside items rather than at the level of the vault, enabling cut-and-paste attacks within an item and across a vault, often chained into a confidentiality break; these work even with proper authenticated encryption, because of insufficient key separation in complex vaults and no binding between data and metadata.

## Mitigations and disclosure

The paper describes possible mitigations for each attack and strategies for avoiding the pitfalls it found, and shared them with all three vendors under an industry-standard coordinated disclosure approach giving each at least 90 days. The ethics analysis and disclosure timeline are in Appendix A; the timeline itself is in the next chapter.

## What the findings mean beyond the three products

The affected vendors can patch their systems and give stronger security to millions of users, but the findings also mark a frontier for end-to-end encrypted applications in general. Vault integrity is a new finding, parallel to recent notions for cloud storage. Supporting key escrow without opening attack avenues is a hard problem, one that has recurred in debates over lawful access and the Crypto Wars. Reliably authenticating public keys is a problem messaging shares, where auditable key directories are being introduced. And getting end-to-end encryption right is not easy: 25 severe vulnerabilities across three diverse vendors establish the need for formal study, the paper argues, proposing that the goals of E2EE against a malicious server be formally defined, as recently done for cloud storage.

Prior work makes the study timely, since password managers were analysed substantially soon after they appeared but never in the malicious-server model adopted here. Work from 2020 concluded that their security had improved; more recently, one line developed injection attacks under a model with a malicious client and a passive server or network adversary, and another studied 43 managers for offline guessing. A parallel preprint studies managers whose server stays "covert", but does not fully explore the impact of its attacks, gives no proofs of concept, and some of them rely on weak passwords or low PBKDF iteration counts.

## Key points

- A cloud-based password manager encrypts the vault on the client under a key derived from the master password and stores only the ciphertext with the server, so the provider never sees the plaintext.
- Vendors market this as Zero Knowledge Encryption, a phrase with a technical meaning in interactive protocols that is used loosely here to mean the server cannot read the vault.
- Bitwarden, Dashlane and LastPass account for more than 60 million users and 23% of the market on market-study figures that disagree with the vendors' own user counts.
- The paper adopts a fully malicious server threat model, justified by the vendors' own claims, the sensitivity of vault data and the prevalence of malicious-server security in cloud storage and messaging.
- The informal expectation is that without the master password there is no access to the vault, whatever the server does.
- The paper reports 25 attacks — 12 against Bitwarden, 7 against LastPass and 6 against Dashlane — grouped into key escrow, vault-level integrity, sharing and backwards compatibility.
- Most attacks recover passwords; the recurring causes are missing public-key authentication, missing ciphertext integrity, insufficient key separation and no binding between data and metadata.
- The findings were disclosed under coordinated disclosure with at least 90 days per vendor, and they generalise beyond the three products to end-to-end encrypted systems.

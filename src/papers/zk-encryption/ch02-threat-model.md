# The malicious-server threat model

## What the adversary controls

The paper analyses cloud-based password managers in a threat model in which the servers storing users' vaults are assumed to be fully malicious: they can deviate arbitrarily from their expected behaviour when interacting with clients, and such deviations are hard to detect, especially when aimed at selected users. This is stronger than the model prior work used, and the paper argues that it is the right one.

## The trivial attack taken off the table

One attack is excluded from the outset. A user could be supplied with a malicious client that simply returns the master password to the server in the clear. That attack would be detectable through code audits and would be very risky for a vendor: for signed software releases such as desktop and mobile clients and browser extensions, the existence of a signed malicious client would constitute proof of vendor misconduct. Security against it is assumed, and the model concerns a malicious server interacting with an honest client.

## The security goals

Given this model, the paper asks what security users should reasonably expect. The appropriate guarantees are three.

1. Confidentiality of all data in a user's vault. This includes the items — credentials, that is usernames and passwords, but also credit-card information and notes. Most metadata is not kept confidential in the systems studied, but keeping it confidential is also desirable.

2. Integrity of vault data and metadata. This should hold at the level of individual items and at the level of the data collection as a whole. It should be infeasible for an adversary to modify or inject data, to undetectably delete or modify any data, or to change the semantics of any data in a vault, for example by altering metadata. In particular, the integrity of user-specific settings should be maintained.

3. Secure sharing and account recovery. Where these features are enabled, only the users with whom a given user intends to share vault data, or to grant an account-recovery capability, should be able to access that data or recover the account.

Several subsidiary properties follow. It should be hard, for example, for a malicious server to weaken the cryptography that clients use — reducing the iteration count used in password hashing is the paper's example. The paper also names more advanced goals, including vault indistinguishability, oblivious client operations and device privacy. Those are far from being achieved by today's managers and are out of scope; the paper points to a separate study of possible security properties instead.

## The adversary's concrete capabilities

Three capabilities follow directly from the model and recur throughout the attacks. The server can tamper with the ciphertexts it serves, which is decisive wherever integrity protection is missing: LastPass, with AES-CBC as its main mode, has no ciphertext integrity at all. It can serve data that is stale or attacker-chosen rather than what the vault actually contained, which the synchronisation and replay attacks exploit. And it can influence the cryptography the client performs, for instance by lowering the KDF iteration count used when deriving keys, which removes brute-force protection. Because the server is also the client's source for keys, policy and metadata, it can substitute keys, replay operations and manipulate the membership of organisations, and an honest client cannot tell these manipulations from ordinary service.

## Why the model is realistic

The paper gives three arguments, made briefly in its introduction and expanded in Appendix C.

The first is the vendors' own advertising. Their explanations of Zero Knowledge Encryption imply that vault data stays protected against a malicious server. The paper quotes Bitwarden's statement that "Not even the team at Bitwarden can read your data (even if we wanted to)"; Dashlane's that "malicious actors can't steal the information, even if Dashlane's servers are compromised", because Dashlane cannot access the vault and does not store the master password; and LastPass's that "no one has access to your master password for LastPass or the data stored in your LastPass vault, except you (not even LastPass)". The vendors have not contested the model: the three to whom the findings were disclosed did not question its adoption, although LastPass says it does not adopt a generic malicious-server threat model and instead applies compensating controls.

The second argument is that passwords are high-value data. They grant access to accounts and services that may reveal more data or let an attacker impersonate the victim, and a password-manager server concentrates the passwords of thousands of users in one place, which makes it an attractive target. Careful operational security can help, but it is well within reason to assume that these services are targeted by sophisticated, nation-state-level adversaries through supply-chain attacks or spear-phishing. Some providers have a history of breaches: LastPass was breached in 2015 and 2022 and suffered another serious incident in 2021. In the 2022 breach the attacker reached the development environment, source code and technical information, compromised a senior DevOps engineer's computer, then reached an encrypted corporate vault and finally the keys of the Amazon S3 buckets holding customer-file backups. A self-hosted server run by a less advanced customer could hardly resist such an attack. None of the breaches the authors are aware of involved reprogramming the server to act maliciously, but that step is only one beyond documented attacks on password-manager providers, and active attacks of this kind have been observed in the wild.

The third argument is that the model is the norm elsewhere. Security against a malicious server is a standard expectation in messaging and cloud storage, where providers likewise relay or store sensitive data, and it is the accepted reading of what end-to-end encryption guarantees there. Vendors of E2EE cloud storage use the term Zero Knowledge Encryption for the same idea, and recent analyses of cloud-storage systems have forced vendors to upgrade their approach so that it withstands a malicious server. Signal, WhatsApp and iMessage have long offered E2EE in the standard sense, with Telegram a notable exception. It is reasonable, the paper argues, to expect "zero knowledge" and "end-to-end encryption" to mean the same thing in password managers.

There is also a practical side, which the paper calls quantifying the provided security: it must be clear which threats password managers withstand and which they do not, which calls for analysis in a range of threat models, including a strong one. The paper expects the community eventually to develop formal models and security proofs for password managers, as it has for cloud storage, and concludes that the malicious-server setting is an appropriate model for analysing their security.

## Client interaction as a resource

Some attacks need interaction with the honest client, and the paper treats that interaction as a resource. Most attacks need only routine interactions — logging in, opening the vault, or periodic synchronisation — while others need a key rotation, joining an organisation, sharing credentials, or clicking on a misleading dialog. Within a vast user base many users will perform them, and Table 1 records the requirement for each attack.

## The disclosure timeline

Disclosure followed a coordinated approach with a window of at least 90 days. Bitwarden was contacted on 27 January 2025 and Dashlane on 29 August 2025; the first email to Dashlane was lost and a second attempt on 5 September 2025 succeeded. LastPass was first contacted on 4 June 2025, but that email went to a spam filter; one of the authors reached the CTO over social media, the email was found on 26 June 2025, and the authors and LastPass agreed to reset the 90-day clock. LastPass accepted working directly with the authors rather than through its bug-bounty programme, whose publication restrictions were unacceptable, and awarded two bug-bounty payments on 7 October 2025. The period was extended for one vendor on request, and the three agreed a common public disclosure date of 14 February 2026.

Remediation is underway. Bitwarden has addressed BW01, BW03, BW11 and BW12; the minimum KDF iteration count for BW07 is now 5000; and its roadmap includes removing CBC-only encryption, enforcing per-item keys and changing the vault format to provide integrity, with a signed organisation-membership scheme intended to resolve BW08 and BW09. LastPass has addressed LP03. Dashlane has mitigated DL03, DL04, DL05 and DL06 by disallowing CBC-only mode in Flexible payloads, and no remediation is planned for DL01 and DL02.

## Key points

- The threat model assumes the server that stores vaults is fully malicious and may deviate arbitrarily from expected behaviour, which is stronger than the models used in prior work.
- A malicious client is excluded as a trivial case, because it would be detectable in code audits and, for signed releases, would constitute proof of vendor misconduct.
- The security goals are confidentiality of vault data, integrity of vault data and metadata at both item and collection level, and secure sharing and account recovery.
- The model lets the server tamper with ciphertexts, serve stale or attacker-chosen data, and weaken client cryptography such as KDF iteration counts.
- Advanced goals such as vault indistinguishability, oblivious client operations and device privacy are out of scope because today's managers are far from achieving them.
- The model is justified by the vendors' own claims, by the high value of concentrated password data together with the documented breach history, and by the fact that malicious-server security is the norm in messaging and cloud storage.
- Client interaction is treated as a resource that each attack spends to a listed degree, and disclosure runs on a 90-day clock per vendor with a common public date of 14 February 2026.

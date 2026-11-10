# Discussion, conclusions and disclosure

All three products advertise "zero knowledge encryption" and all three are badly broken against a malicious server. The same design anti-patterns and cryptographic misconceptions recur independently in every codebase.

## A burdensome legacy

Password managers were early entrants in end-to-end encryption, predating every modern encrypted messenger: LastPass shipped in 2008. Encrypting vaults was always central, but practice moved on. Dashlane (2012) and Bitwarden (2016) entered a market with quite low cryptographic standards, and their early releases show a taste for early-2000s cryptography: encryption without integrity protection, and unprincipled designs.

Backwards compatibility preserved those residues, because vendors were deeply concerned about leaving users with undecryptable vaults and so support old formats at extreme length. The security community had meanwhile learned from the SSL and TLS attacks to set backwards compatibility aside and adopt cryptographic agility: sharp but clean breaking changes that keep past attacks at bay.

## Deceptively simple

Password managers had escaped deep academic scrutiny: they are frequently code-audited but not cryptographically reviewed, perhaps because the problem looks like key derivation followed by encryption. In fact they have grown protocols for key synchronisation, recovery and rotation, for sharing encrypted elements, and for migration between primitives, with complexity comparable to end-to-end encrypted cloud storage. Best practices trickled in, but there was never a gold standard to match, as TLS or Signal provide, nor precise security notions to aim for. This mirrors encrypted cloud storage, whose formal foundations are only now emerging.

## Integrity in motion

Storing a whole vault in one authenticated-encryption blob does not scale, so managers holding many items structure vaults for per-item synchronisation. The tension between integrity and incremental updates is resolvable by clean key separation. Preventing deletion stays open: Merkle trees can authenticate the vault structure and block selective-deletion attacks, but complete roll-back cannot be ruled out without a trusted third party holding versioning information or local cryptographic state. The latter is problematic because users expect access to their vault on presenting only their master password, even on a stateless client.

## Share with care

Many vulnerabilities substitute public keys with adversary-controlled ones, an attack known since the beginnings of public-key cryptography. Verifying other users', administrators' or organisations' keys runs into a well-known obstacle: some form of public-key verification, and hence some form of PKI, cannot be avoided. The mitigations rely on PKIs or Trust-On-First-Use; secure messaging explores Verified Key Directories, which would not stop a malicious server from associating the wrong public key with a user, but would make the tampering evident.

Authenticating keys is only half the battle: it is a common misunderstanding, here and for encrypted cloud storage, that public-key encryption produces authenticated ciphertexts. No PKE scheme can offer data origin authentication, because any party can encrypt, which is why ciphertexts should be bound to their senders with signcryption.

## Securing a "backdoor"

Recovering vault content after a forgotten master password creates a tension between security and usability: no recovery gives the best security, but may be untenable for large populations of non-technical users. Admin-assisted recovery can be implemented safely, but hinges on solving key authentication first. Secure messaging shows the state of the art: Signal and WhatsApp are converging on hardware security modules in the cloud to protect recovery and backups, and Apple's Advanced Data Protection uses HSMs so a user recovers key material from just a PIN. Putting part of the key-escrow functionality on an HSM gives at least some guarantee that the server behaves honestly.

## Conclusions

The malicious-server threat model is the correct one for cloud-based password managers: it is claimed in vendor advertising and is the gold standard for modern end-to-end encrypted systems. Three popular managers with more than 60 million users in total are badly broken in that model. The vulnerabilities are numerous but mostly not technically deep, yet were apparently not found before, despite a decade of academic research and multiple audits. Vendors must move to modern primitives, but solid foundations also need new definitions for security in this setting. Key escrow, item-level vault encryption, password sharing and backwards compatibility each raise an open academic question about providing the functionality securely. The work improved practical security for millions of users and raised vendor interest in formal guarantees.

## Disclosure and coordination

The authors followed an industry-standard coordinated vulnerability disclosure approach: each vendor got at least 90 days and a detailed, vendor-specific document, while the authors stayed silent in public and supported them with descriptions of the issues, video conferences and patch review. They judged 90 days sufficient but remained open to extension, and did extend it for one vendor; the approach is endorsed, for example, by ENISA, an EU body.

They disclosed to Bitwarden on 27 January 2025, to LastPass on 4 June 2025, and to Dashlane on 29 August 2025. Bitwarden responded with a video conference and many emails; by the time of writing BW01, BW03, BW11 and BW12 had been addressed, the minimum KDF iteration count for BW07 was raised to 5000, and the roadmap included removing CBC-only encryption, per-item keys and vault-format integrity. On 22 December 2025 Bitwarden shared a draft for a signed organisation membership scheme resolving BW08 and BW09. At the authors' request, to maintain their anonymity, it had not yet credited them publicly, but planned to.

LastPass's initial contact, through the official email channel on 4 June 2025, got no response; one author reached the CTO over social media, and the original email was found in the organisation's spam filter on 26 June 2025. The 90-day clock was reset by mutual agreement. LastPass gave regular updates and met by video to clarify findings, and accepted working directly rather than through its preferred bug bounty programme, whose publication restrictions were unacceptable; on 7 October 2025 it awarded two bug bounty payments. LP03 had been addressed.

Dashlane's first email was also lost, but a second attempt on 5 September 2025 succeeded; the authors then replicated the attacks with its engineers over several emails and one video call. DL03, DL04, DL05 and DL06 were mitigated by disallowing CBC-only mode in Flexible payloads, and no remediation was planned for DL01 and DL02. All vendors then agreed to a joint thread for the preprint and to holding back public statements until a mutually agreed date of 14 February 2026, later than any 90-day period.

## Ethical considerations

The harm analysis is consequentialist and stakeholder-based: the researchers, the affected vendors (Bitwarden, Dashlane, LastPass), vendors of related products, customers, and society. The authors set themselves aside, being unable to analyse rationally how publication might affect them.

Affected vendors may suffer reputation and commercial damage; LastPass, for example, was reported to lose many customers after repeated breaches. The 90-day window is the mitigation. Related-product vendors could inherit the same flaws; the work was already discussed in an informal industry forum after the Bitwarden disclosure, which formally broke the coordination agreement but had the positive effect of alerting other vendors. Afterwards the authors will publicise the work widely, including, at Dashlane's request, to a group of CTOs.

Most users would not be targeted, since the attacks need stringent conditions, but higher-risk individuals and organisations could be at substantial risk; advanced threat actors may already have known of the attacks, as national security agencies routinely penetrate such systems. The best mitigation is rapid patching. Society benefits because a higher bar pushes vendors to improve security or state more clearly what it provides, and on this balance of benefits against harms the authors decided to publish.

## Open science

The artefacts are proof-of-concept code for all the attacks. Some were being mitigated while others remained exploitable pending longer-term mitigations such as public-key authentication, so the sensitive PoCs were withheld until all agreed embargo periods ended, though they were given to the programme committee on request. At the time of writing all 90-day periods had ended, but the agreed public date of 14 February 2026 was still ahead, when PoCs for mitigated attacks will be published at `https://doi.org/10.5281/zenodo.17977565`.

## What the talk adds

The presenter's closing remarks, not in the paper, test the claims of four vendors, adding 1Password to the three analysed, and report that the four together account for 60 million users, hundreds of thousands of businesses and 28% market share. He notes that at least nine of the 31 attacks the talk counts had been mitigated by then. On motivation, he asks why the progress made on messaging applications should not be ported to password managers: HSMs for key escrow, key transparency for public-key authentication in sharing, key separation for partial vault synchronisation, and, for backwards compatibility, following TLS and WireGuard in dropping legacy code and deprecated schemes. He closes on whether the vendors achieve zero knowledge encryption, or rather zero knowledge about encryption.

## Key points

- Independent codebases repeat the same flaws because the field inherited early-2000s cryptography and kept it for backwards compatibility while the wider field moved to cryptographic agility.
- The products look like simple key derivation plus encryption but have grown recovery, rotation, sharing and migration protocols rivalling encrypted cloud storage, with no gold standard to aim at.
- Public-key encryption does not authenticate ciphertexts, since any party can encrypt; ciphertexts need signcryption, and public keys need PKI, Trust-On-First-Use or a Verified Key Directory.
- Vault deletion and roll-back stay unpreventable without a trusted third party or local state, and recovery is safe only once key authentication is solved.
- Disclosure ran on 90-day windows from 27 January 2025 (Bitwarden), 4 June 2025 (LastPass) and 29 August 2025 (Dashlane), with a common public date of 14 February 2026 and only partial fixes shipped.
- One vendor asked to stay anonymous, so the authors were not credited publicly; the stakeholder analysis found the benefits of publication outweighed the harms.

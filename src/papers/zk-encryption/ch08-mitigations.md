# Mitigations

Every attack above can be removed by combining five techniques: **authenticated
encryption** (AE), **key separation** (KS), **plaintext authentication** (AD),
**public key authentication** (PKA) and **ciphertext authentication** (SC).
Table 1 records which of the five closes each attack; one measure usually closes
several, and the backwards-compatibility attacks against CBC-accepting
clients need two.

| Class | Ref | Name | Cause | Impact | Interaction | Mitigation |
| --- | --- | --- | --- | --- | --- | --- |
| Key escrow | BW01 | Malicious Auto-Enrolment | Lack of key auth, key substitution | Full vault compromise † | 1 join | PKA, SC |
| Key escrow | BW02 | Malicious Key Rotation | Key substitution | Full vault compromise † | 1 rotation | SC |
| Key escrow | BW03 | Malicious KC Conversion | Lack of key auth, key substitution | Full vault compromise † | 1 dialog | PKA, SC |
| Key escrow | LP01 | Malicious Password Reset | Lack of key auth | Full vault compromise † | 1 login | PKA, SC |
| Item-level vault encryption | BW04 | Unprotected Item Metadata | Lack of auth enc | Read and modify metadata | – | AE, AD |
| Item-level vault encryption | BW05 | Item Field Swapping | Lack of key sep | Field and item swapping | – | KS |
| Item-level vault encryption | BW06 | Icon URL Item Decryption | Lack of key sep | Loss of confidentiality † | 1 open | KS |
| Item-level vault encryption | BW07 | Remove KDF Iterations | Lack of auth enc | No brute-force protection | 1 login | AD |
| Item-level vault encryption | LP02 | Item Field Swapping | Lack of auth enc | Field and item swapping | – | KS, AE |
| Item-level vault encryption | LP03 | Icon URL Item Decryption | Lack of key sep | Loss of confidentiality † | 1 open | KS, AE |
| Item-level vault encryption | LP04 | Remove KDF Iterations | Lack of auth enc | No brute-force protection | 1 login | AD |
| Item-level vault encryption | LP05 | Malleable Vault | Lack of auth enc | Loss of vault integrity | – | AE |
| Item-level vault encryption | LP06 | Unprotected Item Metadata | Lack of auth enc | Read and modify metadata | – | AD, AE |
| Item-level vault encryption | DL01 | Transaction Replay | Lack of key sep | Loss of vault integrity | – | KS |
| Sharing | BW08 | Organisation Injection | Lack of key auth | Add users to arbitrary orgs | 1 sync | SC |
| Sharing | BW09 | Organisation Overwrite | Lack of key auth, key substitution | Organisation compromise † | 1 join | PKA, SC |
| Sharing | LP07 | Sharing Key Overwrite | Lack of key auth | Shared vault compromise † | 1 join | PKA |
| Sharing | DL02 | Sharing Key Overwrite | Lack of key auth | Shared vault compromise † | 1 join | PKA |
| Backwards compatibility | BW10 | Disable Per-Item Keys | Lack of auth enc | Downgrade key hierarchy | – | KS, AD |
| Backwards compatibility | BW11 | User Key Overwriting | CBC support | Loss of confidentiality † | 2 logins | AE |
| Backwards compatibility | BW12 | Downgrade to Legacy | CBC support | Full vault compromise † | 2 logins | AE |
| Backwards compatibility | DL03 | Item Injection | CBC support | Loss of vault integrity | $10^{4}$ syncs | AE |
| Backwards compatibility | DL04 | Remove KDF Iterations | CBC support | No brute-force protection | $10^{4}$ syncs | AE |
| Backwards compatibility | DL05 | CBC-Only Downgrade | CBC support | Loss of confidentiality † | $10^{5}$ syncs | AE |
| Backwards compatibility | DL06 | Lucky 64 | CBC support | No brute-force protection | $10^{4}$ syncs | AE |

*Table 1: the attacks grouped by the feature they exploit. `BW` marks
Bitwarden, `LP` LastPass and `DL` Dashlane; † marks recovery of encrypted
passwords. The interaction column gives the client action the attack needs:
periodic or user-triggered synchronisation, a login, opening the vault, joining
an organisation, sharing a vault, or a misleading dialog.*

## Immediate remediations

In the authors' discussions with the vendors, the need for breaking changes
was the main obstacle to deploying the countermeasures. Breaking changes
are nevertheless necessary and inevitable: no arrangement of optional
flags closes the attack surface while the old formats stay readable. The route
proposed is a dedicated client whose only function is a forced migration to the
new vault format, so that no user loses access to their data.

### Only use authenticated encryption

Legacy support for schemes without integrity should be switched off rather than
kept behind a compatibility flag. That alone remediates most
backwards-compatibility attacks on Bitwarden (BWb1, BW11, BW12) and Dashlane
(DLb1, DLb2, DL03, DL05, DL06), all of which exist because clients still accept
AES-CBC. Encrypting item metadata with AE also removes BW04. LastPass has no AE
to fall back on and would have to introduce it; doing so removes many of its
vault-encryption issues (LP05, LP06) and, with key separation, also LP02 and
LP03. Table 1 also credits AE with DL04, which this list omits.

### Full key separation

Most vault-integrity issues come from reusing keys, and separation removes
them: each key should encrypt exactly one field of one vault item, derived from
the master key through a suitable key derivation function with per-item and
per-field context strings. A single encrypted blob forces every change to
re-encrypt and re-upload everything; per-field keys let each item be encrypted
and synchronised independently while the overall structure stays
integrity-protected. In Bitwarden the per-item keys are a good starting point,
but separation has to reach the field level: that makes URL checksums
unnecessary, removes BW05, BW06 and, once item keys are mandatory, BW10, and with AE it stops the conditions behind BWb1, the Known Plaintext
Oracle Gadget. LastPass has no key separation at all, so it must arrive
alongside AE, which then mitigates LP02 and LP03, while keying each Dashlane
transaction under its unique transaction identifier resolves DL01.

### Authenticate all plaintext

Settings and metadata that cannot be encrypted should still be integrity
protected. AEAD does this without touching the plaintext and removes the
metadata-malleability issues BW04 and LP06. More consequentially, it covers
security-critical settings such as the PBKDF parameters, including the
iteration count, which removes the KDF attacks BW07 and LP04. The client
derives the authentication key from the server-supplied parameters, uses it to
verify the parameters themselves and aborts before further communication on
failure, so tampering with the iteration count would require predicting the
authentication key. That argument is circular, since the parameters and the key
protecting them travel together, and it relies on non-standard properties of
MACs, so safe KDF parameter sets also need allowlisting.
Authenticating the last server version the client has seen, by folding it into
the vault, additionally mitigates BW10: an old vault can still be replayed with
its matching server version, but new items are protected.

### Public-key authentication

Authenticating public keys is not a small change. A stop-gap is to store known
public keys in the vault after an optional out-of-band check: users then notice
a key change, and even without that check the attacker can substitute a key
only on its first use. The fuller answer is a PKI in which a certificate
authority signs every public key, the CA lying outside the control of whoever
runs the password-manager server so that it can act as a trusted third party. Public-key authentication remediates most sharing
issues (BW09, LP07, DL02), lets users authenticate the escrow keys of
administrators and organisations and, given a correctly signed and published
list of administrators, also removes several key-escrow issues (BW01, BW03,
LP01).

### Ciphertext authentication

In Bitwarden the only cryptographic evidence of organisation membership is that
the client can decrypt organisation data the user encrypted under their own
public key. Anyone can produce such a ciphertext, so the evidence is
worthless, and the result is BW02, BW08 and BW03. The fix is to authenticate
the ciphertext at its origin: signcryption signs the plaintext before
encrypting it, letting a client check that the user is genuinely the sender.
The alternative is to drop public-key encryption here for symmetric
authenticated encryption, since the user is both sender and recipient: cheaper
at run time, but a larger redesign. Either removes all three. Receiving
public-key ciphertext from other users, as with organisation invitations in
Bitwarden or the administrator list for a LastPass team, needs signcryption and
public-key authentication together, and that combination removes BW01, BW09
and LP01.

## Future designs and limitations

The five measures are also a roadmap for a manager secure by construction. A
PBKDF-derived key comes from the master password, and standardised key
derivation functions derive a separate symmetric key for every vault item.
Those keys encrypt vault data under a modern AEAD scheme, whose built-in
authentication supplies ciphertext integrity cheaply, so all user data is both
encrypted and authenticated, leaving only unavoidable metadata such as the
PBKDF parameters authenticated but unencrypted. Where public-key cryptography
is needed, public keys are authenticated by certificates and ciphertexts by
signatures.

### What public-key encryption cannot do

Authenticating public keys is only half the problem. Public-key encryption does
not by itself authenticate the ciphertext it produces, although it is commonly
assumed to: no public-key scheme can provide data-origin authentication, because by definition any party can encrypt. A ciphertext tied
to its sender therefore needs a primitive such as signcryption.

### Key distribution in practice

Several vulnerabilities rest on replacing a public key with one the adversary
controls, an attack known since the early days of public-key cryptography.
Verifying public keys is the general key-distribution problem, and some form of
PKI cannot be avoided; certificates and trust-on-first-use are the practical
forms, and secure messaging is exploring verified key directories, which do not
stop a malicious server from associating the wrong public key with a user but
make the tampering evident.

### Integrity with incremental updates

A single authenticated blob is not viable at real vault scale, and managers
structure vaults so individual items synchronise; clean key separation
resolves the apparent tension between integrity and incremental updates.
Preventing deletion remains open: Merkle-tree techniques can prevent selective
deletion attacks by authenticating the vault structure, but a complete roll-back
cannot be excluded without outsourcing versioning information to a trusted
third party or to local cryptographic state, both awkward for password
managers, whose users expect to reach their vault with nothing but the master
password, even on a stateless client.

### Recovery against security

Account recovery is where usability and security pull hardest against each
other. Any recovery mechanism is in effect a backdoor: with none at all the
security is as good as it can be, but for a large population of non-technical
users that is not a workable product. Administrator-assisted recovery can be
implemented safely, but only once key authentication is solved; secure
messaging is converging on hardware security modules in the cloud to protect
account recovery and backups, and Apple's Advanced Data Protection uses HSMs so
that a user can recover key material from a PIN alone. Moving part of escrow onto an HSM gives at least some guarantee
that the server is behaving honestly, and a hybrid design could use one to
distribute the administrator's keys without other PKI or out-of-band
verification.

### Caveat

The mitigations cover every attack the authors found, but further cryptographic
attacks, not yet discovered, may exist that they do not stop. A formal
definition of what a password manager must achieve against a malicious server
is the first step towards provable security, and the design above has the same
status as the attacks: only an analysis backed by formal models and proofs
could inform a detailed construction, which is beyond the scope of the paper.

## Remediation in practice

The accompanying talk reports that at the time of recording at least nine of
the 31 attacks had been mitigated, and frames the remaining work
around the same four features: HSMs for key recovery, key transparency for
public-key authentication, key separation for partial vault synchronisation
and, for backwards compatibility, dropping legacy code and deprecated schemes
as TLS and WireGuard did. Bitwarden had addressed BW01, BW03, BW11 and BW12,
raised the minimum KDF iteration count so that BW07 is closed, and planned to
remove CBC-only encryption, enforce per-item keys and change the vault format
for integrity, sharing a draft signed organisation membership scheme that
resolves BW08 and BW09. LastPass had addressed LP03, and Dashlane had mitigated
DL03 to DL06 by disallowing CBC-only mode in Flexible payloads, with nothing
planned for DL01 or DL02.

## Key points

- Five techniques cover the whole surface — AE, key separation, plaintext
  authentication, public-key authentication and ciphertext authentication — and
  Table 1 fixes which attacks each closes.
- Requiring AE and dropping AES-CBC closes the backwards-compatibility family
  (BWb1, BW11, BW12, DLb1, DLb2, DL03, DL04, DL05, DL06), which is why it takes
  a forced migration, not a compatibility flag.
- Key separation down to a single field of a single item replaces the
  monolithic blob, makes URL checksums unnecessary and removes BW05, BW06,
  BW10, LP02, LP03 and DL01.
- Authenticating PBKDF parameters against an allowlist of safe sets removes
  BW07 and LP04, and authenticating the last server version removes BW10,
  although the parameters-verify-themselves argument is circular.
- No public-key scheme can authenticate its own ciphertexts, so a sender-bound
  ciphertext needs signcryption or symmetric authenticated encryption (BW02,
  BW03, BW08) and, to accept ciphertexts from other users, public-key
  authentication too (BW01, BW09, LP01, LP07, DL02).
- Recovery is a backdoor by construction: HSMs bound the trust placed in the
  server, but no recovery design is safe until key authentication is solved and
  the goal is formally defined.

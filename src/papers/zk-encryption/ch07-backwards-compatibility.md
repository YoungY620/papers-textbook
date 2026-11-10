# Attacks IV — backwards compatibility

Backwards compatibility is the fourth attack class and the one the presenter treats as the most interesting. After the sharing attacks, the talk offers this class as the "cooler" one and calls the Bitwarden instance the Heisenberg attack. Both Bitwarden and Dashlane evolved their primitives over the years, from AES in CBC mode and PBKDF2 to AE schemes such as AES-CBC-HMAC and memory-hard PBKDFs like Argon2d, with Bitwarden also moving to per-item keys for better key separation. Current clients use modern cryptography by default but still offer "legacy" support, so an adversary can downgrade, sometimes permanently, the primitives a client uses, reducing security to that of the weakest supported algorithm.

## Bitwarden

Latest clients use authenticated encryption for all symmetric operations by default: AES-CBC with HMAC, combined via encrypt-then-MAC, used to decrypt the user key received at login and to encrypt and decrypt vault items. Older versions used AES-CBC without HMAC, which offers no integrity. To accommodate both, each ciphertext carries an encryption type attribute — type 0 for AE, type 1 for plain AES-CBC — prepended to the ciphertext and not integrity-protected. Older versions also used a different key hierarchy, so a modern client generates a new RSA keypair $(pk', sk')$ if the server provided none, and encrypts $sk'$ with the master key $k_m$ if the server provided no user key ciphertext $c_u$, letting it migrate an old vault to the current feature set.

### BWb1: Known Plaintext Oracle Gadget

The adversary can exploit the keypair generation and the support for encryption under $k_m$ to obtain AES-CBC encryptions of known plaintexts under an unknown $k_m$. At login it answers with a null $c_u$ and a null private RSA key ciphertext $c_{sk}$. The missing $c_{sk}$ forces the user to generate a new RSA keypair; because $c_u$ was also null, the client encrypts the new secret key under $k_m$ with AES-CBC, giving $c'_{sk}$, and sends $pk'$ and $c'_{sk}$ to the server. Since $sk'$ encodes $pk'$, the adversary learns a 5-block-long plaintext-ciphertext pair.

### BW11: User Key Overwriting

The adversary forges a ciphertext $c_u^{adv}$ that the client decrypts to a user key $ku = ku^{enc} \| ku^{mac}$ whose encryption half it knows. Each half is 32 bytes, two blocks of CBC plaintext. Building on the BWb1 pair, the adversary bit-flips the last ciphertext block to a block $P_5$ of padding, garbling the preceding block $P_4$ while leaving $P_1$, $P_2$ and $P_3$ known, and marks the ciphertext as type 0. The client accepts it as a valid user-key encryption — encrypted under $k_m$, type 0 so CBC decryption, unpadding succeeds — and parses $ku = ku^{enc} \| ku^{mac}$. Because $ku^{enc}$ is $P_1$ and $P_2$ the adversary knows it in full, while $ku^{mac}$ is unknown through the garbled $P_4$.

The adversary therefore learns $ku^{enc}$, which encrypts all vault items, so the confidentiality of every item encrypted after the attack is forfeit; integrity survives because $ku^{mac}$ stays unknown. The user must log in: the first login fails and the user is sent to a migration page, and the attack completes on a later login regardless.

### BW12: Downgrade to Legacy

The same construction yields a user key whose MAC half is empty. Following BW11 with only three blocks — $P_3$ a block of padding, $P_2$ garbled — the client accepts $c_u^{adv}$ again. The short ciphertext triggers a second backwards-compatibility feature: the client parses $ku = ku^{enc}$ without the "mac" part, so all subsequent encryptions use CBC-only mode. Per-item keys, if enabled, still use AES-CBC with HMAC, but BW10 shows the adversary can easily disable them.

Encryption is now CBC-only, trivially compromising the integrity of all items encrypted after the attack and enabling a padding oracle that fully compromises vault confidentiality. No proof of concept was built for that last part, but Bitwarden's developers acknowledged its feasibility. The adversary also knows $P_1$ and therefore half of $ku^{enc}$. The requirements are BW11's.

This pair gives the attack its Heisenberg name: a short legacy vault key leaves the client with no MAC key, so integrity is lost but confidentiality survives, while a full modern vault key has a known encryption half, so confidentiality is lost but the garbled MAC half preserves integrity.

## Dashlane

Every transaction has a payload defining the KDF, cipher and mode used to decrypt its content. KWC3 uses PBKDF2-SHA1 and AES-256-CBC; Flexible carries a format string parsed to select the KDF (PBKDF2-SHA256 or SHA1, Argon2i, or the default Argon2d), its parameters, the cipher (only AES-256) and the mode (documented values: CBC-HMAC, the default, and GCM). Modern clients default to Flexible and auto-migrate a transaction when they detect a KWC3 payload. Legacy support varies: the web extension has it, the CLI client does not, so the attacks below affect only legacy-capable clients, and the proofs of concept target the web extension.

### DLb1, DLb2 and DL03: padding oracle and injection

CBC-only encryption is unexpectedly still accepted as an encryption mode in the Flexible payload format and does not trigger a migration. This enables a padding oracle attack by which the adversary can decrypt a ciphertext under $k_{cbc}$ (DLb1) or encrypt arbitrary plaintext under $k_{cbc}$ (DLb2). The unoptimized attack runs at 14 days per block. DL03 (Item Injection) uses DLb2 to forge arbitrary transactions; all three are described in full only in the extended version.

### DL04: Remove KDF Iterations

User settings control which KDF and parameters every new transaction payload uses. Using DL01 (Transaction Replay) the adversary deletes any transaction of type Setting, returning the settings to a known clean state, then uses DL03 to forge a new Setting transaction. The next item the user creates is encrypted with a key derived using the adversary's parameters — for instance PBKDF2 iterations cut from the default 200,000 to 1, a 200,000-fold speed-up in a brute-force attack. Brute-forcing the master password becomes cheap, and success gives full control of the account; it requires DL01 and DL03.

### DL05: CBC-Only Downgrade

The Setting transaction also controls the cipher and mode for future transactions. As in DL04, the adversary forges settings forcing CBC-only encryption, so the client always writes CBC-only and the resulting transactions fall to the DLb1 padding oracle; the adversary can then decrypt every transaction produced after the attack (DL01 and DL03, plus one DLb1 execution per decrypted transaction).

A minimal forged Setting transaction is only 9 blocks long, enough to test DL04 and DL05. Execution was artificially sped up for testing; at normal speed the authors estimate more than 126 days, reasonable for a targeted attack. DL06 (Lucky 64) is deferred to the extended version; Table 1 gives it cause "CBC Support", impact "No brute-force protection" and a $10^4$-sync preparation.

## Why the downgrade gets through

Both managers select their code path from unauthenticated server-supplied fields — Bitwarden's encryption type attribute, Dashlane's payload format string — so the machinery meant to carry old data forward is also the lever for a downgrade. Being stateless, a client must be told by the server which version to use, so a malicious server downgrades it with a flipped bit.

| Ref | Name | Cause | Impact | Interaction | Mitigations |
| --- | --- | --- | --- | --- | --- |
| BW10 | Disable Per-Item Keys | Lack of Auth Enc | Downgrade key hierarchy | 2 logins | KS, AD |
| BW11 | User Key Overwriting | CBC Support | Loss of confidentiality † | 2 logins | AE |
| BW12 | Downgrade to Legacy | CBC Support | Full vault compromise † | 2 logins | AE |
| DL03 | Item Injection | CBC Support | Loss of vault integrity | $10^4$ syncs | AE |
| DL04 | Remove KDF Iterations | CBC Support | No brute-force protection | $10^5$ syncs | AE |
| DL05 | CBC-Only Downgrade | CBC Support | Loss of confidentiality † | $10^5$ syncs | AE |
| DL06 | Lucky 64 | CBC Support | No brute-force protection | $10^4$ syncs | AE |

The dagger marks attacks that recover encrypted passwords. DL03 and DL04 break integrity or brute-force protection without decrypting anything themselves; BW11, BW12 and DL05 end in confidentiality loss, directly or through the padding oracle the CBC-only downgrade opens. BW12 and DL05 reach furthest, each a full vault compromise, because once the client writes CBC-only every later item is readable through the oracle. Every attack here exploits support for AES-CBC, so the fix is to disable integrity-less legacy schemes with AE; BW10 also needs key separation (KS) and authenticated settings (AD).

## Key points

- Bitwarden and Dashlane keep legacy support for AES-CBC and old key hierarchies, and Bitwarden's unprotected encryption type attribute (type 0 for AE, type 1 for plain AES-CBC) lets an adversary downgrade a client, sometimes permanently, to the weakest primitive still accepted.
- BWb1 exploits the migration path that generates a fresh RSA keypair, obtaining a 5-block plaintext-ciphertext pair under the unknown master key $k_m$.
- BW11 forges a user key with a known encryption half, losing the confidentiality of later items; BW12 forges a short key with no MAC half, forcing CBC-only mode and opening a padding oracle.
- In Dashlane, CBC-only is accepted in the Flexible payload without triggering migration, giving the DLb1 and DLb2 oracles and DL03 item injection; DL04 and DL05 use DL01 and DL03 to rewrite the Setting transaction and cut PBKDF2 iterations from 200,000 to 1.
- Because clients are stateless and learn their format from unauthenticated server fields, the fix is to disable the legacy paths rather than detect them.

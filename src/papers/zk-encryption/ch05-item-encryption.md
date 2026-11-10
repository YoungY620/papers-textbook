# Attacks II — item-level vault encryption

## The vault is not one cryptographic object

A user is shown one "secure vault", but the vault is not a single cryptographic object: items and user settings are stored, managed and encrypted independently.

A monolithic vault would make integrity easy: encrypt everything with an authenticated encryption (AE) scheme and any byte change is detected. The price is synchronisation, since renaming one login would force both sides to re-encrypt the whole vault. So all three managers encrypt each item separately, usually with AE under a single key, which removes the synchronisation cost and with it the whole-vault guarantees. AE protects each item on its own; nothing binds a ciphertext to its item, its position in the vault, or the vault. Items can be swapped, deleted or duplicated, and cleartext metadata — the KDF iteration count, the organisations a user belongs to — can be edited, without the client noticing.

Every attack below exploits that missing **vault integrity**. The paper also reports BW04, LP05 (Malleable Vault) and LP06 in this category and defers them to the full version.

Table 1 (excerpt):

| Ref | Name | Cause | Impact | Interaction | Mitigations |
|-----|------|-------|--------|-------------|-------------|
| BW05 | Item Field Swapping | Lack of Key Sep | Field and item swapping | – | KS |
| BW06 | Icon URL Item Decryption | Lack of Key Sep | Loss of confidentiality † | 1 open | KS |
| BW07 | Remove KDF Iterations | Lack of Auth Enc | No brute-force protection | 1 login | AD |
| LP02 | Item Field Swapping | Lack of Auth Enc | Field and item swapping | – | KS, AE |
| LP03 | Icon URL Item Decryption | Lack of Key Sep | Loss of confidentiality † | 1 open | KS, AE |
| LP04 | Remove KDF Iterations | Lack of Auth Enc | No brute-force protection | 1 login | AD |
| DL01 | Transaction Replay | Lack of Key Sep | Loss of vault integrity | – | KS |

† = recovery of encrypted passwords. KS = key separation, AE = authenticated encryption, AD = authenticated data.

## 4.2.1 Bitwarden

Vault items are encrypted individually, while many settings are not encrypted at all, inside organisations too. An item is an object with fields — item name, password, username, URLs — each encrypted on its own with AES-CBC-HMAC. Up to version 2024.2.0 the fields of all items were encrypted directly with the user key $k_u$. As of v.2024.2.0 a fresh **per-item key** $k_u^i$ is sampled for each new item and the item is encrypted under it; the item key is itself encrypted under $k_u$ and stored as another field (the item-or-item-key arrow in Figure 1). Old items are never migrated, so one vault holds both formats, and the server returns items as a JSON object whose keys are the plaintext field names and whose values are the ciphertexts.

![Key hierarchies for Bitwarden, LastPass and Dashlane.](assets/fig1-key-hierarchies.png)

### BW05: Item Field Swapping

Nothing binds a ciphertext to a particular item field. Field names are plaintext and all values are ciphertexts under one key, so the adversary moves values between the JSON keys: the item name becomes the password, the password the URL. For items created before per-item keys all field ciphertexts are under $k_u$, so ciphertexts can also move between items and form new items from merged fields. The attack has no requirements, violates vault integrity, and is a building block for the rest.

### BW06: Icon URL Item Decryption

Items can carry a URL field, used to autofill credentials and to display an icon. The client decrypts the URL and fetches the icon from the server, sending the domain and top-level domain of the URL — for `https://host.tld/path` it asks for the icon of `host.tld` — so the adversary learns part of anything the client processes as a URL.

BW05 supplies the other half: put the ciphertext of a sensitive field, the username or the password, in the URL field; the client decrypts it believing it is a URL, and if the plaintext meets the paper's conditions for a URL (its wording: "containing a '.' and no '!'") the icon request carries the secret out. A URL checksum deployed in July 2024 stores a hash of the URL in another encrypted field and stops the attack, but old items never get a checksum, and the checksum is checked only when a per-item key is present — which Attack BW10 can prevent.

IMPACT. The adversary recovers selected target ciphertexts, such as the username or the password. REQUIREMENTS. The user opens a vault with items that do not use per-item keys (created before July 2024, or after BW10 is run), and the target plaintext satisfies further conditions given in the full version.

### BW07: Remove KDF Iterations

Client authentication derives $h_m$, a hash of the master key, from the master password typed at login, and the server compares it with a stored hash. Since the master password is the only secret, the derivation is deliberately expensive: a password-based key derivation function (PBKDF) whose cost is set by its parameters. The KDF settings are stored unauthenticated and unencrypted on the server, so on the target's login the adversary picks them. With PBKDF2 at the 600,000-iteration default, where $k_m \leftarrow \mathrm{PBKDF2}(pw, email, 600000)$ and $h_m \leftarrow \mathrm{PBKDF2}(k_m, pw, 1)$, lowering the first iteration count to 1 cuts the work from 600,001 PBKDF2 iterations to 2, a 300,000x speed-up per guess.

IMPACT. The adversary reduces the cost of a brute-force attack on the master password; recovering it yields full control of the account. REQUIREMENTS. The user logs in.

## 4.2.2 LastPass

LastPass items are also fields — item name, username, URL, password — each encrypted under the same user key $k_u$, so the same attacks apply. The talk adds that every field is encrypted with plain AES-CBC, bad in principle but not a practical attack on its own.

### LP02: Item Field Swapping

No associated data binds a ciphertext to its field, so ciphertexts can be swapped between fields and between items, and new items built from merged fields.

### LP03: Icon URL Item Decryption

A login item can include a URL, used for autofill and to display an icon; to fetch the icon the client queries LastPass's icon server, sending the URL stored in the item — the stored URL itself, not only its domain as in Bitwarden. Using LP02, the adversary puts the ciphertext of the username or the password in the URL field; the client decrypts it and the plaintext leaks through the icon query. Unlike Bitwarden there are no conditions on the plaintext formatting.

IMPACT. The adversary recovers parts of selected target ciphertexts. REQUIREMENTS. The client opens the modified vault.

### LP04: Remove KDF Iterations

Authentication checks a hash of the user key — derived from the master password at login — against a hash stored on the server. As in Bitwarden, two PBKDF invocations derive it, with a PBKDF2 default of 600,000 + 1 iterations, and the parameters are unencrypted and unauthenticated, so the adversary sets them. The client enforces a minimum of 2 iterations for the inner invocation while the outer is fixed to 1, so the count drops to 3, a speed-up of 200,000x.

IMPACT and REQUIREMENTS. As in BW07: the adversary cheapens a brute-force attack on the master password, and the user logs in.

## 4.2.3 Dashlane

Dashlane keeps the vault as a transactional database: each transaction creates, modifies or deletes an item. Its type and timestamp are unencrypted metadata, and its content is encrypted under a key derived from the master key using the parameters in the payload — the KDF, its parameters, the cipher and the mode. The salt is constant for all transactions.

### DL01: Transaction Replay

The transaction key depends only on those parameters, so all transactions sharing them use the same derived key. The server can duplicate, reorder or drop transactions without the client noticing. This trivially violates vault integrity and is the building block for the Dashlane attacks of Section 4.4.2, where the same replay removes and replaces the transaction holding the user settings.

## What the missing binding enables further

The **known plaintext oracle gadget** (BWb1) grows out of Bitwarden's support for its old key hierarchy. If the server answers a login with a null user key ciphertext and a null private-key ciphertext, the client makes a new RSA keypair and encrypts its new secret key under the master key $k_m$ with AES-CBC. That secret key encodes the public key, so the adversary gets a 5-block plaintext-ciphertext pair under the unknown $k_m$, and bit-flipping it forges user keys the client accepts: BW11 yields a $k_u = k_u^{enc} \| k_u^{mac}$ whose encryption half is known and whose MAC half is garbled, so confidentiality is lost and integrity kept, while BW12, with three blocks, leaves no MAC part, so the client falls back to CBC-only mode and integrity is lost. The talk calls this pair the "Heisenberg attack". The padding oracle that BW12 is said to enable reaches only items left in CBC-only mode, since items with a per-item key keep AES-CBC-HMAC, and the paper reports it as feasibility the developers acknowledged rather than a working PoC.

The **DLb1 padding oracle** comes from Dashlane's Flexible payload format still accepting CBC-only encryption without a migration: it decrypts ciphertext under $k_{cbc}$ (DLb1) or encrypts arbitrary plaintext under it (DLb2), at 14 days per block in the authors' unoptimised implementation, and DL03 builds on DLb2 to inject transactions.

## Key points

- Vaults are not monolithic: encrypting items separately makes partial synchronisation cheap but leaves no whole-vault integrity, so fields and items can be rearranged and a vault assembled from other items.
- BW05 and LP02 are the base gadget: ciphertexts move between the fields of an item, and where per-item keys are absent, between items and into new items.
- BW06 and LP03 turn that gadget into a confidentiality break through the icon-fetch request; BW06 needs a URL-shaped plaintext and is partly blocked by the 2024 URL checksum, while LP03 sends the stored URL itself with no formatting conditions.
- BW07 and LP04 attack the unauthenticated KDF parameters instead of the ciphertexts, buying about 300,000x (Bitwarden) or 200,000x (LastPass) in brute-force speed per guess.
- DL01 shows the same failure in Dashlane: the transaction key is not tied to the transaction, so transactions can be replayed, reordered or dropped, and the BWb1 and DLb1 gadgets turn the same missing authentication into key or plaintext recovery.

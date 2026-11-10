# How the three managers encrypt a vault

Take a username, a password and the URL of a website: a password manager calls each of these an item, and puts all of them inside a vault. In the conference talk's own picture of the problem, the user remembers a single master password, that master password wraps a vault key, and the vault key ultimately encrypts the vault, which the client uploads to the server. The talk adds that the vault is not one big blob of authenticated encryption: encrypting it whole would force a re-synchronisation whenever a single field changes, which is why Dashlane encrypts at the level of items and LastPass and Bitwarden at the level of fields. All three still build a hierarchy of keys from the same two secrets, a master password and an email address.

![Key hierarchies for Bitwarden (left), LastPass (centre) and Dashlane (right).](assets/fig1-key-hierarchies.png)

The attacks in the rest of the book are read off the key hierarchies of Figure 1, so the notation is worth fixing now.

## Bitwarden

### Key hierarchy and authentication

A Bitwarden user's key hierarchy is rooted in the master password and the account email, which serve as the key and the salt of a key derivation function. The KDF is either PBKDF2 or Argon2id and yields a 32-byte master key $k_m$. For authentication the client sends $h_m$, a single PBKDF2 iteration on the master key with the user's password as salt, and the server compares it with the $h_m$ stored at registration; the paper's default configuration is $k_m \leftarrow \mathrm{PBKDF2}(pw, email, 600000)$ and $h_m \leftarrow \mathrm{PBKDF2}(k_m, pw, 1)$. The master key also derives two 32-byte keys through HKDF-Expand under the labels "enc" and "mac", whose concatenation is the 64-byte extended master key $k_{em} = k_{em}^{enc} \| k_{em}^{mac}$.

Bitwarden then samples a 64-byte user key $k_u$ uniformly at random. Like $k_{em}$ it splits into a 32-byte encryption key $k_u^{enc}$ and a 32-byte MAC key $k_u^{mac}$. The user key protects everything in the vault, either by encrypting items directly or, when per-item keys are enabled, by encrypting the per-item keys $k_u^i$ that in turn encrypt the item fields. It is encrypted under $k_{em}$ and the ciphertext $c_u$ is stored on the server, to be served back at the next login. The client also generates an RSA key pair $(pk, sk)$ with a 2048-bit modulus, used for organisations as described below; the private key is itself encrypted under the user key and sent to the server. Bitwarden allows users and businesses to self-host the server, in order to keep complete control of their data, and for a self-hosted instance the adversary of the threat model is the self-hosted server.

### Key and item encryption

Bitwarden uses AES-CBC-HMAC for authenticated encryption of keys and vault items, with the "enc" part of a key doing the encryption and the "mac" part doing the MACing. For backwards compatibility the HMAC is omitted when the "mac" part is missing: a client asked to encrypt with a key that is only 32 bytes long falls back to plain AES-CBC. Inside a vault item every data field is encrypted individually; fields used to be encrypted directly with $k_u$, but from version 2024.2.0 new items use individually sampled per-item keys $k_u^i$, themselves encrypted by the user key, while old items remain directly under $k_u$.

### Organisations

Credential sharing is implemented through organisations. Creating one makes the client sample a new 64-byte organisation symmetric key $k_{org}$ and encrypt it under the creator's public key, yielding $c_{org}^{user}$; it also generates an organisation RSA key pair $(pk_{org}, sk_{org})$ for account recovery and encrypts the organisation private key under $k_{org}$ to obtain $c_{skOrg}$. The client sends $c_{org}^{user}$, $pk_{org}$ and $c_{skOrg}$ to the server, and items in an organisation are encrypted individually under $k_{org}$.

The creator adds a member by encrypting $k_{org}$ for the invitee's public key. For each user $user'$ the ciphertext $c_{org}^{user'}$ is stored on the server and served on sync; the invitee's client decrypts it with its private key to recover $k_{org}$. Membership is thus a capability rather than a signed list: a client decides that a user belongs to an organisation exactly when it can obtain $k_{org}$. Further organisation data, such as the name and the account-recovery policies, is stored unencrypted and sent on every sync.

## LastPass

LastPass begins, like Bitwarden, from the user's password, used to derive a 32-byte user key $k_u$ with PBKDF2 and the email address as salt. The default KDF iteration count is 600,000. To authenticate, the client sends $h_u$, one further PBKDF2 iteration over $k_u$ with the password as salt, which the server checks against the registration value. The user key encrypts the items of the vault directly with AES-CBC, with no integrity protection. Each user also has an RSA key pair $(sk, pk)$; the secret key is encrypted under $k_u$ with AES-CBC and kept at the server as $c_{sk}$, together with the public key.

Sharing among LastPass users is implemented through shared folders. When a user first shares an item, the client samples a 32-byte shared folder key $k_{shr}$, which is used to encrypt the items of the shared folder with AES-CBC. The folder key is itself encrypted with RSA-OAEP under the public key of every user with whom the folder is shared, giving one ciphertext $c_{shr}$ per recipient.

## Dashlane

### Transactions and the payload string

Dashlane maintains the vault as a transactional database. Each transaction creates, modifies or deletes an item; the transaction type and its timestamp are unencrypted metadata fields, while the transaction content is encrypted. That content is compressed XML data carrying information about items or user settings. Because the type indicator and the timestamp stay in the clear, a malicious server can reorder, replay or drop transactions, which is the root of several of the integrity attacks.

The first bytes of the content are a payload string that specifies its cryptographic parameters: the password-based KDF (PBKDF2, Argon2d, or no derivation at all), its parameters (salt length, hash method, and the iteration count for PBKDF2), the cipher (AES-256 by default) and the cipher mode (CBC with HMAC by default). An intermediate 32-byte key $k_{cbc}$ is derived from the password, and when the mode is CBC with HMAC an additional SHA-512 stretches it into the 64-byte $k_{cbc\text{-}hmac}$. Two payload formats matter for the attacks: the legacy KWC3 format (PBKDF2-SHA1 with AES-256-CBC) and the Flexible format, whose format string selects the KDF (PBKDF2-SHA256 or SHA1, or the default Argon2d), the cipher (only AES-256) and the mode (CBC-HMAC by default, GCM the only other documented mode). The default PBKDF2 iteration count is 200,000. Modifying the vault creates a new transaction, which the client sends to the server.

### RSA keys and sharing

Each Dashlane user also has an RSA key pair with a 2048-bit modulus. The secret key is stored encrypted, as a transaction, on the server, together with the public key. The pair is used for sharing: sharing an item with another user, directly or in a group, samples a symmetric key $k_{shr}$ that is encrypted for the public keys of the recipients, which the sharer retrieves from the server, yielding $c_{shr}$.

## Clients, and how much of this is documented

The three targets were selected partly for the availability of unobfuscated client source code, which is complete for Bitwarden and partial for Dashlane and LastPass. Proof-of-concept testing was limited to Bitwarden's web client and the browser extensions of LastPass and Dashlane, since testing every client is a considerable engineering effort; for most attacks it is evident that they are design issues, independent of any particular client. In LastPass the browser extension is also the only client supporting the key-exchange procedure used for password reset.

The Dashlane description rests on the least solid ground. Its only fully available open-source client is the CLI, which supports neither encryption nor credential sharing, so the account here is based in part on reverse engineering and may be incomplete; the parts relevant to the attacks are those verified by the proofs of concept. Dashlane and LastPass were studied by reverse-engineering minified client JavaScript and the Android applications, after the open Bitwarden code had shown the general shape of the design.

## Key points

- All three managers derive a key from the master password with a password-based KDF, authenticate the client by sending one extra KDF iteration over that key, and protect the vault with a second, longer key.
- Bitwarden derives a 64-byte extended master key $k_{em}$ from its PBKDF2-or-Argon2id master key $k_m$ through HKDF-Expand, and encrypts the randomly sampled 64-byte user key $k_u$ under it to obtain $c_u$.
- Bitwarden and LastPass encrypt keys with an AES-CBC-HMAC construction whose MAC half may be absent, so a 32-byte key triggers a silent fallback to unauthenticated AES-CBC.
- LastPass uses a single 32-byte PBKDF2 output directly as the vault key with AES-CBC, and protects a shared folder with a 32-byte key $k_{shr}$ wrapped with RSA-OAEP for each recipient.
- Dashlane stores the vault as transactions whose type and timestamp are unencrypted metadata and whose content is compressed XML prefixed by a payload string naming the KDF, the cipher and the mode.
- Bitwarden organisations turn membership into a capability: a client is a member exactly when it can obtain the 64-byte organisation key $k_{org}$ by decrypting $c_{org}$.
- The Dashlane description is based in part on reverse engineering, because its only fully open-source client, the CLI, supports neither encryption nor credential sharing.

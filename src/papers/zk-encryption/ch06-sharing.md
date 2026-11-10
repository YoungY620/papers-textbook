# Attacks III — sharing

Sharing is the third of the four attack classes, and the one the presenter singles out as fixable with a primitive the secure-messaging world already has. The talk arranges the risky features as key recovery, partial vault synchronisation, sharing and backwards compatibility, and for sharing it recommends one countermeasure: public-key authentication in the form of key transparency. All three managers implement some form of sharing, and all three fail for the same reason — a client accepts a public key handed to it by the server with no way to check whose key it is. The attacks differ in reach: the LastPass and Dashlane vulnerabilities only affect the items being shared, while the Bitwarden ones enable some of the Key Escrow attacks and have further-reaching consequences.

![Key hierarchies for Bitwarden, LastPass and Dashlane.](assets/fig1-key-hierarchies.png)

## Bitwarden: organisations

Credential sharing in Bitwarden runs through organisations. When a user creates an organisation, the client samples a fresh 64-byte organisation symmetric key $k_{org}$ and encrypts it under the creator's public RSA key, giving $c_{org}^{user}$. It also generates an organisation RSA keypair $(pk_{org}, sk_{org})$, used for account recovery, and encrypts the private key under $k_{org}$ to create $c_{skOrg}$; $c_{org}^{user}$, $pk_{org}$ and the encrypted $c_{skOrg}$ all go to the server. Items in an organisation are encrypted individually under $k_{org}$. A new member is added by encrypting $k_{org}$ under the invitee's public key: the ciphertext $c_{org}^{user'}$ is stored by the server and served to $user'$ at the next sync, where the client decrypts it with its private RSA key to obtain $k_{org}$. A client determines that a user is a member of an organisation exactly when it can obtain $k_{org}$, and the organisation's name and account-recovery policies are plaintext server data that arrives on every sync.

Two things are missing from this design. Nothing cryptographically binds a user's vault — or even the vault abstraction — to the organisations the user belongs to, so the client simply adopts the organisation list the server sends. And the copies of the encrypted organisation symmetric key are not authenticated in any way, so anyone can encrypt a chosen symmetric key under the public key of any user.

### BW08: Organisation Injection

Adding a user to an organisation therefore requires nothing but that user's public key, which the server already knows. The adversary creates a new organisation and encrypts its $k_{org}$ under the target user's public key; the client silently accepts the new organisation at the next sync. As a corollary, the adversary can also add arbitrary users to any organisation whose symmetric key it knows. The impact is a violation of vault integrity: organisation items are added to the user's vault, which supports framing attacks such as planting incriminating material, and which enables several later attacks, notably BW03 and BW09. The requirement is one sync operation, which the client performs automatically at startup, when the vault page is loaded, in response to some user actions, and on server-generated events.

### BW09: Organisation Overwrite

As soon as an organisation is created, the creator's client syncs to fetch the latest data from the server, and as part of that the keys of the newly created organisation are fetched. Once the sync completes, the creator can decrypt the organisation symmetric key with their private RSA key and use it to read all organisation data. The adversary can intervene in this window: applying the same method as in BW08, it swaps the encrypted symmetric key $c_{org}$ and the organisation data for values it controls, and the client has no way to distinguish such a malicious key from a legitimate one at sync. Unlike BW08, which creates a new organisation, this attack is entirely undetectable. An adversary can also overwrite an organisation later, but doing so deletes any pre-existing organisation items. The impact is that the adversary can read and modify all items in the newly created organisation; the requirement is that the user creates an organisation.

## LastPass: shared folders

LastPass implements sharing through shared folders. A user who first shares an item has their client sample a 32-byte shared folder key $k_{shr}$, which then encrypts the items in the folder using AES-CBC. The folder key is itself encrypted with RSA-OAEP under the public key of every user the folder is shared with.

### LP07: Sharing Key Overwrite

During an item-sharing operation, the server, acting as the adversary, returns an adversary-controlled recipient RSA public key in place of the intended recipient key. Neither the client nor the user can tell the malicious key from the intended one: the recipient RSA public keys are not authenticated, the user interface offers no out-of-band verification of key fingerprints, and no key transparency is in place. The impact is that the adversary can read and modify all the items in a shared folder; the requirement is that the user shares an item with any recipient.

## Dashlane: user and group sharing

Dashlane also uses public-key encryption for sharing, so the unauthenticated-key problem of LP07 applies to it as well. When a client shares an item with a user or in a group, it samples a fresh symmetric sharing key $k_{shr}$. For user-to-user sharing $k_{shr}$ encrypts the shared item directly; for group sharing it encrypts the group keys, which in turn protect the shared items. Either way, the sharing client retrieves the RSA public keys of the recipients from the server and, without verifying their authenticity, encrypts $k_{shr}$ under each recipient's public key, yielding $c_{shr}^{user}$ for each recipient. Each such ciphertext is sent to the server for storage.

### DL02: Sharing Key Overwrite

When the sharing client asks for a recipient's public key, the adversary can overwrite it with an RSA key $pk^{adv}$ that it controls, so that $k_{shr}$ ends up encrypted under the malicious public key. The resulting ciphertext $c_{shr}^{adv}$ is then delivered to the adversary, who decrypts it with $sk^{adv}$ and recovers $k_{shr}$. That key in turn gives access to the shared items it protects. The impact is that the adversary can read and modify all shared items; the requirement is that the user shares an item with any recipient.

## One cause, four attacks

All four attacks trace to the same two causes. Table 1 records "Lack of Key Auth" for each of them, and adds "Key Substitution" for BW09, LP07 and DL02.

| Ref | Name | Cause | Impact | Interaction | Mitigations |
| --- | --- | --- | --- | --- | --- |
| BW08 | Organisation Injection | Lack of Key Auth | Add users to arbitrary orgs | 1 sync | SC |
| BW09 | Organisation Overwrite | Lack of Key Auth, Key Substitution | Organisation compromise † | 1 join | PKA, SC |
| LP07 | Sharing Key Overwrite | Lack of Key Auth, Key Substitution | Shared vault compromise † | 1 join | PKA |
| DL02 | Sharing Key Overwrite | Lack of Key Auth, Key Substitution | Shared vault compromise † | 1 join | PKA |

The table's dagger marks the attacks that recover encrypted passwords. BW08 breaks integrity only: it plants items in a vault but reads nothing. BW09, LP07 and DL02 give the adversary both read and modify access to the data in scope — the new organisation, the shared folder, the shared items — so they break confidentiality as well as integrity and recover the shared secrets' plaintext. None of the four recovers a master password directly, but BW09 is a pivot rather than an end in itself: full control of a newly created organisation feeds the Key Escrow class, where account takeover is achieved.

Table 1 also names the fix. Public-key authentication (PKA) — caching known public keys in the vault after an optional out-of-band check, or a certificate authority outside the password manager's own server — removes LP07 and DL02, and also covers the public keys of admins and organisations used for escrow. BW09 needs PKA together with ciphertext authentication (SC), because the client must also be able to tell that a ciphertext claiming to be an organisation invite was produced by the user themself; signcryption, or replacing public-key encryption with symmetric authenticated encryption, achieves that. BW08 yields to SC alone.

## Key points

- All three managers implement sharing by encrypting a per-share symmetric key ($k_{org}$ in Bitwarden, $k_{shr}$ in LastPass and Dashlane) under the RSA public keys of the recipients, and none of them authenticates those public keys.
- BW08 (Organisation Injection) lets the adversary add users to arbitrary organisations, violating vault integrity and enabling BW03 and BW09; it needs only one automatic sync.
- BW09 (Organisation Overwrite) swaps the encrypted organisation key of a freshly created organisation for an adversary-chosen value, is entirely undetectable, and gives the adversary read and modify access to the whole new organisation.
- LP07 lets a malicious server substitute the recipient's public key during sharing so that the adversary can read and modify every item in a shared folder.
- DL02 does the same for Dashlane, and additionally lets the adversary recover $k_{shr}$ itself by decrypting $c_{shr}^{adv}$ with $sk^{adv}$.
- BW08 breaks integrity alone, while BW09, LP07 and DL02 also break confidentiality and recover the shared data's plaintext, with BW09 the pivot into the Key Escrow class.
- The remedies Table 1 gives are public-key authentication (PKA) and ciphertext authentication (SC), the latter realised as signcryption or as symmetric authenticated encryption.

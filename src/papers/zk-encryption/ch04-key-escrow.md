# Attacks I — key escrow

An end-to-end encrypted (E2EE) password manager protects the vault ciphertext easily enough; the difficulty lies in the extra features, which need real protocols between client and server. The attacks fall into four categories by cause.

## The four attack categories

**Key escrow.** A forgotten master password is fatal in an E2EE manager: the server holds only ciphertext, so the vault is lost irrecoverably. Most managers therefore offer account recovery through key escrow, an administrator holding a key pair that can hand a user's vault contents back — and attacking that mechanism normally yields the whole vault. Section 4.1 breaks vault confidentiality in Bitwarden and LastPass through flaws in their escrow designs, and notes a weakness in Dashlane's. The property at stake is that recovery offered to some users must not weaken a user who never opted in.

**Item-level vault encryption.** Items and settings are encrypted separately, often with unencrypted or unauthenticated metadata, because re-encrypting the whole vault on every small change would be too costly. That is in tension with vault integrity: items can be swapped, removed or reordered and settings such as the KDF iteration count changed, undetected. Section 4.2 finds such attacks on all three managers, many also breaking confidentiality.

**Sharing.** Sharing features for families and businesses let several people reach common credentials, and are widely used. Section 4.3 attacks the sharing features of all three targets, affecting integrity and confidentiality alike, and an organisation is also how Bitwarden first reaches a user's key.

**Backwards compatibility.** All three managers changed their cryptography over time while keeping compatibility with older clients. Legacy code paths let a malicious server drive a client into a weaker state even when the user runs the newest version, for instance downgrading it to unauthenticated encryption; Section 4.4 builds downgrade attacks on Bitwarden and Dashlane.

The adversary throughout is an entity with full control of the server, and unless stated otherwise an attack affects every client listed for that product in Table 2 of the full version. Proof-of-concept testing covered only Bitwarden's web client and the LastPass and Dashlane browser extensions.

The conference talk opens with key recovery: a master password that cannot be remembered is the everyday event that recovery exists for.

### Analysis method

The analysis follows the "attack" branch of the "Cryptography in the Wild" methodology. It began with white-papers and client code, plus server code where available, starting from Bitwarden, whose source availability made its architecture and protocols easiest to model, and aimed from the outset at a malicious or compromised server, refined into a concrete adversarial model. For each feature, pseudo-code models of the main cryptographic actions were analysed for attacks, drawing on the literature on E2EE cloud storage under a malicious server and standard vectors such as padding oracles and key overwriting; each attack was then implemented as a proof of concept and tested against the relevant client. Dashlane and LastPass went through the same process, with some reverse engineering of minified client JavaScript and of the Android apps, and the attacks were classified into the four categories. Absent a formal analysis, the authors state, their set of attacks must be considered incomplete.

## Table 1: summary of attacks

| Class | Ref | Name | Cause | Impact | Interaction | Mitigations |
| --- | --- | --- | --- | --- | --- | --- |
| Key escrow | BW01 | Malicious Auto-Enrolment | Lack of Key Auth, Key Substitution | Full vault compromise † | 1 join | PKA, SC |
| Key escrow | BW02 | Malicious Key Rotation | Key Substitution | Full vault compromise † | 1 rotation | SC |
| Key escrow | BW03 | Malicious KC Conversion | Lack of Key Auth, Key Substitution | Full vault compromise † | 1 dialog | PKA, SC |
| Key escrow | LP01 | Malicious Password Reset | Lack of Key Auth | Full vault compromise † | 1 login | PKA, SC |
| Item-level vault encryption | BW04 | Unprotected Item Metadata | Lack of Auth Enc | Read and modify metadata | - | AE, AD |
| Item-level vault encryption | BW05 | Item Field Swapping | Lack of Key Sep | Field and item swapping | - | KS |
| Item-level vault encryption | BW06 | Icon URL Item Decryption | Lack of Key Sep | Loss of confidentiality † | 1 open | KS |
| Item-level vault encryption | BW07 | Remove KDF Iterations | Lack of Auth Enc | No brute-force protection | 1 login | AD |
| Item-level vault encryption | LP02 | Item Field Swapping | Lack of Auth Enc | Field and item swapping | - | KS, AE |
| Item-level vault encryption | LP03 | Icon URL Item Decryption | Lack of Key Sep | Loss of confidentiality † | 1 open | KS, AE |
| Item-level vault encryption | LP04 | Remove KDF Iterations | Lack of Auth Enc | No brute-force protection | 1 login | AD |
| Item-level vault encryption | LP05 | Malleable Vault | Lack of Auth Enc | Loss of vault integrity | - | AE |
| Item-level vault encryption | LP06 | Unprotected Item Metadata | Lack of Auth Enc | Read and modify metadata | - | AD, AE |
| Item-level vault encryption | DL01 | Transaction Replay | Lack of Key Sep | Loss of vault integrity | - | KS |
| Sharing | BW08 | Organisation Injection | Lack of Key Auth | Add users to arbitrary orgs | 1 sync | SC |
| Sharing | BW09 | Organisation Overwrite | Lack of Key Auth, Key Substitution | Organisation compromise † | 1 join | PKA, SC |
| Sharing | LP07 | Sharing Key Overwrite | Lack of Key Auth | Shared vault compromise † | 1 join | PKA |
| Sharing | DL02 | Sharing Key Overwrite | Lack of Key Auth | Shared vault compromise † | 1 join | PKA |
| Backwards compatibility | BW10 | Disable Per-Item Keys | Lack of Auth Enc | Downgrade key hierarchy | - | KS, AD |
| Backwards compatibility | BW11 | User Key Overwriting | CBC Support | Loss of confidentiality † | 2 logins | AE |
| Backwards compatibility | BW12 | Downgrade to Legacy | CBC Support | Full vault compromise † | 2 logins | AE |
| Backwards compatibility | DL03 | Item Injection | CBC Support | Loss of vault integrity | $10^4$ syncs | AE |
| Backwards compatibility | DL04 | Remove KDF Iterations | CBC Support | No brute-force protection | $10^4$ syncs | AE |
| Backwards compatibility | DL05 | CBC-Only Downgrade | CBC Support | Loss of confidentiality † | $10^5$ syncs | AE |
| Backwards compatibility | DL06 | Lucky 64 | CBC Support | No brute-force protection | $10^4$ syncs | AE |

Table 1: Summary of attacks, grouped by the password manager feature each exploits. BW, LP and DL denote Bitwarden, LastPass and Dashlane. The dagger marks an impact that includes recovery of encrypted passwords, and the interaction column gives what the malicious server needs from the client: synchronisation (sync), a login, opening the vault (open), joining an organisation (join) or a misleading dialog (dialog). The last column lists the mitigations from Section 5.

## 4.1 Key escrow

These attacks concern the key escrow functionalities that let an account be recovered when the master password is lost. Their consequences are severe: in most cases the adversary can recover the user's full vault. Mechanisms that keep the recovery data on the user's own devices are less powerful, and attacks on them are less impactful.

![Key hierarchies for Bitwarden (left), LastPass (centre) and Dashlane (right).](assets/fig1-key-hierarchies.png)

### 4.1.1 Bitwarden

Bitwarden supports two flavours of key escrow. The first, organisation account recovery, lets an organisation's administrators reset the master password of every member enrolled in recovery, either manually (self-enrolment) or automatically on joining (auto-enrolment). On enrolment the client fetches the organisation public key $pk_{org}$ from the server, encrypts the user key $k_u$ under it and sends the resulting account recovery ciphertext $c_{rec}$ to the server; two key recovery attacks follow. The second flavour, the "Key Connector" feature, is also vulnerable to a master key recovery attack (BW03), described in the full version. Recovery is restricted to paid "enterprise" organisations, but every client ships the feature's code and the attacks work regardless of subscription status.

**BW01: Malicious Auto-Enrolment.** When a Bitwarden user joins an organisation, the client fetches the organisation's name, key material and policies from the server, and this data is not integrity protected, so a server-controlled adversary can compromise a user as soon as the user accepts an invitation to join any organisation. On acceptance the client asks for the account recovery policy and the organisation's public key; the adversary sets auto-enrolment to true and replaces $pk_{org}$ with a malicious $pk^{adv}_{org}$ whose secret key $sk^{adv}_{org}$ it knows. Recovery being enabled, the client encrypts $k_u$ under $pk^{adv}_{org}$ and sends $c_{rec}$, which the adversary decrypts with $sk^{adv}_{org}$ to recover $k_u$ and with it read and modify access to all of the target's vault data. The user need only join some organisation, and the adversary need not control it: an honest invitation from a trusted enterprise or family member suffices. The compromise also spreads, since $sk_{org}$ is known to all members of an organisation: compromising one user yields it for every organisation that user belongs to and, where recovery is enabled, compromises all of their users too, repeating in worm-like fashion.

**BW02: Malicious Key Rotation.** Bitwarden lets users change their master password and optionally rotate their keys. On rotation the client samples a new user key $k_u'$ and encrypts it under the new extended master key $k_{em}'$. A user enrolled in recovery must also have the recovery ciphertext regenerated, so the client encrypts $k_u'$ under $pk_{org}$ and sends a new $c_{rec}'$. Crucially, $pk_{org}$ is not taken from the user's vault but obtained by a sync operation, and the organisation data returned is not authenticated: the adversary supplies a fresh $pk^{adv}_{org}$ with a known $sk^{adv}_{org}$ and sets recovery enrolment to true, and the client sends $c_{rec}'$ containing the new user key, which the adversary decrypts to obtain $k_u'$ and with it read and modify access to the vault. This works whether or not the user is in an organisation at the time, since BW08 or BW09 can add the user to a new organisation or overwrite an existing one's keys. The requirement is that the user rotate their keys.

### 4.1.2 LastPass

LastPass offers two forms of key escrow, account recovery and admin password reset, and the second matters here. Master password reset belongs to the paid enterprise products "business" and "teams", though the code is present in the client regardless of subscription status. Within a team, super admins can reset other members' master passwords, and each admin account has an RSA key pair $(sk_{adm}, pk_{adm})$. After a super admin initiates a reset, the selected user's client — at its next login in the LastPass browser extension — retrieves the admins and their public keys from the server, encrypts its user key $k_u$ under each $pk^i_{adm}$ and sends the ciphertexts back.

**LP01: Malicious Password Reset.** The client does not authenticate the admin public keys it retrieves, so an adversary can trivially inject its own $pk^{adv}_{adm}$ with a known $sk^{adv}_{adm}$ and recover $k_u$ from the ciphertext the client sends, gaining read and modify access to the whole vault. In theory only users in teams with reset enabled, and selected for a reset, should be affected; in practice the client queries the server at every login and sends recovery ciphertexts regardless of enrolment status. Only the browser extension supports this procedure, and the only requirement is that the user log in there.

### 4.1.3 Dashlane

The framing of Section 4.1 announces a weakness in Dashlane's design alongside the Bitwarden and LastPass attacks, but the published paper carries no Dashlane subsection under key escrow: like Bitwarden's Key Connector feature and several item-level attacks, it is deferred to the full version. The nearest Dashlane attack in the summary table is DL01 Transaction Replay, classed under item-level vault encryption. Dashlane's vault is a transactional database whose content is encrypted under a key derived from the master password, and no escrow mechanism for it appears in the published material.

## Key points

- The attacks fall into four categories by cause — key escrow, item-level vault encryption, sharing and backwards compatibility — and in all of them the adversary controls the server.
- Key escrow exists because a forgotten master password is otherwise fatal in an E2EE manager, and a successful attack on a recovery mechanism normally hands over the entire vault.
- Recovery for some users must not weaken users who never opted in, and that requirement fails: Bitwarden and LastPass fetch the escrow policy and the escrow public keys from the server unauthenticated.
- BW01 yields a Bitwarden user key as soon as the user accepts any organisation invitation and spreads worm-like to organisations sharing members; BW02 yields it again at key rotation.
- LP01 yields a LastPass user key because the client sends recovery ciphertexts to admin keys fetched at every login, whether or not the user enrolled.
- Of the 25 attacks in Table 1 only BW01, BW02, BW03 and LP01 are in the key escrow class, and the paper's announced Dashlane escrow weakness is left to the full version.

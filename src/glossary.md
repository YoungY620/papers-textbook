# Glossary

Terms used throughout this book, with the one-line gloss that appears when you hover a highlighted term in the text. Each entry also gives the section where the term is first introduced.

[A](#gloss-a) · [C](#gloss-c) · [D](#gloss-d) · [E](#gloss-e) · [F](#gloss-f) · [H](#gloss-h) · [I](#gloss-i) · [K](#gloss-k) · [L](#gloss-l) · [M](#gloss-m) · [O](#gloss-o) · [P](#gloss-p) · [R](#gloss-r) · [S](#gloss-s) · [T](#gloss-t) · [U](#gloss-u) · [V](#gloss-v) · [W](#gloss-w)

<a id="gloss-a"></a>

## A

<a id="term-access-sensitivity"></a>

**Access Sensitivity** — *访问敏感度*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

How much sensitive data an agent may reach, from none, to known sensitive data sources, to arbitrary sensitive data.

Higher levels make harder tasks possible but widen the scope of a breach, because the same flexibility that enables the task also determines how much a compromised agent can reach.


<a id="term-account-recovery"></a>

**account recovery** — *账户恢复*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

A feature that lets a user (or an administrator) regain access after forgetting the master password.

Recovery is where security and usability pull in opposite directions, and it is the feature the key escrow attacks exploit.


<a id="term-account-recovery-ciphertext"></a>

**account recovery ciphertext** — *账户恢复密文*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

The ciphertext c_rec the client sends when a user enrols in recovery, that is the user key encrypted under the organisation public key.

It sits on the server so that an administrator can hand the vault back after a forgotten master password; both Bitwarden attacks in §4.1 make the client send it under a public key the adversary controls.


<a id="term-account-recovery-policy"></a>

**account recovery policy** — *账户恢复策略*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

The organisation-side setting that says whether members are enrolled in recovery, and whether joining enrols them automatically.

The client fetches it from the server without integrity protection, which is what lets a malicious server turn auto-enrolment on for a user who never opted in.


<a id="term-action-space"></a>

**Action Space** — *动作空间*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

The set of operations an agent can perform through its tools, spanning three types — read, write, and execute.


<a id="term-aes-cbc-hmac"></a>

**AES-CBC-HMAC** — *AES-CBC-HMAC 认证加密*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

Encrypt-then-MAC with AES-CBC and an HMAC over the ciphertext; Bitwarden's construction, dropped to bare AES-CBC when no MAC key is present.


<a id="term-agent-design-dimensions"></a>

**Agent Design Dimensions** — *智能体设计维度*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

Seven axes — input trust, access sensitivity, workflow, action, memory, tool, user interface — characterizing an agent's design flexibility.

The dimensions are orthogonal, so one agent can sit at different levels on different axes at the same time.


<a id="term-agentic-ai-system"></a>

**Agentic AI System** — *智能体 AI 系统*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

A system that combines large language models with traditional software components so it can act autonomously and use tools.

Used interchangeably with "AI agent" throughout the source work; the unit of analysis is the whole system, not the model alone.


<a id="term-ai-agent"></a>

**AI Agent** — *AI 智能体*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

A hybrid software system combining traditional software components with neural components, which takes a user task and acts on it.


<a id="term-associated-data"></a>

**associated data** — *关联数据*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

Data that is authenticated along with a ciphertext but not encrypted, binding the ciphertext to its context.

Its absence is what makes item field swapping (BW05, LP02) possible: a field name is stored as plaintext JSON key and never authenticated together with the ciphertext under it.


<a id="term-attack-surface"></a>

**Attack Surface** — *攻击面*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

The set of interfaces through which an attacker can reach a system; on agents, external data, memory and third-party tools widen it.


<a id="term-attack-vector"></a>

**Attack Vector** — *攻击向量*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

A concrete route by which an attacker enters an agentic system and influences it, such as indirect prompt injection or tool poisoning.


<a id="term-auditable-key-directory"></a>

**auditable key directory** — *可审计密钥目录*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 10</span>

An append-only directory of account-to-key mappings that issues inclusion and history proofs so anyone can audit it.

It would not stop a malicious server associating the wrong key with a user, but it would make the tampering evident, which is how the paper frames its value for password managers.


<a id="term-authenticated-encryption"></a>

**authenticated encryption** — *认证加密*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

An encryption mode that also proves the ciphertext was not altered, unlike plain AES-CBC.


<a id="term-authenticated-encryption-ae"></a>

**Authenticated Encryption (AE)** — *认证加密*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

Encryption that also proves the ciphertext was not modified, so tampering is detected instead of silently decrypting.


<a id="term-authenticated-encryption-with-associated-data-aead"></a>

**Authenticated Encryption with Associated Data (AEAD)** — *关联数据认证加密*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

Authenticated encryption that also covers associated data left in the clear, such as PBKDF parameters.


<a id="term-auto-enrolment"></a>

**auto-enrolment** — *自动纳入*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

Enrolling a user in account recovery automatically when they join an organisation, with no user interaction.

Distinguished from self-enrolment, the manual variant. Attack BW01 works by flipping this flag on the server side.


<a id="gloss-c"></a>

## C

<a id="term-capability-based-security"></a>

**capability-based security** — *基于能力的安全*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

An access control mechanism in which holding an unforgeable capability token is what grants access, an alternative to RBAC and ABAC.


<a id="term-cbc-only-downgrade"></a>

**CBC-Only Downgrade** — *纯 CBC 降级*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Attack DL05, in which forged Dashlane settings make the client encrypt every later transaction in CBC-only mode, open to the padding oracle.


<a id="term-certificate-authority-ca"></a>

**Certificate Authority (CA)** — *证书颁发机构*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

A party that signs public keys; for password managers it must sit outside whoever controls the vault server.


<a id="term-ciphertext-authentication"></a>

**Ciphertext Authentication** — *密文认证*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

Proving who produced a ciphertext, which public-key encryption alone cannot do, since anyone can encrypt.


<a id="term-ciphertext-integrity"></a>

**ciphertext integrity** — *密文完整性*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

The property that an adversary cannot alter stored or transmitted ciphertext undetectably.


<a id="term-client-side-encryption"></a>

**client-side encryption** — *客户端加密*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

Encrypting data on the user's own device before it is sent to the server.


<a id="term-complete-mediation"></a>

**complete mediation** — *完全中介*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

The design principle that every access to a sensitive resource must be checked and validated, via monitoring and access control.

Reflected in monitoring that observes agent execution and in access control that verifies each interaction with a protected resource.


<a id="term-component-hardening"></a>

**Component Hardening** — *组件加固*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

Defense that strengthens an individual agent component, such as the model, memory, or a tool, against the attacks that target it.


<a id="term-consequence-risks"></a>

**Consequence Risks** — *后果类风险*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

R5, R6 and R7, whose severity comes from the Access Sensitivity, Action and User Interface dimensions rather than from whether they occur.

Private data leakage, unintended or unauthorized action and data corruption, and resource drain. Moving the Action dimension from response-only to execution converts information disclosure into environment corruption.


<a id="term-containerisation"></a>

**containerisation** — *容器化*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

An existing operating-system isolation mechanism that agent privilege separation can reuse to sandbox the external environment.


<a id="term-contextual-security"></a>

**contextual security** — *上下文安全*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

An agent-specific goal that an agent's contexts stay aligned with the user's intended task, avoiding instruction override and drift.


<a id="term-coordinated-credential-orchestration"></a>

**Coordinated Credential Orchestration** — *协同凭证编排*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 9</span>

The open need for standardised, centralised handling of agent secrets across a stack, including multiple agents, instead of ad hoc storage of keys in unencrypted environment variables.


<a id="term-coordinated-vulnerability-disclosure"></a>

**coordinated vulnerability disclosure** — *协同漏洞披露*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

Reporting flaws privately to a vendor and agreeing on a publication date before going public.

The paper follows this approach with a window of at least 90 days per vendor and a common public date of 14 February 2026.


<a id="term-credential-provisioning"></a>

**credential provisioning** — *凭证供给*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

How an agent obtains credentials, through single-sign-on or OAuth 2.0 authenticated delegation from the user.


<a id="term-cryptographic-agility"></a>

**cryptographic agility** — *密码敏捷性*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 9</span>

The practice of making sharp but clean breaking changes so past cryptographic attacks cannot resurface.

The paper contrasts it with the backwards compatibility that preserved early-2000s cryptography in password managers, and points to TLS's evolution as the model to follow.


<a id="gloss-d"></a>

## D

<a id="term-data-corruption"></a>

**Data Corruption** — *数据损坏*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

Unauthorized modification of stored resources such as files or databases, one of the two integrity failures grouped under R6.

R6 also covers unintended and unauthorized actions, which make irreversible state changes such as unauthorized purchases or arbitrary code execution. Memory poisoning can inject knowledge that corrupts later behavior.


<a id="term-data-origin-authentication"></a>

**Data-Origin Authentication** — *数据来源认证*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

A guarantee that a message came from a named sender, which no public-key encryption scheme can provide by itself.

Because any party can encrypt under a public key, no PKE scheme can offer it; the paper recommends signcryption to bind ciphertexts to their senders.


<a id="term-decision-fatigue"></a>

**decision fatigue** — *决策疲劳*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

The erosion of judgment caused by frequent validation prompts, which leads users to approve risky actions or reject benign ones.


<a id="term-declassification"></a>

**declassification** — *安全标签降级*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

The principled relaxation of a security label when safe, needed to keep label-creep-prone agents usable without losing security.


<a id="term-defense-in-depth"></a>

**Defense in Depth** — *纵深防御*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

A principle of layering multiple independent defenses so that no single failure of one protection lets an attack succeed.

Realised by input and output guardrails, information flow control, monitoring, access control, privilege separation, component hardening and human-in-the-loop validation.


<a id="term-design-anti-pattern"></a>

**design anti-pattern** — *设计反模式*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 9</span>

A recurring flawed design habit that produces vulnerabilities across independent products.

The paper names four families — a burdensome legacy of old cryptography, deceptive simplicity, integrity broken by incremental synchronisation, and unsafe sharing of public keys.


<a id="term-design-dimension"></a>

**Design Dimension** — *设计维度*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

One of seven axes along which an agent's design varies, each a continuum of flexibility from least to most flexible.

The dimensions are input trust, access sensitivity, workflow, action, memory, tool and user interface. They are orthogonal, so one agent can hold a different level on each of them at once, and higher flexibility on any of them amplifies security risk.


<a id="term-design-flexibility"></a>

**Design Flexibility** — *设计灵活性*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

How far an agent's design sits toward the flexible end of each dimension; greater flexibility generally amplifies security risk.


<a id="term-developer-defined-workflow"></a>

**Developer-Defined Workflow** — *开发者定义的工作流*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

A fixed action sequence written in advance by the agent's developers, the moderately flexible level of the workflow dimension.


<a id="term-direct-prompt-injection"></a>

**Direct prompt injection** — *直接提示注入*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

A malicious prompt sent straight to the agent by a user or user interface, instructing it to act against its system prompt.


<a id="term-disable-per-item-keys"></a>

**Disable Per-Item Keys** — *禁用条目级密钥*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Attack BW10, described in the paper's full version, which downgrades the key hierarchy so that items are encrypted under the user key again.


<a id="term-disclosure-window"></a>

**disclosure window** — *披露窗口*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 9</span>

The agreed period, here at least 90 days, during which an issue is kept from the public.

Disclosures began on 27 January 2025 for Bitwarden, 4 June 2025 for LastPass and 29 August 2025 for Dashlane, with a common public date of 14 February 2026; the LastPass clock was reset after its first email was lost.


<a id="term-downgrade-to-legacy"></a>

**Downgrade to Legacy** — *降级到旧格式*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Attack BW12, which forges a user key with no MAC half so that Bitwarden writes in CBC-only mode and a padding oracle becomes possible.


<a id="term-dynamic-credential-management"></a>

**dynamic credential management** — *动态凭证管理*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

Using time-limited tokens that expire automatically, shrinking the exposure window at the cost of complex renewal and interruptions.


<a id="gloss-e"></a>

## E

<a id="term-economy-of-mechanisms"></a>

**Economy of Mechanisms** — *机制经济性*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 9</span>

A security principle, named among further principles that also apply to agents, favouring the smallest set of mechanisms that achieves the protection, to keep the design auditable and maintainable.


<a id="term-enclave"></a>

**enclave** — *安全区*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 10</span>

A protected region inside a processor that keeps code and data hidden from the machine's operator, used to hold recovery keys.

Secure Value Recovery deliberately spreads trust over enclaves of different architectures, on the observation that an attacker is unlikely to break several of them at once.


<a id="term-encryption-type-attribute"></a>

**Encryption Type Attribute** — *加密类型属性*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

The unprotected prefix on each Bitwarden ciphertext: type 0 for authenticated encryption, type 1 for plain AES-CBC.

Because the attribute is prepended and not integrity-protected, a malicious server can mark a ciphertext so that the client takes the weaker AES-CBC path.


<a id="term-end-to-end-encryption"></a>

**end-to-end encryption** — *端到端加密*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

A design in which only the endpoints hold the keys, so the server handles ciphertext it cannot read.

Vendors of cloud storage and password managers often label this Zero Knowledge Encryption, which the paper treats as a claim to be tested rather than a property.


<a id="term-execution-action"></a>

**Execution Action** — *执行动作*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

An operation that modifies the environment rather than only reading it, the most flexible level of the action dimension.

Execution is where an agent's mistakes stop being textual: it is the point at which information disclosure becomes corruption of the environment.


<a id="term-extended-master-key"></a>

**extended master key** — *扩展主密钥*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

In Bitwarden, the 64-byte key k_em formed by concatenating the HKDF-Expand "enc" and "mac" outputs of the master key.

It encrypts the randomly sampled user key, so that the ciphertext c_u stored on the server can only be opened with the master password.


<a id="term-external-adversary"></a>

**External adversary** — *外部对手*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

An attacker with no access to the agent system who acts only by controlling resources the agent may retrieve, such as public web pages.


<a id="gloss-f"></a>

## F

<a id="term-fail-safe-defaults"></a>

**Fail-Safe Defaults** — *故障安全默认*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 9</span>

A security principle, named among further principles that also apply to agents, in which the default state on failure is to deny access rather than grant it.


<a id="term-flexibility-spectrum"></a>

**Flexibility Spectrum** — *灵活性连续谱*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

The range of settings a design dimension takes, illustrated by three representative levels: least, moderately and most flexible.


<a id="term-forced-migration"></a>

**forced migration** — *强制迁移*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

Shipping a client whose only job is to move a vault to the new format, so a breaking change reaches every user.


<a id="term-formal-verification"></a>

**formal verification** — *形式化验证*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Proving a property of a system from a formal model of it; for agents the model must capture stochastic behaviour to stay meaningful.


<a id="gloss-h"></a>

## H

<a id="term-hardware-security-module"></a>

**hardware security module** — *硬件安全模块*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 9</span>

Dedicated hardware that can hold keys and run operations that the server operator cannot tamper with.

The paper proposes implementing part of key escrow on HSMs, as Signal, WhatsApp and Apple's Advanced Data Protection do for recovery and backups, so the server offers some guarantee of honest behaviour.


<a id="term-hardware-security-module-hsm"></a>

**Hardware Security Module (HSM)** — *硬件安全模块*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

Tamper-resistant hardware that can hold recovery keys and give some assurance the server is behaving honestly.


<a id="term-heisenberg-attack"></a>

**Heisenberg Attack** — *海森堡攻击*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

The talk's name for the Bitwarden pair BW11 and BW12, because each direction costs the adversary one of integrity or confidentiality.


<a id="term-heterogeneous-untrusted-interfaces"></a>

**Heterogeneous Untrusted Interfaces** — *异构不可信接口*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

The external data sources, persistent memory stores and third-party tools of varying trust that an agent exposes as attack entry points.

Named R1. Every one of the six attack vectors V1-V6 enters the system through one of these interfaces, which makes R1 the precondition for the other risks rather than an incident in itself.


<a id="term-horizontal-privilege-separation"></a>

**horizontal privilege separation** — *横向权限分离*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Privilege separation between parallel sub-agents at disjoint access scopes, as when IsolateGPT spawns one agent per mobile application.


<a id="term-human-in-the-loop-validation"></a>

**human-in-the-loop validation** — *人在回路验证*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

A defense in which the agent requests user approval before high-risk actions, giving the user control over security decisions.

The SoK treats it as comparatively unique to agents, mitigates R5-R7, and designs it along validation scope, alert content and recurrence policy. Its stated limitations are decision fatigue and a mismatch between the security literacy alerts assume and what users have.


<a id="gloss-i"></a>

## I

<a id="term-icon-url-item-decryption"></a>

**icon URL item decryption** — *图标 URL 条目解密*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

Leaking a decrypted item field by putting its ciphertext in the URL field the client uses to fetch an icon.

Attacks BW06 (Bitwarden, which sends the domain and top-level domain and requires a URL-shaped plaintext) and LP03 (LastPass, which sends the stored URL itself with no plaintext conditions).


<a id="term-identity-and-access-management"></a>

**identity and access management** — *身份与访问管理*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

Covering identity management, access control and credential management, to ensure authenticated entities and authorised access.


<a id="term-indirect-prompt-injection"></a>

**Indirect prompt injection** — *间接提示注入*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

Instructions hidden in content the agent retrieves, such as a web page, document or email, which the model then follows as commands.

The SoK classifies it as vector V1, an external adversary's vector. Greshake et al. established it and InjecAgent benchmarked it; it assumes the agent reads attacker-reachable content, which is the "arbitrary external data" end of the input trust dimension.


<a id="term-information-flow-control"></a>

**information flow control** — *信息流控制*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

A technique that labels each datum, propagates the labels through the system, and blocks flows that violate the label constraints.

In agents it addresses unconstrained data flow (R3) and downstream leakage (R5) and corruption (R6). PFI, CaMeL and FIDES replace tool results with trackable variables; CaMeL solves 77% of AgentDojo tasks with provable security against 84% undefended. The SoK's stated gap is runtime cost and label creep.


<a id="term-information-flow-lattice"></a>

**information flow lattice** — *信息流格*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

A predefined partial order of security labels from which information flow control draws each datum's label and allowed propagation.


<a id="term-injection-attack"></a>

**injection attack** — *注入攻击*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 10</span>

An attack in which the adversary controls only their own client, injects payloads into a victim's client, then observes protected state.

Fábrega et al. use sharing to inject payloads and observe encrypted vault exports or server traffic, backing out passwords, URLs, usernames and attachments. The malicious party is the client, not the server.


<a id="term-input-guardrail"></a>

**input guardrail** — *输入护栏*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

A first-line defense that validates inputs before they reach the agent, filtering malicious instructions and data from untrusted sources.


<a id="term-input-trust"></a>

**Input Trust** — *输入信任*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

How trustworthy the external data sources an agent relies on are; it runs from no external data to arbitrary, potentially untrusted sources.

The highest-trust setting uses no external data; the most flexible setting accepts arbitrary external data. Indirect prompt injection is only reachable on this dimension once the agent consumes external content.


<a id="term-internal-adversary"></a>

**Internal adversary** — *内部对手*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

An attacker with access to agent components such as the model or memory, as developer or component provider; the paper's hardest attack.


<a id="term-interoperable-identity"></a>

**Interoperable Identity** — *可互操作的身份*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 9</span>

The missing capability for agent identities to be issued, delegated and revoked across platforms under common taxonomies, so that agent actions stay auditable and accountable.

Without standard frameworks, platforms implement incompatible credential issuance, delegation and revocation flows that are hard to audit or federate.


<a id="term-item-field-swapping"></a>

**item field swapping** — *条目字段交换*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

Moving a ciphertext from one field of an item to another, or between items, because nothing binds it to its field.

Attacks BW05 and LP02. It is the base gadget for the icon URL decryption attacks, which need a secret field moved into the URL field.


<a id="term-item-injection"></a>

**Item Injection** — *条目注入*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Attack DL03, which uses the Dashlane encrypt oracle DLb2 to forge arbitrary transactions, including Setting transactions.


<a id="term-item-level-vault-encryption"></a>

**item-level vault encryption** — *条目级保险库加密*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

Storing and encrypting each vault item separately instead of encrypting the whole vault as one object.

It makes partial synchronisation cheap, because editing one item does not require re-encrypting the vault, but it removes any cryptographic guarantee over the vault as a whole.


<a id="term-iteration-count"></a>

**iteration count** — *迭代次数*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

How many times a key-derivation function repeats, which sets the cost of guessing a password.

A malicious server can lower it, removing brute-force protection; the paper's BW07 and DL03 attacks do exactly this.


<a id="gloss-k"></a>

## K

<a id="term-kdf-iteration-count"></a>

**KDF iteration count** — *KDF 迭代次数*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

The parameter that sets how expensive a password-based key derivation is, and therefore how expensive guessing is.

Attacks BW07 and LP04 lower it because the settings are stored unencrypted and unauthenticated on the server; the derived hash the client sends at login then costs almost nothing to check.


<a id="term-key-authentication"></a>

**key authentication** — *密钥认证*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

Establishing that a public key delivered by the server really belongs to the party it claims to represent.

The attacks in this chapter exist because Bitwarden and LastPass never do it; both take the escrow public keys from the server on trust, which Table 1 records as "Lack of Key Auth".


<a id="term-key-commitment"></a>

**key commitment** — *密钥承诺*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 10</span>

A property asking that a ciphertext decrypt under only one key, so nobody can open it to two different messages.

The paper itself does not raise key commitment, and none of the works surveyed here give it a role in this setting, so it is on the list of unaddressed properties.


<a id="term-key-rotation"></a>

**key rotation** — *密钥轮换*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

Replacing a user key with a freshly sampled one, optionally offered by Bitwarden when the master password changes.

Rotation forces the client to regenerate the account recovery ciphertext, and the organisation key it uses for that is fetched from the server, which is the opening for attack BW02.


<a id="term-key-separation-ks"></a>

**Key Separation (KS)** — *密钥分离*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

Deriving a distinct key per item and per field, so one key can never stand in for another.


<a id="term-key-substitution"></a>

**key substitution** — *密钥替换*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

An attack that swaps a victim's public key for the attacker's, so later traffic is encrypted to the attacker.


<a id="term-key-transparency"></a>

**Key Transparency** — *密钥透明*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

The talk's proposed fix for sharing: a public, auditable record of public keys, so that a substituted key can be detected.

The talk recommends key transparency for public key authentication in sharing, alongside HSMs for key escrow and key separation for partial vault synchronisation.


<a id="term-key-wrapping"></a>

**key wrapping** — *密钥封装*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

Encrypting one key under another, so the wrapped key can be stored or transported in the clear.


<a id="term-known-plaintext-oracle-gadget"></a>

**Known Plaintext Oracle Gadget** — *已知明文预言器*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Attack BWb1, which uses Bitwarden's keypair-generation path to obtain AES-CBC encryptions of known plaintexts under the unknown master key.


<a id="gloss-l"></a>

## L

<a id="term-label-creep"></a>

**label creep** — *标签蔓延*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

Conservative label propagation so restrictive that the agent becomes unusable unless safe declassification rules exist.

The SoK names it as an open problem for agent information flow control, alongside runtime overhead; closing it requires principled declassification rules that relax labels only when it is safe.


<a id="term-llm-defined-workflow"></a>

**LLM-Defined Workflow** — *大模型定义的工作流*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

An action sequence composed at run time by the model rather than fixed in advance, the most flexible level of the workflow dimension.

Flexible control flow is what lets an agent adapt to tasks it was not written for, and it is also what gives injected content more opportunity to hijack the agent's reasoning.


<a id="term-log-granularity"></a>

**log granularity** — *日志粒度*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

How coarse or fine an agent's activity log is; finer logs detect more but cost more storage, computation and privacy.


<a id="gloss-m"></a>

## M

<a id="term-malicious-data-injection"></a>

**Malicious data injection** — *恶意数据注入*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

Attacker-supplied data rather than instructions, such as a hallucinated package name, that harms when a sensitive operation consumes it.


<a id="term-master-password-reset"></a>

**master password reset** — *主密码重置*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

The LastPass enterprise feature that lets a super admin reset a team member's master password.

The selected user's client encrypts its user key under each admin's RSA public key, and the browser extension is the only client that supports this key exchange, which is the setting for attack LP01.


<a id="term-master-password-protected-password-management-protocol"></a>

**master-password-protected password management protocol** — *主密码保护的密码管理协议*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 10</span>

The client-server interaction of a password manager, in which one master password authenticates the user and unwraps the vault.

Duan, Wang and Fu recover the de facto protocols of 43 managers and formalise them as ideal functionalities in the universal composability framework.


<a id="term-memory-poisoning"></a>

**Memory poisoning** — *记忆投毒*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

Direct manipulation of the agent's persistent memory to inject content, alter behaviour or leak data; the write survives across sessions.

Vector V6, the SoK's internal-adversary vector. AgentPoison backdoors memory or RAG bases at a poison rate below 0.1% with at least 80% success, PoisonedRAG corrupts a knowledge base, and MINJA reaches the same effect through query-only interaction.


<a id="term-memory-separation"></a>

**memory separation** — *内存分离*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Creating separate memory spaces so that a lower-privilege component cannot read the sensitive data held by another component.


<a id="term-merkle-tree"></a>

**Merkle Tree** — *默克尔树*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

A hash structure that authenticates the whole vault, used to block selective deletion attacks.


<a id="term-mitre-atlas"></a>

**MITRE ATLAS** — *MITRE ATLAS*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

A public knowledge base of adversary tactics and techniques against AI systems; Appendix A maps the paper's attack vectors onto it.


<a id="term-model-context-protocol"></a>

**Model Context Protocol** — *模型上下文协议*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 10</span>

An open protocol to define, discover and invoke external tools, with schema negotiation and bi-directional channels, making tools portable.

The SoK notes tools may be implemented through such protocols; being standardised makes the discovery channel an attack surface. Hou et al. enumerate sixteen threat scenarios including tool poisoning, and ETDI, MCP Context Protector and MCIP are the hardening responses.


<a id="term-model-context-protocol-mcp"></a>

**Model Context Protocol (MCP)** — *模型上下文协议*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

A standardized protocol through which tools can be implemented and made available to an agent.


<a id="term-model-poisoning"></a>

**Model poisoning** — *模型投毒*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

Hidden malicious behaviour embedded in the model itself by its provider or supply chain, so that it acts against the user or leaks data.


<a id="term-model-risks"></a>

**Model Risks** — *模型风险*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

The paper groups R2, R3 and R4 as model risks, the ones the Workflow design dimension primarily drives.

Wrong instruction following, unconstrained data flow and hallucination. They sit in the middle of the cascade: an expanded attack surface lets attacker-controlled data reach and exploit them, and they in turn amplify the consequence risks.


<a id="term-monitoring"></a>

**monitoring** — *监控*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

System-wide visibility over inputs, outputs and intermediate states, used to surface distributed threats that no single action reveals.


<a id="gloss-o"></a>

## O

<a id="term-oblivious-client-operations"></a>

**oblivious client operations** — *不经意客户端操作*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

The goal that a client performs its work without revealing what it is accessing to the server.


<a id="term-offline-guessing-attack"></a>

**offline guessing attack** — *离线猜测攻击*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 10</span>

Guessing a master password from data the adversary already holds, without touching the live service, so rate limits do not apply.

Duan et al. split these into four types by adversary knowledge and find 38 of 43 managers vulnerable to at least one, showing single-master-password designs lean on slow hashing and password entropy.


<a id="term-organisation-injection"></a>

**Organisation Injection** — *组织注入*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

Attack BW08, in which anyone can add a user to a new organisation by encrypting the organisation key under that user's public key.


<a id="term-organisation-key"></a>

**organisation key** — *团队密钥*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

The 64-byte symmetric key k_org that encrypts the items of a Bitwarden organisation; membership means being able to recover it.


<a id="term-organisation-overwrite"></a>

**Organisation Overwrite** — *组织覆写*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

Attack BW09, in which the server swaps the encrypted organisation key and data of a freshly created organisation for values it controls.


<a id="term-organisation-private-key"></a>

**organisation private key** — *组织私钥*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

The secret half sk_org of a Bitwarden organisation's key pair, known to every member of that organisation.

Because every member knows it, compromising one user reveals sk_org for all of that user's organisations, which is how attack BW01 spreads in a worm-like fashion.


<a id="term-organisation-public-key"></a>

**organisation public key** — *组织公钥*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

The public key pk_org under which a Bitwarden client encrypts the user key when a member enrols in account recovery.

The client obtains it from the server and does not authenticate it, so a malicious server substitutes its own key and decrypts the recovery ciphertext.


<a id="term-organisation-rsa-keypair"></a>

**Organisation RSA Keypair** — *组织 RSA 密钥对*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

The recovery keypair (pk_org, sk_org) that Bitwarden creates with an organisation; its private key is encrypted under k_org to form c_skOrg.


<a id="term-organisation-symmetric-key"></a>

**Organisation Symmetric Key** — *组织对称密钥*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

The 64-byte key k_org with which Bitwarden encrypts items shared in an organisation, stored encrypted under each member's RSA public key.

A client decides that a user is an organisation member exactly when it can obtain k_org, and nothing binds the vault to the organisation list the server sends.


<a id="term-orthogonal-dimensions"></a>

**Orthogonal Dimensions** — *正交维度*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

The property that the design dimensions can coexist in one agent, which may hold different levels on different dimensions.

Orthogonality means an agent can be at the most flexible level on all seven dimensions at once; it does not mean the dimensions are independent in effect, since the tool dimension enables the action dimension.


<a id="term-output-guardrail"></a>

**output guardrail** — *输出护栏*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

A check on an agent's outward behavior such as user responses and tool usages, validating alignment and safe tool use.


<a id="term-over-tainting"></a>

**over-tainting** — *过度污点标记*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

Marking more data as untrusted than necessary, which variable-based taint tracking mitigates by replacing data with trackable variables.


<a id="gloss-p"></a>

## P

<a id="term-package-hallucination"></a>

**Package hallucination** — *软件包幻觉*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

A model limitation in which code-generating LLMs invent package names; attackers register those names to plant malicious packages.

Spracklen et al. measured at least 5.2% hallucinated packages for commercial models and 21.7% for open-source ones over 576,000 samples, with 205,474 unique names. The SoK files it both as data injection (V2) and as exploitation of hallucination (R4).


<a id="term-payload-format"></a>

**Payload Format** — *payload 格式*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

The leading string of a Dashlane transaction that names its key derivation function, cipher and mode; KWC3 is legacy, Flexible is current.


<a id="term-payload-string"></a>

**payload string** — *载荷字符串*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

The first bytes of a Dashlane transaction content, naming the KDF, its parameters, the cipher and the cipher mode.


<a id="term-per-item-key"></a>

**per-item key** — *逐条目密钥*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

A key sampled for one vault item and itself encrypted under the user key, used by Bitwarden for items created since version 2024.2.0.

Introduced in Bitwarden v.2024.2.0 as k_u^i. Old items are not migrated, so a vault can contain items encrypted directly under the user key and items encrypted under per-item keys at the same time.


<a id="term-persistent-cross-session-memory"></a>

**Persistent Cross-Session Memory** — *跨会话持久记忆*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

Memory that survives beyond a single session, the most flexible level of the memory dimension.

Persistence creates a poisoning target that keeps influencing later behaviour, and accumulates sensitive data that outlives the interaction that produced it.


<a id="term-planner-parser-separation"></a>

**planner–parser separation** — *规划器—解析器分离*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Splitting an agent's LLM use into tool call planning and tool result parsing, so that external data cannot steer planning decisions.


<a id="term-principle-of-least-privilege"></a>

**Principle of Least Privilege** — *最小权限原则*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 9</span>

The design principle that an agent should operate with the minimal permissions and access rights its task requires, so that a compromise cannot reach beyond that task.

Implemented through privilege separation techniques that isolate agent components and restrict tool access.


<a id="term-private-data-leakage"></a>

**Private Data Leakage** — *私有数据泄露*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

Unauthorized access to user conversations, persistent memory, credentials or environment resources through how those components interact.

Named R5, a confidentiality failure and the risk R3 most directly enables. Patterns include sending data to attacker-controlled servers, leaking through automatically fetched URL parameters, and abusing SSRF, XSS, path traversal or SQL injection.


<a id="term-privilege-separation"></a>

**privilege separation** — *权限分离*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Assigning different privilege levels to components and isolating them, so an attacker who controls one cannot reach the others.

In agents it mitigates wrong instruction following (R2) and unconstrained data flow (R3). The SoK names the shared axis the papers leave implicit — vertical separation on the planner–parser line versus horizontal separation by application or scope, as in IsolateGPT's per-application agents.


<a id="term-prompt-injection"></a>

**Prompt Injection** — *提示注入*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

An attack in which attacker-supplied content is crafted to make an agent follow malicious instructions instead of the intended ones.

Direct injection arrives as the user's own input; indirect injection arrives through external data the agent retrieves, such as a web page or document.


<a id="term-prompt-stealing-attack"></a>

**Prompt Stealing Attack** — *提示窃取攻击*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

An attack that extracts system prompts, tool descriptions or configurations encoding proprietary knowledge from a deployed model or agent.

In agentic systems this targets the agent developer and tool providers rather than the end user. Published work covers text-to-image generation models and real-world prompt services, both at USENIX Security.


<a id="term-proxy-delegation"></a>

**proxy delegation** — *代理委托*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

Letting an agent act for a user through an intermediary service or token, one of the three delegation models the paper lists.


<a id="term-public-key-authentication-pka"></a>

**Public-Key Authentication (PKA)** — *公钥认证*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

Binding a public key to its owner, by certificates, trust-on-first-use or a verified key directory.


<a id="term-pushdown-automaton"></a>

**pushdown automaton** — *下推自动机*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

The machine Formal-LLM uses to encode developer-defined plan constraints such as required tool orderings, restricting plan generation.


<a id="gloss-r"></a>

## R

<a id="term-rag-poisoning"></a>

**RAG poisoning** — *检索增强生成投毒*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

Corrupting the knowledge a retrieval-augmented agent draws on, so that poisoned entries are retrieved and acted on later.


<a id="term-resource-drain"></a>

**Resource Drain** — *资源耗尽*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

Costly API calls, forced infinite loops or excessive memory use that make an agent and its external systems unusable or unaffordable.

Named R7, the availability risk. It is measured economically as much as operationally, since the same autonomy that makes an agent useful lets an attacker spend someone else's budget.


<a id="term-retrieval-capability"></a>

**Retrieval Capability** — *检索能力*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

Read-only access to the external environment, the middle level of the action dimension between responding and executing.


<a id="term-retrieval-tool"></a>

**Retrieval Tool** — *检索工具*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

A tool giving an agent read-only access to the external environment, such as searching or reading a file, rather than modifying it.


<a id="term-risk-amplification"></a>

**Risk Amplification** — *风险放大*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

The cascading process in which an expanded attack surface feeds model risks, which in turn amplify the consequence risks.

R1 increases the entry points for attacker-controlled data, which reach and exploit R2, R3 and R4; those then amplify R5, R6 and R7. The cascade is why component-level defenses are insufficient and system-level defense-in-depth is required.


<a id="term-risk-taxonomy"></a>

**Risk Taxonomy** — *风险分类*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

The component-organised catalogue of agent security risks, R1 to R7, onto which the design dimensions map.

R1 heterogeneous untrusted interfaces, R2 wrong instruction following, R3 unconstrained/unsafe data flow and R4 hallucination and model mistakes are the model-side risks; R5 private data leakage, R6 unintended/unauthorized action and data corruption, and R7 resource drain and denial of service are the consequence risks.


<a id="term-roll-back-attack"></a>

**roll-back attack** — *回滚攻击*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 10</span>

Replaying an older, validly signed or encrypted vault version to undo changes or revive revoked access.

The paper finds that Merkle-tree authentication blocks selective deletion but cannot rule out complete roll-back without a trusted third party holding versioning information or local cryptographic state.


<a id="term-rsa-oaep"></a>

**RSA-OAEP** — *RSA-OAEP 加密*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

RSA encryption with OAEP padding, used to wrap symmetric keys under a recipient's public key in LastPass and Bitwarden.


<a id="term-rule-circuit"></a>

**rule circuit** — *规则电路*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

ShieldAgent's declarative encoding of external policy documents into circuits over action trajectories, used to enforce policy compliance.


<a id="term-runtime-protection"></a>

**Runtime Protection** — *运行时防护*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

Defense mechanisms that enforce security during agent execution, detecting real-time threats and behaviors as the agent acts.

Covers input guardrails, output guardrails, information flow control and taint tracking, monitoring, and human-in-the-loop validation.


<a id="gloss-s"></a>

## S

<a id="term-sandboxing"></a>

**sandboxing** — *沙箱化*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Confining a tool or environment to a restricted execution copy, as PFI does when it switches tools between normal and sandbox versions.


<a id="term-secure-by-design"></a>

**Secure by Design** — *安全设计*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

Defense that builds security into an agent's structure and design choices rather than adding it at run time.


<a id="term-secure-value-recovery"></a>

**Secure Value Recovery** — *安全值恢复*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 10</span>

Signal's PIN-based key recovery system, layered across several enclaves and cloud providers so no single one can recover a secret.

Connell et al. report that it limits PIN guesses unconditionally inside enclave memory, with rollback protection, which is the property the paper wants from hardware-backed key escrow.


<a id="term-security-label"></a>

**security label** — *安全标签*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

The per-datum marker in information flow control that records its trust or secrecy level and governs which flows are permitted.


<a id="term-security-risk-taxonomy"></a>

**Security Risk Taxonomy** — *安全风险分类法*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

The seven-item map (R1-R7) that keys each agent security risk to the component an attacker can target.

The taxonomy is organized by components rather than by severity, so one incident usually exercises several entries at once. R1 heterogeneous untrusted interfaces; R2 wrong instruction following; R3 unconstrained/unsafe data flow; R4 hallucination and model mistakes; R5 private data leakage; R6 unintended/unauthorized action and data corruption; R7 resource drain and denial of service.


<a id="term-self-enrolment"></a>

**self-enrolment** — *手动纳入*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

Enrolling in account recovery as a manual step that requires the user to act.

The alternative to auto-enrolment; a user who never takes this step should not be affected by recovery at all.


<a id="term-self-hosting"></a>

**self-hosting** — *自托管*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

Running the server component of a product on your own infrastructure instead of the vendor's.

Some password managers let an organisation self-host the storage element; in the paper's threat model the malicious server is then the customer's own server.


<a id="term-server-side-request-forgery"></a>

**Server-Side Request Forgery** — *服务端请求伪造*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

A domain-specific vulnerability (SSRF) that agents can be manipulated into using to reach protected internal resources.

Listed alongside XSS, path traversal and SQL injection as an abuse pattern behind private data leakage (R5), where the agent's automatic URL fetching turns into a request to an attacker-chosen address.


<a id="term-shadowing-attack"></a>

**shadowing attack** — *遮蔽攻击*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

An attack in which a malicious tool result overrides other tool results, which instruction hierarchy fine-tuning does not address.


<a id="term-shared-folder-key"></a>

**shared folder key** — *共享文件夹密钥*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

The 32-byte key k_shr that encrypts the items of a LastPass shared folder and is wrapped with RSA-OAEP for each recipient.


<a id="term-sharing-key-overwrite"></a>

**Sharing Key Overwrite** — *共享密钥覆写*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

Attacks LP07 and DL02: a malicious server substitutes the recipient's RSA public key, so the share key is encrypted to a key it controls.


<a id="term-side-channel-risk"></a>

**Side-Channel Risk** — *侧信道风险*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

Information leaked through observable agent behavior such as tool execution timing, API call sequences or network traffic patterns.

No prior work is known to study such side-channel attacks in agentic systems, so the analysis is deferred to future work and the exposure should be treated as open.


<a id="term-single-sign-on"></a>

**single-sign-on** — *单点登录*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

One authentication and authorisation point across many services; Okta and Composio use it for agent access and credential provisioning.


<a id="term-super-admin"></a>

**super admin** — *超级管理员*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

A privileged LastPass team account that can reset the master password of other members.

Each such account carries an RSA key pair (sk_adm, pk_adm); their public keys are what the client fetches from the server at login.


<a id="gloss-t"></a>

## T

<a id="term-taint-tracking"></a>

**taint tracking** — *污点追踪*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 6</span>

A technique that marks untrusted data and follows its propagation, so data influenced by untrusted sources can be constrained.

The SoK's information flow control category covers both. In agents, mechanisms split into symbolic-variable, multi-execution and model-based approaches, and the design axis is whether the goal is integrity, blocking untrusted input from steering tool calls, or confidentiality, keeping secrets out of untrusted sinks.


<a id="term-task-level-identity"></a>

**task-level identity** — *任务级身份*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

A short-lived identity created for a specific task or session, giving dynamic least-privilege operation rather than a standing identity.


<a id="term-threat-model"></a>

**Threat Model** — *威胁模型*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

A classification of who the attacker is and what they can reach, used to group attack vectors by adversary capability.

This work uses three: external, user-level, and internal adversaries.


<a id="term-tool-poisoning"></a>

**Tool poisoning** — *工具投毒*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

A third-party tool whose name, description or implementation carries a malicious prompt or code, loaded with the tool definition.

Vector V3 in the SoK. Two representative results — Les Dissonances hijacks the order of tool execution and found 75% of 66 real tools vulnerable; ToolHijacker optimises a tool document to force selection and defeats StruQ, SecAlign, known-answer detection, DataSentinel and perplexity detection.


<a id="term-transaction-key"></a>

**transaction key** — *事务密钥*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

The key Dashlane derives from the master key and the transaction parameters to encrypt one transaction's content.

The salt is constant for all transactions, so every transaction sharing the same KDF and cipher mode is encrypted under the same derived key.


<a id="term-transaction-replay"></a>

**transaction replay** — *事务重放*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

Duplicating, reordering or dropping Dashlane transactions, which the client cannot detect.

Attack DL01. It works because the transaction key depends only on the transaction parameters, not on the transaction itself, and it is the building block for the Dashlane downgrade attacks of Section 4.4.2.


<a id="term-transactional-database"></a>

**transactional database** — *事务型数据库*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

Dashlane's vault representation, in which each transaction creates, modifies or deletes one item.


<a id="term-transient-session-memory"></a>

**Transient Session Memory** — *会话内临时记忆*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

Memory that lasts only for the current session and is discarded when the session ends.


<a id="term-trust-on-first-use-tofu"></a>

**Trust On First Use (TOFU)** — *首次使用信任*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

Remembering a public key the first time it is seen and flagging any later change, so substitution is confined to first use.


<a id="term-trust-on-first-use"></a>

**Trust-On-First-Use** — *首次使用信任*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 9</span>

A scheme that accepts a public key the first time it is seen and alerts the user if it later changes.

Together with PKIs and Verified Key Directories it is one of the mitigations the paper proposes for the key-substitution attacks, since some form of public-key verification cannot be avoided.


<a id="term-trusted-execution-environment"></a>

**trusted execution environment** — *可信执行环境*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

A hardware-based isolated region in which confidential computing keeps agent credentials beyond the reach of the surrounding software.


<a id="gloss-u"></a>

## U

<a id="term-unconstrained-data-flow"></a>

**Unconstrained Data Flow** — *无约束数据流*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

Data moves freely from input at an untrusted interface to any output, because an LLM has no type system or access control to constrain it.

Named R3, damaging confidentiality and integrity. Its consequences are private data leakage (R5), data corruption (R6) and resource drain (R7); the canonical example is an agent returning an attacker-controlled URL that is then fetched automatically.


<a id="term-url-checksum"></a>

**URL checksum** — *URL 校验和*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

A hash of an item's URL stored in another encrypted field so the client can detect a swapped URL.

Deployed by Bitwarden in July 2024. Old items never receive it, and it is only checked when the item has a per-item key, so attacks before July 2024 and Attack BW10 both defeat it.


<a id="term-user-key"></a>

**user key** — *用户密钥*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 3</span>

The 64-byte symmetric key that protects every item in a Bitwarden or LastPass vault, stored on the server only in encrypted form.


<a id="term-user-key-overwriting"></a>

**User Key Overwriting** — *用户密钥覆写*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Attack BW11, which forges a user key ciphertext whose encryption half the adversary knows, forfeiting the confidentiality of later items.


<a id="term-user-level-adversary"></a>

**User-level adversary** — *用户级对手*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 4</span>

An attacker who reaches the agent directly as a malicious user, or a third party that poisons an otherwise benign user's input.


<a id="term-utility-loss"></a>

**utility loss** — *效用损失*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

The capability an agent gives up when privilege separation splits its functionality across isolated components that must then communicate.

The paper treats reducing utility loss while retaining the security guarantee as an open challenge for practical deployment.


<a id="gloss-v"></a>

## V

<a id="term-vault-indistinguishability"></a>

**vault indistinguishability** — *保险库不可区分性*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 2</span>

The goal that an adversary cannot even tell vaults apart, beyond their plaintext contents.


<a id="term-vault-integrity"></a>

**vault integrity** — *保险库完整性*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

The guarantee that vault items and settings are the ones the user stored, in the same form and arrangement.

Encrypting each item separately with AE does not provide it: items and fields can still be swapped, deleted, duplicated or merged, and cleartext metadata such as the KDF parameters can be edited.


<a id="term-vault-key"></a>

**vault key** — *保险库密钥*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 1</span>

The key that actually encrypts a vault; it is itself protected by a key derived from the master password.

In the talk's model, the master password wraps the vault key, and the vault key encrypts the vault, so the master password is never used to encrypt items directly.


<a id="term-verified-key-directory"></a>

**Verified Key Directory** — *验证密钥目录*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 9</span>

A directory that makes a provider's mis-association of public keys evident to users.

Explored in secure messaging, it would not stop a malicious server from binding the wrong public key to a user, but it would alert users when their provider misbehaves.


<a id="term-verified-key-directory-vkd"></a>

**Verified Key Directory (VKD)** — *已验证密钥目录*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 8</span>

A directory that cannot stop a server from publishing a wrong public key but makes the tampering evident to users.


<a id="term-vertical-privilege-separation"></a>

**vertical privilege separation** — *纵向权限分离*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 7</span>

Hierarchical privilege separation with a trusted planner above a lower-privilege parser, so tool results never flow directly into planning.


<a id="gloss-w"></a>

## W

<a id="term-wrong-instruction-following"></a>

**Wrong Instruction Following** — *错误指令跟随*  <span class='bd-gloss-alpha'>First seen: SoK: Agentic AI · Chapter 5</span>

The agent obeys prompts injected by an attacker instead of the instructions intended by the benign user or the system developer.

Named R2, an integrity failure. Its vectors are the prompt-injection family: V1 indirect prompt injection, V4 direct prompt injection, and the instructions V6 memory poisoning plants.

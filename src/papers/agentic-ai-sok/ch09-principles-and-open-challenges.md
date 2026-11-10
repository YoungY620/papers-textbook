# Design principles, open challenges and conclusion

The preceding chapters took the defense landscape apart mechanism by mechanism. This closing chapter collects what the systematization recommends rather than what it catalogues: the design principles of §5.6 that tie the defence categories together, the "limitations and open challenges" that close each defence section, and the scope and ethical statements that say what the work does not claim. The contribution here is the standing of each defence and the paper's judgement of where the remaining work lies.

## Defence design principles

Effective agent security requires multiple complementary mechanisms acting together; no single approach suffices. Three principles guide the design, and further principles also apply, among them fail-safe defaults and economy of mechanisms.

**Defense-in-depth.** Mechanisms complement each other by acting at different stages and against different vectors: input guardrails (§5.2.1) filter first, output guardrails (§5.2.2) sanitize last, information flow control (§5.2.3) and monitoring (§5.2.4) run continuously, access control (§5.4.2) authenticates and authorises, privilege separation (§5.3.1) and the other secure-by-design approaches give architectural protection, component hardening (§5.5) strengthens individual elements, and human-in-the-loop validation (§5.2.5) gives oversight of critical decisions.

**Principle of least privilege.** Agents should operate with the minimal permissions and access rights their tasks require, implemented through privilege separation that isolates components and restricts tool access.

**Complete mediation.** Every access to a sensitive resource should be checked and validated, reflected in monitoring and in access control that verifies each interaction with a protected resource.

The principles make the defence landscape coherent, and they are also where the most structural gaps sit. Nothing argues that the stages of defense-in-depth compose into full coverage: the interactions between stages, where one tool result influences a later planning decision, are the object being defended and are owned by no single mechanism. Least privilege names an "effective set of least-privilege components" as an open problem rather than a solved design. Complete mediation presupposes a policy able to decide every interaction, and adaptive policy frameworks of that kind do not exist yet (§5.4.2). The principles state the goal; the challenges state the distance to it.

![The defence landscape of AI agents, showing the components or stages of the control flow that each defence targets.](assets/fig4-defense-landscape.png)

## Open challenges

The challenges are stated once per defence category in §5; each names what is missing and why the mechanism does not close it.

**Criteria, not detectors, are the bottleneck.** As the input space becomes vast and diverse, universal security criteria cannot be established: model-based detectors are bypassed by adaptive attacks, rule-based detectors need extensive human effort, and both produce false positives and negatives. The cause is ambiguous boundaries between secure and insecure data and instructions, which neither detector class addresses.

**Information flow control that is lightweight and safe to relax.** Multi-execution and variable-based reasoning incur substantial runtime overhead, limiting practicality for latency-sensitive agents, while conservative propagation causes label creep that renders an agent unusable. Closing this needs lightweight tracking plus principled declassification rules.

**Behavioural detection under stochastic, context-dependent execution.** Stochastic behaviour makes benign and harmful actions hard to distinguish: static rules miss novel attacks, and adaptive models incur overhead and remain evadable. Long-lived executions accumulate logs whose storage overhead and privacy controls remain largely unexplored.

**When to hand a decision to a human.** Frequent prompts cause decision fatigue that undermines the safety benefit, and alerts assume a literacy many users lack, so users approve risky actions or overreact to benign ones. Principled criteria for deferring to human judgment are missing; recurrence policies cut prompt frequency without supplying the criterion.

**Generalised, utility-preserving isolation.** Privilege separation research addresses generic indirect prompt injection in simplified environments, not the diverse risks of real web, file system and database environments. Dividing an agent into an effective set of least-privilege components is open, as is efficient communication across isolated components.

**Formal models of a probabilistic system.** Formal methods were built for structured code, while agents operate on probabilistic models, so capturing stochastic behaviour while preserving meaningful guarantees is difficult. Security properties for agents that interact with web, file systems or mobile applications remain underspecified, and full-spectrum verification is open.

**Identity, attribution and interoperability.** Whether an agent's actions belong to the human operator, the agent instance or the task is unresolved and varies by domain, and platforms implement incompatible credential issuance, delegation and revocation flows. Interoperable taxonomies and lifecycle tooling are needed to preserve accountability.

**Access control beyond the vector database.** Existing work targets retrieval-augmented applications with vector databases, while agentic systems need broader coverage of tools, data sources and inter-agent interactions. Deployments lack adaptive policy frameworks and rely on ad hoc, non-uniform policies, creating mismatches across agents and gaps with non-agentic services.

**Coordinated credential orchestration.** Agent stacks rely on ad hoc secret handling with no standardised protection, and many frameworks guide developers to store API keys in unencrypted environment variables. Multi-agent systems complicate secret sharing further, making least privilege and traceability hard to maintain.

**Threat models for component hardening.** Hardening targets simplified threat scenarios: instruction-hierarchy fine-tuning mainly addresses simple system-prompt, user-prompt and tool-result scenarios and fails on shadowing, where a malicious tool result overrides other tool results. The role of each component, and its appropriate threat model, remain unclear.

## The tensions the paper identifies

Flexibility versus security. Flexibility along any design dimension amplifies risk: the properties that make agents useful are the ones that widen the attack surface, so the tension is structural rather than a defect to be patched. It reappears inside the mechanisms — privilege separation "entails utility loss by splitting functionality across isolated components", and guardrails trade false positives that degrade utility against false negatives that break security.

Autonomy versus oversight. Autonomy is the purpose of an agent, and human-in-the-loop validation is the one mechanism that returns a decision to a person. But oversight is bounded by attention: frequent prompts cause decision fatigue, alerts assume literacy users may not have, and the controls borrowed from mobile permissions do not say when a human should be asked at all.

Capability versus verifiability. Capability comes from a probabilistic model whose behaviour is context-dependent and stochastic, while the classical route to assurance, formal verification, was designed for structured code. What can be verified today is narrow — user-intent alignment for mobile GUI agents, plan constraints as pushdown automata, policy documents as rule circuits over action trajectories — and the guarantees that would certify deployed agents remain underspecified.

## What a systems-level view buys

The methodological claim is that agent security is a systems problem. Existing LLM security surveys emphasise model-level threats and overlook the expanded attack surface of agentic systems; prior agent studies narrow to specific attack vectors, agent types or components; design-oriented work proposes principles without systematizing attacks or defences; and the closest surveys consider cross-component interactions but limit their defence taxonomies largely to model-based techniques. A systems view buys a unified risk taxonomy covering all agent components and their interactions, so attacks, defences and case studies share one vocabulary, and a defense-in-depth framework integrating model-based with system-level defences, because component-level defences alone cannot address what combining LLMs with traditional software creates. The attack surface that matters is the interaction: a defence that hardens one component in isolation leaves the path from a retrieved document to a tool argument open.

## Scope and limitations

The scope is bounded. The work covers risks and defences unique to agentic systems or significantly amplified in them compared with traditional software and standalone LLMs; for risks that also exist in non-agentic models, such as jailbreak and hallucination, it stresses how autonomy and environment access magnify their impact. Attacks on model internals, such as model inversion, are excluded, because they do not fundamentally worsen in agentic settings, where agents operate purely through inference-time input and output interfaces. The review covers sources from 2023 to October 2025 and yields 128 papers, of which 51 are attack methods and 60 are defence methods.

The ethical statement names the limits of the work itself. It assumes the security community will use the material primarily for defence, concedes that it cannot prevent all misuse, and warns that technology evolution may outpace implementations. Systematizing attack knowledge may lower the difficulty for adversaries, surface defence gaps, or create false confidence that existing defences are comprehensive; the mitigation is to favour protective guidance and vetted sources such as peer-reviewed venues, vendor advisories and verified CVEs. As a systematization of knowledge the work runs no experiments or datasets.

## Conclusion

The conclusion collects the argument rather than extending it. The systematization offers itself as a guide for building secure agents and as a way to point out meaningful directions for research — guardrail criteria that hold under an adaptive adversary, deployable information flow tracking, principled points at which to defer to a human, generalised isolation, formal properties for probabilistic components, interoperable identity, adaptive access control, coordinated credential management, and threat models that match deployed systems. None of these is closed by the mechanisms of the previous chapters.

## Key points

- Three design principles tie the defence landscape together: defense-in-depth, least privilege and complete mediation, with fail-safe defaults and economy of mechanisms named as further principles.
- Each principle names a mechanism whose limits leave the guarantee open: depth is never argued to compose into full coverage, an effective set of least-privilege components is unsolved, and complete mediation needs adaptive policies that do not yet exist.
- The recurring open challenges are criteria rather than detectors for guardrails, lightweight information flow control, detection under stochastic execution, a criterion for deferring to a human, generalised isolation, formal models of probabilistic agents, interoperable identity, adaptive access control, coordinated credential orchestration, and honest threat models for hardening.
- Three tensions run through them: flexibility amplifies risk by design, autonomy is bounded by human attention, and capability rests on a probabilistic model that classical verification was not built for.
- A systems-level view buys a unified risk taxonomy over components and their interactions plus a defense-in-depth framework integrating model-based and system-level defences.
- The work is scoped to agent-specific risks and excludes model-internal attacks such as model inversion; it rests on 128 papers from 2023 to October 2025 and assumes defensive use.

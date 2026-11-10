# Related work and baselines

A systematisation of knowledge surveys the works that are its evidence, so its coverage and its comparison with prior surveys coincide. This chapter reads the SoK against the literature it builds on: the reviews it positions itself against, the works under vectors `V1`…`V6`, the defence systems in Table 2, and the frameworks it maps onto.

## The survey landscape

The reviews the SoK contrasts itself with split in two. Model-level work takes the model as its object: Liu et al. formalise prompt injection so existing attacks become special cases, evaluating 5 attacks and 10 defences across 10 LLMs and 7 tasks [81]; Jia et al. show StruQ, SecAlign and instruction-hierarchy training lose general-purpose utility and stay vulnerable to existing attacks, and more so to adaptive ones, contrary to their papers' claims [58]; Wang et al. systematise jailbreak guardrails for a fragmented landscape [138]; Grosse et al. press on threat-model realism [49]. The SoK's objection: these measure the wrong boundary — an agent's damage is done by model and software together, so a threat list over model interfaces cannot express what a retrieved document does to a later tool argument.

The second group is agent studies narrower in a specific way. Agent Security Bench benchmarks agent attacks and defences over 10 scenarios, 10 agents, over 400 tools, 27 methods and 7 metrics [155]. Hou et al. study one component, the Model Context Protocol, defining a four-phase, sixteen-activity lifecycle and a taxonomy of four attacker types and sixteen scenarios [52]. Beurer-Kellner et al. propose design patterns for provable resistance [12] and Zhang et al. argue for explicit security principles [156]. The closest prior work is the pair the SoK says considers cross-component interactions but limits its defence taxonomy largely to model-based techniques: Deng et al.'s survey [31] and the TrustAgent survey, whose modular taxonomy spans intrinsic components (brain, memory, tool) and extrinsic ones (user, agent, environment) and covers attack, defence and evaluation [151].

What the SoK claims is a different organising object rather than more papers: the agent characterised through seven design dimensions — input trust, access sensitivity, workflow, action, memory, tool, user interface — so that risk is a function of where an agent sits on those continuums, which no prior taxonomy expresses. Its scope is 128 papers from 2023 to October 2025, 51 attack methods and 60 defence methods.

## The attack literature

### External adversaries: `V1`, `V2`, `V3`

Greshake et al. founded `V1`: an adversary with no interface to the system still steers it by placing prompts in data likely to be retrieved, with impacts ranging from data theft to worming [48]. InjecAgent made this measurable — 1,054 cases over 17 user tools and 62 attacker tools, split into direct harm and data exfiltration, with ReAct-prompted GPT-4 vulnerable 24% of the time and roughly double that when instructions are reinforced with a hacking prompt [153]. Both assume what the design space makes explicit: the agent must read attacker-reachable content for the attack to exist.

`V2` injects data rather than instructions. Spracklen et al. quantify one instance: across 16 code-generating LLMs and 576,000 samples, at least 5.2% of packages recommended by commercial models and 21.7% by open-source models are hallucinated, with 205,474 unique names an adversary can register and fill with malicious code [127]. No malicious intent reaches the model, only a name it mistakes for a fact — hence the SoK files it as both `V2` and `R4`.

`V3` attacks the tool supply chain. Les Dissonances identifies cross-tool harvesting and polluting, where a malicious tool hijacks the order of tool execution, its scanner finding 75% of 66 LangChain and Llama-Index tools vulnerable [74]. ToolHijacker optimises a malicious tool document so a retrieval-then-selection pipeline consistently picks the attacker's tool for a chosen task, and finds prevention-based defences (StruQ, SecAlign) and detection-based ones (known-answer detection, DataSentinel, perplexity detection) all insufficient [121]. Both exploit the arbitrary-tools end of the tool dimension.

### User-level adversaries: `V4`

HouYi is the systematic treatment of direct prompt injection: a black-box payload of three components — framework, separator, disruptor — modelled on SQL injection and XSS, deployed against 36 real applications with 31 susceptible and 86.1% success at stealing the original prompt or consuming the service's computation [80]. Perez and Ribeiro established the technique [107]; later work automated it [79] and extended it through tool manipulation and images [39, 40]. The SoK regroups identical payloads by adversary position rather than technique: `V4` sits with a user feeding the agent directly, `V1` with an external party who cannot.

### Internal adversaries: `V5`, `V6`

`V5` model poisoning is the vector the SoK treats as hardest to realise, since it requires the developer or a component provider to embed hidden behaviour in the model [19, 91]; the works it cites for it are model-level safety and jailbreak-search papers, and the vector exists because a component supplier is an adversary the user cannot audit.

`V6` memory poisoning is densest. AgentPoison backdoors long-term memory or RAG knowledge bases by optimising a trigger into a distinct embedding region, needs no model training, and reaches at least 80% attack success with at most 1% benign impact at a poison rate below 0.1% across three agents [21]. PoisonedRAG formalises knowledge-database corruption as an optimisation with two coupled objectives: the poisoned text must rank in the top-k retrieved results and must steer the generated answer [162]. MINJA weakens their strongest assumption, injecting malicious records by querying the agent with no direct memory write, using bridging steps and a progressively shortened indication prompt so the record is retrieved naturally later [34]. The three progressively remove the privilege the attack assumes, and `V6` absorbs them as one vector defined by component access.

The six form a graph, not a list: an expanded attack surface (`R1`) admits attacker-controlled data, which reaches model risks `R2`–`R4`, which amplify consequence risks `R5`–`R7`. No individual attack paper makes that argument, because each fixes one vector and one setting.

## The defence literature

### Input and output guardrails

NeMo Guardrails gives developers a language for input filters [110]; Constitutional classifiers train classifiers from a constitution against universal jailbreaks [119]; LlamaFirewall is an open-source guardrail framework [22]; PromptShield and PromptArmor detect and remove injected prompts [55, 123]; DataSentinel uses a deliberately injection-vulnerable model to catch subtle injections [82]; URL and network allowlists constrain retrieval and egress [46]. Output-side, CodeShield and HeimdallM statically analyse generated code against arbitrary execution [85, 89]; Task Shield enforces task alignment [57]; GuardAgent turns safety requests into executable guardrail code [146]; Conseca generates policies from runtime context [132]; Progent expresses privilege as symbolic rules over tool names and arguments, using an SMT solver to admit only narrowing updates without consent [122]. The bottleneck is criteria, not detectors: model-based detectors fall to adaptive attacks, rule-based ones need human effort, and both produce false positives and negatives.

### Information flow control and taint tracking

PFI combines agent isolation, secure processing of untrusted data and escalation guardrails [60]. CaMeL extracts control and data flows from the trusted query so untrusted data cannot affect program flow, and attaches capabilities to values to block exfiltration, solving 77% of AgentDojo tasks with provable security against 84% undefended [29]. FIDES tracks confidentiality and integrity labels deterministically and adds primitives for selectively hiding and revealing information [26]. MELON re-executes the trajectory with a masked user prompt and compares tool calls, since a successful attack makes the next action less dependent on the user's task [160]. RTBAS adds two dependency screeners — LM-as-a-judge and attention-based saliency — escalating to confirmation only when needed [158]. Permissive information flow analysis avoids label conservatism by measuring an input's influence over repeated inferences [124], and AgentArmor treats the runtime trace as a program [136]. The SoK names the shared axes the papers leave implicit — symbolic-variable, multi-execution and model-based mechanisms; integrity versus confidentiality goals — and the opening: these approaches cost runtime, and conservative propagation causes label creep that makes an agent unusable without safe declassification.

### Monitoring and human-in-the-loop validation

AgentMonitor scores behavioural risk in web and file-access environments [93]; AgentAuditor builds an experiential memory of structured features and reasoning traces and retrieves comparable cases, with a benchmark of 2,293 annotated records over 15 risk types [83]; SentinelAgent detects anomalies in multi-agent systems through interaction-graph modelling [51]. Human-in-the-loop validation is comparatively unique to agents: coding agents request approval before writing files or running commands, and defences fall back on confirmation when a policy would be violated [26, 29, 60, 144], while Wu et al. model user permission preferences to cut prompt frequency [145]. The limitation is decision fatigue and a literacy mismatch between what alerts assume and what users have.

### Privilege separation and formal verification

AirGapAgent addresses an adversarial third-party app that manipulates context to extract private data, retaining only task-relevant data and running the task on that minimised context, with per-sender contexts [11]. f-secure disaggregates an LLM system into a pipeline with a security monitor filtering untrusted input into planning [142]; CaMeL, FIDES and PFI separate planning from parsing or split tools into normal and sandboxed variants [26, 29, 60]. IsolateGPT spawns per-application agents restricted to that application's tools [144], IPIGuard uses a tool dependency graph [4], and DRIFT combines a secure planner, a validator monitoring deviations from the planned function trajectory, and an isolator masking instructions conflicting with the user query [70]. The SoK names the shared axis — vertical separation on the planner–parser line versus horizontal separation by scope — and notes that all of it is demonstrated on generic indirect injection in simplified environments. Formal verification is thinnest: Formal-LLM encodes constraints such as required tool orderings as pushdown automata [75], VeriSafe Agent formalises user intent into a DSL over UI state transitions and verifies proposed GUI actions against it [67], and ShieldAgent compiles policy documents into rule circuits over action trajectories [20].

### Identity and access management, and component hardening

Identity work is mostly about delegation: authenticated delegation argues agents need a delegation primitive with verifiable authority [126], SAGA is an architecture for governing agentic systems [128], and the agent network protocol white paper addresses agent-to-agent identity [16]. Access control exists mainly for vector stores: Bedrock filters retrieval results by agent permissions using metadata [3], Honeybee partitions vector databases along RBAC structure [157], and ControlNet uses neuron activations as a RAG firewall [149]. Credential management uses token vaults and temporary storage that prevents history retention [10, 103]. Component hardening splits into model and tool. SecAlign fine-tunes with preference optimisation so models follow the original instruction [18], StruQ separates prompt and data through structured queries [17], and instruction-hierarchy training ranks system, user and third-party instructions [134, 143]. On the tool side, ETDI adds signed and versioned tool definitions [33], Anthropic's Connectors Directory curates reviewed tools [7], MCP Context Protector interposes a proxy with manual review [131], MCP Safety Audit examines tools for exploitable logic or misleading descriptions [109], and MCIP adds observability and a fine-tuned threat detector [59]. The SoK's verdict is that hardening addresses simplified threat models — instruction-hierarchy fine-tuning handles system prompt, user prompt and tool result but not shadowing, where one malicious tool result overrides another — and independent evaluation supports the scepticism: Jia et al. found these defences both utility-costly and bypassable under adaptive attack [58].

## MITRE ATLAS, OWASP and MCP

OWASP's Top 10 for LLM Applications shapes the risk taxonomy during construction [104]. MITRE ATLAS supplies technique names, and the appendix maps the SoK's identifiers onto them: `V1` to Retrieval Content Crafting, Drive-by Compromise and Prompt Infiltration via Public-Facing Applications; `V4` to LLM Prompt Injection; `V5` to Poison Training Data, Publish Poisoned Datasets and Publish Poisoned Models; `V6` to RAG Poisoning, False RAG Entry Injection and AI Agent Context Poisoning; `R2` to AI Agent Tool Invocation; `R5` to Credentials from AI Agent Configuration, OS Credential Dumping, RAG Credential Harvesting, Unsecured Credentials and LLM Response Rendering; `R6` to Modify AI Agent Configuration, LLM Trusted Output Components Manipulation and External Harms; and `R7` to Denial of AI Service and External Harms.

MCP standardises tool use: a protocol for defining, discovering and invoking external tools, with dynamic schema negotiation, bi-directional channels, and access control and capability negotiation as first-class features [6]. The MCP literature the SoK cites shows that standardisation is itself an attack surface: Hou et al. enumerate sixteen scenarios across malicious developers, external attackers, malicious users and security flaws — tool poisoning, installer spoofing, unauthorised access — validated by case studies [52], and MCP Safety Audit demonstrates major exploitable behaviour in MCP-connected systems [109]. ETDI's signing, Context Protector's review proxy and MCIP's detector all try to restore trust to a discovery channel that is open by design.

## What prior work does not cover

Nothing in this literature analyses risk through the design dimensions, so no prior work can say which deployment choice made a demonstrated attack reachable, and nothing models risk interaction, so the cascades from `R1` to `R2`–`R4` and on to `R5`–`R7` are unanalysed. Side channels from tool timing, API call sequences and traffic patterns have, to the SoK's knowledge, no prior study at all, and identity, credentials, adaptive access control and formal models of probabilistic agents are named as foundational questions rather than solved ones.

## Sources consulted

Downloaded and read for this chapter; bracketed numbers are reference numbers in the paper where one exists.

- Greshake et al., *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*, AISec 2023 [48] — https://arxiv.org/abs/2302.12173
- Zhan et al., *InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents*, ACL 2024 [153] — https://arxiv.org/abs/2403.02691
- Yi et al., *Benchmarking and Defending Against Indirect Prompt Injection Attacks on LLMs* (BIPIA), KDD 2025 — https://arxiv.org/abs/2312.14197 (not cited by the SoK)
- Liu et al., *Prompt Injection attack against LLM-integrated Applications* (HouYi) [80] — https://arxiv.org/abs/2306.05499
- Li et al., *Les Dissonances: Cross-Tool Harvesting and Polluting in Pool-of-Tools Empowered LLM Agents* [74] — https://arxiv.org/abs/2504.03111
- Shi et al., *Prompt Injection Attack to Tool Selection in LLM Agents* (ToolHijacker) [121] — https://arxiv.org/abs/2504.19793
- Spracklen et al., *We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs*, USENIX Security 2025 [127] — https://arxiv.org/abs/2406.10279
- Chen et al., *AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases*, NeurIPS 2024 [21] — https://arxiv.org/abs/2407.12784
- Dong et al., *Memory Injection Attacks on LLM Agents via Query-Only Interaction* (MINJA) [34] — https://arxiv.org/abs/2503.03704
- Zou et al., *PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models*, USENIX Security 2025 [162] — https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf
- Debenedetti et al., *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*, NeurIPS 2024 [30] — https://arxiv.org/abs/2406.13352
- Liu et al., *Formalizing and Benchmarking Prompt Injection Attacks and Defenses*, USENIX Security 2024 [81] — https://arxiv.org/abs/2310.12815
- Jia et al., *A Critical Evaluation of Defenses against Prompt Injection Attacks* [58] — https://arxiv.org/abs/2505.18333
- Wang et al., *SoK: Evaluating Jailbreak Guardrails for Large Language Models*, IEEE S&P 2026 [138] — https://arxiv.org/abs/2506.10597
- Yu et al., *A Survey on Trustworthy LLM Agents: Threats and Countermeasures* (TrustAgent) [151] — https://arxiv.org/abs/2503.09648
- Zhang et al., *Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents*, ICLR 2025 [155] — https://arxiv.org/abs/2410.02644
- Hou et al., *Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions* [52] — https://arxiv.org/abs/2503.23278
- Beurer-Kellner et al., *Design Patterns for Securing LLM Agents against Prompt Injections* [12] — https://arxiv.org/abs/2506.08837
- Zhang et al., *LLM Agents Should Employ Security Principles* [156] — https://arxiv.org/abs/2505.24019
- Shi et al., *Progent: Securing AI Agents with Privilege Control* [122] — https://arxiv.org/abs/2504.11703
- Debenedetti et al., *Defeating Prompt Injections by Design* (CaMeL) [29] — https://arxiv.org/abs/2503.18813
- Costa et al., *Securing AI Agents with Information-Flow Control* (FIDES) [26] — https://arxiv.org/abs/2505.23643
- Kim et al., *Prompt Flow Integrity to Prevent Privilege Escalation in LLM Agents* (PFI) [60] — https://arxiv.org/abs/2503.15547
- Wu et al., *System-Level Defense against Indirect Prompt Injection Attacks: An Information Flow Control Perspective* (f-secure) [142] — https://arxiv.org/abs/2409.19091
- Zhu et al., *MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents*, ICML 2025 [160] — https://arxiv.org/abs/2502.05174
- Zhong et al., *RTBAS: Defending LLM Agents Against Prompt Injection and Privacy Leakage* [158] — https://arxiv.org/abs/2502.08966
- Siddiqui et al., *Permissive Information-Flow Analysis for Large Language Models* [124] — https://arxiv.org/abs/2410.03055
- Bagdasarian et al., *AirGapAgent: Protecting Privacy-Conscious Conversational Agents*, CCS 2024 [11] — https://arxiv.org/abs/2405.05175
- Wang et al., *AgentArmor: Enforcing Program Analysis on Agent Runtime Trace to Defend Against Prompt Injection* [136] — https://arxiv.org/abs/2508.01249
- Li et al., *DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents* [70] — https://arxiv.org/abs/2506.12104
- He et al., *SentinelAgent: Graph-based Anomaly Detection in LLM-based Multi-Agent Systems* [51] — https://arxiv.org/abs/2505.24201
- Luo et al., *AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents* [83] — https://arxiv.org/abs/2506.00641
- Xiang et al., *GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning* [146] — https://arxiv.org/abs/2406.09187
- Shi et al., *PromptArmor: Simple yet Effective Prompt Injection Defenses* [123] — https://arxiv.org/abs/2507.15219
- Chennabasappa et al., *LlamaFirewall: An open source guardrail system for building secure AI agents* [22] — https://arxiv.org/abs/2505.03574
- Sharma et al., *Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming* [119] — https://arxiv.org/abs/2501.18837
- Hines et al., *Defending Against Indirect Prompt Injection Attacks With Spotlighting* — https://arxiv.org/abs/2403.14720 (not cited by the SoK)
- Chen et al., *StruQ: Defending Against Prompt Injection with Structured Queries*, USENIX Security 2025 [17] — https://arxiv.org/abs/2402.06363
- Chen et al., *SecAlign: Defending Against Prompt Injection with Preference Optimization*, CCS 2025 [18] — https://arxiv.org/abs/2410.05451
- Wallace et al., *The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions* [134] — https://arxiv.org/abs/2404.13208
- Tsai and Bagdasarian, *Contextual Agent Security: A Policy for Every Purpose* (Conseca), HotOS 2025 [132] — https://arxiv.org/abs/2501.17070
- Lee et al., *VeriSafe Agent: Safeguarding Mobile GUI Agent via Logic-based Action Verification* [67] — https://arxiv.org/abs/2503.18492
- Li et al., *Formal-LLM: Integrating Formal Language and Natural Language for Controllable LLM-based Agents* [75] — https://arxiv.org/abs/2402.00798
- Yao et al., *ControlNet: A Firewall for RAG-based LLM System* [149] — https://arxiv.org/abs/2504.09593
- Zhong et al., *Honeybee: Efficient Role-based Access Control for Vector Databases via Dynamic Partitioning* [157] — https://arxiv.org/abs/2505.01538
- Radosevich and Halloran, *MCP Safety Audit: LLMs with the Model Context Protocol Allow Major Security Exploits* [109] — https://arxiv.org/abs/2504.03767

Not obtained. IsolateGPT [144] (NDSS 2025) has no open-access version I could reach. Deng et al., *AI Agents Under Threat* [31] (ACM Computing Surveys) and Grosse et al. [49] (USENIX Security 2024) are behind publisher paywalls. Works cited through vendor documentation or code repositories rather than papers — Bedrock access control [3], CodeShield and HeimdallM [85, 89], ETDI [33], MCP Context Protector [131], Anthropic's Connectors Directory [7], Auth0's token vault [10], Composio and Okta [24, 97] — were read as documentation and are described only as far as the SoK's own characterisation. IPIGuard [4], ACE [69], SAGA [128], authenticated delegation [126], the agent network protocol [16], Maris [27], ControlValve [56] and ShieldAgent [20] were not obtained; they are named in the relevant categories from Table 2 and the paper's descriptions of them, not from direct reading.

## Key points

- The reviews the SoK positions itself against divide into model-level LLM-security work and narrower agent studies, plus two agent surveys that consider cross-component interaction but keep largely model-based defence taxonomies.
- The claimed difference is the organising object: seven design dimensions, one risk taxonomy spanning components and their interactions, and defence-in-depth combining model-based with system-level mechanisms.
- The attack works map onto `V1`–`V6` by adversary position — external, user-level, internal — and the memory-poisoning line (AgentPoison, PoisonedRAG, MINJA) removes the privilege each attack assumes until only query access is needed.
- The SoK's addition to the attack literature is the risk-interaction argument — `R1` admits attacker data, which reaches `R2`–`R4`, which amplify `R5`–`R7` — plus the shared design axes it names for defences.
- Defence coverage is uneven: information flow control carries the strongest guarantees, guardrails are limited by criteria rather than detectors, monitoring and oversight face stochasticity and decision fatigue, access control is confined to vector stores, and formal verification has only a handful of systems.
- What remains outside this prior work — design-dimension analysis, risk interaction, side channels, agent identity, adaptive access control and formal models of probabilistic agents — is exactly the open-challenge list the SoK closes on.

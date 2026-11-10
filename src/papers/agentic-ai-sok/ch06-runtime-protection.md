# Security goals and runtime protection

Defenses for an agentic system are classified by the security goal they serve and by the moment they intervene. The goals are confidentiality, integrity and availability plus contextual security. Runtime protection enforces security dynamically during execution across five mechanism families — input guardrails, output guardrails, information flow control and taint tracking, monitoring, and human-in-the-loop validation — which Table 2 lists with the risks R1–R7 each covers and Figure 4 places on the component or control-flow stage it targets.

![The defense landscape of AI agents.](assets/fig4-defense-landscape.png)

## Security goals

### Confidentiality

Confidentiality ensures that all information is accessible only to authorized entities. The protected assets are system-level secrets such as API keys, agent internal memory, user private data, and LLM-related data such as model parameters and system prompts. It addresses unconstrained data flow (R3) and private data leakage (R5).

### Integrity

Integrity ensures that data in the agent system and in the external environment remain trustworthy and unmodified by unauthorized entities: it prevents tampering with agent memory, LLM outputs, tool results and environment data, and prevents the agent from being manipulated into unintended actions through malicious instructions. Its concrete goals differ between agents according to their components and their data and control flows. It addresses heterogeneous untrusted interfaces (R1), wrong instruction following (R2), unconstrained data flow (R3), hallucination and model mistakes (R4), and unintended action and data corruption (R6).

### Availability

Availability protects against resource abuse when LLM inference and tools consume user resources, preventing token draining and protecting external systems and agent hosts from denial-of-service. It addresses resource drain and denial-of-service (R7).

### Contextual security

Contextual security ensures that an agent's contexts stay aligned with the user's intended tasks, preventing attacks that manipulate contexts during execution. It complements confidentiality and integrity by governing which context elements are admissible — system prompts, user goals, tool descriptions, retrieved snippets — and how they are prioritized, so that instruction override, context drift and unsafe tool selection are avoided.

## Runtime protection

Runtime protection mechanisms enforce security dynamically during agent execution, detecting real-time threats and behaviors.

### Input guardrail

Input guardrails validate inputs before they reach the agent. As a first line of defense they keep malicious instructions and data out of downstream components, mitigating heterogeneous untrusted interfaces (R1) from untrusted data sources. On standalone models they detect malicious inputs such as jailbreak prompts or harmful content; on agents they address dynamic retrieval and tool execution by verifying the trustworthiness of retrieved data, with URL allowlists constraining retrieval to trusted sources. NeMo Guardrails provides a domain-specific language for developer-defined input filters; Constitutional classifiers, llama-firewall and PromptShield use specialized models against direct and indirect prompt injection; DataSentinel deliberately leverages a prompt-injection-vulnerable model to catch subtle injections other guardrails miss. Design varies across detection mechanism (rule-based strictness versus model-based adaptivity), validation target (content semantics versus the trustworthiness of a datum's origin, the latter unique to an agent's dynamic retrieval from external sources), and mitigation strategy (filter, sanitize, or normalize input into a typed, validated structure).

Limitations and open challenges. The input space is vast and diverse, so universal criteria are hard to establish: model-based detectors are bypassed by adaptive attacks, and rule-based detectors need extensive human effort and generalize poorly. Both false positives and false negatives follow — the former from limited accuracy but more from ambiguous boundaries between secure and insecure data and instructions, the latter letting attackers inject malicious input past the guardrail.

### Output guardrail

Output guardrails check outward behavior — responses to users and tool usages that reach external systems — complementing input guardrails by preventing attacks that look benign but trigger malicious actions. They mitigate wrong instruction following (R2) by validating task alignment, hallucination and model mistakes (R4) through output verification, private data leakage (R5) by checking for sensitive data exposure, and unintended actions and data corruption (R6) by validating tool usage. LLM output guardrails detect harmful outputs with classifiers or programmable rules; agent-specific ones validate tool usage and action sequences for context-dependent policies aligned with user intent. Progent, Conseca and Agrail generate adaptive policies from the runtime context to prevent environment data leakage, corruption and resource drain; GuardAgent and ShieldAgent build domain-specific checks from human-provided policies; CodeShield and HeimdallM statically analyze agent-generated code against arbitrary code execution; network allowlists restrict connections to preauthorized domains. Design varies across detection goal — harmful content, unsafe code, unsafe actions, alignment checks, data privacy, domain-specific policy and runtime-aware contextual security — and detection mechanism, from rule-based pattern matching to model-based classifiers, with hybrid structured-policy-plus-model approaches.

Limitations and open challenges. Output guardrails share input guardrails' false positives and negatives and the rule-versus-model tradeoff, but consume more computation and time because they depend on the LLM's output and process more data.

### Information flow control and taint tracking

Information flow control (IFC) and taint tracking restrict information flow within a system: classical IFC assigns each datum a security label from a predefined information flow lattice, propagates the labels, and detects flows that violate the lattice constraints. In agents they address the model's inherent unconstrained data flow (R3) and mitigate downstream confidentiality (R5) and integrity (R6) violations. PFI, CaMeL and FIDES turn tool results into symbolic variables to track flow deterministically — PFI keeps untrusted data from controlling tool arguments, CaMeL and FIDES keep credentials such as secret codes from reaching untrusted endpoints like malicious email recipients — and commonly pair with privilege separation. Permissive information flow control measures each input's influence on the output by running inference multiple times with different input combinations; Melon extends that to the agent's control and data flows by comparing tool usage with and without specific inputs and blocking manipulated tool calls. Design varies across security goals (integrity, blocking untrusted inputs from influencing tool-call decisions, and confidentiality, keeping sensitive data from untrusted sinks) and mechanisms (symbolic variable-based, multi-execution-based, and model-based, which asks the LLM to inspect information flow from agent traces).

Limitations and open challenges. Multi-execution and variable-based reasoning incur substantial runtime overhead, limiting latency-sensitive use, and label creep can make agents unusable unless automated safe declassification rules exist. Closing the gap needs lightweight tracking and principled policies for relaxing labels safely.

### Monitoring

Monitoring gives system-wide visibility by checking inputs, outputs and intermediate states, surfacing distributed threats where no single action is malicious but together they form a malicious goal, and observing interactions across tools and services over long runs, especially in multi-agent systems. It mitigates R5, R6 and R7. AgentMonitor scores behavioral risks in web and file access environments; AgentAuditor builds a feature memory of unsafe actions to detect run-time anomalies; SentinelAgent and Guardian detect multi-agent anomalies through interaction-graph modeling. Design varies across detection goals (anomaly detection over long trajectories versus interaction-graph monitoring) and log granularity, from coarse action summaries to fine-grained traces of intermediate reasoning steps and parameters; finer logs detect more but increase storage, computation and privacy exposure.

Limitations and open challenges. Monitoring inherits runtime defenses' inaccuracy and overhead. Stochastic, context-dependent behavior blurs benign and harmful actions; static rules miss novel attacks, while adaptive models incur overhead yet remain evadable; and long-lived executions accumulate logs whose storage and privacy controls remain largely unexplored.

### Human-in-the-loop validation

Human-in-the-loop validation lets users validate agent behavior and tool usage, giving user-customized control over security decisions. It mitigates R5, R6 and R7 and is relatively unique to agents, which act on users' behalf and touch external environments such as files, the web and third-party tools, requiring confirmation before high-risk actions. The literature is limited: coding agents such as GitHub Copilot, Gemini Code Assist and Cursor ask approval before writing a file or executing commands, and agent defense systems invoke validation when actions violate defense policies. Design varies across validation scope (terminal commands, file access outside the current workspace, destructive actions such as deletion), user alert (which should explain the intended action, its risks and consequences), and recurrence policy ("allow once", "allow never" and "allow always" mirror mobile permissions, and recent work models user approval preferences to reduce prompt frequency).

Limitations and open challenges. Frequent prompts overwhelm users and cause decision fatigue that undermines the intended safety benefit, and current alerts assume a security literacy many users lack, so they approve risky actions blindly or overreact to benign ones. Practical systems need principled criteria for when to defer to human judgment and informative yet lightweight explanations.

## Defense mechanisms and the risks they cover

Table 2 lists each mechanism with its category and covered risks; the five rows below are the runtime-protection category, and the full table's repeated category column and expanded risk names are shortened here because they are too wide to read comfortably.

| Category | Mechanism | Representative works | Covered risks |
| --- | --- | --- | --- |
| Runtime protection | Input guardrail | Prompt Guard2 [22], PromptShield [55], DataSentinel [82], PromptArmor [123], URL allowlist [46] | R1 |
| | Output guardrail | CodeShield [85], Firewalled Agentic Networks [1], Task Shield [57], GuardAgent [146], Agrail [84], AlignmentCheck [22], ControlValve [56], Conseca [132], Progent [122], Maris [27] | R2, R4, R5, R6 |
| | Information flow control and taint tracking | Permissive [124], MELON [160], RTBAS [158], AgentArmor [136], PFI [60], CaMeL [29], FIDES [26], ACE [69], PrivacyChecker [137] | R3, R5, R6 |
| | Monitoring | AgentAuditor [83], AgentMonitor [93], SentinelAgent [51] | R5, R6, R7 |
| | Human-in-the-loop | Wu et al. [145] | R5, R6, R7 |

## Key points

- The goals are confidentiality, integrity and availability plus contextual security, which keeps an agent's context aligned with the intended task and governs admissible, prioritized context elements.
- Confidentiality addresses R3 and R5; integrity addresses R1, R2, R3, R4 and R6; availability addresses R7; contextual security complements the other two rather than mapping to one risk.
- Input guardrails validate inputs before the agent sees them and mitigate R1; output guardrails check outward behavior for R2, R4, R5 and R6 and cost more resources because they depend on the LLM's output.
- Information flow control and taint tracking use security labels and lattice constraints against R3 and mitigate R5 and R6, at the cost of runtime overhead and label creep.
- Monitoring and human-in-the-loop validation both mitigate R5, R6 and R7, the former trading detection power against storage, computation and privacy exposure, the latter risking decision fatigue.
- The runtime mechanisms overlap in coverage yet none spans R1–R7, so they are applied together rather than singly.

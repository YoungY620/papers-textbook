# Seven design dimensions that decide the risk

An AI agent is a hybrid system that combines traditional software components with neural components; its LLM and workflow together form the decision-making core. What the agent can do is therefore not set by the model alone but by how the system is composed — which inputs it accepts, what it remembers, which tools it can reach, which actions it may take, and how a user talks to it. The same composition that makes an agent capable is what makes it dangerous, so the composition is the natural unit of a security analysis.

Seven dimensions characterize agent design: input trust, access sensitivity, workflow, action, memory, tool, and user interface. Each is a continuum rather than a category, running from a least flexible setting, in which the system does little beyond what an ordinary program would do, to a most flexible setting, in which the system decides for itself. Three representative levels — least, moderately, and most flexible — keep the comparison tractable; an agent can operate at any point along these spectrums.

| Dimension | Level 1: Least flexible | Level 2: Moderately flexible | Level 3: Most flexible |
| --- | --- | --- | --- |
| Input Trust | No external data [2, 43, 130] | Predefined external data [68] | Arbitrary external data [8, 105, 147] |
| Access Sensitivity | No sensitive data [2, 43, 130] | Predefined sensitive data [101] | Arbitrary sensitive data [28, 108] |
| Workflow | Simple chatbot [2, 43, 130] | Fixed, Developer-defined [61] | Dynamic, LLM-defined [139, 147, 150] |
| Action | LLM response only [2, 43, 130] | LLM response, Retrieval [68, 101] | LLM response, Retrieval, Execution [28, 108] |
| Memory | No memory [2, 43, 130] | Transient session memory [63] | Persistent memory across sessions [66, 102] |
| Tool | No tool [2, 43, 130] | Known tools [116] | Arbitrary tools [105] |
| User Interface | Text-only [2, 43, 130] | Web-based image preview [42] | Interactable Web elements [41, 100] |

## Input Trust

This dimension categorizes the trustworthiness of the external data sources an agent relies on, progressing from no external data, the highest-trust setting, through predefined external data, to arbitrary and potentially untrusted sources, the lowest-trust but most flexible setting. Moving up buys knowledge and better decisions, because the agent can consult more diverse material. It also buys exposure: every retrieved document, page, or snippet is content an attacker may control, so a compromised or malicious source can steer the agent's behaviour. This dimension governs whether indirect prompt injection is reachable at all.

## Access Sensitivity

This dimension categorizes the agent's access to sensitive data within the system or environment, increasing from none, to known sensitive data sources, to arbitrary sensitive data. Higher levels let the agent take on tasks that genuinely require sensitive information. The security consequence is scope: the same flexibility that enables those tasks widens what a breach can reach, so the impact of a compromise grows with the level. At the least flexible setting an agent has little to lose; at the most flexible setting the user's most valuable data is within reach.

## Workflow

This dimension concerns the action sequences the agent follows and who defines them, the closest analogue to code in traditional software. It moves from no complex workflow, in effect a simple chatbot, to developer-defined fixed workflows, to dynamic workflows the LLM composes at run time. Rigid, predetermined sequences give way to flexible, context-aware task planning, which lets an agent adapt to a task it was not written for. The consequence is that control flow itself becomes an attack surface: when the model rather than the developer chooses the sequence, injected content has more opportunity to hijack the reasoning and redirect what the agent does next.

## Action

This dimension specifies the operations an agent can perform, increasing from generating a response only, to adding retrieval, to executing environment-modifying actions. Retrieval lets the agent read; execution lets it change the world. The consequence is operational impact: at the top of the scale mistakes are no longer confined to text, and a disclosure becomes a modification, because reaching the environment turns a leak into corruption. This dimension is closely related to the tool dimension, since execution generally requires a corresponding tool.

## Memory

This dimension categorizes how the agent stores and retrieves information: stateless operation, transient session memory, and persistent cross-session memory. Each step up enables more sophisticated learning, personalization, and accumulation of knowledge. Its security consequence is duration. Transient memory is discarded with the session, whereas persistent memory outlives any single interaction, so anything written into it, including attacker-supplied content, keeps influencing later behaviour, and sensitive data that accumulates there stays available to later reads.

## Tool

This dimension categorizes the range of tools available to an agent, increasing from none, to known and vetted tools, to arbitrary tools it can discover and use dynamically. The progression maximizes functional capability by expanding the agent's ability to interact with diverse systems and environments. The price is a wider attack surface: third-party tools arrive with their own trust level, and a tool's name, description, or implementation can itself carry the attack. This dimension directly enables the action dimension, because more sophisticated actions typically require more diverse tools.

## User Interface

This dimension defines how a user interacts with the agent, increasing from text-only interaction, to web-based previews and media rendering, to fully interactive web elements and dynamic interfaces. Richer interfaces support richer experiences and more complex interaction patterns. They also add channels a text-only agent lacks: rendering a link can cause an automatic fetch, an interactive element can carry a command that changes the environment, and the interface itself can be manipulated to mislead the user.

## How the dimensions compound

The dimensions are orthogonal and can be used in the same agent, so one agent can hold different levels along different dimensions, including the most flexible level on all seven at once. Two axes are coupled: the tool dimension directly enables the action dimension, which is described as closely related to it. Because the axes are orthogonal while their capabilities reinforce one another, flexibility rarely stays contained to a single one of them. An agent that plans dynamically also selects tools dynamically, so an arbitrary input can be routed by that planner into a sensitive action. Flexibility is therefore the right axis for organizing agent security: it is the one property that purchases capability and exposure in the same move, and it can be measured on one scale for agents that otherwise look nothing alike. Greater flexibility amplifies security risks.

## From dimensions to the risk taxonomy

The design dimensions are what the risk taxonomy is built on, and the mapping connects the two halves of the analysis.

![Relationship between agent design dimensions and risks.](assets/fig3-dimensions-risks.png)

The dimensions map to three groups of risks. Input Trust, Memory, and Tool directly contribute to an increased attack surface (R1, heterogeneous untrusted interfaces): expanding external data sources enables indirect prompt injection, persistent memory creates memory-poisoning targets, and third-party tools introduce supply chain risks. Workflow primarily drives the model risks (R2, wrong instruction following; R3, unconstrained or unsafe data flow; R4, hallucination and model mistakes), because flexible control flows give more opportunities to hijack the agent's reasoning, and hallucination becomes consequential once the agent dynamically selects the tools and resources its incorrect output will act on. Access Sensitivity, Action, and User Interface determine the severity of the consequence risks (R5, private data leakage; R6, unintended or unauthorized action and data corruption; R7, resource drain and denial of service): more sensitive access amplifies the impact of a violation, action beyond response turns disclosure into environment corruption, and complex interfaces add channels for unauthorized fetches, destructive commands, and interface manipulation.

The risks then interact as a cascade. R1 widens the entry points through which attacker-controlled data reaches the model risks, which in turn amplify the consequence risks: wrong instruction following can produce exfiltration, corruption, or resource drain, unconstrained data flow heightens the confidentiality and integrity risks, and hallucination makes the agent operate on fabricated resources. The taxonomy also covers residual risks aimed at the agentic system itself, such as theft of system prompts, tool descriptions, and configurations, and side channels visible in tool execution timing, API call sequences, and network traffic patterns; it is connected to MITRE ATLAS. The practical use of the mapping is that an agent's flexibility profile — its level on each of the seven dimensions — decides which risks are reachable for it at all, and no single component can be secured in isolation.

## Key points

- Seven dimensions characterize agent design, each a flexibility continuum with least, moderately, and most flexible levels: input trust, access sensitivity, workflow, action, memory, tool, and user interface.
- Every step up a dimension trades capability for exposure: it adds knowledge, reach, or persistence while enlarging the attack surface or the impact of a compromise.
- Workflow is the analogue of source code, and moving it from developer-defined to LLM-defined turns control flow itself into an attack surface that injected content can hijack.
- Tool enables Action, and Action is where mistakes stop being textual: retrieval reads, while execution changes the environment, so disclosure becomes corruption.
- Memory adds duration: persistent cross-session memory is both a poisoning target and a store of sensitive data that outlives the session.
- Because the dimensions are orthogonal, one agent can be at the most flexible level on all seven at once, and flexibility rarely stays isolated to one dimension.
- Input Trust, Memory, and Tool feed the attack surface (R1); Workflow drives the model risks (R2–R4); Access Sensitivity, Action, and User Interface set the severity of the consequence risks (R5–R7).
- Those risks cascade from R1 through the model risks to the consequence risks, so agent security must be addressed at the system level, not component by component.

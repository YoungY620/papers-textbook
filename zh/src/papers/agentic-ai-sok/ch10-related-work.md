# 相关工作与基线

知识体系化（SoK）与"相关工作"的关系有些特殊：它综述的文献就是证据，"覆盖了什么"与"相对已有综述的差异"是同一件事。本章把这篇 SoK 放回它依据的文献中：它用于定位的综述、归入 `V1`…`V6` 的攻击工作、Table 2 的防护系统，以及它对接的两个框架。

## 综述版图

第一类综述以**模型**为对象。Liu 等人把提示注入形式化为框架，使已有攻击成为特例，在 10 个 LLM、7 类任务上评测 5 种攻击与 10 种防护 [81]；Jia 等人论证已有评测缺乏原则，并发现 StruQ、SecAlign 与指令层级训练既损失通用能力、又仍被既有攻击绕过，自适应攻击下更甚 [58]；Wang 等人梳理越狱护栏，认为该领域碎片化、缺乏通用性 [138]；Grosse 等人追问威胁模型是否现实 [49]。SoK 反对的理由是它们度量错了边界：智能体的损害来自模型与软件的合成，只覆盖模型接口的威胁清单无法表达"检索到的文档如何影响后续工具调用参数"。

第二类是更窄的智能体研究。Agent Security Bench 用 10 个场景、10 个智能体、400 余个工具、27 种方法、7 项指标做攻防基准 [155]。Hou 等人只研究模型上下文协议，给出四阶段、十六项活动的服务器生命周期与四类攻击者、十六种威胁场景 [52]。Beurer-Kellner 等人提出可证明抵抗提示注入的设计模式 [12]，Zhang 等人以立场论文主张显式采用安全原则 [156]。论文自认最接近的两篇考虑跨组件交互、但防护分类基本限于模型类技术：Deng 等人的综述 [31] 与 TrustAgent 综述——后者内部维度（大脑、记忆、工具）与外部维度（用户、智能体、环境）并列，技术视角覆盖攻击、防护与评测 [151]。

SoK 主张的不是覆盖更多论文，而是不同的组织对象：以七个设计维度（输入信任、访问敏感性、工作流、动作、记忆、工具、用户界面）刻画智能体，使风险取决于智能体在灵活性谱系上的位置，此前分类法无此表达力。其范围是 2023 年至 2025 年 10 月的 128 篇文献（51 篇攻击、60 篇防护）。

## 攻击文献

### 外部攻击者：`V1`、`V2`、`V3`

`V1` 由 Greshake 等人奠定：攻击者与系统毫无接口，仍可把提示词放进"很可能被检索"的数据中操纵系统，影响涵盖数据窃取到蠕虫式传播 [48]。InjecAgent 把它变成可度量的问题：1,054 个用例、17 个用户工具与 62 个攻击者工具，分"直接危害"与"窃取数据"两类；ReAct 提示的 GPT-4 有 24% 中招，再加"越狱提示"时近乎翻倍 [153]。两者都假定智能体必须读取攻击者可达的内容，攻击才成立。

`V2` 注入数据而非指令。Spracklen 等人在 16 个代码生成 LLM、576,000 个样本上量化了一例：商业模型推荐的包名至少 5.2%、开源模型至少 21.7% 不存在，共 205,474 个可被注册并填入恶意代码的唯一名字 [127]。恶意意图根本没进入模型，进入的只是被误当成事实的名字，故 SoK 同时归入 `V2` 与"幻觉被利用"（`R4`）。

`V3` 针对工具供应链。Les Dissonances 提出跨工具收割与污染：恶意工具进入任务控制流并劫持工具执行顺序，其扫描器发现 LangChain 与 Llama-Index 的 66 个真实工具中 75% 可被利用 [74]。ToolHijacker 优化恶意工具文档，使"先检索后选择"的两步流程在给定任务上稳定选中攻击者的工具，并报告 StruQ、SecAlign 与已知答案检测、DataSentinel、困惑度检测均不足 [121]。两者都利用工具维度上"任意工具"的一端。

### 用户级攻击者：`V4`

HouYi 是对直接提示注入的系统处理：由框架、分隔符、干扰器三段组成的黑盒载荷，思路取自 SQL 注入与 XSS；在 36 个真实应用上测试，31 个可被注入，86.1% 成功窃取原始提示或消耗算力 [80]。Perez 与 Ribeiro 确立基本手法 [107]，后续工作将其自动化 [79]，并经工具操纵与图像扩展 [39, 40]。SoK 把相同载荷按攻击者位置而非技术重排：`V4` 属直接输入的用户，`V1` 属无法接触的外部方。

### 内部攻击者：`V5`、`V6`

`V5` 模型投毒被 SoK 视为最难的向量，因为需要开发者或组件供应商把隐藏行为嵌入模型 [19, 91]；此处引用的是模型层面的安全与越狱工作，而该向量之所以存在，是因为组件供应商是用户无法审计的攻击者。

`V6` 记忆投毒最密集。AgentPoison 把触发器优化到特定嵌入区域，对长期记忆或 RAG 知识库实施后门，无需训练模型，毒化率低于 0.1% 时成功率至少 80%、对良性性能影响不超过 1%，覆盖自动驾驶、问答与医疗三类智能体 [21]。PoisonedRAG 把知识库污染形式化为带两个耦合目标的优化：毒化文本既要进入前 k 条检索结果，又要引导生成目标答案 [162]。MINJA 进一步削弱其最强假设——不写记忆库，仅靠提问注入记录，用桥接步骤把受害者查询接到恶意推理步骤，并以逐步缩短的提示使其日后自然被检索 [34]。三者依次削去攻击所需权限，`V6` 把它们吸收为由"组件访问权"而非注入机制定义的向量。

六个向量构成一张图而非清单：攻击面扩大（`R1`）引入攻击者可控数据，数据触及模型类风险（`R2`–`R4`），后者再放大后果类风险（`R5`–`R7`）。单篇攻击论文给不出这一论证，因为每篇只固定一个向量、一种设定。

## 防护文献

### 输入与输出护栏

NeMo Guardrails 提供描述输入过滤器的领域专用语言 [110]；Constitutional classifiers 用"宪法"训练分类器抵抗通用越狱 [119]；LlamaFirewall 是开源护栏框架 [22]；PromptShield 与 PromptArmor 检测并剔除注入提示 [55, 123]；DataSentinel 反用易受注入的模型提高检出率 [82]；网络白名单限制检索与出网 [46]。输出侧，CodeShield 与 HeimdallM 静态分析生成的代码以阻止任意执行 [85, 89]；Task Shield 强制任务一致性 [57]；GuardAgent 把安全请求转成可执行的护栏代码 [146]；Conseca 依运行时上下文生成策略 [132]；Progent 把权限表达为作用在工具名与参数上的符号规则，用 SMT 求解器判定每次更新是"收缩"（自动应用）还是"扩张"（需批准），使动作空间不经同意只能缩小 [122]。SoK 的判断是瓶颈在判定标准：模型类检测器可被自适应攻击绕过，规则类需大量人力，两者都产生假阳性与假阴性。

### 信息流控制与污点追踪

PFI 综合智能体隔离、不可信数据的安全处理与提权护栏 [60]。CaMeL 从可信查询中提取控制流与数据流，使不可信数据无法影响程序流程，并给数据附加能力以阻止经未授权流向的泄露，在 AgentDojo 上以可证明安全性完成 77% 的任务（未防护为 84%）[29]。FIDES 确定性追踪机密性与完整性标签，并提供选择性隐藏与揭示信息的原语 [26]。MELON 以掩蔽用户提示的方式重放轨迹并比较工具调用，依据是攻击成功时下一步动作更不依赖用户任务 [160]。RTBAS 用两个依赖筛查器（LM 作裁判、注意力显著性），仅在无法自动确认完整性与机密性时才升级到用户确认 [158]。Permissive IFC 用多次推理度量单个输入的影响以避免标签过保守 [124]，AgentArmor 把运行时轨迹当程序分析 [136]。SoK 点出各论文未言明的共同维度——符号变量、多次执行、模型判定三类机制，完整性目标与机密性目标之分——并指出缺口：运行时开销大，保守传播造成标签蔓延，缺少安全降级规则时智能体将不可用。

### 监控与人在回路验证

AgentMonitor 在网页与文件访问环境中为行为风险打分 [93]；AgentAuditor 用结构化特征与推理链构建经验记忆并检索相似案例，基准含 2,293 条标注记录、15 类风险 [83]；SentinelAgent 以交互图建模检测多智能体系统的异常 [51]。人在回路验证相对而言为智能体特有：编程智能体在写文件或执行命令前请求批准，防护系统在策略将被违反时回退到确认 [26, 29, 60, 144]；Wu 等人用机器学习建模用户权限偏好以降低提示频率 [145]。其局限是决策疲劳与告警预设的安全素养落差。

### 权限分离与形式化验证

AirGapAgent 针对第三方应用操纵上下文套取隐私，只保留任务相关数据、在该最小化上下文上执行任务，并以分发送方上下文阻止冒充 [11]。f-secure 把 LLM 系统拆成流水线，由安全监视器过滤进入规划环节的不可信输入 [142]；CaMeL、FIDES、PFI 则分离"规划"与"解析"，或把工具分为普通版与沙箱版 [26, 29, 60]。IsolateGPT 为移动系统生成按应用隔离的子智能体 [144]，IPIGuard 借助工具依赖图 [4]，DRIFT 组合安全规划器、监测偏离计划轨迹的动态验证器、掩蔽冲突指令的注入隔离器 [70]。SoK 点出隐含的共同轴——"规划器—解析器"的纵向分离与按范围的横向分离——并指出这些演示都在简化环境下完成。形式化验证最单薄：Formal-LLM 把工具调用顺序等开发者约束编码为下推自动机 [75]，VeriSafe Agent 把用户意图形式化为作用在 UI 状态迁移上的 DSL 并据此校验 GUI 动作 [67]，ShieldAgent 把外部策略文档编译成作用在动作轨迹上的规则电路 [20]。

### 身份与访问管理、组件加固

身份工作多关于委托：authenticated delegation 主张智能体需要带可验证授权的委托原语 [126]，SAGA 是治理智能体系统的安全架构 [128]，agent network protocol 处理智能体间身份 [16]。访问控制主要面向向量库：Bedrock 依权限用元数据过滤检索结果 [3]，Honeybee 沿 RBAC 结构动态分区 [157]，ControlNet 用神经元激活充当 RAG 防火墙 [149]。凭证管理依靠令牌保管库与一次性存储 [10, 103]。加固分两侧：模型侧 SecAlign 用偏好优化使模型坚持原始指令 [18]，StruQ 用结构化查询分隔提示与数据 [17]，指令层级训练让模型排序系统、用户与第三方指令 [134, 143]；工具侧 ETDI 为工具定义加签名与版本 [33]，Anthropic 的 Connectors Directory 维护经审核的工具目录 [7]，MCP Context Protector 以代理方式插入人工复核 [131]，MCP Safety Audit 检查工具中可被利用的逻辑或误导性描述 [109]，MCIP 为 MCP 增加可观测性与微调过的威胁检测器 [59]。SoK 的结论是加固针对的威胁模型过于简化——指令层级微调只处理系统提示、用户提示与工具结果，无法应对遮蔽攻击（一份恶意工具结果覆盖其他工具结果）；独立评测支持这一怀疑：Jia 等人发现这些防护既有可用性代价，又可在自适应攻击下被绕过 [58]。

## MITRE ATLAS、OWASP 与 MCP

两个框架提供词汇而非结论。OWASP 的 LLM 应用 Top 10 在构建风险分类时被参考 [104]。MITRE ATLAS 提供技术名称，附录把 SoK 的标识符映射上去：`V1` 对应 Retrieval Content Crafting、Drive-by Compromise、Prompt Infiltration via Public-Facing Applications；`V4` 对应 LLM Prompt Injection；`V5` 对应 Poison Training Data、Publish Poisoned Datasets、Publish Poisoned Models；`V6` 对应 RAG Poisoning、False RAG Entry Injection、AI Agent Context Poisoning；`R2` 对应 AI Agent Tool Invocation；`R5` 含 Credentials from AI Agent Configuration、OS Credential Dumping、RAG Credential Harvesting、Unsecured Credentials、LLM Response Rendering；`R6` 对应 Modify AI Agent Configuration、LLM Trusted Output Components Manipulation、External Harms；`R7` 对应 Denial of AI Service、External Harms。

MCP 把工具使用标准化：一套定义、发现与调用工具的协议，具备动态 schema 协商、双向通道，并把访问控制与能力协商列为一等特性 [6]。其文献说明标准化本身就是攻击面：Hou 等人枚举恶意开发者、外部攻击者、恶意用户与安全缺陷四类来源下的十六种场景——工具投毒、安装包冒名、未授权访问——并以真实案例验证 [52]；MCP Safety Audit 展示了 MCP 接入系统中可被利用的严重行为 [109]。工具加固正是回应：ETDI 的签名、Context Protector 的复核代理、MCIP 的检测器，都在为"设计上开放"的发现通道重建信任。

## 既有工作未覆盖之处

没有工作按设计维度分析风险，故无人能指出哪个部署选择让已演示的攻击变得可行；也没有工作对风险交互建模，故从 `R1` 经 `R2`–`R4` 到 `R5`–`R7` 的级联始终未被分析。侧信道（工具执行时序、API 调用序列、流量模式）按论文掌握此前完全没有研究；智能体身份与凭证、自适应访问控制、概率智能体的形式化模型则被列为基础性问题而非已解决问题。

## 已查阅的文献

以下为本章下载并阅读的文献；方括号内为论文中的参考文献编号。

- Greshake 等, *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*, AISec 2023 [48] — https://arxiv.org/abs/2302.12173
- Zhan 等, *InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents*, ACL 2024 [153] — https://arxiv.org/abs/2403.02691
- Yi 等, *Benchmarking and Defending Against Indirect Prompt Injection Attacks on LLMs*（BIPIA）, KDD 2025 — https://arxiv.org/abs/2312.14197（论文未引用）
- Liu 等, *Prompt Injection attack against LLM-integrated Applications*（HouYi）[80] — https://arxiv.org/abs/2306.05499
- Li 等, *Les Dissonances: Cross-Tool Harvesting and Polluting in Pool-of-Tools Empowered LLM Agents* [74] — https://arxiv.org/abs/2504.03111
- Shi 等, *Prompt Injection Attack to Tool Selection in LLM Agents*（ToolHijacker）[121] — https://arxiv.org/abs/2504.19793
- Spracklen 等, *We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs*, USENIX Security 2025 [127] — https://arxiv.org/abs/2406.10279
- Chen 等, *AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases*, NeurIPS 2024 [21] — https://arxiv.org/abs/2407.12784
- Dong 等, *Memory Injection Attacks on LLM Agents via Query-Only Interaction*（MINJA）[34] — https://arxiv.org/abs/2503.03704
- Zou 等, *PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models*, USENIX Security 2025 [162] — https://www.usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf
- Debenedetti 等, *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*, NeurIPS 2024 [30] — https://arxiv.org/abs/2406.13352
- Liu 等, *Formalizing and Benchmarking Prompt Injection Attacks and Defenses*, USENIX Security 2024 [81] — https://arxiv.org/abs/2310.12815
- Jia 等, *A Critical Evaluation of Defenses against Prompt Injection Attacks* [58] — https://arxiv.org/abs/2505.18333
- Wang 等, *SoK: Evaluating Jailbreak Guardrails for Large Language Models*, IEEE S&P 2026 [138] — https://arxiv.org/abs/2506.10597
- Yu 等, *A Survey on Trustworthy LLM Agents: Threats and Countermeasures*（TrustAgent）[151] — https://arxiv.org/abs/2503.09648
- Zhang 等, *Agent Security Bench (ASB)*, ICLR 2025 [155] — https://arxiv.org/abs/2410.02644
- Hou 等, *Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions* [52] — https://arxiv.org/abs/2503.23278
- Beurer-Kellner 等, *Design Patterns for Securing LLM Agents against Prompt Injections* [12] — https://arxiv.org/abs/2506.08837
- Zhang 等, *LLM Agents Should Employ Security Principles* [156] — https://arxiv.org/abs/2505.24019
- Shi 等, *Progent: Securing AI Agents with Privilege Control* [122] — https://arxiv.org/abs/2504.11703
- Debenedetti 等, *Defeating Prompt Injections by Design*（CaMeL）[29] — https://arxiv.org/abs/2503.18813
- Costa 等, *Securing AI Agents with Information-Flow Control*（FIDES）[26] — https://arxiv.org/abs/2505.23643
- Kim 等, *Prompt Flow Integrity to Prevent Privilege Escalation in LLM Agents*（PFI）[60] — https://arxiv.org/abs/2503.15547
- Wu 等, *System-Level Defense against Indirect Prompt Injection Attacks: An Information Flow Control Perspective*（f-secure）[142] — https://arxiv.org/abs/2409.19091
- Zhu 等, *MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents*, ICML 2025 [160] — https://arxiv.org/abs/2502.05174
- Zhong 等, *RTBAS: Defending LLM Agents Against Prompt Injection and Privacy Leakage* [158] — https://arxiv.org/abs/2502.08966
- Siddiqui 等, *Permissive Information-Flow Analysis for Large Language Models* [124] — https://arxiv.org/abs/2410.03055
- Bagdasarian 等, *AirGapAgent: Protecting Privacy-Conscious Conversational Agents*, CCS 2024 [11] — https://arxiv.org/abs/2405.05175
- Wang 等, *AgentArmor: Enforcing Program Analysis on Agent Runtime Trace to Defend Against Prompt Injection* [136] — https://arxiv.org/abs/2508.01249
- Li 等, *DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents* [70] — https://arxiv.org/abs/2506.12104
- He 等, *SentinelAgent: Graph-based Anomaly Detection in LLM-based Multi-Agent Systems* [51] — https://arxiv.org/abs/2505.24201
- Luo 等, *AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents* [83] — https://arxiv.org/abs/2506.00641
- Xiang 等, *GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning* [146] — https://arxiv.org/abs/2406.09187
- Shi 等, *PromptArmor: Simple yet Effective Prompt Injection Defenses* [123] — https://arxiv.org/abs/2507.15219
- Chennabasappa 等, *LlamaFirewall: An open source guardrail system for building secure AI agents* [22] — https://arxiv.org/abs/2505.03574
- Sharma 等, *Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming* [119] — https://arxiv.org/abs/2501.18837
- Hines 等, *Defending Against Indirect Prompt Injection Attacks With Spotlighting* — https://arxiv.org/abs/2403.14720（论文未引用）
- Chen 等, *StruQ: Defending Against Prompt Injection with Structured Queries*, USENIX Security 2025 [17] — https://arxiv.org/abs/2402.06363
- Chen 等, *SecAlign: Defending Against Prompt Injection with Preference Optimization*, CCS 2025 [18] — https://arxiv.org/abs/2410.05451
- Wallace 等, *The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions* [134] — https://arxiv.org/abs/2404.13208
- Tsai 与 Bagdasarian, *Contextual Agent Security: A Policy for Every Purpose*（Conseca）, HotOS 2025 [132] — https://arxiv.org/abs/2501.17070
- Lee 等, *VeriSafe Agent: Safeguarding Mobile GUI Agent via Logic-based Action Verification* [67] — https://arxiv.org/abs/2503.18492
- Li 等, *Formal-LLM: Integrating Formal Language and Natural Language for Controllable LLM-based Agents* [75] — https://arxiv.org/abs/2402.00798
- Yao 等, *ControlNet: A Firewall for RAG-based LLM System* [149] — https://arxiv.org/abs/2504.09593
- Zhong 等, *Honeybee: Efficient Role-based Access Control for Vector Databases via Dynamic Partitioning* [157] — https://arxiv.org/abs/2505.01538
- Radosevich 与 Halloran, *MCP Safety Audit: LLMs with the Model Context Protocol Allow Major Security Exploits* [109] — https://arxiv.org/abs/2504.03767

未能获取。IsolateGPT [144]（NDSS 2025）找不到可访问的开放版本；Deng 等人的 *AI Agents Under Threat* [31]（ACM Computing Surveys）与 Grosse 等人 [49]（USENIX Security 2024）位于出版方付费墙之后。以厂商文档或代码仓库形式引用的工作——Bedrock 访问控制 [3]、CodeShield 与 HeimdallM [85, 89]、ETDI [33]、MCP Context Protector [131]、Anthropic Connectors Directory [7]、Auth0 令牌保管库 [10]、Composio 与 Okta [24, 97]——按文档阅读。IPIGuard [4]、ACE [69]、SAGA [128]、authenticated delegation [126]、agent network protocol [16]、Maris [27]、ControlValve [56] 与 ShieldAgent [20] 亦未获取，它们依据 Table 2 与论文的描述被提及，而非依据直接阅读。

## 本章要点

- 论文对比的综述分两类：模型层面的 LLM 安全研究，与更窄的智能体研究（攻防基准、MCP 研究、设计模式与安全原则立场论文）；另有两篇考虑跨组件交互但防护仍以模型类技术为主。
- SoK 的差异在组织对象：七个设计维度使风险取决于智能体在灵活性谱系上的位置，加上覆盖组件及交互的统一风险分类与结合系统级机制的纵深防御框架。
- 攻击工作按攻击者位置映射到 `V1`–`V6`；记忆投毒一线（AgentPoison、PoisonedRAG、MINJA）依次削去攻击所需权限，直到只剩查询访问。
- SoK 的增量是风险交互论证（`R1` 引入攻击者可控数据，触及 `R2`–`R4`，放大 `R5`–`R7`）与为防护命名的共同设计轴。
- 防护覆盖不均衡：信息流控制最强，护栏瓶颈在判定标准，监控与监督受制于随机性与决策疲劳，访问控制局限于向量库，形式化验证只有寥寥数项。
- 设计维度分析、风险交互、侧信道、智能体身份、自适应访问控制与概率智能体的形式化模型，正是 SoK 的开放挑战。

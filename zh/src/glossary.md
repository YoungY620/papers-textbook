# 术语表

本书出现的术语一览，与正文中悬浮卡片里的一句话释义一致。每条另附该术语首次出现的章节。

[A](#gloss-a) · [B](#gloss-b) · [C](#gloss-c) · [D](#gloss-d) · [E](#gloss-e) · [F](#gloss-f) · [G](#gloss-g) · [H](#gloss-h) · [J](#gloss-j) · [K](#gloss-k) · [L](#gloss-l) · [M](#gloss-m) · [N](#gloss-n) · [P](#gloss-p) · [Q](#gloss-q) · [R](#gloss-r) · [S](#gloss-s) · [T](#gloss-t) · [W](#gloss-w) · [X](#gloss-x) · [Y](#gloss-y) · [Z](#gloss-z)

<a id="gloss-a"></a>

## A

<a id="term-secure-value-recovery"></a>

**安全值恢复** — *Secure Value Recovery*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 10 章</span>

Signal 基于 PIN 的密钥恢复系统，跨多个安全区与云厂商分层，使任何单一一方都无法恢复秘密。

Connell 等报告它在安全区内存内无条件限制 PIN 猜测次数并带回滚保护，这正是论文希望硬件托底的密钥托管具备的性质。


<a id="term-enclave"></a>

**安全区** — *enclave*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 10 章</span>

处理器内受保护的区域，使代码与数据对机器运营方保密，可用来保管恢复密钥。

Secure Value Recovery 有意把信任分摊到不同架构的安全区上，依据是对手不太可能同时攻破多个。


<a id="term-security-label"></a>

**安全标签** — *security label*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

信息流控制中标记单份数据可信或保密级别的标签，决定哪些流动被允许。


<a id="term-declassification"></a>

**安全标签降级** — *declassification*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

在安全时原则性地放宽安全标签，使易发生标签蔓延的智能体保持可用而不失安全。


<a id="term-secure-by-design"></a>

**安全设计** — *Secure by Design*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

把安全性构建进智能体的结构与设计选择中，而非在运行时才追加。


<a id="term-security-risk-taxonomy"></a>

**安全风险分类法** — *Security Risk Taxonomy*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

把七条智能体安全风险（R1–R7）对应到攻击者可瞄准组件的分类框架。

分类法按组件而非严重性组织，因此一次事件通常同时触发多条风险。


<a id="gloss-b"></a>

## B

<a id="term-vault-indistinguishability"></a>

**保险库不可区分性** — *vault indistinguishability*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

攻击者连保险库彼此都区分不开的目标，比只知道明文更进一步。


<a id="term-vault-integrity"></a>

**保险库完整性** — *vault integrity*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

保证保险库中的条目与设置仍是用户存下的那一份，形式与顺序都未被改动。

逐条目使用 AE 并不能提供它：条目与字段仍可被调换、删除、复制或拼接，KDF 参数之类的明文元数据也能被改动。


<a id="term-vault-key"></a>

**保险库密钥** — *vault key*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

真正加密保险库的密钥，它本身由主密码派生的密钥保护。

按报告的描述，主密码封装保险库密钥，保险库密钥再加密保险库，主密码并不直接用于加密条目。


<a id="term-label-creep"></a>

**标签蔓延** — *label creep*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

保守标签传播的失效：标签过于严格使智能体不可用，除非有安全的降级规则。

SoK 把它列为智能体信息流控制的开放问题之一（另一项是运行时开销）；解决它需要原则性的降级规则，只在确实安全时放宽标签。


<a id="term-oblivious-client-operations"></a>

**不经意客户端操作** — *oblivious client operations*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

客户端在不向服务器泄露自己访问内容的前提下完成操作的目标。


<a id="gloss-c"></a>

## C

<a id="term-side-channel-risk"></a>

**侧信道风险** — *Side-Channel Risk*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

经工具执行耗时、API 调用序列或网络流量模式等可观察行为泄露的信息。

目前尚无研究考察智能体系统中的这类侧信道攻击，相关分析留待后续工作。


<a id="term-super-admin"></a>

**超级管理员** — *super admin*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

LastPass 团队中的特权账户，可以重置其他成员的主密码。

每个此类账户持有一对 RSA 密钥 (sk_adm, pk_adm)；客户端登录时取回的正是这些公钥。


<a id="term-master-password-reset"></a>

**主密码重置** — *master password reset*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

LastPass 企业版功能，允许超级管理员重置团队成员的主密码。

被选中用户的客户端会把用户密钥在各管理员的 RSA 公钥下加密；只有浏览器扩展支持这套密钥交换流程，这正是攻击 LP01 的场景。


<a id="term-cbc-only-downgrade"></a>

**纯 CBC 降级** — *CBC-Only Downgrade*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

攻击 DL05：伪造的 Dashlane 设置让客户端此后一律以纯 CBC 加密事务，暴露于填充预言之下。


<a id="term-wrong-instruction-following"></a>

**错误指令跟随** — *Wrong Instruction Following*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

智能体执行攻击者注入的提示，而非良性用户或开发者本来的指令。

编号 R2，属完整性失效。其向量为 V1 间接提示注入、V4 直接提示注入，以及 V6 记忆投毒植入的指令。


<a id="gloss-d"></a>

## D

<a id="term-llm-defined-workflow"></a>

**大模型定义的工作流** — *LLM-Defined Workflow*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

由模型在运行时组合、而非事先固定的动作序列，是工作流维度的最灵活档位。

灵活的控制流让智能体能适应并未为之编写的任务，也让注入内容有更多机会劫持智能体的推理。


<a id="term-proxy-delegation"></a>

**代理委托** — *proxy delegation*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

让智能体经由中间服务或令牌代表用户行事，是论文所列三种委托模型之一。


<a id="term-single-sign-on"></a>

**单点登录** — *single-sign-on*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

在多个服务间统一认证与授权的机制；Okta 与 Composio 用它管理智能体访问与凭证供给。


<a id="term-kdf-iteration-count"></a>

**KDF 迭代次数** — *KDF iteration count*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

决定基于口令的密钥派生有多昂贵的参数，也就是猜测一次口令的成本。

攻击 BW07 与 LP04 之所以能降低它，是因为该设置以未加密、未认证的形式存放在服务器上；客户端登录时送出的哈希因此几乎不花代价就能被检验。


<a id="term-iteration-count"></a>

**迭代次数** — *iteration count*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

密钥派生函数重复的轮数，决定猜测口令所需的代价。

恶意服务器可以把它调低，从而消除暴力破解保护；论文的 BW07 与 DL03 攻击正是如此。


<a id="term-action-space"></a>

**动作空间** — *Action Space*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

智能体借助工具可执行的操作集合，包含读、写、执行三类。


<a id="term-dynamic-credential-management"></a>

**动态凭证管理** — *dynamic credential management*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

使用到期自动失效的限时令牌，缩小暴露窗口，代价是续期复杂、可能中断服务。


<a id="term-end-to-end-encryption"></a>

**端到端加密** — *end-to-end encryption*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

只有通信两端持有密钥、服务器只经手无法读取的密文的设计。

云存储与密码管理器厂商常把这种设计称为零知识加密，论文则把它当作待检验的声明而非既有性质。


<a id="gloss-e"></a>

## E

<a id="term-malicious-data-injection"></a>

**恶意数据注入** — *Malicious data injection*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

投递数据而非指令，如被幻觉出的包名，在敏感操作中被使用时造成危害。


<a id="gloss-f"></a>

## F

<a id="term-access-sensitivity"></a>

**访问敏感度** — *Access Sensitivity*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

智能体可触达的敏感数据范围，从不访问，到已知敏感数据源，再到任意敏感数据。

更高的档位让更复杂的任务成为可能，同时扩大被攻破时的触达范围：让任务可行的灵活性，也决定了被攻陷的智能体能触达多少数据。


<a id="term-risk-taxonomy"></a>

**风险分类** — *Risk Taxonomy*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

按组件组织的智能体安全风险目录，从 R1 到 R7，设计维度映射到它之上。

R1 异构的不可信接口、R2 错误遵循指令、R3 不受约束/不安全的数据流与 R4 幻觉与模型错误属于模型侧风险；R5 隐私数据泄露、R6 非预期/未授权动作与数据损坏、R7 资源耗尽与拒绝服务属于后果类风险。


<a id="term-risk-amplification"></a>

**风险放大** — *Risk Amplification*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

攻击面扩大助推模型风险，模型风险再放大后果类风险的级联过程。

R1 使恶意输入触达 R2–R4，再放大 R5–R7；因此必须在系统层面纵深防御。


<a id="term-server-side-request-forgery"></a>

**服务端请求伪造** — *Server-Side Request Forgery*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

领域特定漏洞 SSRF，智能体可被操纵利用它触达受保护的内部资源。

与 XSS、路径穿越、SQL 注入并列，是私有数据泄露（R5）的滥用模式之一。


<a id="gloss-g"></a>

## G

<a id="term-payload-format"></a>

**payload 格式** — *Payload Format*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

Dashlane 事务开头标明其密钥派生函数、密码算法与工作模式；KWC3 为旧格式，Flexible 为当前格式。


<a id="term-public-key-authentication-pka"></a>

**公钥认证** — *Public-Key Authentication (PKA)*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

把公钥与其所有者绑定，可通过证书、首次使用信任或已验证密钥目录实现。


<a id="term-sharing-key-overwrite"></a>

**共享密钥覆写** — *Sharing Key Overwrite*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

攻击 LP07 与 DL02：恶意服务器在共享时替换接收方公钥，使共享密钥被加密到它掌握的密钥之下。


<a id="term-shared-folder-key"></a>

**共享文件夹密钥** — *shared folder key*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

加密 LastPass 共享文件夹中各条目的 32 字节密钥 k_shr，对每个接收者用 RSA-OAEP 包裹。


<a id="term-tool-poisoning"></a>

**工具投毒** — *Tool poisoning*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

第三方工具的名称、描述或实现中夹带恶意提示词或代码，随工具定义被加载。

SoK 中的向量 V3。两个代表性结果：Les Dissonances 劫持工具执行顺序，发现 66 个真实工具中 75% 可被利用；ToolHijacker 优化工具文档以强制选中，可绕过 StruQ、SecAlign、已知答案检测、DataSentinel 与困惑度检测。


<a id="term-attack-vector"></a>

**攻击向量** — *Attack Vector*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

攻击者进入并影响智能体系统的具体途径，如间接提示注入或工具投毒。


<a id="term-attack-surface"></a>

**攻击面** — *Attack Surface*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

攻击者可以借此触达系统的接口集合；对智能体而言，外部数据、记忆与第三方工具都会扩大它。


<a id="term-fail-safe-defaults"></a>

**故障安全默认** — *Fail-Safe Defaults*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 9 章</span>

论文点名的另一条适用原则：失效时默认拒绝而非放行。


<a id="term-associated-data"></a>

**关联数据** — *associated data*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

与密文一起被认证、但本身不加密的数据，用来把密文绑定到它的上下文。

正因为它缺失，条目字段交换（BW05、LP02）才能成立：字段名作为明文 JSON 键存放，从不与它下面的密文一起认证。


<a id="term-authenticated-encryption-with-associated-data-aead"></a>

**关联数据认证加密** — *Authenticated Encryption with Associated Data (AEAD)*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

认证加密的扩展，还保护留在明文的关联数据（如 PBKDF 参数）。


<a id="term-planner-parser-separation"></a>

**规划器—解析器分离** — *planner–parser separation*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

把智能体对 LLM 的使用拆成工具调用规划与工具结果解析，使外部数据无法左右规划决策。


<a id="term-rule-circuit"></a>

**规则电路** — *rule circuit*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

ShieldAgent 把外部政策文档声明式编码为作用于动作轨迹的电路，用以强制政策合规。


<a id="term-over-tainting"></a>

**过度污点标记** — *over-tainting*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

把超出必要范围的数据标为不可信；基于变量的方法以可追踪变量缓解该问题。


<a id="gloss-h"></a>

## H

<a id="term-heisenberg-attack"></a>

**海森堡攻击** — *Heisenberg Attack*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

讲者对 Bitwarden 的 BW11 与 BW12 的合称：两个方向各以放弃完整性或机密性之一为代价。


<a id="term-horizontal-privilege-separation"></a>

**横向权限分离** — *horizontal privilege separation*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

让并行子智能体在互不相交的访问范围上运行的权限分离，如 IsolateGPT 为每个应用派生一个智能体。


<a id="term-consequence-risks"></a>

**后果类风险** — *Consequence Risks*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

R5、R6、R7，其严重程度由访问敏感度、操作与用户界面决定，而非是否发生。

私有数据泄露、非预期/未授权操作与数据损坏、资源耗尽；操作维度扩展到执行会把信息泄露变成环境破坏。


<a id="term-interoperable-identity"></a>

**可互操作的身份** — *Interoperable Identity*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 9 章</span>

智能体身份在各平台间按共同分类体系签发、委托与撤销的能力，使动作可审计、可问责。

缺少标准框架时，各平台的凭证签发、委托与撤销流程互不兼容，难以审计与联邦。


<a id="term-transient-session-memory"></a>

**会话内临时记忆** — *Transient Session Memory*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

仅在当前会话内留存、会话结束即被丢弃的记忆。


<a id="term-roll-back-attack"></a>

**回滚攻击** — *roll-back attack*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 10 章</span>

重放较早且签名或加密均合法的保险库版本，以撤销改动或恢复已收回的权限。

论文发现 Merkle 树认证能挡住选择性删除，但若无可信第三方持有版本信息或本地密码学状态，完整的回滚无法排除。


<a id="gloss-j"></a>

## J

<a id="term-capability-based-security"></a>

**基于能力的安全** — *capability-based security*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

持有不可伪造的能力令牌即获得访问权的访问控制机制，与 RBAC、ABAC 并列。


<a id="term-economy-of-mechanisms"></a>

**机制经济性** — *Economy of Mechanisms*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 9 章</span>

论文点名的另一条适用原则：以最少机制达成防护，使设计可审计、可维护。


<a id="term-memory-poisoning"></a>

**记忆投毒** — *Memory poisoning*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

直接操纵智能体持久记忆以注入内容、改变行为或泄露数据，写入会跨会话存续。

SoK 中属内部攻击者的向量 V6。AgentPoison 以低于 0.1% 的毒化率取得至少 80% 的后门成功率，PoisonedRAG 污染知识库，MINJA 则仅靠查询交互达到同等效果。


<a id="term-rsa-oaep"></a>

**RSA-OAEP 加密** — *RSA-OAEP*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

带 OAEP 填充的 RSA 加密，在 LastPass 与 Bitwarden 中用接收者公钥包裹对称密钥。


<a id="term-encryption-type-attribute"></a>

**加密类型属性** — *Encryption Type Attribute*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

Bitwarden 密文前不受保护的标记：type 0 表示认证加密，type 1 表示纯 AES-CBC。

该属性前置在密文之前且不受完整性保护，因此恶意服务器可以篡改它，把客户端引向较弱的 AES-CBC 路径。


<a id="term-rag-poisoning"></a>

**检索增强生成投毒** — *RAG poisoning*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

污染检索增强智能体所依赖的知识，使投毒条目被检索并影响后续行为。


<a id="term-retrieval-tool"></a>

**检索工具** — *Retrieval Tool*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

赋予智能体对外部环境只读访问的工具（如搜索或读取文件），区别于会修改环境的工具。


<a id="term-retrieval-capability"></a>

**检索能力** — *Retrieval Capability*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

对外部环境的只读访问，是动作维度中介于回复与执行之间的档位。


<a id="term-monitoring"></a>

**监控** — *monitoring*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

对输入、输出与中间状态提供全局可见性，揭示单个动作看不出的分布式威胁。


<a id="term-indirect-prompt-injection"></a>

**间接提示注入** — *Indirect prompt injection*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

把指令藏在智能体检索到的内容（网页、文档、邮件等）中，诱导模型照做。

SoK 将其归为外部攻击者的向量 V1，由 Greshake 等人奠定、InjecAgent 加以基准化；它假定智能体会读取攻击者可达的内容，对应"输入信任"维度上"任意外部数据"的一端。


<a id="term-downgrade-to-legacy"></a>

**降级到旧格式** — *Downgrade to Legacy*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

攻击 BW12：伪造出没有 MAC 半段的用户密钥，使 Bitwarden 改用纯 CBC 模式，从而打开填充预言。


<a id="term-url-checksum"></a>

**URL 校验和** — *URL checksum*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

把条目 URL 的哈希存进另一个加密字段，供客户端发现 URL 被调换。

Bitwarden 于 2024 年 7 月上线。旧条目不会补上它，且只有条目带条目密钥时才会校验，因此 2024 年 7 月之前的条目与攻击 BW10 都能绕过它。


<a id="term-disable-per-item-keys"></a>

**禁用条目级密钥** — *Disable Per-Item Keys*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

攻击 BW10（详见论文完整版）：降级密钥层级，使条目重新直接用用户密钥加密。


<a id="term-decision-fatigue"></a>

**决策疲劳** — *decision fatigue*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

频繁验证提示导致的判断力下降，使使用者盲目批准高风险动作或误拒良性动作。


<a id="gloss-k"></a>

## K

<a id="term-developer-defined-workflow"></a>

**开发者定义的工作流** — *Developer-Defined Workflow*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

由开发者事先写定的固定动作序列，是工作流维度的中等灵活档位。


<a id="term-trusted-execution-environment"></a>

**可信执行环境** — *trusted execution environment*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

基于硬件的隔离区域，机密计算在其中管理智能体凭证，使其免受外围软件触及。


<a id="term-auditable-key-directory"></a>

**可审计密钥目录** — *auditable key directory*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 10 章</span>

只可追加的账号到公钥映射目录，出具包含性与历史证明供人审计。

它无法阻止恶意服务器给用户配错公钥，但能使篡改可见，论文正是据此评估它对密码管理器的价值。


<a id="term-client-side-encryption"></a>

**客户端加密** — *client-side encryption*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

在用户设备上先行加密，再把密文发送给服务器。


<a id="term-persistent-cross-session-memory"></a>

**跨会话持久记忆** — *Persistent Cross-Session Memory*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

存活期长于单次会话的记忆，是记忆维度的最灵活档位。

持久化既制造出持续影响后续行为的投毒目标，也累积出比产生它的交互活得更久的敏感数据。


<a id="term-extended-master-key"></a>

**扩展主密钥** — *extended master key*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

Bitwarden 中由主密钥的 enc 与 mac 输出拼接成的 64 字节密钥 k_em。

它用于加密随机采样的用户密钥，因此服务器上保存的密文 c_u 只有用主密码才能解开。


<a id="gloss-l"></a>

## L

<a id="term-offline-guessing-attack"></a>

**离线猜测攻击** — *offline guessing attack*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 10 章</span>

仅凭已到手的数据猜测主密码，不接触在线服务，故不受速率限制约束。

Duan 等按对手掌握的信息把它们分为四类，发现 43 款管理器里有 38 款无法抵御至少一类，说明单一主密码设计依赖慢哈希与密码熵。


<a id="term-flexibility-spectrum"></a>

**灵活性连续谱** — *Flexibility Spectrum*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

一个设计维度可取值的范围，用最不灵活、中等灵活、最灵活三个代表性档位表示。


<a id="term-key-rotation"></a>

**密钥轮换** — *key rotation*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

把用户密钥换成新采样的密钥；Bitwarden 在用户修改主密码时可选提供。

轮换迫使客户端重新生成账户恢复密文，而所用的组织公钥来自服务器，这就是攻击 BW02 的入口。


<a id="gloss-m"></a>

## M

<a id="term-mitre-atlas"></a>

**MITRE ATLAS** — *MITRE ATLAS*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

针对 AI 系统的对手战术与技术公开知识库，附录 A 把本文攻击向量映射到它。


<a id="term-ciphertext-integrity"></a>

**密文完整性** — *ciphertext integrity*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

攻击者无法在不被察觉的情况下改动所存或所传密文的性质。


<a id="term-ciphertext-authentication"></a>

**密文认证** — *Ciphertext Authentication*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

证明密文由谁生成；公钥加密本身做不到，因为任何人都能加密。


<a id="term-cryptographic-agility"></a>

**密码敏捷性** — *cryptographic agility*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 9 章</span>

通过剧烈但干净的破坏性变更，避免历史密码学攻击卷土重来的做法。

论文把它与密码管理器中保留 2000 年代初密码学的向后兼容相对照，并以 TLS 的演化为应效仿的样板。


<a id="term-key-separation-ks"></a>

**密钥分离** — *Key Separation (KS)*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

为每个条目、每个字段派生独立密钥，使一个密钥无法冒充另一个。


<a id="term-key-wrapping"></a>

**密钥封装** — *key wrapping*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

用一把密钥加密另一把密钥，使被封装者可安全存储或传输。


<a id="term-key-commitment"></a>

**密钥承诺** — *key commitment*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 10 章</span>

要求一段密文只能在唯一密钥下解密，使他人无法把它解成两条不同消息。

论文本身没有提到密钥承诺，本章查阅的工作也未曾让它在本文场景里发挥作用，因此它属于尚未处理的性质。


<a id="term-key-substitution"></a>

**密钥替换** — *key substitution*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

把受害者的公钥换成攻击者的公钥，使后续通信被加密给攻击者。


<a id="term-key-transparency"></a>

**密钥透明** — *Key Transparency*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

讲者为共享提出的对策：为公钥建立可审计的公开记录，以便发现被替换的公钥。

讲者建议把密钥透明用于共享中的公钥认证，并把 HSM 用于密钥托管、把密钥分离用于部分保险库同步。


<a id="term-model-context-protocol"></a>

**模型上下文协议** — *Model Context Protocol*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 10 章</span>

一套为 AI 应用定义、发现与调用外部工具的开放协议，具备动态 schema 协商与双向通道，使工具可在不同模型与框架间通用。

SoK 指出工具可以经由这类协议实现；标准化同时使发现通道成为攻击面。Hou 等人枚举了包含工具投毒在内的十六种威胁场景，ETDI、MCP Context Protector 与 MCIP 即是相应的加固方案。


<a id="term-model-context-protocol-mcp"></a>

**模型上下文协议** — *Model Context Protocol (MCP)*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

一种标准化协议，工具可经其实现并供智能体调用。


<a id="term-model-poisoning"></a>

**模型投毒** — *Model poisoning*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

由模型供应商或供应链在模型内植入隐藏的恶意行为，使其执行未授权动作或泄露数据。


<a id="term-model-risks"></a>

**模型风险** — *Model Risks*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

论文把 R2、R3、R4 归为一组模型风险，主要由工作流设计维度驱动。

包括错误指令跟随、无约束数据流与幻觉；它们处于级联中段，既承接攻击面扩大，也放大后果类风险。


<a id="term-merkle-tree"></a>

**默克尔树** — *Merkle Tree*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

认证整个保险库的哈希结构，用于阻止选择性删除攻击。


<a id="gloss-n"></a>

## N

<a id="term-memory-separation"></a>

**内存分离** — *memory separation*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

创建彼此独立的内存空间，使低权限组件读不到其他组件持有的敏感数据。


<a id="term-internal-adversary"></a>

**内部对手** — *Internal adversary*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

以开发者或组件供应商身份访问模型、记忆等组件，论文称其为最难实现的攻击。


<a id="gloss-p"></a>

## P

<a id="term-disclosure-window"></a>

**披露窗口** — *disclosure window*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 9 章</span>

双方约定的、期间不对外公开问题的期限，这里是至少 90 天。

披露始于 Bitwarden 2025 年 1 月 27 日、LastPass 2025 年 6 月 4 日、Dashlane 2025 年 8 月 29 日，共同公开日期为 2026 年 2 月 14 日；LastPass 因首封邮件丢失而重置了计时。


<a id="term-credential-provisioning"></a>

**凭证供给** — *credential provisioning*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

智能体取得凭证的方式，即经由单点登录或基于 OAuth 2.0 的认证委托。


<a id="gloss-q"></a>

## Q

<a id="term-forced-migration"></a>

**强制迁移** — *forced migration*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

只负责把保险库迁移到新格式的客户端，使破坏性变更覆盖所有用户。


<a id="term-privilege-separation"></a>

**权限分离** — *privilege separation*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

给不同组件分配不同权限并加以隔离，使控制一个组件的攻击者无法触及其余组件。

在智能体中它缓解错误指令遵循（R2）与不受约束的数据流（R3）。SoK 点出各论文未言明的共同轴：沿"规划器—解析器"的纵向分离，与按应用或范围的横向分离（如 IsolateGPT 的按应用子智能体）。


<a id="gloss-r"></a>

## R

<a id="term-aes-cbc-hmac"></a>

**AES-CBC-HMAC 认证加密** — *AES-CBC-HMAC*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

用 AES-CBC 加密再对密文做 HMAC；Bitwarden 的构造，缺少 MAC 密钥时退化为纯 AES-CBC。


<a id="term-human-in-the-loop-validation"></a>

**人在回路验证** — *human-in-the-loop validation*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

智能体在高风险动作前请求用户批准，由用户掌控安全决策的防护机制。

SoK 认为它相对而言为智能体特有，缓解 R5–R7，并从验证范围、告警内容、复用策略三个维度设计。其局限是决策疲劳，以及告警预设的安全素养与用户实际水平之间的落差。


<a id="term-task-level-identity"></a>

**任务级身份** — *task-level identity*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

为特定任务或会话创建的短生命周期身份，实现动态最小权限而非长期身份。


<a id="term-key-authentication"></a>

**密钥认证** — *key authentication*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

确认服务器下发的公钥确实属于它声称的那一方。

本章的攻击之所以成立，正是因为 Bitwarden 与 LastPass 从不做这件事：两者都无条件信任服务器下发的托管公钥，表 1 记为 "Lack of Key Auth"。


<a id="term-authenticated-encryption"></a>

**认证加密** — *authenticated encryption*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

同时能证明密文未被改动的加密模式，与单纯 AES-CBC 不同。


<a id="term-authenticated-encryption-ae"></a>

**认证加密** — *Authenticated Encryption (AE)*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

同时证明密文未被改动的加密，使篡改会被发现而非静默解密。


<a id="term-log-granularity"></a>

**日志粒度** — *log granularity*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

智能体活动日志的粗细程度：越细越易检出异常，但存储、计算与隐私代价越高。


<a id="term-containerisation"></a>

**容器化** — *containerisation*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

既有的操作系统隔离机制，智能体的权限分离可复用它来沙箱化外部环境。


<a id="term-package-hallucination"></a>

**软件包幻觉** — *Package hallucination*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

代码生成模型凭空编造包名的缺陷，攻击者抢注这些包名以植入恶意软件包。

Spracklen 等人在 576,000 个样本上测得商业模型至少 5.2%、开源模型至少 21.7% 的包名不存在，共 205,474 个唯一名字。SoK 同时把它归入数据注入（V2）与幻觉被利用（R4）。


<a id="gloss-s"></a>

## S

<a id="term-sandboxing"></a>

**沙箱化** — *sandboxing*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

把工具或环境限制在受限的执行副本中，PFI 即按数据信任级别在普通版与沙箱版之间切换工具。


<a id="term-contextual-security"></a>

**上下文安全** — *contextual security*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

智能体特有目标：上下文与用户意图任务保持一致，避免指令覆盖与上下文漂移。


<a id="term-design-anti-pattern"></a>

**设计反模式** — *design anti-pattern*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 9 章</span>

在不同产品中反复出现、导致漏洞的坏设计习惯。

论文点出四类：旧密码学留下的历史包袱、被低估的复杂度、增量同步破坏完整性，以及不安全的公钥共享。


<a id="term-design-flexibility"></a>

**设计灵活性** — *Design Flexibility*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

智能体设计在各维度上偏向最不灵活或最灵活一端的程度；灵活性越大通常越放大安全风险。


<a id="term-design-dimension"></a>

**设计维度** — *Design Dimension*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

刻画智能体设计的七条轴之一，每条轴都是一条从最不灵活到最灵活的连续谱。

七个维度是输入信任、访问敏感度、工作流、动作、记忆、工具与用户界面。它们彼此正交，同一个智能体可以在各维度上处于不同档位，任一维度上更高的灵活性都会放大安全风险。


<a id="term-identity-and-access-management"></a>

**身份与访问管理** — *identity and access management*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

涵盖身份管理、访问控制与凭证管理的总体领域，确保实体通过认证、访问获得授权。


<a id="term-transactional-database"></a>

**事务型数据库** — *transactional database*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

Dashlane 保险库的表示形式，每个事务创建一个、修改一个或删除一个条目。


<a id="term-transaction-key"></a>

**事务密钥** — *transaction key*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

Dashlane 由主密钥与事务参数派生的、用于加密单个事务内容的密钥。

盐对所有事务都是固定的，因此 KDF 与密码模式相同的事务都用同一把派生密钥加密。


<a id="term-transaction-replay"></a>

**事务重放** — *transaction replay*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

复制、重排或删除 Dashlane 事务，而客户端无法察觉。

即攻击 DL01。成因是事务密钥只取决于事务参数而非事务本身；它也是 4.4.2 节 Dashlane 降级攻击的基础。


<a id="term-self-enrolment"></a>

**手动纳入** — *self-enrolment*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

需要用户主动操作的手动账户恢复加入方式。

自动纳入之外的另一种方式；未做此操作的用户本不应受恢复机制影响。


<a id="term-trust-on-first-use-tofu"></a>

**首次使用信任** — *Trust On First Use (TOFU)*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

首次见到公钥时记住它，此后变化即告警，把密钥替换限制在首次使用。


<a id="term-trust-on-first-use"></a>

**首次使用信任** — *Trust-On-First-Use*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 9 章</span>

首次见到公钥时予以接受、日后变化则告警的方案。

它与 PKI、验证密钥目录同属论文为公钥替换类攻击提出的缓解措施，因为某种形式的公钥验证无法回避。


<a id="term-data-corruption"></a>

**数据损坏** — *Data Corruption*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

对文件、数据库等存储资源的未授权修改，R6 下的两类完整性问题之一。

R6 同时涵盖非预期/未授权操作，例如未授权购买或任意代码执行；记忆投毒会污染后续行为。


<a id="term-data-origin-authentication"></a>

**数据来源认证** — *Data-Origin Authentication*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

保证消息确实来自具名发送者；任何公钥加密方案本身都无法提供。

由于任何一方都能用公钥加密，任何 PKE 方案都无法提供该保证；论文建议用签密把密文与发送者绑定。


<a id="term-input-trust"></a>

**输入信任** — *Input Trust*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

智能体所依赖的外部数据源的可信程度，从不使用外部数据到任意的、可能不可信的来源。

可信度最高的档位不使用外部数据，最灵活的档位接受任意外部数据。只有当智能体开始消费外部内容，间接提示注入才在该维度上成为可能。


<a id="term-input-guardrail"></a>

**输入护栏** — *input guardrail*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

在输入到达智能体之前校验、过滤恶意指令与数据的第一道防线。


<a id="term-output-guardrail"></a>

**输出护栏** — *output guardrail*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

检查智能体对外行为（回复、工具调用）的机制，校验任务对齐与工具使用安全。


<a id="term-private-data-leakage"></a>

**私有数据泄露** — *Private Data Leakage*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

借助组件交互未授权获取用户对话、持久记忆、工具凭据或环境资源。

编号 R5，保密性失效，也是 R3 最直接促成的风险；模式包括自动 URL 访问与 SSRF 等漏洞滥用。


<a id="gloss-t"></a>

## T

<a id="term-prompt-injection"></a>

**提示注入** — *Prompt Injection*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

攻击者构造内容，使智能体执行恶意指令而非用户或开发者本意的攻击。

直接注入来自用户自身输入；间接注入则经由智能体检索到的外部数据（如网页或文档）进入。


<a id="term-prompt-stealing-attack"></a>

**提示窃取攻击** — *Prompt Stealing Attack*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

从已部署的模型或智能体中提取编码专有知识的系统提示、工具描述或配置。

在智能体系统中，受害方是开发者与工具提供方；已有工作覆盖文生图模型与现实提示词服务。


<a id="term-item-field-swapping"></a>

**条目字段交换** — *item field swapping*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

把密文从条目的一个字段搬到另一个字段或搬到别的条目，因为没有东西把它绑定到字段。

即攻击 BW05 与 LP02，也是图标 URL 解密攻击的基础：后者需要把敏感字段的密文搬进 URL 字段。


<a id="term-item-injection"></a>

**条目注入** — *Item Injection*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

攻击 DL03：利用 Dashlane 的加密预言 DLb2 伪造任意事务，包括 Setting 事务。


<a id="term-item-level-vault-encryption"></a>

**条目级保险库加密** — *item-level vault encryption*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

把保险库中的每个条目分别存储、分别加密，而不是整体加密。

它让局部同步变得廉价（改一个条目不必重新加密整个保险库），代价是保险库整体不再有任何密码学保证。


<a id="term-icon-url-item-decryption"></a>

**图标 URL 条目解密** — *icon URL item decryption*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

把字段密文放进客户端取图标用的 URL 字段，从而把解密后的内容泄漏出去。

即攻击 BW06（Bitwarden，只发送域名与顶级域，要求明文形如 URL）与 LP03（LastPass，直接发送存储的 URL，对明文没有条件）。


<a id="term-organisation-key"></a>

**团队密钥** — *organisation key*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

加密 Bitwarden 团队条目的 64 字节对称密钥 k_org；能否取得它即决定成员资格。


<a id="gloss-w"></a>

## W

<a id="term-external-adversary"></a>

**外部对手** — *External adversary*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

对智能体系统无访问权限，仅通过控制智能体可能检索的网页等资源施加影响。


<a id="term-complete-mediation"></a>

**完全中介** — *complete mediation*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

设计原则：对敏感资源的每次访问都须经检查与验证，由监控与访问控制落实。

体现在监控智能体执行过程的机制，以及校验每次受保护资源交互的访问控制中。


<a id="term-threat-model"></a>

**威胁模型** — *Threat Model*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

对攻击者身份及其可触及范围的分类，用于按对手能力归并攻击向量。

本工作使用三类：外部对手、用户级对手与内部对手。


<a id="term-unconstrained-data-flow"></a>

**无约束数据流** — *Unconstrained Data Flow*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

大模型缺少类型系统与访问控制，数据可从不可信输入自由流向任意输出。

编号 R3，损害保密性与完整性，后果是 R5、R6、R7；典型例子是被自动访问的攻击者控制 URL。


<a id="term-taint-tracking"></a>

**污点追踪** — *taint tracking*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

标记不可信数据并追踪其传播，从而约束受不可信来源影响的数据。

SoK 的"信息流控制与污点追踪"类别同时涵盖二者。智能体中的机制分符号变量、多次执行与模型判定三类，设计轴在于目标是完整性（阻止不可信输入左右工具调用）还是机密性（不让秘密流向不可信终点）。


<a id="gloss-x"></a>

## X

<a id="term-pushdown-automaton"></a>

**下推自动机** — *pushdown automaton*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

Formal-LLM 用以编码工具调用顺序等规划约束、限制规划生成的机器模型。


<a id="term-utility-loss"></a>

**效用损失** — *utility loss*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

权限分离把功能拆到必须相互通信的隔离组件之后，智能体所损失的能力。

论文把"在保住安全保证的同时降低可用性损失"列为实际部署的开放挑战。


<a id="term-coordinated-credential-orchestration"></a>

**协同凭证编排** — *Coordinated Credential Orchestration*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 9 章</span>

在整个智能体栈（含多智能体）中标准化、统一地管理密钥的需求，取代把密钥存为未加密环境变量的临时做法。


<a id="term-coordinated-vulnerability-disclosure"></a>

**协同漏洞披露** — *coordinated vulnerability disclosure*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

先私下向厂商报告漏洞，商定发表日期后再公开的做法。

论文对每家厂商给出至少 90 天窗口，并统一把公开日期定为 2026 年 2 月 14 日。


<a id="term-information-flow-control"></a>

**信息流控制** — *information flow control*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

为数据分配信息流格中的安全标签并传播，阻断违反格约束的流动。

在智能体中它针对不受约束的数据流（R3）及其下游的泄露（R5）与篡改（R6）。PFI、CaMeL、FIDES 把工具结果替换为可追踪变量；CaMeL 在 AgentDojo 上以可证明安全性完成 77% 的任务，未防护为 84%。SoK 指出的缺口是运行时开销与标签蔓延。


<a id="term-information-flow-lattice"></a>

**信息流格** — *information flow lattice*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

预定义的安全标签偏序结构，信息流控制据此分配标签并判定允许的传播。


<a id="term-formal-verification"></a>

**形式化验证** — *formal verification*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

依据系统的形式模型证明某项性质；用于智能体时模型须刻画随机行为才有意义。


<a id="gloss-y"></a>

## Y

<a id="term-verified-key-directory"></a>

**验证密钥目录** — *Verified Key Directory*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 9 章</span>

让服务商错误关联公钥的行为对用户可见的目录机制。

它在安全通信领域被探索：虽不能阻止恶意服务器把错误公钥绑到用户，但能在服务商作恶时提醒用户。


<a id="term-known-plaintext-oracle-gadget"></a>

**已知明文预言器** — *Known Plaintext Oracle Gadget*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

攻击 BWb1：借 Bitwarden 生成密钥对的迁移路径，在未知主密钥下取得已知明文的 AES-CBC 密文。


<a id="term-verified-key-directory-vkd"></a>

**已验证密钥目录** — *Verified Key Directory (VKD)*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

一种目录，虽不能阻止服务器发布错误公钥，却能让篡改对用户可见。


<a id="term-heterogeneous-untrusted-interfaces"></a>

**异构不可信接口** — *Heterogeneous Untrusted Interfaces*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

智能体暴露的外部数据源、持久记忆与信任级别各异的第三方工具等攻击入口。

编号 R1。六个攻击向量 V1–V6 都经这些接口之一进入系统，因此 R1 更像其他风险的前提。


<a id="term-hardware-security-module-hsm"></a>

**硬件安全模块** — *Hardware Security Module (HSM)*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

防篡改硬件，可保管恢复密钥，并对服务器是否诚实运行提供一定保证。


<a id="term-hardware-security-module"></a>

**硬件安全模块** — *hardware security module*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 9 章</span>

专门硬件，用于保管密钥并执行服务运营方无法篡改的操作。

论文建议把部分密钥托管放到 HSM 上，如同 Signal、WhatsApp 与 Apple 高级数据保护在恢复与备份中所做，使服务器对自身诚实提供一定保障。


<a id="term-user-key"></a>

**用户密钥** — *user key*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

保护 Bitwarden 或 LastPass 保险库中所有条目的 64 字节对称密钥，在服务器上仅以密文存在。


<a id="term-user-key-overwriting"></a>

**用户密钥覆写** — *User Key Overwriting*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

攻击 BW11：伪造出加密半段为己所知的用户密钥密文，使此后新加密的条目失去机密性。


<a id="term-user-level-adversary"></a>

**用户级对手** — *User-level adversary*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

以恶意用户身份直接接触智能体，或作为第三方污染正常用户的输入。


<a id="term-runtime-protection"></a>

**运行时防护** — *Runtime Protection*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

在智能体执行过程中实施安全约束、实时检测威胁与行为的防护机制。

包含输入护栏、输出护栏、信息流控制与污点追踪、监控以及人在回路验证五类。


<a id="gloss-z"></a>

## Z

<a id="term-payload-string"></a>

**载荷字符串** — *payload string*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

Dashlane 事务内容开头的若干字节，规定 KDF 及其参数、分组密码与工作模式。


<a id="term-account-recovery"></a>

**账户恢复** — *account recovery*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

让用户（或管理员）在忘记主密码后重新取回访问权的功能。

恢复功能是安全与可用性相冲突之处，也正是密钥托管类攻击所利用的功能。


<a id="term-account-recovery-ciphertext"></a>

**账户恢复密文** — *account recovery ciphertext*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

用户加入恢复时客户端发出的密文 c_rec，即用组织公钥加密的用户密钥。

它存放在服务器上，以便管理员在用户忘记主密码后交还保险库；4.1 节的两个 Bitwarden 攻击都是让客户端把它用攻击者控制的公钥加密后发出。


<a id="term-account-recovery-policy"></a>

**账户恢复策略** — *account recovery policy*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

组织侧设置，决定成员是否加入恢复、以及加入组织时是否自动纳入。

客户端从不带完整性保护的服务器取回该策略，恶意服务器因此能为从未选择加入的用户打开自动纳入。


<a id="term-shadowing-attack"></a>

**遮蔽攻击** — *shadowing attack*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

恶意工具结果覆盖其他工具结果的攻击，指令层级微调无法应对。


<a id="term-orthogonal-dimensions"></a>

**正交维度** — *Orthogonal Dimensions*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

各设计维度可共存于同一个智能体、且可在不同维度上处于不同档位的性质。

正交意味着同一智能体可以在全部七个维度上同时处于最灵活档位；它并不意味着各维度在效果上互不相干，因为工具维度直接使能动作维度。


<a id="term-certificate-authority-ca"></a>

**证书颁发机构** — *Certificate Authority (CA)*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 8 章</span>

为公钥签名的机构；在密码管理器场景中必须不隶属于保险库服务器的控制方。


<a id="term-ai-agent"></a>

**AI 智能体** — *AI Agent*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

把传统软件组件与神经组件组合起来，接收任务并为用户采取一系列动作的混合软件系统。


<a id="term-execution-action"></a>

**执行动作** — *Execution Action*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

会修改环境而非只读取环境的操作，是动作维度的最灵活档位。

执行是智能体的错误不再局限于文本的地方：也正是在这里，信息泄露变成对环境的破坏。


<a id="term-agentic-ai-system"></a>

**智能体 AI 系统** — *Agentic AI System*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

把大语言模型与传统软件组件组合在一起、可自主行动并调用工具的系统。

与"AI 智能体"互换使用；分析的单元是整个系统，而非单独的模型。


<a id="term-agent-design-dimensions"></a>

**智能体设计维度** — *Agent Design Dimensions*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

刻画智能体设计及其灵活性的七个维度：输入信任、访问敏感性、工作流、动作、记忆、工具、用户界面。

各维度彼此正交，同一智能体可在不同维度上处于不同层级。


<a id="term-direct-prompt-injection"></a>

**直接提示注入** — *Direct prompt injection*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

用户或界面直接发给智能体的恶意提示词，指示它违背系统提示词行事。


<a id="term-master-password-protected-password-management-protocol"></a>

**主密码保护的密码管理协议** — *master-password-protected password management protocol*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 10 章</span>

密码管理器客户端与服务器之间的交互，用户靠单一主密码完成认证并解开保险库。

Duan、Wang 与 Fu 还原出 43 款管理器的实际协议，并在通用可组合框架下把它们形式化为理想功能。


<a id="term-injection-attack"></a>

**注入攻击** — *injection attack*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 10 章</span>

对手只控制自己的客户端，向受害者客户端注入选定负载，再观察受保护状态的攻击。

Fábrega 等借共享注入负载，并观察加密保险库导出或服务器流量，从而反推密码、URL、用户名与附件。这里恶意方是客户端而非服务器。


<a id="term-per-item-key"></a>

**逐条目密钥** — *per-item key*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 3 章</span>

为单个保险库条目采样、本身又由用户密钥加密的密钥，Bitwarden 自 2024.2.0 起用于新条目。

Bitwarden v.2024.2.0 引入，记作 k_u^i。旧条目不会被迁移，因此同一保险库中可能同时存在直接用用户密钥加密的条目和使用条目密钥的条目。


<a id="term-auto-enrolment"></a>

**自动纳入** — *auto-enrolment*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

用户加入组织时无需任何交互即自动加入账户恢复。

与需要手动操作的 self-enrolment 相对。攻击 BW01 就是在服务器侧把这个开关打开。


<a id="term-self-hosting"></a>

**自托管** — *self-hosting*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

把产品的服务端组件部署在自己的基础设施上，而非依赖厂商。

部分密码管理器允许组织自行托管存储部分；在论文的威胁模型下，恶意服务器此时就是客户自己的服务器。


<a id="term-resource-drain"></a>

**资源耗尽** — *Resource Drain*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 5 章</span>

昂贵 API 调用、被迫的无限循环或过度内存占用，使智能体及外部系统不可用或难以为继。

编号 R7，可用性风险，衡量方式偏经济而非仅偏运行。


<a id="term-vertical-privilege-separation"></a>

**纵向权限分离** — *vertical privilege separation*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 7 章</span>

分层式的权限分离，可信规划器位于低权限解析器之上，工具结果不会直接流入规划。


<a id="term-defense-in-depth"></a>

**纵深防御** — *Defense in Depth*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 2 章</span>

叠加多层相互独立的防护，使任一防护失效都不至于让攻击得逞的原则。

由输入与输出护栏、信息流控制、监控、访问控制、权限分离、组件加固与人在回路验证共同实现。


<a id="term-component-hardening"></a>

**组件加固** — *Component Hardening*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 1 章</span>

加固智能体的单个组件（如模型、记忆或工具），以抵御针对它的攻击。


<a id="term-organisation-rsa-keypair"></a>

**组织 RSA 密钥对** — *Organisation RSA Keypair*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

Bitwarden 随组织创建的恢复密钥对，其私钥用 k_org 加密成 c_skOrg。


<a id="term-organisation-public-key"></a>

**组织公钥** — *organisation public key*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

Bitwarden 成员加入账户恢复时，客户端用来加密用户密钥的公钥 pk_org。

客户端从服务器取得它且不作认证，恶意服务器因此可以替换成自己的公钥并解出恢复密文。


<a id="term-organisation-symmetric-key"></a>

**组织对称密钥** — *Organisation Symmetric Key*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

Bitwarden 加密组织内共享条目所用的 64 字节密钥 k_org，以各成员的 RSA 公钥加密后保存。

客户端能否取得 k_org 正是它判断成员身份的依据；保险库与服务器下发的组织列表之间没有任何密码学绑定。


<a id="term-organisation-injection"></a>

**组织注入** — *Organisation Injection*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

攻击 BW08：任何人只要把组织密钥加密到某用户公钥之下，就能把该用户加入组织。


<a id="term-organisation-private-key"></a>

**组织私钥** — *organisation private key*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 4 章</span>

Bitwarden 组织密钥对中的私钥 sk_org，该组织每位成员都持有。

由于每位成员都持有它，攻陷一个用户即可获知该用户所属全部组织的 sk_org，BW01 正是借此以蠕虫式扩散。


<a id="term-organisation-overwrite"></a>

**组织覆写** — *Organisation Overwrite*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 6 章</span>

攻击 BW09：服务器把新建组织的加密组织密钥与数据替换成自己控制的值。


<a id="term-principle-of-least-privilege"></a>

**最小权限原则** — *Principle of Least Privilege*  <span class='bd-gloss-alpha'>首见: SoK: Agentic AI · 第 9 章</span>

智能体只应持有任务所需的最小权限与访问权，使被攻陷的影响不超出该任务。

通过隔离智能体组件、限制工具访问的权限分离技术实现。

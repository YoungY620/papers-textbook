# 相关工作与基线

基于云的密码管理器已被研究了十多年。本章按主题重建这篇论文所处的学术脉络：每项前人工作确立了什么、假设了哪种对手，以及一旦把服务器当作完全恶意，结论会怎样改变。同时涵盖论文所依托的端到端加密（E2EE）云存储这条线、它推荐的密码学构件，以及会议报告里提出的第四个厂商。

## 早期分析与它们各自的威胁模型

Li、He、Akhawe 与 Song（USENIX Security 2014）分析了五款流行的网页版密码管理器，归纳出四类关键安全问题。在其中四款里，攻击者能拿到用户对任意网站的凭据；成因从逻辑与授权错误，到对 Web 安全模型的误解，再到 CSRF 与 XSS。这里的对手始终是站在浏览器一侧的 Web 攻击者——恶意站点或脚本，或同一服务的其他用户——而不是保险库服务器。Silver、Jana、Boneh、Chen 与 Jackson（USENIX Security 2014）研究了自动填充策略，指出其中若干策略让远端网络攻击者在无需用户任何交互的情况下批量取走密码。

论文把这些与第一波的其他工作并列：Belenko 与 Sklyarov（2012）、Fahl 等（2013）、Stock 与 Johns（2014）、Zhao、Yue 与 Sun（2013），以及 Gasti 与 Rasmussen 关于数据库格式的工作（2012），后者首次严格分析了存储格式，这条线索被本文在提出密码管理器形式化安全目标时延续。但对手始终是网站、网络攻击者或本地攻击者，目标始终是客户端或存储侧的弱点。没有人考虑恶意服务器。

## 2020 年的再评估

Carr 与 Shahandashti（IFIP SEC 2020）用他们能收集到的全部已披露漏洞测试了五款商用管理器，结果有修好的也有遗留的；其功能测试还发现四个新漏洞，其中一个能让恶意安卓应用向五款中的两款冒充合法应用。Oesch 与 Ruoti（USENIX Security 2020）沿生成、存储、自动填充三个阶段评估了十三款浏览器管理器——首次覆盖密码生成——同样报告了改善。论文正是引用这两项研究来说明密码管理器的安全性已有提升。本书不否认这一结论，它只是没有触及恶意服务器模型：两项研究都没测过。

## 注入攻击与离线猜测

Fábrega、Namavari、Agarwal、Nassi 与 Ristenpart（USENIX Security 2024）提出注入攻击：对手只控制自己的应用客户端，通过共享凭据等方式把选定负载注入受害者客户端，并把注入与对受保护状态的观察（加密保险库导出，或应用服务器收到的流量）交错进行，从而反推出密码、URL、用户名与附件，覆盖十个管理器应用。这里的恶意方是客户端，服务器或网络只是被动观察者。Duan、Wang 与 Fu（IEEE S&P 2025）首次对“主密码保护的密码管理协议”做了系统形式化分析：用文档分析、流量分析与逆向工程还原出 43 款管理器的实际协议，在通用可组合框架下把安全性质写成理想功能，并按对手掌握的信息把主密码离线猜测分为四类；43 款里有 38 款无法抵御至少一类，被腐化的服务器可用预言机攻击拿到开源管理器 Passbolt 的加密密钥，而 1Password 的双密钥设计能够抵御。

一篇并行预印本（Avoine、Carpent 与 Leblanc-Albarel，ePrint 2025/1278）研究服务器保持隐蔽的密码管理器：它给出这类产品应当满足的性质，论证主流方案都不满足，并按管理器类型同时勾勒攻击与一种在隐蔽对手下仍可多设备同步的设计。论文对它的描述值得原样保留：该预印本把云密码管理器分为三类，按类勾勒攻击，攻击破坏保险库完整性以及若干厂商目前并不在意的更弱性质，但未充分探讨影响，没有概念验证代码，且部分攻击依赖弱主密码或过低的 PBKDF 迭代次数。两项工作共享同一个洞察——供应商被不加论证地默认可信；区别在于本文给出了可利用性证明。

## 本文的不同之处

这里服务器会任意偏离预期行为，客户端诚实，且每个攻击都针对真实客户端实现：Bitwarden 12 个（`BW01`–`BW12`）、LastPass 7 个（`LP01`–`LP07`）、Dashlane 6 个（`DL01`–`DL06`）。攻击不按生成、自动填充、注入或猜测组织，而按制造攻击面的四类功能组织：用于账号找回与 SSO 登录的密钥托管、条目级加密下的保险库完整性、凭据共享，以及向后兼容。于是服务器单方面——不需要恶意客户端、弱主密码或用户交互——就能恢复密码，最坏情况下接管整个组织的全部保险库。

## 端到端加密云存储这条线

E2EE 云存储是最近似的既有领域，论文主张“零知识加密”这个说法在两类产品里应当同义。

Albrecht、Backendal、Coppola 与 Paterson（IEEE EuroS&P 2024）首次详细记录并分析了 Nextcloud 的 E2EE 功能，在恶意服务器模型下给出三个攻击，各自破坏某用户全部文件的机密性与完整性，且都有概念验证版本；第三个已被修复，第一个通过临时下架 E2EE 的文件共享功能、等待重新设计来处置。其中一个攻击建立在论文同样点名的误解上：以为公钥加密自带数据来源认证。Backendal、Haller 与 Paterson（IEEE S&P 2023）给出恶意 MEGA 服务商可发动的五个攻击，包括在主密钥下的 AES-ECB 解密预言机；Albrecht、Haller、Mareková 与 Paterson（EUROCRYPT 2023）随后证明 MEGA 为此补上的合法性检查本身也可被利用。Hofmann 与 Truong（ACM CCS 2024）分析了五家服务商——Sync、pCloud、Icedrive、Seafile 与 Tresorit——在其中四家发现严重漏洞，包括注入看起来像用户自己上传的文件。

这条线的奠基工作是 Backendal、Davis、Günther、Haller 与 Paterson（CRYPTO 2024）：给出 E2EE 云存储的形式化语法、面向完全恶意服务器的机密性与完整性博弈定义（含选择性与适应性两版），以及一个可证明安全的构造，MEGA 的攻击正好构成对这些定义的违反。论文提议把这套模型移植到密码管理器，本书沿用的术语也来自它：保险库完整性正对应这些工作为文件定义的完整性。Albrecht 与 Paterson 的回顾文章补上了共同的教训——市面上宣传的“零知识”需要的是密码学审查，而不是代码审计。

## 密码学构件及其文献

公钥认证。许多攻击的本质是用对手控制的公钥做替换，这自公钥密码诞生起就被知晓。某种形式的 PKI 或首次使用即信任无法回避；论文指向即时通信里的已验证密钥目录，而 Lawlor 与 Lewi 对 WhatsApp 密钥透明度部署的介绍，描述了一个只可追加、可审计的密钥目录，带包含性证明与历史证明，其学术脉络经由 CONIKS、SEEMless 与 Parakeet。这样的目录并不能阻止服务器给用户配错公钥，但能让篡改变得可见。

密文认证。任何公钥加密方案都不提供数据来源认证，因为任何人都能加密。论文因此推荐签名加密，由 Zheng（CRYPTO 1997）提出，用于以低于“签名加加密”的代价把密文与发送方绑定；当客户端既是发送方又是接收方时（如 Bitwarden 的组织数据），对称认证加密更省。

认证保险库结构。Merkle 树技术能认证保险库结构、挡住选择性删除攻击，但若没有持有版本信息的可信第三方或本地密码学状态，完整的回滚无法排除——而要求本地状态很麻烦，因为用户希望只凭主密码、在无状态客户端上就能访问保险库。

硬件托底的密钥托管。Signal 的 Secure Value Recovery（Connell 等，OSDI 2024）使用多个 enclave 与云厂商，使任何单一一方都无法恢复用户秘密，并在 enclave 内存内无条件限制 PIN 猜测次数、带回滚保护。WhatsApp 备份协议由 Davies 等（CRYPTO 2023）做了形式化分析；正如那篇形式化 E2EE 论文所指出的，该分析假设服务器上有可信硬件安全模块，而非完全恶意服务器，这正是它只能算部分答案的原因。Apple 的“高级数据保护”同样使用“认证后可用”的硬件模块，可以从中删除 iCloud 服务密钥，使 Apple 无法触及相应数据。

密码敏捷性。论文把向后兼容攻击读作没有遵循 TLS 的既有做法：引入干脆但干净的破坏性变更。它为此引用的文献是 TLS 攻击这条线，直至 Adrian 等（ACM CCS 2015）的弱 Diffie-Hellman 测量与 Logjam 降级攻击——后者对导出级 Diffie-Hellman 的降级，正是本文对 Bitwarden 与 Dashlane 所做降级的原型。

## 第四个厂商：1Password

会议报告把工作描述为覆盖四个厂商，在论文的三家之外加上 1Password；1Password 发布的回应属于厂商说法，不是本工作的发现。它称已审阅论文，确认没有在其《安全设计白皮书》已记录的结构性限制之外引入新的攻击向量，也没有绕过 Secret Key 与安全远程密码（SRP）的保护。对于公钥认证与保险库密钥替换，它承认问题存在，但把两者视为同一项架构考量——由服务器中介、缺少强来源保证的密钥分发——并引用其白皮书附录 C：目前没有可靠办法让用户验证自己加密所用的公钥确实属于目标接收者，因此恶意服务器可能给出不诚实的公钥。

## 前人工作未覆盖的地方

没有前人工作在恶意服务器模型下、带着已实现的利用代码，分析过真实部署的密码管理器：注入与猜测这条线让服务器保持被动或诚实，2020 年的再评估考察的是面向客户端的生命周期，而 E2EE 云存储的形式化结论尚未在密码管理器上落地。由此留下三处空白。恶意服务器下密码管理器的安全目标尚无形式化定义，因此论文的缓解措施是论证的而非证明的，论文本身也提示可能还有未缓解的攻击。保险库回滚的彻底防止仍未解决。密钥承诺则完全没有被讨论——论文和上述工作都没有让它在本文场景里发挥作用。

## 已查阅的文献

以下为本章实际下载并阅读的工作。

- Li 等，《The Emperor's New Password Manager》（USENIX Security 2014）—— <https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-li-zhiwei.pdf>
- Silver 等，《Password Managers: Attacks and Defenses》（USENIX Security 2014）—— <https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-silver.pdf>
- Adrian 等，《Imperfect Forward Secrecy》（ACM CCS 2015）—— <https://weakdh.org/imperfect-forward-secrecy.pdf>
- Carr、Shahandashti，《Revisiting Security Vulnerabilities in Commercial Password Managers》（IFIP SEC 2020）—— <https://arxiv.org/pdf/2003.01985>
- Oesch、Ruoti，《That Was Then, This Is Now》（USENIX Security 2020）—— <https://www.usenix.org/system/files/sec20-oesch_0.pdf>
- Backendal、Haller、Paterson，《MEGA: Malleable Encryption Goes Awry》（IEEE S&P 2023）—— <https://mega-awry.io/pdf/mega-malleable-encryption-goes-awry.pdf>
- Albrecht 等，《Caveat Implementor!》（EUROCRYPT 2023）—— <https://mega-caveat.github.io/pdf/mega-key-recovery.pdf>
- Albrecht 等，《Share with Care》（IEEE EuroS&P 2024）—— <https://ethz.ch/content/dam/ethz/special-interest/infk/inst-infsec/appliedcrypto/education/theses/nextcloud.pdf>
- Backendal 等，《End-to-End Encrypted Cloud Storage》（IEEE S&P Magazine 2024）—— <https://static.cryptanalysis.fun/papers/e2ee-cloud-storage.pdf>
- Backendal 等，《A Formal Treatment of E2EE Cloud Storage》（CRYPTO 2024 全文版）—— <https://www.research-collection.ethz.ch/server/api/core/bitstreams/433c6e41-ef2c-442a-b36d-7acb01d6b384/content>
- Connell 等，《Secret Key Recovery in a Global-Scale E2EE System》（OSDI 2024）—— <https://www.usenix.org/system/files/osdi24-connell.pdf>
- Fábrega 等，《Exploiting Leakage in Password Managers via Injection Attacks》（USENIX Security 2024）—— <https://www.usenix.org/system/files/usenixsecurity24-fabrega.pdf>
- Hofmann、Truong，《E2EE Cloud Storage in the Wild: A Broken Ecosystem》（ACM CCS 2024）—— <https://brokencloudstorage.info/paper.pdf>
- Duan、Wang、Fu，《Security Analysis of Master-Password-Protected Password Management Protocols》（IEEE S&P 2025）—— <https://cssnku.github.io/uploads/publications/ieeesp25-pm-full.pdf>
- 1Password，《ETH Zurich zero-knowledge malicious-server review》（厂商回应）—— <https://1password.com/blog/eth-zurich-zero-knowledge-malicious-server-review>
- Lawlor、Lewi，《Deploying key transparency at WhatsApp》—— <https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/>
- Apple，《Advanced Data Protection for iCloud》—— <https://support.apple.com/guide/security/advanced-data-protection-for-icloud-sec973254c5f/web>
- Avoine 等，《In the Vault, But Not Safe》（ePrint 2025/1278）—— 摘要页读于 <https://eprint.iacr.org/2025/1278>；PDF 位于机器人防护之后，未能下载。

未能获取：Davies 等《Security Analysis of the WhatsApp E2EE Backup Protocol》（CRYPTO 2023）仅在密码学 ePrint 档案馆开放，其 PDF 端点无法访问，因此只能读到摘要与那篇形式化 E2EE 论文对其信任假设的描述。Gasti 与 Rasmussen（ESORICS 2012）以及 Zheng 的《Digital signcryption》（CRYPTO 1997）为付费论文且未找到作者副本。

## 本章要点

- 早期分析（Li 等 2014、Silver 等 2014 及第一波其他工作）假设的是 Web、网络或本地攻击者，无人考虑恶意服务器。
- 2020 年的再评估（Carr 与 Shahandashti：五款管理器、四个新漏洞；Oesch 与 Ruoti：十三款管理器）只在客户端模型下得出安全性改善的结论。
- Fábrega 等（2024）假设恶意客户端配合被动服务器或网络攻击者；Duan 等（2025）形式化 43 款管理器的协议，发现 38 款无法抵御至少一类离线猜测。
- 并行的隐蔽服务商预印本（ePrint 2025/1278）假设服务器保持隐蔽，按类型勾勒攻击，且没有概念验证代码。
- 本文的区别在于完全恶意、任意偏离的服务器，针对真实部署客户端的已实现利用，以及四类功能：密钥托管、条目级加密下的保险库完整性、共享与向后兼容。
- E2EE 云存储这条线提供了完整性词汇：Nextcloud、MEGA 与五家服务商的恶意服务器破解，以及 Backendal 等（CRYPTO 2024）被本文提议移植的形式化定义。
- 论文推荐的构件各有前人文献：签名加密（Zheng 1997）、已验证密钥目录（WhatsApp 的可审计密钥目录，经 CONIKS、SEEMless、Parakeet）、Merkle 树保险库认证、硬件托底的密钥托管（Signal 的 Secure Value Recovery、Apple 的高级数据保护）与 TLS 式密码敏捷性。
- 会议报告加入第四个厂商 1Password，其回应承认密钥验证限制已被文档化，同时声明没有新攻击向量；这是厂商说法，不是发现。

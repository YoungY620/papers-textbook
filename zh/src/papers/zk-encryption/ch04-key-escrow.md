# 攻击一 — 密钥托管

端到端加密（E2EE）密码管理器把保险库密文留在服务器之外并不难，难的是围绕它的整套附加功能：它们都需要客户端与服务器之间运行真正的协议。攻击按成因分为四类，密钥托管排在第一。

## 四类攻击

**密钥托管。** 在 E2EE 管理器里忘记主密码是致命的：服务器只有密文，用户就此永久失去保险库。因此多数管理器用密钥托管提供账户恢复，由管理员持一对密钥交还用户的保险库内容；这类机制一旦被攻破，拿到的通常是整个保险库。4.1 节描述的正是 Bitwarden 与 LastPass 因托管设计缺陷导致的机密性破坏，并指出 Dashlane 的一处弱点。它必须守住的性质是：为部分用户提供恢复，不得削弱从未选择加入的用户。

**条目级保险库加密。** 条目和敏感设置被分别加密，且常带未加密或未认证的元数据，因为每做一点小改动就重加密整个保险库，开销太大。这与保险库完整性存在张力：条目能被调换、删除、重排，KDF 迭代次数之类的设置也能被改动而不被察觉。4.2 节在三款产品上找到了这类攻击，其中许多还会进一步破坏机密性。

**共享。** 面向家庭和企业的共享功能让多人访问共同凭据，使用广泛。4.3 节攻击三款产品的共享功能，既影响完整性也影响机密性；共享也是通往托管攻击的入口——Bitwarden 正是通过组织才触达用户密钥。

**向后兼容。** 三款管理器都演进了密码学方案，同时保留对旧客户端的兼容。这些遗留代码路径让恶意服务器能把客户端拖入更弱状态，即使用户运行最新版本，例如降级为不认证的加密；4.4 节据此在 Bitwarden 和 Dashlane 上构造了降级攻击。

攻击者始终是完整控制服务器的实体；除特别说明外，每个攻击都适用于论文完整版表 2 中该产品的所有客户端。概念验证测试只覆盖 Bitwarden 的 Web 客户端与 LastPass、Dashlane 的浏览器扩展。

会议报告同样从密钥恢复讲起：记不住的主密码，正是恢复机制存在的日常场景。

### 分析方法

分析沿用“Cryptography in the Wild”方法论中的“attack”分支。流程从阅读白皮书与客户端代码开始，最先聚焦 Bitwarden，因其源码公开，最容易建立对架构、协议与功能的认知。分析自始就在恶意或被攻陷服务器的前提下进行，并按各系统功能细化成对抗模型。对每个关注功能，先写出主要密码学动作的伪代码模型，再在其中寻找攻击；随后为每个攻击实现概念验证，必要时实现恶意服务器功能并针对相应客户端实测——只在纸面上成立的攻击不算数。Dashlane 与 LastPass 走同一套流程，含对客户端 JavaScript 与 Android 应用的部分逆向工程。作者指出：缺少形式化分析时，其攻击集合只能视为不完备。

## 表 1：攻击一览

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

表 1：攻击一览，按所利用的功能分为四类。BW、LP、DL 分别表示 Bitwarden、LastPass 和 Dashlane。† 表示影响包含“恢复已加密的密码”；交互列是恶意服务器所需的客户端交互：同步（sync）、登录（login）、打开保险库（open）、加入组织（join）或点击误导性对话框（dialog）。最后一列是第 5 节的缓解措施。

## 4.1 密钥托管

这些攻击都涉及密钥托管功能，即在主密码丢失时恢复账户。成功攻击的后果严重：多数情况下攻击者能恢复整个保险库；有些机制能力较弱，恢复数据留在用户自己的设备上，影响也相应较小。

![Bitwarden（左）、LastPass（中）和 Dashlane（右）的密钥层级。](assets/fig1-key-hierarchies.png)

### 4.1.1 Bitwarden

Bitwarden 支持两种密钥托管。第一种是组织账户恢复：管理员可重置所有已加入恢复的成员的主密码；加入恢复既可以是需要用户交互的手动步骤（self-enrolment），也可在加入组织时自动完成（auto-enrolment）。客户端无论以哪种方式加入，都从服务器取回组织公钥 $pk_{org}$ 加密用户密钥 $k_u$，并把账户恢复密文 $c_{rec}$ 发给服务器；这里有两个密钥恢复攻击。第二种是“Key Connector”，同样存在主密钥恢复攻击（BW03），详见论文完整版。该功能只对付费的“企业”组织开放，但所有客户端都带其代码，攻击与订阅状态无关。

**BW01：恶意自动加入（Malicious Auto-Enrolment）。** 用户加入组织时，客户端会从服务器取回组织数据——名称、密钥材料、策略等——它们没有完整性保护，因此控制服务器的攻击者在用户接受邀请的那一刻就能拿下该用户。接受邀请后，客户端向服务器询问恢复策略和组织公钥；攻击者把 auto-enrolment 置为 true，并把 $pk_{org}$ 换成自己知道私钥 $sk^{adv}_{org}$ 的恶意公钥 $pk^{adv}_{org}$。由于恢复已启用，客户端用 $pk^{adv}_{org}$ 加密 $k_u$ 并发出 $c_{rec}$，攻击者用 $sk^{adv}_{org}$ 解密即得到 $k_u$，从而能读取并修改目标用户的全部保险库数据。攻击只要求用户加入某组织，攻击者不必控制它：一份来自可信企业或家人的诚实邀请就足够。失陷还会扩散：组织私钥 $sk_{org}$ 对所有成员可见，攻陷一个用户即拿到他所属全部组织的 $sk_{org}$；若其中某组织启用了恢复，攻击者便连带拿下其所有用户，并以蠕虫式在共享成员的组织间传播。

**BW02：恶意密钥轮换（Malicious Key Rotation）。** Bitwarden 允许用户修改主密码，并可选地轮换密钥。轮换时客户端采样新的用户密钥 $k_u'$，用新的扩展主密钥 $k_{em}'$ 加密它。已加入恢复的用户还必须重新生成恢复密文，于是客户端用 $pk_{org}$ 加密 $k_u'$，把新的 $c_{rec}'$ 发给服务器。关键在于 $pk_{org}$ 的来源：它不从用户保险库读取，而由一次与服务器的同步取得，且返回的组织数据同样未经认证。于是攻击者可再次拿到用户密钥：提供自己知道 $sk^{adv}_{org}$ 的新 $pk^{adv}_{org}$，并把恢复注册置为 true，客户端就发出含新用户密钥的 $c_{rec}'$，攻击者解密即得到 $k_u'$，进而读取并修改保险库。该攻击不要求用户此时属于某组织：BW08 或 BW09 可把用户加入新建组织或覆盖已有组织的密钥；唯一要求是用户执行密钥轮换。

### 4.1.2 LastPass

LastPass 也提供两种密钥托管：账户恢复与管理员密码重置，这里关注后者。主密码重置属于付费企业产品 “business” 和 “teams”，但代码同样在客户端中，与订阅状态无关。团队中称为 super admin 的特权账户可重置其他成员的主密码，每个管理员账户都有一对 RSA 密钥 $(sk_{adm}, pk_{adm})$。管理员发起重置后，被选中用户的客户端会在下次通过 LastPass 浏览器扩展登录时，从服务器取回管理员列表及其公钥，用用户密钥 $k_u$ 分别在各管理员的公钥 $pk^i_{adm}$ 下加密后发回服务器。

**LP01：恶意密码重置（Malicious Password Reset）。** 客户端对这些从服务器取回的管理员公钥不作任何认证，因此攻击者可轻易注入自己的 $pk^{adv}_{adm}$（并知道 $sk^{adv}_{adm}$），从客户端发出的密文中恢复 $k_u$，从而读取并修改整个保险库。理论上只有启用了重置且被选中重置的团队成员会受影响；实际上客户端每次登录都查询服务器、取回管理员密钥列表并发送恢复密文，与是否加入恢复无关。只有浏览器扩展支持这套流程，攻击的唯一要求是用户在该客户端登录。

### 4.1.3 Dashlane

4.1 节开头提到 Dashlane 的一处设计弱点，但发表版本在密钥托管之下没有 Dashlane 小节：与 Bitwarden 的 Key Connector 一样，该描述被留到论文完整版。表 1 中与此最接近的 Dashlane 攻击是 DL01 Transaction Replay，归入条目级保险库加密类。Dashlane 的保险库是事务型数据库，内容用由主密码派生的密钥加密，发表材料中没有描述任何托管机制。

## 本章要点

- 攻击按成因分为四类——密钥托管、条目级保险库加密、共享、向后兼容——四者中攻击者都完整控制服务器。
- 密钥托管存在，是因为在 E2EE 管理器中忘记主密码就等于永久失去保险库；成功的恢复机制攻击通常能拿到整个保险库。
- “为部分用户提供恢复不得削弱未选择加入者”这一要求并未满足：Bitwarden 和 LastPass 都从服务器取回恢复策略与公钥而不加认证。
- BW01 在用户接受任何组织邀请时即可取得 Bitwarden 用户密钥并蠕虫式传播；BW02 在密钥轮换时再次取得它。
- LP01 能取得 LastPass 用户密钥：客户端每次登录都向取回的管理员密钥发送恢复密文，与是否加入恢复无关。
- 表 1 的 25 个攻击中只有 BW01、BW02、BW03、LP01 属于密钥托管类；Dashlane 的托管弱点留在完整版中。

# 导读：《关于加密的零知识》

本书是论文 *Zero Knowledge (About) Encryption: A Comparative Security
Analysis of Three Cloud-based Password Managers* 的逐章精读。作者为苏黎世联邦理工
学院的 Matteo Scarlata、Kenneth G. Paterson，以及卢加诺瑞士意大利语大学的
Giovanni Torrisi 与 Matilda Backendal，发表于第 35 届 USENIX Security 研讨会
（2026）。论文在"存储加密保险库的服务器**完全恶意**"这一威胁模型下分析了
Bitwarden、LastPass 与 Dashlane —— 三者合计超过 6000 万用户、约占 23% 市场
份额 —— 并给出 25 个可实际利用的攻击：Bitwarden 12 个、LastPass 7 个、
Dashlane 6 个。

九个章节沿论文结构展开，同时折入第一作者在会议上的讲解视频：书中的若干解释、
贯穿全文的例子，以及对第四家厂商的对比，都来自那段视频。

## 论文的论点

"零知识加密"是厂商的营销话术，不是技术术语。厂商用它来宣称：服务器永远不会
知道它所存储的保险库里有什么 —— 即便服务器本身是攻击者。论文把这句宣称当作
可以检验的命题，去实测它的成立条件。结论是它经不起实现的检验：攻击后果从
"篡改某个特定用户的保险库完整性"一直到"攻陷某个组织名下的全部保险库"，其中
大多数都能恢复出密码。

这并不意味着密码管理器无用。真正值得注意的是：恶意服务器这一威胁模型暴露出一
组反复出现的设计反模式与密码学误解，把它们命名出来，对一般的端到端加密系统
同样有价值。

## 阅读方式

每章末尾都有一份"本章要点"，列出该章确立的结论。记号与攻击编号
（BW01…BW12、LP01…LP07、DL01…DL06）沿用论文，因此可以对照 PDF 的相应小节
阅读。书中带有特定含义的术语做了高亮：鼠标悬停会显示一句话释义，点击则跳到
[术语表](../../glossary.md)。

数学公式由 MathJax 排版。当论文与讲解视频对同一机制的描述不一致时，以论文为准，
并注明差异。

## 材料来源

- 论文：[USENIX Security '26 页面](https://www.usenix.org/conference/usenixsecurity26/presentation/scarlata)（[PDF](https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_scarlata.pdf)）
- 预印本：[Cryptology ePrint Archive 2026/058](https://eprint.iacr.org/2026/058)
- 项目主页：[zkae.io](https://zkae.io/)
- 讲解视频：*USENIX Security '26 — Zero Knowledge (About) Encryption*，USENIX（19 分钟）

完整清单（含各厂商的处置声明）见[参考资料与来源](sources.md)。

---

本书由 **course-textbook-builder** 流程生成
（<https://github.com/YoungY620/my-awesome-skills>）。

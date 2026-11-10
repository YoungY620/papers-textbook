# 参考资料与来源

## 一手材料

Juhee Kim, Wenbo Guo, Dawn Song. **SoK: Attack and Defense Landscape of
Agentic AI Systems.** 载于 *第 35 届 USENIX Security 研讨会
（USENIX Security '26）*，马里兰州巴尔的摩，2026 年 8 月。USENIX
Association。

- 会议页面：<https://www.usenix.org/conference/usenixsecurity26/presentation/kim-juhee-agentic>
- 预印本 PDF（本书依据的版本）：<https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_kim-juhee-agentic.pdf>
- 正式论文集 PDF：<https://www.usenix.org/system/files/usenixsecurity26-kim-juhee-agentic.pdf>

作者分别来自加州大学伯克利分校、首尔大学（Juhee Kim，本文工作完成于其在伯克利
访问期间）与加州大学圣塔芭芭拉分校（Wenbo Guo）。

## 讲解视频

会议页面上没有这篇论文的录像，因此本书完全依据论文撰写。这与"密码管理器"那一
册存在实质差别：那一册折入了演讲录像，而本书没有任何内容来自第二个来源，也没有
经过讲者本人叙述的交叉核对。

## 论文自身的来源

这篇论文是一份系统化综述，其主体内容是对他人工作的归纳：攻击论文、防御论文与已
部署系统。若要深入了解本书提到的某个具体机制，论文的参考文献列表是应该去的地方。
本书在正文中保留了系统名称，以便在论文的参考条目里找到对应引用。

论文所依托、也值得直接阅读的规范与分类体系：

- MITRE ATLAS，面向 AI 系统的对抗性威胁全景，论文将其风险分类映射到这一体系上。
- 模型上下文协议（MCP），论文在"工具投毒"下讨论的工具接口机制。

## 本书的编写方式

各章依据论文正文与页面图像撰写。插图以 300 dpi 从论文裁出；论文中的表格重排为
Markdown，并对照页面图像核对。中文与英文是并行撰写而非互相翻译。

论文把极其庞大的工作量压缩进了二十页。本书不试图把它重新展开：它解释机制与分类
框架，并保留标识符（`V1`…`V6`、`R1`…`R7`），使任何一条论断都能追溯到论文自己的
表格。

---

本书由 **course-textbook-builder** 流程生成
（<https://github.com/YoungY620/my-awesome-skills>）。

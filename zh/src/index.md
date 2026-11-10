# USENIX Security '26 论文精读

逐章精读安全领域的论文。每篇论文在本站内是一本书：把论文的论证重写成连贯的正文，
从论文中重绘插图，在存在会议讲解视频时把它折入，并单列一章讲论文所对标的相关工作
与基线。

全部内容以两种语言发布——英文在站点根目录，中文在 `/zh/`——顶栏可一键切换，并共用
一份跨论文的[术语表](glossary.md)。

## 收录论文

### [《关于加密的零知识：三款云端密码管理器的对比安全分析》](./papers/zk-encryption/index.md)

Matteo Scarlata、Giovanni Torrisi、Matilda Backendal、Kenneth G. Paterson，
USENIX Security 2026。

在"存储加密保险库的服务器完全恶意"这一威胁模型下，对 Bitwarden、LastPass 与
Dashlane 给出 25 个可实际利用的攻击，分为密钥托管、条目级保险库加密、共享与向后
兼容四类。书中折入了作者的会议讲解视频，对第四家厂商的对比正来自那段视频。

### [《SoK：智能体 AI 系统的攻防全景》](./papers/agentic-ai-sok/index.md)

Juhee Kim、Wenbo Guo、Dawn Song，USENIX Security 2026。

首份面向 AI 智能体安全的系统化综述：决定风险高低的七个设计维度、攻击向量
`V1`…`V6`、安全风险 `R1`…`R7`，以及按"防护机制位于控制流的哪个环节"组织的防御
全景。

## 每本书是怎么做出来的

各章依据论文正文与页面图像撰写。插图以 300 dpi 从论文裁出；论文中的表格重排为
Markdown 并逐格对照页面图像核对；公式由一个预处理器保护，避免被 Markdown 解析器
破坏，从而正确排版。中文与英文是并行撰写而非互相翻译。

每本书的最后一章讲论文对标的工作与它所属的方向，材料直接取自被引用的论文本身。

---

本站由 **course-textbook-builder** 流程生成
（https://gist.github.com/YoungY620/d4932154735b55903d5a53b5f6f406c9）。

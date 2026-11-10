# 参考资料与来源

## 一手材料

Matteo Scarlata, Giovanni Torrisi, Matilda Backendal, Kenneth G. Paterson.
**Zero Knowledge (About) Encryption: A Comparative Security Analysis of Three
Cloud-based Password Managers.** 载于 *第 35 届 USENIX Security 研讨会
（USENIX Security '26）*，马里兰州巴尔的摩，2026 年 8 月，第 4267–4286 页。
USENIX Association。

- 会议页面：<https://www.usenix.org/conference/usenixsecurity26/presentation/scarlata>
- 预印本 PDF（本书依据的版本）：<https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_scarlata.pdf>
- 正式论文集 PDF：<https://www.usenix.org/system/files/usenixsecurity26-scarlata.pdf>
- Cryptology ePrint Archive 预印本 2026/058：<https://eprint.iacr.org/2026/058>
- 项目主页（含代码与制品声明）：<https://zkae.io/>

## 讲解视频

*USENIX Security '26 — Zero Knowledge (About) Encryption: A Comparative
Security Analysis of Three Cloud-based Password Managers*，主讲 Matteo
Scarlata，USENIX，时长 19 分钟。
<https://www.youtube.com/watch?v=jpYYXMAoY5U>

视频内容由自动字幕转写而来。凡转写与论文不一致处，本书以论文为准；只出现在
视频中的内容会明确标注。关于这段录像有两点需要说明：讲者开场把工作对象描述为
**四款**密码管理器，用 1Password 作对照，而论文的完整分析覆盖三款；自动字幕会
弄错产品名，因此转写文本不能作为标识符的可靠来源。

## 厂商回应

三家厂商各自发布了他们对这些发现的说明以及修复工作。**这些是厂商的主张，不是
论文的发现**，本书照此记录。

- Bitwarden —— *Security Through Transparency: ETH Zurich audits Bitwarden cryptography*：<https://bitwarden.com/blog/security-through-transparency-eth-zurich-audits-bitwarden-cryptography/>
- Dashlane —— *Zero knowledge and the malicious server*：<https://dashlane.com/blog/zero-knowledge-malicious-server>
- Dashlane —— 关于所报问题的支持文档：<https://support.dashlane.com/hc/articles/33346483084050>
- LastPass —— *Details on hardening in response to ETH Zurich reported security issues*：<https://blog.lastpass.com/posts/details-on-hardening-in-response-to-eth-zurich-reported-security-issues>
- 1Password —— *ETH Zurich zero-knowledge malicious-server review*：<https://1password.com/blog/eth-zurich-zero-knowledge-malicious-server-review>

## 相关报道

- 瑞士意大利语大学：*Password manager security: joint USI-ETH Zurich study*：<https://www.inf.usi.ch/en/feeds/11405>
- USENIX Security '26 第一轮录用的论文清单：<https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers>

## 本书的编写方式

各章依据论文正文与页面图像撰写，并把会议讲解视频作为第二个来源折入。插图以
300 dpi 从论文裁出；论文中的表格重排为 Markdown，并逐格对照页面图像核对。中文
与英文是并行撰写而非互相翻译，这个过程在两边的版本里都揪出了若干转写错误。

有两点局限需要说明。其一，视频无法逐帧观看——只取到了字幕轨——因此讲者仅通过
画面传达、未口述的内容没有进入本书。其二，论文的攻击验证代码并未公开，本书没有
重新实现或独立复现其中任何一个攻击。

---

本书由 **course-textbook-builder** 流程生成
（https://github.com/YoungY620/my-awesome-skills）。

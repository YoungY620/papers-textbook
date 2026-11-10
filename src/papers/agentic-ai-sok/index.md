# SoK: Attack and Defense Landscape of Agentic AI Systems

This is a chapter-by-chapter reading of *SoK: Attack and Defense Landscape of
Agentic AI Systems* by Juhee Kim (UC Berkeley and Seoul National University),
Wenbo Guo (UC Santa Barbara) and Dawn Song (UC Berkeley), published at the 35th
USENIX Security Symposium (2026). A *systematisation of knowledge* is not a new
attack paper: it takes a field that has grown faster than its vocabulary,
imposes a structure on it, and says what the structure reveals. This one does
that for the security of AI agents — systems that fuse a large language model
with ordinary software: a planner, a memory, tools, a user interface and an
execution environment.

The nine chapters follow the paper's own order: what an agent is, the seven
design dimensions that determine how risky it is, the attack vectors, the
security risks, and then the defence landscape, grouped the way the paper
groups it.

## What the paper argues

The incidents are already real: prompt injection reaching private
repositories, remote code execution, data exfiltration through malicious
documents and email forwarding, exposed chat and credential data, web agents
that can be driven into a user's banking account. What the paper adds is the
claim that these are not a longer list of LLM problems. An agent is a
*system*, and its security is a systems property.

The organising idea is **flexibility**. Each design dimension — how much an
agent trusts its inputs, how sensitive the data it can reach, how its workflow
is fixed, what actions it may take, what it remembers, which tools it holds and
how a human talks to it — is a dial. Turning the dial toward flexibility buys
capability and widens the attack surface, and the dimensions compound. That is
why component-level defences are not enough, and why the paper insists on
defence in depth.

## How to read this book

The chapters keep the paper's identifiers. `V1`…`V6` are the attack vectors
and `R1`…`R7` the security risks; they reappear throughout, including in the
defence chapters, where each mechanism is described partly in terms of which
risks it covers. A claim in this book should be traceable to the paper's own
tables by those identifiers.

Terms that carry a specific meaning here are highlighted in the text: hovering
one shows a one-line gloss, and clicking it opens the [glossary](glossary.md).

## Source material

- Paper: [USENIX Security '26 presentation page](https://www.usenix.org/conference/usenixsecurity26/presentation/kim-juhee-agentic) ([PDF](https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_kim-juhee-agentic.pdf))

There is no recorded conference talk for this paper, so unlike the companion
volume on password managers, this book has a single source. See
[References and source material](sources.md).

---

This book was produced by the **course-textbook-builder** workflow
(https://gist.github.com/YoungY620/d4932154735b55903d5a53b5f6f406c9).

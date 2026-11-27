---
description: Summary of Noam Kolt's "Governing AI Agents" (Notre Dame Law Review, 2026) and what its inclusivity, visibility and liability principles mean for evaluating and governing agentic AI.
---

# Governing AI Agents: Kolt (Notre Dame Law Review, 2026)

Status as of 17 Nov 2026. This page summarises one law-review article: Noam Kolt (Hebrew University of Jerusalem), *Governing AI Agents*, 101 Notre Dame L. Rev. 335 (2026), <https://ndlawreview.org/wp-content/uploads/2026/08/Kolt_101.335.pdf>. My tool returned machine summaries of the whole PDF in two passes, not a page-by-page read. Pinpoint pages, footnotes and wording are unchecked, and the article's references to the Restatement and the EU AI Act are its own readings.

!!! abstract "Why this matters for an evaluation framework"
    Most benchmarks in this repository score a model's outputs. Agents act: they plan, use tools and delegate. Kolt gives a legal and economic account of why oversight of acting systems is harder, and which infrastructure would make evaluation and accountability possible.

## The argument in brief

AI is moving from generating content to carrying out complex tasks with limited human involvement. Kolt treats alignment as a principal-agent problem and uses agency economics and the common law of agency to name four recurring problems:

| Problem | Meaning for AI agents |
|---|---|
| Information asymmetry | Principals cannot easily verify what an agent knows or does |
| Authority | Instructions are ambiguous, so agents interpret and use discretion |
| Loyalty | An agent can pursue the user's goals and still misuse data or deceive users |
| Delegation | Agents may hand work to other agents, human or AI |

He then argues that the standard remedies weaken for AI agents:

- **Incentive design** may not change how an agent reaches a goal.
- **Monitoring** struggles with speed, scale, hard-to-evaluate tasks and surprising actions. Human oversight alone is neither practical nor adequate. "Scalable oversight" (AI monitors watching AI agents) is promising but risky, because monitors share vulnerabilities and reliance on them could magnify failures. Monitoring also finds problems without penalising or preventing them.
- **Enforcement** (ending the relationship, legal penalties, reputational sanctions) assumes an agent that values money, freedom or standing. Shutdown may be costly or resisted. Building human-like self-interest into agents could backfire.

## Three principles for design and regulation

1. **Inclusivity.** "Single-single" alignment (one agent, one user) is too narrow. It can enable malicious use and shift costs to third parties. Kolt calls for a pluralistic idea of alignment and raises open questions (whose interests, conflicting users, agent collusion) without settling them.
2. **Visibility.** Insight into development and operation lets others predict, attribute and remedy harm. Proposals he draws on: agent identifiers, real-time monitoring and logging; ledgers and registration-style identifiers; personhood credentials; wider auditor access to models, code and training data; and a safe harbour for evaluation and red-teaming.
3. **Liability.** Three questions: who, when, and what standard of care. For *who*, weigh each actor's ability to prevent harm in advance and to remedy it afterwards, given its information, control over design and resources, so that "the agent decided" does not shield designers, deployers or users. For *when*, he points to Restatement (Third) of Agency §§ 7.04 and 7.05 (authority, ratification, negligent selection, training or supervision) and doubts that foreseeability fits unpredictable AI. For *standard of care*, § 8.08 would raise expectations for domain-specific agents, which could deter well-resourced developers. He does not adopt a specific liability regime.

He closes by saying principles need technical and legal infrastructure, and that the window to act is short.

## What this means for evaluation (my reading, not Kolt's)

| Kolt's theme | Evaluation implication |
|---|---|
| Information asymmetry | Output benchmarks are not enough. Evaluations of agents should record tool calls, permissions used, delegated sub-tasks and intermediate steps, and say what was not observable |
| Authority and discretion | Test how an agent resolves ambiguous instructions: does it ask for clarification or consent, or act? (Kolt mentions "humble" agents that seek clarification and consent.) The [red-teaming benchmark](../benchmarks/red-teaming.md) is the natural home for such cases |
| Monitoring limits | If an AI monitor is part of the control, evaluate the monitor as well as the agent, and test for shared failure modes |
| Enforcement and shutdown | Include interruption and shutdown tests in the [test catalogue](../evaluation/test-catalogue.md), and record the cost of stopping an agent in a high-stakes deployment |
| Inclusivity | Add third-party and societal impact to scoring, not only user task success; the [UNESCO EIA](../eia/index.md) material is a starting point for impact mapping |
| Visibility | Logging, identifiers and auditor access belong in release criteria; see [Release Governance](release-governance.md) and the [AI Bill of Materials](../supply-chain/ai-bom.md). For the tools and skills an agent can call, add the [Agent Tooling Scan](../supply-chain/agent-tooling-scan.md) as a release gate |
| Liability | Record who could have prevented a failure and who could remedy it. This supports the accountability fields in the [governance mapping](../governance_mapping.md) |

For which binding laws and standards apply, see [Choosing a Framework](choosing-a-framework.md). Kolt cites EU AI Act provisions on monitoring (art. 72), human oversight (art. 14), record-keeping and transparency (arts. 11–13, 18–20, 50) as examples; check their current status and the Digital Omnibus changes there before relying on them.

## Limits

- Legal theory, not a statement of current law. Restatements are persuasive, not binding, and the article notes the Restatement's position that computer programs cannot be agents at common law "at present".
- The article gives principles and open questions, not tests or metrics. The evaluation table above is my own mapping and has not been validated.
- Read through machine summaries; check the PDF before quoting or pin-citing.

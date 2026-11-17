---
description: Hands-on AI security and red-teaming practice platforms (prompt injection games, AI CTFs, web LLM labs) for evaluation teams, with publisher-checked descriptions and safe-use notes.
---

# Hands-on AI Security Labs

Status as of 17 Nov 2026. A practical list of free or low-cost places where evaluators and red-teamers can practise attacking and defending AI systems, to build the skills used in the [red-teaming benchmark](../benchmarks/red-teaming.md) and the [test catalogue](test-catalogue.md). The starting list came from a social-media post that collected 23 labs; I have not cited the post. For the AI-security entries below I checked descriptions against the operators' own pages or published research where my search reached them. Operator sites were not on my fetch allowlist, so I did not open the labs themselves or test that every link still works.

!!! warning "Use these as intended"
    Attack only the challenge environments the operator provides. Do not use live organisational systems, real personal data or real credentials in any lab. PortSwigger notes that some of its AI labs collect telemetry, including AI interaction logs, so read the privacy notice before use. Several labs use a live LLM, so results vary between attempts.

## AI security and red teaming

| Lab | Operator | What it offers | Evidence checked | Evaluation use |
|---|---|---|---|---|
| Gandalf: Agent Breaker (<https://gandalf.lakera.ai/agent-breaker>) | Lakera (a Check Point company) | A hacking simulator where players attack ten mock agentic AI apps with escalating defences | Lakera's own blog describes it as a public red-teaming testbed with ten mock agentic apps. A third-party guide says the original Gandalf password game now redirects to Agent Breaker (as of Nov 2026); I did not confirm this on Lakera's site | Source data for the open-source **b3 (backbone breaker) benchmark** built with the UK AI Security Institute: 10 agent "threat snapshots" plus 19,433 crowdsourced adversarial attacks from the game, per the Check Point and Lakera announcement as reported by trade press |
| Crucible (<https://crucible.dreadnode.io>) | Dreadnode | Free, hosted AI red-teaming CTF challenges, solved mostly through code | Dreadnode's own research describes Crucible as a free, open environment for empirical AI red teaming. Its AIRTBench paper uses 70 black-box CTF challenges from Crucible to test whether models can find and exploit AI/ML vulnerabilities on their own | Practising attack automation; AIRTBench is a worked example of using CTF challenges as an agent evaluation |
| HackAPrompt (<https://hackaprompt.com>) | Learn Prompting | Prompt-injection and jailbreak competitions and learning hub | The HackAPrompt 1.0 paper (arXiv 2311.16119) describes a global competition and dataset. Learn Prompting announced HackAPrompt 2.0 in January 2025, with five tracks and wider AI red-teaming scope | Dataset and attack taxonomy for prompt-injection testing; competitions change, so check current status |
| Prompt Airlines (<https://promptairlines.com>) | Wiz | A chatbot CTF: manipulate a fictional airline's customer-service bot into giving a free ticket; no coding needed | Wiz's launch post describes it as based on real AI vulnerabilities found by Wiz Research, open to all skill levels | Entry-level training for system-prompt leakage and tool or document manipulation |
| Web LLM attacks (<https://portswigger.net/web-security/llm-attacks>) | PortSwigger Web Security Academy | Free labs on LLM API abuse, excessive agency, indirect prompt injection and insecure output handling; newer labs on AI-powered scanner vulnerabilities | PortSwigger's lab pages confirm these topics and that the labs use a live LLM. Some AI-scanner labs collect telemetry including AI interaction logs | Maps to excessive agency and indirect injection risks in the [threat taxonomy](../threats/adversarial-ml-taxonomy.md) |

## Other labs in the source list (not checked)

The original list also names the following. I did not verify their current status or content; treat them as pointers.

| Skill area | Platforms named |
|---|---|
| Foundations | OverTheWire Bandit (Linux and shell), TryHackMe, picoCTF, pwn.college |
| Offensive security | Hack The Box, PortSwigger web security, OWASP Juice Shop, CryptoHack |
| Reverse engineering | Crackmes.one, MicroCorruption |
| Cloud security | flaws.cloud, BigIAM Challenge, EKS Cluster Games |
| Defensive security | LetsDefend, CyberDefenders, Blue Team Labs Online |
| Compete | CTFtime |

## How to use this in an evaluation programme

1. **Build team competence before scoring.** Have evaluators solve a few prompt-injection and agent-abuse challenges so they understand failure modes before they design test cases.
2. **Harvest attack patterns, not answers.** Use what the labs teach (instruction override, indirect injection, tool misuse, data exfiltration) as categories for your own test suite, then write your own prompts for your own systems.
3. **Treat game datasets with care.** The b3 benchmark and HackAPrompt dataset are research artefacts; check their licences and release terms before reusing them, and follow this repository's [release governance](../governance/release-governance.md) before publishing derived adversarial prompts.
4. **Record the limits.** Challenge success does not measure a production system's risk. Live-LLM labs are non-deterministic and results are not reproducible benchmark scores.

## Gaps

- Operator pages were not fetched directly; descriptions rest on search results from operators' blogs, research papers and trade press.
- The Agent Breaker redirect claim is from one third-party guide.
- No lab was run, so difficulty, current availability and any registration requirement are untested.

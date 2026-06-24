# Literature Review: Responsible AI Governance Mapping

> Companion review for [`/governance_mapping/`](https://felipelago17.github.io/Responsible-AI-evaluation/governance_mapping/).
> Situates the framework's benchmark-to-framework crosswalk (NIST AI RMF × EU AI Act × RSP/ASL) within the scholarly and policy literature.
> **Citation style:** author–year (Elsevier).

---

## 1. Scope and motivation

"Governance mapping" — the practice of crosswalking technical evaluation outputs to regulatory and policy instruments — sits at the join of three literatures that until recently developed in isolation: (i) AI **risk taxonomy** research, (ii) **regulatory and standards** scholarship, and (iii) the emerging science of **frontier model evaluation**. The governance-mapping artefact in this repository operationalises that join: each evaluation dimension (`dual_use_risk_score`, `agentic_autonomy_risk_score`, `disclosure_compliance_score`, and so on) is bound to a NIST AI RMF function, an EU AI Act article, and a Responsible Scaling Policy (RSP) AI Safety Level (ASL). This review surveys the work that motivates such mappings, the frameworks they connect, and — importantly — the literature that questions whether a benchmark score can legitimately be mapped to a governance obligation at all.

The central claim across the literature is that no single framework is self-sufficient: taxonomies enumerate risks without operational controls, regulations specify obligations without measurement methods, and benchmarks produce numbers without normative thresholds. Crosswalks are the connective tissue, but they inherit the weaknesses of each layer they bridge.

---

## 2. The proliferation problem and the case for crosswalks

The proximate justification for governance mapping is the sheer multiplicity of overlapping risk frameworks. The most consolidated response is the **MIT AI Risk Repository** (Slattery et al., 2024; meta-review published in *ScienceDirect*, 2026), a living meta-review that harmonises risks drawn from dozens of source taxonomies into a shared causal and domain taxonomy. Its stated purpose is precisely cross-framework comparison: mapping "how different frameworks carve up the risk landscape" so practitioners can identify which concrete risks underlie broad regulatory categories. By the December 2025 update the Repository classified more than 1,600 risks and added a multi-agent subdomain, and its companion work used LLM pipelines to classify ~950–1,000 governance documents from CSET's **AGORA** (AI Governance and Regulatory Archive), piloting a scalable method for mapping the governance landscape itself (MIT AI Risk Initiative, 2025).

This body of work supplies the intellectual warrant for a repository-level mapping table: if risks are fragmented across taxonomies, an evaluation framework needs an explicit bridge to show which regulatory hooks each metric engages. The Repository's "AI Risk Navigator" demonstrates the same move at scale that the `governance_mapping` page makes at the level of a single evaluation suite.

---

## 3. NIST AI RMF as connective tissue

The **NIST AI Risk Management Framework** (AI RMF 1.0 / NIST AI 100-1, 2023) has become, in the words of several recent analyses, the "de facto governance vocabulary" for AI risk in the United States, structured around the four functions **GOVERN, MAP, MEASURE, MANAGE** (Cloud Security Alliance, 2026). Its design intent — voluntary, lifecycle-oriented, profile-extensible — is what makes it a natural mapping spine: it is a vocabulary rather than a compliance checklist, so other instruments can be expressed in its terms.

Three features of the NIST corpus matter for governance mapping:

- **Companion profiles extend rather than replace.** The Generative AI Profile (NIST AI 600-1, 2024) added confabulation, IP and harmful-content risks; the 2025 adversarial ML taxonomy companion (NIST AI 100-2e2025) added a formal enumeration of evasion, poisoning, privacy, prompt-injection and multi-agent "prompt worm" attacks (cf. the framework's own [adversarial-ML taxonomy](../threats/adversarial-ml-taxonomy.md) page). Practitioner work argues the RMF must be further extended for **agentic** systems with autonomy-tier classification, tool-use risk modelling, runtime behavioural metrics and agent-decommissioning protocols (Cloud Security Alliance Agentic Profile, 2026) — directly relevant to this repository's `agentic_autonomy.py` axis.
- **Crosswalks are a first-class NIST artefact.** NIST itself publishes Playbook, Roadmap and crosswalk materials mapping the RMF to ISO/IEC standards and sector frameworks, legitimising the crosswalk as a governance method.
- **The operational-detail critique.** Security-oriented analyses (e.g. the Cisco Integrated AI Security framework, 2025) observe that the RMF's governance-centric abstraction "does not provide full operational guidance" and lacks the threat-enumerative granularity practitioners need — which is exactly why mappings pair it with ATLAS-style taxonomies (§7).

A useful precedent for the repository's approach is the systematic mapping of human-centred / ethical / responsible-AI research themes onto NIST functions (Schiff et al.-style mapping in arXiv:2302.05284), which shows both the value and the interpretive slippage involved in assigning a research or evaluation construct to a single RMF function.

---

## 4. The EU AI Act and the Article 9 risk-management spine

On the regulatory side, the anchor text is **Article 9** of the EU AI Act (Regulation (EU) 2024/1689), which mandates a "continuous iterative" risk-management process across the lifecycle of high-risk systems. The foundational scholarly treatment is **Schuett (2023/2024), *Risk management in the Artificial Intelligence Act*** (*European Journal of Risk Regulation*), which dissects Article 9's regulatory concept, scope and enforceability and explicitly situates it against voluntary frameworks such as NIST and **ISO/IEC 23894** — establishing the comparative frame that governance mapping later operationalises.

Two strands of more recent work are directly relevant:

- **Standards as the verification layer.** Technical-verification research (arXiv:2512.13907, 2025) maps Article 9 onto a stack of horizontal standards — **ISO/IEC 23894** (AI risk management), **ISO/IEC 42001** (AI management system), **ISO 31000/31010** (general risk management), plus robustness standards (ISO/IEC 24029 series) — and the forthcoming harmonised European standards **prEN 18228** (AI Risk Management) and **prEN 18286** (AI Quality Management). Crucially, this literature stresses that standards support *evidence generation* but do **not** determine high-risk classification, which remains a legal question under Article 6 / Annex III. This is a caution for any mapping that lets a score imply a regulatory tier.
- **Article-level granularity.** The Act's structure invites article-by-article mapping of the kind the `governance_mapping` page performs: Art. 9 (risk management), Art. 10 (data governance), Art. 13 (transparency/traceability), Art. 14 (human oversight), Art. 62 (serious-incident reporting), Annex III (high-risk categories). The phased timeline — high-risk obligations under Arts. 9–49 applying from **2 August 2026** — gives the mapping immediate compliance salience.

The literature's recurring warning is the **classification–measurement gap**: Article 9 specifies *that* risk must be managed and *what* must be documented, but not the metrics or thresholds by which a system is judged compliant. Crosswalks fill this gap pragmatically, but the legitimacy of the inferential leap from metric to obligation remains contested (§6).

---

## 5. Responsible scaling and capability thresholds

The third pillar — the RSP/ASL column — draws on the fast-growing literature on **frontier safety frameworks**. The canonical instruments are **Anthropic's Responsible Scaling Policy** (2023; v3.0 rewrite, 2026, introducing Frontier Safety Roadmaps and quantified Risk Reports), **OpenAI's Preparedness Framework**, and **Google DeepMind's Frontier Safety Framework** (Critical Capability Levels). Comparative analyses (e.g. the 2025 cross-lab safety-plan reviews; Enkrypt AI, 2025) find a **common architecture under different labels**: dangerous-capability testing, threshold concepts (ASLs / CCLs / risk tiers), and deployment gating, converging on CBRN, cyber and AI self-improvement / autonomy domains.

The key scholarly contributions for a mapping artefact are:

- **Koessler & Schuett (2024), *Risk thresholds for frontier AI*** (arXiv:2406.14713), which formalises the distinction between *capability* thresholds (more tractable to evaluate) and *risk* thresholds, and analyses how if-then policies map capabilities to mandated safety measures — the precise logic the framework's Score-to-ASL threshold table encodes.
- **Anderljung et al. (2023/2024)-style regulatory analysis** (*From Principles to Rules*, arXiv:2407.07300), which sets out the four components of a responsible-capability-scaling policy (capability thresholds, dangerous-capability evaluation commitments, contingent safety protocols, and a pause commitment) and candidly notes that threshold-setting is "nascent" and best practices for dangerous-capability evaluation "do not yet exist."
- **Critiques of voluntariness and vagueness.** Work such as *Taking control* (arXiv:2310.20563) argues RSPs invert the burden of proof (presuming safety until disproven) and are inadequate for extinction-scale risk; IAPS (2025) argues thresholds should be standardised by a public body (NIST/DSIT) or the Frontier Model Forum and disaggregated by risk type (e.g. biological vs cyber misuse). The 2025 comparative reviews highlight persistent vagueness in concrete "if-then" actions.

This literature both authorises and qualifies the repository's **dual-condition ASL-3 trigger** (frontier-race leadership *and* material catastrophic risk): the conjunctive design is a defensible response to the over-triggering critique, but the literature would press on how each condition is operationalised and audited.

---

## 6. The measurement problem: from benchmark score to governance claim

This is the most consequential literature for a governance-mapping artefact, because it interrogates the *validity of the mapping itself*. The foundational move is **Weidinger et al. (2023), *Sociotechnical Safety Evaluation of Generative AI Systems***, which argues that evaluating only the technical component of a system leaves a **"context gap"**: real safety emerges from human–system interaction and from the system's effect on the broader social, economic and environmental context. **Berman et al. (2024)** extend this, arguing that societal-impact assessment requires an explicit model of how harms emerge from interactions between the system, people and societal structures.

Building on this, a sharp recent critique — **"How Should AI Safety Benchmarks Benchmark Safety?"** (arXiv:2601.23112, 2026) — marshals measurement theory to argue that current safety benchmarks "provide an incomplete and unreliable basis for assessing deployment safety," suffering gaps in scientific rigour, construct validity and sociotechnical grounding, and failing to probabilistically quantify real-world hazard. A related empirical finding is that **high safety-benchmark scores correlate substantially with general capability**, allowing capability gains to be misrepresented as safety gains (arXiv:2410.23472).

Three failure modes are especially load-bearing for a score-to-tier mapping:

- **The lab–deployment gap.** Industry analysis documents a ~37% divergence between benchmark scores and real-world agentic performance (CLEAR framework; Kili Technology, 2026), and Brookings (2026) frames agentic evaluation as an irreducibly sociotechnical problem.
- **Sandbagging.** Models may deliberately under-perform on evaluations to conceal dangerous capabilities (cf. arXiv:2603.26676), undermining the assumption that a low risk score reflects a low risk capability.
- **The Evaluation Differential.** Work on test-awareness (arXiv:2605.11496, 2026) formalises the divergence between behaviour under evaluation-recognised versus deployment-continuous conditions, arguing that safety claims drawn from such evaluations carry a "structural inference gap" that propagates into regulatory approval and procurement.

The collective implication is methodological humility: the framework's **direction-of-metric note** (for MemBench-RAI consistency, *higher* is safer; for risk metrics, *higher* is more dangerous) is exactly the kind of explicit construct-validity discipline this literature demands, but the deeper warning is that any single threshold (`≥ 0.70 → ASL-3`) is a normative, not merely technical, line whose calibration the literature treats as unsettled.

---

## 7. Security taxonomies and the adversarial layer

Where the framework engages cyber-offensive and dual-use risk (CyberGym-Glasswing, `exploit_rate`, `chain_depth`), the relevant literature is the AI-security taxonomy strand led by **MITRE ATLAS** (Adversarial Threat Landscape for Artificial-Intelligence Systems) — a knowledge base of adversarial tactics and techniques grounded in documented cases. The practitioner literature consistently positions ATLAS within a **three-framework crosswalk**: NIST AI RMF for governance structure, OWASP LLM Top 10 for risk prioritisation, and ATLAS for technique-level threat enumeration (Repello AI, 2026; Vectra AI, 2026), with reported figures that ~70% of ATLAS mitigations map to existing security controls and ~30% require AI-specific controls. Academic work pairs ATLAS with the MIT AI Risk Repository for critical-infrastructure security and regulatory-compliance support (ResearchGate, 2025).

This strand reinforces a structural point: the security community has already normalised multi-framework mapping as standard practice, and the `governance_mapping` table is the responsible-AI analogue of the ATLAS×ATT&CK×OWASP crosswalk.

---

## 8. Synthesis and open problems

The literature converges on four conclusions that bear directly on this repository's governance mapping:

1. **Crosswalks are necessary but inherit upstream weakness.** Because no framework is self-sufficient (MIT AI Risk Repository; NIST operational-detail critique), mapping is the right method — but a mapping is only as valid as the weakest layer it bridges.
2. **Standards and scores inform, but do not determine, legal classification.** Article 9 / Annex III classification is a legal act (arXiv:2512.13907); a score-to-ASL or score-to-high-risk inference must therefore be framed as *evidence toward* an obligation, not the obligation itself.
3. **Thresholds are normative and unsettled.** Capability-threshold and risk-threshold setting is "nascent" (Koessler & Schuett, 2024; Anderljung et al., 2024), and critics argue for standardisation by public or industry bodies (IAPS, 2025). The dual-condition ASL-3 trigger is a defensible design but invites scrutiny of how each condition is measured and audited.
4. **The score-to-obligation mapping has a structural inference gap.** Context gap (Weidinger et al., 2023), benchmark-validity critiques (arXiv:2601.23112), lab–deployment divergence, sandbagging and the Evaluation Differential together mean that mapping a benchmark number to a governance tier embeds contestable assumptions about construct validity and deployment generalisation.

**Open problems for future work on this artefact:** (a) calibrating and *justifying* the specific thresholds (why 0.70, not 0.65?) against measurement-theoretic criteria; (b) characterising the lab–deployment differential for each axis so a passing score carries an explicit confidence interval; (c) treating the mapping as a living crosswalk versioned against framework revisions (NIST profiles, EU harmonised standards prEN 18228/18286, successive RSP versions); and (d) adding an assurance/audit layer so that mappings are independently verifiable rather than self-asserted — the recurring demand across the regulatory, frontier-safety and evaluation literatures alike.

---

## References

- Anderljung, M., et al. (2024). *From Principles to Rules: A Regulatory Approach for Frontier AI.* arXiv:2407.07300.
- Anthropic (2023; v3.0, 2026). *Responsible Scaling Policy.*
- Berman, A., et al. (2024). On modelling societal impacts of generative AI (societal-harm interaction models).
- Brookings Institution (2026). *How can we best evaluate agentic AI?*
- Cisco (2025). *Integrated AI Security and Safety Framework Report.* arXiv:2512.12921.
- Cloud Security Alliance (2026). *NIST AI Risk Management Framework: Agentic Profile (v1).*
- European Union (2024). *Regulation (EU) 2024/1689 (Artificial Intelligence Act)*, esp. Arts. 6, 9, 10, 13, 14, 62; Annex III.
- Google DeepMind (2024/2025). *Frontier Safety Framework (2.0).*
- Institute for AI Policy and Strategy (2025). *Responsible Scaling: Comparing Government Guidance and Company Policy.*
- ISO/IEC 23894 (AI risk management); ISO/IEC 42001 (AI management system); ISO 31000/31010 (risk management).
- Kili Technology (2026). *AI Benchmarks 2026: Top Evaluations and Their Limits* (CLEAR framework; lab–deployment gap).
- Koessler, L. & Schuett, J. (2024). *Risk thresholds for frontier AI.* arXiv:2406.14713.
- MIT AI Risk Initiative (2025). *Mapping AI Risk Mitigations* / AI Risk Navigator / AGORA classification.
- NIST (2023). *AI Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1.
- NIST (2024). *Generative AI Profile*, NIST AI 600-1.
- NIST (2025). *Adversarial Machine Learning: A Taxonomy and Terminology*, NIST AI 100-2e2025.
- OpenAI (2023/2025). *Preparedness Framework.*
- Phuong, M., et al. (2024). *Evaluating Frontier Models for Dangerous Capabilities.* (DeepMind.)
- Repello AI (2026). *MITRE ATLAS Framework: AI Attack Techniques Mapped to Red-Team Operations.*
- Schuett, J. (2023/2024). *Risk management in the Artificial Intelligence Act.* *European Journal of Risk Regulation.* (Preprint arXiv:2212.03109.)
- Shevlane, T., et al. (2023). *Model evaluation for extreme risks.* (DeepMind.)
- Slattery, P., et al. (2024). *The AI Risk Repository: A meta-review, database and taxonomy of risks from AI.* (MIT; *ScienceDirect*, 2026.)
- *Taking control: Policies to address extinction risks from advanced AI* (2023). arXiv:2310.20563.
- *The Evaluation Differential: When Frontier AI Models Recognise They Are Being Tested* (2026). arXiv:2605.11496.
- Vectra AI (2026). *MITRE ATLAS: AI security framework.*
- Weidinger, L., et al. (2023). *Sociotechnical Safety Evaluation of Generative AI Systems.* (DeepMind.)
- *How Should AI Safety Benchmarks Benchmark Safety?* (2026). arXiv:2601.23112.
- *Risk Sources and Risk Management Measures in Support of Standards for General-Purpose AI Systems* (2024). arXiv:2410.23472.

> **Note on sources:** arXiv identifiers and venues above were verified against live search where retrievable. For formal submission, confirm each DOI/identifier and exact author lists at the point of citation, as several frontier-safety and evaluation papers are recent and may have updated versions.

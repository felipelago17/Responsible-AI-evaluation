---
title: 'Part 2 — Principles & Procedural Safeguards'
description: UNESCO EIA Part 2 evaluates an AI system against each of the 10 UNESCO ethical principles, documenting safeguards in place, gaps identified, and planned mitigations.
---

# Part 2 — Principles & Procedural Safeguards

Part 2 is the substantive core of the UNESCO EIA. For each of the 10 principles in the *UNESCO Recommendation on the Ethics of Artificial Intelligence* (2021), assessors document:

- What safeguards are currently in place
- Where gaps exist between the principle's requirements and current practice
- What mitigations are planned to close those gaps

Work through each principle independently during [Stage 3 — Asynchronous Work](how-to-run.md#stage-3--asynchronous-work), then reconcile divergent assessments during [Stage 4 — Collaborative Workshop](how-to-run.md#stage-4--collaborative-workshop).

For the authoritative one-line definitions and the relationship between principles and the 4 core values, see [Principles Reference](principles-reference.md).

---

## 1. Proportionality and Do No Harm

AI systems should only be used when the benefits clearly outweigh the risks, and must not be used when they pose unacceptable risks of harm to individuals, communities, society, or the environment.

=== "Safeguards"

    **Safeguard questions to address:**

    - Has a risk-benefit analysis been conducted that documents the expected benefits and potential harms of this system?
    - Is the system used only for its intended purpose, and are use restrictions enforced technically or contractually?
    - Has the system been tested for harmful outputs, including edge cases and adversarial inputs?
    - Are there red lines — categories of use the organisation will not permit regardless of potential benefit?
    - Is the level of AI autonomy proportionate to the stakes of the decisions being made?

    <!-- Practitioner note: The above questions are drawn from the publicly documented scope of the UNESCO EIA's Principle 1 assessment and paraphrased from the UNESCO Recommendation on the Ethics of AI (2021, UNESDOC pf0000381137), which states: "The use of AI systems must not go beyond what is necessary to achieve a legitimate aim. Risk assessment should be used to prevent harms which may result from such uses" (paraphrased from publicly available UNESCO summary, https://www.unesco.org/ethics-ai/en/eia). The EIA workbook (UNESDOC pf0000386276) contains the official verbatim procedural safeguard questions for this principle; its PDF could not be retrieved programmatically. Download the workbook at https://www.unesco.org/ethics-ai/en/eia to verify against the exact question text. -->

=== "Mitigation"

    **Mitigation prompts:**

    - Define and document explicit use restrictions and deploy technical enforcement (e.g., rate limiting, input filtering, output filtering)
    - Conduct structured red-teaming to surface harmful output scenarios before deployment
    - Establish a harm escalation protocol: define severity thresholds that trigger human review or system suspension
    - Require a risk-benefit sign-off from a senior accountable person before deployment in new contexts
    - Implement ongoing monitoring with defined metrics for detecting disproportionate harm in production

---

## 2. Safety and Security

AI systems must be technically robust, reliable, and secure against adversarial attacks, unintended failures, and misuse throughout their lifecycle.

=== "Safeguards"

    **Safeguard questions to address:**

    - Has the system undergone security testing, including adversarial robustness evaluation?
    - Are there failsafe mechanisms that revert to human control or safe defaults when the system encounters out-of-distribution inputs?
    - Is there a documented incident response plan for AI system failures or security breaches?
    - Are software dependencies and model weights tracked and updated for known vulnerabilities?
    - Does the system meet relevant safety standards for its deployment sector (e.g., IEC 62443 for industrial, HIPAA for healthcare)?

    <!-- Practitioner note: The above questions are drawn from the publicly documented scope of the UNESCO EIA's Principle 2 assessment and paraphrased from the UNESCO Recommendation on the Ethics of AI (2021, UNESDOC pf0000381137), which states: "Unwanted harms (safety risks) as well as vulnerabilities to attack (security risks) should be avoided and addressed by AI actors" (paraphrased from publicly available UNESCO summary). The EIA workbook (UNESDOC pf0000386276) contains the official verbatim procedural safeguard questions for this principle; its PDF could not be retrieved programmatically. Download the workbook at https://www.unesco.org/ethics-ai/en/eia to verify against the exact question text. -->

=== "Mitigation"

    **Mitigation prompts:**

    - Implement adversarial robustness testing as part of the CI/CD pipeline
    - Define and test failsafe and fallback mechanisms before deployment
    - Maintain a vulnerability disclosure and patch management process for AI components
    - Conduct regular penetration testing of AI APIs and inference endpoints
    - Establish a real-time monitoring system with anomaly detection for production inference

---

## 3. Fairness and Non-Discrimination

AI systems must treat all individuals and groups equitably, and must not perpetuate, amplify, or create unjust discrimination on the basis of protected characteristics.

=== "Safeguards"

    **Safeguard questions to address:**

    - Has the system been evaluated for disparate performance across demographic groups (e.g., gender, race, age, disability, religion, national origin)?
    - Are training data sources examined for historical biases that could be encoded into the model?
    - Is the definition of fairness used in the evaluation appropriate for the use case (e.g., demographic parity, equal opportunity, calibration)?
    - Are there mechanisms to detect and correct bias in production (ongoing monitoring)?
    - Does the system avoid using protected characteristics or proxies thereof in ways that produce discriminatory outcomes?

    <!-- Practitioner note: The above questions are drawn from the publicly documented scope of the UNESCO EIA's Principle 3 assessment and paraphrased from the UNESCO Recommendation on the Ethics of AI (2021, UNESDOC pf0000381137), which states that "AI actors should promote social justice and safeguard fairness and non-discrimination of any kind in compliance with international law. This implies an inclusive approach to ensuring that the benefits of AI technologies are available and accessible to all, taking into consideration the specific needs of different age groups, cultural systems, different language groups, persons with disabilities, girls and women, and disadvantaged, marginalised and vulnerable people" (paraphrased from publicly available UNESCO documentation). The EIA workbook (UNESDOC pf0000386276) contains the official verbatim procedural safeguard questions for this principle; its PDF could not be retrieved programmatically. Download the workbook at https://www.unesco.org/ethics-ai/en/eia to verify against the exact question text. -->

=== "Mitigation"

    **Mitigation prompts:**

    - Run bias audits using established fairness benchmarks (e.g., BBQ, WinoBias) before deployment
    - Document the fairness metric chosen and the rationale for that choice
    - Where bias is detected, implement targeted debiasing (data augmentation, re-weighting, post-processing) and retest
    - Establish demographic disaggregation in production monitoring dashboards
    - Engage affected communities (Stage 5) to identify discrimination harms not surfaced by automated metrics

---

## 4. Sustainability

AI systems should support environmental sustainability, minimise resource consumption, and not compromise the capacity of future generations to meet their own needs.

=== "Safeguards"

    **Safeguard questions to address:**

    - Has the environmental cost of training and operating the system been measured (energy consumption, carbon footprint, water usage)?
    - Is the model architecture proportionate to the task, avoiding unnecessary scale?
    - Are renewable energy sources used for training and inference infrastructure?
    - Has the system's impact on broader environmental decision-making been evaluated (e.g., optimising systems that may have ecological effects)?
    - Is there a commitment to reducing the system's environmental footprint over its lifecycle?

    <!-- Practitioner note: The above questions are drawn from the publicly documented scope of the UNESCO EIA's Principle 4 assessment and paraphrased from the UNESCO Recommendation on the Ethics of AI (2021, UNESDOC pf0000381137), which states that AI technologies should be assessed against their impacts on sustainability and that "potential harms to and negative impacts on the environment and ecosystems should not be ignored but instead addressed" (paraphrased from publicly available UNESCO documentation). The EIA workbook (UNESDOC pf0000386276) contains the official verbatim procedural safeguard questions for this principle; its PDF could not be retrieved programmatically. Download the workbook at https://www.unesco.org/ethics-ai/en/eia to verify against the exact question text. -->

=== "Mitigation"

    **Mitigation prompts:**

    - Measure and disclose training compute and estimated CO2 emissions using tools such as CodeCarbon or ML CO2 Impact calculator
    - Default to smaller, more efficient model variants where performance requirements allow
    - Prefer cloud providers with verified renewable energy commitments for training workloads
    - Set internal targets for reducing energy-per-inference over time and track against them
    - Include environmental impact in go/no-go deployment criteria

---

## 5. Right to Privacy and Data Protection

AI systems must respect individuals' right to privacy and comply with applicable data protection law throughout the data lifecycle.

=== "Safeguards"

    **Safeguard questions to address:**

    - Has a Data Protection Impact Assessment (DPIA) been conducted where required by applicable law?
    - Is data collection limited to what is strictly necessary for the system's purpose (data minimisation)?
    - Are privacy-enhancing technologies (PETs) such as differential privacy, federated learning, or secure multi-party computation used where appropriate?
    - Are data retention periods defined and enforced? Are deletion mechanisms in place?
    - Can individuals exercise their rights (access, rectification, erasure, restriction, portability) effectively?

    <!-- Practitioner note: The above questions are drawn from the publicly documented scope of the UNESCO EIA's Principle 5 assessment and paraphrased from the UNESCO Recommendation on the Ethics of AI (2021, UNESDOC pf0000381137), which states: "Privacy must be protected and promoted throughout the AI lifecycle. Adequate data protection frameworks should also be established" and that data collection should be governed by principles of necessity and proportionality (paraphrased from publicly available UNESCO documentation). The EIA workbook (UNESDOC pf0000386276) contains the official verbatim procedural safeguard questions for this principle; its PDF could not be retrieved programmatically. Download the workbook at https://www.unesco.org/ethics-ai/en/eia to verify against the exact question text. -->

=== "Mitigation"

    **Mitigation prompts:**

    - Conduct a DPIA and integrate its findings into this assessment
    - Implement data minimisation by design: audit training data and inference inputs for unnecessary personal data
    - Deploy PETs where processing sensitive data cannot be avoided
    - Automate data retention enforcement via deletion schedules and audit logs
    - Establish a data subject rights fulfilment process with defined response timelines

---

## 6. Human Oversight and Determination

Humans must retain meaningful oversight and control over AI systems and their consequences, especially in high-stakes decision-making contexts.

=== "Safeguards"

    **Safeguard questions to address:**

    - Is there a designated human or human team responsible for monitoring and overriding the system's outputs?
    - Are human reviewers provided with sufficient information to make meaningful oversight decisions (not just rubber-stamping)?
    - Is there a documented process for humans to override or correct the system, and is this process exercised in practice?
    - Are the circumstances under which the system can operate without human review clearly defined and limited?
    - Are there mechanisms to prevent automation bias (over-reliance on AI recommendations)?

    <!-- Practitioner note: The above questions are drawn from the publicly documented scope of the UNESCO EIA's Principle 6 assessment and paraphrased from the UNESCO Recommendation on the Ethics of AI (2021, UNESDOC pf0000381137), which states that AI actors should ensure that "the necessary oversight and control is maintained" and that human determination remains at the centre of consequential decisions (paraphrased from publicly available UNESCO documentation). The EIA workbook (UNESDOC pf0000386276) contains the official verbatim procedural safeguard questions for this principle; its PDF could not be retrieved programmatically. Download the workbook at https://www.unesco.org/ethics-ai/en/eia to verify against the exact question text. -->

=== "Mitigation"

    **Mitigation prompts:**

    - Define and document the Human-in-the-Loop (HITL) or Human-on-the-Loop (HOTL) model for this system
    - Provide human reviewers with confidence scores, uncertainty indicators, and counterfactual explanations
    - Train human reviewers specifically on automation bias and the limits of the AI system
    - Log all human overrides and use them as a quality signal for system improvement
    - Establish escalation thresholds: automatic suspension of automated decisions above a defined risk level

---

## 7. Transparency and Explainability

The existence of AI systems, their capabilities, limitations, and the basis for their decisions must be communicated clearly to affected individuals and the public.

=== "Safeguards"

    **Safeguard questions to address:**

    - Are individuals notified when they are subject to AI-driven decisions or AI-assisted processes?
    - Can the system provide explanations for its outputs in a form that is meaningful to non-technical users?
    - Is technical documentation (model cards, datasheets) published and kept up to date?
    - Are the system's limitations and known failure modes disclosed to users and affected individuals?
    - Is the system's decision logic auditable by regulators, auditors, and affected individuals (subject to trade secret protections)?

    <!-- Practitioner note: The above questions are drawn from the publicly documented scope of the UNESCO EIA's Principle 7 assessment and paraphrased from the UNESCO Recommendation on the Ethics of AI (2021, UNESDOC pf0000381137), which requires that AI actors "provide meaningful information to the public" about AI systems and that transparency and explainability be ensured throughout the lifecycle (paraphrased from publicly available UNESCO documentation). The EIA workbook (UNESDOC pf0000386276) contains the official verbatim procedural safeguard questions for this principle; its PDF could not be retrieved programmatically. Download the workbook at https://www.unesco.org/ethics-ai/en/eia to verify against the exact question text. -->

=== "Mitigation"

    **Mitigation prompts:**

    - Publish a model card and/or datasheet for datasets used
    - Implement explainability methods (e.g., SHAP, LIME, attention visualisation) and surface them in the user interface
    - Add AI disclosure notices to all user-facing interfaces where AI influences outputs
    - Establish a plain-language public summary of the system's purpose, capabilities, and limitations
    - Create an audit log accessible to regulators upon request

---

## 8. Responsibility and Accountability

Clear lines of responsibility and accountability must exist for AI systems and their outcomes, with mechanisms for redress when harm occurs.

=== "Safeguards"

    **Safeguard questions to address:**

    - Is there a named individual or team accountable for the ethical performance of this AI system?
    - Are roles and responsibilities documented for all parties in the AI supply chain (developer, deployer, integrator, user)?
    - Is there a complaints and redress mechanism for individuals harmed by the system's outputs?
    - Are suppliers and third-party model providers contractually bound to ethical standards consistent with this assessment?
    - Are accountability mechanisms enforced in practice, not merely documented?

    <!-- Practitioner note: The above questions are drawn from the publicly documented scope of the UNESCO EIA's Principle 8 assessment and paraphrased from the UNESCO Recommendation on the Ethics of AI (2021, UNESDOC pf0000381137), which states that "AI actors must be responsible and accountable for the proper functioning of AI systems and for the decisions made throughout the AI lifecycle" (paraphrased from publicly available UNESCO documentation). The EIA workbook (UNESDOC pf0000386276) contains the official verbatim procedural safeguard questions for this principle; its PDF could not be retrieved programmatically. Download the workbook at https://www.unesco.org/ethics-ai/en/eia to verify against the exact question text. -->

=== "Mitigation"

    **Mitigation prompts:**

    - Appoint a named AI Ethics Lead with authority to suspend the system
    - Publish a RACI (Responsible, Accountable, Consulted, Informed) matrix for the system's AI supply chain
    - Establish a publicly accessible complaints process with defined response and resolution timelines
    - Include AI ethics requirements in supplier contracts and conduct periodic supplier audits
    - Report accountability metrics (e.g., complaints received, overrides logged, incidents resolved) to the governance board

---

## 9. Awareness and Literacy

All stakeholders — including developers, deployers, users, and affected communities — must have sufficient understanding of AI systems to engage with them critically and responsibly.

=== "Safeguards"

    **Safeguard questions to address:**

    - Are users of the system provided with adequate training or onboarding on how the system works and its limitations?
    - Do affected communities have access to information about the system in accessible language and formats?
    - Are internal teams (including non-technical staff) educated on the ethical dimensions of AI?
    - Is there a programme to improve AI literacy among the organisation's stakeholders over time?
    - Are communications about the system's capabilities calibrated to avoid over-confidence or anthropomorphisation?

    <!-- Practitioner note: The above questions are drawn from the publicly documented scope of the UNESCO EIA's Principle 9 assessment and paraphrased from the UNESCO Recommendation on the Ethics of AI (2021, UNESDOC pf0000381137), which requires that AI actors promote "AI literacy" and that all stakeholders have access to information enabling meaningful engagement with AI systems (paraphrased from publicly available UNESCO documentation). The EIA workbook (UNESDOC pf0000386276) contains the official verbatim procedural safeguard questions for this principle; its PDF could not be retrieved programmatically. Download the workbook at https://www.unesco.org/ethics-ai/en/eia to verify against the exact question text. -->

=== "Mitigation"

    **Mitigation prompts:**

    - Develop mandatory AI ethics training for all staff who interact with or are responsible for the system
    - Produce accessible public-facing documentation in plain language, including translations where relevant
    - Partner with civil society organisations to co-develop literacy materials for affected communities
    - Include AI literacy assessments in user onboarding and track completion rates
    - Avoid marketing language that overstates the system's capabilities or autonomy

---

## 10. Multi-stakeholder and Adaptive Governance and Collaboration

AI governance must be inclusive of diverse stakeholders, adaptable to evolving technologies and societal norms, and grounded in international cooperation.

=== "Safeguards"

    **Safeguard questions to address:**

    - Does the organisation's AI governance structure include diverse internal and external stakeholders?
    - Is the EIA (and AI governance more broadly) reviewed and updated as the system and its context evolve?
    - Does the organisation participate in multi-stakeholder initiatives or standard-setting bodies relevant to its AI use?
    - Are the organisation's AI governance policies publicly available and open to external scrutiny?
    - Is there a mechanism to incorporate emerging regulatory requirements and ethical standards into governance practice?

    <!-- Practitioner note: The above questions are drawn from the publicly documented scope of the UNESCO EIA's Principle 10 assessment and paraphrased from the UNESCO Recommendation on the Ethics of AI (2021, UNESDOC pf0000381137), which requires that "multi-stakeholder approaches" and "adaptive governance" be adopted, and that governance frameworks be regularly reviewed in light of evolving technology and societal contexts (paraphrased from publicly available UNESCO documentation). The EIA workbook (UNESDOC pf0000386276) contains the official verbatim procedural safeguard questions for this principle; its PDF could not be retrieved programmatically. Download the workbook at https://www.unesco.org/ethics-ai/en/eia to verify against the exact question text. -->

=== "Mitigation"

    **Mitigation prompts:**

    - Establish a multi-stakeholder AI Ethics Board or Advisory Panel with external members
    - Schedule annual reviews of all active EIAs and update when major regulatory changes occur
    - Engage with standard-setting bodies (e.g., ISO/IEC JTC1/SC42, IEEE, NIST) and incorporate emerging standards
    - Publish the organisation's AI governance framework and EIA process publicly
    - Designate a regulatory horizon-scanning function to track AI policy developments globally

---
title: 'Part 1 — Scoping Questions'
description: UNESCO EIA Part 1 guides assessors through defining the AI system, its deployment context, data sources, affected stakeholders, and regulatory environment before substantive ethical analysis begins.
---

# Part 1 — Scoping Questions

!!! note "Part 1 of 3"
    This is the first of three parts of the UNESCO Ethical Impact Assessment. Part 1 establishes the boundaries and context for the assessment. It feeds directly into [Part 2 — Principles & Safeguards](principles.md) and [Part 3 — Impact Mapping](impact-mapping.md). Complete Part 1 before proceeding.

The scoping phase serves three functions:

1. **Defining system boundaries:** What exactly is being assessed, and what is out of scope?
2. **Understanding deployment context:** In what environments, jurisdictions, and decision-making situations will the system operate?
3. **Identifying affected stakeholders:** Who will be directly or indirectly affected by the system's outputs?

Scoping answers completed here will anchor all subsequent analysis. Be precise — vague scoping leads to gaps in the impact mapping and undetected risks.

---

## Section 1 — System Description and Intended Use

This section establishes a shared understanding of what the AI system is and what it is designed to do.

**1.1 System name and version**
Provide the official name and version number of the AI system being assessed.

**1.2 System description**
Describe the AI system in plain language. Include the AI techniques used (e.g., machine learning, large language model, computer vision, rules-based), the inputs the system receives, and the outputs it produces.

**1.3 Intended use cases**
List the primary use cases the system is designed for. Be specific about the tasks, decisions, or recommendations the system will make or support.

**1.4 Foreseeable misuse cases**
Describe ways the system could be used outside its intended purpose, including unintended or malicious uses.

**1.5 Deployment environment**
Describe where and how the system will be deployed: cloud, on-premise, embedded device, API, or a combination. Include the geographic regions of deployment.

> **TODO(source):** Insert verbatim question text from the official EIA workbook Part 1, Section 1 (UNESDOC pf0000381137) for system description questions.

---

## Section 2 — Data Sources and Data Subjects

Understanding what data the system uses — and whose data — is essential for assessing privacy, fairness, and data protection risks.

**2.1 Training data sources**
List all datasets used to train or fine-tune the system. For each dataset, note: its origin, whether it is proprietary or publicly available, and whether it contains personal data.

**2.2 Operational/inference-time data**
Describe the data the system processes at inference time (i.e., inputs to the deployed system). Note whether this data is personal, sensitive, or subject to special legal protections.

**2.3 Sensitive data categories**
Identify whether the system processes any of the following categories of sensitive personal data: racial or ethnic origin, political opinions, religious beliefs, trade union membership, health data, biometric data, genetic data, sexual orientation, criminal records.

**2.4 Data subjects**
Who are the individuals whose data is used to train and/or operate the system? Are they the same as the individuals directly affected by the system's outputs?

**2.5 Data governance**
How is data collected, stored, and used? What consent mechanisms are in place? What data retention and deletion policies apply?

> **TODO(source):** Insert verbatim question text from the official EIA workbook Part 1, Section 2 (UNESDOC pf0000381137) for data source questions.

---

## Section 3 — Affected Stakeholders and Communities

A complete stakeholder map prevents the assessment from focusing only on direct users while overlooking populations who bear the system's risks without receiving its benefits.

**3.1 Direct users**
Who will directly interact with or operate the AI system?

**3.2 Affected individuals**
Who will be subject to decisions, recommendations, or outputs produced by the system, even if they do not interact with it directly?

**3.3 Vulnerable and marginalised groups**
Are any of the affected populations particularly vulnerable due to age, disability, socioeconomic status, language, literacy, migration status, or other factors? How might the system interact differently with these groups?

**3.4 Excluded groups**
Are there groups who might be excluded from benefits the system provides (e.g., due to lack of access, digital literacy, or representation in training data)?

**3.5 Third parties and society at large**
Beyond direct users and affected individuals, what broader societal effects might the system have?

> **TODO(source):** Insert verbatim question text from the official EIA workbook Part 1, Section 3 (UNESDOC pf0000381137) for stakeholder mapping questions.

---

## Section 4 — Decision-Making Context

The ethical stakes of an AI system depend heavily on the nature and finality of the decisions it influences.

**4.1 Decision type**
Is the system:

- [ ] **Advisory** — provides information, recommendations, or scores that a human uses to make a decision
- [ ] **Automated** — makes decisions autonomously without human review
- [ ] **Hybrid** — makes some decisions autonomously and flags others for human review

**4.2 Consequentiality**
How consequential are the decisions the system influences? (e.g., low-stakes content recommendation vs. high-stakes credit scoring, medical diagnosis, or criminal justice)

**4.3 Human oversight mechanisms**
What mechanisms exist for humans to review, override, or correct the system's outputs? Are these mechanisms accessible and effective in practice?

**4.4 Appeals and redress**
Can individuals affected by the system's decisions appeal those decisions? What is the process?

> **TODO(source):** Insert verbatim question text from the official EIA workbook Part 1, Section 4 (UNESDOC pf0000381137) for decision-making context questions.

---

## Section 5 — Jurisdiction and Regulatory Context

AI systems are subject to different legal requirements depending on where they are deployed and the sectors they operate in.

**5.1 Applicable jurisdictions**
In which countries or regions will the system operate? Note any cross-border data flows.

**5.2 Sector-specific regulations**
What sector-specific regulations apply (e.g., healthcare, financial services, employment, education, law enforcement)?

**5.3 AI-specific legal obligations**
Are there AI-specific legal obligations in the applicable jurisdictions (e.g., EU AI Act classification, algorithmic accountability laws, impact assessment requirements)?

**5.4 Rights of data subjects**
What rights do individuals have regarding data used by or decisions made by this system under applicable law (e.g., GDPR rights of access, rectification, erasure, and automated decision-making rights under Article 22)?

> **TODO(source):** Insert verbatim question text from the official EIA workbook Part 1, Section 5 (UNESDOC pf0000381137) for regulatory context questions.

---

## Section 6 — Prior Assessments and Audits

Documenting prior assessments avoids duplication and surfaces whether earlier risks were adequately addressed.

**6.1 Prior ethical, privacy, or risk assessments**
Has this system (or a predecessor version) been subject to any prior ethical assessment, Data Protection Impact Assessment (DPIA), privacy impact assessment, or risk audit? If so, provide references and summarise key findings.

**6.2 Outstanding issues from prior assessments**
Are there any open issues, risks, or mitigations from prior assessments that have not yet been resolved?

**6.3 Third-party audits**
Has the system been assessed by any third-party auditor, certifier, or regulator? Provide references.

**6.4 Incident history**
Has the system (or a substantially similar predecessor) been involved in any documented incidents, harms, or near-misses? Describe and note what was done in response.

> **TODO(source):** Insert verbatim question text from the official EIA workbook Part 1, Section 6 (UNESDOC pf0000381137) for prior assessments questions.

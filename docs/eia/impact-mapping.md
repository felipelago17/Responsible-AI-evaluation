---
title: 'Part 3 — Mapping Potential Impacts'
description: UNESCO EIA Part 3 guides assessors through mapping positive and negative impacts for each of the 10 UNESCO principles, scoring likelihood and severity, and planning mitigations.
---

# Part 3 — Mapping Potential Impacts

Part 3 translates the safeguard analysis from [Part 2](principles.md) into a structured impact register. For each of the 10 UNESCO principles, assessors identify concrete positive and negative impacts, score them by likelihood and severity, and commit to specific mitigation actions.

---

## Purpose and Scope

Impact mapping serves three purposes:

1. **Surfacing:** Making implicit risks explicit and forcing systematic consideration of both benefits and harms
2. **Prioritising:** Scoring likelihood and severity enables risk-prioritised mitigation planning
3. **Accountability:** A documented impact register provides evidence of due diligence for regulators, auditors, and affected communities

**Distinction between positive and negative impacts:**

- **Positive impacts** are benefits the system creates for individuals, communities, or society (e.g., faster access to services, improved diagnostic accuracy, reduced human error)
- **Negative impacts** are harms or risks the system creates or amplifies (e.g., discriminatory outcomes, privacy violations, reduction in human agency)

Both must be documented. Over-weighting negative impacts leads to missed opportunities; ignoring them leads to avoidable harm.

---

## Scoring Guide

| Dimension | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **Likelihood** | Highly unlikely | Unlikely | Possible | Likely | Almost certain |
| **Severity** | Negligible | Minor | Moderate | Serious | Critical/irreversible |

**Risk Score** = Likelihood × Severity

| Risk Score | Priority |
|---|---|
| 1–4 | Low — monitor |
| 5–9 | Medium — mitigate |
| 10–16 | High — mitigate urgently |
| 17–25 | Critical — do not deploy without mitigation |

---

## How to Use the Impact Tables

1. For each principle, add one row per distinct impact you have identified
2. Classify each impact as Positive or Negative
3. Assign Likelihood (1–5) and Severity (1–5) scores independently before consulting colleagues
4. Calculate Risk Score (Likelihood × Severity) — note that Severity for positive impacts represents magnitude of benefit
5. For every Negative impact with Risk Score ≥ 5, a Mitigation action is **required**
6. Positive impacts with Risk Score ≥ 10 may warrant active investment to amplify them
7. Transfer all high and critical negative impacts (Risk Score ≥ 10) to the organisation's risk register

For a fillable version, see [`eia/templates/impact-mapping.md`](../../eia/templates/impact-mapping.md).

---

## Impact Tables

### Principle 1 — Proportionality and Do No Harm

| Impact | Type | Description | Likelihood (1–5) | Severity (1–5) | Risk Score | Mitigation |
|---|---|---|---|---|---|---|
| | Positive | System used only for clearly beneficial, proportionate purposes | | | | |
| | Negative | System deployed in contexts where risks outweigh benefits | | | | |
| | Negative | Harmful outputs in edge cases not covered by testing | | | | |

### Principle 2 — Safety and Security

| Impact | Type | Description | Likelihood (1–5) | Severity (1–5) | Risk Score | Mitigation |
|---|---|---|---|---|---|---|
| | Positive | Increased reliability and safety compared to manual process | | | | |
| | Negative | System failure or adversarial attack causes harm | | | | |
| | Negative | Security breach exposes sensitive model inputs or outputs | | | | |

### Principle 3 — Fairness and Non-Discrimination

| Impact | Type | Description | Likelihood (1–5) | Severity (1–5) | Risk Score | Mitigation |
|---|---|---|---|---|---|---|
| | Positive | More consistent decisions compared to human subjectivity | | | | |
| | Negative | Disparate performance across demographic groups | | | | |
| | Negative | Amplification of historical discrimination present in training data | | | | |

### Principle 4 — Sustainability

| Impact | Type | Description | Likelihood (1–5) | Severity (1–5) | Risk Score | Mitigation |
|---|---|---|---|---|---|---|
| | Positive | Efficiency gains reduce resource consumption compared to prior process | | | | |
| | Negative | High energy consumption of training and inference | | | | |
| | Negative | E-waste from hardware lifecycle for AI infrastructure | | | | |

### Principle 5 — Right to Privacy and Data Protection

| Impact | Type | Description | Likelihood (1–5) | Severity (1–5) | Risk Score | Mitigation |
|---|---|---|---|---|---|---|
| | Positive | Better data governance than prior manual process | | | | |
| | Negative | Inference of sensitive attributes from non-sensitive data | | | | |
| | Negative | Unauthorised data retention beyond stated purpose | | | | |

### Principle 6 — Human Oversight and Determination

| Impact | Type | Description | Likelihood (1–5) | Severity (1–5) | Risk Score | Mitigation |
|---|---|---|---|---|---|---|
| | Positive | Automation of routine decisions frees humans for complex judgment | | | | |
| | Negative | Automation bias leads humans to rubber-stamp AI recommendations | | | | |
| | Negative | Loss of human skills due to over-reliance on AI | | | | |

### Principle 7 — Transparency and Explainability

| Impact | Type | Description | Likelihood (1–5) | Severity (1–5) | Risk Score | Mitigation |
|---|---|---|---|---|---|---|
| | Positive | Users better understand basis for decisions than in prior process | | | | |
| | Negative | Black-box outputs prevent meaningful challenge or appeal | | | | |
| | Negative | Users unaware they are subject to AI-driven decisions | | | | |

### Principle 8 — Responsibility and Accountability

| Impact | Type | Description | Likelihood (1–5) | Severity (1–5) | Risk Score | Mitigation |
|---|---|---|---|---|---|---|
| | Positive | Clear accountability structure reduces governance gaps | | | | |
| | Negative | Responsibility gaps across AI supply chain | | | | |
| | Negative | Inadequate redress for individuals harmed by system outputs | | | | |

### Principle 9 — Awareness and Literacy

| Impact | Type | Description | Likelihood (1–5) | Severity (1–5) | Risk Score | Mitigation |
|---|---|---|---|---|---|---|
| | Positive | User training increases appropriate and safe use of the system | | | | |
| | Negative | Low AI literacy leads to inappropriate trust or misuse | | | | |
| | Negative | Affected communities unable to understand or challenge AI-driven decisions | | | | |

### Principle 10 — Multi-stakeholder and Adaptive Governance

| Impact | Type | Description | Likelihood (1–5) | Severity (1–5) | Risk Score | Mitigation |
|---|---|---|---|---|---|---|
| | Positive | Diverse governance structure improves quality of ethical decisions | | | | |
| | Negative | Governance structure fails to adapt to new capabilities or harms | | | | |
| | Negative | Marginalised stakeholders excluded from governance processes | | | | |

---

## Aggregating Scores

After completing the impact tables:

1. **Count** the number of High (10–16) and Critical (17–25) negative impacts
2. **Calculate** an overall risk posture: if any Critical negative impacts remain unmitigated, the system should not be deployed
3. **Summarise** the top 5 risks by Risk Score in the executive summary section of the EIA
4. **Map** each High/Critical risk to a named mitigation owner and target completion date
5. **Schedule** a post-deployment review at 90 days to re-score all impacts against observed production data

!!! warning "Critical Risks Require Sign-Off"
    Any impact with a Risk Score of 17–25 requires explicit sign-off from the Approver (see Stage 6) before the system may proceed to deployment. Document the rationale for proceeding despite critical risk.

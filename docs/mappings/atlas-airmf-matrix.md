# ATLAS × AI RMF Mapping Matrix

Cross-reference matrix linking each RAI control area to MITRE ATLAS v2.1 tactics/techniques and NIST AI RMF 1.0 + GenAI Profile (NIST AI 600-1) subcategories. Use this matrix to identify which framework obligations a given control satisfies, and which ATLAS techniques it mitigates.

!!! note "Sources"
    ATLAS technique identifiers follow MITRE ATLAS v2.1 (<https://atlas.mitre.org>). NIST AI RMF subcategories follow AI RMF 1.0 (NIST AI 100-1) and the GenAI Profile (NIST AI 600-1, 2024). GenAI trustworthy characteristics follow NIST AI 600-1 Appendix A.

---

## Full Mapping Matrix

| RAI Control Area | Threat Category | ATLAS Tactic | ATLAS Technique(s) | NIST AI RMF Function | NIST AI RMF Subcategory | GenAI Trustworthy Characteristic |
|---|---|---|---|---|---|---|
| **Data provenance & integrity verification** | Data Poisoning | ML Attack Staging | AML.T0020 Poison Training Data; AML.T0018 Publish Poisoned Datasets | MAP | MAP 1.1 — Context; MAP 5.1 — Data provenance | Validity & Reliability |
| **Backdoor scanning (activation clustering, Neural Cleanse, STRIP)** | Backdoor | ML Attack Staging | AML.T0019 Backdoor ML Model | MEASURE | MS 2.5 — Bias/fairness; MS 2.6 — Security | Security & Resilience |
| **ML supply chain controls (signed weights, verified hubs)** | Supply Chain Compromise | Initial Access | AML.T0040 ML Supply Chain Compromise | GOVERN | GV 1.1 — Policies; GV 1.7 — Documentation | Accountability & Transparency |
| **Adversarial input testing (AdvGLUE, PromptBench, TextFooler)** | Evasion | Defense Evasion | AML.T0015 Evade ML Model; AML.T0043 Craft Adversarial Data | MEASURE | MS 2.2 — Effectiveness; MS 2.5 — Bias | Security & Resilience |
| **Differential privacy enforcement (ε-DP guarantee)** | Membership Inference | Exfiltration | AML.T0003 Infer Training Data Membership | MEASURE | MS 2.10 — Privacy | Privacy |
| **API rate limiting & query anomaly detection** | Model Extraction | Exfiltration | AML.T0002 Create Proxy ML Model; AML.T0035 Steal ML Model | MANAGE | MG 2.2 — Risk treatment; MG 4.1 — Residual risk | Security & Resilience |
| **Prompt sanitisation & system prompt hardening** | Prompt Injection | Initial Access / Execution | AML.T0051 LLM Prompt Injection | MEASURE | MS 2.2 — Effectiveness; MS 2.6 — Security | Safety |
| **Output toxicity filtering & red-team evaluation** | Harmful Output | Impact | AML.T0048 Societal Harm | MEASURE | MS 2.5 — Bias; MS 2.6 — Security | Safety |
| **Bias auditing (StereoSet, CrowS-Pairs, WinoBias)** | Representational / Allocation Bias | Impact | AML.T0048 Societal Harm | MEASURE | MS 2.5 — Bias & fairness | Fairness & Bias Management |
| **Model card & training data documentation** | Opacity | Discovery | AML.T0013 Discover ML Model Ontology | GOVERN | GV 1.7 — Risk documentation; GV 4.1 — Transparency | Explainability & Interpretability |
| **Human oversight & escalation protocols** | Autonomy Risk | Impact | AML.T0048 Societal Harm | GOVERN | GV 1.2 — Accountability; GV 6.1 — Incidents | Human Oversight |
| **Incident response & coordinated disclosure** | Post-deploy Exploitation | Impact | AML.T0048 Societal Harm | GOVERN | GV 6.1 — Incident policies; GV 6.2 — Documentation | Accountability & Transparency |
| **Continuous drift & performance monitoring** | Capability Degradation | Persistence | AML.T0006 Active Scanning (model artifacts) | MANAGE | MG 4.1 — Residual risk; MG 4.2 — Improvements | Validity & Reliability |
| **Fairness monitoring in production** | Distribution Shift Bias | Persistence | AML.T0006 Active Scanning | MANAGE | MG 4.1 — Residual risk | Fairness & Bias Management |

---

## NIST AI RMF Function Summary

| NIST Function | Controls in This Matrix |
|---|---|
| **GOVERN** | Supply chain controls; model documentation; human oversight; incident response; fairness policies |
| **MAP** | Data provenance & integrity verification |
| **MEASURE** | Backdoor scanning; adversarial input testing; DP enforcement; prompt sanitisation; toxicity filtering; bias auditing |
| **MANAGE** | API rate limiting; extraction detection; drift monitoring; fairness monitoring in production |

---

## ATLAS Tactic Coverage

| ATLAS Tactic | Controls Addressing It |
|---|---|
| ML Attack Staging | Data provenance verification; backdoor scanning |
| Initial Access | ML supply chain controls; prompt sanitisation |
| Defense Evasion | Adversarial input testing |
| Exfiltration | Differential privacy; API rate limiting & extraction detection |
| Execution | Prompt sanitisation & system prompt hardening |
| Persistence | Continuous drift monitoring; fairness monitoring |
| Impact | Output toxicity filtering; bias auditing; human oversight; incident response |
| Discovery | Model card & training data documentation |

---

## GenAI Profile Characteristic Coverage

| GenAI Trustworthy Characteristic | Controls in This Matrix |
|---|---|
| Validity & Reliability | Data provenance verification; continuous drift monitoring |
| Safety | Prompt sanitisation; output toxicity filtering; red-team evaluation |
| Security & Resilience | Backdoor scanning; adversarial input testing; API rate limiting |
| Accountability & Transparency | Supply chain controls; incident response; model documentation |
| Explainability & Interpretability | Model card & training data documentation |
| Privacy | Differential privacy enforcement |
| Fairness & Bias Management | Bias auditing; fairness monitoring in production |
| Human Oversight | Human oversight & escalation protocols |

---

## References

- Lago, F. (2026). *Comprehensive Cybersecurity Risk Assessment Framework*. June 2026.
- MITRE (2024). *ATLAS: Adversarial Threat Landscape for Artificial-Intelligence Systems*, v2.1. <https://atlas.mitre.org>
- NIST (2023). *AI Risk Management Framework 1.0* (NIST AI 100-1). <https://doi.org/10.6028/NIST.AI.100-1>
- NIST (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1). <https://doi.org/10.6028/NIST.AI.600-1>

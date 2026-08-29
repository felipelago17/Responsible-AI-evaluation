# Deployment-Readiness Barriers as RAI Criteria

> Field evidence for this section draws on practitioner-facing reports from the energy sector (see Sources). Where figures originate from vendor-sponsored or summit surveys, they are labelled accordingly and treated as directional rather than epidemiological.

Operational research in the energy sector identifies three recurring barriers that prevent AI systems from transitioning from controlled pilots to production deployment. These barriers are not model defects — the underlying algorithms typically perform adequately in testing environments. The failure is organizational and operational. For a responsible-AI evaluation framework, each barrier maps to a distinct set of governance and management controls that should be assessed alongside technical benchmarks.

Up to 95% of AI initiatives are reported to fail to deliver measurable value at scale, with the failure attributed to operational rather than algorithmic causes [A]. This observation has direct implications for how deployment readiness is framed in AI governance: a system that passes technical benchmarks but lacks the organizational conditions for production embedding may score well on model-quality metrics while generating zero realized value.

## Barrier 1 — Data Trust Gap

### Description

Production AI environments require a level of data quality and governance that pilot environments rarely replicate. Approximately 30% of energy-sector leaders surveyed at the AI in Energy Summit 2026 cited data quality, foundations, and governance as the primary barrier to execution (self-reported, summit survey) [A]. The practical threshold reported by practitioners is approximately 85% accuracy: below that level, operational teams distrust model outputs and revert to manual processes, negating the deployment [A].

Notably, leading operators do not wait for "perfect" data before deploying. The pattern observed is deployment on "good enough" data combined with continuous data improvement in parallel — treating data quality as an ongoing operational discipline rather than a pre-deployment gate [A].

### Crosswalk

| Dimension | NIST AI RMF | EU AI Act | ISO/IEC 42001 |
|---|---|---|---|
| Data quality thresholds (≥ 85% accuracy for operational trust) | MEASURE 2.2 — AI system performance | Art. 10 — Data and data governance | Clause 8.4 — Operational planning and control |
| Data governance controls | MEASURE 2.3 — Bias and fairness testing | Art. 10(2) — Training data requirements | Clause 6.1 — Actions to address risks |
| Continuous data improvement posture | MANAGE 1.3 — Risk response | Art. 10(4) — Data quality measures | Clause 9.1 — Monitoring and measurement |
| Data as primary execution barrier (cited by ~30% of leaders) | MAP 2.1 — Impact assessment | Art. 9(2)(b) — Risk identification | Clause 6.1.2 — AI risk treatment |

**EU AI Act note (Art. 10 / Art. 15):** The ~85% accuracy threshold and continuous-improvement posture are directly relevant as practitioner-evidenced benchmarks for the data-governance obligations under Article 10 and the accuracy/robustness requirements under Article 15. These figures are self-reported survey data from 130+ energy leaders — they support the evidence trail for compliance arguments but do not constitute legal interpretation of the threshold requirements.

## Barrier 2 — Workflow Embedding

### Description

Return on investment from AI deployments appears only when the system is embedded directly into day-to-day decision-making workflows [A]. Tools that surface outputs through dashboards or analytics layers — without a direct link to the action a frontline operator must take — rarely drive behavior change and should be evaluated as low or zero realized value regardless of model quality. This is a deployment-readiness failure mode, not a model defect.

The distinction between *insight generation* and *action enablement* is operationally significant: predictive and prescriptive maintenance use cases gain traction specifically because the insight is delivered at the point where the frontline action occurs, not in a separate analytics environment [A].

### Crosswalk

| Dimension | NIST AI RMF | EU AI Act | ISO/IEC 42001 |
|---|---|---|---|
| Deployment context (embedded vs. dashboard-only) | GOVERN 1.1 — Policies for AI risk | Art. 9(2) — Risk management in context of use | Clause 4.1 — Understanding the organization |
| Action-enabling vs. insight-only distinction | MANAGE 2.2 — Human oversight implementation | Art. 14(1) — Human oversight measures | Clause 8.4 — Operational planning |
| Workflow integration monitoring | MANAGE 4.2 — Residual risk monitoring | Art. 9(6) — Ongoing risk management | Clause 9.1 — Performance monitoring |
| Deployment-context evaluation | MAP 1.5 — Deployment context documentation | Art. 13 — Transparency obligations | Clause 8.2 — AI system requirements |

**Evaluation guidance:** When assessing a deployment, distinguish between a system that generates recommendations (insight layer) and one whose output triggers a defined operator action (action-enabling layer). A system classified as "dashboard-only" should carry a deployment-readiness flag in the evaluation record regardless of benchmark scores on model quality dimensions.

## Barrier 3 — Workforce Readiness

### Description

The limiting factor for AI scale in production is workforce readiness, not technology capability [A]. Survey data from the AI in Energy Summit 2026 (130+ energy leaders, self-reported) indicates that only 17% of energy organizations consider themselves "highly prepared" — meaning AI is embedded into daily workflows for a significant proportion of staff [A]. The remaining 83% are at early or transitional stages.

The demand pattern is for AI-fluent existing staff rather than additional AI specialists. Three specific constraints are reported: skills gaps, change fatigue from successive technology programmes, and the loss of institutional knowledge when experienced staff disengage from digitised workflows [A].

### Crosswalk

| Dimension | NIST AI RMF | EU AI Act | ISO/IEC 42001 |
|---|---|---|---|
| AI fluency of operational workforce | GOVERN 4.1 — Organizational roles and responsibilities | Art. 9(2)(d) — Human oversight capability | Clause 7.2 — Competence |
| Change management and change fatigue | GOVERN 5.1 — Organizational culture | Art. 14(4) — Staff training and awareness | Clause 7.3 — Awareness |
| Institutional knowledge retention | GOVERN 4.2 — Accountability | Art. 9(2)(d) — Knowledge management | Clause 7.2 — Competence |
| Readiness baseline (17% "highly prepared") | MAP 5.2 — Capacity assessment | Art. 9 — Risk management system | Clause 6.1 — Risk assessment |

**Evaluation guidance:** A workforce-readiness assessment should be part of any deployment evaluation, scored separately from technical benchmark results. The 17% "highly prepared" baseline (self-reported, energy sector) provides a reference point: organizations reporting AI embedded into daily workflows for a majority of relevant staff represent the upper tier of current operational maturity.

## Summary Crosswalk

| Barrier | Primary NIST function | EU AI Act anchors | ISO/IEC 42001 clauses |
|---|---|---|---|
| Data trust gap | MEASURE (2.2, 2.3) + MANAGE (1.3) | Art. 10; Art. 15 | Cls. 6.1, 8.4, 9.1 |
| Workflow embedding | GOVERN (1.1) + MANAGE (2.2, 4.2) | Art. 9(2); Art. 13; Art. 14(1) | Cls. 4.1, 8.2, 8.4, 9.1 |
| Workforce readiness | GOVERN (4.1, 4.2, 5.1) | Art. 9(2)(d); Art. 14(4) | Cls. 7.2, 7.3 |

!!! note "Scope"
    These barriers and figures are drawn from operational AI deployment in the energy sector. They are included as practitioner-evidenced deployment-readiness criteria that complement the technical benchmark scores produced by this framework. ASL-level crosswalks are not affected — these sources address operational deployment, not frontier-capability evaluation.

---

## Sources

```text
[A] Oil & Gas IQ, "Why Most AI Pilots in Oil and Gas Still Fail to Scale" (8 Jun 2026);
    figures from the AI in Energy Summit 2026 Insights Report (survey of 130+ energy leaders).
[B] Utility Dive (sponsored by Paces), "How AI fits in the energy development workflow,"
    K. Baranko (22 Jun 2026).
```

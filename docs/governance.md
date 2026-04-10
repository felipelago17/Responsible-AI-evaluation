# Governance

> **Last updated:** April 2026 — reflects the February 2026 Responsible Scaling Policy (RSP) revision.
> See [Governance Mapping](governance_mapping.md) for detailed mapping of evaluation dimensions to
> NIST AI RMF, EU AI Act, and RSP ASL levels.

This page describes the governance policies for the Open LLM Safety Evaluation framework, covering data handling, result versioning, contribution standards, and responsible use.

## Data Handling

### Dataset Licensing

All benchmark datasets used in this framework are governed by their original licenses. Before using a dataset in a new context, review its license to confirm permitted use cases. Dataset licenses are documented in each benchmark configuration file under `benchmarks/`.

### No Personal Data

Benchmark datasets should not contain personal data (PII) in any form. If a dataset is found to contain PII, it must be reported immediately and will be removed from the framework pending review.

### Dataset Versioning

Datasets are pinned to specific versions (commit SHA or release tag) to ensure reproducibility. Updates to dataset versions are treated as breaking changes and require a framework minor version bump.

## Result Versioning

### Versioning Scheme

The framework uses semantic versioning (`MAJOR.MINOR.PATCH`):

- **MAJOR** — incompatible changes to the evaluation protocol that break score comparability
- **MINOR** — new benchmarks or dataset version updates
- **PATCH** — bug fixes that do not affect scores

### Result Archiving

Evaluation results should be archived with the full provenance metadata (framework version, dataset version, model identifier, timestamp) to support longitudinal comparisons and auditing.

### Score Comparability

Scores are only directly comparable when produced by the same framework version. When upgrading the framework, re-evaluate all models of interest to obtain comparable scores.

## Contribution Standards

### Adding New Benchmarks

Benchmark contributions must include:

1. A benchmark adapter in `benchmarks/` with a pinned dataset version
2. Metric definitions and a primary metric designation
3. Documentation in `docs/benchmarks/`
4. At least one example result in `results/examples/`

### Code Review Requirements

All contributions undergo peer review with attention to:

- Correctness of metric implementation
- Absence of data leakage between prompt construction and evaluation
- Compliance with dataset license terms
- Documentation completeness

### Disclosure Policy

Known issues, metric errors, or reproducibility failures should be disclosed via GitHub Issues with the `governance` label. Critical issues affecting score validity will be communicated via the project changelog.

## Responsible Scaling Policy (RSP) Alignment

### Severity Tiers

This framework recognises the following severity tiers, aligned with the Anthropic RSP (February 2026 revision).  A new tier above "high" has been introduced:

| Tier | Description |
|---|---|
| Low | Minimal capability concern; within normal deployment envelope |
| Medium | Elevated concern; mitigations recommended before deployment |
| High | Significant capability risk; mitigations required |
| **ASL-3 risk** | **Above-threshold capability; mandatory safety review before deployment or further training** |

### ASL-2 / ASL-3 Threshold Mapping

Benchmark scores are mapped to ASL thresholds as follows (see [Governance Mapping](governance_mapping.md) for the full table):

- Scores below the ASL-2 boundary indicate compliance with current RSP operating constraints.
- Scores in the elevated-concern range trigger enhanced monitoring obligations.
- Scores at or above the ASL-3 trigger require a mandatory pause and safety review before the model is deployed, scaled, or used for further training.

### Dual-Condition ASL-3 Trigger

An ASL-3 designation requires **both** conditions to be met simultaneously:

1. **Frontier race leadership** — the model is at or near the current capability frontier among deployed systems.
2. **Material catastrophic risk** — the model demonstrates capabilities that create a materially increased risk of catastrophic harm (e.g., CBRN uplift, autonomous cyberoffense at nation-state scale, or self-replication across safety boundaries).

Meeting only one condition is insufficient to trigger ASL-3 obligations.  Both conditions must be documented and independently reviewed.

## Responsible Use

### Intended Use

This framework is intended for:

- Research into AI safety measurement methodology
- Pre-deployment safety screening of LLMs
- Longitudinal tracking of model safety across versions
- Supporting AI governance and compliance programmes

### Misuse Prohibition

This framework must not be used to:

- Identify attack vectors for malicious exploitation of AI systems
- Circumvent safety measures in production systems
- Produce misleading safety certifications or compliance claims

### Limitations Disclosure

Users who publish or share evaluation results produced by this framework must clearly disclose the framework version, dataset versions, and the [known limitations](limitations.md) relevant to their use case.

## Contact

For governance questions, dataset licensing issues, or responsible use inquiries, open an issue on the project repository with the `governance` label.

# Governance

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

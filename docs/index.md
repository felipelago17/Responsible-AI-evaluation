# Open LLM Safety Evaluation

Welcome to the **Open LLM Safety Evaluation** framework — an open-source toolkit for stress-testing AI systems across five critical safety dimensions:

- **Bias** — detecting and quantifying demographic and representational bias
- **Toxicity** — measuring harmful, offensive, or inappropriate outputs
- **Truthfulness** — assessing factual accuracy and hallucination rates
- **Robustness** — evaluating stability against adversarial and edge-case inputs
- **Red Teaming** — structured adversarial probing for high-risk failure modes

## Why This Framework?

Modern large language models (LLMs) are being deployed in high-stakes domains including healthcare, finance, education, and public services. Responsible deployment requires rigorous, reproducible safety evaluation grounded in academic research and real-world governance standards.

This framework is built for:

- **Researchers** seeking reproducible benchmarks and transparent methodology
- **Developers** integrating safety checks into CI/CD pipelines
- **Risk & Compliance teams** requiring structured, auditable evaluation reports
- **Policy makers** needing evidence-based assessments of AI system risk

## Getting Started

Browse the documentation sections to learn more:

- [Methodology](methodology.md) — how evaluations are designed and conducted
- [Benchmarks](benchmarks/bias.md) — dataset adapters and evaluation configs
- [Scoring](scoring.md) — metrics, aggregation, and reporting
- [Limitations](limitations.md) — known gaps and scope boundaries
- [Governance](governance.md) — data handling, versioning, and responsible use

## Quick Links

| Section | Description |
|---|---|
| [Bias](benchmarks/bias.md) | Stereotype, representation, and allocation bias metrics |
| [Toxicity](benchmarks/toxicity.md) | Hate speech, harassment, and harmful content detection |
| [Truthfulness](benchmarks/truthfulness.md) | Factual accuracy, hallucination, and calibration |
| [Robustness](benchmarks/robustness.md) | Adversarial inputs, prompt injection, and distributional shift |
| [Red Teaming](benchmarks/red-teaming.md) | Structured adversarial probing and jailbreak resistance |

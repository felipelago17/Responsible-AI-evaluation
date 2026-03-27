# Evaluation Methodology

## Overview

This project uses benchmark-based evaluation to measure the safety properties of large language models. Benchmarks provide structured, repeatable test conditions that enable systematic comparison across models and over time. This document describes how benchmarks are selected, how evaluations are conducted, and how results should be interpreted.

---

## Why Benchmark-Based Evaluation

Benchmark evaluation offers several properties that are well-suited to reproducible safety assessment:

- **Repeatability**: The same test suite can be run across different models or different versions of the same model, producing directly comparable results.
- **Transparency**: Published datasets allow independent parties to inspect, critique, and re-run evaluations.
- **Scalability**: Automated benchmarks can cover thousands of test cases, providing broader coverage than manual review alone.
- **Version control**: Benchmarks can be pinned to specific dataset versions, enabling longitudinal comparisons.

Benchmark evaluation is not a substitute for qualitative expert review, red teaming, or deployment-specific testing. It is one input among several that together constitute a responsible evaluation posture.

---

## Dataset Selection Criteria

Benchmarks are included in this project only when they meet all of the following criteria:

1. **Publicly available**: The dataset must be openly accessible without restrictive licensing that would prevent reproduction.
2. **Peer-reviewed or community-validated**: The benchmark must have been published in a peer-reviewed venue or subjected to significant community scrutiny (e.g., widely cited workshops, shared tasks).
3. **Reproducible construction**: The dataset construction methodology must be documented well enough to understand what the benchmark measures and how the data was collected or generated.
4. **Relevance to safety dimensions**: The benchmark must address at least one of the five core risk dimensions: bias, toxicity, truthfulness, robustness, or adversarial resilience.

Benchmarks are reviewed periodically. Datasets that become outdated, are found to contain significant construction flaws, or cease to reflect real-world conditions may be deprecated or replaced. See [Governance](governance.md) for the process.

---

## What Benchmarks Can Capture

When used carefully, benchmarks can provide evidence about:

- **Aggregate tendencies**: Whether a model systematically produces biased, toxic, or false outputs across a large and diverse test set
- **Comparative standing**: How a model performs relative to other models on the same benchmark, under identical conditions
- **Regression detection**: Whether safety properties change between model versions or fine-tuning runs
- **Specific failure modes**: Structured benchmarks can highlight specific input patterns or demographic categories where a model underperforms

---

## What Benchmarks Cannot Capture

Benchmark results have inherent limitations that users must understand before drawing conclusions:

- **Real-world incidence rates**: A benchmark score does not translate directly to the frequency of harmful outputs in production use.
- **Novel attack surfaces**: Benchmarks test known patterns. Adversarial actors may discover new elicitation techniques not covered by current test sets.
- **Context-dependence**: A model may perform well on a benchmark but behave differently when deployed in a specific domain, language, or user population.
- **Intent and harm severity**: Automated benchmarks cannot fully capture the severity or real-world impact of a harmful output. A toxicity classifier marking a response as "low toxicity" does not mean the response is benign in all contexts.
- **Instruction-following and RLHF effects**: Fine-tuned and instruction-following models may respond differently to benchmark prompts than to natural user queries, inflating or deflating observed scores.

---

## Evaluation Protocol

All evaluations in this project follow a documented protocol to ensure consistency:

1. **Environment specification**: Python version, dependency versions, and hardware are recorded for each run.
2. **Dataset pinning**: Specific dataset versions or commit hashes are used and recorded.
3. **Prompt formatting**: For instruction-tuned models, the system prompt and formatting are standardised per model family according to publicly available documentation.
4. **Sampling parameters**: Temperature and other decoding parameters are set to reproducible values (typically temperature = 0 for deterministic tasks, or a fixed seed where stochastic sampling is required).
5. **Metric reporting**: Primary metrics are reported as defined by the benchmark's original authors. Secondary metrics may be included where they add interpretive value.

---

## Interpreting Results

Benchmark scores in this project should be treated as **relative, contextual indicators**, not absolute safety verdicts.

- A higher score on a safety benchmark generally indicates fewer observed failures, but does not certify that the model is safe.
- A lower score indicates more frequent failures on that benchmark's specific test set, which warrants further investigation.
- Scores should always be interpreted alongside the [Limitations](limitations.md) documented for each benchmark.
- Comparisons across benchmarks with different scales, metrics, or construction methodologies require caution.

For guidance on how individual scores are reported and aggregated, see [Scoring](scoring.md).

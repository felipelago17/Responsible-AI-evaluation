# Truthfulness Evaluation

This benchmark evaluates the factual accuracy of LLM outputs and measures the tendency to generate plausible-sounding but false statements (hallucinations).

## Overview

| Property | Value |
|---|---|
| Primary Metric | Accuracy (% true answers) |
| Dataset | TruthfulQA + HaluEval |
| Dataset Version | Pinned (see `benchmarks/truthfulness/config.yaml`) |
| Evaluation Type | Classification + Generation |

## Evaluation Dimensions

### Factual Accuracy

Measures whether the model's stated claims are factually correct. Evaluated using TruthfulQA, which contains questions that humans often answer incorrectly due to misconceptions, and HaluEval, which evaluates hallucination in summarization, question answering, and dialogue.

### Calibration

Measures whether the model's expressed confidence aligns with its actual accuracy. A well-calibrated model should be uncertain when it is likely to be wrong and confident when it is likely to be correct.

### Hallucination Rate

Measures the fraction of generated claims that are factually unsupported or contradicted by a reference source.

### Source Attribution

Measures whether the model correctly attributes claims to sources when asked, and avoids fabricating citations.

## Evaluation Protocol

### TruthfulQA

The model is evaluated on 817 questions spanning 38 categories (law, health, finance, politics, etc.). Questions are designed to tempt models toward common misconceptions.

- **MC1**: Single-answer multiple choice accuracy
- **MC2**: Multi-answer multiple choice (normalised probability across true answers)
- **Generation**: Open-ended generation judged by a fine-tuned truth/information classifier

### HaluEval

The model is provided with source documents and evaluated on whether its summaries, answers, and dialogue responses introduce hallucinated content not present in the source.

## Metrics

| Metric | Description | Target |
|---|---|---|
| TruthfulQA MC1 | Single-answer accuracy | Higher is better |
| TruthfulQA MC2 | Multi-answer accuracy | Higher is better |
| Hallucination Rate | Fraction of generations with hallucinated content | Lower is better |
| ECE | Expected Calibration Error | Lower is better |
| Accuracy (primary) | Overall fraction of true responses | Higher is better |

## References

- Lin et al. (2022) — TruthfulQA
- Li et al. (2023) — HaluEval
- Guo et al. (2017) — Calibration of Modern Neural Networks

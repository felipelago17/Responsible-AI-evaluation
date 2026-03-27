# Red Teaming Evaluation

This benchmark uses structured adversarial probing to uncover high-risk failure modes in LLMs, including jailbreaks, misuse facilitation, and dangerous capability elicitation.

## Overview

| Property | Value |
|---|---|
| Primary Metric | Refusal Rate (higher is better) |
| Dataset | HarmBench + Custom Red-Team Suite |
| Dataset Version | Pinned (see `benchmarks/red-teaming/config.yaml`) |
| Evaluation Type | Generation |

## Red Teaming Dimensions

### Jailbreak Resistance

Measures the model's resistance to jailbreak prompts that attempt to bypass safety guardrails. Covers a broad taxonomy of jailbreak strategies including role-play, hypothetical framing, encoding, and multi-step manipulation.

### Harmful Instruction Following

Measures whether the model complies with requests to provide instructions for harmful activities including violence, self-harm, illegal activities, and weapons development.

### Misuse Facilitation

Measures whether the model assists in creating content that could facilitate real-world harm, including disinformation, targeted harassment, fraud, and social engineering.

### Dangerous Capability Elicitation

Measures whether the model can be prompted to demonstrate dangerous capabilities such as cyberoffense assistance, CBRN-relevant information, or manipulation techniques.

### Safe Refusal Quality

In addition to measuring whether refusals occur, this dimension evaluates the quality of refusals — whether they are helpful, non-judgmental, and provide appropriate guidance to the user.

## Evaluation Protocol

### HarmBench

The model is evaluated on HarmBench's standard behaviours dataset covering 400 harmful behaviours across 7 functional categories. Both direct requests and optimised adversarial attacks (GCG, AutoDAN, etc.) are used.

### Custom Red-Team Suite

A curated set of 200 hand-crafted adversarial prompts targeting known failure modes of aligned LLMs, developed in consultation with safety researchers. This suite is updated quarterly.

### Attack Coverage

| Attack Type | Description |
|---|---|
| Direct request | Plaintext harmful instruction |
| Role-play | Harmful instruction framed as fiction or role-play |
| Hypothetical | Harmful instruction framed as hypothetical or academic |
| Jailbreak template | Known jailbreak prompt templates (DAN, etc.) |
| Optimised adversarial | GCG and AutoDAN suffix attacks |
| Multi-turn | Harmful intent revealed across multiple conversation turns |

## Metrics

| Metric | Description | Target |
|---|---|---|
| Refusal Rate (primary) | Fraction of harmful prompts correctly refused | Higher is better |
| Attack Success Rate | Fraction of attacks that elicit harmful outputs | Lower is better |
| False Refusal Rate | Fraction of benign prompts incorrectly refused | Lower is better |
| Refusal Quality Score | Human-rated quality of refusal responses | Higher is better |

## Safety Notes

The red-teaming benchmark datasets contain harmful content by design. Access to the full dataset is restricted. Evaluation results from this benchmark should be treated as sensitive and shared only with appropriate stakeholders under responsible disclosure norms.

## References

- Mazeika et al. (2024) — HarmBench
- Ganguli et al. (2022) — Red Teaming Language Models
- Zou et al. (2023) — Universal and Transferable Adversarial Attacks (GCG)
- Liu et al. (2023) — AutoDAN

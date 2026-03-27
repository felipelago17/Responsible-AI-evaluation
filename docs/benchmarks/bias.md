# Bias Evaluation

This benchmark evaluates demographic and representational bias in LLM outputs across multiple bias types and demographic dimensions.

## Overview

| Property | Value |
|---|---|
| Primary Metric | Macro F1 (bias classification) |
| Dataset | WinoBias + StereoSet + CrowS-Pairs |
| Dataset Version | Pinned (see `benchmarks/bias/config.yaml`) |
| Evaluation Type | Classification + Generation |

## Bias Types Covered

### Stereotyping Bias

Measures the tendency of a model to associate demographic groups with stereotypical roles, traits, or characteristics. Evaluated using StereoSet (intrasentence and intersentence) and CrowS-Pairs.

### Allocation Bias

Measures differential treatment in allocation decisions (e.g., hiring, lending, healthcare recommendations) when the only varying factor is a demographic attribute. Uses counterfactual prompts that differ only in the demographic variable.

### Representational Bias

Measures whether a model systematically underrepresents or misrepresents certain groups in open-ended generation tasks.

### Co-reference Bias

Measures gender bias in pronoun resolution using the WinoBias dataset.

## Demographic Dimensions

- Gender (binary and non-binary)
- Race and ethnicity
- Age
- Religion
- Nationality
- Socioeconomic status
- Sexual orientation
- Disability status

## Evaluation Protocol

1. **StereoSet** — the model scores stereotypical vs. anti-stereotypical sentence continuations. The Language Modelling Score (LMS) measures coherence; the Stereotype Score (SS) measures bias.
2. **CrowS-Pairs** — the model is presented with minimally differing sentence pairs; preference for the stereotypical sentence is measured.
3. **Counterfactual Allocation** — the model receives allocation prompts with demographic attributes swapped; response consistency is measured.

## Metrics

| Metric | Description | Target |
|---|---|---|
| ICAT Score | Composite of LMS and SS from StereoSet | Higher is better |
| CrowS-Pairs Score | Fraction preferring stereotypical sentence | Lower is better |
| Counterfactual Consistency | Agreement rate across demographic variants | Higher is better |
| Macro F1 (primary) | F1 across all bias categories | Higher is better |

## References

- Nadeem et al. (2021) — StereoSet
- Nangia et al. (2020) — CrowS-Pairs
- Zhao et al. (2018) — WinoBias

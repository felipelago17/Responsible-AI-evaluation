# Toxicity Benchmarks

## Harmful and Toxic Language Risks in Generative Models

Generative language models can produce content that is harmful, offensive, or hateful, either in direct response to user prompts or spontaneously during open-ended generation. Evaluating toxicity risk is essential because:

- Models may produce harmful content even when not explicitly instructed to do so.
- Toxic outputs can cause real harm to users, particularly members of marginalised groups.
- Toxicity can be explicit (clearly offensive language) or implicit (coded language, microaggressions, or harmful framing that does not trigger surface-level filters).
- Toxicity is context-dependent: the same text may be harmful in one setting and acceptable in another.

---

## Benchmarks Used

### CrowS-Pairs (Toxicity Dimension)

**CrowS-Pairs** (Nangia et al., 2020) is used in this project both for bias evaluation and for toxicity assessment. Many of its stereotypical sentence pairs are inherently harmful in nature, encoding derogatory associations about demographic groups. By measuring a model's preference for stereotypical versus counter-stereotypical completions, CrowS-Pairs provides a signal about the model's implicit endorsement of harmful group-level associations.

When used for toxicity evaluation, the focus is on the subset of examples that express or encode explicitly demeaning, derogatory, or harmful content, rather than subtler stereotyping.

### RealToxicityPrompts

**RealToxicityPrompts** (Gehman et al., 2020) is a dataset of 100,000 naturally occurring sentence prefixes drawn from the web, paired with toxicity scores from the Perspective API classifier. Each prompt is a partial sentence that a model is asked to complete; the resulting completion is then scored for toxicity.

RealToxicityPrompts is designed to measure the probability that a model generates toxic content during open-ended generation, rather than in response to adversarial prompts. The dataset includes both prompts that are themselves non-toxic and prompts that already contain some degree of toxicity, enabling analysis of how toxic context influences model behaviour.

**Why RealToxicityPrompts**: It is one of the most widely used toxicity evaluation datasets, grounded in naturalistic text, and supports probabilistic analysis of toxicity rates across a large prompt corpus. Its construction is documented and the dataset is publicly available.

---

## Explicit vs. Implicit Toxicity

A key distinction in toxicity evaluation is between **explicit** and **implicit** toxicity:

- **Explicit toxicity**: Content that overtly uses slurs, threats, or clearly derogatory language. Automated classifiers tend to perform better on this category because the surface features are more predictable.
- **Implicit toxicity**: Content that encodes harm through framing, implication, coded language, or subtext. Examples include subtle derogatory associations, harmful stereotypes expressed in neutral-sounding language, or microaggressions. Automated classifiers have substantially lower accuracy on implicit toxicity.

This project reports toxicity scores using automated classifiers, which are better suited to detecting explicit toxicity. Implicit toxicity detection requires human review and is not fully captured by benchmark scores alone.

---

## Why Toxicity Evaluation Is Probabilistic, Not Binary

Toxicity is not a binary property of a model. A model does not either "produce toxic content" or "not produce toxic content" in all circumstances. Instead, toxicity should be understood as a **probability distribution over outputs**:

- The same prompt may generate toxic or non-toxic completions across multiple runs, depending on sampling randomness.
- Toxicity rates vary with prompt content, context, and phrasing.
- A model may have a very low overall toxicity rate but a substantially higher rate for specific demographic groups or topics, a pattern that aggregate scores can obscure.

For this reason, RealToxicityPrompts reports expected toxicity probability across many prompts and sampling runs, rather than a single pass/fail verdict. Results should be interpreted as probabilistic estimates of generation risk, not deterministic predictions.

---

## Limitations

- **Classifier dependence**: Toxicity scores rely on the Perspective API or similar classifiers, which are known to have higher false positive rates for text involving certain dialects, communities, or topics. Classifier errors propagate into benchmark scores.
- **English-language and cultural specificity**: Most toxicity benchmarks are constructed from English-language web text and reflect US and Western European norms. What constitutes harmful language varies across languages, cultures, and communities.
- **Context collapse**: Benchmark prompts are typically evaluated without conversational context. Toxicity in multi-turn conversation, role-playing scenarios, or domain-specific contexts may not be captured.
- **Evolving language**: Slurs, coded language, and harmful terminology evolve. Static datasets may not reflect new forms of toxicity.
- **Adversarial elicitation**: RealToxicityPrompts uses naturalistic prompts, not adversarial ones. Models may produce low toxicity scores on this benchmark while remaining susceptible to targeted adversarial attacks. See [Robustness](robustness.md) and [Red Teaming](red-teaming.md) for adversarial evaluation.

For broader context on evaluation limitations, see [Limitations](../limitations.md).

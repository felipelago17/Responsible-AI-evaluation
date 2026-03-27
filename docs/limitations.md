# Limitations

This document describes the known limitations of this project and its evaluation methodology. Acknowledging these limitations is essential for responsible use of the results.

---

## Limits of Benchmark-Driven Evaluation

Benchmark evaluation measures model behaviour on a fixed, predefined test set. This has several structural consequences:

- **Coverage is bounded**: No benchmark can cover all possible inputs, contexts, or failure modes. A model that scores well on available benchmarks may still exhibit harmful behaviour in uncovered scenarios.
- **Goodhart's Law applies**: When a model is trained or fine-tuned with knowledge of specific benchmarks, scores on those benchmarks may overestimate real-world safety. Benchmark saturation — where top models cluster near ceiling performance — can obscure meaningful differences in safety behaviour.
- **Automation introduces errors**: Automated evaluators (classifiers, answer-matching heuristics) are imperfect. False positives and false negatives in scoring are an unavoidable feature of automated evaluation at scale.
- **Static tests, dynamic models**: Benchmarks are fixed; models are continuously updated. Results reflect a model at a specific point in time and may not remain accurate after fine-tuning, alignment updates, or system prompt changes.

---

## Dataset Bias and Cultural Limitations

All datasets used in this project reflect the populations, cultural norms, and languages present in their construction:

- **Demographic skew**: Many widely-used safety benchmarks are constructed primarily from English-language data and reflect North American or Western European cultural contexts. Bias and toxicity findings may not generalise to other languages, regions, or communities.
- **Annotator perspective**: Human-labelled datasets encode the perspectives and blind spots of their annotators. Categories like "toxicity" or "bias" are culturally contingent and may be operationalised differently across datasets.
- **Intersectionality**: Most benchmarks assess single demographic axes (e.g., gender or race) independently. Intersectional effects — where multiple identities interact — are rarely tested.
- **Historical data**: Datasets drawn from historical text inherit historical patterns of discrimination and harm that may no longer reflect contemporary norms or that may underrepresent groups that were marginalised in historical data sources.

---

## Prompt Sensitivity and Model Stochasticity

LLM outputs are sensitive to small changes in input formatting, wording, and context:

- **Prompt format effects**: The same semantic query expressed in different syntactic forms can elicit meaningfully different model responses. Benchmark scores reflect the specific prompt formulations used, not the full range of ways a user might phrase an equivalent request.
- **System prompt dependence**: Instruction-tuned models are highly sensitive to system prompts. A model evaluated without a system prompt may behave differently when deployed with one, and vice versa.
- **Stochastic sampling**: When temperature > 0 or top-p sampling is used, model outputs are non-deterministic. Scores on probabilistic benchmarks carry variance that is not always quantified or reported.
- **Context window effects**: Long-context behaviour may differ from short-context benchmark conditions. Results from standard-length benchmarks may not reflect model behaviour on long documents or multi-turn conversations.

---

## Benchmark Construction Limitations

Each benchmark used in this project has specific known limitations, documented on the relevant benchmark pages:

- [Bias Benchmarks — Limitations](benchmarks/bias.md#known-limitations-and-failure-modes)
- [Toxicity Benchmarks — Limitations](benchmarks/toxicity.md#limitations)
- [Truthfulness Benchmarks — Limitations](benchmarks/truthfulness.md#limitations-and-appropriate-use)
- [Robustness Benchmarks — Limitations](benchmarks/robustness.md#limitations)
- [Red Teaming — Limitations](benchmarks/red-teaming.md#limitations)

---

## What This Project Cannot Claim or Guarantee

This project does not and cannot:

- **Certify** that any model is safe, ethical, aligned, or fit for any specific purpose
- **Guarantee** that a model will not produce harmful outputs in production environments
- **Predict** how a model will behave with real users, in specific domains, or under deployment pressures
- **Assess** the full range of social, legal, political, or contextual harms that a model may contribute to
- **Replace** domain-specific evaluation, legal review, human expert testing, or regulatory compliance assessment
- **Remain current** indefinitely — model capabilities and safety properties change; results should be treated as time-stamped snapshots

Users who rely on these results for deployment decisions, procurement, or policy should conduct their own supplemental evaluation appropriate to their specific context and risk tolerance.

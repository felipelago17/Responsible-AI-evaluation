# Scoring

## How Individual Benchmark Results Are Reported

Each benchmark evaluation produces one or more metric scores as defined by the benchmark's original authors. Results are reported at the following levels:

- **Primary metric**: The headline metric as defined by the benchmark authors (e.g., accuracy, toxicity probability, stereotype score). This is always reported.
- **Per-category breakdown**: Where the benchmark supports subcategory analysis (e.g., CrowS-Pairs by demographic dimension, TruthfulQA by domain), per-category scores are reported alongside the overall metric.
- **Evaluation metadata**: Each result is accompanied by the model identifier and version, dataset version, evaluation date, and inference configuration (e.g., temperature, prompt format). This metadata is required to interpret scores correctly.

Results are presented in tabular form in the repository, with links to the underlying data files and the evaluation code used to produce them.

---

## Why Aggregate Scores Are Treated Cautiously

This project does not produce a single aggregate "safety score" that collapses all benchmark results into one number. This is an intentional design decision based on the following considerations:

- **Incommensurability**: Different benchmarks measure different properties on different scales using different metrics. Combining accuracy on a commonsense reasoning task with a toxicity probability estimate requires arbitrary weighting decisions that have no principled basis.
- **Masking**: Aggregate scores can obscure serious failures in specific dimensions. A model with strong truthfulness and robustness scores but poor toxicity performance would receive an aggregate score that misrepresents its safety profile.
- **False precision**: A single number implies a precision and completeness of assessment that benchmark evaluation cannot support. It invites misinterpretation as a comprehensive safety verdict.
- **Gaming risk**: Models or systems optimised to maximise an aggregate score may trade off important safety properties in uncovered dimensions.

Where summary comparisons are provided, they are presented as profiles across individual dimensions, not collapsed into a single value.

---

## Why Rankings Are Contextual, Not Absolute

Rankings derived from benchmark scores should be interpreted as conditional on the benchmarks used, the models tested, and the evaluation conditions. Rankings are not statements of absolute safety:

- **Benchmark coverage is incomplete**: A model that ranks first on all current benchmarks may still have serious vulnerabilities in dimensions not covered.
- **Rankings reflect evaluation conditions**: Different system prompts, deployment configurations, or use cases can substantially change relative performance. A model that ranks well under one configuration may rank differently under another.
- **Rankings are time-stamped**: Model safety properties change with updates and fine-tuning. Rankings should include the date of evaluation to remain interpretable.
- **Ranking does not imply adequacy**: A model may rank first on a benchmark while still exhibiting an unacceptably high rate of harmful outputs in absolute terms. Higher rank means fewer observed failures relative to other evaluated models, not that the model is safe.

---

## How Score Comparisons Should and Should Not Be Used

### Appropriate uses of score comparisons

- Comparing two versions of the same model to detect safety regressions after a fine-tuning or alignment update
- Comparing models from the same family or provider under consistent evaluation conditions
- Identifying which specific benchmark dimensions show the largest performance gaps between models
- Tracking improvement over time on a specific benchmark for a specific model under fixed evaluation conditions

### Inappropriate uses of score comparisons

- Declaring a model "safe" or "unsafe" based on benchmark scores alone
- Using scores as a substitute for domain-specific evaluation, expert review, or deployment testing
- Comparing models evaluated under different conditions, at different times, or with different prompt formats without accounting for those differences
- Using scores from this project as evidence of regulatory compliance, contractual safety guarantees, or liability limitation
- Ranking models for general-purpose use cases from evaluation results obtained under specific conditions

---

## Relationship to Limitations

Scores should always be read in conjunction with the documented limitations of each benchmark. A high score on a benchmark with known coverage gaps provides less assurance than a high score on a benchmark with broad, validated coverage. See [Limitations](limitations.md) and individual benchmark pages for the specific limitations relevant to each metric.

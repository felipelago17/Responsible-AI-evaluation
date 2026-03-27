# Limitations

This page documents the known limitations of the Open LLM Safety Evaluation framework. Being explicit about scope boundaries is a core governance requirement.

## Scope Limitations

### Language Coverage

The current benchmark suite is primarily English-language. Safety properties do not transfer uniformly across languages; a model that scores well in English may behave differently in other languages. Multilingual evaluation support is planned for a future release.

### Modality Coverage

This framework evaluates text-only models. Multimodal models (vision-language, audio-language) require additional benchmark dimensions not currently implemented.

### Domain Coverage

Benchmarks are designed for general-purpose LLMs. Specialized domain models (medical, legal, financial) may require domain-specific benchmark adaptations that are not included in the default configuration.

## Metric Limitations

### Classifier Dependence

Toxicity and bias metrics rely on off-the-shelf classifier models (e.g., Perspective API, hate speech classifiers). These classifiers have their own error rates, biases, and coverage gaps. Scores should be interpreted in light of the referee classifier's own limitations.

### Ground Truth Quality

Benchmark datasets were constructed by human annotators and may contain labeling errors, cultural biases, or outdated norms. Dataset documentation should be reviewed before using results for high-stakes decisions.

### Adversarial Arms Race

Robustness and red-teaming benchmarks reflect known attack strategies at the time of dataset creation. Novel attack strategies not represented in the benchmark may succeed against models that score well.

## Evaluation Setup Limitations

### Inference Parameters

Results are sensitive to inference parameters such as temperature, sampling strategy, and system prompt. The framework fixes these parameters for comparability, but production deployments may use different settings that affect safety properties.

### Context Window Effects

Some safety properties emerge only in long-context interactions. Current benchmarks use single-turn or short multi-turn evaluations and may not capture safety failures that arise in extended conversations.

### Fine-tuning and RLHF

Post-training alignment procedures (RLHF, DPO, etc.) can significantly change safety properties. Evaluation results for a base model do not predict results for instruction-tuned or aligned variants.

## What This Framework Does Not Replace

- **Red team exercises** with domain experts and affected communities
- **User research** with real end users from at-risk populations
- **Legal and regulatory compliance review**
- **Ongoing monitoring** in production environments
- **Incident response** procedures

These evaluations are a complement to, not a substitute for, a comprehensive AI safety and governance programme.

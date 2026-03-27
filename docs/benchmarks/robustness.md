# Robustness Benchmarks

## Robustness as Resistance to Adversarial or Malformed Inputs

In AI safety evaluation, **robustness** refers to a model's ability to maintain reliable, safe behaviour when presented with inputs that deviate from typical usage patterns. These deviations may be:

- **Adversarial**: Deliberately crafted to exploit weaknesses in the model's behaviour, safety filters, or reasoning
- **Out-of-distribution**: Inputs from contexts, languages, or phrasings not well represented in training
- **Malformed**: Inputs that contain errors, unusual formatting, encoding anomalies, or prompt injection attempts
- **Boundary-probing**: Inputs that test the edges of a model's guidelines or constraints

Robustness failures are particularly concerning in deployment because they can expose safety failures that are invisible under normal evaluation conditions. A model may perform well on standard benchmarks while remaining highly susceptible to targeted manipulation.

---

## Jailbreak and Adversarial Prompt Risks

A **jailbreak** is an adversarial prompt specifically designed to cause a model to bypass its safety guidelines, content policies, or alignment training and produce outputs it would otherwise refuse to generate.

Jailbreak risks include:

- **Instruction overrides**: Prompts that attempt to override system instructions or "reset" the model's persona
- **Role-playing exploits**: Prompts that use fictional framing, hypothetical scenarios, or role-playing to elicit otherwise-refused content
- **Encoding attacks**: Inputs that use unusual character encoding, languages, or character substitutions to evade keyword-based safety filters
- **Multi-step manipulation**: Sequences of prompts that gradually escalate toward policy-violating content, with each individual step appearing benign
- **Prompt injection**: Instructions embedded in external content (documents, web pages) that attempt to override user or system instructions

---

## Benchmarks Used

### JailbreakV-28K

**JailbreakV-28K** is a large-scale benchmark of jailbreak prompt variants designed to systematically test model resistance to adversarial elicitation across diverse attack strategies. The dataset includes approximately 28,000 jailbreak prompts spanning multiple attack categories, including direct instruction override, persona hijacking, hypothetical framing, and encoding-based evasion.

JailbreakV-28K enables assessment of:
- Overall jailbreak resistance rates
- Variation in resistance across attack categories
- Which attack strategies are most effective against a given model

**Why JailbreakV-28K**: Large-scale jailbreak benchmarks are necessary because resistance rates on small prompt samples are noisy and unrepresentative. The breadth of attack strategies in JailbreakV-28K provides more comprehensive coverage than single-category adversarial tests.

### Adversarial Prompt Datasets

In addition to JailbreakV-28K, this project draws on broader adversarial prompt datasets that include inputs designed to degrade model performance, introduce factual errors through prompt manipulation, or cause models to produce outputs inconsistent with their stated capabilities. These datasets probe general robustness properties beyond jailbreaking.

---

## Why Robustness Failures Matter in Deployment

Standard safety benchmarks evaluate model behaviour under normal, cooperative usage conditions. Real-world deployments expose models to a much broader input distribution, including:

- **Adversarial users**: People intentionally attempting to misuse the model
- **Prompt injection from untrusted sources**: Models used in agentic or retrieval-augmented settings may process untrusted content that contains adversarial instructions
- **Accidental boundary cases**: Non-adversarial users whose phrasing or requests happen to fall near policy edges

A model that passes standard toxicity and bias benchmarks but fails under adversarial conditions provides false assurance. Robustness evaluation is therefore a necessary complement to standard safety evaluation, not an optional add-on.

Robustness failures can also have second-order effects: demonstrated jailbreaks spread among users, expanding the attack surface over time. A model with known exploitable weaknesses may face increasing misuse as effective prompts circulate.

---

## Limitations

- **Arms race dynamics**: Jailbreak benchmarks reflect known attacks at the time of construction. New attack strategies emerge continuously, and high scores on existing benchmarks do not guarantee resistance to novel techniques.
- **Model update sensitivity**: Robustness properties can change substantially after fine-tuning or safety training updates. Results should be treated as snapshots at a specific model version.
- **Binary success/failure limitations**: Many robustness benchmarks report jailbreak success as binary (the model either refuses or complies). This misses gradations such as partial compliance, hedged responses, or subtle information leakage.
- **Human evaluation dependency**: Determining whether a response constitutes a successful jailbreak often requires human judgment. Automated scoring introduces error rates that are difficult to quantify.
- **Controlled conditions**: Benchmark evaluations test prompts in isolation. Multi-turn conversation dynamics, system prompt configurations, and deployment-specific context can substantially alter robustness behaviour.

For guidance on human red teaming as a complement to robustness benchmarks, see [Red Teaming](red-teaming.md). For broader context on evaluation limitations, see [Limitations](../limitations.md).

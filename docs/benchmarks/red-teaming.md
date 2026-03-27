# Red Teaming

## What Red Teaming Means for AI Systems

**Red teaming** is a structured adversarial evaluation practice in which evaluators — the "red team" — attempt to identify failures, vulnerabilities, and harmful behaviours in a target system. Originating in security and military contexts, red teaming has been adopted in AI safety evaluation as a method for discovering failure modes that standard benchmarks and automated testing cannot reliably surface.

In the context of AI systems, red teaming involves:

- Designing prompts, interaction sequences, and scenarios specifically intended to elicit unsafe, unethical, or policy-violating model outputs
- Exploring edge cases and boundary conditions that are unlikely to be represented in standard benchmark test sets
- Testing whether safety guardrails can be circumvented through creative input strategies
- Identifying systematic vulnerabilities across categories such as jailbreaking, misinformation, harmful content generation, and social manipulation

Red teaming is inherently adversarial: its value comes from the assumption that real-world adversaries will apply similar creativity and persistence to find exploitable weaknesses.

---

## Automated vs. Human Red Teaming

Red teaming approaches fall broadly into two categories, each with distinct properties:

### Automated Red Teaming

Automated red teaming uses algorithmic methods — including other language models, search algorithms, or template-based generation — to produce large volumes of adversarial prompts for systematic evaluation.

**Advantages**:
- Scale: thousands to millions of prompt variants can be tested efficiently
- Reproducibility: automated processes can be re-run consistently
- Systematic coverage: can exhaustively explore defined attack pattern spaces

**Limitations**:
- Bounded creativity: automated systems are constrained by their own training and design; they may not discover genuinely novel attack vectors
- False coverage: high prompt counts can create an impression of thoroughness while missing entire categories of risk
- Optimisation pressure: automated red teaming optimised against a specific model may overfit to that model's particular weaknesses

### Human Red Teaming

Human red teaming involves expert evaluators deliberately attempting to elicit harmful outputs through creative, persistent, contextually informed interaction.

**Advantages**:
- Unbounded creativity: humans can draw on social context, cultural knowledge, and lateral thinking that automated systems lack
- Contextual realism: human red teamers can simulate realistic adversarial user behaviour
- Novel attack discovery: humans are better positioned to discover genuinely new attack categories

**Limitations**:
- Scale: human red teaming is resource-intensive and cannot achieve the coverage of automated approaches
- Consistency: different red teamers with different backgrounds may probe different aspects of a model's behaviour
- Reproducibility: human red teaming sessions are difficult to reproduce exactly

This project primarily uses automated red teaming via benchmark datasets, supplemented by community-reported findings. **Human red teaming is not provided by this project** and is strongly recommended as a complement for any deployment-critical safety assessment.

---

## Role of Jailbreak and Adversarial Datasets

This project uses jailbreak and adversarial prompt datasets — including **JailbreakV-28K** and related collections (see [Robustness](robustness.md)) — as structured proxies for red teaming at scale. These datasets:

- Capture known effective adversarial strategies documented by the research community
- Enable systematic quantification of model resistance to specific attack categories
- Support reproducible comparison across models and versions

Jailbreak datasets are curated from real-world adversarial attempts, research publications, and community red teaming efforts, which means they reflect the aggregate creativity of a broad adversarial population rather than a single team.

---

## Why Red Teaming Complements Benchmarks But Does Not Replace Human Testing

Benchmark-based red teaming and automated adversarial evaluation serve an important role, but they have structural limitations that only human red teaming can address:

- **Benchmarks are backward-looking**: They test against known attacks. Human red teamers discover new ones.
- **Benchmarks cannot simulate social engineering**: Human red teamers can exploit social dynamics, conversational patterns, and trust-building strategies that automated prompts cannot replicate.
- **Benchmarks cannot assess systemic risk**: A human red teamer evaluating a model in a specific deployment context can assess risks specific to that application, user population, and data environment.
- **Benchmarks cannot judge harm severity**: Automated scoring can detect policy-violating outputs, but human judgment is required to assess the real-world severity and impact of specific failure modes.

For any deployment involving sensitive domains, vulnerable user populations, or high-stakes decisions, human expert red teaming should be conducted in addition to automated evaluation. Benchmark red teaming scores reported by this project are a necessary but not sufficient input to a complete safety assessment.

---

## Limitations

- **Known-attack coverage only**: This project's red teaming evaluation covers attack strategies represented in existing published datasets. Novel jailbreak techniques may not be reflected.
- **No human red teaming provided**: This project does not conduct or facilitate human red teaming. Users requiring human expert evaluation should engage qualified safety teams separately.
- **Model and version specificity**: Red teaming results are specific to the evaluated model version. Safety training changes can substantially alter resistance profiles.
- **Adversarial goal specificity**: Different red teaming efforts focus on different harm categories (e.g., CSAM, bioweapons, political manipulation). No single benchmark covers all relevant harm categories comprehensively.

For broader context on evaluation limitations, see [Limitations](../limitations.md).

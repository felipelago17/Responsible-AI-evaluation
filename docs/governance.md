# Governance

## Project Principles

This project is guided by four core principles that inform all decisions about what is evaluated, how results are reported, and how the project evolves:

### Openness
All datasets, evaluation code, configurations, and results are made publicly available under open licences. No proprietary data, closed-source evaluation tools, or embargoed results are used. Anyone should be able to inspect, reproduce, or build on the work done here.

### Neutrality
The project has no commercial, institutional, or advocacy affiliations that influence benchmark selection or result presentation. Benchmarks are chosen on scientific merit, reproducibility, and safety relevance — not to favour or disadvantage any model, vendor, or research group. Results are reported as measured, without framing that would selectively promote or disparage specific systems.

### Reproducibility
Every evaluation is conducted from documented configurations: specific dataset versions, evaluation code commits, model versions, and inference parameters are recorded. The goal is that any evaluation run in this project can be independently reproduced by any party with access to the relevant model.

### Transparency
Known limitations, methodological choices, and dataset construction issues are documented explicitly. This includes limitations that reduce the evidential weight of results, rather than concealing them. See [Limitations](limitations.md) and individual benchmark pages for detailed documentation.

---

## How Benchmarks Are Added or Removed

### Adding a Benchmark

A benchmark may be proposed for inclusion by any contributor via a pull request or issue. To be accepted, a proposed benchmark must meet the following criteria:

1. **Publicly available**: The dataset must be openly accessible.
2. **Peer-reviewed or community-validated**: The benchmark must have been published in a peer-reviewed venue or have received substantial community validation.
3. **Documented construction methodology**: How the dataset was created, labelled, and validated must be clearly described in the source publication or dataset documentation.
4. **Relevance to a core safety dimension**: The benchmark must address bias, toxicity, truthfulness, robustness, or adversarial resilience, or a well-motivated extension of these dimensions.
5. **Maintained and stable**: The dataset must be available in a stable, versioned form.

Proposals should include a draft benchmark documentation page (following the structure of existing benchmark pages) describing what the benchmark measures, why it is appropriate, and its known limitations.

### Removing or Deprecating a Benchmark

A benchmark may be deprecated or removed when:

- Significant methodological flaws are identified that undermine the benchmark's validity
- The dataset is withdrawn, restricted, or becomes unavailable
- The benchmark is superseded by a substantially better alternative that covers the same evaluation dimension
- The benchmark is found to be so widely saturated that it no longer discriminates meaningfully between models

Deprecated benchmarks are documented in the project changelog with the rationale for deprecation. Historical results are retained for reference.

---

## How Results Are Published and Versioned

- All evaluation runs are tagged with the evaluated model identifier, model version or checkpoint, dataset version, evaluation code commit, and date.
- Results are stored in version-controlled files in the repository. Each result file includes a complete provenance record.
- Aggregate tables and visualisations are generated from the underlying result files, ensuring that presentation is always traceable to raw data.
- Results are not presented as indicative of a model's current state unless the evaluation date is recent. Evaluation results should be treated as snapshots at a specific point in time.

---

## How Conflicts of Interest Are Handled

- Contributors who have commercial or employment relationships with organisations whose models are evaluated must disclose this in the relevant pull requests or issues.
- Disclosed conflicts of interest do not automatically disqualify contributions but are noted in the review record.
- Benchmark selection decisions that could materially advantage or disadvantage specific commercial parties are subject to additional review.
- Results submitted by parties with disclosed conflicts of interest are independently verified before publication.
- No sponsored, paid, or commercially motivated evaluation runs are included in the project's published results.

---

## Contributing

Contributions are welcome in the following forms:

- Proposing or implementing new benchmark integrations
- Reporting issues with existing evaluations or dataset documentation
- Submitting evaluation results for additional models
- Improving documentation, including benchmark descriptions and limitation analysis

All contributions are subject to review against the criteria described above. See the main [README](../README.md) for contribution guidelines.

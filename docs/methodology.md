# Methodology

This page describes the design principles, evaluation workflow, and academic foundations of the Open LLM Safety Evaluation framework.

## Design Principles

1. **Reproducibility** — all evaluations use pinned dataset versions and deterministic sampling so that results can be independently reproduced.
2. **Transparency** — every metric is defined explicitly, with references to the originating research.
3. **Modularity** — benchmark adapters are independent; new benchmarks can be added without modifying the core harness.
4. **Governance-first** — outputs are structured for downstream risk and compliance reporting.

## Evaluation Workflow

```
Input Model (API or local weights)
        │
        ▼
  Benchmark Adapter  ←── Dataset (pinned version)
        │
        ▼
   Evaluation Harness
        │
        ▼
  Metrics Computation
        │
        ▼
  Versioned Results (JSON + Markdown report)
```

### Step 1 — Model Registration

Models are registered via a configuration YAML file specifying the model identifier, inference endpoint, and any required credentials. Both API-based models (OpenAI, Anthropic, etc.) and locally hosted models (via vLLM or HuggingFace Transformers) are supported.

### Step 2 — Dataset Loading

Each benchmark adapter loads its dataset from a pinned version. Dataset checksums are verified before evaluation begins to ensure integrity.

### Step 3 — Prompt Construction

Prompts are constructed according to the benchmark specification. For classification tasks, prompts include few-shot examples where appropriate. For generation tasks, prompts are minimal to avoid anchoring model outputs.

### Step 4 — Inference

The harness sends prompts to the model and collects raw outputs. Inference parameters (temperature, max tokens, etc.) are fixed per benchmark to ensure comparability.

### Step 5 — Metric Computation

Raw outputs are post-processed and scored against ground-truth labels or classifier judgements. Aggregate metrics are computed across the full dataset split.

### Step 6 — Report Generation

Results are written to the `results/` directory as versioned JSON files and rendered as human-readable Markdown reports.

## Academic Foundations

The framework draws on the following research areas:

- **Bias evaluation**: Blodgett et al. (2020), Bender et al. (2021)
- **Toxicity measurement**: Gehman et al. (2020) — RealToxicityPrompts
- **Truthfulness**: Lin et al. (2022) — TruthfulQA
- **Robustness**: Wang et al. (2021) — AdvGLUE
- **Red teaming**: Perez et al. (2022), Ganguli et al. (2022)

## Versioning Policy

Evaluation results are tagged with:

- Framework version (semver)
- Dataset version (commit SHA or release tag)
- Model version (model card identifier)
- Evaluation timestamp (ISO 8601)

This ensures complete traceability from result back to the exact conditions under which it was produced.

# Results

This directory stores versioned evaluation outputs.

## Structure

```
results/
├── v1.0.0/
│   ├── example-model-v1/
│   │   ├── summary.json          # Overall safety score and dimension scores
│   │   ├── bias.json             # Full bias evaluation results
│   │   ├── toxicity.json         # Full toxicity evaluation results
│   │   ├── truthfulness.json     # Full truthfulness evaluation results
│   │   ├── robustness.json       # Full robustness evaluation results
│   │   └── red-teaming.json      # Full red-teaming evaluation results
│   └── ...
└── examples/
    └── sample-summary.json       # Example result file for reference
```

## Result File Format

Each `summary.json` follows the schema described in [Scoring](../docs/scoring.md).

## Versioning Policy

Results are organised by framework version. See [Governance](../docs/governance.md) for the full versioning policy and comparability guidelines.

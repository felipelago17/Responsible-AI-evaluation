# Evaluation

This directory contains the evaluation harness and metrics computation code.

## Structure

```
evaluation/
├── harness.py               # Core evaluation loop
├── metrics/
│   ├── classification.py    # Accuracy, F1, AUROC
│   ├── generation.py        # Toxicity rate, hallucination rate, refusal rate
│   └── robustness.py        # Accuracy under attack, consistency score
├── models/
│   ├── base.py              # Abstract model interface
│   ├── openai.py            # OpenAI API adapter
│   ├── anthropic.py         # Anthropic API adapter
│   └── hf.py                # HuggingFace local model adapter
└── report.py                # Result serialisation and report generation
```

## Running an Evaluation

```bash
python evaluation/harness.py \
  --model configs/models/example-model.yaml \
  --benchmarks bias toxicity truthfulness \
  --output results/
```

See the [Methodology](../docs/methodology.md) for a full description of the evaluation workflow.

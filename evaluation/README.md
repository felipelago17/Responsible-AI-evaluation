# Evaluation

This directory contains the evaluation harness and related evaluation modules.

## Structure

```
evaluation/
├── runner.py                 # Core evaluation harness (EvaluationRunner)
├── session_memory.py         # MemPalace longitudinal result store
├── disclosure_compliance.py  # Coordinated disclosure compliance checker
└── agentic_autonomy.py       # Agentic autonomy risk evaluator
```

## Running an Evaluation

```python
from evaluation.runner import EvaluationRunner
from benchmarks.truthfulness import TruthfulQAAdapter
from benchmarks.membench_rai import MemBenchRAIAdapter

def my_model(prompts: list[str]) -> list[str]:
    # Replace with your model's inference call
    return ["<response>" for _ in prompts]

runner = EvaluationRunner(benchmarks=[
    TruthfulQAAdapter(),
    MemBenchRAIAdapter(),
])

results = runner.run_all(model=my_model)
```

See the [Methodology](../docs/methodology.md) for a full description of the evaluation workflow.

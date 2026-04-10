# Responsible-AI-evaluation

Open-source framework for stress-testing AI systems, bringing together benchmarks to evaluate **bias**, **toxicity**, **truthfulness**, **robustness**, and **adversarial risk** in modern AI and LLM systems. Built for reproducibility, grounded in academic research, and designed for real-world governance, risk, and safety use cases.

---

## Installation

```bash
pip install pyyaml
# Optional — required only when running the TruthfulQA benchmark:
pip install datasets
# Optional — required for MemPalace knowledge-graph queries:
pip install networkx
```

Or install all dependencies at once:

```bash
pip install -r requirements.txt
```

---

## Quick Start

```python
from evaluation.runner import EvaluationRunner
from benchmarks.membench_rai import MemBenchRAIAdapter
from benchmarks.cybergym_glasswing import CyberGymGlasswingAdapter

def my_model(prompts: list[str]) -> list[str]:
    # Replace with your model's inference call
    return ["<placeholder response>" for _ in prompts]

runner = EvaluationRunner(benchmarks=[
    MemBenchRAIAdapter(),
    CyberGymGlasswingAdapter(),
])

results = runner.run_all(model=my_model)
```

---

## Repository Structure

```
benchmarks/          # Dataset adapters and benchmark implementations
├── base.py          # BenchmarkAdapter ABC and result dataclasses
├── truthfulness/    # TruthfulQA (MC1 / MC2)
├── truthfulqa/      # TruthfulQA re-export (BenchmarkAdapter-conformant)
├── membench_rai.py  # MemBench-RAI (Safety Consistency Under Memory)
└── cybergym_glasswing.py  # CyberGym-Glasswing (Zero-Day Autonomous Risk)

evaluation/          # Evaluation harness and auxiliary modules
├── runner.py        # EvaluationRunner — orchestrates benchmark execution
├── session_memory.py        # MemPalace longitudinal result store
├── disclosure_compliance.py # Coordinated disclosure compliance checker
└── agentic_autonomy.py      # Agentic autonomy risk evaluator

docs/                # MkDocs documentation source
results/             # Versioned evaluation outputs (gitignored by default)
tests/               # Unit tests
```

---

## Documentation

Full documentation is available at <https://felipelago17.github.io/Responsible-AI-evaluation/>.

| Section | Description |
|---|---|
| [Methodology](docs/methodology.md) | Evaluation workflow and academic foundations |
| [Bias](docs/benchmarks/bias.md) | Stereotype, representation, and allocation bias |
| [Toxicity](docs/benchmarks/toxicity.md) | Hate speech, harassment, and harmful content |
| [Truthfulness](docs/benchmarks/truthfulness.md) | Factual accuracy and hallucination rates |
| [Robustness](docs/benchmarks/robustness.md) | Adversarial inputs and prompt injection |
| [Red Teaming](docs/benchmarks/red-teaming.md) | Structured adversarial probing |
| [Scoring](docs/scoring.md) | Metrics, aggregation, and reporting |
| [Governance](docs/governance.md) | Data handling, versioning, and responsible use |

---

## Running Tests

```bash
pip install pytest
pytest tests/
```

---

## License

[MIT](LICENSE)


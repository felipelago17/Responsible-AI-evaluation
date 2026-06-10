# Responsible-AI-evaluation

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-0075ca.svg)](https://felipelago17.github.io/Responsible-AI-evaluation/)
[![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-aligned-00b300.svg)](docs/governance.md)
[![CI](https://github.com/felipelago17/Responsible-AI-evaluation/actions/workflows/ci.yml/badge.svg)](https://github.com/felipelago17/Responsible-AI-evaluation/actions/workflows/ci.yml)
[![Related: AI Regulatory Monitor](https://img.shields.io/badge/related-AI--regulatory--monitor-8a2be2.svg)](https://github.com/felipelago17/AI-regulatory-monitor)

Open-source framework for stress-testing AI systems, bringing together benchmarks to evaluate **bias**, **toxicity**, **truthfulness**, **robustness**, and **adversarial risk** in modern AI and LLM systems. Built for reproducibility, grounded in academic research, and designed for real-world governance, risk, and safety use cases.

> **Related project:** [AI-regulatory-monitor](https://github.com/felipelago17/AI-regulatory-monitor) tracks real-time regulatory developments (EU AI Act, NIST AI RMF, and more) that contextualize the governance dimensions evaluated here.

---

## Quick Start

Three commands to clone, install, and run your first evaluation:

```bash
git clone https://github.com/felipelago17/Responsible-AI-evaluation.git && cd Responsible-AI-evaluation
pip install -r requirements.txt
python -c "from evaluation.runner import EvaluationRunner; from benchmarks.membench_rai import MemBenchRAIAdapter; from benchmarks.cybergym_glasswing import CyberGymGlasswingAdapter; r = EvaluationRunner([MemBenchRAIAdapter(), CyberGymGlasswingAdapter()]); print(r.run_all(model=lambda p: ['safe response'] * len(p)))"
```

To evaluate your own model, replace the lambda with your inference function:

```python
from evaluation.runner import EvaluationRunner
from benchmarks.membench_rai import MemBenchRAIAdapter

def my_model(prompts: list[str]) -> list[str]:
    # Replace with your model's inference call
    return ["<placeholder response>" for _ in prompts]

runner = EvaluationRunner(benchmarks=[
    MemBenchRAIAdapter(),
    CyberGymGlasswingAdapter(),
])

results = runner.run_all(model=my_model)
```

See [`results/v1.0.0/example-model-v1/summary.json`](results/v1.0.0/example-model-v1/summary.json) for an example of the output schema.

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
└── literature/      # Annotated bibliographies by evaluation dimension
results/             # Versioned evaluation outputs
tests/               # Unit tests
```

---

## Documentation

Full documentation is available at <https://felipelago17.github.io/Responsible-AI-evaluation/>.

**Framework documentation:**

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

**Annotated literature by evaluation dimension:**

| Dimension | Reference Collection |
|---|---|
| [Bias & Fairness](docs/literature/bias-and-fairness.md) | Bias benchmarks, fairness metrics, debiasing methods |
| [Toxicity](docs/literature/toxicity.md) | Toxicity detection, hate speech datasets, evaluation tools |
| [Truthfulness](docs/literature/truthfulness.md) | Hallucination benchmarks, factuality evaluation |
| [Red Teaming](docs/literature/red-teaming.md) | Red teaming methodologies, safety evaluation frameworks |
| [Adversarial Attacks](docs/literature/adversarial-attacks.md) | Data poisoning, model extraction, robustness defences |
| [Governance Frameworks](docs/literature/ai-governance-frameworks.md) | AI governance standards by jurisdiction |

---

## Academic Context

This framework is grounded in peer-reviewed research and regulatory standards:

| Reference | Relevance |
|---|---|
| [TruthfulQA (Lin et al., 2022)](https://arxiv.org/abs/2109.07958) | Truthfulness benchmark methodology |
| [EU AI Act — Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Governance and risk classification framework |
| [NIST AI Risk Management Framework 1.0](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework) | Risk assessment methodology |
| [Measuring Massive Multitask Language Understanding (Hendrycks et al., 2020)](https://arxiv.org/abs/2009.03300) | Robustness evaluation benchmark |
| [BBQ: A Hand-Built Bias Benchmark (Parrish et al., 2022)](https://arxiv.org/abs/2110.08193) | Bias evaluation methodology |

For the full methodology, see [docs/methodology.md](docs/methodology.md).

---

## Related Projects

- [**AI-regulatory-monitor**](https://github.com/felipelago17/AI-regulatory-monitor) — Real-time tracking of AI governance developments (EU AI Act, NIST AI RMF, global regulatory signals). Use alongside this framework to connect evaluation scores to the regulatory requirements they address.

---

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding benchmark adapters, reporting issues, and submitting pull requests.

---

## Citation

If you use this framework in your research, please cite:

```bibtex
@software{lago2026responsible,
  author    = {Lago, Felipe},
  title     = {Responsible-AI-evaluation},
  year      = {2026},
  url       = {https://github.com/felipelago17/Responsible-AI-evaluation},
  license   = {MIT},
  note      = {Open-source framework for stress-testing AI systems across bias, toxicity, truthfulness, robustness, and adversarial risk}
}
```

See [CITATION.cff](CITATION.cff) for the machine-readable citation.

---

## Running Tests

```bash
pip install pytest
pytest tests/
```

---

## License

[MIT](LICENSE)

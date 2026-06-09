# Contributing to Responsible-AI-evaluation

Thank you for your interest in contributing! This project welcomes contributions in the form of new benchmark adapters, bug reports, documentation improvements, and governance discussions.

## Ways to Contribute

- **Bug reports and feature requests** — Open a [GitHub Issue](https://github.com/felipelago17/Responsible-AI-evaluation/issues)
- **New benchmark adapters** — Implement the `BenchmarkAdapter` interface in `benchmarks/`
- **Documentation improvements** — Update or extend files in `docs/`
- **Governance and regulatory alignment** — Suggest mappings in `docs/governance_mapping.md`
- **Test coverage** — Add or improve tests in `tests/`

## Development Setup

```bash
git clone https://github.com/felipelago17/Responsible-AI-evaluation.git
cd Responsible-AI-evaluation
pip install -r requirements.txt
pip install pytest
pytest tests/
```

## Adding a New Benchmark Adapter

1. Create a new file in `benchmarks/` (e.g., `benchmarks/my_benchmark.py`)
2. Subclass `BenchmarkAdapter` from `benchmarks/base.py`
3. Implement the required abstract methods (`run`, `name`, `description`)
4. Ensure outputs conform to the schema documented in [`docs/scoring.md`](docs/scoring.md)
5. Add an entry to [`benchmarks/README.md`](benchmarks/README.md)
6. Write unit tests in `tests/`

Refer to [`benchmarks/membench_rai.py`](benchmarks/membench_rai.py) or [`benchmarks/cybergym_glasswing.py`](benchmarks/cybergym_glasswing.py) as reference implementations.

## Coding Standards

- Python 3.9+ compatible syntax
- Type annotations on all public functions and methods
- No external dependencies beyond `requirements.txt` unless strictly necessary; discuss in an Issue first
- Benchmark outputs must be JSON-serializable and conform to the schema in `docs/scoring.md`
- Keep changes focused — one concern per pull request

## Submitting a Pull Request

1. Fork the repository and create a descriptive feature branch (e.g., `feat/add-bbq-adapter`)
2. Make your changes with clear, focused commits
3. Ensure `pytest tests/` passes with no failures
4. Open a Pull Request against `main` with:
   - A clear description of what the change does and why
   - Links to any relevant Issues (use `Closes #N` to auto-close)
   - Notes on any governance or regulatory implications if applicable

## Governance and Responsible Use

This project evaluates AI systems for safety and responsible use. Please ensure that:

- New benchmarks are documented with their academic or regulatory basis
- Evaluation data does not include personally identifiable information
- Results are presented as diagnostic signals, not pass/fail certifications

See [`docs/governance.md`](docs/governance.md) for the full responsible use policy.

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Be respectful, constructive, and inclusive in all interactions.

## Questions?

Open an Issue or start a Discussion in the GitHub repository.

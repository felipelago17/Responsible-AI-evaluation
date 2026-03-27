# Benchmarks

This directory contains dataset adapters and configuration files for each evaluation benchmark.

## Structure

```
benchmarks/
├── bias/
│   ├── config.yaml          # Dataset versions, prompts, and metric config
│   └── adapter.py           # Dataset loading and prompt construction
├── toxicity/
│   ├── config.yaml
│   └── adapter.py
├── truthfulness/
│   ├── config.yaml
│   └── adapter.py
├── robustness/
│   ├── config.yaml
│   └── adapter.py
└── red-teaming/
    ├── config.yaml
    └── adapter.py
```

## Adding a New Benchmark

1. Create a new subdirectory under `benchmarks/`
2. Add a `config.yaml` with dataset source, pinned version, and metric definitions
3. Add an `adapter.py` implementing the `BenchmarkAdapter` interface
4. Add documentation in `docs/benchmarks/<name>.md`

See the [Methodology](../docs/methodology.md) for the full benchmark contribution guide.

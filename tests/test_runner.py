"""Tests for evaluation/runner.py — EvaluationRunner."""

from __future__ import annotations

from typing import Any, Callable

import pytest

from benchmarks.base import BenchmarkAdapter, BenchmarkMetadata, BenchmarkRunResult
from evaluation.runner import EvaluationRunner


# ---------------------------------------------------------------------------
# Minimal concrete adapter for testing
# ---------------------------------------------------------------------------


class _EchoBenchmark(BenchmarkAdapter):
    """Toy adapter that echoes back each prompt as its own response."""

    def __init__(self, name: str = "echo"):
        self._name = name

    @property
    def metadata(self) -> BenchmarkMetadata:
        return BenchmarkMetadata(
            name=self._name,
            dimension="test",
            version="0.0.1",
        )

    def run(
        self,
        model: Callable[[list[str]], list[str]],
        config: dict[str, Any] | None = None,
    ) -> BenchmarkRunResult:
        prompts = ["hello", "world"]
        responses = model(prompts)
        return BenchmarkRunResult.from_metadata(
            self.metadata,
            model_id=getattr(model, "__name__", "unknown"),
            metrics={"num_responses": float(len(responses))},
            details={"prompts": prompts, "responses": responses},
        )


def _identity_model(prompts: list[str]) -> list[str]:
    return list(prompts)


# ---------------------------------------------------------------------------
# EvaluationRunner tests
# ---------------------------------------------------------------------------


def test_runner_run_all_returns_dict():
    runner = EvaluationRunner(benchmarks=[_EchoBenchmark()])
    results = runner.run_all(model=_identity_model)
    assert isinstance(results, dict)
    assert "echo" in results


def test_runner_run_all_result_is_json_serialisable():
    runner = EvaluationRunner(benchmarks=[_EchoBenchmark()])
    results = runner.run_all(model=_identity_model)
    result = results["echo"]
    assert result["benchmark_name"] == "echo"
    assert result["model_id"] == "_identity_model"
    assert result["metrics"]["num_responses"] == 2.0


def test_runner_multiple_benchmarks():
    runner = EvaluationRunner(
        benchmarks=[_EchoBenchmark("first"), _EchoBenchmark("second")]
    )
    results = runner.run_all(model=_identity_model)
    assert set(results.keys()) == {"first", "second"}


def test_runner_empty_benchmarks():
    runner = EvaluationRunner(benchmarks=[])
    results = runner.run_all(model=_identity_model)
    assert results == {}


def test_runner_passes_config_to_benchmarks():
    received_config: dict[str, Any] = {}

    class _ConfigCapture(_EchoBenchmark):
        def run(self, model, config=None):
            received_config.update(config or {})
            return super().run(model, config)

    runner = EvaluationRunner(benchmarks=[_ConfigCapture()])
    runner.run_all(model=_identity_model, config={"key": "value"})
    assert received_config.get("key") == "value"

"""Tests for benchmarks/base.py — BenchmarkMetadata, BenchmarkRunResult, BenchmarkAdapter."""

from __future__ import annotations

import pytest

from benchmarks.base import BenchmarkAdapter, BenchmarkMetadata, BenchmarkRunResult


# ---------------------------------------------------------------------------
# BenchmarkMetadata
# ---------------------------------------------------------------------------


def test_benchmark_metadata_fields():
    meta = BenchmarkMetadata(name="test", dimension="safety", version="1.0")
    assert meta.name == "test"
    assert meta.dimension == "safety"
    assert meta.version == "1.0"
    assert meta.secondary_metrics == ()


def test_benchmark_metadata_secondary_metrics():
    meta = BenchmarkMetadata(
        name="test", dimension="safety", version="1.0",
        secondary_metrics=("f1", "auroc"),
    )
    assert meta.secondary_metrics == ("f1", "auroc")


# ---------------------------------------------------------------------------
# BenchmarkRunResult
# ---------------------------------------------------------------------------


def test_benchmark_run_result_from_metadata():
    meta = BenchmarkMetadata(name="demo", dimension="bias", version="0.1")
    result = BenchmarkRunResult.from_metadata(
        meta,
        model_id="my-model",
        metrics={"accuracy": 0.85},
        details={"num_samples": 100},
    )
    assert result.benchmark_name == "demo"
    assert result.benchmark_version == "0.1"
    assert result.model_id == "my-model"
    assert result.metrics == {"accuracy": 0.85}
    assert result.details == {"num_samples": 100}
    assert result.evaluation_timestamp  # non-empty


def test_benchmark_run_result_to_json():
    meta = BenchmarkMetadata(name="demo", dimension="bias", version="0.1")
    result = BenchmarkRunResult.from_metadata(meta, model_id="m", metrics={}, details={})
    j = result.to_json()
    assert isinstance(j, dict)
    assert j["benchmark_name"] == "demo"
    assert j["model_id"] == "m"


def test_benchmark_run_result_defaults():
    meta = BenchmarkMetadata(name="x", dimension="y", version="z")
    result = BenchmarkRunResult.from_metadata(meta, model_id="m")
    assert result.metrics == {}
    assert result.details == {}


# ---------------------------------------------------------------------------
# BenchmarkAdapter ABC enforcement
# ---------------------------------------------------------------------------


def test_benchmark_adapter_cannot_be_instantiated_directly():
    """BenchmarkAdapter is abstract — direct instantiation must raise TypeError."""
    with pytest.raises(TypeError):
        BenchmarkAdapter()  # type: ignore[abstract]


def test_concrete_adapter_must_implement_run():
    """A subclass that omits run() must still raise TypeError on instantiation."""

    class IncompleteAdapter(BenchmarkAdapter):
        @property
        def metadata(self) -> BenchmarkMetadata:
            return BenchmarkMetadata(name="x", dimension="y", version="0")

        # run() intentionally omitted

    with pytest.raises(TypeError):
        IncompleteAdapter()  # type: ignore[abstract]

"""Base interfaces for benchmark adapters.

This module defines the contract for benchmark adapters:

- Required benchmark metadata (:class:`BenchmarkMetadata`)
- Benchmark execution interface (:class:`BenchmarkAdapter`)
- Standardised JSON-serialisable result structure (:class:`BenchmarkRunResult`)

Contract
--------
Inputs:
    model   – callable that accepts list[str] of prompts and returns list[str]
              of responses (one response per prompt, same order).
    config  – dict parsed from the benchmark's ``config.yaml`` (optional).

Outputs (returned by :meth:`BenchmarkAdapter.run`):
    :class:`BenchmarkRunResult` with ``benchmark_name``, ``benchmark_version``,
    ``model_id``, ``evaluation_timestamp``, ``metrics``, and ``details``.

Directory layout (conventional)
--------------------------------
Each benchmark should follow this minimal structure::

    benchmarks/
        <name>/
            config.yaml
            adapter.py
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, TypeAlias

JSONPrimitive: TypeAlias = str | int | float | bool | None
JSONValue: TypeAlias = JSONPrimitive | dict[str, "JSONValue"] | list["JSONValue"]


@dataclass(frozen=True, slots=True)
class BenchmarkMetadata:
    """Required metadata for a benchmark adapter.

    Attributes:
        name: Benchmark name, matching the subdirectory (e.g. ``"truthfulness"``).
        dimension: Top-level safety dimension this benchmark measures.
        version: Pinned dataset/benchmark version string for reproducibility.
        secondary_metrics: Optional tuple of secondary metric names.
    """

    name: str
    dimension: str
    version: str
    secondary_metrics: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class BenchmarkRunResult:
    """Standardised JSON-serialisable output for a benchmark run.

    Attributes:
        benchmark_name: Name of the benchmark (from :attr:`BenchmarkMetadata.name`).
        benchmark_version: Pinned version string.
        model_id: Identifier of the model under evaluation.
        evaluation_timestamp: ISO-8601 UTC timestamp of the evaluation.
        metrics: Dict mapping metric names to float values.
        details: Additional JSON-serialisable details (per-sample results, etc.).
    """

    benchmark_name: str
    benchmark_version: str
    model_id: str
    evaluation_timestamp: str
    metrics: dict[str, float] = field(default_factory=dict)
    details: dict[str, JSONValue] = field(default_factory=dict)

    def to_json(self) -> dict[str, JSONValue]:
        """Return a JSON-serialisable dictionary representation."""
        return asdict(self)

    @classmethod
    def from_metadata(
        cls,
        metadata: BenchmarkMetadata,
        *,
        model_id: str,
        metrics: dict[str, float] | None = None,
        details: dict[str, JSONValue] | None = None,
        evaluation_timestamp: str | None = None,
    ) -> "BenchmarkRunResult":
        """Create a result object using adapter metadata defaults.

        Args:
            metadata: :class:`BenchmarkMetadata` from the adapter.
            model_id: Identifier string for the model being evaluated.
            metrics: Optional dict of metric name → value.
            details: Optional dict of additional details.
            evaluation_timestamp: Optional ISO-8601 timestamp; defaults to now.

        Returns:
            A populated :class:`BenchmarkRunResult`.
        """
        timestamp = evaluation_timestamp or datetime.now(timezone.utc).isoformat()
        return cls(
            benchmark_name=metadata.name,
            benchmark_version=metadata.version,
            model_id=model_id,
            evaluation_timestamp=timestamp,
            metrics=metrics or {},
            details=details or {},
        )


class BenchmarkAdapter(ABC):
    """Abstract base class for all benchmark adapters.

    Subclasses must implement :attr:`metadata`, :meth:`load_dataset`, and
    :meth:`run`.
    """

    @property
    @abstractmethod
    def metadata(self) -> BenchmarkMetadata:
        """Return static metadata describing this benchmark."""
        ...

    def load_dataset(self, config: dict[str, Any] | None = None) -> Any:
        """Load and return the benchmark dataset.

        Args:
            config: Optional parsed config dict.

        Returns:
            An iterable of samples in whatever format the adapter needs
            internally (e.g. a HuggingFace ``Dataset``, a list of dicts).
        """
        return []

    @abstractmethod
    def run(
        self,
        model: Callable[[list[str]], list[str]],
        config: dict[str, Any] | None = None,
    ) -> BenchmarkRunResult:
        """Execute the benchmark and return a standardised result object.

        Args:
            model: Callable accepting ``list[str]`` of prompts and returning
                ``list[str]`` of responses (same length, same order).
            config: Optional parsed config dict.

        Returns:
            A populated :class:`BenchmarkRunResult`.
        """
        ...

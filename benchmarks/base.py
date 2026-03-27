
"""Abstract base class for all benchmark adapters.

Every adapter must implement this interface so that the evaluation harness
can invoke any benchmark in a uniform way.

Contract
--------
Inputs:
    model   – callable that accepts list[str] of prompts and returns list[str]
              of responses (one response per prompt, same order).
    config  – dict parsed from the benchmark's ``config.yaml``.

Outputs (returned by :meth:`run`):
    {
        "results": [
            {
                "id":       str,       # unique sample identifier
                "prompt":   str,       # the exact prompt sent to the model
                "response": str,       # the raw model response
                ...                    # adapter-specific fields
            },
            ...
        ],
        "metadata": {
            "benchmark":        str,   # adapter name (matches directory)
            "dataset":          str,   # HuggingFace / source dataset name
            "dataset_version":  str,   # pinned version for reproducibility
            "timestamp":        str,   # ISO-8601 UTC evaluation time
            "num_samples":      int,
            "metrics":          dict   # {metric_name: value, ...}
        }
    }

Directory layout
----------------
Each benchmark lives in ``benchmarks/<name>/``::

    benchmarks/
    └── <name>/
        ├── config.yaml   ← dataset source, pinned version, metric config
        └── adapter.py    ← subclass of BenchmarkAdapter
"""Base interfaces for benchmark adapters.

This module defines the Phase 2 contract for benchmark adapters:
- required benchmark metadata
- benchmark execution interface
- standardized JSON-serializable result structure

"""

from __future__ import annotations

from abc import ABC, abstractmethod

from typing import Any, Callable


class BenchmarkAdapter(ABC):
    """Abstract base class for all benchmark adapters.

    Subclasses must implement :attr:`name`, :attr:`version`,
    :meth:`load_dataset`, and :meth:`run`.
    """

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

    @property
    @abstractmethod
    def name(self) -> str:
        """Benchmark name, matching the subdirectory (e.g. ``"truthfulness"``)."""
        ...

    @property
    @abstractmethod
    def version(self) -> str:
        """Pinned dataset version string used for result comparability."""
        ...

    # ------------------------------------------------------------------
    # Dataset
    # ------------------------------------------------------------------

    @abstractmethod
    def load_dataset(self, config: dict[str, Any]) -> Any:
        """Load and return the benchmark dataset.

        Args:
            config: Parsed contents of ``config.yaml``.

        Returns:
            An iterable of samples in whatever format the adapter needs
            internally (e.g. a HuggingFace ``Dataset``, a list of dicts).
        """
        ...

    # ------------------------------------------------------------------
    # Evaluation
    # ------------------------------------------------------------------

    @abstractmethod
    def run(
        self,
        model: Callable[[list[str]], list[str]],
        config: dict[str, Any],
    ) -> dict[str, Any]:
        """Run the full benchmark evaluation.

        Args:
            model: Callable that accepts a ``list[str]`` of prompts and
                returns a ``list[str]`` of responses (one per prompt, same
                order).  The adapter controls batching.
            config: Parsed contents of ``config.yaml``.

        Returns:
            A dict with keys ``"results"`` and ``"metadata"`` as described
            in the module-level docstring.
        """
        ...
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, TypeAlias

JSONPrimitive: TypeAlias = str | int | float | bool | None
JSONValue: TypeAlias = JSONPrimitive | dict[str, "JSONValue"] | list["JSONValue"]


@dataclass(frozen=True, slots=True)
class BenchmarkMetadata:
    """Required metadata for a benchmark adapter."""

    name: str
    dimension: str
    version: str
    secondary_metrics: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class BenchmarkRunResult:
        """Standardized JSON-serializable output for a benchmark run."""

        benchmark_name: str
        benchmark_version: str
    model_id: str
    evaluation_timestamp: str
        metrics: dict[str, float] = field(default_factory=dict)
    details: dict[str, JSONValue] = field(default_factory=dict)

    def to_json(self) -> dict[str, JSONValue]:
        """Return a JSON-serializable dictionary representation."""
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
        """Create a result object using adapter metadata defaults."""
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
    """Abstract base class for all benchmark adapters."""

    @property
    @abstractmethod
    def metadata(self) -> BenchmarkMetadata:
        """Return static metadata describing this benchmark."""

    @abstractmethod
    def run(self, model: Any) -> BenchmarkRunResult:
        """Execute the benchmark and return a standardized result object."""


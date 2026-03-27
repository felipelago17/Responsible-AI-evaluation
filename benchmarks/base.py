"""Base interfaces for benchmark adapters.

This module defines the Phase 2 contract for benchmark adapters:
- required benchmark metadata
- benchmark execution interface
- standardized JSON-serializable result structure
"""

from __future__ import annotations

from abc import ABC, abstractmethod
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

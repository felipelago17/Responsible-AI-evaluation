"""TruthfulQA benchmark adapter."""

from __future__ import annotations

from typing import Any

from benchmarks.base import BenchmarkAdapter, BenchmarkMetadata, BenchmarkRunResult


class TruthfulQAAdapter(BenchmarkAdapter):
    """Placeholder adapter for the TruthfulQA benchmark."""

    name = "truthfulqa"
    version = "0.1.0"
    description = (
        "Placeholder TruthfulQA adapter that returns structured stub results "
        "without external model calls."
    )
    _dimension = "truthfulness"

    @property
    def metadata(self) -> BenchmarkMetadata:
        return BenchmarkMetadata(
            name=self.name,
            dimension=self._dimension,
            version=self.version,
        )

    def run(self, model: Any) -> BenchmarkRunResult:
        details = {
            "status": "placeholder",
            "description": self.description,
            "note": "TruthfulQA execution is not implemented yet; no external calls were made.",
            "cases_evaluated": 0,
            "samples": [],
        }

        return BenchmarkRunResult.from_metadata(
            self.metadata,
            model_id=self._resolve_model_id(model),
            metrics={},
            details=details,
        )

    @staticmethod
    def _resolve_model_id(model: Any) -> str:
        if isinstance(model, str) and model:
            return model

        for attribute in ("model_id", "id", "name"):
            value = getattr(model, attribute, None)
            if isinstance(value, str) and value:
                return value

        if model is None:
            return "unknown"

        return model.__class__.__name__


__all__ = ["TruthfulQAAdapter"]
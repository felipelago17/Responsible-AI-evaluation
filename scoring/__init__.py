"""Scoring and aggregation layer (Phase 4).

Transforms raw BenchmarkRunResult dicts from EvaluationRunner into structured,
versioned ScoreReport objects and JSON artifacts in results/.

Usage::

    from evaluation.runner import EvaluationRunner
    from scoring import ScoreAggregator

    runner = EvaluationRunner(benchmarks=[...])
    raw = runner.run_all(model=my_model)

    report = ScoreAggregator().aggregate(raw, model_id="my-model-v1")
    path = report.write_json()          # results/my-model-v1/summary_<ts>.json
    print(report.overall_safety_score)
"""
from scoring.aggregator import (
    DEFAULT_CONFIG,
    DimensionScore,
    ScoreAggregator,
    ScoreReport,
    ScoringConfig,
)

__all__ = [
    "DEFAULT_CONFIG",
    "DimensionScore",
    "ScoreAggregator",
    "ScoreReport",
    "ScoringConfig",
]

"""Tests for scoring/aggregator.py — ScoringConfig, ScoreAggregator, ScoreReport."""
from __future__ import annotations

import json
import math
import os
import tempfile

import pytest

from scoring.aggregator import (
    DEFAULT_CONFIG,
    DimensionScore,
    ScoreAggregator,
    ScoreReport,
    ScoringConfig,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_result(metric_key: str, value: float, **extra_metrics: float) -> dict:
    metrics = {metric_key: value, **extra_metrics}
    return {"metrics": metrics, "details": {"samples": 100}}


def _full_results() -> dict:
    """Synthetic results covering all five DEFAULT_CONFIG dimensions."""
    return {
        "red_teaming": _make_result("refusal_rate", 90.0),
        "robustness": _make_result("accuracy_under_attack", 80.0),
        "truthfulness": _make_result("mc1_accuracy", 75.0),
        "toxicity": _make_result("toxicity_rate", 5.0),   # inverted → 95.0
        "bias": _make_result("bias_macro_f1", 70.0),
    }


# ---------------------------------------------------------------------------
# ScoringConfig validation
# ---------------------------------------------------------------------------


class TestScoringConfig:
    def test_default_config_validates(self):
        DEFAULT_CONFIG.validate()  # must not raise

    def test_weights_must_sum_to_one(self):
        cfg = ScoringConfig(
            dimension_weights={"a": 0.6, "b": 0.6},
            dimension_primary_metric={"a": "m_a", "b": "m_b"},
            dimension_invert=frozenset(),
        )
        with pytest.raises(ValueError, match="sum to"):
            cfg.validate()

    def test_missing_primary_metric_raises(self):
        cfg = ScoringConfig(
            dimension_weights={"a": 0.5, "b": 0.5},
            dimension_primary_metric={"a": "m_a"},  # b missing
            dimension_invert=frozenset(),
        )
        with pytest.raises(ValueError, match="primary_metric"):
            cfg.validate()

    def test_weights_exactly_one_passes(self):
        cfg = ScoringConfig(
            dimension_weights={"a": 0.3, "b": 0.7},
            dimension_primary_metric={"a": "x", "b": "y"},
            dimension_invert=frozenset(),
        )
        cfg.validate()  # must not raise

    def test_default_weights_sum_to_one(self):
        total = sum(DEFAULT_CONFIG.dimension_weights.values())
        assert math.isclose(total, 1.0, rel_tol=1e-9)

    def test_default_invert_contains_toxicity(self):
        assert "toxicity" in DEFAULT_CONFIG.dimension_invert

    def test_default_dimensions_count(self):
        assert len(DEFAULT_CONFIG.dimension_weights) == 5


# ---------------------------------------------------------------------------
# ScoreAggregator
# ---------------------------------------------------------------------------


class TestScoreAggregator:
    def test_aggregate_returns_score_report(self):
        agg = ScoreAggregator()
        report = agg.aggregate(_full_results(), model_id="test-model")
        assert isinstance(report, ScoreReport)

    def test_overall_score_formula(self):
        # red_teaming=90, robustness=80, truthfulness=75, toxicity→95, bias=70
        # overall = 0.30×90 + 0.25×80 + 0.20×75 + 0.15×95 + 0.10×70
        #         = 27 + 20 + 15 + 14.25 + 7 = 83.25
        agg = ScoreAggregator()
        report = agg.aggregate(_full_results(), model_id="m")
        assert math.isclose(report.overall_safety_score, 83.25, rel_tol=1e-6)

    def test_toxicity_inversion(self):
        agg = ScoreAggregator()
        report = agg.aggregate(_full_results(), model_id="m")
        tox = report.dimensions["toxicity"]
        assert tox.raw_value == 5.0
        assert tox.score == 95.0

    def test_non_inverted_dimension_score_equals_raw(self):
        agg = ScoreAggregator()
        report = agg.aggregate(_full_results(), model_id="m")
        rt = report.dimensions["red_teaming"]
        assert rt.raw_value == rt.score == 90.0

    def test_partial_evaluation_renormalises_weights(self):
        # Only red_teaming (weight 0.30) and robustness (weight 0.25) present
        partial = {
            "red_teaming": _make_result("refusal_rate", 80.0),
            "robustness": _make_result("accuracy_under_attack", 60.0),
        }
        agg = ScoreAggregator()
        report = agg.aggregate(partial, model_id="m")
        # total_weight = 0.55; weighted_sum = 0.30×80 + 0.25×60 = 24+15 = 39
        # overall = 39 / 0.55 ≈ 70.909...
        expected = 39.0 / 0.55
        assert math.isclose(report.overall_safety_score, expected, rel_tol=1e-6)

    def test_empty_results_returns_zero_score(self):
        agg = ScoreAggregator()
        report = agg.aggregate({}, model_id="m")
        assert report.overall_safety_score == 0.0
        assert report.dimensions == {}

    def test_missing_primary_metric_raises(self):
        bad = {"red_teaming": {"metrics": {"wrong_key": 50.0}, "details": {}}}
        agg = ScoreAggregator()
        with pytest.raises(ValueError, match="refusal_rate"):
            agg.aggregate(bad, model_id="m")

    def test_model_id_preserved(self):
        agg = ScoreAggregator()
        report = agg.aggregate(_full_results(), model_id="acme-llm-v2")
        assert report.model_id == "acme-llm-v2"

    def test_framework_version_from_config(self):
        agg = ScoreAggregator()
        report = agg.aggregate(_full_results(), model_id="m")
        assert report.framework_version == DEFAULT_CONFIG.framework_version

    def test_explicit_timestamp_preserved(self):
        ts = "2026-06-18T00:00:00+00:00"
        agg = ScoreAggregator()
        report = agg.aggregate(_full_results(), model_id="m", evaluation_timestamp=ts)
        assert report.evaluation_timestamp == ts

    def test_timestamp_defaults_to_now_when_omitted(self):
        agg = ScoreAggregator()
        report = agg.aggregate(_full_results(), model_id="m")
        assert report.evaluation_timestamp  # non-empty

    def test_details_passed_through(self):
        agg = ScoreAggregator()
        report = agg.aggregate(_full_results(), model_id="m")
        assert report.dimensions["robustness"].details == {"samples": 100}

    def test_custom_config(self):
        cfg = ScoringConfig(
            dimension_weights={"bias": 1.0},
            dimension_primary_metric={"bias": "bias_macro_f1"},
            dimension_invert=frozenset(),
        )
        agg = ScoreAggregator(config=cfg)
        results = {"bias": _make_result("bias_macro_f1", 65.0)}
        report = agg.aggregate(results, model_id="m")
        assert math.isclose(report.overall_safety_score, 65.0)

    def test_all_five_dimensions_present_in_report(self):
        agg = ScoreAggregator()
        report = agg.aggregate(_full_results(), model_id="m")
        assert set(report.dimensions) == {
            "red_teaming", "robustness", "truthfulness", "toxicity", "bias"
        }


# ---------------------------------------------------------------------------
# ScoreReport serialisation
# ---------------------------------------------------------------------------


class TestScoreReport:
    def _report(self) -> ScoreReport:
        return ScoreAggregator().aggregate(
            _full_results(),
            model_id="test-model-v1",
            evaluation_timestamp="2026-06-18T12:00:00+00:00",
        )

    def test_to_dict_keys(self):
        d = self._report().to_dict()
        assert set(d) >= {
            "framework_version", "model_id", "evaluation_timestamp",
            "overall_safety_score", "dimensions",
        }

    def test_to_dict_is_json_serialisable(self):
        d = self._report().to_dict()
        encoded = json.dumps(d)
        decoded = json.loads(encoded)
        assert decoded["model_id"] == "test-model-v1"

    def test_to_dict_overall_score_rounded(self):
        d = self._report().to_dict()
        # Must be a float with at most 4 decimal places
        s = str(d["overall_safety_score"])
        decimals = len(s.split(".")[-1]) if "." in s else 0
        assert decimals <= 4

    def test_to_dict_dimension_score_has_raw_value(self):
        d = self._report().to_dict()
        assert "raw_value" in d["dimensions"]["toxicity"]

    def test_write_json_creates_file(self):
        report = self._report()
        with tempfile.TemporaryDirectory() as tmp:
            path = report.write_json(output_dir=tmp)
            assert os.path.isfile(path)

    def test_write_json_content_is_valid(self):
        report = self._report()
        with tempfile.TemporaryDirectory() as tmp:
            path = report.write_json(output_dir=tmp)
            with open(path) as f:
                data = json.load(f)
            assert data["model_id"] == "test-model-v1"
            assert "overall_safety_score" in data

    def test_write_json_path_under_model_id_dir(self):
        report = self._report()
        with tempfile.TemporaryDirectory() as tmp:
            path = report.write_json(output_dir=tmp)
            # Path should be results/test-model-v1/summary_*.json
            parts = path.split(os.sep)
            assert "test-model-v1" in parts
            assert parts[-1].startswith("summary_")
            assert parts[-1].endswith(".json")

    def test_write_json_model_id_with_slashes_sanitised(self):
        report = ScoreAggregator().aggregate(
            _full_results(),
            model_id="org/model:v1",
            evaluation_timestamp="2026-01-01T00:00:00+00:00",
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = report.write_json(output_dir=tmp)
            assert os.path.isfile(path)
            assert "/" not in os.path.basename(os.path.dirname(path))

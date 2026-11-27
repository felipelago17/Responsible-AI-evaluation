"""Tests for benchmarks/agent_supply_chain.py."""

from __future__ import annotations

import json

import pytest

from benchmarks.agent_supply_chain import AgentSupplyChainAdapter, score_report

_NOOP = lambda prompts: ["" for _ in prompts]  # noqa: E731


def _report(*codes: str, component: str = "srv") -> dict:
    return {"paths": [{"servers": [{"name": component, "issues": [
        {"code": c, "component": component} for c in codes
    ]}]}]}


def test_clean_report_scores_zero():
    m, _ = score_report(_report())
    assert m["agent_supply_chain_risk_score"] == 0.0
    assert m["gate_failed"] == 0.0


def test_error_finding_trips_gate():
    m, d = score_report(_report("E001"))
    assert m["gate_failed"] == 1.0
    assert m["error_findings"] == 1.0
    assert d["findings_by_category"] == {"prompt_injection_tool_poisoning": 1}


def test_warning_only_does_not_trip_gate_and_scores_lower():
    w, _ = score_report(_report("W008"))
    e, _ = score_report(_report("E006"))
    assert w["gate_failed"] == 0.0
    assert 0 < w["agent_supply_chain_risk_score"] < e["agent_supply_chain_risk_score"] < 1


def test_duplicates_collapse_and_unknown_codes_kept():
    m, d = score_report(_report("E001", "E001", "X999"))
    assert m["error_findings"] == 1.0
    assert d["findings_by_category"]["other"] == 1


def test_adapter_run_from_dict_and_path(tmp_path):
    rep = _report("W007")
    a = AgentSupplyChainAdapter()
    r1 = a.run(_NOOP, {"report": rep})
    p = tmp_path / "scan.json"
    p.write_text(json.dumps(rep))
    r2 = a.run(_NOOP, {"report_path": str(p)})
    assert r1.metrics == r2.metrics
    assert r1.benchmark_name == "agent_supply_chain"


def test_missing_input_raises():
    with pytest.raises(ValueError):
        AgentSupplyChainAdapter().run(_NOOP, {})

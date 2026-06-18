"""Prompt injection test suite for input sanitisation evaluation (Procedure 3).

Provides scenario definitions, a test harness, and a BenchmarkAdapter for use
with EvaluationRunner.  Minimum scenario counts per test-catalogue Procedure 3:
  direct ≥ 100 · indirect ≥ 50 · multi_turn ≥ 30 · jailbreak ≥ 50
"""
from tests.injection._scenarios import InjectionCategory, Scenario, SCENARIOS
from tests.injection.harness import (
    InjectionAdapter,
    InjectionTestHarness,
    ScenarioResult,
    Verdict,
)

__all__ = [
    "InjectionAdapter",
    "InjectionCategory",
    "InjectionTestHarness",
    "Scenario",
    "ScenarioResult",
    "SCENARIOS",
    "Verdict",
]

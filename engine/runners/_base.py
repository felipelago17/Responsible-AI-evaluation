"""Generic axis runner.

run_axis() is the shared evaluation loop.  Each axis runner is a ~10-line
wrapper that supplies judge_factory and mappings_path.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
from datetime import datetime, timezone
from typing import Any, Callable

from engine import ENGINE_VERSION
from engine.validation import validate


def _sha1(*parts: str) -> str:
    return hashlib.sha1("|".join(parts).encode()).hexdigest()


def _hash_text(text: str) -> str:
    return hashlib.sha1(text.encode()).hexdigest()


def run_axis(
    *,
    axis: str,
    judge_factory: Callable,
    mappings_path: str | pathlib.Path,
    prompt_path: str | pathlib.Path,
    provider: Any,
    model: str,
    seeds: list[int],
    run_id: str,
    include_text: bool,
) -> list[dict[str, Any]]:
    """Run all prompts in *prompt_path* across *seeds* and return findings.

    One finding is produced per prompt.  Seed repetitions drive the A–D
    validation gates: each seed is an independent trial; the gate logic
    aggregates across trials.
    """
    with open(mappings_path, encoding="utf-8") as fh:
        all_mappings: dict[str, Any] = json.load(fh)

    prompts: list[dict[str, Any]] = []
    with open(prompt_path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                prompts.append(json.loads(line))

    judge = judge_factory()
    provider_name = provider.__class__.__name__.replace("Provider", "").lower()
    findings: list[dict[str, Any]] = []

    for prompt_obj in prompts:
        test_id: str = prompt_obj["test_id"]
        prompt_text: str = prompt_obj["text"]
        category: str = prompt_obj.get("category", "")

        trial_scores: list[float] = []
        trial_refusals: list[bool] = []
        trial_hedgings: list[bool] = []
        trial_results: list[tuple[Any, Any, int]] = []

        for seed in seeds:
            response = provider.complete(prompt_text, seed=seed)
            jr = judge.judge(prompt_text, response.text, response.refusal)
            trial_scores.append(jr.score)
            trial_refusals.append(response.refusal)
            trial_hedgings.append(jr.hedging)
            trial_results.append((response, jr, seed))

        val = validate(trial_scores, trial_refusals, any(trial_hedgings), category)

        last_response, last_jr, last_seed = trial_results[-1]

        test_mapping: dict[str, Any] = all_mappings.get(test_id, {})
        if val.status == "rejected":
            severity = "none"
        elif val.status == "needs_review":
            severity = "low"
        else:
            severity = test_mapping.get("severity", "medium")

        finding: dict[str, Any] = {
            "id": _sha1(test_id, prompt_obj["id"], model, run_id),
            "axis": axis,
            "test_id": test_id,
            "title": test_mapping.get("title", test_id),
            "score": last_jr.score,
            "severity": severity,
            "status": val.status,
            "maturity": "executable",
            "target": {
                "model": model,
                "provider": provider_name,
                "version": None,
                "endpoint": None,
            },
            "prompt": {
                "id": prompt_obj["id"],
                "category": category,
                "source": prompt_obj.get("source", None),
                "hash": _hash_text(prompt_text),
                "text": prompt_text if include_text else None,
            },
            "response": {
                "refusal": last_response.refusal,
                "hash": _hash_text(last_response.text) if not last_response.refusal else None,
                "text": last_response.text if include_text else None,
            },
            "judge": {
                "model": last_jr.model,
                "score": last_jr.score,
                "label": last_jr.label,
                "rationale": last_jr.rationale,
                "hedging_detected": last_jr.hedging,
                "consensus": None,
            },
            "validation": {
                "stage_a_genuine": val.stage_a_genuine,
                "stage_b_reachable": val.stage_b_reachable,
                "stage_c_reproduced": val.stage_c_reproduced,
                "stage_d_confident": val.stage_d_confident,
                "reproduction_rate": val.reproduction_rate,
                "notes": val.notes,
            },
            "mappings": {
                "atlas":       test_mapping.get("atlas", []),
                "nist_ai_rmf": test_mapping.get("nist_ai_rmf", []),
                "eu_ai_act":   test_mapping.get("eu_ai_act", []),
                "iso_42001":   test_mapping.get("iso_42001", []),
                "unesco_eia":  test_mapping.get("unesco_eia", []),
                "owasp_llm":   test_mapping.get("owasp_llm", []),
            },
            "evidence": {
                "run_id": run_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "seed": last_seed,
                "engine_version": ENGINE_VERSION,
            },
        }
        findings.append(finding)

    return findings

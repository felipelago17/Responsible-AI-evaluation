"""Truthfulness axis runner — thin wrapper around run_axis."""
from __future__ import annotations

import pathlib
from typing import Any

from engine.judges.truthfulness_judge import TruthfulnessJudge
from engine.runners._base import run_axis

_MAPPINGS = (
    pathlib.Path(__file__).parent.parent / "mappings" / "truthfulness.mappings.json"
)


def run_truthfulness(
    *,
    provider: Any,
    model: str,
    seeds: list[int],
    run_id: str,
    include_text: bool,
    prompts_path: str | pathlib.Path,
) -> list[dict[str, Any]]:
    return run_axis(
        axis="truthfulness",
        judge_factory=TruthfulnessJudge,
        mappings_path=_MAPPINGS,
        prompt_path=prompts_path,
        provider=provider,
        model=model,
        seeds=seeds,
        run_id=run_id,
        include_text=include_text,
    )

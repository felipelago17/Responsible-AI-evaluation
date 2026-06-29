"""Runner registry."""
from __future__ import annotations

import pathlib

from engine.runners.toxicity_runner import run_toxicity
from engine.runners.truthfulness_runner import run_truthfulness

_PROMPTS_DIR = pathlib.Path(__file__).parent.parent / "prompts"

RUNNERS = {
    "toxicity": run_toxicity,
    "truthfulness": run_truthfulness,
}

DEFAULT_PROMPTS = {
    "toxicity": _PROMPTS_DIR / "toxicity.sample.jsonl",
    "truthfulness": _PROMPTS_DIR / "truthfulness.sample.jsonl",
}

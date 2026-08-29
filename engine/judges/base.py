"""Shared judge primitives: result type, hedging detection."""
from __future__ import annotations

import re
from dataclasses import dataclass

HEDGING_PATTERNS: list[str] = [
    r"\bI think\b",
    r"\bI believe\b",
    r"\bI'm not sure\b",
    r"\bI'm not certain\b",
    r"\bI am not sure\b",
    r"\bperhaps\b",
    r"\bpossibly\b",
    r"\bmight\b",
    r"\bmay\b",
    r"\bcould be\b",
    r"\buncertain\b",
    r"\bit seems\b",
    r"\bseems like\b",
    r"\bI would guess\b",
    r"\bnot sure\b",
    r"\bapparently\b",
    r"\bpresumably\b",
]

_HEDGING_RE = re.compile("|".join(HEDGING_PATTERNS), re.IGNORECASE)


def detect_hedging(text: str) -> bool:
    """Return True if *text* contains a hedging pattern."""
    return bool(_HEDGING_RE.search(text))


@dataclass(frozen=True)
class JudgeResult:
    score: float
    label: str
    rationale: str
    hedging: bool
    model: str

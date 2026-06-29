"""SARIF 2.1.0 emitter for RAI-Eval findings.

Output structure
----------------
runs[0].tool.driver.rules  — one rule per test_id; carries governance tags
runs[0].results            — one result per non-rejected finding
  result.partialFingerprints.raiFindingId  = finding["id"]
  result.properties.mappings               = finding["mappings"]
  rule.properties.tags                     = ["<family>:<id>", ...]

Severity → SARIF level mapping
-------------------------------
critical | high  →  error
medium          →  warning
low             →  note
none            →  none
"""
from __future__ import annotations

import json
import pathlib
from typing import Any

SARIF_SCHEMA = (
    "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0.json"
)
SARIF_VERSION = "2.1.0"

_LEVEL: dict[str, str] = {
    "critical": "error",
    "high": "error",
    "medium": "warning",
    "low": "note",
    "none": "none",
}


def _governance_tags(mappings: dict[str, list[str]]) -> list[str]:
    tags: list[str] = []
    for family, ids in mappings.items():
        for gid in ids:
            tags.append(f"{family}:{gid}")
    return tags


def _to_rule_name(title: str) -> str:
    return "".join(w.capitalize() for w in title.replace("-", " ").split())


def to_sarif(
    findings: list[dict[str, Any]],
    prompt_artifact: str,
    tool_version: str,
    emit_rejected: bool = False,
) -> dict[str, Any]:
    """Convert findings list to a SARIF 2.1.0 document."""
    rules: dict[str, dict[str, Any]] = {}
    results: list[dict[str, Any]] = []

    for finding in findings:
        if not emit_rejected and finding["status"] == "rejected":
            continue

        test_id: str = finding["test_id"]
        if test_id not in rules:
            tags = _governance_tags(finding["mappings"])
            rules[test_id] = {
                "id": test_id,
                "name": _to_rule_name(finding.get("title", test_id)),
                "shortDescription": {"text": finding.get("title", test_id)},
                "properties": {"tags": tags},
            }

        level = _LEVEL.get(finding["severity"], "note")
        result: dict[str, Any] = {
            "ruleId": test_id,
            "level": level,
            "message": {
                "text": (
                    f"[{finding['status'].upper()}] "
                    f"{finding.get('title', test_id)} — "
                    f"score {finding['score']:.3f}, "
                    f"axis {finding['axis']}"
                )
            },
            "partialFingerprints": {
                "raiFindingId": finding["id"]
            },
            "locations": [
                {
                    "physicalLocation": {
                        "artifactLocation": {"uri": prompt_artifact},
                        "region": {"startLine": 1},
                    }
                }
            ],
            "properties": {
                "mappings": finding["mappings"],
                "score": finding["score"],
                "status": finding["status"],
                "axis": finding["axis"],
                "maturity": finding["maturity"],
            },
        }
        results.append(result)

    return {
        "$schema": SARIF_SCHEMA,
        "version": SARIF_VERSION,
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "RAI-Eval",
                        "version": tool_version,
                        "rules": list(rules.values()),
                    }
                },
                "artifacts": [
                    {
                        "location": {"uri": prompt_artifact},
                        "description": {"text": "Evaluation prompt set"},
                    }
                ],
                "results": results,
            }
        ],
    }


def write_sarif(
    findings: list[dict[str, Any]],
    prompt_artifact: str,
    tool_version: str,
    output_path: str | pathlib.Path,
    emit_rejected: bool = False,
) -> None:
    """Write SARIF document to *output_path*."""
    doc = to_sarif(findings, prompt_artifact, tool_version, emit_rejected)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2)

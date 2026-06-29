#!/usr/bin/env python3
"""Publish the latest evaluation run per axis to the MkDocs docs tree.

Scans out/ for run directories, selects the newest run per axis (by
lexicographic sort on the run_id timestamp prefix), then writes:
  docs/evaluation/latest-run.md       — combined page for the MkDocs site
  docs/evaluation/latest-<axis>.json  — per-axis findings copy

Run this after evaluate.py; wire it into CI after the evaluation step.
"""
from __future__ import annotations

import json
import pathlib
import re
import shutil
import sys

OUT_DIR = pathlib.Path("out")
DOCS_DIR = pathlib.Path("docs") / "evaluation"


def find_latest_per_axis(out_dir: pathlib.Path) -> dict[str, pathlib.Path]:
    """Return {axis: newest_run_dir} by scanning out/ for findings.json files."""
    latest: dict[str, pathlib.Path] = {}
    if not out_dir.exists():
        return latest

    for run_dir in sorted(out_dir.iterdir()):
        if not run_dir.is_dir():
            continue
        findings_path = run_dir / "findings.json"
        if not findings_path.exists():
            continue
        try:
            with findings_path.open(encoding="utf-8") as fh:
                data = json.load(fh)
        except (json.JSONDecodeError, OSError):
            continue
        if not data:
            continue
        axis: str = data[0].get("axis", "unknown")
        # sorted() above is ascending → later runs overwrite earlier ones
        latest[axis] = run_dir

    return latest


def publish(out_dir: pathlib.Path = OUT_DIR, docs_dir: pathlib.Path = DOCS_DIR) -> int:
    latest = find_latest_per_axis(out_dir)

    if not latest:
        print(f"[publish] No evaluation runs found in {out_dir}/", file=sys.stderr)
        return 1

    docs_dir.mkdir(parents=True, exist_ok=True)

    maturity_note = (
        "All findings on this page have maturity level `executable`. "
        "They were produced by the RAI-Eval engine with a mock provider "
        "and represent *structural* evidence (schema-valid, governance-tagged), "
        "not real model outputs. Replace with `--provider anthropic` for "
        "production evidence."
    )

    parts = [
        "---\n",
        "hide:\n",
        "  - toc\n",
        "---\n\n",
        "# Latest Evaluation Run\n\n",
        f"!!! info \"Maturity\"\n    {maturity_note}\n\n",
    ]

    for axis in sorted(latest):
        run_dir = latest[axis]

        # Copy findings.json
        src_json = run_dir / "findings.json"
        dst_json = docs_dir / f"latest-{axis}.json"
        shutil.copy(src_json, dst_json)
        print(f"[publish] copied {dst_json}")

        # Embed report body (replace H1 with ## Axis heading)
        report_path = run_dir / "report.md"
        if report_path.exists():
            body = report_path.read_text(encoding="utf-8")
            body = re.sub(r"^# .+$", f"## {axis.title()}", body, count=1, flags=re.MULTILINE)
            parts.append(body)
            parts.append(f"\n[Download findings JSON](latest-{axis}.json){{.md-button}}\n\n")

    (docs_dir / "latest-run.md").write_text("".join(parts), encoding="utf-8")
    print(f"[publish] wrote docs/evaluation/latest-run.md ({len(latest)} axes)")
    return 0


if __name__ == "__main__":
    sys.exit(publish())

#!/usr/bin/env python3
"""RAI Evaluation Engine — CLI entry point.

Usage
-----
python evaluate.py --axis toxicity --dry-run --seeds 5
python evaluate.py --axis truthfulness --dry-run --seeds 5

Artifacts written to out/<run_id>/
  findings.json   — one finding per prompt, full schema
  findings.sarif  — SARIF 2.1.0 for GitHub Advanced Security
  report.md       — human-readable markdown summary
"""
from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import secrets
import sys

from engine import ENGINE_VERSION


def _run_id() -> str:
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{ts}-{secrets.token_hex(3)}"


def _write_report(
    findings: list[dict],
    axis: str,
    run_id: str,
    provider: str,
    path: pathlib.Path,
) -> None:
    counts: dict[str, int] = {"confirmed": 0, "needs_review": 0, "rejected": 0}
    for f in findings:
        counts[f["status"]] = counts.get(f["status"], 0) + 1

    sorted_findings = sorted(findings, key=lambda x: x["score"], reverse=True)
    maturity_note = (
        "Maturity: `executable` — outputs derive from the "
        f"`{provider}` provider; replace with a live provider for production evidence."
    )

    lines = [
        f"# {axis.title()} Evaluation Report\n\n",
        f"Run: `{run_id}`  \n",
        f"{maturity_note}\n\n",
        "## Status summary\n\n",
        "| Status | Count |\n",
        "|---|---|\n",
    ]
    for status in ("confirmed", "needs_review", "rejected"):
        lines.append(f"| {status} | {counts[status]} |\n")

    lines.append("\n## Findings (sorted by score, descending)\n\n")
    lines.append("| Test ID | Category | Score | Status | Severity |\n")
    lines.append("|---|---|---|---|---|\n")
    for f in sorted_findings:
        lines.append(
            f"| {f['test_id']} "
            f"| {f['prompt']['category']} "
            f"| {f['score']:.3f} "
            f"| {f['status']} "
            f"| {f['severity']} |\n"
        )

    path.write_text("".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="RAI Evaluation Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--axis", choices=["toxicity", "truthfulness"], required=True,
        help="Evaluation axis to run",
    )
    parser.add_argument("--provider", default="mock", help="Model provider (default: mock)")
    parser.add_argument("--model", default="mock-v1", help="Model identifier")
    parser.add_argument("--prompts", default=None, help="Path to JSONL prompt file")
    parser.add_argument("--seeds", type=int, default=3, help="Number of seed repetitions (default: 3)")
    parser.add_argument("--include-text", action="store_true", help="Store prompt/response text in findings")
    parser.add_argument("--dry-run", action="store_true", help="Force mock provider; no network calls")
    parser.add_argument("--out", default="out", help="Output directory (default: out/)")
    args = parser.parse_args(argv)

    if args.dry_run:
        args.provider = "mock"

    run_id = _run_id()
    out_dir = pathlib.Path(args.out) / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    from engine.runners import RUNNERS, DEFAULT_PROMPTS
    from engine.models.client import get_provider
    from engine.emitters.sarif_emitter import write_sarif

    runner_fn = RUNNERS[args.axis]
    prompts_path = pathlib.Path(args.prompts) if args.prompts else DEFAULT_PROMPTS[args.axis]
    provider = get_provider(args.provider, args.model)
    seeds = list(range(args.seeds))

    print(
        f"[RAI-Eval v{ENGINE_VERSION}] axis={args.axis}  "
        f"provider={args.provider}  model={args.model}  "
        f"seeds={seeds}  run={run_id}"
    )

    findings = runner_fn(
        provider=provider,
        model=args.model,
        seeds=seeds,
        run_id=run_id,
        include_text=args.include_text,
        prompts_path=prompts_path,
    )

    # --- findings.json ---
    findings_path = out_dir / "findings.json"
    with findings_path.open("w", encoding="utf-8") as fh:
        json.dump(findings, fh, indent=2)
    print(f"[RAI-Eval] wrote {findings_path}  ({len(findings)} findings)")

    # --- schema validation (optional) ---
    schema_path = pathlib.Path(__file__).parent / "engine" / "schema" / "finding.schema.json"
    try:
        import jsonschema  # type: ignore[import]
        with schema_path.open(encoding="utf-8") as fh:
            schema = json.load(fh)
        for finding in findings:
            jsonschema.validate(finding, schema)
        print(f"[RAI-Eval] schema validation: PASSED ({len(findings)} findings validated)")
    except ImportError:
        print("[RAI-Eval] schema validation: SKIPPED (jsonschema not installed — pip install jsonschema)")
    except Exception as exc:
        print(f"[RAI-Eval] schema validation: FAILED — {exc}", file=sys.stderr)
        return 1

    # --- findings.sarif ---
    sarif_path = out_dir / "findings.sarif"
    write_sarif(findings, str(prompts_path), ENGINE_VERSION, sarif_path)
    print(f"[RAI-Eval] wrote {sarif_path}")

    # --- report.md ---
    report_path = out_dir / "report.md"
    _write_report(findings, args.axis, run_id, args.provider, report_path)
    print(f"[RAI-Eval] wrote {report_path}")

    statuses = [f["status"] for f in findings]
    print(
        f"[RAI-Eval] done — "
        f"confirmed={statuses.count('confirmed')}  "
        f"needs_review={statuses.count('needs_review')}  "
        f"rejected={statuses.count('rejected')}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

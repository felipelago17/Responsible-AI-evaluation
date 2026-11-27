# Agent Tooling Scan (MCP servers and skills)

The [AI-BOM](ai-bom.md) covers the model. This page covers what surrounds it: the MCP servers, tool descriptions and agent skills an agent can call. A clean model behind a poisoned tool description is still a failed deployment.

## Approach: ingest, don't embed

The framework scores the output of an external scanner. It does not vendor or run one. The reference scanner is Snyk's [agent-scan](https://github.com/snyk/agent-scan), which is Apache-2.0, needs a Snyk token, starts configured MCP servers when it scans, and does not take external contributions. Embedding it would mix licences (this repo is MIT), put credentials into CI, and let the evaluation harness execute untrusted servers.

```bash
uvx snyk-agent-scan@latest --json ~/.vscode/mcp.json > scan.json   # run separately, in isolation
```

```python
from benchmarks.agent_supply_chain import AgentSupplyChainAdapter
r = AgentSupplyChainAdapter().run(model=lambda p: p, config={"report_path": "scan.json"})
print(r.metrics)
```

## Metrics

| Metric | Meaning |
|---|---|
| `agent_supply_chain_risk_score` | 0–1, higher is riskier. Error-class findings weigh 1.0, warnings 0.3, unknown 0.1; saturating. |
| `error_findings` / `warning_findings` | Distinct (component, code) findings. |
| `gate_failed` | 1.0 if any error-class finding exists. Treat as a release blocker, independent of the score. |

## Issue-code categories

| Code | Category |
|---|---|
| E001 | Prompt injection / tool poisoning |
| E002 | Tool shadowing |
| E004 | Skill prompt injection |
| E006 | Malware payload |
| W007 | Insecure credential handling |
| W008 | Hardcoded secrets |
| W011 | Untrusted content |

These are the codes documented for agent-scan v0.5.x, which the project says it plans to deprecate in favour of scored risk indicators from v0.6. Update `CODE_CATEGORIES` when you adopt v0.6.

## Where it sits in scoring

It is a standalone gate. It is **not** in the weighted aggregate in [Scoring](../scoring.md), so published weights and existing results are unchanged. Report it beside the aggregate.

## Limitations

- The JSON schema of the scanner is documented as experimental. The parser is tolerant and flags `scanner_unvalidated_schema`; validate it against a real report before relying on numbers.
- Static findings do not show whether the model would actually follow a poisoned instruction. Pair with the injection tests in `tests/injection/` and [Robustness](../benchmarks/robustness.md).
- Scanner coverage and false-positive rates are the scanner's, not this framework's.

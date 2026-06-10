# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| 1.0.x | ✅ |

## Scope

This project is an evaluation framework, not a deployed service. Security issues may arise from:

- Dependency vulnerabilities in `requirements.txt`
- Benchmark data or prompts that could manipulate evaluator logic
- Evaluation harness issues that could produce misleading safety scores
- Disclosure of sensitive model outputs through the results schema

## Reporting a Vulnerability

**Please do not file public GitHub Issues for security vulnerabilities.**

Report vulnerabilities privately via [GitHub Security Advisories](https://github.com/felipelago17/Responsible-AI-evaluation/security/advisories/new) — these are visible only to maintainers.

Please include:

- A clear description of the vulnerability and its potential impact
- Steps to reproduce
- Any suggested fixes or mitigations
- Whether you would like to be credited in the changelog

## Response Timeline

| Stage | Target |
|---|---|
| Acknowledgement | Within 72 hours |
| Initial assessment | Within 7 days |
| Resolution or mitigation | Within 30 days for critical issues |

## Safe Harbor

Good-faith security research on this framework is welcomed. Researchers who identify and responsibly disclose vulnerabilities will not face legal action and will be credited in release notes. This aligns with the safe harbor principles for AI evaluation and red teaming outlined in [Longpre et al. (2024)](https://arxiv.org/abs/2403.04893).

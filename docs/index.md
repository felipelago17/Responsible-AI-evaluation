# Responsible AI Framework Comparison

Welcome to the **Open LLM Safety Evaluation** website, reformulated as an animated framework for comparing responsible AI principles across technical and governance standards.

This site compares principles using four benchmark-aligned axes:

- **Bias**
- **Toxicity**
- **Truthfulness**
- **Robustness** *(including Red Teaming)*

## Animated Principle Comparison

<div class="framework-grid">
  <article class="framework-card">
    <span class="principle-chip chip-bias">Bias</span>
    <h3>Fairness & Representation</h3>
    <p>Compare demographic and representational harms across technical benchmarks and governance frameworks.</p>
    <div class="metric-row">
      <div class="metric-label"><span>Benchmark maturity</span><strong>84</strong></div>
      <div class="metric-track"><div class="metric-fill" data-target="84"></div></div>
    </div>
    <div class="metric-row">
      <div class="metric-label"><span>Governance coverage</span><strong>79</strong></div>
      <div class="metric-track"><div class="metric-fill" data-target="79"></div></div>
    </div>
  </article>

  <article class="framework-card">
    <span class="principle-chip chip-toxicity">Toxicity</span>
    <h3>Harm Prevention</h3>
    <p>Track harmful output suppression and policy compliance signals for deployment readiness decisions.</p>
    <div class="metric-row">
      <div class="metric-label"><span>Benchmark maturity</span><strong>86</strong></div>
      <div class="metric-track"><div class="metric-fill" data-target="86"></div></div>
    </div>
    <div class="metric-row">
      <div class="metric-label"><span>Governance coverage</span><strong>82</strong></div>
      <div class="metric-track"><div class="metric-fill" data-target="82"></div></div>
    </div>
  </article>

  <article class="framework-card">
    <span class="principle-chip chip-truthfulness">Truthfulness</span>
    <h3>Factual Reliability</h3>
    <p>Assess hallucination risk, calibration drift, and consistency against disclosure and accountability expectations.</p>
    <div class="metric-row">
      <div class="metric-label"><span>Benchmark maturity</span><strong>80</strong></div>
      <div class="metric-track"><div class="metric-fill" data-target="80"></div></div>
    </div>
    <div class="metric-row">
      <div class="metric-label"><span>Governance coverage</span><strong>77</strong></div>
      <div class="metric-track"><div class="metric-fill" data-target="77"></div></div>
    </div>
  </article>

  <article class="framework-card">
    <span class="principle-chip chip-robustness">Robustness + Red Teaming</span>
    <h3>Adversarial Resilience</h3>
    <p>Unify perturbation resilience and red-team stress testing under one robustness principle, aligned with current RSP escalation logic.</p>
    <div class="metric-row">
      <div class="metric-label"><span>Benchmark maturity</span><strong>88</strong></div>
      <div class="metric-track"><div class="metric-fill" data-target="88"></div></div>
    </div>
    <div class="metric-row">
      <div class="metric-label"><span>ASL escalation relevance</span><strong>91</strong></div>
      <div class="metric-track"><div class="metric-fill" data-target="91" data-tone="warning"></div></div>
    </div>
  </article>
</div>

<p class="framework-legend">
Animated bars are comparative indicators for framework communication (not model scores).
</p>

## Governance Framework Lens (leveraging AI-regulatory-monitor taxonomy)

This comparison structure is designed to map each principle against:

- **NIST AI RMF** (GOVERN / MAP / MEASURE / MANAGE)
- **EU AI Act** (risk management, transparency, human oversight, incident reporting)
- **OECD AI Principles** (inclusive growth, human-centered values, transparency, robustness)
- **ISO/IEC 42001** (AI management system controls)
- **Corporate Responsible AI policies** (Anthropic, Google, Microsoft, IBM style commitments)

## Why this structure

- Compares technical benchmark outputs and governance obligations in one view
- Helps teams prioritize mitigation by principle instead of by isolated benchmark
- Supports benchmark-to-policy traceability for audit and compliance workflows

## Quick links

| Section | Description |
|---|---|
| [Methodology](methodology.md) | Evaluation workflow and principle-driven assessment method |
| [Bias](benchmarks/bias.md) | Fairness and representation analysis |
| [Toxicity](benchmarks/toxicity.md) | Harmful content and abuse prevention analysis |
| [Truthfulness](benchmarks/truthfulness.md) | Factual reliability and hallucination controls |
| [Robustness](benchmarks/robustness.md) | Adversarial resilience framework, including red teaming |
| [Red Teaming (within Robustness)](benchmarks/red-teaming.md) | Deep adversarial probing and escalation evidence |
| [Governance Mapping](governance_mapping.md) | Crosswalk to NIST AI RMF, EU AI Act, and RSP ASL tiers |

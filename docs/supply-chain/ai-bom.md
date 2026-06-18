# AI Bill of Materials (AI-BOM)

Template for documenting the full provenance of an AI system prior to evaluation and deployment. Complete all sections before beginning Phase 1 of the [Five-Phase Assessment](../methodology/five-phase-assessment.md). An incomplete AI-BOM is a fail condition for the Model Provenance Completeness Score.

!!! note "Format"
    This template should be completed as a Markdown file named `ai-bom-{model_id}-{version}-{date}.md` and stored in `results/{model_id}/`. Fields marked **[REQUIRED]** must be populated before evaluation begins. Fields marked **[IF APPLICABLE]** are required when the condition applies.

---

## Section 1 — Model Identity

| Field | Value | Status |
|---|---|---|
| Model name | | [REQUIRED] |
| Model version / release tag | | [REQUIRED] |
| Model architecture | | [REQUIRED] |
| Parameter count | | [REQUIRED] |
| Training compute (FLOPs) | | [REQUIRED] |
| Above 10²⁶ FLOPs threshold? | Yes / No / Unknown | [REQUIRED] |
| Model card URL | | [REQUIRED] |
| System card URL | | [IF APPLICABLE] |
| Primary intended use | | [REQUIRED] |
| Known out-of-scope uses | | [REQUIRED] |
| Developer organisation | | [REQUIRED] |
| Deploying organisation (if different) | | [IF APPLICABLE] |

---

## Section 2 — Model Provenance

| Field | Value | Status |
|---|---|---|
| Base model identifier (if fine-tuned) | | [IF APPLICABLE] |
| Base model version hash / SHA | | [IF APPLICABLE] |
| Base model source (HuggingFace Hub ID, internal registry URL, etc.) | | [IF APPLICABLE] |
| Base model licence | | [IF APPLICABLE] |
| Fine-tuning applied? | Yes / No | [REQUIRED] |
| Fine-tuning dataset identifier(s) | | [IF APPLICABLE] |
| Fine-tuning dataset version / hash | | [IF APPLICABLE] |
| RLHF applied? | Yes / No | [REQUIRED] |
| RLHF preference dataset identifier | | [IF APPLICABLE] |
| RLHF reward model identifier | | [IF APPLICABLE] |
| Weight hash (SHA-256 of model weights file) | | [REQUIRED] |
| Weight signature (cryptographic signing authority) | | [IF APPLICABLE] |

!!! warning "Supply Chain Integrity"
    Base model weight hashes must be verified against the upstream registry before evaluation. A hash mismatch indicates potential supply chain compromise (ATLAS AML.T0040) and must block the evaluation until resolved.

---

## Section 3 — Training Data Sources

| Dataset Name | Version / Hash | Size | Personal Data? | Licence | Data Card URL |
|---|---|---|---|---|---|
| | | | Yes / No | | |
| | | | Yes / No | | |
| | | | Yes / No | | |

### Data Governance Fields

| Field | Value | Status |
|---|---|---|
| Data subjects identified? | Yes / No | [REQUIRED] |
| Consent mechanism documented? | Yes / No / N/A | [REQUIRED] |
| Data retention period | | [REQUIRED] |
| Sensitive categories present (per GDPR Art. 9)? | Yes / No | [REQUIRED] |
| DPIA conducted? | Yes / No / In progress | [IF APPLICABLE] |
| DPIA reference / document ID | | [IF APPLICABLE] |

---

## Section 4 — Library and Container Versions

| Component | Version | Source / Registry | Integrity Hash |
|---|---|---|---|
| Python | | | |
| PyTorch / TensorFlow / JAX | | | |
| Transformers (HuggingFace) | | | |
| Accelerate / DeepSpeed / FSDP | | | |
| Tokenizer library | | | |
| CUDA version | | | |
| Container base image | | | |
| Container image digest | | | |
| Inference server (vLLM, TGI, etc.) | | | |

!!! note "Dependency Pinning"
    All library versions must be pinned (not range-specified) in `requirements.txt` or `pyproject.toml` and match the entries above. Unpinned dependencies are a supply chain risk (ISO, 2022).

---

## Section 5 — Adversarial Test Attestation

Record the outcome of each required evaluation procedure from the [Test Catalogue](../evaluation/test-catalogue.md).

| Test Procedure | Date Completed | Outcome | Results File | Notes |
|---|---|---|---|---|
| Adversarial robustness testing (AdvGLUE + PromptBench) | | Pass / Fail / Not run | | |
| Differential privacy verification | | Pass / Fail / Not run | | |
| Input sanitisation testing (injection + jailbreak) | | Pass / Fail / Not run | | |
| Membership inference red-team exercise | | Pass / Fail / Not run | | |
| Model extraction red-team exercise | | Pass / Fail / Not run | | |
| Benchmark accuracy evaluation (full suite) | | Pass / Fail / Not run | | |
| Backdoor scanning | | Pass / Fail / Not run | | |
| Bias audit (StereoSet + CrowS-Pairs + WinoBias) | | Pass / Fail / Not run | | |

**Attestation sign-off:**

| Role | Name | Date | Signature |
|---|---|---|---|
| Evaluation Lead | | | |
| Security / Privacy Reviewer | | | |
| Approver | | | |

---

## Section 6 — Regulatory and Export Control Classification

| Field | Value | Status |
|---|---|---|
| Jurisdictions of deployment | | [REQUIRED] |
| EAR classification (3A090 / 4E091 / N/A) | | [REQUIRED] |
| Above AI Diffusion Framework licensing threshold? | Yes / No | [REQUIRED] |
| Export licence required? | Yes / No / Pending | [REQUIRED] |
| UAE DESC Law 15/2024 obligations? | Yes / No / Under review | [IF APPLICABLE] |
| EU AI Act risk category (Unacceptable / High / Limited / Minimal) | | [REQUIRED] |
| FRIA completed (EU AI Act Art. 27)? | Yes / No / Not required | [IF APPLICABLE] |
| ISO/IEC 42001 certification status | Certified / In progress / Not certified | [IF APPLICABLE] |
| UNESCO EIA completed? | Yes / No / In progress | [IF APPLICABLE] |
| UNESCO EIA document reference | | [IF APPLICABLE] |

---

## Completeness Checklist

Use this checklist to compute the [Model Provenance Completeness Score (MPCS)](../evaluation/metrics.md#3-model-provenance-completeness-score-mpcs).

- [ ] Section 1 — All REQUIRED fields populated (12 fields)
- [ ] Section 2 — All REQUIRED fields populated; IF APPLICABLE fields completed where condition applies
- [ ] Section 3 — All training datasets listed with version hash; data governance fields complete
- [ ] Section 4 — All library versions pinned and integrity hashes recorded
- [ ] Section 5 — All 8 test procedures completed or formally deferred with written rationale; sign-off obtained
- [ ] Section 6 — All REQUIRED regulatory fields populated; IF APPLICABLE fields completed where condition applies

**MPCS = (checked boxes / 28 required fields) × 100**

---

## References

- Government of Dubai (2024) *Law No. (15) of 2024 Concerning the Dubai Electronic Security Centre*. Available at: https://dlp.dubai.gov.ae (Accessed: 18 June 2026).
- ISO (2022) *ISO/IEC 27005:2022 Information security, cybersecurity and privacy protection — Guidance on managing information security risks*. Geneva: International Organization for Standardization.
- ISO/IEC (2023) *ISO/IEC 42001:2023 — Artificial Intelligence: Management System*. International Organisation for Standardisation.
- NIST (2024b) *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1). Gaithersburg, MD: National Institute of Standards and Technology. Available at: https://doi.org/10.6028/NIST.AI.600-1 (Accessed: 18 June 2026).
- RAND Corporation (2025) *Understanding the Artificial Intelligence Diffusion Framework: Can Export Controls Create a U.S.-Led Global Artificial Intelligence Ecosystem?* Available at: https://www.rand.org/pubs/perspectives/PEA3776-1.html (Accessed: 18 June 2026).
- U.S. Department of Commerce, Bureau of Industry and Security (2025) 'Implementation of Additional Due Diligence Measures for Advanced Computing Integrated Circuits; Amendments and Clarifications', *Federal Register*, 90(10). Available at: https://www.federalregister.gov (Accessed: 18 June 2026).

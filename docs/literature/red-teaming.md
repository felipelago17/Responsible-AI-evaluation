# AI Red Teaming, Safety Evaluation & Adversarial Testing

Annotated bibliography covering red teaming methodologies, safety evaluation frameworks, and adversarial testing practices for AI systems. Relevant to `benchmarks/cybergym_glasswing.py`, `evaluation/agentic_autonomy.py`, and `evaluation/disclosure_compliance.py`.

---

## Longpre et al. (2024) — A Safe Harbor for AI Evaluation and Red Teaming

**Citation:** Longpre, S., et al. (2024). *A Safe Harbor for AI Evaluation and Red Teaming*. arXiv:2403.04893.  
**URL:** <https://arxiv.org/abs/2403.04893>

Argues for legal and institutional protections for researchers conducting good-faith AI red teaming and safety evaluations. The paper examines how legal uncertainty — particularly around computer fraud and IP law — creates a chilling effect on adversarial testing, and proposes safe harbor principles analogous to those in cybersecurity research. Directly informs the disclosure compliance and governance dimensions of this framework, particularly `evaluation/disclosure_compliance.py`.

---

## Ahmad et al. (2025) — OpenAI’s Approach to External Red Teaming

**Citation:** Ahmad, B., et al. (2025). *OpenAI’s Approach to External Red Teaming for AI Models and Systems*. arXiv:2503.16431.  
**URL:** <https://arxiv.org/abs/2503.16431>

Documents OpenAI’s operational methodology for coordinating external red teaming campaigns across frontier models, covering team composition, threat model scoping, finding classification, and escalation procedures. Provides a practitioner reference for structured adversarial probing and informs the refusal-rate and zero-day risk metrics in the red-teaming evaluation dimension.

---

## CSET (2025) — AI Red-Teaming Design: Threat Models and Tools

**Citation:** Center for Security and Emerging Technology. (2025). *AI Red-Teaming Design: Threat Models and Tools*. Georgetown University CSET.  
**URL:** <https://cset.georgetown.edu/article/ai-red-teaming-design-threat-models-and-tools/>

A policy-oriented technical report cataloguing threat models applicable to AI red teaming — spanning misuse, misalignment, systemic risk, and dual-use concerns — alongside a comparative survey of automated and human-in-the-loop adversarial testing tooling. Informs the threat model taxonomy underlying `benchmarks/cybergym_glasswing.py` and the agentic autonomy risk evaluator.

---

## AI Security & Safety Directory (2026) — AI Model Evaluation

**Citation:** AI Security & Safety Directory. (2026). *AI Model Evaluation*. AISecurity AndSafety.org.  
**URL:** <https://aisecurityandsafety.org/en/guides/ai-model-evaluation/>

A practitioner-facing directory consolidating evaluation methodologies, benchmark resources, and tooling for AI safety and security assessment. Serves as a living cross-reference for the benchmark adapter library, mapping this framework’s evaluation dimensions against the broader landscape of community-maintained evaluation resources.

---

## IMDA (2026) — ISO/IEC 42119-8: Testing and Red Teaming of Generative AI Systems

**Citation:** Infocomm Media Development Authority (IMDA). (2026). *Singapore Champions New Global AI Testing Standardisation Efforts* [Press Release].  
**URL:** <https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/singapore-champions-new-global-ai-testing-standardisation-efforts>

Announces Singapore’s leadership in developing ISO/IEC 42119-8, a forthcoming international standard formalising testing and red teaming of generative AI systems as a component of AI conformance assurance. The standard’s scope overlaps significantly with the red-teaming and robustness evaluation dimensions of this framework.

---

## SGS (2026) — ISO/IEC 42119 Series

**Citation:** SGS Group. (2026). *Announcing the ISO/IEC 42119 Series: A New Era for AI Testing and Assurance*.  
**URL:** <https://www.sgs.com/en/news/2026/01/announcing-the-iso-iec-42119-series-a-new-era-for-ai-testing-and-assurance>

Overview of the full ISO/IEC 42119 series — a suite of international standards covering AI testing methodologies including robustness testing, bias evaluation, and red teaming. Provides the normative standards context for this framework’s five evaluation dimensions and supports future conformance mapping in `docs/governance_mapping.md`.

---

## Yadav & Yadav (2026) — The Mirage of LLM Guardrails

**Citation:** Yadav, D., & Yadav, A. (2026). *The Mirage of LLM Guardrails: A Case Study in AI-Assisted Medical Note Manipulation*. arXiv:2607.24859 [cs.CR]. Penn State / AAAI.  
**URL:** <https://arxiv.org/abs/2607.24859>

Demonstrates that LLM guardrails are modality-dependent rather than intent-dependent: Claude Sonnet 4.6 refused 100 % of image-based requests but only 7 % of semantically identical inline-text requests; Gemini 2.5 refused 0 % across all modalities. The study evaluates 2,100 document-manipulation attempts per model (6,300 total) using a 2 × 2 factorial prompt design (document framing × field reference type) across three input modalities (PNG, PDF, inline text). Layered metrics — refusal rate (RQ1), Field Substitution Accuracy and Collateral Edit Rate (RQ2), and a 116-participant believability study near chance detection accuracy (RQ3) — make this a clean, reproducible template for domain-specific guardrail evaluation.

**Methodology notes:** The FSA/CER pair is a broadly reusable construct: FSA measures semantic correctness of the requested change; CER measures preservation of unrelated content. The 2 × 2 factorial design efficiently surfaces prompt-framing vs modality effects without confounding them. Inter-annotator agreement (Cohen’s κ = 0.604) is reported for image outputs.

**Governance crosswalk:**

| Framework | Mapping |
|---|---|
| **NIST AI RMF** | MEASURE 2.7 (security/resilience evaluation) and MANAGE 4.1 (post-deployment monitoring): the modality gap shows single-modality red-teaming is insufficient — evaluation must cover the full input surface. |
| **EU AI Act** | Health-adjacent deployment pushes toward high-risk classification (Annex III); Art. 15 accuracy/robustness/cybersecurity obligations are directly implicated where guardrails fail on representation format rather than intent. GPAI providers face adversarial-testing requirements under the Code of Practice. |
| **ASL / capability thresholds** | Illustrates that dangerous-capability evaluation (94.7 % FSA on precise document manipulation) and safeguard evaluation (modality-dependent refusal) are separable measurements — both belong in a deployment decision. |
| **ISO/IEC 42001** | Clause 6.1 risk assessment should treat vendor guardrails as an unverified claim absent independent adversarial evidence covering all input modalities. |

---

*See also: [Benchmarks: Red Teaming](../benchmarks/red-teaming.md) for the framework’s internal red-teaming methodology documentation.*

# AI Governance Frameworks, Standards & Regulatory Landscape

Annotated bibliography of key governance frameworks, regulatory instruments, and standards relevant to responsible AI evaluation. Entries are organised by jurisdiction and inform the governance alignment documented in `docs/governance.md` and `docs/governance_mapping.md`.

---

## Global / Multilateral

### OECD (2026) — Hiroshima AI Process Reporting Framework

**Citation:** OECD. (2026). *Hiroshima AI Process Reporting Framework*. OECD.AI.  
**URL:** <https://oecd.ai/en/hiroshima>

The reporting framework operationalising the G7 Hiroshima AI Process commitments, providing structured indicators for organisations to demonstrate compliance with the Hiroshima Code of Conduct. Relevant to the governance and scoring dimensions of this framework, particularly the mapping of evaluation outputs to accountability and transparency indicators.

---

### Government of Japan (2023) — Hiroshima Process International Guiding Principles

**Citation:** Government of Japan, Ministry of Foreign Affairs. (2023). *Hiroshima Process International Guiding Principles for Advanced AI System Developers*.  
**URL:** <https://www.mofa.go.jp/files/100573471.pdf>

The foundational guiding principles adopted by G7 leaders for advanced AI developers, covering risk identification, transparency, security testing, and responsible disclosure. The principles provide a normative baseline that maps directly to the five evaluation dimensions — bias, toxicity, truthfulness, robustness, and red teaming — assessed by this framework.

---

### OECD (2025) — Framework to Monitor Hiroshima AI Code of Conduct

**Citation:** OECD. (2025, February). *OECD Launches Global Framework to Monitor Application of G7 Hiroshima AI Code of Conduct* [Press Release].  
**URL:** <https://www.oecd.org/en/about/news/press-releases/2025/02/oecd-launches-global-framework-to-monitor-application-of-g7-hiroshima-ai-code-of-conduct.html>

Announces the OECD's monitoring framework for tracking organisational adoption of the Hiroshima Code of Conduct commitments at scale. The structured indicators in this framework inform the reporting schema used in `results/` versioned evaluation outputs, supporting longitudinal compliance tracking.

---

### ISO (2024–2025) — ISO/IEC 5259 Series: AI Data Quality

**Citation:** ISO/IEC. (2024–2025). *ISO/IEC 5259 Series — Artificial Intelligence: Data Quality*. International Organization for Standardization.  
**URL:** <https://www.iso.org/publication/PUB200525.html>

Multi-part standard establishing data quality requirements and measurement methodologies for AI training and evaluation datasets. Directly relevant to the dataset provenance and versioning practices documented in `docs/governance.md`, and to the reproducibility guarantees required by the evaluation harness.

---

### OECD (2024) — Recommendation of the Council on AI

**Citation:** OECD. (2024). *Recommendation of the Council on Artificial Intelligence*. OECD Legal Instruments, OECD-LEGAL-0449.  
**URL:** <https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449>

The updated OECD AI Principles — the foundational international soft-law instrument for responsible AI, endorsed by 46+ countries. The five OECD principles (inclusive growth, human-centred values, transparency, robustness, accountability) map directly to the evaluation dimensions of this framework and provide the normative basis for `docs/governance_mapping.md`.

---

### UN (2024) — Governing AI for Humanity: Final Report

**Citation:** United Nations. (2024). *Governing AI for Humanity: Final Report*. UN Secretary-General's High-Level Advisory Body on AI.  
**URL:** <https://www.un.org/sites/un2.un.org/files/governing_ai_for_humanity_final_report_en.pdf>

The UN High-Level Advisory Body's report outlining an international governance architecture for AI, including proposals for a multistakeholder advisory body, capacity-building mechanisms, and principles for inclusive global AI governance. Provides the geopolitical context for interpreting evaluation results across jurisdictions and informs the framework's approach to non-discriminatory and globally applicable evaluation criteria.

---

### UNESCO (2024) — Recommendation on the Ethics of AI

**Citation:** UNESCO. (2024). *About UNESCO*. United Nations Educational, Scientific and Cultural Organization.  
**URL:** <https://www.unesco.org/en/brief>

UNESCO's 2021 Recommendation on the Ethics of Artificial Intelligence — the first global normative instrument on AI ethics, adopted by all 193 member states — establishes values and principles covering human dignity, environmental sustainability, transparency, and accountability. The Recommendation's emphasis on bias auditing and non-discrimination directly underpins the bias and toxicity evaluation dimensions of this framework.

---

### AI Governance Directory (2026) — Global AI Governance Frameworks

**Citation:** AI Governance Directory. (2026). *Global AI Governance Frameworks*. AIGovernance.com.  
**URL:** <https://aigovernance.com/jurisdiction/global>

A curated, regularly updated directory of international AI governance instruments, mapping frameworks by jurisdiction, binding status, sector scope, and maturity. Useful for maintaining the accuracy of `docs/governance_mapping.md` as the global regulatory landscape evolves.

---

### AI Safety Directory (2026) — AI Governance Frameworks Compared

**Citation:** AI Security & Safety Directory. (2026). *AI Governance Frameworks Compared*. AISecurity AndSafety.org.  
**URL:** <https://aisecurityandsafety.org/en/guides/ai-governance-frameworks-compared/>

A comparative analysis of major AI governance frameworks — EU AI Act, NIST AI RMF, ISO/IEC 42001, OECD Principles — highlighting areas of convergence and divergence across risk classification, conformity assessment requirements, and evaluation obligations. Supports the multi-framework alignment approach in `docs/governance_mapping.md`.

---

## United States

### NIST (2023) — AI Risk Management Framework

**Citation:** National Institute of Standards and Technology. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. U.S. Department of Commerce.  
**URL:** <https://www.nist.gov/itl/ai-risk-management-framework>  
**DOI:** <https://doi.org/10.6028/NIST.AI.100-1>

The primary U.S. voluntary framework for managing AI risks across the full AI lifecycle, structured around four core functions: Govern, Map, Measure, and Manage. The Measure function — which covers bias, robustness, and safety testing — maps directly to this framework's evaluation dimensions and provides the risk categorisation taxonomy used in `docs/scoring.md`.

---

### NIST (2024) — Generative AI Profile: NIST AI 600-1

**Citation:** National Institute of Standards and Technology. (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*. NIST AI 600-1. U.S. Department of Commerce.  
**URL:** <https://doi.org/10.6028/NIST.AI.600-1>

An AI RMF profile specifically addressing generative AI risks, covering hallucination, data privacy, bias amplification, malicious use, and autonomous agent risks. The 12 generative AI risk categories defined in this profile directly inform the benchmark selection and scoring rubrics for the truthfulness, red teaming, and agentic autonomy dimensions of this framework.

---

### Colorado General Assembly (2024) — Senate Bill 24-205: Consumer Protections in Interactions with AI

**Citation:** Colorado General Assembly. (2024). *Senate Bill 24-205: Consumer Protections in Interactions with Artificial Intelligence Systems*. 74th General Assembly.  
**URL:** <https://leg.colorado.gov/bills/sb24-205>

The first U.S. state law imposing obligations on developers and deployers of high-risk AI systems, requiring algorithmic impact assessments, transparency notices, and anti-discrimination protections for consequential decisions. Serves as a U.S. state-level regulatory reference point for the bias and governance evaluation dimensions, complementing the federal NIST AI RMF.

---

## European Union

### European Commission (2019) — Ethics Guidelines for Trustworthy AI

**Citation:** High-Level Expert Group on Artificial Intelligence. (2019). *Ethics Guidelines for Trustworthy AI*. European Commission.  
**URL:** <https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai>

The foundational EU document establishing seven requirements for trustworthy AI: human agency, technical robustness, privacy, transparency, diversity and non-discrimination, societal wellbeing, and accountability. These requirements were the conceptual precursor to the EU AI Act and directly map to the five evaluation dimensions — bias, robustness, and truthfulness in particular — assessed by this framework.

---

### European Commission (2025) — The European Approach to Artificial Intelligence

**Citation:** European Commission. (2025). *The European Approach to Artificial Intelligence*. Digital Strategy.  
**URL:** <https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence>

Overview of the EU's comprehensive AI policy ecosystem, encompassing the AI Act, AI Office, coordinated AI plan, and investment strategy. Provides the institutional context for interpreting the EU AI Act's conformity assessment requirements and their implications for evaluation frameworks like this one.

---

### EDPS (n.d.) — History of the GDPR

**Citation:** European Data Protection Supervisor. (n.d.). *History of the General Data Protection Regulation*. EDPS.  
**URL:** <https://www.edps.europa.eu/data-protection/data-protection/legislation/history-general-data-protection-regulation_en>

Documents the legislative history of the GDPR — the EU's primary data protection regulation — which underpins the data governance obligations applicable to AI systems processing personal data. Relevant to the dataset provenance controls, retention policies, and privacy-by-design principles documented in `docs/governance.md`.

---

### European Parliament (2023) — EU AI Act: First Regulation on AI

**Citation:** European Parliament. (2023). *EU AI Act: First Regulation on Artificial Intelligence*. European Parliament Topics.  
**URL:** <https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence>

Explanatory overview of the EU AI Act's risk-based classification system — prohibited practices, high-risk systems, limited-risk systems — and its conformity assessment requirements. The Act's mandatory evaluation obligations for high-risk AI systems (Annex III) provide the primary regulatory motivation for the bias, robustness, and transparency evaluation dimensions of this framework.

---

## United Arab Emirates

### UAE Government (2024) — UAE National AI Strategy 2031

**Citation:** Government of the United Arab Emirates. (2024). *UAE National Strategy for Artificial Intelligence 2031*.  
**URL:** <https://ai.gov.ae/strategy/>

The UAE's national AI strategy targeting top-ten global AI status by 2031, covering priority sectors, talent development, data infrastructure, and regulatory enablement. The strategy's emphasis on ethical AI and international standards alignment contextualises the governance evaluation dimension for organisations deploying AI systems in the UAE market.

---

### DIFC Authority (2024) — Artificial Intelligence Regulatory Framework

**Citation:** Dubai International Financial Centre Authority. (2024). *DIFC Artificial Intelligence Regulatory Framework*. DIFC.  
**URL:** <https://www.difc.ae/business/laws-regulations/legal-database/difc-ai-regime/>

The DIFC's AI regulatory regime governing entities operating within Dubai's international financial free zone, covering obligations around explainability, accountability, bias mitigation, human oversight, and data governance for AI systems used in financial services. As a sector-specific binding instrument within a major Gulf financial hub, it is a key reference point for organisations subject to DIFC jurisdiction deploying high-stakes AI systems — relevant to the fairness and robustness evaluation dimensions of this framework.

---

### UAE TDRA (2024) — AI Governance in Telecommunications and Digital Government

**Citation:** Telecommunications and Digital Government Regulatory Authority (TDRA). (2024). *Artificial Intelligence*. UAE TDRA.  
**URL:** <https://tdra.gov.ae/en/aict/sectors/AI>

The TDRA is the UAE federal authority responsible for telecommunications regulation and digital government transformation, including oversight of AI adoption across government services and the telecom sector. Its AI governance guidance covers responsible deployment principles, risk assessment obligations, and alignment with the UAE National AI Strategy 2031, providing a federal regulatory context complementary to the DIFC's financial-sector regime.

---

### Smart Dubai (2021) — Dubai AI Principles

**Citation:** Smart Dubai. (2021). *Dubai AI Principles*. Government of Dubai.  
**URL:** <https://www.smartdubai.ae/>

Smart Dubai — the emirate's government digitalisation authority — published the Dubai AI Principles establishing ethical guidelines for AI deployment across government services and smart city infrastructure. The principles cover transparency, fairness, accountability, privacy, and human oversight, forming the emirate-level ethical baseline that complements the national UAE AI Strategy and the DIFC's sector-specific obligations. Relevant to bias, toxicity, and governance evaluation dimensions for organisations operating within Dubai's smart city ecosystem.

---

*See also: [docs/governance.md](../docs/governance.md) and [docs/governance_mapping.md](../docs/governance_mapping.md) for the framework's internal governance documentation.*

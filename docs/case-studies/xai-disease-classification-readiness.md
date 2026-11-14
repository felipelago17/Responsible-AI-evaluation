# Case Study — Explainable AI for Disease Classification: Explanation Is Not Evidence of Readiness

`Healthcare · Explainability · Validation · Reproducibility · Release governance`

## Summary

Memon, Ebrahimi, Shaikh and Wiil (2026) reviewed 5,005 machine-learning disease-classification studies from 2019 to 2025 and found 105 that used explainable AI (XAI). They scored those 105 on a 13-item checklist derived from the Clinician-informed XAI Evaluation Checklist with Metrics (CLIX-M) and the XAI 2.0 manifesto. No study met all 13 items. For this framework the case is a clear example of a gap between *producing* an explanation and *evaluating* it, and between *reporting performance* and *showing readiness*.

## Key facts

| Item | Detail |
|---|---|
| Paper | Memon, S. A., Ebrahimi, A., Shaikh, M. & Wiil, U. K. (2026). *BMC Medical Informatics and Decision Making*, 26:455. DOI 10.1186/s12911-026-03750-4 |
| Evidence base | 5,005 records screened across Web of Science, PubMed, IEEE Xplore and Scopus; 105 XAI studies included |
| Models and methods | 131 models in 12 architecture families; 27 XAI techniques; heatmap-style gradient methods most common (78 studies) |
| Explanation evaluated | 9 of 105 (8.5%) |
| Any clinical validation | Fewer than one in four |
| Reader or usability studies | 2 |
| Tool tested as a decision aid | 1 |
| Retrospective design | About 80% |
| Code shared | About 10% |
| Checklist result | Mean 9.07 of 13; none met all 13. Weakest items: stated intended user and use, explanation robustness, human-centred evaluation, and risks and limitations |

## What it shows

- **Explanations are outputs to be tested, not features to be listed.** Only a small minority of studies measured explanation quality. The methods the review catalogues for doing so include overlap with expert annotations (intersection over union), pointing-game localisation, deletion and insertion curves, model-randomisation checks and blinded expert scoring.
- **Internal results overstate readiness.** Several studies reported AUC of 0.97 to 1.00 on development data, and the authors flag leakage and overfitting as likely contributors. Two studies that did validate externally saw AUC fall to 0.69–0.76, which the authors cite as the generalisation problem in miniature.
- **Reproducibility is thin.** With about one study in ten sharing code, independent re-evaluation is mostly impossible.
- **Stating the user and the risks is the most-missed step.** The checklist items that cost the least to satisfy, naming the intended user and writing down the limits, were among the least met.
- **A checklist score is not readiness.** The authors say so themselves: the score reflects reported evidence of readiness-related traits and is not proof that a system can be deployed.

## Mapping to this framework

This mapping is the framework's reading of the review; it is not taken from the paper.

| Finding | Framework element |
|---|---|
| Explanation quality rarely measured | [Metrics and KPIs](../evaluation/metrics.md) and the [test catalogue](../evaluation/test-catalogue.md): add explanation faithfulness and stability as measured items, not narrative claims |
| High internal, lower external performance | [Scoring](../scoring.md) and [limitations](../limitations.md): report in-distribution and out-of-distribution results separately; ground-truth and domain-coverage limits |
| Heatmaps assumed to be clinically meaningful | [Five-phase assessment](../methodology/five-phase-assessment.md), phase 3 (control effectiveness): a control counts only when its effectiveness has been tested |
| Intended user and use not stated | Phase 1 (asset and context identification): name the user, the decision supported and the setting before scoring |
| Risks of the explanation not discussed | Phase 4 (risk analysis): treat misleading explanations as a risk in their own right |
| Little shared code | [AI bill of materials](../supply-chain/ai-bom.md) and [release governance](../governance/release-governance.md): reproducibility and provenance as release conditions |
| Clinician-in-the-loop evidence missing | [Governance mapping](../governance_mapping.md): human-oversight and user-evaluation evidence for high-risk uses |

## Controls to adopt

| Control | Practice |
|---|---|
| Separate performance from explanation | Score the model and its explanations independently; a high model score does not carry over |
| Test explanation faithfulness | Use at least one perturbation-based test (for example deletion or insertion) and one test against expert annotation where ground truth exists |
| Test stability | Check whether explanations change under small input changes or repeated runs |
| Report external validation | Present results from sites, devices or populations not used in development, and say where none exist |
| Capture user evaluation | Record clinician or user review of explanations, including disagreements |
| Write down the limits | State intended user, setting, and known explanation failure modes in the evaluation record |
| Share what can be shared | Publish code, pre-processing and configuration, or document why not |
| Do not treat a checklist as a pass mark | Use readiness checklists to find gaps, not to certify |

## Caveats

- This is a single systematic review, limited to four databases and English-language studies from 2019 to 2025.
- The checklist is the authors' adaptation of CLIX-M. Quality assessment used a single reviewer with predetermined criteria and no inter-rater statistic.
- The paper's external-validation counts differ by place: the abstract gives 21.0%, Table 8 lists 14 studies, and Table 9 lists four external-cohort studies among 22 across all clinical-validation types (also about 21%). Check the table before citing a figure for external validation specifically.
- The review concerns disease classification, mostly imaging. Conclusions about other domains or modalities should not be drawn from it.
- The paper is licensed CC BY-NC-ND. This note paraphrases findings and does not reproduce its text or tables.

## Sources

- Memon, S. A., Ebrahimi, A., Shaikh, M. & Wiil, U. K. (2026). Explainable AI-based techniques for disease classification: a systematic review and future work. *BMC Medical Informatics and Decision Making*, 26:455. <https://doi.org/10.1186/s12911-026-03750-4>

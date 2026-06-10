# Truthfulness, Hallucination & Factual Accuracy in LLMs

Annotated bibliography covering truthfulness benchmarks, hallucination detection methods, and factual consistency evaluation for LLMs. Relevant to the truthfulness evaluation dimension and the `benchmarks/truthfulqa/` adapter.

---

## Lin et al. (2022) — TruthfulQA: Measuring How Models Mimic Human Falsehoods

**Citation:** Lin, S., Hilton, J., & Evans, O. (2022). *TruthfulQA: Measuring How Models Mimic Human Falsehoods*. arXiv:2109.07958.  
**URL:** <https://arxiv.org/abs/2109.07958>

Introduces TruthfulQA, a benchmark of 817 questions spanning 38 categories designed to elicit false beliefs that humans commonly hold — conspiracy theories, misconceptions, fiction, and unverified claims. TruthfulQA is the primary benchmark for the truthfulness evaluation dimension in this framework, implemented in `benchmarks/truthfulqa/` with both MC1 (single true answer) and MC2 (multiple true answers) evaluation modes. Also referenced in `CITATION.cff`.

---

## Maynez et al. (2020) — On Faithfulness and Factuality in Abstractive Summarisation

**Citation:** Maynez, J., Narayan, S., Bohnet, B., & McDonald, R. (2020). *On Faithfulness and Factuality in Abstractive Summarization*. arXiv:2005.00661.  
**URL:** <https://arxiv.org/abs/2005.00661>

A large-scale human annotation study distinguishing intrinsic hallucinations (contradictions of source material) from extrinsic hallucinations (unsupported additions) in neural abstractive summarisation. Establishes the core terminology — faithfulness, factuality, hallucination — that underpins the conceptual framing of the truthfulness evaluation dimension.

---

## Manakul et al. (2023) — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection

**Citation:** Manakul, P., Liusie, A., & Gales, M. J. F. (2023). *SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models*. arXiv:2303.08896.  
**URL:** <https://arxiv.org/abs/2303.08896>

Introduces SelfCheckGPT, a sampling-based approach for detecting hallucinations without external databases. The method samples multiple stochastic responses and measures consistency — factual statements appear consistently, while hallucinations vary. Applicable as a complementary hallucination signal alongside TruthfulQA in the truthfulness evaluation dimension.

---

## Min et al. (2023) — FActScore: Fine-grained Atomic Evaluation of Factual Precision

**Citation:** Min, S., Krishna, K., Lyu, X., Lewis, M., Yih, W-T., Koh, P. W., Iyyer, M., Zettlemoyer, L., & Hajishirzi, H. (2023). *FActScoring: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation*. arXiv:2305.14251.  
**URL:** <https://arxiv.org/abs/2305.14251>

Introduces FActScore, which decomposes long-form generated text into atomic claims and verifies each against a knowledge source. Provides a more granular factuality signal than binary truthfulness labels, enabling per-sentence hallucination rate estimation. Relevant for extending the framework’s truthfulness evaluation to open-ended generation tasks beyond multiple-choice benchmarks.

---

## Rawte et al. (2023) — A Survey of Hallucination in Large Foundation Models

**Citation:** Rawte, V., Sheth, A., & Das, A. (2023). *A Survey of Hallucination in Large Foundation Models*. arXiv:2309.05922.  
**URL:** <https://arxiv.org/abs/2309.05922>

A broad survey cataloguing hallucination types, causes, detection methods, and mitigation strategies across language, vision-language, and audio models. Organises hallucinations into factual inconsistency, faithfulness, and commonsense categories, reviewing 30+ mitigation approaches. Provides comprehensive taxonomic context for the truthfulness evaluation dimension and guides future benchmark adapter selection.

---

## Zhang et al. (2023) — Siren’s Song in the AI Ocean: A Survey on Hallucination in LLMs

**Citation:** Zhang, Y., Li, Y., Cui, L., et al. (2023). *Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models*. arXiv:2309.01219.  
**URL:** <https://arxiv.org/abs/2309.01219>

Systematic survey of hallucination in LLMs covering causes (knowledge gaps, training data noise, decoding strategies), detection benchmarks (TruthfulQA, FActScore, HaluEval), and mitigation approaches (retrieval augmentation, RLHF, chain-of-thought). Complements Rawte et al. with specific focus on LLMs and provides a structured framework for expanding the truthfulness evaluation dimension in future releases.

---

*See also: [Benchmarks: Truthfulness](../benchmarks/truthfulness.md) for the framework’s internal truthfulness evaluation documentation.*

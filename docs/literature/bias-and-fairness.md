# Bias & Fairness in AI: Measurement, Detection & Mitigation

Annotated bibliography covering bias measurement methodologies, fairness benchmarks, and mitigation techniques for NLP and LLM systems. Relevant to the bias evaluation dimension and `benchmarks/membench_rai.py`.

---

## Bolukbasi et al. (2016) — Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings

**Citation:** Bolukbasi, T., Chang, K-W., Zou, J., Saligrama, V., & Kalai, A. (2016). *Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings*. arXiv:1607.06520.  
**URL:** <https://arxiv.org/abs/1607.06520>

Seminal paper demonstrating that word2vec embeddings encode gender stereotypes reflecting societal biases in training corpora. Introduces a geometric debiasing method that projects gendered subspaces. Foundational reference for understanding how representational bias in pretrained models propagates through fine-tuned LLMs, directly motivating the bias evaluation dimension of this framework.

---

## Caliskan et al. (2017) — Semantics Derived Automatically from Language Corpora Contain Human-like Biases

**Citation:** Caliskan, A., Bryson, J. J., & Narayanan, A. (2017). *Semantics derived automatically from language corpora contain human-like biases*. *Science*, 356(6334), 183–186.  
**URL:** <https://arxiv.org/abs/1608.07187>

Introduces the Word Embedding Association Test (WEAT), a statistical method for measuring implicit biases in word embeddings analogous to the Implicit Association Test in psychology. Demonstrates that embeddings replicate human gender, racial, and age stereotypes from real-world corpora. The WEAT methodology underpins many subsequent bias measurement approaches and informs the association-based bias metrics in this framework.

---

## Blodgett et al. (2020) — Language (Technology) is Power: A Critical Survey of “Bias” in NLP

**Citation:** Blodgett, S. L., Barocas, S., Daumé III, H., & Wallach, H. (2020). *Language (Technology) is Power: A Critical Survey of “Bias” in NLP*. arXiv:2005.14050.  
**URL:** <https://arxiv.org/abs/2005.14050>

A critical survey of bias research in NLP, arguing that the field lacks consistent definitions, clear harm motivations, and rigorous evaluation standards. Examines 146 papers and finds that most do not articulate what harms their bias measures are intended to address. Essential reading for grounding the bias evaluation dimension in principled harm taxonomies rather than purely technical metrics.

---

## Zhao et al. (2018) — Gender Bias in Coreference Resolution: Evaluation and Debiasing Methods (WinoBias)

**Citation:** Zhao, J., Wang, T., Yatskar, M., Ordonez, V., & Chang, K-W. (2018). *Gender Bias in Coreference Resolution: Evaluation and Debiasing Methods*. arXiv:1804.06876.  
**URL:** <https://arxiv.org/abs/1804.06876>

Introduces WinoBias, a benchmark for measuring gender bias in coreference resolution using Winograd-schema-style sentences that probe whether models rely on occupational gender stereotypes. The benchmark’s controlled sentence pairs with occupational role swaps inform the allocation bias testing approach in `benchmarks/membench_rai.py`.

---

## Dhamala et al. (2021) — BOLD: Dataset and Metrics for Measuring Biases in Open-Ended Language Generation

**Citation:** Dhamala, J., Sun, T., Kumar, V., Krishna, S., Pruksachatkun, Y., Chang, K-W., & Gupta, R. (2021). *BOLD: Dataset and Metrics for Measuring Biases in Open-Ended Language Generation*. arXiv:2101.11718.  
**URL:** <https://arxiv.org/abs/2101.11718>

Introduces BOLD, a large-scale benchmark for measuring biases in open-ended text generation across five domains: profession, gender, race, religion, and political ideology. BOLD’s generation-based evaluation approach — prompting models and analysing output sentiment, toxicity, and psycholinguistic properties — is directly applicable to the bias and toxicity evaluation dimensions of this framework.

---

## Parrish et al. (2022) — BBQ: A Hand-Built Bias Benchmark for Question Answering

**Citation:** Parrish, A., Chen, A., Nangia, N., et al. (2022). *BBQ: A Hand-Built Bias Benchmark for Question Answering*. arXiv:2110.08193.  
**URL:** <https://arxiv.org/abs/2110.08193>

Introduces BBQ, a dataset of 58,492 question sets measuring social biases in LLM question-answering across nine categories (age, disability, gender, nationality, race, religion, SES, sexual orientation, physical appearance). BBQ’s ambiguous-context/disambiguated-context design enables precise separation of bias from model uncertainty. Cited in the README Academic Context table and directly informs the bias scoring methodology in `docs/scoring.md`.

---

*See also: [Benchmarks: Bias](../benchmarks/bias.md) for the framework’s internal bias evaluation documentation.*

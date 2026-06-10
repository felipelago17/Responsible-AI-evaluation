# Toxicity, Hate Speech & Harmful Content Detection

Annotated bibliography covering toxicity detection benchmarks, hate speech datasets, and evaluation methodologies for harmful content in LLMs. Relevant to the toxicity evaluation dimension and `benchmarks/membench_rai.py`.

---

## Gehman et al. (2020) — RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models

**Citation:** Gehman, S., Gururangan, S., Sap, M., Choi, Y., & Smith, N. A. (2020). *RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models*. arXiv:2009.11462.  
**URL:** <https://arxiv.org/abs/2009.11462>

Introduces RealToxicityPrompts, a dataset of 100K naturally occurring sentence-level prompts drawn from the web, paired with Perspective API toxicity scores. Demonstrates that even non-toxic prompts can elicit highly toxic completions from pretrained LLMs. The prompted-generation evaluation paradigm — measuring toxicity rate of model outputs across diverse inputs — directly informs the toxicity metric implemented in this framework.

---

## Hartvigsen et al. (2022) — ToxiGen: A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection

**Citation:** Hartvigsen, T., Gabriel, S., Palangi, H., Sap, M., Ray, D., & Kamar, E. (2022). *ToxiGen: A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection*. arXiv:2203.09509.  
**URL:** <https://arxiv.org/abs/2203.09509>

Introduces ToxiGen, a 274K-statement dataset of implicitly toxic and benign statements about 13 minority groups, generated using a pretrained language model steered with a classifier-in-the-loop approach. Focuses on implicit toxicity — statements harmful without explicit slurs — which is particularly relevant to evaluating LLMs fine-tuned to avoid surface-level toxic language.

---

## Röttger et al. (2021) — HateCheck: Functional Tests for Hate Speech Detection Models

**Citation:** Röttger, P., Vidgen, B., Nguyen, D., Waseem, Z., Margetts, H., & Pierrehumbert, J. B. (2021). *HateCheck: Functional Tests for Hate Speech Detection Models*. arXiv:2012.15606.  
**URL:** <https://arxiv.org/abs/2012.15606>

Introduces HateCheck, a suite of functional tests for hate speech classifiers covering 29 model functionalities across 7 protected groups. Tests include detection of explicit and implicit hate, handling of negation, counter-speech, reclaimed language, and non-hate about protected groups. The functional testing methodology — structured test cases targeting specific failure modes — is directly applicable to adversarial benchmark design within this framework.

---

## Vidgen et al. (2021) — Learning from the Worst: Dynamically Generated Datasets to Improve Online Hate Detection

**Citation:** Vidgen, B., Thrush, T., Waseem, Z., & Kiela, D. (2021). *Learning from the Worst: Dynamically Generated Datasets to Improve Online Hate Detection*. arXiv:2108.09134.  
**URL:** <https://arxiv.org/abs/2108.09134>

Presents a human-in-the-loop adversarial dataset collection methodology for hate speech, where annotators iteratively construct examples that fool current classifiers. The dynamic adversarial data collection approach informs the red-teaming methodology used in this framework’s adversarial evaluation dimension.

---

## Lees et al. (2022) — A New Generation of Perspective API

**Citation:** Lees, A., Tran, V. Q., Tay, Y., Sorensen, J., Gupta, J., Metzler, D., & Vasserman, L. (2022). *A New Generation of Perspective API: Efficient Multilingual Character-level Transformers*. arXiv:2208.09612.  
**URL:** <https://arxiv.org/abs/2208.09612>

Describes the Perspective API’s updated toxicity detection models, supporting multilingual toxicity scoring across attributes including toxicity, severe toxicity, identity attack, insult, profanity, and threat. The Perspective API provides an industry-standard external scorer that can be integrated as an annotation layer for validating the framework’s toxicity evaluation outputs.

---

## Perez et al. (2022) — Red Teaming Language Models with Language Models

**Citation:** Perez, E., Huang, S., Song, F., Cai, T., Ring, R., Aslanides, J., Glaese, A., McAleese, N., & Irving, G. (2022). *Red Teaming Language Models with Language Models*. arXiv:2202.03286.  
**URL:** <https://arxiv.org/abs/2202.03286>

Demonstrates a scalable approach to red teaming LLMs by using a separate language model to automatically generate test cases that elicit harmful outputs from a target model, evaluated across 16 harm categories including toxicity and offensive content. The automated red teaming paradigm is directly relevant to the agentic autonomy and zero-day risk evaluators in `evaluation/agentic_autonomy.py`.

---

*See also: [Benchmarks: Toxicity](../benchmarks/toxicity.md) for the framework’s internal toxicity evaluation documentation.*

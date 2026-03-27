# Truthfulness Benchmarks

## Hallucinations and Misinformation Risks in LLMs

Large language models generate text by predicting plausible continuations of input sequences. This process does not inherently require factual grounding: a model can produce confident, fluent, grammatically correct statements that are factually false. This failure mode is commonly referred to as **hallucination**.

Hallucination and misinformation risks matter because:

- Users may trust model outputs without independent verification, particularly for topics outside their expertise.
- Confidently stated falsehoods can be more persuasive and more harmful than uncertain ones.
- Models trained on large text corpora may have absorbed and reproduced false or contested claims present in training data.
- Instruction-tuned models may be fine-tuned to produce confident, helpful-sounding responses, which can exacerbate the presentation of false information.

---

## Benchmark Used

### TruthfulQA

**TruthfulQA** (Lin et al., 2022) is a benchmark of 817 questions designed to test whether language models give truthful answers, particularly in domains where models are likely to generate plausible but false responses. Questions span 38 categories including health, law, finance, history, science, and popular misconceptions.

The benchmark is specifically constructed to target **imitative falsehoods**: false statements that appear frequently in text on the internet and that a language model trained on web-scale data is likely to have absorbed. Questions are designed so that truthful answers are often counter-intuitive or less common than the corresponding false popular belief.

TruthfulQA evaluates models on two dimensions:
- **Truthfulness**: Whether the model's answer is factually correct
- **Informativeness**: Whether the answer provides substantive information rather than refusing to answer or responding with "I don't know"

Both dimensions matter: a model that always declines to answer is "truthful" in a trivial sense but is not useful.

**Why TruthfulQA**: It is the most widely adopted benchmark targeting hallucination and imitative falsehood in LLMs, and its construction explicitly targets the failure modes most likely to emerge from large-scale web training. The dataset and evaluation code are publicly available.

---

## Why Truthfulness Differs from Factual Recall

A common misconception is that truthfulness evaluation measures general factual knowledge. This is not the case:

- **Factual recall benchmarks** (e.g., TriviaQA, Natural Questions) test whether a model can correctly retrieve facts that are unambiguously present in its training data.
- **Truthfulness benchmarks** like TruthfulQA test whether a model can resist producing plausible-sounding false statements, particularly in domains where false beliefs are widespread.

A model may score well on factual recall benchmarks — correctly answering questions about well-documented facts — while still scoring poorly on TruthfulQA, because TruthfulQA specifically targets the intersection of high model confidence and factual incorrectness.

Truthfulness is therefore a distinct safety property from factual knowledge: it measures the model's epistemic calibration and resistance to producing confident falsehoods.

---

## Appropriate Interpretation of Scores

TruthfulQA scores should be interpreted carefully:

- **Scores are relative, not absolute**: A higher TruthfulQA score indicates fewer observed imitative falsehoods on this specific test set, not general factual reliability.
- **Domain variation**: Models may perform very differently across TruthfulQA's 38 categories. Aggregate scores can obscure poor performance in specific high-risk domains (e.g., medical or legal advice).
- **Evaluation method matters**: TruthfulQA can be scored using human annotation, fine-tuned classifier models (GPT-Judge), or multiple-choice variants. Scores from different evaluation methods are not directly comparable.
- **The benchmark tests known falsehoods**: TruthfulQA can only test against a fixed set of known imitative falsehoods. Novel hallucination patterns — including in domains, languages, or topics not covered — will not be detected.
- **Informativeness trade-off**: Some models improve truthfulness scores by refusing to answer or hedging excessively, which may reduce practical utility. Both dimensions should be examined together.

---

## Limitations and Appropriate Use

- **English-language and cultural specificity**: TruthfulQA questions are in English and reflect primarily US cultural and informational contexts. Misinformation patterns differ across languages and regions.
- **Static test set**: The benchmark was constructed at a specific point in time. As public knowledge evolves, some answers may become outdated.
- **False belief representation**: The categories of false belief tested reflect the choices of the benchmark's constructors and may not cover high-priority misinformation risks in specific deployment domains.
- **Multi-turn and context effects**: TruthfulQA evaluates single-turn responses. Hallucination patterns in multi-turn conversation, retrieval-augmented settings, or specialised domain use cases may differ substantially.
- **Instruction-tuned model behaviour**: Fine-tuning for helpfulness or instruction-following can influence TruthfulQA scores in ways that do not reflect real-world truthfulness, both positively and negatively.

For broader context on evaluation limitations, see [Limitations](../limitations.md).

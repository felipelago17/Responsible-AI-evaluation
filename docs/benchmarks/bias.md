# Bias Benchmarks

## What Bias Means in LLM Evaluation

In the context of large language model evaluation, **bias** refers to systematic disparities in model outputs that correlate with demographic attributes such as gender, race, ethnicity, religion, nationality, age, or disability status. Bias can manifest in several ways:

- **Representational bias**: A model consistently associates certain demographic groups with positive or negative attributes, occupations, or capabilities.
- **Allocation bias**: A model produces outputs that would favour or disadvantage one group over another in consequential decisions.
- **Stereotyping**: A model applies group-level generalisations to individuals, regardless of individual context.

Bias in LLMs is typically not intentional; it emerges from patterns present in training data, which reflect existing social inequalities and historical representation disparities. Evaluation aims to measure the degree to which these patterns persist in model outputs.

---

## Benchmarks Used

### WinoGrande

**WinoGrande** (Sakaguchi et al., 2021) is a large-scale commonsense reasoning benchmark derived from the Winograd Schema Challenge. It presents sentence pairs where a pronoun must be resolved to one of two candidate referents, with the correct answer depending on commonsense reasoning rather than demographic shortcuts.

WinoGrande is used in this project to probe whether models use gender or social stereotypes as shortcuts when resolving ambiguous pronoun references. Models that rely on stereotypical associations — for example, defaulting to female pronouns for caregiving roles — will perform inconsistently across demographically balanced sentence pairs.

**Why WinoGrande**: The dataset is large (44,000+ examples), carefully balanced to reduce annotation artefacts, and widely adopted as a fairness-relevant reasoning benchmark. Its construction methodology is documented and the dataset is publicly available.

### CrowS-Pairs

**CrowS-Pairs** (Nangia et al., 2020) is a crowdsourced benchmark for measuring social stereotypes in masked language models and, by extension, in generative models. Each example presents a pair of sentences that are minimally different: one expresses a stereotype and the other violates it. A model exhibiting bias will assign higher probability (or preference) to the stereotypical sentence.

CrowS-Pairs covers nine categories of bias: race/ethnicity, gender/gender identity, sexual orientation, religion, age, nationality, disability, physical appearance, and socioeconomic status.

**Why CrowS-Pairs**: It covers a broader range of bias dimensions than most alternatives and is grounded in crowdsourced annotation of real stereotypical statements, providing ecological validity.

---

## What These Benchmarks Measure Well

- **Direction and prevalence of stereotyping**: Both benchmarks can detect whether a model disproportionately associates groups with specific roles, traits, or valences.
- **Cross-demographic comparison**: Scores can be disaggregated by demographic category to identify which groups are most affected.
- **Relative comparison across models**: Given identical evaluation conditions, both benchmarks support meaningful comparison of bias levels across models.

---

## Known Limitations and Failure Modes

- **English-language and US-centric**: Both benchmarks are primarily constructed in English and reflect social stereotypes as they appear in US cultural contexts. Findings may not generalise to other languages or cultural settings.
- **Binary gender framing**: CrowS-Pairs largely frames gender as binary. Non-binary and gender-nonconforming identities are underrepresented.
- **Static stereotypes**: Stereotypes encoded in these datasets reflect the views of annotators at the time of construction. Social norms evolve; older datasets may not capture current stereotype landscapes.
- **Sentence-level, context-free testing**: Both benchmarks test individual sentences in isolation. Real-world bias often emerges in longer conversational contexts that these benchmarks do not capture.
- **Instruction-tuned model limitations**: Models trained with RLHF or instruction tuning may produce different outputs on benchmark prompts than on natural user queries, potentially masking bias that appears in other contexts.
- **WinoGrande and commonsense reasoning conflation**: High scores on WinoGrande may reflect general commonsense reasoning ability rather than specifically reduced bias, making scores difficult to interpret in isolation.

For broader context on evaluation limitations, see [Limitations](../limitations.md).

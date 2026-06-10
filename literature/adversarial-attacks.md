# Data Poisoning, Model Extraction & Adversarial Robustness

Annotated bibliography covering data poisoning attacks, model extraction and stealing techniques, and adversarial robustness defences. Relevant to `benchmarks/cybergym_glasswing.py`, `evaluation/agentic_autonomy.py`, and the robustness evaluation dimension.

---

## Data Poisoning

### Zhao P. et al. (2025) — Data Poisoning in Deep Learning: A Survey

**Citation:** Zhao, P., et al. (2025). *Data Poisoning in Deep Learning: A Survey*. arXiv:2503.22759.  
**URL:** <https://arxiv.org/abs/2503.22759>

A comprehensive survey of data poisoning attack taxonomies in deep learning, covering clean-label attacks, backdoor injection, availability attacks, and targeted misclassification. Reviews attack surfaces across training pipelines — including web-scraped pretraining corpora, fine-tuning datasets, and RLHF feedback — and evaluates detection and mitigation strategies. Foundational reference for the data integrity assumptions underlying this framework's benchmark evaluation pipeline.

---

### IEEE (2025) — Data Poisoning Attacks of Fine-Tuning for LLMs

**Citation:** IEEE. (2025). *Data Poisoning Attacks of Fine-Tuning for Large Language Models*. IEEE Xplore, doc. 11427210.  
**URL:** <https://ieeexplore.ieee.org/document/11427210>

Examines adversarial attacks that exploit the fine-tuning phase of large language models, demonstrating how small volumes of poisoned instruction-tuning or preference data can systematically alter model behaviour while evading standard evaluation. Relevant to the safety consistency under memory dimension evaluated by `benchmarks/membench_rai.py`, where persistent knowledge graph states may be vulnerable to analogous injection techniques.

---

### IEEE (2022) — A Survey on Data Poisoning Attacks and Defenses

**Citation:** IEEE. (2022). *A Survey on Data Poisoning Attacks and Defenses*. IEEE Xplore, doc. 9900151.  
**URL:** <https://ieeexplore.ieee.org/document/9900151>

Systematic survey covering the threat landscape of data poisoning — including label flipping, feature manipulation, and gradient-based attacks — alongside a taxonomy of defences (data sanitisation, robust training, certified defences). Provides the theoretical grounding for robustness evaluation methodology and informs adversarial test case design in `benchmarks/cybergym_glasswing.py`.

---

### Zhao P. (2026) — Data Poisoning Resource Repository

**Citation:** Zhao, P. (2026). *Data Poisoning Resource Repository*. GitHub.  
**URL:** <https://github.com/Pinlong-Zhao/Data-Poisoning>

A curated, living repository of papers, codebases, and datasets related to data poisoning research. Useful as an up-to-date index for tracking new attack vectors and defences relevant to the evaluation benchmarks in this framework, particularly as the benchmark adapter library expands to cover training-time threat models.

---

## Model Extraction & Stealing

### Zhao K. et al. (2025) — Systematic Survey of Model Extraction Attacks

**Citation:** Zhao, K., et al. (2025). *A Systematic Survey of Model Extraction Attacks: Taxonomy, Techniques, and Defences*. arXiv:2508.15031.  
**URL:** <https://arxiv.org/abs/2508.15031>

Provides a unified taxonomy of model extraction attacks — covering functional cloning, hyperparameter inference, training data reconstruction, and architecture theft — along with a structured evaluation of defence strategies including query rate limiting, output perturbation, and watermarking. Relevant to the agentic autonomy and zero-day risk components of the adversarial evaluation dimension.

---

### Hu & Pang (2021) — Stealing Machine Learning Models

**Citation:** Hu, T., & Pang, J. (2021). *Stealing Machine Learning Models: Attacks and Countermeasures for Generative Adversarial Networks*. In *Proceedings of the 37th Annual Computer Security Applications Conference (ACSAC)*. ACM.  
**URL:** <https://dl.acm.org/doi/fullHtml/10.1145/3485832.3485838>

Demonstrates practical model stealing attacks against generative adversarial networks via black-box API access, extracting functional equivalents of target models from query responses alone. Establishes empirical baselines for extraction feasibility and cost that inform the autonomous action risk thresholds modelled in `evaluation/agentic_autonomy.py`.

---

### Springer (2025) — Defenses against Model Stealing Attacks in MLaaS

**Citation:** Springer. (2025). *Defenses against Model Stealing Attacks in Machine Learning as a Service Environments*. *Cluster Computing*.  
**URL:** <https://link.springer.com/article/10.1007/s10586-025-05207-1>

Evaluates defence mechanisms for model stealing in MLaaS deployments, including prediction obfuscation, watermarking-based detection, and access control strategies. Directly relevant to the disclosure compliance and adversarial risk assessment modules, particularly for evaluating how well a model resists systematic capability probing under the CyberGym-Glasswing benchmark.

---

### IEEE (2025) — A Comprehensive Survey of Model Extraction Attacks

**Citation:** IEEE. (2025). *A Comprehensive Survey of Model Extraction Attacks and Defense Strategies*. IEEE Xplore, doc. 11137084.  
**URL:** <https://ieeexplore.ieee.org/document/11137084>

Broad-scope survey of model extraction techniques across supervised, generative, and reinforcement learning paradigms, evaluating both white-box and black-box attack vectors. Complements the Zhao et al. (2025) survey with coverage of RL-based and multimodal extraction scenarios, informing the adversarial risk dimension of this framework's evaluation harness.

---

*See also: [docs/benchmarks/robustness.md](../docs/benchmarks/robustness.md) and [docs/benchmarks/red-teaming.md](../docs/benchmarks/red-teaming.md) for the framework's internal methodology documentation.*

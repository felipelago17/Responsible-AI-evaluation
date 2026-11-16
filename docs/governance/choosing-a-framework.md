---
description: A two-step method for choosing among AI governance instruments — map binding laws to your footprint first, then layer voluntary standards — with status and dates checked against public sources as of 16 November 2026.
---

# Choosing an AI Governance Framework: Laws First, Standards Second

Many AI governance cheat-sheets circulate as graphics: a list of laws on one side, a list of standards on the other. The split is useful, but graphics go stale fast. This page keeps the split, checks every entry against public sources, and flags where a commonly repeated date or status has changed.

!!! info "Status and method"
    Checked on **16 November 2026** against official texts where they were reachable and against law-firm or standards-body summaries where they were not. Source type is shown for each row. This is a research aid, not legal advice. Where I could not confirm a point on a primary source, the table says so.

## Step 1: map binding laws to your footprint

Binding rules attach to **where you build, sell or use AI**, not to your preferences. Start with the jurisdictions where you place systems on the market, serve users, or deploy AI in decisions about people.

| Instrument | Status (16 Nov 2026) | Applies when | Source |
|---|---|---|---|
| **EU AI Act**, Regulation (EU) 2024/1689 | In force since 1 Aug 2024, applied in phases: prohibitions and AI literacy from 2 Feb 2025; general-purpose AI model duties from 2 Aug 2025. The Digital Omnibus on AI (Regulation (EU) 2026/1744, in force 27 Jul 2026) moved stand-alone high-risk obligations to 2 Dec 2027 and product-embedded high-risk to 2 Aug 2028 | You place AI on the EU market, put it into service there, or its output is used in the EU | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj); [Cooley on the Omnibus](https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/) |
| **GDPR Art. 22** | In force; automated individual decision-making | A decision based solely on automated processing has legal or similarly significant effects on a person | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj) |
| **South Korea AI Basic Act** | In force 22 Jan 2026 with its Enforcement Decree. The ministry announced a grace period of at least one year for fact-finding and corrective orders | You offer AI products or services in Korea (foreign providers can be covered) | [US ITA](https://www.trade.gov/market-intelligence/south-korea-ai-basic-act); [Shin & Kim](https://www.shinkim.com/eng/media/newsletter/3117?page=4) |
| **China Interim Measures for Generative AI Services** | In force 15 Aug 2023 | You provide generative AI services to the public in mainland China (offshore providers serving only users outside China are outside scope) | [Bird & Bird](https://www.twobirds.com/en/insights/2023/china/what-you-need-to-know-about-china’s-new-generative-ai-measures); [FPF](https://fpf.org/blog/chinas-interim-measures-for-the-management-of-generative-ai-services/) |
| **Japan AI Promotion Act** | Enacted 28 May 2025; most provisions from 4 Jun 2025, institutional chapters from 1 Sep 2025. Promotion-first: it sets principles and a government AI Basic Plan and carries no monetary penalties | You research, develop or use AI in Japan | [Japanese Law Translation](https://www.japaneselawtranslation.go.jp/en/laws/view/5066); [White & Case](https://www.whitecase.com/insight-alert/japans-first-ai-legislation-becomes-law-focus-promoting-research-and-development-no) |
| **California SB 53** (Transparency in Frontier AI Act) | In effect 1 Jan 2026 (some provisions 1 Jan 2027) | You train a frontier model above 10^26 operations; the heaviest duties fall on "large frontier developers" with revenue above $500m. Attorney General penalties up to $1m per violation | [White & Case](https://www.whitecase.com/insight-alert/california-enacts-landmark-ai-transparency-law-transparency-frontier-artificial); [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/california-governor-newsom-signs-groundbreaking-ai-legislation-into-law) |
| **Texas TRAIGA** (HB 149) | In effect 1 Jan 2026 | You develop or deploy AI in Texas or offer AI-enabled products to Texans. It prohibits specified harmful uses by intent rather than regulating by model scale | [Baker Botts](https://www.mondaq.com/unitedstates/new-technology/1651482/texas-enacts-responsible-ai-governance-act-what-companies-need-to-know); [Perkins Coie](https://admin.mondaq.com/unitedstates/new-technology/1647882/texas-enacts-responsible-artificial-intelligence-governance-act) |
| **Utah AI Policy Act** (SB 149) | In effect 1 May 2024; amended in 2025 (SB 226, SB 332), which narrowed disclosure to high-risk interactions or direct requests and extended the sunset to July 2027 | Generative AI interacts with consumers in Utah, or is used in a regulated occupation | [FPF](https://fpf.org/blog/chatbots-in-check-utahs-latest-ai-legislation/); [Davis Polk](https://www.davispolk.com/insights/client-update/utah-scales-back-reach-generative-ai-consumer-protection-law) |
| **NYC Local Law 144** | Effective 1 Jan 2023; enforced from 5 Jul 2023 | You use automated employment decision tools to screen candidates or employees for hiring or promotion in New York City (annual independent bias audit, notices) | [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/2023/04/26/nyc-dcwp-adopts-rules-to-implement-law-governing-automated-employment-decision-tools-and-sets-july-enforcement-date/); [Seyfarth](https://seyfarth.com/news-insights/new-york-city-releases-final-rules-implementing-local-law-144-aimed-at-curbing-artificial-intelligence-bias-in-employment-decisions.html) |
| **Council of Europe Framework Convention on AI** (CETS 225) | Opened for signature 5 Sep 2024. **Not confirmed in force**: entry needs five ratifications including three Council of Europe member states, then a three-month wait. The EU approved it by Council Decision (EU) 2026/1080 and, per reports, ratified on 15 May 2026 | It binds states, not companies directly; relevant to public-sector AI and to private actors acting on a state's behalf | [EUR-Lex decision](https://eur-lex.europa.eu/eli/dec/2026/1080/oj); [status commentary](https://aibusiness.vc/government/framework-convention-ai-two-years-not-in-force-procurement-governs-2026) |

!!! warning "Conflicting reports on the Council of Europe treaty"
    Sources disagree. One secondary source says the treaty entered into force on 1 Nov 2025; others, including a 2026 status review and the EUR-Lex text page ("not yet in force"), say the threshold has not been reached. I could not reach the Council of Europe's own treaty page from this environment, so treat the status as **unconfirmed** and check the treaty office before relying on it.

!!! warning "US federal overlay"
    A 11 Dec 2025 executive order directs a Department of Justice AI Litigation Task Force (established January 2026) to challenge state AI laws, and names laws like California's and Texas's as likely targets ([Paul Hastings](https://www.paulhastings.com/thought-leadership/president-trump-signs-executive-order-challenging-state-ai-laws)). A 2026 Cloud Security Alliance note says the state laws remain in effect unless Congress acts or courts intervene. I did not verify any court ruling, so re-check before treating a state law as settled.

## Step 2: layer voluntary standards that fit your risk

Voluntary instruments do not create legal duties by themselves. They show good practice, give you a common vocabulary with customers and auditors, and often supply the evidence regulators and contracts ask for.

| Instrument | Date | Use when | Source |
|---|---|---|---|
| **NIST AI RMF 1.0** (AI 100-1) | 26 Jan 2023 | You need a flexible, widely used risk-management method (Govern, Map, Measure, Manage) | [NIST](https://www.nist.gov/itl/ai-risk-management-framework) |
| **NIST Generative AI Profile** (AI 600-1) | 26 Jul 2024 | Your risks are specific to generative AI; names twelve risk areas with suggested actions | [NIST publication](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) |
| **ISO/IEC 42001** | Dec 2023 | You want a certifiable AI management system, built like ISO 27001 | [DQS overview](https://www.dqsglobal.com/en/explore/dqs-knowledge-center/iso-42001-explained) |
| **ISO/IEC 23894** | 2023 (date not confirmed on ISO's own page) | You want AI-specific risk-management guidance that extends ISO 31000 | [Techopedia overview](https://www.techopedia.com/?p=163464) |
| **ISO/IEC 42005** | 28 May 2025 | You need a method for AI system impact assessments. It is guidance, not certifiable, and is not a GDPR DPIA or an EU AI Act fundamental-rights assessment | [ISO](https://www.iso.org/standard/42005); [CASRAI note](https://casrai.org/guides/iso-42005-ai-system-impact-assessment) |
| **OECD AI Principles** | Adopted 22 May 2019; revised 3 May 2024 (AI system definition updated Nov 2023) | You want internationally agreed principles as a baseline | [OECD.AI](https://oecd.ai/en/ai-principles) |
| **G7 Hiroshima Code of Conduct** | 30 Oct 2023 | You develop advanced AI and want a shared code of conduct; OECD runs a reporting framework | [EY summary](https://assets.ey.com/content/dam/ey-sites/ey-com/en_gl/topics/ai/ey-g7-ai-principles-and-code-of-conduct-final.pdf) |
| **Singapore Model AI Governance Framework for Generative AI** | 30 May 2024 | You want practical, nine-dimension generative AI governance guidance | [Baker McKenzie](https://insightplus.bakermckenzie.com/bm/intellectual-property/singapore-imda-and-ai-verify-foundation-finalize-model-ai-governance-framework) |
| **UNESCO Recommendation on the Ethics of AI** | 23 Nov 2021 | You need a global ethics baseline; this repo's [UNESCO EIA module](../eia/index.md) builds on it | [ITU report](https://www.itu.int/net/epub/TSB/2025-The-Annual-AI-Governance-Report-2025-Steering-the-Future-of-AI/files/basic-html/page27.html) |
| **OWASP GenAI LLM Top 10** | **2026 edition published 3–4 Aug 2026** (the 2025 edition dates from Nov 2024) | You need to secure LLM applications; use alongside OWASP's agentic-applications list when a model has tools or memory | [OWASP 2026](https://genai.owasp.org/home/resources/owasp-genai-llm-top-10-2026/); [announcement](https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/) |

## Where common cheat-sheets are stale or too simple

- **EU AI Act "in force Aug 2024"** is true for entry into force, but obligations apply in phases and the high-risk dates have since moved (above). Planning from the 2024 dates would be wrong.
- **OWASP "2025"** has been superseded by the 2026 edition, which also weights its ranking with real-world incident data.
- **Council of Europe treaty** is "opened Sep 2024", not "binding on you". Its force depends on ratifications and it binds states.
- **"Binding" is not the same as "burdensome".** Korea's Act has a grace period for corrective orders, Japan's carries no monetary penalties, and California's SB 53 reaches only developers above a compute threshold.
- **"Voluntary" can become mandatory by contract.** Customers, insurers and procurement teams increasingly ask for ISO/IEC 42001 certification or NIST AI RMF alignment, so a voluntary standard can still be a commercial requirement.

## A short decision path

1. **List footprint**: where you build, host, sell and deploy, and who is affected by decisions.
2. **Map laws**: for each jurisdiction, note whether the rule is in force, delayed or in a grace period, and which role you hold (developer, deployer, provider).
3. **Pick one management backbone**: ISO/IEC 42001 if you want certification; NIST AI RMF if you want a flexible method.
4. **Add specialist layers**: NIST AI 600-1 and OWASP for generative AI and LLM apps; ISO/IEC 42005 for impact assessments.
5. **Evidence it**: connect your assessment outputs to the [governance mapping](../governance_mapping.md) and [UNESCO EIA](../eia/index.md) crosswalks, and keep a dated register of which instruments you applied and why.

## Limits of this page

- Most legal rows rest on law-firm and government-agency summaries; I did not read every statute in full.
- ISO standards are paywalled, so ISO/IEC 42001 and 23894 details come from certification-body and overview sources.
- Status can change quickly (Omnibus timing, Korean enforcement, US preemption, the Council of Europe treaty). Re-check before relying on any row.

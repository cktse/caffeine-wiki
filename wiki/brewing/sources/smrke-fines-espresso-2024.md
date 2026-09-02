---
title: "The Role of Fines in Espresso Extraction Dynamics (Smrke et al. 2024)"
domain: brewing
date_ingested: 2026-09-02
source_type: paper
tags: [espresso, fines, particle-size-distribution, share-of-fines, permeability, flow-rate, extraction-time, extraction-yield, turbo, aroma, voc, ptr-ms, peer-reviewed, zhaw]
raw_path: raw/brewing/The role of fines in espresso extraction dynamics.md
---

# The Role of Fines in Espresso Extraction Dynamics (Smrke et al. 2024)

## Summary

**Peer-reviewed** (Scientific Reports / Nature, open access) from **Samo Smrke, André Eiermann & Chahan Yeretzian** at the **[[brewing/entities/zhaw-coffee-excellence-center|ZHAW Coffee Excellence Center]]** — the same lab and Camsizer X2 instrument behind the Gagné PSD analysis already in the wiki. They isolate the effect of **fines** by holding a coffee fixed, varying median grind (X50), and **spiking sieved fines** to independently sweep the "**share of fines**" (Q₁₀₀µm = volume % of particles < 100 µm). Headline: fines govern **bed permeability → flow rate → extraction time**, and act **only** through permeability — not extraction efficiency — with **no sensory penalty**. Credibility: **high (peer-reviewed)**; caveats = single coffee/roast/grinder, fines *added* (not grinder-native), sensory by one Q-grader hedonic (authors flag this as non-double-blind).

## Method (for grounding)
Single-origin Costa Rica arabica, pulped-natural, medium roast (143 Colorette Pt). Bentwood Vertical 63 grinder (µm-calibrated burr spacing, settings 160–250); fines sieved < 120 µm and spiked (+1/2/4 g into 19/18/16 g) at settings 190/210/250. **20 g → 40 g (1:2), 9 bar**, Victoria Arduino Black Eagle, VST basket, 20 kgF tamp, 3 replicates. Measured: dynamic beverage weight, TDS/EY (VST refractometer), time, **dynamic-headspace PTR-MS** (aroma VOCs), Q-grader sensory (flavor/balance/tactile).

## Key Claims

- **Fines drive bed permeability → flow → time.** More fines = lower permeability = slower flow = longer extraction. Confirmed by **PLSR on whole PSDs** (first untargeted statistical confirmation): coefficients **positive < 150 µm** (fines raise time), ~zero 150–250 µm, **negative > 250 µm** (coarse main-peak lowers time).
- **Fines act *only* via permeability — not extraction efficiency (key nuance).** Spiking fines into a coarser grind produced the **same EY/time curve** as grinding finer (all points scatter on one curve); flow-rate profiles didn't fundamentally change. The extra surface area from fines has only a **marginal** effect on extraction efficiency. So the share of fines is primarily a **flow/time** lever, not a direct EY lever.
- **A single particle-size number is insufficient.** You need **Q₁₀₀µm (share of fines) + X50 (median)** to characterise espresso dynamics — both contribute significantly, similar-sized coefficients. Applied models: predict **time** from (Q₁₀₀µm, X50); predict **EY** from (Q₁₀₀µm, X50, time). Café dial-in oriented, not fundamental.
- **No sensory penalty from fines (myth-refining).** Higher share of fines did **not** hurt Q-grader scores; **surprisingly, +1 g and +2 g fines at setting 210 were among the highest-scoring**. Counters the common "fines = muddy/astringent" belief (at least for espresso, this coffee, hedonic scoring).
- **Fast/turbo is efficient.** < 10–15 s extractions gave **17–18 % EY = > 80 % of max**; max EY reached only for **> 40 s**. Supports "turbo" (10–20 s) espresso.
- **Aroma vs EY is non-linear.** PTR-MS VOCs cluster into 4 behaviours vs EY: **A** — continuously *decrease* with EY (highly volatile, non-polar); **B** — U-shaped, minimum ~19.5 % then rise; **C** — flat; **D** — *increase* with EY (heavier/soluble, e.g. maltol). 
- **Espresso extraction ≠ pure diffusion.** Headspace aroma isn't explained by extraction alone; VOCs are **lost** (i) at grinding (desorption), (ii) during extraction (**CO₂ degassing / crema carries volatiles off**), (iii) post-extraction (**evaporation from the flow & cup**, worse at higher temp / longer time), (iv) matrix partitioning.
- **"Turbo → fruity."** Fast, low-yield shots **retain more highly-volatile, non-polar (fruity) aroma** because there's less post-extraction loss. The aroma-side rationale for turbo — complements the [[brewing/entities/christopher-hendon|Hendon]] & Cameron turbo work (this paper cites Cameron et al. 2020).
- **Peak sensory is coffee/roast-specific.** For *this* coffee, the panelist's optimum was **~30 s / 19–20 % EY** — *not* the turbo range. Where peak quality sits depends on green + roast.

## Fit / Contradictions

- **Peer-reviewed backbone for [[brewing/concepts/particle-size-distribution]]** — rigorously defines Q₁₀₀µm and proves the fines→permeability mechanism that Gagné's practitioner analysis (same lab/instrument) described; reconciles with Gagné's "dial-in = dialling the fines fraction" and "over-shooting."
- **Refines the wiki's fines framing.** The model/lever pages loosely treat "more fines → body + astringency + EY." This paper says fines primarily set **flow/time**, with **marginal** direct extraction effect and **no sensory penalty** — a genuine nuance/partial myth-bust. (Not a hard contradiction with [[shared/astringency]]: that filtration/suspended-particle model is *filter*-brew; this is 9-bar espresso with crema, single-taster hedonic.)
- **Aroma losses corroborate [[brewing/concepts/blooming]]** (CO₂ off-gassing transports volatiles away) — and here it's the **same author (Smrke)** the blooming page already cites on bed-swelling.

## Wiki Pages Updated
- Updated: [[brewing/concepts/particle-size-distribution]], [[brewing/concepts/espresso-fundamentals]], [[brewing/concepts/blooming]], [[brewing/entities/zhaw-coffee-excellence-center]], wiki/index.md, wiki/log.md

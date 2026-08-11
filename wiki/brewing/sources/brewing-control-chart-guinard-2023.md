---
title: "A new Coffee Brewing Control Chart relating sensory properties and consumer liking to brew strength, extraction yield, and brew ratio (Guinard et al. 2023)"
domain: brewing
date_ingested: 2026-08-01
source_type: paper
tags: [brewing-control-chart, bcc, tds, extraction-yield, brew-ratio, sensory, consumer-preference, drip, sweetness, uc-davis, guinard, ristenpart, lockhart]
raw_path: raw/brewing/A new Coffee Brewing Control Chart relating sensory properties and consumer liking to brew strength, extraction yield, and brew ratio 1.md
---

# A new Coffee Brewing Control Chart (Guinard et al. 2023)

**Authors**: Jean-Xavier Guinard, Scott Frost, Mackenzie Batali, Andrew Cotter, Lik X. Lim, William D. Ristenpart (UC Davis Coffee Center)
**Journal**: *Journal of Food Science* 88(5):2168–2177, 2023 — doi:10.1111/1750-3841.16531
**Credibility**: **High** — peer-reviewed; UC Davis Coffee Center; synthesizes three prior peer-reviewed studies (Frost 2020, Batali 2020, Cotter 2021) totaling 324 physical, 32,076 sensory, and 3,186 consumer measurements; response-surface methodology; IRB-approved consumer panels. Same lab as the wiki's cold-brew source ([[cold-brew-vs-iced-batali-2022]]).

## Summary

Replaces the classic 1950s **Coffee Brewing Control Chart** (Lockhart 1957 — the "ideal cup" TDS × extraction chart in the SCA Brewing Handbook) with evidence-based versions. Maps **13 sensory attributes** onto the TDS × percent-extraction plane, and overlays **two distinct consumer preference clusters** — dismantling the single "ideal cup." Drip coffee only. This is the parent framework behind the wiki's sweetness work and the canonical source for the TDS/PE/brew-ratio math used in [[../concepts/bypass]].

## Key Claims

### The three axes and the governing equation
- **TDS** (total dissolved solids) = brew *strength* (mass fraction of solubles in the cup). Vertical axis.
- **PE** (percent extraction / extraction yield) = mass fraction of solubles removed from the grounds. Horizontal axis.
- **Brew ratio** R_brew = water / grounds. Diagonals on the chart.
- Linked by conservation of mass:

  **PE = [TDS / (1 − TDS)] × (R_brew − R_abs)**, where **R_abs ≈ 2.1** is the absorption / liquid-retention ratio of water held in spent grounds (Ristenpart & Kuhl 2021; Liang et al. 2021).

### The new Sensory BCC (13 attributes; where each is *maximized*)
- **High TDS + low PE** (upper-left): **acid/sour, citrus, berry, dried fruit** — the bright/fruity "specialty" corner.
- **High TDS + high PE** (upper-right): **bitter, astringent, roasted, burnt/ash, viscous/thick, black tea** — over-extracted/strong corner.
- **Low TDS + low-to-mid PE** (lower-left, PE ≈ 18%): **'sweet'** — written in quotes deliberately (see below).
- Also mapped: **dark greens** (small font). Font size = intensity; bitter/roasted/acidity are large-font (most intense).

### The 'sweet' caveat (corroborates the wiki's sweetness model)
'sweet' is quoted because it "most likely does not represent true sweet taste but rather a 'sweet' flavor impression … perceived in association with 'sweet' aromatics, and in contrast with, or in the absence of, bitterness and to a lesser extent acidity." Sugars are **below recognition threshold** in brewed coffee (Batali et al. 2020, monosaccharide analysis). Independent convergence with [[shared/sweetness-perception]].

### The new Consumer BCC — two preference clusters (no single "ideal")
- **Cluster 1 (57%, majority)** — dome response surface; **peak liking at low TDS + ~18% PE**, colocated with 'sweet' and opposite bitter/acid. Likes low-bitterness, low-acidity, 'sweet' cups. Penalty/Lift: **more positively driven by tea/floral and citrus; more negatively by sour and burnt.** Authors read this as the typical/average drinker (likely to add milk/sugar).
- **Cluster 2 (43%)** — saddle surface with **two** liking peaks: (a) **low PE + med-high TDS** = acid/sour/citrus/berry/dried-fruit ("specialty coffee" profile); (b) **high PE + med TDS** = roasted/burnt/thick/black-tea ("espresso blend" profile). Penalty/Lift: **more positively driven by roasted, dark chocolate, nutty; more negatively by paper/woody, green vegetables, rubbery.** Read as experienced/neophilic drinkers.
- Averaging the whole population *would* reproduce the classic "ideal" point — but that averaging hides the segmentation and is therefore misleading. The classic single "ideal cup" is rejected.

### Streamlined BCC
A 6-attribute, 4-corner version on the classic chart's background, relabeling Lockhart's "ideal" box as **"classic standard"** (since it is unclear which consumers found it ideal).

## Key Entities Mentioned
- [[../entities/uc-davis-coffee-center]] — the producing lab (created from this source)
- [[brewing/entities/sca]] — classic BCC lives in the SCA Coffee Brewing Handbook (Lingle 2011)

## Contradictions / Open Questions
- **No contradiction** — strongly corroborates [[shared/sweetness-perception]] ('sweet' as aroma illusion; sugars below threshold) from an independent method, and supplies the canonical extraction math behind [[../concepts/bypass]].
- **Attribute locations are where an attribute is *maximized*, not where it is guaranteed** — "to be expressed, the attribute must be present in the coffee to begin with." A light floral washed coffee will not read bitter/roasted at high PE if it has little of those to give. The chart does not encode variety, origin, or roast effects (beyond the study's designs).
- **Scope limits**: drip only (espresso/cold-brew BCCs flagged as future work); consumer clusters are young Northern-California black-coffee drinkers — segmentation may differ elsewhere and could have >2 clusters.
- **Brew temperature** had *little* sensory impact at fixed TDS/PE (Batali et al. 2020, one of the three underlying studies) — reinforces that TDS/PE, not temperature per se, drive the sensory profile.

## Wiki Pages Updated
- `wiki/brewing/sources/brewing-control-chart-guinard-2023.md` (this file)
- `wiki/brewing/concepts/brewing-control-chart.md` (created)
- `wiki/brewing/entities/uc-davis-coffee-center.md` (created)
- `wiki/shared/sweetness-perception.md` — independent corroboration of the 'sweet' aroma-illusion model
- `wiki/brewing/concepts/bypass.md` — BCC as the parent chart; bypass = vertical (TDS-down) move at constant PE
- `wiki/brewing/concepts/dialing-in.md` — BCC as target-setting framework; partial answer to the TDS-target open question (drip)
- `wiki/brewing/overview.md` — BCC added to concepts; brew-temp finding noted
- `wiki/index.md`, `wiki/log.md`

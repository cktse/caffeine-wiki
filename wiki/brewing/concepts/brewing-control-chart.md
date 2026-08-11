---
title: "Brewing Control Chart (BCC)"
domain: brewing
tags: [bcc, tds, extraction-yield, percent-extraction, brew-ratio, sensory-map, consumer-preference, drip, sweetness, extraction]
source_count: 1
last_updated: 2026-08-01
---

# Brewing Control Chart (BCC)

## Definition

A 2-D map of drip-coffee outcomes with **strength (TDS)** on the vertical axis, **extraction yield (percent extraction, PE)** on the horizontal axis, and **brew ratio** as diagonals. The classic BCC (Lockhart, 1957; taught via the SCA Coffee Brewing Handbook) marked a single central **"ideal cup."** Guinard et al. 2023 replaced it with an evidence-based **Sensory BCC** (where each flavor attribute is maximized) and a **Consumer BCC** (where different drinkers actually prefer to be) — and showed there is **no single ideal**. See [[../sources/brewing-control-chart-guinard-2023]].

## The Three Quantities and the Equation

The three axes are not independent — conservation of mass links them:

> **PE = [TDS / (1 − TDS)] × (R_brew − R_abs)**

- **TDS** — % solubles in the cup (strength). Measured with a refractometer.
- **PE** — % of the coffee's mass extracted into the cup (18–22% is the classic "ideal" band).
- **R_brew** — water-to-grounds ratio (e.g. 15).
- **R_abs ≈ 2.1** — absorption / liquid-retention ratio: water retained by spent grounds (~2.1 g per g dry coffee). This is the same retention constant used empirically in the wiki's worked examples (≈2.0–2.3 g/g).

Practical use: measure TDS + know your ratio → compute PE. Or target a (TDS, PE) point on the chart → back out the grind/ratio to get there.

## The Sensory BCC — where each attribute is maximized

| Chart region | TDS | PE | Attributes maximized here |
|---|---|---|---|
| **Upper-left** | High | Low | acid/sour, citrus, **berry, dried fruit** — bright/fruity "specialty" corner |
| **Upper-right** | High | High | **bitter, astringent, roasted, burnt/ash, viscous/thick, black tea** — over-extracted/strong corner |
| **Lower-left** | Low | Low–mid (~18%) | **'sweet'** (see caveat) |
| **Lower-right** | Low | High | thin/dilute; dark greens, papery/vegetal tendency |

Font size on the original chart encodes intensity: **bitter, roasted, acid/sour are the most intense** (large); berry and dark greens are subtle (small).

> **Critical caveat:** these are locations of *maximum expression*, not guarantees. "To be expressed, the attribute must be present in the coffee to begin with." A light-roast floral washed coffee brewed at high PE won't necessarily taste bitter/roasted if it has little of those compounds — the chart maps *extraction behavior*, not the coffee's inherent character (variety/origin/roast are not encoded).

## The 'sweet' caveat

'sweet' sits in quotes because it is an **aroma-driven flavor impression**, not sugar taste — sugars are below recognition threshold in brewed coffee (Batali et al. 2020). Perceived when 'sweet' aromatics are present *and* bitterness/acidity are low — which is exactly why it peaks in the low-TDS, low-PE corner. This is independent corroboration of [[shared/sweetness-perception]] from a different research method.

## The Consumer BCC — two preference clusters (no single "ideal")

| Cluster | Share | Where they peak | Likes | Penalty/Lift drivers |
|---|---|---|---|---|
| **Cluster 1** | 57% | Low TDS, PE ≈ 18% (the 'sweet' corner) | Low-bitter, low-acid, 'sweet' cups | **+** tea/floral, citrus · **−** sour, burnt |
| **Cluster 2** | 43% | Saddle — two peaks: (a) low PE + med-high TDS; (b) high PE + med TDS | (a) acid/sour/citrus/berry/dried-fruit "specialty"; (b) roasted/burnt/thick/black-tea "espresso blend" | **+** roasted, dark chocolate, nutty · **−** paper/woody, green veg, rubbery |

Authors' reading: Cluster 1 = typical/average drinker (would add milk/sugar); Cluster 2 = experienced/neophilic drinker comfortable across specialty-acidic and dark-roast-bitter extremes. Averaging the whole panel reproduces the old "ideal" point — but that average is a mirage that hides the segmentation.

## Practical Use (for this wiki)

- **Target-setting for dialing in:** decide *where on the chart* you want the cup, then use grind/ratio to land there. See [[concepts/dialing-in]].
- **Bypass is a vertical move.** Adding bypass water lowers TDS at (essentially) constant PE — it slides the cup **straight down** the chart, away from the high-TDS bitter/astringent band toward the lower 'sweet'/cleaner zone, without changing extraction. This is the BCC-level reason bypass reads as cleaner and sweeter. See [[concepts/bypass]].
- **CK's target zone:** given a sweetness-forward preference on light-medium washed coffees, aim **low-to-mid TDS + ~18–21% PE** (Cluster 1's 'sweet' peak / Cluster 2's bright-specialty peak). Extract fully for sweetness, keep TDS modest (dilute/bypass) to stay out of the bitter/astringent upper-right.
- **Temperature is secondary.** At fixed TDS/PE, brew temperature had little sensory impact (Batali et al. 2020) — grind/ratio/extraction move you on the chart; temperature mostly changes *how* you reach a TDS/PE, not the destination's sensory signature.

## Key Sources
- [[../sources/brewing-control-chart-guinard-2023]] — Guinard et al. 2023; the new Sensory + Consumer BCC; synthesis of Frost 2020 / Batali 2020 / Cotter 2021

## Related Concepts
- [[concepts/bypass]] — vertical (TDS-down) move at constant PE; shares the R_abs/PE math
- [[concepts/dialing-in]] — the BCC as a target framework
- [[concepts/46-method]] — the flavor/strength axes are a hands-on way to move around the chart
- [[concepts/espresso-fundamentals]] — espresso BCC is future work; Cluster 2's high-PE peak maps to espresso-blend profiles
- [[concepts/cold-brew]] — cold-brew BCC is future work; same UC Davis group
- [[shared/sweetness-perception]] — the 'sweet' aroma-illusion model this chart independently supports

## Open Questions
- What do the espresso and cold-brew BCCs look like (flagged by the authors as future work)?
- Do non-US / non-young / with-milk consumer populations segment into the same two clusters, or more?
- Where exactly do this wiki's recipes land on the chart — e.g. the Yunnan bypass cup (TDS 1.43%, PE ~20.5%) sits upper-mid, yet reads sweet/clean because its light-medium washed character has little bitter/roasted to express (the caveat in action)?

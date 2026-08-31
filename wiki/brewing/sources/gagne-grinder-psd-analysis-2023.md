---
title: "Analyzing 300 Particle Size Distributions for 24 Espresso Grinders (Gagné 2023)"
domain: brewing
date_ingested: 2026-08-31
source_type: article
tags: [grinder, particle-size-distribution, psd, fines, boulders, unimodality, uniformity, burr-geometry, conical, flat-burr, dial-in, espresso, tri-lognormal, kaffeemacher, zhaw, jonathan-gagne]
raw_path: raw/brewing/What I learned from analyzing 300 particle size distributions for 24 espresso grinders.md
---

# Analyzing 300 Particle Size Distributions for 24 Espresso Grinders (Gagné 2023)

## Summary

Jonathan Gagné (physicist; *The Physics of Filter Coffee*) mines a **Kaffeemacher / ZHAW** dataset — ~300 particle-size distributions (PSDs) across **24 espresso grinders**, measured by Marco Wellinger at the ZHAW Coffee Excellence Center on a Retsch **Camsize X2** imaging device using one 82-point natural Brazilian coffee, across many grind sizes plus dialled-in ristretto/espresso/allongé. He extracts two orthogonal grinder metrics — **unimodality** (few fines) and **uniformity** (few boulders) — and a headline dial-in insight. Credibility: **high (practitioner-scientist + academic dataset)**. This is the scientific grounding for the "fines management" theme running through the recent WBrC ingests.

## Key concepts defined

- **PSD** — the contribution of each particle diameter to the ground coffee. **Volume-weighted** plots reveal the coarse **nominal peak**; **number-weighted** plots emphasise the **fines peak** (informs mouthfeel, puck resistance, alignment).
- **Unimodality** — how *few fines* a grinder makes: fraction of fines by volume (0–100μm) at a reference median of **340μm**. More unimodal = fewer fines.
- **Uniformity** — how *narrow the coarse peak* is: the "**extent of boulders**" (right-side half-width of the nominal peak). More uniform = fewer boulders (oversized particles).
- **Tri-log-normal model** — PSDs from ~10–1200μm are well reproduced by **three log-normal components** (fines / middle / nominal), fit via the cumulative distribution to dodge binning artefacts.

## Key Claims

- **Methodology first:** comparing a *handful* of PSDs across grinders is "more often than not useless" — you need many PSDs across grind sizes, on the **same coffee + same machine** (different laser/imaging devices bin and err differently). Also control **grinder RPM and bean feed rate** (huge for some grinders, e.g. conical Weber Key).
- **Conical vs flat:** conical burrs are **less unimodal *and* less uniform** than flat — but only **on average** (large overlap; specific exceptions exist).
- **Unimodality correlates strongly with uniformity** — *contrary to hearsay*. The intuition that "more cuts → more uniform but more fines" is an over-simplification; burr geometry/alignment dominate.
- **RPM shows no clear trend** with unimodality/uniformity across grinders — the effect is **grinder-specific**, and for many grinders RPM mostly just **shifts grind size** rather than changing the PSD shape. (Conicals run slower RPM on average.)
- **Burr size isn't destiny:** larger burrs did **not** systematically give more uniform/unimodal grinds; within the sample bigger flat burrs were often *less* unimodal. **Burr tooth geometry + coating matter more than diameter** (lone 83mm Ceado E37 Nero is a unimodal exception).
- **Taste (blind, Kaffeemacher):** top-rated grinders sat **mid-range** on unimodality/uniformity, not at extremes → other factors matter. A badly-rated grinder (G-Iota Probarista) plotted near top-rated ones (Niche Zero, Baratza Forté) — hinting at effects **not visible in a PSD** (clumping, grounds heating).
- **Dial-in headline:** *"When we dial in espresso, we are dialling in the amount of **fines** more than the average size of coarse particles."* The fines fraction drives puck resistance, so **more unimodal (fewer-fines) grinders must grind *finer* for espresso** (median grind at dial-in correlates best with unimodality).
- **"Over-shooting" twist (counter-intuitive):** once dialled in, more unimodal grinders end up with *slightly **more** fines per gram* than less unimodal ones — hard to explain (likely puck compression/reconfiguration). This also muddies why **unimodal shots (e.g. Weber EG-1 ULF burrs) have *lower* body** despite more fines — perhaps finer gaps make fines clog in-puck before reaching the cup.
- **Geophysics permeability fails for coffee:** soil's "flow ∝ (10th-centile diameter)²" does **not** predict espresso puck resistance at dial-in. Hypotheses: (a) different PSDs → different **initial slurry viscosity** (surface area liberates solubles/oils/CO₂); (b) **high espresso pressure reconfigures** the puck (compression, fines migration/clogging) unlike soil; (c) coffee particle shape/roughness unusual (he deems this least likely).
- **Style implication:** unimodality strongly shapes **espresso style** — average EY and the **clarity-vs-mouthfeel** balance (cf. Gagné's low-fines-espresso work). Uniformity's taste effect is **less clear** (he'd expect higher uniformity → higher EY + more clarity, little mouthfeel change — unproven).

## Key Entities Mentioned
- [[brewing/entities/jonathan-gagne]] — author/analyst
- [[brewing/entities/kaffeemacher]] — ran the 24-grinder study + blind tastings
- [[brewing/entities/zhaw-coffee-excellence-center]] — Marco Wellinger; measured the PSDs (Camsize X2)
- [[brewing/entities/lance-hedrick|Lance Hedrick]] — flagged the dataset to Gagné; contributed hand-grinder laser-diffraction PSDs
- Grinders discussed (not filed): Lelit Fred, Mazzer Omega, Kinu M47, [[brewing/entities/comandante|Comandante C40]], Mahlkönig X54, Baratza Forté, Niche Zero, Weber EG-1 (ULF), Ceado E37 Nero, G-Iota Probarista

## Contradictions / Open Questions
- **Nuance vs practitioner "low-RPM = fewer fines"** (e.g. Nas Jaafar in [[brewing/concepts/flow-resistance]]): Gagné finds RPM's PSD effect is **grinder-specific**, often just a grind-size shift — so the advice isn't universal.
- Alignment of the tested units is unknown and could confound both metrics.
- The metrics → taste mapping is still unproven; blind-taste winners were mid-range, so PSD isn't the whole story (clumping/heating).

## Wiki Pages Updated
- Created: [[brewing/concepts/particle-size-distribution]], [[brewing/entities/kaffeemacher]], [[brewing/entities/zhaw-coffee-excellence-center]]
- Updated: [[brewing/entities/jonathan-gagne]], [[brewing/entities/lance-hedrick]], [[brewing/concepts/espresso-fundamentals]], [[brewing/concepts/flow-resistance]], [[brewing/concepts/sandwich-extraction]], wiki/index.md, wiki/log.md

---
title: "Particle Size Distribution (Grinder Characterization)"
domain: brewing
tags: [grinder, particle-size-distribution, psd, fines, boulders, unimodality, uniformity, burr-geometry, conical, flat-burr, dial-in, espresso, mouthfeel, clarity, tri-lognormal]
source_count: 1
last_updated: 2026-08-31
---

# Particle Size Distribution (Grinder Characterization)

## Definition

A **particle size distribution (PSD)** is the contribution of each particle diameter to a ground-coffee sample. Coffee PSDs are typically **bimodal**: a **fines peak** (sub-~100μm) and a coarser **nominal peak**. How you plot it matters — **volume-weighted** shows the nominal peak (extraction dynamics); **number-weighted** emphasises the fines peak (mouthfeel, puck resistance, burr alignment). PSDs from ~10–1200μm are well modelled by **three log-normal components** (fines / middle / nominal).

This is the grind-science layer under the wiki's many practitioner "fines" discussions — see grounding note below.

## Two orthogonal grinder metrics (Gagné 2023)

| Metric | Measures | "Good" direction | How measured |
|---|---|---|---|
| **Unimodality** | how *few fines* | more unimodal = fewer fines | fraction of fines by volume (0–100μm) at a reference median of **340μm** |
| **Uniformity** | how *narrow the coarse peak* (few **boulders**) | more uniform = fewer oversized particles | "extent of boulders" = right-side half-width of the nominal peak |

To characterise a grinder you need **many PSDs across grind sizes** on the **same coffee + machine** — a single PSD (or a few across different machines) is "more often than not useless." Control **RPM and feed rate** too.

## What the data shows

- **Conical < flat** on both metrics **on average** (less unimodal, less uniform) — with large overlap; not a rule for any specific pair.
- **Unimodality strongly correlates with uniformity** — *contrary to hearsay* that "more cuts = more uniform but more fines." Burr **geometry/alignment** dominate, not "number of cuts."
- **RPM:** no clear cross-grinder trend; effect is **grinder-specific**, often just shifting grind size rather than reshaping the PSD.
- **Burr size ≠ quality:** larger burrs don't systematically grind more uniform/unimodal; **tooth geometry + coating > diameter**.
- **Taste:** blind-tasting winners were **mid-range** on both metrics, not extreme — so PSD isn't the whole story (clumping, grounds heating matter; e.g. a poorly-rated grinder plotted near top-rated ones).

## The dial-in insight (the practical headline)

**Dialling in espresso adjusts the *fines fraction* far more than the coarse-peak size.** Because fines drive puck resistance, **fewer-fines (more unimodal) grinders must grind *finer* for espresso** — the median grind at dial-in correlates best with unimodality.

**"Over-shooting" twist:** once dialled in, more unimodal grinders end up with *slightly **more** fines per gram* than less-unimodal ones (counter-intuitive; likely puck compression/reconfiguration). This also complicates why **very unimodal shots (Weber EG-1 ULF) taste *lower* in body** despite more fines — perhaps the finer gaps trap fines in-puck before they reach the cup.

**Geophysics doesn't transfer:** soil permeability (flow ∝ 10th-centile diameter²) fails to predict espresso puck resistance — espresso's high pressure reconfigures the puck (compression, fines migration/clogging) and different PSDs give different initial slurry viscosity.

## Why it matters (extraction & sensory)

- **Unimodality shapes espresso style** — average EY and the **clarity ↔ mouthfeel** balance. Low-fines/unimodal → cleaner, often lower body; more fines → more body/resistance but more astringency risk (the grind-size ceiling, [[shared/astringency]], [[brewing/concepts/espresso-fundamentals]]).
- **Grinder choice is a sensory lever**, not just "finer/coarser" — two grinders at the *same median* can pull very different shots because their fines fractions differ.
- **Uniformity**'s taste role is still unproven (expected: higher uniformity → higher EY + clarity, little mouthfeel change).

## Grounding the wiki's "fines" discussions

The recent WBrC ingests treated fines as a practitioner lever in opposite directions — Nas Jaafar used **low-RPM to cut fines** ([[brewing/concepts/flow-resistance]]); Bavis Kwong **sieved fines out and re-layered them** for body/sweetness ([[brewing/concepts/sandwich-extraction]]). This source grounds *why*: the **fines fraction is a real, measurable grinder property** with a genuine mouthfeel-vs-clarity trade-off. It also **nuances** the "low-RPM = fewer fines" advice — Gagné finds RPM's PSD effect is grinder-specific, often just a grind-size shift.

Independently echoed by working pros: in the Harmony survey ([[brewing/sources/harmony-pourover-recipes-2026]]), several — notably Junchao Huang (targets 600–800 µm, *"temperature is not the key factor… particle size distribution is"*) — rank **grind/PSD above temperature** as the primary extraction control.

## Key Sources
- [[brewing/sources/gagne-grinder-psd-analysis-2023]] — Gagné's analysis of the Kaffeemacher/ZHAW 24-grinder, ~300-PSD dataset; unimodality vs uniformity; dial-in = dialing fines; over-shooting; burr geometry; high (practitioner-scientist + academic dataset)

## Related Concepts
- [[brewing/concepts/espresso-fundamentals]] — grind ceiling, low-fines espresso, clarity vs mouthfeel
- [[brewing/concepts/flow-resistance]] · [[brewing/concepts/sandwich-extraction]] — the practitioner fines levers this grounds
- [[brewing/concepts/comandante-grind-size]] — grind setting → size (click/micron); this is the *distribution* behind the median
- [[shared/astringency]] — finer grind → more liberated astringent particles (the ceiling)
- [[brewing/concepts/dialing-in]] — grind-first adjustment; here, you're adjusting fines
- [[brewing/concepts/bed-depth]] — deeper beds filter fines better; grind offsets pair with depth

## Open Questions
- Metrics → taste mapping is unproven; need many more datasets to link unimodality/uniformity to specific sensory outcomes.
- Unit-to-unit **alignment** could confound both metrics (untested here).
- Does uniformity independently raise EY/clarity as hypothesised?

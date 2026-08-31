---
title: "The Pulsar Mini and the Importance of Bed Depth (Gagné 2025)"
domain: brewing
date_ingested: 2026-08-31
source_type: article
tags: [pour-over, bed-depth, dripper-diameter, darcy, grind, brew-time, filtration, astringency, batch-brew, pulsar, no-bypass, espresso-puck, jonathan-gagne]
raw_path: raw/brewing/The Importance of Bed Depth.md
---

# The Pulsar Mini and the Importance of Bed Depth (Gagné 2025)

## Summary

Jonathan Gagné argues that a dripper's **diameter (width)** is mostly a *batch-size* knob, while its **bed depth** is a **fundamental flavor parameter** — one you can't easily compensate for with other variables. He gives four mechanisms by which depth changes the cup, a practical grind/brew-time cheat sheet (deeper → coarser *and* longer *and* more forgiving), and a speculative surface-adsorption filtration model that links deep beds to lower astringency. Credibility: **high (practitioner-scientist)**; the astringency-filtration part is explicitly a hypothesis.

## Key Claims

### Diameter ≈ batch size (idealized no-bypass)
Changing **dripper diameter** while holding bed depth, ratio, coffee, temp, and grind fixed yields **the same brew time, TDS, and EY** — just a **larger batch**. To keep the same water-column height you pour **faster** (drip rate scales with bed surface area). So the same recipe transfers across diameters: Gagné brews his **Pulsar** recipe in the **Pulsar Mini** at **0.6× dose** (e.g. 25 g → 15 g).
- **Dial-in cue:** don't judge dial-in by *total* drip rate across dripper sizes (a Mini looks like fast droplets, not a stream, when correctly dialled) — watch the **water-column drop rate**, which is diameter-independent for a given recipe + depth.

### Bed depth is a fundamental parameter
Ranks alongside ratio, grind, water mineral/temperature, dripper geometry, grinder PSD, and the coffee itself. **Four ways depth changes the brew:**
1. **Longer brew time and/or coarser grind** (Darcy's law: a thicker percolation medium resists flow more). Gagné's preference is a **compromise** — grind a bit coarser *and* accept longer times.
2. **Reduces the impact of bed disturbances/channels** — a channel of a given depth spans a *smaller fraction* of a deeper path.
3. **Better filtration of insolubles** (fines, chaff, and *maybe* astringency molecules).
4. **Changes bottom-of-bed extraction style** — the bottom meets more-concentrated/near-saturated water, slowing extraction of fast-diffusing compounds there.
(On a V60, depth also shifts the **bypass fraction**.)

### Cheat sheet (1:17 ratio; EG-1 lab sweet burrs; burr shifts are *relative* µm)
Both optimal **grind size and brew time rise** with bed depth, and the **acceptable brew-time range widens** — deeper beds are **more forgiving**, with more **body, sweetness, complexity** even for light roasts. His daily go-to: **~17 mm** (Pulsar Mini, 15 g).

| Bed depth | Brew time | Rel. burr gap | Dose (Pulsar) | Dose (Mini) |
|---|---|---|---|---|
| 14 mm | 3:20–3:40 | 0 | 20 g | 10.7 g |
| 15 mm | 3:30–4:00 | +15 µm | 22 g | 12 g |
| 17 mm | 3:40–4:40 | +40 µm | 25 g | 15 g |
| 19 mm | 3:53–5:20 | +65 µm | 28 g | 18 g |
| 20 mm | 4:00–5:40 | +80 µm | 30 g | 19.5 g |
| 23.3 mm | 4:20–6:45 | +125 µm | 35 g | 22.8 g |
| 25 mm | 4:30–7:20 | +145 µm | 37.5 g | 24.4 g |

Rows ≥20 mm are extrapolated toward Scott Rao's parallel recommendation (deeper 20–23 mm). Absolute burr gaps don't transfer (even between EG-1 units). Shallow/narrow beds are **finicky** and usually taste worse.

### Filtration model of astringency (hypothesis)
Astringency likely comes from **long molecules** that don't dissolve at brew temperature. They're far too small (<20 nm) to be sieved by inter-particle gaps — instead Gagné suspects they **stick to rough particle/fines surfaces**, trapped or released depending on bed **tortuosity/depth** and **microscopic fluid velocity** (driven by pressure / water-column height). So a **deeper bed + gentle velocity → better filtration → less astringency**. Explains his preference for a **narrow water column**, why espresso-machine filter coffee is cloudier/astringent (high pressure) *except* 0-bar **Filter3**, and why shallow beds are finicky (small disturbances → poor-filtration channels; small water-column changes → big velocity swings). Thicker beds tolerate **taller water columns** without astringency.
- **Caveat:** don't let the water column vanish — it lowers bed temperature and **re-introduces air**, undoing the bloom (like watering a dry plant pot: air obstructs flow paths).

### Batch brew & espresso
- **Batch brew** tastes best at ~5–6 min vs pour-over ~3:30 — Gagné thinks this is **just bed depth**; he's converging toward batch parameters (Rao's 90s rule: batch optimal depth **3–5 cm**).
- **Espresso pucks:** similar percolation mechanics, but (1) **filtration matters less** (high pressure dislodges what a filter bed would trap), and (2) thicker pucks may make **more crema** (fresh / dark-enough coffee).

## Key Entities Mentioned
- [[brewing/entities/jonathan-gagne]] — author
- [[brewing/entities/nextlevel-pulsar]] — Pulsar + the new **Pulsar Mini** (0.6× diameter) motivating the post
- [[roasting/entities/scott-rao]] — parallel bed-depth post; recommends deeper 20–23 mm beds
- [[brewing/entities/lance-hedrick]] — cited on portafilter diameter (same diameter=batch logic)

## Contradictions / Open Questions
- The **surface-adsorption filtration** mechanism is explicitly a hypothesis ("no good demonstration that this actually happens") — consistent with the wiki's unresolved astringency-compound identity ([[shared/astringency]]).
- Cheat-sheet grind offsets are EG-1-specific; only *relative* µm shifts are claimed to transfer.
- Espresso filtration/crema claims are fluid-mechanics intuition, not measured.

## Wiki Pages Updated
- Created: [[brewing/concepts/bed-depth]]
- Updated: [[brewing/entities/jonathan-gagne]], [[brewing/entities/nextlevel-pulsar]] (Pulsar Mini), [[shared/astringency]], [[brewing/concepts/espresso-fundamentals]], [[brewing/concepts/particle-size-distribution]], wiki/index.md, wiki/log.md

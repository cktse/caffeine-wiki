---
title: "Comandante Grind Size Reference"
domain: brewing
tags: [comandante, grind-size, reference, c40, c60, microns, calibration]
source_count: 1
last_updated: 2026-06-17
---

# Comandante Grind Size Reference

A calibration page for translating Comandante C40 click counts (used throughout this wiki's recipes) to microns and to other Comandante models.

## C40 Click → Micron Conversion

**Rule of thumb:** 1 C40 click ≈ 30µm. (Back-calculated: 20 clicks = 600µm → 30µm/click.)

| Brew Method | C40 Clicks | Microns | Notes |
|---|---|---|---|
| Turkish (Ibrik) | 0–3 | 0–90 | |
| Espresso | 3–6 | 90–180 | Red Clix strongly recommended |
| AeroPress (espresso-style) | 10–20 | 300–600 | |
| Pour-over (all: V60, Graycano, Kalita, Orea) | 20–30 | 600–900 | See per-dripper notes below |
| AeroPress (filter-style) | 20–30 | 600–900 | |
| Cupping | 25–30 | 750–900 | |
| Cold Brew (drip) | 25–30 | 750–900 | |
| Cold Brew (immersion) | 30–40 | 900–1,200 | |

## Pour-Over Grind Nuance (within 20–30 clicks)

All pour-over methods fall in the same 20–30 click range, but the practical starting points differ:

| Dripper / Method | C40 Starting Point | Microns | Source |
|---|---|---|---|
| Graycano cone | ~25 clicks | ~750µm | [[sources/graycano-two-recipes-basic-barista]] |
| Graycano wave (Coin) | ~30 clicks | ~900µm | [[sources/graycano-two-recipes-basic-barista]] |
| Hario V60 (general) | 20–30 clicks | 600–900µm | [[sources/comandante-grind-size-chart]] |
| Kasuya 4:6 method | Medium-coarse to coarse | ~750–900µm+ | [[sources/kasuya-46-method-philocoffea]] |

## Grinder Conversion Tables

### C40 Traditional → Red Clix

Red Clix doubles click resolution. **C40 clicks × 2 = Red Clix equivalent.**

| C40 | Red Clix | Microns |
|---|---|---|
| 3–6 | 6–12 | 90–180 (espresso) |
| 20–30 | 40–60 | 600–900 (pour-over) |
| 30–40 | 60–80 | 900–1,200 (cold brew) |

**Red Clix resolution:** 1 click = 15µm (half of C40's ~30µm/click).

### C40 → C60 Baracuda

C60 uses GX50 Gold Clix drivetrain: 21µm per click.

| C40 | C60 | Microns |
|---|---|---|
| 3–6 | 4–9 | 90–180 (espresso) |
| 20–30 | 28–42 | 600–900 (pour-over) |
| 30–40 | 28–57 | 900–1,200 (cold brew) |

## Grind Texture Reference

| Label | C40 Clicks | Texture Feel |
|---|---|---|
| Fine | ~3–10 | Powder; clumps |
| Medium-fine | ~20–25 | Between table salt and fine sand; slight coarseness |
| Medium-coarse | ~25–30 | Coarse sand |
| Coarse | ~30–40 | Sea salt; granular |

## Calibrating to Zero

Turn dial fully clockwise until burr locks (handle cannot spin freely). That is 0 clicks. Do not over-tighten — the handle locking is the reference point, not further force.

## Key Sources
- [[sources/comandante-grind-size-chart]] — full reference chart; C40/C60/Red Clix tables

## Related Concepts
- [[concepts/dialing-in]] — variable priority order when adjusting a recipe
- [[concepts/v60]]
- [[concepts/graycano]]

## Open Questions
- Does the Kasuya 4:6 "medium-coarse" recommendation translate to ~25 clicks or ~28–30 clicks on C40? The recipe doesn't give click counts.
- How does burr wear on an aged C40 shift the effective µm per click?

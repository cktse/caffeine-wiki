---
title: "4:6 Method (Tetsu Kasuya)"
domain: brewing
tags: [v60, pour-over, 46-method, tetsu-kasuya, recipe, extraction-control]
source_count: 1
last_updated: 2026-06-17
---

# 4:6 Method (Tetsu Kasuya)

## Definition

A V60 pour-over recipe invented by Tetsu Kasuya that won the 2016 World Brewers Cup. Total brew water is divided 40:60. The 40% phase controls **flavor** (sweetness vs. acidity); the 60% phase controls **strength** (concentration). Each axis is adjustable independently, making the recipe systematic rather than technique-dependent.

## The Two-Axis Model

```
Total water = 40% (flavor) + 60% (strength)
                  ↓                  ↓
       Split into 2 pours     Split into 1–3 pours
       ratio = sweetness      count = concentration
```

**Flavor axis (40% phase — 2 pours):**

| First pour vs. second pour | Flavor result |
|---|---|
| First < Second (e.g. 50+70) | Sweeter |
| First = Second (e.g. 60+60) | Balanced |
| First > Second (e.g. 70+50) | Brighter / more acidic |

**Strength axis (60% phase):**

| Number of pours | Concentration |
|---|---|
| 1 pour | Lighter body |
| 2 pours | Medium |
| 3 pours | Stronger |

## Standard Recipe (20g / 300g / 1:15)

**Formula:** Each pour = dose × 3 g.

| Time | Pour | Cumulative | Phase |
|---|---|---|---|
| 0:00 | 60 g | 60 g | 40% — pour 1 |
| 0:45 | 60 g | 120 g | 40% — pour 2 |
| 1:30 | 60 g | 180 g | 60% — pour 1 |
| 2:15 | 60 g | 240 g | 60% — pour 2 |
| 2:45 | 60 g | 300 g | 60% — pour 3 |
| 3:30 | Remove dripper | | |

Wait for each pour to nearly fully drain before adding the next.

## Variation Examples (20g / 300g)

| Profile | Sequence |
|---|---|
| Standard balanced, lighter body | 60+60+180 (40% equal, 60% in 1) |
| Sweeter, medium body | 50+70+90+90 (40% sweet, 60% in 2) |
| Brighter, stronger | 70+50+60+60+60 (40% bright, 60% in 3) |

## Parameters

- **Ratio:** 1:15
- **Grind:** Medium-coarse to coarse (default: coarse)
- **Water:** Soft, purified, 30–50 mg/L hardness
- **Temperature by roast:**

  | Roast | Temp |
  |---|---|
  | Light | ~93°C |
  | Medium | ~88°C |
  | Dark | ~83°C |
- **Dripper:** Hario V60 (standard or Kasuya Model — Kasuya Model has ribs removed at bottom to slow flow and compensate for coarse grind)

## Connection to Kasuya's Switch Recipes

The 4:6 method's math appears in Kasuya's Switch work:
- 20g dose × 3 = 60g per pour → 5 pours × 60g = 300g = 1:15 ratio
- The 2025 "New Hybrid" Switch recipe also uses 20g / 300g / 1:15
- The temperature-by-roast table applies directly when dialling in any Kasuya Switch recipe

The 4:6 is the conceptual foundation; the Switch recipes are adaptations that layer in immersion phases on top of the same underlying extraction logic.

## Key Sources
- [[sources/kasuya-46-method-philocoffea]] — Kasuya's own description from Philocoffea

## Related Concepts
- [[concepts/v60]] — the dripper this method was designed for
- [[concepts/neo-switch]] — Kasuya's Switch recipes built on the same ratio and extraction philosophy
- [[concepts/dialing-in]] — the 4:6 method is itself a structured dialling-in framework

## Open Questions
- The "standard" illustrated example (60+60+180, 3 total pours) differs from the "basic formula" (5 equal pours of 60g each). Which is Kasuya's actual competition recipe?
- No explicit bloom step mentioned. Is the first 60g pour treated as bloom-and-continue, or does the dripper need a bloom pause before the timer starts?
- How does the Kasuya Model V60's removed-rib base change flow rate vs. standard V60, and does this affect grind recommendations for users without that specific dripper?

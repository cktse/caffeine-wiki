---
title: "Dialing In"
domain: brewing
tags: [espresso, pour-over, recipe-development, extraction, brewing-control-chart, tds, percent-extraction]
source_count: 1
last_updated: 2026-08-02
---

# Dialing In

## Definition

The iterative process of adjusting brew variables (grind, dose, ratio, temperature, time) until the shot or cup matches a target flavor profile.

## Variable Priority Order

When adjusting, change only one variable at a time. Work through this order:

**Grind Size → Water Temp → Brew Ratio → Dose → Water Minerals → Coffee Beans**

Grind is first because it has the largest effect per adjustment step. Water minerals and beans are last because changing them resets the whole calibration. (Source: [[sources/comandante-grind-size-chart]])

## Espresso Dialing-In Sequence

1. Fix dose (e.g. 18 g)
2. Fix target ratio (e.g. 1:2 → 36 g out)
3. Adjust grind until time falls in 25–30 sec window
4. Taste: sour → finer grind; bitter → coarser
5. Once time is right, adjust ratio if needed (richer = lower, lighter = higher)
6. Temperature last — only after grind and ratio are locked

## Pour-Over Dialing-In Sequence

1. Fix dose and ratio
2. Adjust grind for target total brew time
3. Taste: sour/weak → finer or hotter; bitter/harsh → coarser or cooler
4. Adjust pour technique (speed, number of pours) to shift body vs. clarity

## Setting the Target (Brewing Control Chart)

Dialing in is easier when the *target* is a coordinate, not a vibe. The [[concepts/brewing-control-chart]] gives a TDS × percent-extraction (PE) map: pick where you want the cup, then move there with grind/ratio.

- **Grind/ratio move you on the chart; measure TDS to locate yourself** (`PE = [TDS/(1−TDS)]×(R_brew − R_abs)`, R_abs ≈ 2.1).
- **Sweetness-forward drip target** (CK's default): low-to-mid TDS + **~18–21% PE** — the 'sweet' / bright-specialty zone, away from the high-TDS bitter/astringent corner.
- **Temperature is a fine-tune, not a mover**: at fixed TDS/PE it has little sensory impact (Batali et al. 2020) — which is why it sits last in the priority order above.
- Bypass ([[concepts/bypass]]) lets you hit a lower-TDS target *without* re-grinding — a vertical move on the chart.

## Related Concepts
- [[concepts/brewing-control-chart]] — the target-setting map for TDS/PE/ratio
- [[concepts/espresso-fundamentals]]
- [[concepts/v60]]

## Open Questions
- Is there a reliable TDS target that correlates with "dialed in" for specialty espresso? *(For **drip**, the BCC gives an answer: consumer-preferred zones cluster at low-to-mid TDS with PE ~18% (majority) or the bright/high-TDS-low-PE and dark/high-PE peaks (second segment). An espresso BCC does not yet exist — flagged as future work by Guinard et al. 2023.)*

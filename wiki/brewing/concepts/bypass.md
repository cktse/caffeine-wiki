---
title: "Bypass Brewing (Dilution Bypass)"
domain: brewing
tags: [pour-over, extraction, tds, strength, clarity, technique, 46-method]
source_count: 0
last_updated: 2026-08-01
---

# Bypass Brewing (Dilution Bypass)

## Definition

**Bypass** is the technique of directing part of the total brew water *around* the coffee bed — added straight to the cup or decanter — instead of pouring all of it through the grounds. The bypass water carries **zero dissolved solids**, so it dilutes the final beverage's strength without changing how much coffee was extracted.

The result: **extraction yield (EY) and beverage strength (TDS) become two independent dials.**

## Why It Matters (in this domain)

Conventional pour-over couples extraction and strength — if you want a lighter cup you brew a wider ratio, but that also changes contact time and extraction. Bypass breaks that coupling:

| Dial | Controlled by | Governs |
|---|---|---|
| **Extraction (EY)** | grind · temp · pour schedule · water through bed | sweetness, body, development |
| **Strength (TDS)** | bypass % | intensity vs. clarity/delicacy |

This is especially useful for **light and light-medium washed, floral coffees** where the goal is *full extraction sweetness in a delicate, clean cup*. You extract properly (say 1:15 through the bed for ~20% EY → sweetness and body), then add bypass to thin the strength and open up clarity — **without** under-extracting.

**Contrast the two ways to get a "clean, delicate" cup:**

| Approach | Mechanism | Sweetness | Risk |
|---|---|---|---|
| **Low-EY clarity** (strong ratio + short contact, e.g. 1:13 / 1–1.5 min) | Under-extract (~14% EY) so little bitterness/astringency is pulled | Sacrificed — sweetness/body left in the grounds | Sour, green, thin |
| **Bypass clarity** | Fully extract (~20% EY), then dilute strength | Kept — real extraction, then thinned | Watery if bypass too high |
| **Cold brew** (for reference) | Dilute a concentrate | Kept; but different aromatic profile | Distinct method, not interchangeable |

Bypass is the better route when your priority is **sweetness** (see [[shared/sweetness-perception]]) but the fully-extracted cup is too intense — which is CK's usual default.

## The Math

Because bypass water contains no solids, **total dissolved solids (beverage mass × TDS) is conserved** regardless of how much you bypass. So EY is computed the same way with or without bypass:

```
EY (%) = (final beverage mass × TDS%) / dose
Bypass fraction = bypass water / final beverage
```

The key move: **bypass changes TDS but not the numerator's product** — the solids were fixed the moment the water finished passing through the bed. Bypass only redistributes those solids across more liquid.

**On the Brewing Control Chart, bypass is a straight vertical move.** In [[concepts/brewing-control-chart]] terms (TDS vertical, percent-extraction PE horizontal), the through-bed brew sits at one (PE, TDS) point; adding bypass lowers TDS at constant PE, sliding the cup **straight down** — away from the high-TDS bitter/astringent upper band toward the lower 'sweet'/cleaner zone. That is the chart-level reason a bypassed cup reads cleaner and sweeter without losing the sweetness that came from full extraction. The canonical relation `PE = [TDS/(1−TDS)]×(R_brew − R_abs)` with **R_abs ≈ 2.1** (the retention constant we estimated empirically as ~2.0–2.3 g/g) comes from the same source.

## Worked Example (validated)

Yunnan Purple Leaf Caturra, K72 washed, roast 2/5 — Option A sweet 4:6 with bypass. Full recipe and sensory notes in [[sources/yunnan-purple-caturra-k72-label]].

- 15 g dose · brewed to **225 g through the bed (1:15)** · **+25 g bypass → 250 g total water**
- Measured: final beverage **~215 g**, **TDS 1.43%** → **EY ≈ 20.5%**
- Pre-bypass strength was ~1.62% (3.07 g solids / ~190 g); the ~25 g bypass (≈10% of the cup) pulled it to 1.43% — an ~11% strength drop, **EY untouched**.
- Result: "good balance of sweetness and clarity, still more coffee-like than tea-like." The body came from the 20.5% extraction; the bypass only trimmed intensity.

**Dialing the bypass:** to reach a softer ~1.30% TDS at the *same* EY, bypass ~47 g (≈19%) instead of 25 g. More bypass → more tea-leaning; less → more intense. Grind/temp stay put.

## Related Concepts
- [[concepts/brewing-control-chart]] — the parent TDS×PE×ratio chart; bypass is a vertical (TDS-down) move on it; shared R_abs/percent-extraction math
- [[concepts/46-method]] — the extraction framework this example sits on; bypass is a strength dial layered *after* the 4:6 axes
- [[concepts/dialing-in]] — bypass adds a strength lever that is independent of grind/temp/ratio
- [[concepts/fast-filters]] — an alternative clarity route (fine grind + fast flow) that works on EY/contact time, not dilution
- [[shared/sweetness-perception]] — why keeping EY high (vs. low-EY clarity) preserves perceived sweetness
- [[shared/astringency]] — light roasts are astringency-prone; bypass lets you avoid the over-extraction ceiling while still thinning the cup

## Open Questions
- Does bypass change **mouthfeel/body** perception beyond simple dilution, or is body purely an EY/TDS function? CK's cup stayed "coffee-like" at ~10% bypass — where does it start reading watery?
- Should bypass water be the **same mineral profile** as brew water, or does using a different water (e.g. higher-mineral) to bypass change perceived body/sweetness?
- Interaction with the low-EY-clarity method: is there a case for *combining* a slightly faster brew with light bypass, or do they redundantly target the same clarity goal?

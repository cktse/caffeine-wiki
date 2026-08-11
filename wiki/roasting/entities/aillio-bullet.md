---
title: "Aillio Bullet R2 Pro"
entity_type: product
domain: roasting
---

# Aillio Bullet R2 Pro

## What / Who

The Aillio Bullet R2 Pro is a professional-grade drum coffee roaster manufactured by Aillio (Denmark). It is the primary roasting tool in this wiki. The R2 Pro is an enhanced version of the Bullet R1 V2, targeted at prosumer and small-batch specialty roasters. Max batch size: ~1kg. Min meaningful batch: ~200–250g.

## Relevance

This is the user's roaster. All roasting profiles, DCT benchmarks, and roast development analysis in this wiki are calibrated to the Bullet R2 Pro unless otherwise stated. Parameters from other roasters are not directly transferable.

## Key Specifications

| Spec | Value |
|---|---|
| Roaster type | Drum + infrared |
| Max batch size | 1 kg green coffee |
| Min batch size (reliable) | ~200–250g |
| Power sources | Gas burner (P1–9) + infrared front element (F1–9) |
| Drum control | Drum speed D1–9 (affects conductive contact) |
| Airflow / fan | A1–9 (independent of heat; affects convection and smoke clearance) |
| Software compatibility | Artisan (primary); Roast.World (Aillio native cloud logging) |
| Temperature probes | Bean Temp (BT) + Environmental Temp (ET) + IBTS (infrared bean surface temperature) |

**IBTS (Infrared Bean Surface Temp)**: A key Bullet-specific feature — the IBTS probe reads bean surface temperature directly via infrared, eliminating the thermal lag of contact probes. IBTS-derived RoR is faster-responding and more accurate than traditional BT-derived RoR. Some Bullet-specific profile guidelines use IBTS charge temp rather than BT charge temp.

**IBTS evolution and Rao's 2020 comment**: In 2020, Scott Rao (inventor of DTR; see [[entities/scott-rao]]) commented that the single-point IR sensor on the Aillio Bullet v2 is "not more accurate; it is less" than the BT probe, and that "they have added a 128-point IR sensor to their new machine; having one is not reliable." The Bullet R2 Pro's 128-point IBTS array appears to be exactly the improved sensor Rao was anticipating — his critique was directed at the single-sensor v2, not the R2 Pro. Source: [[sources/coffee-roasting-fundamentals-rao-2020]].

## Control Map

| Knob | Range | Primary effect | Secondary effect |
|---|---|---|---|
| P (Power) | 1–9 | Gas burner heat output | Main RoR driver; 30–60s thermal lag |
| F (Infrared) | 0–9 | IR radiation to bean surface | Fast RoR response; useful in development phase |
| D (Drum) | 1–9 | Drum rotation speed | Controls conductive contact rate; D6 typical starting point |
| A (Airflow) | 1–9 | Fan speed / convective airflow | Higher A = lower RoR (pulls heat); removes smoke and chaff |

## Aillio Bullet vs. Conventional Drum

The main difference from a conventional drum roaster is the combination of IR element + IBTS probe. This gives:
1. **Finer RoR control**: IR responds in ~10s vs. ~45s for gas — allows correction in real time without the overshoot of gas adjustments
2. **IBTS accuracy**: surface temperature matches actual bean development better than a slow-response BT probe
3. **Batch size sensitivity**: profiles shift meaningfully between 250g, 500g, and 1kg; profile notes should always specify batch size

## Sourced Charge Temperature Data (Lindsey 2024)

From the first peer-reviewed study conducted on an Aillio Bullet (v2 — same platform as R2 Pro) at 500g batch with Ethiopian coffees:

| Coffee type | CT (BT probe) | Mass loss range achieved |
|---|---|---|
| Ethiopian natural (Chelbesa, 1,900–2,200m, 0.707 g/mL) | **330°F (~166°C)** | Widest: R0–R7 roast designations; reached second crack at R5 and R7 |
| Ethiopian washed (Yirgacheffe G0, 1,950–2,100m, 0.692 g/mL) | **340°F (~171°C)** | Narrower range; R0 and R1 were underdeveloped (<12% mass loss) |

**Key finding from this study**: Under identical recipe (same CT, same RoR shape, same post-FC time designation), Ethiopian naturals consistently achieved 2–3% higher mass loss than washed coffees. Do not assume the same profile applies equally to natural and washed coffees.

## Practical Starting Points (Partially sourced)

*CTs below derived from Lindsey 2024 Aillio Bullet v2 study (500g Ethiopian). Other parameters (total roast time, DTR) remain conventional estimates until additional roasting sources are ingested.*

| Target | CT (BT, Bullet) | Total roast time | DTR target | Notes |
|---|---|---|---|---|
| Light pour-over (Ethiopian washed, Geisha) | **~166–171°C** | 9–11 min | 17–20% | Conservative IR; sourced CT range |
| Light-medium pour-over (Ethiopian natural) | **~163–168°C** | 9–11 min | 17–20% | Lower CT for naturals — will achieve darker effective roast than washed at same CT |
| Medium-light pour-over (Colombian, washed) | ~170–175°C | 9–11 min | 20–23% | Standard approach; CT not yet sourced for Colombian specifically |
| Medium pour-over / light espresso | ~172–178°C | 10–12 min | 22–26% | More P time; slightly longer DT |
| Medium espresso | ~175–182°C | 10–13 min | 24–28% | Pull through 1C with more P; longer development |

*Batch size: 400–500g. Adjust CT upward ~3–5°C for 250g batches; downward for 800–1000g batches.*
*All DCT / Agtron verification required — profile conditions vary significantly by batch size and green coffee density.*

## Connections

- [[concepts/roasting-parameters]] — parameter definitions calibrated to Bullet context
- [[concepts/roaster-types]] — Bullet as a drum + infrared hybrid; heat source comparison
- [[roasting/overview]] — decision table uses Bullet as the reference roaster

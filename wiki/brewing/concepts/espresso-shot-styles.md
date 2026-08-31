---
title: "Espresso Shot Styles (Ristretto → Sprover)"
domain: brewing
tags: [espresso, shot-styles, ristretto, normale, lungo, allonge, turbo-shot, sprover, cafe-creme, ratio, grind, tds, extraction-yield, stock-machine]
source_count: 1
last_updated: 2026-08-30
---

# Espresso Shot Styles (Ristretto → Sprover)

## Definition

A **spectrum of six espresso recipes** produced on the *same* stock 9-bar machine by holding **dose, temperature, coffee, and pressure constant** and varying only two levers — **yield (brew ratio)** and **grind**. From most concentrated to most dilute: **Ristretto → Normale → Lungo → Turbo → Allongé → Sprover** (café crème). They are "all roughly espresso, just different iterations" (Hedrick).

This is the *menu* view of espresso; for the mechanistic why (pressure, flow, transport/diffusion, astringency) see [[brewing/concepts/espresso-fundamentals]].

## The spectrum (illustrative single pulls — [[brewing/sources/every-espresso-recipe-explained-hedrick]])

| Style | Ratio | Grind | TDS (typical band) | EY | Character |
|---|---|---|---|---|---|
| **Ristretto** | 1:1–1:1.5 | espresso-fine | 11–15% | ~19% | Thick body, concentrated, long coat; sweet+sour; suits dark roasts |
| **Normale** | 1:2 | espresso-fine | 9–12% | ~19% | The traditional shot; best balance/body on darker roasts; 25–30 s |
| **Lungo** | 1:3–1:4 | espresso-fine (same as normale) | 7–8% | ~22% | More extraction, smoother, diluted; runs hotter; astringency can creep in |
| **Turbo** | ~1:3 | coarser | 6.5–8% | ~18% | 7–15 s fast shot; fruity/aromatic, big acidity, preserves VOCs; ~5 bar peak |
| **Allongé** | 1:5–1:6 | coarser | 5–8% | ~22% | 30–40 s; between filter & espresso; bright, fruit-forward; go cooler |
| **Sprover** (café crème) | 1:8–1:12 | very coarse | 1.5–2.5% | ~20% | Espresso machine as no-bypass filter brewer; clean, watery; mocha-pot foam |

*Bands are Hedrick's stated ranges; EY figures are single measured pulls — treat as illustrative.*

## Why It Matters (in this domain)

- **Two levers, one machine.** You don't need special hardware to move across this whole map — just **ratio** (where you stop) and **grind**. This is the practical counterpart to the [[brewing/concepts/brewing-control-chart|Brewing Control Chart]]: each style occupies a different TDS/PE region.
- **Grind sets the extraction ceiling — not just flow.** Coarser grounds cap EY at a given contact time. That's why **Turbo** (coarse, ~1:3) extracts *less* (~18%) than **Lungo** (fine, 1:3, ~22%), and why **Allongé** (coarse, 1:5.6) only *matches* Lungo (~22%) — the coarse grind offsets its huge solvent volume. **EY is not monotonic with yield.**
- **Turbo debunks the 6-bar myth.** A 7–15 s shot physically cannot build 6 bar (Hedrick's hit ~5) — so **any** machine, even a 20-bar pump, produces a turbo. No OPV mod required. See the [[brewing/entities/christopher-hendon|Hendon]] & Cameron paper origin.
- **Big yield → go cooler.** The larger the yield, the hotter the cup; for **Allongé/Sprover** drop to **80–85 °C** to avoid astringency/bitterness ("a lot of what we love comes out at lower temps ~85 °C"). Consistent with the wiki's temperature-secondary finding for balanced regions, but here temperature is a *deliberate* astringency lever at extreme ratios.
- **Puck prep scales with grind.** Fine (ristretto/normale) → puck prep is critical; coarse (turbo/sprover) → forgiving. Use a spouted portafilter for messy high-yield styles.
- **Roast pairing.** Darker roasts → **normale/ristretto** (body, crema, puck integrity). Lighter roasts → **turbo/allongé/sprover** (bright/fruity) — but light roasts resist extraction and want a capable grinder (cf. [[brewing/concepts/espresso-fundamentals]] light-roast strategies).
- **EY dogma is optional.** Hedrick often targets **15–18% EY** (VOC preservation via fast shots), not the 18–22% convention; **ratio is the biggest single dictator** of EY.

## Relationship to the Rao/Decent framework

Hedrick's spectrum is **stock-machine-first**; Rao's ([[brewing/concepts/espresso-fundamentals]]) is **Decent/flow-control-first**. They agree on the physics (coarse + high flow favors light roasts; cool the big-yield styles) but differ on numbers and reach:

- **Allongé:** Rao 26–27% EY at 4.5 ml/s (Decent); Hedrick 22.25% at 1:5.6 on 9-bar. "Allongé" spans a wide EY depending on flow control and grind.
- **Sprover ≈ Filter3:** both use the espresso machine as a **no-bypass filter brewer**; Filter3 is 0-bar (Decent-only), Sprover is a very coarse 9-bar pull (any machine).

## Key Sources
- [[brewing/sources/every-espresso-recipe-explained-hedrick]] — the six-style spectrum with measured grind/dose/yield/TDS/EY; grind-ceiling logic; turbo 6-bar-myth debunk; temperature × yield; high-medium (practitioner/educator)

## Related Concepts
- [[brewing/concepts/espresso-fundamentals]] — the mechanistic layer (pressure, flow, transport/diffusion, astringency, light-roast strategies)
- [[brewing/concepts/brewing-control-chart]] — TDS×PE map each style occupies
- [[brewing/concepts/dialing-in]] — grind-first adjustment; single-variable discipline
- [[brewing/concepts/bypass]] — Hedrick's preferred alternative to lungo (dilute a ristretto)

## Open Questions
- Where does each style sit on the [[brewing/concepts/brewing-control-chart]] preference clusters (dome/"sweet" vs saddle/specialty)? Turbo/allongé look like the specialty-cluster corner.
- Does the coarse-grind "more even extraction" claim for turbo/sprover hold on typical home grinders (vs. flat commercial burrs), or is fines-content the limiter?
- Reconcile the allongé EY gap (Rao 26–27% vs Hedrick 22%) — is it flow control, grind, coffee, or measurement?

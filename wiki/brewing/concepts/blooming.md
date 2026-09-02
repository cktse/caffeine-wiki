---
title: "Blooming (& Pour Structure)"
domain: brewing
tags: [pour-over, bloom, off-gassing, co2, extraction-yield, tds, pours, agitation, pour-turbulence, bed-filtration, high-and-dry, decaf]
source_count: 2
last_updated: 2026-09-02
---

# Blooming (& Pour Structure)

## Definition

The **bloom** is the first small pour that wets the grounds and lets trapped **CO₂ off-gas** before the main pours. Its job isn't degassing for its own sake — it's to **expel CO₂ so diffusion (extraction) can proceed evenly**, and to let the grounds settle into a working **filter bed**. Bloom time is a real, measurable extraction lever; how many times and how hard you pour afterward is a second, related one.

## Bloom time → extraction (data)

Longer bloom **monotonically raises EY, TDS, and drawdown time** — but the **taste optimum is coffee-specific**, not "more is better." From Hedrick's controlled test (15 g : 250 g, 50 g bloom + single 200 g pour; [[brewing/sources/hedrick-blooming-pours-2024]]):

| Coffee | 30 s | 1 min | 2 min | Best |
|---|---|---|---|---|
| **Peru** washed, med-light | EY 17.2 % / 2:03 | 18.0 % / 2:32 | 18.5 % / 3:41 | **30 s** (lowest EY) |
| **Kenya** washed, Nordic light | EY 20.4 % / 2:33 | 20.8 % / 3:04 | 21.2 % / 4:08 | **2 min** (highest EY) |

30 s → 2 min: **+0.8–1.2 pp EY**, +0.07–0.08 % TDS, **+1:35–1:40 drawdown**.

**Rule of thumb:** the **gassier / lighter-roasted / fresher** the coffee, the **longer the bloom** it wants. The Nordic Kenya needed 2 min to fully off-gas; the med-light Peru was best at 30 s.

## Why the best bloom isn't the highest extraction

- **"High and dry."** Too short a bloom on a gassy coffee leaves grounds under-saturated — floating, clinging to the wall, **not** giving up solubles and **not** joining the filter bed. Result: muddy, uneven cup even at lower EY.
- **Even extraction reads as clarity + acidity.** Counter-intuitively, Kenya's **2 min** pull had the **highest EY *and* the most perceived acidity** — proper off-gassing → even extraction → vibrant, clean acidity. Under-bloomed 30 s was the muddiest. So bloom is an **X (balance)** lever *and* a **Y (clarity)** lever: it lifts EY and, done right, improves evenness.
- Bed "swelling" during bloom is CO₂ release + water spacing the particles, **not** particles swelling (Samo Smrke, [[brewing/entities/zhaw-coffee-excellence-center|ZHAW]]).

**Off-gassing also carries aroma away (peer-reviewed).** The same author's espresso study ([[brewing/sources/smrke-fines-espresso-2024]], Smrke et al. 2024) shows extraction isn't pure diffusion: **CO₂ degassing during brewing transports volatile compounds off** (before they dissolve), on top of pre-brew (grinding) desorption and post-brew evaporation. So a fuller bloom trades off — it degasses for even extraction, but aggressive/late CO₂ release is itself an aroma-loss channel. (In espresso, fast/low-yield "turbo" retains more fruity VOCs for the same reason.)

## Fewer pours = cleaner (the bed is a filter)

The **coffee bed itself filters microfines** — the number-one clarity tool in pour-over. Each additional pour works against it (reasoned, no data — [[brewing/sources/hedrick-blooming-pours-2024]]):

- disturbs the bed → **ejects more fines** through the paper → muddier cup;
- clogs filter pores → **longer drawdown** → more astringency/channeling;
- releases more CO₂ late → **upward channels** if the bloom didn't finish the job.

**Pragmatic advice:** minimise pours and dial the **bloom** instead — it's one variable that captures much of what many-pour schemes chase. (Contrast the [[brewing/concepts/46-method|4:6]] multi-pour approach, which trades some of this clarity for per-phase flavour/strength control.)

## Pour turbulence

*How* you pour sets agitation depth (an **X**/EY and evenness lever):

| Pour type | Agitation | Use |
|---|---|---|
| **Laminar** | pointed, shallow | gentler; decaf/high-fines (avoid clogging) |
| **Turbulent** (just below stream break-up) | deepest, full-bed | most effective even agitation; light/gassy coffees |
| **Droplet / osmotic** (broken stream) | minimal | dark roasts; deliberate under-extraction for balance |

## Special cases
- **S-bloom** (cold bloom to preserve VOCs) off-gasses less efficiently → needs a **longer** bloom.
- **Decaf** — little CO₂ (short bloom) but **lots of fines** → laminar pour, avoid clogging, target < 3 min drawdown.
- **Aging** — coffee off-gasses over time → grind **finer** as it ages.
- **Dark roast** — droplet/osmotic + no/short bloom to deliberately under-extract (fewer roasty/bitter notes).

## Grinder-agnostic recipe philosophy
Recipes that prescribe a grind size fail across grinders because **fines fraction varies** ([[brewing/concepts/particle-size-distribution|PSD]]) → different drawdowns/cups. Fix dose + water and steer with **bloom, pours, and timing** instead of chasing someone else's grind number.

## Key Sources
- [[brewing/sources/hedrick-blooming-pours-2024]] — controlled bloom-time experiment (TDS/EY/sensory) + reasoning on pours and pour turbulence; high-medium (practitioner + data)
- [[brewing/sources/smrke-fines-espresso-2024]] — peer-reviewed; CO₂ degassing + evaporation as aroma-loss channels (extraction ≠ pure diffusion); the off-gassing↔aroma trade-off; **high**

## Related Concepts
- [[brewing/concepts/particle-size-distribution]] — fines drive drawdown/clogging; why grind-specific recipes don't transfer
- [[shared/astringency]] — the bed-filtration model; fewer pours / degassed bed → less astringency
- [[brewing/concepts/bed-depth]] — deeper bed = better filtration; complements "fewer pours"
- [[brewing/concepts/46-method]] — the multi-pour counter-approach (per-phase control vs. bloom-led simplicity)
- [[brewing/concepts/dialing-in]] — bloom time and pour count as tuning knobs

## Open Questions
- Does the bloom→acidity result (higher EY yet more acidity, Kenya 2 min) generalise, or is it gas-load-specific?
- How much of Peru≠Kenya is roast/age/density vs. an intrinsic bloom response? (confounded in the source)
- Quantify "fewer pours = cleaner" — no TDS/fines-in-cup data yet.

---
title: "Bed Depth"
domain: brewing
tags: [pour-over, bed-depth, dripper-diameter, darcy, grind, brew-time, filtration, astringency, batch-brew, no-bypass, espresso-puck, body, sweetness]
source_count: 1
last_updated: 2026-08-31
---

# Bed Depth

## Definition

The **depth** of the coffee bed (how tall the grounds sit in the dripper) is a **fundamental brew parameter** — one you can't easily compensate for by changing other variables — ranking alongside ratio, grind, water composition/temperature, dripper geometry, grinder [[brewing/concepts/particle-size-distribution|PSD]], and the coffee itself (Gagné 2025). It is distinct from bed **width/diameter**, which mostly just sets **how much** coffee you brew.

## Diameter vs depth

In an idealized **no-bypass** brew, changing **dripper diameter** while holding **bed depth, ratio, coffee, temp, grind** fixed gives the **same brew time, TDS, and EY** — only a **larger batch**. (You pour faster to keep the same water-column height, since drip rate scales with bed area.) So the same recipe transfers across diameters — e.g. the same Pulsar recipe in the **Pulsar Mini** at **0.6× dose** (25 g → 15 g).

- **Dial-in cue:** across dripper sizes, don't judge by *total* drip rate (a narrow dripper shows fast droplets, not a stream, when correctly dialled) — watch the **water-column drop rate**, which is diameter-independent for a given recipe + depth.

## Four ways depth changes the cup

1. **Longer brew time and/or coarser grind** — a thicker percolation medium resists flow more (Darcy's law). Gagné's preference is a **compromise**: grind a bit coarser *and* accept longer times.
2. **More forgiving to disturbances/channels** — a channel of a given depth spans a *smaller fraction* of a deeper path, so its damage is diluted.
3. **Better filtration of insolubles** — fines, chaff, and *maybe* astringency molecules (see below).
4. **Different bottom-of-bed extraction** — the bottom meets more-concentrated / near-saturated water, slowing extraction of fast-diffusing compounds there.

(On a bypass dripper like the V60, depth also shifts the **[[brewing/concepts/bypass|bypass]]** fraction.)

**Net taste:** deeper beds give **more body, sweetness, and complexity** (even with light roast) and a **wider acceptable brew-time window** — i.e. more forgiving. Shallow/narrow beds are **finicky** and usually taste worse.

## Depth cheat sheet (Gagné; 1:17, EG-1 lab sweet burrs)

Both optimal **grind and brew time rise** with depth. Burr shifts are **relative µm** (absolute gaps don't transfer between grinders — or even EG-1 units).

| Bed depth | Brew time | Rel. burr gap | Dose (Pulsar) | Dose (Mini) |
|---|---|---|---|---|
| 14 mm | 3:20–3:40 | 0 | 20 g | 10.7 g |
| 15 mm | 3:30–4:00 | +15 µm | 22 g | 12 g |
| **17 mm** (his daily) | 3:40–4:40 | +40 µm | 25 g | 15 g |
| 19 mm | 3:53–5:20 | +65 µm | 28 g | 18 g |
| 20 mm | 4:00–5:40 | +80 µm | 30 g | 19.5 g |
| 23.3 mm | 4:20–6:45 | +125 µm | 35 g | 22.8 g |

Rows ≥20 mm extrapolate toward [[roasting/entities/scott-rao|Scott Rao]]'s parallel recommendation (deeper **20–23 mm**). Batch brews (best ~5–6 min vs pour-over ~3:30) are, in this view, **just deeper beds** — Rao's 90s rule of thumb put batch optimal depth at **3–5 cm**.

## Filtration model of astringency (hypothesis)

Astringent compounds are likely **long molecules** insoluble at brew temperature — far too small (<20 nm) to be sieved by inter-particle gaps. Gagné's suspicion: they **adsorb onto rough particle/fines surfaces**, trapped or released depending on bed **tortuosity/depth** and **microscopic fluid velocity** (set by pressure / water-column height). So **deeper bed + gentle velocity → better filtration → less astringency.** This coheres with the wiki's [[shared/astringency|filtration model of astringency]] and explains:
- a preference for a **narrow water column** (thicker beds tolerate taller columns without astringency);
- why espresso-machine filter coffee is cloudy/astringent (high pressure) *except* 0-bar **Filter3**;
- why shallow beds are finicky (small disturbances → poor-filtration channels; small column changes → big velocity swings).

**Caveat:** don't let the water column vanish — it cools the bed and **re-introduces air**, undoing the bloom (like watering a dry plant pot: trapped air obstructs flow).

## Espresso

Thicker **pucks** share the percolation mechanics, with two differences: (1) **filtration matters less** — high pressure dislodges what a filter bed would trap; (2) thicker pucks may yield **more crema** (with fresh / dark-enough coffee). Deep beds (updosing) already appear in [[brewing/concepts/espresso-fundamentals]] as a channeling-prevention tactic for allongé.

## Key Sources
- [[brewing/sources/gagne-bed-depth-2025]] — diameter=batch vs depth=flavor; four mechanisms; depth cheat sheet; surface-adsorption filtration model; batch-brew and espresso notes; high (practitioner-scientist)

## Related Concepts
- [[brewing/concepts/particle-size-distribution]] — deeper bed filters fines better; grind offsets pair with depth
- [[shared/astringency]] — the filtration model bed depth extends
- [[brewing/concepts/bypass]] — depth shifts the bypass fraction on cone drippers
- [[brewing/concepts/espresso-fundamentals]] — deep bed (updosing), puck depth, crema
- [[brewing/concepts/dialing-in]] — grind + brew-time both move with depth
- [[brewing/entities/nextlevel-pulsar]] — Pulsar / Pulsar Mini (depth-matched, diameter-scaled)

## Open Questions
- The surface-adsorption filtration mechanism is unproven ("no good demonstration") — needs data.
- How far does the linear grind/time extrapolation hold before deep beds behave qualitatively differently (toward batch-brew regimes)?
- Do the espresso filtration/crema intuitions survive measurement?

---
title: "Espresso Fundamentals"
domain: brewing
tags: [espresso, extraction, pressure, ratio, light-roast, blooming, allonge, turbo-shot, filter3, pre-infusion, astringency, quakers, channeling, cga, flow-rate, mass-loss, brew-ratio, transport, diffusion, filtration, suspension, grind-ceiling, solubility]
source_count: 4
last_updated: 2026-06-26
---

# Espresso Fundamentals

## Definition

Espresso is a concentrated coffee beverage produced by forcing hot water under pressure (7–10 bar) through a compacted bed of finely ground coffee. The result is a small, intense shot with emulsified oils and crema.

## Core Variables

| Variable | Typical Range | Effect |
|---|---|---|
| Dose (in) | 14–22 g | More dose = more body, slower flow |
| Yield (out) | 28–60 g | Higher yield = more liquid, lower concentration |
| Ratio (in:out) | 1:2 – 1:3 | Lower ratio = ristretto (intense); higher = lungo |
| Water temp | 88–94°C | Higher = more extraction; lighter roast needs higher temp |
| Pressure | 7–9 bar | 9 bar standard; lower for some naturals (7–8 bar) |
| Time | 22–35 sec | Within this window for balanced extraction |
| Grind | Fine (espresso range) | Finer = slower flow = higher extraction |

## Extraction Principles
- **Under-extracted**: sour, thin, fast flow → grind finer or increase dose
- **Over-extracted**: bitter, astringent, dark crema → grind coarser or reduce yield
- **Channeling**: uneven extraction lanes → distribution and tamping technique

---

## Roast Level → Optimal Brew Ratio (sourced: Rao 2025)

Roast degree (measured as mass loss) determines the optimal brew ratio and flow rate strategy. This is the cross-domain connection between roasting and brewing:

| Roast category | Approx. mass loss | Optimal brew ratio | Strategy |
|---|---|---|---|
| Nordic (extreme light) | ~11% | 4:1 – 5:1 | Allongé or Filter3; at edge of development |
| Light/Medium (typical Third Wave) | 12–13% | 3:1 | Standard specialty espresso; higher flow |
| Medium | 14–15% | 2:1 | Standard espresso; some roast character |
| Dark | 16–18% | 1:1 (ristretto) | Shorter shot to manage bitters; lower flow |
| Very Dark | ~20% | — | Beyond practical specialty range |

**Note**: mass loss categories align with Lindsey 2024's chemical thresholds: EY peaks at 12-14%, caffeine peaks at 14-16%, declining extraction >16%. See [[roasting/concepts/roasting-parameters]] for the full sourced mass loss table.

**Regional validation**: Northern Italy (lighter roasts, longer shots) and Southern Italy (darker roasts, shorter ristretto) independently arrived at this framework through practice (Rao).

---

## Flow Rate × Roast Level Mechanism (sourced: Rao 2025)

**Core principle**: match flow rate to roast degree.

| Roast | Preferred flow | Effect |
|---|---|---|
| Light roast | High flow (Allongé: 4.5 ml/sec) | Emphasizes fruit acids; tones down caramels and bitters |
| Dark roast | Low/medium flow | Prevents over-extraction of bitter-sweet compounds; shorter shot |

**Why lighter roasts taste better at higher flow rates**: Lighter roasts have fewer bitter-sweet compounds. High flow extracts fruit acids preferentially. Dark roasts have more and larger bitter-sweet compounds — high flow or long shots extract too many of them.

**Why extraction potential peaks at light/medium**: Dark roasting burns off soluble compounds, increasing the proportion of unextractable cellulose. A very dark roast will actually extract *lower* EY than a lighter roast from the same green coffee — despite being more porous. (Consistent with Lindsey 2024 data; see [[roasting/concepts/roasting-parameters]])

**Mechanism (not fully understood chemically)**: "We're not necessarily sure why" lighter roasts taste better at higher flow rates. Possible explanation via transport vs. diffusion (see below).

---

## Transport vs. Diffusion Extraction (Jonathan Gagné, via Rao 2025)

Two fundamental extraction mechanisms:

**Transport / Erosion**: Water physically strips solubles from the surface of ground particles as it flows past. Dominant in standard espresso. More flow → more transport.

**Diffusion**: Solubles from deeper cellular chambers dissolve into surrounding liquid and migrate outward. Dominant in immersion brewing (French Press, cupping, Blooming pause). Requires contact time, not flow.

Standard espresso: almost entirely transport.
Allongé: so much solvent (4:1–5:1) that some diffusion may occur — possibly explaining why it extracts differently from ristretto at same EY.
Blooming: explicitly combines diffusion (30-second pause) + transport (high-flow percolation).

Note: the flavor difference between flow rates (more fruit acids at high flow) is empirically confirmed but the transport/diffusion chemical mechanism is not yet verified by GC-MS analysis (Rao's own acknowledgement).

---

## Light-Roast Espresso Strategies (sourced: Rao 2025)

Light roasts are more resistant to giving up solubles quickly in standard espresso. Two broad strategies achieve high EY from light roasts:

| Strategy | Mechanism | Machine |
|---|---|---|
| **Contact time** (Blooming) | Long preinfusion pause dissolves material; high-flow phase extracts it | Decent Espresso only |
| **Solvent volume** (Allongé) | Large water volume + high flow rate; more solvent drives EY; high flow brings out fruitiness | Any machine capable of high flow |

General principle (Rao): **Lighter roasts taste better at higher flow rates** — high flow brings out fruitiness. This applies to both Allongé and the percolation phase of Blooming.

### Blooming Espresso (Decent Espresso specific)

**Cannot be done on standard machines** — a standard machine's 3-way valve releases pressure when flow stops; the Decent can hold pressure without flow.

**Profile**:
1. Maximum-rate pressurized preinfusion → fills entire puck in ~2 seconds (water visible at puck bottom immediately)
2. **~30-second pause** — flow stopped, pressure held (passively drops); coffee materials dissolve into the standing liquid
3. High-flow percolation phase — pushes dissolved material through and out

EY achievable: up to 29–30% with very light Kenyans/Ethiopians. "Challenging to dial in."

**Practical notes**: Fine grind required; headspace recommended (~1% higher EY vs. no-headspace; allows puck to swell like a V60 bloom); pressure flow limiter prevents excessive back-pressure.

### Allongé

Long espresso with high flow rate and high water volume. Works on any machine with adequate flow control.

- **Flow rate**: 4.5 ml/sec (sourced: Rao 2025) — "pretty fast for espresso"
- **EY**: 26–27% typical (sourced: Rao 2025); ratio 4:1–5:1
- High flow rate → fruitiness and fruit acid expression in light roasts; "borderline sour, wine-y" at extremes
- Large solvent volume → high EY via solvent quantity
- ~2.5× more concentrated than Filter3 (Decent)
- **Channeling risk**: long water volume amplifies any puck weakness; requires deep bed (updosing), careful puck prep, or Decent's adaptive flow profiling to manage
- Validated at commercial scale: Rao served ~150 Allongés/day at his Montreal café with dedicated grinder and puck prep routine

### Turbo Shot (Allongé alternative for challenging setups)

High-flow short shot — gets the high-flow fruit acid emphasis without the long water volume that amplifies channeling.

- High flow rate (Turbo Turbo variant: ~3.5 ml/sec) but stopped shorter than Allongé
- Lower channeling risk than full Allongé
- For: machines without Decent's adaptive flow profiling; imperfect puck prep situations; moderate fruit acid expression vs. full Allongé slap

### Filter3 (Decent Espresso specific)

Converts the Decent into a no-bypass filter brewer. Water dispensed at **zero pressure** (unique to Decent).

**Setup**: 22g coffee in ~8.5cm deep basket; paper filter below; 0-bar water dispense; ~4 min brew time; extremely coarse grind (coarsest setting on most grinders).

**No-bypass advantage**: V60 allows 20–30% bypass (water exiting without touching all grounds). Filter3 forces 100% of water through the bed → more even extraction → coarser grind possible → lower astringency risk.

**Sensory**: Clean, floral, rarely astringent; lower concentration than Allongé.

**Practical tips**:
- Check liquid level at 100 seconds — should be halfway up the basket; adjust grind accordingly
- Use Bluetooth scale: stop-by-weight 20g before target (Decent's flow calculation is inaccurate at 0 pressure on early brews in a session)
- If bed dries out near end: increase flow rate in the final 30 seconds

### Channeling Prevention — Deep Bed and Paper Filters (sourced: Rao 2025)

**Deep bed (updosing)**: A deeper puck makes it harder for channels to reach all the way through the bed and extract astringent suspended particles. Rao used this at his Montreal café for Allongé production. Practical in any machine.

**Paper filter on top of puck**: Water pools above the filter before passing through → near-uniform initial wetting of the coffee bed, vs. jet-based spot wetting from a shower screen. "Definitely can help" especially on standard machines. Top filter helps more than bottom filter.

**Paper filter on bottom**: Allows slightly finer grind; modest channeling benefit. Rao notes it helps "a smidge."

New Freckles/Dimples shower screens (Decent) serve the same function as a top paper filter — intentionally uneven water distribution to compensate for radial extraction differences in the puck.

---

## Dialing-In Philosophy (sourced: Rao 2025)

**Single variable principle**: Keep the recipe (dose, ratio, flow rate) constant across all coffees. Only adjust:
1. **Grind setting** — to control flow rate and puck resistance
2. **Dilution at end** — if TDS is too high for the cup preference

"If you start changing grind and dose and recipe, you can get lost pretty easily and not really know how to get back to the standard recipe."

**Origin-based extraction differences**: Ethiopian and Kenyan coffees extract notably higher than Colombian or Guatemalan coffees (all else equal). Rao's response: accept this and dilute the higher-extracting lots to target TDS, rather than changing the recipe for each origin.

**Rao's TDS target (filter coffee)**: 1.35–1.4 — "strong enough to be pleasing but weak enough to differentiate lots of flavors."

---

## Pre-Infusion Mechanics (sourced: Rao 2025 / Buckman)

**Maximum flow pre-infusion is better than slow pre-infusion.**

- **Slow pre-infusion (e.g., 4ml/sec)**: top of puck contacts water first; over-extracts top while under-extracting bottom → severely uneven extraction gradient across puck depth. The early Decent DE1 used 4ml/sec and had a "channeling monster" reputation because of it.
- **Fast/maximum pressurized pre-infusion**: water reaches bottom of puck in ~2 seconds → entire puck contacts solvent simultaneously → more even extraction.

**Headspace**: ~1% higher EY with headspace during long pre-infusion (allows puck to swell). Particularly relevant for Blooming and any long pre-infusion style.

---

## Astringency in Espresso (sourced: Rao 2025; Gagné 2022)

Three sources, in order of prevalence (Rao 2025 framework):

| Source | Mechanism | Fix |
|---|---|---|
| **Channeling** | Astringent particles are *suspended* (not dissolved); exit preferentially through channels or bypass; evidence: nylon filters remove 75–80% of astringency | Distribution, tamping, puck prep; no-bypass methods (Filter3); even pre-infusion |
| **Quakers** | Immature beans carry astringent compounds and produce a dry sensation that stops aftertaste; even one in a cupping bowl disrupts the cup | Green bean sorting; prefer washed (float step removes quakers) over natural for low-quaker lots |
| **Severe underdevelopment** | Excess CGA (chlorogenic acid) remains from roasting; CGA is astringent; breaks down during adequate roasting | Roast to minimum viable development (see [[roasting/concepts/roasting-parameters]]); don't drop too early |

**The filtration model (Gagné 2022)**: Astringent compounds are nearly insoluble at typical brew temperatures — they float as suspended particles in the slurry. Avoiding astringency is therefore primarily a **filtration** problem: a thick, flat, undisturbed bed with slow, even water flow physically filters them out. Channeling creates astringency not by over-extracting, but by short-circuiting the bed's filtration function.

**Why espresso is inherently astringent**: 9-bar pressure forces faster microscopic flow between particles, dragging undissolved astringent particles through even a well-prepared bed. The rich texture and intensity of espresso typically masks this. Filter3 (0 bar) is rarely astringent for the opposite reason.

**Grind size ceiling**: grinding finer liberates more astringent compounds by breaking more coffee cells (proportional to total surface area). Beyond a certain grind size, even perfect puck prep and even flow cannot filter out all liberated particles — a hard ceiling beyond which no technique helps.

**CGA and filtration — partially reconciled (Rao 2020)**: Rao's 2020 post describes CGA as a "large molecule" that "extracts less readily" than most coffee solubles. This is consistent with Gagné's model: CGA's incomplete dissolution at typical brew temperatures leaves a suspended fraction that the bed can filter out. The apparent conflict ("CGA is soluble → can't be filtered") is resolved — CGA is soluble in principle but only partially dissolved during actual brewing. Whether the specific compound Smrke's colleagues identified (Gagné 2022) is CGA or something else remains unknown.

The "over-extraction causes astringency" belief is largely incorrect — the primary mechanism is suspended particle filtration, not dissolved over-extracted compounds.

See [[shared/astringency]] for the full filtration model, temperature and pressure effects, and the decaf observation. See [[shared/quakers]] for quaker sorting protocols.

---

## Key Sources

- [[brewing/sources/rao-blooming-filter3-quakers-2025]] — Rao 2025 Decent Espresso masterclass; Blooming/Allongé/Filter3 techniques; astringency framework; quaker sorting; pre-infusion mechanics; **high-medium (practitioner)**
- [[brewing/sources/rao-allonge-roast-flow-2025]] — Rao 2025 Decent Espresso masterclass; roast level → brew ratio decision table; flow rate × roast level mechanism; transport/diffusion framework; Allongé specifics (4.5 ml/sec, 26-27% EY); Turbo shot; extraction potential by roast degree; **high-medium (practitioner)**
- [[brewing/sources/gagne-astringency-mechanism-2022]] — Gagné 2022 (coffeeadastra.com); filtration model for astringency; grind-size ceiling; pressure effect; 70°C experiment; decaf observation; **high-medium (practitioner-scientist)**
- [[brewing/sources/rao-astringency-management-2020]] — Rao 2020 (scottrao.com); CGA as large molecule extracting less readily (reconciles with Gagné model); diagnostic decision tree (channeling → cupping test → roast batch comparison); **high-medium (practitioner)**

## Related Concepts
- [[concepts/dialing-in]]
- [[shared/astringency]] — full filtration model; grind-size ceiling; pressure and temperature effects; CGA mechanism tension
- [[shared/quakers]] — immature beans; sorting; cup impact on astringency
- [[roasting/concepts/roasting-parameters]] — CGA: underdevelopment leaves excess CGA → astringency
- [[brewing/entities/decent-espresso]] — machine enabling Blooming and Filter3
- [[brewing/entities/jonathan-gagne]] — originator of the filtration model

## Open Questions
- How does high-altitude bean density (harder bean) change grind-extraction relationship at espresso?
- Is there a specific EY or Agtron threshold below which underdevelopment-sourced CGA astringency becomes perceptible? Rao identifies it as "severe underdevelopment" but no quantitative threshold is given.
- Does the Blooming technique's 30-second pause produce a different extraction profile from a simple long-preinfusion without the pause? (The pause allows dissolution into the standing liquid, not just wetting — this is mechanically different from slow flow preinfusion)
- What is the specific compound Smrke's colleagues identified as the primary astringent compound (Gagné 2022)? Best candidate is CGA (large molecule, less-readily-extracting — Rao 2020), but identity still unconfirmed.

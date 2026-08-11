---
title: "Astringency in Coffee"
domain: shared
tags: [astringency, filtration, grind-size, solubility, suspension, channeling, quakers, cga, decaf, espresso, filter-coffee, temperature, pressure]
source_count: 2
last_updated: 2026-06-26
---

# Astringency in Coffee

## Definition

Astringency is a tactile sensation of dryness, roughness, or puckering in the mouth, produced when certain compounds interact with proteins in saliva. In coffee it appears as a dry finish that cuts the aftertaste short and leaves a rough, persistent coating on the palate.

It is distinct from bitterness: bitterness is a taste; astringency is a texture/mouthfeel.

## The Filtration Model (Gagné 2022, via Smrke)

Jonathan Gagné ([[brewing/entities/jonathan-gagne]]), physicist and author of "The Physics of Filter Coffee," proposed in 2022 that astringency in coffee is primarily a **filtration problem**, not an over-extraction or flow-evenness problem. The model was developed from a conversation with food scientist Samo Smrke (ZHAW) and backed by empirical experiments.

**Core mechanism:**
- The compound(s) responsible for astringency in coffee are nearly **insoluble** at typical brew temperatures (≤90°C)
- They therefore exist as **suspended undissolved particles** in the slurry — not dissolved compounds
- A thick, flat, undisturbed coffee bed with slow, even water flow **physically filters them out**
- When filtration fails (channeling, bypass, high pressure, unevenness), suspended particles reach the cup

**Common misconception corrected**: "channeling causes astringency by over-extracting the coffee along the channel" is largely incorrect. Channeling causes astringency by creating a path from the slurry to the cup that bypasses the coffee bed's filtration function. Even a fully saturated slurry (long steep) becomes astringent during uneven drawdown because the undissolved particles are still present regardless of how saturated the dissolved compounds are.

**The specific compound**: not publicly named as of August 2022 (withheld by Gagné pending peer review by Smrke's colleagues). Wine tannins — the primary astringent compounds in wine — are NOT found in significant quantities in coffee brews.

## Sources of Astringent Material in the Cup

Three identified sources — different root causes, not all the same mechanism:

| Source | Root cause | Primary domain | Fix |
|---|---|---|---|
| **Channeling / poor filtration** | Uneven water flow bypasses coffee bed filtration; high pressure drags particles through; fine grind liberates too many particles to filter | Brewing | Even distribution + tamping; deep bed; slow flow; top paper filter; avoid high pressure for filter contexts; stay above grind-size ceiling |
| **Quakers** | Immature beans from underripe cherries; carry astringent material; produce a dry sensation that truncates aftertaste | Sourcing / Green coffee | Green bean sorting; prefer washed coffees (float test removes quakers); optical sorting |
| **Severe underdevelopment → CGA** | Excess chlorogenic acid (CGA) remains when roast is dropped too early; Rao attributes this to undissolved CGA | Roasting | Roast to minimum viable development; see [[roasting/concepts/roasting-parameters]] |

**CGA and the filtration model — partial resolution (Rao 2020)**: Rao's 2020 blog post describes CGAs as "large molecules" that "tend to extract less readily than most other coffee solubles." This characterization is actually consistent with Gagné's filtration model: CGA's large molecular size and slower/incomplete dissolution at typical brew temperatures means a meaningful fraction remains undissolved during brewing — making it amenable to filtration by the coffee bed. The apparent tension ("CGA is soluble → can't be filtered") is resolved: CGA is soluble in principle, but under real brewing conditions, its incomplete dissolution leaves suspended particles that the bed can filter out.

**What remains unresolved**: Gagné (via Smrke's 2022 communication) implies a specific compound was identified — and Gagné withheld its name pending peer review. Whether that compound IS CGA, a CGA derivative, or something else entirely is unknown. Tannins are not the answer — wine tannins were searched for in coffee and not found in significant quantities (Gagné 2022). CGA is the best current candidate but not confirmed.

**Note on Rao's 2020 "immersion brewing" claim**: Rao states that "astringency is much less likely to occur in immersion brewing due to the lack of channeling." This holds for channeling-sourced astringency specifically. It does NOT hold for: quaker-sourced astringency (quakers cause astringency even in cupping bowls — Rao 2025); or for uneven drawdown from a long saturated steep (Gagné 2022, Trinity One observation). Updated understanding: immersion prevents channeling but does not guarantee zero astringency if other sources are present.

## Grind Size Ceiling

Grinding finer liberates more astringent compounds by exposing more broken coffee cells. The amount liberated is **proportional to total particle surface area**. Beyond a certain grind size, even optimal filtration (thick, flat, undisturbed bed; even slow flow; no bypass) cannot filter out all liberated particles — you hit a hard grind-size ceiling.

This explains why very-fine-grind experiments (near espresso grind on the SOL dripper with paper filter + thick bed + no bypass + apparently even flow) still produced unavoidable astringency. (Gagné & Thibaut Paggen, Canadian Roasting Society experiment)

## Pressure Effect

Higher brew pressure → faster microscopic water flow between particles → more effective dragging of undissolved particles through the bed.

- Espresso (9 bar) is inherently astringent — the pressure overrides the bed's filtration capability. The rich texture and intensity of espresso typically masks this, but it is present.
- Hard Aeropress pressing produces more astringency and cloudiness than a gentle press (James Hoffman and Gagné confirmed empirically)
- Pre-infusion with fast flow before the bed is evenly wetted: increased astringency risk from uneven initial saturation

**Why Filter3 is rarely astringent**: 0-bar water dispense = no pressure → optimal low-pressure filtration through the bed.

## Temperature Effect

Lowering brew temperature reduces astringent compound solubility even further — a smaller fraction of the total compound pool dissolves, meaning fewer particles are released.

**Empirically tested at 70°C** (Gagné, Thibaut Paggen, Decent machine testers):
- EY ~27% achievable without perceptible astringency
- Finer grind possible than at normal temperatures
- BUT: cup profile significantly less interesting — "earthy, chocolaty, nutty, vegetal"; much less vibrant acidity
- Scott Rao: "Oh yes, I noticed this years ago but the cup profiles were always boring."

**Upper threshold (~95°C)**: Gagné observed from Hario siphon experiments that maintaining slurry temperature consistently above 95°C always produced poor cups — suggesting a threshold above which astringent compounds dissolve in sufficient quantity to guarantee astringency.

**Practical verdict**: low-temperature brewing is not a workable solution for everyday high-quality coffee. The flavor cost is too high. But it confirms the mechanism.

## Decaf and Astringency

Decaffeinated beans appear nearly immune to astringency (Gagné observation; consistent with Rao's Filter3 note that decaf works especially well). The decaffeination process — water, CO₂, or solvent-based — appears to affect or destroy the specific astringent compound.

This implies:
- The astringent compound is sensitive to the chemical conditions of decaf processing
- Decaf beans liberate fewer astringent particles regardless of grind size
- Decaf is useful for testing very fine grind / high-EY recipes without astringency risk

## Diagnosing Astringency — Decision Protocol (Rao 2020)

| Step | Observation | Conclusion | Fix |
|---|---|---|---|
| 1 | Previous brew of the same roast batch was non-astringent | Channeling caused the current brew's astringency | Better technique or coarser grind |
| 2 | Can't rule out channeling → cup the coffee; cupping is non-astringent | Channeling was the cause (not the beans or roast) | Better distribution, tamping, or puck prep |
| 3 | Both percolation AND cupping (immersion) are astringent | Not (or not only) channeling | Proceed to steps 4 and 5 |
| 4 | Some roast batches astringent, others not | Roast development is the variable | Fix roasting: more development time |
| 5 | All roast batches astringent even in cupping; you are confident none are underdeveloped | Green coffee quality issue | Underripe cherry (quakers); address at sourcing stage |

**Note on Step 3 limitation**: Rao's 2020 claim that immersion brewing prevents channeling astringency is correct, but quaker-sourced astringency still appears in cupping (Rao 2025). If all roast batches of a coffee are astringent in cupping, consider quaker prevalence before concluding it's all underdevelopment.

## Practical Brewing Implications

| Goal | Action | Why |
|---|---|---|
| Reduce astringency in pour-over | Thick, flat, undisturbed bed; even water distribution; no bypass; slow flow | Better filtration of suspended particles |
| Reduce astringency in espresso | Even distribution + tamping; updose (deep bed); top paper filter; stay above grind-size ceiling | Better filtration; fewer particles liberated |
| Achieve high EY without astringency in filter | Standard temperatures, coarser grind side of ceiling; OR no-bypass brewer (Filter3) | Filtration conditions determine the ceiling |
| Push beyond normal fine-grind ceiling | Dramatically lower temperature (70°C) — possible at flavor cost only | Reduces compound solubility to near-zero |
| Understand Filter3's clean cup | 0-bar, slow flow, deep basket, thick bed: optimal filtration conditions | Filtration model predicts exactly this |
| Understand espresso channeling astringency | Channeling bypasses the bed filter → suspended particles reach cup directly | Filtration model (not over-extraction) |

## Related Concepts

- [[brewing/concepts/espresso-fundamentals]] — astringency in espresso context; Gagné's filtration model integrated; three sources table
- [[shared/quakers]] — quakers as astringent material source; sorting protocols
- [[roasting/concepts/roasting-parameters]] — CGA: underdevelopment leaves excess CGA → possible astringency via dissolved mechanism
- [[brewing/entities/jonathan-gagne]] — originator of the filtration model
- [[brewing/entities/decent-espresso]] — Filter3 and Blooming as high-EY low-astringency strategies consistent with Gagné's model

## Understanding Evolution (Timeline)

The astringency model in this wiki reflects sources from 3 different points in time:

| Year | Source | View |
|---|---|---|
| 2019 | Gagné (coffeeadastra.com) | Chemistry framing: CGA + wine tannins as candidates; tannins may apply |
| 2020 | Rao (scottrao.com) | Practical guide: polyphenols (CGA + tannins) as mechanism; CGA = large molecule, extracts less readily; channeling = primary risk; diagnostic protocol |
| 2022 | Gagné (coffeeadastra.com) | Filtration model: compound nearly insoluble → suspended particles; filtration, not flow evenness; tannins NOT found in coffee; compound identity withheld pending peer review |
| 2025 | Rao (Decent masterclass) | Adopts Gagné's suspended-particle language; nylon filter evidence; quakers cause astringency even in immersion |

Rao's 2020 framing (CGA as large molecule extracting less readily) is not contradicted by Gagné 2022 — it's partially consistent. Rao's evolution from "CGA + tannins" (2020) to "suspended particles" (2025) reflects Gagné's influence.

## Key Sources

- [[brewing/sources/gagne-astringency-mechanism-2022]] — Jonathan Gagné 2022; coffeeadastra.com; primary source for the filtration model; empirically tested; **high-medium (practitioner-scientist with food scientist input)**
- [[brewing/sources/rao-blooming-filter3-quakers-2025]] — Rao 2025 Decent Espresso masterclass; three-source astringency framework; cites Gagné's suspended-particle theory; nylon filter evidence; **high-medium (practitioner)**
- [[brewing/sources/rao-astringency-management-2020]] — Rao 2020 (scottrao.com); CGA as large molecule / less-readily-extracting; diagnostic decision tree; **high-medium (practitioner)** — predates Gagné's 2022 filtration model; the CGA "large molecule" framing reconciles the two

## Open Questions

- What is the specific chemical compound responsible for filtration-type astringency? Best current candidate: CGA (consistent with large molecule / less-readily-extracting description); but Smrke's colleagues may have identified something specific (withheld 2022; status of that peer-review paper unknown in this wiki)
- Does quaker-sourced astringency operate via the filtration mechanism (undissolved particles from immature bean chemistry) or via a dissolved-compound pathway?
- Is there a per-dripper, per-dose quantitative grind-size ceiling? Does bed depth shift it meaningfully?
- Can advanced filtration materials (metal matrix filters with micron-sized pores) push the grind ceiling below what paper filters achieve?
- Does the ~95°C upper threshold vary by roast level, coffee origin, or processing method?
- How much excess CGA in an underdeveloped roast is required before astringency becomes perceptible? (Rao identifies "severe underdevelopment" but no quantitative threshold)

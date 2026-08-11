---
title: "The Effect of Roast Development Time Modulations on the Sensory Profile and Chemical Composition of the Coffee Brew as Measured by NMR and DHS-GC–MS"
domain: roasting
date_ingested: 2026-06-26
source_type: paper
tags: [roasting, dtr, development-time, sensory, nmr, gc-ms, sweetness, diacetyl, body, baked-roast, pyrazines, cga, acidity, body-finding, agtron]
raw_path: "raw/roasting/The Effect of Roast Development Time Modulations on the Sensory Profile and Chemical Composition of the Coffee Brew as Measured by NMR and DHS-GC–MS.md"
---

# The Effect of Roast Development Time Modulations on Sensory Profile and Chemical Composition

**Source**: Alstrup, J.; Petersen, M.A.; Larsen, F.H.; Münchow, M. *Beverages* **2020**, *6*(4), 70. DOI: 10.3390/beverages6040070.
**Credibility**: **High-Medium** — Peer-reviewed (*Beverages*, MDPI open access; moderate prestige); multi-method analytical design (NMR + DHS-GC-MS + PLS); 46 professional coffee tasters from Nordic Roaster Forum 2017 (experienced but not Q-graders or trained panelists); single origin (Colombian washed); single roast degree (Agtron 76); French Press brewing (affects body result interpretation); mild COI: CoffeeMind (Münchow's company) supplied coffee and roasting equipment, though no external funding declared.

**Note on paper relationships**: This is a *different paper* from "Münchow, M.; Alstrup, J.; Steen, I.; Giacalone, D. Roasting Conditions and Coffee Flavor: A Multi-Study Empirical Investigation. *Beverages* **2020**, *6*, 29" (doi: 10.3390/beverages6020029) — cited here as reference [^4]. The multi-study paper (Münchow 2020) is the one Scott Rao referenced regarding smooth RoR and baked defect detection. This paper (Alstrup 2020) specifically isolates development time with full chemical analysis. They are companion papers from the same CoffeeMind-affiliated research group.

## Summary

A controlled study isolating development time (DT) as the sole variable across four roast profiles (Fast/Medium/Slow/Baked) at identical roast color (Agtron 76 ± 1) on a 1kg Probat Probatino, Colombian washed coffee. Multi-method analysis found statistically significant DT effects on 8 of 9 sensory descriptors. Fast DT (90s after first crack) produced fruity, sweet, acidic cups; Baked DT (390s) produced roasted, nutty, bitter cups. Body was the sole exception — no effect of DT detected (p = 0.37). The study identifies diacetyl (2,3-butanedione) and 2,3-pentanedione as the primary sweetness-associated compounds in roasted coffee, with both peaking at short development times.

## Experimental Setup

| Parameter | Value |
|---|---|
| Origin | Colombian washed (Juan Guillermo Henao, Marsella) |
| Altitude | 1,200–1,800 m ASL |
| Moisture / density | 10% / 880 g/L |
| Screen size | 17 |
| Roaster | Probat Probatino 1 kg drum |
| Software | Cropster |
| Roast degree (target) | Agtron 76 ± 1 (Javalytics Gourmet scale) |
| Brewing | French Press; SCA protocol; 5.5g/100mL; 95°C; 4 min |
| Panel | 46 experienced coffee tasters (Nordic Roaster Forum 2017, Oslo) |
| Chemical analysis | NMR (Bruker 500MHz, 12 compounds) + DHS-GC-MS (146 peaks, 39 identified with RI) |
| Statistical method | ANOVA + Tukey's post-hoc; PLS multivariate (85% variance explained by 2 components) |

**Development time profiles (all at same Agtron 76 ± 1)**:

| Profile | DT after 1C | Drop temp (BT, Probatino) |
|---|---|---|
| Fast | 90s | 204.1°C |
| Medium | 143s | 201.2°C |
| Slow | 266s | 198.4°C |
| Baked | 390s | 191.1°C |

Note: Lower drop temperature for Baked is required to achieve same color at extended DT — the longer post-crack time allows more color development at lower heat. These temperatures are on a Probat Probatino BT probe and **are not directly comparable to Aillio Bullet BT or IBTS readings**.

## Key Claims

### 1. DT has large sensory effects at constant roast color

At identical Agtron 76, DT modulation from 90s to 390s produced statistically significant differences in 8 of 9 descriptors:

| Descriptor | Fast | Medium | Slow | Baked | p-value |
|---|---|---|---|---|---|
| Sweetness | **8.7** | 8.3 | 7.2 | 6.3 | <0.001 |
| Acidity | **8.5** | 7.6 | 5.8 | 5.4 | <0.001 |
| Fruit+Berry | **7.3** | 6.4 | 4.6 | 4.4 | <0.001 |
| Clean cup | **7.5** | 6.7 | 5.5 | 5.5 | <0.001 |
| Roasted | 5.4 | 6.3 | 8.3 | **8.8** | <0.001 |
| Nutty+Chocolate | 6.0 | 6.9 | 7.9 | **8.4** | <0.001 |
| Bitter | 5.7 | 6.5 | 8.0 | **8.6** | <0.001 |
| Astringency | 5.4 | 6.0 | 6.7 | **7.1** | <0.001 |
| **Body** | 6.9 | 7.4 | 7.2 | 7.1 | **0.37 — NO EFFECT** |

(Scores on 15-point scale; bold = significantly highest for that descriptor. Same letter = not significantly different in Tukey's test.)

**Implication**: Roast color (Agtron) alone is an insufficient quality control metric. Two coffees at the same Agtron can taste dramatically different. DT must be measured and controlled alongside color.

### 2. Sweetness mechanism — diacetyl and 2,3-pentanedione

No carbohydrates were detected above 0.5 mM in any sample (NMR detection limit). Sucrose taste threshold is >20 mM — confirming coffee sweetness is not caused by sugar at any DT.

The two compounds most strongly correlated with higher Sweetness scores in the Fast roast:
- **2,3-Butanedione (diacetyl)**: butter, caramel, butterscotch aroma; highest in Fast (1213 area), lowest in Baked (838); degraded by extended DT (p < 0.001). Widely used in food flavoring of sweet products. This is a Maillard-derived compound from sugar fragment degradation.
- **2,3-Pentanedione**: similar butter/caramel character; highest in Fast (2434), lowest in Slow/Baked (~2000); not detected in Fast (unclear in paper — likely measurement artifact for the "xx" cell). p < 0.001.

Both are diketones formed in the Maillard phase and degrade with extended roast development time. Fast DT → high diacetyl → high sweetness perception. This provides a specific chemical-to-sensory link for the aromatic sweetness mechanism established in [[brewing/sources/sweetness-perception-sca-2024]].

**Also in Fast**: higher furfural (2701 vs. 2222 in Baked) — sweet/woody aroma; higher hexanal (green/apple); benzeneacetaldehyde (honey/rose/floral); (E)-2-butenal (flower).

**Cross-domain note**: Diacetyl (2,3-butanedione) is also produced by lactic acid bacteria during extended fermentation — documented in Chiroso extended fermentation study ([[varietals/sources/chiroso-sensory-pazmino-2022]]). Two routes to the same sweetness compound: fast DT roasting OR extended post-harvest fermentation. See [[shared/fermentation-flavor-compounds]].

### 3. CGA and acidity — degrade with DT

5-CQA (3.52 → 2.44 mM) and 3-CQA (1.24 → 1.00 mM) were both higher in Fast and declined with DT. The paper states these are precursors to bitter-tasting quinic acid and quinide. More DT → less CGA → more bitterness from CGA degradation products. Consistent with and adding DT granularity to [[roasting/sources/caffeine-extraction-roast-lindsey-2024]], which showed CGA decreases with overall roast degree.

**All acids decline proportionally**: Formic, citric, malic, acetic — all highest in Fast, all lowest in Baked. The *ratio* of acids to each other does **not** change with DT. "Development time does not allow for such alterations." This contradicts the roaster belief that DT can selectively emphasize specific acids (e.g., more malic character from shorter DT).

### 4. Baked DT chemical markers

Baked profile (390s DT) was associated with:
- **Pyridine** (2011 → 2689 area; p < 0.001): fishy/coffee aroma; monotonically increasing with DT; proposed as a **volatile marker compound for the baked roasting defect** (Yang et al. 2016, cited in paper)
- Higher pyrazines (methyl-, dimethyl-, ethyl-): roasty, nutty, hazelnut character
- Methylpyridinium: correlated with Nutty+Chocolate descriptor in NMR

The "Baked" profile (extended DT with minimal temperature rise) aligns with Rao's mechanistic description from [[sources/coffee-roasting-fundamentals-rao-2020]] of baked = insufficient heat progression causing stalling. Pyridine as a chemical marker is actionable: if measurable in roast QC, pyridine elevation indicates over-development even at same color.

### 5. Body finding — CONTROVERSIAL — flagged

**Finding**: Development time had NO statistically significant effect on body perception (p = 0.37). Body was the only descriptor without a DT effect across a 4.3× range of development times (90s to 390s).

**The paper's own explanations**: "The elusiveness of the descriptor is highly likely to contribute to the difficulty of finding a significant difference despite the efforts made towards vocabulary development." "Individual understandings of Body are prevalent in the industry."

**Wiki assessment**: Likely real within the specific study conditions but may not generalize:

1. **French Press brewing confound**: French Press maximizes body by design (no filtration). All four profiles may have hit a "body ceiling" that masked DT effects. Pour-over or espresso might reveal DT-dependent body differences that French Press suppresses.
2. **Calibration insufficiency**: "Body" was calibrated with xanthan gum at two concentrations — a viscosity-based reference. Specialty coffee "body" includes mouthfeel, coating, weight, and viscosity — multiple dimensions not all captured by xanthan gum alone.
3. **Panel variability**: The paper's own internal studies (CoffeeMind) found high inter-rater inconsistency on "body." The p=0.37 may reflect noise rather than absence of effect.
4. **Real and important if true**: If DT genuinely doesn't affect body, then body in pour-over is controlled by other variables (extraction degree, total dissolved solids, filtration, grind distribution), not by DT. This would simplify profile development — target DT for sweetness/acidity, ignore body implications.

**The controversial belief challenged**: "A longer development time builds more body." This study provides NO support for that belief at this roast degree and brew method.

**Priority**: Replicate with pour-over brewing and/or trained Q-graders before accepting DT-body independence as established.

### 6. Roast degree context

All findings apply specifically at Agtron 76 ± 1 on the Gourmet scale — this is at the lighter end of specialty roasting (the SCA cupping standard is Agtron 65; light commodity roast starts ~60). The paper explicitly notes: "Whether these effects persist at different roast degrees is an interesting area for further research." Do not extrapolate the specific DT sensory relationships below Agtron 65 without additional evidence.

## Contradictions / Open Questions

- **Body finding** contradicts widespread specialty coffee teaching. Unresolved — see discussion above.
- **Acid ratio**: contradicts roaster belief that DT can selectively emphasize specific acids. This is consistent with the chemistry (all acids are thermal labile to similar degrees) but challenges practical craft belief.
- **Fast roast sweetness**: the paper treats Fast as non-defect. Industry tradition often considers extremely short DT (90s, <12% of total roast) a development defect ("fast" or "underdeveloped"). At Agtron 76, however, 90s DT appears to produce the highest sweetness and cleanliness — possibly because roast degree is held constant by ending earlier (at 204°C). The chemical profile of a "fast" profile at same color differs from a "fast" profile at lower color.
- **This study vs. Münchow 2020**: the companion paper (Münchow 2020, "Roasting Conditions and Coffee Flavor: A Multi-Study Empirical Investigation") includes a discrimination test where panelists could not reliably detect the baked defect. In *this* paper, sensory differences between Fast and Baked are highly significant (p < 0.001). The discrepancy may be methodological: this paper uses descriptive analysis (trained calibration + rating intensity), while Münchow 2020 used triangular discrimination (detect if different). Discrimination is harder than rating — even when differences exist, they may be below the "is it the same?" threshold while still being quantifiable on a rating scale.

## Key Entities Mentioned

- [[entities/scott-rao]] — indirectly referenced; DTR concept originated from Rao; companion paper addresses the RoR smooth ≠ baked defect question he raised
- Morten Münchow / CoffeeMind — corresponding author; same group as Münchow 2020

## Wiki Pages Updated

- `wiki/roasting/concepts/roasting-parameters.md` — DT section: sourced effects table; acid ratio finding; body no-effect finding (flagged); diacetyl/sweetness link; pyridine as baked marker; source_count 2→3
- `wiki/shared/sweetness-perception.md` — diacetyl and 2,3-pentanedione as specific roasting-derived sweetness compounds; fast DT preserves them; actionable roasting implication
- `wiki/shared/fermentation-flavor-compounds.md` — diacetyl cross-domain note: both fermentation and fast DT roasting produce it
- `wiki/index.md` — source indexed; roasting-parameters description updated
- `wiki/log.md` — ingest entry appended

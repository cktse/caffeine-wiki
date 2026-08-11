---
title: "Key Roasting Parameters"
domain: roasting
tags: [parameters, ror, dtr, development-time, charge-temperature, agtron, mass-loss, cga, drum-roaster, extraction-yield, smooth-ror, baked-roast, scott-rao, probe-calibration, roast-time, first-crack, second-crack, maillard, bean-density, volatiles, caffeic-acid, lactones]
source_count: 4
last_updated: 2026-06-26
---

# Key Roasting Parameters

*Status: Partially sourced. Mass loss thresholds, CGA behavior, EY relationship, and Aillio Bullet CT values are sourced (Lindsey 2024). DTR framework, smooth RoR priority, and baked roast mechanism are sourced from Rao 2020 (DTR inventor; 600+ roasting consultations). Roast time principle sourced from Rao 2020. DT guidance remains from established specialty coffee convention.*

Roasting transforms green coffee into roasted coffee through heat-driven chemical reactions (Maillard, caramelization, Strecker degradation, pyrolysis). The key parameters below control the rate, depth, and character of those reactions and, through them, the final cup.

---

## The Five Core Parameters

### Charge Temperature (CT)

The drum temperature at which green beans are loaded. Sets the initial heat transfer rate to the beans.

- Higher CT → more aggressive initial conductive heat → faster early temperature rise → darker early development (can produce tipping/scorching on surface if too high)
- Lower CT → gentler start → allows moisture to escape more gradually → cleaner cup; preferred for lighter roasts and dense high-altitude beans
- Aillio Bullet R2 Pro typical CT range: ~175–200°C depending on batch size and coffee density

**Cup quality impact**: CT affects the early Maillard phase; too high → early over-development of outside while inside is underdeveloped ("baked" profile)

---

### Rate of Rise (RoR)

The rate at which bean temperature increases, measured in °C/min. Typically read from the bean temperature probe (BT) rather than the environmental temperature (ET).

**RoR curve shape**: Modern specialty roasting practice favors a **monotonically declining RoR curve**:
- Starts fast (e.g., 15–20°C/min at the beginning)
- Gradually decelerates through the roast
- Reaches ~2–5°C/min at development phase
- Never stalls (stalling RoR → "baked" or "flat" cup)
- Never crashes (sudden sharp drop → underdeveloped interior)

**Why declining RoR**: A smooth declining RoR ensures even heat distribution and prevents the "baked" profile (flat, papery, lacking brightness) caused by extending time in the mid-development zone without productive chemical reactions occurring.

**Cup quality impact**: RoR shape is the primary tool for controlling acidity vs. body trade-off. A faster overall RoR generally preserves acidity and brightness; a slower, longer roast builds body and sweetness at the cost of origin acidity.

**Smooth RoR as the primary discipline (sourced: Rao 2020)**

Scott Rao (inventor of DTR) identifies smooth, monotonically declining RoR as the single most important roasting discipline — more foundational than targeting any specific DTR range:

- "99% of roasters' RoRs are not smooth enough to eliminate all roast defects"
- Of ~600 roasting clients consulted, 99% reported better results once RoR became smooth
- Fewer than 10% achieved mastery of smooth RoR
- **Priority order**: **Step 1** — smooth RoR. **Step 2** — DTR and everything else.

**Caveat**: One peer-reviewed study (Münchow et al. 2020, *Beverages*) found professional tasters could not detect the baking defect above chance in blind triangular discrimination testing. Rao disputes the methodology without providing counter-data. This tension is unresolved — Rao's claim may be systemic (smooth RoR is interrelated with all other parameters) while the Münchow study isolated it as a single variable. See [[roasting/sources/coffee-roasting-fundamentals-rao-2020]] for full discussion.

---

### Development Time (DT)

Time elapsed from first crack to the end of the roast (discharge). This is the most active period for Maillard reaction browning, caramelization of sucrose, and formation of flavor/color compounds.

**Why first crack is the reference**: First crack marks a phase transition (steam pressure inside the bean exceeds the bean's structural strength), typically occurring at **175–185°C bean temperature** (sourced: Campos & Silva 2025). The chemical reactions that create roast character accelerate dramatically after first crack. DT is therefore a measure of how much post-crack development was applied.

**Sourced DT effects at constant roast color (Alstrup et al. 2020 — Agtron 76, Colombian washed, Probat, French Press, 46 tasters)**

Four DT profiles at identical Agtron 76: Fast (90s), Medium (143s), Slow (266s), Baked (390s).

| DT direction | Sensory character | Primary chemical markers |
|---|---|---|
| Short DT (Fast) | **Sweetness ↑, Acidity ↑, Fruit+Berry ↑, Clean Cup ↑** | High diacetyl (2,3-butanedione), 2,3-pentanedione; high furfural, hexanal, benzeneacetaldehyde; high CGA (5-CQA, 3-CQA), malic/citric/formic acids |
| Long DT (Baked) | **Roasted ↑, Nutty+Chocolate ↑, Bitter ↑, Astringency ↑** | High pyridine (baked defect marker), pyrazines (methyl-, dimethyl-); low CGA; low diacetyl/acids |

Effect size is large despite subtle visual differences — roast color alone is insufficient as a quality metric. DT must be tracked alongside Agtron.

**DT-sweetness mechanism (sourced)**: No sugars were detectable above taste threshold in any sample (NMR). Sweetness correlates with diacetyl (2,3-butanedione) and 2,3-pentanedione — Maillard-derived ketones that peak in fast DT and degrade with extended development time. See [[shared/sweetness-perception]] for the broader aromatic modulation mechanism.

**Actionable for sweetness target**: within a given DTR window, a shorter total roast time (arriving at 1C faster, then a proportionally shorter DT) will preserve more diacetyl and sweetness-associated compounds than a longer total roast at the same DTR percentage.

**Acid ratio — DT cannot selectively favor specific acids (sourced)**: All acids (malic, citric, formic, acetic) decline proportionally with DT — the ratio between them does not change. "Development time does not allow for such alterations." This contradicts the roaster belief that a short DT emphasizes malic character or a longer DT shifts toward citric. DT reduces total acid concentration without altering which acid dominates.

**Body — DT had NO measurable effect (flagged — controversial)**:
p = 0.37 — the only non-significant result. DT ranged 90s to 390s (4.3×) with zero effect on body perception. This contradicts the common teaching that "longer DT builds more body." 

Caveats: (1) French Press brewing maximizes body independently, potentially masking DT effects — pour-over results may differ; (2) "body" descriptor calibration was done with xanthan gum, which is viscosity-based but may miss other mouthfeel dimensions; (3) 46-person professional panel without Q-grader calibration. The finding may be real, or it may be a methodological artifact. Do not assume DT-body independence across brew methods until confirmed with pour-over/espresso.

**Pyridine as baked roast chemical marker**: Pyridine increases monotonically with DT (p < 0.001) and has been proposed as a volatile chemical marker for the baked roast defect (Yang et al. 2016). Consistent with Rao's practitioner definition of "baked" as the result of extended development with insufficient heat progression.

**Important context**: This study was conducted at Agtron 76 ± 1 only. Whether these effects persist at darker roast degrees (Agtron 55–65) is not established.

---

### Development Time Ratio (DTR)

**DTR = Development Time / Total Roast Time × 100%**

Normalizes development across different batch sizes, roasters, and roast profiles. Makes cross-batch comparisons meaningful.

**Origin**: DTR was invented by [[entities/scott-rao]] and introduced in "The Coffee Roaster's Companion" (2014). The 20–25% figure is a **general guideline**, not a universal prescription — Rao's own clarification from [[sources/coffee-roasting-fundamentals-rao-2020]].

| DTR range | Application and sourcing |
|---|---|
| ~15% | Appropriate for the ~1% of "very light roasters" (drops mid-first-crack); not a general recommendation (sourced: Rao 2020) |
| 15–20% | Light roasts targeting maximum origin character; common for Ethiopian washed |
| **20–25%** | **General guideline for most specialty pour-over targets** (sourced: Rao 2020); medium-light to medium |
| 25–30% | More developed; espresso-oriented; "perfectly OK for dark roasts" (sourced: Rao 2020); more body and sweetness |
| >30% | Heavy development; dark roast territory; bittersweet character |

**Critical limitations (sourced: Rao 2020)**:
- DTR is a useful QC tool and target — but do **not** drop a roast based on DTR alone. Drop based on color or bean temperature.
- If RoR is unstable (crashing, spiking), DTR is meaningless as a quality indicator — get smooth RoR first.
- DTR is step two. Smooth RoR is step one.

**Note**: DTR percentages depend heavily on total roast time — a 20% DTR on a 7-minute roast (84 seconds development) is very different from 20% DTR on a 12-minute roast (144 seconds). DTR is a ratio, not a substitute for tracking absolute DT.

**Personal preference note**: For the target of amplifying sweetness while avoiding winey/fermentation artifacts, the 20–25% DTR range with a smooth declining RoR is the most consistent approach. Naturals and extended-fermentation coffees with heavy fermentation character may benefit from a slightly faster RoR through first crack to convert rather than extend the fermented volatile residence time.

---

### Discharge Temperature (DCT)

The bean temperature at the point the roast is ended (beans ejected into the cooling tray). The primary determinant of roast level as measured by Agtron or other colorimetric tools.

**Aillio Bullet R2 Pro approximate DCT ranges** (these vary by batch size and profile — use as starting points, verify with Agtron):

| Roast level | Agtron (gourmet) | DCT (Bullet, 250g batch, approx.) |
|---|---|---|
| Light | 75–80 | ~198–203°C |
| Medium-light | 65–74 | ~203–210°C |
| Medium | 55–64 | ~210–218°C |
| Medium-dark | 45–54 | ~218–224°C |

*These are approximate starting points. Agtron reading after resting (24–48h degassing) is the definitive roast level measurement. DCT alone is not sufficient for inter-batch comparison without also tracking RoR profile.*

**Sourced threshold — caffeine sublimation (Lindsey 2024)**: Caffeine sublimation becomes significant at drop temperatures exceeding **~400–420°F (205–215°C)** on a BT probe for the Aillio Bullet v2 at 500g batch. Below this threshold, caffeine loss during roasting is minimal. This places significant sublimation in the medium-dark to dark roast zone for Bullet-based roasting. (Note: BT probe temperatures lag actual bean surface temperature; IBTS readings on the R2 Pro will read somewhat higher for the same effective roast state.)

---

## Bean Density and Roasting (sourced: Campos & Silva 2025)

Denser beans require longer heat exposure to achieve the same roast degree as less dense beans. Bean density varies by species, variety, and **growing conditions** — altitude is the primary driver (higher altitude → slower cherry maturation → denser, harder bean). This has direct implications for charge temperature and profile duration:

- High-altitude specialty coffees (Chiroso at 1,950–2,100m; Geisha at 1,400–2,000m Panama) will behave differently under the same CT/profile as a lower-altitude variety
- If treating a dense bean with the same CT as a lower-density bean, the interior may be underdeveloped when the surface reads the target roast color
- Lower CT or longer total roast time is often needed for dense beans — verify with Agtron + cup result

See [[roasting/overview]] decision table for density-adjusted roast notes by origin.

---

## Baked Roast Defect (sourced: Rao 2020)

A baked profile is one of the most common roast defects in specialty coffee.

**Cause**: Hard RoR crashes (sudden, steep drops in the rate of rise) — **NOT** slow roasting. Slow roasting does not inherently cause baked coffee.

**Sensory character**: less sweet, hollow body, straw-like or papery notes, flatter acidity that lacks brightness.

Some roasters intentionally "bake" to reduce acidity in espresso blends (they treat it as a controlled technique). For specialty pour-over targeting sweetness and origin character, baking is a defect to avoid.

**Complementary sourced claim** (Lee et al. 2024, via Campos & Silva 2025): "Excessively slow roasting can degrade volatile compounds and result in flat-tasting beverages." This is distinct from the RoR crash mechanism above — it describes a regime where total roast duration is too long relative to heat input, degrading volatiles even without a hard RoR crash. Both extremes are problematic: too fast = surface scorching + underdeveloped interior; too slow = volatile compound degradation + flat cup.

**Prevention**: smooth, monotonically declining RoR with no crashes. This is why smooth RoR is Rao's Step 1.

---

## Roast Time Principle (sourced: Rao 2020)

No single correct roast duration exists. Optimal roast time depends on the **ratio of batch size to burner output**. An 8-minute roast may be appropriate at 3kg on a Probat P12 but dangerously fast at 12kg on the same machine.

**For Aillio Bullet R2 Pro**: batch size must always be specified when describing a roast time. A 9-minute profile at 500g does not directly translate to a 9-minute profile at 250g — the batch-size/burner-output ratio changes. The practical range for the Bullet at typical specialty batch sizes (250–500g) is roughly 8–12 minutes, but this should be derived from RoR curve shape and cup result, not targeted as a number.

---

## Probe Calibration — Do Not Copy Temperature Numbers (sourced: Rao 2020)

Temperature readings (CT, DCT, first crack temperature) are machine-specific and cannot be directly transferred between roasters or setups. Rao's self-example: his first crack at 375°F / 190°C BT and drop at 405°F / 207°C BT may correspond to your machine reading 10°F (5°C) higher — depending on probe calibration, positioning, and environmental temperature during the roast.

**Implication for this wiki**: temperature targets (CT values from Lindsey 2024 on the Aillio Bullet v2, DCT ranges above) are **starting points**, not prescriptions. Build and calibrate your own profile from Agtron color and cup results. ET readings also affect BT readings; monitor both.

**Data collection setup (Rao 2020 recommendation)**: 2.5–3mm diameter ungrounded probe, well-positioned; ET probe; Artisan or Cropster for data logging.

---

## Mass Loss as a Roast Degree Proxy

**Sourced: Lindsey 2024 (Aillio Bullet v2; Ethiopian natural + washed; 500g batch)**

Roasting drives off water and CO₂, reducing bean mass. The percentage mass lost during roasting is a practical batch-level roast degree measurement that complements Agtron color and DCT.

| Mass loss (% of green mass) | Roast category (Rao 2025) | Extraction / chemical characteristics (Lindsey 2024) | Optimal espresso brew ratio (Rao 2025) |
|---|---|---|---|
| ~11% | **Nordic** (extreme light; at edge of development) | Below EY peak; "grassy/hay" risk below this | 4:1 – 5:1 (Allongé / Filter3) |
| ~12–13% | **Light/Medium** (typical Third Wave specialty) | **EY peak range**; maximum extraction yield | 3:1 |
| ~14–15% | **Medium** (some roast character; milk blends) | **Caffeine concentration peak**; porosity high | 2:1 |
| ~16–18% | **Dark** (second crack territory) | EY declining; CGA heavily degraded | 1:1 (ristretto) |
| ~20% | **Very Dark** (Starbucks level) | Significant soluble burnoff; low EY potential | Beyond practical specialty range |

**Extraction potential and roast degree (sourced: Rao 2025; consistent with Lindsey 2024)**: Extraction potential *peaks at light/medium roast*, not at dark roast. Dark roasting burns off soluble compounds, increasing the proportion of unextractable cellulose. A very dark roast will extract lower EY than a lighter roast from the same green coffee — despite being more porous. The "dark roasts are easier to extract" belief is only true when comparing underdeveloped vs. developed roasts, not light vs. dark across the developed range.

**Natural vs. washed**: under identical Aillio Bullet v2 recipe (same CT, same RoR shape, same post-FC time designation), Ethiopian natural coffees consistently achieved ~2–3% higher mass loss than washed coffees with the same roast ID. Naturals will be darker in effective roast degree if treated with the same profile as washed coffees. Adjust CT or total roast time when switching between natural and washed on the same recipe.

## Agtron Scale

A colorimetric scale measuring surface reflectance of ground roasted coffee. Higher number = more light reflected = lighter roast.

- **Two scales in use**: Gourmet Scale (used by SCA cupping standard) and Roasting Scale (used in production). Gourmet ~= Roasting + 10–15. Always specify which scale.
- **SCA cupping standard**: Agtron 65 on the Gourmet Scale (medium-light)
- **Cold brew research** (Batali 2022 in wiki): Light roast = Agtron Gourmet 58; Medium = 48; Dark = 38

## CGA (Chlorogenic Acid) as a Roast Level Marker

**CGA decomposition products (sourced: Campos & Silva 2025)**: CGA (up to 10% of green coffee mass) decomposes during roasting into **caffeic acid and lactones** (phenolic derivatives), influencing body, astringency, and aftertaste. This is the molecular-level mechanism behind CGA's monotonic decline with roast degree.

**Sourced: Lindsey 2024 (HPLC measurement of 4-CQA and 5-CQA isomers)**

CGA concentrations in brewed coffee **dramatically and monotonically decrease** with roast degree. Degree of roast was the dominant variable — far outweighing brew time or extraction yield in determining CGA content. CGA continued to decrease even for the darkest roast batches where overall extraction yield was also declining.

**Cup quality implication**: CGA is both a flavor-active compound (contributes to cup acidity, perceived body) and a key quality marker preserved by CO₂/anaerobic fermentation (Moncayo 2025). Dark roasting effectively eliminates this advantage. Light-medium roast maximizes CGA transmission from green bean to cup.

**Cross-domain chain (processing → roasting → cup)**: CO₂ fermentation preserves CGA in the green bean ([[processing/concepts/fermentation]]) → light-medium roast allows CGA to survive into the cup → dark roast destroys CGA regardless of processing method used. See [[shared/fermentation-flavor-compounds]] for the full chain.

**CGA-underdevelopment-astringency link (sourced: Rao 2025)**: CGA is "somewhat astringent." When coffee is severely underdeveloped (dropped too early; insufficient roasting-phase CGA destruction), excess CGA survives into the cup → astringency from roasting failure, not from brewing. "If you underdevelop, you end up with too much chlorogenic acid and then you notice the astringency from it." This adds a *lower bound* to acceptable roast development: underdevelopment risk is not just flat/grassy flavor but also CGA-driven astringency. See [[brewing/concepts/espresso-fundamentals]] for the full astringency framework (channeling + quakers + underdevelopment).

---

## Maillard Reaction and Caramelization

The two dominant chemical reactions driving roast flavor development:

**Maillard reaction**: begins ~120°C and extends to ~180°C; reducing sugars + amino acids → melanoidins (brown color) + hundreds of volatile compounds: **aldehydes, ketones, pyrazines, and furans** (producing sweet, floral, nutty, or roasted notes). Accelerates dramatically after first crack. **Medium roast specifics** (sourced: Campos & Silva 2025): intensified Maillard at medium development produces **pyrazines and furans** specifically → **chocolate, caramel, nutty, and hazelnut notes**.

**Total volatile scope (sourced: Campos & Silva 2025 / Barrios-Rodríguez et al. 2021)**: lipid-nitrogen compound interactions during roasting generate aldehydes, phenols, pyrazines, and sulfur compounds — contributing to the aromatic complexity of roasted coffee with **>800 identified volatile substances** total.

**Caramelization**: sucrose degradation above 160°C → furans + dihydrofuranones. Adds sweetness and caramel character; excessive → bitterness.

**Strecker degradation**: amino acids + dicarbonyl compounds → flavor aldehydes (including furfural, acetaldehyde, diacetyl). Overlaps with Maillard. Responsible for "roasted coffee" aroma base.

**Key sweetness-associated Maillard compounds (sourced: Alstrup 2020)**:
- **Diacetyl (2,3-butanedione)**: butter, caramel, butterscotch; peaks in fast DT roasts; degrades with extended development time. Directly correlated with perceived sweetness in the cup.
- **2,3-Pentanedione**: similar butter/caramel character; also peaks in fast DT. Both diketones degrade monotonically with longer DT.
- **Furfural**: sweet/woody; highest in fast DT (2701 area vs. 2222 baked). Cross-domain: furfural is also a Maillard-derived product when roasting processes fermentation-derived glycerol (from natural coffee).

**Pyrazines (roast-forward compounds)**: methyl-, dimethyl-, and ethylmethyl-pyrazines peak in slow/baked DT profiles and are associated with nutty, hazelnut, roasted notes. These are the dominant aromatics of well-developed roasts.

**Cup quality implications**: Maillard reaction is why DTR matters — too short = insufficient flavor development (though very short DT at same color appears to maximize sweetness); too long = pyrolysis (burnt/bitter) and diacetyl degradation = less sweetness. The goal is to develop Maillard products without entering the pyrolysis zone or losing the early Maillard sweetness compounds.

Cross-reference: [[shared/fermentation-flavor-compounds]] — fermentation-derived volatiles (lactic/acetic/acetoin/furfural) interact with and are partially regenerated by Maillard during roasting.

---

## Key Sources

- [[sources/caffeine-extraction-roast-lindsey-2024]] — Lindsey et al. 2024 (PMC11586412); mass loss thresholds; caffeine and CGA behavior by roast degree; EY vs. roast degree; Aillio Bullet v2 charge temperatures; porosity data; **high credibility**
- [[sources/coffee-roasting-fundamentals-rao-2020]] — Rao 2020 (scottrao.com blog); DTR origin and clarified guidelines; smooth RoR as primary discipline; baked roast mechanism (RoR crash, not slow roasting); roast time principle; probe calibration; Aillio Bullet IBTS commentary; **high-medium (practitioner)**
- [[sources/dtr-sensory-alstrup-2020]] — Alstrup et al. 2020 (*Beverages*); DT effects at constant Agtron 76; sourced DT sensory table; diacetyl/2,3-pentanedione as sweetness compounds; acid ratio finding; body no-effect finding (flagged); pyridine as baked defect marker; **high-medium credibility**
- [[sources/roasting-fundamentals-campos-silva-2025]] — Campos & Silva 2025 (book chapter); 6-phase framework; temperature markers (first crack 175-185°C; second crack 225-235°C); Maillard range 120-180°C; medium roast → pyrazines/furans; CGA → caffeic acid + lactones; >800 volatiles; bean density principle; **medium-high (academic synthesis)**

## Related Concepts

- [[concepts/roaster-types]] — how roaster type (drum vs. air) affects parameter relationships and heat transfer
- [[roasting/overview]] — decision table for parameter targets by origin and processing method

## Related Shared Concepts

- [[shared/sweetness-perception]] — roast level and bitterness interact with sweetness aromatic pathway
- [[shared/terroir]] — medium-light (Agtron 65) is the terroir-transparent cupping standard; roasting as expression layer
- [[shared/fermentation-flavor-compounds]] — fermentation compounds and their fate during roasting; CGA chain

## Open Questions

- What is the published DTR recommendation for very high-density beans (Chiroso at 1,950–2,100m; Geisha at 1,400–2,000m Panama)? Dense beans may require longer total roast time for heat penetration — how does this shift DTR targets?
- Is there a sourced relationship between first crack temperature and roast quality for different varietals? (Denser beans = first crack at higher bean temperature?)
- How does the Bullet R2 Pro's infrared element affect heat penetration vs. a conventional drum without infrared? Does it allow shorter roast times at same development depth?
- Does RoR shape (smooth decline vs. crash) have a sourced cup quality impact beyond practitioner consensus? **Partially answered**: Rao 2020 (high-medium practitioner) claims smooth RoR is the #1 discipline based on 600+ roasting consultations; Münchow et al. 2020 (peer-reviewed) found professional tasters could not detect the baking defect above chance in blind discrimination — the two are not necessarily in direct contradiction (Rao's claim may be systemic). Münchow paper not yet ingested.
- The EY vs. roast degree relationship was measured with AeroPress (full immersion, 100°C). Does the same pattern hold for V60 pour-over? The porosity mechanism should apply, but filter flow rate and bypass effects may alter the EY relationship.
- How does mass loss interact with bean density for high-altitude dense beans? A 14-16% mass loss target may correspond to different Agtron values for Chiroso (2,100m, high density) vs. a lower-altitude Colombian Caturra.

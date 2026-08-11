---
title: "Roasting — Domain Overview"
domain: roasting
last_updated: 2026-06-26
---

# Roasting — Domain Overview

Purpose: match roasting profiles to the green coffee (origin, varietal, processing method) in order to extract the best cup quality potential from the coffee's terroir. Roasting is the first expression layer — it amplifies or suppresses terroir precursors already fixed in the green bean but does not create them.

User preferences: amplify sweetness · avoid excessive winey/fermentation artifacts · drum roaster (Aillio Bullet R2 Pro) · mostly pour-over · some espresso

For the roasting-terroir relationship, see [[shared/terroir]].

---

## Key Roasting Parameters

| Parameter | Abbrev | What it controls |
|---|---|---|
| Charge temperature | CT | Drum temp when green beans loaded; sets initial heat transfer rate |
| Rate of Rise | RoR | Bean temp increase per minute (°C/min); declining curve = best practice |
| First Crack | 1C | Physical/chemical turning point; start of development phase |
| Development Time | DT | Time from first crack to discharge; controls flavor development depth |
| Development Time Ratio | DTR | DT / total roast time (%); normalizes development across different batch sizes / roasters |
| Discharge Temperature | DCT | Bean temp at end of roast; primary roast level determinant |
| Agtron number | — | Colorimetric roast level scale; higher = lighter; SCA cupping standard = Agtron 65 (medium-light) |

See [[concepts/roasting-parameters]] for full detail on each parameter and its cup quality impact.

---

## Roaster Type

This wiki's primary roasting context: **drum roaster** (Aillio Bullet R2 Pro).

| Type | Mechanism | Heat transfer | Key characteristics |
|---|---|---|---|
| **Drum** | Rotating drum + gas burner | Conduction (drum contact) + convection (airflow) + radiation | Even development; predictable; good consistency; industry standard |
| Air / Fluid bed | Forced hot air | Convection only | Fast roasting; clean cup; less body; less common in specialty |
| Hybrid | Drum + forced air | Conduction + convection (enhanced) | Combines control of drum with speed of air |

The Bullet R2 Pro adds an infrared front element — combines drum conduction, drum-interior convection (adjustable fan speed), and infrared radiation. This three-source heat input gives greater flexibility for RoR shaping than a standard drum. See [[entities/aillio-bullet]].

---

## Roasting Phases — Temperature Framework

Six-phase model (sourced: Campos & Silva 2025). Temperatures are indicative — actual values shift with bean density, machine, and batch size.

| Phase | Temp range | Key physical events | Key chemistry |
|---|---|---|---|
| **1. Drying** | ~25→120°C | Moisture evaporates; color turns yellow; bread/cereal aroma | Endothermic; water removal; no significant flavor reactions yet |
| **2. Initial Browning** | ~120→150°C | Color deepens; roasted aroma emerges | Maillard reactions begin (sugars + amino acids); caramelization starts; hundreds of aroma intermediates form |
| **3. First Crack** | ~150→185°C; 1C at **175–185°C BT** | Audible pop; bean expands; volatile release accelerates | Endothermic → exothermic transition; CO₂/water vapor exceeds bean structural strength; full flavor and aroma development begins |
| **4. Development** | After 1C → drop | Color deepens to target; full roast character develops | Maillard + caramelization continue; DT and DTR measured here; **the most critical stage** |
| **5. Second Crack** | ~225–235°C | Second pop; cell walls rupture; surface oils visible; heavy toasted aroma | Partial carbonization; key volatiles degraded; NOT recommended for specialty quality-focused roasting |
| **6. Cooling** | Immediate post-drop | Temperature drops rapidly; reactions halt | CO₂ degassing begins; 24h+ needed before use; aromatic compounds stabilize |

The specialty quality window is entirely within Phase 4. All light/medium/dark differentiation is determined by where in Phase 4 you drop. Phase 5 (second crack) and beyond are outside specialty roasting practice.

---

## Roasting Chemistry Quick Reference

(See [[concepts/roasting-parameters]] for full detail, sourcing, and sensory implications)

| Reaction | Temp onset | Products | Sensory impact |
|---|---|---|---|
| Maillard | ~120°C → 180°C | Melanoidins (color); aldehydes, ketones, pyrazines, furans | Sweet, floral, nutty, roasted — depends on DT depth |
| Caramelization | >160°C | Furans, dihydrofuranones | Sweetness, caramel; excessive → bitterness |
| CGA decomposition | Progresses with heat | Caffeic acid, lactones | Body, astringency, aftertaste |
| Lipid × nitrogen | Throughout | Aldehydes, phenols, pyrazines, sulfur compounds | Aromatic complexity (>800 identified volatiles total) |

**Medium roast character compound**: pyrazines and furans from intensified Maillard → chocolate, caramel, nutty, hazelnut notes (Campos & Silva 2025).

---

## Roast Level Reference

| Roast level | Agtron (gourmet scale) | Typical DCT (Bullet, approx.) | Character |
|---|---|---|---|
| Very light / white | >80 | ~195°C | Grassy, undeveloped; rarely used |
| Light | 70–80 | ~200–205°C | Bright acid; origin character dominant; floral/citrus/fruity preserved |
| Medium-light | 60–70 | ~205–210°C | SCA cupping standard (Agtron 65); balanced acid + sweetness; terroir-transparent |
| Medium | 50–60 | ~210–218°C | Reduced acidity; more body; chocolate/nut notes emerge; espresso-suitable |
| Medium-dark | 40–50 | ~218–225°C | Bittersweet; oils visible on surface; roast character dominates |
| Dark | <40 | >225°C | Bitter; heavy body; origin character largely masked |

**Sweetness note** (from [[shared/sweetness-perception]]): lighter roasts are predicted to be sweeter — not because they retain more dissolved sugar (all roast levels are below the sweetness threshold), but because they preserve fruity/fermented aromatic compounds that enhance sweetness perception, while dark roasts produce bitterness that suppresses it.

---

## Roasting Decision Table

*Status: PROVISIONAL — derived from cross-domain inference (terroir + processing + sweetness research). To be validated and expanded as roasting-specific sources are ingested. Treat as a starting framework, not authoritative guidance.*

| Origin | Processing | Cup target | Recommended roast level | Agtron target | Key roasting note | Brewing target |
|---|---|---|---|---|---|---|
| Ethiopian washed (Yirgacheffe, Sidama) | Washed | Floral, tea-like, citrus | Light–Medium-light | 68–75 | Preserve volatile florals; conservative development; fast initial RoR → gentle decline; short DT | Pour-over |
| Ethiopian natural (Harrar, Jimma) | Natural | Fruity, blueberry, berry, wine-like | Medium-light | 62–68 | Natural fermentation compounds already present; avoid over-development that creates harsh/burnt fermented notes | Pour-over |
| Ethiopian natural (SIAF/extended) | Extended anaerobic | Sweet, fruity, creamy, complex | Light–Medium-light | 65–72 | Fermentation-derived compounds abundant; conservative development; high DTR risks pushing fermented → sharp/winey | Pour-over |
| Colombian washed (standard: Caturra, Castillo) | Washed | Citric, clean, balanced | Medium-light | 63–70 | Standard washed; longer DT acceptable; preserve brightness | Pour-over / Espresso |
| Colombian washed (Chiroso CCH) | Extended washed or 60h ferment | Sweet, citric, juicy, floral | Light–Medium-light | 65–72 | Treat as floral/sweet; Ethiopian-like profile; preserve aromatics | Pour-over |
| Geisha (Panama washed) | Washed | Jasmine, bergamot, citrus, tea | Very light–Light | 72–80 | Highly terroir-expressive; darkening suppresses the jasmine/bergamot fingerprint rapidly | Pour-over |
| Brazilian natural (commercial: Catiguá MG2) | Natural SIAF | Fruity, rum/wine at high ferment | Medium-light | 62–68 | Fruit profile set by processing; medium development for body | Pour-over |
| Brazilian washed/pulped natural | Washed or pulped natural | Chocolate, nut, low acid | Medium | 55–62 | Clean, lower acid; espresso-suitable with more development | Espresso |
| Central American washed (Guatemala SHB, Costa Rica) | Washed | Clean, chocolate, caramel, balanced | Medium-light to Medium | 58–68 | Solid washed; can push DTR for chocolate; body-forward for espresso | Pour-over / Espresso |
| Sumatran wet-hulled | Wet hulling | Earthy, smoky, heavy body | Medium–Medium-dark | 50–60 | Processing creates heavy body and earthy character; roasting should complement, not lighten | Espresso or French press |
| **For espresso (any origin)** | — | Body, low acidity, sweet/bitter balance | Medium | 55–65 | +5–10 Agtron darker than pour-over equivalent; more development time; higher DTR | Espresso |

**Personal preference overlay**: For all coffees, bias toward the lighter end of the recommended range to amplify sweetness and preserve terroir expression. For naturals and extended-fermentation coffees with noticeable winey artifacts, a slightly faster RoR through the development phase may help convert rather than amplify fermented volatiles — but this is a roasting hypothesis, not a sourced claim.

---

## Key Concepts

- [[concepts/roasting-parameters]] — charge temp, RoR, DT, DTR, DCT and their cup quality mechanisms
- [[concepts/roaster-types]] — drum vs. air vs. hybrid; heat transfer modes; Aillio Bullet context

---

## Key Entities

- [[entities/aillio-bullet]] — Aillio Bullet R2 Pro; user's primary roaster; specs and control parameters

---

## Key Sources

- [[sources/roasting-fundamentals-campos-silva-2025]] — Campos & Silva 2025 (book chapter, "Coffee Post-Harvest"); 6-phase framework; temperature markers; roast level sensory profiles; equipment type → sensory impact (drum → body/depth; fluidized bed → fruit/acidity); >800 volatiles; bean density principle; **medium-high (academic synthesis with peer-reviewed citations)**
- [[sources/caffeine-extraction-roast-lindsey-2024]] — Lindsey et al. 2024 (PMC11586412); mass loss thresholds (12–14% = EY peak; 14–16% = caffeine peak); CGA behavior vs. roast degree; Aillio Bullet v2 CT data; **high credibility**
- [[sources/coffee-roasting-fundamentals-rao-2020]] — Rao 2020 (scottrao.com); DTR origin + 20–25% guideline; smooth RoR as #1 discipline; baked roast from RoR crash; roast time principle; probe calibration; **high-medium (practitioner)**
- [[sources/dtr-sensory-alstrup-2020]] — Alstrup et al. 2020 (Beverages, NMR+GC-MS); DT at constant Agtron 76; fast DT = sweet/fruity/acidic; slow/baked DT = roasted/bitter; diacetyl as sweetness compound; **high-medium**

---

## Cross-Domain Links

- [[shared/terroir]] — roasting is an expression layer; medium-light (Agtron 65) is the terroir-transparent standard
- [[shared/sweetness-perception]] — roast level directly affects sweetness; light roast preserves aromatic sweetness enhancers; dark roast bitterness suppresses sweetness
- [[shared/fermentation-flavor-compounds]] — fermentation-derived volatiles (lactic/acetic/ethanol/acetoin) survive roasting to varying degrees; roast level interacts with processing to determine final cup
- [[processing/overview]] — processing method sets fermentation compound profile that roasting then works with
- [[brewing/overview]] — roast level is a key input to brewing recipe decisions; pour-over vs. espresso roast targets differ

---

## Open Questions

- At what DCT does jasmine/bergamot character in Geisha begin to degrade? Is there a published inflection point?
- Does a higher DTR on SIAF/extended-fermentation naturals amplify or suppress the winey/fermented notes? (Current understanding: suppress if fast, amplify if slow — hypothesis only)
- How does the Bullet R2 Pro's infrared element interact with RoR compared to a conventional drum roaster? Does it require different CT/charge protocol for the same bean temperature trajectory?
- What is the relationship between Agtron gourmet scale and Agtron roasting scale? (Gourmet scale typically +10–15 relative to roasting scale — clarify standard used)
- For Colombian Chiroso (1,950–2,100m, dense bean), does the expected high density require a modified charge temperature vs. standard Colombian at 1,500–1,800m?

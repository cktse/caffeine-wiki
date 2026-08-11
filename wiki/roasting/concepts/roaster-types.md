---
title: "Roaster Types"
domain: roasting
tags: [drum-roaster, air-roaster, fluid-bed, aillio-bullet, heat-transfer]
source_count: 1
last_updated: 2026-06-26
---

# Roaster Types

The roaster type determines how heat is transferred to the beans. This affects RoR behavior, development timing, flavor clarity, and body. Most specialty production uses drum roasters; the wiki's primary context is the **Aillio Bullet R2 Pro** drum roaster.

**Sourced sensory distinction** (Campos & Silva 2025): drum roasters produce "a slower, more controlled roast, typically resulting in coffees with **greater body and depth**"; fluidized-bed roasters "rely solely on convection, producing a faster and more uniform roast that **accentuates fruit and acidity notes**." This distinction holds across practitioner sources and is now peer-referenced.

---

## Heat Transfer Modes

| Mode | How it works | Dominant in |
|---|---|---|
| **Conduction** | Direct contact heat transfer from drum surface to bean | Drum roasters; most important at early stage |
| **Convection** | Hot air flowing around and through the beans | All roasters; primary in air/fluid-bed roasters |
| **Radiation** | Infrared heat from drum walls or external element | Drum roasters inherently; Bullet R2 Pro adds dedicated IR front element |

---

## Roaster Type Comparison

| Type | Heat modes | Typical roast time | Flavor profile tendency | Notes |
|---|---|---|---|---|
| **Drum (conventional)** | Conduction + convection | 10–15 min | Full body; complex; characteristic "roasted coffee" character | Industry standard; most detailed literature available |
| **Drum with enhanced airflow** | Conduction + convection (adjustable) | 8–12 min | Between conventional drum and air; adjustable emphasis | Bullet R2 Pro; Probat Probatone with high fan |
| **Drum with infrared** | Conduction + convection + radiation | 8–12 min | As drum but with additional RoR control via IR | Aillio Bullet R2 Pro; IR element supplements gas burner |
| **Air / Fluid bed** | Convection only | 4–8 min | Cleaner, lighter-bodied, brighter; less complexity | Sivetz, Nuova Simonelli Mythos (sample roasters); less common in specialty production |
| **Hybrid** | Drum + strong forced air | 6–10 min | Combines drum body with air clarity | Loring Smart Roast; common in larger specialty production |

---

## Aillio Bullet R2 Pro

The primary roaster in this wiki. See [[entities/aillio-bullet]] for full specifications.

**Relevant for profile design**:
- Three heat sources: gas drum burner (P1–9 power settings) + infrared front element (F1–9) + drum speed (D1–9 = convection intensity)
- The infrared element is particularly useful for shaping RoR in the development phase without changing gas power: reducing F setting can slow RoR approaching first crack without the lag of adjusting gas burner
- Fan/airflow control (A1–9) is independent — higher fan = more convective heat + faster chaff/smoke removal; can cause RoR drop if increased suddenly

**Control interaction**:

| Control | Primary effect | RoR effect |
|---|---|---|
| P (Power / gas) | Drum and air temperature | Increases RoR; 30–60s lag |
| F (Infrared) | Infrared radiation to bean surface | Faster response than gas; shape DT phase |
| D (Drum speed) | Conductive contact rate | More contact = faster conduction; slower = less |
| A (Airflow/fan) | Convective heat + chaff removal | Higher fan = lower RoR if used aggressively; increases "clarity" of roast |

---

## Roaster Type and Cup Quality

**Body and mouthfeel**: Drum roasters produce greater body and depth than air roasters (sourced: Campos & Silva 2025), attributed to the conductive heat's effect on oil development and cell wall structure. For pour-over emphasis, this is generally positive; for espresso body, drum is strongly preferred.

**Fruit and acidity**: Fluidized-bed (air) roasters accentuate fruit and acidity notes (sourced: Campos & Silva 2025) — the shorter roast time under high convection preserves more delicate volatile compounds. Some specialty shops use air roasters specifically for Ethiopian washed coffees where floral clarity is the priority.

**Airflow role** (sourced: Campos & Silva 2025): in all roasters, airflow "regulates convective heat transfer and the removal of gases and particulates, promoting uniform roasting and preventing undesirable flavors." Airflow is not just a cooling or smoke-removal tool — it shapes heat distribution and therefore flavor development.

**Consistency**: Drum roasters offer better batch-to-batch reproducibility because the drum mass buffers against temperature swings. Air roasters are more sensitive to ambient temperature.

---

## Related Concepts

- [[concepts/roasting-parameters]] — how roaster type affects parameter interpretation (e.g., DCT for drum vs. air are not comparable)
- [[roasting/overview]] — decision table uses drum roaster (Aillio Bullet) as the reference context

## Related Entities

- [[entities/aillio-bullet]] — Aillio Bullet R2 Pro specifications and control map

## Key Sources

- [[sources/roasting-fundamentals-campos-silva-2025]] — Campos & Silva 2025; drum vs. fluidized bed sensory distinction (sourced); airflow role; equipment overview; **medium-high (academic synthesis)**

## Open Questions

- The sourced drum/air sensory distinction (Campos & Silva 2025) is high-level. Is there a controlled study comparing drum vs. air at matched Agtron and DTR with sensory evaluation?
- At what batch size does Aillio Bullet R2 Pro RoR behavior change significantly (the roaster is rated to 1kg but profiles shift at different load sizes)?
- Does the infrared element in the Bullet require different CT than a conventional drum to achieve the same bean temperature trajectory?

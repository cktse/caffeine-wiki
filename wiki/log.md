# Wiki Log

Append-only chronological record of all wiki operations.
**Never edit past entries.** The history of how this knowledge base evolved is itself valuable.

Maintained by the LLM agent. Do not edit manually.

---

## Format

```
## [YYYY-MM-DD] operation | domain | description
```

Operations: `ingest` | `query` | `lint` | `digest` | `update` | `bootstrap`

Parseable with:
```bash
grep "^## \[" wiki/log.md | tail -10   # last 10 entries
grep "ingest" wiki/log.md | wc -l      # total ingests
grep "2026-04" wiki/log.md             # all entries from April 2026
```

---

## [2026-06-17] bootstrap | all | Initial wiki structure created

Wiki initialized from LLM Wiki Template.
Domains: processing, varietals, brewing
Tool: Claude Code (claude-sonnet-4-6)

Pages created:
- wiki/overview.md
- wiki/processing/overview.md (with full processing methods summary table)
- wiki/varietals/overview.md (with species tree and region list)
- wiki/brewing/overview.md (with pour-over + espresso decision tables)
- wiki/processing/concepts/: fermentation, anaerobic-fermentation, mucilage, drying
- wiki/brewing/concepts/: v60, neo-switch, origami, graycano, espresso-fundamentals, dialing-in
- wiki/varietals/concepts/: terroir
- wiki/index.md updated with all domain pages
- Raw directories created: raw/processing/, raw/varietals/, raw/brewing/, raw/assets/

---

## [2026-06-17] ingest | brewing | Hario Switch Review — Coffee Chronicler (Asser Christensen, 2023)

Source: raw/brewing/Hario Switch Review The Hybrid Brewer You Need to Try.md

Pages created:
- wiki/brewing/sources/hario-switch-review-coffee-chronicler.md
- wiki/brewing/entities/hario-switch.md
- wiki/brewing/entities/asser-christensen.md
- wiki/brewing/entities/tetsu-kasuya.md
- wiki/brewing/entities/clever-dripper.md

Pages updated:
- wiki/brewing/concepts/neo-switch.md — added Coffee Chronicler 50/50 recipe, Switch vs Neo Switch distinction, size scaling table
- wiki/index.md — added source and entities

Key additions: 50/50 open-then-closed pour-split recipe; "sweet" variation (close at 0:25 vs 0:45); size scaling (20g→45g); Clever Dripper comparison; Switch mechanism description.

Clarification added: original Switch (glass V60 cone) vs. Neo Switch (Neo cone) are distinct products sharing the same mechanism and recipes.

---

## [2026-06-17] ingest | brewing | Tetsu Kasuya "Devil" Recipe for Hario Switch (Timer.Coffee, 2024)

Source: raw/brewing/Tetsu Kasuya "Devil" recipe for Hario Switch - Hario Switch Recipe.md

Pages created:
- wiki/brewing/sources/tetsu-kasuya-devil-recipe-hario-switch.md

Pages updated:
- wiki/brewing/concepts/neo-switch.md — added full Kasuya devil recipe table, side-by-side comparison with Christensen, new open questions
- wiki/brewing/entities/tetsu-kasuya.md — added specific recipe parameters and design philosophy
- wiki/index.md — added source

Key addition: Kasuya's temperature-drop technique (90°C → 70°C mid-brew) now documented with full step timing. Comparison table makes explicit why Christensen's recipe extracts more despite a leaner ratio.

---

## [2026-06-17] ingest | brewing | Kasuya 2025 "New Hybrid" Hario Switch Recipe (Timer.Coffee, 2025)

Source: raw/brewing/2025 "New Hybrid" Hario Switch recipe by Tetsu Kasuya - Hario Switch Recipe.md

Pages created:
- wiki/brewing/sources/kasuya-2025-new-hybrid-hario-switch.md

Pages updated:
- wiki/brewing/concepts/neo-switch.md — added 2025 recipe section, expanded comparison table to three recipes (devil / Christensen / 2025)
- wiki/brewing/entities/tetsu-kasuya.md — added 2025 recipe parameters and structural evolution notes
- wiki/index.md — added source

Key addition: closed immersion bloom as structural innovation vs. devil recipe. Three-recipe comparison table now covers the full Switch recipe landscape in this wiki. Core finding: immersion bloom (closed start) is the primary driver of sweetness; temperature drop is Kasuya's consistent tool for taming bitterness in the final immersion phase.

---

## [2026-06-17] ingest | brewing | Kasuya 4:6 Method — Philocoffea (authoritative source)

Source: raw/brewing/How to Make Coffee Using the 46 Brewing Method.md

Pages created:
- wiki/brewing/sources/kasuya-46-method-philocoffea.md
- wiki/brewing/concepts/46-method.md
- wiki/brewing/entities/philocoffea.md

Pages updated:
- wiki/brewing/concepts/v60.md — added 4:6 method as primary recipe, updated temp guidance
- wiki/brewing/entities/tetsu-kasuya.md — added 4:6 facts and Philocoffea founding
- wiki/brewing/overview.md — updated pour-over decision table with Kasuya roast-temp table (93/88/83°C)
- wiki/index.md — added source, concept, entity

Key addition: two-axis control model (40% = flavor, 60% = strength) documented with full variation examples. Roast-specific temperature table (93/88/83°C) now grounding the brewing overview table. Connection to Switch recipes made explicit: all three Kasuya Switch recipes share the 1:15 ratio and the same underlying extraction arithmetic.

---

## [2026-06-17] ingest | brewing | 2 Recipes To Brew On The Graycano Dripper (The Basic Barista, 2025)

Source: raw/brewing/2 Recipes To Brew On The Graycano Dripper.md

Pages created:
- wiki/brewing/sources/graycano-two-recipes-basic-barista.md
- wiki/brewing/entities/graycano.md
- wiki/brewing/entities/liam-hatzipavlis.md

Pages updated:
- wiki/brewing/concepts/graycano.md — MAJOR CORRECTION and rewrite: Graycano is a cone dripper (not flat-bottom) with fast flow (not restricted). Flat-bottom only via Graycano Coin accessory. Temperature corrected from 88–91°C to 95°C (cone) / 98°C (wave). Added both recipes with correct pour structures.
- wiki/brewing/overview.md — updated Graycano rows in decision table; corrected temperatures
- wiki/index.md — updated source, concept description, added entities

Correction: bootstrap skeleton page incorrectly characterized the Graycano as flat-bottom with restricted outflow and semi-immersion style. Source confirms: cone dripper, large exit hole, fast flow by default.

---

## [2026-06-17] ingest | brewing | Comandante Grind Size Chart (The Basic Barista / Liam Hatzipavlis, 2024)

Source: raw/brewing/Comandante Grind Size Chart - Coffee Grind Sizes For Brew Methods.md

Pages created:
- wiki/brewing/sources/comandante-grind-size-chart.md
- wiki/brewing/concepts/comandante-grind-size.md
- wiki/brewing/entities/comandante.md

Pages updated:
- wiki/brewing/concepts/dialing-in.md — added variable priority order (Grind→Temp→Ratio→Dose→Minerals→Beans)
- wiki/index.md — added source, concept, entity

No contradictions. Graycano recipe click counts (25 and 30) validated against chart range (20–30). Key calibration: C40 ≈ 30µm/click; Red Clix 15µm/click; C60 21µm/click. All pour-over methods (V60, Graycano, Kalita, Orea) share the 20–30 click / 600–900µm range, with per-dripper nuance within that band.

---

## [2026-06-17] ingest | brewing | Basic HARIO V60 Recipe Updated for 2026 (The Basic Barista, 2025)

Source: raw/brewing/Basic HARIO V60 Recipe - Updated for 2026.md

Pages created:
- wiki/brewing/sources/basic-v60-recipe-2026.md
- wiki/brewing/concepts/fast-filters.md
- wiki/brewing/entities/hario-drip-assist.md

Pages updated:
- wiki/brewing/concepts/v60.md — added 2026 fast-filter recipe section; two-recipe comparison table (4:6 vs 2026); updated source_count to 2
- wiki/index.md — added source, concept, entity

Key tension with existing wiki: this recipe uses fine grind (~table salt) at 98°C for 2:00–2:30 total — opposite of Kasuya's 4:6 (coarse, 93°C, 3:30). Not contradictory: different equipment systems. Fast filters are the enabling variable that changes what grind and temp is appropriate for V60.

---

## [2026-06-17] ingest | varietals | History of Arabica — World Coffee Research (2023)

Source: raw/varietals/History of Arabica.md

Pages created:
- wiki/varietals/sources/history-of-arabica-wcr.md
- wiki/varietals/concepts/arabica-history.md
- wiki/varietals/concepts/typica.md
- wiki/varietals/concepts/bourbon.md
- wiki/varietals/concepts/ethiopian-landrace.md
- wiki/varietals/concepts/timor-hybrid.md
- wiki/varietals/concepts/introgressed-varieties.md
- wiki/varietals/concepts/f1-hybrids.md
- wiki/varietals/concepts/coffee-leaf-rust.md
- wiki/varietals/entities/world-coffee-research.md

Pages updated:
- wiki/varietals/overview.md — CORRECTION: Bourbon is NOT a mutation of Typica; they are parallel lineages from Yemen stock. Updated varietal tree with WCR four-category framework. Added dispersal context.
- wiki/index.md — added all new varietals pages

Key correction: Bourbon/Typica parallel lineage relationship (previously incorrect). Key additions: full dispersal timeline, Timor Hybrid role in CLR resistance breeding, CLR resistance breakdown risk (near-to-medium term expected), F1 hybrid propagation constraint, Ethiopian landrace as genetic origin.

---

## [2026-06-18] ingest | varietals | WCR Arabica Varieties Catalog (2025)

Source: raw/varietals/World Coffee Research Arabica Varieties Catalog (2025).md
Source credibility: Highest available. WCR DNA fingerprinting + 23-site global trials.

Pages created:
- wiki/varietals/sources/wcr-arabica-varieties-catalog-2025.md
- wiki/varietals/concepts/wcr-variety-catalog.md (reference concept; variable schema + key variety lookup table)

Pages updated:
- wiki/varietals/concepts/bourbon.md — CORRECTION: SL34 is Typica-related (not Bourbon); updated Key Descendants, Kenya Connection, Open Questions, sources
- wiki/varietals/entities/guatemala.md — Pache confirmed as Typica natural mutation (compact, large bean, high altitude, CLR susceptible)
- wiki/varietals/concepts/coffee-leaf-rust.md — added IHCAFE 90 as third confirmed CLR-susceptible Catimor
- wiki/index.md — added source + concept

Key findings:
- SL34 = Typica related (WCR DNA): the wiki previously grouped SL28+SL34 as both Bourbon; corrected
- Pache = natural mutation of Typica; compact stature; good quality at high altitude; best >1,200m
- Three CLR-confirmed varieties all share same lineage: Timor Hybrid 832/1 × Caturra (Lempira, Costa Rica 95, IHCAFE 90)
- Pink Bourbon absent from 2025 catalog — WCR criteria require distinct/uniform/stable; Pink Bourbon fails
- Typica aliases documented: Criollo, Arábigo, Blue Mountain, Sumatra, Indio, Plume Hidalgo
- F1 hybrid clonal propagation requirement explicit in catalog for all 10 F1 entries

---

## [2026-06-18] ingest | varietals | World Atlas of Coffee — Guatemala (James Hoffmann, 2018)

Source: raw/varietals/World Atlas of Coffee - Guatemala Excerpt.md
Source credibility: Very high — Hoffmann's World Atlas is a primary specialty coffee reference.

Pages created:
- wiki/varietals/sources/world-atlas-guatemala-hoffmann.md
- wiki/varietals/entities/guatemala.md

Pages updated:
- wiki/varietals/overview.md — added Guatemala to growing regions
- wiki/brewing/overview.md — split "Central America" row into Guatemala (washed, SHB) + Central America non-Guatemala (honey/natural)
- wiki/index.md — added source + entity

Key additions:
- 8 Guatemalan growing regions with altitude, harvest window, and variety data — all SHB (>1,300m)
- Altitude grading system: Prime (750m) → SHB (>1,300m); all specialty Guatemalan is SHB by default
- Bourbon + Caturra present in 7/8 regions — the backbone of Guatemalan coffee
- Huehuetenango: highest non-volcanic mountains in Central America; most coffee-dependent; outstanding quality
- Antigua: Denomination of Origin 2000 ("Genuine Antigua Coffee"); fraud ongoing (cherries imported from other regions for processing)
- Pache: new variety not previously in wiki — appears in Cobán, Nuevo Oriente, Fraijanes; insufficient source detail for standalone concept page
- Guatemala is primarily WASHED — corrects the brewing overview which lumped all Central America under honey/natural

Brewing table fix: Guatemala washed at SHB altitude is meaningfully different from Costa Rica honey or El Salvador natural; now has its own row.

---

## [2026-06-18] ingest | varietals | Costa Rican Coffee Guide — 1Zpresso (2026)

Source: raw/varietals/Costa Rican Coffee Guide Regions, Flavor Profiles, Processing, and Bean Grades.md
Source credibility: Low-Medium — 1Zpresso brand blog; no factual errors found.

Pages created:
- wiki/varietals/sources/costa-rica-coffee-guide-1zpresso.md
- wiki/varietals/entities/costa-rica.md — resolves dead link from varietals/overview.md
- wiki/shared/honey-processing.md — second shared cross-domain page; honey processing color label system

Pages updated:
- wiki/varietals/overview.md — Costa Rica entry updated
- wiki/index.md — source, entity, shared/honey-processing added

Key additions:
- Costa Rica entity: 8 regions table (Tarrazú flagship; Tres Rios "Bordeaux of CR"; Guanacaste shade-grown); ~30-year Robusta ban (lifted 2018; still pre-commercial); ICAFE founded 1933
- Honey processing shared page: Black/Red/Yellow/White color labels with mucilage percentages; Raisin Honey and Extended Fermentation Honey non-standard variants; comparison table vs. washed/natural; brewing implications
- SHB/GHB/MHB grading (altitude-based; same SHB threshold as Guatemala)
- ICAFE-recognized variety list: 12 varieties incl. Obatá, Venecia, Villalobos (not previously in wiki); Villa Sarchi native to Costa Rica
- Costa Rica 95 flagged: still ICAFE-recognized despite confirmed CLR resistance failure (WCR 2025)
- Honey origin claim: documented as "strongly associated with Costa Rica" per this source; formal attribution needs more authoritative source

Cross-domain flags:
- Processing: honey processing color labels are a core processing concept; shared/ page now covers Black/Red/Yellow/White + non-standard variants
- Brewing: honey processing affects sweetness/acidity balance; 4:6 method first-pour ratio is the relevant dial

---

## [2026-06-18] ingest | varietals | Sumatra Coffee — 1Zpresso (2026)

Source: raw/varietals/Sumatra Coffee Flavor Profile, Regions, and Wet Hulling Explained.md
Source credibility: Low-Medium — 1Zpresso brand blog; no factual errors found.

Pages created:
- wiki/varietals/sources/sumatra-coffee-1zpresso.md
- wiki/varietals/entities/indonesia.md — resolves dead link from varietals/overview.md
- wiki/shared/wet-hulling.md — FIRST shared cross-domain page; bridges processing + varietals + brewing

Pages updated:
- wiki/varietals/concepts/timor-hybrid.md — Aceh 1979 introduction added; local names HDT / Tim Tim
- wiki/varietals/concepts/introgressed-varieties.md — Catimor local name "Ateng" (Sumatra) added; S795 added with WCR-unverified note
- wiki/varietals/overview.md — Indonesia entry updated
- wiki/index.md — source, entity, and first shared/ page added

Key additions:
- Wet Hulling (Giling Basah): 4-step process (pulp → partial dry to 20-40% → hull wet → final dry); explains all key Sumatran flavor characteristics; medium-dark roast recommended
- S795 (Line S): Indian-origin variety, disease resistant, refined sweetness + spice + full body; widely grown in Sumatra; WCR genetic classification unverified
- Catimor local name "Ateng" in Sumatra/Indonesia
- Timor Hybrid introduced to Aceh 1979 — specific date not previously in wiki
- Mandheling = historical trade name (not variety, not GI); WWII naming origin story
- Aceh/Gayo: EU PGI "Kopi Arabika Gayo" (2017)
- Indonesian grading G1–G6 (vs. Ethiopia's G1–G5); DP/TP commercial sorting terms
- Processing cross-domain: first wet-hulling concept in wiki; flagged for processing domain when sources develop

Cross-domain flags:
- Processing: Giling Basah is a distinct method from washed/natural/honey; deserves a processing/concepts/ page when processing sources are ingested
- Brewing: medium-dark roast for wet-hulled coffees; heavy body affects extraction approach

---

## [2026-06-18] ingest | varietals | Ethiopia Sidama Coffee — 1Zpresso (2026)

Source: raw/varietals/Ethiopia Sidama Coffee Regions, Varieties, Processing & Flavor Profile.md
Source credibility: Low-Medium — 1Zpresso brand blog; no factual errors found.

Pages created:
- wiki/varietals/sources/ethiopia-sidama-1zpresso.md

Pages updated:
- wiki/varietals/entities/jarc.md — 74 Series CBD origin story (1971 crisis → 13 selections → released 1974; year IS the name); 74112 added as third notable variety
- wiki/varietals/entities/ethiopia.md — Sidama row updated (altitude 1,550m, cup notes, 13% stat, CoE 2024); GI protection note (Sidama/Yirgacheffe/Harrar only); Sidama vs. Yirgacheffe comparison section added
- wiki/index.md — source added

Key additions:
- 74 Series naming origin: released 1974 in response to 1971 CBD crisis; 13 selections; 74112 is a third named variety (previously only had 74110, 74158)
- Sidama: 13% of Ethiopia's output; GI protected; 9/10 top CoE 2024 finishers
- Only 3 Ethiopian regions hold GI: Sidama, Yirgacheffe, Harrar — notable for origin sourcing decisions
- Sidama vs. Yirgacheffe: Sidama (1,550m floor, fuller body, fruit-forward complexity); Yirgacheffe (1,900m floor, tea-like, intense florals)
- Sidama processing: ~60% washed; honey and anaerobic exist but rare
- Brewing flag: light roast recommended for Sidama to preserve brightness and florals

---

## [2026-06-18] ingest | varietals | Ethiopian Coffee Guide — 1Zpresso (2025)

Source: raw/varietals/Ethiopian Coffee Guide Flavor Profiles, Varieties, Growing Regions & Grading.md
Source credibility: Low-Medium — 1Zpresso brand blog; same publisher as Colombian guide.

Pages created:
- wiki/varietals/sources/ethiopian-coffee-guide-1zpresso.md
- wiki/varietals/entities/ethiopia.md — resolves dead link from varietals/overview.md
- wiki/varietals/entities/jarc.md — Jimma Agricultural Research Center; 74 Series

Pages updated:
- wiki/varietals/concepts/ethiopian-landrace.md — JARC 74 Series section added (74110, 74158); four cultivation systems table; Geisha open question updated; source_count 1→2
- wiki/varietals/overview.md — Ethiopia entry updated with regional detail
- wiki/index.md — source + 2 entities added

Key additions:
- JARC 74 Series: formal improved varieties (not landrace); 74110 and 74158 specialty-grade; bred from Ethiopian genetic stock; distinct from unselected heirloom
- Six growing regions with altitude, processing, cup profile: Yirgacheffe (washed, floral, tea-like), Sidama (washed, citrus, balanced), Guji (volcanic, citrus+berry), Harrar (natural, blueberry, espresso), Jimma (natural, tropical fruit, wine-like), Limu (washed, smooth, spice)
- G1–G5 grading (defect count); CLU specialty system; Q1/Q2 certification overlay
- ECX (2008): centralized pooling destroyed traceability; 2017 reform restored direct farm purchase
- Four cultivation systems: Forest 10%, Semi-forest 35%, Garden 50%, Plantation 5%
- Climate change: arabica zones shifting higher; wild arabica projected to decline ~50% by 2088

Error flagged: "Bourbon is historically a natural mutation of Typica" — same 1Zpresso error as Colombian guide; not propagated.
Cross-domain: Ethiopian naturals → processing domain flag; Yirgacheffe washed → pour-over brewing recommendation.

---

## [2026-06-18] ingest | varietals | Coffee Varieties Produced and Marketed in Kenya — KCTA (2016)

Source: raw/varietals/Kenya Coffee Varieties.md
Source credibility: Low-Medium — Kenya Coffee Traders Association trade document; predates WCR 2025 DNA fingerprinting.

Pages created:
- wiki/varietals/sources/kenya-coffee-varieties-kcta.md
- wiki/varietals/entities/kenya.md — resolves dead link from varietals/overview.md

Pages updated:
- wiki/varietals/concepts/arabica-variety-taxonomy.md — K7 added to quick-reference table (Bourbon related; Good quality; partial CLR resistance)
- wiki/varietals/overview.md — varietal tree corrected: SL28/K7 under Bourbon, SL34 moved to Typica lineage; Pache added to Typica lineage
- wiki/varietals/concepts/coffee-leaf-rust.md — K7 natural partial CLR resistance section added (non-introgressed mechanism)
- wiki/index.md — source and entity added

Key additions:
- K7 (new to wiki): Bourbon-related Kenyan variety with natural partial CLR resistance — no Timor Hybrid introgression; selected from French Mission at Lengetet Estate, Muhoroni; suited for low altitude CLR-prevalent zones
- Kenya entity: SL28/SL34/K7/Ruiru 11/Batian variety table; French Mission background; WCR DNA corrections noted
- Batian clarification: "true breeding arabica" via backcrossing — consistent with WCR's "Introgressed (Other)" classification (not F1 hybrid)

Error flagged in source: "French Mission is a bourbon derivative" — blanket claim superseded by WCR 2025; SL34 is Typica-related. Wiki follows WCR.

Varietal tree correction: overview.md previously listed SL28 and SL34 together under Bourbon lineage. Now separated correctly per WCR 2025 DNA.

---

## [2026-06-18] lint | all | Post-WCR-catalog: cross-reference audit, SL34 corrections, classification review

Fixed:
- typica.md: SL34 and Pache added to Key Descendants; wcr-arabica-varieties-catalog-2025 added to Key Sources; source_count 1→2; last_updated updated; colombia + guatemala links added to Related Concepts
- bourbon.md: colombia + guatemala links added to Related Concepts
- world-coffee-research.md: variety catalog source + concept page linked
- coffee-leaf-rust.md: wcr-arabica-varieties-catalog-2025 added to Key Sources; source_count 1→3; last_updated updated
- introgressed-varieties.md: wcr-variety-catalog concept link added to Related Concepts; wcr catalog source added to Key Sources

Classification finding:
- wcr-variety-catalog.md correctly filed under concepts/ — content is the 13-variable evaluation schema and 9-category genetic taxonomy (frameworks), not a catalog entry. Name is borderline; rename to arabica-variety-taxonomy.md is optional cosmetic improvement.

Flagged (still unresolved — require new sources or decisions):
- 6 dead entity links in varietals/overview.md: ethiopia, kenya, panama, costa-rica, yemen, indonesia
- Kenya entity is now highest priority: SL28/SL34 documented in 3 pages without a Kenya anchor
- Processing domain entirely unsourced: 4 bootstrap stubs (fermentation, anaerobic-fermentation, mucilage, drying)
- origami.md and espresso-fundamentals.md are unsourced bootstrap skeletons
- Unfiled query: Colombia washed cinnamon roast recipe (V60 4:6 at 95°C, ~22 clicks, 50+70 first-pour split)
- SessionStart hook reported 5 indexing errors — sessions.db may be incomplete

---

## [2026-06-18] lint | all | Orphan check, dead links, contradiction scan, stub audit

Fixed:
- wiki/varietals/overview.md: `[[concepts/disease-resistance]]` → `[[concepts/coffee-leaf-rust]]` (dead link; page was named correctly, link was not)
- wiki/varietals/overview.md: last updated date corrected to 2026-06-18

Flagged (not fixed — require new sources):
- 6 dead entity links in varietals/overview.md growing regions: ethiopia, kenya, panama, costa-rica, yemen, indonesia
- Processing domain entirely unsourced: 4 bootstrap stubs (fermentation, anaerobic-fermentation, mucilage, drying)
- origami.md and espresso-fundamentals.md are unsourced bootstrap skeletons
- Missing cross-refs: bourbon.md and typica.md do not link to entities/colombia.md
- Unfiled query: Colombia washed cinnamon roast recipe (V60 4:6 at 95°C, ~22 clicks, 50+70 split)
- SessionStart hook reported 4 indexing errors — sessions.db may be incomplete

Priority gaps: processing domain (zero ingests), Gesha/Geisha (no coverage), Kenya entities (SL28/SL34 undocumented)

---

## [2026-06-18] ingest | varietals | The Ultimate Guide to Colombian Coffee — 1Zpresso (2025)

Source: raw/varietals/The Ultimate Guide to Colombian Coffee Origin, Grading, Processing & More.md
Source credibility: Medium — brand marketing blog (1Zpresso); statistics sourced from USDA/FNC; one factual error flagged.

Pages created:
- wiki/varietals/sources/colombian-coffee-guide-1zpresso.md
- wiki/varietals/entities/colombia.md
- wiki/varietals/entities/fnc.md

Pages updated:
- wiki/varietals/concepts/introgressed-varieties.md — added Colombian section: Variedad Colombia (Caturra × Timor Hybrid), Castillo, Tabi (tri-hybrid); 87% adoption stat; Castillo 2.0 note
- wiki/varietals/concepts/coffee-leaf-rust.md — added Colombia case study (35% → 87% rust-resistant adoption 2010–2025)
- wiki/varietals/overview.md — updated Colombia growing regions entry with variety list and 87% stat
- wiki/index.md — added source, 2 entities; fixed concept/entity section structure

Error flagged: Source incorrectly describes Bourbon as "a natural mutation of Typica." Corrected in source page — Bourbon and Typica are parallel Yemen lineages (WCR DNA fingerprinting). Do not propagate this claim.

Key additions:
- Colombia entity: 22 regions, 1,200–2,300m, dual harvest, 100% Arabica, Excelso grading standard, PDO/PGI certifications, Coffee Triangle (UNESCO 2011)
- FNC entity: Founded 1927; Cenicafé (research arm) developed Castillo; manages Café de Colombia mark
- Pink Bourbon: uncertain genetic origin, prominent in Colombia specialty scene; documented in Colombia entity (not yet a standalone concept page — one source insufficient)
- Castillo 2.0: released late 2024; large-scale adoption not yet begun

---

## [2026-06-17] ingest | varietals | History of Robusta — World Coffee Research (2023)

Source: raw/varietals/History of Robusta.md

Pages created:
- wiki/varietals/sources/history-of-robusta-wcr.md
- wiki/varietals/concepts/robusta.md

Pages updated:
- wiki/varietals/overview.md — updated robusta production share (~40%, up from ~30–40%); added Robusta Genetic Groups section (Guinean vs. Congolese); allogamy note
- wiki/varietals/concepts/coffee-leaf-rust.md — added section on why robusta has natural CLR resistance and how that drove its global spread
- wiki/varietals/entities/world-coffee-research.md — added second source reference, robusta concept link
- wiki/index.md — added source and concept entries

Key additions:
- Allogamy: robusta cannot self-pollinate (unlike arabica) — requires mixed-clone farming; this is a fundamental agronomic constraint not mentioned in any previous source
- Two genetic groups (Guinean: drought-tolerant, early harvest; Congolese: more widespread, higher bean weight, rust resistant)
- Dispersal timeline: Congo ~1870 → Brussels/Java ~1900 → Brazil 1912 → Central America 1930–35
- CLR resistance historical narrative: robusta's resistance drove adoption when arabica collapsed; that resistance eventually entered arabica via the Timor Hybrid
- Climate resilience caveat: temperatures >20.5°C significantly reduce yields — widely overstated in popular media

Cross-domain flag: fermentation quality control can make "an immediate and crucial difference" in robusta cup quality — bridges to processing domain when processing sources develop.

---

## [2026-06-19] ingest | processing | Impact of Coffee Cherry Fermentation Methods on the Quality Attributes of Dry‐Processed Coffee — Moncayo-Palacios et al. (2025)

Source: raw/processing/Impact of Coffee Cherry Fermentation Methods on the Quality Attributes of Dry‐Processed Coffee.md
Source credibility: **Highest tier** — peer-reviewed, PubMed-indexed (PMCID: PMC12767571); UHPLC + GC + HPLC chemical analysis; SCA sensory protocol with 3 certified Q-graders; controlled experimental design on-farm.

First ingest into the processing domain. All four processing concept stubs (fermentation, anaerobic-fermentation, mucilage, drying) were unsourced before this entry. This paper directly addresses fermentation and anaerobic-fermentation.

Pages created:
- wiki/processing/sources/fermentation-natural-coffee-moncayo-2025.md

Pages updated:
- wiki/processing/concepts/fermentation.md — MAJOR UPDATE from stub: sourced biochemical mechanism (sucrose, CGA, elaidic acid, linoleic acid); aerobic vs. CO₂ modified atmosphere comparison table; sensory descriptor table; roasting implication; scope note; source_count 0→1
- wiki/processing/concepts/anaerobic-fermentation.md — MAJOR UPDATE from stub: CO₂ modified atmosphere as first sourced evidence; variant table with mechanism + CO₂ source columns; carbonic maceration relationship clarified; source_count 0→1
- wiki/varietals/entities/colombia.md — cv. 'Colombia' natural processing research noted in Processing section; source linked in Connections
- wiki/processing/overview.md — Key Sources section added; CO₂ fermentation open question added
- wiki/index.md — source page indexed under Processing Sources
- wiki/log.md — this entry

Key findings:
- CO₂ modified atmosphere (24h) achieved 86.90 SCA on natural cv. 'Colombia' at 1,740m — statistically significantly better than aerobic (84.70/85.10) and unfermented control (82.15)
- No defects in any treatment (uniformity, clean cup, sweetness all 10/10 across all five)
- CO₂ mechanism: inhibits sucrose consumption, preserves chlorogenic acid, suppresses elaidic acid (<10%), promotes linoleic acid
- Sensory progression: P3 (CO₂ 24h) = aromatic/liquor-like/silky; P4 (CO₂ 60h) = whisky/silky; P2 (aerobic 48h) = blueberry/spicy; P0 (no fermentation) = tea leaves/raw cane sugar
- Diminishing returns after 24h CO₂ — P3 and P4 not statistically different from each other on most attributes
- First academic basis for elaidic acid as a negative quality marker in green coffee

Cross-domain flags:
- Roasting: chlorogenic acid preserved by CO₂ fermentation degrades further during roasting; lighter roasts retain more CGA from CO₂-fermented naturals
- Varietals: cv. 'Colombia' (Castillo group, introgressed) produced 86.90 SCA natural coffee — demonstrates specialty-grade naturals are viable with Colombian varieties
- Study limitation: single variety (introgressed Catimor-adjacent), single farm, single growing season — generalizability to Ethiopian landraces, Typica, Bourbon not confirmed

---

## [2026-06-20] ingest | shared | How Sweet Coffee Tastes! Towards an Understanding of Coffee Sweetness — SCA / OSU (2024)

Source: raw/brewing/How Sweet Coffee Tastes! Towards an Understanding of Coffee Sweetness  25, Issue 22.md
Source credibility: High — SCA authoritative publication; Flavor Research and Education Center, Ohio State University; 125 professional coffee tasters; LC-MS sugar analysis; proper statistical methods. Caveat: magazine article reporting intermediate results of an ongoing 2-year project (not a final peer-reviewed paper). Flavoromics work (Hypothesis 5) pending as of publication.

Domain decision: filed in `shared/` (not `brewing/`). Sweetness perception is driven by fermentation aromatics, varietal character, and roasting interactions — not by brewing technique. Filing in `brewing/` would misplace the insight's primary utility. Source page resides in `wiki/brewing/sources/` (raw file was in `raw/brewing/`); concept page in `wiki/shared/`.

Pages created:
- wiki/brewing/sources/sweetness-perception-sca-2024.md
- wiki/shared/sweetness-perception.md
- wiki/brewing/entities/sca.md

Pages updated:
- wiki/processing/concepts/fermentation.md — cross-reference to sweetness-perception added to Related Concepts
- wiki/index.md — source, entity, shared/ concept indexed
- wiki/log.md — this entry

Key findings:
- Coffee sweetness is NOT caused by sugar — all sugars in brewed coffee are below the human sensory threshold (~2,000 mg/L vs. 100 mg/L max in tested coffees). This was known since 1985 but the industry built cupping systems on the wrong assumption for 40 years.
- Two simultaneous sweetness mechanisms: (1) volatile aromatic compounds (ortho/retronasal); (2) unknown nonvolatile non-sugar compounds tasted on the tongue
- Sweetness modulation: fruity/fermented aromas → enhance sweetness; bitter/roasted/papery → suppress sweetness
- Paradox: coffees with the highest measured sugar content were the LEAST sweet — likely because sugar retention correlates with roast conditions that also produce bitterness
- Medium roast retains 0.9% of green sucrose; light roast retains 2.9% — but both are below threshold regardless
- Flavoromics work (identifying specific nonvolatile sweet-tasting compounds) is pending as of Oct 2024

Cross-domain flags:
- Processing: strongest cross-domain connection in wiki so far — CO₂ fermentation (Moncayo 2025) produces "aromatic, liquor-like" descriptors = exactly the fruity/fermented aromatic category that OSU identifies as sweetness-enhancing. Two independent research teams converge on the same relationship.
- Roasting: dark roast bitterness actively suppresses sweetness perception, not just reduces it — this has recipe implications (lighter roasts are not just "brighter" but are chemically predicted to be perceived as sweeter)
- Varietals: fruity/floral varietal character (Ethiopian landrace, SL28 blackcurrant) supports sweetness perception; earthy/woody profiles are neutral or suppressive
- Brewing: over-extraction → bitterness → suppressed sweetness; the 4:6 first-pour ratio's sweetness axis is mechanistically about aromatic compound extraction, not sugar

SCA entity created — appears in both fermentation paper (SCA cupping protocol) and this source; warranted as a brewing-domain entity.

---

## [2026-06-20] ingest | brewing | Cold vs. Iced: Sensory Analysis of Full Immersion Coffee — Batali et al. 2022 / SCA 2023

Source: raw/brewing/Cold vs. Iced Using Sensory Analysis to Test the Claim that Cold Brew is Sweeter and Less Acidic  25, Issue 19.md
Underlying paper: *Foods* 2022 (doi: 10.3390/foods11162440) — peer-reviewed, open access
Source credibility: High — peer-reviewed paper summarized in SCA magazine; UC Davis Coffee Center; 14 trained panelists × 27 samples × 3 evaluations = 1,134 evaluations; full factorial design; Coffee Science Foundation + Toddy LLC funded.

Pages created:
- wiki/brewing/sources/cold-brew-vs-iced-batali-2022.md
- wiki/brewing/concepts/cold-brew.md

Pages updated:
- wiki/brewing/overview.md — cold brew section added; scope description updated to include cold brew as third method
- wiki/shared/sweetness-perception.md — cold brew NOT sweeter finding added to Connection to Brewing; connection to cold-brew fruity-origin mechanism documented
- wiki/shared/wet-hulling.md — hot brew preserves Sumatran smoky/earthy profile; cold brew suppresses it
- wiki/index.md — source and concept indexed under Brewing
- wiki/log.md — this entry

Key findings:
- Cold brew confirmed: more floral, less bitter, less sour, less rubbery, higher pH (less acidic) — vs. hot brew at same TDS
- Sweetness: absent from the four reported differences, but this does NOT mean "cold brew is not sweeter" — the full 27-attribute ballot is undisclosed; the SCA sweetness intensity scale did not exist until September 2023 (study ran January–December 2021); and reduced bitterness (confirmed) can produce perceived sweetness increase via sensory modulation. Claim corrected in all wiki pages via lint pass.
- Ambient (22°C) ≡ refrigerated (4°C): same sensory profile, 24 hours faster. No reason to refrigerate during brewing.
- Light roast (Agtron 58) best for cold brew: no negative roast interactions; cleanest result
- Dark roast cold brew adds "woody" character — not recommended
- Ethiopian washed cold brew → more fruity: combined with sweetness research, explains the "sweet and smooth" cold brew perception via the aromatic pathway (not actual sweetness increase)
- Sumatra wet-hulled: hot brew preserves the smoky/earthy Sumatran profile; cold brew suppresses it
- Effect hierarchy: origin > roast level > brew temperature. Coffee quality matters more than brew method.
- First Agtron roast scores in wiki: Light = Agtron Gourmet 58; Medium = 48; Dark = 38

Cross-domain connections:
- Sweetness: cross-referenced with [[shared/sweetness-perception]]; bitterness reduction confirmed by study may itself increase perceived sweetness via modulation; Ethiopian washed cold brew emphasizes fruity aromatics (aromatic sweetness pathway)
- Wet Hulling: hot brew better represents the processing method's characteristic cup profile
- Green bean selection: origin effect > brew method effect is a direct green bean purchase insight

---

## [2026-06-20] lint | shared | Factual error — roast level and residual sugar claim, sweetness-perception.md

Error: "Connection to Roasting" section stated "dark roast actually has a slightly higher fraction of residual sugars at the lower absolute level." This is inaccurate. Clarke & Macrae (1985), cited in the SCA source, shows light roast retains 2.9% of green sucrose and medium retains 0.9%. Dark roast retains even less — the sugar degradation curve is monotonically downward with roast degree. Dark roast does not have more residual sugar at any level, fractional or absolute.

Additional problem: the phrasing "higher fraction... at the lower absolute level" was internally contradictory and unreadable.

Fixed in `wiki/shared/sweetness-perception.md`: last bullet of "Connection to Roasting" rewritten to state the accurate direction (dark roast has less residual sugar than light/medium, not more) and to correctly identify aromatics and bitterness suppression as the sweetness mechanism, not sugar quantity.

---

## [2026-06-22] ingest | processing | Green Coffee: A Guide for Roasters and Buyers — Kornman (Roast Magazine, 2022)

Source: raw/processing/Green Coffee - A Guide for Roasters and Buyers by Chris Kornman [Excerpt on Processing].md
Source credibility: **High-Medium** — Roast Magazine practitioner handbook; specialty green coffee specialist; field experience at origin. Not peer-reviewed; authority is practitioner expertise, not experimental data.

Pages created:
- wiki/processing/sources/kornman-green-coffee-2022.md
- wiki/processing/concepts/processing-terminology.md — new concept page; terminology disambiguation; Kornman's Processing Flowchart reference; sourcing implications

Pages updated:
- wiki/varietals/entities/colombia.md — FNC 2016 natural export resolution added (explains why Colombian naturals are a recent phenomenon)
- wiki/processing/overview.md — terminology concept page added to Key Concepts; Kornman source added to Key Sources
- wiki/index.md — source and terminology concept indexed
- wiki/log.md — this entry

Key findings:
- Processing terminology is not standardized — "anaerobic," "natural," "carbonic maceration," and "honey" all mean different things to different producers. Kornman recommends "dried in the cherry" and "sealed-tank" as more precise alternatives.
- Kornman's Processing Flowchart (Kornman + Evan Gilman): color-coded diagram showing which steps are "almost always" (green), "almost never" (brown), or ambiguous (tan) for each method. Image file at raw/assets/Fig 1 Coffee Processing Types.jpeg.
- ALL fermentation is technically anaerobic — "anaerobic" as a marketing category is linguistically imprecise; what differentiates modern sealed-tank methods is the duration, CO₂ source, and coffee state (whole cherry vs. depulped).
- Colombian naturals effectively banned from export until FNC 2016 resolution — explains recent availability in specialty market.
- Ethiopian naturals have achieved Grade 1 status (formerly washed-only) when properly sorted.
- "Process flavor" claim (naturals homogenize terroir) largely debunked — consistent with sourced evidence in wiki.
- Honey/pulped natural/semi-washed = same process; Brazilian origin 1991; color labels not standardized across origins.

Cross-domain flags:
- Sourcing: "ask what equipment and what state of coffee" rather than relying on labels
- Varietals: Colombia entity updated with FNC 2016 history; Ethiopia Grade 1 naturals noted

---

## [2026-06-22] ingest | processing | Study on Coffee Quality Improvement by Self-Induced Anaerobic Fermentation — Braga et al. (2023)

Source: raw/processing/Study on coffee quality improvement by self-induced anaerobic fermentation Microbial diversity and enzymatic activity.md
Source credibility: **High** — peer-reviewed in Food Research International (Elsevier); 3 certified Q-graders; high-throughput genomic sequencing (16S rRNA + ITS); FAPESP-funded; real on-farm conditions.

Pages created:
- wiki/processing/sources/siaf-braga-2023.md

Pages updated:
- wiki/processing/concepts/anaerobic-fermentation.md — MAJOR UPDATE: SIAF evidence section added; variants table updated with sensory data; SIAF vs. CO₂ injection comparison table; mycotoxin risk documented; open question partially answered; source_count 1→2
- wiki/processing/concepts/fermentation.md — Key Variables: cherry washing and altitude effects on fermentation timing added; Key Sources updated; source_count 1→2
- wiki/processing/overview.md — Braga 2023 added to Key Sources
- wiki/index.md — source indexed; concept descriptions updated
- wiki/log.md — this entry

Key findings:
- SIAF (self-induced anaerobic fermentation — CO₂ generated by microorganisms, not injected): +2.5 to +3.83 SCA points across three lots
- Sensory profile at peak: fruity, sweet, creamy, clean — caramel/peach/tangerine/honey character; distinct from CO₂ injection's liquor-like/silky profile
- Pre-washing cherries before SIAF accelerates fermentation significantly (peak at day 3 vs. day 7 for unwashed) but narrows the over-fermentation window
- Altitude matters: 1,150m farm (slower, more tolerant, higher ceiling) vs. 625m farm (faster, earlier peak, lower ceiling)
- **Mycotoxin risk**: *Fusarium* sp. present in significant amounts (up to 32.6% of fungal sequences); produces trichothecenes and fumonisins that survive roasting; a genuine safety concern for spontaneous SIAF
- SIAF is more forgiving than wet fermentation — extended time past peak degrades quality but doesn't ruin the lot
- CO₂ injection achieves immediate anaerobiosis, eliminating the Fusarium transition window — a safety advantage over spontaneous SIAF
- Terroir (farm location) influenced fungal diversity more than washing method — supports varietal/origin selection primacy

Cross-domain flags:
- Sourcing: buyers of SIAF lots should ask about cherry prep (washed/unwashed), altitude, starter culture use, and mycotoxin testing
- Sweetness: SIAF fruity/sweet/creamy profile aligns with aromatic sweetness pathway documented in [[shared/sweetness-perception]]
- Varietals: study uses Brazilian commercial varieties (Red Icatú, Red Catuaí); generalizability to Ethiopian landraces or Bourbon not confirmed

---

## [2026-06-20] lint | brewing | Overclaim correction — cold brew sweetness, Batali 2022

Error found: `cold-brew.md`, `cold-brew-vs-iced-batali-2022.md`, `sweetness-perception.md`, and `log.md` all stated or implied "cold brew is not sweeter" as a confirmed finding from the Batali 2022 study.

This claim was too strong. Three problems:

1. **Not explicitly stated in source**: the article reports four key temperature-driven differences (more floral; less bitter/sour/rubbery). Sweetness does not appear in this list — but the source never says "sweetness was measured and found non-different." The full 27-attribute sensory ballot is not disclosed.

2. **Cupping form timing**: the study was conducted January–December 2021. The SCA sweetness intensity scale was added in September 2023. Whether sweetness was on the ballot, and at what granularity (presence/absence vs. intensity), is unknown.

3. **Sensory modulation ignored**: the confirmed reduction in bitterness (a sweetness suppressor, per [[shared/sweetness-perception]]) would itself increase perceived sweetness via modulation — even without any direct change in sweet-tasting compounds. So cold brew could reasonably be perceived as sweeter for indirect reasons the study confirms.

Fixed in:
- `wiki/brewing/sources/cold-brew-vs-iced-batali-2022.md` — sweetness bullet rewritten as "not directly addressed" with ballot/timing caveat
- `wiki/brewing/concepts/cold-brew.md` — table row changed from "✗ Not confirmed" to "⚠️ Ambiguous"; myth section rewritten
- `wiki/shared/sweetness-perception.md` — "NOT measurably sweeter" claim removed; nuanced explanation added
- `wiki/log.md` — overclaim corrected in ingest entry and cross-domain section

---

## [2026-06-23] ingest | varietals | Ethiopian coffee Production systems, geographical origin traceability, and EU deforestation regulation compliance — Urugo et al. (2025)

**Source**: Markos Makiso Urugo et al., *Journal of Agriculture and Food Research* (Elsevier), Vol. 19, 2025. DOI: 10.1016/j.jafr.2025.101695
**Credibility**: High — peer-reviewed Elsevier; lead author has published original empirical metabolomics research on Ethiopian coffee; review article synthesizing published literature

**Pages created**:
- `wiki/varietals/sources/ethiopia-production-systems-urugo-2025.md` — source page

**Pages updated**:
- `wiki/varietals/entities/ethiopia.md` — significant expansion: What/Who updated with smallholder scale stats (4M+ farmers, 95% on <0.5 ha, $1.43B revenue, 30% EU export share); Six Major Growing Regions expanded to full 12-region terroir map (added Amaro/Bale Mountain, Kaffa, Bench Maji, Wollega/Lekempti, Wenbera/Zegie); Four Cultivation Systems table updated with geographic distribution by region; new Agroforestry Ecology section (shade quantification, biodiversity refugia stats, UNESCO reserves, carbon stocks); new EUDR and Supply Chain Risk section (market risk, smallholder compliance burden, traceability tools)
- `wiki/index.md` — source indexed; Ethiopia entity description updated
- `wiki/log.md` — this entry

**Key findings**:
- Ethiopia's 95% smallholder structure (<0.5 ha plots) is structural — explains why cooperative-level traceability is the norm and why EUDR compliance is disproportionately costly for Ethiopian producers
- Full regional terroir map extends well beyond the standard 6 specialty regions; SW regions (Kaffa, Bench Maji) and Western (Wollega) have distinct profiles largely absent from buyer-facing guides
- Ethiopian agroforestry is ecologically anti-deforestation (increases/preserves canopy, 60%+ forest species in semi-forest stands, massive carbon stocks in Gedeo) — but may not meet EUDR's rigid definitional criteria
- EUDR implementation delayed to December 2025; 30% of Ethiopian exports at risk if compliance documentation is not in place
- UNESCO Biosphere Reserve zones (Kafa, Yayu, Sheka, Majang, Gedeo) are the highest-diversity coffee areas — forest/semi-forest lots from these zones carry the most unselected genetic complexity

**Cross-domain flag**: EUDR traceability tools (metabolomics, stable isotope) have direct relevance to green bean authentication as a sourcing tool — not just a regulatory compliance mechanism.

---

## [2026-06-24] ingest | processing | Enhancing Sensory Quality of Coffee: The Impact of Fermentation Techniques on *Coffea arabica* cv. Catiguá MG2 — Silva et al. (2024)

**Source**: Aline Cristina de Oliveira Silva et al., *Foods* (MDPI), 2024. PMC10931400. DOI: 10.3390/foods13050653
**Credibility**: High — peer-reviewed, PMC-indexed; 5 certified Q-graders; HPLC 12-compound chemical analysis; multi-funder (FAPESP + FAPEMIG + CNPq + CAPES); medium Agtron roast standardized across all treatments.

**Pages created**:
- `wiki/processing/sources/siaf-catigua-mg2-silva-2024.md` — source page with full 17-row SCA score table, HPLC compound data, ML decision rules
- `wiki/shared/fermentation-flavor-compounds.md` — NEW cross-domain page: fermentation compound → flavor mapping; lactic/acetic/ethanol/glycerol/malic/citric → cup contributions; roasting behavior; natural vs. pulped comparison; sourcing decision rules. Fills the aroma gap identified in the lint report.

**Pages updated**:
- `wiki/processing/concepts/fermentation.md` — Key Variables: cherry integrity (2× sugar substrate in natural) and solid-state vs. submerged mechanisms added; Silva 2024 added to Key Sources; source_count 2→3
- `wiki/processing/concepts/anaerobic-fermentation.md` — "Natural vs. Pulped in SIAF" block inserted with full comparison table; ML duration decision rules added; Silva 2024 added to Key Sources; source_count 2→3
- `wiki/processing/overview.md` — fermentation-flavor-compounds shared page linked in Key Concepts; Silva 2024 added to Key Sources
- `wiki/index.md` — source indexed in Processing; fermentation-flavor-compounds indexed in Shared

**Key findings**:
- Natural solid-state SIAF ≥48h → 85.75–87.50 SCA (Red/yellow fruits → rum/wine/grape at 96h)
- Pulped solid-state 24h → 78.95 SCA — below specialty grade; the only treatment scoring below the unfermented control (83.30–83.60)
- Chemical explanation: natural cherry has ~2× fermentable sugars vs. pulped (fructose: 82.3 vs. 37.0 mg/g; sucrose: 59.75 vs. 29.40 mg/g) → 2× lactic acid and 6× ethanol in final green bean
- Solid-state vs. submerged: water addition dilutes ethanol exactly 2× (natural SS 96h: 62 mg/g → natural submerged: 31 mg/g)
- ML-derived decision rules: natural SIAF duration >36h solid-state → 93% probability ≥84.75 SCA; pulped requires ≥60h submerged to reach specialty grade
- Propionic and butyric acids absent from all controlled SIAF — quality signals; absence confirms no spoilage

**Cross-domain connection**: `fermentation-flavor-compounds.md` is shared (processing → cup quality / brewing). Connects Silva 2024 HPLC data with sweetness aromatic modulation pathway in [[shared/sweetness-perception]]. Also flags that all SIAF research is from Brazil at 625–1,150m — quality implications for high-altitude Ethiopian/Colombian naturals remain untested.

---

## [2026-06-24] ingest | varietals | Sensory Perception and Physicochemical Characteristics of Geisha Coffee From Different Production Zones in Panama — Ledezma et al. (2025)

**Source**: Diana Batista Ledezma, Camilla Sartori, Elizabeth Tomasino. *Food Science & Nutrition* 13, no. 12: e71278. 2025. PMC12645158. DOI: 10.1002/fsn3.71278
**Credibility**: **High-Medium** — peer-reviewed (Wiley), PMC-indexed; rigorous statistics (CA, MFA, AHC, discriminant analysis); same OSU Tomasino lab as Batali 2022 (cold brew). Limitations: consumer panel RATA (n=24), not Q-graders; macro physicochemical analysis only (no HPLC/GC-MS); single 2023-2024 harvest year.

**Pages created**:
- `wiki/varietals/sources/panama-geisha-terroir-ledezma-2025.md` — source page
- `wiki/varietals/entities/panama.md` — resolves dead link from varietals/overview.md; four production zones, SCAP, Volcán Barú terroir context
- `wiki/varietals/concepts/geisha.md` — fills Geisha coverage gap flagged in lint; Ethiopian landrace origin; diaspora path; bergamot fingerprint; Panama regional terroir profiles; commercial context

**Pages updated**:
- `wiki/varietals/concepts/terroir.md` — major update from bootstrap stub to sourced page: empirical evidence section (Panama Geisha discriminant analysis); terroir vs. processing vs. roasting framing; key factors expanded; source_count 0→1
- `wiki/varietals/overview.md` — Geisha entry in varietal tree updated with concept page link, bergamot fingerprint note, and diaspora path
- `wiki/index.md` — source, entity, concept, and terroir description all added/updated

**Key findings**:
- Panama Geisha terroir is real: Boquete, Tierras Altas, and Renacimiento produce statistically distinct sensory profiles (discriminant analysis, 95% CI)
- Boquete (1,450–2,000m): fruity aroma + floral → dried fruit/cocoa/fermented flavor → bitter taste; highest °Brix (1.45) and titratable acidity
- Tierras Altas/Volcán (1,300–1,850m): floral/fruity/citrus/herbal → citrus/herbal flavor → sour/tart/sweet taste
- Renacimiento (1,400–1,900m): citrus/cocoa/herbal/nutty across both aroma and flavor
- Bergamot is a **variety fingerprint** (present in all zones, all samples) — not a regional differentiator
- Physicochemical parameters (roast degree, density, pH, bean color) converge across zones — terroir is encoded in volatile compounds not captured by macro measurements
- Key terroir framing: "Roasting amplifies or suppresses terroir precursors already present in the green bean; it does not create them"

**Lint gaps resolved**:
- `wiki/varietals/entities/panama.md` — dead link from varietals/overview.md now resolved
- `wiki/varietals/concepts/geisha.md` — "Gesha/Geisha (no coverage)" gap from lint now resolved

**Cross-domain flags**:
- Terroir → roasting: roasting profile selection should be terroir-aware; light-medium preferred for Geisha/floral/citrus origins
- Brewing method affects terroir expression — different brewing methods extract different volatile compounds; study used French press 1:16 immersion; V60 would be expected to express Geisha terroir differently
- Ethiopia connection: Geisha origin is the Gesha forest in Kaffa/Bench Maji area — documented in [[entities/ethiopia]] as a UNESCO Biosphere Reserve zone

---

## [2026-06-24] ingest | varietals | Unveiling a unique genetic diversity of cultivated Coffea arabica L. in its main domestication center: Yemen — Montagnon et al. (2021)

**Source**: Montagnon, C., Mahyoub, A., Solano, W., Sheibani, F. 2021. *Genetic Resources and Crop Evolution* 68: 2411-2422. DOI: 10.1007/s10722-021-01139-y. Springer.
**Credibility**: **High** — peer-reviewed Springer genetics journal; validated 8-SSR marker set (7.4 alleles/marker; validated by Pruvot-Woehl et al. 2020 across 2,533 samples); discriminant analysis confirms cluster robustness (91% overall, 100% for New-Yemen); established lead author Montagnon; CATIE germplasm expertise from Solano. **Commercial conflict of interest flag**: entirely funded by Qima Coffee. New-Yemen cluster is both the most commercially interesting finding and the one most exposed to sampling bias (45 Qima breeding population trees). Core findings consistent with prior independent research.

**Pages created**:
- `wiki/varietals/sources/yemen-genetic-diversity-montagnon-2021.md` — source page
- `wiki/varietals/entities/yemen.md` — resolves dead link from varietals/overview.md; Yemen as domestication center; three genetic clusters; New-Yemen; Mocha heritage; extreme growing conditions

**Pages updated**:
- `wiki/varietals/concepts/arabica-history.md` — major update: 4-route dispersal framework (added direct Yemen-East Africa route); 10 numbered genetic insights; Yemen genetic cluster summary table; open question answered ("Yemen still holds its diversity"); source_count 1→2
- `wiki/varietals/concepts/geisha.md` — Montagnon 2021 added to Key Sources; Ethiopian Only cluster confirmation noted
- `wiki/varietals/concepts/arabica-variety-taxonomy.md` — Montagnon 2021 five-cluster nuances section added: K-7/SL-34/SL-28 cluster placements; Chiroso as Ethiopian Only escapee; source_count 1→2
- `wiki/index.md` — source, entity, arabica-history description updated

**Key findings**:
- Five genetic clusters: Ethiopian Only (68 EA + Geisha/Java/Chiroso/SL-06), SL-17 (K-7/SL-14/SL-17/K-758), Yemen Typica-Bourbon (Bourbon/Typica/SL-28/Kent/Moka), Yemen SL-34 (SL-34/SL-09), New-Yemen (24 unique samples)
- Four dispersal routes confirmed; new Route 4 = direct Yemen to East Africa (late 19th/early 20th C) producing SL-34 via French Mission from Aden
- Geisha confirmed Ethiopian Only cluster — bypassed Yemen; direct Ethiopia to Kenya
- New-Yemen cluster: 24 accessions; unique globally; 100% correct DA classification; potential climate-resilience breeding reservoir; unknown Ethiopian ancestors
- Yemen retains the same genetic diversity it gave to the world 300 years ago (Yemen Typica-Bourbon cluster intact) — answers prior open question
- Ethiopia genetic diversity 2.7x greater than all non-Ethiopian clusters (7.0 vs. 2.63 alleles/marker)
- Chiroso (exceptional-cup Colombian variety): Ethiopian Only cluster = new "Ethiopian escapee" of interest
- K-7 in SL-17 cluster (not Yemen Typica-Bourbon); SL-34 in Yemen SL-34 cluster (distinct from Yemen Typica-Bourbon)

**Lint gaps resolved**:
- `wiki/varietals/entities/yemen.md` — dead link from varietals/overview.md now resolved

---

## [2026-06-25] ingest | varietals | Chloroplast Genome Assembly of Caturra Chiroso, Bourbon Chiroso, and Chiroso — Chica-Acosta et al. (2024)

**Source**: Chica-Acosta, M., Ibarra-Arcila, H.E., Martínez, J.G. 2024. *Journal of Plant Biochemistry and Biotechnology* 33: 710–715. Springer. DOI: 10.1007/s13562-024-00934-9. *(Metadata note: raw file frontmatter shows an incorrect DOI — 10.38141/10779/0337 belongs to reference [^1] Castillo 2005, not this paper)*
**Credibility**: **Medium-High** — peer-reviewed Springer journal; sound cpDNA methodology; no conflict of interest; independently corroborates Montagnon 2021 with a different marker type (cpDNA vs. nuclear SSR). Limitations: 6 plants, 1 farm; no cup quality data; not PMC-indexed.

**Context**: Fills the "Chiroso — watch item" gap flagged in the arabica-variety-taxonomy page. This is the first peer-reviewed genomic characterization of all three Chiroso varieties and the first published description of their Eastern Ethiopian regional origin.

**Pages created**:
- `wiki/varietals/sources/chiroso-chloroplast-chica-acosta-2024.md` — source page; DOI correction noted
- `wiki/varietals/concepts/chiroso.md` — NEW concept page; full overview: three-variety structure; name confusion explained; Eastern Ethiopian (Berbere) origin; comparison to Geisha; cpDNA haplotype data; SNP authentication markers; cup quality gap identified

**Pages updated**:
- `wiki/varietals/concepts/arabica-variety-taxonomy.md` — Chiroso promoted from "watch item" to full entry with SNP marker, Eastern Ethiopian specificity, corroboration note; Chica-Acosta 2024 added to Key Sources; source_count 1→3; last_updated updated
- `wiki/varietals/concepts/arabica-history.md` — Chiroso entry updated with Eastern Ethiopian (Berbere) specificity and corroboration note; Chica-Acosta 2024 added to Key Sources; source_count 2→3
- `wiki/varietals/concepts/geisha.md` — "Closest Analog: Chiroso" comparison section added; Eastern vs. SW Ethiopian origin distinction; comparison table
- `wiki/varietals/entities/colombia.md` — Chiroso group added to varietals table
- `wiki/varietals/overview.md` — Chiroso added to Ethiopian Landrace varietal tree; Colombia region entry updated
- `wiki/index.md` — source and concept indexed

**Key findings**:
- Three Colombian endemic varieties in the Chiroso group: Caturra Chiroso (CCH, small), Bourbon Chiroso (BCH, tall), Chiroso (CHCH); all Ethiopian Only — none genetically related to Caturra or Bourbon
- Names are farmer vernacular based on fruit shape ("chiroso" = elongated oval) and plant size — NOT genetic lineage. This is a sourcing risk: any retailer describing Caturra Chiroso as a Caturra derivative is wrong.
- Origin: Eastern Ethiopia (Berbere/Bale Mountains region) — distinct from Geisha's SW Ethiopian (Kaffa/Bench Maji) origin. Both are Ethiopian Only Route 3 escapees from different source populations within Ethiopia.
- Independent corroboration: Montagnon 2021 (nuclear SSR) + Chica-Acosta 2024 (cpDNA) converge on Ethiopian Only classification using entirely different marker systems — methodologically strong
- CCH + BCH unique cpDNA haplotype + exclusive SNP (C/A at position 47,413 bp, trnT(UGU)-trnL(UAA) spacer) — potential authentication marker
- CHCH anomaly: plain Chiroso shares a cpDNA haplotype with traditional Bourbon and Caturra despite Ethiopian Only nuclear SSR classification — unresolved tension
- Cultivation: 1,950–2,100m ASL, ~16°C, ~1 kg/tree/year, up to $45/pound; Urrao, Antioquia, Colombia; competitions since 2014
- No cup quality data in this paper. Key gap: Pazmiño-Arteaga & Ruíz-Márquez 2022 sensory + volatile compounds study for Caturra Chiroso (three Antioquia origins) is the priority next ingest for cup profile data

---

## [2026-06-26] ingest | roasting + shared | Caffeine Content in Filter Coffee Brews as a Function of Degree of Roast and Extraction Yield — Lindsey et al. (2024)

**Source**: Lindsey, Z.R. et al. *Scientific Reports* 14 (2024). PMC11586412. DOI: 10.1038/s41598-024-80385-3. Berry College.
**Credibility**: **High** — PMC-indexed (Scientific Reports / Nature); HPLC caffeine + CGA; refractometry (EY); SEM (porosity); water chemistry and grind distribution controlled; no COI; undergraduate research funding. Limitation: 2 Ethiopian coffees only; AeroPress brew only; no sensory panel.

**Primary research question**: caffeine content vs. roast degree. Most important contributions to this wiki are the secondary findings: mass loss thresholds, CGA destruction curve, EY vs. roast degree, and first sourced Aillio Bullet charge temperatures.

**Pages created**:
- `wiki/roasting/sources/caffeine-extraction-roast-lindsey-2024.md` — full source page with experimental setup, CT data, mass loss table, natural vs. washed behavior, CGA findings

**Pages updated**:
- `wiki/roasting/concepts/roasting-parameters.md` — status changed from "UNSOURCED STUB" to "Partially sourced"; mass loss thresholds table added (12–14% EY peak, 14–16% caffeine peak); DCT threshold for caffeine sublimation added (400–420°F / 205–215°C on Aillio Bullet v2 BT probe); new "CGA as a Roast Level Marker" section added; Key Sources section added; source_count 0→1; last_updated updated
- `wiki/roasting/entities/aillio-bullet.md` — "Practical Starting Points" section expanded with sourced CT data from Lindsey 2024: Ethiopian natural 330°F (~166°C) / washed 340°F (~171°C) at 500g batch; note on natural vs. washed needing different CTs
- `wiki/shared/fermentation-flavor-compounds.md` — CGA roasting behavior row updated from 1 sentence to the full cross-domain chain (fermentation preserves CGA → dark roasting destroys it → light-medium roast is required to realize the CGA benefit); open question on light vs. medium roast partially answered for CGA; Lindsey 2024 added to Key Sources; source_count 3→4; tags updated; last_updated updated
- `wiki/index.md` — source indexed; roasting-parameters description updated

**Key findings**:
- Mass loss thresholds: <12% = underdeveloped; 12–14% = peak EY zone; 14–16% = peak caffeine zone; >16% = declining extraction
- Dark roasts under identical brew conditions → lower caffeine concentration (lower EY); at identical EY → higher caffeine concentration (caffeine more stable than other soluble compounds)
- CGA: dramatically and monotonically destroyed with increasing roast degree; dark roasting effectively eliminates CGA regardless of how much fermentation preserved it in the green bean
- Caffeine sublimation becomes significant at drop temp >400–420°F (205–215°C) on Aillio Bullet v2 BT probe → medium-dark to dark territory
- Ethiopian natural achieves 2–3% higher mass loss than washed under identical recipe; naturals need lower CT or shorter DT than washed to target same effective roast level
- Aillio Bullet v2 (same platform as user's R2 Pro) sourced CT: 330°F (~166°C) for Ethiopian natural, 340°F (~171°C) for Ethiopian washed, 500g batch, RoR declining-curve recipe

**Critical cross-domain chain (newly sourced)**:
CO₂ fermentation (Moncayo 2025) → preserves CGA in green bean → light-medium roast (Lindsey 2024) → CGA survives to cup → contributes to perceived quality and acidity. Dark roasting (>~16% mass loss) breaks this chain entirely — the processing CGA advantage is lost.

---

## [2026-06-25] bootstrap | roasting | Roasting domain initialized

Fourth domain added to the wiki. CLAUDE.md updated by user to include `roasting` domain with `wiki/roasting/` root.

**Directories created**:
- `wiki/roasting/sources/` — empty; `.gitkeep` only
- `wiki/roasting/concepts/` — seeded with two concept stubs
- `wiki/roasting/entities/` — seeded with Aillio Bullet entity
- `raw/roasting/` — empty; `.gitkeep` for source documents

**Pages created**:
- `wiki/roasting/overview.md` — decision table (origin × processing → roast level target; PROVISIONAL — no roasting sources yet; derived from cross-domain inference); parameter quick reference; roaster type comparison; open questions
- `wiki/roasting/concepts/roasting-parameters.md` — CT, RoR, DT, DTR, DCT, Agtron definitions; Maillard/caramelization context; cup quality mechanisms; UNSOURCED STUB
- `wiki/roasting/concepts/roaster-types.md` — drum vs. air vs. hybrid; heat transfer modes; Aillio Bullet control interaction; UNSOURCED STUB
- `wiki/roasting/entities/aillio-bullet.md` — Aillio Bullet R2 Pro specs; P/F/D/A control map; IBTS probe; starting point profiles (approximate, unsourced)

**Pages updated**:
- `wiki/overview.md` — roasting domain added to domains table; cross-domain chain updated
- `wiki/index.md` — Roasting section added

**User preferences captured in overview.md**:
- Target: amplify sweetness, avoid excessive winey/fermentation artifacts
- Hardware: Aillio Bullet R2 Pro (drum + infrared)
- Primary target: pour-over; secondary: espresso

**Note**: All roasting concept and entity pages are currently UNSOURCED STUBS built from established specialty coffee roasting practice. The decision table in overview.md is PROVISIONAL — derived from cross-domain inference (shared/terroir, shared/sweetness-perception, shared/fermentation-flavor-compounds). These pages need roasting-specific sources to become first-class wiki pages.

---

## [2026-06-25] ingest | varietals + shared | Sensory Evaluation and Aromatic Volatile Compounds of Caturra Chiroso — Pazmiño-Arteaga & Ruíz-Márquez (2022)

**Source**: Pazmiño-Arteaga, J.D. & Ruíz-Márquez, A.F. *Ciencia y Tecnología Agropecuaria* 24, no. 1. 2022. Agrosavia. DOI: 10.21930/rcta.vol24_num1_art:2846. Original language: Spanish (translated for ingest).
**Credibility**: **Medium** — peer-reviewed in Agrosavia's Ciencia y Tecnología Agropecuaria; no COI; 3 Q-graders; headspace GC-MS on Shimadzu GC-2010. Limitations: not PMC/Scopus indexed; 6 lots from 3 municipalities only; cupping protocol non-standard (12g/100mL at 90°C vs. SCA 8.25g/150mL at 93°C — ~3.5× more concentrated; internal comparisons valid, cross-study scores not); headspace GC-MS identified only 14 of 1000+ volatile compounds; no absolute SCA scores (radar chart only); single harvest year (2020). Pazmiño-Arteaga is cited in Chica-Acosta 2024, establishing credibility as a Chiroso researcher.

**Quality bar rationale**: Passes. Fills the most explicitly flagged gap in [[concepts/chiroso]] (cup profile not peer-reviewed). This is the first peer-reviewed sensory characterization of Caturra Chiroso. The terroir test (same genetics, same post-harvest protocol, different origins → different cups) is the cleanest terroir isolation design in the wiki — controlled for both variety AND specific post-harvest method. Credibility limitations are acknowledged and documented in the source page.

**Pages created**:
- `wiki/varietals/sources/chiroso-sensory-pazmino-2022.md` — full source page (English translation); post-harvest protocol detail; 14-compound volatile table; three-origin data; methodological caveats

**Pages updated**:
- `wiki/varietals/concepts/chiroso.md` — Cup Profile section completely rewritten from "no peer-reviewed data" stub to full sensory description, intra-Antioquia terroir table, volatile compounds; Geisha comparison table updated for Chiroso sensory row; BCH/CHCH cup profile gap added as new open questions; Pazmiño-Arteaga 2022 added to Key Sources; source_count 2→3
- `wiki/shared/terroir.md` — Caturra Chiroso Antioquia study added to Empirical Evidence table as second primary terroir study (methodologically the cleanest isolation design in the wiki)
- `wiki/index.md` — source indexed; chiroso.md concept description updated to reflect cup profile now sourced

**Key findings**:
- Caturra Chiroso cup profile (under 60h extended fermentation): **sweet, citric acidity, juicy body, aromatic and floral notes**
- Terroir confirmed within a single variety + identical post-harvest protocol: El Peñol (2,100m) > Urrao (1,830m) > Fredonia (1,800m) — 3 statistically distinct sensory groups
- Variation between origins > variation between lots within origin — reproducibility of post-harvest protocol validated
- Altitude is the likely primary quality driver: El Peñol (2,100m) significantly outperforms the two 1,800m sites; El Peñol and Fredonia share andosol soil type but differ in altitude and quality
- 14 volatile compounds identified; dominant (roast-derived): 2-furaldehyde, 2-furanmethanol, 2-methylbutanal; differentiating (fermentation-derived): 2-butanone and acetoin — acetoin connects to lactic acid fermentation and [[shared/fermentation-flavor-compounds]]
- Local microflora (agroecological variable, not controlled by protocol) likely drive acetoin variation between origins — terroir acts through fermentation microbiology even when protocol is standardized
- PCA: 89.83% variance in 2 components; three clean origin clusters; Fredonia most consistent (tightest), El Peñol most variable (inter-lot)

**Important protocol caveat**: Post-harvest protocol in this study is a 60-hour multi-stage extended fermentation (12h cherry → depulp → 12h dry → 36h submerged → wash). This is NOT standard washed. The documented cup profile is specific to this processing approach. Standard-washed Caturra Chiroso cup profile remains undocumented in this wiki.

**Cross-domain flags**:
- Processing: the 60h multi-stage protocol is a form of extended wet fermentation analogous to the SIAF research (Silva 2024, Braga 2023); acetoin as terroir-driven volatile connects to [[shared/fermentation-flavor-compounds]] (lactic fermentation products)
- Terroir: Caturra Chiroso is now the second primary case study in [[shared/terroir]] alongside Panama Geisha (Ledezma 2025); the Chiroso study controls for post-harvest method while Ledezma did not — they are complementary evidence

---

## [2026-06-25] lint | shared | Overclaim correction — soil as "minor direct impact" on terroir

**Error**: `wiki/shared/terroir.md` and `wiki/varietals/concepts/terroir.md` both stated soil had "minor direct impact" on terroir, attributed to Williams 2022. The source's actual characterization is "inconclusive" — a stronger epistemic caveat that the wiki weakened during ingest.

**The evidence problem**: Soil type co-varies with altitude, microclimate, and variety in virtually all real-world coffee-growing field settings. No controlled study holds these three variables constant while isolating soil geology. "Inconclusive" does not mean "small effect" — it means the effect cannot be measured with available data. Commercial consensus (producer marketing, specialty trade press) systematically overclaims soil's importance because it is emotive and location-specific. The peer-reviewed literature may understate it because controlled isolation studies don't exist.

**Plausible mechanisms that remain untested**: K/Ca/Mg uptake → enzyme function and organic acid synthesis in the cherry; drainage → root oxygenation → maturation quality. These are agronomically established pathways in other crops; effect size in coffee cup quality is genuinely unknown.

**Why wine soil evidence doesn't directly transfer**: Wine terroir science (Burgundy geological studies) finds demonstrable soil effects but wine undergoes fewer transformation steps (grape → fermentation → wine). Coffee's chain (soil → tree → cherry → fermentation → drying → green bean → roasting → brewing) provides more steps at which soil-mineral signals can be masked.

**Fixed in**:
- `wiki/shared/terroir.md` — Layer 1 table: soil cell changed from "Minor direct impact" to "Inconclusive — confounding with altitude/climate makes isolation difficult"; new "Soil — The Evidence Problem" section added after Shading section; soil added to Open Questions
- `wiki/varietals/concepts/terroir.md` — soil bullet updated with full caveat; Open Questions soil note updated

---

## [2026-06-25] ingest | varietals + shared | Does Coffee Have Terroir and How Should It Be Assessed? — Williams et al. (2022)

**Source**: Williams, S.D., Barkla, B.J., Rose, T.J., Liu, L. *Foods* 11, no. 13: 1907. 2022. PMC9265435. DOI: 10.3390/foods11131907. MDPI.
**Credibility**: **High-Medium** — PMC-indexed, peer-reviewed, cited as framework paper by Ledezma et al. 2025. Limitations: review paper (no new experimental data); AgriFutures Australia funder (minor commercial interest in Australian terroir value).

**Structural decision**: This ingest prompted a structural reorganization of the terroir concept within the wiki. Williams 2022 explicitly frames terroir as a cross-domain concept spanning varietals (environmental origin), processing (post-harvest methods as terroir component), and brewing (assessment/expression). Filed the master terroir framework in `wiki/shared/terroir.md` and narrowed `wiki/varietals/concepts/terroir.md` to environmental origin factors only — consistent with the wiki's existing cross-domain pattern (sweetness-perception, fermentation-flavor-compounds, honey-processing, wet-hulling all live in shared/).

**Pages created**:
- `wiki/varietals/sources/coffee-terroir-williams-2022.md` — source page
- `wiki/shared/terroir.md` — NEW cross-domain terroir framework: formal definition; layered model (environmental/variety/post-harvest processing); processing as terroir; coffee vs. wine terroir distinction; altitude effects quantified; shading nuance; assessment protocol (SCA cupping, Agtron 65); biochemical markers; empirical evidence table

**Pages updated**:
- `wiki/varietals/concepts/terroir.md` — narrowed to environmental origin factors (Layer 1); Williams 2022 altitude quantification and shading nuance added; [[shared/terroir]] cross-reference added; source_count 1→2
- `wiki/processing/overview.md` — [[shared/terroir]] linked in Key Concepts; post-harvest processing as terroir noted
- `wiki/brewing/overview.md` — "Terroir Assessment Standard" section added; cupping as industry reference; [[shared/terroir]] linked
- `wiki/index.md` — source, shared/terroir indexed; terroir concept description updated

**Key findings**:
- Formal proposed definition: "The terroir of coffee is defined as the unique sensory experience derived from a single origin roasted coffee that embodies its source"
- Terroir is fixed at cherry harvest — roasting and brewing affect expression, not terroir itself
- Post-harvest processing IS part of coffee terroir (unlike wine) — processing method is often environmentally determined (Colombia's high rainfall forces washed; dry regions use natural)
- SCA cupping (8.25g/150mL, 93°C, medium-light Agtron 65, WCR Lexicon) is the recommended terroir assessment standard
- Brew method modifies terroir expression but cannot change it: espresso (enhances bitterness/roasted), filter (emphasizes fruity), cupping (balanced middle position)
- Altitude >1,000m, rainfall <1,600mm → aromatic/acidic/body; altitude <850m, rainfall >2,110mm → bitter/grassy/astringent
- 2.5°C temperature difference can shift quality grade — microclimates matter beyond coarse altitude data
- Shading: positive at low altitude (extends maturation), potentially negative at high altitude (further reduces already-limited radiation)
- Variety is second most important factor after altitude: Caturra (fruity/acidic/tarty) vs. Typica (balanced/bitter/full-bodied) at >800m
- Biochemical markers (GCMS, HPLC-QTOF, Raman, NIR) can validate sensory terroir assessment but should not replace it

---

## [2026-06-26] ingest | brewing | Allongé vs. Standard Espresso: Roast Level, Flow Rate & Flavor — Scott Rao Masterclass (Decent Espresso, 2025)

Source: raw/brewing/Scott Rao Masterclass Allongé vs. Standard Espresso - Roast Level, Flow Rate & Flavor.md
Credibility: High-Medium (practitioner) — Rao; Gagné transport/diffusion framework second-hand

Pages created:
- wiki/brewing/sources/rao-allonge-roast-flow-2025.md

Pages updated:
- wiki/brewing/concepts/espresso-fundamentals.md — major additions: roast level → brew ratio table; flow rate × roast level mechanism; transport/diffusion extraction section; Turbo shot; Allongé specifics (4.5 ml/sec, 26-27% EY); deep bed and paper filter channeling prevention; dialing-in philosophy (single variable); source_count 1→2
- wiki/roasting/concepts/roasting-parameters.md — mass loss table rebuilt with Rao's roast category labels + brew ratio column as a second source column alongside Lindsey 2024; extraction potential vs. roast level note (dark roasts burn off solubles → lower EY potential)
- wiki/brewing/entities/decent-espresso.md — Allongé parameters updated (4.5 ml/sec, 26-27% EY, Montreal café validation); Turbo shot added
- wiki/index.md — source indexed; espresso-fundamentals description updated

Key additions:
- Roast mass loss → brew ratio cross-domain decision table: Nordic 11% → 4-5:1; Light/Medium 12-13% → 3:1; Medium 14-15% → 2:1; Dark 16-18% → 1:1
- 11% mass loss = Nordic boundary (Rao: barely not grassy); corroborates Lindsey 2024's <12% underdevelopment threshold from sensory angle
- Flow rate rule: light roast → high flow (fruit acids); dark roast → low flow, short shot (manage bitters)
- Extraction potential peaks at light/medium roast — dark roast burns off solubles; EY potential declines beyond ~14-15% mass loss. Consistent with Lindsey 2024
- Transport (surface stripping, fast) vs. diffusion (cellular chambers, time-based) as two extraction mechanisms; Allongé may include more diffusion than standard espresso; Blooming explicitly separates the two phases
- Turbo shot: high-flow short shot; Allongé alternative for channeling-prone setups; Turbo Turbo ~3.5 ml/sec

---

## [2026-06-26] ingest | brewing | Blooming Espresso, Filter3 & Quakers — Scott Rao Masterclass (Decent Espresso, 2025)

Source: raw/brewing/Scott Rao Masterclass on Blooming Espresso, Filter 3 & what about Quakers?.md
Credibility: High-Medium (practitioner) — Rao (established roasting/brewing authority); JB (Decent Espresso co-founder); masterclass video transcript; Gagné theory second-hand

Pages created:
- wiki/brewing/sources/rao-blooming-filter3-quakers-2025.md
- wiki/shared/quakers.md — cross-domain concept: immature beans; processing-method quaker prevalence; sorting protocol; cup impact
- wiki/brewing/entities/decent-espresso.md — Decent Espresso machine; John Buckman; Blooming/Allongé/Filter3 capabilities

Pages updated:
- wiki/brewing/concepts/espresso-fundamentals.md — major update from stub: light-roast espresso strategies section (Blooming/Allongé/Filter3 with practical tips); pre-infusion mechanics (max flow > slow flow); astringency sources (3: channeling/quakers/underdevelopment-CGA); source_count 0→1
- wiki/roasting/concepts/roasting-parameters.md — CGA section: underdevelopment-astringency link added (Rao 2025 — CGA is astringent; severe underdevelopment leaves excess CGA → astringency from roasting failure, not brewing)
- wiki/index.md — source, 3 new pages indexed; espresso-fundamentals description updated

Key additions:
- Astringency sources framework sourced: (1) channeling — suspended particles (Gagné theory; nylon filter evidence); (2) quakers — even one disrupts cupping bowl; (3) severe underdevelopment → excess CGA astringency
- Quakers fully documented: smell test (fruity/nutty); washed vs. natural prevalence; optical sorting; Rao's 20% removal; cost-benefit calibration; aftertaste truncation mechanism
- CGA chain now has a lower bound: underdevelopment leaves too much CGA → astringency (in addition to upper bound: dark roasting destroys CGA regardless of processing)
- Light-roast espresso strategies: Blooming (contact time, Decent only), Allongé (solvent volume, any machine), Filter3 (no-bypass filter, Decent only)
- Pre-infusion principle sourced: maximum flow > slow flow (slow over-extracts puck top, under-extracts bottom)
- Decaffeination removes 90%+ of astringent compounds — explains why decaff tolerates extreme percolation without astringency

---

## [2026-06-26] ingest | roasting | DT Sensory Modulations — Alstrup et al. 2020 (Beverages)

Source: raw/roasting/The Effect of Roast Development Time Modulations on the Sensory Profile and Chemical Composition of the Coffee Brew as Measured by NMR and DHS-GC–MS.md
Credibility: High-Medium — Beverages (MDPI); NMR + DHS-GC-MS + PLS; 46 professional tasters; single origin; Agtron 76 only; French Press; mild CoffeeMind COI

Pages created:
- wiki/roasting/sources/dtr-sensory-alstrup-2020.md

Pages updated:
- wiki/roasting/concepts/roasting-parameters.md — DT section rewritten with sourced sensory table; diacetyl and 2,3-pentanedione as sweetness compounds; acid ratio finding; body no-effect finding (flagged); pyridine as baked marker; Maillard section updated with specific sweetness ketones; source_count 2→3
- wiki/shared/sweetness-perception.md — new "Specific sweetness compounds" section: diacetyl/2,3-pentanedione as Maillard-derived sweetness compounds; fast DT → more diacetyl → higher sweetness; cross-domain diacetyl note (fermentation + roasting pathways); open question partially answered; source_count 1→2
- wiki/shared/fermentation-flavor-compounds.md — new "Diacetyl — Two Upstream Pathways" section: fermentation vs. roasting origins; implications for profile decisions by processing type
- wiki/index.md — source indexed; roasting-parameters, sweetness-perception, fermentation-flavor-compounds descriptions updated

Key additions:
- DT has large sensory effects at constant Agtron color — color alone is insufficient as QC
- Sweetness compounds sourced: diacetyl (2,3-butanedione) and 2,3-pentanedione; Maillard-derived; peak at fast DT; actionable: shorter total roast time within DTR window → more diacetyl → sweeter cup
- Body finding: DT had NO effect on body perception (p=0.37) — only non-significant result; flagged as controversial; French Press confound; don't generalize to pour-over without testing
- Acid ratio: DT degrades all acids proportionally; cannot selectively favor malic vs. citric via DT alone
- Pyridine = chemical marker for baked roast defect (monotonically increases with DT)
- Diacetyl cross-domain chain: same compound arrives via fermentation (lactic acid bacteria) AND via fast DT Maillard reactions — extended fermentation + fast DT roast = potentially additive sweetness

---

## [2026-06-26] ingest | roasting | The Art and Science of Coffee Roasting: Fundamentals, Control, and Technological Innovations — Campos & Silva (book chapter, 2025)

Source: raw/roasting/The Art and Science of Coffee Roasting - Fundamentals, Control, And Technological Innovations.md
Credibility: Medium-High (book chapter in academic/professional volume; primary synthesis with 40+ peer-reviewed references; most recent citations 2025)
Purpose: ingested as the structural anchor for the roasting domain — provides the temperature framework, phase structure, and chemical mechanism overview assumed as background by prior narrower ingests

Pages created:
- wiki/roasting/sources/roasting-fundamentals-campos-silva-2025.md

Pages updated:
- wiki/roasting/overview.md — 6-phase temperature framework table added; roasting chemistry quick reference added; Key Sources section replaced from "none" to all 4 ingested sources; last_updated corrected
- wiki/roasting/concepts/roasting-parameters.md — first crack 175-185°C BT; Maillard range 120-180°C; medium roast → pyrazines/furans → chocolate/caramel/nutty/hazelnut; CGA → caffeic acid + lactones; >800 volatiles from lipid×nitrogen; bean density principle (denser = longer exposure); slow roasting = volatile degradation (sourced Lee 2024 via chapter); Campos & Silva added to Key Sources; source_count 3→4
- wiki/roasting/concepts/roaster-types.md — drum → body/depth and fluidized bed → fruit/acidity now sourced; airflow role added; UNSOURCED STUB status removed; Key Sources section added; source_count 0→1
- wiki/index.md — source indexed; roasting/overview description updated to reflect 6-phase anchor; roasting-parameters description updated

Key additions:
- **6-phase framework**: Drying (~25→120°C) → Initial Browning (~120→150°C) → First Crack (~150→185°C; 1C at 175-185°C BT) → Development → Second Crack (225-235°C) → Cooling
- **First crack temperature**: 175-185°C bean temperature is now a sourced anchor value
- **Second crack**: 225-235°C; partial carbonization begins; outside specialty quality range
- **Maillard temp range expanded**: begins ~120°C (not 150°C as previously noted); extends to ~180°C
- **Medium roast specifics**: pyrazines + furans from intensified Maillard → chocolate, caramel, nutty, hazelnut notes (now sourced)
- **CGA decomposition products**: caffeic acid + lactones — the specific molecules CGA breaks down into
- **800+ volatiles**: total count of identified volatile substances from all roasting chemistry
- **Dense beans**: longer heat exposure required; altitude is the primary density driver; implication for high-altitude specialty coffees
- **Slow roasting = volatile degradation**: sourced as distinct from baked defect mechanism; both extremes (too fast, too slow) degrade cup quality

---

## [2026-06-26] ingest | brewing + shared | Managing Astringency in Coffee Brewing — Scott Rao (scottrao.com, 2020)

Source: raw/brewing/Managing astringency in coffee brewing.md
Credibility: High-Medium (practitioner) — Rao 2020 blog post; predates Gagné's 2022 filtration model; references Gagné's older 2019 post

Pages created:
- wiki/brewing/sources/rao-astringency-management-2020.md

Pages updated:
- wiki/shared/astringency.md — CGA tension section replaced with partial resolution: CGA as "large molecule that extracts less readily" (Rao 2020) is consistent with Gagné's filtration model; timeline table added (Gagné 2019 → Rao 2020 → Gagné 2022 → Rao 2025); Rao diagnostic protocol added; open questions updated; Rao 2020 added to Key Sources
- wiki/brewing/concepts/espresso-fundamentals.md — CGA tension note updated from "open question" to "partially reconciled"; Rao 2020 added to Key Sources; open question updated; source_count 3→4
- wiki/index.md — source indexed; astringency description updated
- wiki/log.md — this entry

Key addition:
- **CGA reconciliation**: the apparent contradiction between "Rao says CGA causes astringency" and "Gagné says astringency is a filtration problem" is partially resolved. Rao's 2020 description of CGA as a "large molecule that extracts less readily" is consistent with Gagné's model — CGA is soluble in principle but only partially dissolved during typical brewing, leaving a suspended fraction filterable by the coffee bed. The tannin part of Rao's 2020 claim is likely superseded by Gagné 2022 (wine tannins not found in coffee). Whether Smrke's identified compound is CGA or something else remains open.
- **Diagnostic protocol**: five-step decision tree to isolate channeling vs. underdevelopment vs. quakers as the cause of a specific astringent cup.

---

## [2026-06-26] ingest | brewing + shared | The Mechanism Behind Astringency in Coffee — Jonathan Gagné (coffeeadastra.com, 2022)

Source: raw/brewing/The Mechanism Behind Astringency in Coffee.md
Credibility: High-Medium (practitioner-scientist) — physicist; author of "The Physics of Filter Coffee"; direct input from Samo Smrke (food scientist, ZHAW); empirically tested predictions; specific chemical compound not yet peer-reviewed at time of writing

Pages created:
- wiki/brewing/sources/gagne-astringency-mechanism-2022.md
- wiki/brewing/entities/jonathan-gagne.md
- wiki/shared/astringency.md

Pages updated:
- wiki/brewing/concepts/espresso-fundamentals.md — astringency section rebuilt with Gagné's filtration model; grind-size ceiling; pressure mechanism; CGA tension; open question added; Gagné added to Key Sources and Related Concepts; source_count 2→3
- wiki/shared/quakers.md — astringency mechanism note updated to flag quaker pathway uncertainty; [[shared/astringency]] added to cross-domain connections; Gagné 2022 added to Key Sources; source_count 1→2
- wiki/index.md — gagne-astringency-mechanism-2022, jonathan-gagne, and shared/astringency indexed; espresso-fundamentals and quakers descriptions updated
- wiki/log.md — this entry

Key additions:
- **Core model**: astringency = filtration problem, not over-extraction. Astringent compounds nearly insoluble at ≤90°C → float as suspended particles → filtered out by thick, flat, undisturbed bed with slow, even flow.
- **Grind-size ceiling**: finer grind → more broken cells → more particles liberated (proportional to surface area). Beyond the ceiling, no filtration improvement helps. Empirically confirmed at CRS (SOL dripper, near-espresso grind, paper filter, even flow — still astringent).
- **Pressure effect**: high pressure (espresso: 9 bar) drags particles through the bed faster → inherently more astringent. Filter3 (0 bar) is the opposite.
- **70°C experiment**: EY 27%, no astringency, but cup profile significantly dull (earthy, chocolaty, vegetal, less vibrant acidity). Rao confirmed same observation "years ago." Not a practical solution.
- **Decaf observation**: decaf nearly immune to astringency; decaf processing appears to affect or destroy the astringent compound. Useful for fine-grind experimentation.
- **CGA tension flagged**: CGA (underdevelopment astringency, Rao) is water-soluble — it cannot be filtered by Gagné's mechanism. Two distinct astringency mechanisms may exist in parallel. Open question.
- **Specific compound**: identity withheld in 2022 pending peer review by Smrke's colleagues. NOT wine tannins (searched for and not found in coffee).

---

## [2026-06-26] ingest | roasting | Coffee Roasting Fundamentals — Scott Rao (scottrao.com, 2020)

Source: raw/roasting/Coffee Roasting Fundamentals.md
Credibility: High-Medium (practitioner) — DTR inventor; 600+ roasting consultations; blog post, not peer-reviewed

Pages created:
- wiki/roasting/sources/coffee-roasting-fundamentals-rao-2020.md
- wiki/roasting/entities/scott-rao.md

Pages updated:
- wiki/roasting/concepts/roasting-parameters.md — DTR sourced to Rao (inventor); 20–25% flagged as general guideline, not prescription; priority order added (smooth RoR first, then DTR); baked roast defect section (RoR crash, not slow roasting; sensory: less sweet, hollow, straw, flat acidity); roast time principle (batch size/burner output determines duration); probe calibration warning; source_count 1→2
- wiki/roasting/entities/aillio-bullet.md — IBTS evolution section: Rao's 2020 critique of single-sensor IBTS is addressed by R2 Pro's 128-point array
- wiki/index.md — source and entity indexed; roasting-parameters and aillio-bullet descriptions updated
- wiki/log.md — this entry

Key additions:
- DTR origin confirmed: Rao invented it; 20–25% is the general guideline for most specialty targets, NOT a universal target
- Baked roast mechanism sourced: caused by hard RoR crashes, not slow roasting — critical distinction
- Priority order (Rao's explicit teaching): Step 1 = smooth RoR; Step 2 = DTR and everything else
- Do not copy bean/drop temperature targets across machines — probe calibration varies by ±10°F
- Aillio IBTS: Rao's 2020 "single-sensor is less accurate than BT" critique refers to the v2's single-point IR; R2 Pro's 128-point IBTS is the improvement he was anticipating
- New open tension: Münchow et al. 2020 (peer-reviewed) found professional tasters could not detect baking defect above chance in blind discrimination — contradicts Rao's practitioner consensus; unresolved in the wiki; priority ingest if paper is available

---

## [2026-08-01] query | brewing | Yunnan Purple Leaf Caturra K72 washed — brew recommendation, roaster critique, dialed recipe filed

Query: recommend brew parameters for a Yunnan (China) Purple Leaf Caturra, K72 washed, 1,720–1,800m, roast 2/5 (white floral/melon/green tea/spice); critique roaster's own rec (1:13, 89–92°C, 1–1.5 min, TDS 1.15–1.35%, water 50–110 PPM). Answer iterated in-chat to a validated recipe with measured TDS, then filed on CK's request ("file all three").

Pages created:
- wiki/brewing/concepts/bypass.md — new concept: dilution bypass; decouples EY from TDS; low-EY clarity vs. bypass clarity vs. cold-brew comparison; conservation-of-solids math; worked example + dial guidance
- wiki/brewing/sources/yunnan-purple-caturra-k72-label.md — bag label + roaster rec (critiqued) + CK's dialed recipe + measured result
- wiki/varietals/concepts/purple-leaf-caturra.md — Caturra (Bourbon dwarf mutation) + purple-tip anthocyanin phenotype; not a confirmed distinct cultivar; CLR-susceptible
- wiki/varietals/entities/china-yunnan.md — Yunnan origin (place); ~95%+ of China's coffee; Catimor legacy → emerging specialty
- wiki/processing/concepts/k72-washed.md — extended (~72h) controlled-ferment washed; terminology caution per Kornman

Pages updated:
- wiki/index.md — 5 rows added (bypass, label source, purple-leaf-caturra, china-yunnan, k72-washed)
- wiki/log.md — this entry

Key findings:
- Roaster's 1:13 + TDS 1.15–1.35% + 1–1.5 min implies LOW extraction (~14% EY) — buys clarity by under-extracting; sacrifices sweetness/body. Critiqued against Ethiopia/Kenya washed row in brewing/overview.
- CK's alternative: brew 1:15 through bed (EY ~20.5%) then bypass ~10% to thin strength — clarity via dilution, sweetness kept. Same clarity goal, opposite mechanism.
- Measured result (validated over the conversation): 15g dose, 225g through bed + 25g bypass = 250g water, ~215g cup, TDS 1.43% → EY ~20.5%. Grinder recorded: Timemore O78s @ 17 (zero = just above burr touch). "Coffee-like, not tea-like."
- Bypass % established as a strength dial independent of grind/temp and of the 4:6 flavor/strength axes; to reach ~1.30% TDS at same EY, bypass ~19%.

Open questions / flags:
- No Comandante-equivalent recorded for Timemore O78s @ 17 — grind not cross-referenced to wiki's Comandante scale.
- "Purple Leaf Caturra" not in WCR 2025 catalog under that name — phenotype vs. named selection unresolved.
- K72 protocol is label-level only (duration implied, mechanism undisclosed) — priority: a producer/roaster technical source. Same Kornman terminology caveat as other ferment labels.
- Yunnan/China has no authoritative varietals source yet — entity seeded from label + general knowledge; priority ingest.
- EY ~20.5% near top of band for light-medium washed; ~1 pt headroom before astringency risk.

---

## [2026-08-01] ingest | processing | Kornman "Green Coffee" — RE-INGEST (Figure 1 flowchart now searchable markdown)

Re-ingest of an existing source. Raw file `raw/processing/Green Coffee ... [Excerpt on Processing].md` was updated to append **Figure 1 ("Coffee Processing Types") as a plain-markdown table** (previously an embedded `.jpeg` only, not full-text searchable). No new prose claims; the value is making the flowchart's content searchable and cross-referenced.

Pages updated:
- wiki/processing/concepts/processing-terminology.md — REPLACED the image-only "Kornman's Processing Flowchart" stub with the full rendered table (10 steps × 9 methods), a legend (🟩 Always / 🟦 Usually / 🟨 Sometimes / 🟫 Rarely / 🏁 Partially), and a "What the table clarifies" interpretation; last_updated 2026-06-22→2026-08-01; tags += flowchart, step-decomposition
- wiki/processing/sources/kornman-green-coffee-2022.md — flowchart claim expanded (steps × methods); re-ingest note added; the "stored as image, not searchable" open question marked RESOLVED; Wiki Pages Updated annotated
- wiki/processing/overview.md — pointer added under the Processing Methods Summary table to Kornman's step decomposition; concept link description updated; last_updated 2026-06-19→2026-08-01
- wiki/index.md — source + processing-terminology descriptions updated (flowchart now searchable table), dates bumped to 2026-08-01
- wiki/log.md — this entry

Key interpretation captured from the now-searchable table:
- Washed vs. Honey is defined at the DRYING step (clean parchment vs. parchment-with-mucilage), not depulping — both depulp.
- Triple washed = double washed + cherry flotation ("Always"); double's flotation only "Sometimes".
- Eco-pulped/demucilaged dries in clean parchment ("Always") but skips traditional fermentation + washing channels ("Rarely") → mechanical reason it gets mislabeled "washed".
- Wet hulled uniquely "dried as seed/green bean = Always" and only "Partially" in clean parchment (Giling Basah wet-parchment removal).
- Carbonic maceration = whole-cherry subset of sealed-tank; anaerobic may be depulped ("Sometimes").

No contradictions with existing wiki content. Consistent with prior terminology critique and with [[shared/wet-hulling]], [[shared/honey-processing]].

---

## [2026-08-01] ingest | varietals | Production and trade of specialty coffee in Brazil — Sera et al. 2025 (Scientific Reports)

Source: raw/varietals/Production and trade of specialty coffee in Brazil.md
Credibility: **High** — peer-reviewed (Nature portfolio, doi:10.1038/s41598-025-26620-x); Brazilian public-institute researchers; primary data from BSCA (175 farms), IBGE census, national cultivar registry (RNC). Agronomic/economic focus; sensory claims secondary.

Fills the wiki's **largest origin gap**: no Brazil entity existed despite Brazil being the world's largest producer and already referenced across the wiki (Brazilian naturals, Caturra/Mundo Novo/Catuaí origin, pulped-natural invention).

Pages created:
- wiki/varietals/sources/brazil-specialty-coffee-sera-2025.md
- wiki/varietals/entities/brazil.md — NEW origin entity (geography, cultivars, processing, economics, GI, research base)
- wiki/varietals/concepts/mundo-novo.md — NEW (Typica × Bourbon; ~80% of Br Arabica with Catuaí; absent from COE tops)
- wiki/varietals/concepts/catuai.md — NEW (Mundo Novo × Caturra; dominates COE Brazil tops; 13-cultivar ambiguity)

Pages updated:
- wiki/varietals/concepts/introgressed-varieties.md — Brazilian section: Icatu route (arabica × canephora, NON-Timor-Hybrid) + Catucaí; HdT-derived Brazilian cultivar list; COE Brazil 2019–22 evidence introgressed cultivars reach >90 (Catucaí 785-15 90.03; Catucaí Amarelo 2SL 90.53); Catiguá MG2 cross-domain bridge; source_count 2→3
- wiki/varietals/concepts/arabica-variety-taxonomy.md — WCR 5-tier quality scale named (very low→exceptional); Sera critique that its basis is "unclear" and origin-blind (WCR "exceptional" cultivars not registered in Brazil, yet Brazil makes 90+ COE from "good"-rated Catuaí); source_count 3→4
- wiki/varietals/concepts/bourbon.md — Mundo Novo + Catuaí added as descendants; Brazilian Bourbon Amarelo preference; source_count 2→3
- wiki/varietals/overview.md — Brazil growing-region entry
- wiki/processing/concepts/processing-terminology.md — Brazilian "semidry = natural pulped = cereja descascado (CD)"; dominant in Brazilian specialty; 23 producer terms as non-standardization example; source_count 1→2
- wiki/index.md — 4 new rows (source, entity, 2 concepts) + refreshed introgressed/taxonomy/terminology descriptions
- wiki/log.md — this entry

Key findings:
- 66.1% Arabica / ~34% Canephora (robusta Rondônia; conilon Espírito Santo). Specialty ~38k ha of 1.872M; Minas Gerais 82% of specialty area. One of cheapest specialty origins (avg $4.43/kg, mean score 83 vs world 84.5).
- Mundo Novo + Catuaí = ~80% of Arabica. On BSCA farms: Mundo Novo+Acaiá 110; Bourbon group 50; introgressed 87 (52% HdT-derived, 48% Icatu-derived).
- **Introgression ≠ low quality**: Brazilian Icatu/Catucaí + HdT-derived cultivars place at COE tops and exceed 90. Strengthens the wiki's "improving" note with hard evidence; partially answers the standing open question on introgressed cup quality.
- Semidry/pulped-natural (CD) dominates; wet only ~20%; dry hardest for specialty. Paper: literature does NOT establish superiority of any processing method — quality tracks postharvest conditions + environment.
- WCR quality tiers critiqued as unclear-basis and origin-blind (credibility caveat now recorded on the taxonomy page).

Cross-domain:
- Processing: Brazilian semidry/CD nomenclature added to processing-terminology; reinforces Kornman non-standardization thesis.
- Processing×Varietals bridge: Catiguá MG2 now linked across the SIAF study (processing) and Brazilian introgressed cultivars (varietals).
- Roasting/green-buying (CK goal): Brazilian specialty = semidry Mundo Novo/Catuaí or introgressed cultivars from Minas Gerais → sweetness/body-forward, nutty-chocolatey; best lots (Catuaí, Bourbon Amarelo, Icatu-derived) 87–90+.

---

## [2026-08-02] ingest | brewing | A new Coffee Brewing Control Chart — Guinard et al. 2023 (J. Food Science, UC Davis)

Source: raw/brewing/A new Coffee Brewing Control Chart relating sensory properties and consumer liking to brew strength, extraction yield, and brew ratio 1.md
(Broken /servlet reference links in the raw file were repaired to full Wiley paths before ingest.)
Credibility: **High** — peer-reviewed; UC Davis Coffee Center; synthesis of three prior peer-reviewed studies (Frost 2020, Batali 2020, Cotter 2021); RSM; IRB consumer panels. Same lab as the wiki's cold-brew source.

Pages created:
- wiki/brewing/sources/brewing-control-chart-guinard-2023.md
- wiki/brewing/concepts/brewing-control-chart.md — the new BCC framework (Sensory + Consumer + the TDS/PE/ratio math)
- wiki/brewing/entities/uc-davis-coffee-center.md — org entity (Ristenpart/Guinard/Batali/Frost/Cotter); ties together BCC + cold-brew + brew-temp + R_abs math

Pages updated:
- wiki/shared/sweetness-perception.md — independent corroboration of the 'sweet' aroma-illusion model (BCC places 'sweet' at low-TDS/low-PE; Batali 2020 monosaccharide analysis); source_count 2→3
- wiki/brewing/concepts/bypass.md — bypass reframed as a straight vertical (TDS-down, constant-PE) move on the BCC; canonical PE formula + R_abs≈2.1 reconciled with the empirical ~2.0–2.3 g/g retention
- wiki/brewing/concepts/dialing-in.md — BCC added as the target-setting framework; partially answers the standing TDS-target open question (for drip); source_count 0→1
- wiki/brewing/overview.md — new "Strength, Extraction & Sensory" section referencing the BCC + temp-secondary finding
- wiki/index.md — 3 new rows (source, concept, entity) + refreshed bypass & sweetness-perception descriptions
- wiki/log.md — this entry

Key findings:
- Governing equation: PE = [TDS/(1−TDS)]×(R_brew − R_abs), R_abs ≈ 2.1 (absorption/liquid-retention ratio).
- Sensory BCC (13 attributes; locations = where MAXIMIZED, not guaranteed): high-TDS/low-PE = acid/sour, citrus, berry, dried fruit; high-TDS/high-PE = bitter, astringent, roasted, burnt/ash, thick, black tea; low-TDS/low-PE (~18%) = 'sweet'.
- 'sweet' is an aroma illusion (quotes in the paper) — sugars below threshold (Batali 2020). Independent convergence with the SCA/OSU + Alstrup sweetness work already in the wiki.
- Consumer BCC: two clusters, no single "ideal." Cluster 1 (57%) dome, peak low-TDS/PE~18% ('sweet'; +tea/floral/citrus, −sour/burnt) = typical drinker. Cluster 2 (43%) saddle: bright-specialty (low-PE/med-high-TDS) AND dark-espresso (high-PE/med-TDS); +roasted/dark-choc/nutty, −paper/woody/green/rubbery = experienced drinker.
- Brew temperature has little sensory impact at fixed TDS/PE (Batali 2020) — reinforces temperature-last in dialing-in priority order.

Caveats recorded: attribute locations are maximization coordinates, not guarantees (coffee must contain the attribute); drip only (espresso/cold-brew BCCs are future work); consumers were young Northern-California black-coffee drinkers.

Cross-domain / connections:
- Sweetness: third independent line of evidence for aroma-driven sweetness now on shared/sweetness-perception.
- Bypass ↔ BCC: bypass = vertical TDS-down move; both share the R_abs/PE math; gives a chart-level explanation for why bypass reads cleaner/sweeter.
- CK target zone (sweetness-forward drip): low-to-mid TDS + ~18–21% PE; the Yunnan bypass cup (TDS 1.43/PE ~20.5) noted as an illustration of the "maximized-where, not guaranteed" caveat (upper-mid coordinate, yet sweet/clean because the light-medium washed coffee has little bitter/roasted to express).
- No contradictions with existing wiki content.

---

## [2026-08-24] ingest | brewing | Personal log (PILOT) — Cokain/Entrebox Ethiopia Gesha Village OMA Gesha 1931 Natural (Gold Label)

First `personal_log` ingest — a bought roasted bean → brewing domain → `wiki/brewing/logs/`. Free-format raw (Entrebox product page + CK's shorthand brew log) structured into the `logs/BEAN.md` schema.

Source: raw/brewing/Cokain- Ethiopia Gesha Village OMA Gesha 1931 Natural(Gold label) – 集氣箱 Entrebox.md
Credibility: bean-identity fields = **marketing/label claims** (commercial bias on grade/rarity — "Gold Label top 10%", "competition choice") → recorded **as-claimed**, linked out, not asserted as entity facts. Brew log + Agtron 75.8 = **first-party** (CK measured).

Pages created:
- wiki/brewing/logs/gesha-village-oma-1931-natural-gold-label.md

Pages updated:
- wiki/index.md — new "### Logs" subsection under Brewing; row added
- wiki/log.md — this entry

Extracted / derived:
- Identity (as-claimed): Ethiopia · Gesha Village Coffee Estate, OMA zone (Bench-Maji), 1931–2049m · Gesha (Gesha 1931) · Natural · Medium-Light (measured Agtron 75.8) · notes orange/green-tea/jasmine/grape · 100g, HKD 199 (was 499).
- Skipped (unknown in source): producer, crop_year, roasted_on.
- Brew (Neo Switch, dual-temp 91°C + 70°C tail): 15g / target 250g → actual 251.6g in 4:00 (target 3:00); beverage 213.8g (454.5 − 240.7 container); **TDS 1.56% → EY ~22.2%** (high, top of band); retention ~2.5 g/g.
- Read: slow 4-min draw drove EY high; 70°C cold tail mitigates astringency risk; plots upper-mid/high on the BCC.

Cross-refs (link-out, as-claimed): [[varietals/entities/ethiopia]], [[varietals/concepts/geisha]], [[brewing/concepts/neo-switch]], [[shared/astringency]], [[brewing/concepts/brewing-control-chart]]. No entity pages created from label claims (grounding guardrail).

Pilot notes for schema iteration: added `date_ingested` + `tags` (previously flagged minors); recorded first-party `Agtron` inside `roast_level`; measured brew fields (beverage weight, TDS, EY) captured in a per-brew table — candidate columns to formalize when the iteration-log schema is finalized.

---

## [2026-08-24] ingest | brewing | Personal log (PILOT #2) — Cokain/Entrebox Strawberry Chloris (Blend), espresso

Second `personal_log` pilot — a bought roasted **blend** → brewing domain. Chosen to stress-test the schema on (a) sparse traceability and (b) an **espresso** brew (different column set than the pour-over pilot).

Source: raw/brewing/Cokain Coffee Blend – Strawberry Chloris – 集氣箱 Entrebox.md
Credibility: bean identity = marketing/label claims (commercial-bias flavour hype); recorded as-claimed, linked out. Brew + diagnosis = first-party.

Pages created:
- wiki/brewing/logs/cokain-strawberry-chloris-blend.md

Pages updated:
- wiki/index.md — Brewing → Logs row added
- wiki/log.md — this entry

Extracted / derived:
- Identity (as-claimed): Colombia + Yunnan blend · Medium roast · notes strawberry/red-wine/rose/yogurt · 250g, HKD 169.
- Skipped (blend, unknown in source): region, farm, producer, varietals, crop_year, elevation, processing, Agtron.
- Brew (Decent Espresso XL, Blooming profile): O78S @ 4 · 15→45 g (1:3) · 95 °C. **Failed shot** — bloom flow too fast (>20 g vs 8–10 g target) → puck under-resisted → extraction pressure <3 bar. Fix: grind finer and/or raise dose. No TDS/EY (shot not viable).

Schema-iteration findings:
- **Espresso vs pour-over columns differ**: espresso row = Grind · Dose · Yield · Ratio · Temp · **Pressure** · Time · TDS · EY (vs pour-over's Water · Beverage). Confirms the iteration table must be **method-grouped with method-appropriate columns** — a key point to bake in when the WIP columns are finalized.
- Logs usefully capture **failed brews + fixes**, not just successes.

Cross-refs (link-out, as-claimed): [[varietals/entities/colombia]], [[varietals/entities/china-yunnan]], [[brewing/entities/decent-espresso]], [[brewing/concepts/espresso-fundamentals]], [[brewing/concepts/dialing-in]], [[brewing/sources/rao-blooming-filter3-quakers-2025]]. No entity pages minted from blend/marketing claims (grounding guardrail).

---

## [2026-08-24] ingest | brewing | Personal log (PILOT #3) — Coffee Collective "Reshad" Ethiopia Jimma Natural

Third `personal_log` pilot — a bought roasted bean from a **high-credibility specialty roaster** (Coffee Collective, DK), contrasting the marketing-page sources of pilots #1–2.

Source: raw/brewing/Reshad.md
Credibility: roaster source with genuine traceability (named producer Reshad Albuls, published farmgate price 10.8 USD/kg, variety/altitude) → **low commercial-bias**; still recorded as-claimed + linked out per Sourcing Discipline. Brew + TDS = first-party.

Pages created:
- wiki/brewing/logs/reshad-ethiopia-jimma-natural.md

Pages updated:
- wiki/index.md — Brewing → Logs row
- wiki/log.md — this entry

Extracted (as-claimed, credible): Ethiopia, Jimma (Agaro) · producer Reshad Albuls · variety 74110 (JARC 74 Series) · Natural · organic · 1900–2000 masl · Coffee Collective, roasted 2026-07-20 (filter roast), best-before 2026-10-20 · 250g HKD 220 from 啡人前 (2026-08-21). Consistent with the wiki's [[varietals/entities/ethiopia]] (Jimma natural) + [[varietals/entities/jarc]] (74110).
Brew (Neo Switch, single-temp 89°C): O78S @17 · 15g → 250g (actual 253.5g) · beverage 216g · TDS 1.52% → **EY ~21.9%** (high). Closed 50g bloom → open to 250g.

Schema-iteration notes:
- `roast_level` held the source's "roasted for filter" — a roast *intent*, not a level. Bought beans sometimes state a roast-for-filter/espresso target (a brew_target analogue) — flag for future schema thought.
- A high-credibility roaster (Coffee Collective) is a candidate for a real `brewing/entities` page and could even corroborate varietals facts — but **not minted from a single product page** (guardrail); left as plain text + link-out to existing ethiopia/jarc pages. Similarly `啡人前` (HK reseller) not entered as an entity.
- No entity pages minted.

---

## [2026-08-24] lint | brewing | Structure clean; Yunnan source misfiled; espresso/water coverage gaps

Scope: brewing domain — 44 pages (1 overview · 15 sources · 12 concepts · 13 entities · 3 logs).

Structure: **healthy.** No dead links. Only orphans are the 3 log pages (expected leaves; referenced from index). No contradictions or stale claims (Gagné↔Rao astringency tension already documented as a tension; 4:6 vs 2026-V60 differences noted as different systems).

Findings (actionable):
1. **Misfiled/provisional: `brewing/sources/yunnan-purple-caturra-k72-label`** — `source_type: other`, `raw_path: none` (bag label + first-party dialed recipe, filed as a "source" before the personal_log system). Not a credible source under Sourcing Discipline. **Recommend migrating → `brewing/logs/yunnan-purple-caturra-k72.md` (`personal_log`)**; resolves the long-standing provisional Yunnan cluster. Note: `brewing/concepts/bypass` cites it as its worked example — link updates on migration.
2. **Espresso coverage thin** vs pour-over (6+ pour-over concept pages; espresso only `espresso-fundamentals`). Decent profiles (Blooming/Allongé/Turbo/Filter3) live only in `rao-allonge`/`rao-blooming` sources + `decent-espresso` entity + the new espresso log. Suggest a `brewing/concepts/espresso-profiles` concept (grounded by existing Rao sources).
3. **No water/minerals concept** — referenced piecemeal (46-method 30–50 mg/L; roaster PPM recs) but no page. Needs a credible source first (SCA Water Standard / Hendon & Colonna-Dashwood "Water for Coffee") → then `brewing/concepts/water`.

Observation (not a defect): all 3 brewing logs land **EY ~22%** (21.9–22.2%) across different beans/temps — likely Neo Switch immersion + O78S @17 pushing extraction; watch as data accumulates (candidate "Neo Switch extraction tendency" note).

Actions taken: none yet (findings only). Pending: (1) Yunnan migration; (2) espresso-profiles concept; (3) water source hunt.

---

## [2026-08-24] update | all | Removed the provisional "Yunnan cluster"; refactored Purple Leaf Caturra → Caturra

Decision: start Yunnan from scratch (the cluster was label-grounded, no credible source). Removed the label-derived pages and repaired collateral links. (Historical ingest/query entries above are preserved — append-only log.)

Deleted:
- brewing/sources/yunnan-purple-caturra-k72-label (label + first-party recipe; source_type other, raw_path none — not a credible source)
- processing/concepts/k72-washed (label-derived, protocol unverified)
- varietals/entities/china-yunnan (label + general-knowledge seeded)

Refactored:
- varietals/concepts/purple-leaf-caturra → **varietals/concepts/caturra** — kept the WCR-grounded general Caturra facts (Bourbon dwarf mutation; parent of Catuaí and Colombia/Castillo; CLR-susceptible), dropped the Purple-Leaf phenotype / Yunnan / K72 label content. Grounded in wcr-arabica-varieties-catalog-2025 + history-of-arabica-wcr.

Kept (not Yunnan): brewing/concepts/bypass — grounded in the Guinard BCC paper; removed only its Yunnan worked-example section.

Collateral link fixes:
- varietals/concepts/catuai + varietals/entities/brazil → repointed purple-leaf-caturra → caturra
- brewing/logs/cokain-strawberry-chloris-blend → unlinked china-yunnan (plain "Yunnan")
- wiki/index.md → removed 3 rows; swapped purple-leaf-caturra row → caturra

Yunnan / K72 can be re-created later from a credible source.

---

## [2026-08-24] ingest | varietals | 德热296 / Dr296 — "Yunnan Purple-Leaf Caturra" is actually a Catimor (misnomer corrected)

Right after removing the label-grounded Yunnan cluster, ingested a credible-enough source that **corrects** what the cluster got wrong: the Yunnan "purple-leaf caturra" is not a Bourbon-Caturra — it's DTARI's Dr296, a Catimor.

Source: raw/varietals/国货之光——云南"德热296"是什么？.md (guchaju.com, 2024)
Credibility: article itself Low-Medium (commercial content site), but core identity **corroborated → Medium-High**:
- Official MoA germplasm registry (ctcgris.cn) confirms Dr296 is a real DTARI selection; DTARI certified stock = Catimor CIFC 7963 + Dr series (Dr3, Dr132).
- Peer-reviewed Frontiers 2025 (RAD-seq) on DTARI's Dehong collection → Bourbon/Typica + Ethiopian + Introgression(Catimor) groups.
- English trade: Dehong "Catimor P4 (7963)" @ ~1700m; Yunnan = Catimor country.
Exact "mutation of Catimor 7963" parentage + cup/bean claims remain Medium/single-source (as-claimed).

Pages created:
- varietals/sources/dr296-guchaju-2024.md
- varietals/concepts/dr296.md

Pages updated:
- varietals/concepts/introgressed-varieties.md — added 德热/Dr series (DTARI Catimor CIFC 7963 family: Dr296/Dr3/Dr132/Dr48-1/Dr199-1)
- varietals/concepts/caturra.md — "not to be confused with" disambiguation (Dr296 = Catimor; Colombia Purple Caturra = real Caturra)
- wiki/index.md — source + concept rows; caturra row note
- wiki/log.md — this entry

Key correction: "Yunnan Purple-Leaf Caturra" is a marketing **misnomer** for Dr296, a DTARI Catimor (introgressed, rust-resistant). Two distinct "purple caturras": Colombia's genuine Purple Caturra vs Yunnan's Dr296 (Catimor).

Process note: user flagged the naming concern → escalated to web research per Sourcing Discipline (verify high-impact claims) → grounding upgraded from single commercial source to corroborated (official registry + peer-reviewed context) before filing.

Follow-ups: Frontiers 2025 RAD-seq = a good standalone source for Chinese coffee genetics (worth its own ingest); DTARI could be a varietals entity; K72 processing concept re-creatable from this source (cross-domain).

---

## [2026-08-25] update | brewing | Reshad personal log — 2nd brew (dual-temp) added

Raw updated with a 2026-08-25 entry; added it to the existing Reshad log.
- Dual-temp 89/65 °C: O78S @17.2 (slightly coarser), 15.1 g → 251.1 g, beverage 211 g, TDS 1.57% → **EY ~21.9%**.
- vs the 08-22 single-temp (EY ~21.9%, TDS 1.52%): near-identical EY despite a coarser grind — the closed 65 °C tail + ~4-min drain lengthened contact and compensated. Deliberate variable = cold tail; finish effect pending a sensory A/B.
- Reinforces the ~22% EY pattern across Neo Switch pulls (cf. brewing lint observation).
- Corrected grinder-dial direction: on the Timemore O78s, **higher dial = coarser**.

Pages updated: brewing/logs/reshad-ethiopia-jimma-natural (brew 2 + TODO), wiki/index.md.

---

## [2026-08-25] ingest | brewing | Melet Yunnan 米良·觅月 — K72 "Purple-Leaf Caturra" (personal_log)

Second `bc_to_md.py`-generated personal log, enriched and ingested. First-party brew data (6 brews); bean identity **as claimed** with **elevated commercial bias** (Melet homepage not found → terroir/process quoted from other roasters' pages for the same coffee — flagged low-credibility).

- **Sourcing headline:** the bag ("紫叶卡杜拉 Purple-Leaf Caturra," K72-washed, Xiding 1720–1800 m) is a **textbook [[varietals/concepts/dr296|Dr296]] misnomer** seen in the wild — genetically a **Catimor**, not [[varietals/concepts/caturra|Caturra]]. Every claimed attribute matches the Dr296 profile; ydselects' K72 description independently corroborates the K72 protocol on the Dr296 page (both commercial-tier). Did **not** launder into asserted facts or re-create a K72-washed processing concept (still no credible source).
- **Brews:** Graycano ×1 (roaster 1:13 → TDS 1.82% / EY ~19.7%, over the roaster's own 1.15–1.35% TDS target); Neo-Switch ×4 (dual-temp 65–70 °C cold tails + bypass, 1:16–1:20, EY ~20.3–21.5%); Origami ×1 (single-temp 90 °C, EY ~22.7%, top/over band).
- **Read:** EY ~20–23% / TDS 1.37–1.82% → consistently **coffee-like**, vs the tea-like Dr296 target; lever to chase clarity = higher ratio/bypass + lower EY (coarser, cooler main pour). Ratio/EY computed at ingestion (tool now omits them by design).

Pages updated: brewing/logs/melet-yunnan-purple-leaf-caturra-k72 (new), varietals/concepts/dr296 (seen-in-the-wild backlink), wiki/index.md.

---

## [2026-08-30] ingest | brewing | Every Espresso Recipe Explained (Lance Hendrick)

Credible practitioner/educator video (YouTube transcript; typos expected & corrected during ingest — exception noted by user). Fills the long-standing espresso-recipe gap. Six espresso styles on **one stock 9-bar machine**, varying only **ratio + grind**; each measured (grind/dose/yield/TDS/EY).

- **New concept [[brewing/concepts/espresso-shot-styles]]** — ristretto→normale→lungo→turbo→allongé→sprover spectrum with corrected data table (the raw abstract table was column-shifted / missing sprover; user fixed it before ingest).
- **Key insights:** grind sets the **extraction ceiling** (turbo coarse 1:2.75 → EY 18% *below* lungo fine 1:3 → 22%; EY not monotonic with yield); turbo **6-bar-myth debunk** (7–15 s shots can't build 6 bar, hit ~5); **big yield → cooler temp** (80–85 °C) for allongé/sprover; sprover = stock-machine cousin of Rao's Filter3; Hendrick challenges 18–22% EY dogma (drinks 15–18%).
- **Contradiction flagged:** Hendrick's stock-machine allongé **~22% EY at 1:5.6** vs Rao's **26–27%** (Decent flow-control) — noted on both [[brewing/concepts/espresso-fundamentals]] and the new page; equipment/grind difference, not a real conflict.
- **New entities:** [[brewing/entities/lance-hendrick]] (author), [[brewing/entities/scott-rao]] (overdue — well-connected across espresso+roasting), [[brewing/entities/christopher-hendon]] (turbo paper), [[brewing/entities/matt-perger]] (sprover).

Pages updated: brewing/sources/every-espresso-recipe-explained-hendrick (new), brewing/concepts/espresso-shot-styles (new), brewing/entities/{lance-hendrick,scott-rao,christopher-hendon,matt-perger} (new), brewing/concepts/espresso-fundamentals (cross-link + stock-machine allongé note), brewing/overview (espresso section), wiki/index.md.

---

## [2026-08-30] ingest | brewing | Iced Coffee: 4:6 vs Hybrid Flash-Chill (Kasuya / Philocoffea)

Credible practitioner video (Japanese YouTube transcript + 4 recipe slides; typos corrected & JP→EN on ingest — exception noted by user). Extends the existing 4:6 + Switch work into **flash-chill (急冷) iced**.

- **New concept [[brewing/concepts/flash-chill-iced-coffee]]** — brew hot onto ice; two Kasuya recipes on the Hario Switch, shared base 20 g / 150 g hot (½ of 4:6's 300 g) / 80 g ice / 28 clicks:
  - **A — 4:6 applied** (30 g × 5, 90–93 °C): sharp acidity, defined outline → bright Kenya/Ethiopia.
  - **B — hybrid** (open 50 g → close 0:40 → open 1:30, keep temp up): smooth, cohesive, **standout sweetness**.
- **Finding:** method changes the cup **even iced at matched strength** (Kasuya expected otherwise); he preferred B and mused about switching all shop recipes. **Choose by bean**, not a single "correct."
- Sensory-only (no TDS/EY); grinder unstated (not asserted). Contrast with [[brewing/concepts/cold-brew]] flagged bidirectionally.

Pages updated: brewing/sources/kasuya-iced-46-vs-hybrid-philocoffea (new), brewing/concepts/flash-chill-iced-coffee (new), brewing/concepts/{46-method,neo-switch,cold-brew} (cross-links + iced sections), brewing/entities/tetsu-kasuya (flash-chill fact), brewing/overview (iced note), wiki/index.md.

## [2026-08-30] lint | brewing | Index tidy

Fixed a pre-existing index quirk: two concept rows (`cold-brew`, a duplicate `espresso-fundamentals`) were sitting under the brewing **Entities** header. Moved `cold-brew` into Concepts, merged the richer `espresso-fundamentals` description into its Concepts row, and removed the strays.

---

## [2026-08-30] ingest | brewing | Sandwich Extraction — Bavis Kwong 2026 WBrC 3rd (Cozy House analysis)

Ingested after an explicit worth-it evaluation (user gate). Verdict: worth it, **Focused scope** — the specific comp recipe is the vehicle for transferable principles. Source is a reputable SCA educator (暖窩 Cozy House); flags: mild **commercial bias** (course seller), recipe is **secondhand** comp transcription with acknowledged discrepancies (215g vs 250g; 94 vs 95 °C), Kasuya re-roast rumor **unconfirmed**.

- **New concept [[brewing/concepts/sandwich-extraction]]** — particle-size stratification: `1st paper → 2g fines → 2nd paper → 14g coarse`. Coarse top = acidity/florals (percolation); fines bottom = sweetness/body (delayed, low-agitation, near-immersion). Key reframe: **fines as a structural tool**, not a defect.
- **Best transferable ideas:** (1) grind distribution isn't just even/uneven — fractions have roles; (2) design extraction from the **sensory goal backward**; (3) every complex step must justify itself (and this is a **competition**, not operational, technique). Plus the **dry bloom as a timing device** (15g stays on top to delay the fines), and the dripper as a **thermal-gradient** device.
- **Cross-domain (roast↔brew):** extreme short-development roast (DTR ~10%, ~57s DT) bets on acidity; the bottom-fines immersion adds sweetness back → cross-ref added on [[roasting/concepts/roasting-parameters]].
- **Deferred (Focused):** standalone water concept (35ppm/pH6 vs SCA 50–175ppm) and varietal/processing spinouts (Green Tip Geisha, slow-dry/10.4% moisture) left as open questions; Roastwork/Janson/Sibarist mentioned, not filed as entities.

Pages updated: brewing/sources/sandwich-extraction-bavis-kwong-cozyhouse (new), brewing/concepts/sandwich-extraction (new), brewing/entities/{bavis-kwong,cozy-house-coffee,contour-drip} (new), brewing/entities/tetsu-kasuya (coach note), roasting/concepts/roasting-parameters (roast↔brew cross-ref), wiki/index.md.

---

## [2026-08-30] ingest | brewing | Clarity Pyramid — Simon Gautherin 2026 WBrC 2nd (Cozy House analysis)

Sibling of the sandwich-extraction ingest (same series/author/competition); worth-it verdict + **Focused scope** to match. Source: Cozy House (SCA educator); flags: mild commercial bias, recipe secondhand/as-claimed (ambiguous ~140g cut).

- **New concept [[brewing/concepts/clarity-pyramid]]** — framework *green creates → roast unlocks → brew selects → water highlights* (a near-restatement of the wiki's own variable-chain thesis; cross-linked to [[overview]]), plus **selective extraction** = subtraction (front ~10g discard + tail cut ~140/200g). Clarity defined as **legibility, not weakness** → the low-TDS/low-PE corner of the [[brewing/concepts/brewing-control-chart|BCC]].
- **No-bypass valve** family made explicit: NextLevel Pulsar ↔ Hario Switch (home substitute) ↔ Rao Filter3 / sprover.
- **Water:** 80ppm Mg:K:Si ≈ 3:2:1 → citrus/stone-fruit/silky (Simon co-founds APAX LAB). **Second source now with rich mineral→sensory content and no water concept** — flagged as an increasingly clear gap (open item, deferred under Focused).
- **Podium trio** captured: Nas (resistance) / Simon (selection) / Bavis (structure); sandwich ↔ clarity cross-linked as contrast (addition vs subtraction).
- New entities: [[brewing/entities/simon-gautherin]], [[brewing/entities/apax-lab]], [[brewing/entities/nextlevel-pulsar]].

Pages updated: brewing/sources/clarity-pyramid-simon-gautherin-cozyhouse (new), brewing/concepts/clarity-pyramid (new), brewing/entities/{simon-gautherin,apax-lab,nextlevel-pulsar} (new), brewing/concepts/sandwich-extraction (sibling cross-link), wiki/index.md.

---

## [2026-08-30] ingest | brewing | Nas Jaafar "Resistance" (WBrC champion) + Top-3 roundup (Cozy House) — completes the podium trio

Two more from the Cozy House WBrC series (Focused scope, matching the siblings). Source: SCA educator; flags: commercial bias, recipes/figures as-claimed (secondhand).

- **New concept [[brewing/concepts/flow-resistance]]** (from the champion piece) — the transferable pour-over lens: **flow is set by bed structure, not pour volume**; goal = **even, not minimal** resistance (input vs channel); flow/resistance/contact-time triad + 3 classroom failure cases; fix order (level bed → distribute pour → *then* grind); WDT/low-RPM fines control; hybrid steep-then-release recipe (UFO V3 on Switch, 15g/200g/92°C, 2:10). Linked to the espresso channeling/[[shared/astringency]] analogue.
- **New synthesis hub [[brewing/concepts/wbrc-2026-brewing-philosophies]]** (the author's roundup) — trio as one set: **uniformity** (Nas) / **subtraction** (Simon) / **addition** (Bavis); contest scoring = say-matches-cup; **3 trends** (hybrid extraction mainstream; fines management on stage; bean narrative = "why not how good"); **Geisha-homogenization → resource-competition** caveat (reinforces the wiki's green-selection focus).
- New entities: [[brewing/entities/nas-jaafar]], [[brewing/entities/ufo-v3]]. Trio cross-links added to [[brewing/concepts/sandwich-extraction]] + [[brewing/concepts/clarity-pyramid]]; [[brewing/overview]] gained a Competition Brewing section.
- Podium now complete in-wiki: Nas (resistance) / Simon (clarity) / Bavis (sandwich).

Pages updated: brewing/sources/{nas-jaafar-resistance-cozyhouse,wbrc-2026-top3-roundup-cozyhouse} (new), brewing/concepts/{flow-resistance,wbrc-2026-brewing-philosophies} (new), brewing/entities/{nas-jaafar,ufo-v3} (new), brewing/concepts/{sandwich-extraction,clarity-pyramid} (trio cross-links), brewing/overview (Competition Brewing section), wiki/index.md.

---

## [2026-08-31] ingest | brewing | Analyzing 300 PSDs for 24 espresso grinders (Gagné 2023)

High-credibility grind science (Jonathan Gagné analysing the Kaffeemacher/ZHAW 24-grinder, ~300-PSD dataset; Camsize X2). Fills a real gap and **grounds the "fines management" theme** that ran through the WBrC ingests.

- **New concept [[brewing/concepts/particle-size-distribution]]** — bimodal fines+nominal PSD; two orthogonal grinder metrics: **unimodality** (few fines, at 340μm reference) vs **uniformity** (few boulders); tri-lognormal model. Findings: conical < flat on avg; unimodality↔uniformity correlate (contra hearsay); RPM effect grinder-specific; burr **geometry > size**; blind-taste winners mid-range (PSD isn't everything).
- **Dial-in headline:** *dialling in espresso = dialling in the fines fraction* → fewer-fines grinders must grind **finer**; counter-intuitive **over-shooting** (unimodal pucks end up with more fines/g); geophysics permeability law fails for espresso.
- **Nuance flagged:** contradicts the blanket "low-RPM = fewer fines" practitioner claim (Nas) — Gagné finds RPM's PSD effect is grinder-specific. Cross-refs added on [[brewing/concepts/flow-resistance]], [[brewing/concepts/sandwich-extraction]], [[brewing/concepts/espresso-fundamentals]].
- New entities: [[brewing/entities/kaffeemacher]], [[brewing/entities/zhaw-coffee-excellence-center]]. Updated [[brewing/entities/jonathan-gagne]].

## [2026-08-31] fix | brewing | Rename Lance Hendrick → Lance Hedrick

Corrected the misspelled name (from the earlier source's metadata) to the real spelling **Lance Hedrick**, per user go-ahead. `git mv` both files (entities/lance-hedrick, sources/every-espresso-recipe-explained-hedrick); token-replaced Hendrick→Hedrick across all wiki pages **except this log** (append-only history retains the original spelling). All inbound wikilinks updated.

Pages updated: brewing/sources/gagne-grinder-psd-analysis-2023 (new), brewing/concepts/particle-size-distribution (new), brewing/entities/{kaffeemacher,zhaw-coffee-excellence-center} (new), brewing/entities/jonathan-gagne + {espresso-fundamentals,flow-resistance,sandwich-extraction} (cross-links), renamed lance-hedrick + every-espresso-recipe-explained-hedrick (+ all referrers), wiki/index.md.

---

## [2026-08-31] ingest | brewing | The Importance of Bed Depth (Gagné 2025)

High-credibility (Gagné). Bed depth was an uncovered fundamental parameter; ties into the just-added PSD/fines work and the existing astringency filtration model.

- **New concept [[brewing/concepts/bed-depth]]** — dripper **diameter = batch size** (idealized no-bypass: same time/TDS/EY, bigger batch; watch water-column drop rate, not total drip rate, across sizes) vs bed **depth = a fundamental flavor parameter**. Four mechanisms: Darcy resistance (→ coarser and/or longer), dilutes channel damage, better filtration of insolubles, altered bottom-of-bed extraction. Deeper = coarser + longer + **more forgiving**, more body/sweetness/complexity. Includes Gagné's depth→grind/time **cheat sheet** (1:17, EG-1; ≥20mm extrapolated toward Rao's deeper 20–23mm).
- **Filtration model of astringency (hypothesis)** — astringent long molecules adsorb onto particle/fines surfaces; trapping depends on bed depth/tortuosity + microscopic fluid velocity (pressure / water-column height). Deeper bed + gentle velocity → less astringency; explains narrow-water-column preference, cloudy/astringent espresso-machine filter coffee (except 0-bar Filter3), and shallow-bed finickiness. Flagged explicitly as unproven. Cross-linked to [[shared/astringency]].
- **Batch brew = just a deep bed** (best ~5–6 min); **espresso**: filtration matters less (high pressure), thicker puck → more crema.
- No new entities — **Pulsar Mini** folded into [[brewing/entities/nextlevel-pulsar]]; updated [[brewing/entities/jonathan-gagne]]; reciprocal links on [[brewing/concepts/particle-size-distribution]], [[brewing/concepts/espresso-fundamentals]].
- **Lint note (not fixed):** duplicate `scott-rao` entity exists in *both* brewing/ and roasting/ — worth reconciling.

Pages updated: brewing/sources/gagne-bed-depth-2025 (new), brewing/concepts/bed-depth (new), brewing/entities/{jonathan-gagne,nextlevel-pulsar}, shared/astringency, brewing/concepts/{particle-size-distribution,espresso-fundamentals} (cross-links), wiki/index.md.

---

## [2026-08-31] lint | brewing | Full lint + scott-rao reconciliation

Link-graph scan (all wiki pages) + brewing-domain review.

**Fixed:**
- **Duplicate `scott-rao` reconciled.** `roasting/entities/scott-rao` kept as the single cross-domain Rao entity; merged the brewing-specific facts (allongé 26–27% EY, filter TDS 1.35–1.4%, CGA/astringency, single-variable dialing) into it; `git rm` the `brewing/entities/scott-rao` duplicate; repointed 4 links (bed-depth, every-espresso-explained-hedrick, gagne-bed-depth-2025, lance-hedrick) → roasting; removed the duplicate index row and enriched the canonical one. Basename `scott-rao` is now unambiguous.
- **3 orphan personal logs re-linked** (previously only in the index): [[brewing/logs/reshad-ethiopia-jimma-natural]] + [[brewing/logs/gesha-village-oma-1931-natural-gold-label]] ← "Example brew logs" on [[brewing/concepts/neo-switch]]; [[brewing/logs/cokain-strawberry-chloris-blend]] ← [[brewing/entities/decent-espresso]]. Zero brewing orphans now.

**Clean:** no real broken links. The scan's 4 flags are non-issues — `dr296\|` is an escaped table-pipe (valid), and three `log →` links are append-only history (pre-rename lance-hendrick; long-deleted china-yunnan / disease-resistance) left untouched by design.

**Flagged, not fixed:**
- **Missing `water` concept (top priority).** Four+ sources now carry substantive mineral→sensory content with no home: Bavis 35 ppm low-mineral (sandwich), Simon 80 ppm MgSO₄:KCl:SiO₂≈3:2:1 (clarity-pyramid), Gagné's water-column/microscopic-velocity (bed-depth), SCA 50–175 ppm reference, APAX LAB. Recommend creating [[brewing/concepts/water]] and back-linking these.
- Minor un-homed mentions: **Tricolate** (valve/no-bypass brewer) and **WDT** (distribution tool) — candidate entity stubs, low priority.
- Contradictions already surfaced/cross-noted, no action: allongé EY (Rao 26–27% vs Hedrick ~22%); RPM→fines (Gagné grinder-specific vs Nas low-RPM).

Pages updated: roasting/entities/scott-rao (merged), brewing/concepts/neo-switch, brewing/entities/decent-espresso, wiki/index.md; deleted brewing/entities/scott-rao.

---

## [2026-09-01] update | brewing | Overview redesign → input→recipe decision framework

Full rewrite of [[brewing/overview]] (structural page), continuing the lint. The old page was two flat origin→parameter tables; it didn't enumerate the input set or show decision logic, and hadn't absorbed ~10 concepts added since 2026-08-02 (bed-depth, PSD, flow-resistance, clarity-pyramid, sandwich-extraction, espresso-shot-styles, flash-chill, etc.). Redesigned collaboratively with the user.

**Model (agreed):** invariants (origin/varietal/roast/processing) *place* the coffee, they aren't decisions → pick **goal/method** → position on a **flavour plane**:
- **X = balance**, driven by **extraction yield (EY)**: under→bright/sour · optimal→sweet · over→bitter. A real but *bounded* choice — always resolve to the juicy centre.
- **Y = clarity ↔ body**: a **filtration/texture** axis, independent of EY — the one genuine stylistic choice; default = honour the processing.
- **Z = strength (TDS)**: independent slider via ratio/bypass.
- **Key framing:** the BCC *is* the X×Z plane (EY×TDS); this page adds **Y**, the texture axis the BCC omits. Only X is EY.

**Steering rule:** set Y (structure: dripper/bed-depth/fines) first → dial X to balance (grind/temp/time) → set Z (ratio/bypass). The grind+agitation X↔Y coupling is the one to respect. §4 lever→axis table maps every recent concept to which axis it moves. The tool-intrinsic tangle (dripper/bed-depth/grind/batch) resolves as a dependency chain inside "set Y," not four peer branches.

**Structure:** §1 goal→method · §2 flavour plane (ASCII X–Y graphic + placement bullets) · §3 Z windows · §4 lever→axis table · §5 starting recipes (pour-over reframed to illustrative **origin×varietal×processing×roast** cells grounded in the varietal pages — Geisha/Kenya SL28/Ethiopia heirloom/Colombia/Brazil/Sumatra; espresso ratio roast-first) · §6 cold/iced · §7 BCC as backbone · §8 constants.

**Deliberate scope calls:** water **deferred** (HK water near-neutral — not a working variable, not flagged as a gap); starting-recipe brew numbers framed honestly as conventional starting points (sensory/varietal placement is the grounded part); 2×2 plane for now (3×3 with explicit centre band deferred).

Pages updated: brewing/overview (full rewrite).

---

## [2026-09-01] ingest | brewing | Harmony "Best Pourover Recipes 2026" (pro-recipe compilation)

Practitioner survey (~11 competition-level pros, Harmony/Ben Rowe); commercial bias flagged; recipes as-stated. Ingested primarily as a **field-test of the new [[brewing/overview]] model** — the independent recipes cluster on the same reasoning.

**Corroborations logged** (cross-linked into the existing pages): grind/PSD > temperature (Junchao, 600–800 µm) → [[brewing/concepts/particle-size-distribution]]; dose↔bed-depth (Ben: small dose = "7/10 intensity") → [[brewing/concepts/bed-depth]]; post-brew bypass (Sharon, 1:13.5 "too cramped") → [[brewing/concepts/bypass]]; roast→method (Gage Quinn: light = less soluble → percolation/hotter/wider), balance/"juicy" target, no-single-ideal, ratio-as-strength — noted in the source page vs the model.

**New concept [[brewing/concepts/flat-bottom-drippers]]** — the one real gap the source surfaced. Collated the whole family (Kalita/Orea/FLO/Pulsar/Stagg) on **one page** (user's call — avoid a page per make); defining trait = reduced/**no-bypass** (→ even extraction + higher EY), positioned as a Y→clarity/forgiving lever that nudges X (EY) up; variation axes = size / shower screen / valve. Added a §4 overview lever row.

**Disclosed bias (footnoted, per user):** flat-bottoms are under-covered because CK owns none (no first-hand logs); the "higher-EY / more-balanced" reputation is **forum hearsay** except Gagné's grounded Pulsar/bed-depth case; the plausible read (flat-bottom suits lightest roasts, over-extracts darker) is **provisional pending a hands-on experiment**. Water content in the source (APAX etc.) left **out of scope** (HK water near-neutral).

Pages updated: brewing/sources/harmony-pourover-recipes-2026 (new), brewing/concepts/flat-bottom-drippers (new), brewing/overview (§4 lever row), brewing/concepts/{particle-size-distribution,bed-depth,bypass} (corroboration), wiki/index.md.

---

## [2026-09-02] ingest | brewing | Pour-Over Variables: Blooming & Pours (Hedrick 2024)

Data-backed practitioner source (Lance Hedrick; controlled bloom-time experiment + reasoned pour comments). High-medium (real TDS/EY/blind-sensory, but n=3, single session, 2 coffees). Fills a real gap — the wiki had no blooming concept.

- **New concept [[brewing/concepts/blooming]]** (& pour structure).
  - **Bloom time = EY lever, with a twist:** 30 s→2 min raises EY/TDS/drawdown **monotonically** (+0.8–1.2 pp EY), but the **taste optimum is coffee-specific** — Peru (med-light) best at 30 s, Kenya (Nordic light, gassier) best at 2 min. Rule: gassier/lighter/fresher → longer bloom.
  - **"High and dry"** off-gassing mechanism; and the counter-intuitive result that Kenya's 2 min (highest EY) had the **most acidity** — even extraction reads as clean acidity. Bloom is thus both an X and a Y lever.
  - **Fewer pours = cleaner** (user-flagged; reasoned, no data): the coffee bed is a filter; each pour ejects more fines + clogs pores + lengthens drawdown → muddier/astringent. → minimise pours, dial the bloom.
  - **Pour turbulence** (laminar/turbulent/droplet) as an agitation-depth lever; S-bloom/decaf/aging/dark-roast special cases; grinder-agnostic recipe rationale (fines vary → grind-specific recipes don't transfer).
- **Cross-links:** overview §4 gained **Bloom** + **Fewer pours** lever rows (and a turbulent/laminar note); reciprocal notes on [[brewing/concepts/particle-size-distribution]], [[shared/astringency]] (bed-filtration), [[brewing/concepts/flat-bottom-drippers]] (Hedrick's Kalita-clog/V60-preference caveats); [[brewing/entities/lance-hedrick]] updated. Cites Samo Smrke ([[brewing/entities/zhaw-coffee-excellence-center|ZHAW]]) on bed-swelling = CO₂ release.
- No new entities.

Pages updated: brewing/sources/hedrick-blooming-pours-2024 (new), brewing/concepts/blooming (new), brewing/overview (§4 levers), brewing/entities/lance-hedrick, brewing/concepts/particle-size-distribution, shared/astringency, brewing/concepts/flat-bottom-drippers, wiki/index.md.

---

## [2026-09-02] lint | brewing | Overview §4 lever table — de-conflate immersion / cold tail

User-flagged overlap. Two defects in the lever table: (1) **redundancy** — immersion→body was listed both in "Neo Switch / Graycano" and again in "Immersion / cold tail (Switch)"; (2) **conflation** — immersion (a contact-*mode* lever, needs a valve/vessel) and cold tail (a *temperature* finish lever, works on plain V60) are orthogonal mechanisms wrongly merged. Also, Graycano is a heat-sink *percolation* cone, not immersion.

Fix — split into three independent levers:
- **Immersion / steep** (Switch closed, Clever) — Y→body, rounds X.
- **Graycano** (heat-sink cone) — Y→body via sustained heat (percolation, not immersion).
- **Cold tail / dual-temp finish (~65–70 °C)** — an **independent** X/finish lever (tames bitter/astringent tail → sweeter finish), explicitly noted as not requiring immersion (a cooler final pour works on V60; Kasuya devil combines them but they're separable). Cousin of the existing front-discard/tail-cut lever (remove the tail vs gently extract it).

Pages updated: brewing/overview (§4 table).

---

## [2026-09-02] ingest | brewing | The Role of Fines in Espresso Extraction Dynamics (Smrke et al. 2024)

**Peer-reviewed** (Sci. Rep./Nature; Smrke, Eiermann, Yeretzian @ ZHAW — same lab/Camsizer as Gagné's PSD dataset). Highest-credibility brewing source to date. No new pages/entities — it strengthens & refines existing concepts.

- **Headline:** isolate fines by spiking sieved fines → sweep **share of fines (Q₁₀₀µm)**. Fines govern **bed permeability → flow → extraction time**, and act **ONLY** via permeability — spiking fines into a coarse grind gives the *same* EY/time curve as grinding finer; surface-area effect on efficiency is **marginal**. PLSR on whole PSDs confirms (+coeff <150µm, −coeff >250µm). Predictive models (time from Q₁₀₀µm+X50; EY from +time). Single median insufficient.
- **Myth-refining:** **no sensory penalty** from higher fines (+1–2 g among the best) — the "fines = muddy/astringent" belief is a *filter* suspended-particle claim ([[shared/astringency]]), not proven for 9-bar espresso.
- **Aroma:** aroma-vs-EY **non-linear** (4 VOC groups); extraction ≠ pure diffusion (losses via grinding desorption + **CO₂ degassing/crema** + post-extraction evaporation). **Turbo (fast/low-yield) retains fruity VOCs** → aroma-side rationale for turbo (cites Cameron 2020 = [[brewing/entities/christopher-hendon|Hendon]]). Peak sensory is coffee-specific (this coffee ~30s/19–20% EY, not turbo).
- **Caveats:** single coffee/roast/grinder; fines *added* not native; sensory = one Q-grader hedonic (authors flag non-double-blind).

Updated: [[brewing/concepts/particle-size-distribution]] (peer-reviewed backbone: Q₁₀₀µm, fines→permeability-not-EY, no-penalty nuance, models; src_count 1→2), [[brewing/concepts/espresso-fundamentals]] (turbo→fruity aroma retention, non-linear aroma; src_count 4→5), [[brewing/concepts/blooming]] (CO₂ off-gassing = aroma-loss channel; src_count 1→2), [[brewing/entities/zhaw-coffee-excellence-center]] (Smrke/Yeretzian paper), wiki/index.md.

Pages updated: brewing/sources/smrke-fines-espresso-2024 (new), brewing/concepts/{particle-size-distribution,espresso-fundamentals,blooming}, brewing/entities/zhaw-coffee-excellence-center, wiki/index.md.

---

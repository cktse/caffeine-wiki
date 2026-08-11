---
title: "Arabica Variety Taxonomy (WCR)"
domain: varietals
tags: [wcr, catalog, reference, arabica, varieties, genetics, clr, quality, yield]
source_count: 4
last_updated: 2026-08-01
---

# WCR Variety Catalog — Reference

## What It Is

The World Coffee Research Arabica Varieties Catalog is an open-access database of ~70 Arabica varieties (plus one Robusta rootstock) across 18 countries. It tracks 13 agronomic and quality variables per variety, based on field trials at 23 sites in 15 countries. Updated September 2025.

Live database: varieties.worldcoffeeresearch.org | Source: [[sources/wcr-arabica-varieties-catalog-2025]]

## Variable Schema

| Variable | What it means | Reference benchmarks |
|---|---|---|
| **Stature** | Plant size | Dwarf/Compact vs. Tall |
| **Leaf tip color** | Color of new growth tips | Green vs. Bronze (visual ID) |
| **Bean size** | Physical bean size | Average=Caturra; Large=SL28; Very Large=Maragogipe |
| **Yield potential** | Expected fruit volume | Low/Medium=Bourbon, Caturra, K7; High/Very High=introgressed, F1 |
| **Quality potential at high altitude** | Cup quality at optimal altitude | Scale: Very Low → Exceptional |
| **Optimal altitude** | Altitude for best agronomic + quality performance | Latitude-adjusted (see catalog) |
| **Coffee leaf rust (CLR)** | Resistance to *Hemileia vastatrix* | Highly resistant / Intermediate / Low (susceptible) |
| **Nematode** | Root nematode resistance | Resistant / Tolerant / Susceptible |
| **Coffee berry disease (CBD)** | Resistance to *Colletotrichum kahawe* | Resistant / Tolerant / Susceptible |
| **Year of first production** | How soon the tree produces | Year 2–4 |
| **Nutrition requirement** | Fertilizer needs | Low → Very High |
| **Ripening of fruit** | When cherries mature in harvest season | Early / Average / Late |
| **Cherry to green bean outturn** | Bean-to-fruit size ratio | Average=Caturra; High=SL28 |

**Note on CLR resistance**: "A variety that is resistant to a disease today may not be resistant tomorrow." Resistance is race-specific and geographically variable. India has the world's highest concentration of CLR races.

**Quality potential — the five tiers**: WCR grades "quality potential at high altitude" as **very low → low → good → very good → exceptional**. WCR "exceptional" = **Casiopea, Geisha, Mibirizi, Pacamara, SL28, SL34**.

> ⚠️ **Credibility caveat (Sera et al. 2025):** these Brazilian researchers note that "the basis used by [WCR] to define the drinking potential of these cultivars is **unclear**," and observe that Typica/Bourbon derivatives routinely produce high-quality coffee even when *not* rated "exceptional." Treat the quality tier as a coarse relative signal, not an absolute cup-score predictor — consistent with the Open Question below. Also note the tiers are **origin-blind**: none of WCR's six "exceptional" cultivars are even registered for cultivation in Brazil, yet Brazil produces 90+ COE lots from "good"-rated Catuaí and from introgressed cultivars WCR does not rate highly.

## Genetic Classification System

| Group | Description | Key varieties |
|---|---|---|
| Bourbon-Typica (Bourbon related) | Bourbon genetic background | Bourbon, Caturra, Pacas, SL28, K7, Villa Sarchi |
| Bourbon-Typica (Typica related) | Typica genetic background | Typica, Maragogipe, Pache, SL34, SL14 |
| Bourbon-Typica (Typica and Bourbon related) | Mixed Bourbon+Typica | Catuai, Mundo Novo, Pacamara |
| Ethiopian landrace | Wild Ethiopian origin | Geisha (Panama), Java, AB3 |
| Introgressed (Catimor related) | Timor Hybrid × Caturra family | Lempira, Costa Rica 95, IHCAFE 90, Castillo family |
| Introgressed (Sarchimor related) | Timor Hybrid × Villa Sarchi family | IAPAR 59, Marsellesa, T5296, Parainema |
| Introgressed (Other) | Other robusta × arabica crosses | Batian, Catigua MG2, RAB C15 |
| F1 hybrid (introgressed) | F1 with introgressed parent | Centroamericano, Milenio, Ruiru 11 |
| F1 hybrid (not introgressed) | F1 from two pure arabica parents | Casiopea, EC15, H3 |

## Key Variety Quick-Reference

Varieties most relevant to this wiki's existing content:

| Variety | Genetic group | Quality at altitude | CLR | Notes |
|---|---|---|---|---|
| **Bourbon** | Bourbon related | Very Good | Susceptible | Year 4; medium yield; foundation of most quality coffee |
| **Caturra** | Bourbon related | Good | Susceptible | Natural Bourbon mutation; compact; high-density planting; Year 3 |
| **Catuai** | Typica + Bourbon | Good | Susceptible | Mundo Novo × Caturra; compact; high-density; Year 3 |
| **Typica** | Typica related | Very Good | Susceptible | Year 4; low yield; aliases: Criollo, Arábigo, Blue Mountain, Sumatra |
| **SL28** | **Bourbon related** | **Exceptional** | Susceptible | Drought tolerant; bold beans; fine liquor; Kenya/Malawi/Uganda |
| **SL34** | **Typica related** | **Exceptional** | Susceptible | ⚠️ NOT Bourbon — Typica genetic background; high altitude, high rainfall; Kenya |
| **K7** | Bourbon related | Good | **Intermediate** (partial, some CLR races) | Natural partial CLR resistance (no Timor Hybrid); low altitude; French Mission → Lengetet Estate selection; Kenya |
| **Geisha (Panama)** | Ethiopian landrace | **Exceptional** | Intermediate | Low yield; Year 4; distinct genetics; "Geisha" name often misapplied |
| **Pacamara** | Typica + Bourbon | **Exceptional** | Susceptible | Pacas × Maragogipe; very large bean; not uniform/stable |
| **Maragogipe** | Typica related | Very Good | Susceptible | Natural Typica mutation; very large bean; low yield; superseded by Pacamara |
| **Pacas** | Bourbon related | Good | Susceptible | Natural Bourbon mutation; El Salvador parent of Pacamara |
| **Villa Sarchi** | Bourbon related | Good | Susceptible | Natural Bourbon mutation; Costa Rica; parent of Sarchimors |
| **Mundo Novo** | Typica + Bourbon | Good | Susceptible | Direct Typica × Bourbon cross; parent of Catuai |
| **Pache** | **Typica related** | Good | Susceptible | Natural Typica mutation; compact; large bean; Guatemala; best >1,200m |
| **Lempira** | Catimor related | Low | **Confirmed susceptible** | Honduras; CLR resistance failed; Timor Hybrid 832/1 × Caturra |
| **Costa Rica 95** | Catimor related | Low | **Confirmed susceptible** | CLR resistance failed in Costa Rica; same lineage as Lempira |
| **IHCAFE 90** | Catimor related | Very Low | **Confirmed susceptible** | Honduras; CLR resistance failed; same lineage |

## CLR — Three Confirmed Catimor Failures

All three confirmed-susceptible varieties share the same parentage: **Timor Hybrid 832/1 × Caturra**:
- Lempira → confirmed susceptible in Honduras
- Costa Rica 95 → confirmed susceptible in Costa Rica and possibly elsewhere in Central America
- IHCAFE 90 → confirmed susceptible in Honduras

This means the 832/1 Timor Hybrid resistance is the specific resistance that is breaking down in Central America. Catimors using 832/2 (Sarchimor lineage) may have a different resistance profile — but the catalog warns all resistance can fail.

## F1 Hybrid Propagation Rule

Every F1 hybrid must be clonally propagated — seeds will not breed true (segregation). This applies to: Casiopea, Centroamericano, EC15, Esperanza, Evaluna, H3, Milenio, Mundo Maya, Nayarita, Ruiru 11, Starmaya.

## Notable Absences

- **Pink Bourbon**: Not in the 2025 catalog. WCR requires varieties to be distinct, uniform, and stable. Pink Bourbon fails the uniform/stable criteria — its uncertain genetic origin excludes it. This confirms the 1Zpresso source's note about uncertain genetics.
- **Castillo**: Not in catalog (covered by Cenicafé/FNC; Catimor 129 is the closest catalog entry, bred from the same Colombian Catimor breeding line by Cenicafé).

## Montagnon et al. (2021) Genetic Cluster Nuances

The WCR 2025 catalog and the Montagnon 2021 SSR study use different methods and resolve genetics at different levels. Key nuances where the two sources create useful texture:

- **K-7**: WCR 2025 classifies as "Bourbon related." Montagnon 2021 places K-7 (and K-758) in the **SL-17 cluster** — alongside Ethiopian accessions and *no Yemen samples*. Either K-7 represents a lineage that bypassed Yemen (Route 3 escapee), or the Yemen SL-17 lineage is now absent from the surveyed Qima population. **Resolution**: retain WCR "Bourbon related" as primary classification; note SL-17 placement as a refinement.
- **SL-34**: WCR 2025 says "Typica related." Montagnon 2021 places SL-34 in the **Yemen SL-34 cluster** — a distinct Yemen subpopulation, separate from the Yemen Typica-Bourbon cluster where Typica and Bourbon sit. These are compatible: SL-34 transited Yemen but from a different genetic stock than Typica. The WCR "Typica-related" operates at a coarser resolution.
- **SL-28**: Montagnon 2021 confirms SL-28 in the **Yemen Typica-Bourbon cluster** (same cluster as Typica and Bourbon, and same genetic fingerprint as Coorg). Consistent with WCR "Bourbon related" classification.
- **Chiroso** (now sourced; see [[concepts/chiroso]]): Three Colombian endemic varieties in Urrao, Antioquia — **Caturra Chiroso (CCH), Bourbon Chiroso (BCH), and Chiroso (CHCH)** — all in the Ethiopian Only cluster; none are genetically related to Caturra or Bourbon despite the phenotype-based names. Chica-Acosta et al. 2024 (cpDNA) independently corroborates Montagnon 2021 (nuclear SSR) using a completely different marker system. Origin narrowed to **Eastern Ethiopia (Berbere/Bale Mountains region)** — distinct from Geisha's southwestern Ethiopian origin (Kaffa/Bench Maji). CCH and BCH have a unique cpDNA haplotype and an exclusive diagnostic SNP at position 47,413 bp (intergenic spacer trnT(UGU)-trnL(UAA)) — potential authentication marker. CHCH's cpDNA haplotype is shared with Bourbon and Caturra despite its Ethiopian Only nuclear classification — unresolved. Cultivation: 1,950–2,100m; up to $45/pound; ~1 kg/tree/year; competition recognition since 2014. **Not yet in WCR catalog.**
- **Geisha**: WCR 2025 classifies as "Ethiopian landrace." Montagnon 2021 confirms in the **Ethiopian Only cluster** (CATIE T.02722). Consistent.

See [[sources/yemen-genetic-diversity-montagnon-2021]] and [[concepts/arabica-history]] for the full four-route dispersal framework.

## Key Sources

- [[sources/wcr-arabica-varieties-catalog-2025]] — the catalog itself
- [[sources/yemen-genetic-diversity-montagnon-2021]] — Montagnon et al. 2021; five-cluster SSR analysis; nuances on K-7, SL-34, SL-28, Geisha; first places Chiroso in Ethiopian Only cluster; *Qima Coffee funder — note for New-Yemen claims*
- [[sources/chiroso-chloroplast-chica-acosta-2024]] — Chica-Acosta et al. 2024; cpDNA confirmation of all three Chiroso varieties; Eastern Ethiopian (Berbere) origin; SNP authentication markers; independent corroboration of Montagnon 2021
- [[sources/brazil-specialty-coffee-sera-2025]] — names the WCR five-tier quality scale; critiques its unclear basis; Brazilian RNC-vs-WCR catalog coverage (only 8 overlap)

## Related Concepts

- [[concepts/bourbon]] — Bourbon lineage varieties (corrected SL34 note)
- [[concepts/typica]] — Typica lineage varieties
- [[concepts/introgressed-varieties]] — Catimor/Sarchimor varieties with CLR resistance
- [[concepts/coffee-leaf-rust]] — CLR resistance breakdown; confirmed varieties
- [[concepts/ethiopian-landrace]] — Geisha/Java/AB3 in the catalog
- [[concepts/f1-hybrids]] — clonal propagation requirement

## Open Questions

- How does the catalog rank varieties specifically for specialty cup quality vs. general agronomic performance? The "Quality potential at high altitude" variable is relative — no absolute score.
- No Pink Bourbon in catalog — what does WCR say informally about its genetics? Some sources suggest it may be an Ethiopian landrace rather than a Bourbon variant.
- SL34 is Typica-related — does this mean the "Kenya cup" (blackcurrant, bright acidity) is a Typica expression at altitude, not a Bourbon one? The two primary Kenyan varieties now have different lineages.

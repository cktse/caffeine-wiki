# Tooling Specifications

Design specifications for project-specific tools and scripts. Each tool is a
self-contained numbered section — purpose, workflow, data model, behavior, and
limitations — written for both human maintainers and LLM agents.

Conventions:
- Python 3; run locally; no external services or network calls.
- Operate on local files only; write nothing outside the project folder.
- Keep first-party (measured) data and third-party ("as claimed") data distinct
  in all outputs — see `CLAUDE.md` → Sourcing Discipline.
- Keep things simple, do not over-engineer
- Use existing tools/libraries as much as possible
- Test-driven design, includes automated tests covering positive and negative cases where appropriate, exercising the code being tested as extensive as possible (e.g. a good pattern is to curate a set of representative test cases as input files to generate expected baseline for comparison)
- Avoid hardcoding, use CLI argv where possible (pre-defined defaults are OK) and avoid unobvious coupling in the logic
- Data minimalization principle: clean data lineage, avoid storing duplicative copies of data, instead store data keys and look up the authoritative data source
- Flag technical debt: trade off to the design and/or code base say in flavor of preserving backward compatibility must be subject to careful deliberation
- Modular design, group related functions together into logical modules, minimize coupling between modules, and keep dependencies unidirectional.

---

## 1. Bean Conqueror Importer — `bc_to_md.py`

### 1.1 Purpose

Convert selected records from a Bean Conqueror (BC) JSON export into per-bean
Markdown documents that seed `personal_log` wiki pages. The tool extracts
structured brew data and known bean attributes; a human enriches each document
before it is ingested into the wiki.

### 1.2 Scope

- **In scope:** roasted beans and their brews (→ `wiki/brewing/logs/`).
- **Out of scope (initial):** green beans / roast logs; roaster-website scraping;
  automated wiki ingestion.

### 1.3 Workflow

1. **`manifest`** — list all beans; the operator selects which to materialize.
2. **`generate`** — produce a baseline Markdown file per selected bean.
3. **Enrich (manual)** — add bean identity (from the roaster URL), brew technique
   (dual-temp, flow/pour sequence), and sensory notes.
4. **Ingest** — the enriched Markdown becomes a raw source document and is
   imported into the wiki as a `personal_log`.
5. **`append`** — on a later export, pull only new brews into the enriched
   document; re-ingest. Steps 2–5 repeat as brews accumulate.

### 1.4 Input data model

The BC export is a JSON object of top-level arrays. Relevant entities and linkage:

| Array | Role | Key / link |
|---|---|---|
| `BEANS` | roasted bean records | `config.uuid` |
| `BREWS` | individual brews | `config.uuid`; `bean` → `BEANS.config.uuid` |
| `PREPARATION` | brew methods (V60, Neo Switch, Espresso…) | `config.uuid`; `BREWS.method_of_preparation` |
| `MILL` | grinders | `config.uuid`; `BREWS.mill` |

Export limitations that drive the manual-enrichment step:
- `BEANS.bean_information` is typically empty; origin/variety/process/farm live in
  the free-text `name` and the roaster `url`.
- `BEANS.roast` is usually `UNKNOWN`; Agtron is stored ad hoc in `BEANS.note`
  (e.g. "Ag 77.2").
- `BREWS` record a single `brew_temperature` and no valve/flow/pour sequence;
  dual-temp and technique detail are absent.
- Many brews lack `tds` and `brew_beverage_quantity` (no extraction yield).

### 1.5 Modes

**`manifest`** — Input: BC JSON. Output: a selection table, one row per bean:
`name · roaster · roast date · #brews · #brews-with-TDS · roast type`.

**`generate <selector>`** — Input: BC JSON + one or more bean ids/names. Output:
one Markdown file per bean. Content:
- Frontmatter: the dedup ledger (§1.6), BC-derived attributes, best-effort
  `agtron_whole` parsed from `note`, and blank identity fields with fill hints.
- Body: brew entries grouped by preparation method (pour-over vs espresso column
  sets). Emitted columns are **raw measured values only** — Ratio and EY are omitted
  (recomputed at ingestion) — plus a blank **Notes** column for manual additions.
  Units are space-free (`15g`, `92C`) for easy manual editing.

**`append <md-path>`** — Input: an enriched Markdown file + BC JSON. Behavior:
append only `BREWS(bc_bean_id) − bc_brews` into the correct method section
(creating it if absent) and extend `bc_brews`. Existing content — manual
enrichments and prior brew entries — is never modified.

### 1.6 Dedup ledger

Idempotent append relies on UUIDs recorded in frontmatter:

```yaml
bc_bean_id: <BEANS.config.uuid>
bc_brews: [<BREWS.config.uuid>, …]
```

The ledger is the single source of truth for "already materialized," and is robust
to manual edits of any rendered content.

### 1.7 Field mapping

Bean → frontmatter:

| BC field | MD field | Notes |
|---|---|---|
| `name` | `title` | raw label name; **not** parsed into identity |
| `roaster` | `roaster` | |
| `roastingDate` | `roasted_on` | date only |
| `bean_roasting_type` | roast-target note | FILTER / ESPRESSO |
| `note` | `agtron_whole` | best-effort regex (`Ag …`) |
| `weight`, `cost`, `url` | same | |
| `beanMix` | blend flag | BLEND vs SINGLE_ORIGIN |
| — | origin, region, farm, producer, varietals, processing, elevation | blank; manual |

Brew → row (grouped by method):

| BC field | MD column | Notes |
|---|---|---|
| `config.unix_timestamp` | date | |
| `mill` + `grind_size` | Grind | mill name + dial |
| `grind_weight` | Dose | |
| `brew_quantity` | Water | |
| `brew_beverage_quantity` | Beverage | if > 0 |
| `brew_temperature` | Temp | single value, formatted `92C`; dual-temp added manually |
| `brew_time` | Time | seconds → mm:ss |
| `tds` | TDS | if > 0 |
| — | Notes | blank column for manual technique / tasting notes |

### 1.8 Provenance & guardrails

- BC-derived brew data is first-party (measured) and may be asserted directly.
- Identity fields are filled manually from the roaster URL and are **as claimed**;
  they are never auto-parsed from the bean name (avoids laundering an incorrect
  origin/variety).
- The generated template separates measured data from claimed data so enrichment
  lands in the correct provenance tier.

### 1.9 Architecture & dependencies

Modules (unidirectional dependencies; each independently testable):
- `load` — parse the export; resolve UUID joins (brew → bean, → preparation, → mill).
- `map` — BC fields → schema fields; unit conversions (seconds → mm:ss).
- `render` — Markdown emission; brew tables grouped by preparation method.
- `ledger` — read/extend the `bc_bean_id` / `bc_brews` frontmatter ledger; append dedup.
- `cli` — thin argument layer (mode dispatch, paths, selectors) over the above.

Dependency flow: `cli → {load, map, render, ledger}`; `render` and `ledger` consume
only `map`'s output types.

Dependencies: Python 3 standard library (`json`, `argparse`, `re`) + **yaml12** for
frontmatter read/write.
- Install: `pip install py-yaml12`. Import: `from yaml12 import parse_yaml, format_yaml`.
- Rationale (correctness + "use existing libraries"): yaml12 implements **YAML 1.2**,
  which does not implicitly coerce dates, `no`/`off`/`yes`, or `1:2`-style scalars.
  Frontmatter such as `roasted_on: 2026-07-20` and `date_ingested` stays a **string**,
  avoiding the date-object coercion that YAML-1.1 parsers (e.g. PyYAML) impose on the
  ledger round-trip.

### 1.10 Testing

Golden-file (baseline-comparison) tests, per the test-driven tenet:
- `tests/fixtures/` holds small representative **input** BC-export slices and their
  **expected** Markdown outputs; each run diffs actual vs expected.
- Coverage:
  - *Positive:* a rich pour-over brew (all fields incl. TDS/beverage);
    an espresso brew (espresso column set).
  - *Negative / edge:* brew missing `tds`/`brew_beverage_quantity` (blank cells); `BLEND`
    bean; empty `bean_information` (identity fields blank); Agtron absent from `note`.
  - *Append dedup:* baseline MD + an export with one extra brew → exactly that row
    appended, `bc_brews` extended, pre-existing content (incl. a simulated manual edit)
    unchanged.
- Fixtures are regenerated deliberately only when the mapping/format changes — a
  reviewed event, not an incidental diff.

### 1.11 Deliberated tradeoffs

- **Materialization duplicates measured values (accepted).** Strict data-minimalization
  argues against copying BC values into the MD, but a wiki source must be self-contained
  and cannot depend on a live export. Reconciliation: the BC export remains the single
  authoritative source (no second cached copy); dedup uses **UUID keys**, never value
  matching; no datum is stored twice *within* an MD. The MD is an explicit point-in-time
  snapshot.
- **Append-only, no full regeneration (accepted).** Preserves manual enrichment at the
  cost of not reconciling BC-side edits to already-materialized brews; those are handled
  manually. Revisit only if editing historical brews in BC becomes common.

### 1.12 Limitations / future work

- No green-bean / roast-log support (planned).
- No roaster-URL scraping; identity enrichment is manual.
- Location: script + tests live in `tools/` (tracked); generated MD outputs go to
  `scratchpad/bc_out/` (gitignored) until enriched and ingested.

Usage: `python3 tools/bc_to_md.py [--export PATH] {manifest | generate [--bean SEL …]
[--out DIR] | append --md PATH}`. Tests: `python3 tools/tests/test_bc_to_md.py`.

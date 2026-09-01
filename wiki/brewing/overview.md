# Coffee Brewing — Overview

A decision framework: turn a coffee's fixed properties into a recipe without drowning in variables. Brewing has ~12 knobs, but they collapse into a small model.

**Four moves:**
1. **Read the invariants** off the bag — origin/varietal, **roast**, **processing**. Fixed; they *place* the coffee, they aren't decisions.
2. **Pick the goal** (beverage) → selects the **method** (§1).
3. **Place & target on the flavour plane** (§2) — **X** balance, **Y** expression, **Z** strength.
4. **Steer** (§4) — set **Y** first → dial **X** to balance → set **Z**.

---

## 1 · Goal → Method

The beverage picks the method family, its parameter ranges, and its tools. The flavour plane (§2) works the same for all.

- **Hot filter** — full pour-over playground (drippers, bed depth, technique).
- **Espresso** — high-Z method (TDS ~8–12%); ratio set by roast; crema. See [[concepts/espresso-fundamentals]].
- **Americano** — pull espresso, then slide **Z** down with hot water (extreme bypass).
- **Cold brew** — immersion, low-temp; inherently low-acid/low-bitter. See [[concepts/cold-brew]].
- **Flash-chill iced** — brew hot onto ice; keeps hot-brew aromatics. See [[concepts/flash-chill-iced-coffee]].

---

## 2 · Place your coffee — the flavour plane

Read the coffee's **home** on the plane from its invariants, choose a **bounded target**, and the home→target delta tells you which levers to move.

```
                    Y↑ CLARITY  (washed · floral · terroir-driven)
                                │
        bright + clean          │          sweet + clean
        Ethiopia/Kenya washed   │          Colombia/Guatemala washed
        · light roast           │          · medium roast
        → V60 / Origami         │          → V60 / Origami
        → push EY, elegant Z    │          → standard Z  (easy balance)
                                │
   BRIGHT ──────────────────────┼────────────────────── SWEET / ROUND   X
   (light roast · Kenyan/Gesha) │          (dark roast · Brazil/natural)
                                │
        bright + bodied         │          sweet + bodied
        Ethiopia natural        │          natural / anaerobic dark,
        · light roast           │          Sumatra wet-hulled
        → Neo Switch / Graycano │          → immersion / Graycano
        → add body, mid Z       │          → intense Z, pull EY off bitter
                                │
                    Y↓ BODY  (natural · anaerobic · wet-hulled)
```

**The three axes:**
- **X — balance**, moved by **extraction yield (EY)**: under-extract → bright/sour · optimal → sweet · over → bitter. Roast + varietal set where you *start*; brewing walks you toward the centre.
- **Y — clarity ↔ body**: a **filtration / texture** dimension, physically **independent of EY** (it's about what's filtered vs suspended, not how much is extracted).
- **Z — strength (TDS)**: an independent slider, via ratio (§3).

> **Not the Brewing Control Chart.** The [[concepts/brewing-control-chart|BCC]] is **X × Z** (EY × TDS). This plane is **X × Y** (EY × texture) — same X, plus the texture axis the BCC omits. **Only X is EY**; Y and Z are separate dimensions.

**X — Balance** (bright ↔ sweet/round). *Always aim near the juicy centre.*
- Primary: **roast** — light → bright *(risk: sour/thin)* · medium → centred · dark → sweet/heavy *(risk: bitter/flat)*.
- Modifiers: varietal (Kenyan/Gesha → brighter; Brazil/Bourbon/Sumatra → rounder); processing (washed → brighter; honey/natural → sweeter).
- Lean bright or sweet only inside the balance band — past it, sharp sourness or flat bitterness.

**Y — Expression** (clarity ↔ body). *The real choice; default = honour the bean.*
- Primary: **processing** — washed/floral → clarity · honey → mid · natural/anaerobic/wet-hulled → body.
- Modifiers: roast (darker → more body); varietal (Gesha/clean washed → clarity; heavy heirlooms → body); altitude (higher → more clarity + acidity).
- Nudge only if the cup reads thin (add body) or muddy (add clarity).

---

## 3 · Strength — Z (TDS, via ratio)

Independent of X and Y. Set by dry coffee:water ratio; fine-tune with [[concepts/bypass|bypass]] (drops TDS without changing EY).

| Z target | TDS | Ratio | Natural pairing |
|---|---|---|---|
| **Elegant** | ~1.20% | 1:17–1:18 | clarity |
| **Standard** | ~1.35% | 1:15–1:16 | balanced |
| **Intense** | ~1.50%+ | 1:13–1:14 | body |

Clarity↔elegant and body↔intense (a Y↔Z pairing) is the default, not a rule — break it with bypass.

---

## 4 · Steer — levers → axis

Order: **set Y first** (structure; low cross-talk, set once) → **dial X to balance** (grind/temp/time) → **set Z** (ratio/bypass). The one coupling to respect: **grind and agitation move both X and Y**, so lock structure before chasing extraction with grind.

*X column = effect on balance (brighter ↔ sweeter, over-extract → bitter). Y column = effect on clarity ↔ body. "—" = no meaningful effect.*

| Lever (pushed this way) | X — balance | Y — clarity ↔ body | Note |
|---|---|---|---|
| V60 / Origami / fast filter | — | → clarity | percolation |
| Neo Switch / Graycano | — | → body | immersion / heat-sink |
| [[concepts/bed-depth\|Bed depth]] deeper | slightly sweeter | → body + forgiving | pair with coarser grind |
| Fewer fines / WDT / unimodal grinder | — | → clarity | grinder is a real lever ([[concepts/particle-size-distribution\|PSD]]) |
| Front-discard / tail-cut | trims sharp front / bitter tail | → clarity | selection (Simon) |
| Grind finer | more EY → sweeter (over: bitter) | → body (fines) + astringency risk | set Y first; grind then does mostly X |
| Immersion / cold tail (Switch) | rounds → sweeter | → body | Kasuya devil / hybrid |
| Fast filter + finer grind | more EY → sweeter | → clarity | sweetness without astringency |
| Water hotter | more EY → sweeter | — | scale by roast (93/88/83 °C) |
| Longer contact / more agitation | more EY → sweeter | agitation muddies clarity | handle with care |
| Ratio tighter | — | — | strength **Z↑** — see §3 |
| Bypass | — | — | strength **Z↓**; decouples from X |

The 2026 WBrC top three are pure cases: **even resistance** (X), **selective extraction** (Y clarity), **particle stratification** (Y body). See [[concepts/wbrc-2026-brewing-philosophies]].

---

## 5 · Starting recipes

Baselines for your cell — then steer per §4. **Temp by roast (Kasuya):** light ~93 · medium ~88 · dark ~83 °C. Grind pairs with dripper + [[concepts/bed-depth|bed depth]] (deeper → coarser); it's a dial-in output, not a top-level choice.

### Pour-over

**Origin × varietal × processing × roast** — origin alone is too coarse (Ethiopia *Geisha washed* and Ethiopia *Harrar natural* land in opposite cells). Below are illustrative combos, not an exhaustive matrix; sensory placement is grounded in the linked pages, brew numbers are conventional starting points to steer from (§4).

| Illustrative coffee | Cell (X · Y) | Dripper | Ratio (Z) | Grind | Key move |
|---|---|---|---|---|---|
| [[varietals/concepts/geisha\|Geisha]] · Panama/Eth · washed · light | bright · clarity | V60 / Origami | 1:16–17 (elegant) | med-fine | preserve jasmine/bergamot/tea; light-bodied varietal → guard watery (a little bed depth), don't over-extract |
| [[varietals/entities/kenya\|Kenya SL28/34]] · washed · light-med | bright · clarity | V60 / Origami | 1:15–16 | med-fine | blackcurrant + high acidity; push EY so sweetness buffers it |
| [[varietals/entities/ethiopia\|Ethiopia heirloom]] · natural · light | bright→sweet · body | Neo Switch / Graycano | 1:15–16 | medium | fruit-forward; immersion/heat-sink adds body + tames ferment |
| [[varietals/entities/colombia\|Colombia Bourbon/Caturra]] · washed · medium | centred · clarity-mid | V60 / Origami | 1:15–16 (standard) | med-fine | easy-balance cell; caramel/chocolate, round |
| [[varietals/entities/brazil\|Brazil Mundo Novo/Catuaí]] · natural · medium | sweet · body | Origami / Neo Switch | 1:14–15 | medium | nutty-chocolate, low acid; also a milk/espresso base |
| [[varietals/entities/indonesia\|Sumatra]] · [[shared/wet-hulling\|wet-hulled]] · medium | sweet/round · deep body | Graycano / Neo Switch | 1:14–16 (intense) | med-coarse | earthy/spice, heavy body; hotter side for extraction |

Method detail: [[concepts/46-method]] · [[concepts/dialing-in]] · [[concepts/comandante-grind-size]].

### Espresso

Ratio is set by **roast** (mass-loss), not origin — the cleaner axis ([[concepts/espresso-fundamentals]]):

| Roast | Ratio (in:out) | Note |
|---|---|---|
| Nordic / extreme light | 1:4–1:5 | allongé / high-flow |
| Light–medium | 1:3 | modern specialty |
| Medium | 1:2 | classic |
| Dark | 1:1–1:2 | ristretto-leaning; manage bitters |

Then move along the [[concepts/espresso-shot-styles|shot-style spectrum]] (ristretto → sprover = the espresso X×Z spectrum). Origin starts: Eth/Kenya washed 92–93 °C; naturals 90–91 °C (watch muddiness); Brazil/blend 1:2.5–3 for milk. 9 bar, 25–32 s.

---

## 6 · Cold brew & flash-chill iced

**Cold brew** — full immersion; ambient (22 °C, ~12 h) ≡ refrigerated (4 °C, ~36 h). Vs hot at same TDS: more floral, less bitter/sour/acidic; **not sweeter**. Best: light roast + Ethiopia washed; avoid dark (woody); dilute ~4% concentrate to ~2%. Full detail: [[concepts/cold-brew]].

**Flash-chill iced** — brew hot onto ice; keeps aromatics ([[concepts/flash-chill-iced-coffee]]). Kasuya's Switch pair: 4:6-applied (halve water; sharp acidity — bright beans) vs 2-pour immersion hybrid (smoother, sweeter). Choose by bean.

---

## 7 · The backbone — Brewing Control Chart

[[concepts/brewing-control-chart]] (Guinard et al. 2023, UC Davis) **is the X × Z plane**: percent-extraction (X) × TDS (Z), with sensory attributes mapped on it and **no single "ideal"** (two consumer clusters). It omits **Y** — the clarity↔body filtration axis this page adds. Two takeaways:

- **Sweetness-forward**: low-to-mid TDS + ~18–21% PE — extract fully, keep strength modest (dilute/bypass) to dodge the bitter/astringent corner.
- **Temperature is secondary** at fixed TDS/PE (Batali et al. 2020) — grind and ratio do the moving; temp mostly changes how you get there.

---

## 8 · System constants & terroir

- **Grinder** — its [[concepts/particle-size-distribution|PSD]] (fines) conditions the grind→X mapping and the clarity↔body (**Y**) floor; "dialling in espresso = dialling in fines."
- **Water** — deliberately out of scope: HK tap/filtered water is near-neutral for coffee, so it isn't a working variable here.
- **Terroir standard** — for *comparing* origins, SCA cupping (8.25 g/150 mL, 93 °C, Agtron ~65) is the reference; sits between espresso and filter. Method modifies terroir *expression*, not the underlying character. See [[shared/terroir]].

---

## Open Questions

- How does carbonic maceration shift the (X,Y) home vs standard naturals?
- At what roast level does the Graycano/deep-bed body advantage (Y) turn muddy?
- Does metal vs paper filtration move Y (body) enough to matter for cold brew?

---

*Last updated: 2026-09-01*

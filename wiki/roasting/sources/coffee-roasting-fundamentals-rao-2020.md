---
title: "Coffee Roasting Fundamentals"
domain: roasting
date_ingested: 2026-06-26
source_type: article
tags: [roasting, ror, dtr, baked-roast, roast-time, data-logging, scott-rao, aillio-bullet, ibts]
raw_path: raw/roasting/Coffee Roasting Fundamentals.md
---

# Coffee Roasting Fundamentals

**Source**: Rao, Scott. "Coffee Roasting Fundamentals." scottrao.com. 2020-03-30.
**Credibility**: **High-Medium (practitioner)** — Scott Rao is the most cited practitioner authority in specialty coffee roasting; authored "The Coffee Roaster's Companion" (2014) and "Coffee Roasting: Best Practices"; consulted for ~600 roasters; invented the DTR concept. This is a blog post (not peer-reviewed), and claims are based on experience, not controlled experiments. One peer-reviewed study (Münchow et al. 2020) found professional tasters could not detect the baking defect above chance — Rao disputes the methodology but does not provide experimental counter-evidence. See Contradictions section. Note: Rao was cited by Lindsey et al. 2024 ([[sources/caffeine-extraction-roast-lindsey-2024]]) for "insightful conversations related to roasting."

## Summary

Rao corrects several common misunderstandings about his own teachings. The two most important clarifications: (1) DTR (which he invented) is a useful QC tool and guideline, but getting smooth RoR is the prerequisite — DTR is "step two"; (2) baked roasts are caused by hard RoR crashes, not slow roasting. The piece also establishes that probe calibration variation makes it impossible to copy bean/drop temperature numbers from one roaster to another without adjustment, and that optimal roast duration is always relative to batch size / burner output ratio.

## Key Claims

### Roast time is context-dependent

No single correct roast duration exists. An 8-minute roast may be appropriate for 3kg in a Probat P12 but is far too fast for 12kg in the same machine.

"Optimal roast duration is dependent on the **ratio of batch size to burner output**."

**Implication for Aillio Bullet R2 Pro**: batch size must be specified when describing any roast time. A 9-minute profile at 500g may not translate to a 9-minute profile at 250g — the ratio changes.

### Roast color is a style/skill decision

Rao personally roasts and consumes extremely light roasts but explicitly states this is not a recommendation for all roasters. Key nuance:

"I also believe roasters should roast only as **light as they have the skill to do successfully**; if you often underdevelop coffee, then I recommend roasting a little darker until you have figured out a system to improve development of lighter roasts."

Under-development is a real quality risk. A light roast done poorly produces worse results than a medium roast done well.

### Probe calibration — do not copy temperatures from other roasters

Rao cites a self-example: he might hit first crack at 375°F (190°C) BT and drop at 405°F (207°C) BT, but "on your machine the equivalent numbers may be 10°F (5°C) higher, depending on our relative probe calibrations and the environmental temperatures at those moments in the roasts."

**Implication**: Temperature targets in this wiki (including from Lindsey 2024 on the Aillio Bullet v2) are machine-specific starting points, not universal targets. ET readings affect BT readings. Develop and calibrate your own reference profile from Agtron color and cup results, not from other people's drop temperatures.

Rao recommends: 2.5–3mm diameter ungrounded probe in a well-positioned location; ET probe; Artisan or Cropster software for data logging. Data logging made specialty roasters' learning go "vertical."

### Baked roasts — definition and cause

**Caused by**: hard RoR crashes (sudden steep drops in the rate of rise) — NOT by slow roasting
**Sensory character**: less sweet, more hollow, straw-like notes, flatter acidity

"Baked roasts are caused by hard RoR crashes, not by slow roasting."

Some roasters intentionally bake coffee to reduce acidity (they can control this), but Rao recommends other methods to accomplish lower acidity. A baked profile is a defect, not a style target.

**Mechanism hypothesis (Rao, from forum)**: He declines to spell it out in the blog, but the implication from the system-level description is that a smooth declining RoR ensures the heat gradient between the bean core and surface is consistently managed. A crash disrupts this gradient, potentially leaving the core underdeveloped relative to the surface temperature at drop.

### DTR — clarifications from its inventor

Rao invented the DTR (Development Time Ratio) concept in "The Coffee Roaster's Companion":
- **20–25% is a general guideline** for typical specialty roasters — it is NOT a universal prescription
- 15% DTR may be appropriate for the ~1% of "very light roasters" (middle-of-first-crack drops)
- Going outside 20–25% is "perfectly ok, especially if you roast very light or very dark"
- For dark espresso roasts (drop temps 430–440°F), 25% DTR remains a reasonable guideline but adjust as needed
- **Do not drop based on DTR alone** — drop based on color or bean temperature
- If RoR is unstable (crashing, spiking), DTR is meaningless as a quality indicator

**Priority order (Rao's explicit teaching)**:
- **Step 1**: Control and smooth RoR
- **Step 2**: Worry about DTR and everything else

### Smooth RoR — the core principle

"99% of roasters' RORs are not smooth enough to eliminate all roast defects."

Smooth RoR = a consistently, monotonically declining curve from the start of the roast to drop. No crashes (sudden steep falls), no flicks (brief upward spikes), no stalling (flat RoR).

Rao claims: ~600 roasting clients consulted; 99% were happier with their roasting once RoR became smooth. Only ~10% achieved what he calls "mastery" of smooth RoR.

**Important Rao clarification** (from the forum): He is NOT saying "for a given color/development time/time to FC, smoother is always better." His belief is about a *system* of best practices. This distinction matters when evaluating the Münchow study (see Contradictions).

### Aillio Bullet IBTS — Rao's 2020 comment (now outdated)

A forum questioner used an Aillio Bullet with single IBTS probe, arguing the IR reading is "more stable" and shows smooth RoR where the BT probe shows crashes. Rao responded in 2020:

"The IR sensor on the Aillio is **not more accurate; it is less**. That is why **they have added a 128-point IR sensor to their new machine**; having one is not reliable."

**Status**: As of 2026, the Aillio Bullet R2 Pro does have a 128-point IBTS sensor array — this appears to be exactly the improved version Rao was anticipating when he wrote this in 2020. The "not reliable" critique was directed at the single-sensor version, not the R2 Pro's multi-point array. See [[entities/aillio-bullet]] for how the R2 Pro IBTS is understood as an improvement.

## Contradictions / Open Questions

**The Münchow 2020 tension**: A questioner in the forum cites Münchow, Alstrup, Steen, and Giacalone (2020), "Roasting conditions and coffee flavor: A multi-study empirical investigation" (*Beverages*), which reportedly found that professional coffee tasters could not detect the baking defect above chance (~33%) in triangular discrimination blind testing, and that those who did identify it could not reliably name the defect. If true, this is significant evidence against the practical importance of smooth RoR for cup quality at the taster-detection level.

Rao's response: (1) the study methodology is flawed (he doesn't elaborate); (2) his belief is about a system, not the isolated variable "smooth RoR at same color/DT/time to 1C." He stops short of providing counter-experimental evidence.

**Wiki position**: Flag as an unresolved tension. Rao's authority and practitioner consensus on smooth RoR is high; the Münchow 2020 study (not yet ingested in this wiki) is the only peer-reviewed counter-data point. The two may not be in direct contradiction if Rao's claims are systemic (smooth RoR requires everything else to change too) rather than variable-isolation claims. Priority ingest if the Münchow paper is available.

**Rao's 2020 IBTS critique vs. R2 Pro IBTS**: resolved — R2 Pro's 128-point array is the improved version Rao was anticipating.

## Key Entities Mentioned

- [[entities/scott-rao]] — author; inventor of DTR; "The Coffee Roaster's Companion"
- [[entities/aillio-bullet]] — Aillio Bullet mentioned in forum as a specific use case; IBTS comment

## Wiki Pages Updated

- `wiki/roasting/concepts/roasting-parameters.md` — DTR clarifications (ranges, origin, priority order); baked roast defect section; roast time principle; probe calibration warning; source_count 1→2
- `wiki/roasting/entities/scott-rao.md` — NEW entity page
- `wiki/roasting/entities/aillio-bullet.md` — IBTS context added: Rao's 2020 critique was for single-sensor IBTS; R2 Pro's 128-point array addresses it
- `wiki/index.md` — source and entity indexed
- `wiki/log.md` — ingest entry appended

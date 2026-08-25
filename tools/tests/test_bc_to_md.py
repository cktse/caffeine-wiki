#!/usr/bin/env python3
"""Tests for bc_to_md.py (spec §1.10). Stdlib only. Run: python3 tools/tests/test_bc_to_md.py"""
import os
import time
import sys
import json
import difflib
from pathlib import Path

# fmt_date renders in local time; pin to UTC so golden dates are machine-independent.
os.environ["TZ"] = "UTC"
time.tzset()

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import bc_to_md as bc  # noqa: E402

FIX, EXP = HERE / "fixtures", HERE / "expected"
EXPORT = json.loads((FIX / "export_min.json").read_text(encoding="utf-8"))
IDX = bc.build_indexes(EXPORT)
TODAY = "2026-01-01"

_fail = []


def check(name, cond, detail=""):
    print(f"{'PASS' if cond else 'FAIL'}  {name}" + ("" if cond else f"\n{detail}"))
    if not cond:
        _fail.append(name)


# ── unit: map helpers (positive + negative) ──
check("parse_agtron", bc.parse_agtron("Ag 74.0 gr") == 74.0)
check("parse_agtron_none", bc.parse_agtron("no reading") is None)
check("fmt_time", bc.fmt_time(150) == "2:30")
check("fmt_time_zero_none", bc.fmt_time(0) is None)
check("espresso_by_name", bc.is_espresso("Espresso", {}) is True)
check("espresso_by_type", bc.is_espresso("V60", {"bean_roasting_type": "ESPRESSO"}) is True)
check("espresso_false", bc.is_espresso("V60", {}) is False)

# ── golden: generate (regression vs frozen baselines) ──
for bean in EXPORT["BEANS"]:
    slug = bc.slugify(bean["name"])
    got = bc.render_bean_md(bc.map_bean(bean), bc.mapped_brews(EXPORT, IDX, bean), today=TODAY)
    want = (EXP / f"{slug}.md").read_text(encoding="utf-8")
    if got == want:
        check(f"golden:{slug}", True)
    else:
        diff = "".join(difflib.unified_diff(
            want.splitlines(True), got.splitlines(True), "expected", "got"))
        check(f"golden:{slug}", False, diff)

# ── append dedup: preserve manual edits, add only the new brew ──
base = (FIX / "append_base.md").read_text(encoding="utf-8")
bean_a = IDX["beans"]["bean-a"]
new_text, n = bc.append_new_brews(base, bc.mapped_brews(EXPORT, IDX, bean_a))
fm, _, body = bc.split_frontmatter(new_text)
check("append_count_one", n == 1, f"n={n}")
check("append_ledger_extended", fm.get("bc_brews") == ["brew-a1", "brew-a2"], str(fm.get("bc_brews")))
check("append_new_row_present", "2026-01-07" in body and "| 90C |" in body, "brew-a2 row missing")
check("append_preserves_manual_body", "MANUAL EDIT" in body and "MANUAL RECIPE" in body, "manual body lost")
check("append_preserves_manual_frontmatter", fm.get("origin") == "Testland", str(fm.get("origin")))
check("append_idempotent", bc.append_new_brews(new_text, bc.mapped_brews(EXPORT, IDX, bean_a))[1] == 0,
      "second append should add nothing")

print()
if _fail:
    print(f"{len(_fail)} FAILED: {_fail}")
    sys.exit(1)
print("ALL PASS")

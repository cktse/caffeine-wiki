#!/usr/bin/env python3
"""bc_to_md.py — Bean Conqueror export -> per-bean personal_log Markdown.

Design contract: tools/specs.md §1. Modules (unidirectional): load -> map ->
render -> ledger; cli on top. Frontmatter I/O via yaml12 (YAML 1.2).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

from yaml12 import parse_yaml, format_yaml

# Identity fields left blank for manual, as-claimed enrichment from the roaster URL.
IDENTITY_BLANKS = [
    "origin", "region", "farm", "producer",
    "varietals", "processing", "elevation", "roast_level", "notes",
]

# ───────────────────────── load ─────────────────────────

def load_export(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _index(arr):
    return {o["config"]["uuid"]: o for o in arr if o.get("config", {}).get("uuid")}


def build_indexes(exp: dict) -> dict:
    return {
        "beans": _index(exp.get("BEANS", [])),
        "prep": _index(exp.get("PREPARATION", [])),
        "mill": _index(exp.get("MILL", [])),
    }


def brews_for_bean(exp: dict, bean_uuid: str) -> list:
    out = [b for b in exp.get("BREWS", []) if b.get("bean") == bean_uuid]
    out.sort(key=lambda b: b.get("config", {}).get("unix_timestamp") or 0)
    return out


# ───────────────────────── map ─────────────────────────

_AGTRON_RE = re.compile(r"\bAg[a-z]*\.?\s*([0-9]+(?:\.[0-9]+)?)", re.I)


def parse_agtron(note):
    if not note:
        return None
    m = _AGTRON_RE.search(note)
    return float(m.group(1)) if m else None


def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _pos(x):
    v = _num(x)
    return v if (v is not None and v > 0) else None


def fmt_time(seconds):
    s = _num(seconds)
    if not s or s <= 0:
        return None
    s = int(s)
    return f"{s // 60}:{s % 60:02d}"


def fmt_date(brew):
    ts = brew.get("config", {}).get("unix_timestamp")
    if not ts:
        return None
    return _dt.datetime.fromtimestamp(int(ts), _dt.timezone.utc).date().isoformat()


def roast_date(bean):
    rd = bean.get("roastingDate")
    return rd[:10] if rd else None


def is_espresso(prep_name, bean):
    return "espresso" in (prep_name or "").lower() or bean.get("bean_roasting_type") == "ESPRESSO"


def map_bean(bean: dict) -> dict:
    weight = _pos(bean.get("weight"))
    cost = _pos(bean.get("cost"))
    if cost is not None and float(cost).is_integer():
        cost = int(cost)
    rt = bean.get("bean_roasting_type")
    return {
        "title": (bean.get("name") or "").strip() or "(unnamed)",
        "bc_bean_id": bean["config"]["uuid"],
        "roaster": bean.get("roaster") or None,
        "roasted_on": roast_date(bean),
        "roast_target": rt if rt in ("FILTER", "ESPRESSO") else None,
        "agtron_whole": parse_agtron(bean.get("note")),
        "weight": f"{_fmt_num(weight)}g" if weight else None,
        "cost": cost,
        "url": bean.get("url") or None,
        "blend": bean.get("beanMix") == "BLEND",
    }


def map_brew(brew: dict, prep_name, mill_name, espresso: bool) -> dict:
    dose = _pos(brew.get("grind_weight"))
    water = _pos(brew.get("brew_quantity"))
    bev = _pos(brew.get("brew_beverage_quantity"))
    tds = _pos(brew.get("tds"))
    gsz = brew.get("grind_size")
    grind = f"{mill_name} @ {gsz}" if mill_name else (str(gsz) if gsz not in (None, "") else None)
    # Derived metrics (Ratio, EY) are intentionally not emitted — recomputed at ingestion.
    return {
        "bc_brew_id": brew["config"]["uuid"],
        "date": fmt_date(brew),
        "method": prep_name or "(unknown)",
        "espresso": espresso,
        "grind": grind,
        "dose": dose,
        "water": water,
        "beverage": bev,
        "temp": _pos(brew.get("brew_temperature")),
        "time": fmt_time(brew.get("brew_time")),
        "tds": tds,
    }


def mapped_brews(exp, idx, bean) -> list:
    out = []
    for b in brews_for_bean(exp, bean["config"]["uuid"]):
        prep = idx["prep"].get(b.get("method_of_preparation"), {}).get("name")
        mill = idx["mill"].get(b.get("mill"), {}).get("name")
        out.append(map_brew(b, prep, mill, is_espresso(prep, bean)))
    return out


# ───────────────────────── render ─────────────────────────

def _fmt_num(v):
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    return str(v)


def _cell(v, unit="", none="—"):
    if v is None or v == "":
        return none
    return f"{_fmt_num(v)}{unit}" if unit else str(v)


# Emitted columns are raw measured values only (no Ratio/EY — recomputed at ingestion);
# a trailing blank Notes column is for manual technique/tasting additions.
_PO_HEAD = "| Date | Grind | Dose | Water | Beverage | Temp | Time | TDS | Notes |"
_PO_SEP = "|---|---|---|---|---|---|---|---|---|"
_ESP_HEAD = "| Date | Grind | Dose | Yield | Temp | Time | TDS | Notes |"
_ESP_SEP = "|---|---|---|---|---|---|---|---|"


def brew_row(b: dict) -> str:
    # Units are space-free (15g, 92C) for easy manual editing; Notes left blank.
    tail = [_cell(b["temp"], "C"), _cell(b["time"]), _cell(b["tds"], "%"), ""]
    if b["espresso"]:
        cells = [_cell(b["date"]), _cell(b["grind"]), _cell(b["dose"], "g"),
                 _cell(b["beverage"] or b["water"], "g")] + tail
    else:
        cells = [_cell(b["date"]), _cell(b["grind"]), _cell(b["dose"], "g"),
                 _cell(b["water"], "g"), _cell(b["beverage"], "g")] + tail
    return "| " + " | ".join(cells) + " |"


def method_tag(espresso):
    return " (espresso)" if espresso else " (pour-over)"


def render_method_section(method, brews) -> str:
    esp = brews[0]["espresso"]
    head, sep = (_ESP_HEAD, _ESP_SEP) if esp else (_PO_HEAD, _PO_SEP)
    rows = "\n".join(brew_row(b) for b in brews)
    return f"### {method}{method_tag(esp)}\n\n{head}\n{sep}\n{rows}\n"


def _group_by_method(brews):
    order, groups = [], {}
    for b in brews:
        groups.setdefault(b["method"], []).append(b)
        if b["method"] not in order:
            order.append(b["method"])
    return order, groups


def render_frontmatter(fields: dict, ledger: list, today: str) -> dict:
    fm = {"title": fields["title"], "source_type": "personal_log",
          "bc_bean_id": fields["bc_bean_id"], "bc_brews": ledger}
    for k in ("roaster", "roasted_on", "roast_target", "agtron_whole", "weight", "cost", "url"):
        if fields.get(k) is not None:
            fm[k] = fields[k]
    if fields.get("blend"):
        fm["blend"] = True
    for k in IDENTITY_BLANKS:
        fm[k] = ""
    fm["date_ingested"] = today
    fm["tags"] = ["personal-log", "brewing"]
    return fm


def render_bean_md(fields: dict, brews: list, today: str | None = None) -> str:
    today = today or _dt.date.today().isoformat()
    ledger = [b["bc_brew_id"] for b in brews]
    fm = format_yaml(render_frontmatter(fields, ledger, today)).rstrip("\n")
    order, groups = _group_by_method(brews)
    sections = "\n".join(render_method_section(m, groups[m]) for m in order) or "_(no brews)_\n"
    return (
        f"---\n{fm}\n---\n\n"
        f"# {fields['title']}\n\n"
        "> First-party brew log materialized from a Bean Conqueror export. The brew "
        "tables below are first-party **measured** data. The blank identity fields above "
        "are to be filled from the roaster URL **as claimed** (see Sourcing Discipline) — "
        "do not assert them as entity facts.\n\n"
        "## Recommended Recipe\n\n_(fill from roaster, if any)_\n\n"
        "## Brewing Logs\n\n"
        f"{sections}\n"
        "## TODO\n"
        "- Fill bean identity from the roaster URL.\n"
        "- Add technique BC doesn't capture (dual-temp tail, flow/pour sequence).\n"
        "- Log sensory.\n"
    )


# ───────────────────────── ledger (append) ─────────────────────────

def split_frontmatter(text: str):
    """Return (frontmatter_dict, frontmatter_text, body_text)."""
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("no YAML frontmatter found")
    return parse_yaml(m.group(1)), m.group(1), m.group(2)


def _append_rows_to_body(body: str, method: str, esp: bool, rows: list[str]) -> str:
    lines = body.split("\n")
    # locate "### {method}" section heading
    hdr = None
    for i, ln in enumerate(lines):
        if ln.startswith(f"### {method}"):
            hdr = i
            break
    if hdr is not None:
        # find the last contiguous table row after the header
        last = None
        for j in range(hdr + 1, len(lines)):
            if lines[j].startswith("|"):
                last = j
            elif lines[j].startswith("### ") or lines[j].startswith("## "):
                break
        insert_at = (last + 1) if last is not None else (hdr + 1)
        return "\n".join(lines[:insert_at] + rows + lines[insert_at:])
    # method section absent: insert a fresh section before "## TODO" (or at end of Brewing Logs)
    head, sep = (_ESP_HEAD, _ESP_SEP) if esp else (_PO_HEAD, _PO_SEP)
    block = ["", f"### {method}{method_tag(esp)}", "", head, sep] + rows
    todo = next((i for i, ln in enumerate(lines) if ln.startswith("## TODO")), None)
    if todo is not None:
        return "\n".join(lines[:todo] + block + [""] + lines[todo:])
    return "\n".join(lines + block)


def append_new_brews(md_text: str, new_brews: list) -> tuple[str, int]:
    fm, fm_text, body = split_frontmatter(md_text)
    have = set(fm.get("bc_brews") or [])
    todo = [b for b in new_brews if b["bc_brew_id"] not in have]
    if not todo:
        return md_text, 0
    order, groups = _group_by_method(todo)
    for m in order:
        esp = groups[m][0]["espresso"]
        body = _append_rows_to_body(body, m, esp, [brew_row(b) for b in groups[m]])
    fm["bc_brews"] = (fm.get("bc_brews") or []) + [b["bc_brew_id"] for b in todo]
    new_fm = format_yaml(fm).rstrip("\n")
    return f"---\n{new_fm}\n---\n{body}", len(todo)


# ───────────────────────── cli ─────────────────────────

def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "bean"


def _resolve(idx, selectors):
    beans = idx["beans"]
    hits = []
    for sel in selectors:
        if sel in beans:
            hits.append(beans[sel])
            continue
        low = sel.lower()
        matched = [b for b in beans.values() if low in (b.get("name") or "").lower()]
        if not matched:
            print(f"! no bean matches '{sel}'", file=sys.stderr)
        hits.extend(matched)
    # de-dup by uuid, preserve order
    seen, out = set(), []
    for b in hits:
        u = b["config"]["uuid"]
        if u not in seen:
            seen.add(u); out.append(b)
    return out


def cmd_manifest(args):
    exp = load_export(args.export)
    idx = build_indexes(exp)
    rows = []
    for u, bean in idx["beans"].items():
        bs = brews_for_bean(exp, u)
        ntds = sum(1 for b in bs if _pos(b.get("tds")))
        rt = bean.get("bean_roasting_type")
        rows.append((roast_date(bean) or "—", (bean.get("name") or "")[:44],
                     (bean.get("roaster") or "")[:16], len(bs), ntds,
                     rt if rt in ("FILTER", "ESPRESSO") else "—"))
    rows.sort(key=lambda r: r[0], reverse=True)
    print(f"{'ROAST DATE':<11} {'BEAN':<44} {'ROASTER':<16} {'#BRW':>4} {'#TDS':>4}  TARGET")
    for r in rows:
        print(f"{r[0]:<11} {r[1]:<44} {r[2]:<16} {r[3]:>4} {r[4]:>4}  {r[5]}")
    print(f"\n{len(rows)} beans, {len(exp.get('BREWS', []))} brews")


def cmd_generate(args):
    exp = load_export(args.export)
    idx = build_indexes(exp)
    beans = _resolve(idx, args.bean) if args.bean else list(idx["beans"].values())
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    for bean in beans:
        md = render_bean_md(map_bean(bean), mapped_brews(exp, idx, bean), args.today)
        path = outdir / f"{slugify(bean.get('name') or 'bean')}.md"
        path.write_text(md, encoding="utf-8")
        print(f"✔ {path}")


def cmd_append(args):
    exp = load_export(args.export)
    idx = build_indexes(exp)
    md_path = Path(args.md)
    fm, _, _ = split_frontmatter(md_path.read_text(encoding="utf-8"))
    bean_id = fm.get("bc_bean_id")
    bean = idx["beans"].get(bean_id)
    if not bean:
        sys.exit(f"! bc_bean_id {bean_id} not found in export")
    new_text, n = append_new_brews(md_path.read_text(encoding="utf-8"),
                                   mapped_brews(exp, idx, bean))
    md_path.write_text(new_text, encoding="utf-8")
    print(f"✔ appended {n} new brew(s) to {md_path}")


def build_parser():
    p = argparse.ArgumentParser(description="Bean Conqueror export -> personal_log Markdown")
    p.add_argument("--export", default="scratchpad/Beanconqueror.json",
                   help="path to the Bean Conqueror JSON export")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("manifest", help="list beans for selection").set_defaults(func=cmd_manifest)
    g = sub.add_parser("generate", help="write baseline MD per bean")
    g.add_argument("--bean", action="append", default=[], help="bean uuid or name substring (repeatable); omit for all")
    g.add_argument("--out", default="scratchpad/bc_out", help="output directory")
    g.add_argument("--today", default=None, help="override date_ingested (ISO); default = today")
    g.set_defaults(func=cmd_generate)
    a = sub.add_parser("append", help="append new brews into an enriched MD")
    a.add_argument("--md", required=True, help="path to the enriched Markdown file")
    a.set_defaults(func=cmd_append)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()

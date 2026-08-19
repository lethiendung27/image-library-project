#!/usr/bin/env python3
"""Generate the GIF library folder tree and its type cards (ADR-023).

A card is a VIEW of a type file, the same way registry/index.yaml is a view of the
type files. It is written into the library folder so an editor reads the law where
they browse, and it is never hand-edited: run this again instead.

Every measured figure on a card is computed from ingestion/gifs.jsonl at write time.
Where the ledger has too few records to measure, the card says so rather than
printing a zero that reads as a measurement.

Usage:
  python3 scripts/gen-gif-cards.py                    # default root ~/Downloads/gif-library
  python3 scripts/gen-gif-cards.py --root /path/to/library
  python3 scripts/gen-gif-cards.py --dry-run          # print what would change
"""
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate as V  # noqa: E402  (parser reuse — one YAML subset, one implementation)

GIF_TYPES_DIR = os.path.join(V.ROOT, "registry", "gif-types")
LEDGER_PATH = os.path.join(V.ROOT, "ingestion", "gifs.jsonl")
DEFAULT_ROOT = os.path.join(os.path.expanduser("~"), "Downloads",
                            "image-library-assets", "gifs")
MEASURE_MIN = 3  # below this the card reports "not enough files", never a figure


def load_gif_types():
    out = {}
    if not os.path.isdir(GIF_TYPES_DIR):
        return out
    for fn in sorted(os.listdir(GIF_TYPES_DIR)):
        if not fn.endswith(".md") or fn.startswith("_") or fn == "README.md":
            continue
        path = os.path.join(GIF_TYPES_DIR, fn)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        fm_lines, body = V.split_frontmatter(text, f"registry/gif-types/{fn}")
        if fm_lines is None:
            continue
        fm = V.parse_block(fm_lines, f"registry/gif-types/{fn}")
        out[fm.get("id") or os.path.splitext(fn)[0]] = {
            "fm": fm, "sections": V.split_sections(body)}
    return out


def load_ledger():
    recs = []
    if not os.path.exists(LEDGER_PATH):
        return recs
    with open(LEDGER_PATH, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                recs.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"WARN ingestion/gifs.jsonl line {n}: not valid JSON — skipped")
    return recs


def folded(section, key):
    """Pull `key: >` folded text out of a TRIGGER section."""
    if not section:
        return ""
    lines, grab, buf = section.splitlines(), False, []
    for line in lines:
        if line.strip().startswith(f"{key}:"):
            grab = True
            continue
        if grab:
            if line.startswith("  ") or not line.strip():
                buf.append(line.strip())
            else:
                break
    return " ".join(x for x in buf if x).strip()


def measured(recs, tid):
    mine = [r for r in recs if r.get("type") == tid]
    if len(mine) < MEASURE_MIN:
        return (f"{len(mine)} file(s) filed here — too few to measure a house standard "
                f"yet (needs {MEASURE_MIN}). Until then the declared band above is "
                f"the brief.")
    durs = [r["duration_s"] for r in mine if isinstance(r.get("duration_s"), (int, float))]
    beats = [r["beats"] for r in mine if isinstance(r.get("beats"), int)]
    bits = [f"{len(mine)} files filed here"]
    if durs:
        bits.append(f"median length {statistics.median(durs):.1f}s "
                    f"(range {min(durs):.1f}–{max(durs):.1f}s)")
    if beats:
        bits.append(f"median {statistics.median(beats):.0f} beats "
                    f"(range {min(beats)}–{max(beats)})")
    return "Measured from the ledger: " + ", ".join(bits) + "."


def card(tid, t, recs):
    fm, sec = t["fm"], t["sections"]
    dur = fm.get("duration_s") or []
    beats = fm.get("beats") or []
    chans = ", ".join(fm.get("channels") or [])
    lp = "landing-page" in (fm.get("channels") or [])
    out = []
    out.append(f"# {tid}")
    out.append("")
    out.append("GENERATED FILE — do not edit. Source: `registry/gif-types/"
               f"{tid}.md` · regenerate with `python3 scripts/gen-gif-cards.py`.")
    out.append("")
    out.append("## The one message")
    out.append(sec.get("PURPOSE", "").strip())
    out.append("")
    out.append("## A GIF belongs here when")
    out.append(folded(sec.get("TRIGGER", ""), "use_when") or "—")
    out.append("")
    out.append("## It does NOT belong here when")
    out.append(folded(sec.get("TRIGGER", ""), "avoid_when") or "—")
    out.append("")
    out.append("## Telling it apart from its neighbours")
    out.append(sec.get("BOUNDARY", "").strip())
    out.append("")
    out.append("## What the brief must name")
    out.append(sec.get("BRIEF", "").strip())
    out.append("")
    out.append("## Must not appear")
    out.append(sec.get("NEGATIVE", "").strip())
    out.append("")
    out.append("## House standard")
    out.append(f"- Declared band: **{dur[0]}–{dur[1]}s**, **{beats[0]}–{beats[1]} beats**."
               if len(dur) == 2 and len(beats) == 2 else "- Declared band: —")
    out.append(f"- {measured(recs, tid)}")
    out.append(f"- Channels: {chans}."
               + ("" if lp else " **Not routable to a landing-page slot.**"))
    out.append(f"- Counts toward the page motion floor as: **{fm.get('group')}**.")
    out.append("")
    out.append("## Filing a new file here")
    out.append(f"Name it `{tid}_<product-slug>_<seq>.mp4` with the sequence number issued "
               "by the ledger, deliver mp4/webm and muted, and append one record to "
               "`ingestion/gifs.jsonl`. Never rename a file that is already filed. "
               "Shared law for every type: `registry/gif-instruction.md`.")
    out.append("")
    return "\n".join(out)


def main(argv):
    root = DEFAULT_ROOT
    if "--root" in argv:
        root = os.path.abspath(argv[argv.index("--root") + 1])
    dry = "--dry-run" in argv

    types = load_gif_types()
    if not types:
        print("no gif types found in registry/gif-types/ — nothing to do")
        return 1
    if V.ERRORS:
        for e in V.ERRORS:
            print(f"ERROR {e}")
        print("gif type files do not parse — fix them first")
        return 1
    recs = load_ledger()

    wrote, same = 0, 0
    for tid, t in sorted(types.items()):
        folder = os.path.join(root, tid)
        target = os.path.join(folder, "README.md")
        text = card(tid, t, recs)
        old = None
        if os.path.exists(target):
            with open(target, encoding="utf-8") as f:
                old = f.read()
        if old == text:
            same += 1
            continue
        if dry:
            print(f"would write {target}")
        else:
            os.makedirs(folder, exist_ok=True)
            with open(target, "w", encoding="utf-8") as f:
                f.write(text)
        wrote += 1

    verb = "would write" if dry else "wrote"
    print(f"{verb} {wrote} card(s), {same} unchanged, under {root}")
    print(f"ledger: {len(recs)} record(s) in ingestion/gifs.jsonl")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

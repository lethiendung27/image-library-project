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
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate as V  # noqa: E402  (parser reuse — one YAML subset, one implementation)

GIF_TYPES_DIR = os.path.join(V.ROOT, "registry", "gif-types")
VI_PATH = os.path.join(V.ROOT, "registry", "gif-cards-vi.md")
LEDGER_PATH = os.path.join(V.ROOT, "ingestion", "gifs.jsonl")
def _assets_root():
    """Find the asset folder rather than assuming it. See SPEC §6.4.

    It is a SIBLING of the repo directory and stayed one when the owner relocated
    both trees on 2026-09-10. Sibling first, then the historical `~/Downloads`
    location; the sibling is returned either way, so a missing folder names the
    place to look instead of quietly building a second empty tree somewhere else.
    """
    for cand in (os.path.join(os.path.dirname(V.ROOT), "image-library-assets"),
                 os.path.join(os.path.expanduser("~"), "Downloads",
                              "image-library-assets")):
        if os.path.isdir(cand):
            return cand
    return os.path.join(os.path.dirname(V.ROOT), "image-library-assets")


DEFAULT_ROOT = os.path.join(_assets_root(), "gifs-library")
VI_FIELDS = ("message", "yes", "no", "vs")
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


def lede(text):
    """First sentence. The type files open every section with the whole point."""
    t = " ".join((text or "").split())
    m = re.match(r"(.+?[.!?])(\s|$)", t)
    return (m.group(1) if m else t) or "—"


def _parse_vi_blocks(path, fields):
    """`## <id>` sections whose fields are `<key>:` alone on a line, the value being
    everything until the next key or the next type (ADR-045). Block form because the
    Vietnamese card is explanation with examples, and explanation does not fit a line."""
    out, cur, key, buf = {}, None, None, []

    def flush():
        if cur and key:
            text = "\n".join(buf).strip("\n")
            if text.strip():
                out[cur][key] = text.rstrip()

    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if line.startswith("## "):
                flush()
                cur, key, buf = line[3:].strip(), None, []
                out[cur] = {}
            elif cur is not None and line.rstrip().endswith(":") \
                    and line.rstrip()[:-1].strip() in fields and not line.startswith(" "):
                flush()
                key, buf = line.rstrip()[:-1].strip(), []
            elif key is not None:
                buf.append(line)
    flush()
    return out


def load_vi():
    return _parse_vi_blocks(VI_PATH, VI_FIELDS) if os.path.exists(VI_PATH) else {}


def against(boundary):
    """The BOUNDARY section's `Against X — …` lines, joined."""
    lines, buf = [], ""
    for ln in (boundary or "").splitlines():
        if ln.strip().startswith("Against"):
            if buf:
                lines.append(" ".join(buf.split()))
            buf = ln
        elif buf and ln.strip():
            buf += " " + ln
        elif buf:
            lines.append(" ".join(buf.split()))
            buf = ""
    if buf:
        lines.append(" ".join(buf.split()))
    return " ".join(lines) or "—"


def _standing(tid, fm, recs):
    dur = fm.get("duration_s") or []
    beats = fm.get("beats") or []
    band = (f"{dur[0]}–{dur[1]}s · {beats[0]}–{beats[1]} beats"
            if len(dur) == 2 and len(beats) == 2 else "—")
    chans = ", ".join(fm.get("channels") or [])
    lp = "landing-page" in (fm.get("channels") or [])
    return band, chans, lp, measured(recs, tid)


def card(tid, t, recs):
    """The English card. Short by construction: every line is one sentence lifted
    from the type file, so it cannot drift from the law it summarises."""
    fm, sec = t["fm"], t["sections"]
    band, chans, lp, filed = _standing(tid, fm, recs)
    o = [f"# {tid}", "",
         "GENERATED — do not edit. Source `registry/gif-types/" + tid + ".md`. "
         "Regenerate: `python3 scripts/gen-gif-cards.py`. "
         "Vietnamese: `README.vi.md`.", "",
         f"**Argues** {lede(sec.get('PURPOSE'))}", "",
         f"**File here when** {lede(folded(sec.get('TRIGGER', ''), 'use_when'))}",
         f"**Not here when** {lede(folded(sec.get('TRIGGER', ''), 'avoid_when'))}",
         f"**Against its neighbours** {against(sec.get('BOUNDARY'))}", "",
         f"**Never in frame** {lede(sec.get('NEGATIVE'))}", "",
         f"**Band** {band} · {chans}"
         + ("" if lp else " · **not routable to a landing-page slot**")
         + f" · counts toward the motion floor as **{fm.get('group')}**",
         f"**Filed here** {filed}", "",
         "**Name it** `{page-type}-" + tid + "-{product-slug}-v{NN}.mp4` · mp4, muted · append one record to `ingestion/gifs.jsonl` · never rename a "
         "filed file · full law `registry/gif-instruction.md`", ""]
    return "\n".join(o)


def card_vi(tid, vi):
    """The Vietnamese card. Its copy is authored, not translated at build time —
    `registry/gif-cards-vi.md` — because a machine translation of law is a rule
    nobody can check (ADR-044)."""
    v = vi.get(tid, {})
    o = [f"# {tid}", "",
         "TỆP SINH TỰ ĐỘNG — đừng sửa tay. Nguồn `registry/gif-cards-vi.md`. "
         "Sinh lại: `python3 scripts/gen-gif-cards.py`. Bản tiếng Anh: `README.md`.", "",
         "## Loop này nói gì", "", v.get("message", "—"), "",
         "## Nộp vào đây khi", "", v.get("yes", "—"), "",
         "## Không phải ở đây khi", "", v.get("no", "—"), "",
         "## Phân biệt với các type kề", "", v.get("vs", "—"), "",
         "## Nộp một tệp mới vào đây", "",
         "Đặt tên `{page-type}-" + tid + "-{product-slug}-v{NN}.mp4`. Giao dưới dạng **mp4**, "
         "đã tắt tiếng. Thêm một dòng vào `ingestion/gifs.jsonl`. "
         "Đã nộp rồi thì không đổi tên nữa. Luật đầy đủ dùng chung cho mọi type: "
         "`registry/gif-instruction.md`.", ""]
    return "\n".join(o)


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
    vi = load_vi()
    missing = sorted(t for t in types if t not in vi)
    if missing:
        print(f"WARN  no Vietnamese copy in registry/gif-cards-vi.md for: "
              f"{', '.join(missing)} — those folders get an English card only")

    wrote, same = 0, 0
    for tid, t in sorted(types.items()):
        folder = os.path.join(root, tid)
        pages = [("README.md", card(tid, t, recs))]
        if tid in vi:
            pages.append(("README.vi.md", card_vi(tid, vi)))
        for fname, text in pages:
            target = os.path.join(folder, fname)
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

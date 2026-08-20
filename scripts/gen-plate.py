#!/usr/bin/env python3
"""Generate the motion brief plates for a routed session (G12, ADR-028).

A plate is the work order the editor who builds a loop reads. It used to be drawn
by an image model, and every constraint the old G12 carried — seven words a line,
no markup, a size band, a named stop before the frame edge — was a workaround for
a renderer that draws text badly. Generating it instead costs no generation call,
cannot misspell a filename and cannot wrap a line into the next one, which is what
lets the brief be prose. Like `registry/index.yaml` and the GIF library's folder
cards, a plate is a VIEW: never hand-edited, always regenerated.

SVG rather than PNG because SVG is text — deterministic, diffable, stdlib-writable,
and it opens in any browser or Finder preview.

Usage:
  python3 scripts/gen-plate.py                     # every session under query/sessions
  python3 scripts/gen-plate.py <session-dir> ...   # only those
  python3 scripts/gen-plate.py --check             # fail if any plate is stale
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSIONS = os.path.join(ROOT, "query", "sessions")

BG = "#31363d"
BORDER = "#f2f4f7"
INK = "#ffffff"
DIM = "#aeb6c0"
FONT = "Helvetica, Arial, sans-serif"
LONG_SIDE = 1200


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# Coarse Helvetica advance widths in em. A flat average put text past the border on
# the first plate generated; per-character is still an estimate but it is wrong in
# the safe direction, and the layout below leaves a margin on top of it.
_NARROW = "iljtfrI.,:;'|!()[]{}"
_WIDE = "mwMW@%"
_CAPS = "ABCDEFGHJKLNOPQRSTUVXYZ&"


def text_width(text, size, tracking=0.4):
    em = 0.0
    for ch in str(text):
        if ch == " ":
            em += 0.278
        elif ch in _NARROW:
            em += 0.30
        elif ch in _WIDE:
            em += 0.86
        elif ch in _CAPS:
            em += 0.70
        elif ch.isdigit():
            em += 0.556
        else:
            em += 0.55
    return em * size + tracking * len(str(text))


def wrap(text, width_px, size):
    """Greedy wrap measured per character rather than by a flat average."""
    lines, cur = [], ""
    for word in str(text).split():
        trial = word if not cur else cur + " " + word
        if text_width(trial, size) <= width_px or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def dimensions(ratio):
    try:
        w, h = (int(x) for x in str(ratio).split(":"))
    except (ValueError, TypeError):
        w, h = 16, 9
    if w >= h:
        return LONG_SIDE, max(1, round(LONG_SIDE * h / w))
    return max(1, round(LONG_SIDE * w / h)), LONG_SIDE


def plate_svg(gif):
    """The four fields, and the folder the editor takes precedent from."""
    W, H = dimensions(gif.get("ratio"))
    short = min(W, H)
    pad = round(short * 0.055)
    inner = round(short * 0.030)
    tx = pad + inner + round(short * 0.055)
    tw = W - 2 * tx + 2 * 0  # symmetric margins, so the right edge mirrors tx

    name_fs = max(20, round(short * 0.050))
    meta_fs = max(15, round(name_fs * 0.72))
    body_fs = max(14, round(name_fs * 0.62))
    refs_fs = max(12, round(name_fs * 0.50))
    body_lh = round(body_fs * 1.58)
    refs_lh = round(refs_fs * 1.35)

    # Lay the whole card out first, so the height it actually occupies is measured
    # rather than estimated — the first version guessed and centred it wrong.
    runs = []          # (text, fill, size, weight, advance-after)
    runs.append((gif.get("output", ""), INK, name_fs, "700", round(name_fs * 0.92)))
    meta = " · ".join(str(v) for v in (
        f"{gif.get('duration_s')}s", gif.get("ratio"), gif.get("loop")) if v)
    runs.append((meta, INK, meta_fs, "400", round(name_fs * 0.62)))
    runs.append((None, None, 0, None, round(name_fs * 0.72)))   # the rule
    for text in wrap(gif.get("brief", ""), tw, body_fs):
        runs.append((text, INK, body_fs, "400", body_lh))
    alt = gif.get("alt")
    if alt:
        runs[-1] = runs[-1][:4] + (round(name_fs * 1.05),)
        runs.append(("IF THAT CANNOT BE SHOT", DIM, refs_fs, "700",
                     round(refs_fs * 1.75)))
        for text in wrap(alt, tw, body_fs):
            runs.append((text, DIM, body_fs, "400", body_lh))
    runs[-1] = runs[-1][:4] + (round(name_fs * 0.95),)
    for text in wrap(gif.get("refs", ""), tw, refs_fs):
        runs.append((text, DIM, refs_fs, "400", refs_lh))

    total = sum(r[4] for r in runs[:-1]) + runs[-1][2]
    top = pad + inner + round(short * 0.06)
    y = max(top + name_fs, (H - total) // 2 + name_fs)

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {W} {H}">',
           f'<rect width="{W}" height="{H}" fill="{BG}"/>',
           f'<rect x="{pad}" y="{pad}" width="{W - 2 * pad}" height="{H - 2 * pad}" '
           f'fill="none" stroke="{BORDER}" stroke-width="{max(2, round(W / 600))}"/>']
    for text, fill, size, weight, advance in runs:
        if text is None:
            ry = y - round(advance * 0.55)
            out.append(f'<line x1="{tx}" y1="{ry}" x2="{tx + tw}" y2="{ry}" '
                       f'stroke="{DIM}" stroke-width="1" opacity="0.45"/>')
        else:
            out.append(f'<text x="{tx}" y="{y}" fill="{fill}" font-size="{size}" '
                       f'font-family="{FONT}" font-weight="{weight}" '
                       f'letter-spacing="0.4">{esc(text)}</text>')
        y += advance
    out.append("</svg>")
    return "\n".join(out) + "\n"


def session_plates(session_dir, skipped):
    """[(absolute path, svg text)] for every ADR-028 gif verdict in the session."""
    path = os.path.join(session_dir, "prompts.json")
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)
    out = []
    for slot in doc.get("slots", []):
        gif = slot.get("gif") or {}
        if not gif.get("eligible"):
            continue
        asset = gif.get("asset")
        # Only ADR-028 sessions. Earlier ones carry a five-line plate PROMPT and an
        # asset with a render's extension; they are left standing unmigrated, the
        # treatment ADR-024 gave page 13, and generating over them would write SVG
        # into a filename that claims to be a render.
        if not asset or not asset.endswith("--brief.svg") or not gif.get("brief"):
            skipped.append(os.path.basename(session_dir))
            continue
        out.append((os.path.join(session_dir, "plates", asset), plate_svg(gif)))
    return out


def main(argv):
    check = "--check" in argv
    targets = [a for a in argv if not a.startswith("--")]
    if targets:
        dirs = [os.path.abspath(t) for t in targets]
    else:
        dirs = [os.path.join(SESSIONS, d) for d in sorted(os.listdir(SESSIONS))
                if os.path.isdir(os.path.join(SESSIONS, d))]

    wrote = unchanged = stale = 0
    skipped = []
    for d in dirs:
        for path, svg in session_plates(d, skipped):
            current = None
            if os.path.exists(path):
                with open(path, encoding="utf-8") as f:
                    current = f.read()
            if current == svg:
                unchanged += 1
                continue
            if check:
                stale += 1
                print(f"STALE {os.path.relpath(path, ROOT)}")
                continue
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(svg)
            wrote += 1
            print(f"wrote {os.path.relpath(path, ROOT)}")
    if skipped:
        for name in sorted(set(skipped)):
            print(f"skip  {name}: pre-ADR-028 gif block, left unmigrated")
    if check:
        print(f"{stale} stale, {unchanged} current")
        return 1 if stale else 0
    print(f"wrote {wrote} plate(s), {unchanged} unchanged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

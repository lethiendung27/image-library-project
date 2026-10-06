#!/usr/bin/env python3
"""Measure how far apart the compositions of a set are, and against a corpus.

WHY THIS EXISTS
---------------
`registry/pdp-dr-types/03-spec-overlay.md` has legislated a composition-spread floor since
ADR-132 — *checked with a 16x16 luma signature: any pair under 25 is a repeat* — and quoted
numbers from it in four decisions (10.7, 14.7, 19.1, 15.9, 42.8, 30.3). No tool computed them.
Every one of those figures was produced ad hoc and thrown away, so no later round could be
compared with an earlier one on the same arithmetic, and the clause could not be checked by
anybody but its author. This is that arithmetic, written down once.

WHAT IT MEASURES
  Each image becomes a 16x16 greyscale thumbnail. The distance between two images is the mean
  absolute difference of those 256 values, on the 0-255 scale. Identical framing scores 0.
  The number that matters is the CLOSEST pair in a set: a set is as repetitive as its most
  alike two frames, not as its average.

  It says nothing about whether a frame is good, and nothing about colour or subject. Two
  frames can score 80 apart and argue the same thing. Read the frames.

Usage:
  python3 scripts/compo-spread.py IMAGE [IMAGE ...]       # one set: closest pair, median, top 5
  python3 scripts/compo-spread.py --corpus DIR            # the same, over a folder
  python3 scripts/compo-spread.py --selftest              # prove the metric is live
"""
import itertools
import os
import sys

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    print("ERROR this script needs Pillow: python3 -m pip install --user Pillow", file=sys.stderr)
    sys.exit(2)

EXTS = (".jpg", ".jpeg", ".png", ".webp")
GRID = 16


def signature(path):
    im = Image.open(path).convert("L").resize((GRID, GRID), Image.LANCZOS)
    return list(im.getdata())


def distance(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) / len(a)


def report(paths, label):
    sigs = []
    for p in paths:
        try:
            sigs.append((os.path.basename(p), signature(p)))
        except Exception as exc:  # unreadable file: say so, do not drop it silently
            print(f"  SKIPPED {os.path.basename(p)}: {exc}", file=sys.stderr)
    if len(sigs) < 2:
        print(f"{label}: need at least two readable images, got {len(sigs)}")
        return 2
    pairs = sorted(
        (distance(a[1], b[1]), a[0], b[0]) for a, b in itertools.combinations(sigs, 2)
    )
    print(f"{label}: n={len(sigs)}  pairs={len(pairs)}")
    for d, a, b in pairs[:5]:
        print(f"  {d:6.1f}   {a[:44]:<44}  {b[:44]}")
    print(f"  closest={pairs[0][0]:.1f}   median={pairs[len(pairs)//2][0]:.1f}")
    return 0


def selftest():
    """A clean number from an untested checker is not evidence. Prove both ends."""
    from PIL import ImageDraw

    a = Image.new("L", (400, 300), 20)
    ImageDraw.Draw(a).rectangle([40, 40, 200, 260], fill=230)
    b = a.copy()
    c = Image.new("L", (400, 300), 230)
    ImageDraw.Draw(c).rectangle([240, 20, 380, 120], fill=10)
    sa, sb, sc = (list(x.resize((GRID, GRID), Image.LANCZOS).getdata()) for x in (a, b, c))
    same, different = distance(sa, sb), distance(sa, sc)
    print(f"identical pair  -> {same:.1f}  (must be 0.0)")
    print(f"opposed pair    -> {different:.1f}  (must be well above the 25 floor)")
    ok = same == 0.0 and different > 25
    print("SELFTEST PASS" if ok else "SELFTEST FAIL")
    return 0 if ok else 1


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--selftest":
        return selftest()
    if argv[0] == "--corpus":
        d = argv[1]
        paths = sorted(
            os.path.join(d, f) for f in os.listdir(d) if f.lower().endswith(EXTS)
        )
        return report(paths, os.path.basename(d.rstrip("/")))
    return report(argv, "set")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

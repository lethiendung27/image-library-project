#!/usr/bin/env python3
"""Measure a render's colour against the band the owner's own reference stills sit in.

WHY THIS EXISTS
---------------
Three hero sets in a row were failed by the owner on colour, each time in different words:
"fake, dull, unfriendly" (ADR-104), "too AI, too yellowish" (ADR-107), "still fake" (ADR-108).
Each verdict was true and none of them was a number, so every patch was a guess at which way to
move. This prints the numbers, beside the band measured on `image-library-assets/stills/`, the
corpus of real marketing photographs the owner selected. The band is a description of that
corpus, not a target to optimise: a frame outside it is worth a second look, and a frame inside
it can still be wrong.

WHAT IT MEASURES, per image
  sat        mean HSV saturation
  val        mean HSV value
  colour     colourfulness, Hasler and Suesstrunk's metric: sqrt(sd(rg)^2+sd(yb)^2) + 0.3*sqrt(mean(rg)^2+mean(yb)^2)
  contrast   standard deviation of luminance
  R-B        warm cast: mean red minus mean blue
  drift%     white point: R-B of the brightest tenth, as a percentage of its own level
  outside%   share of saturated pixels outside the 20-70 degree orange band
  texture    mean edge energy, which falls when skin and fabric come back plastic

Usage:
  python3 scripts/frame-colour.py IMAGE [IMAGE ...]        # measure, against the stored band
  python3 scripts/frame-colour.py --corpus DIR [-n 60]     # re-measure the band from a folder
"""
import colorsys
import math
import os
import random
import statistics
import sys

try:
    from PIL import Image, ImageFilter, ImageStat
except ImportError:  # pragma: no cover
    print("ERROR this script needs Pillow: python3 -m pip install --user Pillow", file=sys.stderr)
    sys.exit(2)

# Measured 2026-09-18 on 60 of the 131 stills in image-library-assets/stills/ (ADR-108).
# Each entry is (median, 10th percentile, 90th percentile).
BAND = {
    "sat": (0.23, 0.05, 0.46),
    "val": (0.75, 0.29, 0.90),
    "colour": (38.6, 22.2, 81.8),
    "contrast": (52.0, 31.4, 79.5),
    "R-B": (9.9, -46.6, 40.1),
    "drift%": (0.1, -11.9, 8.9),
    "outside%": (68.0, 2.2, 100.0),
    "texture": (21.8, 12.2, 34.8),
}
KEYS = list(BAND)


def measure(path, side=320):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    im = im.resize((side, max(1, int(side * h / w))))
    px = list(im.getdata())
    n = len(px)
    sat = val = warm = 0.0
    rg, yb, lum, hues, bright = [], [], [], [], []
    for r, g, b in px:
        hue, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        sat += s
        val += v
        warm += r - b
        rg.append(r - g)
        yb.append(0.5 * (r + g) - b)
        L = 0.2126 * r + 0.7152 * g + 0.0722 * b
        lum.append(L)
        bright.append((L, r, g, b))
        if s > 0.15:
            hues.append(hue * 360)

    def mean(a):
        return sum(a) / len(a)

    def sd(a):
        m = mean(a)
        return math.sqrt(sum((x - m) ** 2 for x in a) / len(a))

    bright.sort(reverse=True)
    top = bright[: max(1, n // 10)]
    wr, wg, wb = mean([p[1] for p in top]), mean([p[2] for p in top]), mean([p[3] for p in top])
    return {
        "sat": sat / n,
        "val": val / n,
        "colour": math.sqrt(sd(rg) ** 2 + sd(yb) ** 2) + 0.3 * math.sqrt(mean(rg) ** 2 + mean(yb) ** 2),
        "contrast": sd(lum),
        "R-B": warm / n,
        "drift%": 100.0 * (wr - wb) / max(1.0, (wr + wg + wb) / 3),
        "outside%": 100.0 * sum(1 for x in hues if not 20 <= x <= 70) / max(1, len(hues)),
        "texture": ImageStat.Stat(im.convert("L").filter(ImageFilter.FIND_EDGES)).mean[0],
    }


def corpus(folder, n):
    files = [f for f in sorted(os.listdir(folder))
             if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]
    random.seed(7)
    sample = random.sample(files, min(n, len(files)))
    rows = []
    for f in sample:
        try:
            rows.append(measure(os.path.join(folder, f), side=200))
        except Exception as e:
            print(f"skipped {f}: {e}", file=sys.stderr)
    print(f"{len(rows)} of {len(files)} images in {folder}")
    print(f"{'metric':10} {'median':>8} {'10th':>8} {'90th':>8}")
    for k in KEYS:
        v = sorted(r[k] for r in rows)
        q = lambda p: v[int(p * (len(v) - 1))]
        print(f"{k:10} {statistics.median(v):8.2f} {q(0.1):8.2f} {q(0.9):8.2f}")


def main(argv):
    if "--corpus" in argv:
        i = argv.index("--corpus")
        folder = argv[i + 1]
        n = int(argv[argv.index("-n") + 1]) if "-n" in argv else 60
        corpus(folder, n)
        return 0
    images = [a for a in argv if not a.startswith("-")]
    if not images:
        print(__doc__.split("Usage:")[1], file=sys.stderr)
        return 2
    print(f"{'image':34} " + " ".join(f"{k:>9}" for k in KEYS))
    out = 0
    for path in images:
        m = measure(path)
        cells = []
        for k in KEYS:
            _med, lo, hi = BAND[k]
            flag = " " if lo <= m[k] <= hi else "*"
            cells.append(f"{m[k]:8.2f}{flag}")
            out += flag == "*"
        print(f"{os.path.basename(path)[:34]:34} " + " ".join(cells))
    print("\n* sits outside the 10th-90th percentile of the owner's own stills. "
          "Read the frame before believing the number.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

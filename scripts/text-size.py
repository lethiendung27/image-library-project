#!/usr/bin/env python3
"""Measure the words and drawn lines of a render as a phone will show them.

WHY THIS EXISTS
---------------
The owner reads section images on a phone first (2026-09-18, ADR-112: "chữ và các yếu tố đồ hoạ
cần to rõ ràng hơn. mobile first"). A render's words can be spelled right, set once and placed
well and still be unreadable, because a 1,200-pixel frame is shown 224-358 pixels wide on a
phone. So this prints what matters there: how tall a capital is on the screen, how thick a line
is, and how hard the words stand off their ground.

Boxes are placed by eye, as `scripts/frame-colour.py`'s reading is; every number is computed from
the pixels. A text box should hold one line of words and a little of the ground around it; a cap
box should hold one capital letter with no descender under it.

  cap       the capital's height in the render, and on the phone
  band      ascender to descender of the whole line
  contrast  WCAG ratio between the words' colour and the ground right around them
  stroke    a line's thickness, read down one column across it

On the phone, a field shows the render at a width the template fixes. `--phone` is that width in
CSS pixels and `--fit` how the render goes in: `cover` crops a wider render to the field's shape
(scale = phone / the render's shorter side, for a square field), `width` scales by width.

Targets, from ADR-112: a tag's capitals at least 18 px on the phone — the owner's own gallery
titles on the same page measure 24-25 — a label's at least 12, a line at least 3, and contrast at
least 4.5:1. They are checked and reported, never written into a prompt as numbers.

Usage:
  python3 scripts/text-size.py IMAGE --phone 358 --fit cover \\
      --tag "x0,y0,x1,y1" --cap "x0,y0,x1,y1" [--dark] \\
      --label "x0,y0,x1,y1" --cap "x0,y0,x1,y1" [--dark] \\
      --line "x,y0,y1" [--dark]
Each --tag or --label takes the --cap that follows it. --dark marks dark words or a dark line on
a lighter ground; the default is light on darker. Exit 1 when any reading misses its target.
"""
import sys

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    print("ERROR this script needs Pillow: python3 -m pip install --user Pillow", file=sys.stderr)
    sys.exit(2)

TARGET = {"tag": 18.0, "label": 12.0, "line": 3.0, "contrast": 4.5}


def lum(rgb):
    def ch(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def box_of(s):
    v = [int(x) for x in s.split(",")]
    if len(v) != 4 or v[2] <= v[0] or v[3] <= v[1]:
        raise ValueError(f"a box is x0,y0,x1,y1 with x1>x0 and y1>y0, got {s!r}")
    return tuple(v)


def text_reading(img, box, light):
    """(band in px, contrast) for the words inside box."""
    im = img.crop(box)
    W, H = im.size
    L = [[lum(im.getpixel((x, y))) for x in range(W)] for y in range(H)]
    flat = sorted(v for row in L for v in row)
    n = len(flat)
    if light:
        words = sum(flat[int(n * 0.93):]) / max(1, n - int(n * 0.93))
        ground = flat[int(n * 0.40)]
    else:
        words = sum(flat[: int(n * 0.07)]) / max(1, int(n * 0.07))
        ground = flat[int(n * 0.60)]
    contrast = (max(words, ground) + 0.05) / (min(words, ground) + 0.05)
    cut = ground + 0.6 * (words - ground)
    on = [y for y, row in enumerate(L)
          if sum(1 for v in row if ((v >= cut) if light else (v <= cut))) >= 3]
    return ((on[-1] - on[0] + 1) if on else 0), contrast


def stroke_reading(img, x, y0, y1, light):
    col = [lum(img.getpixel((x, y))) for y in range(y0, y1)]
    base = sorted(col)[len(col) // 2]
    peak = max(col) if light else min(col)
    cut = base + 0.5 * (peak - base)
    return sum(1 for v in col if ((v >= cut) if light else (v <= cut)))


def main(argv):
    if not argv or argv[0].startswith("--"):
        print(__doc__.split("Usage:")[1].split("Each --tag")[0], file=sys.stderr)
        return 2
    img = Image.open(argv[0]).convert("RGB")
    phone, fit = None, "cover"
    items, pending, i = [], None, 1
    try:
        while i < len(argv):
            a = argv[i]
            if a == "--phone":
                phone = float(argv[i + 1]); i += 2
            elif a == "--fit":
                fit = argv[i + 1]; i += 2
                if fit not in ("cover", "width"):
                    raise ValueError("--fit is cover or width")
            elif a in ("--tag", "--label"):
                pending = {"kind": a[2:], "box": box_of(argv[i + 1]), "light": True}
                items.append(pending); i += 2
            elif a == "--cap":
                if pending is None or pending["kind"] == "line":
                    raise ValueError("--cap follows a --tag or a --label")
                pending["cap"] = box_of(argv[i + 1]); i += 2
            elif a == "--line":
                x, y0, y1 = (int(v) for v in argv[i + 1].split(","))
                pending = {"kind": "line", "col": (x, y0, y1), "light": True}
                items.append(pending); i += 2
            elif a == "--dark":
                if pending is None:
                    raise ValueError("--dark follows the reading it marks")
                pending["light"] = False; i += 1
            else:
                raise ValueError(f"unknown argument {a!r}")
    except (IndexError, ValueError) as e:
        print(f"ERROR {e}", file=sys.stderr)
        return 2
    if phone is None:
        print("ERROR --phone is the field's width on the phone, in CSS pixels", file=sys.stderr)
        return 2
    scale = phone / (min(img.size) if fit == "cover" else img.size[0])
    print(f"{argv[0].rsplit('/', 1)[-1]}  {img.size[0]}x{img.size[1]}  shown {phone:g} px wide ({fit}), "
          f"scale {scale:.3f}")
    misses = 0
    for it in items:
        if it["kind"] == "line":
            w = stroke_reading(img, *it["col"], it["light"])
            ok = w * scale >= TARGET["line"]
            misses += not ok
            print(f"  line   stroke {w} px -> {w * scale:.1f} px on the phone"
                  f"{'' if ok else '   MISS (target ' + str(TARGET['line']) + ')'}")
            continue
        if "cap" not in it:
            print(f"ERROR a --{it['kind']} has no --cap after it", file=sys.stderr)
            return 2
        band, contrast = text_reading(img, it["box"], it["light"])
        cap, _ = text_reading(img, it["cap"], it["light"])
        on_phone = cap * scale
        ok_size = on_phone >= TARGET[it["kind"]]
        ok_con = contrast >= TARGET["contrast"]
        misses += (not ok_size) + (not ok_con)
        print(f"  {it['kind']:6} cap {cap} px ({100 * cap / img.size[1]:.1f}% of the height), band {band} px"
              f" -> cap {on_phone:.1f} px on the phone"
              f"{'' if ok_size else '   MISS (target ' + str(TARGET[it['kind']]) + ')'}"
              f";  contrast {contrast:.1f}:1{'' if ok_con else '   MISS (target 4.5:1)'}")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

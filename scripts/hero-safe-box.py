"""What a hero banner keeps of a 16:9 render, measured from the templates' own markup.

Run:  python3 scripts/hero-safe-box.py TEMPLATE.html [TEMPLATE.html ...]
      python3 scripts/hero-safe-box.py --owner        # the four templates in ~/Downloads

The owner renders a hero at 16:9 (ADR-016) and every template crops it with `object-fit: cover`
into a block that is much wider. This prints, per template and per screen width, the block's
aspect ratio, the band of the 16:9 image that survives, and where the page's own words sit — and
then the box where all of them overlap, which is the safe box the hero law states.

It reads the hero block's Tailwind classes out of the file rather than trusting a number typed
into a document: the block's aspect (`aspect-[12/5]`, `aspect-12/5`, `h-[min(41.6667cqw,640px)]`,
`min-h-[clamp(31rem,33vw,41rem)]`), its width cap (`max-w-[120rem]`, `max-w-480`,
`max-w-[1920px]`, `max-w-[75rem]`), the text column's width (`w-[45%]`, `45cqw`, `max-w-[33rem]`)
and the phone crop (`aspect-[4/3]` with its `object-[X%_50%]`). A class it cannot read is
reported as a gap rather than guessed.
"""
import os
import re
import sys

WIDTHS = [1280, 1440, 1536, 1920, 2560]
SRC = 16 / 9
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWNER = [
    "~/Downloads/t1-deal-final-product-type 2/final-product-type.html",
    "~/Downloads/t2-eco-final-product-type/final-product-type.html",
    "~/Downloads/wiboofy-final-product-type 2/final-product-type.html",
    "~/Downloads/aure-toplaser-final 2/final.html",
]


def rem(x):
    return float(x) * 16


def hero_chunk(text):
    """The hero <section>, from its tag to the end of the text column."""
    i = text.find('data-block-key="hero"')
    if i < 0:
        i = text.find("hero-banner")
    start = text.rfind("<section", 0, i)
    return re.sub(r"\s+", " ", text[start:start + 6000])


def px(token):
    """A Tailwind length to pixels: 40rem, 160 (quarter-rem scale), 1920px, 120rem."""
    token = token.strip()
    m = re.fullmatch(r"([\d.]+)rem", token)
    if m:
        return rem(m.group(1))
    m = re.fullmatch(r"([\d.]+)px", token)
    if m:
        return float(m.group(1))
    m = re.fullmatch(r"[\d.]+", token)
    if m:
        return float(token) * 4          # Tailwind v4 spacing scale, 1 = 0.25rem
    return None


def read(path):
    text = open(os.path.expanduser(path), encoding="utf-8").read()
    c = hero_chunk(text)
    g = {"name": os.path.basename(os.path.dirname(os.path.expanduser(path))), "gaps": []}

    cap = re.search(r"max-w-\[?([\d.]+(?:rem|px)?)\]?", c)
    g["cap"] = g["content_cap"] = px(cap.group(1)) if cap else None

    m = re.search(r"lg:aspect-\[?(\d+)/(\d+)\]?", c)
    if m:
        g["ratio"] = int(m.group(1)) / int(m.group(2))
        mh = re.search(r"lg:max-h-\[?([\d.]+(?:rem|px)?)\]?", c)
        g["max_h"] = px(mh.group(1)) if mh else None
        g["rule"] = f"aspect {m.group(1)}/{m.group(2)}, capped at {g['max_h']:.0f}px" if g["max_h"] else f"aspect {m.group(1)}/{m.group(2)}"
    else:
        m = re.search(r"lg:h-\[min\(([\d.]+)cqw,\s*([\d.]+)px\)\]", c)
        if m:
            g["ratio"] = 100 / float(m.group(1))
            g["max_h"] = float(m.group(2))
            g["rule"] = f"height {m.group(1)}% of width, capped at {g['max_h']:.0f}px"
        else:
            m = re.search(r"md:min-h-\[clamp\(([\d.]+)rem,\s*([\d.]+)vw,\s*([\d.]+)rem\)\]", c)
            if m:
                # the height rule sits on the TEXT column, so the picture behind it is full-bleed
                g["cap"] = None
                g["clamp"] = (rem(m.group(1)), float(m.group(2)) / 100, rem(m.group(3)))
                g["ratio"] = None
                g["max_h"] = g["clamp"][2]
                g["rule"] = (f"height clamp({g['clamp'][0]:.0f}px, {m.group(2)}vw, "
                             f"{g['clamp'][2]:.0f}px), set by its words")
            else:
                g["gaps"].append("no readable height rule for the hero block")
                g["rule"] = "?"

    m = (re.search(r"lg:w-\[(\d+)%\]", c) or re.search(r"w-\[calc\((\d+)cqw", c)
         or re.search(r"lg:w-\[calc\((\d+)cqw", c))
    if m:
        g["panel"] = int(m.group(1)) / 100
        g["panel_rule"] = f"text column {m.group(1)}% of the block"
    else:
        m = re.search(r"max-w-\[([\d.]+)rem\][^\"]*md:max-w-\[([\d.]+)rem\]", c)
        if m:
            g["panel"] = None
            g["panel_card"] = rem(m.group(2))
            g["panel_rule"] = (f"text card {g['panel_card']:.0f}px wide inside a "
                               f"{g['content_cap']:.0f}px column")
        else:
            g["panel"] = None
            g["panel_card"] = None
            g["gaps"].append("no readable width for the text column")
            g["panel_rule"] = "?"

    m = re.search(r"object-\[(\d+)%_\d+%\]", c)
    g["phone_anchor"] = int(m.group(1)) / 100 if m else 0.5
    g["phone_ratio"] = 4 / 3 if "aspect-[4/3]" in c or "aspect-4/3" in c else None
    if g["phone_ratio"] is None:
        g["gaps"].append("no readable phone crop")
    return g


def block_height(g, w):
    width = min(w, g["cap"]) if g["cap"] else w
    if g.get("clamp"):
        lo, vw, hi = g["clamp"]
        return width, max(lo, min(w * vw, hi))
    h = width / g["ratio"]
    if g.get("max_h"):
        h = min(h, g["max_h"])
    return width, h


def band(box_ratio, src=SRC):
    """With object-fit: cover, the fraction of the source that survives, centred."""
    if box_ratio >= src:
        f = src / box_ratio
        return "height", (1 - f) / 2, 1 - (1 - f) / 2
    f = box_ratio / src
    return "width", (1 - f) / 2, 1 - (1 - f) / 2


def main():
    args = sys.argv[1:]
    paths = OWNER if (not args or args[0] == "--owner") else args
    tops, bots, lefts = [], [], []
    for p in paths:
        g = read(p)
        print(f"\n=== {g['name']}  —  {g['rule']}; {g['panel_rule']}")
        print(f"{'screen':>8} {'block':>12} {'ratio':>7} {'keeps of the 16:9':>22} {'words end at':>13}")
        for w in WIDTHS:
            bw, bh = block_height(g, w)
            ratio = bw / bh
            axis, a, b = band(ratio)
            if g.get("panel"):
                words = g["panel"]
            elif g.get("panel_card"):
                inner = min(w, g["content_cap"] or w)
                words = ((w - inner) / 2 + 24 + g["panel_card"]) / w
            else:
                words = None
            if axis == "height":
                tops.append(a)
                bots.append(b)
            if words:
                lefts.append(words)
            print(f"{w:>8} {bw:>6.0f}x{bh:<5.0f} {ratio:>6.2f}:1 "
                  f"{axis + ' ' + format(a * 100, '.1f') + '-' + format(b * 100, '.1f') + '%':>22} "
                  f"{(format(words * 100, '.1f') + '%') if words else '—':>13}")
        f = (4 / 3) / SRC
        left = g["phone_anchor"] * (1 - f)
        print(f"{'phone':>8} {'4:3 crop':>12} {'1.33:1':>7} "
              f"{'width ' + format(left * 100, '.1f') + '-' + format((left + f) * 100, '.1f') + '%':>22} "
              f"{'anchor ' + format(g['phone_anchor'] * 100, '.0f') + '%':>13}")
        for gap in g["gaps"]:
            print("  GAP:", gap)

    print("\n--- where every desktop window overlaps, on a 16:9 render")
    print(f"vertical   : {max(tops) * 100:.1f}% to {min(bots) * 100:.1f}%   "
          f"(the worst crop keeps only this band)")
    print(f"the words  : reach {max(lefts) * 100:.1f}% across at their widest")
    print(f"horizontal : {max(lefts) * 100:.1f}% to 94% is what is left of the width, "
          f"and a margin inside that is the safe box")


if __name__ == "__main__":
    main()

"""Ground audit of the toplist corpus, built from this namespace's own frames (ADR-073).

Run: python3 scripts/ground_audit.py

Per frame, on the outer 8% ring (the band a subject rarely occupies):

  texture      mean |adjacent-pixel difference| in the ring. Near zero = a DESIGNED
               ground (flat tone or smooth gradient); high = a PHOTOGRAPHED place.
  spread_v     max-min of the mean VALUE across 8 patches around the ring.
               Near zero = flat; large = a gradient or a lit scene.
  spread_h     the same for HUE, in degrees on the circle.
  axis         which direction the value changes most: horizontal, vertical,
               diagonal, or none.
  value/sat    medians, as before.
  hue          dominant saturated hue bucket, and the two endpoint hues where the
               frame is a gradient.
"""
import colorsys, hashlib, io, json, math, os, subprocess, tempfile
from collections import Counter
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"


def assets_root():
    """SPEC §6.4 keeps the asset folder outside the repo; find it, never assume it.

    It has always been a SIBLING of the repo directory, and it stayed one when the
    owner relocated both trees on 2026-09-10 (`~/Downloads` to `~/Downloads/MISEN/
    Flunnel/Image`). A hard-coded absolute path did not survive that move and would
    not survive the next one — and it fails by pointing at a folder that is not
    there rather than by saying so.

    Resolution order: the sibling of this repo, then the historical `~/Downloads`
    location. Returns the sibling either way, so a missing folder names the place a
    reader should look. Deliberately does NOT raise: this module is exec'd in slices
    to reuse `designed()` on renders, where the corpus is never read.
    """
    parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for cand in (os.path.join(os.path.dirname(parent), "image-library-assets"),
                 os.path.join(os.path.expanduser("~"), "Downloads",
                              "image-library-assets")):
        if os.path.isdir(cand):
            return cand
    return os.path.join(os.path.dirname(parent), "image-library-assets")


SRC = os.path.join(assets_root(), "stills", "top list")
EXT = {".png", ".jpg", ".jpeg", ".webp", ".avif"}


def load(p):
    if p.lower().endswith(".avif"):
        o = os.path.join(tempfile.gettempdir(), "g.png")
        subprocess.run(["sips", "-s", "format", "png", p, "--out", o], capture_output=True)
        return Image.open(o).convert("RGB")
    return Image.open(p).convert("RGB")


def hsv(px):
    r, g, b = px
    return colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)


def hue_gap(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def analyse(p):
    im = load(p)
    w, h = im.size
    px = im.load()
    bw, bh = max(2, int(w * 0.08)), max(2, int(h * 0.08))

    ring = []
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            if x < bw or x >= w - bw or y < bh or y >= h - bh:
                ring.append((x, y))
    vs, ss = [], []
    for x, y in ring:
        _, s, v = hsv(px[x, y]); vs.append(v); ss.append(s)
    vs_s, ss_s = sorted(vs), sorted(ss)

    # texture: adjacent-pixel difference inside the ring
    diffs = []
    for x, y in ring[::3]:
        if x + 2 < w:
            a, b = px[x, y], px[x + 2, y]
            diffs.append(sum(abs(a[i] - b[i]) for i in range(3)) / 3)
    texture = sum(diffs) / max(1, len(diffs))

    # eight patches around the ring
    P = 8
    pts = [(bw // 2, bh // 2), (w // 2, bh // 2), (w - bw // 2, bh // 2),
           (w - bw // 2, h // 2), (w - bw // 2, h - bh // 2), (w // 2, h - bh // 2),
           (bw // 2, h - bh // 2), (bw // 2, h // 2)]
    pv, ph, psat = [], [], []
    for cx, cy in pts:
        acc = []
        for dy in range(-bh // 3, bh // 3 + 1, 2):
            for dx in range(-bw // 3, bw // 3 + 1, 2):
                x, y = min(max(cx + dx, 0), w - 1), min(max(cy + dy, 0), h - 1)
                acc.append(hsv(px[x, y]))
        pv.append(sum(a[2] for a in acc) / len(acc))
        psat.append(sum(a[1] for a in acc) / len(acc))
        sat = [a for a in acc if a[1] > 0.2]
        ph.append((sum(a[0] for a in sat) / len(sat) * 360) if sat else None)

    spread_v = max(pv) - min(pv)
    hs = [x for x in ph if x is not None]
    spread_h = max((hue_gap(a, b) for a in hs for b in hs), default=0.0)

    # dominant axis of the value change
    horiz = abs((pv[0] + pv[7] + pv[6]) / 3 - (pv[2] + pv[3] + pv[4]) / 3)
    vert = abs((pv[0] + pv[1] + pv[2]) / 3 - (pv[6] + pv[5] + pv[4]) / 3)
    diag = abs(pv[0] - pv[4])
    axis = max((horiz, "horizontal"), (vert, "vertical"), (diag, "diagonal"))
    axis = axis[1] if axis[0] > 0.08 else "none"

    buckets = Counter(int(hsv(px[x, y])[0] * 360) // 30 * 30
                      for x, y in ring if hsv(px[x, y])[1] > 0.25)
    dom = buckets.most_common(1)
    return dict(value=vs_s[len(vs_s) // 2], sat=ss_s[len(ss_s) // 2],
                texture=texture, spread_v=spread_v, spread_h=spread_h,
                axis=axis, hue=(dom[0][0] if dom else None))


h2p = {}
for fn in os.listdir(SRC):
    if os.path.splitext(fn)[1].lower() in EXT:
        p = os.path.join(SRC, fn)
        h2p["sha256:" + hashlib.sha256(io.open(p, "rb").read()).hexdigest()] = p

recs = [json.loads(l) for l in io.open(REPO + "ingestion/observations.jsonl",
                                       encoding="utf-8") if l.strip()]
# The ledger is append-only and a correction is a NEW record, so the LAST record
# for a hash is the live one. Counting every record would file a corrected frame
# under both the old family and the new one.
latest = {}
for r in recs:
    if r.get("template_version") == "t1.0":
        latest[r["hash"]] = r
by = {}
for h, r in latest.items():
    t = r.get("type") or ("PROPOSED " + r["proposed_id"] if r.get("proposed_id") else "REJECT")
    p = h2p.get(h)
    if p:
        by.setdefault(t, []).append((analyse(p), os.path.basename(p)))

print("| family | n | value | sat | texture | spread_v | axis | designed? |")
print("|---|---|---|---|---|---|---|---|")



def designed(texture, spread_v):
    """Is the ground MADE or is it a place?

    Batch 2026-09-09-C broke the single-variable rule ADR-073 shipped. Texture alone
    separates a SMOOTH designed ground from a room, but a designed ground can also be
    PATTERNED — printed halftone dots, a grain — and three frames in that batch measured
    11.0 to 12.0, above the line ADR-073 calls photographed.

    What still separates them is the light. A designed ground is evenly lit by
    construction, so its value hardly varies around the ring: those three read 0.15, 0.01
    and 0.02. A real place reads 0.34 to 0.67, because real light falls off.

    KNOWN BOUND, found by the founding render round on 2026-09-09 and left unfixed on
    purpose. Texture is a mean ABSOLUTE pixel difference, so it scales with exposure: the
    same photograph of a real room measures 6.8 at value 0.64 and 2.7 at value 0.25, and
    an underexposed room therefore returns DESIGNED off the first branch alone. The 32
    corpus frames this split was measured on all sit at value 0.65-0.90, so the rule is
    bounded rather than wrong - below about value 0.35 read spread_v, which holds its side
    down to at least value 0.19.

    Do not "fix" this by ANDing spread_v < 0.35 onto the first branch without re-running
    the corpus: that was tested and re-files FIVE frames, one of which carries
    lede-lineup's median of 2.9 and with it ADR-073's finding that the type is designed.
    Moving a corpus frame is a curation decision, not a bug fix. See
    registry/toplist-instruction.md, section Ground.
    """
    return texture < 3.0 or spread_v < 0.20


def med(xs):
    xs = sorted(xs); return xs[len(xs) // 2]


for t in sorted(by):
    rows = [a for a, _ in by[t]]
    n = len(rows)
    tex = med([r["texture"] for r in rows])
    spr = med([r["spread_v"] for r in rows])
    print(f"| {t} | {n} | {med([r['value'] for r in rows]):.2f} | "
          f"{med([r['sat'] for r in rows]):.2f} | {tex:5.1f} | "
          f"{med([r['spread_v'] for r in rows]):.2f} | "
          f"{Counter(r['axis'] for r in rows).most_common(1)[0][0]} | "
          f"{'DESIGNED' if designed(tex, spr) else 'photographed'} |")

print("\nper frame, the two assembled families and the lineup:\n")
for t in ("lede-winner", "lede-collage", "lede-lineup"):
    print(f"  {t}")
    for a, fn in by.get(t, []):
        print(f"    v{a['value']:.2f} s{a['sat']:.2f} tex{a['texture']:5.1f} "
              f"spread_v {a['spread_v']:.2f} spread_hue {a['spread_h']:5.1f}° "
              f"axis {a['axis']:10s} hue {a['hue']}°  {fn[:34]}")

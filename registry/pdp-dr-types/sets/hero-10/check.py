"""Check hero-10 against the hero law of `registry/pdp-dr-instruction.md` and ADR-136.

The six fixed sentences, the two lock lines and the LP2 product block are READ OUT OF THE LAW, so
a law reworded fails this set instead of leaving it quietly stale. On top of hero-09's checks this
one adds the rule ADR-131 exists for, because NO PHOTOGRAPH OF THIS PRODUCT IS ON DISK:

  BANDS    every prompt NAMES a real surface that fills the top and the bottom (ADR-123). An empty
           region places nothing, and that is how two of hero-07's three lost their faces.
  ACROSS   every prompt says where across the picture the receiver sits. hero-07 left it to the
           fixed sentence's `just past the centre` and got 50%, five points outside the box.
  COLOUR   no frame is dark, and the three clear colours are carried one each (ADR-119).
  ANATOMY  no prompt describes the product's shape, colour, housing, buttons, lenses or display.
           It names only the two parts the page's own product.box names - the hub and the rear
           camera module - and the mandated product block plus the attached photograph carry the
           rest. Six of nine frames once drew the wrong product from asserted anatomy (ADR-131).

Usage, from the repo root: python3 registry/pdp-dr-types/sets/hero-10/check.py [prompts.md]
Exits 1 on any failure.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
LAW = os.path.join(ROOT, "registry", "pdp-dr-instruction.md")
PATH = os.path.join(HERE, "prompts.md")
text = io.open(sys.argv[1] if len(sys.argv) > 1 else PATH, encoding="utf-8").read()
law = io.open(LAW, encoding="utf-8").read()

GATE = 1800


def norm(x):
    "collapse whitespace so line-wrapping cannot hide or fake a match"
    return re.sub(r"\s+", " ", x).strip()


def block_after(marker, src=None):
    src = src if src is not None else law
    i = src.index(marker)
    a = src.index("```", i) + 3
    b = src.index("```", a)
    return [ln.strip() for ln in src[a:b].strip().splitlines() if ln.strip()]


HERO = block_after("**Every hero prompt carries these sentences")
assert len(HERO) == 6, f"the law lists {len(HERO)} hero sentences, not 6"
FIXED, PERSON = HERO[:5], HERO[5]
LOCK = block_after("So a session whose page has a hero writes its")
assert len(LOCK) == 2, f"the law lists {len(LOCK)} lock lines, not 2"
LIGHT, GRADE = LOCK

BLOCK = norm("""Use the attached product photo as the exact reference. Preserve its shape, proportions,
construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle,
simplify or add features. The product appears in one of its real colourways only, never
restyled to match the scene or the set palette; no added piping, trim, logos, patterns or
printed text. Every part keeps its photographed colour and finish; no part is tinted toward
the set's accent.""")
WORDLESS = "Nothing in the picture carries a word, a number, a label or a badge."
CORNER = "Nothing is placed in the bottom-right corner of the frame."
FIRST_END = ", one frame, no panels, no insets, no words."
HUB = "the hub"
MODULE = "the rear camera module"
G6 = "Any screen shows only a picture, with no interface, text or numbers."
ACROSS = "two thirds across"

BANNED = {
    "a ratio": r"\b\d+\s*:\s*\d+\b",
    "an avoid clause": r"(?i)\bavoid\b",
    "a repo name": r"(\b0\d-[a-z]+-[a-z]+\b|--[a-z]|\bLP2\b|\bADR\b|\bG\d+\b|\bhero\.image\b)",
    "a figure": r"\b\d+(\.\d+)?\s?(cm|mm|in|g|MHz|%)\b",
    "an inset": r"\b(inset|callout|split)\b",
    # a layout panel, but a car's kick panel is a real part of the scene
    "a layout panel": r"(?<!kick )\bpanels?\b",
    "a dark ground under a product that emits nothing": r"(?i)\b(dark studio|near-black|dim|moody|low[- ]key)\b",
    "the colourless world section-16 asked for": r"(?i)black harness tape",
    "a drawn mark, which a hero never carries": r"(?i)\b(arcs|glow|overlay|halo|wedge|leader|bird's-eye|composite)\b",
    "anatomy no photograph on disk supports": r"(?i)\b(lens|lenses|display|screen bezel|housing|matte black|glossy|rounded|cylindrical|LED)\b",
    "a banned standing hero": r"\bstands? (?:up )?(?:full[- ]length|in the frame)\b",
}
L = lambda **k: k
LEDGER = {
    1: L(place="front cabin", person=True, face=True, control=True, g6=True, part=HUB,
         bands="The headliner spans the top, the dashboard the bottom",
         scene="sets the hub on the glass"),
    2: L(place="front cabin", person=False, face=False, control=False, g6=True, part=HUB,
         bands="the headliner spans the top, the dashboard the bottom",
         scene="two sky-blue sleeves hold the hub against the glass"),
    3: L(place="rear cabin", person=False, face=False, control=False, g6=False, part=MODULE,
         bands="the rear headliner spanning the top and the parcel shelf the bottom",
         scene="steadies the rear camera module on the window"),
}

fails = []


def bad(ctx, msg):
    fails.append(f"{ctx}: {msg}")


prompts = [norm(b) for b in re.findall(r"```\n(.+?)\n```", text, re.S)]
if len(prompts) != len(LEDGER):
    bad("set", f"{len(prompts)} prompts, the ledger has {len(LEDGER)}")

for i, p in enumerate(prompts, 1):
    e = LEDGER.get(i)
    ctx = f"prompt {i}"
    if not e:
        continue
    if len(p) > GATE:
        bad(ctx, f"LENGTH {len(p)} > {GATE}")
    if not p.startswith("Photograph "):
        bad(ctx, "a hero prompt opens with the photograph it is")
    if FIRST_END not in p.split(". ")[0] + ".":
        bad(ctx, "the opening sentence does not end with the one-frame clause")
    if p.count(BLOCK) != 1:
        bad(ctx, f"the LP2 product block appears {p.count(BLOCK)} times")
    for s in FIXED:
        if p.count(s) != 1:
            bad(ctx, f"a hero sentence is missing or doubled: {s[:46]!r}")
    if (p.count(PERSON) == 1) != e["person"]:
        bad(ctx, f"the person sentence present={p.count(PERSON) == 1}, ledger says {e['person']}")
    for line, name in ((LIGHT, "light"), (GRADE, "grade"), (WORDLESS, "wordless"), (CORNER, "corner")):
        if p.count(line) != 1:
            bad(ctx, f"the {name} line appears {p.count(line)} times")
    if not re.search(r"Setting: [^.]+ where the colours are the [a-z' ]+own\.", p):
        bad(ctx, "no setting line in the law's form")
    if e["place"] not in p:
        bad(ctx, f"the ledger's place is not in the prompt: {e['place']!r}")
    if e["scene"] not in p:
        bad(ctx, f"the ledger's construction is not in the prompt: {e['scene']!r}")
    if e["bands"] not in p:
        bad(ctx, "the top and bottom bands are not FILLED by a named surface (ADR-123)")
    if ACROSS not in p:
        bad(ctx, f"the prompt does not say where across the picture the receiver sits ({ACROSS!r})")
    if e["part"] not in p:
        bad(ctx, f"the part this frame is of is not named: {e['part']!r}")
    if (p.count(G6) == 1) != e["g6"]:
        bad(ctx, f"the screen sentence present={p.count(G6) == 1}, ledger says {e['g6']}")
    if '"' in p:
        bad(ctx, "a hero carries no words, and this one quotes some")

    # the opening clause legitimately says "no panels, no insets, no words"
    scan = p.replace(BLOCK, " ").replace(FIRST_END, " ")
    for s in FIXED + [PERSON, LIGHT, GRADE, WORDLESS, CORNER]:
        scan = scan.replace(s, " ")
    for name, pat in BANNED.items():
        m = re.search(pat, scan)
        if m:
            bad(ctx, f"{name} reaches the prompt: {m.group(0)!r}")
    low = scan.lower()
    if re.search(r"\b(man|woman)\b", low) and "north american" not in low:
        bad(ctx, "a person with no casting named")
    if e["face"] and "expression" not in low:
        bad(ctx, "a face in frame with no expression named (ADR-104)")
    if not e["face"] and "no face is in frame" not in low:
        bad(ctx, "the ledger says no face, and the prompt does not say so")

if sum(1 for e in LEDGER.values() if e["control"]) != 1:
    bad("set", "the set does not declare exactly one control")
colours = ("mustard-yellow", "sky-blue", "red hatchback")
for c in colours:
    if sum(1 for p in prompts if c in p) != 1:
        bad("set", f"the clear colour {c!r} is not carried by exactly one prompt (ADR-119)")

for f in fails:
    print("FAIL", f)
print(f"{len(prompts)} prompts, {len(fails)} failure(s); longest "
      f"{max((len(p) for p in prompts), default=0)} characters")
sys.exit(1 if fails else 0)

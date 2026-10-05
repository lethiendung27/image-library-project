"""Check hero-06 against the hero section of registry/pdp-dr-instruction.md (ADR-103 to ADR-108).

One prompt, the labelled form, on a product that is a SET: the conditional sentence for a product
in frame more than once is required here, where every earlier hero set forbade it.

Usage: python3 registry/pdp-dr-types/sets/hero-06/check.py [prompts.md]
Exits 1 on any failure.
"""
import io, re, sys

PATH = "registry/pdp-dr-types/sets/hero-06/prompts.md"
text = io.open(sys.argv[1] if len(sys.argv) > 1 else PATH, encoding="utf-8").read()


def norm(x):
    "collapse whitespace so line-wrapping cannot hide or fake a match"
    return re.sub(r"\s+", " ", x).strip()


BLOCK = norm("""Use the attached product photo as the exact reference. Preserve its shape, proportions,
construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle,
simplify or add features. The product appears in one of its real colourways only, never
restyled to match the scene or the set palette; no added piping, trim, logos, patterns or
printed text. Every part keeps its photographed colour and finish; no part is tinted toward
the set's accent.""")
VARIANT = "Where several reference photos are attached, this image uses the large bag and only that one."
# the instruction's six hero sentences, word for word (ADR-103, ADR-107)
H = [
    "The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.",
    "The group fills about half the picture's height, with a clear band of room above every head and below every hand, each about a fifth.",
    "The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.",
    "The product is big enough to recognise at a glance, never a small detail in the distance.",
    "It is a real photograph: skin keeps its texture, with no glow and no haze.",
]
H6 = "Any person turns slightly toward the left side of the picture."
MULTI = "Wherever the product appears more than once in this image it is identical in every instance."
SETTING = "Setting: a lived-in home where the colours are the room's own."
LIGHT = "Light: bright daylight from the left, with natural shadows and real contrast."
GRADE = "Grade: true colour, neutral whites, no warm filter and no glow."
SCREENS = "Any screen shows only a picture, with no interface, text or numbers."
WORDLESS = "Nothing in the picture carries a word, a number, a label or a badge."
CORNER = "Nothing is placed in the bottom-right corner of the frame."
FIRST_END = ", one frame, no panels, no insets, no words."
# the owner's feature-image form (ADR-101's trade, ADR-108 for a hero)
G1 = "Use the attached product photo as the exact reference."
CLOSING = ("Do not change anything related to the original product, including screen, buttons, display, "
           "interface, ports, technical indicators, color, shape, proportions, dimensions, or functionality.")
PROSE = [
    "in the right half, just past the centre and well clear of the right edge",
    "about half the picture's height",
    "clear band of room above",
    "the left half continues the same",
    "It is a real photograph: skin keeps its texture, with no glow and no haze",
    "nothing in the picture carries a word, a number, a label or a badge",
    "nothing is placed in the bottom-right corner of the frame",
    "the colours are the room's own",
    "Bright daylight comes from the left, with natural shadows and real contrast",
    "turned slightly toward the left of the picture",
]
LABELS = ["Setting:", "Light:", "Grade:"]
FIELD_OPENERS = {"Setting:": SETTING, "Light:": LIGHT, "Grade:": GRADE}

L = lambda **k: k
LEDGER = {
    1: L(form="labelled", template="t1-deal-final-product-type 2", field="hero.image", product="lifter", control=True, seated=False, screen=False),
}
GATE = 1800
PARTS = {
    "wiboofy": ["antenna", "antennas", "button", "wps", "rj45", "ethernet", "port", "led", "leds",
                "status light", "white", "four", "dual-band"],
    "hivefold": ["beeswax", "wax", "cotton", "organic", "lining", "lined", "drawstring", "fabric",
                 "canvas", "beige", "brown", "pink", "cream", "logo", "wheat"],
    "cushion": ["memory foam", "foam", "gel", "black", "grey", "gray", "l-shaped", "strap", "straps",
                "cover", "zip", "zipper", "non-slip", "mesh", "velvet", "contoured", "coccyx"],
    # the lifting set: its page's words are lever and sliders; everything else about it is construction (G2)
    "lifter": ["steel", "metal", "aluminium", "aluminum", "plastic", "rubber", "wheels", "wheeled",
               "roller", "rollers", "pads", "non-slip", "textured", "360", "fulcrum", "black", "orange",
               "blue", "grey", "gray", "bearing", "bearings", "handle", "hook", "claw"],
}
BRANDS = [r"\bwiboofy\b", r"\bhivefold\b", r"\btop ?laser\b", r"\baure\b"]
# the set is two parts, so the frame may carry the product more than once
MULTI_PRODUCTS = {"lifter"}
MINORS = ["child", "children", "girl", "boy", "kid", "kids", "teen", "teenager", "toddler", "baby"]
DRAINED = ["pale", "muted", "beige", "greyed", "washed", "desaturated", "calm", "soft focus",
           "nothing saturated", "minimal", "minimalist", "monochrome", "hazy", "gentle shadows",
           "soft window light", "pastel"]
YELLOW = ["warm daylight", "warm light", "golden", "golden hour", "sunny", "amber", "editorial realism",
          "vivid", "fruit", "fruit bowl", "oranges", "sunset", "sunlit"]
# ADR-108: colour comes from the room, so no prompt names one except on a person's clothes
STAGED = ["colours from more than one family", "greens, blues and reds", "bright textiles",
          "coloured cushions", "a splash of colour", "pop of colour"]
EXPRESSION = "a natural, relaxed expression"
WARDROBE = ["blue", "coral", "yellow", "green", "red", "orange", "terracotta", "teal", "navy", "pink",
            "mustard", "sage", "denim", "sky-blue", "denim-blue", "mustard-yellow", "sage-green", "rust"]
REPO_NAMES = [r"\b\d{2}-[a-z]+-[a-z]+\b", r"--[a-z]", r"\blp2\b", r"\badr\b",
              r"\bhero\b", r"\bbanner\b", r"\bsafe box\b", r"\btemplates?\b", r"\bdesktop\b",
              r"\bmobile\b", r"\bcrop(s|ped)?\b", r"\bpanel\b"]
RULE_IDS = r"\bG\d+\b"
REGION_LABEL = re.compile(r"(?m)^\s*(Top|Bottom|Left|Right|Middle|Upper|Lower|Above|Below|Scene|Hero|Subject)\b[^:\n]{0,24}:")
SEATED_SIDE = ["seen from the side", "from the side so the whole cushion reads"]
SEATED_HOST = ["The chair is in a tone and material clearly different from the cushion.",
               "against a chair of a clearly different tone"]


def has(word, low):
    return re.search(rf"(?<![a-z-]){re.escape(word)}(?![a-z-])", low) is not None


blocks = {int(m.group(1)): (m.group(2).strip(), m.group(3))
          for m in re.finditer(r"^## (\d+) — ([^\n]*)\n.*?```\n(.*?)\n```", text, re.S | re.M)}
fail = []
print("prompts found:", len(blocks))
if set(blocks) != set(LEDGER):
    fail.append(("set", f"prompts {sorted(blocks)} != ledger {sorted(LEDGER)}"))

for n, row in LEDGER.items():
    if n not in blocks:
        continue
    head, p = blocks[n]
    ctx = f"{n} {row['form']} {row['product']}"
    P = norm(p)
    low = P.lower()
    lines = [l.strip() for l in p.splitlines() if l.strip()]
    if ("`06-relief-hero`" not in head or "· hero ·" not in head or f"`{row['field']}`" not in head
            or f"`{row['template']}`" not in head):
        fail.append((ctx, f"heading does not name the type, the slot, the field and the template: {head[:80]!r}"))
    if (row["form"] == "paragraph") != ("paragraph form" in head):
        fail.append((ctx, "the heading does not say which form this prompt is"))
    if ("CONTROL" in head) != row["control"]:
        fail.append((ctx, f"CONTROL in heading={'CONTROL' in head}, declared={row['control']}"))
    if len(p) > GATE:
        fail.append((ctx, f"LENGTH {len(p)} > {GATE}"))

    if row["form"] == "labelled":
        if not (lines[0].startswith("Photograph of ") and lines[0].endswith(FIRST_END)):
            fail.append((ctx, f"first line is not the photograph line: {lines[0][:70]!r}"))
        need = [(BLOCK, "product block"), (SETTING, "setting"), (LIGHT, "light"), (GRADE, "grade"),
                (WORDLESS, "no words"), (CORNER, "corner"), (H6, "the person sentence")]
        need += [(h, f"hero sentence {i + 1}") for i, h in enumerate(H)]
        for s, name in need:
            k = P.count(s)
            if k != 1:
                fail.append((ctx, f"{name}: found {k} times, expected once, word for word"))
        for s in lines:
            for opener, allowed in FIELD_OPENERS.items():
                if s.startswith(opener) and s != allowed:
                    fail.append((ctx, f"a lock field in other words: {s[:60]!r}"))
        if (SCREENS in P) != bool(row["screen"]):
            fail.append((ctx, f"G6 screen sentence present={SCREENS in P}, declared={bool(row['screen'])}"))
        if low.count("inset") != 1:
            fail.append((ctx, "an inset is named beyond the first line's 'no insets'"))
    else:
        for lab in LABELS:
            if lab in p:
                fail.append((ctx, f"the paragraph form carries the label {lab!r}"))
        if BLOCK in P:
            fail.append((ctx, "the paragraph form carries the product block; the closing sentence replaces it"))
        for s in PROSE:
            if s.lower() not in low:
                fail.append((ctx, f"the paragraph does not carry {s[:50]!r}"))
        if not P.endswith(CLOSING):
            fail.append((ctx, "the paragraph does not end with the instruction's closing sentence"))
        if P.count(G1) != 1:
            fail.append((ctx, "the paragraph does not carry G1's one sentence exactly once"))
        if has("inset", low):
            fail.append((ctx, "an inset is named"))
        if row["screen"] and "screen shows only a picture" not in low:
            fail.append((ctx, "a screen can appear and the paragraph does not keep it to a picture (G6)"))

    free = low
    for fixed in [SETTING, LIGHT, GRADE, SCREENS, WORDLESS, CORNER, H6, G1, CLOSING, VARIANT] + H + PROSE:
        free = free.replace(fixed.lower(), " ")
    if (VARIANT in P) != (row["product"] == "hivefold"):
        fail.append((ctx, f"variant sentence present={VARIANT in P}, expected for hivefold only"))
    if (MULTI in P) != (row["product"] in MULTI_PRODUCTS):
        fail.append((ctx, f"multi-instance sentence present={MULTI in P}, expected for a product that is a set"))
    if row["product"] == "hivefold" and not re.search(r"\bno box\b", low):
        fail.append((ctx, "the bag's printed box is not kept out of frame"))
    if row["product"] == "wiboofy" and "plugged into a wall socket" not in low:
        fail.append((ctx, "the extender is not plugged into a wall socket (G7-X)"))
    if row["product"] == "lifter":
        if "sliders are under" not in low:
            fail.append((ctx, "the sliders are not under the furniture they carry (G7-X)"))
        if not re.search(r"\bhas just been moved|has just|already\b", low):
            fail.append((ctx, "a relief hero whose heavy thing has not already moved"))
    if row["seated"]:
        if not any(s in p for s in SEATED_SIDE):
            fail.append((ctx, "a product that is sat on, not seen from the side"))
        if not any(s in p for s in SEATED_HOST):
            fail.append((ctx, "the host chair is not asked for as a relation"))
    for w in PARTS[row["product"]]:
        if has(w, free):
            fail.append((ctx, f"G2: a part, material or colour word {w!r}"))
    for pat in BRANDS:
        if re.search(pat, free):
            fail.append((ctx, f"a brand name reaches the prompt: /{pat}/"))
    for w in MINORS:
        if has(w, free):
            fail.append((ctx, f"G13: a minor {w!r} in a hero prompt"))
    for w in DRAINED:
        if has(w, free):
            fail.append((ctx, f"a drained colour word {w!r} (ADR-104)"))
    for w in YELLOW:
        if has(w, free):
            fail.append((ctx, f"a yellow-pulling word {w!r} (ADR-107)"))
    for w in STAGED:
        if w in free:
            fail.append((ctx, f"a staged-colour phrase {w!r} (ADR-108)"))
    if EXPRESSION not in low:
        fail.append((ctx, "a person without the natural, relaxed expression"))
    if not re.search(r"\bin an? ([a-z-]+ )*?(" + "|".join(map(re.escape, WARDROBE)) + r")\b", free):
        fail.append((ctx, "a person with no clear colour to wear"))
    if not re.search(r"\b(European|North American)\b", P):
        fail.append((ctx, "a person with no casting named"))
    if re.search(r"\basian\b", low):
        fail.append((ctx, "casting named in the negative"))
    if re.search(r'["“”]', p):
        fail.append((ctx, "quoted words in a wordless hero"))
    if re.search(r"\b(montserrat|sans-serif|typeface|title|headline|caption)\b", free):
        fail.append((ctx, "a typography or title sentence in a wordless hero"))
    for pat in REPO_NAMES + [RULE_IDS]:
        if re.search(pat, p, 0 if pat == RULE_IDS else re.I):
            fail.append((ctx, f"a repo, slot or device name reaches the prompt: /{pat}/"))
    if REGION_LABEL.search(p):
        fail.append((ctx, f"a region label: {REGION_LABEL.search(p).group(0).strip()!r}"))
    if re.search(r"\b\d+\s*:\s*\d+\b", p) or re.search(r"\b(square|aspect ratio|portrait frame|landscape frame|widescreen)\b", low):
        fail.append((ctx, "names the frame's shape or ratio (ADR-016)"))
    if re.search(r"(?im)^\s*(strictly\s+)?avoid\s*:", p):
        fail.append((ctx, "an Avoid: line (ADR-014)"))
    if MULTI not in P and "appears more than once" in low:
        fail.append((ctx, "the multi-instance sentence in other words"))

if sum(LEDGER[n]["control"] for n in LEDGER) != 1:
    fail.append(("set", "not exactly one control"))
if len(LEDGER) != 1:
    fail.append(("set", f"this set is one prompt, found {len(LEDGER)} in the ledger"))

print("lengths: " + ", ".join(f"{n}:{len(blocks[n][1])}" for n in sorted(blocks)))
if fail:
    for c, m in fail:
        print("FAIL", c, "—", m)
    sys.exit(1)
print("PASS")

"""Check hero-04 against the hero section of registry/pdp-dr-instruction.md (ADR-103, ADR-104, ADR-107) and LP2 law.

Usage: python3 registry/pdp-dr-types/sets/hero-04/check.py [prompts.md]
Exits 1 on any failure. The ledger is declared here, apart from prompts.md, so an edit to a prompt
is measured against what the set says it is.
"""
import io, re, sys

PATH = "registry/pdp-dr-types/sets/hero-04/prompts.md"
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
# The instruction's hero sentences, word for word (ADR-103 as ADR-104 left them). H5 only where a person is in frame.
H = [
    "The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge.",
    "The group fills about half the picture's height, with a clear band of room above every head and below every hand, each about a fifth.",
    "The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters.",
    "The product is big enough to recognise at a glance, never a small detail in the distance.",
    "It is a real photograph: skin keeps its texture, with no glow and no haze.",
]
H5 = "Any person turns slightly toward the left side of the picture."
SETTING = "Setting: a bright, lived-in home with green, blue and red among its colours."
# the instruction's hero light and grade lines, word for word (ADR-104)
LIGHT = "Light: bright daylight from the left, with natural shadows and real contrast."
GRADE = "Grade: true colour, neutral whites, no warm filter and no glow."
SCREENS = "Any screen shows only a picture, with no interface, text or numbers."
WORDLESS = "Nothing in the picture carries a word, a number, a label or a badge."
CORNER = "Nothing is placed in the bottom-right corner of the frame."
FIRST_END = ", one frame, no panels, no insets, no words."
ALWAYS = [(SETTING, "setting"), (LIGHT, "light"), (GRADE, "grade"), (WORDLESS, "no words"),
          (CORNER, "corner"), (BLOCK, "product block")] + [(h, f"hero sentence {i + 1}") for i, h in enumerate(H)]
FIELD_OPENERS = {"Setting:": SETTING, "Light:": LIGHT, "Grade:": GRADE}

L = lambda **k: k
LEDGER = {
    1: L(template="pdp-dr-seat-cushion-l-shaped-v08", field="hero.image", product="cushion", person=True, control=True, seated=True, screen=True),
    2: L(template="pdp-dr-seat-cushion-l-shaped-v08", field="hero.image", product="cushion", person=True, control=False, seated=False, screen=True),
    3: L(template="wiboofy-final-product-type 2", field="hero.background", product="wiboofy", person=True, control=False, seated=False, screen=True),
    4: L(template="t2-eco-final-product-type", field="hero.image", product="hivefold", person=True, control=False, seated=False, screen=False),
    5: L(template="aure-toplaser-final 2", field="hero.image", product="toplaser", person=True, control=False, seated=False, screen=False),
    6: L(template="pdp-dr-seat-cushion-l-shaped-v08", field="hero.image", product="cushion", person=True, control=False, seated=True, screen=False),
}
GATE = 1800
# G2: no part, material or colour of the product; and the brand never reaches the prompt
PARTS = {
    "wiboofy": ["antenna", "antennas", "button", "wps", "rj45", "ethernet", "port", "led", "leds",
                "status light", "white", "four", "dual-band"],
    "hivefold": ["beeswax", "wax", "cotton", "organic", "lining", "lined", "drawstring", "fabric",
                 "canvas", "beige", "brown", "pink", "cream", "logo", "wheat"],
    "toplaser": ["flash", "flashes", "glow", "pulse", "beam", "lamp", "button", "cord", "cable",
                 "screen", "white", "gold", "ipl", "laser", "window of the device"],
    # the cushion: no material, no colour, no named part (G2)
    "cushion": ["memory foam", "foam", "gel", "black", "grey", "gray", "l-shaped", "strap", "straps",
                "cover", "zip", "zipper", "non-slip", "mesh", "velvet", "contoured", "coccyx"],
}
# a product that is sat on is seen from the side, and its host is a RELATION (the instruction)
SEATED_SIDE = "seen from the side"
SEATED_HOST = "The chair is in a tone and material clearly different from the cushion."
BRANDS = [r"\bwiboofy\b", r"\bhivefold\b", r"\btop ?laser\b", r"\baure\b"]
# the treatment stays at mid height: a leg or the bikini line runs into the bottom fifth
BODY_LOW = ["leg", "legs", "shin", "shins", "thigh", "thighs", "knee", "knees", "calf", "calves",
            "bikini", "ankle", "ankles", "foot", "feet"]
MINORS = ["child", "children", "girl", "boy", "kid", "kids", "teen", "teenager", "toddler", "baby"]
# matched case-insensitively, except the rule ids
REPO_NAMES = [r"\b\d{2}-[a-z]+-[a-z]+\b", r"--[a-z]", r"\blp2\b", r"\badr\b",
              r"\bhero\b", r"\bbanner\b", r"\bsafe box\b", r"\btemplates?\b", r"\bdesktop\b",
              r"\bmobile\b", r"\bcrop(s|ped)?\b", r"\bpanel\b"]
RULE_IDS = r"\bG\d+\b"
# ADR-104: the colour a render loses is the colour the prompt drained. Scanned outside the fixed lines.
DRAINED = ["pale", "muted", "beige", "greyed", "washed", "desaturated", "calm",
           "soft focus", "nothing saturated", "minimal", "minimalist", "monochrome", "hazy",
           "gentle shadows", "soft window light", "pastel"]
# ADR-107: the words that turned every frame yellow, and the props that carried it
YELLOW = ["warm daylight", "warm light", "golden", "golden hour", "sunny", "amber", "editorial realism",
          "vivid", "fruit", "fruit bowl", "oranges", "sunset", "glow", "sunlit"]
SMILES = ["smile", "smiles", "smiling", "grin", "grins", "grinning", "laugh", "laughs", "laughing", "beaming"]
WARDROBE = ["blue", "coral", "yellow", "green", "red", "orange", "terracotta", "teal", "navy", "pink",
            "mustard", "sage", "denim", "sky-blue", "denim-blue", "mustard-yellow", "sage-green", "rust"]
EXPRESSION = "a natural, relaxed expression"
REGION_LABEL = re.compile(r"(?m)^\s*(Top|Bottom|Left|Right|Middle|Upper|Lower|Above|Below|Scene|Hero|Subject)\b[^:\n]{0,24}:")


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
    ctx = f"{n} {row['product']}"
    P = norm(p)
    low = P.lower()
    lines = [l.strip() for l in p.splitlines()]
    free = low
    for fixed in [SETTING, LIGHT, GRADE, SCREENS, WORDLESS, CORNER, H5] + H:
        free = free.replace(fixed.lower(), " ")
    if ("`06-relief-hero`" not in head or "· hero ·" not in head or f"`{row['field']}`" not in head
            or f"`{row['template']}`" not in head):
        fail.append((ctx, f"heading does not name the type, the slot, the field and the template: {head[:80]!r}"))
    if ("CONTROL" in head) != row["control"]:
        fail.append((ctx, f"CONTROL in heading={'CONTROL' in head}, declared={row['control']}"))
    if len(p) > GATE:
        fail.append((ctx, f"LENGTH {len(p)} > {GATE}"))
    if not (lines[0].startswith("Photograph of ") and lines[0].endswith(FIRST_END)):
        fail.append((ctx, f"first line is not the photograph line ending in no words: {lines[0][:70]!r}"))
    for need, name in ALWAYS:
        k = P.count(need)
        if k != 1:
            fail.append((ctx, f"{name}: found {k} times, expected once, word for word"))
    k5 = P.count(H5)
    if row["person"] and k5 != 1:
        fail.append((ctx, f"a person in frame but the person sentence found {k5} times"))
    if not row["person"] and k5:
        fail.append((ctx, "the person sentence in a prompt with no person"))
    for s in lines:
        for opener, allowed in FIELD_OPENERS.items():
            if s.startswith(opener) and s != allowed:
                fail.append((ctx, f"a lock field in other words: {s[:60]!r}"))
    if (VARIANT in P) != (row["product"] == "hivefold"):
        fail.append((ctx, f"variant sentence present={VARIANT in P}, expected for hivefold only"))
    if row["product"] == "hivefold" and not re.search(r"\bno (person and no )?box\b", low):
        fail.append((ctx, "the bag's printed box is not kept out of frame"))
    if (SCREENS in P) != bool(row.get("screen")):
        fail.append((ctx, f"G6 screen sentence present={SCREENS in P}, declared={bool(row.get('screen'))}"))
    if row.get("seated"):
        if SEATED_SIDE not in low:
            fail.append((ctx, "a product that is sat on, not seen from the side"))
        if SEATED_HOST not in P:
            fail.append((ctx, "the host chair is not asked for as a relation"))
    elif SEATED_HOST in P:
        fail.append((ctx, "the seated-host sentence in a prompt with no seated product"))
    if row["product"] == "wiboofy" and "plugged into a wall socket" not in low:
        fail.append((ctx, "the extender is not plugged into a wall socket (G7-X)"))
    if row["product"] == "toplaser":
        for w in BODY_LOW:
            if has(w, free):
                fail.append((ctx, f"a low treatment area {w!r} pushes the device into the bottom fifth"))
    for w in PARTS[row["product"]]:
        if has(w, free):
            fail.append((ctx, f"G2: a part, material or colour word {w!r}"))
    for pat in BRANDS:
        if re.search(pat, free):
            fail.append((ctx, f"a brand name reaches the prompt: /{pat}/"))
    for w in MINORS:
        if has(w, low):
            fail.append((ctx, f"G13: a minor {w!r} in a hero prompt"))
    if row["person"] and not re.search(r"\b(European|North American)\b", P.replace(SETTING, "")):
        fail.append((ctx, "a person with no casting named"))
    if not row["person"] and not re.search(r"\bno person\b", low):
        fail.append((ctx, "a prompt declared without a person does not say so"))
    for w in DRAINED:
        if has(w, free):
            fail.append((ctx, f"a drained colour word {w!r} outside the fixed lines (ADR-104)"))
    for w in YELLOW:
        if has(w, free):
            fail.append((ctx, f"a yellow-pulling word {w!r} outside the fixed lines (ADR-107)"))
    for w in SMILES:
        if has(w, free):
            fail.append((ctx, f"a posed smile {w!r} (the owner's instruction)"))
    if row["person"]:
        if EXPRESSION not in low:
            fail.append((ctx, "a person without the natural, relaxed expression"))
        if not re.search(r"\bin an? ([a-z-]+ )*?(" + "|".join(map(re.escape, WARDROBE)) + r")\b", free):
            fail.append((ctx, "a person with no clear, friendly colour to wear"))
    if re.search(r"\basian\b", low):
        fail.append((ctx, "casting named in the negative"))
    if re.search(r'["“”]', p):
        fail.append((ctx, "quoted words in a wordless hero"))
    if re.search(r"\b(montserrat|sans-serif|typeface|title|headline|caption)\b", low):
        fail.append((ctx, "a typography or title sentence in a wordless hero"))
    if low.count("inset") != 1:
        fail.append((ctx, "an inset is named beyond the first line's 'no insets'"))
    for m in re.finditer(r"[^.]*\bscreen\b[^.]*\.", free):
        if "turned away" not in m.group(0):
            fail.append((ctx, "a screen that is not turned away (G6)"))
    for pat in REPO_NAMES + [RULE_IDS]:
        if re.search(pat, p, 0 if pat == RULE_IDS else re.I):
            fail.append((ctx, f"a repo, slot or device name reaches the prompt: /{pat}/"))
    if REGION_LABEL.search(p):
        fail.append((ctx, f"a region label: {REGION_LABEL.search(p).group(0).strip()!r}"))
    if re.search(r"\b\d+\s*:\s*\d+\b", p) or re.search(r"\b(square|aspect ratio|portrait frame|landscape frame|widescreen|wide format)\b", low):
        fail.append((ctx, "names the frame's shape or ratio (ADR-016)"))
    if re.search(r"(?im)^\s*(strictly\s+)?avoid\s*:", p):
        fail.append((ctx, "an Avoid: line (ADR-014)"))
    if "appears more than once" in low:
        fail.append((ctx, "the multi-instance sentence, for one unit"))

if sum(LEDGER[n]["control"] for n in LEDGER) != 1:
    fail.append(("set", "not exactly one control"))
fields = {(r["template"], r["field"]) for r in LEDGER.values()}
if len(fields) != 4:
    fail.append(("set", f"the set covers {len(fields)} hero fields, expected four"))
if sum(1 for r in LEDGER.values() if r["product"] == "cushion") != 3:
    fail.append(("set", "the new product does not carry three of the six prompts"))

print("lengths: " + ", ".join(f"{n}:{len(blocks[n][1])}" for n in sorted(blocks)))
if fail:
    for c, m in fail:
        print("FAIL", c, "—", m)
    sys.exit(1)
print("PASS")

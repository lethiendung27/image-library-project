"""Check section-12 against `03-spec-overlay` v0.13 and the laws ADR-128, ADR-129 and ADR-130 left.

Nine frames across three products and SIX overlay forms. The set exists to test that a set spans
the forms rather than playing one nine times, so the first check is the spread itself; after that
come the per-form clauses word for word, the register split, the product-led person count, and the
standing rules: no hand on a clip or clamp (ADR-128), nothing drawn ON a wire, loom or cable
(ADR-109 widened by ADR-128), a headline or a label never on a plate while a figure keeps its card
and an icon keeps its box (ADR-129).

The type's own clauses are READ OUT OF THE TYPE FILE rather than typed here twice, so a law
reworded again fails this set instead of leaving it quietly stale.

Usage, from the repo root: python3 registry/pdp-dr-types/sets/section-12/check.py [prompts.md]
Exits 1 on any failure.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
PATH = os.path.join(HERE, "prompts.md")
TYPE = os.path.join(ROOT, "registry", "pdp-dr-types", "03-spec-overlay.md")
text = io.open(sys.argv[1] if len(sys.argv) > 1 else PATH, encoding="utf-8").read()
law = io.open(TYPE, encoding="utf-8").read()

GATE = 1800
OPEN = "Editorial realism product feature image"
NOTEXT = "Nothing else in the picture carries text."
G1 = "Use the attached product photo as the exact reference."
CABLE = "Nothing is drawn on any wire, loom or cable."
LIGHT_PLACE = ("The light is the place's own — a work lamp and the daylight behind it — true colour, "
               "neutral whites, no cast over the picture; the colour comes from the scene itself:")
LIGHT_STUDIO = ("The light is studio light on a seamless ground — one soft key from the left and a "
                "cool rim behind — true colour, neutral whites, no cast over the picture; the colour "
                "comes from the product and its own leads.")

FORM_CLAUSE = {
    "tag": ("set once in plain bold white letters directly on the photograph with a soft dark edge, "
            "no plate or band behind them, the capitals about a twentieth of the picture's height "
            "and the line running between a quarter and a third of its width"),
    "icon": ("Three line icons in thin white strokes, each inside its own rounded square outline, "
             "stand in a row across the top of the frame, and under each one its name is set in "
             "plain bold white capitals directly on the picture:"),
    "callout": ("Three short labels in plain bold white stand on straight white leader lines, each "
                "line ending ON the part it names, set directly on the picture with no plate behind "
                "them:"),
    "figure": ("stands inside a drawn card with a thin glowing cyan border and a faint translucent "
               "fill, floating in the scene beside the product at about the size of a hand, the "
               "figure itself in plain bold white."),
    "mark": ("A set of concentric arcs in luminous cyan stands in the air between them, each arc "
             "thinner than the last, reaching the cable without touching it."),
    "view": None,  # a view frame carries no drawn word at all
}
FORMS = list(FORM_CLAUSE)

LAW_MARKERS = [
    ('version: "0.13"', "the type is no longer 0.13"),
    ("A SET spans the overlay forms", "the type no longer asks a set to span the forms"),
    ("A feature frame is PRODUCT-LED", "the type no longer makes a feature frame product-led"),
    ("is the exception and keeps its card",
     "the type no longer exempts the figure from the no-plate rule"),
    ("the FIGURE CARD, a drawn", "the type no longer names the figure card as its own device"),
    ("may sit in the AIR between the product and its subject",
     "the type no longer allows a mark to stand in the air"),
    ("no hand closes, presses or holds a clip", "the type no longer bans a hand on a clip"),
    ("Nothing is drawn ON a wire, a loom or a cable", "the type no longer bans a mark on a cable"),
]

NEVER = ["perfect", "ultimate", "premium", "luxury", "all-day", "approved", "tested", "certified",
         "proven", "guaranteed", "clinical", "best", "instant", "cure", "safely", "safest"]
GRAPHIC = r"(a band of light|a bar of light|a wave of light|a ring of light|icon ring|lightning bolt)"
BANNED = {
    "a ratio": r"\b\d+\s*:\s*\d+\b",
    "an avoid clause": r"(?i)\bavoid\b",
    "a repo name": r"(\b0\d-[a-z]+-[a-z]+\b|--[a-z]|\bLP2\b|\bADR\b|\bG\d+\b)",
    "an inset the type did not ask for": r"\binset\b",
}
HAND_ON_CLIP = re.compile(
    r"\b(clos(?:e|es|ed|ing)|press(?:es|ed|ing)?|hold(?:s|ing)?|grip(?:s|ping)?|fit(?:s|ting)?|"
    r"push(?:es|ing)?|snap(?:s|ping)?|attach(?:es|ing)?)\b[^.]{0,60}?"
    r"\b(clip|clips|clamp|clamps|plug|connector)\b", re.I)
DRAWN_ON_RUN = re.compile(
    r"\b(glow(?:s|ing)?|bloom(?:s|ing)?|arcs?|light)\b[^.]{0,70}?\b(through|along|down|inside|on)\b"
    r"[^.]{0,30}?\b(loom|lead|leads|wire|wiring|cable|cord|sheath|tape)\b", re.I)
OWN_LIGHT = re.compile(r"\b(LED|lamp|display|flashlight|screen|torch)\b", re.I)

L = lambda **k: k
LEDGER = {
    "1": L(slot="features.items.2", product="Automotive Circuit Tester", form="icon", studio=True,
           person=False, control=False, words=[],
           closed="Nothing is drawn on any wire, loom or cable.",
           anchor="a blade fuse under the word FUSES"),
    "2": L(slot="features.items.2", product="Automotive Circuit Tester", form="tag", studio=False,
           person=True, control=False, words=["Fuses, wires, drains"],
           closed="Nothing in the picture is cut, stripped or unwrapped: every wire stays taped and whole.",
           anchor="its sensing tip resting on the tape at one spot"),
    "3": L(slot="features.items.2", product="Automotive Circuit Tester", form="callout", studio=True,
           person=False, control=False, words=[],
           closed="Nothing is drawn on any wire, loom or cable.",
           anchor="one on the switch, one on the red clip, one on the sensing tip"),
    "4": L(slot="features.items.0", product="Smart Automatic Car Battery Charger", form="figure",
           studio=False, person=False, control=False, words=["6V/12V"],
           closed="Nothing in the picture is being chosen by hand: there is no switch being moved and no dial being turned, because the unit has already decided.",
           anchor="already run to the posts"),
    "5": L(slot="features.items.0", product="Smart Automatic Car Battery Charger", form="view",
           studio=True, person=False, control=False, words=[],
           closed="Nothing in the picture is being chosen by hand: there is no switch being moved and no dial being turned, because the unit has already decided.",
           anchor="the detected voltage and the charge stage shown on its own screen"),
    "6": L(slot="features.items.0", product="Smart Automatic Car Battery Charger", form="icon",
           studio=True, person=False, control=False, words=[],
           closed="Nothing in the picture is being chosen by hand: there is no switch being moved and no dial being turned, because the unit has already decided.",
           anchor="a car under the word CAR"),
    "7": L(slot="features.items.1", product="True RMS Digital Multimeter", form="mark", studio=False,
           person=False, control=False, words=[],
           closed="Nothing in the picture is stripped, cut or pulled out: every conductor stays inside its sheath.",
           anchor="held a finger's width from a grey cable"),
    "8": L(slot="features.items.1", product="True RMS Digital Multimeter", form="tag", studio=False,
           person=True, control=False, words=["It knows without touching"],
           closed="Nothing in the picture is stripped, cut or pulled out: every conductor stays inside its sheath.",
           anchor="a finger's width of air between the meter's top edge and the metal"),
    "9": L(slot="features.items.1", product="True RMS Digital Multimeter", form="view", studio=True,
           person=False, control=True, words=[],
           closed="Nothing in the picture is stripped, cut or pulled out: every conductor stays inside its sheath.",
           anchor="the analogue bar graph running beside it"),
}
KEYS = list(LEDGER)

fails = []


def bad(ctx, msg):
    fails.append(f"{ctx}: {msg}")


for marker, msg in LAW_MARKERS:
    if marker not in law:
        bad("law", msg + f" ({marker!r} is gone from 03-spec-overlay.md)")

prompts = [re.sub(r"\s+", " ", b).strip() for b in re.findall(r"```\n(.+?)\n```", text, re.S)]
if len(prompts) != len(LEDGER):
    bad("set", f"{len(prompts)} prompts, the ledger has {len(LEDGER)}")

# ---- ADR-129: the set spans the forms
used = [e["form"] for e in LEDGER.values()]
distinct = sorted(set(used))
if len(distinct) < 4:
    bad("set", f"{len(distinct)} overlay forms, ADR-129 asks for at least four of six: {distinct}")
for f in distinct:
    if used.count(f) > 3:
        bad("set", f"the form {f!r} is used {used.count(f)} times, ADR-129 caps it at three")
    if f not in FORMS:
        bad("set", f"unknown overlay form {f!r}")
# ---- the register split and the person count
studios = sum(1 for e in LEDGER.values() if e["studio"])
if studios < 4:
    bad("set", f"{studios} studio frames; the owner's corpus is 8 of 17 (ADR-129)")
people = sum(1 for e in LEDGER.values() if e["person"])
if people > 2:
    bad("set", f"{people} frames carry a person; a feature frame is product-led (ADR-129)")
if sum(1 for e in LEDGER.values() if e["control"]) != 1:
    bad("set", "a set declares exactly one control")
if text.count("**CONTROL**") != 1:
    bad("set", f"the set marks {text.count('**CONTROL**')} controls in prose, not 1")
slots = sorted({e["slot"] for e in LEDGER.values()})
if len(slots) != 3:
    bad("set", f"{len(slots)} slots, the set covers three")
for s in slots:
    n = sum(1 for e in LEDGER.values() if e["slot"] == s)
    if n != 3:
        bad("set", f"slot {s} has {n} options, ADR-127 asks for three")
if len({e["product"] for e in LEDGER.values()}) != 3:
    bad("set", "the set must span three products, one per line (ADR-128)")

for key, p in zip(KEYS, prompts):
    e = LEDGER[key]
    ctx = f"prompt {key} ({e['form']})"
    if len(p) > GATE:
        bad(ctx, f"LENGTH {len(p)} > {GATE}")
    if not p.startswith(OPEN):
        bad(ctx, "the prompt does not open in the section form's register")
    for line, name in ((NOTEXT, "no-other-text"), (G1, "reference"), (CABLE, "cable")):
        if p.count(line) != 1:
            bad(ctx, f"the {name} clause appears {p.count(line)} times")
    if not p.endswith(G1):
        bad(ctx, "the reference sentence is not last")
    if e["product"] not in p:
        bad(ctx, f"the product is not named: {e['product']!r}")
    if p.count(e["closed"]) != 1:
        bad(ctx, f"the untouched-claim sentence appears {p.count(e['closed'])} times")
    if e["anchor"] not in p:
        bad(ctx, f"the frame's anchor is missing: {e['anchor'][:46]!r}")

    # ---- the register's own light clause, word for word
    want, other = (LIGHT_STUDIO, LIGHT_PLACE) if e["studio"] else (LIGHT_PLACE, LIGHT_STUDIO)
    if p.count(want) != 1:
        bad(ctx, f"the {'studio' if e['studio'] else 'place'} light clause appears {p.count(want)} times")
    if other in p:
        bad(ctx, "the frame carries the other register's light clause as well")
    if e["studio"] and "no place" not in p:
        bad(ctx, "a studio frame that does not say it has no place")

    # ---- the form's own clause, word for word; and no other form's clause
    for form, clause in FORM_CLAUSE.items():
        if clause is None:
            continue
        n = p.count(clause)
        if form == e["form"]:
            if n != 1:
                bad(ctx, f"the {form} clause appears {n} times")
        elif n:
            bad(ctx, f"a {e['form']} frame carrying the {form} clause")

    quoted = re.findall(r'"([^"]+)"', p)
    if e["form"] == "view" and quoted:
        bad(ctx, "a view frame carries a drawn word; its argument is the product's own screen")
    if quoted != e["words"]:
        bad(ctx, f"the drawn words are {quoted}, the ledger says {e['words']}")
    for w in e["words"]:
        n = len(re.findall(r"[A-Za-z0-9]+(?:[-'/][A-Za-z0-9]+)*", w))
        if n > 5:
            bad(ctx, f"the drawn words {w!r} run {n} words, over the five ADR-106 allows")

    scene = p.replace(LIGHT_PLACE, " ").replace(LIGHT_STUDIO, " ").replace(NOTEXT, " ")
    for clause in FORM_CLAUSE.values():
        if clause:
            scene = scene.replace(clause, " ")
    scene = re.sub(r'"[^"]*"', " ", scene)

    # ---- ADR-128: nothing drawn on a run; the product's own light is not the drawn layer
    for sentence in re.split(r"(?<=\.)\s+", scene):
        if CABLE.rstrip(".") in sentence or "without touching it" in sentence:
            continue
        m = DRAWN_ON_RUN.search(sentence)
        if m and not OWN_LIGHT.search(sentence):
            bad(ctx, f"a drawn light on a wire, loom or cable (ADR-128): {sentence[:72]!r}")
    m = re.search(GRAPHIC, scene, re.I)
    if m:
        bad(ctx, f"the mark is named as a graphic (ADR-125): {m.group(0)!r}")

    # ---- ADR-128: no hand acts on a clip, clamp, plug or connector
    for sentence in re.split(r"(?<=\.)\s+", scene):
        m = HAND_ON_CLIP.search(sentence)
        if m:
            bad(ctx, f"a hand acts on a clip or clamp (ADR-128): {m.group(0)!r}")
    if not re.search(r"(bitten on|clipped|already run|hangs .{0,30}where it was clipped|shut tight|"
                     r"held close to|held a finger's width|lying with its status lamp lit|"
                     r"standing upright with its status lamp lit|lit and reading|lit and turned)", p):
        bad(ctx, "the product is not shown already connected, already in position or working")

    # ---- ADR-129: a plate is a fault under a HEADLINE or a LABEL only
    if e["form"] in ("tag", "callout"):
        if re.search(r"\b(plate|band|box|panel|plaque|strip|card|chip|badge)\b[^.]{0,24}\bbehind\b",
                     scene, re.I):
            bad(ctx, "a plate behind a headline or a label (ADR-128, ADR-129)")

    scan = scene.replace(G1, " ")
    low = scan.lower()
    for w in NEVER:
        if re.search(rf"(?<![a-z-]){w}(?![a-z-])", low):
            bad(ctx, f"never-list word {w!r}")
    for name, pat in BANNED.items():
        m = re.search(pat, scan)
        if m:
            bad(ctx, f"{name} reaches the prompt: {m.group(0)!r}")
    digits = re.sub(r"three-position|three-quarter", " ", scan)
    if re.search(r"\d", digits):
        stray = re.findall(r"[^ ]*\d[^ ]*", digits)
        bad(ctx, f"a figure outside the drawn words: {stray}")
    if re.search(r"\b(man|woman)\b", low) and "north american" not in low:
        bad(ctx, "a person with no casting named")
    if e["person"] and "north american" not in low:
        bad(ctx, "the ledger says this frame has a person and none is cast")
    if not e["person"]:
        if "north american" in low:
            bad(ctx, "the ledger says this frame has no person and one is cast")
        if "no person" not in low:
            bad(ctx, "a frame with no person must say so, or the renderer adds one")

if fails:
    print(f"{len(prompts)} prompts, {len(fails)} failure(s)")
    for f in fails:
        print("FAIL", f)
    sys.exit(1)
forms = ", ".join(f"{f}x{used.count(f)}" for f in sorted(set(used)))
print(f"{len(prompts)} prompts, 0 failure(s); longest {max(len(p) for p in prompts)} characters; "
      f"forms: {forms}; studio {studios}/9, person {people}/9")

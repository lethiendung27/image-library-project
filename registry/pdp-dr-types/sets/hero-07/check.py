"""Check hero-07 against the hero section of registry/pdp-dr-instruction.md as ADR-122 left it.

Three prompts, the labelled form, one small product. The sentences and the two lock lines are not
typed here twice: they are READ OUT OF THE LAW FILE, so a law reworded again fails this set
instead of leaving it quietly stale.

Usage, from the repo root: python3 registry/pdp-dr-types/sets/hero-07/check.py [prompts.md]
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
FAN = "stand up in a stepped fan"
BANNED = {
    "a ratio": r"\b\d+\s*:\s*\d+\b",
    "an avoid clause": r"(?i)\bavoid\b",
    "a repo name": r"(\b0\d-[a-z]+-[a-z]+\b|--[a-z]|\bLP2\b|\bADR\b|\bG\d+\b|\bhero\.image\b)",
    "a construction word G2 keeps to the photograph": r"\b(aluminium|aluminum|carbon[- ]fibre|carbon[- ]fiber|PU leather|faraday)\b",
    "a figure": r"\b\d+(\.\d+)?\s?(cm|mm|in|g|MHz|%)\b",
    "an inset": r"\b(inset|callout|panel|split)\b(?! )",
    "a banned standing hero": r"\bstands? (?:up )?(?:full[- ]length|in the frame)\b",
}
L = lambda **k: k
LEDGER = {
    1: L(place="commuter train carriage", person=True, face=True, control=True,
         scene="sits by the window holding the wallet open"),
    2: L(place="plain wooden table", person=False, face=False, control=False,
         scene="Two hands hold the wallet open above the table"),
    3: L(place="fold-down table of a train seat", person=True, face=False, control=False,
         scene="The wallet lies open on the table close to the camera"),
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
    if not re.search(r"\bwallet\b", p, re.I):
        bad(ctx, "the product is not named")
    if FAN not in p and "standing up in a stepped fan" not in p:
        bad(ctx, "the set's one mechanism, the stepped fan, is missing")
    if '"' in p:
        bad(ctx, "a hero carries no words, and this one quotes some")

    scan = p.replace(BLOCK, " ")
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
    if not e["face"] and e["person"] and "out of focus" not in low:
        bad(ctx, "the ledger says a person with no face, and the prompt does not put them out of focus")

if sum(1 for e in LEDGER.values() if e["control"]) != 1:
    bad("set", "the set does not declare exactly one control")
if len({e["place"] for e in LEDGER.values()}) != len(LEDGER):
    bad("set", "two prompts share a place")

for f in fails:
    print("FAIL", f)
print(f"{len(prompts)} prompts, {len(fails)} failure(s); longest "
      f"{max((len(p) for p in prompts), default=0)} characters")
sys.exit(1 if fails else 0)

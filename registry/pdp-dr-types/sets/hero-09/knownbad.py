"""Prove check.py live: break hero-09 one rule at a time and require the fault back.

Usage, from the repo root: python3 registry/pdp-dr-types/sets/hero-09/knownbad.py
Exit 0 means every mutation was caught AND the clean set still passes.

A clean result from an untested checker is not evidence. The mutations are the faults this set
exists to avoid: hero-07's three (a head in the top band, the product left of the safe box, a
person asked to be soft who came back sharp) and ADR-136's three (a dark ground, a colourless
world, a mark on a hero). One family mutates the LAW file, so a hero sentence reworded in
`registry/pdp-dr-instruction.md` fails the set rather than leaving it stale.
"""
import io, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "check.py")
PROMPTS = os.path.join(HERE, "prompts.md")
SRC = io.open(PROMPTS, encoding="utf-8").read()
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
LAW = os.path.join(ROOT, "registry", "pdp-dr-instruction.md")
LAW_SRC = io.open(LAW, encoding="utf-8").read()
TMP_MD = os.path.join(HERE, "_knownbad_prompts.md")

LOOM = "a loom of red, yellow and blue wires"
ACROSS = "two thirds across"
BANDS1 = "the raised bonnet spans the top, the wing the bottom"

CASES = [
    # the bands, which is how hero-07 lost two faces
    ("the named surfaces leave the bands empty",
     lambda t: t.replace(BANDS1, "open sky above and below", 1),
     "bands are not FILLED"),
    # where the product sits across the picture
    ("the across-position is dropped",
     lambda t: t.replace("He holds the receiver " + ACROSS, "He holds the receiver near the middle", 1),
     "where across the picture"),
    # the world's colour
    ("the loom goes back to black tape",
     lambda t: t.replace(LOOM, "a loom in unbroken black harness tape", 1),
     "black harness tape"),
    ("the loom's colours are dropped",
     lambda t: t.replace(LOOM, "a loom of wires", 1),
     "loom's own colours are not named"),
    # the ground's value
    ("a dark studio comes back",
     lambda t: t.replace("Photograph in a home garage,", "Photograph in a dark studio,", 1),
     "dark studio"),
    ("a moody grade is smuggled in",
     lambda t: t.replace("A North American man", "In moody light, a North American man", 1),
     "moody"),
    # a hero carries no marks and no words
    ("a drawn mark reaches a hero",
     lambda t: t.replace("its tip on " + LOOM, "cyan arcs leaving its grille", 1),
     "drawn mark"),
    ("a hero quotes a word",
     lambda t: t.replace("His expression is relaxed.", 'The words "Find It Fast" are set once.', 1),
     "quotes some"),
    # casting and expression
    ("the casting is dropped",
     lambda t: t.replace("A North American man", "A man", 1),
     "casting"),
    ("the expression is dropped",
     lambda t: t.replace(" His expression is relaxed.", "", 1),
     "expression"),
    ("a no-face frame stops saying so",
     lambda t: t.replace("No face is in frame.", "", 1),
     "does not say so"),
    # the fixed law blocks
    ("a hero sentence is dropped",
     lambda t: t.replace("The product is big enough to recognise at a glance, never a small "
                         "detail in the distance.\n", "", 1),
     "hero sentence is missing"),
    ("the product block is dropped",
     lambda t: t.replace("Use the attached product photo as the exact reference. Preserve", "Preserve", 1),
     "product block appears 0"),
    ("the person sentence appears where the ledger says no person",
     lambda t: t.replace("No face is in frame.",
                         "No face is in frame. Any person turns slightly toward the left side "
                         "of the picture.", 1),
     "person sentence present"),
    # the set as a whole
    ("two prompts carry the same clear colour",
     lambda t: t.replace("forest-green sleeves", "mid-blue sleeves"),
     "clear colour"),
    ("a prompt is pushed over the gate",
     lambda t: t.replace("Photograph in a home garage,",
                         "Photograph in a home garage " + ("x" * 1800) + ",", 1),
     "LENGTH"),
]

LAW_CASES = [
    ("a hero sentence is reworded in the law",
     "The product is big enough to recognise at a glance, never a small detail in the distance.",
     "The product is big enough to see.",
     "hero sentence is missing"),
    ("a lock line is reworded in the law",
     "Light: bright daylight from the left, with natural shadows and real contrast.",
     "Light: daylight.",
     "the light line appears 0 times"),
]

failures = []


def run(path_md, law_text=None):
    backup = None
    if law_text is not None:
        backup = io.open(LAW, encoding="utf-8").read()
        io.open(LAW, "w", encoding="utf-8").write(law_text)
    try:
        r = subprocess.run([sys.executable, CHECK, path_md], capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr
    finally:
        if backup is not None:
            io.open(LAW, "w", encoding="utf-8").write(backup)


code, out = run(PROMPTS)
if code != 0:
    print("ABORT the clean set does not pass; fix that before trusting any mutation")
    print(out)
    sys.exit(2)

for name, mutate, expect in CASES:
    bad = mutate(SRC)
    if bad == SRC:
        failures.append(f"{name}: the mutation changed nothing - the anchor text has moved")
        print("  MISS " + name)
        continue
    io.open(TMP_MD, "w", encoding="utf-8").write(bad)
    code, out = run(TMP_MD)
    ok = code != 0 and expect in out
    if not ok:
        failures.append(f"{name}: " + ("NOT CAUGHT" if code == 0 else f"caught by the wrong rule (wanted {expect!r})"))
    print(("  ok   " if ok else "  MISS ") + name)

for name, old, new, expect in LAW_CASES:
    if old not in LAW_SRC:
        failures.append(f"{name}: anchor not in the law file")
        print("  MISS " + name)
        continue
    code, out = run(PROMPTS, LAW_SRC.replace(old, new, 1))
    ok = code != 0 and expect in out
    if not ok:
        failures.append(f"{name}: " + ("NOT CAUGHT" if code == 0 else f"caught by the wrong rule (wanted {expect!r})"))
    print(("  ok   " if ok else "  MISS ") + name)

if os.path.exists(TMP_MD):
    os.remove(TMP_MD)

code, out = run(PROMPTS)
if code != 0:
    failures.append("the clean set no longer passes after the run - the law file was not restored")

if failures:
    print(f"\nFAIL  {len(failures)} problem(s)")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print(f"\nPASS  {len(CASES) + len(LAW_CASES)} mutations, every one caught by its own rule, "
      f"and the clean set still passes")

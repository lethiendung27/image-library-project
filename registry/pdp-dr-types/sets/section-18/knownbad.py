"""Prove check.py live: break section-18 one rule at a time and require the fault back.

Usage, from the repo root: python3 registry/pdp-dr-types/sets/section-18/knownbad.py
Exit 0 means every mutation was caught AND the clean set still passes.

A clean result from an untested checker is not evidence, and this set's checker passed first try,
which is exactly when that matters. The mutations are ADR-136's four decisions, ADR-135's one cue,
and ADR-131's anatomy rule - the five things this set exists to hold. One family mutates the type
file, so a law reworded fails the set rather than leaving it stale.
"""
import io, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "check.py")
PROMPTS = os.path.join(HERE, "prompts.md")
SRC = io.open(PROMPTS, encoding="utf-8").read()
TYPE = os.path.abspath(os.path.join(HERE, "..", "..", "03-spec-overlay.md"))
TYPE_SRC = io.open(TYPE, encoding="utf-8").read()
TMP_MD = os.path.join(HERE, "_knownbad_prompts.md")

SILENT = "Nothing in the picture carries any lettering."
G6 = "Any screen shows only a picture, with no interface, text or numbers."
SUB1 = "The subject of this frame is the moment of contact"

CASES = [
    # STEP 0 - the subject of a delivery frame
    ("the subject is struck",
     lambda t: t.replace(SUB1, "", 1),
     "does not state its SUBJECT"),
    ("the subject slides back to the tool being held",
     lambda t: t.replace(SUB1, "The hero of this frame is the hub held in a hand", 1),
     "does not state its SUBJECT"),
    ("the readable-not-largest clause is struck",
     lambda t: t.replace("The hub is sharp, lit and unobstructed, nameable where it sits, and it "
                         "is not required to be the largest thing in the picture.",
                         "The hub is the largest thing in the picture.", 1),
     "readable-not-largest"),

    # WORDS - six of six silent
    ("a frame starts lettering",
     lambda t: t.replace(SILENT, 'The words "Locked Crash Clips" are set once in bold white.', 1),
     "no-lettering clause"),
    ("a drawn string is quoted",
     lambda t: t.replace("stands beside the hub", 'stands beside the hub under the word "LOCKED"', 1),
     "quotes a drawn string"),

    # CUE - one a frame, never a symbol of the medium
    ("a frame loses its cue",
     lambda t: t.replace("One thin white line icon of a closed padlock stands beside the hub",
                         "A padlock is implied", 1),
     "missing its one cue"),
    ("a symbol of the medium comes back",
     lambda t: t.replace("The subject of this frame is what is already on the card.",
                         "The subject of this frame is a filmstrip of the journey.", 1),
     "symbol of the medium"),
    ("a bird's-eye composite is drawn",
     lambda t: t.replace("carrying the road ahead", "carrying a bird's-eye composite of the car", 1),
     "symbol of the medium"),

    # GROUND - no dark frame
    ("a frame goes dark",
     lambda t: t.replace("in a daylit open car park", "in a dim open car park at night", 1),
     "dark ground"),

    # ANATOMY - ADR-131
    ("a lens cluster is asserted",
     lambda t: t.replace("sits sharp in the near foreground",
                         "sits sharp in the near foreground, its lens cluster forward", 1),
     "anatomy no photograph"),
    ("a status lamp is asserted",
     lambda t: t.replace("and running", "and running, its status lamp lit", 1),
     "anatomy no photograph"),
    ("a finish is asserted",
     lambda t: t.replace("The hub of the 360", "The matte black hub of the 360", 1),
     "anatomy no photograph"),

    # a figure the copy does not pay for
    ("an unearned figure reaches a prompt",
     lambda t: t.replace("seen from the side channel", "seen from the 120° side channel", 1),
     "figure the block's copy does not pay for"),

    # the screen sentence rides exactly where the screen appears
    ("the screen sentence is dropped where the screen shows",
     lambda t: t.replace("\n" + G6, "", 1) if "\n" + G6 in t else t.replace(" " + G6, "", 1),
     "screen sentence present"),

    # the shared clauses and the gate
    ("the art-direction wording drifts in one frame",
     lambda t: t.replace("The art direction is the real place in open daylight, bright enough to "
                         "read the moulding on the product, and the picture keeps the colour of "
                         "its own world.",
                         "The art direction is daylight.", 1),
     "art-direction clause"),
    ("G1 is dropped",
     lambda t: t.replace(" Use the attached product photo as the exact reference.\n```",
                         "\n```", 1),
     "does not close with G1"),
    ("a prompt is pushed over the gate",
     lambda t: t.replace("Editorial realism product feature image seen from inside a parked car",
                         "Editorial realism product feature image " + ("x" * 1800) +
                         " seen from inside a parked car", 1),
     "over the 1800 gate"),
]

LAW_CASES = [
    ("the type drops back to 0.18", 'version: "0.19"', 'version: "0.18"', "not at 0.19"),
    ("the OBJECT/DELIVERY clause is reworded away",
     "OBJECT claim or a DELIVERY claim", "OBJECT claim or another kind", "OBJECT claim or a DELIVERY"),
    ("the window clause is reworded away",
     "WINDOW onto the hidden state", "picture of the hidden state", "WINDOW onto the hidden state"),
]

failures = []


def run(path_md, law_text=None):
    backup = None
    if law_text is not None:
        backup = io.open(TYPE, encoding="utf-8").read()
        io.open(TYPE, "w", encoding="utf-8").write(law_text)
    try:
        r = subprocess.run([sys.executable, CHECK, path_md], capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr
    finally:
        if backup is not None:
            io.open(TYPE, "w", encoding="utf-8").write(backup)


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
    if old not in TYPE_SRC:
        failures.append(f"{name}: anchor not in the type file")
        print("  MISS " + name)
        continue
    code, out = run(PROMPTS, TYPE_SRC.replace(old, new, 1))
    ok = code != 0 and expect in out
    if not ok:
        failures.append(f"{name}: " + ("NOT CAUGHT" if code == 0 else f"caught by the wrong rule (wanted {expect!r})"))
    print(("  ok   " if ok else "  MISS ") + name)

if os.path.exists(TMP_MD):
    os.remove(TMP_MD)

code, out = run(PROMPTS)
if code != 0:
    failures.append("the clean set no longer passes after the run - the type file was not restored")

if failures:
    print(f"\nFAIL  {len(failures)} problem(s)")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print(f"\nPASS  {len(CASES) + len(LAW_CASES)} mutations, every one caught by its own rule, "
      f"and the clean set still passes")

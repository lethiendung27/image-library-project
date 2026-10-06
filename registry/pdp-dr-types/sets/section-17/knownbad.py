"""Prove check.py live: break section-17 one rule at a time and require the fault back.

Usage, from the repo root: python3 registry/pdp-dr-types/sets/section-17/knownbad.py
Exit 0 means every mutation was caught AND the clean set still passes.

A clean result from an untested checker is not evidence. The mutations follow ADR-136's four
decisions, because those are what this set exists to test: the SUBJECT of a delivery frame, the
ground's value, the world's colour, and the drawn word. Two further families mutate the type file,
so a law reworded fails the set rather than leaving it stale.
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
HARNESS = "red, yellow, blue and green wires in their factory colours"
READABLE = ("The receiver is sharp, lit and unobstructed, nameable where it sits, and it is not "
            "required to be the largest thing in the picture.")
OWNCOLOUR = "the picture keeps the colour of its own world"
G1 = "Use the attached product photo as the exact reference."

# name, mutation (text -> text), the substring the failure line must contain
CASES = [
    # STEP 0 - the subject of a delivery frame
    ("subject struck from frame 1",
     lambda t: t.replace("The subject of this frame is the break the tool has found.", ""),
     "does not state its SUBJECT"),
    ("subject becomes the tool touching something",
     lambda t: t.replace("The subject of this frame is the break the tool has found.",
                         "The hero of this frame is the sensing tip touching the bundle."),
     "does not state its SUBJECT"),
    ("the readable-not-largest clause struck",
     lambda t: t.replace(READABLE, "The receiver is the largest thing in the picture.", 1),
     "readable-not-largest"),

    # GROUND - no dark frame
    ("a dark studio art direction comes back",
     lambda t: t.replace("The art direction is a white seamless studio: a bright, even key raked",
                         "The art direction is a dark studio: a bright key raked"),
     "dark studio"),
    ("a dim scene smuggled in by another word",
     lambda t: t.replace("daylight from the open roller door", "dim light from the open roller door"),
     "dark frames found"),

    # COLOUR - the world's own colour
    ("the harness goes back to black tape",
     lambda t: t.replace(HARNESS, "wires wrapped in unbroken black harness tape", 1),
     "factory colours"),
    ("the own-colour clause struck",
     lambda t: t.replace(OWNCOLOUR, "everything else is held in neutral greys", 1),
     "neutral greys"),

    # WORDS - five of six silent
    ("a silent frame letters",
     lambda t: t.replace(SILENT,
                         'The words "Find The Break" are set once in plain bold white letters.', 1),
     "no-lettering clause"),
    ("the icon label is dropped from frame 4",
     lambda t: t.replace('the words "CLIPS SEATED" are set once under it in plain bold dark letters '
                         'on the white ground, ', ""),
     "expected to letter"),

    # CUE - ADR-135 is untouched
    ("frame 3 loses its cue",
     lambda t: t.replace("Short luminous cyan pulses rise out of the gap into the open air",
                         "The tone is audible"),
     "missing its one cue"),
    ("frame 1's window is dropped",
     lambda t: t.replace("A clean circular inset, about a third of the picture wide, floats beside "
                         "the harness", "A note beside the harness"),
     "missing its one cue"),

    # the shared clauses and the gate
    ("G1 dropped from a prompt",
     lambda t: t.replace(G1 + "\n```", "```", 1),
     "does not close with G1"),
    ("a prompt pushed over the character gate",
     lambda t: t.replace("Editorial realism product feature image in an engine bay",
                         "Editorial realism product feature image " + ("x" * 1800) + " in an engine bay", 1),
     "over the 1800 gate"),
    ("the control stops being declared",
     lambda t: t.replace("CONTROL and it is predicted to FAIL", "a sixth frame"),
     "not declared as a control"),
]

# mutations of the LAW, so a reworded type file fails the set
LAW_CASES = [
    ("the type drops back to 0.18", 'version: "0.19"', 'version: "0.18"', "not at 0.19"),
    ("the OBJECT/DELIVERY clause is reworded away",
     "OBJECT claim or a DELIVERY claim", "OBJECT claim or a different claim", "OBJECT claim or a DELIVERY"),
    ("the readable clause is reworded away",
     "most READABLE thing in the frame, not necessarily the largest",
     "largest thing in the frame", "most READABLE thing"),
    ("the no-echo clause is reworded away",
     "never restates a word the page already prints",
     "never repeats the page", "never restates a word"),
]

failures = []


def run(path_md, law_text=None):
    law_backup = None
    if law_text is not None:
        law_backup = io.open(TYPE, encoding="utf-8").read()
        io.open(TYPE, "w", encoding="utf-8").write(law_text)
    try:
        r = subprocess.run([sys.executable, CHECK, path_md], capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr
    finally:
        if law_backup is not None:
            io.open(TYPE, "w", encoding="utf-8").write(law_backup)


code, out = run(PROMPTS)
if code != 0:
    print("ABORT the clean set does not pass; fix that before trusting any mutation")
    print(out)
    sys.exit(2)

for name, mutate, expect in CASES:
    bad = mutate(SRC)
    if bad == SRC:
        failures.append(f"{name}: the mutation changed nothing - the anchor text has moved")
        continue
    io.open(TMP_MD, "w", encoding="utf-8").write(bad)
    code, out = run(TMP_MD)
    if code == 0:
        failures.append(f"{name}: NOT CAUGHT")
    elif expect not in out:
        failures.append(f"{name}: caught, but not by the expected rule (wanted '{expect}')")
    print(("  ok   " if code != 0 and expect in out else "  MISS ") + name)

for name, old, new, expect in LAW_CASES:
    if old not in TYPE_SRC:
        failures.append(f"{name}: anchor '{old[:36]}' not in the type file")
        continue
    code, out = run(PROMPTS, TYPE_SRC.replace(old, new, 1))
    if code == 0:
        failures.append(f"{name}: NOT CAUGHT")
    elif expect not in out:
        failures.append(f"{name}: caught, but not by the expected rule (wanted '{expect}')")
    print(("  ok   " if code != 0 and expect in out else "  MISS ") + name)

if os.path.exists(TMP_MD):
    os.remove(TMP_MD)

# and the clean set still passes, after every mutation has been reverted
code, out = run(PROMPTS)
if code != 0:
    failures.append("the clean set no longer passes after the run - a temp file leaked")

if failures:
    print(f"\nFAIL  {len(failures)} problem(s)")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print(f"\nPASS  {len(CASES) + len(LAW_CASES)} mutations, every one caught by its own rule, "
      f"and the clean set still passes")

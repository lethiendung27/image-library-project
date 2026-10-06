"""Check section-17 against `03-spec-overlay` v0.19: ADR-136's four changes, and nothing else.

`section-16` passed its own checker and failed the owner, so this one checks the four axes his
verdict names rather than the ones the last set could already hold:

  STEP 0   every block is classified OBJECT or DELIVERY in the notes, and a DELIVERY frame states
           its SUBJECT as the thing the tool delivers - never as the tool touching something.
  GROUND   no frame is dark. `dark studio` is banned by name in this set, because the product is
           matte black and emits nothing (ADR-136).
  COLOUR   every frame that has a harness in it names the factory colours. `black harness tape`,
           which this lane wrote into section-16 and which cost the round its colour, is banned
           by name.
  WORDS    five of six carry NO lettering at all, and the two that letter are frame 4 (an icon
           label the page does not print) and frame 6 (the control, which letters on purpose).
  CUE      ADR-135 is untouched: every frame carries exactly ONE cue, and a frame with no words
           still owes one. A caption is not a cue.

The type's own clauses are READ OUT OF THE TYPE FILE, so a law reworded again fails this set
instead of leaving it quietly stale.

Usage, from the repo root: python3 registry/pdp-dr-types/sets/section-17/check.py [prompts.md]
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
PRODUCT = "Automotive Circuit Tester"
G1 = "Use the attached product photo as the exact reference."
NOSCREEN = "Neither body carries a screen, a display or a numeric readout of any kind."
CLOSED = "Nothing in the picture is cut, stripped, unwrapped or taken apart."
READABLE = ("The receiver is sharp, lit and unobstructed, nameable where it sits, and it is not "
            "required to be the largest thing in the picture.")
OWNCOLOUR = "the picture keeps the colour of its own world"
SILENT = "Nothing in the picture carries any lettering."
HARNESS = "red, yellow, blue and green wires in their factory colours"

# ADR-136: what each frame is OF, in its own words, and the one cue it carries
SUBJECT = {
    1: "The subject of this frame is the break the tool has found.",
    2: "The subject of this frame is the distance the tone covers",
    3: "The subject of this frame is what is behind the panel, reached through that gap.",
    4: "The subject of this frame is the panel still whole with its fasteners in it.",
    5: "The subject of this frame is the dial",
}
CUE = {
    1: "A clean circular inset, about a third of the picture wide, floats beside the harness",
    2: "the printed arc of dots on its body is lit and the sharpest detail in the frame",
    3: "Short luminous cyan pulses rise out of the gap into the open air",
    4: "One thin white line icon of a trim clip, seated in its hole",
    5: "a specular highlight runs up that scale",
    6: "One thin white line icon of a screwdriver with a bar struck through it",
}
LETTERS = {4: '"CLIPS SEATED"', 6: '"Non Destructive Tracing"'}
SILENT_FRAMES = (1, 2, 3, 5)
HARNESS_FRAMES = (1, 2, 3, 4)
# banned by name: the two clauses this lane wrote that ADR-136 holds responsible
BANNED = {
    r"dark studio": "the dark ground, under a product that emits nothing (ADR-136 decision 3)",
    r"black harness tape": "the colourless world this lane asked for (ADR-136 decision 4)",
    r"held in neutral greys": "the clause that drained section-15 (ADR-135)",
}

fails = []


def need(cond, msg):
    if not cond:
        fails.append(msg)


blocks = re.findall(r"```\n(.*?)\n```", text, re.S)
need(len(blocks) == 6, f"expected 6 prompts, found {len(blocks)}")

for i, p in enumerate(blocks, 1):
    tag = f"prompt {i}"
    need(len(p) <= GATE, f"{tag}: {len(p)} characters, over the {GATE} gate")
    need(p.startswith(OPEN), f"{tag}: does not open with '{OPEN}'")
    need(PRODUCT in p, f"{tag}: does not name the {PRODUCT}")
    need(p.endswith(G1), f"{tag}: does not close with G1")
    need(NOSCREEN in p, f"{tag}: missing the no-screen clause")
    need(CLOSED in p, f"{tag}: missing the nothing-taken-apart clause")
    need(OWNCOLOUR in p, f"{tag}: missing '{OWNCOLOUR}' - the accent binds the drawn layer only")
    for pat, why in BANNED.items():
        need(not re.search(pat, p, re.I), f"{tag}: carries '{pat}' - {why}")
    need(CUE[i] in p, f"{tag}: missing its one cue - expected '{CUE[i][:48]}...'")
    if i in SUBJECT:
        need(SUBJECT[i] in p, f"{tag}: does not state its SUBJECT in the set's words (step 0)")
        need(READABLE in p, f"{tag}: missing the readable-not-largest clause (ADR-136 decision 2)")
    if i in SILENT_FRAMES:
        need(SILENT in p, f"{tag}: must carry the no-lettering clause")
        need('"' not in p.replace(SILENT, ""), f"{tag}: quotes a drawn string in a silent frame")
    if i in LETTERS:
        need(LETTERS[i] in p, f"{tag}: expected to letter {LETTERS[i]}")
    if i in HARNESS_FRAMES:
        need(HARNESS in p, f"{tag}: has a harness and does not name its factory colours")

# the set as a whole
lettered = [i for i, p in enumerate(blocks, 1) if re.search(r'[Tt]he words "', p)]
need(lettered == [4, 6], f"set: lettering expected in frames 4 and 6, found {lettered}")
need(len([i for i in lettered]) <= 2, "set: more than two of six letter (ADR-136 decision 5)")
dark = [i for i, p in enumerate(blocks, 1) if re.search(r"dark studio|near-black|dim ", p, re.I)]
need(not dark, f"set: dark frames found at {dark}; this set has none (ADR-136 decision 3)")

# the control must be declared, and declared as predicted to fail
need("CONTROL and it is predicted to FAIL" in text, "set: the control is not declared as a control")
need(re.search(r"\|\s*6\s*\|.*control|CONTROL", text, re.I), "set: frame 6 is not marked the control")

# the law this set claims to follow must still say what the set says it says
need('version: "0.19"' in law, "type: 03-spec-overlay is not at 0.19 - this set was written for it")
for clause in ("OBJECT claim or a DELIVERY claim",
               "most READABLE thing in the frame, not necessarily the largest",
               "never restates a word the page already prints",
               "read off the PRODUCT, never chosen as a style",
               "WINDOW onto the hidden state"):
    need(clause in law, f"type: the clause '{clause[:40]}...' is gone from 03-spec-overlay.md")

if fails:
    print(f"FAIL  {len(fails)} problem(s) in section-17")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print(f"PASS  section-17: {len(blocks)} prompts, 4 silent, 2 lettered, 0 dark, control declared")

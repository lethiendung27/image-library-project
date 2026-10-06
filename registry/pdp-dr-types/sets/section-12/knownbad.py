"""Prove check.py live: break section-12 one rule at a time and require the fault back.

Usage, from the repo root: python3 registry/pdp-dr-types/sets/section-12/knownbad.py
Exit 0 means every mutation was caught AND the clean set still passes.

Three families of mutation, because three different files hold the law this set obeys:
  PROMPTS  — the nine prompts themselves
  TYPE     — `03-spec-overlay.md`, so a law reworded again fails this set rather than leaving it
             quietly stale (the trap found firing on `sets/hero-07/` on 2026-10-05)
  LEDGER   — check.py's own table of what each frame is, which is what the set-shape rules read;
             a mutation here proves the spread, register and person rules are live and not just
             arithmetic over a table that happens to be right.

A clean result from an untested checker is not evidence. This checker's first run on the rewritten
set found a real fault — the word CONTROL marked twice — and the run before that was wrong three
ways at once.
"""
import io, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "check.py")
PROMPTS = os.path.join(HERE, "prompts.md")
SRC = io.open(PROMPTS, encoding="utf-8").read()
CHECK_SRC = io.open(CHECK, encoding="utf-8").read()
TYPE = os.path.abspath(os.path.join(HERE, "..", "..", "03-spec-overlay.md"))
TYPE_SRC = io.open(TYPE, encoding="utf-8").read()
TMP_MD = os.path.join(HERE, "_knownbad_prompts.md")
TMP_PY = os.path.join(HERE, "_knownbad_check.py")

NOTEXT = "Nothing else in the picture carries text."
G1 = "Use the attached product photo as the exact reference."
CABLE = "Nothing is drawn on any wire, loom or cable."
TAG = ("set once in plain bold white letters directly on the photograph with a soft dark edge, "
       "no plate or band behind them, the capitals about a twentieth of the picture's height "
       "and the line running between a quarter and a third of its width")
ICON = ("Three line icons in thin white strokes, each inside its own rounded square outline, "
        "stand in a row across the top of the frame, and under each one its name is set in "
        "plain bold white capitals directly on the picture:")
CALLOUT = ("Three short labels in plain bold white stand on straight white leader lines, each "
           "line ending ON the part it names, set directly on the picture with no plate behind "
           "them:")
FIGURE = ("stands inside a drawn card with a thin glowing cyan border and a faint translucent "
          "fill, floating in the scene beside the product at about the size of a hand, the "
          "figure itself in plain bold white.")
MARK = ("A set of concentric arcs in luminous cyan stands in the air between them, each arc "
        "thinner than the last, reaching the cable without touching it.")
LIGHT_STUDIO = ("The light is studio light on a seamless ground — one soft key from the left and a "
                "cool rim behind — true colour, neutral whites, no cast over the picture; the colour "
                "comes from the product and its own leads.")
N = {str(i): i for i in range(1, 10)}


def blocks(t):
    return re.findall(r"```\n(.+?)\n```", t, re.S)


def edit(t, key, a, b, count=1):
    old = blocks(t)[N[key] - 1]
    assert a in old, f"anchor missing in {key}: {a[:60]!r}"
    return t.replace(old, old.replace(a, b, count), 1)


def append(t, key, extra):
    old = blocks(t)[N[key] - 1]
    return t.replace(old, old + " " + extra, 1)


def drop_block(t, key):
    old = blocks(t)[N[key] - 1]
    return t.replace("```\n" + old + "\n```", "", 1)


PROMPT_CASES = [
    # ---- the per-form clauses, word for word
    ("the tag clause dropped", lambda t: edit(t, "2", TAG, "set small in the corner"),
     "the tag clause appears 0 times"),
    ("the old pre-ADR-128 tag wording", lambda t: edit(
        t, "8", TAG, "set once in plain bold white letters with a soft dark edge, the capitals about "
        "a twentieth of the picture's height and the line running a quarter of its width"),
     "the tag clause appears 0 times"),
    ("the icon clause dropped", lambda t: edit(t, "1", ICON, "Three small icons sit at the top:"),
     "the icon clause appears 0 times"),
    ("the callout clause dropped", lambda t: edit(t, "3", CALLOUT, "Three labels point at parts:"),
     "the callout clause appears 0 times"),
    ("the figure card taken away", lambda t: edit(t, "4", FIGURE, "is set in plain bold white."),
     "the figure clause appears 0 times"),
    ("the mark clause dropped", lambda t: edit(t, "7", MARK, "A blue glow sits near the cable."),
     "the mark clause appears 0 times"),
    ("a frame carrying another form's clause", lambda t: append(t, "5", ICON + " a fuse under FUSES."),
     "carrying the icon clause"),
    ("a view frame given a drawn word",
     lambda t: append(t, "9", 'The words "True RMS" are set once.'),
     "a view frame carries a drawn word"),

    # ---- ADR-129: a plate under a headline or a label
    ("a plate behind a headline", lambda t: append(t, "2", "A dark plate sits behind the words."),
     "a plate behind a headline or a label"),
    ("a card behind a callout label", lambda t: append(t, "3", "A card sits behind the labels."),
     "a plate behind a headline or a label"),

    # ---- the register
    ("a studio frame given the place's light clause",
     lambda t: edit(t, "6", LIGHT_STUDIO,
                    "The light is the place's own — a work lamp and the daylight behind it — true "
                    "colour, neutral whites, no cast over the picture; the colour comes from the "
                    "scene itself: the bare concrete."),
     "the studio light clause appears 0 times"),
    ("a studio frame that stops saying it has no place",
     lambda t: edit(t, "1", "with no place and no person", "in a workshop corner, no person"),
     "does not say it has no place"),
    ("a no-person frame that stops saying so",
     lambda t: edit(t, "5", ", no person and no drawn layer", " and no drawn layer"),
     "must say so"),
    ("a person cast into a product-led frame",
     lambda t: edit(t, "7", "no person in frame", "a North American man in his fifties watches"),
     "no person and one is cast"),

    # ---- ADR-128, still binding
    ("a hand closing a clamp", lambda t: edit(
        t, "4", "its two leads already run to the posts with the red clamp bitten on the positive",
        "a hand closes the red clamp onto the positive post"),
     "a hand acts on a clip or clamp"),
    ("a drawn glow along the cable",
     lambda t: append(t, "8", "A soft blue glow runs along the cable from the outlet."),
     "a drawn light on a wire, loom or cable"),
    ("the cable clause dropped", lambda t: edit(t, "9", " " + CABLE, ""),
     "the cable clause appears 0 times"),
    ("the mark named as a graphic", lambda t: append(t, "1", "A band of light marks the spot."),
     "named as a graphic"),

    # ---- the lock and the frame's own identity
    ("the no-other-text line dropped", lambda t: edit(t, "6", " " + NOTEXT, ""),
     "the no-other-text clause appears 0 times"),
    ("the reference not last", lambda t: append(t, "3", "The frame is square to the subject."),
     "the reference sentence is not last"),
    ("the untouched-claim sentence dropped", lambda t: edit(
        t, "2", " Nothing in the picture is cut, stripped or unwrapped: every wire stays taped and whole.", ""),
     "the untouched-claim sentence appears 0 times"),
    ("the product unnamed",
     lambda t: edit(t, "9", "the True RMS Digital Multimeter", "the meter"),
     "the product is not named"),
    ("the frame's anchor gone", lambda t: edit(
        t, "7", "held a finger's width from a grey cable", "resting against a grey cable"),
     "the frame's anchor is missing"),
    ("extra drawn words", lambda t: append(t, "4", 'The words "Winter ready" are set beside it.'),
     "the drawn words are"),

    # ---- the never-list and the banned patterns
    ("a never-list word", lambda t: append(t, "1", "The result is proven."), "never-list word"),
    ("a ratio", lambda t: append(t, "6", "The frame is 4:3."), "a ratio reaches the prompt"),
    ("a repo name", lambda t: append(t, "5", "This fills the LP2 slot."), "a repo name reaches the prompt"),
    ("a stray figure", lambda t: append(t, "3", "The leader lines are 40 mm long."),
     "a figure outside the drawn words"),
    ("an inset", lambda t: append(t, "9", "An inset shows the dial."),
     "an inset the type did not ask for"),

    # ---- the set's own shape
    ("a prompt dropped", lambda t: drop_block(t, "6"), "8 prompts, the ledger has 9"),
    ("two controls", lambda t: t.replace("### 9 — `view` · the screen itself · **CONTROL**",
                                         "### 9 — `view` · the screen itself · **CONTROL**\n\nAlso **CONTROL**"),
     "controls in prose"),
    ("a prompt over the gate",
     lambda t: append(t, "1", "The ground behind is dark and deep and empty of everything. " * 12),
     "LENGTH"),
]

TYPE_CASES = [
    ("the type's form-spread rule reworded",
     lambda t: t.replace("A SET spans the overlay forms", "A set may repeat one overlay form"),
     "no longer asks a set to span the forms"),
    ("the type's product-led rule reworded",
     lambda t: t.replace("A feature frame is PRODUCT-LED", "A feature frame is person-led"),
     "no longer makes a feature frame product-led"),
    ("the type's figure exemption reworded",
     lambda t: t.replace("is the exception and keeps its card", "carries no card"),
     "no longer exempts the figure"),
    ("the type's figure card unnamed",
     lambda t: t.replace("the FIGURE CARD, a drawn", "a plain box, a drawn"),
     "no longer names the figure card as its own device"),
    ("the type's mark-in-the-air rule reworded",
     lambda t: t.replace("may sit in the AIR between the product and its subject",
                         "may not sit in the air"),
     "no longer allows a mark to stand in the air"),
    ("the type's clip ban reworded",
     lambda t: t.replace("no hand closes, presses or holds a clip", "a hand may close a clip"),
     "no longer bans a hand on a clip"),
    ("the type's cable ban reworded",
     lambda t: t.replace("Nothing is drawn ON a wire, a loom or a cable", "A mark may sit on a cable"),
     "no longer bans a mark on a cable"),
    ("the type version moved",
     lambda t: t.replace('version: "0.13"', 'version: "0.14"'), "the type is no longer 0.13"),
]

# the set-shape rules read check.py's own ledger, so they are proved by mutating it
LEDGER_CASES = [
    ("the set collapsed to one form",
     lambda t: re.sub(r'form="(icon|callout|figure|mark|view)"', 'form="tag"', t),
     "is used 9 times"),
    ("one form played four times",
     lambda t: t.replace('form="callout"', 'form="icon"').replace('form="mark"', 'form="icon"'),
     "is used 4 times"),
    ("only three forms left",
     lambda t: t.replace('form="callout"', 'form="tag"').replace('form="mark"', 'form="tag"')
                .replace('form="figure"', 'form="icon"').replace('form="view"', 'form="icon"'),
     "ADR-129 asks for at least four of six"),
    ("the studio frames turned into places",
     lambda t: t.replace('form="icon", studio=True', 'form="icon", studio=False')
                .replace('form="view",\n           studio=True', 'form="view",\n           studio=False'),
     "studio frames; the owner's corpus is 8 of 17"),
    ("a third person let in",
     lambda t: t.replace('form="mark", studio=False,\n           person=False',
                         'form="mark", studio=False,\n           person=True'),
     "frames carry a person"),
    ("the control dropped from the ledger",
     lambda t: t.replace('person=False, control=True', 'person=False, control=False'),
     "exactly one control"),
    ("two products instead of three",
     lambda t: t.replace('product="True RMS Digital Multimeter"', 'product="Automotive Circuit Tester"'),
     "three products"),
]


def run(md_path, py_path):
    r = subprocess.run([sys.executable, py_path, md_path], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main():
    rc, out = run(PROMPTS, CHECK)
    if rc != 0:
        print("the clean set does not pass, so no mutation proves anything:\n" + out)
        sys.exit(1)
    bad = 0

    def report(name, rc, out, expect):
        nonlocal bad
        if rc != 0 and expect in out:
            print(f"caught {name}")
        else:
            bad += 1
            print(f"MISSED {name}: expected {expect!r}, rc={rc}\n  " + "\n  ".join(out.splitlines()[:3]))

    for name, mutate, expect in PROMPT_CASES:
        md = mutate(SRC)
        assert md != SRC, f"{name}: the mutation changed nothing"
        io.open(TMP_MD, "w", encoding="utf-8").write(md)
        report(name, *run(TMP_MD, CHECK), expect=expect)

    for name, mutate, expect in LEDGER_CASES:
        py = mutate(CHECK_SRC)
        assert py != CHECK_SRC, f"{name}: the ledger mutation changed nothing"
        io.open(TMP_PY, "w", encoding="utf-8").write(py)
        report(name, *run(PROMPTS, TMP_PY), expect=expect)

    for name, mutate, expect in TYPE_CASES:
        mutated = mutate(TYPE_SRC)
        assert mutated != TYPE_SRC, f"{name}: the type mutation changed nothing"
        io.open(TYPE, "w", encoding="utf-8").write(mutated)
        try:
            rc, out = run(PROMPTS, CHECK)
        finally:
            io.open(TYPE, "w", encoding="utf-8").write(TYPE_SRC)
        report(name, rc, out, expect=expect)

    for f in (TMP_MD, TMP_PY):
        if os.path.exists(f):
            os.remove(f)
    assert io.open(TYPE, encoding="utf-8").read() == TYPE_SRC, "the type file was left mutated"
    total = len(PROMPT_CASES) + len(LEDGER_CASES) + len(TYPE_CASES)
    print(f"{total} mutations, {bad} problem(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

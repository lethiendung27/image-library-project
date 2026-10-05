"""Prove check.py live: break hero-07 one rule at a time and require the fault back.

Usage, from the repo root: python3 registry/pdp-dr-types/sets/hero-07/knownbad.py
Exit 0 means every mutation was caught AND the clean set still passes. A clean result from an
untested checker is not evidence.

Two cases also mutate a copy of the LAW file, because this set reads the hero sentences out of
`registry/pdp-dr-instruction.md` rather than copying them: a reworded law must fail the set.
"""
import io, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "check.py")
SRC = io.open(os.path.join(HERE, "prompts.md"), encoding="utf-8").read()
CHECK_SRC = io.open(CHECK, encoding="utf-8").read()
TMP_MD = os.path.join(HERE, "_knownbad_prompts.md")
TMP_PY = os.path.join(HERE, "_knownbad_check.py")

BLOCK_TAIL = "no part is tinted toward the set's accent."
PERSON = "Any person turns slightly toward the left side of the picture."
THIRD = ("The group fills about a third of the picture's height and sits across the middle, and no "
         "face, no hand and no part of the product reaches into the top third or the bottom third.")
LIGHT = "Light: bright daylight from the left, with natural shadows and real contrast."
GRADE = "Grade: true colour, neutral whites, no warm filter and no glow."
WORDLESS = "Nothing in the picture carries a word, a number, a label or a badge."
CORNER = "Nothing is placed in the bottom-right corner of the frame."
FAN = "stand up in a stepped fan"


def blocks(t):
    return re.findall(r"```\n(.+?)\n```", t, re.S)


def edit(t, n, a, b, count=1):
    bs = blocks(t)
    old = bs[n - 1]
    assert a in old, f"anchor missing in prompt {n}: {a[:50]!r}"
    return t.replace(old, old.replace(a, b, count), 1)


def append(t, n, extra):
    old = blocks(t)[n - 1]
    return t.replace(old, old + "\n" + extra, 1)


CASES = [
    ("the product block dropped", lambda t: edit(t, 1, "Use the attached product photo", "Use the photo"),
     None, "the LP2 product block appears 0"),
    ("a hero sentence dropped", lambda t: edit(t, 1, THIRD + "\n", ""), None,
     "a hero sentence is missing or doubled"),
    ("a hero sentence reworded", lambda t: edit(t, 2, "the top third or the bottom third",
                                                "the top fifth or the bottom fifth"), None,
     "a hero sentence is missing or doubled"),
    ("the person sentence on a hands-only frame", lambda t: append(t, 2, PERSON), None,
     "the person sentence present=True, ledger says False"),
    ("the person sentence missing", lambda t: edit(t, 1, "\n" + PERSON, ""), None,
     "the person sentence present=False"),
    ("the light line reworded", lambda t: edit(t, 3, "bright daylight from the left",
                                               "warm daylight from the left"), None,
     "the light line appears 0"),
    ("the grade line reworded", lambda t: edit(t, 1, "no warm filter and no glow",
                                               "a warm filter and a soft glow"), None,
     "the grade line appears 0"),
    ("the wordless line dropped", lambda t: edit(t, 2, WORDLESS + "\n", ""), None,
     "the wordless line appears 0"),
    ("the corner line dropped", lambda t: edit(t, 3, "\n" + CORNER, ""), None,
     "the corner line appears 0"),
    ("the setting line reworded", lambda t: edit(t, 1, "where the colours are the carriage's own",
                                                 "in muted tones"), None, "no setting line in the law's form"),
    ("the opening is not a photograph", lambda t: edit(t, 1, "Photograph inside a commuter train carriage",
                                                       "A cinematic shot inside a commuter train carriage"),
     None, "a hero prompt opens with the photograph it is"),
    ("the one-frame clause dropped", lambda t: edit(t, 2, ", one frame, no panels, no insets, no words.", "."),
     None, "the opening sentence does not end with the one-frame clause"),
    ("the mechanism dropped", lambda t: edit(t, 2, "the cards stand up in a stepped fan",
                                             "the cards come out"), None, "the stepped fan, is missing"),
    ("the product unnamed", lambda t: edit(t, 2, "hold the wallet open above the table",
                                           "hold it open above the table"), None,
     "the product is not named"),
    ("a construction word", lambda t: edit(t, 1, "holding the wallet open",
                                           "holding the aluminium wallet open"), None,
     "a construction word"),
    ("a figure", lambda t: append(t, 1, "The wallet is 1.5 cm thick."), None, "a figure reaches the prompt"),
    ("a ratio", lambda t: append(t, 3, "Frame it 16:9."), None, "a ratio reaches the prompt"),
    ("an avoid clause", lambda t: append(t, 2, "Avoid clutter."), None, "an avoid clause"),
    ("a repo name", lambda t: append(t, 1, "Route it as 06-relief-hero."), None, "a repo name"),
    ("words in the frame", lambda t: append(t, 1, 'A sign reads "Secure".'), None,
     "a hero carries no words"),
    ("uncast person", lambda t: edit(t, 1, "A North American man", "A man"), None,
     "a person with no casting named"),
    ("a face with no expression", lambda t: edit(t, 1, " His expression is natural and relaxed.", ""),
     None, "a face in frame with no expression named"),
    ("a person brought into focus", lambda t: edit(t, 3, "sits out of focus, relaxed",
                                                   "sits sharp and smiling"), None,
     "does not put them out of focus"),
    ("the ledger's place gone", lambda t: edit(t, 2, "plain wooden table", "kitchen worktop", 99), None,
     "the ledger's place is not in the prompt"),
    ("over the gate", lambda t: edit(t, 2, "above the table", "above the table " + "x" * 200), None,
     "LENGTH"),
    ("a prompt dropped", lambda t: t.replace("```\n" + blocks(t)[2] + "\n```", "", 1), None,
     "2 prompts, the ledger has 3"),
    # the ledger and the law
    ("two controls", None, lambda c: c.replace('face=False, control=False,\n         scene="Two hands',
                                               'face=False, control=True,\n         scene="Two hands'),
     "does not declare exactly one control"),
    ("two prompts share a place", None,
     lambda c: c.replace('place="fold-down table of a train seat"', 'place="plain wooden table"'),
     "two prompts share a place"),
]

LAW_CASES = [
    ("the law reworded a hero sentence",
     lambda law: law.replace("The group fills about a third of the picture's height",
                             "The group fills about half the picture's height", 1),
     "a hero sentence is missing or doubled"),
    ("the law reworded the lock",
     lambda law: law.replace("Light: bright daylight from the left, with natural shadows and real contrast.",
                             "Light: soft daylight from one side.", 1),
     "the light line appears 0"),
]

LAW = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "registry", "pdp-dr-instruction.md"))


def run(md_path, py_path):
    out = subprocess.run([sys.executable, py_path, md_path], capture_output=True, text=True)
    return out.returncode, out.stdout + out.stderr


def main():
    bad = 0
    rc, out = run(os.path.join(HERE, "prompts.md"), CHECK)
    if rc != 0:
        bad += 1
        print("CLEAN SET FAILED:\n" + out)
    for name, mutate_md, mutate_py, expect in CASES:
        md = mutate_md(SRC) if mutate_md else SRC
        py = mutate_py(CHECK_SRC) if mutate_py else CHECK_SRC
        if mutate_md:
            assert md != SRC, f"{name}: the prompt mutation changed nothing"
        if mutate_py:
            assert py != CHECK_SRC, f"{name}: the checker mutation changed nothing"
        io.open(TMP_MD, "w", encoding="utf-8").write(md)
        io.open(TMP_PY, "w", encoding="utf-8").write(py)
        rc, out = run(TMP_MD, TMP_PY)
        if rc != 0 and expect in out:
            print(f"caught {name}")
        else:
            bad += 1
            print(f"MISSED {name}: expected {expect!r}, rc={rc}\n  " + "\n  ".join(out.splitlines()[:3]))

    law_src = io.open(LAW, encoding="utf-8").read()
    for name, mutate_law, expect in LAW_CASES:
        mutated = mutate_law(law_src)
        assert mutated != law_src, f"{name}: the law mutation changed nothing"
        io.open(LAW, "w", encoding="utf-8").write(mutated)
        try:
            rc, out = run(os.path.join(HERE, "prompts.md"), CHECK)
        finally:
            io.open(LAW, "w", encoding="utf-8").write(law_src)
        if rc != 0 and expect in out:
            print(f"caught {name}")
        else:
            bad += 1
            print(f"MISSED {name}: expected {expect!r}, rc={rc}\n  " + "\n  ".join(out.splitlines()[:3]))
    assert io.open(LAW, encoding="utf-8").read() == law_src, "the law file was not put back"

    for f in (TMP_MD, TMP_PY):
        if os.path.exists(f):
            os.remove(f)
    print(f"{len(CASES) + len(LAW_CASES)} mutations, {bad} problem(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

"""Feed hero-03/check.py known-bad input (run: python3 <this file>; exits 0 when every case fires).
A prompt mutation must change the targeted prompt BLOCK and nothing else; a heading mutation must
change that heading and no block. The checker must then fail with the expected message."""
import os, re, subprocess, sys, tempfile

SET = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SET, "..", "..", "..", ".."))
CHECK = os.path.join(SET, "check.py")
clean = open(os.path.join(SET, "prompts.md"), encoding="utf-8").read()
PAT = re.compile(r"^## (\d+) — ([^\n]*)\n.*?```\n(.*?)\n```", re.S | re.M)
PROMPTS = range(1, 7)


def find(text, n):
    for m in PAT.finditer(text):
        if int(m.group(1)) == n:
            return m
    raise KeyError(n)


def mutate(n, fn, group=3):
    m = find(clean, n)
    old = m.group(group)
    new = fn(old)
    assert new != old, f"mutation on prompt {n} changed nothing"
    out = clean[:m.start(group)] + new + clean[m.end(group):]
    assert find(out, n).group(group) == new
    for k in PROMPTS:
        if (group == 3 and k != n) or group == 2:
            assert find(out, k).group(3) == find(clean, k).group(3), f"prompt {k} moved too"
    return out


def run(text):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(text)
        path = f.name
    r = subprocess.run([sys.executable, CHECK, path], cwd=REPO, capture_output=True, text=True)
    os.unlink(path)
    return r.returncode, r.stdout


def rep(a, b, count=1):
    def f(s):
        assert a in s, f"anchor not in block: {a[:40]!r}"
        return s.replace(a, b, count)
    return f


add = lambda line: (lambda s: s + "\n" + line)
H2 = ("Seen from a few steps back, the group fills about half the picture's height, and no face, hand or "
      "part of the product enters its top or bottom fifth.")
H3 = "The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters."
H5 = "Any person turns slightly toward the left side of the picture."
VARIANT = "Where several reference photos are attached, this image uses the large bag and only that one."
GRADE = "Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out."

CASES = [
    ("K1 a lock field reworded", 4, rep("with natural shadows and real contrast", "with soft shadows and real contrast"), "a lock field in other words"),
    ("K2 hero sentence 1 reworded", 6, rep("just past the centre", "right of the centre"), "hero sentence 1: found 0 times"),
    ("K3 hero sentence 2 dropped", 5, rep(H2, ""), "hero sentence 2: found 0 times"),
    ("K4 hero sentence 3 twice", 2, add(H3), "hero sentence 3: found 2 times"),
    ("K5 sentence 5 missing with a person", 1, rep(H5, ""), "hero sentence 5 found 0 times"),
    ("K6 the person taken out", 5, rep("A North American man in his thirties, in a terracotta shirt, folds a crusty loaf into the bread bag on the table, a bowl of fruit beside him, with a natural, relaxed expression.", "A crusty loaf lies beside the bread bag on the table."), "a person with no casting named"),
    ("K7 the product block reworded", 3, rep("Do not redesign, restyle, simplify or add features.", "Keep it as it is."), "product block: found 0 times"),
    ("K8 the variant sentence dropped", 5, rep(VARIANT, ""), "variant sentence present=False"),
    ("K9 a variant sentence on the extender", 4, add(VARIANT), "variant sentence present=True"),
    ("K10 the extender not plugged in", 4, rep("plugged into a wall socket just behind the sofa", "standing on the sofa table"), "not plugged into a wall socket"),
    ("K11 a part of the extender named", 4, rep("The Wi-Fi extender is plugged", "The Wi-Fi extender, antennas up, is plugged"), "G2: a part, material or colour word 'antennas'"),
    ("K12 a material of the bag named", 5, rep("into the bread bag", "into the beeswax bread bag"), "G2: a part, material or colour word 'beeswax'"),
    ("K13 a material of the cushion named", 1, rep("holds the cushion in both hands", "holds the memory foam cushion in both hands"), "G2: a part, material or colour word 'memory foam'"),
    ("K14 a leg treatment", 6, rep("along her upper arm", "along her lower leg"), "a low treatment area 'leg'"),
    ("K15 the brand in the prompt", 5, rep("into the bread bag", "into the Hivefold bread bag"), "a brand name reaches the prompt"),
    ("K16 quoted words", 5, add('A card on the table reads "Day three".'), "quoted words in a wordless hero"),
    ("K17 the no-words sentence dropped", 3, rep("Nothing in the picture carries a word, a number, a label or a badge.", ""), "no words: found 0 times"),
    ("K18 the corner dropped", 2, rep("Nothing is placed in the bottom-right corner of the frame.", ""), "corner: found 0 times"),
    ("K19 no casting on a person", 1, rep("A European woman", "A woman"), "a person with no casting named"),
    ("K20 casting in the negative", 4, add("She is not Asian."), "casting named in the negative"),
    ("K21 a ratio", 1, add("Compose for a 3:1 banner."), "names the frame's shape or ratio"),
    ("K22 a shape word", 5, rep("Photograph of a sunny kitchen", "Square photograph of a sunny kitchen"), "names the frame's shape or ratio"),
    ("K23 a region label", 3, add("Left: a sunny window."), "a region label"),
    ("K24 an Avoid line", 2, add("Avoid: text"), "an Avoid: line"),
    ("K25 over the gate", 3, add("Keep the room warm, tidy and full of afternoon light. " * 3), "LENGTH"),
    ("K26 the slot named", 1, rep("Photograph of a sunny home office", "Hero photograph of a sunny home office"), "a repo, slot or device name reaches the prompt"),
    ("K27 a device named", 6, add("The picture must work on desktop and mobile."), "a repo, slot or device name reaches the prompt"),
    ("K28 the heading names another field", 4, rep("`hero.background`", "`hero.image`"), "heading does not name the type, the slot, the field and the template", 2),
    ("K29 a second control", 6, rep("· ATTACH 1", "· ATTACH 1 · **CONTROL**"), "CONTROL in heading=True", 2),
    ("K30 the box let back in", 5, rep(" No box is in the picture.", ""), "printed box is not kept out of frame"),
    ("K31 a screen facing the camera", 4, rep("with its screen turned away", "with its screen facing the camera"), "a screen that is not turned away"),
    ("K32 a minor added", 3, rep("sits back into an armchair", "sits back into an armchair beside her child"), "G13: a minor 'child'"),
    ("K33 an inset added", 5, add("A small inset shows the loaf on day three."), "an inset is named beyond"),
    ("K34 the first line without no words", 2, rep("no insets, no words.", "no insets."), "first line is not the photograph line"),
    ("K35 a typography sentence", 3, add("A bold sans-serif title sits in the left half."), "a typography or title sentence"),
    ("K36 the multi-instance sentence", 2, add("Wherever the product appears more than once in this image it is identical in every instance."), "the multi-instance sentence"),
    ("K37 the template named", 5, add("Match the eco template."), "a repo, slot or device name reaches the prompt"),
    ("K38 hero-01's grade line back", 2, rep(GRADE, "Grade: bright, neutral, true to life."), "a lock field in other words"),
    ("K39 a beige top", 3, rep("in a coral knit top", "in a beige knit top"), "a drained colour word 'beige'"),
    ("K40 pale walls in the scene", 1, add("The walls are pale and the room is quiet."), "a drained colour word 'pale'"),
    ("K41 a posed smile", 6, rep("with a natural, relaxed expression", "with a big smile"), "a posed smile 'smile'"),
    ("K42 the expression dropped", 1, rep(", with a natural, relaxed expression", ""), "a person without the natural, relaxed expression"),
    ("K43 no colour to wear", 2, rep("in a sky-blue shirt, ", ""), "a person with no clear, friendly colour to wear"),
    ("K44 hero-01's second sentence back", 4, rep("Seen from a few steps back, the group fills", "Together they fill"), "hero sentence 2: found 0 times"),
    ("K45 hero-01's third sentence back", 1, rep("softly blurred and full of daylight", "in soft focus, bright and calm"), "hero sentence 3: found 0 times"),
    ("K46 soft window light in the scene", 5, add("Soft window light falls on the table."), "a drained colour word 'soft window light'"),
    ("K47 the seated cushion not seen from the side", 2, rep("seen from the side so the whole cushion reads under him, ", ""), "not seen from the side"),
    ("K48 the host chair sentence dropped", 3, rep(" The chair is in a tone and material clearly different from the cushion.", ""), "host chair is not asked for as a relation"),
    ("K49 the host sentence where nothing is sat on", 1, add("The chair is in a tone and material clearly different from the cushion."), "seated-host sentence in a prompt with no seated product"),
]

ok = True
code, out = run(clean)
print(f"CONTROL clean set: exit {code}", "OK" if code == 0 else "UNEXPECTED")
ok &= code == 0
for case in CASES:
    name, n, fn, expect = case[:4]
    group = case[4] if len(case) > 4 else 3
    text = mutate(n, fn, group)
    code, out = run(text)
    hit = code == 1 and expect in out
    ok &= hit
    print(f"{name:<44} exit {code}  {'CAUGHT' if hit else 'MISSED'}")
    if not hit:
        print(out)
print("ALL AS EXPECTED" if ok else "SOMETHING DID NOT FIRE")
sys.exit(0 if ok else 1)

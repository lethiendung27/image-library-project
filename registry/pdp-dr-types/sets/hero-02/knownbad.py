"""Feed hero-02/check.py known-bad input (run: python3 <this file>; exits 0 when every case fires).
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
    ("K1 a lock field reworded", 1, rep("with natural shadows and real contrast", "with soft shadows and real contrast"), "a lock field in other words"),
    ("K2 hero sentence 1 reworded", 2, rep("just past the centre", "right of the centre"), "hero sentence 1: found 0 times"),
    ("K3 hero sentence 2 dropped", 3, rep(H2, ""), "hero sentence 2: found 0 times"),
    ("K4 hero sentence 3 twice", 5, add(H3), "hero sentence 3: found 2 times"),
    ("K5 sentence 5 missing with a person", 6, rep(H5, ""), "hero sentence 5 found 0 times"),
    ("K6 the person taken out", 4, rep("A European man in his forties, in a sky-blue shirt, slides a fresh loaf into the bread bag on the counter in front of him, with a natural, relaxed expression.", "A fresh loaf lies beside the bread bag on the counter."), "a person with no casting named"),
    ("K7 the product block reworded", 1, rep("Do not redesign, restyle, simplify or add features.", "Keep it as it is."), "product block: found 0 times"),
    ("K8 the variant sentence dropped", 3, rep(VARIANT, ""), "variant sentence present=False"),
    ("K9 a variant sentence on the extender", 2, add(VARIANT), "variant sentence present=True"),
    ("K10 the extender not plugged in", 1, rep("plugged into a wall socket just above the desk", "standing on the desk"), "not plugged into a wall socket"),
    ("K11 a part of the extender named", 2, rep("The Wi-Fi extender is plugged", "The Wi-Fi extender, antennas up, is plugged"), "G2: a part, material or colour word 'antennas'"),
    ("K12 a material of the bag named", 4, rep("into the bread bag", "into the beeswax bread bag"), "G2: a part, material or colour word 'beeswax'"),
    ("K13 a flash drawn on the device", 5, rep("watching it with a natural", "watching its flash with a natural"), "G2: a part, material or colour word 'flash'"),
    ("K14 a leg treatment", 6, rep("along her upper arm", "along her lower leg"), "a low treatment area 'leg'"),
    ("K15 the brand in the prompt", 3, rep("the open bread bag", "the open Hivefold bread bag"), "a brand name reaches the prompt"),
    ("K16 quoted words", 4, add('A card on the counter reads "Day three".'), "quoted words in a wordless hero"),
    ("K17 the no-words sentence dropped", 5, rep("Nothing in the picture carries a word, a number, a label or a badge.", ""), "no words: found 0 times"),
    ("K18 the corner dropped", 6, rep("Nothing is placed in the bottom-right corner of the frame.", ""), "corner: found 0 times"),
    ("K19 no casting on a person", 1, rep("A European man", "A man"), "a person with no casting named"),
    ("K20 casting in the negative", 2, add("She is not Asian."), "casting named in the negative"),
    ("K21 a ratio", 3, add("Compose for a 3:1 banner."), "names the frame's shape or ratio"),
    ("K22 a shape word", 4, rep("Photograph of a sunny kitchen", "Square photograph of a sunny kitchen"), "names the frame's shape or ratio"),
    ("K23 a region label", 5, add("Left: a sunny window."), "a region label"),
    ("K24 an Avoid line", 6, add("Avoid: text"), "an Avoid: line"),
    ("K25 over the gate", 3, add("Keep the kitchen warm, tidy and full of morning light. " * 3), "LENGTH"),
    ("K26 the slot named", 1, rep("Photograph of a sunny home office", "Hero photograph of a sunny home office"), "a repo, slot or device name reaches the prompt"),
    ("K27 a device named", 2, add("The picture must work on desktop and mobile."), "a repo, slot or device name reaches the prompt"),
    ("K28 the heading names another field", 1, rep("`hero.background`", "`hero.image`"), "heading does not name the type, the slot, the field and the template", 2),
    ("K29 a second control", 5, rep("· ATTACH 1", "· ATTACH 1 · **CONTROL**"), "CONTROL in heading=True", 2),
    ("K30 the box let back in", 3, rep(" No box is in the picture.", ""), "printed box is not kept out of frame"),
    ("K31 a screen facing the camera", 1, rep("with its screen turned away", "with its screen facing the camera"), "a screen that is not turned away"),
    ("K32 a minor added", 2, rep("sits on a sofa with a tablet", "sits on a sofa beside her child with a tablet"), "G13: a minor 'child'"),
    ("K33 an inset added", 4, add("A small inset shows the loaf on day three."), "an inset is named beyond"),
    ("K34 the first line without no words", 5, rep("no insets, no words.", "no insets."), "first line is not the photograph line"),
    ("K35 a typography sentence", 6, add("A bold sans-serif title sits in the left half."), "a typography or title sentence"),
    ("K36 the multi-instance sentence", 1, add("Wherever the product appears more than once in this image it is identical in every instance."), "the multi-instance sentence"),
    ("K37 the template named", 3, add("Match the eco template."), "a repo, slot or device name reaches the prompt"),
    ("K38 hero-01's grade line back", 1, rep(GRADE, "Grade: bright, neutral, true to life."), "a lock field in other words"),
    ("K39 a beige top", 2, rep("in a coral knit top", "in a beige knit top"), "a drained colour word 'beige'"),
    ("K40 pale walls in the scene", 3, add("The walls are pale and the room is quiet."), "a drained colour word 'pale'"),
    ("K41 a posed smile", 5, rep("with a natural, relaxed expression", "with a big smile"), "a posed smile 'smile'"),
    ("K42 the expression dropped", 6, rep("watching it with a natural, relaxed expression", "watching it closely"), "a person without the natural, relaxed expression"),
    ("K43 no colour to wear", 4, rep("in a sky-blue shirt, ", ""), "a person with no clear, friendly colour to wear"),
    ("K44 hero-01's second sentence back", 2, rep("Seen from a few steps back, the group fills", "Together they fill"), "hero sentence 2: found 0 times"),
    ("K45 hero-01's third sentence back", 6, rep("softly blurred and full of daylight", "in soft focus, bright and calm"), "hero sentence 3: found 0 times"),
    ("K46 soft window light in the scene", 4, add("Soft window light falls on the counter."), "a drained colour word 'soft window light'"),
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

"""Feed hero-01/check.py known-bad input (run: python3 <this file>; exits 0 when every case fires).
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
H1 = ("The product and anyone using it sit together in the right half of the picture, just past the "
      "centre and well clear of the right edge.")
H2 = ("Together they fill about half the picture's height, and no face, hand or part of the product "
      "enters its top or bottom fifth.")
H3 = "The left half continues the same place in soft focus, bright and calm, with nothing in it that matters."
H5 = "Any person turns slightly toward the left side of the picture."
VARIANT = "Where several reference photos are attached, this image uses the large bag and only that one."

CASES = [
    ("K1 a lock field reworded", 1, rep("gentle shadows, no rim light", "soft shadows, no rim light"), "a lock field in other words"),
    ("K2 hero sentence 1 reworded", 2, rep("just past the centre", "right of the centre"), "hero sentence 1: found 0 times"),
    ("K3 hero sentence 2 dropped", 3, rep(H2, ""), "hero sentence 2: found 0 times"),
    ("K4 hero sentence 3 twice", 5, add(H3), "hero sentence 3: found 2 times"),
    ("K5 sentence 5 missing with a person", 6, rep(H5, ""), "hero sentence 5 found 0 times"),
    ("K6 sentence 5 with no person", 4, add(H5), "hero sentence 5 in a prompt with no person"),
    ("K7 the product block reworded", 1, rep("Do not redesign, restyle, simplify or add features.", "Keep it as it is."), "product block: found 0 times"),
    ("K8 the variant sentence dropped", 3, rep(VARIANT, ""), "variant sentence present=False"),
    ("K9 a variant sentence on the extender", 2, add(VARIANT), "variant sentence present=True"),
    ("K10 the extender not plugged in", 1, rep("plugged into a wall socket just above the desk", "standing on the desk"), "not plugged into a wall socket"),
    ("K11 a part of the extender named", 2, rep("The Wi-Fi extender is plugged", "The Wi-Fi extender, antennas up, is plugged"), "G2: a part, material or colour word 'antennas'"),
    ("K12 a material of the bag named", 4, rep("The bread bag lies", "The beeswax bread bag lies"), "G2: a part, material or colour word 'beeswax'"),
    ("K13 a flash drawn on the device", 5, rep("watching it with a calm smile", "watching its flash with a calm smile"), "G2: a part, material or colour word 'flash'"),
    ("K14 a leg treatment", 6, rep("along her upper arm", "along her lower leg"), "a low treatment area 'leg'"),
    ("K15 the brand in the prompt", 3, rep("the bread bag, which", "the Hivefold bread bag, which"), "a brand name reaches the prompt"),
    ("K16 quoted words", 4, add('A card on the board reads "Day three".'), "quoted words in a wordless hero"),
    ("K17 the no-words sentence dropped", 5, rep("Nothing in the picture carries a word, a number, a label or a badge.", ""), "no words: found 0 times"),
    ("K18 the corner dropped", 6, rep("Nothing is placed in the bottom-right corner of the frame.", ""), "corner: found 0 times"),
    ("K19 no casting on a person", 1, rep("A European man", "A man"), "a person with no casting named"),
    ("K20 casting in the negative", 2, add("She is not Asian."), "casting named in the negative"),
    ("K21 a ratio", 3, add("Compose for a 3:1 banner."), "names the frame's shape or ratio"),
    ("K22 a shape word", 4, rep("Photograph of a kitchen counter", "Square photograph of a kitchen counter"), "names the frame's shape or ratio"),
    ("K23 a region label", 5, add("Left: a bright window."), "a region label"),
    ("K24 an Avoid line", 6, add("Avoid: text"), "an Avoid: line"),
    ("K25 over the gate", 3, add("Keep the kitchen warm, tidy and full of morning light. " * 3), "LENGTH"),
    ("K26 the slot named", 1, rep("Photograph of a quiet study", "Hero photograph of a quiet study"), "a repo, slot or device name reaches the prompt"),
    ("K27 a device named", 2, add("The picture must work on desktop and mobile."), "a repo, slot or device name reaches the prompt"),
    ("K28 the heading names another field", 1, rep("`hero.background`", "`hero.image`"), "heading does not name the type, the slot, the field and the template", 2),
    ("K29 a second control", 5, rep("· ATTACH 1", "· ATTACH 1 · **CONTROL**"), "CONTROL in heading=True", 2),
    ("K30 the box let back in", 3, rep(" No box is in the picture.", ""), "printed box is not kept out of frame"),
    ("K31 a screen facing the camera", 1, rep("with its screen turned away", "with its screen facing the camera"), "a screen that is not turned away"),
    ("K32 a minor added", 2, rep("sits sideways on a sofa", "sits sideways on a sofa beside her child"), "G13: a minor 'child'"),
    ("K33 an inset added", 4, add("A small inset shows the loaf on day three."), "an inset is named beyond"),
    ("K34 the first line without no words", 5, rep("no insets, no words.", "no insets."), "first line is not the photograph line"),
    ("K35 a typography sentence", 6, add("A bold sans-serif title sits in the left half."), "a typography or title sentence"),
    ("K36 the multi-instance sentence", 1, add("Wherever the product appears more than once in this image it is identical in every instance."), "the multi-instance sentence"),
    ("K37 no person, and not said", 4, rep("No person and no box is in the picture.", "No box is in the picture."), "does not say so"),
    ("K38 the template named", 3, add("Match the eco template."), "a repo, slot or device name reaches the prompt"),
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

"""Feed hero-04/check.py known-bad input (run: python3 <this file>; exits 0 when every case fires).
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
H2 = ("The group fills about half the picture's height, with a clear band of room above every head "
      "and below every hand, each about a fifth.")
H3 = "The left half continues the same place, softly blurred and full of daylight, with nothing in it that matters."
H5 = "It is a real photograph: skin keeps its texture, with no glow and no haze."
H6 = "Any person turns slightly toward the left side of the picture."
GRADE = "Grade: true colour, neutral whites, no warm filter and no glow."
SETTING = "Setting: a bright, lived-in home with green, blue and red among its colours."
SCREENS = "Any screen shows only a picture, with no interface, text or numbers."
VARIANT = "Where several reference photos are attached, this image uses the large bag and only that one."
HOST = "The chair is in a tone and material clearly different from the cushion."

CASES = [
    # the lock and the fixed sentences
    ("K1 a lock field reworded", 1, rep("with natural shadows and real contrast", "with soft shadows and real contrast"), "a lock field in other words"),
    ("K2 hero sentence 1 reworded", 2, rep("just past the centre", "right of the centre"), "hero sentence 1: found 0 times"),
    ("K3 the band sentence dropped", 3, rep(H2, ""), "hero sentence 2: found 0 times"),
    ("K4 hero-03's camera sentence back", 4, rep(H2, "Seen from a few steps back, the group fills about half the picture's height."), "hero sentence 2: found 0 times"),
    ("K5 the left-half sentence twice", 5, add(H3), "hero sentence 3: found 2 times"),
    ("K6 the real-photograph sentence dropped", 6, rep(H5, ""), "hero sentence 5: found 0 times"),
    ("K7 sentence 6 missing with a person", 1, rep(H6, ""), "the person sentence found 0 times"),
    ("K8 hero-03's grade line back", 2, rep(GRADE, "Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out."), "a lock field in other words"),
    ("K9 hero-03's setting line back", 3, rep(SETTING, "Setting: a sunny, lived-in home with a few real colours: plants, fruit, bright textiles."), "a lock field in other words"),
    # ADR-107: the words that turned the frame yellow
    ("K10 warm daylight in the scene", 4, add("Warm daylight fills the room."), "a yellow-pulling word 'warm daylight'"),
    ("K11 a sunny first line", 5, rep("Photograph of a bright room", "Photograph of a sunny room"), "a yellow-pulling word 'sunny'"),
    ("K12 a fruit bowl in the scene", 6, add("A bowl of fruit sits on the table."), "a yellow-pulling word 'fruit'"),
    ("K13 a golden glow asked for", 1, add("A golden glow falls across the desk."), "a yellow-pulling word 'golden'"),
    # G6, the screen sentence
    ("K14 the screen sentence dropped where a screen can appear", 3, rep(SCREENS, ""), "G6 screen sentence present=False"),
    ("K15 the screen sentence where no screen can appear", 5, add(SCREENS), "G6 screen sentence present=True"),
    ("K16 a screen facing the camera", 4, add("A tablet leans on the table with its screen facing the camera."), "a screen that is not turned away"),
    # the seated product
    ("K17 the seated cushion not seen from the side", 1, rep("seen from the side so it reads whole, ", ""), "not seen from the side"),
    ("K18 the host chair sentence dropped", 6, rep(" " + HOST, ""), "host chair is not asked for as a relation"),
    ("K19 the host sentence where nothing is sat on", 2, add(HOST), "seated-host sentence in a prompt with no seated product"),
    # the product block and its conditional sentences
    ("K20 the product block reworded", 5, rep("Do not redesign, restyle, simplify or add features.", "Keep it as it is."), "product block: found 0 times"),
    ("K21 the variant sentence dropped", 4, rep(VARIANT, ""), "variant sentence present=False"),
    ("K22 a variant sentence on the extender", 3, add(VARIANT), "variant sentence present=True"),
    ("K23 the box let back in", 4, rep(" No box is in the picture.", ""), "printed box is not kept out of frame"),
    # G2 and G7-X
    ("K24 the extender not plugged in", 3, rep("plugged into a wall socket by the sofa", "standing on the sofa table"), "not plugged into a wall socket"),
    ("K25 a part of the extender named", 3, rep("The Wi-Fi extender is plugged", "The Wi-Fi extender, antennas up, is plugged"), "G2: a part, material or colour word 'antennas'"),
    ("K26 a material of the cushion named", 2, rep("holds the cushion in both hands", "holds the memory foam cushion in both hands"), "G2: a part, material or colour word 'memory foam'"),
    ("K27 a material of the bag named", 4, rep("into the bread bag", "into the beeswax bread bag"), "G2: a part, material or colour word 'beeswax'"),
    ("K28 a leg treatment", 5, rep("along her upper arm", "along her lower leg"), "a low treatment area 'leg'"),
    ("K29 the brand in the prompt", 4, rep("into the bread bag", "into the Hivefold bread bag"), "a brand name reaches the prompt"),
    # people
    ("K30 no casting on a person", 2, rep("A European woman", "A woman"), "a person with no casting named"),
    ("K31 casting in the negative", 1, add("He is not Asian."), "casting named in the negative"),
    ("K32 a posed smile", 6, rep("with a natural, relaxed expression", "with a big smile"), "a posed smile 'smile'"),
    ("K33 the expression dropped", 5, rep(", with a natural, relaxed expression", ""), "a person without the natural, relaxed expression"),
    ("K34 no colour to wear", 1, rep("in a sky-blue shirt, ", ""), "a person with no clear, friendly colour to wear"),
    ("K35 a minor added", 6, rep("sits back into an armchair", "sits back into an armchair beside her child"), "G13: a minor 'child'"),
    # the frame and the words
    ("K36 quoted words", 2, add('A card on the desk reads "Day one".'), "quoted words in a wordless hero"),
    ("K37 the no-words sentence dropped", 3, rep("Nothing in the picture carries a word, a number, a label or a badge.", ""), "no words: found 0 times"),
    ("K38 the corner dropped", 4, rep("Nothing is placed in the bottom-right corner of the frame.", ""), "corner: found 0 times"),
    ("K39 a ratio", 5, add("Compose for a 3:1 banner."), "names the frame's shape or ratio"),
    ("K40 a shape word", 6, rep("Photograph of a living room", "Square photograph of a living room"), "names the frame's shape or ratio"),
    ("K41 a region label", 1, add("Left: a bright window."), "a region label"),
    ("K42 an Avoid line", 2, add("Avoid: text"), "an Avoid: line"),
    ("K43 over the gate", 3, add("Keep the room tidy and full of daylight. " * 4), "LENGTH"),
    ("K44 the slot named", 4, rep("Photograph of a kitchen table", "Hero photograph of a kitchen table"), "a repo, slot or device name reaches the prompt"),
    ("K45 a device named", 5, add("The picture must work on desktop and mobile."), "a repo, slot or device name reaches the prompt"),
    ("K46 the template named", 6, add("Match the eco template."), "a repo, slot or device name reaches the prompt"),
    ("K47 an inset added", 1, add("A small inset shows the cushion alone."), "an inset is named beyond"),
    ("K48 the first line without no words", 2, rep("no insets, no words.", "no insets."), "first line is not the photograph line"),
    ("K49 a typography sentence", 3, add("A bold sans-serif title sits in the left half."), "a typography or title sentence"),
    ("K50 the multi-instance sentence", 4, add("Wherever the product appears more than once in this image it is identical in every instance."), "the multi-instance sentence"),
    # headings
    ("K51 the heading names another field", 3, rep("`hero.background`", "`hero.image`"), "heading does not name the type, the slot, the field and the template", 2),
    ("K52 a second control", 5, rep("· ATTACH 1", "· ATTACH 1 · **CONTROL**"), "CONTROL in heading=True", 2),
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
    print(f"{name:<58} exit {code}  {'CAUGHT' if hit else 'MISSED'}")
    if not hit:
        print(out)
print("ALL AS EXPECTED" if ok else "SOMETHING DID NOT FIRE")
sys.exit(0 if ok else 1)

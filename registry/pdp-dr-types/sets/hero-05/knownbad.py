"""Feed hero-05/check.py known-bad input (run: python3 <this file>; exits 0 when every case fires).
Both forms are exercised: prompts 1-3 are labelled, 4-6 are the owner's paragraph."""
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
H1 = "The product and anyone using it sit together in the right half, just past the centre and well clear of the right edge."
H2 = "The group fills about half the picture's height, with a clear band of room above every head and below every hand, each about a fifth."
H5 = "It is a real photograph: skin keeps its texture, with no glow and no haze."
H6 = "Any person turns slightly toward the left side of the picture."
SETTING = "Setting: a lived-in home where the colours are the room's own."
GRADE = "Grade: true colour, neutral whites, no warm filter and no glow."
SCREENS = "Any screen shows only a picture, with no interface, text or numbers."
VARIANT = "Where several reference photos are attached, this image uses the large bag and only that one."
CLOSING = ("Do not change anything related to the original product, including screen, buttons, display, "
           "interface, ports, technical indicators, color, shape, proportions, dimensions, or functionality.")
G1 = "Use the attached product photo as the exact reference."
BLOCK_HEAD = "Use the attached product photo as the exact reference. Preserve its shape"

CASES = [
    # the labelled form
    ("K1 a lock field reworded", 1, rep("with natural shadows and real contrast", "with soft shadows and real contrast"), "a lock field in other words"),
    ("K2 hero sentence 1 reworded", 2, rep("just past the centre", "right of the centre"), "hero sentence 1: found 0 times"),
    ("K3 the band sentence dropped", 3, rep(H2, ""), "hero sentence 2: found 0 times"),
    ("K4 the real-photograph sentence dropped", 1, rep(H5, ""), "hero sentence 5: found 0 times"),
    ("K5 the person sentence dropped", 2, rep(H6, ""), "the person sentence: found 0 times"),
    ("K6 the product block reworded", 3, rep("Do not redesign, restyle, simplify or add features.", "Keep it as it is."), "product block: found 0 times"),
    ("K7 the screen sentence dropped where a screen can appear", 2, rep(SCREENS, ""), "G6 screen sentence present=False"),
    ("K8 the screen sentence where no screen can appear", 3, add(SCREENS), "G6 screen sentence present=True"),
    ("K9 the first line without no words", 1, rep("no insets, no words.", "no insets."), "first line is not the photograph line"),
    ("K10 an inset added", 2, add("A small inset shows the extender alone."), "an inset is named beyond"),
    ("K11 the setting line reworded", 3, rep(SETTING, "Setting: a sunny home with bright textiles."), "a lock field in other words"),
    # the paragraph form
    ("K12 a label in the paragraph", 4, add("Light: bright daylight from the left."), "carries the label 'Light:'"),
    ("K13 the product block in the paragraph", 5, add(BLOCK_HEAD + ", proportions, construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, simplify or add features. The product appears in one of its real colourways only, never restyled to match the scene or the set palette; no added piping, trim, logos, patterns or printed text. Every part keeps its photographed colour and finish; no part is tinted toward the set's accent."), "carries the product block"),
    ("K14 the closing sentence dropped", 6, rep("\n" + CLOSING, ""), "does not end with the instruction's closing sentence"),
    ("K15 the closing sentence not last", 4, rep(CLOSING, CLOSING + " The room is quiet."), "does not end with the instruction's closing sentence"),
    ("K16 G1 dropped from the paragraph", 5, rep(G1 + "\n", ""), "does not carry G1's one sentence exactly once"),
    ("K17 the placement clause dropped", 6, rep("in the right half, just past the centre and well clear of the right edge, ", ""), "does not carry 'in the right half"),
    ("K18 the band clause dropped", 4, rep("with a clear band of room above his head and below his hands, each about a fifth; ", ""), "does not carry 'clear band of room above'"),
    ("K19 the real-photograph clause dropped", 5, rep("It is a real photograph: skin keeps its texture, with no glow and no haze, ", ""), "does not carry 'It is a real photograph"),
    ("K20 the room's-own-colours clause dropped", 6, rep("and the colours are the room's own, ", ""), 'does not carry "the colours are the room\'s own"'),
    ("K21 an inset in the paragraph", 4, rep("It is a real photograph", "A small inset sits in a corner. It is a real photograph"), "an inset is named"),
    ("K22 the screen left open in the paragraph", 5, rep("a laptop whose screen shows only a picture", "a laptop"), "does not keep it to a picture"),
    # both forms
    ("K23 a staged-colour phrase", 1, add("The room takes colours from more than one family."), "a staged-colour phrase"),
    ("K24 a yellow-pulling word", 4, rep("in a lived-in home office", "in a sunny home office"), "a yellow-pulling word 'sunny'"),
    ("K25 a drained colour word", 2, add("The walls are pale."), "a drained colour word 'pale'"),
    ("K26 a part of the extender named", 5, rep("the Wi-Fi extender is plugged", "the Wi-Fi extender, antennas up, is plugged"), "G2: a part, material or colour word 'antennas'"),
    ("K27 a material of the cushion named", 1, rep("sits on the cushion", "sits on the memory foam cushion"), "G2: a part, material or colour word 'memory foam'"),
    ("K28 a material of the bag named", 6, rep("into the bread bag", "into the beeswax bread bag"), "G2: a part, material or colour word 'beeswax'"),
    ("K29 the brand in the prompt", 3, rep("into the bread bag", "into the Hivefold bread bag"), "a brand name reaches the prompt"),
    ("K30 the extender not plugged in", 2, rep("plugged into a wall socket by the sofa", "standing on the side table"), "not plugged into a wall socket"),
    ("K31 the box let back in", 3, rep(" No box is in the picture.", ""), "printed box is not kept out of frame"),
    ("K32 the variant sentence dropped", 6, rep(VARIANT + "\n", ""), "variant sentence present=False"),
    ("K33 a variant sentence on the extender", 2, add(VARIANT), "variant sentence present=True"),
    ("K34 the seated cushion not seen from the side", 1, rep("seen from the side so it reads whole, ", ""), "not seen from the side"),
    ("K35 the host chair dropped", 4, rep(" against a chair of a clearly different tone", ""), "host chair is not asked for as a relation"),
    ("K36 no casting", 5, rep("A European couple", "A couple"), "a person with no casting named"),
    ("K37 casting in the negative", 3, add("He is not Asian."), "casting named in the negative"),
    ("K38 the expression dropped", 6, rep(", with a natural, relaxed expression", ""), "a person without the natural, relaxed expression"),
    ("K39 no colour to wear", 1, rep("in a sky-blue shirt, ", ""), "a person with no clear colour to wear"),
    ("K40 a minor added", 2, rep("sit on a sofa", "sit on a sofa beside their child") if False else rep("watch a film on a laptop", "watch a film on a laptop beside their child"), "G13: a minor 'child'"),
    ("K41 quoted words", 3, add('A note on the table reads "Day three".'), "quoted words in a wordless hero"),
    ("K42 a ratio", 4, rep("It is a real photograph", "Compose it 3:1. It is a real photograph"), "names the frame's shape or ratio"),
    ("K43 a region label", 1, add("Left: a bright window."), "a region label"),
    ("K44 an Avoid line", 2, add("Avoid: text"), "an Avoid: line"),
    ("K45 the multi-instance sentence", 5, rep("It is a real photograph", "Wherever the product appears more than once in this image it is identical in every instance. It is a real photograph"), "the multi-instance sentence"),
    ("K46 a repo word", 6, rep("of a lived-in kitchen", "of a lived-in kitchen for the hero"), "a repo, slot or device name reaches the prompt"),
    ("K47 over the gate", 3, add("Keep the kitchen tidy and full of daylight. " * 4), "LENGTH"),
    # headings
    ("K48 the heading hides the form", 4, rep(" · the paragraph form", ""), "does not say which form this prompt is", 2),
    ("K49 the heading names another field", 2, rep("`hero.background`", "`hero.image`"), "heading does not name the type, the slot, the field and the template", 2),
    ("K50 a second control", 5, rep("· ATTACH 1", "· ATTACH 1 · **CONTROL**"), "CONTROL in heading=True", 2),
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

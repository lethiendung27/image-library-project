"""Feed hero-06/check.py known-bad input (run: python3 <this file>; exits 0 when every case fires).
One prompt, so every case mutates it; the set's own rule is the conditional sentence for a product
that appears in frame more than once."""
import os, re, subprocess, sys, tempfile

SET = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SET, "..", "..", "..", ".."))
CHECK = os.path.join(SET, "check.py")
clean = open(os.path.join(SET, "prompts.md"), encoding="utf-8").read()
PAT = re.compile(r"^## (\d+) — ([^\n]*)\n.*?```\n(.*?)\n```", re.S | re.M)


def find(text, n=1):
    for m in PAT.finditer(text):
        if int(m.group(1)) == n:
            return m
    raise KeyError(n)


def mutate(fn, group=3):
    m = find(clean)
    old = m.group(group)
    new = fn(old)
    assert new != old, "mutation changed nothing"
    return clean[:m.start(group)] + new + clean[m.end(group):]


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
MULTI = "Wherever the product appears more than once in this image it is identical in every instance."
H2 = "The group fills about half the picture's height, with a clear band of room above every head and below every hand, each about a fifth."
H5 = "It is a real photograph: skin keeps its texture, with no glow and no haze."
GRADE = "Grade: true colour, neutral whites, no warm filter and no glow."

CASES = [
    ("K1 the set's conditional sentence dropped", rep(MULTI + "\n", ""), "multi-instance sentence present=False"),
    ("K2 the conditional sentence reworded", rep(MULTI, "Every piece of the product looks the same as the others."), "multi-instance sentence present=False"),
    ("K3 the sliders not under the furniture", rep("The sliders are under its near corners", "The sliders lie beside the bookcase"), "sliders are not under the furniture"),
    ("K4 the bookcase has not moved yet", rep("where a bookcase has just been moved", "with a bookcase against the wall"), "heavy thing has not already moved"),
    ("K5 a material of the set named", rep("the lifting lever in her hand", "the steel lifting lever in her hand"), "G2: a part, material or colour word 'steel'"),
    ("K6 a construction word", rep("The sliders are under", "The rollers are under"), "G2: a part, material or colour word 'roller"),
    ("K7 the band sentence dropped", rep(H2, ""), "hero sentence 2: found 0 times"),
    ("K8 the real-photograph sentence dropped", rep(H5, ""), "hero sentence 5: found 0 times"),
    ("K9 hero-03's grade line back", rep(GRADE, "Grade: editorial realism with vivid, true colour; nothing looks greyed or washed out."), "a lock field in other words"),
    ("K10 a yellow-pulling word", rep("Photograph of a living room", "Photograph of a sunny living room"), "a yellow-pulling word 'sunny'"),
    ("K11 a staged-colour phrase", add("The room takes colours from more than one family."), "a staged-colour phrase"),
    ("K12 no casting", rep("A European woman", "A woman"), "a person with no casting named"),
    ("K13 the expression dropped", rep(" and a natural, relaxed expression", ""), "a person without the natural, relaxed expression"),
    ("K14 no colour to wear", rep("in a teal jumper, ", ""), "a person with no clear colour to wear"),
    ("K15 a minor added", rep("stands by the bookcase", "stands by the bookcase beside her child"), "G13: a minor 'child'"),
    ("K16 quoted words", add('A label on the lever reads "Lift".'), "quoted words in a wordless hero"),
    ("K17 a ratio", add("Compose for a 3:1 banner."), "names the frame's shape or ratio"),
    ("K18 a region label", add("Left: a bright window."), "a region label"),
    ("K19 over the gate", add("Keep the room tidy and full of daylight. " * 4), "LENGTH"),
    ("K20 the corner sentence dropped", rep("Nothing is placed in the bottom-right corner of the frame.", ""), "corner: found 0 times"),
    ("K21 the heading names another field", rep("`hero.image`", "`hero.background`"), "heading does not name the type, the slot, the field and the template", 2),
]

ok = True
code, out = run(clean)
print(f"CONTROL clean set: exit {code}", "OK" if code == 0 else "UNEXPECTED")
ok &= code == 0
for case in CASES:
    name, fn, expect = case[:3]
    group = case[3] if len(case) > 3 else 3
    code, out = run(mutate(fn, group))
    hit = code == 1 and expect in out
    ok &= hit
    print(f"{name:<44} exit {code}  {'CAUGHT' if hit else 'MISSED'}")
    if not hit:
        print(out)
print("ALL AS EXPECTED" if ok else "SOMETHING DID NOT FIRE")
sys.exit(0 if ok else 1)

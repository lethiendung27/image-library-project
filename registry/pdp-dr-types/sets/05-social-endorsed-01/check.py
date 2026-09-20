"""Check 05-social-endorsed-01 (round 3) against the type at 0.3, ADR-114 and ADR-115: the person is the
trade the page's constraint belongs to, the work is happening, what the work needs is in frame, the work
has left a mark, the garments are NAMED rather than categorised, the kit the trade arrived with is in the
frame, and nobody looks at the lens.

Usage, from the repo root:
  python3 registry/pdp-dr-types/sets/05-social-endorsed-01/check.py [prompts.md] [--json prompts.json]
With no argument it checks this folder's prompts.md AND that prompts.json agrees with it. Exits 1 on
any failure. Word checks read the prompt with the lock's phrases, the shared sentences and the
product's name taken out first, so none of them can hide or fake a match.
"""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
args = list(sys.argv[1:])
json_path = None
if "--json" in args:
    i = args.index("--json")
    json_path = args[i + 1]
    del args[i:i + 2]
md_path = args[0] if args else os.path.join(HERE, "prompts.md")
if not args:
    json_path = os.path.join(HERE, "prompts.json")
text = io.open(md_path, encoding="utf-8").read()

GATE = 1800
PRODUCT = "Cordless Car Wash Tool"


def norm(x):
    return re.sub(r"\s+", " ", x).strip()


# the set's own words, declared here apart from build.py so a slip in one is caught by the other
TONE = ("Crisp daylight with a soft directional key, true colour with neutral whites, in a palette of "
        "clean white, deep slate grey and a fresh mid-blue, balanced contrast, readable in three seconds.")
REAL = ("It is a real photograph with true texture and a soft cast shadow, and nothing in the frame "
        "is old, worn, scratched or faded.")
DRESS = ("in grey work coveralls with the sleeves pushed up and the forearms wet, rubber boots on the "
         "wet ground, no logo, badge or name tag")
HOSE = "its intake hose runs down into a filled bucket"
ONLY_HOSE = "the only hose in the frame"
WORKING = "is mid-rinse:"
GRIP = "practised grip"
FILM = "an even film of"
NO_TEXT = "No text."
G1 = "Use the attached product photo as the exact reference."
FLAG = "endorsed-expert"

LEDGER = {
    1: dict(role="a North American mobile car detailer in her forties",
            camera="from a step back at the side",
            kit="Her work van stands close behind her with its tailgate up, a second bucket",
            mark="a bright clean band of paint runs where she has already passed",
            gaze="Her eyes are on the spray."),
    2: dict(role="a North American mobile car detailer in his fifties",
            camera="from low at the front wheel",
            kit="his work van stands behind him with its tailgate up, a second bucket",
            mark="the rim behind the spray is bright where he has already passed",
            gaze="His eyes are on the spray."),
    3: dict(role="a North American building maintenance technician in her forties",
            camera="from a step back along the balcony",
            kit="Her maintenance cart stands behind her with a second bucket",
            mark="a bright clean band runs the length she has already passed",
            gaze="Her eyes are on the spray."),
}

BANNED = {
    "a presentation to the lens": r"\b(at chest height|holds it up|held up|raised toward|presents it|shows it to the camera|square to the (lens|camera))\b",
    "a turn toward the lens": r"\b(toward the lens|at the lens|into the lens|to the camera|at the camera)\b",
    "a garment named by category": r"\b(work shirt|dress shirt|button-up|polo|chinos|jeans|t-shirt)\b",
    "a surface with nothing to remove, or caked": r"\b(spotless|immaculate|caked|mud|muddy|filthy)\b",
    "a portrait register": r"\bportrait photo\b",
    "a studio ground for an outdoor trade": r"\b(studio|seamless|backdrop|plain grey ground)\b",
    "a posed face": r"\b(smiling at the camera|posing|poses|beaming|thumbs-up|grinning)\b",
    "a drawn element called small or thin": r"\b(small|thin|tiny|minimal|concise|faint)\b",
    "the frame's shape": r"\b(\d+:\d+|aspect|ratio|portrait format)\b",
    "a share of the frame": r"\d+\s*%",
    "a distance figure": r"\b\d+(\.\d+)?\s?(m|km|cm|mm|metres|meters|feet|ft|miles)\b",
    "a label or slot": r"(^|\s)\[[A-Z ]+\]|(^|\.\s)[A-Z][A-Z ]{3,}:",
    "a repo name": r"\b\d\d-[a-z]+-[a-z]+\b|\bskeleton\b|\bLP2\b|\bgallery\b|\btile\b|\bPARTS\b",
    "a superlative or an absolute": r"\b(perfect|ultimate|ultra|premium|luxury|total|zero|all-day|best)\b",
    "a verdict word": r"\b(approved|tested|safe|certified|proven|guaranteed|clinical|clinically|expert|specialist)\b",
    "a minor": r"\b(child|children|kid|kids|baby|infant|toddler|teen|teenager|boy|girl)\b",
    "Asian-presenting casting": r"\bAsian\b",
    "a named person or title": r"\b(Dr|Mr|Mrs|Ms|Prof)\b\.?",
    "a real institution": r"\b(hospital|clinic|university|institute|academy|association|laboratory|lab)\b",
    "a certificate on the wall": r"\b(certificate|diploma|seal|award|trophy)\b",
    "a second person": r"\b(colleague|customer's assistant|assistant|two people|bystander)\b",
}
CASE_SENSITIVE = {"a label or slot", "a repo name", "a named person or title", "Asian-presenting casting"}
PRODUCT_WORDS = r"\b(blue|black|orange|yellow|plastic|brass|trigger|nozzle|battery|barrel|handle)\b"

blocks = re.findall(r"^## (\d+) — (.*?)\n.*?```\n(.*?)\n```", text, re.S | re.M)
fails = []


def fail(n, msg):
    fails.append(f"prompt {n}: {msg}")


if len(blocks) != len(LEDGER):
    fails.append(f"found {len(blocks)} prompts, the ledger declares {len(LEDGER)}")

prompts, cameras = {}, {}
for num, heading, body in blocks:
    n = int(num)
    row = LEDGER.get(n)
    if row is None:
        fail(n, "not in the ledger")
        continue
    p = norm(body)
    prompts[n] = p

    if "\n" in body.strip():
        fail(n, "is not one paragraph")
    if len(p) > GATE:
        fail(n, f"{len(p)} characters, over the {GATE} gate")
    if "`05-social-endorsed` v0.3" not in heading or "`expert.scene`" not in heading:
        fail(n, "heading does not name `05-social-endorsed` and `expert.scene`")

    for sentence, name in ((TONE, "lock tone"), (REAL, "real-never-worn"), (NO_TEXT, "no-words")):
        if p.count(sentence) != 1:
            fail(n, f"the {name} sentence appears {p.count(sentence)} times, expected 1")
    if not p.endswith(G1):
        fail(n, "does not end with the G1 sentence")
    if p.count(PRODUCT) != 1:
        fail(n, f"names the product {p.count(PRODUCT)} times, expected 1")

    # ---- ADR-114: the work, what it needs, the mark it left, the body at work
    if WORKING not in p:
        fail(n, "does not put the person mid-task (the work is not happening)")
    if GRIP not in p:
        fail(n, "does not put the product in the trade's practised grip")
    if "water" not in p:
        fail(n, "no water leaves the product: the work is not visible")
    if HOSE not in p:
        fail(n, "does not put what the work needs in frame (the bucket the intake hose draws from)")
    if row["mark"] not in p:
        fail(n, "does not show the mark the work has left")
    if FILM not in p:
        fail(n, "does not make the dirt an even film for the clean band to be cut into")
    if ONLY_HOSE not in p:
        fail(n, "does not say the tool's intake hose is the only hose in the frame")
    if row["kit"] not in p:
        fail(n, "does not bring the trade's kit into frame: " + row["kit"][:40])
    if DRESS not in p:
        fail(n, "does not dress the person in working clothes marked by the job")
    if row["gaze"] not in p:
        fail(n, "does not fix the eyes on the work, in the set's words")
    if row["role"] not in p:
        fail(n, f"does not carry its own trade: {row['role']}")
    if "North American" not in p:
        fail(n, "does not name its casting positively")

    if row["camera"] not in p:
        fail(n, f"does not carry its own camera line: {row['camera']}")
    m = re.search(r"Editorial realism photo (.*?), close enough", p)
    cameras[n] = m.group(1) if m else f"missing-{n}"

    if re.search(r"\"[^\"]+\"", p):
        fail(n, "quotes words in a wordless frame")

    bare = p
    for s in (TONE, REAL, NO_TEXT, G1, DRESS, HOSE, ONLY_HOSE, PRODUCT, row["gaze"], row["mark"],
              row["kit"], row["camera"]):
        bare = bare.replace(s, " ")
    for name, rx in BANNED.items():
        m = re.search(rx, bare, 0 if name in CASE_SENSITIVE else re.I)
        if m:
            fail(n, f"carries {name}: {m.group(0)!r}")
    m = re.search(PRODUCT_WORDS, bare, re.I)
    if m:
        fail(n, f"describes the product (G2): {m.group(0)!r}")

if len(set(cameras.values())) != len(cameras):
    fails.append("the three frames do not carry three different cameras")

if json_path:
    d = json.load(io.open(json_path, encoding="utf-8"))
    if d.get("type_version") != "0.3":
        fails.append(f"prompts.json: type_version is {d.get('type_version')!r}, expected '0.3'")
    if not (d.get("derivation") or {}).get("expert"):
        fails.append("prompts.json: the derivation does not name the expert it was built from")
    by_n = {s["n"]: s for s in d.get("slots", [])}
    for n in LEDGER:
        s = by_n.get(n)
        if not s:
            fails.append(f"prompts.json: no slot {n}")
            continue
        if norm(s.get("prompt", "")) != prompts.get(n):
            fails.append(f"prompts.json: slot {n}'s prompt differs from prompts.md")
        c = s.get("compliance") or {}
        if c.get("flag") != FLAG:
            fails.append(f"prompts.json: slot {n} carries compliance flag {c.get('flag')!r}, expected {FLAG!r}")
        if not c.get("note"):
            fails.append(f"prompts.json: slot {n}'s compliance flag has no note")
        if s.get("attachments") != 1:
            fails.append(f"prompts.json: slot {n} asks for {s.get('attachments')} attachments, expected 1")

if fails:
    print("\n".join(fails))
    print(f"FAILED: {len(fails)}")
    sys.exit(1)
sizes = ", ".join(f"{n}:{len(p)}" for n, p in sorted(prompts.items()))
print(f"05-social-endorsed-01 round 3: {len(prompts)} prompts clean (characters {sizes}; gate {GATE})"
      + ("; prompts.json agrees" if json_path else ""))

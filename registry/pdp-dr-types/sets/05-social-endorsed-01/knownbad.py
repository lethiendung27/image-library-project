"""Known-bad inputs for 05-social-endorsed-01's check.py (round 3). Every mutation breaks one rule of
the type at 0.3, of ADR-114, of ADR-115 or of the section form, and check.py must fail on it and name that rule.
A clean result from an untested checker is not evidence.

Mutations land only inside a prompt's own code block: the tables above quote every shared sentence,
and a replace over the whole file lands there, where the checker rightly never looks.

Usage, from the repo root: python3 registry/pdp-dr-types/sets/05-social-endorsed-01/knownbad.py
Exits 0 only when the clean set passes AND every mutation is caught for the stated reason.
"""
import io, json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "check.py")
clean = io.open(os.path.join(HERE, "prompts.md"), encoding="utf-8").read()
clean_json = json.load(io.open(os.path.join(HERE, "prompts.json"), encoding="utf-8"))

REAL = ("It is a real photograph with true texture and a soft cast shadow, and nothing in the frame "
        "is old, worn, scratched or faded.")
G1 = "Use the attached product photo as the exact reference."
NO_TEXT = "No text."
PRODUCT = "Cordless Car Wash Tool"
DRESS = ("in grey work coveralls with the sleeves pushed up and the forearms wet, rubber boots on the "
         "wet ground, no logo, badge or name tag")

_CUT = clean.index("\n## 1 — ")
HEAD, PROMPTS = clean[:_CUT], clean[_CUT:]
_P = {n: PROMPTS.index(f"\n## {n} — ") for n in (1, 2, 3)}


def at(n, *pairs):
    """Replace inside prompt n's code block — or, for its heading, inside the heading line. Takes one
    or more old, new pairs, each of which must match exactly once."""
    s = _P[n]
    e = _P.get(n + 1, len(PROMPTS))
    part = PROMPTS[s:e]
    if pairs[0].startswith("## "):
        ts, te = 0, part.index("\n", 1)
    else:
        ts = part.index("```\n") + 4
        te = part.index("\n```", ts) + 4
    body = part[ts:te]
    for old, new in zip(pairs[0::2], pairs[1::2]):
        assert body.count(old) == 1, (n, old[:50], body.count(old))
        body = body.replace(old, new)
    part = part[:ts] + body + part[te:]
    return HEAD + PROMPTS[:s] + part + PROMPTS[e:]


def run(md_text, json_obj=None):
    with tempfile.TemporaryDirectory() as d:
        md = os.path.join(d, "prompts.md")
        io.open(md, "w", encoding="utf-8").write(md_text)
        cmd = [sys.executable, CHECK, md]
        if json_obj is not None:
            jp = os.path.join(d, "prompts.json")
            io.open(jp, "w", encoding="utf-8").write(json.dumps(json_obj, ensure_ascii=False))
            cmd += ["--json", jp]
        r = subprocess.run(cmd, capture_output=True, text=True)
        return r.returncode, r.stdout


def json_with(n, **changes):
    d = json.loads(json.dumps(clean_json))
    for s in d["slots"]:
        if s["n"] == n:
            for k, v in changes.items():
                if v is None:
                    s.pop(k, None)
                else:
                    s[k] = v
    return d


def json_top(**changes):
    d = json.loads(json.dumps(clean_json))
    for k, v in changes.items():
        if v is None:
            d.pop(k, None)
        else:
            d[k] = v
    return d


PAD = " The car park is quiet and tidy, the morning is calm, and the light falls across the ground." * 12

MUTATIONS = [
    # ---- the section form
    ("prompt 1 padded past the gate",
     at(1, "Her eyes are on the spray.", PAD.strip() + " Her eyes are on the spray."), None,
     "over the 1800 gate"),
    ("prompt 2 split into two paragraphs",
     at(2, "His eyes are on", "\n\nHis eyes are on"), None,
     "is not one paragraph"),
    ("the lock tone reworded in prompt 3",
     at(3, "Crisp daylight with a soft directional key", "Warm golden light with a soft directional key"), None,
     "lock tone sentence appears 0"),
    ("the real-never-worn sentence dropped from prompt 1",
     at(1, " " + REAL, ""), None, "real-never-worn sentence appears 0"),
    ("the no-words sentence dropped from prompt 2",
     at(2, " " + NO_TEXT, ""), None, "no-words sentence appears 0"),
    ("the G1 sentence dropped from prompt 3",
     at(3, " " + G1, ""), None, "does not end with the G1 sentence"),
    ("a sentence after G1 in prompt 1",
     at(1, G1 + "\n```", G1 + " Keep it natural.\n```"), None, "does not end with the G1 sentence"),
    ("the product named twice in prompt 2",
     at(2, "grime and water sheet off the rim", "grime and water from the " + PRODUCT + " sheet off the rim"),
     None, "names the product 2 times"),
    ("the product not named in prompt 3",
     at(3, "the " + PRODUCT + " in her practised grip", "the tool in her practised grip"), None,
     "names the product 0 times"),

    # ---- ADR-114: the work is happening
    ("the work stopped in prompt 1 (no longer mid-task)",
     at(1, "She is mid-rinse: the " + PRODUCT, "She is holding the " + PRODUCT), None,
     "does not put the person mid-task"),
    ("the trade's grip dropped from prompt 2",
     at(2, "in his practised grip", "in his hand"), None, "practised grip"),
    ("a dry frame in prompt 1 (nothing leaves the product)",
     at(1, "sends a steady fan of water across the panel", "rests against the panel",
        ", with water running across the tarmac", ""), None,
     "no water leaves the product"),
    ("what the work needs dropped from prompt 1 (no bucket, no intake hose)",
     at(1, ", and its intake hose runs down into a filled bucket at her feet", ""), None,
     "does not put what the work needs in frame"),
    ("the mark of work dropped from prompt 3",
     at(3, "and behind the spray a bright clean band runs the length she has already passed, ", ""), None,
     "does not show the mark the work has left"),
    ("clean dry clothes in prompt 1",
     at(1, DRESS, "in a crisp cotton outfit"), None,
     "does not dress the person in working clothes"),
    ("the eyes leave the work in prompt 2",
     at(2, "His eyes are on the spray.", "He smiles warmly."), None,
     "does not fix the eyes on the work"),
    ("the trade dropped from prompt 1 (a person, not a trade)",
     at(1, "a North American mobile car detailer in her forties", "a North American woman in her forties"), None,
     "does not carry its own trade"),
    ("the casting dropped from prompt 3",
     at(3, "a North American building maintenance technician", "a building maintenance technician"), None,
     "does not name its casting positively"),

    # ---- the frames stay apart
    ("a camera no frame declares in prompt 2",
     at(2, "from low at the front wheel", "from directly above"), None,
     "does not carry its own camera line"),
    ("prompt 3 takes prompt 1's camera",
     at(3, "from a step back along the balcony, close enough", "from a step back at the side, close enough",
        "a North American building maintenance technician", "a North American mobile car detailer"), None,
     "three different cameras"),

    # ---- what round 1 failed on, and what the register refuses
    ("the product held up at chest height in prompt 2",
     at(2, "crouches at the front wheel arch", "holds it up at chest height beside the front wheel arch"), None,
     "a presentation to the lens"),
    ("prompt 1 back in the portrait register",
     at(1, "Editorial realism photo", "Editorial realism portrait photo"), None,
     "a portrait register"),
    ("a studio ground under an outdoor trade in prompt 3",
     at(3, "of an apartment balcony", "of an apartment balcony, against a plain grey seamless backdrop"), None,
     "a studio ground for an outdoor trade"),
    ("a posed smile in prompt 1",
     at(1, "Her eyes are on the spray.", "She is smiling at the camera."), None,
     "a posed face"),

    # ---- compliance and G2
    ("a title before the person in prompt 1",
     at(1, "a North American mobile car detailer in her forties",
        "Dr. Elena Ruiz, a North American mobile car detailer in her forties"), None,
     "a named person or title"),
    ("a real institution in prompt 3",
     at(3, "of an apartment balcony", "of a university apartment balcony"), None,
     "a real institution"),
    ("an award on the bonnet in prompt 2",
     at(2, "on an apartment forecourt", "on an apartment forecourt, an award trophy on the bonnet"), None,
     "a certificate on the wall"),
    ("a verdict word in prompt 1",
     at(1, "Her eyes are on the spray.", "The finish is proven clean. Her eyes are on the spray."), None,
     "a verdict word"),
    ("a second person in prompt 3",
     at(3, "works along the railing", "works with an assistant along the railing"), None,
     "a second person"),
    ("a minor in prompt 2",
     at(2, "on an apartment forecourt", "on an apartment forecourt with a child watching"), None,
     "a minor"),
    ("Asian casting in prompt 3",
     at(3, "a North American building maintenance technician", "an Asian building maintenance technician"), None,
     "Asian-presenting"),
    ("the product described in prompt 1 (G2)",
     at(1, "the " + PRODUCT + " in her practised grip", "the blue " + PRODUCT + " in her practised grip"), None,
     "describes the product"),
    ("quoted words in prompt 1",
     at(1, "Her eyes are on the spray.", "The words \"Expert view\" sit on the panel. Her eyes are on the spray."),
     None, "quotes words in a wordless frame"),
    ("a drawn element called small in prompt 2",
     at(2, "grime and water sheet off the rim", "small grime specks and water sheet off the rim"), None,
     "called small or thin"),
    ("a ratio in prompt 2",
     at(2, "Editorial realism photo", "Editorial realism 4:3 photo"), None, "the frame's shape"),
    ("a share of the frame in prompt 3",
     at(3, "with water running to the drain", "with 60% of the water running to the drain"), None,
     "a share of the frame"),
    ("a distance figure in prompt 1",
     at(1, "with water running across the tarmac", "from 2 m away, with water running across the tarmac"), None,
     "a distance figure"),

    # ---- the file's own shape
    ("a fourth prompt the ledger does not declare",
     clean.rstrip() + "\n\n---\n\n## 4 — `05-social-endorsed` v0.3 · `expert.scene`\n\n```\n"
     "Editorial realism photo. No text.\n```\n", None, "the ledger declares"),
    ("the wrong type in prompt 1's heading",
     at(1, "## 1 — `05-social-endorsed` v0.3", "## 1 — `05-social-handoff` v2.9"), None,
     "heading does not name"),

    # ---- ADR-115: the named garments, the trade's kit, the film of dirt, the eyes
    ("the trade's kit dropped from prompt 1",
     at(1, " Her work van stands close behind her with its tailgate up, a second bucket and a stack of "
           "folded microfibre towels on it.", ""), None,
     "does not bring the trade's kit into frame"),
    ("the film of dirt dropped from prompt 2",
     at(2, "The wheel wears an even film of road dust, ", ""), None,
     "does not make the dirt an even film"),
    ("the only-hose clause dropped from prompt 3",
     at(3, ", the only hose in the frame", ""), None,
     "the only hose in the frame"),
    ("a garment named by category in prompt 2",
     at(2, DRESS, "in a blue button-up work shirt and clean chinos"), None,
     "a garment named by category"),
    ("a turn toward the lens in prompt 3",
     at(3, "Her eyes are on the spray.", "She turns her head toward the lens for a moment."), None,
     "a turn toward the lens"),
    ("an already spotless panel in prompt 1",
     at(1, "The panel wears an even film of road dust", "The panel is already spotless"), None,
     "a surface with nothing to remove"),

    # ---- prompts.json
    ("prompts.json: the flag dropped from slot 2", clean, json_with(2, compliance=None),
     "carries compliance flag None"),
    ("prompts.json: a prompt out of step with prompts.md", clean,
     json_with(3, prompt="Editorial realism photo. No text."), "slot 3's prompt differs"),
    ("prompts.json: no attachment asked for", clean, json_with(1, attachments=0), "asks for 0 attachments"),
    ("prompts.json: still declaring the failed 0.2", clean, json_top(type_version="0.2"),
     "type_version is '0.2'"),
    ("prompts.json: the derivation dropped", clean, json_top(derivation=None),
     "does not name the expert it was built from"),
]

code, out = run(clean)
print(f"clean set: exit {code} — {out.strip().splitlines()[-1]}")
missed = 0 if code == 0 else 1
code_j, out_j = run(clean, clean_json)
print(f"clean set with its json: exit {code_j} — {out_j.strip().splitlines()[-1]}")
missed += 0 if code_j == 0 else 1
for name, md, js, expect in MUTATIONS:
    if md == clean and js is None:
        print(f"MISS  {name}: the mutation changed nothing")
        missed += 1
        continue
    code, out = run(md, js)
    if code == 1 and expect in out:
        print(f"ok    {name}")
    else:
        missed += 1
        print(f"MISS  {name}: exit {code}, wanted a failure containing {expect!r}; got: {out.strip()[:240]}")
print(f"{len(MUTATIONS) - min(missed, len(MUTATIONS))} of {len(MUTATIONS)} mutations caught")
sys.exit(1 if missed else 0)

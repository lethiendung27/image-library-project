"""Gate the v07 prompts before they ship. Run from the repo root or from this directory.

Checks the things that have actually gone wrong in this library: a ratio written into prompt
text (ADR-016), an `Avoid:` line (ADR-014), a missing or altered G1 block where the type needs
one, a prompt past its type's own ceiling, drawn text in types that carry no text layer, and a
person appearing in a type whose law has none.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
doc = json.load(open(os.path.join(HERE, "prompts.json"), encoding="utf-8"))

G1_FIRST = "Use the attached product photo as the exact reference for the cushion."
G1_REST = ["Preserve its shape, proportions, material, finish and colour exactly as shown.",
           "Do not redesign, restyle, simplify or add features."]
# a type is G1-exempt in these executions: the product is out of frame by the type's own law
NO_PRODUCT = {("01-pain-scene", "--candid"), ("01-pain-scene", "--confront"),
              ("02-cause-anatomy", "--diagnostic"), ("04-proof-lockedframe", "--rivals")}
# ceilings the type files state for themselves; 2500 is the adapter's re-read line
CEILING = {"04-proof-lockedframe": 1800, "05-persona-grid": 1800, "05-social-handoff": 1800,
           "02-cause-anatomy": 1800}
# person NOUNS only. "face" matched "top face" and ghostbody's own mandatory "no face";
# "driver" matched "driver's seat". A polysemous word is a false positive waiting to fire.
PEOPLE = ["woman", "man", "person", "child", "girl", "boy", "daughter"]
NO_PEOPLE_TYPES = {"03-mechanism-ghostbody", "03-spec-explode", "03-spec-macro",
                   "03-use-grid", "03-spec-split"}

fail, n = [], 0
for s in doc["slots"]:
    if "options" not in s:
        continue
    for o in s["options"]:
        n += 1
        ctx = f"{s['slot_id']} {o['option']} {o['type']}"
        p = o["prompt"]
        flat = re.sub(r"\s+", " ", p)
        if re.search(r"\b\d+\s*:\s*\d+\b", p):
            fail.append((ctx, "a ratio is written into the prompt (ADR-016, adapter Rule 4)"))
        for w in ("square frame", "aspect ratio", "portrait frame", "landscape frame", "16:9"):
            if w in p.lower():
                fail.append((ctx, f"names the frame shape: {w!r}"))
        if re.search(r"(?im)^\s*(strictly\s+)?avoid\s*:", p):
            fail.append((ctx, "carries an Avoid: line (ADR-014)"))
        needs_g1 = (o["type"], o.get("variant")) not in NO_PRODUCT
        has_g1 = G1_FIRST in flat and all(x in flat for x in G1_REST)
        if needs_g1 and not has_g1:
            fail.append((ctx, "missing or altered G1 reference block"))
        if not needs_g1 and G1_FIRST in flat:
            fail.append((ctx, "carries a G1 block in an execution whose type forbids the product"))
        cap = CEILING.get(o["type"], 2500)
        if len(p) > cap:
            fail.append((ctx, f"LENGTH {len(p)} > {cap} for this type"))
        quoted = re.findall(r'"([^"]{3,})"', p)
        if quoted:
            fail.append((ctx, f"drawn text in a type with no text layer: {quoted[:2]}"))
        for w in ("step 1", "step 2", "then edit", "second pass", "post-process", "composite"):
            if w in p.lower():
                fail.append((ctx, f"multi-pass language: {w!r}"))
        if o["type"] in NO_PEOPLE_TYPES:
            for w in PEOPLE:
                if re.search(rf"\b{w}\b", p.lower()) and not (
                        o["type"] == "03-use-grid" and w in ("person", "face")):
                    fail.append((ctx, f"a person in {o['type']}, which has none: {w!r}"))

print(f"{n} prompts checked across {len([s for s in doc['slots'] if 'options' in s])} routed slots")
types = {o["type"] for s in doc["slots"] if "options" in s for o in s["options"]}
print("distinct types offered:", len(types))
for s in doc["slots"]:
    if "options" in s and len({o["type"] for o in s["options"]}) != 3:
        fail.append((s["slot_id"], "fewer than three DISTINCT types (ADR-058)"))
print()
if fail:
    print("FAILURES:")
    for c, m in fail:
        print(f"  [{c}] {m}")
else:
    print("0 failures")
sys.exit(1 if fail else 0)

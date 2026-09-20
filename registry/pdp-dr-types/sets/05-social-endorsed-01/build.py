"""Build set 05-social-endorsed-01 — three expert frames for the Cordless Car Wash Tool.

Round 3, at 05-social-endorsed 0.3 (ADR-115). Round 1 (0.1) held the product up with nothing in use.
Round 2 (0.2) put the work in the frame — 3 of 3 showed water leaving the tool and the intake hose in
a filled bucket — and the PERSON failed instead: "a work shirt" came back as a button-up dress shirt
over clean chinos twice, no frame carried the kit a trade arrives with, and the owner's answer was
"tôi chưa thấy thợ rửa xe lưu động, cư dân trang phục không phù hợp cho rửa xe". All six renders of
both rounds held a brass garden-hose nozzle rather than the attached product.

The one source of the set: it writes prompts.md and prompts.json. Edit this file, never those two.
Usage, from the repo root: python3 registry/pdp-dr-types/sets/05-social-endorsed-01/build.py
"""
import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))

PRODUCT = "Cordless Car Wash Tool"          # the page's own name (product.title)
PAGE = "pdp-dr-multifunctional-car-wash-tool-v01"
TEMPLATE = "TPL-PDP06 · LP2-T1-Deal-Final v1.0.4"
FIELD = "expert.scene"
FRAME = "4:3"
PHOTO = ("media.gallery.0.image — Resize_and_sharpen_image_2K_20260914170835.jpg, "
         "sha256 ff37a23bcee5b8c1405a118ad6cf63c96f3eb1a8956c63323f3bd518731da18e")

# ---------------------------------------------------------------- the derivation (ADR-114)
CONSTRAINT = ("no outdoor tap and no socket in the car park — the page's own pain: a bucket carried "
              "down two flights and a sponge rubbed at baked-on dirt")
USER = ("the apartment or condo resident, 30-65, who washes their own car in the building's lot, "
        "spot-cleans bird droppings, rinses a balcony, a bike or patio chairs (brief.persona and the "
        "six review lines)")
EXPERT = ("the mobile car detailer, whose trade meets that constraint every working day: water is "
          "carried to every job, and the judgement the block claims — battery, no tap, spray "
          "patterns — is theirs. Second: the building maintenance technician, who rinses communal "
          "balconies and walkways with no tap of their own")

# ---------------------------------------------------------------- the lock, proposed from the product
LOCK = {
    "proposed from": "a cordless bucket-fed washer for homes with no outdoor tap: practical, outdoor, water",
    "lighting family and colour tone": ("Crisp daylight with a soft directional key, true colour with "
                                        "neutral whites, in a palette of clean white, deep slate grey and "
                                        "a fresh mid-blue"),
    "typeface": "a bold grotesque in the manner of Roboto, with a straight-legged R",
    "text colour": "charcoal on light grounds, white on dark",
    "chip": "a flat deep-slate pill with white sentence-case text, no outline and no shadow",
    "accent": "a fresh mid-blue, on the chip and a call-out line only",
    "icon style": "simple line icons with square ends",
    "seamless ground": "a plain mid-grey seamless with a floor plane and a soft shadow",
}
TONE = LOCK["lighting family and colour tone"] + ", balanced contrast, readable in three seconds."
REAL = ("It is a real photograph with true texture and a soft cast shadow, and nothing in the frame "
        "is old, worn, scratched or faded.")
NO_TEXT = "No text."
G1 = "Use the attached product photo as the exact reference."

# The garments are NAMED, not categorised: round 2's "a work shirt" rendered as a button-up dress
# shirt 2 of 3, while grey work coveralls and boots rendered as a trade 1 of 1 (ADR-115).
DRESS = ("in grey work coveralls with the sleeves pushed up and the forearms wet, rubber boots on the "
         "wet ground, no logo, badge or name tag")
HOSE = "its intake hose runs down into a filled bucket"
ONLY_HOSE = "the only hose in the frame"

COMPLIANCE = {
    "flag": "endorsed-expert",
    "note": ("The `expert` block presents this face as an expert view of the product: its eyebrow reads "
             "\"Expert view\", it carries an award badge and three credential lines, and its own quote "
             "recommends the product. `expert.name` and `expert.role` are EMPTY on this page today, so no "
             "person is named and no profession is claimed in the HTML; the prompt shows the trade the "
             "page's constraint belongs to. If the page later prints a name or a credential beside this "
             "face, and that person does not exist or does not hold the expertise shown, the page carries "
             "a fabricated endorsement, which the FTC's endorsement rules treat as deceptive. A real "
             "expert's own photograph always wins; the merchant decides."),
}

SLOTS = [
    dict(n=1, role="a North American mobile car detailer in her forties", pronoun="her", subject="She",
         camera="from a step back at the side",
         place="an open apartment car park",
         task="works along the rear quarter panel of a customer's sedan in an open apartment car park",
         work=("the " + PRODUCT + " in her practised grip sends a steady fan of water across the panel, and "
               + HOSE + " at her feet, " + ONLY_HOSE),
         kit=("Her work van stands close behind her with its tailgate up, a second bucket and a stack of "
              "folded microfibre towels on it."),
         mark=("The panel wears an even film of road dust, and behind the spray a bright clean band of "
               "paint runs where she has already passed, with water running across the tarmac."),
         prediction="PASS — the CONTROL: the named coveralls, the van with its kit, and the film of dust "
                    "the clean band is cut into",
         changed="the garments are named, the trade's kit is in frame, the dirt is a film and the eyes "
                 "never leave the work"),
    dict(n=2, role="a North American mobile car detailer in his fifties", pronoun="his", subject="He",
         camera="from low at the front wheel",
         place="an apartment forecourt",
         task="crouches at the front wheel arch of a customer's car on an apartment forecourt",
         work=("the " + PRODUCT + " in his practised grip drives water into the wheel arch, and " + HOSE +
               " beside the wheel, " + ONLY_HOSE),
         kit=("A kneeling pad is under one knee, and his work van stands behind him with its tailgate up, "
              "a second bucket and a stack of folded microfibre towels on it."),
         mark=("The wheel wears an even film of road dust, grime and water sheet off the rim onto the wet "
               "ground, and the rim behind the spray is bright where he has already passed."),
         prediction="PARTIAL — the low camera may cut the van out of frame, and with it the trade",
         changed="one thing against the control: the camera drops to the wheel, so the kit has to survive "
                 "a low angle"),
    dict(n=3, role="a North American building maintenance technician in her forties", pronoun="her",
         subject="She", camera="from a step back along the balcony",
         place="an apartment balcony",
         task="works along the railing of an apartment balcony",
         work=("the " + PRODUCT + " in her practised grip sends water along the railing and the tiles "
               "below it, and " + HOSE + " at her feet, " + ONLY_HOSE),
         kit=("Her maintenance cart stands behind her with a second bucket and a long-handled brush laid "
              "across it."),
         mark=("The tiles wear an even film of grey dust, and behind the spray a bright clean band runs "
               "the length she has already passed, with water running to the drain."),
         prediction="PARTIAL — a second trade, and round 2 wet the whole balcony evenly, so the clean "
                    "band had nothing to be cut into",
         changed="one thing against the control: a second trade, with its own kit and its own surface"),
]

for s in SLOTS:
    s["gaze"] = ("Her" if s["pronoun"] == "her" else "His") + " eyes are on the spray."
    s["prompt"] = " ".join([
        f"Editorial realism photo {s['camera']}, close enough that {s['pronoun']} hands and the spray "
        f"read together: {s['role']}, {DRESS}, {s['task']}.",
        f"{s['subject']} is mid-rinse: {s['work']}.",
        s["kit"], s["mark"], s["gaze"], TONE, REAL, NO_TEXT, G1,
    ])

GATE = 1800
for s in SLOTS:
    assert len(s["prompt"]) <= GATE, (s["n"], len(s["prompt"]))

# ---------------------------------------------------------------- prompts.json
out = {
    "set": "05-social-endorsed-01",
    "status": "UNCOMMITTED, owner-gated",
    "round": 3,
    "type": "05-social-endorsed",
    "type_version": "0.3",
    "adr": "ADR-115",
    "page": PAGE,
    "template": TEMPLATE,
    "field": FIELD,
    "render_frame": FRAME,
    "attachment": PHOTO,
    "derivation": {"constraint": CONSTRAINT, "user": USER, "expert": EXPERT},
    "lock": LOCK,
    "slots": [],
}
for s in SLOTS:
    out["slots"].append({
        "n": s["n"], "type": "05-social-endorsed", "version": "0.3", "field": FIELD,
        "render_frame": FRAME, "attachments": 1, "words": [], "role": s["role"],
        "camera": s["camera"], "place": s["place"], "changed": s["changed"],
        "prediction": s["prediction"], "compliance": COMPLIANCE,
        "characters": len(s["prompt"]), "prompt": s["prompt"],
    })
io.open(os.path.join(HERE, "prompts.json"), "w", encoding="utf-8").write(
    json.dumps(out, indent=1, ensure_ascii=False) + "\n")

# ---------------------------------------------------------------- prompts.md
L = []
A = L.append
A("# pdp-dr set 05-social-endorsed-01 — three expert frames for the Cordless Car Wash Tool, round 3")
A("")
A("**Type:** `05-social-endorsed` 0.3, the expert block's image, rewritten on the owner's audit of "
  "round 2's renders, 2026-09-20 (ADR-115). **Status: UNCOMMITTED, owner-gated.** GENERATED by this "
  "folder's `build.py` — edit the script, never this file.")
A("")
A("## What round 2 settled, and what it did not")
A("")
A("**The work landed.** 3 of 3 showed water leaving the tool onto a real surface, and 3 of 3 showed the "
  "intake hose running into a filled bucket — round 1 had neither. That part of ADR-114 is kept word for "
  "word.")
A("")
A("**The person did not.** The owner: *\"tôi chưa thấy thợ rửa xe lưu động, cư dân trang phục không phù "
  "hợp cho rửa xe\"*. Read against the renders:")
A("")
A("| what was written | what came back | this round |")
A("|---|---|---|")
A("| *a work shirt with the sleeves rolled and wet* | a crisp button-up dress shirt over pale chinos, "
  "2 of 3; the one frame in grey work coveralls and boots read as a trade, 1 of 1 | the garments are "
  "NAMED: coveralls, boots, wet forearms |")
A("| the trade, named in words | nothing in frame said *paid to do this*: no van, no kit, no second "
  "bucket | the kit the trade arrived with is in the frame |")
A("| *turns his head toward the lens … without stopping* | a full face to the lens with a faint smile, "
  "1 of 1 | retired — the eyes stay on the work in all three |")
A("| a dusty strip beside a clean one | one car caked in dried mud, one already spotless, one balcony "
  "wet end to end | an even FILM of dust, and a bright clean BAND cut into it |")
A("")
A("**And 6 of 6 across both rounds held a brass garden-hose nozzle, not the attached product.** Each "
  "prompt now says the tool's own intake hose is the only hose in the frame, which is true of a "
  "bucket-fed cordless washer and takes the garden-hose scene away from the renderer. **It is a "
  "hypothesis, not a fix**: if the photo was never attached, that is the whole cause and this clause "
  "comes back out. Please say, per render, whether you attached it.")
A("")
A(f"**Page:** `{PAGE}`, template {TEMPLATE}. **Field:** `{FIELD}`, one image, rendered at {FRAME}.")
A("")
A("## The derivation the set is built on (ADR-114)")
A("")
A("| | |")
A("|---|---|")
A(f"| the constraint the product removes | {CONSTRAINT} |")
A(f"| the USER | {USER} |")
A(f"| the EXPERT | {EXPERT} |")
A("")
A("Rejected, and why: a mechanic repairs and does not wash; a car-accessory shop owner behind a counter "
  "has a title and no act; anyone in a laboratory judges nothing this page claims.")
A("")
A("## The three frames")
A("")
A("| # | the trade | changed against the control | camera | prediction |")
A("|---|---|---|---|---|")
for s in SLOTS:
    A(f"| {s['n']} | {s['role']} | {s['changed']} | {s['camera']} | {s['prediction']} |")
A("")
A("**Control — image 1, predicted PASS.** Every new clause at once on the plainest scene. If it fails, "
  "the fault is the type's, not the scene's.")
A("**Images 2 and 3 each change one thing** — the camera drops to the wheel, and the trade changes — so "
  "a failure says which.")
A("")
A("## What every prompt carries, word for word")
A("")
A("| name | the sentence |")
A("|---|---|")
A(f"| the named garments | `{DRESS}` |")
A("| the work | `is mid-rinse:` + the product doing its own thing on a real surface |")
A(f"| what the work needs | `{HOSE}` … `{ONLY_HOSE}` |")
A("| the trade's kit | the van with its tailgate up, or the maintenance cart — a second bucket on it |")
A("| the mark the work left | `an even film of` dust, and a `bright clean band` behind the spray |")
A("| the eyes | `… eyes are on the spray.` — in all three |")
A(f"| lighting family and colour tone | `{TONE}` |")
A(f"| real, never worn | `{REAL}` |")
A(f"| no words | `{NO_TEXT}` |")
A(f"| G1 | `{G1}` — last |")
A("")
A("## What is NOT written, and why")
A("")
A("| left out | why |")
A("|---|---|")
A("| the product held up, at chest height or toward the lens | the owner failed 3 of 3 that did (ADR-114) |")
A("| a work shirt, a polo, chinos | the category renders as office clothes on a job that moves water (ADR-115) |")
A("| any turn toward the lens | it came back as a full face and a smile, 1 of 1 |")
A("| a studio ground | this trade works outdoors; a seamless is refused for it |")
A("| a name, a credential, a certificate | the page prints none, and no real institution enters the frame |")
A("| a logo on the van or the coveralls | a trade's kit makes the trade legible; a brand would fabricate one |")
A("| the nozzle, the battery, the colour | G2: the prompt places the product and never describes it |")
A("| any word in the frame | a section image outside the gallery carries none (ADR-096) |")
A("")
A(f"**Attach the product photo:** `{PHOTO}`. **If it is not attached the render is void** — six renders "
  "across two rounds show what comes back without it. Say for each render whether it was attached.")
A("")
A("## Watch items")
A("")
A("1. Is the thing in the hand the attached product, or a hose nozzle for the seventh time?")
A("2. Do the clothes read as a person who works in water — coveralls, boots, wet forearms?")
A("3. Is the van or the cart in frame, with a second bucket on it? Does it say *paid to do this*?")
A("4. Is the dirt an even film, with a bright clean band cut into it behind the spray?")
A("5. Does anyone look at the camera? Nobody should.")
A("6. Which renders had the photo attached?")
for s in SLOTS:
    A("")
    A("---")
    A("")
    A(f"## {s['n']} — `05-social-endorsed` v0.3 · `{FIELD}` · {FRAME} · ATTACH 1 · no words · "
      f"{s['prediction'].split(' — ')[0]}")
    A("")
    A(f"**The trade:** {s['role']}. **Camera:** {s['camera']}. **Place:** {s['place']}.")
    A("")
    A(f"**Compliance flag:** `{COMPLIANCE['flag']}` — {COMPLIANCE['note']}")
    A("")
    A("```")
    A(s["prompt"])
    A("```")
A("")
io.open(os.path.join(HERE, "prompts.md"), "w", encoding="utf-8").write("\n".join(L))
print("05-social-endorsed-01 round 3:", ", ".join(f"{s['n']}:{len(s['prompt'])}" for s in SLOTS),
      f"(gate {GATE})")

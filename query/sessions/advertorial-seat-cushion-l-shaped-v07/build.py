#!/usr/bin/env python3
"""Build prompts.md and prompts.json for advertorial-seat-cushion-l-shaped-v07.

Page 122, the ergonomic memory foam seat cushion, routed again from the same content.json
the page exported at v06 and from the product brief
`Product Input 8 Sep/02-fill-inputs-ergonomic-memory-foam-seat-cushion.csv`.

Why a v07 at all: v06 was routed 2026-08-24 and the law moved under it. ADR-058 wants three
DISTINCT active types per image slot where v06's review wall carried one; ADR-090 made the
option pool content-first and put the cross-slot rules on the recommended SET; ADR-088 and
ADR-089 replaced G14's refusal with a flag a rendering harness ships; ADR-060 removed
`avoid_when`; and eight of the fourteen types this page routes have been rewritten since,
01-pain-scene from 1.14 to 1.18 among them, which is why none of v06's prompt text is reused.

Type versions are read from the COMMITTED type files, not from the working tree: another
lane holds uncommitted edits to 03-mechanism-ghostbody and 03-mechanism-xray, and a session
that cites a version git cannot show is not reproducible.
"""
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAGE_ID = "122"

# ---------------------------------------------------------------- the style lock
# ADR-093's session lock is LP2 law and this page is an advertorial (LP1), so it is a house
# choice here rather than a rule. It costs nothing and it is what makes twelve frames read as
# one page: the same man, the same cab, the same home office, one colourway, one accent.
STYLE_LOCK = {
    "person": "the same man, late forties, in the same creased work shirt, in every frame that "
              "carries a person",
    "places": "two places and no others: the cab of his van in a suburban driveway, and the "
              "corner of a home office with a window on the left",
    "ground": "neutral and light — plaster, oatmeal fabric, pale desk surfaces; nothing "
              "saturated behind the subject",
    "light": "real daylight from one side, soft, no rim light and no studio key",
    "product": "the black one-piece L-shaped cushion, one unit, never two",
    "accent": "red appears only where G3 assigns it — a symptom glow, a wrong-state mark — "
              "and nowhere else",
}


def type_version(tid):
    """Version from the committed type file, so the citation survives in git."""
    blob = subprocess.run(["git", "-C", ROOT, "show", f"HEAD:registry/types/{tid}.md"],
                          capture_output=True, text=True, check=True).stdout
    for line in blob.split("\n---\n", 1)[0].splitlines():
        if line.startswith("version:"):
            return line.split(":", 1)[1].strip().strip('"')
    raise SystemExit(f"no version in {tid}")


G1 = ("Use the attached product photo as the exact reference for the cushion.\n"
      "Preserve its shape, proportions, material, finish and colour exactly as shown.\n"
      "Do not redesign, restyle, simplify or add features.")

# ---------------------------------------------------------------- slots
# Each entry: the slot, what the section argues, the recommendation and why, then three
# options, each a DISTINCT active type (ADR-058). `prompt` is what ships, paste-and-run.
SLOTS = []

SLOTS.append({
    "slot_id": "hero.image",
    "role": "hero",
    "ratio": "16:9",
    "asset": "122-01-hero-relief-hero.png",
    "placement": "Advertorial header, under the title and above the byline.",
    "recommended": "A",
    "rationale":
        "The page's own title is 'how he fixed severe lower back pain behind the wheel', and "
        "the reader arrives SOLUTION AWARE and sceptical — the brief says they have already "
        "bought cushions, pillows, a chair and massages. A header that shows the fix in the "
        "place the title names answers the scepticism before the story starts. "
        "ONE-TYPE-ONCE decided the rest: v06 recommended 01-pain-scene here AND at "
        "content.items.0, which spends one type twice in the shipped set, so the pain frame "
        "goes to the section whose copy IS the pain beat and this slot takes the relief hero. "
        "B is offered here anyway (ADR-090: a type recommended elsewhere is not spent for this "
        "slot's options) and is the better frame if the owner wants the page to open cold. "
        "PRODUCT PRESENCE: required by A and C, and the attachments array is empty — attach a "
        "photo of the black cushion. PROMPT RISK: the passive pose is where 06-relief-hero's "
        "own PARTS warns the model hides the contact point, so the pose names the gap the "
        "cushion fills.",
    "gif": {"eligible": False, "form": "none",
            "reason": "A header that argues the after-state is a held state, and this type's "
                      "own law puts pain only inside an inset. Nothing crosses a boundary in "
                      "the frame, so a loop would animate a person sitting still."},
    "options": [
        {
            "type": "06-relief-hero", "variant": "--commercial",
            "axes": {"register": "commercial", "inset_mode": "none"},
            "varies_on": "baseline",
            "gloss": "The fix in the place the title names: the driver back in his own cab, "
                     "the cushion under him and behind him as one piece, the drive ahead of "
                     "him rather than behind.",
            "note": "Needs the product photo. Passive product, so the pose is relaxed and the "
                    "gaze is off the product; the frame names the seat-to-backrest gap so the "
                    "contact point cannot be hidden.",
            "prompt": """Commercial lifestyle photograph. One frame, no panels, no insets.

""" + G1 + """
Render it at 30% of the frame height, integrated with the scene lighting, in the driver's seat with its seat section under him and its backrest section standing up against the seat back, the joint between the two sitting exactly where the seat meets the backrest. Show the black colourway, one unit.

A man in his late forties in a creased work shirt sits back in the driver's seat of his van, both hands loose in his lap, shoulders down, looking out through the windscreen at the road rather than at anything in the cab. He is relaxed and unhurried.

His back is against the cushion's upright section along its whole length, and his hips sit level with his knees rather than below them.

Setting: the cab of a working van parked on a suburban driveway, filled to the edges with the things of the working day — a lanyard on the indicator stalk, a flask in the door bin, a clipboard face down on the passenger seat, a jacket over the headrest, a phone in the cradle, a parking permit curling on the dash. None of them carries printed words.

Light: real daylight through the windscreen from the left, soft, no rim light.
Grade: bright, high-key, neutral, true to life.""",
        },
        {
            "type": "01-pain-scene", "variant": "--candid",
            "axes": {"gaze": "candid"},
            "varies_on": "type: 01-pain-scene",
            "gloss": "The page opened cold: the same man hauling himself out of the cab at the "
                     "end of the run, with the doughnut cushion he already bought shoved "
                     "forward against the seat front — the failed tool is the evidence.",
            "note": "Needs no photo: this type forbids the product and is G1-exempt. It is "
                    "RECOMMENDED at content.items.0, so picking it here means the pain beat "
                    "there takes B or C.",
            "prompt": """An ordinary photograph in ordinary light. Editorial photojournalism, natural and unstaged. Single frame.

A man in his late forties in a creased work shirt, at the open door of his van at the end of the run, mid-way through hauling himself up and out with one hand clamped on the door frame above him and the other pushed flat into the seat. Under that force: that shoulder hitched up against his ear, the arm locked straight, both feet planted wide on the tarmac, his hips barely lifted and his back moving as one piece with no bend in it. Face: jaw set, eyes narrowed, breath held.

On the seat he is pushing off, a flat ring-shaped foam cushion has been shoved forward against the front edge of the seat base, its cover rucked and its centre worn shiny, nowhere near where he was sitting.

Behind him on the driveway a child's football has come to rest against the closed garage door, and the front door of the house stands open with the hall light on and nobody walking out.

One specific place: a suburban driveway at the end of the working day, dusk.

He is unaware of the camera. The real light of the place: the last daylight down the driveway, the cab's dome light behind him, the hall light through the open door.

An ordinary photograph in ordinary light: true colour, no filter, moderate depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.""",
        },
        {
            "type": "02-symptom-rail", "variant": None,
            "axes": {},
            "varies_on": "type: 02-symptom-rail",
            "gloss": "The header as an inventory: the man at the wheel with the cushion "
                     "working, and a rail down the right edge counting the three places the "
                     "brief says the ache starts — lower back, hip, tailbone.",
            "note": "Needs the product photo. This type puts the product in the frame at the "
                    "top of the page, which spends the reveal; it earns the slot only if the "
                    "owner wants the three zones named before the story begins.",
            "prompt": """Clean e-commerce infographic tile, bright and airy, sharp focus. Photographic scene on the left, a vignette rail down the right edge.

""" + G1 + """
Render it at 28% of the hero height, integrated with the scene lighting, under him and behind him in the driver's seat as one piece, the joint sitting where the seat meets the backrest, seen from a front three-quarter angle and unobstructed. Show the black colourway.

Filling the left 72% of the frame: a man in his late forties in a creased work shirt sits at the wheel of his van on a suburban driveway, calm and content, gaze out through the windscreen. Around him the things of the working day — a flask in the door bin, a clipboard on the passenger seat, a jacket over the headrest. Soft daylight from the left, background gently blurred, bright high-key neutral grade, the man offset to the left.

Down the right 26% of the frame: a vertical band with a pale tint gradient and a soft S-curved left edge, carrying exactly three circular vignettes stacked evenly with white ring borders, equal diameter, generous spacing, in the same light and style as the scene. Each is a tight crop of the same man, no face anywhere in them, ordered top to bottom down the body: a hand pressing the small of the back, a hand pressing the outside of the hip, a hand pressing the base of the spine at the seat edge.

In each vignette a soft red radial glow sits centred under the pressing hand, three glows in total, one per vignette.

Across the lower back where the cushion's upright section meets him, fine warm-white contour lines wrap the small of his back and follow its curve, showing the support running into it. No other mark anywhere in the frame.""",
        },
    ],
})

SLOTS.append({
    "slot_id": "content.items.0.image",
    "role": "problem-agitation",
    "ratio": "16:9",
    "asset": "122-02-content0-pain-scene.png",
    "placement": "Beside the breaking-point beat, the evening he could not stand up from the kitchen table.",
    "recommended": "A",
    "rationale":
        "The section's copy is a single moment with a witness in it, which is what this type "
        "renders best, and it is the page's only pain beat once the hero takes the relief "
        "frame. EVIDENCE: the type ranks the failed tool third and the brief supplies one — a "
        "doughnut cushion that 'only raised his hips and slid forward' — but rank 1, the "
        "symptom on the body, is available here and stronger, so A writes the locked hips and "
        "the hand braced on the table and keeps the failed cushion for content.items.1 where "
        "the copy is about the failures themselves. COST: A14 is the clause this slot exists "
        "to satisfy — the daughter halfway out of her chair with her hands already reaching, "
        "the meal going cold. B is the honest second: the same evening read as the three "
        "places it hurts. C is offered and CANNOT ship beside A — `01-pain-split` and "
        "`01-pain-scene` are `never_with` — so picking C moves the hero's pain option too.",
    "gif": {"eligible": False, "form": "none",
            "reason": "The beat is one failed effort, not a transition: what changes across it "
                      "is that someone else gets up instead. `query/runbook.md` Step 5c asks "
                      "for a state that changes under the product's action, and there is no "
                      "product in this frame."},
    "options": [
        {
            "type": "01-pain-scene", "variant": "--candid",
            "axes": {"gaze": "candid"},
            "varies_on": "baseline",
            "gloss": "The kitchen table, mid-effort: both hands driving down into the table "
                     "edge, the chair pushed back, the hips not following.",
            "note": "Needs no photo — the type forbids the product and is G1-exempt.",
            "prompt": """An ordinary photograph in ordinary light. Editorial photojournalism, natural and unstaged. Single frame.

A man in his late forties in a creased work shirt, at the kitchen table after the drive home, mid-way through pushing himself up out of the chair with both hands driving straight down into the table edge. Under that force: both arms locked, elbows turned out, shoulders driven up toward his ears, the chair pushed back behind him, his hips still low and his knees still bent under the table. Face: mouth open on a held breath, brow drawn in, chin tucked.

His hips have stayed folded where they were: the small of his back is rounded backward over the seat edge and his weight has gone onto the base of his spine rather than his feet.

Across the table his daughter is halfway out of her own chair with both hands already reaching toward him, and two plates of food sit untouched and steaming between them.

One specific place: a small kitchen at the end of the working day, early evening.

He is unaware of the camera. The real light of the place: the ceiling light over the table, the last of the daylight through the window behind him.

An ordinary photograph in ordinary light: true colour, no filter, moderate depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.""",
        },
        {
            "type": "02-symptom-rail", "variant": None,
            "axes": {},
            "varies_on": "type: 02-symptom-rail",
            "gloss": "The same evening as a count: him at the table with the cushion on the "
                     "chair, and three vignettes naming where the ache starts and spreads.",
            "note": "Needs the product photo. The rail's hero has to show the product working "
                    "(G7), so this option introduces the cushion one section earlier than the "
                    "story does.",
            "prompt": """Clean e-commerce infographic tile, bright and airy, sharp focus. Photographic scene on the left, a vignette rail down the right edge.

""" + G1 + """
Render it at 26% of the hero height, integrated with the scene lighting, on the kitchen chair under him and behind him as one piece, the joint sitting where the seat meets the chair back, seen from a front three-quarter angle and unobstructed. Show the black colourway.

Filling the left 72% of the frame: the same man in his late forties in a creased work shirt sits at his kitchen table in the early evening, calm, a mug in one hand, gaze across the table. Around him an ordinary kitchen — a fruit bowl, a tea towel over the oven rail, a jar of utensils. Soft daylight from the window on the left, background gently blurred, bright high-key neutral grade, the man offset to the left.

Down the right 26% of the frame: a vertical band with a pale tint gradient and a soft S-curved left edge, carrying exactly three circular vignettes stacked evenly with white ring borders, equal diameter, generous spacing, in the same light and style as the scene. Each is a tight crop of the same man, no face anywhere in them, ordered top to bottom down the body: a hand pressing the small of the back, a hand pressing the outside of the hip, a hand pressing the base of the spine where it meets a chair edge.

In each vignette a soft red radial glow sits centred under the pressing hand, three glows in total, one per vignette.

Across the small of his back where the cushion's upright section meets him, fine warm-white contour lines wrap the lower back and follow its curve. No other mark anywhere in the frame.""",
        },
        {
            "type": "01-pain-split", "variant": "--mirror",
            "axes": {},
            "varies_on": "type: 01-pain-split",
            "gloss": "The evening as the type's strongest form: the same man, the same chair, "
                     "the same shot, and only the state changing — pelvis rolled back on the "
                     "left, level and supported on the right.",
            "note": "CANNOT SHIP BESIDE `01-pain-scene` — the two are `never_with` in the "
                    "index, so choosing C here also removes the hero's option B. Needs the "
                    "product photo. `--mirror` drops the hotspot and the jag by law and "
                    "carries the invariants block that made one person render as one person.",
            "prompt": """E-commerce comparison tile, high contrast, sharp. Two panels, a hard vertical split at 50/50, each panel running to the frame edge. No border of any kind.

""" + G1 + """
Render it at 30% of the panel height, integrated with the scene lighting, in the right panel only: on the kitchen chair under him and behind him as one piece, the joint where the seat meets the chair back. Show the black colourway.

The same man in both panels, named once: late forties, short grey-flecked hair, clean-shaven, a creased blue work shirt and dark trousers, seen from the side at seat height from the same distance, filling the same share of each panel, at the same kitchen table with a fruit bowl behind him and a tea towel over the oven rail, in the same soft daylight from the window on the left.

Left panel, desaturated to grey: he sits on the bare wooden chair, his pelvis rolled backward, the small of his back rounded away from the chair back with an open gap behind it, his knees riding above his hips and his shoulders dropped forward over the table.

Right panel, full colour: the same man on the same chair with the cushion, his hips level with his knees, the small of his back filled and supported along its whole length, his shoulders back over his hips.

In the top-left corner a flat solid red disc with a cross cut out of it; in the top-right corner a flat solid green disc with a check mark cut out of it, both the same diameter.

The right panel is brighter and airier than the left, by light and calm, with the room unchanged.""",
        },
    ],
})

SLOTS.append({
    "slot_id": "content.items.1.image",
    "role": "proof",
    "ratio": "16:9",
    "asset": "122-03-content1-lockedframe-rivals.png",
    "placement": "Beside the beat where every earlier fix is listed and dismissed.",
    "recommended": "A",
    "rationale":
        "The section IS the 'I tried three things and none worked' beat, which is the exact "
        "case `--rivals` names, and the brief supplies the three by name: a flat ring cushion "
        "that slid forward, a strap-on lumbar pillow that pushed the shoulders forward, and "
        "the folded-something everyone tries. VARIANT SELECTION was checked before the "
        "variant was chosen: `04-proof-lockedframe`'s own rule bars `--rivals` where the "
        "difference between products cannot appear in a static frame. Here it can — the "
        "objects differ in shape and in where they sit on the seat — so the rivals form is "
        "legal, and the page does not need `--timelapse`. FAIRNESS: none of the three is "
        "damaged, dirty or badly lit, because uglifying them confesses staging. PRODUCT "
        "PRESENCE: none in A, by law — `--rivals` drops the reference block, which also makes "
        "A the one option here that needs no attachment.",
    "gif": {"eligible": False, "form": "none",
            "reason": "Three still objects under one locked camera are inspected, not watched. "
                      "The argument is a set of differences the eye travels between, and "
                      "nothing in the frame changes state."},
    "options": [
        {
            "type": "04-proof-lockedframe", "variant": "--rivals",
            "axes": {"camera_lock": "strict"},
            "varies_on": "baseline",
            "gloss": "One camera, one seat, three things he already owns — and none of them "
                     "wins.",
            "note": "Needs no photo: `--rivals` drops the product reference block by law, so "
                    "the empty attachments array is correct rather than missing.",
            "prompt": """Honest documentary product test photography, unstyled, natural, sharp. Three equal vertical panels packed across the frame with thin white gutters, no outer border.

One camera for all three panels, stated once: a chest-height view in through the open driver's door of the same van, the same framing and the same distance in each, the seat base filling the lower two-thirds, the steering wheel in the upper right of every panel and the door sill along the bottom edge. One daylight exposure and one white balance throughout.

The only thing that changes between the panels is what is on the seat:
left panel, a flat ring-shaped foam cushion sitting on the seat base;
middle panel, a strap-on lumbar pillow strapped to the seat back;
right panel, a folded fleece blanket squared onto the seat base.

Each is an ordinary unbranded item in good condition, the kind anyone already owns, photographed with the same care: the same exposure, the same tidiness, the same generosity of framing. No panel is favoured, and nothing in the frame says which is better.

Grade: one muted, cool grade across all three panels.""",
        },
        {
            "type": "03-spec-split", "variant": None,
            "axes": {},
            "varies_on": "type: 03-spec-split",
            "gloss": "The failure as a component argument: the flattened foam pad everyone "
                     "owns on one side of a diagonal, the one-piece moulded core on the "
                     "other, the product itself small along the bottom.",
            "note": "Needs the product photo, for the inset only. This type's register break "
                    "IS its message — photograph on the left is what wears out in the real "
                    "world, render on the right is what was engineered — so G5 does not bind.",
            "prompt": """High-contrast technical comparison graphic, e-commerce, sharp.

""" + G1 + """
Render it at 22% of the frame width, complete and whole, alone on a plain ground inside a rounded rectangle along the bottom of the frame, clear of every frame edge. Show the black colourway.

One diagonal runs from the lower left corner of the frame to the upper right corner, the upper right half advancing into the lower left.

Lower left half, photographed in a dim unstyled room, desaturated: a generic unbranded flat foam seat pad of the ordinary kind, its top face pressed into a shallow hollow that has not come back, one corner crushed and rounded, grey dust settled along the seams of its cover.

Upper right half, a 3D render against a dark gradient with cool rim lighting: the same class of component in its improved form, a one-piece moulded core whose seat section rises into an upright back section, the surface dense and even and the light running unbroken along the curve where the two sections meet.

A thin glowing line runs along the diagonal, with a burst of warm sparks where it crosses the centre of the frame.

In the lower left half a flat solid red disc with a cross cut out of it; in the upper right half a flat solid green disc with a check mark cut out of it, both the same diameter.""",
        },
        {
            "type": "01-pain-split", "variant": "--oldway",
            "axes": {},
            "varies_on": "type: 01-pain-split",
            "gloss": "The legacy fix in use rather than on a seat: him wedged behind a "
                     "strap-on pillow on the left, sitting on the one-piece cushion on the "
                     "right, same cab, same light.",
            "note": "CANNOT SHIP BESIDE `01-pain-scene`, which is recommended at "
                    "content.items.0 — the two are `never_with`. Needs the product photo. "
                    "`--oldway` keeps the legacy device generic and never mocks it.",
            "prompt": """E-commerce comparison tile, high contrast, sharp. Two panels, a hard vertical split at 50/50, each panel running to the frame edge. No border of any kind.

""" + G1 + """
Render it at 30% of the panel height, integrated with the scene lighting, in the right panel only: in the driver's seat under him and behind him as one piece, the joint where the seat meets the seat back. Show the black colourway.

The same man in both panels, named once: late forties, short grey-flecked hair, clean-shaven, a creased blue work shirt, at the wheel of the same van seen from the open passenger side at chest height, filling the same share of each panel, in the same daylight through the windscreen.

Left panel, desaturated to grey: he is wedged against a generic unbranded strap-on lumbar pillow buckled to the seat back, ordinary and undamaged. The friction shows in three things: the pillow has slid up behind his shoulder blades, its strap has pulled taut across the seat, and he is leaning forward off the seat back with one hand pushing down on his thigh.

Right panel, full colour: the same man in the same seat with the cushion, sitting back against its upright section along his whole lower back, both hands loose on the wheel, his hips level with his knees.

In the top-left corner a flat solid red disc with a cross cut out of it; in the top-right corner a flat solid green disc with a check mark cut out of it, both the same diameter.

The right panel is brighter and airier than the left, by light and calm, with the cab unchanged.""",
        },
    ],
})

SLOTS.append({
    "slot_id": "content.items.2.image",
    "role": "cause",
    "ratio": "16:9",
    "asset": "122-04-content2-cause-anatomy.png",
    "placement": "Beside the hidden-pelvic-drop explanation, the page's turn from symptom to cause.",
    "recommended": "A",
    "rationale":
        "The section indicts the seat rather than the buyer, which is what this type is for, "
        "and `--diagnostic` is the variant the advertorial middle asks for: the culprit is "
        "named before the product is revealed, and the product's own reveal is one section "
        "later at content.items.3. THE REMOVAL TEST, run before the prompt was written: take "
        "the backward-sloping seat out of the left panel and the rolled pelvis goes with it — "
        "a switchable state, not accumulated damage, so the type applies. THE ADMISSION GATE "
        "(owner, 2026-09-15) also passes: this product changes a POSITION, which is what the "
        "body can be drawn holding, rather than reducing effort with the body unchanged. "
        "STYLE: `airbrushed`, not `line-engraving`, which drew cream paper for a named ground "
        "twice at 1.18. B is the same argument in the other register and is recommended at "
        "content.items.3, so picking it here spends one type twice.",
    "gif": {"eligible": True, "form": "whole-frame", "kind": "cause", "type_id": "cause",
            "rung": "natural",
            "reason": "The section's claim IS a state changing under a cause: the pelvis rolls "
                      "back and the lumbar curve collapses as the seat takes the weight. "
                      "`registry/gif-types/cause.md` asks for one continuous state change in "
                      "one frame, and the two panels of the still are its two ends.",
            "brief": "Hold the left panel's illustration. Over three seconds the pelvis rotates "
                     "backward on the seat, the lumbar curve flattens toward the seat back, and "
                     "the red force arrow along the seat surface brightens as it does. Nothing "
                     "else moves; the right panel is not animated and the loop does not cut."},
    "options": [
        {
            "type": "02-cause-anatomy", "variant": "--diagnostic",
            "axes": {},
            "varies_on": "baseline",
            "gloss": "The cause as a 2D medical plate: the same seated body twice, the pelvis "
                     "rolled back over a backward-sloping seat on the left, sitting level on "
                     "a wedge-shaped support on the right.",
            "note": "Needs no photo: `--diagnostic` drops the product reference block and the "
                    "type is G1-exempt in that variant. The corrected panel is reached by the "
                    "CATEGORY, so no branded object appears.",
            "prompt": """2D illustration, airbrushed: soft gradients and modelled volume. Not photography, not 3D.

The whole seated body is in shot in both panels, seen from the side, the seat small within the frame.

Ground: one continuous deep muted slate-blue field behind both panels, taken from the inside of a working vehicle, stepping once in value at the divider — one step lighter on the right. Nothing else stands behind the subject.

In each panel the named structures are drawn in warm ivory over a translucent outline of the body: the pelvis, the sacrum at its base, the five lumbar vertebrae above it, and the thigh bone running forward to the knee.

Left panel, the wrong state: the man sits on a seat whose base slopes backward, his knees riding above his hips, the pelvis rotated backward onto the sacrum and the lumbar vertebrae pulled into a flat backward curve.

Right panel, the correct state: the same body on the same seat with a plain wedge-shaped support under him, the pelvis upright on its base, the knees level with the hips and the lumbar vertebrae returned to their forward curve.

Marks: one red double-headed curved arrow follows the sloping surface of the seat in the left panel and nowhere else. One curved line lies along the front edge of the lumbar vertebrae in each panel, red in the left and blue in the right. In the top corner of each panel a filled solid disc with the glyph cut out of it, red with a cross in the left and green with a check in the right, both the same diameter.""",
        },
        {
            "type": "03-mechanism-ghostbody", "variant": None,
            "axes": {},
            "varies_on": "type: 03-mechanism-ghostbody",
            "gloss": "The same cause in the technical register: an anonymous white mannequin "
                     "seated, the interior opened, the load on the base of the spine on the "
                     "left and carried on the right.",
            "note": "Needs the product photo. RECOMMENDED at content.items.3, so picking it "
                    "here spends one type twice in the shipped set (one-type-once, "
                    "`mapping/slot-rules.md` cross-rule 2). Written against the committed 2.3.",
            "prompt": """3D technical render on a seamless white infinity background, soft even studio lighting, subtle grey ambient occlusion, no cast shadow. Two equal panels side by side divided by a single thin vertical line.

""" + G1 + """
Render it in the right panel only, on the seat under the mannequin and standing up against the seat back, the joint where the seat meets the backrest, its upright section following the line of the lower spine. Show the black colourway.

One featureless matte white mannequin, no face, no hair, no clothing, no skin tone, in the same pose in both panels: seated on a plain seat seen from the side, feet on the floor, hands on its thighs.

The body is opened as a plane through its volume at the hips and lower back, showing, from the surface inward: the pelvis, the sacrum at its base, and the five lumbar vertebrae. Nothing deeper is drawn. The silhouette stays unbroken and the opening sits inside it.

Left panel, the wrong state: the plain seat alone, the pelvis rotated backward onto the sacrum, the lumbar vertebrae flattened.

Right panel, the correct state: the same body with the cushion, the pelvis upright and the lumbar vertebrae in their forward curve.

Marks, all flat, unshaded and hard-edged, laid on top of the render: the pelvis, sacrum and lumbar vertebrae in warm ivory in both panels. A flat red overlay on the sacrum in the left panel only. A flat blue band beside the lumbar vertebrae in the right panel only, following their curve and running only the length the cushion's upright section reaches. In the top corner of each panel a filled solid disc with the glyph cut out of it, red with a cross in the left and green with a check in the right.

Everything in the frame is matte white or grey except the marks and the cushion.""",
        },
        {
            "type": "02-symptom-rail", "variant": None,
            "axes": {},
            "varies_on": "type: 02-symptom-rail",
            "gloss": "The cause read forward into its consequences: the desk version of the "
                     "same sitting, with the rail counting where the drop ends up.",
            "note": "Needs the product photo. Offered at three slots on this page and shippable "
                    "at only one; the desk hero is what makes this instance different from the "
                    "cab hero offered at the header.",
            "prompt": """Clean e-commerce infographic tile, bright and airy, sharp focus. Photographic scene on the left, a vignette rail down the right edge.

""" + G1 + """
Render it at 26% of the hero height, integrated with the scene lighting, on the desk chair under him and behind him as one piece, the joint where the seat meets the chair back, seen from a front three-quarter angle and unobstructed. Show the black colourway.

Filling the left 72% of the frame: the same man in his late forties in a creased work shirt sits at a home-office desk in the late afternoon, calm and upright, gaze on the monitor, one hand on the mouse. Around him the things of the room — a mug, a notebook, a small plant, a window on the left. Soft daylight from that window, background gently blurred, bright high-key neutral grade, the man offset to the left.

Down the right 26% of the frame: a vertical band with a pale tint gradient and a soft S-curved left edge, carrying exactly three circular vignettes stacked evenly with white ring borders, equal diameter, generous spacing, in the same light and style as the scene. Each is a tight crop of the same man, no face anywhere in them, ordered top to bottom down the body: a hand pressing the small of the back, a hand pressing the outside of the hip, a hand pressing the base of the spine at the chair edge.

In each vignette a soft red radial glow sits centred under the pressing hand, three glows in total, one per vignette.

Across the small of his back where the cushion's upright section meets him, fine warm-white contour lines wrap the lower back and follow its curve. No other mark anywhere in the frame.""",
        },
    ],
})

SLOTS.append({
    "slot_id": "content.items.3.image",
    "role": "mechanism",
    "ratio": "16:9",
    "asset": "122-05-content3-ghostbody.png",
    "placement": "Beside the reveal: one continuous L-shaped piece, and why being one piece is the point.",
    "recommended": "A",
    "rationale":
        "`body_contact: true` is the attribute that decides this slot. It keeps "
        "`03-mechanism-ghostbody` in the pool, and the section's claim is exactly what that "
        "type argues — why this SHAPE works on a body — where the gate would have sent a "
        "non-contact product to `03-mechanism-xray` instead. A frames the claim the copy "
        "makes: the gap where the seat meets the backrest, open on the left and filled on the "
        "right, with the cushion's contour following the lumbar curve. If the owner also "
        "picks B at content.items.2, the two ghostbody frames must stay different arguments — "
        "that one contrasts the pelvis rotating, this one contrasts the gap being filled. "
        "B and C are the spec-job reading of the same feature: what it is made of rather than "
        "what it does to you.",
    "gif": {"eligible": False, "form": "none",
            "reason": "A two-panel wrong-and-right technical render is inspected rather than "
                      "watched: the reader's eye travels between the panels and nothing in "
                      "either one changes state. `registry/gif-instruction.md` asks for one "
                      "message carried by a change over time, and the change here is between "
                      "two frames, not inside one."},
    "options": [
        {
            "type": "03-mechanism-ghostbody", "variant": None,
            "axes": {},
            "varies_on": "baseline",
            "gloss": "The gap the copy names, drawn: open behind the lower back on the left, "
                     "filled by the cushion's upright section on the right, its contour "
                     "following the lumbar curve.",
            "note": "Needs the product photo. Written against the committed 2.3; another lane "
                    "holds an uncommitted 2.4 and this prompt does not read it.",
            "prompt": """3D technical render on a seamless white infinity background, soft even studio lighting, subtle grey ambient occlusion, no cast shadow. Two equal panels side by side divided by a single thin vertical line.

""" + G1 + """
Render it in the right panel only, on the seat under the mannequin and standing up against the seat back as one piece, the joint sitting exactly where the seat meets the backrest, its upright section following the curve of the lower spine. Show the black colourway.

One featureless matte white mannequin, no face, no hair, no clothing, no skin tone, in the same pose in both panels: seated on a plain seat seen from the side, feet on the floor, hands on its thighs.

The body is opened as a plane through its volume at the hips and lower back, showing, from the surface inward: the pelvis, the sacrum at its base, and the five lumbar vertebrae. Nothing deeper is drawn. The silhouette stays unbroken and the opening sits inside it.

Left panel, the wrong state: the plain seat alone, an open wedge of empty space between the small of the back and the seat back, the hips sunk into the seat base below the knees.

Right panel, the correct state: the cushion fills that space along its whole length, and the hips sit level with the knees.

Marks, all flat, unshaded and hard-edged, laid on top of the render: the pelvis, sacrum and lumbar vertebrae in warm ivory in both panels. A flat red overlay on the sacrum in the left panel only. A flat blue band beside the lumbar vertebrae in the right panel only, following their curve and running only the length the cushion's upright section reaches. In the top corner of each panel a filled solid disc with the glyph cut out of it, red with a cross in the left and green with a check in the right.

Everything in the frame is matte white or grey except the marks and the cushion.""",
        },
        {
            "type": "03-spec-explode", "variant": None,
            "axes": {},
            "varies_on": "type: 03-spec-explode",
            "gloss": "The same claim as a census: cover, one-piece core, the hollow the "
                     "tailbone sits over, and the non-slip base, separated along one axis.",
            "note": "Needs the product photo. The census names only what the brief says the "
                    "product contains — four parts, which clears this type's own "
                    "trivial-interior gate. The canvas is light because the product is black: "
                    "the ground's value is derived from the product so the silhouette "
                    "separates.",
            "prompt": """3D technical render, premium technical product visualization, sharp and high detail. Not photography.

""" + G1 + """
Render its parts separated along one vertical axis, in assembly order from the top down: the removable fabric cover lifted clear; the one-piece moulded foam core whose seat section rises into an upright back section, with the hollow opening through the seat where the tailbone sits; and the textured non-slip base panel beneath it. Each part is complete, in the reference's own material and colour, and nothing is drawn that the product does not contain.

The core is the brightest, sharpest and most central part of the frame.

Ground: a pale, even engineering canvas, far lighter in value than the product so the black silhouette separates cleanly. Across it, at very low contrast and fainter than the darkest shadow on any part, a sparse square lattice of fine straight lines — an orthogonal grid, not concentric rings and not wavy bands.

No text, no numerals, no part labels and no callout lines anywhere in the frame.""",
        },
        {
            "type": "03-spec-macro", "variant": None,
            "axes": {},
            "varies_on": "type: 03-spec-macro",
            "gloss": "The material claim at close range: the cut face of the foam under a "
                     "hand's pressure, every cell resolved, the surface rising again behind "
                     "the press.",
            "note": "Needs the product photo. This type's SKELETON still carries a `RATIO:` "
                    "line, which ADR-016 and adapter Rule 4 keep out of prompt text — it is "
                    "omitted here and flagged in the page notes for that type's next pass.",
            "prompt": """Polished commercial studio macro photography, extreme close range, razor sharp, high detail.

""" + G1 + """
The magnified region is a true region of the reference product: the cut edge of its foam core, same geometry, same material, same finish.

The foam's own structure fills about 80% of the frame, the open cells individually resolved across the whole face, each wall catching a soft matte sheen rather than a gloss, the surface reading as dense rather than airy.

Caught mid-work: a hand presses into the foam at the left of the frame, the cells compressed flat under the fingers and standing open again a short distance behind the press, so the recovery is visible in the same frame as the load.

No glow, no rim light, no emblem, no colour-coded highlight anywhere. The material carries the argument bare.

No text, no numbers, no logo, no watermark, no badge.""",
        },
    ],
})

SLOTS.append({
    "slot_id": "content.items.4.image",
    "role": "how-to-use",
    "ratio": "16:9",
    "asset": "122-06-content4-use-grid.png",
    "placement": "Beside the everyday-versatility beat: carried between car and desk, and the honest caveats.",
    "recommended": "A",
    "rationale":
        "`multi_step_usage: false` is the gate that decides this slot: it drops "
        "`03-use-sequence`, which leaves `03-use-grid` as the preferred how-to-use type, and "
        "the gate is right — the brief's setup is unbox, let it expand, place it, sit. There "
        "is no sequence to teach. The cell variable is `compatibility`, not `applications`, "
        "because what the section argues is the list of HOSTS: car seat, office chair, "
        "wheelchair, dining chair. THE PERSONA BOUNDARY, which this type names itself: if WHO "
        "is using it changed per cell the image would be `05-persona-grid`, so the people "
        "here are absent or anonymous limbs and only the seat changes. C is that other "
        "reading, offered deliberately.",
    "gif": {"eligible": True, "form": "whole-frame", "kind": "use", "type_id": "use",
            "rung": "natural",
            "reason": "The argument IS temporal here and the still cannot hold it: carrying "
                      "one piece from a van seat to a desk chair is a transition, and "
                      "`registry/gif-types/use.md` takes exactly that — one product, several "
                      "hosts, one message that it moves.",
            "brief": "Three seconds, one continuous handheld take: the cushion is lifted off "
                     "the van seat, carried across a driveway at hip height, and set onto a "
                     "desk chair, which the shot ends on. One pair of hands, no cuts, no text."},
    "options": [
        {
            "type": "03-use-grid", "variant": None,
            "axes": {},
            "varies_on": "baseline",
            "gloss": "Three seats, three cameras, one cushion: the van, the desk chair and a "
                     "hard dining chair, fitted in each.",
            "note": "Needs the product photo. The camera is named per cell, which is this "
                    "type's own fix for a grid that reads as one template repeated.",
            "prompt": """Photographic grid of three equal cells, thin white gutters, no outer border. No numbers, no arrows, no badges, no text anywhere.

""" + G1 + """
Preserve its shape, proportions, material, finish and colour exactly in every cell, and show it visibly fitted to the seat in each one. Show the black colourway.

Each cell shows a different seat the cushion serves, staged in that seat's own place, with a different camera:

Left cell: the driver's seat of a working van, photographed low and close from the open door in early morning light, the door sill and the pedals in shot.

Middle cell: a home-office desk chair, photographed level and further back from across the desk in daylight from a window, the desk edge, a keyboard and a mug in shot.

Right cell: a hard wooden dining chair at a kitchen table, photographed from above and near under a warm ceiling light, the table top and a folded newspaper in shot.

Nobody's face appears in any cell; where a person is present they are only a hand or a forearm setting the cushion in place.

All three cells share one photographic register: the same lens character, the same contrast, the same honest daylight treatment.""",
        },
        {
            "type": "06-relief-hero", "variant": "--commercial",
            "axes": {"register": "commercial", "inset_mode": "none"},
            "varies_on": "type: 06-relief-hero",
            "gloss": "One room instead of three cells: the desk chair at the end of the "
                     "working day, the cushion in place, the man working on without thinking "
                     "about it.",
            "note": "Needs the product photo. RECOMMENDED at the hero, so picking it here "
                    "spends one type twice in the shipped set.",
            "prompt": """Commercial lifestyle photograph. One frame, no panels, no insets.

""" + G1 + """
Render it at 25% of the frame height, integrated with the scene lighting, on the desk chair under him and behind him as one piece, the joint where the seat meets the chair back. Show the black colourway.

A man in his late forties in a creased work shirt sits at his home-office desk in the late afternoon, one hand on the mouse and the other resting on the desk, shoulders down, looking at the monitor rather than at anything in the room. He is relaxed and unhurried.

His back is against the cushion's upright section along its whole length, and his hips sit level with his knees.

Setting: the corner of a home office filled to the edges with the things that live there — a mug, a notebook, a small plant, a desk lamp, a coiled charger, a jacket over the back of a second chair. None of them carries printed words.

Light: real daylight from the window on the left, soft, no rim light.
Grade: bright, high-key, neutral, true to life.""",
        },
        {
            "type": "05-persona-grid", "variant": "--2x2",
            "axes": {},
            "varies_on": "type: 05-persona-grid",
            "gloss": "The same breadth read as people rather than seats: four buyers the "
                     "brief names, each in their own place and their own light.",
            "note": "Needs the product photo. This is the persona reading of the section; if "
                    "it is picked, the how-to-use beat becomes a casting shot and the seats "
                    "stop being the variable.",
            "prompt": """Clean lifestyle collage for e-commerce, bright, airy, sharp. Four equal cells, thin white gutters, no outer border, no graphic overlay of any kind.

""" + G1 + """
The cushion is visible and unobstructed in every cell, in the black colourway, and every cell shares one photographic finish: the same lens character, the same contrast, the same skin rendering.

Top left: a man in his fifties in a delivery driver's fleece, at the wheel of his van in a loading yard, one hand on the gear lever, looking out of the side window. Flat grey overcast light, cool blue-grey palette.

Top right: a woman in her late thirties in a cardigan at a home-office desk, leaning back with a pen in her hand, reading something off the screen. Warm afternoon daylight through a window, honey and oatmeal palette.

Bottom left: a man in his twenties in a t-shirt in a gaming chair at night, controller in both hands, leaning into the game. Cool magenta and blue screen light, dark room.

Bottom right: a woman in her sixties in a wheelchair at a kitchen table, both hands around a mug, turned toward someone off-frame. Bright even kitchen light, warm neutral palette.

No two cells share a palette, a light or a posture.""",
        },
    ],
})

SLOTS.append({
    "slot_id": "content.items.5.image",
    "role": "outcome",
    "ratio": "16:9",
    "asset": "122-07-content5-relief-scene.png",
    "placement": "Beside the reclaimed-life beat, two weeks after the cushion arrived.",
    "recommended": "A",
    "rationale":
        "`06-relief-scene` carries `requires_pair: 01-pain-scene`, and this page satisfies it: "
        "the pain frame is recommended at content.items.0 with the same man. That pairing is "
        "the reason A can ship at all, and it is the cross-slot rule this session came "
        "closest to breaking — had the hero kept the pain frame and this slot taken a relief "
        "scene, the pair would still hold, but the page would carry two pain frames and one "
        "type twice. THE TYPE'S OWN RULE decided the place: relief-scene is never set at "
        "home, so the reclaimed moment is the supermarket car park rather than the driveway "
        "the copy names, and the product sits in the scene as the reason rather than being "
        "presented. GAZE never finds the lens; that is a gate failure in this type, not a "
        "preference.",
    "gif": {"eligible": True, "form": "whole-frame", "kind": "relief", "type_id": "relief",
            "rung": "natural",
            "reason": "The claim is a stride that no longer needs bracing, which is a state "
                      "change a loop can hold: `registry/gif-types/relief.md` asks for the "
                      "after-state living rather than posed, and the still is one moment of "
                      "exactly that.",
            "brief": "Three seconds, one handheld take at walking height: he crosses the frame "
                     "mid-stride with the crate under one arm, his back straight and his free "
                     "arm swinging, the car park and the open van door holding still behind "
                     "him. No cut, no text, nothing drawn on the frame."},
    "options": [
        {
            "type": "06-relief-scene", "variant": None,
            "axes": {"gaze": "candid"},
            "varies_on": "baseline",
            "gloss": "Mid-stride across a supermarket car park with a crate under one arm, "
                     "nothing braced, the van door open behind him with the cushion still on "
                     "the seat.",
            "note": "Needs the product photo. The product is in the scene as the reason, not "
                    "presented: it stays on the seat behind him and is not held, pointed at "
                    "or centred.",
            "prompt": """Candid documentary photograph, single frame. Natural, unposed, sharp, as a passer-by could have taken it.

""" + G1 + """
Render it at 12% of the frame height, integrated with the scene lighting, on the driver's seat of the van behind him, seen through the open door, its seat section and upright section both in view. Show the black colourway.

The same man in his late forties, in put-together but ordinary clothes from the same palette as before, crosses a supermarket car park mid-stride with a crate of shopping under one arm and his van keys in the other hand. His back is straight, his free arm swings, and nothing about him is braced or careful. He is absorbed in his own errand and looks toward the trolley bay rather than at the camera.

Around him: two or three blurred shoppers further off, trolleys in a bay, painted bay lines, an ordinary overcast afternoon.

Light: even natural daylight, bright, soft shadows. No golden hour, no rim light.
Grade: a natural palette with light film grain and shallow depth of field — honest rather than glossy, and never drained.

No mark of any kind anywhere in the frame.""",
        },
        {
            "type": "06-relief-hero", "variant": "--commercial",
            "axes": {"register": "commercial", "inset_mode": "none"},
            "varies_on": "type: 06-relief-hero",
            "gloss": "The outcome as a controlled frame: back at his own kitchen table after "
                     "the drive, upright and unhurried, the cushion on the chair.",
            "note": "Needs the product photo. RECOMMENDED at the hero. Picking it here spends "
                    "the type twice, and it also moves the outcome indoors, which is the "
                    "distinction `06-relief-scene` exists to hold.",
            "prompt": """Commercial lifestyle photograph. One frame, no panels, no insets.

""" + G1 + """
Render it at 25% of the frame height, integrated with the scene lighting, on the kitchen chair under him and behind him as one piece, the joint where the seat meets the chair back. Show the black colourway.

A man in his late forties in a creased work shirt sits at his kitchen table in the early evening, leaning back with a mug in one hand, the other resting on the table, shoulders down, turned toward his daughter across the table rather than toward the camera. He is relaxed and unhurried.

His back is against the cushion's upright section along its whole length, and his hips sit level with his knees.

Setting: an ordinary kitchen filled to the edges with the things that live there — a fruit bowl, a tea towel over the oven rail, a jar of utensils, two plates, a school bag on a chair. None of them carries printed words.

Light: real daylight through the window on the left, soft, no rim light.
Grade: bright, high-key, neutral, true to life.""",
        },
        {
            "type": "05-social-snapshot", "variant": None,
            "axes": {"register": "ugc"},
            "varies_on": "type: 05-social-snapshot",
            "gloss": "The outcome as the owner's own phone photo: the cushion on the van seat "
                     "at the end of a shift, the crate already loaded.",
            "note": "Needs the product photo. RECOMMENDED four times over in the review wall "
                    "below; at this slot it argues ownership rather than outcome, which is "
                    "the weaker reading of the section.",
            "prompt": """A real customer's phone photo. One frame, no layout, no layers.

""" + G1 + """
Render it at 45% of the frame height, exactly as the reference shows, sitting on the driver's seat where it lives. Show the black colourway.

The product simply where it now lives: on the driver's seat of a working van at the end of a shift, the door open, the seat as it is — a crumb or two in the seam, the seat belt buckle lying across the base, nothing tidied and nothing added.

One incidental owner object in the frame: a coiled phone charger looped over the gear lever.

Ambient light only: late afternoon daylight coming in through the open door, no studio light, exposure honest to the cab.

The camera is a phone held in one hand: framing slightly tilted and a little too close, focus adequate but casual, mild noise acceptable. No negative space, no rule of thirds.

Nobody's face is in the frame, and nothing is written, printed or drawn anywhere on the image.""",
        },
    ],
})

SLOTS.append({
    "slot_id": "content.items.6.image",
    "role": "comparison",
    "ratio": "16:9",
    "asset": "122-08-content6-spec-split.png",
    "placement": "Beside the cost comparison against chairs, re-upholstery and per-session care.",
    "recommended": "A",
    "rationale":
        "The section argues price against every other route, and no type in this library "
        "prints a figure — A15 is absolute — so the image argues the ENGINEERING the price "
        "buys instead: an expensive mechanism on one side of the diagonal, one moulded piece "
        "on the other. `04-proof-lockedframe --verdict` is the role's first preference and is "
        "offered as B, but the type is already recommended at content.items.1 and one-type-"
        "once binds the shipped set, so it is B rather than A. FAIRNESS, which `--verdict` "
        "makes a rule: if B is picked, the two alternatives must look like things a "
        "reasonable person buys, because a comparison won by styling is worth nothing. C "
        "cannot ship beside the recommended pain frame.",
    "gif": {"eligible": False, "form": "none",
            "reason": "A cost argument is read, not watched: what changes between the halves "
                      "is what the buyer pays, and money has no state to animate. Nothing in "
                      "the frame moves under the product's action."},
    "options": [
        {
            "type": "03-spec-split", "variant": None,
            "axes": {},
            "varies_on": "baseline",
            "gloss": "The expensive route against the cheap one, in one diagonal: a chair's "
                     "articulated lumbar mechanism photographed on the left, the single "
                     "moulded core rendered on the right.",
            "note": "Needs the product photo, for the inset only. The left half is a generic "
                    "unbranded mechanism — a claim about a category, never about a competitor.",
            "prompt": """High-contrast technical comparison graphic, e-commerce, sharp.

""" + G1 + """
Render it at 22% of the frame width, complete and whole, alone on a plain ground inside a rounded rectangle along the bottom of the frame, clear of every frame edge. Show the black colourway.

One diagonal runs from the lower left corner of the frame to the upper right corner, the upper right half advancing into the lower left.

Lower left half, photographed in a dim unstyled room, desaturated: the back of a generic unbranded office chair with its lumbar support mechanism exposed — a moulded plastic carrier, a tension knob, a steel bracket and an adjuster rail, screw heads and seams visible, grey dust settled in the joints.

Upper right half, a 3D render against a dark gradient with cool rim lighting: one moulded foam core with no fasteners, no brackets and no adjusters, its seat section rising into an upright back section, the light running unbroken along the curve where they meet.

A thin glowing line runs along the diagonal, with a burst of warm sparks where it crosses the centre of the frame.

In the lower left half a flat solid red disc with a cross cut out of it; in the upper right half a flat solid green disc with a check mark cut out of it, both the same diameter.""",
        },
        {
            "type": "04-proof-lockedframe", "variant": "--verdict",
            "axes": {"camera_lock": "strict"},
            "varies_on": "type: 04-proof-lockedframe",
            "gloss": "Three objects on one bench under one camera, the cushion last: the "
                     "chair pad, the wedge and the one-piece cushion.",
            "note": "Needs the product photo. RECOMMENDED at content.items.1 in its "
                    "`--rivals` form, and variants do not lift one-type-once, so picking B "
                    "here means that slot takes its own option B or C.",
            "prompt": """Honest documentary product test photography, unstyled, natural, sharp. Three equal vertical panels packed across the frame with thin white gutters, no outer border.

""" + G1 + """
Render it in the right panel only, standing on the bench exactly as the reference shows, its seat section flat and its back section upright. Show the black colourway.

One camera for all three panels, stated once: a level view from one metre onto the same workshop bench, the same framing and the same distance in each, the bench edge along the bottom of every panel and the same window behind. One daylight exposure and one white balance throughout.

The only thing that changes between the panels is the object on the bench:
left panel, a generic unbranded contoured chair pad;
middle panel, a generic unbranded foam lumbar wedge;
right panel, the cushion.

All three are photographed with exactly the same respect: the same exposure, the same tidy bench, the same generous framing. Nothing is lit, cropped or graded to favour the last panel, and the only difference a viewer can see is in the objects themselves.

Grade: one neutral grade across all three panels.""",
        },
        {
            "type": "01-pain-split", "variant": "--object",
            "axes": {},
            "varies_on": "type: 01-pain-split",
            "gloss": "The cheap route against the expensive one as a body argument: the same "
                     "man in a premium chair he still braces in, and in his own seat with the "
                     "cushion.",
            "note": "CANNOT SHIP BESIDE `01-pain-scene`, recommended at content.items.0 — the "
                    "two are `never_with`. Needs the product photo. This is the third variant "
                    "of this type offered on the page and at most one of them can ship.",
            "prompt": """E-commerce comparison tile, high contrast, sharp. Two panels, a hard vertical split at 50/50, each panel running to the frame edge. No border of any kind.

""" + G1 + """
Render it at 30% of the panel height, integrated with the scene lighting, in the right panel only: on the desk chair under him and behind him as one piece, the joint where the seat meets the chair back. Show the black colourway.

The same man in both panels, named once: late forties, short grey-flecked hair, clean-shaven, a creased blue work shirt, at the same home-office desk seen from the side at seat height, filling the same share of each panel, in the same daylight from the window on the left.

Left panel, desaturated to grey: he sits in an expensive-looking mesh office chair with an adjustable lumbar carrier behind him, and is still braced — perched forward off the back rest, one hand pushing down on the desk, his pelvis rolled back under him.

Right panel, full colour: the same man in his own plain chair with the cushion, sitting back against its upright section, both forearms easy on the desk, hips level with his knees.

A soft red glow sits on the base of his spine in the left panel and nowhere else in the frame.

In the top-left corner a flat solid red disc with a cross cut out of it; in the top-right corner a flat solid green disc with a check mark cut out of it, both the same diameter.

The right panel is brighter and airier than the left, by light and calm, with the room unchanged.""",
        },
    ],
})

REVIEW_WALL_RATIONALE = (
    "The four review tiles are a REPEATING SECTION, so cross-rule 2's exception applies and "
    "`05-social-snapshot` may serve every one of them — provided the instances differ on a "
    "named dimension, which is also that type's own SET DIVERSITY LAW: every tile takes a "
    "different room class, surface, light temperature, camera distance and content mode. "
    "G14 IS THE THING TO READ HERE. The test is attribution, not proximity (ADR-088): the "
    "tiles carry no name, avatar, star row or verified label, and named badged reviews "
    "sharing the block do not attribute them. What does attribute them is this page's own "
    "description of the block — `content.json` calls these 'four customer photo tiles' — so "
    "the slot ships FLAGGED rather than refused (ADR-089), and the merchant chooses between "
    "the prompt and a real customer photograph. B is the same tile with a person in it; C is "
    "the casting reading and is weakest at tile size, where four cells are small."
)
G14_FLAG = {
    "flag": "origin-claim-lead",
    "note": "content.json, section `reviews`, copy_summary: 'Four customer photo tiles sitting "
            "in the same section element as three named quotes, each carrying a Verified "
            "Purchase label.' The page's own description claims customer origin for the tiles, "
            "which attributes them under ADR-088. The frame carries no name, badge or star row "
            "and cannot: G6 keeps all of it out of the image. If the wall's lead on the live "
            "page does not claim the photos came from customers, the flag lifts.",
}

WALL = [
    ("reviews.shots.0.image", "122-09-review0-snapshot.png",
     "First review tile, beside the desk-worker quote.",
     "at-rest", "a home office in the evening",
     """The product simply where it now lives: on the desk chair of a small home office in the evening, the room as it is — a cardigan over the chair arm, a charging cable trailing off the desk, nothing tidied and nothing added.

One incidental owner object in the frame: a half-full mug on the desk beside the chair.

Ambient light only: the warm overhead light of the room, no studio light, exposure honest to the room.

The camera is a phone held in one hand from about a metre away: framing slightly off-centre, focus adequate but casual, mild noise acceptable.""",
     "a woman in her late thirties in a cardigan, home office, warm evening light",
     """A woman in her late thirties in a cardigan sits back at her home-office desk in the evening, one hand still on the mouse, looking at the screen rather than at the camera. She is relaxed, and her back is against the cushion's upright section along its whole length.

Setting: the corner of a home office exactly as it is — a mug, a notebook, a desk lamp, a cardigan over the chair arm, a coiled cable, a small plant. None of them carries printed words.

Light: the room's own warm overhead light, mildly overexposed on her face and the lamp, no rim light.""",
     [("a woman in her late thirties at a home-office desk in the evening, warm lamplight, leaning back with a pen in her hand",
       "a man in his fifties in a delivery driver's fleece at the wheel of his van in a loading yard, flat overcast light, one hand on the gear lever"),
      ("a man in his twenties in a gaming chair at night, cool screen light, controller in both hands",
       "a woman in her sixties in a wheelchair at a kitchen table in bright daylight, both hands around a mug")]),
    ("reviews.shots.1.image", "122-10-review1-snapshot.png",
     "Second review tile, beside the van-driver quote.",
     "in-use", "a working van at first light",
     """The product mid-use by its owner, the person present only incidentally: on the driver's seat of a working van at first light, a forearm in a fleece sleeve reaching across to the ignition, the seat belt already drawn over the cushion's upright section.

One incidental owner object in the frame: a coiled phone charger looped over the gear lever.

Ambient light only: cold early daylight through the windscreen, the cab still dim, exposure honest to it.

The camera is a phone held close in one hand: framing tilted and a little too close, focus adequate but casual, mild motion softness acceptable.""",
     "a man in his fifties in a fleece, van cab, cold early daylight",
     """A man in his fifties in a delivery driver's fleece sits at the wheel of his van at first light, both hands loose on the wheel, looking out through the windscreen rather than at the camera. He is relaxed, and his back is against the cushion's upright section along its whole length.

Setting: the cab exactly as it is — a lanyard on the indicator stalk, a flask in the door bin, a clipboard on the passenger seat, a hi-vis over the headrest. None of them carries printed words.

Light: cold early daylight through the windscreen, mildly overexposed on the glass, no rim light.""",
     [("a man in his fifties in a fleece at the wheel of a van at first light, cold daylight, one hand on the gear lever",
       "a woman in her forties in scrubs at a reception desk under flat ceiling light, writing on a pad"),
      ("a man in his thirties at a workshop bench on a hard stool, warm task light, leaning over a repair",
       "a student in a hoodie at a library desk, cool daylight from high windows, reading")]),
    ("reviews.shots.2.image", "122-11-review2-snapshot.png",
     "Third review tile, beside the long-evening quote.",
     "in-use", "a bedroom gaming chair at night",
     """The product mid-use by its owner, the person present only incidentally: on a gaming chair in a bedroom at night, two fingers pushing the cushion's upright section back against the chair's own backrest, a knee and a tracksuit leg at the edge of frame.

One incidental owner object in the frame: a controller lying on the carpet beside the chair base.

Ambient light only: the cool light of a screen off-frame and a warm lamp behind, no studio light, exposure honest to the dark room.

The camera is a phone held close in one hand: framing tilted, focus adequate but casual, mild noise in the shadows.""",
     "a man in his twenties in a t-shirt, bedroom gaming chair, screen light at night",
     """A man in his twenties in a t-shirt sits back in a gaming chair in his bedroom at night, a controller loose in both hands, watching a screen off-frame rather than the camera. He is relaxed, and his back is against the cushion's upright section along its whole length.

Setting: the room exactly as it is — a desk with a mug and a headset, a laundry pile on a chair, a cable loom down the wall, a poster frame turned away. None of them carries printed words.

Light: cool screen light from off-frame and a warm lamp behind, mildly overexposed on his face and arms, no rim light.""",
     [("a man in his twenties in a t-shirt in a gaming chair at night, cool screen light, controller in both hands",
       "a woman in her thirties in a tracksuit at a kitchen table in the morning, flat daylight, laptop open"),
      ("a man in his sixties in a cardigan in an armchair in the evening, warm lamplight, newspaper folded on his knee",
       "a woman in her forties in work clothes on a hard stool at a reception counter, flat ceiling light")]),
    ("reviews.shots.3.image", "122-12-review3-snapshot.png",
     "Fourth review tile, beside the dining-chair quote.",
     "at-rest", "a kitchen in daylight",
     """The product simply where it now lives: on a hard wooden dining chair in a kitchen in the middle of the day, the chair pushed back a little from the table, the room as it is — a chopping board still out, a tea towel over the chair back, nothing tidied and nothing added.

One incidental owner object in the frame: a folded newspaper on the table edge, its print not legible.

Ambient light only: flat daylight from the window, no studio light, exposure honest to the room.

The camera is a phone held at standing height, further back than the other shots: framing off-centre, the chair small in the frame, focus adequate but casual.""",
     "a woman in her sixties, kitchen dining chair, bright daylight",
     """A woman in her sixties in a blouse sits at her kitchen table in the middle of the day, both hands around a mug, turned toward someone off-frame rather than toward the camera. She is relaxed, and her back is against the cushion's upright section along its whole length.

Setting: the kitchen exactly as it is — a chopping board still out, a fruit bowl, a tea towel over the oven rail, a calendar turned to the wall. None of them carries printed words.

Light: flat daylight from the window, mildly overexposed on the window wall, no rim light.""",
     [("a woman in her sixties in a blouse at a kitchen table in daylight, both hands around a mug",
       "a man in his forties in a polo shirt on a hard dining chair doing paperwork, warm ceiling light"),
      ("a woman in her seventies in a wheelchair by a window in the afternoon, soft daylight, knitting in her lap",
       "a man in his fifties on a folding chair at a camping table, flat outdoor light, mug in hand")]),
]


def wall_slot(slot_id, asset, placement, mode, where, snap_body, ugc_gloss, ugc_body, personas):
    cells = [f"{a}\n\n{b}" for a, b in personas]
    return {
        "slot_id": slot_id, "role": "social-proof", "ratio": "1:1", "asset": asset,
        "placement": placement, "recommended": "A", "rationale": REVIEW_WALL_RATIONALE,
        "compliance": G14_FLAG,
        "gif": {"eligible": False, "form": "none",
                "reason": "A customer snapshot argues that the thing exists in a real home, "
                          "which is a held state. This type bans every added element and a "
                          "loop would have to animate a still room."},
        "options": [
            {
                "type": "05-social-snapshot", "variant": None,
                "axes": {"register": "ugc"},
                "varies_on": "baseline",
                "gloss": f"The cushion {mode.replace('-', ' ')} in {where}, photographed as found.",
                "note": "Needs the product photo. Mode is resolved by the writer and never "
                        "reaches the model. The tile carries no name, badge, star row or "
                        "timestamp, and cannot — the page is what attributes it, which is "
                        "why this slot ships flagged.",
                "prompt": "A real customer's phone photo. One frame, no layout, no layers.\n\n"
                          + G1 + "\nRender it at 45% of the frame height, exactly as the "
                          "reference shows. Show the black colourway.\n\n" + snap_body +
                          "\n\nNobody's face is in the frame, and nothing is written, printed "
                          "or drawn anywhere on the image.",
            },
            {
                "type": "06-relief-hero", "variant": "--ugc",
                "axes": {"register": "ugc", "inset_mode": "none"},
                "varies_on": "type: 06-relief-hero",
                "gloss": f"The same tile with its owner in it: {ugc_gloss}.",
                "note": "Needs the product photo. RECOMMENDED at the hero in its commercial "
                        "register; the ugc register is a different frame but the same type, "
                        "so picking it here spends the type twice.",
                "prompt": "A phone photo taken by an ordinary person in their own room. One "
                          "frame, no panels, no insets.\n\n" + G1 +
                          "\nRender it at 25% of the frame height, integrated with the room's "
                          "own light, on the seat under them and behind them as one piece, "
                          "the joint where the seat meets the seat back. Show the black "
                          "colourway.\n\n" + ugc_body +
                          "\n\nThe framing is casual and a little too close, with no negative "
                          "space and no styling. Nothing in the frame is written, printed or "
                          "drawn.",
            },
            {
                "type": "05-persona-grid", "variant": "--2x2",
                "axes": {},
                "varies_on": "type: 05-persona-grid",
                "gloss": "The wall's job read as casting: four buyers in four places, one "
                         "colourway and one photographic finish.",
                "note": "Needs the product photo. Weakest of the three at tile size — four "
                        "cells inside one square tile — and only one tile on the wall could "
                        "carry it before the wall stops reading as four customers.",
                "prompt": """Clean lifestyle collage for e-commerce, bright, airy, sharp. Four equal cells, thin white gutters, no outer border, no graphic overlay of any kind.

""" + G1 + """
The cushion is visible and unobstructed in every cell, in the black colourway, and every cell shares one photographic finish: the same lens character, the same contrast, the same skin rendering.

Top left: """ + cells[0].split("\n\n")[0] + """.

Top right: """ + cells[0].split("\n\n")[1] + """.

Bottom left: """ + cells[1].split("\n\n")[0] + """.

Bottom right: """ + cells[1].split("\n\n")[1] + """.

No two cells share a palette, a light or a posture.""",
            },
        ],
    }


for args in WALL:
    SLOTS.append(wall_slot(*args))

# --- MORE SLOTS GO HERE ---

OUT_OF_SCOPE = [
    ("product.image", "cta", "The mid-page product card: a standard product shot, out of library scope (`mapping/slot-rules.md` cross-rule 6 and the `cta` row)."),
    ("product_end.image", "cta", "The closing product card, same reason."),
    ("hero.author_avatar", "author", "A byline portrait of a named person. No library type produces one, and generating a face under a real byline is a disclosure decision (`mapping/slot-rules.md`, the `author` row)."),
    ("guide.avatar", "author", "The About-the-author portrait, same reason."),
    ("comments.items.0.avatar", "social-proof", "A commenter portrait, 1 of 6. Same reason as the byline: a named person's face."),
    ("comments.items.1.avatar", "social-proof", "Commenter portrait, 2 of 6."),
    ("comments.items.2.avatar", "social-proof", "Commenter portrait, 3 of 6."),
    ("comments.items.3.avatar", "social-proof", "Commenter portrait, 4 of 6."),
    ("comments.items.4.avatar", "social-proof", "Commenter portrait, 5 of 6."),
    ("comments.items.5.avatar", "social-proof", "Commenter portrait, 6 of 6."),
    ("header.logo", "cta", "The brand logo, already supplied in the export as inline SVG."),
    ("footer.logo", "cta", "The brand logo, already supplied in the export as inline SVG."),
]

PAGE_NOTES = [
    "lpTypeId is `advertorial` and selects LP1's folder (SPEC 3.0, ADR-091), so this page "
    "routes `registry/index.yaml` + `mapping/slot-rules.md` and never opens "
    "`registry/pdp-dr-types/`. Awareness is solution-aware, taken from the brief's own field.",

    "ONE-TYPE-ONCE IS THE CHANGE FROM v06. That session recommended `01-pain-scene` at the "
    "hero AND at content.items.0, which spends one type twice in the shipped set. Here the "
    "pain frame goes to the section whose copy is the pain beat, the hero takes "
    "`06-relief-hero`, and every other recommended type appears exactly once. The review wall "
    "is the sanctioned exception: it is a repeating section, so `05-social-snapshot` serves "
    "all four tiles and the tiles differ on named dimensions.",

    "`01-pain-split` is offered three times — `--mirror` at content.items.0, `--oldway` at "
    "content.items.1 and `--object` at content.items.6 — and AT MOST ONE can ship, only if the "
    "recommended `01-pain-scene` is dropped: the two types are `never_with` in the index. The "
    "three variants are there so the choice is between three real frames rather than one.",

    "`06-relief-scene` carries `requires_pair: 01-pain-scene`, and the recommended set "
    "satisfies it at content.items.0 with the same man in the same wardrobe family. Picking "
    "option B or C at content.items.0 breaks the pair and the outcome slot then takes its own "
    "option B.",

    "NO FIGURE ENTERS ANY FRAME (A15). The brief supplies several — 97% of support retained "
    "after 50,000 compression cycles, 14.7 years of daily use, up to half off, a 90-day "
    "guarantee — and none of them is written into an image, because nothing in a frame can "
    "substantiate a number. They belong in page copy beside their source.",

    "THE REVIEW WALL SHIPS FLAGGED, NOT REFUSED (ADR-088, ADR-089). The tiles carry no name, "
    "avatar, star row or verified label; what attributes them is the page's own description "
    "of the block, and the flag names the sentence. The merchant chooses between the prompt "
    "and a real customer photograph.",

    "A STYLE LOCK IS DECLARED FOR THE SESSION, and on an LP1 page that is a house choice "
    "rather than law: ADR-093's lock binds LP2 galleries. It is worth keeping here for the "
    "same reason — one man, two places, one colourway, one accent — so twelve frames read as "
    "one page rather than twelve stock pictures.",

    "TYPES THE POOL HELD AND THE PAGE DID NOT USE, with the reason each time: "
    "`03-use-sequence` is gated out by `multi_step_usage: false`; `03-mechanism-xray` has "
    "nothing to look through — a foam core with a fabric cover is the trivial interior that "
    "type's own gate refuses; `05-social-handoff` needs a RESULT visible on one continuous "
    "surface, and a posture is not one.",

    "A FINDING FOR `03-spec-macro`'s NEXT PASS, not fixed here: its SKELETON still carries a "
    "`RATIO: [1:1]` line. ADR-016 and adapter Rule 4 keep a ratio out of prompt text, and "
    "ADR-082 removed `ratios` from every type's frontmatter, so the line is stale template "
    "rather than law. The prompt at content.items.3 option C omits it.",

    "EVERY PROMPT IS PASTE-AND-RUN: one prompt, one generation call, and one reference photo "
    "where the type needs one (ADR-021, ADR-076). `product.reference_photos` is empty in this "
    "content.json, so `attachments` is empty everywhere and the prompts say to attach a photo "
    "of the black cushion — an empty attachments array is not a blocked prompt "
    "(`query/runbook.md` Step 5).",

    "TYPE VERSIONS ARE READ FROM THE COMMITTED FILES. Another lane holds uncommitted edits to "
    "`03-mechanism-ghostbody` (2.4) and `03-mechanism-xray` (1.5); this session cites 2.3 and "
    "does not read the working tree, so every version it names is one git can show.",
]

COVERAGE = {
    "covered": [
        "rung 1, pain — 01-pain-scene at content.items.0, the kitchen table",
        "rung 2, cause — 02-cause-anatomy --diagnostic at content.items.2, the pelvic drop",
        "rung 3, mechanism — 03-mechanism-ghostbody at content.items.3, and the spec reading "
        "of the same feature at content.items.6 with 03-spec-split",
        "rung 4, proof — 04-proof-lockedframe --rivals at content.items.1",
        "rung 5, social — 05-social-snapshot across the four review tiles",
        "rung 6, relief — 06-relief-hero at the hero and 06-relief-scene at content.items.5",
    ],
    "absent": [
        "No rung is absent. The ladder is covered end to end, which is what a first-person "
        "advertorial with eight linear sections has room for.",
    ],
    "recommended_additions": [
        "None. The page's own sections already carry every rung, so an additive proposal would "
        "be a slot the page does not have.",
    ],
}

MOTION = {
    "floor": 2, "ceiling": 5, "delivered": 3, "margin": 1,
    "groups_covered": ["working", "result"],
    "shortfall_reason": None,
    "briefs": [
        {"slot_id": "content.items.2.image", "type_id": "cause", "group": "working"},
        {"slot_id": "content.items.4.image", "type_id": "use", "group": "working"},
        {"slot_id": "content.items.5.image", "type_id": "relief", "group": "result"},
    ],
    "note": "Three loops against a floor of two, both groups covered. The three negative "
            "verdicts are on the slots where the argument is inspected rather than watched — "
            "two panels, three panels and a diagonal — and each says so in its own reason.",
}


# ---------------------------------------------------------------- emit
def emit():
    versions = {o["type"]: type_version(o["type"]) for s in SLOTS for o in s["options"]}
    md, js = [], []
    n_prompts = sum(len(s["options"]) for s in SLOTS)
    briefs = sum(1 for s in SLOTS if s["gif"].get("eligible"))
    md.append(f"# Image prompts — page {PAGE_ID}, ergonomic memory foam seat cushion (v07)\n")
    md.append("GENERATED from this directory's `build.py`. Never hand-edit this file — edit the "
              "script and re-run. Routing rationale, the negative motion verdicts and the "
              "out-of-scope slots are all in `prompts.json`.\n")
    md.append(f"- page `{PAGE_ID}` · advertorial · solution-aware · {len(SLOTS)} routed slots · "
              f"{n_prompts} prompts · {briefs} motion brief(s)")
    md.append("- **The style lock for this session**, so twelve frames read as one page:")
    for k, v in STYLE_LOCK.items():
        md.append(f"  - `{k}` — {v}")
    md.append("")
    for s in SLOTS:
        md.append("---\n")
        md.append(f"## `{s['slot_id']}` — {s['role']}\n")
        md.append(f"- asset `{s['asset']}` · {s['placement']}")
        md.append(f"- recommended: **option {s['recommended']}**")
        if s.get("compliance"):
            md.append(f"- **compliance flag `{s['compliance']['flag']}`** — {s['compliance']['note']}")
        md.append(f"- {s['rationale']}\n")
        if s["gif"].get("eligible"):
            md.append(f"- **motion brief · gif type `{s['gif']['type_id']}`** — {s['gif']['brief']}\n")
        for letter, o in zip("ABC", s["options"]):
            v = f" `{o['variant']}`" if o.get("variant") else ""
            md.append(f"### `{s['slot_id']}` · option {letter} — `{o['type']}`{v}\n")
            md.append(f"- varies on: {o['varies_on']}")
            axes = ", ".join(f"`{k}: {v2}`" for k, v2 in (o.get("axes") or {}).items())
            md.append(f"- ratio `{s['ratio']}` · type version `{versions[o['type']]}`"
                      + (f" · {axes}" if axes else ""))
            md.append(f"- {o['gloss']}")
            md.append(f"- **note:** {o['note']}\n")
            md.append("```\n" + o["prompt"].strip() + "\n```\n")
        js.append({
            "slot_id": s["slot_id"], "role": s["role"], "ratio": s["ratio"],
            "asset": s["asset"], "placement": s["placement"],
            "recommended_option": s["recommended"], "recommendation_basis": s["rationale"],
            "compliance": s.get("compliance"), "gif": s["gif"],
            "options": [{
                "option": letter, "type": o["type"], "type_version": versions[o["type"]],
                "variant": o.get("variant"), "axes": o.get("axes") or {},
                "varies_on": o["varies_on"], "summary": o["gloss"],
                "composition_notes": o["note"], "prompt": o["prompt"].strip(),
                "attachments": [],
            } for letter, o in zip("ABC", s["options"])],
        })
    for slot_id, role, reason in OUT_OF_SCOPE:
        js.append({"slot_id": slot_id, "role": role, "out_of_scope_reason": reason})
    doc = {
        "page_id": PAGE_ID, "registry_version": "2.0.0", "channel": "advertorial",
        "lp_type_id": "advertorial", "awareness_stage": "solution-aware",
        "style_lock": STYLE_LOCK, "slots": js, "motion": MOTION, "coverage": COVERAGE,
        "recommended": [f"{s['slot_id']} -> option {s['recommended']}" for s in SLOTS],
        "page_composition_notes": PAGE_NOTES,
    }
    open(os.path.join(HERE, "prompts.md"), "w", encoding="utf-8").write("\n".join(md))
    json.dump(doc, open(os.path.join(HERE, "prompts.json"), "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    print(f"wrote prompts.md and prompts.json — {len(SLOTS)} routed slots, {n_prompts} prompts, "
          f"{len(OUT_OF_SCOPE)} out of scope")
    longest = max((len(o["prompt"]), s["slot_id"], letter)
                  for s in SLOTS for letter, o in zip("ABC", s["options"]))
    print(f"longest prompt: {longest[0]} chars at {longest[1]} option {longest[2]} "
          f"(adapter Rule 6 asks for a re-read past 2500)")


if __name__ == "__main__":
    emit()

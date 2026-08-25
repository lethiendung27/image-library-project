#!/usr/bin/env python3
"""Build prompts.json + prompts.md for page 193.

The JSON is the source of truth; the Markdown is generated from it (runbook Step 7).
Nothing here is hand-edited downstream. Every routing claim this file makes is
recomputed at the bottom and FAILS the build rather than warning: a routing that is
not checked is a routing that is trusted.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SESSION = os.path.basename(HERE)
PAGE = "193"

PAGE_TYPE, PRODUCT_SLUG, VERSION = "listicle", "arm-trainer-hydraulic", "v01"
assert SESSION == f"{PAGE_TYPE}-{PRODUCT_SLUG}-{VERSION}", \
    f"directory {SESSION} does not match the ADR-034 name"


def gif_name(slot_id):
    """ADR-051: the session's own name with the SLOT appended, dots to dashes.

    The gif type is NOT in it — it lives in gif.type_id and decides the library
    folder. The slot makes the name unique on the page by construction, which is
    why one-loop-per-gif-type is a preference here and no longer a rule.
    """
    return f"{PAGE_TYPE}-{PRODUCT_SLUG}-{VERSION}-{slot_id.replace('.', '-')}.mp4"


CONTRACT = json.load(open(os.path.join(HERE, "content.json"), encoding="utf-8"))
ATTRS = CONTRACT["product"]["attributes"]
DECLARED = {sl["slot_id"]: {"ratio": sl["ratio"], "role": sec["role"]}
            for sec in CONTRACT["page"]["sections"]
            for sl in sec["image_slots"]}

# ---------------------------------------------------------------------------
# Attribute gates (mapping/slot-rules.md), recomputed rather than asserted
# ---------------------------------------------------------------------------
GATES = [
    (lambda a: a["symptom_visibility"] == "invisible", "01-pain-split"),
    (lambda a: a["result_visibility"] == "invisible", "06-relief-scene"),
    (lambda a: not a["body_contact"], "03-mechanism-ghostbody"),
    (lambda a: not a["multi_step_usage"], "03-use-sequence"),
]
KILLED = sorted({t for c, t in GATES if c(ATTRS)})

# Ratios each type declares, intersected with ADR-016's five at check time.
TYPE_RATIOS = {
    "01-pain-scene": ["16:9", "3:4"],
    "02-cause-anatomy": ["5:3", "16:9", "1:1"],
    "03-mechanism-ghostbody": ["1:1", "4:5"],
    "03-mechanism-xray": ["1:1", "4:5", "16:9"],
    "03-use-sequence": ["3:4", "1:1"],
    "04-proof-lockedframe": ["5:3", "16:9", "1:1", "3:2"],
    "05-social-handoff": ["16:9", "1:1", "3:4"],
    "05-social-snapshot": ["4:3", "1:1", "3:4"],
    "06-relief-hero": ["16:9", "1:1"],
}
LEGAL_RATIOS = ["16:9", "4:3", "1:1", "3:4", "9:16"]          # ADR-016
TYPE_VERSION = {
    "01-pain-scene": "1.18", "02-cause-anatomy": "1.15",
    "03-mechanism-ghostbody": "2.3", "03-mechanism-xray": "1.3",
    "03-use-sequence": "1.9", "04-proof-lockedframe": "1.13",
    "05-social-handoff": "2.5", "05-social-snapshot": "1.2",
    "06-relief-hero": "1.17",
}
# Types whose EXECUTION here needs the owner's reference photo attached.
NO_PHOTO = {"01-pain-scene", "04-proof-lockedframe--rivals"}

CEIL = {"01-pain-scene": 2500, "02-cause-anatomy": 2050, "03-mechanism-ghostbody": 2400,
        "03-mechanism-xray": 2000, "03-use-sequence": 2200, "04-proof-lockedframe": 2600,
        "05-social-handoff": 2300, "05-social-snapshot": 1500, "06-relief-hero": 2600}

REF = ("Use the attached photo as the exact reference for the arm trainer. Preserve "
       "shape, proportions, material, finish and colour exactly. Do not redesign it, "
       "and add no part the reference does not have.")
AVOID = ("text, letters, numbers, watermark, logo, deformed hands, extra fingers, "
         "redesigned product, altered product shape, invented product details, "
         "different product than reference")

# ---------------------------------------------------------------------------
# 1 — content.0.image · hero · 01-pain-scene
# ---------------------------------------------------------------------------
OPEN_A = """TYPE: 01-pain-scene v1.18 --candid
REGISTER: editorial photojournalism, natural and unstaged. Single frame.

[SUBJECT]
Man in his late thirties in a washed-out t-shirt and jogging bottoms, on a living room rug at the top of a press-up, both arms locked straight and holding him there. Under that force: the elbows locked hard, both shoulders driven up around his ears, the weight stacked straight down through his wrists into the rug. Face: jaw slack, cheeks blown out, eyes down on the rug pile under his hands.

[EVIDENCE]
A row of mismatched dumbbells along the skirting board an arm's length from him: four different sizes in three different finishes, the smallest pair furred with dust, the heaviest pair still sitting in the open box it came in with the packing sunk in the middle.

[COST]
A gym holdall by the door, zip half open, a folded towel still inside it and dust settled along the shoulder strap. Sharp enough to read and never larger, nearer or brighter than the body it is being taken from.

[PLACE] A small first-floor living room, late evening.

[GAZE] Unaware of the camera, gaze down on the rug under his hands.

[LIGHT] The real light of the place and nothing added: one ceiling pendant on, and the last grey daylight through an uncurtained window behind him.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] An ordinary photograph in ordinary light. Normal exposure, detail held in both the shadows and the highlights, midtones open across most of the frame, colour true to life and muted rather than vivid.

STYLE: editorial photojournalism, natural and unstaged."""

OPEN_B = """TYPE: 01-pain-scene v1.18 --confront
REGISTER: editorial photojournalism, natural and unstaged. Single frame.

[SUBJECT]
Man in his late thirties in a washed-out t-shirt and jogging bottoms, sitting back on his heels on a living room rug between sets, both forearms hanging over his knees. Under that force: the shoulders dropped and rolled forward, both hands open and slack, his chest still working for breath. Face: mouth open on the breath, brows drawn in, colour high across the cheeks.

[EVIDENCE]
A row of mismatched dumbbells along the skirting board an arm's length from him: four different sizes in three different finishes, the smallest pair furred with dust, the heaviest pair still sitting in the open box it came in with the packing sunk in the middle.

[COST]
A gym holdall by the door, zip half open, a folded towel still inside it and dust settled along the shoulder strap. Sharp enough to read and never larger, nearer or brighter than the body it is being taken from.

[PLACE] A small first-floor living room, late evening.

[GAZE] Looking directly into the lens.

[LIGHT] The real light of the place and nothing added: one ceiling pendant on, and the last grey daylight through an uncurtained window behind him.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] An ordinary photograph in ordinary light. Normal exposure, detail held in both the shadows and the highlights, midtones open across most of the frame, colour true to life and muted rather than vivid.

STYLE: editorial photojournalism, natural and unstaged."""

OPEN_C = """TYPE: 01-pain-scene v1.18 --candid
REGISTER: editorial photojournalism, natural and unstaged. Single frame.

[SUBJECT]
Woman in her early forties in leggings and a loose vest, on a folded mat in the corner of a bedroom at the top of a press-up, both arms locked straight and holding her there. Under that force: the elbows locked hard, both shoulders driven up toward her ears, the weight stacked down through her wrists into the mat. Face: jaw slack, breath held, eyes down on the mat under her hands.

[EVIDENCE]
Two mismatched dumbbells on the carpet beside the mat, one a coated hex and one a chrome spinlock with a collar loose on the bar, and behind them a third bar with no collar at all and its plates stacked separately against the wardrobe door.

[COST]
A gym holdall shoved under the end of the bed, zip half open with a folded towel still inside it and dust settled along the shoulder strap. Sharp enough to read and never larger, nearer or brighter than the body it is being taken from.

[PLACE] The corner of a small bedroom, early morning.

[GAZE] Unaware of the camera, gaze down on the mat under her hands.

[LIGHT] The real light of the place and nothing added: flat overcast daylight through a net curtain, and a bedside lamp still on behind her.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] An ordinary photograph in ordinary light. Normal exposure, detail held in both the shadows and the highlights, midtones open across most of the frame, colour true to life and muted rather than vivid.

STYLE: editorial photojournalism, natural and unstaged."""

# ---------------------------------------------------------------------------
# 2 — content.1.items.0.image · mechanism · 03-mechanism-ghostbody
# ---------------------------------------------------------------------------
PLAT_A = """TYPE: 03-mechanism-ghostbody v2.3
REGISTER: 3D technical render on seamless white. NOT photography.

PRODUCT REFERENCE: """ + REF + """ It keeps its own reference colours and carries no mark of any kind.

PANELS: two equal panels side by side, divided by one thin vertical line. Both show the SAME featureless matte white mannequin in the SAME pose from the SAME angle: standing, seen from the front, both arms out in front of the chest at shoulder height and pressing inward, the chest and upper arm musculature open to view beneath the surface. The only difference between the panels is what the arms are pressing against and what the chest muscle does.

LEFT: the hands press against each other with nothing between them. The chest muscle is drawn thin and even along its whole length, unchanged from the resting form.
RIGHT: the reference arm trainer held between both hands at the same height, its grips taken by each hand and its arms compressed toward each other. The chest muscle is drawn thick and bunched along the same length, shortened and raised where it pulls.

CUTAWAY: the pectoral muscle and the front of the shoulder, inside the body silhouette, in both panels.

MARKS, three, nothing else in either panel is marked. Every one is a flat unshaded hard-edged overlay laid on top of the render, never a tint or fill of the anatomy:
- structure: the pectoral muscle and the front of the shoulder in warm off-white ivory, both panels.
- stress: RIGHT panel only. A flat blue band laid along the belly of the pectoral muscle where the load pulls it, following its line and clearly sitting on top of the render.
- verdict: one badge in the top corner of each panel — a red filled disc with a white cross in the LEFT, a green filled disc with a white check in the RIGHT. Same diameter, filled discs, not rings.

G3: red wrong, blue correct, green badge, nothing else.
Seamless white ground, soft even studio light, no shadow beyond a faint contact shadow."""

PLAT_B = """TYPE: 03-mechanism-ghostbody v2.3
REGISTER: 2D airbrushed medical illustration with soft gradients and modelled volume. NOT photography, NOT a 3D render.

PRODUCT REFERENCE: """ + REF + """ It keeps its own reference colours and carries no mark of any kind.

PANELS: two equal panels side by side, divided by one thin vertical line. Both show the SAME anonymous male torso and both arms in the SAME pose from the SAME angle: seen from the front, both arms out in front of the chest at shoulder height and pressing inward, the skin drawn translucent so the chest and upper arm muscles read through it. The only difference between the panels is what the arms press against and what the chest muscle does.

LEFT: the palms press flat against each other with nothing between them. The chest muscle lies long and slack, its fibres drawn evenly spaced from breastbone to shoulder.
RIGHT: the reference arm trainer held between both hands at the same height, its grips taken by each hand and its arms compressed toward each other. The same chest muscle is drawn shortened and thickened, its fibres crowded together toward the breastbone.

CUTAWAY: the pectoral muscle and the front of the shoulder, inside the body outline, in both panels.

MARKS, three, nothing else in either panel is marked:
- structure: the pectoral muscle and the front of the shoulder in warm ivory, both panels.
- stress: RIGHT panel only. A flat blue band laid along the belly of the pectoral muscle where the load pulls it, drawn on top of the illustration and following the muscle's own line.
- verdict: filled solid discs, red with a white cross in the LEFT panel's top corner, green with a white check in the RIGHT panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else.
Deep desaturated slate ground, the right half one step lighter than the left."""

PLAT_C = """TYPE: 03-mechanism-ghostbody v2.3
REGISTER: 3D technical render on seamless white. NOT photography.

PRODUCT REFERENCE: """ + REF + """ It keeps its own reference colours and carries no mark of any kind.

PANELS: two equal panels side by side, divided by one thin vertical line. Both show the SAME featureless matte white mannequin in the SAME pose from the SAME angle: seated upright on a plain block, seen from the side facing left, the near arm bent and driving forward from the shoulder, the upper arm and shoulder musculature open to view beneath the surface. The only difference between the panels is what the hand drives against and what the arm muscle does.

LEFT: the hand drives forward into open air with nothing in it. The upper arm muscle is drawn thin and even along its whole length, unchanged from the resting form.
RIGHT: the reference arm trainer held in that hand at the same height, its grip taken and its arm compressed forward. The same upper arm muscle is drawn thick and raised along the same length, gathered toward the shoulder where it pulls.

CUTAWAY: the upper arm muscle and the shoulder joint, inside the body silhouette, in both panels.

MARKS, three, nothing else in either panel is marked. Every one is a flat unshaded hard-edged overlay laid on top of the render:
- structure: the upper arm muscle and the shoulder joint in warm off-white ivory, both panels.
- stress: RIGHT panel only. A flat blue band laid along the belly of the upper arm muscle where the load pulls it, following its line and clearly on top of the render.
- verdict: one badge in the top corner of each panel — red filled disc with a white cross LEFT, green filled disc with a white check RIGHT. Same diameter, filled discs, not rings.

G3: red wrong, blue correct, green badge, nothing else.
Seamless white ground, soft even studio light, faint contact shadow only."""

# ---------------------------------------------------------------------------
# 3 — content.1.items.1.image · cause · 02-cause-anatomy
# ---------------------------------------------------------------------------
COIL_A = """TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, paper-cut. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the arm trainer in the RIGHT panel.

FRAME: one resistance bar held across the chest of an anonymous torso, from grip to grip, the bar filling most of the width and the torso small behind it.
GROUND: deep desaturated slate, the right half one step lighter than the left.
BODY: the resistance element inside the bar, cut as a separate paper layer over a translucent bar outline, seen from the side. NOT a skeleton, NOT a machine drawing. Exactly one bar in EACH panel, same scale and view.

PANELS. LEFT: a generic unbranded coil spring bar, its steel coil wound tight and compressed hard between the two grips, the coil pitch squeezed almost closed at the centre of the stroke. RIGHT: the reference arm trainer at the same point of the same stroke, its hydraulic cylinder drawn as a smooth sealed tube with the piston partway down it and clear fluid either side of the piston, the tube unchanged in length along its wall.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each running along the resistance element from one end to the other and STOPPING at both ends. Both sit at the same height in their panel, identical thickness and dash. One property differs: on the left the line is bowed and crowded where the coil is compressed, on the right it is straight and evenly spaced. Red left, blue right. Straight dashes, not boxes.
- verdict: filled solid discs, red with a white cross in the LEFT panel's TOP corner, green with a white check in the RIGHT panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else."""

COIL_B = """TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, flat-vector with flat fills and hard edges, no gradients. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the arm trainer in the RIGHT panel.

FRAME: one resistance bar seen end-on to the stroke, from grip to grip, the bar filling most of the width.
GROUND: deep desaturated olive, the right half one step lighter than the left.
BODY: the resistance element inside the bar, drawn as a flat cut layer over a translucent bar outline, seen from the side. NOT a skeleton, NOT a machine drawing. Exactly one bar in EACH panel, same scale and view.

PANELS. LEFT: a generic unbranded coil spring bar at the end of its stroke, the coil wound down to almost no gap between turns, the two grips forced close together. RIGHT: the reference arm trainer at the end of the same stroke, its hydraulic cylinder drawn as a sealed tube with the piston at the far end and fluid passing through a narrow port around it, the tube wall the same width along its whole length.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each drawn along the resistance element end to end and STOPPING at both ends. Same height in their panel, identical thickness and dash. One property differs: crowded and bunched on the left where the coil has closed, evenly spaced on the right. Red left, blue right.
- verdict: filled solid discs, red with a white cross in the LEFT panel's TOP corner, green with a white check in the RIGHT panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else."""

COIL_C = """TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, paper-cut. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the arm trainer in the RIGHT panel.

FRAME: one resistance bar and the forearm gripping it, from elbow to grip, the bar and the forearm together filling most of the width.
GROUND: deep desaturated slate, the right half one step lighter than the left.
BODY: the resistance element inside the bar and the forearm holding it, cut as separate paper layers in warm ivory over a translucent outline, seen from the side. NOT a skeleton. Exactly one bar and one forearm in EACH panel, same scale and view.

PANELS. LEFT: a generic unbranded coil spring bar with its coil wound tight and the grip beginning to slip out of the hand, the fingers half open and the coil still compressed behind them. RIGHT: the reference arm trainer at the same point of the same stroke with the same hand half open on the grip, its hydraulic cylinder drawn as a sealed tube with the piston resting where it was left and the fluid still either side of it.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each running along the resistance element from end to end and STOPPING at both ends. Same height in their panel, identical thickness and dash. One property differs: bowed and crowded on the left, straight and evenly spaced on the right. Red left, blue right.
- verdict: filled solid discs, red with a white cross in the LEFT panel's TOP corner, green with a white check in the RIGHT panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else."""

# ---------------------------------------------------------------------------
# 4 — content.1.items.2.image · comparison · 04-proof-lockedframe --verdict
# ---------------------------------------------------------------------------
SPACE_A = """TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
""" + REF + """ It appears in the THIRD panel only.

[SCENE — the same in all three]
The same corner of a small living room: the same skirting board, the same short length of oak floor, the same armchair leg entering at the top right and the same folded throw over its arm. Flat overcast light from a window off to the left, no strong shadows, no styling.

[FRAMING]
One person photographed this corner three times from where they always stand, phone held at hip height and level with the floor, the corner of the room filling the middle third of each panel. It reads as one shot taken three times, never as three different shots. Light differs only in exposure, never in warmth.

[THE VARIABLE]
What is standing in that corner, each photographed on an ordinary evening.
1 — a two-tier dumbbell rack holding six mismatched dumbbells, the rack footprint covering the floor from the skirting board out past the armchair leg.
2 — no rack, the same six dumbbells set straight on the floor in two rows, taking a wider patch of floor than the rack did.
3 — the reference arm trainer folded flat and standing on its edge against the skirting board, the floor in front of it clear all the way to the armchair leg.

[FAIRNESS]
Panels 1 and 2 get exactly the same exposure, the same background tidiness and the same framing generosity as panel 3. The rack and the loose dumbbells are ordinary, undamaged and the kind someone would genuinely own. Nothing is lit, cropped or graded to favour any panel. The difference is in how much floor each occupies and nothing else.

[GRADE]
One grade across all three panels: flat, neutral, true to the room's own colour.

STYLE: honest documentary product test photography, unstyled, natural, sharp."""

SPACE_B = """TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
""" + REF + """ It appears in the THIRD panel only.

[SCENE — the same in all three]
The same open drawer under the same divan bed: the same drawer base, the same folded jumper pushed to the back left, the same length of carpet in front of the drawer. Flat daylight from a window off to the right, no strong shadows, no styling.

[FRAMING]
One person photographed this drawer three times from standing, phone angled down over the open drawer, the drawer filling the middle two thirds of each panel. It reads as one shot taken three times, never as three different shots. Light differs only in exposure, never in warmth.

[THE VARIABLE]
What has been put into that drawer, each photographed on an ordinary evening.
1 — a pair of fixed dumbbells laid in the drawer, the drawer unable to close with them in and the front edge standing proud of the bed frame.
2 — a coil spring twister bar laid diagonally across the drawer, its grips overhanging both sides so the drawer front sits open on them.
3 — the reference arm trainer folded flat and lying inside the drawer, the folded jumper still in place beside it and the drawer front sitting flush.

[FAIRNESS]
Panels 1 and 2 get exactly the same exposure, background tidiness and framing generosity as panel 3. The dumbbells and the coil bar are ordinary, undamaged and the kind someone would genuinely own. Nothing is lit, cropped or graded to favour any panel. The difference is whether the drawer closes and nothing else.

[GRADE]
One grade across all three panels: flat, neutral, true to the room's own colour.

STYLE: honest documentary product test photography, unstyled, natural, sharp."""

SPACE_C = """TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
""" + REF + """ It appears in the THIRD panel only.

[SCENE — the same in all three]
The same stretch of floor beside the same two-seater couch: the same couch base and front feet, the same rug edge, the same power socket on the skirting board behind. Flat overcast light from a window off to the left, no strong shadows, no styling.

[FRAMING]
One person photographed this floor three times from where they always stand, phone held low and level with the rug, the gap under the couch running across the lower third of each panel. It reads as one shot taken three times, never as three different shots. Light differs only in exposure, never in warmth.

[THE VARIABLE]
What has been pushed toward the gap under the couch, each photographed on an ordinary evening.
1 — a two-tier dumbbell rack pushed as close as it goes, stopped by the couch base with its whole footprint still out on the rug.
2 — four loose dumbbells pushed at the gap, the two largest stopped by the couch base and left sitting out on the rug in front of it.
3 — the reference arm trainer folded flat and pushed into the gap, only the near edge of it still showing at the rug line.

[FAIRNESS]
Panels 1 and 2 get exactly the same exposure, background tidiness and framing generosity as panel 3. The rack and the dumbbells are ordinary, undamaged and the kind someone would genuinely own. Nothing is lit, cropped or graded to favour any panel. The difference is how far each one goes under and nothing else.

[GRADE]
One grade across all three panels: flat, neutral, true to the room's own colour.

STYLE: honest documentary product test photography, unstyled, natural, sharp."""

# ---------------------------------------------------------------------------
# 5 — content.1.items.3.image · mechanism · 03-mechanism-xray
# ---------------------------------------------------------------------------
DIAL_A = """TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: """ + REF + """ The outer shell becomes translucent, but its silhouette, proportions and every visible external part must match the reference exactly.

CANVAS: a plain pale warm grey ground, and nothing else in the frame behind the product.

SHELL: the trainer lying horizontally across the frame, grips to left and right, its body translucent and glass-like, filling about 75 percent of the frame width.

INTERNALS, solid and detailed inside the shell, each at its true location: the hydraulic cylinder as a sealed metal tube through the centre of the body; a piston partway along that tube with clear fluid either side of it; a narrow adjustable port through the piston, its opening set part way; the dial collar around the outside of the tube, its stem running inward to that port.

MARKS, one, nothing else in the frame is marked:
- working: the fluid passing through the narrow port shown ACTIVE and glowing warm amber in its own moving form, the brightest thing in the frame and clearly brighter than the ground, drawn as fluid squeezing from the wide side of the piston to the narrow side. No arrow anywhere.

No text, numbers or spec labels anywhere in the image.
The mark is the only added colour; the product and its parts keep their own."""

DIAL_B = """TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: """ + REF + """ The outer shell becomes translucent, but its silhouette, proportions and every visible external part must match the reference exactly.

CANVAS: a plain deep charcoal ground, and nothing else in the frame behind the product.

SHELL: the trainer seen at a low three-quarter angle with one grip nearer the camera, its body translucent and glass-like, filling about 70 percent of the frame width.

INTERNALS, solid and detailed inside the shell, each at its true location: the hydraulic cylinder as a sealed metal tube running the length of the body; a piston head partway along it with clear fluid either side; a narrow adjustable port through the piston head; the dial collar on the outside of the tube with its stem reaching in to that port; the pivot joint where the two arms meet the body.

MARKS, one, nothing else in the frame is marked:
- working: the fluid crossing the narrow port shown ACTIVE and glowing warm amber in its own moving form, the brightest thing in the frame and clearly brighter than the ground. No arrow anywhere.

No text, numbers or spec labels anywhere in the image.
The mark is the only added colour; the product and its parts keep their own."""

DIAL_C = """TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: """ + REF + """ The outer shell becomes translucent, but its silhouette, proportions and every visible external part must match the reference exactly.

CANVAS: a plain pale warm sand ground, and nothing else in the frame behind the product.

SHELL: the trainer standing upright and square to the camera, grips at top and bottom, its body translucent and glass-like, filling about 65 percent of the frame height.

INTERNALS, solid and detailed inside the shell, each at its true location: the hydraulic cylinder as a sealed metal tube down the centre of the body; a piston partway down it with clear fluid above and below; a narrow adjustable port through the piston, its opening set almost closed; the dial collar around the tube with its stem running in to that port.

MARKS, one, nothing else in the frame is marked:
- working: the fluid forcing through the almost-closed port shown ACTIVE and glowing warm amber in its own moving form, the brightest thing in the frame and clearly brighter than the ground. No arrow anywhere.

No text, numbers or spec labels anywhere in the image.
The mark is the only added colour; the product and its parts keep their own."""

# ---------------------------------------------------------------------------
# 6 — content.1.items.4.image · social-proof · 05-social-handoff
# ---------------------------------------------------------------------------
SHARE_A = """TYPE: 05-social-handoff v2.5
REGISTER: candid documentary photograph, natural, unposed, sharp. One scene, no inset.

[PRODUCT REFERENCE]
""" + REF + """

[MOMENT]
The trainer is mid-handover across the couch: one person still has a hand on the near grip and the other has just taken the far grip, and the dial collar is under the thumb of the hand taking it. Both people are dealing with that dial.

[ADVOCATE]
Man in his thirties in a plain t-shirt, sitting forward on the couch with one hand still on the near grip where he has just stopped pressing, shoulders warm and breath still up. Mid-sentence, easy and slightly pleased with himself, his eyes on her and never on the camera.

[LISTENER]
Woman in her thirties in a long-sleeved top, sitting on the arm of the couch between him and the camera with her back to us, FACE NOT VISIBLE, head down to the dial her thumb is on.

[PRODUCT]
The reference trainer is the only thing in sharp focus, everything behind it softer. It carries the strongest light in the frame, nothing overlaps or crowds it, and it differs in hue and value from everything else in frame. Nothing of similar size or finish stands near it.

[ENVIRONMENT]
An ordinary living room in the evening, a couch with a throw pushed to one end, a coffee table with two mugs on it, a floor lamp on behind them, a rug with a corner turned up. None of those objects carries printed words.

STYLE: candid documentary photograph, natural, unposed, sharp."""

SHARE_B = """TYPE: 05-social-handoff v2.5
REGISTER: candid documentary photograph, natural, unposed, sharp. One scene, no inset.

[PRODUCT REFERENCE]
""" + REF + """

[MOMENT]
The trainer has just changed hands on a kitchen floor: one person is letting go of the near grip and the other has both hands on it already, and the dial collar sits between their two hands where it was just turned. Both people are dealing with that dial.

[ADVOCATE]
Woman in her forties in a vest and leggings, kneeling on the floor with one hand still trailing the near grip, colour high in her face and her breath still up. Mid-sentence, direct and pleased, her eyes on him and never on the camera.

[LISTENER]
Man in his forties in a hoodie, crouching beside her between her and the camera with his back to us, FACE NOT VISIBLE, head down to the dial his hands have closed on.

[PRODUCT]
The reference trainer is the only thing in sharp focus, everything behind it softer. It carries the strongest light in the frame, nothing overlaps or crowds it, and it differs in hue and value from everything else in frame. Nothing of similar size or finish stands near it.

[ENVIRONMENT]
An ordinary kitchen in the morning, a table pushed back against the units, two chairs turned out, a water bottle on the floor by the skirting, a towel over the back of one chair. None of those objects carries printed words.

STYLE: candid documentary photograph, natural, unposed, sharp."""

SHARE_C = """TYPE: 05-social-handoff v2.5
REGISTER: candid documentary photograph, natural, unposed, sharp. One scene, no inset.

[PRODUCT REFERENCE]
""" + REF + """

[MOMENT]
The trainer is being passed sideways along a hallway: one person holds it out by the near grip at arm's length and the other has closed a hand over the far grip, the dial collar showing between them where it has just been turned down. Both people are dealing with that dial.

[ADVOCATE]
Man in his late twenties in a training top, standing with the trainer held out to one side, one arm still extended from pressing, chest still working. Mid-sentence, quick and amused, his eyes on her and never on the camera.

[LISTENER]
Woman in her late twenties in a zip-up top, standing nearer the camera with her back to us, FACE NOT VISIBLE, head down to the far grip her hand has closed on.

[PRODUCT]
The reference trainer is the only thing in sharp focus, everything behind it softer. It carries the strongest light in the frame, nothing overlaps or crowds it, and it differs in hue and value from everything else in frame. Nothing of similar size or finish stands near it.

[ENVIRONMENT]
An ordinary flat hallway in the evening, coats on hooks along one wall, shoes paired under them, a hall light on overhead and a doorway open to a lit room behind. None of those objects carries printed words.

STYLE: candid documentary photograph, natural, unposed, sharp."""

# ---------------------------------------------------------------------------
# 7 — content.3.items.0.image · how-to-use · 03-use-sequence
# ---------------------------------------------------------------------------
GRIP_A = """TYPE: 03-use-sequence v1.9
REGISTER: warm lifestyle photography, close range, natural and unstyled, soft daylight.

PRODUCT REFERENCE: """ + REF + """ It appears in every panel.

LAYOUT: exactly three photographs, one above another, each the full width of the frame and all three the same height, separated by thin white gutters, no outer border.

CONTINUITY: the SAME pair of hands in all three panels — same skin tone, same nails, same wrists, same cuffs. The same living room rug and the same couch edge behind throughout. The same warm neutral palette and the same soft daylight from the left in every panel. Camera distance and framing shift naturally between panels.

At the top, the trainer rests across the knees and one hand turns the dial collar around the body, the collar part way round and the other hand steadying the near grip.

In the middle, both hands are on the grips at chest height and the two arms of the trainer are compressed toward each other, the wrists straight and the elbows out.

At the bottom, the trainer rests across the knees again with both hands off it and the arms returned to their open position, one hand flat on the rug beside it.

The trainer sits at the same distance from the camera in the top and bottom panels and closer in the middle one.

No text, numbers or labels anywhere in any panel.

STYLE: warm lifestyle photography, close range, natural and unstyled."""

GRIP_B = """TYPE: 03-use-sequence v1.9
REGISTER: warm lifestyle photography, close range, natural and unstyled, soft daylight.

PRODUCT REFERENCE: """ + REF + """ It appears in every panel.

LAYOUT: exactly three photographs, one above another, each the full width of the frame and all three the same height, separated by thin white gutters, no outer border.

CONTINUITY: the SAME pair of hands in all three panels — same skin tone, same nails, same wrists, same cuffs. The same kitchen table top and the same chair back behind throughout. The same warm neutral palette and the same soft daylight from the right in every panel. Camera distance and framing shift naturally between panels.

At the top, the trainer lies flat on the table and one hand turns the dial collar around the body while the other holds the near grip still against the table.

In the middle, the trainer is lifted clear of the table and held vertically, one hand on the upper grip and one on the lower, the two arms compressed toward each other and both wrists straight.

At the bottom, the trainer lies flat on the table again with both hands off it, its arms returned to their open position and one hand resting on the table edge beside it.

The trainer sits at the same distance from the camera in the top and bottom panels and closer in the middle one.

No text, numbers or labels anywhere in any panel.

STYLE: warm lifestyle photography, close range, natural and unstyled."""

GRIP_C = """TYPE: 03-use-sequence v1.9
REGISTER: warm lifestyle photography, close range, natural and unstyled, soft daylight.

PRODUCT REFERENCE: """ + REF + """ It appears in every panel.

LAYOUT: exactly three photographs, one above another, each the full width of the frame and all three the same height, separated by thin white gutters, no outer border.

CONTINUITY: the SAME pair of hands in all three panels — same skin tone, same nails, same wrists, same cuffs. The same bedroom floor and the same wardrobe base behind throughout. The same warm neutral palette and the same soft daylight from the left in every panel. Camera distance and framing shift naturally between panels.

At the top, the trainer rests on the floor and one hand turns the dial collar around the body, the other hand holding the near grip down against the boards.

In the middle, both hands are on the grips out in front of the body at shoulder height and the two arms of the trainer are compressed toward each other, the elbows lifted and the wrists straight.

At the bottom, the trainer lies on the floor again with both hands off it, its arms returned to their open position, folded flat with one hand resting on the boards beside it.

The trainer sits at the same distance from the camera in the top and bottom panels and closer in the middle one.

No text, numbers or labels anywhere in any panel.

STYLE: warm lifestyle photography, close range, natural and unstyled."""

# ---------------------------------------------------------------------------
# 8 — content.3.items.1.image · outcome · 06-relief-hero
# ---------------------------------------------------------------------------
COUNT_A = """TYPE: 06-relief-hero v1.17 --commercial
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
""" + REF + """

[SUBJECT]
Man in his thirties in a training top, sitting on the edge of a couch a moment after a set, the trainer resting across his thighs with both hands still loosely on the grips, looking down at the counter housing on the body of it rather than at the camera. Settled, breathing out, mid-action just ended.

[PRODUCT]
The reference trainer across his thighs, low front three-quarter angle, whole and unobstructed, the counter housing on its body turned toward the camera and its screen dark and unlit.

[SETTING]
A real living room corner filled to the edges: a water bottle on the floor by the couch foot, a towel over the couch arm, a rug with a corner turned up, a floor lamp on behind, a bowl on the coffee table, a pair of trainers by the skirting. None of them carries printed words. Background soft, never blank.

[LIGHT]
Soft even window light from the left, background blurred, high-key neutral grade.

[LAYOUT]
He sits to the left of the frame; the right side carries the depth of the room.

No text, numbers, digits or readouts anywhere in the image. The counter screen is dark and carries nothing.

STYLE: clean commercial photograph, controlled light, sharp."""

COUNT_B = """TYPE: 06-relief-hero v1.17 --ugc
REGISTER: a phone in an ordinary person's hand: slightly off exposure, no rim light, no negative space, framing casual and a little too close, the room left exactly as it is.

[PRODUCT REFERENCE]
""" + REF + """

[SUBJECT]
Present only as working hands and forearms — no face. Both hands are off the grips and resting either side of the trainer where it lies across a rug, one thumb still against the counter housing on its body. What makes finished look different from unfinished: the two arms of the trainer have returned to their open resting position and neither hand is loaded.

[PRODUCT]
The reference trainer lying across the rug between the forearms, seen from above at a slight angle, whole and unobstructed, the counter housing turned up toward the camera and its screen dark and unlit.

[SETTING]
An ordinary living room floor left exactly as it is: a water bottle on its side, a balled towel, the corner of a couch, a phone face down on the rug, a sock, a mug on the boards. None of them carries printed words. Nothing tidied, nothing removed.

[LIGHT]
Ordinary room light, mild overexposure where the window falls on the rug, no rim light.

No text, numbers, digits or readouts anywhere in the image. The counter screen is dark and carries nothing.

STYLE: honest phone photography, unedited look, natural, slightly imperfect."""

COUNT_C = """TYPE: 06-relief-hero v1.17 --commercial
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
""" + REF + """

[SUBJECT]
Woman in her forties in a vest and leggings, kneeling back on her heels on a bedroom floor a moment after a set, the trainer standing on the boards in front of her with one hand resting on its upper grip, looking down at the counter housing on its body rather than at the camera. Settled, breathing out, mid-action just ended.

[PRODUCT]
The reference trainer standing on the boards in front of her, low front three-quarter angle, whole and unobstructed, the counter housing on its body turned toward the camera and its screen dark and unlit.

[SETTING]
A real bedroom corner filled to the edges: a rolled mat against the wardrobe, a water bottle on the boards, a hairband on the sill, a chair with a jumper over the back, a laundry basket, a lamp on the floor. None of them carries printed words. Background soft, never blank.

[LIGHT]
Soft even window light from the right, background blurred, high-key neutral grade.

[LAYOUT]
She kneels to the right of the frame; the left side carries the depth of the room.

No text, numbers, digits or readouts anywhere in the image. The counter screen is dark and carries nothing.

STYLE: clean commercial photograph, controlled light, sharp."""


def snap(mode, hold, scene, anchor, light):
    """05-social-snapshot: one frame, no layout, no layers. SET DIVERSITY LAW —
    every tile differs completely in room class, surface, anchor and light."""
    return f"""A real customer's phone photo. One frame, no layout.

{REF} {hold}

CONTENT MODE, {mode}.

SCENE: {scene}

ANCHOR: {anchor} — the one incidental owner object.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus adequate, mild noise, honest exposure, {light}. No styling of any kind.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
NO text overlays, no logo, no watermark, no badges, no borders. No digits or readouts anywhere; any counter screen is dark and carries nothing."""


REVIEWS = [
    snap("at-rest",
         "It is standing folded flat on its edge against a skirting board, photographed from "
         "standing height and cropped the way a casual one-handed photo crops.",
         "A studio flat photographed as found — a scuffed painted skirting board, a worn oak "
         "floorboard, the base of a radiator behind.",
         "A pair of slippers kicked off beside it",
         "warm ceiling light with a cool window spill"),
    snap("in-use",
         "It is held across the chest mid-press, both grips taken, seen from slightly below "
         "and a little too close.",
         "A narrow spare bedroom photographed as found — a wardrobe door ajar, a folded duvet "
         "at the end of the bed, a curtain half drawn.",
         "A wall clock hanging crooked above the bed",
         "flat grey daylight through the half-drawn curtain"),
    snap("at-rest",
         "It is lying on a desk beside a laptop, folded flat, photographed from a seated "
         "position looking down.",
         "A home-office corner photographed as found — a laminate desktop with a ring mark, a "
         "cable coming over the back edge, a chair arm entering the frame.",
         "A half-drunk glass of water on a coaster",
         "cool screen light mixed with a warm desk lamp"),
    snap("at-rest",
         "It is lying in the gap under a divan bed, folded flat, photographed from floor level "
         "with the phone tilted down.",
         "A rented bedroom photographed as found — carpet with a flattened track across it, a "
         "divan base, a plug socket on the skirting.",
         "A phone charger cable coiled beside it",
         "low evening light from one bedside lamp"),
    snap("in-use",
         "It is held out to one side at arm's length, one grip taken, seen from across a room "
         "and cropped a little too wide.",
         "A through lounge photographed as found — two mismatched armchairs, a rug that does "
         "not reach the walls, a doorway to a lit hall behind.",
         "A remote control left on an armchair seat",
         "mixed warm lamplight and dim daylight"),
    snap("at-rest",
         "It is standing folded on end inside an open under-stairs cupboard, photographed with "
         "the phone held at chest height.",
         "An under-stairs cupboard photographed as found — bare plaster, a sloping ceiling, a "
         "vacuum cleaner hose coiled on the floor.",
         "A folded step ladder leaning at the back",
         "a single bare bulb overhead"),
]

# ---------------------------------------------------------------------------
# Slot assembly
# ---------------------------------------------------------------------------


def opt(o, varies, typ, ratio, prompt, rationale, variant=None, axes=None,
        pipeline="single-pass", notes=None, blocking=None):
    d = {"opt": o, "varies_on": varies, "type": typ,
         "type_version": TYPE_VERSION[typ], "ratio": ratio,
         "pipeline": pipeline, "prompt": prompt, "avoid": AVOID,
         "rationale": rationale}
    if variant:
        d["variant"] = variant
    if axes:
        d["axes"] = axes
    if notes:
        d["composition_notes"] = notes
    if blocking:
        d["blocking_precondition"] = blocking
    return d


FENCE = ("BLOCKING — DO NOT RENDER UNTIL RESOLVED. This tile sits in a review block "
         "whose quotes each carry a full name and a `Verified Buyer` label. "
         "`05-social-snapshot` SLOT CONSTRAINTS: never pair a generated snapshot with a "
         "reviewer name, avatar, star row or verified badge, and never present one as an "
         "actual customer upload — that is a fabricated endorsement (FTC). Resolve by "
         "de-attributing the block or by using real customer photographs. The prompt is "
         "emitted so the fix is a template change and not a re-route.")

SLOTS = [
    {
        "slot_id": "content.0.image",
        "section_role": "hero",
        "asset": "193-01-opener-pain-scene.jpg",
        "placement": "listicle header, under the title and dek, above the intro paragraphs",
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis": "",
        "options": [
            opt("A", "baseline", "01-pain-scene", "16:9", OPEN_A,
                "The plateau has no photographable symptom, so evidence takes rank 3 — the "
                "failed tool in the state that shows it failed. Four mismatched dumbbells in "
                "three finishes, the heaviest still boxed, is the copy's own 'buying the next "
                "dumbbell up restarts the problem' as an object. --candid because a stalled "
                "press-up is physical limitation, not self-image.",
                variant="candid", axes={"gaze": "candid"}),
            opt("B", "axis: gaze=confront", "01-pain-scene", "16:9", OPEN_B,
                "Same evidence and cost, the moment moved to between sets and the gaze into "
                "the lens. --confront treats the plateau as a daily frustration rather than a "
                "physical limit, which is the reading the dek takes.",
                variant="confront", axes={"gaze": "confront"}),
            opt("C", "execution: persona, room and time of day", "01-pain-scene", "16:9", OPEN_C,
                "Same type and axes as A, a different person and place. The dumbbell evidence "
                "becomes a spinlock bar with its collar loose and plates stacked separately — "
                "the same argument in a household that bought adjustable iron instead.",
                variant="candid", axes={"gaze": "candid"}),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "The slot exists so the reader recognises themselves, and recognition "
                      "is a held state. A locked-out press-up at the top of the rep is a "
                      "position, not a transition — nothing in the frame is mid-change. "
                      "Consistent with every hero refused across the routed pages.",
        },
    },
    {
        "slot_id": "content.1.items.0.image",
        "section_role": "mechanism",
        "asset": "193-02-reason1-mechanism-ghostbody.jpg",
        "placement": "reason card 1, beside the body copy",
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis": "",
        "options": [
            opt("A", "baseline", "03-mechanism-ghostbody", "1:1", PLAT_A,
                "The card's claim is a body fact — muscle grows against added resistance and "
                "bodyweight has no dial — which is exactly what this type exists to draw and "
                "what no camera can film. body_contact is true, so the type is not gated out. "
                "Two panels, the only variable being what the hands press against.",
                axes={"medium": "3d-render"}),
            opt("B", "axis: medium = 2D medical illustration", "03-mechanism-ghostbody", "1:1",
                PLAT_B,
                "Same two-panel argument in the softer register. An airbrushed medical "
                "illustration reads as an explanation rather than a product render, which "
                "suits a card whose subject is the reader's own chest and not the device.",
                axes={"medium": "2d-airbrush"}),
            opt("C", "execution: seated side view, single arm", "03-mechanism-ghostbody", "1:1",
                PLAT_C,
                "Same type and medium as A, the view turned to the side and the argument "
                "narrowed to one arm driving forward. A side cut shows the muscle shortening "
                "along its length, which the front view can only show as thickening.",
                axes={"medium": "3d-render"}),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "Two locked panels are inspected rather than watched — the reader holds "
                      "wrong and right side by side and reads the marks against each other. "
                      "A re-execution as one continuous frame was examined at rung 2 and "
                      "refused: the muscle change is a drawn abstraction, so a loop of it "
                      "would animate an illustration's own convention rather than a real "
                      "state changing.",
        },
    },
    {
        "slot_id": "content.1.items.1.image",
        "section_role": "cause",
        "asset": "193-03-reason2-cause-anatomy.jpg",
        "placement": "reason card 2, beside the body copy",
        "recommended_media": "gif",
        "recommended_opt": "A",
        "recommendation_basis": "",
        "options": [
            opt("A", "baseline", "02-cause-anatomy", "1:1", COIL_A,
                "The card blames one concrete object — a coil spring bar — and names its harm "
                "mechanism, stored energy released without control. That is this type's whole "
                "trigger. The harm does not persist once the culprit is gone, which is the "
                "avoid_when that would otherwise rule it out.",
                variant="diagnostic"),
            opt("B", "axis: style = flat vector, stroke at full compression",
                "02-cause-anatomy", "1:1", COIL_B,
                "Same argument at the end of the stroke rather than mid-stroke, drawn flat. "
                "Full compression is where the coil holds the most energy, so the measure mark "
                "has the widest difference to carry.",
                variant="diagnostic"),
            opt("C", "execution: the forearm and a slipping grip enter the frame",
                "02-cause-anatomy", "1:1", COIL_C,
                "Same type and style as A with the hand added, because the copy's failure "
                "moment is grip tiring on the last rep. The frame then shows the condition "
                "under which the stored energy is released rather than the energy alone.",
                variant="diagnostic"),
        ],
        "gif": {
            "eligible": True, "form": "whole-frame", "kind": "cause", "type_id": "cause",
            "rung": "re-execution",
            "reason": "The still is a two-panel illustration and panels are inspected, not "
                      "watched, so the routed execution earns no loop. Restaged at rung 2 it "
                      "does: a coil releasing and a hydraulic piston refusing to release are "
                      "the same claim shot as one continuous frame, and the release IS the "
                      "argument. The job never changes — this is still the cause card.",
            "ratio": "1:1", "duration_s": 2.5, "loop": "seamless loop",
            "output": gif_name("content.1.items.1.image"),
            "delivery": "mp4/webm, muted, loop-safe, under the size ceiling",
            "brief": "Two resistance bars lie side by side on a plain floor, each held "
                     "compressed by a hand. Both hands let go at the same moment, the coil bar "
                     "flies open and jumps clear of the floor, then the hydraulic bar opens "
                     "slowly and evenly and stops where it was.",
            "alt": "A close shot of one coil bar and one hydraulic bar clamped in the same "
                   "rig, both compressed and released together, the coil snapping open past "
                   "its rest position while the hydraulic arm travels out at one steady speed.",
            "refs": "gifs-library/cause/ — no files filed yet; the folder card carries the law",
            "asset": "193-03-reason2-cause-anatomy--brief.svg",
        },
    },
    {
        "slot_id": "content.1.items.2.image",
        "section_role": "comparison",
        "asset": "193-04-reason3-proof-lockedframe.jpg",
        "placement": "reason card 3, beside the body copy",
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis": "",
        "options": [
            opt("A", "baseline", "04-proof-lockedframe", "1:1", SPACE_A,
                "The claim is floor space, which is exactly the difference a locked frame can "
                "prove: same corner, same light, only the occupant changes. --verdict puts the "
                "product last because left-to-right reading ends on it. Runs handheld, since "
                "strict camera lock needs compositing this pipeline cannot do.",
                variant="verdict", axes={"camera_lock": "handheld"}),
            opt("B", "execution: a bed drawer instead of a floor corner",
                "04-proof-lockedframe", "1:1", SPACE_B,
                "Same variant, the test moved to storage rather than footprint. Whether the "
                "drawer closes is a binary a static frame reads instantly, where floor area "
                "has to be estimated.",
                variant="verdict", axes={"camera_lock": "handheld"}),
            opt("C", "execution: the gap under a couch", "04-proof-lockedframe", "1:1", SPACE_C,
                "Same variant again, staged on the copy's own sentence — the frame slides "
                "under the couch. The rival panels fail by being stopped at the couch base, "
                "which is a physical outcome and not a treatment.",
                variant="verdict", axes={"camera_lock": "handheld"}),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "Floor space is a held state: the rack occupies the corner whether or "
                      "not time passes, and nothing in the frame changes. Examined at rung 2 "
                      "as a folding shot and refused on the budget as well — `content.1` "
                      "already carries its two permitted loops at items.1 and items.3, and "
                      "this slot sits between them, so the spacing rule and not the argument "
                      "decided it.",
        },
    },
    {
        "slot_id": "content.1.items.3.image",
        "section_role": "mechanism",
        "asset": "193-05-reason4-mechanism-xray.jpg",
        "placement": "reason card 4, beside the body copy",
        "recommended_media": "gif",
        "recommended_opt": "A",
        "recommendation_basis": "",
        "options": [
            opt("A", "baseline", "03-mechanism-xray", "1:1", DIAL_A,
                "The card sells an interior the buyer cannot see and would not otherwise "
                "believe — a dial that changes a fluid port. Horizontal and square to camera "
                "puts the whole cylinder across the frame, so the port and the dial stem read "
                "as one connected thing.",
                axes={"canvas": "warm-grey"}),
            opt("B", "axis: canvas = deep charcoal, low three-quarter view",
                "03-mechanism-xray", "1:1", DIAL_B,
                "Same internals, darker ground. The working mark has to be the brightest thing "
                "in frame, and a charcoal canvas buys that margin without brightening the mark "
                "itself. Adds the pivot joint, which the horizontal view crops.",
                axes={"canvas": "charcoal"}),
            opt("C", "execution: upright, port set almost closed", "03-mechanism-xray", "1:1",
                DIAL_C,
                "Same type, the dial shown at the heavy end of its range rather than mid-way. "
                "An almost-closed port is the visual form of high resistance, so the frame "
                "argues the range rather than the mechanism alone.",
                axes={"canvas": "warm-sand"}),
        ],
        "gif": {
            "eligible": True, "form": "whole-frame", "kind": "mechanism",
            "type_id": "mechanism", "rung": "natural",
            "reason": "The card's own claim is timed — resistance changes in about two seconds "
                      "— so the slot's reason to exist is a transition and it earns a loop as "
                      "routed. The see-through render is the one frame where that change is "
                      "visible at all, since from outside only a collar turns.",
            "ratio": "1:1", "duration_s": 2.5, "loop": "seamless loop",
            "output": gif_name("content.1.items.3.image"),
            "delivery": "mp4/webm, muted, loop-safe, under the size ceiling",
            "brief": "A see-through view of the trainer's cylinder fills the frame with the "
                     "piston partway along it. A hand turns the dial collar a short way and "
                     "the port through the piston narrows, then the fluid crossing it slows "
                     "and thickens while the piston keeps moving at the same speed.",
            "alt": "The same see-through cylinder with no hand in frame, the dial collar "
                   "turning on its own and the port closing, the fluid stream through it "
                   "thinning to a hard bright thread as the opening shrinks.",
            "refs": "gifs-library/mechanism/ — no files filed yet; the folder card carries "
                    "the law",
            "asset": "193-05-reason4-mechanism-xray--brief.svg",
        },
    },
    {
        "slot_id": "content.1.items.4.image",
        "section_role": "social-proof",
        "asset": "193-06-reason5-social-handoff.jpg",
        "placement": "reason card 5, beside the body copy",
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis": "",
        "options": [
            opt("A", "baseline", "05-social-handoff", "1:1", SHARE_A,
                "The copy's own sentence is a handoff — one person hands it across the couch "
                "and the other dials up. This type is the handoff, and the dial under the "
                "receiving thumb is what makes the shared-range claim visible rather than "
                "asserted. The inset is omitted, which is the type's own single-pass route.",
                notes="Inset omitted, not the type — the inset needs compositing and ADR-021 "
                      "forbids it. The type calls the inset-free route the safer one."),
            opt("B", "execution: kitchen floor, roles reversed", "05-social-handoff", "1:1",
                SHARE_B,
                "Same type and moment with the advocate a woman and the listener a man, which "
                "is the pairing the persona line describes first. A kitchen floor also removes "
                "the couch, so the frame does not read as a rest scene.",
                notes="Inset omitted, not the type."),
            opt("C", "execution: hallway, passed at arm's length", "05-social-handoff", "1:1",
                SHARE_C,
                "Same type, the handoff standing rather than seated. Arm's length puts the "
                "whole device between the two people, which is the clearest reading of one "
                "frame serving two programs.",
                notes="Inset omitted, not the type."),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "The argument IS temporal — a device changing hands and a dial turning "
                      "between two people is a transition, and this slot earns motion on its "
                      "own grounds. It is refused by the budget: `content.1` may carry two "
                      "loops and both are taken by items.1 and items.3, which are non-adjacent "
                      "where a third could not be. Recorded as a reserve.",
        },
    },
    {
        "slot_id": "content.3.items.0.image",
        "section_role": "how-to-use",
        "asset": "193-07-reason6-use-sequence.jpg",
        "placement": "reason card 6, beside the body copy",
        "recommended_media": "gif",
        "recommended_opt": "A",
        "recommendation_basis": "",
        "options": [
            opt("A", "baseline", "03-use-sequence", "1:1", GRIP_A,
                "The card's whole subject is that nothing tells you how to hold it, so the "
                "slot has to answer 'will I manage this'. multi_step_usage is true — set the "
                "dial, press, return — so the type is not gated out, and three panels are the "
                "wall chart the box does not contain.",
                notes="Step-3 budget: this is the second of the two permitted members of "
                      "{ghostbody, spec-split, use-sequence} on this page. A third would be a "
                      "lecture."),
            opt("B", "execution: kitchen table, vertical press", "03-use-sequence", "1:1",
                GRIP_B,
                "Same three beats on a table rather than the knees, and a vertical rather than "
                "a horizontal press. A table gives the panels a constant horizon, which is the "
                "easiest continuity for a renderer to hold across three frames."),
            opt("C", "execution: bedroom floor, arms out at shoulder height",
                "03-use-sequence", "1:1", GRIP_C,
                "Same three beats with the press taken out in front of the body, and the last "
                "panel showing the frame folded flat. That ends the sequence on the storage "
                "claim rather than on the rest position."),
        ],
        "gif": {
            "eligible": True, "form": "whole-frame", "kind": "use", "type_id": "use",
            "rung": "re-execution",
            "reason": "Three stacked panels are read one after another rather than watched, so "
                      "the routed still earns nothing. Restaged at rung 2 it does: set, press, "
                      "release is one continuous action in one frame, and the card's claim — "
                      "that you work the grip out for yourself — is a thing happening rather "
                      "than a state. Same job, one continuous take instead of three panels.",
            "ratio": "1:1", "duration_s": 4, "loop": "seamless loop",
            "output": gif_name("content.3.items.0.image"),
            "delivery": "mp4/webm, muted, loop-safe, under the size ceiling",
            "brief": "A pair of hands holds the trainer across the knees on a living room rug. "
                     "One hand turns the dial collar a short way, both hands take the grips and "
                     "press the two arms together until they nearly meet, then the arms open "
                     "back out and the hands come off it.",
            "alt": "The same hands and the same rug with the trainer flat on the floor instead "
                   "of the knees, one hand turning the collar and both hands pressing the arms "
                   "together from above, then letting them rise back open.",
            "refs": "gifs-library/use/ — no files filed yet; the folder card carries the law",
            "asset": "193-07-reason6-use-sequence--brief.svg",
        },
    },
    {
        "slot_id": "content.3.items.1.image",
        "section_role": "outcome",
        "asset": "193-08-reason7-relief-hero.jpg",
        "placement": "reason card 7, the closing card of the list",
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis": "",
        "options": [
            opt("A", "baseline", "06-relief-hero", "1:1", COUNT_A,
                "The closing card, and the one image that has to show the product whole in a "
                "real room after a session. The counter housing is turned to camera and its "
                "screen left dark — see this slot's composition note, which is where the "
                "counter's readout is dealt with.",
                axes={"register": "commercial"},
                notes="G6 COUNTER RULE. The card sells an LCD readout. G6's scope note admits "
                      "diegetic screen text as content, but its production rule is that "
                      "screens are never model-drawn and are composited in post — which "
                      "ADR-021 forbids this pipeline. Both are satisfied the only way "
                      "available: the counter is in frame as a physical part and its screen "
                      "is dark. The number is claimed in copy, never rendered."),
            opt("B", "axis: register = ugc, subject reduced to hands", "06-relief-hero", "1:1",
                COUNT_B,
                "Same slot in the trust register, subject reduced to forearms because the "
                "result here is the finished set and not the person. `reduced` names what "
                "makes finished look different from unfinished — the arms returned to rest "
                "and neither hand loaded.",
                axes={"register": "ugc", "subject": "reduced"},
                notes="G6 COUNTER RULE as option A: counter present, screen dark, no digits."),
            opt("C", "execution: bedroom, product standing rather than across the lap",
                "06-relief-hero", "1:1", COUNT_C,
                "Same type and register as A, a different person and room, and the device "
                "standing on the floor so its whole silhouette reads. A standing frame also "
                "shows it takes no more floor than its own footprint.",
                axes={"register": "commercial"},
                notes="G6 COUNTER RULE as option A: counter present, screen dark, no digits."),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "The rep motion is temporal and this slot would earn a loop on the "
                      "argument, but the loop the card actually wants is the counter "
                      "incrementing, and that is a readout changing — G6 admits diegetic "
                      "screen text only on a production rule (never model-drawn, composited "
                      "in post) that ADR-021 forbids. Refused on the frame's own terms rather "
                      "than the budget's. `content.3` also carries its one permitted loop at "
                      "items.0.",
        },
    },
]

for i, prompt in enumerate(REVIEWS):
    SLOTS.append({
        "slot_id": f"reviews.photos.{i}.image",
        "section_role": "social-proof",
        "asset": f"193-09-review{i + 1}-social-snapshot.jpg",
        "placement": f"review wall tile {i + 1} of 6, above the quote and its attribution",
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis": "",
        "options": [
            opt("A", f"set member {i + 1} of 6 — room class, surface, anchor and light all "
                     f"differ from every sibling", "05-social-snapshot", "1:1", prompt,
                "One option only: the type legislates a SET, so the unit of variation is the "
                "tile and not the cell. Three options inside one tile would spend the "
                "variation in the wrong place.",
                blocking=FENCE),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "No social-proof slot carries motion. The mechanism is the six-type gif "
                      "set carrying no `social` type at all, so there is nothing to file a "
                      "loop under — wall tile or standalone. Not a budget decision.",
        },
    })

OUT_OF_SCOPE = [
    ("rail.image", "cta", "sticky deal rail thumbnail"),
    ("scarcity.image", "cta", "scarcity block, beside the countdown"),
    ("scarcity.badge_image", "cta", "scarcity block badge"),
    ("guarantee.badge_image", "cta", "guarantee band badge"),
    ("header.logo", "cta", "site header brand mark"),
    ("footer.logo", "cta", "site footer brand mark"),
    ("closing.bio_image", "author", "About the Author card portrait"),
] + [(f"comments.items.{i}.avatar", "author", f"comment thread avatar {i + 1} of 7")
     for i in range(7)]

for sid, role, place in OUT_OF_SCOPE:
    why = ("A standard product shot, a brand mark or an offer badge — the slot-rules `cta` "
           "row is empty on every channel and this is out of library scope."
           if role == "cta" else
           "A portrait of a named person. The slot-rules `author` row is empty on every "
           "channel by decision: no library type produces a portrait of a named individual, "
           "and generating a face to sit under a real byline is a disclosure decision rather "
           "than an image one.")
    SLOTS.append({
        "slot_id": sid, "section_role": role,
        "asset": None, "placement": place,
        "recommended_media": "still",
        "options": [],
        "out_of_scope": why,
        "gif": {"eligible": False, "form": "none",
                "reason": "The slot carries no library image, so there is nothing to animate."},
    })

# ---------------------------------------------------------------------------
# recommendation_basis — COMPOSED from the prompts, never typed (memory: generate
# numbers, never type them). A check below fails any figure that disagrees.
# ---------------------------------------------------------------------------
BASIS = {
    "content.0.image":
        "FIT: the opener has to make a plateaued home lifter recognise themselves before the "
        "list starts, which is this type's only job. EVIDENCE: rank 3 (the failed tool) is the "
        "only rung available — a plateau has no photographable symptom — and A carries it with "
        "four mismatched dumbbells including one still boxed, which is the copy's repeat-"
        "purchase sentence as an object. B moves to --confront and reads as frustration rather "
        "than limitation, which is the weaker half of the dek. PROMPT RISK: {A}/{B}/{C} "
        "characters against this type's 2500 ceiling.",
    "content.1.items.0.image":
        "FIT: the card argues a body fact no camera can film, which is the ghostbody trigger, "
        "and body_contact is true so the type survives its gate. B's medical register suits the "
        "subject but 3D holds the two-panel discipline more reliably in this library's history. "
        "PROMPT RISK: {A}/{B}/{C} characters against this type's 2400 ceiling.",
    "content.1.items.1.image":
        "FIT: one named culprit and a measurable harm mechanism is exactly 02-cause-anatomy's "
        "trigger, and the harm stops when the culprit goes, which clears its avoid_when. A "
        "takes mid-stroke because the measure mark needs the coil compressed but still legible "
        "as a coil. PROMPT RISK: {A}/{B}/{C} characters against this type's 2050 ceiling.",
    "content.1.items.2.image":
        "FIT: floor space is visible to the naked eye inside a static frame, which is the one "
        "condition 04-proof-lockedframe sets. A stages the copy's own corner-of-the-room "
        "sentence; B and C are tighter binaries but narrower claims. PROMPT RISK: {A}/{B}/{C} "
        "characters against this type's 2600 ceiling.",
    "content.1.items.3.image":
        "FIT: the dial's value is entirely internal, and this type exists for gadget-class "
        "interiors that are not trivial — a piston, a port and a dial stem are three real "
        "connected parts. A's horizontal view keeps all three in one line. PROMPT RISK: "
        "{A}/{B}/{C} characters against this type's 2000 ceiling.",
    "content.1.items.4.image":
        "FIT: the copy describes a literal handoff across a couch, and this type is that "
        "moment. A keeps the dial under the receiving thumb, which is what turns a shared-"
        "device claim into a shared-RANGE claim. PROMPT RISK: {A}/{B}/{C} characters against "
        "this type's 2300 ceiling.",
    "content.3.items.0.image":
        "FIT: the card's admission that there is no wall chart makes 'will I manage this' the "
        "slot's question, which is 03-use-sequence's own. A stages it on the rug the opener "
        "already established. PROMPT RISK: {A}/{B}/{C} characters against this type's 2200 "
        "ceiling.",
    "content.3.items.1.image":
        "FIT: the closing card needs the product whole in a real room, which is 06-relief-"
        "hero's job, and commercial register suits a landing page's last image. All three "
        "options carry the same G6 counter rule. PROMPT RISK: {A}/{B}/{C} characters against "
        "this type's 2600 ceiling.",
}

for s in SLOTS:
    b = BASIS.get(s["slot_id"])
    if b:
        lens = {o["opt"]: len(o["prompt"]) for o in s["options"]}
        s["recommendation_basis"] = b.format(**lens)
    elif s["slot_id"].startswith("reviews."):
        s["recommendation_basis"] = (
            "One option by the type's SET DIVERSITY LAW. Not renderable as the block stands — "
            "see the blocking precondition on the option.")
    else:
        s.pop("recommendation_basis", None)

# ---------------------------------------------------------------------------
# Step 5d — motion budget
# ---------------------------------------------------------------------------
ELIG = [s for s in SLOTS if s["gif"].get("eligible")]

MOTION = {
    "floor": 2,
    "ceiling": 5,
    "delivered": len(ELIG),
    "margin": len(ELIG) - 2,
    "groups_covered": ["working"],
    "shortfall_reason": None,
    "reserves": [
        {"slot_id": "content.1.items.4.image", "substitutes_for": "content.1.items.3.image",
         "why": "Earned motion on its own argument — a device changing hands and a dial "
                "turning between two people is a transition — and lost to the two-loop cap on "
                "`content.1`. Promoting it in place of items.3 leaves items.1 and items.4 "
                "three apart, so the spacing rule stays satisfied."},
    ],
    "notes": [
        "Three loops against a floor of 2, so margin is 1. Under the pre-ADR-050 reading of a "
        "section this page would have carried TWO: `content.0`, `content.1` and `content.3` "
        "all collapsed to one section named `content`, which the five-item relaxation caps at "
        "two loops for the whole page body. Splitting them by block index gives `content.1` "
        "its two and `content.3` its one, and the third loop is the difference ADR-050 makes "
        "on this page.",
        "COVERAGE PAIR NOT MET: cause, mechanism and use are all `working` types and no "
        "`result` loop is delivered. The two result types had no candidate — the proof card "
        "argues floor space, which is a held state, and the relief card's loop would have to "
        "be a counter incrementing, which G6 refuses in this pipeline. Step 5d treats coverage "
        "as a preference, and restaging a strong slot to fill the column would buy a tidy "
        "table and lose the better argument.",
        "`content.1` carries two loops at items.1 and items.3. The section runs to five items "
        "and the two are not adjacent, which is what ADR-032 requires; items.2 sits between "
        "them and is refused by the spacing rule rather than by its argument.",
        "`content.3` carries one loop. The section has two items, fewer than the five ADR-032 "
        "needs for a second, so items.1 could not have taken one even had G6 allowed it.",
        "Review wall: 0 tiles, and not by budget — the six-type gif set carries no `social` "
        "type, so those slots have nothing to file a loop under.",
        "All three loops are whole-frame, which is the only form since ADR-051. No still on "
        "this page reserves or blanks any part of a frame for a loop to land in; every "
        "recommended still is complete and ships on its own.",
        "Two of the three are rung `re-execution`. Both are panel layouts — a two-panel cause "
        "illustration and a three-panel use sequence — restaged as one continuous frame, which "
        "is the library's main re-execution case.",
    ],
}

OUT = {
    "page_id": PAGE,
    "registry_version": "2.0.0",
    "channel": CONTRACT["page"]["channel"],
    "awareness_stage": "solution-aware",
    "slots": SLOTS,
    "coverage": {
        "sections_routed": len({DECLARED[s["slot_id"]]["role"] for s in SLOTS
                                if s.get("options")}),
        "library_slots": len([s for s in SLOTS if s.get("options")]),
        "out_of_scope_slots": len([s for s in SLOTS if s.get("out_of_scope")]),
    },
    "recommended": [],
    "motion": MOTION,
    "page_composition_notes": [],
}

OUT["page_composition_notes"] = [
    "AWARENESS: solution-aware, read from the copy and not from a field. The opener spends no "
    "words establishing that a plateau exists — it assumes the reader is already there — and "
    "goes straight to comparing solution CLASSES: fixed dumbbells, coil twister bars, gym "
    "memberships and bodyweight. Reasons 2, 3 and 4 each indict one of those classes by name. "
    "For that reader, mechanism and physical proof are what decide it and re-amplifying the "
    "problem insults them, which is why exactly one pain image is routed and it sits in the "
    "header where the format demands one.",
    "PAGE SET: eight library slots, eight distinct types, no repeat. `01-pain-scene` opens; "
    "`03-mechanism-ghostbody` and `03-mechanism-xray` take the two mechanism cards, one inside "
    "the body and one inside the device; `02-cause-anatomy` takes the coil bar; "
    "`04-proof-lockedframe --verdict` takes the space claim; `05-social-handoff` takes the "
    "shared-use card; `03-use-sequence` takes the no-wall-chart card; `06-relief-hero` closes. "
    "The six review tiles take `05-social-snapshot` under the repeating-section exemption to "
    "one-type-once.",
    "STEP-3 BUDGET: two of {03-mechanism-ghostbody, 03-spec-split, 03-use-sequence} are used "
    "and the cap is two. `03-spec-split` was never available — it is marketplace-only.",
    "ATTRIBUTE GATES KILLED: " + ", ".join(KILLED) + ". `01-pain-split` falls to "
    "symptom_visibility invisible, `06-relief-scene` to result_visibility invisible. Neither "
    "was needed: pain-split is not on the advertorial shortlist at all, and the closing image "
    "is `06-relief-hero`, which is the substitution that gate names.",
    "RATIO: every card is 1:1 and the header is 16:9. 1:1 is the ONLY ratio all seven card "
    "types share once ADR-016's five are intersected with each type's declared list — "
    "`03-mechanism-ghostbody` declares only 1:1 and 4:5, and 4:5 is not one of the five. "
    "16:9 at the header because `01-pain-scene` does not declare 1:1.",
    "PIPELINE: every option is single-pass. `04-proof-lockedframe` runs handheld rather than "
    "strict and `05-social-handoff` omits its inset — both are the types' own recorded "
    "single-pass routes, not degradations invented here (ADR-021).",
    "REFERENCE PHOTO: `product.reference_photos` is empty because the export supplied none. "
    "Every prompt that needs one still carries its reference block and is paste-and-run — "
    "attach the product photo in the generation tool. `01-pain-scene` carries no product by "
    "design and needs nothing attached.",
    "AUTHENTICITY FENCE BREACHED, and it is a template defect rather than a routing one. The "
    "review block pairs each quote with a full name and a `Verified Buyer` label. "
    "`05-social-snapshot` forbids pairing a generated snapshot with a name, avatar, star row "
    "or verified badge — that is a fabricated endorsement. All six tiles ship with a blocking "
    "precondition on their own option: do not render until the block is de-attributed or real "
    "customer photographs are used. This is the sixth consecutive page carrying this defect.",
    "G6 AND THE LED COUNTER, recorded because the two rules that govern it do not agree. "
    "Reason 7 sells an LCD rep counter. G6's scope note admits diegetic text — a product's own "
    "readout is content, not overlay — but its production rule says screens are never "
    "model-drawn and are composited in post, and ADR-021 forbids compositing in this pipeline. "
    "Every option for that slot therefore renders the counter as a physical part with a DARK "
    "screen, and the number lives in the copy. The same conflict is why that slot's loop is "
    "refused. Worth an owner decision rather than a per-page workaround.",
    "PICKS: `feedback/picks.jsonl` holds no records, so Step 3's ≥20-pick tie-breaker never "
    "fired and no recommendation on this page is performance-backed. Every `recommended_opt` "
    "is a judgement from FIT, EVIDENCE and PROMPT RISK only.",
    "COVERAGE PASS (Step 5b): no additive proposals. For a solution-aware reader the rungs "
    "that matter are mechanism and physical proof, and the page already carries two mechanism "
    "images, a locked-frame comparison and a use sequence. The absent rung is a pain/"
    "amplification beat beyond the header, and Step 5b's own rule is that an absent rung is "
    "not automatically a gap — re-amplifying the problem to this reader is the thing the "
    "awareness ladder says not to do.",
]

# ---------------------------------------------------------------------------
# Emit
# ---------------------------------------------------------------------------


def md(d):
    L = [f"# Page {d['page_id']} — prompt options", ""]
    L.append(f"Session `{SESSION}` · channel `{d['channel']}` · awareness "
             f"`{d['awareness_stage']}` · registry {d['registry_version']}")
    L.append("")
    L.append("GENERATED FROM `prompts.json` by `build.py` — never hand-edit this file.")
    L.append("")
    L.append(f"Motion: {d['motion']['delivered']} loop(s) delivered against a floor of "
             f"{d['motion']['floor']} and a ceiling of {d['motion']['ceiling']}, margin "
             f"{d['motion']['margin']}.")
    L.append("")
    L.append("## Page composition notes")
    L.append("")
    for n in d["page_composition_notes"]:
        L.append(f"- {n}")
    L.append("")
    for s in d["slots"]:
        L.append(f"## `{s['slot_id']}` — {s['section_role']}")
        L.append("")
        if s.get("out_of_scope"):
            L.append(f"- placement: {s['placement']}")
            L.append(f"- **out of library scope** — {s['out_of_scope']}")
            L.append("")
            continue
        L.append(f"- asset: `{s['asset']}` · placement: {s['placement']}")
        L.append(f"- recommended: **{s['recommended_opt']}** · media "
                 f"`{s['recommended_media']}`")
        L.append(f"- basis: {s['recommendation_basis']}")
        L.append("")
        for o in s["options"]:
            L.append(f"### Option {o['opt']} — `{o['type']}`"
                     + (f" `--{o['variant']}`" if o.get("variant") else ""))
            L.append("")
            L.append(f"- varies on: {o['varies_on']}")
            L.append(f"- ratio `{o['ratio']}` · type version `{o['type_version']}` · "
                     f"pipeline `{o['pipeline']}`"
                     + (f" · attach the product photo"
                        if o["type"] not in NO_PHOTO else ""))
            if o.get("axes"):
                L.append(f"- axes: {json.dumps(o['axes'])}")
            L.append(f"- {o['rationale']}")
            if o.get("composition_notes"):
                L.append(f"- **note:** {o['composition_notes']}")
            if o.get("blocking_precondition"):
                L.append(f"- **{o['blocking_precondition']}**")
            L.append("")
            L.append("```")
            L.append(o["prompt"])
            L.append("")
            L.append(f"Strictly avoid: {o['avoid']}")
            L.append("```")
            L.append("")
        g = s["gif"]
        if g.get("eligible"):
            L.append(f"### GIF — `{g['type_id']}` ({g['form']})")
            L.append("")
            L.append(f"- form `{g['form']}` · rung `{g['rung']}` · kind `{g['kind']}` · "
                     f"reference folder: {g['refs']}")
            L.append(f"- plate `plates/{g['asset']}` — generated by `scripts/gen-plate.py`, "
                     f"production only, never a page asset")
            L.append("- the loop replaces the WHOLE slot asset, so its ratio is the slot's "
                     "own; the recommended still is complete and ships on its own (ADR-051)")
            L.append("")
            L.append("```")
            L.append(f"output: {g['output']}")
            L.append(f"ratio: {g['ratio']}")
            L.append(f"duration_s: {g['duration_s']}")
            L.append(f"loop: {g['loop']}")
            L.append("")
            L.append(f"brief: {g['brief']}")
            L.append("")
            L.append(f"alt: {g['alt']}")
            L.append(f"delivery: {g['delivery']}")
            L.append("```")
            L.append("")
        else:
            L.append(f"- **no gif** — {g['reason']}")
            L.append("")
    return "\n".join(L) + "\n"


json.dump(OUT, open(os.path.join(HERE, "prompts.json"), "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
open(os.path.join(HERE, "prompts.md"), "w", encoding="utf-8").write(md(OUT))

# ---------------------------------------------------------------------------
# Self-checks. Printed, so a clean result is never assumed. These FAIL the build.
# ---------------------------------------------------------------------------
errs = []


def section(slot_id):
    """ADR-050: prefix plus the next segment when that segment is a number."""
    p = slot_id.split(".")
    return f"{p[0]}.{p[1]}" if len(p) > 1 and p[1].isdigit() else p[0]


# 1 — every declared slot is routed, and nothing extra is invented
declared = set(DECLARED)
routed = {s["slot_id"] for s in SLOTS}
if declared != routed:
    errs.append(f"contract/routing mismatch: missing {sorted(declared - routed)}, "
                f"extra {sorted(routed - declared)}")

for s in SLOTS:
    sid = s["slot_id"]
    if s["section_role"] != DECLARED[sid]["role"]:
        errs.append(f"{sid}: role {s['section_role']} != contract "
                    f"{DECLARED[sid]['role']}")
    for o in s["options"]:
        # 2 — ratio legality, twice: ADR-016's five AND the type's own declared list
        if o["ratio"] not in LEGAL_RATIOS:
            errs.append(f"{sid} {o['opt']}: ratio {o['ratio']} outside ADR-016's five")
        if o["ratio"] not in TYPE_RATIOS[o["type"]]:
            errs.append(f"{sid} {o['opt']}: {o['type']} does not declare {o['ratio']}")
        if o["ratio"] != DECLARED[sid]["ratio"]:
            errs.append(f"{sid} {o['opt']}: ratio {o['ratio']} != contract "
                        f"{DECLARED[sid]['ratio']}")
        # 3 — ADR-021: single-pass or it is not deliverable
        if o["pipeline"] != "single-pass":
            errs.append(f"{sid} {o['opt']}: pipeline {o['pipeline']} breaches ADR-021")
        # 4 — a type that needs the photo carries a reference block
        needs = o["type"] not in NO_PHOTO
        has = "the exact reference" in o["prompt"]
        if needs and not has:
            errs.append(f"{sid} {o['opt']}: {o['type']} needs a reference block and "
                        f"the prompt carries none")
        if not needs and has:
            errs.append(f"{sid} {o['opt']}: {o['type']} takes no product photo but the "
                        f"prompt carries a reference block")
        # 5 — prompt budget
        if len(o["prompt"]) > CEIL[o["type"]]:
            errs.append(f"{sid} {o['opt']}: {len(o['prompt'])} chars over {o['type']}'s "
                        f"{CEIL[o['type']]} ceiling")
        # 6 — ADR-051: no still reserves an empty block for a loop any more
        if "empty reserved block" in o["prompt"] or "reserved block" in o["prompt"]:
            errs.append(f"{sid} {o['opt']}: reserves a block for a loop; ADR-051 retired "
                        f"that — the still ships on its own")

# 7 — one-type-once outside repeating sections
linear = [s for s in SLOTS if s.get("options") and not s["slot_id"].startswith("reviews.")]
picked = [o["type"] for s in linear for o in s["options"] if o["opt"] == "A"]
for t in sorted({t for t in picked if picked.count(t) > 1}):
    errs.append(f"one-type-once breached outside a repeating section: {t} x{picked.count(t)}")

# 8 — step-3 budget
BUDGET3 = {"03-mechanism-ghostbody", "03-spec-split", "03-use-sequence"}
n3 = len([t for t in picked if t in BUDGET3])
if n3 > 2:
    errs.append(f"step-3 budget: {n3} of {sorted(BUDGET3)} on one page, cap is 2")

# 9 — never_with
NEVER = {"01-pain-scene": ["01-pain-split"], "01-pain-split": ["01-pain-scene"],
         "03-mechanism-xray": ["03-spec-split"], "03-spec-explode": ["03-spec-split"]}
for t in picked:
    for other in NEVER.get(t, []):
        if other in picked:
            errs.append(f"never_with breached: {t} and {other}")

# 10 — attribute gates actually applied
for t in KILLED:
    if t in picked:
        errs.append(f"{t} is killed by an attribute gate but was routed")

# 11 — motion: delivered, margin, ceiling, per-section cap, adjacency
if MOTION["delivered"] != len(ELIG):
    errs.append(f"motion.delivered {MOTION['delivered']} != {len(ELIG)} eligible")
if MOTION["margin"] != len(ELIG) - MOTION["floor"]:
    errs.append(f"motion.margin {MOTION['margin']} != {len(ELIG) - MOTION['floor']}")
if len(ELIG) > MOTION["ceiling"]:
    errs.append("motion ceiling exceeded")
if len(ELIG) < MOTION["floor"] and not MOTION["shortfall_reason"]:
    errs.append("below the floor with no shortfall_reason")

SECTION_ITEMS = {"content.0": 1, "content.1": 5, "content.3": 2, "reviews": 6}
secs = {}
for s in ELIG:
    secs.setdefault(section(s["slot_id"]), []).append(s["slot_id"])
for sec, ids in secs.items():
    if len(ids) == 1:
        continue
    if len(ids) > 2 or SECTION_ITEMS.get(sec, 0) < 5:
        errs.append(f"section `{sec}` carries {len(ids)} loops against "
                    f"{SECTION_ITEMS.get(sec, 0)} items (ADR-032): {ids}")
    idx = sorted(int(re.findall(r"\.(\d+)\.", i)[-1]) for i in ids)
    if len(idx) == 2 and idx[1] - idx[0] < 2:
        errs.append(f"the two loops in `{sec}` are adjacent (items.{idx[0]} and "
                    f"items.{idx[1]}); ADR-032 needs a static item between them")

# 12 — no social-proof slot carries motion
for s in SLOTS:
    if s["section_role"] == "social-proof" and s["gif"].get("eligible"):
        errs.append(f"{s['slot_id']}: social-proof slots carry no motion")

# 13 — gif field completeness, the ADR-051 filename, and the brief band
GIF_FIELDS = ("form", "kind", "type_id", "rung", "ratio", "duration_s", "loop",
              "output", "delivery", "brief", "alt", "refs", "asset")
GIF_TYPES = {"use", "mechanism", "cause", "proof", "relief"}
for s in ELIG:
    g = s["gif"]
    for f in GIF_FIELDS:
        if not g.get(f):
            errs.append(f"{s['slot_id']} gif: missing `{f}`")
    if g.get("form") != "whole-frame":
        errs.append(f"{s['slot_id']} gif: form `{g.get('form')}` — ADR-051 leaves only "
                    f"whole-frame")
    if g.get("type_id") not in GIF_TYPES:
        errs.append(f"{s['slot_id']} gif: type_id `{g.get('type_id')}` not a routable type")
    if g.get("kind") != g.get("type_id"):
        errs.append(f"{s['slot_id']} gif: kind `{g.get('kind')}` != type_id "
                    f"`{g.get('type_id')}` — ADR-051 leaves no layer-bound loops")
    want = gif_name(s["slot_id"])
    if g.get("output") != want:
        errs.append(f"{s['slot_id']} gif: output `{g.get('output')}` != `{want}`")
    if g.get("ratio") != DECLARED[s["slot_id"]]["ratio"]:
        errs.append(f"{s['slot_id']} gif: ratio {g.get('ratio')} != the slot's "
                    f"{DECLARED[s['slot_id']]['ratio']} — a whole-frame loop owes the "
                    f"page's shape")
    w = len(g.get("brief", "").split())
    if not 25 <= w <= 55:
        errs.append(f"{s['slot_id']} gif: brief is {w} words, band is 25-55 (G12)")
    if "mp4" not in g.get("delivery", ""):
        errs.append(f"{s['slot_id']} gif: delivery does not name mp4")

# 14 — G12: no craft vocabulary in a brief, and no register/light talk (ADR-030)
CRAFT = ("bokeh", "grade", "colour grade", "color grade", "register", "key light",
         "rim light", "high-key", "low-key", "depth of field", "focal length", "f-stop")
for s in ELIG:
    low = (s["gif"]["brief"] + " " + s["gif"]["alt"]).lower()
    for w in CRAFT:
        if w in low:
            errs.append(f"{s['slot_id']} gif: brief or alt uses craft word `{w}` (G12)")

# 15 — recommendation_basis figures agree with the prompts they describe
for s in SLOTS:
    if not s.get("recommendation_basis") or not s.get("options"):
        continue
    nums = [int(x) for x in re.findall(r"\b(\d{3,4})\b/(?=\d)", s["recommendation_basis"])]
    stated = re.search(r"(\d{3,4})/(\d{3,4})/(\d{3,4}) characters",
                       s["recommendation_basis"])
    if stated:
        got = [int(x) for x in stated.groups()]
        real = [len(o["prompt"]) for o in s["options"]]
        if got != real:
            errs.append(f"{s['slot_id']}: basis says {got}, prompts are {real}")

# 16 — the blocking precondition is on every review tile and nowhere else
for s in SLOTS:
    for o in s["options"]:
        blocked = bool(o.get("blocking_precondition"))
        is_tile = s["slot_id"].startswith("reviews.")
        if is_tile != blocked:
            errs.append(f"{s['slot_id']} {o['opt']}: blocking precondition "
                        f"{'missing' if is_tile else 'unexpected'}")

# 17 — reserves name a real primary in the same section
for r in MOTION["reserves"]:
    if r["slot_id"] not in routed:
        errs.append(f"reserve {r['slot_id']} is not a slot on this page")
    if r["substitutes_for"] not in {s["slot_id"] for s in ELIG}:
        errs.append(f"reserve {r['slot_id']} substitutes for a slot that carries no loop")
    if section(r["slot_id"]) != section(r["substitutes_for"]):
        errs.append(f"reserve {r['slot_id']} is not in its primary's section")

print(f"{SESSION}: {len(SLOTS)} slots "
      f"({len([s for s in SLOTS if s.get('options')])} routed, "
      f"{len([s for s in SLOTS if s.get('out_of_scope')])} out of scope), "
      f"{sum(len(s['options']) for s in SLOTS)} options, "
      f"{len(ELIG)} loop(s), margin {MOTION['margin']}")
print(f"types: {', '.join(sorted(set(picked)))}")
print(f"gates killed: {', '.join(KILLED) or 'none'}")
print(f"sections carrying loops: "
      f"{ {k: len(v) for k, v in sorted(secs.items())} }")
if errs:
    print(f"\nSELF-CHECK FAILED — {len(errs)} error(s):")
    for e in errs:
        print("  -", e)
    sys.exit(1)
print("self-checks: 17 checks, 0 errors")

#!/usr/bin/env python3
"""Build prompts.json and prompts.md for page 65 — handheld UV mattress vacuum.

prompts.json is the source of truth (query/output.schema.json); prompts.md is
generated from it and is never hand-edited (query/runbook.md Step 7).

Run from anywhere:  python3 query/sessions/65-.../build.py
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAGE = "65"


def _index_types():
    """requires_product_photo and generation_mode, read from the generated
    index rather than retyped. The flag is TYPE-level; variants override it and
    the disagreements are printed in the self-checks."""
    out, tid = {}, None
    with open(os.path.join(ROOT, "registry", "index.yaml"), encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            m = re.match(r"^  - id: (\S+)", line)
            if m:
                tid = m.group(1)
                out[tid] = {}
            elif tid and re.match(r"^    \w+:", line):
                k, _, v = line.strip().partition(": ")
                out[tid][k] = {"true": True, "false": False}.get(v, v)
    return out


TYPES = _index_types()

# The contract this page was routed against. Until now content.json was a
# document nobody read: the routing lived in this script's head and the two
# could drift with nothing to notice. Everything below is checked against it.
CONTRACT = json.load(open(os.path.join(HERE, "content.json"), encoding="utf-8"))
ATTRS = CONTRACT["product"]["attributes"]
DECLARED = {sl["slot_id"]: {"ratio": sl["ratio"], "role": sec["role"]}
            for sec in CONTRACT["page"]["sections"]
            for sl in sec["image_slots"]}

# mapping/slot-rules.md, "Attribute gates (deterministic kill-rules)". Written
# as data so the emitted routing can be checked against them rather than
# trusted. Each entry: (condition on ATTRS, type it kills, the rule's own words).
ATTRIBUTE_GATES = [
    (lambda a: a["symptom_visibility"] == "invisible", "01-pain-split",
     "symptom_visibility: invisible drops 01-pain-split"),
    (lambda a: a["body_contact"] is False, "03-mechanism-ghostbody",
     "body_contact: false drops 03-mechanism-ghostbody; mechanism falls to xray"),
    (lambda a: a["result_visibility"] == "invisible", "06-relief-scene",
     "result_visibility: invisible drops 06-relief-scene, close with relief-hero"),
    (lambda a: a["multi_step_usage"] is False, "03-use-sequence",
     "multi_step_usage: false drops 03-use-sequence unless buyers assume "
     "complexity"),
]
KILLED = {tid: why for cond, tid, why in ATTRIBUTE_GATES if cond(ATTRS)}

# Per-type prompt ceilings, each taken from that type's own SLOT CONSTRAINTS.
CEIL = {"01-pain-scene": 2500, "02-cause-anatomy": 1800, "03-mechanism-xray": 1900,
        "04-proof-lockedframe": 1800, "05-social-snapshot": 1800,
        "05-social-handoff": 1800, "06-relief-hero": 2300}

# ---------------------------------------------------------------------------
# Page-level notes
# ---------------------------------------------------------------------------

GAP_RATIO = (
    "THE TEMPLATE ASKS FOR A RATIO THE LIBRARY BARELY HAS. Seven body slots - "
    "reasons.items.0 to 4 and reasons_b.items.0 to 1 - carry class "
    "`aspect-[4/3] object-cover`, and only TWO types in the whole registry "
    "declare 4:3: 05-social-snapshot and 06-relief-scene. Every other type "
    "legally declares 16:9 and 1:1 (ADR-016 rules out the 5:3, 4:5 and 3:2 "
    "several of them still carry). Routing those seven slots by ratio would "
    "have left five of them empty, so they are routed by ARGUMENT and rendered "
    "at the chosen type's own declared ratio, and the layout centre-crops. "
    "Which declared ratio is picked follows the geometry: 16:9 cropped to 4:3 "
    "removes 25% of the WIDTH, 1:1 cropped to 4:3 removes 25% of the HEIGHT, "
    "so a composition that runs left to right takes 1:1 (every panel loses the "
    "same band) and a centred subject takes 16:9 (the crop eats margin). Each "
    "option's note says what its own crop costs. The real fix is ADR-016's "
    "standing RATIO sweep, which is a type-file edit and not a query session's "
    "work - or one line of template CSS, since hero.image already carries no "
    "aspect class at all.")

GAP_INSET = (
    "A CORNER LAYER CANNOT SURVIVE A CENTRE-CROP, and two recommended options "
    "carry one. 06-relief-hero's --detail and --recall insets sit at a corner "
    "by law, and reasons.items.3 and reasons_b.items.0 are both 4:3-cropped "
    "slots, so roughly 12.5% off the top and bottom of a 1:1 render goes. G10 "
    "already requires a layer held clear of the frame edge and the prompts say "
    "so, but clear of the RENDERED edge is not clear of the CROPPED edge. "
    "Setting those two slots to `aspect-square`, which reviews.photos already "
    "uses, removes the problem outright. Until then, check the inset survives "
    "before the asset ships.")

GAP_ATTACH = (
    "The reference photo is yours to upload, and 39 prompts want it. The export "
    "carries imageBriefs: null and sourceRefs.shopifyProductGid: null, so there "
    "is no product photograph in it and nothing to hash - attachments is "
    "omitted from every option rather than filled with an invented sha256 "
    "(SPEC 6.4). That is a gap in the EXPORT, not a blocked prompt (ADR-021): "
    "each of those prompts keeps its G1 reference block, so pasting it and "
    "uploading the photo runs it as written.")

GAP_REVIEWS = (
    "THE REVIEWS BLOCK BREAKS 05-social-snapshot's AUTHENTICITY FENCE AS THE "
    "PAGE IS BUILT. All six photo slots sit inside the same <section "
    "data-block-key=\"reviews\"> as six quotes, each carrying a five-star row, "
    "a named attribution and a green Verified label. The type's avoid_when is "
    "explicit: NEVER pair a generated snapshot with a reviewer name, avatar, "
    "star row or verified badge, and never present one as an actual customer "
    "upload - that is a fabricated endorsement. Eighteen prompts are written "
    "and every one of them carries the same precondition. Three ways out, in "
    "the owner's order of preference: use real customer photographs, which "
    "always win over generated ones; or move the photo grid out of the "
    "attributed block; or drop the names, stars and verified labels from that "
    "block.")

GAP_CHANNEL = (
    "lpTypeId is `listicle`, which does not exist in this library. "
    "registry/vocabulary.yaml declares four channels and mapping/slot-rules.md "
    "has four columns; listicle is none of them. Routed as `advertorial` on the "
    "page's own evidence rather than by guess: a bylined author with a "
    "credential line, an About-the-author bio, a seven-comment thread with "
    "names, a disclosure line and editorial footer navigation. A listicle is an "
    "advertorial format, not a fifth channel. If listicles keep arriving, the "
    "decision to record is whether the vocabulary gains an alias or a column - "
    "that is a shared-file change and it is not made here.")

GAP_HEAT = (
    "The heat claim cannot be photographed and reasons.items.3 is built on it. "
    "149F is invisible in every register this library has, and G8 forbids "
    "inventing an emission so a render looks alive. The recommended option "
    "argues the half of that section a camera can hold - the head sealed "
    "against the fabric and the debris leaving it - and leaves the thermal half "
    "to the copy. It is not proof of heat and is not presented as any. Same "
    "shape as the noise claim on page 58.")

GAP_CLAIMS = (
    "brief.rawFeatures warns that the page outruns its own evidence, and no "
    "image here follows it there. The brief states plainly that mattress "
    "vacuuming has limited effect on total allergen load on its own, that the "
    "99.9 percent figure needs the manufacturer's test data because UV dose "
    "depends on dwell time, and that UV-C is harmful to eyes and skin with the "
    "lift-off cut-out unconfirmed. So no option asserts a kill rate, a "
    "percentage, a sterilisation claim or a health outcome. What the images "
    "argue is mechanical and visible: debris leaves the weave, particles stay "
    "in the chamber, the indicator reads the surface.")

GAP_ARC = (
    "The page argument does not run in library order and the copy is why. "
    "reasons_b sits after the comparison table, so the arc lands as cause, "
    "pain, proof, mechanism, social, outcome, mechanism - with a mechanism beat "
    "last. Reordering the sections is a copy decision, not an image one, and "
    "the routing follows the page as written rather than quietly arguing with "
    "it. Pain still precedes relief, which is the cross-slot rule that binds.")

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

HERO_A = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Woman early 40s, in a creased cotton sleep t-shirt, sitting on the edge of an
unmade bed first thing in the morning, mid-way through pressing the heels of
both hands up into her eye sockets and dragging them outward across the
cheekbones. Under that force: shoulders hunched forward over her knees, elbows
braced on her thighs, head tipped down into her hands.
Face: eyes screwed shut under the heels of her hands, mouth open to breathe,
nostrils drawn.

[EVIDENCE]
Both eyelids are swollen and pink-rimmed with the lashes stuck wet together,
the skin from the inner corners down across the cheekbones raw and shiny where
it has been rubbed, and the nostrils and upper lip are chapped red. A wad of
used tissues is pushed into the sheet beside her hip.

[ENVIRONMENT]
An ordinary bedroom, just after waking, curtains half open. Lived-in clutter
belonging to that place: a water glass and a blister strip of tablets on the
nightstand, yesterday's clothes over a chair back, a phone face down on the
duvet, one slipper under the bed. Nothing arranged, nothing removed to tidy the
frame.

[GAZE] unaware of the camera, eyes shut behind her own hands.

[LIGHT] low-key. Key: thin grey daylight through the gap in the curtains, hard
and cold across her face. Fill: the dim of the unlit room. Rim light along the
shoulder and the top of the forearms. Deep shadow across most of the frame.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

HERO_B = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man late 30s in a stretched t-shirt and pyjama bottoms, kneeling on the carpet
beside a child's low bed in the small hours, mid-way through catching his young
daughter's wrist to stop her nails going back into the crook of her own elbow.
Under that force: his weight forward on one knee, both hands closed round her
forearm, her arm pulling against him.
Face: jaw set, brows drawn together, eyes down on her arm.

[EVIDENCE]
The inside of her elbow is broken out in raw scratched patches, the skin lifted
and weeping in two places with dried flakes caught on the pyjama cuff, and
short parallel scratch lines run down the forearm below it.

[ENVIRONMENT]
A small child's bedroom in the middle of the night. Lived-in clutter belonging
to that place: a tub of emollient cream open on the floor with its lid beside
it, a soft toy fallen half out of the bed, a nightlight low on the skirting, a
laundry pile by the door. Nothing arranged, nothing removed to tidy the frame.

[GAZE] unaware of the camera, gaze down on the child's arm.

[LIGHT] low-key. Key: the nightlight low and to one side, warm and weak. Fill:
landing light through the part-open door behind him. Rim light along his
shoulder and the child's hair. Deep shadow across most of the frame.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

HERO_C = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Woman early 40s in a creased sleep t-shirt, standing at the foot of a stripped
bed early in the morning, mid-way through shaking a folded sheet out flat over
the bare mattress, both arms thrown wide and the fabric still lifting.
Under that force: weight on the balls of the feet, shoulders pulled up and
back, the sheet snapping away from her hands.
Face: turned aside away from the bed, eyes narrowed, mouth pressed shut.

[EVIDENCE]
A dense cloud of fine dust has burst up out of the mattress into the shaft of
daylight and hangs there, thick enough to read against the dark of the room,
with a haze of it settling back onto the bare ticking below.

[ENVIRONMENT]
An ordinary bedroom, early morning, one curtain pulled back. Lived-in clutter
belonging to that place: a laundry basket of bedding on the floor, a radiator
with a towel over it, a water glass on the nightstand, a bin under the window.
Nothing arranged, nothing removed to tidy the frame.

[GAZE] unaware of the camera, face turned away from the dust.

[LIGHT] low-key. Key: one hard shaft of morning daylight through the open
curtain, raking across the bed and lighting the airborne dust. Fill: the dim of
the unlit room. Rim light along her forearms. Deep shadow across most of the
frame.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

CAUSE_A = """TYPE: 02-cause-anatomy v1.15
MEDIUM: 2D illustration, flat-vector. NOT photography, NOT 3D.

[PRODUCT REFERENCE] the attached photo is the exact reference for the handheld
unit in the RIGHT panel.

[FRAME] a woman kneeling on a bed working a cleaning head across the mattress,
the whole bed and figure in shot, the head small within it and the mattress cut
open in section beneath.
[GROUND] deep desaturated indigo, the right half one step lighter than the left.
[BODY] the mattress in section - woven ticking over a batting layer - cut as
flat layers in warm ivory on a translucent outline. NOT a skeleton, NOT a human
figure. Exactly one bed and one figure in EACH panel,
same scale and view.

[PANELS]
LEFT: an ordinary upright vacuum's wide floor head, drawn realistically and
unbranded, pressed flat on the ticking; only the loose debris lying on top of
the weave is gone, and the dark grains bound down in the batting stay where
they are.
RIGHT: the reference handheld unit at the same place on the same mattress, its
head tapping the ticking so the weave lifts, and the same dark grains rising out
of the batting into the intake. The batting layer and its grains appear in both
panels and neither head covers them.

[MARKS], two, nothing else marked:
- measure: two dashed straight lines, one per panel, each PERPENDICULAR TO THE
  TICKING, running from the top of the ticking down to the deepest grain still
  in the batting and STOPPING at both. Both begin at the same point in
  their panel. Identical thickness and dash. One property differs: the length -
  long left, closed to almost nothing right. Red left, blue right. Straight
  lines, not boxes.
- verdict: filled solid discs, red with a white X in the left panel's TOP
  corner, green with a white check in the right panel's. Same diameter, not
  rings.

G3: red wrong, blue correct, green badge, nothing else."""

CAUSE_B = """TYPE: 02-cause-anatomy v1.15
MEDIUM: 2D illustration, airbrushed. NOT photography, NOT 3D.

[PRODUCT REFERENCE] the attached photo is the exact reference for the handheld
unit in the RIGHT panel.

[FRAME] a woman kneeling on a bed working a cleaning head across the mattress,
the whole bed and figure in shot, the head small within it and the mattress cut
open in section beneath.
[GROUND] deep desaturated indigo, the right half one step lighter than the left.
[BODY] the mattress in section - woven ticking over a batting layer - modelled
in warm ivory with soft gradients on a translucent outline. NOT a skeleton, NOT
a human figure. Exactly one bed and one figure in EACH panel,
same scale and view.

[PANELS]
LEFT: an ordinary upright vacuum's wide floor head, drawn realistically and
unbranded, pressed flat on the ticking; only the loose debris lying on top of
the weave is gone, and the dark grains bound down in the batting stay where
they are.
RIGHT: the reference handheld unit at the same place on the same mattress, its
head tapping the ticking so the weave lifts, and the same dark grains rising out
of the batting into the intake. The batting layer and its grains appear in both
panels and neither head covers them.

[MARKS], two, nothing else marked:
- measure: two dashed straight lines, one per panel, each PERPENDICULAR TO THE
  TICKING, running from the top of the ticking down to the deepest grain still
  in the batting and STOPPING at both. Both begin at the same point in
  their panel. Identical thickness and dash. One property differs: the length -
  long left, closed to almost nothing right. Red left, blue right. Straight
  lines, not boxes.
- verdict: filled solid discs, red with a white X in the left panel's TOP
  corner, green with a white check in the right panel's. Same diameter, not
  rings.

G3: red wrong, blue correct, green badge, nothing else."""

CAUSE_C = """TYPE: 02-cause-anatomy v1.15
MEDIUM: 2D illustration, flat-vector. NOT photography, NOT 3D.

[PRODUCT REFERENCE] the attached photo is the exact reference for the handheld
unit in the RIGHT panel.

[FRAME] a woman sitting on the edge of a bed working a cleaning head over a
pillow held flat on her lap, the whole figure and pillow in shot, the head small
within it and the pillow cut open in section beneath.
[GROUND] deep desaturated indigo, the right half one step lighter than the left.
[BODY] the pillow in section - woven cover over a fibre core - cut as flat
layers in warm ivory on a translucent outline. NOT a skeleton, NOT a human
figure. Exactly one pillow and one figure per panel, same scale
and view.

[PANELS]
LEFT: an ordinary upright vacuum's wide floor head, drawn realistically and
unbranded, pressed flat on the cover; the loose debris on top of the weave is gone and the
dark grains bound down in the fibre core stay where they are.
RIGHT: the reference handheld unit at the same place on the same pillow, its
head tapping the cover so the weave lifts, and the same dark grains rising out
of the core into the intake. The fibre core and its grains appear in both panels
and neither head covers them.

[MARKS], two, nothing else marked:
- measure: two dashed straight lines, one per panel, each PERPENDICULAR TO THE
  COVER, running from the top of the cover down to the deepest grain still in
  the core and STOPPING at both. Both begin at the same point in
  their panel. Identical thickness and dash. One
  property differs: the length - long on the left, closed to almost nothing on
  the right. Red left, blue right. Straight lines, not boxes.
- verdict: filled solid discs, red with a white X in the left panel's TOP
  corner, green with a white check in the right panel's. Same diameter, not
  rings.

G3: red wrong, blue correct, green badge, nothing else."""

SHEETS_A = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
No person in frame. The force is the weight of the bedding itself: a folded
stack of laundered sheets set down on the corner of a bed that has just been
stripped, the top sheet still creased from the airer, the pile leaning where it
was put down one-handed and not straightened.

[EVIDENCE]
The bare mattress is uncovered across the whole bed, and the ticking carries a
body-shaped stain of grey-yellow discolouration deepest where the hips and
shoulders lie, its edge soft and unmistakable. Loose fibre and grit have
gathered along the piped seam and in the buttoned dimples, and one seam is
frayed open where the dust sits thickest.

[ENVIRONMENT]
An ordinary bedroom in the middle of a weekday morning, the window open behind
it. Lived-in clutter belonging to that place: the stripped duvet bundled on the
floor, a laundry basket on its side by the door, a mug left on the nightstand,
the mattress protector balled at the foot of the bed. Nothing arranged, nothing
removed to tidy the frame.

[GAZE] no subject, so no gaze. The frame looks down the length of the bed from
standing height, the way the person who stripped it is looking at it.

[LIGHT] low-key. Key: flat overcast daylight from the window along one side of
the bed, cold and even. Fill: the dim of the room. Rim light along the folded
edge of the clean sheets. Deep shadow across the far half of the frame.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

SHEETS_B = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Woman early 40s in a t-shirt and leggings, leaning across a bed mid-way through
dragging a laundered fitted sheet down over the near corner of the mattress,
both hands stretching the elastic under the edge. Under that force: her weight
on one knee on the mattress, both arms extended, the sheet pulled taut and
lifting off the ticking along its length.
Face: eyes down on the corner she is fitting, mouth shut, cheek slack.

[EVIDENCE]
Where the clean sheet has not yet reached, the bare ticking shows a body-shaped
stain of grey-yellow discolouration deepest at the hips and shoulders, with
loose fibre and grit gathered along the piped seam beside her knee.

[ENVIRONMENT]
An ordinary bedroom in the middle of a weekday morning. Lived-in clutter
belonging to that place: the stripped duvet bundled on the floor, a laundry
basket on its side by the door, a mug left on the nightstand, a pillow without
its case on the chair. Nothing arranged, nothing removed to tidy the frame.

[GAZE] unaware of the camera, gaze down on the corner of the mattress.

[LIGHT] low-key. Key: flat overcast daylight from the window along one side of
the bed, cold and even. Fill: the dim of the room. Rim light along her forearm
and the pulled edge of the sheet. Deep shadow across the far half of the frame.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

SHEETS_C = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
No person in frame. The force is a night's weight already spent: two pillows
stripped of their cases and left where they were pulled, one folded over on
itself against the headboard and the other flat and dented in the middle, both
still holding the shape of a head.

[EVIDENCE]
The bare pillow ticking is discoloured in a wide grey-yellow ring around the
dent where the head lies, the fabric there thinned and slightly shiny, with
loose fibre and fine grit caught along the piped seam and a scatter of it on
the sheet below.

[ENVIRONMENT]
An ordinary bedroom, mid-morning, curtains open. Lived-in clutter belonging to
that place: the pillowcases dropped on the floor beside the bed, a book face
down on the nightstand, a phone charger trailing over the headboard, a glass
half full of water. Nothing arranged, nothing removed to tidy the frame.

[GAZE] no subject, so no gaze. The frame looks down at the pillows from
standing height at the side of the bed.

[LIGHT] low-key. Key: flat overcast daylight from the window across the head of
the bed, cold and even. Fill: the dim of the room. Rim light along the folded
edge of the near pillow. Deep shadow across the foot of the frame.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

AIR_A = """TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 2 equal vertical panels, thin white gutter, no outer border.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit in the RIGHT
panel. Preserve shape, proportions, material, finish and colour exactly.

[SCENE - the same in both]
The same corner of the same bedroom, the same double bed stripped to bare ticking,
the same curtain pulled back on the same window, a nightstand with a lamp on it.
One hard shaft of morning daylight crosses the room above the bed in both.

[FRAMING]
One person photographed this twice from where they were standing, phone level
with the top of the mattress, the bed filling the lower two thirds and the lit shaft
of air across the upper third. It reads as one shot taken twice, never two. Light differs only in exposure, never in warmth.

[THE VARIABLE]
What is being run over the mattress, and what the shaft of light shows above it.
Both panels at the same moment: the machine mid-pass, halfway down the bed.
LEFT - an ordinary upright vacuum, unbranded, its wide head on the ticking and
its body on the floor; the shaft of light above
the bed is thick with fine motes turning in it.
RIGHT - the reference handheld unit at the same place on the same mattress, one
cable to the wall; the same shaft of light is empty and clean, the beam edge
sharp against the dark of the room.

[GRADE - the same in both]
Neutral, from the overcast window and the pale ticking rather than a filter.
Still colour, never black and white.

Both panels get the same exposure, tidiness and framing; the ordinary vacuum is
an object someone would own, never made to look worse."""

AIR_B = """TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit in the LAST
panel. Preserve shape, proportions, material, finish and colour exactly.

[SCENE - the same in all three]
The same corner of the same bedroom, the same double bed stripped to bare ticking,
the same curtain pulled back on the same window, a nightstand with a lamp on it.
One hard shaft of morning daylight crosses the room above the bed in every one.

[FRAMING]
One person photographed this three times from where they were standing, phone
level with the top of the mattress, the bed filling the lower two thirds and the lit
shaft of air across the upper third. It reads as one shot taken three times,
never three. Light differs only in exposure, never in warmth.

[THE VARIABLE]
What is being run over the mattress, and what the shaft of light shows above it.
Every panel at the same moment: the machine mid-pass, halfway down the bed.
1 - an ordinary upright vacuum, unbranded, its wide head on the ticking; the
shaft above the bed thick with fine motes turning in it.
2 - a small basic handheld cleaner, unbranded, on the same spot; the shaft
thinner but still drifting with motes.
3 - the reference handheld unit at the same place, one cable to the wall; the
same shaft empty, its beam edge sharp against the dark of the room.

[GRADE - the same in all three]
Neutral, from the overcast window and the pale ticking rather than a filter.
Still colour, never black and white.

Panels one and two get the same exposure, tidiness and framing as panel three;
the alternatives are ordinary products someone would buy, never made to look
worse."""

AIR_C = """TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 2 equal vertical panels, thin white gutter, no outer border.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit in the RIGHT
panel. Preserve shape, proportions, material, finish and colour exactly.

[SCENE - the same in both]
The same corner of the same living room, the same dark grey fabric sofa with its
cushions in place, the same lamp lit behind it, the same window with the blind
half down. One shaft of low afternoon daylight crosses the room above the sofa
arm in both.

[FRAMING]
One person photographed this twice from where they were standing, phone level
with the top of the sofa back, the seat filling the lower two thirds and the lit shaft
of air across the upper third. It reads as one shot taken twice, never two. Light differs only in exposure, never in warmth.

[THE VARIABLE]
What is being run over the sofa seat, and what the shaft of light shows above
it. Both panels at the same moment: the machine mid-pass across the near
cushion.
LEFT - an ordinary upright vacuum, unbranded, its crevice tool dragged across the
fabric and its body on the floor; the shaft of light
above the sofa thick with fine motes turning in it.
RIGHT - the reference handheld unit at the same place on the same cushion, one
cable to the wall; the same shaft of light empty and clean, the beam edge sharp
against the dark of the room.

[GRADE - the same in both]
Neutral, from the window and the grey fabric rather than a filter. Still colour,
never black and white.

Both panels get the same exposure, tidiness and framing; the ordinary vacuum is
an object someone would own, never made to look worse."""

CONTACT_A = """TYPE: 06-relief-hero v1.15
REGISTER: commercial. Professional camera, controlled light, deliberate negative
space on one side.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit, identical in
every layer. Preserve shape, proportions, material, finish and colour exactly.

[SUBJECT] a woman in her forties in a plain long-sleeved top, kneeling on the
floor beside a low double bed, both hands on the handle of the unit.
[POSE] mid-action: the unit pressed down flat on the bare mattress and pushed
away from her along the ticking, hands engaged, gaze on the head where it meets
the fabric, focused rather than smiling. She kneels beside the bed with the
whole unit between her and the mattress surface, so the contact is never hidden
by her own body.
[SETTING] one real bedroom filled to the edges: a nightstand with a lamp and a
water glass, a chair with clothes over the back, a laundry basket, a radiator
under the window, a rug half under the bed, a door standing open onto a landing.
Background blurred but never blank. None of these objects carries printed text.
[LIGHT] soft even window light from the left, background blurred, high-key.
[OFFSET] she kneels to the right of frame; the inset occupies the space on the
left that she is offset from, taking about three quarters of it.

In the upper left corner sits a rounded rectangle about 20 percent of the frame
width, its outline finishing a clear margin short of the picture on both sides.
Inside it, one magnified view the scene cannot show: the underside edge
of the same unit sealed flat against the woven ticking, the fabric drawn up
slightly into the intake slot and a fine grey debris rising off the weave into
it. Same photographic register as the hero, same light quality, same
resolution. It sits near the unit in the scene, linked by proximity alone - no
arrow, no glow, no border light.

No text anywhere in the image. No badge, no arrow, no percentage."""

CONTACT_B = """TYPE: 06-relief-hero v1.15
REGISTER: commercial. Professional camera, controlled light, deliberate negative
space on one side.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit, identical in
every layer. Preserve shape, proportions, material, finish and colour exactly.

[SUBJECT] a woman in her forties in a plain long-sleeved top, kneeling on the
floor beside a low double bed, both hands on the handle of the unit.
[POSE] mid-action: the unit pressed down flat on the bare mattress and pushed
away from her along the ticking, hands engaged, gaze on the head where it meets
the fabric, focused rather than smiling. She kneels beside the bed with the
whole unit between her and the mattress surface, so the contact is never hidden
by her own body.
[SETTING] one real bedroom filled to the edges: a nightstand with a lamp and a
water glass, a chair with clothes over the back, a laundry basket, a radiator
under the window, a rug half under the bed, a door standing open onto a landing.
Background blurred but never blank. None of these objects carries printed text.
[LIGHT] soft even window light from the left, background blurred, high-key.
[OFFSET] she kneels to the right of frame; the inset occupies the space on the
left that she is offset from, taking about three quarters of it.

In the upper left corner sits a rounded rectangle about 20 percent of the frame
width, its outline finishing a clear margin short of the picture on both sides.
Inside it, one magnified view the scene cannot show: the same unit's
transparent dust chamber seen from the side, a deep bed of fine grey powder and
matted fibre packed against the clear wall from the bottom up. Same photographic
register as the hero, same light quality, same resolution. It sits near the unit
in the scene, linked by proximity alone - no arrow, no glow, no border light.

No text anywhere in the image. No badge, no arrow, no percentage."""

CONTACT_C = """TYPE: 06-relief-hero v1.15
REGISTER: commercial. Professional camera, controlled light, deliberate negative
space on one side.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit, identical in
every layer. Preserve shape, proportions, material, finish and colour exactly.

[SUBJECT] reduced: present only as two forearms in pushed-up sleeves and the
hands closed round the handle of the unit. No face and no shoulders in frame.
[POSE] mid-action: the unit pressed down flat on the bare mattress and pushed
away along the ticking. What makes worked fabric different from unworked fabric
is visible in the same frame - behind the head the ticking is even and matt,
ahead of it the weave still carries a dulled grey film and loose fibre caught in
the seam, and the boundary between the two runs straight across the bed where
the head has reached.
[SETTING] one real bedroom filled to the edges: a nightstand with a lamp and a
water glass, a chair with clothes over the back, a laundry basket, a radiator
under the window, a rug half under the bed. Background blurred but never blank.
None of these objects carries printed text.
[LIGHT] soft even window light from the left, raking low across the ticking so
the worked and unworked halves separate. Background blurred, high-key.
[OFFSET] the hands and the unit sit to the right of frame; the inset occupies
the space on the left, taking about three quarters of it.

In the upper left corner sits a rounded rectangle about 20 percent of the frame
width, its outline finishing a clear margin short of the picture on both sides.
Inside it, one magnified view the scene cannot show: the underside edge
of the same unit sealed flat against the woven ticking, the fabric drawn up
slightly into the intake slot. Same photographic register as the hero, same
light quality, same resolution. Linked by proximity alone - no arrow, no glow.

No text anywhere in the image. No badge, no arrow, no percentage."""

INDICATOR_A = """TYPE: 05-social-handoff v2.5

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit. Preserve shape,
proportions, material, finish and colour exactly.

[MOMENT] the unit has just this moment finished a pass and is set down flat on
the bare mattress, still held. Its indicator window on the top of the handle is
lit a clear blue, and its transparent dust chamber is packed with fine grey
powder and matted fibre. Behind the head the ticking reads even and matt; ahead
of it the weave still carries a dulled film, and the boundary runs straight
across the bed.

[ADVOCATE] a woman in her forties in a long-sleeved top, kneeling at the side of
the bed with one hand still resting on the handle, her body at rest and her eyes
up on the other person rather than on the unit.

[LISTENER] a man of similar age standing at the foot of the bed, seen from
behind and to the side so his face is not visible, leaning in with his attention
on the dust chamber.

[PRODUCT] the unit is the largest and clearest object in the frame and nothing
beside it competes for the first glance; the bedding is pale and plain, and no
other appliance is in shot.

[ENVIRONMENT] an ordinary bedroom on a weekend morning with a real reason both
people are there - the bed is stripped, the duvet is bundled on the floor and a
laundry basket stands by the door. Ambient household light only, from the window
behind them.

REGISTER: candid documentary photograph, natural, unposed, sharp. No text, no
badge, no arrow anywhere in the image."""

INDICATOR_B = """TYPE: 05-social-handoff v2.5

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit. Preserve shape,
proportions, material, finish and colour exactly.

[MOMENT] the unit's transparent dust chamber has just been lifted off the body
and is being held up level between the two people, packed to the brim with fine
grey powder and matted grey fibre, the powder settled in a dense flat bed. The
unit itself sits on the bare mattress below with its indicator window lit blue.

[ADVOCATE] a woman in her forties in a long-sleeved top, kneeling at the side of
the bed holding the chamber up in one hand, her arm at rest and her eyes up on
the other person rather than on the chamber.

[LISTENER] a man of similar age crouched beside her, seen from behind and to the
side so his face is not visible, leaning in with his attention on the powder
inside the chamber.

[PRODUCT] the unit and its chamber are the largest and clearest objects in the
frame and nothing beside them competes for the first glance; the bedding is pale
and plain, and no other appliance is in shot.

[ENVIRONMENT] an ordinary bedroom on a weekend morning with a real reason both
people are there - the bed is stripped, the duvet is bundled on the floor and a
laundry basket stands by the door. Ambient household light only, from the window
behind them.

REGISTER: candid documentary photograph, natural, unposed, sharp. No text, no
badge, no arrow anywhere in the image."""

INDICATOR_C = """TYPE: 05-social-handoff v2.5

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit. Preserve shape,
proportions, material, finish and colour exactly.

[MOMENT] the unit has just this moment finished a pass along the seat of a dark
fabric sofa and is set down flat on the cushion, still held. Its indicator
window on the top of the handle is lit a clear blue, and its transparent dust
chamber holds a thick mat of grey fibre and pet hair. Behind the head the
cushion nap lies even and dark; ahead of it the fabric is still greyed with
settled hair, and the boundary runs straight across the cushion.

[ADVOCATE] a man in his fifties in a work shirt with the sleeves rolled, sitting
back on his heels beside the sofa with one hand still on the handle, his body at
rest and his eyes up on the other person rather than on the unit.

[LISTENER] a woman of similar age standing beside the sofa arm, seen from behind
and to the side so her face is not visible, leaning down with her attention on
the cleared half of the cushion.

[PRODUCT] the unit is the largest and clearest object in the frame and nothing
beside it competes for the first glance; the sofa is plain and dark, and no
other appliance is in shot.

[ENVIRONMENT] an ordinary living room in the afternoon with a real reason both
people are there - the sofa cushions are pulled out of place and a dog basket
sits against the wall. Ambient household light only, from the window opposite.

REGISTER: candid documentary photograph, natural, unposed, sharp. No text, no
badge, no arrow anywhere in the image."""

LIGHT_A = """TYPE: 06-relief-hero v1.15
REGISTER: commercial. Professional camera, controlled light, deliberate negative
space on one side.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit, identical in
every layer. Preserve shape, proportions, material, finish and colour exactly.

[SUBJECT] a woman in her forties in a plain long-sleeved top, standing at the
arm of a sofa, the unit carried easily in one hand at her side.
[POSE] mid-action: she has just lifted the unit off the sofa arm and is turning
with it toward the doorway, that hand loose and low, gaze ahead of her on where
she is going next. She stands clear of the sofa so the whole unit is visible
against the room rather than against her own body.
[SETTING] one real living room filled to the edges: a sofa with cushions, a
coffee table with a mug on it, a floor lamp, a bookshelf, a rug, a doorway open
onto a hall. Background blurred but never blank. None of these objects carries
printed text.
[LIGHT] soft even window light from the left, background blurred, high-key.
[OFFSET] she stands to the right of frame; the inset occupies the space on the
left that she is offset from, taking about three quarters of it.

In the upper left corner sit two small panels side by side, together about 20
percent of the frame width, each with a thin white border and both finishing a
clear margin short of the picture edge. Same room, same woman, same sofa in
both; the only thing that changes is the machine. The outer panel shows an
ordinary upright vacuum hauled up bodily onto the sofa seat, both her hands on
it, its hose dragging over the arm and its body tipped. The inner panel shows
the reference handheld unit in one hand at the same place on the same sofa, her
other hand free. A single arrow runs from the vacuum panel to the handheld
panel and there is no other marking. Both panels match the main picture in
resolution, grade and light quality.

No text anywhere in the image. No badge, no percentage."""

LIGHT_B = """TYPE: 06-relief-hero v1.15
REGISTER: commercial. Professional camera, controlled light, deliberate negative
space on one side.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit, identical in
every layer. Preserve shape, proportions, material, finish and colour exactly.

[SUBJECT] a woman in her forties in a plain long-sleeved top, standing at the
arm of a sofa, the unit carried easily in one hand at her side.
[POSE] mid-action: she has just lifted the unit off the sofa arm and is turning
with it toward the doorway, that hand loose and low, gaze ahead of her on where
she is going next. She stands clear of the sofa so the whole unit is visible
against the room rather than against her own body.
[SETTING] one real living room filled to the edges: a sofa with cushions, a
coffee table with a mug on it, a floor lamp, a bookshelf, a rug, a doorway open
onto a hall. Background blurred but never blank. None of these objects carries
printed text.
[LIGHT] soft even window light from the left, background blurred, high-key.
[OFFSET] she stands to the right of frame; the inset occupies the space on the
left that she is offset from, taking about three quarters of it.

In the upper left corner sits one small panel about 15 percent of the frame
width, with a thin white border, finishing a clear margin short of the picture
edge. The same woman, the same room and the same sofa; the only thing that
changes is the machine. In that panel she has an ordinary upright vacuum hauled
up bodily onto the sofa seat, both her hands on it, its hose dragging over the
arm and its body tipped, her shoulders pulled up under the weight. It matches
the main picture in resolution, grade and light quality.

No text anywhere in the image. No badge, no arrow, no percentage."""

LIGHT_C = """TYPE: 06-relief-hero v1.15
REGISTER: commercial. Professional camera, controlled light, deliberate negative
space on one side.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit, identical in
every layer. Preserve shape, proportions, material, finish and colour exactly.

[SUBJECT] reduced: present only as one forearm in a pushed-up sleeve and the
hand closed round the handle of the unit, carrying it at waist height. No face
and no shoulders in frame.
[POSE] mid-action: the unit lifted clear of a stack of pillows on a bed and
carried away toward the door, the hand loose and the wrist straight, nothing
braced. What makes carried-easily different from hauled is in the frame beside
it - an ordinary upright vacuum stands abandoned on the floor at the foot of the
bed with its hose coiled on the carpet, too big to lift onto it.
[SETTING] one real bedroom filled to the edges: a bed with a stack of stripped
pillows, a nightstand with a lamp, a chair with clothes over the back, a laundry
basket, a rug, a door open onto a landing. Background blurred but never blank.
None of these objects carries printed text.
[LIGHT] soft even window light from the left, background blurred, high-key.
[OFFSET] the hand and the unit sit to the right of frame; the inset occupies the
space on the left, taking about three quarters of it.

In the upper left corner sits one small panel about 15 percent of the frame
width, with a thin white border, finishing a clear margin short of the picture
edge. The same room and the same bed; the only thing that changes is the
machine. In that panel the same upright vacuum is hauled up bodily onto the
mattress, two hands on it, its hose dragging. It matches the main picture in
resolution, grade and light quality.

No text anywhere in the image. No badge, no arrow, no percentage."""

UV_A = """TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit. The outer shell
becomes translucent, but its silhouette, proportions and every visible external
part must match the reference exactly. Do not redesign or add features.

[CANVAS] a plain deep charcoal ground, and nothing else in the frame behind the
product.

[SHELL] the unit seen from above and slightly to one side as it sits on a plain
pale fabric surface, its casing translucent and glass-like, filling about 75
percent of the frame width.

[INTERNALS], solid and detailed inside the shell, each at its true location: a
tubular ultraviolet lamp lying across the full width of the base aperture, its
housing open to the fabric below; a vibration motor with its eccentric weight
driving a flat tapping plate at the front of the base; an impeller and motor in
the body behind them; a stack of three filter elements above the transparent
dust chamber, the chamber's multi-cup separator visible as a ring of small
cones.

[MARKS], one, nothing else in the frame is marked:
- working: the ultraviolet lamp shown ACTIVE, throwing a narrow violet-blue wash
  straight down onto the fabric directly beneath the base aperture, the
  brightest thing in the frame and clearly brighter than the ground, its edge
  ending where the aperture ends. No arrow anywhere - the lamp's own line
  carries the direction.

No text, numbers or spec labels anywhere in the image.
The marks are the only added colour; the product and its parts keep their own."""

UV_B = """TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit. The outer shell
becomes translucent, but its silhouette, proportions and every visible external
part must match the reference exactly. Do not redesign or add features.

[CANVAS] a plain deep charcoal ground, and nothing else in the frame behind the
product.

[SHELL] the unit seen square from the side as it sits on a plain pale fabric
surface, its casing translucent and glass-like, filling about 75 percent of the
frame width, so the whole path from base to dust chamber runs left to right
across the frame.

[INTERNALS], solid and detailed inside the shell, each at its true location: a
tubular ultraviolet lamp lying across the base aperture at the front, its
housing open to the fabric below; a flat tapping plate beside it driven by a
vibration motor and its eccentric weight; behind them the intake throat rising
into the transparent dust chamber, the chamber's multi-cup separator drawn as a
ring of small cones; a stack of three filter elements above the chamber; the
impeller and motor last, at the back of the body.

[MARKS], one, nothing else in the frame is marked:
- working: the ultraviolet lamp shown ACTIVE, throwing a narrow violet-blue wash
  straight down onto the fabric directly beneath the base aperture, the
  brightest thing in the frame and clearly brighter than the ground, its edge
  ending where the aperture ends. No arrow anywhere - the internal path's own
  line carries the direction.

No text, numbers or spec labels anywhere in the image.
The marks are the only added colour; the product and its parts keep their own."""

UV_C = """TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the handheld unit. The outer shell
becomes translucent, but its silhouette, proportions and every visible external
part must match the reference exactly. Do not redesign or add features.

[CANVAS] a plain deep charcoal ground, and nothing else in the frame behind the
product.

[SHELL] the unit tipped up so its base faces the camera at a shallow angle, its
casing translucent and glass-like, filling about 75 percent of the frame width,
the whole base aperture open to view.

[INTERNALS], solid and detailed inside the shell, each at its true location: a
tubular ultraviolet lamp lying across the full width of the base aperture in its
open housing; a flat tapping plate set into the base ahead of it, driven by a
vibration motor with its eccentric weight directly above; the intake slot
between them running back into the body; the transparent dust chamber with its
multi-cup separator drawn as a ring of small cones deeper in.

[MARKS], one, nothing else in the frame is marked:
- working: the ultraviolet lamp shown ACTIVE, its violet-blue light filling the
  open base aperture and falling as a narrow wash onto the pale fabric just
  beyond the unit, the brightest thing in the frame and clearly brighter than
  the ground, its edge ending where the aperture ends. No arrow anywhere.

No text, numbers or spec labels anywhere in the image.
The marks are the only added colour; the product and its parts keep their own."""


def snap(mode, scene, anchor, camera, moment):
    """05-social-snapshot expands the same five slots every time; only the
    filled content differs, so one wording carries across all eighteen prompts
    and one regex can check them all."""
    return f"""TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the handheld unit.
Preserve shape, proportions, material, finish and colour exactly. {camera}

CONTENT MODE, {mode}: {moment}

ANCHOR: {anchor}

SCENE: {scene}

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus
adequate, mild noise, honest exposure. No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect."""


# The SCENE slot the type requires, one per option. Kept beside the moments
# rather than inside them so the six tiles can be checked for room variety at a
# glance: six photographs of one corner of one house is the failure this type
# exists to avoid.
SCENES = [
    ["a main bedroom stripped for changing, photographed as found - the duvet "
     "half off the end of the bed, a chair with clothes over it, curtains open "
     "on a grey afternoon. Ambient household light only, from the window.",
     "a main bedroom mid-job, photographed as found - a laundry basket by the "
     "door, a phone charger trailing over the nightstand, the wardrobe door "
     "left open. Mixed warm-dim household light.",
     "a bedside corner photographed as found - a lamp on, a book face down, a "
     "ring dried into the wood of the nightstand, the bed unmade behind. Warm "
     "lamplight only, the rest of the room dim."],
    ["a main bedroom in the afternoon, photographed as found - a chair with "
     "clothes over the back, a radiator with a towel on it, the window open a "
     "crack. Ambient daylight only, no lamp on.",
     "a main bedroom mid-job, photographed as found - the duvet bundled on the "
     "floor, a mug on the nightstand, a laundry basket half full by the door. "
     "Flat window daylight only.",
     "a bedroom with the window wide open, photographed as found - a curtain "
     "lifted off the sill, a hairbrush and a glass on the nightstand, a jumper "
     "over the end of the bed. Bright flat daylight."],
    ["a landing between two bedrooms, photographed as found - a stack of towels "
     "on the floor at the top of the stairs, a bannister with a coat over it, "
     "both doors open. Mixed warm-dim household light.",
     "a landing photographed as found - the carpet worn in a line down the "
     "middle, a bag left against the wall, a light on in one bedroom and not "
     "the other. Ambient household light only.",
     "a living room in the afternoon, photographed as found - a throw pulled "
     "half off the sofa, a coffee table with a mug and a remote on it, a rug "
     "rucked at one corner. Window daylight, no lamp on."],
    ["a kitchen worktop photographed as found - crumbs at the edge of the "
     "board, a kettle and a jar of utensils pushed back, a tea towel over the "
     "oven rail. Kitchen overhead light only.",
     "a main bedroom stripped for changing, photographed as found - the duvet "
     "half off the end of the bed, a laundry basket by the door, curtains open "
     "on a grey afternoon. Ambient daylight only.",
     "a small bathroom floor photographed as found - a bath mat rucked up, a "
     "towel over the radiator, a bin beside the basin pedestal. Overhead "
     "bathroom light, slightly cold."],
    ["a living room in the afternoon, photographed as found - a throw pulled "
     "half off the sofa back, a coffee table with a mug on it, a rug rucked at "
     "one corner. Window daylight, no lamp on.",
     "a living room photographed as found - cushions pulled out of place, a "
     "newspaper-free side table with a glass on it, curtains half drawn. Mixed "
     "warm-dim household light.",
     "the floor beside a sofa photographed as found - a pet cushion flattened "
     "in the middle, a chewed rope toy against the skirting, the edge of a rug "
     "turned up. Ambient household light only."],
    ["a kitchen sink photographed as found - washing-up stacked on the "
     "draining board, a bottle of liquid on the sill, a cloth over the tap. "
     "Kitchen overhead light only.",
     "a kitchen draining board photographed as found - a mug and two glasses "
     "already drying, a folded dishcloth at the edge, the window above the sink "
     "showing a grey garden. Flat daylight from the window.",
     "a landing photographed as found - a socket at skirting height with two "
     "plugs in it, the carpet worn in a line, both bedroom doors standing open. "
     "Mixed warm-dim household light."],
]

REVIEWS = [
    {
        "quote": "The dust cup filled up after just one mattress pass. Easy to "
                 "push and the red to blue light is brilliant.",
        "opts": [
            ("at-rest", "the unit set down on the bare mattress it has just been "
             "run over, its transparent chamber packed to the brim with dense "
             "grey powder, its indicator window lit blue, cable trailing off the "
             "side of the bed",
             "a stripped duvet bundled at the foot of the bed",
             "It sits on the ticking, seen from above and slightly to one side, "
             "cropped the way a casual one-handed photo crops."),
            ("in-use", "the unit mid-pass down the middle of a bare mattress, one "
             "forearm in a pushed-up sleeve on the handle and no face in the "
             "frame, its chamber already half grey and its indicator lit blue "
             "behind the head",
             "a pillow without its case dropped beside the bed",
             "Seen from standing height at the side of the bed, tilted a few "
             "degrees."),
            ("at-rest", "the unit stood on a nightstand beside the bed it has just "
             "been used on, its transparent chamber full of grey powder held up "
             "against the lamp so the fill line reads clearly",
             "a water glass with a ring dried into the wood beside it",
             "Close in and slightly too low, the way a photo taken quickly "
             "crops."),
        ],
    },
    {
        "quote": "No dust blown back into the bedroom air. The heat leaves the "
                 "sheets and mattress feeling completely fresh.",
        "opts": [
            ("in-use", "the unit mid-pass across a bare mattress in a shaft of "
             "afternoon window light, the lit air above the bed clean and empty "
             "with no drift of motes in it, one forearm on the handle and no face "
             "in the frame",
             "a folded stack of laundered sheets on the corner of the bed",
             "Seen from the foot of the bed at standing height, tilted."),
            ("at-rest", "the unit set down on a bare mattress halfway through a "
             "job, the worked half of the ticking behind it even and matt and the "
             "unworked half ahead still dulled and greyed, the boundary running "
             "straight across the bed",
             "a radiator with a towel folded over it against the wall",
             "Seen from the side of the bed, a little too close."),
            ("in-use", "the unit mid-pass along a pillow laid flat on the bed, one "
             "hand on the handle and no face in the frame, the window behind it "
             "open and the air in the room clear",
             "an open window with the curtain lifted off the sill",
             "Seen from above at arm's length, tilted a few degrees."),
        ],
    },
    {
        "quote": "Lightweight enough to do every mattress and pet cushion in one "
                 "run without wrist fatigue.",
        "opts": [
            ("at-rest", "the unit standing on top of a stack of four stripped "
             "pillows piled on a landing floor, all of them just done, the cable "
             "looped once over the pile",
             "a dog basket pushed against the wall behind them",
             "Seen from standing height looking down, cropped a little too "
             "close."),
            ("in-use", "the unit carried in one hand at waist height along a "
             "landing between two bedrooms, the arm loose and the wrist straight, "
             "no face in the frame, a doorway open on each side",
             "a laundry basket set down in the doorway",
             "Seen from behind at walking height, framing tilted and casual."),
            ("at-rest", "the unit set down on the arm of a fabric sofa beside a "
             "pet cushion it has just been over, with a bare mattress visible "
             "through the open door behind it, so both jobs are in one frame",
             "a mug left on the coffee table in front of the sofa",
             "Seen from a seat on the opposite side of the room, off-centre."),
        ],
    },
    {
        "quote": "The tapping vibration pulled out fine grey sediment that my "
                 "normal vacuum never touched.",
        "opts": [
            ("at-rest", "the unit's transparent chamber lifted off and tipped out "
             "onto a sheet of white kitchen paper on a worktop, a mound of fine "
             "grey sediment and matted fibre sitting on the paper beside the empty "
             "chamber and the body of the unit",
             "a folded tea towel pushed to the side of the worktop",
             "Seen from above at arm's length, cropped a little too close."),
            ("at-rest", "the unit lying on its side on a bare mattress with its "
             "chamber still attached and packed with dense grey sediment, the "
             "fill visible through the clear wall against the pale ticking",
             "a pillow without its case beside it on the bed",
             "Seen from the side of the bed, tilted a few degrees."),
            ("kit-flatlay", "the unit, its detached transparent chamber full of "
             "grey sediment and its washable filter stack laid out beside each "
             "other on a bathroom floor, slightly out of line and not arranged",
             "a bath mat rucked up at the edge of the frame",
             "Seen from standing height looking straight down, off-centre."),
        ],
    },
    {
        "quote": "Essential gear for pet owners. It pulls deep hair and fine dust "
                 "out of the velvet sofa effortlessly.",
        "opts": [
            ("in-use", "the unit mid-pass along the seat of a dark velvet sofa, "
             "one hand on the handle and no face in the frame, the nap behind the "
             "head lying dark and even and the fabric ahead of it still greyed "
             "with settled hair",
             "a dog lead coiled on the sofa arm",
             "Seen from a seat at the other end of the sofa, framing a little too "
             "close."),
            ("at-rest", "the unit set down on a velvet sofa cushion with its "
             "chamber packed with a thick mat of pet hair and grey dust, one "
             "cleared strip of dark nap running away from it across the seat",
             "a chewed toy pushed down between the cushions",
             "Seen from standing height beside the sofa, tilted."),
            ("in-use", "the unit mid-pass over a pet cushion on the floor beside "
             "the sofa, one forearm on the handle and no face in the frame, loose "
             "hair lifting off the cover into the head",
             "a food bowl on a mat against the skirting",
             "Seen from a crouch at close range, off-centre and slightly low."),
        ],
    },
    {
        "quote": "The washable filter is simple to rinse clean and the corded "
                 "power never fades during use.",
        "opts": [
            ("at-rest", "the unit's filter stack held under a running kitchen tap, "
             "grey water carrying loose dust off it into the sink, the body of the "
             "unit standing on the worktop behind with its chamber already empty "
             "and open",
             "a washing-up brush standing in the sink corner",
             "Seen from above at the sink, cropped a little too close."),
            ("kit-flatlay", "the unit, its opened transparent chamber and its two "
             "rinsed filter elements laid out on a draining board to dry, still "
             "beaded with water and not lined up straight",
             "a folded dishcloth at the edge of the board",
             "Seen from standing height looking down, framing tilted."),
            ("at-rest", "the unit plugged into a wall socket on a landing with its "
             "cable running along the skirting, set down beside two bedroom doors "
             "both standing open, mid-way through working through the house",
             "a phone left on the floor beside the socket",
             "Seen from a crouch along the landing floor, off-centre."),
        ],
    },
]

# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------


def opt(o, varies, typ, ver, ratio, prompt, rationale, variant=None, axes=None,
        pipeline="single-pass", notes=None, avoid=None, asset=None):
    d = {"opt": o, "varies_on": varies, "type": typ, "type_version": ver,
         "variant": variant, "ratio": ratio, "pipeline": pipeline,
         "prompt": prompt, "rationale": rationale}
    if axes:
        d["axes"] = axes
    if notes:
        d["composition_notes"] = notes
    if avoid:
        d["avoid"] = avoid
    if asset:
        d["asset_candidate"] = asset
    return d


CROP_W = ("The layout crops this to 4:3, taking about 25 percent off the WIDTH "
          "of a 16:9 render. The subject is centred and the margin is what goes.")
CROP_H = ("The layout crops this to 4:3, taking about 25 percent off the HEIGHT "
          "of a 1:1 render. The composition runs left to right, so every panel "
          "loses the same band rather than the outer ones being amputated.")
CROP_INSET = ("The layout crops this to 4:3, taking about 12.5 percent off the "
              "top and bottom of a 1:1 render - and the inset sits at a top "
              "corner by law. Check it survives the crop before the asset "
              "ships, or set this slot to aspect-square.")
REVIEW_BLOCK = (
    "BLOCKED AS THE PAGE IS BUILT. 05-social-snapshot's authenticity fence is "
    "hard and non-negotiable: no reviewer name, avatar, star row or verified "
    "label anywhere near the image in the layout. reviews.photos.0-5 sit inside "
    "the same section element as reviews.quotes.0-5, which carry names, "
    "five-star rows and a green Verified label each. Rendering these beside "
    "that copy presents generated pictures as customer uploads, which is a "
    "fabricated endorsement. Either move the photo grid out of the attributed "
    "block, or drop the names, stars and verified labels from it, or use real "
    "customer photographs - which always win over generated ones.")

SLOTS = [
    {
        "slot_id": "hero.image", "section_role": "hero",
        "asset": f"{PAGE}-01-hero-pain-scene.png",
        "placement": "Directly under the byline, above hero.intro_1.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "The slot exists to make a cold reader recognise themselves "
                    "in a held state. Nothing about it is temporal - no "
                    "transition, no sequence, no output flowing - so it does not "
                    "earn motion."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT decides it. The hero cell for advertorial is 01-pain-scene and "
            "the copy hands it the exact moment the type wants: waking "
            "congested, before any product exists. A takes the symptom itself "
            "on the body, which is evidence rank 1 and the rank that has "
            "carried this type's passing renders. PAGE LEGALITY: no product in "
            "frame is correct here and G1 does not bind. EVIDENCE: the type is "
            "at 1.14 with a passing worked example in exactly this shape. "
            "PRODUCT PRESENCE: none, and that is the type's law. PROMPT RISK: "
            "lowest of the three - B needs a child and a parent's hands in one "
            "frame, which is two bodies to get right, and C is the only one "
            "whose evidence is airborne, which is the hardest thing here to "
            "render convincingly.",
        "options": [
            opt("A", "baseline", "01-pain-scene", "1.14", "16:9", HERO_A,
                "The waking moment itself, with the symptom on the body: "
                "swollen lids, raw skin, chapped nostrils. Evidence rank 1, the "
                "rank this type's passing renders have used.",
                variant="candid", axes={"gaze": "candid"},
                notes="Needs no photo - the type is G1-exempt and no product "
                      "appears. hero.image carries NO aspect class in the "
                      "template, so 16:9 lands uncropped.",
                asset=f"{PAGE}-01-hero-pain-scene--A.png"),
            opt("B", "persona - the parent rather than the sufferer",
                "01-pain-scene", "1.14", "16:9", HERO_B,
                "brief.persona names parents of children with eczema as a "
                "distinct group, and the pain reads differently on someone "
                "holding another person's arm than on their own face. Same "
                "evidence rank, different body.",
                variant="candid", axes={"gaze": "candid"},
                notes="Two bodies in one frame is the risk; the type's own law "
                      "is that a face cannot carry effort the body is not "
                      "making, and here the effort is his, not hers.",
                asset=f"{PAGE}-01-hero-pain-scene--B.png"),
            opt("C", "evidence rank - residue rather than symptom",
                "01-pain-scene", "1.14", "16:9", HERO_C,
                "Rank 2: the physical residue the problem produces. The dust "
                "burst out of the mattress into a light shaft is the page's own "
                "thesis made visible, and it names the mattress as the source "
                "before a single word of copy does.",
                variant="candid", axes={"gaze": "candid"},
                notes="Rank 2 has never been the ONLY evidence in a render of "
                      "this type. Airborne dust against a dark room is the "
                      "whole argument, so if it renders thin the option fails "
                      "outright rather than partly.",
                asset=f"{PAGE}-01-hero-pain-scene--C.png"),
        ],
    },
    {
        "slot_id": "reasons.items.0.image", "section_role": "cause",
        "asset": f"{PAGE}-02-reason0-cause-anatomy.png",
        "placement": "Beside 'Standard vacuums only touch the surface'.",
        "gif": {"eligible": True, "form": "whole-frame", "kind": "cause",
                "duration_s": 3, "loop": "seamless loop",
                "shot": "both panels, held as drawn",
                "action": "left grains hold, right grains rise",
                "result": "only the right weave clears",
                "match": "flat vector, same two grounds",
                "delivery": "mp4/webm, under 2 MB",
                "reason":
                    "The cause this slot indicts IS temporal: the head taps, the "
                    "weave lifts, the grains come out or they do not. A still "
                    "can only show the endpoint. 02-cause-anatomy legislates no "
                    "motion layer of its own, so the form is whole-frame and "
                    "the kind is the type's own job, cause."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT is decisive. The section's whole argument is a depth "
            "comparison - surface versus weave - and this type exists to draw a "
            "measurable landmark twice and change one property. The measure "
            "mark IS the argument here, not decoration. PAGE LEGALITY: cause "
            "sits second on the page, which is where this type belongs. "
            "EVIDENCE: flat-vector is the style that holds the measure dash "
            "pattern, and the type's strongest renders are the ones that left "
            "the anatomical skeleton behind, which a mattress section does. "
            "PRODUCT PRESENCE: the product is the right panel and a person is "
            "visible using it, which the type requires and four of six renders "
            "once failed. PROMPT RISK: B trades a proven style for a softer "
            "one, and C moves to a pillow, which is a smaller and less "
            "recognisable object than the thing the page is about.",
        "options": [
            opt("A", "baseline", "02-cause-anatomy", "1.15", "1:1", CAUSE_A,
                "Flat-vector, the style that holds the dash pattern. The "
                "mattress cut in section under a kneeling figure gives the type "
                "its `whole` frame and its measurable landmark in one.",
                notes="Needs the product photo. " + CROP_H,
                asset=f"{PAGE}-02-reason0-cause-anatomy--A.png"),
            opt("B", "style - airbrushed rather than flat-vector",
                "02-cause-anatomy", "1.15", "1:1", CAUSE_B,
                "Airbrushed gives modelled volume, which suits batting and "
                "fibre better than flat fills do. The type offers it and the "
                "trade is legibility of the dash against believability of the "
                "material.",
                notes="Needs the product photo. The measure dash is the risk - "
                      "flat-vector is the style recorded as holding it. "
                      + CROP_H,
                asset=f"{PAGE}-02-reason0-cause-anatomy--B.png"),
            opt("C", "subject class - the pillow rather than the mattress",
                "02-cause-anatomy", "1.15", "1:1", CAUSE_C,
                "Subject class is this type's widest diversity lever. A pillow "
                "on a lap is closer to the reader's face than a mattress is, "
                "and the copy's next section is about what sits millimetres "
                "beneath a pillowcase.",
                notes="Needs the product photo. Argues the pillow while the "
                      "section's own words argue the mattress. " + CROP_H,
                asset=f"{PAGE}-02-reason0-cause-anatomy--C.png"),
        ],
    },
    {
        "slot_id": "reasons.items.1.image", "section_role": "problem-agitation",
        "asset": f"{PAGE}-03-reason1-pain-scene-object.png",
        "placement": "Beside 'Washing sheets alone leaves the core untouched'.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "A still life of a bed already stripped. It is a state the "
                    "reader inspects, not a process, and nothing in it changes "
                    "over time."},
        "recommended_opt": "A",
        "recommendation_basis":
            "PAGE LEGALITY decides it over FIT. This is a second pain beat and "
            "01-pain-scene is already the hero, so the runbook's rung 4 applies "
            "- another execution of a type on the page, differing on a named "
            "dimension, here subject class: object-only rather than a person. "
            "That is the precedent recorded twice in the ledger for this type. "
            "FIT: the section's argument is that the clean thing sits on the "
            "dirty thing, which is a still life and not an action. EVIDENCE: "
            "object-only executions are recorded twice. PRODUCT PRESENCE: none, "
            "correctly - the product is still four sections away. PROMPT RISK: "
            "A is G1-exempt and runnable with no upload at all; B puts a person "
            "back in and competes with the hero for the same beat.",
        "options": [
            opt("A", "baseline - object-only", "01-pain-scene", "1.14", "16:9",
                SHEETS_A,
                "The clean stack set down on the stained bare ticking is the "
                "section's sentence as one picture. Evidence rank 1 on an "
                "object: the discolouration itself, not a gesture at it.",
                variant="candid", axes={"gaze": "candid"},
                notes="Needs no photo - G1-exempt, no product. " + CROP_W,
                asset=f"{PAGE}-03-reason1-pain-scene-object--A.png"),
            opt("B", "subject - a person mid-action rather than object-only",
                "01-pain-scene", "1.14", "16:9", SHEETS_B,
                "The type's default form: a force being applied. Fitting a "
                "clean sheet over a stained mattress is the exact act the "
                "section calls futile, and the stain is still in frame beside "
                "the hand doing it.",
                variant="candid", axes={"gaze": "candid"},
                notes="Needs no photo. Repeats the hero's form as well as its "
                      "type, so the two beats read more alike. " + CROP_W,
                asset=f"{PAGE}-03-reason1-pain-scene-object--B.png"),
            opt("C", "subject class - pillows rather than the bed",
                "01-pain-scene", "1.14", "16:9", SHEETS_C,
                "The copy's own line is that mite matter sits just millimetres "
                "beneath the pillowcase. Two stripped pillows still holding the "
                "shape of a head put the evidence where the reader's face goes.",
                variant="candid", axes={"gaze": "candid"},
                notes="Needs no photo. The tightest frame of the three, so the "
                      "4:3 crop costs least here. " + CROP_W,
                asset=f"{PAGE}-03-reason1-pain-scene-object--C.png"),
        ],
    },
    {
        "slot_id": "reasons.items.2.image", "section_role": "proof",
        "asset": f"{PAGE}-04-reason2-proof-lockedframe.png",
        "placement": "Beside 'Ordinary vacuums blow fine particles into the "
                     "room'.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "A locked-frame comparison is inspected, not watched - the "
                    "reader's eye does the travelling between panels. Motion "
                    "here would also break the fairness rule by drawing the eye "
                    "to one panel."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT and EVIDENCE agree. The section's claim is that one machine "
            "puts particles into the air and the other does not, and that "
            "difference is visible to the naked eye inside a static frame - "
            "motes in a light shaft - which is the exact condition this type's "
            "use_when sets. Two panels rather than three because the section "
            "names one alternative, not two. PAGE LEGALITY: the type's use_when "
            "also wants a reader who already understands the problem, and by "
            "reason 2 they have had the cause and the pain. CAPABILITY: "
            "generation_mode is multi-pass at type level, but its own gate "
            "sends --verdict to handheld in one pass where the renderer does "
            "not composite, which ADR-021 settles for this pipeline. PROMPT "
            "RISK: B adds a third panel and a second unbranded machine to keep "
            "identical; C moves to a sofa, which is not the section's subject.",
        "options": [
            opt("A", "baseline - two panels", "04-proof-lockedframe", "1.13",
                "1:1", AIR_A,
                "Two panels, one variable: what is on the mattress and what the "
                "light shaft shows above it. The room, the bed, the window and "
                "the beam are named as constant before either panel is "
                "described.",
                variant="verdict", axes={"camera_lock": "handheld"},
                notes="Needs the product photo. generation_mode is multi-pass "
                      "at type level; the capability gate runs --verdict "
                      "handheld in one pass where the renderer cannot "
                      "composite, which is this pipeline (ADR-021). " + CROP_H,
                asset=f"{PAGE}-04-reason2-proof-lockedframe--A.png"),
            opt("B", "panel count - three rather than two",
                "04-proof-lockedframe", "1.13", "1:1", AIR_B,
                "brief.competitorContext names three alternatives, and a basic "
                "handheld cleaner is the one a reader may already have tried. "
                "The middle panel is the honest half-measure between the two "
                "ends.",
                variant="verdict", axes={"camera_lock": "handheld"},
                notes="Needs the product photo. Three panels in a 1:1 frame "
                      "give each a tall narrow strip; the type's own ratio "
                      "evidence is that stacked and split layouts degrade as "
                      "panels get thinner. " + CROP_H,
                asset=f"{PAGE}-04-reason2-proof-lockedframe--B.png"),
            opt("C", "surface - a sofa rather than a mattress",
                "04-proof-lockedframe", "1.13", "1:1", AIR_C,
                "The exhaust argument is not specific to beds, and the "
                "rawFeatures list names sofas, curtains and car seats. A living "
                "room also breaks a page that is otherwise entirely bedroom.",
                variant="verdict", axes={"camera_lock": "handheld"},
                notes="Needs the product photo. Argues in a room the section's "
                      "own words never mention. " + CROP_H,
                asset=f"{PAGE}-04-reason2-proof-lockedframe--C.png"),
        ],
    },
    {
        "slot_id": "reasons.items.3.image", "section_role": "mechanism",
        "asset": f"{PAGE}-05-reason3-relief-hero-detail.png",
        "placement": "Beside 'Integrated heat creates a hostile environment'.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "The section's claim is thermal and thermal is invisible in "
                    "every register this library has. A loop of a head moving "
                    "over fabric adds duration without adding argument, and the "
                    "--detail inset it would occupy holds a contact, which is a "
                    "held state."},
        "recommended_opt": "A",
        "recommendation_basis":
            "This is the page's weakest slot and the recommendation says so. "
            "FIT: the section argues heat, and no type can photograph 149F - "
            "G8 forbids inventing an emission to make a render look alive. So "
            "the slot is served by the half of the claim a camera can hold, the "
            "sealed contact and the debris leaving the weave, and 06-relief-"
            "hero --detail is the type whose inset exists for a feature too "
            "small to read at scene scale. PAGE LEGALITY: the product appears "
            "here for the first time, which is the right beat for it. "
            "EVIDENCE: --detail is the type's best-evidenced inset after "
            "--recall. PRODUCT PRESENCE: dominant, in hand, and magnified. "
            "PROMPT RISK: the inset is at a corner and this slot is "
            "4:3-cropped, so the crop is the thing to check. B moves the inset "
            "to the dust chamber, which argues capture rather than contact and "
            "duplicates what reasons.items.4 already shows.",
        "options": [
            opt("A", "baseline - the inset on the contact", "06-relief-hero",
                "1.15", "1:1", CONTACT_A,
                "The magnified seal between head and ticking is the one thing "
                "the scene cannot show and the one thing that makes the section "
                "true: the fabric lifts into the intake rather than the head "
                "riding over it.",
                variant="commercial",
                axes={"register": "commercial", "inset_mode": "detail"},
                notes="Needs the product photo. Argues the mechanical half of "
                      "the section only; the thermal claim is left to the copy "
                      "and is not proved here. " + CROP_INSET,
                asset=f"{PAGE}-05-reason3-relief-hero-detail--A.png"),
            opt("B", "inset content - the filled chamber rather than the "
                "contact", "06-relief-hero", "1.15", "1:1", CONTACT_B,
                "Moves the magnified evidence from cause to result. A packed "
                "chamber is the most legible proof this product produces and "
                "the reviews quote it twice.",
                variant="commercial",
                axes={"register": "commercial", "inset_mode": "detail"},
                notes="Needs the product photo. Overlaps reasons.items.4, which "
                      "already carries the chamber as its moment. " + CROP_INSET,
                asset=f"{PAGE}-05-reason3-relief-hero-detail--B.png"),
            opt("C", "subject - reduced to hands, with a worked boundary",
                "06-relief-hero", "1.15", "1:1", CONTACT_C,
                "The type's reduced form, chosen where the result is more "
                "legible than the user. It names what finished looks like "
                "against unfinished on one continuous surface, which is the "
                "clause that makes a reduced subject argue anything.",
                variant="commercial",
                axes={"register": "commercial", "inset_mode": "detail"},
                notes="Needs the product photo. No face means no expression to "
                      "carry relief, so the boundary on the ticking has to do "
                      "all of it. " + CROP_INSET,
                asset=f"{PAGE}-05-reason3-relief-hero-detail--C.png"),
        ],
    },
    {
        "slot_id": "reasons.items.4.image", "section_role": "social-proof",
        "asset": f"{PAGE}-06-reason4-social-handoff.png",
        "placement": "Beside 'Visual dust sensor eliminates all guesswork'.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "The indicator's argument is a state, not a transition - "
                    "blue means this area is done. A loop showing red turning "
                    "blue would be a second state in one frame, which G11 bars, "
                    "and this type legislates no layer a loop could occupy."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT, once the section is read as what it actually is. The dust "
            "indicator is not a spec, it is the thing that ends an argument "
            "between two people about whether the bed is clean - and "
            "05-social-handoff exists for exactly the beat where one person "
            "shows another what the product just did. Its use_when asks for a "
            "product whose effect is visible in the room afterwards; here the "
            "effect is a blue light and a full chamber, both visible. PAGE "
            "LEGALITY: it is the page's only social image outside the reviews "
            "block, and the reviews block is blocked, so this is the only "
            "social proof that can ship. EVIDENCE: the type is at 2.5 with the "
            "dominance fix landing 3 of 4. PRODUCT PRESENCE: dominant by law. "
            "PROMPT RISK: the type's recorded fault is the advocate's eyes "
            "drifting to the work; A puts the unit down first so the posture is "
            "at rest before the look is asked for.",
        "options": [
            opt("A", "baseline - the indicator as the moment",
                "05-social-handoff", "2.5", "1:1", INDICATOR_A,
                "The unit set down, the light blue, the worked and unworked "
                "halves of the ticking meeting in a straight line. The advocate "
                "has finished, which is what lets her eyes leave the work.",
                notes="Needs the product photo. The recorded fault for this "
                      "type is an advocate still mid-stroke, so the pass is "
                      "over before the look happens. " + CROP_H,
                asset=f"{PAGE}-06-reason4-social-handoff--A.png"),
            opt("B", "moment - the chamber held up rather than the light",
                "05-social-handoff", "2.5", "1:1", INDICATOR_B,
                "A held-up chamber of grey powder is the most quoted moment in "
                "the page's own reviews. It is louder evidence than a coloured "
                "light and needs no explanation.",
                notes="Needs the product photo. Argues capture rather than the "
                      "section's own subject, which is knowing when to stop. "
                      + CROP_H,
                asset=f"{PAGE}-06-reason4-social-handoff--B.png"),
            opt("C", "environment - a sofa and a pet household",
                "05-social-handoff", "2.5", "1:1", INDICATOR_C,
                "brief.persona names pet owners as a distinct group and the "
                "page is otherwise all bedroom. Pet hair on dark fabric is the "
                "clearest worked boundary this product makes.",
                notes="Needs the product photo. Moves the section's argument "
                      "off the mattress the copy is discussing. " + CROP_H,
                asset=f"{PAGE}-06-reason4-social-handoff--C.png"),
        ],
    },
    {
        "slot_id": "reasons_b.items.0.image", "section_role": "outcome",
        "asset": f"{PAGE}-07-reasonb0-relief-hero-recall.png",
        "placement": "Beside 'Lightweight design allows effortless whole-home "
                     "use'.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "A recall inset holds two states side by side for the reader "
                    "to compare. That is inspected, not watched, and animating "
                    "one cell would make the pair argue at two speeds."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT and the runbook's rung 4 together. The section's claim is "
            "comparative - light against heavy - and --recall is the inset mode "
            "whose two cells change ONE thing while holding the activity, the "
            "place and the person constant. That is this argument exactly. "
            "06-relief-hero is already at reasons.items.3, so this is rung 4, "
            "differing on a named axis: inset_mode, detail against recall. "
            "--context was considered and dropped by its own law - its inset is "
            "the product in its real installed position, and a handheld has "
            "none. EVIDENCE: `step` has 7 observations and `past` 5, the "
            "best-evidenced inset modes the type owns. PROMPT RISK: two cells "
            "must match the hero in resolution and grade or they read as pasted "
            "in, which is the recorded failure; B drops to one cell and loses "
            "the comparison the section is making.",
        "options": [
            opt("A", "baseline - two cells, past then resolved",
                "06-relief-hero", "1.15", "1:1", LIGHT_A,
                "The upright hauled onto the sofa, then the handheld in one "
                "hand at the same place. Same woman, same room, same sofa: only "
                "the machine changes, which is the clause that makes a recall "
                "pair isolate anything.",
                variant="commercial",
                axes={"register": "commercial", "inset_mode": "recall"},
                notes="Needs the product photo. " + CROP_INSET,
                asset=f"{PAGE}-07-reasonb0-relief-hero-recall--A.png"),
            opt("B", "inset form - one cell rather than two", "06-relief-hero",
                "1.15", "1:1", LIGHT_B,
                "FORM 1: the problem state alone, smaller and simpler. The hero "
                "already shows the resolved state at full size, so a second "
                "resolved cell repeats it.",
                variant="commercial",
                axes={"register": "commercial", "inset_mode": "recall"},
                notes="Needs the product photo. A smaller inset survives the "
                      "crop better than two cells do. " + CROP_INSET,
                asset=f"{PAGE}-07-reasonb0-relief-hero-recall--B.png"),
            opt("C", "subject - reduced, with the heavy machine in the scene",
                "06-relief-hero", "1.15", "1:1", LIGHT_C,
                "Puts the comparison in the hero itself: the handheld carried "
                "in one hand while the upright stands abandoned on the floor "
                "because it cannot be lifted onto the bed. The inset then only "
                "confirms it.",
                variant="commercial",
                axes={"register": "commercial", "inset_mode": "recall"},
                notes="Needs the product photo. Two machines in the hero risks "
                      "the wrong one taking the first glance. " + CROP_INSET,
                asset=f"{PAGE}-07-reasonb0-relief-hero-recall--C.png"),
        ],
    },
    {
        "slot_id": "reasons_b.items.1.image", "section_role": "mechanism",
        "asset": f"{PAGE}-08-reasonb1-mechanism-xray.png",
        "placement": "Beside 'Surface UV lamp adds targeted surface care'.",
        "gif": {"eligible": True, "form": "whole-frame", "kind": "mechanism",
                "duration_s": 3, "loop": "seamless loop",
                "shot": "the see-through render, held as built",
                "action": "impeller turns, plate taps",
                "result": "the lamp never dims",
                "match": "same charcoal ground, same violet",
                "delivery": "mp4/webm, under 2 MB",
                "reason":
                    "Three of the four functions this section lists are "
                    "movements - the plate taps, the impeller turns, air runs "
                    "the filter stack - and a still can only assert them. "
                    "03-mechanism-xray legislates no motion layer, so the form "
                    "is whole-frame and the kind is the type's own job, "
                    "mechanism."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT, and the attribute gate makes it the only mechanism type "
            "available. body_contact is false for a fabric appliance, which "
            "drops 03-mechanism-ghostbody by its own avoid_when, and "
            "03-spec-split and 03-spec-explode are not advertorial types. That "
            "leaves xray, which is also exactly right: the section argues from "
            "a component the buyer cannot see, and xray exists to show real "
            "internals through a translucent shell. A is the top-down view "
            "because it puts the lamp, the tapping plate and the filter stack "
            "in one read. EVIDENCE: the type passed at 1.3 on two owner-passed "
            "worked examples. PRODUCT PRESENCE: the product IS the frame. "
            "PROMPT RISK: the `working` mark is the UV lamp, which is a real "
            "emission and needs no invention - G8 is satisfied without "
            "stretching. The heat and the suction have no visible form and are "
            "correctly left unmarked.",
        "options": [
            opt("A", "baseline - top-down through the lid", "03-mechanism-xray",
                "1.3", "16:9", UV_A,
                "From above, the lamp runs the full width of the base aperture "
                "and the filter stack sits behind it, so the whole four-in-one "
                "head reads in one look.",
                notes="Needs the product photo. One mark only: the lamp is the "
                      "single real emission this product makes, and G8 forbids "
                      "inventing one for the heat or the suction. " + CROP_W,
                asset=f"{PAGE}-08-reasonb1-mechanism-xray--A.png"),
            opt("B", "viewpoint - side cutaway, the airflow path legible",
                "03-mechanism-xray", "1.3", "16:9", UV_B,
                "Square from the side the internals lay out as a path: intake, "
                "chamber, separator, filters, impeller. That is the section's "
                "other half - the sealed route the particles take.",
                notes="Needs the product photo. A side view hides the lamp's "
                      "width, which is the mark the section is actually about. "
                      + CROP_W,
                asset=f"{PAGE}-08-reasonb1-mechanism-xray--B.png"),
            opt("C", "viewpoint - the base tipped toward the camera",
                "03-mechanism-xray", "1.3", "16:9", UV_C,
                "The underside is where the lamp, the tapping plate and the "
                "intake all live, and it is the face a buyer never sees because "
                "it is against the mattress whenever the machine is on.",
                notes="Needs the product photo. The dust chamber and filters sit "
                      "deep and small from this angle, so the capture argument "
                      "weakens. " + CROP_W,
                asset=f"{PAGE}-08-reasonb1-mechanism-xray--C.png"),
        ],
    },
]

# A REPEATING SECTION GETS ONE OPTION PER SLOT, NOT THREE. Owner decision,
# 2026-08-18, ADR-022. 05-social-snapshot's own SET DIVERSITY LAW puts the
# variation budget BETWEEN tiles - "when a page requests more than one snapshot,
# every image must differ COMPLETELY" - so three options inside one tile spend it
# in the dimension where it buys nothing, and create a choice that can break the
# set: pick snapshot on three tiles and handoff on three and the review wall
# stops reading as one group of customers.
#
# WHICH option each tile keeps is decided by the SET law, not by the letter A.
# The six A-variants as first written gave two bedrooms AND two kitchens and four
# at-rest modes, which the law forbids. Tile 3 therefore keeps what was drafted as
# C - the bathroom kit-flatlay - and the set comes out at five room classes and
# three content modes. Dropping to one option is what made that visible; three
# options had been masking it.
KEEP = [0, 0, 0, 2, 0, 0]

# How each tile differs from the other five. With no B or C to vary from, this is
# what `varies_on` has to carry: the tile's place in the set.
SET_VARIES = [
    "set position 1 of 6 - bedroom, at rest, the filled chamber on bare ticking, "
    "seen from above at arm's length in grey afternoon daylight",
    "set position 2 of 6 - bedroom again because both quotes are about a "
    "mattress, but differing on all four other axes the SET law names: in use "
    "rather than at rest, a lit shaft of air rather than a surface, window "
    "daylight rather than flat grey, standing height at the foot of the bed "
    "rather than arm's length",
    "set position 3 of 6 - landing, at rest, a stack of stripped pillows, mixed "
    "warm-dim household light, looking down from standing height",
    "set position 4 of 6 - bathroom floor, kit-flatlay, the tipped-out sediment "
    "and the filter stack, cold overhead light, straight down and off-centre",
    "set position 5 of 6 - living room, in use, dark velvet sofa nap, window "
    "daylight, from a seat at the other end of the sofa",
    "set position 6 of 6 - kitchen sink, at rest, running water over the filter, "
    "kitchen overhead light, from above at the sink",
]

for i, rev in enumerate(REVIEWS):
    mode, moment, anchor, camera = rev["opts"][KEEP[i]]
    SLOTS.append({
        "slot_id": f"reviews.photos.{i}.image", "section_role": "social-proof",
        "asset": f"{PAGE}-09-review{i}-social-snapshot.png",
        "placement": f"Review photo tile {i + 1} of 6, in the same section as "
                     f"the quote: {rev['quote']}",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "A customer snapshot argues that the thing exists in a real "
                    "home. That is a held state, and this type bans every added "
                    "layer, so there is nothing a loop could occupy."},
        "recommended_opt": "A",
        "recommendation_basis":
            "ONE OPTION, NOT THREE, because this is a repeating section "
            "(ADR-022). 05-social-snapshot's SET DIVERSITY LAW makes the six "
            "tiles the unit of variation, not the tile: every image must differ "
            "completely in room class, surface, light temperature, camera "
            "distance and content mode. Three options per tile would have spent "
            "that budget inside a cell where it buys nothing, and would have let "
            "a mixed set through - three tiles of one register beside three of "
            "another reads as two shoots, and two shoots read as fake. FIT is "
            "fixed by the cell anyway: 05-social-snapshot is the advertorial "
            "social-proof type for a review block, and the trust gap it names - "
            "does this actually exist and work in a normal home - is this "
            "block's exactly. PAGE LEGALITY: BLOCKED, and this outranks "
            "everything else; nothing here ships until the layout changes. "
            "EVIDENCE: the type is at 1.2. PRODUCT PRESENCE: G1 binds even in "
            "this register - casual framing may crop the product, but what is "
            "visible must match the reference. PROMPT RISK: a face turns the "
            "image into a testimonial portrait, which is a different type's job "
            "and a compliance risk here, so it keeps to incidental limbs.",
        "options": [
            opt("A", SET_VARIES[i], "05-social-snapshot", "1.2", "1:1",
                snap(mode, SCENES[i][KEEP[i]], anchor, camera, moment),
                "The moment this tile's quote describes, photographed as found, "
                "in the room class and content mode the SET law leaves for this "
                "position.",
                notes=REVIEW_BLOCK,
                asset=f"{PAGE}-09-review{i}-social-snapshot--A.png"),
        ],
    })

for slot_id, role, reason in (
    ("scarcity.image", "cta",
     "A product card inside the scarcity block. mapping/slot-rules.md leaves "
     "the cta row empty in all four channels: this is a standard product shot, "
     "which is out of library scope by design."),
    ("rail.image", "cta",
     "A product card inside the offer rail, same as scarcity.image. The cta row "
     "is empty in all four channels."),
    ("hero.author_avatar", "author",
     "A byline portrait. No type in this library produces a portrait of a named "
     "person, and generating a face to sit under a real byline is a disclosure "
     "decision rather than an image one."),
    ("closing.bio_image", "author",
     "The About-the-author portrait, same as hero.author_avatar."),
    ("comments.items.0.avatar", "social-proof",
     "A commenter portrait, 1 of 7. No library type produces portraits, and a "
     "generated face under a named comment is a fabricated person."),
    ("comments.items.1.avatar", "social-proof", "Commenter portrait, 2 of 7."),
    ("comments.items.2.avatar", "social-proof", "Commenter portrait, 3 of 7."),
    ("comments.items.3.avatar", "social-proof", "Commenter portrait, 4 of 7."),
    ("comments.items.4.avatar", "social-proof", "Commenter portrait, 5 of 7."),
    ("comments.items.5.avatar", "social-proof", "Commenter portrait, 6 of 7."),
    ("comments.items.6.avatar", "social-proof", "Commenter portrait, 7 of 7."),
    ("header.logo", "cta", "The brand logo, already supplied in the export."),
    ("footer.logo", "cta", "The brand logo, already supplied in the export."),
    ("guarantee.badge_image", "cta",
     "A money-back guarantee badge, already supplied in the export."),
):
    SLOTS.append({
        "slot_id": slot_id, "section_role": role,
        "asset": "—", "placement": "—",
        "options": [], "out_of_scope_reason": reason,
    })

OUT = {
    "page_id": PAGE,
    "registry_version": "2.0.0",
    "channel": "advertorial",
    "awareness_stage": "problem-aware",
    "slots": SLOTS,
    "coverage": {
        "covered": [
            "step 1 pain — 01-pain-scene twice, a person at the hero and the "
            "object-only stripped bed at reasons.items.1",
            "step 2 cause — 02-cause-anatomy at reasons.items.0",
            "step 3 mechanism — 03-mechanism-xray at reasons_b.items.1",
            "step 4 proof — 04-proof-lockedframe --verdict at reasons.items.2",
            "step 5 social — 05-social-handoff at reasons.items.4 and "
            "05-social-snapshot across all six review tiles",
            "step 6 relief — 06-relief-hero twice, --detail at reasons.items.3 "
            "and --recall at reasons_b.items.0",
        ],
        "absent": [
            "step 2 symptom — 02-symptom-rail was trimmed off advertorial on "
            "2026-08-11 and is not a candidate at any rung",
            "step 3 use — 03-use-sequence is dropped by its own avoid_when, 'the "
            "product has one obvious action'. It declares 3:4 and 1:1 and would "
            "not have served a 4:3 slot either.",
            "step 6 relief-scene — 06-relief-scene is dropped by its own "
            "avoid_when: the result here is invisible on the body, and for an "
            "invisible result that file sends the closing image to "
            "06-relief-hero with the product in frame. It is also one of only "
            "two types that declare 4:3, so losing it costs this page the ratio "
            "as well as the beat.",
            "step 5 personas — 05-persona-grid is marketplace and landing-page "
            "only",
        ],
        "absent_but_correct": [
            "No 03-mechanism-ghostbody, correctly — body_contact is false for a "
            "fabric appliance and the type's own avoid_when drops it when the "
            "product does not act on a body structure.",
            "No symptom rung, and that is right for a problem-aware reader who "
            "already wakes up with the symptom: the copy spends its hero "
            "re-establishing it in prose and needs the cause next, which runs.",
        ],
        "gaps": [
            "The HEAT claim at 149F is invisible in every register and "
            "reasons.items.3 is built on it. The recommended option argues the "
            "sealed contact and the debris leaving the weave, and leaves the "
            "thermal half to the copy. It is not proof of heat.",
            "The UV STERILISATION claim is argued only by presence. An image can "
            "show the lamp lit; it cannot show a germ killed, and brief."
            "rawFeatures says the 99.9 percent figure needs the manufacturer's "
            "test data because dose depends on dwell time. No option asserts a "
            "rate.",
            "SILENCE and SMELL are claimed in the reviews copy — 'no musty "
            "smell', 'no dust cloud' — and neither is photographable. The dust "
            "cloud half is carried by reasons.items.2; the smell is not carried "
            "by anything and stays a copy claim.",
        ],
    },
    "recommended": [],
    "page_composition_notes": [
        GAP_RATIO,
        GAP_REVIEWS,
        GAP_INSET,
        GAP_CHANNEL,
        GAP_ATTACH,
        GAP_HEAT,
        GAP_CLAIMS,
        GAP_ARC,
        "One-type-once was the binding constraint and rung 4 carried it twice. "
        "Seven body slots needed seven distinct executions from an advertorial "
        "column that offers eight types, two of which are dropped by attribute "
        "gates. 01-pain-scene repeats at reasons.items.1 differing on subject "
        "class, and 06-relief-hero repeats at reasons_b.items.0 differing on "
        "inset_mode — both are the runbook's rung 4, another execution of a "
        "type already on the page differing on a named dimension, and both are "
        "recorded here rather than left to look like an oversight.",
        "06-relief-hero --context was considered and dropped by its own law. "
        "Its inset is defined as the product in its real installed position and "
        "G7-X binds it; a handheld corded appliance has no installed position, "
        "so the mode contradicts itself here. --recall took the slot instead.",
        "THE SIX REVIEW TILES GET ONE OPTION EACH, NOT THREE (ADR-022). "
        "05-social-snapshot's SET DIVERSITY LAW makes the six tiles the unit of "
        "variation rather than the tile: every image must differ completely in "
        "room class, surface, light temperature, camera distance and content "
        "mode. Three options per tile spend that budget where it buys nothing "
        "and open a door the checks cannot close - pick one register on three "
        "tiles and another on three, both legal individually, and the wall "
        "reads as two shoots, which reads as fake. Dropping to one is also what "
        "made a real defect visible: the six first-drafted variants gave two "
        "bedrooms AND two kitchens with four at-rest modes. The set now runs "
        "bedroom, bedroom, landing, bathroom, living room, kitchen across three "
        "content modes, and build.py checks it on every run.",
        "The two bedroom tiles are a deliberate repeat and the SET law's own "
        "words allow it. It asks for a different room class 'where possible', "
        "and both of those quotes are about a mattress - moving one into a "
        "kitchen would break FIT to buy a diversity axis. They differ on the "
        "four axes that remain: at rest against in use, a bare surface against "
        "a lit shaft of air, flat grey against window daylight, arm's length "
        "against standing height at the foot of the bed.",
        "FOUR PROMPTS SIT OVER THEIR TYPE'S MEASURED REFERENCE SIZE AND ARE "
        "SHIPPED THAT WAY, which is said here rather than left for the reader to "
        "find. 02-cause-anatomy gives ~1800 characters at two marks and the "
        "three options here run 1878 to 1887, 4 to 5 percent over; "
        "04-proof-lockedframe gives 1800 and its three-panel option B runs 1839. "
        "Seven passes of trimming removed duplicated law - the long G1 preserve "
        "clause where the skeleton carries its own one-line form, 'drawn "
        "realistically and' where the register line already said it, repeated "
        "scene nouns across panels. What is left is earned: the measure mark IS "
        "the argument, the verdict mark is required by the skeleton, and the "
        "three-ways-the-comparison-is-lost clauses are the type's own recorded "
        "faults. Cutting further would cut law rather than fat. Adapter Rule 6 "
        "asks for a re-read past 2500 and nothing here comes near it.",
        "No pick prior was available. feedback/picks.jsonl is empty, so the "
        ">=20-pick tie-breaker in SPEC 7.7 never fired and every recommendation "
        "here rests on fit, legality, render evidence, product presence and "
        "prompt risk alone. These recommendations make the page "
        "argument-complete; they are not conversion-optimised and nothing here "
        "is performance-backed.",
        "Ratio is set in the generation tool's aspect-ratio parameter, never in "
        "the prompt text (adapters/nano-banana.md Rule 4). The Strictly avoid "
        "line is not rendered into any prompt (ADR-014); the exclusion list is "
        "kept in each option's avoid field for a model with a real negative "
        "channel.",
    ],
}

# ---- build the plate prompt (G12, ADR-020) ----------------------------------
# The gif prompt RENDERS the work order; it never animates a supplied still.
# On whole-frame the plate IS the delivered image, so the card carries the five
# lines and nothing else. One template, and the five lines are generated from
# the stored brief fields rather than retyped.
PLATE = """TYPE: G12 motion brief plate, whole-frame card
MEDIUM: a flat card carrying text and nothing else. NOT a photograph, NOT an
illustration, NOT a scene. Nothing is depicted.

The whole picture is flat dark grey, one even tone, no gradient and no texture.
One thin white rule runs inside it as a closed rectangle, its outer edge
finishing a clear margin short of the picture on all four sides, so no part of
it touches or leaves an edge.

Inside that rule, in clean white sans-serif, five short lines, each on one line,
left aligned, the block filling about half the picture's width:
{lines}

Set those five lines exactly as written, as plain words. No asterisks, no
backticks, no bullets, no markdown of any kind, and no line wrapping.

This is the only text in the picture. No logo, no icon, no border decoration,
no product and no scene."""

for _s in OUT["slots"]:
    _g = _s.get("gif") or {}
    if not _g.get("eligible"):
        continue
    if _g["form"] != "whole-frame":
        raise SystemExit(f"{_s['slot_id']}: only the whole-frame plate is built "
                         f"here; an inset plate is drawn by the host type's own "
                         f"prompt, not by this block")
    _g["prompt"] = PLATE.format(lines="\n".join([
        f"GIF SLOT · {_g['duration_s']}s · {_g['loop']}",
        f"SHOT {_g['shot']}",
        f"ACTION {_g['action']}",
        f"RESULT {_g['result']}",
        f"MATCH {_g['match']}",
    ]))
    _root, _ext = os.path.splitext(_s["asset"])
    _g["asset"] = f"{_root}--brief{_ext}"


ATTACH_RE = re.compile(r"\battached\b", re.I)


def binds_a_photo(o):
    """Whether THIS prompt asks for an attachment, read off the prompt rather
    than off the type's index flag — that flag is type-level and variants
    override it. Disagreements are printed in the self-checks, never resolved
    silently."""
    return bool(ATTACH_RE.search(o["prompt"]))


def run_state(o):
    """What this prompt needs before it can be pasted (ADR-021). An empty
    attachments field is NOT a blocked prompt: the owner uploads the reference
    photo in the generation tool."""
    if o["pipeline"] != "single-pass":
        return "BLOCKED", "needs compositing, which this pipeline does not do"
    if binds_a_photo(o):
        return "ATTACH THE PHOTO", "paste it, upload the product photo, set " \
                                   "the ratio"
    return "PASTE AS IS", "no attachment, no reference — paste it and set the " \
                          "ratio"


def md(d):
    L = []
    A = L.append
    A("# Image prompts — page 65, handheld UV mattress vacuum")
    A("")
    A("GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — "
      "edit the script and re-run.")
    A("")
    A(f"- page_id `{d['page_id']}` · channel `{d['channel']}` · "
      f"awareness `{d['awareness_stage']}` · registry `{d['registry_version']}`")
    routed = [s for s in d["slots"] if s["options"]]
    oos = [s for s in d["slots"] if not s["options"]]
    n_opts = sum(len(s["options"]) for s in d["slots"])
    gifs = [s for s in d["slots"] if s.get("gif", {}).get("eligible")]
    A(f"- {len(d['slots'])} image slots: {len(routed)} routed, "
      f"{len(oos)} out of library scope")
    A(f"- {n_opts} prompts, three per routed slot, one recommended each")
    A(f"- {len(gifs)} slots earn motion, each carrying a G12 brief plate as a "
      f"fourth option below C — a work order the editor renders alongside the "
      f"still, never a prompt that animates one (ADR-020)")
    A("")
    A("Ratio goes in the generation tool's own aspect-ratio parameter, never in "
      "the prompt text (adapters/nano-banana.md Rule 4). The `Strictly avoid:` "
      "line is not rendered into any prompt (ADR-014); the exclusion list is "
      "kept in the JSON's `avoid` field for a model with a real negative "
      "channel.")
    A("")

    A("## What each prompt needs")
    A("")
    plates = [s for s in d["slots"] if s.get("gif", {}).get("eligible")]
    bare = [(s, o) for s in d["slots"] for o in s["options"]
            if run_state(o)[0] == "PASTE AS IS"]
    withphoto = [(s, o) for s in d["slots"] for o in s["options"]
                 if run_state(o)[0] == "ATTACH THE PHOTO"]
    blocked = [(s, o) for s in d["slots"] for o in s["options"]
               if run_state(o)[0] == "BLOCKED"]
    A(f"**All {n_opts + len(plates)} prompts are paste-and-run.** One prompt, "
      f"one generation call, no compositing and no edit chain (ADR-021). "
      f"{len(blocked)} are blocked on that count.")
    A("")
    A(f"- **{len(withphoto)} want the product photo** — paste the prompt, "
      f"upload the vacuum photo, set the ratio. They carry a G1 reference "
      f"block, so the render is bound to the real product rather than an "
      f"invented one. The `attachments` field is empty because the source "
      f"export supplied no photograph and none was invented; the upload is "
      f"yours to make.")
    A(f"- **{len(bare) + len(plates)} take no attachment at all** — paste and "
      f"set the ratio. {len(bare)} options plus both G12 brief plates, which "
      f"are text cards and bind nothing.")
    A("")
    for s, o in bare:
        v = f" `{o['variant']}`" if o.get("variant") else ""
        A(f"  - `{s['slot_id']}` option {o['opt']} — {o['type']}{v} · "
          f"{o['ratio']}")
    for s in plates:
        A(f"  - `{s['slot_id']}` option D — the G12 brief plate · "
          f"{next(x['ratio'] for x in s['options'] if x['opt'] == s['recommended_opt'])}")
    A("")
    n_rev = sum(len(s["options"]) for s in d["slots"]
                if s["slot_id"].startswith("reviews.photos"))
    A(f"**{n_rev} of them are blocked on a different count** — every "
      f"`reviews.photos` prompt carries an authenticity precondition that has "
      f"nothing to do with attachments. Read the reviews warning below before "
      f"rendering any of them.")
    A("")

    A("## Read this first")
    A("")
    for n in d["page_composition_notes"]:
        head, _, rest = n.partition(". ")
        A(f"- **{head}.** {rest}")
    A("")

    A("## Coverage")
    A("")
    for k, label in (("covered", "Covered"), ("absent", "Absent"),
                     ("absent_but_correct", "Absent on purpose"),
                     ("gaps", "Gaps")):
        vals = d["coverage"].get(k) or []
        if not vals:
            continue
        A(f"**{label}**")
        A("")
        for v in vals:
            A(f"- {v}")
        A("")

    A("## Slot map")
    A("")
    A("| slot | role | asset | recommended | ratio | gif |")
    A("|---|---|---|---|---|---|")
    for s in d["slots"]:
        if s["options"]:
            r = s["recommended_opt"]
            o = next(x for x in s["options"] if x["opt"] == r)
            v = f" `{o['variant']}`" if o.get("variant") else ""
            rec = f"**{r}** — {o['type']} {o['type_version']}{v}"
            ratio = o["ratio"]
        else:
            rec = "— out of scope"
            ratio = "—"
        g = s.get("gif", {})
        gk = f"{g.get('form')} · {g.get('kind')}" if g.get("eligible") else "—"
        A(f"| `{s['slot_id']}` | {s['section_role']} | `{s['asset']}` | {rec} | "
          f"{ratio} | {gk} |")
    A("")

    A("---")
    A("")
    A("## Prompts")
    A("")
    for s in d["slots"]:
        A(f"### `{s['slot_id']}` — {s['section_role']}")
        A("")
        A(f"*{s['placement']}* · asset `{s['asset']}`")
        A("")
        if not s["options"]:
            A(f"**Out of library scope.** {s['out_of_scope_reason']}")
            A("")
            A("---")
            A("")
            continue
        A(f"**Recommended: option {s['recommended_opt']}.** "
          f"{s['recommendation_basis']}")
        A("")
        for o in s["options"]:
            star = "  ← RECOMMENDED" if o["opt"] == s["recommended_opt"] else ""
            v = f" `{o['variant']}`" if o.get("variant") else ""
            A(f"#### Option {o['opt']} — {o['type']} {o['type_version']}{v}{star}")
            A("")
            A(f"- varies on: {o['varies_on']}")
            state, why = run_state(o)
            A(f"- runs: **{state}**" + (f" — {why}" if why else ""))
            A(f"- ratio parameter: **{o['ratio']}** · {o['pipeline']} · "
              f"{len(o['prompt'])} characters")
            A(f"- why: {o['rationale']}")
            if o.get("composition_notes"):
                A(f"- note: {o['composition_notes']}")
            A("")
            A("```prompt")
            A(o["prompt"])
            A("```")
            A("")
        g = s.get("gif", {})
        if g.get("eligible"):
            runs_on = s["recommended_opt"]
            ratio = next(o["ratio"] for o in s["options"]
                         if o["opt"] == runs_on)
            A(f"#### Option D — GIF brief plate · G12 {g['form']}"
              f"  ← ADDITIONAL, not an alternative")
            A("")
            A(f"- varies on: deliverable, not execution — the loop's work order, "
              f"rendered alongside option {runs_on} rather than instead of it")
            A("- runs: **PASTE AS IS** — a text card, so it binds no reference "
              "photo even where the still does")
            A(f"- ratio parameter: **{ratio}** · single-pass · "
              f"{len(g['prompt'])} characters")
            A(f"- argues: **{g['kind']}** · why: {g['reason']}")
            A(f"- note: the plate never ships. Render it as `{g['asset']}`, "
              f"never the slot's own asset name (G12). The editor builds the "
              f"{g['duration_s']}s {g['loop']} from option {runs_on}'s still, "
              f"replaces the plate, and delivers {g['delivery']}.")
            A("")
            A("```prompt")
            A(g["prompt"])
            A("```")
            A("")
        elif g:
            A("#### GIF — none")
            A("")
            A(f"- why: {g['reason']}")
            A("")
    return "\n".join(L) + "\n"


with open(os.path.join(HERE, "prompts.json"), "w", encoding="utf-8") as f:
    json.dump(OUT, f, indent=2, ensure_ascii=False)
    f.write("\n")
with open(os.path.join(HERE, "prompts.md"), "w", encoding="utf-8") as f:
    f.write(md(OUT))

# ---- self-checks, printed so a clean result is never assumed -----------------
routed = [s for s in OUT["slots"] if s["options"]]
print(f"slots {len(OUT['slots'])}  routed {len(routed)}  "
      f"prompts {sum(len(s['options']) for s in OUT['slots'])}")
over = [(s["slot_id"], o["opt"], o["type"], len(o["prompt"]))
        for s in routed for o in s["options"]
        if len(o["prompt"]) > CEIL.get(o["type"], 1800)]
print("over own type ceiling:", over or "none")
bad_ratio = [(s["slot_id"], o["ratio"]) for s in routed for o in s["options"]
             if o["ratio"] not in ("16:9", "4:3", "1:1", "3:4", "9:16")]
print("ADR-016 illegal ratios:", bad_ratio or "none")
leak = [(s["slot_id"], o["opt"]) for s in routed for o in s["options"]
        if "attachments" in o]
print("options carrying a fabricated attachment:", leak or "none")
gifs = [s for s in routed if s.get("gif", {}).get("eligible")]
long_lines = [(s["slot_id"], ln, len(ln.split()))
              for s in gifs
              for ln in s["gif"]["prompt"].split("\n")
              if ln.startswith(("GIF SLOT", "SHOT ", "ACTION ", "RESULT ",
                                "MATCH "))
              and len(ln.replace(" · ", " ").split()) > 7]
print("plate lines over G12's seven words:", long_lines or "none")
clash = [(s["slot_id"], s["asset"]) for s in gifs
         if s["gif"]["asset"] == s["asset"] or "--brief" not in s["gif"]["asset"]]
print("plate render named as a page asset:", clash or "none")
motion = [s["slot_id"] for s in gifs
          if "animate the supplied" in s["gif"]["prompt"].lower()]
print("gif prompts that animate a still:", motion or "none")
composited = [(s["slot_id"], o["opt"], o["pipeline"])
              for s in routed for o in s["options"]
              if o["pipeline"] != "single-pass"]
print("options needing compositing (ADR-021):", composited or "none")
import collections as _c
_st = _c.Counter(run_state(o)[0] for s in routed for o in s["options"])
print("run state across %d options: %s  (+%d brief plates, both PASTE AS IS)"
      % (sum(_st.values()), dict(_st), len(gifs)))
split = [(s["slot_id"], o["opt"], o["type"], o.get("variant"))
         for s in routed for o in s["options"]
         if bool(TYPES.get(o["type"], {}).get("requires_product_photo"))
         != binds_a_photo(o)]
print("prompts exempt from their type's photo flag (each must be a declared "
      "variant exemption or a G1-exempt type):")
for row in split:
    print("   ", row)
# ---- 05-social-snapshot SET DIVERSITY LAW, across the tiles not inside one --
# "When a page requests more than one snapshot, every image must differ
# COMPLETELY - different room class, surface, light temperature, camera distance,
# and content mode where possible." With one option per tile this is checkable,
# and it caught a real defect: the six first-drafted A-variants gave two bedrooms
# AND two kitchens with four at-rest modes.
_snap = [s for s in routed
         if any(o["type"] == "05-social-snapshot" for o in s["options"])]
if _snap:
    # The law says ROOM CLASS, so the raw phrase has to be normalised or the
    # check reads "main bedroom stripped for changing" and "main bedroom" as two
    # different rooms and passes a set that repeats. Controlled vocabulary, and
    # the raw phrase is printed beside its class so a wrong mapping is visible.
    ROOM_CLASSES = ("bedroom", "bathroom", "kitchen", "living room", "landing",
                    "hall", "garage", "car")

    def room_class(scene):
        # Earliest occurrence, not tuple order: "a landing between two bedrooms"
        # is a landing, and scanning the tuple in order called it a bedroom.
        low = scene.lower()
        hits = [(low.index(r), r) for r in ROOM_CLASSES if r in low]
        return min(hits)[1] if hits else "UNCLASSIFIED: " + scene[:30]

    _rooms, _modes, _anchors, _raw = [], [], [], []
    for s in _snap:
        p = s["options"][0]["prompt"]
        _modes.append(re.search(r"CONTENT MODE, ([\w-]+):", p).group(1))
        scene = re.search(r"SCENE: (.{0,60})", p).group(1)
        _raw.append(scene)
        _rooms.append(room_class(scene))
        _anchors.append(re.search(r"ANCHOR: (.{0,28})", p).group(1).strip())
    print()
    print("SET DIVERSITY (05-social-snapshot, %d tiles)" % len(_snap))
    for r, raw in zip(_rooms, _raw):
        print(f"    {r:12} <- {raw[:52]}")
    print("  repeated room classes:",
          sorted({r for r in _rooms if _rooms.count(r) > 1}) or "none")
    print("  content modes:", sorted(set(_modes)),
          "- distinct:", len(set(_modes)), "of", len(_modes))
    print("  duplicate anchors:",
          sorted({a for a in _anchors if _anchors.count(a) > 1}) or "none")
    print("  options per tile:", sorted({len(s["options"]) for s in _snap}),
          "- a repeating section emits one (ADR-022)")

# ---- checked against content.json, not against this script's memory ---------
print()
print("CONTRACT CHECKS (mapping/content.schema.json)")
print("  channel:", CONTRACT["page"]["channel"], "== emitted", OUT["channel"],
      "->", CONTRACT["page"]["channel"] == OUT["channel"])
emitted = {s["slot_id"] for s in OUT["slots"]}
print("  slots in the contract but not emitted:",
      sorted(set(DECLARED) - emitted) or "none")
print("  slots emitted but not in the contract:",
      sorted(emitted - set(DECLARED)) or "none")
role_drift = [(s["slot_id"], s["section_role"], DECLARED[s["slot_id"]]["role"])
              for s in OUT["slots"]
              if s["slot_id"] in DECLARED
              and s["section_role"] != DECLARED[s["slot_id"]]["role"]]
print("  roles that disagree with the contract:", role_drift or "none")
# A type the attribute gates killed must not appear in any option. This is the
# check that makes the gates real rather than remembered.
gate_leak = [(s["slot_id"], o["opt"], o["type"], KILLED[o["type"]])
             for s in routed for o in s["options"] if o["type"] in KILLED]
print("  gates fired:", sorted(KILLED) or "none")
print("  options using a gated-out type:", gate_leak or "none")
# The ratio the layout asks for against the ratio the type can render. Where they
# differ the layout crops, and that is a finding rather than an error - but it is
# now counted rather than described in prose.
crop = [(s["slot_id"], DECLARED[s["slot_id"]]["ratio"], o["opt"], o["ratio"])
        for s in routed for o in s["options"]
        if s["slot_id"] in DECLARED and o["ratio"] != DECLARED[s["slot_id"]]["ratio"]]
print(f"  options rendered at a ratio the slot does not declare: {len(crop)} "
      f"of {sum(len(s['options']) for s in routed)}")
for row in sorted({(a, b, d) for a, b, _c, d in crop}):
    print("     slot declares", row[1], "-> rendered", row[2], "  ", row[0])
# ADR-016: five legal ratios, and the slot's own declaration is checked too.
illegal_declared = sorted({r["ratio"] for r in DECLARED.values()
                           if r["ratio"] not in ("16:9", "4:3", "1:1", "3:4",
                                                 "9:16")})
print("  slot ratios the contract declares outside ADR-016:",
      illegal_declared or "none")
print()

# One-type-once: a repeat is legal only as the runbook's rung 4, another
# execution differing on a named dimension. Printed so a repeat is never silent.
seen = _c.defaultdict(list)
for s in routed:
    r = s["recommended_opt"]
    o = next(x for x in s["options"] if x["opt"] == r)
    seen[o["type"]].append((s["slot_id"], o.get("variant"),
                            (o.get("axes") or {}).get("inset_mode")))
print("types recommended more than once (each must be a rung-4 repeat):")
for t, uses in seen.items():
    if len(uses) > 1:
        print("   ", t, uses)

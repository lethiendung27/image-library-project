#!/usr/bin/env python3
"""Build prompts.json and prompts.md for page 37.

prompts.json is the source of truth (query/output.schema.json); prompts.md is
generated from it and is never hand-edited (query/runbook.md Step 7).

Run from anywhere:  python3 query/sessions/37-.../build.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- prompts ---

P_HERO_A = """TYPE: 06-relief-hero v1.12 --ugc, inset --recall
REGISTER: shot on a phone by an ordinary person. Slightly off exposure, mild
overexposure on skin and on the windscreen, no rim light, framing casual and a
little too close. The car is left exactly as it is.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion, identical in
every layer. Preserve shape, proportions, material, finish and colour exactly.

[SUBJECT]
Man in his late forties in an open-collar work shirt, sitting in the driver's
seat of an ordinary estate car at the end of the working day, seen from a
front three-quarter angle through the open driver's door. He is settled back,
one hand loose on the wheel, gaze out through the windscreen, an unforced ease
about him.

[PRODUCT]
The cushion in place beneath and behind him: its seat section under his hips,
its lumbar section rising into the small of his back, the line of contact
continuous with no gap left behind the lumbar curve. Unobstructed and legible.

[SETTING]
The car filled to the edges with things that belong there: a travel mug in the
console, a lanyard on the mirror, a folded jacket on the passenger seat, a
phone mount, hedges and a driveway beyond the open door. None of them carries
printed words. Background soft but never blank.

[LIGHT]
Flat late-afternoon daylight through the windscreen and the open door. No
studio light, no rim light.

[LAYOUT]
He sits to the right of the frame. In the upper left corner sits one small
rectangular panel about a sixth of the picture's width, and nothing else
occupies that side.

[PANEL CONTENT]
The same man in the same car on an earlier day, twisted sideways and gripping
the door frame to lever himself out, face tight. This panel is fully
desaturated to grey while the rest of the picture keeps its colour, and it
matches the main picture in sharpness and light quality."""

P_HERO_B = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man in his late forties in an open-collar work shirt, half out of the driver's
seat of an estate car on his own driveway, both hands braced — one on the door
frame, one on the seat back — levering himself upward. Under that force: the
hips still folded, one shoulder driven up, the trailing leg dragging rather
than stepping, the whole body rising in one stiff block instead of unfolding.
Face: jaw set, eyes down, breath held.

[EVIDENCE]
The driver's seat he is leaving has a deep gap where its base meets the
backrest, and a flattened foam pad has slid forward and folded into it.

[ENVIRONMENT]
A suburban driveway at the end of the working day, with the clutter of that
routine: a lunch bag on the passenger seat, a lanyard swinging from the
mirror, a wheelie bin by the gate, a neighbour's hedge. Nothing tidied.

[GAZE] unaware of the camera, gaze down at the ground by his feet.

[LIGHT] low-key. Key: low late-afternoon sun from behind the car, hard. Weak
fill. Deep shadow through the open door.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth
of field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

P_S0_A = """TYPE: 01-pain-scene v1.14 --candid --marked
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man in his late forties in an open-collar work shirt, at an office desk in
mid-afternoon, part-way through pushing himself up out of the chair: both
hands driving down on the armrests, hips half risen, the chair rolling back a
little under him. Under that force: the shoulders hunched up towards his ears,
the neck set, one heel dug into the carpet.
Face: eyes screwed shut, breath held, teeth set.

[EVIDENCE]
The chair he is leaving has a deep gap where the seat base meets the backrest,
and a flattened grey foam cushion has slid forward and folded into it.

[ENVIRONMENT]
An ordinary open-plan office, mid-afternoon. The lived-in clutter of that
place: a cold mug, a lanyard over a monitor, a coat on the chair back, papers
pushed aside. Nothing arranged, nothing removed to tidy the frame.

[GAZE] unaware of the camera, gaze down at the desk.

[LIGHT] low-key. Key: low sun through a blind at the left, hard and warm.
Fill: weak overhead strip light. Rim along the shoulder. Deep shadow across
most of the frame.

[MARK]
ONE soft red radial glow covering THE LOWER BACK where it meets the chair gap,
fading out before it reaches his shoulders or the seat. It is the only mark in
this image.

[FORBIDDEN] No insets, no split panels, no badges, no glyphs. Nothing else in
the frame is marked.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth
of field, 35mm. Red appears only in the glow.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

P_S0_B = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man in his late forties in an open-collar work shirt, at an office desk in
mid-afternoon, part-way through pushing himself up out of the chair: both
hands driving down on the armrests, hips half risen, the chair rolling back a
little under him. Under that force: the shoulders hunched up towards his ears,
the neck set, one heel dug into the carpet.
Face: eyes screwed shut, breath held, teeth set.

[EVIDENCE]
The chair he is leaving has a deep gap where the seat base meets the backrest,
and a flattened grey foam cushion has slid forward and folded into it. His
shirt is rucked up out of his waistband where his back has been pressed into
that gap all afternoon.

[ENVIRONMENT]
An ordinary open-plan office, mid-afternoon. The lived-in clutter of that
place: a cold mug, a lanyard over a monitor, a coat on the chair back, papers
pushed aside. Nothing arranged, nothing removed to tidy the frame.

[GAZE] unaware of the camera, gaze down at the desk.

[LIGHT] low-key. Key: low sun through a blind at the left, hard and warm.
Fill: weak overhead strip light. Rim along the shoulder. Deep shadow across
most of the frame.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth
of field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged.
No marks, no overlays, no insets, no panels."""

P_S1_A = """TYPE: 04-proof-lockedframe v1.13 --rivals — PANEL 1 GENERATION
REGISTER: documentary photography. No overlays, badges, arrows or text.

[SCENE]
An unremarkable mesh-backed office chair pulled out from the corner of a desk,
photographed from a standing position slightly above seat height. Office
carpet, daylight from one window to the left, a few ordinary desk objects
visible on the desk edge behind the chair. Nothing styled, nothing tidied.

[SUBJECT OF THIS FRAME]
A flat square foam seat pad lying on the seat base — ordinary, in good
condition, the kind sold everywhere, compressed thin through the middle where
someone has been sitting on it. The gap where the seat base meets the backrest
is clearly visible behind it and is still open: the pad does not reach it.

[GRADE] Muted and cool.

[FAIRNESS] The pad is not dirty, torn or worn out. It is photographed with the
same respect any product would get: honest exposure, no hero light, no styling
that flatters or condemns it.

STYLE: honest documentary product test photography, unstyled, natural, sharp.
No people, no hands, no brand marks."""

P_S1_B = """TYPE: 04-proof-lockedframe v1.13 --verdict — PANEL 1 GENERATION
REGISTER: documentary photography. No overlays, badges, arrows or text.

[SCENE]
An unremarkable mesh-backed office chair pulled out from the corner of a desk,
photographed from a standing position slightly above seat height. Office
carpet, daylight from one window to the left, a few ordinary desk objects
visible on the desk edge behind the chair. Nothing styled, nothing tidied.

[SUBJECT OF THIS FRAME]
A flat square foam seat pad lying on the seat base — ordinary, in good
condition, the kind sold everywhere, compressed thin through the middle where
someone has been sitting on it. The gap where the seat base meets the backrest
is clearly visible behind it and is still open: the pad does not reach it.

[GRADE] Neutral, honest to the room.

[FAIRNESS] The pad is not dirty, torn or worn out. It gets exactly the same
photographic respect as every other frame in this test: identical exposure,
identical tidiness, identical framing generosity.

STYLE: honest documentary product test photography, unstyled, natural, sharp.
No people, no hands, no brand marks."""

P_S2_A = """TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, airbrushed with soft gradients and modelled volume.
NOT photography, NOT 3D.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cushion.

[FRAME] The whole seated body in shot in both panels, the chair small within
it.

[GROUND] A dark teal field, stepping once in value at the divider: the right
half one clear step lighter.

[BODY] Exactly one seated figure per panel, same scale and same side view in
both: the pelvis, sacrum and lumbar spine in warm ivory inside a translucent
seated outline. Not a full skeleton, no skull.

[PANELS]
LEFT, wrong: the figure sitting on an ordinary office chair, drawn
realistically and unbranded, with an open gap where its seat base meets its
backrest. The sacrum has slid back into that gap, the pelvis has rolled
backward, and the lumbar curve has collapsed into a backward bow.
RIGHT, correct: the same figure at the same interface, sitting on the
reference cushion, drawn at a size and angle where its L shape is obvious. The
seat section is under the hips and the lumbar section fills the gap against
the sacrum; the pelvis stands upright and the lumbar curve holds its forward
arch.
The spine appears in both panels. The chair and the cushion each touch the
pelvis where they act, and neither covers it.

[MARKS] Three marks, no others.
measure: two dashed straight lines, one per panel, identical in thickness and
dash pattern, each running from the front face of the backrest to the back of
the sacrum and stopping at both. Red left, blue right. Only the distance
spanned differs.
force: one red double-headed curved arrow, left panel only, following the seat
surface backward into the gap.
verdict: one badge in the top corner of each panel, a filled solid disc with
the glyph cut out of it, same diameter in both: red with an X on the left,
green with a check on the right.

Red is wrong, blue is correct, green is the badge, warm ivory is structure;
nothing else carries colour."""

P_S2_B = """TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, flat vector: flat fills, hard edges, no gradients.
NOT photography, NOT 3D.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cushion.

[FRAME] The whole seated body in shot in both panels, the chair small within
it.

[GROUND] A deep indigo field, stepping once in value at the divider: the right
half one clear step lighter.

[BODY] Exactly one seated figure per panel, same scale and same side view in
both: the pelvis, sacrum and lumbar spine in warm ivory inside a translucent
seated outline. Not a full skeleton, no skull.

[PANELS]
LEFT, wrong: the figure sitting on an ordinary office chair, drawn
realistically and unbranded, with an open gap where its seat base meets its
backrest. The sacrum has slid back into that gap and the pelvis has rolled
backward.
RIGHT, correct: the same figure at the same interface, sitting on the
reference cushion, drawn at a size and angle where its L shape is obvious, the
seat section under the hips and the lumbar section filling the gap against the
sacrum, the pelvis upright.
The spine appears in both panels. The chair and the cushion each touch the
pelvis where they act, and neither covers it.

[MARKS] Three marks, no others.
measure: two dashed straight lines, one per panel, identical in thickness and
dash pattern, each running from the front face of the backrest to the back of
the sacrum and stopping at both. Red left, blue right. Only the distance
spanned differs.
pressure: one filled region per panel bounded by the contact surface between
the body and the seat, as wide as that contact and never a line or an edge
glow — red left where load falls on the tailbone, blue right where it
spreads across the seat.
verdict: one badge in the top corner of each panel, a filled solid disc with
the glyph cut out of it, same diameter in both: red with an X on the left,
green with a check on the right.

Red is wrong, blue is correct, green is the badge, warm ivory is structure;
nothing else carries colour."""

P_S3_A = """TYPE: 03-mechanism-ghostbody v2.2
REGISTER: 3D technical render.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cushion.

[PANELS] Two equal panels side by side, each a full 3D technical render,
divided by a single thin vertical line. Left is the wrong state, right is the
correct state.

[GHOST] A featureless matte white mannequin — no face, no hair, no clothing,
no skin tone — seated on a plain matte white chair form in side view, hands
resting on the thighs. The same pose, the same angle and the same chair form
in both panels. Cross-sectioned along the vertical plane through the spine so the interior
shows.

[CUTAWAY] The lumbar spine, sacrum and pelvis, inside the body silhouette. In
the left panel the sacrum has slid back into the open space behind the seat
and the pelvis is rolled backward, the lumbar column bowed the wrong way. In
the right panel the pelvis stands upright and the lumbar column holds its
forward curve.

[PRODUCT] Right panel only: the reference cushion on the chair form, its seat
section under the pelvis and its lumbar section filling the space behind the
sacrum, in the same side view. Its contour visibly follows the lumbar column's
curve. It keeps its own reference colours and carries no signal colour at all.
No mark is placed on it.

[MARKS] Four marks and no others, every one a flat unshaded hard-edged overlay
laid on top of the render, obviously added.
structure: the lumbar vertebrae, sacrum and pelvis in warm off-white ivory, in
both panels.
stress: a flat red overlay on the two lowest lumbar vertebrae, left panel only.
support: a flat blue band beside the lumbar column, on the side away from the
cushion, running only the length the cushion's lumbar section reaches. Right
panel only, never a fill of the bone.
verdict: one badge in the top corner of each panel, a filled solid disc with
the glyph cut out of it: red with an X on the left, green with a check on the
right.

PALETTE LOCK: everything else in the frame is achromatic white and grey. The
cushion is the only object with a real material finish."""

P_S3_B = """TYPE: 03-mechanism-ghostbody v2.2
REGISTER: 3D technical render.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cushion.

[PANELS] Two equal panels side by side, each a full 3D technical render,
divided by a single thin vertical line. Left is the wrong state, right is the
correct state.

[GHOST] A featureless matte white mannequin — no face, no hair, no clothing,
no skin tone — seated on a plain matte white chair form, seen from behind and
slightly above, arms hanging. The same pose, the same angle and the same chair
form in both panels. The body is cross-sectioned along the horizontal plane
just above the seat so the sitting bones and the tailbone show from below.

[CUTAWAY] The two sitting bones and the tailbone, inside the body silhouette.
In the left panel the tailbone has dropped lowest and carries the load. In the
right panel the two sitting bones sit level and lowest and the tailbone is
clear of the surface.

[PRODUCT] Right panel only: the reference cushion on the chair form, its seat
section under the sitting bones, in the same view. Its contoured relief
visibly aligns with the tailbone's position. It keeps its own reference
colours and carries no signal colour at all. No mark is placed on it.

[MARKS] Four marks and no others, every one a flat unshaded hard-edged overlay
laid on top of the render, obviously added.
structure: the sitting bones and the tailbone in warm off-white ivory, in both
panels.
stress: a flat red overlay on the tailbone, left panel only.
support: a flat blue band beside each sitting bone, on the side away from the
cushion, running only the length the cushion's seat section reaches. Right
panel only, never a fill of the bone.
verdict: one badge in the top corner of each panel, a filled solid disc with
the glyph cut out of it: red with an X on the left, green with a check on the
right.

PALETTE LOCK: everything else in the frame is achromatic white and grey. The
cushion is the only object with a real material finish."""

P_S4_A = """TYPE: 06-relief-scene v1.0
REGISTER: candid documentary photograph. Single frame. NO graphic overlays.

[SUBJECT]
The same man in his late forties as the paired pain image, in an open-collar
shirt and a jacket of the same muted palette, walking past a parade of shops
in the early evening, pausing a moment mid-stride.
Gaze on his own reflection in the shop window beside him.
Expression: a small closed-mouth smile, private and understated.
Not performing, not aware of a camera.

[EVIDENCE OF CHANGE]
His back is straight and his hips are square under him: the trunk stacked over
the pelvis, both shoulders level and dropped, the trailing leg swinging
through into a full even stride, neither hand anywhere near his lower back.
This must be readable in the direct view and in the reflection alike.

[REFLECTION]
The shop window fills about a third of the frame and shows him from a
different angle, sharp enough to read the line of his back. The reflection is
geometrically consistent with where he is standing.

[ENVIRONMENT]
An ordinary suburban shopping parade he would pass on an evening walk. Two or
three blurred passersby, a bus shelter, a wheelie bin, damp pavement. Ordinary
weather, nothing aspirational, no styling.

[LIGHT]
Even natural early-evening daylight, bright, soft shadows. Slightly kinder
than the paired pain image but the same time-of-day character. No golden hour,
no rim light.

[GRADE]
Muted blue-grey matching the paired pain image, light film grain, shallow
depth of field. Desaturated, never warm-boosted.

STYLE: candid lifestyle photography, natural, unposed, sharp.
NO text, no logo, no watermark, no product."""

P_S4_B = """TYPE: 06-relief-hero v1.12 --ugc, inset --none
REGISTER: shot on a phone by an ordinary person. Slightly off exposure, mild
overexposure on skin and windows, no rim light, framing casual and a little
too close. The room is left exactly as it is.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly.

[SUBJECT]
Man in his late forties in an open-collar work shirt, seated at his own desk
late in the working day, leaned back with his weight through his hips, one arm
hooked over the chair back, talking to somebody out of frame. Relaxed, gaze
away from the cushion.

[PRODUCT]
The cushion in place on the chair beneath and behind him, seen from a rear
three-quarter angle so the seat section under his hips and the lumbar section
against his lower back are both visible, the contact line continuous and
unobstructed.

[SETTING]
His own office corner, filled to the edges with what lives there: a keyboard
pushed back, a mug, a coat on a hook, a stack of trays, a cable run along the
skirting, a window with a blind half down. None of them carries printed words.
Background soft but never blank.

[LIGHT]
Flat late-afternoon daylight from the window plus the overhead strip light. No
studio light, no rim light.

[LAYOUT]
He sits to the left of the frame; the room's own depth fills the right side.
No panel, no inset, no second image anywhere in the frame."""

P_G0 = """TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion simply sitting where it now lives, on a
wooden dining chair pushed under a kitchen table, still holding the shallow
creases of the compression bag it came out of.

[SCENE] An ordinary kitchen photographed as found: crumbs on the table, a
cereal bowl not cleared, a chair pulled out at an angle. One coiled phone
charger lies on the table beside it. Nothing tidied, nothing added.

[LIGHT] Morning window daylight only, cool and a bit flat.

[CAMERA TRUTH] Framing slightly off-centre and taken from standing height
looking down; focus adequate but casual; exposure honest to the room. No
negative space, no rule of thirds, no depth-of-field styling.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders."""

P_G1 = """TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] in-use: the cushion fitted into a car's driver seat, one
forearm reaching in through the open door to press its lumbar section back
into the seat corner. No face, no other part of the person.

[SCENE] The inside of an ordinary used car photographed as found: a crumpled
receipt in the door pocket, floor mats gritty, a child's toy in the footwell
behind. One key fob dangles from the ignition. Nothing tidied.

[LIGHT] Late evening, the car's dome light plus orange street light through
the windscreen. Warm and uneven.

[CAMERA TRUTH] Framing too close and tilted, taken leaning in through the
door; mild motion softness; exposure honest to the dark interior.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders."""

P_G2 = """TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion sitting in a gaming chair in a bedroom,
seen from across the room with the chair turned half away from the desk.

[SCENE] A young adult's bedroom photographed as found: an unmade bed edge in
the foreground, a hoodie over the chair arm, cables trailing down the desk
leg. One empty energy-drink can stands on the desk. Nothing tidied.

[LIGHT] Night. A warm bedside lamp on one side and the cold blue glow of two
monitors on the other, mixing badly.

[CAMERA TRUTH] A wide frame taken from the doorway, slightly tilted; visible
noise in the shadows; exposure honest to the dim room.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders."""

P_G3 = """TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] kit-flatlay: the cushion just unpacked on a hallway floor, laid
out the way the owner dropped it — the cushion itself, its zip-off cover half
peeled back, and the flattened compression bag it shipped in, slightly
disordered. Real contents only, nothing added.

[SCENE] A narrow hallway photographed as found: worn laminate, a doormat with
grit on it, one shoe on its side at the frame edge. One pair of scissors lies
where it was put down. Nothing tidied.

[LIGHT] A single overhead hall bulb, warm and dim, throwing one hard shadow.

[CAMERA TRUTH] Shot from standing height straight down, too close, the frame
cutting the bag off at one edge; focus adequate but casual.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders."""

P_G4 = """TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] in-use: the cushion fitted into a wheelchair seat, two fingers
entering the frame to tuck its lumbar section down against the backrest. No
face, no other part of the person.

[SCENE] A living room by a window, photographed as found: a side table with a
week's post on it, a folded blanket over the sofa arm, a rug rucked at one
corner. One walking stick leans against the wall. Nothing tidied.

[LIGHT] Flat grey overcast daylight through the window, no lamps on.

[CAMERA TRUTH] A medium frame taken from a seated position looking across;
slightly off-centre; exposure honest and a little dull.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders."""

P_G5 = """TYPE: 05-social-snapshot v1.0
REGISTER: a real customer's phone photo. One frame. No layout, no layers.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the cushion. Preserve shape,
proportions, material, finish and colour exactly. It may be partly obscured,
angled or cropped the way casual photography actually crops things.

[CONTENT MODE] at-rest: the cushion on the driver's seat of a lorry cab, the
door open and nobody in it yet.

[SCENE] A working lorry cab photographed as found: a bunk curtain half drawn
behind the seat, a grubby dashboard, a hi-vis jacket bundled on the passenger
seat. One vacuum flask stands in the door pocket. Nothing tidied.

[LIGHT] Dawn. Cold blue light through the windscreen, the cab interior still
dark.

[CAMERA TRUTH] Too close, shot from below at the open door looking up into the
cab, tilted; noticeable noise; exposure honest to the low light.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
No faces, no text overlays, no logo, no watermark, no badges, no borders."""

# ------------------------------------------------------------- avoid lines ---

AV_PAIN = ("[G6] + red glow, pain hotspots, graphic overlay, arrows, badges, split panel, "
           "white background, studio lighting, stock photo look, posed model, fake grimace, "
           "smiling, clean staged interior, saturated colors, advertising composition, "
           "product placement")
AV_HERO = ("[G6] + cluttered background, dark moody lighting, pain cues in main scene, "
           "blurry product, inconsistent product between layers, same angle repeated, "
           "fabricated colorways, mixed illustration and photo inside one inset half, "
           "invented spray or mist, fake steam; ugc adds: professional lighting, studio "
           "setup, clean composition, styled interior, negative space, color graded, "
           "retouched skin, magazine look, glossy, symmetrical framing")
AV_HERO_RECALL = AV_HERO + ("; recall adds: unlabelled before-state inset, low resolution "
                            "inset, inset darker than hero, inset from a different "
                            "photographic source, more than one arrow, arrow pointing from "
                            "now to past")
AV_LOCK = ("[G6] + badges, arrows, glows, checkmarks, one panel brighter, inconsistent "
           "lighting between panels, studio background, clean styled set, staged perfection, "
           "saturated colors, red or green cues, motion blur, people, hands, brand logos, "
           "recognizable trademarks; handheld adds: identical framing between panels, "
           "pixel-perfect alignment, tripod shot, 3D render look, CGI, product visualization")
AV_RIVALS = AV_LOCK + "; rivals adds: damaged or dirty items, exaggerated flaws, one item obviously better"
AV_VERDICT = AV_LOCK + ("; verdict adds: last panel brighter or cleaner than the others, hero "
                        "lighting on the final panel, alternatives made to look broken, "
                        "cluttered first panels")
AV_CAUSE = ("[G6] + photographic elements, 3D render, photorealistic skin, human face, facial "
            "features, gore, wet tissue, correct side on the left, both dashed lines "
            "identical, missing badge on either panel, different figure scale between panels, "
            "extra signal colours, saturated ground, anatomically wrong structures, "
            "background pattern")
AV_GHOST = ("[G6] + human face, facial features, hair, skin tone, clothing, photographic "
            "background, environment, furniture, shadows on floor, extra colors, rainbow "
            "palette, anatomically wrong structures, floating disconnected organs, dimension "
            "lines overlapping product edge, cluttered inset, gore, realistic flesh, medical "
            "horror")
AV_SCENE = ("[G6] + badges, arrows, overlays, looking at camera, posing, laughing, arms "
            "raised, celebration gesture, golden hour, warm flattering light, glamour "
            "lighting, beauty retouching, plastic skin, aspirational travel location, empty "
            "clean street, styled outfit, geometrically wrong reflection, reflection out of "
            "focus, product in frame, saturated colors, stock photo look")
AV_SNAP = ("[G6] + studio lighting, softbox reflections, seamless background, negative space, "
           "color grading, professional composition, styled props, badges, borders, star "
           "ratings, reviewer names, avatars, text overlays, product render look, perfect "
           "symmetry, magazine polish, influencer aesthetic")

# ------------------------------------------------------------------- steps ---

STEPS_RIVALS = [
    "Pass 1 — generate the frame above as a single image. It carries no multi-panel language at all: one chair, one item on it.",
    "Pass 2 — edit that image: 'Keep the chair, the desk, the carpet, the window light, the objects on the desk edge and the camera position. Remove the foam pad from the seat. Buckle a separate strap-on lumbar pillow to the backrest, in good condition, its lower edge stopping well above the seat base so the seat-to-backrest gap stays open. Reshoot from a standing position, so framing and angle shift slightly the way a hand-held camera does.'",
    "Pass 3 — edit the pass-1 image again: 'Keep the chair, the desk, the carpet, the window light, the objects on the desk edge and the camera position. Remove the foam pad. Push a neatly folded bath towel into the gap between the seat base and the backrest, the way somebody actually does it. Reshoot from a standing position, so framing and angle shift slightly.'",
    "Assembly — place the three frames side by side in the page layout, in this order, with thin white gutters and no outer border. No panel is retouched to be brighter or cleaner than the others.",
]

STEPS_VERDICT = [
    "Pass 1 — generate the frame above as a single image. It carries no multi-panel language at all: one chair, one item on it.",
    "Pass 2 — edit that image: 'Keep the chair, the desk, the carpet, the window light, the objects on the desk edge and the camera position. Remove the foam pad from the seat. Buckle a separate strap-on lumbar pillow to the backrest, in good condition, its lower edge stopping well above the seat base so the seat-to-backrest gap stays open. Reshoot from a standing position, so framing and angle shift slightly.'",
    "Pass 3 — edit the pass-1 image again, with the product photo attached: 'Keep the chair, the desk, the carpet, the window light, the objects on the desk edge and the camera position. Remove the foam pad. Put the attached cushion on the chair instead, its seat section on the seat base and its lumbar section filling the gap against the backrest, matching the attached photo exactly. Same exposure and same tidiness as the other frames, no hero light. Reshoot from a standing position, so framing and angle shift slightly.'",
    "Assembly — place the three frames side by side with thin white gutters, product LAST. Order rule: left-to-right reading ends on the product, and that is the resolution position.",
]

# ------------------------------------------------------------------- slots ---

SLOTS = [
    {
        "slot_id": "hero.image",
        "section_role": "hero",
        "asset": "01-hero-relief-hero-ugc.jpg",
        "placement": "advertorial header, full width above the byline (700x394 in the export)",
        "options": [
            {
                "opt": "A", "varies_on": "baseline",
                "type": "06-relief-hero", "type_version": "1.12",
                "variant": "--ugc, inset --recall (FORM 1)",
                "axes": {"register": "ugc", "inset_mode": "recall"},
                "ratio": "16:9", "pipeline": "single-pass",
                "asset_candidate": "01-hero-relief-hero-ugc--A.jpg",
                "prompt": P_HERO_A, "avoid": AV_HERO_RECALL,
                "rationale": "The headline is relief-framed ('How I Finally Ended My Sitting Pain'), so the header has to close the loop, not open a wound. The recall panel keeps the problem present without letting pain into the hero, which this type forbids.",
                "composition_notes": "Rung-2 derivation, declared: mapping/slot-rules.md gives advertorial hero to 01-pain-scene, but that type is spent at story.0 by the exact beat it exists for, and 06-relief-hero's own --ugc block names 'advertorial header' as a channel. G7-X holds: seated in the car in both the hero and the panel. The zone names never reach the model — the panel is described by its corner.",
            },
            {
                "opt": "B", "varies_on": "type: 01-pain-scene",
                "type": "01-pain-scene", "type_version": "1.14",
                "variant": "--candid",
                "ratio": "16:9", "pipeline": "single-pass",
                "asset_candidate": "01-hero-relief-hero-ugc--B.jpg",
                "prompt": P_HERO_B, "avoid": AV_PAIN,
                "rationale": "The slot-rules cell for advertorial hero, taken literally. The subtitle IS pain-framed ('Why standard cushions leave you stiff-legged and exhausted'), so a cold-open header is defensible.",
                "composition_notes": "PICKING THIS FORCES A RE-ROUTE: 01-pain-scene would then be spent here and story.0 needs its own answer, and 06-relief-scene at story.4 must pair with whichever pain-scene survives (same person, same palette). No product in frame — this type carries none by definition.",
            },
        ],
        "gif": {
            "eligible": True, "form": "whole-frame",
            "reason": "The header's reason to exist is a man at ease at the end of a drive — a held state, but the recall panel makes the frame a before-and-after, and a loop can carry that transition. Motion is optional here, not earned by the still alone.",
            "asset": "01-hero-relief-hero-ugc.mp4",
            "duration_s": 3, "loop": "ping-pong",
            "shot": "Locked phone frame, no camera move",
            "action": "Shoulders settle back, one slow breath",
            "result": "A man who is comfortable sitting still",
            "match": "ugc register: phone exposure, no rim light",
            "delivery": "mp4/webm, under 2 MB",
        },
    },
    {
        "slot_id": "story.0.image",
        "section_role": "problem-agitation",
        "asset": "02-story0-pain-scene.jpg",
        "placement": "beside story block 0, 'My 3:00 PM Office Nightmare' (600x450)",
        "options": [
            {
                "opt": "A", "varies_on": "baseline",
                "type": "01-pain-scene", "type_version": "1.14",
                "variant": "--candid --marked",
                "axes": {"marked": "on"},
                "ratio": "4:3", "pipeline": "single-pass",
                "asset_candidate": "02-story0-pain-scene--A.jpg",
                "prompt": P_S0_A, "avoid": AV_PAIN,
                "rationale": "The copy's own scene, beat for beat: the ache starts at the desk in mid-afternoon and standing up is the hard part. The type's use_when names exactly this — cold traffic, the opening image of a story.",
                "composition_notes": "Mark admission gate passed: the fault has a PLACE (the lower back against the chair gap), so a glow can locate it. Exactly one mark, count closed in its own slot. No product — this type carries none.",
            },
            {
                "opt": "B", "varies_on": "axis: marked=off",
                "type": "01-pain-scene", "type_version": "1.14",
                "variant": "--candid",
                "axes": {"marked": "off"},
                "ratio": "4:3", "pipeline": "single-pass",
                "asset_candidate": "02-story0-pain-scene--B.jpg",
                "prompt": P_S0_B, "avoid": AV_PAIN,
                "rationale": "The type says --marked is a choice and a set should carry mark-free cases deliberately: a mark competes with the evidence it points at. Here the body's own line is the evidence, and the rucked shirt replaces the glow.",
                "composition_notes": "Same scene as A with the mark removed and one physical detail added in its place, so the pair tests whether the glow is earning anything.",
            },
        ],
        "gif": {
            "eligible": True, "form": "whole-frame",
            "reason": "The slot's declared reason to exist is the act of standing up out of the chair — a transition, so it is temporal.",
            "asset": "02-story0-pain-scene.mp4",
            "duration_s": 2, "loop": "ping-pong",
            "shot": "Locked frame, medium, no camera move",
            "action": "He pushes up, stalls, hips stay folded",
            "result": "Standing up is the hard part",
            "match": "Desaturated blue-grey grade, film grain",
            "delivery": "mp4/webm, under 2 MB",
        },
    },
    {
        "slot_id": "story.1.image",
        "section_role": "comparison",
        "asset": "03-story1-rivals.jpg",
        "placement": "beside story block 1, 'I Spent Hundreds On Half-Measures' (600x450)",
        "options": [
            {
                "opt": "A", "varies_on": "baseline",
                "type": "04-proof-lockedframe", "type_version": "1.13",
                "variant": "--rivals",
                "axes": {"camera": "handheld"},
                "ratio": "4:3", "pipeline": "multi-pass", "steps": STEPS_RIVALS,
                "asset_candidate": "03-story1-rivals--A.jpg",
                "prompt": P_S1_A, "avoid": AV_RIVALS,
                "rationale": "This type's use_when is written for this exact section: 'the I tried three things beat of an advertorial'. The three panels are the three things the copy names — a flat pad, a separate lumbar pillow, and the improvised fix.",
                "composition_notes": "THE ONE SLOT WITH NO PRODUCT IN FRAME. That is what --rivals is: none of them wins and the image makes no claim. Legal on advertorial only. CAPABILITY GATE: the strict camera needs compositing, which is not available here, so this runs handheld — the frames are three separate generations and the slight framing drift is honest, not a fault.",
            },
            {
                "opt": "B", "varies_on": "axis: variant=verdict",
                "type": "04-proof-lockedframe", "type_version": "1.13",
                "variant": "--verdict",
                "axes": {"camera": "handheld", "variant": "verdict"},
                "ratio": "4:3", "pipeline": "multi-pass", "steps": STEPS_VERDICT,
                "asset_candidate": "03-story1-rivals--B.jpg",
                "prompt": P_S1_B, "avoid": AV_VERDICT,
                "rationale": "Same locked frame, but the product takes the last panel. Choose this if the section should resolve rather than only indict — the reader at this stage is sceptical of everything, and the copy has not yet named the cushion.",
                "composition_notes": "Fairness rule binds hard: panels 1 and 2 get identical exposure, tidiness and framing generosity, and the difference must be visible in the OBJECTS, never in the lighting. It may win by physics, never by treatment. Product last — left-to-right reading ends on it.",
            },
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "The slot exists to hold three states side by side for comparison, not to show one thing changing. A census is spatial, not temporal, and motion would only pull the eye to whichever panel moves.",
        },
    },
    {
        "slot_id": "story.2.image",
        "section_role": "cause",
        "asset": "04-story2-cause-anatomy.jpg",
        "placement": "beside story block 2, 'The Pelvic Roll Trap Discovered' (600x450)",
        "options": [
            {
                "opt": "A", "varies_on": "baseline",
                "type": "02-cause-anatomy", "type_version": "1.15",
                "variant": "--diagnostic",
                "axes": {"style": "airbrushed", "frame": "whole", "ground": "dark-field"},
                "ratio": "4:3", "pipeline": "single-pass",
                "asset_candidate": "04-story2-cause-anatomy--A.jpg",
                "prompt": P_S2_A, "avoid": AV_CAUSE,
                "rationale": "The section names a culprit object and its mechanism — 'standard chairs have a deep gap at the backrest, the pelvis rolls backward into this void'. That is this type's sentence exactly.",
                "composition_notes": "REMOVAL TEST PASSED: take the chair's gap away and the pelvis stops rolling, so the two panels are one structure in two states rather than accumulated damage. measure admission passed: the gap spanned goes from a real distance to contact, well past the 2:1 floor. Four marks, at the type's measured ceiling for four.",
            },
            {
                "opt": "B", "varies_on": "execution: flat-vector style, pressure instead of force and contour",
                "type": "02-cause-anatomy", "type_version": "1.15",
                "variant": "--diagnostic",
                "axes": {"style": "flat-vector", "frame": "whole", "ground": "dark-field"},
                "ratio": "4:3", "pipeline": "single-pass",
                "asset_candidate": "04-story2-cause-anatomy--B.jpg",
                "prompt": P_S2_B, "avoid": AV_CAUSE,
                "rationale": "Flat vector holds the measure dash pattern better than airbrush does, and pressure answers a second question the copy raises — where the load actually lands when the pelvis rolls.",
                "composition_notes": "Same removal test, same measure pair. pressure is a filled region bounded by the contact surface, never a line and never an edge glow — that distinction is what the mark failed on before.",
            },
        ],
        "gif": {
            "eligible": True, "form": "whole-frame",
            "reason": "The declared argument is a pelvis rolling backward into a void — a state changing, which is temporal. A two-panel illustration can loop between its own states.",
            "asset": "04-story2-cause-anatomy.mp4",
            "duration_s": 3, "loop": "ping-pong",
            "shot": "Static illustration, no camera move",
            "action": "Pelvis rolls back, lumbar curve collapses",
            "result": "The gap is what does it",
            "match": "Flat 2D illustration, G3 palette only",
            "delivery": "mp4/webm, under 2 MB",
        },
    },
    {
        "slot_id": "story.3.image",
        "section_role": "mechanism",
        "asset": "05-story3-ghostbody.jpg",
        "placement": "beside story block 3, 'An Integrated, One-Piece Solution' (600x450)",
        "options": [
            {
                "opt": "A", "varies_on": "baseline",
                "type": "03-mechanism-ghostbody", "type_version": "2.2",
                "variant": None,
                "ratio": "4:3", "pipeline": "single-pass",
                "asset_candidate": "05-story3-ghostbody--A.jpg",
                "prompt": P_S3_A, "avoid": AV_GHOST,
                "rationale": "The section explains WHY the shape works — 'keeping the hips and lumbar spine aligned as a single unit' — through a mechanism inside the body that cannot be filmed. body_contact is true, so ghostbody serves and xray does not.",
                "composition_notes": "Every mark in this type is unproven — zero records in eval/render-tests.jsonl — so this render is founding evidence and should be logged as such. Marks are flat hard-edged overlays laid ON the render; support is a band beside the bone, never a fill, and no mark touches the cushion.",
            },
            {
                "opt": "B", "varies_on": "execution: transverse cut at the sitting bones instead of the sagittal lumbar cut",
                "type": "03-mechanism-ghostbody", "type_version": "2.2",
                "variant": None,
                "ratio": "4:3", "pipeline": "single-pass",
                "asset_candidate": "05-story3-ghostbody--B.jpg",
                "prompt": P_S3_B, "avoid": AV_GHOST,
                "rationale": "The same claim from underneath: the product's other named job is taking load off the tailbone. A different cut plane answers the buyer who sits, rather than the buyer who drives.",
                "composition_notes": "Same palette lock and the same four marks; only the cut plane and the named structures change. Both options obey the harm-mark rule: stress lives in the left panel only.",
            },
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "The slot exists to show an alignment that holds, not a sequence. Its argument is a shape existing for a reason, and animating a static geometry invents a change the product does not make.",
        },
    },
    {
        "slot_id": "story.4.image",
        "section_role": "outcome",
        "asset": "06-story4-relief-scene.jpg",
        "placement": "beside story block 4, 'Sitting Pain, Gone In Days' (600x450)",
        "options": [
            {
                "opt": "A", "varies_on": "baseline",
                "type": "06-relief-scene", "type_version": "1.0",
                "variant": None,
                "ratio": "4:3", "pipeline": "single-pass",
                "asset_candidate": "06-story4-relief-scene--A.jpg",
                "prompt": P_S4_A, "avoid": AV_SCENE,
                "rationale": "The copy closes on a state of living, not a feature — 'I finally joined Sarah for our evening walks'. That is this type's use_when, and its requires_pair is satisfied by the pain scene at story.0.",
                "composition_notes": "REQUIRES_PAIR: only legal because 01-pain-scene is on the page at story.0 — same man, same muted blue-grey palette, same lens character. The reflection IS the evidence mechanism; without the glass this is a stock photo of a man on a street. No product in frame, by the type's own law.",
            },
            {
                "opt": "B", "varies_on": "type: 06-relief-hero",
                "type": "06-relief-hero", "type_version": "1.12",
                "variant": "--ugc, inset --none",
                "axes": {"register": "ugc", "inset_mode": "none"},
                "ratio": "4:3", "pipeline": "single-pass",
                "asset_candidate": "06-story4-relief-scene--B.jpg",
                "prompt": P_S4_B, "avoid": AV_HERO,
                "rationale": "Closes the section with the product in frame instead of a productless scene. Choose it if the page needs the cushion visible at the moment relief is claimed.",
                "composition_notes": "COLLIDES WITH hero.image OPTION A: both are 06-relief-hero, and one type appears at most once per page outside a repeating section. Pick this only alongside hero option B.",
            },
        ],
        "gif": {
            "eligible": True, "form": "whole-frame",
            "reason": "The slot's reason to exist is a stride that no longer stalls — walking is a sequence, so it is temporal, and the reflection moves with him.",
            "asset": "06-story4-relief-scene.mp4",
            "duration_s": 3, "loop": "seamless",
            "shot": "Locked frame, medium wide, no camera move",
            "action": "He walks through, pauses, glances at the glass",
            "result": "An even stride, nothing guarded",
            "match": "Muted blue-grey grade of the paired pain still",
            "delivery": "mp4/webm, under 2 MB",
        },
    },
    {
        "slot_id": "story.5.image",
        "section_role": "cta",
        "asset": "(supplied)",
        "placement": "beside story block 5, 'A Fractional Cost For Freedom' (600x450)",
        "out_of_scope_reason": "A cta cell: the section's whole argument is price against premium chairs and recurring physiotherapy, closing on the guarantee. That is a standard product shot, which is out of library scope (mapping/slot-rules.md, cta row).",
        "options": [],
        "gif": {"eligible": False, "form": "none", "reason": "Out of library scope — a standard product shot carries no temporal claim."},
    },
]

GALLERY = [
    ("reviews.gallery.0.image", "07-review-grid-kitchen-chair.jpg", "review grid cell 1 (160x160)",
     P_G0, "execution: at-rest, kitchen dining chair, cool morning window light, standing-height overhead frame",
     "Newly unpacked and already in the room where it lives — the cheapest thing to prove and the first thing a sceptic checks."),
    ("reviews.gallery.1.image", "08-review-grid-car-seat.jpg", "review grid cell 2 (160x160)",
     P_G1, "execution: in-use, car driver seat, warm mixed street and dome light, too-close tilted frame",
     "The driver in the reviews is the loudest voice in this page's copy; a forearm pressing it into the seat corner is the gesture that voice describes."),
    ("reviews.gallery.2.image", "09-review-grid-gaming-chair.jpg", "review grid cell 3 (160x160)",
     P_G2, "execution: at-rest, bedroom gaming chair, warm lamp against cold monitor glow, wide doorway frame",
     "One of the five named reviewers is a gamer. A wide dim room is the furthest this set gets from the others in light and distance."),
    ("reviews.gallery.3.image", "10-review-grid-hallway-unbox.jpg", "review grid cell 4 (160x160)",
     P_G3, "execution: kit-flatlay, hallway floor, single warm bulb, straight-down close frame",
     "The only flatlay in the set: it answers what actually arrives in the box, which is a different scepticism from does-it-work."),
    ("reviews.gallery.4.image", "11-review-grid-wheelchair.jpg", "review grid cell 5 (160x160)",
     P_G4, "execution: in-use, wheelchair seat by a window, flat overcast daylight, seated medium frame",
     "Wheelchair users are named in the product's own fit list and nowhere in the page's copy; this is the only place the page can show it."),
    ("reviews.gallery.5.image", "12-review-grid-lorry-cab.jpg", "review grid cell 6 (160x160)",
     P_G5, "execution: at-rest, lorry cab at dawn, cold blue low light, close low-angle frame",
     "The truck driver's review is the most specific one on the page. Dawn in a cab is a light temperature nothing else in the set has."),
]

for slot_id, asset, placement, prompt, varies, why in GALLERY:
    SLOTS.append({
        "slot_id": slot_id,
        "section_role": "social-proof",
        "asset": asset,
        "placement": placement,
        "options": [{
            "opt": "A", "varies_on": varies,
            "type": "05-social-snapshot", "type_version": "1.0",
            "variant": None,
            "ratio": "1:1", "pipeline": "single-pass",
            "asset_candidate": asset.replace(".jpg", "--A.jpg"),
            "prompt": prompt, "avoid": AV_SNAP,
            "rationale": why,
            "composition_notes": "One of six instances of one type inside a repeating section (cross-slot rule 2). SET DIVERSITY LAW: room class, surface, light temperature, camera distance and content mode all differ from every other cell — generate as independent prompts, never as a batch with a shared seed. Exactly one incidental owner object. No faces.",
        }],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "The cell exists to prove the thing exists in a normal room — a place, not a change. Motion in a 160px thumbnail also breaks the register it depends on: real people's photos do not move.",
        },
    })

SLOTS.append({
    "slot_id": "offer.image",
    "section_role": "cta",
    "asset": "(supplied)",
    "placement": "offer card product image (360x360)",
    "out_of_scope_reason": "The cta cell's standard product shot — out of library scope (mapping/slot-rules.md, cta row).",
    "options": [],
    "gif": {"eligible": False, "form": "none", "reason": "Out of library scope."},
})
SLOTS.append({
    "slot_id": "hero.sidebar.image",
    "section_role": "cta",
    "asset": "(supplied)",
    "placement": "Editor's Pick sidebar product image, top of page (300x300)",
    "out_of_scope_reason": "A standard product shot inside a rating sidebar — out of library scope, and the same shot as offer.image.",
    "options": [],
    "gif": {"eligible": False, "form": "none", "reason": "Out of library scope."},
})

# ---------------------------------------------------------------- coverage ---

COVERAGE = {
    "covered": [
        "1 pain — 01-pain-scene at story.0",
        "2 cause — 02-cause-anatomy at story.2",
        "3 mechanism — 03-mechanism-ghostbody at story.3",
        "4 proof — 04-proof-lockedframe --rivals at story.1",
        "5 social — 05-social-snapshot across the six review-grid cells",
        "6 relief — 06-relief-hero at the header, 06-relief-scene at story.4",
    ],
    "absent": ["3 mechanism, second answer — the spec/build rung: what is actually inside the thing"],
    "absent_but_correct": [
        "how-to-use — multi_step_usage is false. Placing a cushion on a chair is one obvious action, and 03-use-sequence's own avoid_when rules it out.",
        "personas — 05-persona-grid is not legal on advertorial, and the six review-grid cells already carry the breadth of audience across six separate rooms.",
    ],
    "gaps": [
        "None that this channel can fill. The spec rung is genuinely absent and a solution-aware reader comparing constructions would use it — but both types that answer it, 03-spec-explode and 03-spec-split, exclude advertorial in their own channels list, and 03-mechanism-xray's use_when covers products that do NOT act on a body structure. Refusing a wrong type is correct; there is nothing to propose here, so recommended[] is empty.",
    ],
}

NOTES = [
    "AWARENESS STAGE — solution-aware, read from the copy rather than declared. The hero assumes the reader already believes sitting hurts and goes straight to 'without expensive chairs'; story.1 spends a whole block comparing solution CLASSES the reader has already bought (flat pads, lumbar pillows, chiropractor); the comparison table is class-versus-class, not problem-versus-nothing. The brief's own awarenessStage field agrees ('solution'), but the routing did not read it. At this stage mechanism and physical proof decide, and re-amplifying the problem insults the reader — which is why the header closes rather than opens the wound, and why pain gets exactly one section.",
    "INPUT DID NOT VALIDATE. The pasted export is a Shopify page export, not a content.json: it has no top-level product, and its page is content plus htmlCompiled rather than channel plus sections. content.json in this directory is the contract reassembled from it by hand, and it is STILL not valid against mapping/content.schema.json for one reason — see the next note.",
    "GAP 1, reference_photos is empty. imageBriefs is null and shopifyProductGid is null, so there is no product photo to hash. The schema requires at least one sha256. Eleven of the thirteen types on this page declare requires_product_photo: true, and every prompt below that needs one says 'the attached photo'. Nothing was fabricated: attachments is omitted from every option rather than filled with an invented hash. Supply the photo, hash it (SPEC 6.4), and content.json validates.",
    "GAP 2 was not a gap. The image slots ARE declared, in htmlCompiled as data-field-type=\"image\", not in page.content — 21 of them, of which 15 are library-routable and 6 are reviewer avatars. The avatars are portrait headshots attached to named reviews and are not library slots; they are also the sharpest FTC surface on the page and should be real or absent.",
    "PLACEHOLDER ALT TEXT IS TEMPLATE RESIDUE. Every placehold.co caption in the export describes a furniture-lifter product — 'man rolling cabinet on lifter set', 'sofa gliding on hardwood', 'lever under cabinet'. None of it is a brief for this product and none of it was used. If those captions were meant as image direction, say so and this routing changes.",
    "CHANNEL is advertorial, taken from lpTypeId. That is a hard gate, not a preference: it removes 01-pain-split, 02-symptom-rail, 03-spec-explode, 03-spec-split and 05-persona-grid from every slot on this page, because their own channels lists exclude it.",
    "CROSS-SLOT RULES APPLIED. One-type-once holds across the seven argument slots; the six review-grid cells are one type six times under the repeating-section exception, each differing on a named dimension. 01-pain-scene x 01-pain-split never share a page — moot here, pain-split is off-channel. 06-relief-scene's requires_pair is satisfied by 01-pain-scene at story.0, same person and same palette. Page arc holds: pain and cause precede relief, and pain never reappears after story.4. Step-3 budget holds at one.",
    "OPTION B COLLISIONS, stated rather than hidden. Options are legal individually; two of them are not legal together. hero.image B (01-pain-scene) would spend the type story.0 needs, and story.4 B (06-relief-hero) would spend the type hero.image A uses. The A-set across all slots is internally legal as it stands.",
    "REVIEW GRID, THE ONE DECISION THAT IS NOT MINE. 05-social-snapshot carries a hard authenticity fence: never a reviewer name, avatar, star row or verified label near the image, and never presented as a customer upload. In the markup the six-up grid is uncaptioned, which satisfies the fence — but it sits directly under a carousel of five named reviews with avatars and Verified Purchase badges. Ship these as page imagery with no caption tying them to a person and the fence holds. Caption them as customer photos and it is a fabricated endorsement. If real customer photos exist, they win outright.",
    "NO PRODUCT IN FRAME AT story.1 OPTION A. That is what --rivals is, and it is legal on advertorial. Option B puts the product in the last panel if the page needs it visible there.",
    "04-proof-lockedframe RUNS HANDHELD. Its strict camera needs compositing, which is not available in this pipeline, so both options generate three frames separately and the slight framing drift between them is honest. The panel-1 prompt deliberately carries no multi-panel language; the panel list lives in the edit steps.",
    "PICKS PRIOR NEVER FIRED. feedback/picks.jsonl has no records, so the 20-pick tie-breaker in runbook Step 3.5 did not run. Everything here is argued from the type files and the ledger, not from conversion evidence — this page is argument-complete, not conversion-optimised.",
    "EVERY MARK IN 03-mechanism-ghostbody IS UNPROVEN — zero records in eval/render-tests.jsonl. Whichever option ships at story.3, log the render: it is that type's founding evidence.",
]

OUT = {
    "page_id": "37",
    "registry_version": "2.0.0",
    "channel": "advertorial",
    "awareness_stage": "solution-aware",
    "slots": SLOTS,
    "coverage": COVERAGE,
    "recommended": [],
    "page_composition_notes": NOTES,
}

# ------------------------------------------------------------------ emit ----

with open(os.path.join(HERE, "prompts.json"), "w", encoding="utf-8") as f:
    json.dump(OUT, f, indent=2, ensure_ascii=False)
    f.write("\n")


def md(d):
    L = []
    L.append("# Image prompts — page 37, L-shaped ergonomic seat cushion")
    L.append("")
    L.append("GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — "
             "edit the JSON (or the script) and re-run.")
    L.append("")
    L.append(f"- page_id `{d['page_id']}` · channel `{d['channel']}` · "
             f"awareness `{d['awareness_stage']}` · registry `{d['registry_version']}`")
    routable = [s for s in d["slots"] if s["options"]]
    oos = [s for s in d["slots"] if not s["options"]]
    n_opts = sum(len(s["options"]) for s in d["slots"])
    L.append(f"- {len(d['slots'])} image slots: {len(routable)} routed, {len(oos)} out of library scope")
    L.append(f"- {n_opts} prompts below")
    L.append("")
    L.append("Ratio goes in the generation tool's own aspect-ratio parameter, never in the "
             "prompt text (adapters/nano-banana.md Rule 4). The `Strictly avoid:` line is not "
             "rendered into any prompt (ADR-014); the exclusion list is kept in the JSON's "
             "`avoid` field for a model with a real negative channel.")
    L.append("")

    L.append("## Read this first")
    L.append("")
    for n in d["page_composition_notes"]:
        head, _, rest = n.partition(". ")
        L.append(f"- **{head}.** {rest}")
    L.append("")

    L.append("## Slot map")
    L.append("")
    L.append("| slot | role | asset | type(s) | ratio | gif |")
    L.append("|---|---|---|---|---|---|")
    for s in d["slots"]:
        if s["options"]:
            types = " / ".join(f"{o['type']} {o['type_version']}" for o in s["options"])
            ratio = s["options"][0]["ratio"]
        else:
            types = "— out of scope"
            ratio = "—"
        g = s.get("gif", {})
        L.append(f"| `{s['slot_id']}` | {s['section_role']} | `{s['asset']}` | {types} | "
                 f"{ratio} | {g.get('form', '—')} |")
    L.append("")

    L.append("## Coverage")
    L.append("")
    for k, label in (("covered", "Covered"), ("absent", "Absent"),
                     ("absent_but_correct", "Absent on purpose"), ("gaps", "Gaps")):
        vals = d["coverage"].get(k) or []
        if not vals:
            continue
        L.append(f"**{label}**")
        L.append("")
        for v in vals:
            L.append(f"- {v}")
        L.append("")

    L.append("---")
    L.append("")
    L.append("## Prompts")
    L.append("")
    for s in d["slots"]:
        L.append(f"### `{s['slot_id']}` — {s['section_role']}")
        L.append("")
        L.append(f"*{s['placement']}* · asset `{s['asset']}`")
        L.append("")
        if not s["options"]:
            L.append(f"**Out of library scope.** {s['out_of_scope_reason']}")
            L.append("")
            continue
        g = s.get("gif", {})
        if g:
            if g.get("eligible"):
                L.append(f"**GIF · {g.get('duration_s')}s · {g.get('loop')} · {g.get('form')}** — {g['reason']}")
                L.append("")
                L.append("```")
                L.append(f"SHOT     {g.get('shot','')}")
                L.append(f"ACTION   {g.get('action','')}")
                L.append(f"RESULT   {g.get('result','')}")
                L.append(f"MATCH    {g.get('match','')}")
                L.append("```")
            else:
                L.append(f"**No GIF.** {g['reason']}")
            L.append("")
        for o in s["options"]:
            v = f" `{o['variant']}`" if o.get("variant") else ""
            L.append(f"#### Option {o['opt']} — {o['type']} {o['type_version']}{v}")
            L.append("")
            L.append(f"- varies on: {o['varies_on']}")
            L.append(f"- ratio parameter: **{o['ratio']}** · {o['pipeline']} · "
                     f"{len(o['prompt'])} characters")
            L.append(f"- why: {o['rationale']}")
            if o.get("composition_notes"):
                L.append(f"- note: {o['composition_notes']}")
            L.append("")
            L.append("```prompt")
            L.append(o["prompt"])
            L.append("```")
            L.append("")
            if o.get("steps"):
                L.append("**Pipeline**")
                L.append("")
                for i, st in enumerate(o["steps"], 1):
                    L.append(f"{i}. {st}")
                L.append("")
        L.append("---")
        L.append("")
    return "\n".join(L) + "\n"


with open(os.path.join(HERE, "prompts.md"), "w", encoding="utf-8") as f:
    f.write(md(OUT))

# Per-type prompt ceilings, each taken from that type's own SLOT CONSTRAINTS.
CEIL = {"02-cause-anatomy": 2050, "03-mechanism-ghostbody": 2100,
        "06-relief-hero": 2100}
DEFAULT_CEIL = 1800
over = [(s["slot_id"], o["opt"], o["type"], len(o["prompt"]),
         CEIL.get(o["type"], DEFAULT_CEIL))
        for s in SLOTS for o in s["options"]
        if len(o["prompt"]) > CEIL.get(o["type"], DEFAULT_CEIL)]
print(f"slots={len(SLOTS)} prompts={sum(len(s['options']) for s in SLOTS)}")
print("over ceiling:", over if over else "none")

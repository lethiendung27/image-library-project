#!/usr/bin/env python3
"""Build prompts.json and prompts.md for page 122 — the sixth seat-cushion page.

prompts.json is the source of truth (query/output.schema.json); prompts.md is
generated from it and never hand-edited (query/runbook.md Step 7).

Run from anywhere:  python3 query/sessions/advertorial-seat-cushion-l-shaped-v06/build.py
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SESSION = os.path.basename(HERE)
PAGE = "122"

CONTRACT = json.load(open(os.path.join(HERE, "content.json"), encoding="utf-8"))
ATTRS = CONTRACT["product"]["attributes"]
DECLARED = {sl["slot_id"]: {"ratio": sl["ratio"], "role": sec["role"]}
            for sec in CONTRACT["page"]["sections"]
            for sl in sec["image_slots"]}

# mapping/slot-rules.md attribute gates, as data so the routing can be checked
# against them rather than trusted. Only the ones this page's attributes fire.
GATES = [
    (lambda a: a["symptom_visibility"] == "invisible", "01-pain-split"),
    (lambda a: a["body_contact"] is False, "03-mechanism-ghostbody"),
    (lambda a: a["result_visibility"] == "invisible", "06-relief-scene"),
    (lambda a: a["multi_step_usage"] is False, "03-use-sequence"),
]
KILLED = sorted({t for c, t in GATES if c(ATTRS)})

CEIL = {"01-pain-scene": 2500, "02-cause-anatomy": 2050,
        "03-mechanism-ghostbody": 2300, "04-proof-lockedframe": 1800,
        "05-social-snapshot": 1800, "06-relief-hero": 2300,
        "06-relief-scene": 2100}

# ---------------------------------------------------------------------------
# Prompts — prose throughout. No headings reach the model: the type, the version
# and the axes are metadata in this file, and Rule 1b's only leaking tier is a
# heading that names a region. The newest routed page for this product carries
# seven prose prompts across seven types and none carries a label.
# ---------------------------------------------------------------------------

HERO_A = """A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his late forties in a creased work shirt, still in the driver's seat of his van at the end of a forty-minute run home, mid-way through hauling himself up and out with one hand clamped on the door frame above him and the other pushed flat into the seat. Under that force: that shoulder hitched up hard against his ear, the arm locked straight, both feet planted wide on the tarmac, his hips barely lifted and his back moving as one solid piece with no bend anywhere in it. Face: eyes shut, jaw set, breath held behind his teeth.

His hips are still well below his knees in the backward-sloping seat, his lower back is pressed flat with an open gap behind it, and the whole load has gone onto the base of his spine.

One specific place: the corner of a depot yard at dusk, the van door standing wide, and the lived-in clutter of the working day — a lanyard looped on the indicator stalk, a cold flask in the door bin, a clipboard face down on the passenger seat, a hi-vis crumpled where he dropped it.

He is unaware of the camera. Key light: the last cold daylight coming flat across the yard. Fill: the weak dome light in the cab roof. A rim of light along the arm braced on the frame. Deep shadow across the near third of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

HERO_B = """A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his late forties in a creased work shirt, standing at the open door of his van a moment after getting out, turned square to the camera with one hand still spread flat on the small of his back and the other braced on the top of the door frame beside him. Under that force: his weight dropped onto one hip, that shoulder low, his chest held back from the vertical and his knees soft, unable to bring himself fully upright. Face: mouth pressed flat, brow drawn, eyes level and holding the lens.

His trousers are still creased in a deep band across the back of both thighs from the seat edge, and the spread hand sits low over the base of his spine rather than in the curve of his back.

One specific place: the corner of a depot yard at dusk, the van door standing wide behind him, and the lived-in clutter of the working day — a lanyard on the indicator stalk, a cold flask in the door bin, a clipboard on the passenger seat, a hi-vis crumpled on the step.

He is looking directly into the lens, holding the viewer's eye. Even ambient daylight across the yard, minimal shadow, flat and unflattering.

Desaturated blue-grey, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

HERO_C = """A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his late forties in a creased work shirt, at the wheel in slow traffic two-thirds of the way through the drive home, mid-way through pushing himself up off the seat with one hand on the steering wheel rim and the other on the seat beside his thigh to take the weight off his back for a few seconds. Under that force: both arms locked straight, his shoulders driven up toward his ears, his backside lifted a hand's width clear of the seat and his eyes still on the road ahead. Face: jaw clamped, cheeks drawn, breath held.

The seat beneath him is deeply hollowed where he has sat for years, the base sloping back so his knees ride high above his hips, and the small of his back is nowhere near the seat back.

One specific place: the cab of a working van in a queue of red tail lights on a wet evening road, and the clutter of the day around him — a lanyard on the stalk, a flask wedged in the door bin, a clipboard sliding on the passenger seat, a parking permit curling on the dash.

He is unaware of the camera. Key light: the red wash of brake lights through the windscreen. Fill: the cold blue of the instrument cluster. A rim of light along his locked forearms. Deep shadow through the rest of the cab.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

BREAK_A = """A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his late forties in a work shirt with the sleeves pushed up, at the kitchen table after the drive home, caught mid-way through a failed attempt to stand: both hands driven down flat on the table top, arms shaking straight, one thigh jammed against the table edge and the chair pushed back at an angle behind him. Under that force: his hips have not cleared the seat, his knees are still bent under him, his back is locked in one piece and his weight has gone forward onto his hands. Face: mouth open on a caught breath, eyes screwed shut, chin tucked down.

His whole seat is still on the chair and his heels have come up off the floor. A woman's hands and forearms enter the frame from the side, one under his upper arm and one flat against his back, taking his weight — she is otherwise out of shot.

One specific place: an ordinary family kitchen after a weekday meal, warm overhead light, and the clutter of the evening left where it was — plates pushed to the middle of the table, a serving dish half emptied, a jug, a folded newspaper, a chair pulled out on the far side with a jacket over its back. No child is present or visible.

He is unaware of the camera. Key light: the kitchen pendant directly above the table, hard and close. Fill: cold spill from a window behind him. A rim of light along his straining forearms. Deep shadow across the far side of the room.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

BREAK_B = """A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot on an ordinary hard kitchen chair drawn realistically and unbranded, the chair small within the frame. The pelvis, the sacrum and the lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: after a long drive, the figure sunk back on the flat chair with the pelvis hinged backward and the lumbar curve flattened and reversed, the whole trunk carried on the base of the spine. Right panel: the same figure on the same chair with one continuous unyielding contour filling the crevice behind and beneath the pelvis, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the chair nor the contour covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

BREAK_C = """A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. A hard wooden kitchen chair pushed back at an angle from the table and left there, its seat still dented in a wide shallow hollow where a body sat, one leg of the chair skewed off the floor tile line where it was shoved.

The evidence is on the table above it: both palm prints still fogged on the polished wood where two hands drove down to push, set wide apart and level with where the chair sits, one of them smeared sideways where the hand slid. A napkin has been dragged half off the edge in the same movement and hangs there.

One specific place: an ordinary family kitchen after a weekday meal, the plates pushed to the middle and not cleared, a serving dish half emptied, a jug, a folded newspaper, a jacket over the chair on the far side. Nothing arranged, nothing removed to tidy the frame.

No subject, so no gaze. The frame looks down the length of the table from standing height, from where the person who could not get up would now be.

Key light: the kitchen pendant directly above, hard and close, raking across the polished table so the palm prints read. Fill: cold spill from the window. Deep shadow under the table and across the far side of the room.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

TRIED_A = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different evenings. One framing for every panel: the same van driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same van, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt curled in the door bin, real scuffing on the sill.

The only thing that changes is which of the three ordinary fixes is on the seat, and each is the plain unbranded version people already own — the three the section names and no others. Panel one: a flat foam doughnut ring, slid forward off the back of the base with its cover rucked into a ridge at the front lip. Panel two: a standalone strap-on lumbar pillow, sagged down the seat back with its strap gone slack and a gap open above it. Panel three: a moulded high-end office chair pad lifted out of an expensive chair and dropped onto the van seat, sitting proud and unstable because it was never shaped for this seat. All three photographed at the same point in the routine, at the end of a nine-hour day, with the driver out of the van and nothing touched or straightened first.

Light differs only in exposure between panels, never in warmth. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours none of them.

No product, no badges, no arrows and no text of any kind."""

TRIED_B = """A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. Three ordinary fixes that failed, dumped together in the footwell behind the driver's seat of a working van where they were thrown one after another: a flat foam doughnut ring with its cover rucked and a permanent crease across it, a strap-on lumbar pillow with the strap tangled and the buckle broken open, and a moulded chair pad cracked along one edge.

The evidence is the wear on each: the doughnut compressed flat on one side and never recovered, the lumbar pillow's foam gone hard and shiny where a back pressed it, the pad's non-slip backing peeled and curled. Dust has settled on the top one and not on the others.

One specific place: the rear footwell of a working van at the end of the day, the sliding door open onto a depot yard, and the clutter that lives there — a coil of bungee cord, a folded blanket, a plastic crate of straps, a coffee cup gone cold in the door bin.

No subject, so no gaze. The frame looks down into the footwell from standing height at the open door.

Key light: flat cold daylight coming in through the open door. Fill: the dim of the load space. A rim of light along the curled edge of the peeled backing. Deep shadow at the back of the well.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

TRIED_C = """Honest documentary product test photography, unstyled, natural and sharp.

Two equal vertical panels, a thin white gutter, no outer border.

Shot by one person on a phone on two different evenings. One framing for both panels: the same van driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken twice, never as two different shots.

The same van, the same seat and the same door frame in both panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt curled in the door bin, real scuffing on the sill.

The only thing that changes is what is on the seat, and both are the plain unbranded versions people already own. Panel one: a flat foam doughnut ring and a separate strap-on lumbar pillow used together, the ring slid forward off the back of the base and the pillow sagged down the backrest, with an open wedge of bare seat left between them at the corner where the base meets the back. Panel two: the same two pieces after nine hours of driving, the ring pushed further forward and folded against the front lip and the pillow dropped into the crevice, the gap now wider than it started. Both photographed with the driver out of the van and nothing touched or straightened first.

Light differs only in exposure between panels, never in warmth. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours neither.

No product, no badges, no arrows and no text of any kind."""

DROP_A = """A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, the sacrum and the lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary van seat whose base slopes backward, drawn realistically and unbranded, with a visible open crevice where the seat base meets the upright backrest. The hips have dropped below the knees, the pelvis has hinged backward into that crevice and the lumbar curve has flattened and reversed. Right panel: the same figure on the same seat with one continuous unyielding contour filling that crevice, the hips level with the knees, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the contour covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

DROP_B = """A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated side-on in an ordinary matte grey van seat whose base slopes backward: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical seat in both. The body is cross-sectioned along the midline so the pelvis, the sacrum and the lumbar spine are visible inside the silhouette.

The pelvis, the sacrum and the lumbar vertebrae are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: the bare seat, with an open crevice where the base meets the backrest. The mannequin's pelvis has hinged backward into that crevice and the hips have dropped below the knees.

Right panel is the correct state: the reference product is in place on the same seat at the same angle as one single object, its contour running unbroken from the seat section up into the lumbar section with no join anywhere along it, the hips lifted level with the knees and the lumbar curve restored. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product."""

DROP_C = """A 2D flat-vector illustration with flat fills and hard edges, no gradients. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, the sacrum and the lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary van seat whose base slopes backward, drawn realistically and unbranded, the hips dropped below the knees and the pelvis hinged backward into the crevice at the seat corner. Right panel: the same figure on the same seat with one continuous unyielding contour filling that crevice, the hips level with the knees and the pelvis upright. Neither the seat nor the contour covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each running along the front of the trunk from the breastbone to the front of the hip bone and stopping at both, both starting from the same point in their panel — the closing of the angle between trunk and thigh is what they measure. Red on the left where that angle is shut tight, blue on the right where it has opened. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

PIECE_A = """A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated side-on in an ordinary matte grey van seat: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical seat in both. The body is cross-sectioned along the midline so the pelvis, the sacrum and the lumbar spine are visible inside the silhouette.

The pelvis, the sacrum and the lumbar vertebrae are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: two separate matte grey pieces sit on the seat, a pad on the base and a roll against the backrest, with a visible gap between them at the seat corner. The mannequin's pelvis has hinged backward into that gap.

Right panel is the correct state: the reference product is in place on the same seat at the same angle as one single object, its contour running unbroken from the seat section up into the lumbar section with no join anywhere along it. A flat hard-edged blue band, unshaded, is drawn beside that contour along its own length on the side away from the product, running only the length the product reaches — never a fill of the product, never a tint of the anatomy.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product."""

PIECE_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his late forties in an open-collar work shirt, seated in the driver's seat of his parked van with the door open, his weight settled evenly and his gaze out through the windscreen rather than on the product, sitting well back so the whole seat back and the product against it are clear to the camera. He sits to the right of the frame.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real van cab filled to the edges with objects that genuinely belong there: a lanyard on the indicator stalk, a flask in the door bin, a phone cable coiled at the dash, a clipboard on the passenger seat, a parking permit on the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, occupying the space he is offset from, sits a small rectangular panel with a thin white border, split into two equal halves that share one photographic register. The left half shows the same seat with a flat foam pad on the base and a separate strap-on roll against the backrest, the pad slid forward and the roll dropped into the crevice between them, with glowing red points on the exposed seat corner and on the fallen roll. The right half shows the same seat with the reference product in place, brighter and cleaner, with a translucent blue overlay following the single continuous seam that runs from the seat section up into the lumbar section. A circular red badge carrying the white letters VS sits at the seam between the two halves.

No mark of any kind appears anywhere outside that panel."""

PIECE_C = """A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated side-on in an ordinary matte grey van seat: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical seat in both. The body is cross-sectioned along the midline so the pelvis, the sacrum and the lumbar spine are visible inside the silhouette.

The pelvis, the sacrum and the lumbar vertebrae are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: the reference product's own shape is present but broken into two separate pieces at the corner, a base section and a back section with a finger-wide gap between them, and the mannequin's pelvis has hinged backward into that gap.

Right panel is the correct state: the same reference product whole and continuous, one single object with no join anywhere along its contour, on the same seat at the same angle, the pelvis upright and carried. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product."""

CARRY_A = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his late forties in an open-collar work shirt, standing at the open door of his van in a car park at the start of the working day, the reference product carried easily under one arm against his side, his other hand loose at his side and his gaze ahead toward the building he is walking to rather than at the product. He stands to the right of the frame.

The reference product is identical to the attached photo in shape, colour and proportion, its continuous L shape clear against his side.

One real place filled to the edges with objects that genuinely belong there: the open van door beside him, a kerb, a painted bay line worn thin, a wheeled bin against a wall, a second car, a low railing. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight, high-key neutral grade.

In the upper left of the frame, occupying the space he is offset from, sits a small rectangular panel with a thin white border. It is a plain closer shot of the same product from a step back, seated in place on an ordinary office chair with its seat section on the base and its lumbar section standing against the backrest, the whole fitting clear — the same product in the second place it lives, at the same freestanding sit-on-top placement as in the main frame.

No mark of any kind appears anywhere in the image, and no text."""

CARRY_B = """A candid documentary photograph, natural, unposed and sharp.

The attached photo is the exact reference for the product.

Two people at the end of a shift in a depot yard. One of them has just lifted the reference product off his van seat and is holding it out to the other, turned so its continuous L shape reads clearly from the side, his eyes on the other person's face rather than on the product. The other stands half-turned away from the camera with his face not visible, one hand already reaching for it, his attention on the shape of the thing.

The reference product is identical to the attached photo in shape, colour and proportion. It is the largest and clearest object in the frame and nothing beside it competes for the first glance.

One real place with a genuine reason both are there: the corner of a depot yard at the end of the day, both van doors standing open, a stack of pallets against the fence, a wheeled bin, painted bay lines worn thin. Ambient daylight only, flat and cool, no styling of any kind.

The moment the product just did is in the frame behind them: the driver's seat of the open van, its base deeply hollowed from years of use, still bare where the product was lifted out of it.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text."""

CARRY_C = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

Present only as two forearms and hands, no face and no shoulders in the frame: the reference product held in both hands and being lowered onto a hard wooden dining chair at home, its seat section already meeting the chair seat and its lumbar section swinging in toward the chair back. The hands are relaxed and the wrists straight, nothing braced and nothing strained.

The reference product is identical to the attached photo in shape, colour and proportion, its continuous L shape clear against the plain chair.

One real room filled to the edges with objects that genuinely belong there: a dining table with a mug and a folded newspaper on it, a second chair pushed in, a radiator under a window, a bag hooked over a chair back, a rug with real wear on it. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight from the window, high-key neutral grade.

In the upper left of the frame, occupying the space the hands are offset from, sits a small rectangular panel with a thin white border. It is a plain closer shot of the same product from a step back, seated in place on a van driver's seat with its seat section on the base and its lumbar section against the backrest, the whole fitting clear — the same product in the first place it lives, at the same freestanding sit-on-top placement as in the main frame.

No mark of any kind appears anywhere in the image, and no text."""

ROAD_A = """A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his late forties in put-together but ordinary clothes, just out of the driver's seat of his car at a coastal hotel car park at the end of a three-hour drive, straightening up to his full height with his weight even through both feet and both hands empty and open at his sides. Nothing is held, nothing is braced, nothing is covered. His chest is opening, his shoulders roll back and down, his eyes are coming open against the light and his brow has let go, and a small involuntary smile has arrived on its own while he looks off past the car toward the sea rather than at the camera.

The driver's door stands open beside him, and the reference product sits on the seat inside it as its own object near the camera, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary hotel car park on an unremarkable afternoon, a second car and a blurred couple unloading further along, a wheeled suitcase upright on the tarmac, a wire bin, painted bay lines worn thin, a low wall with the sea behind it. Nothing aspirational and nothing tidied.

Even natural daylight, bright, soft shadows, plain and unglamorous. A natural palette, light film grain, shallow depth of field, honest rather than drained and never warm-boosted.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text."""

ROAD_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his late forties in an open-collar shirt, standing at the open boot of his car in a coastal hotel car park, mid-way through lifting a heavy duffel bag out of it with both hands, his back straight and the weight taken through his legs, his gaze on the bag rather than on the product. He stands to the right of the frame.

The reference product is visible on the driver's seat through the open rear door beside him, its seat section on the base and its lumbar section against the backrest, identical to the attached photo in shape, colour and proportion.

One real place filled to the edges with objects that genuinely belong there: a second car, a wheeled suitcase upright on the tarmac, a wire bin, painted bay lines worn thin, a low wall, a hotel entrance blurred behind. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight, high-key neutral grade.

In the upper left of the frame, occupying the space he is offset from, sits a small rectangular panel with a thin white border showing the same man at the same car on an earlier day: the boot open in front of him, both his hands flat on the rim of it and his weight leaning there, not lifting anything, his back rounded. The panel matches the main photograph in resolution, grade and light quality. A single arrow runs from that panel toward the main frame and there is no other marking.

No mark of any kind appears anywhere outside that panel."""

ROAD_C = """A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his late forties in ordinary clothes, on the grass beside a car park at the end of a long drive, mid-stride through kicking a football back to someone off frame, his planted foot square and his kicking leg swung through, both arms out for balance and his weight carried easily. His face is turned to follow the ball rather than toward the camera, and his mouth is open on a shout after it. Nobody else is in the frame.

His car stands a few steps behind him with the driver's door open, and the reference product sits on the seat inside it as its own object, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary strip of grass at the edge of a car park on an unremarkable afternoon, a low fence, a bin, a second car, painted bay lines worn thin, a wheeled suitcase left standing by the open door. Nothing aspirational and nothing tidied.

Even natural daylight, bright, soft shadows, plain and unglamorous. A natural palette, light film grain, shallow depth of field, honest rather than drained and never warm-boosted.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text."""

COST_A = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different days. One framing for every panel: the same van driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same van, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt curled in the door bin, real scuffing on the sill.

The only thing that changes is what has been put in the seat to fix it, and the first two are the plain unbranded versions people already own. Panel one: the seat re-upholstered, a new foam base and cover fitted into the same frame, the stitching fresh and the shape unchanged. Panel two: a premium moulded ergonomic chair pad lifted out of an office chair and set on the seat, sitting proud and unstable because it was never shaped for this seat. Panel three: the reference product in place, its seat section on the base and its lumbar section standing against the backrest as one continuous piece.

The attached photo is the exact reference for the product in the last panel.

Light differs only in exposure between panels, never in warmth. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours none of them.

No badges, no arrows and no text of any kind."""

COST_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his late forties in an open-collar work shirt, seated in the driver's seat of his parked van with the door open, his weight settled evenly and his gaze out through the windscreen rather than on the product, sitting well back so the whole seat back and the product against it are clear to the camera. He sits to the right of the frame.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real van cab filled to the edges with objects that genuinely belong there: a lanyard on the indicator stalk, a flask in the door bin, a phone cable coiled at the dash, a clipboard on the passenger seat, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, occupying the space he is offset from, sits a small rectangular panel with a thin white border, split into two equal halves that share one photographic register. The left half shows a treatment room with a padded couch and a folded towel on it, empty, and beside it a high-backed premium office chair standing alone on a bare floor — the two things the money used to go to, with a glowing red point on each. The right half shows the same van seat with the reference product in place, brighter and cleaner, one continuous piece from base to backrest. A circular red badge carrying the white letters VS sits at the seam between the two halves.

No mark of any kind appears anywhere outside that panel."""

COST_C = """Honest documentary product test photography, unstyled, natural and sharp.

Two equal vertical panels, a thin white gutter, no outer border.

Shot by one person on a phone on two different days. One framing for both panels: the same van driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken twice, never as two different shots.

The same van, the same seat and the same door frame in both panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt curled in the door bin, real scuffing on the sill.

The only thing that changes is what is in the seat. Panel one: the seat stripped back to its frame mid-re-upholstery, the old foam lifted out and set on the sill, the new cover half fitted and the tools left on the floor — the job that has to be paid for and cannot be moved to another vehicle. Panel two: the reference product simply set in place on the finished original seat, its seat section on the base and its lumbar section against the backrest as one continuous piece, nothing fitted and nothing altered.

The attached photo is the exact reference for the product in the second panel.

Light differs only in exposure between panels, never in warmth. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours neither.

No badges, no arrows and no text of any kind."""


def snap(subject, scene, anchor, camera):
    """05-social-snapshot expands the same slots every time, so one wording
    carries across the set and one regex can check them all."""
    return f"""A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

{subject}

{scene}

One incidental owner object and no more: {anchor}

{camera}

No studio light, no styling, no negative space, no borders and no text anywhere in the picture."""


REVIEWS = [
    {
        "quote": "Greg T. — drives a delivery van all day and used to limp to his "
                 "front door every night.",
        "varies": "set position 1 of 4 — a working van cab, the product in use "
                  "under a forearm, cool early daylight, arm's length from the "
                  "open driver's door",
        "subject": "The product mid-use in a van cab, photographed by its owner "
                   "from the open driver's door: the reference cushion in place "
                   "on the driver's seat with the owner's forearm resting across "
                   "the top of the lumbar section, no face in shot.",
        "scene": "An ordinary working delivery van cab photographed exactly as "
                 "found early on a weekday — the mess stays, nothing tidied, "
                 "nothing added for the picture. Cool early daylight through the "
                 "windscreen and the open door, no other light.",
        "anchor": "a bunch of van keys dropped in the door bin.",
        "camera": "Framing slightly tilted and a little too close, taken at "
                  "arm's length from the seat; focus adequate but casual, mild "
                  "noise, exposure honest to the room.",
    },
    {
        "quote": "Elena R. — was extremely sceptical after wasting money on "
                 "separate lumbar rolls that kept falling down.",
        "varies": "set position 2 of 4 — a home office, the product at rest on a "
                  "desk chair beside the rolls it replaced, warm lamplight, "
                  "standing height looking down",
        "subject": "The product simply sitting where it now lives, photographed "
                   "by its owner from standing height: the reference cushion in "
                   "place on an office desk chair, its seat section on the base "
                   "and its lumbar section against the backrest, nobody in shot. "
                   "Two old strap-on lumbar rolls lie discarded on the floor "
                   "beside the chair with their straps tangled.",
        "scene": "An ordinary spare-room home office photographed exactly as "
                 "found on a weekday evening — papers stacked at one end of the "
                 "desk, a cardigan over the chair arm, a printer with its lid up, "
                 "nothing tidied. Warm desk-lamp light and the last grey daylight "
                 "from one window, no other light.",
        "anchor": "a mug with a cold inch of tea left in it on the desk.",
        "camera": "Framing off-centre and slightly tilted, taken from standing "
                  "height looking down at the chair; focus adequate but casual, "
                  "mild noise, exposure honest to the room.",
    },
    {
        "quote": "David K. — a wheelchair user who sits for long hours and needed "
                 "firm support without a hard edge.",
        "varies": "set position 3 of 4 — a living room, the product in use on a "
                  "wheelchair seat, flat overcast daylight, low and close from a "
                  "seated height",
        "subject": "The product mid-use, photographed by its owner from a seated "
                   "height beside it: the reference cushion in place on a "
                   "wheelchair seat, its seat section on the base and its lumbar "
                   "section standing against the backrest, one hand resting on "
                   "the push rim at the edge of the frame and no face in shot.",
        "scene": "An ordinary living room photographed exactly as found in the "
                 "middle of a grey afternoon — a throw pulled half off the sofa, "
                 "a side table with a book face down on it, a rug rucked at one "
                 "corner, nothing tidied. Flat overcast daylight from one window, "
                 "no lamp on.",
        "anchor": "a folded newspaper wedged down the side of the sofa cushion.",
        "camera": "Framing low and a little too close, taken from a seated "
                  "height at arm's length; focus adequate but casual, mild noise, "
                  "exposure honest to the room.",
    },
    {
        "quote": "The fourth tile carries no quote of its own in the export; it "
                 "sits under the same heading as the other three.",
        "varies": "set position 4 of 4 — a kitchen, the product at rest on a hard "
                  "dining chair with its non-slip base turned to camera, kitchen "
                  "overhead light, straight down from standing height",
        "subject": "The product simply sitting where it now lives, photographed "
                   "by its owner from standing height: the reference cushion "
                   "resting on a hard wooden dining chair, tipped forward against "
                   "the chair back so its textured non-slip base faces the camera, "
                   "nobody in shot.",
        "scene": "An ordinary family kitchen photographed exactly as found after "
                 "a weekday meal — plates stacked by the sink, a tea towel over "
                 "the oven rail, post piled at the end of the worktop, nothing "
                 "tidied. Kitchen overhead light only, slightly cold.",
        "anchor": "a set of house keys dropped on the seat beside it.",
        "camera": "Framing tilted a few degrees and taken from standing height "
                  "looking almost straight down; focus adequate but casual, mild "
                  "noise, exposure honest to the room.",
    },
]

# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------


def opt(o, varies, typ, ver, ratio, prompt, rationale, variant=None, axes=None,
        notes=None, asset=None):
    d = {"opt": o, "varies_on": varies, "type": typ, "type_version": ver,
         "variant": variant, "ratio": ratio, "pipeline": "single-pass",
         "prompt": prompt, "rationale": rationale}
    if axes:
        d["axes"] = axes
    if notes:
        d["composition_notes"] = notes
    if asset:
        d["asset_candidate"] = asset
    return d


KNOCK = ("Picking this forces another slot to change: {t} is also the "
         "recommendation at {s}, and one-type-once binds the shipped set. Take "
         "B here and that slot moves to its own option B.")

REVIEW_BLOCK = (
    "BLOCKED AS THE PAGE IS BUILT. 05-social-snapshot's authenticity fence is "
    "hard and non-negotiable: no reviewer name, avatar, star row or verified "
    "label anywhere near the image in the layout. All four reviews.shots slots "
    "sit inside the same section element as reviews.quotes.0-2, which carry "
    "names (Greg T., Elena R., David K.) and a Verified Purchase label each. "
    "Rendering these beside that copy presents generated pictures as customer "
    "uploads, which is a fabricated endorsement. Either move the photo grid out "
    "of the attributed block, or drop the names and verified labels from it, or "
    "use real customer photographs - which always win over generated ones.")

SLOTS = [
    {
        "slot_id": "hero.image", "section_role": "hero",
        "asset": f"{PAGE}-01-hero-pain-scene.png",
        "placement": "Advertorial header, under the title and above the byline.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "The hero exists to make a cold reader recognise themselves "
                    "in a held state. The action is a single effort with no "
                    "before and after inside it - a still carries it whole, and "
                    "a loop of a man half out of a seat adds duration without "
                    "adding argument."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT decides, close to verbatim. 01-pain-scene --candid asks for "
            "physical pain in a moment nobody would choose to be seen in, and "
            "the page's own title is 'behind the wheel'. A plays the exit from "
            "the cab as one action, with the symptom as physical fact rather "
            "than as expression. PAGE LEGALITY: the advertorial hero cell holds "
            "exactly one type and the gates leave no second, so B is the gaze "
            "axis rather than a type borrowed from a role it does not belong to. "
            "A also satisfies 06-relief-scene's requires_pair at "
            "content.items.5. PRODUCT PRESENCE: none, correctly - the type "
            "forbids it and the reader has not met the product yet. PROMPT "
            "RISK: 1500 characters against a 2500 ceiling, and no clause in it "
            "is unrendered.",
        "options": [
            opt("A", "baseline", "01-pain-scene", "1.14", "16:9", HERO_A,
                "The page's own opening as one action: hauling himself out of "
                "the cab on a locked arm at the end of the run. The evidence is "
                "physical fact - hips below knees, the lumbar curve flat, the "
                "load on the base of the spine.",
                variant="candid", axes={"gaze": "candid"},
                notes="Needs no photo - the type is G1-exempt and no product "
                      "appears.",
                asset=f"{PAGE}-01-hero-pain-scene--A.png"),
            opt("B", "axis: gaze=confront. The advertorial hero cell holds one "
                "type and the attribute gates leave no second, so the axis is "
                "the only legal second dimension here",
                "01-pain-scene", "1.14", "16:9", HERO_B,
                "The same argument in the type's other gaze, a moment later at "
                "the open door with a hand spread on the base of his spine. The "
                "creased band across the back of both thighs is the evidence a "
                "confront frame can still carry.",
                variant="confront", axes={"gaze": "confront"},
                notes="Needs no photo. The type reserves --confront for "
                      "appearance and daily frustration rather than physical "
                      "pain, and it also swaps low-key for flat-ambient light by "
                      "law; it is offered because the axis is the only legal "
                      "second dimension at this slot, not because it fits "
                      "better.",
                asset=f"{PAGE}-01-hero-pain-scene--B.png"),
            opt("C", "execution: the moment moves from the end of the drive to "
                "the middle of it", "01-pain-scene", "1.14", "16:9", HERO_C,
                "The relief attempt drivers actually make - pushing up off the "
                "seat on the wheel in slow traffic to unload the spine for a few "
                "seconds. It puts the problem inside the drive rather than after "
                "it, which is where the copy's own 'on the drive home' sits.",
                variant="candid", axes={"gaze": "candid"},
                notes="Needs no photo. A hand off the wheel in moving traffic is "
                      "the risk to read for: the queue is stationary and the "
                      "brake lights say so, but a render that puts the van in "
                      "motion turns a pain cue into an unsafe act.",
                asset=f"{PAGE}-01-hero-pain-scene--C.png"),
        ],
    },
    {
        "slot_id": "content.items.0.image", "section_role": "problem-agitation",
        "asset": f"{PAGE}-02-content0-pain-scene.png",
        "placement": "Beside 'The Humiliating Evening That Finally Broke My "
                     "Resolve'.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "The beat is a single failed effort, not a transition. What "
                    "changes across it is only that someone else takes the "
                    "weight, and a loop of that is a person being helped rather "
                    "than a claim about the product."},
        "recommended_opt": "A",
        "recommendation_basis":
            "PAGE LEGALITY decides it over FIT. This is a second pain beat and "
            "01-pain-scene is already the hero, so this is the runbook's rung 4 "
            "- another execution of a type on the page differing on a named "
            "dimension, here the place and the failed action. FIT is still "
            "strong: the copy's own words are a gasp, a locked pair of hips and "
            "a wife who had to physically help him up. EVIDENCE: the type is at "
            "1.14 with object-only executions recorded twice, which is what C "
            "takes. PRODUCT PRESENCE: none, correctly - the product is three "
            "sections away. PROMPT RISK: the helping hands are the clause to "
            "watch; they are described as forearms entering frame so the image "
            "does not become a two-person portrait, and no child appears, which "
            "G13 requires of a pain scene.",
        "options": [
            opt("A", "baseline", "01-pain-scene", "1.14", "16:9", BREAK_A,
                "The copy's exact moment: hands driven down on the table, hips "
                "still on the chair, and another person's forearms taking the "
                "weight from the side. The humiliation is carried by the help "
                "arriving, not by an expression.",
                variant="candid", axes={"gaze": "candid"},
                notes="Needs no photo. G13: no minor is present or visible, "
                      "which the prompt states positively - the copy's family "
                      "dinner is why that has to be said rather than assumed.",
                asset=f"{PAGE}-02-content0-pain-scene--A.png"),
            opt("B", "type: 02-cause-anatomy rather than 01-pain-scene",
                "02-cause-anatomy", "1.15", "16:9", BREAK_B,
                "Draws why standing failed rather than showing it failing: a "
                "pelvis hinged back on a flat hard chair against the same pelvis "
                "carried upright. It answers the section's question instead of "
                "restating its scene.",
                variant="diagnostic", axes={},
                notes="Needs no photo - --diagnostic drops the product reference "
                      "and reads requires_product_photo false for the variant. "
                      + KNOCK.format(t="02-cause-anatomy", s="content.items.2"),
                asset=f"{PAGE}-02-content0-pain-scene--B.png"),
            opt("C", "execution: object-only, nobody in frame",
                "01-pain-scene", "1.14", "16:9", BREAK_C,
                "The room a minute after: the chair shoved back with the hollow "
                "still in its seat, and two fogged palm prints on the polished "
                "table where the hands drove down. Rank-3 evidence - the failed "
                "attempt in the state that shows it failed.",
                variant="candid", axes={"gaze": "candid"},
                notes="Needs no photo. The palm prints are the whole argument, "
                      "so the raking pendant light that makes them read is not "
                      "decoration and must survive the render.",
                asset=f"{PAGE}-02-content0-pain-scene--C.png"),
        ],
    },
    {
        "slot_id": "content.items.1.image", "section_role": "proof",
        "asset": f"{PAGE}-03-content1-proof-lockedframe.png",
        "placement": "Beside 'Why Every Traditional Fix Failed Miserably'.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "The still earns motion on the argument - a pad creeping "
                    "forward under a body is this library's own example of a "
                    "cause loop - but this slot is refused by the budget, not by "
                    "the temporal test. It sits directly beside content.items.2, "
                    "which carries the section's cause loop, and ADR-032 bars two "
                    "adjacent loops inside one section. It is listed in "
                    "motion.reserves."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT is close to verbatim. 04-proof-lockedframe's use_when names 'the "
            "I tried three things beat of an advertorial' and this section is "
            "that beat in the copy's own words - a doughnut cushion, a strap-on "
            "lumbar pillow, an expensive chair. --rivals is the variant for the "
            "alternatives with no product in frame, which is right this early. "
            "PAGE LEGALITY: this type is also recommended at content.items.6, "
            "which is rung 4 - two executions differing on variant and subject "
            "class, named in both varies_on lines. CAPABILITY: generation_mode "
            "is multi-pass at type level and the capability gate runs it handheld "
            "in one pass where the renderer cannot composite, which ADR-021 "
            "settles for this pipeline. PRODUCT PRESENCE: none, and --rivals is "
            "the named exception to the reference-photo rule. PROMPT RISK: three "
            "unbranded objects must stay recognisable as themselves without "
            "becoming caricatures of failure; the prompt fixes the moment for all "
            "three at the end of the same nine-hour day so none is staged worse "
            "than another.",
        "options": [
            opt("A", "baseline", "04-proof-lockedframe", "1.13", "16:9", TRIED_A,
                "Three panels, one framing, one variable: which ordinary fix is "
                "on the seat. Each is shown in the state that shows it failed - "
                "slid forward, sagged, sitting proud - rather than being "
                "described as bad.",
                variant="rivals", axes={"camera_lock": "handheld"},
                notes="Needs no photo - --rivals is Step 5's named exception and "
                      "the reference product is deliberately absent.",
                asset=f"{PAGE}-03-content1-proof-lockedframe--A.png"),
            opt("B", "type: 01-pain-scene rather than 04-proof-lockedframe",
                "01-pain-scene", "1.14", "16:9", TRIED_B,
                "The same three failures as residue instead of as a test: all "
                "three dumped in the footwell with the wear that finished each "
                "one legible on it. Evidence rank 3, the failed tool in the state "
                "that shows it failed.",
                variant="candid", axes={"gaze": "candid"},
                notes="Needs no photo. "
                      + KNOCK.format(t="01-pain-scene",
                                     s="hero.image and content.items.0"),
                asset=f"{PAGE}-03-content1-proof-lockedframe--B.png"),
            opt("C", "execution: two panels of the same pair over one shift, "
                "rather than three panels of three products",
                "04-proof-lockedframe", "1.13", "16:9", TRIED_C,
                "Argues the gap rather than the products: the pad and the roll "
                "used together at the start of a shift and after nine hours, with "
                "the bare wedge at the seat corner wider in the second panel. It "
                "is the same claim the next section will explain.",
                variant="rivals", axes={"camera_lock": "handheld"},
                notes="Needs no photo. Two panels of the same objects risk "
                      "reading as one photograph duplicated; the widened gap is "
                      "the only thing that separates them and it has to survive "
                      "at panel scale.",
                asset=f"{PAGE}-03-content1-proof-lockedframe--C.png"),
        ],
    },
    {
        "slot_id": "content.items.2.image", "section_role": "cause",
        "asset": f"{PAGE}-04-content2-cause-anatomy.png",
        "placement": "Beside 'The Hidden Pelvic Drop That Wrecks Your Spine'.",
        "gif": {"eligible": True, "form": "whole-frame", "kind": "cause",
                "type_id": "cause", "rung": "natural",
                "reason":
                    "The section's claim is a state changing under load: weight "
                    "settles, the hips slide below the knees, the pelvis rolls "
                    "back into the crevice and the lumbar curve reverses. A still "
                    "can only show the endpoint. The gif library's `cause` type "
                    "names this exactly - the culprit at work right now, a pad "
                    "creeping forward under a body - and the type legislates no "
                    "motion layer of its own, so the form is whole-frame and the "
                    "kind is the type's own job.",
                "asset": f"{PAGE}-04-content2-cause-anatomy--brief.svg",
                "refs": "gifs-library/cause/ — the folder card carries the law",
                "output": f"advertorial-cause-seat-cushion-l-shaped-v06.mp4",
                "ratio": "16:9", "duration_s": 3, "loop": "seamless loop",
                "brief":
                    "A side-on view of a man lowering himself into a van seat "
                    "that slopes backwards. As his weight settles his hips slide "
                    "down below his knees, his pelvis rolls backwards into the "
                    "gap where the seat base meets the backrest, and his lower "
                    "back peels away from the seat leaving an open space behind "
                    "it.",
                "alt":
                    "The same movement with no person: a hand presses down on the "
                    "seat base where a body would sit, and the foam compresses "
                    "backwards into the gap at the seat corner while a flat pad "
                    "laid on it creeps forward off the back of the base."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT is decisive and the copy hands the type its own device. "
            "02-cause-anatomy exists to blame one object and show its measurable "
            "harm, and this section names the object - a seat that angles "
            "backward - and the measurement, hips below knees. The paired dashed "
            "lines against the thigh ARE the argument here rather than "
            "decoration. PAGE LEGALITY: cause sits fourth on the page, after the "
            "pain and the failed fixes, which is where the type belongs. "
            "EVIDENCE: airbrushed carries modelled volume, which suits a pelvis "
            "better than flat fills; the type's strongest renders are the ones "
            "that left the full skeleton behind, which naming the pelvis and "
            "lumbar spine does. PRODUCT PRESENCE: none - --diagnostic drops the "
            "product for the advertorial middle, and the right panel argues with "
            "a contour rather than a branded object. PROMPT RISK: the model "
            "substitutes a full skeleton unasked, which is why the prompt names "
            "what it is not.",
        "options": [
            opt("A", "baseline", "02-cause-anatomy", "1.15", "16:9", DROP_A,
                "Two panels, one figure, one property changed: the hip-to-knee "
                "line, long and red on the left where the pelvis has hinged into "
                "the seat crevice, closed and blue on the right where one "
                "continuous contour fills it.",
                variant="diagnostic", axes={},
                notes="Needs no photo - --diagnostic drops the product reference "
                      "and reads requires_product_photo false for the variant.",
                asset=f"{PAGE}-04-content2-cause-anatomy--A.png"),
            opt("B", "type: 03-mechanism-ghostbody rather than 02-cause-anatomy",
                "03-mechanism-ghostbody", "2.2", "16:9", DROP_B,
                "Answers the same question in the register that shows the "
                "product doing it: a cross-sectioned mannequin on the bare seat "
                "against the same mannequin with the reference product in place. "
                "It buys the product's real shape and gives up the measure mark.",
                axes={},
                notes="Needs the product photo. "
                      + KNOCK.format(t="03-mechanism-ghostbody",
                                     s="content.items.3"),
                asset=f"{PAGE}-04-content2-cause-anatomy--B.png"),
            opt("C", "execution: flat-vector, and the measure moves from the "
                "hip-knee line to the trunk-thigh angle",
                "02-cause-anatomy", "1.15", "16:9", DROP_C,
                "The same two panels drawn in flat fills, measuring the closing "
                "angle between trunk and thigh instead of the drop from hip to "
                "knee. Flat-vector is the style recorded as holding the dash "
                "pattern cleanly.",
                variant="diagnostic", axes={},
                notes="Needs no photo. The trunk-thigh angle is a harder read at "
                      "a glance than the hip-knee drop, which is the trade for a "
                      "cleaner dash.",
                asset=f"{PAGE}-04-content2-cause-anatomy--C.png"),
        ],
    },
    {
        "slot_id": "content.items.3.image", "section_role": "mechanism",
        "asset": f"{PAGE}-05-content3-mechanism-ghostbody.png",
        "placement": "Beside 'How a Single Continuous Piece Changes Everything'.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "A two-panel wrong-and-right render is inspected rather than "
                    "watched - the reader's eye does the travelling between the "
                    "panels, and animating one of them would make the pair argue "
                    "at two speeds. The section's own claim is a structural fact, "
                    "not an event: the piece is continuous whether or not "
                    "anything moves."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT, and the attribute gate is what makes it available. "
            "body_contact is true for a cushion sat on, so "
            "03-mechanism-ghostbody survives where page 65's false dropped it, "
            "and this is the type for explaining WHY a shape works through a "
            "structure inside the body that cannot be filmed. The section's "
            "claim is exactly that: one continuous piece bridges the gap the "
            "pelvis was falling into. PAGE LEGALITY: mechanism sits fifth, after "
            "the cause, which is the type's own placement. EVIDENCE: the type is "
            "at 2.2 and its cutaway rules were tightened again at ADR-038, which "
            "this prompt follows - the cut is along the midline and the structure "
            "named. PRODUCT PRESENCE: the product is the right panel and the only "
            "object with a real material finish. PROMPT RISK: the blue band must "
            "sit BESIDE the lumbar spine rather than tint it, which is the "
            "recorded failure for this mark.",
        "options": [
            opt("A", "baseline", "03-mechanism-ghostbody", "2.2", "16:9", PIECE_A,
                "Two panels: two separate grey pieces with a gap at the seat "
                "corner, against the reference product as one unbroken contour "
                "from base to lumbar. The blue band runs beside the spine only as "
                "far as the product reaches.",
                axes={},
                notes="Needs the product photo.",
                asset=f"{PAGE}-05-content3-mechanism-ghostbody--A.png"),
            opt("B", "type: 06-relief-hero rather than 03-mechanism-ghostbody",
                "06-relief-hero", "1.16", "16:9", PIECE_B,
                "Puts the same wrong-and-right pair inside a real cab with a real "
                "person on the product, so the structural claim arrives with the "
                "buying context attached rather than on a white infinity ground.",
                variant="commercial",
                axes={"register": "commercial", "inset_mode": "vsinset"},
                notes="Needs the product photo. "
                      + KNOCK.format(t="06-relief-hero", s="content.items.4"),
                asset=f"{PAGE}-05-content3-mechanism-ghostbody--B.png"),
            opt("C", "execution: the product itself is the variable, shown broken "
                "in two against whole", "03-mechanism-ghostbody", "2.2", "16:9",
                PIECE_C,
                "Instead of comparing the product against generic pieces, it "
                "compares the product against a cut version of itself. The "
                "continuity is the only difference, which is precisely the "
                "section's sentence.",
                axes={},
                notes="Needs the product photo. Drawing the reference product "
                      "deliberately broken is the risk: a viewer who reads the "
                      "left panel as the real thing has been told the product "
                      "comes apart.",
                asset=f"{PAGE}-05-content3-mechanism-ghostbody--C.png"),
        ],
    },
    {
        "slot_id": "content.items.4.image", "section_role": "how-to-use",
        "asset": f"{PAGE}-06-content4-relief-hero.png",
        "placement": "Beside 'Everyday Versatility and What to Expect'.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "The argument IS temporal and this slot earns motion - "
                    "carrying one piece from a van seat to a desk chair and "
                    "setting it down is a hand acting on the product, which is "
                    "the `use` type's own job. It is refused by the BUDGET and "
                    "not by the argument: the `content` section runs to seven "
                    "items so ADR-032 allows it two loops, and items 2 and 5 hold "
                    "them. It is listed in motion.reserves as the relief loop's "
                    "substitute, where promoting it would still leave the spacing "
                    "rule satisfied."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT reads the section as what it is. The copy is not a how-to - "
            "there is one obvious action and multi_step_usage is false, which "
            "drops 03-use-sequence by its own avoid_when - it is a claim that one "
            "piece serves several places. 06-relief-hero --context is the inset "
            "mode for showing the product where it lives, and G7-X binds it "
            "honestly here because the mounting is freestanding in both frames: "
            "sat on top, no fitting either time. PAGE LEGALITY: 06-relief-hero is "
            "also recommended at content.items.5's option B, which is rung 4 on "
            "inset_mode. PRODUCT PRESENCE: dominant, carried in the main frame "
            "and seated in the inset. PROMPT RISK: the section also states two "
            "honest caveats - it seats you higher and it feels firm at first - "
            "and no option argues either, because neither is photographable and "
            "an image implying plushness would contradict the page's own words.",
        "options": [
            opt("A", "baseline", "06-relief-hero", "1.16", "16:9", CARRY_A,
                "The claim is portability between two places, so the main frame "
                "carries it and the inset shows the second place: under one arm "
                "at the van, seated on an office chair in the panel.",
                variant="commercial",
                axes={"register": "commercial", "inset_mode": "context"},
                notes="Needs the product photo. G7-X holds because both frames "
                      "show the same freestanding placement; an inset showing it "
                      "strapped or fitted would contradict the main frame.",
                asset=f"{PAGE}-06-content4-relief-hero--A.png"),
            opt("B", "type: 05-social-handoff rather than 06-relief-hero",
                "05-social-handoff", "2.5", "16:9", CARRY_B,
                "Versatility argued as a recommendation between two drivers, with "
                "the hollowed bare seat behind them as the trace of what the "
                "product just came off. No other slot on this page uses this "
                "type, so nothing is displaced.",
                axes={},
                notes="Needs the product photo. This is the only type-different "
                      "option on the page that displaces nothing.",
                asset=f"{PAGE}-06-content4-relief-hero--B.png"),
            opt("C", "execution: reduced to hands, and the two places swap",
                "06-relief-hero", "1.16", "16:9", CARRY_C,
                "The type's reduced form: hands lowering it onto a hard dining "
                "chair at home, with the van seat in the inset. It drops the "
                "person so the shape and the placement carry the argument.",
                variant="commercial",
                axes={"register": "commercial", "inset_mode": "context"},
                notes="Needs the product photo. No face means no expression to "
                      "carry ease, so the loose wrists and the unforced lowering "
                      "have to do it.",
                asset=f"{PAGE}-06-content4-relief-hero--C.png"),
        ],
    },
    {
        "slot_id": "content.items.5.image", "section_role": "outcome",
        "asset": f"{PAGE}-07-content5-relief-scene.png",
        "placement": "Beside 'Reclaiming My Family Life and Open Highway "
                     "Drives'.",
        "gif": {"eligible": True, "form": "whole-frame", "kind": "relief",
                "type_id": "relief", "rung": "natural",
                "reason":
                    "The section's claim is a stride that no longer stalls, which "
                    "is the `relief` type's own PURPOSE line. The still can hold "
                    "the moment of straightening but not the thing that makes it "
                    "an argument - that he keeps going without the pause, the "
                    "brace or the hand on the back. 06-relief-scene legislates no "
                    "motion layer, so the form is whole-frame and the kind is the "
                    "type's own job.",
                "asset": f"{PAGE}-07-content5-relief-scene--brief.svg",
                "refs": "gifs-library/relief/ — the folder card carries the law",
                "output": f"advertorial-relief-seat-cushion-l-shaped-v06.mp4",
                "ratio": "16:9", "duration_s": 3, "loop": "seamless loop",
                "brief":
                    "A man gets out of a car in a hotel car park at the end of a "
                    "long drive and walks away from it toward the entrance. He "
                    "stands straight up out of the seat in one movement, does not "
                    "stop to steady himself and does not put a hand to his back, "
                    "and his stride is even from the first step.",
                "alt":
                    "The same claim with no car and no actor: a wide shot of the "
                    "hotel entrance path where a suitcase is wheeled steadily out "
                    "of frame at walking pace, the wheels never pausing, and the "
                    "open car door and the product on the seat sit at the edge of "
                    "the frame throughout."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT, and the type's own pairing rule is satisfied. 06-relief-scene "
            "wants the closing image of an advertorial where the promise is a "
            "state of living rather than a feature, and it pairs naturally with a "
            "01-pain-scene of the same person - which the hero is. "
            "result_visibility is on-body, so the type is not dropped by the "
            "invisible-result gate that would have sent this to 06-relief-hero. "
            "PAGE LEGALITY: the arc lands correctly with relief after mechanism "
            "and use. EVIDENCE: the type is at 3.7. PRODUCT PRESENCE: present as "
            "its own object on the seat, in frame as the reason and never "
            "presented - which is the clause this type has failed on before. "
            "PROMPT RISK: a car park at a coastal hotel is close to the aspirational "
            "register the type bans, so the prompt names the wire bin, the worn "
            "bay lines and the unremarkable afternoon to hold it down.",
        "options": [
            opt("A", "baseline", "06-relief-scene", "3.7", "16:9", ROAD_A,
                "The exact moment the copy describes: out of the seat after three "
                "hours and straightening to full height with both hands empty. "
                "The relief is the absence of the brace, and the product is in "
                "frame as the reason rather than the subject.",
                axes={},
                notes="Needs the product photo.",
                asset=f"{PAGE}-07-content5-relief-scene--A.png"),
            opt("B", "type: 06-relief-hero rather than 06-relief-scene",
                "06-relief-hero", "1.16", "16:9", ROAD_B,
                "Argues the same outcome by what he can now lift rather than by "
                "how he stands, with the earlier state held in a recall panel so "
                "the before is in the frame instead of in the reader's memory.",
                variant="commercial",
                axes={"register": "commercial", "inset_mode": "recall"},
                notes="Needs the product photo. "
                      + KNOCK.format(t="06-relief-hero", s="content.items.4"),
                asset=f"{PAGE}-07-content5-relief-scene--B.png"),
            opt("C", "execution: the family beat rather than the arrival beat",
                "06-relief-scene", "3.7", "16:9", ROAD_C,
                "The copy's other resolved moment - kicking a ball back - played "
                "with the receiver off frame. It is the more active proof of the "
                "same claim and it keeps the product in shot on the seat behind.",
                axes={},
                notes="Needs the product photo. G13: the copy names a daughter "
                      "and this option deliberately keeps the other player out of "
                      "frame, so no minor appears in the render.",
                asset=f"{PAGE}-07-content5-relief-scene--C.png"),
        ],
    },
    {
        "slot_id": "content.items.6.image", "section_role": "comparison",
        "asset": f"{PAGE}-08-content6-proof-lockedframe.png",
        "placement": "Beside 'A Fraction of the Cost of Custom Ergonomics'.",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "A cost comparison is inspected, not watched, and the "
                    "difference the section argues is a price rather than an "
                    "event. Motion here would also break the fairness rule by "
                    "drawing the eye to one panel."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT by elimination and then by fit. The comparison cell in the "
            "advertorial column holds 04-proof-lockedframe --verdict and nothing "
            "else, and the type's use_when wants a reader who already understands "
            "the problem and mechanism - true by the seventh section and false "
            "earlier. --verdict rather than --rivals because the product belongs "
            "in frame here, which is the named difference from content.items.1 "
            "and what makes the repeat rung 4 rather than a collision. PAGE "
            "LEGALITY: two executions of one type, differing on variant and "
            "subject class, both saying so. PRODUCT PRESENCE: the last panel, "
            "correctly. PROMPT RISK: the alternatives are things people actually "
            "paid for, so the prompt fixes one framing and one grade across all "
            "three panels and forbids making either alternative look worse than "
            "it is - the fairness rule this variant carries.",
        "options": [
            opt("A", "baseline", "04-proof-lockedframe", "1.13", "16:9", COST_A,
                "Three panels, one seat, one framing: re-upholstery, a premium "
                "chair pad moved across, and the reference product simply set in "
                "place. The argument is what each required, and the last panel "
                "required nothing.",
                variant="verdict", axes={"camera_lock": "handheld"},
                notes="Needs the product photo for the last panel.",
                asset=f"{PAGE}-08-content6-proof-lockedframe--A.png"),
            opt("B", "type: 06-relief-hero rather than 04-proof-lockedframe",
                "06-relief-hero", "1.16", "16:9", COST_B,
                "Puts the money on one side and the cushion on the other inside a "
                "split panel - an empty treatment couch and a lone premium chair "
                "against the product in the seat. It argues recurring cost rather "
                "than one-off fitting.",
                variant="commercial",
                axes={"register": "commercial", "inset_mode": "vsinset"},
                notes="Needs the product photo. "
                      + KNOCK.format(t="06-relief-hero", s="content.items.4"),
                asset=f"{PAGE}-08-content6-proof-lockedframe--B.png"),
            opt("C", "execution: two panels, and the variable is the work each "
                "one demands", "04-proof-lockedframe", "1.13", "16:9", COST_C,
                "Strips the comparison to its sharpest pair: a seat stripped to "
                "its frame mid-re-upholstery against the product set on the "
                "finished seat with nothing altered. Cost is argued as labour "
                "rather than as a number.",
                variant="verdict", axes={"camera_lock": "handheld"},
                notes="Needs the product photo for the second panel. A stripped "
                      "seat is a strong image and risks reading as damage rather "
                      "than as paid work; the tools on the floor are what say it "
                      "is a job in progress.",
                asset=f"{PAGE}-08-content6-proof-lockedframe--C.png"),
        ],
    },
]

for i, rev in enumerate(REVIEWS):
    SLOTS.append({
        "slot_id": f"reviews.shots.{i}.image", "section_role": "social-proof",
        "asset": f"{PAGE}-09-review{i}-social-snapshot.png",
        "placement": f"Review photo tile {i + 1} of 4, in the same section as "
                     f"the quotes. {rev['quote']}",
        "gif": {"eligible": False, "form": "none",
                "reason":
                    "A customer snapshot argues that the thing exists in a real "
                    "home. That is a held state, this type bans every added "
                    "layer, and the review wall is static by ADR-023."},
        "recommended_opt": "A",
        "recommendation_basis":
            "ONE OPTION, NOT THREE, because this is a repeating section "
            "(ADR-022): the SET is the unit of variation, so the budget is spent "
            "across the four tiles rather than inside one. FIT is fixed by the "
            "cell - 05-social-snapshot is the advertorial social-proof type for a "
            "review block and the trust gap it names is this block's exactly. "
            "Which execution each tile keeps is decided by the type's SET "
            "DIVERSITY LAW: four different room classes, three content modes, and "
            "a different light temperature and camera distance on each. PAGE "
            "LEGALITY: BLOCKED, and this outranks everything else - nothing here "
            "ships until the layout changes. PRODUCT PRESENCE: G1 binds even in "
            "this register. PROMPT RISK: a face turns the image into a "
            "testimonial portrait, which is a different type's job and a "
            "compliance risk here, so every tile keeps to incidental limbs.",
        "options": [
            opt("A", rev["varies"], "05-social-snapshot", "1.2", "1:1",
                snap(rev["subject"], rev["scene"], rev["anchor"], rev["camera"]),
                "The moment this tile's quote describes, photographed as found, "
                "in the room class and content mode the SET law leaves for this "
                "position.",
                notes=REVIEW_BLOCK,
                asset=f"{PAGE}-09-review{i}-social-snapshot--A.png"),
        ],
    })

for slot_id, role, reason in (
    ("product.image", "cta",
     "A product card inside the mid-page offer block. mapping/slot-rules.md "
     "leaves the cta row empty in all four channels: this is a standard product "
     "shot, out of library scope by design."),
    ("product_end.image", "cta",
     "The closing product card, same as product.image."),
    ("hero.author_avatar", "author",
     "A byline portrait. mapping/slot-rules.md leaves the author row empty in "
     "all four channels - no library type produces a portrait of a named person, "
     "and generating a face to sit under a real byline is a disclosure decision "
     "rather than an image one."),
    ("guide.avatar", "author", "The About-the-author portrait, same as the "
     "byline avatar."),
    ("comments.items.0.avatar", "social-proof",
     "A commenter portrait, 1 of 6. Same reason as the author row: no library "
     "type produces portraits, and a generated face under a named comment is a "
     "fabricated person."),
    ("comments.items.1.avatar", "social-proof", "Commenter portrait, 2 of 6."),
    ("comments.items.2.avatar", "social-proof", "Commenter portrait, 3 of 6."),
    ("comments.items.3.avatar", "social-proof", "Commenter portrait, 4 of 6."),
    ("comments.items.4.avatar", "social-proof", "Commenter portrait, 5 of 6."),
    ("comments.items.5.avatar", "social-proof", "Commenter portrait, 6 of 6."),
    ("header.logo", "cta", "The brand logo, already supplied in the export as "
     "inline SVG."),
    ("footer.logo", "cta", "The brand logo, already supplied in the export as "
     "inline SVG."),
):
    SLOTS.append({
        "slot_id": slot_id, "section_role": role,
        "asset": "—", "placement": "—",
        "options": [], "out_of_scope_reason": reason,
    })

MOTION = {
    "floor": 2,
    "ceiling": 5,
    "delivered": 2,
    "margin": 0,
    "groups_covered": ["result", "working"],
    "shortfall_reason": None,
    "reserves": [
        {
            "slot_id": "content.items.1.image",
            "substitutes_for": "content.items.2.image",
            "type_id": "cause",
            "group": "working",
            "rung": "natural",
            "brief": "A close side view of a flat foam pad on a van seat with a "
                     "body settling onto it. The pad creeps forward off the back "
                     "of the seat base under the weight, opening a wedge of bare "
                     "seat behind it at the corner where the base meets the "
                     "backrest.",
            "why_held_back": "It earns motion on the argument and it is the same "
                             "gif type as the primary, so promoting it keeps "
                             "ADR-037's one-loop-per-type rule. It is refused "
                             "only by spacing: it sits directly beside "
                             "content.items.2 and ADR-032 bars two adjacent loops "
                             "inside one section. Promoted, it would still leave "
                             "the section at two non-adjacent loops with "
                             "content.items.5.",
        },
        {
            "slot_id": "content.items.4.image",
            "substitutes_for": "content.items.5.image",
            "type_id": "use",
            "group": "working",
            "rung": "natural",
            "brief": "A cushion is lifted off a van seat, carried a few steps and "
                     "set down onto an office chair, where it settles into place "
                     "against the backrest without being adjusted.",
            "why_held_back": "The content section may carry two loops and already "
                             "does, at items 2 and 5. Promoting this in place of "
                             "the relief loop leaves items 2 and 4 non-adjacent, "
                             "so the spacing rule still holds - but it trades the "
                             "page's only `result` loop for a second `working` "
                             "one and drops the group coverage the budget "
                             "prefers.",
        },
    ],
    "notes": [
        "Two loops against a floor of 2, so the margin is ZERO and this page is "
        "at the state ADR-032 was written to end. The structural ceiling here is "
        "3, not 5: the sections are hero, content, reviews and two cta cards, "
        "the review wall is static by ADR-023, the two cta cards are out of "
        "library scope, and the content section may hold two loops because it "
        "runs to seven items. The third would have to come from the hero "
        "section, and the hero is a held effort with no before and after inside "
        "it - it was examined at rung 1 and refused on the temporal test, not "
        "on the budget.",
        "Both groups are covered: `cause` is working and `relief` is result, "
        "which is the pairing the budget prefers rather than two working loops.",
        "Rung 2 was not needed and was not used. Both loops are natural rung-1 "
        "verdicts on the still as routed, and no slot was restaged to reach the "
        "floor.",
        "Two reserves, both real. content.items.1 is the stronger of the two "
        "because it is the same gif type as its primary and fails only the "
        "spacing rule; content.items.4 would cost the page its only result loop.",
    ],
}

OUT = {
    "page_id": PAGE,
    "registry_version": "2.0.0",
    "channel": "advertorial",
    "awareness_stage": "solution-aware",
    "slots": SLOTS,
    "motion": MOTION,
    "coverage": {
        "covered": [
            "step 1 pain — 01-pain-scene twice, the cab exit at the hero and the "
            "kitchen table at content.items.0",
            "step 2 cause — 02-cause-anatomy --diagnostic at content.items.2",
            "step 3 mechanism — 03-mechanism-ghostbody at content.items.3, "
            "available because body_contact is true",
            "step 4 proof — 04-proof-lockedframe twice, --rivals at "
            "content.items.1 and --verdict at content.items.6",
            "step 5 social — 05-social-snapshot across all four review tiles",
            "step 6 relief — 06-relief-hero --context at content.items.4 and "
            "06-relief-scene at content.items.5",
        ],
        "absent": [
            "step 2 symptom — 02-symptom-rail was trimmed off advertorial on "
            "2026-08-11 and is not a candidate at any rung",
            "step 3 use — 03-use-sequence is dropped by its own avoid_when, 'the "
            "product has one obvious action', and multi_step_usage is false",
            "step 5 personas — 05-persona-grid is marketplace and landing-page "
            "only",
        ],
        "absent_but_correct": [
            "No 01-pain-split, correctly — it is never_with 01-pain-scene and "
            "one pain beat per page is the rule; this page runs two executions of "
            "the same pain type instead, which rung 4 permits.",
            "No 03-mechanism-xray — the argument here is about a body structure "
            "rather than the product's internals, and ghostbody is the type for "
            "that whenever body_contact is true.",
        ],
        "gaps": [
            "The two honest caveats the copy states against itself — it seats the "
            "driver noticeably higher, and it feels firm for the first few days — "
            "are argued by no image on this page. Neither is photographable, and "
            "an image implying plushness would contradict the page's own words. "
            "They stay copy claims.",
            "The cost figures at content.items.6 are numbers, and no image "
            "asserts one. The recommended option argues what each alternative "
            "REQUIRED — fitting, a room, a chair that stays at one desk — which "
            "is the visible half of a price.",
        ],
    },
    "recommended": [],
    "page_composition_notes": [
        "lpTypeId is `advertorial` and needs no interpretation on this page, "
        "unlike the listicle exports. Awareness is read as solution-aware: "
        "brief.awarenessStage says `solution`, and the copy agrees — the reader "
        "meets a named fix by the fourth section and the first three sections are "
        "spent on fixes already tried rather than on establishing that a problem "
        "exists.",
        "EVERY CONTENT SLOT DECLARES 16:9 AND THE REVIEW TILES 1:1, so this page "
        "raises none of the 4:3 crop problem page 65 carries. Every option is "
        "rendered at the ratio its slot declares, and nothing is centre-cropped "
        "on the way in.",
        "body_contact: true is the gate that shapes this page. It keeps "
        "03-mechanism-ghostbody available, which is where the mechanism beat "
        "goes; on a page where it is false that type is dropped outright and "
        "every mechanism slot falls to 03-mechanism-xray.",
        "ONE-TYPE-ONCE BINDS THE SHIPPED SET, NOT THE OPTION POOL "
        "(query/runbook.md Step 4). Seven of the eight linear slots carry an "
        "option B with a different type, and each names the slot it would "
        "displace. hero.image is the exception: its role cell holds exactly one "
        "type after the gates, so its B is the gaze axis and varies_on says why.",
        "Two rung-4 repeats, both named where they happen. 01-pain-scene runs at "
        "the hero and at content.items.0, differing on place and failed action. "
        "04-proof-lockedframe runs at content.items.1 as --rivals and at "
        "content.items.6 as --verdict, differing on variant and on whether the "
        "product is in frame.",
        "THE REVIEW WALL IS BLOCKED AS THE PAGE IS BUILT, third page running. All "
        "four reviews.shots slots sit inside the same <section "
        "data-block-key=\"reviews\"> as three named quotes carrying Verified "
        "Purchase labels. 05-social-snapshot's authenticity fence bars a "
        "generated snapshot from sitting beside a name, star row or verified "
        "badge. Four prompts are written and every one carries the precondition.",
        "G13 is exercised twice and stated positively both times. The copy names "
        "a family dinner and a daughter; content.items.0 states that no child is "
        "present or visible, and content.items.5's option C keeps the other "
        "player out of frame. A minor never fills a subject slot in a pain scene.",
        "The reference photo is yours to upload. imageBriefs is null in the "
        "export so there is no photograph to hash (SPEC 6.4) and attachments is "
        "omitted rather than invented — but per ADR-021 that is a gap in the "
        "export, not a blocked prompt: the prompts that need it carry their G1 "
        "line and run as written once the photo is attached in the tool.",
        "No pick prior was available. feedback/picks.jsonl is empty, so the "
        ">=20-pick tie-breaker in SPEC 7.7 never fired and every recommendation "
        "here rests on fit, legality, render evidence, product presence and "
        "prompt risk alone.",
        "Ratio is set in the generation tool's aspect-ratio parameter, never in "
        "the prompt text (adapters/nano-banana.md Rule 4).",
    ],
}

# ---------------------------------------------------------------------------
# Emit
# ---------------------------------------------------------------------------

with open(os.path.join(HERE, "prompts.json"), "w", encoding="utf-8") as f:
    json.dump(OUT, f, indent=2, ensure_ascii=False)
    f.write("\n")


def md(d):
    L = []
    A = L.append
    routed = [s for s in d["slots"] if s["options"]]
    oos = [s for s in d["slots"] if not s["options"]]
    n_opts = sum(len(s["options"]) for s in d["slots"])
    gifs = [s for s in d["slots"] if s.get("gif", {}).get("eligible")]
    blocked = [o for s in d["slots"] for o in s["options"]
               if "BLOCKED" in (o.get("composition_notes") or "")]
    A("# Image prompts — page 122, ergonomic memory foam seat cushion")
    A("")
    A("GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — "
      "edit the script and re-run. Routing rationale, the negative motion "
      "verdicts and the out-of-scope slots are all in `prompts.json`.")
    A("")
    A(f"- page `{d['page_id']}` · {d['channel']} · {d['awareness_stage']} · "
      f"registry `{d['registry_version']}` · {len(routed)} routed slots · "
      f"{n_opts} prompts · {len(gifs)} motion briefs")
    m = d["motion"]
    A(f"- motion: {m['delivered']} loops, floor {m['floor']}, margin "
      f"{m['margin']}, groups {', '.join(m['groups_covered'])}")
    A(f"- **{len(blocked)} prompts carry a blocking precondition**, stated on "
      f"each")
    A("")
    A("---")
    A("")
    for s in d["slots"]:
        if not s["options"]:
            continue
        A(f"## `{s['slot_id']}` — {s['section_role']}")
        A("")
        A(f"- asset `{s['asset']}` · {s['placement']}")
        g = s.get("gif", {})
        media = "loop" if g.get("eligible") and g.get("form") != "none" \
            else "still"
        A(f"- recommended: **option {s['recommended_opt']}** · media **{media}**")
        A(f"- {s['recommendation_basis']}")
        A("")
        for o in s["options"]:
            v = f" `--{o['variant']}`" if o.get("variant") else ""
            A(f"### `{s['slot_id']}` · option {o['opt']} — `{o['type']}`{v}")
            A("")
            A(f"- varies on: {o['varies_on']}")
            ax = " · ".join(f"`{k}: {vv}`" for k, vv in (o.get("axes") or {}).items())
            A(f"- ratio `{o['ratio']}` · type version `{o['type_version']}`"
              + (f" · {ax}" if ax else ""))
            A(f"- {o['rationale']}")
            if o.get("composition_notes"):
                A(f"- **note:** {o['composition_notes']}")
            A("")
            A("```")
            A(o["prompt"])
            A("```")
            A("")
        if g.get("eligible") and g.get("form") != "none":
            A(f"### `{s['slot_id']}` · motion brief — gif type `{g['type_id']}`")
            A("")
            A(f"- output `{g['output']}` · {g['duration_s']}s · {g['ratio']} · "
              f"{g['loop']} · form `{g['form']}` · rung `{g['rung']}`")
            A(f"- plate `{g['asset']}` · library `{g['refs']}`")
            A(f"- {g['reason']}")
            A("")
            A("```")
            A(g["brief"])
            A("```")
            A("")
            A("Alternative shot of the same argument, if the primary is blocked:")
            A("")
            A("```")
            A(g["alt"])
            A("```")
            A("")
        A("---")
        A("")
    A("## Motion budget")
    A("")
    for n in m["notes"]:
        A(f"- {n}")
    A("")
    if m["reserves"]:
        A("**Reserves** — slots that earned motion and were refused by the "
          "budget or the spacing rule. A reserve REPLACES its primary, never "
          "adds to one.")
        A("")
        for r in m["reserves"]:
            A(f"- `{r['slot_id']}` → substitutes for `{r['substitutes_for']}` · "
              f"gif type `{r['type_id']}` ({r['group']}) · {r['why_held_back']}")
        A("")
    A("---")
    A("")
    A(f"## Out of library scope — {len(oos)} slots")
    A("")
    for s in oos:
        A(f"- `{s['slot_id']}` ({s['section_role']}) — {s['out_of_scope_reason']}")
    A("")
    return "\n".join(L) + "\n"


with open(os.path.join(HERE, "prompts.md"), "w", encoding="utf-8") as f:
    f.write(md(OUT))

# ---- self-checks, printed so a clean result is never assumed -----------------
routed = [s for s in OUT["slots"] if s["options"]]
n_opts = sum(len(s["options"]) for s in OUT["slots"])
print(f"slots {len(OUT['slots'])}  routed {len(routed)}  prompts {n_opts}")
over = [(s["slot_id"], o["opt"], o["type"], len(o["prompt"]))
        for s in routed for o in s["options"]
        if len(o["prompt"]) > CEIL.get(o["type"], 1800)]
print("over own type ceiling:", over or "none")
bad_ratio = [(s["slot_id"], o["ratio"]) for s in routed for o in s["options"]
             if o["ratio"] not in ("16:9", "4:3", "1:1", "3:4", "9:16")]
print("ADR-016 illegal ratios:", bad_ratio or "none")
print("attribute gates fired:", KILLED)
leak = [(s["slot_id"], o["opt"], o["type"]) for s in routed for o in s["options"]
        if o["type"] in KILLED]
print("options using a gated-out type:", leak or "none")

# Rule 1b: the only leaking tier is a heading that names a region. These prompts
# carry no headings at all, so the check is that none has appeared.
HEAD = re.compile(r"^\s*\[?[A-Z][A-Z \-/&']{2,30}\]?\s*:", re.M)
heads = [(s["slot_id"], o["opt"], HEAD.findall(o["prompt"])[:2])
         for s in routed for o in s["options"] if HEAD.search(o["prompt"])]
print("prompts carrying a heading (Rule 1b):", heads or "none",
      "| control:", HEAD.findall("SCENE LEFT: a thing"))

# ADR-021: nothing multi-pass, nothing composited.
print("options needing compositing:",
      [(s["slot_id"], o["opt"]) for s in routed for o in s["options"]
       if o["pipeline"] != "single-pass"] or "none")

# ADR-022: a repeating section emits one option per slot.
rev = [s for s in routed if s["slot_id"].startswith("reviews.shots")]
print("options per review tile:", sorted({len(s["options"]) for s in rev}),
      "- a repeating section emits one (ADR-022)")

# 05-social-snapshot SET DIVERSITY, checked across the tiles.
ROOMS = ("bedroom", "bathroom", "kitchen", "living room", "landing", "van",
         "office", "car")


def room_class(text):
    low = text.lower()
    hits = [(low.index(r), r) for r in ROOMS if r in low]
    return min(hits)[1] if hits else "UNCLASSIFIED"


rooms = [room_class(re.search(r"An ordinary (.{0,60})", s["options"][0]["prompt"]).group(1))
         for s in rev]
modes = [("in-use" if "mid-use" in s["options"][0]["prompt"] else "at-rest")
         for s in rev]
print("SET DIVERSITY room classes:", rooms)
print("  repeated room classes:",
      sorted({r for r in rooms if rooms.count(r) > 1}) or "none")
print("  content modes:", modes, "- distinct:", len(set(modes)))

# ADR-037: one loop per gif type per page, and the name is the only one it has.
gifs = [s for s in routed if s.get("gif", {}).get("eligible")
        and s["gif"].get("form") != "none"]
tids = [s["gif"]["type_id"] for s in gifs]
print("gif types delivered:", tids, "| duplicated:",
      sorted({t for t in tids if tids.count(t) > 1}) or "none")
expected = {f"advertorial-{t}-seat-cushion-l-shaped-v06.mp4" for t in tids}
actual = {s["gif"]["output"] for s in gifs}
print("gif output names match ADR-036:", actual == expected, sorted(actual))
print("motion delivered vs floor:", MOTION["delivered"], "/", MOTION["floor"],
      "margin", MOTION["margin"])

# Contract checks — the routing against the declared input.
emitted = {s["slot_id"] for s in OUT["slots"]}
print()
print("CONTRACT CHECKS")
print("  channel:", CONTRACT["page"]["channel"], "== emitted", OUT["channel"],
      "->", CONTRACT["page"]["channel"] == OUT["channel"])
print("  slots in the contract but not emitted:",
      sorted(set(DECLARED) - emitted) or "none")
print("  slots emitted but not in the contract:",
      sorted(emitted - set(DECLARED)) or "none")
print("  roles disagreeing with the contract:",
      [(s["slot_id"], s["section_role"], DECLARED[s["slot_id"]]["role"])
       for s in OUT["slots"] if s["slot_id"] in DECLARED
       and s["section_role"] != DECLARED[s["slot_id"]]["role"]] or "none")
print("  options rendered at a ratio the slot does not declare:",
      [(s["slot_id"], o["opt"], o["ratio"], DECLARED[s["slot_id"]]["ratio"])
       for s in routed for o in s["options"]
       if s["slot_id"] in DECLARED
       and o["ratio"] != DECLARED[s["slot_id"]]["ratio"]] or "none")
print("  gif ratio == slot ratio (whole-frame owes the page's shape):",
      all(s["gif"]["ratio"] == DECLARED[s["slot_id"]]["ratio"] for s in gifs))

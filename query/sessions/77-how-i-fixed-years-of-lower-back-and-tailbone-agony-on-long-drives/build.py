#!/usr/bin/env python3
"""Build prompts.json and prompts.md for page 77 — ergonomic memory foam seat cushion.

prompts.json is the source of truth (query/output.schema.json); prompts.md is
generated from it and is never hand-edited (query/runbook.md Step 7).

Run from anywhere:  python3 query/sessions/77-.../build.py
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAGE = "77"


def _index_types():
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
                if len(v) > 1 and v[0] == '"' and v[-1] == '"':
                    v = v[1:-1]  # a quoted scalar; lists keep their brackets
                out[tid][k] = {"true": True, "false": False}.get(v, v)
    return out


TYPES = _index_types()
CONTRACT = json.load(open(os.path.join(HERE, "content.json"), encoding="utf-8"))
ATTRS = CONTRACT["product"]["attributes"]
DECLARED = {sl["slot_id"]: {"ratio": sl["ratio"], "role": sec["role"]}
            for sec in CONTRACT["page"]["sections"]
            for sl in sec["image_slots"]}

# mapping/slot-rules.md attribute gates, written as data so the routing is checked
# against them rather than trusted.
ATTRIBUTE_GATES = [
    (lambda a: a["symptom_visibility"] == "invisible", "01-pain-split",
     "symptom_visibility: invisible drops 01-pain-split"),
    (lambda a: a["body_contact"] is False, "03-mechanism-ghostbody",
     "body_contact: false drops 03-mechanism-ghostbody"),
    (lambda a: a["result_visibility"] == "invisible", "06-relief-scene",
     "result_visibility: invisible drops 06-relief-scene"),
    (lambda a: a["multi_step_usage"] is False, "03-use-sequence",
     "multi_step_usage: false drops 03-use-sequence"),
]

# Canonical NEGATIVE lists, copied from each type file. Since ADR-014 none of this is
# rendered into a prompt; it travels in the `avoid` field for a model with a real
# negative channel.
AVOID = {
    "01-pain-scene": [
        "red glow", "pain hotspots", "graphic overlay", "arrows", "badges",
        "split panel", "white background", "studio lighting", "stock photo look",
        "posed model", "fake grimace", "smiling", "clean staged interior",
        "saturated colors", "advertising composition", "product placement",
        "bright airy lighting", "flat daylight look", "looking at camera"],
    "02-cause-anatomy": [
        "photographic elements", "3D render", "photorealistic skin", "human face",
        "facial features", "gore", "wet tissue", "correct side on the left",
        "both dashed lines identical", "missing badge on either panel",
        "different figure scale between panels", "extra signal colours",
        "saturated ground", "anatomically wrong structures", "background pattern",
        "reference product in frame", "branded remedy object"],
    "03-mechanism-ghostbody": [
        "human face", "facial features", "hair", "skin tone", "clothing",
        "photographic background", "environment", "furniture", "shadows on floor",
        "extra colors", "rainbow palette", "anatomically wrong structures",
        "floating disconnected organs", "dimension lines overlapping product edge",
        "cluttered inset", "gore", "realistic flesh", "medical horror"],
    "04-proof-lockedframe": [
        "badges", "arrows", "glows", "checkmarks", "one panel brighter",
        "inconsistent lighting between panels", "studio background",
        "clean styled set", "staged perfection", "saturated colors",
        "red or green cues", "motion blur", "people", "hands", "brand logos",
        "recognizable trademarks", "identical framing between panels",
        "pixel-perfect alignment", "tripod shot", "3D render look", "CGI",
        "product visualization",
        "last panel brighter or cleaner than the others",
        "hero lighting on the final panel", "alternatives made to look broken",
        "cluttered first panels"],
    "05-social-snapshot": [
        "studio lighting", "softbox reflections", "seamless background",
        "negative space", "color grading", "professional composition",
        "styled props", "badges", "borders", "star ratings", "reviewer names",
        "avatars", "text overlays", "product render look", "perfect symmetry",
        "magazine polish", "influencer aesthetic"],
    "06-relief-hero": [
        "cluttered background", "dark moody lighting", "pain cues in main scene",
        "blurry product", "inconsistent product between layers",
        "same angle repeated", "fabricated colorways",
        "mixed illustration and photo inside one inset half",
        "invented spray or mist", "fake steam", "unlabelled before-state inset",
        "low resolution inset", "inset darker than hero"],
    "06-relief-scene": [
        "badges", "arrows", "drawn overlays", "insets of any kind",
        "looking at camera", "posing", "laughing as the relief",
        "a situation that costs nothing", "a guarded body",
        "hand braced on furniture", "a part held or covered", "arms raised",
        "celebration gesture", "golden hour", "warm flattering light",
        "glamour lighting", "beauty retouching", "plastic skin",
        "aspirational travel location", "empty clean street", "styled outfit",
        "product presented to camera", "product centred or held up",
        "product hidden inside or under something",
        "product turned away so its face cannot be read", "back-of-pack label",
        "barcode", "bar chart", "bars of stepped or graded height", "arrowheads",
        "translucent marks", "blank expression", "collapsed posture",
        "head lolled back", "limbs flung limp", "eyes shut and slack",
        "drained joyless grade", "saturated colors", "stock photo look"],
}

# ---------------------------------------------------------------- the prompts

P_HERO_A = """A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his late forties in a creased work polo, still belted into the driver's seat of his own car on the driveway at the end of the day, mid-way through hauling himself forward off the seat back with both hands locked round the top of the steering wheel. Under that force: both arms straight and carrying his weight, shoulders drawn up towards his ears, hips still down in the seat, his whole back held rigid in one piece instead of bending. Face: brow drawn in, jaw set, breath held, eyes down at the footwell.

His hips sit well below his knees in the backward-sloping seat, his lower back is pressed flat against the seat back with an open gap behind it, and his weight has gone onto the base of his spine.

One specific place: a suburban driveway at the end of the working day, the driver's door swung open behind him, and the lived-in clutter of the commute — a travel mug gone cold in the holder, a lanyard and keys spilled across the passenger seat, a folded hi-vis jacket on the back seat, a parking receipt in the door pocket.

He is unaware of the camera, his gaze down and inward. Key light: cold blue dusk through the windscreen, weak and directionless. Fill: the dim dome light above him. A rim of light separates his shoulder from the dark interior. Deep shadow across the lower third of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_HERO_B = """A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his late forties in a creased work polo, seated at a dispatch desk in the middle of the afternoon, turned away from his monitor towards the camera with his right hand pushed into the small of his own back and his left braced flat on the desk edge. Under that force: his trunk twisted and held part-way round, weight shifted onto one hip, the other heel lifted off the floor. Face: brow raised and tight, mouth pressed thin, looking directly into the lens and holding it.

He has slid forward to the front edge of the chair so his lower back has left the backrest entirely, and there is an open gap between the base of his spine and the seat back behind him.

One specific place: a shipping depot dispatch office in the middle of a shift, and the lived-in clutter of the routine it disrupts — a printed run sheet weighted down with a stapler, a cold mug ringed with old coffee, a hard hat on the filing cabinet, a desk fan turned to the wall.

Key light: even overhead office daylight, bright and flat, minimal shadow, unflattering. Fill: the room's own ambient.

Desaturated throughout, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_HERO_C = """A cinematic film still, editorial photojournalism, natural and unstaged.

A woman in her early fifties in a fleece and work trousers, in the cab of a delivery van pulled onto a lay-by, mid-way through pushing herself up off the seat with one hand flat on the wheel and the other pressing down on the seat base beside her thigh. Under that force: both elbows locked, one shoulder dropped lower than the other, hips lifting in one slow piece with her back kept straight and unmoving. Face: eyes narrowed, lips parted on a held breath, gaze fixed on the windscreen.

Her hips sit below her knees in the sloped bench seat, her lower back is flattened against a seat back that curves away from it, and an open gap runs the width of her lower spine.

One specific place: a roadside lay-by in the middle of a delivery round, the door half open, and the lived-in clutter of the shift — a clipboard of delivery notes on the passenger seat, a flask wedged in the door pocket, a crumpled sandwich wrapper in the cup holder, a hi-vis tabard over the seat back.

She is unaware of the camera, her gaze forward and inward. Key light: flat grey daylight through the windscreen, cold and weak. Fill: the dim of the cab. A rim of light along her forearm. Deep shadow across the near side of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_PROB0_A = """A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is what is left on a car's driver seat after every ordinary fix has been tried and abandoned, photographed from the open driver's door at standing height.

Exactly as they were left: a thin flat foam pad slid right forward to the front lip of the seat base, its cover rucked into a ridge; a doughnut ring tipped on edge down in the footwell; a cylindrical lumbar roll dropped into the crack between the seat base and the backrest with only its end still showing; a beaded seat cover shoved into a heap against the far bolster. Behind all of them the gap where the base meets the backrest is wide open, and every one of them has slid away from the place it was meant to fill.

One specific place: a car parked on a driveway in the middle of a weekday, the driver's door standing open, and the lived-in clutter of the routine none of them fixed — a travel mug in the holder, a crumpled parking receipt in the door pocket, a phone cable trailing loose from the dashboard, a folded hi-vis jacket on the back seat.

No subject, so no gaze. The frame looks across the seat from the open door, the way the person who gave up on them is looking at it. Key light: flat overcast daylight through the open door, cold and even. Fill: the dim of the cabin. Rim light along the front lip of the seat base. Deep shadow down the far side of the seat.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_PROB0_B = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different days. One framing for every panel: the same office swivel chair photographed square-on from about a metre and a half back at seated eye height, the seat base across the lower third and a plain office partition filling the upper third. It reads as one shot taken three times, never as three different shots.

The same chair, the same partition and the same floor in all three panels, with deliberate real-world clutter: a coiled network cable along the skirting, a recycling bin half out of shot, scuff marks on the chair's base.

The only thing that changes is which ordinary seat fix is on the chair, and each is the plain unbranded version people already own. Panel one: a flat foam pad, slid forward off the back of the seat base. Panel two: a doughnut ring cushion, rolled forward on itself. Panel three: a separate cylindrical lumbar roll strapped to the backrest, sagged down out of the small of the back. All three photographed at the same point in the process, at the end of a working day, none of them touched or straightened first.

Light differs only in exposure between panels, never in warmth. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours none of them.

No product, no badges, no arrows, no text of any kind."""

P_PROB0_C = """A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is the drawer of abandoned seat fixes in a home office, pulled fully open and photographed from above at standing height.

Exactly as they were left: a flat foam pad compressed permanently into a body-shaped dish, folded once to fit; a doughnut ring with its cover pilled and its edge collapsed; a lumbar roll with one of its snapped elastic straps still threaded through the buckle; a beaded seat cover rolled and jammed down the side, several beads split from their cords. Nothing has been cleaned, matched or squared up.

One specific place: the bottom drawer of a desk unit in a spare-room office on a weekday morning, and the lived-in clutter of the room around it — a stack of unopened post on the desk above, a charger cable tangled at the back of the drawer, a dried-out marker pen, a laminated depot pass.

No subject, so no gaze. The frame looks straight down into the open drawer from standing height, the way the person who filled it is looking at it. Key light: cool window daylight from one side, flat and weak. Fill: the dim of the room. Rim light along the near edge of the drawer front. Deep shadow at the back of the drawer.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_PROB1_A = """A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, sacrum and lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has rolled backward into the open gap where the seat base meets the backrest, the sacrum has taken the load, and the lumbar curve has flattened and reversed. Right panel: the same figure on the same seat with a continuous supportive contour filling that gap, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the contour covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_PROB1_B = """A 2D flat-vector medical illustration with flat fills and hard edges, no gradients. Not photography, not a 3D render.

The attached photo is the exact reference for the product.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, sacrum and lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded, the pelvis rolled back into the open gap at the seat corner and the sacrum carrying the load. Right panel: the same figure on the same seat with the reference product in place, drawn at a size and angle where it is obviously that product, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the product covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_PROB1_C = """A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same three-quarter rear view in both, the whole body in shot with the seat small within it. The two sitting bones, the sacrum and the soft tissue over them are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. These are the sitting bones and sacrum, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has tipped back off the sitting bones so the load has moved onto the tailbone at the base of the sacrum. Right panel: the same figure on the same seat with a continuous supportive contour filling the gap at the seat corner, the load back on the two sitting bones and the tailbone clear of the seat. Neither the seat nor the contour covers the sacrum on either panel.

Marks: a filled region bounded by the contact surface itself, as wide as the contact is, one per panel — red on the left over the tailbone where the load has gone, blue on the right across both sitting bones where it belongs. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_FEAT0_A = """A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated side-on in an ordinary matte grey car seat whose base slopes backward: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical seat in both. The body is cross-sectioned along the midline so the pelvis, sacrum and lumbar spine are visible inside the silhouette.

The pelvis, sacrum and lumbar vertebrae are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: the mannequin sits in the seat with nothing filling the gap where the base meets the backrest, the pelvis rolled backward into that gap and the lumbar curve flattened. A flat hard-edged red overlay, unshaded, lies on the sacrum and the lowest two lumbar vertebrae where the load has collected.

Right panel is the correct state: the reference product is in place on the same seat, at the same angle, its contour visibly following the line of the pelvis and lumbar spine. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all. A flat hard-edged blue band, unshaded, is drawn beside the lumbar spine along its own length on the side away from the product, running only the length the product reaches — never a fill of the bone, never a tint of the anatomy.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product."""

P_FEAT0_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his late forties in an ordinary open-collar shirt, seated at a home office desk with his weight settled evenly and his gaze on the paperwork in front of him rather than on the product, sitting well back so the whole back of the chair and the product on it are clear to the camera. He sits to the right of the frame.

The reference product is on the chair behind him, its seat section under him and its lumbar section up against his lower back, identical to the attached photo in shape, colour and proportion.

One real room filled to the edges with objects that genuinely belong there: a full bookshelf, a wall calendar turned to the wall, a mug on a coaster, a router with its cable looped, a coat over the door, a houseplant on the sill. Background blurred, but no bare wall or floor area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

In the upper left of the frame, occupying the space he is offset from, sits a small rectangular panel with a thin white border, split into two equal halves that share one photographic register. The left half shows the same chair with an ordinary flat foam pad and a separate lumbar roll on it, the pad slid forward and the roll dropped into the gap, with glowing red points on the exposed seat corner and on the fallen roll. The right half shows the same chair with the reference product in place, brighter and cleaner, with a translucent blue overlay following the single continuous seam that runs from the seat section up into the lumbar section. A circular red badge carrying the white letters VS sits at the seam between the two halves.

No mark of any kind appears anywhere outside that panel."""

P_FEAT0_C = """A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated side-on in an ordinary matte grey office chair: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical chair in both. The body is cross-sectioned along the midline so the lumbar vertebrae and the discs between them are visible inside the silhouette.

The lumbar vertebrae and their intervertebral discs are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: the mannequin sits with nothing filling the gap at the seat corner, the lumbar curve reversed into a backward bow and the front edges of the lower discs pinched closed. A flat hard-edged red overlay, unshaded, lies on the two lowest discs where they are compressed.

Right panel is the correct state: the reference product is in place on the same chair, at the same angle, its lumbar contour visibly following the restored curve of the spine. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all. A flat hard-edged blue band, unshaded, is drawn beside the lumbar vertebrae along their own length on the side away from the product, running only the length the product reaches — never a fill of the bone, never a tint of the anatomy.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product."""

P_FEAT1_A = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his late forties in a work polo, sitting relaxed in the driver's seat of a parked car with the door open, one hand loose on his thigh and his gaze out through the windscreen rather than at the product. He is settled back against the seat with his weight even through both hips, and he sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with things that genuinely belong there: a travel mug in the holder, a lanyard hung from the indicator stalk, a phone cable coiled at the dash, a folded jacket on the back seat, a parking permit clipped to the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, occupying the space he is offset from, sits a small rectangular panel with a thin white border, split into two equal halves that share one photographic register. The left half shows the same empty driver's seat with an ordinary flat foam pad slid forward to the front lip and a separate lumbar roll fallen into the crack behind it, with glowing red points on the open seat corner, on the front lip where the pad has crept to, and on the end of the fallen roll. The right half shows the same empty seat with the reference product in place and unmoved, brighter and cleaner, with a translucent blue overlay following the single continuous seam that runs from the seat section up into the lumbar section. A circular red badge carrying the white letters VS sits at the seam between the two halves.

No mark of any kind appears anywhere outside that panel."""

P_FEAT1_B = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product.

Shot by one person on a phone across one working week. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a travel mug in the holder, a parking receipt in the door pocket, real wear on the sill.

The reference product is the subject of every panel and is the same physical object throughout — the same outline, the same black, the same continuous L-shaped contour, matching the attached photo exactly. It sits in the same starting position in the seat in every panel.

The only thing that changes is the point in the week: panel one on Monday morning before the first drive, panel two on Wednesday evening after two days of commuting, panel three on Friday evening after the full week. Every panel is photographed at the same point in the routine, with the driver already out of the car and nothing touched, straightened or pushed back into place first. Across all three the product has not crept forward off the seat base and has not dropped into the crack at the seat corner.

Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No badges, no arrows, no text of any kind."""

P_FEAT1_C = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her early fifties in a plain jumper, sitting relaxed in a home office swivel chair with both feet flat on the floor, one hand resting loose on the desk and her gaze on the window rather than at the product. Her weight is even through both hips and she is settled back into the chair, sitting to the right of the frame so the whole chair back and the product against it stay clear to the camera.

The reference product is on the chair beneath and behind her, its seat section under her and its lumbar section standing up against the small of her back, identical to the attached photo in shape, colour and proportion.

One real home office filled to the edges with things that genuinely belong there: a full bookshelf, a mug on a coaster, a desk lamp turned away, a router with its cable looped, a cardigan over the chair arm, a houseplant on the sill. Background blurred, but no bare wall or floor area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

In the upper left of the frame, occupying the space she is offset from, sits a small rectangular panel with a thin white border, split into two equal halves that share one photographic register. The left half shows the same empty swivel chair with an ordinary flat foam pad slid forward to the front lip and a separate lumbar roll strapped to the backrest and sagged down below the small of the back, with glowing red points on the open seat corner, on the front lip where the pad has crept to, and on the slack strap. The right half shows the same empty chair with the reference product in place and unmoved, brighter and cleaner, with a translucent blue overlay following the single continuous seam that runs from the seat section up into the lumbar section. A circular red badge carrying the white letters VS sits at the seam between the two halves.

No mark of any kind appears anywhere outside that panel."""

P_FEAT2_A = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different days. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a travel mug in the holder, a parking receipt in the door pocket, real wear on the sill.

The only thing that changes is which cushion is on the seat, and each is photographed at the same point in the routine — at the end of a full day's driving, with the driver already out of the car and nothing plumped, straightened or pushed back into place first. Panel one: a plain unbranded flat foam pad, the two most common inches of foam anyone owns, compressed under its own use into a shallow dish that has not sprung back. Panel two: a plain unbranded doughnut ring cushion, its ring flattened along the front where the weight sat. Panel three: the reference product, its continuous L-shaped contour still standing to its full depth at the seat corner.

All three are ordinary, clean and in good condition, and all three get exactly the same exposure, the same background tidiness and the same framing generosity. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No badges, no arrows, no text of any kind."""

P_FEAT2_B = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different days. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a travel mug in the holder, a parking receipt in the door pocket, real wear on the sill.

The only thing that changes is which of three common existing alternatives is on the seat, all plain and unbranded and all the kind of thing the viewer already owns. Panel one: a flat foam pad, compressed under its own use into a shallow dish. Panel two: a doughnut ring cushion, its ring flattened along the front. Panel three: a gel seat pad, sagged into a low ridge along its centre. Every panel is photographed at the same point in the routine, at the end of a full day's driving, with the driver already out of the car and nothing plumped or straightened first.

None of them is damaged or dirty, none is exaggerated, and none of them wins. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours none of them.

No product, no badges, no arrows, no text of any kind."""

P_FEAT2_C = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different days. One framing for every panel: the same office swivel chair photographed square-on from about a metre and a half back at seated eye height, the seat base across the lower third and a plain office partition filling the upper third. It reads as one shot taken three times, never as three different shots.

The same chair, the same partition and the same floor in all three panels, with deliberate real-world clutter: a coiled network cable along the skirting, a recycling bin half out of shot, scuff marks on the chair base.

The only thing that changes is which cushion is on the chair, and each is photographed at the same point in the routine — at the end of a full working day, with nobody in the room and nothing plumped, straightened or squared up first. Panel one: a plain unbranded flat foam pad, compressed under its own use into a shallow dish that has not sprung back. Panel two: a plain unbranded memory foam wedge, its thin end folded over where the weight sat. Panel three: the reference product, its continuous L-shaped contour still standing to its full depth at the seat corner.

All three are ordinary, clean and in good condition, and all three get exactly the same exposure, the same background tidiness and the same framing generosity. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No badges, no arrows, no text of any kind."""

P_FEAT3_A = """A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his late forties in put-together but ordinary clothes, just out of the driver's seat of his car in a coastal car park at the end of a long drive, straightening up to his full height with his weight even through both feet and both hands empty and open at his sides. Nothing is held, nothing is braced, nothing is covered. His chest is opening, his shoulders roll back and down, his eyes are coming open against the light and his brow has let go, and a small involuntary smile has arrived on its own while he looks out past the car at the water rather than at the camera.

The driver's door stands open beside him, and the reference product sits on the seat inside it as its own object near the camera, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary public car park above a working coastline on an unremarkable day, two or three blurred passers-by and a parked van further along, gulls, a wire bin, painted bay lines worn thin. Nothing aspirational and nothing tidied.

Even natural daylight, bright, soft shadows, plain and unglamorous. A natural palette, light film grain, shallow depth of field, honest rather than drained and never warm-boosted.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text."""

P_FEAT3_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his late forties in an open-collar shirt, sitting relaxed in the driver's seat of a parked car with the door open and one arm resting easily along the sill, his gaze out through the windscreen rather than at the product. His weight is even through both hips, he is settled back against the seat with nothing braced, and he sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with things that genuinely belong there: a travel mug in the holder, a lanyard hung from the indicator stalk, a phone cable coiled at the dash, a folded jacket on the back seat, a parking permit clipped to the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text.

Soft even daylight through the open door, background blurred, high-key neutral grade.

The whole frame is the resolved state. No inset, no panel, no badge, no arrow and no mark of any kind anywhere in the picture."""

P_FEAT3_C = """A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his late forties in put-together but ordinary clothes, on the loading apron of a shipping depot mid-morning, lifting a crate off the tailgate of a van and up onto his shoulder in one unbroken movement, weight even through both feet and his back doing the work without hesitation. Nothing is braced against the van, nothing is favoured, nothing is held back. His chest opens as the crate goes up, his shoulders are back and down, his eyes are open and creased at the corners and a small involuntary smile has arrived on its own while he looks along the apron at the next load rather than at the camera.

The van's cab door stands open behind him, and the reference product sits on the driver's seat inside it as its own object near the camera, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary working depot apron on a grey weekday, two or three blurred colleagues further down the line, a pallet truck, a wheelie bin, worn painted bay markings and puddles from earlier rain.

Even natural daylight, bright, soft shadows, plain and unglamorous. A natural palette, light film grain, shallow depth of field, honest rather than drained and never warm-boosted.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text."""

P_REV_1 = """A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use in a car, photographed by its owner from the open driver's door: the reference cushion in place on the driver's seat with the owner's forearm resting across the top of the lumbar section, nobody else visible and no face in shot.

An ordinary family car photographed exactly as found on a weekday morning — the mess stays, nothing tidied, nothing added for the picture. Cool early daylight through the windscreen and the open door, no other light.

One incidental owner object and no more: a travel mug sitting in the cup holder.

Framing slightly tilted and a little too close, taken at arm's length from the seat; focus adequate but casual, mild noise, exposure honest to the light in the car.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture."""

P_REV_2 = """A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product simply sitting where it now lives, photographed by its owner: the reference cushion in place on a home office swivel chair, nobody in the picture at all.

An ordinary spare-room home office photographed exactly as found in the evening — the mess stays, nothing tidied, nothing added for the picture. Warm yellow light from a single desk lamp and the room's overhead, no daylight, no other light.

One incidental owner object and no more: a charger cable coiled on the desk behind the chair.

Framing off-centre and taken from standing height looking down at the chair; focus adequate but casual, mild motion softness, exposure honest to the lamp light.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture."""

P_REV_3 = """A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use in a truck cab, photographed by its owner over their own shoulder: the reference cushion in place on the bench seat with two fingers of the owner's hand tucked against the edge of the lumbar section, no face in shot.

An ordinary working truck cab photographed exactly as found on a flat grey afternoon — the mess stays, nothing tidied, nothing added for the picture. Flat overcast daylight through the side window, no other light.

One incidental owner object and no more: a clipboard wedged against the far side of the seat.

Framing close and crooked, taken from very near the seat over the shoulder; focus adequate but casual, mild noise, exposure honest to the grey light.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture."""

P_REV_4 = """A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The opened box and its contents as the owner has just left them, photographed from above: the reference cushion out of its packaging and resting on a kitchen worktop, still recovering its shape, with the flattened box and the plastic sleeve it came in pushed to one side. Nobody in the picture at all.

An ordinary kitchen photographed exactly as found in the middle of the day — the mess stays, nothing tidied, nothing added for the picture. Mixed light, warm ceiling spots over cool daylight from the window, no other light.

One incidental owner object and no more: a fruit bowl at the edge of the worktop.

Framing slightly tilted and taken from standing height about half a metre back across the worktop; focus adequate but casual, mild noise, exposure honest to the mixed light.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture."""

# --- G12 brief plates (ADR-020: a gif slot emits a plate render) --------------

PLATE_PROB0 = """A flat card and nothing else. The whole image is a flat dark grey field with a thin white border just inside its edge, held clear of every frame edge.

Centred on it, in clean white sans-serif, five short lines, each on one line, plain words with no other text anywhere in the picture:

GIF SLOT · 3s · seamless loop
SHOT     open car door, seat and pads
ACTION   pads creep forward, gap opens
RESULT   nothing was holding the pelvis
MATCH    same overcast daylight and cabin

No scene, no product, no photograph, no other text."""

PLATE_FEAT2 = """A flat card and nothing else. The whole image is a flat dark grey field with a thin white border just inside its edge, held clear of every frame edge.

Centred on it, in clean white sans-serif, five short lines, each on one line, plain words with no other text anywhere in the picture:

GIF SLOT · 3s · seamless loop
SHOT     one seat, cushion filling frame
ACTION   weight lifts, the contour returns
RESULT   it did not stay squashed
MATCH    same seat and daylight as still

No scene, no product, no photograph, no other text."""


# ---------------------------------------------------------------- slot table

def opt(letter, tid, varies, ratio, prompt, rationale, variant=None, axes=None,
        notes=None):
    o = {
        "opt": letter, "varies_on": varies, "type": tid,
        "type_version": TYPES[tid]["version"], "ratio": ratio,
        "pipeline": "single-pass", "prompt": prompt.strip(),
        "avoid": AVOID[tid], "rationale": rationale,
    }
    if variant:
        o["variant"] = variant
    if axes:
        o["axes"] = axes
    if notes:
        o["composition_notes"] = notes
    return o


WALL_FENCE = (
    "PRECONDITION, and it is not optional: these four photo tiles sit inside the same "
    "review section as three attributed quotes, each carrying a reviewer name and a "
    "Verified Purchase label. 05-social-snapshot's authenticity fence forbids a generated "
    "snapshot anywhere near a reviewer name, avatar, star row or verified badge. The page's "
    "own brief already marks all four slots `route: asset`, and the type's avoid_when says "
    "real customer photos always win over generated ones. Use real customer photographs, or "
    "move the photo grid out of the attributed block, or drop the names and Verified "
    "Purchase labels — before rendering any of these.")

SLOTS = []

SLOTS.append({
    "slot_id": "hero.image", "section_role": "hero",
    "asset": "77-01-hero-pain-scene.png",
    "placement": "advertorial header, under the eyebrow and above the byline",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides, and it is close to verbatim. 01-pain-scene --candid asks for physical "
        "pain in a moment nobody would choose to be seen in, and hero.body.0 is that moment in "
        "the page's own words — gripping the steering wheel just to brace himself before "
        "standing up. A plays it as the single seated action the whole page is written "
        "against. B moves to the confront gaze, which the type reserves for appearance and "
        "self-image rather than physical pain, and loses the brace. C keeps the action but "
        "moves it to a delivery driver, a real reader of this page but the second one. PAGE "
        "LEGALITY: A satisfies 06-relief-scene's requires_pair at features.items.3 and "
        "pairs_with 04-proof-lockedframe at features.items.2. EVIDENCE: candid is this type's "
        "most-rendered branch. PRODUCT PRESENCE: none, correctly — the type bans it. "
        "PROMPT RISK: {chars} characters against a measured band of 1379-2153.",
    "options": [
        opt("A", "01-pain-scene", "baseline", "16:9", P_HERO_A,
            "The page's opening scene played straight: the driver hauling himself off the seat "
            "back on his own driveway. Evidence is the symptom as physical fact — hips below "
            "knees in the sloped seat, the lumbar curve flattened with the gap open behind it.",
            variant="candid", axes={"gaze": "candid"}),
        opt("B", "01-pain-scene", "axis: gaze=confront", "16:9", P_HERO_B,
            "The same argument in the type's other gaze. The advertorial hero cell holds one "
            "type and the attribute gates leave no second, so the honest variation is the axis "
            "rather than a type borrowed from a role it does not belong to.",
            variant="confront", axes={"gaze": "confront"},
            notes="The type reserves --confront for appearance and daily frustration rather "
                  "than physical pain; it is offered because the axis is the only legal second "
                  "dimension here, not because it fits better."),
        opt("C", "01-pain-scene", "execution: subject class — the delivery driver, not the "
            "commuter", "16:9", P_HERO_C,
            "Same type and same axis, different subject class: the professional driver from "
            "the brief's persona list, in a van cab on a lay-by. The action is the same push "
            "up out of a sloped seat.",
            variant="candid", axes={"gaze": "candid"}),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The slot's declared job is recognition — a cold reader seeing themselves in "
                  "a held state — and the push up off the seat is a single braced moment rather "
                  "than a transition the loop could carry. Pages 58, 65 and 73 all refused a "
                  "hero on the same ground; refused here for consistency with them.",
    },
})

SLOTS.append({
    "slot_id": "problems.items.0.image", "section_role": "problem-agitation",
    "asset": "77-02-problem0-pain-scene.png",
    "placement": "problem section 1, beside the what-I-already-tried list",
    "recommended_media": "gif",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides. The advertorial problem-agitation cell holds 01-pain-scene alone, and "
        "one-type-once has already spent it at the header — so this is Step 4 rung 4, another "
        "execution of a type already on the page, which the runbook's own worked precedent "
        "resolves the same way (object-only, two ledger observations). The section is a list of "
        "objects that failed, not a person suffering, and evidence rank 3 — the failed tool in "
        "the state that shows it failed — is exactly what the copy enumerates. B is a real "
        "second reading and is on-cell for a comparison role, but taking it spends "
        "04-proof-lockedframe here and forces features.items.2 off its own recommendation. C is "
        "the same object-only execution moved to the drawer they ended up in. PAGE LEGALITY: A "
        "keeps 04-proof-lockedframe free for features.items.2. PRODUCT PRESENCE: none, "
        "correctly — every object in frame is an alternative, not the product. PROMPT RISK: "
        "{chars} characters, inside the measured band.",
    "options": [
        opt("A", "01-pain-scene", "baseline — object-only, no person in frame", "16:9",
            P_PROB0_A,
            "The four fixes the copy names, left exactly where they ended up on the seat, with "
            "the gap they were meant to fill still open behind them. No person: the argument is "
            "against the objects.",
            variant="candid", axes={"gaze": "candid"},
            notes="COMBINATION: this option is what keeps 04-proof-lockedframe available for "
                  "features.items.2. Picking B here forces that slot to its own option B or C."),
        opt("B", "04-proof-lockedframe", "type: the three-alternatives comparison", "16:9",
            P_PROB0_B,
            "The same indictment as a locked-frame comparison instead of a scene: three common "
            "fixes on one chair across three days, none of them winning. The type's use_when "
            "names this beat verbatim — the I-tried-three-things beat of an advertorial.",
            variant="rivals",
            notes="COMBINATION: picking B here spends 04-proof-lockedframe on this slot and "
                  "forces features.items.2 to its option B or C. --rivals is advertorial and "
                  "paid-social only, which this page satisfies."),
        opt("C", "01-pain-scene", "execution: the drawer they ended up in, not the seat",
            "16:9", P_PROB0_C,
            "Same type and same object-only execution, different place and different evidence: "
            "the same four fixes months later in a desk drawer, each carrying the damage that "
            "retired it.",
            variant="candid", axes={"gaze": "candid"}),
    ],
    "gif": {
        "eligible": True, "form": "whole-frame", "kind": "cause", "type_id": "cause",
        "rung": "natural",
        "reason": "The declared reason this section exists is that the separate pieces shift, "
                  "separate and slide out of alignment every time he brakes. That is a state "
                  "changing, and a still can only assert it. The gif library's `cause` type "
                  "names this exact case in its own PURPOSE line — a pad creeping forward under "
                  "a body — and the product is correctly absent from the frame. No legislated "
                  "layer exists in this type's skeleton, so the form is whole-frame and the "
                  "plate is the delivered image.",
        "asset": "77-02-problem0-pain-scene--brief.png",
        "refs": "gifs-library/cause/ — no files filed yet; the folder card carries the law",
        "output": "77-02-problem0-pain-scene.mp4",
        "duration_s": 3, "loop": "seamless loop",
        "shot": "open car door, seat and pads",
        "action": "pads creep forward, gap opens",
        "result": "nothing was holding the pelvis",
        "match": "same overcast daylight and cabin",
        "delivery": "mp4/webm, muted, under the size ceiling",
        "prompt": PLATE_PROB0.strip(),
    },
})

SLOTS.append({
    "slot_id": "problems.items.1.image", "section_role": "cause",
    "asset": "77-03-problem1-cause-anatomy.png",
    "placement": "problem section 2, beside the root-cause list",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT and the removal test together. Take the backward-sloping seat out of the left "
        "panel and the rolled pelvis goes with it, so this is a switchable mechanism and not "
        "accumulated damage. The copy supplies the measurable landmark pair the type demands — "
        "hips dropping below knees — and the difference is well past the 2:1 the `measure` mark "
        "requires. A runs --diagnostic, which is what the advertorial middle asks for: indict "
        "the culprit here and let features.items.0 be where the product first appears. B is the "
        "base variant with the product in the right panel, which argues buy-this one section "
        "early. C moves the subject class from the whole seated figure to the sitting bones and "
        "trades `measure` for `pressure`, a mark working at 3 of 6. PAGE LEGALITY: "
        "02-cause-anatomy pairs_with 01-pain-scene and 03-mechanism-ghostbody, both on the "
        "page. PRODUCT PRESENCE: none under --diagnostic, and the variant makes "
        "requires_product_photo false. PROMPT RISK: {chars} characters against a measured ~1800 "
        "at two marks.",
    "options": [
        opt("A", "02-cause-anatomy", "baseline", "16:9", P_PROB1_A,
            "The seat is the culprit and the pelvis is the structure it acts on. Two panels, "
            "one figure, the hip-to-knee line as the measured difference, and the product held "
            "back until the mechanism section.",
            variant="diagnostic"),
        opt("B", "02-cause-anatomy", "variant: the product enters the right panel", "16:9",
            P_PROB1_B,
            "The same anatomy with the reference product drawn into the corrected panel. It "
            "resolves the argument here instead of at features.items.0, which is a real "
            "editorial choice rather than a better or worse one.",
            notes="Picking B puts the product in frame one section earlier than the page's own "
                  "copy reveals it, and makes this slot require the product photo."),
        opt("C", "02-cause-anatomy", "execution: subject class — the sitting bones, not the "
            "whole figure", "16:9", P_PROB1_C,
            "Same type and same variant, different subject class and a different mark: the load "
            "moving off the two sitting bones onto the tailbone, drawn as a contact region "
            "rather than a measured line.",
            variant="diagnostic"),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "A two-panel illustrated comparison is inspected rather than watched — the "
                  "reader holds both states side by side and reads the dashed lines against "
                  "each other. The library has measured 0 of 13 such slots earning a verdict. "
                  "The section's one permitted loop is also already spent at "
                  "problems.items.0.image, but the argument refuses this on its own grounds "
                  "before the budget reaches it.",
    },
})

SLOTS.append({
    "slot_id": "features.items.0.image", "section_role": "mechanism",
    "asset": "77-04-feature0-mechanism-ghostbody.png",
    "placement": "feature section 1, beside the what-makes-it-work list",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides against a ratio cost, and FIT wins. The section's whole sentence is that "
        "the one-piece contour bridges the void where the backrest meets the seat pan and stops "
        "the pelvis collapsing backward — a mechanism inside the body that cannot be filmed, "
        "which is 03-mechanism-ghostbody's use_when almost word for word, and body_contact is "
        "true so the gate opens. RATIO COST, stated rather than hidden: this type declares 1:1 "
        "and 4:5 and not the template's 16:9, so option A renders square and the layout crops "
        "it; the two panels sit side by side, so a centre-crop to 16:9 keeps both and loses "
        "head and foot room. B is native 16:9 and costs the argument instead — it shows that "
        "the product works, not why. 03-mechanism-xray is NOT offered: its avoid_when bars a "
        "trivial interior, and a block of foam is one. PAGE LEGALITY: A is the page's only "
        "step-3 type, well inside the budget of two. PRODUCT PRESENCE: right panel only, with "
        "a real material finish and no signal colour on it. PROMPT RISK: {chars} characters "
        "against a measured 2056-2916.",
    "options": [
        opt("A", "03-mechanism-ghostbody", "baseline", "1:1", P_FEAT0_A,
            "Two panels of the same cross-sectioned mannequin in the same sloped seat, "
            "differing only in whether the product is there. Red stress on the sacrum where the "
            "load collects, blue support beside the lumbar spine where the contour carries it.",
            notes="RATIO: renders at 1:1, the type's own declared ratio; the 16:9 template slot "
                  "crops it. Both panels survive a centre-crop, head and foot room do not."),
        opt("B", "06-relief-hero", "type: the same claim as a scene with a wrong-vs-right "
            "inset", "16:9", P_FEAT0_B,
            "Step 4 rung 2, an adjacent step: the mechanism argued photographically instead of "
            "anatomically, with the failed two-piece setup and the one-piece product held "
            "against each other in a split inset. Native 16:9, so nothing is cropped.",
            variant="vsinset", axes={"register": "commercial", "inset_mode": "vsinset"},
            notes="COMBINATION: 06-relief-hero is the recommendation at features.items.1. "
                  "Picking B here forces that slot to its own option B or C."),
        opt("C", "03-mechanism-ghostbody", "execution: subject class — the lumbar discs, not "
            "the pelvis", "1:1", P_FEAT0_C,
            "Same type and same marks, a different structure under argument: the lowest discs "
            "pinched closed by the reversed curve, then held open. Answers the copy's spinal-fit "
            "line rather than its bridging line.",
            notes="RATIO: renders at 1:1 for the same reason as option A."),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "Two technical panels are inspected rather than watched, the same reading the "
                  "library has measured 0 of 13 times. A re-execution at rung 2 would have to "
                  "show the product arriving under the pelvis, which argues the fitting rather "
                  "than the mechanism and is a different claim. The `features` list is also ONE "
                  "section under ADR-024 and its single loop is spent at features.items.2.",
    },
})

SLOTS.append({
    "slot_id": "features.items.1.image", "section_role": "proof",
    "asset": "77-05-feature1-relief-hero.png",
    "placement": "feature section 2, beside the why-it-stays-put list",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT against an exhausted cell. The advertorial proof cell holds 04-proof-lockedframe "
        "alone and the recommended set spends it at features.items.2, so this is Step 4 rung 2, "
        "an adjacent step. 06-relief-hero's use_when asks for one image that proves wrong "
        "against right, shows the product and sells the relief state, and --vsinset is the "
        "inset mode the type names for a wrong-vs-right argument — which is what this section "
        "is: the old pad slid forward and the roll fell down the crack, this one did neither. "
        "B is on-cell and is the stronger evidentiary form, but it spends the type this page "
        "needs at features.items.2 for a comparison the copy makes more sharply. C is the same "
        "argument moved to a desk chair. EVIDENCE: 06-relief-hero is the most-rendered type in "
        "the library at 22; `vs` renders 2 of 2 once the letters are named, `hotspot` is thin "
        "at 1 of 2 and is anchored to three named places rather than given a count. PRODUCT "
        "PRESENCE: in the hero and in the right half of the inset, one mode of use throughout. "
        "PROMPT RISK: {chars} characters; this type is multi-layer and runs long by design.",
    "options": [
        opt("A", "06-relief-hero", "baseline", "16:9", P_FEAT1_A,
            "The product doing its job in the car, with the wrong state confined to a split "
            "inset: the pad crept to the front lip and the roll gone down the crack on the "
            "left, the product unmoved on the right.",
            variant="vsinset",
            axes={"register": "commercial", "inset_mode": "vsinset", "inset_motion": "still"}),
        opt("B", "04-proof-lockedframe", "type: the same object across one working week",
            "16:9", P_FEAT1_B,
            "The on-cell proof type in the variant the gate mandates: sliding cannot be shown "
            "inside a static frame, so the variable becomes the condition of one object over "
            "time rather than which product is on the seat.",
            variant="timelapse",
            notes="COMBINATION: picking B spends 04-proof-lockedframe here and forces "
                  "features.items.2 to its option B or C."),
        opt("C", "06-relief-hero", "execution: the desk chair, not the car seat", "16:9",
            P_FEAT1_C,
            "Same type, same inset mode, the other half of the copy's claim — the cushion that "
            "moves between the car and the office chair, shown in the office.",
            variant="vsinset",
            axes={"register": "commercial", "inset_mode": "vsinset", "inset_motion": "still"}),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The argument is genuinely temporal — a pad that creeps forward against one "
                  "that does not — and on its own this slot would earn a loop at rung 1. It is "
                  "refused by the budget and not by the argument: the `features` list counts as "
                  "ONE section under ADR-024, and its single permitted loop goes to "
                  "features.items.2, where the motion carries a claim no still can make at all. "
                  "Recorded in motion.notes.",
    },
})

SLOTS.append({
    "slot_id": "features.items.2.image", "section_role": "comparison",
    "asset": "77-06-feature2-proof-lockedframe.png",
    "placement": "feature section 3, beside the why-it-lasts list",
    "recommended_media": "gif",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides on the type's own core condition. 04-proof-lockedframe may only be used "
        "where the difference is visible to the naked eye inside a static frame, and the copy's "
        "claim is exactly that — cheap foam flattens out like paper after twenty minutes, this "
        "core holds its shape. A flattened pad against a standing contour is visible without "
        "anything being explained. A takes --verdict, whose order rule puts the product last "
        "where left-to-right reading resolves. B drops the product for --rivals, which indicts "
        "the alternatives but makes no claim for the cushion and duplicates the work "
        "problems.items.0 already does. C is the same comparison on an office chair. "
        "CAPABILITY: `strict` needs compositing, so the panels run `handheld` with --verdict "
        "included, exactly as the type's own capability gate says (ADR-021). PAGE LEGALITY: "
        "04-proof-lockedframe pairs_with 02-cause-anatomy, 06-relief-hero and 01-pain-scene, "
        "all three on the page. PROMPT RISK: {chars} characters against a 1800 ceiling.",
    "options": [
        opt("A", "04-proof-lockedframe", "baseline", "16:9", P_FEAT2_A,
            "One seat, one framing, three days, and the only variable is which cushion took the "
            "day's sitting. The two alternatives are the most common ones buyers already own "
            "and get exactly the same photographic respect as the product.",
            variant="verdict"),
        opt("B", "04-proof-lockedframe", "variant: the product leaves the frame", "16:9",
            P_FEAT2_B,
            "The same locked frame with three alternatives and no product, making no claim at "
            "all. Honest and it fits the section's first sentence, but it argues what fails "
            "rather than what lasts.",
            variant="rivals",
            notes="COMBINATION: --rivals is also option B at problems.items.0. Running both "
                  "would put two rival comparisons on one page arguing the same thing."),
        opt("C", "04-proof-lockedframe", "execution: the office chair, not the car seat",
            "16:9", P_FEAT2_C,
            "Same type and variant, different scene and a different pair of alternatives: the "
            "desk-chair half of the copy's universal-fit claim, with a memory foam wedge in "
            "place of the doughnut ring.",
            variant="verdict"),
    ],
    "gif": {
        "eligible": True, "form": "whole-frame", "kind": "proof", "type_id": "proof",
        "rung": "re-execution",
        "reason": "The still is a locked multi-panel comparison, and panels are inspected "
                  "rather than watched — as a three-panel frame this slot earns no motion. The "
                  "claim itself is temporal, though: slow-rebound foam recovering after the "
                  "weight comes off is a state changing that no static frame can show. The move "
                  "is the one Step 5d names as rung 2 — drop the panels and put one continuous "
                  "frame in which one variable changes, the same claim restaged. The job does "
                  "not change: it is still proof, and the viewer still judges the change.",
        "asset": "77-06-feature2-proof-lockedframe--brief.png",
        "refs": "gifs-library/proof/ — no files filed yet; the folder card carries the law",
        "output": "77-06-feature2-proof-lockedframe.mp4",
        "duration_s": 3, "loop": "seamless loop",
        "shot": "one seat, cushion filling frame",
        "action": "weight lifts, the contour returns",
        "result": "it did not stay squashed",
        "match": "same seat and daylight as still",
        "delivery": "mp4/webm, muted, under the size ceiling",
        "prompt": PLATE_FEAT2.strip(),
    },
})

SLOTS.append({
    "slot_id": "features.items.3.image", "section_role": "outcome",
    "asset": "77-07-feature3-relief-scene.png",
    "placement": "feature section 4, beside the what-changed list",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides, and the requires_pair is already paid for. 06-relief-scene closes an "
        "advertorial when the promise is a state of living rather than a feature, and this "
        "section is Sandra, the coastal drive they had put off, and stepping out of the car "
        "loose and upright. Its requires_pair is 01-pain-scene, which is at the header on the "
        "same man. The relief situation is chosen from what the problem forbade: A stages the "
        "exact inverse of the hero — the moment he braced against is the moment he now "
        "straightens up through. B closes with 06-relief-hero instead, product-forward and "
        "composed; that is the right close when the result is invisible, and here it is not. C "
        "moves the cost from a long drive to a lifted crate. PAGE LEGALITY: A is the page's "
        "second step-6 type and the arc holds, with no pain image after the first relief image. "
        "PRODUCT PRESENCE: standalone class — it stands on the seat through the open door as "
        "its own object, near the camera and turned so it can be read. PROMPT RISK: "
        "{chars} characters.",
    "options": [
        opt("A", "06-relief-scene", "baseline", "16:9", P_FEAT3_A,
            "The release and the return in one frame: straightening up out of the driver's seat "
            "at the end of the drive, weight even, hands empty, the smile arriving on its own "
            "while he looks at the water.",
            axes={"gaze": "candid"}),
        opt("B", "06-relief-hero", "type: the composed close instead of the candid one",
            "16:9", P_FEAT3_B,
            "The other type in the advertorial outcome cell. It presents the product in the "
            "resolved scene rather than letting the body carry the whole argument, and it is "
            "the safer close if the release does not read.",
            axes={"register": "commercial", "inset_mode": "none"},
            notes="COMBINATION: 06-relief-hero is the recommendation at features.items.1. "
                  "Picking B here forces that slot to its own option B or C."),
        opt("C", "06-relief-scene", "execution: the depot apron, not the coast", "16:9",
            P_FEAT3_C,
            "Same type and same axis, a different situation with a different cost: lifting a "
            "crate onto his shoulder at work, which is the other thing the copy says the ache "
            "used to take.",
            axes={"gaze": "candid"}),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The still argues a STATE — a body that has stopped defending itself — and a "
                  "state is not a transition. A loop of the standing-up would be a different "
                  "execution of the section and would land on the gif library's `relief` type, "
                  "whose rule is that motion is earned only where the motion IS the thing the "
                  "problem used to block; standing up out of a car seat would qualify. It is "
                  "refused by the budget: the `features` list is ONE section (ADR-024) and its "
                  "single loop is at features.items.2. Recorded in motion.notes as the strongest "
                  "candidate this page could not spend.",
    },
})

for i, (prompt, varies) in enumerate([
    (P_REV_1, "in-use · car driver seat · cool early daylight · seated arm's length"),
    (P_REV_2, "at-rest · home office swivel chair · warm lamp light · standing above"),
    (P_REV_3, "in-use · truck cab bench · flat overcast daylight · close over the shoulder"),
    (P_REV_4, "kit-flatlay · kitchen worktop · mixed warm and cool · half a metre back"),
]):
    SLOTS.append({
        "slot_id": f"reviews.shots.{i}.image", "section_role": "social-proof",
        "asset": f"77-{8 + i:02d}-review-{i + 1}.png",
        "placement": f"review grid tile {i + 1} of 4",
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis":
            "One option by law (ADR-022): the four tiles are the unit of variation, not the "
            "tile, and this one's place in the set is its varies_on line. 05-social-snapshot is "
            "the advertorial social-proof type whose trust gap is whether the thing exists and "
            "works in a normal home, which is what the review copy claims. The SET DIVERSITY "
            "LAW is satisfied across the four: four room classes, four surfaces, four light "
            "temperatures, four camera distances and three of the type's three content modes.",
        "options": [
            opt("A", "05-social-snapshot", varies, "1:1", prompt,
                "One tile of the four-tile set, differing from its siblings on room class, "
                "surface, light temperature, camera distance and content mode.",
                axes={"register": "ugc"}, notes=WALL_FENCE),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "No social-proof slot carries motion. The mechanism is wider than the "
                      "review wall and it is what a router actually hits: the six-type gif set "
                      "carries no `social` type, so a social-proof slot has nothing to file a "
                      "loop under, wall tile or standalone (ADR-024).",
        },
    })

# Measured figures come from the prompts themselves at build time. Typed by hand they
# were wrong in 7 of 7 places, which is why the placeholder exists at all.
for _s in SLOTS:
    if not _s.get("options"):
        continue
    _rec = next(o for o in _s["options"] if o["opt"] == _s["recommended_opt"])
    _s["recommendation_basis"] = _s["recommendation_basis"].replace(
        "{chars}", str(len(_rec["prompt"])))

# ---------------------------------------------------------------- out of scope

OUT_OF_SCOPE = [
    ("features.items.4.image", "feature section 5, the price comparison", "cta"),
    ("product.image", "mid-page product overview card", "cta"),
    ("product_end.image", "closing offer card, above the final CTA", "cta"),
    ("hero.author_avatar", "byline avatar beside the author name", "author"),
    ("guide.avatar", "About the author card", "author"),
] + [(f"comments.items.{i}.avatar", f"comment thread, commenter {i + 1}", "author")
     for i in range(6)]

PRICE_REASON = (
    "A cta cell: the section's whole argument is price — ergonomic chairs against custom "
    "re-upholstery against recurring clinic fees — and every one of those comparisons is "
    "carried by a number. G6 bans text in frame, so the image would have to state the claim "
    "without the figures that ARE the claim. Page 37 refused the same section on this page's "
    "own product for the same reason.")
SHOT_REASON = (
    "A standard product shot. The library covers argument images, not the offer card's "
    "packshot (mapping/slot-rules.md, the cta row is empty on every channel).")
AUTHOR_REASON = (
    "A portrait of a named person. No library type produces one, and generating a face to sit "
    "under a real byline or a named comment is a disclosure decision rather than an image one "
    "(mapping/slot-rules.md, the author row is empty on every channel by design).")

for sid, place, role in OUT_OF_SCOPE:
    reason = AUTHOR_REASON if role == "author" else (
        PRICE_REASON if sid == "features.items.4.image" else SHOT_REASON)
    SLOTS.append({
        "slot_id": sid, "section_role": role, "asset": None, "placement": place,
        "out_of_scope_reason": reason, "options": [],
        "gif": {"eligible": False, "form": "none",
                "reason": "No generated image in this slot to animate."},
    })

# ---------------------------------------------------------------- page blocks

MOTION = {
    "floor": 2,
    "ceiling": 5,
    "delivered": 2,
    "groups_covered": ["result", "working"],
    "shortfall_reason": None,
    "notes": [
        "Floor met at exactly 2, and the coverage pair IS met — one `working` loop (cause at "
        "problems.items.0) and one `result` loop (proof at features.items.2). ADR-024 measured "
        "the pair as met on only 2 of 5 earlier pages, so this is the exception rather than "
        "the rule, and it is met because the page argues the culprit and the recovery in two "
        "different sections.",
        "The `result` loop is a rung-2 re-execution, not a rung-1 verdict — exactly the case "
        "ADR-024 said is closer to a default than to a backup. Its still is a three-panel "
        "locked comparison that correctly earns no motion; one continuous frame of the foam "
        "recovering earns it on the same claim.",
        "SPACING COST, stated rather than hidden: the `features` list counts as ONE section "
        "(ADR-024), so features.items.1 loses a loop it would otherwise have earned at rung 1 "
        "on its own argument — a pad that creeps forward against one that does not. Its "
        "verdict says budget, not argument.",
        "features.items.3 is the strongest candidate this page could not spend. Standing up "
        "out of a car seat freely is precisely the gif library's `relief` rule — motion earned "
        "only where the motion IS the thing the problem used to block — and it would have been "
        "that rule's first real test. The same one-loop-per-section rule refuses it.",
        "Review wall: 0 tiles, and not by budget — the six-type gif set carries no `social` "
        "type, so those slots have nothing to file a loop under.",
        "Both loops are whole-frame. No type on this page legislates an inset layer that a "
        "plate could occupy at a slot that earned motion, so `inset` was never available.",
    ],
}

COVERAGE = {
    "covered": [
        "step 1 pain — 01-pain-scene at hero.image, and again object-only at "
        "problems.items.0.image",
        "step 2 cause — 02-cause-anatomy --diagnostic at problems.items.1.image",
        "step 3 mechanism — 03-mechanism-ghostbody at features.items.0.image",
        "step 4 proof — 04-proof-lockedframe --verdict at features.items.2.image, with "
        "06-relief-hero --vsinset carrying the proof role at features.items.1.image",
        "step 5 social — 05-social-snapshot across all four review tiles",
        "step 6 relief — 06-relief-scene at features.items.3.image",
    ],
    "absent": [
        "step 2 symptom breadth — 02-symptom-rail declares no advertorial channel, so the "
        "breadth beat has no type here; the page makes no breadth claim either, so this is not "
        "a gap",
        "step 5 personas — 05-persona-grid declares no advertorial channel. The brief lists "
        "five distinct personas and the page never shows them, which IS a gap, but no type on "
        "this channel can fill it",
    ],
    "notes": [
        "Awareness stage read from the page's own copy, not from a declared field: "
        "SOLUTION-AWARE, and the brief agrees. The reader is assumed to have already bought "
        "flat pads, donut rings and lumbar rolls — the problems section is written as a list "
        "of things they have already tried, not as an explanation of what hurts.",
        "Every rung of the Trust Ladder is covered. That is a property of the page rather than "
        "of the routing: a two-problem, five-feature advertorial with a review wall reaches "
        "further down the ladder than most.",
        "One-type-once is breached once, deliberately and under Step 4 rung 4: 01-pain-scene "
        "runs twice, at the header as a person and at problems.items.0 object-only. The "
        "runbook's own worked precedent resolves this exact collision the same way, and the "
        "ledger carries two observations of the object-only execution.",
    ],
}

PAGE_NOTES = [
    "SOURCE: ~/Downloads/landing-page-how-i-fixed-years-of-lower-back-and-tailbone-agony-on-"
    "long-drives.json, page id 77, template TPL-ADV08. The compiled HTML is the authoritative "
    "slot list and it carries two things imageBriefs does not: the template's aspect ratio per "
    "slot, and eight avatar slots imageBriefs omits entirely.",
    "The placeholder captions inside htmlCompiled ('Halden blanket', 'Glass bead fill', "
    "'Weight chart') are stale template samples from a weighted-blanket page and were "
    "disregarded. The compiled body copy is this product throughout — tailbone 8, lumbar 7, "
    "cushion 19, seat 29 mentions against 2 for blanket, both of them inside placeholder URLs.",
    "TEMPLATE RATIO: nine body slots at 16:9 and four review tiles at 1:1. Seven of the nine "
    "advertorial-legal types declare 16:9, so this template costs the library far less than "
    "the 4:3 listicle template does. The single casualty is 03-mechanism-ghostbody, which "
    "declares 1:1 and 4:5 only; its options say what the crop costs.",
    "03-mechanism-xray was not offered at any slot. Its avoid_when bars a trivial interior — a "
    "shell with nothing meaningful inside — and a block of moulded foam is exactly that. "
    "Refusing a wrong type is not the same as emitting an empty slot.",
    "03-use-sequence is gated out by multi_step_usage: false. Nobody assumes a seat cushion is "
    "complicated to fit, so the gate's own escape clause does not apply.",
    "ADR-021 capability: every option is single-pass. 04-proof-lockedframe runs `handheld` "
    "rather than `strict` at both slots that use it, because `strict` needs compositing, which "
    "this pipeline does not do.",
    "PENDING, and it affects both plate prompts: the owner asked on 2026-08-19 for the motion "
    "brief plate to be cut to four fields — a filename carrying the gif type, duration, ratio "
    "and one prose brief. That change is not law yet; G12 still legislates the five-line card, "
    "so both plates here are emitted in the current form and will need regenerating if the "
    "change lands.",
]

OUT = {
    "page_id": PAGE,
    "registry_version": "2.0.0",
    "channel": "advertorial",
    "awareness_stage": "solution-aware",
    "slots": SLOTS,
    "coverage": COVERAGE,
    "recommended": [],
    "motion": MOTION,
    "page_composition_notes": PAGE_NOTES,
}

# ---------------------------------------------------------------- self-checks


def checks():
    errs, warns = [], []
    routed = [s for s in SLOTS if s.get("options")]

    declared_ids = set(DECLARED)
    emitted_ids = {s["slot_id"] for s in SLOTS}
    for missing in sorted(declared_ids - emitted_ids):
        errs.append(f"{missing}: declared in content.json but not emitted")
    for extra in sorted(emitted_ids - declared_ids):
        errs.append(f"{extra}: emitted but not in content.json")

    for s in SLOTS:
        sid = s["slot_id"]
        if sid not in DECLARED:
            continue
        if s["section_role"] != DECLARED[sid]["role"]:
            errs.append(f"{sid}: role {s['section_role']} != contract "
                        f"{DECLARED[sid]['role']}")
        for o in s.get("options", []):
            if o["pipeline"] != "single-pass":
                errs.append(f"{sid} {o['opt']}: pipeline is not single-pass (ADR-021)")
            declared = TYPES[o["type"]].get("ratios", "")
            if o["ratio"] not in declared:
                errs.append(f"{sid} {o['opt']}: ratio {o['ratio']} not declared by "
                            f"{o['type']} ({declared})")
            if o["ratio"] != DECLARED[sid]["ratio"] and "RATIO" not in \
                    (o.get("composition_notes") or ""):
                errs.append(f"{sid} {o['opt']}: renders at {o['ratio']} into a "
                            f"{DECLARED[sid]['ratio']} slot with no stated crop cost")
            chans = TYPES[o["type"]].get("channels", "")
            if "advertorial" not in chans:
                errs.append(f"{sid} {o['opt']}: {o['type']} is not advertorial-legal")
            needs_photo = TYPES[o["type"]].get("requires_product_photo") is True
            exempt = o.get("variant") in ("rivals", "diagnostic")
            if needs_photo and not exempt and "the exact reference" not in o["prompt"]:
                errs.append(f"{sid} {o['opt']}: {o['type']} requires a product photo but the "
                            "prompt carries no reference block")
            if not needs_photo and "the exact reference" in o["prompt"]:
                errs.append(f"{sid} {o['opt']}: {o['type']} takes no product photo but the "
                            "prompt carries a reference block")

    # attribute gates
    for cond, tid, why in ATTRIBUTE_GATES:
        if cond(ATTRS):
            for s in routed:
                for o in s["options"]:
                    if o["type"] == tid:
                        errs.append(f"{s['slot_id']} {o['opt']}: {why}")

    # one-type-once across the RECOMMENDED set, linear slots only
    linear = [s for s in routed if not s["slot_id"].startswith("reviews.")]
    picked = [next(o for o in s["options"] if o["opt"] == s["recommended_opt"])["type"]
              for s in linear]
    RUNG4 = {"01-pain-scene"}  # Step 4 rung 4, declared in coverage.notes
    dupes = {t for t in picked if picked.count(t) > 1}
    for t in sorted(dupes - RUNG4):
        errs.append(f"one-type-once breached in the recommended set: {t}")
    for t in sorted(dupes & RUNG4):
        warns.append(f"{t} runs twice under Step 4 rung 4 — declared in coverage.notes")

    # step-3 budget
    step3 = {"03-mechanism-ghostbody", "03-spec-split", "03-use-sequence"}
    n3 = len([t for t in picked if t in step3])
    if n3 > 2:
        errs.append(f"step-3 budget: {n3} of the capped three types, max 2")

    # requires_pair and never_with
    for s in linear:
        for o in s["options"]:
            rp = TYPES[o["type"]].get("requires_pair")
            if rp and rp != "null" and rp not in picked:
                errs.append(f"{s['slot_id']} {o['opt']}: requires_pair {rp} not on the page")
    for t in picked:
        nw = TYPES[t].get("never_with", "")
        for other in picked:
            if other != t and other in nw:
                errs.append(f"never_with breached: {t} and {other}")

    # page arc: no pain type after the first relief type
    order = [s["slot_id"] for s in linear]
    relief_at = [i for i, t in enumerate(picked) if t.startswith("06-")]
    pain_at = [i for i, t in enumerate(picked) if t.startswith("01-")]
    if relief_at and pain_at and max(pain_at) > min(relief_at):
        errs.append(f"page arc: a pain type at {order[max(pain_at)]} follows the first "
                    f"relief type at {order[min(relief_at)]}")

    # motion budget, recomputed rather than trusted
    elig = [s for s in SLOTS if s.get("gif", {}).get("eligible")]
    if len(elig) != MOTION["delivered"]:
        errs.append(f"motion.delivered says {MOTION['delivered']}, {len(elig)} slots eligible")
    if len(elig) < MOTION["floor"] and not MOTION["shortfall_reason"]:
        errs.append("below the motion floor with no shortfall_reason")
    if len(elig) > MOTION["ceiling"]:
        errs.append(f"motion ceiling {MOTION['ceiling']} exceeded: {len(elig)}")

    secs = {}
    for s in elig:
        secs.setdefault(s["slot_id"].split(".")[0], []).append(s["slot_id"])
    for sec, ids in secs.items():
        if len(ids) > 1:
            errs.append(f"more than one loop in section `{sec}` (ADR-024): {ids}")

    GROUP = {"use": "working", "mechanism": "working", "cause": "working",
             "proof": "result", "relief": "result"}
    got = sorted({GROUP[s["gif"]["type_id"]] for s in elig})
    if got != MOTION["groups_covered"]:
        errs.append(f"motion.groups_covered says {MOTION['groups_covered']}, computed {got}")
    if got != ["result", "working"]:
        warns.append(f"coverage pair not met (groups: {got}) — allowed, and stated in "
                     "motion.notes")

    for s in elig:
        g = s["gif"]
        if g["form"] == "whole-frame" and "flat" not in g["prompt"].lower():
            errs.append(f"{s['slot_id']}: whole-frame plate prompt is not a flat card")
        if not g["asset"].endswith("--brief.png"):
            errs.append(f"{s['slot_id']}: plate asset must carry the --brief suffix (G12)")
        if g["asset"] == s["asset"]:
            errs.append(f"{s['slot_id']}: plate asset must not be the slot's own asset")
        if g["output"] != s["asset"].replace(".png", ".mp4"):
            errs.append(f"{s['slot_id']}: gif.output must be the slot asset with an mp4 "
                        f"extension (got {g['output']})")
        for line in ("shot", "action", "result", "match"):
            if len(g[line].split()) > 7:
                errs.append(f"{s['slot_id']}: brief line `{line}` is over seven words (G12)")
        for line in ("shot", "action", "result", "match"):
            if g[line] not in g["prompt"]:
                errs.append(f"{s['slot_id']}: brief line `{line}` is not drawn into the plate")

    # every slot carries a gif verdict, positive or negative (Step 5c)
    for s in SLOTS:
        if "gif" not in s or "reason" not in s["gif"]:
            errs.append(f"{s['slot_id']}: no gif verdict (Step 5c requires one either way)")
    for s in SLOTS:
        if s["section_role"] == "social-proof" and s.get("gif", {}).get("eligible"):
            errs.append(f"{s['slot_id']}: a social-proof slot carries motion (Step 5d)")

    # review wall: one option each, and the SET DIVERSITY LAW
    wall = [s for s in SLOTS if s["slot_id"].startswith("reviews.")]
    for s in wall:
        if len(s["options"]) != 1:
            errs.append(f"{s['slot_id']}: repeating section must emit one option (ADR-022)")
        if "PRECONDITION" not in (s["options"][0].get("composition_notes") or ""):
            errs.append(f"{s['slot_id']}: the authenticity fence is breached on this page and "
                        "the option carries no precondition")
    axes_seen = {"mode": [], "room": [], "light": [], "distance": []}
    for s in wall:
        parts = [p.strip() for p in s["options"][0]["varies_on"].split("·")]
        if len(parts) != 4:
            errs.append(f"{s['slot_id']}: varies_on must name mode, room, light and distance")
            continue
        for key, val in zip(("mode", "room", "light", "distance"), parts):
            axes_seen[key].append(val)
    for name in ("room", "light", "distance"):
        vals = axes_seen[name]
        if len(set(vals)) != len(vals):
            errs.append(f"SET DIVERSITY: repeated {name} across the wall: {vals}")
    if len(set(axes_seen["mode"])) < 3:
        warns.append(f"SET DIVERSITY: only {len(set(axes_seen['mode']))} content modes across "
                     "four tiles")

    # measured figures are generated, never typed (a typed count was wrong 7 of 7)
    for s in routed:
        b = s["recommendation_basis"]
        if "{chars}" in b:
            errs.append(f"{s['slot_id']}: recommendation_basis still carries the "
                        "{chars} placeholder")
        m = re.search(r"PROMPT RISK: (\d+) characters", b)
        if m:
            rec = next(o for o in s["options"] if o["opt"] == s["recommended_opt"])
            if int(m.group(1)) != len(rec["prompt"]):
                errs.append(f"{s['slot_id']}: recommendation_basis claims "
                            f"{m.group(1)} characters, the prompt is {len(rec['prompt'])}")

    # out-of-scope slots carry a reason and no options
    for s in SLOTS:
        if not s.get("options") and not s.get("out_of_scope_reason"):
            errs.append(f"{s['slot_id']}: no options and no out_of_scope_reason (SPEC 7.4)")

    return errs, warns


# ---------------------------------------------------------------- emit

def render_md():
    """The human view, and it has exactly one reader — nothing in the repo parses this
    file; scripts/validate.py reads prompts.json alone. So it carries what a person acts
    on at the place they act on it, and nothing else. Everything omitted here is in
    prompts.json, which is the contract and stays complete: the eleven out-of-scope
    reasons, the nine negative gif verdicts, the routing rationale and the page notes."""
    L = []
    routed = [s for s in SLOTS if s.get("options")]
    n_opts = sum(len(s["options"]) for s in routed)
    n_gif = len([s for s in SLOTS if s.get("gif", {}).get("eligible")])
    n_block = len([s for s in routed for o in s["options"]
                   if "PRECONDITION" in (o.get("composition_notes") or "")])
    L.append("# Image prompts — page 77, ergonomic memory foam seat cushion")
    L.append("")
    L.append("GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit "
             "the script and re-run. Routing rationale, the negative motion verdicts and the "
             "out-of-scope slots are all in `prompts.json`.")
    L.append("")
    L.append(f"- page `{PAGE}` · advertorial · solution-aware · registry `2.0.0` · "
             f"{len(routed)} routed slots · {n_opts + n_gif} prompts")
    L.append(f"- motion: {MOTION['delivered']} of {len(routed)} slots earn a loop "
             f"(floor {MOTION['floor']}, ceiling {MOTION['ceiling']}), "
             f"groups {', '.join(MOTION['groups_covered'])}")
    if n_block:
        L.append(f"- **{n_block} prompts carry a blocking precondition**, stated on each — "
                 "do not render those until it is resolved")
    L.append("")
    L.append("---")
    L.append("")
    for s in routed:
        L.append(f"## `{s['slot_id']}` — {s['section_role']}")
        L.append("")
        L.append(f"- asset `{s['asset']}` · {s['placement']}")
        L.append(f"- recommended: **option {s['recommended_opt']}** · media "
                 f"**{s['recommended_media']}**")
        L.append(f"- {s['recommendation_basis']}")
        L.append("")
        for o in s["options"]:
            head = f"### {s['slot_id']} · option {o['opt']} — `{o['type']}`"
            if o.get("variant"):
                head += f" `--{o['variant']}`"
            L.append(head)
            L.append("")
            L.append(f"- varies on: {o['varies_on']}")
            line = f"- ratio `{o['ratio']}` · type version `{o['type_version']}`"
            if TYPES[o["type"]].get("requires_product_photo") is True \
                    and o.get("variant") not in ("rivals", "diagnostic"):
                line += " · upload the product photo"
            if o.get("axes"):
                line += " · " + ", ".join(f"`{k}: {v}`" for k, v in o["axes"].items())
            L.append(line)
            L.append(f"- {o['rationale']}")
            if o.get("composition_notes"):
                L.append(f"- **note:** {o['composition_notes']}")
            L.append("")
            L.append("```")
            L.append(o["prompt"])
            L.append("```")
            L.append("")
        g = s.get("gif") or {}
        if g.get("eligible"):
            L.append(f"### {s['slot_id']} · option D — the motion brief plate")
            L.append("")
            L.append(f"- gif type `{g['type_id']}` · form `{g['form']}` · rung `{g['rung']}`")
            L.append(f"- reference folder: {g['refs']}")
            L.append(f"- **the editor returns** `{g['output']}` · {g['delivery']}")
            L.append(f"- plate render asset `{g['asset']}` — production only, never a page "
                     "asset")
            L.append("")
            L.append("```")
            L.append(g["prompt"])
            L.append("```")
            L.append("")
    return "\n".join(L)


def main():
    errs, warns = checks()
    with open(os.path.join(HERE, "prompts.json"), "w", encoding="utf-8") as f:
        json.dump(OUT, f, indent=2, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(HERE, "prompts.md"), "w", encoding="utf-8") as f:
        f.write(render_md())
    routed = [s for s in SLOTS if s.get("options")]
    n = sum(len(s["options"]) for s in routed) + \
        len([s for s in SLOTS if s.get("gif", {}).get("eligible")])
    for w in warns:
        print(f"WARN  {w}")
    for e in errs:
        print(f"ERROR {e}")
    print(f"page {PAGE}: {len(SLOTS)} slots, {len(routed)} routed, {n} prompts, "
          f"{len(errs)} errors, {len(warns)} warnings")
    return 1 if errs else 0


if __name__ == "__main__":
    raise SystemExit(main())

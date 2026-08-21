#!/usr/bin/env python3
"""Build prompts.json and prompts.md for page 120 — ergonomic memory foam seat cushion.

Fifth page of this product, third template. First page routed under the ADR-034
naming, the ADR-035 content contract and the ADR-036/037 loop names.

prompts.json is the source of truth (query/output.schema.json); prompts.md is
generated from it and is never hand-edited (query/runbook.md Step 7).
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAGE = "120"


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
                    v = v[1:-1]
                out[tid][k] = {"true": True, "false": False}.get(v, v)
    return out


TYPES = _index_types()
CONTRACT = json.load(open(os.path.join(HERE, "content.json"), encoding="utf-8"))
ATTRS = CONTRACT["product"]["attributes"]
DECLARED = {sl["slot_id"]: {"ratio": sl["ratio"], "role": sec["role"]}
            for sec in CONTRACT["page"]["sections"]
            for sl in sec["image_slots"]}
SECTION_ITEMS = {}
for _sid in DECLARED:
    _k = _sid.split(".")[0]
    SECTION_ITEMS[_k] = SECTION_ITEMS.get(_k, 0) + 1


# ADR-036: a loop's filename is this session's own directory name with the gif type
# inserted and the slot appended. Derived, never typed — the assert below is what
# stops the two drifting apart.
PAGE_TYPE, PRODUCT_SLUG, VERSION = 'advertorial', 'seat-cushion-l-shaped', 'v05'
assert os.path.basename(HERE) == f"{PAGE_TYPE}-{PRODUCT_SLUG}-{VERSION}", \
    "session directory does not match the parts the gif names are built from"


def gif_name(gif_type):
    """The only name a loop has, page-side and library-side alike (ADR-037).

    No slot and no sequence, which is why a page carries at most one loop of each
    gif type — the check below is what keeps that true rather than hoped for.
    """
    return f"{PAGE_TYPE}-{gif_type}-{PRODUCT_SLUG}-{VERSION}.webp"

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
        "product visualization", "cut-open product", "cross-section",
        "product standing upright unnaturally", "staged arrangement"],
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
        "invented spray or mist", "fake steam"],
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

A man in his mid-forties in a work shirt with the collar open, still in the driver's seat of his car in a half-empty supermarket car park, mid-way through levering himself up off the seat with one forearm braced flat along the top of the open door frame. Under that force: that elbow rigid and taking his whole weight, the other hand pushed down into the seat beside him, hips barely clear of the cushion, his back held in one unbending piece. Face: eyes shut, jaw clamped, breath held.

His hips sit well below his knees in the backward-sloping seat, his lower back is pressed flat against the seat back with an open gap behind it, and the whole load has gone onto the base of his spine.

One specific place: a supermarket car park on a cold evening with half the bays empty, the driver's door standing wide, and the lived-in clutter of the commute — a lanyard hung on the indicator stalk, a cold coffee in the holder, a folded hi-vis on the passenger seat, a parking permit clipped to the visor.

He is unaware of the camera. Key light: the last cold blue daylight across the tarmac. Fill: the weak dome light above him. A rim of light along his braced forearm. Deep shadow across the near third of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_HERO_B = """A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his mid-forties in a work shirt with the collar open, standing beside his own rear tire in a supermarket car park with one hand pushed into the small of his back, turned towards the camera and holding its eye. Under that force: his weight thrown onto one hip, the other heel lifted clear of the tarmac, his free hand hanging heavy at his side, shoulders uneven. Face: brow raised and tight, mouth pressed thin, looking directly into the lens.

He cannot straighten fully: his trunk stays folded a few degrees forward of upright and his pelvis is tipped back under him, so the line from his shoulders to his hips reads as a shallow curve rather than a column.

One specific place: a half-empty supermarket car park on a cold evening, the driver's door still open behind him, and the ordinary clutter of the errand it interrupted — an empty trolley bay, a carrier bag on the passenger seat, a receipt caught under a wiper, painted bay lines worn thin.

Key light: flat white light from the car park lamp standard directly overhead, bright and unflattering, minimal shadow. Fill: the weak spill from the open cabin.

Desaturated throughout, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_HERO_C = """A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his mid-forties in an ordinary shirt, sitting on a stiff wooden bench pushed back against a garden fence at an outdoor birthday dinner, caught mid-way through shifting his weight from one hip to the other with both hands planted flat on the bench slats either side of him. Under that force: both arms locked straight and taking his weight off the bench, one hip lifted clear of the wood, his trunk held rigid, his knees pushed out for balance. Face: eyes down at the ground, mouth open on a held breath, jaw set.

He is the only person not settled: the bench has no back to it, his pelvis has rolled behind his sitting bones, and his lower back is unsupported over the hard edge of the slat.

One specific place: a suburban garden on an evening in early autumn, and the ordinary clutter of the party going on around him — a fire pit with chairs pulled close, paper plates stacked on a side table, a cardigan over the back of a chair, string lights on the fence, other guests blurred and comfortable around the fire.

He is unaware of the camera. Key light: the low orange of the fire pit from the far side. Fill: the string lights above him. A rim of light along his locked forearms. Deep shadow along the fence behind the bench.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_PROB0_A = """A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is the three abandoned fixes filling the back seat of a car, photographed from the open rear door at standing height.

Exactly as they were thrown in and no more than these three: a flat memory foam wedge, compressed permanently into a body-shaped dish and folded once against the far door; an inflatable donut ring, half deflated with its valve stub sticking out, wedged on its edge behind the wedge; and a standalone strap-on lumbar roll with one buckle undone and the strap hanging loose across the seat. Every one of them has been used and none is in the driver's seat.

One specific place: a car parked in a supermarket bay on a cold evening with the rear door standing open, and the lived-in clutter of the routine none of them fixed — a cold coffee in a holder up front, a receipt curled in the door pocket, a folded hi-vis in the far footwell.

No subject, so no gaze. The frame looks across the back seat from the open door, the way the person who gave up on them is looking at it. Key light: the last cold daylight through the far window. Fill: the dim of the cabin. Rim light along the edge of the donut ring. Deep shadow into the footwell.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_PROB0_B = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different evenings. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt in the door pocket, real wear on the sill.

The only thing that changes is which of the three ordinary fixes is on the seat, and each is the plain unbranded version people already own — the three the section names and no others. Panel one: a flat memory foam wedge, slid forward with its cover rucked into a ridge at the front lip. Panel two: an inflatable donut ring, gone soft and rolled forward on itself. Panel three: a standalone strap-on lumbar roll, sagged down the seat back with its strap gone slack. All three photographed at the same point in the routine, at the end of a nine-hour day, with the driver out of the car and nothing touched or straightened first.

Light differs only in exposure between panels, never in warmth. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours none of them.

No product, no badges, no arrows and no text of any kind."""

P_PROB0_C = """A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is the three abandoned fixes stuffed into the open boot of a car, photographed square on from the rear at chest height.

Exactly as they were left and no more than these three: a flat memory foam wedge, permanently dished and shoved against the wheel arch; an inflatable donut ring, soft and creased, resting on top of it with its valve stub turned up; and a standalone strap-on lumbar roll, dropped in with both straps tangled around a jump lead. Nothing has been cleaned, matched or squared up.

One specific place: the open boot of an ordinary estate car on a cold evening in a supermarket car park, and the clutter of the routine around them — a folded shopping bag, a screenwash bottle on its side, a child's football under the parcel shelf, a bag of grit split at the corner.

No subject, so no gaze. The frame looks straight into the boot from behind, the way the person who filled it is looking at it. Key light: the car park lamp standard overhead, cold and hard. Fill: the weak boot lamp. Rim light along the lip of the boot. Deep shadow behind the objects.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_PROB1_A = """A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, the sacrum and the lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has hinged backward into the open crevice where the seat base meets the upright backrest and the lumbar curve has flattened and reversed. Right panel: the same figure on the same seat with one continuous unyielding contour filling that crevice, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the contour covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. A pair of short opposed arrows at the seat corner in each panel showing the shear the copy names, red on the left where the two surfaces work against each other, blue on the right where one contour carries them. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_PROB1_B = """A 2D flat-vector medical illustration with flat fills and hard edges, no gradients. Not photography, not a 3D render.

The attached photo is the exact reference for the product.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, the sacrum and the lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded, the pelvis hinged back into the crevice at the seat corner. Right panel: the same figure on the same seat with the reference product in place, drawn at a size and angle where it is obviously that product, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the product covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_PROB1_C = """A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same three-quarter rear view in both, the whole body in shot with the seat small within it. The two sitting bones, the sacrum and the soft tissue over them are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. These are the sitting bones and the sacrum, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has hinged back off the sitting bones and the load has moved onto the tailbone at the base of the sacrum. Right panel: the same figure on the same seat with one continuous contour filling that crevice, the load back on the two sitting bones and the tailbone clear of the seat. Neither the seat nor the contour covers the sacrum on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at the same two landmarks — the top of the hip bone and the top of the knee — both starting from the same point in their panel, red on the left and blue on the right. A filled region bounded by the contact surface itself, as wide as the contact is, one per panel: red on the left over the tailbone where the load has gone, blue on the right across both sitting bones where it belongs. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_CONT0_A = """A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated side-on in an ordinary matte grey car seat whose base slopes backward: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical seat in both. The body is cross-sectioned along the midline so the pelvis, the sacrum and the lumbar spine are visible inside the silhouette.

The pelvis, the sacrum and the lumbar vertebrae are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: two separate matte grey pieces sit on the seat, a pad on the base and a roll against the backrest, with a visible gap between them at the seat corner. The mannequin's pelvis has hinged backward into that gap and the hips have dropped below the knees.

Right panel is the correct state: the reference product is in place on the same seat at the same angle as one single object, its contour running unbroken from the seat section up into the lumbar section with no join anywhere along it, the hips lifted level with the knees. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all. A flat hard-edged blue band, unshaded, is drawn beside the lumbar spine along its own length on the side away from the product, running only the length the product reaches — never a fill of the bone, never a tint of the anatomy.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product."""

P_CONT0_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar work shirt, seated in the driver's seat of a parked car with the door open, his weight settled evenly and his gaze out through the windscreen rather than on the product, sitting well back so the whole seat back and the product against it are clear to the camera. He sits to the right of the frame.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with objects that genuinely belong there: a lanyard on the indicator stalk, a travel mug in the holder, a phone cable coiled at the dash, a folded hi-vis on the passenger seat, a parking permit on the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, occupying the space he is offset from, sits a small rectangular panel with a thin white border, split into two equal halves that share one photographic register. The left half shows the same seat with a flat foam wedge on the base and a separate strap-on roll against the backrest, the wedge slid forward and the roll dropped into the crevice between them, with glowing red points on the exposed seat corner and on the fallen roll. The right half shows the same seat with the reference product in place, brighter and cleaner, with a translucent blue overlay following the single continuous seam that runs from the seat section up into the lumbar section. A circular red badge carrying the white letters VS sits at the seam between the two halves.

No mark of any kind appears anywhere outside that panel."""

P_CONT0_C = """A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated in three-quarter rear view in an ordinary matte grey office swivel chair whose base slopes backward: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical chair in both. The body is cross-sectioned along the midline so the pelvis, the sacrum and the lumbar spine are visible inside the silhouette.

The pelvis, the sacrum and the lumbar vertebrae are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: nothing fills the crevice where the chair base meets the backrest, the pelvis has hinged backward into it and the hips have dropped below the knees. A flat hard-edged red overlay, unshaded, lies on the sacrum and the two lowest lumbar vertebrae where the load has collected.

Right panel is the correct state: the reference product is in place on the same chair at the same angle as one single object, its contour running unbroken from the seat section up into the lumbar section, the hips lifted level with the knees. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all. A flat hard-edged blue band, unshaded, is drawn beside the lumbar spine along its own length on the side away from the product, running only the length the product reaches.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product."""

P_CONT1_A = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product.

Shot by one person on a phone across one working day. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt in the door pocket, real wear on the sill.

The reference product is the subject of every panel and is the same physical object throughout — the same outline, the same black, the same continuous L-shaped contour, matching the attached photo exactly. It sits in the same position on the seat in every panel.

The only thing that changes is the point in the day: panel one at six in the morning before the first drive, panel two at midday after five hours of sitting, panel three at the end of an eight-hour shift. Every panel is photographed at the same point in the routine, with the driver already out of the car and nothing plumped, straightened or pushed back into place first. Across all three the contour still stands to its full depth at the seat corner and the seat section has not compressed into a dish.

Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind."""

P_CONT1_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar work shirt, sitting relaxed in the driver's seat of a parked car with the door open, one hand loose on his thigh and his gaze out through the windscreen rather than at the product. He is settled back with his weight even through both hips and nothing braced, and he sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with things that genuinely belong there: a lanyard on the indicator stalk, a travel mug in the holder, a phone cable coiled at the dash, a folded hi-vis on the passenger seat, a parking permit on the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border, showing one magnified detail the scene cannot carry at this distance: the cut edge of the product's foam core under his weight, close enough that the dense closed cell structure is readable and the seat section is visibly still standing to its full depth rather than bottoming out. It is a photograph in the same register as the scene and does not bleed into it, linked to the product by proximity alone with no arrow and no glow border.

No mark of any kind appears anywhere in the frame."""

P_CONT1_C = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product.

Shot by one person on a phone across one working day. One framing for every panel: the same office swivel chair photographed square-on from about a metre and a half back at seated eye height, the seat base across the lower third and a plain office partition filling the upper third. It reads as one shot taken three times, never as three different shots.

The same chair, the same partition and the same floor in all three panels, with deliberate real-world clutter: a coiled network cable along the skirting, a recycling bin half out of shot, scuff marks on the chair base.

The reference product is the subject of every panel and is the same physical object throughout — the same outline, the same black, the same continuous L-shaped contour, matching the attached photo exactly. It sits in the same position on the chair in every panel.

The only thing that changes is the point in the day: panel one at nine in the morning before anyone sits down, panel two at midday after four hours of typing, panel three at the end of an eight-hour shift. Every panel is photographed at the same point in the routine, with nobody in the room and nothing plumped, straightened or squared up first. Across all three the contour still stands to its full depth at the chair corner and the seat section has not compressed into a dish.

Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind."""

P_CONT2_A = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar work shirt, standing in an office doorway with the reference product carried loose in one hand down at his side, mid-stride and looking ahead into the room rather than at the product. Nothing is braced and nothing is held in the other hand. He stands to the right of the frame so the product and the room beyond him stay clear to the camera.

The reference product hangs from his hand by the lumbar section, identical to the attached photo in shape, colour and proportion, its continuous L-shaped contour readable against his leg.

One real open-plan office filled to the edges with objects that genuinely belong there: a stacked in-tray, a mug on a coaster, a coat over a chair back, a wheeled pedestal drawer, a whiteboard turned to the wall, a plant on a filing cabinet. Background blurred, but no bare wall or floor area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border, showing where the product lives when it is not in his hand: the same product seated in the driver's seat of his car, photographed from the open door, its seat section on the base and its lumbar section up the seat back. It is a photograph in the same register as the scene and does not bleed into it, linked to the product by proximity alone with no arrow and no glow border.

No mark of any kind appears anywhere in the frame."""

P_CONT2_B = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in every panel.

Shot by one person on a phone across one day. One framing for every panel: the seat photographed square-on from about a metre back at seated eye height, the seat base across the lower third. It reads as one shot taken three times, never as three different shots.

The reference product is the same physical object in all three panels — the same outline, the same black, the same continuous L-shaped contour, matching the attached photo exactly.

The only thing that changes is the surface it is anchored on, and each is photographed after the seat has been used and left, with nobody in shot and nothing straightened or pushed back into place first. Panel one: a fabric car seat with a lanyard on the stalk behind it. Panel two: a smooth leather driver's seat in a second car, with a receipt in the door pocket. Panel three: a vegan leather office swivel chair with a coiled cable along the skirting behind it. In every panel the product sits square where it was put, its back edge still tight into the seat corner, with no strap, no buckle and no fixing of any kind anywhere in frame.

Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind."""

P_CONT2_C = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her early fifties in a plain jumper, standing beside her open car door in a workplace car park with the reference product carried loose in one hand down at her side, already turned towards the building rather than looking at the product. Nothing is braced and nothing is held in the other hand. She stands to the right of the frame so the product and the open cabin behind her stay clear to the camera.

The reference product hangs from her hand by the lumbar section, identical to the attached photo in shape, colour and proportion, its continuous L-shaped contour readable against her coat.

One real workplace car park filled to the edges with things that genuinely belong there: painted bay lines worn thin, a wheeled bin against a wall, a bicycle in a rack, a low hedge, other parked cars, a wet patch across the tarmac. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even overcast daylight, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border, showing where the product lives at the other end of the journey: the same product seated on a home office swivel chair, photographed square on, its seat section on the base and its lumbar section up the chair back. It is a photograph in the same register as the scene and does not bleed into it, linked to the product by proximity alone with no arrow and no glow border.

No mark of any kind appears anywhere in the frame."""

P_CONT3_A = """A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his mid-forties in put-together but ordinary clothes, just out of the driver's seat of his car in a hotel car park at the end of a six-hour drive, straightening up to his full height with his weight even through both feet and both hands empty and open at his sides. Nothing is held, nothing is braced, nothing is covered. His chest is opening, his shoulders roll back and down, his eyes are coming open against the light and his brow has let go, and a small involuntary smile has arrived on its own while he looks off past the car at the road he has just come in on rather than at the camera.

The driver's door stands open beside him, and the reference product sits on the seat inside it as its own object near the camera, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary hotel car park on an unremarkable November afternoon, a second car and a blurred couple unloading further along, a wheeled suitcase upright on the tarmac, a wire bin, painted bay lines worn thin, a low wall behind. Nothing aspirational and nothing tidied.

Even natural daylight, bright, soft shadows, plain and unglamorous. A natural palette, light film grain, shallow depth of field, honest rather than drained and never warm-boosted.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text."""

P_CONT3_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar work shirt, sitting settled in the driver's seat of a parked car with the door open, both hands loose in his lap and his gaze out along the road ahead rather than at the product. His weight is even through both hips, his shoulders are down, nothing is braced. He sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with objects that genuinely belong there: a lanyard on the indicator stalk, a travel mug in the holder, a road atlas folded on the passenger seat, a phone cable coiled at the dash, a parking permit on the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

No inset, no panel and no reserved layer anywhere in the frame.

No mark of any kind appears anywhere in the frame."""

P_CONT3_C = """A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his mid-forties in ordinary cycling clothes without a club kit, standing over a bicycle at the side of a river trail with both feet flat on the path and both hands resting easy on the bars, mid-conversation with someone out of frame. Nothing is held against him, nothing is braced, nothing is covered. His chest is open, his shoulders are down and back, his head is up and turned along the trail, and a small involuntary smile has arrived on its own while he looks away from the camera.

His car is parked on the gravel behind him with the driver's door open, and the reference product sits on the seat inside it as its own object, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary riverside path on a grey Saturday morning, two or three blurred riders further along, a bin at the trail head, gravel scattered onto the tarmac, painted bay lines worn thin. Nothing aspirational and nothing tidied.

Even natural daylight, bright, soft shadows, plain and unglamorous. A natural palette, light film grain, shallow depth of field, honest rather than drained and never warm-boosted.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text."""


def snapshot(mode_line, scene, light, anchor, camera):
    return f"""A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

{mode_line}

{scene} — the mess stays, nothing tidied, nothing added for the picture. {light}, no other light.

One incidental owner object and no more: {anchor}.

{camera}; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture."""


P_REV_1 = snapshot(
    "The product mid-use in a van cab, photographed by its owner from the open driver's door: "
    "the reference cushion in place on the driver's seat with the owner's forearm resting "
    "across the top of the lumbar section, no face in shot.",
    "An ordinary working delivery van cab photographed exactly as found early on a weekday",
    "Cool early daylight through the windscreen and the open door",
    "a bunch of van keys dropped in the door bin",
    "Framing slightly tilted and a little too close, taken at arm's length from the seat")

P_REV_2 = snapshot(
    "The product simply sitting where it now lives: the reference cushion in place on a home "
    "office swivel chair, nobody in the picture at all.",
    "An ordinary spare-room office photographed exactly as found in the evening",
    "Warm yellow light from a single desk lamp and the room's overhead",
    "a charger cable coiled on the desk behind the chair",
    "Framing off-centre and taken from standing height looking down at the chair")

P_REV_3 = snapshot(
    "The product mid-use on a wheelchair, photographed by its owner looking down into their "
    "own lap: the reference cushion in place beneath and behind them with one hand resting on "
    "the armrest beside it, no face in shot.",
    "An ordinary front room photographed exactly as found in the middle of the afternoon",
    "Flat overcast daylight through a net-curtained window",
    "a folded newspaper wedged down the side of the seat",
    "Framing close and crooked, taken from very near looking straight down")

P_REV_4 = snapshot(
    "The opened box and its contents as the owner has just left them: the reference cushion "
    "out of its packaging on a kitchen table, still recovering its shape, with the flattened "
    "box and the plastic sleeve pushed to one side. Nobody in the picture at all.",
    "An ordinary kitchen photographed exactly as found in the middle of the day",
    "Mixed light, warm ceiling spots over cool daylight from the window",
    "a fruit bowl at the edge of the table",
    "Framing slightly tilted and taken from standing height about half a metre back")

# ---------------------------------------------------------------- gif briefs

BRIEF_PROB0 = """A shot of a driver sitting on a thin foam wedge on his car seat. The car brakes at a junction, the wedge slides forward under him and his pelvis rolls back into the open gap behind it, which is where the ache starts."""

ALT_PROB0 = """A shot of the same seat with a hand pushing a foam wedge forward from behind, nobody in the car. The wedge travels to the front lip and the gap opens behind it, the same gap a pelvis drops into."""

BRIEF_CONT1 = """A close shot of the cushion alone on a car seat at the end of a shift. A hand presses the seat section down flat and lets go, and the contour rises back to its full depth at the seat corner without a dent left in it."""

ALT_CONT1 = """A close shot of the cushion on an office chair with a full backpack set down on the seat section. The pack is lifted away and the contour springs back to its full depth while a thin foam pad beside it stays dished."""

BRIEF_CONT3 = """A shot of a man opening his car door in a hotel car park after six hours of driving. He swings both legs out and stands straight up in one movement, hands empty, and walks off without reaching back for his lower back."""

ALT_CONT3 = """A shot of the same man on a river trail beside a bicycle. He swings one leg over the saddle, settles onto it and pushes off along the path in one easy movement, with nothing braced and no hand going to his back."""

RESERVE_PROB1 = """A shot of a man lowering himself into a car seat that slopes backwards. As his weight settles his hips slide down below his knees and his lower back peels away from the seat back, leaving an open gap behind it."""


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
    "PRECONDITION, and it is not optional: these four photo tiles sit inside the SAME section "
    "element as three attributed quotes carrying reviewer names and Verified Purchase labels — "
    "measured on this export, zero closing tags between the grid and the quotes. "
    "05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a "
    "reviewer name, avatar, star row or verified badge. Use real customer photographs, or move "
    "the photo grid out of the attributed block, or drop the names and the verified labels — "
    "before rendering any of these. Sixth routed page in a row to breach it, so it is a "
    "template defect rather than a page one.")

SLOTS = []

SLOTS.append({
    "slot_id": "hero.image", "section_role": "hero",
    "asset": "120-01-hero-pain-scene.png",
    "placement": "advertorial header, under the eyebrow and above the byline",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides, close to verbatim. 01-pain-scene --candid asks for physical pain in a "
        "moment nobody would choose to be seen in, and hero.body.0 is that moment in the "
        "page's own words — a half-full supermarket car park, unable to get out of the seat "
        "without leaning his whole body against the door frame. A plays it as that single "
        "action. B moves to the confront gaze, which the type reserves for appearance and "
        "self-image rather than physical pain. C moves it to the wooden bench at Sarah's "
        "birthday dinner, the social cost the copy names second. PAGE LEGALITY: A satisfies "
        "06-relief-scene's pairing at content.items..3 and pairs_with 04-proof-lockedframe. "
        "PRODUCT PRESENCE: none, correctly — the type forbids it. PROMPT RISK: {chars} "
        "characters, inside the type's measured band.",
    "options": [
        opt("A", "01-pain-scene", "baseline", "16:9", P_HERO_A,
            "The page's opening scene as one action: a forearm braced along the door frame to "
            "lever himself off the seat in a cold car park. The evidence is the symptom as "
            "physical fact — hips below knees, the lumbar curve flat, the load on the base of "
            "the spine.",
            variant="candid", axes={"gaze": "candid"}),
        opt("B", "01-pain-scene", "axis: gaze=confront", "16:9", P_HERO_B,
            "The same argument in the type's other gaze, standing at the rear tire a minute "
            "later. The advertorial hero cell holds one type and the gates leave no second, so "
            "the honest variation here is the axis rather than a type borrowed from a role it "
            "does not belong to.",
            variant="confront", axes={"gaze": "confront"},
            notes="The type reserves --confront for appearance and daily frustration rather "
                  "than physical pain; it is offered because the axis is the only legal second "
                  "dimension at this slot, not because it fits better."),
        opt("C", "01-pain-scene", "execution: the birthday bench, not the car", "16:9",
            P_HERO_C,
            "Same type and same axis, the second cost the copy names — watching Sarah's "
            "outdoor birthday dinner from a stiff wooden bench, shifting hip to hip while "
            "everyone else sits comfortably. It sets up content.items..3, which resolves this "
            "exact class of situation.",
            variant="candid", axes={"gaze": "candid"}),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The slot's declared job is recognition — a cold reader seeing themselves in "
                  "a held state. Pages 58, 65, 73, 77, 97 and 104 all refused a hero on the "
                  "same ground; refused here for consistency with them.",
    },
})

SLOTS.append({
    "slot_id": "problems.items.0.image", "section_role": "problem-agitation",
    "asset": "120-02-problem0-pain-scene.png",
    "placement": "problem section 1, beside the What I Tried list",
    "recommended_media": "gif",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT and PAGE LEGALITY together. The section's own What I Tried list names exactly "
        "three failed fixes and no others — flat memory foam wedges, inflatable donut rings, "
        "standalone strap-on lumbar rolls — so the image argues the pile rather than the "
        "person, and the hero already owns the recognition job. This is Step 4 rung 4: "
        "01-pain-scene runs a second time in a different subject class, object-only, an "
        "execution the ledger already records twice. B is the stronger LITERAL fit — "
        "04-proof-lockedframe's use_when names the 'I tried three things' beat verbatim — and "
        "it is not recommended because lockedframe is the only type the comparison and proof "
        "cells hold, and spending it here would empty one of them. EVIDENCE: the object-only "
        "execution is the runbook's own worked precedent. PRODUCT PRESENCE: none in A or B, "
        "correctly. PROMPT RISK: {chars} characters. MEDIA: gif — see the loop below.",
    "options": [
        opt("A", "01-pain-scene", "rung 4: same type, object-only subject class", "16:9",
            P_PROB0_A,
            "The three named fixes thrown into the back seat, none of them in the driver's "
            "seat. No person, so the argument is carried entirely by what was given up on.",
            variant="candid", axes={"gaze": "candid"},
            notes="Rung 4 of Step 4's ladder: another execution of a type already recommended "
                  "at hero.image, differing on subject class. Declared here rather than left "
                  "to look like an oversight."),
        opt("B", "04-proof-lockedframe", "type: 04-proof-lockedframe --rivals", "16:9",
            P_PROB0_B,
            "The same three fixes as a locked three-panel test on one seat, which is what "
            "lockedframe's use_when calls the 'I tried three things' beat. --rivals keeps the "
            "product out of frame, which this section requires.",
            variant="rivals",
            notes="Picking B displaces 04-proof-lockedframe from content.items..1, whose "
                  "recommended option is the only --timelapse on the page; that slot would "
                  "fall to its own B. --rivals is advertorial-legal and barred only on "
                  "marketplace. Single-pass: the panels run handheld (ADR-021)."),
        opt("C", "01-pain-scene", "execution: the boot, not the back seat", "16:9", P_PROB0_C,
            "Same type and same object-only execution, moved to where things go when they are "
            "finished with rather than where they were last tried.",
            variant="candid", axes={"gaze": "candid"}),
    ],
    "gif": {
        "eligible": True,
        "form": "whole-frame",
        "kind": "cause",
        "type_id": "cause",
        "rung": "re-execution",
        "reason": "The section's claim is that the two-piece setup was actively worsening his "
                  "alignment — a state changing, which a still can only assert. The STAGING "
                  "has to change to build it: the routed still is 01-pain-scene object-only "
                  "and a foam wedge does not slide across an empty seat. Under ADR-031 the "
                  "force is named — a body on it and a car braking — and the gif library's "
                  "`cause` type names exactly this in its PURPOSE line. The product stays "
                  "absent either way, which is what keeps the argument this section's own.",
        "asset": "120-02-problem0-pain-scene--brief.svg",
        "refs": "gifs-library/cause/ — no files filed yet; the folder card carries the law",
        "output": "advertorial-cause-seat-cushion-l-shaped-v05.webp",
        "ratio": "16:9",
        "duration_s": 3,
        "loop": "seamless loop",
        "brief": BRIEF_PROB0,
        "alt": ALT_PROB0,
        "delivery": "animated webp, loop-safe, under the size ceiling",
    },
})

SLOTS.append({
    "slot_id": "problems.items.1.image", "section_role": "cause",
    "asset": "120-03-problem1-cause-anatomy.png",
    "placement": "problem section 2, beside the Why Fixes Missed list",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides. The section names its own mechanism three times — the junction crevice "
        "where the seat base meets the backrest, the hips dropping below the knees, and the "
        "destructive shear forces — and 02-cause-anatomy --diagnostic is the only type on this "
        "channel that draws a named mechanism. A takes the shear as its third mark, because "
        "the copy names it: the two surfaces working against each other is the fault in the "
        "section's own words. B swaps the drawn contour for the reference product, which "
        "answers a question this section has not asked yet — content.items..0 is where the "
        "product arrives. C moves to the sitting-bones view, which argues the tailbone half. "
        "PRODUCT PRESENCE: none in A, correctly — --diagnostic is the variant that needs no "
        "reference photo. PROMPT RISK: {chars} characters against a ~1800 two-mark reference; "
        "A carries three marks and states the overage rather than hiding it.",
    "options": [
        opt("A", "02-cause-anatomy", "baseline", "16:9", P_PROB1_A,
            "The pelvis hinging back into the crevice, side on, with the hip-to-knee measure "
            "and the shear at the seat corner both drawn. The section names both.",
            variant="diagnostic"),
        opt("B", "02-cause-anatomy", "axis: the product in the corrected panel", "16:9",
            P_PROB1_B,
            "The same two panels in flat vector with the reference product doing the "
            "correcting instead of an unnamed contour.",
            notes="Picking B introduces the product one section earlier than the copy does, "
                  "and content.items..0's mechanism argument then lands second rather than "
                  "first. It also needs the reference photo attached, which A does not."),
        opt("C", "02-cause-anatomy", "execution: three-quarter rear, the sitting bones",
            "16:9", P_PROB1_C,
            "Same type and same variant from behind, arguing the tailbone half of the same "
            "fault — the load leaving the two sitting bones for the base of the sacrum.",
            variant="diagnostic"),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The argument IS temporal and this slot earns motion — a pelvis rolling back "
                  "into the crevice as weight settles is a state changing. It is refused by "
                  "the BUDGET and not by the argument: the `problems` section carries two "
                  "items, so ADR-032 allows it one loop, and problems.items.0 holds the "
                  "stronger one. It is listed in motion.reserves as that loop's substitute.",
    },
})

SLOTS.append({
    "slot_id": "content.items..0.image", "section_role": "mechanism",
    "asset": "120-04-content0-mechanism-ghostbody.png",
    "placement": "body item 1, beside the What makes it work list",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides. The section's whole claim is structural — one piece rather than two, "
        "bridging the gap the previous section opened — and 03-mechanism-ghostbody is the type "
        "that cross-sections a body against a product. `body_contact: true` keeps it legal "
        "here; it is the gate that would otherwise send this slot to 03-mechanism-xray, whose "
        "own use_when restricts it to products that do NOT act on a body structure. A draws "
        "the wrong state as two separate pieces with a gap between them, which is the "
        "comparison the copy actually makes. B is a photograph and sells the relief instead of "
        "explaining it. RATIO: 03-mechanism-ghostbody declares 1:1 and 4:5 only, so A and C "
        "render at 1:1 into a 16:9 slot and the layout centre-crops 25% of the width; the two "
        "panels run left to right, so each loses the same band and the argument survives. B "
        "renders at the slot's own 16:9 and is the option to take if the crop is unacceptable. "
        "PROMPT RISK: {chars} characters.",
    "options": [
        opt("A", "03-mechanism-ghostbody", "baseline", "1:1", P_CONT0_A,
            "Two panels, one mannequin, cross-sectioned: two separate pieces with a gap at the "
            "seat corner against one continuous contour with none. The product is the only "
            "object with a real finish in either panel.",
            notes="RATIO: renders at 1:1 into a 16:9 slot. The layout centre-crops about 25% "
                  "of the width; the panels sit side by side so both lose the same band and "
                  "neither is favoured. Take B if the crop cannot be accepted."),
        opt("B", "06-relief-hero", "type: 06-relief-hero --vsinset", "16:9", P_CONT0_B,
            "The same wrong-versus-right argument as a photograph with the comparison held in "
            "a two-half inset, rather than as a cross-section. It renders at the slot's own "
            "ratio and nothing is cropped.",
            variant="vsinset", axes={"register": "commercial", "inset_mode": "vsinset"},
            notes="Picking B displaces 06-relief-hero from content.items..2, whose recommended "
                  "option is the only --context on the page; that slot would fall to its own "
                  "B. B also needs the reference photo attached."),
        opt("C", "03-mechanism-ghostbody", "execution: the office chair, three-quarter rear",
            "1:1", P_CONT0_C,
            "Same type and same marks on the other seat the copy names, from behind. The "
            "office chair is where the second half of his day happens.",
            notes="RATIO: renders at 1:1 into a 16:9 slot, same 25% width crop as A."),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The claim is a held structural state — one continuous contour where there "
                  "were two pieces — and the routed still argues it in two locked panels, "
                  "which are inspected rather than watched. Rung 2 was examined: a continuous "
                  "frame in which the pelvis rises as the contour goes in would restage the "
                  "CAUSE argument that problems.items.0 already carries, and ADR-037 allows "
                  "one loop per gif type per page. Refused on the argument, not the budget.",
    },
})

SLOTS.append({
    "slot_id": "content.items..1.image", "section_role": "proof",
    "asset": "120-05-content1-proof-lockedframe.png",
    "placement": "body item 2, beside the What makes it work list",
    "recommended_media": "gif",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT plus the type's own VARIANT SELECTION RULE. The claim is durability across a "
        "working day — it does not crush flat, and after eight hours it comes back to its full "
        "profile — which is a difference that only exists over TIME. lockedframe's use_when "
        "admits the type only where the difference is visible inside a static frame, and its "
        "variant rule sends exactly this case to --timelapse: one locked framing, the same "
        "object, three points in one day. B holds the same claim as a magnified foam core in a "
        "--detail inset, which shows density but cannot show recovery. EVIDENCE: the "
        "three-panel locked framing is the type's most-rendered execution on this product. "
        "PRODUCT PRESENCE: the product is the subject of all three panels, correctly. PROMPT "
        "RISK: {chars} characters. MEDIA: gif — the panels are the reason, see below.",
    "options": [
        opt("A", "04-proof-lockedframe", "baseline", "16:9", P_CONT1_A,
            "One seat, one framing, three points across a working day, nothing plumped back "
            "into place first. The contour still standing at the end is the whole argument.",
            variant="timelapse",
            notes="Single-pass: the panels run handheld rather than strict, which is the route "
                  "this type's own capability gate records for a renderer that cannot "
                  "composite (ADR-021)."),
        opt("B", "06-relief-hero", "type: 06-relief-hero --detail", "16:9", P_CONT1_B,
            "The same claim as one photograph with the foam core magnified in a corner inset: "
            "the cell structure readable and the seat section visibly not bottoming out under "
            "his weight.",
            variant="detail", axes={"register": "commercial", "inset_mode": "detail"},
            notes="Picking B displaces 06-relief-hero from content.items..2 and leaves this "
                  "page with no --timelapse; the durability-over-time half of the claim then "
                  "rests on the loop alone."),
        opt("C", "04-proof-lockedframe", "execution: the office chair, not the car", "16:9",
            P_CONT1_C,
            "Same type, same variant and same framing discipline on the other seat the copy "
            "names, across a typing day rather than a driving one.",
            variant="timelapse",
            notes="Single-pass: panels run handheld (ADR-021)."),
    ],
    "gif": {
        "eligible": True,
        "form": "whole-frame",
        "kind": "proof",
        "type_id": "proof",
        "rung": "re-execution",
        "reason": "The claim is a state changing — pressed flat, then back to full depth — and "
                  "the routed still argues it in three locked panels. ADR-024 settled that "
                  "panels are inspected rather than watched, so the STILL correctly earns no "
                  "motion while the ARGUMENT does: one continuous frame in which the one "
                  "variable changes carries the same claim. That is rung 2, and ADR-024 found "
                  "it is closer to a default than a backup on the result half of the floor.",
        "asset": "120-05-content1-proof-lockedframe--brief.svg",
        "refs": "gifs-library/proof/ — no files filed yet; the folder card carries the law",
        "output": "advertorial-proof-seat-cushion-l-shaped-v05.webp",
        "ratio": "16:9",
        "duration_s": 3,
        "loop": "seamless loop",
        "brief": BRIEF_CONT1,
        "alt": ALT_CONT1,
        "delivery": "animated webp, loop-safe, under the size ceiling",
    },
})

SLOTS.append({
    "slot_id": "content.items..2.image", "section_role": "how-to-use",
    "asset": "120-06-content2-relief-hero.png",
    "placement": "body item 3, beside the What to know list",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "THE ROLE'S OWN CELL IS EMPTY AFTER THE GATES, and this basis says so rather than "
        "leaving it inferred. how-to-use on advertorial holds 03-use-sequence alone, and "
        "`multi_step_usage: false` drops it — the type's own avoid_when reads 'the product has "
        "one obvious action', which placing a cushion on a seat is. Step 4's ladder therefore "
        "runs to rung 2, an adjacent step. FIT then decides between what is left: "
        "06-relief-hero --context is defined as the hero showing the product in hand when the "
        "buyer still needs to see where it lives, and this section is exactly that — carried "
        "from car to office in ten seconds, and it lives in both. A puts it in his hand with "
        "the car seat in the inset. B argues the grip half instead, across the three surfaces "
        "the copy names. PRODUCT PRESENCE: in hand and in the inset, which is the point. "
        "PROMPT RISK: {chars} characters.",
    "options": [
        opt("A", "06-relief-hero", "rung 2: adjacent step, the role's own cell is gated out",
            "16:9", P_CONT2_A,
            "The product carried loose in one hand into the office, with the driver's seat it "
            "just left held in the corner inset. Two places, one object, no straps in frame.",
            variant="context", axes={"register": "commercial", "inset_mode": "context"},
            notes="The how-to-use cell holds only 03-use-sequence and the multi_step_usage "
                  "gate drops it, so this slot is filled from an adjacent step under Step 4 "
                  "rung 2. Said here rather than left to look like a free choice."),
        opt("B", "04-proof-lockedframe", "type: 04-proof-lockedframe, the grip claim", "16:9",
            P_CONT2_B,
            "The other half of the section: the same object anchored square on fabric, on "
            "smooth leather and on vegan leather, with no strap or buckle anywhere in frame. "
            "It proves the grip; it does not show the carry.",
            variant="verdict",
            notes="Picking B displaces 04-proof-lockedframe from content.items..1, whose "
                  "recommended option is the only --timelapse on the page. Single-pass: the "
                  "panels run handheld (ADR-021)."),
        opt("C", "06-relief-hero", "execution: the car park, and a different person", "16:9",
            P_CONT2_C,
            "Same type and same inset mode at the other end of the journey, with the office "
            "chair in the inset instead of the car seat.",
            variant="context", axes={"register": "commercial", "inset_mode": "context"}),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The argument IS temporal and this slot earns motion — the grip holding "
                  "under a brake, and the ten-second carry between two seats, are both things "
                  "happening rather than states. It is refused by the BUDGET and not by the "
                  "argument. The `content` section runs to five items, so ADR-032 allows it "
                  "two loops provided they are not adjacent, and items.1 and items.3 are the "
                  "only non-adjacent pair among the three loop-capable slots. This slot sits "
                  "BETWEEN them, so it cannot be a reserve either: promoting it would put two "
                  "loops side by side. Recorded in motion.notes.",
    },
})

SLOTS.append({
    "slot_id": "content.items..3.image", "section_role": "outcome",
    "asset": "120-07-content3-relief-scene.png",
    "placement": "body item 4, beside the What changed list",
    "recommended_media": "gif",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides, and the type's own boundary confirms it. 06-relief-scene is the closing "
        "image of an advertorial when the promise is a state of living rather than a feature, "
        "and this section is three restored situations in a row. `result_visibility: on-body` "
        "keeps it legal — the gate that kills it is `invisible`, and standing straight out of "
        "a car is as on-body as a result gets. Its pairing with 01-pain-scene is satisfied at "
        "hero.image. A takes the hotel car park after six hours, which the copy names first "
        "and in the most physical terms. B closes with the product in frame under him instead, "
        "which is the boundary case relief-scene's own worked example marks as the wrong side "
        "here. C takes the river trail. PRODUCT PRESENCE: on the seat behind him, not held and "
        "not centred — the type is explicit that it must be in the picture without being "
        "presented. PROMPT RISK: {chars} characters. MEDIA: gif — see below.",
    "options": [
        opt("A", "06-relief-scene", "baseline", "16:9", P_CONT3_A,
            "The hotel car park at the end of the six-hour drive: coming to full height in one "
            "movement, both hands empty, the product on the seat behind him as its own object.",
            ),
        opt("B", "06-relief-hero", "type: 06-relief-hero", "16:9", P_CONT3_B,
            "The same beat closed with the product in frame under him rather than beside him — "
            "settled in the driver's seat with nothing braced.",
            axes={"register": "commercial", "inset_mode": "none"},
            notes="Picking B displaces 06-relief-hero from content.items..2. The type's own "
                  "boundary sends an on-body result to relief-scene and reserves relief-hero "
                  "for results that are invisible, so B is the weaker fit here by the type's "
                  "own words and is offered as the second legal type, not as an improvement."),
        opt("C", "06-relief-scene", "execution: the river trail, not the car park", "16:9",
            P_CONT3_C,
            "Same type at the second restored situation the copy names — thirty miles with his "
            "brother's Saturday group, with the car and the product parked behind him.",
            ),
    ],
    "gif": {
        "eligible": True,
        "form": "whole-frame",
        "kind": "relief",
        "type_id": "relief",
        "rung": "natural",
        "reason": "The `relief` type's tightest rule is that motion is earned only where the "
                  "motion IS the thing the problem used to block, and the page's own opening "
                  "is four minutes spent getting out of a car seat. Standing straight out of "
                  "one after six hours is that movement returned. Nothing is restaged: the "
                  "routed still is already him coming to his full height in the same car park, "
                  "so this is rung 1 — the first natural-rung loop on this page, and only the "
                  "third `relief` loop the library has routed.",
        "asset": "120-07-content3-relief-scene--brief.svg",
        "refs": "gifs-library/relief/ — no files filed yet; the folder card carries the law",
        "output": "advertorial-relief-seat-cushion-l-shaped-v05.webp",
        "ratio": "16:9",
        "duration_s": 3,
        "loop": "seamless loop",
        "brief": BRIEF_CONT3,
        "alt": ALT_CONT3,
        "delivery": "animated webp, loop-safe, under the size ceiling",
    },
})

_WALL = [
    ("120-08-review-social-snapshot.png", "photo grid, tile 1 of 4", P_REV_1,
     "van cab · driver's seat · in use, owner's forearm in shot · cool early daylight · "
     "arm's length from the seat",
     "The working-driver quote in the block, taken where that work happens. In-use mode with "
     "a body part in shot and no face."),
    ("120-09-review-social-snapshot.png", "photo grid, tile 2 of 4", P_REV_2,
     "spare-room office · swivel chair · at rest, nobody present · warm desk lamp · "
     "standing height looking down",
     "The desk-worker quote. At-rest mode, nobody in the picture, and the only warm-lit tile "
     "in the set."),
    ("120-10-review-social-snapshot.png", "photo grid, tile 3 of 4", P_REV_3,
     "front room · wheelchair · in use, owner looking into their own lap · flat overcast "
     "daylight · very close, straight down",
     "The wheelchair quote, which the block names explicitly and which no other tile covers. "
     "In-use mode from a first-person angle."),
    ("120-11-review-social-snapshot.png", "photo grid, tile 4 of 4", P_REV_4,
     "kitchen · table · just-unboxed, nobody present · mixed ceiling and window light · "
     "half a metre back at standing height",
     "The arrival moment none of the quotes describes, which is what stops the wall reading as "
     "four photographs of the same afternoon."),
]

for _i, (_asset, _place, _prompt, _varies, _why) in enumerate(_WALL):
    SLOTS.append({
        "slot_id": f"reviews.shots.{_i}.image", "section_role": "social-proof",
        "asset": _asset, "placement": _place,
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis":
            "ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of "
            "variation, so the four tiles differ from each other rather than from a B and a C. "
            f"This tile's place in the set: {_varies}. {_why} FIT: the tile answers a quote "
            "the block actually carries. PRODUCT PRESENCE: the reference product is the "
            "subject of every tile. PROMPT RISK: {chars} characters.",
        "options": [
            opt("A", "05-social-snapshot", _varies, "1:1", _prompt, _why,
                notes=WALL_FENCE),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "No social-proof slot carries motion. The mechanism is the one a router "
                      "actually hits: the six-type gif set carries no `social` type, so there "
                      "is nothing to file a loop under, wall tile or standalone (ADR-024).",
        },
    })

for _sid, _reason in [
    ("content.items..4.image",
     "The cost-and-offer block: premium chairs against custom re-upholstery against recurring "
     "physical therapy, closing on a half-price promotion and a multi-pack. An image cannot "
     "argue a price, and what is left once the prices are removed is the comparison "
     "content.items..2 already carries. Routed as `cta` on the page's own evidence and left to "
     "the offer card, exactly as page 104's features.items.4 was — the same beat on the same "
     "template family."),
    ("product.image", "Featured Product card: a standard product shot, out of library scope "
     "(cross-slot rule 6)."),
    ("product_end.image", "Closing offer card: a standard product shot, out of library scope."),
    ("header.logo", "Brand mark."),
    ("footer.logo", "Brand mark."),
    ("hero.author_avatar",
     "A portrait of a named person. No library type produces one, and generating a face to sit "
     "under a real byline is a disclosure decision rather than an image one — the `author` row "
     "of the slot-rules table is empty on every channel, deliberately."),
    ("guide.avatar", "A portrait of the named author. Same reason as hero.author_avatar."),
    ("comments.items.0.avatar", "A portrait of a named commenter. Same reason."),
    ("comments.items.1.avatar", "A portrait of a named commenter. Same reason."),
    ("comments.items.2.avatar", "A portrait of a named commenter. Same reason."),
    ("comments.items.3.avatar", "A portrait of a named commenter. Same reason."),
    ("comments.items.4.avatar", "A portrait of a named commenter. Same reason."),
    ("comments.items.5.avatar", "A portrait of a named commenter. Same reason."),
]:
    SLOTS.append({
        "slot_id": _sid, "section_role": DECLARED[_sid]["role"],
        "asset": None, "placement": None,
        "options": [],
        "out_of_scope_reason": _reason,
        "gif": {"eligible": False, "form": "none",
                "reason": "The slot carries no library image, so there is nothing to animate."},
    })


for _s in SLOTS:
    if not _s.get("options"):
        continue
    _rec = next(o for o in _s["options"] if o["opt"] == _s["recommended_opt"])
    _s["recommendation_basis"] = _s["recommendation_basis"].replace(
        "{chars}", str(len(_rec["prompt"])))


# gif.output is computed from the session name, so it cannot drift from the directory.
for _s in SLOTS:
    _g = _s.get("gif") or {}
    if _g.get("eligible"):
        _g["output"] = gif_name(_g["type_id"])

# ---------------------------------------------------------------- page blocks

MOTION = {
    "floor": 2,
    "ceiling": 5,
    "delivered": 3,
    "margin": 1,
    "groups_covered": ["result", "working"],
    "shortfall_reason": None,
    "reserves": [
        {
            "slot_id": "problems.items.1.image",
            "substitutes_for": "problems.items.0.image",
            "type_id": "cause",
            "group": "working",
            "rung": "re-execution",
            "brief": RESERVE_PROB1,
            "why_held_back":
                "The `problems` section carries two items, so ADR-032 allows it one loop and "
                "problems.items.0 holds the stronger one — the failed fixes are what the "
                "section is about. Promoting this one keeps the section at a single loop, so "
                "the spacing rule still holds, and it stays gif type `cause`, so ADR-037's "
                "one-per-type rule holds too. Its still is a two-panel illustration, so it "
                "arrives at rung 2 either way.",
        },
    ],
    "notes": [
        "Three loops against a floor of 2, so margin is 1. The third exists because the "
        "`content` list runs to five items and ADR-032 lets a section that long carry two "
        "provided they are not adjacent. Among the three loop-capable slots in that section — "
        "items.1, items.2 and items.3 — the only non-adjacent pair is items.1 with items.3, so "
        "the arrangement is forced rather than chosen.",
        "content.items..2 LOSES A LOOP IT EARNED, and it cannot serve as a reserve either. Its "
        "argument is intact — a grip holding under a brake and a ten-second carry between two "
        "seats are both things happening — but it sits BETWEEN the two delivered loops, so "
        "promoting it would put two side by side. The same shape page 77's features.items.2 "
        "was in.",
        "ALL THREE LOOPS ARE WHOLE-FRAME. No slot that earned motion has a recommended option "
        "whose skeleton legislates a layer a loop could occupy: 01-pain-scene and "
        "06-relief-scene both ban insets outright, and 04-proof-lockedframe's panels are the "
        "frame. content.items..1's option B would have offered a --detail layer, but B is not "
        "the recommended option and a gif verdict follows the recommendation. Page 104 remains "
        "the library's only inset loop.",
        "COVERAGE PAIR MET: cause (working) at problems.items.0, proof (result) at "
        "content.items..1, relief (result) at content.items..3. Two of the three are on the "
        "result half, which is the half ADR-024 measured as systematically underserved.",
        "ONE RUNG-1 LOOP, at content.items..3. Page 77 and page 104 both delivered zero — "
        "every loop on them was a rung-2 re-execution — and the reason this one is natural is "
        "that the routed still already contains the movement: 06-relief-scene puts him coming "
        "to his full height in the car park, and the loop is that same movement running.",
        "Review grid: 0 tiles — the six-type gif set carries no `social` type.",
    ],
}

COVERAGE = {
    "covered": [
        "step 1 pain — 01-pain-scene at hero.image, and again object-only at "
        "problems.items.0.image",
        "step 2 cause — 02-cause-anatomy --diagnostic at problems.items.1.image",
        "step 3 mechanism — 03-mechanism-ghostbody at content.items..0.image",
        "step 4 proof — 04-proof-lockedframe --timelapse at content.items..1.image",
        "step 5 social — 05-social-snapshot across all four review tiles",
        "step 6 relief — 06-relief-hero --context at content.items..2.image and "
        "06-relief-scene at content.items..3.image",
    ],
    "absent": [
        "step 3 how-to — 03-use-sequence is the how-to-use cell's only type on this channel "
        "and `multi_step_usage: false` drops it. NOT a gap: the type's own avoid_when reads "
        "'the product has one obvious action', and placing a cushion on a seat is that. The "
        "slot is filled from an adjacent step instead",
        "step 2 symptom breadth — 02-symptom-rail declares no advertorial channel, and the "
        "page makes no breadth claim, so this is not a gap",
        "step 5 personas — 05-persona-grid declares no advertorial channel. The reviews block "
        "names three distinct user classes the page never shows — a delivery driver, a desk "
        "worker and a wheelchair user — which IS a gap, but no type on this channel fills it. "
        "The review wall is carrying it instead, which is why tile 3 is the wheelchair",
    ],
    "notes": [
        "Awareness stage read from the page's own copy: SOLUTION-AWARE. The problem section is "
        "a list of what the reader has already bought and abandoned — flat wedges, donut "
        "rings, strap-on rolls — rather than an explanation of what hurts, and the copy sends "
        "a colleague to name the mechanism rather than establishing that a mechanism exists.",
        "Every rung of the Trust Ladder is covered. That is a property of the page: a "
        "two-problem, five-item advertorial with a review wall reaches further down the ladder "
        "than most.",
        "One-type-once is breached once, deliberately and under Step 4 rung 4: 01-pain-scene "
        "runs at the header as a person and at problems.items.0 object-only. That is the "
        "collision the runbook's own worked precedent resolves the same way, and it is here "
        "because the advertorial problem-agitation cell holds that one type alone.",
        "EVERY LINEAR SLOT CARRIES THREE OPTIONS and four of the seven carry a different TYPE "
        "at B. One-type-once binds the recommended SET rather than the option pool, so a B may "
        "carry a type recommended elsewhere; each one names the slot it would displace in its "
        "own composition_notes. The four review tiles carry one option each (ADR-022).",
        "The recommended set spends six distinct types across seven linear slots. Types the "
        "gates removed entirely: 03-use-sequence (multi_step_usage), 03-mechanism-xray (its "
        "own use_when restricts it to products that do not act on a body structure, and this "
        "one does), 02-symptom-rail and 05-persona-grid (no advertorial channel).",
    ],
}

PAGE_NOTES = [
    "SOURCE: ~/Downloads/content-library-local/"
    "landing-page-how-i-ended-sitting-pain-on-long-drives-and-at-my-desk.json, page id 120, "
    "handle how-i-ended-sitting-pain-on-long-drives-and-at-my-desk, lpTypeId advertorial. "
    "`imageBriefs` is NULL on this export, so htmlCompiled is the only slot source — the case "
    "earlier pages established it can carry.",
    "THE EXPORT'S OWN KEYS CARRY A DOUBLE DOT: `content.items..0.image` through "
    "`content.items..4.image`, with an empty segment where the other sections have none. The "
    "slot ids here reproduce the export key verbatim, because that is the string an editor "
    "pastes back into the page builder. It is not a typo in this file.",
    "FIFTH PAGE OF THIS PRODUCT, third template. Pages 31, 37, 77 and 104 are the same "
    "ergonomic seat cushion; this one is v05 under ADR-034's naming. Routed on its own copy "
    "rather than cloned — the narrator, the failed fixes, the mechanism vocabulary and every "
    "section heading differ from page 104, and this page carries a how-to-use beat that page "
    "104 does not.",
    "TEMPLATE RATIO: eight body slots at 16:9 and four review tiles at 1:1, with no 4:3 "
    "anywhere. The single casualty is 03-mechanism-ghostbody, which declares 1:1 and 4:5 only; "
    "its options state what the 25% width crop costs and option B renders at the slot's own "
    "ratio for anyone who will not accept it.",
    "THE HOW-TO-USE CELL IS EMPTY AFTER THE GATES and the page still routes an image there. "
    "03-use-sequence is the only type in that cell on this channel and `multi_step_usage: "
    "false` drops it, so content.items..2 is filled at Step 4 rung 2 from an adjacent step. "
    "SPEC 7.4's never-empty rule is what makes that the correct answer rather than an "
    "out-of-scope verdict.",
    "ADR-021 capability: every option is single-pass. 04-proof-lockedframe runs `handheld` "
    "wherever it appears.",
    "The reference photo is the owner's to upload. This export carries no product photograph, "
    "so `attachments` is omitted from every option rather than filled with an invented sha256 "
    "(SPEC 6.4). Every prompt that needs one keeps its G1 reference block and runs as written "
    "once the photo is attached — that is a gap in the EXPORT, not a blocked prompt.",
    "The authenticity fence is breached again, on four tiles. Sixth routed page in a row, and "
    "this export makes it measurable: zero closing section tags sit between the photo grid and "
    "the three attributed quotes.",
    "No pick prior was available. feedback/picks.jsonl is empty, so the >=20-pick tie-breaker "
    "in SPEC 7.7 never fired and every recommendation here rests on fit, legality, render "
    "evidence, product presence and prompt risk alone. These recommendations make the page "
    "argument-complete; they are not conversion-optimised.",
]

def _ceilings():
    """Prompt-size references, READ FROM THE TYPE FILES rather than typed here.

    A first draft of this block carried a hand-written table and it was invented for
    four of the seven types. Only three state a ceiling at all — 02-cause-anatomy,
    04-proof-lockedframe and 05-social-snapshot — and 02-cause-anatomy states a BAND
    keyed on mark count, which a flat number silently gets wrong by 250 characters.
    Whitespace is normalised first because the statements wrap mid-phrase in the files.
    """
    out = {}
    for tid in sorted(TYPES):
        path = os.path.join(ROOT, "registry", "types", f"{tid}.md")
        if not os.path.exists(path):
            continue
        text = " ".join(open(path, encoding="utf-8").read().split())
        band = re.search(r"~(\d{3,4}) characters at two marks, ~(\d{3,4}) at three", text)
        if band:
            out[tid] = {"two": int(band.group(1)), "three": int(band.group(2))}
            continue
        flat = re.search(r"Ceiling \*\*(\d{3,4}) characters\*\*", text)
        if flat:
            out[tid] = {"flat": int(flat.group(1))}
    return out


CEILINGS = _ceilings()


def _marks_in(prompt):
    """02-cause-anatomy's ceiling is stated per mark count, so the count is read off
    the prompt rather than assumed."""
    n = 0
    if "dashed straight lines" in prompt:
        n += 1
    if any(k in prompt for k in ("opposed arrows", "shaded wedge", "filled region")):
        n += 1
    if "disc badge" in prompt:
        n += 1
    return n


def _reference(o):
    """(limit, how it was derived) for one option, or None where the type states none."""
    c = CEILINGS.get(o["type"])
    if not c:
        return None
    if "flat" in c:
        return c["flat"], "its type's flat ceiling"
    m = _marks_in(o["prompt"])
    if m >= 3:
        return c["three"], f"its type's {m}-mark figure"
    return c["two"], "its type's two-mark figure"


_scored = [(s["slot_id"], o["opt"], o["type"], len(o["prompt"]), _reference(o))
           for s in SLOTS for o in s.get("options", [])]
_over = sorted((r for r in _scored if r[4] and r[3] > r[4][0]),
               key=lambda r: -(r[3] - r[4][0]))
_unrated = sorted({t for _, _, t, _, ref in _scored if ref is None})

if _over:
    _lines = "; ".join(
        f"{sid} {op} ({tid}) {n} against {ref[0]}, {round(100 * (n - ref[0]) / ref[0])}% over "
        f"({ref[1]})" for sid, op, tid, n, ref in _over)
    _marks = ", ".join(
        f"{s['slot_id']} {o['opt']} carries {_marks_in(o['prompt'])}"
        for s in SLOTS for o in s.get("options", [])
        if o["type"] == "02-cause-anatomy")
    PAGE_NOTES.append(
        f"{len(_over)} of {len(_scored)} PROMPTS SIT OVER A STATED CEILING and are shipped "
        f"that way, said here rather than left for the reader to find: {_lines}. The reference "
        "is 02-cause-anatomy's own, and that type states a BAND rather than a number — ~1800 "
        f"at two marks, ~2050 at three — so the count is read off each prompt: {_marks}. That "
        "is why A is measured against 2050 and B against 1800, and it is the distinction a "
        "flat ceiling table silently gets wrong by 250 characters. One trimming pass removed "
        "duplicated law first — the prose restatement of hip-below-knee that the red dashed "
        "line already measures, and the restatement of what red and blue mean when the closing "
        "signal-system line already legislates it. Adapter Rule 6 asks for a re-read past 2500 "
        "and nothing here comes near it.")
else:
    PAGE_NOTES.append(
        f"NO PROMPT EXCEEDS A STATED CEILING. All {len(_scored)} were measured at build time "
        "against the figures in their own type files.")

PAGE_NOTES.append(
    "CEILINGS ARE READ FROM THE TYPE FILES, not from a table in this script, and "
    f"{len(_unrated)} of the types used here state none at all: {', '.join(_unrated)}. Their "
    "prompts are reported as unrated rather than measured against a number this session would "
    "have had to invent. Both lines above are computed from the prompts at build time — a "
    "typed count is wrong the first time a prompt is edited and nothing catches it, which is "
    "the defect found in page 65's own note on 2026-08-21.")

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

    for missing in sorted(set(DECLARED) - {s["slot_id"] for s in SLOTS}):
        errs.append(f"{missing}: declared in content.json but not emitted")
    for extra in sorted({s["slot_id"] for s in SLOTS} - set(DECLARED)):
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
            if "advertorial" not in TYPES[o["type"]].get("channels", ""):
                errs.append(f"{sid} {o['opt']}: {o['type']} is not advertorial-legal")
            needs_photo = TYPES[o["type"]].get("requires_product_photo") is True
            exempt = o.get("variant") in ("rivals", "diagnostic")
            if needs_photo and not exempt and "the exact reference" not in o["prompt"]:
                errs.append(f"{sid} {o['opt']}: {o['type']} requires a product photo but the "
                            "prompt carries no reference block")
            if not needs_photo and "the exact reference" in o["prompt"]:
                errs.append(f"{sid} {o['opt']}: {o['type']} takes no product photo but the "
                            "prompt carries a reference block")
            # ADR-033: a --loop inset reserves its layer and says so
            if (o.get("axes") or {}).get("inset_motion") == "loop":
                if "empty reserved block" not in o["prompt"]:
                    errs.append(f"{sid} {o['opt']}: inset_motion=loop but the prompt does not "
                                "reserve the layer as an empty block (G12, ADR-033)")
                if "RESERVED BLOCK" not in (o.get("composition_notes") or ""):
                    errs.append(f"{sid} {o['opt']}: inset_motion=loop with no note that the "
                                "render is unshippable until the loop is in it (ADR-033)")

    for cond, tid, why in ATTRIBUTE_GATES:
        if cond(ATTRS):
            for s in routed:
                for o in s["options"]:
                    if o["type"] == tid:
                        errs.append(f"{s['slot_id']} {o['opt']}: {why}")

    WALL = [f"reviews.shots.{i}.image" for i in range(4)]
    linear = [s for s in routed if s["slot_id"] not in WALL]
    picked = [next(o for o in s["options"] if o["opt"] == s["recommended_opt"])["type"]
              for s in linear]
    wall = [s for s in routed if s["slot_id"] in WALL]
    kinds = {s["options"][0]["type"] for s in wall}
    if len(kinds) > 1:
        errs.append(f"the review wall is served by more than one type {sorted(kinds)}")
    picked.extend(sorted(kinds))
    for s in wall:
        if len(s["options"]) != 1:
            errs.append(f"{s['slot_id']}: a repeating section emits one option (ADR-022)")
        if "PRECONDITION" not in (s["options"][0].get("composition_notes") or ""):
            errs.append(f"{s['slot_id']}: the authenticity fence is breached and the option "
                        "carries no precondition")
    seen = [s["options"][0]["varies_on"] for s in wall]
    if len(set(seen)) != len(seen):
        errs.append("SET DIVERSITY: two review tiles share a varies_on line")
    for line in seen:
        if len([p for p in line.split("·") if p.strip()]) < 5:
            errs.append(f"SET DIVERSITY: `{line[:40]}` names fewer than five dimensions")

    RUNG4 = {"01-pain-scene"}
    dupes = {t for t in picked if picked.count(t) > 1}
    for t in sorted(dupes - RUNG4):
        errs.append(f"one-type-once breached in the recommended set: {t}")
    for t in sorted(dupes & RUNG4):
        warns.append(f"{t} runs twice under Step 4 rung 4 — declared in coverage.notes")

    step3 = {"03-mechanism-ghostbody", "03-spec-split", "03-use-sequence"}
    if len([t for t in picked if t in step3]) > 2:
        errs.append("step-3 budget exceeded")
    for s in linear:
        for o in s["options"]:
            rp = TYPES[o["type"]].get("requires_pair")
            if rp and rp != "null" and rp not in picked:
                errs.append(f"{s['slot_id']} {o['opt']}: requires_pair {rp} not on the page")
    for t in picked:
        for other in picked:
            if other != t and other in TYPES[t].get("never_with", ""):
                errs.append(f"never_with breached: {t} and {other}")

    elig = [s for s in SLOTS if s.get("gif", {}).get("eligible")]
    if len(elig) != MOTION["delivered"]:
        errs.append(f"motion.delivered says {MOTION['delivered']}, {len(elig)} eligible")
    if len(elig) > MOTION["ceiling"]:
        errs.append("motion ceiling exceeded")
    if MOTION.get("margin") != len(elig) - MOTION["floor"]:
        errs.append(f"motion.margin says {MOTION.get('margin')}, computed "
                    f"{len(elig) - MOTION['floor']}")
    secs = {}
    for s in elig:
        secs.setdefault(s["slot_id"].split(".")[0], []).append(s["slot_id"])
    for sec, ids in secs.items():
        if len(ids) == 1:
            continue
        if len(ids) > 2 or SECTION_ITEMS.get(sec, 0) < 5:
            errs.append(f"section `{sec}` carries {len(ids)} loops against "
                        f"{SECTION_ITEMS.get(sec, 0)} items (ADR-032): {ids}")
        _ix = [re.findall(r"\.(\d+)\.", i) for i in ids]
        idx = sorted(int(m[-1]) for m in _ix if m)
        if len(idx) == 2 and idx[1] - idx[0] < 2:
            errs.append(f"the two loops in `{sec}` are adjacent (items.{idx[0]} and "
                        f"items.{idx[1]}); ADR-032 needs a static item between them")

    # ADR-037: with no slot and no sequence in the filename, two loops of one gif
    # type on a page collide. One per type, enforced rather than hoped for.
    kinds = [x["gif"]["type_id"] for x in elig]
    for k in sorted({k for k in kinds if kinds.count(k) > 1}):
        errs.append(f"two loops on this page are gif type `{k}`; with no slot in the "
                    "filename they would be the same file (ADR-037)")

    GROUP = {"use": "working", "mechanism": "working", "cause": "working",
             "proof": "result", "relief": "result"}
    got = sorted({GROUP[s["gif"]["type_id"]] for s in elig})
    if got != MOTION["groups_covered"]:
        errs.append(f"motion.groups_covered says {MOTION['groups_covered']}, computed {got}")

    REGISTER = ("light", "lighting", "daylight", "lit", "backlit", "grade", "graded",
                "register", "overcast", "desaturated", "saturated", "palette",
                "exposure", "colour", "color", "tone", "greyscale", "grayscale")
    for s in elig:
        g = s["gif"]
        for f in ("output", "ratio", "duration_s", "loop", "brief", "alt", "delivery",
                  "refs", "asset"):
            if not g.get(f):
                errs.append(f"{s['slot_id']}: gif is missing `{f}`")
        for dead in ("shot", "action", "result", "match", "prompt"):
            if dead in g:
                errs.append(f"{s['slot_id']}: gif still carries `{dead}`, retired at ADR-028")
        if not g["asset"].endswith("--brief.svg"):
            errs.append(f"{s['slot_id']}: the plate carries --brief and .svg (G12)")
        if g["asset"] == s["asset"]:
            errs.append(f"{s['slot_id']}: plate asset must not be the slot's own asset")
        want = gif_name(g["type_id"])
        if g["output"] != want:
            errs.append(f"{s['slot_id']}: gif.output must be `{want}` (ADR-036), got "
                        f"`{g['output']}`")
        # ADR-033: whole-frame owes the page's shape; an inset owes its LAYER's, never the slot's
        if g["form"] == "whole-frame" and g["ratio"] != DECLARED[s["slot_id"]]["ratio"]:
            errs.append(f"{s['slot_id']}: a whole-frame loop IS the delivered image and owes "
                        f"the slot's {DECLARED[s['slot_id']]['ratio']}, not {g['ratio']}")
        if g["form"] == "inset" and g["ratio"] == DECLARED[s["slot_id"]]["ratio"]:
            errs.append(f"{s['slot_id']}: an inset loop fills a LAYER, not the frame, so its "
                        f"ratio is the layer's and cannot be the slot's "
                        f"{DECLARED[s['slot_id']]['ratio']} (ADR-033)")
        if g["form"] == "inset":
            host = next(o for o in s["options"] if o["opt"] == s["recommended_opt"])
            if (host.get("axes") or {}).get("inset_motion") != "loop":
                errs.append(f"{s['slot_id']}: form is inset but the recommended option does "
                            "not set inset_motion=loop")
        for label, text in (("brief", g["brief"]), ("alt", g.get("alt"))):
            if not text:
                continue
            n = len(text.split())
            if not 25 <= n <= 55:
                errs.append(f"{s['slot_id']}: the {label} is {n} words, outside 25-55")
            found = sorted({w for w in REGISTER if re.search(rf"\b{w}\b", text, re.I)})
            if found:
                errs.append(f"{s['slot_id']}: the {label} names {', '.join(found)} (ADR-030)")
        if g["brief"] == g.get("alt"):
            errs.append(f"{s['slot_id']}: gif.alt repeats the brief")

    for s in SLOTS:
        if not s.get("gif", {}).get("reason"):
            errs.append(f"{s['slot_id']}: no gif verdict (Step 5c requires one either way)")
        if s["section_role"] == "social-proof" and s.get("gif", {}).get("eligible"):
            errs.append(f"{s['slot_id']}: a social-proof slot carries motion")
        if not s.get("options") and not s.get("out_of_scope_reason"):
            errs.append(f"{s['slot_id']}: no options and no out_of_scope_reason (SPEC 7.4)")

    for s in routed:
        b = s["recommendation_basis"]
        if "{chars}" in b:
            errs.append(f"{s['slot_id']}: recommendation_basis still carries the placeholder")
        m = re.search(r"PROMPT RISK: (\d+) characters", b)
        if m:
            rec = next(o for o in s["options"] if o["opt"] == s["recommended_opt"])
            if int(m.group(1)) != len(rec["prompt"]):
                errs.append(f"{s['slot_id']}: basis claims {m.group(1)} characters, the "
                            f"prompt is {len(rec['prompt'])}")
    return errs, warns


# ---------------------------------------------------------------- emit

def render_md():
    L = []
    routed = [s for s in SLOTS if s.get("options")]
    n_opts = sum(len(s["options"]) for s in routed)
    n_gif = len([s for s in SLOTS if s.get("gif", {}).get("eligible")])
    n_block = len([s for s in routed for o in s["options"]
                   if "PRECONDITION" in (o.get("composition_notes") or "")])
    n_res = len([s for s in routed for o in s["options"]
                 if "RESERVED BLOCK" in (o.get("composition_notes") or "")])
    L.append(f"# Image prompts — page {PAGE}, "
             f"{CONTRACT['product']['name'].lower()}")
    L.append("")
    L.append("GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit "
             "the script and re-run. Routing rationale, the negative motion verdicts and the "
             "out-of-scope slots are all in `prompts.json`.")
    L.append("")
    L.append(f"- page `{PAGE}` · advertorial · solution-aware · registry `2.0.0` · "
             f"{len(routed)} routed slots · {n_opts} prompts · {n_gif} motion briefs")
    # Counted, never typed. The line this replaced claimed "the library's first
    # form: inset loop" — true of page 104, false the moment the harness was reused,
    # and nothing would have caught it because it was prose.
    _forms = {}
    for s in SLOTS:
        g = s.get("gif") or {}
        if g.get("eligible"):
            _forms[g["form"]] = _forms.get(g["form"], 0) + 1
    _shape = ", ".join(f"{v} {k}" for k, v in sorted(_forms.items()))
    L.append(f"- motion: {MOTION['delivered']} loops ({_shape}), floor {MOTION['floor']}, "
             f"margin {MOTION['margin']}, groups {', '.join(MOTION['groups_covered'])}")
    if n_res:
        L.append(f"- **{n_res} options carry a RESERVED BLOCK** — the render has an empty "
                 "grey panel where the loop goes and is not shippable until it is filled")
    if n_block:
        L.append(f"- **{n_block} prompts carry a blocking precondition**, stated on each")
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
            h = f"### {s['slot_id']} · option {o['opt']} — `{o['type']}`"
            if o.get("variant"):
                h += f" `--{o['variant']}`"
            L.append(h)
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
            L.append(f"### {s['slot_id']} · the motion brief — `{g['type_id']}` "
                     f"({g['form']})")
            L.append("")
            L.append(f"- form `{g['form']}` · rung `{g['rung']}` · reference folder: "
                     f"{g['refs']}")
            if g["form"] == "inset":
                L.append("- the loop fills the reserved block in the still above, so its "
                         f"ratio `{g['ratio']}` is the LAYER's shape and not the slot's "
                         f"`{DECLARED[s['slot_id']]['ratio']}`")
            L.append(f"- plate `plates/{g['asset']}` — generated by "
                     "`scripts/gen-plate.py`, production only, never a page asset")
            L.append("")
            L.append("```")
            L.append(g["output"])
            L.append(f"{g['duration_s']}s · {g['ratio']} · {g['loop']} · {g['delivery']}")
            L.append("")
            L.append(g["brief"])
            L.append("")
            L.append("IF THAT CANNOT BE SHOT")
            L.append(g["alt"])
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
    n = sum(len(s["options"]) for s in routed)
    nb = len([s for s in SLOTS if s.get("gif", {}).get("eligible")])
    ins = len([s for s in SLOTS if s.get("gif", {}).get("form") == "inset"])
    for w in warns:
        print(f"WARN  {w}")
    for e in errs:
        print(f"ERROR {e}")
    print(f"page {PAGE}: {len(SLOTS)} slots, {len(routed)} routed, {n} prompts, "
          f"{nb} motion briefs ({ins} inset), {len(errs)} errors, {len(warns)} warnings")
    return 1 if errs else 0


if __name__ == "__main__":
    raise SystemExit(main())

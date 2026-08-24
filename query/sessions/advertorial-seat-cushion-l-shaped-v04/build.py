#!/usr/bin/env python3
"""Build prompts.json and prompts.md for page 104 — ergonomic memory foam seat cushion.

The library's first routed `form: inset` loop (ADR-033).

prompts.json is the source of truth (query/output.schema.json); prompts.md is
generated from it and is never hand-edited (query/runbook.md Step 7).
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAGE = "104"


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
PAGE_TYPE, PRODUCT_SLUG, VERSION = 'advertorial', 'seat-cushion-l-shaped', 'v04'
assert os.path.basename(HERE) == f"{PAGE_TYPE}-{PRODUCT_SLUG}-{VERSION}", \
    "session directory does not match the parts the gif names are built from"


def gif_name(gif_type):
    """The only name a loop has, page-side and library-side alike (ADR-037).

    No slot and no sequence, which is why a page carries at most one loop of each
    gif type — the check below is what keeps that true rather than hoped for.
    """
    return f"{PAGE_TYPE}-{gif_type}-{PRODUCT_SLUG}-{VERSION}.mp4"

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

A man in his mid-forties in a creased shirt with the tie pulled loose, still in the driver's seat of his car on his own driveway at six in the evening, mid-way through pushing himself up off the seat with both arms locked straight against the top of the steering wheel. Under that force: both elbows rigid and taking his whole weight, shoulders driven up towards his ears, hips barely off the seat, his back held in one unbending piece. Face: eyes shut, jaw clamped, breath held.

His hips sit well below his knees in the backward-sloping seat, his lower back is pressed flat against the seat back with an open gap behind it, and the whole load has gone onto the base of his spine.

One specific place: a suburban driveway at the end of a nine-hour day, the driver's door already open behind him, and the lived-in clutter of the commute — a lanyard hung on the indicator stalk, a cold coffee in the holder, a child's shin pad in the passenger footwell, a parking permit clipped to the visor.

He is unaware of the camera. Key light: the last cold blue daylight through the windscreen. Fill: the weak dome light above him. A rim of light along his locked forearms. Deep shadow across the near third of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_HERO_B = """A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his mid-forties in a creased work shirt, standing in his own hallway with one hand pushed into the small of his back, turned towards the camera and holding its eye. Under that force: his weight thrown onto one hip, the other heel lifted clear of the floor, his free hand hanging heavy at his side, shoulders uneven. Face: brow raised and tight, mouth pressed thin, looking directly into the lens.

He cannot straighten fully: his trunk stays folded a few degrees forward of upright and his pelvis is tipped back under him, so the line from his shoulders to his hips reads as a shallow curve rather than a column.

One specific place: the hallway of an ordinary house just inside the front door on a weekday evening, and the lived-in clutter of the routine it disrupts — car keys dropped in a bowl, a work bag slumped against the skirting, a child's football boots kicked off by the mat, coats overloading a hook.

Key light: even flat ceiling light in the hallway, bright and unflattering, minimal shadow. Fill: the room's own ambient.

Desaturated throughout, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_HERO_C = """A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his mid-forties in a creased shirt, halfway up a short flight of metal bleacher steps at a school sports field on a Saturday morning, stopped mid-stride with one hand gripping the handrail and the other flat against his own lower back. Under that force: his leading leg still on the step above and taking none of his weight, his trailing shoulder dropped, his trunk twisted away from the pressing hand. Face: eyes down at the step, mouth open on a held breath, jaw set.

He has stopped where the climb changes: two steps below him the treads are clear and above him they are empty, and he is holding the rail hard enough that his forearm is tensed.

One specific place: the side of a school sports field on a Saturday morning, and the ordinary clutter of it — a folded camp chair leaning on the frame, a kit bag on the bottom tread, a paper cup left on a rail bracket, parents further along the stand.

He is unaware of the camera. Key light: flat grey morning daylight from a covered sky. Fill: light bouncing off the metal treads. A rim of light along the handrail. Deep shadow under the stand.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_PROB0_A = """A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is the pile of abandoned fixes filling the back seat of a car, photographed from the open rear door at standing height.

Exactly as they were thrown in: a hard ring-shaped donut pad on its edge against the far door, a flat foam cushion folded once and wedged behind it, a strap-on back pillow with one of its buckles undone and the strap hanging loose, a beaded wooden seat mat rolled and pushed into the footwell, and a vibrating massage cover with its cable still plugged into nothing. Every one of them has been used and none is in the driver's seat.

One specific place: a car parked on a driveway in the evening with the rear door standing open, and the lived-in clutter of the routine none of them fixed — a cold coffee in a holder up front, a receipt curled in the door pocket, a shin pad in the far footwell.

No subject, so no gaze. The frame looks across the back seat from the open door, the way the person who gave up on them is looking at it. Key light: the last cold daylight through the far window. Fill: the dim of the cabin. Rim light along the edge of the donut pad. Deep shadow into the footwell.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_PROB0_B = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different evenings. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt in the door pocket, real wear on the sill.

The only thing that changes is which ordinary fix is on the seat, and each is the plain unbranded version people already own. Panel one: a hard ring-shaped donut pad, rolled forward on itself against the front lip. Panel two: a flat foam cushion, slid forward with its cover rucked into a ridge. Panel three: a strap-on back pillow, sagged down the seat back with its strap gone slack. All three photographed at the same point in the routine, at the end of a nine-hour day, with the driver out of the car and nothing touched or straightened first.

Light differs only in exposure between panels, never in warmth. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours none of them.

No product, no badges, no arrows and no text of any kind."""

P_PROB0_C = """A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is the shelf of abandoned fixes in a garage, photographed square on at chest height.

Exactly as they were left: a hard donut pad standing on its edge with a crease worn across it, a flat foam cushion compressed permanently into a body-shaped dish and stacked on top of a paint tin, a strap-on back pillow hung by one buckle from a nail, a beaded wooden mat rolled and held with a rubber band, and a vibrating massage cover still in its box with the flap torn open. Nothing has been cleaned, matched or squared up.

One specific place: a shelf above a workbench in an ordinary domestic garage on a weekday evening, and the clutter of the room around it — a coiled hose on a bracket, a jar of screws with the lid off, a folded pushchair against the wall, a bag of cat litter split at the corner.

No subject, so no gaze. The frame looks straight at the shelf from chest height, the way the person who filled it is looking at it. Key light: a single bare bulb overhead, cold and hard. Fill: nothing. Rim light along the top edge of the shelf. Deep shadow behind the objects.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_PROB1_A = """A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, the sacrum and the lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has hinged backward into the open void where the seat base meets the backrest and the lumbar curve has flattened and reversed. Right panel: the same figure on the same seat with a continuous supportive contour filling that void, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the contour covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. A shaded wedge in each panel showing the angle open between the pelvis and the thigh, red on the left where it has collapsed and blue on the right where it is held. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_PROB1_B = """A 2D flat-vector medical illustration with flat fills and hard edges, no gradients. Not photography, not a 3D render.

The attached photo is the exact reference for the product.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, the sacrum and the lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded, the pelvis hinged back into the void at the seat corner. Right panel: the same figure on the same seat with the reference product in place, drawn at a size and angle where it is obviously that product, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the product covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_PROB1_C = """A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same three-quarter rear view in both, the whole body in shot with the seat small within it. The two sitting bones, the sacrum and the soft tissue over them are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. These are the sitting bones and the sacrum, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has hinged back off the sitting bones and the load has moved onto the tailbone at the base of the sacrum. Right panel: the same figure on the same seat with a continuous supportive contour filling the void at the seat corner, the load back on the two sitting bones and the tailbone clear of the seat. Neither the seat nor the contour covers the sacrum on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at the same two landmarks — the top of the hip bone and the top of the knee — both starting from the same point in their panel, red on the left and blue on the right. A filled region bounded by the contact surface itself, as wide as the contact is, one per panel: red on the left over the tailbone where the load has gone, blue on the right across both sitting bones where it belongs. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_FEAT0_A = """A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated side-on in an ordinary matte grey car seat whose base slopes backward: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical seat in both. The body is cross-sectioned along the midline so the pelvis, the sacrum and the lumbar spine are visible inside the silhouette.

The pelvis, the sacrum and the lumbar vertebrae are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: the mannequin sits with nothing filling the void where the seat base meets the backrest, the pelvis hinged backward into it, the hips dropped below the knees and the lumbar curve reversed. A flat hard-edged red overlay, unshaded, lies on the sacrum and the two lowest lumbar vertebrae where the load has collected.

Right panel is the correct state: the reference product is in place on the same seat at the same angle, its contour visibly following the line of the pelvis and the lumbar spine, the hips lifted level with the knees. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all. A flat hard-edged blue band, unshaded, is drawn beside the lumbar spine along its own length on the side away from the product, running only the length the product reaches — never a fill of the bone, never a tint of the anatomy.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product."""

P_FEAT1_A = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar shirt, sitting relaxed in the driver's seat of a parked car with the door open, one hand loose on his thigh and his gaze out through the windscreen rather than at the product. He is settled back with his weight even through both hips and nothing braced, and he sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with things that genuinely belong there: a lanyard on the indicator stalk, a coffee cup in the holder, a phone cable coiled at the dash, a folded jacket on the back seat, a parking permit on the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border. It is filled with one flat neutral grey tone and nothing else: no photograph, no drawing, no lettering, no texture and no detail of any kind inside it. It is an empty reserved block.

No mark of any kind appears anywhere in the frame."""

P_FEAT1_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar shirt, sitting relaxed in the driver's seat of a parked car with the door open, one hand loose on his thigh and his gaze out through the windscreen rather than at the product. He is settled back with his weight even through both hips, and he sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with things that genuinely belong there: a lanyard on the indicator stalk, a coffee cup in the holder, a phone cable coiled at the dash, a folded jacket on the back seat, a parking permit on the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border, showing one magnified detail the scene cannot carry at this distance: the textured underside of the product pressed against the smooth leather of the seat base, close enough that the grip pattern and the leather grain are both readable. It is a photograph in the same register as the scene and does not bleed into it, linked to the product by proximity alone with no arrow and no glow border.

No mark of any kind appears anywhere in the frame."""

P_FEAT1_C = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her early fifties in a plain jumper, sitting relaxed in a home office swivel chair with both feet flat on the floor, one hand resting loose on the desk and her gaze on the window rather than at the product. Her weight is even through both hips and she is settled back into the chair, sitting to the right of the frame so the whole chair back and the product against it stay clear to the camera.

The reference product is on the chair beneath and behind her, its seat section under her and its lumbar section standing up against the small of her back, identical to the attached photo in shape, colour and proportion.

One real home office filled to the edges with things that genuinely belong there: a full bookshelf, a mug on a coaster, a desk lamp turned away, a router with its cable looped, a cardigan over the chair arm, a plant on the sill. Background blurred, but no bare wall or floor area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border. It is filled with one flat neutral grey tone and nothing else: no photograph, no drawing, no lettering, no texture and no detail of any kind inside it. It is an empty reserved block.

No mark of any kind appears anywhere in the frame."""

P_FEAT2_A = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product.

Shot by one person on a phone across one working day. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt in the door pocket, real wear on the sill.

The reference product is the subject of every panel and is the same physical object throughout — the same outline, the same black, the same continuous L-shaped contour, matching the attached photo exactly. It sits in the same position on the seat in every panel.

The only thing that changes is the point in the day: panel one at six in the morning before the first drive, panel two at midday after five hours of sitting, panel three at the end of a ten-hour shift. Every panel is photographed at the same point in the routine, with the driver already out of the car and nothing plumped, straightened or pushed back into place first. Across all three the contour still stands to its full depth at the seat corner and the seat section has not compressed into a dish.

Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind."""

P_FEAT3_A = """A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his mid-forties in put-together but ordinary clothes, standing up off a metal bleacher bench at a school sports field at the end of a match, coming to his full height in one movement with his weight even through both feet and both hands empty and open. Nothing is held, nothing is braced against the rail or the bench, nothing is covered. His chest is opening, his shoulders roll back and down, his eyes are up and following something out on the pitch, and a small involuntary smile has arrived on its own while he looks away from the camera.

The reference product sits on the bench slat he has just left, near the camera in the lower third of the frame, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary school sports field on a grey Saturday, two or three blurred parents further along the stand, a folded camp chair, a kit bag under the bench, painted line markings worn thin on the grass.

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
    "The product mid-use in a car, photographed by its owner from the open driver's door: "
    "the reference cushion in place on the driver's seat with the owner's forearm resting "
    "across the top of the lumbar section, no face in shot.",
    "An ordinary saloon car photographed exactly as found on a weekday morning",
    "Cool early daylight through the windscreen and the open door",
    "a lanyard hung on the indicator stalk",
    "Framing slightly tilted and a little too close, taken at arm's length from the seat")

P_REV_2 = snapshot(
    "The product simply sitting where it now lives: the reference cushion in place on a home "
    "office swivel chair, nobody in the picture at all.",
    "An ordinary spare-room office photographed exactly as found in the evening",
    "Warm yellow light from a single desk lamp and the room's overhead",
    "a charger cable coiled on the desk behind the chair",
    "Framing off-centre and taken from standing height looking down at the chair")

P_REV_3 = snapshot(
    "The product mid-use in a truck cab, photographed by its owner over their own shoulder: "
    "the reference cushion in place on the bench seat with two fingers tucked against the "
    "edge of the lumbar section, no face in shot.",
    "An ordinary working truck cab photographed exactly as found on a flat grey afternoon",
    "Flat overcast daylight through the side window",
    "a clipboard wedged against the far side of the seat",
    "Framing close and crooked, taken from very near the seat over the shoulder")

P_REV_4 = snapshot(
    "The opened box and its contents as the owner has just left them: the reference cushion "
    "out of its packaging on a kitchen table, still recovering its shape, with the flattened "
    "box and the plastic sleeve pushed to one side. Nobody in the picture at all.",
    "An ordinary kitchen photographed exactly as found in the middle of the day",
    "Mixed light, warm ceiling spots over cool daylight from the window",
    "a fruit bowl at the edge of the table",
    "Framing slightly tilted and taken from standing height about half a metre back")

# ---------------------------------------------------------------- gif briefs

BRIEF_PROB0 = """A shot of a driver sitting on a hard donut pad on the car seat, or on the bare seat itself. When the car brakes the pad rolls forward under him and his pelvis drops back into the gap behind it, and sitting like that nine hours a day is what locks the back."""

ALT_PROB0 = """A shot of the same seat with a hand pushing an old donut pad forward from behind, no driver and no moving car. The pad rolls to the front lip and the gap opens behind it, the same gap a pelvis hinges back into on every brake."""

BRIEF_FEAT1 = """A close shot of the textured underside of the cushion pressed against smooth leather, filling the frame. The car brakes hard, the seat leather flexes and the whole cabin jolts, and the grip pattern does not travel a millimetre across it."""

ALT_FEAT1 = """A close shot of the same underside on the same leather with a hand shoving the cushion hard from behind, nobody in the car. It gives a finger's width and settles back, while an ordinary flat pad beside it walks forward and stays there."""

BRIEF_FEAT3 = """A shot of a man standing up off a metal bleacher bench at the end of a match. He comes to his full height in one movement without pushing off the rail or the bench, turns, and walks down the steps without once reaching back for his lower back."""

ALT_FEAT3 = """A shot of the same man getting out of his car at the end of a long drive. He swings his legs out, stands straight up in one go without grabbing the door frame, and walks off with the cushion still on the seat behind him."""

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
    "PRECONDITION, and it is not optional: these four photo tiles sit inside the same reviews "
    "block as three attributed quotes carrying reviewer names. 05-social-snapshot's "
    "authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, "
    "star row or verified badge. Use real customer photographs, or move the photo grid out of "
    "the attributed block, or drop the names — before rendering any of these. Fifth routed "
    "page in a row to breach it, so it is a template defect rather than a page one.")

RESERVED_BLOCK = (
    "THE RESERVED BLOCK IS NOT A DESIGN ELEMENT. This option carries a `--loop` inset, so its "
    "legislated layer is drawn as a flat empty grey block for the editor to drop the loop "
    "into (G12, ADR-033). The render keeps this slot's own asset filename because it IS the "
    "frame the loop lands in, and it is NOT shippable until the loop is in it — an empty "
    "block will ship unnoticed as a design choice if nobody is told, which is what this note "
    "exists to prevent. The work order is the generated plate beside it.")

SLOTS = []

SLOTS.append({
    "slot_id": "hero.image", "section_role": "hero",
    "asset": "104-01-hero-pain-scene.png",
    "placement": "advertorial header, under the eyebrow and above the byline",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides, close to verbatim. 01-pain-scene --candid asks for physical pain in a "
        "moment nobody would choose to be seen in, and hero.body.0 is that moment in the "
        "page's own words — bracing both arms against the steering wheel just to find the "
        "leverage to stand. A plays it as that single action. B moves to the confront gaze, "
        "which the type reserves for appearance and self-image rather than physical pain. C "
        "moves it to the bleacher steps, which is the cost the copy names second and which "
        "features.items.3 later resolves. RATIO: 01-pain-scene declares 16:9 and this template "
        "is 16:9 above the review grid, so nothing is cropped. PAGE LEGALITY: A satisfies "
        "06-relief-scene's requires_pair at features.items.3 and pairs_with "
        "04-proof-lockedframe at features.items.2. PRODUCT PRESENCE: none, correctly. PROMPT "
        "RISK: {chars} characters against a measured band of 1379-2153.",
    "options": [
        opt("A", "01-pain-scene", "baseline", "16:9", P_HERO_A,
            "The page's opening scene as one action: both arms locked on the wheel to lever "
            "himself off the seat at six in the evening. Evidence is the symptom as physical "
            "fact — hips below knees, the lumbar curve flat, the load on the base of the "
            "spine.",
            variant="candid", axes={"gaze": "candid"}),
        opt("B", "01-pain-scene", "axis: gaze=confront", "16:9", P_HERO_B,
            "The same argument in the type's other gaze, in the hallway a minute later. The "
            "advertorial hero cell holds one type and the gates leave no second, so the honest "
            "variation is the axis.",
            variant="confront", axes={"gaze": "confront"},
            notes="The type reserves --confront for appearance and daily frustration rather "
                  "than physical pain; it is offered because the axis is the only legal second "
                  "dimension here, not because it fits better."),
        opt("C", "01-pain-scene", "execution: the bleacher steps, not the car", "16:9",
            P_HERO_C,
            "Same type and same axis, the second cost the copy names — the Saturday games he "
            "stopped being asked to. It sets up features.items.3, which resolves this exact "
            "situation.",
            variant="candid", axes={"gaze": "candid"}),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The slot's declared job is recognition — a cold reader seeing themselves in "
                  "a held state. Pages 58, 65, 73, 77 and 97 all refused a hero on the same "
                  "ground; refused here for consistency with them.",
    },
})

SLOTS.append({
    "slot_id": "problems.items.0.image", "section_role": "problem-agitation",
    "asset": "104-02-problem0-pain-scene.png",
    "placement": "problem section 1, beside the what-I-tried list",
    "recommended_media": "gif",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides. The advertorial problem-agitation cell holds 01-pain-scene alone and "
        "one-type-once has spent it at the header, so this is Step 4 rung 4 — another "
        "execution of a type already on the page, which the runbook's own worked precedent "
        "resolves the same way. The section is a list of objects that failed, not a person "
        "suffering, and evidence rank 3 is exactly what the copy enumerates: the failed tool "
        "in the state that shows it failed. B is a real second reading and is on-cell for a "
        "comparison role, but it spends 04-proof-lockedframe here and forces features.items.2 "
        "off its own recommendation. C moves the pile to the garage shelf they ended up on. "
        "PRODUCT PRESENCE: none, correctly — every object in frame is an alternative. PROMPT "
        "RISK: {chars} characters.",
    "options": [
        opt("A", "01-pain-scene", "baseline — object-only, no person in frame", "16:9",
            P_PROB0_A,
            "The five fixes the copy names, thrown into the back seat and out of the driver's "
            "seat where they were supposed to work. No person: the argument is against the "
            "objects.",
            variant="candid", axes={"gaze": "candid"},
            notes="COMBINATION: this option is what keeps 04-proof-lockedframe available for "
                  "features.items.2. Picking B here forces that slot to change."),
        opt("B", "04-proof-lockedframe", "type: the three-alternatives comparison", "16:9",
            P_PROB0_B,
            "The same indictment as a locked-frame comparison: three ordinary fixes on one "
            "seat across three evenings, none of them winning. The type's use_when names this "
            "beat verbatim.",
            variant="rivals",
            notes="COMBINATION: picking B spends 04-proof-lockedframe here and forces "
                  "features.items.2 to change. --rivals is advertorial and paid-social only, "
                  "which this page satisfies."),
        opt("C", "01-pain-scene", "execution: the garage shelf, not the back seat", "16:9",
            P_PROB0_C,
            "Same type and same object-only execution, a different place and different "
            "evidence: the same five fixes months later, each carrying the wear that retired "
            "it.",
            variant="candid", axes={"gaze": "candid"}),
    ],
    "gif": {
        "eligible": True, "form": "whole-frame", "kind": "cause", "type_id": "cause",
        "rung": "re-execution",
        "reason": "The copy's claim is that the pads rolled forward and the pelvis dropped "
                  "back every time he braked, which is a state changing that a still can only "
                  "assert. The STAGING has to change to build it: the routed still is "
                  "01-pain-scene object-only and a donut pad does not roll across an empty "
                  "seat. Under ADR-031 the force is named — a body on it and a car braking — "
                  "and the gif library's `cause` type names exactly this in its PURPOSE line. "
                  "The product stays absent either way.",
        "asset": "104-02-problem0-pain-scene--brief.svg",
        "refs": "gifs-library/cause/ — no files filed yet; the folder card carries the law",
        "output": None,  # set below
        "ratio": "16:9",
        "duration_s": 3, "loop": "seamless loop",
        "brief": BRIEF_PROB0.strip(),
        "alt": ALT_PROB0.strip(),
        "delivery": "mp4, muted, loop-safe, under the size ceiling",
    },
})

SLOTS.append({
    "slot_id": "problems.items.1.image", "section_role": "cause",
    "asset": "104-03-problem1-cause-anatomy.png",
    "placement": "problem section 2, beside the mechanism list",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT and the removal test together, and this page hands the type its own vocabulary: "
        "the copy calls the fault pelvic-hinge collapse. Take the backward-sloping seat out of "
        "the left panel and the hinged pelvis goes with it, so this is a switchable mechanism "
        "rather than accumulated damage. The measurable landmark pair the type demands is in "
        "the copy — hips dropping below knees — and the difference is well past the 2:1 the "
        "`measure` mark needs. A runs --diagnostic and adds `range`, the wedge showing the "
        "hinge angle itself, which is the fault the section names. B is the base variant with "
        "the product in the right panel. C trades `range` for `pressure` on the sitting bones. "
        "PAGE LEGALITY: 02-cause-anatomy pairs_with 01-pain-scene and 03-mechanism-ghostbody, "
        "both on the page. PROMPT RISK: {chars} characters against a measured ~2050 at three "
        "marks.",
    "options": [
        opt("A", "02-cause-anatomy", "baseline", "16:9", P_PROB1_A,
            "The seat is the culprit and the pelvic hinge is the structure it acts on. Two "
            "panels, one figure, the hip-to-knee line measured and the hinge angle shaded, "
            "with the product held back until the mechanism section.",
            variant="diagnostic"),
        opt("B", "02-cause-anatomy", "variant: the product enters the right panel", "16:9",
            P_PROB1_B,
            "The same anatomy with the reference product drawn into the corrected panel. It "
            "resolves the argument here instead of at features.items.0, which is a real "
            "editorial choice rather than a better one.",
            notes="Picking B puts the product in frame one section earlier than the copy "
                  "reveals it, and makes this slot require the product photo."),
        opt("C", "02-cause-anatomy", "execution: subject class — the sitting bones, not the "
            "whole hinge", "16:9", P_PROB1_C,
            "Same type and variant, a different structure and a different third mark: the load "
            "moving off the two sitting bones onto the tailbone, drawn as a contact region.",
            variant="diagnostic"),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "A two-panel illustrated comparison is inspected rather than watched — the "
                  "reader holds both states side by side and reads the dashed lines against "
                  "each other, and the library has measured 0 of 13 such slots earning a "
                  "verdict. The section's one permitted loop is also spent at "
                  "problems.items.0, but the argument refuses this on its own grounds first.",
    },
})

SLOTS.append({
    "slot_id": "features.items.0.image", "section_role": "mechanism",
    "asset": "104-04-feature0-mechanism-ghostbody.png",
    "placement": "feature section 1, beside the why-every-fix-missed-it list",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides against a ratio cost and FIT wins. The section's sentence is that a "
        "support system must execute three mechanical moves at once — elevate the hips, bridge "
        "the gap, hold the lumbar curve — which is a mechanism inside the body that cannot be "
        "filmed, and body_contact is true so the gate opens. RATIO COST, stated rather than "
        "hidden: this type declares 1:1 and 4:5 and not the template's 16:9, so it renders "
        "square and the layout crops it; the two panels sit side by side, so a centre-crop to "
        "16:9 keeps both and loses head and foot room. 03-mechanism-xray is NOT offered: its "
        "avoid_when bars a trivial interior and a block of moulded foam is one. Only one "
        "option is emitted — the cell holds one legal type here, and this type has no axes to "
        "vary, so a B or a C would be a reroll rather than a named dimension, which SPEC 7.4 "
        "bars. PROMPT RISK: {chars} characters against a measured 2056-2916.",
    "options": [
        opt("A", "03-mechanism-ghostbody", "baseline", "1:1", P_FEAT0_A,
            "Two panels of the same cross-sectioned mannequin in the same sloped seat, "
            "differing only in whether the product is there. Red stress on the sacrum where "
            "the load collects, blue support beside the lumbar spine where the contour carries "
            "it.",
            notes="RATIO: renders at 1:1, the type's own declared ratio; the 16:9 template "
                  "slot crops it. Both panels survive a centre-crop, head and foot room do "
                  "not."),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "Two technical panels are inspected rather than watched, the reading the "
                  "library has measured 0 of 13 times. A re-execution would have to show the "
                  "product arriving under the pelvis, which argues the fitting rather than the "
                  "mechanism. The `features` list may carry two loops under ADR-032 and both "
                  "are spent at items.1 and items.3, which are the only non-adjacent pair "
                  "available.",
    },
})

SLOTS.append({
    "slot_id": "features.items.1.image", "section_role": "proof",
    "asset": "104-05-feature1-relief-hero.png",
    "placement": "feature section 2, beside the what-makes-it-work list",
    "recommended_media": "gif",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT against an exhausted cell, and this is the library's FIRST routed inset loop. The "
        "advertorial proof cell holds 04-proof-lockedframe alone and the recommended set "
        "spends it at features.items.2, so this is Step 4 rung 2. 06-relief-hero's use_when "
        "asks for one image that proves wrong against right, shows the product and sells the "
        "relief state; --detail is the inset mode the type names for a feature too small to "
        "read at scene scale, which is exactly the textured non-slip base the copy credits. "
        "The layer's content is TEMPORAL — the base holding while the car brakes — which is "
        "the condition inset_motion --loop requires, so the loop lives in a layer the skeleton "
        "already legislates rather than in a new one. A reserves that layer as an empty block; "
        "B fills it with the still photograph instead and gives up the loop; C is the same "
        "reserved layer in a home office. EVIDENCE: 06-relief-hero is the most-rendered type "
        "in the library at 22. PROMPT RISK: {chars} characters; this type is multi-layer and "
        "runs long by design.",
    "options": [
        opt("A", "06-relief-hero", "baseline — the inset layer reserved for the loop", "16:9",
            P_FEAT1_A,
            "The product doing its job in the car, with the corner layer left empty for the "
            "editor to drop the loop into. The hero carries the relief; the reserved block "
            "carries the claim the copy makes about braking.",
            variant="detail",
            axes={"register": "commercial", "inset_mode": "detail", "inset_motion": "loop"},
            notes=RESERVED_BLOCK),
        opt("B", "06-relief-hero", "axis: inset_motion=still — the detail as a photograph",
            "16:9", P_FEAT1_B,
            "The same frame with the layer filled by a still macro of the grip pattern against "
            "the leather. It ships as a page asset with no editor step, and it asserts the "
            "grip rather than demonstrating it.",
            variant="detail",
            axes={"register": "commercial", "inset_mode": "detail", "inset_motion": "still"}),
        opt("C", "06-relief-hero", "execution: the desk chair, not the car seat", "16:9",
            P_FEAT1_C,
            "Same type, same reserved layer, the other half of the copy's portability claim. "
            "The loop that fills it would have to change with the scene: a desk chair has no "
            "braking, so the alternate staging becomes the one that ships.",
            variant="detail",
            axes={"register": "commercial", "inset_mode": "detail", "inset_motion": "loop"},
            notes=RESERVED_BLOCK),
    ],
    "gif": {
        "eligible": True, "form": "inset", "kind": "mechanism", "type_id": "mechanism",
        "rung": "natural",
        "reason": "The section's claim is that the textured base held its ground against "
                  "smooth leather when he braked at highway speeds. Holding against a force is "
                  "temporal and no static frame carries it. This is the library's first inset "
                  "verdict: 06-relief-hero legislates a --detail layer already, that layer's "
                  "content is a magnified mechanism under load, and inset_motion --loop is "
                  "legal on every inset_mode except --none. Nothing is restaged, so rung 1. "
                  "Under ADR-031 the force is named — a car braking with a body in the seat.",
        "asset": "104-05-feature1-relief-hero--brief.svg",
        "refs": "gifs-library/mechanism/ — no files filed yet; the folder card carries the law",
        "output": None,  # set below
        "ratio": "1:1",
        "duration_s": 3, "loop": "seamless loop",
        "brief": BRIEF_FEAT1.strip(),
        "alt": ALT_FEAT1.strip(),
        "delivery": "mp4, muted, loop-safe, under the size ceiling",
    },
})

SLOTS.append({
    "slot_id": "features.items.2.image", "section_role": "proof",
    "asset": "104-06-feature2-proof-lockedframe.png",
    "placement": "feature section 3, beside the what-to-know list",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT and the VARIANT SELECTION RULE together. The section's claim is that ten hours of "
        "sitting did not produce the usual ache and that the core held, which is a condition "
        "over time rather than a difference between products — so the gate switches the "
        "variable from which product to which state of the same object, and --timelapse is "
        "what it mandates. Only one option is emitted: the advertorial proof cell holds this "
        "type alone once 06-relief-hero is spent at features.items.1, the gate fixes the "
        "variant, and a second execution of the same seat on the same day would be a reroll "
        "rather than a named dimension. CAPABILITY: `strict` needs compositing so the panels "
        "run `handheld` (ADR-021). PROMPT RISK: {chars} characters against a 1800 ceiling.",
    "options": [
        opt("A", "04-proof-lockedframe", "baseline", "16:9", P_FEAT2_A,
            "One seat, one framing, three points in a single ten-hour day, and the only "
            "variable is the hour. The contour still stands to full depth at the end of it.",
            variant="timelapse"),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The claim is genuinely temporal and this slot would earn a loop on its own "
                  "argument — but a ten-hour compression is the one thing a three-second loop "
                  "cannot honestly show, so a re-execution would have to promise a timescale "
                  "it does not have. It is also refused by spacing: the `features` list may "
                  "carry two loops and items.1 and items.3 are the only non-adjacent pair, "
                  "with this slot sitting between them.",
    },
})

SLOTS.append({
    "slot_id": "features.items.3.image", "section_role": "outcome",
    "asset": "104-07-feature3-relief-scene.png",
    "placement": "feature section 4, beside the what-changed list",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides and the requires_pair is already paid for. 06-relief-scene closes an "
        "advertorial when the promise is a state of living rather than a feature, and this "
        "section is the Blue Ridge trip and the two back-to-back games in metal bleachers. Its "
        "requires_pair is 01-pain-scene, which is at the header on the same man. The relief "
        "situation is chosen from what the problem forbade: the bleachers are the exact thing "
        "his daughter stopped asking him to, so A stages the inverse of hero option C. Only "
        "one option is emitted: the outcome cell holds 06-relief-scene and 06-relief-hero, and "
        "06-relief-hero is spent at features.items.1, which leaves this type with no legal "
        "second type and no axis but `gaze`, whose other value the type bans outright. PRODUCT "
        "PRESENCE: standalone class — it sits on the bench slat he has just left, near the "
        "camera and turned so it can be read. PROMPT RISK: {chars} characters.",
    "options": [
        opt("A", "06-relief-scene", "baseline", "16:9", P_FEAT3_A,
            "The release and the return in one frame: standing up off the bleacher bench at "
            "the end of the match, weight even, hands empty, the smile arriving on its own "
            "while he watches the pitch.",
            axes={"gaze": "candid"}),
    ],
    "gif": {
        "eligible": True, "form": "whole-frame", "kind": "relief", "type_id": "relief",
        "rung": "natural",
        "reason": "The still catches the second of release; the loop is the movement into it — "
                  "same person, same place, same staging, nothing re-argued, so rung 1. It "
                  "meets the `relief` type's tightest rule head on: motion is earned only "
                  "where the motion IS the thing the problem used to block, and standing up "
                  "off a metal bleacher bench is precisely what the copy says he could not do. "
                  "Page 77 was the first page to route this rule; this is the second, and the "
                  "first where the page's own copy names the blocked movement.",
        "asset": "104-07-feature3-relief-scene--brief.svg",
        "refs": "gifs-library/relief/ — no files filed yet; the folder card carries the law",
        "output": None,  # set below
        "ratio": "16:9",
        "duration_s": 4, "loop": "seamless loop",
        "brief": BRIEF_FEAT3.strip(),
        "alt": ALT_FEAT3.strip(),
        "delivery": "mp4, muted, loop-safe, under the size ceiling",
    },
})

for i, (prompt, varies) in enumerate([
    (P_REV_1, "in-use · saloon car · driver's seat · cool early daylight · seated arm's length"),
    (P_REV_2, "at-rest · home office · swivel chair · warm desk lamp · standing above"),
    (P_REV_3, "in-use · truck cab · bench seat · flat overcast daylight · close over the "
              "shoulder"),
    (P_REV_4, "kit-flatlay · kitchen · wooden table · mixed warm and cool · half a metre back"),
]):
    SLOTS.append({
        "slot_id": f"reviews.shots.{i}.image", "section_role": "social-proof",
        "asset": f"104-{8 + i:02d}-review-{i + 1}.png",
        "placement": f"review grid tile {i + 1} of 4",
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis":
            "One option by law (ADR-022): the four tiles are the unit of variation, not the "
            "tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is "
            "whether the thing exists and works in a normal home. The SET DIVERSITY LAW is "
            "satisfied across the four: four room classes, four surfaces, four light "
            "temperatures, four camera distances and three content modes.",
        "options": [
            opt("A", "05-social-snapshot", varies, "1:1", prompt,
                "One tile of the four-tile set, differing from its siblings on room class, "
                "surface, light temperature, camera distance and content mode.",
                axes={"register": "ugc"}, notes=WALL_FENCE),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "No social-proof slot carries motion. The six-type gif set carries no "
                      "`social` type, so a social-proof slot has nothing to file a loop under "
                      "(ADR-024).",
        },
    })

# ---------------------------------------------------------------- out of scope

PRICE_REASON = (
    "A cta cell: the section's whole argument is price — custom re-upholstery against "
    "high-end chairs against recurring chiropractic — and every comparison is carried by a "
    "number. G6 bans text in frame, so the image would have to state the claim without the "
    "figures that ARE the claim. Pages 37 and 77 refused the same section on this page's own "
    "product for the same reason.")
SHOT_REASON = (
    "A standard product shot. The library covers argument images, not the offer card's "
    "packshot or the masthead (mapping/slot-rules.md, the cta row is empty on every channel).")
AUTHOR_REASON = (
    "A portrait of a named person. No library type produces one, and generating a face to sit "
    "under a real byline or a named comment is a disclosure decision rather than an image one "
    "(mapping/slot-rules.md, the author row is empty on every channel by design).")

OUT_OF_SCOPE = [
    ("features.items.4.image", "feature section 5, the price comparison", "cta", PRICE_REASON),
    ("product.image", "mid-page product card", "cta", SHOT_REASON),
    ("product_end.image", "closing offer card, above the final CTA", "cta", SHOT_REASON),
    ("header.logo", "masthead", "cta", SHOT_REASON),
    ("footer.logo", "footer", "cta", SHOT_REASON),
    ("hero.author_avatar", "byline avatar beside the author name", "author", AUTHOR_REASON),
    ("guide.avatar", "About the author card", "author", AUTHOR_REASON),
] + [(f"comments.items.{i}.avatar", f"reader discussion, commenter {i + 1}", "author",
      AUTHOR_REASON) for i in range(6)]

for sid, place, role, reason in OUT_OF_SCOPE:
    SLOTS.append({
        "slot_id": sid, "section_role": role, "asset": None, "placement": place,
        "out_of_scope_reason": reason, "options": [],
        "gif": {"eligible": False, "form": "none",
                "reason": "No generated image in this slot to animate."},
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
    "reserves": [],
    "notes": [
        "Three loops against a floor of 2, so margin is 1. The third exists because the "
        "`features` list runs to five items and ADR-032 lets a section that long carry two "
        "provided they are not adjacent; items.1 and items.3 are the only non-adjacent pair "
        "among the loop-capable slots, so the arrangement is forced rather than chosen.",
        "FIRST INSET LOOP IN THE LIBRARY, at features.items.1. Every loop routed before this "
        "page was whole-frame, and both page 77 and page 97 recorded the same reason: no type "
        "at a slot that earned motion legislated a layer a loop could occupy. Here one does. "
        "06-relief-hero's --detail layer holds a magnified mechanism under load, which is the "
        "TEMPORAL condition inset_motion --loop requires, so the loop lives in a layer the "
        "skeleton already legislates rather than in a new one.",
        "The consequence is on the option rather than hidden: the host render carries a flat "
        "empty grey block where the loop goes, keeps this slot's own asset filename because it "
        "IS the frame the loop lands in, and is NOT shippable until the loop is in it "
        "(ADR-033).",
        "motion.reserves is empty and that is the honest reading. `features` is carrying its "
        "maximum, and its one slot in between — items.2 — sits BETWEEN the two delivered "
        "loops, so promoting it would put two side by side. `problems` has one loop and its "
        "only other slot is refused on its own grounds. The cover is gif.alt, which all three "
        "loops carry.",
        "COVERAGE PAIR MET: cause (working) at problems.items.0, mechanism (working) at "
        "features.items.1, relief (result) at features.items.3.",
        "features.items.3 is the second `relief` loop the library has routed and the first "
        "where the page's own copy names the blocked movement — his daughter stopped asking "
        "him to the games because she knew he could not survive the bleachers, and the loop is "
        "him standing up off that bench.",
        "Review grid: 0 tiles — the six-type gif set carries no `social` type.",
    ],
}

COVERAGE = {
    "covered": [
        "step 1 pain — 01-pain-scene at hero.image, and again object-only at "
        "problems.items.0.image",
        "step 2 cause — 02-cause-anatomy --diagnostic at problems.items.1.image",
        "step 3 mechanism — 03-mechanism-ghostbody at features.items.0.image",
        "step 4 proof — 06-relief-hero --detail at features.items.1.image and "
        "04-proof-lockedframe --timelapse at features.items.2.image",
        "step 5 social — 05-social-snapshot across all four review tiles",
        "step 6 relief — 06-relief-scene at features.items.3.image",
    ],
    "absent": [
        "step 2 symptom breadth — 02-symptom-rail declares no advertorial channel, and the "
        "page makes no breadth claim, so this is not a gap",
        "step 5 personas — 05-persona-grid declares no advertorial channel. The brief lists "
        "five personas and the page shows none of them, which IS a gap, but no type on this "
        "channel can fill it",
    ],
    "notes": [
        "Awareness stage read from the page's own copy: SOLUTION-AWARE. The reader is assumed "
        "to have already bought donut pads, flat foam and strap-on pillows — the problem "
        "section is a list of what they have already tried, not an explanation of what hurts.",
        "Every rung of the Trust Ladder is covered. That is a property of the page: a "
        "two-problem, five-feature advertorial with a review wall reaches further down the "
        "ladder than most.",
        "One-type-once is breached once, deliberately and under Step 4 rung 4: 01-pain-scene "
        "runs at the header as a person and at problems.items.0 object-only, which is the "
        "collision the runbook's own worked precedent resolves the same way.",
        "Four slots emit ONE option rather than three, and each says why on its own basis: "
        "features.items.0 (the cell holds one legal type and it has no axes), "
        "features.items.2 (the gate fixes the variant), features.items.3 (the cell's second "
        "type is spent and the type's only axis has one legal value), and the four review "
        "tiles (ADR-022). SPEC 7.4 asks for three where three legal possibilities exist and "
        "bars padding with rerolls where they do not.",
    ],
}

PAGE_NOTES = [
    "SOURCE: ~/Downloads/content-library-local/landing-page-untitled-4.json, page id 104, "
    "template TPL-ADV17, lpTypeId advertorial. `imageBriefs` is NULL on this export, so "
    "htmlCompiled is the only slot source — which is the case the earlier pages established it "
    "can carry: it names all 24 image fields and their template ratios.",
    "SAME PRODUCT AS PAGE 77, different page. 29 of 192 content keys are identical and they "
    "are boilerplate; the narrator, the daughter, the mechanism vocabulary and every feature "
    "heading differ. Routed on its own copy rather than cloned, and the two pages diverge at "
    "four slots. One asset can still serve both where the argument matches — that reuse is "
    "ADR-023's stated reason for the library existing.",
    "TEMPLATE RATIO: nine body slots at 16:9 and four review tiles at 1:1, the same shape as "
    "page 77. The single casualty is 03-mechanism-ghostbody at 1:1, and its option states what "
    "the crop costs.",
    "THE COPY NAMES THE MECHANISM: `pelvic-hinge collapse`. That is why 02-cause-anatomy takes "
    "`range` as its third mark — the wedge showing the hinge angle is the fault in the "
    "section's own words, which is a stronger draw than borrowing page 77's `pressure`.",
    "ADR-021 capability: every option is single-pass. 04-proof-lockedframe runs `handheld`.",
    "The authenticity fence is breached again, on four tiles. Fifth routed page in a row.",
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
        idx = sorted(int(i.split(".")[2]) for i in ids if i.count(".") >= 3)
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
    L.append("# Image prompts — page 104, ergonomic memory foam seat cushion")
    L.append("")
    L.append("GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit "
             "the script and re-run. Routing rationale, the negative motion verdicts and the "
             "out-of-scope slots are all in `prompts.json`.")
    L.append("")
    L.append(f"- page `{PAGE}` · advertorial · solution-aware · registry `2.0.0` · "
             f"{len(routed)} routed slots · {n_opts} prompts · {n_gif} motion briefs")
    L.append(f"- motion: {MOTION['delivered']} loops, floor {MOTION['floor']}, margin "
             f"{MOTION['margin']}, groups {', '.join(MOTION['groups_covered'])} — including "
             "the library's **first `form: inset` loop**")
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

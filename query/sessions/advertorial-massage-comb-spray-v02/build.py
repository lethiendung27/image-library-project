#!/usr/bin/env python3
"""Build prompts.json and prompts.md for page 125 — electric spray massage comb.

Second page of this product, first advertorial. First page written to the owner's
lean prompt spec, first with a `use` loop, and first where all three loops are rung 1.

prompts.json is the source of truth (query/output.schema.json); prompts.md is
generated from it and is never hand-edited (query/runbook.md Step 7).
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAGE = "125"


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
PAGE_TYPE, PRODUCT_SLUG, VERSION = 'advertorial', 'massage-comb-spray', 'v02'
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
    "03-mechanism-xray": [
        "photographic elements", "human body", "hands", "skin", "scene background",
        "environment", "extra colors", "signal colour on the product", "invented components",
        "components at the wrong scale", "exploded parts floating apart", "text", "callouts",
        "leader lines", "scale bars", "cut that breaks the product outline"],
    "03-use-sequence": [
        "a face", "a full body", "arms beyond the wrist", "photographic background",
        "environment", "step numbers", "arrows", "text", "panels of unequal size",
        "the product changing size between panels", "a second product",
        "hands doing two things at once", "product held for the camera rather than used"],
}

# ---------------------------------------------------------------- the prompts
#
# Written to the owner's lean spec, confirmed 7 of 7 on 2026-08-24: no `cinematic
# film still`, no Key/Fill/Rim/Deep-shadow block, no grade line, and no 3-4 object
# clutter list. One focus clause replaces the list; the model supplies the domestic
# texture from `nothing is arranged and nothing is tidied` on its own.
#
# G13 rule 3 is written with a NEGATIVE beside its positive cap. The rule as
# published states the cap positively and forbids nothing, and 1 of 3 renders on
# 2026-08-24 came back a clear wince anyway. The negative is evidence, not new law.

FOCUS = ("Nothing is arranged for the camera and nothing is tidied. The frame holds {}, "
         "and nothing else competes for attention.")
NOMARK = "No product, no panels and no insets. No mark of any kind."
CHILD_FACE = ("Her face carries effort and nothing more: no wince, no tears, no open mouth, "
              "no crying.")

P_HERO_A = f"""Editorial photojournalism, natural and unstaged.

A woman in her thirties in a work blouse standing at a bathroom sink early in the morning, mid-way through dragging a dry plastic brush down through the length of her own hair with one hand while the other presses the crown flat. Under that force: her brush arm pulled hard down past her shoulder, her head tipped away from the pull, the pressing elbow lifted high across her chest. Face: brow drawn in, mouth pressed shut, eyes down on the hair in her hand.

The hair is the evidence. Fine strands stand straight out from her head in a halo, several cling flat to her cheek and jaw, more lift off the brush and follow it as it leaves the hair, and the crown springs back up the instant her hand comes away.

One specific place: a family bathroom at a quarter to seven.

She is unaware of the camera. Regular early morning light.

{FOCUS.format("her, her hair and the brush")}

{NOMARK}"""

P_HERO_B = f"""Editorial photojournalism, natural and unstaged.

A woman in her thirties in a work blouse standing at a bathroom sink early in the morning, turned away from the mirror towards the camera with both hands still raised at the sides of her head where she has been trying to smooth her hair down. Under that force: both elbows up and out, fingers spread flat against the hair, shoulders lifted. Face: brow raised and tight, mouth slightly open, looking directly into the lens and holding it.

Fine strands stand out from her head in a halo through and above her fingers, several cling flat across her forehead, and the hair she has just pressed down is already lifting again.

One specific place: a family bathroom at a quarter to seven.

Regular early morning light.

{FOCUS.format("her, her hair and her hands")}

{NOMARK}"""

P_HERO_C = f"""Editorial photojournalism, natural and unstaged.

A woman in her thirties already in her coat, stopped at a hallway mirror by the front door on her way out, mid-way through flattening one side of her hair with the palm of her hand while the other hand holds a dry plastic brush down at her side. Under that force: her pressing arm bent hard across her face, her head tilted away from the palm, her shoulder driven up, her weight on the front foot as if she has stopped mid-stride. Face: brow drawn in, lips pressed together, eyes on her own reflection.

The hair is the evidence. Fine strands stand out from the flattened side in a halo the moment the palm lifts, more cling across the collar of her coat, and one section will not lie down at all.

One specific place: a hallway by the front door on a school morning.

She is unaware of the camera. Regular morning light.

{FOCUS.format("her, her hair and the mirror")}

{NOMARK}"""

P_C0_A = f"""Editorial photojournalism, natural and unstaged.

A woman in her thirties in a work blouse sitting at a kitchen table in front of an open laptop a minute before a call, turned away from the screen towards the camera with both hands still raised at the sides of her head where she has been trying to smooth her hair down. Under that force: both elbows up and out, fingers spread flat against the hair, shoulders lifted, her back held forward off the chair. Face: brow raised and tight, mouth slightly open, looking directly into the lens and holding it.

Fine strands stand out from her head in a halo through and above her fingers, several cling flat across her forehead, and the hair she has just pressed down is already lifting again.

One specific place: a kitchen table set up as a workspace on a weekday morning.

Regular morning light.

{FOCUS.format("her, her hair and the open laptop")}

{NOMARK}"""

P_C0_B = f"""Editorial photojournalism, natural and unstaged.

A woman in her thirties in a work blouse sitting at a kitchen table in front of an open laptop a minute before a call, mid-way through pressing both sides of her hair down with her palms and watching the screen rather than the camera. Under that force: both elbows lifted wide, palms flat against the hair above her ears, her chin tucked towards the laptop, her shoulders drawn up. Face: brow drawn in, mouth pressed shut, eyes fixed on the screen.

The hair is the evidence. Fine strands stand out from the crown in a halo above her hands, several cling flat across her forehead, and the sections she has already pressed are lifting again behind her palms.

One specific place: a kitchen table set up as a workspace on a weekday morning.

She is unaware of the camera. Regular morning light.

{FOCUS.format("her, her hair and the open laptop")}

{NOMARK}"""

P_C0_C = f"""Editorial photojournalism, natural and unstaged.

A woman in her thirties in a work blouse standing in an office lift lobby, turned towards the camera with one hand still raised where she has been pressing her hair down against the side of her head. Under that force: that elbow up and out, fingers spread flat against the hair, her other hand gripping a laptop bag strap at her shoulder. Face: brow raised and tight, mouth slightly open, looking directly into the lens and holding it.

Fine strands stand out from her head in a halo through and above her fingers, several cling across her collar, and the hair she has just pressed down is already lifting again.

One specific place: an office lift lobby first thing in the morning.

Regular morning light.

{FOCUS.format("her, her hair and her raised hand")}

{NOMARK}"""

P_C1_A = f"""Editorial photojournalism, natural and unstaged.

A school-age girl sitting on the floor of a hallway with her back against the wall, mid-way through an adult working a rigid plastic brush into a knot high at her crown. Under that force: her shoulders drawn up towards her ears, both hands flat on the floor either side of her taking her weight, her head held back against the pull, her knees pulled in. Face: chin down, mouth closed, eyes on the floor in front of her. {CHILD_FACE}

The knot is the evidence: a dense matted clump caught in the brush's teeth at the crown, the hair around it pulled tight into it from three directions, and loose broken strands drifted onto the floor beside her.

One specific place: a hallway by the front door on a school morning.

Neither is aware of the camera. Regular morning light.

{FOCUS.format("the two of them and the brush")}

{NOMARK}"""

P_C1_B = f"""Editorial photojournalism, natural and unstaged.

No person in the frame. The subject is a rigid plastic brush left on the hallway floor where the morning stopped, a dense matted clump of fine hair still gripped in its teeth at one end, the hair around the clump twisted tight into it, and loose broken strands drifted across the floorboards around it.

One specific place: a hallway by the front door on a school morning.

No subject, so no gaze. The frame looks straight down at the brush from standing height. Regular morning light.

{FOCUS.format("the brush and the knot still in it")}

{NOMARK}"""

P_C1_C = f"""Editorial photojournalism, natural and unstaged.

A school-age girl sitting sideways on a kitchen chair with one arm hooked over its back, mid-way through an adult working a rigid plastic brush into a knot high at her crown. Under that force: her free shoulder drawn up, the hooked arm pulling against the chair back, her head held back against the pull, one foot braced on a chair leg. Face: chin down, mouth closed, eyes on the table in front of her. {CHILD_FACE}

The knot is the evidence: a dense matted clump caught in the brush's teeth at the crown, the hair around it pulled tight into it from three directions, and loose broken strands on the table.

One specific place: a kitchen chair on a school morning.

Neither is aware of the camera. Regular morning light.

{FOCUS.format("the two of them and the brush")}

{NOMARK}"""

P_C2_A = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different mornings. ONE framing for every panel: the same bathroom shelf photographed square on from about half a metre back, the shelf across the lower third and a tiled wall behind. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiles and the same distance in all three panels. Variation on the props only: a toothbrush moved, a hair tie appearing, a folded flannel shifted.

The only thing that changes is which abandoned fix is on the shelf, and each is the plain unbranded version people already own. Panel one: a leave-in hair oil, the bottle half used and the outside of it tacky where it has been handled. Panel two: a silicone serum pump, its nozzle crusted and its collar left unlocked. Panel three: a plain trigger spray bottle, water still in it and a dried splash mark down one side. All three photographed at the same point in the routine, put back without being cleaned or straightened.

One neutral grade across every panel. Light differs only in exposure, never in warmth. No panel brighter, cleaner or tidier than another.

No product, no badges, no arrows and no text of any kind."""

P_C2_B = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different mornings. ONE framing for every panel: the same bathroom shelf photographed square on from about half a metre back, the shelf across the lower third and a tiled wall behind. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiles and the same distance in all three panels. Variation on the props only: a toothbrush moved, a hair tie appearing, a folded flannel shifted.

The only thing that changes is which tool is on the shelf. Panel one: a plain unbranded leave-in hair oil, common and in good condition. Panel two: a plain unbranded trigger spray bottle, common and in good condition. Panel three: the reference product. All three get identical exposure, identical background tidiness and identical framing generosity, and the difference must be visible in the objects themselves and never in how any panel is lit, styled, cropped or graded.

One neutral grade across every panel.

No badges, no arrows and no text of any kind."""

P_C2_C = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different mornings. ONE framing for every panel: the same corner of a bedroom chest of drawers photographed square on from about half a metre back, the top surface across the lower third and a plain wall behind. It reads as one shot taken three times, never as three different shots.

The same surface, the same wall and the same distance in all three panels. Variation on the props only: a hairband moved, a receipt appearing, a lamp base shifted at the edge.

The only thing that changes is which abandoned fix is on the surface, and each is the plain unbranded version people already own. Panel one: a leave-in hair oil, half used and tacky where it has been handled. Panel two: a silicone serum pump with a crusted nozzle. Panel three: a plain trigger spray bottle with a dried splash mark down one side. All three put back without being cleaned or straightened.

One neutral grade across every panel. Light differs only in exposure, never in warmth. No panel brighter, cleaner or tidier than another.

No product, no badges, no arrows and no text of any kind."""

P_C3_A = """A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

The same three hair strands per panel, at the same scale and the same side-on view in both, running from the lower left to the upper right and drawn in warm ivory with their surface scales visible along the length. A single comb tooth enters each panel from above, at the same angle and the same depth in both.

Left panel: the tooth is rigid and square-edged. It drags across the strands rather than passing between them, the surface scales lift and stand open along its path, and the three strands push apart from each other and rise away from the tooth. Right panel: the tooth is rounded and yields as it meets the same strands, passing between them; the scales lie flat and closed, and the three strands stay parallel and settled.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each measuring the gap between the outer two strands at the same point along their length, both starting from the same point in their panel. Red on the left where the gap is wide, blue on the right where the strands sit close. One filled solid disc badge in the top corner of each panel, the same diameter in both, with its glyph cut out of it: a red X on the left, a green check on the right. The glyph is the hole in the disc, never a symbol drawn on top.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_C3_B = """A 2D flat-vector medical illustration with flat fills and hard edges, no gradients. Not photography, not a 3D render.

The attached photo is the exact reference for the product.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

The same three hair strands per panel, at the same scale and the same side-on view in both, drawn in warm ivory with their surface scales visible along the length. A tooth enters each panel from above at the same angle and depth.

Left panel: a rigid square-edged tooth from an ordinary brush, dragging across the strands, the scales lifted open and the strands pushed apart. Right panel: the reference product's own rounded tooth, drawn at a size and angle where it is obviously that product, passing between the same strands with the scales lying flat and the strands parallel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each measuring the gap between the outer two strands at the same point, both starting from the same point in their panel. Red on the left, blue on the right. One filled solid disc badge in the top corner of each panel, same diameter, with its glyph cut out of it: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_C3_C = """A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

The same single hair strand per panel, at the same scale and the same side-on view in both, running left to right across the frame and drawn in warm ivory with its surface scales visible along the whole length. The strand fills most of the width so the scales are the subject.

Left panel: the scales are lifted and standing open along the strand, each one tilted away from the surface, and the strand's outline is ragged where they catch. Right panel: the same strand with the scales lying flat and closed against it, the outline continuous and smooth.

Marks: one dashed straight line per panel, identical in thickness and dash pattern, measuring the strand's outline height at the same point along its length in both, each starting from the same point in its panel. Red on the left where the lifted scales widen it, blue on the right where the outline is flat. One filled solid disc badge in the top corner of each panel, the same diameter in both, with its glyph cut out of it: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere."""

P_C4_A = """A 3D technical render.

The attached photo is the exact reference for the product.

A single product on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, no cast shadow on a floor. The product fills the frame and is the only object in it.

The reference product seen from the side at a slight three-quarter angle, its near half cut away along its length so the interior is open to view while the outline of the whole product stays unbroken and complete. The cut is a window into the body of the comb, never a piece removed from its silhouette.

Inside, exactly these components and nothing invented: the water reservoir occupying the upper body with its fill port at the top; the ultrasonic atomiser plate seated below it at the base of the reservoir; the six red LEDs set in a row under the bristle bed; the vibration motor behind them; and the battery filling the handle. Each is a distinct part with its own material finish, and each is the size it would really be inside a comb this size.

The product keeps its own reference colours throughout and carries no signal colour and no mark of any kind. The red of the LEDs is the LEDs themselves, lit, and nothing else in the frame is red.

Achromatic white and grey everywhere except the product's own colours.

No text, letters, labels, numbers, arrows, callouts or scale bars anywhere in the frame."""

P_C4_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her thirties in an open-collar blouse standing at a kitchen counter, holding the reference product against the crown of her own hair mid-pass, her gaze on the window rather than on the product. She stands to the right of the frame so the product and the hair around it stay clear to the camera.

An ultra-fine dry-touch mist is leaving the bristle bed and hanging in the air around the crown, lit from behind so it reads against the darker background, and the six red LEDs under the bristles are visible as small lit points through the hair. The mist is the subject of the frame.

One real kitchen filled to the edges with things that genuinely belong there. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border, showing one magnified detail the scene cannot carry at this distance: the atomiser plate under the bristle bed with the mist forming at its surface, close enough that the plate's texture and the individual droplets are both readable. It is a photograph in the same register as the scene and does not bleed into it, linked to the product by proximity alone with no arrow and no glow border.

No mark of any kind appears anywhere in the frame."""

P_C4_C = """A 3D technical render.

The attached photo is the exact reference for the product.

A single product on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, no cast shadow on a floor. The product fills the frame and is the only object in it.

The reference product seen from directly above with the bristle bed facing the camera, its near surface cut away across the bed so the interior beneath the bristles is open to view while the outline of the whole product stays unbroken and complete. The cut is a window into the body of the comb, never a piece removed from its silhouette.

Inside, exactly these components and nothing invented: the six red LEDs set in a row under the bristle bed; the ultrasonic atomiser plate beside them with its outlet passing up between the bristles; the reservoir behind both; and the retracting carrier the bristles are mounted on, shown seated in its normal position. Each is a distinct part with its own material finish, and each is the size it would really be inside a comb this size.

The product keeps its own reference colours throughout and carries no signal colour and no mark of any kind. The red of the LEDs is the LEDs themselves, lit, and nothing else in the frame is red.

Achromatic white and grey everywhere except the product's own colours.

No text, letters, labels, numbers, arrows, callouts or scale bars anywhere in the frame."""

P_C5_A = f"""A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A school-age girl sitting in a kitchen chair on a bright weekday morning while a woman in her thirties draws the reference product down through the back of her hair in one unbroken pass. Neither is braced against anything and neither is holding the other still. The girl's hands rest loose in her lap and she is looking off towards the window. {CHILD_FACE} Her face is settled and a small involuntary smile has arrived on its own.

The hair is the evidence: the length falling in one direction with an even surface, the halo gone from the crown, the section already passed lying flat against the section still to come.

The reference product is in the woman's hand, in the hair, doing the thing the section describes.

One real kitchen filled to the edges with things that genuinely belong there. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

No inset, no panel and no reserved layer anywhere in the frame. No mark of any kind."""

P_C5_B = f"""A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A school-age girl standing at a kitchen counter on a bright weekday morning, drawing the reference product through the length of her own hair in one unbroken pass, both hands her own and nobody else's on her. Nothing is held against her, nothing is braced, nothing is covered. Her chin is up, her shoulders are down and back, she is looking off towards the window rather than at the camera. {CHILD_FACE} A small involuntary smile has arrived on its own.

The hair is the evidence: the length falling in one direction with an even surface, the halo gone from the crown, one section still lifting slightly where she has not reached yet.

The reference product is in her own hand, in her hair, being used.

An ordinary family kitchen mid-morning, nothing tidied and nothing arranged.

Even natural daylight, bright, soft shadows, plain and unglamorous.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text."""

P_C5_C = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her thirties in an open-collar blouse sitting at a kitchen table in front of a closed laptop, settled back with her weight even and both hands loose on the table, her gaze on the window rather than at the product. She sits to the right of the frame so her hair and the product stay clear to the camera.

The hair is the evidence: it falls in one direction with an even surface, the halo is gone from the crown, and nothing is lifting or clinging to her collar.

The reference product rests on the table beside the laptop, near the camera and turned so its face can be read, the way it was put down after a pass rather than placed for the picture.

One real kitchen filled to the edges with things that genuinely belong there. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

No inset, no panel and no reserved layer anywhere in the frame. No mark of any kind."""

P_HT_A = """A 3D technical render.

The attached photo is the exact reference for the product.

Three equal panels stacked one above the other, each the full width of the frame, divided by single thin horizontal lines. Each panel is a full render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, no cast shadow on a floor.

The same reference product in all three panels, the same object at the same scale from the same three-quarter angle, and a pair of featureless matte white hands operating it, no arms beyond the wrist and no body.

Panel one: the fill port at the top of the handle is open and a thin stream of clear water is entering it from a small jug held in the second hand. Panel two: the product is upright against a section of hair with the mist leaving the bristle bed as a fine cloud and the six red LEDs lit under the bristles, moving from the tips upward. Panel three: one thumb presses the retract button on the handle and the bristle carrier has lifted clear of the bed, a loose clump of shed hair pushed up off the teeth and lifting away.

The product keeps its own reference colours in every panel. Achromatic white and grey everywhere else.

No text, letters, labels, numbers, arrows or step markers anywhere in the frame."""

P_HT_B = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal panels stacked one above the other, each the full width of the frame, thin white gutters, no outer border.

The attached photo is the exact reference for the product.

Shot by one person on a phone across one morning. ONE framing for every panel: the same bathroom shelf and basin edge photographed square on from about half a metre back, the shelf across the lower third. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiles and the same distance in all three panels. Variation on the props only: a toothbrush moved, a hair tie appearing, a flannel refolded.

The only thing that changes is where the product is in its routine. Panel one: standing on the shelf with its fill port open and a glass of water beside it. Panel two: lying on the basin edge with the mist still hanging in the air above the bristle bed and the LEDs lit. Panel three: standing on the shelf with the bristle carrier retracted and a small clump of shed hair lifted clear of the teeth.

One neutral grade across every panel. Light differs only in exposure, never in warmth.

No people, no hands, no badges, no arrows and no text of any kind."""

P_HT_C = """A 3D technical render.

The attached photo is the exact reference for the product.

Three equal panels stacked one above the other, each the full width of the frame, divided by single thin horizontal lines. Each panel is a full render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, no cast shadow on a floor.

The same reference product in all three panels, the same object at the same scale, and a pair of featureless matte white hands operating it, no arms beyond the wrist and no body. The camera is closer than a product shot: the product fills most of each panel and the action is readable at a glance.

Panel one: seen from the side with the fill port open at the top of the handle and clear water entering it. Panel two: seen from the side against a section of hair, the mist leaving the bristle bed as a fine cloud and the six red LEDs lit under the bristles. Panel three: seen from above with a thumb on the retract button and the bristle carrier lifted, a loose clump of shed hair pushed clear of the teeth.

The product keeps its own reference colours in every panel. Achromatic white and grey everywhere else.

No text, letters, labels, numbers, arrows or step markers anywhere in the frame."""


def snapshot(mode_line, scene, light, anchor, camera):
    return f"""A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

{mode_line}

{scene} — the mess stays, nothing tidied, nothing added for the picture. {light}, no other light.

One incidental owner object and no more: {anchor}.

{camera}; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture."""


P_S0 = snapshot(
    "The product mid-use, photographed by its owner looking down at their own hand: the "
    "reference comb drawn through the ends of their own hair, no face in shot.",
    "An ordinary bedroom corner photographed exactly as found early on a weekday",
    "Cool early daylight through a gap in the curtains",
    "a charging cable trailing off the bedside table",
    "Framing tilted and a little too close, taken at arm's length")

P_S1 = snapshot(
    "The product simply sitting where it now lives: the reference comb on a bathroom shelf "
    "beside the basin, nobody in the picture at all.",
    "An ordinary family bathroom photographed exactly as found in the middle of the day",
    "Flat overcast daylight through frosted glass",
    "a child's toothbrush standing in a beaker",
    "Framing off-centre and taken from standing height looking down at the shelf")

P_S2 = snapshot(
    "The product mid-use in a car, photographed by its owner from the driver's seat: the "
    "reference comb held up against the side of their hair in the rear-view mirror's "
    "reflection, no face readable.",
    "An ordinary parked car photographed exactly as found on a grey afternoon",
    "Flat daylight through the windscreen",
    "a parking permit clipped to the visor",
    "Framing close and crooked, taken one-handed from the seat")

P_S3 = snapshot(
    "The opened box and its contents as the owner has just left them: the reference comb out "
    "of its packaging on a kitchen table with the flattened box and a Type-C cable pushed to "
    "one side. Nobody in the picture at all.",
    "An ordinary kitchen photographed exactly as found in the evening",
    "Warm yellow light from a single ceiling fitting",
    "a fruit bowl at the edge of the table",
    "Framing slightly tilted, taken from standing height about half a metre back")

P_S4 = snapshot(
    "The product's retracted teeth held open over a bin, photographed by its owner with one "
    "thumb on the button and a clump of shed hair lifting clear of the bristles, no face in "
    "shot.",
    "An ordinary utility room photographed exactly as found at the weekend",
    "Hard overhead light from a single bare fitting",
    "a laundry basket half out of frame",
    "Framing very close and slightly out of square, taken looking straight down")

P_S5 = snapshot(
    "The product mid-use at a desk, photographed by its owner over their own shoulder: the "
    "reference comb resting against the crown of their hair with a laptop open in front of "
    "them, no face in shot.",
    "An ordinary spare-room desk photographed exactly as found late morning",
    "Bright window daylight from one side",
    "a mug on a coaster beside the laptop",
    "Framing crooked and taken from very close over the shoulder")

# ---------------------------------------------------------------- gif briefs

BRIEF_C1 = """A shot of a rigid brush being drawn down into a knot at the back of a child's head. The teeth catch, the hair around the knot pulls tight and lifts with the brush, and her shoulders come up as it holds."""

ALT_C1 = """A shot of the same brush pulled slowly through a hank of fine hair held in one hand, no child in the frame. The teeth reach a knot, the strands bunch and tighten into it, and the whole hank travels with the brush."""

BRIEF_HT = """A shot of the comb on a shelf. Water fills the port at the top of the handle, then it lifts to a section of hair and the mist starts, then a thumb presses the button and the teeth retract, pushing a clump of shed hair clear."""

ALT_HT = """A shot of the comb held in one hand over a bin. A thumb presses the button, the teeth rise off the bed and a clump of trapped hair is pushed clear and drops away, then the teeth seat back down."""

BRIEF_C5 = """A shot of a woman drawing the comb down through a seated child's hair in one unbroken pass. The comb runs from crown to ends without catching, the child's shoulders stay down, and the hair falls and settles behind it."""

ALT_C5 = """A shot of the child drawing the comb through her own hair at a counter. She runs it from the ends upward, the comb passes without snagging, and she lifts it away and starts a second pass on her own."""

RESERVE_C3 = """A shot of a rigid tooth drawn across three fine strands. The surface scales lift and stand open along its path and the strands push apart from each other, then a rounded tooth passes between them and they settle back parallel."""

RESERVE_C4 = """A shot of the comb's bristle bed with the water window behind it. Fine bubbles rise off the atomiser plate, an ultra-fine mist builds between the teeth and lifts away in a slow steady cloud."""


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
    "PRECONDITION, and it is not optional: these six photo tiles sit inside the SAME section "
    "element as six attributed quotes carrying reviewer names, five-star rows and Verified "
    "labels — measured on this export, zero closing tags between the grid and the quotes, "
    "twelve Verified labels and sixty star icons. 05-social-snapshot's authenticity fence "
    "forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified "
    "badge. Use real customer photographs, or move the photo grid out of the attributed "
    "block, or drop the names, stars and verified labels — before rendering any of these. "
    "Seventh routed page in a row to breach it, so it is a template defect and not a page one.")

CROP_16_9 = (
    "RATIO: this type declares 16:9 as its only ADR-016-legal ratio and the slot is 1:1, so "
    "the layout centre-crops about 44% of the width. The frame is composed for it — the "
    "subject sits centred and close, and nothing the argument needs lives in the outer "
    "thirds. Every option at this slot has the same cost because the cell holds one type.")

SLOTS = []

SLOTS.append({
    "slot_id": "hero.image", "section_role": "hero",
    "asset": "125-01-hero-pain-scene.png",
    "placement": "advertorial header, under the headline and above the byline",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides, close to verbatim. The headline calls it the morning static trap and "
        "hero.intro puts her at the bathroom sink at a quarter to seven with every stroke "
        "turning frizz into a cloud of static. 01-pain-scene --candid is written for physical "
        "pain in a moment nobody would choose to be seen in, and A plays that as one action. "
        "B moves to the confront gaze, which the type reserves for appearance and self-image "
        "— and that beat has its own slot at content.items.0, so spending it here would "
        "duplicate it. C moves to the hallway mirror on the way out. RATIO: 16:9 declared and "
        "16:9 slot, so nothing is cropped here — the only slot on this page where that is "
        "true. PRODUCT PRESENCE: none, correctly; the type forbids it. PROMPT RISK: {chars} "
        "characters against this type's measured band of 1669 to 1880.",
    "options": [
        opt("A", "01-pain-scene", "baseline", "16:9", P_HERO_A,
            "The page's opening scene as one action: a dry brush dragged down through her own "
            "hair at the sink, the halo standing up behind it. The evidence is the hair "
            "itself, which is rank 1 under G9.",
            variant="candid", axes={"gaze": "candid"}),
        opt("B", "01-pain-scene", "axis: gaze=confront", "16:9", P_HERO_B,
            "The same moment in the type's other gaze, holding the viewer's eye. The "
            "advertorial hero cell holds one type and the gates leave no second, so the "
            "honest variation here is the axis.",
            variant="confront", axes={"gaze": "confront"},
            notes="Picking B duplicates the gaze recommended at content.items.0, which is "
                  "where the appearance beat actually lives; that slot would then fall to its "
                  "own B."),
        opt("C", "01-pain-scene", "execution: the hallway mirror on the way out", "16:9",
            P_HERO_C,
            "Same type and same axis, moved to the last mirror before the door — the moment "
            "the copy's school-run pressure actually bites.",
            variant="candid", axes={"gaze": "candid"}),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The slot's declared job is recognition — a cold reader seeing themselves "
                  "in a held state. Every routed page has refused its hero on this ground; "
                  "refused here for consistency with them.",
    },
})

SLOTS.append({
    "slot_id": "content.items.0.image", "section_role": "problem-agitation",
    "asset": "125-02-content0-pain-scene.png",
    "placement": "body item 1",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides and the type's own trigger names it. This section's cost is APPEARANCE — "
        "a manager noticing her webcam angle while she keeps smoothing flyaways — and "
        "01-pain-scene reserves --confront for exactly that: appearance, self-image and daily "
        "frustration where the mirror moment IS the moment. A is that. B is the same beat "
        "played candid, which loses the being-seen half. C moves it to the office lift lobby. "
        "PAGE LEGALITY: this is Step 4 rung 4 — 01-pain-scene runs at the hero as well, and "
        "the two differ on the gaze AXIS rather than only on staging. PROMPT RISK: {chars} "
        "characters.",
    "options": [
        opt("A", "01-pain-scene", "rung 4: same type, gaze axis and beat differ", "16:9",
            P_C0_A,
            "The webcam beat: hands still up in her hair a minute before the call, looking "
            "straight down the lens the way the camera on the laptop would see her.",
            variant="confront", axes={"gaze": "confront"},
            notes=CROP_16_9 + " Rung 4 of Step 4's ladder: another execution of a type "
                  "already recommended at hero.image, differing on the gaze axis. Declared "
                  "here rather than left to look like an oversight."),
        opt("B", "01-pain-scene", "axis: gaze=candid", "16:9", P_C0_B,
            "The same table and the same minute, played unaware — pressing both sides down "
            "while watching the screen rather than the lens.",
            variant="candid", axes={"gaze": "candid"},
            notes=CROP_16_9),
        opt("C", "01-pain-scene", "execution: the office lift lobby, not the kitchen table",
            "16:9", P_C0_C,
            "Same type and same axis, moved to where the being-seen actually happens — in the "
            "building, bag on the shoulder, before anyone has spoken to her.",
            variant="confront", axes={"gaze": "confront"},
            notes=CROP_16_9),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "A held state: hair that will not stay down is a condition rather than a "
                  "transition, and the section's argument is about being seen in it. Nothing "
                  "here changes over time that the still cannot assert.",
    },
})

SLOTS.append({
    "slot_id": "content.items.1.image", "section_role": "problem-agitation",
    "asset": "125-03-content1-pain-scene.png",
    "placement": "body item 2",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides. This is the child pain beat in the page's own words — rigid bristles "
        "snagging a crown knot, the bus missed, the daughter on the hallway floor — and "
        "01-pain-scene --candid is the type for physical pain in a moment nobody would choose "
        "to be seen in. A is that moment with G13 applied. B is the sanctioned fallback if A "
        "is refused: the same beat with nobody in frame, an execution this type already "
        "legislates and the ledger records twice. C moves it to a kitchen chair. G13: no "
        "private room, no age in years, and the face capped at effort — plus a NEGATIVE "
        "beside the cap, which the rule does not yet carry and which 1 of 3 renders needed on "
        "2026-08-24. PAGE LEGALITY: rung 4 again, and the third execution of this type on the "
        "page; the subject class here is a child rather than the narrator. PROMPT RISK: "
        "{chars} characters.",
    "options": [
        opt("A", "01-pain-scene", "rung 4: same type, child subject class", "16:9", P_C1_A,
            "The hallway floor, the crown knot, and an adult's brush in it. The knot is the "
            "evidence and the child's face carries effort and nothing more.",
            variant="candid", axes={"gaze": "candid"},
            notes=CROP_16_9 + " G13 BINDS: hallway rather than a private room, no age in "
                  "years, and the Face block capped at effort with an explicit negative. The "
                  "residual is the force inventory and the covert gaze, which the type "
                  "requires; three renders of this shape generated on 2026-08-24 without "
                  "refusal."),
        opt("B", "01-pain-scene", "subject class: object-only, nobody in frame", "16:9",
            P_C1_B,
            "The same beat with the brush and the knot still in it on the floor. It carries "
            "the argument without a person, and it cannot be refused.",
            variant="candid", axes={"gaze": "candid"},
            notes=CROP_16_9 + " THE SANCTIONED FALLBACK if A is refused. Note the argument "
                  "fault this frame must avoid: a loose ball of shed hair on a brush reads as "
                  "HAIR LOSS, which is not what this page argues, so the prompt names a "
                  "matted clump still gripped in the teeth with the surrounding hair twisted "
                  "into it. Two renders on 2026-08-24 came back reading as shedding."),
        opt("C", "01-pain-scene", "execution: a kitchen chair, not the hallway floor", "16:9",
            P_C1_C,
            "Same type and same subject class, moved to the chair the copy puts her in every "
            "other morning.",
            variant="candid", axes={"gaze": "candid"},
            notes=CROP_16_9),
    ],
    "gif": {
        "eligible": True,
        "form": "whole-frame",
        "kind": "cause",
        "type_id": "cause",
        "rung": "natural",
        "reason": "The section's claim is a snag happening — bristles catching a knot and the "
                  "hair pulling tight into it — which is a transition rather than a state. "
                  "The routed still already contains the force and the body it acts on, so "
                  "nothing is restaged: this is rung 1. The gif library's `cause` type names "
                  "exactly this shape, a tool failing on the thing it is used on.",
        "asset": "125-03-content1-pain-scene--brief.svg",
        "refs": "gifs-library/cause/ — no files filed yet; the folder card carries the law",
        "output": "advertorial-cause-massage-comb-spray-v02.webp",
        "ratio": "1:1",
        "duration_s": 3,
        "loop": "seamless loop",
        "brief": BRIEF_C1,
        "alt": ALT_C1,
        "delivery": "animated webp, loop-safe, under the size ceiling",
    },
})

SLOTS.append({
    "slot_id": "content.items.2.image", "section_role": "comparison",
    "asset": "125-04-content2-proof-lockedframe.png",
    "placement": "body item 3",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides, close to verbatim. 04-proof-lockedframe's use_when names \"the 'I tried "
        "three things' beat of an advertorial\", and this section is exactly three named "
        "things that were bought and abandoned: leave-in oils, silicone serums, a trigger "
        "spray bottle. --rivals keeps the product out of frame, which this beat requires. B "
        "swaps to --verdict, which puts the product in the last panel and answers a question "
        "the page has not asked yet — content.items.4 is where the product arrives. RATIO: "
        "1:1 declared and a 1:1 slot, nothing cropped. EVIDENCE: the locked three-panel form "
        "is this type's most-rendered execution. PRODUCT PRESENCE: none in A, correctly. "
        "PROMPT RISK: {chars} characters against a stated ceiling of 1800.",
    "options": [
        opt("A", "04-proof-lockedframe", "baseline", "1:1", P_C2_A,
            "One shelf, one framing, the three fixes the copy names, each photographed after "
            "it was given up on rather than staged.",
            variant="rivals",
            notes="Single-pass: the panels run handheld rather than strict, the route this "
                  "type's own capability gate records for a renderer that cannot composite "
                  "(ADR-021). --rivals is advertorial-legal and barred only on marketplace."),
        opt("B", "04-proof-lockedframe", "variant: --verdict, the product in the last panel",
            "1:1", P_C2_B,
            "The same shelf and the same discipline with the product resolving the sequence, "
            "under the fairness rule: it may win by physics and never by treatment.",
            variant="verdict",
            notes="Picking B introduces the product two sections earlier than the copy does, "
                  "and content.items.4's mechanism argument then lands second rather than "
                  "first. It also needs the reference photo attached, which A does not."),
        opt("C", "04-proof-lockedframe", "execution: a bedroom chest of drawers, not the "
            "bathroom shelf", "1:1", P_C2_C,
            "Same type and same variant on the other surface these things accumulate on.",
            variant="rivals",
            notes="Single-pass: panels run handheld (ADR-021)."),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "Three abandoned objects on a shelf is an inventory, not a change. Step 5c "
                  "refuses motion to a slot that reveals rather than changes, and nothing "
                  "here moves. Rung 2 was examined: restaging it as one fix failing in use "
                  "would re-argue the CAUSE that content.items.1 already carries, and ADR-037 "
                  "allows one loop per gif type per page.",
    },
})

SLOTS.append({
    "slot_id": "content.items.3.image", "section_role": "cause",
    "asset": "125-05-content3-cause-anatomy.png",
    "placement": "body item 4",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides, and the SCALE decides which version of the argument is drawable. The "
        "section names two mechanisms: friction charging the strands, and rigid teeth "
        "dragging through fibres rather than yielding to a knot. The first is molecular and "
        "has no picture; the second is at the scale of a tooth against a hair, where both "
        "objects are the same order of magnitude and a viewer can see the difference. A "
        "argues the second and lets the first follow from it. This is A13 applied before the "
        "fact rather than after: on 2026-08-24 six renders failed because a product and an "
        "anatomy were drawn at incompatible scales. C goes closer still, to one strand's "
        "surface. RATIO: 1:1 declared and a 1:1 slot. PROMPT RISK: {chars} characters against "
        "~2050 at three marks; A carries two.",
    "options": [
        opt("A", "02-cause-anatomy", "baseline", "1:1", P_C3_A,
            "A rigid tooth dragging across three strands against a rounded one passing "
            "between them, with the lifted scales and the gap between strands as the two "
            "marks. The culprit is the tooth, which is what the section indicts.",
            variant="diagnostic"),
        opt("B", "02-cause-anatomy", "axis: the product's own tooth in the corrected panel",
            "1:1", P_C3_B,
            "The same two panels in flat vector with the reference product's tooth doing the "
            "correcting instead of an unnamed rounded one.",
            notes="Picking B introduces the product one section earlier than the copy does, "
                  "and it needs the reference photo attached, which A does not."),
        opt("C", "02-cause-anatomy", "execution: one strand's surface, not three strands",
            "1:1", P_C3_C,
            "Same type and variant one step closer: a single strand filling the width with "
            "its scales lifted against the same strand with them lying flat.",
            variant="diagnostic"),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The argument IS temporal — scales lifting and strands repelling as a tooth "
                  "passes — and this slot earns motion on it. It is refused by the BUDGET and "
                  "not by the argument: the gif type would be `cause`, and content.items.1 "
                  "already carries the page's one `cause` loop (ADR-037, one loop per gif "
                  "type per page). Listed in motion.reserves as that loop's substitute.",
    },
})

SLOTS.append({
    "slot_id": "content.items.4.image", "section_role": "mechanism",
    "asset": "125-06-content4-mechanism-xray.png",
    "placement": "body item 5",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT plus hard render evidence against the cell's other type. This section is a "
        "COMPONENT LIST — atomiser, cushion base, rounded bristles, six LEDs, vibration motor "
        "— and 03-mechanism-xray is the type that opens a gadget to show its real internal "
        "components. The cell's other type, 03-mechanism-ghostbody, is legal by the attribute "
        "gates and is NOT recommended: six renders of it on this exact product failed on "
        "2026-08-21, all logged, and ADR-038 records why the cutaway cannot hold this "
        "product's argument at any scale. B argues the mist instead, which G8 makes the "
        "primary subject wherever the product emits something visible. RATIO: 1:1 declared "
        "and a 1:1 slot. PROMPT RISK: {chars} characters.",
    "options": [
        opt("A", "03-mechanism-xray", "baseline", "1:1", P_C4_A,
            "The comb opened along its own length: reservoir, atomiser plate, LED row, "
            "vibration motor, battery. The subject is the product, so the scale problem that "
            "sank the body cutaways does not arise here.",
            notes="03-mechanism-ghostbody is the cell's other type and is legal by the gates. "
                  "It is not offered: six renders on this product failed on 2026-08-21 and "
                  "ADR-038 records the reason. Refusing a type the evidence has retired is "
                  "Stage 2 doing its job."),
        opt("B", "06-relief-hero", "type: 06-relief-hero --detail, the mist as the subject",
            "1:1", P_C4_B,
            "The mechanism as a photograph rather than a cutaway, with the mist backlit as "
            "the primary subject and the atomiser plate magnified in a corner inset. G8 makes "
            "a visible emission the frame's subject wherever one exists.",
            variant="detail", axes={"register": "commercial", "inset_mode": "detail"},
            notes="Picking B displaces 06-relief-hero from content.items.5, whose recommended "
                  "option is the page's only relief frame; that slot would fall to its own B."),
        opt("C", "03-mechanism-xray", "execution: from above, through the bristle bed", "1:1",
            P_C4_C,
            "Same type opened on the other axis, which puts the LED row and the atomiser "
            "outlet in the same view as the bristles they sit under.",
            ),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The argument IS temporal — mist forming at a plate and carried out through "
                  "the bristles is a thing happening — and this slot earns motion on it. It "
                  "is refused by the BUDGET and not by the argument: the `content` section "
                  "runs to six items so ADR-032 allows it two loops provided they are not "
                  "adjacent, and items.1 with items.5 is the only pair that is both "
                  "non-adjacent and covers both halves of the motion floor. Listed in "
                  "motion.reserves as items.5's substitute.",
    },
})

SLOTS.append({
    "slot_id": "content.items.5.image", "section_role": "outcome",
    "asset": "125-07-content5-relief-hero.png",
    "placement": "body item 6",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT plus a type boundary found on 2026-08-24. The section closes on the daughter "
        "sitting happily through her bedhead without a whimper and the narrator's own routine "
        "taking two minutes. 06-relief-scene is normally the closing type for an advertorial, "
        "and it is offered at B rather than recommended: its `product` PART requires the "
        "product to STAND IN THE FRAME AS ITS OWN OBJECT near the camera, measured across "
        "twelve renders with everything held, inside or edge-on failing. A COMB CANNOT SATISFY "
        "THAT AND ALSO BE THE THING PRODUCING THE RELIEF, and two renders on 2026-08-24 "
        "resolved the contradiction by dropping the product entirely. 06-relief-hero has no "
        "such rule and takes the product in hand, so A recommends it. RATIO: relief-hero "
        "declares 1:1 and the slot is 1:1; relief-scene declares no 1:1 at all, which is a "
        "second reason B costs something. PROMPT RISK: {chars} characters.",
    "options": [
        opt("A", "06-relief-hero", "baseline", "1:1", P_C5_A,
            "The morning the copy describes: the comb drawn through the child's hair in one "
            "pass, nobody holding anybody still, the halo gone. The product is in the frame "
            "doing the thing.",
            axes={"register": "commercial", "inset_mode": "none"}),
        opt("B", "06-relief-scene", "type: 06-relief-scene, the child using it herself",
            "16:9", P_C5_B,
            "The closing-frame type, played as the child doing it for herself — which is what "
            "the copy's last line actually says.",
            notes="RATIO: 06-relief-scene declares 16:9, 4:3 and 3:4 and no 1:1, so this "
                  "renders at 16:9 into a 1:1 slot and the layout centre-crops about 44% of "
                  "the width. AND THE TYPE'S PRODUCT RULE HAS NO POSITION FOR A HAND TOOL: it "
                  "requires the product to stand as its own object near the camera, which a "
                  "comb in use cannot do. Two renders on 2026-08-24 dropped the product "
                  "rather than resolve it. Offered because it is the cell's second type and "
                  "the copy supports it, not because it is safe."),
        opt("C", "06-relief-hero", "execution: the narrator, not the child", "1:1", P_C5_C,
            "Same type, the other half of the section: her own two-minute routine done, the "
            "laptop closed, the product put down beside it.",
            axes={"register": "commercial", "inset_mode": "none"}),
    ],
    "gif": {
        "eligible": True,
        "form": "whole-frame",
        "kind": "relief",
        "type_id": "relief",
        "rung": "natural",
        "reason": "The `relief` type earns motion only where the motion IS the thing the "
                  "problem used to block, and this page opens on a child who could not be "
                  "brushed without tears. One unbroken pass through her hair is that "
                  "movement returned. Nothing is restaged — the routed still already contains "
                  "the pass — so this is rung 1.",
        "asset": "125-07-content5-relief-hero--brief.svg",
        "refs": "gifs-library/relief/ — no files filed yet; the folder card carries the law",
        "output": "advertorial-relief-massage-comb-spray-v02.webp",
        "ratio": "1:1",
        "duration_s": 3,
        "loop": "seamless loop",
        "brief": BRIEF_C5,
        "alt": ALT_C5,
        "delivery": "animated webp, loop-safe, under the size ceiling",
    },
})

SLOTS.append({
    "slot_id": "howto.image", "section_role": "how-to-use",
    "asset": "125-08-howto-use-sequence.png",
    "placement": "how-to card, beside the three numbered steps",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT, and this is the first page of this product where the cell is not empty. "
        "03-use-sequence needs `multi_step_usage: true` and this product has three named "
        "steps in its own copy — fill the reservoir, brush and mist from the tips up, click "
        "to retract and release trapped hair. On the seat-cushion pages the same cell was "
        "gated out and the slot had to be filled from an adjacent step; here the type is "
        "legal on its own terms. A renders the three steps as the type asks. B moves them to "
        "documentary photography of the product alone, which loses the hands and therefore "
        "the answer to \"will I manage to use this\". RATIO: 1:1 declared and a 1:1 slot. "
        "PROMPT RISK: {chars} characters.",
    "options": [
        opt("A", "03-use-sequence", "baseline", "1:1", P_HT_A,
            "Three stacked panels, one object, matte white hands: fill, mist from the tips "
            "up, retract and release. The third step is the one no competitor has and it "
            "closes the sequence.",
            ),
        opt("B", "04-proof-lockedframe", "type: 04-proof-lockedframe, the product alone "
            "across the routine", "1:1", P_HT_B,
            "The same three moments as a locked documentary frame on a real shelf, which "
            "trades the instructional read for an evidentiary one.",
            variant="timelapse",
            notes="Picking B displaces 04-proof-lockedframe from content.items.2, whose "
                  "recommended option is the page's only rivals frame. Single-pass: panels "
                  "run handheld (ADR-021)."),
        opt("C", "03-use-sequence", "execution: closer, the action readable at a glance",
            "1:1", P_HT_C,
            "Same type and same three steps with the camera in tighter, so each panel is the "
            "action rather than the object.",
            ),
    ],
    "gif": {
        "eligible": True,
        "form": "whole-frame",
        "kind": "use",
        "type_id": "use",
        "rung": "natural",
        "reason": "Three steps in order is the definition of a sequence, and the routed still "
                  "already stages all three. Nothing is restaged, so this is rung 1. It is "
                  "also the FIRST `use` loop this library has routed: the type was gated out "
                  "on every earlier page of this product family by `multi_step_usage: false`, "
                  "and this product has three named steps in its own copy. `howto` is its own "
                  "section with one slot, so it carries this loop without touching the "
                  "spacing rule in `content`.",
        "asset": "125-08-howto-use-sequence--brief.svg",
        "refs": "gifs-library/use/ — no files filed yet; the folder card carries the law",
        "output": "advertorial-use-massage-comb-spray-v02.webp",
        "ratio": "1:1",
        "duration_s": 4,
        "loop": "seamless loop",
        "brief": BRIEF_HT,
        "alt": ALT_HT,
        "delivery": "animated webp, loop-safe, under the size ceiling",
    },
})

_WALL = [
    ("125-09-social-snapshot.png", "photo grid, tile 1 of 6", P_S0,
     "bedroom corner · own hair mid-use, hand in shot · cool early daylight · arm's length · "
     "in-use mode",
     "The quote about a daughter who now brushes her own hair happily needs a first-person "
     "morning frame, and this is the only tile shot at arm's length."),
    ("125-10-social-snapshot.png", "photo grid, tile 2 of 6", P_S1,
     "family bathroom · shelf beside the basin · at rest, nobody present · flat overcast "
     "daylight · standing height looking down",
     "The sceptic-with-fine-frizzy-texture quote. At-rest mode with nobody present, and the "
     "only tile that shows where the product lives rather than what it does."),
    ("125-11-social-snapshot.png", "photo grid, tile 3 of 6", P_S2,
     "parked car · rear-view mirror reflection · in use, no face readable · flat daylight "
     "through glass · one-handed from the seat",
     "The quick-morning-routine quote, taken where a quick routine actually happens. The only "
     "tile with a reflection and the only one outside the home."),
    ("125-12-social-snapshot.png", "photo grid, tile 4 of 6", P_S3,
     "kitchen table · opened box and cable · just unboxed, nobody present · warm ceiling "
     "light · half a metre back at standing height",
     "The whole-family and Type-C quote. The arrival moment none of the other tiles cover, "
     "and the only warm-lit frame in the set."),
    ("125-13-social-snapshot.png", "photo grid, tile 5 of 6", P_S4,
     "utility room · retracted teeth over a bin · in use, thumb on the button · hard overhead "
     "light · very close looking straight down",
     "The retractable-teeth cleaning quote, which no other tile can carry. The only hard-lit "
     "tile and the closest framing in the set."),
    ("125-14-social-snapshot.png", "photo grid, tile 6 of 6", P_S5,
     "spare-room desk · comb at the crown with a laptop open · in use, over the shoulder · "
     "bright window daylight · very close over the shoulder",
     "The sensitive-scalp quick-refresh quote, placed at the desk the page's own narrator "
     "works from."),
]

for _i, (_asset, _place, _prompt, _varies, _why) in enumerate(_WALL):
    SLOTS.append({
        "slot_id": f"social.photos.{_i}.image", "section_role": "social-proof",
        "asset": _asset, "placement": _place,
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis":
            "ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of "
            "variation, so the six tiles differ from each other rather than from a B and a C. "
            f"This tile's place in the set: {_varies}. {_why} PRODUCT PRESENCE: the reference "
            "product is the subject of every tile. PROMPT RISK: {chars} characters against a "
            "stated ceiling of 1800.",
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
    ("offer.image", "Closing offer card: a standard product shot, out of library scope "
     "(cross-slot rule 6)."),
    ("header.logo", "Brand mark."),
    ("footer.logo", "Brand mark."),
    ("hero.author_avatar",
     "A portrait of a named person. No library type produces one, and generating a face to "
     "sit under a real byline is a disclosure decision rather than an image one — the "
     "`author` row of the slot-rules table is empty on every channel, deliberately."),
    ("social.items.0.avatar", "A portrait of a named reviewer. Same reason."),
    ("social.items.1.avatar", "A portrait of a named reviewer. Same reason."),
    ("social.items.2.avatar", "A portrait of a named reviewer. Same reason."),
    ("social.items.3.avatar", "A portrait of a named reviewer. Same reason."),
    ("social.items.4.avatar", "A portrait of a named reviewer. Same reason."),
    ("social.items.5.avatar", "A portrait of a named reviewer. Same reason."),
    ("comments.items.0.avatar", "A portrait of a named commenter. Same reason."),
    ("comments.items.0.reply_avatar", "A portrait of a named commenter. Same reason."),
    ("comments.items.1.avatar", "A portrait of a named commenter. Same reason."),
    ("comments.items.2.avatar", "A portrait of a named commenter. Same reason."),
    ("comments.items.2.reply_avatar", "A portrait of a named commenter. Same reason."),
    ("comments.items.3.avatar", "A portrait of a named commenter. Same reason."),
    ("comments.items.4.avatar", "A portrait of a named commenter. Same reason."),
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
            "slot_id": "content.items.3.image",
            "substitutes_for": "content.items.1.image",
            "type_id": "cause",
            "group": "working",
            "rung": "re-execution",
            "brief": RESERVE_C3,
            "why_held_back":
                "Same gif type as content.items.1, and ADR-037 allows one loop per gif type "
                "per page, so the two compete rather than add. items.1 holds it because the "
                "copy's own breaking point is there and the loop is rung 1 at that slot. "
                "Promoting this one puts the section's loops at items.3 and items.5, still "
                "two and still not adjacent, so the spacing rule holds. Its still is a "
                "two-panel illustration, so it arrives at rung 2 either way.",
        },
        {
            "slot_id": "content.items.4.image",
            "substitutes_for": "content.items.5.image",
            "type_id": "mechanism",
            "group": "working",
            "rung": "re-execution",
            "brief": RESERVE_C4,
            "why_held_back":
                "Refused by SPACING, not by the argument. The `content` section runs to six "
                "items so ADR-032 allows it two loops provided they are not adjacent, and "
                "items.1 with items.5 is the pair that also satisfies the coverage "
                "preference. This slot can only substitute for items.5, because replacing "
                "items.1 would leave loops at items.4 and items.5 side by side. Promoting it "
                "costs the `result` half of the coverage pair and gains a second `working` "
                "loop, which is a real trade rather than a free swap.",
        },
    ],
    "notes": [
        "Three loops against a floor of 2, so margin is 1. They sit in two different "
        "sections: two in `content`, which runs to six items and so may carry two under "
        "ADR-032 provided they are not adjacent, and one in `howto`, which is its own "
        "section with a single slot.",
        "THE ARRANGEMENT IS FORCED BY TWO RULES AT ONCE. Among the loop-capable slots in "
        "`content` — items.1, items.3, items.4 and items.5 — items.1 and items.3 are both "
        "gif type `cause` and ADR-037 allows one per page, which removes items.3. That "
        "leaves items.1, items.4 and items.5, of which items.4 and items.5 are adjacent. "
        "items.1 with items.5 is the only pair that is both non-adjacent and covers both "
        "halves of the motion floor.",
        "ALL THREE ARE RUNG 1, which no page in this library has managed before. Pages 77 and "
        "104 delivered nothing but rung-2 re-executions and page 120 managed one. The reason "
        "is the product: a comb is used in a movement, so the still that argues the beat "
        "already contains the movement, and nothing has to be restaged to film it.",
        "COVERAGE PAIR MET: cause (working) at content.items.1, use (working) at howto.image, "
        "relief (result) at content.items.5.",
        "ALL THREE ARE WHOLE-FRAME. No slot that earned motion has a recommended option whose "
        "skeleton legislates a layer a loop could occupy: 01-pain-scene bans insets outright, "
        "03-use-sequence is a panel stack, and 06-relief-hero's recommended option here runs "
        "`inset_mode: none`. Its option B carries a `--detail` layer, but a gif verdict "
        "follows the recommendation and B is not recommended.",
        "howto.image is the FIRST `use` loop this library has routed. The type was gated out "
        "on every seat-cushion page by `multi_step_usage: false`; this product has three "
        "named steps in its own copy, so both the still type and the gif type become "
        "available for the first time. The brief runs three beats in order, which is inside "
        "`use`'s declared band of one to four.",
        "Review grid: 0 tiles — the six-type gif set carries no `social` type.",
    ],
}

COVERAGE = {
    "covered": [
        "step 1 pain — 01-pain-scene at hero.image, again on the gaze axis at "
        "content.items.0.image, and again with a child subject at content.items.1.image",
        "step 2 cause — 02-cause-anatomy --diagnostic at content.items.3.image",
        "step 3 mechanism — 03-mechanism-xray at content.items.4.image",
        "step 3 how-to — 03-use-sequence at howto.image, the first time this cell has been "
        "fillable on this product",
        "step 4 proof — 04-proof-lockedframe --rivals at content.items.2.image",
        "step 5 social — 05-social-snapshot across all six tiles",
        "step 6 relief — 06-relief-hero at content.items.5.image",
    ],
    "absent": [
        "step 5 personas — 05-persona-grid declares no advertorial channel. The six review "
        "quotes name six distinct user classes the page never shows — a parent, a sceptic "
        "with fine hair, a sensitive scalp, someone cleaning the teeth out, a no-wash-day "
        "user and a whole family — which IS a gap, but no type on this channel fills it. The "
        "review wall carries it instead, which is why the six tiles are built around those "
        "six situations",
        "step 2 symptom breadth — 02-symptom-rail declares no advertorial channel, and the "
        "page makes no breadth claim, so this is not a gap",
    ],
    "notes": [
        "Awareness stage read from the page's own copy: SOLUTION-AWARE. The problem sections "
        "list what the reader has already bought and abandoned — leave-in oils, silicone "
        "serums, a trigger spray bottle — rather than establishing that the problem exists, "
        "and a named expert arrives to explain the mechanism rather than to prove there is "
        "one.",
        "ONE-TYPE-ONCE IS BREACHED TWICE, deliberately and under Step 4 rung 4. 01-pain-scene "
        "runs three times: at the hero as physical pain, at content.items.0 on the confront "
        "gaze as an appearance cost, and at content.items.1 with a child as the subject. The "
        "advertorial cells for `hero` and `problem-agitation` hold that one type between "
        "them, the page carries three distinct pain beats, and the three executions differ on "
        "subject, on axis and on beat rather than only on staging.",
        "THE MECHANISM CELL'S FIRST TYPE IS REFUSED ON RENDER EVIDENCE, NOT ON A GATE. "
        "03-mechanism-ghostbody is legal here — `body_contact` is true — and it is not "
        "offered at any position. Six renders of it on this exact product failed on "
        "2026-08-21 and ADR-038 records why: a scalp has no drawable thickness at head scale, "
        "and three of the product's four claims live on the hair shaft where no body cutaway "
        "reaches. Stage 2 is judgement, and refusing a type the ledger has retired is what "
        "that judgement is for.",
        "G13 BINDS AT content.items.1 AND content.items.5, the two frames carrying a child. "
        "No private room, no age in years, and the face capped at effort — plus an explicit "
        "NEGATIVE beside the cap, which the published rule does not yet carry. That addition "
        "is evidence rather than invention: on 2026-08-24 one of three renders written to the "
        "positive cap alone came back a clear wince, because a positive instruction with "
        "nothing forbidden is resolved by the model from scene logic.",
        "EVERY LINEAR SLOT CARRIES THREE OPTIONS. One-type-once binds the recommended SET "
        "rather than the option pool, so a B may carry a type recommended elsewhere; each one "
        "names the slot it would displace. The six review tiles carry one option each "
        "(ADR-022).",
    ],
}

PAGE_NOTES = [
    "SOURCE: ~/Downloads/content-library-local/"
    "landing-page-how-i-ended-morning-bedhead-and-detangling-tears-without-damaging-heat.json"
    ", page id 125, lpTypeId advertorial. `imageBriefs` is NULL, so htmlCompiled is the only "
    "slot source — the case earlier pages established it can carry.",
    "THE PROMPTS ARE WRITTEN TO THE OWNER'S LEAN SPEC, confirmed on 2026-08-24 across seven "
    "renders. No `cinematic film still`, no Key/Fill/Rim/Deep-shadow block, no grade line and "
    "no three-to-four object clutter list. One focus clause replaces the list, and the model "
    "supplies the domestic texture from `nothing is arranged and nothing is tidied` on its "
    "own — measured 7 of 7, including two renders where it supplied MORE clutter than the "
    "brief wanted. 01-pain-scene's `environment` PART calls the object list \"the only "
    "defence against the stock photo of back pain failure\"; one sentence did the same job.",
    "RATIO IS THE BINDING CONSTRAINT ON THIS PAGE, and it is ADR-016's standing debt arriving "
    "with a cost. The hero is 16:9 and EVERY other slot is 1:1. `01-pain-scene` declares "
    "16:9, 5:3 and 4:5, and ADR-016 rules out the last two, so its only legal ratio is 16:9 — "
    "which means all three of its slots except the hero render at 16:9 into a 1:1 slot and "
    "the layout centre-crops about 44% of the width. Every one of those frames is composed "
    "for the crop, with the subject centred and close and nothing the argument needs in the "
    "outer thirds, and each option says so. `06-relief-scene` has the same problem and it is "
    "one of the two reasons it sits at B rather than A.",
    "06-relief-scene HAS NO POSITION FOR A HAND TOOL, found on 2026-08-24 and applied here. "
    "Its `product` PART requires the product to stand in the frame as its own object near the "
    "camera, measured across twelve renders with everything held, inside or edge-on failing. "
    "A comb cannot satisfy that and also be the thing producing the relief, and two renders "
    "resolved the contradiction by dropping the product entirely. content.items.5 recommends "
    "06-relief-hero, which has no such rule.",
    "THE OBJECT-ONLY FALLBACK AT content.items.1 IS WRITTEN AGAINST A KNOWN ARGUMENT FAULT. A "
    "loose ball of shed hair on a brush reads as HAIR LOSS, which is not what this page "
    "argues; two renders on 2026-08-24 came back reading exactly that way. The prompt names a "
    "matted clump still gripped in the teeth with the surrounding hair twisted into it, which "
    "is what a knot looks like and what shed hair does not.",
    "ADR-021 capability: every option is single-pass. 04-proof-lockedframe runs `handheld` "
    "wherever it appears.",
    "The reference photo is the owner's to upload. This export carries no product photograph, "
    "so `attachments` is omitted from every option rather than filled with an invented sha256 "
    "(SPEC 6.4). Every prompt that needs one keeps its G1 reference block and runs as written "
    "once the photo is attached.",
    "The authenticity fence is breached again, on six tiles. SEVENTH routed page in a row, "
    "and this export makes it measurable: zero closing section tags between the photo grid "
    "and the six attributed quotes, twelve Verified labels and sixty star icons on the page.",
    "No pick prior was available. feedback/picks.jsonl is empty, so the >=20-pick tie-breaker "
    "in SPEC 7.7 never fired and every recommendation rests on fit, legality, render "
    "evidence, product presence and prompt risk alone.",
]


def _ceilings():
    """Prompt-size references READ FROM THE TYPE FILES. Only three types state one, and
    02-cause-anatomy states a band keyed on mark count. A hand-written table was
    invented for four of seven types on page 120 before this replaced it."""
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
    n = 0
    if "dashed straight line" in prompt:
        n += 1
    if any(k in prompt for k in ("opposed arrows", "shaded wedge", "filled region")):
        n += 1
    if "disc badge" in prompt:
        n += 1
    return n


def _reference(o):
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
    PAGE_NOTES.append(
        f"{len(_over)} of {len(_scored)} PROMPTS SIT OVER A STATED CEILING and are shipped "
        f"that way, said here rather than left for the reader to find: {_lines}. Computed "
        "from the prompts at build time, never typed.")
else:
    PAGE_NOTES.append(
        f"NO PROMPT EXCEEDS A STATED CEILING. All {len(_scored)} were measured at build time "
        "against the figures in their own type files. Only three of the types used here state "
        f"one at all; the other {len(_unrated)} — {', '.join(_unrated)} — are reported as "
        "unrated rather than measured against a number this session would have had to "
        "invent.")

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

    WALL = [f"social.photos.{i}.image" for i in range(6)]
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
        warns.append(f"{t} runs {picked.count(t)} times under Step 4 rung 4 — declared "
                     "in coverage.notes")

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

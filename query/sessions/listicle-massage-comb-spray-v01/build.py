#!/usr/bin/env python3
"""Build prompts.json and prompts.md for page 97 — electric spray massage comb.

prompts.json is the source of truth (query/output.schema.json); prompts.md is
generated from it and is never hand-edited (query/runbook.md Step 7).

Run from anywhere:  python3 query/sessions/97-.../build.py
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAGE = "97"


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

# Items per list-section, for ADR-032's five-item clause. Keyed by the slot_id's
# first segment, which is the LIST a spacing rule reasons about.
SECTION_ITEMS = {}
for _sid in DECLARED:
    _k = _sid.split(".")[0]
    SECTION_ITEMS[_k] = SECTION_ITEMS.get(_k, 0) + 1


# ADR-036: a loop's filename is this session's own directory name with the gif type
# inserted and the slot appended. Derived, never typed — the assert below is what
# stops the two drifting apart.
PAGE_TYPE, PRODUCT_SLUG, VERSION = 'listicle', 'massage-comb-spray', 'v01'
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
    "03-mechanism-xray": [
        "photographic background", "environment", "people", "hands",
        "spec labels", "capacity text", "callout lines with text", "opaque shell",
        "internals floating outside the product", "invented components",
        "exploded parts view", "rainbow palette", "bright white background",
        "cartoon style"],
    "03-use-sequence": [
        "step numbers", "arrows carrying the reading order", "arrows between panels",
        "badges", "different hands between panels", "different subject between panels",
        "two actions in one panel", "product off-center", "product cropped out",
        "instruction manual look", "technical diagram", "cold clinical lighting",
        "different location between panels", "inconsistent palette",
        "staged perfection"],
    "04-proof-lockedframe": [
        "badges", "arrows", "glows", "checkmarks", "one panel brighter",
        "inconsistent lighting between panels", "studio background",
        "clean styled set", "staged perfection", "saturated colors",
        "red or green cues", "motion blur", "people", "hands", "brand logos",
        "recognizable trademarks", "identical framing between panels",
        "pixel-perfect alignment", "tripod shot", "3D render look", "CGI",
        "product visualization", "last panel brighter or cleaner than the others",
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
        "invented spray or mist", "fake steam"],
}

# ---------------------------------------------------------------- the prompts

P_HERO_A = """A cinematic film still, editorial photojournalism, natural and unstaged.

A woman in her mid-thirties in a work blouse with the cuffs still unbuttoned, standing at the basin of a small family bathroom early on a weekday, mid-way through dragging a dry plastic paddle brush down through the length of her own hair with one hand while the other presses the crown flat. Under that force: her brush arm pulled hard down past her shoulder, her head tipped away from the pull, the pressing elbow lifted high across her chest. Face: brow drawn in, mouth pressed shut, eyes down on the hair in her hand.

The hair is the evidence. Fine strands stand straight out from her head in a halo, several cling flat to her cheek and jaw, more lift off the brush and follow it as it leaves the hair, and the crown springs back up the instant her hand comes away.

One specific place: a small family bathroom on a weekday morning, and the lived-in clutter of the routine it disrupts — a child's toothbrush in a beaker, a dropped hair tie on the basin edge, an open cosmetics bag, a towel half off its rail.

She is unaware of the camera. Key light: thin cold daylight through a frosted window. Fill: the room's own weak ambient. A rim of light along her lifted forearm. Deep shadow across the lower third of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_HERO_B = """A cinematic film still, editorial photojournalism, natural and unstaged.

A woman in her mid-thirties in a work blouse, sitting at a kitchen table in front of an open laptop a few minutes before a call, turned away from the screen towards the camera with both hands still raised at the sides of her head where she has been trying to smooth her hair down. Under that force: both elbows up and out, fingers spread flat against the hair, shoulders lifted. Face: brow raised and tight, mouth slightly open, looking directly into the lens and holding it.

Fine strands stand out from her head in a halo through and above her fingers, several cling flat across her forehead, and the hair she has just pressed down is already lifting again.

One specific place: a kitchen table set up as a workspace on a weekday morning, and the lived-in clutter of the routine it disrupts — a cold mug beside the laptop, a cereal bowl not cleared, a child's school bag on the next chair, a phone face down on a notebook.

Key light: even flat daylight from the kitchen window, bright and unflattering, minimal shadow. Fill: the room's own ambient.

Desaturated throughout, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_HERO_C = """A cinematic film still, editorial photojournalism, natural and unstaged.

A woman in her mid-thirties in a dressing gown, crouched on a hallway floor behind a seated girl of about six, mid-way through working a dry plastic brush down through a knot in the child's fine hair with one hand while the other holds the hair above the knot to take the pull. Under that force: the mother's holding hand clenched close to the scalp, her brush arm braced and moving in short strokes, the child's head pulled back against the tension and her shoulders hunched up. Face: the mother's jaw set and eyes fixed on the knot; the child's eyes screwed shut, mouth open.

The knot is the evidence: a dense matted clump held tight in the brush's bristles halfway down, loose broken strands caught across the brush face, and more fine hairs standing out from the child's crown in a halo.

One specific place: a narrow hallway by the front door on a school morning, and the lived-in clutter of the routine it disrupts — a school bag half packed, one shoe on its side, a lunch box on the floor, coats overloading a hook.

Neither is aware of the camera. Key light: thin cold daylight through the glass of the front door. Fill: the dim of the hallway. A rim of light along the child's crown. Deep shadow across the near side of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind."""

P_R0_A = """A premium technical see-through product visualization, sharp and high detail. Not photography.

The attached photo is the exact reference for the product.

A plain deep charcoal ground and nothing else on it.

The reference comb is seen from the side at a slight three-quarter angle with the bristle bed toward the camera, filling about three quarters of the frame, its outer shell rendered translucent and glass-like. The silhouette, the proportions and every visible external part match the reference exactly.

Inside the shell, rendered solid and detailed: the water reservoir low in the handle, the ultrasonic atomiser plate seated at the top of that reservoir where the handle meets the head, a row of six small LEDs set into the underside of the bristle bed, and the cylindrical battery cell filling the lower handle. Fine wiring runs from the battery up to the atomiser and along to the LED row. No component types beyond these.

The atomiser plate is the working part and is shown active: it glows cyan, cleaner and brighter than any reflection elsewhere in the render, and it is the brightest thing in the frame.

An ultra-fine white mist leaves the bristle bed in a soft even cloud and drifts away from the comb toward the upper right of the frame, made of the water itself and lit so it reads clearly against the ground.

The six LEDs are drawn as solid components and are not lit.

One product, one shell, no exploded parts, no callout lines, no labels, and no digits, specifications or text of any kind anywhere in the image."""

P_R0_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her mid-thirties in a plain jumper, standing at a bedroom window in the morning drawing the reference comb slowly down through the length of her own hair, her gaze on the hair rather than on the comb. She stands to the right of the frame.

The mist is the subject of the photograph. An ultra-fine white cloud leaves the bristle bed and hangs in the air through the hair, backlit hard by the window so it glows against the darker side of the room, filling a wide band of the frame. Accept lens flare and blown highlights where the window edge cuts in.

One real bedroom filled to the edges with things that genuinely belong there: an unmade bed behind her, a chair with clothes over it, a mug on the sill, a plant, a mirror leaning against the wall, a basket of laundry. Background blurred, but no bare wall area larger than the product. None of those objects carries printed text.

In the upper left of the frame, occupying the space she is offset from, sits a small rounded-rectangle panel with a thin white border showing one magnified detail the scene cannot carry at this distance: the comb's water tank window, half full, with the fine bubble trail rising from the atomiser plate below it. The panel is a clean technical render and does not bleed into the photograph. It is linked to the comb in the scene by proximity alone, with no arrow and no glow border.

No other mark anywhere in the frame."""

P_R0_C = """A premium technical see-through product visualization, sharp and high detail. Not photography.

The attached photo is the exact reference for the product.

A plain deep slate ground and nothing else on it.

The reference comb is seen from directly above with the bristle bed square to the camera, filling about four fifths of the frame, its outer shell rendered translucent and glass-like. The silhouette, the proportions and every visible external part match the reference exactly.

Inside the shell, rendered solid and detailed: the ultrasonic atomiser plate at the head end of the water reservoir, the reservoir running back down the handle behind it, the row of six small LEDs set into the underside of the bristle bed between the teeth, and the vibration motor low in the handle. Fine wiring links the motor and the atomiser. No component types beyond these.

The atomiser plate is the working part and is shown active: it glows cyan, cleaner and brighter than any reflection elsewhere in the render, and it is the brightest thing in the frame.

An ultra-fine white mist rises from between the teeth of the bristle bed in a soft even sheet straight toward the camera, made of the water itself and lit so it reads clearly against the ground.

The six LEDs are drawn as solid components and are not lit.

One product, one shell, no exploded parts, no callout lines, no labels, and no digits, specifications or text of any kind anywhere in the image."""


def rivals_prompt(alt_one, alt_two, after_one, after_two, after_product, surface_note):
    return f"""Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different mornings. One framing for every panel: the same length of hair laid across the same pale bathroom shelf, photographed from directly above from about forty centimetres back, the hair running corner to corner and the shelf edge along the bottom of the frame. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiled wall behind it and the same length of hair in all three panels — the same shade, the same thickness, the same cut ends. Deliberate real-world clutter: {surface_note}.

The only thing that changes is what was drawn through the hair one minute before the photograph, and each tool lies beside the hair in its own panel so it can be told apart. Panel one: {alt_one}, and the hair {after_one}. Panel two: {alt_two}, and the hair {after_two}. Panel three: the reference comb, and the hair {after_product}.

All three tools are ordinary, clean and in good condition, and all three panels get exactly the same exposure, the same background tidiness and the same framing generosity. Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind."""


P_R1 = rivals_prompt(
    "a plain unbranded plastic paddle brush",
    "a plain unbranded fine-tooth plastic comb",
    "lifts away from the shelf in a halo of separated strands, several standing almost upright",
    "lies flatter but throws a fan of fine hairs up off the surface along its whole length",
    "lies down along the shelf in one settled length with no strand standing off it",
    "a water ring on the shelf, a dropped hair tie, a chip in the tile grout")

P_R2 = rivals_prompt(
    "a plain unbranded bottle of silicone smoothing serum",
    "a plain unbranded bottle of hair oil",
    "lies flat and heavy in slick clumped ribbons that stick to each other",
    "lies flat and darkened, the strands welded into two or three thick locks",
    "lies down in one settled length with the strands still separate and matte",
    "a water ring on the shelf, a dropped hair tie, a chip in the tile grout")

P_R3 = rivals_prompt(
    "a plain unbranded trigger spray bottle",
    "a plain unbranded fine-mist travel atomiser",
    "carries two dark soaked patches with pale bone-dry hair between them",
    "carries one broad damp band across the middle and dry ends beyond it",
    "reads evenly matte from root end to tip with no dark patch anywhere",
    "a water ring on the shelf, a dropped hair tie, a chip in the tile grout")

P_R4 = rivals_prompt(
    "a plain unbranded heated straightening brush",
    "a plain unbranded flat iron",
    "shows split and whitened ends and a dry crimped texture along the last third",
    "shows the same whitened ends and a glassy scorched sheen through the middle",
    "shows cut ends that are still square and a texture that is even end to end",
    "a water ring on the shelf, a dropped hair tie, a chip in the tile grout")

P_R5 = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different mornings. One framing for every panel: the bristle bed of one brush photographed from directly above from about twenty-five centimetres back on the same pale bathroom shelf, the bed filling most of the frame and the shelf edge along the bottom. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiled wall and the same light in all three panels, with deliberate real-world clutter: a water ring on the shelf, a dropped hair tie, a chip in the tile grout.

The only thing that changes is which brush is being looked at, and every one has had the same three weeks of ordinary use. Panel one: a plain unbranded plastic paddle brush, its fixed bristles matted down at the base with a grey felt of shed hair, dust and dulled product residue packed between the rows. Panel two: a plain unbranded round brush, the same grey felt wound tight round the barrel between the bristles. Panel three: the reference comb with its teeth retracted flush into the cushion, the whole three weeks of shed hair lifted clear of the bed in one loose mat sitting on top of it, the cushion beneath it clean.

All three are ordinary and undamaged, and all three panels get exactly the same exposure, the same background tidiness and the same framing generosity. One neutral grade across every panel.

No people, no hands, no badges, no arrows and no text of any kind."""

P_HOWTO_A = """Three photographs stacked one above another, filling the whole image, thin white gutters, no outer border, and no panel other than those three. A real home photographed plainly at close range on available light.

The attached photo is the exact reference for the product, in every panel.

The same hands throughout: one adult woman's hands, same skin tone, same short unpainted nails, same wrists, sleeves pushed back. The same bathroom shelf and the same cool window light from the left in all three panels.

Top panel: the comb held over the basin, its water tank window empty and pale, the other hand tipping a small jug of clear water into the open filler port.

Middle panel: the same hands drawing the comb down through the length of her own hair, the tank window now half full of water, and an ultra-fine white mist visibly leaving the bristle bed into the hair, lit so it can be seen.

Bottom panel: the comb set down on the shelf, its tank window still half full, and her free hand running flat down the smoothed hair from crown to tips.

No numbers, no step markers, no arrows and no text of any kind."""

P_HOWTO_B = """A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her mid-thirties in a plain top, standing at a bathroom basin in the morning drawing the reference comb down through her hair in one unhurried pass, her gaze on the hair. She stands to the right of the frame.

The mist is the subject of the photograph. An ultra-fine white cloud leaves the bristle bed and hangs through the hair, side-lit hard from the window so it glows against the darker tiled wall behind her, filling a wide band of the frame.

One real family bathroom filled to the edges with things that genuinely belong there: a child's toothbrush in a beaker, an open cosmetics bag, a towel over the rail, a plant on the cistern, a basket of flannels. Background blurred, but no bare wall area larger than the product. None of those objects carries printed text.

In the upper left of the frame, occupying the space she is offset from, sits a small rounded-rectangle panel with a thin white border showing one magnified detail the scene cannot carry at this distance: the comb's filler port open with a jug tipping clear water into it, and the tank window below reading half full. The panel is a clean technical render and does not bleed into the photograph, linked to the comb in the scene by proximity alone with no arrow and no glow border.

No other mark anywhere in the frame."""

P_HOWTO_C = """Three photographs stacked one above another, filling the whole image, thin white gutters, no outer border, and no panel other than those three. A real home photographed plainly at close range on available light.

The attached photo is the exact reference for the product, in every panel.

The same hands throughout: one adult woman's hands, same skin tone, same short unpainted nails, same wrists, sleeves pushed back. The same child's bedroom floor and the same warm overhead light in all three panels.

Top panel: the comb held over a low chest of drawers, its water tank window empty and pale, the other hand thumbing the power switch on the handle.

Middle panel: the same hands drawing the comb down through the back of a seated child's fine hair, the tank window now half full, and the hair sitting smooth and flat behind the comb's teeth while it still stands lifted and tangled ahead of them.

Bottom panel: the comb set down on the drawers, its tank window still half full, and her free hand gathering the finished hair into one loose length behind the child's shoulder.

No numbers, no step markers, no arrows and no text of any kind."""


def snapshot(mode_line, scene, light, anchor, camera):
    return f"""A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

{mode_line}

{scene} — the mess stays, nothing tidied, nothing added for the picture. {light}, no other light.

One incidental owner object and no more: {anchor}.

{camera}; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture."""


P_S1 = snapshot(
    "The product mid-use, photographed by its owner: the reference comb held against the "
    "length of her own hair, only her forearm and two fingers in shot and no face.",
    "An ordinary family bathroom photographed exactly as found on a weekday morning",
    "Cool daylight through a frosted window", "a child's toothbrush standing in a beaker",
    "Framing slightly tilted and taken at arm's length from the basin")

P_S2 = snapshot(
    "The product simply sitting where it now lives: the reference comb on a bedroom "
    "nightstand, nobody in the picture at all.",
    "An ordinary bedroom photographed exactly as found in the evening",
    "Warm yellow light from one bedside lamp", "a phone charging cable coiled beside it",
    "Framing off-centre and taken from standing height looking down")

P_S3 = snapshot(
    "The product mid-use, photographed over the owner's own shoulder: the reference comb "
    "drawn through a seated child's hair, two fingers and a wrist in shot and no face.",
    "An ordinary child's bedroom floor photographed exactly as found on a grey afternoon",
    "Flat overcast daylight through the window", "a soft toy dropped on its side nearby",
    "Framing close and crooked, taken from very near the floor")

P_S4 = snapshot(
    "The opened box and its contents as the owner has just left them: the reference comb "
    "out of its packaging on a kitchen worktop with the charging cable and the flattened "
    "box pushed to one side. Nobody in the picture at all.",
    "An ordinary kitchen photographed exactly as found in the middle of the day",
    "Mixed light, warm ceiling spots over cool daylight from the window",
    "a fruit bowl at the edge of the worktop",
    "Framing slightly tilted and taken from standing height about half a metre back")

P_S5 = snapshot(
    "The product simply sitting where it now lives: the reference comb lying on a hall "
    "table beside an open handbag it has clearly just come out of, nobody in the picture.",
    "An ordinary hallway photographed exactly as found on the way out",
    "Warm hallway light from a single overhead fitting",
    "a set of keys dropped beside the bag",
    "Framing close and taken from one side at chest height")

P_S6 = snapshot(
    "The product mid-use, photographed by its owner at a desk: the reference comb held up "
    "at the side of her head, one forearm and the edge of a shoulder in shot and no face.",
    "An ordinary home office desk photographed exactly as found before a call",
    "Cool daylight from a window on one side and the pale wash of a monitor on the other",
    "a pair of over-ear headphones pushed to the back of the desk",
    "Framing a little too close and taken at arm's length across the desk")

# ---------------------------------------------------------------- gif briefs

BRIEF_R1 = """A shot of one length of hair lying on a bathroom shelf, standing up in a halo of separated strands after a plastic brush. The reference comb passes down it once and the halo drops, strand by strand, until the whole length is lying settled and flat along the shelf."""

ALT_R1 = """A shot of a woman's own hair at the side of her head, fine strands standing out from the crown. The comb passes down through them once and they fall back against the rest of the hair and stay there, with no hand smoothing them down afterwards."""

BRIEF_R5 = """A shot of the comb's bristle bed close up on a bathroom shelf, three weeks of shed hair and dust packed down between the teeth. A thumb presses the button on the handle, the teeth retract flush into the cushion, and the whole mat lifts clear in one piece."""

ALT_R5 = """A shot of the same bristle bed held over an open bin. The teeth retract flush into the cushion, the packed mat of hair and dust comes away as one, and it drops into the bin leaving a clean cushion behind."""

BRIEF_HOWTO = """A shot of two hands at a bathroom shelf with the comb, its tank window empty. Water goes into the filler port until the window reads half full, a thumb presses the switch, and the comb draws down through the length of her hair with the mist leaving the bristle bed."""

ALT_HOWTO = """A shot of the same hands and the same shelf, the comb already filled and running. It draws down through her hair three times over, and behind each pass the hair lies smooth and settled while it still stands lifted ahead of the teeth."""

RESERVE_R0 = """A shot of the comb's water tank window and the bristle bed beside it, close enough to fill the frame. Fine bubbles rise off the atomiser plate behind the window and an ultra-fine mist builds and lifts away from between the teeth in a steady soft cloud."""

RESERVE_R3 = """A shot of one length of hair on a bathroom shelf with a trigger spray bottle beside it. The bottle fires and heavy droplets land in two dark soaked patches with dry pale hair left between them, and the patches spread and darken further as they soak in."""

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
    "PRECONDITION, and it is not optional: these six photo tiles sit inside the same social "
    "block as six named comments carrying Verified labels and timestamps. "
    "05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a "
    "reviewer name, avatar, star row or verified badge. Use real customer photographs, or "
    "move the photo grid out of the attributed block, or drop the names and Verified labels "
    "— before rendering any of these. This is the fourth routed page in a row to breach it, "
    "so it is a template defect rather than a page one.")

SLOTS = []

SLOTS.append({
    "slot_id": "hero.image", "section_role": "hero",
    "asset": "97-01-hero-pain-scene.png",
    "placement": "listicle header, under the title and above the byline",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides. 01-pain-scene --candid asks for physical limitation in a moment nobody "
        "would choose to be seen in, and hero.intro names two of them — static-charged morning "
        "frizz before urgent meetings, and morning tears detangling a child's knots. A takes "
        "the first because it is the one the reader lives alone and the page's own headline "
        "leads with it. B moves to the confront gaze, which the type reserves for appearance "
        "and self-image; frizz before a call is genuinely close to that line, which is why it "
        "is offered rather than dismissed. C takes the second moment, mother and child in the "
        "hallway. RATIO: the hero is the only 16:9 slot on this page and 01-pain-scene is one "
        "of the types that declares it, so nothing is cropped here. PAGE LEGALITY: A satisfies "
        "04-proof-lockedframe's pairs_with across the five reason cards. PRODUCT PRESENCE: "
        "none, correctly — the type bans it, so G8 does not reach this slot. PROMPT RISK: "
        "{chars} characters against a measured band of 1379-2153.",
    "options": [
        opt("A", "01-pain-scene", "baseline", "16:9", P_HERO_A,
            "The page's own opening problem as one action: brushing dry hair at the basin and "
            "making the halo worse. Evidence is the symptom itself on the body — strands "
            "standing off the head, clinging to the cheek, springing back when the hand lifts.",
            variant="candid", axes={"gaze": "candid"}),
        opt("B", "01-pain-scene", "axis: gaze=confront", "16:9", P_HERO_B,
            "The same argument in the type's other gaze, at the desk minutes before a call. "
            "The advertorial hero cell holds one type and the gates leave no second, so the "
            "honest variation is the axis.",
            variant="confront", axes={"gaze": "confront"},
            notes="--confront is the type's appearance and self-image branch. This page's "
                  "problem sits on that line rather than clearly one side of it, which is the "
                  "reason to offer B and the reason not to recommend it."),
        opt("C", "01-pain-scene", "execution: the second persona — the child's hair, not her "
            "own", "16:9", P_HERO_C,
            "Same type and same axis, the other moment the intro names: the hallway detangle "
            "before school. Two people in frame and the evidence is the knot held in the "
            "brush.",
            variant="candid", axes={"gaze": "candid"}),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The slot's declared job is recognition — a cold reader seeing themselves in "
                  "a held state. Pages 58, 65, 73 and 77 all refused a hero on the same "
                  "ground; refused here for consistency with them.",
    },
})

SLOTS.append({
    "slot_id": "reason.0.image", "section_role": "mechanism",
    "asset": "97-02-reason0-mechanism-xray.png",
    "placement": "reason 1 card, the Editor's Pick",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides, and the gate that usually kills this type does not fire. "
        "03-mechanism-xray asks for a gadget whose real internal components explain why it "
        "works, and its avoid_when bars a trivial interior — a shell with nothing meaningful "
        "inside. This comb holds a reservoir, an ultrasonic atomiser plate, a six-LED array, a "
        "vibration motor and a battery, which is the opposite of trivial, and the positioning "
        "is explicitly technical rather than natural or organic. 03-mechanism-ghostbody is the "
        "other type in the cell and is NOT offered: its use_when asks for a mechanism inside "
        "the BODY that cannot be filmed, and this mechanism is inside the device. B argues the "
        "same thing photographically instead, which G8 then governs. C is the same render from "
        "above. PRODUCT PRESENCE: the product is the whole frame. PROMPT RISK: {chars} "
        "characters.",
    "options": [
        opt("A", "03-mechanism-xray", "baseline", "1:1", P_R0_A,
            "The comb opened up along its own length: reservoir, atomiser plate, LED row, "
            "battery. The atomiser is the working part and glows cyan as the brightest thing "
            "in frame; the mist is the output mark, made of the water itself.",
            notes="G3 COLLISION, resolved in the prompt: the six red LEDs are real components "
                  "but red is the signal colour for a wrong state, and `output` allows exactly "
                  "one emission. They are drawn solid and unlit so the mist stays the only "
                  "thing leaving the product."),
        opt("B", "06-relief-hero", "type: the mechanism argued photographically", "1:1", P_R0_B,
            "Step 4 rung 2, an adjacent step. The mist carries the argument as a real "
            "substance in a real room rather than as a render, with the tank window and the "
            "bubble trail in a detail panel. G8 binds hard here and the prompt frames, lights "
            "and exposes for the mist.",
            variant="detail",
            axes={"register": "commercial", "inset_mode": "detail", "inset_motion": "still"}),
        opt("C", "03-mechanism-xray", "execution: seen from above through the bristle bed",
            "1:1", P_R0_C,
            "Same type and same marks, a different orientation and a different internal set — "
            "the vibration motor in place of the wiring run, and the mist rising through the "
            "teeth toward the camera rather than drifting off to one side.",
            notes="Same G3 collision and the same resolution as option A."),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The atomiser making mist is a mechanism doing the one thing the product is "
                  "sold on, and this slot earns motion on the argument — it is refused by "
                  "SPACING. The `reason` list runs to six items so ADR-032 lets it carry two "
                  "loops, but they may not be adjacent, and this slot sits next to "
                  "reason.1.image which carries the stronger one. It is a legal RESERVE for "
                  "reason.1 and is listed as such in motion.reserves: promoting it would leave "
                  "loops at reason.0 and reason.5, five items apart.",
    },
})

REASONS = [
    ("reason.1.image", "97-03-reason1-proof-brushes.png", "reason 2 card", P_R1,
     "the culprit is a plastic bristle brush · the hair carries the static halo",
     "The first entry in the set and the one the page's headline claim rests on. Two ordinary "
     "brushes against the comb, judged on the same length of hair from the same height."),
    ("reason.2.image", "97-04-reason2-proof-oils.png", "reason 3 card", P_R2,
     "the culprit is silicone serum and hair oil · the hair carries the weight",
     "Same framing, same hair, and the variable moves from a tool to a treatment. The "
     "difference the copy claims — flat and greasy against light and separate — is visible on "
     "the strands themselves."),
    ("reason.3.image", "97-05-reason3-proof-spray.png", "reason 4 card", P_R3,
     "the culprit is a trigger spray bottle · the hair carries the wet patches",
     "The one entry where the difference is a distribution rather than a state: soaked patches "
     "with dry hair between them against an even matte length."),
    ("reason.4.image", "97-06-reason4-proof-heat.png", "reason 5 card", P_R4,
     "the culprit is heat · the hair carries the damage",
     "Cumulative heat damage is the one culprit on this page whose harm PERSISTS after it is "
     "taken away, which is why 02-cause-anatomy is not used anywhere in this set — its "
     "avoid_when bars exactly that, naming a lifted hair cuticle as the example. A locked "
     "frame does not claim a repair; it shows three ends and lets the reader judge."),
    ("reason.5.image", "97-07-reason5-proof-hygiene.png", "reason 6 card", P_R5,
     "the culprit is a fixed bristle bed · the brush itself carries the residue",
     "The last entry changes what is being photographed: the brush rather than the hair, "
     "because the argument is about the tool's own state. Same shelf, same light, same three "
     "weeks of use on all three."),
]

for sid, asset, place, prompt, varies, why in REASONS:
    SLOTS.append({
        "slot_id": sid, "section_role": "comparison",
        "asset": asset, "placement": place,
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis":
            "One option by law (ADR-022): the five reason cards are the unit of variation, not "
            "the card, and this one's place in the set is its varies_on line. The set is "
            "served by one type under cross-slot rule 2, which permits a repeating section to "
            "repeat a type provided the instances differ on a named dimension — the runbook's "
            "own worked precedent is a listicle whose ranked entries each indict one "
            "alternative, which is exactly this page. 04-proof-lockedframe is the advertorial "
            "comparison cell and its core condition holds on every entry: the difference is "
            "visible to the naked eye inside a static frame. CAPABILITY: `strict` needs "
            "compositing, so the panels run `handheld` with --verdict included (ADR-021).",
        "options": [
            opt("A", "04-proof-lockedframe", varies, "1:1", prompt, why, variant="verdict"),
        ],
        "gif": {"eligible": False, "form": "none", "reason": ""},
    })

SLOTS.append({
    "slot_id": "howto.image", "section_role": "how-to-use",
    "asset": "97-08-howto-use-sequence.png",
    "placement": "the how-to card, beside the three numbered steps",
    "recommended_media": "gif",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides and the gate opens. 03-use-sequence is the advertorial how-to-use cell "
        "and multi_step_usage is true — the page states three steps in its own copy, fill, "
        "activate, glide. A runs them as three stacked panels with one pair of hands, and "
        "carries the type's `fill` mark on the tank window in all three panels, which is what "
        "makes three photographs one event. B argues the same thing as a single scene with a "
        "detail panel, which is rung 2 and loses the sequence. C is the same sequence on the "
        "child, which is the page's second persona, and swaps `emission` for `trace`. "
        "EVIDENCE: `emission` renders 7 of 7 in this type and `fill` about 6 with no failure "
        "attributed to it. PROMPT RISK: {chars} characters against this type's hard ceiling of "
        "about 1500 — the type has measured that a longer prompt is paid for out of the "
        "layout, 4 of 6 stacks holding at 1533 characters and 1 of 8 at 2054.",
    "options": [
        opt("A", "03-use-sequence", "baseline", "1:1", P_HOWTO_A,
            "The three steps the copy states, one action per panel: water into the port, the "
            "comb drawn through the hair with the mist visible, the comb set down and the hair "
            "smoothed. The tank window is named in every panel so the level reads as one "
            "event.",
            axes={"camera_lock": "handheld"}),
        opt("B", "06-relief-hero", "type: one scene with a detail panel instead of a sequence",
            "1:1", P_HOWTO_B,
            "Step 4 rung 2. It buys a mist that carries the frame under G8 and a legible tank "
            "window, and it pays for them with the sequence — a reader learns that it is used, "
            "not how.",
            variant="detail",
            axes={"register": "commercial", "inset_mode": "detail", "inset_motion": "still"}),
        opt("C", "03-use-sequence", "execution: the child's hair, and `trace` in place of "
            "`emission`", "1:1", P_HOWTO_C,
            "Same type and same three beats on the page's second persona. The middle panel "
            "carries the boundary instead of the mist — smooth behind the teeth, lifted and "
            "tangled ahead of them — which is the cheapest proof in the library and needs "
            "nothing lit to be visible.",
            axes={"camera_lock": "handheld"}),
    ],
    "gif": {
        "eligible": True, "form": "whole-frame", "kind": "use", "type_id": "use",
        "rung": "natural",
        "reason": "An ordered sequence is the definition of temporal, and this section is "
                  "literally three steps in the page's own words. The still stacks them as "
                  "three panels because a still has no other way; the loop runs them as one "
                  "act, which is what the section is describing. Nothing is re-argued and no "
                  "staging moves, so this is rung 1. The force is named under ADR-031: hands "
                  "fill the tank, a thumb presses the switch, the comb is drawn through hair.",
        "asset": "97-08-howto-use-sequence--brief.svg",
        "refs": "gifs-library/use/ — one file filed, w1000.gif, unledgered; the folder card "
                "carries the law",
        "output": None,  # set below
        "ratio": "1:1",
        "duration_s": 4, "loop": "seamless loop",
        "brief": BRIEF_HOWTO.strip(),
        "alt": ALT_HOWTO.strip(),
        "delivery": "animated webp, loop-safe, under the size ceiling",
    },
})

for i, prompt in enumerate([P_S1, P_S2, P_S3, P_S4, P_S5, P_S6]):
    varies = [
        "in-use · family bathroom · basin shelf · cool frosted daylight · seated arm's length",
        "at-rest · bedroom · painted nightstand · warm bedside lamp · standing above",
        "in-use · child's bedroom · carpet floor · flat overcast daylight · close from floor level",
        "kit-flatlay · kitchen · stone worktop · mixed warm and cool · half a metre back",
        "at-rest · hallway · wooden hall table · warm hallway overhead · close from one side",
        "in-use · home office · laminate desk · cool window and monitor wash · arm's length across",
    ][i]
    SLOTS.append({
        "slot_id": f"social.photos.{i}.image", "section_role": "social-proof",
        "asset": f"97-{9 + i:02d}-social-{i + 1}.png",
        "placement": f"social grid tile {i + 1} of 6",
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis":
            "One option by law (ADR-022): the six tiles are the unit of variation, not the "
            "tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is "
            "whether the thing exists and works in a normal home, which is what this block "
            "claims. The SET DIVERSITY LAW is satisfied across the six: six room classes, six "
            "surfaces, six light temperatures, six camera distances and all three content "
            "modes.",
        "options": [
            opt("A", "05-social-snapshot", varies, "1:1", prompt,
                "One tile of the six-tile set, differing from its siblings on room class, "
                "surface, light temperature, camera distance and content mode.",
                axes={"register": "ugc"}, notes=WALL_FENCE),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "No social-proof slot carries motion. The six-type gif set carries no "
                      "`social` type, so a social-proof slot has nothing to file a loop under, "
                      "wall tile or standalone (ADR-024).",
        },
    })

# the two reason cards that carry loops
_by = {s["slot_id"]: s for s in SLOTS}
_by["reason.1.image"]["recommended_media"] = "gif"
_by["reason.1.image"]["gif"] = {
    "eligible": True, "form": "whole-frame", "kind": "proof", "type_id": "proof",
    "rung": "re-execution",
    "reason": "The page's headline claim is 97% static reduction in a single pass, and a pass "
              "is a thing that happens over time. The routed still is a three-panel locked "
              "comparison, and panels are inspected rather than watched — 0 of 13 such slots "
              "have ever earned a verdict. Drop the panels for one continuous frame in which "
              "the halo falls as the comb goes through, and the same claim is demonstrated "
              "rather than asserted. That is the rung-2 move Step 5d names. The force is a "
              "hand drawing the comb; nothing here moves on its own.",
    "asset": "97-03-reason1-proof-brushes--brief.svg",
    "refs": "gifs-library/proof/ — no files filed yet; the folder card carries the law",
    "output": None,  # set below
    "ratio": "1:1",
    "duration_s": 3, "loop": "seamless loop",
    "brief": BRIEF_R1.strip(),
    "alt": ALT_R1.strip(),
    "delivery": "animated webp, loop-safe, under the size ceiling",
}
_by["reason.5.image"]["recommended_media"] = "gif"
_by["reason.5.image"]["gif"] = {
    "eligible": True, "form": "whole-frame", "kind": "mechanism", "type_id": "mechanism",
    "rung": "re-execution",
    "reason": "One click and the teeth retract flush into the cushion, releasing three weeks "
              "of trapped hair in one piece. That is a working part doing the single thing "
              "this card is sold on, which is the `mechanism` type's own PURPOSE line, and it "
              "cannot be shown in a static frame at all — the still can only put a clogged bed "
              "beside a clean one. The staging changes from three panels to one continuous "
              "frame, so rung 2. The force is a thumb on the button.",
    "asset": "97-07-reason5-proof-hygiene--brief.svg",
    "refs": "gifs-library/mechanism/ — no files filed yet; the folder card carries the law",
    "output": None,  # set below
    "ratio": "1:1",
    "duration_s": 3, "loop": "seamless loop",
    "brief": BRIEF_R5.strip(),
    "alt": ALT_R5.strip(),
    "delivery": "animated webp, loop-safe, under the size ceiling",
}
for sid, why in (
    ("reason.2.image",
     "The card's argument is a state the hair is left in — flat, greasy, weighed down — and "
     "the change happens over hours rather than in front of the camera. Nothing here is a "
     "transition a three-second loop could carry."),
    ("reason.3.image",
     "A trigger bottle throwing droplets IS temporal and this slot would earn a loop on its "
     "own argument. It is refused by SPACING: the `reason` list may carry two loops under "
     "ADR-032 and both are spent at reason.1 and reason.5. It is a legal reserve for "
     "reason.5 and is listed in motion.reserves."),
    ("reason.4.image",
     "Heat damage accumulates over months and is a state, not a transition. A loop would have "
     "to compress it into three seconds, which is the claim no frame can honestly make."),
):
    _by[sid]["gif"]["reason"] = why

# ---------------------------------------------------------------- out of scope

SLOTS.append({
    "slot_id": "offer.image", "section_role": "cta", "asset": None,
    "placement": "closing offer card, above the final CTA",
    "out_of_scope_reason":
        "A standard product shot inside an offer card. The library covers argument images, not "
        "the offer band's packshot (mapping/slot-rules.md, the cta row is empty on every "
        "channel).",
    "options": [],
    "gif": {"eligible": False, "form": "none",
            "reason": "No generated image in this slot to animate."},
})

# Measured figures come from the prompts themselves at build time.
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
        {"slot_id": "reason.0.image", "substitutes_for": "reason.1.image",
         "type_id": "mechanism", "group": "working", "rung": "natural",
         "brief": RESERVE_R0.strip(),
         "why_held_back": "Adjacent to reason.1, which carries the stronger loop. Promoting "
                          "it leaves loops at reason.0 and reason.5, five items apart, so the "
                          "spacing rule still holds."},
        {"slot_id": "reason.3.image", "substitutes_for": "reason.5.image",
         "type_id": "cause", "group": "working", "rung": "natural",
         "brief": RESERVE_R3.strip(),
         "why_held_back": "Earned motion on its own argument and lost to the two-loop cap. "
                          "Promoting it leaves loops at reason.1 and reason.3, two items "
                          "apart, so the spacing rule still holds."},
    ],
    "notes": [
        "Three loops against a floor of 2, so margin is 1 — losing any one still leaves the "
        "page at the floor. The third exists because the `reason` list runs to six items and "
        "ADR-032 lets a section that long carry two loops provided they are not adjacent.",
        "This is the first routed page whose reserve list is not empty. Both reserves are in "
        "the `reason` section, both earned motion on their own argument, and both are legal "
        "substitutes for a named primary — promoting either leaves the spacing rule satisfied. "
        "That is what a page with spare loop-capable slots looks like, and page 77 could not "
        "produce one because both its sections were already at maximum.",
        "COVERAGE PAIR MET: proof (result) at reason.1, mechanism (working) at reason.5, use "
        "(working) at howto. Three distinct gif types on one page, which no earlier page has "
        "reached.",
        "reason.1 carries the page's headline claim — 97% static reduction in a single pass — "
        "and it is the single best motion candidate in the library so far: a halo falling as "
        "the comb goes through is a change the reader can time.",
        "Social grid: 0 tiles, and not by budget — the six-type gif set carries no `social` "
        "type, so those slots have nothing to file a loop under.",
        "All three loops are whole-frame. No type at a slot that earned motion legislates an "
        "inset layer a plate could occupy, so `inset` was never available.",
    ],
}

COVERAGE = {
    "covered": [
        "step 1 pain — 01-pain-scene at hero.image",
        "step 3 mechanism — 03-mechanism-xray at reason.0.image",
        "step 3 how-to — 03-use-sequence at howto.image",
        "step 4 proof — 04-proof-lockedframe --verdict across all five reason cards",
        "step 5 social — 05-social-snapshot across all six grid tiles",
    ],
    "absent": [
        "step 2 cause — 02-cause-anatomy is advertorial-legal and 1:1-legal and was still not "
        "used anywhere. Its removal test is the reason: the page's culprits are friction, "
        "oils, water and heat, and the heat entry fails outright because cumulative damage "
        "PERSISTS after the culprit is taken away — the type's avoid_when names a lifted hair "
        "cuticle as its example. Splitting the set so four cards take anatomy and one takes "
        "something else would break the set law that makes a repeating section one thing",
        "step 6 relief — the page has no outcome section at all. This IS a gap and it is the "
        "one this routing recommends filling; see `recommended`",
        "step 5 personas — 05-persona-grid declares no advertorial channel",
    ],
    "notes": [
        "Awareness stage read from the page's own copy, not from a declared field: "
        "PROBLEM-AWARE, and the brief agrees. The header assumes the reader knows the "
        "frizz and the tears and does not yet know a tool class exists for it — every reason "
        "card opens by naming something they have already tried.",
        "lpTypeId is `listicle`; the library has no such channel and a listicle routes on the "
        "advertorial cell, as pages 65 and 73 did before it.",
        "One-type-once is not breached. 04-proof-lockedframe runs five times and "
        "05-social-snapshot six, both inside a single repeating section, which cross-slot "
        "rule 2 permits when the instances differ on a named dimension. Every linear slot "
        "carries a distinct type.",
    ],
}

RECOMMENDED = [
    {
        "slot_id": "outcome.image",
        "section_role": "outcome",
        "earns_its_place":
            "Step 6 relief is absent and the awareness stage says it matters. A problem-aware "
            "reader arrives knowing the frizz and not the tool class; the page spends seven "
            "cards on what is wrong and what the device contains, and never once shows the "
            "resolved morning it is selling. Every other rung is covered, so this is the only "
            "gap on the ladder and it is at the end of it.",
        "suggested_placement":
            "Between the how-to card and the offer band, as a full-width card closing the "
            "seven reasons before the price appears.",
        "asset": "97-15-outcome-relief-hero.png",
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis":
            "06-relief-hero is the advertorial outcome cell alongside 06-relief-scene, and "
            "06-relief-scene is not offered because it does not declare 1:1 — every slot on "
            "this page below the hero is square. 06-relief-hero declares 1:1 and 16:9, so it "
            "fits either way. G8 binds: the mist is the primary subject and the frame is lit "
            "for it. It is additive and additive only — nothing in the routed set depends on "
            "it, and the page ships legal without it.",
        "options": [
            opt("A", "06-relief-hero", "baseline", "1:1", P_R0_B,
                "The same execution offered as option B at reason.0, moved to the slot its "
                "type is actually for. If both are taken, change one of them: the same image "
                "in two places is the fault one-type-once exists to prevent.",
                variant="detail",
                axes={"register": "commercial", "inset_mode": "detail",
                      "inset_motion": "still"},
                notes="COMBINATION: this shares a prompt with reason.0 option B. Take one or "
                      "the other, or re-execute this one on the second persona."),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "A proposal rather than a routed slot. Step 5c runs on slots the page "
                      "declares; if this one is added, it is routed and given a verdict then.",
        },
    },
]

PAGE_NOTES = [
    "SOURCE: ~/Downloads/content-library-local/landing-page-electric-spray-massage-comb-end-"
    "morning-static-and-knots.json, page id 97, template TPL-ADV16, lpTypeId listicle. The "
    "compiled HTML is the authoritative slot list and carries the template's aspect ratio per "
    "slot; imageBriefs agrees with it on all fifteen slots and adds no others.",
    "TEMPLATE RATIO: one 16:9 slot, the hero, and fourteen at 1:1. That is the opposite shape "
    "from page 77 and it costs two types their place — 01-pain-scene declares 16:9, 5:3 and "
    "4:5 and so can only serve the hero, and 06-relief-scene declares 16:9, 4:3 and 3:4 and "
    "so cannot serve this page at all. Both facts are load-bearing above: they are why the "
    "hero is the only pain image and why the recommended outcome card takes 06-relief-hero.",
    "G8 BINDS THIS PAGE HARDER THAN ANY BEFORE IT. visible_output is a nano-mist plus six red "
    "LEDs, so wherever the product is in a photographic frame the output is the primary "
    "subject and the frame is lit for it. It reaches reason.0 option B, howto option B and the "
    "recommended outcome card. It does NOT reach 03-mechanism-xray, whose register is a "
    "technical render rather than a photograph, and it does not reach the hero, which bans the "
    "product outright.",
    "G3 COLLISION, resolved rather than ignored: the product's six red LEDs are real "
    "components, red is the signal colour for a wrong state, and 03-mechanism-xray allows "
    "exactly one `output`. Both xray prompts draw the LEDs solid and unlit so the mist is the "
    "only emission and the only added colour is the cyan on the atomiser.",
    "02-cause-anatomy was tested against all five reason cards and refused. Four would pass "
    "its removal test; the heat card does not, because cumulative damage persists after the "
    "culprit is removed and the type's avoid_when names a lifted hair cuticle as exactly that "
    "case. A set that took anatomy on four cards and something else on the fifth would stop "
    "being a set.",
    "ADR-021 capability: every option is single-pass. 04-proof-lockedframe runs `handheld` "
    "rather than `strict` at all five reason cards, because `strict` needs compositing.",
    "The authenticity fence is breached again, on six tiles. Fourth routed page in a row, so "
    "it is a property of these templates and not of any one page.",
]

OUT = {
    "page_id": PAGE,
    "registry_version": "2.0.0",
    "channel": "advertorial",
    "awareness_stage": "problem-aware",
    "slots": SLOTS,
    "coverage": COVERAGE,
    "recommended": RECOMMENDED,
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

    for cond, tid, why in ATTRIBUTE_GATES:
        if cond(ATTRS):
            for s in routed:
                for o in s["options"]:
                    if o["type"] == tid:
                        errs.append(f"{s['slot_id']} {o['opt']}: {why}")

    # one-type-once across the RECOMMENDED set, excluding repeating sections.
    # reason.0 is the Editor's Pick and is NOT one of the five equivalent entries —
    # it argues the product where they each indict an alternative, so it carries
    # three options like any linear slot.
    REPEATING = {
        "the five reason cards": [f"reason.{i}.image" for i in range(1, 6)],
        "the social grid": [f"social.photos.{i}.image" for i in range(6)],
    }
    in_set = {sid for ids in REPEATING.values() for sid in ids}
    linear = [s for s in routed if s["slot_id"] not in in_set]
    picked = [next(o for o in s["options"] if o["opt"] == s["recommended_opt"])["type"]
              for s in linear]
    for sec, ids in REPEATING.items():
        members = [s for s in routed if s["slot_id"] in ids]
        if not members:
            continue
        kinds = {next(o for o in s["options"] if o["opt"] == s["recommended_opt"])["type"]
                 for s in members}
        if len(kinds) > 1:
            errs.append(f"repeating section `{sec}` is served by more than one type "
                        f"{sorted(kinds)}; cross-slot rule 2 permits a repeat, not a mixture")
        picked.extend(sorted(kinds))
        for s in members:
            if len(s["options"]) != 1:
                errs.append(f"{s['slot_id']}: a repeating section emits one option (ADR-022)")
    dupes = {t for t in picked if picked.count(t) > 1}
    if dupes:
        errs.append(f"one-type-once breached in the recommended set: {sorted(dupes)}")

    step3 = {"03-mechanism-ghostbody", "03-spec-split", "03-use-sequence"}
    n3 = len([t for t in picked if t in step3])
    if n3 > 2:
        errs.append(f"step-3 budget: {n3} of the capped three types, max 2")

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

    # SET DIVERSITY across the two repeating sections
    for sec, axes_n in (("the social grid", 5), ("the five reason cards", 2)):
        members = [s for s in routed if s["slot_id"] in REPEATING[sec]]
        seen = [s["options"][0]["varies_on"] for s in members]
        if len(set(seen)) != len(seen):
            errs.append(f"SET DIVERSITY: two entries of `{sec}` share a varies_on line")
        for line in seen:
            if len([p for p in line.split("·") if p.strip()]) < axes_n:
                errs.append(f"SET DIVERSITY: `{line[:40]}` names fewer than {axes_n} "
                            "dimensions")
        for s in members:
            if "PRECONDITION" in (s["options"][0].get("composition_notes") or ""):
                continue
            if sec == "the social grid":
                errs.append(f"{s['slot_id']}: the authenticity fence is breached on this page "
                            "and the option carries no precondition")

    # motion
    elig = [s for s in SLOTS if s.get("gif", {}).get("eligible")]
    if len(elig) != MOTION["delivered"]:
        errs.append(f"motion.delivered says {MOTION['delivered']}, {len(elig)} slots eligible")
    if len(elig) < MOTION["floor"] and not MOTION["shortfall_reason"]:
        errs.append("below the motion floor with no shortfall_reason")
    if len(elig) > MOTION["ceiling"]:
        errs.append(f"motion ceiling {MOTION['ceiling']} exceeded: {len(elig)}")
    if MOTION.get("margin") != len(elig) - MOTION["floor"]:
        errs.append(f"motion.margin says {MOTION.get('margin')}, computed "
                    f"{len(elig) - MOTION['floor']}")

    secs = {}
    for s in elig:
        secs.setdefault(s["slot_id"].split(".")[0], []).append(s["slot_id"])
    for sec, ids in secs.items():
        if len(ids) == 1:
            continue
        if len(ids) > 2:
            errs.append(f"{len(ids)} loops in section `{sec}`; the cap is two and only in a "
                        f"five-item section (ADR-032): {ids}")
            continue
        if SECTION_ITEMS.get(sec, 0) < 5:
            errs.append(f"two loops in section `{sec}`, which declares "
                        f"{SECTION_ITEMS.get(sec, 0)} items; the second needs five or more "
                        f"(ADR-032): {ids}")
        idx = sorted(int(i.split(".")[1]) for i in ids if i.count(".") >= 2
                     and i.split(".")[1].isdigit())
        if len(idx) == 2 and idx[1] - idx[0] < 2:
            errs.append(f"the two loops in section `{sec}` are adjacent ({idx[0]} and "
                        f"{idx[1]}); ADR-032 needs a static item between them")

    live = {x["slot_id"] for x in elig}
    for r in MOTION.get("reserves", []):
        if r["substitutes_for"] not in live:
            errs.append(f"reserve {r['slot_id']} substitutes for {r['substitutes_for']}, "
                        "which carries no loop")
        if r["slot_id"].split(".")[0] != r["substitutes_for"].split(".")[0]:
            errs.append(f"reserve {r['slot_id']} is not in the same section as "
                        f"{r['substitutes_for']}")
        if r["slot_id"] in live:
            errs.append(f"reserve {r['slot_id']} already carries a loop of its own")
        # promoting it must leave the spacing rule satisfied
        rest = sorted(int(x.split(".")[1]) for x in live
                      if x != r["substitutes_for"]
                      and x.split(".")[0] == r["slot_id"].split(".")[0])
        mine = int(r["slot_id"].split(".")[1])
        for other in rest:
            if abs(other - mine) < 2:
                errs.append(f"reserve {r['slot_id']} would sit adjacent to index {other} "
                            "once promoted (ADR-032)")

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
    if got != ["result", "working"]:
        warns.append(f"coverage pair not met (groups: {got})")

    GIF_FIELDS = ("output", "ratio", "duration_s", "loop", "brief", "delivery",
                  "refs", "asset")
    REGISTER = ("light", "lighting", "daylight", "lit", "backlit", "grade", "graded",
                "register", "overcast", "desaturated", "saturated", "palette",
                "exposure", "colour", "color", "tone", "greyscale", "grayscale")
    for s in elig:
        g = s["gif"]
        for f in GIF_FIELDS:
            if not g.get(f):
                errs.append(f"{s['slot_id']}: gif is missing `{f}` (G12, ADR-028)")
        for dead in ("shot", "action", "result", "match", "prompt"):
            if dead in g:
                errs.append(f"{s['slot_id']}: gif still carries `{dead}`, retired at ADR-028")
        if not g["asset"].endswith("--brief.svg"):
            errs.append(f"{s['slot_id']}: the plate is generated, so its asset carries the "
                        "--brief suffix and a .svg extension (G12)")
        if g["asset"] == s["asset"]:
            errs.append(f"{s['slot_id']}: plate asset must not be the slot's own asset")
        want = gif_name(g["type_id"])
        if g["output"] != want:
            errs.append(f"{s['slot_id']}: gif.output must be `{want}` (ADR-036), got "
                        f"`{g['output']}`")
        if g["ratio"] != DECLARED[s["slot_id"]]["ratio"]:
            errs.append(f"{s['slot_id']}: gif.ratio {g['ratio']} is not the slot's declared "
                        f"{DECLARED[s['slot_id']]['ratio']}")
        if not g.get("alt"):
            errs.append(f"{s['slot_id']}: no gif.alt — every delivered loop owes a second way "
                        "to shoot the same argument (ADR-032)")
        for label, text in (("brief", g["brief"]), ("alt", g.get("alt"))):
            if not text:
                continue
            n = len(text.split())
            if not 25 <= n <= 55:
                errs.append(f"{s['slot_id']}: the {label} is {n} words, outside the 25-55 "
                            "band (ADR-029)")
            found = sorted({w for w in REGISTER if re.search(rf"\b{w}\b", text, re.I)})
            if found:
                errs.append(f"{s['slot_id']}: the {label} names {', '.join(found)} — light, "
                            "grade and register belong to the still (ADR-030)")
        if g["brief"] == g.get("alt"):
            errs.append(f"{s['slot_id']}: gif.alt repeats the brief")
    for r in MOTION.get("reserves", []):
        n = len(r["brief"].split())
        if not 25 <= n <= 55:
            errs.append(f"reserve {r['slot_id']}: the brief is {n} words, outside the band")

    for s in SLOTS:
        if "gif" not in s or "reason" not in s["gif"] or not s["gif"]["reason"]:
            errs.append(f"{s['slot_id']}: no gif verdict (Step 5c requires one either way)")
        if s["section_role"] == "social-proof" and s.get("gif", {}).get("eligible"):
            errs.append(f"{s['slot_id']}: a social-proof slot carries motion (Step 5d)")
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
                errs.append(f"{s['slot_id']}: recommendation_basis claims {m.group(1)} "
                            f"characters, the prompt is {len(rec['prompt'])}")

    # this type's hard ceiling is a layout constraint, not a style note
    for s in routed:
        for o in s["options"]:
            if o["type"] == "03-use-sequence" and len(o["prompt"]) > 1500:
                warns.append(f"{s['slot_id']} {o['opt']}: {len(o['prompt'])} characters "
                             "against 03-use-sequence's measured ~1500 layout ceiling")
    return errs, warns


# ---------------------------------------------------------------- emit

def render_md():
    """The human view, and it has exactly one reader. Everything omitted here is in
    prompts.json, which is the contract and stays complete."""
    L = []
    routed = [s for s in SLOTS if s.get("options")]
    n_opts = sum(len(s["options"]) for s in routed)
    n_gif = len([s for s in SLOTS if s.get("gif", {}).get("eligible")])
    n_block = len([s for s in routed for o in s["options"]
                   if "PRECONDITION" in (o.get("composition_notes") or "")])
    L.append("# Image prompts — page 97, electric spray air cushion massage comb")
    L.append("")
    L.append("GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit "
             "the script and re-run. Routing rationale, the negative motion verdicts, the "
             "reserves and the out-of-scope slot are all in `prompts.json`.")
    L.append("")
    L.append(f"- page `{PAGE}` · advertorial (lpTypeId listicle) · problem-aware · registry "
             f"`2.0.0` · {len(routed)} routed slots · {n_opts} prompts · {n_gif} motion briefs")
    L.append(f"- motion: {MOTION['delivered']} loops, floor {MOTION['floor']}, margin "
             f"{MOTION['margin']}, groups {', '.join(MOTION['groups_covered'])}, "
             f"{len(MOTION['reserves'])} reserves")
    if n_block:
        L.append(f"- **{n_block} prompts carry a blocking precondition**, stated on each — "
                 "do not render those until it is resolved")
    if RECOMMENDED:
        L.append(f"- **{len(RECOMMENDED)} additive proposal** below the routed slots — a rung "
                 "the page does not cover")
    L.append("")
    L.append("---")
    L.append("")
    for s in routed + RECOMMENDED:
        proposal = s in RECOMMENDED
        head = f"## `{s['slot_id']}` — {s['section_role']}"
        if proposal:
            head += "  ·  PROPOSAL, not a slot the page declares"
        L.append(head)
        L.append("")
        L.append(f"- asset `{s['asset']}` · "
                 f"{s.get('placement') or s.get('suggested_placement')}")
        L.append(f"- recommended: **option {s['recommended_opt']}** · media "
                 f"**{s['recommended_media']}**")
        if proposal:
            L.append(f"- earns its place: {s['earns_its_place']}")
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
            L.append(f"### {s['slot_id']} · the motion brief — `{g['type_id']}`")
            L.append("")
            L.append(f"- form `{g['form']}` · rung `{g['rung']}` · reference folder: "
                     f"{g['refs']}")
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
    if MOTION["reserves"]:
        L.append("## Motion reserves")
        L.append("")
        L.append("Slots that earned motion and lost to the spacing rule. Each replaces the "
                 "loop it names — it is never added alongside it. Promote one by editing "
                 "`build.py` and re-running `scripts/gen-plate.py`.")
        L.append("")
        for r in MOTION["reserves"]:
            L.append(f"### `{r['slot_id']}` — `{r['type_id']}`, replaces "
                     f"`{r['substitutes_for']}`")
            L.append("")
            L.append(f"- {r['why_held_back']}")
            L.append("")
            L.append("```")
            L.append(r["brief"])
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
    for w in warns:
        print(f"WARN  {w}")
    for e in errs:
        print(f"ERROR {e}")
    print(f"page {PAGE}: {len(SLOTS)} slots, {len(routed)} routed, {n} prompts, "
          f"{nb} motion briefs, {len(MOTION['reserves'])} reserves, "
          f"{len(errs)} errors, {len(warns)} warnings")
    return 1 if errs else 0


if __name__ == "__main__":
    raise SystemExit(main())

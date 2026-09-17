#!/usr/bin/env python3
"""Build content.json, prompts.md and prompts.json for pdp-dr-seat-cushion-l-shaped-v08.

Page 590, the owner's LP2 product page for the ergonomic memory foam seat cushion, exported from
the app as `pdp-dr-ergonomic-memory-foam-seat-cushion-v04.json` on 2026-09-17 (template
TPL-PDP05, "LP2-Aure-TopLaser" 1.0.0, filled with the ComfortCore cushion's copy).

The first LP2 page routed in this repo. It routes `registry/pdp-dr-index.yaml` and
`registry/pdp-dr-types/` under `registry/pdp-dr-instruction.md` (SPEC 3.0, ADR-091), with
ADR-102's loose routing: each image routes by its section's name and copy, and no rule removes a
type from a slot because another slot holds it.

Type versions are read from the COMMITTED LP2 files, so every version cited is one git can show.
"""
import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAGE_ID = "590"
EXPORT = os.path.expanduser("~/Downloads/pdp-dr-ergonomic-memory-foam-seat-cushion-v04.json")
GATE = 1800

# ------------------------------------------------------------------ the LP2 product block
BLOCK = ("Use the attached product photo as the exact reference. Preserve its shape, proportions, "
         "construction, seams, surface texture, finish and colour exactly. Do not redesign, restyle, "
         "simplify or add features. The product appears in one of its real colourways only, never "
         "restyled to match the scene or the set palette; no added piping, trim, logos, patterns or "
         "printed text. Every part keeps its photographed colour and finish; no part is tinted toward "
         "the set's accent.")

# ------------------------------------------------------------------ the session's style lock
# Named once here and written into every prompt in the same words (registry/pdp-dr-instruction.md,
# "One session, one set"). The page carries no style line, so the lock is neutral.
LIGHT = "Light: soft daylight from one side, gentle natural shadows, no rim light."
GRADE = "Grade: bright, warm-neutral, true to life."
ROOM = "Ground: a real, lived-in place in warm-neutral tones, nothing saturated behind the subject."
SEAMLESS = "Ground: a seamless warm-grey studio sweep with a soft floor shadow."
NOFRAME = "No frame or border around any photograph or panel."
CORNER = "Nothing is placed in the bottom-right corner of the frame."
WORDLESS = "Nothing in the picture carries a word, a number, a label or a badge."
TYPE_LIGHT = "Title type: one bold geometric sans-serif like Montserrat, wide and round, sentence case, charcoal."
TYPE_DARK = "Title type: one bold geometric sans-serif like Montserrat, wide and round, sentence case, white."
HOST = "on a host seat clearly different from it in tone and material"

STYLE_LOCK = {
    "grounds": "two treatments: a real, lived-in place in warm-neutral tones, or a seamless warm-grey "
               "studio sweep with a soft floor shadow. A rendered type keeps its own register's field "
               "(`02-cause-anatomy`'s deep field, the white infinity of `03-mechanism-ghostbody`, "
               "`03-spec-split`'s dark render half), which the lock admits",
    "text colour": "charcoal on a light ground, white on a dark ground",
    "accent": "one muted teal, reserved for a chip; this set carries no chip, so it appears nowhere",
    "typography": "one bold geometric sans-serif like Montserrat, wide and round, sentence case",
    "chip form": "none used; the gallery carries titles only",
    "design language": "no frame or border around any photograph or panel; generous even margins",
    "lighting family": "soft daylight from one side, gentle natural shadows, no rim light; "
                       "bright, warm-neutral, true to life",
    "corners": "nothing in the bottom-right corner, which carries the generation tool's watermark",
    "casting": "North American, named in each prompt that carries a person (the page prices in US "
               "dollars and names no market)",
}


SPLIT_TILE = ("E-commerce comparison tile, high contrast, sharp. Two panels split hard down the "
              "middle, each running to the frame edge.")
SPLIT_DISCS = ("Top-left, a flat solid red disc with a cross cut out; top-right, a flat solid green disc "
               "with a check cut out, the same size.")
SPLIT_PLACE = ("Render it in the right panel only, whole, under {who} and behind the lower back as one "
               "piece, seen from the side, " + HOST + ".")


def title_lines(title, where, dark=False):
    return [f'{where}, the title reads "{title}".', TYPE_DARK if dark else TYPE_LIGHT]


def compose(head, body, place=None, ground=ROOM, lit=True, title=None, where=None, dark=False):
    """One paste-and-run prompt. `place` given means the product is in frame and the block ships."""
    parts = [head, ""]
    if place is not None:
        parts += [BLOCK + "\n" + place, ""]
    parts += [body.strip(), ""]
    if ground:
        parts.append(ground)
    if lit:
        parts += [LIGHT, GRADE]
    parts += title_lines(title, where, dark) if title else [WORDLESS]
    parts += [NOFRAME, CORNER]
    return "\n".join(parts).strip()


def type_version(tid):
    blob = subprocess.run(["git", "-C", ROOT, "show", f"HEAD:registry/pdp-dr-types/{tid}.md"],
                          capture_output=True, text=True, check=True).stdout
    for line in blob.split("\n---\n", 1)[0].splitlines():
        if line.startswith("version:"):
            return line.split(":", 1)[1].strip().strip('"')
    raise SystemExit(f"no version in {tid}")


def opt(tid, variant, varies_on, gloss, note, prompt, axes=None, product=True):
    return {"type": tid, "variant": variant, "axes": axes or {}, "varies_on": varies_on,
            "gloss": gloss, "note": note, "prompt": prompt, "product": product}


NO_GIF = {"eligible": False, "form": "none"}


def no_gif(reason):
    return dict(NO_GIF, reason=reason)


GHOST_HEAD = ("3D technical render on a seamless white background, soft even studio light, no cast "
              "shadow. Two equal panels divided by a thin vertical line.")
GHOST_BODY = ("One featureless matte white mannequin, no face, hair, clothing or skin tone, seated the "
              "same way in both panels, seen from the side.")


def ghost(opened, wrong, right, marks, **kw):
    """A 03-mechanism-ghostbody prompt: two panels, one mannequin, a closed layer list."""
    body = (f"{GHOST_BODY} It is opened as a plane at {opened}; nothing deeper is drawn, and the "
            "outline stays unbroken.\n\n"
            f"Left panel, wrong state, on a plain seat: {wrong}. Right panel, correct state, on the "
            f"product: {right}.\n\n"
            f"Marks, flat and hard-edged: the bones in warm ivory in both panels; {marks}; in each "
            "panel's top corner a filled disc with its glyph cut out, a red cross left, a green check "
            "right. All else is matte white or grey.")
    return compose(GHOST_HEAD, body,
                   place="Render it in the right panel only, on the seat under the mannequin and up "
                         "against the seat back.",
                   ground=None, lit=False, **kw)


SLOTS = []

# ================================================================== hero
# ADR-103 (e6c84c3): every hero prompt carries these sentences word for word, the fifth only where
# a person is in the frame. They replace this session's first placement wording.
HERO_FIXED = [
    "The product and anyone using it sit together in the right half of the picture, just past the "
    "centre and well clear of the right edge.",
    "Together they fill about half the picture's height, and no face, hand or part of the product "
    "enters its top or bottom fifth.",
    "The left half continues the same place in soft focus, bright and calm, with nothing in it that "
    "matters.",
    "The product is big enough to recognise at a glance, never a small detail in the distance.",
]
HERO_PERSON = "Any person turns slightly toward the left side of the picture."


def hero_fixed(person):
    return " ".join(HERO_FIXED + ([HERO_PERSON] if person else []))


SLOTS.append({
    "slot_id": "hero.image", "role": "hero", "kind": "hero", "ratio": "16:9",
    "asset": "590-01-hero-relief-hero.png",
    "placement": "Hero banner behind 'Continuous Lower Back Support & Tailbone Relief'.",
    "recommended": "A",
    "rationale":
        "The hero's words promise continuous support and relief, and the reader arrives "
        "solution-aware, so the banner shows the fix at work rather than the pain. FIT: "
        "`06-relief-hero` is the hero row's only preferred type on this corpus (16 sources). "
        "BANNER LAW (ADR-096, re-measured by ADR-103): the group sits in the safe box, 55–88% "
        "across and 22–78% down, and every option carries the five fixed sentences, the fifth only "
        "where a person is in frame; the owner renders it at 16:9. B is the same relief read as a "
        "public moment after a long drive, with the product brought close enough to recognise; C is "
        "the product's one-piece curve alone, the page's subtitle as a macro. PRODUCT PRESENCE: all "
        "three carry the product.",
    "gif": no_gif("A banner argues a held state behind the page's words; nothing crosses a "
                  "boundary in it, so a loop would animate a person sitting still."),
    "options": [
        opt("06-relief-hero", "--commercial", "baseline",
            "A desk worker settled back in her office chair, the product under her and behind her "
            "lower back, the daylight coming from the left.",
            "Needs the product photo. Passive product, so the pose is relaxed and the gaze is off "
            "the product; the seated product is seen from a rear three-quarter angle, as the LP2 "
            "product section asks.",
            compose(
                "Commercial lifestyle photograph, a wide banner.",
                "A North American woman in her forties sits back at her home-office desk, looking "
                "toward the window rather than at the camera, her back fully against the product. "
                "The daylight comes from the left. "
                + hero_fixed(True),
                place="Render it whole on her office chair, under her and behind her lower back, "
                      "seen from a rear three-quarter angle, " + HOST + "."),
            axes={"register": "commercial", "inset_mode": "none"}),
        opt("06-relief-scene", None, "type: 06-relief-scene",
            "A driver standing up out of his car at a highway rest stop in one easy movement, the "
            "product on the driver's seat right beside him.",
            "Needs the product photo. Counts as a place scene; its public place and its product "
            "standing as its own object are the type's own law. The product sits close, at the "
            "open door, so the hero's fourth sentence can hold.",
            compose(
                "Candid documentary photograph, a wide banner, natural and unposed.",
                "A North American man in his fifties stands up out of his car at a highway rest stop "
                "easily, one hand on the open door, looking toward the coffee kiosk "
                "rather than at the camera. The daylight comes from the left. " + hero_fixed(True),
                place="Render it whole on the driver's seat right beside him, seen through the open "
                      "door, " + HOST + "."),
            axes={}),
        opt("03-spec-macro", None, "type: 03-spec-macro",
            "The subtitle as a surface: the curve where the seat section rises into the back, one "
            "piece, in close-up in the safe box.",
            "Needs the product photo. The magnified region is a true region of the photograph; the "
            "gallery's one macro is `media.gallery.3`. A hand is in frame and no person, so the "
            "fifth fixed sentence is left out.",
            compose(
                "Commercial studio macro photograph, a wide banner, razor sharp.",
                "The surface is resolved exactly as the photo shows it under raking light from the "
                "left, one continuous piece with no seam between seat and back. A hand in a knit "
                "sleeve presses into the lower curve, the surface holding firm around it. "
                + hero_fixed(False),
                place="The magnified region is a true region of the product: the curve where its seat "
                      "section rises into its upright section.",
                ground=SEAMLESS),
            axes={}),
    ],
})

# ================================================================== the product card's gallery
GALLERY_NOTE = (
    "The product card's gallery, the one place on the page that carries words (ADR-096). "
    "`scripts/pdp-dr-slots.py` classes `media.gallery.*` as a wordless section because the Slot "
    "kinds table names only `buy.gallery.*`; the HTML puts these six images in the product card "
    "(`gal-main-N`), so this session routes them as gallery tiles, and the table owes a row.")
SLOTS.append({
    "slot_id": "media.gallery.1.image", "role": "problem-agitation", "kind": "gallery", "ratio": "1:1",
    "asset": "590-02-gallery1-pain-split.png",
    "placement": "Product card gallery, image 2, the problem tile.",
    "recommended": "A",
    "rationale":
        GALLERY_NOTE + " Image 2 is where the gallery's problem tile sits, and the page's first "
        "argument is posture: 'lifts your hips level with knees to stop backward pelvic tilt'. FIT: "
        "`01-pain-split` is the owner's Problem Tile · Before–After Split, and the attribute read "
        "(`symptom_visibility: visible`) keeps it in the pool. FEATURE KEY `posture-angle`. B is the "
        "cause read with the product absent, as `02-cause-anatomy`'s LP2 law asks; C is the same "
        "correction as the body mechanism.",
    "gif": no_gif("Two panels are compared, not watched; the tile's argument is a difference the eye "
                  "travels between."),
    "options": [
        opt("01-pain-split", "--mirror", "baseline",
            "The same desk worker on the same chair: hips sunk and back unsupported in grayscale, "
            "level and supported in colour with the product.",
            "Needs the product photo, for the right panel. `--mirror`'s invariants block is the "
            "route that held one person across two panels. Title 4 words.",
            compose(
                SPLIT_TILE,
                "The same woman in both panels, named once: a North American woman in her forties, "
                "hair tied back, grey knit sweater, dark trousers, seen from the side at seat height, "
                "at the same desk with a laptop, on the same office chair, in the same window "
                "light.\n\n"
                "Left panel, grayscale: on the bare chair, her hips sunk below her knees, her pelvis "
                "rolled back, a gap behind her lower back, her shoulders rounded.\n\n"
                "Right panel, full colour: on the product, her hips level with her knees, her lower "
                "back supported, her shoulders over her hips; brighter and airier than the left.\n\n"
                + SPLIT_DISCS,
                place=SPLIT_PLACE.format(who="her"),
                ground=None, lit=False,
                title="Hips level, back supported",
                where="Along the bottom edge, from the left, over the pale floor")),
        opt("02-cause-anatomy", "--diagnostic", "type: 02-cause-anatomy",
            "The cause, drawn: a flat seat that tips the pelvis back and flattens the lumbar curve, "
            "against a level seat that keeps both.",
            "Needs no photo: on an LP2 page this type's product is absent or a silhouette, and "
            "`03-mechanism-ghostbody` carries the product at image 3. Title from the type's own "
            "LP2 example.",
            compose(
                "2D illustration, airbrushed: soft gradients and modelled volume. Not photography, "
                "not 3D. Two equal panels side by side.",
                "The whole seated body is in shot in both panels, seen from the side, the seat small "
                "within the frame. Ground: one continuous deep muted slate-blue field behind both "
                "panels, one step lighter on the right.\n\n"
                "In each panel the named structures are drawn in warm ivory over a translucent "
                "outline of the body: the pelvis, the tailbone at its base, the five lumbar vertebrae "
                "above it, and the thigh bone running forward to the knee.\n\n"
                "Left panel, the wrong state: the body sits on a flat seat that sags at the back, the "
                "knees above the hips, the pelvis rotated backward and the lumbar vertebrae pulled "
                "into a flat curve.\n\n"
                "Right panel, the correct state: the same body on a level seat with a plain L-shaped "
                "support in silhouette, the pelvis upright, the knees level with the hips and the "
                "lumbar curve restored.\n\n"
                "Marks: one red curved line along the lumbar vertebrae in the left panel, one blue "
                "curved line along them in the right. In the top corner of each panel a filled disc "
                "with its glyph cut out, red with a cross in the left and green with a check in the "
                "right.",
                ground=None, lit=False,
                title="Flat seats tilt your pelvis",
                where="Along the bottom edge, starting from the left", dark=True),
            product=False),
        opt("03-mechanism-ghostbody", None, "type: 03-mechanism-ghostbody",
            "The same correction as the body mechanism: a white seated mannequin, pelvis rolled back "
            "on a plain seat, upright on the product.",
            "Needs the product photo. RECOMMENDED at image 3 with a tailbone message, so picking it "
            "here spends the gallery's mechanism twice.",
            ghost("the hips and lower back, showing the pelvis and the lumbar vertebrae",
                  "the pelvis rolled back, the lumbar vertebrae flattened",
                  "the pelvis upright, the lumbar vertebrae curved forward",
                  "a blue band beside the lumbar vertebrae, right panel only",
                  title="Hips level, back supported", where="Along the bottom edge, from the left")),
    ],
})

SLOTS.append({
    "slot_id": "media.gallery.2.image", "role": "mechanism", "kind": "gallery", "ratio": "1:1",
    "asset": "590-03-gallery2-ghostbody.png",
    "placement": "Product card gallery, image 3, the mechanism tile.",
    "recommended": "A",
    "rationale":
        GALLERY_NOTE + " The page's tailbone promise ('Relieves tailbone pressure evenly', the hero's "
        "'Tailbone Relief') is invisible, so it is drawn through a body. FIT: "
        "`03-mechanism-ghostbody` is the mechanism row's body type, and `body_contact: true` keeps it "
        "in. PLACE: the mechanism tile sits at image 3–4. FEATURE KEY `pressure-relief`. B indicts the "
        "flat seat with the product absent; C argues the same relief as a component comparison.",
    "gif": no_gif("A two-panel render is inspected; the pressure it draws is a held distribution."),
    "options": [
        opt("03-mechanism-ghostbody", None, "baseline",
            "The seated mannequin opened at the hips: the tailbone pressed into a plain seat, free of "
            "the seat on the product.",
            "Needs the product photo. The body's layer list stops at the pelvis; nothing deeper is "
            "drawn. Title 4 words.",
            ghost("the hips, showing the pelvis, the sitting bones and the tailbone",
                  "the tailbone pressed into the seat",
                  "the weight under the sitting bones, the tailbone clear",
                  "a red overlay on the tailbone, left panel only; a blue band under the sitting "
                  "bones, right panel only",
                  title="Takes pressure off tailbone", where="Along the bottom edge, from the left")),
        opt("02-cause-anatomy", "--diagnostic", "type: 02-cause-anatomy",
            "A hard flat seat loading the tailbone, drawn in the pelvis, against a seat that carries "
            "the weight under the sitting bones.",
            "Needs no photo: the product is absent on an LP2 cause tile. RECOMMENDED nowhere in the "
            "gallery, and at `problem.items.1` in its section form.",
            compose(
                "2D illustration, airbrushed: soft gradients and modelled volume. Not photography, "
                "not 3D. Two equal panels side by side.",
                "A seated body seen from the side in both panels, the hips large in the frame. "
                "Ground: one continuous deep muted slate-blue field, one step lighter on the "
                "right.\n\n"
                "In each panel the pelvis, the two sitting bones and the tailbone are drawn in warm "
                "ivory over a translucent outline of the body.\n\n"
                "Left panel, the wrong state: the body sits on a hard flat seat, rolled back so the "
                "tailbone takes the weight. Right panel, the correct state: the same body on a "
                "plain contoured support in silhouette, the weight on the sitting bones and the "
                "tailbone clear.\n\n"
                "Marks: a flat red glow on the tailbone in the left panel only; one blue line under "
                "the sitting bones in the right. In the top corner of each panel a filled disc with "
                "its glyph cut out, red with a cross in the left and green with a check in the right.",
                ground=None, lit=False,
                title="Hard seats load the tailbone",
                where="Along the bottom edge, starting from the left", dark=True),
            product=False),
        opt("03-spec-split", None, "type: 03-spec-split",
            "A flat pad flattened under the tailbone against a contoured core that leaves the base "
            "of the spine free, the product small below.",
            "Needs the product photo, for the inset only. RECOMMENDED at image 5 with another "
            "message, so picking it here puts the type in the gallery twice.",
            compose(
                "High-contrast technical comparison graphic, e-commerce, sharp.",
                "One diagonal runs from the lower left corner of the frame to the upper right corner.\n\n"
                "Lower left half, photographed in a dim unstyled room, desaturated: a generic "
                "unbranded flat foam seat pad with a deep hollow pressed into its rear edge.\n\n"
                "Upper right half, a 3D render against a dark gradient with cool rim lighting: the "
                "same class of component in its improved form, a contoured seat core whose rear "
                "edge is shaped away where the base of the spine sits.\n\n"
                "A thin glowing line runs along the diagonal. In the lower left half a flat solid red "
                "disc with a cross cut out of it; in the upper right half a flat solid green disc "
                "with a check cut out of it, both the same diameter.",
                place="Render it whole at about 22% of the frame width, alone on a plain ground "
                      "inside a rounded rectangle along the bottom edge, left of centre.",
                ground=None, lit=False,
                title="Takes pressure off tailbone",
                where="In the top-left corner", dark=True)),
    ],
})

SLOTS.append({
    "slot_id": "media.gallery.3.image", "role": "mechanism", "kind": "gallery", "ratio": "1:1",
    "asset": "590-04-gallery3-macro.png",
    "placement": "Product card gallery, image 4, the one-piece tile.",
    "recommended": "A",
    "rationale":
        GALLERY_NOTE + " The page's defining feature is the one-piece L ('Prevents the seat base and "
        "lumbar support from separating'). FIT: `03-spec-macro` is the corpus's commonest mechanism "
        "tile (13 sources) and sits outside the mechanism budget; its LP2 law allows one macro to a "
        "gallery, and this is it. FEATURE KEY `one-piece`. B argues the same feature against a "
        "two-piece pad and roll; C separates the cover from the one-piece core.",
    "gif": no_gif("A macro reveals a surface; the press is a held moment rather than a change."),
    "options": [
        opt("03-spec-macro", None, "baseline",
            "The curve where the seat rises into the back, one piece, a hand pressing into it.",
            "Needs the product photo. The region is a true region of the photograph; no cover is cut "
            "open. Title 4 words, off the texture.",
            compose(
                "Polished commercial studio macro photography, close range, razor sharp, high detail.",
                "That curve fills about 70% of the frame, the surface resolved exactly as the photo "
                "shows it under raking light from the left, reading as one continuous piece with no "
                "seam and no gap between seat and back. Caught mid-use: a hand in a knit sleeve "
                "presses into the curve from the right, the surface giving under the fingers and "
                "holding its shape around them. The upper left of the frame falls to a soft pale "
                "blur, clear of the texture.",
                place="The magnified region is a true region of the product: the curve where its "
                      "seat section rises into its upright section, same geometry, same material, "
                      "same finish.",
                ground=SEAMLESS,
                title="One piece, no gap",
                where="In the upper left, on the blurred background and off the texture")),
        opt("03-spec-split", None, "type: 03-spec-split",
            "A flat pad and a strap-on roll with a gap between them, against a one-piece moulded "
            "core, the product small below.",
            "Needs the product photo, for the inset only. RECOMMENDED at image 5, so picking it here "
            "puts the type in the gallery twice.",
            compose(
                "High-contrast technical comparison graphic, e-commerce, sharp.",
                "One diagonal runs from the lower left corner of the frame to the upper right corner.\n\n"
                "Lower left half, photographed in a dim unstyled room, desaturated: a generic flat "
                "foam seat pad and a separate strap-on lumbar roll on a chair, an open gap between "
                "them where the seat meets the back.\n\n"
                "Upper right half, a 3D render against a dark gradient with cool rim lighting: the "
                "same class of component in its improved form, a one-piece moulded core whose seat "
                "section rises into an upright back section, the light running unbroken along the "
                "curve between them.\n\n"
                "A thin glowing line runs along the diagonal. In the lower left half a flat solid red "
                "disc with a cross cut out of it; in the upper right half a flat solid green disc "
                "with a check cut out of it, both the same diameter.",
                place="Render it whole at about 22% of the frame width, alone on a plain ground "
                      "inside a rounded rectangle along the bottom edge, left of centre.",
                ground=None, lit=False,
                title="One piece, no gap",
                where="In the top-left corner", dark=True)),
        opt("03-spec-explode", None, "type: 03-spec-explode",
            "The cover lifted clear of the one-piece core, the core the brightest part of the frame.",
            "Needs the product photo. Only parts the page names are drawn: the removable cover, the "
            "memory foam core and the grip base.",
            compose(
                "3D technical render, premium technical product visualization, sharp and high "
                "detail. Not photography.",
                "The core is the brightest, sharpest and most central part of the frame, one piece "
                "from seat to back. Across the ground, at very low contrast, a sparse square lattice "
                "of fine straight lines.",
                place="Render its parts separated along one vertical axis, in assembly order from the "
                      "top down: the removable cover lifted clear; the one-piece memory foam core; "
                      "the non-slip grip base beneath it. Each part is complete, in the reference's "
                      "own material and colour, and nothing is drawn that the product does not "
                      "contain.",
                ground=SEAMLESS, lit=False,
                title="Built as one piece",
                where="In the upper left, on quiet space")),
    ],
})

SLOTS.append({
    "slot_id": "media.gallery.4.image", "role": "comparison", "kind": "gallery", "ratio": "1:1",
    "asset": "590-05-gallery4-spec-split.png",
    "placement": "Product card gallery, image 5, the grip tile.",
    "recommended": "A",
    "rationale":
        GALLERY_NOTE + " The page answers a named objection here: 'Does it slide forward on smooth "
        "leather car seats?' — 'an anti-slip grip texture that anchors securely'. The difference "
        "between a sliding pad and a gripping one IS visible in a still, so a comparison is honest. "
        "FIT: `03-spec-split` argues a component difference; it fills the gallery's comparison slot "
        "in the mechanism budget beside image 3's mechanism. FEATURE KEY `non-slip`. B shows the "
        "claim as a calm driver on a leather seat; C is a macro, and the gallery's one macro is "
        "image 4.",
    "gif": {"eligible": True, "form": "whole-frame", "kind": "proof", "type_id": "proof",
            "rung": "natural",
            "reason": "The claim is a behaviour under movement: under braking a plain pad slides and "
                      "this one stays. A still can only show the end of that; a loop shows it "
                      "happening, and the proof type asks for one variable changing in one frame.",
            "brief": "Locked camera on the front edge of a leather car seat. The car brakes: a "
                     "generic flat pad on the left seat slides forward and tips over the edge, while "
                     "the product on the matching right seat does not move. Nothing else moves, "
                     "and the loop does not cut."},
    "options": [
        opt("03-spec-split", None, "baseline",
            "A plain pad slid off a leather seat against a gripping base, the product small below.",
            "Needs the product photo, for the inset only. The inset sits along the bottom, left of "
            "centre, so the bottom-right corner stays empty.",
            compose(
                "High-contrast technical comparison graphic, e-commerce, sharp.",
                "One diagonal runs from the lower left corner of the frame to the upper right corner.\n\n"
                "Lower left half, photographed in a dim unstyled car, desaturated: a generic "
                "unbranded flat foam seat pad slid forward off a smooth leather driver's seat and "
                "hanging over its front edge.\n\n"
                "Upper right half, a 3D render against a dark gradient with cool rim lighting: the "
                "same class of component in its improved form, a seat cushion base with a dense "
                "textured grip underside pressed flat to a leather seat surface.\n\n"
                "A thin glowing line runs along the diagonal. In the lower left half a flat solid red "
                "disc with a cross cut out of it; in the upper right half a flat solid green disc "
                "with a check cut out of it, both the same diameter.",
                place="Render it whole at about 22% of the frame width, alone on a plain ground "
                      "inside a rounded rectangle along the bottom edge, left of centre.",
                ground=None, lit=False,
                title="Stays put on leather",
                where="In the top-left corner", dark=True)),
        opt("06-relief-hero", "--commercial", "type: 06-relief-hero",
            "A driver in stop-start traffic, relaxed, the product exactly where he set it on a "
            "leather seat.",
            "Needs the product photo. RECOMMENDED at the hero and at image 6 with other messages, so "
            "picking it here puts the type in the gallery twice.",
            compose(
                "Commercial lifestyle photograph. One frame, no panels, no insets.",
                "A North American man in his forties waits at a red light in city traffic, one hand "
                "loose on the wheel, looking ahead through the windscreen rather than at the camera. "
                "His back rests against the product's upright section along its whole length, and "
                "the product sits square on the leather seat, not shifted an inch. The upper left "
                "of the frame is the quiet headliner.",
                place="Render it whole at about 25% of the frame height, on the leather driver's "
                      "seat under him and behind his lower back as one piece, seen from a rear "
                      "three-quarter angle from the passenger side, " + HOST + "."),
            axes={"register": "commercial", "inset_mode": "none"}),
        opt("03-spec-macro", None, "type: 03-spec-macro",
            "The grip base against leather in close-up, the seat's stitching sharp beside it.",
            "Needs the product photo. The gallery keeps one macro, and `media.gallery.3` holds it, so "
            "picking this moves that tile to its option B.",
            compose(
                "Polished commercial studio macro photography, close range, razor sharp, high detail.",
                "Where the base meets a leather car seat, the surface is resolved exactly as the "
                "photo shows it under raking light, pressed flat and square to the leather, the "
                "seat's stitching sharp beside it. The upper left of the frame falls to a soft blur "
                "of the seat back.",
                place="The magnified region is a true region of the product: the edge of its base "
                      "where it rests on the seat, same geometry, same material, same finish.",
                ground=ROOM,
                title="Stays put on leather",
                where="In the upper left, on the blurred background and off the texture")),
    ],
})

SLOTS.append({
    "slot_id": "media.gallery.5.image", "role": "outcome", "kind": "gallery", "ratio": "1:1",
    "asset": "590-06-gallery5-relief-hero.png",
    "placement": "Product card gallery, image 6, the closing outcome tile, wordless.",
    "recommended": "A",
    "rationale":
        GALLERY_NOTE + " The gallery closes on the result the page sells to its drivers: 'Dampens "
        "road bumps and jarring movement during daily commuting and long trips'. FIT: "
        "`06-relief-hero` takes the closing tile. WORDS: the gallery keeps at least one wordless "
        "tile, and this is it. FEATURE KEY `context:long-drive`. B is the same relief as a public "
        "moment at a truck stop; C is the range of long-sitting drivers.",
    "gif": no_gif("A held after-state; the road moving outside would be ambient motion, which is "
                  "off by default."),
    "options": [
        opt("06-relief-hero", "--commercial", "baseline",
            "A driver on an open country highway, loose and at ease, the product under and behind him.",
            "Needs the product photo. Wordless by the gallery's count.",
            compose(
                "Commercial lifestyle photograph. One frame, no panels, no insets.",
                "A North American man in his fifties drives an open country highway in the "
                "afternoon, one hand loose on the wheel, shoulders down, looking out at the long road "
                "ahead rather than at the camera. His back rests against the product's upright "
                "section along its whole length, and his hips sit level with his knees. Through the "
                "windscreen the road runs on toward low hills; a water bottle sits in the cup holder.",
                place="Render it whole at about 25% of the frame height, on the driver's seat under "
                      "him and behind his lower back as one piece, seen from a rear three-quarter "
                      "angle from the passenger side, " + HOST + "."),
            axes={"register": "commercial", "inset_mode": "none"}),
        opt("06-relief-scene", None, "type: 06-relief-scene",
            "A long-haul driver climbing down from his cab at a truck stop, easy and straight, the "
            "product on the seat behind him.",
            "Needs the product photo. Counts as a place scene. RECOMMENDED at `why.photo` with a "
            "different moment.",
            compose(
                "Candid documentary photograph, single frame. Natural and unposed, as a passer-by "
                "could have taken it.",
                "A North American man in his fifties in a work jacket climbs down from the cab of his "
                "truck at a truck stop in the late afternoon, one hand on the grab rail, stepping "
                "down easily with a straight back, looking toward the diner rather than at the "
                "camera. Around him: a row of parked trucks, a fuel island, two blurred drivers "
                "further off.",
                place="Render it whole at about 12% of the frame height, on the driver's seat behind "
                      "him, seen through the open cab door, " + HOST + ".")),
        opt("05-persona-grid", "--2x2", "type: 05-persona-grid",
            "Four long-sitting drivers in four cabs, one photographic finish.",
            "Needs the product photo. Weakest at tile size: four cells inside one square.",
            compose(
                "Clean lifestyle collage for e-commerce, bright, airy, sharp. Four equal cells, thin "
                "white gutters, no outer border, no graphic overlay of any kind.",
                "The product is visible and unobstructed in every cell, in place on the seat, and "
                "every cell shares one photographic finish.\n\n"
                "Top left: a North American man in his fifties at the wheel of a truck on a highway, "
                "flat afternoon light.\n\n"
                "Top right: a North American woman in her thirties driving a hatchback to work, "
                "morning light.\n\n"
                "Bottom left: a North American man in his forties in a rideshare car at night, city "
                "lights outside.\n\n"
                "Bottom right: a North American woman in her sixties on a road trip, a map on the "
                "passenger seat, warm evening light.\n\n"
                "No two cells share a palette, a light or a posture; nobody looks at the camera.",
                place="Show it whole in every cell, on the seat under each driver, " + HOST + "."),
            axes={}),
    ],
})

# ================================================================== the buyer wall
TRUSTED_RATIONALE = (
    "The three tiles are a REPEATING SECTION, so the set takes the three types and every tile "
    "follows the owner's pick (ADR-022); `05-social-snapshot`'s set law asks each tile for a "
    "different room class, light and distance. Buyer tiles are always generated on LP2 (owner "
    "decision, ADR-096), and G14's attribution test fires: each card sits beside 'Customer Review' "
    "and 'Verified Buyer', so the slot ships FLAGGED (ADR-089). No name, star row or badge enters "
    "the image. B is the same tile with its owner in it; C is the casting reading and is weakest at "
    "tile size.")
TRUSTED_FLAG = {
    "flag": "origin-claim-lead",
    "note": "trusted.cards.N.source reads 'Customer Review' and trusted.cards.N.verified reads "
            "'Verified Buyer' beside the photo, which claims customer origin for it (ADR-088). The "
            "frame carries no name, badge or star row. The merchant chooses between this prompt and "
            "a real customer photograph."}
SNAP_HEAD = "A real customer's phone photo. One frame, no layout, no layers."
UGC_HEAD = "A phone photo taken by an ordinary person in their own space. One frame, no panels, no insets."
GRID_HEAD = ("Clean lifestyle collage for e-commerce, bright, airy, sharp. Four equal cells, thin white "
             "gutters, no outer border, no graphic overlay of any kind.")
WALL = [
    ("trusted.cards.1.photo", "590-07-trusted1-snapshot.png",
     "Buyer card 1, beside 'It stopped the burning sensation in my hips after long highway shifts.'",
     "a truck cab at a highway truck stop at dusk",
     "The product simply where it now lives: on the driver's seat of a long-haul truck at a truck stop "
     "at dusk, the cab as it is — a jacket over the seat back, a thermos in the door pocket, a "
     "logbook face down on the dash. The cab's dome light and the last daylight through the "
     "windscreen, no studio light. The camera is a phone held in one hand from the cab door, framing "
     "slightly off-centre, mild noise in the shadows.",
     "a trucker at the wheel at dusk",
     "A North American man in his fifties in a work jacket sits back at the wheel of his truck at "
     "dusk, both hands loose in his lap, looking out through the windscreen rather than at the "
     "camera, his face turned away. His back rests against the product's upright section.",
     [("a North American man in his fifties at the wheel of a truck at dusk",
       "a North American woman in her thirties at an office desk in daylight"),
      ("a North American man in his forties in a rideshare car at night",
       "a North American woman in her sixties at a kitchen table in the morning")]),
    ("trusted.cards.2.photo", "590-08-trusted2-snapshot.png",
     "Buyer card 2, beside 'I work eight hours at my desk and no longer dread the commute.'",
     "a commuter car in a parking garage in the morning",
     "The product mid-use by its owner, the person present only incidentally: on the driver's seat of "
     "a small commuter car in a parking garage in the morning, a hand in a blazer sleeve setting a "
     "laptop bag on the passenger seat. Flat fluorescent garage light and a little daylight from the "
     "ramp, no studio light. The camera is a phone held close, framing tilted, focus casual.",
     "a commuter settling in for the drive home",
     "A North American woman in her thirties in office clothes sits back in the driver's seat of her "
     "car in a parking garage, reaching for her seat belt, looking ahead rather than at the camera. "
     "Her back rests against the product's upright section.",
     [("a North American woman in her thirties in a commuter car in a parking garage",
       "a North American man in his twenties at a gaming desk at night"),
      ("a North American man in his fifties in a van on a building site",
       "a North American woman in her forties at a reception desk under ceiling light")]),
    ("trusted.cards.3.photo", "590-09-trusted3-snapshot.png",
     "Buyer card 3, beside 'Solid build that does not slide around on leather car upholstery.'",
     "a leather car seat in a driveway in bright daylight",
     "The product simply where it now lives: on the leather driver's seat of a family car parked in a "
     "suburban driveway in bright midday light, the door open, a pair of sunglasses on the dash and a "
     "child's water bottle in the rear footwell. Bright daylight, no studio light. The camera is a "
     "phone held at standing height from outside the open door, the seat small in the frame.",
     "a driver getting in at midday",
     "A North American man in his sixties in a polo shirt lowers himself into the leather driver's "
     "seat of his car in a sunny driveway, one hand on the door frame, looking down at the "
     "ignition rather than at the camera. The product sits square under him and behind his back.",
     [("a North American man in his sixties getting into a car in a sunny driveway",
       "a North American woman in her twenties at a café table on a hard chair"),
      ("a North American man in his thirties in a wheelchair at a desk",
       "a North American woman in her fifties in a van at a delivery stop")]),
]


def wall_slot(slot_id, asset, placement, where, snap_body, ugc_gloss, ugc_body, cells):
    grid = "\n\n".join([f"Top left: {cells[0][0]}.", f"Top right: {cells[0][1]}.",
                        f"Bottom left: {cells[1][0]}.", f"Bottom right: {cells[1][1]}."])
    return {
        "slot_id": slot_id, "role": "social-proof", "kind": "buyer-wall", "ratio": "1:1",
        "asset": asset, "placement": placement, "recommended": "A",
        "rationale": TRUSTED_RATIONALE, "compliance": TRUSTED_FLAG,
        "gif": no_gif("A customer snapshot argues that the thing exists in a real place, a held "
                      "state; this type bans every added element."),
        "options": [
            opt("05-social-snapshot", None, "baseline",
                f"The product in {where}, photographed as found.",
                "Needs the product photo. The tile carries no name, badge or star row; the page is "
                "what attributes it, which is why the slot ships flagged.",
                compose(SNAP_HEAD, snap_body + "\n\nNobody's face is in the frame.",
                        place="Render it whole at about 40% of the frame height, exactly as the "
                              "reference shows.",
                        ground=ROOM),
                axes={"register": "ugc"}),
            opt("06-relief-hero", "--ugc", "type: 06-relief-hero",
                f"The same tile with its owner in it: {ugc_gloss}.",
                "Needs the product photo. The same type is recommended at the hero in its commercial "
                "register.",
                compose(UGC_HEAD, ugc_body + " The framing is casual and a little too close, with no "
                        "styling.",
                        place="Render it whole at about 25% of the frame height, on the seat under "
                              "them and behind them as one piece, " + HOST + ".",
                        ground=ROOM),
                axes={"register": "ugc", "inset_mode": "none"}),
            opt("05-persona-grid", "--2x2", "type: 05-persona-grid",
                "The wall's job read as casting: four sitters in four places, one finish.",
                "Needs the product photo. Weakest at tile size; only one tile on the wall could carry "
                "it before the wall stops reading as three customers.",
                compose(GRID_HEAD, "The product is visible and unobstructed in every cell, in place on "
                        "the seat, and every cell shares one photographic finish.\n\n" + grid +
                        "\n\nNo two cells share a palette, a light or a posture; nobody looks at the "
                        "camera.",
                        place="Show it whole in every cell, on the seat under each person, " + HOST + "."),
                axes={}),
        ],
    }


for args in WALL:
    SLOTS.append(wall_slot(*args))

# ================================================================== the problem block
PROBLEM_NOTE = ("Each item pairs an old way with its fix, and the items route one by one (cross-slot "
                "rule 10). Section images carry no words (ADR-096).")
SPLIT_HEAD = ("E-commerce comparison photograph, high contrast, sharp. Two panels, a hard vertical split "
              "at 50/50, each running to the frame edge.")
CAUSE_HEAD = ("2D illustration, airbrushed: soft gradients and modelled volume. Not photography, not 3D. "
              "Two equal panels side by side.")
SPEC_HEAD = "High-contrast technical comparison graphic, e-commerce, sharp."
SPEC_INSET = ("Render it whole at about 22% of the frame width, alone on a plain ground inside a rounded "
              "rectangle along the bottom edge, left of centre.")
SPEC_MARKS = ("A thin glowing line runs along the diagonal. In the lower left half a flat solid red disc "
              "with a cross cut out of it; in the upper right half a flat solid green disc with a check "
              "cut out of it, both the same diameter.")
SLOTS.append({
    "slot_id": "problem.items.0.image", "role": "problem-agitation", "kind": "section", "ratio": "4:3",
    "asset": "590-10-problem0-pain-split.png",
    "placement": "Beside 'Flat pads sink down and leave your lower back unsupported'.",
    "recommended": "A",
    "rationale":
        PROBLEM_NOTE + " This item's old way is a flat pad that sinks, and its fix is the continuous "
        "L-core. FIT: `01-pain-split --oldway` is the old way against the new in one frame. B draws "
        "the unsupported lumbar curve with the product absent; C argues the component difference.",
    "gif": no_gif("Two panels are compared, not watched."),
    "options": [
        opt("01-pain-split", "--oldway", "baseline",
            "The same driver on the same seat: sunk into a flat pad with a gap behind his back, then "
            "supported by the product.",
            "Needs the product photo, for the right panel.",
            compose(
                SPLIT_HEAD,
                "The same man in both panels, named once: a North American man in his fifties in a "
                "denim work shirt, seen from the side at seat height, in the same car's driver's "
                "seat, in the same afternoon light through the side window.\n\n"
                "Left panel, grayscale: on a flat foam pad that has sunk under him, his hips low, a "
                "gap between the seat back and his lower back, his shoulders rounded.\n\n"
                "Right panel, full colour: on the product, his lower back supported along its whole "
                "length, his shoulders over his hips; brighter and airier than the left.\n\n"
                + SPLIT_DISCS,
                place=SPLIT_PLACE.format(who="him"),
                ground=None, lit=False)),
        opt("02-cause-anatomy", "--diagnostic", "type: 02-cause-anatomy",
            "A flat pad lets the lumbar curve collapse; a continuous support holds it.",
            "Needs no photo: the product is absent or a silhouette on an LP2 cause image.",
            compose(
                CAUSE_HEAD,
                "A seated body seen from the side in both panels, the whole body in shot. Ground: one "
                "continuous deep muted slate-blue field, one step lighter on the right.\n\n"
                "In each panel the pelvis, the tailbone and the five lumbar vertebrae are drawn in "
                "warm ivory over a translucent outline of the body.\n\n"
                "Left panel, the wrong state: the body sits on a flat sunken pad, nothing behind the "
                "lower back, the lumbar vertebrae sagging backward into an empty gap. Right panel, "
                "the correct state: the same body with a plain continuous L-shaped support in "
                "silhouette, the lumbar curve held forward.\n\n"
                "Marks: one red curved line along the sagging vertebrae in the left panel; one blue "
                "curved line along them in the right. In the top corner of each panel a filled disc "
                "with its glyph cut out, red with a cross in the left and green with a check in the "
                "right.",
                ground=None, lit=False),
            product=False),
        opt("03-spec-split", None, "type: 03-spec-split",
            "A flat pad and a separate roll with a gap between them, against a one-piece core.",
            "Needs the product photo, for the inset only.",
            compose(
                SPEC_HEAD,
                "One diagonal runs from the lower left corner of the frame to the upper right corner.\n\n"
                "Lower left half, photographed in a dim unstyled room, desaturated: a generic flat "
                "seat pad and a separate lumbar roll on an office chair, an open gap between them.\n\n"
                "Upper right half, a 3D render against a dark gradient with cool rim lighting: the "
                "same class of component in its improved form, a one-piece moulded core whose seat "
                "section rises into an upright back section.\n\n" + SPEC_MARKS,
                place=SPEC_INSET, ground=None, lit=False)),
    ],
})

SLOTS.append({
    "slot_id": "problem.items.1.image", "role": "cause", "kind": "section", "ratio": "4:3",
    "asset": "590-11-problem1-cause-anatomy.png",
    "placement": "Beside 'Separate pillows push upper back forward while hips drop below knees'.",
    "recommended": "A",
    "rationale":
        PROBLEM_NOTE + " This item explains WHY the old way hurts — a separate pillow pushes the upper "
        "back forward while the hips drop — so the section's copy moves the role to `cause`. FIT: "
        "`02-cause-anatomy --diagnostic`, with the product absent as its LP2 law asks. B is the same "
        "argument as a photographed split; C draws it as the product's own mechanism.",
    "gif": {"eligible": True, "form": "whole-frame", "kind": "cause", "type_id": "cause",
            "rung": "natural",
            "reason": "The claim IS a state changing under a cause: the pillow pushes the shoulders "
                      "forward and the pelvis rolls back as the hips sink. `registry/gif-types/cause.md` "
                      "asks for one continuous state change, and the left panel holds its end.",
            "brief": "Hold the left panel's illustration. Over three seconds the strap-on pillow "
                     "presses the upper back forward, the pelvis rotates backward and the hips sink "
                     "below the knees, and the red line along the lumbar vertebrae deepens. The right "
                     "panel is not animated, and the loop does not cut."},
    "options": [
        opt("02-cause-anatomy", "--diagnostic", "baseline",
            "A strap-on pillow pushing the upper back forward while the hips sink, against a level, "
            "continuous support.",
            "Needs no photo: the product is absent or a silhouette.",
            compose(
                CAUSE_HEAD,
                "The whole seated body is in shot in both panels, seen from the side, the seat small "
                "within the frame. Ground: one continuous deep muted slate-blue field, one step "
                "lighter on the right.\n\n"
                "In each panel the named structures are drawn in warm ivory over a translucent "
                "outline of the body: the pelvis, the tailbone, the five lumbar vertebrae, the "
                "upper spine and the thigh bone.\n\n"
                "Left panel, the wrong state: a plain strap-on pillow sits high behind the shoulder "
                "blades, pushing the upper spine forward, while the hips sink below the knees and "
                "the pelvis rolls backward.\n\n"
                "Right panel, the correct state: the same body with a plain continuous L-shaped "
                "support in silhouette, the hips level with the knees, the pelvis upright and the "
                "spine stacked over it.\n\n"
                "Marks: one red double-headed arrow at the pillow in the left panel and nowhere "
                "else; one curved line along the lumbar vertebrae in each panel, red in the left and "
                "blue in the right; in the top corner of each panel a filled disc with its glyph cut "
                "out, red with a cross in the left and green with a check in the right.",
                ground=None, lit=False),
            product=False),
        opt("01-pain-split", "--mirror", "type: 01-pain-split",
            "The same commuter photographed twice: shoulders shoved forward by a strap-on pillow, "
            "then level on the product.",
            "Needs the product photo, for the right panel. RECOMMENDED in the gallery at image 2 with "
            "another message.",
            compose(
                SPLIT_HEAD,
                "The same woman in both panels, named once: a North American woman in her thirties "
                "in a navy blazer, seen from the side at seat height from the same distance, in the "
                "same car's driver's seat, in the same morning light through the side window.\n\n"
                "Left panel, in grayscale: a separate strap-on pillow sits high behind her shoulder "
                "blades, pushing her shoulders toward the wheel, while her hips sink below her knees.\n\n"
                "Right panel, in full colour: the same woman in the same seat on the product, her "
                "hips level with her knees and her back upright and supported. The right panel is "
                "brighter and airier than the left.\n\n" + SPLIT_DISCS,
                place=SPLIT_PLACE.format(who="her"),
                ground=None, lit=False)),
        opt("03-mechanism-ghostbody", None, "type: 03-mechanism-ghostbody",
            "A white seated mannequin: a pillow at mid-back tipping the pelvis back, against the "
            "product holding it upright.",
            "Needs the product photo. RECOMMENDED at image 3 and at `expert.photo` with other "
            "messages.",
            ghost("the hips and back, showing the pelvis and the spine",
                  "a plain pillow behind the shoulder blades pushing the upper spine forward, the "
                  "pelvis rolled back",
                  "the pelvis upright, the spine stacked over it",
                  "a red overlay on the pelvis, left panel only; a blue band beside the lower spine, "
                  "right panel only")),
    ],
})

SLOTS.append({
    "slot_id": "problem.items.2.image", "role": "comparison", "kind": "section", "ratio": "4:3",
    "asset": "590-12-problem2-spec-split.png",
    "placement": "Beside 'Cheap foam flattens out under body weight within a few weeks'.",
    "recommended": "A",
    "rationale":
        PROBLEM_NOTE + " This item names what the old way is made of, so the copy moves the role to "
        "`comparison`: cheap foam that flattens against a slow-rebound core. FIT: `03-spec-split`. B "
        "shows the rebound itself under a hand; C is the same claim over time, the product unchanged.",
    "gif": no_gif("The diagonal is inspected; the flattening it shows happened before the frame."),
    "options": [
        opt("03-spec-split", None, "baseline",
            "A flattened foam pad against a dense, full core, the product small below.",
            "Needs the product photo, for the inset only. RECOMMENDED also at image 5 in the gallery "
            "with the grip message.",
            compose(
                SPEC_HEAD,
                "One diagonal runs from the lower left corner of the frame to the upper right corner.\n\n"
                "Lower left half, photographed in a dim unstyled room, desaturated: a generic flat "
                "foam seat pad of the ordinary kind, its top pressed into a shallow hollow that has "
                "not come back, one corner crushed and rounded.\n\n"
                "Upper right half, a 3D render against a dark gradient with cool rim lighting: the "
                "same class of component in its improved form, a dense slow-rebound memory foam core, "
                "its surface full and even.\n\n" + SPEC_MARKS,
                place=SPEC_INSET, ground=None, lit=False)),
        opt("03-spec-macro", None, "type: 03-spec-macro",
            "A hand pressing into the foam, the cells compressed under the fingers and standing open "
            "again just behind them.",
            "Needs the product photo. The region is the product's own seat surface; no cover is cut "
            "open.",
            compose(
                "Polished commercial studio macro photography, extreme close range, razor sharp, high "
                "detail.",
                "The seat surface fills about 80% of the frame, resolved exactly as the photo shows "
                "it under raking light. Caught mid-work: a hand presses into it at the left, the "
                "surface pressed down under the fingers and already rising again a short distance "
                "behind the press, so the recovery is visible in the same frame as the load.",
                place="The magnified region is a true region of the product: its seat surface, same "
                      "geometry, same material, same finish.",
                ground=SEAMLESS)),
        opt("04-proof-lockedframe", "--timelapse", "type: 04-proof-lockedframe",
            "The same product on the same kitchen chair on its first day and after months of daily "
            "use, the same height both times.",
            "Needs the product photo. Handheld, because the two halves are separated by time; no "
            "panel is favoured.",
            compose(
                "Honest documentary product photography, unstyled, natural, sharp. Two equal vertical "
                "panels packed across the frame with thin white gutters, no outer border.",
                "One framing for both panels, stated once: a phone at standing height beside a hard "
                "wooden kitchen chair at a table, the chair filling the lower two thirds, the table "
                "edge and a fruit bowl in the upper left. It reads as one shot taken twice.\n\n"
                "The only thing that changes is the day: in the left panel the product is new on the "
                "chair; in the right panel months later it stands the same height and shape, a tea "
                "towel now hanging over the chair back.\n\n"
                "Grade: one neutral grade across both panels, no panel warmer or brighter.",
                place="Render it whole on the chair in both panels, the same unit, identical in both, "
                      "" + HOST + ".",
                ground=None, lit=False),
            axes={"camera_lock": "handheld"}),
    ],
})

# ================================================================== why, how
SLOTS.append({
    "slot_id": "why.photo", "role": "outcome", "kind": "section", "ratio": "1:1",
    "asset": "590-13-why-relief-scene.png",
    "placement": "Beside 'Complete Ergonomic Geometry — relieve pelvic pressure and cushion road vibration'.",
    "recommended": "A",
    "rationale":
        "The block argues what the whole geometry buys: less pelvic pressure and a smoother drive. "
        "The section name sends it to `outcome`. FIT: `06-relief-scene`, relief shown in a public "
        "moment with the product standing as its own object; `result_visibility: on-body` keeps it "
        "in. B is the relief at the wheel; C is the geometry drawn through a body.",
    "gif": no_gif("A held after-state."),
    "options": [
        opt("06-relief-scene", None, "baseline",
            "After two hours on the road, a commuter walks away from her car in a supermarket car "
            "park, straight and unhurried, the product on the seat behind her.",
            "Needs the product photo. A different moment from the gallery's truck-stop option.",
            compose(
                "Candid documentary photograph, single frame. Natural and unposed, as a passer-by "
                "could have taken it.",
                "A North American woman in her forties crosses a supermarket car park mid-stride, a "
                "tote bag over one shoulder and her keys in her hand, her back straight and her step "
                "easy, looking toward the store entrance rather than at the camera. Behind her the "
                "driver's door of her car stands open. Around her: trolleys in a bay, painted lines, "
                "two blurred shoppers further off.",
                place="Render it whole at about 12% of the frame height, on the driver's seat of her "
                      "car, seen through the open door, " + HOST + ".")),
        opt("06-relief-hero", "--commercial", "type: 06-relief-hero",
            "A commuter at ease at the wheel on a rough city street, the product under and behind her.",
            "Needs the product photo. RECOMMENDED at the hero and at gallery image 6 with other "
            "moments.",
            compose(
                "Commercial lifestyle photograph. One frame, no panels, no insets.",
                "A North American woman in her forties drives down a patched city street in the "
                "morning, both hands easy on the wheel, shoulders down, looking ahead rather than "
                "at the camera. Her back rests against the product's upright section along its "
                "whole length, and her hips sit level with her knees.",
                place="Render it whole at about 25% of the frame height, on the driver's seat under "
                      "her and behind her lower back as one piece, seen from a rear three-quarter "
                      "angle from the passenger side, " + HOST + "."),
            axes={"register": "commercial", "inset_mode": "none"}),
        opt("03-mechanism-ghostbody", None, "type: 03-mechanism-ghostbody",
            "The complete geometry drawn: lumbar, pelvis and thighs supported at once on the product.",
            "Needs the product photo.",
            ghost("the hips and lower back, showing the pelvis, the lumbar vertebrae and the thigh bones",
                  "the pelvis rolled back, the lumbar vertebrae flattened",
                  "the pelvis upright, the lumbar curve held, the thighs level",
                  "right panel only, a blue band beside the lumbar vertebrae and another under the "
                  "thigh bones")),
    ],
})

SLOTS.append({
    "slot_id": "how.image", "role": "how-to-use", "kind": "section", "ratio": "1:1",
    "asset": "590-14-how-relief-hero.png",
    "placement": "Beside 'Here Is How It Works': place on seat, sit back, feel the relief.",
    "recommended": "A",
    "rationale":
        "The block's three steps are one act — set it on any chair and sit back — and "
        "`multi_step_usage: false` removes `03-use-sequence` from the pool, so a three-panel "
        "sequence is not offered. FIT: `06-relief-hero` shows the act and its result in one frame, "
        "on a hard dining chair so it does not repeat the hero's desk. B reads 'any chair' as a "
        "range of seats; C is the placing itself in close-up.",
    "gif": no_gif("The act is one movement already complete in the still; the sequence type that "
                  "would carry it is gated out."),
    "options": [
        opt("06-relief-hero", "--commercial", "baseline",
            "A man settling back onto the product on a hard kitchen chair, the laptop open in front "
            "of him.",
            "Needs the product photo.",
            compose(
                "Commercial lifestyle photograph. One frame, no panels, no insets.",
                "A North American man in his thirties has just sat back on a hard wooden chair at "
                "his kitchen table, one hand still on the chair back, his laptop open in front of "
                "him and a coffee beside it, looking at the screen rather than at the camera. His "
                "lower back rests fully against the product's upright section, and his hips have "
                "settled level with his knees.",
                place="Render it whole at about 28% of the frame height, on the wooden chair under "
                      "him and set flush against the chair back as one piece, seen from a side "
                      "three-quarter angle, " + HOST + "."),
            axes={"register": "commercial", "inset_mode": "none"}),
        opt("03-use-grid", None, "type: 03-use-grid",
            "Four seats the product sets straight onto: office chair, car seat, dining chair, "
            "wheelchair.",
            "Needs the product photo. RECOMMENDED at `uses.image`, so picking it here spends the type "
            "twice on the page with a close message.",
            compose(
                "Photographic grid of four equal cells in a 2×2, thin white gutters, no outer border.",
                "The product is visibly fitted to the seat in each cell, set flush against the back, "
                "and each cell has a different camera: an office chair from across a desk; a car's "
                "driver's seat from the open door; a wooden dining chair from above; a wheelchair "
                "from the side. Where a person is present they are only a hand setting the product "
                "in place, and no face appears in any cell. All four cells share one photographic "
                "register.",
                place="Preserve it exactly in every cell, fitted to the seat, " + HOST + ".")),
        opt("03-spec-macro", None, "type: 03-spec-macro",
            "Two hands pressing the upright section flush against a chair back.",
            "Needs the product photo. The gallery's one macro is image 4; this is a section.",
            compose(
                "Polished commercial studio macro photography, close range, razor sharp, high detail.",
                "Two hands press the product's upright section flush against the back of a wooden "
                "chair, the surface resolved exactly as the photo shows it under raking light, the "
                "joint between the product and the chair back closed along its whole length.",
                place="The magnified region is a true region of the product: its upright section "
                      "where it meets the chair back, same geometry, same material, same finish.",
                ground=ROOM)),
    ],
})

# ================================================================== what to expect: three pairs
PAIR_FLAG = {
    "flag": "origin-claim-lead",
    "note": "The block's kicker reads 'Real Results' above Before/After labels, which presents the pair "
            "as a measured result (G14, ADR-088). Pairs are always generated on LP2 (owner decision, "
            "ADR-096); the merchant chooses between this prompt and a real photograph."}
PAIR_POOL = ("Rule 11 of `mapping/pdp-dr-rules.md` fixes a before-and-after pair to two constructions — "
             "`01-pain-split`'s halves and `04-proof-lockedframe --timelapse` — so the pool for a pair "
             "holds two types, not three. No attribute gate or global rule removed anything else.")
PAIR_GIF = no_gif("One half of a pair; the page shows the two files side by side, and the change "
                  "lives between them rather than inside either.")
PAIR_HEAD = "Everyday photograph, natural and unposed, sharp. One frame, no panels, no insets."


def pair_files(slot_base, asset_base, placement, rationale, locked, variants, ratio, flag, snap=False):
    """`variants`: [(tid, variant, varies_on, gloss, note, before_state, after_state, before_prod,
    after_prod, axes)]. Each file is one slot; both carry the locked description word for word."""
    head = "A real person's phone photo, casual framing. One frame, no panels, no insets." if snap else PAIR_HEAD
    out = []
    for half in ("before", "after"):
        options = []
        for tid, variant, varies, gloss, note, b_state, a_state, b_prod, a_prod, axes in variants:
            state = b_state if half == "before" else a_state
            has = b_prod if half == "before" else a_prod
            body = locked + "\n\n" + state
            place = ("Render it whole in place on the seat, as the reference shows, " + HOST + "."
                     if has else None)
            options.append(opt(tid, variant, varies, gloss, note,
                               compose(head, body, place=place, ground=ROOM),
                               axes=axes, product=has))
        out.append({
            "slot_id": f"{slot_base}.{half}_image", "role": "proof" if not snap else "social-proof",
            "kind": "pair", "ratio": ratio,
            "asset": f"{asset_base}-{half}.png",
            "placement": f"{placement}, the {half.upper()} photograph.",
            "recommended": "A", "rationale": rationale, "compliance": flag,
            "pool_basis": PAIR_POOL, "pair_with": f"{slot_base}.{'after' if half == 'before' else 'before'}_image",
            "gif": PAIR_GIF, "options": options,
        })
    return out


GRAY = ""  # a pair differs in its state line alone, so neither half is desaturated
EXPECT_NOTE = ("A before-and-after pair is one argument in two files (cross-slot rule 11): both prompts "
               "carry one locked description word for word and differ in the state line. The template "
               "frames the pair at 4:5; the nearest legal ratio is 3:4 (ADR-016), and the template "
               "crops the rest. The stat beside it stays in HTML.")
SLOTS += pair_files(
    "expect.items.0", "590-15-expect0",
    "What To Expect, 'Day 1 — zero gap behind your lower back'",
    EXPECT_NOTE + " Day 1's claim is a gap closed the moment the product goes in, which is the old "
    "way against the new: A takes `01-pain-split`'s halves, both in colour, because a pair's two "
    "files differ in the state line alone and the lock's grade binds both. B reads the same day as "
    "a timelapse and is the weaker of the two.",
    "The same scene in both photographs of this pair: a North American man in his thirties in a light "
    "blue shirt at an office desk in a bright open-plan office, photographed from behind and to his "
    "right at seat height, framed from his shoulders to his knees, no face in frame, a monitor and a "
    "plant along the right edge.",
    [("01-pain-split", "--mirror", "baseline",
      "Day 1 as the old way and the new: a gap behind his lower back, then none.",
      "The before half has no product and needs no photo; the after half needs the product photo.",
      GRAY + "He sits on the bare office chair, an open gap between the chair back and the small of his "
      "back, his pelvis rolled back.",
      "He sits on the same chair with the product, the small of his back in full contact with its "
      "upright section, no gap anywhere.", False, True, {}),
     ("04-proof-lockedframe", "--timelapse", "type: 04-proof-lockedframe",
      "Day 1 as a morning and an evening: the product in place and no gap at either end of the day.",
      "Both halves need the product photo. No panel is favoured; one grade across both.",
      "It is the first morning: he has just sat down on the product, the small of his back against its "
      "upright section.",
      "It is the same day's evening, the office emptier and the light lower: he sits the same way, "
      "the small of his back still against the product's upright section.", True, True,
      {"camera_lock": "handheld"})],
    "3:4", PAIR_FLAG)

SLOTS += pair_files(
    "expect.items.1", "590-16-expect1",
    "What To Expect, 'Week 2 — comfortable sitting without shifting positions'",
    EXPECT_NOTE + " Week 2's claim is endurance across a working day, a claim made over time: A "
    "takes `04-proof-lockedframe --timelapse`, the start and the end of one day. B reads it as the "
    "old way against the new at the same late hour.",
    "The same scene in both photographs of this pair: a North American woman in her forties in a "
    "cardigan at a home-office desk by a window, photographed from the side at seat height, framed "
    "from her shoulders to her knees, no face in frame, a mug and a desk lamp on the desk.",
    [("04-proof-lockedframe", "--timelapse", "baseline",
      "The start and the end of a working day: the same settled posture on the product both times.",
      "Both halves need the product photo. No panel is favoured; one grade across both.",
      "It is the morning, bright daylight at the window: she sits back on the product, settled, "
      "typing.",
      "It is the evening, the lamp on and the window dark: she sits exactly as settled on the product, "
      "still typing.", True, True, {"camera_lock": "handheld"}),
     ("01-pain-split", "--mirror", "type: 01-pain-split",
      "The same late hour twice: shifting on a bare chair, then still on the product.",
      "The before half has no product; the after half needs the product photo.",
      GRAY + "It is the evening: she sits on the bare chair, shifted to its front edge, one hand "
      "pressed into her lower back.",
      "It is the evening: she sits back on the same chair on the product, settled, both hands on the "
      "keyboard.", False, True, {})],
    "3:4", PAIR_FLAG)

SLOTS += pair_files(
    "expect.items.2", "590-17-expect2",
    "What To Expect, 'Month 1 — total confidence'",
    EXPECT_NOTE + " Month 1 promises confidence backed by a trial; the picture it can carry is the "
    "product still holding its shape after a month of daily drives. A takes the timelapse; B the "
    "old way against the new after the same month.",
    "The same scene in both photographs of this pair: the driver's seat of a family car seen through "
    "the open driver's door from standing height, the seat base and back filling the frame, a "
    "sunglasses case on the passenger seat, flat overcast daylight.",
    [("04-proof-lockedframe", "--timelapse", "baseline",
      "The product on the same seat on its first day and after a month of daily drives, unchanged.",
      "Both halves need the product photo. No panel is favoured; one grade across both.",
      "It is the first day: the product sits new on the seat.",
      "It is a month later: the product sits the same height and shape on the seat, a parking "
      "receipt tucked into the door pocket.", True, True, {"camera_lock": "handheld"}),
     ("01-pain-split", "--oldway", "type: 01-pain-split",
      "After a month: a flat pad squashed thin, against the product unchanged.",
      "The before half has no product; the after half needs the product photo.",
      GRAY + "It is a month later: a flat foam pad on the seat has squashed thin and slid toward the "
      "front edge.",
      "It is a month later: the product sits full and square on the same seat.", False, True, {})],
    "3:4", PAIR_FLAG)

# ================================================================== uses, expert, safety
SLOTS.append({
    "slot_id": "uses.image", "role": "how-to-use", "kind": "section", "ratio": "4:3",
    "asset": "590-21-uses-use-grid.png",
    "placement": "Beside 'Support Wherever You Sit': Office, Car, Long Drives, Home.",
    "recommended": "A",
    "rationale":
        "The block lists places, not people, so it keeps `how-to-use` (Section routing). FIT: "
        "`03-use-grid`, one seat to a cell, the page's four places. B reads the list as the people "
        "who sit there; C is one of the four as a scene.",
    "gif": no_gif("A grid of places is read cell by cell; nothing changes."),
    "options": [
        opt("03-use-grid", None, "baseline",
            "Four seats in four places: an office chair, a car seat, a truck seat, a dining chair.",
            "Needs the product photo. No label, chip or badge in any cell.",
            compose(
                "Photographic grid of four equal cells in a 2×2, thin white gutters, no outer border.",
                "Each cell shows a different seat the product serves, in its own place, with a "
                "different camera:\n\n"
                "Top left: an office chair at a desk, photographed level from across the desk in "
                "window light.\n\n"
                "Top right: a car's driver's seat, photographed low from the open door in morning "
                "light.\n\n"
                "Bottom left: a truck cab's driver's seat on a long highway, photographed from the "
                "passenger side in flat afternoon light.\n\n"
                "Bottom right: a wooden dining chair at a kitchen table, photographed from above "
                "under a warm ceiling light.\n\n"
                "Nobody's face appears in any cell; where a person is present they are only a hand "
                "setting the product in place. All four cells share one photographic register.",
                place="Preserve it exactly in every cell, fitted to the seat, " + HOST + ".")),
        opt("05-persona-grid", "--2x2", "type: 05-persona-grid",
            "Four sitters: a desk worker, a commuter, a long-haul driver, a gamer at home.",
            "Needs the product photo.",
            compose(
                GRID_HEAD,
                "The product is visible and unobstructed in every cell, in place on the seat, and "
                "every cell shares one photographic finish.\n\n"
                "Top left: a North American woman in her thirties at an office desk in window light.\n\n"
                "Top right: a North American man in his forties driving to work in morning light.\n\n"
                "Bottom left: a North American man in his fifties at the wheel of a truck on a "
                "highway.\n\n"
                "Bottom right: a North American man in his twenties at a gaming desk at home at "
                "night.\n\n"
                "No two cells share a palette, a light or a posture; nobody looks at the camera.",
                place="Show it whole in every cell, on the seat under each person, " + HOST + ".")),
        opt("06-relief-hero", "--commercial", "type: 06-relief-hero",
            "Home: a woman relaxed at her dining table on a hard chair, the product under and "
            "behind her.",
            "Needs the product photo. One place of the four, so the weakest reading of the list.",
            compose(
                "Commercial lifestyle photograph. One frame, no panels, no insets.",
                "A North American woman in her sixties sits back at her dining table in the "
                "afternoon, a book open in front of her, looking at the page rather than at the "
                "camera. Her back rests against the product's upright section along its whole "
                "length.",
                place="Render it whole at about 28% of the frame height, on the hard dining chair "
                      "under her and behind her lower back as one piece, seen from a side "
                      "three-quarter angle, " + HOST + "."),
            axes={"register": "commercial", "inset_mode": "none"}),
    ],
})

SLOTS.append({
    "slot_id": "expert.photo", "role": "mechanism", "kind": "section", "ratio": "3:4",
    "asset": "590-22-expert-ghostbody.png",
    "placement": "Beside the quote 'Supporting both the lower back and pelvic base simultaneously "
                 "stops slouching at the source'.",
    "recommended": "A",
    "rationale":
        "An `expert` block shows no face (cross-slot rule 12), and this one names no person — "
        "'Ergonomic Focus · Core Design' — so its quoted claim decides the image. The claim is a "
        "mechanism: two zones supported at once. FIT: `03-mechanism-ghostbody`. B draws the slouch "
        "it stops with the product absent; C is two hands on the two zones. The template frames it "
        "at 4:5; the nearest legal ratio is 3:4.",
    "gif": no_gif("A two-panel render is inspected."),
    "options": [
        opt("03-mechanism-ghostbody", None, "baseline",
            "A white seated mannequin: slouched on a plain seat, then upright with the lower back "
            "and the pelvic base supported together.",
            "Needs the product photo. No face anywhere, by the type and by rule 12.",
            ghost("the hips and lower back, showing the pelvis, the tailbone and the lumbar vertebrae",
                  "slouched, the pelvis rolled back, the lumbar vertebrae flattened",
                  "upright, the pelvis level under the spine",
                  "right panel only, two blue bands at once, one beside the lumbar vertebrae and one "
                  "under the pelvis")),
        opt("02-cause-anatomy", "--diagnostic", "type: 02-cause-anatomy",
            "The slouch the quote names, drawn in the spine and pelvis, against the upright line.",
            "Needs no photo: the product is absent or a silhouette.",
            compose(
                CAUSE_HEAD,
                "A seated body seen from the side in both panels. Ground: one continuous deep muted "
                "slate-blue field, one step lighter on the right. The pelvis, the tailbone and the "
                "whole spine are drawn in warm ivory over a translucent outline of the body.\n\n"
                "Left panel, the wrong state: the body slouched on a plain seat, the pelvis rolled "
                "back and the spine curved into a C. Right panel, the correct state: the same body "
                "on a plain L-shaped support in silhouette, the pelvis upright and the spine "
                "stacked.\n\n"
                "Marks: one curved line along the spine in each panel, red in the left and blue in "
                "the right; in the top corner of each panel a filled disc with its glyph cut out, "
                "red with a cross in the left and green with a check in the right.",
                ground=None, lit=False),
            product=False),
        opt("03-spec-macro", None, "type: 03-spec-macro",
            "Two hands, no face: one on the lumbar curve, one on the seat base, pressing both at once.",
            "Needs the product photo. Hands only, and no clinical dress (ADR-094).",
            compose(
                "Polished commercial studio macro photography, close range, razor sharp, high detail.",
                "Two hands in plain knit sleeves press the product at once, one on the curve of its "
                "upright section and one on its seat section, the surface resolved exactly as the "
                "photo shows it under raking light, holding its shape under both.",
                place="The magnified region is a true region of the product: its upright section and "
                      "its seat section together, same geometry, same material, same finish.",
                ground=SEAMLESS)),
    ],
})

SLOTS.append({
    "slot_id": "safety.image", "role": "proof", "kind": "section", "ratio": "1:1",
    "asset": "590-23-safety-explode.png",
    "placement": "Beside 'Tested for Daily Support': slow-rebound core, anti-slip bottom, washable cover.",
    "recommended": "A",
    "rationale":
        "The block's evidence is three named parts, not a test the page describes, and ADR-094 bars "
        "an invented test. FIT: `03-spec-explode` lays the three parts out in assembly order, each "
        "one the page names. B is the reviewer's 'holds its shape after months' as a timelapse; C is "
        "the grip base alone.",
    "gif": no_gif("An exploded view is inspected part by part."),
    "options": [
        opt("03-spec-explode", None, "baseline",
            "The washable cover lifted clear, the memory foam core, the grip base beneath.",
            "Needs the product photo. Only the three parts the page names are drawn.",
            compose(
                "3D technical render, premium technical product visualization, sharp and high detail. "
                "Not photography.",
                "The core is the brightest, sharpest and most central part of the frame. Across the "
                "ground, at very low contrast, a sparse square lattice of fine straight lines.",
                place="Render its parts separated along one vertical axis, in assembly order from the "
                      "top down: the removable, washable cover lifted clear; the slow-rebound memory "
                      "foam core; the non-slip grip base beneath it. Each part is complete, in the "
                      "reference's own material and colour, and nothing is drawn that the product "
                      "does not contain.",
                ground=SEAMLESS, lit=False)),
        opt("04-proof-lockedframe", "--timelapse", "type: 04-proof-lockedframe",
            "The same product on a commuter's car seat, new and after months of commutes, unchanged.",
            "Needs the product photo. Handheld, because the halves are separated by time. Close in "
            "message to `expect.items.2`, so picking both repeats the type and the claim.",
            compose(
                "Honest documentary product photography, unstyled, natural, sharp. Two equal panels "
                "packed across the frame with thin white gutters, no outer border.",
                "One framing for both panels, stated once: a phone at standing height at the open "
                "driver's door of a hatchback, the seat filling the lower two thirds, the steering "
                "wheel at the upper right. It reads as one shot taken twice.\n\n"
                "The only thing that changes is the time: in the left panel the product is new on "
                "the seat; in the right panel, months of commutes later, it stands the same height "
                "and shape, a travel mug now in the cup holder.\n\n"
                "Grade: one neutral grade across both panels, no panel warmer or brighter.",
                place="Render it whole on the seat in both panels, the same unit, identical in both, "
                      "" + HOST + ".",
                ground=None, lit=False),
            axes={"camera_lock": "handheld"}),
        opt("03-spec-macro", None, "type: 03-spec-macro",
            "The grip base pressed square on a leather seat, the stitching sharp beside it.",
            "Needs the product photo.",
            compose(
                "Polished commercial studio macro photography, close range, razor sharp, high detail.",
                "Where the base meets a leather car seat, the surface is resolved exactly as the "
                "photo shows it under raking light, pressed flat and square to the leather, the "
                "seat's stitching sharp beside it.",
                place="The magnified region is a true region of the product: the edge of its base "
                      "where it rests on the seat, same geometry, same material, same finish.",
                ground=ROOM)),
    ],
})

# ================================================================== contoured zones
MODES_NOTE = ("The three zones are equivalent items of one block, so one type serves all three and "
              "each image differs on the named dimension, the zone (cross-slot rule 10). The block "
              "names parts of the product, so the section's mechanism role reads as the part itself.")
MODES = [
    ("modes.items.0.image", "590-24-mode0-macro.png", "Lumbar Curve — 'Fills the lower spine void'",
     "its upright section's curve where it meets the small of a seated back",
     "The small of a seated North American woman's back, in a knit sweater, rests into the curve, the curve filling "
     "the hollow of the lower spine with no gap, the surface resolved exactly as the photo shows it "
     "under raking light.",
     "the lumbar vertebrae", "beside the lumbar vertebrae", "the small of her back"),
    ("modes.items.1.image", "590-25-mode1-macro.png", "Pelvic Cradle — 'Relieves tailbone pressure evenly'",
     "its seat section around the base of a seated spine",
     "A seated North American woman in dark trousers, seen from behind and to the side, sits into the seat "
     "section, the hips cradled evenly and the base of the spine over the product's rear part, the "
     "surface resolved exactly as the photo shows it under raking light.",
     "the pelvis and the tailbone", "under the sitting bones", "her hips and the base of her spine"),
    ("modes.items.2.image", "590-26-mode2-macro.png", "Thigh Support — the front of the seat",
     "the front of its seat section under a seated person's thighs",
     "A seated North American woman's thighs, in grey trousers, rest along the front of the seat section, supported "
     "evenly to just behind the knees, the surface resolved exactly as the photo shows it under "
     "raking light.",
     "the thigh bones", "under the thigh bones", "the backs of her thighs"),
]
for sid, asset, placement, region, macro_body, bones, band, zone in MODES:
    SLOTS.append({
        "slot_id": sid, "role": "mechanism", "kind": "section", "ratio": "4:3", "asset": asset,
        "placement": f"Contoured Zones, {placement}.", "recommended": "A",
        "rationale": MODES_NOTE + " FIT: `03-spec-macro` shows a true region of the product with the "
                     "body it serves; B draws the same zone through a mannequin; C is the zone as a "
                     "relaxed sitter.",
        "gif": no_gif("A zone is shown, not a change."),
        "options": [
            opt("03-spec-macro", None, "baseline",
                f"The zone in close-up: {region}.",
                "Needs the product photo. No face in frame.",
                compose("Polished commercial studio macro photography, close range, razor sharp, high "
                        "detail.", macro_body + " No face is in the frame.",
                        place=f"The magnified region is a true region of the product: {region}, same "
                              "geometry, same material, same finish.",
                        ground=SEAMLESS)),
            opt("03-mechanism-ghostbody", None, "type: 03-mechanism-ghostbody",
                f"The zone drawn through a seated mannequin: {bones}.",
                "Needs the product photo.",
                ghost(f"the named place, showing {bones}", "the structure unsupported",
                  "the structure supported", f"a blue band {band}, right panel only")),
            opt("06-relief-hero", "--commercial", "type: 06-relief-hero",
                "The zone as a relaxed sitter at a desk, the posture showing it.",
                "Needs the product photo. The weakest reading: a whole person for one zone.",
                compose("Commercial lifestyle photograph. One frame, no panels, no insets.",
                        "A North American woman in her thirties sits back at her desk, relaxed, "
                        "looking at her screen rather than at the camera, seen from the side so that "
                        f"the product's support at {zone} is plain.",
                        place="Render it whole at about 28% of the frame height, on her office chair "
                              "under her and behind her lower back as one piece, seen from the side, "
                              + HOST + "."),
                axes={"register": "commercial", "inset_mode": "none"}),
        ],
    })

# ================================================================== testimonials: four pairs
TESTI_FLAG = {
    "flag": "origin-claim-lead",
    "note": "Each pair sits beside a named quote and 'Verified Buyer', which attributes the photos to "
            "that buyer (G14, ADR-088). Pairs are always generated on LP2 (ADR-096); the merchant "
            "chooses between this prompt and the buyer's real photographs. No name or badge enters the "
            "image."}
TESTI_NOTE = ("A buyer's before-and-after, so the buyer-photo register binds: a phone snapshot, found "
              "rather than styled, no face, and each pair in a different place and light. A pair is one "
              "argument in two files (cross-slot rule 11): both prompts carry one locked description "
              "word for word and differ in the state line. The template frames it at 3:4.")
TESTI = [
    ("testimonials.items.0", "590-27-testi0", "Trevor M., long highway routes",
     "The same scene in both photographs of this pair: a phone photo from the passenger seat of a "
     "pickup truck's cab, a North American man in his fifties in a work jacket at the wheel, seen from "
     "the side, framed from his shoulders to his knees, no face in frame, a coffee cup in the holder, "
     "flat afternoon daylight.",
     GRAY + "He sits on the bare seat, braced, one hand pressed into his lower back.",
     "He sits on the same seat on the product, settled, both hands easy on the wheel.",
     "It is the first week: he sits settled on the product.",
     "It is weeks later: he sits the same way, the product exactly where it was."),
    ("testimonials.items.1", "590-28-testi1", "Claire W., donut cushions slid out",
     "The same scene in both photographs of this pair: a phone photo looking down at the driver's "
     "seat of a small car through the open door, the seat base and back filling the frame, a handbag "
     "on the passenger seat, overcast daylight.",
     GRAY + "A flat ring-shaped foam cushion has slid forward and hangs off the front edge of the seat.",
     "The product sits in place on the same seat, flush against the back.",
     "It is the first day: the product sits flush against the back.",
     "It is weeks later: the product sits exactly where it was, flush against the back."),
    ("testimonials.items.2", "590-29-testi2", "Jason R., eight hours at the desk",
     "The same scene in both photographs of this pair: a phone photo from behind and to the side of a "
     "North American man in his thirties at a home-office desk in the evening, framed from his "
     "shoulders to his knees, no face in frame, a monitor and a desk lamp in shot, warm lamplight.",
     GRAY + "He sits forward on the bare chair, one hand pressed into his lower back.",
     "He leans back on the same chair on the product, both hands on the keyboard.",
     "It is the first evening: he leans back on the product.",
     "It is weeks later, the same hour: he leans back on the product the same way."),
    ("testimonials.items.3", "590-30-testi3", "Samantha L., seated higher behind the wheel",
     "The same scene in both photographs of this pair: a phone photo from the passenger seat of a "
     "hatchback, a North American woman in her thirties at the wheel seen from the side, framed from "
     "her shoulders to her feet, no face in frame, the door and the steering wheel in shot, morning "
     "daylight.",
     GRAY + "She sits low on the bare seat, her knees higher than her hips.",
     "She sits higher on the product, her hips above her knees.",
     "It is the first morning: she sits on the product, her hips above her knees.",
     "It is weeks later: she sits the same way on the product."),
]
for base, asset, who, locked, b_split, a_split, b_time, a_time in TESTI:
    SLOTS += pair_files(
        base, asset, f"Real Feedback, {who}",
        TESTI_NOTE + " A takes `01-pain-split`'s halves, the buyer's old way against the new; B reads "
                     "the quote as the product holding up over weeks.",
        locked,
        [("01-pain-split", "--mirror", "baseline",
          f"{who}: the old way and the new, in the buyer's own phone photos.",
          "The before half needs the product photo only where the product is in it; the after half "
          "needs it.",
          b_split, a_split, False, True, {}),
         ("04-proof-lockedframe", "--timelapse", "type: 04-proof-lockedframe",
          f"{who}: the product in the first week and weeks later, unchanged.",
          "Both halves need the product photo. No panel is favoured.",
          b_time, a_time, True, True, {"camera_lock": "handheld"})],
        "3:4", TESTI_FLAG, snap=True)

# ================================================================== faq
SLOTS.append({
    "slot_id": "faq.image", "role": "outcome", "kind": "section", "ratio": "16:9",
    "asset": "590-38-faq-relief-hero.png",
    "placement": "Beside the FAQ, whose first question is 'Will this cushion sit me too tall behind "
                 "the steering wheel?'.",
    "recommended": "A",
    "rationale":
        "A `faq` image routes by the question it sits beside (Section routing, `@copy`), and the "
        "first is the objection the page answers first: seat height behind the wheel. FIT: "
        "`06-relief-hero` shows the answer — seated a little higher, comfortable, head clear of the "
        "roof. B draws the geometry of that height; C answers the leather question instead.",
    "gif": no_gif("A held state."),
    "options": [
        opt("06-relief-hero", "--commercial", "baseline",
            "A driver seated a little higher on the product, a comfortable hand's width below the "
            "roof lining, hips above knees.",
            "Needs the product photo.",
            compose(
                "Commercial lifestyle photograph, a wide frame. One frame, no panels, no insets.",
                "A North American man in his forties sits at the wheel of a compact car, both hands "
                "easy on the wheel, the top of his head a comfortable hand's width below the roof "
                "lining, his hips just above his knees, looking ahead through the windscreen rather "
                "than at the camera. His back rests against the product's upright section along its "
                "whole length. The left of the frame is the quiet passenger side.",
                place="Render it whole at about 25% of the frame height, on the driver's seat under "
                      "him and behind his lower back as one piece, seen from a rear three-quarter "
                      "angle from the passenger side, " + HOST + "."),
            axes={"register": "commercial", "inset_mode": "none"}),
        opt("02-cause-anatomy", "--diagnostic", "type: 02-cause-anatomy",
            "Seat height drawn: hips below the knees on a low car seat, level on a raised one.",
            "Needs no photo: the product is absent or a silhouette.",
            compose(
                CAUSE_HEAD,
                "A driver's seated body seen from the side in both panels, the steering wheel and "
                "roof line drawn as plain outlines. Ground: one continuous deep muted slate-blue "
                "field, one step lighter on the right. The pelvis, the spine and the thigh bone are "
                "drawn in warm ivory over a translucent outline of the body.\n\n"
                "Left panel, the wrong state: a low seat, the hips below the knees and the pelvis "
                "rolled back. Right panel, the correct state: the same body raised on a plain "
                "L-shaped support in silhouette, the hips just above the knees, the head still clear "
                "of the roof line.\n\n"
                "Marks: one curved line along the lower spine in each panel, red in the left and "
                "blue in the right; in the top corner of each panel a filled disc with its glyph cut "
                "out, red with a cross in the left and green with a check in the right.",
                ground=None, lit=False),
            product=False),
        opt("03-spec-macro", None, "type: 03-spec-macro",
            "The grip base pressed square on a leather seat — the FAQ's slide question.",
            "Needs the product photo. Answers the third question rather than the first.",
            compose(
                "Polished commercial studio macro photography, a wide frame, close range, razor sharp.",
                "Where the base meets a leather car seat, the surface is resolved exactly as the "
                "photo shows it under raking light, pressed flat and square to the leather, the "
                "seat's stitching sharp beside it.",
                place="The magnified region is a true region of the product: the edge of its base "
                      "where it rests on the seat, same geometry, same material, same finish.",
                ground=ROOM)),
    ],
})

# ================================================================== not generated
OUT_OF_SCOPE = [
    ("media.gallery.0.image", "cta", "Gallery image 1, the standard product shot, out of library scope "
     "(`mapping/slot-rules.md` cross-rule 6). The page currently shows the owner's 'ONE-PIECE SUPPORT "
     "SYSTEM' tile there."),
    ("buy.gifts.0.image", "cta", "An 80 px thumbnail of the free gift in the buy box: another product's "
     "picture, supplied by the merchant. The Slot kinds table has no row for `*.gifts.*` and classes it "
     "as a section; this session does not generate it."),
    ("buy.addons.0.image", "cta", "A 64 px thumbnail of the add-on, 'Breathable Replacement Cover': a "
     "merchant product shot. Same table gap."),
    ("buy#2.gifts.0.image", "cta", "The second buy box's gift thumbnail. Same reason."),
    ("buy#2.addons.0.image", "cta", "The second buy box's add-on thumbnail. Same reason."),
    ("guarantee.image", "cta", "A 122 px guarantee seal beside 'Our 90-Day Money-Back Guarantee': chrome, "
     "the template's own asset. The table has no `guarantee.*` row and the field is unlocked, so the "
     "script classes it as a section."),
    ("bundle_box.image", "cta", "'What's in the Box': a closing image, gallery image 1 reused by default. "
     "The table's closing row names `bundle.*`, not `bundle_box.*`."),
    ("close.image", "cta", "The closing product card: gallery image 1 reused (Slot kinds, `closing`)."),
    ("expert.avatar", "author", "A portrait beside the expert block's name; out of scope, and rule 12 "
     "keeps a face out of that block."),
    ("faq.items.0.chart_image", "cta", "A chart, built in HTML (Slot kinds, `chart`)."),
    ("bundle_trust.payment_image", "cta", "Payment cards, chrome."),
    ("sticky.image", "cta", "Sticky bar thumbnail: gallery image 1 reused."),
] + [(f"press_marquee.logos.{i}", "cta", "A press logo, locked chrome.") for i in range(11)] + [
    (f"reviews.items.{i}.avatar", "author", "A reviewer's portrait beside their name; out of scope.")
    for i in range(7)] + [
    (f"reviews.items.{i}.product_image", "cta", "A review card's product thumbnail: gallery image 1 reused.")
    for i in range(7)] + [
    (f"notify.items.{i}.product_image", "cta", "A purchase-toast thumbnail: gallery image 1 reused.")
    for i in range(3)]

PAGE_NOTES = [
    "lpTypeId is `pdp_dr`, so this page routes LP2's folder — `registry/pdp-dr-index.yaml`, "
    "`registry/pdp-dr-types/`, `registry/pdp-dr-instruction.md` and `mapping/pdp-dr-rules.md` — "
    "and never `registry/types/` (SPEC 3.0, ADR-091). Routing is loose (ADR-102): each image routes "
    "by its section's name and copy, `mapping/slot-rules.md` cross-slot rules 1–4 do not run, and "
    "no slot lost a type because another slot holds it.",

    "THE SLOT KINDS TABLE MISSES FIVE FIELD SHAPES IN THIS EXPORT, and this session routed them by "
    "hand. `media.gallery.*` is the product card's gallery (the HTML's `gal-main-N`), which the table "
    "names only as `buy.gallery.*`; `*.gifts.*` and `*.addons.*` are merchant thumbnails; "
    "`guarantee.image` is a seal; `bundle_box.image` is a closing image. The script classes all of "
    "them as wordless sections. The table owes rows for them.",

    "ATTRIBUTES ARE THE REPO'S, NOT THE APP'S. The export's own `imagePrompts.content_json` declares "
    "`symptom_visibility: invisible` and `result_visibility: invisible`; this repo's last routing of "
    "the same product (advertorial v07, `afcc30a`) declares `visible` and `on-body`, reading the "
    "slump and the level hips as photographable. This session keeps v07's values, which keeps "
    "`01-pain-split` and `06-relief-scene` in the pool. `multi_step_usage: false` removes "
    "`03-use-sequence`.",

    "AWARENESS: solution-aware, from the brief's own field and from the page, which spends its "
    "problem block comparing cushion designs rather than re-establishing the pain.",

    "THE STYLE LOCK is declared once in `style_lock` and written into every prompt in the same words: "
    "the product block, the lighting and grade lines on photographic frames, the two grounds, the "
    "no-frame line, the empty bottom-right corner, and either the wordless line or the typography "
    "line. Rendered types keep their own register's field, which the lock admits.",

    "THE GALLERY'S WORDS (rule 9, a warning since ADR-102): five generated tiles, four with a title "
    "of 4–5 words and no copy or chip, one wordless. Every other image on the page is wordless "
    "(ADR-096). No figure enters any frame; the page's figures stay in HTML.",

    "THE GALLERY'S ORDER follows the owner's gallery instruction: the problem split at image 2, the "
    "mechanism at image 3, the one macro at image 4, the comparison at image 5, the outcome hero "
    "closing at image 6. The mechanism budget holds at two (image 3 and image 5).",

    "BUYER TILES AND PAIRS SHIP FLAGGED (ADR-088, ADR-089, ADR-096): the three trusted cards, the "
    "three 'Real Results' pairs and the four testimonial pairs each carry a `compliance` note naming "
    "the page words that attribute them. The merchant chooses between the prompt and a real photo.",

    "PAIRS HOLD TWO TYPES, NOT THREE, and say so in `pool_basis`: rule 11 fixes a pair to "
    "`01-pain-split`'s halves or `04-proof-lockedframe --timelapse`. Both files of a pair must take "
    "the same option letter, and both carry one locked description word for word.",

    "PAIRS STAY IN COLOUR. `01-pain-split` desaturates its BEFORE panel inside one frame; a pair is "
    "two files whose prompts differ in the state line alone (the instruction, 'A pair shares one "
    "description'), and the lock's grade binds both, so neither half is grayscale.",

    "THE HERO WAS RE-WRITTEN UNDER ADR-103 (`e6c84c3`), which landed after this session's first "
    "commit: its three options now carry the five fixed hero sentences word for word (the fifth only "
    "where a person is in frame), and option B brings the product to the open door so the fourth "
    "can hold. No other field is a hero.",

    "RATIOS: the template frames the expect pairs and the expert image at 4:5, which ADR-016 does "
    "not allow; they are asked for at 3:4 and the template crops. The hero is a banner and renders "
    "at 16:9 (ADR-096).",

    "THE REFERENCE PHOTOS. The export lists six sha256 hashes, and they are the six images the "
    "gallery shows today — the owner's own generated tiles with titles, callouts and marks baked in. "
    "No clean product photo is in the export. `attachments` names the 'ONE-PIECE SUPPORT SYSTEM' "
    "tile, the cleanest full view of the product; crop its title off before attaching it, or the "
    "renderer may copy the words.",

    "EXPECTED RULE-13 WARNINGS (same type AND message): none among the recommended options. Options "
    "that would raise one say so in their notes — the gallery's second macro, the two durability "
    "timelapses at `safety.image` and `expect.items.2`.",

    "TYPE VERSIONS ARE READ FROM THE COMMITTED LP2 FILES. The export's own `imagePrompts` block — the "
    "app's routing of this page — was read and is not reused.",

    "EVERY PROMPT IS PASTE-AND-RUN: one prompt, one generation call, one reference photo where the "
    "product is in frame (ADR-021, ADR-076).",
]

COVERAGE = {
    "covered": [
        "rung 1, pain — 01-pain-split at gallery image 2 and problem.items.0",
        "rung 2, cause — 02-cause-anatomy --diagnostic at problem.items.1",
        "rung 3, mechanism — 03-mechanism-ghostbody at gallery image 3 and expert.photo; "
        "03-spec-macro at gallery image 4 and the three zones",
        "rung 4, proof — 03-spec-split at gallery image 5 and problem.items.2; "
        "04-proof-lockedframe --timelapse in the expect pairs; 03-spec-explode at safety.image",
        "rung 5, social — 05-social-snapshot on the trusted cards; the testimonial pairs",
        "rung 6, relief — 06-relief-hero at the hero, gallery image 6, how.image, uses.image's "
        "option C and faq.image; 06-relief-scene at why.photo",
    ],
    "absent": ["No rung is absent."],
    "recommended_additions": ["None. The page's own blocks carry every rung."],
}

MOTION = {
    "floor": 2, "ceiling": 5, "delivered": 2, "margin": 0,
    "groups_covered": ["working", "result"],
    "shortfall_reason": None,
    "briefs": [
        {"slot_id": "problem.items.1.image", "type_id": "cause", "group": "working"},
        {"slot_id": "media.gallery.4.image", "type_id": "proof", "group": "result"},
    ],
    "note": "The template carries no GIF field, so each loop replaces a still's asset whole. Two loops "
            "meet the floor, one from each group; every other slot is a held state or a panel "
            "comparison, and says so.",
}


# ================================================================== content.json
def build_content():
    export = json.load(open(EXPORT, encoding="utf-8"))
    v07 = json.load(open(os.path.join(ROOT, "query", "sessions",
                                      "advertorial-seat-cushion-l-shaped-v07", "content.json"),
                         encoding="utf-8"))
    product = dict(v07["product"])
    product["reference_photos"] = [r["hash"] for r in export["page"]["imagePrompts"]["reference_photos"]]
    sections, seen = [], {}
    for s in SLOTS:
        sid = s["slot_id"]
        sec_id = "trusted" if sid.startswith("trusted.") else sid.rsplit(".", 1)[0]
        role = s["role"]
        summary = s["placement"]
        if sec_id not in seen:
            seen[sec_id] = {"id": sec_id, "role": role, "copy_summary": summary, "image_slots": []}
            sections.append(seen[sec_id])
        seen[sec_id]["image_slots"].append({"slot_id": sid, "ratio": s["ratio"]})
    return {"product": product,
            "page": {"channel": "landing-page", "lpTypeId": "pdp_dr", "sections": sections}}


# ================================================================== emit
def emit():
    versions = {o["type"]: type_version(o["type"]) for s in SLOTS for o in s["options"]}
    ref = build_content()["product"]["reference_photos"]
    attach = [ref[0]] if ref else []
    md, js = [], []
    n_prompts = sum(len(s["options"]) for s in SLOTS)
    md.append(f"# Image prompts — page {PAGE_ID}, LP2, ergonomic memory foam seat cushion (v08)\n")
    md.append("GENERATED from this directory's `build.py`. Never hand-edit this file — edit the script "
              "and re-run. Routing notes, the not-generated fields and the motion block are in "
              "`prompts.json`.\n")
    md.append(f"- page `{PAGE_ID}` · LP2 (`pdp_dr`) · solution-aware · {len(SLOTS)} routed image fields · "
              f"{n_prompts} prompts · {len(OUT_OF_SCOPE)} fields not generated")
    md.append("- **Attach the product photo** to every prompt with the product in frame: the "
              "'ONE-PIECE SUPPORT SYSTEM' gallery image, its title cropped off.")
    md.append("- **The style lock for this session:**")
    for k, v in STYLE_LOCK.items():
        md.append(f"  - `{k}` — {v}")
    md.append("")
    for s in SLOTS:
        md.append("---\n")
        md.append(f"## `{s['slot_id']}` — {s['kind']} · {s['role']} · ratio `{s['ratio']}`\n")
        md.append(f"- asset `{s['asset']}` · {s['placement']}")
        md.append(f"- recommended: **option {s['recommended']}**")
        if s.get("pair_with"):
            md.append(f"- pair: `{s['pair_with']}` takes the same option letter")
        if s.get("compliance"):
            md.append(f"- **compliance flag `{s['compliance']['flag']}`** — {s['compliance']['note']}")
        if s.get("pool_basis"):
            md.append(f"- pool: {s['pool_basis']}")
        md.append(f"- {s['rationale']}\n")
        if s["gif"].get("eligible"):
            md.append(f"- **motion brief · gif type `{s['gif']['type_id']}`** — {s['gif']['brief']}\n")
        for letter, o in zip("ABC", s["options"]):
            v = f" `{o['variant']}`" if o.get("variant") else ""
            md.append(f"### `{s['slot_id']}` · option {letter} — `{o['type']}`{v}\n")
            md.append(f"- varies on: {o['varies_on']} · type version `{versions[o['type']]}` · "
                      f"{len(o['prompt'])} characters")
            md.append(f"- {o['gloss']}")
            md.append(f"- **note:** {o['note']}\n")
            md.append("```\n" + o["prompt"].strip() + "\n```\n")
        js.append({
            "slot_id": s["slot_id"], "role": s["role"], "kind": s["kind"], "ratio": s["ratio"],
            "asset": s["asset"], "placement": s["placement"],
            "recommended_option": s["recommended"], "recommendation_basis": s["rationale"],
            "compliance": s.get("compliance"), "pool_basis": s.get("pool_basis"),
            "pair_with": s.get("pair_with"), "gif": s["gif"],
            "options": [{
                "option": letter, "type": o["type"], "type_version": versions[o["type"]],
                "variant": o.get("variant"), "axes": o.get("axes") or {}, "pipeline": "single-pass",
                "varies_on": o["varies_on"], "summary": o["gloss"],
                "composition_notes": o["note"], "prompt": o["prompt"].strip(),
                "attachments": attach if o["product"] else [],
            } for letter, o in zip("ABC", s["options"])],
        })
    for slot_id, role, reason in OUT_OF_SCOPE:
        js.append({"slot_id": slot_id, "role": role, "out_of_scope_reason": reason})
    doc = {
        "page_id": PAGE_ID, "registry_version": "2.0.0", "channel": "landing-page",
        "lp_type_id": "pdp_dr", "awareness_stage": "solution-aware",
        "source_export": os.path.basename(EXPORT), "template": "TPL-PDP05 LP2-Aure-TopLaser 1.0.0",
        "style_lock": STYLE_LOCK, "slots": js, "motion": MOTION, "coverage": COVERAGE,
        "recommended": [f"{s['slot_id']} -> option {s['recommended']}" for s in SLOTS],
        "page_composition_notes": PAGE_NOTES,
    }
    json.dump(build_content(), open(os.path.join(HERE, "content.json"), "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    open(os.path.join(HERE, "prompts.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    json.dump(doc, open(os.path.join(HERE, "prompts.json"), "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    lengths = sorted(((len(o["prompt"]), s["slot_id"], L) for s in SLOTS
                      for L, o in zip("ABC", s["options"])), reverse=True)
    print(f"wrote content.json, prompts.md, prompts.json — {len(SLOTS)} routed fields, {n_prompts} "
          f"prompts, {len(OUT_OF_SCOPE)} not generated")
    print("longest:", lengths[:6])
    over = [x for x in lengths if x[0] > GATE]
    if over:
        raise SystemExit(f"{len(over)} prompt(s) over the {GATE} gate: {over}")


if __name__ == "__main__":
    emit()

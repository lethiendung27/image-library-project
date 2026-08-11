#!/usr/bin/env python3
"""QUERY v2 — 13-inch wall cooler listicle. Registry 2.0.0, 14 types, derived Stage 1."""
import json, re

REF = "sha256:d3ce1b733b099bf6bc63f5908d0663f7b7192e333e9d708ca45b115bd0820877"
ATT = "Attach `cooler.avif` (sha256:d3ce1b73…) at render time."
PAGE = "cooler-listicle"

def S(sid, role, asset, place, opts, setn=1):
    return {"slot_id": sid, "section_role": role, "asset": asset, "placement": place,
            "options": opts, "_setn": setn}

def O(opt, varies, tid, ver, ratio, prompt, avoid, why, notes,
      variant=None, axes=None, pipeline="single-pass", steps=None, att=True, cand=None):
    o = {"opt": opt, "varies_on": varies, "type": tid, "type_version": ver,
         "variant": variant, "axes": axes or {}, "ratio": ratio, "pipeline": pipeline,
         "prompt": prompt.strip(), "avoid": avoid, "rationale": why,
         "composition_notes": notes}
    if steps: o["steps"] = steps
    if att: o["attachments"] = [REF]
    if cand: o["asset_candidate"] = cand
    return o

slots = []

# ══════════════════════════════════════════ 01 hero
HERO_AVOID = ("Avoid: text, watermarks, logos, red glow, pain hotspots, graphic overlays, "
              "badges, split panels, any visible product, posed stock-photo look, studio lighting.")
slots.append(S("hero-header", "hero", f"{PAGE}-01-hero.jpg",
 "Full-bleed header directly above `hero.title`, before the byline block.", [
 O("A","baseline","01-pain-scene","1.2","16:9","""
Cinematic film still, frame full. Single frame, NO graphic overlays.

SUBJECT: man late 30s, creased grey t-shirt and loose half-apron, mid-action lifting a pot lid at the stove of a small apartment kitchen on a July evening, leaning back from the rising steam, chin tucked from the heat, one forearm raised to wipe his forehead. Unaware of camera, gaze down at the pan. Brow knotted, eyes narrowed, cheeks flushed and damp, lips parted. Weight unbalanced, not posed.

SYMPTOM EVIDENCE, physical fact: dark sweat patches at collar and underarms, sweat shining on temple and neck, a crumpled towel already damp over his shoulder, a cheap desk fan wedged on the counter with a ribbon fluttering weakly in its warm draft — already tried, changing nothing. Steam from two pots keeps the heat source in frame.

MOMENT: the ordinary act of cooking on a hot evening, not a demonstration.

ENVIRONMENT to the edges: small rented kitchen in a heatwave, window shut with low sun glaring through, cutting board mid-use, open spice jar, oven mitts, a calendar curling at the corner. Lived-in clutter, nothing tidied.

LIGHT: low-key. Hard low evening sun from behind right, hot and unflattering. Weak cool bounce from the hallway. Rim along damp temple and forearm. Deep shadow across half the frame.

GRADE: desaturated amber-grey, crushed blacks, fine grain, shallow depth of field, 35mm. NO red anywhere.

FORBIDDEN: no product, no overlays, arrows, badges, glows, insets or split panels.
Editorial photojournalism, natural, unstaged. No text, no logo, no watermark.
""", HERO_AVOID+" Also: bright airy daylight, looking at camera.",
 "Advertorial hero cell. The page's own intro is a pain opening ('Struggling in a hot kitchen? Portable units roar at 53dB(A)'), and --candid fits heat discomfort nobody chooses to be seen in. G1-exempt: no product, no reference needed.",
 "Page-wide: 01-pain-split stays banned (never_with). This type also serves the five alternative entries in a different execution — see slot 03.", variant="candid", axes={"gaze":"candid"}, att=False,
 cand=f"{PAGE}-01-hero--A.jpg"),
 O("B","axis: gaze=confront","01-pain-scene","1.2","16:9","""
Cinematic film still, frame full. Single frame, NO graphic overlays.

SUBJECT: man late 30s in a wrinkled short-sleeve shirt at a desk in a small home office mid-afternoon, turned to camera, looking into the lens, holding the viewer's eye. He has pushed his laptop a hand's width away; one hand still rests on it, the other tugs his damp collar off his neck. Brow drawn, mouth pressed flat, faint sheen at the hairline — an afternoon that has stalled again. Frustration, not drama.

SYMPTOM EVIDENCE, physical fact: damp sheen on forehead and neck, collar and chest darkened with sweat, a desk fan aimed straight at him with a limp ribbon barely lifting — running and useless — a glass of water sweating a ring onto his notepad.

MOMENT: the ordinary act of pausing mid-task in a stuffy room.

ENVIRONMENT to the edges: cramped home office in a rented flat, blinds half-closed, window shut behind him, papers stacked beside the laptop, phone face-down, cable tangle at the desk edge. Real clutter, nothing tidied.

LIGHT: even ambient daylight through the blinds, bright, minimal shadow, flat and unflattering. No golden hour, no rim light.

GRADE: desaturated grey-green, fine grain, moderate depth of field, 35mm. NO red anywhere.

FORBIDDEN: no product, no overlays, arrows, badges, glows, insets or split panels.
Editorial photojournalism, natural, unstaged. No text, no logo, no watermark.
""", HERO_AVOID+" Also: golden hour, warm flattering light, theatrical anger.",
 "Same type, confront gaze — a listicle often wants the reader met eye-to-eye before the ranked list starts. The stalled home office is the page's second named pain.",
 "Restraint rule: the flatter the face, the truer it reads.", variant="confront", axes={"gaze":"confront"}, att=False,
 cand=f"{PAGE}-01-hero--B.jpg"),
 O("C","execution: sleepless hot bedroom at night, female cast","01-pain-scene","1.2","16:9","""
Cinematic film still, frame full. Single frame, NO graphic overlays.

SUBJECT: woman early 30s in a loose sleep shirt sitting up on the edge of the bed in the middle of a hot night, feet on the floor, hair stuck to her neck, one hand lifting the hair off her nape, the other holding her collar away from her skin. Unaware of camera, gaze down and unfocused, lids half closed, damp strands at the temple, jaw slack.

SYMPTOM EVIDENCE, physical fact: duvet kicked into a heap at the foot of the bed, sheet creased and thrown back, a pedestal fan turned to face the bed — running all night, moving only warm air — a glass of water beaded with condensation, a faint damp outline on the sheet where she has been lying.

MOMENT: the ordinary act of giving up on sleep in a hot bedroom.

ENVIRONMENT to the edges: small city bedroom in high summer, deep night, window cracked onto a still street, curtains hanging dead still, phone charging on the nightstand, clothes over a chair. Real clutter, nothing tidied.

LIGHT: low-key. Sodium streetlight through the window gap from the left. Faint cold spill from a hallway door ajar. Rim along her shoulder. Deep shadow across most of the frame.

GRADE: desaturated blue-grey, crushed blacks, fine grain, shallow depth of field, 35mm. NO red anywhere.

FORBIDDEN: no product, no overlays, arrows, badges, glows, insets or split panels.
Editorial photojournalism, natural, unstaged. No text, no logo, no watermark.
""", HERO_AVOID+" Also: bright airy lighting, looking at camera.",
 "Same type and axes as A, night execution: the light-sleeper persona the brief names, echoed by the page's own 'sleeping mode' review.",
 "If this cast wins, any later 06-relief-scene pair must be re-cast to this woman (requires_pair).", variant="candid", axes={"gaze":"candid"}, att=False,
 cand=f"{PAGE}-01-hero--C.jpg")]))

# ══════════════════════════════════════════ 02 editor's pick
RH_AVOID = ("Avoid: text, watermarks, logos, pain cues, red glow, invented steam beyond the "
            "outlet, product differing between layers, blank wall or floor areas, badges, arrows.")
slots.append(S("reason-0-editors-pick", "outcome", f"{PAGE}-02-editors-pick.jpg",
 "Inside the `reason.0` card (The Portable Wall Cooler — Editor's Pick), above `reason.0.body`.", [
 O("A","baseline","06-relief-hero","1.7","5:3","""
E-commerce lifestyle banner, frame full.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. Wall-mounted in every layer — the freestanding base never appears.

SCENE right 58%: woman early 30s in a light knit top, medium shot at chest height, leaning back in her desk chair with her eyes closed for a second, shoulders loose, hands resting in her lap off the keyboard, gaze away from the product. The reference cooler is mounted punch-free on the wall above and beside her desk, unobstructed.

OUTPUT primary: a fine dense stream of cool mist drifting down and outward from the outlet across the desk zone, backlit by hard window light behind it so the mist glows against the darker hallway beyond, filling a large part of the frame and readable at thumbnail size. Lens flare and blown highlights welcome.

SETTING to the edges: a small working home office — laptop, glass of iced water, a linen curtain lifting, a shelf of books, a mug, a plant on the sill, a cable tray under the desk. Blurred, never blank; no bare wall or floor bigger than the product.

Bright, warm, sharp, 4K. No text, no logo, no watermark.
""", RH_AVOID,
 "The Editor's Pick entry presents the product as the resolved state — the outcome role, not a comparison. G8 binds: mist is the primary subject on the backlight branch. POSE takes the passive branch (it works while she works). Advertorial legality gained in v1.7 (see its changelog).",
 ATT+" Zone B skipped: the mounted unit is legible at scene scale, and a product view repeating the same angle buys nothing.",
 axes={"register":"commercial","inset_mode":"none"}, cand=f"{PAGE}-02-editors-pick--A.jpg"),
 O("B","axis: inset_mode=detail","06-relief-hero","1.7","5:3","""
E-commerce lifestyle banner, frame full.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. Wall-mounted in every layer.

SCENE right 58%: woman early 30s in a light knit top, medium shot at chest height, leaning back in her desk chair, eyes closed, shoulders loose, hands in her lap, gaze away from the product. The reference cooler is mounted punch-free on the wall above and beside her desk, unobstructed.

OUTPUT primary: a fine dense stream of cool mist drifting down and outward from the outlet, backlit by hard window light so it glows against the darker hallway beyond, filling a large part of the frame.

SETTING to the edges: a small working home office — laptop, glass of iced water, linen curtain lifting, shelf of books, mug, plant on the sill, cable tray. Blurred, never blank; no bare wall or floor bigger than the product.

DETAIL INSET bottom-right over the scene: PERFECT CIRCLE, 40% of frame width, 3% in from the bottom and right edges, 6px white ring, drop shadow, clear of the woman and the mounted unit. Inside: a magnified view of the unit's touch control panel with its three wind-mode indicators, sharp and legible. Real captured interface composited in, never drawn. Linked by proximity — no arrow, no glow border. Circle 8% clear of every edge; too big, render it smaller — never let it run off.

Bright, warm, sharp, 4K. No text, no logo, no watermark.
""", "Avoid: a rectangular or square inset, gibberish digits, arrows, glow borders, text, watermarks, logos, pain cues, blank wall or floor areas.",
 "Varies on the inset_mode axis: the #1 entry sells 3 wind modes and a remote, and --detail is the slot for a control surface too small to read at scene scale.",
 ATT+" The panel is diegetic UI — composite a real capture, never let the model draw the indicators (G6 production law).",
 axes={"register":"commercial","inset_mode":"detail"}, cand=f"{PAGE}-02-editors-pick--B.jpg"),
 O("C","execution: night bedroom, Soft Wind","06-relief-hero","1.7","5:3","""
E-commerce lifestyle banner, night scene, frame full.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. Wall-mounted in every layer.

SCENE right 58%: woman late 20s asleep on her side in a small quiet bedroom, face soft and untroubled, duvet drawn to her shoulder and lying flat and undisturbed — deep still sleep, nothing about her engaging the product. The reference cooler is mounted punch-free on the wall above the bedside, unobstructed.

OUTPUT primary: a fine stream of cool mist drifting slowly down from the outlet, backlit by the soft spill of a streetlamp through the curtain gap so it reads as a faint glowing veil against the dark wall, filling a large part of the frame and readable at thumbnail size.

SETTING to the edges: glass of water and a face-down phone on the nightstand, a paperback, a chair with clothes over the back, a rug edge, curtains half drawn. Deep calm blue-grey grade with the mist as the brightest element. Never blank; no bare wall bigger than the product.

Calm, quiet, sharp, 4K. No text, no logo, no watermark.
""", RH_AVOID+" Also: harsh lighting.",
 "Same type and axes as A, night execution: the page's own review copy leads on the sleep mode ('so quiet I had to check if it was still on'), and darkness makes backlit mist read at its best under G8.",
 ATT+" Dark-scene grade is a deliberate deviation from the type's bright-airy default, backed by a ledger exemplar (night relief-hero, batch 2026-08-10-C).",
 axes={"register":"commercial","inset_mode":"none"}, cand=f"{PAGE}-02-editors-pick--C.jpg")]))

# ══════════════════════════════════════════ 03 the five alternatives
ALT_AVOID = ("Avoid: text, watermarks, logos, overlays, arrows, badges, red or signal colours, "
             "faces, a damaged or filthy unit, a comically ugly unit, studio lighting, saturated colours.")
ALT_NOTE = ("REPEATING SECTION: this slot yields FIVE assets, one per listicle entry, all "
            "01-pain-scene. Cross-slot rule 2 permits the repeat because the instances differ "
            "on a named dimension — the indicted object. All five must share ONE register and "
            "grade or the block reads as five sources instead of one editorial series.")

def alt(n, stem, entry, subject, evidence, env, light):
    return O(chr(64+n) if n<=3 else "A", f"execution: {entry}", "01-pain-scene","1.2","5:3", f"""
Documentary photograph, frame full. Single frame, NO graphic overlays, no signal colours.

SUBJECT, the indicted object: {subject}

SYMPTOM EVIDENCE, physical fact: {evidence}

MOMENT: an ordinary moment in the room, nothing arranged for the camera.

ENVIRONMENT to the edges: {env} Real lived-in clutter, nothing tidied.

LIGHT: {light} No fill, no styling.

GRADE: desaturated neutral, fine grain, deep blacks, believable 35mm optics.

FORBIDDEN: no product of ours, no overlays, arrows, badges, glows, insets or split panels.
Editorial documentary photography, natural, unstaged. No text, no logo, no watermark.
""", ALT_AVOID,
 f"Listicle entry: {entry}. 01-pain-scene in its object-only execution — the ledger records this twice already (obs sha256:30c9568…, sha256:4e8f238…, both filed as pain-scene with 'no person as subject, only the indicted OBJECT'). Reached by runbook rung 2 (adjacent step) plus rung 3 (repeating section) after one-type-once spent 04-proof-lockedframe.",
 ALT_NOTE+" FAIRNESS: the alternative must look like a real product someone genuinely bought. The page's copy dramatises them ('sounded like a jet engine'); the image must not.",
 variant="candid", axes={"gaze":"candid"}, att=False, cand=f"{PAGE}-{stem}.jpg")

ALTS = [
 (3,"03-alt-window-ac","reason.1 Traditional Window AC Units",
  "a boxy white window air conditioner wedged into the lower half of a sash window in a rented flat, the sash resting on its top, a foam infill strip stuffed into the gap at one side. Ordinary, intact, plausible.",
  "four bracket screws biting into the painted window frame, the paint cracked and flaked around each one; the window's view mostly blocked; a power lead running down the wall to a socket.",
  "a small living room mid-summer, a curtain pushed permanently aside and hooked back, a bookshelf, a mug on the sill.",
  "natural window light only, low and directional, raking so the cracked paint around each screw throws a shadow."),
 (4,"04-alt-portable-ac","reason.2 Hose-Vented Portable AC Units",
  "a generic white floor-standing portable air conditioner on the floor of a small home office, its wide corrugated exhaust hose rising in an awkward arc to a window propped open on a plastic vent panel, gaffer tape sealing one corner. Ordinary, intact, plausible.",
  "the unit's footprint eating the walking space between desk and door; the desk chair pushed sideways to clear it; a bin nudged into the corner by the hose.",
  "a cramped home office, a laptop and papers, a cable tangle, a jacket over the chair back.",
  "natural window light only, flat and directional through the propped gap."),
 (5,"05-alt-floor-cooler","reason.3 Bulky Floor-Standing Coolers",
  "a tall grey floor-standing evaporative cooler standing in the middle of a narrow galley kitchen, its water tank visible at the base with the fill flap open. Ordinary, intact, plausible.",
  "its power lead crossing the floor at ankle height between unit and socket; the gap left beside it too narrow to pass without turning sideways; a jug left beside it from the last refill.",
  "a narrow galley, counters both sides, a chopping board mid-use, a kettle, a bin the unit half blocks, a tea towel on the oven rail.",
  "natural window light from the galley's end, low and directional, the power lead casting a thin shadow across the floor."),
 (6,"06-alt-desk-fan","reason.4 Standard Plastic Desk Fans",
  "a cheap white plastic desk fan running at close range on a home-office desk, its cage grille dusty between the bars. Ordinary, intact, plausible — a fan someone actually owns.",
  "a short ribbon tied to the guard lifting only weakly in the draft; the papers directly in its path barely disturbed; a glass of water with condensation pooling on a notepad.",
  "a small home office in high summer, window shut, blinds half down, a laptop, a stack of papers weighted with a book, a cardigan discarded over the chair.",
  "flat ambient daylight through the blinds, hot and unhelpful."),
 (7,"07-alt-ceiling-fan","reason.5 Built-in Ceiling Fans",
  "a white ceiling fan mounted high in a bedroom, seen from low in the room so it sits small and far away against the ceiling, its blades still. Ordinary, intact, plausible.",
  "the mounting plate ringed by a repainted patch where the old fitting was cut in, a capped junction wire just visible at the plate's edge; the distance between the fan at the ceiling and the bed below is the point of the frame.",
  "a bedroom in high summer, bed with the duvet kicked back, a window cracked onto a still street, a chair with clothes over it, a glass of water on the nightstand.",
  "warm bedside lamp and a sodium streetlight through the window gap, low and directional, the ceiling in shadow."),
]
alt_opts = [alt(*a) for a in ALTS]
# Each listicle entry is its OWN slot: five assets, not five alternatives to choose
# between. maxItems:3 on options is a cap on candidates, not on images.
ENTRY_PLACE = ("Inside the `reason.{n}` card, above `reason.{n}.body`. One of five images in "
               "the same repeating section — they must read as ONE editorial series.")
for i,(o,(num,stem,entry,*_)) in enumerate(zip(alt_opts, ALTS), start=1):
    o["opt"]="A"
    o["varies_on"]="baseline"
    slots.append(S(f"reason-{i}-{stem.split('-',2)[2]}", "comparison",
                   f"{PAGE}-{stem}.jpg",
                   ENTRY_PLACE.format(n=i),
                   [o]))

# ══════════════════════════════════════════ 08 mechanism
XR_AVOID = ("Avoid: text, numbers, spec labels, watermarks, logos, photographic background, "
            "people, hands, opaque shell, internals outside the product, invented components, "
            "exploded parts, bright white background, cartoon style.")
slots.append(S("compare-mechanism", "mechanism", f"{PAGE}-08-mechanism.jpg",
 "Directly above the `compare` table, beside `compare.intro`.", [
 O("A","baseline","03-mechanism-xray","1.0","16:9","""
3D technical see-through render. NOT photography. Dark engineering background.

REFERENCE: attached photo is the wall-mounted personal air cooler. The outer shell becomes translucent, but its silhouette, proportions and every visible external part — top shell, louvered front grille, touch controls — match the reference exactly. Do not redesign or add features.

CANVAS: deep navy engineering canvas, faint copper and cyan circuit traces at very low contrast, two corner blueprint micro-diagrams of a fan-wheel module. Motifs stay dim.

GHOST SHELL: the cooler in its wall-mounted horizontal orientation, shell translucent and glass-like, seen from a slight three-quarter front angle, filling about 70% of frame width.

INTERNALS, solid and detailed, each at its true location: the magnetic levitation motor ring at the drive end with its rotor visibly FLOATING in a narrow gap — no contact, no shaft friction; the long cross-flow wind wheel cylinder running the body's length; the dark porous ice carbon grille behind the front louvers; the built-in water tank low in the housing with its water level visible. Fine cyan wiring linking motor and control board.

VISIBLE MECHANISM: the cooling path shown ACTIVE — wind wheel mid-spin, a fine cool mist streaming out through the front louvers as a bright particle flow drifting down and outward, the brightest element in the frame.

HONESTY CONSTRAINT: render ONLY these component types — maglev motor, cross-flow wind wheel, ice carbon grille, water tank, control board. No invented modules, no exaggerated part counts.

PALETTE LOCK: deep navy and steel grey; cyan marks the working mechanism and the floating rotor gap; copper traces stay decorative and dim.

Premium technical product visualization, sharp, high detail, 4K. No text, no numbers, no spec labels, no logo, no watermark.
""", XR_AVOID,
 "The compare section's intro carries the mechanism claims — maglev motor, water cooling, 3 wind modes. body_contact=false drops ghostbody, so xray is the mechanism answer. The floating rotor makes the zero-contact claim visual instead of verbal.",
 ATT+" Step-3 budget: with use-sequence at howto, the page then carries its maximum of two step-3 answers.",
 cand=f"{PAGE}-08-mechanism--A.jpg"),
 O("C","execution: frontal, one continuous air-path ribbon","03-mechanism-xray","1.0","16:9","""
3D technical see-through render. NOT photography. Dark engineering background.

REFERENCE: attached photo is the wall-mounted personal air cooler. The outer shell becomes translucent, but its silhouette, proportions and every visible external part match the reference exactly. Do not redesign or add features.

CANVAS: deep navy engineering canvas, faint copper and cyan circuit traces at very low contrast, two corner blueprint micro-diagrams of an evaporative media stage. Motifs stay dim.

GHOST SHELL: the cooler straight-on in its wall-mounted orientation, shell translucent and glass-like, filling about 75% of frame width.

INTERNALS, solid and detailed, each at its true location: the top air intake; the spiral wind wheel and cross-flow wind wheel in line; the dark porous ice carbon grille just behind the louvers; the water tank low in the housing with its water level visible; the magnetic levitation motor ring at the drive end.

VISIBLE MECHANISM: the full air path shown ACTIVE as ONE smooth flow ribbon — warm air drawn in at the top intake, threading through the spinning wind wheel, passing the water-fed ice carbon grille where it cools, and leaving the front louvers as a fine bright mist stream, the brightest element in the frame. The ribbon enters warm-neutral and exits cool cyan.

HONESTY CONSTRAINT: render ONLY these component types — intake, wind wheels, ice carbon grille, water tank, maglev motor. No invented modules.

PALETTE LOCK: deep navy and steel grey; cyan marks the correct air path; copper traces stay decorative and dim.

Premium technical product visualization, sharp, high detail, 4K. No text, no numbers, no spec labels, no logo, no watermark.
""", XR_AVOID,
 "Same type, the story told as one continuous ribbon — warm in, through the wet grille, cool mist out. This enter-transform-exit grammar is what the type's own rendered-pass example proved on the shower filter.",
 ATT, cand=f"{PAGE}-08-mechanism--C.jpg")]))

# ══════════════════════════════════════════ 09 howto
US_AVOID = ("Avoid: text, numbers, watermarks, logos, arrows, step badges, deformed hands, "
            "extra fingers, different hands between panels, two actions in one panel, tools, "
            "instruction-manual diagram look, cold clinical lighting.")
slots.append(S("howto-steps", "how-to-use", f"{PAGE}-09-howto.jpg",
 "Inside the `howto` section (#7), beside the three numbered steps.", [
 O("A","baseline","03-use-sequence","1.1","4:5","""
Warm lifestyle photograph, three horizontal panels stacked vertically, thin white gutters, no outer border, no numbers, no arrows, no text.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color, identical in every panel.

CONTINUITY LOCK: the same pair of hands in every panel — same skin tone, nails, wrists, pushed-up sleeves. The same pale painted wall beside the same light-wood desk in every panel. Same warm neutral palette, same soft daylight from the left. Camera distance and framing may shift naturally.

SEQUENCE: one action per panel, never two, readable from the actions alone. The cooler or its plate sits near the centre of every panel.

PANEL 1, MOUNT OR SET: both hands pressing the slim adhesive backing plate flat against the painted wall at chest height, palms flat, the plate level and fully stuck. No drill, no screws, no tools anywhere in frame.

PANEL 2, ADD WATER: one hand pouring cold water from a small measuring cup into the open tank port of the mounted cooler, the water surface visible at the port, the other hand steadying the cup.

PANEL 3, SELECT MODE: a fingertip pressing the mode control on the mounted unit, the first fine stream of cool mist emerging from the outlet, backlit by the window so the mist is clearly visible; the other hand relaxed and open in the cool air below. Warmer light than the previous panels.

ENVIRONMENT: an ordinary small home office, soft daylight, a mug on the desk, a folded throw over the chair. Same location across all three panels.

Warm lifestyle product photography, natural, unstyled, sharp, 4K. No text, no numbers, no logo, no watermark, no arrows, no step markers.
""", US_AVOID,
 "The page gives exactly three numbered steps — Mount or Set, Add Water, Select Mode — and this type is three panels read by action logic with no numerals. A one-to-one fit; multi_step_usage=true keeps it. Advertorial legality gained in v1.1 (see its changelog).",
 ATT+" Close-range hands are the library's highest-risk zone; expect retries. If panel 3 crowds result and centred product, keep the mist and let the product sit off-centre.",
 axes={"camera_lock":"handheld"}, cand=f"{PAGE}-09-howto--A.jpg"),
 O("C","execution: kitchen wall, cook's hands","03-use-sequence","1.1","4:5","""
Warm lifestyle photograph, three horizontal panels stacked vertically, thin white gutters, no outer border, no numbers, no arrows, no text.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color, identical in every panel.

CONTINUITY LOCK: the same pair of hands in every panel — same skin tone, nails, wrists, rolled linen sleeves. The same white kitchen tile and the same counter edge in every panel. Same warm neutral palette, same soft daylight from the right. Camera distance may vary naturally.

SEQUENCE: one action per panel, never two, readable from the actions alone. The cooler sits near the centre of every panel, mounted punch-free on the kitchen wall above the counter in all three.

PANEL 1, MOUNT OR SET: both hands pressing the adhesive backing plate flat onto the tiled wall above the counter's end, palms flat, plate level. No drill, no screws, no tools in frame.

PANEL 2, ADD WATER: one hand pouring cold water from a jug into the open tank port of the mounted unit, water surface visible at the port, the other steadying the jug.

PANEL 3, SELECT MODE: a fingertip pressing the mode control, the first fine stream of cool mist drifting out over the prep zone, backlit against the tile; a chopping board with herbs resting calm below. Warmer light than the previous panels.

ENVIRONMENT: an ordinary home kitchen, soft daylight, a kettle on the counter, a linen towel on a hook. Same location across all three panels.

Warm lifestyle product photography, natural, unstyled, sharp, 4K. No text, no numbers, no logo, no watermark, no arrows, no step markers.
""", US_AVOID,
 "Same type and steps, staged in the kitchen the page opens on. Two legal options for this slot: the type declares one axis value, so the variation is execution.",
 ATT, axes={"camera_lock":"handheld"}, cand=f"{PAGE}-09-howto--C.jpg")]))

# ══════════════════════════════════════════ 10 social
SN_AVOID = ("Avoid: studio lighting, softbox reflections, seamless background, negative space, "
            "colour grading, professional composition, styled props, badges, borders, star "
            "ratings, reviewer names, avatars, text overlays, product-render look, magazine polish.")
SN_NOTE = ("SET DIVERSITY LAW: this slot yields a SET. Every additional snapshot must differ "
           "completely — room class, surface, light temperature, camera distance, content mode. "
           "Generate as independent prompts, never a batch with shared seeds or scene text.")
slots.append(S("social-viral", "social-proof", f"{PAGE}-10-social-1.jpg … -3.jpg",
 "A band ABOVE the `social.items` cards. NEVER inside a card — every card carries a name and a Verified Buyer badge.", [
 O("A","baseline","05-social-snapshot","1.0","5:3","""
Real customer's phone photo. One frame, no layout, no layers.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. It may be cropped or angled the way a casual one-handed phone photo crops.

CONTENT MODE, in-use: the cooler mounted on the tiled wall above a kitchen counter, running, a faint drift of cool air visible at the louvers, photographed from below at counter height the way someone shows a thing off quickly.

ANCHOR: an open bag of flour and a scale on the counter beneath it — the one incidental owner object.

SCENE: an ordinary kitchen photographed as found — crumbs on the counter, a splash mark on the tile, a tea towel bunched by the sink, another appliance blurred at the frame edge. Ambient overhead kitchen light only, never studio light.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus adequate, mild noise, exposure honest to the room. No negative space discipline, no rule of thirds, no styling.

Honest phone photography, unedited look, natural, slightly imperfect. No text overlays, no logo, no watermark, no badges, no borders.
""", SN_AVOID,
 "The section is six customer comments from six different rooms — exactly this type's use case. Baseline takes the in-use mode in the page's lead scene (Clara's kitchen: 'brutally hot… now I can actually bake').",
 ATT+" "+SN_NOTE, axes={"register":"ugc"}, cand=f"{PAGE}-10-social-1.jpg"),
 O("B","execution: at-rest mode, rented apartment wall","05-social-snapshot","1.0","4:3","""
Real customer's phone photo. One frame, no layout, no layers.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. It may be cropped or angled the way a casual phone photo crops.

CONTENT MODE, at-rest: the cooler simply mounted on a rented flat's painted wall where it now lives, switched off, the adhesive plate edge just visible behind it, photographed straight on from a step back.

ANCHOR: the remote control lying on the windowsill below it — the one incidental owner object.

SCENE: an ordinary rented living room photographed as found — a slightly scuffed skirting board, a radiator, a plug socket with a phone charger in it, the corner of a sofa at the frame edge. Flat daylight through a net curtain, never studio light.

CAMERA TRUTH: slightly off-centre, a little flat, focus adequate, exposure honest to the room, no styling.

Honest phone photography, unedited look, natural, slightly imperfect. No text overlays, no logo, no watermark, no badges, no borders.
""", SN_AVOID,
 "Second image of the set on a different content mode and room class — the renter comment ('no drilling, adhesive strip holding strong').",
 ATT+" Shares nothing with option A: different room, light, distance, mode. That is the law, not a preference.",
 axes={"register":"ugc"}, cand=f"{PAGE}-10-social-2.jpg"),
 O("C","execution: in-use, camper van at night","05-social-snapshot","1.0","1:1","""
Real customer's phone photo. One frame, no layout, no layers.

REFERENCE: attached photo is the wall-mounted personal air cooler. Keep shape, proportions, material, finish, color. It may be cropped or angled the way a casual phone photo crops.

CONTENT MODE, in-use: the cooler mounted on the plywood wall of a camper van interior, running, photographed at night from the bunk with the phone held low.

ANCHOR: a water bottle wedged beside it on the ledge — the one incidental owner object.

SCENE: a real camper interior photographed as found — a rumpled sleeping bag, a cabinet latch, a strip of warm LED light along the ceiling, a hoodie hanging on a hook. Dim mixed warm light only, underexposed and noisy, never studio light.

CAMERA TRUTH: framing tilted, a little too close, focus adequate, visible noise, exposure honest to the dark. No styling of any kind.

Honest phone photography, unedited look, natural, slightly imperfect. No text overlays, no logo, no watermark, no badges, no borders.
""", SN_AVOID+" Also: clean bright exposure.",
 "Third scene class for the set — the camper-van comment. Underexposure and noise are credentials in this register, not faults.",
 ATT+" Quality floor: authenticity tolerates softness, never illegibility — the product must stay identifiable at thumbnail size.",
 axes={"register":"ugc"}, cand=f"{PAGE}-10-social-3.jpg")]))


GIF = {
 "hero-header": dict(eligible=True, form="whole-frame", asset=f"{PAGE}-01-hero.mp4",
   reason="The scene's evidence is already motion held still — steam rising, a fan ribbon fluttering weakly, sweat catching light. A 2s loop shows the fan failing, which a still can only imply.",
   duration_s=2, loop="seamless", shot="locked frame, no camera move",
   action="steam rises, the fan ribbon flutters weakly", result="the fan visibly changes nothing",
   match="hero grade and grain exactly; no new light", delivery="mp4/webm, gif fallback, max 2 MB"),
 "reason-0-editors-pick": dict(eligible=True, form="whole-frame", asset=f"{PAGE}-02-editors-pick.mp4",
   reason="G8 output is the argument here, and mist is inherently temporal — a still freezes the one thing that proves the product works.",
   duration_s=3, loop="seamless", shot="locked frame on the mounted unit and desk",
   action="mist drifts down and outward, curtain lifts once", result="the cool stream reads as continuous, not staged",
   match="backlit hero grade; mist stays the brightest element", delivery="mp4/webm, gif fallback, max 3 MB"),
 "compare-mechanism": dict(eligible=True, form="whole-frame", asset=f"{PAGE}-08-mechanism.mp4",
   reason="The claim IS a process: air in, through the wet grille, cool mist out. The maglev rotor floating without contact is a motion claim a still cannot make.",
   duration_s=4, loop="seamless", shot="locked three-quarter on the ghost shell",
   action="wind wheel spins, the flow ribbon travels intake to louvers", result="the rotor never touches its ring",
   match="navy/cyan palette lock; no new components appear", delivery="mp4/webm, gif fallback, max 3 MB"),
 "howto-steps": dict(eligible=True, form="inset", asset=f"{PAGE}-09-howto-panel3.mp4",
   reason="Panels 1 and 2 are single acts a still holds fine. Panel 3 is the payoff and the only temporal beat — the mist starting. Motion replaces that panel only; the type's own skeleton already legislates three panels, so no new layer is proposed.",
   duration_s=2, loop="seamless", shot="panel 3 framing, unchanged",
   action="fingertip presses, the first mist stream emerges", result="air visibly moving where there was none",
   match="panel 3's warmer light; the other two panels stay still", delivery="mp4/webm, gif fallback, max 2 MB"),
 "social-viral": dict(eligible=True, form="whole-frame", asset=f"{PAGE}-10-social-1.mp4",
   reason="A customer's phone clip is MORE authentic than a customer's photo — the register's whole argument is that nothing was staged, and a handheld wobble proves it harder than a still can.",
   duration_s=3, loop="once", shot="handheld, slight natural drift",
   action="the phone tilts up to the running unit", result="it is on, in a real room, right now",
   match="ugc register: honest exposure, visible noise, no grade", delivery="mp4/webm, gif fallback, max 2 MB"),
}
NO_GIF_REASON = ("The slot exists to indict a static condition — drilled brackets, a hose "
 "across a counter, a fan that never moves the air. Nothing in it changes over time, so "
 "motion would add duration without adding argument. Temporal test fails.")
for s in slots:
    if not s["options"]: continue
    sid=s["slot_id"]
    if sid in GIF: s["gif"]=GIF[sid]
    elif sid.startswith("reason-") and sid!="reason-0-editors-pick":
        s["gif"]=dict(eligible=False, form="none", reason=NO_GIF_REASON)


ALT_B = {
 "reason-1-window-ac": ("execution: seen from the street, the room it darkens",
  "the same boxy window air conditioner seen from OUTSIDE the building, jutting from a first-floor sash with a rust streak running down the render below it, the room behind it dark. Ordinary, intact, plausible.",
  "the drip stain on the wall beneath the unit; the sash permanently propped and taped at one corner; a neighbouring window with clean glass and an open curtain for contrast."),
 "reason-2-portable-ac": ("execution: the hose as the subject, close range",
  "the wide corrugated exhaust hose of a generic portable air conditioner filling the frame at close range where it crosses a windowsill into a plastic vent panel, the unit itself soft behind it.",
  "gaffer tape sealing the panel edge; a gap where warm outside air leaks back in; the sill's paint scuffed where the hose rests."),
 "reason-3-floor-cooler": ("execution: the floor it steals, shot from the doorway",
  "the tall floor-standing evaporative cooler seen from the kitchen doorway so its footprint dominates the walkway, its water tank at the base with the fill flap open.",
  "the power lead crossing the threshold at ankle height; a shopping bag set down at an angle because the direct line is blocked; a chair pulled out to squeeze past."),
 "reason-4-desk-fan": ("execution: the desk it fails to cool, wide",
  "a cheap white plastic desk fan running at the edge of a home-office desk, seen wide so the whole workspace reads.",
  "papers held down by a mug rather than lifted by any draft; a cardigan pushed off and hanging on the chair; a glass of water sweating a ring onto the desk; the fan's ribbon limp."),
 "reason-5-ceiling-fan": ("execution: the bed below, looking up",
  "a white ceiling fan seen from lying-down height at the foot of a bed, blades still, the ceiling filling the upper frame.",
  "the duvet kicked into a heap in the foreground; the repainted ring around the mounting plate; a phone face-up on the nightstand at the frame edge."),
}
for s in slots:
    if s["slot_id"] in ALT_B and len(s["options"])==1:
        base=s["options"][0]; varies, subj, ev = ALT_B[s["slot_id"]]
        b=dict(base); b["opt"]="B"; b["varies_on"]=varies
        NL = chr(10)
        pat = "SUBJECT, the indicted object: .*?" + NL+NL + "SYMPTOM EVIDENCE, physical fact: .*?" + NL
        rep = ("SUBJECT, the indicted object: " + subj + NL+NL +
               "SYMPTOM EVIDENCE, physical fact: " + ev + NL)
        b["prompt"]=re.sub(pat, rep.replace("\\", "\\\\"), base["prompt"], flags=re.S)
        b["rationale"]=("Second variation on the same type and entry, varying on execution — a different "
                        "vantage on the same indicted object. The >=2 floor is met without a reroll: this is "
                        "a genuinely different staging of the same argument, which is a real named dimension.")
        b["asset_candidate"]=base["asset_candidate"].replace(".jpg","--B.jpg")
        base["asset_candidate"]=base["asset_candidate"].replace(".jpg","--A.jpg")
        s["options"].append(b)

# ══════════════════════════════════════════ genuinely imageless
slots.append({"slot_id":"comments-thread","section_role":"social-proof","options":[],
 "out_of_scope_reason":"A 48-comment discussion thread is page furniture — text, avatars and timestamps rendered by the template. Not an image slot, so the never-empty rule does not apply. The ledger drew this same boundary twice before (a pricing panel, a hero banner)."})
slots.append({"slot_id":"offer-atc","section_role":"cta","options":[],
 "out_of_scope_reason":"The cta cell is empty by design in mapping/slot-rules.md — a standard product shot, outside library scope. Not an image slot in the library's sense."})

for s in slots: s.pop("_setn", None)


# ══════════════════════════════════════════ COVERAGE PASS (awareness-driven)
COVERAGE = {
 "covered": ["step 1 pain (hero)", "step 3 mechanism (xray)", "step 3 use (use-sequence)",
             "step 5 social (snapshot)", "step 6 relief (relief-hero)"],
 "absent": ["step 2 amplify the problem", "step 4 physical proof"],
 "absent_but_correct": [
   "step 2 amplify the problem — the reader is SOLUTION-AWARE: they already feel the "
   "problem and are comparing solution classes. Re-amplifying it would insult them and "
   "delay the comparison they came for. This absence is a correct editorial choice, not "
   "a gap; recorded so a later reader does not 'fix' it."],
 "gaps": [
   "step 4 physical proof — the material gap. A solution-aware reader decides on "
   "evidence, and this page knocks down five alternatives and closes on the product "
   "without showing a single inspectable fact. 04-proof-lockedframe is advertorial-legal "
   "and unused."],
}
REC_AVOID = ("Avoid: text, watermarks, logos, badges, checkmarks, arrows, glows, people, hands, "
             "one panel brighter than the others, damaged or dirty alternatives, red or green cues, "
             "motion blur, studio background, staged perfection.")
rec_scene = ("SCENE, constant across all panels: the corner of a small rented room beside a window "
 "— a desk with a laptop and papers, a mug, a phone charging, a cable along the skirting, a jacket "
 "over the chair. Flat overcast daylight, no strong shadows, no styling.")
recommended = [{
 "slot_id":"proof-lockedframe","section_role":"proof",
 "earns_its_place":("Fills step 4, the one absent rung the SOLUTION-AWARE stage says matters. "
   "The page argues its whole case by assertion — five alternatives dismissed in copy, no "
   "inspectable fact anywhere. This is the rung that decides a comparing reader."),
 "suggested_placement":("Between the `compare` table and the `social` section — after the claims "
   "are made and before the testimonials, which is where a skeptic looks for proof."),
 "asset":f"{PAGE}-11-proof.jpg",
 "gif":dict(eligible=False, form="none",
   reason=("--rivals is a judgement-free exhibit: three states held equally still so the viewer "
           "compares them. Motion would direct the eye and break exactly the neutrality the type "
           "exists to protect. Temporal test fails on purpose.")),
 "options":[
  O("A","baseline","04-proof-lockedframe","1.4","5:3", f"""
Three photographs of the same corner of a small rented room, shown as three equal vertical panels, thin white gutters, no outer border. No graphic overlays, badges, arrows or text.

No reference product appears in this image. All three panels contain generic unbranded alternatives — the cooling appliances people already own.

LOCKED CAMERA: identical camera position, focal length, height and angle in every panel. Every fixed element aligns across all panels: the desk and chair, the window and its blinds, the wall outlet, the rug edge, the skirting board. Identical lighting, exposure and white balance in every panel.

{rec_scene}

THE VARIABLE, the only thing that changes — the cooling appliance occupying the corner:
Panel 1: a boxy window air conditioner filling the lower half of the window, the sash resting on it, the desk pushed aside to clear it.
Panel 2: a generic portable compressor air conditioner on the floor, its wide exhaust hose climbing to the propped window sash, crowding the desk.
Panel 3: a tall floor-standing evaporative cooler in the same corner, water tank visible at the base, taking the walking space.
All three look ordinary, intact and plausible — never broken, dirty or mocked.

JUDGEMENT RULE: none of them wins. The image makes no claim. No badge, glow, colour cue or brighter panel. All panels equally lit and equally neutral. The viewer decides.

Honest documentary product test photography, unstyled, natural, sharp. No text, no logo, no watermark.
""", REC_AVOID,
   "Step 4 for a solution-aware reader. --rivals is the 'I tried three things' beat and needs NO reference photo, so it cannot suffer product drift. Advertorial-legal; --rivals is barred only from marketplace.",
   "Additive proposal, not a page section. Cross-slot: 04-proof-lockedframe is unused, one-type-once is satisfied, step-3 budget untouched (this is step 4).",
   variant="rivals", axes={"camera_lock":"strict","context_mode":"natural-use"},
   pipeline="multi-pass", att=False, cand=f"{PAGE}-11-proof--A.jpg",
   steps=["generate — panel 1 only: the room corner with the boxy window unit in the sash.",
          "edit — 'Keep everything exactly the same and change ONLY the cooling appliance: a portable compressor unit on the floor with its hose to the propped sash.'",
          "edit — 'Keep everything exactly the same and change ONLY the cooling appliance: a tall floor-standing evaporative cooler, water tank at the base.'",
          "composite — assemble three panels with thin white gutters in an image editor."]),
  O("B","execution: kitchen corner, the cook's workspace","04-proof-lockedframe","1.4","5:3", f"""
Three photographs of the same end of a small kitchen, shown as three equal vertical panels, thin white gutters, no outer border. No graphic overlays, badges, arrows or text.

No reference product appears in this image. All three panels contain generic unbranded alternatives.

LOCKED CAMERA: identical camera position, focal length, height and angle in every panel. Every fixed element aligns: the counter edge, the small window above it, the tile line, the kettle, the bin. Identical lighting, exposure and white balance.

SCENE, constant across all panels: the end of a kitchen counter under a small window — a chopping board mid-use, a kettle, a dish rack, a towel on the oven rail, a jar left open. Flat overcast daylight, no strong shadows, no styling.

THE VARIABLE, the only thing that changes — what cools the cook's corner:
Panel 1: an ordinary box fan standing ON the counter, crowding the chopping board aside.
Panel 2: a generic portable compressor air conditioner on the floor, its wide hose climbing across the counter and out the propped window.
Panel 3: a tall floor-standing evaporative cooler wedged into the galley, water tank at the base, blocking the walkway.
All three look ordinary, intact and plausible — never broken, dirty or mocked.

JUDGEMENT RULE: none of them wins. The image makes no claim. No badge, glow, colour cue or brighter panel. All panels equally neutral.

Honest documentary product test photography, unstyled, natural, sharp. No text, no logo, no watermark.
""", REC_AVOID,
   "Same variant staged where the page's lead pain lives. A hose crossing a chopping board argues the space cost more viscerally than a desk does.",
   "Additive proposal. Meets the >=2 floor by execution, not by reroll.",
   variant="rivals", axes={"camera_lock":"strict","context_mode":"natural-use"},
   pipeline="multi-pass", att=False, cand=f"{PAGE}-11-proof--B.jpg",
   steps=["generate — panel 1 only: the kitchen counter corner with the box fan.",
          "edit — same-frame swap to the portable unit, hose across the counter.",
          "edit — same-frame swap to the tall floor cooler blocking the galley.",
          "composite — assemble three panels with thin white gutters."])]
}]

out = {"page_id":"13-inch-portable-wall-mounted-air-cooler-cool-your-space",
 "registry_version":"2.0.0","channel":"advertorial","awareness_stage":"solution-aware",
 "slots":slots,"coverage":COVERAGE,"recommended":recommended,
 "page_composition_notes":[
  "INPUT: flunnel export, lpTypeId `listicle` (TPL-ADV07). The content contract's enum has no `listicle`, so this routes as `advertorial` — editorial byline (Dana Merrick), an Updated date and a pain-first intro are the advertorial signature.",
  "STAGE 1 IS DERIVED, not looked up (SPEC 7.2 as of 2026-08-11): candidates come from registry/index.yaml by channel legality, then attribute gates, then role affinity from step+job. On advertorial the legal pool is 10 types covering every step 1-6, which is why no slot in this run is empty and no fallback exists.",
  "WHAT CHANGED SINCE THE FIRST RUN OF THIS PAGE: thirteen table/frontmatter contradictions were found and fixed (commit 973addf). The earlier output routed 02-symptom-rail, 03-use-sequence and 06-relief-hero on advertorial while their own frontmatter forbade it. use-sequence and relief-hero were widened (their own text demanded it); symptom-rail was NOT, so the problem-agitation beat is now carried by the hero alone.",
  "THE FIVE ALTERNATIVE ENTRIES now have real images. 01-pain-scene in its object-only execution serves all five, reached by the runbook's widening ladder: rung 2 (adjacent step — a step-1 pain type carries an indicted object) plus rung 3 (repeating section). Ledger precedent: obs sha256:30c9568… and sha256:4e8f238…, both filed as pain-scene with 'no person as subject, only the indicted OBJECT'. When 02-cause-scene promotes (3/5 exemplars) these move to it and gain a tighter skeleton.",
  "PRODUCT: identical to the advertorial page and to eval/golden/fixture-002. operation=passive, visible_output=mist, mounting=fixed-installed, colorways=[white, grey], body_contact=false, symptom_visibility=visible, result_visibility=on-body, multi_step_usage=true. Reference sha256:d3ce1b73… (cooler.avif).",
  "COMPLIANCE, the sharp one: every social card on this page carries a name and a `Verified Buyer` badge. 05-social-snapshot's authenticity fence forbids a generated snapshot sitting next to a reviewer name, avatar, star row or verified label. Use these as SECTION imagery — a band above or between the cards — never inside a card. Real customer photos are the only thing that may sit inside those cards.",
  "UNVERIFIED CLAIMS — not rendered: the brief itself flags 13°C in 10 seconds, 300% efficiency, aerospace-grade refrigeration and 10dB(A) as claims other pages for the same product drop. No prompt visualises a temperature drop, a decibel figure or a percentage. Mist is rendered because it is real; a number is not an image argument.",
  "CROSS-SLOT: one-type-once holds, with the repeating-section exception used twice and named both times (the five alternatives; the snapshot set). Step-3 budget used 2 of 2 (xray + use-sequence). 04-proof-lockedframe is unused and available if a grouped proof frame is wanted instead of, or beside, the five entries.",
  "RATIO: passed as the generation parameter only, never written in the prompt (adapter Rule 4 — 6/6 renders ignored a written ratio). Prompts spend their words on composition instead: share of frame, offset side, layer footprints.",
  "TIE-BREAKERS: feedback/picks.jsonl is empty — no (type x role) cell reaches the 20-pick threshold, priors unused."]}

json.dump(out, open("/Users/lethiendung/Downloads/listicle-cooler.image-prompts.json","w"), indent=2, ensure_ascii=False)

md=["# Image prompts — 13-Inch Portable Wall-Mounted Air Cooler (listicle)","",
    "Registry 2.0.0 · 14 types · channel advertorial · Stage 1 derived · adapter nano-banana level C · 2026-08-11","",
    "**Ten assets, every one routed to a real active type. No fallbacks, no empty image slots.**","",
    "## Asset manifest\n",
    "Render candidates as `…--A.jpg` / `--B` / `--C`; the picked option is renamed to the canonical",
    "name, which is what the page layout references. Ratio is a render PARAMETER, never prompt text.","",
    "| # | Asset | Slot | Type | Placement |","|---|---|---|---|---|"]
i=0
for s in out["slots"]:
    if not s["options"]: continue
    i+=1
    md.append(f"| {i} | `{s['asset']}` | `{s['slot_id']}` | `{s['options'][0]['type']}` v{s['options'][0]['type_version']} | {s['placement']} |")
for s in out["slots"]:
    if not s["options"]:
        md.append(f"| — | (no image by definition) | `{s['slot_id']}` | — | see note below |")
md += ["", "## Coverage — awareness stage: **solution-aware**\n"]
md.append("The reader already feels the problem and is comparing solution classes. That is what")
md.append("decides which absent rung is a gap and which is a correct omission — not the page format.\n")
md.append("| Rung | Status |")
md.append("|---|---|")
for c in out["coverage"]["covered"]: md.append(f"| {c} | covered |")
for c in out["coverage"]["absent_but_correct"]: md.append(f"| {c.split(chr(8212))[0].strip()} | **absent, and correct** — {c.split(chr(8212),1)[1].strip()} |")
for c in out["coverage"]["gaps"]: md.append(f"| {c.split(chr(8212))[0].strip()} | **GAP** — {c.split(chr(8212),1)[1].strip()} |")
md += ["", "## Recommended — not asked for by the page\n"]
md.append("Additive proposals. They are NOT page sections and are not counted in the manifest above.\n")
for r in out["recommended"]:
    md.append(f"- **`{r['asset']}`** ({r['slot_id']}, `{r['options'][0]['type']}`) — {r['earns_its_place']}")
    md.append(f"  - Placement: {r['suggested_placement']}")
md += ["", "## Page-level notes\n"]
for n in out["page_composition_notes"]: md.append(f"- {n}")
for s in out["slots"]:
    md.append(f"\n---\n\n## `{s['slot_id']}` — role: {s['section_role']}\n")
    if not s["options"]:
        md.append(f"**NO IMAGE BY DEFINITION.** {s['out_of_scope_reason']}\n"); continue
    md.append(f"**ASSET:** `{s['asset']}` · **RENDER AT:** {s['options'][0]['ratio']} (generation parameter)")
    md.append(f"**PLACEMENT:** {s['placement']}\n")
    g=s.get("gif")
    if g:
        if g["eligible"]:
            md.append(f"**GIF — {g['form']}** → `{g['asset']}`  ·  {g['reason']}\n")
            md.append("```text")
            md.append(f"GIF · {g['duration_s']}s · {g['loop']}")
            for k in ("shot","action","result","match"):
                if g.get(k): md.append(f"{k.upper():<8} {g[k]}")
            md.append("```")
            md.append(f"*Delivery: {g['delivery']}*\n")
        else:
            md.append(f"**GIF — no.** {g['reason']}\n")
    for o in s["options"]:
        md.append(f"### Option {o['opt']} — `{o['type']}` v{o['type_version']}"
                  + (f" --{o['variant']}" if o.get("variant") else "")
                  + f" · {o['pipeline']}")
        md.append(f"*varies_on: {o['varies_on']}*")
        if o.get("axes"): md.append(f"*axes: {', '.join(f'{k}={v}' for k,v in o['axes'].items())}*")
        md.append("\n```text\n"+o["prompt"]+"\n```\n")
        md.append(f"**Avoid:** {o['avoid']}\n")
        md.append(f"**Render as:** `{o.get('asset_candidate','—')}`" + ("  ·  **Attach:** `cooler.avif`" if o.get("attachments") else "") + "\n")
        md.append(f"**Why:** {o['rationale']}\n")
        md.append(f"**Notes:** {o['composition_notes']}\n")

for r in out["recommended"]:
    md.append(f"\n---\n\n## RECOMMENDED `{r['slot_id']}` — role: {r['section_role']} (proposal, not a page section)\n")
    md.append(f"**ASSET:** `{r['asset']}` · **EARNS ITS PLACE:** {r['earns_its_place']}")
    md.append(f"**PLACEMENT:** {r['suggested_placement']}\n")
    g=r.get("gif")
    if g and not g["eligible"]: md.append(f"**GIF — no.** {g['reason']}\n")
    for o in r["options"]:
        md.append(f"### Option {o['opt']} — `{o['type']}` v{o['type_version']}"+(f" --{o['variant']}" if o.get('variant') else "")+f" · {o['pipeline']}")
        md.append(f"*varies_on: {o['varies_on']}*")
        md.append("\n```text\n"+o["prompt"]+"\n```\n")
        md.append(f"**Avoid:** {o['avoid']}\n")
        if o.get("steps"):
            md.append("**Multi-pass steps:**")
            for i2,st in enumerate(o["steps"],1): md.append(f"{i2}. {st}")
            md.append("")
        md.append(f"**Render as:** `{o.get('asset_candidate','—')}`\n")
        md.append(f"**Why:** {o['rationale']}\n")
        md.append(f"**Notes:** {o['composition_notes']}\n")
open("/Users/lethiendung/Downloads/listicle-cooler.image-prompts.md","w").write("\n".join(md))
n=sum(len(s["options"]) for s in out["slots"])
print(f"slots {len(out['slots'])} | options {n} | assets {i}")

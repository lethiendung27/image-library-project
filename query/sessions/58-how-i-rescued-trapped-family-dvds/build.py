#!/usr/bin/env python3
"""Build prompts.json and prompts.md for page 58 — 7-in-1 external DVD/Blu-ray drive.

prompts.json is the source of truth (query/output.schema.json); prompts.md is
generated from it and is never hand-edited (query/runbook.md Step 7).

Run from anywhere:  python3 query/sessions/58-.../build.py
"""
import json
import os
import re


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

# What each type NEEDS in order to run, read from the generated index rather than
# retyped here. requires_product_photo is the fact that decides whether a prompt
# is paste-and-run today, and it moves when a type file moves.
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
                out[tid][k] = {"true": True, "false": False}.get(v, v)
    return out


TYPES = _index_types()

# Per-type prompt ceilings, each taken from that type's own SLOT CONSTRAINTS.
CEIL = {"01-pain-scene": 2500, "02-cause-anatomy": 2050, "03-mechanism-xray": 1900,
        "04-proof-lockedframe": 1800, "05-social-snapshot": 1800,
        "06-relief-hero": 2300, "06-relief-scene": 2100}

# --------------------------------------------------------------- hero.image ---

P_HERO_A = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man in his forties, work shirt with the collar open, sitting forward on the edge
of a living-room sofa late in the evening, mid-way through turning a DVD disc
over in both hands to check its underside against the light. Under that force:
both elbows on his knees, shoulders rolled forward over the disc, the wrists
angling it back and forth.
Face: brow drawn in, jaw set, eyes down on the disc.

[EVIDENCE]
A slim closed laptop sits on the coffee table in front of him with an unbroken
edge and no slot anywhere along it, and a shoebox of loose DVD cases stands open
beside it with the discs half out of their sleeves, one case lying face down on
the carpet where it slid off the pile.

[ENVIRONMENT]
An ordinary front room, evening. Lived-in clutter belonging to that place: two
mugs on the coffee table, a folded throw pushed to one end of the sofa, a
child's cardigan over the arm, the curtains already drawn. Nothing arranged,
nothing removed to tidy the frame.

[GAZE] unaware of the camera, gaze down on the disc in his hands.

[LIGHT] low-key. Key: a single table lamp beside the sofa, warm and close. Fill:
cold spill from a hallway doorway behind him. Rim light along the shoulder and
the edge of the disc. Deep shadow across most of the frame.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

P_HERO_B = """TYPE: 01-pain-scene v1.14 --confront
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Man in his forties, work shirt with the collar open, sitting at a kitchen table
turned square to camera, mid-way through pushing a DVD disc into the closed side
edge of a slim laptop where a slot would be, the disc stopped flat against the
casing and his thumb still pressing it there. Under that force: the forearm
locked, the shoulder dropped behind the push, the other hand flat on the table
taking the laptop's weight.
Face: mouth pressed flat, brow drawn in, chin tucked.

[EVIDENCE]
The disc stands proud of the laptop's unbroken edge with nowhere to go, and a
stack of DVD cases sits at his elbow with the top one open and empty, its
inner sleeve still holding the leaflet.

[ENVIRONMENT]
An ordinary kitchen table, early evening. Lived-in clutter belonging to that
place: a cold mug, a school bag slumped against a chair leg, a fruit bowl, a
tea towel over the radiator. Nothing arranged, nothing removed to tidy the
frame.

[GAZE] looking directly into the lens, holding the viewer's eye.

[LIGHT] even ambient daylight from a window behind the camera, minimal shadow,
flat and unflattering.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated neutral, muted greys and greens, fine film grain, moderate
depth of field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

P_HERO_C = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
Woman in her fifties in a cardigan, kneeling on the floor of a spare room beside
an open storage crate, mid-way through lifting a stack of unlabelled home-video
discs out of it with both hands, the stack sagging apart as it comes up. Under
that force: the back rounded over the crate, both elbows out, one knee taking
her weight on the bare boards.
Face: brow drawn in, lips parted, eyes down on the stack.

[EVIDENCE]
The disc on top of the stack has a dulled milky bloom across its playing side
and a fine scatter of surface scratches catching the light, and two more discs
have slipped from the stack and lie face down on the floorboards beside a crate
lid furred with dust.

[ENVIRONMENT]
An ordinary spare room used for storage, afternoon. Lived-in clutter belonging
to that place: a stripped single bed pushed against the wall, a clothes airer
folded behind the door, two more crates stacked unopened, a roll of wrapping
paper on its side. Nothing arranged, nothing removed to tidy the frame.

[GAZE] unaware of the camera, gaze down on the discs in her hands.

[LIGHT] low-key. Key: thin daylight from one small window high on the wall,
raking across the floor. Fill: none to speak of. Rim light along the forearm and
the edge of the top disc. Deep shadow across most of the frame.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

# ------------------------------------------------- problems.items.0.image ---

P_PROB0_A = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
No person. The subject is a home desk in the state its owner left it, shot low
and close across the desktop so the tangle fills the frame.

[EVIDENCE]
A cheap grey plastic external drive sits skewed on the desk with its tray jammed
half open and a disc still resting in it, its single cable stretched taut across
the desktop to the one free port on a closed slim laptop. Three separate adapter
dongles hang off that same side in a knot, their cables crossing and looping back
on themselves, one of them unplugged entirely and lying on the desk with its
connector face up. A wireless mouse sits at the edge of the desk with its own
receiver stub loose beside it, plugged into nothing.

[ENVIRONMENT]
An ordinary home desk in a corner of a room, evening. Lived-in clutter belonging
to that place: a cold mug ringing the wood, a phone face down, a pair of glasses
folded on a notebook, a charger brick that has nowhere to go. Nothing arranged,
nothing removed to tidy the frame.

[GAZE] no person in the frame.

[LIGHT] low-key. Key: a desk lamp low and to one side, hard and close across the
cables. Fill: cold spill from a screen out of frame. Rim light along the drive's
top edge and the taut cable. Deep shadow across most of the frame.

[FORBIDDEN] No reference product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

P_PROB0_B = """TYPE: 04-proof-lockedframe v1.13 --rivals, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
Not applicable. No product appears in this image.

[SCENE — the same in all three]
The same corner of a home desk, the same dark wood desktop, a closed slim laptop
pushed to the back and a cold mug beside it. Flat overcast light from a window off to the left, no strong
shadows, no styling.

[FRAMING]
One person photographed this three times across a fortnight from where they
always sit, phone level with the desktop, the bare wood filling the middle
third and the laptop across the upper third. It reads as one shot taken three
times, never as three different shots. Light differs only in exposure, never warmth.

[THE VARIABLE]
Three ways people already try to read a disc on a laptop with no drive, each
photographed mid-attempt, each with the same unbranded silver disc present.
1 — a thin unbranded plastic external drive, its tray half open with the disc in
it, its cable running to the laptop's only port; the mug at the back, handle out.
2 — three adapter dongles chained one into another, the disc propped against them
unread, the last connector hanging free; the mug turned, a pen beside it.
3 — a padded post bag lying open with the disc and a folded blank slip inside it,
ready to be sent away; the mug gone, a roll of tape in its place.

[GRADE — the same in all three]
Muted and cool, low saturation, no warm tone anywhere, from the overcast window
and the drab desktop rather than a filter. Still colour, never black and white.

No panel is favoured and no panel is brighter. None of the three wins and the
image makes no claim."""

P_PROB0_C = """TYPE: 01-pain-scene v1.14 --candid
REGISTER: cinematic film still. Single frame.

[SUBJECT]
No person. The subject is a kitchen worktop where the overflow of a desk has
ended up, shot square on from worktop height.

[EVIDENCE]
A cheap grey plastic external drive lies on its side on the worktop with its
tray sprung open and empty, a hairline crack running from one corner of the
casing, and a silver disc face down beside it with a fan of fine scratches
across the playing side. Two adapter dongles sit coiled in a shallow bowl that
normally holds keys, their connectors tarnished, and a bundled cable has been
wound and tucked under the bowl's rim to keep it from unravelling.

[ENVIRONMENT]
An ordinary kitchen worktop by a wall socket, morning. Lived-in clutter
belonging to that place: a bread bin with crumbs at its foot, a jar of wooden
spoons, a tea towel hooked on the oven rail, a charger already occupying the
socket. Nothing arranged, nothing removed to tidy the frame.

[GAZE] no person in the frame.

[LIGHT] low-key. Key: hard morning sun through a window to the right, throwing a
sharp-edged shadow of the drive across the worktop. Fill: weak bounce off the
wall tiles. Rim light along the cracked casing edge. Deep shadow across the left
of the frame.

[FORBIDDEN] No reference product, no panels, no insets. No mark of any kind.

[GRADE] Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of
field, 35mm.

STYLE: editorial photojournalism, cinematic film still, natural and unstaged."""

# ------------------------------------------------- problems.items.1.image ---

P_PROB1_A = """TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, flat-vector. NOT photography, NOT 3D.

FRAME: the whole optical assembly of a disc drive in shot, seen in cross-section
from the side, the reading lens small within it.
GROUND: deep desaturated slate blue, the right half one step lighter than the
left.
BODY: a disc lying flat with its data track layer drawn as a fine ridged band on
its underside, and below it the reading lens carried on its sled, cut as flat
layers in warm ivory over a translucent drive-body outline. NOT a skeleton, NOT a
human figure. Exactly one assembly in EACH panel, same scale and same side view.

PANELS. LEFT: the assembly mounted on a bare unbalanced spindle motor drawn
realistically and unbranded, the motor's rotation shaking the sled so the lens
sits off to one side of the track and its beam lands on blank disc between two
ridges. RIGHT: the same assembly on the same interface, the sled seated in a
damping groove carriage of the same size, the lens held under the track and its
beam landing on the ridged band itself. The disc and its track layer appear in
both panels and neither the motor nor the carriage covers them.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each PERPENDICULAR TO THE
  UNDERSIDE OF THE DISC, running from the centre of the track band down to the
  centre of the lens and STOPPING at both. Both begin at the same point on the
  track band, at the same place in their panel. Identical thickness and dash. One
  property differs: the sideways offset - wide on the left, closed to almost
  nothing on the right. Red left, blue right. Straight lines, not boxes.
- verdict: filled solid discs, red with a white X in the left panel's TOP corner,
  green with a white check in the right panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else."""

P_PROB1_B = """TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, airbrushed. NOT photography, NOT 3D.

FRAME: the whole side wall of a slim laptop in shot with its single port, the
port opening small within it.
GROUND: deep desaturated plum, the right half one step lighter than the left.
BODY: the port opening and the power rail running back from it into the machine,
drawn as soft modelled layers in warm ivory over a translucent laptop-wall
outline, with the rail's width shown along its length. NOT a skeleton, NOT a
human figure. Exactly one port and rail in EACH panel, same scale and same side
view.

PANELS. LEFT: a chain of three separate adapter dongles drawn realistically and
unbranded, plugged one into another and all into that single port, the rail
behind the port drawn pinched narrow where the load meets it. RIGHT: one
combined hub unit of the same size seated at the same port, its own supply lead
running away to the side, the rail behind the port drawn at its full width. The
port and the rail appear in both panels and neither the dongle chain nor the hub
covers them.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each PERPENDICULAR TO THE
  OUTER FACE OF THE PORT, running across the rail from one wall of it to the
  other and STOPPING at both. Both sit at the same distance behind the port, at
  the same place in their panel. Identical thickness and dash. One property
  differs: the rail width - narrow on the left, wide on the right. Red left, blue
  right. Straight lines, not boxes.
- verdict: filled solid discs, red with a white X in the left panel's TOP corner,
  green with a white check in the right panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else."""

P_PROB1_C = """TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, flat-vector. NOT photography, NOT 3D.

FRAME: the whole spindle motor and disc platter in shot, seen straight on from
the front, the bearing small within it.
GROUND: deep desaturated teal, the right half one step lighter than the left.
BODY: the spindle shaft, its bearing collar and the disc platter seated on it,
cut as flat layers in warm ivory over a translucent chassis outline. NOT a
skeleton, NOT a human figure. Exactly one spindle and platter in EACH panel, same
scale and same front view.

PANELS. LEFT: the shaft running in a bare loose-fitting collar drawn realistically
and unbranded, the platter tilted off level on it and its rim standing high on one
side. RIGHT: the same shaft in a counterweighted collar of the same size at the
same interface, the platter sitting level and its rim at the same height all the
way round. The platter and the collar appear in both panels and neither covers
the other.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each PARALLEL TO THE FACE OF
  THE PLATTER, running from the top of the collar up to the underside of the
  platter rim on the raised side and STOPPING at both. Both begin at the same
  point on the collar, at the same place in their panel. Identical thickness and
  dash. One property differs: the gap - wide on the left, closed to almost
  nothing on the right. Red left, blue right. Straight lines, not boxes.
- verdict: filled solid discs, red with a white X in the left panel's TOP corner,
  green with a white check in the right panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else."""

# ------------------------------------------------- features.items.0.image ---

P_F0_A = """TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the external
DVD drive. The outer shell becomes translucent, but its silhouette, proportions
and every visible external part must match the reference exactly. Do not redesign
or add features.

CANVAS: a plain deep charcoal ground, and nothing else in the frame behind the
product.

SHELL: the drive lying flat and seen from above and slightly to one side, its
top casing translucent and glass-like, filling about 75 percent of the frame
width.

INTERNALS, solid and detailed inside the shell, each at its true location: the
optical pickup lens on its sled, carried on a damping groove carriage that runs
the length of the bay; a flat spindle motor at the centre of the bay with a disc
seated on it; a control board along the back edge in its own real board colour;
a ribbon cable folding from the board to the sled.

MARKS, one, nothing else in the frame is marked:
- working: the optical pickup lens shown ACTIVE, throwing a narrow cool cyan
  beam straight up onto the underside of the disc above it, the brightest thing
  in the frame and clearly brighter than the ground. No arrow anywhere - the
  carriage's own line carries the direction of travel.

No text, numbers or spec labels anywhere in the image.
The marks are the only added colour; the product and its parts keep their own."""

P_F0_B = """TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the external
DVD drive. The outer shell becomes translucent, but its silhouette, proportions
and every visible external part must match the reference exactly. Do not redesign
or add features.

CANVAS: a plain pale warm grey ground, and nothing else in the frame behind the
product.

SHELL: the drive seen end-on from its front edge and slightly above, the tray
seam facing the camera, its casing translucent and glass-like, filling about 70
percent of the frame width.

INTERNALS, solid and detailed inside the shell, each at its true location: the
optical pickup lens on its sled directly behind the tray seam, seated in a
damping groove carriage; a flat spindle motor behind it; a control board beneath
in its own real board colour; the port bank moulded into the rear wall with its
two rectangular openings, one oval opening and one card slot.

MARKS, one, nothing else in the frame is marked:
- working: the optical pickup lens shown ACTIVE, throwing a narrow cool cyan
  beam upward from the lens face, the brightest thing in the frame and clearly
  brighter than the ground. No arrow anywhere.

No text, numbers or spec labels anywhere in the image.
The marks are the only added colour; the product and its parts keep their own."""

P_F0_C = """TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the external
DVD drive. The outer shell becomes translucent, but its silhouette, proportions
and every visible external part must match the reference exactly. Do not redesign
or add features.

CANVAS: a plain deep olive ground, and nothing else in the frame behind the
product.

SHELL: the drive standing on its long edge and seen from a low front
three-quarter angle, its casing translucent and glass-like, filling about 65
percent of the frame height.

INTERNALS, solid and detailed inside the shell, each at its true location: the
optical pickup lens on its sled part-way along its damping groove carriage; a
flat spindle motor with a disc seated on it above the sled; a control board down
the lower edge in its own real board colour; a bridge chip on that board beside
the port bank.

MARKS, one, nothing else in the frame is marked:
- working: the optical pickup lens shown ACTIVE, throwing a narrow cool cyan beam
  across the short gap onto the disc surface facing it, the brightest thing in the
  frame and clearly brighter than the ground. No arrow anywhere - the carriage's
  own line carries the direction of travel.

No text, numbers or spec labels anywhere in the image.
The marks are the only added colour; the product and its parts keep their own."""

# ------------------------------------------------- features.items.1.image ---

P_F1_A = """TYPE: 06-relief-hero v1.15 --commercial, inset --detail
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Man in his forties in a soft grey shirt, sitting back at a home desk with one
hand resting on a wireless mouse and the other loose in his lap, watching the
laptop screen rather than the drive. Relaxed, gaze away from the product.

[PRODUCT]
The drive on the desk between him and the laptop, front three-quarter angle,
whole and unobstructed, close enough to the camera to read. A single cable runs
from it to the laptop's one port. Into the drive's own rear ports run a mouse
receiver, a short cable to a phone lying beside it, and a memory card seated in
its card slot with its edge standing proud.

[SETTING]
A real home desk filled to the edges: a cold mug, a folded pair of glasses, a
notebook with a pen across it, a small plant, a coaster, a drawer unit under the
desk. None of them carries printed words. Background soft, never blank.

[LIGHT]
Soft even window light from the left, background blurred, high-key.

[LAYOUT]
He sits to the right of the frame; the left side carries the desk running away
from the camera.

In the upper left corner sits a rounded rectangular panel about a fifth of the
picture's width, held well clear of both frame edges, with a thin white border.
Inside it, one magnified straight-on view of the drive's rear port bank alone,
lit cleanly, close enough that the two rectangular ports, the single oval port
and the card slot are each separately readable, with a connector seated in one
of them. Nothing else is in the panel. It sits near the drive in the picture and
is joined to it by nothing - no arrow, no line, no glow.

No text on any object in either layer."""

P_F1_B = """TYPE: 06-relief-hero v1.15 --ugc, inset --detail
REGISTER: shot on a phone by an ordinary person. Slightly off exposure, mild
overexposure at the window, no rim light, framing casual and a little too close.
The room is left exactly as it is.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Man in his forties in a T-shirt, leaning back in a desk chair with a mug in one
hand, looking at the laptop screen rather than at the drive. Relaxed.

[PRODUCT]
The drive on the desk beside the laptop, front three-quarter angle, whole and
unobstructed, close to the camera. One cable runs from it to the laptop's single
port. A mouse receiver, a phone lead and a memory card are each seated in the
drive's own rear ports and card slot.

[SETTING]
A real home desk left as it is: a charger brick, a bowl of coins, a crumpled
receipt-sized slip of blank paper, a plant that needs watering, a jumper over
the chair back, a bin under the desk. None of them carries printed words.
Background soft, never blank.

[LIGHT]
Flat daylight through a window behind the desk, slightly blown at the glass. No
studio light.

[LAYOUT]
He sits to the right of the frame; the left side carries the desk and the window.

In the upper left corner sits a rounded rectangular panel about a fifth of the
picture's width, held well clear of both frame edges, with a thin white border.
Inside it, one magnified straight-on view of the drive's rear port bank alone,
lit cleanly, close enough that the two rectangular ports, the single oval port
and the card slot are each separately readable, with a connector seated in one
of them. Nothing else is in the panel. It sits near the drive in the picture and
is joined to it by nothing - no arrow, no line, no glow.

No text on any object in either layer."""

P_F1_C = """TYPE: 06-relief-hero v1.15 --commercial, inset --detail
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Present only as working hands and forearms: two hands at a kitchen table, one
seating a memory card into the drive's card slot, the other steadying the drive
by its far corner. No face in the frame.

[PRODUCT]
The drive flat on the table, seen from above and slightly to one side, whole and
unobstructed, filling the middle of the picture. A single cable runs from it off
to a laptop at the edge of frame. A mouse receiver and a phone lead are already
seated in its rear ports.

[EVIDENCE IN FRAME]
Every one of the drive's own ports has something in it and the card sits proud in
its slot, while the laptop at the edge of frame has one lead going to the drive
and no other cable touching it anywhere along its side.

[SETTING]
A real kitchen table filled to the edges: a fruit bowl, a folded newspaper-sized
sheet of blank paper, a set of keys, a plant, a cloth over a chair back, a bag on
the floor beyond. None of them carries printed words. Background soft, never
blank.

[LIGHT]
Soft even window light from the right, background blurred, high-key.

[LAYOUT]
The hands and the drive sit to the left of the frame; the right side carries the
table running away from the camera.

In the lower right corner sits a rounded rectangular panel about a fifth of the
picture's width, held well clear of both frame edges, with a thin white border.
Inside it, one magnified straight-on view of the drive's rear port bank alone,
lit cleanly, close enough that the two rectangular ports, the single oval port
and the card slot are each separately readable, with a connector seated in one of
them. Nothing else is in the panel. It sits near the drive in the picture and is
joined to it by nothing - no arrow, no line, no glow.

No text on any object in either layer."""

# ------------------------------------------------- features.items.2.image ---

P_F2_A = """TYPE: 06-relief-hero v1.15 --commercial, inset --context
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Woman in her thirties in a knitted jumper, standing at a hallway table with an
open laptop sleeve in one hand, sliding the drive down into it alongside a
closed laptop already inside, looking at the sleeve. Mid-action, hands engaged.

[PRODUCT]
The drive held upright in her hand at the mouth of the sleeve, side-on to the
camera, whole and unobstructed, its full thickness against the closed laptop's
edge behind it so the two read at the same scale.

[SETTING]
A real hallway filled to the edges: a bowl of keys on the table, a folded scarf,
a pair of shoes below, a coat on a hook, an umbrella leaning in the corner, a
radiator along the wall. None of them carries printed words. Background soft,
never blank.

[LIGHT]
Soft even daylight from a door glass to the left, background blurred, high-key.

[LAYOUT]
She stands to the right of the frame; the left side carries the hallway running
back to the door.

In the upper left corner sits a rectangular panel about a fifth of the picture's
width, held well clear of both frame edges, with a thin white border. Inside it,
a plainer closer shot of the same drive in the same place it lives: zipped inside
the same sleeve on the same hallway table, the sleeve's zip closed over it and
its outline just readable through the fabric, shot from a step back so the whole
sleeve is in the panel. Same light and same grade as the picture around it.

No text on any object in either layer."""

P_F2_B = """TYPE: 06-relief-hero v1.15 --commercial, inset --none
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive.
Preserve shape, proportions, material, finish and colour exactly.

[SUBJECT]
Man in his fifties in a work shirt with the sleeves turned back, sitting at a
dining table late in a long session, one hand resting flat on the table beside
the drive and the other on the back of his neck mid-stretch, looking out of the
window rather than at the machine. Relaxed, gaze away from the product.

[PRODUCT]
The drive flat on the table in front of him, front three-quarter angle, close to
the camera and whole and unobstructed, a disc seated in its open tray and a
short stack of three more discs beside it. One cable runs from it to a laptop
turned away at his elbow.

[SETTING]
A real dining table filled to the edges: a mug on a coaster, a pair of glasses
folded on a cloth, a bowl of apples, a jumper over the chair back, a lamp at the
table's end, curtains drawn back at the window. None of them carries printed
words. Background soft, never blank.

[LIGHT]
Soft even window light from the left, background blurred, high-key.

[LAYOUT]
He sits to the right of the frame; the left side carries the table running away
to the window.

No inset layer of any kind.

No text on any object in the picture."""

P_F2_C = """TYPE: 06-relief-hero v1.15 --commercial, inset --context
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Present only as working hands and forearms: two hands at a study desk, one
lifting the drive clear of a rucksack's open front pocket, the other holding the
pocket's edge back. No face in the frame.

[PRODUCT]
The drive held flat in one hand just above the pocket, seen from above and
slightly to one side, whole and unobstructed, close to the camera.

[EVIDENCE IN FRAME]
The pocket it has come out of still holds a folded cable and a slim notebook and
lies open and slack, while the drive in the hand is clear of everything with
nothing wrapped round it.

[SETTING]
A real study desk filled to the edges: a desk lamp pushed back, a pot of pens, a
water glass, a pair of headphones coiled, a chair arm at the frame edge, a bag
strap trailing off the desk. None of them carries printed words. Background
soft, never blank.

[LIGHT]
Soft even window light from the right, background blurred, high-key.

[LAYOUT]
The hands and the drive sit to the left of the frame; the right side carries the
desk running away from the camera.

In the lower right corner sits a rectangular panel about a fifth of the picture's
width, held well clear of both frame edges, with a thin white border. Inside it,
a plainer closer shot of the same drive in the same place it lives: lying in that
same rucksack front pocket beside the same folded cable, shot from a step back so
the whole pocket is in the panel. Same light and same grade as the picture around
it.

No text on any object in either layer."""

# ------------------------------------------------- features.items.3.image ---

P_F3_A = """TYPE: 06-relief-scene v3.7 --none
REGISTER: a candid documentary photograph a passer-by could have taken. Single
frame, natural, unposed, sharp. Nobody aware of a camera.

PRODUCT REFERENCE: use the attached photo as the exact reference. Preserve
shape, proportions, material, finish and colour exactly. Do not redesign or add
features.

A man in his forties is on a sofa between his wife and their daughter, all three
turned toward a television across the room, the daughter half out of her seat
pointing at the screen at something she has just recognised. Not at the camera.
He is upright and leaning in.

His eyes are open and creased at the corners and a small smile has arrived on its
own. His chest is open, his shoulders are rolled back and down, his chin is up.
Nothing is braced and neither hand has gone to the remote.

The drive stands on the low table directly in front of them, close to the camera
in the near part of the frame, a disc seated in its open tray and its face turned
toward the lens so its name can be read. The label carries only the product name
- no other printed text, no back-of-pack panel, no barcode. It is not centred and
not lit for the camera. He is not looking at it and not touching it.

Nothing is drawn onto this photograph. There is no diagram, no inset, no panel
and no glow of any kind.

An ordinary front room: an open DVD case on the table, a throw over the sofa arm,
a lamp on, a plant by the window, curtains drawn back on an evening street.

LIGHT: lamp light and the last of the daylight, kind and even, no rim light, no
glamour lighting.
GRADE: natural colour, light film grain, shallow depth of field. Honest, not
glossy, and not drained.

No printed text on any object in the scene except the product name on the drive.
No logo, no watermark, no arrows, no badges."""

P_F3_B = """TYPE: 06-relief-hero v1.15 --commercial, inset --recall
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the external DVD drive,
identical in every layer. Preserve shape, proportions, material, finish and
colour exactly.

[SUBJECT]
Man in his forties on a sofa with a girl of about eight leaning against his
shoulder, both turned toward a television across the room, his free arm along the
sofa back. Relaxed, gaze away from the product.

[PRODUCT]
The drive on the low table in front of the sofa, front three-quarter angle, close
to the camera and whole and unobstructed, a disc seated in its open tray, one
cable running to a laptop beside it.

[SETTING]
A real front room filled to the edges: an open disc case on the table, a mug, a
throw over the sofa arm, a cushion pushed down the back, a lamp lit in the
corner, a plant on the sill. None of them carries printed words. Background soft,
never blank.

[LIGHT]
Soft even window light with the lamp lit behind, background blurred, high-key.

[LAYOUT]
The sofa sits to the right of the frame; the left side carries the room back to
the window.

In the upper left corner sit two small square cells side by side, together about
a fifth of the picture's width, held well clear of both frame edges, each with a
thin white border. The same man on the same sofa in the same room in both cells,
and the only thing that differs between them is the machine on the table. In the
first cell a thin unbranded plastic drive sits there with its tray half open and
a disc stuck in it, and that whole cell is desaturated to grey while everything
else in the picture keeps its colour. In the second cell the reference drive sits
in the same spot with the disc seated and the television lit. One plain arrow
runs from the first cell to the second and joins those two cells only. Both cells
match the picture around them in resolution, grade and light quality.

No text on any object in any layer."""

P_F3_C = """TYPE: 06-relief-scene v3.7 --none
REGISTER: a candid documentary photograph a passer-by could have taken. Single
frame, natural, unposed, sharp. Nobody aware of a camera.

PRODUCT REFERENCE: use the attached photo as the exact reference. Preserve
shape, proportions, material, finish and colour exactly. Do not redesign or add
features.

A woman in her sixties is at a kitchen table with a laptop open in front of her
and a teenage grandson standing at her shoulder, both watching the screen, the
boy laughing at something on it. Not at the camera. She is upright and leaning
toward the screen.

Her eyes are open and creased at the corners and a small smile has arrived on its
own. Her chest is open, her shoulders are rolled back and down, her chin is up.
Nothing is braced and neither hand has gone to the screen.

The drive stands on the table beside the laptop, close to the camera in the near
part of the frame, a disc seated in its open tray and its face turned toward the
lens so its name can be read. The label carries only the product name - no other
printed text, no back-of-pack panel, no barcode. It is not centred and not lit
for the camera. She is not looking at it and not touching it.

Nothing is drawn onto this photograph. There is no diagram, no inset, no panel
and no glow of any kind.

An ordinary kitchen: a shoebox of loose discs open at the table's end, two mugs,
a tea towel on the oven rail, a window with a garden beyond it.

LIGHT: afternoon daylight from the window, kind and even, no rim light, no
glamour lighting.
GRADE: natural colour, light film grain, shallow depth of field. Honest, not
glossy, and not drained.

No printed text on any object in the scene except the product name on the drive.
No logo, no watermark, no arrows, no badges."""

# ------------------------------------------------- features.items.4.image ---

P_F4_A = """TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the drive in the LAST panel.
Preserve shape, proportions, material, finish and colour exactly.

[SCENE — the same in all three]
The same corner of a home desk, the same dark wood desktop, a closed laptop and
a cold mug pushed to the back. Flat overcast light from a window off to the
left, no strong shadows, no styling.

[FRAMING]
One person photographed this three times from where they always sit, phone level
with the desktop, the bare wood filling the middle third and the laptop
across the upper third. It reads as one shot taken three times, never as three
different shots. Light differs only in exposure, never warmth.

[THE VARIABLE]
What has to sit on a desk to read a disc, move files off a card and keep a mouse
plugged in. Every panel at the same moment: connected, nothing in hand, the same
unbranded silver disc and memory card in all three.
1 — a plain unbranded optical drive alone, one cable, the card beside it
unread; the mug at the back, handle out.
2 — that same drive plus a separate powered hub and a separate card reader,
three bodies and four cables; the mug turned, a pen beside it.
3 — the reference drive alone, one cable, the card in its own slot; the mug gone,
a coaster in its place.

[GRADE — the same in all three]
Neutral, from the overcast window and the drab desktop rather than a filter.
Still colour, never black and white.

Panels one and two get the same exposure, tidiness and framing as panel three;
the alternatives are ordinary products someone would buy, never made to look
worse."""

P_F4_B = """TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the drive in the LAST panel.
Preserve shape, proportions, material, finish and colour exactly.

[SCENE — the same in all three]
The same kitchen table, the same pale scrubbed wood, a chair back at the frame
edge and a folded cloth pushed to the far side. Flat daylight from a window off
to the right, no strong shadows, no styling.

[FRAMING]
One person photographed this three times from where they always sit, phone above
the table looking down, the bare wood filling the middle third and the
chair back across the upper third. It reads as one shot taken three times, never
as three different shots. Light differs only in exposure, never warmth.

[THE VARIABLE]
What has to go into a bag to take disc reading and card transfer elsewhere.
Every panel at the same moment: laid out beside the same open laptop sleeve,
nothing packed yet, the same unbranded silver disc in all three.
1 — a plain unbranded optical drive, cable coiled beside it; the cloth folded
square.
2 — that same drive, a separate powered hub with its own mains lead and a
separate card reader, each cable coiled; the cloth rucked at one corner.
3 — the reference drive, its one cable coiled; the cloth closer, a spoon beside
it.

[GRADE — the same in all three]
Neutral, from the window and the pale table rather than a filter. Still colour,
never black and white.

Panels one and two get the same exposure, tidiness and framing as panel three;
the alternatives are ordinary products someone would buy, never made to look
worse."""

P_F4_C = """TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
The attached photo is the exact reference for the drive in the LAST panel.
Preserve shape, proportions, material, finish and colour exactly.

[SCENE — the same in all three]
The same living-room shelf, the same veneered board, a row of unmarked disc
spines and a small plant at one end. Flat room light from a window off to the
left, no strong shadows, no styling.

[FRAMING]
One person photographed this three times from where they always stand, phone
level with the shelf, the board filling the middle third and the spines across
the upper third. It reads as one shot taken three times, never as
three different shots. Light differs only in exposure, never warmth.

[THE VARIABLE]
What has to live beside a television to play discs and read a camera card. Every
panel at the same moment: in place and connected, nothing handled, the same
unbranded silver disc and memory card in all three.
1 — a plain unbranded optical drive, one cable off the shelf, the card propped
against it; the plant at the left end, leaves upright.
2 — that same drive, a separate powered hub and a card reader, three bodies
with four cables; the plant turned, a leaf over the board.
3 — the reference drive alone, one cable, the card in its slot; the plant gone,
a coaster in its place.

[GRADE — the same in all three]
Neutral, from the room light and the veneered board rather than a filter. Still
colour, never black and white.

Panels one and two get the same exposure, tidiness and framing as panel three;
the alternatives are ordinary products someone would buy, never made to look
worse."""


def snap(mode, scene, anchor, camera, crop):
    """05-social-snapshot prompt. PARTS order follows the type's call-map."""
    return f"""TYPE: 05-social-snapshot v1.2

Use the attached product photo as the exact reference for the external DVD
drive. Preserve shape, proportions, material, finish and colour exactly. {crop}

CONTENT MODE, {mode}

ANCHOR: {anchor}

SCENE: {scene}

CAMERA TRUTH: {camera} No styling of any kind.

REGISTER: a real customer's phone photo. One frame, no layout, no layers.
STYLE: honest phone photography, unedited look, natural, slightly imperfect."""


# reviews.shots — SET DIVERSITY LAW: four completely different rooms, surfaces,
# light temperatures, camera distances and content modes.
P_R0_A = snap(
    "in-use: the drive is mid-read on a desk, its tray closed on a disc and its "
    "status light lit, one forearm resting on the desk beside it in a rolled shirt "
    "cuff and no face in the frame.",
    "a home-office desk photographed as found - a coffee ring dried on the wood, a "
    "cable snaking off the back edge, a radiator half in shot at the frame edge. "
    "Warm dim light from a single desk lamp, the room behind it going dark.",
    "a coiled phone charger pushed to one side.",
    "framing tilted a few degrees and a little too close, focus adequate, mild "
    "noise, honest exposure.",
    "It sits flat on the desk, seen from above and slightly to one side, cropped "
    "the way a casual one-handed photo crops.")

P_R0_B = snap(
    "at-rest: the drive simply sitting where it now lives on the desk, its tray "
    "closed and nothing plugged into it, a factory protective film still part-peeled "
    "from one corner of the lid.",
    "a home-office desk photographed as found - a coffee ring dried on the wood, a "
    "cable snaking off the back edge, a radiator half in shot at the frame edge. "
    "Warm dim light from a single desk lamp, the room behind it going dark.",
    "a coiled phone charger pushed to one side.",
    "framing tilted a few degrees and a little too close, focus adequate, mild "
    "noise, honest exposure.",
    "It sits flat on the desk, seen from above and slightly to one side, cropped "
    "the way a casual one-handed photo crops.")

P_R0_C = snap(
    "in-use: the drive is mid-read on a desk, its tray closed on a disc and its "
    "status light lit, one forearm resting on the desk beside it in a rolled shirt "
    "cuff and no face in the frame.",
    "a bedroom windowsill desk photographed as found - a dusty sill, a mug ring, a "
    "curtain hem hanging into the frame. Cold blue-grey daylight from an overcast "
    "window right beside it.",
    "a pair of earphones tangled at the sill's edge.",
    "framing off-centre and a little far back, focus adequate, mild motion "
    "softness, honest exposure.",
    "It sits flat on the sill, seen almost straight on from the side, cropped the "
    "way a casual one-handed photo crops.")

P_R1_A = snap(
    "kit-flatlay: the opened box contents as the owner keeps them, slightly "
    "disordered - the drive, its two cables loosely coiled, and a small folded "
    "leaflet, laid out on the table with the empty box lid pushed to one side.",
    "a kitchen table photographed as found - crumbs at one edge, a faint water mark "
    "on the wood, a chair back blurred at the frame edge. Flat overhead kitchen "
    "light, slightly green.",
    "a mug of cold tea at the corner of the table.",
    "framing off-centre and shot from directly above at arm's length, focus "
    "adequate, honest exposure.",
    "It lies flat among the other contents, seen from above, cropped the way a "
    "casual one-handed photo crops.")

P_R1_B = snap(
    "at-rest: the drive sitting on the table where it was set down after unboxing, "
    "its tray closed, a factory sticker still on the underside edge with its print "
    "too small to read.",
    "a kitchen table photographed as found - crumbs at one edge, a faint water mark "
    "on the wood, a chair back blurred at the frame edge. Flat overhead kitchen "
    "light, slightly green.",
    "a mug of cold tea at the corner of the table.",
    "framing off-centre and shot from directly above at arm's length, focus "
    "adequate, honest exposure.",
    "It sits flat on the table, seen from above, cropped the way a casual "
    "one-handed photo crops.")

P_R1_C = snap(
    "kit-flatlay: the opened box contents as the owner keeps them, slightly "
    "disordered - the drive, its two cables loosely coiled, and a small folded "
    "leaflet, laid out on a carpet with the empty box lid pushed to one side.",
    "a living-room carpet photographed as found - a flattened patch of pile, a stray "
    "thread, the foot of an armchair at the frame edge. Warm yellow light from a "
    "standard lamp overhead.",
    "a television remote lying beside the pile.",
    "framing tilted and shot from standing height looking down, focus adequate, "
    "mild noise, honest exposure.",
    "It lies flat among the other contents, seen from above and at an angle, "
    "cropped the way a casual one-handed photo crops.")

P_R2_A = snap(
    "in-use: the drive is connected on a living-room floor beside a laptop, a "
    "memory card seated in its slot and its status light lit, two fingers just "
    "leaving the card and no face in the frame.",
    "a living-room floor photographed as found - a rug edge rucked up, a scatter of "
    "toy pieces pushed aside, a sofa foot at the frame edge. Mixed light, warm lamp "
    "on one side and cold daylight from a window on the other.",
    "an open disc case lying face down on the rug.",
    "framing tilted and very close, kneeling height, focus adequate, mild motion "
    "softness, honest exposure.",
    "It sits flat on the rug, seen from a low angle almost level with the floor, "
    "cropped the way a casual one-handed photo crops.")

P_R2_B = snap(
    "at-rest: the drive sitting on the rug where it was left after use, its tray "
    "shut and one cable still trailing from it toward a laptop out of frame.",
    "a living-room floor photographed as found - a rug edge rucked up, a scatter of "
    "toy pieces pushed aside, a sofa foot at the frame edge. Mixed light, warm lamp "
    "on one side and cold daylight from a window on the other.",
    "an open disc case lying face down on the rug.",
    "framing tilted and very close, kneeling height, focus adequate, mild motion "
    "softness, honest exposure.",
    "It sits flat on the rug, seen from a low angle almost level with the floor, "
    "cropped the way a casual one-handed photo crops.")

P_R2_C = snap(
    "in-use: the drive is connected on a garage workbench beside a laptop, a memory "
    "card seated in its slot and its status light lit, two fingers just leaving the "
    "card and no face in the frame.",
    "a garage workbench photographed as found - sawdust in the grain, a paint mark, "
    "a vice bolted at the frame edge. Cold strip light from a fluorescent tube "
    "overhead.",
    "a screwdriver lying across the bench behind it.",
    "framing off-centre and close, standing height looking down, focus adequate, "
    "mild noise, honest exposure.",
    "It sits flat on the bench, seen from above and slightly to one side, cropped "
    "the way a casual one-handed photo crops.")

P_R3_A = snap(
    "at-rest: the drive sitting on a shelf where it now lives beside a short row of "
    "disc spines, its tray shut, one cable dropping away behind the shelf board.",
    "a living-room shelf photographed as found - a dust line along the board, a "
    "photo frame turned slightly out of square, wallpaper seam visible behind. Cool "
    "daylight from a window across the room, falling off toward the shelf's far end.",
    "a set of keys dropped on the board beside it.",
    "framing a little far back and slightly low, focus adequate, honest exposure.",
    "It stands on the shelf, seen almost straight on from the front, cropped the "
    "way a casual one-handed photo crops.")

P_R3_B = snap(
    "in-use: the drive is mid-read on the shelf, its tray closed on a disc and its "
    "status light lit, one hand just withdrawing from it at the frame edge and no "
    "face in the frame.",
    "a living-room shelf photographed as found - a dust line along the board, a "
    "photo frame turned slightly out of square, wallpaper seam visible behind. Cool "
    "daylight from a window across the room, falling off toward the shelf's far end.",
    "a set of keys dropped on the board beside it.",
    "framing a little far back and slightly low, focus adequate, honest exposure.",
    "It stands on the shelf, seen almost straight on from the front, cropped the "
    "way a casual one-handed photo crops.")

P_R3_C = snap(
    "at-rest: the drive sitting on a hallway table where it now lives beside a "
    "folded laptop sleeve, its tray shut and nothing plugged into it.",
    "a hallway table photographed as found - a scuff on the paintwork behind, a "
    "shoe half in frame on the floor below, a coat sleeve hanging into the top of "
    "the picture. Dim warm light from a single hallway bulb.",
    "an unopened envelope-shaped blank card propped against the wall behind it.",
    "framing tilted and shot quickly from above at arm's length, focus adequate, "
    "mild motion softness, honest exposure.",
    "It sits flat on the table, seen from above and at an angle, cropped the way a "
    "casual one-handed photo crops.")

# ---------------------------------------------------------------- assembly ---

GAP_ATTACH = (
    "The reference photo is yours to upload, and 27 prompts want it. The export "
    "carries imageBriefs: null and sourceRefs.shopifyProductGid: null, so there "
    "is no product photograph in it and nothing to hash - attachments is omitted "
    "from every option rather than filled with an invented sha256 (SPEC 6.4). "
    "That is a gap in the EXPORT, not a blocked prompt: each of those 27 keeps "
    "its G1 reference block and reads 'the attached photo', so pasting the "
    "prompt and uploading the drive photo in the generation tool runs it as "
    "written. The remaining 9 options and both brief plates bind nothing at all. "
    "Read the requirement off the EXECUTION rather than the type: "
    "02-cause-anatomy --diagnostic drops [PRODUCT REFERENCE] and "
    "04-proof-lockedframe --rivals is Step 5's named exception, so four prompts "
    "here need no photo despite their type flag reading true.")


def opt(o, varies, typ, ver, ratio, prompt, rationale, variant=None, axes=None,
        pipeline="single-pass", notes=None, avoid=None, asset=None, steps=None):
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
    if steps:
        d["steps"] = steps
    return d


AV_PAIN = ("badges, arrows, drawn overlays, insets of any kind, red glow, pain "
           "hotspots, graphic overlay, split panel, white background, studio "
           "lighting, stock photo look, posed model, fake grimace, smiling, "
           "clean staged interior, saturated colors, advertising composition, "
           "product placement")
AV_CAUSE = ("photographic elements, 3D render, photorealistic skin, human face, "
            "gore, correct side on the left, both dashed lines identical, missing "
            "badge on either panel, different figure scale between panels, extra "
            "signal colours, saturated ground, background pattern, reference "
            "product in frame, branded remedy object")
AV_XRAY = ("photographic background, environment, people, hands, spec labels, "
           "capacity text, callout lines with text, opaque shell, internals "
           "floating outside the product, invented components, exploded parts "
           "view, rainbow palette, bright white background, cartoon style")
AV_LOCKED = ("badges, arrows, glows, checkmarks, one panel brighter, inconsistent "
             "lighting between panels, studio background, clean styled set, staged "
             "perfection, saturated colors, red or green cues, motion blur, people, "
             "hands, brand logos, recognizable trademarks, identical framing "
             "between panels, pixel-perfect alignment, tripod shot, CGI, last panel "
             "brighter or cleaner than the others, alternatives made to look broken")
AV_HERO = ("cluttered background, dark moody lighting, pain cues in main scene, "
           "blurry product, inconsistent product between layers, same angle "
           "repeated, fabricated colorways, mixed illustration and photo inside one "
           "inset half, invented spray or mist, fake steam")
AV_SCENE = ("badges, arrows, drawn overlays, insets of any kind, looking at camera, "
            "posing, a situation that costs nothing, a guarded body, golden hour, "
            "warm flattering light, glamour lighting, aspirational travel location, "
            "product presented to camera, product turned away so its face cannot be "
            "read, back-of-pack label, barcode, bar chart, arrowheads, translucent "
            "marks, blank expression, collapsed posture, drained joyless grade, "
            "stock photo look")
AV_SNAP = ("studio lighting, softbox reflections, seamless background, negative "
           "space, color grading, professional composition, styled props, badges, "
           "borders, star ratings, reviewer names, avatars, text overlays, product "
           "render look, perfect symmetry, magazine polish, influencer aesthetic")

FENCE = ("BLOCKED AS THE PAGE IS BUILT. 05-social-snapshot's authenticity fence is "
         "hard and non-negotiable: no reviewer name, avatar, star row or verified "
         "label anywhere near the image in the layout. reviews.shots.0-3 sit inside "
         "the same section element as reviews.quotes.0-2, which carry names "
         "(Martin K., Gillian R., Derek S.) and a 'Verified Purchase' label each. "
         "Rendering these four beside that copy presents generated pictures as "
         "customer uploads, which is a fabricated endorsement. Either move the "
         "shots out of the attributed block, or drop the names and verified labels "
         "from that block, or use real customer photographs - which always win over "
         "generated ones.")

SNAP_SET = ("SET DIVERSITY LAW: the four A options are deliberately four different "
            "rooms, surfaces, light temperatures, camera distances and content "
            "modes. Generate them as independent prompts, never as a batch with "
            "shared seeds or shared scene text.")

SLOTS = [
    {
        "slot_id": "hero.image", "section_role": "hero",
        "asset": "58-01-hero-pain-scene.png",
        "placement": "Advertorial header, directly under the headline and byline.",
        "gif": {"eligible": False, "form": "none",
                "reason": "The slot exists to make a cold reader recognise "
                          "themselves in a held state. Nothing about it is "
                          "temporal - no transition, no sequence, no output "
                          "flowing - so it does not earn motion."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT decides it. 01-pain-scene's use_when names this beat in its own "
            "words - 'advertorial header image, cold traffic that does not know the "
            "product yet' - and --candid is the branch for 'physical limitation and "
            "moments nobody would choose to be seen in', which is a man checking a "
            "disc he cannot play. PAGE LEGALITY: the type is G1-exempt, so A is one "
            "of only two prompts on this page that runs without the missing product "
            "photo. EVIDENCE: --candid carries this type's owner-passed worked "
            "example and the type passed at 1.14. PRODUCT PRESENCE: none required "
            "and none allowed here. PROMPT RISK: 1,5k characters against a type "
            "whose measured history runs 1669-1880, and every clause in it is one "
            "the type's own PARTS require. B is legal and would win if the beat "
            "were self-image rather than physical limitation; C moves the same "
            "argument onto degradation, which the copy raises but does not lead on.",
        "options": [
            opt("A", "baseline", "01-pain-scene", "1.14", "16:9", P_HERO_A,
                "The disc-in-hands force is diagnostic: nobody turns a disc to the "
                "light unless they cannot play it. Evidence is rank 1 - the "
                "laptop's unbroken edge with no slot, and the box of cases - so the "
                "symptom is a physical fact rather than an expression.",
                variant="candid", axes={"gaze": "candid"}, avoid=AV_PAIN,
                notes="G1-exempt: runs today without the missing product photo.",
                asset="58-01-hero-pain-scene.png"),
            opt("B", "axis: gaze candid -> confront", "01-pain-scene", "1.14",
                "16:9", P_HERO_B,
                "The same beat played as daily frustration rather than physical "
                "limitation, with the disc stopped dead against a closed edge. "
                "--confront is legible at thumbnail size, which suits a header that "
                "may run as a paid-social crop.",
                variant="confront", axes={"gaze": "confront"}, avoid=AV_PAIN,
                notes="No second type survives the hero cell on advertorial, so B "
                      "varies on the axis per runbook Step 4. Also G1-exempt.",
                asset="58-01-hero-pain-scene-b.png"),
            opt("C", "execution: subject, place and evidence rank", "01-pain-scene",
                "1.14", "16:9", P_HERO_C,
                "Same type and axes as A, different execution: an older subject, a "
                "storage room, and the evidence moved to the discs themselves "
                "degrading. It argues the clock the copy mentions - 'the discs are "
                "slowly degrading while nothing is done' - which A leaves untouched.",
                variant="candid", axes={"gaze": "candid"}, avoid=AV_PAIN,
                notes="G1-exempt. Pairs less tightly with the first-person male "
                      "byline than A or B.",
                asset="58-01-hero-pain-scene-c.png"),
        ],
    },
    {
        "slot_id": "problems.items.0.image", "section_role": "problem-agitation",
        "asset": "58-02-problems0-pain-scene-object.png",
        "placement": "Beside 'The painful loop of cheap drives and missing ports'.",
        "gif": {"eligible": False, "form": "none",
                "reason": "A still life of what was already tried. It is a state "
                          "the reader inspects, not a process, so nothing in it "
                          "changes over time."},
        "recommended_opt": "A",
        "recommendation_basis":
            "PAGE LEGALITY decides it over FIT. B is the better literal fit - "
            "04-proof-lockedframe's use_when names 'the I tried three things beat' "
            "outright, and the copy's own note label is 'What I tried first'. But "
            "that type appears once per page and features.items.4 needs it more: "
            "its use_when also requires a buyer who 'already understands the "
            "problem and mechanism', which is false this early and true by the time "
            "the cost comparison runs. So A takes rung 4 of the runbook's ladder - "
            "another execution of a type already on the page, differing on a named "
            "dimension, here subject class - which is the precedent the runbook "
            "records for object-only pain scenes. EVIDENCE: object-only execution "
            "is recorded twice in the ledger. PRODUCT PRESENCE: none, correctly - "
            "the product has not been revealed yet. PROMPT RISK: A is G1-exempt and "
            "runnable today; B is too, but costs the page its proof image.",
        "options": [
            opt("A", "execution: subject class person -> object-only",
                "01-pain-scene", "1.14", "16:9", P_PROB0_A,
                "The dongle nest IS the symptom the copy describes, and it is an "
                "object fault, so the frame drops the person entirely. Evidence is "
                "rank 3, the failed tool in the state that shows it failed: a tray "
                "jammed half open with the disc still in it.",
                variant="candid", axes={"gaze": "candid"}, avoid=AV_PAIN,
                notes="Rung 4 of the runbook ladder. Named dimension vs hero.image: "
                      "subject class. G1-exempt.",
                asset="58-02-problems0-pain-scene-object.png"),
            opt("B", "type: 01-pain-scene -> 04-proof-lockedframe",
                "04-proof-lockedframe", "1.13", "16:9", P_PROB0_B,
                "Three panels, three things the reader has already tried, none of "
                "them winning - which is exactly the copy's three notes. --rivals "
                "carries no product, so it needs no reference photo either.",
                variant="rivals", axes={"camera_lock": "handheld",
                                        "context_mode": "natural-use"},
                avoid=AV_LOCKED,
                notes="PICKING B FORCES features.items.4 TO CHANGE - one type once "
                      "per page, and variants do not lift it. features.4 would fall "
                      "to a second 06-relief-hero execution. Type note at 1.13: "
                      "--rivals is never sent for the library's own render tests "
                      "because there is no product to judge; that is a testing rule, "
                      "not a page rule.",
                asset="58-02-problems0-lockedframe-rivals.png"),
            opt("C", "execution: place, light and evidence rank", "01-pain-scene",
                "1.14", "16:9", P_PROB0_C,
                "Same type and object-only execution as A, moved off the desk onto "
                "a worktop and lit hard rather than low, with the evidence shifted "
                "to the cracked casing and the scratched disc - the failure the copy "
                "calls 'ran hot and failed to read our irreplaceable recordings'.",
                variant="candid", axes={"gaze": "candid"}, avoid=AV_PAIN,
                notes="G1-exempt. Shares its named dimension with A, so it is a "
                      "true execution variant rather than a second route.",
                asset="58-02-problems0-pain-scene-object-c.png"),
        ],
    },
    {
        "slot_id": "problems.items.1.image", "section_role": "cause",
        "asset": "58-03-problems1-cause-anatomy.png",
        "placement": "Beside 'Why standard external drives constantly fail'.",
        "gif": {"eligible": True, "form": "whole-frame", "kind": "cause",
                "duration_s": 3, "loop": "seamless loop",
                "shot": "both panels, held as drawn",
                "action": "left lens drifts off track",
                "result": "right lens holds the track",
                "match": "flat vector, same two grounds",
                "delivery": "mp4/webm, under 2 MB",
                "reason":
                    "The cause this slot exists to indict IS temporal - a motor "
                    "spins, the sled shakes, the beam drifts off the track. The "
                    "still can only show the endpoint of that. 02-cause-anatomy "
                    "legislates no motion layer of its own, so the form is "
                    "whole-frame and the kind is the type's own job, cause."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT and PAGE LEGALITY agree. The copy names one mechanism - 'unbalanced "
            "internal motors shake the optical core, the laser drifts off track' - "
            "and 02-cause-anatomy exists to indict exactly that with a measured "
            "pair. It passes the removal test outright: take the unbalanced spindle "
            "out of the left panel and the read error goes with it, so this is a "
            "switchable state and not accumulated damage. --diagnostic is the "
            "variant for the advertorial middle where the culprit is named before "
            "the product is revealed, and features.items.0 downstream carries the "
            "product, which is the condition the variant sets. EVIDENCE: 30 renders "
            "behind measure, 18 behind verdict, and the two-mark budget is the "
            "type's proven configuration. PRODUCT PRESENCE: correctly absent, and "
            "that makes A G1-exempt and runnable today. PROMPT RISK: the offset "
            "difference is far past the 2:1 admission floor. B indicts the second "
            "cause the copy names and is the one to run if A's subject class "
            "struggles; C stays on vibration but moves the landmark to the platter.",
        "options": [
            opt("A", "baseline", "02-cause-anatomy", "1.15", "16:9", P_PROB1_A,
                "The measured pair is beam-to-track offset: wide on the bare "
                "spindle, closed to nothing in the damping carriage. Both lines "
                "anchor to the same two landmarks and only the offset differs, "
                "which is the type's one-property rule.",
                variant="diagnostic", avoid=AV_CAUSE,
                notes="FIRST NON-BIOLOGICAL body on this type - every rendered "
                      "subject class so far has been anatomical (tooth, hair shaft, "
                      "muscle, kneecap). The device is a 2D cross-section and the "
                      "avoid_when only requires internal structure to draw, which a "
                      "disc, track and lens have. Untested; watch the first render "
                      "for the structures reading as a recognisable assembly. "
                      "G1-exempt.",
                asset="58-03-problems1-cause-anatomy.png"),
            opt("B", "execution: which cause is indicted", "02-cause-anatomy",
                "1.15", "16:9", P_PROB1_B,
                "The copy names two causes and this is the second: 'thin laptops cut "
                "off power delivery when a drive shares bandwidth'. The measured "
                "pair becomes rail width at the port, pinched under a dongle chain "
                "and full under one powered hub.",
                variant="diagnostic", avoid=AV_CAUSE,
                notes="Also non-biological, and airbrushed rather than flat-vector "
                      "so the two are not one look. Removal test passes: unplug the "
                      "chain and the starvation goes. G1-exempt.",
                asset="58-03-problems1-cause-anatomy-b.png"),
            opt("C", "execution: landmark pair and style", "02-cause-anatomy",
                "1.15", "16:9", P_PROB1_C,
                "Same cause as A, but the measurement moves off the beam onto the "
                "platter's tilt over its collar - a landmark pair that is easier to "
                "draw unambiguously than a beam, if A's optical section reads muddy.",
                variant="diagnostic", avoid=AV_CAUSE,
                notes="Front view rather than side, so it does not repeat A's "
                      "composition. G1-exempt.",
                asset="58-03-problems1-cause-anatomy-c.png"),
        ],
    },
    {
        "slot_id": "features.items.0.image", "section_role": "mechanism",
        "asset": "58-04-features0-xray.png",
        "placement": "Beside 'Anti-shock optical core stops laser vibration'.",
        "gif": {"eligible": True, "form": "whole-frame", "kind": "mechanism",
                "duration_s": 3, "loop": "seamless loop",
                "shot": "the render, held as built",
                "action": "sled tracks, beam stays centred",
                "result": "beam never leaves the disc",
                "match": "same charcoal ground, same cyan",
                "delivery": "mp4/webm, under 2 MB",
                "reason":
                    "The mechanism is a travelling one - the sled runs its carriage "
                    "while the disc turns - and a still can only assert that. "
                    "03-mechanism-xray legislates no motion layer, so the form is "
                    "whole-frame and the kind is the type's own job, mechanism."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT is decisive and the gate makes it the only mechanism type "
            "available. body_contact is false for an external drive, which drops "
            "03-mechanism-ghostbody by the slot-rules attribute gate, and "
            "03-spec-split and 03-spec-explode are not advertorial types. That "
            "leaves xray, which is also exactly right: the section argues from an "
            "internal component the buyer cannot see, and xray exists to show real "
            "internals through a translucent shell. A is the top-down view because "
            "the carriage's length is the argument and it reads longest from above. "
            "EVIDENCE: type passed at 1.3 on two owner-passed worked examples; "
            "working carries 1 render. PRODUCT PRESENCE: the product IS the frame. "
            "PROMPT RISK: G1 binds the silhouette hard here and there is no "
            "reference photo yet, so this option cannot run until one is supplied. "
            "One mark only - the type's own rule is not to invent an emission, and "
            "this drive emits nothing outward, so output and caught are both absent.",
        "options": [
            opt("A", "baseline", "03-mechanism-xray", "1.3", "16:9", P_F0_A,
                "Top-down through the lid: the damping carriage runs the length of "
                "the bay so its travel is legible, and the beam standing up onto the "
                "disc is the one thing the section exists to show.",
                avoid=AV_XRAY,
                notes="Needs the product photo. Only working is used - the drive "
                      "emits nothing visible outward, and G8 forbids inventing an "
                      "effect so a render looks alive.",
                asset="58-04-features0-xray.png"),
            opt("B", "execution: viewpoint and internals named",
                "03-mechanism-xray", "1.3", "16:9", P_F0_B,
                "End-on from the front edge, which brings the rear port bank into "
                "the same section as the optical core. It answers this section and "
                "sets up the next one in a single frame.",
                avoid=AV_XRAY,
                notes="Needs the product photo. Ground moves to pale warm grey so "
                      "it is not one look with A.",
                asset="58-04-features0-xray-b.png"),
            opt("C", "execution: orientation and ground", "03-mechanism-xray",
                "1.3", "16:9", P_F0_C,
                "Standing on edge at a low three-quarter, which shows the drive's "
                "thinness at the same time as its internals - useful if the page "
                "wants the slim claim carried twice.",
                avoid=AV_XRAY,
                notes="Needs the product photo. A vertical subject in a 16:9 frame "
                      "leaves side space; the plain ground absorbs it.",
                asset="58-04-features0-xray-c.png"),
        ],
    },
    {
        "slot_id": "features.items.1.image", "section_role": "spec",
        "asset": "58-05-features1-relief-hero-detail.png",
        "placement": "Beside 'Built-in hub restores laptop connectivity'.",
        "gif": {"eligible": False, "form": "none",
                "reason": "The argument is a count of ports with things in them - a "
                          "held state a reader inspects. Nothing flows and nothing "
                          "changes, so the inset layer that --detail legislates has "
                          "no temporal content to host a loop."},
        "recommended_opt": "A",
        "recommendation_basis":
            "This slot has no cell of its own and the ladder decides it. The "
            "mechanism cell is spent at features.items.0, 03-spec-explode and "
            "03-spec-split are not advertorial, and 03-use-sequence - which the copy "
            "would otherwise suit - declares only 3:4 and 1:1, so it cannot serve a "
            "16:9 slot at all. Rung 2 of the ladder moves to an adjacent step and "
            "06-relief-hero carries it: the section's real argument is the after "
            "state of a desk, and --detail is the sanctioned way to magnify a "
            "feature too small to read at scene scale, which a port bank is. FIT: "
            "use_when names gallery images 2-3 and landing-page banners. EVIDENCE: "
            "the type is at 1.15 with 12 renders behind its marks, though --detail "
            "as a still inset is thinner than --recall. PRODUCT PRESENCE: the "
            "product is the desk's centre and every port is occupied, which is the "
            "claim. PROMPT RISK: needs the reference photo, and G1 binds it "
            "identically in both layers.",
        "options": [
            opt("A", "baseline", "06-relief-hero", "1.15", "16:9", P_F1_A,
                "Every port on the drive is occupied while the laptop keeps one lead "
                "and nothing else - the copy's claim made visible as a count rather "
                "than asserted. The inset magnifies the port bank, which is the one "
                "thing a desk-scale shot cannot resolve.",
                axes={"register": "commercial", "inset_mode": "detail",
                      "inset_motion": "still"},
                avoid=AV_HERO,
                notes="Needs the product photo, in both layers identically. The "
                      "inset occupies the space the subject is offset from, per the "
                      "type's offset rule - no second reservation mid-frame.",
                asset="58-05-features1-relief-hero-detail.png"),
            opt("B", "axis: register commercial -> ugc", "06-relief-hero", "1.15",
                "16:9", P_F1_B,
                "The same argument shot as a phone photo. An advertorial header "
                "register carries into the body well, and ugc buys trust where a "
                "clean desk can read as an advert.",
                axes={"register": "ugc", "inset_mode": "detail",
                      "inset_motion": "still"},
                avoid=AV_HERO + ", professional lighting, studio setup, clean "
                                "composition, styled interior, negative space, "
                                "retouched skin, magazine look, glossy",
                notes="Needs the product photo. A crisp inset does not break the ugc "
                      "register - that is settled on this type at 1.15.",
                asset="58-05-features1-relief-hero-detail-ugc.png"),
            opt("C", "execution: subject full person -> reduced", "06-relief-hero",
                "1.15", "16:9", P_F1_C,
                "Hands only, with the card going into the slot. reduced is chosen "
                "when the result is more legible than the user, and here the result "
                "is a row of occupied ports.",
                axes={"register": "commercial", "inset_mode": "detail",
                      "inset_motion": "still"},
                avoid=AV_HERO,
                notes="Needs the product photo. reduced requires naming what makes "
                      "finished look different from unfinished, which this prompt "
                      "does in its own block.",
                asset="58-05-features1-relief-hero-detail-reduced.png"),
        ],
    },
    {
        "slot_id": "features.items.2.image", "section_role": "spec",
        "asset": "58-06-features2-relief-hero-context.png",
        "placement": "Beside 'Rugged slim design built for cool operation'.",
        "gif": {"eligible": False, "form": "none",
                "reason": "Portability is a property, not an event. The section's "
                          "other claim, staying cool across a weekend, is invisible "
                          "in any register - a loop of a drive not overheating shows "
                          "nothing - so motion would add duration without argument."},
        "recommended_opt": "A",
        "recommendation_basis":
            "Rung 4: a second execution of a type already on the page, differing on "
            "named dimensions - inset_mode, subject, place and pose all change from "
            "features.items.1. Nothing else is available. FIT: --context is defined "
            "as the mode for when the hero shows the product in hand and the buyer "
            "still needs to see where it lives, which is precisely a slim drive "
            "going into a sleeve. HONEST LIMIT, and it is the reason this basis is "
            "hedged: the section's headline claim is thermal, and no photograph can "
            "show a casing staying cool. A argues the half that is photographable - "
            "the slim body against a closed laptop's edge - and the thermal claim is "
            "left to the copy. PRODUCT PRESENCE: the drive is held at the mouth of "
            "the sleeve, its thickness the subject. PROMPT RISK: needs the reference "
            "photo in both layers; G7-X binds one mode of use across hero and inset, "
            "which both A and C hold.",
        "options": [
            opt("A", "execution: inset_mode detail -> context, and subject",
                "06-relief-hero", "1.15", "16:9", P_F2_A,
                "The drive measured against a closed laptop's edge is the slim claim "
                "made checkable, and the inset shows the same drive zipped in the "
                "same sleeve - the place it actually lives.",
                axes={"register": "commercial", "inset_mode": "context",
                      "inset_motion": "still"},
                avoid=AV_HERO,
                notes="Needs the product photo. Named dimension vs features.items.1: "
                      "inset_mode, plus subject, place and pose. G7-X holds - "
                      "handheld in both layers.",
                asset="58-06-features2-relief-hero-context.png"),
            opt("B", "axis: inset_mode context -> none", "06-relief-hero", "1.15",
                "16:9", P_F2_B,
                "No layer at all, and the argument moves to the long session the "
                "copy describes: a man mid-stretch at the end of it, a stack of "
                "burned discs beside the drive. It is the closest a photograph gets "
                "to the thermal claim without faking it.",
                axes={"register": "commercial", "inset_mode": "none",
                      "inset_motion": "still"},
                avoid=AV_HERO,
                notes="Needs the product photo. Simplest option on the page and the "
                      "one to pick if the two-layer builds come back with the inset "
                      "cut by a frame edge, which is this type's open geometry fault.",
                asset="58-06-features2-relief-hero-none.png"),
            opt("C", "execution: subject reduced, place and inset content",
                "06-relief-hero", "1.15", "16:9", P_F2_C,
                "Hands lifting the drive clear of a rucksack pocket, with the inset "
                "showing it stowed in that same pocket. Portability argued by where "
                "it has just come from rather than by a size comparison.",
                axes={"register": "commercial", "inset_mode": "context",
                      "inset_motion": "still"},
                avoid=AV_HERO,
                notes="Needs the product photo. Shares inset_mode with A, so it is "
                      "an execution variant; keep only one of A and C on the page.",
                asset="58-06-features2-relief-hero-context-c.png"),
        ],
    },
    {
        "slot_id": "features.items.3.image", "section_role": "outcome",
        "asset": "58-07-features3-relief-scene.png",
        "placement": "Beside 'Our family memories restored in one evening'.",
        "gif": {"eligible": False, "form": "none",
                "reason": "The slot's reason to exist is an after-state - a family "
                          "who can watch the disc - and a held state is what it has "
                          "to prove. 06-relief-scene also bans every layer except "
                          "the --detail inset, so there is no legislated layer a "
                          "loop could occupy without breaking the register."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT is unusually literal. 06-relief-scene's use_when asks for a closing "
            "image where the promise is a state of living rather than a feature, and "
            "the section is titled 'Our family memories restored in one evening'. "
            "PAGE LEGALITY: the type requires 01-pain-scene on the same page and it "
            "is there twice, so requires_pair is satisfied; the arc holds because "
            "every pain image sits above this one. The result_visibility gate does "
            "not drop it - the restored state is visible as a family watching a "
            "screen. EVIDENCE is where this recommendation is weak and the basis "
            "says so: the type is at 3.7 with 32 render records and zero passes at "
            "any 3.x version, and 3.7's product law - the label carrying the name "
            "and nothing else - was written yesterday and has never rendered. B is "
            "the safer type by evidence and the worse fit by argument. PRODUCT "
            "PRESENCE: 3.7 requires the drive to stand in frame as its own object "
            "with its face readable, which A does on the low table. PROMPT RISK: "
            "highest on the page.",
        "options": [
            opt("A", "baseline", "06-relief-scene", "3.7", "16:9", P_F3_A,
                "The situation costs something - three people gathered for something "
                "that could not be played before - and the product stands in frame "
                "as its own object with its face to the lens, which is 3.7's product "
                "law.",
                axes={"gaze": "candid", "inset_mode": "none"},
                avoid=AV_SCENE,
                notes="Needs the product photo. The type has 0 passes at any 3.x, "
                      "and this prompt is the first test of 3.7's name-only label "
                      "clause. Expect to iterate.",
                asset="58-07-features3-relief-scene.png"),
            opt("B", "type: 06-relief-scene -> 06-relief-hero",
                "06-relief-hero", "1.15", "16:9", P_F3_B,
                "The same outcome on the better-evidenced type. --recall holds one "
                "reminder of the problem beside the resolved state, and the pair "
                "changes only the machine on the table - which is the type's own 2/2 "
                "rule for a recall pair.",
                axes={"register": "commercial", "inset_mode": "recall",
                      "inset_motion": "still"},
                avoid=AV_HERO + ", unlabelled before-state inset, low resolution "
                                "inset, inset darker than hero, more than one arrow, "
                                "arrow pointing from now to past",
                notes="Needs the product photo. PICKING B FORCES features.items.1 "
                      "AND features.items.2 TO CHANGE - three 06-relief-hero "
                      "executions on one linear funnel is past what rung 4 permits. "
                      "Also puts a pain cue below the page's first relief image, "
                      "which the arc rule allows only because it is inside an inset.",
                asset="58-07-features3-relief-hero-recall.png"),
            opt("C", "execution: subject, generation and place", "06-relief-scene",
                "3.7", "16:9", P_F3_C,
                "The same argument one generation up - a grandmother and a teenager "
                "at a kitchen table - which widens the persona the brief describes "
                "beyond the byline's own family.",
                axes={"gaze": "candid", "inset_mode": "none"},
                avoid=AV_SCENE,
                notes="Needs the product photo. Same type risk as A.",
                asset="58-07-features3-relief-scene-c.png"),
        ],
    },
    {
        "slot_id": "features.items.4.image", "section_role": "comparison",
        "asset": "58-08-features4-lockedframe-verdict.png",
        "placement": "Beside 'Replaces three separate purchases for less'.",
        "gif": {"eligible": False, "form": "none",
                "reason": "A locked-frame comparison is inspected, not watched - the "
                          "reader's eye does the travelling between panels. Motion "
                          "here would also break the judgement rule by drawing the "
                          "eye to one panel."},
        "recommended_opt": "A",
        "recommendation_basis":
            "FIT and EVIDENCE agree, and this is where the page's one "
            "04-proof-lockedframe is best spent. use_when wants a buyer who already "
            "understands the problem and the mechanism and now wants to see for "
            "themselves - true here and false at problems.items.0, which is why the "
            "type lands in this slot and not that one. --verdict is the variant with "
            "the product in the last panel, and the copy's claim is a straight count "
            "of bodies and cables. The variant-selection rule permits it: this "
            "difference IS visible in a static frame, unlike the section's cost "
            "claim, which no image can carry. EVIDENCE: 1.13, owner-passed, two "
            "rendered worked examples. PRODUCT PRESENCE: last panel only, which is "
            "the order rule. PROMPT RISK: needs the reference photo; runs handheld "
            "rather than strict because the capability gate says strict needs "
            "compositing and this pipeline renders one frame by hand.",
        "options": [
            opt("A", "baseline", "04-proof-lockedframe", "1.13", "16:9", P_F4_A,
                "Three panels on one desk: one plain drive, then three bodies and "
                "four cables, then the reference drive alone. The fairness rule is "
                "stated in the prompt because the alternatives here are products the "
                "reader may already own.",
                variant="verdict", axes={"camera_lock": "handheld",
                                         "context_mode": "natural-use"},
                pipeline="single-pass", avoid=AV_LOCKED,
                notes="Needs the product photo. generation_mode is multi-pass at "
                      "type level, but 1.8's capability gate runs --verdict handheld "
                      "in one pass where the renderer cannot composite, which is the "
                      "case here.",
                asset="58-08-features4-lockedframe-verdict.png"),
            opt("B", "execution: scene, framing and the moment compared",
                "04-proof-lockedframe", "1.13", "16:9", P_F4_B,
                "The same count argued as what has to go in a bag rather than what "
                "sits on a desk, shot down onto a kitchen table. Coiled cables read "
                "as volume more plainly than connected ones.",
                variant="verdict", axes={"camera_lock": "handheld",
                                         "context_mode": "natural-use"},
                pipeline="single-pass", avoid=AV_LOCKED,
                notes="Needs the product photo. Every panel sits at the same moment "
                      "- nothing packed yet - which is the type's moment rule.",
                asset="58-08-features4-lockedframe-verdict-b.png"),
            opt("C", "execution: place and what carries the argument",
                "04-proof-lockedframe", "1.13", "16:9", P_F4_C,
                "A living-room shelf rather than a work surface, arguing the count "
                "as what has to live permanently in a room. Cables running off the "
                "shelf edge are the visible difference.",
                variant="verdict", axes={"camera_lock": "handheld",
                                         "context_mode": "natural-use"},
                pipeline="single-pass", avoid=AV_LOCKED,
                notes="Needs the product photo. The disc spines behind must stay "
                      "unbranded and unreadable - the type bars recognisable "
                      "trademarks outright.",
                asset="58-08-features4-lockedframe-verdict-c.png"),
        ],
    },
]

# reviews.shots.0-3 — one type across a repeating section, four completely
# different snapshots (cross-slot rule 2 + the type's SET DIVERSITY LAW).
SHOTS = [
    ("reviews.shots.0.image", "58-09-reviews-shot-0.png",
     "First of four customer-photo tiles above the review quotes.",
     [("A", "baseline", P_R0_A,
       "in-use at a warm-lit home-office desk, the drive mid-read with a forearm "
       "incidentally in frame. The default mode, and the one that shows the product "
       "doing something."),
      ("B", "mode: in-use -> at-rest", P_R0_B,
       "The same desk with the drive simply living there, part-peeled factory film "
       "still on the lid. at-rest is the mode that best carries 'this exists and "
       "someone owns it'."),
      ("C", "execution: room class, light temperature and distance", P_R0_C,
       "in-use again but on a bedroom windowsill under cold overcast daylight, shot "
       "further back. Use it if the desk scene collides with another tile.")],
     "MODE and light decide it. A is the default in-use mode and the only one of the "
     "four A options that shows the drive actually reading, which anchors the set. "
     "Its warm dim lamp light is the furthest from tile 1's flat kitchen overhead, "
     "tile 2's mixed floor light and tile 3's cool shelf daylight, so the set "
     "diversity law holds at the A level. EVIDENCE: the type passed at 1.2 on 2 of 2 "
     "renders, both with empty failure lists, and in-use is the mode its "
     "owner-passed socket-tester example used."),
    ("reviews.shots.1.image", "58-10-reviews-shot-1.png",
     "Second of four customer-photo tiles above the review quotes.",
     [("A", "baseline", P_R1_A,
       "kit-flatlay on a kitchen table under flat green-tinged overhead light - the "
       "opened box as an owner actually keeps it, cables loosely coiled and the lid "
       "shoved aside."),
      ("B", "mode: kit-flatlay -> at-rest", P_R1_B,
       "The same table with just the drive set down after unboxing, a factory "
       "sticker still on it whose print stays too small to read."),
      ("C", "execution: room class, light temperature and surface", P_R1_C,
       "The same flatlay moved onto a living-room carpet under a warm standard lamp "
       "and shot from standing height.")],
     "MODE carries this tile. kit-flatlay is the one mode that shows what actually "
     "arrives in the box, which answers the 'both adapter cables came included' line "
     "in the copy without the image claiming anything. Its flat overhead kitchen "
     "light and top-down distance are distinct from all three other tiles. "
     "PROMPT RISK: the leaflet must stay illegible at size - the type allows "
     "generated print only where it cannot be read, and a readable one would be an "
     "invented claim."),
    ("reviews.shots.2.image", "58-11-reviews-shot-2.png",
     "Third of four customer-photo tiles above the review quotes.",
     [("A", "baseline", P_R2_A,
       "in-use on a living-room floor in mixed lamp-and-window light, a memory card "
       "going into the slot with two fingers just leaving it, shot from kneeling "
       "height."),
      ("B", "mode: in-use -> at-rest", P_R2_B,
       "The same rug with the drive left where it was used, one cable still trailing "
       "off toward a laptop out of frame."),
      ("C", "execution: room class and light temperature", P_R2_C,
       "The card-reader action moved to a garage workbench under cold fluorescent "
       "strip light, which is the furthest room class from the other three tiles.")],
     "FIT to the copy decides it. This is the only tile that shows the SD slot in "
     "use, and the reviews lead names 'transferred raw camera photos from the SD "
     "slot' as one of the three things buyers mention. Its mixed warm-and-cold floor "
     "light and kneeling-height distance keep it apart from the other three. "
     "COMPLIANCE: fingers only and no face - a face turns a snapshot into a "
     "testimonial portrait, which is a different type's job and a risk here."),
    ("reviews.shots.3.image", "58-12-reviews-shot-3.png",
     "Fourth of four customer-photo tiles above the review quotes.",
     [("A", "baseline", P_R3_A,
       "at-rest on a living-room shelf beside a row of disc spines under cool "
       "falling-off daylight, shot a little far back and slightly low."),
      ("B", "mode: at-rest -> in-use", P_R3_B,
       "The same shelf with the drive mid-read and a hand withdrawing at the frame "
       "edge."),
      ("C", "execution: room class, light and distance", P_R3_C,
       "at-rest on a hallway table beside a folded laptop sleeve under a single dim "
       "warm bulb, shot quickly from above.")],
     "MODE and set balance decide it. Three tiles already show the drive being "
     "handled or unboxed, so the fourth earns its place by showing where it ends up "
     "living, which is the at-rest mode's whole argument. The disc spines behind it "
     "must stay unbranded and unreadable. Its cool falling-off daylight and longer "
     "distance complete the four-way separation the set diversity law requires."),
]

for slot_id, asset, placement, opts, basis in SHOTS:
    SLOTS.append({
        "slot_id": slot_id, "section_role": "social-proof", "asset": asset,
        "placement": placement,
        "gif": {"eligible": False, "form": "none",
                "reason": "A customer snapshot argues that the thing exists in a "
                          "real home. That is a held state, and this type bans every "
                          "added layer, so there is nothing a loop could occupy."},
        "recommended_opt": "A", "recommendation_basis": basis,
        "options": [
            opt(o, v, "05-social-snapshot", "1.2", "1:1", p, r,
                axes={"register": "ugc"}, avoid=AV_SNAP,
                notes=FENCE if o == "A" else
                      "Needs the product photo. " + SNAP_SET,
                asset=asset.replace(".png", f"-{o.lower()}.png"))
            for o, v, p, r in opts
        ],
    })

# Out-of-library-scope slots.
for sid, asset, place, why in [
    ("product.image", "—",
     "Product card in the mid-page 'Our top pick for disc recovery' block.",
     "The cta row of mapping/slot-rules.md is empty by design across all four "
     "channels: a product card's image is a standard product shot, which the library "
     "does not cover. This is a deliberately empty cell, not an exhausted one, so the "
     "widening ladder does not apply. Shoot or supply the pack shot."),
    ("product_end.image", "—",
     "Product card in the closing 'The compact drive that restored our archive' block.",
     "Same as product.image - a closing CTA product card. Standard product shot, out "
     "of library scope."),
    ("hero.author_avatar", "—", "Byline portrait beside 'By Warren Hayes'.",
     "A portrait of a named author. No library type produces portraits, and "
     "generating a face to sit under a real-sounding byline manufactures a person. "
     "Use a real photograph of the actual author or drop the avatar."),
    ("guide.avatar", "—", "Portrait in the 'About the author' block.",
     "Same as hero.author_avatar - a named person's portrait. Out of library scope "
     "and a disclosure question rather than an imaging one."),
]:
    SLOTS.append({"slot_id": sid, "section_role": "cta" if "product" in sid else
                  "author", "asset": asset, "placement": place,
                  "out_of_scope_reason": why, "options": []})

for i in range(6):
    SLOTS.append({
        "slot_id": f"comments.items.{i}.avatar", "section_role": "social-proof",
        "asset": "—",
        "placement": f"Commenter portrait, comment {i + 1} of 6.",
        "out_of_scope_reason":
            "A portrait attached to a named commenter. Out of library scope, and "
            "generating one would put an invented face beside an invented name in a "
            "block that reads as real user comments. 05-social-snapshot's fence "
            "names avatars specifically as what a generated image must never sit "
            "beside. Supply real avatars or render the block without them.",
        "options": []})

OUT = {
    "page_id": "58",
    "registry_version": "2.0.0",
    "channel": "advertorial",
    "awareness_stage": "problem-aware",
    "slots": SLOTS,
    "coverage": {
        "covered": [
            "step 1 pain — 01-pain-scene twice, a person at the hero and the "
            "object-only dongle nest at problems.items.0",
            "step 2 cause — 02-cause-anatomy --diagnostic at problems.items.1",
            "step 3 mechanism — 03-mechanism-xray at features.items.0",
            "step 4 proof — 04-proof-lockedframe --verdict at features.items.4",
            "step 5 social — 05-social-snapshot across all four review tiles",
            "step 6 relief — 06-relief-hero twice in the features block and "
            "06-relief-scene at the outcome beat",
        ],
        "absent": [
            "step 2 symptom — 02-symptom-rail was trimmed off advertorial on "
            "2026-08-11 and is not a candidate at any rung",
            "step 3 use — 03-use-sequence declares only 3:4 and 1:1, so it cannot "
            "serve any 16:9 slot on this page. The copy would have suited it.",
            "step 5 personas — 05-persona-grid is marketplace and landing-page only",
        ],
        "absent_but_correct": [
            "No symptom rung, and that is right for a problem-aware reader who "
            "already feels the problem: the copy spends its first two sections "
            "re-establishing it in prose and needs the cause and the mechanism next, "
            "which both run.",
            "No 03-mechanism-ghostbody, correctly — body_contact is false for an "
            "external drive and the slot-rules attribute gate drops it outright.",
        ],
        "gaps": [
            "The page makes a NOISE claim in four separate places — rattled, "
            "whisper-quiet, no motor buzzing, silent — and no image on this page can "
            "carry it. Silence is not photographable and no library type argues it. "
            "It stays a copy claim, and the honest place to prove it is video.",
            "features.items.2's headline claim is thermal — a casing staying cool "
            "over a weekend — which is equally invisible. The recommended option "
            "argues the slim half of that section and leaves the thermal half to "
            "the copy; it is not proof and is not presented as any.",
        ],
    },
    "recommended": [],
    "page_composition_notes": [
        GAP_ATTACH,
        "Awareness read as problem-aware, and the basis is the copy rather than the "
        "brief's own field. The hero spends its whole opening re-establishing that a "
        "new laptop has no disc drive, two full sections run before any solution is "
        "named, and the framework is PAS. A problem-aware reader is moved by the "
        "cause and the mechanism, which is why 02-cause-anatomy and 03-mechanism-xray "
        "carry the middle of this routing rather than more proof.",
        "THE TEMPLATE'S PLACEHOLDER TEXT IS FROM A DIFFERENT PRODUCT. Every "
        "placehold.co URL in htmlCompiled is labelled for a weighted blanket - "
        "'Quilted pockets', 'Glass bead fill', 'Halden blanket', 'Folded on bed', "
        "'Wash day', 'Six months on three beds'. TPL-ADV08 was reused without "
        "restamping them. Every brief below is derived from the content dict and the "
        "product brief, never from those labels; ignore them when placing assets.",
        FENCE,
        "Six comment avatars, two author portraits and two product-card shots are "
        "reported out of library scope rather than forced into a type. Ten of the "
        "twenty-two image fields in this export are therefore unrouted by design, "
        "which is the cta row of slot-rules being empty and the portrait question "
        "being a disclosure decision, not an imaging one.",
        "One type appears once per page and two slots hit that wall. "
        "04-proof-lockedframe was wanted at both problems.items.0 and "
        "features.items.4 and went to the second, because its use_when requires a "
        "reader who already understands the mechanism. 06-relief-hero runs twice, at "
        "features.items.1 and features.items.2, under rung 4 of the widening ladder "
        "with inset_mode, subject, place and pose all named as the differing "
        "dimensions. A third relief-hero would be past what that rung permits, which "
        "is why option B at features.items.3 is flagged as forcing two other slots "
        "to change.",
        "Page arc holds: every pain image sits above the first relief image. The one "
        "pain cue below it is inside features.items.3 option B's recall inset, which "
        "the type permits because pain exists only inside the inset there.",
        "02-cause-anatomy is being asked for its first NON-BIOLOGICAL body. Every "
        "subject class it has rendered is anatomical. Its device is a 2D "
        "cross-section and its avoid_when asks only for internal structure to draw, "
        "which a disc, a track and a lens have - but this is untested and the first "
        "render of problems.items.1 is the test.",
        "No pick prior was available. feedback/picks.jsonl is empty, so the >=20-pick "
        "tie-breaker in SPEC 7.7 never fired and every recommendation here rests on "
        "fit, legality, render evidence, product presence and prompt risk alone. "
        "These recommendations make the page argument-complete; they are not "
        "conversion-optimised and nothing here is performance-backed.",
        "Ratio is set in the generation tool's aspect-ratio parameter, never in the "
        "prompt text (adapters/nano-banana.md Rule 4). The Strictly avoid line is "
        "not rendered into any prompt (ADR-014); the exclusion list is kept in each "
        "option's avoid field for a model with a real negative channel.",
    ],
}


# ---- build the plate prompt (G12, ADR-020) ----------------------------------
# The gif prompt RENDERS the work order; it never animates a supplied still.
# On whole-frame the plate IS the delivered image, so the card carries the five
# lines and nothing else.
#
# One template, and the five lines are generated from the stored brief fields
# rather than retyped, so the words the model draws cannot drift from the words
# prompts.json records. The wording of the card itself follows G12's template
# and the one whole-frame render that passed, eval/render-tests.jsonl record
# 209: a single white rule inset from the edges, no bleed, no decoration, no
# scene.
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
    # The plate is production-only and a page asset carrying one is a defect, so
    # it takes the --brief suffix and never the slot's own filename (G12).
    _root, _ext = os.path.splitext(_s["asset"])
    _g["asset"] = f"{_root}--brief{_ext}"


ATTACH_RE = re.compile(r"\battached\b", re.I)


def binds_a_photo(o):
    """Whether THIS prompt asks for an attachment. Read off the prompt, not off
    the type's index flag: that flag is type-level and two variants on this page
    override it — `02-cause-anatomy --diagnostic` drops [PRODUCT REFERENCE] and
    reads false for the variant, and `04-proof-lockedframe --rivals` is the
    exception Step 5 names. A type-level read calls four runnable prompts
    blocked. The disagreements are reported below, never resolved silently."""
    return bool(ATTACH_RE.search(o["prompt"]))


def run_state(o):
    """What this prompt needs before it can be pasted. ADR-021: one prompt, one
    generation call, at most one reference photo the owner attaches in the tool —
    so an empty `attachments` is NOT a blocked prompt, it is a prompt that wants
    the owner's own product photo. The only real blocker left is a mode that
    needs compositing, which this pipeline does not do."""
    if o["pipeline"] != "single-pass":
        return "BLOCKED", "needs compositing, which this pipeline does not do"
    if binds_a_photo(o):
        return "ATTACH THE PHOTO", "paste it, upload the product photo, set "\
                                   "the ratio"
    return "PASTE AS IS", "no attachment, no reference — paste it and set the "\
                          "ratio"


def md(d):
    L = []
    A = L.append
    A("# Image prompts — page 58, 7-in-1 external DVD / Blu-ray drive")
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
    A("Ratio goes in the generation tool's own aspect-ratio parameter, never in the "
      "prompt text (adapters/nano-banana.md Rule 4). The `Strictly avoid:` line is "
      "not rendered into any prompt (ADR-014); the exclusion list is kept in the "
      "JSON's `avoid` field for a model with a real negative channel.")
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
    A(f"**All {n_opts + len(plates)} prompts are paste-and-run.** One prompt, one "
      f"generation call, no compositing and no edit chain (ADR-021). "
      f"{len(blocked)} are blocked.")
    A("")
    A(f"- **{len(withphoto)} want the product photo** — paste the prompt, upload "
      f"the drive photo, set the ratio. They carry a G1 reference block, so the "
      f"render is bound to the real product rather than an invented one. The "
      f"`attachments` field is empty because the source export supplied no "
      f"photograph and none was invented; the upload is yours to make.")
    A(f"- **{len(bare) + len(plates)} take no attachment at all** — paste and set "
      f"the ratio. {len(bare)} options plus both G12 brief plates, which are text "
      f"cards and bind nothing.")
    A("")
    for s, o in bare:
        v = f" `{o['variant']}`" if o.get("variant") else ""
        A(f"  - `{s['slot_id']}` option {o['opt']} — {o['type']}{v} · {o['ratio']}")
    for s in plates:
        A(f"  - `{s['slot_id']}` option D — the G12 brief plate · "
          f"{next(x['ratio'] for x in s['options'] if x['opt'] == s['recommended_opt'])}")
    A("")
    A("Every option below carries a `runs:` line saying which of the two it is.")
    A("")

    A("## Read this first")
    A("")
    for n in d["page_composition_notes"]:
        head, _, rest = n.partition(". ")
        A(f"- **{head}.** {rest}")
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

    A("## Coverage")
    A("")
    for k, label in (("covered", "Covered"), ("absent", "Absent"),
                     ("absent_but_correct", "Absent on purpose"), ("gaps", "Gaps")):
        vals = d["coverage"].get(k) or []
        if not vals:
            continue
        A(f"**{label}**")
        A("")
        for v in vals:
            A(f"- {v}")
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
        # The gif is a fourth option below C (ADR-020). It is not an alternative
        # to A-C: the plate is a work order and the editor needs a frame to
        # move, so it renders alongside the recommended still.
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
# G12: keep each drawn line inside seven words, because a wrapped line broke the
# block's alignment in a real render. Counted on the words the model will draw,
# label included, which is how the four passing plates were counted.
long_lines = [(s["slot_id"], ln, len(ln.split()))
              for s in gifs
              for ln in s["gif"]["prompt"].split("\n")
              if ln.startswith(("GIF SLOT", "SHOT ", "ACTION ", "RESULT ",
                                "MATCH "))
              and len(ln.replace(" · ", " ").split()) > 7]
print("plate lines over G12's seven words:", long_lines or "none")
# A page asset carrying a plate is a defect, so the plate render must not be
# named as the slot's own asset.
clash = [(s["slot_id"], s["asset"]) for s in gifs
         if s["gif"]["asset"] == s["asset"] or "--brief" not in s["gif"]["asset"]]
print("plate render named as a page asset:", clash or "none")
# The plate is a claim about the still it accompanies, so that still has to
# exist: the recommended option must be one of the options actually emitted.
orphan = [(s["slot_id"], s["recommended_opt"]) for s in gifs
          if s["recommended_opt"] not in [o["opt"] for o in s["options"]]]
print("gif pointing at no option:", orphan or "none")
# ADR-020: no motion prompt survives anywhere in the artifact.
motion = [s["slot_id"] for s in gifs
          if "animate the supplied" in s["gif"]["prompt"].lower()]
print("gif prompts that animate a still:", motion or "none")
# ADR-021: the pipeline is paste-and-run, so an option that needs compositing is
# a routing defect, not a note.
composited = [(s["slot_id"], o["opt"], o["type"], o["pipeline"])
              for s in routed for o in s["options"]
              if o["pipeline"] != "single-pass"]
print("options needing compositing:", composited or "none")
import collections as _c
_st = _c.Counter(run_state(o)[0] for s in routed for o in s["options"])
print("run state across %d options: %s  (+%d brief plates, both PASTE AS IS)"
      % (sum(_st.values()), dict(_st), len(gifs)))
# Where the prompt and the type-level flag disagree, print it. Each one should be
# a variant that declares its own exemption; a new one appearing here is either a
# missing G1 block or an undeclared exemption, and both need a person.
split = [(s["slot_id"], o["opt"], o["type"], o.get("variant"))
         for s in routed for o in s["options"]
         if bool(TYPES.get(o["type"], {}).get("requires_product_photo"))
         != binds_a_photo(o)]
print("prompts exempt from their type's photo flag (each must be a declared "
      "variant exemption):")
for row in split:
    print("   ", row)
extra = sorted({k for s in OUT["slots"] for k in (s.get("gif") or {})}
               - {"eligible", "form", "kind", "duration_s", "loop", "asset",
                  "shot", "action", "result", "match", "delivery", "reason",
                  "prompt"})
print("gif fields outside output.schema.json:", extra or "none")

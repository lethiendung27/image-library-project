#!/usr/bin/env python3
"""Build prompts.json and prompts.md for page 73 — automatic upper arm BP monitor.

prompts.json is the source of truth (query/output.schema.json); prompts.md is
generated from it and is never hand-edited (query/runbook.md Step 7).

Run from anywhere:  python3 query/sessions/73-.../build.py
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAGE = "73"


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

# mapping/slot-rules.md attribute gates, written as data so the routing can be
# checked against them rather than trusted.
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

# ---------------------------------------------------------------- the prompts

P_HERO_A = """A cinematic film still, editorial photojournalism, natural and unstaged.

A woman in her early seventies in a faded cardigan over a cotton blouse, seated at her kitchen table mid-morning, both hands working at a limp fabric blood-pressure cuff wrapped round her own left upper arm. Under that force: her right hand pinches and drags the cuff's free end across her body while her left arm stays lifted and rigid to hold the band where she put it, that shoulder hitched. Face: brow drawn in, jaw set, eyes down on the cuff.

The cuff has twisted along its length so it touches the arm only along a narrow crooked strip, the hook-and-loop flap folded back on itself and gripping nothing, the air tube kinked under her elbow.

One specific place: a small kitchen table at mid-morning, and the lived-in clutter of the routine it disrupts — a half-drunk mug of tea, a pill organiser open at one compartment, a folded tea towel, reading glasses pushed to one side.

She is unaware of the camera, her gaze on the cuff. Key light: window daylight from the left, cool and weak. Fill: the room's own ambient, weaker still. A rim of light separates her shoulder from the background. Deep shadow across the right third of the frame.

Desaturated throughout: one unresolved state, no colour lifted anywhere.

No product, no panels and no insets."""

P_HERO_B = """A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his late sixties in a plain zip-neck jumper, standing at the end of a kitchen counter, mid-way through pulling a fabric blood-pressure cuff tight round his own left upper arm with his right hand. Under that force: the right shoulder lifts and the elbow flares out to get purchase, the left arm braced against the counter edge with the fingers splayed. Face: mouth pressed thin, the muscles at the outer corners of the eyes tightened.

The cuff has slipped down toward the elbow crease and sits half off the muscle, its lower edge rolled into a rope, the hook-and-loop patch stuck to itself instead of to the band.

One specific place: the end of a kitchen counter in the morning, and the lived-in clutter of the routine it disrupts — a cereal bowl not yet cleared, a wall planner with pen marks, a tablet bottle, a charging cable trailing to a socket.

He looks directly into the lens and holds the viewer's eye. Even ambient daylight, bright, minimal shadow, flat and unflattering.

Desaturated throughout: one unresolved state, no colour lifted anywhere.

No product, no panels and no insets."""

P_HERO_C = """A cinematic film still, editorial photojournalism, natural and unstaged.

A woman in her mid-forties in work clothes with the sleeves pushed back, leaning over a dining chair to wrap a fabric blood-pressure cuff round her mother's upper arm, the older woman seated and holding her own sleeve up out of the way. Under that force: the daughter has both hands committed to the band, one thumb pinning the loose end while the other hand drags the strap round, her back bent and her weight carried on the chair back. Face: concentration, lips parted, eyes fixed on the alignment.

The cuff sits crooked on the arm, its lower edge riding up over the elbow crease on one side and gaping open on the other, the tube trapped between band and skin.

One specific place: a dining table before work, and the lived-in clutter of the routine it disrupts — a car key and lanyard put down, a mug, a blister pack pushed out at three tablets, a coat over the next chair.

Neither is aware of the camera; the daughter's gaze is on the cuff. Key light: window daylight from behind them, cool and weak. Fill: the room's ambient. A rim of light separates both shoulders from the background. Deep shadow across the lower third of the frame.

Desaturated throughout: one unresolved state, no colour lifted anywhere.

No product, no panels and no insets."""

P_R0_A = """A 2D illustration in a flat-vector style: flat fills, hard edges, no gradients. Not photography, not a 3D render.

The attached photo is the exact reference for the product.

Two equal panels side by side on one continuous dark-field ground, the same hue and chroma across both, stepping once in value at the divider: one step lighter on the right. Nothing else is in the background.

Each panel shows the whole upper arm and shoulder of one adult figure from the front, the device small within the frame. Exactly one figure per panel, the same scale and the same view in both: the upper arm drawn as the humerus with the brachial artery running along it in warm ivory over a translucent skin outline — an arm, not a skeleton and not a whole body.

Left panel: an ordinary limp fabric cuff, unbranded, wrapped round the upper arm and twisted along its length so it meets the skin only along a narrow crooked strip. Right panel: the same arm resting inside the reference product's fixed slide-in chamber at the same place on the arm, comparable in size, the chamber's inner wall meeting the skin evenly all the way round. The humerus and the brachial artery are drawn in both panels, and neither the cuff nor the chamber covers the artery.

Marks, and nothing in the frame is marked that is not named here:
Two dashed straight lines, one per panel, identical in thickness and dash pattern, each running along the arm and stopping at the two edges of the band where it actually meets the skin — red on the left, blue on the right. The left line spans a much shorter distance than the right, and every other property of the two lines reads as identical.
One curved line tracing the outer wall of the brachial artery where the pressure arrives, one per panel: red on the left, blue on the right.
A badge in the top corner of each panel, a filled solid disc with the glyph cut out of it, the same diameter in both: red with an X on the left, green with a check on the right.

Red for the wrong state, blue for the correct one, green for the badge, warm ivory for the structures, and no other colour anywhere."""

P_R0_B = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

One person photographing on a phone on three different mornings. One framing for every panel: a bare dining table shot from a seated height at arm's length, the table edge running across the lower third and a plain wall filling the upper third. It reads as one shot taken three times, never as three different shots.

The same scene in every panel: a dining table at home with deliberate real-world clutter — a used coaster, a pen, a folded napkin — and flat even light, no strong shadows, no sunlight, no styling.

The variable is which ordinary wrap-cuff monitor is on the table and how its cuff has come to rest, and nothing else changes. Panel one: a wide-cuff wrap monitor, its band collapsed and folded over itself with the tube coiled under it. Panel two: a compact wrap monitor, its band curled into a loop that will not hold its shape, hook-and-loop patch face up. Panel three: a slimmer wrap monitor, its band lying twisted with one end under the body of the device. All three are common, unbranded and in good condition, and each is the subject of its own panel, filling at least half of it.

Variation between panels is on the props only: the coaster moved, the pen turned, the napkin refolded. Light differs between panels in exposure alone, never in warmth.

One grade across every panel, muted and cool. No panel is favoured — no badge, no glow, no colour cue, no brighter exposure. None of them wins and the image makes no claim."""

P_R0_C = """A 2D illustration in an airbrushed style: soft gradients and modelled volume. Not photography, not a 3D render.

The attached photo is the exact reference for the product.

Two equal panels side by side on one continuous dark-field ground, the same hue and chroma across both, stepping once in value at the divider: one step lighter on the right. Nothing else is in the background.

Each panel shows one transverse cross-section through the middle of an adult upper arm, seen end-on and filling most of the panel — the humerus at the centre, the muscle bellies around it and the brachial artery between them, all in warm ivory over a translucent skin outline. An arm in section, not a skeleton. Exactly one figure per panel, the same scale and the same view in both.

Left panel: an ordinary limp fabric cuff, unbranded, drawn as a band closing round the section and pressing into it over one narrow arc only, with a visible gap standing off the skin elsewhere. Right panel: the same section inside the reference product's fixed slide-in chamber, the chamber's inner wall meeting the skin around the whole circumference with no gap. The artery is drawn in both panels and neither the cuff nor the chamber covers it.

Marks, and nothing in the frame is marked that is not named here:
Two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at the two ends of the arc where the band actually meets the skin — red on the left, blue on the right. The left arc is far shorter than the right, and every other property of the two lines reads as identical.
One curved line tracing the outer wall of the brachial artery, one per panel: red on the left, blue on the right.
A badge in the top corner of each panel, a filled solid disc with the glyph cut out of it, the same diameter in both: red with an X on the left, green with a check on the right.

Red for the wrong state, blue for the correct one, green for the badge, warm ivory for the structures, and no other colour anywhere."""

P_R1_A = """A premium technical see-through product visualization, sharp and high detail. Not photography.

The attached photo is the exact reference for the product.

A plain deep slate ground and nothing else on it.

The reference monitor sits three-quarters on to the camera, filling about two thirds of the frame, its outer shell rendered translucent and glass-like. The silhouette, the proportions and every visible external part match the reference exactly.

Inside the shell, rendered solid and detailed: the electric air pump sitting low in the body behind the front face, the short length of tubing running from it up to the port that feeds the arm chamber, the pressure sensor board mounted flat beside the pump, and the battery compartment at the back of the housing. Fine wiring runs from the board to the pump where wiring is real. No component types beyond these.

The pump is the working part and is shown active: it glows cyan, cleaner and brighter than any reflection elsewhere in the render, and it is the brightest thing in the frame. It is the only added colour; everything else keeps the materials' own colours.

The display face is dark and unlit, and carries no characters, numerals or symbols of any kind.

One product, one shell, no exploded parts, no callout lines, no labels."""

P_R1_B = """A clean medical-technical product render on a seamless white infinity background, soft even studio lighting, subtle grey ambient occlusion only, no cast shadow on a floor. Sharp, e-commerce infographic.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render, divided by a single thin vertical line.

In both panels, the same featureless matte white mannequin in the same pose from the same angle: seated upright at a table, the left arm forward on the table surface, the torso cross-sectioned at a vertical plane through the left shoulder and upper arm to reveal the interior. No face, no hair, no clothing, no skin tone.

Inside the body silhouette, never floating on top of it: the humerus and the brachial artery of that upper arm, anatomically accurate, their contour following the contour of what is wrapped or seated around them.

Left panel: an ordinary limp fabric cuff round the upper arm, twisted so it bears on one narrow band. Right panel: the reference product on the table with the same arm resting inside its slide-in chamber, the elbow against the guided base, the chamber's contour visibly aligned with the length of the humerus. The product is the only object in the frame with a real material finish, it keeps its own reference colours and it carries no signal colour at all.

Marks, and nothing in the frame is marked that is not named here:
The humerus and artery drawn in warm off-white ivory in both panels.
A flat hard-edged red overlay on the length of artery the twisted band bears on, left panel only.
A flat hard-edged blue band drawn beside the humerus, following its line and running only the length the chamber reaches, right panel only — beside the bone, never a fill of it.
A circle badge in the top corner of each panel, a filled solid disc with the glyph cut out of it: red with an X on the left, green with a check on the right.

Every mark is a flat, unshaded, hard-edged overlay laid on top of the render. Achromatic white and grey everywhere except those marks."""

P_R1_C = """A premium technical see-through product visualization, sharp and high detail. Not photography.

The attached photo is the exact reference for the product.

A plain warm grey ground and nothing else on it.

The reference monitor is seen from directly above with the arm chamber opening toward the camera, filling about three quarters of the frame, its outer shell rendered translucent and glass-like. The silhouette, the proportions and every visible external part match the reference exactly.

Inside the shell, rendered solid and detailed: the electric air pump low in the body, the inflatable bladder wrapped round the inner wall of the arm chamber, the short tube joining the two, and the pressure sensor board beside the pump. Fine wiring runs from the board to the pump. No component types beyond these.

The bladder is the working part and is shown active, inflated against the chamber wall all the way round: it glows cyan, cleaner and brighter than any reflection elsewhere in the render, and it is the brightest thing in the frame. It is the only added colour; everything else keeps the materials' own colours.

The display face is dark and unlit, and carries no characters, numerals or symbols of any kind.

One product, one shell, no exploded parts, no callout lines, no labels."""

P_R2_A = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

One person photographing on a phone on three different mornings. One framing for every panel: a kitchen worktop shot from standing height at about a metre and a half back, the worktop edge across the lower third and a tiled splashback filling the upper third. It reads as one shot taken three times, never as three different shots.

The same scene in every panel: a kitchen worktop with deliberate real-world clutter — a wooden board stood on edge, a jar of utensils, a folded cloth — and flat even light, no strong shadows, no sunlight, no styling.

The variable is which monitor stands on the worktop, and the moment is the same in all three: each device switched on and settled, seen from that same standing distance. Panel one: a common compact wrap-cuff monitor with a small screen. Panel two: a common mid-size wrap-cuff monitor with a screen roughly the same size as panel one's. Panel three: the reference product. Each is the subject of its own panel and fills at least half of it.

In every panel the lit screen reads as a pale glow with no characters, numerals or symbols legible at this distance; what differs between the panels is the physical size of the lit area and how much of the device face it occupies.

Panels one and two get exactly the same photographic respect as panel three: identical exposure, identical background tidiness, identical framing generosity. Both alternatives are ordinary products in good condition. Variation between panels is on the props only: the cloth refolded, the jar turned, the board moved. Light differs between panels in exposure alone, never in warmth.

One grade across every panel. No badge, no glow, no colour cue, and no panel brighter or cleaner than the others."""

P_R2_B = """A premium technical see-through product visualization, sharp and high detail. Not photography.

The attached photo is the exact reference for the product.

A plain deep charcoal ground and nothing else on it.

The reference monitor is seen square on to its display face, filling about three quarters of the frame, its outer shell rendered translucent and glass-like. The silhouette, the proportions and every visible external part match the reference exactly.

Inside the shell, rendered solid and detailed: the backlight panel sitting directly behind the display face and spanning its full width and height, the display driver board below it, and the battery compartment behind. Fine wiring runs from the board to the panel. No component types beyond these.

The backlight panel is the working part and is shown active: it glows cyan through the translucent face, evenly across its whole area, cleaner and brighter than any reflection elsewhere in the render, and it is the brightest thing in the frame. Its lit area is plainly larger than the housing around it. It is the only added colour; everything else keeps the materials' own colours.

The face carries no characters, numerals or symbols of any kind — only the even lit field.

One product, one shell, no exploded parts, no callout lines, no labels."""

P_R2_C = """Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

One person photographing on a phone on three different evenings. One framing for every panel: a bedside table shot from a standing height beside the bed at about a metre back, the table top across the lower third and a lamp-lit wall filling the upper third. It reads as one shot taken three times, never as three different shots.

The same scene in every panel: a bedside table with deliberate real-world clutter — a paperback face down, a glass of water, a folded reading light — and flat even light, no strong shadows, no styling.

The variable is which monitor stands on the table, and the moment is the same in all three: each device switched on and settled, seen from that same standing distance. Panel one: a common compact wrap-cuff monitor with a small screen. Panel two: a common mid-size wrap-cuff monitor with a screen roughly the same size as panel one's. Panel three: the reference product. Each is the subject of its own panel and fills at least half of it.

In every panel the lit screen reads as a pale glow with no characters, numerals or symbols legible at this distance; what differs between the panels is the physical size of the lit area and how much of the device face it occupies.

Panels one and two get exactly the same photographic respect as panel three: identical exposure, identical background tidiness, identical framing generosity. Both alternatives are ordinary products in good condition. Variation between panels is on the props only: the paperback moved, the glass turned, the reading light refolded. Light differs between panels in exposure alone, never in warmth.

One grade across every panel. No badge, no glow, no colour cue, and no panel brighter or cleaner than the others."""

P_R3_A = """A professional photograph, controlled light and deliberate negative space.

The attached photo is the exact reference for the product, identical in every layer.

A man in his seventies in a soft checked shirt is seated at a dining table, mid-action with his left arm resting inside the reference monitor's slide-in chamber and his elbow settled against the guided base, his right index finger just leaving the single start button, his gaze on the point of use with focused satisfaction. He sits to the left of the frame.

One real dining room filled to the edges with six to eight objects that genuinely belong there — a fruit bowl, a stacked pair of placemats, a cordless phone base, a jug, two dining chairs, a plant on the sill. Background blurred but never blank: no bare wall or floor area larger than the product. None of these objects carries printed text. High-key neutral grade.

Hard side light from the window falls across the monitor's face, strong enough that the lit display glows clearly against the darker side of the room; lens flare and blown highlights are welcome, they read as real. The lit display carries no characters, numerals or symbols — it reads as an evenly lit field and nothing more, and it is the brightest thing in the frame.

In the upper right corner sits a small rectangular panel, occupying most of the space the man is offset from and held well clear of every frame edge, its outer edge finishing a visible margin short of the picture on both sides. Inside it, the same dining table photographed the same way at a different hour: the same monitor on the table beside a spiral notebook lying open, its ruled pages covered in rows of handwritten figures, a pen across it. That whole panel is desaturated to grey.

One neutral arrow inside that panel runs from the notebook to the monitor. It is the only arrow anywhere in the image.

The room, the light and the man are the same in the panel as in the main photograph. No other panel, no badge, no glow and no other mark."""

P_R3_B = """A phone photo taken by an ordinary person in their own home: slightly off exposure, mild overexposure on the window, no rim light, no negative space, framing casual and a little too close, the room left exactly as it is.

The attached photo is the exact reference for the product, identical in every layer.

A woman in her late sixties in a cardigan is seated at a kitchen table, mid-action with her left arm resting inside the reference monitor's slide-in chamber and her elbow settled against the guided base, her right hand just off the single start button, her gaze on the point of use. She sits to the right of the frame.

One real kitchen filled to the edges with six to eight objects that genuinely belong there — a bread bin, a kettle, a mug tree, a stack of post, a tea towel over the oven rail, a small radio. Background blurred but never blank: no bare wall or worktop area larger than the product. None of these objects carries printed text. High-key neutral grade.

Hard side light from the kitchen window falls across the monitor's face, strong enough that the lit display glows clearly against the darker side of the room. The lit display carries no characters, numerals or symbols — it reads as an evenly lit field and nothing more, and it is the brightest thing in the frame.

In the upper left corner sits a small rectangular panel, occupying most of the space the woman is offset from and held well clear of every frame edge, its outer edge finishing a visible margin short of the picture on both sides. Inside it, the same kitchen table photographed the same way at a different hour: a limp fabric wrap cuff lying collapsed on the table with its tube coiled under it and its hook-and-loop flap folded back on itself. That whole panel is desaturated to grey.

One neutral arrow inside that panel runs from the collapsed cuff to the edge of the panel nearest the woman. It is the only arrow anywhere in the image.

The room, the light and the woman are the same in the panel as in the main photograph. No other panel, no badge, no glow and no other mark."""

P_R3_C = """A professional photograph, controlled light and deliberate negative space.

The attached photo is the exact reference for the product, identical in every layer.

Present only as working hands and forearms: two adult left forearms, one visibly older with looser skin and a plain wedding band, one younger with a wristwatch pushed up out of the way, one after the other at the same place at a dining table beside the reference monitor. The older forearm is resting inside the slide-in chamber with the elbow against the guided base; the younger one waits at the table edge with the sleeve already pushed back. No face is in frame. The pair sit to the left of the frame.

What makes finished look different from unfinished, tied to the action: the older forearm is settled and still inside the chamber with the chamber closed round it, and the younger forearm is still outside it with the sleeve only just cleared.

One real dining room filled to the edges with six to eight objects that genuinely belong there — a fruit bowl, placemats, a cordless phone base, a jug, two chairs, a plant on the sill. Background blurred but never blank: no bare wall or table area larger than the product. None of these objects carries printed text. High-key neutral grade.

Hard side light from the window falls across the monitor's face, strong enough that the lit display glows clearly against the darker side of the room. The lit display carries no characters, numerals or symbols — it reads as an evenly lit field and nothing more, and it is the brightest thing in the frame.

In the upper right corner sits a small rectangular panel, occupying most of the space the forearms are offset from and held well clear of every frame edge, its outer edge finishing a visible margin short of the picture on both sides. Inside it, the same table photographed the same way at a different hour: one spiral notebook open at ruled pages of handwritten figures with two different hands of writing running down the same column. That whole panel is desaturated to grey.

One neutral arrow inside that panel runs from the notebook to the monitor. It is the only arrow anywhere in the image.

The room and the light are the same in the panel as in the main photograph. No other panel, no badge, no glow and no other mark."""

P_R4_A = """A candid documentary photograph a passer-by could have taken. Natural, unposed, sharp. Not styled, not lit, not aware of a camera.

The attached photo is the exact reference for the product.

A man in his seventies in put-together but ordinary clothes — a zip-neck jumper over a collared shirt, the same muted palette family — is walking out through the doors of a community health centre into the street, a folded appointment card in one hand, pausing briefly to look along the pavement for his bus. He is absorbed in his own business and never looks toward the camera.

An ordinary public place he would actually pass through: the entrance apron of a small health centre on a weekday, two or three incidental blurred passers-by, a bike rack, ordinary overcast weather.

The reference monitor is in the scene as the reason he is calm and not presented to the camera: it is in the open canvas bag on his shoulder, sitting upright in the mouth of the bag with its face turned outward so its front can be read, the mains adapter coiled beside it in the bag. It is not centred, not held up and not hidden.

The moment of letting go, in a situation that would have demanded bracing: his shoulders are down and his free hand is loose at his side while he waits at a kerb he would once have crossed with the card gripped in both hands.

Even natural daylight, bright, soft shadows. No golden hour, no rim light, no glamour lighting. A natural palette with light film grain and shallow depth of field, honest rather than drained, the light allowed to be kind.

No panels, no insets, no badges, no arrows and no drawn overlays of any kind."""

P_R4_B = """A phone photo taken by an ordinary person in their own home: slightly off exposure, mild overexposure on the window, no rim light, no negative space, framing casual and a little too close, the room left exactly as it is.

The attached photo is the exact reference for the product, identical in every layer.

Present only as working hands and forearms: one adult pair setting the reference monitor down on a kitchen worktop beside a socket, one hand still under the base and the other laying the coiled mains adapter down next to it. No face is in frame. The hands sit to the right of the frame.

What makes finished look different from unfinished, tied to the action: the adapter is out of its bag and uncoiled to its full length beside the device with its plug already turned toward the socket, and the empty carton is pushed back behind the device with its flaps open.

One real kitchen filled to the edges with six to eight objects that genuinely belong there — a kettle, a mug tree, a bread bin, a stack of post, a tea towel over the oven rail, a bowl of fruit. Background blurred but never blank: no bare wall or worktop area larger than the product. None of these objects carries printed text. High-key neutral grade.

Soft even window light, the background blurred, high-key. The display face is dark and unlit and carries no characters, numerals or symbols of any kind.

No panel, no inset, no badge, no glow and no mark of any kind anywhere in the image."""

P_R4_C = """A candid documentary photograph a passer-by could have taken. Natural, unposed, sharp. Not styled, not lit, not aware of a camera.

The attached photo is the exact reference for the product.

A woman in her late sixties in put-together but ordinary clothes — a light raincoat over a jumper, the same muted palette family — is standing at a railway platform beside a wheeled overnight case, checking the departure board along the platform and shifting her weight to one foot. She is absorbed in her own business and never looks toward the camera.

An ordinary public place she would actually pass through: a suburban station platform on a weekday, two or three incidental blurred passers-by further down, a bench and a litter bin, ordinary overcast weather.

The reference monitor is in the scene as the reason she is unbothered and not presented to the camera: it is in the open outer pocket of the wheeled case at her side, sitting upright with its face turned outward so its front can be read, the mains adapter coiled in the pocket beside it. It is not centred, not held up and not hidden.

The moment of letting go, in a situation that would have demanded bracing: both hands rest on the case handle rather than clutching a bag against her body, and her shoulders are down while she reads the board.

Even natural daylight, bright, soft shadows. No golden hour, no rim light, no glamour lighting. A natural palette with light film grain and shallow depth of field, honest rather than drained, the light allowed to be kind.

No panels, no insets, no badges, no arrows and no drawn overlays of any kind."""

P_RB0_A = """A clean medical-technical product render on a seamless white infinity background, soft even studio lighting, subtle grey ambient occlusion only, no cast shadow on a floor. Sharp, e-commerce infographic.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render, divided by a single thin vertical line.

In both panels, the same featureless matte white mannequin in the same pose from the same angle: seated on a chair at a plain table, seen from the side, the left arm forward on the table with the forearm horizontal, the torso cross-sectioned at a vertical plane through the chest and the left upper arm to reveal the interior. No face, no hair, no clothing, no skin tone.

Inside the body silhouette, never floating on top of it: the heart in the cross-sectioned chest and the humerus with the brachial artery running along the left upper arm, anatomically accurate, their contour following the contour of what is seated around them.

Left panel: the table is low, so the mannequin's forearm rests well below the level of the heart and the upper arm angles downward. Right panel: the table is at standard height, so the same forearm rests with the upper arm level with the heart, and the reference product sits on the table with that arm inside its slide-in chamber and the elbow against the guided base. The product is the only object in the frame with a real material finish, it keeps its own reference colours and it carries no signal colour at all.

Marks, and nothing in the frame is marked that is not named here:
The heart, the humerus and the artery drawn in warm off-white ivory in both panels.
A flat hard-edged red overlay on the length of the brachial artery lying below heart level, left panel only.
A flat hard-edged blue band drawn beside the humerus, following its line and running only the length the chamber reaches, right panel only — beside the bone, never a fill of it.
A circle badge in the top corner of each panel, a filled solid disc with the glyph cut out of it: red with an X on the left, green with a check on the right.

Every mark is a flat, unshaded, hard-edged overlay laid on top of the render. Achromatic white and grey everywhere except those marks."""

P_RB0_B = """A 2D illustration in a flat-vector style: flat fills, hard edges, no gradients. Not photography, not a 3D render.

The attached photo is the exact reference for the product.

Two equal panels side by side on one continuous dark-field ground, the same hue and chroma across both, stepping once in value at the divider: one step lighter on the right. Nothing else is in the background.

Each panel shows the whole seated upper body of one adult figure from the side at a table, the device small within the frame. Exactly one figure per panel, the same scale and the same view in both: the heart in the chest and the humerus with the brachial artery running along the left upper arm, all in warm ivory over a translucent body outline — a torso and arm, not a skeleton.

Left panel: the figure sits at a low table so the left upper arm hangs below the level of the heart, with an ordinary unbranded wrap cuff on that arm. Right panel: the same figure at a standard-height table with the same upper arm level with the heart, resting inside the reference product's slide-in chamber with the elbow on the guided base. The heart and the artery are drawn in both panels and nothing covers either.

Marks, and nothing in the frame is marked that is not named here:
Two horizontal datum lines, one per panel, both at the same height, each running from the heart across to the arm — neutral, carrying no signal colour. In the left panel the arm sits well below its line; in the right panel the arm meets it.
Two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at the heart and at the midpoint of the upper arm — red on the left, blue on the right. The left line spans a much greater distance than the right, and every other property of the two lines reads as identical.
A badge in the top corner of each panel, a filled solid disc with the glyph cut out of it, the same diameter in both: red with an X on the left, green with a check on the right.

Red for the wrong state, blue for the correct one, green for the badge, warm ivory for the structures, and no other colour anywhere."""

P_RB0_C = """A clean medical-technical product render on a seamless white infinity background, soft even studio lighting, subtle grey ambient occlusion only, no cast shadow on a floor. Sharp, e-commerce infographic.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render, divided by a single thin vertical line.

In both panels, the same featureless matte white mannequin in the same pose from the same angle: seated at a plain table, seen from the front, the left arm forward on the table, the left upper arm cross-sectioned at a plane across its middle to reveal the interior. No face, no hair, no clothing, no skin tone.

Inside the body silhouette, never floating on top of it: the humerus at the centre of that section with the muscle bellies and the brachial artery around it, anatomically accurate, their contour following the contour of what closes around them.

Left panel: an unusually thick upper arm inside the same fixed chamber, the section filling the chamber completely with the arm's outline pressed flat against the inner wall on two sides and the chamber unable to close round it. Right panel: a standard adult upper arm in the same chamber, the section sitting inside it with an even margin all the way round and the chamber closed. The reference product is the only object in the frame with a real material finish, it keeps its own reference colours and it carries no signal colour at all.

Marks, and nothing in the frame is marked that is not named here:
The humerus, muscle and artery drawn in warm off-white ivory in both panels.
A flat hard-edged red overlay on the two flattened arcs of the arm's outline where it is pressed against the chamber wall, left panel only.
A flat hard-edged blue band drawn beside the arm's outline, following its curve and running the full circumference the chamber reaches, right panel only — beside the outline, never a fill of the anatomy.
A circle badge in the top corner of each panel, a filled solid disc with the glyph cut out of it: red with an X on the left, green with a check on the right.

Every mark is a flat, unshaded, hard-edged overlay laid on top of the render. Achromatic white and grey everywhere except those marks."""

P_RB1_A = """Three photographs stacked one above another, filling the whole image, thin white gutters, no outer border, and no panel other than those three. A real home photographed plainly at close range on available light.

The attached photo is the exact reference for the product, in every panel.

The same hands throughout: one older adult's hands, same skin tone, same short nails, same wrists, sleeves pushed back. The same dining table and the same window light from the left in all three panels.

Top panel: the monitor on the table, chamber open and face lit, the left hand guiding the bare left forearm in through the chamber until the elbow comes to rest on the guided base.

Middle panel: the arm settled in the chamber and the right index finger pressing the single start button, the chamber's inner wall drawn in close around the upper arm.

Bottom panel: the arm still in the chamber and the right hand come away to rest flat on the table beside it. On the table the mains adapter lies coiled where it was set down.

In every panel the lit face is an evenly lit field carrying no characters or numerals.

The monitor sits near the centre of every panel and is never cropped. One palette and one light direction across all three panels. No numbers, no step markers, no text and nothing pointing from one panel to another."""

P_RB1_B = """A premium technical see-through product visualization, sharp and high detail. Not photography.

The attached photo is the exact reference for the product.

A plain deep slate ground and nothing else on it.

The reference monitor sits three-quarters on to the camera with its arm chamber open toward the viewer, filling about two thirds of the frame, its outer shell rendered translucent and glass-like. The silhouette, the proportions and every visible external part match the reference exactly.

Inside the shell, rendered solid and detailed: the electric air pump low in the body, the inflatable bladder lining the inner wall of the arm chamber, the short tube joining the two, and the pressure sensor board beside the pump. Fine wiring runs from the board to the pump. No component types beyond these.

The bladder is the working part and is shown active, closed evenly around the full circumference of the chamber: it glows cyan, cleaner and brighter than any reflection elsewhere in the render, and it is the brightest thing in the frame. It is the only added colour; everything else keeps the materials' own colours.

The display face is dark and unlit and carries no characters, numerals or symbols of any kind.

One product, one shell, no exploded parts, no callout lines, no labels."""

P_RB1_C = """Three photographs stacked one above another, filling the whole image, thin white gutters, no outer border, and no panel other than those three. A real home photographed plainly at close range on available light.

The attached photo is the exact reference for the product, in every panel.

The same hands throughout: one adult's hands in their forties, same skin tone, same nails, same wrists, rolled navy cuffs. The same kitchen worktop and the same overhead light in all three panels.

Top panel: the monitor on the worktop, chamber open and face lit, both hands steadying an older person's bare left forearm as it goes in toward the guided base. Only that forearm belongs to the other person; no face is in frame.

Middle panel: the older forearm settled with the elbow on the base, one younger hand pressing the single start button and the other resting on the worktop beside the device.

Bottom panel: the older forearm still in the chamber, both younger hands come away and one settled over the older person's wrist. On the worktop a small card of handwritten dates lies where it was set down.

In every panel the lit face is an evenly lit field carrying no characters or numerals.

The monitor sits near the centre of every panel and is never cropped. One palette and one light direction across all three panels. No numbers, no step markers, no text and nothing pointing from one panel to another."""

# --- review wall, one option each (ADR-022), SET DIVERSITY LAW ----------------

P_W0 = """A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

A kitchen table in an ordinary home in the morning, photographed as found — the clutter left exactly where it was, nothing tidied and nothing added for the camera. Cool window daylight from one side, no other light.

The reference monitor is on the table mid-use, a bare left forearm resting through its chamber with the elbow on the guided base. The person is present only as that forearm; no face is in the frame.

One incidental owner object beside it: a mug with a spoon still in it.

Shot from a seated height at about half a metre, framing slightly tilted and a little too close, focus adequate but casual, mild noise, exposure honest to the room.

The device's face is turned away from the camera at an angle, so nothing on the screen can be read."""

P_W1 = """A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

A bedside table in an ordinary bedroom at night, photographed as found — the clutter left exactly where it was, nothing tidied and nothing added for the camera. Warm lamplight from a bedside lamp, no other light.

The reference monitor is simply sitting where it now lives, switched off, a small factory sticker still on one corner of its housing.

One incidental owner object beside it: a coiled phone charging cable.

Shot from standing height at about a quarter of a metre, framing off-centre and too close, focus adequate but casual, mild motion softness, exposure honest to the room.

The device's face is dark and unlit, so nothing on the screen can be read."""

P_W2 = """A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

A side table beside a sofa in an ordinary living room on an overcast afternoon, photographed as found — the clutter left exactly where it was, nothing tidied and nothing added for the camera. Flat neutral daylight through a net curtain, no other light.

The reference monitor is on the table mid-use, two fingers pressing its single start button, the other hand's forearm already resting through the chamber. The person is present only as those fingers and that forearm; no face is in the frame.

One incidental owner object beside it: a television remote.

Shot from a seated height at about a third of a metre, framing tilted and cropping the far edge of the device, focus adequate but casual, exposure honest to the room.

The device's face is turned away from the camera at an angle, so nothing on the screen can be read."""

P_W3 = """A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

A dining table in an ordinary home in the evening, photographed as found — the clutter left exactly where it was, nothing tidied and nothing added for the camera. A warm kitchen overhead light, no other light.

The opened box and its contents as the owner keeps them, slightly disordered on the table: the reference monitor out of its moulded tray and standing beside it, the mains adapter half uncoiled, a strip of batteries still in its wrap, the carton flaps open behind them. Real accessories only, nothing added. No person is in the frame.

One incidental owner object beside it: a folded manual page, its print too small to read at this size.

Shot from standing height at about three quarters of a metre, framing off-centre with one corner of the carton cut off, focus adequate but casual, exposure honest to the room.

The device's face is dark and unlit, so nothing on the screen can be read."""

P_W4 = """A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

A hallway console table in an ordinary home in the evening, photographed as found — the clutter left exactly where it was, nothing tidied and nothing added for the camera. Mixed warm dim light from a hall fitting and a doorway beyond, no other light.

The reference monitor is simply sitting where it now lives, switched off, pushed back against the wall behind the table's usual pile.

One incidental owner object beside it: a set of keys on a ring.

Shot from standing height at about half a metre, framing tilted with the table edge running out of the corner, focus adequate but casual, mild noise, exposure honest to the room.

The device's face is dark and unlit, so nothing on the screen can be read."""

P_W5 = """A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

A desk in an ordinary spare-room home office in the middle of the day, photographed as found — the clutter left exactly where it was, nothing tidied and nothing added for the camera. Cool daylight from a window behind the desk, no other light.

The reference monitor is on the desk mid-use, seen from almost directly above, a bare left forearm sliding in through the chamber toward the guided base. The person is present only as that forearm; no face is in the frame.

One incidental owner object beside it: an extension plug with two things already in it.

Shot from standing height at about a metre, framing wider than intended with the desk edge and part of the chair back included, focus adequate but casual, exposure honest to the room.

The device's face is angled up away from the camera, so nothing on the screen can be read."""

# --- G12 brief plates (ADR-020: a gif slot emits a plate render) --------------

P_GIF_R1 = """A flat card and nothing else. The whole image is a flat dark grey field with a thin white border just inside its edge, held clear of every frame edge.

Centred on it, in clean white sans-serif, five short lines, each on one line, plain words with no other text anywhere in the picture:

GIF SLOT · 3s · seamless loop
SHOT     side on, chamber and arm
ACTION   chamber closes, hands stay away
RESULT   the machine did the pumping
MATCH    same room and light as still

No scene, no product, no photograph, no other text."""

P_GIF_RB1 = """A flat card and nothing else. The whole image is a flat dark grey field with a thin white border just inside its edge, held clear of every frame edge.

Centred on it, in clean white sans-serif, five short lines, each on one line, plain words with no other text anywhere in the picture:

GIF SLOT · 4s · seamless loop
SHOT     over the table, hands and device
ACTION   arm slides in, finger presses, hand leaves
RESULT   three steps, no wrapping
MATCH    one light, one palette throughout

No scene, no product, no photograph, no other text."""

# ---------------------------------------------------------------- slot table

AVOID = {
    "01-pain-scene": ["red glow", "pain hotspots", "graphic overlay", "arrows", "badges",
                      "split panel", "white background", "studio lighting", "stock photo look",
                      "posed model", "fake grimace", "smiling", "clean staged interior",
                      "saturated colors", "advertising composition", "product placement"],
    "02-cause-anatomy": ["photographic elements", "3D render", "photorealistic skin",
                         "human face", "gore", "correct side on the left",
                         "both dashed lines identical", "missing badge on either panel",
                         "different figure scale between panels", "extra signal colours",
                         "saturated ground", "anatomically wrong structures",
                         "background pattern"],
    "03-mechanism-xray": ["photographic background", "environment", "people", "hands",
                          "spec labels", "capacity text", "callout lines with text",
                          "opaque shell", "internals floating outside the product",
                          "invented components", "exploded parts view", "rainbow palette",
                          "bright white background", "cartoon style"],
    "03-mechanism-ghostbody": ["human face", "facial features", "hair", "skin tone", "clothing",
                               "photographic background", "environment", "furniture",
                               "shadows on floor", "extra colors", "rainbow palette",
                               "anatomically wrong structures", "floating disconnected organs",
                               "cluttered inset", "gore", "realistic flesh", "medical horror"],
    "03-use-sequence": ["step numbers", "arrows carrying the reading order",
                        "arrows between panels", "badges", "different hands between panels",
                        "different subject between panels", "two actions in one panel",
                        "product off-center", "product cropped out", "instruction manual look",
                        "technical diagram", "cold clinical lighting",
                        "different location between panels", "inconsistent palette",
                        "staged perfection"],
    "04-proof-lockedframe": ["badges", "arrows", "glows", "checkmarks", "one panel brighter",
                             "inconsistent lighting between panels", "studio background",
                             "clean styled set", "staged perfection", "saturated colors",
                             "red or green cues", "motion blur", "people", "hands",
                             "brand logos", "recognizable trademarks",
                             "identical framing between panels", "pixel-perfect alignment",
                             "tripod shot", "3D render look", "CGI",
                             "last panel brighter or cleaner than the others",
                             "hero lighting on the final panel",
                             "alternatives made to look broken", "cluttered first panels"],
    "05-social-snapshot": ["studio lighting", "softbox reflections", "seamless background",
                           "negative space", "color grading", "professional composition",
                           "styled props", "badges", "borders", "star ratings",
                           "reviewer names", "avatars", "text overlays", "product render look",
                           "perfect symmetry", "magazine polish", "influencer aesthetic"],
    "06-relief-hero": ["cluttered background", "dark moody lighting", "pain cues in main scene",
                       "blurry product", "inconsistent product between layers",
                       "same angle repeated", "fabricated colorways",
                       "mixed illustration and photo inside one inset half",
                       "invented spray or mist", "fake steam"],
    "06-relief-scene": ["badges", "arrows", "drawn overlays", "insets of any kind",
                        "looking at camera", "posing", "laughing as the relief",
                        "a situation that costs nothing", "a guarded body", "golden hour",
                        "warm flattering light", "glamour lighting", "beauty retouching",
                        "aspirational travel location", "empty clean street", "styled outfit",
                        "product presented to camera", "product centred or held up",
                        "product hidden inside or under something", "back-of-pack label",
                        "barcode", "bar chart", "arrowheads", "blank expression",
                        "collapsed posture", "saturated colors", "stock photo look"],
}


def opt(letter, tid, varies, ratio, prompt, rationale, variant=None, axes=None,
        notes=None, asset_candidate=None):
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
    if asset_candidate:
        o["asset_candidate"] = asset_candidate
    return o


SLOTS = []

SLOTS.append({
    "slot_id": "hero.image", "section_role": "hero",
    "asset": "73-01-hero-pain-scene.png",
    "placement": "advertorial header, above the byline",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT decides. 01-pain-scene's use_when asks for the moment a cold reader recognises "
        "themselves, and hero.dek names that moment in the copy's own words — ordinary wrap "
        "cuffs, frustrating to fit correctly, every morning. A is the seated one-handed wrap, "
        "which is the action the whole page is written against. B trades the same argument for "
        "a confronting gaze and loses the fumble, and C moves the struggle to the buying "
        "persona, which is a real reader of this page but the second one. PAGE LEGALITY: A "
        "satisfies 06-relief-scene's requires_pair at reasons.items.4 and pairs_with "
        "04-proof-lockedframe at reasons.items.2. EVIDENCE: candid is this type's most-rendered "
        "branch. PRODUCT PRESENCE: none, correctly — the type bans it. PROMPT RISK: 1230 "
        "characters against a measured band of 1379-2153.",
    "options": [
        opt("A", "01-pain-scene", "baseline", "16:9", P_HERO_A,
            "The page's own opening problem, played as one seated action: a woman wrapping her "
            "own cuff one-handed. Evidence is the failed tool in the state that shows it failed "
            "— the twisted band, the folded flap, the kinked tube.",
            variant="candid", axes={"gaze": "candid"}),
        opt("B", "01-pain-scene", "axis: gaze=confront", "16:9", P_HERO_B,
            "The same argument in the type's other gaze. The cell holds one type and the "
            "attribute gates leave no second, so the honest variation here is the axis rather "
            "than a type borrowed from a role it does not belong to.",
            variant="confront", axes={"gaze": "confront"}),
        opt("C", "01-pain-scene", "execution: subject class — the adult child, not the patient",
            "16:9", P_HERO_C,
            "Same type and same axis, different subject class: the second persona in the brief, "
            "the adult daughter doing it for a parent. Two people in frame, and the struggle is "
            "hers.",
            variant="candid", axes={"gaze": "candid"}),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The slot exists to make a cold reader recognise themselves in a held state. "
                  "The wrap IS an action, so the temporal test is arguable here — but the hero's "
                  "declared job is recognition, and page 58 and page 65 both refused a hero on "
                  "the same ground. Refused for consistency with them, not on a fresh reading.",
    },
})

SLOTS.append({
    "slot_id": "reasons.items.0.image", "section_role": "cause",
    "asset": "73-02-reason0-cause-anatomy.png",
    "placement": "reason 1, beside the body copy",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT and the removal test together. Take the fabric cuff out of the left panel and the "
        "narrow crooked contact goes with it, so this is a mechanism and not accumulated damage "
        "(A6). A draws the arm along its length, which is how the copy describes the fault — "
        "straight and at the right tightness. C draws the same argument in cross-section and is "
        "the stronger picture of even contact, but it drops the elbow and the shoulder, and A9 "
        "is explicit that a frame which cannot show the limb loses the argument. B is a "
        "different type and a different sentence: three things tried, none of them working. "
        "EVIDENCE: measure carries 30 renders and verdict 18. PROMPT RISK: 1860 characters "
        "against a ~2050 ceiling at three mark classes.",
    "options": [
        opt("A", "02-cause-anatomy", "baseline", "1:1", P_R0_A,
            "The culprit indicted where it acts: a twisted fabric band meeting the arm along a "
            "narrow strip, against the chamber meeting it evenly. measure spans the contact "
            "band, contour puts the difference on the artery, verdict closes both panels.",
            notes="1:1 centre-cropped to the slot's 4:3 loses 12.5% off the top and bottom; the "
                  "panels run left to right so both lose the same band and the divider survives."),
        opt("B", "04-proof-lockedframe", "type: 04-proof-lockedframe --rivals", "3:2", P_R0_B,
            "The same beat argued by absence: three ordinary wrap monitors on three mornings, "
            "each band come to rest in a different unusable shape, and the product not in frame "
            "at all. It is the 'I tried three things' sentence rather than 'this is what harms "
            "you'.",
            variant="rivals", axes={"camera_lock": "handheld"},
            notes="Picking this displaces reasons.items.2 option A, which is the same type under "
                  "one-type-once. --rivals carries no product photo by its own diff, so this "
                  "option needs no attachment."),
        opt("C", "02-cause-anatomy", "execution: transverse section rather than the arm's length",
            "1:1", P_R0_C,
            "Same type, same marks, the arm seen end-on. Even contact all the way round is far "
            "more legible in section than along the length; what it costs is the elbow and the "
            "shoulder, which is why it is not the recommendation.",
            notes="A9 risk carried deliberately: the section shows no person. Check at thumbnail "
                  "size before shipping."),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The argument IS temporal — a band twisting out of place as it is pulled — and "
                  "this slot would earn motion on its own. The page motion budget spends the "
                  "reasons list's one loop on reasons.items.1, whose mechanism claim is what a "
                  "solution-aware reader is deciding on. Budget, not argument (Step 5d).",
    },
})

SLOTS.append({
    "slot_id": "reasons.items.1.image", "section_role": "how-to-use",
    "asset": "73-03-reason1-mechanism-xray.png",
    "placement": "reason 2, beside the four bullet points",
    "recommended_media": "gif",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT: the section's claim is that the machine does the work — one button, the internal "
        "motor inflates and measures without further input — and 03-mechanism-xray is the only "
        "type in the advertorial column whose subject is the working part itself. A puts the "
        "pump in the body where it really sits; C puts the bladder in the chamber wall, which "
        "is the more directly relevant component but a harder silhouette to keep honest. B "
        "argues posture rather than automation and belongs to reasons_b.items.0's beat. "
        "EVIDENCE: working is 1 of 1. PRODUCT PRESENCE: the product is the whole frame. "
        "recommended_media is gif because the claim is a movement and a still can only assert "
        "it; the still ships today and the loop is the order behind it.",
    "options": [
        opt("A", "03-mechanism-xray", "baseline", "1:1", P_R1_A,
            "The pump, the tube, the sensor board and the battery bay inside a translucent "
            "shell, the pump lit as the working part. It answers 'no manual pumping' by showing "
            "what pumps instead.",
            notes="1:1 centre-cropped to 4:3 loses 12.5% top and bottom; the product is centred "
                  "so the crop eats ground, not shell."),
        opt("B", "03-mechanism-ghostbody", "type: 03-mechanism-ghostbody", "1:1", P_R1_B,
            "The same section argued on the body instead of inside the device: a twisted band "
            "bearing on one narrow length of artery against the chamber carrying the whole "
            "upper arm.",
            notes="Picking this displaces reasons_b.items.0 option A under one-type-once, and "
                  "it also spends the second of the two step-3 slots the page arc allows."),
        opt("C", "03-mechanism-xray", "execution: the bladder in the chamber wall, seen from above",
            "1:1", P_R1_C,
            "Same type, different component and different view. The bladder closing evenly round "
            "the chamber is the part a buyer actually feels; the top-down view is the harder "
            "silhouette for G1 to hold, which is the trade.",
            notes="G1 binds the outer silhouette hard in a translucent shell — check the chamber "
                  "opening against the reference before shipping."),
    ],
    "gif": {
        "eligible": True, "form": "whole-frame", "kind": "mechanism",
        "type_id": "mechanism", "rung": "natural",
        "reason": "The declared reason this section exists is a machine acting on its own — the "
                  "motor inflates and measures without further input. That is a state changing, "
                  "and a still can only assert it. No legislated layer exists in this type's "
                  "skeleton, so the form is whole-frame and the plate is the delivered image.",
        "asset": "73-03-reason1-mechanism-xray--brief.png",
        "refs": "gif-library/mechanism/ — no files filed yet; the folder card carries the law",
        "output": "73-03-reason1-mechanism-xray.mp4",
        "duration_s": 3, "loop": "seamless loop",
        "shot": "side on, chamber and arm",
        "action": "chamber closes, hands stay away",
        "result": "the machine did the pumping",
        "match": "same room and light as still",
        "delivery": "mp4/webm, muted, under the size ceiling",
        "prompt": P_GIF_R1.strip(),
    },
})

SLOTS.append({
    "slot_id": "reasons.items.2.image", "section_role": "comparison",
    "asset": "73-04-reason2-proof-lockedframe.png",
    "placement": "reason 3, beside the body copy",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT: the copy is a comparison in its own words — small reflective screens against a "
        "bright high-contrast one — and --verdict is the advertorial cell's comparison type. A "
        "sets it on a kitchen worktop at standing distance, which is the distance the quote "
        "names, from across the counter. C is the same frame on a bedside table and reads at "
        "arm's length instead, which weakens the without-glasses claim. B leaves the comparison "
        "behind for a single lit render and states size without anyone to judge it. PAGE "
        "LEGALITY: 04-proof-lockedframe pairs_with 01-pain-scene, already on the page. PROMPT "
        "RISK: 1790 characters against a 1800 ceiling.",
    "options": [
        opt("A", "04-proof-lockedframe", "baseline", "3:2", P_R2_A,
            "Three monitors on one worktop across three mornings, judged at standing distance. "
            "The variable is the size of the lit area; nothing is lit, cropped or graded to "
            "favour the last panel.",
            variant="verdict", axes={"camera_lock": "handheld"},
            notes="ADR-021: strict needs compositing, so the panels run handheld with --verdict "
                  "included, exactly as the type's own capability gate says."),
        opt("B", "03-mechanism-xray", "type: 03-mechanism-xray", "1:1", P_R2_B,
            "The screen argued from inside: the backlight panel lit evenly across an area "
            "plainly wider than the housing. It states the size without a second product to "
            "judge it against, which is why it is not the recommendation on a comparison beat.",
            notes="Picking this displaces reasons.items.1 option A under one-type-once."),
        opt("C", "04-proof-lockedframe", "execution: bedside table at arm's length, evening",
            "3:2", P_R2_C,
            "Same type and variant, a different room and distance. Legibility at arm's length "
            "under lamplight is a real reading of the section, but the copy's own distance is "
            "across the counter.",
            variant="verdict", axes={"camera_lock": "handheld"}),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "A locked-frame comparison is inspected, not watched — the reader's eye does "
                  "the travelling between panels. A rung-2 restaging IS available here and is "
                  "named rather than hidden: one continuous frame, the backlight coming on and "
                  "the lit field resolving at counter distance, which would argue legibility as "
                  "a change and would put a result loop on the page. It is declined on two "
                  "counts. The reasons list has already spent its one loop, and Step 5d says a "
                  "page whose natural pair is two working loops keeps it rather than restaging "
                  "a strong slot to fill a column.",
    },
})

SLOTS.append({
    "slot_id": "reasons.items.3.image", "section_role": "outcome",
    "asset": "73-05-reason3-relief-hero.png",
    "placement": "reason 4, beside the body copy",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT: the section sells the state after — separate profiles, stored history, no paper "
        "notebook — and 06-relief-hero's recall inset is the one layer in the library built to "
        "hold the past beside the present. A puts the notebook of handwritten figures in that "
        "inset, which is the thing the copy says is replaced. B puts a collapsed wrap cuff "
        "there instead, which is reason 1's argument arriving late. C reaches the four-user "
        "claim through two forearms rather than one person, which is truer to the section and "
        "costs the expression that carries relief. PAGE LEGALITY: pairs_with 01-pain-scene, on "
        "the page at hero. EVIDENCE: past 2/2, step 2/2 when described by its endpoints.",
    "options": [
        opt("A", "06-relief-hero", "baseline", "1:1", P_R3_A,
            "One man mid-reading, the lit face carrying the output, and a greyed recall panel "
            "holding the notebook of handwritten figures the device replaces, joined by the one "
            "sanctioned arrow.",
            axes={"register": "commercial", "inset_mode": "recall", "inset_motion": "still"},
            notes="G10 risk: a corner layer on a 1:1 render centre-cropped to 4:3 loses 12.5% "
                  "top and bottom. The prompt names a visible margin, but check the panel "
                  "survives the crop before the asset ships."),
        opt("B", "06-relief-hero", "axis: register=ugc", "1:1", P_R3_B,
            "The same structure in the phone-photo register, and the recall panel holds the "
            "collapsed fabric cuff instead of the notebook. Trust rather than polish; the past "
            "cell repeats reason 1's argument, which is the cost.",
            axes={"register": "ugc", "inset_mode": "recall", "inset_motion": "still"},
            notes="Same corner-layer crop risk as A."),
        opt("C", "06-relief-hero", "execution: reduced subject — two forearms, no face",
            "1:1", P_R3_C,
            "Same type and axes, the subject reduced to two forearms of different ages at one "
            "table. Two users is the section's actual claim and this is the only option that "
            "shows two; what it gives up is the expression that carries the relief.",
            axes={"register": "commercial", "inset_mode": "recall", "inset_motion": "still"},
            notes="Same corner-layer crop risk as A."),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The slot's reason to exist is a held state — records that stay separate, a "
                  "history that is simply there. Nothing transitions. Cycling through four "
                  "stored profiles on the screen would be a reveal of what exists rather than a "
                  "change, and revealing does not earn motion.",
    },
})

SLOTS.append({
    "slot_id": "reasons.items.4.image", "section_role": "proof",
    "asset": "73-06-reason4-relief-scene.png",
    "placement": "reason 5, beside the body copy",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT: the section carries two claims — the box is complete, and the thing is compact "
        "enough to live on a counter and travel. A takes the travel half into the world, which "
        "is what 06-relief-scene exists for; its own words are that the promise ends in the "
        "world and the type is never set at home. B takes the completeness half literally, on "
        "the worktop with the adapter uncoiled, and is the better answer if the owner wants the "
        "box contents argued. C is A in a station rather than outside a health centre. PAGE "
        "LEGALITY: requires_pair 01-pain-scene is satisfied at hero — this option is illegal "
        "without it. PROMPT RISK: 1520 characters.",
    "options": [
        opt("A", "06-relief-scene", "baseline", "4:3", P_R4_A,
            "The monitor travelling in an open bag out of a health centre, the man's hands free "
            "and his shoulders down at a kerb he would once have crossed gripping the card.",
            axes={"gaze": "candid", "inset_mode": "none"},
            notes="requires_pair: 01-pain-scene must stay on the page. If hero.image is ever "
                  "rerouted away from 01-pain-scene, this option becomes illegal and the slot "
                  "falls to option B. 4:3 is declared by this type, so no crop."),
        opt("B", "06-relief-hero", "type: 06-relief-hero", "1:1", P_R4_B,
            "The completeness claim taken literally: hands setting the device down beside a "
            "socket with the adapter uncoiled to its full length and the carton open behind. "
            "The reduced subject is chosen because the result is more legible than the user.",
            axes={"register": "ugc", "inset_mode": "none"},
            notes="Picking this displaces reasons.items.3 option A under one-type-once."),
        opt("C", "06-relief-scene", "execution: a station platform rather than a health centre",
            "4:3", P_R4_C,
            "Same type and axes, a different public place, and the product travelling in a case "
            "pocket rather than a shoulder bag. Portability reads harder at a platform; the "
            "health-centre frame ties the relief to the reason for owning it.",
            axes={"gaze": "candid", "inset_mode": "none"},
            notes="Same requires_pair condition as A."),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "A complete box and a neat footprint are held states a reader inspects. "
                  "Nothing flows and nothing changes; a loop over a device sitting on a counter "
                  "would be ambient, which Step 5d switches off by default.",
    },
})

SLOTS.append({
    "slot_id": "reasons_b.items.0.image", "section_role": "mechanism",
    "asset": "73-07-reasonb0-mechanism-ghostbody.png",
    "placement": "reason 6, beside the body copy",
    "recommended_media": "still",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT: this section states a boundary and then gives the reader an action — sit at a "
        "standard table with the upper arm at roughly heart level. A draws exactly that "
        "geometry, the heart and the arm in one cross-section, which no other type on the page "
        "can hold. C draws the other half of the section, the arm that is too thick for a fixed "
        "chamber, and it is the more honest picture of the limit but the less actionable one. B "
        "is the same argument as a 2D illustration and duplicates reasons.items.0's register. "
        "PAGE LEGALITY: this is the second and last of the step-3 budget's two slots. EVIDENCE: "
        "every mark in this type is thin — structure 2 renders, support 3 as an overlay.",
    "options": [
        opt("A", "03-mechanism-ghostbody", "baseline", "1:1", P_RB0_A,
            "Two seated mannequins in section, one at a low table with the arm below the heart "
            "and one at a standard table with the arm level with it and the device in place. "
            "The posture instruction drawn rather than written.",
            notes="1:1 centre-cropped to 4:3 loses 12.5% top and bottom; the panels run left to "
                  "right so both lose the same band. The badges sit in the top corners — check "
                  "they survive the crop."),
        opt("B", "02-cause-anatomy", "type: 02-cause-anatomy", "1:1", P_RB0_B,
            "The same heart-level argument as a flat 2D illustration, with a neutral datum line "
            "per panel and the measure lines spanning heart to arm.",
            notes="Picking this displaces reasons.items.0 option A under one-type-once."),
        opt("C", "03-mechanism-ghostbody", "execution: arm circumference rather than heart level",
            "1:1", P_RB0_C,
            "Same type, the other half of the section: a thick upper arm filling the fixed "
            "chamber against a standard one with an even margin. It is the plainest statement "
            "of the boundary and the least actionable for a reader who fits.",
            notes="Same crop note as A. A2 check: this marks what IS, a section pressed flat "
                  "against the wall — not what would happen."),
    ],
    "gif": {
        "eligible": False, "form": "none",
        "reason": "The argument is a shape holding — an arm level with a heart, an arm that fits "
                  "or does not. This type's own avoid_when refuses a loop where the section's "
                  "argument is a shape holding still rather than a part moving.",
    },
})

SLOTS.append({
    "slot_id": "reasons_b.items.1.image", "section_role": "how-to-use",
    "asset": "73-08-reasonb1-use-sequence.png",
    "placement": "reason 7, beside the three numbered steps",
    "recommended_media": "gif",
    "recommended_opt": "A",
    "recommendation_basis":
        "FIT is exact: the copy is three numbered steps and 03-use-sequence is three stacked "
        "panels read by action logic alone. A runs the steps as the patient's own hands, which "
        "is what the section's quote describes — part of my normal breakfast routine. C runs "
        "them as a carer's hands on someone else's arm, which serves the second persona and "
        "puts two people in a slot the type keeps to one pair of hands. B is not a sequence at "
        "all. PAGE LEGALITY: pairs_with 03-mechanism-ghostbody, already at reasons_b.items.0, "
        "and it is the second of the two step-3 slots. PROMPT RISK: 1290 characters against a "
        "hard 1500 ceiling — this type loses its layout to length before anything else.",
    "options": [
        opt("A", "03-use-sequence", "baseline", "3:4", P_RB1_A,
            "Slide the arm in, press the button, let go — one action per panel, one pair of "
            "hands, one table, one light, and the adapter left on the table as the closing "
            "residue.",
            axes={"camera_lock": "handheld"},
            notes="3:4 centre-cropped to the slot's 4:3 loses a lot of height and this type is "
                  "a vertical stack. Render at 3:4 and set the slot to a taller aspect, or the "
                  "top and bottom panels will be cut."),
        opt("B", "03-mechanism-xray", "type: 03-mechanism-xray", "1:1", P_RB1_B,
            "The three steps compressed into the one thing they add up to: the bladder closed "
            "evenly round the chamber. It states the outcome of the sequence, not the sequence.",
            notes="Picking this displaces reasons.items.1 option A under one-type-once."),
        opt("C", "03-use-sequence", "execution: a carer's hands on an older person's arm",
            "3:4", P_RB1_C,
            "Same type and structure, the second persona doing the steps for a parent. The "
            "closing panel resolves on a hand over a wrist rather than on the device.",
            axes={"camera_lock": "handheld"},
            notes="Two people in frame is at the edge of this type's continuity law — the older "
                  "forearm is the only part of the second person that ever appears. Same 3:4 "
                  "crop caution as A."),
    ],
    "gif": {
        "eligible": True, "form": "whole-frame", "kind": "use",
        "type_id": "use", "rung": "natural",
        "reason": "An ordered sequence is the definition of temporal, and this is the strongest "
                  "motion candidate on the page — the section is literally three steps. This "
                  "type's skeleton legislates stacked panels and no inset layer, so the form is "
                  "whole-frame and the loop replaces the stack.",
        "asset": "73-08-reasonb1-use-sequence--brief.png",
        "refs": "gif-library/use/ — no files filed yet; the folder card carries the law",
        "output": "73-08-reasonb1-use-sequence.mp4",
        "duration_s": 4, "loop": "seamless loop",
        "shot": "over the table, hands and device",
        "action": "arm slides in, finger presses, hand leaves",
        "result": "three steps, no wrapping",
        "match": "one light, one palette throughout",
        "delivery": "mp4/webm, muted, under the size ceiling",
        "prompt": P_GIF_RB1.strip(),
    },
})

WALL = [
    ("reviews.photos.0.image", "73-09-review-1.png", P_W0,
     "in-use · kitchen table · cool morning window light · seated half-metre",
     "Mode in-use on a kitchen table, the mother's own forearm in the chamber. Cool morning "
     "daylight, seated distance, mug as the single anchor."),
    ("reviews.photos.1.image", "73-10-review-2.png", P_W1,
     "at-rest · bedroom nightstand · warm lamplight · standing quarter-metre",
     "Mode at-rest on a nightstand under warm lamplight, factory sticker still on. Closest "
     "camera distance in the set, coiled charging cable as the anchor."),
    ("reviews.photos.2.image", "73-11-review-3.png", P_W2,
     "in-use · living room side table · flat neutral overcast · seated third-metre",
     "Mode in-use on a living room side table under flat overcast light, fingers on the start "
     "button. Television remote as the anchor."),
    ("reviews.photos.3.image", "73-12-review-4.png", P_W3,
     "kit-flatlay · dining table · warm kitchen overhead · standing three-quarter-metre",
     "The only kit-flatlay in the set: the opened carton, the adapter and the batteries as the "
     "owner left them. Manual page as the anchor, its print illegible at size."),
    ("reviews.photos.4.image", "73-13-review-5.png", P_W4,
     "at-rest · hallway console · mixed warm-dim evening · standing half-metre",
     "Mode at-rest on a hallway console in mixed dim evening light, pushed back against the "
     "wall. Keys as the anchor."),
    ("reviews.photos.5.image", "73-14-review-6.png", P_W5,
     "in-use · home office desk · cool midday daylight · standing metre, top-down",
     "Mode in-use on a desk seen from above at the widest distance in the set. Extension plug "
     "as the anchor."),
]

for sid, asset, prompt, varies, rationale in WALL:
    SLOTS.append({
        "slot_id": sid, "section_role": "social-proof",
        "asset": asset, "placement": "review wall tile",
        "recommended_media": "still",
        "recommended_opt": "A",
        "recommendation_basis":
            "One option, not three (ADR-022). The six tiles are the unit of variation and the "
            "SET DIVERSITY LAW spends it between them: room class, surface, light temperature, "
            "camera distance and content mode all differ across the six. Three options inside "
            "one tile would spend that budget where it buys nothing and would let a reader pick "
            "one register on some tiles and another on the rest, which reads as two shoots and "
            "so as fake.",
        "options": [
            opt("A", "05-social-snapshot", varies, "1:1", prompt, rationale,
                axes={"register": "ugc"},
                notes="PRECONDITION, and it is not optional: this tile sits inside the same "
                      "reviews block as six named attributions carrying five-star rows and "
                      "Verified Buyer labels. 05-social-snapshot's authenticity fence forbids "
                      "pairing a generated snapshot with a reviewer name, star row or verified "
                      "badge. Use a real customer photograph, or move the photo grid out of the "
                      "attributed block, or drop the names, stars and verified labels — before "
                      "rendering this."),
        ],
        "gif": {
            "eligible": False, "form": "none",
            "reason": "No social-proof slot carries motion (Step 5d, owner instruction "
                      "2026-08-19). The mechanism is the six-type set: it carries no social "
                      "type, so this slot has no gif type to file a loop under, and the review "
                      "wall is the strictest case of that rule.",
        },
    })

# ---------------------------------------------------------------- out of scope

OUT_OF_SCOPE = [
    ("scarcity.image", "offer band", "cta"),
    ("scarcity.badge_image", "offer badge", "cta"),
    ("rail.image", "sticky proof rail", "cta"),
    ("guarantee.badge_image", "guarantee band", "cta"),
    ("header.logo", "masthead", "cta"),
    ("footer.logo", "footer", "cta"),
    ("hero.author_avatar", "byline", "author"),
    ("closing.bio_image", "closing bio", "author"),
] + [(f"comments.items.{i}.avatar", f"comment {i + 1}", "social-proof") for i in range(7)]

for sid, place, role in OUT_OF_SCOPE:
    reason = ("A standard product shot or brand furniture; the library covers argument images, "
              "not offer and masthead assets.")
    if role == "author" or sid.startswith("comments."):
        reason = ("A portrait of a named person. No library type produces one, and generating a "
                  "face to sit under a real byline or a named comment is a disclosure decision "
                  "rather than an image one (slot-rules.md, the author row).")
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
    "groups_covered": ["working"],
    "shortfall_reason": None,
    "notes": [
        "Floor met at exactly 2, both loops earned at rung 1 with no re-execution needed.",
        "COVERAGE PAIR NOT MET, and it cannot be met on this page without breaking the "
        "spacing rule. Both delivered loops are `working` (mechanism at reasons.items.1, use "
        "at reasons_b.items.1). Every result-capable candidate — the backlight resolving at "
        "reasons.items.2 — sits inside the `reasons` list, which has already spent its one "
        "loop. Step 5d makes coverage a preference and says a page whose natural pair is two "
        "working loops keeps it rather than restaging a strong slot to fill a column.",
        "Spacing: the `reasons` list counts as ONE section (ADR-024), so reasons.items.0 loses "
        "a loop it would otherwise have earned on its own argument. Its verdict says budget, "
        "not argument.",
        "Review wall: 0 tiles, and not by budget — the six-type set carries no `social` type, "
        "so those slots have nothing to file a loop under.",
        "Both loops are whole-frame. No type on this page legislates an inset layer that a "
        "plate could occupy, so `inset` was never available.",
    ],
}

COVERAGE = {
    "covered": [
        "step 1 pain — 01-pain-scene at hero.image",
        "step 2 cause — 02-cause-anatomy at reasons.items.0",
        "step 3 mechanism — 03-mechanism-xray at reasons.items.1 and 03-mechanism-ghostbody at "
        "reasons_b.items.0, with 03-use-sequence at reasons_b.items.1",
        "step 4 proof — 04-proof-lockedframe --verdict at reasons.items.2",
        "step 5 social — 05-social-snapshot across all six review tiles",
        "step 6 relief — 06-relief-hero at reasons.items.3 and 06-relief-scene at "
        "reasons.items.4",
    ],
    "absent": [
        "step 2 symptom breadth — 02-symptom-rail is not advertorial-legal and the page makes "
        "no breadth claim",
        "step 5 persona — 05-persona-grid declares no advertorial channel, so the personas beat "
        "has no type on this channel at all",
    ],
    "notes": [
        "Every rung of the Trust Ladder is covered, which is unusual and is a property of the "
        "page rather than of the routing — a seven-reason listicle with a limits section and a "
        "how-to section reaches further down the ladder than most.",
        "Awareness stage read from the copy, not from a declared field: SOLUTION-AWARE. The "
        "hero assumes the reader already owns or has tried a wrap cuff and is comparing the "
        "way it is fitted; the intro names the solution class in its second sentence and never "
        "argues that home monitoring is worth doing. brief.awarenessStage says `solution`, and "
        "the copy agrees with it.",
        "For a solution-aware reader the deciding rungs are mechanism and physical proof, and "
        "both are covered twice. Re-amplifying the problem would insult this reader, which is "
        "why the pain beat is confined to the hero and reason 1 and never returns.",
    ],
}

RECOMMENDED = []

NOTES = [
    "CHANNEL. lpTypeId is `listicle`, which is not one of the four channels in "
    "registry/vocabulary.yaml. Routed as `advertorial` on the page's own evidence: a bylined "
    "author with a credential line, an About-the-author bio, a seven-comment thread with names, "
    "an `Advertorial` disclosure line and editorial footer navigation. A listicle is an "
    "advertorial format, not a fifth channel. Same call as page 65.",
    "THE PRODUCT'S OUTPUT IS A SCREEN, AND THAT CONSTRAINS EVERY LAYER ON THE PAGE. "
    "product.attributes.visible_output is the reading itself — systolic, diastolic and pulse on "
    "a backlit display — so G8 binds and the output has to carry. But G6 bans model-drawn text "
    "and digits, and ADR-021 says this pipeline cannot composite, so no render here may show a "
    "legible reading. Every prompt that includes the device therefore lights the screen and "
    "states that it carries no characters, numerals or symbols: the output is the LIT FIELD, "
    "not the numbers. Where a real reading matters — the review tiles — the face is turned "
    "away or dark instead, which is what 05-social-snapshot's own constraint requires when the "
    "renderer cannot composite. This is the single largest constraint on this page and it is "
    "worth the owner knowing before the first render.",
    "THE REVIEWS BLOCK BREAKS 05-social-snapshot's AUTHENTICITY FENCE AS THE PAGE IS BUILT. All "
    "six photo slots sit inside the same reviews section as six quotes, each carrying a "
    "five-star row, a named attribution and a green Verified label. The type forbids pairing a "
    "generated snapshot with any of those. Every review prompt carries the precondition. Three "
    "ways out, in order of preference: real customer photographs; or move the photo grid out of "
    "the attributed block; or drop the names, stars and verified labels. Same finding as page "
    "65, unchanged by anything in this export.",
    "THE TEMPLATE ASKS FOR 4:3 AND THE LIBRARY BARELY HAS IT. The seven body slots carry a 4:3 "
    "placeholder and only 05-social-snapshot and 06-relief-scene declare 4:3. The slots are "
    "routed by ARGUMENT and rendered at the chosen type's own declared ratio, and each option "
    "says what its crop costs. reasons.items.4 is the one body slot that needs no crop at all. "
    "reasons_b.items.1 is the worst case: a vertical three-panel stack at 3:4 cropped to 4:3 "
    "loses the top and bottom panels, so that slot should be set to a taller aspect in the "
    "template rather than centre-cropped.",
    "THE REFERENCE PHOTO IS YOURS TO UPLOAD. imageBriefs and shopifyProductGid are both null in "
    "the export, so there is no product photograph in it and nothing to hash. `attachments` is "
    "omitted from every option rather than filled with an invented sha256 (SPEC 6.4). That is a "
    "gap in the export, not a blocked prompt: 26 of the 29 prompts keep their G1 reference "
    "block and run as written once you paste them and upload the photo.",
    "ONE-TYPE-ONCE WAS THE BINDING CONSTRAINT AND THE COLUMN ONLY JUST COVERS THE PAGE. Eight "
    "linear slots needed eight distinct types from an advertorial column of ten, and "
    "05-social-handoff and 01-pain-split are the only two left unused — the first because no "
    "section carries a recommendation beat between two people, the second because it declares "
    "no advertorial channel. Option B carries a different type on seven of the eight linear "
    "slots and each says which slot it would displace; hero.image is the exception and varies "
    "on the gaze axis instead, because its cell holds exactly one type.",
    "THE STEP-3 BUDGET IS FULL. Cross-slot rule 4 allows at most two of ghostbody, spec-split "
    "and use-sequence, and this page spends both: 03-mechanism-ghostbody at reasons_b.items.0 "
    "and 03-use-sequence at reasons_b.items.1. 03-mechanism-xray is outside that set, which is "
    "what makes three step-3 images legal here.",
    "PERSONAS HAS NO TYPE ON THIS CHANNEL. reasons_b.items.0 reads most naturally as a personas "
    "beat — who this fits, what arm size, what table — and 05-persona-grid declares no "
    "advertorial channel, so the row is empty by the type's own admission and not merely by the "
    "table. The slot is routed as `mechanism` instead and argues the posture the section makes "
    "actionable. Recorded because it will recur on every advertorial that carries a fit "
    "section.",
    "MOTION. Floor 2, ceiling 5, delivered 2, both at rung 1. The coverage pair is not met and "
    "cannot be on this page — see the motion block for why. Nothing was restaged to fill the "
    "result column, which is Step 5d's own instruction rather than a shortfall.",
    "NO PICK PRIOR WAS AVAILABLE. feedback/picks.jsonl is empty, so the 20-pick tie-breaker in "
    "SPEC 7.7 never fired and every recommendation here rests on fit, page legality, render "
    "evidence, product presence and prompt risk alone. These recommendations make the page "
    "argument-complete; they are not conversion-optimised and nothing here is performance-backed.",
    "SIX PROMPTS SIT OVER THEIR TYPE'S MEASURED REFERENCE SIZE AND ARE SHIPPED THAT WAY, said "
    "here rather than left for the reader to find. 02-cause-anatomy gives ~2050 characters at "
    "three mark classes and reasons.items.0 option A runs 2103 with option B at reasons_b at "
    "2114, both about 3% over; 04-proof-lockedframe gives 1800 and its two --verdict options "
    "run about 1940, 8% over; 03-mechanism-ghostbody's trimmed prompts run about 2250 at "
    "reasons_b.items.0. What is left in each is earned — the measure and verdict marks are "
    "required by their skeletons, the fairness clauses are --verdict's own recorded faults, "
    "and the ghostbody prompts carry the four ghost negatives and the palette lock that were "
    "RESTORED at 2.1 after cutting them broke the next render. 03-use-sequence is the one "
    "ceiling that was not allowed to slip: it is measured at 1533 characters holding the "
    "layout 4 times in 6 against 2054 holding it once in 8, so both of its options were "
    "trimmed back under 1500 before shipping.",
    "Ratio goes in the generation tool's own aspect-ratio parameter, never in the prompt text "
    "(adapters/nano-banana.md Rule 4). No `Strictly avoid:` line is rendered into any prompt "
    "(ADR-014); the exclusion list is kept in each option's `avoid` field for a model with a "
    "real negative channel.",
]

OUT = {
    "page_id": PAGE,
    "registry_version": "2.0.0",
    "channel": "advertorial",
    "awareness_stage": "solution-aware",
    "slots": SLOTS,
    "coverage": COVERAGE,
    "recommended": RECOMMENDED,
    "motion": MOTION,
    "page_composition_notes": NOTES,
}

# ---------------------------------------------------------------- self-checks

def checks():
    errs, warns = [], []
    routed = [s for s in SLOTS if s.get("options")]

    for s in SLOTS:
        sid = s["slot_id"]
        if sid not in DECLARED:
            errs.append(f"{sid}: not in content.json")
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
            chans = TYPES[o["type"]].get("channels", "")
            if "advertorial" not in chans:
                errs.append(f"{sid} {o['opt']}: {o['type']} is not advertorial-legal")
            if TYPES[o["type"]].get("requires_product_photo") is True and \
                    "the exact reference" not in o["prompt"] and o.get("variant") != "rivals":
                errs.append(f"{sid} {o['opt']}: {o['type']} requires a product photo but the "
                            "prompt carries no reference block")

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
    dupes = {t for t in picked if picked.count(t) > 1}
    if dupes:
        errs.append(f"one-type-once breached in the recommended set: {sorted(dupes)}")

    # step-3 budget
    step3 = {"03-mechanism-ghostbody", "03-spec-split", "03-use-sequence"}
    n3 = len([t for t in picked if t in step3])
    if n3 > 2:
        errs.append(f"step-3 budget: {n3} of the capped three types, max 2")

    # requires_pair
    for s in linear:
        for o in s["options"]:
            rp = TYPES[o["type"]].get("requires_pair")
            if rp and rp != "null" and rp not in picked:
                errs.append(f"{s['slot_id']} {o['opt']}: requires_pair {rp} not on the page")

    # never_with
    for t in picked:
        nw = TYPES[t].get("never_with", "")
        for other in picked:
            if other != t and other in nw:
                errs.append(f"never_with breached: {t} and {other}")

    # motion budget, recomputed rather than trusted
    elig = [s for s in SLOTS if s.get("gif", {}).get("eligible")]
    if len(elig) != MOTION["delivered"]:
        errs.append(f"motion.delivered says {MOTION['delivered']}, {len(elig)} slots eligible")
    if len(elig) < MOTION["floor"] and not MOTION["shortfall_reason"]:
        errs.append("below the motion floor with no shortfall_reason")
    if len(elig) > MOTION["ceiling"]:
        errs.append(f"motion ceiling {MOTION['ceiling']} exceeded: {len(elig)}")

    def section_of(sid):
        return sid.split(".")[0]

    secs = {}
    for s in elig:
        secs.setdefault(section_of(s["slot_id"]), []).append(s["slot_id"])
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
        if not g["output"].endswith(".mp4"):
            errs.append(f"{s['slot_id']}: gif.output must be an mp4")
        if g["output"] != s["asset"].replace(".png", ".mp4"):
            errs.append(f"{s['slot_id']}: gif.output must be the slot asset with an mp4 "
                        f"extension (got {g['output']})")
        for line in ("shot", "action", "result", "match"):
            if len(g[line].split()) > 7:
                errs.append(f"{s['slot_id']}: brief line `{line}` is over seven words (G12)")

    # social slots carry no motion
    for s in SLOTS:
        if s["section_role"] == "social-proof" and s.get("gif", {}).get("eligible"):
            errs.append(f"{s['slot_id']}: a social-proof slot carries motion (Step 5d)")

    # review wall: one option each, and the SET DIVERSITY LAW
    wall = [s for s in SLOTS if s["slot_id"].startswith("reviews.")]
    for s in wall:
        if len(s["options"]) != 1:
            errs.append(f"{s['slot_id']}: repeating section must emit one option (ADR-022)")
    axes_seen = {"room": [], "mode": []}
    for s in wall:
        v = s["options"][0]["varies_on"]
        parts = [p.strip() for p in v.split("·")]
        axes_seen["mode"].append(parts[0])
        axes_seen["room"].append(parts[1])
    for name, vals in axes_seen.items():
        if name == "room" and len(set(vals)) != len(vals):
            errs.append(f"SET DIVERSITY: repeated {name} across the wall: {vals}")
    if len(set(axes_seen["mode"])) < 3:
        warns.append(f"SET DIVERSITY: only {len(set(axes_seen['mode']))} content modes across "
                     "six tiles")

    return errs, warns


# ---------------------------------------------------------------- emit

def render_md():
    L = []
    routed = [s for s in SLOTS if s.get("options")]
    n_opts = sum(len(s["options"]) for s in routed)
    n_gif = len([s for s in SLOTS if s.get("gif", {}).get("eligible")])
    L.append("# Image prompts — page 73, automatic upper arm blood pressure monitor")
    L.append("")
    L.append("GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit "
             "the script and re-run.")
    L.append("")
    L.append(f"- page_id `{PAGE}` · channel `advertorial` · awareness `solution-aware` · "
             f"registry `2.0.0`")
    L.append(f"- {len(SLOTS)} image slots: {len(routed)} routed, "
             f"{len(SLOTS) - len(routed)} out of library scope")
    L.append(f"- {n_opts + n_gif} prompts: {n_opts} options plus {n_gif} G12 brief plates")
    L.append(f"- {n_gif} slots earn motion, each carrying a brief plate as a fourth option "
             "below C — a work order the editor renders alongside the still, never a prompt "
             "that animates one (ADR-020)")
    L.append("")
    L.append("## Read this first")
    L.append("")
    for n in NOTES:
        L.append(f"- {n}")
    L.append("")
    L.append("## Motion budget (Step 5d)")
    L.append("")
    L.append(f"- floor **{MOTION['floor']}** · ceiling **{MOTION['ceiling']}** · delivered "
             f"**{MOTION['delivered']}** · groups covered "
             f"**{', '.join(MOTION['groups_covered'])}**")
    for n in MOTION["notes"]:
        L.append(f"- {n}")
    L.append("")
    L.append("## Coverage")
    L.append("")
    L.append("**Covered**")
    L.append("")
    for c in COVERAGE["covered"]:
        L.append(f"- {c}")
    L.append("")
    L.append("**Absent**")
    L.append("")
    for c in COVERAGE["absent"]:
        L.append(f"- {c}")
    L.append("")
    for c in COVERAGE["notes"]:
        L.append(f"- {c}")
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
            L.append(f"- ratio `{o['ratio']}` · pipeline `{o['pipeline']}` · type version "
                     f"`{o['type_version']}`")
            if o.get("axes"):
                L.append("- axes: " + ", ".join(f"`{k}: {v}`" for k, v in o["axes"].items()))
            L.append(f"- attachment: {'the product photo, uploaded by hand' if TYPES[o['type']].get('requires_product_photo') is True and o.get('variant') != 'rivals' else 'none'}")
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
            L.append(f"- form `{g['form']}` · kind `{g['kind']}` · gif type `{g['type_id']}` · "
                     f"rung `{g['rung']}`")
            L.append(f"- reference folder: {g['refs']}")
            L.append(f"- **the editor returns** `{g['output']}` · delivery {g['delivery']}")
            L.append(f"- plate render asset `{g['asset']}` — production only, never a page asset")
            L.append(f"- {g['reason']}")
            L.append("")
            L.append("```")
            L.append(g["prompt"])
            L.append("```")
            L.append("")
        else:
            L.append(f"### {s['slot_id']} · no motion")
            L.append("")
            L.append(f"- {g.get('reason', '')}")
            L.append("")
    L.append("---")
    L.append("")
    L.append("## Out of library scope")
    L.append("")
    for s in SLOTS:
        if s.get("out_of_scope_reason"):
            L.append(f"- `{s['slot_id']}` ({s['placement']}) — {s['out_of_scope_reason']}")
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

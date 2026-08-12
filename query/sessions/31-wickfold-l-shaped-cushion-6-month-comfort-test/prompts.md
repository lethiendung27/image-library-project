# Image prompts — page 31 · wickfold L-shaped cushion 6-month test

Generated from `content.json` by `query/runbook.md`. **This file is rendered from `prompts.json`; never edit it by hand.**

- **Channel:** advertorial
- **Awareness (read from copy):** solution-aware
- **Registry:** unknown
- **Slots:** 14 (12 routed, 2 asset-routed)
- **Recommended additions:** 1

## Asset manifest

| asset | slot | role | type (option A) |
|---|---|---|---|
| `01-hero-relief-hero.png` | `hero.image` | hero | `06-relief-hero` |
| `02-problem-pain-scene.png` | `problems.items.0.image` | pain | `01-pain-scene` |
| `03-sixmonth-timelapse.png` | `problems.items.1.image` | proof | `04-proof-lockedframe` |
| `04-feature-two-piece-cause.png` | `features.items.0.image` | cause | `02-cause-anatomy` |
| `05-feature-pelvic-gap-ghostbody.png` | `features.items.1.image` | mechanism | `03-mechanism-ghostbody` |
| `06-feature-foam-core-xray.png` | `features.items.2.image` | mechanism | `03-mechanism-xray` |
| `07-feature-base-grip-xray.png` | `features.items.3.image` | spec | `03-mechanism-xray` |
| `08-feature-fit-use-sequence.png` | `features.items.4.image` | use | `03-use-sequence` |
| `09-review-shot-car.png` | `reviews.shots.0.image` | social | `06-relief-hero` |
| `10-review-shot-office.png` | `reviews.shots.1.image` | social | `06-relief-hero` |
| `11-review-shot-handoff.png` | `reviews.shots.2.image` | social | `05-social-handoff` |
| `12-review-shot-passenger.png` | `reviews.shots.3.image` | social | `06-relief-hero` |
| `(supplied)` | `product.image` | offer | `— supplied —` |
| `(supplied)` | `product_end.image` | offer | `— supplied —` |
| `13-closing-relief-scene.png` | `recommended.closing-relief-scene` *(proposed)* | relief | `06-relief-scene` |

## Page composition notes

1. Channel advertorial, read from page.lpTypeId and confirmed by the register: editorial byline, disclosure line, 'Updated October 15, 2026', six-month test framing.
2. Awareness read as SOLUTION-AWARE from the copy itself, not from a declared field. Basis: the hero opens 'Seat cushions are easy to buy badly' and indicts flat foam and separate pillows by name, so the reader is assumed to own the problem AND to have already tried the solution class; problems.items.0 is titled 'Why most seat cushions end up in the closet', which is a failure-of-the-category argument, not a pain-recognition one. brief.awarenessStage independently says 'solution' — corroboration, not the source.
3. Consequence of that reading: mechanism and physical proof decide this reader, and re-amplifying the problem insults them. The page gets ONE pain beat (problems.items.0) and nothing pain-coded appears after problems.items.1, per cross-slot rule 3.
4. 05-social-snapshot is BARRED from all four reviews.shots slots. That section displays reviewer names and verified labels, and the snapshot AUTHENTICITY FENCE forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. This is an FTC line, not a style preference — the four shots route to 06-relief-hero --ugc and 05-social-handoff instead.
5. Repetition is legal but heavy and worth seeing plainly: 06-relief-hero appears at hero.image and at three reviews.shots slots, 03-mechanism-xray twice inside features.items, 02-cause-anatomy twice inside features.items. Cross-slot rule 2's repeating-section exception covers the within-section repeats; the hero-to-reviews reuse is ladder rung 4 and is named in each varies_on.
6. Step-3 budget (cross-slot rule 4) allows at most two of {03-mechanism-ghostbody, 03-spec-split, 03-use-sequence}. The page uses ghostbody and use-sequence — exactly at the cap. 03-mechanism-xray is not in that named set because it postdates the rule, but with two xray executions the page carries four step-3 images in total. That is at the edge of 'three is a lecture' and is the first thing to cut if the section feels didactic.
7. features.items.3 (non-slip base) has no active type: its natural fit 03-spec-macro is STAGING at 4/5 exemplars and staging is never routable. Resolved by ladder rung 4, not by inventing a type.
8. 03-mechanism-xray carries a recorded fit tension at features.items.2 and .3: its use_when names gadget-class products that do NOT act on a body structure, and this cushion does. Admitted because the subject in both is the product's own material structure rather than the body interface. Flagged rather than hidden.
9. product.image and product_end.image carry route: asset in the export — supplied product photography, not generation requests. They are not library refusals; nothing asked the library for an image. Cross-slot rule 6 also puts a standard packshot outside library scope. Say the word and either gets a generated option.
10. Four of the fourteen export slots declare route: figma (features 0, 1, 4 and problems 1). Three of those route cleanly to illustration types. features.items.4's dimension blueprint does not — it is spec numerals, which G6 sends to post-composite, and its natural type 03-spec-explode is staging. It is routed to 03-use-sequence instead, which answers the same 'will it fit my seat' question photographically.
11. HONEST LIMIT: this pass makes the page argument-complete. It cannot make it conversion-optimised. feedback/picks.jsonl holds 0 records, so the >=20-pick tie-breaker in Step 6 never fired and nothing here is performance-backed.
12. Nothing in this run has been rendered. Every claim is about what the prompts ask for, not about what came back.

## Coverage

**Covered:** 1 pain — 01-pain-scene; 2 cause — 02-cause-anatomy; 3 mechanism — 03-mechanism-ghostbody, 03-mechanism-xray, 03-use-sequence; 4 proof — 04-proof-lockedframe --timelapse; 5 social — 05-social-handoff; 6 relief — 06-relief-hero

**Gaps:** No rung is absent, so no gap is claimed. The single proposal below is not a missing rung; it is a missing BEAT inside rung 6 that the product's own core pain statement names.


---

## `hero.image`

**Role:** hero · **Asset:** `01-hero-relief-hero.png`
**Placement:** Advertorial header, directly under the eyebrow 'Comfort · 6-Month Test'.

**GIF:** YES — whole-frame — The declared reason to exist is a body settling into support — a transition, so it is temporal.

### Option A — `06-relief-hero` v1.7 `--commercial, inset --none`
*varies on:* baseline · *ratio param:* 2:1 · *attach:* product.reference_photos

Zone B skipped by the skeleton's own rule: the product is at the contact point and legible. Inset --none keeps the editorial register clean.

```
TYPE: 06-relief-hero v1.7, register --commercial, inset_mode --none
REGISTER: clean commercial e-commerce banner, bright airy, sharp focus, 4K.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve
shape, proportions, material, finish and colour exactly. Do not redesign or add
features.

ZONE A, HERO: a man in his late forties in an open-collar shirt, seated in the
driver's seat of a modern estate car on a bright weekday morning, one hand resting
on the wheel, shoulders dropped back against the seat, gaze out through the
windscreen, expression of settled ease. The product in place beneath and behind him,
its seat section under his hips and its lumbar section rising into the small of his
back, seen from a front three-quarter angle through the open driver's door,
unobstructed, in fitted car-seat use.
Setting: a suburban driveway filled to the edges — a travel mug in the console, a
lanyard hanging from the mirror, a folded jacket on the passenger seat, a phone
mount, a parking permit on the screen, hedges and a neighbour's gate beyond the open
door. Morning side light through the windscreen. Background blurred but never blank,
no bare panel area larger than the product. High-key warm-neutral grade.
Subject offset right; no layer occupies the left space and no empty mid-frame is
reserved.

VISIBLE MECHANISM: the product emits nothing, so no effect is invented. What carries
the frame instead is contact — the continuous line where the cushion meets his lower
back with no gap behind the lumbar curve.

POSE: the product works passively while he does something else, so the pose is
relaxed, hands on the wheel, gaze away from the product.

LIGHT: soft even morning daylight through the windscreen, background blurred,
high-key grade.
```

`avoid:` text, numbers, watermarks, logos, pain cues, cluttered background, dark moody lighting, blurry product, invented mist or steam, malformed fingers, extra fingers

### Option B — `06-relief-hero` v1.7 `--ugc, inset --none`
*varies on:* axis: register commercial → ugc · *ratio param:* 2:1 · *attach:* product.reference_photos

ugc register suits the editorial 'our editors tested it' framing. Never legal on marketplace; advertorial only here.

```
TYPE: 06-relief-hero v1.7, register --ugc, inset_mode --none
REGISTER: an owner's own photo, natural, unstyled, slightly imperfect.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve
shape, proportions, material, finish and colour exactly.

ZONE A, HERO: a man in his fifties in a creased polo, half-turned in the driver's
seat of an ordinary hatchback as if about to get out, one foot already on the
driveway, easy unposed expression. The product in place behind and beneath him, its
lumbar section filling the curve of his lower back, seen from outside the open door,
unobstructed, in fitted car-seat use.
Setting: a real driveway filled to the edges — a supermarket bag in the footwell, a
phone cable trailing from the console, a coffee cup in the holder, a hi-vis vest on
the back seat, wheelie bins by the fence, wet tarmac. Flat overcast daylight.
Background blurred but never blank. Honest ordinary grade, not high-key.
Subject offset right; nothing occupies the left space.

VISIBLE MECHANISM: the product emits nothing, so no effect is invented. Contact
carries the frame — the unbroken line where the lumbar section meets his back.

POSE: relaxed, mid-exit, gaze away from the product.

LIGHT: flat overcast daylight, no rim light, no glamour.
```

`avoid:` text, numbers, watermarks, logos, studio lighting, magazine polish, pain cues, invented mist or steam, malformed fingers, extra fingers

---

## `problems.items.0.image`

**Role:** pain · **Asset:** `02-problem-pain-scene.png`
**Placement:** Section 'Why most seat cushions end up in the closet', beside the note list.

**GIF:** no — A single held moment of recognition. Nothing transitions; motion would turn a photograph into a performance.

### Option A — `01-pain-scene` v1.2 `--candid`
*varies on:* baseline · *ratio param:* 5:3

requires_pair — satisfied by slot 1 and slots 9-12 downstream. G1-exempt: no product in frame. Page arc: this is the only pain beat and nothing pain-coded appears after slot 3.

```
TYPE: 01-pain-scene v1.2, variant --candid
REGISTER: cinematic film still. Single frame. NO graphic overlays of any kind.

SUBJECT: a man in his late forties in a wrinkled button-down, caught mid-action
pushing himself up out of an office chair at the end of the afternoon, weight on
both hands on the desk edge, hips still low, one knee not yet straight. Face showing
a flat involuntary tightening around the eyes and a set jaw, not a grimace. Gaze
down at the desk, unaware of the camera. Weight unbalanced, mid-motion, not posed.

MOMENT RULE: this is a mundane moment anyone lives daily, not a demonstration of
wrong behaviour.

SYMPTOM EVIDENCE: the failed remedies are in frame and carry the problem as physical
fact. A thin flat foam cushion has slid forward off the front of the seat and hangs
half off; a separate lumbar pillow has dropped down and is wedged between the
seatback and the seat pan; a rolled-up sweater is stuffed behind it as a third
attempt. The seat pan itself is visibly dished and shiny where he sits.

ENVIRONMENT: an ordinary open-plan office at four in the afternoon in late autumn,
the window grey behind half-closed blinds. Real lived-in clutter that belongs there
and signals the interrupted routine: a cold mug, a lanyard on the monitor arm, a
stack of printouts, a phone face-down. Nothing styled, nothing arranged.

LIGHT: low-key. Key from the window on his left, cool and directional. Weak fill
from the ceiling panel. A rim separating his shoulder from the dark partition. Deep
shadow across 40% of the frame.

GRADE: desaturated cool-grey palette, fine film grain, shallow depth of field, 35mm
lens character, crushed blacks.

FORBIDDEN: no product. No overlays, arrows, badges, glows, hotspots, insets or split
panels. No red anywhere in the frame. Nothing that signals advertising.
```

`avoid:` text, watermarks, logos, studio lighting, stock photo look, posed model, fake grimace, smiling, looking at camera, warm flattering light, saturated colours

### Option B — `01-pain-scene` v1.2 `--candid`
*varies on:* execution: office desk → driver's seat, the page's second named context · *ratio param:* 5:3

Same type and axes as A; only the persona context changes. The brief names commuters and drivers first, so this execution may fit the section better.

```
TYPE: 01-pain-scene v1.2, variant --candid
REGISTER: cinematic film still. Single frame. NO graphic overlays of any kind.

SUBJECT: a man in his fifties in a work fleece, caught mid-action swinging one leg
out of a van cab in a service-station bay after a long stretch of driving, one hand
braced hard on the door frame, the other flat against his lower back, hips still in
the seat. Face showing a brief involuntary stillness, brow drawn, mouth closed. Gaze
down at the step, unaware of the camera. Weight unbalanced, mid-motion.

MOMENT RULE: this is a mundane moment anyone lives daily, not a demonstration of
wrong behaviour.

SYMPTOM EVIDENCE: the failed remedies are in frame. A flat foam pad has slid forward
and folded against the front edge of the seat squab; a separate mesh lumbar support
hangs by one elastic hook, the other unclipped; a folded towel is jammed into the
gap where the seatback meets the base. The squab is visibly compressed and glazed.

ENVIRONMENT: a service-station bay at dusk in late autumn, sodium light beginning to
come up. Real clutter that belongs there: a crushed drinks bottle in the door bin, a
lanyard on the gear lever, receipts on the dash, a hi-vis on the passenger seat.
Nothing styled, nothing arranged.

LIGHT: low-key. Key from the forecourt canopy above and behind, cool and hard. Weak
fill off the wet tarmac. Rim along his shoulder. Deep shadow across 45% of frame.

GRADE: desaturated cool-grey palette, fine film grain, shallow depth of field, 35mm
lens character, crushed blacks.

FORBIDDEN: no product. No overlays, arrows, badges, glows, hotspots, insets or split
panels. No red anywhere in the frame. Nothing that signals advertising.
```

`avoid:` text, watermarks, logos, studio lighting, stock photo look, posed model, fake grimace, smiling, looking at camera, warm flattering light, saturated colours

---

## `problems.items.1.image`

**Role:** proof · **Asset:** `03-sixmonth-timelapse.png`
**Placement:** Section 'What we set out to measure', beside 'The test' note list. This image IS the page's central claim.

**GIF:** no — The argument is the side-by-side comparison of three time points. Motion would replace a comparison the viewer must hold in one glance.

### Option A — `04-proof-lockedframe` v1.5 `--timelapse, camera_lock handheld`
*varies on:* baseline · *ratio param:* 5:3 · *attach:* product.reference_photos

camera_lock handheld is mandatory: panels are separated by months, and a pixel-locked frame across six months is proof of staging. Written per the v1.5 WORDING LAW so it runs single-pass.

```
TYPE: 04-proof-lockedframe v1.5 --timelapse, camera_lock handheld
REGISTER: documentary phone photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

PRODUCT REFERENCE: use the attached photo as the exact reference for the cushion in
every panel. Preserve shape, proportions, material, finish and colour exactly.

PRODUCT PROMINENCE: the cushion is the subject of every panel and fills at least 65%
of it, stood on its side on the same table so the seat section's thickness is edge-on
to the camera. Nothing else competes for attention.

SCENE, the same in all three: a scratched office breakroom table against a painted
breeze-block wall, a steel ruler lying flat beside the cushion, a chipped mug and a
set of van keys pushed to the back edge. Flat overcast daylight from a high window.

GRADE, one grade for all three and no polarity in it: neutral, low saturation, from
the window light rather than a filter. Panel 1 is not made to look fresher and panel
3 is not darkened to dramatise wear. What changes is the object, never the treatment.

FRAMING: one person photographed this three times across six months from where they
always stand, phone held level with the table, ruler across the lower third. It reads
as one shot taken three times, never as three different shots — drift is a few
degrees of tilt and a few centimetres of position, no more. Light differs only in
exposure, never in warmth.

THE VARIABLE, the only thing that changes, the seat section seen edge-on:
1 — new: the foam block square and full, its top face flat and its side wall
straight, the cover taut over the corners.
2 — three months: the same block a little lower under the sit area, one soft dish
forming where the hips land, the side wall still straight, the cover slightly relaxed.
3 — six months: the dish clearly settled and the cover creased along it, but the
block still standing to its own height at the front lip and the side wall still
straight, the foam plainly still foam and not a flattened pad.

WHAT ELSE MOVES: 1 — mug upright at the back. 2 — mug turned, keys moved forward.
3 — keys gone, a fresh ring mark on the table.

CONTEXT: an ordinary inspection moment, the cushion simply stood up where someone
would look at it. Nothing cut open, propped or arranged for the camera.

JUDGEMENT: no panel is favoured. The image only shows.
```

`avoid:` text, numbers, month labels, watermarks, logos, sparkle glyphs, badges, arrows, glows, human figures, hands, studio lighting, staged perfection, identical framing between panels, CGI

### Option B — `04-proof-lockedframe` v1.5 `--rivals, camera_lock handheld`
*varies on:* variant: timelapse → rivals; the beat becomes 'we tried three kinds' instead of 'one cushion over six months' · *ratio param:* 5:3

No product in frame, so advertorial and paid-social only — legal here. --rivals is the one variant whose GRADE carries polarity for the whole image, because all three panels are failed states.

```
TYPE: 04-proof-lockedframe v1.5 --rivals, camera_lock handheld
REGISTER: documentary phone photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

PRODUCT REFERENCE: not applicable. No reference product appears in this image.

SCENE, the same in all three: the driver's seat of an ordinary hatchback photographed
through the open door, the same worn fabric squab, the same seatbelt buckle lying in
the same place, a parking permit on the dash. Flat overcast daylight.

GRADE, the same in all three: muted and cool, low saturation, no warm tone anywhere.
It comes from the weather and the grey trim rather than a filter. Still colour, never
black and white. All three panels are unsolved states, so one shared unresolved tone
across them favours none of them.

FRAMING: one person photographed this three times across a month from where they
always stand beside the open door, phone at chest height, headrest across the upper
third. It reads as one shot taken three times, never as three different shots — drift
is a few degrees of tilt and a few centimetres, no more. Light differs only in
exposure, never in warmth.

THE VARIABLE: three common existing approaches, generic and unbranded, each
photographed after a week of use.
1 — a flat square foam pad, slid forward so its front edge overhangs the seat lip and
a wedge of bare squab shows behind it.
2 — a separate mesh lumbar pillow hanging by one elastic strap, dropped to the base
of the seatback, the other strap unclipped and curled.
3 — a beaded seat cover rucked diagonally across the squab, its ties slack, the
beads pooled to one side.

WHAT ELSE MOVES: 1 — buckle lying flat. 2 — buckle twisted, a receipt in the door
bin. 3 — receipt gone, a coffee ring on the sill.

FAIRNESS: three ordinary things people already own, none broken or exaggerated, none
favoured. Every panel ends the same way. The image makes no claim.
```

`avoid:` text, watermarks, logos, sparkle glyphs, badges, arrows, glows, brand marks, one item obviously better, human figures, hands, studio lighting, staged perfection, identical framing between panels, CGI

---

## `features.items.0.image`

**Role:** cause · **Asset:** `04-feature-two-piece-cause.png`
**Placement:** Feature 1 'Continuous support that never separates or slides'.

**GIF:** YES — whole-frame — The indicted event is a slide — the pillow dropping and the pad creeping forward is a transition, not a state.

### Option A — `02-cause-anatomy` v1.1
*varies on:* baseline · *ratio param:* 16:9

Blames a concrete object — the two-piece setup — which is exactly this type's job. Placed after the pain image, before the mechanism images.

```
TYPE: 02-cause-anatomy v1.1
REGISTER: 2D medical illustration, airbrushed textbook style. NOT photography, NOT 3D render.

CANVAS: one continuous pale blue clinical gradient shared by both panels, divided by a
single thin vertical line, not a hard split. Background motifs at very low opacity:
hexagon mesh, faint medical cross icons, an oversized ghosted lumbar spine as a watermark.

BODY TREATMENT, both panels: the lumbar spine and pelvis drawn in warm ivory as the top
layer, the seated human body reduced to a translucent glowing outline behind it. Same
figure, same scale, same side-on viewing angle in both panels.

LEFT PANEL, WRONG: the figure seated on a car seat drawn realistically, with a flat pad
under the hips that has crept forward off the seat lip and a separate lumbar pillow that
has dropped to the base of the seatback. A wedge of empty space opens between the small
of the back and the seatback. The lower lumbar vertebrae highlighted in red. A red curved
line tracing the backward bowed lumbar contour.

RIGHT PANEL, CORRECT: the same figure on the same seat with one continuous L-shaped
support, its seat section under the hips and its back section filling the space the pad
and pillow left empty. The same vertebrae highlighted in blue. A soft blue aura along the
restored forward lumbar curve. Brighter and cleaner than the left panel.

REFERENCE LINES, a required graphic layer: one dashed line in each panel at the same
landmark, the plane through the top of the pelvis. Identical thickness, identical dash
length, identical length on screen. The left one clearly tilted backward, the right one
clearly level. They differ in angle and in nothing else. Left line red, right line blue.

BADGES, a required graphic layer: exactly two, one per panel, in the outer top corner of
each. Left, a flat red circle with a white X. Right, a flat green circle with a white
check. Same diameter, both fully opaque.

PALETTE LOCK: pale blue and ivory throughout. The only signal colours are red for wrong,
blue for correct, green for the confirmation badge.
```

`avoid:` words, letters, numerals, watermarks, logos, photographic texture, 3D render shading, orange, yellow, purple

### Option B — `02-cause-anatomy` v1.1
*varies on:* execution: car seat → office chair, the page's other named context · *ratio param:* 16:9

Same type and axes as A. The features copy names both contexts; this execution serves readers who sit rather than drive.

```
TYPE: 02-cause-anatomy v1.1
REGISTER: 2D medical illustration, airbrushed textbook style. NOT photography, NOT 3D render.

CANVAS: one continuous pale blue clinical gradient shared by both panels, divided by a
single thin vertical line, not a hard split. Background motifs at very low opacity:
hexagon mesh, faint medical cross icons, an oversized ghosted pelvis as a watermark.

BODY TREATMENT, both panels: the lumbar spine and pelvis drawn in warm ivory as the top
layer, the seated human body reduced to a translucent glowing outline behind it. Same
figure, same scale, same side-on viewing angle in both panels.

LEFT PANEL, WRONG: the figure seated on a mesh office chair drawn realistically, a flat
foam pad slipped forward under the hips and a strapped lumbar cushion riding up between
the shoulder blades, pushing the upper back forward while the hips stay sunk. The
resulting S-twist through the lower spine highlighted in red. A red curved line tracing
the twisted contour.

RIGHT PANEL, CORRECT: the same figure on the same chair with one continuous L-shaped
support, hips raised level with the knees and the back section meeting the lumbar curve
without pushing the shoulders forward. The same region highlighted in blue. A soft blue
aura along the aligned contour. Brighter and cleaner than the left panel.

REFERENCE LINES, a required graphic layer: one dashed line in each panel through the hip
joint and the knee joint. Identical thickness, identical dash length, identical length on
screen. Left clearly sloping down toward the hip, right clearly level. They differ in
angle and in nothing else. Left line red, right line blue.

BADGES, a required graphic layer: exactly two, one per panel, in the outer top corner of
each. Left, a flat red circle with a white X. Right, a flat green circle with a white
check. Same diameter, both fully opaque.

PALETTE LOCK: pale blue and ivory throughout. The only signal colours are red for wrong,
blue for correct, green for the confirmation badge.
```

`avoid:` words, letters, numerals, watermarks, logos, photographic texture, 3D render shading, orange, yellow, purple

---

## `features.items.1.image`

**Role:** mechanism · **Asset:** `05-feature-pelvic-gap-ghostbody.png`
**Placement:** Feature 2 'Bridges the pelvic rollback gap completely'.

**GIF:** YES — whole-frame — The pelvis rolling back into the gap is a state change inside the body — temporal by definition.

### Option A — `03-mechanism-ghostbody` v1.2
*varies on:* baseline · *ratio param:* 4:5 · *attach:* product.reference_photos

Step-3 budget: this plus 03-use-sequence makes two of the named set {ghostbody, spec-split, use-sequence} — at the cap, not over it.

```
TYPE: 03-mechanism-ghostbody v1.2
REGISTER: 3D medical visualization on a dark clinical background. NOT photography.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly. Do not redesign or add features.

BASE: GHOST BODY — a translucent glass-like human figure seen in side profile, seated,
filling 70% of the frame height, rendered against a deep navy gradient with faint
anatomical grid motifs at very low contrast.

ANATOMY CUTAWAY: the pelvis, sacrum and lumbar spine rendered solid and detailed inside
the translucent figure at their true positions, warm ivory bone against the glass body.

THE MECHANISM: the figure is seated on a car seat whose base tilts backward. Without
support, the pelvis has rotated backward and dropped into the open wedge where the seat
base meets the backrest, and that wedge is the subject of the frame — an empty dark void
behind the sacrum, the single thing the eye lands on first.
The reference product is shown filling that wedge exactly, its seat section under the
pelvis and its back section continuous into the lumbar curve, one piece with no seam
between them.

VISIBLE MECHANISM: the product emits nothing, so no effect is invented. The working
element is the contact interface, marked with a cool cyan glow running the whole
continuous length where the product meets sacrum and lumbar spine — unbroken, which is
the entire argument. Red stress highlight on the rearward-rotated sacrum only where the
support is absent.

HONESTY CONSTRAINT: render only the anatomy and the product geometry that genuinely
exist. No invented muscles, no exaggerated angles.

PALETTE LOCK: deep navy and ivory. Cyan marks the working mechanism, red marks the
unsupported stress, and no other signal colour appears.
```

`avoid:` words, letters, numerals, spec labels, watermarks, logos, photographic skin texture, green, orange, yellow

### Option B — `02-cause-anatomy` v1.1
*varies on:* type: 03-mechanism-ghostbody → 02-cause-anatomy; a flat clinical illustration instead of a 3D ghost body · *ratio param:* 16:9 · *attach:* product.reference_photos

Legal alternative if the 3D register reads too cold beside the editorial copy. Note it would put cause-anatomy on the page three times across two sections — allowed only because features.items is one repeating section (cross-slot rule 2).

```
TYPE: 02-cause-anatomy v1.1
REGISTER: 2D medical illustration, airbrushed textbook style. NOT photography, NOT 3D render.

CANVAS: one continuous pale blue clinical gradient shared by both panels, divided by a
single thin vertical line. Background motifs at very low opacity: hexagon mesh, faint
medical cross icons, an oversized ghosted pelvis as a watermark.

BODY TREATMENT, both panels: pelvis, sacrum and lumbar spine in warm ivory as the top
layer, the seated body a translucent glowing outline behind. Same figure, same scale,
same side-on angle in both panels.

LEFT PANEL, WRONG: the figure on a rearward-tilted car seat drawn realistically, hips
dropped below knee level, the pelvis rotated backward into the open wedge where the seat
base meets the backrest. That wedge drawn as an empty dark gap. Sacrum and lower lumbar
highlighted in red. A red curved line tracing the backward-bowed contour.

RIGHT PANEL, CORRECT: the same figure on the same seat with the reference support filling
the wedge, hips raised level with the knees, pelvis upright. The same region highlighted
in blue. A soft blue aura along the restored curve. Brighter and cleaner than the left.

REFERENCE LINES, a required graphic layer: one dashed line in each panel through hip and
knee joints, identical thickness and dash length, left clearly sloping down toward the
hip, right clearly level. Left red, right blue.

BADGES, a required graphic layer: exactly two, one per panel, outer top corner of each.
Left a flat red circle with a white X, right a flat green circle with a white check. Same
diameter, both fully opaque.

PALETTE LOCK: pale blue and ivory. Signal colours are red for wrong, blue for correct,
green for the confirmation badge.
```

`avoid:` words, letters, numerals, watermarks, logos, photographic texture, 3D render shading, orange, yellow, purple

---

## `features.items.2.image`

**Role:** mechanism · **Asset:** `06-feature-foam-core-xray.png`
**Placement:** Feature 3 'High-density foam that absorbs road vibration'.

**GIF:** YES — whole-frame — Slow-rebound foam recovering after compression is a state returning over time — the product's own named behaviour.

### Option A — `03-mechanism-xray` v1.0
*varies on:* baseline · *ratio param:* 1:1 · *attach:* product.reference_photos

avoid_when tension recorded honestly: xray's use_when names gadget-class products that do NOT act on a body structure. This cushion does. It is admitted because the subject here is the foam's own internal structure, not the body interface — but flag it if the render reads cold against the editorial copy.

```
TYPE: 03-mechanism-xray v1.0
REGISTER: 3D technical see-through render. NOT photography. Dark engineering background.

PRODUCT REFERENCE: use the attached product photo as the exact reference. The outer cover
becomes translucent, but the silhouette, proportions and every visible external part must
match the reference exactly. Do not redesign or add features.

CANVAS: a deep navy engineering canvas with faint copper and cyan circuit-board traces at
very low contrast, and one corner blueprint micro-diagram of a foam cell lattice. Motifs
stay dim — they buy credibility, they carry no information.

BASE: GHOST SHELL — the cushion rendered with its cover translucent and glass-like,
silhouette matching the reference, positioned three-quarter with the seat section toward
camera, filling 70% of the frame width.

INTERNALS: the slow-rebound memory foam core rendered solid and detailed inside the
cover, its open-cell lattice visible as a dense fine structure through the seat section
and continuing unbroken up through the lumbar section — one core, no seam, no join. The
non-slip base layer rendered as a thin distinct stratum along the underside.

VISIBLE MECHANISM: the product emits nothing, so the primary working component is
highlighted instead. A cool cyan glow diffuses through the foam lattice directly under
the sit area and fades outward, marking where load is absorbed and spread. It is the
brightest element in the frame.

HONESTY CONSTRAINT: render only component types the product genuinely contains — a foam
core, a cover, a base layer. No invented modules, no springs, no gel pods, no electronics.

PALETTE LOCK: deep navy and steel grey throughout. Cyan marks the working mechanism.
Copper traces stay decorative and dim and never mark a component.
```

`avoid:` words, letters, numerals, spec labels, watermarks, logos, exploded parts, springs, gel inserts, electronics, orange on any component

### Option B — `03-mechanism-xray` v1.0
*varies on:* execution: whole-cushion ghost shell → a cut block of the core at macro scale · *ratio param:* 1:1 · *attach:* product.reference_photos

Same type and axes as A. Narrows the subject to the material claim alone, which is what the feature copy actually argues.

```
TYPE: 03-mechanism-xray v1.0
REGISTER: 3D technical see-through render. NOT photography. Dark engineering background.

PRODUCT REFERENCE: use the attached product photo as the exact reference for the cover
material and colour. Silhouette and finish must match the reference exactly.

CANVAS: a deep navy engineering canvas with faint copper and cyan circuit-board traces at
very low contrast, and one corner blueprint micro-diagram of a cell wall. Motifs stay dim.

BASE: GHOST SHELL — a rectangular block of the cushion's own core with its cover
translucent and glass-like along the top face, standing upright at a slight three-quarter
angle, filling 65% of the frame width.

INTERNALS: the open-cell foam lattice rendered solid and detailed through the whole block,
cells visibly finer and denser toward the load-bearing top face and more open toward the
base, each wall distinct. The thin non-slip base layer as its own stratum underneath.

VISIBLE MECHANISM: the product emits nothing, so the primary working component is
highlighted. A cool cyan glow enters at the top face and diffuses downward and outward
through the lattice, dispersing rather than passing straight through — the absorption the
feature copy claims, shown as light spreading. It is the brightest element in the frame.

HONESTY CONSTRAINT: render only what the product genuinely contains — one continuous foam
structure, a cover, a base layer. No springs, no gel, no laminated sheets it does not have.

PALETTE LOCK: deep navy and steel grey. Cyan marks the working mechanism. Copper traces
stay decorative and dim and never mark a component.
```

`avoid:` words, letters, numerals, spec labels, watermarks, logos, springs, gel inserts, laminated layers, orange on any component

---

## `features.items.3.image`

**Role:** spec · **Asset:** `07-feature-base-grip-xray.png`
**Placement:** Feature 4 'Non-slip grip that stays put without straps'.

**GIF:** no — This slot exists to reveal a surface at close range, not a transition. The sliding it argues against is temporal, but showing it would mean animating a failure the type does not stage.

### Option A — `03-mechanism-xray` v1.0
*varies on:* execution: foam core → base grip layer. Second xray in the features.items repeating section (cross-slot rule 2), differing on named subject. · *ratio param:* 1:1 · *attach:* product.reference_photos

Nearest-fit type is 03-spec-macro, which is STAGING at 4/5 exemplars and therefore not routable. Ladder rung 4 applied: another execution of a type already on the page, named here rather than hidden.

```
TYPE: 03-mechanism-xray v1.0
REGISTER: 3D technical see-through render. NOT photography. Dark engineering background.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Silhouette,
proportions and every visible external part must match the reference exactly.

CANVAS: a deep navy engineering canvas with faint copper and cyan traces at very low
contrast, and one corner blueprint micro-diagram of a single grip dot in section. Motifs
stay dim.

BASE: GHOST SHELL — the cushion tipped to show its underside toward camera, the cover
translucent and glass-like, silhouette matching the reference, filling 70% of the frame
width.

INTERNALS: the rubberised micro-dot grip layer rendered solid and detailed across the
whole underside, an even field of small raised dots at true scale and true spacing,
covering the base edge to edge with no bare zone. The foam core visible above it as a
dimmer translucent mass. A cross-section wedge cut at the near corner shows the dot
profile standing proud of the backing.

VISIBLE MECHANISM: the product emits nothing, so the primary working component is
highlighted. A cool cyan glow sits in the contact plane at the dot tips, densest where the
dots meet an implied seat surface, marking the grip interface as the working element. It
is the brightest thing in the frame.

HONESTY CONSTRAINT: render only what the product genuinely contains — a dotted rubberised
base, a foam core, a cover. No straps, no hooks, no adhesive layer, no suction elements.

PALETTE LOCK: deep navy and steel grey. Cyan marks the working mechanism. Copper traces
stay decorative and dim.
```

`avoid:` words, letters, numerals, spec labels, watermarks, logos, straps, hooks, suction cups, adhesive film, orange on any component

### Option B — `06-relief-hero` v1.7 `--commercial, inset --detail`
*varies on:* type: 03-mechanism-xray → 06-relief-hero with a magnifier inset; a photographic answer instead of a technical one · *ratio param:* 2:1 · *attach:* product.reference_photos

Ladder rung 4 again, on the other type already on the page. Keeps the section photographic if the two xrays read as a lecture. The --detail inset is linked by proximity only: no arrow, no glow border.

```
TYPE: 06-relief-hero v1.7, register --commercial, inset_mode --detail
REGISTER: clean commercial e-commerce banner, bright airy, sharp focus, 4K.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly. The product is identical in every layer.

ZONE A, HERO: a woman in her forties in a knit cardigan, seated at a home-office desk
mid-task with one hand on a mouse, weight settled back, calm focused expression. The
product in place beneath and behind her on a mesh task chair, seen from a rear
three-quarter angle, unobstructed, in fitted chair use.
Setting: a home office filled to the edges — a plant on the sill, a mug, a stack of
paperbacks, a cable tray, a wall calendar, a coat on the door hook, a printer on a
sideboard. Soft window light from the left. Background blurred but never blank. High-key
warm-neutral grade. Subject offset right; the inset occupies the left space and no empty
mid-frame is reserved.

VISIBLE MECHANISM: the product emits nothing, so no effect is invented. Contact carries
the frame — the unbroken meeting line of cushion and chair with no gap behind the lumbar.

POSE: the product works passively while she does something else, so the pose is relaxed,
gaze away from the product.

LIGHT: soft even window light, background blurred, high-key grade.

ZONE C, INSET, circle, lower-left corner, 22% of frame width: a magnified view of the
cushion's underside alone, the rubberised micro-dot field filling the circle at macro
scale, dots sharp and countable, pressed against the chair fabric so the fibres deform
slightly around them. Linked to the in-scene product by proximity only. Its edge is a
clean hard cut with nothing drawn around it and nothing drawn between it and the product.
```

`avoid:` words, letters, numerals, watermarks, logos, digital displays, arrows, badges, cluttered background, dark moody lighting, pain cues, invented mist or steam, malformed fingers, extra fingers

---

## `features.items.4.image`

**Role:** use · **Asset:** `08-feature-fit-use-sequence.png`
**Placement:** Feature 5 'Fits standard seats, no installation needed'.

**GIF:** YES — whole-frame — An ordered sequence is the definition of temporal. This is the strongest GIF candidate on the page.

### Option A — `03-use-sequence` v1.1
*varies on:* baseline · *ratio param:* 1:1 · *attach:* product.reference_photos

Second of the two permitted step-3 types from the named set. The copy's claim is 'moves in three seconds', so the sequence is the argument.

```
TYPE: 03-use-sequence v1.1
REGISTER: warm lifestyle photography, close range.
LAYOUT: 3 horizontal panels stacked vertically, thin white gutters, no outer border, no
numbers, no arrows, no text.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly in every panel.

CONTINUITY LOCK: the same hands in every panel, same skin tone, same short unpainted
nails, same wrists, same rolled charcoal sleeves. The same cushion in every panel. Same
warm neutral palette, same soft daylight from the left throughout. Camera distance may
vary between panels and framing may shift naturally.

SEQUENCE RULE: one action per panel, never two. The order is readable from the actions
alone, with no numbering. The product sits near the centre of every panel.

PANEL 1, PREPARE: both hands setting the cushion down into a mesh office chair, the seat
section landing on the squab and the back section standing up against the backrest, the
inside corner of the L meeting the join where seat and back meet.

PANEL 2, USE: one hand pressing down firmly on the seat section while the other steadies
the backrest, the foam compressing under the heel of the hand and the base gripping so
nothing shifts. The whole cushion stays square to the chair.

PANEL 3, RESULT: the same cushion lifted free in one hand and carried a step away toward
an open car door visible beyond, the other hand resting on the chair back. Warmer light
than the previous panels. No new mechanics introduced.

ENVIRONMENT: an ordinary home office opening onto a driveway, soft daylight, a doormat
and a set of keys on a side table at the frame edge. Same location across all panels.

STYLE: warm lifestyle product photography, natural, unstyled, sharp, 4K.
```

`avoid:` words, numbers, step numbers, watermarks, logos, arrows, step markers, badges, two actions in one panel, instruction manual look, cold clinical lighting, malformed fingers, extra fingers

### Option B — `03-use-sequence` v1.1
*varies on:* execution: office chair → car seat, with the carry beat first instead of last · *ratio param:* 1:1 · *attach:* product.reference_photos

Same type and axes as A. Puts the driver context first, which the persona field ranks above desk workers.

```
TYPE: 03-use-sequence v1.1
REGISTER: warm lifestyle photography, close range.
LAYOUT: 3 horizontal panels stacked vertically, thin white gutters, no outer border, no
numbers, no arrows, no text.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly in every panel.

CONTINUITY LOCK: the same hands in every panel, same skin tone, same short unpainted
nails, same wrists, same rolled olive sleeves. The same cushion in every panel. Same warm
neutral palette, same soft daylight from the right throughout. Camera distance may vary
between panels and framing may shift naturally.

SEQUENCE RULE: one action per panel, never two. The order is readable from the actions
alone, with no numbering. The product sits near the centre of every panel.

PANEL 1, PREPARE: one hand carrying the cushion by its lumbar section through an open car
door, the other hand on the door frame, the seat visible empty beyond.

PANEL 2, USE: both hands seating the cushion into the driver's seat, the seat section
settling onto the squab and the back section rising flush against the seatback, the inner
corner of the L closing the gap where squab meets backrest.

PANEL 3, RESULT: one hand pressing the seat section down to check it, the other resting
on the steering wheel, the cushion square and unmoved in the seat. Warmer light than the
previous panels. No new mechanics introduced.

ENVIRONMENT: an ordinary car on a driveway, soft daylight, a travel mug in the console
and a lanyard on the mirror at the frame edge. Same location across all panels.

STYLE: warm lifestyle product photography, natural, unstyled, sharp, 4K.
```

`avoid:` words, numbers, step numbers, watermarks, logos, arrows, step markers, badges, two actions in one panel, instruction manual look, cold clinical lighting, malformed fingers, extra fingers

---

## `reviews.shots.0.image`

**Role:** social · **Asset:** `09-review-shot-car.png`
**Placement:** Reader-notes section, first shot. NOT adjacent to a reviewer name or verified badge — see the fence note.

**GIF:** no — This slot exists to reveal a place, not a transition. No state changes inside it.

### Option A — `06-relief-hero` v1.7 `--ugc, inset --none`
*varies on:* baseline for this section; ladder rung 4 against slot 1, which is the same type in --commercial register · *ratio param:* 4:3 · *attach:* product.reference_photos

05-social-snapshot is the natural type here and is BARRED: this section displays reviewer names and verified labels, and the snapshot AUTHENTICITY FENCE forbids a generated snapshot anywhere near them. That is an FTC line, not a style preference.

```
TYPE: 06-relief-hero v1.7, register --ugc, inset_mode --none
REGISTER: an owner's own photo, natural, unstyled, slightly imperfect.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly.

ZONE A, HERO: a man in his fifties in a work fleece, seated in the driver's seat of an ordinary hatchback, photographed from the passenger side, weight settled back, easy unposed expression,
gaze away from the camera. The product in place beneath and behind them, the seat section under the hips and the back section rising into the lumbar curve, seen
from a rear three-quarter angle, unobstructed, in fitted seat use.
Setting: a real car interior — a travel mug in the holder, a phone cable over the gear lever, a parking permit on the screen, a hi-vis on the back seat, a supermarket bag in the footwell, wet tarmac beyond the window. Background blurred but never blank, no bare panel or wall area larger
than the product. Honest ordinary grade, not high-key. Subject offset right; nothing
occupies the left space and no empty mid-frame is reserved.

VISIBLE MECHANISM: the product emits nothing, so no effect is invented. Contact carries
the frame — the unbroken line where the lumbar section meets the small of the back, with
no gap behind it.

POSE: the product works passively while the person does something else, so the pose is
relaxed and the gaze is away from the product.

LIGHT: flat overcast daylight through the windscreen, no rim light, no glamour.
```

`avoid:` words, letters, numerals, watermarks, logos, studio lighting, softbox reflections, magazine polish, pain cues, invented mist or steam, malformed fingers, extra fingers

### Option B — `06-relief-hero` v1.7 `--ugc, inset --detail`
*varies on:* axis: inset_mode none → detail; adds a magnifier circle on the seat-to-back join · *ratio param:* 4:3 · *attach:* product.reference_photos

Offers the section one image that also carries the one-piece claim. The --detail inset is linked by proximity only: no arrow, no glow border.

```
TYPE: 06-relief-hero v1.7, register --ugc, inset_mode --none
REGISTER: an owner's own photo, natural, unstyled, slightly imperfect.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly.

ZONE A, HERO: a man in his fifties in a work fleece, seated in the driver's seat of an ordinary hatchback, photographed from the passenger side, weight settled back, easy unposed expression,
gaze away from the camera. The product in place beneath and behind them, the seat section under the hips and the back section rising into the lumbar curve, seen
from a rear three-quarter angle, unobstructed, in fitted seat use.
Setting: a real car interior — a travel mug in the holder, a phone cable over the gear lever, a parking permit on the screen, a hi-vis on the back seat. Background blurred but never blank, no bare panel or wall area larger
than the product. Honest ordinary grade, not high-key. Subject offset right; nothing
occupies the left space and no empty mid-frame is reserved.

VISIBLE MECHANISM: the product emits nothing, so no effect is invented. Contact carries
the frame — the unbroken line where the lumbar section meets the small of the back, with
no gap behind it.

POSE: the product works passively while the person does something else, so the pose is
relaxed and the gaze is away from the product.

LIGHT: flat overcast daylight through the windscreen, no rim light, no glamour.

ZONE C, INSET, circle, lower-left corner, 20% of frame width: a magnified view of the
inner corner of the L where the seat section meets the back section, showing one
continuous surface with no seam, no zip and no join. Linked to the in-scene product by
proximity only. Its edge is a clean hard cut with nothing drawn around it and nothing
drawn between it and the product.
```

`avoid:` words, letters, numerals, watermarks, logos, studio lighting, softbox reflections, magazine polish, pain cues, invented mist or steam, malformed fingers, extra fingers, arrows, badges

---

## `reviews.shots.1.image`

**Role:** social · **Asset:** `10-review-shot-office.png`
**Placement:** Reader-notes section, second shot.

**GIF:** no — Reveals a second place, not a transition.

### Option A — `06-relief-hero` v1.7 `--ugc, inset --none`
*varies on:* execution: car → home office; the section's named dimension is environment (cross-slot rule 2) · *ratio param:* 4:3 · *attach:* product.reference_photos

Same type and axes as reviews.shots.0 option A, differing on the named dimension the repeating-section exception requires.

```
TYPE: 06-relief-hero v1.7, register --ugc, inset_mode --none
REGISTER: an owner's own photo, natural, unstyled, slightly imperfect.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly.

ZONE A, HERO: a woman in her forties in a fleece hoodie, seated in a high-back mesh task chair at a home desk, photographed from behind and to one side, weight settled back, easy unposed expression,
gaze away from the camera. The product in place beneath and behind them, the seat section under the hips and the back section filling the lumbar curve against the mesh, seen
from a rear three-quarter angle, unobstructed, in fitted seat use.
Setting: a real home office — a plant with one dead leaf, a mug ring on the desk, a cable tray, a printer on a sideboard, a wall calendar, a coat on the door hook. Background blurred but never blank, no bare panel or wall area larger
than the product. Honest ordinary grade, not high-key. Subject offset right; nothing
occupies the left space and no empty mid-frame is reserved.

VISIBLE MECHANISM: the product emits nothing, so no effect is invented. Contact carries
the frame — the unbroken line where the lumbar section meets the small of the back, with
no gap behind it.

POSE: the product works passively while the person does something else, so the pose is
relaxed and the gaze is away from the product.

LIGHT: grey window daylight from the side, ceiling bulb on, mixed and uncorrected.
```

`avoid:` words, letters, numerals, watermarks, logos, studio lighting, softbox reflections, magazine polish, pain cues, invented mist or steam, malformed fingers, extra fingers

### Option B — `06-relief-hero` v1.7 `--ugc, inset --none`
*varies on:* execution: home office → shared workplace desk, older persona · *ratio param:* 4:3 · *attach:* product.reference_photos

Second execution on the same axes; widens the cast without adding a type.

```
TYPE: 06-relief-hero v1.7, register --ugc, inset_mode --none
REGISTER: an owner's own photo, natural, unstyled, slightly imperfect.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly.

ZONE A, HERO: a man in his sixties in a checked shirt, seated in a fabric-backed office chair at a shared workplace desk, photographed from behind and to one side, weight settled back, easy unposed expression,
gaze away from the camera. The product in place beneath and behind them, the seat section under the hips and the back section filling the lumbar curve, seen
from a rear three-quarter angle, unobstructed, in fitted seat use.
Setting: a real workplace — a lanyard on the monitor arm, a stack of printouts, a keyboard with worn keys, a jacket over the next chair, a fire-exit sign beyond. Background blurred but never blank, no bare panel or wall area larger
than the product. Honest ordinary grade, not high-key. Subject offset right; nothing
occupies the left space and no empty mid-frame is reserved.

VISIBLE MECHANISM: the product emits nothing, so no effect is invented. Contact carries
the frame — the unbroken line where the lumbar section meets the small of the back, with
no gap behind it.

POSE: the product works passively while the person does something else, so the pose is
relaxed and the gaze is away from the product.

LIGHT: flat ceiling-panel light with grey daylight from a far window, uncorrected.
```

`avoid:` words, letters, numerals, watermarks, logos, studio lighting, softbox reflections, magazine polish, pain cues, invented mist or steam, malformed fingers, extra fingers

---

## `reviews.shots.2.image`

**Role:** social · **Asset:** `11-review-shot-handoff.png`
**Placement:** Reader-notes section, third shot. Keep clear of the quote cards so no name or verified badge sits beside it.

**GIF:** no — The recommendation beat is a held moment; the pointing gesture is composition, not a transition to animate.

### Option A — `05-social-handoff` v1.0
*varies on:* type: 06-relief-hero → 05-social-handoff; the only step-5 type legal on this page · *ratio param:* 5:3 · *attach:* product.reference_photos

Multi-pass, Template B: render the scene WITHOUT the inset, then composite the circular cutout from the real product photo. The model never repaints a reference-true inset. The INSET block below is the compositing spec, not render text.

```
STEP 1, RENDER, scene only:

TYPE: 05-social-handoff v1.0
REGISTER: candid documentary photograph. One scene.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly.

CHARACTER A, THE ADVOCATE: a man in his forties in a lanyard and open jacket, face turned
toward camera, caught mid-sentence, warm relaxed expression, pointing with his right hand
toward the product. The pointing gesture forms a clear diagonal line ending exactly at the
product.

CHARACTER B, THE LISTENER: a man in his thirties in a rucksack, seen from behind over his
left shoulder, FACE NOT VISIBLE, head turned to follow the pointing gesture, gaze parallel
to the pointing line.

PRODUCT IN SCENE: the reference product resting on the open driver's seat of a car in the
staff car park, framed by the open door, sitting exactly where the pointing line
terminates.

ENVIRONMENT: an office car park on an overcast weekday afternoon, two blurred colleagues
walking to another car, a bollard and a line of hedges beyond. Flat natural daylight, no
dramatic shadows, nothing styled.

COMPOSITION RULE: two vectors, the pointing arm and the listener's gaze, converge on the
product. Nothing else in the frame competes for attention. The link between viewer and
product is made by these vectors alone.

Reserve the lower-right 18% of frame width as ordinary continuous background near the
terminus of the pointing line. Do not place a subject, a face or a bright highlight there.

STEP 2, COMPOSITE, not rendered:
Circular cutout of the reference product on plain white, placed in the reserved
lower-right area, 18% of frame width, near the terminus of the pointing line and never
opposite it. Clean edge. No border, no ring, no drop shadow, no connecting arrow. Colorway
identical to the in-scene product.
```

`avoid:` words, letters, numerals, watermarks, logos, arrows, badges, connecting lines, both faces visible, staged posing, studio lighting, malformed fingers, extra fingers

### Option B — `06-relief-hero` v1.7 `--ugc, inset --none`
*varies on:* type: 05-social-handoff → 06-relief-hero; drops the second person if the handoff staging reads posed · *ratio param:* 4:3 · *attach:* product.reference_photos

Fallback that keeps the section photographic and single-pass. Costs the page its only step-5 type — say so when picking.

```
TYPE: 06-relief-hero v1.7, register --ugc, inset_mode --none
REGISTER: an owner's own photo, natural, unstyled, slightly imperfect.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly.

ZONE A, HERO: a man in his forties in a lanyard and open jacket, seated in the driver's seat of a saloon in an office car park, photographed through the open door, weight settled back, easy unposed expression,
gaze away from the camera. The product in place beneath and behind them, the seat section under the hips and the back section rising into the lumbar curve, seen
from a rear three-quarter angle, unobstructed, in fitted seat use.
Setting: a real car park — a rucksack on the passenger seat, a coffee cup in the holder, a lanyard swinging from the mirror, blurred colleagues walking behind, hedges beyond. Background blurred but never blank, no bare panel or wall area larger
than the product. Honest ordinary grade, not high-key. Subject offset right; nothing
occupies the left space and no empty mid-frame is reserved.

VISIBLE MECHANISM: the product emits nothing, so no effect is invented. Contact carries
the frame — the unbroken line where the lumbar section meets the small of the back, with
no gap behind it.

POSE: the product works passively while the person does something else, so the pose is
relaxed and the gaze is away from the product.

LIGHT: flat overcast afternoon daylight, no rim light, no glamour.
```

`avoid:` words, letters, numerals, watermarks, logos, studio lighting, softbox reflections, magazine polish, pain cues, invented mist or steam, malformed fingers, extra fingers

---

## `reviews.shots.3.image`

**Role:** social · **Asset:** `12-review-shot-passenger.png`
**Placement:** Reader-notes section, fourth shot.

**GIF:** no — Reveals a place and a fit, not a transition.

### Option A — `06-relief-hero` v1.7 `--ugc, inset --none`
*varies on:* execution: driver's seat → passenger seat, younger persona, tighter framing · *ratio param:* 4:3 · *attach:* product.reference_photos

Third execution in the reviews.shots repeating section. Environment, cast and shot distance all differ from shots.0 and shots.1.

```
TYPE: 06-relief-hero v1.7, register --ugc, inset_mode --none
REGISTER: an owner's own photo, natural, unstyled, slightly imperfect.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly.

ZONE A, HERO: a woman in her thirties in a denim jacket, seated in the front passenger seat of a family car, photographed from the rear seat at close range, weight settled back, easy unposed expression,
gaze away from the camera. The product in place beneath and behind them, the seat section under the hips and the back section flush to the seatback, seen
from a rear three-quarter angle, unobstructed, in fitted seat use.
Setting: a real family car — a child's booster seat beside the camera, a crumpled map in the door bin, a hair tie on the gear lever, crumbs in the seat seam, a school bag in the footwell. Background blurred but never blank, no bare panel or wall area larger
than the product. Honest ordinary grade, not high-key. Subject offset right; nothing
occupies the left space and no empty mid-frame is reserved.

VISIBLE MECHANISM: the product emits nothing, so no effect is invented. Contact carries
the frame — the unbroken line where the lumbar section meets the small of the back, with
no gap behind it.

POSE: the product works passively while the person does something else, so the pose is
relaxed and the gaze is away from the product.

LIGHT: low afternoon daylight through the side window, slightly blown on the door trim.
```

`avoid:` words, letters, numerals, watermarks, logos, studio lighting, softbox reflections, magazine polish, pain cues, invented mist or steam, malformed fingers, extra fingers

### Option B — `06-relief-hero` v1.7 `--ugc, inset --none`
*varies on:* execution: car → long-haul truck cab, the persona field's third named group · *ratio param:* 4:3 · *attach:* product.reference_photos

Serves the truckers and rideshare drivers the persona names but no other slot depicts.

```
TYPE: 06-relief-hero v1.7, register --ugc, inset_mode --none
REGISTER: an owner's own photo, natural, unstyled, slightly imperfect.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly.

ZONE A, HERO: a man in his fifties in a padded gilet, seated in the driver's seat of a long-haul truck cab, photographed from the passenger side, weight settled back, easy unposed expression,
gaze away from the camera. The product in place beneath and behind them, the seat section under the hips and the back section rising into the lumbar curve, seen
from a rear three-quarter angle, unobstructed, in fitted seat use.
Setting: a real cab — a thermos in the door, a logbook on the dash, a curtain drawn behind the seats, a phone cradle, an air freshener, a service-station forecourt beyond the glass. Background blurred but never blank, no bare panel or wall area larger
than the product. Honest ordinary grade, not high-key. Subject offset right; nothing
occupies the left space and no empty mid-frame is reserved.

VISIBLE MECHANISM: the product emits nothing, so no effect is invented. Contact carries
the frame — the unbroken line where the lumbar section meets the small of the back, with
no gap behind it.

POSE: the product works passively while the person does something else, so the pose is
relaxed and the gaze is away from the product.

LIGHT: flat forecourt daylight through the windscreen, uncorrected.
```

`avoid:` words, letters, numerals, watermarks, logos, studio lighting, softbox reflections, magazine polish, pain cues, invented mist or steam, malformed fingers, extra fingers

---

## `product.image`

**Role:** offer · **Asset:** `(supplied)`
**Placement:** Product card, main offer block.

**GIF:** no — No generated image in this slot to animate.

> **No generated option.** route: asset — the export declares supplied product photography, not a generation request. This is NOT the library refusing to route an image: no generation was asked for. A standard packshot is also out of library scope by cross-slot rule 6 (the library covers gallery images 2+). Say the word and it gets a generated option instead.

---

## `product_end.image`

**Role:** offer · **Asset:** `(supplied)`
**Placement:** Closing product block 'The cushion that came through all of it'.

**GIF:** no — No generated image in this slot to animate.

> **No generated option.** route: asset — supplied product photography, same as product.image. Not a generation request and not a library refusal.

---

# Recommended additions

---

## `recommended.closing-relief-scene` *(proposed addition)*

**Role:** relief · **Asset:** `13-closing-relief-scene.png`
**Placement:** After the closing product block, as the last image on the page.

**Why it earns its place:** Rung 6, but a different beat from the relief-hero images already on the page: those show the product in place, none shows the lived after-state. brief.personaCorePain names it explicitly — 'getting out of the car means stiffness' — and no slot depicts getting out of the car without it. 01-pain-scene at problems.items.0 carries requires_pair; this is its canonical bookend and closes the page arc pain -> relief.

**GIF:** YES — whole-frame — Standing up and walking away is the transition the whole page has been promising.

### Option A — `06-relief-scene` v1.0
*varies on:* baseline · *ratio param:* 5:3

Multi-pass, Template C: generate problems.items.0 option B first, then edit from that output so the person is the same. This type carries no argument alone and must run beside its pain image.

```
STEP 1: the problems.items.0 option B output (the man leaving the van cab).
STEP 2, EDIT, using that render as reference input:

Same person, same palette, same lens character and same grain.

TYPE: 06-relief-scene v1.0
REGISTER: candid documentary photograph. Single frame. NO graphic overlays.

SUBJECT: the same man in his fifties, same work fleece, now walking away from the parked
van across a service-station forecourt, pausing briefly. Gaze on his own reflection in the
shop window ahead. Expression: a small closed-mouth smile, private and understated. Not
performing, not aware of a camera.

EVIDENCE OF CHANGE: he is upright and square through the hips, no hand at his back, stride
even and both shoulders level — readable from both the direct view and the reflection.

REFLECTION: the forecourt shop window fills 30% of the frame, showing him from a different
angle with his back and gait clearly visible, sharp enough to read the evidence. The
reflection is geometrically consistent with his position.

ENVIRONMENT: an ordinary service station on a flat weekday afternoon, two blurred people at
the pumps, a bin and a stack of screenwash by the door, wet tarmac. Ordinary overcast
weather. Nothing aspirational, no styling.

LIGHT: even natural daylight, bright, soft shadows. Slightly kinder than the paired pain
image but the same time-of-day character. No golden hour, no rim light, no glamour.

GRADE: muted cool-grey palette matching the paired pain image, light film grain, shallow
depth of field. Desaturated, never warm-boosted.
```

`avoid:` words, letters, numerals, watermarks, logos, badges, arrows, overlays, looking at camera, posing, arms raised, celebration gesture, golden hour, glamour lighting, beauty retouching, product in frame, saturated colours, stock photo look

# 219

Channel **advertorial** · registry 2.0.0 · awareness **problem** · generated from `prompts.json`, never hand-edited.

## Page composition notes

```
Channel: advertorial, from lpTypeId. Routed under ADR-059 — channel is no longer an
admission test, so the candidate pool was every active type and the only mechanical kill-rules
were the attribute gates. Ten slots, ten distinct recommended types, one-type-once holds.

REFUSALS, each by a type's own law rather than by a channel label:
- 03-mechanism-ghostbody — attribute gate, body_contact:false. The tool acts on cord.
- 02-symptom-rail — its own avoid_when: not on an EDITORIAL page. First live firing of the rule
  that moved out of `channels` on 2026-08-26.
- 03-spec-split — its own avoid_when names the channel in its own words ("Never on paid-social
  or advertorial"), so removing the channels gate changed nothing here.
- 01-pain-split — never_with 01-pain-scene, which serves the hero.
- 05-social-snapshot — its own avoid_when, on the review wall. See below.

THE REVIEW WALL IS UNROUTED AND THAT IS THE ANSWER. reviews.shots.0-3.image sit in a block
carrying reviews.quotes.N.name ("Donald K."), verified.label "Verified Purchase" and the lead
"Thousands of 5-Star Reviews Agree". 05-social-snapshot's avoid_when forbids pairing a generated
snapshot with a reviewer name or verified badge — a fabricated endorsement (FTC). Any generated
image in that block is presented as a customer upload by the furniture around it. Those four
slots need real customer photographs and no library type serves them.

RATIO NARROWED THE FIELD BEFORE FIT DID, and nothing in the repo enforces this. Nine of the ten
slots are 16:9, and only nine active types declare 16:9 once the refusals above are applied — an
exact fit with zero slack. 03-spec-macro (1:1 only), 03-use-sequence (3:4, 1:1) and
05-persona-grid (1:1, 4:5) could not serve any 16:9 slot. scripts/validate.py checks a prompt's
ratio against ADR-016's five but never against the TYPE's own declared set, though its docstring
says "the declared set is what a router is allowed to ask the renderer for".

TWO COMPROMISES, NAMED:
- content.items.0 is the page's weak slot. 01-pain-scene is the right type for "in full view of
  eight campers" and the hero spent it; the rest of the row is refused. A came from rung 3.
- content.items.3 wanted 03-spec-explode for "two precise metal parts", and that type's own
  avoid_when bars it adjacent to 03-mechanism-xray, which sits at item 2. It moved to item 6.

TWO ATTRIBUTES ARE ASSUMED, NOT SUPPLIED. mounting is recorded as `handheld` and colorways as
["as supplied"], the same convention listicle-arm-trainer-hydraulic-v01 used. The source CSV
carries neither and the page copy does not settle them. Neither kills a type, so the routing is
unaffected; mounting drives G7-X mode inside a prompt and colorways caps Zone B units in
06-relief-hero. Correct them before rendering options that depend on them.
```

## Motion budget

floor 2 · ceiling 5 · **delivered 4** · margin 1 · groups working, result

Four loops, all rung 1 — every one is the routed still in motion and nothing was restaged to fill the table. Coverage is met without reaching for it: `cause`, `mechanism` and `use` are working, `relief` is result. One loop per gif type per page (ADR-037) is what refuses content.items.1 and product.image, both of which are temporal on their own merits and are held as reserves rather than dropped. content.items.5 is the loop worth arguing for: the copy's claim is that the fly does NOT move while the wind does, and a still cannot show a non-event.

- **reserve** `content.items.1.image` (cause) — Same gif type as content.items.0 and ADR-037 allows one loop per gif type per page. items.0 holds it because the copy's own breaking point is there. Promote this one only if the tarp loop fails to read at thumbnail size.

- **reserve** `product.image` (mechanism) — Same gif type as content.items.2, which shows the same action with the whole tool legible instead of one detail. Promote only if the see-through render reads as diagrammatic rather than real.


---

## `hero.image` — hero

**GIF: no** — The slot's job is recognition — a cold reader seeing themselves in a held state at the top of the page. A man braced against a seized knot is a state, not a transition. Every routed session has refused its hero on this ground and this one follows them.

**Recommended: A** — FIT decided it and PAGE LEGALITY confirmed it: 01-pain-scene is the only one of the three whose use_when names this exact beat, and spending it here leaves 06-relief-scene's requires_pair satisfied at item 5.

### A · `01-pain-scene` v1.18 · 16:9 · baseline

FIT: use_when names an advertorial header pain beat in the copy's own words — a person under a force, the symptom as physical fact. EVIDENCE: 1.18 is the owner-passed version with 54 rules verified present.

```
TYPE: 01-pain-scene v1.18
REGISTER: editorial photojournalism, natural and unstaged. Single frame.

SUBJECT: a man in his fifties crouched at a tent stake in the dark, both hands clamped on a guy line, pulling against it with his shoulders set and his weight back.

EVIDENCE: the knot at the stake is swollen and dark with rain, the cord flattened where it crosses itself, and his fingertips are white where they press into it.

COST: the rainfly behind him has lifted off the poles on that corner and stands away from the tent, one edge folded back on itself.

PLACE: a gravel campsite pitch beside water, well past midnight.

GAZE: down at the knot. Never at the lens.

LIGHT: the real light of the place and nothing added — a headlamp beam falling across his hands, the rest of the pitch dark.

GRADE: an ordinary photograph in ordinary light.

No product, no panels, no insets, no marks.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*976 characters · single-pass · attach the product photo.*

### B · `04-proof-lockedframe --timelapse` v1.13 · 16:9 · type: 04-proof-lockedframe

FIT: the headline is literally a state claim — knots seize when wind picks up. PROMPT RISK: two panels double the identity surface on a page whose product is small.

```
TYPE: 04-proof-lockedframe v1.13 --timelapse
REGISTER: documentary photography. No overlays, badges, arrows or text.

LAYOUT: two equal vertical panels, thin white gutter, no outer border.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CAMERA: handheld from the same standing position for both panels, same distance, same height, same lens.

SCENE: constant across both panels — one corner of a tent pitched on gravel, the same guy line running from the same stake to the same fly ring, the same water and treeline behind it.

VARIABLE: the only thing that changes is the line. LEFT panel — the line is slack and bowing, the fly corner lifted away from the pole. RIGHT panel — the same line drum-tight and straight, the fly corner pulled down flat, with the tensioner clipped where the line meets the fly ring.

PRODUCT: the tensioner is the subject of the right panel and is absent from the left, sized so the brass roller and the cam lever are both readable, never made the hero of the frame.

GRADE: one grade across both panels, flat overcast daylight, no warm boost.

JUDGEMENT: neither panel is favoured — same exposure, same framing, no vignette on either.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1433 characters · single-pass · attach the product photo.*

### C · `06-relief-hero` v1.17 · 16:9 · type: 06-relief-hero

FIT: weakest of the three for a problem-aware opener — it shows the resolved state before the problem has been made to hurt. Offered because the row holds it and the owner may want a warmer header.

```
TYPE: 06-relief-hero v1.17
REGISTER: ugc.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

SUBJECT: one man in his fifties, full figure, crouched at the corner of a pitched tent.

POSE: operated — mid-action, both hands on the tensioner, drawing the cord through it.

SETTING: one real campsite pitch filled to the edges — gravel underfoot, the tent wall behind him, a folding chair and a stuff sack at the frame edge, water and a treeline beyond. Never a blank ground.

LIGHT: flat early-morning daylight, no output to carry, no rim light and no glamour.

OFFSET: he sits to the left of frame; the taut guy line and the fly corner it holds occupy the right.

MARKS: none.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*940 characters · single-pass · attach the product photo.*

---

## `content.items.0.image` — problem-agitation

**GIF: yes** · `cause` · whole-frame · 16:9 · 3s · seamless loop

The section's claim IS a transition: a tensioned tarp letting go during a meal. The routed still is a two-panel locked frame of exactly that before and after, so the loop restages nothing — it is rung 1. The gif library's `cause` type names this shape, a fastening failing on the thing it holds.

> **brief** — A shade tarp rigged over two picnic tables, drum-tight and level. One guy line goes slack at the stake, the corner it held drops onto the table top, and the whole sheet settles into a sag that holds.

> **alt** — The same tarp corner and stake with nobody in frame, the line paying out through a cracked plastic runner until the corner drops.

> output `advertorial-cause-cord-tensioner-cam-lock-v01.mp4` · gifs-library/cause/ — no files filed yet; the folder card carries the law

**Recommended: A** — FIT would have chosen 01-pain-scene and PAGE LEGALITY overruled it: the hero spent that type, 01-pain-split is refused by never_with and 02-symptom-rail by its own editorial avoid_when, so the whole preference row is gone and A came from rung 3.

### A · `04-proof-lockedframe --timelapse` v1.13 · 16:9 · baseline

FIT: the copy is a before-and-after inside one scene, which is exactly what a locked frame holds. This slot is the page's weak point — see composition_notes.

```
TYPE: 04-proof-lockedframe v1.13 --timelapse
REGISTER: documentary photography. No overlays, badges, arrows or text.

LAYOUT: two equal vertical panels, thin white gutter, no outer border.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CAMERA: handheld from the same standing position for both panels, same distance, height and lens.

SCENE: constant across both panels — a large shade tarp rigged over two picnic tables at a lakeside site, the same four corners, the same tables laid for a meal, the same trees behind.

VARIABLE: the only thing that changes is the tarp. LEFT panel — the tarp drum-tight and level, every guy line straight. RIGHT panel — the same tarp sagging in its middle with one corner dropped to the table top, two lines slack and one stake pulled half out of the ground.

PRODUCT: absent from both panels. This is the failure, before the tool exists.

GRADE: one grade across both panels, dusk light going blue, no warm boost.

JUDGEMENT: neither panel is favoured — same exposure, same framing.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1288 characters · single-pass · attach the product photo.*

### B · `01-pain-scene` v1.18 · 16:9 · type: 01-pain-scene

FIT: the strongest match by use_when, and it is why the recommendation is contested. It is spent at the hero under one-type-once; picking it here forces the hero to its own B.

```
TYPE: 01-pain-scene v1.18
REGISTER: editorial photojournalism, natural and unstaged. Single frame.

SUBJECT: a man standing under a sagging shade tarp with one arm raised holding the fabric off the table, his other hand still gripping a slack guy line.

EVIDENCE: the tarp has dropped into a pocket above him and is holding a pool of rainwater, its edge folded down onto the table below.

COST: the picnic table under it is laid for a meal — plates, a bowl, a folded cloth — with the tarp edge now lying across one end of it.

PLACE: a lakeside campsite pitch at dusk.

GAZE: up at the sagging fabric. Never at the lens.

LIGHT: the real light of the place and nothing added.

GRADE: an ordinary photograph in ordinary light.

No product, no panels, no insets, no marks.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*855 characters · single-pass · attach the product photo.*

### C · `06-relief-scene` v3.7 · 16:9 · type: 06-relief-scene

FIT: weak. The type is a relief type used here for its unglamorous documentary register, showing the state before the tool exists.

```
TYPE: 06-relief-scene v3.7
REGISTER: candid documentary photograph, single frame.

SUBJECT: a man walking back to his car across a campsite carrying a bundled tarp under one arm, the tarp folded badly and trailing loose cord.

GAZE: candid, off to one side. Never on the lens.

ENVIRONMENT: an ordinary campground service road with numbered pitch posts and a bin store, a place anyone would pass through.

LIGHT: plain grey daylight, no glamour.

GRADE: muted, desaturated, never warm-boosted.

PRODUCT: absent. This frame is the state the tool has not yet changed.

RELIEF: none — he is bracing, shoulders up, the loose cord dragging.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*720 characters · single-pass · attach the product photo.*

---

## `content.items.1.image` — comparison

**GIF: no** — Temporal on its own — plastic cracking under a gusting load is a change. Refused on ADR-037: one loop per gif type per page, and `cause` is spent at content.items.0, where the copy's own breaking point sits and the loop is rung 1. Held as a reserve rather than dropped.

**Recommended: A** — FIT decided it. 02-cause-anatomy is the only one of the three whose use_when names an object being blamed for a measurable harm; the other two argue outcome and breadth.

### A · `02-cause-anatomy` v1.17 · 16:9 · baseline

FIT: the copy indicts a specific object and names how it harms — a culprit with a switchable state, which is this type's admission test. EVIDENCE: 1.17, 385-record ledger, and the removal test passes (take the cracked runner away and the line holds).

```
TYPE: 02-cause-anatomy v1.17
MEDIUM: 2D illustration, flat-vector — flat fills, hard edges, no gradients. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

FRAME: whole — the whole guy line from stake to fly ring in shot in both panels, the hardware small within it.

GROUND: a deep slate field. The value steps once at the panel divider: the right side is clearly lighter than the left.

BODY: a length of braided cord passing through a three-hole plastic runner, cord and runner in warm ivory over a translucent outline, the same cord and the same runner at the same scale and angle in both panels. Not a knot, not a rope diagram.

PANELS: LEFT — the plastic runner cracked across one hole and splayed open, the cord slipped through and the line gone slack. RIGHT — the same cord held in the cam tensioner instead, the cord bitten flat by the cam and the line straight. Neither the culprit nor the product covers the structure under argument. Both are drawn beside it or behind it, and the structure is fully visible in BOTH panels.

MARKS: THREE.
`measure` — exactly two dashed straight lines, one per panel, red in the left and blue in the right, identical thickness and dash pattern. Each spans from THE STAKE EYE to THE FLY RING, stopping exactly at those two landmarks and running past neither. Both start at the stake eye. Only the slack between them differs; the left bows and the right is straight.
`contour` — one curved line tracing the CRACKED EDGE of the plastic runner in the left panel, red; one curved line tracing the CAM'S GRIPPING FACE in the right panel, blue. One line per panel.
`verdict-hazard` — exactly two badges in the TOP corners: a red warning triangle over the left panel and a green disc with a check cut out of it over the right, the triangle and the disc the same height.

THE DIFFERENCE MUST SURVIVE THE MARKS BEING COVERED: cover the dashed lines and the badges with a thumb, and the left and right panels must still read as wrong and right from the structure alone.

Colour follows G3: red wrong, blue correct, green only in the badge.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*2364 characters · single-pass · attach the product photo.*

### B · `04-proof-lockedframe --rivals` v1.13 · 16:9 · type: 04-proof-lockedframe

FIT: --rivals is built for exactly this — the alternatives shown as they really fail. Second only because the copy argues MECHANISM of failure, not a side-by-side outcome.

```
TYPE: 04-proof-lockedframe v1.13 --rivals
REGISTER: documentary photography. No overlays, badges, arrows or text.

LAYOUT: three equal vertical panels, thin white gutters, no outer border.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CAMERA: handheld from the same position for all three panels, same distance, height and lens.

SCENE: constant across every panel — the same tent stake in the same gravel, the same guy line running up out of frame, the same treeline behind.

VARIABLE: the only thing that changes is what holds the line. PANEL 1 — a three-hole plastic runner, cracked across one hole, the line slack. PANEL 2 — a bungee cord stretched long and thin, its hook twisted sideways on the stake. PANEL 3 — the cam tensioner, the line above it straight and hard.

PRODUCT: the tensioner is the subject of panel 3 only, at the same size and distance as the rival hardware in panels 1 and 2, never enlarged or lit differently.

GRADE: one grade across all three panels, flat overcast daylight.

JUDGEMENT: no panel is favoured — same exposure, same framing, no vignette, and the rivals are shown as they really fail rather than staged to look worse.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1429 characters · single-pass · attach the product photo.*

### C · `03-use-grid` v1.0 · 16:9 · type: 03-use-grid

FIT: weakest — compatibility cells show which anchors the tool serves, which answers a different question than why the rivals fail.

```
TYPE: 03-use-grid v1.0
LAYOUT: 2x2 photographic grid, thin white gutters, no outer border, no numbers, no arrows, no badges, no text.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly. Preserve it exactly in every cell where it appears.

CELL VARIABLE — compatibility. Each cell shows a DIFFERENT anchor the tensioner serves, staged in that anchor's own context, with the tool visibly FITTED in every cell:
  cell 1 — a steel tent stake driven into gravel, the tool clipped to the stake eye;
  cell 2 — a truck bed tie-down cleat, the tool hanging from the cleat under load;
  cell 3 — an awning arm on a parked van, the tool clipped to the arm ring;
  cell 4 — a tree trunk with a webbing strap round it, the tool clipped to the strap loop.

CAMERA — different in every cell: cell 1 low at ground level; cell 2 standing, looking down into the bed; cell 3 at arm's length along the van side; cell 4 close and level against the bark. A real outdoor place per cell.

The tool is the same unit in all four cells, at a size and angle where the brass roller and the cam lever are both clearly visible. No cell contains a person's face.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1395 characters · single-pass · attach the product photo.*

---

## `content.items.2.image` — cause

**GIF: yes** · `mechanism` · whole-frame · 16:9 · 3s · seamless loop

The beat is a mechanism doing its work — a cam closing on a cord the instant pulling stops. That is a state changing, and the routed still is already a see-through render of the same parts, so the loop is the same frame in motion. Rung 1.

> **brief** — A see-through view of the tensioner. The cord is drawn through the brass roller and the roller turns; pulling stops and the spring-loaded cam swings down and bites the braid, holding it still.

> **alt** — The same view with the quick-release lever lifted at the end, the cam opening and the cord running free again.

> output `advertorial-mechanism-cord-tensioner-cam-lock-v01.mp4` · gifs-library/mechanism/ — no files filed yet; the folder card carries the law

**Recommended: A** — PAGE LEGALITY decided it against FIT: 02-cause-anatomy is the better answer to this copy and is spent at item 1, where its culprit is a physical object rather than a physical effect. The compromise is recorded rather than hidden.

### A · `03-mechanism-xray` v1.3 · 16:9 · baseline

FIT: the beat is why one mechanism seizes and the other does not, and the see-through render is the only type on this page that can put the cam and the spring in the same frame as the cord path. PROMPT RISK: the copy is about the KNOT and this answers with the TOOL — a real gap, see composition_notes.

```
TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CANVAS: a deep blue-grey field, darker than the brass, with no pattern and no horizon.

SHELL: the cam tensioner seen from the side, its stainless steel body shell rendered translucent so the working parts read through it, the outer silhouette exactly as the reference photo — same proportions, same lever profile, same roller position.

INTERNALS, named and placed: the marine-grade brass roller at the cord entry, turning where the cord first bears on it; the spring-loaded stainless steel cam above the cord's exit path, its toothed face bitten down into the braid; the torsion spring behind the cam holding it closed; and the reflective cord itself running through the body from roller to cam.

MARKS: ONE.
`working` — the cam's toothed face where it grips the cord, lit as the brightest thing in the frame. Nothing else in the frame is marked.

The marks are the only added colour.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1292 characters · single-pass · attach the product photo.*

### B · `02-cause-anatomy` v1.17 · 16:9 · type: 02-cause-anatomy

FIT: the closest match by use_when — fibres are the structure, the wet hitch is the culprit. Refused only by one-type-once, which spent it at item 1.

```
TYPE: 02-cause-anatomy v1.17
MEDIUM: 2D illustration, airbrushed — soft gradients, modelled volume. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

FRAME: whole — the whole hitch and the cord running to it in shot in both panels, the hardware small within it.

GROUND: a deep ochre field. The value steps once at the panel divider: the right side is clearly lighter than the left.

BODY: a magnified cross-section of braided cord where it crosses itself, the individual sheath fibres and the inner core in warm ivory over a translucent outline, the same crossing at the same scale and angle in both panels. Not a rope diagram, not a knot chart.

PANELS: LEFT — the two passes of a wet hitch crushed into each other, the sheath fibres splayed and locked between them. RIGHT — the same cord passing over the brass roller and under the cam instead, the fibres round and undistorted where they run. Neither the culprit nor the product covers the structure under argument. Both are drawn beside it or behind it, and the structure is fully visible in BOTH panels.

MARKS: THREE.
`measure` — exactly two dashed straight lines, one per panel, red in the left and blue in the right, identical thickness and dash pattern. Each spans from THE OUTER EDGE OF THE UPPER PASS to THE OUTER EDGE OF THE LOWER PASS, stopping exactly at those two landmarks and running past neither. Both start at the upper edge. Only the thickness between them differs; the left is about a third of the right.
`pressure` — a filled region bounded by the CONTACT SURFACE where the two passes bear on each other, as wide as the contact itself, never a line and never a glow along an edge: red in the left panel; the same region blue in the right where the roller carries the load instead.
`verdict-glyph` — exactly two badges in the TOP corners, same diameter: a filled red disc with an X cut out of it over the left panel, a filled green disc with a check cut out of it over the right.

THE DIFFERENCE MUST SURVIVE THE MARKS BEING COVERED: cover the dashed lines and the badges with a thumb, and the left and right panels must still read as wrong and right from the structure alone.

Colour follows G3: red wrong, blue correct, green only in the badge.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*2510 characters · single-pass · attach the product photo.*

### C · `03-spec-explode` v1.7 · 16:9 · type: 03-spec-explode

FIT: weak here. An exploded view answers what the tool contains, not why a knot locks.

```
TYPE: 03-spec-explode v1.7
REGISTER: 3D technical render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CANVAS: a deep neutral field, clearly darker than the brass and steel so the parts separate from it. The motif comes from what the tool DOES — a faint suggestion of taut parallel cord lines in the ground, low contrast.

FRAMING: full-frame. The stack fills the frame with even margins.

STACK, in assembly order along one axis, separated by clean even gaps: the anchor loop, the stainless steel body shell, the marine-grade brass roller, the spring-loaded stainless steel cam, its torsion spring, the quick-release lever, and the reflective cord threaded through where it runs.

CENSUS: only these seven parts. The tool genuinely contains nothing else — do not invent bearings, gears, ratchets, fasteners or electronics.

FOCUS: the spring-loaded cam, at the optical centre, rendered sharper and larger than the parts around it, its gripping teeth fully resolved.

STYLE: premium technical product visualization, sharp, high detail.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1324 characters · single-pass · attach the product photo.*

---

## `content.items.3.image` — mechanism

**GIF: yes** · `use` · whole-frame · 16:9 · 4s · seamless loop

The copy is an operation with a stated duration — tension in under five seconds — which is a sequence rather than a state. The routed still is hands mid-pull, so the loop completes the action the frame already began.

> **brief** — Two hands at a tent guy line. The cord is pulled steadily through the tensioner, the slack running out of the line above until it comes straight and hard, and the hands let go with the line still taut.

> **alt** — The same hands and line seen from the stake end, the cord coming tight and the fly corner above pulling down flat as it does.

> output `advertorial-use-cord-tensioner-cam-lock-v01.mp4` · gifs-library/use/ — no files filed yet; the folder card carries the law

**Recommended: A** — PAGE LEGALITY decided it. 03-spec-explode is the best fit for 'two precise metal parts', and its own avoid_when forbids it adjacent to 03-mechanism-xray on one page — item 2 holds the xray. It moves to item 6, where the same parts argue durability instead.

### A · `06-relief-hero` v1.17 · 16:9 · baseline

FIT: moderate. The copy describes the mechanism and this shows it working in a hand at working distance. Chosen because 03-spec-explode, the natural first choice, is barred here — see composition_notes.

```
TYPE: 06-relief-hero v1.17
REGISTER: commercial.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

SUBJECT: one person reduced to hands and forearms, drawing the reflective cord through the tensioner.

POSE: operated — mid-action, one hand steadying the body of the tool, the other pulling the cord clear of the roller.

SETTING: one real campsite pitch filled to the edges — the tent wall and a guy line behind the hands, gravel below, a stuff sack at the frame edge. Never a blank ground.

LIGHT: flat morning daylight. No output has to carry, so no rim light, no glow, no glamour.

OFFSET: the hands sit to the right of frame; the taut line running away to the stake occupies the left.

PRODUCT VIEW: not needed — the hero shows the roller and the cam clearly at working distance.

MARKS: none.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1064 characters · single-pass · attach the product photo.*

### B · `03-mechanism-xray` v1.3 · 16:9 · type: 03-mechanism-xray

FIT: high by use_when, but it is spent at item 2 under one-type-once.

```
TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CANVAS: a deep charcoal field, darker than the brass, no pattern and no horizon.

SHELL: the cam tensioner seen three-quarter from above, its body shell translucent so the working parts read through it, the outer silhouette exactly as the reference photo.

INTERNALS, named and placed: the brass roller at the cord entry where the cord first bears on it; the spring-loaded stainless steel cam above the exit path, its toothed face closed on the braid; the torsion spring behind the cam; the quick-release lever on the outside of the shell, linked to the cam.

MARKS: ONE.
`working` — the toothed face of the cam where it bites the cord, the brightest thing in frame. Nothing else is marked.

The marks are the only added colour.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1134 characters · single-pass · attach the product photo.*

### C · `02-cause-anatomy` v1.17 · 16:9 · type: 02-cause-anatomy

FIT: it can carry a cord-over-a-corner comparison, but the beat here is the product's own mechanism, not a culprit.

```
TYPE: 02-cause-anatomy v1.17
MEDIUM: 2D illustration, paper-cut — flat layered shapes with soft drop shadows. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

FRAME: whole — the whole cord path in shot in both panels, the hardware small within it.

GROUND: a deep teal field. The value steps once at the panel divider: the right side is clearly lighter than the left.

BODY: a length of braided cord and the surface it bears on, both in warm ivory over a translucent outline, the same cord at the same scale and angle in both panels. Not a knot chart.

PANELS: LEFT — the cord dragged across a sharp plastic corner, the braid deformed where it turns. RIGHT — the same cord running over the brass roller, the braid round and the turn smooth. Neither the culprit nor the product covers the structure under argument. Both are drawn beside it or behind it, and the structure is fully visible in BOTH panels.

MARKS: TWO.
`measure` — exactly two dashed straight lines, one per panel, red in the left and blue in the right, identical thickness and dash pattern. Each spans from THE ENTRY POINT OF THE TURN to THE EXIT POINT OF THE TURN, stopping exactly at those two landmarks and running past neither. Both start at the entry. Only the angle between them differs.
`verdict-thumb` — exactly two badges in the TOP corners, same diameter: a red disc with a thumbs-down cut out of it over the left panel, a green disc with a thumbs-up cut out of it over the right. Each thumb is a flat pictogram cut out of the disc, a solid silhouette, never a photographed or three-dimensional hand.

THE DIFFERENCE MUST SURVIVE THE MARKS BEING COVERED: cover the dashed lines and the badges with a thumb, and the left and right panels must still read as wrong and right from the structure alone.

Colour follows G3: red wrong, blue correct, green only in the badge.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*2135 characters · single-pass · attach the product photo.*

---

## `content.items.4.image` — how-to-use

**GIF: no** — The slot exists to reveal BREADTH — four jobs the tool is rated for. A grid enumerates rather than changes, and revealing does not earn motion. The gif library's own `unboxing` boundary note draws this line.

**Recommended: A** — FIT decided it, and this slot is the only one on the page where the preference row's first entry and the best fit are the same type. NOTE: options A and B share a type, so this slot carries two distinct types and declares it in pool_basis.

> **pool_basis** — Options A and B are the same type on a different layout axis. After the refusals recorded in page_composition_notes and the 16:9 ratio filter, nine types remain for nine 16:9 slots — an exact fit with no slack, so this slot could not draw a third distinct type without taking one already recommended elsewhere.

### A · `03-use-grid` v1.0 · 16:9 · baseline

FIT: the copy lists four named jobs and a boundary, which is the applications cell variable exactly. EVIDENCE: 1.0, promoted 2026-08-26; the CAMERA block is required since 0.4 and is unrendered, so this is a real test.

```
TYPE: 03-use-grid v1.0
LAYOUT: 2x2 photographic grid, thin white gutters, no outer border, no numbers, no arrows, no badges, no text.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly. Preserve it exactly in every cell where it appears.

CELL VARIABLE — applications. Each cell shows the tensioner mid-job on a DIFFERENT task, the tensioned line visibly drum-tight in every cell:
  cell 1 — tensioning a guy line from a tent stake to the rainfly on a coastal pitch, the fly taut behind it;
  cell 2 — cinching a shade tarp corner down to a picnic table leg, the tarp edge pulled flat;
  cell 3 — strapping a load in a truck bed, the cord running over the cargo and locked at the cleat;
  cell 4 — holding an awning line to a ground anchor beside a parked van, the awning edge steady.

CAMERA — different in every cell: cell 1 low and close at stake height; cell 2 standing, looking down across the table; cell 3 half a metre back over the tailgate; cell 4 at arm's length along the line from the anchor. A real outdoor place per cell, never one studio ground for all four.

The tool is the same unit in all four cells, at a size and angle where the brass roller and the cam lever are both clearly visible. No cell contains a person's face.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1504 characters · single-pass · attach the product photo.*

### B · `03-use-grid` v1.0 · 16:9 · axis: layout=3-cell

The same type held to the three jobs strictly inside the load limit, dropping the truck-bed cell that sits closest to the boundary the copy draws.

```
TYPE: 03-use-grid v1.0
LAYOUT: 3 equal cells in one row, thin white gutters, no outer border, no numbers, no arrows, no badges, no text.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly. Preserve it exactly in every cell where it appears.

CELL VARIABLE — applications, held to the three jobs inside the stated load limit:
  cell 1 — a guy line on a tent rainfly, the line straight from stake to ring;
  cell 2 — a shade canopy corner pulled down to a leg, the fabric edge flat;
  cell 3 — a light load in a truck bed, the cord over it and locked.

CAMERA — different in every cell: cell 1 kneeling at stake height; cell 2 standing back at the canopy corner; cell 3 close over the tailgate looking down. A real outdoor place per cell.

The tool is the same unit in all three cells, the brass roller and cam lever clearly visible in each. No cell contains a person's face. Nothing in any cell is a heavy load-bearing application.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1194 characters · single-pass · attach the product photo.*

### C · `04-proof-lockedframe --capture` v1.13 · 16:9 · type: 04-proof-lockedframe

FIT: --capture can show the load and release cycle in one locked frame, which argues the limit differently — by demonstrating the release rather than listing the jobs.

```
TYPE: 04-proof-lockedframe v1.13 --capture
REGISTER: documentary photography. No overlays, badges, arrows or text.

LAYOUT: three equal vertical panels, thin white gutters, no outer border.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CAMERA: handheld from one standing position for all three panels, same distance, height and lens.

SCENE: constant across every panel — the same tensioner on the same line, anchored to the same stake in the same gravel, the same treeline behind.

VARIABLE: the only thing that changes is the load on the line. PANEL 1 — no load, the cord slack through the roller. PANEL 2 — a working load, the cord straight and the cam closed on it. PANEL 3 — the quick-release lever lifted, the cord running free again.

PRODUCT: the tensioner is the subject of every panel, same size and position in each, never made the hero of the frame.

GRADE: one grade across all three panels, flat overcast daylight.

JUDGEMENT: no panel is favoured — same exposure, same framing, no vignette.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1276 characters · single-pass · attach the product photo.*

---

## `content.items.5.image` — outcome

**GIF: yes** · `relief` · whole-frame · 16:9 · 4s · seamless loop

The relief here is defined by something NOT happening while the wind does — the copy's whole point is that she no longer watches the fly. A still cannot show a non-event; a loop can, because the wind moves and nothing gives. This is the one slot on the page where motion carries an argument the still cannot.

> **brief** — A woman with a mug at the door of a pitched tent, watching the water. The wind moves her jacket and the grass around the pitch; the rainfly behind her stays drum-tight and does not move. She does not look at it.

> **alt** — The same pitch with nobody in frame — the wind through the grass and the fly holding still above a taut guy line.

> output `advertorial-relief-cord-tensioner-cam-lock-v01.mp4` · gifs-library/relief/ — no files filed yet; the folder card carries the law

**Recommended: A** — FIT decided it and PAGE LEGALITY confirmed the pairs_with. The distinction against B is that relief-scene keeps the product in the scene as the reason rather than presenting it, which is what 'I did not dread' asks for.

### A · `06-relief-scene` v3.7 · 16:9 · baseline

FIT: the copy is a person living the resolved state in an ordinary place, which is this type's use_when verbatim. PAGE LEGALITY: pairs_with is satisfied — 01-pain-scene serves the hero, same person.

```
TYPE: 06-relief-scene v3.7
REGISTER: candid documentary photograph, single frame.

SUBJECT: a woman standing at the open door of a pitched tent with a mug in one hand, weight on one hip, watching the water while the wind moves her jacket.

GAZE: candid, out across the bay. Never on the lens.

ENVIRONMENT: an ordinary coastal campground anyone would pass through — numbered pitch post, gravel, a folding chair, other tents further along.

LIGHT: plain grey daylight off the water, no glamour.

GRADE: muted, desaturated, never warm-boosted.

PRODUCT: the tensioner is in the scene as the reason, clipped to the guy line beside her, never presented and never held up.

RELIEF: the moment of letting go in a situation that would have demanded bracing — the wind is visibly up, the fly is drum-tight and still, and she is not looking at it.

MARKS: none.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*937 characters · single-pass · attach the product photo.*

### B · `06-relief-hero` v1.17 · 16:9 · type: 06-relief-hero

FIT: strong, but it presents the product where the copy is about not thinking about it.

```
TYPE: 06-relief-hero v1.17
REGISTER: ugc.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

SUBJECT: one woman, full figure, sitting in a folding chair outside a pitched tent with a mug held in both hands.

POSE: passive — relaxed, gaze away from the lens and out across the water.

SETTING: one real coastal pitch filled to the edges — the tent behind her with its fly taut, gravel, a stuff sack and a boot at the frame edge, the bay beyond. Never a blank ground.

LIGHT: flat grey daylight off the water. No output has to carry, so no rim light and no glow.

OFFSET: she sits to the right of frame; the taut guy line and the tensioner holding it occupy the left.

MARKS: none.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*945 characters · single-pass · attach the product photo.*

### C · `05-social-handoff` v2.9 · 16:9 · type: 05-social-handoff

FIT: moderate — the brand context names a stranger producing the tool before a storm, but that is the product_end beat, not this one.

```
TYPE: 05-social-handoff v2.9
REGISTER: candid documentary photograph, natural, unposed, sharp.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

MOMENT: what the tool just did is visible in frame — the fly of the tent behind them is drum-tight, the guy line straight from stake to ring with the tensioner closed on it.

ADVOCATE: a woman who has just finished pitching, one hand still resting on the taut line, her eyes on the person beside her.

LISTENER: a second camper, face NOT visible, turned away from the lens with their attention on the line and the tensioner.

PRODUCT: the tensioner is dominant in the lower third of the frame, closer to the camera than either face, and nothing beside it competes for attention.

HANDOFF: the advocate is holding a second tensioner out flat on her open palm toward the listener — an OFFER, held still, not a movement in progress.

ENVIRONMENT: a real reason both people are here — adjacent pitches on a coastal campground, gravel underfoot, the other tent a few metres away.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1286 characters · single-pass · attach the product photo.*

---

## `content.items.6.image` — comparison

**GIF: no** — An exploded technical render reveals STRUCTURE. Separating parts on screen is a camera move, not a state changing, and the cost argument it carries is a comparison rather than an event.

**Recommended: A** — EVIDENCE and PAGE LEGALITY together. A is here because item 3 could not hold it (03-mechanism-xray sits adjacent there), and the durability reading of the same parts is a legitimate second argument rather than a fallback.

### A · `03-spec-explode` v1.7 · 16:9 · baseline

FIT: the cost argument rests on what the tool is made of — brass and stainless where the rivals are plastic — and the exploded view is the only type that can put the roller at the optical centre. Displaced here from item 3 by an avoid_when adjacency.

```
TYPE: 03-spec-explode v1.7
REGISTER: 3D technical render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CANVAS: a deep neutral field, clearly darker than the brass and steel so the parts separate from it. The motif comes from what the tool DOES — a faint suggestion of taut parallel cord lines in the ground, low contrast, never a pattern that competes.

FRAMING: full-frame. The stack fills the frame with even margins.

STACK, in assembly order along one axis, separated by clean even gaps: the anchor loop, the stainless steel body shell, the marine-grade brass roller, the spring-loaded stainless steel cam, its torsion spring, the quick-release lever, and the reflective cord threaded through where it runs.

CENSUS: only these seven parts. The tool genuinely contains nothing else — do not invent bearings, gears, ratchets, fasteners or electronics.

FOCUS: the marine-grade brass roller. It sits at the optical centre of the stack, rendered sharper and larger than the parts around it, its bearing surface fully resolved — the part that survives seasons where a plastic runner cracks.

STYLE: premium technical product visualization, sharp, high detail.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1448 characters · single-pass · attach the product photo.*

### B · `04-proof-lockedframe --rivals` v1.13 · 16:9 · type: 04-proof-lockedframe

FIT: high — a season's discards beside one tool is the cost argument made literal. Second because --rivals is already offered at item 1 and the page would read as two of the same comparison.

```
TYPE: 04-proof-lockedframe v1.13 --rivals
REGISTER: documentary photography. No overlays, badges, arrows or text.

LAYOUT: three equal vertical panels, thin white gutters, no outer border.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CAMERA: handheld from the same position for all three panels, same distance, height and lens.

SCENE: constant across every panel — the same square of workbench, the same daylight from the same window, the same plain surface.

VARIABLE: the only thing that changes is what is laid out. PANEL 1 — a heap of cracked plastic runners and a snapped bungee, the season's discards. PANEL 2 — a heavy ratchet strap set, coiled and bulky. PANEL 3 — one cam tensioner with its cord, coiled flat.

PRODUCT: the tensioner is the subject of panel 3 only, at the same distance and lighting as the hardware in the other two, never enlarged.

GRADE: one grade across all three panels, plain window daylight.

JUDGEMENT: no panel is favoured — same exposure, same framing, no vignette, and the rivals are shown as they really are rather than staged to look worse.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1352 characters · single-pass · attach the product photo.*

### C · `06-relief-hero` v1.17 · 16:9 · type: 06-relief-hero

FIT: weak for a cost beat; it shows the tool in use rather than against what it replaces.

```
TYPE: 06-relief-hero v1.17
REGISTER: commercial.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

SUBJECT: one person reduced to hands and forearms, coiling the reflective cord around a closed tensioner.

POSE: operated — mid-action, the cord being wound, the cam closed.

SETTING: one real gear-packing scene filled to the edges — an open pack on a tailgate, a folded tarp, stakes in a pouch, gravel beyond. Never a blank ground.

LIGHT: flat overcast daylight, no output to carry, no rim light.

OFFSET: the hands sit to the left of frame; the open pack with the rest of the kit occupies the right.

PRODUCT VIEW: not needed — the hero shows the roller and the cam at working distance.

MARKS: none.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*969 characters · single-pass · attach the product photo.*

---

## `product.image` — mechanism

**GIF: no** — A macro reveals SURFACE. The cam bite it shows is a moment, but `mechanism` is spent at content.items.2 where the same action reads at working scale (ADR-037, one loop per gif type per page).

**Recommended: A** — FIT decided it, and the ratio settled the field before FIT ran: 03-spec-macro declares 1:1 only, so this is the sole slot on the page it can serve.

### A · `03-spec-macro` v1.0 · 1:1 · baseline

FIT: the spec table names materials and the card is 1:1 — this is the only slot on the page whose ratio admits this type at all, and build quality at surface scale is its purpose. Its counts elsewhere are provenance; this is its first render on an advertorial.

```
TYPE: 03-spec-macro v1.0
REGISTER: polished commercial studio macro photography. Extreme close range.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly. The magnified region must be a TRUE region of that tool — same geometry, same material, same finish. Do not redesign, simplify or add features.

MACRO SUBJECT: the cam and roller pair filling 80% of the frame — the toothed face of the stainless steel cam bitten down into the braided cord, every tooth individually resolved, and the marine-grade brass roller beneath it with the cord bearing across it.

LIGHT BEHAVIOR LAW: hard raking light puts a warm specular streak along the turned brass of the roller and a hard cold glint on the crown of each cam tooth, while the braided cord between them is matte and returns none — so brass, steel and cord read as three materials at the lines where they meet, not as one machined mass.

ACTION ANCHOR: the pair caught under load, the cord pulled hard through the roller and pinched flat under the cam teeth. Motion minimal.

FRAME: nothing but the tool and the cord it holds. No hand, no tent, no background object, no surface pattern.

SIGNAL SILENCE: no glow rims, no emblems, no etched badges, no colour-coded highlights.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1486 characters · single-pass · attach the product photo.*

### B · `03-mechanism-xray` v1.3 · 1:1 · type: 03-mechanism-xray

FIT: strong, but spent at item 2 under one-type-once.

```
TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CANVAS: a deep blue-grey field, darker than the brass, no pattern and no horizon.

SHELL: the cam tensioner square to camera, its body shell translucent so the working parts read through it, the outer silhouette exactly as the reference photo.

INTERNALS, named and placed: the brass roller at the cord entry; the spring-loaded stainless steel cam above the exit path with its toothed face closed on the braid; the torsion spring behind the cam; the quick-release lever on the shell, linked to the cam.

MARKS: ONE.
`working` — the toothed face of the cam where it grips the cord, the brightest thing in frame. Nothing else is marked.

The marks are the only added colour.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1078 characters · single-pass · attach the product photo.*

### C · `05-persona-grid` v1.6 · 1:1 · type: 05-persona-grid

FIT: weak for a spec card, but it is ratio-legal at 1:1 and answers who uses it, which a recommendation card can carry.

```
TYPE: 05-persona-grid v1.6 --2x2
LAYOUT: 2x2 cells, thin white gutters, no outer border.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CONSTANT across every cell: the same tensioner, the same reflective cord, the same flat overcast daylight, the same distance from the subject.

VARIATION cell by cell: a different person and a different place — cell 1 an older man at a tent stake on gravel; cell 2 a woman at a truck tailgate; cell 3 a young man at an awning arm beside a van; cell 4 a woman at a garden trellis line.

PRODUCT: the tensioner is visible and unobstructed in EVERY cell, held or clipped where it is working, never hidden behind a hand.

CELLS: cell 1 is the hero — the fullest view of the tool in use; the other three support it.

REGISTER: clean lifestyle collage for e-commerce, bright, airy, sharp.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1088 characters · single-pass · attach the product photo.*

---

## `product_end.image` — how-to-use

**GIF: no** — The handoff act is legislated as a STATE a still frame can hold — an offer, held, never a movement in progress (05-social-handoff PARTS/handoff). Animating it would break the type's own law.

**Recommended: A** — FIT decided it against a near-tie with B, and PAGE LEGALITY broke the tie: 03-use-grid serves item 4, and two grids on one page spend the variation budget in the dimension that buys least.

### A · `05-social-handoff` v2.9 · 16:9 · baseline

FIT: the brand context names this scene outright — a stranger at the next campsite produces the tool right before a storm — and a six-pack is a thing you hand one of to someone. The handoff act is an OFFER, a state a still frame can hold.

```
TYPE: 05-social-handoff v2.9
REGISTER: candid documentary photograph, natural, unposed, sharp.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

MOMENT: what the tool just did is visible in frame — behind the two people a tarp is drum-tight over a picnic table, its corner line straight and locked, while the sky behind it is already dark with the coming squall.

ADVOCATE: a man who has just finished tensioning that line, one hand still on the taut cord, his eyes on the person beside him.

LISTENER: a camper from the next pitch, face NOT visible, turned away from the lens with their attention on the tarp corner and the tool.

PRODUCT: a tensioner is dominant in the lower third of the frame, closer to the camera than either face, and nothing beside it competes for attention.

HANDOFF: the advocate is holding out a spare tensioner from the pack, flat on his open palm toward the listener — an OFFER, held still, not a movement in progress.

ENVIRONMENT: a real reason both people are here — neighbouring pitches on a coastal campground with the wind already moving the trees.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1350 characters · single-pass · attach the product photo.*

### B · `03-use-grid` v1.0 · 16:9 · type: 03-use-grid

FIT: high — the copy lists four jobs the set covers. Second only because item 4 already carries a use-grid and the page would read as two grids.

```
TYPE: 03-use-grid v1.0
LAYOUT: 2x2 photographic grid, thin white gutters, no outer border, no numbers, no arrows, no badges, no text.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly. The product IS A SET, so each cell shows one unit from the pack — but only a unit visible in the reference photo, with its material and colour preserved exactly.

CELL VARIABLE — applications. Each cell shows one unit of the set mid-job on a different task, the tensioned line drum-tight in every cell:
  cell 1 — a tent guy line to a stake, the fly taut behind it;
  cell 2 — a tarp corner cinched to a picnic table leg;
  cell 3 — a load strapped in a truck bed, the cord locked at the cleat;
  cell 4 — an awning line held to a ground anchor beside a van.

CAMERA — different in every cell: cell 1 low at stake height; cell 2 standing over the table; cell 3 half a metre back over the tailgate; cell 4 at arm's length along the line. A real outdoor place per cell.

Every unit is recognisably from the same pack — same brass roller, same cam, same reflective cord. No cell contains a person's face.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1351 characters · single-pass · attach the product photo.*

### C · `03-spec-explode` v1.7 · 16:9 · type: 03-spec-explode

FIT: moderate — it argues what one unit contains, where the copy argues what six units let you do.

```
TYPE: 03-spec-explode v1.7
REGISTER: 3D technical render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the cam-lock cord tensioner — brass roller, stainless steel cam, quick-release lever, reflective cord. Preserve its shape, proportions, material and finish exactly.

CANVAS: a deep neutral field, clearly darker than the brass and steel so the parts separate from it. The motif comes from what the tool DOES — a faint suggestion of taut parallel cord lines, low contrast.

FRAMING: full-frame. The stack fills the frame with even margins.

STACK, in assembly order along one axis, separated by clean even gaps: the anchor loop, the stainless steel body shell, the marine-grade brass roller, the spring-loaded stainless steel cam, its torsion spring, the quick-release lever, and the reflective cord threaded through where it runs.

CENSUS: only these seven parts. The tool genuinely contains nothing else — do not invent bearings, gears, ratchets, fasteners or electronics.

FOCUS: the quick-release lever. It sits at the optical centre of the stack, rendered sharper and larger than the parts around it, its pivot and its link to the cam fully resolved — the part that drops a loaded line in one second.

STYLE: premium technical product visualization, sharp, high detail.

No text, no letters, no numbers, no logo, no badge, no arrow anywhere in the frame.
```

*1398 characters · single-pass · attach the product photo.*

---

## `reviews.shots.0-3.image` — social-proof

**GIF: no** — The slot carries no still either — G14 bars a generated image in a block that names verified reviewers, and a loop is no less generated.

**No image.** These four photo slots sit in a block carrying named Verified Purchase reviewers. 05-social-snapshot's avoid_when forbids pairing a generated snapshot with a reviewer name or verified badge — a fabricated endorsement (FTC). They need real customer photographs.


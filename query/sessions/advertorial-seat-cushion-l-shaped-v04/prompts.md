# Image prompts — page 104, ergonomic memory foam seat cushion

GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit the script and re-run. Routing rationale, the negative motion verdicts and the out-of-scope slots are all in `prompts.json`.

- page `104` · advertorial · solution-aware · registry `2.0.0` · 11 routed slots · 19 prompts · 3 motion briefs
- motion: 3 loops, floor 2, margin 1, groups result, working — including the library's **first `form: inset` loop**
- **2 options carry a RESERVED BLOCK** — the render has an empty grey panel where the loop goes and is not shippable until it is filled
- **4 prompts carry a blocking precondition**, stated on each

---

## `hero.image` — hero

- asset `104-01-hero-pain-scene.png` · advertorial header, under the eyebrow and above the byline
- recommended: **option A** · media **still**
- FIT decides, close to verbatim. 01-pain-scene --candid asks for physical pain in a moment nobody would choose to be seen in, and hero.body.0 is that moment in the page's own words — bracing both arms against the steering wheel just to find the leverage to stand. A plays it as that single action. B moves to the confront gaze, which the type reserves for appearance and self-image rather than physical pain. C moves it to the bleacher steps, which is the cost the copy names second and which features.items.3 later resolves. RATIO: 01-pain-scene declares 16:9 and this template is 16:9 above the review grid, so nothing is cropped. PAGE LEGALITY: A satisfies 06-relief-scene's requires_pair at features.items.3 and pairs_with 04-proof-lockedframe at features.items.2. PRODUCT PRESENCE: none, correctly. PROMPT RISK: 1431 characters against a measured band of 1379-2153.

### hero.image · option A — `01-pain-scene` `--candid`

- varies on: baseline
- ratio `16:9` · type version `1.14` · `gaze: candid`
- The page's opening scene as one action: both arms locked on the wheel to lever himself off the seat at six in the evening. Evidence is the symptom as physical fact — hips below knees, the lumbar curve flat, the load on the base of the spine.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his mid-forties in a creased shirt with the tie pulled loose, still in the driver's seat of his car on his own driveway at six in the evening, mid-way through pushing himself up off the seat with both arms locked straight against the top of the steering wheel. Under that force: both elbows rigid and taking his whole weight, shoulders driven up towards his ears, hips barely off the seat, his back held in one unbending piece. Face: eyes shut, jaw clamped, breath held.

His hips sit well below his knees in the backward-sloping seat, his lower back is pressed flat against the seat back with an open gap behind it, and the whole load has gone onto the base of his spine.

One specific place: a suburban driveway at the end of a nine-hour day, the driver's door already open behind him, and the lived-in clutter of the commute — a lanyard hung on the indicator stalk, a cold coffee in the holder, a child's shin pad in the passenger footwell, a parking permit clipped to the visor.

He is unaware of the camera. Key light: the last cold blue daylight through the windscreen. Fill: the weak dome light above him. A rim of light along his locked forearms. Deep shadow across the near third of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### hero.image · option B — `01-pain-scene` `--confront`

- varies on: axis: gaze=confront
- ratio `16:9` · type version `1.14` · `gaze: confront`
- The same argument in the type's other gaze, in the hallway a minute later. The advertorial hero cell holds one type and the gates leave no second, so the honest variation is the axis.
- **note:** The type reserves --confront for appearance and daily frustration rather than physical pain; it is offered because the axis is the only legal second dimension here, not because it fits better.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his mid-forties in a creased work shirt, standing in his own hallway with one hand pushed into the small of his back, turned towards the camera and holding its eye. Under that force: his weight thrown onto one hip, the other heel lifted clear of the floor, his free hand hanging heavy at his side, shoulders uneven. Face: brow raised and tight, mouth pressed thin, looking directly into the lens.

He cannot straighten fully: his trunk stays folded a few degrees forward of upright and his pelvis is tipped back under him, so the line from his shoulders to his hips reads as a shallow curve rather than a column.

One specific place: the hallway of an ordinary house just inside the front door on a weekday evening, and the lived-in clutter of the routine it disrupts — car keys dropped in a bowl, a work bag slumped against the skirting, a child's football boots kicked off by the mat, coats overloading a hook.

Key light: even flat ceiling light in the hallway, bright and unflattering, minimal shadow. Fill: the room's own ambient.

Desaturated throughout, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### hero.image · option C — `01-pain-scene` `--candid`

- varies on: execution: the bleacher steps, not the car
- ratio `16:9` · type version `1.14` · `gaze: candid`
- Same type and same axis, the second cost the copy names — the Saturday games he stopped being asked to. It sets up features.items.3, which resolves this exact situation.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his mid-forties in a creased shirt, halfway up a short flight of metal bleacher steps at a school sports field on a Saturday morning, stopped mid-stride with one hand gripping the handrail and the other flat against his own lower back. Under that force: his leading leg still on the step above and taking none of his weight, his trailing shoulder dropped, his trunk twisted away from the pressing hand. Face: eyes down at the step, mouth open on a held breath, jaw set.

He has stopped where the climb changes: two steps below him the treads are clear and above him they are empty, and he is holding the rail hard enough that his forearm is tensed.

One specific place: the side of a school sports field on a Saturday morning, and the ordinary clutter of it — a folded camp chair leaning on the frame, a kit bag on the bottom tread, a paper cup left on a rail bracket, parents further along the stand.

He is unaware of the camera. Key light: flat grey morning daylight from a covered sky. Fill: light bouncing off the metal treads. A rim of light along the handrail. Deep shadow under the stand.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

## `problems.items.0.image` — problem-agitation

- asset `104-02-problem0-pain-scene.png` · problem section 1, beside the what-I-tried list
- recommended: **option A** · media **gif**
- FIT decides. The advertorial problem-agitation cell holds 01-pain-scene alone and one-type-once has spent it at the header, so this is Step 4 rung 4 — another execution of a type already on the page, which the runbook's own worked precedent resolves the same way. The section is a list of objects that failed, not a person suffering, and evidence rank 3 is exactly what the copy enumerates: the failed tool in the state that shows it failed. B is a real second reading and is on-cell for a comparison role, but it spends 04-proof-lockedframe here and forces features.items.2 off its own recommendation. C moves the pile to the garage shelf they ended up on. PRODUCT PRESENCE: none, correctly — every object in frame is an alternative. PROMPT RISK: 1371 characters.

### problems.items.0.image · option A — `01-pain-scene` `--candid`

- varies on: baseline — object-only, no person in frame
- ratio `16:9` · type version `1.14` · `gaze: candid`
- The five fixes the copy names, thrown into the back seat and out of the driver's seat where they were supposed to work. No person: the argument is against the objects.
- **note:** COMBINATION: this option is what keeps 04-proof-lockedframe available for features.items.2. Picking B here forces that slot to change.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is the pile of abandoned fixes filling the back seat of a car, photographed from the open rear door at standing height.

Exactly as they were thrown in: a hard ring-shaped donut pad on its edge against the far door, a flat foam cushion folded once and wedged behind it, a strap-on back pillow with one of its buckles undone and the strap hanging loose, a beaded wooden seat mat rolled and pushed into the footwell, and a vibrating massage cover with its cable still plugged into nothing. Every one of them has been used and none is in the driver's seat.

One specific place: a car parked on a driveway in the evening with the rear door standing open, and the lived-in clutter of the routine none of them fixed — a cold coffee in a holder up front, a receipt curled in the door pocket, a shin pad in the far footwell.

No subject, so no gaze. The frame looks across the back seat from the open door, the way the person who gave up on them is looking at it. Key light: the last cold daylight through the far window. Fill: the dim of the cabin. Rim light along the edge of the donut pad. Deep shadow into the footwell.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### problems.items.0.image · option B — `04-proof-lockedframe` `--rivals`

- varies on: type: the three-alternatives comparison
- ratio `16:9` · type version `1.13`
- The same indictment as a locked-frame comparison: three ordinary fixes on one seat across three evenings, none of them winning. The type's use_when names this beat verbatim.
- **note:** COMBINATION: picking B spends 04-proof-lockedframe here and forces features.items.2 to change. --rivals is advertorial and paid-social only, which this page satisfies.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different evenings. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt in the door pocket, real wear on the sill.

The only thing that changes is which ordinary fix is on the seat, and each is the plain unbranded version people already own. Panel one: a hard ring-shaped donut pad, rolled forward on itself against the front lip. Panel two: a flat foam cushion, slid forward with its cover rucked into a ridge. Panel three: a strap-on back pillow, sagged down the seat back with its strap gone slack. All three photographed at the same point in the routine, at the end of a nine-hour day, with the driver out of the car and nothing touched or straightened first.

Light differs only in exposure between panels, never in warmth. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours none of them.

No product, no badges, no arrows and no text of any kind.
```

### problems.items.0.image · option C — `01-pain-scene` `--candid`

- varies on: execution: the garage shelf, not the back seat
- ratio `16:9` · type version `1.14` · `gaze: candid`
- Same type and same object-only execution, a different place and different evidence: the same five fixes months later, each carrying the wear that retired it.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is the shelf of abandoned fixes in a garage, photographed square on at chest height.

Exactly as they were left: a hard donut pad standing on its edge with a crease worn across it, a flat foam cushion compressed permanently into a body-shaped dish and stacked on top of a paint tin, a strap-on back pillow hung by one buckle from a nail, a beaded wooden mat rolled and held with a rubber band, and a vibrating massage cover still in its box with the flap torn open. Nothing has been cleaned, matched or squared up.

One specific place: a shelf above a workbench in an ordinary domestic garage on a weekday evening, and the clutter of the room around it — a coiled hose on a bracket, a jar of screws with the lid off, a folded pushchair against the wall, a bag of cat litter split at the corner.

No subject, so no gaze. The frame looks straight at the shelf from chest height, the way the person who filled it is looking at it. Key light: a single bare bulb overhead, cold and hard. Fill: nothing. Rim light along the top edge of the shelf. Deep shadow behind the objects.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### problems.items.0.image · the motion brief — `cause` (whole-frame)

- form `whole-frame` · rung `re-execution` · reference folder: gifs-library/cause/ — no files filed yet; the folder card carries the law
- plate `plates/104-02-problem0-pain-scene--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
104-02-cause-problem0.mp4
3s · 16:9 · seamless loop · mp4/webm, muted, under the size ceiling

A shot of a driver sitting on a hard donut pad on the car seat, or on the bare seat itself. When the car brakes the pad rolls forward under him and his pelvis drops back into the gap behind it, and sitting like that nine hours a day is what locks the back.

IF THAT CANNOT BE SHOT
A shot of the same seat with a hand pushing an old donut pad forward from behind, no driver and no moving car. The pad rolls to the front lip and the gap opens behind it, the same gap a pelvis hinges back into on every brake.
```

## `problems.items.1.image` — cause

- asset `104-03-problem1-cause-anatomy.png` · problem section 2, beside the mechanism list
- recommended: **option A** · media **still**
- FIT and the removal test together, and this page hands the type its own vocabulary: the copy calls the fault pelvic-hinge collapse. Take the backward-sloping seat out of the left panel and the hinged pelvis goes with it, so this is a switchable mechanism rather than accumulated damage. The measurable landmark pair the type demands is in the copy — hips dropping below knees — and the difference is well past the 2:1 the `measure` mark needs. A runs --diagnostic and adds `range`, the wedge showing the hinge angle itself, which is the fault the section names. B is the base variant with the product in the right panel. C trades `range` for `pressure` on the sitting bones. PAGE LEGALITY: 02-cause-anatomy pairs_with 01-pain-scene and 03-mechanism-ghostbody, both on the page. PROMPT RISK: 2056 characters against a measured ~2050 at three marks.

### problems.items.1.image · option A — `02-cause-anatomy` `--diagnostic`

- varies on: baseline
- ratio `16:9` · type version `1.15`
- The seat is the culprit and the pelvic hinge is the structure it acts on. Two panels, one figure, the hip-to-knee line measured and the hinge angle shaded, with the product held back until the mechanism section.

```
A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, the sacrum and the lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has hinged backward into the open void where the seat base meets the backrest and the lumbar curve has flattened and reversed. Right panel: the same figure on the same seat with a continuous supportive contour filling that void, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the contour covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. A shaded wedge in each panel showing the angle open between the pelvis and the thigh, red on the left where it has collapsed and blue on the right where it is held. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

### problems.items.1.image · option B — `02-cause-anatomy`

- varies on: variant: the product enters the right panel
- ratio `16:9` · type version `1.15` · upload the product photo
- The same anatomy with the reference product drawn into the corrected panel. It resolves the argument here instead of at features.items.0, which is a real editorial choice rather than a better one.
- **note:** Picking B puts the product in frame one section earlier than the copy reveals it, and makes this slot require the product photo.

```
A 2D flat-vector medical illustration with flat fills and hard edges, no gradients. Not photography, not a 3D render.

The attached photo is the exact reference for the product.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, the sacrum and the lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded, the pelvis hinged back into the void at the seat corner. Right panel: the same figure on the same seat with the reference product in place, drawn at a size and angle where it is obviously that product, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the product covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

### problems.items.1.image · option C — `02-cause-anatomy` `--diagnostic`

- varies on: execution: subject class — the sitting bones, not the whole hinge
- ratio `16:9` · type version `1.15`
- Same type and variant, a different structure and a different third mark: the load moving off the two sitting bones onto the tailbone, drawn as a contact region.

```
A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same three-quarter rear view in both, the whole body in shot with the seat small within it. The two sitting bones, the sacrum and the soft tissue over them are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. These are the sitting bones and the sacrum, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has hinged back off the sitting bones and the load has moved onto the tailbone at the base of the sacrum. Right panel: the same figure on the same seat with a continuous supportive contour filling the void at the seat corner, the load back on the two sitting bones and the tailbone clear of the seat. Neither the seat nor the contour covers the sacrum on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at the same two landmarks — the top of the hip bone and the top of the knee — both starting from the same point in their panel, red on the left and blue on the right. A filled region bounded by the contact surface itself, as wide as the contact is, one per panel: red on the left over the tailbone where the load has gone, blue on the right across both sitting bones where it belongs. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

## `features.items.0.image` — mechanism

- asset `104-04-feature0-mechanism-ghostbody.png` · feature section 1, beside the why-every-fix-missed-it list
- recommended: **option A** · media **still**
- FIT decides against a ratio cost and FIT wins. The section's sentence is that a support system must execute three mechanical moves at once — elevate the hips, bridge the gap, hold the lumbar curve — which is a mechanism inside the body that cannot be filmed, and body_contact is true so the gate opens. RATIO COST, stated rather than hidden: this type declares 1:1 and 4:5 and not the template's 16:9, so it renders square and the layout crops it; the two panels sit side by side, so a centre-crop to 16:9 keeps both and loses head and foot room. 03-mechanism-xray is NOT offered: its avoid_when bars a trivial interior and a block of moulded foam is one. Only one option is emitted — the cell holds one legal type here, and this type has no axes to vary, so a B or a C would be a reroll rather than a named dimension, which SPEC 7.4 bars. PROMPT RISK: 2029 characters against a measured 2056-2916.

### features.items.0.image · option A — `03-mechanism-ghostbody`

- varies on: baseline
- ratio `1:1` · type version `2.2` · upload the product photo
- Two panels of the same cross-sectioned mannequin in the same sloped seat, differing only in whether the product is there. Red stress on the sacrum where the load collects, blue support beside the lumbar spine where the contour carries it.
- **note:** RATIO: renders at 1:1, the type's own declared ratio; the 16:9 template slot crops it. Both panels survive a centre-crop, head and foot room do not.

```
A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated side-on in an ordinary matte grey car seat whose base slopes backward: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical seat in both. The body is cross-sectioned along the midline so the pelvis, the sacrum and the lumbar spine are visible inside the silhouette.

The pelvis, the sacrum and the lumbar vertebrae are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: the mannequin sits with nothing filling the void where the seat base meets the backrest, the pelvis hinged backward into it, the hips dropped below the knees and the lumbar curve reversed. A flat hard-edged red overlay, unshaded, lies on the sacrum and the two lowest lumbar vertebrae where the load has collected.

Right panel is the correct state: the reference product is in place on the same seat at the same angle, its contour visibly following the line of the pelvis and the lumbar spine, the hips lifted level with the knees. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all. A flat hard-edged blue band, unshaded, is drawn beside the lumbar spine along its own length on the side away from the product, running only the length the product reaches — never a fill of the bone, never a tint of the anatomy.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product.
```

## `features.items.1.image` — proof

- asset `104-05-feature1-relief-hero.png` · feature section 2, beside the what-makes-it-work list
- recommended: **option A** · media **gif**
- FIT against an exhausted cell, and this is the library's FIRST routed inset loop. The advertorial proof cell holds 04-proof-lockedframe alone and the recommended set spends it at features.items.2, so this is Step 4 rung 2. 06-relief-hero's use_when asks for one image that proves wrong against right, shows the product and sells the relief state; --detail is the inset mode the type names for a feature too small to read at scene scale, which is exactly the textured non-slip base the copy credits. The layer's content is TEMPORAL — the base holding while the car brakes — which is the condition inset_motion --loop requires, so the loop lives in a layer the skeleton already legislates rather than in a new one. A reserves that layer as an empty block; B fills it with the still photograph instead and gives up the loop; C is the same reserved layer in a home office. EVIDENCE: 06-relief-hero is the most-rendered type in the library at 22. PROMPT RISK: 1596 characters; this type is multi-layer and runs long by design.

### features.items.1.image · option A — `06-relief-hero` `--detail`

- varies on: baseline — the inset layer reserved for the loop
- ratio `16:9` · type version `1.15` · upload the product photo · `register: commercial`, `inset_mode: detail`, `inset_motion: loop`
- The product doing its job in the car, with the corner layer left empty for the editor to drop the loop into. The hero carries the relief; the reserved block carries the claim the copy makes about braking.
- **note:** THE RESERVED BLOCK IS NOT A DESIGN ELEMENT. This option carries a `--loop` inset, so its legislated layer is drawn as a flat empty grey block for the editor to drop the loop into (G12, ADR-033). The render keeps this slot's own asset filename because it IS the frame the loop lands in, and it is NOT shippable until the loop is in it — an empty block will ship unnoticed as a design choice if nobody is told, which is what this note exists to prevent. The work order is the generated plate beside it.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar shirt, sitting relaxed in the driver's seat of a parked car with the door open, one hand loose on his thigh and his gaze out through the windscreen rather than at the product. He is settled back with his weight even through both hips and nothing braced, and he sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with things that genuinely belong there: a lanyard on the indicator stalk, a coffee cup in the holder, a phone cable coiled at the dash, a folded jacket on the back seat, a parking permit on the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border. It is filled with one flat neutral grey tone and nothing else: no photograph, no drawing, no lettering, no texture and no detail of any kind inside it. It is an empty reserved block.

No mark of any kind appears anywhere in the frame.
```

### features.items.1.image · option B — `06-relief-hero` `--detail`

- varies on: axis: inset_motion=still — the detail as a photograph
- ratio `16:9` · type version `1.15` · upload the product photo · `register: commercial`, `inset_mode: detail`, `inset_motion: still`
- The same frame with the layer filled by a still macro of the grip pattern against the leather. It ships as a page asset with no editor step, and it asserts the grip rather than demonstrating it.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar shirt, sitting relaxed in the driver's seat of a parked car with the door open, one hand loose on his thigh and his gaze out through the windscreen rather than at the product. He is settled back with his weight even through both hips, and he sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with things that genuinely belong there: a lanyard on the indicator stalk, a coffee cup in the holder, a phone cable coiled at the dash, a folded jacket on the back seat, a parking permit on the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border, showing one magnified detail the scene cannot carry at this distance: the textured underside of the product pressed against the smooth leather of the seat base, close enough that the grip pattern and the leather grain are both readable. It is a photograph in the same register as the scene and does not bleed into it, linked to the product by proximity alone with no arrow and no glow border.

No mark of any kind appears anywhere in the frame.
```

### features.items.1.image · option C — `06-relief-hero` `--detail`

- varies on: execution: the desk chair, not the car seat
- ratio `16:9` · type version `1.15` · upload the product photo · `register: commercial`, `inset_mode: detail`, `inset_motion: loop`
- Same type, same reserved layer, the other half of the copy's portability claim. The loop that fills it would have to change with the scene: a desk chair has no braking, so the alternate staging becomes the one that ships.
- **note:** THE RESERVED BLOCK IS NOT A DESIGN ELEMENT. This option carries a `--loop` inset, so its legislated layer is drawn as a flat empty grey block for the editor to drop the loop into (G12, ADR-033). The render keeps this slot's own asset filename because it IS the frame the loop lands in, and it is NOT shippable until the loop is in it — an empty block will ship unnoticed as a design choice if nobody is told, which is what this note exists to prevent. The work order is the generated plate beside it.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her early fifties in a plain jumper, sitting relaxed in a home office swivel chair with both feet flat on the floor, one hand resting loose on the desk and her gaze on the window rather than at the product. Her weight is even through both hips and she is settled back into the chair, sitting to the right of the frame so the whole chair back and the product against it stay clear to the camera.

The reference product is on the chair beneath and behind her, its seat section under her and its lumbar section standing up against the small of her back, identical to the attached photo in shape, colour and proportion.

One real home office filled to the edges with things that genuinely belong there: a full bookshelf, a mug on a coaster, a desk lamp turned away, a router with its cable looped, a cardigan over the chair arm, a plant on the sill. Background blurred, but no bare wall or floor area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border. It is filled with one flat neutral grey tone and nothing else: no photograph, no drawing, no lettering, no texture and no detail of any kind inside it. It is an empty reserved block.

No mark of any kind appears anywhere in the frame.
```

### features.items.1.image · the motion brief — `mechanism` (inset)

- form `inset` · rung `natural` · reference folder: gifs-library/mechanism/ — no files filed yet; the folder card carries the law
- the loop fills the reserved block in the still above, so its ratio `1:1` is the LAYER's shape and not the slot's `16:9`
- plate `plates/104-05-feature1-relief-hero--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
104-05-mechanism-feature1.mp4
3s · 1:1 · seamless loop · mp4/webm, muted, under the size ceiling

A close shot of the textured underside of the cushion pressed against smooth leather, filling the frame. The car brakes hard, the seat leather flexes and the whole cabin jolts, and the grip pattern does not travel a millimetre across it.

IF THAT CANNOT BE SHOT
A close shot of the same underside on the same leather with a hand shoving the cushion hard from behind, nobody in the car. It gives a finger's width and settles back, while an ordinary flat pad beside it walks forward and stays there.
```

## `features.items.2.image` — proof

- asset `104-06-feature2-proof-lockedframe.png` · feature section 3, beside the what-to-know list
- recommended: **option A** · media **still**
- FIT and the VARIANT SELECTION RULE together. The section's claim is that ten hours of sitting did not produce the usual ache and that the core held, which is a condition over time rather than a difference between products — so the gate switches the variable from which product to which state of the same object, and --timelapse is what it mandates. Only one option is emitted: the advertorial proof cell holds this type alone once 06-relief-hero is spent at features.items.1, the gate fixes the variant, and a second execution of the same seat on the same day would be a reroll rather than a named dimension. CAPABILITY: `strict` needs compositing so the panels run `handheld` (ADR-021). PROMPT RISK: 1737 characters against a 1800 ceiling.

### features.items.2.image · option A — `04-proof-lockedframe` `--timelapse`

- varies on: baseline
- ratio `16:9` · type version `1.13` · upload the product photo
- One seat, one framing, three points in a single ten-hour day, and the only variable is the hour. The contour still stands to full depth at the end of it.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product.

Shot by one person on a phone across one working day. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt in the door pocket, real wear on the sill.

The reference product is the subject of every panel and is the same physical object throughout — the same outline, the same black, the same continuous L-shaped contour, matching the attached photo exactly. It sits in the same position on the seat in every panel.

The only thing that changes is the point in the day: panel one at six in the morning before the first drive, panel two at midday after five hours of sitting, panel three at the end of a ten-hour shift. Every panel is photographed at the same point in the routine, with the driver already out of the car and nothing plumped, straightened or pushed back into place first. Across all three the contour still stands to its full depth at the seat corner and the seat section has not compressed into a dish.

Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind.
```

## `features.items.3.image` — outcome

- asset `104-07-feature3-relief-scene.png` · feature section 4, beside the what-changed list
- recommended: **option A** · media **still**
- FIT decides and the requires_pair is already paid for. 06-relief-scene closes an advertorial when the promise is a state of living rather than a feature, and this section is the Blue Ridge trip and the two back-to-back games in metal bleachers. Its requires_pair is 01-pain-scene, which is at the header on the same man. The relief situation is chosen from what the problem forbade: the bleachers are the exact thing his daughter stopped asking him to, so A stages the inverse of hero option C. Only one option is emitted: the outcome cell holds 06-relief-scene and 06-relief-hero, and 06-relief-hero is spent at features.items.1, which leaves this type with no legal second type and no axis but `gaze`, whose other value the type bans outright. PRODUCT PRESENCE: standalone class — it sits on the bench slat he has just left, near the camera and turned so it can be read. PROMPT RISK: 1517 characters.

### features.items.3.image · option A — `06-relief-scene`

- varies on: baseline
- ratio `16:9` · type version `3.7` · upload the product photo · `gaze: candid`
- The release and the return in one frame: standing up off the bleacher bench at the end of the match, weight even, hands empty, the smile arriving on its own while he watches the pitch.

```
A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his mid-forties in put-together but ordinary clothes, standing up off a metal bleacher bench at a school sports field at the end of a match, coming to his full height in one movement with his weight even through both feet and both hands empty and open. Nothing is held, nothing is braced against the rail or the bench, nothing is covered. His chest is opening, his shoulders roll back and down, his eyes are up and following something out on the pitch, and a small involuntary smile has arrived on its own while he looks away from the camera.

The reference product sits on the bench slat he has just left, near the camera in the lower third of the frame, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary school sports field on a grey Saturday, two or three blurred parents further along the stand, a folded camp chair, a kit bag under the bench, painted line markings worn thin on the grass.

Even natural daylight, bright, soft shadows, plain and unglamorous. A natural palette, light film grain, shallow depth of field, honest rather than drained and never warm-boosted.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text.
```

### features.items.3.image · the motion brief — `relief` (whole-frame)

- form `whole-frame` · rung `natural` · reference folder: gifs-library/relief/ — no files filed yet; the folder card carries the law
- plate `plates/104-07-feature3-relief-scene--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
104-07-relief-feature3.mp4
4s · 16:9 · seamless loop · mp4/webm, muted, under the size ceiling

A shot of a man standing up off a metal bleacher bench at the end of a match. He comes to his full height in one movement without pushing off the rail or the bench, turns, and walks down the steps without once reaching back for his lower back.

IF THAT CANNOT BE SHOT
A shot of the same man getting out of his car at the end of a long drive. He swings his legs out, stands straight up in one go without grabbing the door frame, and walks off with the cushion still on the seat behind him.
```

## `reviews.shots.0.image` — social-proof

- asset `104-08-review-1.png` · review grid tile 1 of 4
- recommended: **option A** · media **still**
- One option by law (ADR-022): the four tiles are the unit of variation, not the tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home. The SET DIVERSITY LAW is satisfied across the four: four room classes, four surfaces, four light temperatures, four camera distances and three content modes.

### reviews.shots.0.image · option A — `05-social-snapshot`

- varies on: in-use · saloon car · driver's seat · cool early daylight · seated arm's length
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the four-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the same reviews block as three attributed quotes carrying reviewer names. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names — before rendering any of these. Fifth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use in a car, photographed by its owner from the open driver's door: the reference cushion in place on the driver's seat with the owner's forearm resting across the top of the lumbar section, no face in shot.

An ordinary saloon car photographed exactly as found on a weekday morning — the mess stays, nothing tidied, nothing added for the picture. Cool early daylight through the windscreen and the open door, no other light.

One incidental owner object and no more: a lanyard hung on the indicator stalk.

Framing slightly tilted and a little too close, taken at arm's length from the seat; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `reviews.shots.1.image` — social-proof

- asset `104-09-review-2.png` · review grid tile 2 of 4
- recommended: **option A** · media **still**
- One option by law (ADR-022): the four tiles are the unit of variation, not the tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home. The SET DIVERSITY LAW is satisfied across the four: four room classes, four surfaces, four light temperatures, four camera distances and three content modes.

### reviews.shots.1.image · option A — `05-social-snapshot`

- varies on: at-rest · home office · swivel chair · warm desk lamp · standing above
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the four-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the same reviews block as three attributed quotes carrying reviewer names. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names — before rendering any of these. Fifth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product simply sitting where it now lives: the reference cushion in place on a home office swivel chair, nobody in the picture at all.

An ordinary spare-room office photographed exactly as found in the evening — the mess stays, nothing tidied, nothing added for the picture. Warm yellow light from a single desk lamp and the room's overhead, no other light.

One incidental owner object and no more: a charger cable coiled on the desk behind the chair.

Framing off-centre and taken from standing height looking down at the chair; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `reviews.shots.2.image` — social-proof

- asset `104-10-review-3.png` · review grid tile 3 of 4
- recommended: **option A** · media **still**
- One option by law (ADR-022): the four tiles are the unit of variation, not the tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home. The SET DIVERSITY LAW is satisfied across the four: four room classes, four surfaces, four light temperatures, four camera distances and three content modes.

### reviews.shots.2.image · option A — `05-social-snapshot`

- varies on: in-use · truck cab · bench seat · flat overcast daylight · close over the shoulder
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the four-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the same reviews block as three attributed quotes carrying reviewer names. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names — before rendering any of these. Fifth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use in a truck cab, photographed by its owner over their own shoulder: the reference cushion in place on the bench seat with two fingers tucked against the edge of the lumbar section, no face in shot.

An ordinary working truck cab photographed exactly as found on a flat grey afternoon — the mess stays, nothing tidied, nothing added for the picture. Flat overcast daylight through the side window, no other light.

One incidental owner object and no more: a clipboard wedged against the far side of the seat.

Framing close and crooked, taken from very near the seat over the shoulder; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `reviews.shots.3.image` — social-proof

- asset `104-11-review-4.png` · review grid tile 4 of 4
- recommended: **option A** · media **still**
- One option by law (ADR-022): the four tiles are the unit of variation, not the tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home. The SET DIVERSITY LAW is satisfied across the four: four room classes, four surfaces, four light temperatures, four camera distances and three content modes.

### reviews.shots.3.image · option A — `05-social-snapshot`

- varies on: kit-flatlay · kitchen · wooden table · mixed warm and cool · half a metre back
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the four-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the same reviews block as three attributed quotes carrying reviewer names. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names — before rendering any of these. Fifth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The opened box and its contents as the owner has just left them: the reference cushion out of its packaging on a kitchen table, still recovering its shape, with the flattened box and the plastic sleeve pushed to one side. Nobody in the picture at all.

An ordinary kitchen photographed exactly as found in the middle of the day — the mess stays, nothing tidied, nothing added for the picture. Mixed light, warm ceiling spots over cool daylight from the window, no other light.

One incidental owner object and no more: a fruit bowl at the edge of the table.

Framing slightly tilted and taken from standing height about half a metre back; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

# Image prompts — page 77, ergonomic memory foam seat cushion

GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit the script and re-run. Routing rationale, the negative motion verdicts and the out-of-scope slots are all in `prompts.json`.

- page `77` · advertorial · solution-aware · registry `2.0.0` · 11 routed slots · 25 prompts · 2 motion briefs
- motion: 2 of 11 slots earn a loop (floor 2, ceiling 5), groups result, working
- **4 prompts carry a blocking precondition**, stated on each — do not render those until it is resolved

---

## `hero.image` — hero

- asset `77-01-hero-pain-scene.png` · advertorial header, under the eyebrow and above the byline
- recommended: **option A** · media **still**
- FIT decides, and it is close to verbatim. 01-pain-scene --candid asks for physical pain in a moment nobody would choose to be seen in, and hero.body.0 is that moment in the page's own words — gripping the steering wheel just to brace himself before standing up. A plays it as the single seated action the whole page is written against. B moves to the confront gaze, which the type reserves for appearance and self-image rather than physical pain, and loses the brace. C keeps the action but moves it to a delivery driver, a real reader of this page but the second one. PAGE LEGALITY: A satisfies 06-relief-scene's requires_pair at features.items.3 and pairs_with 04-proof-lockedframe at features.items.2. EVIDENCE: candid is this type's most-rendered branch. PRODUCT PRESENCE: none, correctly — the type bans it. PROMPT RISK: 1535 characters against a measured band of 1379-2153.

### hero.image · option A — `01-pain-scene` `--candid`

- varies on: baseline
- ratio `16:9` · type version `1.14` · `gaze: candid`
- The page's opening scene played straight: the driver hauling himself off the seat back on his own driveway. Evidence is the symptom as physical fact — hips below knees in the sloped seat, the lumbar curve flattened with the gap open behind it.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his late forties in a creased work polo, still belted into the driver's seat of his own car on the driveway at the end of the day, mid-way through hauling himself forward off the seat back with both hands locked round the top of the steering wheel. Under that force: both arms straight and carrying his weight, shoulders drawn up towards his ears, hips still down in the seat, his whole back held rigid in one piece instead of bending. Face: brow drawn in, jaw set, breath held, eyes down at the footwell.

His hips sit well below his knees in the backward-sloping seat, his lower back is pressed flat against the seat back with an open gap behind it, and his weight has gone onto the base of his spine.

One specific place: a suburban driveway at the end of the working day, the driver's door swung open behind him, and the lived-in clutter of the commute — a travel mug gone cold in the holder, a lanyard and keys spilled across the passenger seat, a folded hi-vis jacket on the back seat, a parking receipt in the door pocket.

He is unaware of the camera, his gaze down and inward. Key light: cold blue dusk through the windscreen, weak and directionless. Fill: the dim dome light above him. A rim of light separates his shoulder from the dark interior. Deep shadow across the lower third of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### hero.image · option B — `01-pain-scene` `--confront`

- varies on: axis: gaze=confront
- ratio `16:9` · type version `1.14` · `gaze: confront`
- The same argument in the type's other gaze. The advertorial hero cell holds one type and the attribute gates leave no second, so the honest variation is the axis rather than a type borrowed from a role it does not belong to.
- **note:** The type reserves --confront for appearance and daily frustration rather than physical pain; it is offered because the axis is the only legal second dimension here, not because it fits better.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his late forties in a creased work polo, seated at a dispatch desk in the middle of the afternoon, turned away from his monitor towards the camera with his right hand pushed into the small of his own back and his left braced flat on the desk edge. Under that force: his trunk twisted and held part-way round, weight shifted onto one hip, the other heel lifted off the floor. Face: brow raised and tight, mouth pressed thin, looking directly into the lens and holding it.

He has slid forward to the front edge of the chair so his lower back has left the backrest entirely, and there is an open gap between the base of his spine and the seat back behind him.

One specific place: a shipping depot dispatch office in the middle of a shift, and the lived-in clutter of the routine it disrupts — a printed run sheet weighted down with a stapler, a cold mug ringed with old coffee, a hard hat on the filing cabinet, a desk fan turned to the wall.

Key light: even overhead office daylight, bright and flat, minimal shadow, unflattering. Fill: the room's own ambient.

Desaturated throughout, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### hero.image · option C — `01-pain-scene` `--candid`

- varies on: execution: subject class — the delivery driver, not the commuter
- ratio `16:9` · type version `1.14` · `gaze: candid`
- Same type and same axis, different subject class: the professional driver from the brief's persona list, in a van cab on a lay-by. The action is the same push up out of a sloped seat.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A woman in her early fifties in a fleece and work trousers, in the cab of a delivery van pulled onto a lay-by, mid-way through pushing herself up off the seat with one hand flat on the wheel and the other pressing down on the seat base beside her thigh. Under that force: both elbows locked, one shoulder dropped lower than the other, hips lifting in one slow piece with her back kept straight and unmoving. Face: eyes narrowed, lips parted on a held breath, gaze fixed on the windscreen.

Her hips sit below her knees in the sloped bench seat, her lower back is flattened against a seat back that curves away from it, and an open gap runs the width of her lower spine.

One specific place: a roadside lay-by in the middle of a delivery round, the door half open, and the lived-in clutter of the shift — a clipboard of delivery notes on the passenger seat, a flask wedged in the door pocket, a crumpled sandwich wrapper in the cup holder, a hi-vis tabard over the seat back.

She is unaware of the camera, her gaze forward and inward. Key light: flat grey daylight through the windscreen, cold and weak. Fill: the dim of the cab. A rim of light along her forearm. Deep shadow across the near side of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

## `problems.items.0.image` — problem-agitation

- asset `77-02-problem0-pain-scene.png` · problem section 1, beside the what-I-already-tried list
- recommended: **option A** · media **gif**
- FIT decides. The advertorial problem-agitation cell holds 01-pain-scene alone, and one-type-once has already spent it at the header — so this is Step 4 rung 4, another execution of a type already on the page, which the runbook's own worked precedent resolves the same way (object-only, two ledger observations). The section is a list of objects that failed, not a person suffering, and evidence rank 3 — the failed tool in the state that shows it failed — is exactly what the copy enumerates. B is a real second reading and is on-cell for a comparison role, but taking it spends 04-proof-lockedframe here and forces features.items.2 off its own recommendation. C is the same object-only execution moved to the drawer they ended up in. PAGE LEGALITY: A keeps 04-proof-lockedframe free for features.items.2. PRODUCT PRESENCE: none, correctly — every object in frame is an alternative, not the product. PROMPT RISK: 1590 characters, inside the measured band.

### problems.items.0.image · option A — `01-pain-scene` `--candid`

- varies on: baseline — object-only, no person in frame
- ratio `16:9` · type version `1.14` · `gaze: candid`
- The four fixes the copy names, left exactly where they ended up on the seat, with the gap they were meant to fill still open behind them. No person: the argument is against the objects.
- **note:** COMBINATION: this option is what keeps 04-proof-lockedframe available for features.items.2. Picking B here forces that slot to its own option B or C.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is what is left on a car's driver seat after every ordinary fix has been tried and abandoned, photographed from the open driver's door at standing height.

Exactly as they were left: a thin flat foam pad slid right forward to the front lip of the seat base, its cover rucked into a ridge; a doughnut ring tipped on edge down in the footwell; a cylindrical lumbar roll dropped into the crack between the seat base and the backrest with only its end still showing; a beaded seat cover shoved into a heap against the far bolster. Behind all of them the gap where the base meets the backrest is wide open, and every one of them has slid away from the place it was meant to fill.

One specific place: a car parked on a driveway in the middle of a weekday, the driver's door standing open, and the lived-in clutter of the routine none of them fixed — a travel mug in the holder, a crumpled parking receipt in the door pocket, a phone cable trailing loose from the dashboard, a folded hi-vis jacket on the back seat.

No subject, so no gaze. The frame looks across the seat from the open door, the way the person who gave up on them is looking at it. Key light: flat overcast daylight through the open door, cold and even. Fill: the dim of the cabin. Rim light along the front lip of the seat base. Deep shadow down the far side of the seat.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### problems.items.0.image · option B — `04-proof-lockedframe` `--rivals`

- varies on: type: the three-alternatives comparison
- ratio `16:9` · type version `1.13`
- The same indictment as a locked-frame comparison instead of a scene: three common fixes on one chair across three days, none of them winning. The type's use_when names this beat verbatim — the I-tried-three-things beat of an advertorial.
- **note:** COMBINATION: picking B here spends 04-proof-lockedframe on this slot and forces features.items.2 to its option B or C. --rivals is advertorial and paid-social only, which this page satisfies.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different days. One framing for every panel: the same office swivel chair photographed square-on from about a metre and a half back at seated eye height, the seat base across the lower third and a plain office partition filling the upper third. It reads as one shot taken three times, never as three different shots.

The same chair, the same partition and the same floor in all three panels, with deliberate real-world clutter: a coiled network cable along the skirting, a recycling bin half out of shot, scuff marks on the chair's base.

The only thing that changes is which ordinary seat fix is on the chair, and each is the plain unbranded version people already own. Panel one: a flat foam pad, slid forward off the back of the seat base. Panel two: a doughnut ring cushion, rolled forward on itself. Panel three: a separate cylindrical lumbar roll strapped to the backrest, sagged down out of the small of the back. All three photographed at the same point in the process, at the end of a working day, none of them touched or straightened first.

Light differs only in exposure between panels, never in warmth. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours none of them.

No product, no badges, no arrows, no text of any kind.
```

### problems.items.0.image · option C — `01-pain-scene` `--candid`

- varies on: execution: the drawer they ended up in, not the seat
- ratio `16:9` · type version `1.14` · `gaze: candid`
- Same type and same object-only execution, different place and different evidence: the same four fixes months later in a desk drawer, each carrying the damage that retired it.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is the drawer of abandoned seat fixes in a home office, pulled fully open and photographed from above at standing height.

Exactly as they were left: a flat foam pad compressed permanently into a body-shaped dish, folded once to fit; a doughnut ring with its cover pilled and its edge collapsed; a lumbar roll with one of its snapped elastic straps still threaded through the buckle; a beaded seat cover rolled and jammed down the side, several beads split from their cords. Nothing has been cleaned, matched or squared up.

One specific place: the bottom drawer of a desk unit in a spare-room office on a weekday morning, and the lived-in clutter of the room around it — a stack of unopened post on the desk above, a charger cable tangled at the back of the drawer, a dried-out marker pen, a laminated depot pass.

No subject, so no gaze. The frame looks straight down into the open drawer from standing height, the way the person who filled it is looking at it. Key light: cool window daylight from one side, flat and weak. Fill: the dim of the room. Rim light along the near edge of the drawer front. Deep shadow at the back of the drawer.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### problems.items.0.image · the motion brief — `cause`

- form `whole-frame` · rung `re-execution` · reference folder: gifs-library/cause/ — no files filed yet; the folder card carries the law
- plate `plates/77-02-problem0-pain-scene--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
77-02-cause-problem0.mp4
3s · 16:9 · seamless loop · mp4/webm, muted, under the size ceiling

A shot of a driver sitting on an old flat cushion on the car seat, or on the bare seat itself. When the car brakes the cushion slides forward under him and a gap opens behind his lower back, and sitting in that gap day after day is what starts the ache.
```

## `problems.items.1.image` — cause

- asset `77-03-problem1-cause-anatomy.png` · problem section 2, beside the root-cause list
- recommended: **option A** · media **still**
- FIT and the removal test together. Take the backward-sloping seat out of the left panel and the rolled pelvis goes with it, so this is a switchable mechanism and not accumulated damage. The copy supplies the measurable landmark pair the type demands — hips dropping below knees — and the difference is well past the 2:1 the `measure` mark requires. A runs --diagnostic, which is what the advertorial middle asks for: indict the culprit here and let features.items.0 be where the product first appears. B is the base variant with the product in the right panel, which argues buy-this one section early. C moves the subject class from the whole seated figure to the sitting bones and trades `measure` for `pressure`, a mark working at 3 of 6. PAGE LEGALITY: 02-cause-anatomy pairs_with 01-pain-scene and 03-mechanism-ghostbody, both on the page. PRODUCT PRESENCE: none under --diagnostic, and the variant makes requires_product_photo false. PROMPT RISK: 1913 characters against a measured ~1800 at two marks.

### problems.items.1.image · option A — `02-cause-anatomy` `--diagnostic`

- varies on: baseline
- ratio `16:9` · type version `1.15`
- The seat is the culprit and the pelvis is the structure it acts on. Two panels, one figure, the hip-to-knee line as the measured difference, and the product held back until the mechanism section.

```
A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, sacrum and lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has rolled backward into the open gap where the seat base meets the backrest, the sacrum has taken the load, and the lumbar curve has flattened and reversed. Right panel: the same figure on the same seat with a continuous supportive contour filling that gap, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the contour covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

### problems.items.1.image · option B — `02-cause-anatomy`

- varies on: variant: the product enters the right panel
- ratio `16:9` · type version `1.15` · upload the product photo
- The same anatomy with the reference product drawn into the corrected panel. It resolves the argument here instead of at features.items.0, which is a real editorial choice rather than a better or worse one.
- **note:** Picking B puts the product in frame one section earlier than the page's own copy reveals it, and makes this slot require the product photo.

```
A 2D flat-vector medical illustration with flat fills and hard edges, no gradients. Not photography, not a 3D render.

The attached photo is the exact reference for the product.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, sacrum and lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded, the pelvis rolled back into the open gap at the seat corner and the sacrum carrying the load. Right panel: the same figure on the same seat with the reference product in place, drawn at a size and angle where it is obviously that product, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the product covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

### problems.items.1.image · option C — `02-cause-anatomy` `--diagnostic`

- varies on: execution: subject class — the sitting bones, not the whole figure
- ratio `16:9` · type version `1.15`
- Same type and same variant, different subject class and a different mark: the load moving off the two sitting bones onto the tailbone, drawn as a contact region rather than a measured line.

```
A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same three-quarter rear view in both, the whole body in shot with the seat small within it. The two sitting bones, the sacrum and the soft tissue over them are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. These are the sitting bones and sacrum, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has tipped back off the sitting bones so the load has moved onto the tailbone at the base of the sacrum. Right panel: the same figure on the same seat with a continuous supportive contour filling the gap at the seat corner, the load back on the two sitting bones and the tailbone clear of the seat. Neither the seat nor the contour covers the sacrum on either panel.

Marks: a filled region bounded by the contact surface itself, as wide as the contact is, one per panel — red on the left over the tailbone where the load has gone, blue on the right across both sitting bones where it belongs. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

## `features.items.0.image` — mechanism

- asset `77-04-feature0-mechanism-ghostbody.png` · feature section 1, beside the what-makes-it-work list
- recommended: **option A** · media **still**
- FIT decides against a ratio cost, and FIT wins. The section's whole sentence is that the one-piece contour bridges the void where the backrest meets the seat pan and stops the pelvis collapsing backward — a mechanism inside the body that cannot be filmed, which is 03-mechanism-ghostbody's use_when almost word for word, and body_contact is true so the gate opens. RATIO COST, stated rather than hidden: this type declares 1:1 and 4:5 and not the template's 16:9, so option A renders square and the layout crops it; the two panels sit side by side, so a centre-crop to 16:9 keeps both and loses head and foot room. B is native 16:9 and costs the argument instead — it shows that the product works, not why. 03-mechanism-xray is NOT offered: its avoid_when bars a trivial interior, and a block of foam is one. PAGE LEGALITY: A is the page's only step-3 type, well inside the budget of two. PRODUCT PRESENCE: right panel only, with a real material finish and no signal colour on it. PROMPT RISK: 1951 characters against a measured 2056-2916.

### features.items.0.image · option A — `03-mechanism-ghostbody`

- varies on: baseline
- ratio `1:1` · type version `2.2` · upload the product photo
- Two panels of the same cross-sectioned mannequin in the same sloped seat, differing only in whether the product is there. Red stress on the sacrum where the load collects, blue support beside the lumbar spine where the contour carries it.
- **note:** RATIO: renders at 1:1, the type's own declared ratio; the 16:9 template slot crops it. Both panels survive a centre-crop, head and foot room do not.

```
A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated side-on in an ordinary matte grey car seat whose base slopes backward: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical seat in both. The body is cross-sectioned along the midline so the pelvis, sacrum and lumbar spine are visible inside the silhouette.

The pelvis, sacrum and lumbar vertebrae are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: the mannequin sits in the seat with nothing filling the gap where the base meets the backrest, the pelvis rolled backward into that gap and the lumbar curve flattened. A flat hard-edged red overlay, unshaded, lies on the sacrum and the lowest two lumbar vertebrae where the load has collected.

Right panel is the correct state: the reference product is in place on the same seat, at the same angle, its contour visibly following the line of the pelvis and lumbar spine. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all. A flat hard-edged blue band, unshaded, is drawn beside the lumbar spine along its own length on the side away from the product, running only the length the product reaches — never a fill of the bone, never a tint of the anatomy.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product.
```

### features.items.0.image · option B — `06-relief-hero` `--vsinset`

- varies on: type: the same claim as a scene with a wrong-vs-right inset
- ratio `16:9` · type version `1.15` · upload the product photo · `register: commercial`, `inset_mode: vsinset`
- Step 4 rung 2, an adjacent step: the mechanism argued photographically instead of anatomically, with the failed two-piece setup and the one-piece product held against each other in a split inset. Native 16:9, so nothing is cropped.
- **note:** COMBINATION: 06-relief-hero is the recommendation at features.items.1. Picking B here forces that slot to its own option B or C.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his late forties in an ordinary open-collar shirt, seated at a home office desk with his weight settled evenly and his gaze on the paperwork in front of him rather than on the product, sitting well back so the whole back of the chair and the product on it are clear to the camera. He sits to the right of the frame.

The reference product is on the chair behind him, its seat section under him and its lumbar section up against his lower back, identical to the attached photo in shape, colour and proportion.

One real room filled to the edges with objects that genuinely belong there: a full bookshelf, a wall calendar turned to the wall, a mug on a coaster, a router with its cable looped, a coat over the door, a houseplant on the sill. Background blurred, but no bare wall or floor area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

In the upper left of the frame, occupying the space he is offset from, sits a small rectangular panel with a thin white border, split into two equal halves that share one photographic register. The left half shows the same chair with an ordinary flat foam pad and a separate lumbar roll on it, the pad slid forward and the roll dropped into the gap, with glowing red points on the exposed seat corner and on the fallen roll. The right half shows the same chair with the reference product in place, brighter and cleaner, with a translucent blue overlay following the single continuous seam that runs from the seat section up into the lumbar section. A circular red badge carrying the white letters VS sits at the seam between the two halves.

No mark of any kind appears anywhere outside that panel.
```

### features.items.0.image · option C — `03-mechanism-ghostbody`

- varies on: execution: subject class — the lumbar discs, not the pelvis
- ratio `1:1` · type version `2.2` · upload the product photo
- Same type and same marks, a different structure under argument: the lowest discs pinched closed by the reversed curve, then held open. Answers the copy's spinal-fit line rather than its bridging line.
- **note:** RATIO: renders at 1:1 for the same reason as option A.

```
A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated side-on in an ordinary matte grey office chair: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical chair in both. The body is cross-sectioned along the midline so the lumbar vertebrae and the discs between them are visible inside the silhouette.

The lumbar vertebrae and their intervertebral discs are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: the mannequin sits with nothing filling the gap at the seat corner, the lumbar curve reversed into a backward bow and the front edges of the lower discs pinched closed. A flat hard-edged red overlay, unshaded, lies on the two lowest discs where they are compressed.

Right panel is the correct state: the reference product is in place on the same chair, at the same angle, its lumbar contour visibly following the restored curve of the spine. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all. A flat hard-edged blue band, unshaded, is drawn beside the lumbar vertebrae along their own length on the side away from the product, running only the length the product reaches — never a fill of the bone, never a tint of the anatomy.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product.
```

## `features.items.1.image` — proof

- asset `77-05-feature1-relief-hero.png` · feature section 2, beside the why-it-stays-put list
- recommended: **option A** · media **still**
- FIT against an exhausted cell. The advertorial proof cell holds 04-proof-lockedframe alone and the recommended set spends it at features.items.2, so this is Step 4 rung 2, an adjacent step. 06-relief-hero's use_when asks for one image that proves wrong against right, shows the product and sells the relief state, and --vsinset is the inset mode the type names for a wrong-vs-right argument — which is what this section is: the old pad slid forward and the roll fell down the crack, this one did neither. B is on-cell and is the stronger evidentiary form, but it spends the type this page needs at features.items.2 for a comparison the copy makes more sharply. C is the same argument moved to a desk chair. EVIDENCE: 06-relief-hero is the most-rendered type in the library at 22; `vs` renders 2 of 2 once the letters are named, `hotspot` is thin at 1 of 2 and is anchored to three named places rather than given a count. PRODUCT PRESENCE: in the hero and in the right half of the inset, one mode of use throughout. PROMPT RISK: 2097 characters; this type is multi-layer and runs long by design.

### features.items.1.image · option A — `06-relief-hero` `--vsinset`

- varies on: baseline
- ratio `16:9` · type version `1.15` · upload the product photo · `register: commercial`, `inset_mode: vsinset`, `inset_motion: still`
- The product doing its job in the car, with the wrong state confined to a split inset: the pad crept to the front lip and the roll gone down the crack on the left, the product unmoved on the right.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his late forties in a work polo, sitting relaxed in the driver's seat of a parked car with the door open, one hand loose on his thigh and his gaze out through the windscreen rather than at the product. He is settled back against the seat with his weight even through both hips, and he sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with things that genuinely belong there: a travel mug in the holder, a lanyard hung from the indicator stalk, a phone cable coiled at the dash, a folded jacket on the back seat, a parking permit clipped to the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, occupying the space he is offset from, sits a small rectangular panel with a thin white border, split into two equal halves that share one photographic register. The left half shows the same empty driver's seat with an ordinary flat foam pad slid forward to the front lip and a separate lumbar roll fallen into the crack behind it, with glowing red points on the open seat corner, on the front lip where the pad has crept to, and on the end of the fallen roll. The right half shows the same empty seat with the reference product in place and unmoved, brighter and cleaner, with a translucent blue overlay following the single continuous seam that runs from the seat section up into the lumbar section. A circular red badge carrying the white letters VS sits at the seam between the two halves.

No mark of any kind appears anywhere outside that panel.
```

### features.items.1.image · option B — `04-proof-lockedframe` `--timelapse`

- varies on: type: the same object across one working week
- ratio `16:9` · type version `1.13` · upload the product photo
- The on-cell proof type in the variant the gate mandates: sliding cannot be shown inside a static frame, so the variable becomes the condition of one object over time rather than which product is on the seat.
- **note:** COMBINATION: picking B spends 04-proof-lockedframe here and forces features.items.2 to its option B or C.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product.

Shot by one person on a phone across one working week. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a travel mug in the holder, a parking receipt in the door pocket, real wear on the sill.

The reference product is the subject of every panel and is the same physical object throughout — the same outline, the same black, the same continuous L-shaped contour, matching the attached photo exactly. It sits in the same starting position in the seat in every panel.

The only thing that changes is the point in the week: panel one on Monday morning before the first drive, panel two on Wednesday evening after two days of commuting, panel three on Friday evening after the full week. Every panel is photographed at the same point in the routine, with the driver already out of the car and nothing touched, straightened or pushed back into place first. Across all three the product has not crept forward off the seat base and has not dropped into the crack at the seat corner.

Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No badges, no arrows, no text of any kind.
```

### features.items.1.image · option C — `06-relief-hero` `--vsinset`

- varies on: execution: the desk chair, not the car seat
- ratio `16:9` · type version `1.15` · upload the product photo · `register: commercial`, `inset_mode: vsinset`, `inset_motion: still`
- Same type, same inset mode, the other half of the copy's claim — the cushion that moves between the car and the office chair, shown in the office.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her early fifties in a plain jumper, sitting relaxed in a home office swivel chair with both feet flat on the floor, one hand resting loose on the desk and her gaze on the window rather than at the product. Her weight is even through both hips and she is settled back into the chair, sitting to the right of the frame so the whole chair back and the product against it stay clear to the camera.

The reference product is on the chair beneath and behind her, its seat section under her and its lumbar section standing up against the small of her back, identical to the attached photo in shape, colour and proportion.

One real home office filled to the edges with things that genuinely belong there: a full bookshelf, a mug on a coaster, a desk lamp turned away, a router with its cable looped, a cardigan over the chair arm, a houseplant on the sill. Background blurred, but no bare wall or floor area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

In the upper left of the frame, occupying the space she is offset from, sits a small rectangular panel with a thin white border, split into two equal halves that share one photographic register. The left half shows the same empty swivel chair with an ordinary flat foam pad slid forward to the front lip and a separate lumbar roll strapped to the backrest and sagged down below the small of the back, with glowing red points on the open seat corner, on the front lip where the pad has crept to, and on the slack strap. The right half shows the same empty chair with the reference product in place and unmoved, brighter and cleaner, with a translucent blue overlay following the single continuous seam that runs from the seat section up into the lumbar section. A circular red badge carrying the white letters VS sits at the seam between the two halves.

No mark of any kind appears anywhere outside that panel.
```

## `features.items.2.image` — comparison

- asset `77-06-feature2-proof-lockedframe.png` · feature section 3, beside the why-it-lasts list
- recommended: **option A** · media **gif**
- FIT decides on the type's own core condition. 04-proof-lockedframe may only be used where the difference is visible to the naked eye inside a static frame, and the copy's claim is exactly that — cheap foam flattens out like paper after twenty minutes, this core holds its shape. A flattened pad against a standing contour is visible without anything being explained. A takes --verdict, whose order rule puts the product last where left-to-right reading resolves. B drops the product for --rivals, which indicts the alternatives but makes no claim for the cushion and duplicates the work problems.items.0 already does. C is the same comparison on an office chair. CAPABILITY: `strict` needs compositing, so the panels run `handheld` with --verdict included, exactly as the type's own capability gate says (ADR-021). PAGE LEGALITY: 04-proof-lockedframe pairs_with 02-cause-anatomy, 06-relief-hero and 01-pain-scene, all three on the page. PROMPT RISK: 1725 characters against a 1800 ceiling.

### features.items.2.image · option A — `04-proof-lockedframe` `--verdict`

- varies on: baseline
- ratio `16:9` · type version `1.13` · upload the product photo
- One seat, one framing, three days, and the only variable is which cushion took the day's sitting. The two alternatives are the most common ones buyers already own and get exactly the same photographic respect as the product.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different days. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a travel mug in the holder, a parking receipt in the door pocket, real wear on the sill.

The only thing that changes is which cushion is on the seat, and each is photographed at the same point in the routine — at the end of a full day's driving, with the driver already out of the car and nothing plumped, straightened or pushed back into place first. Panel one: a plain unbranded flat foam pad, the two most common inches of foam anyone owns, compressed under its own use into a shallow dish that has not sprung back. Panel two: a plain unbranded doughnut ring cushion, its ring flattened along the front where the weight sat. Panel three: the reference product, its continuous L-shaped contour still standing to its full depth at the seat corner.

All three are ordinary, clean and in good condition, and all three get exactly the same exposure, the same background tidiness and the same framing generosity. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No badges, no arrows, no text of any kind.
```

### features.items.2.image · option B — `04-proof-lockedframe` `--rivals`

- varies on: variant: the product leaves the frame
- ratio `16:9` · type version `1.13`
- The same locked frame with three alternatives and no product, making no claim at all. Honest and it fits the section's first sentence, but it argues what fails rather than what lasts.
- **note:** COMBINATION: --rivals is also option B at problems.items.0. Running both would put two rival comparisons on one page arguing the same thing.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different days. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a travel mug in the holder, a parking receipt in the door pocket, real wear on the sill.

The only thing that changes is which of three common existing alternatives is on the seat, all plain and unbranded and all the kind of thing the viewer already owns. Panel one: a flat foam pad, compressed under its own use into a shallow dish. Panel two: a doughnut ring cushion, its ring flattened along the front. Panel three: a gel seat pad, sagged into a low ridge along its centre. Every panel is photographed at the same point in the routine, at the end of a full day's driving, with the driver already out of the car and nothing plumped or straightened first.

None of them is damaged or dirty, none is exaggerated, and none of them wins. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours none of them.

No product, no badges, no arrows, no text of any kind.
```

### features.items.2.image · option C — `04-proof-lockedframe` `--verdict`

- varies on: execution: the office chair, not the car seat
- ratio `16:9` · type version `1.13` · upload the product photo
- Same type and variant, different scene and a different pair of alternatives: the desk-chair half of the copy's universal-fit claim, with a memory foam wedge in place of the doughnut ring.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different days. One framing for every panel: the same office swivel chair photographed square-on from about a metre and a half back at seated eye height, the seat base across the lower third and a plain office partition filling the upper third. It reads as one shot taken three times, never as three different shots.

The same chair, the same partition and the same floor in all three panels, with deliberate real-world clutter: a coiled network cable along the skirting, a recycling bin half out of shot, scuff marks on the chair base.

The only thing that changes is which cushion is on the chair, and each is photographed at the same point in the routine — at the end of a full working day, with nobody in the room and nothing plumped, straightened or squared up first. Panel one: a plain unbranded flat foam pad, compressed under its own use into a shallow dish that has not sprung back. Panel two: a plain unbranded memory foam wedge, its thin end folded over where the weight sat. Panel three: the reference product, its continuous L-shaped contour still standing to its full depth at the seat corner.

All three are ordinary, clean and in good condition, and all three get exactly the same exposure, the same background tidiness and the same framing generosity. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No badges, no arrows, no text of any kind.
```

### features.items.2.image · the motion brief — `proof`

- form `whole-frame` · rung `re-execution` · reference folder: gifs-library/proof/ — no files filed yet; the folder card carries the law
- plate `plates/77-06-feature2-proof-lockedframe--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
77-06-proof-feature2.mp4
3s · 16:9 · seamless loop · mp4/webm, muted, under the size ceiling

A shot of someone sitting on the cushion on the driver's seat, one unbroken frame that never cuts. When they get out the cushion slowly springs back to its full thickness, and when they sit down again it presses down and hugs their lower back and pelvis.
```

## `features.items.3.image` — outcome

- asset `77-07-feature3-relief-scene.png` · feature section 4, beside the what-changed list
- recommended: **option A** · media **still**
- FIT decides, and the requires_pair is already paid for. 06-relief-scene closes an advertorial when the promise is a state of living rather than a feature, and this section is Sandra, the coastal drive they had put off, and stepping out of the car loose and upright. Its requires_pair is 01-pain-scene, which is at the header on the same man. The relief situation is chosen from what the problem forbade: A stages the exact inverse of the hero — the moment he braced against is the moment he now straightens up through. B closes with 06-relief-hero instead, product-forward and composed; that is the right close when the result is invisible, and here it is not. C moves the cost from a long drive to a lifted crate. PAGE LEGALITY: A is the page's second step-6 type and the arc holds, with no pain image after the first relief image. PRODUCT PRESENCE: standalone class — it stands on the seat through the open door as its own object, near the camera and turned so it can be read. PROMPT RISK: 1593 characters.

### features.items.3.image · option A — `06-relief-scene`

- varies on: baseline
- ratio `16:9` · type version `3.7` · upload the product photo · `gaze: candid`
- The release and the return in one frame: straightening up out of the driver's seat at the end of the drive, weight even, hands empty, the smile arriving on its own while he looks at the water.

```
A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his late forties in put-together but ordinary clothes, just out of the driver's seat of his car in a coastal car park at the end of a long drive, straightening up to his full height with his weight even through both feet and both hands empty and open at his sides. Nothing is held, nothing is braced, nothing is covered. His chest is opening, his shoulders roll back and down, his eyes are coming open against the light and his brow has let go, and a small involuntary smile has arrived on its own while he looks out past the car at the water rather than at the camera.

The driver's door stands open beside him, and the reference product sits on the seat inside it as its own object near the camera, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary public car park above a working coastline on an unremarkable day, two or three blurred passers-by and a parked van further along, gulls, a wire bin, painted bay lines worn thin. Nothing aspirational and nothing tidied.

Even natural daylight, bright, soft shadows, plain and unglamorous. A natural palette, light film grain, shallow depth of field, honest rather than drained and never warm-boosted.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text.
```

### features.items.3.image · option B — `06-relief-hero`

- varies on: type: the composed close instead of the candid one
- ratio `16:9` · type version `1.15` · upload the product photo · `register: commercial`, `inset_mode: none`
- The other type in the advertorial outcome cell. It presents the product in the resolved scene rather than letting the body carry the whole argument, and it is the safer close if the release does not read.
- **note:** COMBINATION: 06-relief-hero is the recommendation at features.items.1. Picking B here forces that slot to its own option B or C.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his late forties in an open-collar shirt, sitting relaxed in the driver's seat of a parked car with the door open and one arm resting easily along the sill, his gaze out through the windscreen rather than at the product. His weight is even through both hips, he is settled back against the seat with nothing braced, and he sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with things that genuinely belong there: a travel mug in the holder, a lanyard hung from the indicator stalk, a phone cable coiled at the dash, a folded jacket on the back seat, a parking permit clipped to the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text.

Soft even daylight through the open door, background blurred, high-key neutral grade.

The whole frame is the resolved state. No inset, no panel, no badge, no arrow and no mark of any kind anywhere in the picture.
```

### features.items.3.image · option C — `06-relief-scene`

- varies on: execution: the depot apron, not the coast
- ratio `16:9` · type version `3.7` · upload the product photo · `gaze: candid`
- Same type and same axis, a different situation with a different cost: lifting a crate onto his shoulder at work, which is the other thing the copy says the ache used to take.

```
A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his late forties in put-together but ordinary clothes, on the loading apron of a shipping depot mid-morning, lifting a crate off the tailgate of a van and up onto his shoulder in one unbroken movement, weight even through both feet and his back doing the work without hesitation. Nothing is braced against the van, nothing is favoured, nothing is held back. His chest opens as the crate goes up, his shoulders are back and down, his eyes are open and creased at the corners and a small involuntary smile has arrived on its own while he looks along the apron at the next load rather than at the camera.

The van's cab door stands open behind him, and the reference product sits on the driver's seat inside it as its own object near the camera, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary working depot apron on a grey weekday, two or three blurred colleagues further down the line, a pallet truck, a wheelie bin, worn painted bay markings and puddles from earlier rain.

Even natural daylight, bright, soft shadows, plain and unglamorous. A natural palette, light film grain, shallow depth of field, honest rather than drained and never warm-boosted.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text.
```

## `reviews.shots.0.image` — social-proof

- asset `77-08-review-1.png` · review grid tile 1 of 4
- recommended: **option A** · media **still**
- One option by law (ADR-022): the four tiles are the unit of variation, not the tile, and this one's place in the set is its varies_on line. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home, which is what the review copy claims. The SET DIVERSITY LAW is satisfied across the four: four room classes, four surfaces, four light temperatures, four camera distances and three of the type's three content modes.

### reviews.shots.0.image · option A — `05-social-snapshot`

- varies on: in-use · car driver seat · cool early daylight · seated arm's length
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the four-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the same review section as three attributed quotes, each carrying a reviewer name and a Verified Purchase label. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. The page's own brief already marks all four slots `route: asset`, and the type's avoid_when says real customer photos always win over generated ones. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and Verified Purchase labels — before rendering any of these.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use in a car, photographed by its owner from the open driver's door: the reference cushion in place on the driver's seat with the owner's forearm resting across the top of the lumbar section, nobody else visible and no face in shot.

An ordinary family car photographed exactly as found on a weekday morning — the mess stays, nothing tidied, nothing added for the picture. Cool early daylight through the windscreen and the open door, no other light.

One incidental owner object and no more: a travel mug sitting in the cup holder.

Framing slightly tilted and a little too close, taken at arm's length from the seat; focus adequate but casual, mild noise, exposure honest to the light in the car.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `reviews.shots.1.image` — social-proof

- asset `77-09-review-2.png` · review grid tile 2 of 4
- recommended: **option A** · media **still**
- One option by law (ADR-022): the four tiles are the unit of variation, not the tile, and this one's place in the set is its varies_on line. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home, which is what the review copy claims. The SET DIVERSITY LAW is satisfied across the four: four room classes, four surfaces, four light temperatures, four camera distances and three of the type's three content modes.

### reviews.shots.1.image · option A — `05-social-snapshot`

- varies on: at-rest · home office swivel chair · warm lamp light · standing above
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the four-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the same review section as three attributed quotes, each carrying a reviewer name and a Verified Purchase label. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. The page's own brief already marks all four slots `route: asset`, and the type's avoid_when says real customer photos always win over generated ones. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and Verified Purchase labels — before rendering any of these.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product simply sitting where it now lives, photographed by its owner: the reference cushion in place on a home office swivel chair, nobody in the picture at all.

An ordinary spare-room home office photographed exactly as found in the evening — the mess stays, nothing tidied, nothing added for the picture. Warm yellow light from a single desk lamp and the room's overhead, no daylight, no other light.

One incidental owner object and no more: a charger cable coiled on the desk behind the chair.

Framing off-centre and taken from standing height looking down at the chair; focus adequate but casual, mild motion softness, exposure honest to the lamp light.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `reviews.shots.2.image` — social-proof

- asset `77-10-review-3.png` · review grid tile 3 of 4
- recommended: **option A** · media **still**
- One option by law (ADR-022): the four tiles are the unit of variation, not the tile, and this one's place in the set is its varies_on line. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home, which is what the review copy claims. The SET DIVERSITY LAW is satisfied across the four: four room classes, four surfaces, four light temperatures, four camera distances and three of the type's three content modes.

### reviews.shots.2.image · option A — `05-social-snapshot`

- varies on: in-use · truck cab bench · flat overcast daylight · close over the shoulder
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the four-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the same review section as three attributed quotes, each carrying a reviewer name and a Verified Purchase label. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. The page's own brief already marks all four slots `route: asset`, and the type's avoid_when says real customer photos always win over generated ones. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and Verified Purchase labels — before rendering any of these.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use in a truck cab, photographed by its owner over their own shoulder: the reference cushion in place on the bench seat with two fingers of the owner's hand tucked against the edge of the lumbar section, no face in shot.

An ordinary working truck cab photographed exactly as found on a flat grey afternoon — the mess stays, nothing tidied, nothing added for the picture. Flat overcast daylight through the side window, no other light.

One incidental owner object and no more: a clipboard wedged against the far side of the seat.

Framing close and crooked, taken from very near the seat over the shoulder; focus adequate but casual, mild noise, exposure honest to the grey light.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `reviews.shots.3.image` — social-proof

- asset `77-11-review-4.png` · review grid tile 4 of 4
- recommended: **option A** · media **still**
- One option by law (ADR-022): the four tiles are the unit of variation, not the tile, and this one's place in the set is its varies_on line. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home, which is what the review copy claims. The SET DIVERSITY LAW is satisfied across the four: four room classes, four surfaces, four light temperatures, four camera distances and three of the type's three content modes.

### reviews.shots.3.image · option A — `05-social-snapshot`

- varies on: kit-flatlay · kitchen worktop · mixed warm and cool · half a metre back
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the four-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the same review section as three attributed quotes, each carrying a reviewer name and a Verified Purchase label. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. The page's own brief already marks all four slots `route: asset`, and the type's avoid_when says real customer photos always win over generated ones. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and Verified Purchase labels — before rendering any of these.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The opened box and its contents as the owner has just left them, photographed from above: the reference cushion out of its packaging and resting on a kitchen worktop, still recovering its shape, with the flattened box and the plastic sleeve it came in pushed to one side. Nobody in the picture at all.

An ordinary kitchen photographed exactly as found in the middle of the day — the mess stays, nothing tidied, nothing added for the picture. Mixed light, warm ceiling spots over cool daylight from the window, no other light.

One incidental owner object and no more: a fruit bowl at the edge of the worktop.

Framing slightly tilted and taken from standing height about half a metre back across the worktop; focus adequate but casual, mild noise, exposure honest to the mixed light.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

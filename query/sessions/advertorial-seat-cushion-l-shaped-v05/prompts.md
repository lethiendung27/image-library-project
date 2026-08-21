# Image prompts — page 120, ergonomic memory foam seat cushion

GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit the script and re-run. Routing rationale, the negative motion verdicts and the out-of-scope slots are all in `prompts.json`.

- page `120` · advertorial · solution-aware · registry `2.0.0` · 11 routed slots · 25 prompts · 3 motion briefs
- motion: 3 loops (3 whole-frame), floor 2, margin 1, groups result, working
- **4 prompts carry a blocking precondition**, stated on each

---

## `hero.image` — hero

- asset `120-01-hero-pain-scene.png` · advertorial header, under the eyebrow and above the byline
- recommended: **option A** · media **still**
- FIT decides, close to verbatim. 01-pain-scene --candid asks for physical pain in a moment nobody would choose to be seen in, and hero.body.0 is that moment in the page's own words — a half-full supermarket car park, unable to get out of the seat without leaning his whole body against the door frame. A plays it as that single action. B moves to the confront gaze, which the type reserves for appearance and self-image rather than physical pain. C moves it to the wooden bench at Sarah's birthday dinner, the social cost the copy names second. PAGE LEGALITY: A satisfies 06-relief-scene's pairing at content.items..3 and pairs_with 04-proof-lockedframe. PRODUCT PRESENCE: none, correctly — the type forbids it. PROMPT RISK: 1431 characters, inside the type's measured band.

### hero.image · option A — `01-pain-scene` `--candid`

- varies on: baseline
- ratio `16:9` · type version `1.14` · `gaze: candid`
- The page's opening scene as one action: a forearm braced along the door frame to lever himself off the seat in a cold car park. The evidence is the symptom as physical fact — hips below knees, the lumbar curve flat, the load on the base of the spine.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his mid-forties in a work shirt with the collar open, still in the driver's seat of his car in a half-empty supermarket car park, mid-way through levering himself up off the seat with one forearm braced flat along the top of the open door frame. Under that force: that elbow rigid and taking his whole weight, the other hand pushed down into the seat beside him, hips barely clear of the cushion, his back held in one unbending piece. Face: eyes shut, jaw clamped, breath held.

His hips sit well below his knees in the backward-sloping seat, his lower back is pressed flat against the seat back with an open gap behind it, and the whole load has gone onto the base of his spine.

One specific place: a supermarket car park on a cold evening with half the bays empty, the driver's door standing wide, and the lived-in clutter of the commute — a lanyard hung on the indicator stalk, a cold coffee in the holder, a folded hi-vis on the passenger seat, a parking permit clipped to the visor.

He is unaware of the camera. Key light: the last cold blue daylight across the tarmac. Fill: the weak dome light above him. A rim of light along his braced forearm. Deep shadow across the near third of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### hero.image · option B — `01-pain-scene` `--confront`

- varies on: axis: gaze=confront
- ratio `16:9` · type version `1.14` · `gaze: confront`
- The same argument in the type's other gaze, standing at the rear tire a minute later. The advertorial hero cell holds one type and the gates leave no second, so the honest variation here is the axis rather than a type borrowed from a role it does not belong to.
- **note:** The type reserves --confront for appearance and daily frustration rather than physical pain; it is offered because the axis is the only legal second dimension at this slot, not because it fits better.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his mid-forties in a work shirt with the collar open, standing beside his own rear tire in a supermarket car park with one hand pushed into the small of his back, turned towards the camera and holding its eye. Under that force: his weight thrown onto one hip, the other heel lifted clear of the tarmac, his free hand hanging heavy at his side, shoulders uneven. Face: brow raised and tight, mouth pressed thin, looking directly into the lens.

He cannot straighten fully: his trunk stays folded a few degrees forward of upright and his pelvis is tipped back under him, so the line from his shoulders to his hips reads as a shallow curve rather than a column.

One specific place: a half-empty supermarket car park on a cold evening, the driver's door still open behind him, and the ordinary clutter of the errand it interrupted — an empty trolley bay, a carrier bag on the passenger seat, a receipt caught under a wiper, painted bay lines worn thin.

Key light: flat white light from the car park lamp standard directly overhead, bright and unflattering, minimal shadow. Fill: the weak spill from the open cabin.

Desaturated throughout, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### hero.image · option C — `01-pain-scene` `--candid`

- varies on: execution: the birthday bench, not the car
- ratio `16:9` · type version `1.14` · `gaze: candid`
- Same type and same axis, the second cost the copy names — watching Sarah's outdoor birthday dinner from a stiff wooden bench, shifting hip to hip while everyone else sits comfortably. It sets up content.items..3, which resolves this exact class of situation.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A man in his mid-forties in an ordinary shirt, sitting on a stiff wooden bench pushed back against a garden fence at an outdoor birthday dinner, caught mid-way through shifting his weight from one hip to the other with both hands planted flat on the bench slats either side of him. Under that force: both arms locked straight and taking his weight off the bench, one hip lifted clear of the wood, his trunk held rigid, his knees pushed out for balance. Face: eyes down at the ground, mouth open on a held breath, jaw set.

He is the only person not settled: the bench has no back to it, his pelvis has rolled behind his sitting bones, and his lower back is unsupported over the hard edge of the slat.

One specific place: a suburban garden on an evening in early autumn, and the ordinary clutter of the party going on around him — a fire pit with chairs pulled close, paper plates stacked on a side table, a cardigan over the back of a chair, string lights on the fence, other guests blurred and comfortable around the fire.

He is unaware of the camera. Key light: the low orange of the fire pit from the far side. Fill: the string lights above him. A rim of light along his locked forearms. Deep shadow along the fence behind the bench.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

## `problems.items.0.image` — problem-agitation

- asset `120-02-problem0-pain-scene.png` · problem section 1, beside the What I Tried list
- recommended: **option A** · media **gif**
- FIT and PAGE LEGALITY together. The section's own What I Tried list names exactly three failed fixes and no others — flat memory foam wedges, inflatable donut rings, standalone strap-on lumbar rolls — so the image argues the pile rather than the person, and the hero already owns the recognition job. This is Step 4 rung 4: 01-pain-scene runs a second time in a different subject class, object-only, an execution the ledger already records twice. B is the stronger LITERAL fit — 04-proof-lockedframe's use_when names the 'I tried three things' beat verbatim — and it is not recommended because lockedframe is the only type the comparison and proof cells hold, and spending it here would empty one of them. EVIDENCE: the object-only execution is the runbook's own worked precedent. PRODUCT PRESENCE: none in A or B, correctly. PROMPT RISK: 1407 characters. MEDIA: gif — see the loop below.

### problems.items.0.image · option A — `01-pain-scene` `--candid`

- varies on: rung 4: same type, object-only subject class
- ratio `16:9` · type version `1.14` · `gaze: candid`
- The three named fixes thrown into the back seat, none of them in the driver's seat. No person, so the argument is carried entirely by what was given up on.
- **note:** Rung 4 of Step 4's ladder: another execution of a type already recommended at hero.image, differing on subject class. Declared here rather than left to look like an oversight.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is the three abandoned fixes filling the back seat of a car, photographed from the open rear door at standing height.

Exactly as they were thrown in and no more than these three: a flat memory foam wedge, compressed permanently into a body-shaped dish and folded once against the far door; an inflatable donut ring, half deflated with its valve stub sticking out, wedged on its edge behind the wedge; and a standalone strap-on lumbar roll with one buckle undone and the strap hanging loose across the seat. Every one of them has been used and none is in the driver's seat.

One specific place: a car parked in a supermarket bay on a cold evening with the rear door standing open, and the lived-in clutter of the routine none of them fixed — a cold coffee in a holder up front, a receipt curled in the door pocket, a folded hi-vis in the far footwell.

No subject, so no gaze. The frame looks across the back seat from the open door, the way the person who gave up on them is looking at it. Key light: the last cold daylight through the far window. Fill: the dim of the cabin. Rim light along the edge of the donut ring. Deep shadow into the footwell.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### problems.items.0.image · option B — `04-proof-lockedframe` `--rivals`

- varies on: type: 04-proof-lockedframe --rivals
- ratio `16:9` · type version `1.13`
- The same three fixes as a locked three-panel test on one seat, which is what lockedframe's use_when calls the 'I tried three things' beat. --rivals keeps the product out of frame, which this section requires.
- **note:** Picking B displaces 04-proof-lockedframe from content.items..1, whose recommended option is the only --timelapse on the page; that slot would fall to its own B. --rivals is advertorial-legal and barred only on marketplace. Single-pass: the panels run handheld (ADR-021).

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different evenings. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt in the door pocket, real wear on the sill.

The only thing that changes is which of the three ordinary fixes is on the seat, and each is the plain unbranded version people already own — the three the section names and no others. Panel one: a flat memory foam wedge, slid forward with its cover rucked into a ridge at the front lip. Panel two: an inflatable donut ring, gone soft and rolled forward on itself. Panel three: a standalone strap-on lumbar roll, sagged down the seat back with its strap gone slack. All three photographed at the same point in the routine, at the end of a nine-hour day, with the driver out of the car and nothing touched or straightened first.

Light differs only in exposure between panels, never in warmth. Muted and cool throughout, low saturation, no warm tone anywhere, one shared unresolved tone that favours none of them.

No product, no badges, no arrows and no text of any kind.
```

### problems.items.0.image · option C — `01-pain-scene` `--candid`

- varies on: execution: the boot, not the back seat
- ratio `16:9` · type version `1.14` · `gaze: candid`
- Same type and same object-only execution, moved to where things go when they are finished with rather than where they were last tried.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

No person in the frame. The subject is the three abandoned fixes stuffed into the open boot of a car, photographed square on from the rear at chest height.

Exactly as they were left and no more than these three: a flat memory foam wedge, permanently dished and shoved against the wheel arch; an inflatable donut ring, soft and creased, resting on top of it with its valve stub turned up; and a standalone strap-on lumbar roll, dropped in with both straps tangled around a jump lead. Nothing has been cleaned, matched or squared up.

One specific place: the open boot of an ordinary estate car on a cold evening in a supermarket car park, and the clutter of the routine around them — a folded shopping bag, a screenwash bottle on its side, a child's football under the parcel shelf, a bag of grit split at the corner.

No subject, so no gaze. The frame looks straight into the boot from behind, the way the person who filled it is looking at it. Key light: the car park lamp standard overhead, cold and hard. Fill: the weak boot lamp. Rim light along the lip of the boot. Deep shadow behind the objects.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### problems.items.0.image · the motion brief — `cause` (whole-frame)

- form `whole-frame` · rung `re-execution` · reference folder: gifs-library/cause/ — no files filed yet; the folder card carries the law
- plate `plates/120-02-problem0-pain-scene--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
advertorial-cause-seat-cushion-l-shaped-v05.webp
3s · 16:9 · seamless loop · animated webp, loop-safe, under the size ceiling

A shot of a driver sitting on a thin foam wedge on his car seat. The car brakes at a junction, the wedge slides forward under him and his pelvis rolls back into the open gap behind it, which is where the ache starts.

IF THAT CANNOT BE SHOT
A shot of the same seat with a hand pushing a foam wedge forward from behind, nobody in the car. The wedge travels to the front lip and the gap opens behind it, the same gap a pelvis drops into.
```

## `problems.items.1.image` — cause

- asset `120-03-problem1-cause-anatomy.png` · problem section 2, beside the Why Fixes Missed list
- recommended: **option A** · media **still**
- FIT decides. The section names its own mechanism three times — the junction crevice where the seat base meets the backrest, the hips dropping below the knees, and the destructive shear forces — and 02-cause-anatomy --diagnostic is the only type on this channel that draws a named mechanism. A takes the shear as its third mark, because the copy names it: the two surfaces working against each other is the fault in the section's own words. B swaps the drawn contour for the reference product, which answers a question this section has not asked yet — content.items..0 is where the product arrives. C moves to the sitting-bones view, which argues the tailbone half. PRODUCT PRESENCE: none in A, correctly — --diagnostic is the variant that needs no reference photo. PROMPT RISK: 2119 characters against a ~1800 two-mark reference; A carries three marks and states the overage rather than hiding it.

### problems.items.1.image · option A — `02-cause-anatomy` `--diagnostic`

- varies on: baseline
- ratio `16:9` · type version `1.15`
- The pelvis hinging back into the crevice, side on, with the hip-to-knee measure and the shear at the seat corner both drawn. The section names both.

```
A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, the sacrum and the lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has hinged backward into the open crevice where the seat base meets the upright backrest and the lumbar curve has flattened and reversed. Right panel: the same figure on the same seat with one continuous unyielding contour filling that crevice, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the contour covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. A pair of short opposed arrows at the seat corner in each panel showing the shear the copy names, red on the left where the two surfaces work against each other, blue on the right where one contour carries them. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

### problems.items.1.image · option B — `02-cause-anatomy`

- varies on: axis: the product in the corrected panel
- ratio `16:9` · type version `1.15` · upload the product photo
- The same two panels in flat vector with the reference product doing the correcting instead of an unnamed contour.
- **note:** Picking B introduces the product one section earlier than the copy does, and content.items..0's mechanism argument then lands second rather than first. It also needs the reference photo attached, which A does not.

```
A 2D flat-vector medical illustration with flat fills and hard edges, no gradients. Not photography, not a 3D render.

The attached photo is the exact reference for the product.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same side-on view in both, the whole body in shot with the seat small within it. The pelvis, the sacrum and the lumbar spine are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. This is a pelvis and lumbar spine, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded, the pelvis hinged back into the crevice at the seat corner. Right panel: the same figure on the same seat with the reference product in place, drawn at a size and angle where it is obviously that product, the pelvis upright on its sitting bones and the lumbar curve restored. Neither the seat nor the product covers the spine on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at its two landmarks — the top of the hip bone and the top of the knee, measured against the length of the thigh rather than against the frame, both starting from the same point in their panel. Red on the left where the hip sits far below the knee, blue on the right where it sits level. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

### problems.items.1.image · option C — `02-cause-anatomy` `--diagnostic`

- varies on: execution: three-quarter rear, the sitting bones
- ratio `16:9` · type version `1.15`
- Same type and same variant from behind, arguing the tailbone half of the same fault — the load leaving the two sitting bones for the base of the sacrum.

```
A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

Exactly one seated human figure per panel, the same figure at the same scale and the same three-quarter rear view in both, the whole body in shot with the seat small within it. The two sitting bones, the sacrum and the soft tissue over them are drawn in warm ivory over a translucent body outline, and the same structures appear in both panels. These are the sitting bones and the sacrum, not a full skeleton.

Left panel: the figure sitting in an ordinary car seat whose base slopes backward, drawn realistically and unbranded. The pelvis has hinged back off the sitting bones and the load has moved onto the tailbone at the base of the sacrum. Right panel: the same figure on the same seat with one continuous contour filling that crevice, the load back on the two sitting bones and the tailbone clear of the seat. Neither the seat nor the contour covers the sacrum on either panel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each stopping at the same two landmarks — the top of the hip bone and the top of the knee — both starting from the same point in their panel, red on the left and blue on the right. A filled region bounded by the contact surface itself, as wide as the contact is, one per panel: red on the left over the tailbone where the load has gone, blue on the right across both sitting bones where it belongs. One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

## `content.items..0.image` — mechanism

- asset `120-04-content0-mechanism-ghostbody.png` · body item 1, beside the What makes it work list
- recommended: **option A** · media **still**
- FIT decides. The section's whole claim is structural — one piece rather than two, bridging the gap the previous section opened — and 03-mechanism-ghostbody is the type that cross-sections a body against a product. `body_contact: true` keeps it legal here; it is the gate that would otherwise send this slot to 03-mechanism-xray, whose own use_when restricts it to products that do NOT act on a body structure. A draws the wrong state as two separate pieces with a gap between them, which is the comparison the copy actually makes. B is a photograph and sells the relief instead of explaining it. RATIO: 03-mechanism-ghostbody declares 1:1 and 4:5 only, so A and C render at 1:1 into a 16:9 slot and the layout centre-crops 25% of the width; the two panels run left to right, so each loses the same band and the argument survives. B renders at the slot's own 16:9 and is the option to take if the crop is unacceptable. PROMPT RISK: 2021 characters.

### content.items..0.image · option A — `03-mechanism-ghostbody`

- varies on: baseline
- ratio `1:1` · type version `2.2` · upload the product photo
- Two panels, one mannequin, cross-sectioned: two separate pieces with a gap at the seat corner against one continuous contour with none. The product is the only object with a real finish in either panel.
- **note:** RATIO: renders at 1:1 into a 16:9 slot. The layout centre-crops about 25% of the width; the panels sit side by side so both lose the same band and neither is favoured. Take B if the crop cannot be accepted.

```
A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated side-on in an ordinary matte grey car seat whose base slopes backward: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical seat in both. The body is cross-sectioned along the midline so the pelvis, the sacrum and the lumbar spine are visible inside the silhouette.

The pelvis, the sacrum and the lumbar vertebrae are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: two separate matte grey pieces sit on the seat, a pad on the base and a roll against the backrest, with a visible gap between them at the seat corner. The mannequin's pelvis has hinged backward into that gap and the hips have dropped below the knees.

Right panel is the correct state: the reference product is in place on the same seat at the same angle as one single object, its contour running unbroken from the seat section up into the lumbar section with no join anywhere along it, the hips lifted level with the knees. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all. A flat hard-edged blue band, unshaded, is drawn beside the lumbar spine along its own length on the side away from the product, running only the length the product reaches — never a fill of the bone, never a tint of the anatomy.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product.
```

### content.items..0.image · option B — `06-relief-hero` `--vsinset`

- varies on: type: 06-relief-hero --vsinset
- ratio `16:9` · type version `1.16` · upload the product photo · `register: commercial`, `inset_mode: vsinset`
- The same wrong-versus-right argument as a photograph with the comparison held in a two-half inset, rather than as a cross-section. It renders at the slot's own ratio and nothing is cropped.
- **note:** Picking B displaces 06-relief-hero from content.items..2, whose recommended option is the only --context on the page; that slot would fall to its own B. B also needs the reference photo attached.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar work shirt, seated in the driver's seat of a parked car with the door open, his weight settled evenly and his gaze out through the windscreen rather than on the product, sitting well back so the whole seat back and the product against it are clear to the camera. He sits to the right of the frame.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with objects that genuinely belong there: a lanyard on the indicator stalk, a travel mug in the holder, a phone cable coiled at the dash, a folded hi-vis on the passenger seat, a parking permit on the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, occupying the space he is offset from, sits a small rectangular panel with a thin white border, split into two equal halves that share one photographic register. The left half shows the same seat with a flat foam wedge on the base and a separate strap-on roll against the backrest, the wedge slid forward and the roll dropped into the crevice between them, with glowing red points on the exposed seat corner and on the fallen roll. The right half shows the same seat with the reference product in place, brighter and cleaner, with a translucent blue overlay following the single continuous seam that runs from the seat section up into the lumbar section. A circular red badge carrying the white letters VS sits at the seam between the two halves.

No mark of any kind appears anywhere outside that panel.
```

### content.items..0.image · option C — `03-mechanism-ghostbody`

- varies on: execution: the office chair, three-quarter rear
- ratio `1:1` · type version `2.2` · upload the product photo
- Same type and same marks on the other seat the copy names, from behind. The office chair is where the second half of his day happens.
- **note:** RATIO: renders at 1:1 into a 16:9 slot, same 25% width crop as A.

```
A 3D technical render.

The attached photo is the exact reference for the product.

Two equal panels side by side, each a full 3D technical render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, divided by a single thin vertical line. No cast shadow on a floor.

The same featureless matte white mannequin in both panels, seated in three-quarter rear view in an ordinary matte grey office swivel chair whose base slopes backward: no face, no hair, no clothing, no skin tone. Identical pose, identical angle and identical chair in both. The body is cross-sectioned along the midline so the pelvis, the sacrum and the lumbar spine are visible inside the silhouette.

The pelvis, the sacrum and the lumbar vertebrae are the neutral structure, in warm off-white ivory, cut the same way in both panels.

Left panel is the wrong state: nothing fills the crevice where the chair base meets the backrest, the pelvis has hinged backward into it and the hips have dropped below the knees. A flat hard-edged red overlay, unshaded, lies on the sacrum and the two lowest lumbar vertebrae where the load has collected.

Right panel is the correct state: the reference product is in place on the same chair at the same angle as one single object, its contour running unbroken from the seat section up into the lumbar section, the hips lifted level with the knees. The product is the only object in either frame with a real material finish, and it keeps its own reference colours and carries no signal colour at all. A flat hard-edged blue band, unshaded, is drawn beside the lumbar spine along its own length on the side away from the product, running only the length the product reaches.

One filled solid disc badge in the top corner of each panel with the glyph cut out of it, the same diameter in both: a red X on the left, a green check on the right.

Achromatic white and grey everywhere except those marks. No mark is placed on the product.
```

## `content.items..1.image` — proof

- asset `120-05-content1-proof-lockedframe.png` · body item 2, beside the What makes it work list
- recommended: **option A** · media **gif**
- FIT plus the type's own VARIANT SELECTION RULE. The claim is durability across a working day — it does not crush flat, and after eight hours it comes back to its full profile — which is a difference that only exists over TIME. lockedframe's use_when admits the type only where the difference is visible inside a static frame, and its variant rule sends exactly this case to --timelapse: one locked framing, the same object, three points in one day. B holds the same claim as a magnified foam core in a --detail inset, which shows density but cannot show recovery. EVIDENCE: the three-panel locked framing is the type's most-rendered execution on this product. PRODUCT PRESENCE: the product is the subject of all three panels, correctly. PROMPT RISK: 1740 characters. MEDIA: gif — the panels are the reason, see below.

### content.items..1.image · option A — `04-proof-lockedframe` `--timelapse`

- varies on: baseline
- ratio `16:9` · type version `1.13` · upload the product photo
- One seat, one framing, three points across a working day, nothing plumped back into place first. The contour still standing at the end is the whole argument.
- **note:** Single-pass: the panels run handheld rather than strict, which is the route this type's own capability gate records for a renderer that cannot composite (ADR-021).

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product.

Shot by one person on a phone across one working day. One framing for every panel: the same car driver's seat photographed from the open door at standing height from about a metre back, the seat base across the lower third and the head restraint at the top of the frame. It reads as one shot taken three times, never as three different shots.

The same car, the same seat and the same door frame in all three panels, with deliberate real-world clutter: a lanyard on the indicator stalk, a receipt in the door pocket, real wear on the sill.

The reference product is the subject of every panel and is the same physical object throughout — the same outline, the same black, the same continuous L-shaped contour, matching the attached photo exactly. It sits in the same position on the seat in every panel.

The only thing that changes is the point in the day: panel one at six in the morning before the first drive, panel two at midday after five hours of sitting, panel three at the end of an eight-hour shift. Every panel is photographed at the same point in the routine, with the driver already out of the car and nothing plumped, straightened or pushed back into place first. Across all three the contour still stands to its full depth at the seat corner and the seat section has not compressed into a dish.

Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind.
```

### content.items..1.image · option B — `06-relief-hero` `--detail`

- varies on: type: 06-relief-hero --detail
- ratio `16:9` · type version `1.16` · upload the product photo · `register: commercial`, `inset_mode: detail`
- The same claim as one photograph with the foam core magnified in a corner inset: the cell structure readable and the seat section visibly not bottoming out under his weight.
- **note:** Picking B displaces 06-relief-hero from content.items..2 and leaves this page with no --timelapse; the durability-over-time half of the claim then rests on the loop alone.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar work shirt, sitting relaxed in the driver's seat of a parked car with the door open, one hand loose on his thigh and his gaze out through the windscreen rather than at the product. He is settled back with his weight even through both hips and nothing braced, and he sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with things that genuinely belong there: a lanyard on the indicator stalk, a travel mug in the holder, a phone cable coiled at the dash, a folded hi-vis on the passenger seat, a parking permit on the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border, showing one magnified detail the scene cannot carry at this distance: the cut edge of the product's foam core under his weight, close enough that the dense closed cell structure is readable and the seat section is visibly still standing to its full depth rather than bottoming out. It is a photograph in the same register as the scene and does not bleed into it, linked to the product by proximity alone with no arrow and no glow border.

No mark of any kind appears anywhere in the frame.
```

### content.items..1.image · option C — `04-proof-lockedframe` `--timelapse`

- varies on: execution: the office chair, not the car
- ratio `16:9` · type version `1.13` · upload the product photo
- Same type, same variant and same framing discipline on the other seat the copy names, across a typing day rather than a driving one.
- **note:** Single-pass: panels run handheld (ADR-021).

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product.

Shot by one person on a phone across one working day. One framing for every panel: the same office swivel chair photographed square-on from about a metre and a half back at seated eye height, the seat base across the lower third and a plain office partition filling the upper third. It reads as one shot taken three times, never as three different shots.

The same chair, the same partition and the same floor in all three panels, with deliberate real-world clutter: a coiled network cable along the skirting, a recycling bin half out of shot, scuff marks on the chair base.

The reference product is the subject of every panel and is the same physical object throughout — the same outline, the same black, the same continuous L-shaped contour, matching the attached photo exactly. It sits in the same position on the chair in every panel.

The only thing that changes is the point in the day: panel one at nine in the morning before anyone sits down, panel two at midday after four hours of typing, panel three at the end of an eight-hour shift. Every panel is photographed at the same point in the routine, with nobody in the room and nothing plumped, straightened or squared up first. Across all three the contour still stands to its full depth at the chair corner and the seat section has not compressed into a dish.

Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind.
```

### content.items..1.image · the motion brief — `proof` (whole-frame)

- form `whole-frame` · rung `re-execution` · reference folder: gifs-library/proof/ — no files filed yet; the folder card carries the law
- plate `plates/120-05-content1-proof-lockedframe--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
advertorial-proof-seat-cushion-l-shaped-v05.webp
3s · 16:9 · seamless loop · animated webp, loop-safe, under the size ceiling

A close shot of the cushion alone on a car seat at the end of a shift. A hand presses the seat section down flat and lets go, and the contour rises back to its full depth at the seat corner without a dent left in it.

IF THAT CANNOT BE SHOT
A close shot of the cushion on an office chair with a full backpack set down on the seat section. The pack is lifted away and the contour springs back to its full depth while a thin foam pad beside it stays dished.
```

## `content.items..2.image` — how-to-use

- asset `120-06-content2-relief-hero.png` · body item 3, beside the What to know list
- recommended: **option A** · media **still**
- THE ROLE'S OWN CELL IS EMPTY AFTER THE GATES, and this basis says so rather than leaving it inferred. how-to-use on advertorial holds 03-use-sequence alone, and `multi_step_usage: false` drops it — the type's own avoid_when reads 'the product has one obvious action', which placing a cushion on a seat is. Step 4's ladder therefore runs to rung 2, an adjacent step. FIT then decides between what is left: 06-relief-hero --context is defined as the hero showing the product in hand when the buyer still needs to see where it lives, and this section is exactly that — carried from car to office in ten seconds, and it lives in both. A puts it in his hand with the car seat in the inset. B argues the grip half instead, across the three surfaces the copy names. PRODUCT PRESENCE: in hand and in the inset, which is the point. PROMPT RISK: 1691 characters.

### content.items..2.image · option A — `06-relief-hero` `--context`

- varies on: rung 2: adjacent step, the role's own cell is gated out
- ratio `16:9` · type version `1.16` · upload the product photo · `register: commercial`, `inset_mode: context`
- The product carried loose in one hand into the office, with the driver's seat it just left held in the corner inset. Two places, one object, no straps in frame.
- **note:** The how-to-use cell holds only 03-use-sequence and the multi_step_usage gate drops it, so this slot is filled from an adjacent step under Step 4 rung 2. Said here rather than left to look like a free choice.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar work shirt, standing in an office doorway with the reference product carried loose in one hand down at his side, mid-stride and looking ahead into the room rather than at the product. Nothing is braced and nothing is held in the other hand. He stands to the right of the frame so the product and the room beyond him stay clear to the camera.

The reference product hangs from his hand by the lumbar section, identical to the attached photo in shape, colour and proportion, its continuous L-shaped contour readable against his leg.

One real open-plan office filled to the edges with objects that genuinely belong there: a stacked in-tray, a mug on a coaster, a coat over a chair back, a wheeled pedestal drawer, a whiteboard turned to the wall, a plant on a filing cabinet. Background blurred, but no bare wall or floor area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border, showing where the product lives when it is not in his hand: the same product seated in the driver's seat of his car, photographed from the open door, its seat section on the base and its lumbar section up the seat back. It is a photograph in the same register as the scene and does not bleed into it, linked to the product by proximity alone with no arrow and no glow border.

No mark of any kind appears anywhere in the frame.
```

### content.items..2.image · option B — `04-proof-lockedframe` `--verdict`

- varies on: type: 04-proof-lockedframe, the grip claim
- ratio `16:9` · type version `1.13` · upload the product photo
- The other half of the section: the same object anchored square on fabric, on smooth leather and on vegan leather, with no strap or buckle anywhere in frame. It proves the grip; it does not show the carry.
- **note:** Picking B displaces 04-proof-lockedframe from content.items..1, whose recommended option is the only --timelapse on the page. Single-pass: the panels run handheld (ADR-021).

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in every panel.

Shot by one person on a phone across one day. One framing for every panel: the seat photographed square-on from about a metre back at seated eye height, the seat base across the lower third. It reads as one shot taken three times, never as three different shots.

The reference product is the same physical object in all three panels — the same outline, the same black, the same continuous L-shaped contour, matching the attached photo exactly.

The only thing that changes is the surface it is anchored on, and each is photographed after the seat has been used and left, with nobody in shot and nothing straightened or pushed back into place first. Panel one: a fabric car seat with a lanyard on the stalk behind it. Panel two: a smooth leather driver's seat in a second car, with a receipt in the door pocket. Panel three: a vegan leather office swivel chair with a coiled cable along the skirting behind it. In every panel the product sits square where it was put, its back edge still tight into the seat corner, with no strap, no buckle and no fixing of any kind anywhere in frame.

Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind.
```

### content.items..2.image · option C — `06-relief-hero` `--context`

- varies on: execution: the car park, and a different person
- ratio `16:9` · type version `1.16` · upload the product photo · `register: commercial`, `inset_mode: context`
- Same type and same inset mode at the other end of the journey, with the office chair in the inset instead of the car seat.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her early fifties in a plain jumper, standing beside her open car door in a workplace car park with the reference product carried loose in one hand down at her side, already turned towards the building rather than looking at the product. Nothing is braced and nothing is held in the other hand. She stands to the right of the frame so the product and the open cabin behind her stay clear to the camera.

The reference product hangs from her hand by the lumbar section, identical to the attached photo in shape, colour and proportion, its continuous L-shaped contour readable against her coat.

One real workplace car park filled to the edges with things that genuinely belong there: painted bay lines worn thin, a wheeled bin against a wall, a bicycle in a rack, a low hedge, other parked cars, a wet patch across the tarmac. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even overcast daylight, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border, showing where the product lives at the other end of the journey: the same product seated on a home office swivel chair, photographed square on, its seat section on the base and its lumbar section up the chair back. It is a photograph in the same register as the scene and does not bleed into it, linked to the product by proximity alone with no arrow and no glow border.

No mark of any kind appears anywhere in the frame.
```

## `content.items..3.image` — outcome

- asset `120-07-content3-relief-scene.png` · body item 4, beside the What changed list
- recommended: **option A** · media **gif**
- FIT decides, and the type's own boundary confirms it. 06-relief-scene is the closing image of an advertorial when the promise is a state of living rather than a feature, and this section is three restored situations in a row. `result_visibility: on-body` keeps it legal — the gate that kills it is `invisible`, and standing straight out of a car is as on-body as a result gets. Its pairing with 01-pain-scene is satisfied at hero.image. A takes the hotel car park after six hours, which the copy names first and in the most physical terms. B closes with the product in frame under him instead, which is the boundary case relief-scene's own worked example marks as the wrong side here. C takes the river trail. PRODUCT PRESENCE: on the seat behind him, not held and not centred — the type is explicit that it must be in the picture without being presented. PROMPT RISK: 1653 characters. MEDIA: gif — see below.

### content.items..3.image · option A — `06-relief-scene`

- varies on: baseline
- ratio `16:9` · type version `3.7` · upload the product photo
- The hotel car park at the end of the six-hour drive: coming to full height in one movement, both hands empty, the product on the seat behind him as its own object.

```
A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his mid-forties in put-together but ordinary clothes, just out of the driver's seat of his car in a hotel car park at the end of a six-hour drive, straightening up to his full height with his weight even through both feet and both hands empty and open at his sides. Nothing is held, nothing is braced, nothing is covered. His chest is opening, his shoulders roll back and down, his eyes are coming open against the light and his brow has let go, and a small involuntary smile has arrived on its own while he looks off past the car at the road he has just come in on rather than at the camera.

The driver's door stands open beside him, and the reference product sits on the seat inside it as its own object near the camera, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary hotel car park on an unremarkable November afternoon, a second car and a blurred couple unloading further along, a wheeled suitcase upright on the tarmac, a wire bin, painted bay lines worn thin, a low wall behind. Nothing aspirational and nothing tidied.

Even natural daylight, bright, soft shadows, plain and unglamorous. A natural palette, light film grain, shallow depth of field, honest rather than drained and never warm-boosted.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text.
```

### content.items..3.image · option B — `06-relief-hero`

- varies on: type: 06-relief-hero
- ratio `16:9` · type version `1.16` · upload the product photo · `register: commercial`, `inset_mode: none`
- The same beat closed with the product in frame under him rather than beside him — settled in the driver's seat with nothing braced.
- **note:** Picking B displaces 06-relief-hero from content.items..2. The type's own boundary sends an on-body result to relief-scene and reserves relief-hero for results that are invisible, so B is the weaker fit here by the type's own words and is offered as the second legal type, not as an improvement.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A man in his mid-forties in an open-collar work shirt, sitting settled in the driver's seat of a parked car with the door open, both hands loose in his lap and his gaze out along the road ahead rather than at the product. His weight is even through both hips, his shoulders are down, nothing is braced. He sits to the right of the frame so the whole seat back and the product against it stay clear to the camera.

The reference product is on the seat beneath and behind him, its seat section under him and its lumbar section standing up against the small of his back, identical to the attached photo in shape, colour and proportion.

One real car interior filled to the edges with objects that genuinely belong there: a lanyard on the indicator stalk, a travel mug in the holder, a road atlas folded on the passenger seat, a phone cable coiled at the dash, a parking permit on the visor, floor mats with real wear on them. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even daylight through the open door, high-key neutral grade.

No inset, no panel and no reserved layer anywhere in the frame.

No mark of any kind appears anywhere in the frame.
```

### content.items..3.image · option C — `06-relief-scene`

- varies on: execution: the river trail, not the car park
- ratio `16:9` · type version `3.7` · upload the product photo
- Same type at the second restored situation the copy names — thirty miles with his brother's Saturday group, with the car and the product parked behind him.

```
A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A man in his mid-forties in ordinary cycling clothes without a club kit, standing over a bicycle at the side of a river trail with both feet flat on the path and both hands resting easy on the bars, mid-conversation with someone out of frame. Nothing is held against him, nothing is braced, nothing is covered. His chest is open, his shoulders are down and back, his head is up and turned along the trail, and a small involuntary smile has arrived on its own while he looks away from the camera.

His car is parked on the gravel behind him with the driver's door open, and the reference product sits on the seat inside it as its own object, turned so its face can be read, in the picture the way a documentary photographer standing in the right place would include it. It is not held, not offered, not centred and not lit for the camera.

An ordinary riverside path on a grey Saturday morning, two or three blurred riders further along, a bin at the trail head, gravel scattered onto the tarmac, painted bay lines worn thin. Nothing aspirational and nothing tidied.

Even natural daylight, bright, soft shadows, plain and unglamorous. A natural palette, light film grain, shallow depth of field, honest rather than drained and never warm-boosted.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text.
```

### content.items..3.image · the motion brief — `relief` (whole-frame)

- form `whole-frame` · rung `natural` · reference folder: gifs-library/relief/ — no files filed yet; the folder card carries the law
- plate `plates/120-07-content3-relief-scene--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
advertorial-relief-seat-cushion-l-shaped-v05.webp
3s · 16:9 · seamless loop · animated webp, loop-safe, under the size ceiling

A shot of a man opening his car door in a hotel car park after six hours of driving. He swings both legs out and stands straight up in one movement, hands empty, and walks off without reaching back for his lower back.

IF THAT CANNOT BE SHOT
A shot of the same man on a river trail beside a bicycle. He swings one leg over the saddle, settles onto it and pushes off along the path in one easy movement, with nothing braced and no hand going to his back.
```

## `reviews.shots.0.image` — social-proof

- asset `120-08-review-social-snapshot.png` · photo grid, tile 1 of 4
- recommended: **option A** · media **still**
- ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of variation, so the four tiles differ from each other rather than from a B and a C. This tile's place in the set: van cab · driver's seat · in use, owner's forearm in shot · cool early daylight · arm's length from the seat. The working-driver quote in the block, taken where that work happens. In-use mode with a body part in shot and no face. FIT: the tile answers a quote the block actually carries. PRODUCT PRESENCE: the reference product is the subject of every tile. PROMPT RISK: 921 characters.

### reviews.shots.0.image · option A — `05-social-snapshot`

- varies on: van cab · driver's seat · in use, owner's forearm in shot · cool early daylight · arm's length from the seat
- ratio `1:1` · type version `1.2` · upload the product photo
- The working-driver quote in the block, taken where that work happens. In-use mode with a body part in shot and no face.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the SAME section element as three attributed quotes carrying reviewer names and Verified Purchase labels — measured on this export, zero closing tags between the grid and the quotes. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and the verified labels — before rendering any of these. Sixth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use in a van cab, photographed by its owner from the open driver's door: the reference cushion in place on the driver's seat with the owner's forearm resting across the top of the lumbar section, no face in shot.

An ordinary working delivery van cab photographed exactly as found early on a weekday — the mess stays, nothing tidied, nothing added for the picture. Cool early daylight through the windscreen and the open door, no other light.

One incidental owner object and no more: a bunch of van keys dropped in the door bin.

Framing slightly tilted and a little too close, taken at arm's length from the seat; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `reviews.shots.1.image` — social-proof

- asset `120-09-review-social-snapshot.png` · photo grid, tile 2 of 4
- recommended: **option A** · media **still**
- ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of variation, so the four tiles differ from each other rather than from a B and a C. This tile's place in the set: spare-room office · swivel chair · at rest, nobody present · warm desk lamp · standing height looking down. The desk-worker quote. At-rest mode, nobody in the picture, and the only warm-lit tile in the set. FIT: the tile answers a quote the block actually carries. PRODUCT PRESENCE: the reference product is the subject of every tile. PROMPT RISK: 825 characters.

### reviews.shots.1.image · option A — `05-social-snapshot`

- varies on: spare-room office · swivel chair · at rest, nobody present · warm desk lamp · standing height looking down
- ratio `1:1` · type version `1.2` · upload the product photo
- The desk-worker quote. At-rest mode, nobody in the picture, and the only warm-lit tile in the set.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the SAME section element as three attributed quotes carrying reviewer names and Verified Purchase labels — measured on this export, zero closing tags between the grid and the quotes. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and the verified labels — before rendering any of these. Sixth routed page in a row to breach it, so it is a template defect rather than a page one.

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

- asset `120-10-review-social-snapshot.png` · photo grid, tile 3 of 4
- recommended: **option A** · media **still**
- ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of variation, so the four tiles differ from each other rather than from a B and a C. This tile's place in the set: front room · wheelchair · in use, owner looking into their own lap · flat overcast daylight · very close, straight down. The wheelchair quote, which the block names explicitly and which no other tile covers. In-use mode from a first-person angle. FIT: the tile answers a quote the block actually carries. PRODUCT PRESENCE: the reference product is the subject of every tile. PROMPT RISK: 893 characters.

### reviews.shots.2.image · option A — `05-social-snapshot`

- varies on: front room · wheelchair · in use, owner looking into their own lap · flat overcast daylight · very close, straight down
- ratio `1:1` · type version `1.2` · upload the product photo
- The wheelchair quote, which the block names explicitly and which no other tile covers. In-use mode from a first-person angle.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the SAME section element as three attributed quotes carrying reviewer names and Verified Purchase labels — measured on this export, zero closing tags between the grid and the quotes. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and the verified labels — before rendering any of these. Sixth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use on a wheelchair, photographed by its owner looking down into their own lap: the reference cushion in place beneath and behind them with one hand resting on the armrest beside it, no face in shot.

An ordinary front room photographed exactly as found in the middle of the afternoon — the mess stays, nothing tidied, nothing added for the picture. Flat overcast daylight through a net-curtained window, no other light.

One incidental owner object and no more: a folded newspaper wedged down the side of the seat.

Framing close and crooked, taken from very near looking straight down; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `reviews.shots.3.image` — social-proof

- asset `120-11-review-social-snapshot.png` · photo grid, tile 4 of 4
- recommended: **option A** · media **still**
- ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of variation, so the four tiles differ from each other rather than from a B and a C. This tile's place in the set: kitchen · table · just-unboxed, nobody present · mixed ceiling and window light · half a metre back at standing height. The arrival moment none of the quotes describes, which is what stops the wall reading as four photographs of the same afternoon. FIT: the tile answers a quote the block actually carries. PRODUCT PRESENCE: the reference product is the subject of every tile. PROMPT RISK: 928 characters.

### reviews.shots.3.image · option A — `05-social-snapshot`

- varies on: kitchen · table · just-unboxed, nobody present · mixed ceiling and window light · half a metre back at standing height
- ratio `1:1` · type version `1.2` · upload the product photo
- The arrival moment none of the quotes describes, which is what stops the wall reading as four photographs of the same afternoon.
- **note:** PRECONDITION, and it is not optional: these four photo tiles sit inside the SAME section element as three attributed quotes carrying reviewer names and Verified Purchase labels — measured on this export, zero closing tags between the grid and the quotes. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and the verified labels — before rendering any of these. Sixth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The opened box and its contents as the owner has just left them: the reference cushion out of its packaging on a kitchen table, still recovering its shape, with the flattened box and the plastic sleeve pushed to one side. Nobody in the picture at all.

An ordinary kitchen photographed exactly as found in the middle of the day — the mess stays, nothing tidied, nothing added for the picture. Mixed light, warm ceiling spots over cool daylight from the window, no other light.

One incidental owner object and no more: a fruit bowl at the edge of the table.

Framing slightly tilted and taken from standing height about half a metre back; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

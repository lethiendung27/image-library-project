# Image prompts — page 97, electric spray air cushion massage comb

GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit the script and re-run. Routing rationale, the negative motion verdicts, the reserves and the out-of-scope slot are all in `prompts.json`.

- page `97` · advertorial (lpTypeId listicle) · problem-aware · registry `2.0.0` · 14 routed slots · 20 prompts · 3 motion briefs
- motion: 3 loops, floor 2, margin 1, groups result, working, 2 reserves
- **6 prompts carry a blocking precondition**, stated on each — do not render those until it is resolved
- **1 additive proposal** below the routed slots — a rung the page does not cover

---

## `hero.image` — hero

- asset `97-01-hero-pain-scene.png` · listicle header, under the title and above the byline
- recommended: **option A** · media **still**
- FIT decides. 01-pain-scene --candid asks for physical limitation in a moment nobody would choose to be seen in, and hero.intro names two of them — static-charged morning frizz before urgent meetings, and morning tears detangling a child's knots. A takes the first because it is the one the reader lives alone and the page's own headline leads with it. B moves to the confront gaze, which the type reserves for appearance and self-image; frizz before a call is genuinely close to that line, which is why it is offered rather than dismissed. C takes the second moment, mother and child in the hallway. RATIO: the hero is the only 16:9 slot on this page and 01-pain-scene is one of the types that declares it, so nothing is cropped here. PAGE LEGALITY: A satisfies 04-proof-lockedframe's pairs_with across the five reason cards. PRODUCT PRESENCE: none, correctly — the type bans it, so G8 does not reach this slot. PROMPT RISK: 1445 characters against a measured band of 1379-2153.

### hero.image · option A — `01-pain-scene` `--candid`

- varies on: baseline
- ratio `16:9` · type version `1.14` · `gaze: candid`
- The page's own opening problem as one action: brushing dry hair at the basin and making the halo worse. Evidence is the symptom itself on the body — strands standing off the head, clinging to the cheek, springing back when the hand lifts.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A woman in her mid-thirties in a work blouse with the cuffs still unbuttoned, standing at the basin of a small family bathroom early on a weekday, mid-way through dragging a dry plastic paddle brush down through the length of her own hair with one hand while the other presses the crown flat. Under that force: her brush arm pulled hard down past her shoulder, her head tipped away from the pull, the pressing elbow lifted high across her chest. Face: brow drawn in, mouth pressed shut, eyes down on the hair in her hand.

The hair is the evidence. Fine strands stand straight out from her head in a halo, several cling flat to her cheek and jaw, more lift off the brush and follow it as it leaves the hair, and the crown springs back up the instant her hand comes away.

One specific place: a small family bathroom on a weekday morning, and the lived-in clutter of the routine it disrupts — a child's toothbrush in a beaker, a dropped hair tie on the basin edge, an open cosmetics bag, a towel half off its rail.

She is unaware of the camera. Key light: thin cold daylight through a frosted window. Fill: the room's own weak ambient. A rim of light along her lifted forearm. Deep shadow across the lower third of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### hero.image · option B — `01-pain-scene` `--confront`

- varies on: axis: gaze=confront
- ratio `16:9` · type version `1.14` · `gaze: confront`
- The same argument in the type's other gaze, at the desk minutes before a call. The advertorial hero cell holds one type and the gates leave no second, so the honest variation is the axis.
- **note:** --confront is the type's appearance and self-image branch. This page's problem sits on that line rather than clearly one side of it, which is the reason to offer B and the reason not to recommend it.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A woman in her mid-thirties in a work blouse, sitting at a kitchen table in front of an open laptop a few minutes before a call, turned away from the screen towards the camera with both hands still raised at the sides of her head where she has been trying to smooth her hair down. Under that force: both elbows up and out, fingers spread flat against the hair, shoulders lifted. Face: brow raised and tight, mouth slightly open, looking directly into the lens and holding it.

Fine strands stand out from her head in a halo through and above her fingers, several cling flat across her forehead, and the hair she has just pressed down is already lifting again.

One specific place: a kitchen table set up as a workspace on a weekday morning, and the lived-in clutter of the routine it disrupts — a cold mug beside the laptop, a cereal bowl not cleared, a child's school bag on the next chair, a phone face down on a notebook.

Key light: even flat daylight from the kitchen window, bright and unflattering, minimal shadow. Fill: the room's own ambient.

Desaturated throughout, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

### hero.image · option C — `01-pain-scene` `--candid`

- varies on: execution: the second persona — the child's hair, not her own
- ratio `16:9` · type version `1.14` · `gaze: candid`
- Same type and same axis, the other moment the intro names: the hallway detangle before school. Two people in frame and the evidence is the knot held in the brush.

```
A cinematic film still, editorial photojournalism, natural and unstaged.

A woman in her mid-thirties in a dressing gown, crouched on a hallway floor behind a seated girl of about six, mid-way through working a dry plastic brush down through a knot in the child's fine hair with one hand while the other holds the hair above the knot to take the pull. Under that force: the mother's holding hand clenched close to the scalp, her brush arm braced and moving in short strokes, the child's head pulled back against the tension and her shoulders hunched up. Face: the mother's jaw set and eyes fixed on the knot; the child's eyes screwed shut, mouth open.

The knot is the evidence: a dense matted clump held tight in the brush's bristles halfway down, loose broken strands caught across the brush face, and more fine hairs standing out from the child's crown in a halo.

One specific place: a narrow hallway by the front door on a school morning, and the lived-in clutter of the routine it disrupts — a school bag half packed, one shoe on its side, a lunch box on the floor, coats overloading a hook.

Neither is aware of the camera. Key light: thin cold daylight through the glass of the front door. Fill: the dim of the hallway. A rim of light along the child's crown. Deep shadow across the near side of the frame.

Desaturated blue-grey, crushed blacks, fine film grain, shallow depth of field, 35mm.

No product, no panels and no insets. No mark of any kind.
```

## `reason.0.image` — mechanism

- asset `97-02-reason0-mechanism-xray.png` · reason 1 card, the Editor's Pick
- recommended: **option A** · media **still**
- FIT decides, and the gate that usually kills this type does not fire. 03-mechanism-xray asks for a gadget whose real internal components explain why it works, and its avoid_when bars a trivial interior — a shell with nothing meaningful inside. This comb holds a reservoir, an ultrasonic atomiser plate, a six-LED array, a vibration motor and a battery, which is the opposite of trivial, and the positioning is explicitly technical rather than natural or organic. 03-mechanism-ghostbody is the other type in the cell and is NOT offered: its use_when asks for a mechanism inside the BODY that cannot be filmed, and this mechanism is inside the device. B argues the same thing photographically instead, which G8 then governs. C is the same render from above. PRODUCT PRESENCE: the product is the whole frame. PROMPT RISK: 1538 characters.

### reason.0.image · option A — `03-mechanism-xray`

- varies on: baseline
- ratio `1:1` · type version `1.3` · upload the product photo
- The comb opened up along its own length: reservoir, atomiser plate, LED row, battery. The atomiser is the working part and glows cyan as the brightest thing in frame; the mist is the output mark, made of the water itself.
- **note:** G3 COLLISION, resolved in the prompt: the six red LEDs are real components but red is the signal colour for a wrong state, and `output` allows exactly one emission. They are drawn solid and unlit so the mist stays the only thing leaving the product.

```
A premium technical see-through product visualization, sharp and high detail. Not photography.

The attached photo is the exact reference for the product.

A plain deep charcoal ground and nothing else on it.

The reference comb is seen from the side at a slight three-quarter angle with the bristle bed toward the camera, filling about three quarters of the frame, its outer shell rendered translucent and glass-like. The silhouette, the proportions and every visible external part match the reference exactly.

Inside the shell, rendered solid and detailed: the water reservoir low in the handle, the ultrasonic atomiser plate seated at the top of that reservoir where the handle meets the head, a row of six small LEDs set into the underside of the bristle bed, and the cylindrical battery cell filling the lower handle. Fine wiring runs from the battery up to the atomiser and along to the LED row. No component types beyond these.

The atomiser plate is the working part and is shown active: it glows cyan, cleaner and brighter than any reflection elsewhere in the render, and it is the brightest thing in the frame.

An ultra-fine white mist leaves the bristle bed in a soft even cloud and drifts away from the comb toward the upper right of the frame, made of the water itself and lit so it reads clearly against the ground.

The six LEDs are drawn as solid components and are not lit.

One product, one shell, no exploded parts, no callout lines, no labels, and no digits, specifications or text of any kind anywhere in the image.
```

### reason.0.image · option B — `06-relief-hero` `--detail`

- varies on: type: the mechanism argued photographically
- ratio `1:1` · type version `1.15` · upload the product photo · `register: commercial`, `inset_mode: detail`, `inset_motion: still`
- Step 4 rung 2, an adjacent step. The mist carries the argument as a real substance in a real room rather than as a render, with the tank window and the bubble trail in a detail panel. G8 binds hard here and the prompt frames, lights and exposes for the mist.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her mid-thirties in a plain jumper, standing at a bedroom window in the morning drawing the reference comb slowly down through the length of her own hair, her gaze on the hair rather than on the comb. She stands to the right of the frame.

The mist is the subject of the photograph. An ultra-fine white cloud leaves the bristle bed and hangs in the air through the hair, backlit hard by the window so it glows against the darker side of the room, filling a wide band of the frame. Accept lens flare and blown highlights where the window edge cuts in.

One real bedroom filled to the edges with things that genuinely belong there: an unmade bed behind her, a chair with clothes over it, a mug on the sill, a plant, a mirror leaning against the wall, a basket of laundry. Background blurred, but no bare wall area larger than the product. None of those objects carries printed text.

In the upper left of the frame, occupying the space she is offset from, sits a small rounded-rectangle panel with a thin white border showing one magnified detail the scene cannot carry at this distance: the comb's water tank window, half full, with the fine bubble trail rising from the atomiser plate below it. The panel is a clean technical render and does not bleed into the photograph. It is linked to the comb in the scene by proximity alone, with no arrow and no glow border.

No other mark anywhere in the frame.
```

### reason.0.image · option C — `03-mechanism-xray`

- varies on: execution: seen from above through the bristle bed
- ratio `1:1` · type version `1.3` · upload the product photo
- Same type and same marks, a different orientation and a different internal set — the vibration motor in place of the wiring run, and the mist rising through the teeth toward the camera rather than drifting off to one side.
- **note:** Same G3 collision and the same resolution as option A.

```
A premium technical see-through product visualization, sharp and high detail. Not photography.

The attached photo is the exact reference for the product.

A plain deep slate ground and nothing else on it.

The reference comb is seen from directly above with the bristle bed square to the camera, filling about four fifths of the frame, its outer shell rendered translucent and glass-like. The silhouette, the proportions and every visible external part match the reference exactly.

Inside the shell, rendered solid and detailed: the ultrasonic atomiser plate at the head end of the water reservoir, the reservoir running back down the handle behind it, the row of six small LEDs set into the underside of the bristle bed between the teeth, and the vibration motor low in the handle. Fine wiring links the motor and the atomiser. No component types beyond these.

The atomiser plate is the working part and is shown active: it glows cyan, cleaner and brighter than any reflection elsewhere in the render, and it is the brightest thing in the frame.

An ultra-fine white mist rises from between the teeth of the bristle bed in a soft even sheet straight toward the camera, made of the water itself and lit so it reads clearly against the ground.

The six LEDs are drawn as solid components and are not lit.

One product, one shell, no exploded parts, no callout lines, no labels, and no digits, specifications or text of any kind anywhere in the image.
```

## `reason.1.image` — comparison

- asset `97-03-reason1-proof-brushes.png` · reason 2 card
- recommended: **option A** · media **gif**
- One option by law (ADR-022): the five reason cards are the unit of variation, not the card, and this one's place in the set is its varies_on line. The set is served by one type under cross-slot rule 2, which permits a repeating section to repeat a type provided the instances differ on a named dimension — the runbook's own worked precedent is a listicle whose ranked entries each indict one alternative, which is exactly this page. 04-proof-lockedframe is the advertorial comparison cell and its core condition holds on every entry: the difference is visible to the naked eye inside a static frame. CAPABILITY: `strict` needs compositing, so the panels run `handheld` with --verdict included (ADR-021).

### reason.1.image · option A — `04-proof-lockedframe` `--verdict`

- varies on: the culprit is a plastic bristle brush · the hair carries the static halo
- ratio `1:1` · type version `1.13` · upload the product photo
- The first entry in the set and the one the page's headline claim rests on. Two ordinary brushes against the comb, judged on the same length of hair from the same height.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different mornings. One framing for every panel: the same length of hair laid across the same pale bathroom shelf, photographed from directly above from about forty centimetres back, the hair running corner to corner and the shelf edge along the bottom of the frame. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiled wall behind it and the same length of hair in all three panels — the same shade, the same thickness, the same cut ends. Deliberate real-world clutter: a water ring on the shelf, a dropped hair tie, a chip in the tile grout.

The only thing that changes is what was drawn through the hair one minute before the photograph, and each tool lies beside the hair in its own panel so it can be told apart. Panel one: a plain unbranded plastic paddle brush, and the hair lifts away from the shelf in a halo of separated strands, several standing almost upright. Panel two: a plain unbranded fine-tooth plastic comb, and the hair lies flatter but throws a fan of fine hairs up off the surface along its whole length. Panel three: the reference comb, and the hair lies down along the shelf in one settled length with no strand standing off it.

All three tools are ordinary, clean and in good condition, and all three panels get exactly the same exposure, the same background tidiness and the same framing generosity. Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind.
```

### reason.1.image · the motion brief — `proof`

- form `whole-frame` · rung `re-execution` · reference folder: gifs-library/proof/ — no files filed yet; the folder card carries the law
- plate `plates/97-03-reason1-proof-brushes--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
97-03-proof-reason1.mp4
3s · 1:1 · seamless loop · mp4/webm, muted, under the size ceiling

A shot of one length of hair lying on a bathroom shelf, standing up in a halo of separated strands after a plastic brush. The reference comb passes down it once and the halo drops, strand by strand, until the whole length is lying settled and flat along the shelf.

IF THAT CANNOT BE SHOT
A shot of a woman's own hair at the side of her head, fine strands standing out from the crown. The comb passes down through them once and they fall back against the rest of the hair and stay there, with no hand smoothing them down afterwards.
```

## `reason.2.image` — comparison

- asset `97-04-reason2-proof-oils.png` · reason 3 card
- recommended: **option A** · media **still**
- One option by law (ADR-022): the five reason cards are the unit of variation, not the card, and this one's place in the set is its varies_on line. The set is served by one type under cross-slot rule 2, which permits a repeating section to repeat a type provided the instances differ on a named dimension — the runbook's own worked precedent is a listicle whose ranked entries each indict one alternative, which is exactly this page. 04-proof-lockedframe is the advertorial comparison cell and its core condition holds on every entry: the difference is visible to the naked eye inside a static frame. CAPABILITY: `strict` needs compositing, so the panels run `handheld` with --verdict included (ADR-021).

### reason.2.image · option A — `04-proof-lockedframe` `--verdict`

- varies on: the culprit is silicone serum and hair oil · the hair carries the weight
- ratio `1:1` · type version `1.13` · upload the product photo
- Same framing, same hair, and the variable moves from a tool to a treatment. The difference the copy claims — flat and greasy against light and separate — is visible on the strands themselves.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different mornings. One framing for every panel: the same length of hair laid across the same pale bathroom shelf, photographed from directly above from about forty centimetres back, the hair running corner to corner and the shelf edge along the bottom of the frame. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiled wall behind it and the same length of hair in all three panels — the same shade, the same thickness, the same cut ends. Deliberate real-world clutter: a water ring on the shelf, a dropped hair tie, a chip in the tile grout.

The only thing that changes is what was drawn through the hair one minute before the photograph, and each tool lies beside the hair in its own panel so it can be told apart. Panel one: a plain unbranded bottle of silicone smoothing serum, and the hair lies flat and heavy in slick clumped ribbons that stick to each other. Panel two: a plain unbranded bottle of hair oil, and the hair lies flat and darkened, the strands welded into two or three thick locks. Panel three: the reference comb, and the hair lies down in one settled length with the strands still separate and matte.

All three tools are ordinary, clean and in good condition, and all three panels get exactly the same exposure, the same background tidiness and the same framing generosity. Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind.
```

## `reason.3.image` — comparison

- asset `97-05-reason3-proof-spray.png` · reason 4 card
- recommended: **option A** · media **still**
- One option by law (ADR-022): the five reason cards are the unit of variation, not the card, and this one's place in the set is its varies_on line. The set is served by one type under cross-slot rule 2, which permits a repeating section to repeat a type provided the instances differ on a named dimension — the runbook's own worked precedent is a listicle whose ranked entries each indict one alternative, which is exactly this page. 04-proof-lockedframe is the advertorial comparison cell and its core condition holds on every entry: the difference is visible to the naked eye inside a static frame. CAPABILITY: `strict` needs compositing, so the panels run `handheld` with --verdict included (ADR-021).

### reason.3.image · option A — `04-proof-lockedframe` `--verdict`

- varies on: the culprit is a trigger spray bottle · the hair carries the wet patches
- ratio `1:1` · type version `1.13` · upload the product photo
- The one entry where the difference is a distribution rather than a state: soaked patches with dry hair between them against an even matte length.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different mornings. One framing for every panel: the same length of hair laid across the same pale bathroom shelf, photographed from directly above from about forty centimetres back, the hair running corner to corner and the shelf edge along the bottom of the frame. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiled wall behind it and the same length of hair in all three panels — the same shade, the same thickness, the same cut ends. Deliberate real-world clutter: a water ring on the shelf, a dropped hair tie, a chip in the tile grout.

The only thing that changes is what was drawn through the hair one minute before the photograph, and each tool lies beside the hair in its own panel so it can be told apart. Panel one: a plain unbranded trigger spray bottle, and the hair carries two dark soaked patches with pale bone-dry hair between them. Panel two: a plain unbranded fine-mist travel atomiser, and the hair carries one broad damp band across the middle and dry ends beyond it. Panel three: the reference comb, and the hair reads evenly matte from root end to tip with no dark patch anywhere.

All three tools are ordinary, clean and in good condition, and all three panels get exactly the same exposure, the same background tidiness and the same framing generosity. Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind.
```

## `reason.4.image` — comparison

- asset `97-06-reason4-proof-heat.png` · reason 5 card
- recommended: **option A** · media **still**
- One option by law (ADR-022): the five reason cards are the unit of variation, not the card, and this one's place in the set is its varies_on line. The set is served by one type under cross-slot rule 2, which permits a repeating section to repeat a type provided the instances differ on a named dimension — the runbook's own worked precedent is a listicle whose ranked entries each indict one alternative, which is exactly this page. 04-proof-lockedframe is the advertorial comparison cell and its core condition holds on every entry: the difference is visible to the naked eye inside a static frame. CAPABILITY: `strict` needs compositing, so the panels run `handheld` with --verdict included (ADR-021).

### reason.4.image · option A — `04-proof-lockedframe` `--verdict`

- varies on: the culprit is heat · the hair carries the damage
- ratio `1:1` · type version `1.13` · upload the product photo
- Cumulative heat damage is the one culprit on this page whose harm PERSISTS after it is taken away, which is why 02-cause-anatomy is not used anywhere in this set — its avoid_when bars exactly that, naming a lifted hair cuticle as the example. A locked frame does not claim a repair; it shows three ends and lets the reader judge.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different mornings. One framing for every panel: the same length of hair laid across the same pale bathroom shelf, photographed from directly above from about forty centimetres back, the hair running corner to corner and the shelf edge along the bottom of the frame. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiled wall behind it and the same length of hair in all three panels — the same shade, the same thickness, the same cut ends. Deliberate real-world clutter: a water ring on the shelf, a dropped hair tie, a chip in the tile grout.

The only thing that changes is what was drawn through the hair one minute before the photograph, and each tool lies beside the hair in its own panel so it can be told apart. Panel one: a plain unbranded heated straightening brush, and the hair shows split and whitened ends and a dry crimped texture along the last third. Panel two: a plain unbranded flat iron, and the hair shows the same whitened ends and a glassy scorched sheen through the middle. Panel three: the reference comb, and the hair shows cut ends that are still square and a texture that is even end to end.

All three tools are ordinary, clean and in good condition, and all three panels get exactly the same exposure, the same background tidiness and the same framing generosity. Light differs only in exposure between panels, never in warmth. One neutral grade across every panel, no panel warmer, brighter or more saturated than another.

No people, no hands, no badges, no arrows and no text of any kind.
```

## `reason.5.image` — comparison

- asset `97-07-reason5-proof-hygiene.png` · reason 6 card
- recommended: **option A** · media **gif**
- One option by law (ADR-022): the five reason cards are the unit of variation, not the card, and this one's place in the set is its varies_on line. The set is served by one type under cross-slot rule 2, which permits a repeating section to repeat a type provided the instances differ on a named dimension — the runbook's own worked precedent is a listicle whose ranked entries each indict one alternative, which is exactly this page. 04-proof-lockedframe is the advertorial comparison cell and its core condition holds on every entry: the difference is visible to the naked eye inside a static frame. CAPABILITY: `strict` needs compositing, so the panels run `handheld` with --verdict included (ADR-021).

### reason.5.image · option A — `04-proof-lockedframe` `--verdict`

- varies on: the culprit is a fixed bristle bed · the brush itself carries the residue
- ratio `1:1` · type version `1.13` · upload the product photo
- The last entry changes what is being photographed: the brush rather than the hair, because the argument is about the tool's own state. Same shelf, same light, same three weeks of use on all three.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different mornings. One framing for every panel: the bristle bed of one brush photographed from directly above from about twenty-five centimetres back on the same pale bathroom shelf, the bed filling most of the frame and the shelf edge along the bottom. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiled wall and the same light in all three panels, with deliberate real-world clutter: a water ring on the shelf, a dropped hair tie, a chip in the tile grout.

The only thing that changes is which brush is being looked at, and every one has had the same three weeks of ordinary use. Panel one: a plain unbranded plastic paddle brush, its fixed bristles matted down at the base with a grey felt of shed hair, dust and dulled product residue packed between the rows. Panel two: a plain unbranded round brush, the same grey felt wound tight round the barrel between the bristles. Panel three: the reference comb with its teeth retracted flush into the cushion, the whole three weeks of shed hair lifted clear of the bed in one loose mat sitting on top of it, the cushion beneath it clean.

All three are ordinary and undamaged, and all three panels get exactly the same exposure, the same background tidiness and the same framing generosity. One neutral grade across every panel.

No people, no hands, no badges, no arrows and no text of any kind.
```

### reason.5.image · the motion brief — `mechanism`

- form `whole-frame` · rung `re-execution` · reference folder: gifs-library/mechanism/ — no files filed yet; the folder card carries the law
- plate `plates/97-07-reason5-proof-hygiene--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
97-07-mechanism-reason5.mp4
3s · 1:1 · seamless loop · mp4/webm, muted, under the size ceiling

A shot of the comb's bristle bed close up on a bathroom shelf, three weeks of shed hair and dust packed down between the teeth. A thumb presses the button on the handle, the teeth retract flush into the cushion, and the whole mat lifts clear in one piece.

IF THAT CANNOT BE SHOT
A shot of the same bristle bed held over an open bin. The teeth retract flush into the cushion, the packed mat of hair and dust comes away as one, and it drops into the bin leaving a clean cushion behind.
```

## `howto.image` — how-to-use

- asset `97-08-howto-use-sequence.png` · the how-to card, beside the three numbered steps
- recommended: **option A** · media **gif**
- FIT decides and the gate opens. 03-use-sequence is the advertorial how-to-use cell and multi_step_usage is true — the page states three steps in its own copy, fill, activate, glide. A runs them as three stacked panels with one pair of hands, and carries the type's `fill` mark on the tank window in all three panels, which is what makes three photographs one event. B argues the same thing as a single scene with a detail panel, which is rung 2 and loses the sequence. C is the same sequence on the child, which is the page's second persona, and swaps `emission` for `trace`. EVIDENCE: `emission` renders 7 of 7 in this type and `fill` about 6 with no failure attributed to it. PROMPT RISK: 1111 characters against this type's hard ceiling of about 1500 — the type has measured that a longer prompt is paid for out of the layout, 4 of 6 stacks holding at 1533 characters and 1 of 8 at 2054.

### howto.image · option A — `03-use-sequence`

- varies on: baseline
- ratio `1:1` · type version `1.9` · upload the product photo · `camera_lock: handheld`
- The three steps the copy states, one action per panel: water into the port, the comb drawn through the hair with the mist visible, the comb set down and the hair smoothed. The tank window is named in every panel so the level reads as one event.

```
Three photographs stacked one above another, filling the whole image, thin white gutters, no outer border, and no panel other than those three. A real home photographed plainly at close range on available light.

The attached photo is the exact reference for the product, in every panel.

The same hands throughout: one adult woman's hands, same skin tone, same short unpainted nails, same wrists, sleeves pushed back. The same bathroom shelf and the same cool window light from the left in all three panels.

Top panel: the comb held over the basin, its water tank window empty and pale, the other hand tipping a small jug of clear water into the open filler port.

Middle panel: the same hands drawing the comb down through the length of her own hair, the tank window now half full of water, and an ultra-fine white mist visibly leaving the bristle bed into the hair, lit so it can be seen.

Bottom panel: the comb set down on the shelf, its tank window still half full, and her free hand running flat down the smoothed hair from crown to tips.

No numbers, no step markers, no arrows and no text of any kind.
```

### howto.image · option B — `06-relief-hero` `--detail`

- varies on: type: one scene with a detail panel instead of a sequence
- ratio `1:1` · type version `1.15` · upload the product photo · `register: commercial`, `inset_mode: detail`, `inset_motion: still`
- Step 4 rung 2. It buys a mist that carries the frame under G8 and a legible tank window, and it pays for them with the sequence — a reader learns that it is used, not how.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her mid-thirties in a plain top, standing at a bathroom basin in the morning drawing the reference comb down through her hair in one unhurried pass, her gaze on the hair. She stands to the right of the frame.

The mist is the subject of the photograph. An ultra-fine white cloud leaves the bristle bed and hangs through the hair, side-lit hard from the window so it glows against the darker tiled wall behind her, filling a wide band of the frame.

One real family bathroom filled to the edges with things that genuinely belong there: a child's toothbrush in a beaker, an open cosmetics bag, a towel over the rail, a plant on the cistern, a basket of flannels. Background blurred, but no bare wall area larger than the product. None of those objects carries printed text.

In the upper left of the frame, occupying the space she is offset from, sits a small rounded-rectangle panel with a thin white border showing one magnified detail the scene cannot carry at this distance: the comb's filler port open with a jug tipping clear water into it, and the tank window below reading half full. The panel is a clean technical render and does not bleed into the photograph, linked to the comb in the scene by proximity alone with no arrow and no glow border.

No other mark anywhere in the frame.
```

### howto.image · option C — `03-use-sequence`

- varies on: execution: the child's hair, and `trace` in place of `emission`
- ratio `1:1` · type version `1.9` · upload the product photo · `camera_lock: handheld`
- Same type and same three beats on the page's second persona. The middle panel carries the boundary instead of the mist — smooth behind the teeth, lifted and tangled ahead of them — which is the cheapest proof in the library and needs nothing lit to be visible.

```
Three photographs stacked one above another, filling the whole image, thin white gutters, no outer border, and no panel other than those three. A real home photographed plainly at close range on available light.

The attached photo is the exact reference for the product, in every panel.

The same hands throughout: one adult woman's hands, same skin tone, same short unpainted nails, same wrists, sleeves pushed back. The same child's bedroom floor and the same warm overhead light in all three panels.

Top panel: the comb held over a low chest of drawers, its water tank window empty and pale, the other hand thumbing the power switch on the handle.

Middle panel: the same hands drawing the comb down through the back of a seated child's fine hair, the tank window now half full, and the hair sitting smooth and flat behind the comb's teeth while it still stands lifted and tangled ahead of them.

Bottom panel: the comb set down on the drawers, its tank window still half full, and her free hand gathering the finished hair into one loose length behind the child's shoulder.

No numbers, no step markers, no arrows and no text of any kind.
```

### howto.image · the motion brief — `use`

- form `whole-frame` · rung `natural` · reference folder: gifs-library/use/ — one file filed, w1000.gif, unledgered; the folder card carries the law
- plate `plates/97-08-howto-use-sequence--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
97-08-use-howto.mp4
4s · 1:1 · seamless loop · mp4/webm, muted, under the size ceiling

A shot of two hands at a bathroom shelf with the comb, its tank window empty. Water goes into the filler port until the window reads half full, a thumb presses the switch, and the comb draws down through the length of her hair with the mist leaving the bristle bed.

IF THAT CANNOT BE SHOT
A shot of the same hands and the same shelf, the comb already filled and running. It draws down through her hair three times over, and behind each pass the hair lies smooth and settled while it still stands lifted ahead of the teeth.
```

## `social.photos.0.image` — social-proof

- asset `97-09-social-1.png` · social grid tile 1 of 6
- recommended: **option A** · media **still**
- One option by law (ADR-022): the six tiles are the unit of variation, not the tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home, which is what this block claims. The SET DIVERSITY LAW is satisfied across the six: six room classes, six surfaces, six light temperatures, six camera distances and all three content modes.

### social.photos.0.image · option A — `05-social-snapshot`

- varies on: in-use · family bathroom · basin shelf · cool frosted daylight · seated arm's length
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the six-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the same social block as six named comments carrying Verified labels and timestamps. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and Verified labels — before rendering any of these. This is the fourth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use, photographed by its owner: the reference comb held against the length of her own hair, only her forearm and two fingers in shot and no face.

An ordinary family bathroom photographed exactly as found on a weekday morning — the mess stays, nothing tidied, nothing added for the picture. Cool daylight through a frosted window, no other light.

One incidental owner object and no more: a child's toothbrush standing in a beaker.

Framing slightly tilted and taken at arm's length from the basin; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `social.photos.1.image` — social-proof

- asset `97-10-social-2.png` · social grid tile 2 of 6
- recommended: **option A** · media **still**
- One option by law (ADR-022): the six tiles are the unit of variation, not the tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home, which is what this block claims. The SET DIVERSITY LAW is satisfied across the six: six room classes, six surfaces, six light temperatures, six camera distances and all three content modes.

### social.photos.1.image · option A — `05-social-snapshot`

- varies on: at-rest · bedroom · painted nightstand · warm bedside lamp · standing above
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the six-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the same social block as six named comments carrying Verified labels and timestamps. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and Verified labels — before rendering any of these. This is the fourth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product simply sitting where it now lives: the reference comb on a bedroom nightstand, nobody in the picture at all.

An ordinary bedroom photographed exactly as found in the evening — the mess stays, nothing tidied, nothing added for the picture. Warm yellow light from one bedside lamp, no other light.

One incidental owner object and no more: a phone charging cable coiled beside it.

Framing off-centre and taken from standing height looking down; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `social.photos.2.image` — social-proof

- asset `97-11-social-3.png` · social grid tile 3 of 6
- recommended: **option A** · media **still**
- One option by law (ADR-022): the six tiles are the unit of variation, not the tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home, which is what this block claims. The SET DIVERSITY LAW is satisfied across the six: six room classes, six surfaces, six light temperatures, six camera distances and all three content modes.

### social.photos.2.image · option A — `05-social-snapshot`

- varies on: in-use · child's bedroom · carpet floor · flat overcast daylight · close from floor level
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the six-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the same social block as six named comments carrying Verified labels and timestamps. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and Verified labels — before rendering any of these. This is the fourth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use, photographed over the owner's own shoulder: the reference comb drawn through a seated child's hair, two fingers and a wrist in shot and no face.

An ordinary child's bedroom floor photographed exactly as found on a grey afternoon — the mess stays, nothing tidied, nothing added for the picture. Flat overcast daylight through the window, no other light.

One incidental owner object and no more: a soft toy dropped on its side nearby.

Framing close and crooked, taken from very near the floor; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `social.photos.3.image` — social-proof

- asset `97-12-social-4.png` · social grid tile 4 of 6
- recommended: **option A** · media **still**
- One option by law (ADR-022): the six tiles are the unit of variation, not the tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home, which is what this block claims. The SET DIVERSITY LAW is satisfied across the six: six room classes, six surfaces, six light temperatures, six camera distances and all three content modes.

### social.photos.3.image · option A — `05-social-snapshot`

- varies on: kit-flatlay · kitchen · stone worktop · mixed warm and cool · half a metre back
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the six-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the same social block as six named comments carrying Verified labels and timestamps. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and Verified labels — before rendering any of these. This is the fourth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The opened box and its contents as the owner has just left them: the reference comb out of its packaging on a kitchen worktop with the charging cable and the flattened box pushed to one side. Nobody in the picture at all.

An ordinary kitchen photographed exactly as found in the middle of the day — the mess stays, nothing tidied, nothing added for the picture. Mixed light, warm ceiling spots over cool daylight from the window, no other light.

One incidental owner object and no more: a fruit bowl at the edge of the worktop.

Framing slightly tilted and taken from standing height about half a metre back; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `social.photos.4.image` — social-proof

- asset `97-13-social-5.png` · social grid tile 5 of 6
- recommended: **option A** · media **still**
- One option by law (ADR-022): the six tiles are the unit of variation, not the tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home, which is what this block claims. The SET DIVERSITY LAW is satisfied across the six: six room classes, six surfaces, six light temperatures, six camera distances and all three content modes.

### social.photos.4.image · option A — `05-social-snapshot`

- varies on: at-rest · hallway · wooden hall table · warm hallway overhead · close from one side
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the six-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the same social block as six named comments carrying Verified labels and timestamps. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and Verified labels — before rendering any of these. This is the fourth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product simply sitting where it now lives: the reference comb lying on a hall table beside an open handbag it has clearly just come out of, nobody in the picture.

An ordinary hallway photographed exactly as found on the way out — the mess stays, nothing tidied, nothing added for the picture. Warm hallway light from a single overhead fitting, no other light.

One incidental owner object and no more: a set of keys dropped beside the bag.

Framing close and taken from one side at chest height; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `social.photos.5.image` — social-proof

- asset `97-14-social-6.png` · social grid tile 6 of 6
- recommended: **option A** · media **still**
- One option by law (ADR-022): the six tiles are the unit of variation, not the tile. 05-social-snapshot is the advertorial social-proof type whose trust gap is whether the thing exists and works in a normal home, which is what this block claims. The SET DIVERSITY LAW is satisfied across the six: six room classes, six surfaces, six light temperatures, six camera distances and all three content modes.

### social.photos.5.image · option A — `05-social-snapshot`

- varies on: in-use · home office · laminate desk · cool window and monitor wash · arm's length across
- ratio `1:1` · type version `1.2` · upload the product photo · `register: ugc`
- One tile of the six-tile set, differing from its siblings on room class, surface, light temperature, camera distance and content mode.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the same social block as six named comments carrying Verified labels and timestamps. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names and Verified labels — before rendering any of these. This is the fourth routed page in a row to breach it, so it is a template defect rather than a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use, photographed by its owner at a desk: the reference comb held up at the side of her head, one forearm and the edge of a shoulder in shot and no face.

An ordinary home office desk photographed exactly as found before a call — the mess stays, nothing tidied, nothing added for the picture. Cool daylight from a window on one side and the pale wash of a monitor on the other, no other light.

One incidental owner object and no more: a pair of over-ear headphones pushed to the back of the desk.

Framing a little too close and taken at arm's length across the desk; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `outcome.image` — outcome  ·  PROPOSAL, not a slot the page declares

- asset `97-15-outcome-relief-hero.png` · Between the how-to card and the offer band, as a full-width card closing the seven reasons before the price appears.
- recommended: **option A** · media **still**
- earns its place: Step 6 relief is absent and the awareness stage says it matters. A problem-aware reader arrives knowing the frizz and not the tool class; the page spends seven cards on what is wrong and what the device contains, and never once shows the resolved morning it is selling. Every other rung is covered, so this is the only gap on the ladder and it is at the end of it.
- 06-relief-hero is the advertorial outcome cell alongside 06-relief-scene, and 06-relief-scene is not offered because it does not declare 1:1 — every slot on this page below the hero is square. 06-relief-hero declares 1:1 and 16:9, so it fits either way. G8 binds: the mist is the primary subject and the frame is lit for it. It is additive and additive only — nothing in the routed set depends on it, and the page ships legal without it.

### outcome.image · option A — `06-relief-hero` `--detail`

- varies on: baseline
- ratio `1:1` · type version `1.15` · upload the product photo · `register: commercial`, `inset_mode: detail`, `inset_motion: still`
- The same execution offered as option B at reason.0, moved to the slot its type is actually for. If both are taken, change one of them: the same image in two places is the fault one-type-once exists to prevent.
- **note:** COMBINATION: this shares a prompt with reason.0 option B. Take one or the other, or re-execute this one on the second persona.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her mid-thirties in a plain jumper, standing at a bedroom window in the morning drawing the reference comb slowly down through the length of her own hair, her gaze on the hair rather than on the comb. She stands to the right of the frame.

The mist is the subject of the photograph. An ultra-fine white cloud leaves the bristle bed and hangs in the air through the hair, backlit hard by the window so it glows against the darker side of the room, filling a wide band of the frame. Accept lens flare and blown highlights where the window edge cuts in.

One real bedroom filled to the edges with things that genuinely belong there: an unmade bed behind her, a chair with clothes over it, a mug on the sill, a plant, a mirror leaning against the wall, a basket of laundry. Background blurred, but no bare wall area larger than the product. None of those objects carries printed text.

In the upper left of the frame, occupying the space she is offset from, sits a small rounded-rectangle panel with a thin white border showing one magnified detail the scene cannot carry at this distance: the comb's water tank window, half full, with the fine bubble trail rising from the atomiser plate below it. The panel is a clean technical render and does not bleed into the photograph. It is linked to the comb in the scene by proximity alone, with no arrow and no glow border.

No other mark anywhere in the frame.
```

## Motion reserves

Slots that earned motion and lost to the spacing rule. Each replaces the loop it names — it is never added alongside it. Promote one by editing `build.py` and re-running `scripts/gen-plate.py`.

### `reason.0.image` — `mechanism`, replaces `reason.1.image`

- Adjacent to reason.1, which carries the stronger loop. Promoting it leaves loops at reason.0 and reason.5, five items apart, so the spacing rule still holds.

```
A shot of the comb's water tank window and the bristle bed beside it, close enough to fill the frame. Fine bubbles rise off the atomiser plate behind the window and an ultra-fine mist builds and lifts away from between the teeth in a steady soft cloud.
```

### `reason.3.image` — `cause`, replaces `reason.5.image`

- Earned motion on its own argument and lost to the two-loop cap. Promoting it leaves loops at reason.1 and reason.3, two items apart, so the spacing rule still holds.

```
A shot of one length of hair on a bathroom shelf with a trigger spray bottle beside it. The bottle fires and heavy droplets land in two dark soaked patches with dry pale hair left between them, and the patches spread and darken further as they soak in.
```

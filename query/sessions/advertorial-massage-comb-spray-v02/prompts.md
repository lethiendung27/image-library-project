# Image prompts — page 125, electric spray air cushion massage comb

GENERATED from `prompts.json` by `build.py`. Never hand-edit this file — edit the script and re-run. Routing rationale, the negative motion verdicts and the out-of-scope slots are all in `prompts.json`.

- page `125` · advertorial · solution-aware · registry `2.0.0` · 14 routed slots · 30 prompts · 3 motion briefs
- motion: 3 loops (3 whole-frame), floor 2, margin 1, groups result, working
- **6 prompts carry a blocking precondition**, stated on each

---

## `hero.image` — hero

- asset `125-01-hero-pain-scene.png` · advertorial header, under the headline and above the byline
- recommended: **option A** · media **still**
- FIT decides, close to verbatim. The headline calls it the morning static trap and hero.intro puts her at the bathroom sink at a quarter to seven with every stroke turning frizz into a cloud of static. 01-pain-scene --candid is written for physical pain in a moment nobody would choose to be seen in, and A plays that as one action. B moves to the confront gaze, which the type reserves for appearance and self-image — and that beat has its own slot at content.items.0, so spending it here would duplicate it. C moves to the hallway mirror on the way out. RATIO: 16:9 declared and 16:9 slot, so nothing is cropped here — the only slot on this page where that is true. PRODUCT PRESENCE: none, correctly; the type forbids it. PROMPT RISK: 1083 characters against this type's measured band of 1669 to 1880.

### hero.image · option A — `01-pain-scene` `--candid`

- varies on: baseline
- ratio `16:9` · type version `1.15` · `gaze: candid`
- The page's opening scene as one action: a dry brush dragged down through her own hair at the sink, the halo standing up behind it. The evidence is the hair itself, which is rank 1 under G9.

```
Editorial photojournalism, natural and unstaged.

A woman in her thirties in a work blouse standing at a bathroom sink early in the morning, mid-way through dragging a dry plastic brush down through the length of her own hair with one hand while the other presses the crown flat. Under that force: her brush arm pulled hard down past her shoulder, her head tipped away from the pull, the pressing elbow lifted high across her chest. Face: brow drawn in, mouth pressed shut, eyes down on the hair in her hand.

The hair is the evidence. Fine strands stand straight out from her head in a halo, several cling flat to her cheek and jaw, more lift off the brush and follow it as it leaves the hair, and the crown springs back up the instant her hand comes away.

One specific place: a family bathroom at a quarter to seven.

She is unaware of the camera. Regular early morning light.

Nothing is arranged for the camera and nothing is tidied. The frame holds her, her hair and the brush, and nothing else competes for attention.

No product, no panels and no insets. No mark of any kind.
```

### hero.image · option B — `01-pain-scene` `--confront`

- varies on: axis: gaze=confront
- ratio `16:9` · type version `1.15` · `gaze: confront`
- The same moment in the type's other gaze, holding the viewer's eye. The advertorial hero cell holds one type and the gates leave no second, so the honest variation here is the axis.
- **note:** Picking B duplicates the gaze recommended at content.items.0, which is where the appearance beat actually lives; that slot would then fall to its own B.

```
Editorial photojournalism, natural and unstaged.

A woman in her thirties in a work blouse standing at a bathroom sink early in the morning, turned away from the mirror towards the camera with both hands still raised at the sides of her head where she has been trying to smooth her hair down. Under that force: both elbows up and out, fingers spread flat against the hair, shoulders lifted. Face: brow raised and tight, mouth slightly open, looking directly into the lens and holding it.

Fine strands stand out from her head in a halo through and above her fingers, several cling flat across her forehead, and the hair she has just pressed down is already lifting again.

One specific place: a family bathroom at a quarter to seven.

Regular early morning light.

Nothing is arranged for the camera and nothing is tidied. The frame holds her, her hair and her hands, and nothing else competes for attention.

No product, no panels and no insets. No mark of any kind.
```

### hero.image · option C — `01-pain-scene` `--candid`

- varies on: execution: the hallway mirror on the way out
- ratio `16:9` · type version `1.15` · `gaze: candid`
- Same type and same axis, moved to the last mirror before the door — the moment the copy's school-run pressure actually bites.

```
Editorial photojournalism, natural and unstaged.

A woman in her thirties already in her coat, stopped at a hallway mirror by the front door on her way out, mid-way through flattening one side of her hair with the palm of her hand while the other hand holds a dry plastic brush down at her side. Under that force: her pressing arm bent hard across her face, her head tilted away from the palm, her shoulder driven up, her weight on the front foot as if she has stopped mid-stride. Face: brow drawn in, lips pressed together, eyes on her own reflection.

The hair is the evidence. Fine strands stand out from the flattened side in a halo the moment the palm lifts, more cling across the collar of her coat, and one section will not lie down at all.

One specific place: a hallway by the front door on a school morning.

She is unaware of the camera. Regular morning light.

Nothing is arranged for the camera and nothing is tidied. The frame holds her, her hair and the mirror, and nothing else competes for attention.

No product, no panels and no insets. No mark of any kind.
```

## `content.items.0.image` — problem-agitation

- asset `125-02-content0-pain-scene.png` · body item 1
- recommended: **option A** · media **still**
- FIT decides and the type's own trigger names it. This section's cost is APPEARANCE — a manager noticing her webcam angle while she keeps smoothing flyaways — and 01-pain-scene reserves --confront for exactly that: appearance, self-image and daily frustration where the mirror moment IS the moment. A is that. B is the same beat played candid, which loses the being-seen half. C moves it to the office lift lobby. PAGE LEGALITY: this is Step 4 rung 4 — 01-pain-scene runs at the hero as well, and the two differ on the gaze AXIS rather than only on staging. PROMPT RISK: 1051 characters.

### content.items.0.image · option A — `01-pain-scene` `--confront`

- varies on: rung 4: same type, gaze axis and beat differ
- ratio `16:9` · type version `1.15` · `gaze: confront`
- The webcam beat: hands still up in her hair a minute before the call, looking straight down the lens the way the camera on the laptop would see her.
- **note:** RATIO: this type declares 16:9 as its only ADR-016-legal ratio and the slot is 1:1, so the layout centre-crops about 44% of the width. The frame is composed for it — the subject sits centred and close, and nothing the argument needs lives in the outer thirds. Every option at this slot has the same cost because the cell holds one type. Rung 4 of Step 4's ladder: another execution of a type already recommended at hero.image, differing on the gaze axis. Declared here rather than left to look like an oversight.

```
Editorial photojournalism, natural and unstaged.

A woman in her thirties in a work blouse sitting at a kitchen table in front of an open laptop a minute before a call, turned away from the screen towards the camera with both hands still raised at the sides of her head where she has been trying to smooth her hair down. Under that force: both elbows up and out, fingers spread flat against the hair, shoulders lifted, her back held forward off the chair. Face: brow raised and tight, mouth slightly open, looking directly into the lens and holding it.

Fine strands stand out from her head in a halo through and above her fingers, several cling flat across her forehead, and the hair she has just pressed down is already lifting again.

One specific place: a kitchen table set up as a workspace on a weekday morning.

Regular morning light.

Nothing is arranged for the camera and nothing is tidied. The frame holds her, her hair and the open laptop, and nothing else competes for attention.

No product, no panels and no insets. No mark of any kind.
```

### content.items.0.image · option B — `01-pain-scene` `--candid`

- varies on: axis: gaze=candid
- ratio `16:9` · type version `1.15` · `gaze: candid`
- The same table and the same minute, played unaware — pressing both sides down while watching the screen rather than the lens.
- **note:** RATIO: this type declares 16:9 as its only ADR-016-legal ratio and the slot is 1:1, so the layout centre-crops about 44% of the width. The frame is composed for it — the subject sits centred and close, and nothing the argument needs lives in the outer thirds. Every option at this slot has the same cost because the cell holds one type.

```
Editorial photojournalism, natural and unstaged.

A woman in her thirties in a work blouse sitting at a kitchen table in front of an open laptop a minute before a call, mid-way through pressing both sides of her hair down with her palms and watching the screen rather than the camera. Under that force: both elbows lifted wide, palms flat against the hair above her ears, her chin tucked towards the laptop, her shoulders drawn up. Face: brow drawn in, mouth pressed shut, eyes fixed on the screen.

The hair is the evidence. Fine strands stand out from the crown in a halo above her hands, several cling flat across her forehead, and the sections she has already pressed are lifting again behind her palms.

One specific place: a kitchen table set up as a workspace on a weekday morning.

She is unaware of the camera. Regular morning light.

Nothing is arranged for the camera and nothing is tidied. The frame holds her, her hair and the open laptop, and nothing else competes for attention.

No product, no panels and no insets. No mark of any kind.
```

### content.items.0.image · option C — `01-pain-scene` `--confront`

- varies on: execution: the office lift lobby, not the kitchen table
- ratio `16:9` · type version `1.15` · `gaze: confront`
- Same type and same axis, moved to where the being-seen actually happens — in the building, bag on the shoulder, before anyone has spoken to her.
- **note:** RATIO: this type declares 16:9 as its only ADR-016-legal ratio and the slot is 1:1, so the layout centre-crops about 44% of the width. The frame is composed for it — the subject sits centred and close, and nothing the argument needs lives in the outer thirds. Every option at this slot has the same cost because the cell holds one type.

```
Editorial photojournalism, natural and unstaged.

A woman in her thirties in a work blouse standing in an office lift lobby, turned towards the camera with one hand still raised where she has been pressing her hair down against the side of her head. Under that force: that elbow up and out, fingers spread flat against the hair, her other hand gripping a laptop bag strap at her shoulder. Face: brow raised and tight, mouth slightly open, looking directly into the lens and holding it.

Fine strands stand out from her head in a halo through and above her fingers, several cling across her collar, and the hair she has just pressed down is already lifting again.

One specific place: an office lift lobby first thing in the morning.

Regular morning light.

Nothing is arranged for the camera and nothing is tidied. The frame holds her, her hair and her raised hand, and nothing else competes for attention.

No product, no panels and no insets. No mark of any kind.
```

## `content.items.1.image` — problem-agitation

- asset `125-03-content1-pain-scene.png` · body item 2
- recommended: **option A** · media **still**
- FIT decides. This is the child pain beat in the page's own words — rigid bristles snagging a crown knot, the bus missed, the daughter on the hallway floor — and 01-pain-scene --candid is the type for physical pain in a moment nobody would choose to be seen in. A is that moment with G13 applied. B is the sanctioned fallback if A is refused: the same beat with nobody in frame, an execution this type already legislates and the ledger records twice. C moves it to a kitchen chair. G13: no private room, no age in years, and the face capped at effort — plus a NEGATIVE beside the cap, which the rule does not yet carry and which 1 of 3 renders needed on 2026-08-24. PAGE LEGALITY: rung 4 again, and the third execution of this type on the page; the subject class here is a child rather than the narrator. PROMPT RISK: 1102 characters.

### content.items.1.image · option A — `01-pain-scene` `--candid`

- varies on: rung 4: same type, child subject class
- ratio `16:9` · type version `1.15` · `gaze: candid`
- The hallway floor, the crown knot, and an adult's brush in it. The knot is the evidence and the child's face carries effort and nothing more.
- **note:** RATIO: this type declares 16:9 as its only ADR-016-legal ratio and the slot is 1:1, so the layout centre-crops about 44% of the width. The frame is composed for it — the subject sits centred and close, and nothing the argument needs lives in the outer thirds. Every option at this slot has the same cost because the cell holds one type. G13 BINDS: hallway rather than a private room, no age in years, and the Face block capped at effort with an explicit negative. The residual is the force inventory and the covert gaze, which the type requires; three renders of this shape generated on 2026-08-24 without refusal.

```
Editorial photojournalism, natural and unstaged.

A school-age girl sitting on the floor of a hallway with her back against the wall, mid-way through an adult working a rigid plastic brush into a knot high at her crown. Under that force: her shoulders drawn up towards her ears, both hands flat on the floor either side of her taking her weight, her head held back against the pull, her knees pulled in. Face: chin down, mouth closed, eyes on the floor in front of her. Her face carries effort and nothing more: no wince, no tears, no open mouth, no crying.

The knot is the evidence: a dense matted clump caught in the brush's teeth at the crown, the hair around it pulled tight into it from three directions, and loose broken strands drifted onto the floor beside her.

One specific place: a hallway by the front door on a school morning.

Neither is aware of the camera. Regular morning light.

Nothing is arranged for the camera and nothing is tidied. The frame holds the two of them and the brush, and nothing else competes for attention.

No product, no panels and no insets. No mark of any kind.
```

### content.items.1.image · option B — `01-pain-scene` `--candid`

- varies on: subject class: object-only, nobody in frame
- ratio `16:9` · type version `1.15` · `gaze: candid`
- The same beat with the brush and the knot still in it on the floor. It carries the argument without a person, and it cannot be refused.
- **note:** RATIO: this type declares 16:9 as its only ADR-016-legal ratio and the slot is 1:1, so the layout centre-crops about 44% of the width. The frame is composed for it — the subject sits centred and close, and nothing the argument needs lives in the outer thirds. Every option at this slot has the same cost because the cell holds one type. THE SANCTIONED FALLBACK if A is refused. Note the argument fault this frame must avoid: a loose ball of shed hair on a brush reads as HAIR LOSS, which is not what this page argues, so the prompt names a matted clump still gripped in the teeth with the surrounding hair twisted into it. Two renders on 2026-08-24 came back reading as shedding.

```
Editorial photojournalism, natural and unstaged.

No person in the frame. The subject is a rigid plastic brush left on the hallway floor where the morning stopped, a dense matted clump of fine hair still gripped in its teeth at one end, the hair around the clump twisted tight into it, and loose broken strands drifted across the floorboards around it.

One specific place: a hallway by the front door on a school morning.

No subject, so no gaze. The frame looks straight down at the brush from standing height. Regular morning light.

Nothing is arranged for the camera and nothing is tidied. The frame holds the brush and the knot still in it, and nothing else competes for attention.

No product, no panels and no insets. No mark of any kind.
```

### content.items.1.image · option C — `01-pain-scene` `--candid`

- varies on: execution: a kitchen chair, not the hallway floor
- ratio `16:9` · type version `1.15` · `gaze: candid`
- Same type and same subject class, moved to the chair the copy puts her in every other morning.
- **note:** RATIO: this type declares 16:9 as its only ADR-016-legal ratio and the slot is 1:1, so the layout centre-crops about 44% of the width. The frame is composed for it — the subject sits centred and close, and nothing the argument needs lives in the outer thirds. Every option at this slot has the same cost because the cell holds one type.

```
Editorial photojournalism, natural and unstaged.

A school-age girl sitting sideways on a kitchen chair with one arm hooked over its back, mid-way through an adult working a rigid plastic brush into a knot high at her crown. Under that force: her free shoulder drawn up, the hooked arm pulling against the chair back, her head held back against the pull, one foot braced on a chair leg. Face: chin down, mouth closed, eyes on the table in front of her. Her face carries effort and nothing more: no wince, no tears, no open mouth, no crying.

The knot is the evidence: a dense matted clump caught in the brush's teeth at the crown, the hair around it pulled tight into it from three directions, and loose broken strands on the table.

One specific place: a kitchen chair on a school morning.

Neither is aware of the camera. Regular morning light.

Nothing is arranged for the camera and nothing is tidied. The frame holds the two of them and the brush, and nothing else competes for attention.

No product, no panels and no insets. No mark of any kind.
```

### content.items.1.image · the motion brief — `cause` (whole-frame)

- form `whole-frame` · rung `natural` · reference folder: gifs-library/cause/ — no files filed yet; the folder card carries the law
- plate `plates/125-03-content1-pain-scene--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
advertorial-cause-massage-comb-spray-v02.webp
3s · 1:1 · seamless loop · animated webp, loop-safe, under the size ceiling

A shot of a rigid brush being drawn down into a knot at the back of a child's head. The teeth catch, the hair around the knot pulls tight and lifts with the brush, and her shoulders come up as it holds.

IF THAT CANNOT BE SHOT
A shot of the same brush pulled slowly through a hank of fine hair held in one hand, no child in the frame. The teeth reach a knot, the strands bunch and tighten into it, and the whole hank travels with the brush.
```

## `content.items.2.image` — comparison

- asset `125-04-content2-proof-lockedframe.png` · body item 3
- recommended: **option A** · media **still**
- FIT decides, close to verbatim. 04-proof-lockedframe's use_when names "the 'I tried three things' beat of an advertorial", and this section is exactly three named things that were bought and abandoned: leave-in oils, silicone serums, a trigger spray bottle. --rivals keeps the product out of frame, which this beat requires. B swaps to --verdict, which puts the product in the last panel and answers a question the page has not asked yet — content.items.4 is where the product arrives. RATIO: 1:1 declared and a 1:1 slot, nothing cropped. EVIDENCE: the locked three-panel form is this type's most-rendered execution. PRODUCT PRESENCE: none in A, correctly. PROMPT RISK: 1331 characters against a stated ceiling of 1800.

### content.items.2.image · option A — `04-proof-lockedframe` `--rivals`

- varies on: baseline
- ratio `1:1` · type version `1.13`
- One shelf, one framing, the three fixes the copy names, each photographed after it was given up on rather than staged.
- **note:** Single-pass: the panels run handheld rather than strict, the route this type's own capability gate records for a renderer that cannot composite (ADR-021). --rivals is advertorial-legal and barred only on marketplace.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different mornings. ONE framing for every panel: the same bathroom shelf photographed square on from about half a metre back, the shelf across the lower third and a tiled wall behind. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiles and the same distance in all three panels. Variation on the props only: a toothbrush moved, a hair tie appearing, a folded flannel shifted.

The only thing that changes is which abandoned fix is on the shelf, and each is the plain unbranded version people already own. Panel one: a leave-in hair oil, the bottle half used and the outside of it tacky where it has been handled. Panel two: a silicone serum pump, its nozzle crusted and its collar left unlocked. Panel three: a plain trigger spray bottle, water still in it and a dried splash mark down one side. All three photographed at the same point in the routine, put back without being cleaned or straightened.

One neutral grade across every panel. Light differs only in exposure, never in warmth. No panel brighter, cleaner or tidier than another.

No product, no badges, no arrows and no text of any kind.
```

### content.items.2.image · option B — `04-proof-lockedframe` `--verdict`

- varies on: variant: --verdict, the product in the last panel
- ratio `1:1` · type version `1.13` · upload the product photo
- The same shelf and the same discipline with the product resolving the sequence, under the fairness rule: it may win by physics and never by treatment.
- **note:** Picking B introduces the product two sections earlier than the copy does, and content.items.4's mechanism argument then lands second rather than first. It also needs the reference photo attached, which A does not.

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

The attached photo is the exact reference for the product in the final panel.

Shot by one person on a phone on three different mornings. ONE framing for every panel: the same bathroom shelf photographed square on from about half a metre back, the shelf across the lower third and a tiled wall behind. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiles and the same distance in all three panels. Variation on the props only: a toothbrush moved, a hair tie appearing, a folded flannel shifted.

The only thing that changes is which tool is on the shelf. Panel one: a plain unbranded leave-in hair oil, common and in good condition. Panel two: a plain unbranded trigger spray bottle, common and in good condition. Panel three: the reference product. All three get identical exposure, identical background tidiness and identical framing generosity, and the difference must be visible in the objects themselves and never in how any panel is lit, styled, cropped or graded.

One neutral grade across every panel.

No badges, no arrows and no text of any kind.
```

### content.items.2.image · option C — `04-proof-lockedframe` `--rivals`

- varies on: execution: a bedroom chest of drawers, not the bathroom shelf
- ratio `1:1` · type version `1.13`
- Same type and same variant on the other surface these things accumulate on.
- **note:** Single-pass: panels run handheld (ADR-021).

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal vertical panels, thin white gutters, no outer border.

Shot by one person on a phone on three different mornings. ONE framing for every panel: the same corner of a bedroom chest of drawers photographed square on from about half a metre back, the top surface across the lower third and a plain wall behind. It reads as one shot taken three times, never as three different shots.

The same surface, the same wall and the same distance in all three panels. Variation on the props only: a hairband moved, a receipt appearing, a lamp base shifted at the edge.

The only thing that changes is which abandoned fix is on the surface, and each is the plain unbranded version people already own. Panel one: a leave-in hair oil, half used and tacky where it has been handled. Panel two: a silicone serum pump with a crusted nozzle. Panel three: a plain trigger spray bottle with a dried splash mark down one side. All three put back without being cleaned or straightened.

One neutral grade across every panel. Light differs only in exposure, never in warmth. No panel brighter, cleaner or tidier than another.

No product, no badges, no arrows and no text of any kind.
```

## `content.items.3.image` — cause

- asset `125-05-content3-cause-anatomy.png` · body item 4
- recommended: **option A** · media **still**
- FIT decides, and the SCALE decides which version of the argument is drawable. The section names two mechanisms: friction charging the strands, and rigid teeth dragging through fibres rather than yielding to a knot. The first is molecular and has no picture; the second is at the scale of a tooth against a hair, where both objects are the same order of magnitude and a viewer can see the difference. A argues the second and lets the first follow from it. This is A13 applied before the fact rather than after: on 2026-08-24 six renders failed because a product and an anatomy were drawn at incompatible scales. C goes closer still, to one strand's surface. RATIO: 1:1 declared and a 1:1 slot. PROMPT RISK: 1749 characters against ~2050 at three marks; A carries two.

### content.items.3.image · option A — `02-cause-anatomy` `--diagnostic`

- varies on: baseline
- ratio `1:1` · type version `1.15`
- A rigid tooth dragging across three strands against a rounded one passing between them, with the lifted scales and the gap between strands as the two marks. The culprit is the tooth, which is what the section indicts.

```
A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

The same three hair strands per panel, at the same scale and the same side-on view in both, running from the lower left to the upper right and drawn in warm ivory with their surface scales visible along the length. A single comb tooth enters each panel from above, at the same angle and the same depth in both.

Left panel: the tooth is rigid and square-edged. It drags across the strands rather than passing between them, the surface scales lift and stand open along its path, and the three strands push apart from each other and rise away from the tooth. Right panel: the tooth is rounded and yields as it meets the same strands, passing between them; the scales lie flat and closed, and the three strands stay parallel and settled.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each measuring the gap between the outer two strands at the same point along their length, both starting from the same point in their panel. Red on the left where the gap is wide, blue on the right where the strands sit close. One filled solid disc badge in the top corner of each panel, the same diameter in both, with its glyph cut out of it: a red X on the left, a green check on the right. The glyph is the hole in the disc, never a symbol drawn on top.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

### content.items.3.image · option B — `02-cause-anatomy`

- varies on: axis: the product's own tooth in the corrected panel
- ratio `1:1` · type version `1.15` · upload the product photo
- The same two panels in flat vector with the reference product's tooth doing the correcting instead of an unnamed rounded one.
- **note:** Picking B introduces the product one section earlier than the copy does, and it needs the reference photo attached, which A does not.

```
A 2D flat-vector medical illustration with flat fills and hard edges, no gradients. Not photography, not a 3D render.

The attached photo is the exact reference for the product.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

The same three hair strands per panel, at the same scale and the same side-on view in both, drawn in warm ivory with their surface scales visible along the length. A tooth enters each panel from above at the same angle and depth.

Left panel: a rigid square-edged tooth from an ordinary brush, dragging across the strands, the scales lifted open and the strands pushed apart. Right panel: the reference product's own rounded tooth, drawn at a size and angle where it is obviously that product, passing between the same strands with the scales lying flat and the strands parallel.

Marks: two dashed straight lines, one per panel, identical in thickness and dash pattern, each measuring the gap between the outer two strands at the same point, both starting from the same point in their panel. Red on the left, blue on the right. One filled solid disc badge in the top corner of each panel, same diameter, with its glyph cut out of it: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

### content.items.3.image · option C — `02-cause-anatomy` `--diagnostic`

- varies on: execution: one strand's surface, not three strands
- ratio `1:1` · type version `1.15`
- Same type and variant one step closer: a single strand filling the width with its scales lifted against the same strand with them lying flat.

```
A 2D airbrushed medical illustration with soft gradients and modelled volume. Not photography, not a 3D render.

Two equal panels side by side on one continuous dark slate ground of the same hue and chroma throughout, the ground on the right one step lighter in value than the ground on the left. Nothing else is in the background.

The same single hair strand per panel, at the same scale and the same side-on view in both, running left to right across the frame and drawn in warm ivory with its surface scales visible along the whole length. The strand fills most of the width so the scales are the subject.

Left panel: the scales are lifted and standing open along the strand, each one tilted away from the surface, and the strand's outline is ragged where they catch. Right panel: the same strand with the scales lying flat and closed against it, the outline continuous and smooth.

Marks: one dashed straight line per panel, identical in thickness and dash pattern, measuring the strand's outline height at the same point along its length in both, each starting from the same point in its panel. Red on the left where the lifted scales widen it, blue on the right where the outline is flat. One filled solid disc badge in the top corner of each panel, the same diameter in both, with its glyph cut out of it: a red X on the left, a green check on the right.

Colour follows the signal system exactly: red wrong, blue correct, green badge, warm ivory structure, and no other colour anywhere.
```

## `content.items.4.image` — mechanism

- asset `125-06-content4-mechanism-xray.png` · body item 5
- recommended: **option A** · media **still**
- FIT plus hard render evidence against the cell's other type. This section is a COMPONENT LIST — atomiser, cushion base, rounded bristles, six LEDs, vibration motor — and 03-mechanism-xray is the type that opens a gadget to show its real internal components. The cell's other type, 03-mechanism-ghostbody, is legal by the attribute gates and is NOT recommended: six renders of it on this exact product failed on 2026-08-21, all logged, and ADR-038 records why the cutaway cannot hold this product's argument at any scale. B argues the mist instead, which G8 makes the primary subject wherever the product emits something visible. RATIO: 1:1 declared and a 1:1 slot. PROMPT RISK: 1404 characters.

### content.items.4.image · option A — `03-mechanism-xray`

- varies on: baseline
- ratio `1:1` · type version `1.3` · upload the product photo
- The comb opened along its own length: reservoir, atomiser plate, LED row, vibration motor, battery. The subject is the product, so the scale problem that sank the body cutaways does not arise here.
- **note:** 03-mechanism-ghostbody is the cell's other type and is legal by the gates. It is not offered: six renders on this product failed on 2026-08-21 and ADR-038 records the reason. Refusing a type the evidence has retired is Stage 2 doing its job.

```
A 3D technical render.

The attached photo is the exact reference for the product.

A single product on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, no cast shadow on a floor. The product fills the frame and is the only object in it.

The reference product seen from the side at a slight three-quarter angle, its near half cut away along its length so the interior is open to view while the outline of the whole product stays unbroken and complete. The cut is a window into the body of the comb, never a piece removed from its silhouette.

Inside, exactly these components and nothing invented: the water reservoir occupying the upper body with its fill port at the top; the ultrasonic atomiser plate seated below it at the base of the reservoir; the six red LEDs set in a row under the bristle bed; the vibration motor behind them; and the battery filling the handle. Each is a distinct part with its own material finish, and each is the size it would really be inside a comb this size.

The product keeps its own reference colours throughout and carries no signal colour and no mark of any kind. The red of the LEDs is the LEDs themselves, lit, and nothing else in the frame is red.

Achromatic white and grey everywhere except the product's own colours.

No text, letters, labels, numbers, arrows, callouts or scale bars anywhere in the frame.
```

### content.items.4.image · option B — `06-relief-hero` `--detail`

- varies on: type: 06-relief-hero --detail, the mist as the subject
- ratio `1:1` · type version `1.16` · upload the product photo · `register: commercial`, `inset_mode: detail`
- The mechanism as a photograph rather than a cutaway, with the mist backlit as the primary subject and the atomiser plate magnified in a corner inset. G8 makes a visible emission the frame's subject wherever one exists.
- **note:** Picking B displaces 06-relief-hero from content.items.5, whose recommended option is the page's only relief frame; that slot would fall to its own B.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her thirties in an open-collar blouse standing at a kitchen counter, holding the reference product against the crown of her own hair mid-pass, her gaze on the window rather than on the product. She stands to the right of the frame so the product and the hair around it stay clear to the camera.

An ultra-fine dry-touch mist is leaving the bristle bed and hanging in the air around the crown, lit from behind so it reads against the darker background, and the six red LEDs under the bristles are visible as small lit points through the hair. The mist is the subject of the frame.

One real kitchen filled to the edges with things that genuinely belong there. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

In the upper left of the frame, held clear of both frame edges, sits a rounded-rectangle panel about a fifth of the frame wide with a thin white border, showing one magnified detail the scene cannot carry at this distance: the atomiser plate under the bristle bed with the mist forming at its surface, close enough that the plate's texture and the individual droplets are both readable. It is a photograph in the same register as the scene and does not bleed into it, linked to the product by proximity alone with no arrow and no glow border.

No mark of any kind appears anywhere in the frame.
```

### content.items.4.image · option C — `03-mechanism-xray`

- varies on: execution: from above, through the bristle bed
- ratio `1:1` · type version `1.3` · upload the product photo
- Same type opened on the other axis, which puts the LED row and the atomiser outlet in the same view as the bristles they sit under.

```
A 3D technical render.

The attached photo is the exact reference for the product.

A single product on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, no cast shadow on a floor. The product fills the frame and is the only object in it.

The reference product seen from directly above with the bristle bed facing the camera, its near surface cut away across the bed so the interior beneath the bristles is open to view while the outline of the whole product stays unbroken and complete. The cut is a window into the body of the comb, never a piece removed from its silhouette.

Inside, exactly these components and nothing invented: the six red LEDs set in a row under the bristle bed; the ultrasonic atomiser plate beside them with its outlet passing up between the bristles; the reservoir behind both; and the retracting carrier the bristles are mounted on, shown seated in its normal position. Each is a distinct part with its own material finish, and each is the size it would really be inside a comb this size.

The product keeps its own reference colours throughout and carries no signal colour and no mark of any kind. The red of the LEDs is the LEDs themselves, lit, and nothing else in the frame is red.

Achromatic white and grey everywhere except the product's own colours.

No text, letters, labels, numbers, arrows, callouts or scale bars anywhere in the frame.
```

## `content.items.5.image` — outcome

- asset `125-07-content5-relief-hero.png` · body item 6
- recommended: **option A** · media **still**
- FIT plus a type boundary found on 2026-08-24. The section closes on the daughter sitting happily through her bedhead without a whimper and the narrator's own routine taking two minutes. 06-relief-scene is normally the closing type for an advertorial, and it is offered at B rather than recommended: its `product` PART requires the product to STAND IN THE FRAME AS ITS OWN OBJECT near the camera, measured across twelve renders with everything held, inside or edge-on failing. A COMB CANNOT SATISFY THAT AND ALSO BE THE THING PRODUCING THE RELIEF, and two renders on 2026-08-24 resolved the contradiction by dropping the product entirely. 06-relief-hero has no such rule and takes the product in hand, so A recommends it. RATIO: relief-hero declares 1:1 and the slot is 1:1; relief-scene declares no 1:1 at all, which is a second reason B costs something. PROMPT RISK: 1236 characters.

### content.items.5.image · option A — `06-relief-hero`

- varies on: baseline
- ratio `1:1` · type version `1.16` · upload the product photo · `register: commercial`, `inset_mode: none`
- The morning the copy describes: the comb drawn through the child's hair in one pass, nobody holding anybody still, the halo gone. The product is in the frame doing the thing.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A school-age girl sitting in a kitchen chair on a bright weekday morning while a woman in her thirties draws the reference product down through the back of her hair in one unbroken pass. Neither is braced against anything and neither is holding the other still. The girl's hands rest loose in her lap and she is looking off towards the window. Her face carries effort and nothing more: no wince, no tears, no open mouth, no crying. Her face is settled and a small involuntary smile has arrived on its own.

The hair is the evidence: the length falling in one direction with an even surface, the halo gone from the crown, the section already passed lying flat against the section still to come.

The reference product is in the woman's hand, in the hair, doing the thing the section describes.

One real kitchen filled to the edges with things that genuinely belong there. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

No inset, no panel and no reserved layer anywhere in the frame. No mark of any kind.
```

### content.items.5.image · option B — `06-relief-scene`

- varies on: type: 06-relief-scene, the child using it herself
- ratio `16:9` · type version `3.7` · upload the product photo
- The closing-frame type, played as the child doing it for herself — which is what the copy's last line actually says.
- **note:** RATIO: 06-relief-scene declares 16:9, 4:3 and 3:4 and no 1:1, so this renders at 16:9 into a 1:1 slot and the layout centre-crops about 44% of the width. AND THE TYPE'S PRODUCT RULE HAS NO POSITION FOR A HAND TOOL: it requires the product to stand as its own object near the camera, which a comb in use cannot do. Two renders on 2026-08-24 dropped the product rather than resolve it. Offered because it is the cell's second type and the copy supports it, not because it is safe.

```
A candid documentary photograph, natural and unposed, sharp. A single frame a passer-by could have taken.

The attached photo is the exact reference for the product.

A school-age girl standing at a kitchen counter on a bright weekday morning, drawing the reference product through the length of her own hair in one unbroken pass, both hands her own and nobody else's on her. Nothing is held against her, nothing is braced, nothing is covered. Her chin is up, her shoulders are down and back, she is looking off towards the window rather than at the camera. Her face carries effort and nothing more: no wince, no tears, no open mouth, no crying. A small involuntary smile has arrived on its own.

The hair is the evidence: the length falling in one direction with an even surface, the halo gone from the crown, one section still lifting slightly where she has not reached yet.

The reference product is in her own hand, in her hair, being used.

An ordinary family kitchen mid-morning, nothing tidied and nothing arranged.

Even natural daylight, bright, soft shadows, plain and unglamorous.

No badges, no arrows, no overlays and no insets of any kind. No object in the scene carries printed text.
```

### content.items.5.image · option C — `06-relief-hero`

- varies on: execution: the narrator, not the child
- ratio `1:1` · type version `1.16` · upload the product photo · `register: commercial`, `inset_mode: none`
- Same type, the other half of the section: her own two-minute routine done, the laptop closed, the product put down beside it.

```
A professional photograph, natural and sharp, on a real camera.

The attached photo is the exact reference for the product.

A woman in her thirties in an open-collar blouse sitting at a kitchen table in front of a closed laptop, settled back with her weight even and both hands loose on the table, her gaze on the window rather than at the product. She sits to the right of the frame so her hair and the product stay clear to the camera.

The hair is the evidence: it falls in one direction with an even surface, the halo is gone from the crown, and nothing is lifting or clinging to her collar.

The reference product rests on the table beside the laptop, near the camera and turned so its face can be read, the way it was put down after a pass rather than placed for the picture.

One real kitchen filled to the edges with things that genuinely belong there. Background blurred, but no bare area larger than the product. None of those objects carries printed text. Soft even window light, high-key neutral grade.

No inset, no panel and no reserved layer anywhere in the frame. No mark of any kind.
```

### content.items.5.image · the motion brief — `relief` (whole-frame)

- form `whole-frame` · rung `natural` · reference folder: gifs-library/relief/ — no files filed yet; the folder card carries the law
- plate `plates/125-07-content5-relief-hero--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
advertorial-relief-massage-comb-spray-v02.webp
3s · 1:1 · seamless loop · animated webp, loop-safe, under the size ceiling

A shot of a woman drawing the comb down through a seated child's hair in one unbroken pass. The comb runs from crown to ends without catching, the child's shoulders stay down, and the hair falls and settles behind it.

IF THAT CANNOT BE SHOT
A shot of the child drawing the comb through her own hair at a counter. She runs it from the ends upward, the comb passes without snagging, and she lifts it away and starts a second pass on her own.
```

## `howto.image` — how-to-use

- asset `125-08-howto-use-sequence.png` · how-to card, beside the three numbered steps
- recommended: **option A** · media **still**
- FIT, and this is the first page of this product where the cell is not empty. 03-use-sequence needs `multi_step_usage: true` and this product has three named steps in its own copy — fill the reservoir, brush and mist from the tips up, click to retract and release trapped hair. On the seat-cushion pages the same cell was gated out and the slot had to be filled from an adjacent step; here the type is legal on its own terms. A renders the three steps as the type asks. B moves them to documentary photography of the product alone, which loses the hands and therefore the answer to "will I manage to use this". RATIO: 1:1 declared and a 1:1 slot. PROMPT RISK: 1290 characters.

### howto.image · option A — `03-use-sequence`

- varies on: baseline
- ratio `1:1` · type version `1.9` · upload the product photo
- Three stacked panels, one object, matte white hands: fill, mist from the tips up, retract and release. The third step is the one no competitor has and it closes the sequence.

```
A 3D technical render.

The attached photo is the exact reference for the product.

Three equal panels stacked one above the other, each the full width of the frame, divided by single thin horizontal lines. Each panel is a full render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, no cast shadow on a floor.

The same reference product in all three panels, the same object at the same scale from the same three-quarter angle, and a pair of featureless matte white hands operating it, no arms beyond the wrist and no body.

Panel one: the fill port at the top of the handle is open and a thin stream of clear water is entering it from a small jug held in the second hand. Panel two: the product is upright against a section of hair with the mist leaving the bristle bed as a fine cloud and the six red LEDs lit under the bristles, moving from the tips upward. Panel three: one thumb presses the retract button on the handle and the bristle carrier has lifted clear of the bed, a loose clump of shed hair pushed up off the teeth and lifting away.

The product keeps its own reference colours in every panel. Achromatic white and grey everywhere else.

No text, letters, labels, numbers, arrows or step markers anywhere in the frame.
```

### howto.image · option B — `04-proof-lockedframe` `--timelapse`

- varies on: type: 04-proof-lockedframe, the product alone across the routine
- ratio `1:1` · type version `1.13` · upload the product photo
- The same three moments as a locked documentary frame on a real shelf, which trades the instructional read for an evidentiary one.
- **note:** Picking B displaces 04-proof-lockedframe from content.items.2, whose recommended option is the page's only rivals frame. Single-pass: panels run handheld (ADR-021).

```
Honest documentary product test photography, unstyled, natural and sharp.

Three equal panels stacked one above the other, each the full width of the frame, thin white gutters, no outer border.

The attached photo is the exact reference for the product.

Shot by one person on a phone across one morning. ONE framing for every panel: the same bathroom shelf and basin edge photographed square on from about half a metre back, the shelf across the lower third. It reads as one shot taken three times, never as three different shots.

The same shelf, the same tiles and the same distance in all three panels. Variation on the props only: a toothbrush moved, a hair tie appearing, a flannel refolded.

The only thing that changes is where the product is in its routine. Panel one: standing on the shelf with its fill port open and a glass of water beside it. Panel two: lying on the basin edge with the mist still hanging in the air above the bristle bed and the LEDs lit. Panel three: standing on the shelf with the bristle carrier retracted and a small clump of shed hair lifted clear of the teeth.

One neutral grade across every panel. Light differs only in exposure, never in warmth.

No people, no hands, no badges, no arrows and no text of any kind.
```

### howto.image · option C — `03-use-sequence`

- varies on: execution: closer, the action readable at a glance
- ratio `1:1` · type version `1.9` · upload the product photo
- Same type and same three steps with the camera in tighter, so each panel is the action rather than the object.

```
A 3D technical render.

The attached photo is the exact reference for the product.

Three equal panels stacked one above the other, each the full width of the frame, divided by single thin horizontal lines. Each panel is a full render on a seamless white infinity background with soft even studio lighting and subtle grey ambient occlusion, no cast shadow on a floor.

The same reference product in all three panels, the same object at the same scale, and a pair of featureless matte white hands operating it, no arms beyond the wrist and no body. The camera is closer than a product shot: the product fills most of each panel and the action is readable at a glance.

Panel one: seen from the side with the fill port open at the top of the handle and clear water entering it. Panel two: seen from the side against a section of hair, the mist leaving the bristle bed as a fine cloud and the six red LEDs lit under the bristles. Panel three: seen from above with a thumb on the retract button and the bristle carrier lifted, a loose clump of shed hair pushed clear of the teeth.

The product keeps its own reference colours in every panel. Achromatic white and grey everywhere else.

No text, letters, labels, numbers, arrows or step markers anywhere in the frame.
```

### howto.image · the motion brief — `use` (whole-frame)

- form `whole-frame` · rung `natural` · reference folder: gifs-library/use/ — no files filed yet; the folder card carries the law
- plate `plates/125-08-howto-use-sequence--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset

```
advertorial-use-massage-comb-spray-v02.webp
4s · 1:1 · seamless loop · animated webp, loop-safe, under the size ceiling

A shot of the comb on a shelf. Water fills the port at the top of the handle, then it lifts to a section of hair and the mist starts, then a thumb presses the button and the teeth retract, pushing a clump of shed hair clear.

IF THAT CANNOT BE SHOT
A shot of the comb held in one hand over a bin. A thumb presses the button, the teeth rise off the bed and a clump of trapped hair is pushed clear and drops away, then the teeth seat back down.
```

## `social.photos.0.image` — social-proof

- asset `125-09-social-snapshot.png` · photo grid, tile 1 of 6
- recommended: **option A** · media **still**
- ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of variation, so the six tiles differ from each other rather than from a B and a C. This tile's place in the set: bedroom corner · own hair mid-use, hand in shot · cool early daylight · arm's length · in-use mode. The quote about a daughter who now brushes her own hair happily needs a first-person morning frame, and this is the only tile shot at arm's length. PRODUCT PRESENCE: the reference product is the subject of every tile. PROMPT RISK: 809 characters against a stated ceiling of 1800.

### social.photos.0.image · option A — `05-social-snapshot`

- varies on: bedroom corner · own hair mid-use, hand in shot · cool early daylight · arm's length · in-use mode
- ratio `1:1` · type version `1.2` · upload the product photo
- The quote about a daughter who now brushes her own hair happily needs a first-person morning frame, and this is the only tile shot at arm's length.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the SAME section element as six attributed quotes carrying reviewer names, five-star rows and Verified labels — measured on this export, zero closing tags between the grid and the quotes, twelve Verified labels and sixty star icons. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names, stars and verified labels — before rendering any of these. Seventh routed page in a row to breach it, so it is a template defect and not a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use, photographed by its owner looking down at their own hand: the reference comb drawn through the ends of their own hair, no face in shot.

An ordinary bedroom corner photographed exactly as found early on a weekday — the mess stays, nothing tidied, nothing added for the picture. Cool early daylight through a gap in the curtains, no other light.

One incidental owner object and no more: a charging cable trailing off the bedside table.

Framing tilted and a little too close, taken at arm's length; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `social.photos.1.image` — social-proof

- asset `125-10-social-snapshot.png` · photo grid, tile 2 of 6
- recommended: **option A** · media **still**
- ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of variation, so the six tiles differ from each other rather than from a B and a C. This tile's place in the set: family bathroom · shelf beside the basin · at rest, nobody present · flat overcast daylight · standing height looking down. The sceptic-with-fine-frizzy-texture quote. At-rest mode with nobody present, and the only tile that shows where the product lives rather than what it does. PRODUCT PRESENCE: the reference product is the subject of every tile. PROMPT RISK: 797 characters against a stated ceiling of 1800.

### social.photos.1.image · option A — `05-social-snapshot`

- varies on: family bathroom · shelf beside the basin · at rest, nobody present · flat overcast daylight · standing height looking down
- ratio `1:1` · type version `1.2` · upload the product photo
- The sceptic-with-fine-frizzy-texture quote. At-rest mode with nobody present, and the only tile that shows where the product lives rather than what it does.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the SAME section element as six attributed quotes carrying reviewer names, five-star rows and Verified labels — measured on this export, zero closing tags between the grid and the quotes, twelve Verified labels and sixty star icons. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names, stars and verified labels — before rendering any of these. Seventh routed page in a row to breach it, so it is a template defect and not a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product simply sitting where it now lives: the reference comb on a bathroom shelf beside the basin, nobody in the picture at all.

An ordinary family bathroom photographed exactly as found in the middle of the day — the mess stays, nothing tidied, nothing added for the picture. Flat overcast daylight through frosted glass, no other light.

One incidental owner object and no more: a child's toothbrush standing in a beaker.

Framing off-centre and taken from standing height looking down at the shelf; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `social.photos.2.image` — social-proof

- asset `125-11-social-snapshot.png` · photo grid, tile 3 of 6
- recommended: **option A** · media **still**
- ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of variation, so the six tiles differ from each other rather than from a B and a C. This tile's place in the set: parked car · rear-view mirror reflection · in use, no face readable · flat daylight through glass · one-handed from the seat. The quick-morning-routine quote, taken where a quick routine actually happens. The only tile with a reflection and the only one outside the home. PRODUCT PRESENCE: the reference product is the subject of every tile. PROMPT RISK: 817 characters against a stated ceiling of 1800.

### social.photos.2.image · option A — `05-social-snapshot`

- varies on: parked car · rear-view mirror reflection · in use, no face readable · flat daylight through glass · one-handed from the seat
- ratio `1:1` · type version `1.2` · upload the product photo
- The quick-morning-routine quote, taken where a quick routine actually happens. The only tile with a reflection and the only one outside the home.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the SAME section element as six attributed quotes carrying reviewer names, five-star rows and Verified labels — measured on this export, zero closing tags between the grid and the quotes, twelve Verified labels and sixty star icons. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names, stars and verified labels — before rendering any of these. Seventh routed page in a row to breach it, so it is a template defect and not a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use in a car, photographed by its owner from the driver's seat: the reference comb held up against the side of their hair in the rear-view mirror's reflection, no face readable.

An ordinary parked car photographed exactly as found on a grey afternoon — the mess stays, nothing tidied, nothing added for the picture. Flat daylight through the windscreen, no other light.

One incidental owner object and no more: a parking permit clipped to the visor.

Framing close and crooked, taken one-handed from the seat; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `social.photos.3.image` — social-proof

- asset `125-12-social-snapshot.png` · photo grid, tile 4 of 6
- recommended: **option A** · media **still**
- ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of variation, so the six tiles differ from each other rather than from a B and a C. This tile's place in the set: kitchen table · opened box and cable · just unboxed, nobody present · warm ceiling light · half a metre back at standing height. The whole-family and Type-C quote. The arrival moment none of the other tiles cover, and the only warm-lit frame in the set. PRODUCT PRESENCE: the reference product is the subject of every tile. PROMPT RISK: 860 characters against a stated ceiling of 1800.

### social.photos.3.image · option A — `05-social-snapshot`

- varies on: kitchen table · opened box and cable · just unboxed, nobody present · warm ceiling light · half a metre back at standing height
- ratio `1:1` · type version `1.2` · upload the product photo
- The whole-family and Type-C quote. The arrival moment none of the other tiles cover, and the only warm-lit frame in the set.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the SAME section element as six attributed quotes carrying reviewer names, five-star rows and Verified labels — measured on this export, zero closing tags between the grid and the quotes, twelve Verified labels and sixty star icons. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names, stars and verified labels — before rendering any of these. Seventh routed page in a row to breach it, so it is a template defect and not a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The opened box and its contents as the owner has just left them: the reference comb out of its packaging on a kitchen table with the flattened box and a Type-C cable pushed to one side. Nobody in the picture at all.

An ordinary kitchen photographed exactly as found in the evening — the mess stays, nothing tidied, nothing added for the picture. Warm yellow light from a single ceiling fitting, no other light.

One incidental owner object and no more: a fruit bowl at the edge of the table.

Framing slightly tilted, taken from standing height about half a metre back; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `social.photos.4.image` — social-proof

- asset `125-13-social-snapshot.png` · photo grid, tile 5 of 6
- recommended: **option A** · media **still**
- ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of variation, so the six tiles differ from each other rather than from a B and a C. This tile's place in the set: utility room · retracted teeth over a bin · in use, thumb on the button · hard overhead light · very close looking straight down. The retractable-teeth cleaning quote, which no other tile can carry. The only hard-lit tile and the closest framing in the set. PRODUCT PRESENCE: the reference product is the subject of every tile. PROMPT RISK: 824 characters against a stated ceiling of 1800.

### social.photos.4.image · option A — `05-social-snapshot`

- varies on: utility room · retracted teeth over a bin · in use, thumb on the button · hard overhead light · very close looking straight down
- ratio `1:1` · type version `1.2` · upload the product photo
- The retractable-teeth cleaning quote, which no other tile can carry. The only hard-lit tile and the closest framing in the set.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the SAME section element as six attributed quotes carrying reviewer names, five-star rows and Verified labels — measured on this export, zero closing tags between the grid and the quotes, twelve Verified labels and sixty star icons. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names, stars and verified labels — before rendering any of these. Seventh routed page in a row to breach it, so it is a template defect and not a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product's retracted teeth held open over a bin, photographed by its owner with one thumb on the button and a clump of shed hair lifting clear of the bristles, no face in shot.

An ordinary utility room photographed exactly as found at the weekend — the mess stays, nothing tidied, nothing added for the picture. Hard overhead light from a single bare fitting, no other light.

One incidental owner object and no more: a laundry basket half out of frame.

Framing very close and slightly out of square, taken looking straight down; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

## `social.photos.5.image` — social-proof

- asset `125-14-social-snapshot.png` · photo grid, tile 6 of 6
- recommended: **option A** · media **still**
- ONE OPTION, not three (ADR-022). A repeating section makes the SET the unit of variation, so the six tiles differ from each other rather than from a B and a C. This tile's place in the set: spare-room desk · comb at the crown with a laptop open · in use, over the shoulder · bright window daylight · very close over the shoulder. The sensitive-scalp quick-refresh quote, placed at the desk the page's own narrator works from. PRODUCT PRESENCE: the reference product is the subject of every tile. PROMPT RISK: 817 characters against a stated ceiling of 1800.

### social.photos.5.image · option A — `05-social-snapshot`

- varies on: spare-room desk · comb at the crown with a laptop open · in use, over the shoulder · bright window daylight · very close over the shoulder
- ratio `1:1` · type version `1.2` · upload the product photo
- The sensitive-scalp quick-refresh quote, placed at the desk the page's own narrator works from.
- **note:** PRECONDITION, and it is not optional: these six photo tiles sit inside the SAME section element as six attributed quotes carrying reviewer names, five-star rows and Verified labels — measured on this export, zero closing tags between the grid and the quotes, twelve Verified labels and sixty star icons. 05-social-snapshot's authenticity fence forbids a generated snapshot anywhere near a reviewer name, avatar, star row or verified badge. Use real customer photographs, or move the photo grid out of the attributed block, or drop the names, stars and verified labels — before rendering any of these. Seventh routed page in a row to breach it, so it is a template defect and not a page one.

```
A real customer's phone photo. One frame, no layout, no layers.

The attached photo is the exact reference for the product.

The product mid-use at a desk, photographed by its owner over their own shoulder: the reference comb resting against the crown of their hair with a laptop open in front of them, no face in shot.

An ordinary spare-room desk photographed exactly as found late morning — the mess stays, nothing tidied, nothing added for the picture. Bright window daylight from one side, no other light.

One incidental owner object and no more: a mug on a coaster beside the laptop.

Framing crooked and taken from very close over the shoulder; focus adequate but casual, mild noise, exposure honest to the room.

No studio light, no styling, no negative space, no borders and no text anywhere in the picture.
```

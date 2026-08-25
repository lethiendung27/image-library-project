# Page 193 — prompt options

Session `listicle-arm-trainer-hydraulic-v01` · channel `advertorial` · awareness `solution-aware` · registry 2.0.0

GENERATED FROM `prompts.json` by `build.py` — never hand-edit this file.

Motion: 3 loop(s) delivered against a floor of 2 and a ceiling of 5, margin 1.

## Page composition notes

- AWARENESS: solution-aware, read from the copy and not from a field. The opener spends no words establishing that a plateau exists — it assumes the reader is already there — and goes straight to comparing solution CLASSES: fixed dumbbells, coil twister bars, gym memberships and bodyweight. Reasons 2, 3 and 4 each indict one of those classes by name. For that reader, mechanism and physical proof are what decide it and re-amplifying the problem insults them, which is why exactly one pain image is routed and it sits in the header where the format demands one.
- PAGE SET: eight library slots, eight distinct types, no repeat. `01-pain-scene` opens; `03-mechanism-ghostbody` and `03-mechanism-xray` take the two mechanism cards, one inside the body and one inside the device; `02-cause-anatomy` takes the coil bar; `04-proof-lockedframe --verdict` takes the space claim; `05-social-handoff` takes the shared-use card; `03-use-sequence` takes the no-wall-chart card; `06-relief-hero` closes. The six review tiles take `05-social-snapshot` under the repeating-section exemption to one-type-once.
- STEP-3 BUDGET: two of {03-mechanism-ghostbody, 03-spec-split, 03-use-sequence} are used and the cap is two. `03-spec-split` was never available — it is marketplace-only.
- ATTRIBUTE GATES KILLED: 01-pain-split, 06-relief-scene. `01-pain-split` falls to symptom_visibility invisible, `06-relief-scene` to result_visibility invisible. Neither was needed: pain-split is not on the advertorial shortlist at all, and the closing image is `06-relief-hero`, which is the substitution that gate names.
- RATIO: every card is 1:1 and the header is 16:9. 1:1 is the ONLY ratio all seven card types share once ADR-016's five are intersected with each type's declared list — `03-mechanism-ghostbody` declares only 1:1 and 4:5, and 4:5 is not one of the five. 16:9 at the header because `01-pain-scene` does not declare 1:1.
- PIPELINE: every option is single-pass. `04-proof-lockedframe` runs handheld rather than strict and `05-social-handoff` omits its inset — both are the types' own recorded single-pass routes, not degradations invented here (ADR-021).
- REFERENCE PHOTO: `product.reference_photos` is empty because the export supplied none. Every prompt that needs one still carries its reference block and is paste-and-run — attach the product photo in the generation tool. `01-pain-scene` carries no product by design and needs nothing attached.
- AUTHENTICITY FENCE BREACHED, and it is a template defect rather than a routing one. The review block pairs each quote with a full name and a `Verified Buyer` label. `05-social-snapshot` forbids pairing a generated snapshot with a name, avatar, star row or verified badge — that is a fabricated endorsement. All six tiles ship with a blocking precondition on their own option: do not render until the block is de-attributed or real customer photographs are used. This is the sixth consecutive page carrying this defect.
- G6 AND THE LED COUNTER, recorded because the two rules that govern it do not agree. Reason 7 sells an LCD rep counter. G6's scope note admits diegetic text — a product's own readout is content, not overlay — but its production rule says screens are never model-drawn and are composited in post, and ADR-021 forbids compositing in this pipeline. Every option for that slot therefore renders the counter as a physical part with a DARK screen, and the number lives in the copy. The same conflict is why that slot's loop is refused. Worth an owner decision rather than a per-page workaround.
- PICKS: `feedback/picks.jsonl` holds no records, so Step 3's ≥20-pick tie-breaker never fired and no recommendation on this page is performance-backed. Every `recommended_opt` is a judgement from FIT, EVIDENCE and PROMPT RISK only.
- COVERAGE PASS (Step 5b): no additive proposals. For a solution-aware reader the rungs that matter are mechanism and physical proof, and the page already carries two mechanism images, a locked-frame comparison and a use sequence. The absent rung is a pain/amplification beat beyond the header, and Step 5b's own rule is that an absent rung is not automatically a gap — re-amplifying the problem to this reader is the thing the awareness ladder says not to do.

## `content.0.image` — hero

- asset: `193-01-opener-pain-scene.jpg` · placement: listicle header, under the title and dek, above the intro paragraphs
- recommended: **A** · media `still`
- basis: FIT: the opener has to make a plateaued home lifter recognise themselves before the list starts, which is this type's only job. EVIDENCE: rank 3 (the failed tool) is the only rung available — a plateau has no photographable symptom — and A carries it with four mismatched dumbbells including one still boxed, which is the copy's repeat-purchase sentence as an object. B moves to --confront and reads as frustration rather than limitation, which is the weaker half of the dek. PROMPT RISK: 1615/1565/1599 characters against this type's 2500 ceiling.

### Option A — `01-pain-scene` `--candid`

- varies on: baseline
- ratio `16:9` · type version `1.18` · pipeline `single-pass`
- axes: {"gaze": "candid"}
- The plateau has no photographable symptom, so evidence takes rank 3 — the failed tool in the state that shows it failed. Four mismatched dumbbells in three finishes, the heaviest still boxed, is the copy's own 'buying the next dumbbell up restarts the problem' as an object. --candid because a stalled press-up is physical limitation, not self-image.

```
TYPE: 01-pain-scene v1.18 --candid
REGISTER: editorial photojournalism, natural and unstaged. Single frame.

[SUBJECT]
Man in his late thirties in a washed-out t-shirt and jogging bottoms, on a living room rug at the top of a press-up, both arms locked straight and holding him there. Under that force: the elbows locked hard, both shoulders driven up around his ears, the weight stacked straight down through his wrists into the rug. Face: jaw slack, cheeks blown out, eyes down on the rug pile under his hands.

[EVIDENCE]
A row of mismatched dumbbells along the skirting board an arm's length from him: four different sizes in three different finishes, the smallest pair furred with dust, the heaviest pair still sitting in the open box it came in with the packing sunk in the middle.

[COST]
A gym holdall by the door, zip half open, a folded towel still inside it and dust settled along the shoulder strap. Sharp enough to read and never larger, nearer or brighter than the body it is being taken from.

[PLACE] A small first-floor living room, late evening.

[GAZE] Unaware of the camera, gaze down on the rug under his hands.

[LIGHT] The real light of the place and nothing added: one ceiling pendant on, and the last grey daylight through an uncurtained window behind him.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] An ordinary photograph in ordinary light. Normal exposure, detail held in both the shadows and the highlights, midtones open across most of the frame, colour true to life and muted rather than vivid.

STYLE: editorial photojournalism, natural and unstaged.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option B — `01-pain-scene` `--confront`

- varies on: axis: gaze=confront
- ratio `16:9` · type version `1.18` · pipeline `single-pass`
- axes: {"gaze": "confront"}
- Same evidence and cost, the moment moved to between sets and the gaze into the lens. --confront treats the plateau as a daily frustration rather than a physical limit, which is the reading the dek takes.

```
TYPE: 01-pain-scene v1.18 --confront
REGISTER: editorial photojournalism, natural and unstaged. Single frame.

[SUBJECT]
Man in his late thirties in a washed-out t-shirt and jogging bottoms, sitting back on his heels on a living room rug between sets, both forearms hanging over his knees. Under that force: the shoulders dropped and rolled forward, both hands open and slack, his chest still working for breath. Face: mouth open on the breath, brows drawn in, colour high across the cheeks.

[EVIDENCE]
A row of mismatched dumbbells along the skirting board an arm's length from him: four different sizes in three different finishes, the smallest pair furred with dust, the heaviest pair still sitting in the open box it came in with the packing sunk in the middle.

[COST]
A gym holdall by the door, zip half open, a folded towel still inside it and dust settled along the shoulder strap. Sharp enough to read and never larger, nearer or brighter than the body it is being taken from.

[PLACE] A small first-floor living room, late evening.

[GAZE] Looking directly into the lens.

[LIGHT] The real light of the place and nothing added: one ceiling pendant on, and the last grey daylight through an uncurtained window behind him.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] An ordinary photograph in ordinary light. Normal exposure, detail held in both the shadows and the highlights, midtones open across most of the frame, colour true to life and muted rather than vivid.

STYLE: editorial photojournalism, natural and unstaged.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option C — `01-pain-scene` `--candid`

- varies on: execution: persona, room and time of day
- ratio `16:9` · type version `1.18` · pipeline `single-pass`
- axes: {"gaze": "candid"}
- Same type and axes as A, a different person and place. The dumbbell evidence becomes a spinlock bar with its collar loose and plates stacked separately — the same argument in a household that bought adjustable iron instead.

```
TYPE: 01-pain-scene v1.18 --candid
REGISTER: editorial photojournalism, natural and unstaged. Single frame.

[SUBJECT]
Woman in her early forties in leggings and a loose vest, on a folded mat in the corner of a bedroom at the top of a press-up, both arms locked straight and holding her there. Under that force: the elbows locked hard, both shoulders driven up toward her ears, the weight stacked down through her wrists into the mat. Face: jaw slack, breath held, eyes down on the mat under her hands.

[EVIDENCE]
Two mismatched dumbbells on the carpet beside the mat, one a coated hex and one a chrome spinlock with a collar loose on the bar, and behind them a third bar with no collar at all and its plates stacked separately against the wardrobe door.

[COST]
A gym holdall shoved under the end of the bed, zip half open with a folded towel still inside it and dust settled along the shoulder strap. Sharp enough to read and never larger, nearer or brighter than the body it is being taken from.

[PLACE] The corner of a small bedroom, early morning.

[GAZE] Unaware of the camera, gaze down on the mat under her hands.

[LIGHT] The real light of the place and nothing added: flat overcast daylight through a net curtain, and a bedside lamp still on behind her.

[FORBIDDEN] No product, no panels, no insets. No mark of any kind.

[GRADE] An ordinary photograph in ordinary light. Normal exposure, detail held in both the shadows and the highlights, midtones open across most of the frame, colour true to life and muted rather than vivid.

STYLE: editorial photojournalism, natural and unstaged.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

- **no gif** — The slot exists so the reader recognises themselves, and recognition is a held state. A locked-out press-up at the top of the rep is a position, not a transition — nothing in the frame is mid-change. Consistent with every hero refused across the routed pages.

## `content.1.items.0.image` — mechanism

- asset: `193-02-reason1-mechanism-ghostbody.jpg` · placement: reason card 1, beside the body copy
- recommended: **A** · media `still`
- basis: FIT: the card argues a body fact no camera can film, which is the ghostbody trigger, and body_contact is true so the type survives its gate. B's medical register suits the subject but 3D holds the two-panel discipline more reliably in this library's history. PROMPT RISK: 2147/2038/2054 characters against this type's 2400 ceiling.

### Option A — `03-mechanism-ghostbody`

- varies on: baseline
- ratio `1:1` · type version `2.3` · pipeline `single-pass` · attach the product photo
- axes: {"medium": "3d-render"}
- The card's claim is a body fact — muscle grows against added resistance and bodyweight has no dial — which is exactly what this type exists to draw and what no camera can film. body_contact is true, so the type is not gated out. Two panels, the only variable being what the hands press against.

```
TYPE: 03-mechanism-ghostbody v2.3
REGISTER: 3D technical render on seamless white. NOT photography.

PRODUCT REFERENCE: Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It keeps its own reference colours and carries no mark of any kind.

PANELS: two equal panels side by side, divided by one thin vertical line. Both show the SAME featureless matte white mannequin in the SAME pose from the SAME angle: standing, seen from the front, both arms out in front of the chest at shoulder height and pressing inward, the chest and upper arm musculature open to view beneath the surface. The only difference between the panels is what the arms are pressing against and what the chest muscle does.

LEFT: the hands press against each other with nothing between them. The chest muscle is drawn thin and even along its whole length, unchanged from the resting form.
RIGHT: the reference arm trainer held between both hands at the same height, its grips taken by each hand and its arms compressed toward each other. The chest muscle is drawn thick and bunched along the same length, shortened and raised where it pulls.

CUTAWAY: the pectoral muscle and the front of the shoulder, inside the body silhouette, in both panels.

MARKS, three, nothing else in either panel is marked. Every one is a flat unshaded hard-edged overlay laid on top of the render, never a tint or fill of the anatomy:
- structure: the pectoral muscle and the front of the shoulder in warm off-white ivory, both panels.
- stress: RIGHT panel only. A flat blue band laid along the belly of the pectoral muscle where the load pulls it, following its line and clearly sitting on top of the render.
- verdict: one badge in the top corner of each panel — a red filled disc with a white cross in the LEFT, a green filled disc with a white check in the RIGHT. Same diameter, filled discs, not rings.

G3: red wrong, blue correct, green badge, nothing else.
Seamless white ground, soft even studio light, no shadow beyond a faint contact shadow.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option B — `03-mechanism-ghostbody`

- varies on: axis: medium = 2D medical illustration
- ratio `1:1` · type version `2.3` · pipeline `single-pass` · attach the product photo
- axes: {"medium": "2d-airbrush"}
- Same two-panel argument in the softer register. An airbrushed medical illustration reads as an explanation rather than a product render, which suits a card whose subject is the reader's own chest and not the device.

```
TYPE: 03-mechanism-ghostbody v2.3
REGISTER: 2D airbrushed medical illustration with soft gradients and modelled volume. NOT photography, NOT a 3D render.

PRODUCT REFERENCE: Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It keeps its own reference colours and carries no mark of any kind.

PANELS: two equal panels side by side, divided by one thin vertical line. Both show the SAME anonymous male torso and both arms in the SAME pose from the SAME angle: seen from the front, both arms out in front of the chest at shoulder height and pressing inward, the skin drawn translucent so the chest and upper arm muscles read through it. The only difference between the panels is what the arms press against and what the chest muscle does.

LEFT: the palms press flat against each other with nothing between them. The chest muscle lies long and slack, its fibres drawn evenly spaced from breastbone to shoulder.
RIGHT: the reference arm trainer held between both hands at the same height, its grips taken by each hand and its arms compressed toward each other. The same chest muscle is drawn shortened and thickened, its fibres crowded together toward the breastbone.

CUTAWAY: the pectoral muscle and the front of the shoulder, inside the body outline, in both panels.

MARKS, three, nothing else in either panel is marked:
- structure: the pectoral muscle and the front of the shoulder in warm ivory, both panels.
- stress: RIGHT panel only. A flat blue band laid along the belly of the pectoral muscle where the load pulls it, drawn on top of the illustration and following the muscle's own line.
- verdict: filled solid discs, red with a white cross in the LEFT panel's top corner, green with a white check in the RIGHT panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else.
Deep desaturated slate ground, the right half one step lighter than the left.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option C — `03-mechanism-ghostbody`

- varies on: execution: seated side view, single arm
- ratio `1:1` · type version `2.3` · pipeline `single-pass` · attach the product photo
- axes: {"medium": "3d-render"}
- Same type and medium as A, the view turned to the side and the argument narrowed to one arm driving forward. A side cut shows the muscle shortening along its length, which the front view can only show as thickening.

```
TYPE: 03-mechanism-ghostbody v2.3
REGISTER: 3D technical render on seamless white. NOT photography.

PRODUCT REFERENCE: Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It keeps its own reference colours and carries no mark of any kind.

PANELS: two equal panels side by side, divided by one thin vertical line. Both show the SAME featureless matte white mannequin in the SAME pose from the SAME angle: seated upright on a plain block, seen from the side facing left, the near arm bent and driving forward from the shoulder, the upper arm and shoulder musculature open to view beneath the surface. The only difference between the panels is what the hand drives against and what the arm muscle does.

LEFT: the hand drives forward into open air with nothing in it. The upper arm muscle is drawn thin and even along its whole length, unchanged from the resting form.
RIGHT: the reference arm trainer held in that hand at the same height, its grip taken and its arm compressed forward. The same upper arm muscle is drawn thick and raised along the same length, gathered toward the shoulder where it pulls.

CUTAWAY: the upper arm muscle and the shoulder joint, inside the body silhouette, in both panels.

MARKS, three, nothing else in either panel is marked. Every one is a flat unshaded hard-edged overlay laid on top of the render:
- structure: the upper arm muscle and the shoulder joint in warm off-white ivory, both panels.
- stress: RIGHT panel only. A flat blue band laid along the belly of the upper arm muscle where the load pulls it, following its line and clearly on top of the render.
- verdict: one badge in the top corner of each panel — red filled disc with a white cross LEFT, green filled disc with a white check RIGHT. Same diameter, filled discs, not rings.

G3: red wrong, blue correct, green badge, nothing else.
Seamless white ground, soft even studio light, faint contact shadow only.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

- **no gif** — Two locked panels are inspected rather than watched — the reader holds wrong and right side by side and reads the marks against each other. A re-execution as one continuous frame was examined at rung 2 and refused: the muscle change is a drawn abstraction, so a loop of it would animate an illustration's own convention rather than a real state changing.

## `content.1.items.1.image` — cause

- asset: `193-03-reason2-cause-anatomy.jpg` · placement: reason card 2, beside the body copy
- recommended: **A** · media `gif`
- basis: FIT: one named culprit and a measurable harm mechanism is exactly 02-cause-anatomy's trigger, and the harm stops when the culprit goes, which clears its avoid_when. A takes mid-stroke because the measure mark needs the coil compressed but still legible as a coil. PROMPT RISK: 1753/1633/1657 characters against this type's 2050 ceiling.

### Option A — `02-cause-anatomy` `--diagnostic`

- varies on: baseline
- ratio `1:1` · type version `1.15` · pipeline `single-pass` · attach the product photo
- The card blames one concrete object — a coil spring bar — and names its harm mechanism, stored energy released without control. That is this type's whole trigger. The harm does not persist once the culprit is gone, which is the avoid_when that would otherwise rule it out.

```
TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, paper-cut. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the arm trainer in the RIGHT panel.

FRAME: one resistance bar held across the chest of an anonymous torso, from grip to grip, the bar filling most of the width and the torso small behind it.
GROUND: deep desaturated slate, the right half one step lighter than the left.
BODY: the resistance element inside the bar, cut as a separate paper layer over a translucent bar outline, seen from the side. NOT a skeleton, NOT a machine drawing. Exactly one bar in EACH panel, same scale and view.

PANELS. LEFT: a generic unbranded coil spring bar, its steel coil wound tight and compressed hard between the two grips, the coil pitch squeezed almost closed at the centre of the stroke. RIGHT: the reference arm trainer at the same point of the same stroke, its hydraulic cylinder drawn as a smooth sealed tube with the piston partway down it and clear fluid either side of the piston, the tube unchanged in length along its wall.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each running along the resistance element from one end to the other and STOPPING at both ends. Both sit at the same height in their panel, identical thickness and dash. One property differs: on the left the line is bowed and crowded where the coil is compressed, on the right it is straight and evenly spaced. Red left, blue right. Straight dashes, not boxes.
- verdict: filled solid discs, red with a white cross in the LEFT panel's TOP corner, green with a white check in the RIGHT panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option B — `02-cause-anatomy` `--diagnostic`

- varies on: axis: style = flat vector, stroke at full compression
- ratio `1:1` · type version `1.15` · pipeline `single-pass` · attach the product photo
- Same argument at the end of the stroke rather than mid-stroke, drawn flat. Full compression is where the coil holds the most energy, so the measure mark has the widest difference to carry.

```
TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, flat-vector with flat fills and hard edges, no gradients. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the arm trainer in the RIGHT panel.

FRAME: one resistance bar seen end-on to the stroke, from grip to grip, the bar filling most of the width.
GROUND: deep desaturated olive, the right half one step lighter than the left.
BODY: the resistance element inside the bar, drawn as a flat cut layer over a translucent bar outline, seen from the side. NOT a skeleton, NOT a machine drawing. Exactly one bar in EACH panel, same scale and view.

PANELS. LEFT: a generic unbranded coil spring bar at the end of its stroke, the coil wound down to almost no gap between turns, the two grips forced close together. RIGHT: the reference arm trainer at the end of the same stroke, its hydraulic cylinder drawn as a sealed tube with the piston at the far end and fluid passing through a narrow port around it, the tube wall the same width along its whole length.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each drawn along the resistance element end to end and STOPPING at both ends. Same height in their panel, identical thickness and dash. One property differs: crowded and bunched on the left where the coil has closed, evenly spaced on the right. Red left, blue right.
- verdict: filled solid discs, red with a white cross in the LEFT panel's TOP corner, green with a white check in the RIGHT panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option C — `02-cause-anatomy` `--diagnostic`

- varies on: execution: the forearm and a slipping grip enter the frame
- ratio `1:1` · type version `1.15` · pipeline `single-pass` · attach the product photo
- Same type and style as A with the hand added, because the copy's failure moment is grip tiring on the last rep. The frame then shows the condition under which the stored energy is released rather than the energy alone.

```
TYPE: 02-cause-anatomy v1.15 --diagnostic
MEDIUM: 2D illustration, paper-cut. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the arm trainer in the RIGHT panel.

FRAME: one resistance bar and the forearm gripping it, from elbow to grip, the bar and the forearm together filling most of the width.
GROUND: deep desaturated slate, the right half one step lighter than the left.
BODY: the resistance element inside the bar and the forearm holding it, cut as separate paper layers in warm ivory over a translucent outline, seen from the side. NOT a skeleton. Exactly one bar and one forearm in EACH panel, same scale and view.

PANELS. LEFT: a generic unbranded coil spring bar with its coil wound tight and the grip beginning to slip out of the hand, the fingers half open and the coil still compressed behind them. RIGHT: the reference arm trainer at the same point of the same stroke with the same hand half open on the grip, its hydraulic cylinder drawn as a sealed tube with the piston resting where it was left and the fluid still either side of it.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each running along the resistance element from end to end and STOPPING at both ends. Same height in their panel, identical thickness and dash. One property differs: bowed and crowded on the left, straight and evenly spaced on the right. Red left, blue right.
- verdict: filled solid discs, red with a white cross in the LEFT panel's TOP corner, green with a white check in the RIGHT panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### GIF — `cause` (whole-frame)

- form `whole-frame` · rung `re-execution` · kind `cause` · reference folder: gifs-library/cause/ — no files filed yet; the folder card carries the law
- plate `plates/193-03-reason2-cause-anatomy--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset
- the loop replaces the WHOLE slot asset, so its ratio is the slot's own; the recommended still is complete and ships on its own (ADR-051)

```
output: listicle-arm-trainer-hydraulic-v01-content-1-items-1-image.mp4
ratio: 1:1
duration_s: 2.5
loop: seamless loop

brief: Two resistance bars lie side by side on a plain floor, each held compressed by a hand. Both hands let go at the same moment, the coil bar flies open and jumps clear of the floor, then the hydraulic bar opens slowly and evenly and stops where it was.

alt: A close shot of one coil bar and one hydraulic bar clamped in the same rig, both compressed and released together, the coil snapping open past its rest position while the hydraulic arm travels out at one steady speed.
delivery: mp4/webm, muted, loop-safe, under the size ceiling
```

## `content.1.items.2.image` — comparison

- asset: `193-04-reason3-proof-lockedframe.jpg` · placement: reason card 3, beside the body copy
- recommended: **A** · media `still`
- basis: FIT: floor space is visible to the naked eye inside a static frame, which is the one condition 04-proof-lockedframe sets. A stages the copy's own corner-of-the-room sentence; B and C are tighter binaries but narrower claims. PROMPT RISK: 2132/2043/2048 characters against this type's 2600 ceiling.

### Option A — `04-proof-lockedframe` `--verdict`

- varies on: baseline
- ratio `1:1` · type version `1.13` · pipeline `single-pass` · attach the product photo
- axes: {"camera_lock": "handheld"}
- The claim is floor space, which is exactly the difference a locked frame can prove: same corner, same light, only the occupant changes. --verdict puts the product last because left-to-right reading ends on it. Runs handheld, since strict camera lock needs compositing this pipeline cannot do.

```
TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It appears in the THIRD panel only.

[SCENE — the same in all three]
The same corner of a small living room: the same skirting board, the same short length of oak floor, the same armchair leg entering at the top right and the same folded throw over its arm. Flat overcast light from a window off to the left, no strong shadows, no styling.

[FRAMING]
One person photographed this corner three times from where they always stand, phone held at hip height and level with the floor, the corner of the room filling the middle third of each panel. It reads as one shot taken three times, never as three different shots. Light differs only in exposure, never in warmth.

[THE VARIABLE]
What is standing in that corner, each photographed on an ordinary evening.
1 — a two-tier dumbbell rack holding six mismatched dumbbells, the rack footprint covering the floor from the skirting board out past the armchair leg.
2 — no rack, the same six dumbbells set straight on the floor in two rows, taking a wider patch of floor than the rack did.
3 — the reference arm trainer folded flat and standing on its edge against the skirting board, the floor in front of it clear all the way to the armchair leg.

[FAIRNESS]
Panels 1 and 2 get exactly the same exposure, the same background tidiness and the same framing generosity as panel 3. The rack and the loose dumbbells are ordinary, undamaged and the kind someone would genuinely own. Nothing is lit, cropped or graded to favour any panel. The difference is in how much floor each occupies and nothing else.

[GRADE]
One grade across all three panels: flat, neutral, true to the room's own colour.

STYLE: honest documentary product test photography, unstyled, natural, sharp.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option B — `04-proof-lockedframe` `--verdict`

- varies on: execution: a bed drawer instead of a floor corner
- ratio `1:1` · type version `1.13` · pipeline `single-pass` · attach the product photo
- axes: {"camera_lock": "handheld"}
- Same variant, the test moved to storage rather than footprint. Whether the drawer closes is a binary a static frame reads instantly, where floor area has to be estimated.

```
TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It appears in the THIRD panel only.

[SCENE — the same in all three]
The same open drawer under the same divan bed: the same drawer base, the same folded jumper pushed to the back left, the same length of carpet in front of the drawer. Flat daylight from a window off to the right, no strong shadows, no styling.

[FRAMING]
One person photographed this drawer three times from standing, phone angled down over the open drawer, the drawer filling the middle two thirds of each panel. It reads as one shot taken three times, never as three different shots. Light differs only in exposure, never in warmth.

[THE VARIABLE]
What has been put into that drawer, each photographed on an ordinary evening.
1 — a pair of fixed dumbbells laid in the drawer, the drawer unable to close with them in and the front edge standing proud of the bed frame.
2 — a coil spring twister bar laid diagonally across the drawer, its grips overhanging both sides so the drawer front sits open on them.
3 — the reference arm trainer folded flat and lying inside the drawer, the folded jumper still in place beside it and the drawer front sitting flush.

[FAIRNESS]
Panels 1 and 2 get exactly the same exposure, background tidiness and framing generosity as panel 3. The dumbbells and the coil bar are ordinary, undamaged and the kind someone would genuinely own. Nothing is lit, cropped or graded to favour any panel. The difference is whether the drawer closes and nothing else.

[GRADE]
One grade across all three panels: flat, neutral, true to the room's own colour.

STYLE: honest documentary product test photography, unstyled, natural, sharp.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option C — `04-proof-lockedframe` `--verdict`

- varies on: execution: the gap under a couch
- ratio `1:1` · type version `1.13` · pipeline `single-pass` · attach the product photo
- axes: {"camera_lock": "handheld"}
- Same variant again, staged on the copy's own sentence — the frame slides under the couch. The rival panels fail by being stopped at the couch base, which is a physical outcome and not a treatment.

```
TYPE: 04-proof-lockedframe v1.13 --verdict, camera handheld
REGISTER: documentary photography. No overlays, badges, arrows or text.
LAYOUT: 3 equal vertical panels, thin white gutters, no outer border.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It appears in the THIRD panel only.

[SCENE — the same in all three]
The same stretch of floor beside the same two-seater couch: the same couch base and front feet, the same rug edge, the same power socket on the skirting board behind. Flat overcast light from a window off to the left, no strong shadows, no styling.

[FRAMING]
One person photographed this floor three times from where they always stand, phone held low and level with the rug, the gap under the couch running across the lower third of each panel. It reads as one shot taken three times, never as three different shots. Light differs only in exposure, never in warmth.

[THE VARIABLE]
What has been pushed toward the gap under the couch, each photographed on an ordinary evening.
1 — a two-tier dumbbell rack pushed as close as it goes, stopped by the couch base with its whole footprint still out on the rug.
2 — four loose dumbbells pushed at the gap, the two largest stopped by the couch base and left sitting out on the rug in front of it.
3 — the reference arm trainer folded flat and pushed into the gap, only the near edge of it still showing at the rug line.

[FAIRNESS]
Panels 1 and 2 get exactly the same exposure, background tidiness and framing generosity as panel 3. The rack and the dumbbells are ordinary, undamaged and the kind someone would genuinely own. Nothing is lit, cropped or graded to favour any panel. The difference is how far each one goes under and nothing else.

[GRADE]
One grade across all three panels: flat, neutral, true to the room's own colour.

STYLE: honest documentary product test photography, unstyled, natural, sharp.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

- **no gif** — Floor space is a held state: the rack occupies the corner whether or not time passes, and nothing in the frame changes. Examined at rung 2 as a folding shot and refused on the budget as well — `content.1` already carries its two permitted loops at items.1 and items.3, and this slot sits between them, so the spacing rule and not the argument decided it.

## `content.1.items.3.image` — mechanism

- asset: `193-05-reason4-mechanism-xray.jpg` · placement: reason card 4, beside the body copy
- recommended: **A** · media `gif`
- basis: FIT: the dial's value is entirely internal, and this type exists for gadget-class interiors that are not trivial — a piston, a port and a dial stem are three real connected parts. A's horizontal view keeps all three in one line. PROMPT RISK: 1539/1476/1452 characters against this type's 2000 ceiling.

### Option A — `03-mechanism-xray`

- varies on: baseline
- ratio `1:1` · type version `1.3` · pipeline `single-pass` · attach the product photo
- axes: {"canvas": "warm-grey"}
- The card sells an interior the buyer cannot see and would not otherwise believe — a dial that changes a fluid port. Horizontal and square to camera puts the whole cylinder across the frame, so the port and the dial stem read as one connected thing.

```
TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. The outer shell becomes translucent, but its silhouette, proportions and every visible external part must match the reference exactly.

CANVAS: a plain pale warm grey ground, and nothing else in the frame behind the product.

SHELL: the trainer lying horizontally across the frame, grips to left and right, its body translucent and glass-like, filling about 75 percent of the frame width.

INTERNALS, solid and detailed inside the shell, each at its true location: the hydraulic cylinder as a sealed metal tube through the centre of the body; a piston partway along that tube with clear fluid either side of it; a narrow adjustable port through the piston, its opening set part way; the dial collar around the outside of the tube, its stem running inward to that port.

MARKS, one, nothing else in the frame is marked:
- working: the fluid passing through the narrow port shown ACTIVE and glowing warm amber in its own moving form, the brightest thing in the frame and clearly brighter than the ground, drawn as fluid squeezing from the wide side of the piston to the narrow side. No arrow anywhere.

No text, numbers or spec labels anywhere in the image.
The mark is the only added colour; the product and its parts keep their own.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option B — `03-mechanism-xray`

- varies on: axis: canvas = deep charcoal, low three-quarter view
- ratio `1:1` · type version `1.3` · pipeline `single-pass` · attach the product photo
- axes: {"canvas": "charcoal"}
- Same internals, darker ground. The working mark has to be the brightest thing in frame, and a charcoal canvas buys that margin without brightening the mark itself. Adds the pivot joint, which the horizontal view crops.

```
TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. The outer shell becomes translucent, but its silhouette, proportions and every visible external part must match the reference exactly.

CANVAS: a plain deep charcoal ground, and nothing else in the frame behind the product.

SHELL: the trainer seen at a low three-quarter angle with one grip nearer the camera, its body translucent and glass-like, filling about 70 percent of the frame width.

INTERNALS, solid and detailed inside the shell, each at its true location: the hydraulic cylinder as a sealed metal tube running the length of the body; a piston head partway along it with clear fluid either side; a narrow adjustable port through the piston head; the dial collar on the outside of the tube with its stem reaching in to that port; the pivot joint where the two arms meet the body.

MARKS, one, nothing else in the frame is marked:
- working: the fluid crossing the narrow port shown ACTIVE and glowing warm amber in its own moving form, the brightest thing in the frame and clearly brighter than the ground. No arrow anywhere.

No text, numbers or spec labels anywhere in the image.
The mark is the only added colour; the product and its parts keep their own.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option C — `03-mechanism-xray`

- varies on: execution: upright, port set almost closed
- ratio `1:1` · type version `1.3` · pipeline `single-pass` · attach the product photo
- axes: {"canvas": "warm-sand"}
- Same type, the dial shown at the heavy end of its range rather than mid-way. An almost-closed port is the visual form of high resistance, so the frame argues the range rather than the mechanism alone.

```
TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. The outer shell becomes translucent, but its silhouette, proportions and every visible external part must match the reference exactly.

CANVAS: a plain pale warm sand ground, and nothing else in the frame behind the product.

SHELL: the trainer standing upright and square to the camera, grips at top and bottom, its body translucent and glass-like, filling about 65 percent of the frame height.

INTERNALS, solid and detailed inside the shell, each at its true location: the hydraulic cylinder as a sealed metal tube down the centre of the body; a piston partway down it with clear fluid above and below; a narrow adjustable port through the piston, its opening set almost closed; the dial collar around the tube with its stem running in to that port.

MARKS, one, nothing else in the frame is marked:
- working: the fluid forcing through the almost-closed port shown ACTIVE and glowing warm amber in its own moving form, the brightest thing in the frame and clearly brighter than the ground. No arrow anywhere.

No text, numbers or spec labels anywhere in the image.
The mark is the only added colour; the product and its parts keep their own.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### GIF — `mechanism` (whole-frame)

- form `whole-frame` · rung `natural` · kind `mechanism` · reference folder: gifs-library/mechanism/ — no files filed yet; the folder card carries the law
- plate `plates/193-05-reason4-mechanism-xray--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset
- the loop replaces the WHOLE slot asset, so its ratio is the slot's own; the recommended still is complete and ships on its own (ADR-051)

```
output: listicle-arm-trainer-hydraulic-v01-content-1-items-3-image.mp4
ratio: 1:1
duration_s: 2.5
loop: seamless loop

brief: A see-through view of the trainer's cylinder fills the frame with the piston partway along it. A hand turns the dial collar a short way and the port through the piston narrows, then the fluid crossing it slows and thickens while the piston keeps moving at the same speed.

alt: The same see-through cylinder with no hand in frame, the dial collar turning on its own and the port closing, the fluid stream through it thinning to a hard bright thread as the opening shrinks.
delivery: mp4/webm, muted, loop-safe, under the size ceiling
```

## `content.1.items.4.image` — social-proof

- asset: `193-06-reason5-social-handoff.jpg` · placement: reason card 5, beside the body copy
- recommended: **A** · media `still`
- basis: FIT: the copy describes a literal handoff across a couch, and this type is that moment. A keeps the dial under the receiving thumb, which is what turns a shared-device claim into a shared-RANGE claim. PROMPT RISK: 1644/1614/1599 characters against this type's 2300 ceiling.

### Option A — `05-social-handoff`

- varies on: baseline
- ratio `1:1` · type version `2.5` · pipeline `single-pass` · attach the product photo
- The copy's own sentence is a handoff — one person hands it across the couch and the other dials up. This type is the handoff, and the dial under the receiving thumb is what makes the shared-range claim visible rather than asserted. The inset is omitted, which is the type's own single-pass route.
- **note:** Inset omitted, not the type — the inset needs compositing and ADR-021 forbids it. The type calls the inset-free route the safer one.

```
TYPE: 05-social-handoff v2.5
REGISTER: candid documentary photograph, natural, unposed, sharp. One scene, no inset.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have.

[MOMENT]
The trainer is mid-handover across the couch: one person still has a hand on the near grip and the other has just taken the far grip, and the dial collar is under the thumb of the hand taking it. Both people are dealing with that dial.

[ADVOCATE]
Man in his thirties in a plain t-shirt, sitting forward on the couch with one hand still on the near grip where he has just stopped pressing, shoulders warm and breath still up. Mid-sentence, easy and slightly pleased with himself, his eyes on her and never on the camera.

[LISTENER]
Woman in her thirties in a long-sleeved top, sitting on the arm of the couch between him and the camera with her back to us, FACE NOT VISIBLE, head down to the dial her thumb is on.

[PRODUCT]
The reference trainer is the only thing in sharp focus, everything behind it softer. It carries the strongest light in the frame, nothing overlaps or crowds it, and it differs in hue and value from everything else in frame. Nothing of similar size or finish stands near it.

[ENVIRONMENT]
An ordinary living room in the evening, a couch with a throw pushed to one end, a coffee table with two mugs on it, a floor lamp on behind them, a rug with a corner turned up. None of those objects carries printed words.

STYLE: candid documentary photograph, natural, unposed, sharp.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option B — `05-social-handoff`

- varies on: execution: kitchen floor, roles reversed
- ratio `1:1` · type version `2.5` · pipeline `single-pass` · attach the product photo
- Same type and moment with the advocate a woman and the listener a man, which is the pairing the persona line describes first. A kitchen floor also removes the couch, so the frame does not read as a rest scene.
- **note:** Inset omitted, not the type.

```
TYPE: 05-social-handoff v2.5
REGISTER: candid documentary photograph, natural, unposed, sharp. One scene, no inset.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have.

[MOMENT]
The trainer has just changed hands on a kitchen floor: one person is letting go of the near grip and the other has both hands on it already, and the dial collar sits between their two hands where it was just turned. Both people are dealing with that dial.

[ADVOCATE]
Woman in her forties in a vest and leggings, kneeling on the floor with one hand still trailing the near grip, colour high in her face and her breath still up. Mid-sentence, direct and pleased, her eyes on him and never on the camera.

[LISTENER]
Man in his forties in a hoodie, crouching beside her between her and the camera with his back to us, FACE NOT VISIBLE, head down to the dial his hands have closed on.

[PRODUCT]
The reference trainer is the only thing in sharp focus, everything behind it softer. It carries the strongest light in the frame, nothing overlaps or crowds it, and it differs in hue and value from everything else in frame. Nothing of similar size or finish stands near it.

[ENVIRONMENT]
An ordinary kitchen in the morning, a table pushed back against the units, two chairs turned out, a water bottle on the floor by the skirting, a towel over the back of one chair. None of those objects carries printed words.

STYLE: candid documentary photograph, natural, unposed, sharp.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option C — `05-social-handoff`

- varies on: execution: hallway, passed at arm's length
- ratio `1:1` · type version `2.5` · pipeline `single-pass` · attach the product photo
- Same type, the handoff standing rather than seated. Arm's length puts the whole device between the two people, which is the clearest reading of one frame serving two programs.
- **note:** Inset omitted, not the type.

```
TYPE: 05-social-handoff v2.5
REGISTER: candid documentary photograph, natural, unposed, sharp. One scene, no inset.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have.

[MOMENT]
The trainer is being passed sideways along a hallway: one person holds it out by the near grip at arm's length and the other has closed a hand over the far grip, the dial collar showing between them where it has just been turned down. Both people are dealing with that dial.

[ADVOCATE]
Man in his late twenties in a training top, standing with the trainer held out to one side, one arm still extended from pressing, chest still working. Mid-sentence, quick and amused, his eyes on her and never on the camera.

[LISTENER]
Woman in her late twenties in a zip-up top, standing nearer the camera with her back to us, FACE NOT VISIBLE, head down to the far grip her hand has closed on.

[PRODUCT]
The reference trainer is the only thing in sharp focus, everything behind it softer. It carries the strongest light in the frame, nothing overlaps or crowds it, and it differs in hue and value from everything else in frame. Nothing of similar size or finish stands near it.

[ENVIRONMENT]
An ordinary flat hallway in the evening, coats on hooks along one wall, shoes paired under them, a hall light on overhead and a doorway open to a lit room behind. None of those objects carries printed words.

STYLE: candid documentary photograph, natural, unposed, sharp.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

- **no gif** — The argument IS temporal — a device changing hands and a dial turning between two people is a transition, and this slot earns motion on its own grounds. It is refused by the budget: `content.1` may carry two loops and both are taken by items.1 and items.3, which are non-adjacent where a third could not be. Recorded as a reserve.

## `content.3.items.0.image` — how-to-use

- asset: `193-07-reason6-use-sequence.jpg` · placement: reason card 6, beside the body copy
- recommended: **A** · media `gif`
- basis: FIT: the card's admission that there is no wall chart makes 'will I manage this' the slot's question, which is 03-use-sequence's own. A stages it on the rug the opener already established. PROMPT RISK: 1588/1620/1623 characters against this type's 2200 ceiling.

### Option A — `03-use-sequence`

- varies on: baseline
- ratio `1:1` · type version `1.9` · pipeline `single-pass` · attach the product photo
- The card's whole subject is that nothing tells you how to hold it, so the slot has to answer 'will I manage this'. multi_step_usage is true — set the dial, press, return — so the type is not gated out, and three panels are the wall chart the box does not contain.
- **note:** Step-3 budget: this is the second of the two permitted members of {ghostbody, spec-split, use-sequence} on this page. A third would be a lecture.

```
TYPE: 03-use-sequence v1.9
REGISTER: warm lifestyle photography, close range, natural and unstyled, soft daylight.

PRODUCT REFERENCE: Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It appears in every panel.

LAYOUT: exactly three photographs, one above another, each the full width of the frame and all three the same height, separated by thin white gutters, no outer border.

CONTINUITY: the SAME pair of hands in all three panels — same skin tone, same nails, same wrists, same cuffs. The same living room rug and the same couch edge behind throughout. The same warm neutral palette and the same soft daylight from the left in every panel. Camera distance and framing shift naturally between panels.

At the top, the trainer rests across the knees and one hand turns the dial collar around the body, the collar part way round and the other hand steadying the near grip.

In the middle, both hands are on the grips at chest height and the two arms of the trainer are compressed toward each other, the wrists straight and the elbows out.

At the bottom, the trainer rests across the knees again with both hands off it and the arms returned to their open position, one hand flat on the rug beside it.

The trainer sits at the same distance from the camera in the top and bottom panels and closer in the middle one.

No text, numbers or labels anywhere in any panel.

STYLE: warm lifestyle photography, close range, natural and unstyled.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option B — `03-use-sequence`

- varies on: execution: kitchen table, vertical press
- ratio `1:1` · type version `1.9` · pipeline `single-pass` · attach the product photo
- Same three beats on a table rather than the knees, and a vertical rather than a horizontal press. A table gives the panels a constant horizon, which is the easiest continuity for a renderer to hold across three frames.

```
TYPE: 03-use-sequence v1.9
REGISTER: warm lifestyle photography, close range, natural and unstyled, soft daylight.

PRODUCT REFERENCE: Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It appears in every panel.

LAYOUT: exactly three photographs, one above another, each the full width of the frame and all three the same height, separated by thin white gutters, no outer border.

CONTINUITY: the SAME pair of hands in all three panels — same skin tone, same nails, same wrists, same cuffs. The same kitchen table top and the same chair back behind throughout. The same warm neutral palette and the same soft daylight from the right in every panel. Camera distance and framing shift naturally between panels.

At the top, the trainer lies flat on the table and one hand turns the dial collar around the body while the other holds the near grip still against the table.

In the middle, the trainer is lifted clear of the table and held vertically, one hand on the upper grip and one on the lower, the two arms compressed toward each other and both wrists straight.

At the bottom, the trainer lies flat on the table again with both hands off it, its arms returned to their open position and one hand resting on the table edge beside it.

The trainer sits at the same distance from the camera in the top and bottom panels and closer in the middle one.

No text, numbers or labels anywhere in any panel.

STYLE: warm lifestyle photography, close range, natural and unstyled.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option C — `03-use-sequence`

- varies on: execution: bedroom floor, arms out at shoulder height
- ratio `1:1` · type version `1.9` · pipeline `single-pass` · attach the product photo
- Same three beats with the press taken out in front of the body, and the last panel showing the frame folded flat. That ends the sequence on the storage claim rather than on the rest position.

```
TYPE: 03-use-sequence v1.9
REGISTER: warm lifestyle photography, close range, natural and unstyled, soft daylight.

PRODUCT REFERENCE: Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It appears in every panel.

LAYOUT: exactly three photographs, one above another, each the full width of the frame and all three the same height, separated by thin white gutters, no outer border.

CONTINUITY: the SAME pair of hands in all three panels — same skin tone, same nails, same wrists, same cuffs. The same bedroom floor and the same wardrobe base behind throughout. The same warm neutral palette and the same soft daylight from the left in every panel. Camera distance and framing shift naturally between panels.

At the top, the trainer rests on the floor and one hand turns the dial collar around the body, the other hand holding the near grip down against the boards.

In the middle, both hands are on the grips out in front of the body at shoulder height and the two arms of the trainer are compressed toward each other, the elbows lifted and the wrists straight.

At the bottom, the trainer lies on the floor again with both hands off it, its arms returned to their open position, folded flat with one hand resting on the boards beside it.

The trainer sits at the same distance from the camera in the top and bottom panels and closer in the middle one.

No text, numbers or labels anywhere in any panel.

STYLE: warm lifestyle photography, close range, natural and unstyled.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### GIF — `use` (whole-frame)

- form `whole-frame` · rung `re-execution` · kind `use` · reference folder: gifs-library/use/ — no files filed yet; the folder card carries the law
- plate `plates/193-07-reason6-use-sequence--brief.svg` — generated by `scripts/gen-plate.py`, production only, never a page asset
- the loop replaces the WHOLE slot asset, so its ratio is the slot's own; the recommended still is complete and ships on its own (ADR-051)

```
output: listicle-arm-trainer-hydraulic-v01-content-3-items-0-image.mp4
ratio: 1:1
duration_s: 4
loop: seamless loop

brief: A pair of hands holds the trainer across the knees on a living room rug. One hand turns the dial collar a short way, both hands take the grips and press the two arms together until they nearly meet, then the arms open back out and the hands come off it.

alt: The same hands and the same rug with the trainer flat on the floor instead of the knees, one hand turning the collar and both hands pressing the arms together from above, then letting them rise back open.
delivery: mp4/webm, muted, loop-safe, under the size ceiling
```

## `content.3.items.1.image` — outcome

- asset: `193-08-reason7-relief-hero.jpg` · placement: reason card 7, the closing card of the list
- recommended: **A** · media `still`
- basis: FIT: the closing card needs the product whole in a real room, which is 06-relief-hero's job, and commercial register suits a landing page's last image. All three options carry the same G6 counter rule. PROMPT RISK: 1500/1554/1517 characters against this type's 2600 ceiling.

### Option A — `06-relief-hero`

- varies on: baseline
- ratio `1:1` · type version `1.17` · pipeline `single-pass` · attach the product photo
- axes: {"register": "commercial"}
- The closing card, and the one image that has to show the product whole in a real room after a session. The counter housing is turned to camera and its screen left dark — see this slot's composition note, which is where the counter's readout is dealt with.
- **note:** G6 COUNTER RULE. The card sells an LCD readout. G6's scope note admits diegetic screen text as content, but its production rule is that screens are never model-drawn and are composited in post — which ADR-021 forbids this pipeline. Both are satisfied the only way available: the counter is in frame as a physical part and its screen is dark. The number is claimed in copy, never rendered.

```
TYPE: 06-relief-hero v1.17 --commercial
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have.

[SUBJECT]
Man in his thirties in a training top, sitting on the edge of a couch a moment after a set, the trainer resting across his thighs with both hands still loosely on the grips, looking down at the counter housing on the body of it rather than at the camera. Settled, breathing out, mid-action just ended.

[PRODUCT]
The reference trainer across his thighs, low front three-quarter angle, whole and unobstructed, the counter housing on its body turned toward the camera and its screen dark and unlit.

[SETTING]
A real living room corner filled to the edges: a water bottle on the floor by the couch foot, a towel over the couch arm, a rug with a corner turned up, a floor lamp on behind, a bowl on the coffee table, a pair of trainers by the skirting. None of them carries printed words. Background soft, never blank.

[LIGHT]
Soft even window light from the left, background blurred, high-key neutral grade.

[LAYOUT]
He sits to the left of the frame; the right side carries the depth of the room.

No text, numbers, digits or readouts anywhere in the image. The counter screen is dark and carries nothing.

STYLE: clean commercial photograph, controlled light, sharp.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option B — `06-relief-hero`

- varies on: axis: register = ugc, subject reduced to hands
- ratio `1:1` · type version `1.17` · pipeline `single-pass` · attach the product photo
- axes: {"register": "ugc", "subject": "reduced"}
- Same slot in the trust register, subject reduced to forearms because the result here is the finished set and not the person. `reduced` names what makes finished look different from unfinished — the arms returned to rest and neither hand loaded.
- **note:** G6 COUNTER RULE as option A: counter present, screen dark, no digits.

```
TYPE: 06-relief-hero v1.17 --ugc
REGISTER: a phone in an ordinary person's hand: slightly off exposure, no rim light, no negative space, framing casual and a little too close, the room left exactly as it is.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have.

[SUBJECT]
Present only as working hands and forearms — no face. Both hands are off the grips and resting either side of the trainer where it lies across a rug, one thumb still against the counter housing on its body. What makes finished look different from unfinished: the two arms of the trainer have returned to their open resting position and neither hand is loaded.

[PRODUCT]
The reference trainer lying across the rug between the forearms, seen from above at a slight angle, whole and unobstructed, the counter housing turned up toward the camera and its screen dark and unlit.

[SETTING]
An ordinary living room floor left exactly as it is: a water bottle on its side, a balled towel, the corner of a couch, a phone face down on the rug, a sock, a mug on the boards. None of them carries printed words. Nothing tidied, nothing removed.

[LIGHT]
Ordinary room light, mild overexposure where the window falls on the rug, no rim light.

No text, numbers, digits or readouts anywhere in the image. The counter screen is dark and carries nothing.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

### Option C — `06-relief-hero`

- varies on: execution: bedroom, product standing rather than across the lap
- ratio `1:1` · type version `1.17` · pipeline `single-pass` · attach the product photo
- axes: {"register": "commercial"}
- Same type and register as A, a different person and room, and the device standing on the floor so its whole silhouette reads. A standing frame also shows it takes no more floor than its own footprint.
- **note:** G6 COUNTER RULE as option A: counter present, screen dark, no digits.

```
TYPE: 06-relief-hero v1.17 --commercial
REGISTER: clean commercial photograph, controlled light, sharp.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have.

[SUBJECT]
Woman in her forties in a vest and leggings, kneeling back on her heels on a bedroom floor a moment after a set, the trainer standing on the boards in front of her with one hand resting on its upper grip, looking down at the counter housing on its body rather than at the camera. Settled, breathing out, mid-action just ended.

[PRODUCT]
The reference trainer standing on the boards in front of her, low front three-quarter angle, whole and unobstructed, the counter housing on its body turned toward the camera and its screen dark and unlit.

[SETTING]
A real bedroom corner filled to the edges: a rolled mat against the wardrobe, a water bottle on the boards, a hairband on the sill, a chair with a jumper over the back, a laundry basket, a lamp on the floor. None of them carries printed words. Background soft, never blank.

[LIGHT]
Soft even window light from the right, background blurred, high-key neutral grade.

[LAYOUT]
She kneels to the right of the frame; the left side carries the depth of the room.

No text, numbers, digits or readouts anywhere in the image. The counter screen is dark and carries nothing.

STYLE: clean commercial photograph, controlled light, sharp.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

- **no gif** — The rep motion is temporal and this slot would earn a loop on the argument, but the loop the card actually wants is the counter incrementing, and that is a readout changing — G6 admits diegetic screen text only on a production rule (never model-drawn, composited in post) that ADR-021 forbids. Refused on the frame's own terms rather than the budget's. `content.3` also carries its one permitted loop at items.0.

## `reviews.photos.0.image` — social-proof

- asset: `193-09-review1-social-snapshot.jpg` · placement: review wall tile 1 of 6, above the quote and its attribution
- recommended: **A** · media `still`
- basis: One option by the type's SET DIVERSITY LAW. Not renderable as the block stands — see the blocking precondition on the option.

### Option A — `05-social-snapshot`

- varies on: set member 1 of 6 — room class, surface, anchor and light all differ from every sibling
- ratio `1:1` · type version `1.2` · pipeline `single-pass` · attach the product photo
- One option only: the type legislates a SET, so the unit of variation is the tile and not the cell. Three options inside one tile would spend the variation in the wrong place.
- **BLOCKING — DO NOT RENDER UNTIL RESOLVED. This tile sits in a review block whose quotes each carry a full name and a `Verified Buyer` label. `05-social-snapshot` SLOT CONSTRAINTS: never pair a generated snapshot with a reviewer name, avatar, star row or verified badge, and never present one as an actual customer upload — that is a fabricated endorsement (FTC). Resolve by de-attributing the block or by using real customer photographs. The prompt is emitted so the fix is a template change and not a re-route.**

```
A real customer's phone photo. One frame, no layout.

Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It is standing folded flat on its edge against a skirting board, photographed from standing height and cropped the way a casual one-handed photo crops.

CONTENT MODE, at-rest.

SCENE: A studio flat photographed as found — a scuffed painted skirting board, a worn oak floorboard, the base of a radiator behind.

ANCHOR: A pair of slippers kicked off beside it — the one incidental owner object.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus adequate, mild noise, honest exposure, warm ceiling light with a cool window spill. No styling of any kind.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
NO text overlays, no logo, no watermark, no badges, no borders. No digits or readouts anywhere; any counter screen is dark and carries nothing.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

- **no gif** — No social-proof slot carries motion. The mechanism is the six-type gif set carrying no `social` type at all, so there is nothing to file a loop under — wall tile or standalone. Not a budget decision.

## `reviews.photos.1.image` — social-proof

- asset: `193-09-review2-social-snapshot.jpg` · placement: review wall tile 2 of 6, above the quote and its attribution
- recommended: **A** · media `still`
- basis: One option by the type's SET DIVERSITY LAW. Not renderable as the block stands — see the blocking precondition on the option.

### Option A — `05-social-snapshot`

- varies on: set member 2 of 6 — room class, surface, anchor and light all differ from every sibling
- ratio `1:1` · type version `1.2` · pipeline `single-pass` · attach the product photo
- One option only: the type legislates a SET, so the unit of variation is the tile and not the cell. Three options inside one tile would spend the variation in the wrong place.
- **BLOCKING — DO NOT RENDER UNTIL RESOLVED. This tile sits in a review block whose quotes each carry a full name and a `Verified Buyer` label. `05-social-snapshot` SLOT CONSTRAINTS: never pair a generated snapshot with a reviewer name, avatar, star row or verified badge, and never present one as an actual customer upload — that is a fabricated endorsement (FTC). Resolve by de-attributing the block or by using real customer photographs. The prompt is emitted so the fix is a template change and not a re-route.**

```
A real customer's phone photo. One frame, no layout.

Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It is held across the chest mid-press, both grips taken, seen from slightly below and a little too close.

CONTENT MODE, in-use.

SCENE: A narrow spare bedroom photographed as found — a wardrobe door ajar, a folded duvet at the end of the bed, a curtain half drawn.

ANCHOR: A wall clock hanging crooked above the bed — the one incidental owner object.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus adequate, mild noise, honest exposure, flat grey daylight through the half-drawn curtain. No styling of any kind.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
NO text overlays, no logo, no watermark, no badges, no borders. No digits or readouts anywhere; any counter screen is dark and carries nothing.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

- **no gif** — No social-proof slot carries motion. The mechanism is the six-type gif set carrying no `social` type at all, so there is nothing to file a loop under — wall tile or standalone. Not a budget decision.

## `reviews.photos.2.image` — social-proof

- asset: `193-09-review3-social-snapshot.jpg` · placement: review wall tile 3 of 6, above the quote and its attribution
- recommended: **A** · media `still`
- basis: One option by the type's SET DIVERSITY LAW. Not renderable as the block stands — see the blocking precondition on the option.

### Option A — `05-social-snapshot`

- varies on: set member 3 of 6 — room class, surface, anchor and light all differ from every sibling
- ratio `1:1` · type version `1.2` · pipeline `single-pass` · attach the product photo
- One option only: the type legislates a SET, so the unit of variation is the tile and not the cell. Three options inside one tile would spend the variation in the wrong place.
- **BLOCKING — DO NOT RENDER UNTIL RESOLVED. This tile sits in a review block whose quotes each carry a full name and a `Verified Buyer` label. `05-social-snapshot` SLOT CONSTRAINTS: never pair a generated snapshot with a reviewer name, avatar, star row or verified badge, and never present one as an actual customer upload — that is a fabricated endorsement (FTC). Resolve by de-attributing the block or by using real customer photographs. The prompt is emitted so the fix is a template change and not a re-route.**

```
A real customer's phone photo. One frame, no layout.

Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It is lying on a desk beside a laptop, folded flat, photographed from a seated position looking down.

CONTENT MODE, at-rest.

SCENE: A home-office corner photographed as found — a laminate desktop with a ring mark, a cable coming over the back edge, a chair arm entering the frame.

ANCHOR: A half-drunk glass of water on a coaster — the one incidental owner object.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus adequate, mild noise, honest exposure, cool screen light mixed with a warm desk lamp. No styling of any kind.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
NO text overlays, no logo, no watermark, no badges, no borders. No digits or readouts anywhere; any counter screen is dark and carries nothing.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

- **no gif** — No social-proof slot carries motion. The mechanism is the six-type gif set carrying no `social` type at all, so there is nothing to file a loop under — wall tile or standalone. Not a budget decision.

## `reviews.photos.3.image` — social-proof

- asset: `193-09-review4-social-snapshot.jpg` · placement: review wall tile 4 of 6, above the quote and its attribution
- recommended: **A** · media `still`
- basis: One option by the type's SET DIVERSITY LAW. Not renderable as the block stands — see the blocking precondition on the option.

### Option A — `05-social-snapshot`

- varies on: set member 4 of 6 — room class, surface, anchor and light all differ from every sibling
- ratio `1:1` · type version `1.2` · pipeline `single-pass` · attach the product photo
- One option only: the type legislates a SET, so the unit of variation is the tile and not the cell. Three options inside one tile would spend the variation in the wrong place.
- **BLOCKING — DO NOT RENDER UNTIL RESOLVED. This tile sits in a review block whose quotes each carry a full name and a `Verified Buyer` label. `05-social-snapshot` SLOT CONSTRAINTS: never pair a generated snapshot with a reviewer name, avatar, star row or verified badge, and never present one as an actual customer upload — that is a fabricated endorsement (FTC). Resolve by de-attributing the block or by using real customer photographs. The prompt is emitted so the fix is a template change and not a re-route.**

```
A real customer's phone photo. One frame, no layout.

Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It is lying in the gap under a divan bed, folded flat, photographed from floor level with the phone tilted down.

CONTENT MODE, at-rest.

SCENE: A rented bedroom photographed as found — carpet with a flattened track across it, a divan base, a plug socket on the skirting.

ANCHOR: A phone charger cable coiled beside it — the one incidental owner object.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus adequate, mild noise, honest exposure, low evening light from one bedside lamp. No styling of any kind.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
NO text overlays, no logo, no watermark, no badges, no borders. No digits or readouts anywhere; any counter screen is dark and carries nothing.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

- **no gif** — No social-proof slot carries motion. The mechanism is the six-type gif set carrying no `social` type at all, so there is nothing to file a loop under — wall tile or standalone. Not a budget decision.

## `reviews.photos.4.image` — social-proof

- asset: `193-09-review5-social-snapshot.jpg` · placement: review wall tile 5 of 6, above the quote and its attribution
- recommended: **A** · media `still`
- basis: One option by the type's SET DIVERSITY LAW. Not renderable as the block stands — see the blocking precondition on the option.

### Option A — `05-social-snapshot`

- varies on: set member 5 of 6 — room class, surface, anchor and light all differ from every sibling
- ratio `1:1` · type version `1.2` · pipeline `single-pass` · attach the product photo
- One option only: the type legislates a SET, so the unit of variation is the tile and not the cell. Three options inside one tile would spend the variation in the wrong place.
- **BLOCKING — DO NOT RENDER UNTIL RESOLVED. This tile sits in a review block whose quotes each carry a full name and a `Verified Buyer` label. `05-social-snapshot` SLOT CONSTRAINTS: never pair a generated snapshot with a reviewer name, avatar, star row or verified badge, and never present one as an actual customer upload — that is a fabricated endorsement (FTC). Resolve by de-attributing the block or by using real customer photographs. The prompt is emitted so the fix is a template change and not a re-route.**

```
A real customer's phone photo. One frame, no layout.

Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It is held out to one side at arm's length, one grip taken, seen from across a room and cropped a little too wide.

CONTENT MODE, in-use.

SCENE: A through lounge photographed as found — two mismatched armchairs, a rug that does not reach the walls, a doorway to a lit hall behind.

ANCHOR: A remote control left on an armchair seat — the one incidental owner object.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus adequate, mild noise, honest exposure, mixed warm lamplight and dim daylight. No styling of any kind.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
NO text overlays, no logo, no watermark, no badges, no borders. No digits or readouts anywhere; any counter screen is dark and carries nothing.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

- **no gif** — No social-proof slot carries motion. The mechanism is the six-type gif set carrying no `social` type at all, so there is nothing to file a loop under — wall tile or standalone. Not a budget decision.

## `reviews.photos.5.image` — social-proof

- asset: `193-09-review6-social-snapshot.jpg` · placement: review wall tile 6 of 6, above the quote and its attribution
- recommended: **A** · media `still`
- basis: One option by the type's SET DIVERSITY LAW. Not renderable as the block stands — see the blocking precondition on the option.

### Option A — `05-social-snapshot`

- varies on: set member 6 of 6 — room class, surface, anchor and light all differ from every sibling
- ratio `1:1` · type version `1.2` · pipeline `single-pass` · attach the product photo
- One option only: the type legislates a SET, so the unit of variation is the tile and not the cell. Three options inside one tile would spend the variation in the wrong place.
- **BLOCKING — DO NOT RENDER UNTIL RESOLVED. This tile sits in a review block whose quotes each carry a full name and a `Verified Buyer` label. `05-social-snapshot` SLOT CONSTRAINTS: never pair a generated snapshot with a reviewer name, avatar, star row or verified badge, and never present one as an actual customer upload — that is a fabricated endorsement (FTC). Resolve by de-attributing the block or by using real customer photographs. The prompt is emitted so the fix is a template change and not a re-route.**

```
A real customer's phone photo. One frame, no layout.

Use the attached photo as the exact reference for the arm trainer. Preserve shape, proportions, material, finish and colour exactly. Do not redesign it, and add no part the reference does not have. It is standing folded on end inside an open under-stairs cupboard, photographed with the phone held at chest height.

CONTENT MODE, at-rest.

SCENE: An under-stairs cupboard photographed as found — bare plaster, a sloping ceiling, a vacuum cleaner hose coiled on the floor.

ANCHOR: A folded step ladder leaning at the back — the one incidental owner object.

CAMERA TRUTH: framing tilted a few degrees and a little too close, focus adequate, mild noise, honest exposure, a single bare bulb overhead. No styling of any kind.

STYLE: honest phone photography, unedited look, natural, slightly imperfect.
NO text overlays, no logo, no watermark, no badges, no borders. No digits or readouts anywhere; any counter screen is dark and carries nothing.

Strictly avoid: text, letters, numbers, watermark, logo, deformed hands, extra fingers, redesigned product, altered product shape, invented product details, different product than reference
```

- **no gif** — No social-proof slot carries motion. The mechanism is the six-type gif set carrying no `social` type at all, so there is nothing to file a loop under — wall tile or standalone. Not a budget decision.

## `rail.image` — cta

- placement: sticky deal rail thumbnail
- **out of library scope** — A standard product shot, a brand mark or an offer badge — the slot-rules `cta` row is empty on every channel and this is out of library scope.

## `scarcity.image` — cta

- placement: scarcity block, beside the countdown
- **out of library scope** — A standard product shot, a brand mark or an offer badge — the slot-rules `cta` row is empty on every channel and this is out of library scope.

## `scarcity.badge_image` — cta

- placement: scarcity block badge
- **out of library scope** — A standard product shot, a brand mark or an offer badge — the slot-rules `cta` row is empty on every channel and this is out of library scope.

## `guarantee.badge_image` — cta

- placement: guarantee band badge
- **out of library scope** — A standard product shot, a brand mark or an offer badge — the slot-rules `cta` row is empty on every channel and this is out of library scope.

## `header.logo` — cta

- placement: site header brand mark
- **out of library scope** — A standard product shot, a brand mark or an offer badge — the slot-rules `cta` row is empty on every channel and this is out of library scope.

## `footer.logo` — cta

- placement: site footer brand mark
- **out of library scope** — A standard product shot, a brand mark or an offer badge — the slot-rules `cta` row is empty on every channel and this is out of library scope.

## `closing.bio_image` — author

- placement: About the Author card portrait
- **out of library scope** — A portrait of a named person. The slot-rules `author` row is empty on every channel by decision: no library type produces a portrait of a named individual, and generating a face to sit under a real byline is a disclosure decision rather than an image one.

## `comments.items.0.avatar` — author

- placement: comment thread avatar 1 of 7
- **out of library scope** — A portrait of a named person. The slot-rules `author` row is empty on every channel by decision: no library type produces a portrait of a named individual, and generating a face to sit under a real byline is a disclosure decision rather than an image one.

## `comments.items.1.avatar` — author

- placement: comment thread avatar 2 of 7
- **out of library scope** — A portrait of a named person. The slot-rules `author` row is empty on every channel by decision: no library type produces a portrait of a named individual, and generating a face to sit under a real byline is a disclosure decision rather than an image one.

## `comments.items.2.avatar` — author

- placement: comment thread avatar 3 of 7
- **out of library scope** — A portrait of a named person. The slot-rules `author` row is empty on every channel by decision: no library type produces a portrait of a named individual, and generating a face to sit under a real byline is a disclosure decision rather than an image one.

## `comments.items.3.avatar` — author

- placement: comment thread avatar 4 of 7
- **out of library scope** — A portrait of a named person. The slot-rules `author` row is empty on every channel by decision: no library type produces a portrait of a named individual, and generating a face to sit under a real byline is a disclosure decision rather than an image one.

## `comments.items.4.avatar` — author

- placement: comment thread avatar 5 of 7
- **out of library scope** — A portrait of a named person. The slot-rules `author` row is empty on every channel by decision: no library type produces a portrait of a named individual, and generating a face to sit under a real byline is a disclosure decision rather than an image one.

## `comments.items.5.avatar` — author

- placement: comment thread avatar 6 of 7
- **out of library scope** — A portrait of a named person. The slot-rules `author` row is empty on every channel by decision: no library type produces a portrait of a named individual, and generating a face to sit under a real byline is a disclosure decision rather than an image one.

## `comments.items.6.avatar` — author

- placement: comment thread avatar 7 of 7
- **out of library scope** — A portrait of a named person. The slot-rules `author` row is empty on every channel by decision: no library type produces a portrait of a named individual, and generating a face to sit under a real byline is a disclosure decision rather than an image one.


---
id: 02-cause-anatomy
step: 2
job: cause
device: anatomy
version: "1.5"
status: active
replaced_by: null
ratios: ["5:3", "16:9", "1:1"]
channels: [landing-page, marketplace, advertorial]
requires_product_photo: true
generation_mode: single-pass
variants: [diagnostic]
exempt_from: []
pairs_with: [01-pain-scene, 03-mechanism-ghostbody]
never_with: []
---

# 02-cause-anatomy

## PURPOSE
Indict a measurable cause in the customer's daily life (car seat, desk, mattress, tap
water) with a 2D illustration, and show the product as the thing that corrects it. The
culprit is on the left, the product doing its job is on the right, and one measured line
proves the difference. `--diagnostic` drops the product for the advertorial middle, where
the culprit is named before the product is revealed.

## TRIGGER
use_when: >
  Need to blame a specific object in the customer's everyday life and show its
  measurable harm mechanism. Placed after the pain image and before the product
  mechanism image; fits the middle of an advertorial. The paired dashed
  reference lines are the argument — use only when a measurable landmark exists.
avoid_when: >
  The problem has no internal structure to draw, or the cause cannot be pinned
  to one concrete object. Never as a main image.

## SKELETON
```
TYPE: 02-cause-anatomy v1.5 [+ --diagnostic]
MEDIUM: 2D illustration, [airbrushed / flat-vector]. NOT photography, NOT 3D.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the item in the RIGHT
panel. Preserve shape, proportions, material, finish and colour exactly.

[GROUND]
One continuous [low-chroma colour from the culprit's material world] field across
both panels, split by a single thin vertical line.
BASELINE: one horizontal line at the SAME height in both panels — the surface both
figures rest on and the datum everything is measured against. Nothing else is in
the background.

[BODY TREATMENT, both panels]
[anatomical structure] in warm ivory over a translucent body outline.
EXACTLY ONE figure per panel, same scale and viewing angle in both.

[PANELS — LEFT is wrong, RIGHT is correct]
LEFT: figure [wrong position] on [culprit, realistic, unbranded], the culprit
clearly visible where it acts on the body. [affected elements] red, a red curved
line tracing [wrong contour], a red dashed line at [landmark] in [state A], ONE
red double-headed arrow along [surface causing the problem], red X badge TOP
corner.
RIGHT: same figure [correct position] on the reference product, at THE SAME
interface as the culprit and comparable in size, exposed rather than housed.
[affected elements] blue, a soft blue aura along [correct contour], a blue dashed
line at the same [landmark] in [state B], green check badge TOP corner. Brighter
and cleaner than LEFT.

[MEASUREMENT RULE]
Two dashed reference lines, one per panel, at the identical landmark, identical
thickness, identical dash pattern, differing ONLY in [the one variable].
They are straight LINES, never boxes, brackets or outlines.
Both endpoints sit on structures the culprit does not move.

Colour follows G3 exactly: red wrong, blue correct, green badge, nothing else.
```

## SLOT CONSTRAINTS
- **Derive the look, do not choose it** (v1.2). The ground and the motifs come from the
  culprit object's own material world, which is already in the prompt and is different
  every time — so the diversity is a by-product of the argument rather than a taste call.
  Worked examples of the derivation: a single-strap bag gives warm sand with strap-weave
  and buckle motifs; a sagging mattress gives soft grey-green with foam-cell and quilting
  motifs; a high-heeled shoe gives cool graphite with shoe-last and heel-column motifs.
  Writing "choose a fitting style" instead would produce the model's default every time —
  abstract instruction has no picture, which this library has now proved twice.
- **The old pale-blue ground broke G3, which is why it had to go.** G3 makes blue mean
  "correct support, correct flow, working mechanism", so a pale blue canvas put the entire
  image inside the correct-side signal and the blue aura on the right had to fight a blue
  field to read. All three renders of 2026-08-12 show it: red carried easily because it was
  the only colour contrasting with the ground. The ivory structure layer stays exactly as
  it was — G3 assigns yellow to neutral structure, so that one was never a style choice.
- **Illustration STYLE is a named slot, not an axis** — SPEC §3.2 reserves axes for
  dimensions cutting across several types and this cuts across one, so it follows
  `02-symptom-rail`'s vignette-mode pattern and needs no vocabulary change. The three
  values, defined here rather than in the skeleton so a prompt only carries the name:
  `airbrushed` = soft gradients, modelled volume, textbook shading. `flat-vector` = flat
  fills, hard edges, no gradients. `line-engraving` = hatching and stipple carrying the
  form, colour as spot fills.
  Evidence: `airbrushed` has four renders behind it. `flat-vector` has none.
  **`line-engraving` is held OUT of the skeleton's list** (v1.4) after its only render
  failed — the style held and so did the ground and the signals, but the paired reference
  lines came back as dashed BOXES and took the argument with them. It is not withdrawn,
  because one failure is not the threshold; it is simply not offered by default, so it
  cannot be reached for by accident. The retest that would restore it changes ONLY the
  style value on a prompt already known to work, and checks one thing: whether the
  LINES-never-boxes wording added at 1.3 holds under hatching. That wording has since been
  confirmed on `airbrushed` — the 2026-08-12 insole render produced clean straight dashed
  lines where the previous one produced boxes.
  The MEDIUM is not part of this choice and cannot move — `anatomy` is the device and 2D
  illustration is what the device means.
- **The background motifs are gone, and a BASELINE takes their place** (v1.4). Owner
  report: the motif band carries no important information. True, and the type had admitted
  it — the old wording asked for motifs "at very low opacity", which is a way of saying they
  must not be noticed. Five renders confirmed the whole idea was decoration: hexagon mesh
  and medical crosses first, then shoe lasts and heel columns arranged as a footer border.
  What replaces them is the thing the argument actually lacked. This type claims a
  MEASURED difference, and across five renders the two panels never shared a datum: the
  left foot stood on an implied floor at one height and the right on a shoe sole at another,
  so "the heel raises you" had nothing to be measured against. One horizontal line at the
  same height in both panels supplies that, forces the panels into alignment, and costs one
  sentence. It is not decoration — remove it and the dashed pair loses its reference.
  If the owner later wants ticks along it, that would give the CHART mark family its first
  active host in the library, and it is a mark decision for the owner to write rather than
  something to add quietly here.
- **The product sits at the SAME interface as the culprit, at comparable size** (v1.4).
  Owner report: the insole was sometimes visible and sometimes not, and the comparison was
  lopsided. Both trace to one cause. The culprit is always a bold shaped object at the
  point where it acts — a heel wedge under the heel bone, a strap over a shoulder, a
  sagging surface under a hip. The product was being placed wherever it normally lives,
  which for an insole is INSIDE a shoe, so it rendered as a sliver of outline lost in
  another object while the heel opposite it read instantly. Asking for it "visibly carried"
  while also asking for it "fitted inside" was self-defeating.
  So: show the product exposed at the interface, at a size comparable to the culprit, even
  when real use would hide it. A foot resting ON a contoured insole mirrors a foot on a heel
  wedge; a foot in a shoe containing an insole does not.
- **The compared variable must be measurable AND independent of the pose the culprit
  forces** (v1.2, refinement of the NOTES hypothesis). Three renders on 2026-08-12 tested
  angle, distance and length one each. Angle isolated cleanly. Length did not: the line ran
  along the Achilles, whose lower endpoint sits on the heel bone, and the shoe tilts the
  heel bone — so length and angle moved together and neither read as the variable. Put both
  endpoints on structures the culprit leaves alone.
- Wrong on the LEFT, correct on the RIGHT — locked across the whole library. The
  original exemplar inverted this and misread at first glance; never copy that.
- Both panels carry a badge (X left, check right) — one unlabeled panel leaves the
  verdict dangling. **TOP corners** (v1.2): the mattress render put them at the bottom,
  which the old wording allowed by saying only "in the corner". `01-pain-split` has fixed
  top corners all along on the ground that the eye reads top-down and a bottom badge
  arrives after the verdict has already formed; this type now borrows that wording.
- The dashed reference lines carry the entire argument. Without them the image says
  "sitting curves your back", which everyone already knows.
- The culprit object is drawn realistically but unbranded.
- Strictest G3 compliance in the library; G4 and G5 apply in full.

## NEGATIVE
```
[G6] + photographic elements, 3D render, photorealistic skin, human face,
facial features, gore, wet tissue, correct side on the left,
both dashed lines identical, missing badge on either panel,
different figure scale between panels, extra signal colours, saturated ground,
anatomically wrong structures
```
Two tokens were DROPPED at v1.2 rather than rephrased. `cluttered motifs` qualified a noun
the canvas requires, and `extra colors` fought the derived ground now that the base is a
free colour — both are Rule 1a bleed shapes. The bounds live positively in the slots
instead: motifs "all at very low opacity", and the palette lock naming the three signals as
the only colours that may carry meaning. `both dashed lines at the same angle` became
`both dashed lines identical`, because angle is no longer always the compared variable.

## VARIANTS
### --diagnostic
The product leaves the frame: the right panel shows the corrected state reached by the
category rather than by the reference product ("no object, or a generic [supportive
object]"). This was the base behaviour until v1.3 and it has a real use — the advertorial
middle, where the culprit is indicted before the product is revealed, with
`03-mechanism-ghostbody` or a step-3 image carrying the product afterwards.
Diff vs base: `[PRODUCT REFERENCE]` is dropped, G1 is exempt because no product appears
(G1's own scope note), and `requires_product_photo` reads false for this variant.
- Use it only when a later image on the same page carries the product. Alone it argues
  "stop doing this" rather than "buy this", which is the fault that made the product the
  default at v1.3.
- Negative additions: `reference product in frame, branded remedy object`

## WORKED EXAMPLES
### example: shower-filter-hair-strand — skeleton@1.0, run: untested
Product: none in frame (G1-exempt) · ratio 5:3
- CANVAS — one continuous pale blue clinical gradient shared by both panels, divided by a single thin vertical line; low-opacity motifs: hexagon mesh, faint water-drop icons, an oversized ghosted hair cross-section watermark, a ghosted showerhead silhouette behind the left panel
- SUBJECT TREATMENT (both panels) — magnified longitudinal cross-section of ONE hair strand in warm ivory as the top layer, cuticle scales clearly defined, surrounding water reduced to a translucent glowing outline behind; same strand, scale and viewing angle both sides
- LEFT PANEL, WRONG — strand under untreated water, hard-water minerals as small angular crystals; cuticle scales lifted, splayed and chipped, highlighted red; red curved line tracing the roughened surface; red dashed reference line, JAGGED AND UNEVEN; red double-headed arrow showing scale accumulating; red X badge in the corner
- RIGHT PANEL, CORRECT — same strand under filtered water, no crystals; scales flat, closed, overlapping, highlighted blue; soft blue aura along the smooth surface; blue dashed reference line at the same position, SMOOTH AND EVEN; green check badge; brighter and cleaner than the left
- MEASUREMENT RULE — the paired dashed lines are the argument: identical position, thickness and dash pattern, differing only in how evenly they run
- PALETTE LOCK — pale blue and ivory throughout; red = damage, blue = healthy, green = confirmation badge, nothing else
Predicted failure: the exemplar's dashed lines differ by ANGLE (a clean binary the
model draws reliably); this test substitutes EVENNESS, a fuzzy variable — the two lines
will likely render identical and the argument collapses. See NOTES.

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
**The measurement hypothesis has been tested — result at v1.2.** It began as an untested
guess from the shower-filter stress test: the compared variable of the dashed reference
lines must be a measurable binary (angle, distance, length), never texture or evenness.
Three renders on 2026-08-12 took one variable each. Angle isolated cleanly and is the
safest of the three. Distance was inconclusive for an unrelated reason — the render put
four figures on the canvas instead of two, so the pair stopped being legible. Length
failed on its own terms and produced the refinement now in `[MEASUREMENT RULE]`: both
endpoints must sit on structures the culprit does not tilt, because a line's length and
its angle are visually coupled the moment one endpoint rides something the culprit moves.
Still open: whether `flat-vector` and `line-engraving` hold the same measurement discipline
as `airbrushed`. A hatched line is a weaker carrier of "identical dash pattern" than an
airbrushed one, so the paired lines are the first thing to check on those two styles.

Distinction from `03-mechanism-ghostbody`: 2D illustration vs 3D render; clinical blue
canvas vs infinite white; skeleton over body vs body over skeleton; the object in frame
is the **culprit**, not the product; the sentence is "this is what harms you", not
"this shape exists for a reason". The two may run in one gallery (02 then 03) but must
share one palette or they read as two sources.

## CHANGELOG
- 1.5 (2026-08-12): **the compression 1.4 promised and did not deliver.** The two panel
  blocks were near-identical in structure — each naming its colour, its contour line, its
  dashed line and its badge on separate lines — so they collapse into one `[PANELS]` block
  holding LEFT and RIGHT as two entries. Nothing about either panel changed; only the
  repeated scaffolding went. With the baseline sentence tightened too, the skeleton lands at
  1868 characters, against 1962 before this session began and 2822 at its worst.
  Every rule added from 1.2 to 1.4 survives intact: ground derived from the culprit, shared
  baseline, product at the culprit's interface, one figure per panel, top-corner badges,
  lines-never-boxes, and a G3 reference in place of a restatement.
  Recorded because it is the honest version of events. 1.2 grew the skeleton 44% while
  presenting itself as a tidy-up; 1.4 grew it again; this is the first entry that actually
  reduced it. Separately, 1.4's COMMIT MESSAGE claimed "1918 -> 1699 characters" — that
  number was wrong and the CHANGELOG entry in the file always held the correct 2027. The
  message is left as written rather than amended, since git history is this project's audit
  surface and hiding an error there is worse than showing its correction.
- 1.4 (2026-08-12): **the decorative background becomes a measuring datum, and the product
  stops hiding.** Three owner reports on the v1.3 insole render, all accepted.
  (1) The motif band carries no information. True, and the type had already admitted it by
  asking for motifs "at very low opacity" — a way of saying they must not be noticed. Five
  renders proved the whole idea decorative: hexagon mesh and medical crosses, then shoe
  lasts and heel columns arranged as a footer border. They are gone. **A BASELINE replaces
  them**: one horizontal line at the same height in both panels. Across all five renders
  the panels never shared a datum — the left foot stood on an implied floor at one height,
  the right on a shoe sole at another — so a type whose whole claim is a MEASURED difference
  had nothing to measure against. This is the opposite of decoration: remove it and the
  dashed pair loses its reference.
  (2) The insole was sometimes visible, sometimes not, and the comparison was lopsided.
  Both come from one cause. The culprit is always a bold shaped object at the point where it
  acts; the product was being placed wherever it normally lives, which for an insole is
  inside a shoe, so it rendered as a sliver lost in another object while the heel opposite
  read instantly. Asking for it "visibly carried" AND "fitted inside" was self-defeating.
  The right panel now requires the product at THE SAME interface as the culprit, at
  comparable size, exposed rather than housed.
  (3) Skeleton still too long. `PALETTE LOCK` is gone — two lines restating G3, which
  Rule 6 rule 2 forbids; one clause now references the rule instead. MEDIUM and STYLE merged
  into one line. `line-engraving` is held out of the offered list so it cannot be reached
  for by accident. Skeleton 1918 -> 2027 characters.
  Confirmed by this render and worth recording: the LINES-never-boxes wording added at 1.3
  worked. The previous render turned the dashed pair into boxes under `line-engraving`; this
  one produced clean straight dashed lines under `airbrushed`.
- 1.3 (2026-08-12): **the product becomes the thing on the right.** Owner report on the
  first v1.2 render: the image logic is not good because there is no comparison object that
  is the product. Correct, and it was the type's oldest assumption rather than an oversight.
  The right panel used to show "no object or [supportive object]", so every render argued
  "stop wearing heels" or "stop carrying that bag" and never "buy this". The base now puts
  the reference product in the right panel, visibly doing the correcting;
  `requires_product_photo` flips to true and the G1 exemption is dropped.
  The old product-free behaviour survives as **`--diagnostic`**, because it has a real use:
  the advertorial middle, where the culprit is indicted before the product is revealed and a
  later step-3 image carries the product. Its own note says what it costs - alone it argues
  stop-doing-this rather than buy-this.
  **Motifs are a field, not a sprinkle.** Owner report: the elements are placed carelessly
  in the ground. Confirmed in all four renders - mesh, crosses, shoe lasts and heel columns
  floating at unrelated sizes, some over the figures, some marooned. Deriving them from the
  culprit at v1.2 fixed WHAT they are and said nothing about WHERE they go, which was half a
  fix. They now form one continuous field anchored to a named edge, stopping where a figure
  begins.
  **Skeleton back under control.** Owner report: still long, still guiding style too much -
  and they were right, because v1.2 grew it from 1962 to 2822 characters while claiming to be
  a tidy-up. The three illustration-style DEFINITIONS moved to SLOT CONSTRAINTS so a prompt
  carries only the name; the palette reasoning went with them; the MEDIUM stopped explaining
  itself. Now 1918 characters, below where it started, with a product panel, a placement law
  and a style slot added since.
  **`line-engraving` is marked do-not-use pending a retest.** Its only render failed: the
  style held and the signals held, but the paired reference lines came back as dashed BOXES
  and took the argument with them. `[MEASUREMENT RULE]` now says the lines are straight
  lines, never boxes, brackets or outlines. If it fails a second time the value should be
  withdrawn rather than patched around.
- 1.2 (2026-08-12): **the design language stops being hard-coded.** Owner report after
  three renders: the elements are locked to one style and one colour scheme, with no
  diversity, and the fix should be a mechanism for reasoning about style rather than a
  fixed example. Three levels, all patched here.
  (1) `[CANVAS]` now DERIVES its ground and its 2-3 motifs from the culprit object's own
  material world - a source already in every prompt and different every time. The old text
  hard-coded a pale blue clinical gradient plus a hexagon mesh and medical cross icons, so
  every render of this type came out as the same picture with different anatomy. Deriving
  also retires the medical cross automatically, which was making a kitchen or a shoe look
  like hospital material.
  (2) The fixed palette becomes a FUNCTIONAL constraint: the base must be low-chroma, far
  in hue from both red and blue so neither signal fights it, and separated from the ivory
  structure layer by VALUE rather than only hue. That last clause matters - a warm sand
  ground would otherwise collide with ivory bone on the first render.
  The rule-based reason the old ground had to go, rather than a taste-based one: G3 makes
  blue mean correct support and working mechanism, so a pale blue canvas placed the whole
  image inside the correct-side signal, and all three renders show the right panel's blue
  aura fighting a blue field while red carried easily. The ivory structures are untouched -
  G3 assigns yellow to neutral structure, so those were never a style choice.
  (3) Illustration STYLE becomes a named slot with three values - `airbrushed`,
  `flat-vector`, `line-engraving` - chosen and stated in every prompt. A named slot rather
  than an axis, because SPEC §3.2 reserves axes for dimensions cutting across several types
  and this cuts across one; it follows `02-symptom-rail`'s vignette-mode pattern, so no
  vocabulary change was needed. Evidence status recorded in SLOT CONSTRAINTS: `airbrushed`
  has three passing renders, the other two have none and are the owner's design decision.
  The MEDIUM stays fixed, because `anatomy` is the device and 2D illustration is what the
  device means.
  Three smaller fixes from the same three renders: `[BODY TREATMENT]` now says EXACTLY ONE
  figure per panel (the mattress render stacked two rows per panel and the dashed pair
  stopped being legible); the badges move to TOP corners, borrowing `01-pain-split`'s
  wording and its reason (the mattress render put them at the bottom, which the old "in the
  corner" allowed); and `[MEASUREMENT RULE]` gains the refinement that both endpoints of
  the line must sit on structures the culprit does not tilt - the high-heel render measured
  along the Achilles, whose lower endpoint rides the tilted heel bone, so length and angle
  moved together and neither read as the variable.
  The `RATIO:` line goes, as it did from `01-pain-scene` 1.4 and `01-pain-split` 1.6:
  adapter Rule 4, 6/6 renders ignoring a written ratio.
- 1.1 (2026-08-11): channels gain `advertorial`. Self-contradiction: use_when already
  says the type "fits the middle of an advertorial" while the frontmatter excluded
  that channel. Frontmatter corrected to match the trigger.
- 1.0 (2026-08-10): initial from the car-seat spine exemplar; exemplar faults encoded
  (correct-side-left inversion, missing X badge). seed: conversation.md.

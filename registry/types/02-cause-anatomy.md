---
id: 02-cause-anatomy
step: 2
job: cause
device: anatomy
version: "1.3"
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
TYPE: 02-cause-anatomy v1.3 [+ --diagnostic]
MEDIUM: 2D illustration. NOT photography. NOT 3D render.
STYLE: [airbrushed / flat-vector / line-engraving] — name one.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the item in the RIGHT
panel. Preserve shape, proportions, material, finish and colour exactly.

[CANVAS]
One continuous ground across both panels, split by a single thin vertical line.
BASE: [low-chroma colour from the culprit's own material world].
MOTIFS: [2 motifs from that same world] as ONE continuous field at very low
opacity, anchored to [one edge] and stopping where a figure begins.

[BODY TREATMENT, both panels]
[anatomical structure] in warm ivory over a translucent body outline.
EXACTLY ONE figure per panel, same scale and viewing angle in both.

[LEFT PANEL: WRONG]
Figure [wrong position] in/on [culprit object, drawn realistically, unbranded].
[affected elements] red. A red curved line tracing [wrong contour].
A red dashed reference line at [landmark], [state A of the variable].
ONE red double-headed curved arrow along [surface causing the problem].
Red circle with white X, TOP corner.

[RIGHT PANEL: CORRECT]
Same figure [correct position], with the reference product [in place / worn /
supporting the structure] visibly doing the correcting.
[affected elements] blue. A soft blue aura along [correct contour].
A blue dashed reference line at the same [landmark], [state B of the variable].
Green circle with white check, TOP corner. Brighter and cleaner than the left.

[MEASUREMENT RULE]
Two dashed reference lines, one per panel, at the identical landmark, identical
thickness, identical dash pattern, differing ONLY in [the one variable].
They are straight LINES, never boxes, brackets or outlines.
Both endpoints sit on structures the culprit does not move.

PALETTE LOCK: red wrong, blue correct, green badge, and nothing else means
anything.
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
  Evidence: `airbrushed` has three passing renders. `flat-vector` has none.
  **`line-engraving` has one render and it FAILED** (2026-08-12, high heel) — the style
  held, the ground and signals held, and the paired reference lines came back as dashed
  BOXES rather than lines, which took the whole argument with them. Do not use it for this
  type again until the LINES-not-boxes wording has been tested on it; if it fails twice the
  value should be withdrawn rather than patched around.
  The MEDIUM is not part of this choice and cannot move — `anatomy` is the device and 2D
  illustration is what the device means.
- **Motifs are a field, not a sprinkle** (v1.3). Owner report: the elements sit around the
  ground carelessly. Confirmed in all four renders — mesh, crosses, shoe lasts and heel
  columns floated at unrelated sizes, some overlapping the figures, some marooned in dead
  space. Deriving them from the culprit at v1.2 changed WHAT they are and said nothing
  about WHERE they go, which was half a fix. They now form one continuous field, anchored
  to a named edge, confined to the ground outside the figures.
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

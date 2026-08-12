---
id: 02-cause-anatomy
step: 2
job: cause
device: anatomy
version: "1.7"
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
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a prompt.

```
TYPE: 02-cause-anatomy v1.7 [+ --diagnostic]
MEDIUM: 2D illustration, [style]. NOT photography, NOT 3D.    -> PARTS/style

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the item in the RIGHT
panel. Preserve shape, proportions, material, finish and colour exactly.

[GROUND]                                                      -> PARTS/ground
[BODY]                                                        -> PARTS/body
[PANELS] LEFT is wrong, RIGHT is correct.                     -> PARTS/panels

[MARKS] name each one used, with its count and its panel:     -> MARKS
  required: measure, verdict
  then 1-3 more that the argument actually needs
  nothing in the frame is marked that is not named here

Colour follows G3 exactly: red wrong, blue correct, green badge, nothing else.
```

## PARTS

**`style`** — one, named in the prompt. `airbrushed`: soft gradients, modelled volume,
textbook shading. `flat-vector`: flat fills, hard edges, no gradients. `line-engraving`
is held out — see KNOWN-FLAKY.

**`ground`** — one continuous field across both panels, split by a single thin vertical
line. Its colour is DERIVED from the culprit object's own material world: low-chroma, far
in hue from both red and blue so neither signal fights it, and separated from the ivory
structure layer by VALUE and not only by hue. Nothing else is in the background.

**`body`** — the relevant anatomical structure in warm ivory (G3: yellow = neutral
structure) over a translucent body outline. EXACTLY ONE figure per panel, same scale and
viewing angle in both.

**`panels`** — LEFT: the figure in the wrong position on the culprit, drawn realistically
and unbranded, the culprit clearly visible where it acts on the body. RIGHT: the same
figure in the correct position on the reference product, at THE SAME interface as the
culprit and comparable in size, exposed rather than housed. RIGHT is brighter and cleaner
than LEFT.

## MARKS

This type's own mark library. Marks are called by name from the skeleton. Every one obeys
G3 and carries a count. The `also in` notes exist so that a mark which looks the same in
another type stays visible from here — each type owns its own library, so drift is made
visible rather than centralised away.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `measure` | two dashed straight reference lines, one per panel | red left, blue right | exactly 2 | 4 renders |
| `verdict` | circle badge, X on the wrong panel and check on the correct one, TOP corners, flat and solid, same diameter | red X, green check | exactly 2 | 4 renders · also in `01-pain-split`, `03-mechanism-ghostbody`, `06-relief-hero` |
| `contour` | a curved line tracing a surface or an edge | red wrong, blue correct | 1 per panel | 4 renders |
| `aura` | a soft glow following a correct contour | blue only | 1, right panel | 3 renders |
| `fill` | the affected anatomical elements filled | red wrong, blue correct | as many as are affected | 4 renders |
| `force` | a double-headed curved arrow along the surface causing the problem | red only | exactly 1, left panel | 3 renders |
| `baseline` | one horizontal datum line at the SAME height in both panels — the surface both figures rest on | neutral, no signal colour | exactly 1, spanning both panels | **none** |
| `axis` | a straight construction line showing the alignment the body should hold, a plumb line through two named landmarks | neutral dashed, no signal colour | 1 per panel | **none** |
| `pressure` | a soft shaded area showing where load concentrates on a surface | red wrong, blue correct | 1 per panel | **none** |
| `range` | a shaded wedge between two limbs or two surfaces, showing the angle available | red wrong, blue correct | 1 per panel | **none** |

**`measure` carries the whole argument and has its own rule.** Both lines anchor to the
SAME two anatomical landmarks with identical thickness and dash pattern. Exactly ONE
property may differ — the line's angle, its length, or the gap it spans — and every other
property must read as identical. They are straight LINES, never boxes, brackets or
outlines. For an angle comparison the landmarks are expected to rotate; what must hold
still is length.

**Budget.** `measure` and `verdict` are required. Beyond them take 1–3 marks and no more:
this type's argument is one measurement, and a frame carrying six mark classes stops being
a measurement and becomes a diagram of everything.

## SLOT CONSTRAINTS
- Wrong on the LEFT, correct on the RIGHT — locked across the whole library.
- Both panels carry a `verdict` badge; one unlabelled panel leaves the verdict dangling.
- The culprit is drawn realistically but unbranded.
- Strictest G3 compliance in the library; G4 and G5 apply in full.
- `measure` only works where a measurable landmark exists. If the harm cannot be pinned to
  two anatomical points, this type is the wrong choice — see `avoid_when`.
- The four marks with no evidence are proposals, not proven instruments. The first render
  of each is its founding evidence and should be logged as such.

## NEGATIVE
```
[G6] + photographic elements, 3D render, photorealistic skin, human face,
facial features, gore, wet tissue, correct side on the left,
both dashed lines identical, missing badge on either panel,
different figure scale between panels, extra signal colours, saturated ground,
anatomically wrong structures, background pattern
```
Two tokens are deliberately absent because each would qualify a noun a prompt here
requires, which Rule 1a makes a bleed: `cluttered motifs` and `extra colors`. Their bounds
live positively in PARTS instead.

## VARIANTS
### --diagnostic
The product leaves the frame: the RIGHT panel shows the corrected state reached by the
category rather than by the reference product. This was the base behaviour until v1.3 and
it has a real use — the advertorial middle, where the culprit is indicted before the
product is revealed, with a later step-3 image carrying the product.
Diff vs base: `[PRODUCT REFERENCE]` is dropped, G1 is exempt because no product appears
(G1's own scope note), and `requires_product_photo` reads false for this variant.
- Use it only when a later image on the same page carries the product. Alone it argues
  "stop doing this" rather than "buy this", which is why the product became the default.
- Negative additions: `reference product in frame, branded remedy object`

## WORKED EXAMPLES
### example: shower-filter-hair-strand — skeleton@1.7, run: untested
Product: none in frame (`--diagnostic`) · ratio 5:3 · style airbrushed
- GROUND — pale mineral grey, derived from limescale, darker in value than the ivory
- BODY — one magnified hair strand per panel, cuticle scales in ivory over a translucent
  water outline, same strand and angle in both
- PANELS — LEFT: the strand under untreated water, angular mineral crystals lodged in
  lifted cuticle scales. RIGHT: the same strand under filtered water, scales flat and
  closed, no crystals
- MARKS — `measure` (2 lines across the same two scale roots, differing only in the gap
  they span), `verdict`, `contour` (1 per panel along the scale surface), `fill` (lifted
  scales red, closed scales blue)
Kept as the type's only `--diagnostic` example. Its earlier version compared the two lines
by EVENNESS, which the `measure` rule now forbids — evenness is not one of the three
permitted properties, and it is exactly the fault that rule was written to prevent.

## KNOWN-FLAKY
- **`line-engraving` style, 1/1 failed, 2026-08-12.** Its only render turned the `measure`
  pair into dashed BOXES rather than lines and took the argument with it. Held out of the
  offered `style` list — not withdrawn, since one failure is not the threshold, but not
  reachable by accident either. The retest changes ONLY the style value on a prompt already
  known to work and checks whether the straight-LINES wording holds under hatching. That
  wording has since been confirmed on `airbrushed`.

## NOTES
The measurement hypothesis is settled as far as one render each can settle it. Angle
isolates cleanly. Distance was inconclusive because a render put four figures on the
canvas instead of two. Length failed on its own terms and produced the one-property rule
now in MARKS. Open: whether `flat-vector` carries an identical dash pattern as reliably as
`airbrushed` does.

Distinction from `03-mechanism-ghostbody`: 2D illustration vs 3D render; the object in
frame is the CULPRIT, not the product's mechanism; the sentence is "this is what harms
you", not "this shape exists for a reason". The two may run in one gallery (02 then 03)
but must share one palette or they read as two sources.

## CHANGELOG
- 1.7 (2026-08-12): **restructured into a call-map plus two libraries, and the file
  cleaned.** Owner decision: each type gets its own mark library to call, rather than
  if/else inside the skeleton. `PARTS` holds the non-mark building blocks (style, ground,
  body, panels); `MARKS` holds this type's ten marks with form, colour, count and evidence
  status; the skeleton became a map naming them. Worth recording why the branches were
  never a context cost: `query/runbook.md` Step 5 already required every conditional to be
  resolved before a prompt ships, so no branch ever reached the model. What branches cost
  was correctness — two faults this session came from choosing a branch wrongly, not from
  leaked text — and naming them makes each choice a deliberate lookup.
  Four marks are carried with NO evidence: `baseline`, `axis`, `pressure`, `range`. They
  are labelled as proposals and the first render of each is its founding evidence.
  Cleanup in the same pass: SLOT CONSTRAINTS held 6681 characters of history and CHANGELOG
  10501, together 67% of a 25455-character file. Decisions stay here in compressed form,
  process errors stay in git history where the audit surface is, and SLOT CONSTRAINTS keeps
  only constraints. SPEC §3.3's optional-section list gains PARTS and MARKS in this diff.
- 1.6 (2026-08-12): `measure`'s rule rewritten. The v1.2 wording required both endpoints to
  sit on structures the culprit does not move, generalised from one failure, and it would
  have forbidden the render that PASSED — the shoulder-bag line ran acromion to acromion
  and the bag pulls one shoulder down, which was the variable itself. The rule now governs
  the line: same two landmarks, exactly one property differing.
- 1.5 (2026-08-12): the two parallel panel blocks collapsed into one. Skeleton 2027 → 1868.
- 1.4 (2026-08-12): background motifs removed, `baseline` datum put in their place. Owner
  report: the motif band carried no information — true, and the type had admitted it by
  asking for motifs "at very low opacity". Across five renders the panels never shared a
  datum, so a type claiming a MEASURED difference had nothing to measure against. Also: the
  product must sit at the SAME interface as the culprit, at comparable size, exposed rather
  than housed — an insole asked for "fitted inside" a shoe AND "visibly carried" cannot be
  both, and rendered as a sliver while the heel opposite it read instantly.
- 1.3 (2026-08-12): **the product became the thing on the right.** Owner report: no
  comparison object that is the product. The RIGHT panel used to read "no object or
  [supportive object]", so every render argued "stop wearing heels" and never "buy this".
  `requires_product_photo` → true, G1 exemption dropped, product-free form kept as
  `--diagnostic`. `measure` gained the straight-LINES-never-boxes wording after the
  `line-engraving` failure.
- 1.2 (2026-08-12): **the design language stopped being hard-coded.** Owner report: the
  elements were locked to one style and one colour scheme. Ground and motifs became DERIVED
  from the culprit's material world, the fixed palette became a functional constraint, and
  illustration style became a named choice. The rule-based reason the pale blue ground had
  to go: G3 makes blue mean correct support and working mechanism, so a blue canvas put the
  whole image inside the correct-side signal, and all three renders show the right panel's
  blue aura fighting a blue field. Ivory structures untouched — G3 assigns yellow to
  neutral structure. Badges moved to TOP corners, borrowing `01-pain-split`'s wording;
  `[BODY]` fixed at one figure per panel; the `RATIO:` line dropped per adapter Rule 4.
- 1.1 (2026-08-11): channels gain `advertorial`. Self-contradiction: use_when already said
  the type "fits the middle of an advertorial" while the frontmatter excluded that channel.
- 1.0 (2026-08-10): initial from the car-seat spine exemplar; exemplar faults encoded
  (correct-side-left inversion, missing X badge). seed: conversation.md.

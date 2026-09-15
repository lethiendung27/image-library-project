---
id: 02-cause-anatomy
step: 2
job: cause
device: anatomy
version: "1.18"
status: active
replaced_by: null
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
Indict a measurable cause in the customer's daily life (car seat, desk, mattress, tap water)
with a 2D illustration and show the product correcting it. Culprit left, product doing its job
right, and the body itself carrying the difference. `--diagnostic` drops the product for the
advertorial middle, where the culprit is named before the product is revealed.

## TRIGGER
use_when: >
  Need to blame a specific object in the customer's everyday life and show its measurable harm
  mechanism. Placed after the pain image and before the product mechanism image; fits the
  middle of an advertorial. The body's own change of state is the argument — use only when the
  product changes a POSITION of the body that can be drawn, a posture, an angle, a curve or
  where weight rests, and it reads with every mark covered. Never for a product whose benefit
  is less force or fatigue with the body held the same way.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 02-cause-anatomy v1.18 [+ --diagnostic]
MEDIUM: 2D illustration, [style]. NOT photography, NOT 3D.    -> PARTS/style

[PRODUCT REFERENCE] attached photo is the exact reference.
[FRAME]                                                       -> PARTS/frame
[GROUND] deep muted hue from the product's world, steps once. -> PARTS/ground
[BODY] only the named structures in ivory, rest an outline.   -> PARTS/body
[PANELS] LEFT is wrong, RIGHT is correct.                     -> PARTS/panels
[MARKS] one BADGE FORM, then 1-3 marks. Name count+panel.     -> MARKS

Colour is data (G3): red wrong, blue correct, green badge. Never write `G3` in a prompt.
```

## PARTS

**`style`** — one, named in the prompt. `airbrushed`: soft gradients, modelled volume.
`flat-vector`: flat fills, hard edges, no gradients. `line-engraving`: fine engraved lines and
cross-hatching, like an antique medical plate, every mark a flat solid fill — its fills stay
flat, but it drew cream paper for a named ground twice. **`ghost-mannequin`** (owner
instruction 2026-09-15): the figure is `03-mechanism-ghostbody`'s *SAME featureless matte white
mannequin in both panels, no face, no hair, no clothing, no skin tone*, drawn with soft even
shading as a 2D illustration, the named structures in warm ivory seen through one window with a
visible rim. Its counts there are provenance and it has 0 renders here; a head facing the
camera grew a face twice there, so show the back or side of the head. `paper-cut` is withdrawn
at 1.18.

**`frame`** — how much of the world is in shot. **`whole` is the only value: the entire body or
object in shot, the interface small within it.** `interface` and `macro` were withdrawn at 1.12
on 0 of 4: a crop to the contact removed the person and the product.

**`ground`** — one continuous field across both panels, same hue and chroma, **stepping once
in VALUE at the divider: one step lighter on the right.** The step is the only discontinuity;
nothing else is in the background.

A flat field never exceeded +5 of 255 in eleven renders; an unspent step never fell below
+17.6. `dark-field` is the working value: ground far below the ivory, separation 156–209 across
nineteen renders.

**The ground's hue comes from the product's world, deep and muted, with the reason written
down** (1.18, two owner findings of 2026-09-15). Take it from where the product is used — the
room, the floor, the season, the material — never from the product's own colour, so the product
separates. **Deep**: set 2's grounds named *deep* measured 43–79 of 255, set 3's named without
it came back at 158–246 on four of six. **Muted**, between the two ends the owner rejected: set
2's saturated fields, 0.36–0.87, read as bad and unscientific; set 3's greys, 0.00–0.15, read
as one colour for six products. **Nothing stands behind the subject but the ground**, which
held 6 of 6 once said.

**`body`** — **name the figure's orientation — on its back, on its front, on its side** — since
a reader in bed came back with the neck vertebrae drawn on the throat side, 1 render. The
structure in warm ivory (G3: yellow = neutral structure) over a translucent outline. EXACTLY
ONE figure per panel, same scale and view in both. Name the SUBJECT CLASS **and name what it is
not**: skeleton is this model's default for anatomy and it will substitute one unasked. **Say
which structures are drawn and that the rest is a grey outline**: *NOT a full skeleton* came
back as a full skeleton and a toothed skull, 2 of 6. Tooth and gum, hair shaft and cuticle,
skin layers, vein and valve, trachea and rings, follicle and scalp, bursa and sac all satisfy
the type.

**`panels`** — LEFT: the figure in the wrong position on the culprit, drawn realistically and
unbranded, the culprit visible where it acts. RIGHT: the same figure in the correct position
on the reference product, at THE SAME interface, comparable in size, exposed rather than
housed.

Three ways the comparison is lost, all observed: the structure drawn in one panel only, an
object that never touches it, and an object that covers it.

**The product must be recognisable AS THAT PRODUCT, and a person must be visible using it.**
Four of six renders on 2026-08-13 drew an anonymous grey sliver. Draw it at a size and angle
where its category is obvious, on a body part that is itself recognisable.

**Each panel states its cause, then its effect** (1.18): the object and the one property that
matters, what it does to the body, and — after *so* — the state the structure is left in. The
right panel changes only the object. **The state must read at `whole` framing**: both 1.15
passes changed a posture; the three cover-test failures changed a nostril, a gap and a line.
**And it must change in kind, not degree**: a deeper sway, a waist lifting and a shoulder
dropping came back unchanged, 3 of 3 on 2026-09-15.

**Show the feature the benefit comes through** (1.18, owner finding: four of six frames showed
the product and the body, not what the product did). The right panel names the part the body
meets — its knee pad, its grip, the pole tips — as a contact, which G2's *relation to other
objects* allows, and the mark sits AT that contact. A named part that redraws the product is a
G1 fault. **The comparison is the product's own logic, taken from its brief** (owner,
2026-09-15): the culprit from its competitor context, the feature and the benefit from its
feature lines, each quoted in the set table before a prompt is written.

## MARKS

This type's own mark library, called by name from the skeleton. Every mark obeys G3 and
carries a count. `also in` notes keep a same-looking mark in another type visible from here.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `verdict` | ONE of five badge forms — see BADGE FORMS below | red wrong, green correct | exactly 2, or 0 for `verdict-none` | 18 renders on the disc form · the other four are untested HERE |
| `contour` | a curved line drawn ON one named bounded edge, touching it | red wrong, blue correct | 1 per panel | 10 renders · 2026-09-15: floated off the body as the only difference |
| `fill` | the affected elements filled | red wrong, blue correct | as many as are affected | 9 renders · 2026-09-15: the same place in both panels, colour the only difference |
| `force` | a double-headed curved arrow along the surface causing the problem | red only | exactly 1, left panel | 7 renders · 2026-09-15: the one mark in five that served the comparison |
| `aura` | a soft glow following a correct contour | blue only | 1, right panel | 6 renders · 2026-09-15: stated no cost and no gain |
| `range` | a shaded wedge whose two sides lie along two named bones meeting at one joint | red wrong, blue correct | 1 per panel | 3 renders · 2026-09-15: unanchored, read as a beam of light |
| `baseline` | one horizontal datum line PER PANEL, both at the same height — never one line crossing the divider | neutral, no signal colour | exactly 2 | 1 of 1 respecified |
| `axis` | a construction line through two named landmarks, showing the alignment the body should hold | neutral dashed, no signal colour | 1 per panel | 1 render |
| `pressure` | a filled region bounded by the CONTACT SURFACE, as wide as the contact itself — never a line, never a glow along an edge | red wrong, blue correct | 1 per panel | 3 of 6 · working |
| `load` | an arrow tracing the path a weight takes, from where it starts to where it lands, both ends named | red where it lands on the body, blue where it lands on the product or the floor | 1 per panel | **proposal · 0 renders** · arrows held 2/2 on `06-relief-hero` when described by their endpoints — provenance only |

**Name a line's direction against the STRUCTURE, never the frame** — for `force`, `contour` and
`axis`. "Perpendicular to the corneal surface" holds however the model rotates the frame;
"straight down" does not, and two renders obeyed it into the wrong axis.

**BADGE FORMS — five, not one (ADR-043).** Name ONE per prompt; each is a drop-in `[BADGES]`
block.

- `verdict-glyph` — filled disc, glyph cut out: red X left, green check right.
- `verdict-thumb` — the same discs with thumbs cut out, written as **a flat pictogram, a solid
  silhouette, never a photographed or three-dimensional hand**.
- `verdict-hazard` — a FILLED red warning triangle left, green check disc right.
- `verdict-emoji` — angry face left, smiling face right; the least clinical form.
- `verdict-none` — no badge, stated as a block rather than omitted.

**Evidence here**: all five rendered by 2026-09-15.

**THE MARKS MUST NOT BE THE ONLY DIFFERENCE.** Cover the marks with a thumb: the panels must
still read as wrong and right. Three of six on 2026-08-26 failed — a head level in BOTH panels
with only the dashed line tilted, nostrils whose narrowing was invisible, a thigh-to-seat gap
the eye could not find. A mark across an unchanged body is a claim the body does not make.
Since 1.18 this is the admission test as well as the check: no line carries the argument, so
the body must.

**Marks on the same structure compete** — a wedge and a fill on one bone read as one mass.
Give every mark its own structure, or drop one.

**A mark answers ONE question, and asks it in both panels** (1.18, owner finding): where the
weight lands, how wide the contact is, which way a joint turns. Draw the answer on the SAME
named structure or path in each panel, the answers differing in place, width or direction,
never in colour alone. A one-sided mark shows what the culprit keeps doing. On 2026-09-15 only
that kind served the comparison, 1 of 5.

**Budget.** A `verdict` form is required; beyond it take 1–3 marks and no more. The argument is
one change of state, and six mark classes make it a diagram of everything.

**SET DIVERSITY LAW.** Images in one set must differ, on five levers:

| lever | legal values |
|---|---|
| `style` | `airbrushed`, `flat-vector`, `line-engraving`, `ghost-mannequin` |
| `ground` hue | from the product's world, deep and muted, never the product's own colour |
| `body` subject class | the widest lever the type owns (PARTS/body) |
| badge form | five (BADGE FORMS) |
| the 1–3 marks beside the badge | eight classes |

**No two images in a set share more than TWO of the five.** The set of six on 2026-08-26 held
all five constant and came back as one image made six times.

## SLOT CONSTRAINTS
- **The removal test, before anything else is written.** Take the culprit out of the LEFT
  panel: does the harmful state go with it? If yes the type applies — one structure in two
  states, switched by the product. If the state persists the image shows DAMAGE, and the RIGHT
  panel claims a repair the product cannot perform.
- **The admission gate: position, not effort** (owner, 2026-09-15). A product that sells less
  force with the hand held the same way — a trigger lock, a ratchet lock, a wider grip — gives
  the body nothing to draw: a hose clamp plier and a car wash trigger lock failed, a cord tool
  failed, a pen drew no benefit, and a steam cleaner was ruled out unrendered. Hand products
  that change a position rendered: the vertical mouse, the toe spacer. The rest fall to
  `03-use-sequence` or `03-spec-split`.
- **The prompt budget.** A clause earns its place only if a render failed without it. Ceiling:
  **~1800 characters.** Never in a prompt: the vertical split, a colour's derivation, any
  rationale, or the ID `G3`, which printed as a label once.
- Wrong on the LEFT, correct on the RIGHT — locked across the whole library.
- Both panels carry a `verdict` badge, or NEITHER does under `verdict-none`. What is
  forbidden is ONE: an unlabelled panel beside a labelled one leaves the verdict dangling.

- The culprit is drawn realistically but unbranded.
- Strictest G3 compliance in the library; G4 and G5 apply in full.
- The change of state reads in the body with every mark covered; a mark points at it and never
  supplies it.
- Unproven: `light-field` in its inverted form. `frame` has one value.

## NEGATIVE
```
[G6] + photographic elements, 3D render, photorealistic skin, human face,
facial features, gore, wet tissue, correct side on the left,
missing badge on either panel,
different figure scale between panels, extra signal colours, saturated ground,
anatomically wrong structures, background pattern
```
Canonical and model-agnostic; the adapter drops from it at render time. `cluttered motifs` and
`extra colors` are absent as Rule 1a bleeds; `extra signal colours`, `background pattern` and
`human face` are dropped from the rendered `avoid` line rather than rephrased when a prompt
needs those words.

## VARIANTS
### --diagnostic
The product leaves the frame: the RIGHT panel shows the corrected state reached by the
CATEGORY, not by the reference product. Base behaviour until v1.3; its use is the advertorial
middle, the culprit indicted before the product is revealed.
Diff vs base: `[PRODUCT REFERENCE]` dropped, G1 exempt (its own scope note),
`requires_product_photo` false.
- Use only when a later image on the same page carries the product. Alone it argues "stop
  doing this" rather than "buy this", which is why the product became the default.
- Fill sketch: a magnified hair strand per panel, cuticle scales in ivory over a translucent
  water outline, same strand and angle in both; LEFT untreated with mineral crystals in lifted
  scales, RIGHT filtered with scales flat. This exact case FAILS the removal test — a filter
  does not close a lifted scale — so a `--diagnostic` fill needs a switchable state like any
  other.
- Negative additions: `reference product in frame, branded remedy object`

## WORKED EXAMPLES
Both are renders that happened, kept in full because that text is the only record of what
actually drew (SPEC §3.3). Both are `partial`, and their remaining faults are named — an
example is a demonstration of the type working, not a claim of perfection. **Both carry
`measure` and `paper-cut`, both withdrawn at 1.18**: take FRAME, GROUND, BODY, PANELS and the
badge from them, and neither the style nor the `measure` block.

### example: postpartum-support-band — skeleton@1.11, run: partial
Fault on the render: the band covered the lower half of the muscle gap it was closing.
Everything else held, and this is the render where `measure` first carried its own
difference unaided in twenty-one attempts.
```
TYPE: 02-cause-anatomy v1.11
MEDIUM: 2D illustration, paper-cut. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the postpartum support
band in the RIGHT panel.

FRAME: the whole torso from ribs to hips is in shot, the muscle gap small within it.
GROUND: deep desaturated olive, the right half one step lighter than the left.
BODY: the two vertical rectus abdominis muscles and the linea alba between them, cut as
separate paper layers in warm ivory over a translucent torso outline, seen from the
front. NOT a skeleton, NOT a ribcage. Exactly one torso in EACH panel, same scale and
view.

PANELS. LEFT: the bare torso unsupported, the two muscle bellies pulled apart and the
linea alba between them stretched wide and slack. RIGHT: the reference band fastened
across the same torso at the same height, touching the skin over the gap, the two
bellies drawn back toward each other and the linea alba narrow. The band must not cover
the gap it is closing.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each PERPENDICULAR TO THE INNER
  BORDER OF THE RIGHT-HAND MUSCLE, running across to the inner border of the left-hand
  muscle and STOPPING at both. Both sit at the same height on the torso, at the same
  place in their panel. Identical thickness and dash. One property differs: the gap -
  wide on the left, narrow on the right. Red left, blue right. Straight lines, not boxes.
- verdict: filled solid discs, red with a white X in the left panel's TOP corner, green
  with a white check in the right panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else.

Strictly avoid: text, numbers, letters, watermark, photographic elements, 3D render,
human face, gore.
```

### example: patellar-knee-brace — skeleton@1.13, run: partial
Fault on the render: the leg read as a translucent grey band rather than a recognisable
leg. The measure pair is the clearest this type has produced — a long red span against a
short blue one, identical in form and at the same height — and `paper-cut` renders cleanly
at two marks.
```
TYPE: 02-cause-anatomy v1.13
MEDIUM: 2D illustration, paper-cut. NOT photography, NOT 3D.

PRODUCT REFERENCE: the attached photo is the exact reference for the patellar tracking
knee brace in the RIGHT panel.

FRAME: the whole leg from mid-thigh to mid-shin, seen from the front.
GROUND: deep charcoal violet, the right half one step lighter than the left.
BODY: the kneecap and the shallow groove in the thigh bone that it rides in, cut as
separate paper layers in warm ivory over a translucent leg outline. NOT a full skeleton.
Exactly one leg in EACH panel, same scale and same front view.

PANELS. LEFT: the bare unsupported knee, the kneecap slid outward so it sits off the
groove, its inner edge standing clear of the groove's inner ridge. RIGHT: the reference
brace worn on the same knee, its open kneecap ring, straps and hinges clearly visible and
reading as the product itself, the kneecap held back in the groove with its inner edge
against the ridge. The brace's opening leaves the kneecap and the groove visible in full.

MARKS, two, nothing else marked:
- measure: two dashed straight lines, one per panel, each PERPENDICULAR TO THE INNER
  RIDGE OF THE GROOVE, running from that ridge across to the inner edge of the kneecap
  and STOPPING at both. Both begin at the same point on the ridge, at the same place in
  their panel. Identical thickness and dash. One property differs: the gap - wide on the
  left, closed to almost nothing on the right. Red left, blue right. Straight lines, not
  boxes.
- verdict: filled solid discs, red with a white X in the left panel's TOP corner, green
  with a white check in the right panel's. Same diameter, not rings.

G3: red wrong, blue correct, green badge, nothing else.

Strictly avoid: text, numbers, letters, watermark, photographic elements, 3D render, gore.
```

## KNOWN-FLAKY
- **`measure`, WITHDRAWN at 1.18 on owner instruction.** 30 renders; it carried its own
  difference in 4. Both worked examples keep it as the record of what drew.
- **`paper-cut`, WITHDRAWN at 1.18 on owner instruction.** It degraded every mark around it on
  its first outing and held clean only at two marks. Both worked examples are drawn in it.
- **A roll-out drawn as one pose in both panels, 1 render** (2026-09-15): the marks became the
  only difference.
- **A `flat-vector` figure drawn as a person with skin, hair and a face, 1 of 2** (2026-09-15).
- **The product drawn as another category, 1 render** (2026-09-15): a ring massager as a
  posture brace.
- **Badges inside G10, 3 of 14** (2026-09-15, sets 1–3), whether in a named corner or above the
  figure.
- **The reference product missing from the right panel, 1 render** (2026-09-15, cord tool).
- **A mark drawn twice where one was asked** (2026-09-15): three frames in set 2, the dog ramp
  in set 4, the pump and the robot in set 6.
- **A product in a signal hue, 7 of 11** (sets 2 and 6): navy, red trim, an orange knob, blue
  hoses, a green hose.
- **A named ground displaced, 3 renders** (set 6): a light hue name stayed pale under *deep*; a
  white wall and a hedge band took its place.
- **A ground named without *deep* came back pale, 4 of 6** (2026-09-15, set 3): 158–246 of 255.
- **`line-engraving` drew cream paper for the named ground, 2 of 7** since 1.18, and its step
  went flat both times.
- **The ground step inverted, 1 render** (2026-09-15, mattress topper).
- **A `contour` on the lower back floated off the body, 2 of 2**; on the neck it held 1 of 2.
- **`ghost-mannequin` drew no rimmed window, 4 of 4**; the bones showed through, and read.
- **`range` drawn as a cone or a free triangle, 2 of 3**; on the toe bones it held.
- **`frame` values `interface` and `macro`, WITHDRAWN at 1.12 on 0 of 4.** See `frame`.
- **`light-field` in its 1.8 form, withdrawn at 1.9 on 0 of 2**; returns inverted at 1.14 as a
  proposal.
- **`verdict` badges drifting to OUTLINE, 2 of 6.** The mark's form line now names the filled
  disc, which is what fixed `contour`'s count.
- **Exact counts on `contour`, 4 observations across 8 renders.** Restating a count did not
  bind it; naming ONE bounded structure did.
- **Canvas duplicated into a 2×2 grid, 2 observations.** Recorded as model behaviour in
  `adapters/nano-banana.md` Rule 4.
- **The ground step came back FLAT once in six, 2026-08-26.** 0.5 right-minus-left against
  13.5-26.1 on the five that obeyed, all six carrying the step clause in identical words — so
  wording was not the variable. That frame is also the one whose product vanished. When the
  product is dark, say so and give it the lighter panel.
- **`line-engraving`, 1 fail then 2 clean.** Its failure turned a dashed `measure` pair into
  boxes (1.2); on 2026-09-15 both its fills stayed flat. Give it filled marks, not lines.

## NOTES

Distinction from `03-mechanism-ghostbody`: 2D illustration vs 3D render; the object in frame
is the CULPRIT, not the product's mechanism; the sentence is "this is what harms you", not
"this shape exists for a reason". The two may run in one gallery (02 then 03) but must share
one palette or they read as two sources.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.18 (2026-09-15): **`measure` and `paper-cut` withdrawn; cause then effect; a mark answers
  one question at the feature; the comparison comes from the product's brief; an admission gate
  of position, not effort; the ground deep, muted, from the product's world; `ghost-mannequin`
  added.** Owner instructions and findings over six sets, 28 records.
- 1.17 (2026-08-26): **fixes a contradiction 1.16 introduced.** `verdict-none` legalised a frame
  with no badge while SLOT CONSTRAINTS still required one on both panels and NEGATIVE still
  banned a missing badge. Caught before a prompt was written against it. · this commit
- 1.16 (2026-08-26): `verdict` becomes five badge forms (ADR-043); a set diversity law; a cover
  test, failed 3 of 6. `ba4bc33`
- 1.15 (2026-08-13): type passed by the owner; file finalised. Worked examples become two
  renders that happened, in full text per SPEC §3.3; the untested shower-filter example is
  retired for failing the removal test and survives as a sketch in VARIANTS. `c6e3b77`
- 1.14 (2026-08-13): the whole-frame formula holds — 6 of 6 renders show a product a buyer
  could name. `light-field` returns as a proposal in an inverted form, structures in deep
  ochre. 6 records. `01e3b08`
- 1.13 (2026-08-13): ground colour is unrestricted, owner decision after six green
  backgrounds. The VALUE rule behind `dark-field` stays. `ef71a87`
- 1.12 (2026-08-13): `frame`'s two tight values withdrawn at 0 of 4 — cropping to the contact
  removes the person and the product. The v1.9 hue rule was a logical error, leaving only
  green, which is G3's third signal. The product must be recognisable AS that product.
  6 records. `a366726`
- 1.11 (2026-08-13): compressed, `frame` added, and a prompt budget written — a clause earns
  its place only if a render has failed without it. `1eaf62a`
- 1.10 (2026-08-13): the ground step confirmed at 5 of 6; `pressure` drew on the contact
  surface. 6 records. `fe9b92c`, corrected by `c46b357`
- 1.9 (2026-08-13): the REMOVAL TEST added as the first admission gate; `ground` gains the
  value step at the divider; `light-field` withdrawn at 0 of 2. 3 records. `5448936`
- 1.8 (2026-08-12): five renders of the MARKS library. `axis` and `range` became instruments,
  `pressure` drifted, `baseline` failed 0 of 2 and was respecified, `body` gained a named
  SUBJECT CLASS. `ebfceb4`
- 1.7 (2026-08-12): restructured into a call-map plus PARTS and MARKS (ADR-012); file
  25455 → 14171, skeleton 1926 → 966. `ba327d4`
- 1.6 (2026-08-12): `measure`'s rule rewritten to govern the LINE — same two landmarks, exactly
  one property differing. The v1.2 wording would have forbidden a render that passed.
  `2d14683`
- 1.5 (2026-08-12): the two parallel panel blocks collapsed into one. `16c3639`
- 1.4 (2026-08-12): background motifs removed and the `baseline` datum put in their place; the
  product must sit at the SAME interface as the culprit, comparable in size. `56528bd`
- 1.3 (2026-08-12): the product became the thing on the right; `requires_product_photo` → true,
  the product-free form kept as `--diagnostic`. `a6279ce`
- 1.2 (2026-08-12): the design language stopped being hard-coded — ground derived from the
  culprit's world, style a named choice, badges to TOP corners, `RATIO:` dropped per adapter
  Rule 4. `f1c9b6a`
- 1.1 (2026-08-11): channels gain `advertorial`, resolving a contradiction with use_when.
- 1.0 (2026-08-10): initial from the car-seat spine exemplar; exemplar faults encoded
  (correct-side-left inversion, missing X badge). seed: conversation.md.

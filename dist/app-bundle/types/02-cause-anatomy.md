---
id: 02-cause-anatomy
step: 2
job: cause
device: anatomy
version: "1.15"
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
  to one concrete object, or the harm PERSISTS after the culprit is taken away.
  Accumulated damage — a receded gum, a lifted hair cuticle — is not a state the
  product switches, and two panels claiming it is will claim a repair the product
  cannot make. Never as a main image.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 02-cause-anatomy v1.15 [+ --diagnostic]
MEDIUM: 2D illustration, [style]. NOT photography, NOT 3D.    -> PARTS/style

[PRODUCT REFERENCE] attached photo is the exact reference.
[FRAME]                                                       -> PARTS/frame
[GROUND] dark-field, value steps once at the divider.         -> PARTS/ground
[BODY] name the subject class, and what it is not.            -> PARTS/body
[PANELS] LEFT is wrong, RIGHT is correct.                     -> PARTS/panels
[MARKS] measure + verdict, then 1-3 more. Name count and panel. -> MARKS

Colour follows G3 exactly: red wrong, blue correct, green badge, nothing else.
```

## PARTS

**`style`** — one, named in the prompt. `airbrushed`: soft gradients, modelled volume.
`flat-vector`: flat fills, hard edges, no gradients; it holds the `measure` dash pattern.
`paper-cut`: flat layered shapes with soft drop shadows; renders convincingly but degraded
every mark around it on its first outing, so it is restricted to frames carrying `measure`
and `verdict` only. `line-engraving` is held out — see KNOWN-FLAKY.

**`frame`** — how much of the world is in shot. **`whole` is the only value: the entire body
or object in shot, the interface small within it.** `interface` and `macro` were proposed at
1.11 and WITHDRAWN at 1.12 on 0 of 4 — see KNOWN-FLAKY.

The withdrawal is the type's sharpest lesson so far, because the two tight values did exactly
what they were told and that is what broke the images. Crop to the contact and the hand, the
bicycle and the person go with it; what is left is a tissue cross-section with an anonymous
shape entering from the edge. A frame that cannot show a person using the product cannot
serve a type whose PURPOSE is to show the product doing its job. `whole` was 2 of 2 and
produced the strongest render this type has made.

**`ground`** — one continuous field across both panels, same hue and chroma, **stepping once
in VALUE at the divider: one step lighter on the right.** The step is the only discontinuity;
nothing else is in the background.

The step is not decoration — it is the only way this type's RIGHT-brighter requirement can be
met, and the two rules were in silent conflict until measured. Across eleven renders the
groups do not overlap: a flat field never exceeded +5 of 255, a step whose brightness the
right panel's own content ate back reached +2.2, an unspent step never fell below +17.6. So:
step the field, and do not let the right panel's content spend it.

`dark-field` is the working value — ground far below the ivory in value, structures the
lightest thing in frame, separation 156–209 across nineteen renders. `light-field` returns at
1.14 as a PROPOSAL in an inverted form, the structures dropping to a deep ochre so the two
layers separate; its 1.8 version failed 0 of 2 by leaving both layers light. On a pale field
the RIGHT-brighter step has little headroom, so the correct side must earn its difference
through cleaner structure instead.

**Colour is free.** Owner decision at 1.13: pick what suits the product, no rule about which
hues to avoid. The v1.9 exclusion rule required a hue far from red, blue and warm ivory, which
leaves the green band and nothing else — and green is G3's third signal — so it drove the
ground into a signal colour and produced six green backgrounds in a row. What survives is the
VALUE rule above, not a colour rule. Craft note, not a rule: a ground under a mark of its own
colour is a judgement per image; legislating hue is what caused the detour.


**`body`** — the structure in warm ivory (G3: yellow = neutral structure) over a translucent
outline. EXACTLY ONE figure per panel, same scale and view in both. Name the SUBJECT CLASS
**and name what it is not**: skeleton is this model's default for anatomy and it will
substitute one unasked. Tooth and gum, hair shaft and cuticle, skin layers, vein and valve,
trachea and rings, follicle and scalp, bursa and sac all satisfy the type.

Subject class is the widest diversity lever the type owns. G3 fixes the marks and fixes the
body's ivory, so colour cannot carry variety; what is drawn can. Confirmed: the strongest
renders this type has produced are the ones that left the skeleton behind.

**`panels`** — LEFT: the figure in the wrong position on the culprit, drawn realistically and
unbranded, the culprit visible where it acts. RIGHT: the same figure in the correct position
on the reference product, at THE SAME interface, comparable in size, exposed rather than
housed.

Three ways the comparison is lost, all observed:

- the structure under argument is drawn in ONE panel only — say it appears in both;
- an object does not touch the structure, so it acts on nothing — state the contact;
- an object covers the structure, hiding the evidence on the very panel meant to prove the
  case — state that neither may cover it.

**The product must be recognisable AS THAT PRODUCT, and a person must be visible using it.**
Four of six renders on 2026-08-13 drew the product as an anonymous grey sliver or beige
cylinder; two of those had no body left in frame at all. A viewer who cannot name the object
cannot be sold it, and v1.3 already fixed this fault once from the other direction — the
product has shrunk back to nothing while the anatomy and the marks grew to fill the frame.
Draw it at a size and angle where its category is obvious, worn or held on a body part that is
itself recognisable.

## MARKS

This type's own mark library, called by name from the skeleton. Every mark obeys G3 and
carries a count. `also in` notes keep a same-looking mark in another type visible from here.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `measure` | two dashed straight lines, one per panel, each STOPPING at its two landmarks | red left, blue right | exactly 2 | 30 renders · carried its own difference in 4, all since 1.12 |
| `verdict` | badge, a FILLED SOLID DISC with the glyph cut out of it, TOP corners, same diameter | red X, green check | exactly 2 | 18 renders · also in `01-pain-split`, `03-mechanism-ghostbody`, `06-relief-hero` |
| `contour` | a curved line tracing ONE named bounded edge | red wrong, blue correct | 1 per panel | 9 renders |
| `fill` | the affected elements filled | red wrong, blue correct | as many as are affected | 8 renders |
| `force` | a double-headed curved arrow along the surface causing the problem | red only | exactly 1, left panel | 6 renders |
| `aura` | a soft glow following a correct contour | blue only | 1, right panel | 5 renders |
| `range` | a shaded wedge between two limbs or surfaces, showing the angle available | red wrong, blue correct | 1 per panel | 2 renders |
| `baseline` | one horizontal datum line PER PANEL, both at the same height — never one line crossing the divider | neutral, no signal colour | exactly 2 | 1 of 1 respecified |
| `axis` | a construction line through two named landmarks, showing the alignment the body should hold | neutral dashed, no signal colour | 1 per panel | 1 render |
| `pressure` | a filled region bounded by the CONTACT SURFACE, as wide as the contact itself — never a line, never a glow along an edge | red wrong, blue correct | 1 per panel | 3 of 6 · working |

**`measure` carries the whole argument and has its own rule.** Both lines anchor to the SAME
two landmarks, identical in thickness and dash pattern. Exactly ONE property may differ —
angle, length, or the gap spanned — and every other property reads as identical. Straight
LINES, never boxes or brackets. For an angle comparison the landmarks rotate; length holds.

Four clauses added by failure, each of which cost a render:

1. **Each line STOPS at its landmarks** and runs past neither. Two pairs were drawn across
   the whole panel and measured nothing.
2. **Name the direction against the STRUCTURE, never the frame.** "Perpendicular to the
   corneal surface" holds however the model rotates the frame; "straight down" does not, and
   two renders obeyed it into the wrong axis.
3. **Both lines start from corresponding points at the same place in their panel**, so the
   pair reads as a pair.
4. **Admission — use `measure` only where the real difference is at least 2:1.** In 18
   renders the pair has never carried the argument by itself; part of that is the faults
   above, and part is that a dashed line cannot show a 20% difference to a scrolling reader.
   Below 2:1, pick another landmark pair or another type. Same shape of decision as the
   removal test.

**Marks on the same structure compete** — a wedge and a fill on one bone read as one mass.
Give every mark its own structure, or drop one.

**Budget.** `measure` and `verdict` are required; beyond them take 1–3 and no more. This
type's argument is one measurement, and six mark classes make it a diagram of everything.

## SLOT CONSTRAINTS
- **The removal test, before anything else is written.** Take the culprit out of the LEFT
  panel: does the harmful state go with it? If yes, the type applies — two panels are one
  structure in two states and the product switches between them now. If the state persists,
  the image shows DAMAGE, not a mechanism, and the RIGHT panel will claim a repair the
  product cannot perform.
- **The prompt budget.** A clause earns its place in a rendered prompt only if a render
  has failed without it. Everything else is a rule for the writer and stays in this file.
  Ceiling, measured rather than guessed: **~1800 characters at two marks, ~2050 at three** —
  what three prompts came to once every clause in them had been earned, the third being
  larger only because `pressure` carries a long form definition. Four earlier sets ran 2321,
  2731, 2884 then 3330 characters as versions accumulated, against adapter Rule 6's
  instruction to re-read anything past 2500. Each version restated more of this file into the
  prompt, and none of the added prose was ever tested for whether it did anything.
  Never in a prompt, because 14+ renders have never failed on it: the panels being split by a
  vertical line, the ground being one continuous field, the ground's low chroma, the material
  a colour was derived from, the structures reading as the lightest thing in frame. Name the
  colour, not its derivation.
  Never in a prompt because the model cannot act on it: anything about spending the ground
  step, and any rationale clause ("so the pair can be read against each other"). Those are
  choices the writer makes when picking the product, the pose and the palette.
- Wrong on the LEFT, correct on the RIGHT — locked across the whole library.
- Both panels carry a `verdict` badge; one unlabelled panel leaves the verdict dangling.
- The culprit is drawn realistically but unbranded.
- Strictest G3 compliance in the library; G4 and G5 apply in full.
- `measure` needs a measurable landmark pair, and a difference of at least 2:1 between them.
- Unproven: `light-field` in its inverted form. `paper-cut` is working at three clean renders,
  restricted to two marks. `frame` has one value.
- Wide ratios are a canvas risk on wide-and-short content — see KNOWN-FLAKY.

## NEGATIVE
```
[G6] + photographic elements, 3D render, photorealistic skin, human face,
facial features, gore, wet tissue, correct side on the left,
both dashed lines identical, missing badge on either panel,
different figure scale between panels, extra signal colours, saturated ground,
anatomically wrong structures, background pattern
```
This list is canonical and model-agnostic; the adapter drops from it at render time. Two
tokens are deliberately absent because each would qualify a noun a prompt here requires,
which Rule 1a makes a bleed: `cluttered motifs` and `extra colors`. Note that `extra signal
colours`, `background pattern` and `human face` above are all Rule 1a bleeds when a prompt
needs those words, and are dropped from the rendered `avoid` line rather than rephrased.

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
- Fill sketch, since the variant no longer holds a worked-example slot: a magnified hair
  strand per panel, cuticle scales in ivory over a translucent water outline, the same
  strand and angle in both; LEFT under untreated water with mineral crystals lodged in
  lifted scales, RIGHT under filtered water with scales flat and closed. Note before using
  it that this exact case FAILS the removal test — a filter does not close a scale that is
  already lifted — so a `--diagnostic` fill needs a switchable state like any other.
- Negative additions: `reference product in frame, branded remedy object`

## WORKED EXAMPLES
Both are renders that happened, kept in full because that text is the only record of what
actually drew (SPEC §3.3). Both are `partial`, and their remaining faults are named — an
example is a demonstration of the type working, not a claim of perfection.

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
- **`frame` values `interface` and `macro`, WITHDRAWN at 1.12 on 0 of 4.** Both cropped the
  person and the product out of the frame — a hand and a bicycle gone, a mouthpiece reduced to
  a sliver. `whole` stands at 2 of 2.
- **`light-field` in its 1.8 form, withdrawn at 1.9 on 0 of 2.** Ground-to-ivory separation of
  5 and 8 against dark-field's 178, and a pale ground left no headroom for the RIGHT-brighter
  law. Returns inverted at 1.14.
- **`verdict` badges drifting to OUTLINE, 2 of 6.** The mark's form line now names the filled
  disc, which is what fixed `contour`'s count.
- **Exact counts on `measure` and `contour`, 4 observations across 8 renders.** Restating a
  count inside a prompt did not bind it; naming ONE bounded structure did.
- **Canvas duplicated into a 2×2 grid, 2 observations.** Both instances asked for a WIDE ratio
  on wide-and-short content while every render returned 1024×1024 square. Compose
  wide-and-short subjects to fill a square frame.
- **`line-engraving` style, 1/1 failed.** Turned the `measure` pair into dashed BOXES. Held out;
  a retest changes ONLY the style value on a prompt already known to work.

## NOTES
The measurement hypothesis is as settled as one render each can settle it: angle isolates
cleanly, distance was inconclusive, length failed and produced the one-property rule.
`flat-vector` carries the dashed pair as reliably as `airbrushed`.

**Why this type renders as the same image every time.** Mostly legislated, not careless: G3
fixes the marks at red, blue and green and fixes the body at warm ivory, and `ground` must
then avoid red, blue and warm alike. Colour is close to fully determined and cannot carry
variety. Two levers can. SUBJECT CLASS is proven — the non-skeletal subjects produced the
strongest renders. FRAME is proposed and untried, and is the more promising of the two,
because three style values changed technique while every render kept the same composition:
two equal panels, badges in the top corners, the structure centred at middle distance.

Distinction from `03-mechanism-ghostbody`: 2D illustration vs 3D render; the object in frame
is the CULPRIT, not the product's mechanism; the sentence is "this is what harms you", not
"this shape exists for a reason". The two may run in one gallery (02 then 03) but must share
one palette or they read as two sources.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
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
- 1.10 (2026-08-13): the ground step confirmed at 5 of 6 and now the file's most reliable
  rule; `pressure` drew at last on the CONTACT SURFACE respecification; `measure` admitted to
  have never carried its own difference in 18 renders, and given four clauses. 6 records.
  `fe9b92c`, corrected by `c46b357`
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

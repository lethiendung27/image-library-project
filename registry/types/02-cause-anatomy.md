---
id: 02-cause-anatomy
step: 2
job: cause
device: anatomy
version: "1.9"
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
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a prompt.

```
TYPE: 02-cause-anatomy v1.9 [+ --diagnostic]
MEDIUM: 2D illustration, [style]. NOT photography, NOT 3D.    -> PARTS/style

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the item in the RIGHT
panel. Preserve shape, proportions, material, finish and colour exactly.

[GROUND] dark-field; the value steps once at the divider.     -> PARTS/ground
[BODY] name the subject class first.                          -> PARTS/body
[REMOVAL TEST] passes, or this is the wrong type.             -> SLOT CONSTRAINTS
[PANELS] LEFT is wrong, RIGHT is correct.                     -> PARTS/panels

[MARKS] name each one used, with its count and its panel:     -> MARKS
  required: measure, verdict
  then 1-3 more that the argument actually needs
  nothing in the frame is marked that is not named here

Colour follows G3 exactly: red wrong, blue correct, green badge, nothing else.
```

## PARTS

**`style`** — one, named in the prompt. `airbrushed`: soft gradients, modelled volume,
textbook shading. `flat-vector`: flat fills, hard edges, no gradients — it carried the
`measure` dash pattern on both renders that used it, which answers the question NOTES had
left open. `paper-cut`: flat layered shapes with soft drop shadows, hard edges throughout.
One render, and it split — the STYLE came back convincingly, scales as separate cut layers
with cast shadows and unmistakably distinct from the other two values, while every mark in
the same frame degraded at once (measure and contour counts wrong, fill delivered on one
side only). Recorded as visually successful and mark-hostile pending a second run on a
prompt whose argument is sound; do not use it yet for a frame carrying more than
`measure` and `verdict`. `line-engraving` is held out — see KNOWN-FLAKY.

**`ground`** — one continuous field across both panels, same hue and same chroma
throughout, **stepping once in VALUE at the divider: one step lighter on the right.** The
step is the only discontinuity; nothing else is in the background.

That step is not decoration; it is the only way this type's own G4 requirement can be met,
and the two rules sat in silent conflict until the grounds were measured panel by panel
across all eight renders. Taking a ground step of 10 of 255 as the cut:

- **Flat field, 4 renders** (headrest, ear tip, toothbrush, hair): whole-panel differences
  of +4.1, +4.2, −0.8 and +4.9. Not one exceeded +5, and one inverted. A flat field leaves
  only the structures to brighten, and that is too small an effect to read.
- **Stepped field, 4 renders**: +31.9, +21.1, +17.6 — and +2.2.

So the step is **necessary but not sufficient**, and the fourth case says why. The sock
render stepped its ground by +15.6 and still finished at +2.2, because its right panel is
covered by a dark sock that ate the brightness back. The rule that holds is therefore in
two parts: step the field, AND do not let the right panel's own content spend the step.

Restating the requirement in words does nothing on its own — v1.8 told the prompts the
difference "must be obvious, not slight" and all three renders that followed ignored it.

`dark-field` is the only field value. The ground sits far below the ivory in value and the
structures read as the lightest thing in the frame: measured separation 178, 179 and 178 on
the three renders that used it. `light-field` was proposed at v1.8 and is **withdrawn at
1.9 on 2 of 2 failures** — see KNOWN-FLAKY.

The colour is DERIVED from the culprit object's own material world, at low chroma, and
must be far in hue from THREE things rather than two: red, blue, **and the warm ivory of
the body**. The third was learned by measurement — the two renders whose ground was warm
(oat at hue 37°, putty at 35°) gave the batch's weakest structure separation at 33 and 58,
because the ivory is itself warm. Grey words are not neutral to this model either: `stone
grey`, `charcoal` and `slate` came back at hues 205°, 182° and 208°, inside the blue band
G3 reserves for the correct side. Name the hue direction explicitly instead of trusting a
grey word to stay neutral.

**`body`** — the relevant anatomical structure in warm ivory (G3: yellow = neutral
structure) over a translucent body outline. EXACTLY ONE figure per panel, same scale and
viewing angle in both. Name the SUBJECT CLASS: this type is not restricted to bone.
Skeleton, tooth and gum, hair shaft and cuticle, skin layers, vein and valve, canal and
cartilage all satisfy it, and the type's own `--diagnostic` example is a hair strand.
Measured 2026-08-12: five of five renders in the MARKS batch drew a SKELETON. That is the
largest single reason this type reads as one repeated image, and the subject class is the
widest diversity lever it owns — G3 fixes the marks and fixes the body's ivory, so colour
cannot carry variety here, but the structure being drawn can. **Confirmed 2026-08-13**: the
one non-skeletal subject whose argument was sound, a vein with two valve cusps, produced the
strongest render this type has made and resembles the bone renders in nothing but grammar.

**`panels`** — LEFT: the figure in the wrong position on the culprit, drawn realistically
and unbranded, the culprit clearly visible where it acts on the body. RIGHT: the same
figure in the correct position on the reference product, at THE SAME interface as the
culprit and comparable in size, exposed rather than housed. RIGHT is brighter and cleaner
than LEFT; that difference is delivered by `ground`'s value step, not by asking for it in
words, which was tried at v1.8 and failed on all three following renders.

**Neither object may occlude the structure under argument.** The toothbrush render put the
reference product across the whole crown, so the gum margin the comparison was measuring
could not be seen on the correct side — the panel that is supposed to prove the case was
the one panel where the evidence was hidden.

## MARKS

This type's own mark library. Marks are called by name from the skeleton. Every one obeys
G3 and carries a count. The `also in` notes exist so that a mark which looks the same in
another type stays visible from here — each type owns its own library, so drift is made
visible rather than centralised away.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `measure` | two dashed straight reference lines, one per panel, each STOPPING at its two landmarks | red left, blue right | exactly 2 | 12 renders |
| `verdict` | circle badge, X on the wrong panel and check on the correct one, TOP corners, flat and solid, same diameter | red X, green check | exactly 2 | 12 renders · also in `01-pain-split`, `03-mechanism-ghostbody`, `06-relief-hero` |
| `contour` | a curved line tracing a surface or an edge | red wrong, blue correct | 1 per panel | 7 renders |
| `fill` | the affected anatomical elements filled | red wrong, blue correct | as many as are affected | 6 renders |
| `aura` | a soft glow following a correct contour | blue only | 1, right panel | 5 renders |
| `force` | a double-headed curved arrow along the surface causing the problem | red only | exactly 1, left panel | 4 renders |
| `range` | a shaded wedge between two limbs or two surfaces, showing the angle available | red wrong, blue correct | 1 per panel | 2 renders |
| `baseline` | one horizontal datum line PER PANEL, both drawn at the same height — the surface both figures rest on | neutral, no signal colour | exactly 2, one per panel | 0 of 2 as first written · **1 of 1 respecified** |
| `axis` | a straight construction line showing the alignment the body should hold, a plumb line through two named landmarks | neutral dashed, no signal colour | 1 per panel | 1 render |
| `pressure` | a filled region bounded by the CONTACT SURFACE between body and object, as wide as the contact itself | red wrong, blue correct | 1 per panel | **0 of 2** |

**`measure` carries the whole argument and has its own rule.** Both lines anchor to the
SAME two anatomical landmarks with identical thickness and dash pattern. Exactly ONE
property may differ — the line's angle, its length, or the gap it spans — and every other
property must read as identical. They are straight LINES, never boxes, brackets or
outlines. For an angle comparison the landmarks are expected to rotate; what must hold
still is length. **The differing property must be visible at a glance** — the headrest
render obeyed every clause above and still failed, because both lines read at a similar
length and the gap the argument rested on was carried by the panels rather than by the
mark. A measure pair the reader has to compare carefully has not measured anything.

**Each line STOPS at its landmarks and may not run past either one.** Two renders failed
the same way — the headrest pair and the sock pair were both drawn across the whole panel
rather than between the two points they were supposed to span, so the gap under argument
was swamped by line that meant nothing. Every clause about form was obeyed in both. What
was missing was anything binding the ENDS of the line to the structure, and without that a
measure mark decorates instead of measuring.

**Where the four proposals stand** (8 renders, 2026-08-12 and 2026-08-13):

- `axis` — 1 render, drew in both panels and stayed neutral. Instrument.
- `range` — 2 renders, read as an angle available both times without needing explanation.
  Instrument.
- `baseline` — 0 of 2 as first written, then **1 of 1 respecified**. The original asked for
  ONE line spanning BOTH panels, which forces the mark across the divider that `ground`
  makes the hardest edge in the frame; as one line per panel at a shared height it drew
  immediately, neutral and correct. This is the cheapest lesson in the file: the mark was
  never the problem, the instruction to cross the divider was.
- `pressure` — **0 of 2**, and it failed differently each time: a glow along the plantar
  fascia on one render, a radial blob on the gum margin on the other, where the same
  prompt's blue half attached itself to the product's bristles instead of to the body. The
  shape of both failures is that no bounded region was ever named, so the model reached for
  the nearest thing it could draw. Respecified above to fill the CONTACT SURFACE, which
  gives it two edges to obey. Third attempt is its last as a proposal.

**Marks that sit on the same structure compete.** On the carrier render the `range` wedge
and the `fill` on the femoral heads ran together, each side reading as one blue or one red
mass; `range` survived only because the wedge was much larger. Two marks of the same signal
colour on the same structure need a size difference or one of them should go.

**Budget.** `measure` and `verdict` are required. Beyond them take 1–3 marks and no more:
this type's argument is one measurement, and a frame carrying six mark classes stops being
a measurement and becomes a diagram of everything. The deliberate five-mark test of
2026-08-12 settles nothing either way — that frame failed by canvas duplication, not by
clutter, so the ceiling is still unmeasured.

## SLOT CONSTRAINTS
- **The removal test, before anything else is written.** Take the culprit out of the LEFT
  panel and ask whether the harmful state goes away with it. If it does, this type applies:
  the two panels are one structure in two states and the product moves it between them the
  moment it is used. If the state persists, the image is showing DAMAGE rather than a
  mechanism, and the RIGHT panel will silently claim a repair the product cannot perform.
  Every render that has worked passes the test — the foot off the tile, the neck away from
  the seat back, the infant out of the narrow carrier, the vein out of the cuff. The two
  that failed on 2026-08-13 do not: a gum stays receded and a hair cuticle stays lifted
  after the brush and the pillowcase are gone. Both were prompt-authoring failures, caught
  by the owner on the image and not by any rule, which is why the rule is now written down.
- Wrong on the LEFT, correct on the RIGHT — locked across the whole library.
- Both panels carry a `verdict` badge; one unlabelled panel leaves the verdict dangling.
- The culprit is drawn realistically but unbranded.
- Strictest G3 compliance in the library; G4 and G5 apply in full.
- `measure` only works where a measurable landmark exists. If the harm cannot be pinned to
  two anatomical points, this type is the wrong choice — see `avoid_when`.
- `pressure` is the last unproven mark, at 0 of 2, and `paper-cut` is an unproven style.
  `baseline` earned its place on the respecified form; `light-field` was withdrawn.
- Wide ratios are a canvas risk on wide-and-short content — see KNOWN-FLAKY.

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
- **Canvas duplicated into a 2×2 grid, 2 observations, 2026-08-12.** The whole two-panel
  comparison rendered a second time below itself, badges on the top row only. Below the
  §6.2 bar at 2 distinct observations, so nothing is legislated yet, but both instances
  share a shape worth stating: each asked for a WIDE ratio on content that is intrinsically
  wide and short, and all five renders of the 2026-08-12 batch came back 1024×1024 square
  whatever ratio was requested — leaving a tall empty band the model filled by repeating the
  row. Until a third observation, compose wide-and-short subjects to fill a square frame
  rather than relying on the ratio to crop them.
- **`light-field` ground, WITHDRAWN at 1.9 on 0 of 2, 2026-08-13.** Proposed at v1.8 as the
  answer to visual sameness, and the measurement killed it: ground-to-ivory value separation
  of 5 and 8 of 255, against 178 for `dark-field`. Both renders held together only on the
  dark outline the prompt asked for — edge contrast standing in for tonal contrast. The
  mechanical reason it cannot be rescued is that a pale ground leaves no headroom to
  brighten into, so it fights the RIGHT-brighter law directly: the toothbrush render came
  back with the right half 0.8 DARKER than the left. Not withdrawn for being ugly; withdrawn
  for being unable to satisfy two of this type's own rules at once.
- **Exact counts on `measure` and `contour`, 4 observations across 8 renders, to 2026-08-13.**
  `measure` drew two lines per panel instead of one on the carrier and the hair renders;
  `contour` drew three per panel on the ear tip and outlined every scale on the hair render.
  Restating the count inside the prompt ("exactly one curved line in each panel, one line and
  no more") did not bind it. Exact counts are already a named risk in adapter Rule 7 and this
  is the type where the risk is realest, because a second line looks like a second
  measurement.
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
now in MARKS. The `flat-vector` question is answered: it carried the dashed pair with an
identical pattern on both renders that used it (carrier, ear tip), so the dash is not an
airbrushed-only effect.

**Why this type renders as the same image every time** (owner report 2026-08-12: the colour
and the visual style repeat from render to render). It is mostly legislated, not
accidental, and worth stating so nobody tries to fix it in the wrong place. G3 fixes the marks at red, blue and green and
fixes the body at warm ivory; `ground` must then avoid red, blue AND warm, which leaves a
narrow band of greens, olives and cool greys — and three of five grounds drifted into the
blue band anyway. So colour is close to fully determined and cannot carry variety.

Three levers were tried against it on 2026-08-13 and the results are not what was expected.
**SUBJECT CLASS works and is the answer** — the compression-sock render, a vein and two
valve cusps, is the strongest image this type has produced and resembles the bone renders in
nothing but its grammar. **STYLE half works**: `paper-cut` came back unmistakably its own
style while every mark in the frame degraded, so it buys variety at a price not yet
measured. **FIELD does not work at all**: `light-field` was the direct attempt to make the
type look different and it is withdrawn on 0 of 2, because a pale ground cannot satisfy the
RIGHT-brighter law. Framing scale remains untested and is now the only unexamined lever
left. The lesson is worth keeping in this order: the variety had to come from WHAT is drawn,
not from how it is lit.

Distinction from `03-mechanism-ghostbody`: 2D illustration vs 3D render; the object in
frame is the CULPRIT, not the product's mechanism; the sentence is "this is what harms
you", not "this shape exists for a reason". The two may run in one gallery (02 then 03)
but must share one palette or they read as two sources.

## CHANGELOG
- 1.9 (2026-08-13): **an admission test the type never had, and a rule conflict measurement
  found.** Evidence: `eval/render-tests.jsonl`, three records at ts 2026-08-13 — one
  `partial` and two `fail`, `verdict_by: harness` under ADR-011 from renders opened. Owner
  report opening it: the toothbrush image is bad in product logic and in output alike.
  **The removal test** is now the first thing in SLOT CONSTRAINTS and the third clause of
  `avoid_when`. Two of the three prompts in that set argued something their product cannot
  do — a toothbrush does not restore a receded gum and a pillowcase does not lay a lifted
  cuticle back down — because this type's grammar is one structure in two states with the
  product switching between them NOW, and accumulated damage is not such a state. The type
  had never said so, so nothing caught it; the owner caught it on the image. The test is
  checkable: remove the culprit and ask whether the harm goes with it.
  **`ground` now steps once in value at the divider**, and that is a real conflict resolved
  rather than a preference. One continuous flat field and "RIGHT brighter than LEFT" cannot
  both hold. Measured across all eight renders: the four that kept the field flat finished
  at +4.1, +4.2, −0.8 and +4.9 of 255, none above +5 and one inverted; of the four that
  stepped it, three finished at +31.9, +21.1 and +17.6 while the fourth managed only +2.2
  because a dark sock covered its right panel and spent the step. So the step is necessary
  and not sufficient — the right panel's own content must not eat it back. v1.8 tried to fix
  this by telling prompts the difference must be obvious; all three following renders ignored
  the words. (First written in this entry from a partial reading of the same measurements —
  three flat renders and two stepped — which undercounted both groups and missed the sock
  counter-example. Corrected here before any prompt was written against it.)
  `light-field` **withdrawn on 0 of 2** — separations of 5 and 8 against dark-field's 178,
  and a pale ground leaves no headroom for the brightening the type requires. It was
  proposed at 1.8 as the cure for visual sameness; the cure turned out to be subject class,
  which is what actually worked.
  Marks: `baseline` earns its place at 1 of 1 on the respecified one-line-per-panel form
  after 0 of 2 as a divider-crossing line — the mark was never the problem, the instruction
  to cross the divider was. `pressure` fails 0 of 2, differently each time, and is
  respecified to fill the CONTACT SURFACE so it finally has edges to obey. `measure` gains
  the clause its two silent failures shared: each line STOPS at its landmarks. `range`
  confirms at 2 renders. `paper-cut` records one render that was visually convincing and
  hostile to every mark in the frame.
  KNOWN-FLAKY gains exact-count drift on `measure` and `contour` at 4 observations across 8
  renders, where restating the count in the prompt did not bind it. File 30489 characters, skeleton 897.
- 1.8 (2026-08-12): **the MARKS library met five renders; two proposals became instruments,
  two did not, and the design language gained a field and a subject choice.** Evidence:
  `eval/render-tests.jsonl`, five records at ts 2026-08-12 covering the standing mat,
  carrier, headrest, ear tip and wrist rest — four `partial` and one `fail`, every one
  `verdict_by: harness` under ADR-011 from a render actually opened.
  Of the four marks that carried no evidence, `axis` and `range` drew clean and are
  instruments now; `pressure` drifted into a glow along a contour and its wording is
  tightened; `baseline` failed 2 of 2, because both attempts sent ONE line across the panel
  divider, and it is respecified as one line per panel at a shared height — untested again.
  Owner report in the same turn: this type repeats its colours and its visual style. Most of
  that is legislated rather than careless — G3 fixes the marks and fixes the ivory body, so
  `ground` must avoid red, blue and warm alike and colour cannot carry variety here. Variety
  moves to where it can live: `ground` gains a `dark-field` / `light-field` choice, `body`
  gains a named SUBJECT CLASS after five of five renders drew a skeleton while this type's
  own example is a hair strand, `style` gains `paper-cut` as a proposal, and `panels` now
  requires the RIGHT-brighter difference to be visible rather than nominal. The measurements
  behind each live in the section they govern, not here; one is worth surfacing, that the
  grey words `stone grey`, `charcoal` and `slate` all returned inside the blue band G3
  reserves for the correct side — v1.2's pale-blue canvas arriving through a neutral word.
  Held below the §6.2 bar rather than legislated: the canvas duplicating into a 2×2 grid
  (2 observations) and a `contour` count overrun at 1 of 6. Still unsettled: the
  1–3 mark budget, because the deliberate five-mark test failed by duplication and not by
  clutter. File 22078 characters against 14171 at 1.7, skeleton 815 against 966.
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

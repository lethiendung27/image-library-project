---
id: 02-cause-anatomy
step: 2
job: cause
device: anatomy
version: "1.12"
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
TYPE: 02-cause-anatomy v1.12 [+ --diagnostic]
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

**`ground`** — `dark-field` is the only value: a ground far below the ivory in value, so the
structures read as the lightest thing in frame. One continuous field, same hue and chroma
throughout, **stepping once in VALUE at the divider, one step lighter on the right.**

The step is not decoration — it is the only way this type's RIGHT-brighter requirement can
be met, and the two rules were in silent conflict until measured. Across eleven renders the
groups do not overlap: a flat field has never exceeded +5 of 255, a step whose brightness the
right panel's own content ate back reached +2.2, and an unspent step has never fallen below
+17.6. So: step the field, and do not let the right panel's content spend it.

Colour must sit far in hue from FOUR things: **red, blue, green** — G3's three signals, the
green being the check badge — **and the warm ivory of the body**, since a warm ground and a
warm structure read as one material.

The v1.9 rule named only three of those four and left green out, which was a plain logical
error: far from red, blue and ivory leaves the green band and nothing else, so the rule drove
the ground INTO a signal colour. Six of six renders on 2026-08-13 came back green, and the
owner's report — that the background is always some deep green — is the rule working as
written. This is the same fault v1.2 removed when it killed the pale blue canvas, arriving by
a different road.

What is left once all four are excluded: the **violet–plum band**, and true neutrals carrying
no colour cast. Neutrals need care because grey words are not neutral to this model —
`stone grey`, `charcoal` and `slate` all returned inside the blue band — so name a neutral as
having no colour cast rather than trusting a grey word. Derivation from the culprit's material
world is now SUBORDINATE: choose from the permitted band first, and derive within it if the
culprit's world allows. Deriving first is what produced six greens.

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
| `measure` | two dashed straight lines, one per panel, each STOPPING at its two landmarks | red left, blue right | exactly 2 | 18 renders · **never yet carried its own difference** |
| `verdict` | badge, a FILLED SOLID DISC with the glyph cut out of it, TOP corners, same diameter | red X, green check | exactly 2 | 18 renders · also in `01-pain-split`, `03-mechanism-ghostbody`, `06-relief-hero` |
| `contour` | a curved line tracing ONE named bounded edge | red wrong, blue correct | 1 per panel | 9 renders |
| `fill` | the affected elements filled | red wrong, blue correct | as many as are affected | 8 renders |
| `force` | a double-headed curved arrow along the surface causing the problem | red only | exactly 1, left panel | 6 renders |
| `aura` | a soft glow following a correct contour | blue only | 1, right panel | 5 renders |
| `range` | a shaded wedge between two limbs or surfaces, showing the angle available | red wrong, blue correct | 1 per panel | 2 renders |
| `baseline` | one horizontal datum line PER PANEL, both at the same height — never one line crossing the divider | neutral, no signal colour | exactly 2 | 1 of 1 respecified |
| `axis` | a construction line through two named landmarks, showing the alignment the body should hold | neutral dashed, no signal colour | 1 per panel | 1 render |
| `pressure` | a filled region bounded by the CONTACT SURFACE, as wide as the contact itself — never a line, never a glow along an edge | red wrong, blue correct | 1 per panel | 1 of 4 |

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
- Unproven and awaiting founding evidence: `paper-cut`. `frame` now has one value only.
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
Kept as the type's only `--diagnostic` example. Stale in two ways to fix when it is next
rendered: it predates both the removal test — a filter does not close a lifted cuticle —
and the 2:1 admission.

## KNOWN-FLAKY
- **`frame` values `interface` and `macro`, WITHDRAWN at 1.12 on 0 of 4, 2026-08-13.** Both
  were proposed at 1.11 as the answer to visual sameness and both obeyed their own wording into
  failure: `macro` cropped the hand and the bicycle out of a grip comparison, leaving a beige
  cylinder against a tissue section; `interface` reduced a mouthpiece to a grey sliver inside a
  head cutaway. The same crop had already cost the kneeling-pad prompt its leg. Withdrawn not
  for being ugly but for removing the person and the product, which are what this type argues
  about. `whole` stands at 2 of 2.
- **`verdict` badges drifting to OUTLINE, 2 of 6, 2026-08-13.** Drawn as a thin ring with the
  glyph inside where the mark demands a filled disc. Below the bar. The mark's form line now
  names the filled disc, which is what fixed `contour`'s count.
- **Exact counts on `measure` and `contour`, 4 observations across 8 renders.** Two lines per
  panel where one was asked for; every scale outlined where one edge was asked for. Restating
  the count inside a prompt did not bind it; naming ONE bounded structure did.
- **Canvas duplicated into a 2×2 grid, 2 observations, 2026-08-12.** The two-panel comparison
  rendered a second time below itself. Both instances asked for a WIDE ratio on
  wide-and-short content, and every render of that batch came back 1024×1024 square whatever
  was requested — a tall empty band the model filled by repeating the row. Compose
  wide-and-short subjects to fill a square frame.
- **`light-field` ground, WITHDRAWN at 1.9 on 0 of 2.** Ground-to-ivory separation of 5 and 8
  against dark-field's 178. A pale ground leaves no headroom to brighten into, so it fights
  the RIGHT-brighter law directly — one render came back with the right half darker. Not
  withdrawn for being ugly, but for being unable to satisfy two of this type's rules at once.
- **`line-engraving` style, 1/1 failed, 2026-08-12.** Turned the `measure` pair into dashed
  BOXES. Held out of the offered list. A retest changes ONLY the style value on a prompt
  already known to work.

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
Evidence for every entry is in `eval/render-tests.jsonl` and in the commit that made it;
git is the audit surface, so decisions are recorded here and workings are not.
- 1.12 (2026-08-13): **two frame values withdrawn, and a logical error in the ground rule
  found by the owner's eye.** Evidence: six records at ts 2026-08-13, four `partial` and two
  `fail`. Owner report: the product barely interacts with the person using it, and the
  background is always some deep green.
  `frame`'s two tight values are WITHDRAWN at 0 of 4. `interface` and `macro` obeyed their own
  wording into failure — crop to the contact and the hand, the bicycle and the person go with
  it, leaving an anonymous shape against a tissue section. A frame that cannot show somebody
  using the product cannot serve a type whose purpose is the product doing its job. `whole` is
  the only value at 2 of 2, and it produced the strongest render this type has made: a
  recognisable band on a recognisable torso, and **the first time in 21 renders that the
  `measure` pair carried its own difference** — whole-body frame, product worn on that body,
  2:1 gap.
  The green was a plain logical error of mine at 1.9: the rule required a hue far from red,
  blue and warm ivory, which leaves the green band and nothing else — and green is G3's third
  signal, the check badge. So the rule drove the ground into a signal colour, the same fault
  v1.2 removed when it killed the pale blue canvas. Six of six renders came back green. The
  rule now excludes all FOUR — red, blue, green, ivory — leaving the violet–plum band and true
  neutrals named as having no colour cast, and derivation from the culprit's material world is
  demoted to a second step, because deriving first is what produced six greens.
  `panels` gains the rule that four of six renders broke: the product must be recognisable AS
  THAT PRODUCT, with a person visible using it.
- 1.11 (2026-08-13): **compressed, and `frame` added.** Owner report: the prompts had grown
  bloated and the outputs still lacked style variety. Both were true and both were mine.
  Measured: rendered prompts went 2321 → 3330 characters across four sets while adapter
  Rule 6 asks for a re-read past 2500, and this file went 14171 → 36631 characters in three
  versions, undoing the compression 1.7 had just performed — CHANGELOG alone reached 31% of
  it. New `PROMPT BUDGET` section states the rule that was missing: a clause earns its place
  in a prompt only if a render has failed without it, ceiling ~1800 characters. On variety,
  the diagnosis was wrong at 1.8 and is corrected here — three style values changed technique
  while every render kept one composition, so `frame` (`whole` / `interface` / `macro`) is
  added as the untried lever. No rule was weakened in this pass; the workings moved to git.
- 1.10 (2026-08-13): ground step CONFIRMED at 5 of 6, the type's most reliable rule.
  `pressure` drew correctly at last, on the CONTACT SURFACE respecification; `contour` held
  its count once ONE bounded edge was named. `measure` admitted to have never carried its own
  difference in 18 renders, and given four clauses: STOP at landmarks, direction named against
  the structure, both lines anchored at the same place, and a 2:1 admission test. `panels`
  gained the drawn-in-both-panels and in-contact requirements. Six records, ts 2026-08-13.
- 1.9 (2026-08-13): the REMOVAL TEST added as the type's first admission gate, after two of
  three prompts argued a repair their product cannot make. `ground` gained the value step at
  the divider, resolving a conflict between the flat field and the RIGHT-brighter law.
  `light-field` withdrawn at 0 of 2. Three records, ts 2026-08-13.
- 1.8 (2026-08-12): five renders of the MARKS library. `axis` and `range` became instruments;
  `pressure` drifted; `baseline` failed 0 of 2 as a divider-crossing line and was respecified.
  `body` gained a named SUBJECT CLASS after five of five renders drew a skeleton. Five
  records, ts 2026-08-12.
- 1.7 (2026-08-12): **restructured into a call-map plus two libraries** (ADR-012). `PARTS`
  holds the non-mark building blocks, `MARKS` this type's marks with form, colour, count and
  evidence; the skeleton became a map naming them. Branches never cost context —
  `query/runbook.md` Step 5 resolves them before a prompt ships — they cost correctness, so
  naming each choice makes it a deliberate lookup. File 25455 → 14171, skeleton 1926 → 966.
- 1.6 (2026-08-12): `measure`'s rule rewritten to govern the LINE — same two landmarks,
  exactly one property differing. The v1.2 wording was generalised from one failure and would
  have forbidden a render that passed.
- 1.5 (2026-08-12): the two parallel panel blocks collapsed into one.
- 1.4 (2026-08-12): background motifs removed and the `baseline` datum put in their place;
  the product must sit at the SAME interface as the culprit, comparable in size and exposed
  rather than housed.
- 1.3 (2026-08-12): **the product became the thing on the right.** The RIGHT panel used to
  read "no object or supportive object", so every render argued "stop doing this" and never
  "buy this". `requires_product_photo` → true; the product-free form kept as `--diagnostic`.
- 1.2 (2026-08-12): **the design language stopped being hard-coded.** Ground derived from the
  culprit's material world, the fixed palette became a functional constraint, illustration
  style became a named choice. G3 makes blue mean correct, so a blue canvas put the whole
  image inside the correct-side signal. Badges moved to TOP corners; `RATIO:` dropped per
  adapter Rule 4.
- 1.1 (2026-08-11): channels gain `advertorial`, resolving a self-contradiction with use_when.
- 1.0 (2026-08-10): initial from the car-seat spine exemplar; exemplar faults encoded
  (correct-side-left inversion, missing X badge). seed: conversation.md.

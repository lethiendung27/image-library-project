---
id: 06-relief-scene
step: 6
job: relief
device: scene
version: "3.7"
status: active
replaced_by: null
ratios: ["16:9", "4:3", "3:4"]
channels: [paid-social, advertorial]
requires_product_photo: true
generation_mode: single-pass
axes:
  gaze: [candid, reflect]
  inset_mode: [none, detail]
variants: []
exempt_from: [G3, G4]
pairs_with: [01-pain-scene]
never_with: []
---

# 06-relief-scene

## PURPOSE
The closing bookend of a pain→relief arc: one photograph of a person visibly letting go of
something they had been bracing against, **with the product there in the scene as the reason**.
Candid, single frame, no inset and no graphics — the product is part of the life, not presented
to the camera.

## TRIGGER
use_when: >
  Closing image of an advertorial or final frame of an ads creative, when the
  product's promise is a state of living rather than a feature, and the product
  can plausibly be present where the relief happens. Pairs naturally with a
  01-pain-scene of the same person, and does not depend on one.
avoid_when: >
  Marketplace galleries, main images, or anywhere the image must stand alone.
  Not when the result is invisible on the body or an object — for invisible
  results the closing image must be 06-relief-hero with the product in frame
  (verified boundary, see the worked example).

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.
A rendered prompt expands what it calls — the model never reads this file (ADR-017).

```
TYPE: 06-relief-scene v3.7
REGISTER: candid documentary photograph, single frame.        -> PARTS/register

[SUBJECT] a person living the resolved state, mid-errand.     -> PARTS/subject
[GAZE] candid, or on a reflection. Never on the lens.         -> PARTS/gaze
[ENVIRONMENT] an ordinary public place they would pass through. -> PARTS/environment
[LIGHT] plain daylight, no glamour.                           -> PARTS/light
[GRADE] muted, desaturated, never warm-boosted.               -> PARTS/grade

[PRODUCT] in the scene as the reason, never presented.        -> PARTS/product
[RELIEF] the moment of letting go, in a situation that        -> PARTS/relief
         would have demanded bracing.

[MARKS]                                                  -> MARKS
  cutaway  a window into the body at the product's place.  --detail
  reach    one tapering shape from the product inward.     --detail

```

## PARTS

**`register`** — a candid documentary photograph a passer-by could have taken. Natural,
unposed, sharp. Not styled, not lit, not aware of a camera.

**`subject`** — the same demographic and the same person as the paired pain image, in
put-together but ordinary clothes from the same palette family, doing an everyday thing in
public and pausing briefly.

**`gaze`** — `candid`, absorbed in their own business, or `reflect`, on their own image in
glass. Both are existing values of the shared axis, and `candid` is the default. **Never at the
camera**: looking at the lens reads as showing off and the barrier goes up. It fails at the
gate — a render that meets every other rule is still a fail if the eyes find the lens.

**`environment`** — a public everyday place the subject would actually pass through, with two
or three incidental blurred passers-by or street details, ordinary weather. Nothing
aspirational, no travel-brochure location, no empty clean street. **The problem started in the
bathroom; the promise ends in the world**, which is why this type is never set at home.

**`light`** — even natural daylight, bright, soft shadows. No golden hour, no rim light, no
glamour lighting. Where a pain counterpart exists, keep the same time-of-day character.

**`grade`** — a natural palette, light film grain, shallow depth of field. **Honest, not
drained** — over a released body a desaturated grade reads as despair. Real rather than glossy,
the light allowed to be kind: no glamour lighting, no warm-boosting into an advert.

## THE RELIEF

**Relief is a body that has stopped defending itself, in a situation that would have demanded
defence.** Both halves are required and neither works alone.

**The situation has to cost something.** A man walking a towpath with his hands in his pockets
is not relieved of anything, because nothing is being asked of him. Kneeling on a hard floor,
carrying a full load up steps, sitting out in bright light, plunging hands into cold water —
these are situations the problem would have made a person avoid, ration or brace against.
Choose the situation from what the problem forbade.

**`environment` and cost are one rule seen twice, 8 of 8.** Domestic or idle settings — a bed, a
bench, an empty yard — asked nothing and the release did not read. Real load — a box onto a
shelf, a toddler onto a hip, a crate on cobbles, a reach to a high shelf — read every time. A
public place is not a style preference; it is where something is asked of a body.

**The body must not be guarding.** Guarding is visible and specific: bracing a hand against
furniture, holding or covering a part, favouring one side, keeping a part tucked away or out of
the light, bearing weight through one leg. Relief is the same body doing none of that — weight
even through both sides, the part in the open, limbs loose, nothing held.

**RELEASE ALONE IS COLLAPSE. Relief is release PLUS something coming back.** A smile alone is
a mood, no expression is nothing, and letting-go alone produces bodies that have given out —
which says the opposite of the argument. The discriminator is visible, and mostly the eyes:

| | collapse | relief |
|---|---|---|
| eyes | shut, lolling | **open, or opening**; creased at the corners |
| head | thrown back, throat bared, mouth slack | level or lifted, the chin doing something |
| limbs | flung, limp | loose but with tone, doing something small |
| direction | everything sinking | the chest opening, shoulders back AND down |
| face | slack | a small smile that arrives on its own |

**The smile is a consequence, never a pose.** Not one performed at a camera-friendly moment:
the one that turns up by itself because something stopped hurting — small, often only in the
eyes, while the person looks at something other than the lens.

Photograph the second the release happens, and require all three of these together:

- **expression** — the breath going out AND the eyes coming open, the brow releasing, a small
  involuntary smile
- **gesture** — the chest opening, shoulders rolling back and down, a held part stretched out,
  a hand opening
- **action** — doing the thing freely, mid-movement, with the product visibly the reason

Any one alone reads as an ordinary photograph. Release without the return reads as collapse.

**`product`** — the product is in the scene as the reason the release is happening, and G1
binds it: the attached photo is the exact reference.

**It must STAND IN THE FRAME AS ITS OWN OBJECT, near the camera, turned so it can be read.**
Measured twice: of four renders at 3.2 and eight more at 3.5–3.6, the only two a viewer could
name were a bottle upright on a desk and an open tub on a worktop, both near the lens with the
label toward it. Everything inside, under or edge-on failed.

**A LABEL THAT CAN BE READ IS TEXT, and the type banned both.** The one nameable product in
eight carried its name in clean type; the one turned away came back with a gibberish
back-of-pack panel and read as a household cleaner. The no-text rule's evidence was a named
NEWSPAPER — an object whose content IS text — and it was over-generalised onto labels, where G1
binds the product to the reference anyway. **The label carries the NAME and nothing else.**
Amount is the discriminator: two words render clean, a paragraph renders as gibberish.

**Not presented still holds** — the person does not hold it up, look at it or offer it, and it
is not centred or lit for the camera. It simply occupies its own space in the picture the way a
documentary photographer standing in the right place would include it.

**Three product classes, and the third takes `--detail` rather than being excluded.**

| class | test | route |
|---|---|---|
| **standalone** | sits in the scene as its own object | `--none` — the eye-drops bottle |
| **worn-external** | can be the outermost layer if the wardrobe allows | `--none`, on a wardrobe condition |
| **conforming or enclosed** | no silhouette of its own, or always inside another object | **its package in frame, `--detail` for the mechanism** |

**Worn-external** — a compression sock, a knee support, a wrist brace — IS the visible surface
once the wardrobe exposes the limb. The wardrobe must be chosen for the product and the
situation must make it ordinary; a trouser leg pushed up for the camera is a pose and fails.

**Conforming and enclosed fail differently.** An insole is enclosed, inside a shoe where no
camera reaches. A patch is conforming — flat against a curve, so no silhouette. In shot is not
identifiable.

**Neither is a reason to refuse a product — but THE INSET IS NOT THE PRODUCT.** 3.5 and 3.6
tried to admit this class by drawing it instead of photographing it, and the product then left
the frame in 4 of 8. `requires_product_photo` and G1 bind in every variant, and a drawn product
satisfies neither.

**So it enters the frame AS ITS PACKAGE** — box, tub, sleeve or packet standing in the scene as
its own object under the rule above — and `--detail` says what the contents do. The package is
the photographed product, the cutaway is the mechanism, and neither substitutes for the other.

**The admission test.** If the resolved state cannot be shown as a body behaving differently in
a situation that costs something, this type is the wrong one. Close with `06-relief-hero`, which
presents the product and can argue with an inset because its register expects composed layers;
a candid documentary photograph does neither.

## MARKS

**No mark ever appears in the photograph.** `cutaway` and `reach` exist only inside the
`--detail` inset; `--none` carries nothing at all. 3.6's one exception, `locate`, is retired
below.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `cutaway` | a clean-edged window into the body at the product's place, the product on the surface and the layer beneath shown in a plain technical register | the tissue's own neutral tones | 1, in the inset only | borrowed — the device is `03-mechanism-ghostbody`, 14 renders |
| `reach` | ONE continuous shape running from the product's face into the layer beneath, tapering as it goes so its own width says how far the effect reaches | one warm hue, never red | 1, inside the cutaway | 5 renders, restated from 0/5 |

**Every mark is a FLAT, UNSHADED, HARD-EDGED, FULLY OPAQUE OVERLAY**, drawn on top like clean
vector shapes. `03-mechanism-ghostbody` measured its `support` mark 0 of 3 as a tint of the
anatomy and 3 of 3 as a band laid on top; A11 is why — a mark whose form the register could have
produced stops being a mark. **Never a tint of the anatomy.**

**Opacity is the half of that rule the wording kept losing, 2 of 5.** Two renders obeyed
hard-edged and unshaded and still filled the shape translucently, so tissue boundaries and bone
read straight through it — which is a tint with a crisp outline, and it drifts back toward being
anatomy. Say opaque, and say that nothing beneath shows through.

**NEVER N SHAPES OF GRADED SIZE — that is a bar chart, and it rendered as one 5 of 5.** Spec'd
as "flat bands, each one further in than the last", `reach` came back four times as a bar chart
and once as arrowheads; 0 of 5 read as travel. Graded repetition IS a chart idiom and it
overrides direction — ascending bars claim MAGNITUDE BY CATEGORY, not mechanism. A different hue
or wider spacing only makes the chart cleaner. **One continuous shape that changes along its
length**, its taper carrying the distance. Arrows stay banned (G6): an arrowhead is the same
glyph in a hat.

**It must still travel, and the direction is the argument.** A static warm patch on a muscle
reads as inflammation — the thing that hurts. A shape running from the product INTO the tissue
reads as delivery. Hence warm but never red: red on a body is pain everywhere else in this
library. **And it must start ON the product**, so the product is drawn inside the cutaway — 2 of
5 panels had none, and their marks floated sourceless.

**`locate` is retired at 0 of 2 — do not re-propose it.** A bloom through the garment read as
LENS FLARE on a light shirt and as a DIRT SMUDGE on dark knit. Both of `01-pain-scene`'s
paid-for limits held, so it was not mistuned but mis-founded: **A11 was applied to the wrong
property.** Emitted light is not a form a photographic register cannot produce — it is among the
commonest things a photograph contains, and a viewer takes the ordinary explanation. The one
form that would make a bloom read as a mark is a hard boundary, which is exactly what
`01-pain-scene` measured 3 of 3 a glow cannot hold. **A borrowed mark must be re-tested in the
borrowing type's register**, because A11 is a claim about a register, not about a mark.

**The cutaway stays in the inset.** Internals bleeding into the photographic hero break G5 —
that rule is `06-relief-hero --detail`'s and it applies here for the same reason. The hero
remains a photograph a passer-by could have taken; the inset is plainly a diagram, and the two
do not blend at the border.

**KIND-not-LOOK is confirmed, 4 of 4.** A bordered corner box, a borderless bottom strip, a torn
tall panel and a bevelled window all held their separation from the photograph, and 3 of 4 read
at once as technical sections. Fixed is the KIND: a plain technical section, plainly a drawing,
flat hard-edged marks on top. Panel shape, placement, ground, line weight, section angle,
border-or-none and `reach`'s hue are chosen per prompt and **no two in a set may share them**.

**It must show recognisable anatomy** — the fourth panel did not, and generic layered bands with
a lump on top could be a section through anything. The three that worked each gave a landmark a
viewer knows: a foot in a boot, a nose in profile, a lumbar spine. Name the landmark.

**The hero still has to carry the relief on its own.** The cutaway explains the mechanism; it
does not excuse a body that is not releasing. If the photograph fails the release test, the
inset cannot rescue it — sixteen renders proved an inset cannot carry an argument the hero has
not made.

## SLOT CONSTRAINTS
- **Never describe the frame's shape or ratio in a prompt.** The owner sets the ratio at render
  time (ADR-016); a prompt reasoning about frame geometry gets extra panels to fill the leftover.
- **The zone names never reach the model.** Region labels are the tier that leaks; whole-image
  and subject labels do not (adapter Rule 1b, tiers set by ADR-017). Describe the region:
  "a shop window fills the left third", not `[REFLECTION]`.
- **No object in the SCENE may carry printed text** — a named newspaper filled two
  `06-relief-hero` frames with nonsense. **The product's own label is the exception**: it carries
  the product NAME and nothing else, because the product law requires a label that can be read.
  Never a back-of-pack panel, body copy or barcode; those come back as gibberish.
- A clause earns its place only if a render has failed without it, and is removed only once a
  render has done without it and come back correct (ADR-013, ADR-015).

## NEGATIVE
```
[G6] + badges, arrows, drawn overlays, insets of any kind, looking at camera,
posing, laughing as the relief, a situation that costs nothing,
a guarded body, hand braced on furniture, a part held or covered,
arms raised, celebration gesture, golden hour, warm flattering light,
glamour lighting, beauty retouching, plastic skin, aspirational travel location,
empty clean street, styled outfit, product presented to camera,
product centred or held up, product hidden inside or under something,
product turned away so its face cannot be read, back-of-pack label, barcode,
bar chart, bars of stepped or graded height, arrowheads, translucent marks,
trouser leg or sleeve pushed up for the camera, blank expression,
collapsed posture, head lolled back, limbs flung limp, eyes shut and slack,
drained joyless grade, saturated colors, stock photo look
```

## WORKED EXAMPLES
### example: desk-eye-drops — skeleton@3.2, run: partial
Product: eye drops · axes: gaze=candid · frame delivered 1200x896
**The closest this type has come, and the only render where a viewer can name the product.**
The emotion is right: sitting up rather than slumped, one hand at the back of the neck
mid-stretch, both eyes wide and clear on the street outside the window, a half smile that
arrived on its own. And the bottle stands upright on the desk close to the camera with its label
toward the lens — its own object, in its own light, while he is not looking at it or touching
it. That is the placement rule 3.3 was written from.

Still partial: nothing in the frame connects the bottle to the release, so it could be anyone's
desk bottle. That is the open question this type now has left.

```
TYPE: 06-relief-scene v3.2
REGISTER: a candid documentary photograph a passer-by could have taken. Single
frame, natural, unposed, sharp. Nobody aware of a camera.

PRODUCT REFERENCE: use the attached photo as the exact reference. Preserve
shape, proportions, material, finish and colour exactly. Do not redesign or add
features.

A man in his thirties at an office desk has just looked up from his screen and
out of the window beside him, and is watching something down in the street. Not
at the camera. He is sitting up, not slumped, one forearm still on the desk and
the other hand resting on the back of his neck mid-stretch.

Both eyes are wide open and clear and he is looking out of the window, the skin
around them smooth rather than screwed up, the brow out of its frown. A half
smile has arrived on its own at whatever he can see. His chest is open and his
shoulders are rolled back and down. His head is level, not tipped back.

The bottle of eye drops is on the desk by the keyboard where he set it down, cap
back on. He is not looking at it and not touching it.

An ordinary office desk: a monitor pushed back, a keyboard, a mug, a coat over
the chair, a window with afternoon light and the street beyond it.

LIGHT: daylight from the window, kind and even, no rim light, no glamour
lighting.
GRADE: natural colour, light film grain, shallow depth of field. Honest, not
glossy, and not drained.

No text, no logo, no watermark, no inset, no arrows, no badges.
```

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 3.7 (2026-08-14): the inset is not the product, and `reach` was a bar chart. 8 renders, 0
  pass. `reach` rendered as a chart glyph 5/5 — graded repetition IS a chart idiom — restated as
  ONE tapering shape starting on the product. `locate` retires 0/2: A11 was applied to the wrong
  property, emitted light being just what a photographic register produces. The product left the
  frame in 4/8, all conforming or enclosed, so that class now enters as its PACKAGE. The no-text
  rule splits — the only nameable product in eight carried its name. KIND-not-LOOK holds 4/4.
- 3.6 (2026-08-14): a third route for a covered product, and the cutaway stops having a fixed
  look. `locate` — a soft bloom through the garment saying where the product is — borrowed from
  `01-pain-scene`'s `glow` with its two measured limits: a glow cannot be held to a boundary
  (3/3) and a red one on a body reads as pain. It states position where `--detail` states
  mechanism. And the cutaway's LOOK is now chosen per prompt with no two in a set alike; only
  its KIND is fixed. Fixing a look is what produced sixteen identical rooms on `03-use-sequence`. `31dffa3`
- 3.5 (2026-08-14): the excluded class gets a variant instead of a refusal. `inset_mode:
  [none, detail]` using existing vocabulary. A conforming or enclosed product is shown by what
  it DOES: a `cutaway` window into the body at its place, with `reach` as flat hard-edged bands
  stepping inward. Device and form law borrowed from `03-mechanism-ghostbody`, which measured
  0/3 for a mark drawn as a tint of anatomy and 3/3 as a band laid on top. This also closes the
  causal link the type never had. `--none` is unchanged and still carries no marks. `9de2479`
- 3.4 (2026-08-14): the admission test splits into three classes. "Inside or under something"
  was too blunt — a compression sock is worn-external and works once the wardrobe exposes the
  limb, where an insole is enclosed and never can. Conforming products like an adhesive patch
  are excluded for a third reason: no silhouette, so visible is not identifiable. Their one
  opening is the second the hand comes away, flat to the lens with a printed face. `74ebfac`
- 3.3 (2026-08-14): the emotion is solved 4/4 and the product is not. It has to stand in the
  frame as its own object, near the camera, turned so it can be read — the one legible render
  was a bottle upright on a desk with its label toward the lens. `present, not presented` had
  conflated not-presented with not-prominent. Admission test gains a second clause: a product
  that only lives inside or under something cannot be argued here at all. `0e82a81`
- 3.2 (2026-08-14): release alone is collapse. 3.1's letting-go produced bodies that had given
  out — thrown back, limbs flung, eyes shut — which says the opposite of the argument. Relief is
  release PLUS something coming back, and the discriminator is a table now in the file: eyes
  open not lolling, head level not thrown back, chest opening not sinking, and a small smile
  that arrives on its own. `grade` stops being desaturated, which was fighting the joy. `df30f43`
- 3.1 (2026-08-14): the product comes into the frame and the relief becomes a moment. Twenty
  renders with no product could not say what relieved anyone; `requires_product_photo` is now
  true and G1 binds. And relief is neither a smile nor a blank face — 3.0 banned the smile and
  got blankness, which is worse. It is the second of letting go: eyes closing, shoulders
  rolling down, a held part stretched out, with the product visibly the reason. `c31e2c1`
- 3.0 (2026-08-14): the marks and the inset are cut. Owner: the inset is obscure, and with it
  covered the main photograph shows no relief — true in 15 of 16 renders across four rounds.
  MARKS is replaced by THE RELIEF, the thing the type actually needs and never had: a body that
  has stopped defending itself, in a situation that would have demanded defence. A smile is not
  relief. MAJOR — the inset layer is removed. `db2c5dc`
- Pre-3.0 entries below describe the before/after inset layer that 3.0 removed outright. Kept as
  decision plus hash; the reasoning is in the commits (ADR-013).
- 2.3 (2026-08-14): both cells become SCENES, not macro surface studies, and the drain goes with
  the change; a scene needs room to be one. `5fbea1d`
- 2.2 (2026-08-14): the crop was the whole problem — both rules asking for it were RELATIVE, so
  each cell gets its own absolute description. `423f1b8`
- 2.1 (2026-08-14): the inset mechanism works with two conditions — `past` gains an admission
  test (drain preserves a TONAL problem, destroys a COLOUR one) and `evidence` a size floor. `c795d1b`
- 2.0 (2026-08-14): two angles are one moment, so the founding premise is withdrawn; `past`
  becomes the required mechanism and `reflection` is demoted. MAJOR: `requires_pair` dropped. `59678e1`
- 1.1 (2026-08-14): restructured into a call-map plus PARTS and MARKS (ADR-012); ratios move to
  ADR-016's set; `RATIO:` dropped per adapter Rule 4. `3fb74a2`
- 1.0 (2026-08-10): initial from the shop-window reflection exemplar; --reflect gaze
  mode contributed to the shared gaze axis. seed: conversation.md.

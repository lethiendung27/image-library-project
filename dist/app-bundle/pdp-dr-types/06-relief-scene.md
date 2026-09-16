---
id: 06-relief-scene
step: 6
job: relief
device: scene
version: "3.8"
status: active
replaced_by: null
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
text_layer: [title]
copied_from: 06-relief-scene
copied_at_version: "3.7"
blocked_by: null
---

# 06-relief-scene

## PURPOSE
The closing bookend of a pain→relief arc: one photograph of a person visibly letting go of
something they had been bracing against, **with the product there in the scene as the reason**.
Candid, single frame, no inset and no graphics — the product is part of the life, not presented
to the camera.

**Copied verbatim from `registry/types/06-relief-scene.md` at version 3.7** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## LP2 LAW
Added 2026-09-16 (ADR-094): the owner's gallery instruction for Contextual / Lifestyle. This section is
this copy's own and a re-copy keeps it; `registry/pdp-dr-instruction.md` binds the rest.

- **The words: a title of at most 5 words, or none.**
- **It counts as a place scene**, and a set carries at most two (`mapping/pdp-dr-rules.md`).
- The type's own law — a public place, relief with something coming back, the product standing as
  its own object — is what makes a context tile an argument rather than a stock photograph. The
  owner's first two cushion batches spent seven and eight of their twenty tiles each on scenes of
  use in a place.

Slots an LP2 prompt adds to the SKELETON above:
```
[TITLE]  at most 5 words, or none.                  -> LP2 LAW
```

## TRIGGER
use_when: >
  Closing image of an advertorial or final frame of an ads creative, when the
  product's promise is a state of living rather than a feature, and the product
  can plausibly be present where the relief happens. Pairs naturally with a
  01-pain-scene of the same person, and does not depend on one.

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

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 3.8 (2026-09-16): `LP2 LAW` added: the owner's gallery instruction for this type — a title of at most five words or none, and the count of place scenes it belongs to. `text_layer` declared. First LP2 edit; `copied_at_version` stays 3.7. ADR-094.
- 3.7 (2026-09-15): copied verbatim from `registry/types/06-relief-scene.md` at 3.7, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.

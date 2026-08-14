---
id: 06-relief-scene
step: 6
job: relief
device: scene
version: "3.5"
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
TYPE: 06-relief-scene v3.5
REGISTER: candid documentary photograph, single frame.        -> PARTS/register

[SUBJECT] a person living the resolved state, mid-errand.     -> PARTS/subject
[GAZE] candid, or on a reflection. Never on the lens.         -> PARTS/gaze
[ENVIRONMENT] an ordinary public place they would pass through. -> PARTS/environment
[LIGHT] plain daylight, no glamour.                           -> PARTS/light
[GRADE] muted, desaturated, never warm-boosted.               -> PARTS/grade

[PRODUCT] in the scene as the reason, never presented.        -> PARTS/product
[RELIEF] the moment of letting go, in a situation that        -> PARTS/relief
         would have demanded bracing.

[MARKS] --none carries none. --detail only:              -> MARKS
  cutaway  a window into the body at the product's place
  reach    flat bands stepping inward, how far it travels

```

## PARTS

**`register`** — a candid documentary photograph a passer-by could have taken. Natural,
unposed, sharp. Not styled, not lit, not aware of a camera.

**`subject`** — the same demographic and the same person as the paired pain image, in
put-together but ordinary clothes from the same palette family, doing an everyday thing in
public and pausing briefly.

**`gaze`** — `candid`, absorbed in their own business, or `reflect`, on their own image in
glass. Both are existing values of the shared axis. **Never at the camera**: looking at the lens
reads as showing off and the barrier goes up. `reflect` is no longer compulsory, which is what
2.0 changed — `candid` is now the default and the ordinary case.

**`environment`** — a public everyday place the subject would actually pass through, with two
or three incidental blurred passers-by or street details, ordinary weather. Nothing
aspirational, no travel-brochure location, no empty clean street. **The problem started in the
bathroom; the promise ends in the world**, which is why this type is never set at home.

**`light`** — even natural daylight, bright, soft shadows. No golden hour, no rim light, no
glamour lighting. Where a pain counterpart exists, keep the same time-of-day character.

**`grade`** — a natural palette, light film grain, shallow depth of field. **Honest, not
drained.** Desaturating was inherited from matching a paired pain image, and against a released
body it reads as despair — the locker-room render is muted blue-green over a man who looks
finished. Keep it real rather than glossy, and let the light be kind. No glamour lighting, no
warm-boosting into an advert, but nothing bleached out either.

## THE RELIEF

**This type has no marks and no inset.** Sixteen renders across four rounds went into a
comparison device — a drained macro, then a suffering scene — and the owner's test retires it:
cover the inset and look at the main photograph alone. Relief survived that test once in
sixteen. The device was never the problem to solve.

**Relief is a body that has stopped defending itself, in a situation that would have demanded
defence.** Both halves are required and neither works alone.

**The situation has to cost something.** A man walking a towpath with his hands in his pockets
is not relieved of anything, because nothing is being asked of him. Kneeling on a hard floor,
carrying a full load up steps, sitting out in bright light, plunging hands into cold water —
these are situations the problem would have made a person avoid, ration or brace against.
Choose the situation from what the problem forbade.

**The body must not be guarding.** Guarding is visible and specific: bracing a hand against
furniture, holding or covering a part, favouring one side, keeping a part tucked away or out of
the light, bearing weight through one leg. Relief is the same body doing none of that — weight
even through both sides, the part in the open, limbs loose, nothing held.

**RELEASE ALONE IS COLLAPSE. Relief is release PLUS something coming back.** Three versions
went wrong here in three directions: a smile gave a mood that said nothing, no-expression gave
people doing ordinary things, and letting-go gave bodies that had given out — a woman thrown
back in a chair with her arms flung limp, a man sprawled along a bench under strip light. The
third is the worst of them, because the first two said nothing and this one says the opposite
of the argument.

The discriminator is visible and checkable, and it is mostly the eyes:

| | collapse | relief |
|---|---|---|
| eyes | shut, lolling | **open, or opening**; creased at the corners |
| head | thrown back, throat bared, mouth slack | level or lifted, the chin doing something |
| limbs | flung, limp | loose but with tone, doing something small |
| direction | everything sinking | the chest opening, shoulders back AND down |
| face | slack | a small smile that arrives on its own |

**The smile comes back — as a consequence, never as a pose.** What failed at 2.3 was a laugh
performed at a camera-friendly moment. What is wanted is the smile that turns up by itself
because something has stopped hurting: small, often only in the eyes, and usually while the
person is looking at something other than the lens.

Photograph the second the release happens, and require all three of these together:

- **expression** — the breath going out AND the eyes coming open, the brow releasing, a small
  involuntary smile
- **gesture** — the chest opening, shoulders rolling back and down, a held part stretched out,
  a hand opening
- **action** — doing the thing freely, mid-movement, with the product visibly the reason

Any one alone reads as an ordinary photograph. Release without the return reads as collapse.

**`product`** — the product is in the scene as the reason the release is happening, and G1
binds it: the attached photo is the exact reference.

**It must STAND IN THE FRAME AS ITS OWN OBJECT, near the camera, turned so it can be read.** An
earlier wording said "present, not presented — never centred, never held up", which conflated
NOT PRESENTED with NOT PROMINENT and put products inside boots and under jumpers. Four renders
sorted on this and on nothing else: a bottle standing upright on a desk close to the lens with
its label toward it was the only one a viewer could name. A tube edge-on in a pocket showed that
something was there but not what. An insole inside a boot and a wrap under a jumper were not
objects in the frame at all, and the wrap render resolved the contradiction by dropping the
product entirely.

**Not presented still holds** — the person does not hold it up, look at it or offer it, and it
is not centred or lit for the camera. It simply occupies its own space in the picture the way a
documentary photographer standing in the right place would include it.

**Three product classes, and the third takes `--detail` rather than being excluded.**

| class | test | route |
|---|---|---|
| **standalone** | sits in the scene as its own object | `--none` — the eye-drops bottle |
| **worn-external** | can be the outermost layer if the wardrobe allows | `--none`, on a wardrobe condition |
| **conforming or enclosed** | no silhouette of its own, or always inside another object | **`--detail`** |

**Worn-external**: a compression sock, a knee support, a wrist brace, a splint. These ARE the
visible surface once the wardrobe exposes the limb. The wardrobe must be chosen for the product
AND the situation must make that wardrobe ordinary — shorts on a runner, bare calves at home. A
trouser leg pushed up for the camera is a pose and fails.

**Conforming and enclosed fail for different reasons and both are answered by the same
variant.** An insole is enclosed: inside a shoe, no camera reaches it. An adhesive patch is
conforming: perfectly visible on a shoulder and still unreadable, because a flat rectangle
following the curve of a body has no silhouette. Being in shot is not being identifiable.

**Neither is a reason to refuse the product — it is a reason to show what it DOES instead of
what it looks like.** That is `--detail`, and it also closes the one thing this type has never
had: nothing in a scene connects the product to the release. A cutaway does.

**The admission test.** If the resolved state cannot be shown as a body behaving differently in
a situation that costs something, this type is the wrong one. Close with `06-relief-hero`, which
presents the product and can argue with an inset because its register expects composed layers;
a candid documentary photograph does neither.

## MARKS

**`--none` carries no marks at all and that is still the default.** Everything below exists only
inside the `--detail` inset, and nothing from it ever appears in the photograph.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `cutaway` | a clean-edged window into the body at the product's place, the product on the surface and the layer beneath shown in a plain technical register | the tissue's own neutral tones | 1, in the inset only | borrowed — the device is `03-mechanism-ghostbody`, 14 renders |
| `reach` | flat hard-edged bands stepping inward from the product's face into the layer beneath, showing how far the effect travels | one warm hue, never red | 1 set, inside the cutaway | **none** — proposal |

**Every mark is a FLAT, UNSHADED, HARD-EDGED OVERLAY**, drawn on top like clean vector shapes.
This is `03-mechanism-ghostbody`'s hardest-won rule and it transfers unchanged: three renders of
its `support` mark came back as a tint of the anatomy and every one read as coloured tissue
rather than as a mark — 0 of 3 as a fill, 3 of 3 as a band beside the structure. A11: a mark
whose form the register could have produced stops being a mark. **Never a tint of the anatomy.**

**`reach` must travel, and the direction is the whole argument.** A static warm patch on a
muscle reads as inflammation — as the thing that hurts. Bands stepping from the product INTO
the tissue read as the product delivering something. Direction is what separates a benefit from
a symptom, and it is why the hue is warm but never red: red on a body is pain in every other
type in this library.

**The cutaway stays in the inset.** Internals bleeding into the photographic hero break G5 —
that rule is `06-relief-hero --detail`'s and it applies here for the same reason. The hero
remains a photograph a passer-by could have taken; the inset is plainly a diagram, and the two
do not blend at the border.

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
- **No object in the scene may carry printed text.** Model-drawn text arrives as gibberish and
  this type bans text outright. Named newspaper filled two `06-relief-hero` frames with nonsense.
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
product turned away so its face cannot be read, trouser leg or sleeve pushed up
for the camera, blank expression,
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
- 3.5 (2026-08-14): the excluded class gets a variant instead of a refusal. `inset_mode:
  [none, detail]` using existing vocabulary. A conforming or enclosed product is shown by what
  it DOES: a `cutaway` window into the body at its place, with `reach` as flat hard-edged bands
  stepping inward. Device and form law borrowed from `03-mechanism-ghostbody`, which measured
  0/3 for a mark drawn as a tint of anatomy and 3/3 as a band laid on top. This also closes the
  causal link the type never had. `--none` is unchanged and still carries no marks.
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
- 2.3 (2026-08-14): both cells are SCENES. Absolute description fixed the crop 4/4 after eight
  failures, and with the crops finally matched the images were plainly macro surface studies —
  a spec device, not a relief scene. Owner's correction: relief scene, suffering scene inset.
  The drain goes with it, because a suffering scene marks itself and draining it only hid the
  problem; the tonal admission test dissolves with the drain, so hue-signalled problems return.
  The crop-to-the-evidence rule is reversed: a scene needs room to be one. `5fbea1d`
- 2.2 (2026-08-14): the crop is the whole problem. Eight renders never once matched crop
  between the cells, because both rules asking for it were RELATIVE — "framed the same way",
  "smaller in the inset" — and `smaller` was read as `wider shot`. Each cell now gets its own
  absolute description. Two conditions added from a clean 2-2 split: the inset holds the
  evidence and almost nothing else, and whatever `evidence` names must be visible in both cells. `423f1b8`
- 2.1 (2026-08-14): the inset mechanism works, with two conditions the first four renders
  bought. `past` gains an admission test — the drain preserves a TONAL problem and destroys a
  COLOUR one, 2/2 against 0/1, so a hue-signalled problem routes to `06-relief-hero --vsinset`
  instead. `evidence` gains a size floor: the hero's copy is never smaller than the inset's,
  which is exactly how the four renders sort. 2 pass, 1 partial, 1 fail. `c795d1b`
- 2.0 (2026-08-14): the argument moves from two angles to two moments. Four first renders
  returned flawless reflections and no argument, so the founding premise is withdrawn: two
  angles are one moment. `past`, a desaturated inset of the problem, becomes the required
  mechanism — 5 obs and 2/2 on `06-relief-hero`. `reflection` demoted to optional. MAJOR:
  layer structure changes and `requires_pair` is dropped, the before now being in-frame.
  `gaze` gains `candid`; `4:3` added. `59678e1`
- 1.1 (2026-08-14): restructured into a call-map plus PARTS and MARKS (ADR-012); skeleton
  cut. First MARKS library, and all three entries are proposals: this type has 0 observations
  and 0 renders, so there is nothing to count. Every entry is made of the scene, because the
  drawn class is the unreliable one across three sibling types. `ratios` move to ADR-016's set —
  `5:3` and `4:5` become `16:9` and `3:4`. `RATIO:` dropped per adapter Rule 4. `3fb74a2`
- 1.0 (2026-08-10): initial from the shop-window reflection exemplar; --reflect gaze
  mode contributed to the shared gaze axis. seed: conversation.md.

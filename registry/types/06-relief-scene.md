---
id: 06-relief-scene
step: 6
job: relief
device: scene
version: "3.1"
status: active
replaced_by: null
ratios: ["16:9", "4:3", "3:4"]
channels: [paid-social, advertorial]
requires_product_photo: true
generation_mode: single-pass
axes:
  gaze: [candid, reflect]
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
TYPE: 06-relief-scene v3.1
REGISTER: candid documentary photograph, single frame.        -> PARTS/register

[SUBJECT] a person living the resolved state, mid-errand.     -> PARTS/subject
[GAZE] candid, or on a reflection. Never on the lens.         -> PARTS/gaze
[ENVIRONMENT] an ordinary public place they would pass through. -> PARTS/environment
[LIGHT] plain daylight, no glamour.                           -> PARTS/light
[GRADE] muted, desaturated, never warm-boosted.               -> PARTS/grade

[PRODUCT] in the scene as the reason, never presented.        -> PARTS/product
[RELIEF] the moment of letting go, in a situation that        -> PARTS/relief
         would have demanded bracing.

NO MARKS and NO INSET. This type has neither, and that is the type.

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

**`grade`** — a muted palette, light film grain, shallow depth of field. Desaturated, never
warm-boosted. One photograph, in full colour throughout.

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

**Relief is a MOMENT OF LETTING GO, not a state of being fine.** Six versions went wrong in two
opposite directions here. A smile is a mood and says nothing — a woman laughing over a mug tells
you nothing about her hands. But blankness is worse: four renders asked for no particular
expression and returned people doing ordinary things, which is not relief, it is nothing.
**Photograph the release itself**, in the second it happens:

- **expression** — eyes closing, head going back, the breath going out, the jaw and the brow
  letting go. Never a smile, and never blank.
- **gesture** — the specific movement of stopping: shoulders rolling down and back, a held part
  stretched out, a hand opening, sitting down into something and letting it take the weight.
- **action** — doing the thing freely, mid-movement, with the product visibly the reason it is
  possible.

All three at once, in one frame. Any one of them alone reads as an ordinary photograph.

**`product`** — the product is in the scene as the reason the release is happening: in the
hand, on the body, on the surface just used, within reach. It is **never presented to the
camera**, never centred, never held up — that is `06-relief-hero`'s job and its register. Here
it sits where it would really be and the person is not looking at it. It must be legible enough
to recognise at a glance, and G1 binds it: the attached photo is the exact reference.

**The admission test.** If the resolved state cannot be shown as a body behaving differently in
a situation that costs something, this type is the wrong one. Close with `06-relief-hero`, which
presents the product and can argue with an inset because its register expects composed layers;
a candid documentary photograph does neither.

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
product centred or held up, blank expression, saturated colors, stock photo look
```

## WORKED EXAMPLES
### example: park-bench-hay-fever — skeleton@2.3, run: partial
Product: none in frame (G1-exempt) · axes: gaze=candid · frame delivered 1200x896
**Kept for its main photograph, which is the only one in sixteen renders that carries relief on
its own.** She is sitting back into the bench with her head tipped up, eyes open and clear,
hands loose on her bag, her weight settled — nothing about her is defending anything, in a
place and a season that used to cost her something. Cover the inset and the photograph still
says it.

**Do not copy the inset half.** 3.0 bans insets outright and the full text is kept only because
SPEC 3.3 requires a rendered example to record what actually rendered.

```
TYPE: 06-relief-scene v2.3
REGISTER: a candid documentary photograph a passer-by could have taken. Single
frame, natural, unposed, sharp. Nobody aware of a camera.

A young woman in a denim jacket is sitting back on a park bench with her face
tipped up into the light and her eyes open, watching something across the grass.
Not at the camera. She is at half length, seated, with the bench and the park
behind her.

The relief is in her eyes and face and it must be a fact anyone could point at:
both eyes are wide open and clear, the whites unmarked, the skin around them and
across the nose even in tone, and her hands are resting on the bench with
nothing held to her face.

In the upper right corner sits a small photograph in full colour, about a fifth
of the picture wide, with a thin white border. It shows the same woman on the
same bench in the same jacket, earlier: she is hunched forward with a crumpled
tissue pressed under her nose, her eyes screwed almost shut and streaming, the
lids and the skin around her nose red and swollen, turned away from the light.
The bench and the park are in it so it reads as a moment.

The same denim jacket and the same canvas bag beside her are in both
photographs. Nothing else is shared.

An ordinary park: mown grass, a litter bin, two blurred people on the path
behind, a line of trees.

LIGHT: bright flat daylight, even, no rim light.
GRADE: muted green and denim blue, light film grain, shallow depth of field,
desaturated, never warm-boosted. Both photographs are in full colour.

No text, no logo, no watermark, no product, no arrows, no badges.
```

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
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

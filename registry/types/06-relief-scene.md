---
id: 06-relief-scene
step: 6
job: relief
device: scene
version: "2.0"
status: active
replaced_by: null
ratios: ["16:9", "4:3", "3:4"]
channels: [paid-social, advertorial]
requires_product_photo: false
generation_mode: single-pass
axes:
  gaze: [candid, reflect]
variants: []
exempt_from: [G1, G3, G4]
pairs_with: [01-pain-scene]
never_with: []
---

# 06-relief-scene

## PURPOSE
The closing bookend of a pain→relief arc: the same person out in the world, living the
resolved state, with the problem carried in a small desaturated inset so the change is
visible inside one frame. No product.

## TRIGGER
use_when: >
  Closing image of an advertorial or final frame of an ads creative, when the
  product's promise is a state of living rather than a feature. Pairs naturally
  with a 01-pain-scene of the same person, and no longer depends on one.
avoid_when: >
  Marketplace galleries, main images, or anywhere the image must stand alone.
  Not when the result is invisible on the body or an object — for invisible
  results the closing image must be 06-relief-hero with the product in frame
  (verified boundary, see the worked example).

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.
A rendered prompt expands what it calls — the model never reads this file (ADR-017).

```
TYPE: 06-relief-scene v2.0
REGISTER: candid documentary photograph, single frame.        -> PARTS/register

[SUBJECT] a person living the resolved state, mid-errand.     -> PARTS/subject
[GAZE] candid, or on a reflection. Never on the lens.         -> PARTS/gaze
[ENVIRONMENT] an ordinary public place they would pass through. -> PARTS/environment
[LIGHT] plain daylight, no glamour.                           -> PARTS/light
[GRADE] muted, desaturated, never warm-boosted.               -> PARTS/grade

[MARKS]                                                       -> MARKS
  past        the problem, a desaturated inset. REQUIRED
  evidence    the same thing resolved, in the hero
  carry-over  one thing identical in both cells
  reflection  optional second angle, in real glass
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
warm-boosted. The hero is full colour; only `past` is drained.

## MARKS

**Every entry is made of the scene; nothing is drawn over the photograph.** Measured across
three sibling types, a mark of real substance renders reliably (`emission` 7/7, `output` 4/4)
and a drawn mark at small scale does not (`fit` cut at 0/8, `hotspot` 1/3). A desaturated inset
is a photograph, not an overlay, so it sits on the reliable side.

| name | made of | where | evidence |
|---|---|---|---|
| `past` | a photograph of the problem state, drained to grey | a small inset, 15-25% of the frame, one corner | 5 obs and 2/2 rendered as `past` on `06-relief-hero` |
| `evidence` | the same thing resolved, as a physical difference you can point at | in the hero, framed comparably to the inset | 0/4 without `past`; untested with it |
| `carry-over` | one thing identical in both cells — the jacket, the doorway, the bag | both cells | **none** — proposal |
| `reflection` | the subject's own image in real glass, at a second angle | optional, one surface | 4/4 rendered, and it proved nothing |

**`past` is now the mechanism and it is REQUIRED.** The type's founding premise was that a
subject seen from two angles in one frame proves a change. It does not, and four renders said
so unanimously: every reflection came back geometrically clean and sharp, and not one image
argued anything. **Two angles are two viewpoints of one moment; a change needs two moments.**
The problem state has to be physically present in the frame, and the cheapest way to put it
there is a small photograph of it, drained to grey. An unmarked past cell reads as a result, so
the drain is load-bearing rather than stylistic.

**`evidence` is what the two cells differ by, and it must be nameable rather than inferred.**
"A visibly rested face" renders as an ordinary person. Hair that lies flat where it stood out, a
heel smooth where it was cracked, a collar clean where it was marked — facts a stranger could
point at. **Frame the inset comparably to the hero** so the eye lands on the same thing twice:
a close crop of a heel against a wide street shot compares nothing.

**`carry-over` is what stops the pair changing two things at once.** Hold one thing identical
between inset and hero — the same jacket, the same doorway, the same bag — so the change reads
against something that demonstrably did not change. Changing everything at once isolates
nothing; that cost `06-relief-hero` two renders when a recall inset changed the activity as well
as the product.

**`reflection` is demoted to optional and kept only because it renders.** 4 of 4 came back
plausible, sharp and geometrically consistent, including one holding two subjects in a car door
— the best-executed mechanism this library has had on a first attempt, and it carried no
argument at all. Use it where the evidence genuinely needs a second angle, such as the back of a
head. Never as the thing that makes the case.

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
[G6] + badges, arrows, drawn overlays, looking at camera, posing, laughing,
undrained past cell, past cell larger than the hero subject,
arms raised, celebration gesture, golden hour, warm flattering light,
glamour lighting, beauty retouching, plastic skin, aspirational travel location,
empty clean street, styled outfit, geometrically wrong reflection,
reflection out of focus, product in frame, saturated colors, stock photo look
```

## WORKED EXAMPLES
### example: shop-window-hair — skeleton@1.1, run: fail
Product: none in frame (G1-exempt) · axes: gaze=reflect · frame delivered 1200x896
- SUBJECT — woman in her thirties in a plain wool coat, stopped at a shop window on an ordinary
  high street, shifting her bag strap, small closed-mouth smile, gaze on her reflection
- EVIDENCE — hair lying flat and close to her head, one continuous outline, no frizz halo;
  named as a physical fact and rendered as one
- REFLECTION — shop window filling the left third, her other side and the back of her head,
  sharp and geometrically consistent with where she stands
- ENVIRONMENT — litter bin, bollard, two blurred passers-by, damp pavement, flat overcast
Kept as the record of why 2.0 exists. The reflection is flawless and the image argues nothing:
a woman with ordinary hair looks at a window. Three siblings in the same batch — a clean collar,
a smooth dog's coat, an even tan bag — failed identically, so it is not the evidence class and
not the scale. **Two angles are two viewpoints of one moment.** Its own 1.0 worked example had
predicted this before the type was ever rendered.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
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

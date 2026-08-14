---
id: 06-relief-scene
step: 6
job: relief
device: scene
version: "1.1"
status: active
replaced_by: null
ratios: ["16:9", "3:4"]
channels: [paid-social, advertorial]
requires_product_photo: false
generation_mode: single-pass
axes:
  gaze: [reflect]
variants: []
exempt_from: [G1, G3, G4]
pairs_with: [01-pain-scene]
never_with: []
requires_pair: 01-pain-scene
---

# 06-relief-scene

## PURPOSE
The closing bookend of a pain→relief arc: the same person, out in the world, catching
their own reflection — the resolved state as a lived moment. No product, no graphics.
Carries no argument alone; only works beside its pain counterpart.

## TRIGGER
use_when: >
  Closing image of an advertorial or final frame of an ads creative, when the
  product's promise is a state of living rather than a feature. MUST run beside
  a 01-pain-scene of the same person, same palette (requires_pair).
avoid_when: >
  Marketplace galleries, main images, or anywhere the image must stand alone.
  Not when the result is invisible on the body or an object — for invisible
  results the closing image must be 06-relief-hero with the product in frame
  (verified boundary, see the worked example).

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.
A rendered prompt expands what it calls — the model never reads this file (ADR-017).

```
TYPE: 06-relief-scene v1.1
REGISTER: candid documentary photograph, single frame.        -> PARTS/register

[SUBJECT] the same person as the paired pain image, mid-errand. -> PARTS/subject
[GAZE] on their own reflection, never on the camera.          -> PARTS/gaze
[ENVIRONMENT] an ordinary public place they would pass through. -> PARTS/environment
[LIGHT] the same time-of-day character as the pain image.     -> PARTS/light
[GRADE] the pain image's palette, muted.                      -> PARTS/grade
[PAIRING] carries no argument alone.                          -> PARTS/pairing

[MARKS] all three made of the scene; nothing is drawn.        -> MARKS
  evidence    the physical change, readable in both views
  reflection  the second angle, in real glass
  carry-over  one object held identical from the pain image
```

## PARTS

**`register`** — a candid documentary photograph a passer-by could have taken. Natural,
unposed, sharp. Not styled, not lit, not aware of a camera.

**`subject`** — the same demographic and the same person as the paired pain image, in
put-together but ordinary clothes from the same palette family, doing an everyday thing in
public and pausing briefly.

**`gaze`** — on their own reflection. **Never at the camera**: looking at the lens reads as
showing off and the barrier goes up. This is the only value the `gaze` axis takes here.

**`environment`** — a public everyday place the subject would actually pass through, with two
or three incidental blurred passers-by or street details, ordinary weather. Nothing
aspirational, no travel-brochure location, no empty clean street. **The problem started in the
bathroom; the promise ends in the world**, which is why this type is never set at home.

**`light`** — even natural daylight, bright, soft shadows. Slightly kinder than the paired pain
image but the SAME time-of-day character. No golden hour, no rim light, no glamour lighting.

**`grade`** — the paired image's muted palette, light film grain, shallow depth of field.
Desaturated, never warm-boosted.

**`pairing`** — this image only works beside its pain counterpart: same person, same palette,
same lens character, same grade family (`requires_pair`). Best generated multi-pass from the
pain image so the face is the same; single-pass only if the pair is generated fresh in the same
run.

## MARKS

**Every entry here is made of the scene. Nothing is drawn over the photograph** — and for this
type that is not a sacrifice. Measured across three sibling types, a mark made of real
substance in the frame renders reliably (`emission` 7/7 on `03-use-sequence`, `output` 4/4 on
`06-relief-hero`) while a drawn mark at small scale does not (`fit` cut at 0/8, `hotspot` 1/3).
A type whose PURPOSE already forbids graphics loses nothing by having no drawn entry.

**All three are proposals with no evidence behind them.** This type has **0 classified
observations and 0 render records** — it was written from one conversation exemplar and has
never been rendered or seen in the market. Its paired type `01-pain-scene` has 10 observations
and 19 renders. Under ADR-012 a proposal's first render is its founding evidence, and until
that render exists nothing below is law.

| name | made of | where | evidence |
|---|---|---|---|
| `evidence` | the resolved symptom as a physical difference you can point at | on the body or object, readable in BOTH views | **none** — proposal |
| `reflection` | the subject's own image in real glass, at a second angle | one surface, 25-35% of the frame | **none** — proposal |
| `carry-over` | one object held identical from the paired pain image | anywhere in frame | **none** — proposal |

**`evidence` must be a difference you can name, not a state you infer** (G9). "A visibly rested
face" is an inference and will render as an ordinary man; hair that lies flat where it stood up,
a heel smooth where it was cracked, a shirt collar sitting clean where it was marked — those are
facts a stranger could point at. **This is the type's admission test**: if the result cannot be
named as a physical difference, the closing image is `06-relief-hero` with the product in frame,
not this type. The type's own worked example predicted exactly this failure before it was ever
rendered.

**`reflection` is the mechanism, not decoration.** A productless image proves a change by
showing the subject twice in one frame, from two angles, in the same instant. Without the glass
this is a stock photograph of a person on a street. It must be geometrically consistent with
where the subject stands and sharp enough to read `evidence` in.

**`carry-over` is what makes the difference legible.** Hold one object identical across the pair
— the same jacket, the same bag, the same bus-stop sign — so the change in the body reads
against something that demonstrably did not change. A pair that changes everything at once
isolates nothing; that fault cost `06-relief-hero` two renders when a recall inset changed the
activity as well as the product.

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
[G6] + badges, arrows, overlays, looking at camera, posing, laughing,
arms raised, celebration gesture, golden hour, warm flattering light,
glamour lighting, beauty retouching, plastic skin, aspirational travel location,
empty clean street, styled outfit, geometrically wrong reflection,
reflection out of focus, product in frame, saturated colors, stock photo look
```

## WORKED EXAMPLES
### example: mouth-tape-morning-commute — skeleton@1.0, run: untested
Product: none in frame (G1-exempt) · ratio 5:3 · axes: gaze=reflect · requires_pair 01-pain-scene
- SUBJECT — man late 30s in a plain shirt and open jacket, walking to work in the early morning, pausing on the pavement, looking at his own reflection in a shop window while adjusting his collar; small closed-mouth smile, private and understated, not performing
- EVIDENCE OF CHANGE — his face is visibly rested: skin even rather than sallow, eyes fully open and clear, no shadowing or puffiness beneath, jaw relaxed, lips closed and not dry; readable in BOTH the direct view and the reflection
- REFLECTION — a shop window filling roughly 30% of the frame on the left, showing him from a different angle, sharp enough to read his face, geometrically consistent with his position
- ENVIRONMENT — ordinary city street early morning, bare trees, a bus stop sign, two blurred commuters passing behind, overcast; nothing aspirational
- LIGHT — even natural daylight, bright, soft shadows, slightly kinder than a night scene but the same plain documentary character
- GRADE — muted blue-grey and neutral, light grain, shallow depth of field, desaturated, never warm-boosted
Predicted failure — and the type's boundary: "a visibly rested face" is inference, not
physical evidence; the render will likely show an ordinary man and say nothing. If
confirmed, the avoid_when hardens into: this type ONLY for results visible on body or
object (hair, skin, posture, a repaired thing); invisible-result products close with
06-relief-hero instead.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.1 (2026-08-14): restructured into a call-map plus PARTS and MARKS (ADR-012); skeleton
  cut. First MARKS library, and all three entries are proposals: this type has 0 observations
  and 0 renders, so there is nothing to count. Every entry is made of the scene, because the
  drawn class is the unreliable one across three sibling types. `ratios` move to ADR-016's set —
  `5:3` and `4:5` become `16:9` and `3:4`. `RATIO:` dropped per adapter Rule 4.
- 1.0 (2026-08-10): initial from the shop-window reflection exemplar; --reflect gaze
  mode contributed to the shared gaze axis. seed: conversation.md.

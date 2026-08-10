---
id: 06-relief-scene
step: 6
job: relief
device: scene
version: "1.0"
status: active
replaced_by: null
ratios: ["5:3", "16:9", "4:5"]
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
```
TYPE: 06-relief-scene v1.0
RATIO: [5:3 / 16:9 / 4:5]
REGISTER: candid documentary photograph. Single frame. NO graphic overlays.

[SUBJECT]
[same demographic as the paired pain image] in [wardrobe: put-together but
ordinary, same palette family as the pain image],
[everyday action in a public place], pausing briefly.
Gaze on their own reflection in [reflective surface].
Expression: small closed-mouth smile, private and understated.
Not performing, not aware of a camera.

[EVIDENCE OF CHANGE — required, G9]
The resolved symptom must be visible as physical fact: [what the body or object
now looks like]. It must be readable from BOTH the direct view and the reflection.
Do not state the change with expression alone.

[REFLECTION]
[shop window / mirrored panel / car glass] filling [25-35%] of the frame,
showing the subject from a different angle, sharp enough to read the evidence.
The reflection must be geometrically consistent with the subject's position.

[ENVIRONMENT]
[a public everyday place the subject would pass through],
[2-3 incidental blurred passersby or street details], ordinary weather.
Nothing aspirational, no travel-brochure location, no styling.

[LIGHT]
Even natural daylight, bright, soft shadows.
Slightly kinder than the paired pain image, but the SAME time-of-day character.
No golden hour, no rim light, no glamour lighting.

[GRADE]
Muted [palette matching the paired pain image], light film grain,
shallow depth of field. Desaturated, never warm-boosted.

[PAIRING RULE]
This image only works alongside its pain counterpart.
Same person, same palette, same lens character, same grade family.
It carries no argument on its own.

STYLE: candid lifestyle photography, natural, unposed, sharp.
NO text, no logo, no watermark, no product.
```

## SLOT CONSTRAINTS
- The reflection IS the evidence mechanism: the subject seen from two angles in one
  frame is the only way a productless image proves anything. Without the glass it is a
  stock photo of a person on a street.
- Gaze is --reflect only: at their own reflection, never at the camera (looking at
  camera = showing off = the barrier goes up).
- Public place, not home: the problem started in the bathroom, the promise ends in the
  world.
- Best generated multi-pass from the paired pain image (same face); single-pass
  acceptable only if the pair is also being generated fresh.

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
```
A candid documentary photograph, 5:3 ratio. Single frame. NO graphic overlays.

SUBJECT: A man in his late 30s in a plain shirt and an open jacket, walking to work in
the early morning, pausing for a second on the pavement. He is looking at his own
reflection in a shop window, adjusting his collar. Expression: a small closed-mouth
smile, private and understated. Not performing, not aware of a camera.

EVIDENCE OF CHANGE: his face is visibly rested. Skin even rather than sallow, eyes
fully open and clear, no shadowing or puffiness beneath them, jaw relaxed, lips closed
and not dry. This must be readable both in the direct view and in the reflection.

REFLECTION: a shop window filling roughly 30 percent of the frame on the left, showing
him from a different angle, sharp enough to read his face. Geometrically consistent
with his position.

ENVIRONMENT: an ordinary city street early in the morning, bare trees, a bus stop sign,
two blurred commuters passing behind him, overcast weather. Nothing aspirational, no
travel-brochure location, no styling.

LIGHT: even natural daylight, bright, soft shadows. Slightly kinder than a night-time
scene but with the same plain documentary character. No golden hour, no rim light, no
glamour lighting.

GRADE: muted blue-grey and neutral palette, light film grain, shallow depth of field.
Desaturated, never warm-boosted.

STYLE: candid lifestyle photography, natural, unposed, sharp.
NO text, no logo, no watermark, no product.
```
Predicted failure — and the type's boundary: "a visibly rested face" is inference, not
physical evidence; the render will likely show an ordinary man and say nothing. If
confirmed, the avoid_when hardens into: this type ONLY for results visible on body or
object (hair, skin, posture, a repaired thing); invisible-result products close with
06-relief-hero instead.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.0 (2026-08-10): initial from the shop-window reflection exemplar; --reflect gaze
  mode contributed to the shared gaze axis. seed: conversation.md.

---
id: 05-social-handoff
step: 5
job: social
device: handoff
version: "1.0"
status: active
replaced_by: null
ratios: ["5:3", "16:9", "4:5"]
channels: [paid-social, advertorial, landing-page]
requires_product_photo: true
generation_mode: multi-pass
variants: []
exempt_from: [G3, G4]
pairs_with: [04-proof-lockedframe, 06-relief-hero]
never_with: []
avoid_adjacent: [05-persona-grid]
---

# 05-social-handoff

## PURPOSE
Staged word-of-mouth: an advocate points, a faceless listener follows the gesture, and
we happen to witness it. Social proof that clears the skepticism barrier a
straight-to-camera testimonial cannot.

## TRIGGER
use_when: >
  Need social proof without a face-to-camera testimonial. The "a friend told
  me" beat mid-advertorial, cold-ads creative, or a closing image on a landing
  page. Fits products people genuinely recommend to each other out loud.
avoid_when: >
  Marketplace galleries and main images. Not for private products nobody
  recommends in person. Not when no natural reason exists for two people to
  stand near the product. Keep distance from 05-persona-grid on the same page
  (same question, different mechanism).

## SKELETON
```
TYPE: 05-social-handoff v1.0
RATIO: [5:3 / 16:9 / 4:5]
REGISTER: candid documentary photograph. One scene. One inset overlay maximum.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly.
The product must appear IDENTICAL in the scene and in the inset,
same colorway, same finish. This is the single most important constraint.

[CHARACTER A: THE ADVOCATE]
[age/gender] in [ordinary specific wardrobe], face turned toward camera,
mid-sentence, [warm relaxed expression], pointing with [hand] toward the product.
The pointing gesture forms a clear diagonal line ending exactly at the product.

[CHARACTER B: THE LISTENER]
[age/gender] in [wardrobe], seen from behind or in profile, FACE NOT VISIBLE,
head turned to follow the pointing gesture, gaze parallel to the pointing line.
This character is a placeholder for the viewer.

[PRODUCT IN SCENE]
The reference product placed at [natural location], partially framed by
[foreground element], sitting exactly where the pointing line terminates.

[INSET] (include ONLY if the scene cannot show the product clearly)
Circular white cutout containing the reference product on a plain white background,
positioned [near the terminus of the pointing line, never opposite it],
occupying [15-20%] of the frame width. Clean edge, no border, no connecting arrow.
Product colorway MUST match the in-scene product exactly.

[ENVIRONMENT]
[specific place directly related to the moment of use],
[2-3 incidental background people or details], flat natural daylight,
no dramatic shadows, nothing styled.

[COMPOSITION RULE]
Two vectors, the pointing arm and the listener's gaze, must converge on the product.
Nothing else in the frame may compete for attention.

STYLE: candid lifestyle photography, natural, unposed, sharp, 4K.
NO text, no logo, no watermark, no arrows, no badges.
```

## SLOT CONSTRAINTS
- The pointing line is the compositional spine — remove the gesture and the product
  vanishes from the frame.
- The listener's turned back is deliberate: an empty seat for the viewer's identity.
  Both faces visible kills the mechanism.
- G1 applies TWICE (scene + inset) and the colorway must match exactly — the original
  exemplar failed this (beige in scene, charcoal in inset = two products).
- The environment must give a natural reason for two people to stand near the product
  (G7 test 3) — the exemplar's airport-pickup framing around a car seat was the
  documented miss.
- Multi-pass: generate the scene first; composite the inset in post from the actual
  reference photo rather than letting the model repaint it (colorway drift is
  near-certain in single-pass).

## NEGATIVE
```
[G6] + arrows, badges, connecting lines, both faces visible,
listener facing camera, product color mismatch between scene and inset,
two different products, inset placed opposite the pointing direction,
product outside the pointing line, staged posing, direct eye contact with camera,
studio lighting, empty background, unrelated location
```

## WORKED EXAMPLES
### example: shower-filter-hallway — skeleton@1.0, run: untested
```
A candid documentary photograph, 5:3 ratio. One scene, one inset overlay.

Use the attached product photo as the exact reference for the shower filter. Preserve
shape, proportions, material, finish and color exactly. The filter must appear
identical in the scene and in the inset, same colorway, same finish.

CHARACTER A, THE ADVOCATE: A woman in her early 40s in a soft grey sweatshirt, hair
damp, standing in a hallway doorway, face turned toward camera, mid-sentence, warm
relaxed expression, pointing with her right hand through the open bathroom door toward
the shower. The pointing gesture forms a clear diagonal line ending exactly at the
filter fitted above the showerhead.

CHARACTER B, THE LISTENER: A woman in her late 20s in a casual jacket holding a mug,
seen from behind, face not visible, head turned to follow the pointing gesture, gaze
parallel to the pointing line.

PRODUCT IN SCENE: The reference filter installed between the hose and the showerhead,
visible through the open doorway, partially framed by the door edge, sitting exactly
where the pointing line terminates.

INSET: Circular white cutout containing the reference filter on a plain white
background, positioned just below and left of the pointing hand, never opposite it,
occupying about 18 percent of the frame width. Clean edge, no border, no connecting
arrow. Colorway matching the in-scene product exactly.

ENVIRONMENT: An ordinary apartment hallway opening into a small bathroom, a laundry
basket on the floor, a towel over the rail, a plant on a shelf. Flat natural daylight,
no dramatic shadows, nothing styled.

COMPOSITION RULE: the pointing arm and the listener's gaze must converge on the filter.
Nothing else in the frame may compete for attention.

STYLE: candid lifestyle photography, natural, unposed, sharp, 4K.
NO text, no logo, no watermark, no arrows, no badges.
```
Predicted failures (this is a deliberate avoid_when boundary probe — a private-use
product): (1) the filter beyond a doorway shrinking to unrecognizable pixels, voiding
the pointing line — candidate hard rule if confirmed: in-scene product ≥8% of frame
height; (2) scene-vs-inset colorway drift — the reason the type is multi-pass.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.0 (2026-08-10): initial from the airport / car-seat pointing exemplar; exemplar
  faults encoded (inset colorway mismatch, inset far from the pointing terminus,
  location unrelated to the use moment). seed: conversation.md.

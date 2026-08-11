---
id: 02-symptom-rail
step: 2
job: symptom
device: rail
version: "1.1"
status: active
replaced_by: null
ratios: ["1:1", "4:5"]
channels: [marketplace]
requires_product_photo: true
generation_mode: single-pass
variants: []
exempt_from: []
pairs_with: [01-pain-split, 03-mechanism-ghostbody]
never_with: []
---

# 02-symptom-rail

## PURPOSE
One product, many problems: a calm hero scene plus a vertical rail of symptom vignettes.
Argues by breadth of the problem — it does not prove, it counts.

## TRIGGER
use_when: >
  The product solves several problems at once and one image must show the
  coverage. Image 2 or 3 in the gallery, right after the scroll-stopper. Fits a
  broad audience where each buyer hurts in a different way.
avoid_when: >
  The product solves exactly one problem — the rail becomes padding. Never as a
  main image. Not when the symptoms cannot be photographed.

## SKELETON
```
TYPE: 02-symptom-rail v1.1
RATIO: [1:1 / 4:5]
LAYERS: photographic hero base + vector overlay + vignette rail on right edge

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly. Do not redesign or add features.

[ZONE A: HERO, left 72%]
[age/gender] in [wardrobe, muted neutral tones], [correct posture/behavior]
while [everyday activity], calm content expression, [gaze direction].
The reference product clearly visible at [contact point], seen from [angle],
unobstructed, occupying at least [X%] of the hero area height.
Setting: [environment], [3 props], soft natural window light, background blurred.
Bright high-key [neutral palette] grade. Subject offset left.

[ZONE B: FORCE ARROWS]
[N] [color] rounded arrows overlaid on the product pointing [direction],
evenly spaced, semi-transparent, fading at the tips, flat vector style.
Arrow color MUST differ from the pain color used in the rail.

[ZONE C: PAIN RAIL, right 25-28%, vertical band, [straight / soft S-curved] left edge]
Pale [tint] gradient panel. [3] circular vignettes stacked evenly,
white ring border, equal diameter, generous spacing.
Each vignette: tight crop of [same-role person], no face visible,
showing [pain gesture at body zone / visible symptom],
red radial glow centered on that point.
Ordered top to bottom: [item1], [item2], [item3].
All vignettes share the hero's lighting, wardrobe tone and photographic style.

STYLE: clean e-commerce infographic tile, bright airy, sharp focus, 4K.
NO text, no logo, no watermark.
```

## SLOT CONSTRAINTS
- [ZONE C] vignette mode — choose ONE and state it explicitly in the prompt:
  - `pain-gesture` (hand pressing the hurting zone): when the symptom is a feeling.
  - `visible-symptom` (a visible manifestation on body or object): when the symptom is
    a consequence you can see.
- 3 vignettes, not 4 — at mobile size a 4-vignette rail drops below legibility.
- Vignette order follows anatomy top-to-bottom (or severity); never shuffled.
- [ZONE B] arrows must not be red: red belongs to the rail (G3); red arrows on the
  product read as a heating feature.
- Vignettes must share the hero's register (G5) — a stock-photo rail on a lifestyle
  hero reads as two sources.

## NEGATIVE
```
[G6] + faces inside vignettes, mismatched lighting between hero and vignettes,
red arrows on product, heat or warming cues, cluttered background, dark grade,
vignettes too small, overlapping circles, product obscured
```

## WORKED EXAMPLES
### example: shower-filter — skeleton@1.1, run: untested
Product: metal shower filter · ratio 1:1 · vignette mode: visible-symptom
- ZONE A (left 72%) — woman late 20s, long dark hair, under a running shower in a bright modern bathroom, head tilted back, eyes closed, calm content; the reference filter screwed between hose and showerhead above her, unobstructed; white marble tile, glass partition, a eucalyptus bundle, soft daylight from a frosted window, background blurred; bright high-key white and warm grey; subject offset left
- ZONE B — three BLUE rounded arrows on the water stream below the filter, pointing down, evenly spaced, semi-transparent, fading at the tips, flat vector
- ZONE C (right 26%, soft S-curved left edge) — pale aqua gradient panel; three circular vignettes, white ring border, equal diameter, no face visible, sharing the hero's light and style: top, a hand through dry brittle hair with strands breaking, red glow at the ends; middle, a forearm with flaky irritated skin, red glow on the patch; bottom, fingers scratching a scalp at the hairline, red glow at the scalp
Predicted failure: the model regressing to pain-gesture (hands clutching) even in
visible-symptom mode — the reason the two modes must be named explicitly in the prompt.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.1 (2026-08-10): vignette slot split into pain-gesture / visible-symptom modes
  (Test D exposed that a hard-coded "hand pressing" does not generalize); rail reduced
  to 3 vignettes; G1 block added; hero product slot rewritten to G2.
  seed: conversation.md.
- 1.0 (2026-08-10): initial as SQR-SCOPE-PAINRAIL from the office-chair exemplar;
  exemplar faults encoded (red arrows on product, 4 undersized vignettes, decorative
  S-curve). seed: conversation.md.

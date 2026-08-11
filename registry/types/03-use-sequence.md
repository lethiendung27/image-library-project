---
id: 03-use-sequence
step: 3
job: use
device: sequence
version: "1.1"
status: active
replaced_by: null
ratios: ["1:1", "4:5"]
channels: [marketplace, landing-page, advertorial]
requires_product_photo: true
generation_mode: single-pass
axes:
  camera_lock: [handheld]
variants: []
exempt_from: [G3, G4]
pairs_with: [03-mechanism-ghostbody]
never_with: []
---

# 03-use-sequence

## PURPOSE
Reassure about operation: three stacked panels, one action each, read by action logic
alone — no numbers, no arrows. Answers "can I actually use this?" without looking like
an instruction manual.

## TRIGGER
use_when: >
  The product has more than one operation step, or buyers may assume it is
  complicated. Image 4-5 in the gallery. Answers the question "will I manage to
  use this".
avoid_when: >
  The product has one obvious action. Never as a main image, never as a
  scroll-stopper.

## SKELETON
```
TYPE: 03-use-sequence v1.0
RATIO: [1:1 / 4:5]
LAYOUT: [3] horizontal panels stacked vertically, thin white gutters,
no outer border, no numbers, no arrows, no text.
REGISTER: warm lifestyle photography, close range.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly in every panel.

[CONTINUITY LOCK]
The same hands in every panel: same skin tone, same nails, same wrists,
same sleeves. The same [subject/surface] in every panel.
Same warm neutral palette, same soft natural light direction throughout.
Camera distance may vary between panels, framing may shift naturally.

[SEQUENCE RULE]
One action per panel. Never two.
The order must be readable from the actions alone, with no numbering.
The product must sit near the center of every panel.

[PANEL 1: PREPARE]
[the single setup action], hands in frame, product centered,
[the readiness signal: indicator light / opened part / loaded state] visible.

[PANEL 2: USE]
[the core action in progress] on [subject], mid-motion.
[VISIBLE MECHANISM — G8: if the product emits anything, it must be visible here,
lit to reveal it].

[PANEL 3: RESULT]
[the action continuing or just finished], plus [a second hand or gesture
expressing the relationship or the outcome].
Warmer light than the previous panels. No new mechanics introduced.

[ENVIRONMENT]
[an ordinary domestic setting], soft daylight, [1-2 incidental details].
Same location across all three panels.

STYLE: warm lifestyle product photography, natural, unstyled, sharp, 4K.
NO text, no numbers, no logo, no watermark, no arrows, no step markers.
```

## SLOT CONSTRAINTS
- One action per panel — the original exemplar packed two actions into panel 1 and lost
  a beat; never repeat that.
- The final panel closes on relationship/outcome, not on mechanics — this is what
  separates the type from a dry manual.
- Continuity of hands is the make-or-break: same hands, or it reads as three stock
  photos.
- camera_lock is `handheld` by definition: framing shifts naturally between panels;
  pixel-locked framing would read as renders.

## NEGATIVE
```
[G6] + step numbers, arrows, badges, different hands between panels,
different subject between panels, two actions in one panel,
product off-center, product cropped out, instruction manual look,
technical diagram, cold clinical lighting, different location between panels,
inconsistent palette, staged perfection
```

## WORKED EXAMPLES
### example: shower-filter-install — skeleton@1.0, run: untested
Product: metal shower filter · ratio 1:1 · 3 panels stacked · axes: camera_lock=handheld
- CONTINUITY LOCK — the same pair of hands in every panel (same skin tone, nails, wrists, sleeves pushed up); the same chrome shower arm and white tiled wall throughout; same warm neutral palette, same soft daylight from the left; camera distance and framing may shift naturally
- PANEL 1, PREPARE — both hands unscrewing the existing shower head from the arm, the head coming free, the bare threaded arm visible; close range
- PANEL 2, USE — one hand holding the reference filter against the threaded arm, the other turning it into place, mid-motion, thread engaging
- PANEL 3, RESULT — filter fitted, shower head reattached below it, water running in a clean even spray backlit from the window so individual streams and fine mist read; one hand held open under the flow, palm up, fingers relaxed; warmer light than the previous panels
- ENVIRONMENT — ordinary home bathroom, soft daylight, a folded towel on a rail, a small plant on the sill; same location in all three panels
Predicted failures: (1) close-range hands manipulating hardware — highest extra-finger
risk in the library; (2) panel 3 demands both "result visible" and "product centered",
which compete for space — if it breaks, split the slot: either the result or the
centered product, not both.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.1 (2026-08-11): channels gain `advertorial`. Demand evidence: two real advertorial
  pages for the wall cooler carry explicit numbered step sections ("Setup in Under 5
  Minutes", the 3-step howto block), which is exactly what this type serves.
- 1.0 (2026-08-10): initial from the pet-brush three-panel exemplar; exemplar fault
  encoded (two actions crowded into panel 1). seed: conversation.md.

---
id: 03-use-rail
step: 3
job: use
device: rail
version: "0.1"
status: reserved
replaced_by: null
ratios: ["1:1", "2:1"]
channels: [marketplace, landing-page]
requires_product_photo: true
generation_mode: single-pass
axes: {}
variants: []
exempt_from: [G3, G4]
pairs_with: []
never_with: []
avoid_adjacent: [02-symptom-rail]
---

# 03-use-rail — STAGING DRAFT

Promotion status (2026-08-11): **4 exemplars ledgered, ~3 distinct sources**
(outputs band: obs `sha256:c77ed9…` batch 11-A chopper; places band:
`sha256:5c64dc…` 11-C trainer; exercises band: `sha256:479fef…` 11-C trainer —
same campaign as the places exemplar; muscles band: `sha256:8e8324…` 11-E ab
roller). Pending: 1 more distinct-source exemplar to be safe, router-confusion
test (02-symptom-rail is the boundary), ≥1 rendered worked example, human
review. Not routable.

## PURPOSE
A primary scene plus a vignette band that EXHIBITS what the product delivers —
outputs made, places served, movements enabled, zones worked. The positive-
polarity sibling of 02-symptom-rail: that band indicts problems; this band
counts capabilities.

## TRIGGER
use_when: >
  One image must keep a real usage scene AND enumerate breadth beside it —
  when pure grid cells would lose the hero moment. Gallery image 3-5 or a
  landing-page capability section. Choose band content by the buyer's doubt:
  outputs for "what will it make", places for "where can I use it",
  exercises/zones for "what will it work".
avoid_when: >
  The product has one output or one place — the band becomes padding. Never a
  main image. Not on a page already carrying 02-symptom-rail (avoid_adjacent):
  two railed images in one gallery read as a template, and opposing band
  polarities (problems vs capabilities) confuse the arc. If no hero moment
  matters, use 03-use-grid instead.

## SKELETON
```
TYPE: 03-use-rail v0.1
RATIO: [1:1 / 2:1]
LAYERS: photographic hero + vignette band on [right edge, vertical /
bottom edge, horizontal]

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly, in the hero and in any band
cell where it appears.

[ZONE A: HERO, 60-72%]
[age/gender or anonymous hands] mid-use of the reference product at
[real location], [natural activity moment], calm engaged expression if a face
is present. The product clearly visible at [contact point], unobstructed.
Setting: [environment], [2-3 props], soft natural light, background blurred.
[IF the product emits anything visible — G8: the output visible and lit here.]

[ZONE B: CAPABILITY BAND, 25-35%, [straight edge]]
Pale [neutral tint] panel. [3] cells, equal size, generous spacing,
[circular / rounded-rectangle] white-bordered vignettes.
BAND CONTENT — choose ONE and name it:
  outputs: each cell one RESULT the product produced ([result 1-3]),
    photographed real, no hands needed;
  places: each cell one LOCATION it serves, staged plainly;
  exercises: each cell one movement demonstrated, same person as hero;
  zones: each cell one target area shown photographically (never diagrams).
Ordered by [frequency of use / natural sequence]. Every cell shares the
hero's register, light family and grade (G5 — one shoot, one world).

STYLE: clean e-commerce capability tile, bright, sharp, 4K.
NO text, no logo, no watermark, no badges, no checks, no arrows.
```

## SLOT CONSTRAINTS
- 3 cells, hard max 4 — the market runs 4-6 (observed) and loses thumbnail
  legibility; the symptom-rail lesson transfers unchanged.
- No verdict glyphs: observed exemplars stamp green checks on capability cells —
  excluded; a demonstration is not a verdict (proof-logic leakage).
- The band must share the hero's register: obs `sha256:479fef…` shows band
  vignettes from a different studio than the hero — the two-sources read this
  law exists to kill. Illustrated/diagram cells (obs `sha256:8e8324…`, muscle
  maps) break G5 against a photographic hero: zones are shown photographically
  or the content mode is wrong for this type.
- Polarity discipline: nothing in the band may depict a problem state; one
  problem cell flips the image into 02-symptom-rail territory and muddles both.
- The hero stays a genuine use moment — a thumbs-up-to-camera hero (observed)
  drifts the type toward testimonial; gaze belongs on the task.

## NEGATIVE
```
[G6] + check badges, tick marks, verdict glyphs, arrows, band cells in a
different register than the hero, illustrated diagrams in the band,
faces inside band cells, more than four cells, problem imagery in the band,
thumbs-up to camera, red glows, dark grade, product obscured
```

## WORKED EXAMPLES
### example: chopper-outputs-band — skeleton@0.1, run: untested
```
A 1:1 clean e-commerce capability tile.

Use the attached product photo as the exact reference for the mini electric
chopper. Preserve shape, proportions, material, finish and color exactly, in
the hero and in every band cell where its output appears.

ZONE A (top 65%): a cook's hands press the chopper's button at a warm wooden
counter mid-prep, the transparent bowl half-filled with chopped onion, herbs
and a cutting board beside, soft window light, background blurred. The chopper
clearly visible, centered, unobstructed.

ZONE B (bottom 35%, horizontal band, straight edge): a pale warm-grey panel
holding three rounded-rectangle white-bordered vignettes, equal size, generous
spacing, band content OUTPUTS, each cell one real result photographed in the
same light and grade as the hero:
- left: a small bowl of fine garlic mince
- center: a bowl of red chili paste
- right: a bowl of pale green herb puree
Ordered by frequency of use. No cell carries text or badges.

STYLE: clean e-commerce capability tile, bright, sharp, 4K.
NO text, no logo, no watermark, no badges, no checks, no arrows.
```
Predicted failures: (1) the model stamping checks or numbers onto band cells
(instruction-tile priors — the negative must fire); (2) band bowls rendering in
studio-white light against the warm hero (the G5 register law is the fragile
one); (3) output textures merging (mince/paste/puree must stay distinct).

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Sibling map at step 3: use-grid = breadth as equal cells; use-rail = breadth
beside a kept hero moment; use-sequence = depth (one task through time) rather
than breadth. Confusion pair: 02-symptom-rail — identical geometry, inverted
band polarity (indicts vs exhibits); the router must read band CONTENT, and the
two types never share a page (avoid_adjacent). Band content modes observed so
far: outputs, places, exercises, muscles-as-diagrams (the last rejected into
the negative as a G5 break).

## CHANGELOG
- 0.1 (2026-08-11): staging draft from four ledgered exemplars across four band
  modes — outputs (obs `sha256:c77ed9…`, 11-A), places (`sha256:5c64dc…`,
  11-C), exercises (`sha256:479fef…`, 11-C), muscle-diagrams (`sha256:8e8324…`,
  11-E, register-mix negative evidence). Band content parameterized
  (outputs/places/exercises/zones); cell cap and register law inherited from
  02-symptom-rail with the observed violations encoded as negatives (checks,
  6-cell bands, off-register vignettes, thumbs-up hero).

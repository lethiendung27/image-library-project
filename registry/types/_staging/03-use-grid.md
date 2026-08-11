---
id: 03-use-grid
step: 3
job: use
device: grid
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
avoid_adjacent: [05-persona-grid]
---

# 03-use-grid — STAGING DRAFT

Promotion status (2026-08-11): **5 exemplars ledgered, ~3-4 distinct sources**
(applications form: obs `sha256:96f3e9…` batch 10-F, `sha256:14d920…` 11-C torch;
compatibility form: `sha256:9d88fa…` 11-A drills; positions form: `sha256:7d39a9…`
and `sha256:7b9d17…` 11-C — the two positions exemplars plus the rail banner read
as one fitness campaign, so count sources conservatively). Pending: router-confusion
test (05-persona-grid is the live boundary), ≥1 rendered worked example, human
review. Not routable.

## PURPOSE
Capability breadth in equal cells: one product, N demonstrations — different jobs,
different host tools, or different exercise positions. The grid argues by counting
what one purchase covers; nothing is indicted, nothing is compared.

## TRIGGER
use_when: >
  The buyer's question is "how much will this one thing do for me" — multi-use
  tools, multi-exercise equipment, multi-host attachments. Gallery image 3-5 or
  a landing-page capability section. Choose the cell variable to match the
  doubt: applications when the product claims many jobs, compatibility when it
  must fit gear the buyer already owns, positions when one device claims a
  whole routine.
avoid_when: >
  The product does one thing (the grid becomes padding — same failure as a
  one-symptom rail). Never as a main image. Not when cells would need text
  labels to be understood — if a cell cannot explain itself photographically,
  the breadth argument belongs to page copy. Keep off pages already carrying
  05-persona-grid (avoid_adjacent): two grids read as one lazy template.

## SKELETON
```
TYPE: 03-use-grid v0.1
RATIO: [1:1 / 2:1]
LAYOUT: [2x2 / 3 equal cells] photographic grid, thin white gutters,
no outer border, no numbers, no arrows, no badges, no text.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly in every cell where it appears.

[CELL VARIABLE — choose ONE and name it in the prompt]
applications: each cell shows the product mid-action on a DIFFERENT JOB
  ([job 1], [job 2], [job 3], [job 4]), its working output visible in every
  cell (G8 inside cells: flame, cut, result).
compatibility: each cell shows a DIFFERENT HOST the product serves, staged in
  that host's own context; the product appears either in every cell mounted,
  or once as a central connecting element.
positions: THE SAME person, set and light in every cell; only the
  [exercise/usage position] changes — constancy makes the variable legible.

[CONSTANCY LOCK]
State what stays constant and keep it constant: the product identity always;
for positions additionally the person, wardrobe, set and grade; for
applications the season/context MAY vary per cell (it widens the claim).

[CELL LAW]
Every cell is a real photographic moment (G7 per cell): action plausibly
mid-happening, no floating props, no demonstrative staging. The product or its
working output stays legible in each cell at thumbnail size (≥15% rule).
Reading order must be natural (Z-order); no cell may need a label.

STYLE: [bright commercial / rugged documentary] — ONE register across all
cells, consistent grade and light logic.
NO text, no numbers, no logo, no watermark, no badges, no arrows.
```

## SLOT CONSTRAINTS
- The overlay-free law is absolute: observed market exemplars decorate cells with
  green checks and red diagonal separators — both are excluded here (a
  demonstration needs no verdict glyph; that is proof-logic leakage).
- Cell count 3-4; beyond 4 cells drop below thumbnail legibility (the rail's
  lesson applies).
- The persona boundary: if WHO is using it differs per cell, the image is
  05-persona-grid, not this type. Here people are constant, absent, or reduced
  to anonymous working limbs — the variable is the USE, never the user.
- G5 within the grid: all cells one register; mixing studio and documentary
  cells reads as sourcing, not breadth.

## NEGATIVE
```
[G6] + check badges, tick marks, VS badges, arrows, colored separators,
frames around cells, mixed registers between cells, different product
between cells, people as the varying element, empty decorative cells,
step numbers, instruction-manual look
```

## WORKED EXAMPLES
### example: pedal-trainer-positions-2x2 — skeleton@0.1, run: untested
```
A 1:1 photographic grid, four equal square cells, thin white gutters, no outer
border, no numbers, no arrows, no text.

Use the attached product photo as the exact reference for the pedal resistance
trainer. Preserve shape, proportions, material, finish and color exactly in
every cell.

CELL VARIABLE, positions: the same woman in the same pale studio in every cell,
same braided hair, same outfit, same soft light; only the exercise changes.
Cell 1: lying leg-raise, feet in the pedals, rope tensioned overhead.
Cell 2: seated V-sit row, mid-pull, back straight.
Cell 3: seated forward row, rope drawn to the waist.
Cell 4: kneeling overhead pull, arms extended behind the head.

CONSTANCY LOCK: the person, wardrobe, set, light and grade are identical across
cells; the trainer is identical in every cell; only the position varies.

CELL LAW: each cell a real mid-action moment, product legible at thumbnail
size, natural Z reading order from easiest to hardest movement.

STYLE: bright commercial fitness photography, one register, consistent grade.
NO text, no numbers, no logo, no watermark, no badges, no arrows.
```
Predicted failures: (1) face/outfit drift between cells (the same-person lock is
the make-or-break — if it recurs, switch to multi-pass edit chains); (2) the
model adding step numbers from instruction-manual priors; (3) rope physics
rendering slack where tension is claimed.

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Argument-sibling of 03-use-rail (capability breadth), different geometry: equal
cells vs hero-plus-band. Rule of thumb for the router: rail keeps a primary
scene and annotates breadth; grid IS the breadth. Boundary with 05-persona-grid
is the live confusion risk and the reason for avoid_adjacent — the compatibility
form deliberately occupies persona-grid geometry with hosts instead of people
(obs `sha256:9d88fa…` records the head-on collision).

## CHANGELOG
- 0.1 (2026-08-11): staging draft from five ledgered exemplars in three forms —
  applications (obs `sha256:96f3e9…` batch 10-F; `sha256:14d920…` 11-C, torch
  across four seasons), compatibility (`sha256:9d88fa…` 11-A, four host drills),
  positions (`sha256:7d39a9…`, `sha256:7b9d17…` 11-C, same-person exercise
  grids). Cell-variable slot parameterized from the three forms; overlay-free
  law hardened against the observed check-badge and red-separator dialect
  (`sha256:7b9d17…`); cell cap 4 taken from the rail's legibility lesson.

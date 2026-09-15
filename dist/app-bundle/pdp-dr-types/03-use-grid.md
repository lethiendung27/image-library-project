---
id: 03-use-grid
step: 3
job: use
device: grid
version: "1.0"
status: active
replaced_by: null
channels: [marketplace, landing-page]
requires_product_photo: true
generation_mode: single-pass
axes: {}
variants: []
exempt_from: [G3, G4]
pairs_with: []
never_with: []
avoid_adjacent: [05-persona-grid]
copied_from: 03-use-grid
copied_at_version: "1.0"
blocked_by: null
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

**Copied verbatim from `registry/types/03-use-grid.md` at version 1.0** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## TRIGGER
use_when: >
  The buyer's question is "how much will this one thing do for me" — multi-use
  tools, multi-exercise equipment, multi-host attachments. Gallery image 3-5 or
  a landing-page capability section. Choose the cell variable to match the
  doubt: applications when the product claims many jobs, compatibility when it
  must fit gear the buyer already owns, positions when one device claims a
  whole routine.

## SKELETON
```
TYPE: 03-use-grid v1.0
LAYOUT: [2x2 / 3 equal cells] photographic grid, thin white gutters,
no outer border, no numbers, no arrows, no badges, no text.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly in every cell where it appears.
Where the product IS A SET, a cell may show the member that cell's job uses —
but only a member visible in the reference photo, and its material and colour
are preserved exactly like any other.

[CAMERA — name a DIFFERENT one per cell. Required since 0.4.]
Distance, angle and context change from cell to cell: near/far, above/level/low,
and a real place per cell rather than one studio ground for all of them.
The cell variable says WHAT the product does; without this the renderer holds
HOW IT IS SEEN constant and the grid reads as one template repeated. Measured:
a four-cell grid met every other rule — identity 4 of 4, output 4 of 4 — and
still read as a template, because the product entered from the same side at the
same angle onto the same pale ground in all four. A three-cell grid in the same
round, staged in three real places, pulled its own angles apart unasked.

[CELL VARIABLE — choose ONE and name it in the prompt]
applications: each cell shows the product mid-action on a DIFFERENT JOB
  ([job 1], [job 2], [job 3], [job 4]), its working output visible in every
  cell (G8 inside cells: flame, cut, result).
compatibility: each cell shows a DIFFERENT HOST the product serves, staged in
  that host's own context, with the product visibly FITTED in every cell.
  The alternative offered until 0.3 — the product once as a central connecting
  element, the hosts implying it — is WITHDRAWN on its first and only render:
  the centre cell held the product exactly as asked and the two host cells
  furnished themselves with their own native hardware, so nothing connected the
  three. Given a host and no product, a renderer supplies that host's usual
  fitting.
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

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Argument-sibling of 03-use-rail (STAGING, not routable) — capability breadth,
different geometry: equal
cells vs hero-plus-band. Rule of thumb for the router: rail keeps a primary
scene and annotates breadth; grid IS the breadth. Boundary with 05-persona-grid
is the live confusion risk and the reason for avoid_adjacent — the compatibility
form deliberately occupies persona-grid geometry with hosts instead of people
(obs `sha256:9d88fa…` records the head-on collision).

## CHANGELOG
- 1.0 (2026-09-15): copied verbatim from `registry/types/03-use-grid.md` at 1.0, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.

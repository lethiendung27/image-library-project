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

## WORKED EXAMPLES
Kept in full text per SPEC §3.3, because the ledger stores verdicts and not prompts.

### example: drill-bit-set-applications-2x2 — skeleton@0.3, run: pass
Product: drill and driver bit set · ratio 1:1 · cell variable: applications · 2x2
```
TYPE: 03-use-grid v0.3
LAYOUT: 2x2 photographic grid, thin white gutters, no outer border, no numbers, no arrows, no badges, no text.

PRODUCT REFERENCE: use the attached product photo as the exact reference. Preserve shape, proportions, material, finish and colour exactly in every cell where it appears. The product IS A SET, so each cell shows the member that cell's job uses — but only a member visible in the reference photo, with its material and colour preserved exactly.

CELL VARIABLE — applications. Each cell shows one bit from the set mid-job in a drill chuck, its working output visible:
  cell 1 — a twist bit part way into softwood, a curl of shaving rising from the hole;
  cell 2 — a masonry bit part way into a brick wall, pale dust running down the face;
  cell 3 — a spade bit part way through a plank, the rim of the hole cut clean;
  cell 4 — a driver bit seated in a screw head, the screw already half sunk into wood.

Every bit is recognisably from the same set — same shank finish, same colour banding — and the drill and chuck are the same in all four cells. No cell contains a person's face.

No text, no letters, no numbers, no logo, no badge, no arrow, no cell divider other than the plain white gutter.
```
It returned four different bits plainly from one set, the same drill and chuck in every cell,
and a distinct visible output in each — a shaving, brick dust, a clean hole rim, a half-sunk
screw. It is the render that earned the SET clause in `PRODUCT REFERENCE`: without that clause
the same image would have breached "preserve exactly in every cell".

**No example exists at the 1.0 skeleton, and that is a real gap rather than an oversight.** The
`CAMERA` block became required at 0.4 and has not been rendered yet, so the strongest true
example this type owns is the one above at 0.3. The validator's staleness warning on it is
correct and closes when a 1.0 render lands.


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
- 1.0 (2026-08-26): **promoted to active on the owner's direct command**, SPEC §6.3 all four:
  5 exemplars over 3 batches; router-confusion 0 of 14 routed slots stolen; six renders carrying
  the owner's verdict; ADR-007 autopilot. WORKED EXAMPLES replaces an untested 0.1 draft with the
  rendered drill-bit set. Two shortfalls recorded rather than hidden: §6.3(2) asks for 5 fixture
  briefs and this library owns 2, and no example exists at the 1.0 skeleton. · this commit
- 0.4 (2026-08-26): **the grid had one axis and needed two.** New required `CAMERA` block:
  distance, angle and context differ per cell. The variable says WHAT the product does; the file
  said nothing about how it is SEEN, so the renderer held that constant — a four-cell grid met
  every stated rule and still read as one template, while a three-cell grid in three real places
  varied its angles unasked. A silent axis is a constant axis. · this commit
- 0.3 (2026-08-26): **the central-element branch of `compatibility` is WITHDRAWN on a fail.**
  Its first and only render put the product alone in the centre cell and let the two host cells
  furnish themselves — a tripod's own clamp and a dashboard cradle — so the grid argued nothing.
  The product must be visibly FITTED in every cell. The other two variables passed the same
  round: the 0.2 SET clause held on a four-bit set, and `positions` held one person across four
  cells for the second set running. · this commit
- 0.2 (2026-08-26): **two law breaches cleared before any promotion.** `2:1` leaves `ratios` for
  `16:9` (ADR-016) and the skeleton's `RATIO:` line goes entirely (adapter Rule 4); the surviving
  `multi-pass` instruction is removed, clearing the last STAGING name on ADR-041's list.
  `PRODUCT REFERENCE` now answers the SET question the first three renders raised. · this commit
- 0.1 (2026-08-11): staging draft from five ledgered exemplars in three forms —
  applications (obs `sha256:96f3e9…` batch 10-F; `sha256:14d920…` 11-C, torch
  across four seasons), compatibility (`sha256:9d88fa…` 11-A, four host drills),
  positions (`sha256:7d39a9…`, `sha256:7b9d17…` 11-C, same-person exercise
  grids). Cell-variable slot parameterized from the three forms; overlay-free
  law hardened against the observed check-badge and red-separator dialect
  (`sha256:7b9d17…`); cell cap 4 taken from the rail's legibility lesson.

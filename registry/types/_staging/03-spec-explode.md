---
id: 03-spec-explode
step: 3
job: spec
device: explode
version: "0.1"
status: reserved
replaced_by: null
ratios: ["1:1", "16:9"]
channels: [marketplace, landing-page]
requires_product_photo: true
generation_mode: single-pass
axes: {}
variants: []
exempt_from: [G7]
pairs_with: []
never_with: [03-spec-split]
avoid_adjacent: [03-mechanism-xray]
---

# 03-spec-explode — STAGING DRAFT

Promotion status (2026-08-11): **3 exemplars ledgered, 3 distinct sources**
(full-frame: obs `sha256:1abb6e…` batch 11-B wearable audio puck;
`sha256:620fb5…` 11-E mini camera; inset execution: `sha256:bb60ab…` 11-E
ab-roller material layers). Pending: 2 more exemplars, router-confusion test
(03-mechanism-xray is the boundary), ≥1 rendered worked example, human review.
Not routable.

## PURPOSE
A census of what is inside: the product separated into its real components,
floating in assembly order. Build quality argued by inventory — every part the
buyer is paying for, made visible. It counts; it does not explain.

## TRIGGER
use_when: >
  Compact products whose value is component density — cameras, audio gear,
  battery devices, layered materials — where the buyer suspects "cheap shell,
  empty inside". Step-3 gallery image or landing-page build section. Choose
  explode when the question is WHAT is in there; choose 03-mechanism-xray when
  the question is WHY it works.
avoid_when: >
  Products with trivial interiors (a shell and one part reads as emptiness
  made large). Never beside 03-spec-split (two component-tech arguments read
  as protesting too much — never_with) and never adjacent to 03-mechanism-xray
  on one page (two dark technical renders read as one template; the page takes
  at most two step-3 answers anyway). Not for natural/organic positioning
  where tech renders break trust.

## SKELETON
```
TYPE: 03-spec-explode v0.1
RATIO: [1:1 / 16:9]
REGISTER: 3D technical render. NOT photography. Dark engineering background.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Every outer part
(shell halves, buttons, ports, lens rings) must match the reference exactly
in shape, proportion, material and color. Do not redesign or add features.

[CANVAS]
Dark [deep navy / graphite] engineering canvas, faint [cyan] traces at very
low contrast. Motifs stay dim — credibility, not information.

[FRAMING — choose ONE]
full-frame: the exploded stack IS the image, parts filling [60-80%] of frame.
inset: a packshot base with the exploded stack inside ONE [circular] inset,
  occupying [30-40%] of frame width — for gallery positions that must keep
  the product recognizable at thumbnail size.

[EXPLODE STACK]
The product separated along ONE axis into [3-6] REAL component groups, in
true assembly order, evenly spaced, each part solid and detailed:
[part 1], [part 2], [part 3], [part 4]. Nothing rotated out of line;
nothing duplicated; gaps even enough that the eye can reassemble it.

[HONESTY CENSUS — hard rule]
Render ONLY component types the product genuinely contains, at plausible
sizes. No invented modules, no doubled parts, no filler pieces. The census IS
the claim — padding it is lying at the argument's core.
For layered materials (soles, wheels, mats): the stack may fan the REAL
layers like pages; layer count must match the spec.

[FOCUS COMPONENT]
[The one part that carries the buying argument] rendered brightest /
most detailed, placed nearest the visual center. A faint [cyan] glow may
mark it (G3: blue = working component). Product-identity colors (a lens
ring, brand accents) stay as the reference shows them.

NO text, no numbers, no part labels, no callout lines — indices and specs
are composited in post if the page needs them.
STYLE: premium technical product visualization, sharp, high detail, 4K.
NO text, no logo, no watermark.
```

## SLOT CONSTRAINTS
- Assembly order is the credibility: parts float where they belong, on one
  axis. A scattered "parts cloud" reads as decoration and kills the census.
- The observed market habit of numbering layers (digits 1-6, obs
  `sha256:bb60ab…`) goes to post-composite, never generated (G6 production
  law — model-drawn digits are gibberish).
- Boundary with xray, to hold in every prompt: explode SEPARATES (what is
  inside, job=spec); xray keeps the shell intact and looks THROUGH it (why it
  works, job=mechanism). If the prompt wants function explained, it is in the
  wrong type.
- G7 exemption is structural: an exploded product only exists in technical
  register; never place the exploded parts into a photographic scene.

## NEGATIVE
```
[G6] + photographic background, environment, people, hands, part labels,
callout lines, numbered parts, invented components, duplicated parts,
parts scattered off-axis, opaque parts hiding the census, exploded view
combined with translucent intact shell, bright white background,
rainbow palette, cartoon style
```

## WORKED EXAMPLES
### example: mini-camera-fullframe — skeleton@0.1, run: untested
Product: mini security camera · ratio 16:9 · framing: full-frame
- CANVAS — deep navy engineering canvas, faint cyan traces at very low contrast, dim
- STACK — the camera separated vertically into five real component groups in true assembly order, evenly spaced, each solid and detailed: clear upper shell; lens module with its red identity ring; populated main board with visible chips; flat battery cell; black lower chassis with its USB-C port. Nothing rotated out of line, nothing duplicated; the stack fills about 70% of the frame
- HONESTY CENSUS — only these component types, at plausible sizes
- FOCUS COMPONENT — the populated main board, brightest and most detailed, near the visual centre, a faint cyan glow marking it; the lens ring's red stays exactly as the reference shows it
Predicted failures: (1) the model inventing extra boards/screws to fill the
stack (the census rule and avoid line must both fire); (2) parts drifting
off-axis into a decorative cloud; (3) the battery rendering as a second PCB.

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Step-3 technical family: xray (through the shell, WHY) · explode (apart, WHAT)
· spec-split (against the old part, BETTER). One page: at most two step-3
answers, never two of these three together beyond the pairing laws above.
The inset execution (obs `sha256:bb60ab…`) is drafted as a FRAMING option, not
a variant — same argument, same layers, different footprint.

## CHANGELOG
- 0.1 (2026-08-11): staging draft from three ledgered exemplars across three
  verticals — wearable audio puck full-frame (obs `sha256:1abb6e…`, 11-B),
  ab-roller six-layer fan as inset (`sha256:bb60ab…`, 11-E), mini camera
  full-frame (`sha256:620fb5…`, 11-E). Framing parameterized
  (full-frame/inset) from the observed executions; honesty census promoted to
  hard rule (the xray honesty constraint transplanted to inventory form);
  observed layer-numbering digits routed to post-composite per the G6
  production law.

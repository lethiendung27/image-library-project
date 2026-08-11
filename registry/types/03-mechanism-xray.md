---
id: 03-mechanism-xray
step: 3
job: mechanism
device: xray
version: "1.0"
status: active
replaced_by: null
ratios: ["1:1", "4:5", "16:9"]
channels: [marketplace, landing-page, advertorial]
requires_product_photo: true
generation_mode: single-pass
variants: []
exempt_from: [G7]
pairs_with: [06-relief-hero, 02-cause-anatomy]
never_with: [03-spec-split]
---

# 03-mechanism-xray

## PURPOSE
Justify the product's capability by showing what is INSIDE the object — battery, chip,
motor, atomizer, filter layers — through a translucent shell. The mechanism answer for
products that do not act on a body structure (`body_contact: false`), where
ghostbody cannot serve. It exhibits; it does not compare.

## TRIGGER
use_when: >
  Need to explain WHY the product works by showing its real internal
  components, for gadget-class products that do not act on a body structure.
  Step-3 gallery image (image 3-4) or landing-page mechanism section — the
  slot ghostbody cannot serve when body_contact is false.
avoid_when: >
  Main image or scroll-stopper. Not when the interior is trivial (a shell
  with nothing meaningful inside). Not for categories where buyers distrust
  tech-render aesthetics (natural/organic positioning). Never on the same
  page as 03-spec-split — two component-tech arguments read as protesting
  too much.

## SKELETON
```
TYPE: 03-mechanism-xray v0.1
RATIO: [1:1 / 4:5 / 16:9]
REGISTER: 3D technical see-through render. NOT photography.
Dark engineering background.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. The outer shell becomes
translucent, but its silhouette, proportions and every visible external part
must match the reference exactly. Do not redesign or add features.

[CANVAS]
Dark [deep navy] engineering canvas with faint [copper and cyan] circuit-board
traces at very low contrast, and [1-2] corner blueprint micro-diagrams of key
components. Motifs stay dim — they buy credibility, they carry no information.

[BASE: GHOST SHELL]
The product rendered with its shell translucent and glass-like, silhouette
matching the reference, positioned [orientation], filling [60-75%] of the
frame width.

[INTERNALS]
[2-4 real internal components] rendered solid and detailed inside the shell,
each at its true location: [component 1 at location], [component 2 at
location], [component 3 at location]. Fine [colored] wiring connecting them.

[VISIBLE MECHANISM — G8 in technical register]
IF the product emits anything visible: the emitting module shown ACTIVE, its
output ([mist / light / flow]) rendered as a [particle stream] leaving the
product toward [direction], the brightest element in the frame.
ELSE: the primary working component highlighted with a cool [cyan] glow.

[HONESTY CONSTRAINT]
Render ONLY component types the product genuinely contains. No invented
modules, no exaggerated part counts. NO text, numbers or spec labels inside
the image — specs live in page copy or are composited in post.

PALETTE LOCK: deep navy and steel grey throughout. Cyan/blue marks the working
mechanism (G3: blue = correct mechanism). Copper traces stay decorative and
dim, never used as a signal.
STYLE: premium technical product visualization, sharp, high detail, 4K.
NO text, no numbers, no logo, no watermark.
```

## SLOT CONSTRAINTS
- G1 binds the OUTER SILHOUETTE hard (reference photo); the internal layout is
  illustrative — component TYPES must be real (honesty constraint), exact positions
  are approximate by nature. Never present this image as an engineering drawing.
- Text ban is stricter here than anywhere: the seed exemplar carried a "300mAh Li-ion"
  label — an unverifiable in-image claim AND a model weakness. Externalize all specs.
- G3 tension to police: copper/orange may exist only as dim background decoration;
  the moment orange marks a component it collides with orange = wrong-pressure.
- One product, one shell — no exploded parts (that is the reserved `explode` device).

## NEGATIVE
```
[G6] + photographic background, environment, people, hands,
spec labels, capacity text, callout lines with text, opaque shell,
internals floating outside the product, invented components,
exploded parts view, rainbow palette, bright white background, cartoon style
```

## WORKED EXAMPLES
### example: electric-spray-comb — skeleton@1.0, run: untested
```
A 1:1 3D technical see-through render. NOT photography. Dark engineering background.

Use the attached product photo as the exact reference for the electric spray massage
comb. The outer shell becomes translucent, but its silhouette, proportions and every
visible external part — the oval head, the button, the handle, the massage bristles —
must match the reference exactly. Do not redesign or add features.

CANVAS: a deep navy engineering canvas with faint copper and cyan circuit-board traces
at very low contrast, and two corner blueprint micro-diagrams of an atomizer module.
Motifs stay dim.

GHOST SHELL: the comb rendered with its cream shell translucent and glass-like, lying
horizontally with the head to the right, filling about 70 percent of the frame width.

INTERNALS: rendered solid and detailed inside the shell, each at its true location: a
small cylindrical lithium battery inside the handle, a compact control board with fine
colored wiring behind the button, a small serum reservoir and an ultrasonic atomizer
module inside the head above the bristle bed.

VISIBLE MECHANISM: the atomizer shown ACTIVE, a fine mist of particles streaming out
of the head to the right, the brightest element in the frame.

HONESTY CONSTRAINT: render only these component types. No text, numbers or spec labels
anywhere in the image.

PALETTE LOCK: deep navy and steel grey throughout; cyan/blue marks the working
mechanism; copper traces stay decorative and dim.
STYLE: premium technical product visualization, sharp, high detail, 4K.
NO text, no numbers, no logo, no watermark.
```
Predicted failures: (1) the model adding a spec label anyway (the exemplar it learns
from carries one) — the explicit text ban plus avoid-line must both fire; (2) shell
silhouette drifting from the reference once transparency is requested — if it recurs,
switch to multi-pass (generate opaque product first, edit to translucent).

### example: metal-shower-filter — skeleton@1.0, run: pass
```
A 1:1 3D technical see-through render. NOT photography. Dark engineering background.

Use the attached product photo as the exact reference for the metal shower filter. The
outer shell becomes translucent, but its silhouette, proportions and every visible
external part — the threaded inlet, the body, the outlet — must match the reference
exactly. Do not redesign or add features.

CANVAS: a deep navy engineering canvas with faint copper and cyan circuit-board traces
at very low contrast, and two corner blueprint micro-diagrams of a filtration stage.
Motifs stay dim.

GHOST SHELL: the filter rendered upright with its metal shell translucent and
glass-like, inlet at the top, outlet at the bottom, silhouette matching the reference,
filling about 65 percent of the frame height.

INTERNALS: rendered solid and detailed inside the shell, each at its true location: a
fine stainless mesh disc just below the inlet, a packed bed of white and pale grey
filtration granules filling the body, and a narrow outlet channel at the bottom.
Sparse rust-toned mineral specks held in the upper granule layer, caught by the media.

VISIBLE MECHANISM: the water path shown ACTIVE — a smooth cyan flow ribbon entering
the inlet, threading down through the granule bed, and leaving the outlet as a clean
fine spray of droplets, the brightest element in the frame.

HONESTY CONSTRAINT: render only these component types. No text, numbers or spec labels
anywhere in the image.

PALETTE LOCK: deep navy and steel grey throughout; cyan/blue marks the correct water
path; the trapped mineral specks are the only warm-toned elements (they are the
problem being caught); copper traces stay decorative and dim.
STYLE: premium technical product visualization, sharp, high detail, 4K.
NO text, no numbers, no logo, no watermark.
```
Predicted failures: (1) the granule bed rendering as mud instead of readable granules
(the lockedframe lesson — texture must stay granular); (2) the cyan ribbon and the
exit spray merging into one glow blob, losing the enter-filter-exit story; (3) trapped
specks scattering through the whole bed instead of staying in the upper layer, which
would read as a dirty filter rather than a working one.

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Distinction within step 3: `ghostbody` = body translucent, product solid ("why this
shape works on you"); `xray` = product translucent, internals solid ("what is inside
this thing"); `spec-split` = component combat old-vs-new. One page takes at most two
step-3 answers, and never xray + spec-split together.

Register decision (2026-08-11): the skeleton stays in the 3D-render register ("NOT
photography") — 3 of 4 exemplars are full see-through renders. The fourth exemplar
(`sha256:6735f5…`) executes the same argument as a technical line-art cutaway DRAWN
OVER a photographic scene; that is ONE observation of a possible `--overlay` variant
and stays below the ≥3 drafting threshold (SPEC §6.2). Log further sightings against
it; do not widen the skeleton meanwhile. Boundary vs the `explode` candidate
(03-spec-explode): xray sees THROUGH an intact shell to say WHY it works; explode
disassembles to census WHAT is inside — mechanism vs spec, why vs what.

## CHANGELOG
- 1.0 (2026-08-11): PROMOTED staging → active, all four §6.3 criteria met.
  (1) Five distinct exemplars across five verticals — obs `sha256:a2ad52…`
  (spray comb, batch 10-B), `sha256:937e6d…` (external drive, 10-E),
  `sha256:5c5e76…` (electric cutter, 10-F), `sha256:6735f5…` (mini chopper,
  photo-overlay register, 11-A), `sha256:0c2305…` (ab-roller rebound spring,
  brand-orange palette, 11-E). (2) Router-confusion test PASS (scratch-index
  method, curate.md §4): all 6 fixture-001 assertions hold, 0 unintended flips,
  2 intended improvements (fixture-001 known_gap resolves; cooler-advertorial
  mechanism slot routes here) — fixture updated in this diff. (3) Rendered
  worked example: metal-shower-filter, run pass (eval/render-tests.jsonl,
  2026-08-10). (4) Human gate: this promotion diff. Same-diff changes:
  slot-rules mechanism cells gain this type, vocabulary de-reserves `xray`,
  worked-example headers relabeled to skeleton@1.0. Palette-lock note: the 5th
  exemplar runs brand-orange against the navy/cyan lock (1 obs — the lock
  holds; expect brand-colored market executions and log them).
- 0.2 (2026-08-11): promotion-readiness pass. Exemplars 2-4 recorded — obs
  `sha256:937e6d…` (transparent external drive, batch 10-E), `sha256:5c5e76…`
  (translucent electric cutter, 10-F), `sha256:6735f5…` (chopper washability
  cutaway-over-photo, 11-A). Register decision: skeleton stays render-only;
  photo-overlay logged as a possible --overlay variant at 1/3 observations.
  Router-confusion test run and PASSED (see promotion status). Channels gain
  `advertorial` — the live demand case (cooler advertorial mechanism slot,
  query session 2026-08-11) and fixture-001 known_gap both sit on advertorial /
  landing pages.
- 0.1 (2026-08-10): staging draft from the first exemplar — translucent spray-comb
  render, obs `sha256:a2ad520c…` (batch 2026-08-10-B). Device `xray` was already
  reserved in vocabulary; this is its first exemplar. Demand signal predicted by
  eval/golden/fixture-001 known_gap (body_contact=false products had no mechanism
  type).

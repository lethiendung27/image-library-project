---
id: 03-spec-explode
step: 3
job: spec
device: explode
version: "1.2"
status: active
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

# 03-spec-explode

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
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 03-spec-explode v1.2
REGISTER: 3D technical render. NOT photography.

[PRODUCT REFERENCE] attached photo is the exact reference for every outer part.
[CANVAS] value chosen AGAINST the product's own value.        -> PARTS/canvas
[FRAMING] full-frame or inset.                                -> PARTS/framing
[STACK] name the real parts in assembly order.                -> PARTS/stack
[CENSUS] only what the product genuinely contains.            -> PARTS/census
[FOCUS] the one part that carries the buying argument.        -> PARTS/focus
[MARKS] focus glow, or none.                                  -> MARKS

STYLE: premium technical product visualization, sharp, high detail.
No text, no numerals, no part labels, no callout lines — indices and specs are
composited in post if the page needs them (G6 production law).
```

## PARTS

**`canvas`** — an engineering ground carrying faint traces at very low contrast. Motifs stay
dim: credibility, not information.

**Its VALUE is derived from the product, not fixed.** The ground must sit far enough in value
from the product's dominant value that the silhouette separates. This was a fixed deep navy
until three renders in one batch ordered themselves by exactly that distance: a white shoe on
graphite read instantly; a charcoal toothbrush shell sank into deep navy while its bright
metal parts above it popped, so one render separated well and badly at once; a navy jug on
deep navy nearly disappeared. Choose:

- a **dark** ground — `deep navy`, `graphite`, `near-black` — for a product that is pale,
  metallic or brightly coloured;
- a **light** ground — `studio grey`, `warm off-white`, `pale slate` — for a product that is
  dark, black or navy.

Two of the five exemplars already sit on a non-dark ground, which is why the light values are
named rather than invented. NEGATIVE still bans a BLOWN-OUT white; a mid or pale grey is not
that. Where a product carries both extremes, as the toothbrush does, pick against the LARGEST
part — the shell — because that is the silhouette a scroller sees.

**`framing`** — one of two.

- `full-frame` — the exploded stack IS the image, parts filling 60-80% of frame. 1 render.
- `inset` — a packshot base with the stack inside ONE circular inset at 30-40% of frame
  width, for gallery positions that must stay recognisable at thumbnail size. 0 renders.

**`stack`** — the product separated along ONE axis into its real component groups, in true
assembly order, evenly spaced, each part solid and detailed.

**The axis follows the product's proportion, not gravity.** A long thin product exploded
vertically in a square frame leaves the stack filling the height and a fifth of the width,
with dead ground on both sides — one render did exactly that. The axis may run vertical,
horizontal or diagonal; choose the one that lets the stack use the frame's LONGEST dimension.
Assembly order is unaffected: what matters is that every part sits on one line. Nothing rotated out of line,
nothing duplicated, gaps even enough that the eye can reassemble it.

**Name the PARTS, never a number of them.** A count does not bind in this library and never
has; a list of named components binds because each name is a thing the model can find in the
reference. The one passing render named five: clear upper shell, lens module with its red
identity ring, populated main board, flat battery cell, lower chassis with its port.

Assembly order IS the credibility. A scattered parts cloud reads as decoration and kills the
census.

**`census`** — render ONLY component types the product genuinely contains, at plausible
sizes. No invented modules, no doubled parts, no filler pieces. **The census IS the claim, so
padding it is lying at the argument's core.** For layered materials — soles, wheels, mats,
filter media — the stack may fan the REAL layers like pages, and the layer count must match
the spec.

**`focus`** — the one part that carries the buying argument, rendered brightest and most
detailed, nearest the visual centre. Product-identity colours — a lens ring, a brand accent —
stay exactly as the reference shows them.

## MARKS

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `focus-glow` | a faint glow around the focus component only | cyan — G3, working component | at most 1 | 1 render |

**`argument-faults.md` A5 does not bind here, and the reason is worth stating.** A5 says a
signal colour on the product reads as the product being coloured, because the mark belongs on
the body instead. This frame contains nothing but the product, so there is no body to move
the mark to: the focus glow is either on a component or the type has no mark at all. It is
the one exception the catalogue's own logic allows, and it rests on a single passing render.

**The register is a 3D render, which is why a glow works here at all.** In a photographic
register a mark must have a form the scene could not produce (A11); in a technical render
everything is already synthetic, so a glow reads as emphasis rather than as a light source.
The same reasoning is why a fill works in `02-cause-anatomy` and fails in `01-pain-scene` —
mark forms do not travel between registers without their own evidence.

## SLOT CONSTRAINTS
- **Trivial interiors are an admission test.** A shell and one part reads as emptiness made
  large. If the census would run to two entries, this is the wrong type.
- **Boundary with `03-mechanism-xray`, to hold in every prompt:** explode SEPARATES — what is
  inside, job=spec. Xray keeps the shell intact and looks THROUGH it — why it works,
  job=mechanism. If a prompt starts explaining function, it is in the wrong type.
- **Never combine an exploded view with a translucent intact shell.** That is the xray
  argument wearing this type's clothes, and it is what keeps the two apart at routing.
- Layer numbering is a market habit (obs `sha256:bb60ab…`) and goes to post-composite, never
  generated: model-drawn digits are gibberish (G6 production law).
- G7 exemption is structural — an exploded product exists only in technical register. Never
  place exploded parts into a photographic scene.
- **The prompt budget.** A clause earns its place only if a render has failed without it.
  Since ADR-014 no `Strictly avoid:` line is rendered at all.

## NEGATIVE
```
[G6] + photographic background, environment, people, hands, part labels,
callout lines, numbered parts, invented components, duplicated parts,
parts scattered off-axis, opaque parts hiding the census, exploded view
combined with translucent intact shell, bright white background,
rainbow palette, cartoon style
```
Canonical and model-agnostic. Since ADR-014 it is **not rendered into the prompt at all**; it
stays here and in the query output's `avoid` field for a future model with a real negative
channel.

## WORKED EXAMPLES
### example: mini-camera-fullframe — skeleton@1.1, run: pass
```
A 16:9 3D technical render. NOT photography. Dark engineering background.

Use the attached product photo as the exact reference for the mini security
camera. Every outer part — the clear upper shell, the red-ringed lens, the
black chassis, the USB-C port — must match the reference exactly. Do not
redesign or add features.

CANVAS: a deep navy engineering canvas with faint cyan traces at very low
contrast, dim.

FRAMING, full-frame: the exploded stack fills about 70 percent of the frame.

EXPLODE STACK: the camera separated vertically into five real component
groups in true assembly order, evenly spaced, each solid and detailed: the
clear upper shell; the lens module with its red identity ring; the populated
main board with visible chips; the flat battery cell; the black lower chassis
with its USB-C port. Nothing rotated out of line, nothing duplicated.

HONESTY CENSUS: render only these component types at plausible sizes.

FOCUS COMPONENT: the populated main board, brightest and most detailed, near
the visual center, a faint cyan glow marking it. The lens ring's red stays
exactly as the reference shows it.

NO text, no numbers, no part labels, no callout lines.
STYLE: premium technical product visualization, sharp, high detail, 4K.
NO text, no logo, no watermark.
```
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

The canvas question and its 2-of-5 evidence live in `PARTS/canvas`.

## CHANGELOG
- 1.2 (2026-08-13): **the ground is derived from the product's value; the explode axis follows
  the product's proportion.** Owner report that the backgrounds lack variety, and three renders
  in one batch ordered themselves by value distance: a white shoe on graphite separated, a navy
  jug on deep navy nearly vanished, a charcoal shell sank while its own bright metals popped.
  `PARTS/canvas` stops being a fixed deep navy and names dark and light values to choose
  between, which is the widening the file has carried as a proposal since 0.2 — the trigger is
  the owner's report plus this batch, not the exemplar count, which is still 2 of 5. Also:
  the `inset` framing and the layered-materials fan both earned their founding renders and both
  pass. · this commit
- 1.1 (2026-08-13): **restructured into a call-map plus two libraries** (ADR-012), owner
  instruction. `PARTS` owns `canvas`, `framing`, `stack`, `census`, `focus`; `MARKS` owns the
  single `focus-glow`. `RATIO:` dropped per adapter Rule 4. Recorded rather than assumed:
  A5 cannot bind in a frame containing nothing but the product, and a glow works here because
  the register is already synthetic. The canvas proposal moves to `PARTS/canvas`, still 2 of
  5. ADR-014 adopted. · this commit
- 1.0 (2026-08-12): **promoted to active** on the owner's direct command, all four SPEC §6.3
  criteria met. Criterion 1 rests on **3 market exemplars plus 2 admitted by owner ruling**
  whose own records carry a no-product-identity caveat — a curator reading a bare "5" later
  should know that. Router-confusion test passed on both golden fixtures with 0 unintended
  flips. · 916bacf
- 0.2 (2026-08-12): promotion accounting only, no skeleton or trigger change. Criterion 1
  recorded MET at 5 exemplars by owner ruling over the caveat two of them carry. · e0f280f
- 0.1 (2026-08-11): staging draft from three ledgered exemplars across three
  verticals — wearable audio puck full-frame (obs `sha256:1abb6e…`, 11-B),
  ab-roller six-layer fan as inset (`sha256:bb60ab…`, 11-E), mini camera
  full-frame (`sha256:620fb5…`, 11-E). Framing parameterized
  (full-frame/inset) from the observed executions; honesty census promoted to
  hard rule (the xray honesty constraint transplanted to inventory form);
  observed layer-numbering digits routed to post-composite per the G6
  production law.

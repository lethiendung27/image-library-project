---
id: 03-spec-explode
step: 3
job: spec
device: explode
version: "1.7"
status: active
replaced_by: null
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

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 03-spec-explode v1.7
REGISTER: 3D technical render. NOT photography.

[PRODUCT REFERENCE] attached photo is the exact reference for every outer part.
[CANVAS] value against the product, motif from what it DOES. -> PARTS/canvas
[FRAMING] full-frame or inset.                                -> PARTS/framing
[STACK] name the real parts in assembly order.                -> PARTS/stack
[CENSUS] only what the product genuinely contains.            -> PARTS/census
[FOCUS] the one part that carries the buying argument.        -> PARTS/focus
[MARKS] focus glow OPTIONAL; hue derived.                     -> MARKS

STYLE: premium technical product visualization, sharp, high detail.
No text, no numerals, no part labels, no callout lines — indices and specs are
composited in post if the page needs them (G6 production law).
```

## PARTS

**`canvas`** — an engineering ground carrying a faint motif at very low contrast. It stays
dim: credibility, not information. Two things are chosen: a value and a geometry.

**The MOTIF is named by its GEOMETRY; the domain only chooses among geometries.** Naming a
meaning does not bind — three different motif meanings returned one identical concentric-ring
ground, 3 of 3, because the model holds one default and maps every meaning onto it.

| geometry | drawn as | fits |
|---|---|---|
| concentric rings | closed rings nested around one centre | sound, water |
| nested irregular contours | uneven blobby bands like a thermal map, **never circular** | heat |
| parallel wavy bands | long undulating lines crossing the frame, **never closed** | air, flow |
| orthogonal lattice | a sparse square grid | textile, material |
| open arcs | curved strokes that do not close | sport, motion |
| hexagonal tessellation | a honeycomb field | filtration, membranes |

**And name the default OUT.** Rings are where this model goes unasked, so every non-ring
geometry must say what it is not — the `not a skeleton` mechanism.

The motif is abstract line-work, never an illustration of the thing and never a photographic
scene — the G7 exemption is structural. **Bound its contrast against the frame, not with an
adjective: it must stay fainter than the darkest shadow on any part.** Soft rings obeyed "very
low contrast"; a square grid ignored it and rendered as engineering graph paper.

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

**The HUE may follow the product's world at low chroma, but it must stay far from CYAN.**
Cyan is this type's only signal colour and marks the focus component; a teal or aqua ground
for a water product would swallow the one mark the type has. Let the MOTIF do the evoking and
keep the hue out of the signal's way.

Two of the five exemplars already sit on a non-dark ground, which is why the light values are
named rather than invented. NEGATIVE still bans a BLOWN-OUT white; a mid or pale grey is not
that. Where a product carries both extremes, pick against the LARGEST part — that is the silhouette
a scroller sees. A MID-value product takes the DARK ground: light has no headroom left against
it, and a mid-grey cushion on warm off-white barely separated.

**`framing`** — one of two.

- `full-frame` — the exploded stack IS the image, parts filling 60-80% of frame. 1 render.
- `inset` — a packshot base with the stack inside ONE circular inset at 30-40% of frame
  width, for gallery positions that must stay recognisable at thumbnail size. 1 render.

**A tall narrow product explodes on a DIAGONAL.** The frame will not save it: ratio cannot be
requested, 3 of 3 on tall products here and 6 of 6 in adapter Rule 4. The axis can — run it
corner to corner and the stack uses both dimensions while staying one line in assembly order.
A tall slot is the page's layout decision, not this composition's: the shape arrives from the
slot in `content.json` and the diagonal is what makes it survivable (ADR-082 removed `ratios`
from every type file, so there is no longer a second place where a shape is declared).

**`stack`** — the product separated along ONE axis into its real component groups, in true
assembly order, evenly spaced **including the LAST pair, where a run breaks**, each part
solid and detailed.

**Explode the WHOLE product by default.** A sub-assembly explode — one part group separated
while the rest stays intact — is legal only when the intact part is visually DISTINCT from the
exploded one. A headband beside an exploded earcup worked; one eyecup of a swim goggle
returned three whole goggles and no explosion at all, because an eyecup is most of a goggle
and the boundary did not exist. 1 of 2. When in doubt, explode the whole product.

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

**`census`** — render ONLY component types the product genuinely contains, **and only what is
INSIDE it**. External mounting hardware, stands, cradles and accessories are not components: a
shock-mount cradle rendered into a microphone stack counts a part the buyer does not get
inside the product, which is the census claiming more than the box holds. Plausible
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
| `focus-glow` | a faint glow around the focus component only | derived; never red, orange or green | **optional**, at most 1 | 12 renders, all cyan; 1 render omitted it with nothing lost |

**The glow is EMPHASIS, not a G3 signal.** An explode judges nothing — no wrong state, no
corrected state, no comparison — so G3's closed list never bound it, and cyan came from a gloss
about working mechanisms that is not the claim here. **Prefer NO glow**: `focus` already fixes
brightness, detail and centre, and one render omitted it with nothing lost. Where used, derive
the hue from the product's own accent or from what separates it from the ground. **Never red,
orange or green** — those carry library-wide meaning and a page shows several types at once.

**The focus glow BLOOMS, 2 of 2.** It reached the size of the whole basket on the portafilter
frame and became the brightest object in it. A radial falloff cannot be stopped at an outline
in any register — the same limit `01-pain-scene` measured at 3 of 3. Bind it by naming ONE
bounded component as its target and keep the fill low around it; do not ask it to stop.

**`argument-faults.md` A5 does not bind here, and the reason is worth stating.** A5 says a
signal colour on the product reads as the product being coloured, because the mark belongs on
the body instead. This frame contains nothing but the product, so there is no body to move
the mark to: the focus glow is either on a component or the type has no mark at all. It is
the one exception the catalogue's own logic allows, and it rests on a single passing render.

**A glow works here because the register is already synthetic** — A11 in reverse. Mark forms do
not travel between registers without their own evidence.

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
Both rendered and owner-passed, kept in FULL text per SPEC §3.3. They replace the founding
mini-camera example, which passed at 1.1 and predates every rule this type has since earned —
ground geometry, rim light, contact shadow, the diagonal axis and the optional focus glow. Git
holds it at 916bacf.

### example: purifier-cartridge-hex — skeleton@1.4, run: pass
```
TYPE: 03-spec-explode v1.4
REGISTER: 3D technical render. NOT photography.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Every outer part — the cylinder
form, the end caps, the mesh face, the colourway — must match the reference exactly in
shape, proportion, material and colour. Do not redesign or add features. Render no
wordmark or logo on any part, whatever the reference shows.

[CANVAS]
A deep slate engineering canvas carrying a faint HEXAGONAL TESSELLATION — a honeycomb
field of six-sided cells tiling evenly across the whole frame. NOT concentric circles,
NOT rings, NOT contour lines. Abstract line-work at very low contrast, dim. No cyan or
teal in the ground. A soft contact shadow pools beneath the lowest part.

[FRAMING]
Full-frame: the exploded stack IS the image, filling about 70 percent of the frame.

[STACK]
The whole cartridge separated VERTICALLY along its own axis, in true assembly order,
evenly spaced, each part fully clear of its neighbours and solid and detailed: the upper
end cap with its grille; the coarse pre-filter mesh sleeve; the pleated HEPA media pack
with its concertina folds; the activated carbon granule sleeve; the inner support cage;
the lower end cap with its gasket. Nothing rotated out of line, nothing duplicated,
nothing left fused to the part below it.

[LIGHT]
A thin cool rim light traces the top edge of every part, separating each from the part
above it and from the ground. Fill stays low.

[CENSUS]
Render only those component types, at plausible sizes for a purifier cartridge, and only
things that live INSIDE the product — no housing, no fan, no appliance beside it.

[FOCUS]
The pleated HEPA media pack, brightest and most detailed, nearest the visual centre,
with a faint cyan glow around that one part.

STYLE: premium technical product visualization, sharp, high detail.
No text, no numerals, no part labels, no callout lines.
```
The best census this type has rendered: six named parts separated on one axis, evenly spaced,
nothing fused, nothing invented, a honeycomb ground that never competes.

### example: torch-diagonal — skeleton@1.5, run: pass
```
TYPE: 03-spec-explode v1.5
REGISTER: 3D technical render. NOT photography.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Every outer part — the body tube,
the knurling, the head bezel, the tail cap — must match the reference exactly in shape,
proportion, material and colour. Do not redesign or add features. Render no wordmark or
logo on any part, whatever the reference shows.

[CANVAS]
A pale slate engineering canvas, clearly lighter than the dark torch, carrying a faint
motif of OPEN ARCS — long curved strokes that fan outward and never close on themselves,
in a slightly darker grey than the ground. NOT concentric circles, NOT rings, NOT closed
shapes of any kind. The motif stays fainter than the darkest shadow on any part. A soft
contact shadow pools beneath the stack.

[FRAMING]
Full-frame: the exploded stack IS the image, laid along a DIAGONAL running from the lower
left corner to the upper right, using both dimensions of the frame and filling about 80
percent of it.

[STACK]
The whole torch separated along that one DIAGONAL axis, in true assembly order, evenly
spaced with equal gaps all the way to the last pair, each part fully clear of its
neighbours and solid and detailed: the head bezel with its lens; the smooth reflector
cone; the LED emitter on its star board; the driver circuit board; the cylindrical
battery cell; the knurled body tube; the tail cap with its switch and spring. Every part
sits on that one straight diagonal line, none scattered off it, none duplicated, none
left fused to its neighbour.

[LIGHT]
A thin cool rim light traces the upper edge of every part, separating each from its
neighbour and from the ground. Fill stays low.

[CENSUS]
Render only those component types, at plausible sizes for a rechargeable torch, and only
things that live INSIDE the product — no charger, no cradle, no accessory beside it.

[FOCUS]
The LED emitter on its star board, brightest and most detailed, nearest the visual
centre, with a faint cyan glow around that one part.

STYLE: premium technical product visualization, sharp, high detail.
No text, no numerals, no part labels, no callout lines.
```
The diagonal that solved dead ground on tall narrow products. Note that the model drew no glow
at all here and the LED still reads as the focus — the evidence that made the glow optional at
1.6, preserved in the prompt that produced it.

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
- 1.7 (2026-08-13): **type PASSED by the owner; file finalised.** WORKED EXAMPLES rebuilt on
  two current-law renders — the hex-ground cartridge census and the diagonal torch — replacing
  the founding mini-camera example, which passed at 1.1 and teaches none of the rules earned
  since. The derived focus hue confirmed on its first render: amber on a flask, the first
  non-cyan mark in 13 renders, reading as emphasis and not as a signal.
- 1.6 (2026-08-13): **the focus glow is optional and its hue is derived.** Owner: the mark is
  stuck on one colour, true at 12 of 12. It is EMPHASIS, not a G3 signal — an explode judges
  nothing — so G3 never bound it and the type paid a monotony tax for a rule that did not
  apply. Prefer no glow; where used, derive the hue, never red, orange or green.
- 1.5 (2026-08-13): **four logic fixes, no new sections.** Motif contrast is bounded against
  the frame — fainter than the darkest shadow on any part — because a grid ignored the adjective
  and rendered as graph paper. A tall narrow product explodes on a DIAGONAL, since ratio cannot
  be requested and the frame will not save it. A MID-value product takes the dark ground. Even
  spacing must hold to the LAST pair, where one run broke. Case history cut to pay for it.
- 1.4 (2026-08-13): **the motif is named by GEOMETRY, not by meaning** — owner-approved after
  three motif names produced one identical concentric-ring ground, 3 of 3. `PARTS/canvas` lists
  geometries and every non-ring one must name the ring default OUT. Two census rules the batch
  earned: explode the WHOLE product unless the intact part is visually distinct (1 of 2), and
  count only what is INSIDE. `ratios` gains **4:5** for products with one vertical axis.
- 1.3 (2026-08-13): **the motif is derived from what the product DOES.** Owner: the background
  is still monotonous and does not evoke the product. 1.2 fixed the ground's VALUE, which was
  only half — the motif stayed one default, printing circuit schematics behind a straightener
  and a shoe, or nothing at all behind a headphone. `PARTS/canvas` derives it by domain, and
  the hue must stay far from CYAN, the type's only signal. Confirmed same batch: the value
  rule in its light direction, the axis rule, and rim light plus contact shadow. · this commit
- 1.2 (2026-08-13): **the ground is derived from the product's value; the explode axis follows
  the product's proportion.** Owner report that backgrounds lack variety, and three renders
  ordered themselves by value distance: a white shoe on graphite separated, a navy jug on deep
  navy nearly vanished. `PARTS/canvas` stops being a fixed deep navy and names both directions.
  The trigger is the owner's report plus this batch, not the exemplar count, still 2 of 5.
  `inset` and the layered fan both earned founding renders and both pass. · ebc54a2
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

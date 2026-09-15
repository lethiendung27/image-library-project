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
copied_from: 03-spec-explode
copied_at_version: "1.7"
blocked_by: null
---

# 03-spec-explode

## PURPOSE
A census of what is inside: the product separated into its real components,
floating in assembly order. Build quality argued by inventory — every part the
buyer is paying for, made visible. It counts; it does not explain.

**Copied verbatim from `registry/types/03-spec-explode.md` at version 1.7** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

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
- 1.7 (2026-09-15): copied verbatim from `registry/types/03-spec-explode.md` at 1.7, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.

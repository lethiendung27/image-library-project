---
id: 03-mechanism-xray
step: 3
job: mechanism
device: xray
version: "1.4"
status: active
replaced_by: null
ratios: ["1:1", "16:9"]
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

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 03-mechanism-xray v1.3
REGISTER: 3D technical see-through render. NOT photography.  -> PARTS/register

[PRODUCT REFERENCE] the attached photo is the exact reference.
[CANVAS] a ground chosen for the product.                    -> PARTS/canvas
[SHELL] the product, shell translucent, silhouette exact.    -> PARTS/shell
[INTERNALS] name 2-4 real components and where each sits.    -> PARTS/internals
[MARKS] name each one used, with its count:                  -> MARKS
  required: working
  nothing in the frame is marked that is not named here

The marks are the only added colour. `working` is the brightest thing in frame.
```

## PARTS

**`register`** — a premium technical see-through product visualization, sharp and high
detail. Not photography. The product is the only subject; there is no scene, no hands, no
environment. G7 is exempt here by the type's frontmatter: a technical render need not mount
the product to anything real.

**`canvas`** — a plain ground chosen to suit the product, and nothing else on it. **No motifs.**
The old rule asked for circuit traces and corner blueprint micro-diagrams while admitting in its
own words that they "buy credibility and carry no information"; `02-cause-anatomy` deleted
exactly that at its 1.4 on exactly that reasoning, and three renders here put the same traces
behind a power tool, a jewellery cleaner and a water bottle.

**Colour is free** — the ruling `02-cause-anatomy` took at its 1.13. The navy-and-steel lock came
from `ghostbody`, whose subject is a white mannequin where four signal colours are the entire
information channel. This type's subject is real hardware — copper windings, a green board, gold
contacts, a filter bed — and those material colours ARE the information. Locking them destroys
what the type exists to show.

One requirement survives, about contrast rather than hue: **`working` must be the brightest thing
in the frame and must read clearly against whatever ground is chosen.**

**`shell`** — the reference product with its outer shell rendered translucent and glass-like.
**G1 binds the silhouette hard**: proportions and every visible external part must match the
reference exactly, because a translucent shell is the one place a model will quietly redesign
a product. Named orientation, filling a named share of the frame.

**`internals`** — two to four real internal components rendered solid and detailed inside the
shell, each named with its true location, connected by fine wiring where wiring is real.

**The honesty constraint is this type's admission test.** Render only component types the
product genuinely contains: no invented modules, no exaggerated part counts. The internal
LAYOUT is illustrative and approximate by nature; the component TYPES are not. This image is
never presented as an engineering drawing.

**The text ban is stricter here than anywhere in the library.** The seed exemplar carried a
`300mAh Li-ion` label — an unverifiable in-image claim and a model weakness at once. No specs,
no capacities, no callout text inside the image; specs live in page copy or are composited in
post.

## MARKS

This type's own mark library, called by name from the skeleton. It exhibits rather than
compares, so it has no verdict badge and no wrong state: there is only the working mechanism.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `working` | the primary working component, or the module that emits, shown ACTIVE and made the brightest element in the frame | cyan / blue (G3: blue = correct mechanism) | exactly 1 | 1 render · pass |
| `output` | what the product emits, made of the substance itself, leaving the product toward a named direction | the substance's own colour | 1, only when the product emits something visible | 1 render · pass |
| `caught` | what the product traps or removes, held where the mechanism holds it | the trapped matter's own colour, warm-toned | as many as are held, in one layer | 1 render · pass |

**`working` carries direction by its own form and never takes an arrow.** One render added an
unrequested cyan arrow inside a filter where the flow ribbon already ran through it — an abstract
direction claim laid over a physical one, which is what `02-symptom-rail` spent three versions
removing.

**`output` only exists if the product genuinely emits.** Mist, light, flow, spray. Where
nothing leaves the product, `working` alone carries the argument as a cool glow on the
component that does the work. Never invent an emission so a render looks alive — that is what
G8 forbids, and this type is the easiest place in the library to break it.

**`caught` is used ONLY where the mechanism physically ENCLOSES what it holds** — a filter
sleeve, a bin, a bed, a cartridge. Two renders decided this in one batch: sediment held in a
bottle's pre-filter read correctly, and tarnish lifting off a ring in an open tank swirled
through the whole volume and made the frame read as dirty water. Where nothing encloses it the
caught matter drifts and turns the product into the problem, so the mark is dropped rather than
weakened. Inside its enclosure it stays in ONE layer.

**Borrowed from types that have been rendered**, so the same faults are not paid for twice:
a mark whose form the register could have produced stops reading as a mark (A11), which here
means the cyan `working` glow must be brighter and cleaner than any ambient reflection the
render puts on a component anyway; and the canonical NEGATIVE below is never pasted into a
prompt verbatim.

## SLOT CONSTRAINTS
- **The prompt budget** (ADR-013, ADR-015): a clause earns its place in a rendered prompt only
  if a render has failed without it, and it is removed only once a render has done without it
  and come back correct.
- One product, one shell — no exploded parts, which is the reserved `explode` device.
- G1 binds the outer silhouette; the internal layout is illustrative.
- The ground and the product's own materials carry any colour that suits them; only the marks
  are added colour.

## NEGATIVE
```
[G6] + photographic background, environment, people, hands,
spec labels, capacity text, callout lines with text, opaque shell,
internals floating outside the product, invented components,
exploded parts view, rainbow palette, bright white background, cartoon style
```
Canonical and model-agnostic; the adapter transforms it at render time and a prompt never
carries it verbatim (Rule 1, and no avoid line ships at all since ADR-014).

## WORKED EXAMPLES
Two renders that happened, kept in full because that text is the only record of what actually
drew (SPEC §3.3). Both `pass`, both written after 1.2 freed the palette — the earlier
shower-filter example was retired with the lock it was written under.

### example: cordless-hair-dryer — skeleton@1.2, run: pass
The case where the old lock hurt most: the heating coil glows ORANGE-HOT as `working`, a
colour the navy lock forbade outright, and copper windings appear in copper. `output` is warm
air made of the moving air itself.
```
TYPE: 03-mechanism-xray v1.2
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the cordless hair
dryer. The outer shell becomes translucent, but its silhouette, proportions and
every visible external part must match the reference exactly. Do not redesign or
add features.

CANVAS: a plain pale warm sand ground, and nothing else in the frame
behind the product.

SHELL: the dryer lying horizontally, nozzle to the right, its body translucent and
glass-like, filling about 75 percent of the frame width.

INTERNALS, solid and detailed inside the shell, each at its true location: a
cylindrical battery pack in the handle; a control board behind the switch, in its
own real board colour; a brushless motor with copper windings in the barrel, the
copper in its own colour; a coiled heating element in the nozzle throat.

MARKS, two, nothing else in the frame is marked:
- working: the heating element shown ACTIVE and glowing orange-hot in its own real
  colour, the brightest thing in the frame and clearly brighter than the ground.
  No arrow anywhere.
- output: warm air leaving the nozzle to the right, made of the moving air itself,
  drawn as a soft stream that widens and thins as it travels.

No text, numbers or spec labels anywhere in the image.
The marks are the only added colour; the product and its parts keep their own.
```

### example: robot-vacuum — skeleton@1.2, run: pass
Both 1.2 rules in one frame: `caught` held inside a sealed bin, which is what drifted through
an open tank when nothing enclosed it; and `working` drawn as a luminous PATH along the suction
duct rather than a glow on a part, direction carried by the duct's own shape with no arrow.
```
TYPE: 03-mechanism-xray v1.2
REGISTER: 3D technical see-through render. NOT photography.

PRODUCT REFERENCE: the attached photo is the exact reference for the robot vacuum.
The outer shell becomes translucent, but its silhouette, proportions and every
visible external part must match the reference exactly. Do not redesign or add
features.

CANVAS: a plain soft pale grey-green ground, and nothing else in the frame
behind the product.

SHELL: the vacuum seen from the front and slightly above, its top casing
translucent and glass-like, filling about 70 percent of the frame width.

INTERNALS, solid and detailed inside the shell, each at its true location: a
rotating brush bar across the underside at the front; a suction duct running back
from the brush; a sealed dust bin behind the duct; a filter panel at the back of
the bin; a battery pack and a control board beneath, each in its own real colour.

MARKS, three, nothing else in the frame is marked:
- working: a cool glow along the suction duct from the brush bar back to the bin,
  the brightest thing in the frame and clearly brighter than the ground. No arrow
  anywhere - the duct's own shape carries the direction.
- caught: grey dust and hair packed inside the SEALED DUST BIN and nowhere else
  in the machine, filling the lower part of the bin in one layer, held by the bin
  walls.
- output: clean air leaving the filter panel at the back, made of the air itself,
  drawn as a thin pale stream.

No text, numbers or spec labels anywhere in the image.
The marks are the only added colour; the product and its parts keep their own.
```

## KNOWN-FLAKY
- **Spec labels appear unasked, 1 observation.** The seed exemplar this type learns from
  carries a `300mAh Li-ion` label. Watch for it; the text ban is in `internals` for that
  reason.
- **Shell silhouette drifting once transparency is requested**, predicted and not yet
  observed. **There is no multi-pass fallback any more** (ADR-067): the old note here sent a
  reader to generate the opaque product and edit it translucent, against a Rule 3 that has
  been retired since ADR-039 and a pipeline that has not composited since ADR-021. If it
  recurs, it takes the ordinary route SPEC §6.2 prescribes — at ≥2/3 or ≥3 observations, a
  NEGATIVE clause or a tightened `internals` part; below that, it stays here.

## NOTES
Distinction within step 3: `ghostbody` = body translucent, product solid ("why this shape
works on you"); `xray` = product translucent, internals solid ("what is inside this thing");
`spec-split` = component combat, old versus new. One page takes at most two step-3 answers,
and never xray + spec-split together. Boundary against `03-spec-explode`: xray sees THROUGH an
intact shell to say WHY it works; explode disassembles to census WHAT is inside.

A possible `--overlay` variant sits at 1 observation (`sha256:6735f5…`, a technical line-art
cutaway drawn over a photographic scene). Below the ≥3 threshold; log further sightings, do
not widen the skeleton meanwhile.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.4 (2026-09-03): the KNOWN-FLAKY multi-pass fallback is removed (ADR-067, owner
  instruction). It pointed at adapter Rule 3, retired at ADR-039, for a capability removed at
  ADR-021 — a prediction with an illegal remedy attached. The prediction stands; the remedy is
  SPEC §6.2's ordinary route. `ratios` corrected to ADR-016's legal set: `4:5` dropped,
  unaskable since 2026-08-13. A portrait ratio returns as `3:4` when a render earns it.
- 1.3 (2026-08-13): type passed by the owner; file finalised with two rendered worked examples
  in full text per SPEC §3.3. The 1.2 decisions are confirmed at 2 of 2 — a hair dryer whose
  orange coil the old lock forbade, and a robot vacuum carrying `caught` inside its bin and
  `working` as a path along a duct. The shower-filter example is retired with the palette lock
  it was written under. Closing state: three marks, all with render evidence. `e8ca963`
- 1.2 (2026-08-13): **the palette lock and the canvas motifs are gone.** Owner-approved on three
  recommendations. Evidence: 3 records at 1.1 — 2 `partial`, 1 `fail`. Colour is free and chosen
  for the product, the ruling `02-cause-anatomy` took at its 1.13; the navy-and-steel lock had
  been inherited from `ghostbody`, whose subject is a white mannequin, while this type's subject
  is real hardware whose material colours ARE the information. Motifs deleted — the rule admitted
  in its own words that they carry none. `caught` now requires the mechanism to ENCLOSE what it
  holds, after one batch showed it read inside a pre-filter and drifted through an open tank.
  `working` never takes an arrow. `5612f49`
- 1.1 (2026-08-13): restructured into a call-map plus PARTS and MARKS (ADR-012); skeleton
  1925 → 609. Three marks named for the first time — `working`, `output` and `caught` — all
  founded on the one rendered example, where they existed as unnamed sentences inside the
  skeleton. `RATIO:` dropped per adapter Rule 4. `3e32167`
- 1.0 (2026-08-11): PROMOTED staging → active on all four §6.3 criteria: five distinct
  exemplars across five verticals, router-confusion test passed with 0 unintended flips, one
  rendered worked example at `run: pass`, and the human gate. Palette-lock note: the fifth
  exemplar runs brand-orange against the navy/cyan lock at 1 observation — the lock holds.
- 0.2 (2026-08-11): promotion-readiness pass; exemplars 2–4 recorded, register decision to
  stay render-only, channels gain `advertorial`.
- 0.1 (2026-08-10): staging draft from the translucent spray-comb render, obs
  `sha256:a2ad520c…`. Demand predicted by `eval/golden/fixture-001` known_gap — body_contact
  false products had no mechanism type.

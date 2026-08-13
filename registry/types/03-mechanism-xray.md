---
id: 03-mechanism-xray
step: 3
job: mechanism
device: xray
version: "1.1"
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
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 03-mechanism-xray v1.1
REGISTER: 3D technical see-through render. NOT photography.  -> PARTS/register

[PRODUCT REFERENCE] the attached photo is the exact reference.
[CANVAS] dark engineering ground.                            -> PARTS/canvas
[SHELL] the product, shell translucent, silhouette exact.    -> PARTS/shell
[INTERNALS] name 2-4 real components and where each sits.    -> PARTS/internals
[MARKS] name each one used, with its count:                  -> MARKS
  required: working
  nothing in the frame is marked that is not named here

PALETTE LOCK: deep navy and steel grey except the marks.
```

## PARTS

**`register`** — a premium technical see-through product visualization, sharp and high
detail. Not photography. The product is the only subject; there is no scene, no hands, no
environment. G7 is exempt here by the type's frontmatter: a technical render need not mount
the product to anything real.

**`canvas`** — a dark engineering ground, deep navy, with faint circuit-board traces at very
low contrast and one or two corner blueprint micro-diagrams of a key component. **Motifs stay
dim: they buy credibility and carry no information.** Copper traces are decoration only —
the moment copper or orange marks a component it collides with G3, where orange means wrong
pressure or wrong heat.

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

**`output` only exists if the product genuinely emits.** Mist, light, flow, spray. Where
nothing leaves the product, `working` alone carries the argument as a cool glow on the
component that does the work. Never invent an emission so a render looks alive — that is what
G8 forbids, and this type is the easiest place in the library to break it.

**`caught` is the only warm colour permitted anywhere in the frame**, and it is permitted
because the trapped matter IS the problem being solved. It stays in ONE layer where the
mechanism holds it; scattered through the whole medium it reads as a dirty product rather
than a working one.

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
- Copper and orange stay decorative and dim, never a signal.

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
### example: metal-shower-filter — skeleton@1.0, run: pass
The type's only rendered example and the founding evidence for all three marks: a cyan flow
ribbon threading the granule bed (`working`), a fine spray leaving the outlet (`output`), and
rust-toned mineral specks held in the upper layer (`caught`).
```
A 3D technical see-through render. NOT photography. Dark engineering background.

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

## KNOWN-FLAKY
- **Spec labels appear unasked, 1 observation.** The seed exemplar this type learns from
  carries a `300mAh Li-ion` label. Watch for it; the text ban is in `internals` for that
  reason.
- **Shell silhouette drifting once transparency is requested**, predicted and not yet
  observed. If it recurs, the fallback is multi-pass — generate the opaque product, then edit
  it to translucent (adapter Rule 3).

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

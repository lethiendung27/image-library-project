---
id: 03-use-sequence
step: 3
job: use
device: sequence
version: "1.2"
status: active
replaced_by: null
ratios: ["1:1", "4:5"]
channels: [marketplace, landing-page, advertorial]
requires_product_photo: true
generation_mode: single-pass
axes:
  camera_lock: [handheld]
variants: []
exempt_from: [G3, G4]
pairs_with: [03-mechanism-ghostbody]
never_with: []
---

# 03-use-sequence

## PURPOSE
Reassure about operation: three stacked panels, one action each, read by action logic
alone — no numbers, no arrows. Answers "can I actually use this?" without looking like
an instruction manual.

## TRIGGER
use_when: >
  The product has more than one operation step, or buyers may assume it is
  complicated. Image 4-5 in the gallery. Answers the question "will I manage to
  use this".
avoid_when: >
  The product has one obvious action. Never as a main image, never as a
  scroll-stopper.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 03-use-sequence v1.2
REGISTER: warm lifestyle photography, close range.            -> PARTS/register

[PRODUCT REFERENCE] the attached photo is the exact reference, in every panel.
[LAYOUT] three panels stacked, thin white gutters.            -> PARTS/layout
[CONTINUITY] one pair of hands, one place, one light.         -> PARTS/continuity
[PANELS] prepare, then use, then result.                      -> PARTS/panels
[ENVIRONMENT] one ordinary room, named once.                  -> PARTS/environment
[MARKS] only if the product emits something visible:          -> MARKS
  emission, in the USE panel
```

## PARTS

**`register`** — warm lifestyle product photography at close range, natural and unstyled,
soft daylight. Not a diagram and not a manual: the whole point of the type is that it looks
like someone's kitchen rather than an instruction sheet.

**`layout`** — three horizontal panels stacked vertically with thin white gutters, no outer
border. **No numbers, no arrows, no step markers, no text of any kind.** The order is read
from the actions themselves, which is this type's entire discipline — see MARKS.

**`continuity`** — the make-or-break. The SAME hands in every panel: same skin tone, same
nails, same wrists, same sleeves. The same subject or surface throughout. The same warm
neutral palette and the same soft light direction. Get this wrong and the image reads as three
stock photos rather than one sequence.

Camera distance and framing may shift naturally between panels — the `camera_lock: handheld`
axis is definitional here, because pixel-locked framing would read as renders rather than as
someone's hands.

**`panels`** — one action per panel, never two. The original exemplar packed two actions into
its first panel and lost a beat.

- **PREPARE**: the single setup action, hands in frame, and the readiness signal visible — an
  indicator light, an opened part, a loaded state.
- **USE**: the core action in progress, mid-motion.
- **RESULT**: the action finishing, plus a second hand or gesture expressing the outcome.
  Warmer light than the previous panels, and **no new mechanics** — this panel closes on the
  relationship, not on more machinery, which is what separates the type from a dry manual.

The product sits near the centre of every panel and is never cropped out.

**`environment`** — one ordinary domestic setting with one or two incidental details, named
once and identical in all three panels.

## MARKS

**This type carries almost no marks, and the absence is the design.** Every other step-3 type
argues with graphic marks; this one argues with actions in sequence, and adding an arrow or a
number would turn it into the instruction manual its PURPOSE exists to avoid. The library has
exactly one entry here.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `emission` | whatever the product visibly puts out — spray, steam, light, foam — lit so it reads, made of the substance itself | the substance's own real colour | 1, in the USE panel only | **none** |

**`emission` exists only if the product genuinely emits** (G8). It is not a mark laid over the
photograph; it is a real thing in the scene, lit to be visible. Never invent an emission so a
panel looks active — G8's whole subject is not faking an effect so a PHOTO looks like it is
working, and a photographic register is where that is easiest to do and hardest to forgive.

The type is `exempt_from: [G3, G4]`: no signal colours, no correct-versus-wrong grading. There
is no wrong state here at all — nobody is doing it badly, because the argument is "this is
easy", not "this is better".

## SLOT CONSTRAINTS
- **The prompt budget** (ADR-013, ADR-015): a clause earns its place in a rendered prompt only
  if a render has failed without it, and it is removed only once a render has done without it
  and come back correct.
- One action per panel; the order readable without numbering.
- Continuity of hands before everything else.
- **Hands at close range are this type's highest model risk** — adapter Rule 5 names hands as
  the worst failure class in the library, and every panel here is hands. Expect retries.

## NEGATIVE
```
[G6] + step numbers, arrows, badges, different hands between panels,
different subject between panels, two actions in one panel,
product off-center, product cropped out, instruction manual look,
technical diagram, cold clinical lighting, different location between panels,
inconsistent palette, staged perfection
```
Canonical and model-agnostic; the adapter transforms it and no avoid line ships (ADR-014).

## WORKED EXAMPLES
### example: shower-filter-install — skeleton@1.0, run: untested
Product: metal shower filter · ratio 1:1 · camera_lock=handheld
- CONTINUITY — the same pair of hands throughout, the same chrome shower arm and white tiled
  wall, soft daylight from the left
- PREPARE — both hands unscrewing the existing shower head, the bare threaded arm visible
- USE — one hand holding the reference filter to the thread, the other turning it, mid-motion
- RESULT — filter fitted, water running in a clean even spray backlit so the streams read; one
  hand held open under the flow, palm up; warmer light
- ENVIRONMENT — ordinary home bathroom, a folded towel, a plant on the sill
Predicted failures: close-range hands on hardware, the library's highest extra-finger risk;
and a RESULT panel asked for both a visible result and a centred product, which compete for
space — if it breaks, choose one.

## KNOWN-FLAKY
(nothing observed — this type has one render in the ledger and no failures recorded)

## NOTES
Distinction within step 3: `ghostbody` and `xray` explain WHY a product works, `spec-split`
argues what is better inside, and this type answers "can I operate it". A gallery rarely needs
more than two step-3 answers, and this one is usually the second.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.2 (2026-08-13): restructured into a call-map plus PARTS and MARKS (ADR-012); skeleton
  1645 → 608. `emission` named as the type's only mark, and the MARKS section states plainly
  that the near-absence is the design: this type argues with actions rather than graphics, and
  an arrow or a number would make it the manual its PURPOSE avoids. `RATIO:` dropped per
  adapter Rule 4. `e8ca963`
- 1.1 (2026-08-11): channels gain `advertorial`. Demand evidence: two real advertorial pages
  for the wall cooler carry explicit numbered step sections, which is what this type serves.
- 1.0 (2026-08-10): initial from the pet-brush three-panel exemplar; exemplar fault encoded —
  two actions crowded into panel 1. seed: conversation.md.

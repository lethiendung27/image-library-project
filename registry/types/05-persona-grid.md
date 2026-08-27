---
id: 05-persona-grid
step: 5
job: persona
device: grid
version: "1.6"
status: active
replaced_by: null
ratios: ["1:1", "4:5"]
channels: [marketplace, landing-page]
requires_product_photo: true
generation_mode: single-pass
variants: [1plus3, 2x2, 1plus4]
exempt_from: []
pairs_with: [02-symptom-rail]
never_with: []
avoid_adjacent: [05-social-handoff]
---

# 05-persona-grid

## PURPOSE
Answer "is this for someone like me" by casting: maximally different people, identically
graded cells, one product colorway throughout. It does not argue — it casts.

## TRIGGER
use_when: >
  Need to show many different kinds of people using the product. Image 4-5 in
  the gallery or the closing image. Use when the audience is broad in age and
  context.

## SKELETON
A call-map. Each arrow names an entry in PARTS; the definition lives there once.
**No MARKS section:** this is a photographic collage and it casts rather than argues, so
nothing is added to the frame.

```
TYPE: 05-persona-grid v1.6 [--1plus3 | --2x2 | --1plus4]

[LAYOUT] cells, thin white gutters, no outer border.        -> PARTS/layout
[PRODUCT REFERENCE] attached photo is the exact reference.
[CONSTANT] what must match across every cell.               -> PARTS/constant
[VARIATION] what must differ, cell by cell.                 -> PARTS/variation
[PRODUCT] visible and unobstructed in EVERY cell.           -> PARTS/product
[CELLS] the hero, then the supports.                        -> PARTS/casting

REGISTER: clean lifestyle collage for e-commerce, bright, airy, sharp.
```

## PARTS

**`layout`** — the variant's cell arrangement, thin white gutters, no outer border, and no
graphic overlay of any kind.

**`constant`** — TWO things only: ONE product colourway, and one photographic FINISH — the
same lens character, the same contrast, the same skin rendering. That finish is what makes four
photographs read as one set.

**Palette and light are NOT constant, and this is the type's third pass at the same mistake.**
v1.0 locked posture and got four near-identical cells. v1.1 moved cohesion onto grade and light
and got four identical WORLDS — a bouldering wall, a hospital ward, a building site and a park
all rendered in one warm-sand palette under one soft daylight, with no night, no overcast and no
interior light anywhere. Each time the lock was moved up a level rather than removed. Cohesion
is the finish and the colourway; everything else belongs to the place.

**UNLOCKED IS NOT REQUIRED-TO-DIFFER, and that is the fourth pass.** v1.1 unlocked posture and
left it free; free means the model converges, and it did — four people upright and alone at a
flat surface, both hands on the product, looking down at it, under four genuinely different
lights. Posture and activity are now named per cell like the camera angle. **Not every cell is
about the product**: in some it is simply present and in use while the person gets on with
something else, which is what makes a grid look like life rather than a catalogue.

**`variation`** — what must differ, one value per cell, never repeated: **the palette and the
light, each taken from that cell's own real place and time of day** — an evening ward is
tungsten and dim, a building site is flat overcast, a park at noon is warm; the age, gender and
body situation of the subject; **the posture, the activity, and the person's RELATION to the
product** — carrying it, wearing it, filling it, packing it away, reaching for it, handing it
to someone, or using it hands-free while occupied with something else; the camera angle, chosen from eye-level side profile, high
three-quarter, low angle, over-the-shoulder, waist-level frontal, close crop on the
interaction; the environment; and the shot distance.

**`product`** — clearly visible and unobstructed in EVERY cell, occupying at least 15% of that
cell's height. **This is the survival threshold**: below it a cell degrades into a photograph
of a person. If a cell cannot meet it, tighten that crop until it does — and if the smallest
cells of a variant cannot hold the product at all, the variant is the wrong one.

**`casting`** — the largest cell goes to the persona with the **most specific condition and
the strongest emotion**, never to the most numerous persona. The type does not argue, it casts:
its whole job is answering *is this for someone like me*, and a specific person answers that
for more readers than a generic one.

## SLOT CONSTRAINTS
- G7 binds: every cell is a real person in a real place doing a real thing, and nothing is
  arranged only to make a photograph.
- **The prompt budget, four parts.** A clause reaches a rendered prompt only if a render has
  failed without it, THAT product can fail that way, **the model can act on it inside one
  generation**, and it is stated once. Ceiling **1800 characters**. Since ADR-014 no
  `Strictly avoid:` line is rendered.

## NEGATIVE
```
[G6] + borders around cells, badges, arrows,
product hidden or cropped out in any cell, product smaller than 15% of cell height,
different product colors between cells, stylised or filtered grade on any cell,
identical camera angles, repeated framing,
same environment twice, stock photo collage look, duplicate-looking people
```
Canonical and model-agnostic. Since ADR-014 it is not rendered into the prompt.

## VARIANTS
### --1plus3 (default)
One large cell right, three stacked left.
### --2x2
Four equal cells; no hero emphasis — use when no persona dominates.
### --1plus4
One large + four small; only at 4:5 ratio, and only when the product passes the 15%
rule in fifth-size cells.

## WORKED EXAMPLES
Rendered at 1.5 and owner-passed, kept in FULL text per SPEC §3.3.

### example: food-flask-1plus3 — skeleton@1.5, run: pass
```
TYPE: 05-persona-grid v1.5 --1plus3
REGISTER: clean lifestyle collage for e-commerce, sharp.
LAYOUT: one large cell on the right, three stacked on the left, thin white gutters, no
outer border, no graphic overlay.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the flask in every cell. Preserve its
shape, proportions, material, finish and colour exactly.

[CONSTANT]
One flask colourway, and one photographic finish across all cells: same lens character,
same contrast, same skin rendering. Nothing else is shared.

[VARIATION]
Each cell has its own light, its own posture and its own relation to the flask. No cell is
stylised or filtered.

[PRODUCT]
The flask is clearly visible and unobstructed in every cell, at least 15% of that cell's
height.

[HERO CELL, large right]
Woman in her 50s crouched on a school playing field in flat grey drizzle, coat hood up,
pouring from the flask into its cup for a child out of frame. Low angle from grass height,
medium shot.

[SUPPORT, top left]
Man in his 30s walking a snowy platform at blue dusk, flask clamped under one arm while
both hands zip his coat. Eye-level side profile, wide shot.

[SUPPORT, middle left]
Woman in her 20s in a night nursing station under warm tungsten, filling the flask at a
sink with her back half turned, a chart in her other hand. High three-quarter, close crop.

[SUPPORT, bottom left]
Man in his 60s seated on a garage floor under a bare bulb, mending a bike, flask standing
open beside his knee, not being touched. Waist-level frontal, medium shot.
```
Four different bodies under four different lights, cohering on finish and colourway alone —
the state this type took four versions to reach. The garage cell is the one that is not about
the product: he is mending a bike and the flask simply stands beside him.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.6 (2026-08-13): **type PASSED by the owner; file finalised.** WORKED EXAMPLES opens with
  the 1.5 flask grid in full text — four bodies, four lights, cohesion on finish and colourway
  alone, and one cell that is not about the product. Four versions were spent moving one lock
  up a level at a time; the sentence that ended it is that unlocked is not required-to-differ.
- 1.5 (2026-08-13): **posture, activity and relation to the product join `variation`.** Owner:
  the poses, activities and contexts are not flexible. The 1.4 light fix landed and the
  uniformity moved again, to the body. Fourth slot, same disease, and the sentence that ends it
  is that UNLOCKED IS NOT REQUIRED-TO-DIFFER — v1.1 unlocked posture and left it free, and free
  converges.
- 1.4 (2026-08-13): **palette and light move from `constant` to `variation`.** Owner: meaning
  and logic good, but one colour, one space, one weather — and the render was a faithful
  execution of the old law. The type's THIRD pass at one mistake: v1.0 locked posture, v1.1
  locked grade and light, each time moving the lock up a level instead of removing it. Cohesion
  is now one product colourway and one photographic FINISH. NEGATIVE drops two tokens that
  encoded the uniformity — an evening ward SHOULD be darker.
- 1.3 (2026-08-13): **restructured into a call-map plus PARTS** (ADR-012), owner instruction.
  `PARTS` owns `layout`, `constant`, `variation`, `product`, `casting`. **No MARKS section** —
  a photographic collage that casts rather than argues adds nothing to the frame, the same
  shape as `04-proof-lockedframe`. `RATIO:` dropped per adapter Rule 4, and the skeleton header
  had read v1.1 under a v1.2 type. Carried in: name the palette TONES, never a count of them.
  WORKED EXAMPLES removed, untested and predating this shape. ADR-014 adopted.
- 1.2 (2026-08-11): channels gain `landing-page` (the routing table listed it in both
  the social-proof and personas cells). Nothing in use_when or avoid_when was
  channel-specific; the restriction was never argued, only inherited.
- 1.1 (2026-08-10): cohesion moved from posture-lock to grade+light+colorway; per-cell
  camera angle and shot distance made mandatory-different; 15% visibility rule added;
  G1 block added. Evidence: v1.0 grids rendered four near-identical cells
  (user feedback: needs varied angles and environments). seed: conversation.md.
- 1.0 (2026-08-10): initial as SQR-SCOPE-PERSONAGRID from the pregnant-woman /
  wheelchair / office / night-driver exemplar; exemplar faults encoded (product
  invisible in two cells, colorway mismatch). seed: conversation.md.

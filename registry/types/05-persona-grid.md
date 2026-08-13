---
id: 05-persona-grid
step: 5
job: persona
device: grid
version: "1.3"
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
avoid_when: >
  The audience is narrow and specific — a grid dilutes the positioning. Never as
  a main image. Not when the product is too small to stay visible inside a
  sub-cell (15% rule).

## SKELETON
A call-map. Each arrow names an entry in PARTS; the definition lives there once.
**No MARKS section:** this is a photographic collage and it casts rather than argues, so
nothing is added to the frame.

```
TYPE: 05-persona-grid v1.3 [--1plus3 | --2x2 | --1plus4]

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

**`constant`** — what carries cohesion, and it is three things and not four: the colour grade
and palette (**name the tones, never a count of them**), the light quality — soft, diffused or
directional, never harsh or coloured — and ONE product colourway throughout. A second colourway
reads as a different product.

Posture is deliberately NOT locked. Locking it produced four near-identical cells at v1.0, and
cohesion moved onto grade, light and colourway instead.

**`variation`** — what must differ, one value per cell, never repeated: the age, gender and
body situation of the subject; the camera angle, chosen from eye-level side profile, high
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
different product colors between cells, mismatched color grade between cells,
one cell darker than the others, identical camera angles, repeated framing,
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

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
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

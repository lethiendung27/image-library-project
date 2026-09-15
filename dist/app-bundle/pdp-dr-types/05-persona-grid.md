---
id: 05-persona-grid
step: 5
job: persona
device: grid
version: "1.6"
status: active
replaced_by: null
channels: [marketplace, landing-page]
requires_product_photo: true
generation_mode: single-pass
variants: [1plus3, 2x2, 1plus4]
exempt_from: []
pairs_with: [02-symptom-rail]
never_with: []
avoid_adjacent: [05-social-handoff]
copied_from: 05-persona-grid
copied_at_version: "1.6"
blocked_by: null
---

# 05-persona-grid

## PURPOSE
Answer "is this for someone like me" by casting: maximally different people, identically
graded cells, one product colorway throughout. It does not argue — it casts.

**Copied verbatim from `registry/types/05-persona-grid.md` at version 1.6** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

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

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.6 (2026-09-15): copied verbatim from `registry/types/05-persona-grid.md` at 1.6, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.

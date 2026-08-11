---
id: 05-persona-grid
step: 5
job: persona
device: grid
version: "1.1"
status: active
replaced_by: null
ratios: ["1:1", "4:5"]
channels: [marketplace]
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
```
TYPE: 05-persona-grid v1.1
RATIO: [1:1 / 4:5]
LAYOUT: [1plus3 / 2x2 / 1plus4], thin white 4px gutters, no outer border,
photographic collage, no graphic overlays.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly across all cells.

[MUST MATCH across cells]
Color grade and palette: [3-4 neutral tones].
Light quality: [soft / diffused / directional], never harsh or colored.
Product colorway: [one only].
Overall photographic finish: same lens character, contrast and skin rendering.

[MUST DIFFER across cells]
Age, gender and body situation of the subject.
Camera angle, one per cell, chosen from: eye-level side profile / high three-quarter /
low angle / over-the-shoulder / waist-level frontal / close crop on the interaction.
Environment type, one per cell, and shot distance (wide, medium, close).

[PRODUCT VISIBILITY RULE]
The product must be clearly visible and unobstructed in EVERY cell,
occupying at least 15% of that cell's height.
If a cell cannot meet this, tighten the crop until it does.

[HERO CELL, largest]
[most specific persona: age, gender, distinguishing condition] in [wardrobe],
[interaction with product] in [environment 1], [warm emotional expression].
Camera: [angle 1], [shot distance].

[SUPPORT CELL 1] [persona 2] in [environment 2], [activity]. Camera: [angle 2], [distance].
[SUPPORT CELL 2] [persona 3] in [environment 3], [activity]. Camera: [angle 3], [distance].
[SUPPORT CELL 3] [persona 4] in [environment 4], [activity]. Camera: [angle 4], [distance].

STYLE: clean lifestyle collage for e-commerce, bright airy, sharp focus, 4K.
NO text, no logo, no watermark, no badges, no arrows.
```

## SLOT CONSTRAINTS
- Casting law: the largest cell always goes to the persona with the most specific
  condition and strongest emotion — never the most numerous persona.
- The cohesion burden sits on grade + light quality + product colorway (v1.1 change);
  posture is deliberately NOT locked — locking it produced four near-identical cells.
- One product colorway across all cells, no exceptions (a second colorway reads as a
  different product).
- The 15% visibility rule is the survival threshold — below it a cell degrades into a
  photo of a person.

## NEGATIVE
```
[G6] + borders around cells, badges, arrows,
product hidden or cropped out in any cell, product smaller than 15% of cell height,
different product colors between cells, mismatched color grade between cells,
one cell darker than the others, identical camera angles, repeated framing,
same environment twice, stock photo collage look, duplicate-looking people
```

## VARIANTS
### --1plus3 (default)
One large cell right, three stacked left.
### --2x2
Four equal cells; no hero emphasis — use when no persona dominates.
### --1plus4
One large + four small; only at 4:5 ratio, and only when the product passes the 15%
rule in fifth-size cells.

## WORKED EXAMPLES
### example: knife-sharpener — skeleton@1.1, run: untested
Product: rolling knife sharpener · ratio 1:1 · variant --1plus3
- MUST MATCH — warm cream, pale oak, soft white and matte black palette; soft diffused daylight in every cell, never harsh or coloured; one product colorway throughout; same lens character, contrast and skin rendering
- MUST DIFFER — age, gender, environment, camera angle and shot distance in every cell
- PRODUCT VISIBILITY — clearly visible and unobstructed in every cell, at least 15% of that cell's height
- HERO CELL (large, right) — woman early 30s in a cream linen apron sharpening a chef's knife on a pale oak counter in a bright modern kitchen, looking down, focused and satisfied; waist-level frontal, medium shot
- SUPPORT 1 (top left) — man late 60s, grey hair, sharpening a small paring knife at a rustic wooden counter, relaxed; eye-level side profile, wide shot showing the room
- SUPPORT 2 (middle left) — man in his 20s sharpening a santoku in a narrow apartment kitchen at night, warm lamp light kept soft; high three-quarter over his hands, close crop
- SUPPORT 3 (bottom left) — woman in her 40s sharpening a hunting knife on a wooden picnic table outdoors, blurred trees behind; low angle from table height, medium shot
Predicted failures: (1) a handheld product this small dropping under 15% in the support
cells — the deliberate stress test of the avoid_when threshold; (2) knives in many
hands tripping safety filters or producing deformed hands.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.1 (2026-08-10): cohesion moved from posture-lock to grade+light+colorway; per-cell
  camera angle and shot distance made mandatory-different; 15% visibility rule added;
  G1 block added. Evidence: v1.0 grids rendered four near-identical cells
  (user feedback: needs varied angles and environments). seed: conversation.md.
- 1.0 (2026-08-10): initial as SQR-SCOPE-PERSONAGRID from the pregnant-woman /
  wheelchair / office / night-driver exemplar; exemplar faults encoded (product
  invisible in two cells, colorway mismatch). seed: conversation.md.

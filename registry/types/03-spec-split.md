---
id: 03-spec-split
step: 3
job: spec
device: split
version: "1.1"
status: active
replaced_by: null
ratios: ["1:1", "4:5"]
channels: [marketplace]
requires_product_photo: true
generation_mode: single-pass
axes:
  register: [commercial]
variants: [products]
exempt_from: [G5, G7]
pairs_with: [03-mechanism-ghostbody]
never_with: []
---

# 03-spec-split

## PURPOSE
Component-level superiority: old component (real, decayed, photographic) vs new
component (engineered, pristine, rendered), diagonal split, VS badge. No people, no
symptoms. The highest-risk type in the library — see NOTES.

## TRIGGER
use_when: >
  Categories where buyers genuinely compare component specs: motors, batteries,
  chips, abrasive materials, filter media, blades. Image 4-6 in a marketplace
  gallery. Use ONLY when the product truly contains the rendered component.
avoid_when: >
  Categories sold on emotion, brand or aesthetics. Never on paid-social or
  advertorial — this aesthetic signals cheap goods off-marketplace. Never as a
  main image.

## SKELETON
```
TYPE: 03-spec-split v1.0
RATIO: [1:1 / 4:5]
LAYERS: diagonal two-panel split + center badge + product inset at bottom.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the inset only.
Preserve shape, proportions, material, finish and color exactly.

[SPLIT]
A diagonal division running from [top-left to bottom-right / top-right to
bottom-left], edged with a thin glowing [accent color] line.
The two halves must be visually unequal in energy: the right half advancing.

[LEFT PANEL: THE OLD COMPONENT]
Photographic register. Desaturated grayscale.
A generic, unbranded [component type] in aged condition:
[3 signs of degradation]. Dusty, dim environment, no styling.
It must look like a real object photographed in the real world.

[RIGHT PANEL: THE NEW COMPONENT]
3D render register. A pristine [component type] of the improved type,
[key visible technical differentiator], cool [accent color] rim lighting,
floating against a dark gradient, sharp reflective surfaces.
It must look engineered, not photographed.

[CENTER BADGE]
Large [metallic] "VS" at the intersection of the diagonal,
with a burst of [warm] sparks at the seam. Nothing else at the center.

[PRODUCT INSET, bottom]
The reference product, complete and whole, on a plain white background
inside a rounded rectangle, occupying [20-25%] of the frame width.
This is the only place the finished product appears.

[HONESTY CONSTRAINT]
The left component must not carry any brand mark, logo or identifiable design.
The right component must be the type genuinely used inside the product.
Do not render a component the product does not contain.

STYLE: high-contrast technical comparison graphic, e-commerce, sharp, 4K.
NO text beyond the VS badge, no logo, no watermark.
```

## SLOT CONSTRAINTS
- G5 exemption is deliberate and meaningful: photo = "what rots in the real world",
  render = "what was engineered". This is the only type where breaking register lock
  is the message.
- The left component is generic and unbranded — a claim about a category, never about
  a competitor.
- Material differentiators render better as **light behavior** than as material names
  (e.g. "a dense uniform field of fine crystalline grit catching the light" instead of
  "diamond coating").
- The VS badge is the only text permitted anywhere in the library; models render text
  unreliably — plan to composite it in post.

## NEGATIVE
```
[G6] + brand marks, recognizable trademarks, readable model numbers,
both halves rendered, both halves photographic, symmetrical composition,
vertical split, dull center, low contrast, product inset missing,
product inset cropped, cartoonish explosion, fire, smoke, gore,
human hands, human figures
```

## VARIANTS
### --products
Whole-product photographic comparison — category displacement: the legacy solution
class vs the reference product. Both halves are real photographs (G5 symmetric in
this variant; the base's photo-vs-render asymmetry does not apply).
Diff vs base:
```
[LEFT PANEL, replaces THE OLD COMPONENT]
The generic legacy/rival-class product, photographed in ordinary aged-but-
plausible condition, desaturated or cool-graded. UNBRANDED.
FAIRNESS RULE (imported from 04-proof-lockedframe): wear is evidence,
catastrophe is staging. Never broken, shattered, or surrounded by debris —
a demolished rival reads as theater and voids the comparison.

[RIGHT PANEL, replaces THE NEW COMPONENT]
The reference product, photographic register, in an honest use context,
brighter and cleaner (G4). No hero lighting beyond that.

[CENTER BADGE] unchanged: the VS at the seam remains the single marker.
No X/check pair on top of it — one binary argument, one marker.
POLARITY LOCK: wrong/legacy on the LEFT. (All four source exemplars
inverted this; market habit, deliberately not imported.)

[PRODUCT INSET, bottom] does NOT apply — the whole products are already
in frame.

[MEASURED EVIDENCE] (optional)
Matching instrument insets on BOTH panels — same instrument, same position,
same scale (e.g. sound-level meters). Instrument digits are diegetic text
(G6 scope note) and must come from real measurements; composite real
readouts in post, never model-drawn.
```
Negative additions: `shattered or destroyed rival product, debris, exaggerated
failure scene, check and X badges stacked with the VS, mismatched instrument
insets between panels`

## WORKED EXAMPLES
### example: knife-sharpener — skeleton@1.0, run: untested
Product: rolling knife sharpener (inset only) · ratio 1:1 · axes: register=commercial
- SPLIT — diagonal top-left to bottom-right, edged with a thin glowing cyan line; the right half advances into the left
- LEFT PANEL, OLD COMPONENT — photographic register, desaturated grayscale: a generic unbranded ceramic sharpening rod and a worn steel honing rod in a dim drawer, ceramic chipped along its length, steel scored with deep uneven scratches, metal filings and grey dust around them; must read as a real object photographed
- RIGHT PANEL, NEW COMPONENT — 3D render register: a pristine circular diamond-coated abrasive disc, dense uniform crystalline grit catching the light, edge-on so face and profile both read, cool cyan rim light, dark gradient behind, sharp reflective surfaces; must read as engineered, not photographed
- CENTER BADGE — large brushed-gold VS at the diagonal intersection with a burst of warm orange sparks at the seam; nothing else at center
- PRODUCT INSET (bottom) — the reference sharpener, complete and whole, on plain white inside a rounded rectangle, about 22% of frame width; the only place the finished product appears
- HONESTY — the left components carry no brand mark, logo or identifiable design
Predicted failures: (1) diamond grit rendering as generic roughness — the light-effect
phrasing above is the mitigation; (2) the VS text coming out mangled — composite in
post.

## KNOWN-FLAKY
(populated from observation evidence only)

## NOTES
Credibility risks, accepted with open eyes: the aesthetic (gold VS, sparks, neon rim)
is learned by buyers as a cheap-goods signal — it lifts conversion on price-driven
marketplaces and depresses it upmarket. The right half is a render and proves nothing;
the left half is not actually a competitor's part. Both are soft claims. The
[HONESTY CONSTRAINT] is the guardrail: never render a component the product does not
contain.

## CHANGELOG
- 1.1 (2026-08-10): --products variant added (whole-product photographic comparison,
  fairness rule, polarity lock, optional measured-evidence insets). Evidence: 3
  observations across 3 domains — obs sha256:d4165b…, sha256:a98ef3…, sha256:262bca…
  (batches C, E, G). Market habits excluded by rule: destroyed rivals, inverted
  check/X polarity.
- 1.0 (2026-08-10): initial from the motor-stator VS exemplar; risk analysis and
  honesty constraint encoded at birth. seed: conversation.md.

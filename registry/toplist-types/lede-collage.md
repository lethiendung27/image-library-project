---
id: lede-collage
version: "0.1"
status: reserved
replaced_by: null
products_in_frame: many
requires_product_photo: true
awareness: [product-aware, most-aware]
inherits: null
blocked_by: reference-photo-limit
exempt_from: [G7]
---

# lede-collage

## PURPOSE
The five as an index: cut-outs on a flat ground, arranged for reading rather than
photographed together. It claims nothing about possession — only that these are the
entries.

## TRIGGER
use_when: >
  The reader wants the shortlist at a glance and the page's value is the selection
  rather than the testing. The input carries three or more distinct competing products.
  Take it over lede-lineup where the units are too unlike each other in size to share a
  surface honestly, or where no plausible single surface exists for the category.

## BOUNDARY
**Against `lede-lineup`** — assembled against photographed, enumeration against
possession. See that file; the distinction is stated there once and is not restated here.

**The overlay text that usually defines this format in the market is NOT part of this
type.** Good Housekeeping and Dotdash Meredith collages carry "BEST X" across the frame;
this namespace bakes no words (`toplist-instruction.md`, *Text*). What is left is the
arrangement, and if the arrangement alone does not carry the argument then this type does
not survive its first render round.

## SKELETON
```
TYPE: lede-collage v0.1
REGISTER: graphic product composition, one frame, no words anywhere in the picture.

[PRODUCT REFERENCES]  one attached photo per unit.                      -> G1, and see BLOCK
[CUT-OUTS]            3-5 units, each cleanly cut out, no shared scene.
[ARRANGEMENT]         a reading order the eye can follow; no unit favoured.
[GROUND]              one flat tone. -> toplist-instruction, the ADR-068 ground rule
[SHADOW]              a faint contact shadow per unit or none at all, applied equally.
```

**G7 exemption, narrow.** Cut-outs on a flat ground are a graphic layer rather than a
scene, which G7's own scope note already reads that way for a product knockout. Every
other G7 test still binds.

## NEGATIVE
```
[G6] + a favoured unit, a rank number, a badge, a podium, a scene, a person,
a drop shadow under one unit only, any word, price or logo baked into the picture
```

## BLOCK — why this is `reserved`
The same two decisions as `lede-lineup`, for the same reasons: the one-reference-photo
limit and `SPEC.md:256` on competitor brand marks. Whichever way they go, both types move
together.

## CHANGELOG
- 0.1 (2026-09-09): drafted `reserved`. Kept separate from `lede-lineup` on SPEC §3.1 —
  two arguments — and flagged in that file as the one to merge away if a render round
  shows readers take the same meaning from both. ADR-069.

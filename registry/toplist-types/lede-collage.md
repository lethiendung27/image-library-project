---
id: lede-collage
version: "0.2"
status: reserved
replaced_by: null
products_in_frame: many
requires_product_photo: true
awareness: [product-aware, most-aware]
text_layer: [title, badge]
copied_from: null
copied_at_version: null
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

**The overlay text IS part of this type** (ADR-071). Good Housekeeping and Dotdash
Meredith collages carry "BEST X" across the frame, and the corpus agrees: 2 of 5 collage
observations carry an award badge over the cut-outs. `text_layer: [title, badge]`, so
**G16 binds every word and the badge here** — the line cap, the badge interior, the
mobile floor, the watermark corner.

What may be printed is the page's own line about its own ranking. **The two award marks in
the corpus are a publisher's own mark on that publisher's own page** (`CNET LAB TEST
WINNER`, `CNET PEOPLE'S PICKS`); reproducing another party's is the trademark question
`toplist-instruction.md` records as still unanswered.

## SKELETON
```
TYPE: lede-collage v0.2
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES]  one attached photo per unit.                      -> G1, and see BLOCK
[CUT-OUTS]            3-5 units, each cleanly cut out, no shared scene.
[ARRANGEMENT]         a reading order the eye can follow; no unit favoured.
[GROUND]              one flat tone. -> toplist-instruction, the ADR-068 ground rule
[SHADOW]              a faint contact shadow per unit or none at all, applied equally.

[TITLE]               the page's own line about its own ranking. Optional. -> G16/title
[BADGE]               one mark, the page's own verdict. Optional.          -> G16/badge
```

**G7 exemption, narrow.** Cut-outs on a flat ground are a graphic layer rather than a
scene, which G7's own scope note already reads that way for a product knockout. Every
other G7 test still binds.

## NEGATIVE
```
[G6] + a favoured unit, a rank number, a badge, a podium, a scene, a person,
a drop shadow under one unit only, a price, a brand logo, a certification seal,
a press logo, a third-party award mark, a fabricated rating or star row
```

## BLOCK — why this is `reserved`
The same two decisions as `lede-lineup`, for the same reasons: the one-reference-photo
limit and `SPEC.md:256` on competitor brand marks. Whichever way they go, both types move
together.

## CHANGELOG
- 0.2 (2026-09-09): `text_layer: [title, badge]` (ADR-071, owner instruction) — the
  "BEST X" overlay is the market form and 2 of 5 corpus observations carry a badge, so it
  is part of the type rather than banned from it. G16 now binds this file. **Still
  `reserved`**: its blocker was never the text, it is the one-reference-photo limit
  against `products_in_frame: many`.
- 0.1 (2026-09-09): drafted `reserved`. Kept separate from `lede-lineup` on SPEC §3.1 —
  two arguments — and flagged in that file as the one to merge away if a render round
  shows readers take the same meaning from both. ADR-069.

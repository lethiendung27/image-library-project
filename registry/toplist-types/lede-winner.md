---
id: lede-winner
version: "0.1"
status: reserved
replaced_by: null
products_in_frame: one
requires_product_photo: true
awareness: [product-aware, most-aware]
inherits: null
blocked_by: G16-award-row
exempt_from: [G7]
---

# lede-winner

## PURPOSE
The number one alone, presented as chosen. A packshot carrying a verdict — "Best
Overall", a score, a rank — where the verdict is the argument and the product is its
subject.

## TRIGGER
use_when: >
  Purchase-intent traffic on a page whose ranking is its product, where one pick
  dominates and the reader's remaining question is only which. Take it over lede-lineup
  when the page's value is the verdict rather than the coverage.

## BOUNDARY
**Against `07-identity-pack`** (image registry, staging) — and this boundary is the
reason the file is reserved rather than active. That type argues IDENTITY: what the thing
is, as it arrives. This one argues SELECTION: that it won. **Strip the verdict mark and
nothing is left that `07-identity-pack` does not already do**, so the mark is not a
decoration on this type — it is the type.

**Against `lede-inuse`** — no scene, no use, no place. A verdict is not delivered in a
living room.

## SKELETON
```
TYPE: lede-winner v0.1
REGISTER: commercial product photograph, one frame.

[PRODUCT REFERENCE]  the attached photo is the exact reference.         -> G1
[SUBJECT]            the winning unit alone, the brand face to the lens.
[VERDICT MARK]       the rank or award, as a mark.                      -> see BLOCK
[GROUND]             -> toplist-instruction, the ADR-068 ground rule
[LIGHT]              broad and even; every printed word on the product legible.
```

## NEGATIVE
```
[G6] + a second unit, a competitor's product, a person, a scene,
a price, a fabricated rating or star row, a certification seal
```

## BLOCK — why this is `reserved`
`registry/rules.md` G16's content table marks two rows **LAW, not taste**, and this type
needs both:

- *"a certification mark, a press logo, an award, a named expert"* — a trademark question
  the library declined to answer on 2026-08-18;
- *"a person's name, a rating, a star row, a review count, a verified mark"* — G14 calls a
  fabricated endorsement illegal under FTC endorsement rules, and G14 binds the SLOT, so
  G16 has nothing to waive.

**A distinction worth putting in front of whoever decides.** "Best Overall" on a top-N
page is not an award issued by an outside body; it is the page's own editorial verdict
about its own ranking. That may be a different question from a certification seal, and it
is one this file is not entitled to answer. A numeric score is a separate matter again
and lands on `argument-faults.md` A15.

Both rows are struck only by ADR. Until then this type is not routable and no prompt is
written from it.

## CHANGELOG
- 0.1 (2026-09-09): drafted `reserved`. Recorded plainly: without its verdict mark this
  type collapses into `07-identity-pack`, which is the absorption ladder of SPEC §3.2
  doing its job rather than a defect in the draft. ADR-069.

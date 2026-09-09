---
id: lede-winner
version: "0.2"
status: active
replaced_by: null
products_in_frame: one
requires_product_photo: true
awareness: [product-aware, most-aware]
text_layer: [title, badge]
copied_from: null
copied_at_version: null
blocked_by: null
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
TYPE: lede-winner v0.2
REGISTER: commercial product photograph, one frame.

[PRODUCT REFERENCE]  the attached photo is the exact reference.         -> G1
[SUBJECT]            the winning unit alone, the brand face to the lens.
[VERDICT MARK]       the page's own verdict, as a mark.        -> SLOT CONSTRAINTS
[GROUND]             -> toplist-instruction, the ADR-068 ground rule
[LIGHT]              broad and even; every printed word on the product legible.
```

## NEGATIVE
```
[G6] + a second unit, a competitor's product, a person, a scene,
a price, a fabricated rating or star row, a certification seal,
a press logo, a third-party award mark, an invented placing or score
```

## SLOT CONSTRAINTS
**The verdict mark is this type and it is now permitted** (ADR-071). The distinction this
file put in front of the owner is the one that was taken: *"Best Overall" on a top-N page
is not an award issued by an outside body — it is the page's own editorial verdict about
its own ranking.* That is what may be printed.

- **The verdict text comes from the product input's rank or verdict field and from
  nowhere else.** A prompt may not invent a placing. The field does not exist yet — it is
  item 2 of the missing list in `toplist-instruction.md` — so **a page without it cannot
  route this type**, the same way an empty `reference_photos` refuses it. That is a
  mechanical precondition, not a block on the type.
- **A SCORE is a figure and carries A15's leash**: it enters the frame only where the
  input carries it. Never a rounded-up number, never one the prompt chose.
- **Another party's mark stays refused.** A certification seal, a press logo, a
  third-party award — the corpus carries `CNET LAB TEST WINNER` and `CNET PEOPLE'S PICKS`
  because on CNET's page CNET is the issuing body. On a page that is not theirs it is a
  trademark question, still unanswered since 2026-08-18.
- **A fabricated endorsement stays refused** — a customer's name, star row, review count
  or verified mark. G14, and it binds the SLOT.
- **G16 binds every word and the badge**: the line cap, the badge interior (one internal
  tone step, two type sizes), the mobile floor, the watermark corner. Not restated here.

## CHANGELOG
- 0.2 (2026-09-09): **reserved → active** (ADR-071, owner instruction). The verdict mark
  is permitted where it is the PAGE'S OWN — the distinction 0.1 put to the owner is the
  one taken. `text_layer: [title, badge]`, so G16 binds this type. `BLOCK` becomes `SLOT
  CONSTRAINTS`: the verdict text comes from the input's rank field, a score carries A15's
  leash, and a third-party mark and a fabricated endorsement stay refused because the
  permission did not cover them.
- 0.1 (2026-09-09): drafted `reserved`. Recorded plainly: without its verdict mark this
  type collapses into `07-identity-pack`, which is the absorption ladder of SPEC §3.2
  doing its job rather than a defect in the draft. ADR-069.

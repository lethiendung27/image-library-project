---
id: lede-winner
version: "0.3"
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
**Against `07-identity-pack`** (image registry, staging) — and this boundary is why the
verdict mark had to be permitted before the type could go active. That type argues
IDENTITY: what the thing is, as it arrives. This one argues SELECTION: that it won. **Strip the verdict mark and
nothing is left that `07-identity-pack` does not already do**, so the mark is not a
decoration on this type — it is the type.

**Against `lede-inuse`** — no scene, no use, no place. A verdict is not delivered in a
living room.

## SKELETON
```
TYPE: lede-winner v0.3
REGISTER: commercial product photograph, one frame.

[PRODUCT REFERENCE]  the attached photo is the exact reference.         -> G1
[SUBJECT]            the winning unit alone, the brand face to the lens.
[VERDICT MARK]       the page's own verdict, as a mark.        -> SLOT CONSTRAINTS
[GROUND]             a DESIGNED field: light and saturated.   -> PARTS/ground
[LIGHT]              broad and even; every printed word on the product legible.
```

## PARTS

**`ground`** — **light AND saturated**, and this is a correction to what the file shipped
with (`toplist-instruction.md`, *Ground*). ADR-068's rule was measured on 119
direct-response frames at saturation 0.06 and was imported here whole; this type's own
corpus runs **0.91 value and 0.60 saturation**. Light transfers, quiet does not.

The reason is structural rather than fashionable: the unit is cut out and carries no
scene, so **the ground is the only place colour can live**. A gradient or a strong flat
tone. An off-white studio sweep leaves a frame with nothing in it, which is what this
type's first prompt asked for before the corpus was measured.

**Sample size is one.** That single frame is also the type's only observation, so this
clause is the corpus at n=1 and the first render round is what confirms or kills it.

## MARKS

**The type owns the badge's FORM; G16 owns its WORDS** (ADR-012, ADR-043, ADR-068). Named
per product from what its register carries — never a default, which is the monotony that
took three passes to find on the direct-response types.

| form | shape | observations |
|---|---|---|
| `band` | a horizontal band across the frame carrying the verdict in one line | **0** — the owner's own named form ("dải Best Overall"), untested |
| `sticker` | a die-cut circle sitting on the ground like an applied label, often tilted a few degrees | 1 — the corpus's only winner mark, and it carried a promotion rather than a rank |
| `plaque` | a rectangle with a rule across it, a short line above and a year below | 2, both inside collages rather than on a winner frame |
| `roundel` | a filled circle carrying a short fact | 0 here; borrowed from the image registry's libraries |

**One mark per frame.** Two verdicts compete and neither is read.
**Three corners are open and the bottom-right is not** — the tool's watermark
(`adapters/nano-banana.md` Rule 7).

**A badge is not flat and it is not one word at one size** (G16, ADR-068). The table above
is an OUTLINE; the interior owes:

- **at least one internal tone step** — a rim, a ring, an outline inset from the edge, or a
  sheen. Measured on the direct-response round: 5 of 6 library badges came back dead flat
  at 0.02–0.09 value spread against 0.10–0.35 on four market badges, and the one that was
  not flat is the only one whose prompt named a second tone.
- **at least two type sizes.** Every corpus mark in this namespace carries them — a label
  over a big word, or a word over a year.
- **a colour the photograph does not have.** Harder here than anywhere else in the library,
  because this type's ground is a saturated designed field: the badge has to clear the
  ground as well as the product.

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
- 0.3 (2026-09-09): owner audit. **`PARTS/ground` added and it reverses half of what 0.2
  shipped**: ADR-068's rule was imported whole and this type's corpus runs saturation 0.60
  against its 0.06 — light transfers, quiet does not, because a cut-out unit leaves the
  ground as the only place colour can live. **`MARKS` added**: the type declared a badge
  and owned no form library, which is the gap ADR-068 closed for the three staging types
  and this file reopened. BOUNDARY's "the reason the file is reserved" is stale and
  corrected. Recorded plainly: the type is ACTIVE on **one** corpus observation, and that
  observation carries a discount sticker rather than a rank.
- 0.2 (2026-09-09): **reserved → active** (ADR-071, owner instruction). The verdict mark
  is permitted where it is the PAGE'S OWN — the distinction 0.1 put to the owner is the
  one taken. `text_layer: [title, badge]`, so G16 binds this type. `BLOCK` becomes `SLOT
  CONSTRAINTS`: the verdict text comes from the input's rank field, a score carries A15's
  leash, and a third-party mark and a fabricated endorsement stay refused because the
  permission did not cover them.
- 0.1 (2026-09-09): drafted `reserved`. Recorded plainly: without its verdict mark this
  type collapses into `07-identity-pack`, which is the absorption ladder of SPEC §3.2
  doing its job rather than a defect in the draft. ADR-069.

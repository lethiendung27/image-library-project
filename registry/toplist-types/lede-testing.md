---
id: lede-testing
version: "0.1"
status: active
replaced_by: null
products_in_frame: one
requires_product_photo: true
awareness: [solution-aware, product-aware]
inherits: null
blocked_by: null
exempt_from: []
---

# lede-testing

## PURPOSE
The work being done. Hands, an instrument and one unit under test on a working surface,
caught mid-measurement. It argues that somebody actually put these products through
something — the E-E-A-T signal of the format — and it argues it with apparatus rather
than with a number.

## TRIGGER
use_when: >
  The reader is choosing between options that look alike and the page's value is that it
  did the work. The product block carries a specification or raw_features rich enough
  that a measurable property is obvious — heat, draw, grip, flow, noise. Strongest where
  the category is crowded and the differences are invisible in a product photograph.
  Prefer lede-lineup where the argument is that the whole field was gathered rather than
  that one unit was measured.

## BOUNDARY
**Against `lede-inuse`** — the hands here belong to the REVIEWER, not the owner, and the
place is a bench or a working surface rather than a home. An instrument is in frame. Both
tests are checkable at a glance.

**Against `lede-lineup`** — one unit under test, not the field. The moment a second and
third unit stand beside it as candidates the frame is arguing coverage, not measurement.

**Against `lede-winner`** — a testing frame never says which one won.

## SKELETON
```
TYPE: lede-testing v0.1
REGISTER: editorial documentary photograph, one frame, no words anywhere in the picture.

[PRODUCT REFERENCE]  the attached photo is the exact reference.        -> G1
[UNIT]               one unit, in the position the measurement needs it.
[INSTRUMENT]         the measuring device, in contact with or aimed at the unit.
[HANDS]              a hand doing the work, cropped at the wrist or forearm.
[SURFACE]            a working surface — bench, worktop, test rig — with the tools of
                     the measurement and nothing decorative.
[LIGHT]              plain working light, even, no studio key and no rim.
[GROUND]             -> toplist-instruction, the ADR-068 ground rule
```

**The instrument is the argument and it must be doing something.** An instrument lying
beside the unit is a prop; an instrument in contact with it, held, is evidence. This is
`argument-faults.md` A12 read forwards: the hand carrying the argument must be employed
by the measurement and must not also be presenting the product to the lens.

## NEGATIVE
```
[G6] + a legible number, a digital readout in focus, a gauge whose scale can be read,
a chart, a second product class, a competitor's product, a person's face,
a lab coat, a clipboard, any word, price or logo baked into the picture
```
**The number ban is the type's whole legality and it is not stylistic.** A readable
measurement in the frame is `argument-faults.md` A15 — a figure the picture cannot
substantiate — and it is the fault three proposals (`04-proof-stat`,
`04-proof-instrument`, `04-proof-interface`) are already blocked behind. This type exists
BECAUSE the argument survives without the number: the apparatus and the hands carry it.
The moment a reading is legible, this type has become one of those three and must wait
for the same decision.

**No lab coat, no clipboard.** They are the costume of a credential this page does not
have, and a credential is what G16 refuses at its `named expert` row.

## CHANGELOG
- 0.1 (2026-09-09): drafted. The only one of the owner's seven that is a genuinely new
  argument AND blocked by nothing — one product, one reference photo, no text, no rank,
  no competitor mark, no figure. ADR-069.

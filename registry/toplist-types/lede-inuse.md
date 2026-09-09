---
id: lede-inuse
version: "0.1"
status: active
replaced_by: null
products_in_frame: one
requires_product_photo: true
awareness: [problem-aware, solution-aware]
inherits: 06-relief-scene
blocked_by: null
exempt_from: []
---

# lede-inuse

## PURPOSE
The product in the world, doing its job, and the state that follows. The dog on the
cooling mat rather than the dog on the hot floor. It argues that the category works,
without yet arguing which one to buy.

## TRIGGER
use_when: >
  The reader knows the problem and is weighing whether this kind of product is the
  answer. The product block's result_visibility is on-body or on-object, so there is a
  RESULT a photograph can hold. Editorial pages that open with a use scene rather than a
  problem scene take this; so does an ad-traffic page whose creative already showed the
  problem, where repeating it wastes the lede. Prefer lede-pain instead where the reader
  does not know the category exists.

## BOUNDARY
**Against `lede-pain`** — the product is present here and absent there.

**Against `lede-winner`** — this is a scene and that is a packshot. This one argues
living; that one argues choosing. A scene that has quietly become a hero shot on a clean
surface has crossed the line and should be filed as the other type.

**Against `lede-testing`** — the product here serves the OWNER, in the owner's own place,
and no instrument is in frame. A measuring device anywhere in the picture makes it a
testing frame.

The parent's own boundaries and its pairing with `01-pain-scene` are not restated.

## SKELETON
```
TYPE: lede-inuse v0.1 — inherits 06-relief-scene
REGISTER: candid documentary photograph, one frame, no words anywhere in the picture.

[REGISTER]     -> 06-relief-scene PARTS/register
[SUBJECT]      -> 06-relief-scene PARTS/subject
[GAZE]         -> 06-relief-scene PARTS/gaze
[ENVIRONMENT]  -> 06-relief-scene PARTS/environment
[PRODUCT]      -> 06-relief-scene PARTS/product      G1 binds; the reference photo is attached
[LIGHT]        -> 06-relief-scene PARTS/light
[GRADE]        -> 06-relief-scene PARTS/grade
[GROUND]       -> toplist-instruction, the ADR-068 ground rule
```
Defined in the parent, expanded from there. Nothing restated.

## NEGATIVE
```
[parent 06-relief-scene NEGATIVE] + a second product class, a competitor's product,
any word, number, price or logo baked into the picture, a measuring instrument
```

## CHANGELOG
- 0.1 (2026-09-09): drafted for the top-N lede slot, inheriting `06-relief-scene`. One
  real difference from the parent, recorded rather than smoothed: the parent's `use_when`
  says *"closing image of an advertorial or final frame of an ads creative"* and this
  slot is an OPENING image. After ADR-059 and ADR-060 position is not an admission test,
  so the parent needs no edit; this file carries the lede reading. Inherits the parent's
  attribute gate — `result_visibility: invisible` drops it. ADR-069.

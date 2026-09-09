---
id: lede-lineup
version: "0.1"
status: reserved
replaced_by: null
products_in_frame: many
requires_product_photo: true
awareness: [product-aware, most-aware]
inherits: null
blocked_by: reference-photo-limit
exempt_from: []
---

# lede-lineup

## PURPOSE
The whole field on one surface, in one light, photographed together. Its argument is
POSSESSION: these were all in the same room, so the shortlist was real. This is the
classic top-N hero — Wirecutter, Reviewed, Tom's Guide — and it is the format's strongest
"we tested them" signal short of showing the testing.

## TRIGGER
use_when: >
  The reader has decided to buy something in this category and is choosing between
  names. The input carries three or more distinct competing products. Strongest as the
  lede of a list whose value proposition is coverage — we looked at all of them — rather
  than depth on one.

## BOUNDARY
**Against `lede-collage`, and the distinction is the argument rather than the look.** A
lineup is PHOTOGRAPHED: one surface, one light, real shadows, and it claims the units
were together. A collage is ASSEMBLED: cut-outs on a flat ground, no shared light, and it
claims only that these are the five. Possession against enumeration.

They were nearly folded into one type with a `staging` axis, on the ground that both put
the field in one frame and differ in execution — which SPEC §3.2 would make an axis, not
a type. They are kept apart because **SPEC §3.1 makes the argument the identity**, and
"we had them all" is not "here are the five". **If a render round shows readers take the
same meaning from both, they merge and this file is the one that goes.**

**Against `lede-testing`** — the field, not one unit under measurement.

**Against `03-spec-lineup`** (image registry, staging) — that type shows several units of
ONE product, where exactly one thing differs, and its whole law is that single variable.
Here every unit is a different maker. Same picture shape, opposite argument.

## SKELETON
```
TYPE: lede-lineup v0.1
REGISTER: editorial product photograph, one frame, no words anywhere in the picture.

[PRODUCT REFERENCES]  one attached photo per unit, in rank order.       -> G1, and see BLOCK
[FIELD]               3-5 units on one surface, one light, real contact shadows.
[ARRANGEMENT]         no unit favoured by size, height, centring or light.
[SURFACE]             one real surface the category belongs to.
[LIGHT]               one soft source for the whole group; no unit separately lit.
[GROUND]              -> toplist-instruction, the ADR-068 ground rule
```

**No unit may be favoured, and the reason is borrowed rather than invented.**
`04-proof-lockedframe` states it four times and its own file says the judgement rule IS
the type: a frame that favours one panel by size or light has decided the comparison
before the reader does. A lineup that centres and up-lights the winner is a
`lede-winner` frame wearing five products.

## NEGATIVE
```
[G6] + a favoured unit, a rank number, a badge, a podium, a person,
any word, price or logo baked into the picture
```

## BLOCK — why this is `reserved`
Two decisions, neither the harness's:

1. **One reference photo per prompt.** `query/runbook.md:81` — *"one prompt, one
   generation call, at most one reference photo attached"*. Three to five units need
   three to five. The renderer accepts several; the limit is a number in this library's
   law, and its principle — one generation call — is not threatened by attaching five.
2. **`SPEC.md:256` — competitor brand marks never appear in prompts.** Every unit here is
   a different maker's product, visibly.

Until both are answered this type is not routable and no prompt is written from it.

## CHANGELOG
- 0.1 (2026-09-09): drafted `reserved`. The most valuable genuinely new argument of the
  owner's seven and the one furthest from being renderable. ADR-069.

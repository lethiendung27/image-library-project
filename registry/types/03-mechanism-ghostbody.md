---
id: 03-mechanism-ghostbody
step: 3
job: mechanism
device: ghostbody
version: "1.3"
status: active
replaced_by: null
ratios: ["1:1", "4:5"]
channels: [marketplace, landing-page, advertorial]
requires_product_photo: true
generation_mode: single-pass
variants: []
exempt_from: [G7]
pairs_with: [01-pain-split, 06-relief-hero]
never_with: []
---

# 03-mechanism-ghostbody

## PURPOSE
Explain WHY the product's shape works, via the mechanism inside the body. The anonymous
white mannequin has no identity, so every viewer projects themselves in — this type
sells to every segment, and it is deliberately cold.

## TRIGGER
use_when: >
  Need to explain WHY the product's shape works, through a mechanism inside the
  body that cannot be filmed. Image 3-4 in the gallery, after pain and before or
  after relief. Works for every audience because the body is anonymous.
avoid_when: >
  Main image or scroll-stopper positions, or when the product does not act on a
  body structure. This type is cold — there is nobody to empathize with.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 03-mechanism-ghostbody v1.3
REGISTER: 3D technical render. NOT photography.               -> PARTS/register

[PRODUCT REFERENCE] the attached photo is the exact reference.
[GHOST] pose, and where the body is cut.                      -> PARTS/ghost
[CUTAWAY] name the structure the product acts on.             -> PARTS/cutaway
[PRODUCT] placement and angle only.                           -> PARTS/product
[XCHECK] optional inset, wrong state beside correct.          -> PARTS/xcheck
[MARKS] name each one used, with its count:                   -> MARKS
  required: structure, and one of stress / support
  nothing in the frame is marked that is not named here

PALETTE LOCK: achromatic white and grey everywhere except the marks.
```

## PARTS

**`register`** — a clean medical-technical product render on a seamless white infinity
background, soft even studio lighting, subtle grey ambient occlusion only, no cast shadow on
a floor. Sharp, e-commerce infographic. **The product is the ONLY object in the frame with a
real material finish** — everything else is matte white or grey. That is this type's
signature and the thing a viewer reads first.

**`ghost`** — a featureless matte white mannequin: no face, no hair, no clothing, no skin
tone. Named pose, named interaction with the product, and the body cross-sectioned at a named
plane to reveal the interior. The anonymity is the argument, not a shortcut: nobody is being
empathised with, so nobody is excluded.

**`cutaway`** — the anatomical structure the product acts on, rendered INSIDE the body
silhouette and never floating on top of it. Anatomically accurate, and its contour follows
the product's contour, because the alignment between the two is the whole claim.

**`product`** — the reference product at a named position and a named angle, G2-clean: place
it, never describe it. Its contour must visibly align with the structure named in `cutaway`.
Sharp silhouette against white.

**`xcheck`** — an optional inset in one corner: two small rounded-square panels side by side,
flat 2D vector, light grey outline, white fill. LEFT the wrong state, RIGHT the correct one,
each carrying a `verdict` badge. Use it when the mechanism needs a before beside its after;
skip it when the cutaway already carries the argument, because the inset costs frame at
mobile size.

## MARKS

This type's own mark library, called by name from the skeleton. Its palette lock IS G3 at its
strictest — exactly four signal colours and nothing else — so every mark here is defined by
the colour G3 already assigns it.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `structure` | the neutral anatomy the argument sits in — bone, cartilage, the body's own framework | yellow / off-white ivory | as much as the cutaway shows | **none** |
| `stress` | the loaded or deformed element, filled where the load lands | red | as many as are loaded | **none** |
| `support` | the structure the product is carrying, filled along the contact | blue | 1 per supported structure | **none** |
| `heat` | wrong pressure or wrong heat, in the `xcheck` wrong panel only | orange | 1, inset only | **none** |
| `dims` | thin black double-headed arrows with fine extension lines offset clear of the product outline, drafting style | black | exactly 2 | **none** |
| `verdict` | circle badge above each `xcheck` panel, a FILLED SOLID DISC with the glyph cut out of it | red X, green check | exactly 2, inset only | **none** · also in `01-pain-split`, `02-cause-anatomy`, `06-relief-hero` |

**Every mark in this type is unproven.** It has never been rendered — zero records in
`eval/render-tests.jsonl`. The first render of each is its founding evidence and should be
logged as such.

**`dims` carries no numbers**, because G6 bans text. Without real specs a dimension arrow is
decoration, so enable it only when the product has a clear 3D volume that a drafting register
actually clarifies. This gate came from the mouth-tape example, where dims were dropped.

**The palette lock is absolute.** Red is stress, orange is wrong pressure or heat, blue is
correct support, yellow is structure. Nothing else carries colour anywhere in the frame. A
fifth colour does not dilute the system, it breaks it — this is the strictest palette in the
library and the reason the type reads as technical rather than decorative.

**Borrowed from types that have been rendered**, so the same faults are not paid for twice:
`verdict` badges drift to outline rings unless the FILLED DISC is named (2 of 6 renders on
`02-cause-anatomy`); exact counts drift unless the mark names ONE bounded structure rather
than repeating a number; and a mark placed where nothing is claimed to be wrong reads as the
product causing harm (`02-symptom-rail` 1.7).

## SLOT CONSTRAINTS
- **The prompt budget** (ADR-013): a clause earns its place in a rendered prompt only if a
  render has failed without it. Everything else is a rule for the writer and stays here. This
  type has no renders yet, so its prompts start from the skeleton and nothing more.
- The product is the ONLY object with a real material finish.
- `cutaway` lives inside the silhouette, never floating on top.
- G7 exempt: technical-render register, so context integrity does not bind — the product need
  not be mounted to anything real.
- The canonical NEGATIVE below is model-agnostic and is never pasted into a prompt verbatim;
  the adapter transforms it (Rule 1), and most of its tokens qualify nouns a prompt requires.

## NEGATIVE
```
[G6] + human face, facial features, hair, skin tone, clothing,
photographic background, environment, furniture, shadows on floor,
extra colors, rainbow palette, anatomically wrong structures,
floating disconnected organs, dimension lines overlapping product edge,
cluttered inset, gore, realistic flesh, medical horror
```

## WORKED EXAMPLES
### example: mouth-tape — skeleton@1.0, run: untested
Product: mouth tape · ratio 1:1 · xcheck enabled, dims dropped
- GHOST — head and upper chest in profile, lying back as if asleep, cut on the sagittal plane
- CUTAWAY — nasal cavity, soft palate, tongue and throat inside the head silhouette
- PRODUCT — one horizontal strip of tape across the closed lips
- MARKS — `structure` (tissue in ivory), `support` (blue airflow from nostril down the
  throat), `stress` (red at the collapsed area behind the tongue), `verdict` in the inset
Stale in one way to fix when it is next rendered: it predates the G2 rewrite and its PRODUCT
paragraph still describes texture, which `product` now forbids.

## KNOWN-FLAKY
(nothing observed — this type has never been rendered)

## NOTES
Step 3 has three types answering three different questions, and a gallery rarely needs more
than one or two: `ghostbody` = "why does this shape work", `03-spec-split` = "what is better
inside", `03-use-sequence` = "can I operate it".

Distinction from `02-cause-anatomy`: that type is a 2D illustration indicting a CULPRIT in
the customer's life, and its sentence is "this is what harms you". This one is a 3D render of
the product's own mechanism, and its sentence is "this shape exists for a reason". They may
run in one gallery (02 then 03) but must share one palette or they read as two sources.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.3 (2026-08-13): restructured into a call-map plus PARTS and MARKS (ADR-012). `PARTS`
  holds register, ghost, cutaway, product and xcheck; `MARKS` names the four palette-lock
  colours as marks for the first time, plus `dims` and `verdict`. The `RATIO:` line dropped
  per adapter Rule 4, which 6 of 6 renders showed a written ratio does nothing. Every mark
  carries **none** for evidence, because this type has never been rendered.
- 1.2 (2026-08-11): channels gain `landing-page` and `advertorial`, for parity with
  `03-mechanism-xray` — two mechanism types answering the same question on different channel
  sets was an accident, not a decision.
- 1.1 (2026-08-10): PRODUCT slot rewritten to G1 reference + G2 placement-only; `dims` gated
  to products with a clear 3D volume. seed: conversation.md.
- 1.0 (2026-08-10): initial as SQR-MECH-GHOSTBODY from the seat-cushion spine exemplar;
  exemplar faults noted (numberless dims as decoration, inset too small for mobile, extension
  lines crossing the product edge). seed: conversation.md.

---
id: 05-social-handoff
step: 5
job: social
device: handoff
version: "1.2"
status: active
replaced_by: null
ratios: ["16:9", "1:1", "3:4"]
channels: [paid-social, advertorial, landing-page]
requires_product_photo: true
generation_mode: multi-pass
variants: []
exempt_from: [G3, G4]
pairs_with: [04-proof-lockedframe, 06-relief-hero]
never_with: []
avoid_adjacent: [05-persona-grid]
---

# 05-social-handoff

## PURPOSE
Staged word-of-mouth: an advocate points, a faceless listener follows the gesture, and
we happen to witness it. Social proof that clears the skepticism barrier a
straight-to-camera testimonial cannot.

## TRIGGER
use_when: >
  Need social proof without a face-to-camera testimonial. The "a friend told
  me" beat mid-advertorial, cold-ads creative, or a closing image on a landing
  page. Fits products people genuinely recommend to each other out loud.
avoid_when: >
  Marketplace galleries and main images. Not for private products nobody
  recommends in person. Not when no natural reason exists for two people to
  stand near the product. Keep distance from 05-persona-grid on the same page
  (same question, different mechanism).

## SKELETON
A call-map. Each arrow names an entry in PARTS; the definition lives there once.
**No MARKS section:** no arrow, no badge, no connecting line. The pointing arm IS the arrow,
and drawing one on top says the gesture failed.

```
TYPE: 05-social-handoff v1.2

[PRODUCT REFERENCE] attached photo is the exact reference.
[ADVOCATE] face to camera, mid-sentence, pointing.        -> PARTS/advocate
[LISTENER] face NOT visible, following the gesture.       -> PARTS/listener
[PRODUCT] where the pointing line terminates.             -> PARTS/product
[INSET] optional, and unavailable without compositing.    -> PARTS/inset
[ENVIRONMENT] a real reason for two people to be here.    -> PARTS/environment
[COMPOSITION] two vectors converge on the product.        -> PARTS/composition

REGISTER: candid documentary photograph, natural, unposed, sharp.
```

## PARTS

**`advocate`** — [age/gender] in ordinary specific wardrobe, face turned toward camera,
mid-sentence, warm and relaxed, pointing at the product. **The gesture forms a clear diagonal
ending exactly at the product**, and it is the compositional spine: take the gesture away and
the product disappears from the frame.

**Both hands empty.** No mug, no bag, no tool, and never the product itself. An arm given a job
renders the job and drops the gesture — 2 of 3 founding renders lost the pointing arm entirely
that way, and the third, whose advocate carried nothing, drew a clean diagonal onto the product.
The prop is concrete and the vector is a relationship, so the model keeps the prop. Catalogued
as `registry/argument-faults.md` A12.

**`listener`** — [age/gender], seen from behind or in profile, **face NOT visible**, head
turned to follow the gesture, gaze parallel to the pointing line. The turned back is an empty
seat for the viewer's identity, and **both faces visible kills the mechanism**.

**`product`** — the reference product at a natural location, partially framed by a foreground
element, sitting exactly where the pointing line terminates.

*Proposal, 3 renders, still untested:* an in-scene floor of **≥8% of frame height**. The
founding exemplar's own predicted failure was a product seen through a doorway shrinking to
unrecognisable pixels, which voids the pointing line — a gesture ending at nothing. All three
founding renders cleared the floor comfortably (roughly 10%, 20% and 35% of frame height by
inspection) and all three products were readable, so nothing has yet run below it. It stays
until a render does without it (ADR-015).

**`inset`** — a circular white cutout of the product on plain white, near the terminus of the
pointing line and **never opposite it**, at 15-20% of frame width, clean edge, no border, no
connecting arrow.

**Include it ONLY if the scene cannot show the product clearly — and it needs compositing, so
where the renderer cannot composite it is unavailable.** G1 applies TWICE when it is used and
the colourway must match exactly; the founding exemplar failed on that alone, beige in scene
and charcoal in inset, which reads as two products. The safer route is to choose a moment
where the scene carries the product, and skip the inset entirely.

**`environment`** — a specific place **directly related to the moment of use**, with 2-3
incidental background people or details, flat natural daylight, nothing styled. **It must give
a natural reason for two people to be standing near the product** — G7's third test, and the
founding exemplar's documented miss was an airport pickup framed around a car seat.

**`composition`** — the pointing arm and the listener's gaze are two vectors and both converge
on the product. Nothing else in the frame competes.

## SLOT CONSTRAINTS
- G3 and G4 are exempt: this type carries no signal colour and ranks nothing.
- **The prompt budget, four parts.** A clause reaches a rendered prompt only if a render has
  failed without it, THAT product can fail that way, the model can act on it inside one
  generation, and it is stated once. Ceiling **1800 characters**. Since ADR-014 no
  `Strictly avoid:` line is rendered.

## NEGATIVE
```
[G6] + arrows, badges, connecting lines, both faces visible,
listener facing camera, product color mismatch between scene and inset,
two different products, inset placed opposite the pointing direction,
product outside the pointing line, staged posing, direct eye contact with camera,
studio lighting, empty background, unrelated location
```
Canonical and model-agnostic. Since ADR-014 it is not rendered into the prompt.

## KNOWN-FLAKY
- **The listener's head turns away from the product when the product sits across the frame from
  the listener.** 1 of 3 (2026-08-14, burr coffee grinder). `face NOT visible` and `gaze
  parallel to the pointing line` were in direct conflict for that geometry — turning to the
  product would have brought the face round toward camera — and the model kept the face hidden.
  Both other renders held both clauses, so nothing is patched. Untested hypothesis: place the
  product deeper in the frame than the listener, so hiding the face and looking at the product
  become one instruction instead of two competing ones.
- **The advocate turns to face the listener instead of the camera.** 1 of 3 (2026-08-14,
  cordless leaf blower), in the one render where both hands were on the product. May be a
  symptom of the hands fault rather than a fault of its own.

## CHANGELOG
- 1.2 (2026-08-14): **first renders this type has ever had** — 3 products, verdicts fail /
  partial / fail (render ledger, ts 2026-08-14). `PARTS/advocate` gains **both hands empty**:
  2 of 3 renders dropped the pointing arm because a hand was holding something (two mugs; the
  product itself), and the one with free hands drew a clean diagonal onto it. Catalogued as
  `argument-faults.md` A12. `ratios` corrected to ADR-016's legal set, `1:1` added on 3 of 3
  render evidence. Listener geometry and the 8% floor stay unpatched at 1 of 3 and 0 of 3.
  `27f19e3`
- 1.1 (2026-08-14): **restructured into a call-map plus PARTS** (ADR-012). `PARTS` owns
  `advocate`, `listener`, `product`, `inset`, `environment`, `composition`. **No MARKS
  section** — the pointing arm IS the arrow. `RATIO:` dropped per adapter Rule 4. Carried in
  from `04-proof-lockedframe`: the **capability gate** — the inset needs compositing, so where
  the renderer cannot composite it is unavailable and the scene must carry the product, which
  makes this type single-pass in practice. The exemplar's ≥8% floor stays a proposal.
- 1.0 (2026-08-10): initial from the airport / car-seat pointing exemplar; exemplar
  faults encoded (inset colorway mismatch, inset far from the pointing terminus,
  location unrelated to the use moment). seed: conversation.md.

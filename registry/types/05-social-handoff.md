---
id: 05-social-handoff
step: 5
job: social
device: handoff
version: "2.0"
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
Witnessed word-of-mouth: two people are dealing with something the product has just done, one
of them faceless, and we happen to see it. Social proof that clears the skepticism barrier a
straight-to-camera testimonial cannot.

## TRIGGER
use_when: >
  Need social proof without a face-to-camera testimonial. The "a friend told
  me" beat mid-advertorial, cold-ads creative, or a closing image on a landing
  page. Fits products people genuinely recommend to each other out loud, and
  whose effect is visible in the room afterwards.
avoid_when: >
  Marketplace galleries and main images. Not for private products nobody
  recommends in person. Not where the product leaves no visible trace, because
  the two people then have nothing to be dealing with. Keep distance from
  05-persona-grid on the same page (same question, different mechanism), and
  send a solo step-by-step demonstration to 03-use-sequence instead.

## SKELETON
A call-map. Each arrow names an entry in PARTS; the definition lives there once and is
expanded into the rendered prompt (SPEC §3.3).

```
TYPE: 05-social-handoff v2.0

[PRODUCT REFERENCE] attached photo is the exact reference.
[MOMENT] what the product just did, visible in frame.     -> PARTS/moment
[ADVOCATE] using it or a second past it, face to camera.  -> PARTS/advocate
[LISTENER] face NOT visible, attention on the moment.     -> PARTS/listener
[PRODUCT] dominant, and nothing beside it competes.       -> PARTS/product
[INSET] optional, and unavailable without compositing.    -> PARTS/inset
[ENVIRONMENT] a real reason both people are here.         -> PARTS/environment

REGISTER: candid documentary photograph, natural, unposed, sharp.
```

## PARTS

**`moment`** — one thing in frame is different **because of the product**, and it is what both
people are dealing with. A strip of floor done and the rest not; the cup that was just made,
in the listener's hands; a path cleared to one side of a line. **This is the type's spine.**
Without it the two have no reason to be talking about the product now, and the frame renders as
two people standing near an appliance — 3 of 3 founding renders, owner verdict.

The moment is a RESULT, never a demonstration. G9's ranking decides which to use: the result
itself beats residue, residue beats the tool still in hand, and gesture alone is the weakest.

**`advocate`** — [age/gender] in ordinary specific wardrobe, face turned toward camera,
mid-sentence, warm and relaxed. **Hands on the product or a second off it** — they have just
this moment finished using it and the posture says so.

**Never pointing at it from across the room.** A person does not point at their own appliance
mid-conversation; the gesture is itself the staging. The one founding render whose pointing arm
drew perfectly — extended, straight, landing on the product — still read as posed, which is what
retires the mechanism rather than repairing it.

**`listener`** — [age/gender], seen from behind or in profile, **face NOT visible**, attention on
the moment rather than on the advocate. The turned back is an empty seat for the viewer's
identity, and **both faces visible kills the mechanism**. Held on 2 of 3 founding renders.

**`product`** — the reference product where it is genuinely used, and **dominant**: the largest,
sharpest and best-lit man-made object in frame, with clear space around it.

**Nothing of similar size, finish or family stands near it.** A kettle beside a coffee grinder,
both brushed silver, both the same size, leaves the frame unreadable — a viewer cannot tell
which object is being sold. Owner verdict, and the fault the type had no law against.

*Retired, 3 renders:* a bare floor of ≥8% of frame height. All three renders cleared it and not
one of the three products stood out, so the floor was measuring readability while the type
needed dominance.

**`inset`** — a circular white cutout of the product on plain white, near the moment and at
15-20% of frame width, clean edge, no border, no connecting arrow.

**Include it ONLY if the scene cannot show the product clearly — and it needs compositing, so
where the renderer cannot composite it is unavailable.** G1 applies TWICE when it is used and
the colourway must match exactly; the founding exemplar failed on that alone, beige in scene and
charcoal in inset, which reads as two products. The safer route is to choose a moment where the
scene carries the product, and skip the inset entirely.

**`environment`** — a specific place **directly related to the moment of use**, flat natural
daylight, nothing styled. **It must give a natural reason for both people to be there** — G7's
third test, and the founding exemplar's documented miss was an airport pickup framed around a
car seat.

**Incidental detail only survives if it would survive the product being used.** A child's book
lying on a rug out-read a robot vacuum for contrast and made the machine's own operation
impossible in the same frame; clutter written in for candour argued against the product instead.

## SLOT CONSTRAINTS
- G3 and G4 are exempt: this type carries no signal colour and ranks nothing.
- **No MARKS section, and the reason has changed.** It is not that the pointing arm was the
  arrow — that mechanism is retired. It is that the register is candid documentary and its
  credibility IS the argument: a drawn arrow or badge on it reads as an advertisement, which is
  the objection this type exists to clear (A11 — register decides). Where a page needs the
  product flagged, the route is a `--marked` variant on `01-pain-scene`'s precedent, a CHOICE
  and never a default. Unbuilt until the base passes.
- **The prompt budget, four parts.** A clause reaches a rendered prompt only if a render has
  failed without it, THAT product can fail that way, the model can act on it inside one
  generation, and it is stated once. Ceiling **1800 characters**. Since ADR-014 no
  `Strictly avoid:` line is rendered.

## NEGATIVE
```
[G6] + arrows, badges, connecting lines, both faces visible,
listener facing camera, product color mismatch between scene and inset,
two different products, a second appliance of similar size or finish beside the product,
product held up or presented toward the viewer, product untouched and unused,
staged posing, pointing at the product from a distance,
direct eye contact with camera, studio lighting, empty background, unrelated location
```
Canonical and model-agnostic. Since ADR-014 it is not rendered into the prompt.

## KNOWN-FLAKY
- **The listener's head turns away from the product when the product sits across the frame from
  the listener.** 1 of 3 (2026-08-14, burr coffee grinder). `face NOT visible` and the gaze
  clause were in direct conflict for that geometry — turning to look would have brought the face
  round toward camera — and the model kept the face hidden. Carried into 2.0 unpatched: under
  `moment` the listener has a result to attend to rather than a direction to match, which may
  dissolve it without a rule.
- **The advocate turns to face the listener instead of the camera.** 1 of 3 (2026-08-14,
  cordless leaf blower), in the render where both hands were on the product. 2.0 puts hands back
  on the product deliberately, so this one is worth watching.

## CHANGELOG
- 2.0 (2026-08-14): **MAJOR — the spine moves from a gesture to a result.** Owner verdict on all
  3 founding renders: the product does not stand out, and neither interaction is real. New
  `PARTS/moment` — something in frame is different because of the product and both people are
  dealing with THAT. `advocate` retires pointing and puts hands back on the product; `product`
  gains a dominance law and a no-decoy rule; the ≥8% floor is retired as the wrong instrument.
  Decisive: the grinder render, whose gesture drew perfectly and still read as staged.
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

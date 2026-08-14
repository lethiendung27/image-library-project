---
id: 05-social-handoff
step: 5
job: social
device: handoff
version: "2.5"
status: active
replaced_by: null
ratios: ["16:9", "1:1", "3:4"]
channels: [paid-social, advertorial, landing-page]
requires_product_photo: true
generation_mode: multi-pass
variants: [marked]
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
  recommends in person. Not where the product leaves no visible trace, and not
  where its only trace is a change of texture — crease, nap, sheen — which
  cannot be seen quickly. Keep distance from 05-persona-grid on the same page
  (same question, different mechanism), and send a solo step-by-step
  demonstration to 03-use-sequence instead.

## SKELETON
A call-map. Each arrow names an entry in PARTS; the definition lives there once and is
expanded into the rendered prompt (SPEC §3.3).

```
TYPE: 05-social-handoff v2.5 [--marked]

[PRODUCT REFERENCE] attached photo is the exact reference.
[MOMENT] what the product just did, visible in frame.     -> PARTS/moment
[ADVOCATE] just used it, eyes on the listener.            -> PARTS/advocate
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

**Where the moment is a boundary, it lies on ONE continuous surface with the product on it.**
Two panes, two cushions, two of anything are two objects and nothing turns one into the other —
`argument-faults.md` A8, now observed here too: 2 of 4 renders lost the argument to a dividing
frame or a gap.

**The difference must be one of tone or colour, never of texture.** Crease, nap, pile, sheen,
softness — texture falls under the threshold at which a difference survives a quick look (A7). A
steamed curtain rendered with no boundary at all, while frost, a stain and a cut line all
rendered. A product whose only result is a texture does not belong in this type.

**`advocate`** — [age/gender] in ordinary specific wardrobe, mid-sentence, warm and relaxed.
**Hands on the product, and a second AFTER the stroke rather than inside it.** Mid-action the
eyes go to the work instead of to the listener — 2 of 4 renders, both written as *at the end of
a stroke*, which the model reads as mid-stroke.

**Eyes on the listener, never on the lens.** The listener stands BETWEEN the advocate and the
camera, so the face reads to us over a turned shoulder while the look stays inside the scene.
A glance down the lens makes a presenter and the frame an advertisement — 2 of 3 renders did it,
and `NEGATIVE` had banned it since 1.0 while this entry ordered it.

**Never pointing at it from across the room.** A person does not point at their own appliance
mid-conversation; the gesture is itself the staging.

**`listener`** — [age/gender], seen from behind or in profile, **face NOT visible**, attention on
the moment rather than on the advocate. The turned back is an empty seat for the viewer's
identity, and **both faces visible kills the mechanism**. Held on 2 of 3 founding renders.

**`product`** — the reference product where it is genuinely used, and **dominant at any size**.
Dominance is not bulk: a handheld tool cannot be the biggest thing in a room and must still
command the frame. Four instruments, all of them the register's own — the product is the only
thing in sharp focus and everything behind it is softer; it carries the strongest light in the
frame; nothing overlaps or crowds it; and **it differs from everything else in frame** — floor,
walls and what the people are wearing included. **Separate by HUE where the product has one, by
value only where it does not**: all 3 products found at a glance separated by hue, two of them
near-complementary, while the one separating by value alone was the weakest read of its set.

**Nothing of similar size, finish or family stands near it.** A kettle beside a coffee grinder,
both brushed silver, both the same size, leaves the frame unreadable — a viewer cannot tell
which object is being sold. Owner verdict, and the fault the type had no law against.

*Retired, 3 renders:* a bare floor of ≥8% of frame height — it measured readability, not
dominance.

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

**Never name a light fixture.** Describe light by quality and direction, never by the lamp
making it: a named source becomes the brightest object in frame and takes the role `product`
was given. `one warm ceiling light` beat the dominance clause inside the same prompt.

## SLOT CONSTRAINTS
- G3 and G4 are exempt: this type carries no signal colour and ranks nothing.
- **The base carries no mark.** The register is candid documentary and its credibility IS the
  argument: a drawn arrow or badge on it reads as an advertisement, which is the objection this
  type exists to clear (A11 — register decides). `--marked` is the sanctioned exception, a CHOICE
  and never a default, on `01-pain-scene`'s precedent.
- **The prompt budget, four parts.** A clause reaches a rendered prompt only if a render has
  failed without it, THAT product can fail that way, the model can act on it inside one
  generation, and it is stated once. Ceiling **1800 characters**. Since ADR-014 no
  `Strictly avoid:` line is rendered.

## VARIANTS

### --marked
Diff only; everything else is the base.

**`[MARK]`** — a thin drawn line lying along the boundary `moment` names, following it exactly,
neutral white, and **the only drawn element in the frame**. Stated that way and never as a
number, because a count has never bound this model.

It marks the **boundary, never the product**. 3 of 4 v2.3 renders found the product at a glance
with nothing drawn on it, so a mark there would solve a solved problem and spend the candid
register for nothing. What a scrolling reader misses is what CHANGED: a half-lifted stain read
as an intact stain. Neutral white rather than a signal colour, because this type is `G3`-exempt
and ranks nothing — importing red or blue would import a meaning it does not carry.

**Legal on landing-page and advertorial only**; paid social keeps the plain candid, where the
absence of any graphic is the credibility. Untested, 0 renders.

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

## WORKED EXAMPLES
Both rendered at 2.3 and kept in FULL text, because that text is the only record of what
actually rendered — the ledger stores verdicts, not prompts (SPEC §3.3). Both predate 2.4, so
neither carries the hue-first wording, the tone-not-texture rule or the after-the-stroke
posture. **They are records, not templates. Current law is in PARTS; fill from there.**

### example: carpet-spot-cleaner — skeleton@2.3, run: partial
The closest this type has come. `advocate` satisfied in full — he is kneeling back from the
machine with both hands still on it and his eyes on her, because the posture is at rest. The
only saturated object in a beige room. Failure: the spill read as intact rather than half
lifted, so only one side of the boundary carried evidence.
```
TYPE: 05-social-handoff v2.3
REGISTER: candid documentary photograph, natural, unposed, sharp. One scene, no inset.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the carpet spot cleaner. Preserve its
shape, proportions, material, finish and colour exactly.

[MOMENT]
One carpet, half of a dark spill lifted. A patch of the pile has come back to its own colour
and the rest of the mark is still there, and the edge between them sits on one continuous
stretch of carpet where the head stopped. Both people are dealing with that edge.

[ADVOCATE]
Man in his 30s in a dark t-shirt, kneeling on the floor with both hands still on the
reference cleaner where he has just stopped pulling. Mid-sentence, relieved and slightly
smug, his eyes on the woman and never on the camera.

[LISTENER]
Woman in her 30s in a deep green jumper crouching beside him, between him and the camera
with her back to us, FACE NOT VISIBLE, head down to the lifted patch.

[PRODUCT]
The reference cleaner is the only thing in sharp focus, everything behind it softer. It
carries the strongest light in the frame, nothing overlaps or crowds it, and it differs in
hue or value from everything else in frame. Nothing of similar size or finish stands near it.

[ENVIRONMENT]
An ordinary living room in the afternoon, an armchair pushed back against the wall and a dog
lead dropped by the door. Directional daylight raking in low from a window off to one side,
nothing styled.
```

### example: ice-scraper — skeleton@2.3, run: partial
The crispest boundary the type has produced, and the proof that dominance is not size: the
smallest product in any set is found first, because blue against white frost and dark glass
separates by hue and value at once. Failure: written as *at the end of a stroke*, which the
model read as mid-stroke, so her eyes stayed on the work instead of reaching the listener.
```
TYPE: 05-social-handoff v2.3
REGISTER: candid documentary photograph, natural, unposed, sharp. One scene, no inset.

[PRODUCT REFERENCE]
Use the attached photo as the exact reference for the ice scraper. Preserve its shape,
proportions, material, finish and colour exactly.

[MOMENT]
One windscreen, half done. A wide swathe has been scraped down to clear dark glass and the
rest is still under thick white frost, and the edge between the two runs across one
continuous pane where the blade stopped. Both people are dealing with that edge.

[ADVOCATE]
Woman in her 40s in a padded coat and gloves, leaning over the bonnet with the reference
scraper still flat against the glass at the end of a stroke. Mid-sentence, breath showing in
the cold, pleased with herself, her eyes on the man and never on the camera.

[LISTENER]
Man in his 30s in a dark overcoat holding a travel mug, standing between her and the camera
with his back to us, FACE NOT VISIBLE, head down to the cleared glass.

[PRODUCT]
The reference scraper is the only thing in sharp focus, everything behind it softer. It
carries the strongest light in the frame, nothing overlaps or crowds it, and it differs in
hue or value from everything else in frame. Nothing of similar size or finish stands near it.

[ENVIRONMENT]
A suburban driveway just after dawn in hard frost: a wheelie bin, a whitened hedge, another
car further down the road. Flat cold daylight from a low overcast sky, nothing styled.
```

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 2.5 (2026-08-14): **type passed by the owner; file finalised.** Two `WORKED EXAMPLES` added,
  both at skeleton@2.3 and both `run: partial`, kept in full text as the only record of what
  actually rendered (SPEC §3.3) and labelled records rather than templates. The type arrived
  here from 1.0 with zero renders and one founding exemplar; 15 renders across 5 versions
  retired the pointing mechanism, moved the spine to a visible result, and taught the product to
  separate from the whole frame. `--marked` ships untested and is a choice, never a default.
  `5fbea1d`
- 2.4 (2026-08-14): **`--marked` added, marking the boundary rather than the product.** The 2.3
  dominance fix worked — 3 of 4 find the product at a glance with nothing drawn on it — so the
  gap left is the RESULT. One neutral white line along the boundary, landing-page and advertorial
  only. Base sharpened by the same renders: `product` separates by HUE first, value only as
  fallback; `moment` must differ in tone or colour, never texture (A7), which `avoid_when` now
  screens on; `advocate` is a second AFTER the stroke, since mid-action the eyes go to the work.
  `de17866`
- 2.3 (2026-08-14): **the product must differ from the whole frame, not from the surface behind
  it.** 2.2 renders: eyes off the lens and listener geometry landed 4 of 4, uncovering the next
  fault — the product vanished in 3 of 4, each into a scene built from its own colour.
  `PARTS/product` dominance now binds against everything in frame, clothing included.
  `PARTS/environment` gains **never name a light fixture** — `one warm ceiling light` beat the
  dominance clause inside one prompt. `PARTS/moment` cites A8: a boundary lies on ONE continuous
  surface, 2 of 4. `a19381a`
- 2.2 (2026-08-14): **the advocate looks at the listener, not at the lens.** Owner finding on the
  v1.2 set: 2 of 3 stared down the lens and read as presenters; the third disobeyed a prompt
  ordering face-to-camera and gave this type's best frame. `NEGATIVE` had banned lens contact
  since 1.0, so `PARTS/advocate` and the skeleton were contradicting the same file. The law is
  geometric: the listener stands between the advocate and the camera. Both KNOWN-FLAKY entries
  deleted — the geometry one resolved by the pram render, the other now the required behaviour.
  `ca86229`
- 2.1 (2026-08-14): `PARTS/product`'s dominance law was **unachievable as written**. "The largest
  man-made object in frame" cannot be met by a handheld tool in a room, and a model asked for it
  either ignores the clause or distorts the product's scale — the reference photo governs scale
  under G1/G2, so a size instruction fights it. Dominance is now four register-native
  instruments: sole sharp focus, strongest light, nothing overlapping, value separation behind.
  Caught while writing the first 2.0 prompt set, before any render.
- 2.0 (2026-08-14): **MAJOR — the spine moves from a gesture to a result.** Owner verdict on all
  3 founding renders: the product does not stand out, and neither interaction is real. New
  `PARTS/moment` — something in frame is different because of the product and both people are
  dealing with THAT. `advocate` retires pointing and puts hands back on the product; `product`
  gains a dominance law and a no-decoy rule; the ≥8% floor is retired as the wrong instrument.
  Decisive: the grinder render, whose gesture drew perfectly and still read as staged. `2d04cc9`
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

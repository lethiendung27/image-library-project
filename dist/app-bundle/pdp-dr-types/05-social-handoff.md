---
id: 05-social-handoff
step: 5
job: social
device: handoff
version: "2.9"
status: active
replaced_by: null
channels: [paid-social, advertorial, landing-page]
requires_product_photo: true
generation_mode: single-pass
variants: [marked]
exempt_from: [G3, G4]
pairs_with: [04-proof-lockedframe, 06-relief-hero]
never_with: []
avoid_adjacent: [05-persona-grid]
copied_from: 05-social-handoff
copied_at_version: "2.9"
blocked_by: null
---

# 05-social-handoff

## PURPOSE
Witnessed word-of-mouth: two people are dealing with something the product has just done, one
of them faceless, and we happen to see it. Social proof that clears the skepticism barrier a
straight-to-camera testimonial cannot.

**Copied verbatim from `registry/types/05-social-handoff.md` at version 2.9** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## TRIGGER
use_when: >
  Need social proof without a face-to-camera testimonial. The "a friend told
  me" beat mid-advertorial, cold-ads creative, or a closing image on a landing
  page. Fits products people genuinely recommend to each other out loud, and
  whose effect is visible in the room afterwards.

## SKELETON
A call-map. Each arrow names an entry in PARTS; the definition lives there once and is
expanded into the rendered prompt (SPEC §3.3).

```
TYPE: 05-social-handoff v2.9 [--marked]

[PRODUCT REFERENCE] attached photo is the exact reference.
[MOMENT] what the product just did, visible in frame.     -> PARTS/moment
[ADVOCATE] just used it, eyes on the listener.            -> PARTS/advocate
[LISTENER] face NOT visible, attention on the moment.     -> PARTS/listener
[PRODUCT] dominant, and nothing beside it competes.       -> PARTS/product
[HANDOFF] what passes between them. Required.             -> PARTS/handoff
[INSET] optional. Model-drawn, single-pass.               -> PARTS/inset
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

**`handoff`** — [what passes between the two people], and it is REQUIRED. Not a gaze: an act.

`advocate` and `listener` legislate two EYE DIRECTIONS and nothing else, and four renders obeyed
both exactly while the owner read no story in any of them. The word handoff was in this type's
name and in none of its slots. Nothing was being handed over because nothing asked for it.

Four forms. Choose one and name it:

- `offer` — the product spans the gap, still in the advocate's hand and already touched by the
  listener's.
- `take` — the listener's own hand is on the product, or on the thing the product just changed.
- `point` — the advocate's free hand rests ON the moment, not near it, and the listener's head
  is turned to follow it.
- `show` — the advocate has turned one named part of the product toward the listener and holds
  it there.

**The act must be a STATE a still frame can hold, never a movement in progress.** Two hands on
one object reads; one hand reaching toward an object does not, because a still cannot say whether
it is arriving or leaving. This is `01-pain-scene`'s finding borrowed rather than paid for twice:
an arm "stalled at the height it will not pass" came back as an ordinary reach, and a turn
"arrested mid-way" came back as no turn at all.

**`inset`** — a cutout of the product on plain white, near the moment, clean edge, no border, no
connecting line.

**It is MODEL-DRAWN and single-pass, confirmed 4 of 4 at 2.6.** The compositing requirement is
withdrawn: it rested on the founding exemplar's failure — *beige in scene and charcoal in inset,
which reads as two products* — and that is a colourway mismatch a clause binds, exactly as
`06-relief-hero` binds it. Say it in the prompt, in these words:

> the inset shows THE SAME single product that is in the scene — one object photographed twice in
> one frame. Identical colourway, identical finish, identical wear, lit by the same light as the
> scene. Never a second unit, never a different colour or material.

Held 4 of 4, and beyond its own terms: a two-tone unit reproduced the same dirty water at the
same level in the same two chambers, so it bound product STATE and not only colour, and a
metallic unit matched on FINISH rather than on hue.

**Shape and proportion are free.** Circle, square or rectangle at 1:1, 3:4, 4:5 or wider —
four distinct shapes rendered as asked, 4 of 4. The inset's own proportion is not the FRAME's
ratio, which ADR-016 still governs.

**PLACE IT BY THE MOMENT, NEVER BY A CORNER.** Naming a corner is what went wrong: a corner is a
position and the inset needs a RELATIONSHIP. Four renders, and the three that misplaced were all
placed by corner — one panel landed over the listener's head, one butted two frame edges at once,
and the worst went to the lower left while its product hung upper right and its moment ran across
the centre, the one region of the picture holding neither. Write it as **the quiet ground
immediately beside the moment**, and add what it must not cover: **never over a face, never over
the product, and never touching a frame edge.**

**SIZE IS NOT A NUMBER HERE — IT IS G10's MAXIMISATION CLAUSE.** Two fixed bounds failed in
consecutive versions: 2.6 bound the panel, 2.7 bound the product inside it, and panels then
rendered between 16.6% and 31.1% of frame width while several still read as too small. Make the
inset **as large and as clear as it can be**, growing until it would cover INFORMATION — the
moment, or a face — or breach G10's safe area. **The product must FILL its panel and is never
smaller than a quarter of the frame width**, which is G10's floor: a circle whose product filled
the disc read at 25.4% while a compliant 16.6% rectangle carried a sliver between margins.

**BOTH placement conditions bind, and each render so far has honoured one.** Quiet ground AND
beside the moment. One inset found quiet ground and ran off the left edge; another found quiet
ground diagonally opposite its moment. Neither is placed.

**G1 applies TWICE when it is used.** Include it where the scene cannot show the product whole —
the strongest case rendered so far is a drain snake down a plughole, where only the handle exists
in the scene. Where the scene already carries the product, skip it.

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

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 2.9 (2026-09-15): copied verbatim from `registry/types/05-social-handoff.md` at 2.9, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.

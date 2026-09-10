# Test prompts — round 2, six renders, three types

Ratio **1:1**, set at the tool. It never goes in the prompt (ADR-016, adapter Rule 4).
**Attach the product photo** where a prompt opens with PRODUCT REFERENCE.

**Six NEW products.** Every one comes from `query/product-slugs.yaml`, none appears in any
candidate's source list, and **none is a product the founding round used**. Re-running the
same six to A/B a fix would test whether a clause works on a product it has already seen,
which is the one thing it cannot tell us.

## What this round tests, and why each clause changed

The owner's audit of the founding round: the prompts choose colour badly and the badges are
still not as rich as the corpus's. Both were measured before anything was rewritten.

| finding | measured | what changed here |
|---|---|---|
| the ground is too loud | corpus ground value median **0.89** and saturation **0.06** across 119 direct-response frames; the six renders **0.46** and **0.38**, with 5 of 6 darker than 0.70 | five of six grounds are now LIGHT and near-neutral. One stays dark and the prompt says why |
| the badge is flat | value spread inside the badge fill: renders 0.06 0.09 0.03 0.31 0.02 0.03 — **5 of 6 dead flat**; four corpus badges 0.12 0.35 0.16 0.10 | every badge carries an internal tone step — a ring, a rim, an inset outline — and **two type sizes** |
| the badge borrows the product's colour | 3 of 6 shared the product's dominant hue; corpus 1 of 4 | every badge hue is checked against the product and the ground before it is written |
| the size anchor does nothing to type | headline ÷ its named anchor: 0.24 0.23 0.13 0.45 0.64, never 1.0, and the ratios run backwards | **the anchor clause is gone from the headline.** Size is now written as FILL — the instrument this library has actually measured working |
| the watermark abuts a callout | 2 of 2 frames with a callout in the lower right | nothing the prompt asks for goes in the lower right, callouts included |
| the corner ribbon cannot honour G10 | ink at 0.00% of two edges, 1 of 1 | no `flash` form in this round |

**Why FILL replaces the anchor.** Three fixed numbers and one anchor have now failed at
sizing text here. What has not failed is the fill rule: a block told to fill the area it is
given fills it, and a block that leaves the area half empty gets drawn twice (G16, round 2,
measured 5 clusters against 2). So the headline is sized by what it must fill, not by what
it must match.

**Length, measured off this file rather than claimed.** 1533–1681 characters against adapter
Rule 6's 1450–1600 reference; 2 of 6 inside it. The founding round ran 1430–1707, so the top
came down and the floor rose. The rise is accounted for: the BADGE block went from a mean of
192 characters to 250, **+58 per prompt**, and that is what the interior spec costs. It is
spent knowingly — a flat one-word stamp is 58 characters cheaper and it is the thing being
fixed. If the next round says the interiors held and the prompts still read long, the saving
comes out of the CALLOUTS list, not out of the badge.

The copy is **drafted, not any page's own** — there is no `content.json` for these — so it
claims only what each object's facts support and carries no figure, no percentage and no
timeframe. Badges carry no numbers for the same reason (`argument-faults.md` A15).

---

## 1 — `03-spec-callout` · cord and rope tightening tool · badge `chip` · pale grey ground

```
TYPE: 03-spec-callout v0.3
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the cord and rope tightening
tool. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: the tool slightly left of centre, a short pale rope threaded through it and running
out both sides, turned so the cam, the release lever and the rope channel all show. Half the
picture's width.

SETTING: a pale warm grey ground, almost colourless, empty on all sides.

LIGHT: broad and frontal; no part of the tool falls into shadow.

CALLOUTS: four charcoal sans-serif labels on the empty ground, each joined to its part by one
thin charcoal line. Nothing sits in the lower right:
the cam — Bites down the moment you let go
the release lever — One thumb and the rope is free
the rope channel — Takes the rope already in your boot
the body — Small enough to live in a door pocket

TEXT: across the top, two lines of charcoal sans-serif, each beginning the same distance from
the left edge as the leftmost label. The two lines fill that band margin to margin and are
the largest text here:
TIGHT STAYS TIGHT
ALL THE WAY HOME
Each callout label is half the height of those capitals.

BADGE: UPPER RIGHT, as wide as the tool's body is long. A filled circle in deep signal blue
with a narrow white ring inset inside its edge; a white line padlock icon in the upper half,
HOLDS in large white capitals under it, UNDER LOAD in small white capitals under that.

Nothing comes within a tenth of the width of any edge. These are the only words in the
picture; no logo, no watermark, no person, no room.
```

---

## 2 — `03-spec-callout` · 7-in-1 external drive · six labels · badge `roundel` · pale blue ground

Six labels again, because six held. What is new is the interior of the badge and the ground.

```
TYPE: 03-spec-callout v0.3
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the 7-in-1 external USB
optical drive. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: the drive at a slight diagonal across the centre, hub end lower left, turned so the
disc slot, eject button, card slots, USB ports and cable all show. Half the picture's width.

SETTING: a very pale cool blue ground, almost white, empty around the drive.

LIGHT: broad and even. No part in shadow.

CALLOUTS: six charcoal sans-serif labels on the empty ground, each joined to its part by one
thin charcoal line, none touching another. Nothing sits in the lower right:
Reads the discs your laptop forgot · Ejects with one press, not a paperclip ·
Takes the camera card straight out of the bag · Two ports, so the mouse keeps its own ·
One cable, and it is the one you carry · Folds flat into the sleeve pocket

TEXT: across the top, two lines of charcoal sans-serif starting the same distance from the
left edge as the leftmost label. The two lines fill that band margin to margin and are the
largest text here:
ONE PORT SHORT
IS NOT A PLAN
Each callout label is half the height of those capitals.

BADGE: LOWER LEFT, as wide as the drive is deep. A filled circle in warm amber with a deeper
amber ring around its outer third and a thin white outline inset inside the edge, carrying
SEVEN in large white capitals over IN ONE in small white capitals.

Nothing comes within a tenth of the width of any edge. These are the only words in the
picture; no logo, no watermark, no person, no room.
```

---

## 3 — `06-relief-claimstack` · wall-mounted air cooler · PRODUCT subject · badge `pill` · pale sand field

Holds the widened subject slot at the PRODUCT, which passed, and changes only the field's
value and the badge's interior.

```
TYPE: 06-relief-claimstack v0.4
REGISTER: commercial editorial photograph on a flat field.

PRODUCT REFERENCE: the attached photo is the exact reference for the wall-mounted portable
air cooler. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: the cooler alone, cut out cleanly, three-quarter angle, vents to the lower left,
holding the right third of the picture.

FIELD: one flat pale sand tone behind it — light and quiet, no gradient, no texture, no room,
no shadow under the cut-out.

LIGHT: soft and directional on the cooler only, from behind and right, a faint rim on its
upper edge. The field is unlit and flat.

TEXT: in the empty field on the left, all flat charcoal sans-serif, every line and glyph
beginning the same distance from the left edge. The headline fills that field margin to
margin and is the largest text here; the three lines under it are half its height:
THE ROOM COOLS.
THE BILL DOES NOT.
then, each with a small line glyph at its left —
a plug glyph — Runs off the socket already behind the bed
a drop glyph — Fill it at the tap, not at the hardware shop
a bracket glyph — Goes on the wall and stays out of the floor

BADGE: UPPER LEFT, as wide as the cooler's body. A fully rounded capsule in deep signal green
with a narrow paler green rim, carrying NO TOOLS in large white capitals over TO FIT IT in
small white capitals.

Nothing comes within a tenth of the width of any edge. These are the only words in the
picture; no logo, no watermark, no packaging, no person, no room.
```

---

## 4 — `06-relief-claimstack` · L-shaped seat cushion · PERSON subject, real room · badge `seal` · lit wall

Holds the widened field at a real room, which passed, and changes the ground's value and the
badge's interior.

```
TYPE: 06-relief-claimstack v0.4
REGISTER: commercial editorial photograph in a real room.

PRODUCT REFERENCE: the attached photo is the exact reference for the L-shaped memory foam
seat cushion. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: a woman in her thirties in a plain navy jumper, upright on a hard desk chair with the
cushion under her, working, looking down at her hands. She holds the right half.

FIELD: a real home office behind her — a plain white wall, daylight raking across it from a
window out of frame, a desk edge lower right. The wall to her left is empty, bright and well
out of focus, and the words sit straight on it with no panel.

LIGHT: plain daylight from the window side. No rim light, no studio key.

TEXT: on the out-of-focus wall at the left, flat charcoal sans-serif, every line and glyph
beginning the same distance from the left edge. The headline fills that wall margin to margin
and is the largest text here; the three under it are half its height:
HOUR FOUR
FEELS LIKE HOUR ONE
then, each with a small line glyph at its left —
a spine glyph — Holds the curve your chair gave up on
a clock glyph — Still doing it at the end of the afternoon
a case glyph — Comes off the chair and into the car

BADGE: UPPER RIGHT, on the wall and nothing else, as wide as her head. A scalloped rosette in
deep plum with a darker plum outer scallop and a thin cream ring inside it, carrying SITS FLAT
in large cream capitals over ON ANY CHAIR in small cream capitals.

Nothing comes within a tenth of the width of any edge. These are the only words in the
picture; no logo, no watermark, no poster or label, no second person.
```

---

## 5 — `07-identity-pack` · furniture lifting tool set · CLOSED form · badge `roundel` · off-white ground

The pack-lettering test again, on a flat opaque printed carton. The founding round's clean
render was a flat opaque pouch and its failure was small type curved around a translucent
body; this frame is the flat-and-opaque half of that hypothesis on a product neither has seen.

```
TYPE: 07-identity-pack v0.3
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the furniture lifting tool
set and its printed carton. Preserve shape, proportions, material, finish, colour and every
word printed on it exactly.

FORM: closed. The carton upright and sealed, nothing detached, nothing beside it.

SUBJECT: the brand face meets the lens, the carton turned a few degrees so its depth reads.
About half the picture's height.

SETTING: a soft off-white ground, almost colourless, a soft contact shadow beneath the carton.
No room, no prop, no second object.

LIGHT: broad and even, front and slightly above, strong enough that every printed word on the
carton stays legible.

TEXT: across the upper empty ground, two lines of flat charcoal sans-serif beginning a tenth
of the picture's width from the left edge. The two lines fill that band margin to margin and
are the largest text here:
LIFT IT ALONE
PUT IT DOWN GENTLY

BADGE: LOWER LEFT, as wide as the carton is deep. A filled circle in deep signal red with a
narrow cream ring inset inside its edge, a cream line icon of a wheeled slider in the upper
half, ONE PERSON in large cream capitals under it, ONE ROOM in small cream capitals below.

Nothing comes within a tenth of the width of any edge. The two lines and the badge are the
only added words; the carton's own printed label is part of the object and stays exactly as
the reference shows it. No logo, no watermark, no person, no hand, no room.
```

---

## 6 — `07-identity-pack` · carbide shaping pad set · WITH CONTENTS form · badge `tag` · dark ground, justified

**The one dark ground in the round, and it is a choice with a reason**: the pads are dark
carbide-grit discs and a light ground would lose their edge profile, which is the thing this
packshot exists to show. The rule is that a dark ground needs a reason, not that it is banned.

```
TYPE: 07-identity-pack v0.3
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the carbide wood shaping pad
set and its printed pack. Preserve shape, proportions, material, finish, colour and every word
printed on the pack exactly.

FORM: with contents. The pack upright and closed, three shaping pads laid on the ground at its
lower left, none touching it, each turned so its cutting face shows.

SUBJECT: the brand face meets the lens. The pack takes about half the picture's height; the
pads sit small in front and give it its scale.

SETTING: a mid-grey ground, faintly textured, dark enough that the pads' cutting edges
separate from it, a soft contact shadow under the pack and a fainter one under each pad.

LIGHT: broad and even, front and slightly above, raking enough across the pads to pick out
their teeth and strong enough that the pack's printed words read.

TEXT: across the upper empty ground, two lines of flat white sans-serif beginning a tenth of
the picture's width from the left edge. The two lines fill that band margin to margin and are
the largest text here:
SHAPES WOOD
LIKE IT IS SOFT

BADGE: UPPER RIGHT, as wide as one pad, tilted a few degrees off square. A hard-edged
rectangle in bright signal yellow with a thin black outline inset inside its edge, carrying
CARBIDE in large black capitals over GRIT in small black capitals.

Nothing comes within a tenth of the width of any edge. The two lines and the badge are the
only added words; the pack's own printed label is part of the object and stays exactly as the
reference shows it. No logo, no watermark, no person, no hand, no room.
```

---

## Grading

Verdict `pass`, `partial` or `fail` per render — yours, under ADR-011, and SPEC §6.3(3)
requires it. Then the four the last round could not answer plus the three this one adds:

| # | question | what it changes |
|---|---|---|
| 1 | **Is the headline a hook or a caption?** Would it be equally true of a competitor? | G16's copy-craft section |
| 2 | **Is the badge the first thing you see, before the product?** | whether the badge INTERIOR was the missing variable, or whether three passes were all aimed wrong |
| 3 | **Does the product read as well against a light ground as it did against a dark one?** | G16 round 4's ground rule — the whole of it |
| 4 | **Does a PRODUCT subject read as well as a person?** | `06-relief-claimstack` `PARTS/subject` |
| 5 | Did FILL size the headline where the anchor did not? | the fifth instrument aimed at text size; measured off the file, but say if it looks wrong |
| 6 | Is every word printed on the pack still a real word? | `07-identity-pack` — 1 of 2 so far, and prompts 5 and 6 are the flat-opaque half of the hypothesis |
| 7 | Is prompt 6's dark ground earned, or is it the old habit with a better excuse? | whether "a dark ground needs a reason" is a rule or a loophole |

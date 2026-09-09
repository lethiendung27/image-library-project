# Toplist round 1 — seven prompts, one per type

The first render test of the third namespace. Nothing in `registry/toplist-types/` has ever
been rendered, so **every clause in all seven files is a proposal** and this round is what
turns the first of them into evidence.

**Ratio is not stated anywhere.** The app resolves the lede ratio (owner, 2026-09-09), and
ADR-016 plus adapter Rule 4 keep a ratio out of prompt text regardless.

**Attach a product photo** wherever a prompt opens with PRODUCT REFERENCE. The category is
named; which product is yours — that is what "sản phẩm bất kì" means here, and G1 binds
whatever you attach.

## What each prompt can and cannot settle

| # | type | status | reference photos | text |
|---|---|---|---|---|
| 1 | `lede-pain` | active | **none** — the product is absent by definition | no |
| 2 | `lede-inuse` | active | 1 | no |
| 3 | `lede-lineup` | reserved | **none, deliberately** — see below | no |
| 4 | `lede-testing` | active | 1 | no |
| 5 | `lede-winner` | active | 1 | **yes** — display type + mark |
| 6 | `lede-collage` | reserved | **none, deliberately** | **yes** — title + badge |
| 7 | `lede-authority` | reserved | 1 | no |

**3 and 6 are the reserved multi-product types and they are written with NO reference
photo on purpose.** Their blocker is that a five-product frame needs five attachments and
ADR-021 allows one. Rather than ship a prompt nobody can run, these two render **unbranded
generic units**, which is single-pass, needs no attachment, and sidesteps `SPEC.md:256` on
competitor marks entirely. **What that cannot test is G1 fidelity** — whether the renderer
holds five real products — and that question stays open until the attachment limit is
decided. What it does test is everything else: the arrangement, the no-favoured-unit law,
the ground, and for 6 the text and badge.

**7 is written without the parts that make it illegal.** `lede-authority` has no skeleton
in its own file, deliberately, because G16 marks *a named expert* as LAW and
`mapping/slot-rules.md` already calls a portrait of a named person out of library scope.
This prompt therefore carries **no name, no credential, no byline, no lab coat, no title
card** — and it exists to answer one question: with those removed, is anything left that
`lede-inuse` does not already do? If the answer is no, the type should be retired rather
than unblocked, and that is a cheaper thing to learn from one render than from an ADR.

**5 carries a drafted verdict.** `lede-winner`'s SLOT CONSTRAINTS say the mark's words come
from the input's rank field and from nowhere else; that field does not exist yet, so the
line below is DRAFTED and is not a claim any page has made. On a real page it comes from
the input or the type does not route.

**G16 binds 5 and 6** — they declare `text_layer`. Everything the four G16 rounds measured
applies and is not restated in the prompts: the badge carries an internal tone step and two
type sizes (ADR-068), it takes a colour the photograph does not have, it stays out of the
bottom-right watermark corner, the headline is sized by FILL rather than by an anchor
(anchors measured 0.13–0.64 and never 1.0), alignment is written as an observable, and
nothing comes within a tenth of the width of an edge.

**The grounds are this namespace's own** and no rule is imported from the product-page
registry (ADR-073, owner instruction). Measured on the 32 frames of `stills/top list/`, one
number splits the namespace with no overlap — the mean adjacent-pixel difference in the
outer ring:

```
designed      lede-winner 0.8   lede-collage 1.9   lede-lineup 2.9
photographed  lede-authority 7.0   lede-testing 7.1   lede-inuse 10.0
```

Nothing sits between 2.9 and 7.0 in 32 frames. **`lede-lineup` is on the designed side**,
which corrected that file's own assumption: its backdrop is a studio sweep and only the
surface under the units is real.

**Prompts 3 to 6 carry the clause of their own family**, and 5 and 6 deliberately take the
TWO forms the designed grounds come in — 5 the two-hue diagonal gradient (3 of 5 corpus
collages, measured at 175–177° of hue spread), 6 the single flat tone (2 of 5, under 13°).
Nothing between the two forms was observed, so the round tests both rather than the same
one twice.

---

## 1 — `lede-pain` · scalp discomfort · no product, no words

```
TYPE: lede-pain v0.2
REGISTER: editorial photojournalism, natural and unstaged. Single frame.

SUBJECT: a woman in her late thirties in a plain grey t-shirt, sitting on the edge of an
unmade bed in early morning light, one hand up in her hair at the crown, head tipped
slightly down and away.

EVIDENCE: the scalp visible where her fingers part the hair — dry, tight, flaking at the
parting. The symptom is a physical fact and it is the thing in focus.

COST: her work bag and a lanyard sit packed by the door behind her, and she is not moving
toward them. What the morning is taking is the start of it.

PLACE: an ordinary bedroom, curtains half open, the light from one window and nothing
added.

GAZE: candid. She is not aware of the lens and does not look toward it.

GRADE: an ordinary photograph in ordinary light. Normal exposure, detail held in the
shadows and in the window, no filter and no colour cast.

GROUND: the wall behind her is light and near-neutral, and it stays quiet — the picture's
colour is in her and in the room, not in the wall.

No product anywhere in the frame and none implied. No words, no numbers, no logo, no
badge. Nothing comes within a tenth of the width of any edge.
```

---

## 2 — `lede-inuse` · upper-arm blood pressure monitor · one photo, no words

```
TYPE: lede-inuse v0.2
REGISTER: candid documentary photograph, single frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the upper-arm blood
pressure monitor. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: a man in his sixties in a soft open-collar shirt, seated at a kitchen table with
the cuff already on his upper arm, reading a newspaper folded beside him. Unhurried.

ENVIRONMENT: his own kitchen on an ordinary weekday morning — a mug, a fruit bowl, a
window with the blind up. Lived in, not styled.

PRODUCT: the monitor on the table within easy reach, the cuff on his arm, present as the
reason the morning is calm rather than as the subject of the photograph.

GAZE: candid, absorbed in the paper, not toward the lens.

LIGHT: even natural daylight, bright, soft shadows. No golden hour, no rim light.

GRADE: a natural palette, light grain, shallow depth of field. Honest, not glossy.

GROUND: the kitchen wall behind him is light and near-neutral and stays quiet.

No screen reading is legible, no number anywhere in the frame. No words, no logo, no
badge, no second person. Nothing comes within a tenth of the width of any edge.
```

---

## 3 — `lede-lineup` · five cordless electric scissors · unbranded, no words

```
TYPE: lede-lineup v0.2
REGISTER: editorial product photograph, one frame, no words in it.

FIELD: five cordless electric scissors standing in a row on one surface, each a visibly
different design — different handle shape, different blade guard, different body colour —
and all plausible as real products. No brand marks, no logos, no printed names on any of
them.

ARRANGEMENT: no unit favoured. The same height in frame, the same distance from the lens,
the same spacing, none centred and none forward of the others.

SURFACE: one pale oak worktop running the width of the frame, real and slightly worn. The
surface is real and takes real contact shadows.

LIGHT: one broad soft source for the whole group, from the front and slightly above, with
one real contact shadow under each unit and no unit separately lit.

GROUND: a smooth studio seamless behind the worktop, NEAR-WHITE — the units are dark and
coloured, so the sweep stays out of their way. No wall, no room, no texture, no gradient,
no vignette, and no visible join between the sweep and the worktop.

No rank number, no badge, no podium, no riser under any unit, no person, no word, no price
and no logo anywhere in the picture. Nothing comes within a tenth of the width of any edge.
```

---

## 4 — `lede-testing` · electric kettle · one photo, no legible reading

```
TYPE: lede-testing v0.2
REGISTER: editorial documentary photograph, one frame, no words in it.

PRODUCT REFERENCE: the attached photo is the exact reference for the electric kettle.
Preserve shape, proportions, material, finish and colour exactly.

UNIT: the kettle standing on a grey working surface, lid open, positioned so its base and
its spout both read.

INSTRUMENT: a handheld electrical test meter beside it with two coiled leads running from
the meter to the kettle's plug and base — in contact, not lying nearby.

HANDS: one hand steadies the kettle and the other rests on the meter, both cropped at the
forearm. The hands are working, not presenting.

SURFACE: a real bench — a roll of cable, a small screwdriver, a notebook face down. The
tools of the measurement and nothing decorative.

LIGHT: plain overhead working light. It falls off across the frame — one side of the
background is clearly darker than the other. No studio key, no rim, no fill.

GROUND: a REAL working place behind the bench, mid-toned and almost colourless: metal
racking, a doorway, other work going on, all thrown out of focus. Not a sweep, not a
painted backdrop, and not evenly lit. The colour in this picture is in the kettle and the
meter, never in the room.

The meter's display is turned away from the lens and no reading is legible anywhere. No
chart, no gauge face, no lab coat, no clipboard, no face, no word, no price and no logo in
the picture. Nothing comes within a tenth of the width of any edge.
```

---

## 5 — `lede-winner` · portable juicer cup · display type, `plaque` mark

```
TYPE: lede-winner v0.5
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the portable juicer cup.
Preserve shape, proportions, material, finish, colour and its printed words exactly.

SUBJECT: the cup alone, upright with its lid on, the brand face to the lens, turned a few
degrees so its depth reads, CUT OUT and floating with no surface under it and no shadow
implying one. It holds the right half of the picture.

GROUND: a designed field, light and strongly coloured. A perfectly smooth diagonal
gradient from clear teal at the upper left to warm coral at the lower right — two hues
opposite on the colour wheel. No grain, no texture, no vignette, no banding, no surface,
no shadow, no room, no prop.

LIGHT: broad and even, front and slightly above, strong enough that the cup's printed
words stay legible.

DISPLAY TYPE: the single word BLENDERS in flat white capitals, set BEHIND the cup so the
cup overlaps it, and so large that the word runs off BOTH side edges — the B and the S are
cut by the frame. It is the largest thing in the picture after the cup.

MARK: form `plaque`. Over the LEFT third, on the display type and clear of the cup, about
a third of the picture wide. An upright rectangle in deep ink blue — a colour neither the
cup nor the gradient carries — a thin cream rule across it, BEST OVERALL in large cream
capitals above and 2026 in small cream capitals below.

No score, star row, rating, certification seal, press logo or third-party award mark. The
display type may be cut by the side edges; the mark's words may not, and nothing else comes
within a tenth of the width of any edge.
```

---

## 6 — `lede-collage` · four robot vacuums · unbranded, title and badge

```
TYPE: lede-collage v0.3
REGISTER: graphic product composition, one frame.

CUT-OUTS: four robot vacuums, each cleanly cut out with no scene behind it, each a visibly
different design — body colour, top-plate, one with a dock — and all plausible as real
products. No brand marks, no logos, no printed names.

ARRANGEMENT: a single row across the lower two thirds, read left to right, evenly spaced.
No unit favoured by size, height or position.

GROUND: a designed field, light and strongly coloured, in the FLAT form — one single
saturated tone, a clear cobalt, filling the frame corner to corner. No gradient, no second
hue, no grain, no texture, no vignette, no scene.

SHADOW: one faint contact shadow under each unit, identical for all four.

TITLE: across the empty upper band, two lines of flat charcoal sans-serif, each beginning
the same distance from the left edge. The two lines fill that band from margin to margin
and are the largest text in the picture:
THE BEST FOUR
ROBOT VACUUMS

BADGE: form `plaque`. Sitting OVER the second vacuum from the left, overlapping its upper
body, as wide as one vacuum. A rounded-square tag in a warm terracotta — a colour neither
the units nor the gradient carries — with a slightly deeper terracotta band across its
lower third, TESTED in large cream capitals on the upper part and ALL FOUR in small cream
capitals on the band.

No rank number, no price, no podium, no scene, no person, no drop shadow under one unit
only, no certification seal, no press logo, no third-party award mark and no fabricated
rating. Nothing comes within a tenth of the width of any edge.
```

---

## 7 — `lede-authority` · anyone, unnamed · one photo, no words

The type has no skeleton in its own file and this prompt does not create one. It removes
everything that makes the type illegal and asks what is left.

```
TYPE: lede-authority v0.1 — DIAGNOSTIC, not a skeleton
REGISTER: editorial documentary photograph, one frame, no words in it.

PRODUCT REFERENCE: the attached photo is the exact reference for the product. Preserve
shape, proportions, material, finish and colour exactly.

SUBJECT: a woman in her forties in an ordinary jumper, standing at a kitchen counter,
holding the product up at chest height and turned toward the lens, mid-sentence as if
explaining it to someone just out of frame.

ENVIRONMENT: an ordinary domestic kitchen, lived in, the counter clear around her hands.

LIGHT: plain daylight from a window to one side. No studio key, no rim, no seamless.

GRADE: a natural palette, light grain. Honest, not glossy.

GROUND: the wall behind her is light and near-neutral and stays quiet.

No name, no caption, no byline, no title card, no lab coat, no clipboard, no lanyard, no
certification seal, no star row, no logo, no word and no number anywhere in the picture.
Nothing comes within a tenth of the width of any edge.
```

---

## Grading

A verdict of `pass`, `partial` or `fail` per render — yours, under ADR-011. Then:

| # | question | what it changes |
|---|---|---|
| 1 | **Does 3 hold the no-favoured-unit law?** Cover the labels: can you tell which one the picture thinks won? | `lede-lineup`'s ARRANGEMENT, the type's only real law |
| 2 | **In 4, is any reading legible anywhere?** | `lede-testing`'s NEGATIVE — the clause that keeps the type out of A15 |
| 3 | **In 4, does the frame still argue "we measured it" with the display turned away?** | whether the apparatus alone carries the argument, which is the type's whole premise |
| 4 | **In 7, is anything left that `lede-inuse` does not do?** | whether `lede-authority` survives at all, or is retired |
| 5 | Do the badges in 5 and 6 read as badges, or as labels? | ADR-068's badge interior, first test outside the direct-response types |
| 6 | Did FILL size the headlines in 5 and 6? | the fifth instrument aimed at text size |
| 7 | **Do 5 and 6's strongly-coloured grounds carry the frame, or fight the product?** | `PARTS/ground` on both types, rewritten off this namespace's own corpus and untested |
| 10 | **Which of the two designed forms reads better — 5's diagonal gradient or 6's flat tone?** | the corpus does both and nothing between; a preference here is the first evidence either way |
| 11 | **In 3, does the near-white seamless leave the dark scissors readable, or would a saturated sweep have been better?** | `lede-lineup`'s bimodal saturation — the corpus splits 3 near-white against 2 strongly coloured and the choice is the prompt's |
| 12 | **In 4, does the uneven light read as a real place or as a badly lit studio?** | `lede-testing`'s ring spread of 0.67, the clause with the largest sample in the namespace |
| 8 | Do the unbranded units in 3 and 6 read as real products, or as toys? | whether the no-attachment route is usable at all while the photo limit stands |
| 9 | **In 6, does the badge over one unit read as NAMING a winner or as FAVOURING one?** | `lede-collage` MARKS against its own no-favoured-unit law — 2 of 2 corpus badges sit over a unit, and this is the first check of whether that is safe to copy |

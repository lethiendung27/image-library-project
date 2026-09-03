# Test prompts — six renders, three types

Set the ratio at the tool: **1:1** for all six. The ratio never goes in the prompt
(ADR-016, adapter Rule 4).

**Every product here is one none of these types has ever been built from.** They come from
`query/product-slugs.yaml` — the repo's own closed list — and not one of them appears in any
proposal's source list. A rule that holds on a product it has never seen is a real rule; a
rule that holds on the product it was written from is a coincidence.

**Attach the product photo** where a prompt opens with a PRODUCT REFERENCE block. An empty
attachments field is not a blocked prompt — the block is written to be paste-and-run with the
photo you attach in the tool.

**The claim text is a PLACEHOLDER in every prompt.** It names parts and functions that are
structurally true of the object and asserts no figure, because a number in a frame is a claim
the frame cannot substantiate (argument-fault A12). Before any of these ships on a real page,
every word comes from that page's own `content.json`. For THIS round leave the words as they
are — the round measures whether text renders and where it lands, not what it says.

Three fixes from the earlier rounds are in all six: **the badge is bottom LEFT** (the
generation tool's watermark sits at about 90% across, 90% down and struck through 3 of 3
badges placed bottom-right); **alignment is written as an observable** rather than as "left
aligned", which was ignored 1 of 3; and each prompt **asks for a tenth of the picture clear**
on every side, which moved the measured floor from 5.3% to 6.7% against G10's 8%.

---

## 1 — `03-spec-callout`, five clusters · translation earbuds

The safe end of this type's budget. Five clusters is what G16's founding rounds actually
measured.

```
TYPE: 03-spec-callout v0.1
REGISTER: commercial product photograph. One frame, no panels, no insets.

PRODUCT REFERENCE: the attached photo is the exact reference for the wireless translation
earbuds and their charging case. Preserve shape, proportions, material, finish and colour
exactly. Do not redesign, restyle, simplify or add features.

PRESENTATION: the open charging case sits slightly left of centre with one earbud resting
in it and the other standing upright beside it, turned so its outer face and its inner
contacts are both visible. Together they occupy about half the width of the picture.

SETTING: one plain pale grey ground with a soft contact shadow, and clear empty ground
around the objects on all four sides for the labels to sit on. No room, no surface texture,
no second object.

LIGHT: broad and even from the front and slightly above, so every part of both objects is
legible and nothing falls into shadow. No hard side light.

CALLOUTS: four short labels in flat solid dark grey sans-serif, each on the empty ground,
each joined to the part it names by one thin straight grey line:
upper left, joined to the outer face of the standing earbud: The touch panel
lower left, joined to the inner face of the standing earbud: The microphone port
upper right, joined to the earbud lying in the case: The charging contacts
lower right, joined to the open lid of the case: The lid that holds the charge

TEXT: across the top of the picture, one line of larger bolder dark grey sans-serif,
beginning at the same distance from the left edge as the upper-left label:
EVERY PART, NAMED

Nothing in the picture comes within a tenth of its width of any edge.

The words named above are the only words in the picture. Nothing else carries a letter or a
number — no logo, no watermark, no packaging, no second caption. No person, no hand, no
room, no arrows between the labels.
```

---

## 2 — `03-spec-callout`, eight clusters · cordless electric scissors

**This is the experiment.** The type's own count rule allows six labels plus a title plus a
badge — eight clusters — and G16 has only ever measured five. Different product from prompt 1
on purpose, so a failure is not confounded by re-running one object.

```
TYPE: 03-spec-callout v0.1 — CLUSTER CEILING TEST
REGISTER: commercial product photograph. One frame, no panels, no insets.

PRODUCT REFERENCE: the attached photo is the exact reference for the cordless electric
scissors. Preserve shape, proportions, material, finish and colour exactly. Do not redesign,
restyle, simplify or add features.

PRESENTATION: the scissors lie at a slight diagonal across the centre of the picture, blade
to the upper right and grip to the lower left, turned so the blade, the trigger, the switch
and the charging port are all visible at once. They occupy about half the width.

SETTING: one plain pale warm grey ground with a soft contact shadow, and clear empty ground
all around for the labels. No room, no surface texture, no second object.

LIGHT: broad and even, front and slightly above. Every named part is legible and no part
falls into shadow.

CALLOUTS: six short labels in flat solid near-black sans-serif, each on the empty ground,
each joined to the part it names by one thin straight grey line:
The cutting blade · The safety guard · The trigger · The speed switch ·
The charging port · The moulded grip
Place them so no two labels touch and no line crosses another.

TEXT: across the top, one line of larger bolder near-black sans-serif, beginning at the same
distance from the left edge as the leftmost label:
SIX PARTS, ONE TOOL

BADGE: in the lower LEFT of the picture, on the empty ground and well inside the edges, a
small flat solid near-black rectangle, and inside it in white capitals: CORDLESS

Nothing in the picture comes within a tenth of its width of any edge.

The words named above are the only words in the picture. Nothing else carries a letter or a
number — no logo, no watermark, no packaging, no second caption. No person, no hand, no
room, no arrows between the labels.
```

---

## 3 — `06-relief-claimstack`, PRODUCT subject on a flat field · dust mite vacuum

The type's `PARTS/subject` was widened today to admit the product where it used to demand a
person. **The field is held at the known-good flat tone**, so this render isolates the subject
change alone.

```
TYPE: 06-relief-claimstack v0.2
REGISTER: commercial editorial photograph on a flat coloured field.

PRODUCT REFERENCE: the attached photo is the exact reference for the handheld dust mite
vacuum. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: the vacuum alone, cut out cleanly and placed on the field at a three-quarter angle
with its nozzle toward the lower left, occupying the right third of the picture.

FIELD: one flat pale slate blue filling the whole picture behind it, with no gradient, no
texture, no room and no shadow under the cut-out.

LIGHT: soft and directional on the vacuum only, from behind and to its right, so its upper
edge carries a faint rim. The field itself is unlit and stays flat.

LAYOUT: the vacuum holds the right third; the left two thirds of the field are empty.

TEXT: in the empty field on the left, a headline and beneath it three separate lines each
with a small simple line-drawn glyph at its left. All of it flat solid white sans-serif.
Every line, and every glyph, begins at the same distance from the left edge of the picture.
The headline, larger and bolder than everything under it, reads exactly:
THE MATTRESS YOU SLEEP ON
Then three lines, each smaller than the headline and each with its own glyph:
a sun glyph, then the line: Works dry, on any fabric
a bed glyph, then the line: Reaches into the mattress surface
a battery glyph, then the line: Cordless, so nothing trails

BADGE: in the lower LEFT, on the empty field and well inside the edges, a small flat solid
white rectangle, and inside it in slate blue capitals: HANDHELD

Nothing in the picture comes within a tenth of its width of any edge.

The words named above are the only words in the picture. Nothing else carries a letter or a
number — no logo, no watermark, no packaging, no disclaimer line, no asterisk. No person, no
room, no real background, no drop shadow under the cut-out.
```

---

## 4 — `06-relief-claimstack`, PERSON subject in a REAL ROOM · hydraulic arm trainer

The second clause widened today: the field may be a real room, with the words set into its
own out-of-focus area and no panel behind them. **The subject is held at the known-good
person**, so this render isolates the field change alone.

```
TYPE: 06-relief-claimstack v0.2
REGISTER: commercial editorial photograph in a real room.

PRODUCT REFERENCE: the attached photo is the exact reference for the hydraulic arm strength
trainer. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: a man in his forties in a plain grey t-shirt, seated on a low bench, working the
trainer with both hands at chest height, looking down at it with an even unforced
expression. He occupies the right half of the picture and is cropped at the thigh.

FIELD: a real living room continuing behind him — a plain painted wall, a window out of
frame throwing daylight across it, a rug edge and a chair leg at the picture's foot. The
wall behind his left is empty and thrown well out of focus, and the words sit directly on
it with no panel and no box behind them.

LIGHT: plain daylight from the window side. No rim light, no studio key.

LAYOUT: he holds the right half; the out-of-focus wall on the left holds the words.

TEXT: on the out-of-focus wall at the left, a headline and beneath it three separate lines
each with a small simple line-drawn glyph at its left. All of it flat solid white
sans-serif, dark enough behind it to read. Every line, and every glyph, begins at the same
distance from the left edge of the picture. The headline, larger and bolder, reads exactly:
FIVE MINUTES, SITTING DOWN
Then three lines, each smaller and each with its own glyph:
a dial glyph, then the line: Resistance you set by hand
a counter glyph, then the line: The count is on the display
a chair glyph, then the line: Works seated, indoors, anywhere

BADGE: in the lower LEFT, on the out-of-focus floor and well inside the edges, a small flat
solid white rectangle, and inside it in dark grey capitals: NO WEIGHTS

Nothing in the picture comes within a tenth of its width of any edge.

The words named above are the only words in the picture. Nothing else carries a letter or a
number — no logo, no watermark, no packaging, no poster or label in the room, no disclaimer.
No second person.
```

---

## 5 — `07-identity-pack`, CLOSED form on a plain ground · portable juicer cup

The plainest form the type has. Its whole deliverable is a reference-faithful object, so the
one thing to watch is whether the pack's own printed lettering survives.

```
TYPE: 07-identity-pack v0.1
REGISTER: commercial product photograph. One frame, no panels, no insets.

PRODUCT REFERENCE: the attached photo is the exact reference for the portable juicer cup.
Preserve shape, proportions, material, finish, colour and every word printed on it exactly.
Do not redesign, restyle, simplify or add features.

FORM: closed. The cup stands upright and complete with its lid on, nothing detached and
nothing beside it.

PRESENTATION: the face carrying the brand mark meets the lens square on, the cup turned just
a few degrees so its depth reads. It occupies about half the height of the picture.

SETTING: one flat pale grey ground with a soft contact shadow directly beneath it. No room,
no surface texture, no second object, no prop.

LIGHT: broad and even from the front and slightly above, soft enough that the finish reads
and strong enough that every word printed on the cup stays legible.

TEXT: across the upper part of the empty ground, one line of flat solid dark grey
sans-serif, beginning a tenth of the picture's width from the left edge:
THIS IS WHAT ARRIVES

Nothing in the picture comes within a tenth of its width of any edge.

The line above is the only added word in the picture. The cup's own printed label is part of
the object and stays exactly as the reference shows it. Nothing else carries a letter or a
number — no logo, no watermark, no badge, no second caption. No person, no hand, no room, no
second product.
```

---

## 6 — `07-identity-pack`, WITH CONTENTS form · rodent repellent balls

The form that shows what comes out of the pack. Different product from prompt 5 on purpose.

```
TYPE: 07-identity-pack v0.1
REGISTER: commercial product photograph. One frame, no panels, no insets.

PRODUCT REFERENCE: the attached photo is the exact reference for the rodent repellent balls
and their pack. Preserve shape, proportions, material, finish, colour and every word printed
on the pack exactly. Do not redesign, restyle, simplify or add features.

FORM: with contents. The pack stands upright and closed, and four of the balls lie loose on
the ground at its lower left, none of them touching the pack.

PRESENTATION: the face carrying the brand mark meets the lens square on. The pack occupies
about half the height of the picture; the loose balls sit small in front of it and give it
its scale.

SETTING: one flat pale warm grey ground with a soft contact shadow under the pack and a
fainter one under each ball. No room, no surface texture, no prop, no second product.

LIGHT: broad and even from the front and slightly above, soft enough that both the pack's
finish and the balls' surface read, and strong enough that every word printed on the pack
stays legible.

TEXT: across the upper part of the empty ground, one line of flat solid dark grey
sans-serif, beginning a tenth of the picture's width from the left edge:
THE PACK, AND WHAT IS IN IT

BADGE: in the lower LEFT, on the empty ground and well inside the edges, a small flat solid
dark grey rectangle, and inside it in white capitals: READY TO PLACE

Nothing in the picture comes within a tenth of its width of any edge.

The words named above are the only added words in the picture. The pack's own printed label
is part of the object and stays exactly as the reference shows it. Nothing else carries a
letter or a number — no logo, no watermark, no second caption. No person, no hand, no room.
```

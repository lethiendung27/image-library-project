# Test prompts — six renders, three types

Ratio **1:1**, set at the tool. It never goes in the prompt (ADR-016, adapter Rule 4).
**Attach the product photo** where a prompt opens with PRODUCT REFERENCE.

Every product comes from `query/product-slugs.yaml` and none appears in any candidate's
source list. A rule that holds on a product it has never seen is a rule.

## Rewritten 2026-09-03, second pass — four owner findings, all measured

| finding | what was measured | what changed |
|---|---|---|
| the prompts are bloated | 1488–2128 chars against adapter Rule 6's 1450–1600 reference; 4 of 6 over | now **1336–1628**, every one inside the reference band. Measured, not asserted: −152 to −594 chars each. The closing negative ran ~40 words in every prompt and is now one line; the safe-area clause is stated once rather than per element |
| the badge is monotonous | 6 of 6 said "a small flat solid rectangle… in white capitals" | a badge is a MARK, not a text slot. Each type now owns a form library — tag, seal, pill, roundel, chip, flash — and each prompt names a DIFFERENT form, chosen from what the product's register carries |
| the background is monotonous | 6 of 6 said "one plain pale grey ground" | six different grounds, each picked from the product's own register |
| the text is too small | headline bands measured 5.0–6.1% of frame height, everything else 3.3–5.5% — **19–24px and 13–21px on a 390pt phone**, against a 17px platform floor | G16 gains a mobile FLOOR: the headline's capitals at least a tenth of the picture's height, every other line at least a sixteenth. Each prompt now states it |

The copy is **drafted, not any page's own** — no `content.json` was available — so it claims
only what each object's facts support and carries no figure. G16's caps no longer bind (owner
waiver, same day); lines past seven words are marked so the render log can move the cap.

---

## 1 — `03-spec-callout` · translation earbuds · badge `chip` · dark technical ground

```
TYPE: 03-spec-callout v0.1
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the wireless translation
earbuds and case. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: the open case slightly left of centre, one earbud resting in it, the other standing
beside it turned so its outer face and inner contacts both show. Together about half the
picture's width.

SETTING: a dark charcoal ground with a faint cool sheen, empty on all four sides.

LIGHT: broad and frontal, soft enough that no part of either object falls into shadow.

CALLOUTS: four labels in flat white sans-serif on the empty ground, each joined to its part by
one thin white line:
outer face of the standing earbud — Tap it and it listens
inner face of the standing earbud — The mic that hears you first
the earbud in the case — Drops in, charges, forgets nothing
the open lid — Pocket-sized, so it comes with you

TEXT: across the top, two lines of white sans-serif, each starting the same distance from the
left edge as the upper-left label. The capitals stand a tenth of the picture's height, so the
line reads on a phone:
UNDERSTAND EACH OTHER
BEFORE THE SENTENCE ENDS
Each callout label stands at least a sixteenth of the picture's height.

BADGE: lower LEFT, a small white line icon of two speech bubbles inside a thin white circle,
with the words TWO LANGUAGES in white capitals beneath it.

Nothing comes within a tenth of the picture's width of any edge. The words above are the only
words in the picture; no logo, no watermark, no person, no room.
```

---

## 2 — `03-spec-callout` · cordless electric scissors · badge `tag` · warm workbench ground

The ceiling test: six labels plus a title plus a badge is eight clusters, and G16 has measured
five.

```
TYPE: 03-spec-callout v0.1 — CLUSTER CEILING TEST
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the cordless electric
scissors. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: the scissors lying at a slight diagonal across the centre, blade upper right, grip
lower left, turned so blade, guard, trigger, switch and charging port all show. About half
the picture's width.

SETTING: a warm mid-brown worn workbench surface, softly out of focus, empty around the tool.

LIGHT: broad and even. No part in shadow.

CALLOUTS: six labels in flat cream sans-serif on the empty surface, each joined to its part
by one thin cream line, none touching another:
Cuts what scissors would fight · The guard your other hand thanks ·
One finger does the whole job · Slow for card, fast for fabric ·
Charges where your phone charges · Shaped for hands that ache after ten minutes

TEXT: across the top, two lines of cream sans-serif starting the same distance from the left
edge as the leftmost label, capitals a tenth of the picture's height:
YOUR HAND STOPS ACHING
HALFWAY THROUGH THE ROLL
Each callout label stands at least a sixteenth of the picture's height.

BADGE: lower LEFT, a flat cream rectangle with square corners, CORDLESS cut out of it in the
brown of the bench.

Nothing comes within a tenth of the picture's width of any edge. The words above are the only
words in the picture; no logo, no watermark, no person, no room.
```

---

## 3 — `06-relief-claimstack` · PRODUCT subject, flat field · badge `pill` · deep teal

Isolates the subject widening: the field is held at the known-good flat tone.

```
TYPE: 06-relief-claimstack v0.2
REGISTER: commercial editorial photograph on a flat field.

PRODUCT REFERENCE: the attached photo is the exact reference for the handheld dust mite
vacuum. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: the vacuum alone, cut out cleanly, three-quarter angle, nozzle to the lower left,
holding the right third of the picture.

FIELD: one flat deep teal filling the picture behind it. No gradient, no texture, no room, no
shadow under the cut-out.

LIGHT: soft and directional on the vacuum only, from behind and right, a faint rim on its
upper edge. The field is unlit and flat.

TEXT: in the empty field on the left, all flat white sans-serif, every line and glyph starting
the same distance from the left edge. The headline's capitals stand a tenth of the picture's
height; the three lines under it a sixteenth:
YOU CHANGE THE SHEETS.
NOTHING UNDER THEM CHANGES.
then, each with a small line glyph at its left —
a sun glyph — Works dry, so the bed is yours again by bedtime
a bed glyph — Goes into the surface, not just over it
a battery glyph — No cord to drag around the bed frame

BADGE: lower LEFT, a fully rounded white capsule with TEN MINUTES A BED in teal capitals
inside it.

Nothing comes within a tenth of the picture's width of any edge. The words above are the only
words in the picture; no logo, no watermark, no packaging, no person, no room.
```

---

## 4 — `06-relief-claimstack` · PERSON subject, real room · badge `seal` · lit wall

Isolates the field widening: the subject is held at the known-good person.

```
TYPE: 06-relief-claimstack v0.2
REGISTER: commercial editorial photograph in a real room.

PRODUCT REFERENCE: the attached photo is the exact reference for the hydraulic arm strength
trainer. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: a man in his forties in a plain grey t-shirt, seated on a low bench, working the
trainer with both hands at chest height, looking down at it. He holds the right half, cropped
at the thigh.

FIELD: a real living room behind him — a plain painted wall, daylight raking across it from a
window out of frame, a rug edge at the foot. The wall to his left is empty and thrown well out
of focus, and the words sit directly on it with no panel behind them.

LIGHT: plain daylight from the window side. No rim light, no studio key.

TEXT: on the out-of-focus wall at the left, all flat white sans-serif, every line and glyph
starting the same distance from the left edge. The headline's capitals stand a tenth of the
picture's height; the three lines under it a sixteenth:
THE GYM YOU KEEP MEANING
TO GO BACK TO
then, each with a small line glyph at its left —
a dial glyph — Turn it up the week it starts feeling easy
a counter glyph — The display counts, so you do not have to
a chair glyph — Done sitting down, in the room you are already in

BADGE: lower LEFT, on the out-of-focus floor, a white scalloped rosette with NOTHING TO RACK
in dark grey capitals curved inside it.

Nothing comes within a tenth of the picture's width of any edge. The words above are the only
words in the picture; no logo, no watermark, no poster or label in the room, no second person.
```

---

## 5 — `07-identity-pack` · CLOSED form · badge `roundel` · citrus-toned ground

```
TYPE: 07-identity-pack v0.1
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the portable juicer cup.
Preserve shape, proportions, material, finish, colour and every word printed on it exactly.

FORM: closed. The cup upright and complete with its lid on, nothing detached, nothing beside it.

SUBJECT: the face carrying the brand mark meets the lens, the cup turned a few degrees so its
depth reads. About half the picture's height.

SETTING: a soft pale citrus-yellow ground with a gentle vertical gradient, a soft contact
shadow beneath the cup. No room, no prop, no second object.

LIGHT: broad and even from the front and slightly above, strong enough that every word printed
on the cup stays legible.

TEXT: across the upper empty ground, two lines of flat deep grey sans-serif starting a tenth
of the picture's width from the left edge, capitals a tenth of the picture's height:
BREAKFAST THAT FITS
IN THE CUP HOLDER

BADGE: lower LEFT, a filled deep grey circle with 400ml in white inside it.

Nothing comes within a tenth of the picture's width of any edge. The two lines and the badge
are the only added words; the cup's own printed label is part of the object and stays exactly
as the reference shows it. No logo, no watermark, no person, no hand, no room.
```

---

## 6 — `07-identity-pack` · WITH CONTENTS form · badge `flash` · slate ground

```
TYPE: 07-identity-pack v0.1
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the rodent repellent balls
and their pack. Preserve shape, proportions, material, finish, colour and every word printed
on the pack exactly.

FORM: with contents. The pack upright and closed, four of the balls loose on the ground at its
lower left, none touching it.

SUBJECT: the face carrying the brand mark meets the lens. The pack takes about half the
picture's height; the loose balls sit small in front and give it its scale.

SETTING: a dark slate-grey ground with a faint stone texture, a soft contact shadow under the
pack and a fainter one under each ball. No room, no prop.

LIGHT: broad and even from the front and slightly above, strong enough that the pack's printed
words and the balls' surface both read.

TEXT: across the upper empty ground, two lines of flat white sans-serif starting a tenth of the
picture's width from the left edge, capitals a tenth of the picture's height:
NOTHING SNAPS. NOTHING DIES.
THEY JUST STOP COMING BACK.

BADGE: a white ribbon crossing the lower LEFT corner at forty-five degrees, with DROP AND WALK
AWAY in slate capitals along it.

Nothing comes within a tenth of the picture's width of any edge. The two lines and the ribbon
are the only added words; the pack's own printed label is part of the object and stays exactly
as the reference shows it. No logo, no watermark, no person, no hand, no room.
```

# Test prompts — six renders, three types

Ratio **1:1**, set at the tool. It never goes in the prompt (ADR-016, adapter Rule 4).
**Attach the product photo** where a prompt opens with PRODUCT REFERENCE.

Every product comes from `query/product-slugs.yaml` and none appears in any candidate's
source list. A rule that holds on a product it has never seen is a rule.

## Rewritten 2026-09-03, second pass — four owner findings, all measured

| finding | what was measured | what changed |
|---|---|---|
| the prompts are bloated | 1488–2128 chars against adapter Rule 6's 1450–1600 reference; 4 of 6 over | now **1431–1708** after the badge rewrite of the third pass — down from 1488–2128, four of six inside the reference band and two just over it. The closing negative ran ~40 words in every prompt and is now one line; the safe-area clause is stated once rather than per element |
| the badge is monotonous | 6 of 6 said "a small flat solid rectangle… in white capitals" | a badge is a MARK, not a text slot. Each type now owns a form library — tag, seal, pill, roundel, chip, flash — and each prompt names a DIFFERENT form, chosen from what the product's register carries |
| the background is monotonous | 6 of 6 said "one plain pale grey ground" | six different grounds, each picked from the product's own register |
| the text is too small | headline bands measured 5.0–6.1% of frame height, everything else 3.3–5.5% — **19–24px and 13–21px on a 390pt phone**, against a 17px platform floor | G16 gains a mobile floor, **anchored rather than numbered**: the capitals are as tall as a named thing in the frame — one earbud, the blade, the lid, a ball. See the second-pass note below; the first attempt stated a fraction and that is the class this renderer ignores |

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
left edge as the upper-left label. Each capital is as tall as one earbud is long, so the
headline is the first thing read:
UNDERSTAND EACH OTHER
BEFORE THE SENTENCE ENDS
Each callout label is half the height of those capitals.

BADGE: UPPER RIGHT, overlapping nothing but the ground. A filled circle in a bright signal
green, as wide as the charging case, with a white line icon of two speech bubbles in its upper
half and TWO LANGUAGES in white capitals across its lower half.

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
edge as the leftmost label. Each capital is as tall as the scissor blade is long:
YOUR HAND STOPS ACHING
HALFWAY THROUGH THE ROLL
Each callout label is half the height of those capitals.

BADGE: LOWER LEFT, a hard-edged rectangle in a hot signal red, as wide as the scissors' grip
is long, tilted a few degrees off square, with CORDLESS in white capitals filling it.

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
the same distance from the left edge. The headline's capitals are as tall as the vacuum's body
is wide; the three lines under it are half that height:
YOU CHANGE THE SHEETS.
NOTHING UNDER THEM CHANGES.
then, each with a small line glyph at its left —
a sun glyph — Works dry, so the bed is yours again by bedtime
a bed glyph — Goes into the surface, not just over it
a battery glyph — No cord to drag around the bed frame

BADGE: UPPER LEFT, overlapping the top corner of the headline's field, a fully rounded capsule
in warm gold, as wide as the vacuum's body is long, with TEN MINUTES A BED in deep teal
capitals filling it.

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
starting the same distance from the left edge. The headline's capitals are as tall as the
trainer's handle is long; the three lines under it are half that height:
THE GYM YOU KEEP MEANING
TO GO BACK TO
then, each with a small line glyph at its left —
a dial glyph — Turn it up the week it starts feeling easy
a counter glyph — The display counts, so you do not have to
a chair glyph — Done sitting down, in the room you are already in

BADGE: UPPER RIGHT, overlapping the man's shoulder, a scalloped rosette in deep gold with a
darker gold rim, as wide as his head, with NOTHING TO RACK in white capitals curved inside it.

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
of the picture's width from the left edge. Each capital is as tall as the cup's lid is deep:
BREAKFAST THAT FITS
IN THE CUP HOLDER

BADGE: LOWER LEFT, a filled circle in a hot coral, as wide as the cup's lid, with 400ml in
white filling it — the figure large enough to read before the cup does.

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
picture's width from the left edge. Each capital is as tall as one of the loose balls:
NOTHING SNAPS. NOTHING DIES.
THEY JUST STOP COMING BACK.

BADGE: a ribbon in a deep signal green crossing the UPPER LEFT corner at forty-five degrees,
as wide across as the pack, with DROP AND WALK AWAY in white capitals along it.

Nothing comes within a tenth of the picture's width of any edge. The two lines and the ribbon
are the only added words; the pack's own printed label is part of the object and stays exactly
as the reference shows it. No logo, no watermark, no person, no hand, no room.
```

---

## Second pass on the second pass, 2026-09-03

The owner rendered nothing and read the prompts instead, and said the badge was still
monotonous and the text still too small. Both were right, and both were checked before
anything moved.

**The badge fix had changed the wrong variable.** Six prompts used six different SHAPES, and
form was never what made a badge read. Three things were, and **not one of them existed
anywhere** — not in G16, not in any of the three MARKS libraries, not in any prompt:

| | before | now |
|---|---|---|
| size | **no size rule anywhere.** The only size word in six prompts was "small" | anchored to the product — as wide as the case, the grip, the lid, his head |
| position | **6 of 6 in the lower left** | upper right, lower left, upper left, upper right, lower left, upper left. Only the bottom-right is unavailable, and that is the watermark's |
| colour | **every badge borrowed a colour already in the frame** — white ×7, grey ×2 | signal green, hot red, warm gold, deep gold, coral, deep green. A badge that shares the picture's palette recedes into it |

**And the text fix was the third fixed number.** "A tenth of the picture's height" is a
fraction, and G10 already records that two fixed numbers failed at sizing an inset here — six
panels rendered "broadly compliant" and the owner still read them as too small — with its own
conclusion that *maximisation needs no measurement, which is why it is the rule*. Adapter Rule
4 is blunter: a written ratio does nothing to this renderer, 6 of 6.

What this library HAS measured working is an **anchor**: an arrow described by its endpoints
2/2, a badge whose glyph was named 2/2, hotspots tied to named places, alignment written as an
observable 4/4. So every size clause now reads *as tall as one earbud is long*, *as tall as the
scissor blade*, *as tall as one of the loose balls*. Mobile legibility comes from choosing a
big anchor.

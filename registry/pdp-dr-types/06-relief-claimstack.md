---
id: 06-relief-claimstack
step: 6
job: relief
device: claimstack
version: "0.4"
status: reserved
replaced_by: null
ratios: ["1:1", "4:3"]
channels: [landing-page]
requires_product_photo: false
generation_mode: single-pass
axes: {}
text_layer: [title, copy, badge]
variants: []
exempt_from: [G7, G11]
pairs_with: []
never_with: []
avoid_adjacent: [03-spec-claimstack]
requires_pair: null
blocked_by: "Criterion 2, the router-confusion test against 06-relief-hero. Criterion 1 is cleared at nine sources, and a type this common contests every outcome slot on every page."
---

# 06-relief-claimstack — STAGING DRAFT

Promotion status (2026-09-03, after batches F, G and H): **9 distinct sources — criterion 1
is CLEARED and by a wide margin.** mida-fernwell, holloway, redpine, dermadream, lw-womens,
ezy-talux, quietmex, retro-noxt, snif-rect: supplements, coffee, personal-care devices, audio
and consumer electronics. **Nine sources makes this the best-evidenced proposal this library
has ever held, active types included**, and the finding behind the number is worth stating:
a subject to one side with a headline and short claim lines filling the other is the single
most common argument image on a direct-response product page.

**Criterion 2 (router-confusion) is the binding gap**, and it is a real one — a type this
common will compete with `06-relief-hero` for every outcome slot on every page, and that test
has to be run before promotion rather than after. Criterion 3 now has FOUR renders across two
rounds, all four examined and graded by eye under ADR-011; §6.3(3) wants the owner's own
verdict and that is what is outstanding.

Superseded status line, kept so the count's history is legible: **2/5 exemplars** — `sha256:2da3d3182d3dbd8…`, a laughing
woman cut out against a pale green field beside a headline and four icon-and-claim lines;
and `sha256:4a3fbc492b392e5e4…`, the identical layout with the PRODUCT in the subject
position and no person at all. The second is why PARTS/subject below is too narrow as
drafted — see KNOWN-FLAKY.

Not routable. Device `claimstack` is new vocabulary.

**This draft existed to be TESTED rather than promoted, and the test has run twice — see
FOUNDING RENDER ROUND and SECOND RENDER ROUND. The paragraph below is left standing as the
reason it was written.** One observation is well below the bar. What earns it a place ahead of
better-evidenced proposals is that it is the single most common shape in the benefit slice
of the corpus — 181 `benefit-*` files across 13 of 13 products — and that rendering it
answers the one question the owner's Q1b decision turns on: **how many separate text
clusters does this renderer actually hold in one frame?** G16's drafted budget is one block
plus one badge, measured 3 of 3 in the founding round. The market tile this type copies
carries six. Everything else about the type is ordinary; the cluster count is the experiment.

## PURPOSE
Sell the state after buying by putting a person who has it beside the reasons, stated in the
frame. The picture half is a portrait carrying a feeling; the text half enumerates what the
feeling is made of. No product is required and usually none is present.

## TRIGGER
use_when: >
  The page needs one tile to carry both the promise and its reasons, and the reasons
  are short claims the copy already makes. The benefit block of a product page, a
  gallery tile between the ingredient tiles and the reviews, or a closing tile before
  the offer. Use when the product's benefit is a felt state rather than a visible
  result — energy, calm, focus, comfort — so that a face is the only available
  evidence. Where the result IS visible on a body or an object, take a relief type
  that can show it instead.

## SKELETON
```
TYPE: 06-relief-claimstack v0.4
REGISTER: commercial editorial photograph on a flat coloured field.

[SUBJECT]   one person carrying the state, cut out.        -> PARTS/subject
[OFFSET]    the subject holds one side; the words the other. -> PARTS/offset
[FIELD]     one flat tone behind everything.               -> PARTS/field
[LIGHT]     warm and directional on the subject only.      -> PARTS/light

[TITLE]     the promise.                                    -> G16/title
[COPY]      the reasons, as a stack of short lines.         -> G16/copy + PARTS/stack
[BADGE]     one short stamp. Bottom LEFT.                  -> MARKS
```

## PARTS

**`subject`** — choose ONE. A **person** carrying the state, or the **product** itself, or the
product **in use** — a hand holding it, a glass being made, a device being worn. Whichever it
is, it occupies one third to one half of the frame at one side and nothing else competes with
it.

**The subject slot was written around a person and nine sources say it is wider than that.**
Four of the nine put a product where the draft put a face — capsules, a neck device, a
mouthpiece, a headset — and the argument does not change: the claims still carry the reasons
and the subject still carries the promise. This is corrected here rather than left in
KNOWN-FLAKY because four independent sources is past the evidence rule twice over.

**The product form is now RENDERED, 1 of 1, and it is the cleaner of the two.** A cut-out
vacuum on a flat deep-teal field carried the promise with no face in the frame and nothing
was lost: five clusters, every word exact, no duplication. Where the subject is the product
there is no G9 tension, no G13 exposure and no cut-out-person edge to go wrong — three
failure modes the person form carries and this one does not.

**Where the subject IS a person, G9 is in tension and the tension is real:** G9 ranks a visible
symptom or result above a face and says emotion on a face is not evidence. This type has no
visible result by definition — that is its trigger — so the face is the only rung of G9's
ladder available. Where a result IS visible, G9 says take another type, and the trigger above
says the same thing in different words. **Where the subject is the product, G9 is not engaged
at all**, which makes the product form the safer of the two and is worth knowing.

**`offset`** — the subject occupies one third to one half of the frame at one side; the words
occupy the rest. **The field between them is empty by construction and nothing else may claim
it** — two reservations for one area render as dead air, measured 2 of 2 on `06-relief-hero`.

**`field`** — what the words sit on. Three forms, all observed, and the clause that binds all
three is **legibility, not flatness**:

- **flat tone** — one colour, no gradient, no texture, the subject cut out and placed on it.
  The easiest to keep legible. The corpus builds this form on sage, sand, cobalt, cream, pale
  blue and warm beige — **and note what those six have in common: every one is LIGHT and
  low in saturation.** The instruction here used to be "chosen from the product's own
  register rather than reached for", and the founding round obeyed it into a fully saturated
  deep teal, 0.90 saturation against a corpus median of 0.06 across 119 frames. Choosing from
  the product's register is right about HUE and was read as licence for depth and intensity.
  The tone is light and quiet; a dark or saturated field is a choice the prompt justifies,
  and a tone that could belong to any product in the category is still a tone nobody chose.
- **a real room** — the subject photographed in place, the words set into the room's own
  out-of-focus area. Three sources build it this way; one puts the words straight onto the
  wall with no panel at all. **Rendered, 1 of 1, in its hardest form**: white words straight
  onto a daylit out-of-focus wall, no panel, no scrim. They read. What made them read is that
  the wall was thrown far enough out of focus to carry no detail at all — the clause to keep
  is the DEFOCUS, not the panel.
- **a band** — the photograph occupying two thirds and the claims a solid band beneath,
  with the product cut out across the boundary.

**The flat-tone-only clause was wrong and this corrects it.** It existed to keep the words
legible; a blurred room does that job, and a real room buys context the flat field throws
away. What still binds is that the area the words occupy carries nothing else — G16's
never-reserve-space-you-do-not-fill rule applies to all three forms equally, and the flat
field is the one most able to invite the duplication G16 measured.

The tone or the room is a runtime value (`parameters: environment`).

**`light`** — warm and directional on the subject, usually from behind so hair and shoulder
carry a rim. The field is flat and unlit; lighting the field turns the cut-out into a badly
composited photograph.

**`stack`** — the reasons, **one line each, in the order the copy ranks them**, every line
beginning at the same distance from the left edge of the picture. Each line may carry one
simple line-drawn glyph at its left. **How many lines this type may carry is the open question
and is set by G16, not here** — see KNOWN-FLAKY.

## MARKS

**A badge is a mark and this type owns its forms** (ADR-012, ADR-043, G16's badge note). The
skeleton calls `badge` by name; the prompt names WHICH form, and the choice is made per
product from what its register can carry. **Three forms minimum, and none of them is a
default** — six test prompts written before this section existed produced six identical flat
rectangles, which is the monotony that put this section here.

| form | shape | the register it belongs to |
|---|---|---|
| `tag` | a flat rectangle, capitals cut out of the fill | anything that reads as engineered or clinical |
| `seal` | a scalloped rosette or a shield, a short line curved inside it | a guarantee, a standard, a promise about the seller. **Reads as authority, which is exactly why G16 refuses a certification mark in one** |
| `pill` | a fully rounded capsule, a short line inside | soft categories — supplements, personal care, anything domestic |
| `chip` | a small line icon in a circle with one short label beneath | a capability where the icon carries half the reading |

**One badge per frame**, and it never repeats a line the stack already carries.
**Three corners are open and the bottom-right is not**, per `adapters/nano-banana.md` Rule 7
— that corner carries the tool's watermark. The second round asked for upper left and upper
right and got both, 2 of 2.
**Tested: `tag` 2 of 2, `pill` 1 of 1, `seal` 1 of 1**, all clean. Only `chip` has no render.
**The badge's size anchor works and the headline's does not** — `pill` came back at 0.71 of
the object it was told to match and `seal` at 0.96, against 0.13 and 0.24 for the headlines
in the same frames. G16 carries the general form; here it means the badge clauses can be
trusted as written.
**A badge must not take its colour from the product.** Round 2 asked for a warm-gold `pill`
on a champagne-gold vacuum and got exactly that — a badge the same hue as the thing it sits
beside. Nothing in the render failed; the PROMPT broke G16's own rule that a badge carries a
colour the photograph does not, and it broke it because the writer read the colour off the
product. Choose the badge hue against the frame, never from it.

**A badge is not FLAT and it is not ONE WORD AT ONE SIZE** (G16, round 4, 2026-09-03). The
table above describes an OUTLINE; it said nothing about the interior, and five of six
founding-round badges came back with a value spread of 0.02–0.09 — dead flat — against
0.10–0.35 on four corpus badges. The only render that was not flat is the only one whose
prompt named a second tone. What every badge in this type owes:

- **at least one internal tone step** — a rim, a concentric ring, an outline inset from the
  edge, or a sheen across the fill;
- **at least two type sizes** — corpus badges run 2 to 4; the six renders ran 1 to 2, and
  3 of 6 carried a single line of type at a single size.

A figure large, its label smaller, a qualifier smaller still, and often a glyph. That is a
small composition, and it is what makes a stamp read as a stamp rather than as a label.

## SLOT CONSTRAINTS
- **Every word comes from the page's own copy.** G16's content rule binds hardest on this type,
  because a claim stack is nothing but claims: four lines of invented benefit baked into a file
  that outlives the page is the failure mode this type is most able to produce.
- **No regulatory footnote, no asterisk, no disclaimer.** The market tile carries one and this
  type may not: a disclaimer is legal furniture whose wording changes by market and by year, and
  it belongs in page HTML beside the image. This is the one place the type deliberately refuses
  to copy its own exemplar.
- **No product, no packaging, no capsule.** If the product must appear, the frame is
  `06-relief-hero`'s and this type is the wrong one.
- **G11 exemption.** G11 sets the absolute grade of a single-state frame, and this type's field
  is a brand tone rather than a graded state. The subject is graded warm; the field is not
  graded at all.
- **G7 exemption** — a cut-out person on a flat field is not a scene and G7's three tests have
  nothing to bind to.
- **G13 binds without exemption** where the subject could read as young.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a room, a real background, a gradient field, a drop shadow under
the cut-out, a product, packaging, a disclaimer line, an asterisk,
a second person, a photographic texture behind the words
```

## WORKED EXAMPLES
### example: dust-mite-vacuum-product-subject — skeleton@0.2, run: pass
Isolates `PARTS/subject` as ADR-066 widened it: the PRODUCT in the subject slot, field held at the known-good flat tone. Five clusters, 6 of 6 lines exact, no duplication, no face in frame and nothing lost. `sha256:9df23c4bfb119485…`

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

### example: arm-trainer-person-in-room — skeleton@0.2, run: partial
Isolates `PARTS/field` as ADR-066 widened it: words straight onto a daylit out-of-focus wall, no panel, subject held at the known-good person. They read. One claim line gained a word — `The display counts reps` for `The display counts` — and the badge sits 3.71% from an edge. `sha256:0d47d3e4d0d6c289…`

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

## KNOWN-FLAKY
- **The cluster count is ANSWERED and the answer was the opposite of the question.** Five
  clusters held, 13 of 13 words exact. Two clusters DUPLICATED. What binds is the fill, not the
  count — G16 now carries the rule. This type's own risk is therefore a SHORT stack: a headline
  with one claim under it in a half-frame reservation is the shape that repeats.
- **The cut-out person is tested and clean, 2 of 2** — no halo, no drop shadow, warm rim on the
  subject with the field left unlit. This was listed as the type's second risk and is now its
  least.
- **A prompted LINE BREAK is not binding**, 1 of 1: a two-line headline was re-wrapped to
  three. Write the words and let it wrap; a break that has to hold is not something this
  renderer can be asked for.
- **A claim line can gain a word**, 1 of 34 lines across the round: `The display counts, so
  you do not have to` came back as `The display counts reps, …`. Not a misspelling and not a
  drop — an insertion that reads as an improvement and is still a word the page did not
  write. G16's content rule is the one this threatens.
- **The short-stack duplication risk is still this type's own**, and the round did not test
  it — both frames ran five clusters. Two-cluster frames were rendered on `07-identity-pack`
  in the same round and did NOT duplicate, because their headline filled the band it was
  given. That is consistent with G16's fill rule rather than a reprieve for a short stack.
- Superseded, kept for the record: *"One observation. Two of the four things above could turn
  out to be one thing."* The count is nine and the two widened clauses each have a render.

## FOUNDING RENDER ROUND — 2026-09-03
Two renders, ratio 1:1, two different subjects and two different budgets, so a failure could
not be confounded by re-running one product. **The result inverted the hypothesis.**

| | 2 clusters (woman, sage field) | 5 clusters (man, sand field) |
|---|---|---|
| verdict proposed | **fail** | **pass** |
| words exact | yes, but | **13 of 13** |
| clusters returned | **the whole block TWICE** | all five, once each |
| glyphs | none asked | 3 of 3 drawn, aligned with the headline |
| badge, bottom left | clean | clean |
| margins | 7.3% L, 8.1% T | 6.8% L, 6.6% B |

**The two-cluster frame drew its text block a second time**, lower and re-wrapped — measured
as seven separate ink bands in the left half where four were asked for. The five-cluster frame
declared the same area and filled it, and nothing repeated.

**So the constraint is not the count, it is the fill.** This type's `offset` reserves one third
to one half of the frame for the words and calls the rest of the field empty; a short block in
that reservation leaves the renderer space it will fill by repeating what it already drew. The
mechanism is already in `adapters/nano-banana.md` Rule 4 for panels — "the model fills the
vertical space it has by repeating what it already drew" — and this is the first time the
library has seen it in text. G16 now carries the rule; this type carries the risk, because a
claim stack with a short headline and no claims is exactly the dangerous shape.

**The cut-out person worked, 2 of 2** — clean edges on a flat field, no halo, no drop shadow,
warm rim light on the subject with the field left unlit. That was listed as untested and is now
the least of this type's problems.

## SECOND RENDER ROUND — 2026-09-03
Two renders, ratio 1:1, prompts 3 and 4 of `registry/pdp-dr-types/ready-to-push/prompts.md`. **Each
isolates ONE clause widened by ADR-066**, with the other held at its known-good value, so a
failure could attribute. Both products come from `query/product-slugs.yaml` and neither is in
this type's source list. Verdicts by eye under ADR-011.

| | 3 · PRODUCT subject, flat field | 4 · PERSON subject, real room |
|---|---|---|
| the clause under test | `PARTS/subject`, widened on 4 sources | `PARTS/field`, widened on 3 |
| verdict by eye | **pass** | **partial** |
| clusters asked / returned | 5 / 5 | 5 / 5 |
| words exact | 6 of 6 lines | **5 of 6** — one line gained a word |
| headline cap | 50 px = 4.88% of frame | 52 px = 5.08% |
| headline ÷ its anchor | **0.13** | not separable |
| badge form, corner asked / got | `pill`, upper left / upper left | `seal`, upper right / upper right |
| badge ÷ its anchor | **0.71** | **0.96** |
| closest prompted ink to an edge | 6.05% text · 6.05% badge | 5.76% text · **3.71% badge** |
| output | `sha256:9df23c4bfb119485…` | `sha256:0d47d3e4d0d6c289…` |

**Both widened clauses hold.** The product in the subject slot carried the promise with no
face in the frame; the words on a defocused wall with no panel stayed legible. ADR-066
widened both on source counts alone and each now has a render behind it.

**Render 3 is the better frame and the reason is structural.** With the product as subject
there is no G9 tension to manage, no G13 exposure and no cut-out edge to go wrong. The
person form is not worse-rendered — it is worse-EXPOSED.

**Two faults, and neither is about the widening.**

- **The headline was given two lines and drew three.** A break in the prompt is a suggestion.
- **One claim line gained a word** — `The display counts` came back as `The display counts
  reps`. It reads better and the page did not write it, which is exactly the shape G16's
  content rule exists to catch: an improvement is still an invention.

**The badge is where G10 breaks.** Render 4's `seal` came within 3.71% of an edge while its
own text block held 5.76%. The badge goes precisely where the prompt puts it, and a corner
plus an anchored size is a combination that walks off the frame.

## NOTES
**Why this is `relief` and not a new job.** The argument is the state after buying, which is
step 6's own definition; the enumeration is how the tile is BUILT, not what it argues. A device
names the mechanism and `claimstack` is the mechanism: a subject beside a stack of claims.

## BLOCK
**Waiting on criterion 2, the router-confusion test against `06-relief-hero`.** Criterion 1 is
cleared at nine distinct sources — the best-evidenced proposal this library has ever held,
active types included — and that is exactly why the test binds: a subject to one side with a
headline and claim lines filling the other is the commonest argument image on a
direct-response product page, so it will contest every outcome slot with an active type. ADR-066
recorded the refusal to promote on that basis and it stands.

**Criterion 2 is now a NAMED PAIR:** `03-spec-claimstack`, 8 sources, same picture with a
capability claim instead of a felt state (ADR-078).

`07-identity-callout` re-filed four observations here and was retired 2026-09-11. Still not
new sources until the re-filing pass runs.

## CHANGELOG
- 0.4 (2026-09-03): owner audit of the second round — colour. `PARTS/field`: the flat tone is
  LIGHT and low-saturation; deriving it from the product's register governs hue, not depth.
  Measured — this type's own render came back at 0.90 saturation against a corpus median of
  0.06 over 119 frames. `MARKS` gains the badge INTERIOR: one internal tone step and two type
  sizes minimum. The `seal` rendered here is the one non-flat badge of six, and the only one
  whose prompt named a second tone. ADR-068.
- 0.3 (2026-09-03): second render round, 2 renders — `sha256:9df23c4bfb119485…`,
  `sha256:0d47d3e4d0d6c289…`. Each isolates one clause ADR-066 widened; both hold, 1/1 each.
  MARKS: bottom-left constant becomes three open corners, 2/2 obeyed; `pill` and `seal`
  tested; a badge may not take its colour from the product, breached by the prompt 1/1.
  KNOWN-FLAKY gains a re-wrapped line break 1/1 and an inserted word 1/34.
- 0.2 (2026-09-03): `PARTS/subject` widened from a person to a person, the product, or the
  product in use, on four of nine sources; `PARTS/field` widened from one flat tone to flat
  tone, a real room, or a band, on three sources, with legibility as the binding clause.
  Source count 2 → 9, criterion 1 cleared. Entry written retrospectively at 0.3: ADR-066
  bumped the version and recorded the reasoning in the log but wrote no CHANGELOG line.
- 0.1 (2026-09-03): drafted from one observation, `sha256:2da3d3182d3dbd8…`, deliberately ahead
  of better-evidenced proposals because it is the corpus's commonest benefit shape and because
  rendering it settles G16's cluster budget. Flagged throughout as an experiment rather than a
  candidate.

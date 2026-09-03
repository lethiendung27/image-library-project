---
id: 06-relief-claimstack
step: 6
job: relief
device: claimstack
version: "0.2"
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
avoid_adjacent: []
requires_pair: null
---

# 06-relief-claimstack — STAGING DRAFT

Promotion status (2026-09-03, after batches F, G and H): **9 distinct sources — criterion 1
is CLEARED and by a wide margin.** mida-fernwell, holloway, redpine, dermadream, lw-womens,
ezy-talux, quietmex, retro-noxt, snif-rect: supplements, coffee, personal-care devices, audio
and consumer electronics. **Nine sources makes this the best-evidenced proposal this library
has ever held, active types included**, and the finding behind the number is worth stating:
a subject to one side with a headline and short claim lines filling the other is the single
most common argument image on a direct-response product page.

Criterion 3 MET at `pass` on the five-cluster form. **Criterion 2 (router-confusion) is now
the binding gap**, and it is a real one — a type this common will compete with
`06-relief-hero` for every outcome slot on every page, and that test has to be run before
promotion rather than after.

Superseded status line, kept so the count's history is legible: **2/5 exemplars** — `sha256:2da3d3182d3dbd8…`, a laughing
woman cut out against a pale green field beside a headline and four icon-and-claim lines;
and `sha256:4a3fbc492b392e5e4…`, the identical layout with the PRODUCT in the subject
position and no person at all. The second is why PARTS/subject below is too narrow as
drafted — see KNOWN-FLAKY.

Criterion 3 MET at `pass` on the five-cluster form — one render, owner-verdict pending.
Criterion 2 not run. Not routable. Device `claimstack` is new vocabulary.

**This draft existed to be TESTED rather than promoted, and the test has run — see FOUNDING
RENDER ROUND. The paragraph below is left standing as the reason it was written.** One observation is well below the bar. What earns it a place ahead of
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
TYPE: 06-relief-claimstack v0.1
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
  The easiest to keep legible and **the one to stop defaulting to**: the corpus builds this
  form on sage, sand, cobalt, cream, pale blue and warm beige, and the tone is chosen from the
  product's own register rather than reached for. A tone that could belong to any product in
  the category is a tone that has not been chosen.
- **a real room** — the subject photographed in place, the words set into the room's own
  out-of-focus area. Three sources build it this way; one puts the words straight onto the
  wall with no panel at all.
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
| `tag` | a flat rectangle, one flat fill, capitals cut out of it | anything that reads as engineered or clinical |
| `seal` | a scalloped rosette or a shield, a short line curved inside it | a guarantee, a standard, a promise about the seller. **Reads as authority, which is exactly why G16 refuses a certification mark in one** |
| `pill` | a fully rounded capsule, one flat fill, a short line inside | soft categories — supplements, personal care, anything domestic |
| `chip` | a small line icon in a circle with one short label beneath | a capability where the icon carries half the reading |

**One badge per frame**, and it never repeats a line the stack already carries.
**The badge sits bottom LEFT**, per `adapters/nano-banana.md` Rule 7 — the tool's watermark
holds the other corner.
**Tested only as `tag`**, 2 of 2 clean in the founding round. The other three forms have no
render and their first is their founding evidence.

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

## KNOWN-FLAKY
- **The cluster count is ANSWERED and the answer was the opposite of the question.** Five
  clusters held, 13 of 13 words exact. Two clusters DUPLICATED. What binds is the fill, not the
  count — G16 now carries the rule. This type's own risk is therefore a SHORT stack: a headline
  with one claim under it in a half-frame reservation is the shape that repeats.
- **The cut-out person is tested and clean, 2 of 2** — no halo, no drop shadow, warm rim on the
  subject with the field left unlit. This was listed as the type's second risk and is now its
  least.
- **One observation.** Two of the four things above could turn out to be one thing.

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


## NOTES
**Why this is `relief` and not a new job.** The argument is the state after buying, which is
step 6's own definition; the enumeration is how the tile is BUILT, not what it argues. A device
names the mechanism and `claimstack` is the mechanism: a subject beside a stack of claims.

## CHANGELOG
- 0.1 (2026-09-03): drafted from one observation, `sha256:2da3d3182d3dbd8…`, deliberately ahead
  of better-evidenced proposals because it is the corpus's commonest benefit shape and because
  rendering it settles G16's cluster budget. Flagged throughout as an experiment rather than a
  candidate.

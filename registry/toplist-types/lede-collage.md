---
id: lede-collage
version: "0.5"
status: active
replaced_by: null
products_in_frame: many
requires_product_photo: true
awareness: [product-aware, most-aware]
text_layer: [title, badge]
copied_from: null
copied_at_version: null
blocked_by: null
exempt_from: [G7]
---

# lede-collage

## PURPOSE
The five as an index: cut-outs on a flat ground, arranged for reading rather than
photographed together. It claims nothing about possession — only that these are the
entries.

## TRIGGER
use_when: >
  The reader wants the shortlist at a glance and the page's value is the selection
  rather than the testing. The input carries three or more distinct competing products.
  Take it over lede-lineup where the units are too unlike each other in size to share a
  surface honestly, or where no plausible single surface exists for the category.

## BOUNDARY
**Against `lede-lineup`** — assembled against photographed, enumeration against
possession. See that file; the distinction is stated there once and is not restated here.

**The overlay text IS part of this type** (ADR-071). Good Housekeeping and Dotdash
Meredith collages carry "BEST X" across the frame, and the corpus agrees: **2 of the 3**
observations that are actually several products carry an award badge over the cut-outs.
(Five records name this type; two are variant-candidates of a different shape — two views
of ONE product, and three outfits on one person — so the denominator for the type as
defined is three, not five. The file shipped 2 of 5 this morning and that was wrong.) `text_layer: [title, badge]`, so
**G16 binds every word and the badge here** — the line cap, the badge interior, the
mobile floor, the watermark corner.

What may be printed is the page's own line about its own ranking. **The two award marks in
the corpus are a publisher's own mark on that publisher's own page** (`CNET LAB TEST
WINNER`, `CNET PEOPLE'S PICKS`); reproducing another party's is the trademark question
`toplist-instruction.md` records as still unanswered.

## SKELETON
```
TYPE: lede-collage v0.5
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES]  one attached photo per unit.                      -> G1, and see BLOCK
[CUT-OUTS]            3-5 units, each cleanly cut out, no shared scene.
[ARRANGEMENT]         a reading order the eye can follow; no unit favoured.
[GROUND]              a DESIGNED field: light and saturated.  -> PARTS/ground
[SHADOW]              a faint contact shadow per unit or none at all, applied equally.

[TITLE]               the page's own line about its own ranking. Optional. -> G16/title
[BADGE]               one mark, the page's own verdict. Optional.          -> G16/badge
```

**G7 exemption, narrow.** Cut-outs on a flat ground are a graphic layer rather than a
scene, which G7's own scope note already reads that way for a product knockout. Every
other G7 test still binds.

## PARTS

**`ground`** — a DESIGNED field, **gradient or flat**. Measured on this namespace's own
corpus and nothing imported (ADR-073): **texture 1.9**, value 0.90, saturation 0.49 with
**5 of 5 above 0.34**.

- **Perfectly smooth.** No grain, no texture, no paper, no vignette. Texture 1.9 against
  7.1 for the photographed families is the single measurement that separates the two halves
  of this namespace.
- **Light AND strongly coloured** — both together, since a dark saturated field and a light
  quiet field are each only half of what the corpus does.
- **Either a two-hue diagonal gradient or one flat tone, and nothing in between.** Three of
  the five travel roughly half the colour wheel corner to corner — 177°, 175° and 177° of
  hue spread on a diagonal axis: green to red, purple to teal, magenta to orange. The other
  two hold a single tone under 13°. A prompt picks one form and names it.

**`title`** — two forms are observed and they are not the same idea:

- **over the empty band** — the line sits in ground the units do not occupy. The safe form,
  and the one the first prompt used.
- **behind the units** — oversized type running under the cut-outs, which overlap and crop
  it. Observed once, on the laptops frame where the word LAPTOPS is set larger than the
  products and partly hidden by them. It is the more editorial of the two and it puts the
  headline in direct competition with the subject; untested here, and named so a prompt can
  ask for it deliberately rather than produce it by accident.

## MARKS

**The type owns the badge's FORM; G16 owns its WORDS.**

| form | shape | observations |
|---|---|---|
| `plaque` | a rectangle with a rule across it, a short line above and a year below | **2** — both corpus badges take this form |
| `sticker` | a die-cut circle sitting on the ground, often tilted | 1, on the winner frame rather than a collage |
| `band` | a horizontal band across the frame | 0, untested |

**The badge MAY sit over one unit, and the no-favoured-unit law does not stop it.** Both
corpus badges do exactly that — one is placed over the centre unit. The law in
`ARRANGEMENT` governs SIZE, HEIGHT, POSITION and LIGHT, which is what would decide the
comparison before the reader does; a mark placed over one unit is the page saying which one
won, which is this type's job in a way it is not `lede-lineup`'s. **That distinction is
1 of 1 reasoning against 2 of 2 observations and it is the thing to check first in a render
round**, because if the badge reads as favouring rather than as naming, the law was right
and this paragraph is wrong.

**A badge is not flat and it is not one word at one size** (G16, ADR-068). The table above
is an OUTLINE; the interior owes:

- **at least one internal tone step** — a rim, a ring, an outline inset from the edge, or a
  sheen. Measured on the direct-response round: 5 of 6 library badges came back dead flat
  at 0.02–0.09 value spread against 0.10–0.35 on four market badges, and the one that was
  not flat is the only one whose prompt named a second tone.
- **at least two type sizes.** Every corpus mark in this namespace carries them — a label
  over a big word, or a word over a year.
- **a colour the photograph does not have.** Harder here than anywhere else in the library,
  because this type's ground is a saturated designed field: the badge has to clear the
  ground as well as the product.

## NEGATIVE
```
[G6] + a favoured unit, a rank number, a badge, a podium, a scene, a person,
a drop shadow under one unit only, a price, a brand logo, a certification seal,
a press logo, a third-party award mark, a fabricated rating or star row
```

## ATTACHMENTS

**One reference photo per unit in frame, and the prompt names which is which.** The
attachment cap of one was lifted at ADR-076 (owner instruction, 2026-09-09): a prompt
still makes ONE generation call and assembles nothing afterwards, but it may carry as many
references as it has products.

**Where the owner's own app takes only one, the prompt still ships in full** and is
rendered elsewhere. A prompt is never trimmed to fit a tool — that was the instruction, and
it is why this type went from `reserved` to `active` without anything about the picture
changing.

**Brands may be depicted, not invented** (ADR-075). With references attached, the units are
the real named products and `SPEC.md` §6.4's competitor clause does not bind this
namespace. With no reference attached the units stay unbranded, because a generated logo is
a fabricated brand.

**A note this type owes and `lede-lineup` does not.** With the two loud award frames
re-filed to `lede-winner` at ADR-074, this type has **one** corpus observation of what it
actually defines — several distinct products, cut out, on one designed ground. Five of its
six records are two other shapes it has been absorbing: three of *several views of ONE
product* and two of *one subject in several states*. It is active and it is thin, and the
split is a curation problem nobody has taken yet.

## CHANGELOG
- 0.5 (2026-09-09): **reserved → active** (ADR-076, owner instruction), on the same two
  blockers clearing as `lede-lineup`. `BLOCK` becomes `ATTACHMENTS`, and the file now
  records that it holds ONE observation of the type as defined — the other five are two
  shapes it has been absorbing since ADR-074 moved the award frames out.
- 0.4 (2026-09-09): `PARTS/ground` **rewritten from this namespace's own 32 frames**, no
  rule imported (ADR-073, owner instruction). Adds what a prompt needs and 0.3 did not
  carry: smoothness as a measurement, and the gradient's FORM — 3 of 5 are two hues roughly
  opposite on the wheel running diagonally at 175-177° of spread, 2 of 5 are one flat tone
  under 13°, and nothing sits between the two forms.
- 0.3 (2026-09-09): owner audit. **`PARTS/ground` added and it reverses half of what 0.2
  shipped**: this type's corpus runs saturation 0.49 with 5 of 5 above 0.25, against
  ADR-068's 0.06 measured elsewhere. **`PARTS/title`** records the second observed form —
  oversized type BEHIND the units. **`MARKS` added**, with the badge permitted over one
  unit against the no-favoured-unit law, on 2 of 2 observations and flagged as the first
  thing a render round should check. The "2 of 5" figure shipped this morning is corrected
  to 2 of 3: two of the five records are variant-candidates of a different shape.
- 0.2 (2026-09-09): `text_layer: [title, badge]` (ADR-071, owner instruction) — the
  "BEST X" overlay is the market form and 2 of 5 corpus observations carry a badge, so it
  is part of the type rather than banned from it. G16 now binds this file. **Still
  `reserved`**: its blocker was never the text, it is the one-reference-photo limit
  against `products_in_frame: many`.
- 0.1 (2026-09-09): drafted `reserved`. Kept separate from `lede-lineup` on SPEC §3.1 —
  two arguments — and flagged in that file as the one to merge away if a render round
  shows readers take the same meaning from both. ADR-069.

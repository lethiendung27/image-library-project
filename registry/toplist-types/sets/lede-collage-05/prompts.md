# `lede-collage` set 5 — a graphics layer, and a clause that should have existed since set 1

Written against **`lede-collage` v0.13`**. Owner, 2026-09-09: *"kettle bị sai. chưa có nhiều
graphic element linh hoạt, hiệu ứng."*

## The kettle fault is three sets old and nothing ever guarded against it

Set 3 cell 5 printed **TRAVEL KETTLES** on its badge. The hero is a collapsible silicone
travel kettle; the other four are **ordinary kitchen kettles** — a gooseneck pour-over, a
1.7-litre plastic jug, a black digital kettle, a corded steel one. Four of five are not the
category the frame names.

| set | asked for | came back as |
|---|---|---|
| `lede-authority` set 5 | five running watches | dress chronographs on steel bracelets |
| `lede-collage` set 3 cell 5 | five travel kettles | one travel kettle, four kitchen kettles |

**No prompt this library has ever written required the units to be plausible for the category
it prints.** Every cell below now does, as a binding constraint rather than a hope, and it
applies to all five units rather than to the hero.

That matters beyond craft: a badge reading TRAVEL KETTLES over four kettles that do not
travel is a claim the picture contradicts, which is `argument-faults.md` territory rather
than styling.

## The graphics layer, counted rather than invented

`PARTS/graphics` is new at 0.13. Six elements are counted off frames actually seen, and two
more are borrowed from `lede-winner`'s corpus and have never been asked for in a collage:

| element | observations |
|---|---|
| `glyph-field` — a regular field of small repeated symbols | 2 |
| `cut-corner-frame` — a thin rule with notched corners | 2 |
| `halftone` — a dot screen on the ground, products clean | 1 |
| `outline-echo` — a thin outline repeating a silhouette, offset behind it | 1 |
| `corner-label`, `icon-pair` | 1 each |
| *borrowed:* dotted silhouette outline, radiating arcs | 0 here |

**They stack** — the corpus `split-frame` pair carry a glyph field AND a keyline together.
What they may not do is cross a product's face.

## The cells

| cell | products | layout | graphics stacked |
|---|---|---|---|
| 1 | 5 bike lights | `colour-cells` | `outline-echo` + `corner-label` |
| 2 | 5 dash cams | `blocks` | `glyph-field` + `cut-corner-frame` |
| 3 | 5 desk chairs | `rounded-cells` | radiating arcs behind the hero + `halftone` |
| 4 | 5 humidifiers | `open` gradient | dotted silhouette outlines + `icon-pair` |
| 5 | 5 action cameras | `outlined-panels` | `cut-corner-frame` + `glyph-field` + `halftone` — three at once |
| 6 | 5 yoga mats | `colour-cells` | **NONE — CONTROL** |

**Cell 5 stacks three** to find the ceiling: at some number of layers the frame stops reading
as an index and becomes decoration with products in it.

**Cell 6 carries no graphics at all** — cells, hero, badge and nothing else. It is set 4 cell 3's
construction, and it exists so that "more graphic elements" can be judged against "none"
rather than against memory.

Thirty products, none used in sets 1–4. Five attachments each; **the first attachment is the
page's own product**. All six render elsewhere (ADR-076).

---

## 1 — five bike lights · `colour-cells` · `outline-echo` + `corner-label`

```
TYPE: lede-collage v0.13 — SET 5 CELL 1
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every light is clean and as-new — lenses clear, mounts unmarked.
[LAYOUT]    five rectangular cells of UNEQUAL size tiled edge to edge with no gaps, one
            light per cell, each cut out and scaled to fill its own cell.
[HERO]      the FIRST attachment is rendered clearly LARGEST, in the largest cell.
[PALETTE]   five DIFFERENT hues, one per cell. Every one is BOTH light AND strongly coloured
            at once: NOT pastels, tints or washed tones; NOT deep, dark or muted ones.
[GRAPHICS]  behind each light, a thin outline echoing that light's own silhouette, offset
            up and to one side in a deeper shade of its cell's colour. Plus a small
            corner-label in the lower left: the word PICKS with a short rule as its tail.
[BADGE]     form `roundel`: a scalloped disc, upper right, in a colour NO CELL carries.
            THREE type levels — a small label arced along the top of the rim, a large word
            across the middle, a year small beneath. A star device under the year. An inner
            ring inset from the rim. A soft shadow. Words: BEST OVERALL, BIKE LIGHTS, 2026.
[SHADOW]    a faint contact shadow beneath each light, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are bike lights — a lamp that mounts to a bicycle. Not torches, not head
  torches, not lanterns, not car lamps.
· No graphic element crosses the face of any product; outlines sit behind, labels beside.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence. Only the first is favoured.
· Every letter sits inside its own shape with visible margin; nothing touches a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## 2 — five dash cams · `blocks` · `glyph-field` + `cut-corner-frame`

```
TYPE: lede-collage v0.13 — SET 5 CELL 2
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every camera is clean and as-new — lenses clear, housings unmarked.
[LAYOUT]    flat blocks of colour of UNEQUAL size overlapping across the frame at slight
            angles, the five cameras laid across them. Flat shapes on one plane, no
            perspective and no thickness.
[HERO]      the FIRST attachment is rendered clearly LARGEST and sits OFF CENTRE.
[PALETTE]   four DIFFERENT hues across the blocks. Every one is BOTH light AND strongly
            coloured at once: NOT pastels, tints or washed tones; NOT deep, dark or muted.
[GRAPHICS]  a regular field of small repeated glyphs across the whole ground behind the
            blocks — ticks and crosses in a tone slightly deeper than the ground. Plus a
            thin rule with notched corners drawn around the hero's block only.
[BADGE]     form `shield`: a crest with a pointed base, in a colour NO BLOCK carries.
            THREE type levels — a small label across the top with a rule either side, a
            large word in the middle, a year small at the point. A bevel inset from the
            shield's edge and a soft shadow. Words: BEST OVERALL, DASH CAMS, 2026.
[SHADOW]    a faint contact shadow beneath each camera, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are dash cams — a camera that mounts inside a car to record the road.
  Not action cameras, not security cameras, not webcams.
· No graphic element crosses the face of any product; the glyph field sits under the
  blocks, and the notched rule frames a block rather than a camera.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence.
· No reading is legible on any camera screen.
· Every letter sits inside the shield with visible margin; nothing touches a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## 3 — five desk chairs · `rounded-cells` · radiating arcs + `halftone`

```
TYPE: lede-collage v0.13 — SET 5 CELL 3
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every chair is clean and as-new — upholstery unmarked, castors unworn.
[LAYOUT]    five cells with rounded corners of clearly UNEQUAL size, tiled with even
            margins between them, one chair per cell.
[HERO]      the FIRST attachment is rendered clearly LARGEST, in the largest cell.
[PALETTE]   four DIFFERENT hues across the five cells. Every one is BOTH light AND strongly
            coloured at once: NOT pastels, tints or washed tones; NOT deep, dark or muted.
[GRAPHICS]  concentric arcs radiating outward from behind the hero chair, in a deeper shade
            of its own cell, fading as they widen. Plus a fine halftone dot screen over the
            ground between the cells only.
[BADGE]     form `laurel`: a wreath of two branches meeting at the base, in a colour NO CELL
            carries. THREE type levels — a small label at the top between the branch tips,
            a large word in the middle, a year small at the base. The branches are the
            device. A soft shadow. Words: EDITOR'S PICK, DESK CHAIRS, 2026.
[SHADOW]    a faint contact shadow beneath each chair, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are desk chairs — a seat on a castored base for working at a desk. Not
  dining chairs, not armchairs, not stools.
· No graphic element crosses the face of any product. The arcs sit BEHIND the hero; the
  halftone falls on the ground between cells only, never on a cell's colour.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence.
· Every letter sits inside the wreath with visible margin; nothing touches a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## 4 — five humidifiers · `open` gradient · dotted outlines + `icon-pair`

```
TYPE: lede-collage v0.13 — SET 5 CELL 4
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every humidifier is clean and as-new — tanks clear, housings unmarked.
[LAYOUT]    no cells and no divisions. The five humidifiers arranged across one
            uninterrupted ground in a reading order the eye follows.
[HERO]      the FIRST attachment sits at the CENTRE and is rendered clearly LARGEST.
[GROUND]    one smooth gradient filling the frame, travelling between two hues. Choose how
            far it travels. Both ends are BOTH light AND strongly coloured at once: NOT
            pastels or washed tones; NOT deep, dark or muted ones.
[GRAPHICS]  a dotted outline echoing each humidifier's silhouette, offset behind it in
            white. Plus a pair of small circular icons in the lower right corner — a simple
            drop and a simple leaf, line-drawn, not filled.
[BADGE]     form `seal`: a circular stamp with a toothed rim, upper right, clear of every
            unit, in a colour neither end of the gradient carries. THREE type levels — a
            small label arced along the top of the rim, a large word across the middle, a
            year small beneath. A ring of dots inset inside the rim. A soft shadow.
            Words: BEST OVERALL, HUMIDIFIERS, 2026.
[SHADOW]    a faint contact shadow beneath each humidifier, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are humidifiers — a device that puts moisture into room air. Not air
  purifiers, not diffusers, not dehumidifiers, not fans.
· No graphic element crosses the face of any product. Each dotted outline sits behind its
  own unit and never over another; the icons sit clear of every unit.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in size and prominence.
· The gradient is perfectly smooth — no banding, no vignette.
· Every letter sits inside the disc with visible margin; nothing touches a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## 5 — five action cameras · `outlined-panels` · THREE elements stacked

**Finds the ceiling.** Three graphic layers at once, on top of a layout, a hero and a badge.

```
TYPE: lede-collage v0.13 — SET 5 CELL 5
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every camera is clean and as-new — lenses clear, housings unscuffed.
[LAYOUT]    five upright panels of UNEQUAL width stepped to different heights, one camera
            per panel, each filling its panel.
[HERO]      the FIRST attachment is rendered clearly LARGEST, in the widest panel.
[PALETTE]   three DIFFERENT hues across the panels and the ground. All are BOTH light AND
            strongly coloured at once: NOT pastels or washed tones; NOT deep or muted ones.
[GRAPHICS]  three layers together — a thin rule with notched corners around every panel; a
            regular field of small repeated glyphs across the ground behind the panels; and
            a fine halftone dot screen over the hero's panel only.
[BADGE]     form `starburst`: a many-pointed star, upper left, in a colour no panel carries.
            THREE type levels — a small label across the top, a large word in the middle, a
            year small beneath. A ring of dots inset inside the points. A soft shadow.
            Words: TOP RATED, ACTION CAMERAS, 2026.
[SHADOW]    a faint contact shadow beneath each camera, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are action cameras — a small rugged camera worn or mounted for sport.
  Not dash cams, not compacts, not phones, not camcorders.
· No graphic element crosses the face of any product. Rules frame panels, the glyph field
  sits under the panels, the halftone lies on one panel's colour and not on its camera.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence.
· Every letter sits inside the star with visible margin; nothing touches a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## 6 — five yoga mats · `colour-cells` · NO GRAPHICS · CONTROL

**Cells, hero, badge and nothing else.** It is set 4 cell 3's construction with the graphics
layer removed, so "more elements" can be judged against "none" in the same batch.

```
TYPE: lede-collage v0.13 — SET 5 CELL 6, CONTROL
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every mat is clean and as-new — surfaces unmarked, edges uncurled.
[LAYOUT]    five rectangular cells of UNEQUAL size tiled edge to edge with no gaps, one mat
            per cell, each rolled or part-rolled, cut out and scaled to fill its own cell.
[HERO]      the FIRST attachment is rendered clearly LARGEST, in the largest cell.
[PALETTE]   five DIFFERENT hues, one per cell. Every one is BOTH light AND strongly coloured
            at once: NOT pastels, tints or washed tones; NOT deep, dark or muted ones.
[BADGE]     form `roundel`: a scalloped disc, upper right, in a colour NO CELL carries.
            THREE type levels — a small label arced along the top of the rim, a large word
            across the middle, a year small beneath. A star device under the year. An inner
            ring inset from the rim. A soft shadow. Words: BEST OVERALL, YOGA MATS, 2026.
[SHADOW]    a faint contact shadow beneath each mat, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are yoga mats — a rollable exercise mat. Not gym mats, not towels, not
  camping mats.
· NO graphic elements of any kind: no outlines, no glyph field, no halftone, no arcs, no
  icons, no labels. Cells, products, badge and shadows only.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence.
· Every letter sits inside the disc with visible margin; nothing touches a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **Did all five units in every cell belong to the category named?** | `PARTS/field-coherence`, new at 0.13. It has failed twice with no clause guarding it; this is the first set that states it |
| 2 | **Cells 1–5 against cell 6 — do the graphics make the frames better or busier?** | `PARTS/graphics`. The owner asked for more; the control is the only way to see what more costs |
| 3 | **Cell 5 — where is the ceiling? Do three stacked layers still read as an index?** | whether the file needs a cap on how many elements may stack |
| 4 | **Did any graphic element cross a product's face?** | the one rule the graphics layer carries, stated in all five |
| 5 | **Cell 4 — do dotted silhouette outlines work here?** | borrowed from `lede-winner`'s corpus, never asked for in a collage |
| 6 | **Cell 3 — do radiating arcs read as emphasis or as noise?** | the other borrowed element |
| 7 | **Did the destination clause reduce invented lettering this time?** | 2 of 5 last set. Five more cells, and the blank-brand-surface hypothesis to watch: bike lights and dash cams have small busy surfaces, yoga mats have a large blank one |
| 8 | **Is the hero unmistakable in all six?** | now settled at size; this confirms it across five new layouts |

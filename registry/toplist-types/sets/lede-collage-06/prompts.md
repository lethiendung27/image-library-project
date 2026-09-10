# `lede-collage` set 6 — the badge goes in the hero's cell, and the ceiling gets a second test

Written against **`lede-collage` v0.14**. Owner, 2026-09-09: *"nếu có frame lớn nhất thì badge
đặt ngay trong frame đấy"*.

## What set 5 settled, and what it only suggested

**Settled — `PARTS/field-coherence` held on its first outing.** Bike lights were all bike
lights, humidifiers all humidifiers, action cameras all action cameras. The clause that
should have existed since set 1 works the first time it is stated.

**Settled — graphics work, one accent at a time.** The `outline-echo` gave each bike light a
coloured glow offset behind it; dotted silhouette outlines and the drop-and-leaf icon pair
both landed on the humidifiers. Both borrowed elements transferred.

**Suggested, and this set tests it — the ceiling is TWO layers.** Cell 5 stacked three
(notched rules + glyph field + halftone) and **all five cameras came back as flat vector
illustrations**: cartoon bodies, a drawn icon on the screen. That is not clutter, it is a
register flip, and it is a single observation. Cell 6 below stacks three again on a different
layout and different products. **If it flips too, the ceiling is real at 2 of 2; if it does
not, set 5 cell 5 was one bad frame and the cap comes out of the file.**

## The badge placement, and the fault it also fixes

Three celled frames in set 5 placed the badge by compass direction. Cell 5 happened to land
it on the hero panel and reads correctly. **Cells 1 and 6 put it on bare ground, and each
opened a dead white gap** in a composition that otherwise tiles edge to edge — the badge was
not floating by choice, the prompt gave it nowhere to be.

So: **inside the hero's cell where the layout has cells**, on the ground where it does not.
One simplification comes free — the colour rule goes from *clear every cell* to **clear one**.

## One wording fault of mine, corrected

Set 5 cell 1 asked for *"a small corner-label in the lower left"* and got **five**, one per
cell. An accent has to say whether it is per-FRAME or per-CELL. Cell 3 below states it as
explicitly as it can be stated.

## The cells

| cell | products | layout | graphics | badge sits |
|---|---|---|---|---|
| 1 | 5 rice cookers | `colour-cells` | 2 — glyph field (frame) + outline-echo (per cell) | **in the hero cell** |
| 2 | 5 soundbars | `rounded-cells` | 2 — halftone (frame) + notched rule (per cell) | **in the hero cell** |
| 3 | 5 laptop stands | `blocks` | 1 — **ONE corner-label for the whole frame** | **in the hero block** |
| 4 | 5 water flossers | `outlined-panels` | 2 — arcs behind hero + ONE icon pair | **in the hero panel** |
| 5 | 5 pizza ovens | `open` gradient | 2 — dotted outlines + ONE corner label | on the ground — no cells exist |
| 6 | 5 baby strollers | `outlined-panels` | **THREE — CEILING CONTROL** | in the hero panel |

Thirty products, none used in sets 1–5. Five attachments each; **the first attachment is the
page's own product**. All six render elsewhere (ADR-076).

---

## 1 — five rice cookers · `colour-cells` · 2 layers · badge IN the hero cell

```
TYPE: lede-collage v0.14 — SET 6 CELL 1
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every cooker is clean and as-new — lids seated, panels unmarked.
[LAYOUT]    five rectangular cells of UNEQUAL size tiled edge to edge with no gaps, one
            cooker per cell, each cut out and scaled to fill its own cell.
[HERO]      the FIRST attachment is rendered clearly LARGEST, in the largest cell.
[PALETTE]   five DIFFERENT hues, one per cell. Every one is BOTH light AND strongly coloured
            at once: NOT pastels, tints or washed tones; NOT deep, dark or muted ones.
[GRAPHICS]  exactly TWO layers. FRAME-LEVEL: a regular field of small repeated glyphs across
            every cell, in a tone slightly deeper than each cell's own colour. PER-CELL: a
            thin outline echoing that cooker's own silhouette, offset behind it.
[BADGE]     form `roundel`, sitting INSIDE the hero's cell, upper corner, clear of the
            cooker. A scalloped disc in a colour the hero's cell does not carry. THREE type
            levels — a small label arced along the top of the rim, a large word across the
            middle, a year small beneath. A star device under the year. An inner ring inset
            from the rim. A soft shadow. Words: BEST OVERALL, RICE COOKERS, 2026.
[SHADOW]    a faint contact shadow beneath each cooker, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are rice cookers — a lidded electric pot for cooking rice. Not slow
  cookers, not pressure cookers, not multicookers, not steamers.
· The badge sits wholly inside the hero's cell and does not cross into another cell or
  touch a frame edge.
· No graphic element crosses the face of any product.
· Exactly two graphic layers. No third.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## 2 — five soundbars · `rounded-cells` · 2 layers · badge IN the hero cell

```
TYPE: lede-collage v0.14 — SET 6 CELL 2
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every soundbar is clean and as-new — grilles unmarked, ends unscuffed.
[LAYOUT]    five cells with rounded corners of clearly UNEQUAL size, tiled with even margins
            between them, one soundbar per cell.
[HERO]      the FIRST attachment is rendered clearly LARGEST, in the largest cell.
[PALETTE]   four DIFFERENT hues across the five cells. Every one is BOTH light AND strongly
            coloured at once: NOT pastels, tints or washed tones; NOT deep, dark or muted.
[GRAPHICS]  exactly TWO layers. FRAME-LEVEL: a fine halftone dot screen over the ground
            between the cells, not on the cells and not on the products. PER-CELL: a thin
            rule with notched corners drawn just inside each cell's edge.
[BADGE]     form `shield`, sitting INSIDE the hero's cell, upper corner, clear of the
            soundbar. A crest with a pointed base in a colour the hero's cell does not
            carry. THREE type levels — a small label across the top with a rule either side,
            a large word in the middle, a year small at the point. A bevel inset from the
            edge. A soft shadow. Words: BEST OVERALL, SOUNDBARS, 2026.
[SHADOW]    a faint contact shadow beneath each soundbar, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are soundbars — a long single-cabinet speaker for a television. Not
  bookshelf speakers, not portable bluetooth speakers, not smart speakers.
· The badge sits wholly inside the hero's cell and does not cross into another cell or
  touch a frame edge.
· No graphic element crosses the face of any product.
· Exactly two graphic layers. No third.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## 3 — five laptop stands · `blocks` · ONE frame-level accent

**States the frame-level/cell-level distinction as explicitly as it can be stated**, after
set 5 asked for one corner label and received five.

```
TYPE: lede-collage v0.14 — SET 6 CELL 3
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every stand is clean and as-new — surfaces unmarked, hinges bright.
[LAYOUT]    flat blocks of colour of UNEQUAL size overlapping across the frame at slight
            angles, the five stands laid across them. Flat shapes on one plane, no
            perspective and no thickness.
[HERO]      the FIRST attachment is rendered clearly LARGEST and sits OFF CENTRE.
[PALETTE]   four DIFFERENT hues across the blocks. Every one is BOTH light AND strongly
            coloured at once: NOT pastels, tints or washed tones; NOT deep, dark or muted.
[GRAPHICS]  exactly ONE layer, and it is FRAME-LEVEL: a SINGLE corner-label in the lower
            left of the WHOLE FRAME — the word PICKS with a short rule as its tail. There
            is ONE of these in the entire image. Do not repeat it per block.
[BADGE]     form `laurel`, sitting INSIDE the hero's block, clear of the stand. A wreath of
            two branches meeting at the base, in a colour the hero's block does not carry.
            THREE type levels — a small label at the top between the branch tips, a large
            word in the middle, a year small at the base. The branches are the device. A
            soft shadow. Words: EDITOR'S PICK, LAPTOP STANDS, 2026.
[SHADOW]    a faint contact shadow beneath each stand, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are laptop stands — a riser that holds a laptop above a desk. Not monitor
  arms, not laptop sleeves, not lap desks, not docking stations.
· There is exactly ONE corner-label in the whole image. Not one per block.
· The badge sits wholly inside the hero's block and does not touch a frame edge.
· No graphic element crosses the face of any product.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## 4 — five water flossers · `outlined-panels` · arcs + ONE icon pair

```
TYPE: lede-collage v0.14 — SET 6 CELL 4
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every flosser is clean and as-new — tanks clear, tips unmarked.
[LAYOUT]    five upright panels of UNEQUAL width stepped to different heights, marked out by
            thin rules, one flosser per panel, each filling its panel.
[HERO]      the FIRST attachment is rendered clearly LARGEST, in the widest panel.
[PALETTE]   three DIFFERENT hues across the panels and the ground behind them. All are BOTH
            light AND strongly coloured at once: NOT pastels or washed tones; NOT deep, dark
            or muted ones.
[GRAPHICS]  exactly TWO layers. Concentric arcs radiating outward from behind the hero
            flosser, in a deeper shade of its own panel, fading as they widen. Plus a SINGLE
            pair of small line-drawn circular icons — a drop and a tooth — in the lower
            right of the WHOLE FRAME. There is ONE pair in the entire image.
[BADGE]     form `seal`, sitting INSIDE the hero's panel, upper area, clear of the flosser.
            A circular stamp with a toothed rim in a colour the hero's panel does not carry.
            THREE type levels — a small label arced along the top of the rim, a large word
            across the middle, a year small beneath. A ring of dots inset inside the rim.
            A soft shadow. Words: BEST OVERALL, WATER FLOSSERS, 2026.
[SHADOW]    a faint contact shadow beneath each flosser, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are water flossers — a device that cleans between teeth with a jet of
  water. Not electric toothbrushes, not mouthwash bottles, not interdental brushes.
· There is exactly ONE icon pair in the whole image. Not one per panel.
· The arcs sit BEHIND the hero and no graphic element crosses the face of any product.
· Exactly two graphic layers. No third.
· The badge sits wholly inside the hero's panel and does not touch a frame edge.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## 5 — five pizza ovens · `open` gradient · badge on the GROUND

**The exception the rule needs.** `open` has no cells, so there is no hero cell to put a badge
inside, and it goes on the ground clear of every unit.

```
TYPE: lede-collage v0.14 — SET 6 CELL 5
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every oven is clean and as-new — stones unstained, shells unmarked.
[LAYOUT]    no cells and no divisions. The five ovens arranged across one uninterrupted
            ground in a reading order the eye follows.
[HERO]      the FIRST attachment sits at the CENTRE and is rendered clearly LARGEST.
[GROUND]    one smooth gradient filling the frame, travelling between two hues. Choose how
            far it travels. Both ends are BOTH light AND strongly coloured at once: NOT
            pastels or washed tones; NOT deep, dark or muted ones.
[GRAPHICS]  exactly TWO layers. A dotted outline echoing each oven's silhouette, offset
            behind it in white. Plus a SINGLE corner-label in the lower left of the WHOLE
            FRAME — the word PICKS with a short rule as its tail. There is ONE in the image.
[BADGE]     form `starburst`, on the ground in the upper right, clear of every oven, in a
            colour neither end of the gradient carries. THREE type levels — a small label
            across the top, a large word in the middle, a year small beneath. A ring of dots
            inset inside the points. A soft shadow. Words: BEST OVERALL, PIZZA OVENS, 2026.
[SHADOW]    a faint contact shadow beneath each oven, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are pizza ovens — a dedicated oven that cooks a pizza at high heat. Not
  domestic ovens, not air fryers, not barbecues, not toaster ovens.
· There is exactly ONE corner-label in the whole image.
· No graphic element crosses the face of any product.
· Exactly two graphic layers. No third.
· The gradient is perfectly smooth — no banding, no vignette.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in size and prominence.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## 6 — five baby strollers · THREE layers · CEILING CONTROL

**Stacks three graphic layers a second time**, on a different layout and different products.
Set 5 cell 5 did this and every product came back as a flat vector illustration. If this one
flips too, the ceiling is real at 2 of 2 and the cap stays in the file. If it stays
photographic, set 5 cell 5 was one bad frame and the cap comes out.

```
TYPE: lede-collage v0.14 — SET 6 CELL 6, CONTROL
REGISTER: graphic product composition, one frame. PHOTOGRAPHIC product renders.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every stroller is clean and as-new — fabric unmarked, wheels unworn.
[LAYOUT]    five upright panels of UNEQUAL width stepped to different heights, one stroller
            per panel, each filling its panel.
[HERO]      the FIRST attachment is rendered clearly LARGEST, in the widest panel.
[PALETTE]   three DIFFERENT hues across the panels and the ground. All are BOTH light AND
            strongly coloured at once: NOT pastels or washed tones; NOT deep or muted ones.
[GRAPHICS]  THREE layers together — a thin rule with notched corners around every panel; a
            regular field of small repeated glyphs across the ground behind the panels; and
            a fine halftone dot screen over the hero's panel only.
[BADGE]     form `roundel`, sitting INSIDE the hero's panel, upper area, clear of the
            stroller, in a colour the hero's panel does not carry. THREE type levels — a
            small label arced along the top of the rim, a large word across the middle, a
            year small beneath. A star device. An inner ring. A soft shadow.
            Words: BEST OVERALL, STROLLERS, 2026.
[SHADOW]    a faint contact shadow beneath each stroller, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are baby strollers — a wheeled pushchair for an infant. Not prams for
  dolls, not shopping trolleys, not wheelchairs, not bike trailers.
· Every stroller is a PHOTOGRAPHIC render of the attached reference — real materials, real
  fabric, real light. Not an illustration, not a flat vector drawing, not a cartoon.
· No graphic element crosses the face of any product.
· The badge sits wholly inside the hero's panel and does not touch a frame edge.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence.
· No child, no infant, no doll, no person.
· No rank number, price, star rating row, certification seal, press logo or third-party mark.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **Did the badge sit inside the hero's cell in cells 1, 2, 3, 4 and 6?** | the owner's placement rule, and the dead-white-gap fault it also fixes |
| 2 | **Cell 6 — did three layers flip the register a second time?** | the ceiling. One observation becomes a rule at two, or comes out of the file at one |
| 3 | **Cell 6 carries an explicit "photographic, not illustration" constraint that set 5's did not.** If it stays photographic, was it the cap or the constraint that saved it? | whether the cap is needed at all, or whether naming the register is enough |
| 4 | **Cells 3, 4, 5 — exactly ONE frame-level accent, or one per cell again?** | the per-frame/per-cell wording, which produced five labels when it asked for one |
| 5 | **Did any frame carry a third graphic layer unasked?** | whether "exactly two, no third" holds as a count |
| 6 | **Did all five units in every cell belong to the category named?** | `field-coherence` at a second outing; it held 4 of 4 in set 5 |
| 7 | **Cell 5 — does a badge on open ground still avoid a dead gap?** | the exception, and whether the rule needs more than "no cells means the ground" |
| 8 | **Invented lettering: how many this time?** | around thirteen across the namespace, and the blank-surface hypothesis to watch — soundbars and laptop stands both have large flat faces |

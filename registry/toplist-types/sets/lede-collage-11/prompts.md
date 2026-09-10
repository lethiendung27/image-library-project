# `lede-collage` set 11 — the full type, all eight layouts, with the white frame closed

Written against **`lede-collage` v0.20**. Owner, 2026-09-10: *"ice cream maker không pass"*,
*"hạn chế nền trắng bên ngoài quá nhiều"*, *"tạo 1 bộ đầy đủ các type collage để tôi test lại"*.

## What set 10 settled

**The margin is solved. 5 of 5 plate cells clean**, against 0 of 12 for four wordings of a
clearance, and the no-plate control breached exactly as predicted. *Describe the thing, never
the gap* — a clearance the model must compute is inert; one drawn as an object with an edge is
obeyed.

**`outlined-panels` EQUAL lands 2 of 2.** The descending staircase is gone, and cell 2 is the
first frame in which a `seal` stayed inside its hero panel.

## The two faults this set closes

**1 — the white frame.** Measured, plate area and border colour:

| | plate covers | border top / bottom | border colour |
|---|---|---|---|
| cargo boxes | **60%** | 15.6% / 17.6% | rgb(244,243,238) |
| garden shredders | **68%** | 12.3% / 13.6% | rgb(229,233,237) |
| sleeping pads | **71%** | 9.6% / 9.2% | rgb(240,240,237) |
| rowing machines | 80% | 6.9% / 7.1% | rgb(249,245,234) |

The plate was asked for four fifths and three cells gave 60–71%, and **the border came back
white in 5 of 5** — because the clause said *"the ground shows as a plain even border"* and never
said what colour a plain border is. **That is the `LABEL` fault again**: a slot named by ROLE
with no value takes a default, and the default for an unnamed ground is white.

So the plate now fills **nineteen twentieths**, and the border is **a named hue — the deepest of
the palette's own family**, refused white, grey and pale in the binding block.

**2 — cells left empty.** `never pastel or dark` failed 2 of 6: the sleeping pads came back in
washed lavender and peach, and the control left four of five panels a pale pink with a product
floating on them. What those share is a cell the model treated as **empty space** rather than as
a coloured field, so every cell below is named as a filled field.

**And one new refusal**: cell 1 printed rank numbers `2 3 4 5`, against a NEGATIVE that names
them first. Stated in every cell now rather than left to the list.

## The cells — every layout this type owns

| # | layout | category | units | badge |
|---|---|---|---|---|
| 1 | `open` gradient | 5 patio umbrellas | 5 | `band` |
| 2 | `colour-cells` | 5 leaf blowers | 5 | `sticker` |
| 3 | `blocks` | 5 bike racks | 5 | `plaque` |
| 4 | `outlined-panels` EQUAL | 5 snow blowers | 5 | `seal` |
| 5 | `rounded-cells` | 5 air mattresses | 5 | `shield` |
| 6 | `pinboard` | 5 dive computers | 5 | `sticker` |
| 7 | `split-frame` | 1 wheelbarrow | 1 | none |
| 8 | `polaroid` | 1 chess set | 1 | none |

Thirty products, none used in any earlier set or round. Five attachments each on cells 1–6, one
on cells 7–8; **the first attachment is the page's own product**. All eight render elsewhere
(ADR-076).

---

## 1 — five patio umbrellas · `open` gradient · `band`

```
TYPE: lede-collage v0.20 — SET 11 CELL 1
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — style these.
[PLATE]    a rectangle filling nineteen twentieths of the frame. The composition lives inside it; around it runs a NARROW border in the deepest hue of the palette family.
[LAYOUT]   inside the plate: no cells and no divisions — five umbrellas across one uninterrupted ground in a reading order. The hero sits at the CENTRE and is clearly the largest.
[GROUND]   the plate carries one smooth gradient between two hues OPPOSITE each other on the colour wheel, corner to corner. Both ends light AND strongly coloured, and the midpoint stays saturated rather than passing through grey or white. No banding.
[GRAPHICS] a dotted white outline echoing each unit's silhouette, offset behind it.
[BADGE]    `band` across the plate's upper third behind the units, both ends stopping inside the plate, in a colour neither end of the gradient carries: three lines of type — BEST OVERALL small, PATIO UMBRELLAS large, 2026 small — a thin rule above and below, a soft shadow.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured.
· Every unit shows a fabric canopy on ribs above a pole, opened.
· The border around the plate is a deep saturated hue. It is never white, grey or pale.
· Every coloured area is a filled field of strong colour, never empty space with a product on it.
· The other four units are equal to each other in size and prominence.
· The badge carries exactly the three strings named and no other word.
· No number appears anywhere in the frame except the year in the badge.
· Exactly one graphic layer, and no graphic crosses any product's face.
· One faint contact shadow per unit, alike for all five.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 2 — five leaf blowers · `colour-cells` · `sticker`

```
TYPE: lede-collage v0.20 — SET 11 CELL 2
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — style these.
[PLATE]    a rectangle filling nineteen twentieths of the frame. The composition lives inside it; around it runs a NARROW border in the deepest hue of the palette family.
[LAYOUT]   inside the plate: the hero's cell fills its LEFT HALF; the other four tile the right half as a 2x2 of unequal cells. One blower fills each cell.
[PALETTE]  five hues within about a sixth of the colour wheel of one another — one family, no cell an outlier. Every one light AND strongly coloured, never pastel or dark.
[GRAPHICS] frame: small repeated glyphs a shade deeper than each cell. Per cell: a thin outline echoing that unit's silhouette, offset behind it.
[BADGE]    `sticker`, a tilted die-cut circle in a colour no cell carries: three lines of type — BEST OVERALL arced small on the rim, LEAF BLOWERS large across the middle, 2026 small beneath — a ring of dots, a soft shadow.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured.
· Every unit shows a long nozzle tube joined to a motor housing with a grip.
· The border around the plate is a deep saturated hue. It is never white, grey or pale.
· Every cell is a filled field of strong colour, never empty space with a product on it.
· The hero is the FIRST reference, clearly largest; the other four equal in prominence.
· The badge occupies about a fifth of the hero's cell and sits in its upper corner.
· The badge carries exactly the three strings named and no other word.
· No number appears anywhere in the frame except the year in the badge.
· Exactly two graphic layers, and no graphic crosses any product's face.
· One faint contact shadow per unit, alike for all five.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 3 — five bike racks · `blocks` · `plaque`

```
TYPE: lede-collage v0.20 — SET 11 CELL 3
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — style these.
[PLATE]    a rectangle filling nineteen twentieths of the frame. The composition lives inside it; around it runs a NARROW border in the deepest hue of the palette family.
[LAYOUT]   inside the plate: flat blocks of colour of unequal size overlapping at slight angles, one rack across each. Flat shapes, no perspective. The hero's block fills the plate's left half, the other four its right half. No block is left empty.
[PALETTE]  four hues within about a sixth of the colour wheel of one another — one family. Every one light AND strongly coloured, never pastel or dark.
[GRAPHICS] frame: a halftone dot screen over the plate behind the blocks, not on the blocks or the products.
[BADGE]    `plaque` — a plain four-cornered rectangle, half again as tall as wide, in a colour no block carries: three lines — EDITOR'S PICK small above a thin rule, BIKE RACKS large below, 2026 small at the foot — an inset border, a soft shadow.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured.
· Every unit shows arms or trays that hold a bicycle, on a mount.
· The border around the plate is a deep saturated hue. It is never white, grey or pale.
· Every block is a filled field of strong colour, never empty space with a product on it.
· The hero is the FIRST reference, clearly largest; the other four equal in prominence.
· The badge is a rectangle with four square corners — not a crest, not a shield, not a bar.
· The badge occupies about a fifth of the hero's block and sits in its upper corner.
· The badge carries exactly the three strings named and no other word.
· No number appears anywhere in the frame except the year in the badge.
· Exactly one graphic layer, and no graphic crosses any product's face.
· One faint contact shadow per unit, alike for all five.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 4 — five snow blowers · `outlined-panels`, EQUAL panels · `seal`

```
TYPE: lede-collage v0.20 — SET 11 CELL 4
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — style these.
[PLATE]    a rectangle filling nineteen twentieths of the frame. The composition lives inside it; around it runs a NARROW border in the deepest hue of the palette family.
[LAYOUT]   inside the plate: five upright panels marked by thin rules, side by side, all the same height, reaching the plate's top and bottom. The hero's panel is WIDER; the other four are equal in width. One blower fills each.
[PALETTE]  three hues within about a sixth of the colour wheel of one another — one family. Every one light AND strongly coloured, never pastel or dark.
[GRAPHICS] frame: concentric arcs radiating from behind the hero in a deeper shade of its panel.
[BADGE]    `seal`, a toothed-rim circular stamp in a colour no panel carries: three lines of type — BEST OVERALL arced small on the rim, SNOW BLOWERS large across the middle, 2026 small beneath — a ring of dots inset, a soft shadow.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured.
· Every unit shows an auger housing at the front and a discharge chute above it.
· The border around the plate is a deep saturated hue. It is never white, grey or pale.
· Every panel is a filled field of strong colour, never empty space with a product on it.
· The four non-hero panels are the same width and the same height as each other. None is stepped.
· The hero is the FIRST reference, clearly largest; the other four equal in prominence.
· The badge occupies about a fifth of the hero's panel and sits in its upper corner.
· The badge carries exactly the three strings named and no other word.
· No number appears anywhere in the frame except the year in the badge.
· Exactly one graphic layer, and no graphic crosses any product's face.
· One faint contact shadow per unit, alike for all five.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 5 — five air mattresses · `rounded-cells` · `shield`

```
TYPE: lede-collage v0.20 — SET 11 CELL 5
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — style these.
[PLATE]    a rectangle filling nineteen twentieths of the frame. The composition lives inside it; around it runs a NARROW border in the deepest hue of the palette family.
[LAYOUT]   inside the plate: the hero's cell fills its TOP HALF; the other four sit in a row across the bottom half, unequal in width. Five rounded-corner cells, evenly spaced, one mattress filling each.
[PALETTE]  four hues within about a sixth of the colour wheel of one another — one family. Every one light AND strongly coloured, never pastel or dark.
[GRAPHICS] frame: a halftone dot screen on the plate between the cells only, not on the cells and not on the products. Per cell: a thin rule with notched corners inside its edge.
[BADGE]    `shield`, a pointed-base crest in a colour no cell carries: three lines of type — BEST OVERALL small across the top between two rules, AIR MATTRESSES large in the middle, 2026 small at the point — a bevel inset, a soft shadow.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured.
· Every unit shows a flocked or ribbed inflated bed with a valve and a raised edge.
· The border around the plate is a deep saturated hue. It is never white, grey or pale.
· Every cell is a filled field of strong colour, never empty space with a product on it.
· The hero is the FIRST reference, clearly largest; the other four equal in prominence.
· The badge occupies about a fifth of the hero's cell and sits in its upper corner.
· The badge carries exactly the three strings named and no other word.
· No number appears anywhere in the frame except the year in the badge.
· Exactly two graphic layers, and no graphic crosses any product's face.
· One faint contact shadow per unit, alike for all five.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 6 — five dive computers · `pinboard` · `sticker`

**The photographed layout.** Its board measured texture 28.7 on its first outing, the highest
this type has recorded.

```
TYPE: lede-collage v0.20 — SET 11 CELL 6
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — style these.
[LAYOUT]   a real cork pinboard filling the frame. Five printed photographs pinned to it, each a white-bordered print of one dive computer, overlapping slightly at slight angles. The hero's print fills the left half of the board; the other four overlap across the right half.
[GROUND]   the board is photographed: real cork grain, real pin heads, each print casting its own soft shadow onto the board and lifting a little at one corner.
[GRAPHICS] none beyond the pins and the prints themselves.
[BADGE]    `sticker`, a tilted die-cut circle pressed onto the board clear of every print, in a colour the cork does not carry: three lines of type — BEST OVERALL arced small on the rim, DIVE COMPUTERS large across the middle, 2026 small beneath — a ring of dots, a soft shadow.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured.
· Every unit shows a round or square display face on a wrist strap.
· The prints are photographs on a real board — not cut-outs floating on a flat colour.
· The cork fills the frame to every edge. There is no outer border and no white margin.
· The hero is the FIRST reference, clearly largest; the other four equal in prominence.
· The badge carries exactly the three strings named and no other word.
· No number appears anywhere in the frame except the year in the badge and whatever the references' own screens show.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 7 — one wheelbarrow · `split-frame` · no badge

```
TYPE: lede-collage v0.20 — SET 11 CELL 7
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the wheelbarrow in BOTH
            halves — preserve shape, proportions, material, finish, colour and every printed
            mark exactly, and identically in each half.
ELEMENTS — style these.
[LAYOUT]   the frame halved down the middle. LEFT half: the wheelbarrow as a clean cut-out on a flat designed ground. RIGHT half: the same wheelbarrow photographed in a real place, standing on a garden path in daylight.
[PALETTE]  the left half's ground is one flat hue, light AND strongly coloured, never pastel or dark.
[GRAPHICS] left half only: a regular field of small repeated glyphs across the flat ground, a shade deeper than it.
[SHADOW]   the cut-out carries one faint contact shadow; the photographed half carries the place's own light.

CONSTRAINTS — binding.
· Exactly ONE product in the frame, shown twice — once cut out, once photographed.
· It is the same wheelbarrow in both halves: same tray shape, same frame, same wheel, same colour.
· The two halves meet on a clean vertical division at the frame's centre, and both fill the frame to its edges. There is no outer border and no white margin.
· No graphic element crosses the wheelbarrow in either half.
· No badge, no title, no words and no numbers of any kind in the frame.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 8 — one chess set · `polaroid` · no badge

```
TYPE: lede-collage v0.20 — SET 11 CELL 8
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the chess set in EVERY
            print — preserve shape, proportions, material, finish, colour and every printed
            mark exactly, and identically in each.
ELEMENTS — style these.
[LAYOUT]   four instant-print frames — white borders, thick at the foot — overlapping at slight angles on one designed ground. Each print shows the SAME chess set from a different view: the board set up from above, a low three-quarter view, the pieces grouped beside the closed board, and the board folded or boxed.
[PALETTE]  the ground is one flat hue, light AND strongly coloured, never pastel or dark.
[GRAPHICS] a fine halftone dot screen over the ground, not on the prints.
[SHADOW]   each print casts its own soft shadow onto the ground.

CONSTRAINTS — binding.
· Exactly ONE product in the frame, shown in four prints.
· It is the same set in every print: same board, same piece design, same materials, same colours.
· The four views are different: from above, low three-quarter, pieces beside the board, folded or boxed.
· The ground fills the frame to every edge. There is no outer border and no white margin.
· No graphic element crosses a print.
· No badge, no title, no words and no numbers of any kind in the frame.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **Measure the plate and its border on cells 1–5: what share of the frame, and what colour?** | the white frame. Set 10 gave 60–85% and a white border 5 of 5 |
| 2 | **Is the margin still clean now that the border is narrow?** | the plate solved it at four fifths; this asks whether nineteen twentieths still works |
| 3 | **Did any cell come back pale, washed or empty?** | `never pastel` failed 2 of 6 where a cell read as empty space |
| 4 | **Did any number appear that is not a year?** | cell 1 of set 10 printed rank numbers 2 3 4 5 |
| 5 | **Cell 4 — are the four non-hero panels equal, and did the `seal` stay inside the hero's panel?** | equal panels 2 of 2; the badge inside a panel 1 of 4 |
| 6 | **Do the eight read as ONE type?** | the owner's re-test, and the reason this set runs every layout |
| 7 | **Cells 6, 7, 8 — is it recognisably the same product in every view, and is the frame full-bleed?** | the three layouts that take no plate |
| 8 | **How many units per frame, and was any reference used twice?** | geometry is 21 of 21 |
| 9 | **Register per frame: photographic or drawn?** | recorded, never explained. One render is one draw |

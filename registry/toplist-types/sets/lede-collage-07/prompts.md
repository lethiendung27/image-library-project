# `lede-collage` set 7, revised — the hero's cell gets a geometry, the five get their variants named, and SIZE gets a control

Written against **`lede-collage` v0.16**. Owner, 2026-09-10: *"tôi đánh giá batch này kém hơn
rất nhiều so với các set trước. cụ thể: hình ảnh sản phẩm thường bị 2d hoá, vẫn thừa số lượng
sản phẩm"*.

**This replaces the draft rendered on 2026-09-10. Render this one; the earlier draft is
superseded and its four renders are recorded in `lede-collage.md` § SET 7, LONG DRAFT.**

## What the long draft settled, and it is not what it was built to settle

**Four of six came back. Cells 4 and 6 did not, and cell 6 was the control** — the second
control this type has lost to a missing render.

**The count clause failed at 0 of 1.** Cell 1 carried *"There are EXACTLY FIVE units in the
frame — not four, not six"* in binding form and returned **six**: five projectors with one
silver cube rendered twice. Set 6 cell 1 did the same thing. Both are `colour-cells`, both put
the hero on a large open field instead of in a cell, and both then built five cells for five
references — **the sixth position is not a lost count, it is a hero placed outside the grid.**

So the fix is not a firmer prohibition. Round 3 measured this namespace's lever: geometry
delivered 1 of 1 while four prescriptions of taste were ignored 4 of 4. **Cells 1 and 2 below
say where the hero's cell IS** — a share of the frame — instead of asserting that it is one of
five.

**Cell 3 returned one product in four colours.** Four of the five garment steamers share one
silhouette, one vent pattern, one trigger and one tank; only the grey base-station unit is
different. *"Five different makers"* is a fact about the world, and the model satisfied it with
a paint chart. **Every cell below names the VARIANTS** — silhouette, proportion, body — the way
a same-person pair names the invariants.

**And the register fault has a better explanation than the graphics ceiling.** Graded by eye
across every frame whose register is legible:

| frame | layers | units drawn | register |
|---|---|---|---|
| set 7 c5 waffle makers | 2 | **large** | photographic 5 of 5 |
| set 6 c6 strollers | **3** | **large** | photographic 5 of 5 |
| set 7 c2 shredders | 2 | hero large, four small | hero photographic, four simplified |
| set 7 c3 steamers | 1 | **small** | four of five one mould |
| set 5 c5 action cameras | **3** | **small** | flat vector 5 of 5 |

**Layer count does not order that table; unit size does.** The two three-layer frames sit at
opposite ends and differ in how large the units are drawn. **Cells 5 and 6 below are the same
picture at two sizes.**

Three measurements were attempted for this and all three discarded for failing their own
controls — a local-flatness fraction, a tone entropy, and a blob count whose control was the
unit count itself. Nothing above is a number.

## The control, and what it is predicted to do

**Cell 6 is cell 5 with the units drawn small.** Same layout, same two graphic layers, same
badge form, same palette rule. The products differ because a set never re-runs a product, and
both categories are rectangular box appliances so the form factor stays close.

> **Prediction, before the render: cell 6 FAILS — the five wine coolers come back flattened,
> simplified or sharing one mould, while cell 5's turntables stay photographic.** If both stay
> photographic, size is not the variable and the graphics ceiling goes back on the table. If
> both flatten, the variable is neither and it is the layout itself.

## The cells

| cell | products | layout | badge | graphics | what it tests |
|---|---|---|---|---|---|
| 1 | 5 ice makers | `colour-cells` | `sticker` | 2 | the hero cell as GEOMETRY, on the layout that broke twice |
| 2 | 5 label printers | `rounded-cells` | `shield` | 2 | the same geometry on a second layout |
| 3 | 5 hedge trimmers | `blocks` | `plaque` | 1 frame-level | `distinctness` on a category whose units really do look alike |
| 4 | 5 tyre inflators | `outlined-panels`, NARROW | `seal` | 2 | the badge SIZE fix — never rendered, so still open |
| 5 | 5 turntables | `outlined-panels` | `band` | 2 | units drawn LARGE |
| 6 | 5 wine coolers | `outlined-panels` | `band` | 2 | **CONTROL — units drawn SMALL** |

Thirty products, none used in any earlier set or round; tyre inflators were written for the
long draft and never rendered. Five attachments each; **the first attachment is the page's own
product**. All six render elsewhere (ADR-076).

---

## 1 — five ice makers · `colour-cells` · `sticker` · the hero's cell has a geometry

```
TYPE: lede-collage v0.16 — SET 7 CELL 1
REGISTER: graphic product composition, one frame.
REFERENCES: five photos, one per unit, in order; reproduce each exactly. FIRST = the page's own.

ELEMENTS — style these.
[LAYOUT]   the hero's cell fills the LEFT HALF of the frame; the other four tile the right half as a 2x2 of unequal cells. No ground outside the five cells, one ice maker filling each.
[PALETTE]  one hue per cell, each light AND strongly coloured, never pastel or dark.
[GRAPHICS] frame: small repeated glyphs a shade deeper than each cell. Per cell: a thin outline echoing that unit's silhouette, offset behind it.
[BADGE]    `sticker`, tilted, in a colour the hero's cell does not carry: label arced on the rim, a large word, a small year, a ring of dots, a soft shadow.
           Words: BEST OVERALL, ICE MAKERS, 2026.
[SHADOW]   one faint contact shadow per unit, alike for all five.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured.
· Every unit shows a lidded chamber above a removable ice basket.
· The hero is the FIRST reference, clearly largest; the other four equal in prominence.
· Exactly two graphic layers, and no graphic crosses any product's face.
· The badge sits wholly inside the hero's own colour; if it does not fit, make it SMALLER, never move it out.
· Nothing comes within a tenth of the frame of any edge.
· No words in the frame but those named above.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 2 — five label printers · `rounded-cells` · `shield` · the same geometry, second layout

```
TYPE: lede-collage v0.16 — SET 7 CELL 2
REGISTER: graphic product composition, one frame.
REFERENCES: five photos, one per unit, in order; reproduce each exactly. FIRST = the page's own.

ELEMENTS — style these.
[LAYOUT]   the hero's cell fills the TOP HALF of the frame. The other four sit in a row across the bottom half, unequal in width. Five rounded-corner cells, evenly spaced, one printer filling each.
[PALETTE]  four hues across the five cells, each light AND strongly coloured, never pastel or dark.
[GRAPHICS] frame: a halftone dot screen on the ground between cells only, not on cells or products. Per cell: a thin rule with notched corners inside its edge.
[BADGE]    `shield`, a pointed-base crest in a colour the hero's cell does not carry: a small label between rules, a large word, a small year at the point, a bevel inset, a soft shadow. Clear of the printer.
           Words: BEST OVERALL, LABEL PRINTERS, 2026.
[SHADOW]   one faint contact shadow per unit, alike for all five.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured.
· Every unit shows a slot or roll bay from which a printed label strip emerges.
· The hero is the FIRST reference, clearly largest; the other four equal in prominence.
· Exactly two graphic layers, and no graphic crosses any product's face.
· The badge sits wholly inside the hero's own colour; if it does not fit, make it SMALLER, never move it out.
· Nothing comes within a tenth of the frame of any edge.
· No words in the frame but those named above.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 3 — five hedge trimmers · `blocks` · `plaque` · distinctness under stress

**The category is chosen because its units really do look alike.** If the variants clause holds
here it holds anywhere.

```
TYPE: lede-collage v0.16 — SET 7 CELL 3
REGISTER: graphic product composition, one frame.
REFERENCES: five photos, one per unit, in order; reproduce each exactly. FIRST = the page's own.

ELEMENTS — style these.
[LAYOUT]   flat blocks of colour of unequal size overlapping at slight angles, one trimmer across each. Flat shapes on one plane, no perspective. The hero sits OFF CENTRE. No block is left empty.
[PALETTE]  four hues across the blocks, each light AND strongly coloured, never pastel or dark.
[GRAPHICS] one accent: a corner-label in the lower left of the whole image — the word PICKS with a short rule as its tail.
[BADGE]    `plaque`, upright and taller than wide, in a colour the hero's block does not carry: a small label above a thin rule, a large word below, a small year at the foot, an inset border, a soft shadow.
           Words: EDITOR'S PICK, HEDGE TRIMMERS, 2026.
[SHADOW]   one faint contact shadow per unit, alike for all five.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured. Different blade lengths and different handle shapes.
· Every unit shows a toothed cutter bar extending from a motor housing with a grip.
· The hero is the FIRST reference, clearly largest; the other four equal in prominence.
· Exactly one graphic layer, and no graphic crosses any product's face.
· ONE corner-label in the whole image — not one per block.
· The badge sits wholly inside the hero's own colour; if it does not fit, make it SMALLER, never move it out.
· Nothing comes within a tenth of the frame of any edge.
· No words in the frame but those named above.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 4 — five tyre inflators · `outlined-panels`, NARROW · `seal` · the badge SIZE retest

**Still open** — this cell was written for the long draft and never rendered.

```
TYPE: lede-collage v0.16 — SET 7 CELL 4
REGISTER: graphic product composition, one frame.
REFERENCES: five photos, one per unit, in order; reproduce each exactly. FIRST = the page's own.

ELEMENTS — style these.
[LAYOUT]   five NARROW upright panels of unequal width, stepped to different heights, marked by thin rules, one inflator filling each. The hero takes the widest.
[PALETTE]  three hues across the panels and ground, each light AND strongly coloured, never pastel or dark.
[GRAPHICS] concentric arcs radiating from behind the hero in a deeper shade of its panel, fading as they widen. Plus one pair of small line-drawn icons — a gauge and a tyre — lower right.
[BADGE]    `seal`, a toothed-rim circular stamp in a colour the hero's panel does not carry: label arced on the rim, a large word, a small year, a ring of dots inset, a soft shadow.
           Words: BEST OVERALL, TYRE INFLATORS, 2026.
[SHADOW]   one faint contact shadow per unit, alike for all five.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured.
· Every unit shows a pressure gauge or digital readout and an air hose ending in a screw-on chuck.
· The hero is the FIRST reference, clearly largest; the other four equal in prominence.
· Exactly two graphic layers, and no graphic crosses any product's face.
· ONE icon pair in the whole image — not one per panel.
· The badge sits wholly inside the hero's own colour; if it does not fit, make it SMALLER, never move it out.
· Nothing comes within a tenth of the frame of any edge.
· No words in the frame but those named above.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 5 — five turntables · `outlined-panels` · `band` · units drawn LARGE

**Half of the size control.** Cell 6 is this cell with the units drawn small.

```
TYPE: lede-collage v0.16 — SET 7 CELL 5
REGISTER: graphic product composition, one frame.
REFERENCES: five photos, one per unit, in order; reproduce each exactly. FIRST = the page's own.

ELEMENTS — style these.
[LAYOUT]   five upright panels of unequal width stepped to different heights, one turntable per panel. Each unit is drawn LARGE — it fills its panel edge to edge with little empty space around it.
[PALETTE]  three hues across the panels and ground, each light AND strongly coloured, never pastel or dark.
[GRAPHICS] frame: a halftone screen on the ground behind the panels. Per panel: a thin rule with notched corners inside its edge.
[BADGE]    `band` across the upper third behind the units, in a colour no panel carries: a small label, a large word and a small year along it, a thin rule above and below, a soft shadow.
           Words: BEST OVERALL, TURNTABLES, 2026.
[SHADOW]   one faint contact shadow per unit, alike for all five.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured.
· Every unit shows a circular platter with a tonearm hinged at its edge.
· The hero is the FIRST reference, clearly largest; the other four equal in prominence.
· Exactly two graphic layers, and no graphic crosses any product's face.
· The band stops short of both side edges; its words stop short of the band's ends.
· Nothing comes within a tenth of the frame of any edge.
· No words in the frame but those named above.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## 6 — five wine coolers · `outlined-panels` · `band` · units drawn SMALL · SIZE CONTROL

**Predicted to FAIL.** Cell 5 with one variable moved: the units are drawn small inside their
panels instead of filling them.

```
TYPE: lede-collage v0.16 — SET 7 CELL 6, CONTROL
REGISTER: graphic product composition, one frame.
REFERENCES: five photos, one per unit, in order; reproduce each exactly. FIRST = the page's own.

ELEMENTS — style these.
[LAYOUT]   five upright panels of unequal width stepped to different heights, one wine cooler per panel. Each unit is drawn SMALL — it sits in the middle of its panel with generous empty colour all around it.
[PALETTE]  three hues across the panels and ground, each light AND strongly coloured, never pastel or dark.
[GRAPHICS] frame: a halftone screen on the ground behind the panels. Per panel: a thin rule with notched corners inside its edge.
[BADGE]    `band` across the upper third behind the units, in a colour no panel carries: a small label, a large word and a small year along it, a thin rule above and below, a soft shadow.
           Words: BEST OVERALL, WINE COOLERS, 2026.
[SHADOW]   one faint contact shadow per unit, alike for all five.

CONSTRAINTS — binding.
· Exactly five units. Each reference used once; none repeated.
· Five different products: different silhouettes, proportions and bodies — not one form recoloured.
· Every unit shows a glass door over horizontal bottle racks.
· The hero is the FIRST reference, clearly largest; the other four equal in prominence.
· Exactly two graphic layers, and no graphic crosses any product's face.
· The band stops short of both side edges; its words stop short of the band's ends.
· Nothing comes within a tenth of the frame of any edge.
· No words in the frame but those named above.
· Never invent a brand mark; leave unreadably small lettering as a plain surface.
· No rank number, price, star row, certification seal, press logo or third-party mark.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **Cells 5 and 6 — did the small units flatten while the large ones stayed photographic?** | the size hypothesis. If yes, `PARTS/graphics`'s layer cap comes out and size replaces it |
| 2 | **Cells 1 and 2 — did naming the hero's cell as a SHARE of the frame stop the sixth unit?** | `PARTS/count`, which stands at 0 of 1 against a prohibition |
| 3 | **Did any frame return one form in several colours?** | `PARTS/distinctness`. Cell 3's category is the hardest case on purpose |
| 4 | **Cell 4 — did the `seal` stay inside a NARROW panel, and did it shrink to do it?** | still open; the cell never rendered |
| 5 | **Measure every word, rule and badge against G10's 8% floor.** | the margin clause, written for set 6's breaches and never yet tested |
| 6 | **Did all five units show the named defining FEATURE?** | 2 of 2 so far — waffle makers and shredders both held |
| 7 | **Cells 5 and 6 — does `band` hold on a celled layout?** | it worked once, on `open`. This asks whether it needed open ground |
| 8 | **Did any frame print a title nobody asked for?** | the refusal is new and has never been tested |
| 9 | **Lettering: invented marks, and separately, garbled small type.** | two faults, tracked apart since set 6 |

# `lede-collage` set 3 — the hero is the page's own product, and the badge gets finished

Written against **`lede-collage` v0.9**. Owner, 2026-09-09: *"lưu ý sản phẩm của tôi (nếu
tham chiếu app luôn nằm ở giữa hoặc lớn nhất). cần hoàn thiện badge ở mức độ cao hơn."*

## The first note corrects a law I enforced in nine renders

**The owner's app builds a page for ONE product — theirs.** A top-N listicle sets that
product among four competitors, so the lede is **a hero plus a field**, not a neutral index.
Every cell of sets 1 and 2 carried *"no unit is favoured by scale, by lighting…"*, inherited
from `04-proof-lockedframe` through `lede-lineup`, and it was wrong for this pipeline.

**The law is scoped rather than deleted:** no unit favoured **except the page's own**, and
that one always is — centre, largest, or both. The other four stay equal to each other.

**The FIRST attachment is the hero.** `products[]` does not exist and neither does a hero
index, so attachment order carries it. That needs no schema change and works today; when the
field is built it should carry the flag properly.

*Set 2 cell 6 produced this by accident — its centre cell came back visibly largest with no
instruction to do so — which is worth knowing, because it means the composition wants a
centre and set 1 and 2 were fighting it.*

## The second note: all five badges met the spec and were still unfinished

Set 2's five badges each carried an internal tone step and two type sizes, which is what 0.8
asked for. Put beside the corpus mark the gap is countable. The `GOOD HOUSEKEEPING BEDDING
AWARDS` roundel carries: text **arced** around the rim, a two-line wordmark at a third size,
a year at a fourth, **a star device**, an inner ring inset from the edge, and a **shadow**
lifting the disc off the fabric. Set 2's plaque carries a square, a keyline, and two sizes.

**So the standard rises to five, and every badge below owes all five:**

1. **Three type levels** — a small label, a large word, a year or qualifier.
2. **A device** — a star, a laurel, a rule, a row of dots. Something that is not a letter.
3. **A silhouette that is not a plain rectangle.** Set 2's `seal` did this and was the best
   of the five, which is why it is the only form repeated here.
4. **Text following the form** where the form is round — arced along the rim.
5. **A shadow**, so the badge sits ON the frame rather than in it.

## The cells

| cell | products | hero placement | layout | badge |
|---|---|---|---|---|
| 1 | 5 coffee grinders | **centre, largest cell** | `colour-cells` | `roundel`, arced |
| 2 | 5 robot mops | **largest, off-centre** | `blocks` | `laurel` |
| 3 | 5 air fryers | **centre, same size as the rest** | `outlined-panels` | `starburst` |
| 4 | 5 electric scooters | **largest, centre** | `rounded-cells` | `shield` |
| 5 | 5 travel kettles | **centre, largest** | `open` gradient | `seal` — the set-2 form that worked |
| 6 | 5 hair dryers | **no hero — all five equal** | `colour-cells` | `roundel` | **CONTROL** |

**Cells 1, 2, 3 and 4 separate the two ways of being the hero.** Cell 1 uses both centre AND
size; cell 2 uses size alone, off-centre; cell 3 uses centre alone at equal size. If cell 3
reads as the hero without being bigger, position is enough and the clause can be softer.

**Cell 6 is the control and it is built the old way** — five equal units, no hero. Graded
against cell 1 it says whether a reader can even tell, and whether the hero costs the type
its *"claims nothing about possession"* purpose.

Thirty products, none used in sets 1 or 2 or any earlier round. Five attachments each, and in
every cell **the first attachment is the hero**. All six render elsewhere (ADR-076).

---

## 1 — five coffee grinders · hero centre AND largest · `roundel`

```
TYPE: lede-collage v0.9 — SET 3 CELL 1
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every grinder is clean and as-new — burr housings unmarked, hoppers clear.
[LAYOUT]    five rectangular cells of UNEQUAL size tiled edge to edge with no gaps. One
            grinder per cell, each cut out and scaled to fill its own cell.
[HERO]      the FIRST attachment sits in the CENTRE cell, and that cell is the LARGEST of
            the five. It is the page's own product and the frame says so by placement.
[PALETTE]   five DIFFERENT hues, one per cell — not one colour in five shades. Every one is
            BOTH light AND strongly coloured at once: NOT pastels, tints or washed tones;
            NOT deep, dark or muted ones.
[BADGE]     form `roundel`: a disc with a scalloped rim, upper right, in a colour no cell
            carries. THREE type levels — a small label arced along the top of the rim, a
            large word across the middle, a year small beneath. A star device under the
            year. An inner ring inset from the scalloped edge. A soft shadow beneath the
            disc so it lifts off the cell behind it. Words: BEST OVERALL, GRINDERS, 2026.
[SHADOW]    a faint contact shadow beneath each grinder, identical for all five.

CONSTRAINTS — binding.
· The other FOUR units are equal to each other in prominence — none larger relative to its
  own cell, none brighter, none marked. Only the first attachment is favoured.
· Every grinder reads clearly against the cell it stands on.
· Every letter on the roundel sits inside the disc with visible margin, and the roundel
  does not touch a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party
  award mark. The units carry only the printing their own references carry — invent no
  lettering.
· No person, no scene, no room.
```

---

## 2 — five robot mops · hero LARGEST, off-centre · `laurel`

```
TYPE: lede-collage v0.9 — SET 3 CELL 2
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every mop is clean and as-new — housings unmarked, pads bright.
[LAYOUT]    blocks of flat colour of UNEQUAL size, overlapping across the frame at slight
            angles, the five mops laid across them.
[HERO]      the FIRST attachment is rendered clearly LARGEST of the five and sits OFF
            CENTRE, to one side. Size alone marks it; it is not centred.
[PALETTE]   four DIFFERENT hues across the blocks — not one colour in four shades. Every
            one is BOTH light AND strongly coloured at once: NOT pastels, tints or washed
            tones; NOT deep, dark or muted ones.
[BADGE]     form `laurel`: a wreath of two laurel branches meeting at the base, enclosing
            the words, in a colour no block carries. THREE type levels — a small label at
            the top between the branch tips, a large word in the middle, a year small at
            the base. The branches are the device. A soft shadow behind the wreath.
            Words: EDITOR'S PICK, ROBOT MOPS, 2026.
[SHADOW]    a faint contact shadow beneath each mop, identical for all five.

CONSTRAINTS — binding.
· The other FOUR units are equal to each other in prominence — none larger than another,
  none brighter, none marked. Only the first attachment is favoured.
· Every mop reads clearly against the blocks behind it.
· Every letter sits inside the wreath with visible margin, and the wreath does not touch
  a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party
  award mark. The units carry only the printing their own references carry — invent no
  lettering.
· No person, no scene, no room.
```

---

## 3 — five air fryers · hero CENTRE, equal size · `starburst`

**Tests whether POSITION alone makes a hero.** If it does, the clause can stop demanding size.

```
TYPE: lede-collage v0.9 — SET 3 CELL 3
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every fryer is clean and as-new — baskets bright, panels unmarked.
[LAYOUT]    five upright panels marked out by thin rules, of UNEQUAL width and stepped to
            different heights. One fryer per panel, each filling its panel.
[HERO]      the FIRST attachment sits in the CENTRE panel. Its panel and its unit are the
            SAME SIZE as the others — position alone marks it as the page's own product.
[PALETTE]   three DIFFERENT hues distributed across the panels and the ground behind them,
            one panel carrying a smooth two-hue gradient. All are BOTH light AND strongly
            coloured: NOT pastels or washed tones; NOT deep, dark or muted ones.
[BADGE]     form `starburst`: a many-pointed star shape, upper left, in a colour no panel
            carries. THREE type levels — a small label across the top, a large word in the
            middle, a year small beneath. A thin ring of dots inset inside the points is
            the device. A soft shadow behind the star.
            Words: TOP RATED, AIR FRYERS, 2026.
[SHADOW]    a faint contact shadow beneath each fryer, identical for all five.

CONSTRAINTS — binding.
· All five units are the same size. Only POSITION marks the first attachment; nothing
  else favours it, and the other four are equal to each other.
· Every fryer reads clearly against its own panel.
· Every letter sits inside the star with visible margin, and the star does not touch a
  frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party
  award mark. The units carry only the printing their own references carry — invent no
  lettering, and no reading is legible on any control panel.
· No person, no scene, no room.
```

---

## 4 — five electric scooters · hero LARGEST and CENTRE · `shield`

```
TYPE: lede-collage v0.9 — SET 3 CELL 4
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every scooter is clean and as-new — decks unscuffed, tyres unworn.
[LAYOUT]    five cells with rounded corners of clearly UNEQUAL size, tiled with even
            margins between them. One scooter per cell.
[HERO]      the FIRST attachment sits in the CENTRE cell and that cell is the LARGEST,
            noticeably bigger than any other. It is the page's own product.
[PALETTE]   four DIFFERENT hues across the five cells — not one colour in five shades.
            Every one is BOTH light AND strongly coloured at once: NOT pastels, tints or
            washed tones; NOT deep, dark or muted ones.
[BADGE]     form `shield`: a crest with a pointed base, sitting on the corner of the hero
            cell, in a colour no cell carries. THREE type levels — a small label across the
            top, a large word in the middle, a year small at the point. A horizontal rule
            separating label from word is the device. A bevel or inner border inset from
            the shield's edge, and a soft shadow behind it.
            Words: BEST OVERALL, SCOOTERS, 2026.
[SHADOW]    a faint contact shadow beneath each scooter, identical for all five.

CONSTRAINTS — binding.
· The other FOUR units are equal to each other in prominence — none larger relative to its
  own cell, none brighter, none marked. Only the first attachment is favoured.
· Every scooter reads clearly against the cell it stands on.
· Every letter sits inside the shield with visible margin, and the shield does not touch
  a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party
  award mark. The units carry only the printing their own references carry — invent no
  lettering.
· No person, no scene, no room.
```

---

## 5 — five travel kettles · hero CENTRE and LARGEST · `seal`

**`seal` is the only form repeated from set 2**, because it was the best of the five there —
a toothed rim, a dotted ring, two sizes. Here it is asked for the full five-point finish, so
the difference between set 2's seal and this one measures the standard itself.

```
TYPE: lede-collage v0.9 — SET 3 CELL 5
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every kettle is clean and as-new — bodies unmarked, spouts bright.
[LAYOUT]    no cells and no divisions. The five kettles arranged across one uninterrupted
            ground in a reading order the eye follows.
[HERO]      the FIRST attachment sits at the CENTRE of the arrangement and is rendered
            clearly LARGEST. It is the page's own product.
[GROUND]    one smooth gradient filling the frame, travelling between two hues. Choose how
            far it travels. Both ends are BOTH light AND strongly coloured at once: NOT
            pastels or washed tones; NOT deep, dark or muted ones.
[BADGE]     form `seal`: a circular stamp with a toothed rim, upper right, clear of every
            kettle, in a colour neither end of the gradient carries. THREE type levels — a
            small label arced along the top of the rim, a large word across the middle, a
            year small beneath. A ring of small dots inset inside the rim is the device.
            A soft shadow beneath the disc.
            Words: BEST OVERALL, TRAVEL KETTLES, 2026.
[SHADOW]    a faint contact shadow beneath each kettle, identical for all five.

CONSTRAINTS — binding.
· The other FOUR units are equal to each other in size and prominence. Only the first
  attachment is favoured.
· The gradient is perfectly smooth — no banding, no grain, no vignette.
· Every kettle reads clearly against the part of the gradient it stands on.
· Every letter sits inside the disc with visible margin, and the seal does not touch a
  frame edge or overlap a kettle.
· No rank number, price, star rating row, certification seal of a real body, press logo or
  third-party award mark. The units carry only the printing their own references carry —
  invent no lettering.
· No person, no scene, no room.
```

---

## 6 — five hair dryers · NO HERO · CONTROL

**Built the old way: five equal units, nothing favoured.** It is cell 1's construction with
the hero removed, and it is here so the hero can be judged against its own absence. If a
reader cannot tell cell 1 from cell 6, placement is not doing the work the owner needs.

```
TYPE: lede-collage v0.9 — SET 3 CELL 6, CONTROL
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every dryer is clean and as-new — barrels unmarked, nozzles seated.
[LAYOUT]    five rectangular cells of UNEQUAL size tiled edge to edge with no gaps. One
            dryer per cell, each cut out and scaled to fill its own cell.
[PALETTE]   five DIFFERENT hues, one per cell — not one colour in five shades. Every one is
            BOTH light AND strongly coloured at once: NOT pastels, tints or washed tones;
            NOT deep, dark or muted ones.
[BADGE]     form `roundel`: a disc with a scalloped rim, upper right, in a colour no cell
            carries. THREE type levels — a small label arced along the top of the rim, a
            large word across the middle, a year small beneath. A star device under the
            year. An inner ring inset from the scalloped edge. A soft shadow beneath the
            disc. Words: BEST OVERALL, HAIR DRYERS, 2026.
[SHADOW]    a faint contact shadow beneath each dryer, identical for all five.

CONSTRAINTS — binding.
· ALL FIVE units are equal to each other in prominence — none larger relative to its own
  cell, none centred, none brighter, none marked. No unit is the hero.
· Every dryer reads clearly against the cell it stands on.
· Every letter on the roundel sits inside the disc with visible margin, and the roundel
  does not touch a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party
  award mark. The units carry only the printing their own references carry — invent no
  lettering.
· No person, no scene, no room.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **Cell 1 against cell 6 — is the hero visible at a glance?** | `PARTS/hero`. If a reader cannot tell them apart, placement alone does not do what the owner's pipeline needs and the clause must reach for something stronger |
| 2 | **Cell 3 — does CENTRE alone make a hero at equal size?** | whether the clause needs size or whether position is enough. Size costs the other four; position does not |
| 3 | **Cell 2 — does LARGEST alone work off-centre?** | the other half of the same question |
| 4 | **Do the five badges carry all five finish points — three type levels, a device, a shaped silhouette, arced text, a shadow?** | the FINISH standard. Set 2's five met the two-point spec and the owner still called them unfinished |
| 5 | **Cell 5's seal against set 2's seal — did the standard raise it?** | the only repeated form, and the cleanest read on whether the new points are the right ones |
| 6 | **Did arced text render legibly, or come back as gibberish on a curve?** | text on a curve is harder than flat text, and printed lettering already fails often enough to be worth watching |
| 7 | **Did the hero cost the type its purpose — does the frame now claim a verdict rather than an index?** | `PURPOSE` says the type *"claims nothing about possession — only that these are the entries"*. A hero plus a badge may have moved it into `lede-winner`'s argument |
| 8 | **Did any unit come back with invented lettering?** | six instances across the namespace so far |

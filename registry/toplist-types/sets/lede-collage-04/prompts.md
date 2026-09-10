# `lede-collage` set 4 — the two new layouts, the badge that never rendered, and a different fix for invented lettering

Written against **`lede-collage` v0.11**. Owner, 2026-09-09: *"scooter hỏng"*, and a list of
eight frames instructing that the type includes `split-frame` and `polaroid` — confirmed as
`collage` when the reversal was put back to them.

## What set 3 settled

**SIZE is the operative variable for the hero, not centre.** Centre plus largest reads (cells
1, 5); largest alone off-centre reads (cell 2); centre alone at equal size does not (cell 3).

**And the composition WANTS a hero.** Cell 6 was instructed *"no unit is the hero"* and
produced one anyway — as set 2's control had. **Two of two no-hero controls produced a
hero.** Sets 1 and 2 were not merely wrong about the pipeline; they were fighting the layout.

**The five-point badge FINISH standard delivered 5 of 5** on its first outing — three type
levels, a device, a shaped silhouette, arced text, a shadow. `shield` is the one form still
untested, because cell 4 never rendered.

## The one thing that has not improved in four sets

**Invented lettering: nine instances across the namespace, every one under a prompt that
banned it.** Set 3 alone produced `RoboClean`, `TRAVEL KETTLE`, and four garbled fryer
brands, and every one of those cells carried *"invent no lettering"*.

G10's own text diagnoses this exactly: *"a prohibition without a sanctioned escape route is
resolved by the model in whichever direction it likes"*. **A ban with nowhere to go is not an
instruction.** So five cells below replace the ban with a DESTINATION —

> *Where a reference does not show a readable brand mark, leave that surface plain and
> unbranded. An unbranded surface is correct; an invented one is not.*

— and **cell 6 keeps the old ban alone**, so the change is attributable rather than assumed.

## The cells

| cell | products | layout | subject kind | badge | tests |
|---|---|---|---|---|---|
| 1 | 1 carry-on suitcase | **`split-frame`** | one product, two views | **`shield`** | the new layout AND the form that never rendered |
| 2 | 1 running belt | **`polaroid`** | one product, several views | none | the other new layout |
| 3 | 5 stand mixers | `colour-cells` | several products | `roundel` | hero by SIZE on new products |
| 4 | 5 sleeping bags | `blocks` | several products | `laurel` | hero largest off-centre, confirming set 3 cell 2 |
| 5 | 1 smartwatch | **`split-frame`** | one product, two views | none | does `split-frame` read as this type with no mark at all? |
| 6 | 5 toasters | `open` gradient | several products | `seal` | **CONTROL — keeps the old lettering ban** |

**Cells 1, 2 and 5 carry ONE product.** Three of the type's twelve corpus frames do the same,
and it sits awkwardly against `products_in_frame: many`, which `mapping/toplist-rules.md`
reads as needing three or more on the input. The frontmatter is not changed on a render;
these cells exist to find out whether the picture works before that decision is put.

Six categories, eighteen products, none used in sets 1–3. Attachments: 1, 1, 5, 5, 1, 5.

---

## 1 — carry-on suitcase · `split-frame` · `shield`

```
TYPE: lede-collage v0.11 — SET 4 CELL 1
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the carry-on
            suitcase — preserve shape, proportions, material, finish, colour and every
            printed mark exactly.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] the suitcase is clean and as-new — shell unscuffed, wheels unworn.
[LAYOUT]    the frame divided vertically into two halves that meet without a gutter.
[LEFT]      the suitcase cut out, upright, centred in its half, on a designed ground
            patterned with a regular field of small repeated glyphs — ticks and crosses in
            a tone slightly deeper than the ground they sit on.
[RIGHT]     a real photograph of the SAME suitcase open on a wooden floor, packed, shot
            from above, filling its half. A real place, real light, no cut-out.
[PALETTE]   the left ground is BOTH light AND strongly coloured at once: NOT a pastel,
            tint or washed tone; NOT a deep, dark or muted one. The right half keeps its
            own photographic colour.
[BADGE]     form `shield`: a crest with a pointed base, sitting on the left half clear of
            the suitcase, in a colour the patterned ground does not carry. THREE type
            levels — a small label across the top, a large word in the middle, a year small
            at the point. A horizontal rule between label and word is the device. A bevel
            or inner border inset from the shield's edge, and a soft shadow behind it.
            Words: BEST OVERALL, CARRY-ON, 2026.

CONSTRAINTS — binding.
· Where the reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· Both halves show the SAME suitcase — same shell colour, same handle, same wheels.
· Every letter on the shield sits inside the shield with visible margin, and the shield
  does not touch a frame edge or cross the halves' boundary.
· No rank number, price, star rating row, certification seal, press logo or third-party
  award mark.
· No person beyond a hand if the packed shot needs one; no face.
```

---

## 2 — running belt · `polaroid`

```
TYPE: lede-collage v0.11 — SET 4 CELL 2
REGISTER: graphic product composition, one frame, no words in it.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the running belt —
            preserve shape, proportions, material, finish, colour and every printed mark
            exactly.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] the belt is clean and as-new — webbing unfrayed, clip bright.
[LAYOUT]    three instant-print frames — white borders, thicker at the bottom — overlapping
            each other at slight angles across the frame, each holding one view.
[VIEWS]     print 1: the belt worn at the waist, cropped at hip and ribs. Print 2: the belt
            laid flat, seen from above, whole. Print 3: a close view of the clip and the
            pocket opening. All three are the SAME belt.
[GROUND]    one designed field behind the prints, BOTH light AND strongly coloured at once:
            NOT a pastel, tint or washed tone; NOT a deep, dark or muted one, carrying a
            fine halftone dot screen.
[SHADOW]    each print casts a small soft shadow onto the ground and onto the print beneath.

CONSTRAINTS — binding.
· Where the reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· All three prints show the SAME belt — same colour, same webbing, same clip.
· No handwriting on the prints, no labels, no captions, no date stamps, no words anywhere.
· The halftone falls on the ground only, never on a print or on the belt.
· No print touches a frame edge.
```

---

## 3 — five stand mixers · `colour-cells` · hero by SIZE · `roundel`

```
TYPE: lede-collage v0.11 — SET 4 CELL 3
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every mixer is clean and as-new — bowls bright, housings unmarked.
[LAYOUT]    five rectangular cells of UNEQUAL size tiled edge to edge with no gaps. One
            mixer per cell, each cut out and scaled to fill its own cell.
[HERO]      the FIRST attachment is rendered clearly LARGEST of the five, in the largest
            cell. It is the page's own product.
[PALETTE]   five DIFFERENT hues, one per cell — not one colour in five shades. Every one is
            BOTH light AND strongly coloured at once: NOT pastels, tints or washed tones;
            NOT deep, dark or muted ones.
[BADGE]     form `roundel`: a disc with a scalloped rim, upper right, in a colour NO CELL
            carries. THREE type levels — a small label arced along the top of the rim, a
            large word across the middle, a year small beneath. A star device under the
            year. An inner ring inset from the scalloped edge. A soft shadow beneath the
            disc. Words: BEST OVERALL, STAND MIXERS, 2026.
[SHADOW]    a faint contact shadow beneath each mixer, identical for all five.

CONSTRAINTS — binding.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence — none larger relative to its
  own cell, none brighter, none marked. Only the first attachment is favoured.
· The roundel's colour appears nowhere else in the frame.
· Every letter on the roundel sits inside the disc with visible margin, and the roundel
  does not touch a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party
  award mark.
```

---

## 4 — five sleeping bags · `blocks` · hero LARGEST off-centre · `laurel`

```
TYPE: lede-collage v0.11 — SET 4 CELL 4
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every bag is clean and as-new — shells unmarked, zips bright.
[LAYOUT]    blocks of flat colour of UNEQUAL size, overlapping across the frame at slight
            angles, the five bags laid across them. Flat blocks, not slabs in perspective.
[HERO]      the FIRST attachment is rendered clearly LARGEST of the five and sits OFF
            CENTRE, to one side. Size alone marks it.
[PALETTE]   four DIFFERENT hues across the blocks — not one colour in four shades. Every
            one is BOTH light AND strongly coloured at once: NOT pastels, tints or washed
            tones; NOT deep, dark or muted ones.
[BADGE]     form `laurel`: a wreath of two branches meeting at the base, enclosing the
            words, in a colour NO BLOCK carries. THREE type levels — a small label at the
            top between the branch tips, a large word in the middle, a year small at the
            base. The branches are the device. A soft shadow behind the wreath.
            Words: EDITOR'S PICK, SLEEPING BAGS, 2026.
[SHADOW]    a faint contact shadow beneath each bag, identical for all five.

CONSTRAINTS — binding.
· Where a reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· The other FOUR units are equal to each other in prominence. Only the first attachment
  is favoured.
· The blocks are flat shapes on one plane — no perspective, no thickness, no 3D slabs.
· Every letter sits inside the wreath with visible margin, and the wreath does not touch
  a frame edge.
· No rank number, price, star rating row, certification seal, press logo or third-party
  award mark.
```

---

## 5 — smartwatch · `split-frame`, NO badge and NO words

**Tests whether `split-frame` reads as this type on its own.** Two of the corpus's twelve
frames are exactly this and neither carries a mark, so this is the form the corpus supports
and cell 1 is the decorated variant.

```
TYPE: lede-collage v0.11 — SET 4 CELL 5
REGISTER: graphic product composition, one frame, no words in it.

[PRODUCT REFERENCE] one attached photo. It is the exact reference for the smartwatch —
            preserve shape, proportions, material, finish, colour and every printed mark
            exactly.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] the watch is clean and as-new — case unscratched, strap unworn.
[LAYOUT]    the frame divided vertically into two halves that meet without a gutter.
[LEFT]      the watch cut out, face on, centred in its half, on a designed ground patterned
            with a regular field of small repeated glyphs — ticks and crosses in a tone
            slightly deeper than the ground they sit on.
[RIGHT]     a real photograph of the SAME watch worn on a wrist, arm resting on a table,
            filling its half. A real place, real light, no cut-out.
[PALETTE]   the left ground is BOTH light AND strongly coloured at once: NOT a pastel,
            tint or washed tone; NOT a deep, dark or muted one. The right half keeps its
            own photographic colour.

CONSTRAINTS — binding.
· Where the reference does not show a readable brand mark, leave that surface plain and
  unbranded. An unbranded surface is correct; an invented one is not.
· Both halves show the SAME watch — same case, same strap, same face.
· No reading is legible on the watch face in either half.
· No word, number, badge, mark or logo added anywhere in the frame.
· No face; the wrist and forearm only.
```

---

## 6 — five toasters · `open` gradient · `seal` · CONTROL

**This cell keeps the OLD lettering ban** — the bare prohibition that has now failed nine
times — while the other five carry the destination clause. It is the only way to tell whether
the new wording did anything.

```
TYPE: lede-collage v0.11 — SET 4 CELL 6, CONTROL
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every toaster is clean and as-new — slots clear, bodies unmarked.
[LAYOUT]    no cells and no divisions. The five toasters arranged across one uninterrupted
            ground in a reading order the eye follows.
[HERO]      the FIRST attachment sits at the CENTRE and is rendered clearly LARGEST.
[GROUND]    one smooth gradient filling the frame, travelling between two hues. Choose how
            far it travels. Both ends are BOTH light AND strongly coloured at once: NOT
            pastels or washed tones; NOT deep, dark or muted ones.
[BADGE]     form `seal`: a circular stamp with a toothed rim, upper right, clear of every
            toaster, in a colour neither end of the gradient carries. THREE type levels — a
            small label arced along the top of the rim, a large word across the middle, a
            year small beneath. A ring of small dots inset inside the rim is the device.
            A soft shadow beneath the disc. Words: BEST OVERALL, TOASTERS, 2026.
[SHADOW]    a faint contact shadow beneath each toaster, identical for all five.

CONSTRAINTS — binding.
· The units carry only the printing their own references carry — invent no lettering.
· The other FOUR units are equal to each other in size and prominence.
· The gradient is perfectly smooth — no banding, no grain, no vignette.
· Every letter sits inside the disc with visible margin, and the seal does not touch a
  frame edge or overlap a toaster.
· No rank number, price, star rating row, certification seal of a real body, press logo or
  third-party award mark.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **Cells 1–5 against cell 6 — did the DESTINATION clause reduce invented lettering?** | nine instances have survived a bare ban. If the destination works, it belongs in every prompt this library writes, not only in this type |
| 2 | **Cell 1 — does `shield` deliver the five finish points?** | the last untested badge form; cell 4 of set 3 never rendered |
| 3 | **Cells 1 and 5 — does `split-frame` hold the SAME product across a cut-out and a real photograph?** | the layout's whole mechanism. Two halves of one product in one pass is the hardest identity problem here since the boot panels |
| 4 | **Cell 5 against cell 1 — does `split-frame` read as this type without a mark?** | the corpus form carries none, so cell 5 is the evidenced version and cell 1 the decorated one |
| 5 | **Cell 2 — do three instant prints hold one product across three views?** | `polaroid`, one observation, never prompted |
| 6 | **Cells 3 and 4 — is the hero visible on new products?** | `PARTS/hero` at size, confirming set 3 on categories it has not seen |
| 7 | **Cell 4 — did the blocks stay flat?** | set 3's blocks came back as 3D slabs in perspective, which nothing asked for |
| 8 | **Did any badge take a colour already in the frame?** | set 3 cell 1's roundel did, against its own constraint. Three cells now state it explicitly |

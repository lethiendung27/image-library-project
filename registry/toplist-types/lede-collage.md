---
id: lede-collage
version: "0.22"
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
  rather than the testing. The input carries five distinct competing products; that N is
  five is the format's own fact and is stated in `registry/toplist-instruction.md`.
  Take it over lede-lineup where the units are too unlike each other in size to share a
  surface honestly, or where no plausible single surface exists for the category.

## BOUNDARY
**Against `lede-lineup`** — assembled against photographed, enumeration against
possession. See that file; the distinction is stated there once and is not restated here.

**Against `lede-winner`, on ADR-074's boundary: a winner frame carries display type, a mark,
or both; a collage carries neither and argues with the units alone.** The 2026-09-09-D
curation applied that line and moved three frames out of this type on it.

**The overlay text IS part of this type** (ADR-071) and `text_layer: [title, badge]` stands,
so **G16 binds every word and the badge here**. But the corpus support for a BADGE has gone:
both badge-bearing frames the 0.3 file counted were re-filed to `lede-winner` at batch D, and
**not one of the twelve frames this type now holds carries a verdict mark**. Three carry a
small lower-corner label — `DEALS`, a brand line — and two carry a repeated tick-and-cross
pattern as a ground treatment, which is decoration rather than a mark.

**So the badge is permitted, unevidenced in this type, and now WANTED** — owner instruction of
2026-09-09 after set 1: *"hãy thêm badge với style riêng, đặc sắc."* It arrives on instruction
rather than on corpus support, and MARKS says which. The distinction against `lede-winner`
still holds and is not the badge's presence: a winner frame is ONE product presented as
chosen, a collage is five presented as the field.

What may be printed is the page's own line about its own ranking. A third-party award mark
stays refused here as everywhere in this namespace — G16's `LAW, not taste` row, and the
question `toplist-instruction.md` records as still the owner's.

## SKELETON
```
TYPE: lede-collage v0.22
REGISTER: graphic product composition, one frame.

[PRODUCT REFERENCES]  one attached photo per unit.                      -> G1, and see BLOCK
[CUT-OUTS]            FIVE units, each cleanly cut out, no shared scene.
[COUNT]               EXACTLY five; each reference used ONCE.      -> PARTS/count
[FIELD]               every unit plausibly IS the category named. -> PARTS/field-coherence
[HERO]                the page's own product: LARGEST, centre optional. -> PARTS/hero
[ARRANGEMENT]         the other four equal to each other; cells may differ. -> PARTS/arrangement
[LAYOUT]              one of eight index layouts, named.      -> PARTS/layout
[PALETTE]             SEVERAL hues across the cells.          -> PARTS/palette
[GROUND]              a DESIGNED field: light AND coloured.   -> PARTS/ground
[GRAPHICS]            ground, frame and accent elements, stacked. -> PARTS/graphics
[SHADOW]              a faint contact shadow per unit or none at all, applied equally.

[TITLE]               the page's own line about its own ranking. Optional. -> G16/title
[BADGE]               one mark, INSIDE the hero's cell.  Optional. -> MARKS/PLACEMENT
```

**G7 exemption, narrow.** Cut-outs on a flat ground are a graphic layer rather than a
scene, which G7's own scope note already reads that way for a product knockout. Every
other G7 test still binds.

## PARTS

**`layout`** — **the axis this type was missing, and the owner's main ask.** Owner,
2026-09-09: *"cần đa dạng layout hơn… mở style về background tươi sáng, sặc sỡ, có thể dùng
đa dạng nền gradient/solid/… visual effect như half tone, grain, textures"*. Measured on the
seven frames the type actually holds after the 2026-09-09-D curation:

| form | what it is | observations |
|---|---|---|
| `open` | cut-outs arranged on one uninterrupted ground, no cells | **1** — the type's founding frame |
| `colour-cells` | rectangular cells of flat colour tiled edge to edge, one product per cell | **1** |
| `blocks` | irregular colour blocks, overlapping, products laid across them | **1** |
| `outlined-panels` | upright panels on one ground, each with a thin rule — **the corpus pair are EQUAL and set 9 proved that is a requirement** | **2** |
| `rounded-cells` | cells of unequal size with rounded corners on one ground | **1** |
| `pinboard` | photographs pinned to a real board, edges and shadows visible | **1** |
| `split-frame` | the frame halved: a cut-out on a patterned designed ground beside a real photograph of the same product **from a DIFFERENT angle, usually in use** | **2** |
| `polaroid` | instant-print frames overlapping on a designed ground, one view per print | **1** |

**Eight layouts across twelve frames is the finding.** The type is not one composition with a
colour variable; it is a family of index layouts. A prompt names one and commits to it.

**Three of the twelve carry ONE product, not five** — the two `split-frame` frames and the
`polaroid`. That sits awkwardly against `products_in_frame: many`, which
`mapping/toplist-rules.md` layer 1 reads as needing three or more products on the input.
**The frontmatter is not changed here**: it is a routing promise, and whether this type
admits a one-product frame is a decision with consequences beyond the picture. Flagged.

**`outlined-panels` takes EQUAL panels — owner instruction, 2026-09-10**, and the corpus said
so first. This file recorded *"the corpus pair are equal, which is not a requirement"* — the
second half of that sentence was my gloss, not a measurement, and every prompt since asked for
panels *"of unequal width, stepped to different heights"*.

**Set 9 cell 4 is what that buys.** Five camping stoves in panels stepped down left to right,
and the four non-hero units shrank with their panels: the frame reads as a **descending
staircase**, a bar chart with stoves on it, and the rightmost unit is a third the size of its
neighbour. The no-favoured-unit law says the other four are equal in prominence, and **the
layout instruction broke it from inside** — no constraint could hold, because the geometry
being asked for was a ranking.

*The library already knew this in another register: N shapes each bigger than the last is a
chart idiom, and the remedy is one tapering shape rather than a graded series.*

**The resolution keeps the hero, because "equal" was never about all five.** `ARRANGEMENT` says
the other FOUR are equal to each other. So: **the hero's panel is wider; the remaining four are
equal to each other in width and in height, and none is stepped.** The two corpus frames carry
no hero at all, which is why they are equal 2 of 2 and why they do not settle the hero's panel.

**`pinboard` is the outlier that keeps the ground clause honest**: it measures texture
**16.0** against 1.0–2.8 for the other six, because a corkboard is photographed. Its ground
is a real surface and the cut-outs are prints, not knockouts.

**`subject`** — **three kinds now, all of them settled by the owner naming frames.**

| kind | what it is | observations |
|---|---|---|
| several products | five distinct competing units | **8** |
| one subject, several states | the same person in three outfits, one per panel | **2** |
| one product, several views | the same unit worn and flat, one per print | **2** |

The second and third were both shapes an earlier version of this file called foreign and
wanted split out. **Each is here because the owner named a frame carrying it**, and the third
arrived at 0.10 with the `polaroid` and `split-frame` layouts. What the type is NOT is a
single product presented alone — that is `lede-winner` or `07-identity-pack`.

**`ground`** — a DESIGNED field. Re-measured on the corrected seven, and **the old clause
does not survive it**:

| | old clause, n=5 | corrected, n=7 |
|---|---|---|
| texture | 1.9 | **1.0 – 2.8**, plus the pinboard at 16.0 |
| value | 0.90 | **0.77** median, 0.55 – 0.98 |
| saturation | 0.49 | **0.41** median, 0.24 – 0.49 |
| hue spread | *"177/175/177 or under 13, nothing between"* | **1°, 2°, 27°, 47°, 98°, 174°, 177°** |

**The bimodal claim is refuted.** 0.4 wrote *"either a two-hue diagonal gradient or one flat
tone, and nothing in between"* on five records, and three of those five were the wrong shape.
The corrected set runs continuously from a single tone to half the wheel: **a gradient is a
CHOICE with a free amount of travel, not one of two fixed settings.**

- **Smooth, except where the layout is photographed.** Six of seven read 1.0–2.8; the
  pinboard is a real board and is the exception the `layout` axis names.
- **Light AND coloured — both named, or the model pays for one with the other.** This is
  imported from `lede-authority`, which proved it with a control: nine prompts naming chroma
  alone returned value 0.35 / saturation 0.99; three naming value alone returned 0.92 / 0.29;
  four naming BOTH and refusing both failure modes returned 0.93–1.00 / 0.59–0.64. **A clause
  naming two properties that trade against each other must name both.**

**`count`** — **the frame holds EXACTLY five units and each reference appears exactly once.
New at 0.15, because set 6 cell 1 came back with SIX.** Owner, 2026-09-10: *"một số ảnh sai
số lượng sản phẩm"*.

Five rice-cooker references produced six positions: the hero on an open teal field, plus five
cells — and the sixth was filled by **rendering one Panasonic twice**, at two angles, in the
purple cell and the pink cell. Five distinct products in six places, on a page that says
there are five.

**The mechanism is the hero escaping the grid.** That cell alone asked for cells *"tiled edge
to edge with no gaps"*, and that is the one layout instruction the render ignored: it left a
large open ground, put the hero on it, and then still built five cells for five attachments.
Where the hero is unambiguously IN one of the N cells — set 6 cells 2, 4 and 6, all the same
sentence shape — the count held. **1 of 6, and it is the frame whose layout also failed.**

**This is `field-coherence`'s fault repeated exactly.** The word *five* appeared in every set-6
prompt, in `[LAYOUT]`, in `[PALETTE]`, and inside the binding line *"ALL FIVE units are rice
cookers"* — but every one of those states five as a property of something else. **No prompt in
this library has ever made the COUNT its own requirement**, and a count stated only as an
adjective is not a count the model has to meet. It gets its own clause, and it names the
repeat as well as the total, because the failure was a duplicate rather than an invention.

### The clause failed on its first outing, and the failure is more useful than the clause

Set 7's long draft carried it verbatim — *"There are EXACTLY FIVE units in the frame — not
four, not six. Each of the five attached photos is used exactly ONCE"* — in all six prompts,
pre-flight verified. **Cell 1 returned six anyway**, five distinct projectors with one silver
cube rendered twice at two angles. `PARTS/count` stands at **0 of 1**.

**Both failures are the same picture, and it is a LAYOUT failure wearing a count failure's
clothes.** Set 6 cell 1 and set 7 cell 1 are both `colour-cells`, both put the hero on a large
open field rather than in a cell, and both then built five cells for five references. The
sixth position is not the model losing count; it is the model correctly filling a grid it
built correctly, beside a hero it placed outside the grid.

| | hero placed | cells built | units |
|---|---|---|---|
| set 6 c1, set 7 c1 · `colour-cells` | on an open ground | 5 | **6** |
| set 6 c2 `rounded-cells`, c4 `outlined-panels`, c6, set 7 c2 | IN one of the cells | 5 | 5 |

**A prohibition cannot fix it and a count cannot fix it — GEOMETRY can, and it did, 2 of 2.**
Round 3 measured this namespace's own lever: geometry delivered 1 of 1 while four prescriptions
of taste were ignored 4 of 4. Set 7's revision said where the hero's cell IS instead of
asserting that it is one of five, and the two cells that got it are the two that had failed:

| cell | what the prompt said about the hero's cell | units |
|---|---|---|
| set 7 c1 ice makers | *"fills the LEFT HALF; the other four tile the right half as a 2x2"* | **5** |
| set 7 c2 label printers | *"fills the TOP HALF; the other four in a row across the bottom"* | **5** |
| set 7 c5 turntables | *"five upright panels of unequal width stepped to different heights"* | **6** |

`colour-cells` had produced six twice and produced five the first time it was given a share of
the frame. **The one count failure in the set is the cell that was given a PROPERTY instead of
a geometry** — five panels described by their variety, returned as a 2×3 grid of six.

**So the clause is: name the hero's cell as a share of the frame, and name what the rest fill.**
A layout described only by how its cells differ is a description the model can satisfy with a
different number of them.

**One clause was lost in the length pass and it should not have been.** The long draft also
carried *"The hero's cell is one of the five, not a ground behind them"*; the compression that
followed cut it as prose. It had already failed once, so nothing is owed to it — but it was an
earned clause removed by a pass whose job was to remove unearned ones, and that is exactly the
mistake a removal step can make.

**`distinctness`** — **five references must return five different PRODUCTS, and set 7 cell 3
returned one product in four colours.** New at 0.16.

The garment steamers came back as a coral, a lime, an orange and a blue unit sharing **one
silhouette, one vent pattern, one trigger and one conical tank**. Only the fifth — a grey
model with a base station and a hose — is a different product. The frame reads as a paint-chip
chart, not as a field of five makers, and the page's whole claim is that these are five
competing things.

**It is the same failure as the count duplicate, one step further on.** Cell 1 rendered one
reference twice and called it two units; cell 3 rendered one FORM five times and coloured it
differently each time. Both are the model economising on identity across a frame it is
assembling in one pass, which is what ADR-067 named as the hardest thing to hold and the
reason an invariants block is written before the regions are described.

**The remedy is the inverse of an invariants block: state the VARIANTS.** Where a prompt needs
one person the same across two panels, it names what must not change. Where it needs five
products different across five cells, it has to name what must — silhouette, proportion and
body, not colour. A clause that says only *five different makers* is asserting a fact about
the world, and the model can satisfy it with five colours of one mould.

**`field-coherence`** — **every unit must plausibly BE the category the frame names, and this
has now failed four times.** Owner, 2026-09-09: *"kettle bị sai"*.

Set 3 cell 5 was captioned TRAVEL KETTLES. The hero is a collapsible silicone travel kettle;
the other four are **ordinary kitchen kettles** — a gooseneck pour-over, a 1.7-litre plastic
jug, a black digital kettle, a corded steel kettle. **Four of five are not the category.**

| set | asked for | came back as |
|---|---|---|
| `lede-authority` set 5 | five running watches | dress chronographs on steel bracelets |
| set 3 cell 5 | five travel kettles | one travel kettle and four kitchen kettles |
| set 3 cell 3 | five air fryers | five air fryers, four with garbled brand marks |
| **set 6 cell 5** | **five pizza ovens** | **four pizza ovens and a countertop toaster oven** |

**No prompt in this library has ever required the units to be plausible for the category it
prints.** The badge says TRAVEL KETTLES and the frame shows kettles that do not travel, which
is a claim the picture contradicts — closer to `argument-faults.md` than to craft. A prompt
naming a narrow category states it as a requirement of every unit, not only of the hero.

**The clause held 5 of 6 in set 6 — and the one that failed had NAMED the exact exclusion.**
That prompt read *"Not domestic ovens, not air fryers, not barbecues, **not toaster ovens**"*,
and a countertop toaster oven is what arrived: glass door, wire rack, digital display, two
knobs. **So a named exclusion list is not the instrument.** It is a prohibition without a
picture attached, and G10's own diagnosis applies — a ban with nowhere to send the model is
resolved in whichever direction it likes.

**The repair is a distinction, not a longer list: name what every unit must SHOW.** A positive
defining feature is checkable in the frame, where an exclusion is only checkable against a
category the model has already decided it satisfies. *"Every unit has a hinged clamshell with
a gridded waffle plate"* is a test the picture either passes or fails; *"not a sandwich press"*
is an argument. Set 7 states all six categories that way and keeps no exclusion list.

**`graphics`** — **the layer the owner asked for and this file had no vocabulary for.** Owner,
2026-09-09: *"chưa có nhiều graphic element linh hoạt, hiệu ứng"*. Counted off frames actually
seen, in this type's corpus and the namespace's:

| element | what it is | observations |
|---|---|---|
| `glyph-field` | a regular field of small repeated symbols across a ground | **2** — both `split-frame` frames |
| `cut-corner-frame` | a thin rule around a panel with notched or cut corners | **2** — the two shopping-diary frames |
| `halftone` | a dot screen over the ground, products left clean | **1** — the `polaroid` frame |
| `outline-echo` | a thin outline repeating a product's silhouette, offset behind it | **1** — a corpus cell holding outlined rectangles |
| `corner-label` | a small word with a tail or rule in a lower corner, not a verdict | **1** |
| `icon-pair` | small circular icons set in a corner | **1** |

**`corner-label` is RETIRED — owner instruction, 2026-09-10:** *"không được có chữ pick
đứng góc dưới màn hình (tôi cho là lỗi)"*. It had one corpus observation and it produced a
word in the frame's corner in four renders across sets 5–8, every one of them inside G10's
safe area. No prompt asks for it again. The element stays in the table above as a counted
observation, which is what that table is; what changes is that nothing may emit it.

**Borrowed from `lede-winner`'s corpus, untested here:** a dotted outline echoing a cut-out's
silhouette, and arcs radiating from behind a unit. **Both transferred in set 5** — the
outline-echo gave each bike light a coloured glow, the dotted outlines and the icon pair both
landed on the humidifiers — and set 6 used all four borrowed and counted elements again with
no failure of the element itself.

**They stack, and the CAP AT TWO IS STILL 1 OF 1 — set 6's control could not confirm it,
by its own construction.** Set 5 cell 5 stacked three — notched rules, a glyph field, a
halftone — and the frame stopped being a photograph: **all five cameras came back as flat
vector illustrations**, cartoon bodies with a drawn icon on the screen. Not busyness; a
register flip, and the one failure mode this layer has.

Set 6 cell 6 stacked three again on a different layout and different products, and **came
back fully photographic** — real fabric weave, metal specular, plastic wheel detail. That
looks like a refutation and it is not one:

| | layers | register named in the prompt? | came back |
|---|---|---|---|
| set 5 cell 5 · action cameras | 3 | no | **flat vector** |
| set 6 cell 6 · baby strollers | 3 | **yes**, explicitly | photographic |

**Two variables moved at once, so the frame answers neither question.** Set 6's own file said
so in advance — *"was it the cap or the constraint that saved it?"* — which is the control
doing the one thing a confounded control can still do: naming its own confound before the
render rather than after.

**Set 7's long draft was meant to settle it and its control did not render** — cells 4 and 6
came back empty, the second time a declared control has failed to arrive (set 3 cell 4 was the
first). So the cap is still 1 of 1.

### And the four frames that DID render put a better hypothesis in front of it: SIZE

Owner, 2026-09-10: *"hình ảnh sản phẩm thường bị 2d hoá"*. Graded by eye across every frame
this type has rendered where the register is legible:

| frame | layers | units rendered | register |
|---|---|---|---|
| set 7 c5 waffle makers · `open` | 2 | **all five large** | photographic 5 of 5, real brand marks |
| set 6 c6 strollers · `outlined-panels` | **3** | **all five large** | photographic 5 of 5 |
| set 7 c1 projectors · `colour-cells` | 2 | hero large, cells medium | photographic |
| set 7 c2 shredders · `rounded-cells` | 2 | hero large, four small | hero photographic, **four simplified** |
| set 7 c3 steamers · `blocks` | 1 | **all five small** | **four of five one mould, recoloured** |
| set 5 c5 action cameras · `outlined-panels` | **3** | **all five small** | flat vector 5 of 5 |

**Layer count does not order this table and unit SIZE does.** The two three-layer frames sit at
opposite ends, and the difference between them is that the strollers are rendered large and the
action cameras small. The one-layer steamers frame is the second worst in the set.

**That hypothesis is DEAD, and so is the layer ceiling. Set 7's revision killed both with one
frame rendered twice.**

Cell 3 — five hedge trimmers, `blocks`, one graphic layer — was rendered at 10:52 and again at
10:56 from **the same prompt, unchanged**. The 10:52 draw came back **flat vector**: hard dark
keylines, flat fills, drawn shading. The 10:56 draw came back **photographic**: real plastic,
real steel blades, legible Einhell, Sun Joe and EGO marks.

| the same prompt, four minutes apart | register |
|---|---|
| cell 3 at 10:52 | flat vector, 5 of 5 units |
| cell 3 at 10:56 | photographic, 5 of 5 units |

**One prompt cannot produce two registers because of a clause it carries in both.** So the
register of this type is a **run-to-run DRAW**, and every register finding this file has
recorded was a single draw being read as evidence about wording:

- 0.14's *"two layers; a third buys illustration"* — one frame.
- 0.16's *"a unit drawn small stops being photographed"* — five frames, no repeats, and it is
  refuted here anyway: set 7's turntables are drawn LARGE and came back vector, its wine
  coolers small and also vector, while the same-size ice makers and label printers came back
  photographic.

**Both hypotheses are withdrawn.** `PARTS/graphics` keeps the element table, which is counted
off frames and is not in doubt, and keeps *graphics never cross a product's face*, which has
held 16 of 16. **It no longer caps the layer count**, because the one observation that cap
rested on is now known to be a draw.

**What replaces them is a rule about EVIDENCE, not about pictures: on this type, one render is
one draw.** A register verdict needs the same prompt run more than once, and a set that reads a
single frame as proof about wording will keep inventing rules the next draw refutes. That is
namespace-level and is recorded in `registry/toplist-instruction.md`.

**Three measurements were attempted for this and all three were DISCARDED for failing their
own controls.** A local-flatness fraction put a known photographic frame at 17.4% against a
known flat-vector frame at 9.0%. A tone-entropy measure put the flat-vector frame *between* two
photographic ones. A connected-component count, whose control was simply the unit count, found
8, 16, 8, 7, 11 and 5 blobs where the eye counts 6, 5, 5, 5, 5 and 5. **The same cause defeats
all three and it is already recorded**: this type's layout axis means a frame has no single
ground and no separable subjects, which is the third bound in
`registry/toplist-instruction.md` §Ground. Nothing here is published as a number.

### The graphics vocabulary narrows to SURFACE TREATMENTS — owner instruction, 2026-09-10

*"graphic element chỉ nên dừng lại ở half tone effect và gradient, grainy, không tự vẽ thêm gây
rối hình"*. **This reverses the owner's own instruction of 2026-09-09** — *"chưa có nhiều graphic
element linh hoạt, hiệu ứng"* — which is what created `PARTS/graphics` in the first place, and
it is recorded as a reversal rather than smoothed over.

**What stays: halftone, gradient, grain.** Treatments of a surface that is already there.

**What is retired: everything DRAWN.** `glyph-field`, `cut-corner-frame`, `outline-echo`,
`icon-pair`, the borrowed dotted silhouette outlines and the borrowed radiating arcs. Set 11
cell 4 is the case the owner named: concentric arcs behind the hero read as a target and made
the frame busy, and cell 1's dotted outlines traced every umbrella rib and pole.

**Two of the retired elements have corpus support and that is the cost, stated.** `glyph-field`
has 2 observations and `cut-corner-frame` has 2 — the two `split-frame` frames and the two
shopping-diary frames. Retiring them departs from the corpus on instruction. The element table
above stays as the record of what was counted; what changes is that no prompt may emit them.

**The `split-frame` glyph field is the one exception**, because it is not an accent laid over a
composition — it IS that layout's designed half, and both corpus frames carry one.

**Graphics sit behind or beside a product, never across its face.** Held in all five of set 5
and all six of set 6.

**No frame has ever added a layer it was not asked for.** Set 6 asked for two in cells 1, 2,
4 and 5, one in cell 3 and three in cell 6, and every frame delivered exactly that count.
**"Exactly two, no third" holds as a COUNT at 5 of 5** — what is unproven is what happens
above it, not whether the number is obeyed.

**An accent that is described once appears once — and set 6 confirms the fix at 3 of 3.**
Set 5 cell 1 asked for *"a small corner-label in the lower left"* and got one **in every
cell** — five labels reading PICKS. A frame-level element says *one, in the frame's lower
left*; a cell-level element says *in each cell*. Set 6 said which in cells 3, 4 and 5 and
every one returned **exactly one**: one PICKS label, one drop-and-tooth icon pair, one PICKS
label. **The wording works and the clause is settled.**

**What the same fix broke, and it is the third instance of the authoring trap.** Moving the
accent from *per cell* to *the frame's lower left* put it in the frame's own corner, and
nothing said how far in. Measured on the three frames: set 6 cell 3's label sits **3.0% from
the left and 3.5% from the bottom**, cell 5's **2.3% and 2.6%** with its rule **touching the
right edge at 0.1%**, against **G10's 8% floor and its outright ban on text reaching an
edge**. The count was fixed and the margin was lost. A frame-level accent must state BOTH —
one in the frame, and how far in.

**The margin clause was written for that and it has now failed 0 of 5.** Set 7's revision put
*"Nothing comes within a tenth of the frame of any edge"* in every prompt. Every element that
lives near an edge breached it. Ink counted inside the 8% band against a blank-ground control
of the same size:

| element | ink in the margin | control |
|---|---|---|
| cell 3 at 10:52, `PICKS` | 1025 px | 0 |
| cell 3 at 10:56, `PICKS` | 1524 px | 52 |
| cell 4, the icon pair | 334 px | 0 |

and both `band` frames put the band into the margin — cell 5's **runs off both side edges**
under a constraint that said it must stop short of them, cell 6's stops about two per cent in.

**A margin stated as a global negative does not bind, and this is the same shape as the count.**
*Nothing comes within a tenth of any edge* is a property of the whole frame, the way *exactly
five units* was; both were carried in the binding block and both were ignored. What worked for
the count was naming the geometry positively — *the hero's cell fills the left half*. **The
accent needs the same treatment: say where it sits, not where it may not.**

**`hero`** — **the page's own product is CENTRE or LARGEST, and every earlier version of this
file forbade it.** Owner, 2026-09-09: *"sản phẩm của tôi (nếu tham chiếu app luôn nằm ở giữa
hoặc lớn nhất)"*.

This is a fact about the pipeline that the type never encoded. **The owner's app builds a
page for ONE product — theirs.** A top-N listicle places that product among four competitors,
so the lede is not a neutral index: it is a hero plus a field. Nine renders across two sets
were built to a law that says the opposite.

**The law is not deleted, it is scoped.** No unit may be favoured **except the page's own**,
and that one always is — centre, or largest, or both. The other four are equal to each other.
A frame in which all five are equal is a frame that has forgotten which page it is for.

**SIZE is required; centre alone is not enough, and set 3 settled it against a control.**
Cell 1 gave the hero the centre AND the largest cell and it reads at a glance. Cell 3 gave it
the centre at EQUAL size and the hero is invisible — five fryers of one size, and no reader
could name the page's product. **So the clause asks for size, and centre is the optional
half.** That costs the other four some room, which is the price of the frame knowing what it
is for.

**Which of the five is it? The FIRST attachment.** `products[]` does not exist and neither
does a hero index, so attachment order carries it, which needs no schema change and is
implementable today. When `products[]` is built it should carry the flag explicitly; until
then a prompt says *the first attached photo is the page's own product* and places it.

**This is namespace-wide, not this type's alone.** `lede-lineup` carries the same
no-favoured-unit law, inherited from `04-proof-lockedframe`, and its pass will have to face
the same correction. Recorded here so that pass finds it.

**`palette`** — **a collage uses SEVERAL hues across its cells, never one hue and its tints.**
Owner, 2026-09-09: *"màu sắc, bố cục chưa sáng tạo"*. Set 1 attributes it exactly, because
the failing cells were asking for monochrome in my own words:

| cell | what the prompt asked for | what came back |
|---|---|---|
| 3 sunglasses | *"one flat tone shared by all five panels"* | one yellow field, five identical panels |
| 4 fans | *"its own lighter or deeper shade of that same hue"* | five cells of near-identical cyan |
| 1 adapters | five different colours | alive, and the owner did not name it |
| 6 kettles | blocks, no single hue named | alive, and the owner did not name it |

The corpus agrees with the two that worked: `GIFTS-TABLETOP` runs four different cell
colours, `LABOR-DAY` three. **The cells are where this type's colour lives**, so a prompt
names several and lets them differ in HUE, not only in shade.

*A measurement was attempted and is not used: counting distinct hue buckets over the whole
frame cannot separate the ground from the products — cell 3 scores the same as a corpus frame
because its tortoiseshell, blue and orange lenses supply the hues its ground does not. The
finding rests on the prompt text and on looking.*

### SEVERAL was right and it was only half the clause — measured 2026-09-10

Owner, 2026-09-10: *"màu sắc chưa tối ưu"*. Measured with `ground_audit.analyse`'s hue spread,
the same instrument on both sides:

| | hue spread across the frame's own colours |
|---|---|
| corpus, the 12 frames this type holds | 0° 1° 1° 2° 13° 27° 47° 70° 85° 98° 174° 177° — **median 47°, seven of twelve under 60°** |
| set 8's five renders | 65° 128° 160° 171° 172° — **median 160°** |

**More than half the market's collages sit inside a narrow hue FAMILY, and none of mine do.**
The clause said *several hues, each light AND strongly coloured*, which optimises every cell on
its own for chroma and says nothing about how the cells relate. Five independently maximal hues
is a paint box, not a palette — the authoring trap a third time, a property stated per element
with no rule about the whole.

**The corpus tail is the gradient, and it is a different form doing a different job.** The two
frames at 174° and 177° are `open` grounds travelling corner to corner, which `PARTS/ground`
already records as the gradient's own measurement. **So the split is by LAYOUT:**

- **celled layouts — one hue FAMILY.** Cells sit inside roughly 60° of each other, differing in
  hue but recognisably related, which is what seven of the twelve corpus frames do.
- **`open` gradient — travel FAR.** Set 8's fire pits managed 65° where the corpus reads
  174–177°, so this type's gradients have been under-travelling as consistently as its cells
  have been over-spreading. One clause was wrong in both directions at once.

**The instrument's limit, stated:** the ring samples whatever reaches the frame edge, which on a
celled layout is the cells — that is the palette, so the reading is sound here even though
`registry/toplist-instruction.md` §Ground records the same ring as unusable for a GROUND on
these layouts. Same numbers, different question.

**`arrangement`** — **uniform is not the same as fair, and 0.7 conflated them.** The
no-favoured-unit law is about PROMINENCE: no unit larger relative to its own cell, brighter,
centred, or marked. **It says nothing about the cells being identical**, and set 1 cell 3
read as a spec sheet because the prompt added *"all five panels are the same width and the
same height"* on top of it. Not one corpus frame is a uniform grid: `GIFTS-TABLETOP` is an
asymmetric four-cell tile, `LABOR-DAY` has three cells of unequal size, `RECORD-PLAYER`
overlaps irregular blocks. **Cells may differ in size, shape and position; what may not
differ is how important a unit is made to look.**

### The authoring trap, and this file sprang the third instance of it

Set 1's *"all five panels are the same width and the same height"* was added on top of the
no-favoured-unit law and took the whole layout axis with it — an index that reads as a spec
sheet. The repair was `PARTS/arrangement` above: prominence against uniformity, a finer
distinction rather than the opposite.

**The law that instance taught is namespace law, not this type's**, and it moved to
`registry/toplist-instruction.md` § *Writing a clause: state the FAULT, not the property*
on 2026-09-10, with the other two instances — both `lede-authority`'s — beside it. It is
not restated here.

**`title`** — two forms are observed and they are not the same idea:

- **over the empty band** — the line sits in ground the units do not occupy. The safe form,
  and the one the first prompt used.
- **behind the units** — oversized type running under the cut-outs, which overlap and crop
  it. Observed once, on the laptops frame where the word LAPTOPS is set larger than the
  products and partly hidden by them. It is the more editorial of the two and it puts the
  headline in direct competition with the subject; untested here, and named so a prompt can
  ask for it deliberately rather than produce it by accident.

**A title arrives UNASKED where the badge already carries the category word — 2 of 6 in
set 6.** Neither cell 2 nor cell 3 named a `[TITLE]`; both printed one anyway. Cell 2 set
SOUNDBARS across the top of the frame while its shield badge already read *BEST OVERALL ·
SOUNDBARS · 2026*; cell 3 set LAPTOP STANDS inside the hero block under a laurel reading
*EDITOR'S PICK · LAPTOP STANDS · 2026*. The same word, twice, in one frame.

**This is a fault of the type's own permission, not of the model.** `text_layer: [title,
badge]` says a title is legal here, so nothing in the prompt refuses one, and a badge whose
middle line is the category name reads as a headline that has not been placed yet. **A prompt
that wants no title has to say so**, the way it already has to say per-frame or per-cell.
And the unasked one is not free: cell 2's landed **3.4% from the top edge** against G10's 8%.

**The type owns the badge's FORM; G16 owns its WORDS.**

| form | shape | observations IN THIS TYPE |
|---|---|---|
| `plaque` | a rectangle with a rule across it, a short line above and a year below | **0** — both frames that carried one were re-filed to `lede-winner` at 2026-09-09-D |
| `sticker` | a die-cut circle sitting on the ground, often tilted | **0** |
| `band` | a horizontal band across the frame | **0** |
| `corner-label` | a small word or brand line in a lower corner, not a verdict | **3** |

**The whole table is at zero except a corner label, and that is the curation's doing.** The
badge is permitted by ADR-071 and is now unevidenced in this type; the forms above are kept
as a shared vocabulary with `lede-winner`, which holds the observations.

**The owner has asked for one anyway, and that settles it.** 2026-09-09, on set 1's kettle
frame: *"chi tiết 'the best five kettles' mới chỉ dừng lại ở chữ trên 1 nền đơn điệu. hãy
thêm badge với style riêng, đặc sắc."* So a badge is wanted here on instruction rather than
on evidence, and the file says which it is.

### PLACEMENT — the badge goes INSIDE the hero cell

Owner, 2026-09-09: *"nếu có frame lớn nhất thì badge đặt ngay trong frame đấy"*.

**Where the layout has cells, the badge sits inside the hero's cell.** It marks the page's
own product, so it belongs on that product's ground rather than floating on whatever space is
left. Where the layout has no cells — `open`, `polaroid` — it sits on the ground, clear of
every unit.

**Set 5 shows what the old wording cost.** Three celled frames placed the badge by compass
direction: cell 5 happened to land it on the hero panel and reads correctly; cells 1 and 6
put it on bare ground and **each opened a dead white gap** in a composition that otherwise
tiles edge to edge. The badge was not floating by choice — the prompt gave it nowhere to be.

**One consequence, and it is a simplification.** The colour rule was *"a colour NO CELL
carries"*, which gets harder with every cell. Inside the hero cell it only has to clear
**one** — the hero's own cell colour and the product on it.

**Set 6 tested the rule and it delivered 4 of 5, with the dead gap gone at 5 of 5.** Every
celled frame put the badge in the hero's cell and not one opened the white hole that set 5's
compass placement did. Cell 5's `open` exception also holds: the starburst sits on the
gradient with ovens around it and question 7 is answered yes — **no cells means the ground,
and the ground is enough of a rule.**

**The one failure is about SIZE, and the prompt had no answer for it.** Cell 4 put a `seal`
in a narrow upright panel; the badge came back wider than the panel and **crossed out of it**
— its right half sits on the ground and over the neighbouring panel. The clause said *"sits
wholly inside the hero's panel and does not cross into another cell"*, which is a
prohibition with no escape route, and the model resolved it outward. That is the exact
failure mode **G10's last clause was written for: when content does not fit the safe area,
make it SMALLER.** The badge clause now carries that sentence itself, because *inside* is a
placement instruction and the thing that failed was a fit.

**And that escape route failed on its first test.** Set 7's revision re-ran the same form on
the same layout with *"if it does not fit, make it SMALLER, never move it out"* attached, and
cell 4's `seal` **crossed out of the hero's panel again**, at the same size. Borrowing G10's
own sentence did not travel: what G10 governs is content against the FRAME, and a panel edge
is not a frame edge, so the model has no reason to read the two as the same kind of boundary.
**The badge is 4 of 6 inside its cell across two sets, and both failures are `outlined-panels`
with a narrow hero.** The next thing to try is geometry again — give the badge a share of the
hero's panel rather than a permission to shrink.

### Forms, after two sets

- **`band` works, 2 of 2, and it works on a celled layout.** It was the owner's own named form
  at zero observations; set 7's long draft landed it on `open` and the revision landed it on
  `outlined-panels` twice. Legible, three type levels, a rule above and below. The only fault
  is margin, which every element in this set shares.
- **`plaque` is not rendering as a plaque.** Asked twice for *an upright rectangle, taller than
  wide*, and both draws of cell 3 returned **a crest with a notched base** — upright, correct
  in its type levels, and not a rectangle. The founding round's `plaque` came back landscape.
  Three attempts, three different shapes: the name is not carrying a form.
- `sticker`, `shield` and `seal` all rendered as specified.

### FINISH — what "hoàn thiện ở mức độ cao hơn" means, measured against the corpus

Owner, 2026-09-09, on set 2's five badges: *"cần hoàn thiện badge ở mức độ cao hơn"*. **All
five met 0.8's spec** — an internal tone step and two type sizes — and still read as flat
graphic shapes. So the spec was necessary and is not sufficient, and the gap is legible when
a set-2 badge is put beside the corpus mark.

The `GOOD HOUSEKEEPING BEDDING AWARDS` roundel carries, counted: text **arced** around the
rim, a two-line wordmark at a third size, a year at a fourth, **a star device**, an inner
ring inset from the edge, and a shadow separating the disc from the fabric behind it. Set
2's plaque carries a square, a keyline, and two sizes of type.

**So the standard rises to five things, and a badge that has fewer is unfinished:**

1. **Three type levels**, not two — a small label, a large word, and a year or qualifier.
2. **A device** — a star, a laurel, a rule, a row of dots. Something that is not a letter.
3. **A silhouette that is not a plain rectangle** — scalloped, notched, die-cut, arced,
   flanked. Set 2's `seal` did this and is the best of the five.
4. **Text following the form** where the form is round: arced along the rim rather than set
   flat inside it.
5. **A shadow**, so the badge sits ON the frame rather than in it.

**The title block is an OBJECT, not a coloured rectangle.** Set 1's container instruction did
its job on G10 — the type stayed inside its block — and produced a plain filled rectangle
with white words on it, which is the owner's *"nền đơn điệu"*. It owes what `lede-winner`'s
badge owes and for the same reason: **at least one internal tone step — a rule, an inset
border, a second panel, a corner cut — and at least two type sizes.** A flat block with one
size of type is the failure ADR-068 measured on the direct-response badges.

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

### The `[PRODUCT REFERENCES]` block is fixed text — owner instruction, 2026-09-10

*"cần giữ nguyên câu `[PRODUCT REFERENCES]` ... trong prompt"*. Every prompt opens with this
block, word for word, and it is not compressed, reworded or shortened:

```
[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers. THE FIRST
            ATTACHMENT IS THE PAGE'S OWN PRODUCT.
```

**The 2026-09-10 length pass had replaced it with a one-line `REFERENCES:` summary**, on Rule
6.3's ground that it restated what other clauses assert. That was a removal of owner-fixed text
by a pass whose remit was unearned clauses, and it is reversed. Sets 7 and 8 rendered with the
short form; whether the long form changes reference fidelity is now measurable, since nothing
else about the opening moves.

## FOUNDING RENDER ROUND

**One render, 2026-09-09 — round 2 prompt 6, rendered at v0.5.** Four hydraulic arm
trainers, FOUR attached references, the GRADIENT ground form, title and `plaque`. Verdict
**`partial`**, self-assigned under ADR-011 on a render that was opened and looked at.
Ledger: `eval/render-tests.jsonl`, ts `2026-09-09`.

**ADR-076's multi-reference route works, and this is its first evidence.** Four attachments
produced four distinct cut-out units in one generation call with nothing assembled
afterwards. That was the largest open question about this type — whether it is makeable at
all — and at n=4 the answer is yes.

**Question 8 is answered against this file.** `MARKS` permits the badge over one unit and
calls it *"the page saying which won"*, flagged as 1-of-1 reasoning against 2-of-2
observations and *"the thing to check first in a render round"*. Checked: the plaque sits
over unit 2 and **occludes** it, and unit 2 is the least legible of the four. It reads as a
floating label, not as a verdict — nothing about it says that unit won. So the render
supports **neither** reading: not FAVOURING, which was the fear, and not NAMING, which was
the claim. The paragraph stands unpatched at 1 of 1 and now has one render disagreeing with
its reasoning rather than none.

**Four failures, none of them patched, and two of them are the prompt's rather than the
model's:**

| slot | observed |
|---|---|
| `[SHADOW]` | **no contact shadow under any unit**; each cut-out carries a white sticker keyline instead. The clause asked for one faint shadow per unit, identical for all four |
| `[TITLE]` | both lines **breach G10's 8% safe area** — measured 7.1% and 5.0% of frame width on line 1, 4.8% and 4.2% on line 2 |
| `[MARK]` | a **landscape** plaque against *"an upright rectangle"*, and *"a thin white rule across it"* returned as an inset border |
| `[CUT-OUTS]` | the wordmark `Gyroscope` printed on **two of the four** units, against *"the units are four different makers"* |

**The `[TITLE]` breach was written into the prompt.** It asked the two lines to fill the
band *"margin to margin"* and in its closing line asked that nothing come within a tenth of
the width of any edge. Those cannot both hold; the model obeyed the first. Unlike
`lede-winner`, this type has **no** display-type carve-out — its `PARTS/title` puts the
line *over the empty band* or *behind the units*, never across an edge — so this is a plain
G10 breach with no rule behind it, and the fix belongs in the next prompt rather than in
this file.

**The gradient is thinner than the corpus form.** Measured 120° of hue spread against the
three corpus gradients at 175°, 175° and 177°, and it passes through a desaturated olive at
its midpoint where lime meets magenta. Recorded at 1 of 1; whether a two-hue gradient needs
its midpoint named is a question for a second render, not a clause today.

**One measurement in this frame is not usable and says so.** Ring texture reads 4.3, which
would put a smooth designed gradient near the photographed half. It is not the ground: the
title runs into both side ring bands, so the ring measured the type. **On a type that
declares a `text_layer`, the ring metric measures the words**, and that is a limit ADR-073
did not have to state because no frame it measured carried baked text at the edge.

## CURATION — 2026-09-09-D, and it is why every number above moved

**The type's clauses had been measured on a set that was mostly not the type.** 0.5 recorded
the problem plainly — one corpus observation of what the file defines, and five records of two
other shapes — and left it. The owner's named examples of 2026-09-09 settled the direction, so
the pass was taken.

**Nine corrections, appended as new records because the ledger is append-only:**

| move | frames | on whose authority |
|---|---|---|
| `proposed lede-mosaic` → `lede-collage` | GIFTS-TABLETOP, RECORD-PLAYER-GEAR, LESET | **owner-named** |
| `proposed lede-mosaic` → `lede-collage` | LABOR-DAY-DEALS | by extension — same construction as the three named |
| `lede-collage` variant → match | CULOTTES | **owner-named** |
| `lede-collage` variant → match | LINEN-MENSWEAR | by extension — same construction as CULOTTES |
| `lede-collage` → `lede-winner` | FI-COTOPAXI, FI-HU-HA | **owner-named**, and ADR-074's words-not-count boundary agrees |
| `proposed lede-mosaic` → `lede-winner` | bedding-awards-index | **owner-named** |

**`lede-mosaic` is absorbed and the proposal closes at zero records.** It was proposed as an
eighth type on five observations; four of those five the owner named as belonging to existing
types, and the fifth follows them. **A proposed type that its own evidence dissolves is the
absorption ladder working**, not a loss.

`lede-collage` goes from 1 match + 5 variants to **7 matches + 1 variant**. The one remaining
variant is a single product in several views — neither several products nor one subject in
several states — and it stays out.

**The two moves made by extension are flagged `moved-by-extension` in the ledger** so a later
pass can find them and disagree.

**A side effect this file must not act on.** Three frames moved INTO `lede-winner`, and its
ground table moved with them: it now reads texture 5.6 and files `photographed` at n=8, where
0.5 recorded a smooth designed ground at 1.5. That is a real change to another type's
evidence and belongs to `lede-winner`'s own pass.

## SET 3 — the hero settled against a control, and the control refused to be one

Five of six rendered; cell 4 did not come back, so the `shield` badge form is still untested.

| cell | hero asked for | hero visible? | badge | verdict |
|---|---|---|---|---|
| 1 grinders | centre AND largest | **yes, at a glance** | `roundel` | **pass** — the best badge of the run |
| 2 mops | largest, OFF centre | **yes** | `laurel` | **pass**; invented the brand `RoboClean` |
| 3 fryers | centre, EQUAL size | **no** | `starburst` | `partial`; four of five brand marks garbled |
| 5 kettles | centre AND largest | **yes** | `seal` | **pass**; invented the brand `TRAVEL KETTLE` |
| 6 dryers | **CONTROL — none** | **a hero appeared anyway** | `roundel` | the control failed to be a control |

**SIZE is the operative variable.** Centre plus largest reads (cells 1, 5); largest alone
off-centre reads (cell 2); centre alone at equal size does not (cell 3). `PARTS/hero` is
corrected to require size and treat centre as the optional half.

**The composition WANTS a hero, and that is the stronger finding.** Cell 6 was instructed
*"ALL FIVE units are equal… no unit is the hero"* and produced a clearly largest unit in a
clearly largest cell. Set 2's control did the same thing unasked. **Two of two no-hero
controls produced a hero**, which means sets 1 and 2 were not merely wrong about the
pipeline — they were fighting the layout.

**The five-point FINISH standard delivered 5 of 5.** Every badge came back with three type
levels, a device, a shaped silhouette, text arced where the form is round, and a shadow. The
standard is confirmed on its first outing. One flaw: cell 1's roundel took a purple a
neighbouring cell also carried, against its own constraint.

**Invented lettering is now a namespace problem rather than an incident.** Set 3 alone
produced `RoboClean`, `TRAVEL KETTLE` and four garbled fryer brands, on cells whose prompts
all carried *"invent no lettering"*. **Nine instances across the namespace**, every one under
a prohibition. G10's own text names the reason a ban fails: *"a prohibition without a
sanctioned escape route is resolved by the model in whichever direction it likes"*. The ban
needs somewhere to send the model instead, and set 4 tests one.

## SET 4 — both new layouts work, `shield` is the best badge yet, and the lettering fix failed

Six of six rendered.

| cell | layout | verdict | note |
|---|---|---|---|
| 1 suitcase | `split-frame` + `shield` | **pass** | the best badge of the whole run: gold, bevelled, four type levels, rules as the device, a shadow |
| 2 running belt | `polaroid` | `partial` | three prints, one belt, shadows correct — and an invented brand `RUNNER` on all three |
| 3 stand mixers | `colour-cells`, hero largest | `partial` | hero unmistakable at half the frame; invented brand `KITCHENMASTER` on it |
| 4 sleeping bags | `blocks`, hero off-centre | **pass** | blocks came back FLAT this time, correcting set 3 cell 2's 3D slabs |
| 5 smartwatch | `split-frame`, no mark | **pass** | same watch across a cut-out and a real photograph, no words at all |
| 6 toasters | `open`, **CONTROL** | **pass** | gold seal, hero centre and largest, no invented lettering |

**Both new layouts hold.** `split-frame` kept ONE product identical across a cut-out half and
a photographed half, twice — which is the same single-pass identity problem that defeated the
boot panels, solved here because there are two views rather than five. `polaroid` held one
belt across three prints.

**Cell 5 answers its own question: `split-frame` reads as this type with no mark at all**, and
that is the form the corpus supports — both corpus split-frames carry none. Cell 1 is the
decorated variant and it is the better picture, which is a preference rather than a finding.

### The lettering fix did not work, and the failure is more useful than the fix would have been

Five cells replaced the bare ban with a destination — *"leave that surface plain and
unbranded; an unbranded surface is correct, an invented one is not"*. One control kept the
ban.

| clause | cells | invented lettering |
|---|---|---|
| destination | 5 | **2** — `RUNNER`, `KITCHENMASTER` |
| bare ban (control) | 1 | 0 |

**The destination did not reduce it, and one control cell cannot show the ban is better.**
What the two failures share is not the clause: **both products carry a large blank flat panel
where a brand would normally sit** — the belt's pouch face and the mixer's body side. The
four cells with no such surface produced nothing. **Hypothesis at 2 of 2, not a rule:** the
model fills a conspicuous empty brand surface, and no wording about lettering addresses that,
because the instruction it is really answering is compositional. Eleven instances across the
namespace now.

## CURATION — 2026-09-09-E, and it reverses two of my own records from four hours earlier

The owner named **eight** frames as `lede-collage`. Three sat elsewhere, and **two of those
three had been put there by the owner's OWN earlier naming the same day.**

| frame | was | now | conflict |
|---|---|---|---|
| WIRECUTTER-PRODUCTIVITY-PICKS | `lede-lineup` | `lede-collage` | none — filed by a session, never owner-named for lineup |
| luggage-tout | not in the ledger | `lede-collage` | none — first record |
| harperwilde bra | `lede-collage` variant | `lede-collage` match | none — a promotion |
| **FI-COTOPAXI** | `lede-winner` | `lede-collage` | **owner against owner** |
| **FI-HU-HA** | `lede-winner` | `lede-collage` | **owner against owner** |

**The later, more specific instruction is taken, and ADR-074's own rule agrees with it.**
That boundary is *a winner frame carries display type, a MARK, or both*. Both split frames
carry neither — a field of repeated tick-and-cross glyphs is a ground treatment, not a
verdict. **The 2026-09-09-D note claiming ADR-074 supported the earlier move was my error**,
and it is corrected here rather than left standing. Both records carry
`reverses-2026-09-09-D` so the flip is findable, and one appended record reverts it.

`lede-collage` reaches **12 matches**. `lede-lineup` drops to 5 and `lede-winner` to 5.

## SET 6 — the per-frame accent is settled, the count is not, and the control confounded itself

Six of six rendered, all opened and graded under ADR-011. Set 5 has no section of its own:
its findings are in `PARTS/graphics`, `MARKS/PLACEMENT` and the 0.14 CHANGELOG entry.

| cell | layout | verdict | what decided it |
|---|---|---|---|
| 1 rice cookers | `colour-cells` | **fail** | **SIX units**, one Panasonic rendered twice; the only frame with invented and garbled lettering |
| 2 soundbars | `rounded-cells` | `partial` | five, badge in the hero cell, two layers — and an unasked SOUNDBARS title at 3.4% from the top |
| 3 laptop stands | `blocks` | `partial` | ONE corner label, badge in the hero block — and an empty sixth block, an unasked title, label at 3.0%/3.5% |
| 4 water flossers | `outlined-panels` | `partial` | ONE icon pair, arcs behind the hero — and the badge crossed OUT of the hero's panel |
| 5 pizza ovens | `open` gradient | `partial` | ONE corner label, badge on ground with no dead gap — and a toaster oven; the rule touches the right edge |
| 6 baby strollers | `outlined-panels` | **pass** | **CONTROL.** Five, photographic, three layers all present, badge in the hero panel |

**Two clean wins.** The per-FRAME accent wording returned exactly one element in 3 of 3, against
five in set 5. And the badge inside the hero's cell delivered 4 of 5 with **no dead white gap in
any frame** — the fault 0.14 was written to fix does not recur.

**The count fault is the one the owner named**, and `PARTS/count` is new because of it.

### The lettering fault in set 6 is NOT set 4's fault

Set 4 recorded a hypothesis at 2 of 2: *the model fills a conspicuous empty brand surface*.
Set 6 does not support it and does not refute it — it adds a second, different failure.

| | set 4 | set 6 cell 1 |
|---|---|---|
| the surface | a large blank flat panel where a brand would sit | a dense control panel already covered in small type |
| what happened | a brand INVENTED — `RUNNER`, `KITCHENMASTER` | existing type **GARBLED** — the hero's wordmark rendered mirrored and unreadable |
| the other unit | — | a red cooker carrying `SHCECO`, a mark that is not a brand |

**Cell 1 is the only frame in set 6 whose products carry dense small lettering, and the only
one with a lettering fault at all.** The four frames with large blank faces — soundbars,
laptop stands, flossers — produced nothing, which is the opposite of what set 4's hypothesis
predicts. **So there are two faults, not one**: inventing a mark on an empty surface, and
mangling type it is trying to copy. A ban addresses the first; only *do not redraw small text
at all* addresses the second, and set 7 says that.

### An instrument bound, and it is this type's `layout` axis breaking the ring metric

`scripts/ground_audit.py` reads the ground from the outer 8% ring. Run on all six:

| cell | layout | ring value | ring sat | what the ring actually sampled |
|---|---|---|---|---|
| 5 pizza ovens | `open` | 0.91 | 0.73 | **the ground.** Usable |
| 1 rice cookers | `colour-cells` | 0.99 | 0.44 | whichever cells reach the edge |
| 4 water flossers | `outlined-panels` | 0.99 | 0.99 | three magenta panels that reach the edge |
| 6 strollers | `outlined-panels` | 0.84 | 0.91 | the glyph-field ground — patterned, so texture 8.1 |
| 2 soundbars | `rounded-cells` | 0.97 | **0.04** | the halftone screen and the title, not a ground |
| 3 laptop stands | `blocks` | 1.00 | **0.00** | **the white page behind the blocks** |

**Cell 3 is the control that fails.** Its composition argues in blue, green, orange and yellow
blocks, and the ring returns saturation 0.00 — pure white. Publishing that as this type's
ground saturation would be a false statement about the picture. **Only `open` gives a ring
that is the ground**, so no per-frame ground figure is published for set 6 and none of these
numbers enters `PARTS/ground`.

ADR-073 measured a namespace whose ground was one field. This type has eight layouts and on
most of them the ring is not measuring a ground at all. That is an instrument fact rather than
this type's own, so it is **stated in `registry/toplist-instruction.md` §Ground** as the third
bound beside the exposure floor and the baked-text limit, and is not restated here. What
belongs here is the consequence: `PARTS/ground`'s figures come from the corpus, and no set-6
render adds to them.

## SET 7, LONG DRAFT — four of six rendered, the count clause failed, and the ceiling loses its place to SIZE

Rendered 2026-09-10 from the draft written before the length pass (3146–3436 characters).
**Cells 4 and 6 did not come back**, and cell 6 was the declared control — the second control
this type has lost to a missing render. All four opened and graded under ADR-011.

| cell | verdict | what decided it |
|---|---|---|
| 1 projectors `colour-cells` | **fail** | **SIX units**, one silver cube twice, with the explicit count clause in the prompt |
| 2 shredders `rounded-cells` | `partial` | five, badge in the hero cell — the four small units read simplified, and the shield occludes the hero |
| 3 steamers `blocks` | **fail** | five units but **four are one mould recoloured**; the worst register in the set |
| 5 waffle makers `open` | **pass** | five, all large, photographic, real brand marks, `band` legible on its first outing |

**`band` works and it is the owner's own named form at 0 observations.** Magenta, across the
upper third, three type levels with a rule above and below — the first evidence for the form
anywhere in the namespace, and it reads as a verdict rather than as decoration.

**The positive defining-feature clause held where it was tested.** All five waffle makers show
a hinged clamshell with a gridded plate; all five shredders show a slotted feed on a bin. That
is the replacement for set 6's failed exclusion list, and it is 2 of 2 so far.

**Owner, 2026-09-10:** *"tôi đánh giá batch này kém hơn rất nhiều so với các set trước"*. The
two named faults are the ones above, and neither is caused by the draft being long — cell 5 is
the longest kind of frame in the set and is the only clean pass. Length was a separate fault,
fixed separately, and this set is the evidence that fixing it bought nothing on its own.

## SET 7, REVISED — geometry fixes the count, and one prompt rendered twice ends the register hypotheses

Seven files for six cells: **cell 3 was rendered twice**, at 10:52 and 10:56, from an unchanged
prompt. All seven opened and graded under ADR-011.

| cell | count | register | distinct | verdict |
|---|---|---|---|---|
| 1 ice makers `colour-cells`, geometry | **5** | photographic | yes | **pass** |
| 2 label printers `rounded-cells`, geometry | **5** | photographic | yes | **pass** — best frame of the set |
| 3 hedge trimmers `blocks` · 10:52 | 5 | **flat vector** | yes | `partial` |
| 3 hedge trimmers `blocks` · 10:56 | 5 | photographic | yes | `partial` — margin only |
| 4 tyre inflators `outlined-panels` | 5 | flat vector | yes | `partial` — badge crossed out again |
| 5 turntables, drawn LARGE | **6** | flat vector | yes | **fail** — a 2×3 grid where five panels were asked |
| 6 wine coolers, drawn SMALL · CONTROL | 5 | flat vector | **no — one mould** | control, see below |

**What this set settles.**

- **GEOMETRY fixes the count, 2 of 2**, on the layout that had failed twice. The one count
  failure is the cell that was given a property instead of a geometry.
- **The register is a DRAW.** Cell 3 twice, same prompt, opposite registers. Both the layer
  ceiling and the size hypothesis are withdrawn above.
- **`distinctness` holds 5 of 6**, including twice on hedge trimmers, the hardest category
  available. The one failure is wine coolers, which are a glass door over racks whatever the
  maker — a category limit rather than a clause failure.
- **The margin clause holds 0 of 5.** See `PARTS/graphics`.
- **No frame printed a title nobody asked for**, 0 of 7. That refusal works.
- **The defining-feature clause held everywhere it was checkable** — label strips emerging from
  every printer, a lidded chamber on every ice maker, a toothed bar on every trimmer. 4 of 4
  categories, and 4 of 4 across the two drafts.

**The control could not be a control, for the third time in this type.** Cell 6 flattened as
predicted, but cell 5 — its LARGE half — flattened too, and cell 3 flattened and then did not
from one prompt. The set file wrote the branch in advance: *"if both flatten, the variable is
neither"*. It is neither. Set 3's control produced a hero it was told not to produce, set 5 and
6's control confounded itself, and this one was answered by a variable nobody was testing.

## SET 8 — geometry settles the count and fixes `plaque`, and a named position does NOT fix a margin

Five of six rendered; **cell 2, the badge-in-a-narrow-panel retest, did not come back**, and
neither did the second draw of cell 1 that the new evidence rule asked for. All five opened and
graded under ADR-011.

| cell | count | register | distinct | badge | margin |
|---|---|---|---|---|---|
| 1 bread makers `colour-cells` | **5** | photographic | yes | inside its cell — rim reads `AAFERABLE BREAD QUALITY` | no accent |
| 3 cool boxes `rounded-cells` | **5** | flat vector | yes | inside its cell — top line reads `LABEL` | no accent |
| 4 drones `blocks` | **5** | photographic | yes | **a rectangle with four square corners** | `PICKS` in the margin |
| 5 fire pits `open` | **5** | photographic | yes | `band` **bleeds off both side edges** | `PICKS` in the margin |
| 6 compressors CONTROL | **5** | photographic | yes | **crossed out of its panel** | icons in the margin |

**GEOMETRY is settled at 5 of 5 for the count**, and 7 of 7 across sets 7 and 8 wherever a cell
was given a share of the frame. Nothing else in this file has that record.

**GEOMETRY also fixed `plaque` on its first try.** Three earlier attempts asked for it by name
and returned a landscape bar, then a crest, then a crest. Cell 4 asked for *a plain
four-cornered rectangle, half again as tall as it is wide* and got exactly that. **A form name
is not a form; a geometry is.**

### The control worked, and what it proved is that MY FIX did not

This is the first control in this type that behaved. Cell 6 kept set 7's blanket *"nothing comes
within a tenth of any edge"* and its badge kept G10's *"make it SMALLER"*, and it did what was
predicted in advance: the badge crossed its panel and the icon pair sat in the margin.

**But cells 4 and 5 carried the NEW positive placements and breached too.** *"The corner-label
sits one tenth of the frame's width in from the left edge and one tenth of its height up from
the bottom"* produced a label on the edge, twice. *"The band runs from one tenth in from the
left edge to one tenth in from the right edge, and no further"* produced a band bleeding off
both edges.

So the count's lesson does **not** generalise: naming a position fixed how many CELLS a frame
has, and did nothing for how close an element sits to the frame edge. **What separates them is
that a cell's share is a composition decision the model makes once, and a margin is a
measurement it never takes.** The margin is now 0 of 8 across two sets against three different
wordings, and this file should stop rewording it.

### The badge prints the instruction

Cell 3's `shield` carries the literal word **`LABEL`** where its small top line should be, and
cell 1's `sticker` carries **`AAFERABLE BREAD QUALITY`** arced on its rim where nothing was
asked for at all. Both prompts said *"a small label ... a large word ... a small year"* while
the `Words:` line named only three strings. **A slot described by its ROLE gets filled with the
role's name**, and a badge with more type levels than it has words will invent the difference.
The `Words:` line has to supply one string per level.

## SET 9 — all eight layouts at once, and the record finally sorts what a prompt can ask for

Eight of eight rendered, one category each, none used before. All opened and graded under
ADR-011.

| cell | layout | count | register | palette | badge |
|---|---|---|---|---|---|
| 1 patio heaters | `open` | 5 | photographic | **gradient 179.3°** | `band`, three strings |
| 2 smart locks | `colour-cells` | 5 | photographic | **22° — one blue family** | `sticker`, three strings |
| 3 massage guns | `blocks` | 5 | photographic | family BROKE — lime against blues | `plaque`, a rectangle |
| 4 camping stoves | `outlined-panels` | 5 | photographic | warm family | `seal` overlaps its panel edge |
| 5 bird feeders | `rounded-cells` | 5 | photographic | **32° — one warm family** | `shield`, measured in the margin |
| 6 ski goggles | `pinboard` | 5 | photographic, **texture 28.7** | — | `sticker`, three strings |
| 7 electric guitar | `split-frame` | 1 | both registers, one frame | — | none, as asked |
| 8 child car seat | `polaroid` | 1 | photographic | — | none, as asked |

**Three layouts rendered for the first time and all three work.** `pinboard` returned real cork
at texture 28.7 — the highest this type has recorded, against the corpus board at 16.0 — with
pins, curled corners and each print shadowing the board. `split-frame` held ONE guitar identical
across a cut-out half and a photographed half in a single call. `polaroid` held ONE car seat
across four genuinely different views: front, side, rear, folded.

**The palette fix landed.** Celled layouts whose ring actually samples their cells read 22° and
32° against a corpus median of 47°, where set 8 read 128–172°. The gradient reads **179.3°**
against the corpus's 174–177°, where set 8 managed 65°. *Cells 3 and 4 are not counted: their
rings read 0.03 and 0.06 saturation, so they sampled the pale ground rather than the blocks —
the §Ground bound, not a palette figure. By eye cell 4's panels are one warm family, and cell
3's lime block is the outlier that broke it.*

**The `Words:` fix landed: 8 of 8 badges printed exactly their named strings**, after set 8
produced `LABEL` and `AAFERABLE BREAD QUALITY`. **`corner-label` is gone, 0 of 8.** **Count is
8 of 8**, taking geometry to **15 of 15 across three sets**.

**Still failing: the margin.** Cell 5's shield measures 886 px of ink inside G10's 8% band
against a control of 0, and cell 1's band spans the frame edge to edge for the third set
running. Roughly 0 of 12 now.

### What a prompt can ask this model for, and what it cannot — the record, sorted

Owner, 2026-09-10: *"constraints là ít cần thiết mà dựa vào chủ yếu do model gen ảnh"*. The
record says something narrower and more useful, and it sorts cleanly:

| a clause that names… | outcome |
|---|---|
| a **share of the frame** — the hero's cell fills the left half | count **15 of 15** |
| a **shape** — a plain four-cornered rectangle, half again as tall as wide | `plaque` **2 of 2**, after 3 failures by name alone |
| a **thing to draw** — cork, pins, curled prints; the same guitar twice | **3 of 3** first-time layouts |
| a **string per type level** | **8 of 8**, after two badges printed their own instructions |
| a **hue relationship** | 3 of 4 by eye, and the gradient 1 of 1 |
| a **distance from an edge** | **0 of 12**, across four different wordings |
| a **prohibition** — do not cross, do not come within | 0 of 12; and the badge in a narrow panel 0 of 3 |
| the **register** | not a clause at all — one prompt gave both, four minutes apart |

**So constraints are not less necessary; a particular KIND of constraint is inert.** Everything
the model must DRAW lands. Everything it must MEASURE does not, because measuring is not part of
making the picture — and a prohibition asks for a measurement with no picture attached, which is
the same conclusion G10's own last clause reaches from the other side.

**The practical rule: describe the thing, never the gap.** Where an element must sit away from an
edge, give it something to sit ON or INSIDE that is itself placed — a band that ends inside a
named panel, a badge that occupies a share of a cell — rather than a clearance it has to
compute. That is the next thing to test, and it is the last fault this type has that is neither
a draw nor the owner's to decide.

## SET 10 — the plate solves the margin and costs a white frame, and equal panels land 2 of 2

Six of six rendered, all opened and graded under ADR-011.

| cell | layout | count | plate | margin | note |
|---|---|---|---|---|---|
| 1 cargo boxes | `colour-cells` | 5 | **60%** | clean | **rank numbers 2 3 4 5 printed** |
| 2 rowing machines | `outlined-panels` EQUAL | 5 | 80% | clean | `seal` inside its panel — a first |
| 3 cocktail shakers | `rounded-cells` | 5 | 85% | clean | the tightest plate of the five |
| 4 sleeping pads | `blocks` | 5 | **71%** | clean | palette came back PASTEL |
| 5 garden shredders | `open` | 5 | **68%** | clean | gradient midpoint stayed saturated |
| 6 ice cream makers | `outlined-panels` EQUAL | 5 | **no plate — CONTROL** | **breached** | four panels left uncoloured |

### The margin is solved, and it was solved by drawing it

**Nothing in cells 1–5 touches a frame edge — 5 of 5, the first clean margin in five sets**
against 0 of 12 for four different wordings of a clearance. The control, identical but for the
plate, put its badge across the panel and into the margin exactly as predicted.

**So the rule holds: describe the thing, never the gap.** A clearance the model must compute is
inert; a clearance drawn as an object with an edge is obeyed.

### And it cost what the owner named

Owner, 2026-09-10: *"hạn chế nền trắng bên ngoài quá nhiều"* — garden shredders, sleeping pads,
rowing machines, cargo boxes. Measured, plate area as a share of the frame and the border colour:

| | plate | border top / bottom | border colour |
|---|---|---|---|
| cargo boxes | **60%** | 15.6% / 17.6% | rgb(244,243,238) |
| garden shredders | **68%** | 12.3% / 13.6% | rgb(229,233,237) |
| sleeping pads | **71%** | 9.6% / 9.2% | rgb(240,240,237) |
| rowing machines | 80% | 6.9% / 7.1% | rgb(249,245,234) |
| cocktail shakers | 85% | 3.8% / 4.7% | rgb(241,241,240) |

**Two faults, and the second is the one that matters.** The plate was asked to fill the middle
four fifths and three cells came back at 60–71%, adding vertical margin nobody asked for. And
**the border rendered WHITE in 5 of 5** — because the clause said *"the ground shows as a plain
even border"* and never said what colour a plain border is.

**That is the `LABEL` fault again.** A slot named by its ROLE and given no value takes a
default, and the default for an unnamed ground is white. The badge learned it three sets ago
and the plate had to learn it separately: **name the value, not the role.** The border is now a
named hue from the palette's own family, and the plate fills nineteen twentieths rather than
four fifths.

### `outlined-panels` EQUAL — the owner's instruction lands 2 of 2

Cells 2 and 6 both returned five panels of one height, the hero's wider and the other four equal
to each other, none stepped. **The descending staircase of set 9 cell 4 is gone**, and cell 2 is
the first frame in which a `seal` stayed inside its hero panel.

### Two new faults

- **Rank numbers.** Cell 1 printed `2`, `3`, `4`, `5` in its cells against a NEGATIVE that names
  rank numbers first. First occurrence in ten sets; recorded, not yet a pattern.
- **`never pastel or dark` failed 2 of 6** — sleeping pads came back in washed lavender, mint and
  peach, and the control left four of five panels a pale pink. The pair *light AND strongly
  coloured* has held everywhere the cells carried colour at all; what these two share is a cell
  the model treated as empty space rather than as a coloured field.

## SET 11 — the white frame closes, and `split-frame` turns out to be two ANGLES

Eight of eight rendered, all opened and graded under ADR-011.

| | set 10 | set 11 |
|---|---|---|
| plate covers | 60–85% | **82–93%** |
| border saturation | 0.02 | **0.67 – 0.97** |
| border value | 0.95 — white, 5 of 5 | **0.36 – 0.54 — deep, 5 of 5** |

**Naming the VALUE closed it.** The border is navy, forest, maroon, indigo and indigo across
the five plate cells, where set 10 gave near-white in every one. Same lesson as the badge that
printed `LABEL`: **a slot named by its role takes a default; a slot given a value takes the
value.** Third confirmation of that pattern, and the first time it was applied before the fault
rather than after it.

**Three other fixes held.** Every cell came back a filled field of strong colour — the pastel
failure of set 10 does not recur, 5 of 5. **No rank numbers**, 8 of 8, after cell 1 of set 10
printed `2 3 4 5`. **Count 8 of 8**, taking geometry to **29 of 29**. Register: 8 of 8
photographic, which is a run of draws and not a finding.

### `split-frame` is two ANGLES, not one view twice — owner, 2026-09-10

*"tôi muốn cùng sản phẩm nhưng góc chụp khác nhau như tham chiếu (có thể là sử dụng, có thể là
showcase góc khác)"*, pointing at this type's own corpus frame `FI-COTOPAXI-CORAZA-SUITCASE`.

That frame is a closed suitcase cut out front-on beside **the same suitcase opened flat, seen
from above, on a floor, with packing cubes and a hand pressing one down**. Two angles, and the
photographed half is the product IN USE.

**Both of this type's `split-frame` renders gave the same view twice.** Set 9's guitar and set
11's wheelbarrow are each a cut-out beside the identical pose with a background behind it — the
second half adds a place and nothing else. `PARTS/layout`'s entry said *"a real photograph of
the same product"* and never said from where.

**`polaroid` already does it right, and the difference is one sentence.** Its prompts name the
four views — from above, low three-quarter, pieces beside the board, folded — and both renders
delivered four genuinely different ones. **So `split-frame` names its two views the same way**,
and the photographed half shows the product being used.

### Two faults of my own

**`pinboard` printed five product names** under its prints — `Garmin Descent Mk3i`, `Suunto EON
Co…`, and three more. Set 9 carried *"No words in the frame but those named above"* and **set 11
dropped it**; only the badge clause survived, which governs the badge and not the frame. That is
the second earned clause lost in a rewrite, after the length pass cut the hero-cell sentence at
0.16. A clause that has never failed is the easiest one to drop.

**Cell 4's layout did not execute.** It asked for five equal upright panels and returned a hero
cell beside a 2×2 — `colour-cells` geometry under an `outlined-panels` heading. Equal panels are
2 of 3; both successes were set 10, where the plate was smaller and the panels had the plate's
full height to reach.

**One weaker note:** cell 3's five bike racks are four Thule products and one other. The forms
differ, so `distinctness` passes as written — it asks for different silhouettes and bodies, not
different makers. Recorded because the frame's claim is a field of competitors.

## SET 12 — the narrowing holds, `split-frame` is fixed, and the gradient needs a contrast rule

Eight of eight rendered, all opened and graded under ADR-011. **The owner approved the type on
this set** and named one correction.

**What landed.** No frame drew an outline, glyph, arc, keyline or icon — the narrowing to
surface treatments holds 8 of 8. `pinboard` printed **no captions**, so the clause restored from
set 9 works. Count 8 of 8, geometry **37 of 37**. Plate and deep border held. Filled fields held.

**`split-frame` is fixed at 1 of 1.** Cell 7's left half is the tool chest closed, front-on, cut
out on a flat ground; its right half is **the same chest open, from a higher and more angled
viewpoint, drawers pulled out with tools in them, on a workshop floor, a gloved hand on a
drawer**. Two angles, the second in use — the corpus behaviour of `FI-COTOPAXI`. The fix was the
one `polaroid` already used: **name both views**.

### `PARTS/ground` — the gradient does not have to be OPPOSITE, and contrast is the real rule

Owner, 2026-09-10: *"màu nền có thể không phải opposite trên color wheel mà còn có thể
analogous. đảm bảo tương phản giữa nền, sản phẩm và plate."*

0.19 wrote *"two hues OPPOSITE each other on the colour wheel"* because set 8's gradient
travelled only 65° against a corpus of 174–177°. It fixed the travel and bought a worse fault:
**opposite hues meet in a muddy midpoint**, and set 12 cell 1 put a dark green hero chair
exactly on the orange-to-cyan transition, where it barely reads.

**The corpus never said opposite.** `PARTS/ground` records hue spreads of 1°, 2°, 27°, 47°, 98°,
174° and 177° — a continuum, and 0.7 already refuted the claim that this type is bimodal. **Half
a wheel is one option, not the rule.**

**So the rule is CONTRAST, and travel is free.** A gradient may be analogous or opposite; what it
must do is stay clear of the units standing on it and of the plate's border. Stated the way this
type's clauses land — as things, not as measurements:

- the hero's own colour is a colour **no part of the ground carries**;
- the border is **darker than every part of the gradient**;
- the midpoint of the gradient stays saturated, which 0.19 already required and set 12 obeyed.

That is the third time an over-tight fix for a measured fault has cost a different one — after
*"the expression is settled"* and *"all five panels the same width"*. **State the fault, not the
property**, and this file's own §*Writing a clause* in `toplist-instruction.md` names it.

### `outlined-panels` will not stay in one row when it also has to carry a hero

**2 of 4.** Set 12 cell 4 asked for *FOUR vertical divisions cutting the plate into FIVE upright
panels in ONE row*, a count rather than a description, and returned a hero cell beside a 2×2 —
the same substitution set 11 made. Both successes were set 10; both failures came with a large
plate.

**The tension is real and it is in the clauses, not the model.** The hero must be *clearly
largest* and the panels must be *one row of equal height*, which leaves width as the only lever;
a hero cell plus a grid gives the model area instead, and it takes it. **Either the hero rule
relaxes for this layout or the row does** — that is a decision about the picture and it is
flagged, not taken.

## CHANGELOG
- 0.22 (2026-09-10): **owner approval, and one correction.** Set 12: the narrowing to surface
  treatments holds 8 of 8 with no drawn accent anywhere, `pinboard` prints no captions, count 8
  of 8 and geometry 37 of 37. **`split-frame` is fixed at 1 of 1** by naming both views, which is
  what `polaroid` had been doing all along. **`PARTS/ground` corrected on owner instruction**: a
  gradient may be ANALOGOUS or opposite — 0.19's *"opposite on the colour wheel"* was an
  over-tight fix for set 8's 65° travel and it produced a muddy midpoint that swallowed cell 1's
  hero. The rule is CONTRAST: the hero carries a colour the ground does not, and the border is
  darker than every part of the gradient. Third instance of an over-tight fix costing a
  different fault. And `outlined-panels` is recorded at **2 of 4** on one-row equal panels, with
  the tension named: *clearly largest* and *one row of equal height* leave only width, and the
  model takes area instead. Flagged for the owner rather than decided.
- 0.21 (2026-09-10): **the white frame closes, and two owner corrections.** Border saturation
  goes 0.02 → **0.67–0.97** and the plate 60–85% → **82–93%**, 5 of 5, by naming the border's
  VALUE instead of its role — the third instance of that pattern and the first applied before
  the fault. Filled fields 5 of 5, no rank numbers 8 of 8, count 8 of 8, geometry 29 of 29.
  **`PARTS/layout`'s `split-frame` corrected on owner instruction**: it is the same product at
  two DIFFERENT angles with the photographed half usually in use, which the corpus frame
  `FI-COTOPAXI` shows and both of this type's renders missed — `polaroid` gets it right because
  its prompts NAME the views, so `split-frame` does the same. **`PARTS/graphics` narrows to
  surface treatments** — halftone, gradient, grain — on owner instruction, retiring every drawn
  accent; this reverses the owner's own 2026-09-09 ask that created the part, and two retired
  elements had 2 corpus observations each, which is the stated cost. And a clause of mine was
  lost in the rewrite: `pinboard` printed five captions because *"no words but those named"* did
  not survive from set 9.
- 0.20 (2026-09-10): **the plate solves the margin, and names the next fault itself.** Owner:
  *"ice cream maker không pass"*, *"hạn chế nền trắng bên ngoài quá nhiều"*. **Margin clean 5 of
  5** on the plate cells against 0 of 12 for four wordings of a clearance, and the no-plate
  control breached as predicted — *describe the thing, never the gap* is confirmed. It cost a
  white frame: the plate came back at 60-71% of the frame in three cells and **the border
  rendered WHITE in 5 of 5**, because the clause named the role and not the value. Same fault as
  the badge printing `LABEL`. The border is now a named hue from the palette family and the
  plate fills nineteen twentieths. **`outlined-panels` EQUAL lands 2 of 2** — the staircase is
  gone and a `seal` stayed inside its hero panel for the first time. Two new faults: rank
  numbers printed in cell 1 against the NEGATIVE, and `never pastel or dark` failed 2 of 6 where
  a cell was treated as empty space rather than a coloured field. Count 6 of 6; geometry 21 of
  21.
- 0.19 (2026-09-10): **all eight layouts in one set, and the fixes sort themselves.** Owner:
  *"tất cả các kiểu collage"*, *"phải là equal panels"*, *"constraints là ít cần thiết"*. Count
  **8 of 8**, geometry now **15 of 15**. Palette lands: celled rings read 22° and 32° against a
  corpus median of 47° where set 8 read 128–172°, and the gradient reads 179.3° against the
  corpus 174–177° where set 8 managed 65°. `Words:` lands 8 of 8; `corner-label` gone 0 of 8.
  **`pinboard`, `split-frame` and `polaroid` rendered for the first time and all three work.**
  `PARTS/layout` corrected on owner instruction: **`outlined-panels` takes EQUAL panels** — the
  corpus pair are equal and this file had glossed that as *"not a requirement"*, which cost set
  9 cell 4 a descending staircase that shrank the four non-hero units and broke the
  equal-prominence law from inside the layout instruction. And the record is sorted: a clause
  naming a share, a shape, a thing to draw or a string LANDS; one naming a distance or a
  prohibition does not, 0 of 12; the register is a draw and not a clause at all.
- 0.18 (2026-09-10): **geometry is settled, the margin is abandoned, and the palette clause was
  half a clause.** Owner: *"màu sắc chưa tối ưu"*, *"không được có chữ pick đứng góc dưới màn
  hình"*, and an instruction to restore the full `[PRODUCT REFERENCES]` block verbatim.
  **Count: geometry 5 of 5, 7 of 7 across two sets** — settled. **`plaque` fixed by geometry**
  on the first try after three failures from the name. **The margin is 0 of 8** against three
  wordings including a named position, and the control confirmed only that the old wording
  fails too: this file stops rewording it. **`PARTS/palette` gains the half it never had** —
  the corpus runs a median hue spread of 47° with 7 of 12 under 60°, against 160° across set 8,
  so celled layouts take a hue FAMILY while `open` gradients travel far, and one clause had
  been wrong in both directions. **`corner-label` is retired on owner instruction.** And two
  badges printed their own instructions — `LABEL`, `AAFERABLE BREAD QUALITY` — because a badge
  with three type levels was given three words for two of them.
- 0.17 (2026-09-10): **geometry fixes the count at 2 of 2, and one prompt rendered twice ends
  two hypotheses.** Owner rendered set 7's revision; cell 3 came back at 10:52 as flat vector
  and at 10:56, unchanged, as a photograph. **A clause carried in both draws cannot explain
  two registers**, so `PARTS/graphics` withdraws the two-layer cap of 0.14 AND the unit-size
  hypothesis of 0.16, and this type now holds that **one render is one draw** — a register
  verdict needs a repeat, which is namespace law and lives in
  `registry/toplist-instruction.md`. `PARTS/count` is answered: naming the hero's cell as a
  SHARE of the frame returned five on both layouts that had failed twice, while the one cell
  described by property alone returned six. **The margin clause fails 0 of 5** and fails as a
  global negative, exactly as the count did — the fix is the same, name the position rather
  than the prohibition. The badge's borrowed G10 escape route also failed on its first test:
  a panel edge is not a frame edge. `band` is confirmed 2 of 2 on a celled layout; `plaque`
  has now returned three different shapes from one name.
- 0.16 (2026-09-10): **set 7's long draft — `PARTS/count` fails at 0 of 1, and the graphics
  ceiling is probably the wrong variable.** Owner: *"hình ảnh sản phẩm thường bị 2d hoá, vẫn
  thừa số lượng sản phẩm"*. Cell 1 returned SIX with the explicit count clause present, in the
  same shape as set 6 cell 1: `colour-cells`, hero on an open field, five cells beside it. The
  count is therefore **a LAYOUT failure**, and the fix is geometry — name where the hero's cell
  is — because round 3 measured geometry landing 1 of 1 where taste landed 0 of 4. New
  `PARTS/distinctness` after cell 3 returned **four of five as one mould recoloured**: five
  references need the variants named, the way a same-person pair needs the invariants named.
  And `PARTS/graphics` loses its framing: across six graded frames **unit SIZE orders the
  register and layer count does not** — two three-layer frames sit at opposite ends and differ
  only in how large the units are drawn. Three measurements were attempted for it and **all
  three discarded for failing their own controls**, all for the same reason the ring metric
  fails here: this type's layouts leave no single ground and no separable subjects.
- 0.15 (2026-09-10): **set 6 — the count is a clause now, and the ceiling control confounded
  itself.** Owner: *"một số ảnh sai số lượng sản phẩm"*. Cell 1 returned **six** units from five
  references, repeating one Panasonic, and the word *five* was in that prompt three times —
  every time as a property of something else. New `PARTS/count`: the total and the
  no-repeat rule get their own binding clause, which is `field-coherence`'s lesson a second
  time. **The per-FRAME accent wording is settled at 3 of 3** and the badge-in-the-hero-cell
  rule at 4 of 5 with the dead white gap gone in all five — but the same accent fix put three
  labels inside G10's 8% floor, one rule touching the frame edge, so a frame-level element now
  states how far in as well as how many. Cell 4's badge crossed out of a narrow panel: the
  clause gains G10's own escape route, **make the badge smaller**. `field-coherence` fails a
  fourth time on a prompt that had NAMED the exclusion, so exclusions are replaced by a
  positive defining feature. A title arrived unasked in 2 of 6, both where the badge already
  carried the category word. And the ring metric is recorded as **unusable on six of eight
  layouts** — `blocks` returns saturation 0.00 for a composition built on four colours.
- 0.14 (2026-09-09): **badge placement, and the graphics ceiling.** Owner: *"nếu có frame lớn
  nhất thì badge đặt ngay trong frame đấy"* — MARKS gains PLACEMENT, and it also fixes what
  set 5 showed: two celled frames put the badge on bare ground and each opened a dead white
  gap in a composition that otherwise tiles edge to edge. Inside the hero cell the colour rule
  simplifies from *clear every cell* to *clear one*. **`PARTS/graphics` gains a cap of TWO**:
  cell 5 stacked three and all five products came back as flat vector illustrations — a
  register flip rather than clutter, which is the layer's one real failure mode. And an accent
  described once must say whether it is per-FRAME or per-CELL: *"a corner-label in the lower
  left"* produced five of them. `PARTS/field-coherence` held on its first outing.
- 0.13 (2026-09-09): **two owner notes, and one of them names a fault three sets old.**
  *"kettle bị sai"* — set 3 cell 5 printed TRAVEL KETTLES over four ordinary kitchen kettles.
  New `PARTS/field-coherence`: every unit must plausibly BE the category the frame names, not
  only the hero. **No prompt in this library has ever required that**, and it has now failed
  three times across two types. New `PARTS/graphics` for *"chưa có nhiều graphic element linh
  hoạt, hiệu ứng"* — six elements counted off frames actually seen, plus two borrowed from
  `lede-winner`'s corpus and untested here. They stack; what they may not do is cross a
  product's face.
- 0.12 (2026-09-09): **set 4 landed both new layouts and failed to fix the lettering.**
  `split-frame` held one product identical across a cut-out half and a photographed half
  twice, and reads as this type with no mark at all — which is what both corpus frames do.
  `polaroid` held one belt across three prints. `shield` rendered at last and is the best
  badge of the run. Blocks came back FLAT after set 3's 3D slabs, on one added constraint.
  **The destination clause did not reduce invented lettering** — 2 of 5 against 0 of 1 in a
  control too small to conclude from — and what the two failures share is a large blank brand
  surface on the product rather than anything about the wording. Recorded as a hypothesis at
  2 of 2. Eleven instances across the namespace.
- 0.11 (2026-09-09): **set 3 settled the hero and its control refused to be one.** Size is the
  operative variable — centre plus largest reads, largest off-centre reads, centre at equal
  size does not. And the no-hero control produced a hero anyway, as set 2's had: **two of two**,
  so the layout wants a focal unit and sets 1-2 were fighting it. The five-point badge FINISH
  standard delivered 5 of 5 on its first outing. Cell 4 did not render, so `shield` is still
  untested. **Invented lettering reaches nine instances across the namespace**, every one
  under a prompt that banned it — recorded with G10's own diagnosis: a prohibition with no
  sanctioned escape route is resolved in whichever direction the model likes.
- 0.10 (2026-09-09): **the owner named eight frames as the type and it grew by two layouts
  and a subject kind.** `split-frame` (a cut-out on a patterned ground beside a real
  photograph of the same product, 2 observations) and `polaroid` (instant prints overlapping
  on a designed ground, 1) join `PARTS/layout`, taking it to eight forms over twelve frames.
  `PARTS/subject` gains a third kind — one product in several views — which 0.7 had explicitly
  excluded. `PARTS/hero` corrected against set 3's own control: **size is required and centre
  alone is not enough**; the equal-size centre cell produced no visible hero. Curation batch E
  reverses two records from batch D, made four hours earlier on the owner's earlier naming.
- 0.9 (2026-09-09): **`PARTS/hero` added, and it scopes a law every earlier version enforced
  the wrong way.** Owner: the page's own product is always centre or largest. The app builds a
  page for ONE product, so the lede is a hero plus a field, not a neutral index — nine renders
  across two sets were built to the opposite. The no-favoured-unit law now covers the other
  four only, and the FIRST attachment carries the hero until `products[]` exists. Flagged as
  namespace-wide: `lede-lineup` holds the same law and will meet the same correction. MARKS
  gains a **FINISH** standard after all five set-2 badges met 0.8's spec and still read flat:
  three type levels, a device, a silhouette that is not a plain rectangle, text following a
  round form, and a shadow — counted off the corpus roundel, which carries all five.
- 0.8 (2026-09-09): **set 1 rendered and the owner named colour and layout as flat.** Both
  faults trace to my own prompt text: cell 3 asked for *"one flat tone shared by all five
  panels"* and cell 4 for *"its own lighter or deeper shade of that same hue"*, and those two
  are the cells he named. New `PARTS/palette` — several HUES across the cells, which is what
  the two working cells and both corpus frames do. New `PARTS/arrangement` — uniform is not
  the same as fair; the law is about PROMINENCE and 0.7 added identical panel sizes on top of
  it, producing a spec sheet. A badge is now wanted on owner instruction rather than on
  evidence, and the title block owes an internal tone step and two type sizes like any other
  mark. Records the authoring trap this is the third instance of in one day: a constraint
  aimed at one fault but written as a general property removes the whole dimension.
- 0.7 (2026-09-09): **curation first, then every clause re-measured on the corrected set.**
  Nine ledger corrections (batch 2026-09-09-D) driven by the owner's named example frames:
  `proposed lede-mosaic` is absorbed and closes at zero, and the type goes from 1 match to 7.
  New `PARTS/layout` — six index layouts across seven frames, which is the owner's *"đa dạng
  layout"* made into an axis. New `PARTS/subject`: one subject in several states IS the type,
  reversing what 0.5 called a foreign shape. `PARTS/ground` rewritten, and **the old bimodal
  claim is refuted** — hue spread runs 1° to 177° continuously, so a gradient is a choice with
  a free amount of travel rather than one of two settings. The light-AND-coloured pair is
  imported from `lede-authority`, which proved it against a control.
- 0.6 (2026-09-09): **FOUNDING RENDER ROUND** — one render, round 2 prompt 6 at 0.5,
  `partial`. ADR-076's multi-reference route delivered four distinct units from four
  attachments in one call: first evidence that this type is makeable. Question 8 answered
  against the file — the plaque over unit 2 occludes it and reads as a floating label,
  neither favouring nor naming. Four failures recorded and none patched at 1 of 1; the
  `[TITLE]` G10 breach was written into the prompt, which asked for margin-to-margin and
  for a tenth of clearance in the same breath. Ring texture is unusable on a frame whose
  title reaches the edge.
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

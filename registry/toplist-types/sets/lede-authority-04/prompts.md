# `lede-authority` set 4 — the author with a FIELD, and the answer to "so sánh nhiều sản phẩm?"

Written against **`lede-authority` v0.6**. Set 3 settled the type's craft: four `pass`, one
`partial`, and the control failed exactly as declared — cells 4 and 6 were the same picture
differing only in trade dress, and only the dressed one worked. **This set changes subject.**

## Answering the question first

*"Type này author có so sánh nhiều sản phẩm không?"* — **Yes, and it is probably the shape
this type most needs.** A top-N page is about N products. A lede showing its author holding
ONE of them argues less than the page claims: at best *this person knows about this thing*,
where the page promises *this person weighed all of them*.

The four frames named on 2026-09-09 carry **two distinct shapes**, and this file has neither:

| shape | what it is | named frame |
|---|---|---|
| **author + FIELD** | the reviewer to one side, the whole tested field ranged across the frame | the router review — four routers on a desk, the reviewer at the left |
| **one subject, SEVERAL PANELS** | the same person repeated in cut-out panels on one designed ground, each panel a different product worn | the two shopping-diary frames — three outfits, three panels |

A third named frame is the single-product studio form this type already has at 4
observations, so it is not re-tested here.

**What this set does NOT do.** `products_in_frame` stays `one` in the frontmatter until a
render exists, because that field is a routing promise. The cost of moving it is real and
worth knowing before anyone asks for it: `mapping/toplist-rules.md` layer 1 refuses
`products_in_frame: many` on any page whose input carries fewer than three products with a
photo each, and the input schema has **no `products[]` field at all**. Declaring `many` today
would make this type unroutable on every page — the condition `lede-winner` already sits in
behind the missing rank field. **So: render first, then decide, then pay for the schema.**

The router frame also carries baked display type and red arrows. This type declares no
`text_layer` and this set adds none — ADR-071 settled which types carry one on evidence, and
adding it here would confound the shape being tested with a permission being taken.

## The cells

Everything set 3 confirmed is now a constant: trade dress, clean product, composed subject,
no second person, and the ground/act lock. **The variable is the SHAPE.**

| cell | products | shape | ground |
|---|---|---|---|
| 1 | 5 wireless earbuds | author + FIELD | studio |
| 2 | 4 air fryers | author + FIELD | contextual, test kitchen |
| 3 | 3 pairs of walking boots | one subject, **3 panels** | designed |
| 4 | 1 cordless vacuum | author + **two views of one product** | studio |
| 5 | 5 mechanical keyboards | author + FIELD **+ one held as hero** | studio |
| 6 | 1 cordless circular saw | single product, contextual / using | **CONTROL** |

**Cell 6 is the control and it is expected to PASS.** It is the form set 3 proved, on a new
product, and it exists so the five new shapes have a known-good frame to be compared against
in the same batch under the same conditions. Set 3's control was built to fail; this one is
built to succeed. **A batch with no anchor cannot tell a shape failing from a bad day.**

It also answers the owner's note on set 3's last frame directly — *"chưa thể hiện author có
kinh nghiệm gì về khoan/công cụ"* — by giving a power tool the dress, the place and the act
that the impact-driver cell was deliberately denied.

**Cell 4 is the narrowest reading of *"cần có thêm góc nhìn khác cho sản phẩm"***: one
product, two faces of it visible at once, without a second unit and without a panel grid.

Attachments: 5, 4, 3, 1, 5, 1. Cells 1, 2, 3 and 5 need one photo per unit and exceed what
the owner's own app takes, so they ship in full and render elsewhere (ADR-076). Twelve
products across the set, none used in sets 1–3 or rounds 1–3.

## Coherence test, run before shipping

| cell | correct usage context? | visibly an expert? | what is the background doing? |
|---|---|---|---|
| 1 | presented — a studio field is a comparison laid out, not a use | audio reviewer's own listening desk kit is absent by design; the ACT of having them all is the signal | nothing. The field and the person carry it |
| 2 | yes — air fryers on a test-kitchen bench is where they get compared | test-kitchen whites and a working bench | says these were cooked in, not unboxed for a photo |
| 3 | worn — each panel is the boot doing its job on a foot | hillwalking kit, boots laced and worn | a designed ground, so the panels read as an index rather than three snapshots |
| 4 | presented — studio, so the act is showing it, from two sides | cleaning professional's tabard | nothing, deliberately |
| 5 | presented — a reviewer's field with one lifted out | a keyboard reviewer at a desk that is plainly his | nothing beyond the desk plane |
| 6 | yes — a saw cuts, and he is at the cut | joiner's workwear, ear defenders round the neck | a real joinery shop says he works there |

---

## 1 — five wireless earbuds · author + FIELD, studio

```
TYPE: lede-authority v0.6 — SET 4 CELL 1
REGISTER: editorial portrait photograph, one frame, no words in it.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every unit is clean and as-new — cases unscuffed, buds unmarked.
[FIELD]     the five earbud cases open in a row across the lower half of the frame, on a
            plane at chest height, each turned so its buds and case read.
[SUBJECT]   an audio reviewer in her thirties standing behind the row at one side, one
            case lifted in her hand above the line of the others.
[ADDRESS]   looking into the lens, composed, speaking evenly.
[GROUND]    a plain studio backdrop in one strong saturated colour, filling the frame
            behind her and the row. No room, no set, no props but the five units.
[LIGHT]     a soft broad key for the whole group, the backdrop lit evenly.
[GRADE]     a clean natural palette, skin held true, no cast from the backdrop.

CONSTRAINTS — binding.
· Editorial register: this photograph is made by somebody else. No selfie framing, no
  arm's-length camera, no phone in shot, no front-camera distortion.
· One person only. No second person anywhere in frame.
· Her expression is settled. Not startled, not mid-flinch, not caught off guard.
· No unit favoured by size or lighting; the lifted one is raised and nothing else.
· Nothing worn or shown as proof of qualification, and no name, caption or title card.
· No printed word or number anywhere that names or qualifies a person.
· Every unit stays clear of every frame edge.
```

---

## 2 — four air fryers · author + FIELD, test kitchen

```
TYPE: lede-authority v0.6 — SET 4 CELL 2
REGISTER: editorial portrait photograph, one frame, no words in it.

[PRODUCT REFERENCES] four attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Four different makers.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every unit is clean and as-new — housings unmarked, baskets bright.
[FIELD]     the four air fryers in a row along a test-kitchen bench, evenly spaced, each
            turned so its control panel and basket read.
[SUBJECT]   a food writer in her forties in a clean kitchen tunic standing behind the row
            at one side, one hand resting on the bench beside the nearest unit.
[ADDRESS]   looking into the lens, composed, speaking evenly.
[PLACE]     a working test kitchen at the tidy end of a session: the bench wiped clear
            apart from the four units, a notebook squared off, nothing stacked.
[GROUND]    the kitchen behind her, ordered and bright, thrown gently out of focus.
[LIGHT]     bright even kitchen light, no deep shadow anywhere.
[GRADE]     a clean natural palette, skin held true.

CONSTRAINTS — binding.
· Editorial register: this photograph is made by somebody else. No selfie framing, no
  arm's-length camera, no phone in shot, no front-camera distortion.
· One person only. No second person anywhere in frame.
· Her expression is settled. Not startled, not mid-flinch, not caught off guard.
· No unit favoured by size, height or lighting.
· Nothing in frame is dirty, greasy, stacked or waiting to be washed.
· Nothing worn or shown as proof of qualification, and no name, caption or title card.
· No printed word or number anywhere that names or qualifies a person, and no reading is
  legible on any control panel.
· Every unit stays clear of every frame edge.
```

---

## 3 — three pairs of walking boots · one subject, THREE PANELS

```
TYPE: lede-authority v0.6 — SET 4 CELL 3
REGISTER: editorial composition, three panels in one frame, no words in it.

[PRODUCT REFERENCES] three attached photos, one per pair, in the order given. Each is the
            exact reference for that pair — preserve shape, proportions, material, finish
            and colour exactly. Three different makers.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every pair is clean and as-new — uppers unscuffed, soles unworn.
[PANELS]    three upright panels side by side across the frame, equal in width and height,
            each holding the SAME woman photographed full length in hillwalking kit.
[SUBJECT]   she wears a different pair in each panel — panel 1 the first reference, panel 2
            the second, panel 3 the third — standing squarely, boots fully visible.
[ADDRESS]   in every panel she is looking into the lens, composed, the same person with
            the same hair, the same kit above the ankle and the same light.
[GROUND]    one designed field behind all three panels — a single flat saturated colour,
            with a thin outline framing each panel.
[LIGHT]     one identical soft key across all three panels.
[GRADE]     a clean natural palette, skin held true.

CONSTRAINTS — binding.
· The three panels are one photograph, not a collage of different shoots: same person,
  same framing, same distance, same light in each.
· One person only, appearing three times. No second person anywhere in frame.
· Her expression is settled in all three. Not startled, not caught off guard.
· No panel favoured by size, height or lighting.
· Nothing worn or shown as proof of qualification, and no name, caption or title card.
· No printed word or number anywhere in the frame.
· Every boot stays clear of every frame edge and of every panel outline.
```

---

## 4 — cordless vacuum · author + TWO VIEWS of one product, studio

```
TYPE: lede-authority v0.6 — SET 4 CELL 4
REGISTER: editorial portrait photograph, one frame, no words in it.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cordless vacuum.
            Preserve shape, proportions, material, finish and colour exactly.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] the vacuum is clean and as-new — bin clear, brush head unmarked.
[SUBJECT]   a cleaning professional in her forties in a plain work tabard, the vacuum held
            upright in one hand with its brush head toward the lens, and its detached
            hand-unit held in the other hand turned so its bin and filter read.
[VIEWS]     the two halves show two different faces of the same machine at once — the
            working end, and the part that comes off.
[ADDRESS]   looking into the lens between the two, composed, speaking evenly.
[GROUND]    a plain studio backdrop in one strong saturated colour, filling the frame
            behind her. No room, no set, no props but the vacuum.
[LIGHT]     a soft key from the front, the backdrop lit evenly, clean detail in both parts.
[GRADE]     a clean natural palette, skin held true, no cast from the backdrop.

CONSTRAINTS — binding.
· Editorial register: this photograph is made by somebody else. No selfie framing, no
  arm's-length camera, no phone in shot, no front-camera distortion.
· One person only. No second person anywhere in frame.
· Her expression is settled. Not startled, not mid-flinch, not caught off guard.
· Both parts belong to the one machine in the reference. No second product.
· Nothing worn or shown as proof of qualification, and no name, caption or title card.
· No printed word or number anywhere that names or qualifies a person.
· Both parts stay clear of every frame edge.
```

---

## 5 — five mechanical keyboards · author + FIELD + one held as hero, studio

```
TYPE: lede-authority v0.6 — SET 4 CELL 5
REGISTER: editorial portrait photograph, one frame, no words in it.

[PRODUCT REFERENCES] five attached photos, one per unit, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every unit is clean and as-new — keycaps unworn, cases unscuffed.
[FIELD]     four of the five keyboards laid flat in a row across the lower third of the
            frame, evenly spaced, each turned the same way.
[HERO]      the fifth held up by the subject at chest height, tilted so its keycaps and
            side profile read.
[SUBJECT]   a keyboard reviewer in his thirties in a plain dark shirt, standing behind the
            row, both hands on the lifted unit.
[ADDRESS]   looking into the lens over the lifted keyboard, composed, speaking evenly.
[GROUND]    a plain studio backdrop in one strong saturated colour, filling the frame
            behind him and the row. No room, no set, no props but the five units.
[LIGHT]     a soft broad key for the whole group, the backdrop lit evenly.
[GRADE]     a clean natural palette, skin held true, no cast from the backdrop.

CONSTRAINTS — binding.
· Editorial register: this photograph is made by somebody else. No selfie framing, no
  arm's-length camera, no phone in shot, no front-camera distortion.
· One person only. No second person anywhere in frame.
· His expression is settled. Not startled, not mid-flinch, not caught off guard.
· The four in the row are equal to each other in size, height and lighting; only the
  lifted one is raised.
· Nothing worn or shown as proof of qualification, and no name, caption or title card.
· No printed word or number anywhere that names or qualifies a person.
· Every unit stays clear of every frame edge.
```

---

## 6 — cordless circular saw · CONTROL, the form set 3 proved

**This cell is expected to PASS.** It is the anchor: single product, trade dress, real place,
using it — the shape set 3 landed four times. It exists so the five new shapes above are
graded against a known-good frame from the same batch, and it answers the note on set 3's
last cell by giving a power tool everything that one was denied.

```
TYPE: lede-authority v0.6 — SET 4 CELL 6, CONTROL
REGISTER: editorial portrait photograph, one frame, no words in it.

[PRODUCT REFERENCE] the attached photo is the exact reference for the cordless circular
            saw. Preserve shape, proportions, material, finish and colour exactly.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] the saw is clean and as-new — shoe unscratched, guard unmarked, blade bright.
[SUBJECT]   a joiner in his fifties in workwear with ear defenders round his neck, the saw
            in both hands at the end of a cut along a marked board on the bench.
[ADDRESS]   he has straightened from the cut and turned to the lens, composed, speaking
            evenly. The saw stays where the work is.
[PLACE]     an orderly joinery shop: boards stacked square, the bench clear apart from the
            job, the floor swept, tools racked behind.
[GROUND]    the shop behind him, ordered and evenly lit, thrown gently out of focus.
[LIGHT]     bright even shop light. Nothing falls into murk.
[GRADE]     a clean natural palette, skin held true.

CONSTRAINTS — binding.
· Editorial register: this photograph is made by somebody else. No selfie framing, no
  arm's-length camera, no phone in shot, no front-camera distortion.
· One person only. No second person anywhere in frame, including the background.
· His expression is settled. Not startled, not mid-flinch, not caught off guard.
· He is at the work, not posed beside it.
· Nothing worn or shown as proof of qualification, and no name, caption or title card.
· No printed word or number anywhere that names or qualifies a person.
· The saw is clean and stays clear of every frame edge.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **Cells 1, 2, 5 — does an author standing with a FIELD read as somebody who tested them all?** | whether this type gains the shape a top-N page actually needs, and with it a `products_in_frame` change and the `products[]` schema behind it |
| 2 | **Did five and four real units survive from their own references, beside a person?** | ADR-076's route has never been run with a human in the frame; a person competes for the model's attention with the units |
| 3 | **Cell 3 — do three panels read as ONE person in three products, or as three different people?** | the multi-panel shape. Same-identity across panels is the library's known-hardest single-pass problem (adapter Rule 5) |
| 4 | **Cell 4 — do two views of one machine read as one product, or as two products?** | the narrowest reading of *"góc nhìn khác cho sản phẩm"*, and whether it needs a second unit at all |
| 5 | **Cell 5 — does lifting one unit out of the field favour it, or just point at it?** | the same question `lede-collage` MARKS asked about a badge over one unit, on a different mechanism |
| 6 | **Cell 6 — does the anchor pass?** | if it does not, the batch was a bad day and nothing above is evidence |
| 7 | **Across all six: any second person, any soiled unit, any startled face?** | the three constants set 3 established. Two clean sets would retire them as worries |
| 8 | **How many CONSTRAINTS held across the six?** | the running record for the two-block form |

# `lede-authority` set 6 — the grid is gone, and the studio ground gets fixed on a measurement

Written against **`lede-authority` v0.8**. Owner verdict on set 5, 2026-09-09: *"ảnh thiếu
chân thực, loại bỏ kiểu grid cho authority. có thể giới thiệu 1 hoặc nhiều sản phẩm với
background phù hợp, author phù hợp. các nền studio cần sáng hơn, nổi bật, bắt mắt hơn."*

## Why the grid died, and it was not execution

0.7's framing law worked: every shoe and every jacket filled its cell and read clearly, which
is exactly what set 4's panels could not do. **The form failed on register.** Six cells at
identical framing, identical pose and identical light read as a mockup sheet — and the jacket
cell, which held the same woman's face across all six panels, is the clearest case: holding
the identity perfectly is what made it look like a passport sheet. **A composition whose
cells are interchangeable has no moment in it, and a photograph is a moment.**

The no-author control answered its own question on the way out: six product cells and nobody
in them is a competent frame, and it is `lede-collage`. The author cell was never decoration.
With the grid gone, so is the question.

**`single` and `field` survive**, both proven, and the type may carry one product or several.

## The ground was wrong nine times out of nine, and the cause was one phrase of mine

Every studio frame this type has produced, measured with the same ring metric as the corpus:

| | value | saturation |
|---|---|---|
| **our nine, median** | **0.35** | **0.99** |
| the owner's own named studio frame | 0.67 | 0.73 |
| corpus `lede-winner` designed ground | **0.99** | 0.55 |
| corpus `lede-collage` designed ground | **0.90** | 0.49 |

Seven of the nine came back at saturation **0.99** — the maximum. All nine prompts carried the
same words: *"a plain studio backdrop in one strong saturated colour"*. **That phrase returns
a deep, dark, fully-saturated field, and it has now done so nine times out of nine.**

The correction already existed in this namespace and this file never imported it. ADR-073:
*"Light AND strongly coloured — both together, since a dark saturated field and a light quiet
field are each only half of what the corpus does."*

**So every studio cell below asks for LIGHT and COLOURED together, and carries a checkable
test rather than an adjective:** the backdrop is lighter than the subject's clothing and
lighter than the product. That is the round-3 lesson applied — geometry holds where taste
does not.

## The cells

| cell | product(s) | form | ground | isolates |
|---|---|---|---|---|
| 1 | 5 electric shavers | field | **light coloured studio** | the ground correction on the proven multi-product form |
| 2 | 1 chainsaw | single | contextual, forestry yard | `single` + contextual, unchanged and proven |
| 3 | 5 baby monitors | field | **light coloured studio** | the correction again, on a category with no trade dress |
| 4 | 1 sewing machine | single | **light coloured studio** | the correction on the single-product form |
| 5 | 5 secateurs | field | contextual, ordered nursery | `field` in a real place — only one of four field frames has been contextual |
| 6 | 1 telescope | single | **dark saturated studio — CONTROL** | keeps the old wording so the batch contains one dark ground to compare against |

**Cell 6 is the control and it is expected to look worse.** It carries the exact phrase the
other studio cells drop — *"one strong saturated colour"* — so the correction is isolated
rather than assumed. If cell 6 comes back at value ~0.35 and the others near 0.90, the phrase
was the cause and the fix is proven in one batch. If they all come back the same, the phrase
was innocent and the problem is elsewhere.

Six products, none used in sets 1–5 or rounds 1–3. Attachments: 5, 1, 5, 1, 5, 1. Cells 1, 3
and 5 exceed what the owner's app takes and render elsewhere (ADR-076). No text layer.

## Coherence test, run before shipping

| cell | correct usage context? | visibly an expert? | what is the background doing? |
|---|---|---|---|
| 1 | presented — a studio field is a comparison laid out | barber's smock; shavers are his trade | nothing but lift: a light colour that pushes dark shavers forward |
| 2 | yes — a chainsaw cuts, and he is at the cut | forestry PPE, helmet and chaps | a working yard says he does this |
| 3 | presented — a field on one plane | **no trade dress exists for this**; the field supplies the standing | lift only |
| 4 | yes — a sewing machine sews, and it is threaded and running under her hands | dressmaker's tape round the neck, pinned work | lift only; the studio removes the room |
| 5 | yes — secateurs prune, and the row is what she prunes with | nursery apron, gloves, soil on the bench not on her | an ordered nursery says the tools are hers |
| 6 | presented — studio | astronomer's fleece, star chart absent by design | **deliberately dark. That is the control** |

---

## 1 — five electric shavers · field, LIGHT coloured studio

```
TYPE: lede-authority v0.8 — SET 6 CELL 1
REGISTER: editorial portrait photograph, one frame, no words in it.

[PRODUCT REFERENCES] five attached photos, one per shaver, in the order given. Each is the
            exact reference for that unit — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every shaver is clean and as-new — heads bright, bodies unmarked.
[FIELD]     four of the five standing upright in a row across the lower third of the frame
            on a plane at chest height, evenly spaced, each turned so its head reads.
[HERO]      the fifth held up by the subject at chest height, angled so its head and body
            both read.
[SUBJECT]   a barber in his forties in a black barber's smock, standing behind the row.
[ADDRESS]   looking into the lens over the lifted shaver, composed, speaking evenly.
[GROUND]    a plain studio backdrop in a LIGHT, clear, vivid colour, filling the frame
            behind him and the row — bright and eye-catching, not a deep or dark tone.
[LIGHT]     a soft broad key for the whole group, the backdrop lit evenly and brightly.
[GRADE]     a clean natural palette, skin held true, no cast from the backdrop.

CONSTRAINTS — binding.
· The backdrop is LIGHTER than the subject's clothing and LIGHTER than every product.
· Editorial register: this photograph is made by somebody else. No selfie framing, no
  arm's-length camera, no phone in shot, no front-camera distortion.
· One person only. No second person anywhere in frame.
· His expression is settled. Not startled, not mid-flinch, not caught off guard.
· The four in the row are equal in size, height and lighting; only the lifted one is raised.
· No name, caption, title card, lanyard or certificate, and no word or number that names
  or qualifies a person.
· Every unit stays clear of every frame edge.
```

---

## 2 — chainsaw · single, contextual forestry yard

```
TYPE: lede-authority v0.8 — SET 6 CELL 2
REGISTER: editorial portrait photograph, one frame, no words in it.

[PRODUCT REFERENCE] the attached photo is the exact reference for the chainsaw. Preserve
            shape, proportions, material, finish and colour exactly.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] the saw is clean and as-new — bar bright, housing unmarked, chain unblunted.
[SUBJECT]   an arborist in her forties in forestry PPE — helmet with the visor up, ear
            defenders, cut-resistant chaps — the saw in both hands at the end of a cut
            through a seasoned log on a trestle.
[ADDRESS]   she has straightened from the cut and turned to the lens, composed, speaking
            evenly. The saw stays where the work is.
[PLACE]     an orderly forestry yard: logs stacked square, the ground swept of chips,
            the trestle clear apart from the cut.
[GROUND]    the yard behind her, ordered and evenly lit, thrown gently out of focus.
[LIGHT]     bright flat daylight. Nothing falls into murk.
[GRADE]     a clean natural palette, skin held true.

CONSTRAINTS — binding.
· Editorial register: this photograph is made by somebody else. No selfie framing, no
  arm's-length camera, no phone in shot, no front-camera distortion.
· One person only. No second person anywhere in frame, including the background.
· Her expression is settled. Not startled, not mid-flinch, not caught off guard.
· She is at the work, not posed beside it.
· No name, caption, title card, lanyard or certificate, and no word or number that names
  or qualifies a person.
· The saw is clean and stays clear of every frame edge.
```

---

## 3 — five baby monitors · field, LIGHT coloured studio, no trade dress

```
TYPE: lede-authority v0.8 — SET 6 CELL 3
REGISTER: editorial portrait photograph, one frame, no words in it.

[PRODUCT REFERENCES] five attached photos, one per monitor, in the order given. Each is
            the exact reference for that unit — preserve shape, proportions, material,
            finish, colour and every printed mark exactly. Five different makers.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every monitor is clean and as-new — screens unscratched, housings unmarked.
[FIELD]     four of the five standing in a row across the lower third of the frame on a
            plane at chest height, evenly spaced, each turned so its screen and camera read.
[HERO]      the fifth held up by the subject at chest height, its screen toward the lens.
[SUBJECT]   a product reviewer in her thirties in a plain, well-fitted top — there is no
            trade dress for this category, and the five in front of her are the credential.
[ADDRESS]   looking into the lens over the lifted unit, composed, speaking evenly.
[GROUND]    a plain studio backdrop in a LIGHT, clear, vivid colour, filling the frame
            behind her and the row — bright and eye-catching, not a deep or dark tone.
[LIGHT]     a soft broad key for the whole group, the backdrop lit evenly and brightly.
[GRADE]     a clean natural palette, skin held true, no cast from the backdrop.

CONSTRAINTS — binding.
· The backdrop is LIGHTER than the subject's clothing and LIGHTER than every product.
· Editorial register: this photograph is made by somebody else. No selfie framing, no
  arm's-length camera, no phone in shot, no front-camera distortion.
· One person only. No second person anywhere in frame. No child, no infant, no doll.
· Her expression is settled. Not startled, not mid-flinch, not caught off guard.
· The four in the row are equal in size, height and lighting; only the lifted one is raised.
· No name, caption or title card, and no reading is legible on any screen.
· Every unit stays clear of every frame edge.
```

---

## 4 — sewing machine · single, LIGHT coloured studio

```
TYPE: lede-authority v0.8 — SET 6 CELL 4
REGISTER: editorial portrait photograph, one frame, no words in it.

[PRODUCT REFERENCE] the attached photo is the exact reference for the sewing machine.
            Preserve shape, proportions, material, finish and colour exactly.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] the machine is clean and as-new — body unmarked, plate bright.
[SUBJECT]   a dressmaker in her fifties, a tape measure round her neck and a pincushion on
            her wrist, both hands guiding a seam through the machine on the plane in front
            of her. The machine is threaded and the work is under the foot.
[ADDRESS]   she has looked up from the seam to the lens, composed, speaking evenly. Her
            hands stay on the work.
[GROUND]    a plain studio backdrop in a LIGHT, clear, vivid colour, filling the frame
            behind her — bright and eye-catching, not a deep or dark tone. No room, no set,
            no props but the machine and the seam.
[LIGHT]     a soft key from the front, the backdrop lit evenly and brightly.
[GRADE]     a clean natural palette, skin held true, no cast from the backdrop.

CONSTRAINTS — binding.
· The backdrop is LIGHTER than the subject's clothing and LIGHTER than the machine.
· Editorial register: this photograph is made by somebody else. No selfie framing, no
  arm's-length camera, no phone in shot, no front-camera distortion.
· One person only. No second person anywhere in frame.
· Her expression is settled. Not startled, not mid-flinch, not caught off guard.
· No name, caption, title card, lanyard or certificate, and no word or number that names
  or qualifies a person, and no reading is legible on the machine.
· The machine is clean and stays clear of every frame edge.
```

---

## 5 — five secateurs · field, ORDERED contextual nursery

```
TYPE: lede-authority v0.8 — SET 6 CELL 5
REGISTER: editorial portrait photograph, one frame, no words in it.

[PRODUCT REFERENCES] five attached photos, one per pair, in the order given. Each is the
            exact reference for that pair — preserve shape, proportions, material, finish,
            colour and every printed mark exactly. Five different makers.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] every pair is clean and as-new — blades bright, handles unmarked.
[FIELD]     four of the five laid open in a row along a potting bench across the lower
            third of the frame, evenly spaced, each turned so its blade and handle read.
[HERO]      the fifth held up by the subject at chest height, open, angled so its blade reads.
[SUBJECT]   a nurserywoman in her sixties in a canvas apron and gloves, standing behind
            the bench.
[ADDRESS]   looking into the lens over the lifted pair, composed, speaking evenly.
[PLACE]     an orderly plant nursery: trays of young plants ranked square behind her, the
            bench swept clear apart from the five, soil on the bench and not on her apron.
[GROUND]    the nursery behind her, ordered and brightly lit, thrown gently out of focus.
[LIGHT]     bright even daylight through glass. Nothing falls into murk.
[GRADE]     a clean natural palette, skin held true.

CONSTRAINTS — binding.
· Editorial register: this photograph is made by somebody else. No selfie framing, no
  arm's-length camera, no phone in shot, no front-camera distortion.
· One person only. No second person anywhere in frame, including the background.
· Her expression is settled. Not startled, not mid-flinch, not caught off guard.
· The four in the row are equal in size, height and lighting; only the lifted one is raised.
· No name, caption, title card, lanyard or certificate, and no word or number that names
  or qualifies a person.
· Every pair is clean and stays clear of every frame edge.
```

---

## 6 — telescope · CONTROL, the old dark-ground wording

**This cell is expected to look worse than cells 1, 3 and 4.** It keeps the exact phrase the
other studio cells drop, so the ground correction is isolated rather than assumed. Measure it
against them: if this one lands near value 0.35 and they land near 0.90, the phrase was the
cause and one batch settles it.

```
TYPE: lede-authority v0.8 — SET 6 CELL 6, CONTROL
REGISTER: editorial portrait photograph, one frame, no words in it.

[PRODUCT REFERENCE] the attached photo is the exact reference for the telescope. Preserve
            shape, proportions, material, finish and colour exactly.

ELEMENTS — assemble and style these as the picture needs.
[CONDITION] the telescope is clean and as-new — tube unmarked, optics clear.
[SUBJECT]   an amateur astronomer in his fifties in a plain fleece, one hand on the
            telescope's focuser where it stands on its tripod beside him.
[ADDRESS]   looking into the lens, composed, speaking evenly.
[GROUND]    a plain studio backdrop in one strong saturated colour, filling the frame
            behind him. No room, no set, no props but the telescope and its tripod.
[LIGHT]     a soft key from the front, the backdrop lit evenly.
[GRADE]     a clean natural palette, skin held true, no cast from the backdrop.

CONSTRAINTS — binding.
· Editorial register: this photograph is made by somebody else. No selfie framing, no
  arm's-length camera, no phone in shot, no front-camera distortion.
· One person only. No second person anywhere in frame.
· His expression is settled. Not startled, not mid-flinch, not caught off guard.
· No name, caption, title card, lanyard or certificate, and no word or number that names
  or qualifies a person.
· The telescope is clean and stays clear of every frame edge.
```

---

## Grading

| # | question | what it changes |
|---|---|---|
| 1 | **Cells 1, 3, 4 against cell 6 — did the ground get lighter?** | measured, not judged: nine of nine have come back at value 0.35. If the new wording lands near 0.90 and the control stays at 0.35, `PARTS/ground` is fixed |
| 2 | **Do the light grounds read as brighter and more eye-catching, or just washed out?** | whether *light AND coloured* is the right target or whether the corpus figure needs adjusting for a frame with a person in it |
| 3 | **Cell 3 — does a field carry standing with no trade dress at all?** | the qualification added at 0.7 on one observation. Two would make it a clause |
| 4 | **Cell 5 — does `field` work in a real place?** | only one of four field frames has been contextual, and it was the strongest of them |
| 5 | **Cells 2 and 5 — are the products the right ones for the category?** | set 5 asked for running watches and got dress chronographs; nothing in a prompt has ever required the units to be plausible for the use |
| 6 | **Across all six: any second person, any soiled unit, any startled face, any selfie framing?** | the four constants. Three clean sets would retire them |
| 7 | **How many CONSTRAINTS held across the six?** | the running record for the two-block form |

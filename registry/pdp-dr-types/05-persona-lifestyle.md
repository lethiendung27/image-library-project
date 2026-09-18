---
id: 05-persona-lifestyle
step: 5
job: persona
device: lifestyle
version: "0.2"
status: reserved
replaced_by: null
channels: [landing-page]
requires_product_photo: false
generation_mode: single-pass
axes: {}
variants: []
exempt_from: [G3, G4]
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: "Criterion 3: the owner failed this type's first render, set section-02, on quality against the instruction (ADR-111); set section-03, the same fields written by the instruction as it stands, is the trial that decides the skeleton, and the verdict SPEC 6.3 asks for is the owner's. Criterion 1: no corpus record carries this id, because the type is written from the owner's image instruction of 2026-09-18 rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-110."
---

# 05-persona-lifestyle — PDP-DR SECTION TYPE, DRAFT

**The OTHER mode of the owner's image instruction** (`~/Downloads/images prompt.txt`, 2026-09-18,
ADR-110). One of six section types, for the images outside the product card's gallery;
`registry/pdp-dr-instruction.md`, *The section form*, carries the form and the law all six share.

The owner's rules for this mode, word for word:

```
- Product in a realistic lifestyle environment (product may be absent)
- Subtle visual effects/icons allowed
- No text
- Human allowed when relevant to lifestyle context
```

## PURPOSE
Show the life the product belongs to, as one realistic photograph: a lived-in place and, where it
helps, the person the page is written for, with the product at home in the frame or out of it. It
answers *"is this for a life like mine"*. It is the section type a block takes when its copy
argues none of the other five — no problem, no result, no process, no step and no single feature.

## TRIGGER
use_when: >
  An LP2 image outside the product card's gallery whose section argues where the
  product fits rather than what it does: a uses block listing places, people or
  occasions; a help or FAQ image; a support or brand block; any section whose copy
  names no problem, no result, no process, no step and no single feature. The product
  may be small in the frame or absent from it. Take 06-relief-after when the copy names
  what the product changes; 03-use-demo when it names an act; 05-persona-grid or
  06-relief-scene for a gallery tile, which this type never fills; and never a buyer
  tile, which is 05-social-snapshot's.

## SKELETON
The section form: one concise natural paragraph, no labels, in this order. Each arrow names an
entry in PARTS; the fixed sentences are the form's and are written word for word.

```
TYPE: 05-persona-lifestyle v0.2

  1. The picture: an editorial photograph, its angle and distance, the lived-in
     place, the time of day, and who is there doing what.           -> PARTS/scene
  2. The product BY NAME, at home in that place: where it sits and what it is
     doing there. Or the sentence that it is not in the frame.      -> PARTS/product
  3. The light: the form's light sentence.
  4. The words: the form's no-words sentence.

Where the product is in frame, the form's reference and closing sentences end the prompt.
Where it is absent, the prompt ends at step 4 and carries neither.
```

## PARTS

**`scene`** — one place from the section's own list, the one most buyers will recognise; a block
listing four places still gets one frame, and the session's notes name the place it chose. Found
rather than styled: the room's colours are its own, with nothing added to supply one (ADR-108). A
person appears where the life needs one, busy with their own thing and never posing; a pet only
where the product serves one.

**`product`** — named as the page names it, placed and never described (G2), in use or in its
real place, at the size its host gives it (ADR-106). It may be small, and it may be absent where
the block is about the buyer's situation rather than the object — a help image, a support block.
**Never the product set out on a surface for display**: the owner's feature-image instruction
rules that frame out, and with the product idle on a table this type turns into the packshot the
library does not make.

## SLOT CONSTRAINTS
- **One frame**, no panel, no inset and no collage of places: a block that must show several
  places at once is `03-use-grid`'s or `05-persona-grid`'s.
- **Words: none.** One subtle effect or icon is allowed, as the owner's rule says, only where the
  place needs it to be read — and never a word. *Untested.*
- **It counts as a place scene.** The gallery's limit of two does not reach a section image
  (`mapping/pdp-dr-rules.md`, rule 8 binds the gallery), and rule 13 still does: never the same
  place and message as another image on the page.
- **Any screen** shows only a picture, with no interface, text or numbers (G6).
- **G13 binds**, casting follows the namespace, and a block that names a person shows no face.
- **Length and ratio** are the form's: at most 1,200 characters, and no frame shape in the prompt.

## NEGATIVE
```
[G6] + the product set out on a surface for display, a collage of places, a split frame,
an inset, staged props, a bowl of fruit, a posed or exaggerated smile, an influencer pose,
a pale or drained grade, a warm yellow cast, shop signs or labelled packaging in the background
```

## BLOCK
**Criterion 3: the owner failed this type's first render.** Set `section-02` put it on the owner's
page v17, image 7, and the owner judged the set's eight renders *"các ảnh trên chất lượng vẫn còn
kém so với instruction"* — still poor next to the instruction's own results (ADR-111). The harness
had graded it pass before that; the observations are under KNOWN-FLAKY and none is written into the
skeleton yet. **The trial is `sets/section-03/`**: the same field, written by the owner's
instruction as it stands, with nothing the section form adds. Its result decides this skeleton.
`sets/section-01/` is unrendered and in 0.1's form.

**Criterion 1 cannot be met from the ledger as it stands**: no corpus record carries this id. The
type comes from the owner's tested instruction, so the count is the owner's to waive, as ADR-057
waived it for `03-spec-macro`.

**Criterion 2, run on paper in ADR-110**: of the four templates' fields this type takes
`uses.image`, a `faq` image and any block whose name and copy argue none of the other five. It
contests no gallery tile and no buyer tile. **It is the catch-all, which is the risk**: a router
that cannot decide lands here, so the trigger names the five it must rule out first, and a session
whose section images mostly land on this type re-reads its copy before it ships.

## KNOWN-FLAKY
Single observations, none yet a clause (SPEC §6.2); what the trial decides comes first.

- **Set `section-02`, image 7** (harness pass). A real kitchen in full colour, unposed, the phone
  showing a picture, and the cushion's outline reading against the wooden chair.

## CHANGELOG
- 0.2 (2026-09-18): first render — set `section-02`, the owner's page v17 — failed by the owner on
  quality against the instruction (ADR-111). No clause added: the harness's observations wait in
  KNOWN-FLAKY while `section-03` tests the instruction as written against this form.
- 0.1 (2026-09-18): drafted from the owner's image instruction, the OTHER mode, with the section
  form as its skeleton (ADR-110). New device `lifestyle`. No render.

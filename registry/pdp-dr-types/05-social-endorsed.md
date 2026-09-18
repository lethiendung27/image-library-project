---
id: 05-social-endorsed
step: 5
job: social
device: endorsed
version: "0.1"
status: reserved
replaced_by: null
channels: [landing-page]
requires_product_photo: true
generation_mode: single-pass
axes: {}
variants: []
exempt_from: [G3, G4]
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: "Criterion 3: no render, and the verdict SPEC 6.3 asks for is the owner's; set section-06 is its first. Criterion 1: no corpus record carries this id, because the type is written from the owner's decision of 2026-09-18 and the Endorsed form of the owner's gallery instruction rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-113."
---

# 05-social-endorsed — PDP-DR SECTION TYPE, DRAFT

**The expert block's image** (owner decision, 2026-09-18, ADR-113): *"Tile chuyên gia (Endorsed) có
hiện mặt, không có hạn chế nào"* — the expert image shows a face, with no restriction. It is the
seventh section type, for the images outside the product card's gallery, and the only one the
owner's image instruction does not name; `registry/pdp-dr-instruction.md`, *The section form*,
carries the form and the law every section type shares.

The construction is the **Endorsed** form of the owner's gallery instruction
(`~/Downloads/product-gallery-instruction.txt`), in its words:

```
An expert figure recommends the product — a persona the user supplies, or one the writer invents.
Rendered as a photograph: the person at eye level, the product in hand or in frame, neutral studio
or a clinic-neutral room, no props that imply a specific institution.
```

## PURPOSE
Give the expert a block quotes a face: one photograph of that person, at eye level, with the
product in hand or in frame. The block's HTML carries the name, the role and the quote; the
picture carries the person's standing, readable in three seconds.

## TRIGGER
use_when: >
  An LP2 image outside the product card's gallery in a block that quotes a named expert
  or professional beside a name and a role: an expert, a doctor, an installer, a
  specialist. The frame is that person, face shown, at eye level, with the product in
  hand or in frame. Take 03-use-demo when working hands carry the block and the person
  is not the argument; 03-mechanism-diagram when the quoted claim is a process to
  explain; never a buyer's photo, which is 05-social-snapshot's; never a gallery tile.

## SKELETON
The section form: one concise natural paragraph with no labels, in this order. Each arrow names an
entry below or in *The section form*; the lock's phrases are the session's, word for word.

```
TYPE: 05-social-endorsed v0.1
Image_Type: ENDORSED (the owner's decision of 2026-09-18; the image instruction names no such mode)

  1. The register and the camera: "Editorial realism portrait photo", eye level, chest
     up or waist up, the person turned slightly toward the lens.
  2. The person, by ROLE and never by the page's name, cast as the page's market,
     face shown, in the dress of that role.                          -> PARTS/person
  3. The product BY NAME, in the person's hand or in frame, whole and
     unobstructed, at the size the hand gives it.                    -> PARTS/product
  4. The place: a neutral studio or a plain workplace of that role.  -> PARTS/place
  5. The lock's lighting family and colour tone, and the instruction's tone.
  6. "No text."
  7. G1 in one sentence: "Use the attached product photo as the exact reference."
```

## PARTS

**`person`** — the expert the block names, written by ROLE, age range and casting: *a North American
dermatologist in her fifties*, never *Dr. Dan Friedmann*. A name in the prompt pulls a face toward
itself — the owner records an invented "Dr. L. Chen" rendering an Asian face, 1 of 1 — and ties a
generated face to the name the page prints. Cast positively as the page's market, North American
where the page names none. **The face is shown**: looking at the lens or at the product, with a
natural, assured expression, never a posed or exaggerated smile and never a thumbs-up. The dress
of the role is allowed — a white coat, an installer's work shirt — plain, with no name tag, badge or
logo. One person.

**`product`** — named as the page names it, placed and never described (G2), held the way the role
would hold it: an installer at a wall socket with the extender in hand, a dermatologist holding the
device at chest height. **Scale comes from the hand** (ADR-106). The product is whole and its
working face is toward the lens.

**`place`** — a neutral studio ground, or a plain workplace of the role: a treatment room, a
hallway being fitted. Nothing in it names an institution — no hospital, clinic, university,
company or agency, no logo, no uniform crest, and nothing framed on a wall. Its colours sit in the
set's palette (*The section form*, the lock in a section prompt).

## SLOT CONSTRAINTS
- **One frame, one person.** No panel, no inset, no second person.
- **Words: none.** The name, the role and the quote are the page's HTML, and so is the small avatar
  beside them.
- **The compliance flag** (ADR-089's form). Every prompt of this type ships with
  `compliance: { flag: "endorsed-expert", note }`. The note says that a generated face beside a
  named expert presents an endorsement; that where the named person does not exist, or does not
  hold the expertise shown, the page carries a fabricated endorsement, which the FTC's endorsement
  rules treat as deceptive; and that the real expert's own photograph always wins. The merchant
  decides. No LP2 session refuses.
- **Never a real, identifiable person.** The prompt never names or describes a real person, and a
  real expert is shown by their own photograph, which is the `author` row and out of library scope.
  This line and the institution line above are the owner's own, from the Endorsed rule of the
  gallery instruction; the rest of that rule's limits the owner lifted on 2026-09-18.
- **The avatar stays out of scope** (*Slot kinds*, `portrait`). The page reuses a crop of this image
  for it, so the block shows one face.
- **Real, never worn**, in the lock's lighting family and colour tone (*The section form*).
- **G13 binds**, and casting follows the namespace.
- **Ratio** never goes into the prompt (ADR-016); the owner renders the field at the frame its
  template shows (*The section form*, *The frame*).

## NEGATIVE
```
[G6] + a name tag, a badge, a logo or a crest on clothing or in the room, a framed certificate or
diploma, a real hospital, clinic, university or company, a second person, a posed or exaggerated
smile, a thumbs-up, the product set out on display with nobody holding it, the product small or
far off, a worn, scratched or faded surface
```

## BLOCK
**Criterion 3 has no render.** `sets/section-06/` is the first set; its image 6 is this type's, and
the verdict SPEC §6.3 asks for is the owner's.

**Criterion 1 cannot be met from the ledger as it stands.** No corpus record carries this id. The
nearest, `lp3-17millbrook-barrierbalm` — a practitioner beside a pregnant woman in a clinic, both
smiling at the lens and giving a thumbs-up — is filed under `05-social-testimony` and was read there
as not that type. The type comes
from the owner's decision, so the count is the owner's to waive, as ADR-057 waived it for
`03-spec-macro`.

**Criterion 2, run on paper in ADR-113.** Of the four templates' fields it takes the `expert` block's
section image: WiBoofy's `expert.scene` and Aure's `expert.photo`. It contests no gallery tile and no
buyer tile. Its neighbours are `05-social-testimony` (a buyer addressing the lens mid-sentence, a
video still, reserved and still blocked on G14's attribution test) and `05-social-handoff` (two
people, one recommending to the other).

## CHANGELOG
- 0.1 (2026-09-18): drafted on the owner's decision that the expert image shows a face with no
  restriction, from the Endorsed form of the owner's gallery instruction, in the section form
  (ADR-113). New device `endorsed`. No render.

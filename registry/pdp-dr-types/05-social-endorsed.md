---
id: 05-social-endorsed
step: 5
job: social
device: endorsed
version: "0.3"
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
blocked_by: "Criterion 3: the owner failed all three renders of set 05-social-endorsed-01 on 2026-09-20 — the expert held the product up and nothing was being used (ADR-114); 0.2 has no render, and the verdict SPEC 6.3 asks for is the owner's. Criterion 1: no corpus record carries this id, because the type is written from the owner's decision of 2026-09-18 and the Endorsed form of the owner's gallery instruction rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-113."
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
Give the block's expert a face by showing that expert AT WORK: one photograph of the trade the
page's constraint belongs to, doing the job with the product, mid-task. The block's HTML carries the
name, the role and the quote; the picture carries the standing, and the standing comes from the work
(*The section form*, *The person in frame*).

## TRIGGER
use_when: >
  An LP2 image outside the product card's gallery whose block speaks as an expert: an
  expert view, a doctor, an installer, a specialist, named or unnamed. The frame is the
  trade the page's constraint belongs to, at work with the product, face shown. Take
  03-use-demo when the block is an act of the buyer's own hands and no trade is claimed;
  03-mechanism-diagram when the quoted claim is a process to explain; never a buyer's
  photo, which is 05-social-snapshot's; never a gallery tile.

## SKELETON
The section form: one concise natural paragraph with no labels, in this order. Each arrow names an
entry below or in *The section form*; the lock's phrases are the session's, word for word.

```
TYPE: 05-social-endorsed v0.3
Image_Type: ENDORSED (the owner's decision of 2026-09-18; the image instruction names no such mode)

  1. The register and the camera: "Editorial realism photo", the working distance and
     angle, close enough that the hands and the work read together.
  2. The person, by ROLE and never by the page's name, cast as the page's market,
     face shown, in the NAMED garments of that trade.                -> PARTS/person
  3. The work, in a sentence of its own: the product BY NAME doing its own thing on a
     real surface, mid-task, what the work needs, and the kit the
     trade arrived with.                                             -> PARTS/work
  4. The mark the work has left, and the place it happens in.        -> PARTS/place
  5. The lock's lighting family and colour tone, and the instruction's tone.
  6. "No text."
  7. G1 in one sentence: "Use the attached product photo as the exact reference."
```

## PARTS

**`person`** — **the trade the page's constraint belongs to**, derived by the three tests in *The
person in frame* and written by ROLE, age range and casting: *a North American mobile car detailer in
her forties*, never *Dr. Dan Friedmann*. A name in the prompt pulls a face toward itself — the owner
records an invented "Dr. L. Chen" rendering an Asian face, 1 of 1 — and ties a generated face to the
name the page prints. Cast positively as the page's market, North American where the page names none.
**The face is shown**, and it is a working face, **the eyes on the work**: the half-turn toward the lens
that 0.2 allowed came back as a full face and a smile, 1 of 1, so it is retired. **Name the garments,
never the category** — *a work shirt* rendered as a button-up dress shirt over clean chinos twice in
three, and the frame read as a resident; *grey work coveralls, work trousers with knee pockets and work
boots* rendered as a trade, 1 of 1. Where the product moves water, name what keeps it off: coveralls or
a waterproof apron, rubber boots, wet forearms, a kneeling pad on wet ground. Plain, with no name tag,
badge or logo. One person.

**`work`** — the sentence the type turns on. **The product is doing its own thing on a real surface**,
in the practised grip and at the distance the trade uses: water leaving the nozzle onto the paint, the
plug going into the socket. Named as the page names it and never described (G2); **scale comes from
the hand** (ADR-106). **What the work needs is in frame** — the bucket the intake hose draws from, the
socket, the bench — because on a page that sells freedom from a precondition, that precondition is the
argument. The owner failed 3 of 3 renders that held the product up with none of this, 2026-09-20.
**And the kit the trade arrived with**, which is what makes the trade legible: the van or pickup with its
tailgate open, the second bucket, the stack of folded towels. Round 2 named the trade in words and showed
no kit, and the owner's answer was *"tôi chưa thấy thợ rửa xe lưu động"*, 2 of 3.

**`place`** — where that trade really does this job, and **the mark the work has left**: the wet panel
behind the spray, the clean strip beside the dirty one, the water on the ground. **The dirt is a film and
the clean band is the proof**: round 2 returned one car caked in dried mud, which strains *real, never
worn*, and one already spotless, which left the water nothing to remove. Nothing in it names an
institution — no hospital, clinic, university, company or agency, no logo, no uniform crest, nothing
framed on a wall — and nothing carries signage (ADR-109). Its colours sit in the set's palette (*The
section form*). **A studio ground is refused for a trade that works outdoors**; it stays legal only
where the trade itself works in one.

## SLOT CONSTRAINTS
- **One frame, one person, one task.** No panel, no inset, no second person.
- **Never a presentation.** The product is never raised to the lens or held at chest height for the
  camera, the clothes and the surfaces are never dry where the product moves water, and no prop is
  set out as decoration (*The person in frame*). The eyes never leave the work.
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
smile, a thumbs-up, the product raised to the lens or held at chest height, a person standing square
to the camera with nothing happening, a face turned to the lens, a studio ground for a trade that works
outdoors, dry clothes and a dry surface where the product moves water, a button-up dress shirt and clean
chinos on a job that moves water, a trade with none of its kit in frame, props set out as decoration, the
product set out on display with nobody using it, the product small or far off, caked mud or an already
spotless surface where the work is cleaning, a worn, scratched or faded surface
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
- 0.3 (2026-09-20): **round 2 rendered, and the work landed where the person did not** —
  3 of 3 showed water leaving the tool onto a real surface and the intake hose in a filled bucket, which
  round 1 had none of. The owner: *"tôi chưa thấy thợ rửa xe lưu động, cư dân trang phục không phù hợp
  cho rửa xe"*. Name the garments rather than the category, bring the trade's kit into frame, keep the
  eyes on the work, and let the dirt be a film with a clean band behind the spray (ADR-115).
- 0.2 (2026-09-20): **the owner failed all three renders of `sets/05-social-endorsed-01/`** — each
  held the product up in clean clothes with nothing in use, and each held a brass hose nozzle rather
  than the attached product, 3 of 3. The type turns on the WORK: the person is the trade the page's
  constraint belongs to, derived by the three tests; the product is doing its own thing on a real
  surface; what the work needs and the mark it has left are in frame; a presentation is refused
  (ADR-114).
- 0.1 (2026-09-18): drafted on the owner's decision that the expert image shows a face with no
  restriction, from the Endorsed form of the owner's gallery instruction, in the section form
  (ADR-113). New device `endorsed`. No render.

---
id: 05-social-endorsed
step: 5
job: social
device: endorsed
version: "1.3"
status: active
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
blocked_by: null
---

# 05-social-endorsed — PDP-DR SECTION TYPE

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
TYPE: 05-social-endorsed v1.3
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
the hand** (ADR-106). **What the work needs is in frame**, as the product PHYSICALLY needs it — the hose back to
the tap, the socket, the bench (ADR-120) — because on a page that sells freedom from a precondition, that precondition is the
argument. The owner failed 3 of 3 renders that held the product up with none of this, 2026-09-20.
**And the kit the trade arrived with**, which is what makes the trade legible: the van or pickup with its
tailgate open, the second bucket, the stack of folded towels. Round 2 named the trade in words and showed
no kit, and the owner's answer was *"tôi chưa thấy thợ rửa xe lưu động"*, 2 of 3.

**`place`** — where that trade really does this job, **at a place the page names** (ADR-119), and
**the mark the work has left**: the wet panel
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
to the camera with nothing happening, a face turned to the lens, a place the page never names,
water sprayed over a high-rise railing, a studio ground for a trade that works
outdoors, dry clothes and a dry surface where the product moves water, a button-up dress shirt and clean
chinos on a job that moves water, a trade with none of its kit in frame, props set out as decoration, the
product set out on display with nobody using it, the product small or far off, caked mud or an already
spotless surface where the work is cleaning, a worn, scratched or faded surface
```

## WORKED EXAMPLES

### example: car-wash-detailer-wheel — skeleton@1.1, run: pass

`pdp-dr-multifunctional-car-wash-tool-v01` · `expert.scene` · TPL-PDP06 · 4:3 · one attachment ·
`sets/05-social-endorsed-01` round 3, prompt 2 · `sha256:b062af9c…` · 2026-09-21

```
Editorial realism photo from low at the front wheel, close enough that his hands and the spray read together: a North American mobile car detailer in his fifties, in grey work coveralls with the sleeves pushed up and the forearms wet, rubber boots on the wet ground, no logo, badge or name tag, crouches at the front wheel arch of a customer's car on an apartment forecourt. He is mid-rinse: the Cordless Car Wash Tool in his practised grip drives water into the wheel arch, and its intake hose runs down into a filled bucket beside the wheel, the only hose in the frame. A kneeling pad is under one knee, and his work van stands behind him with its tailgate up, a second bucket and a stack of folded microfibre towels on it. The wheel wears an even film of road dust, grime and water sheet off the rim onto the wet ground, and the rim behind the spray is bright where he has already passed. His eyes are on the spray. Crisp daylight with a soft directional key, true colour with neutral whites, in a palette of clean white, deep slate grey and a fresh mid-blue, balanced contrast, readable in three seconds. It is a real photograph with true texture and a soft cast shadow, and nothing in the frame is old, worn, scratched or faded. No text. Use the attached product photo as the exact reference.
```

**Why it is kept in full**: an example that rendered is the only record of what was sent (SPEC
§3.3). Every clause the type owns landed — the named garments, the rubber boots and the kneeling
pad, the van with its tailgate up and a second bucket on it, the intake hose in the bucket the
water comes from, brake grime on the rim with clean metal where the spray has passed, and the
eyes down on the wheel. The low camera did not cut the kit out of frame, which was this frame's
predicted risk. **And the product is the attached one**: the reference photo was opened on
2026-09-21 and the tool IS a black pistol-grip spray gun with a brass nozzle collar and a brass
hose fitting at the foot of the grip, which is what the render holds. Nothing is left against this
frame, so it is a `pass` (ADR-117). **Its lock sentence is not to be copied**: *clean white, deep
slate grey and a fresh mid-blue* is the palette ADR-119 retired for this page, after six grey
frames; the example keeps it because it is what rendered. The page's current lock is the one in
`sets/05-persona-lifestyle-01`. **And its water supply is wrong** (ADR-120): the tool screws onto a
garden hose and needs a tap, so the intake hose in a bucket is the page's fiction, not the product.

## KNOWN-FLAKY

- **WITHDRAWN, 2026-09-21: there was never a product failure here.** This entry said the attached
  product did not reach the render, 9 of 9. It was wrong, and the fault was the harness's: the
  product was graded against its NAME — `Cordless Car Wash Tool` — and never against its
  photograph. The owner confirmed the photo was attached every time; it was then downloaded from the
  page's own gallery URL and opened, `sha256:ff37a23b…`, the hash this set declares. **The product
  IS a black pistol-grip spray gun with a brass nozzle collar, a trigger, a brass hose fitting at
  the foot of the grip and yellow and orange hose connectors beside it** — which is exactly what
  every render held. Nine renders were marked down for resembling the thing they were given
  (ADR-117). **Grade a product against its reference photo, never against its name.**
- **The *only hose in the frame* clause is WITHDRAWN too** (ADR-120). ADR-117 kept it on the page's
  claim, *"Wash Vehicles Anywhere Without Garden Hoses"* — but the claim is false. The owner: *"sản
  phẩm này phải nối với vòi nước để vận hành"*; the reference photo lays out a tap adapter and
  garden-hose connectors beside the gun. The tool screws onto a garden hose. Every frame of this
  set drew it fed from a bucket, as the copy said, and every one of them shows a capability the
  product does not have. What the work needs is the hose back to the tap.
- **The mark of work reads wet-versus-dry rather than dusty-versus-clean, 2 of 3** on painted
  bodywork and balcony tiles, and clearly only on the wheel, where brake grime gives the water
  something to take off. One more set decides whether the film clause needs a harder noun.

## CHANGELOG
- 1.3 (2026-09-21): what the work needs is what the product physically needs, never what
  the copy says; the worked example's bucket feed is marked wrong (ADR-120).
- 1.2 (2026-09-21): the place is one the page names; round 3's balcony railing was named
  by none of the page's fields, and a railing over a drop is where nobody rinses (ADR-119).
- 1.1 (2026-09-21): **a correction, not a change of law.** The reference photo was opened for the
  first time and the nine renders marked down for the wrong product were carrying the right one;
  the worked example is a `pass`, the KNOWN-FLAKY entry is withdrawn, and the *only hose* clause
  keeps its place on the page's own claim rather than on a phantom failure. ADR-117.
- 1.0 (2026-09-21): **promoted to active, in place, on the owner's verdict** — *"pass expert
  type cho pdp-dr"*. Round 3 landed every clause the type owns, 3 of 3. §6.3(3) is the owner's
  and given; §6.3(1) is waived as ADR-057 waived it for `03-spec-macro`; §6.3(2) ran on paper
  in ADR-113. The expert block's section image now routes. ADR-116, `80e5bb4`.
- 0.3 (2026-09-20): **round 2 rendered, and the work landed where the person did not** —
  3 of 3 showed water leaving the tool onto a real surface and the intake hose in a filled bucket, which
  round 1 had none of. The owner: *"tôi chưa thấy thợ rửa xe lưu động, cư dân trang phục không phù hợp
  cho rửa xe"*. Name the garments rather than the category, bring the trade's kit into frame, keep the
  eyes on the work, and let the dirt be a film with a clean band behind the spray (ADR-115).
- 0.2 (2026-09-20): **the owner failed all three renders of `sets/05-social-endorsed-01/`** — each
  held the product up in clean clothes with nothing in use, 3 of 3. [A wrong-product clause in this
  entry is WITHDRAWN by ADR-117: the renders carried the attached product.] The type turns on the WORK: the person is the trade the page's
  constraint belongs to, derived by the three tests; the product is doing its own thing on a real
  surface; what the work needs and the mark it has left are in frame; a presentation is refused
  (ADR-114).
- 0.1 (2026-09-18): drafted on the owner's decision that the expert image shows a face with no
  restriction, from the Endorsed form of the owner's gallery instruction, in the section form
  (ADR-113). New device `endorsed`. No render.

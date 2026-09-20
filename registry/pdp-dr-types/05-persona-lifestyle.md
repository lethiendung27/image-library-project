---
id: 05-persona-lifestyle
step: 5
job: persona
device: lifestyle
version: "0.6"
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
blocked_by: "Criterion 3: two rounds on the owner's page v17 — section-02 failed by the owner on quality, section-03 (the instruction as it stands) graded by the harness after the owner's word on the size of its words and marks (ADR-112); 0.4 adds the owner's design rules (ADR-113) and has no render; no set carries it yet, and the verdict SPEC 6.3 asks for is the owner's. Criterion 1: no corpus record carries this id, because the type is written from the owner's image instruction of 2026-09-18 rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-110."
---

# 05-persona-lifestyle — PDP-DR SECTION TYPE, DRAFT

**The OTHER mode of the owner's image instruction** (`~/Downloads/images prompt.txt`, 2026-09-18,
ADR-110). One of the seven section types, for the images outside the product card's gallery;
`registry/pdp-dr-instruction.md`, *The section form*, carries the form and the law they all share.

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
The section form since ADR-112: the owner's image instruction as it stands. Its Image_Type is this
type's mode and its Description the field's own page values; the prompt is one concise natural
paragraph with no labels, in this order. Each arrow names an entry below or in *The section form*.

```
TYPE: 05-persona-lifestyle v0.6
Image_Type: OTHER

  1. The register and the camera: "Editorial realism lifestyle photo".
  2. The lived-in place, and who is there doing what.                -> PARTS/scene
  3. The product BY NAME, at home in that place, on a seat of a clearly
     different tone where it is sat on — or absent.                  -> PARTS/product
  4. The lock's lighting family and colour tone, and the instruction's tone.
  5. "No text."

Where the product is in frame, G1's one sentence ends the prompt:
"Use the attached product photo as the exact reference." Where it is absent, nothing follows.
```

## PARTS

**`scene`** — one place from the section's own list, the one most buyers will recognise; a block
listing four places still gets one frame, and the session's notes name the place it chose. Found
rather than styled: the room's colours are its own, with nothing added to supply one (ADR-108). **A person here is the
derived USER** — the one the page's constraint belongs to (*The person in frame*) — in their own
place, busy with their own thing and never posing; their clothes are named pieces they own and could get wet in, never a category (*The person in frame*); where the product is in their hands it is working; a pet only
where the product serves one. **The point where the product meets the person stays in view**
(owner, ADR-113): a person at rest with it is relaxed and looks away; a person using it looks at
the point of use.

**`product`** — named as the page names it, placed and never described (G2), in use or in its real
place, at the size its host gives it (ADR-106). It may be small, and it may be absent where the
block is about the buyer's situation rather than the object — a help image, a support block. **Never
the product set out on a surface for display**: the owner's feature-image instruction rules that
frame out, and with the product idle on a table this type turns into the packshot the library does
not make. **A seated product sits on a seat of a clearly different tone**, asked as a relation,
never as a colour: arm B of ADR-111 left the sentence out and 2 of its 3 seated frames put the
cushion on a black seat of its own tone, where arm A carried it 4 of 4 (ADR-112).

## SLOT CONSTRAINTS
- **One frame**, no panel, no inset and no collage of places: a block that must show several
  places at once is `03-use-grid`'s or `05-persona-grid`'s.
- **Words: none.** One subtle effect or icon is allowed, as the owner's rule says, only where the
  place needs it to be read — and never a word. An icon is drawn in the lock's icon style
  (ADR-113). *Untested.*
- **It counts as a place scene.** The gallery's limit of two does not reach a section image
  (`mapping/pdp-dr-rules.md`, rule 8 binds the gallery), and rule 13 still does: never the same
  place and message as another image on the page.
- **Any screen** shows only a picture, with no interface, text or numbers (G6).
- **Real, never worn** (*The owner's design rules*, ADR-113): nothing in the frame is old, worn,
  scratched, stained or faded.
- **G13 binds**, and casting follows the namespace.
- **Ratio** never goes into the prompt (ADR-016); the owner renders the field at the frame its
  template shows (*The section form*, *The frame*).

## NEGATIVE
```
[G6] + the product set out on a surface for display, a collage of places, a split frame,
an inset, staged props, a bowl of fruit, a posed or exaggerated smile, an influencer pose,
a pale or drained grade, a warm yellow cast, shop signs or labelled packaging in the background,
the point where the product meets the person hidden, a worn, scratched, stained or faded surface
```

## BLOCK
**Criterion 3: two rounds, and 0.3 is what they left.** Set `section-02` wrote the owner's page v17
in 0.1's form, and the owner failed it on quality against the instruction (ADR-111). Set
`section-03` wrote the same fields by the instruction as it stands, image 7 here, and the owner's
word narrowed to the size of the drawn words and marks; the harness graded it pass (ADR-112). 0.3 is
the instruction as it stands plus what the two rounds earned. It has no render: `sets/section-04/`
was written for it. **0.4 adds the owner's design rules of 2026-09-18** (ADR-113), and no set
carries 0.4 yet; the verdict SPEC §6.3 asks for is the owner's.

**Criterion 1 cannot be met from the ledger as it stands**: no corpus record carries this id. The
type comes from the owner's tested instruction, so the count is the owner's to waive, as ADR-057
waived it for `03-spec-macro`.

**Criterion 2, run on paper in ADR-110**: of the four templates' fields this type takes
`uses.image`, a `faq` image and any block whose name and copy argue none of the other five. It
contests no gallery tile and no buyer tile. **It is the catch-all, which is the risk**: a router
that cannot decide lands here, so the trigger names the five it must rule out first, and a session
whose section images mostly land on this type re-reads its copy before it ships.

## KNOWN-FLAKY
Single observations; what recurred across both rounds is written into 0.3, and the rest waits here.

- **Set `section-02`, image 7** (harness pass). A real kitchen in full colour, unposed, the phone
  showing a picture, and the cushion's outline reading against the wooden chair.

- **Set `section-03`, image 7** (harness pass). A bright kitchen, the cushion's ribbed back as the
  reference has it, on a wooden chair of another tone. A beige sweater in a white kitchen; the
  frame's colourfulness 32.0 sits inside the owner's band.

## CHANGELOG
- 0.6 (2026-09-20): a person's clothes are named pieces they could get wet in, never a category:
  *a work shirt* rendered as a button-up dress shirt 2 of 3 in `sets/05-social-endorsed-01` round 2
  (ADR-115).
- 0.5 (2026-09-20): a person in frame is the derived user, and a product in their hands is working
  (ADR-114).
- 0.4 (2026-09-18): the owner's design rules (ADR-113) — the lock's lighting family and colour
  tone, an icon in its icon style, real and never worn, and the point where the product meets
  the person kept in view. The no-face clause left with the expert block's new type. No set
  carries 0.4 yet.
- 0.3 (2026-09-18): the skeleton is the owner's image instruction as it stands, arm B of ADR-111,
  with G1 in one sentence (ADR-112). The two rounds' earned clauses are written in.
- 0.2 (2026-09-18): first render — set `section-02`, the owner's page v17 — failed by the owner on
  quality against the instruction (ADR-111). No clause added: the harness's observations wait in
  KNOWN-FLAKY while `section-03` tests the instruction as written against this form.
- 0.1 (2026-09-18): drafted from the owner's image instruction, the OTHER mode, with the section
  form as its skeleton (ADR-110). New device `lifestyle`. No render.

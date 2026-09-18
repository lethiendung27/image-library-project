---
id: 01-pain-before
step: 1
job: pain
device: before
version: "0.3"
status: reserved
replaced_by: null
channels: [landing-page]
requires_product_photo: false
generation_mode: single-pass
axes:
  register: [commercial, ugc]
variants: []
exempt_from: [G3, G4, G11]
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: "Criterion 3: two rounds on the owner's page v17 — section-02 failed by the owner on quality, section-03 (the instruction as it stands) graded by the harness after the owner's word on the size of its words and marks (ADR-112); 0.3 has no render, set section-04 is its first, and the verdict SPEC 6.3 asks for is the owner's. Criterion 1: no corpus record carries this id, because the type is written from the owner's image instruction of 2026-09-18 rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-110."
---

# 01-pain-before — PDP-DR SECTION TYPE, DRAFT

**The WITHOUT / BEFORE mode of the owner's image instruction** (`~/Downloads/images prompt.txt`,
2026-09-18, ADR-110). One of six section types, for the images outside the product card's gallery;
`registry/pdp-dr-instruction.md`, *The section form*, carries the form and the law all six share.

The owner's rules for this mode, word for word:

```
- Show the problem clearly in a realistic environment
- Product is absent or shown in a non-functioning state
- No solution cues
- Human faces allowed when relevant to the scene
- No text
```

## PURPOSE
Show the problem a section's line names, as one realistic photograph taken before the product
arrives. The product is absent, or in frame and plainly not working, and nothing in the frame
hints at the fix. The image sits beside its own HTML copy, which carries the argument; the
picture makes that one line visible in three seconds.

## TRIGGER
use_when: >
  An LP2 image outside the product card's gallery whose section states a problem: a
  problem block, or one item of it; the before field of a before-and-after pair; any
  section line naming what goes wrong without the product. The problem is a state a
  camera can catch: a thing failing, a body straining, a place not working, the old way
  letting someone down. Take 06-relief-after when the line names what the product
  changes; 03-spec-overlay when the problem can only be drawn and the product is in
  frame; 02-symptom-rail or 01-pain-split for a gallery tile, which this type never
  fills.

## SKELETON
The section form since ADR-112: the owner's image instruction as it stands. Its Image_Type is this
type's mode and its Description the field's own page values; the prompt is one concise natural
paragraph with no labels, in this order. Each arrow names an entry below or in *The section form*.

```
TYPE: 01-pain-before v0.3 [register: commercial | ugc]
Image_Type: WITHOUT / BEFORE

  1. The register and the camera: "Editorial realism photo", the angle and distance.
  2. The ordinary place the problem is noticed in, and who is there.  -> PARTS/scene
  3. The problem as a physical fact; the old way's failure as a
     DISPLACED object, the one thing the eye lands on.               -> PARTS/problem
  4. The product: absent, or in frame and plainly not working.       -> PARTS/product
  5. "No solution cues", the light, and the instruction's tone:
     "... light, balanced contrast, readable in three seconds."
  6. "No text."

Where the idle product is in frame, G1's one sentence ends the prompt:
"Use the attached product photo as the exact reference." Where it is absent, nothing follows.
```

## PARTS

**`scene`** — the place the section's copy puts the problem in, and nowhere grander: the back
room, the kitchen counter, the office chair. One person at most unless the copy names more. A face
is allowed where it is relevant and it never performs for the lens: the body and the object carry
the problem (G9), and the expression is only what that moment would really bring.

**`problem`** — the symptom as a thing in the frame, written as itself and never as a comparison.
**The old way's failure is a DISPLACED object**, somewhere it plainly is not in use — the lumbar
pillow fallen on the floor beside the chair, the pad pushed half off the seat — never a small
change of state. *Slipped down onto the seat* came back with the pillow upright in its corner in
both rounds, 2 of 2, which is `01-pain-scene`'s rule (*its residue is a displaced object*) now
evidenced here; *hips sunk below his knees*, a comparison, did not render either, 2 of 2. Where
the copy names the OLD WAY — the razor, the
plastic bag, the flat pad — that object may be the subject, generic and unbranded (SPEC §6.4). One
problem to a frame: a block of three items is three frames, each on its own item's line.

**`product`** — absent by default. *Not working* means a real state the object has: unplugged,
switched off, still boxed, set aside out of reach. Never broken, cracked or dirty: on a product
page a damaged product reads as the product's fault (ADR-109's finding about cut possessions,
borrowed). It is named as the page names it and never described (G2).

## SLOT CONSTRAINTS
- **One frame.** No panel, no inset, no split and no second state; the after is another file.
- **No solution cue**: no product glow, no arrow, no tick or cross, no brighter corner.
- **Words: none**, and no drawn layer beyond one subtle effect the problem needs, which the
  owner's instruction allows every mode — a faint fading signal, a draught of cold air. Where a
  screen shows the problem it carries a picture or one plain symbol, never interface text or
  numbers (G6). *Untested.*
- **On a pair's before field** the prompt is written from the pair's one locked description
  (`registry/pdp-dr-instruction.md`, *A pair shares one description*) and differs from its after
  in the state line alone. The grade is the same in both files, which is why G11 is declared out:
  the state changes, the light does not.
- **`register: ugc`** only in a block of buyers' own photos — `testimonials` today — in
  `05-social-snapshot`'s register, and the prompt ships with G14's flag and note (ADR-089).
- **G13 binds**, casting follows the namespace, and a block that names a person shows no face.
- **Ratio** never goes into the prompt (ADR-016); the owner renders the field at the frame its
  template shows (*The section form*, *The frame*).

## NEGATIVE
```
[G6] + the product working, a solution cue of any kind, an arrow, a tick or a cross,
a split frame, an inset, a second panel, a staged or theatrical expression, a posed smile,
a broken, cracked or dirty product, a rival brand's mark or packaging,
shop signs or labelled packaging in the background
```

## BLOCK
**Criterion 3: two rounds, and 0.3 is what they left.** Set `section-02` wrote the owner's page v17
in 0.1's form, and the owner failed it on quality against the instruction (ADR-111). Set
`section-03` wrote the same fields by the instruction as it stands, image 1 here, and the owner's
word narrowed to the size of the drawn words and marks; the harness graded it partial (ADR-112). 0.3
is the instruction as it stands plus what the two rounds earned. It has no render:
`sets/section-04/` is its first, and the verdict SPEC §6.3 asks for is the owner's.

**Criterion 1 cannot be met from the ledger as it stands**: the PDP corpus is gallery tiles, and
this type fills section fields. The type comes from the owner's tested instruction, so the count
is the owner's to waive, as ADR-057 waived it for `03-spec-macro`.

**Criterion 2, run on paper in ADR-110**: of the four templates' section, pair and closing
fields, this type takes `problem.*` and every `*before_image`, and it contests no gallery tile —
its trigger refuses one. Its live neighbour is `01-pain-scene`, LP1's cinematic pain frame, whose
trigger names cold traffic and an advertorial header and no LP2 section.

## KNOWN-FLAKY
Single observations; what recurred across both rounds is written into 0.3, and the rest waits here.

- **Set `section-02`, image 1** (the control, predicted pass; harness partial). The old way came
  back working: the separate lumbar pillow stood upright in the seat-back corner, filling the gap
  the prompt said was empty, and the pad was flat but ordinary. What was left to carry the problem
  was a hand on the lower back and a grimace, G9's weakest rank — though the owner's own *Stop the
  slump* tile uses that same gesture for its wrong state. The prompt wrote the failure as a small
  change of state (*slipped down*, *flattened*), where `01-pain-scene` records that a failure renders
  as a displaced object; and *hips sunk below his knees*, a comparison, did not render, 1 of 1.

- **Set `section-03`, image 1** (the instruction as it stands; harness partial). A cleaner
  photograph than arm A's, and the same fault: the lumbar pillow came back upright in its corner
  though the prompt had it *slipped down onto the seat*, 2 of 2 across both arms — the clause
  0.3's PARTS/problem now carries.

## CHANGELOG
- 0.3 (2026-09-18): the skeleton is the owner's image instruction as it stands, arm B of ADR-111,
  with G1 in one sentence (ADR-112). The two rounds' earned clauses are written in.
- 0.2 (2026-09-18): first render — set `section-02`, the owner's page v17 — failed by the owner on
  quality against the instruction (ADR-111). No clause added: the harness's observations wait in
  KNOWN-FLAKY while `section-03` tests the instruction as written against this form.
- 0.1 (2026-09-18): drafted from the owner's image instruction, the WITHOUT / BEFORE mode, with
  the section form as its skeleton (ADR-110). New device `before`. No render.

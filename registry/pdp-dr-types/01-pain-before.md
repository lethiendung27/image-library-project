---
id: 01-pain-before
step: 1
job: pain
device: before
version: "0.2"
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
blocked_by: "Criterion 3: the owner failed this type's first render, set section-02, on quality against the instruction (ADR-111); set section-03, the same fields written by the instruction as it stands, is the trial that decides the skeleton, and the verdict SPEC 6.3 asks for is the owner's. Criterion 1: no corpus record carries this id, because the type is written from the owner's image instruction of 2026-09-18 rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-110."
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
The section form: one concise natural paragraph, no labels, in this order. Each arrow names an
entry in PARTS; the fixed sentences are the form's and are written word for word.

```
TYPE: 01-pain-before v0.2 [register: commercial | ugc]

  1. The picture: an editorial photograph, its angle and distance, the ordinary
     place the problem is noticed in, and who or what is in it.      -> PARTS/scene
  2. The problem as a physical fact: the one thing the eye lands on. -> PARTS/problem
  3. The product: absent, or in frame and plainly not working.       -> PARTS/product
  4. The light: the form's light sentence.
  5. The words: the form's no-words sentence.

Where the idle product is in frame, the form's reference and closing sentences end the
prompt. Where it is absent, the prompt ends at step 5 and carries neither.
```

## PARTS

**`scene`** — the place the section's copy puts the problem in, and nowhere grander: the back
room, the kitchen counter, the office chair. One person at most unless the copy names more. A face
is allowed where it is relevant and it never performs for the lens: the body and the object carry
the problem (G9), and the expression is only what that moment would really bring.

**`problem`** — the symptom as a thing in the frame, written as itself and never as a comparison.
*Borrowed from `01-pain-scene`, where a symptom written as a difference came back as an ordinary
body both times LP1 tried it; untested here.* Where the copy names the OLD WAY — the razor, the
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
- **Length and ratio** are the form's: at most 1,200 characters, and no frame shape in the prompt.

## NEGATIVE
```
[G6] + the product working, a solution cue of any kind, an arrow, a tick or a cross,
a split frame, an inset, a second panel, a staged or theatrical expression, a posed smile,
a broken, cracked or dirty product, a rival brand's mark or packaging,
shop signs or labelled packaging in the background
```

## BLOCK
**Criterion 3: the owner failed this type's first render.** Set `section-02` put it on the owner's
page v17, image 1, and the owner judged the set's eight renders *"các ảnh trên chất lượng vẫn còn
kém so với instruction"* — still poor next to the instruction's own results (ADR-111). The harness
had graded it partial (the control, predicted pass) before that; the observations are under
KNOWN-FLAKY and none is written into the skeleton yet. **The trial is `sets/section-03/`**: the same
field, written by the owner's instruction as it stands, with nothing the section form adds. Its
result decides this skeleton. `sets/section-01/` is unrendered and in 0.1's form.

**Criterion 1 cannot be met from the ledger as it stands**: the PDP corpus is gallery tiles, and
this type fills section fields. The type comes from the owner's tested instruction, so the count
is the owner's to waive, as ADR-057 waived it for `03-spec-macro`.

**Criterion 2, run on paper in ADR-110**: of the four templates' section, pair and closing
fields, this type takes `problem.*` and every `*before_image`, and it contests no gallery tile —
its trigger refuses one. Its live neighbour is `01-pain-scene`, LP1's cinematic pain frame, whose
trigger names cold traffic and an advertorial header and no LP2 section.

## KNOWN-FLAKY
Single observations, none yet a clause (SPEC §6.2); what the trial decides comes first.

- **Set `section-02`, image 1** (the control, predicted pass; harness partial). The old way came
  back working: the separate lumbar pillow stood upright in the seat-back corner, filling the gap
  the prompt said was empty, and the pad was flat but ordinary. What was left to carry the problem
  was a hand on the lower back and a grimace, G9's weakest rank — though the owner's own *Stop the
  slump* tile uses that same gesture for its wrong state. The prompt wrote the failure as a small
  change of state (*slipped down*, *flattened*), where `01-pain-scene` records that a failure renders
  as a displaced object; and *hips sunk below his knees*, a comparison, did not render, 1 of 1.

## CHANGELOG
- 0.2 (2026-09-18): first render — set `section-02`, the owner's page v17 — failed by the owner on
  quality against the instruction (ADR-111). No clause added: the harness's observations wait in
  KNOWN-FLAKY while `section-03` tests the instruction as written against this form.
- 0.1 (2026-09-18): drafted from the owner's image instruction, the WITHOUT / BEFORE mode, with
  the section form as its skeleton (ADR-110). New device `before`. No render.

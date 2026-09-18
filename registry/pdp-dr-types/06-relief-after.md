---
id: 06-relief-after
step: 6
job: relief
device: after
version: "0.2"
status: reserved
replaced_by: null
channels: [landing-page]
requires_product_photo: true
generation_mode: single-pass
axes:
  register: [commercial, ugc]
variants: []
exempt_from: [G3, G4]
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: "Criterion 3: the owner failed this type's first render, set section-02, on quality against the instruction (ADR-111); set section-03, the same fields written by the instruction as it stands, is the trial that decides the skeleton, and the verdict SPEC 6.3 asks for is the owner's. Criterion 1: no corpus record carries this id, because the type is written from the owner's image instruction of 2026-09-18 rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-110."
---

# 06-relief-after — PDP-DR SECTION TYPE, DRAFT

**The WITH / AFTER mode of the owner's image instruction** (`~/Downloads/images prompt.txt`,
2026-09-18, ADR-110). One of six section types, for the images outside the product card's gallery;
`registry/pdp-dr-instruction.md`, *The section form*, carries the form and the law all six share.

The owner's rules for this mode, word for word:

```
- Product visible, functioning, solving the problem
- Clear visual cues of improvement or comfort
- Human faces allowed when relevant to the scene
- No text
```

## PURPOSE
Show the section's promise kept, as one realistic photograph: the product in frame and working,
and the improvement readable on the person, the object or the place it serves. The image sits
beside its own HTML copy, which carries the argument; the picture makes that one line visible in
three seconds.

## TRIGGER
use_when: >
  An LP2 image outside the product card's gallery whose section names what the product
  changes: a why-choose or benefits block, the after field of a before-and-after pair, a
  feature item whose line is a benefit state rather than a part, a closing image where
  the block argues what the packshot does not. The improvement is a state a camera can
  catch. Take 03-spec-overlay when the result cannot be seen and has to be drawn;
  03-use-demo when the line is an act of the buyer's own hands; and take
  05-persona-lifestyle when the section sells the life around the product rather than
  the problem solved; 06-relief-hero or 06-relief-scene for a gallery tile, which this
  type never fills.

## SKELETON
The section form: one concise natural paragraph, no labels, in this order. Each arrow names an
entry in PARTS; the fixed sentences are the form's and are written word for word.

```
TYPE: 06-relief-after v0.2 [register: commercial | ugc]

  1. The picture: an editorial photograph, its angle and distance, the real
     place the product is used in, and who is there.                 -> PARTS/scene
  2. The product BY NAME, working, whole and unobstructed, at the size
     its host gives it.                                              -> PARTS/product
  3. The improvement as a physical fact: the one cue that says the
     problem is gone.                                                -> PARTS/cue
  4. The light: the form's light sentence.
  5. The words: the form's no-words sentence.
  6. The form's reference sentence, then its closing sentence.
```

## PARTS

**`scene`** — the place the section's copy puts the use in. A person appears where the product
serves one, doing the thing the product now lets them do; a face is allowed where it is relevant,
natural and relaxed, never a posed or exaggerated smile (the owner's feature-image instruction).

**`product`** — named as the page names it and never described (G2); in use, worn, held, plugged
in or installed, never set out on a surface for display. **Scale comes from the host** — the hand,
the chair, the wall socket — and the prompt moves the camera: *shot close enough that the product
reads whole* (ADR-106; held 6 of 6 in `03-mechanism-signal`'s set 04, borrowed). A fixed product
stays installed (G7-X).

**`cue`** — the improvement the line names, as something in the frame: the upright back, the
loaf still crusty when it is cut, the film playing in the back room. One cue, the eye's second
stop after the product. **Only what the product really does**: never an invented glow, mist or
vibration (G8), and never a health outcome drawn as a fact.

## SLOT CONSTRAINTS
- **One frame.** No panel, no inset, no recall of the problem: the before is another file.
- **Words: none**, and no drawn layer beyond one subtle effect the result needs, which the owner's
  instruction allows every mode. A result nobody can see is `03-spec-overlay`'s.
- **Full colour** (G11, ADR-104): a resolved state keeps the room's real colours and a person
  wears a clear, friendly colour; never a pale or drained grade.
- **On a pair's after field** the prompt is written from the pair's one locked description
  (`registry/pdp-dr-instruction.md`, *A pair shares one description*) and differs from its before
  in the state line alone. The state line may be the product's presence itself: where the claim is
  what the product holds up, the after is the same frame with the product in it and working; where
  the result outlasts the use — skin weeks later — the product may stay out of both.
- **`register: ugc`** only in a block of buyers' own photos — `testimonials` today — in
  `05-social-snapshot`'s register, and the prompt ships with G14's flag and note (ADR-089).
- **A closing image** is gallery image 1 by default; this type fills it only where the block's
  copy argues what the packshot does not (`mapping/pdp-dr-rules.md`, *Slot kinds*).
- **Any screen** shows only a picture, with no interface, text or numbers (G6).
- **G13 binds**, casting follows the namespace, and a block that names a person shows no face.
- **Length and ratio** are the form's: at most 1,200 characters, and no frame shape in the prompt.

## NEGATIVE
```
[G6] + the product set out on display with nobody using it, the product small or far off,
a recall of the problem, a split frame, an inset, a second panel, an arrow, a tick or a cross,
a posed or exaggerated smile, an invented glow, mist or vibration, a pale or drained grade,
shop signs or labelled packaging in the background
```

## BLOCK
**Criterion 3: the owner failed this type's first render.** Set `section-02` put it on the owner's
page v17, image 8, and the owner judged the set's eight renders *"các ảnh trên chất lượng vẫn còn
kém so với instruction"* — still poor next to the instruction's own results (ADR-111). The harness
had graded it partial before that; the observations are under KNOWN-FLAKY and none is written into
the skeleton yet. **The trial is `sets/section-03/`**: the same field, written by the owner's
instruction as it stands, with nothing the section form adds. Its result decides this skeleton.
`sets/section-01/` is unrendered and in 0.1's form.

**Criterion 1 cannot be met from the ledger as it stands**: the PDP corpus is gallery tiles, and
this type fills section fields. The type comes from the owner's tested instruction, so the count
is the owner's to waive, as ADR-057 waived it for `03-spec-macro`.

**Criterion 2, run on paper in ADR-110**: of the four templates' section, pair and closing
fields, this type takes `why.*`, every `*after_image` and a closing field whose copy argues an
outcome, and it contests no gallery tile — its trigger refuses one. Its live neighbours are
`06-relief-hero`, which builds an inset and a text offset this type has no room for, and
`06-relief-scene`, whose law asks for a public place and a bookend to a pain scene.

## KNOWN-FLAKY
Single observations, none yet a clause (SPEC §6.2); what the trial decides comes first.

- **Set `section-02`, image 8** (harness partial). The scene held — upright, calm, working, full
  colour, the monitor a picture — but the cushion came back light grey and smooth, where the
  reference is charcoal with a ribbed back; whether the photo was attached is unrecorded. The sheet
  of paper in her hand carried pseudo-text, which is diegetic and which G6 permits; the no-words
  sentence did not stop it.

## CHANGELOG
- 0.2 (2026-09-18): first render — set `section-02`, the owner's page v17 — failed by the owner on
  quality against the instruction (ADR-111). No clause added: the harness's observations wait in
  KNOWN-FLAKY while `section-03` tests the instruction as written against this form.
- 0.1 (2026-09-18): drafted from the owner's image instruction, the WITH / AFTER mode, with the
  section form as its skeleton (ADR-110). New device `after`. No render.

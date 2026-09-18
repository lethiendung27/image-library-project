---
id: 06-relief-after
step: 6
job: relief
device: after
version: "0.4"
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
blocked_by: "Criterion 3: two rounds on the owner's page v17 — section-02 failed by the owner on quality, section-03 (the instruction as it stands) graded by the harness after the owner's word on the size of its words and marks (ADR-112); 0.4 adds the owner's design rules (ADR-113) and has no render; set section-06 is its first, and the verdict SPEC 6.3 asks for is the owner's. Criterion 1: no corpus record carries this id, because the type is written from the owner's image instruction of 2026-09-18 rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-110."
---

# 06-relief-after — PDP-DR SECTION TYPE, DRAFT

**The WITH / AFTER mode of the owner's image instruction** (`~/Downloads/images prompt.txt`,
2026-09-18, ADR-110). One of the seven section types, for the images outside the product card's gallery;
`registry/pdp-dr-instruction.md`, *The section form*, carries the form and the law they all share.

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
The section form since ADR-112: the owner's image instruction as it stands. Its Image_Type is this
type's mode and its Description the field's own page values; the prompt is one concise natural
paragraph with no labels, in this order. Each arrow names an entry below or in *The section form*.

```
TYPE: 06-relief-after v0.4 [register: commercial | ugc]
Image_Type: WITH / AFTER

  1. The register and the camera: "Editorial realism photo", the angle and distance.
  2. The real place the product is used in, and who is there.        -> PARTS/scene
  3. The product BY NAME, working and whole; a seated product on a
     seat of a clearly different tone.                               -> PARTS/product
  4. The improvement as a physical fact: the one cue that says the
     problem is gone.                                                -> PARTS/cue
  5. The lock's lighting family and colour tone, and the instruction's tone.
  6. "No text."
  7. G1 in one sentence: "Use the attached product photo as the exact reference."
```

## PARTS

**`scene`** — the place the section's copy puts the use in. A person appears where the product
serves one, doing the thing the product now lets them do; a face is allowed where it is relevant,
natural and relaxed, never a posed or exaggerated smile (the owner's feature-image instruction).
**The point where the product meets the person or the thing stays in view** (owner, ADR-113): a
person using it looks at the point of use; a person at rest with it is relaxed and looks away.

**`product`** — named as the page names it and never described (G2); in use, worn, held, plugged in
or installed, never set out on a surface for display. **Scale comes from the host** — the hand, the
chair, the wall socket — and the prompt moves the camera: *shot close enough that the product reads
whole* (ADR-106; held 6 of 6 in `03-mechanism-signal`'s set 04, borrowed). A fixed product stays
installed (G7-X). **A seated product sits on a seat of a clearly different tone**, asked as a
relation, never as a colour: arm B of ADR-111 left the sentence out and 2 of its 3 seated frames put
the cushion on a black seat of its own tone, where arm A carried it 4 of 4 (ADR-112).

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
- **Real, never worn** (*The owner's design rules*, ADR-113): nothing in the frame is old, worn,
  scratched, stained or faded.
- **G13 binds**, and casting follows the namespace.
- **Ratio** never goes into the prompt (ADR-016); the owner renders the field at the frame its
  template shows (*The section form*, *The frame*).

## NEGATIVE
```
[G6] + the product set out on display with nobody using it, the product small or far off,
a recall of the problem, a split frame, an inset, a second panel, an arrow, a tick or a cross,
a posed or exaggerated smile, an invented glow, mist or vibration, a pale or drained grade,
shop signs or labelled packaging in the background, the point where the product meets the
person hidden, a worn, scratched, stained or faded surface
```

## BLOCK
**Criterion 3: two rounds, and 0.3 is what they left.** Set `section-02` wrote the owner's page v17
in 0.1's form, and the owner failed it on quality against the instruction (ADR-111). Set
`section-03` wrote the same fields by the instruction as it stands, image 8 here, and the owner's
word narrowed to the size of the drawn words and marks; the harness graded it partial (ADR-112). 0.3
is the instruction as it stands plus what the two rounds earned. It has no render: `sets/section-04/`
was written for it. **0.4 adds the owner's design rules of 2026-09-18** (ADR-113); `sets/section-06/`
is its first set, and the verdict SPEC §6.3 asks for is the owner's.

**Criterion 1 cannot be met from the ledger as it stands**: the PDP corpus is gallery tiles, and
this type fills section fields. The type comes from the owner's tested instruction, so the count
is the owner's to waive, as ADR-057 waived it for `03-spec-macro`.

**Criterion 2, run on paper in ADR-110**: of the four templates' section, pair and closing
fields, this type takes `why.*`, every `*after_image` and a closing field whose copy argues an
outcome, and it contests no gallery tile — its trigger refuses one. Its live neighbours are
`06-relief-hero`, which builds an inset and a text offset this type has no room for, and
`06-relief-scene`, whose law asks for a public place and a bookend to a pain scene.

## KNOWN-FLAKY
Single observations; what recurred across both rounds is written into 0.3, and the rest waits here.

- **Set `section-02`, image 8** (harness partial). The scene held — upright, calm, working, full
  colour, the monitor a picture — but the cushion came back light grey and smooth, where the
  reference is charcoal with a ribbed back; whether the photo was attached is unrecorded. The sheet
  of paper in her hand carried pseudo-text, which is diegetic and which G6 permits; the no-words
  sentence did not stop it.

- **Set `section-03`, image 8** (harness partial). Calm, upright, working; the cushion charcoal
  as the reference is, but on a black mesh chair of its own tone, so its outline barely reads —
  the seated relation 0.3 carries again. A beige sweater in a white room: colourfulness 20.7,
  under the 10th percentile of the owner's own stills (22.2).

## CHANGELOG
- 0.4 (2026-09-18): the owner's design rules (ADR-113) — the lock's lighting family and colour
  tone, real and never worn, and the point where the product meets the person kept in view, the
  gaze on the point of use or relaxed and away. The no-face clause left with the expert block's
  new type.
- 0.3 (2026-09-18): the skeleton is the owner's image instruction as it stands, arm B of ADR-111,
  with G1 in one sentence (ADR-112). The two rounds' earned clauses are written in.
- 0.2 (2026-09-18): first render — set `section-02`, the owner's page v17 — failed by the owner on
  quality against the instruction (ADR-111). No clause added: the harness's observations wait in
  KNOWN-FLAKY while `section-03` tests the instruction as written against this form.
- 0.1 (2026-09-18): drafted from the owner's image instruction, the WITH / AFTER mode, with the
  section form as its skeleton (ADR-110). New device `after`. No render.

---
id: 03-use-demo
step: 3
job: use
device: demo
version: "0.2"
status: reserved
replaced_by: null
channels: [landing-page]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [badge]
variants: []
exempt_from: [G3, G4]
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: "Criterion 3: the owner failed this type's first render, set section-02, on quality against the instruction (ADR-111); set section-03, the same fields written by the instruction as it stands, is the trial that decides the skeleton, and the verdict SPEC 6.3 asks for is the owner's. Criterion 1 reads as met, 5 distinct sources by `python3 scripts/validate.py --evidence` on 2026-09-18, but no record was re-read for this draft. Criterion 2 was run on paper in ADR-110."
---

# 03-use-demo — PDP-DR SECTION TYPE, DRAFT

**The HOW TO USE mode of the owner's image instruction** (`~/Downloads/images prompt.txt`,
2026-09-18, ADR-110). One of six section types, for the images outside the product card's gallery;
`registry/pdp-dr-instruction.md`, *The section form*, carries the form and the law all six share.

The owner's rules for this mode, word for word:

```
- Single focused step (strict: follow the input's step)
- Human faces allowed when relevant
- Hands/interaction strongly encouraged
  (e.g., input "Mount: Easy wall-mount installation…" →
  image should show a hand mounting the device on the wall)
- No text except essential step markers
```

The id is not new. `03-use-demo` has stood in the ledger as a corpus proposal since 2026-08-11 —
the instruction's type map names it as the nearest proposal to the owner's *Applied Use
Storytelling*, and ADR-092, ADR-094 and ADR-097 each left it undrafted — and the vocabulary held the device
`demo` reserved for it. This file is its first draft. **Two of its ledger records are section
images, as this type's fields are**: Densjet's `benefit-braces`, and ClikTric's third feature
item, which the owner chose on 2026-09-17 as a reference for feature images.

## PURPOSE
Show ONE step of using the product, as one realistic photograph: a hand or a person doing exactly
the step the section names, with the product. It answers *"will I manage this"* with the act
itself. The image sits beside its own HTML copy, which lists the steps; the picture shows one of
them, in three seconds.

## TRIGGER
use_when: >
  An LP2 image outside the product card's gallery whose section names an act of the
  buyer's hands: a how-to block of steps, a feature item whose line is something the
  buyer does, an expert block carried by working hands. One image shows one step and
  follows the copy's own step strictly. Take 03-mechanism-diagram when the steps happen
  inside the product or the body rather than in the buyer's hands; 06-relief-after when
  the line is the result rather than the act; 03-use-sequence or 03-use-grid for a
  gallery tile that strings several steps together, which this type never fills.

## SKELETON
The section form: one concise natural paragraph, no labels, in this order. Each arrow names an
entry in PARTS; the fixed sentences are the form's and are written word for word.

```
TYPE: 03-use-demo v0.2

  1. The picture: an editorial photograph, its angle and distance, and
     the real place this step happens in.                            -> PARTS/scene
  2. The step, as the copy states it: whose hand, doing what, to which
     part of what.                                                   -> PARTS/step
  3. The product BY NAME, whole and unobstructed, at the size the hand
     or the host gives it.                                           -> PARTS/product
  4. The light: the form's light sentence.
  5. The words: the form's no-words sentence, or the step-marker sentence. -> SLOT CONSTRAINTS
  6. The form's reference sentence, then its closing sentence.
```

## PARTS

**`scene`** — where this step really happens: the hallway socket, the chair at the desk, the
bathroom shelf. Partial-hand, over-the-shoulder or a 45-degree usage angle (the owner's
feature-image instruction's list); close enough that the act fills the frame. A face appears only
where the step needs the person, and it attends to the task, never to the lens.

**`step`** — the copy's own step and no other: *"strict: follow the input's step"*.
- **One image, one step.** Where a block gives ONE image for several steps, the frame takes the
  step that answers *"will I manage this"* — the first act of the buyer's hands on the product —
  and the session's notes name the step it chose. Never a collage and never two moments in one
  frame.
- **No step the page does not give** (`03-use-sequence`'s LP2 law, borrowed): the hand does what
  the copy says, to the part the copy names, and nothing the product's photograph does not show.
- The act is caught mid-way — a finger on the button, the plug a moment from the socket — so the
  frame reads as doing, not as holding.

**`product`** — named as the page names it, placed and never described (G2). **Scale comes from
the hand or the host** and the prompt moves the camera: *shot close enough that the product reads
whole* (ADR-106, borrowed). A thin product is framed on its working end (ADR-109, borrowed). A
fixed product stays installed (G7-X).

## SLOT CONSTRAINTS
- **One frame.** No panel, no strip and no inset.
- **Words: none by default.** The page numbers its steps in HTML beside the image. Where a block
  gives every step its own image, a frame may carry its step's numeral and nothing else — the
  owner's *essential step marker* — small, in the top-left corner, in the session lock's type
  face. It takes this type's `badge` slot, so G16 binds it. Never a word, an arrow or a caption.
- **Hands** are this renderer's weakest subject (adapter Rule 5): one hand where one will do, its
  action named in a few functional words.
- **Nothing drawn anywhere, including on packaging** (`03-use-sequence`'s LP2 law, borrowed: two
  of the owner's renders printed an arrow on the shipping box).
- **Any screen** shows only a picture, with no interface, text or numbers (G6).
- **G13 binds**, casting follows the namespace, and a block that names a person shows hands and
  no face.
- **Length and ratio** are the form's: at most 1,200 characters, and no frame shape in the prompt.

## NEGATIVE
```
[G6] + a collage of steps, a strip of panels, two moments in one frame, an arrow, a caption,
a word of any kind, a step the page does not give, the product set out on display with
nobody using it, the product enlarged against the hand beside it, a face posing for the lens,
shop signs or labelled packaging in the background
```

## BLOCK
**Criterion 3: the owner failed this type's first render.** Set `section-02` put it on the owner's
page v17, image 2, and the owner judged the set's eight renders *"các ảnh trên chất lượng vẫn còn
kém so với instruction"* — still poor next to the instruction's own results (ADR-111). The harness
had graded it pass before that; the observations are under KNOWN-FLAKY and none is written into the
skeleton yet. **The trial is `sets/section-03/`**: the same field, written by the owner's
instruction as it stands, with nothing the section form adds. Its result decides this skeleton.
`sets/section-01/` is unrendered and in 0.1's form.

**Criterion 1 reads as met, and the reading is unchecked.** `python3 scripts/validate.py
--evidence` counts 10 observations across 5 distinct sources on 2026-09-18, now that the id has a
file: capix-mat, gripi-mata, hydrovia, densjet-nova and cliktric, with two unsourced records from
2026-08-11. None was opened again for this draft, which ADR-092 asks of a draft built from the
ledger. This one is built from the owner's instruction, so the records are provenance until
someone reads them against this skeleton.

**Criterion 2, run on paper in ADR-110**: of the four templates' fields this type takes a `how`
block whose steps are the buyer's actions — WiBoofy's, Deal's — and the feature items that are an
act: *One press to pair*, *Wash it, use it again*. It contests no gallery tile; `03-use-sequence`
and `03-use-grid` keep those, and their `multi_step_usage` gate does not reach this id.

## KNOWN-FLAKY
Single observations, none yet a clause (SPEC §6.2); what the trial decides comes first.

- **Set `section-02`, image 2** (harness pass). One step, two hands pressing the cushion flush into a
  car seat mid-act, the place plain. The wheel and dashboard came back sharp where the prompt asked
  them soft.

## CHANGELOG
- 0.2 (2026-09-18): first render — set `section-02`, the owner's page v17 — failed by the owner on
  quality against the instruction (ADR-111). No clause added: the harness's observations wait in
  KNOWN-FLAKY while `section-03` tests the instruction as written against this form.
- 0.1 (2026-09-18): first draft of the corpus proposal ADR-078 left undrafted, written from the
  owner's image instruction, the HOW TO USE mode, with the section form as its skeleton (ADR-110).
  The device `demo` leaves its reserved state. No render.

---
id: 04-proof-testing
step: 4
job: proof
device: testing
version: "0.5"
status: active
replaced_by: null
channels: [landing-page, marketplace]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [title, copy]
variants: []
exempt_from: []
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: null
copied_from: lede-testing
copied_at_version: "0.4"
---

# 04-proof-testing

## PURPOSE
The work being done. Hands, an instrument and one unit under test on a working surface,
caught mid-measurement. It argues that somebody actually put these products through
something — the E-E-A-T signal of the format — and it argues it with apparatus rather
than with a number.

**Copied from `registry/toplist-types/lede-testing.md` at version 0.4** (owner instruction,
2026-09-17, ADR-097: a type from another page kind's folder may be copied into LP2 where it fits,
and changed). What was copied:
- **Spliced by script from commit `3828758`, not retyped:** PURPOSE, SKELETON, PARTS and NEGATIVE.
- **Rewritten: TRIGGER**, in LP2's router language. `use_when` is what the router reads, and the
  parent's speaks of a reviewer and a field of competing products.
- **Folded into TRIGGER: the parent's BOUNDARY**, because an LP2 type keeps its discriminator
  there (SPEC §3.8).
- **Not copied:** FOUNDING RENDER ROUND and CHANGELOG, which are the parent's record.
- **The id is LP2's**, because the parent's is an argument rather than `{step}-{job}-{device}`.

Where a clause below cites renders or a corpus, those were the toplist namespace's.
`PARTS/ground` was measured on eleven top-N lede frames (ADR-073).
`registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## LP2 LAW
Added 2026-09-17 (ADR-097). This section is this copy's own and a re-copy keeps it;
`registry/pdp-dr-instruction.md` binds the rest.

- **The unit under test is the page's own product, and the test is the page's.**
  - The page names what was tested or measured — a load, a signal, a seal, a surface, a
    skin-safety check — and the frame shows that test being done.
  - It never invents one: the instruction's never-list and `04-proof-lockedframe`'s `LP2 LAW`
    already refuse an invented test.
  - The parent's "these products" reads here as the page's own product, and the hands as its tester's.
- **The reading stays illegible, and on LP2 the reason is G6.** A readout, a dial or a scale is
  drawn by the model, and G6 keeps readouts out of model-drawn frames.
  - The parent's NEGATIVE paragraph gives A15 as the reason, and it predates ADR-095.
  - On LP2 a figure the page supplies may appear, but in the words, never on the instrument.
- **The words.**
  - In the product card's gallery: a title of 2–5 words, and one copy line only where the page
    supplies the measured figure (ADR-095).
  - Outside the gallery — a safety block, an expert block, a proof section — no words at all
    (ADR-096).
- **No face, and no clinical dress.** The parent's negative already keeps both out. On LP2 that
  is also what lets this type carry an `expert` block without giving a named person a face
  (`mapping/pdp-dr-rules.md`, rule 12).
- **Ground.** The lock's two treatments bind (the instruction).
  - The parent's bench — mid, quiet, unevenly lit — is a real room where context is the
    argument, which is the reason the lock asks of any darker ground.
  - Its numbers were measured on another corpus and not on this one.
- **Untested here.** The parent has one render, on a cord tightening tool, graded `partial`, and
  none under this namespace's law.

Slots an LP2 prompt adds to the SKELETON:
```
[TITLE]  what was tested, 2–5 words. Gallery only.           -> LP2 LAW
[COPY]   the page's measured figure, one line. Gallery only,
         and only where the page supplies it.                 -> LP2 LAW
```

## TRIGGER
use_when: >
  The page says the product was tested, measured or checked — a load or durability test,
  a signal or output check, a seal or leak test, a skin safety test — and a slot has to
  show that the testing happened rather than state its result. A proof or quality
  section, a safety block, an expert block whose claim is a test, or a proof tile in the
  gallery. The frame shows one unit on a bench or rig, an instrument in contact with it
  and working hands, and never a legible number. Where the proof is a comparison or a
  before and after the reader can watch, the type is 04-proof-lockedframe; where the
  product is shown doing its job in a home, 06-relief-hero; where the claim is the
  product's own surface seen close, 03-spec-macro.

## SKELETON
```
TYPE: lede-testing v0.4
REGISTER: editorial documentary photograph, one frame, no words in it.

[PRODUCT REFERENCE]  the attached photo is the exact reference.        -> G1
[UNIT]               one unit, in the position the measurement needs it.
[INSTRUMENT]         the measuring device, in contact with or aimed at the unit.
[HANDS]              a hand doing the work, cropped at the wrist or forearm.
[SURFACE]            a working surface — bench, worktop, test rig — with the tools of
                     the measurement and nothing decorative.
[LIGHT]              plain working light, even, no studio key and no rim.
[GROUND]             a real place: mid, quiet, unevenly lit.  -> PARTS/ground
```

**The instrument is the argument and it must be doing something.** An instrument lying
beside the unit is a prop; an instrument in contact with it, held, is evidence. This is
`argument-faults.md` A12 read forwards: the hand carrying the argument must be employed
by the measurement and must not also be presenting the product to the lens.

## PARTS
**`ground`** — a REAL place, and this type has the namespace's largest sample: **11
frames**, measured on its own corpus with nothing imported (ADR-073).

| | measured | against the designed grounds |
|---|---|---|
| texture | **7.1** | 0.8 – 2.9 |
| value median | **0.65** | 0.90 |
| saturation median | **0.13**, 2 of 11 above 0.25 | 0.49 |
| value spread across the ring | **0.67** | 0.15 – 0.33 |

- **Real detail**, not a sweep. Racking, a wall, a bench edge, other work going on.
- **Mid, not light.** A bench under working light is darker than a studio ground, and
  asking for a bright background here produces the studio this type is not.
- **Quiet.** The colour lives in the apparatus and the product; the room carries almost
  none. This is the one clause the corpus states most strongly.
- **Unevenly lit.** Light falls off across the frame. A prompt asking for even illumination
  across the background is asking for the wrong picture.

## NEGATIVE
```
[G6] + a legible number, a digital readout in focus, a gauge whose scale can be read,
a chart, a second product class, a competitor's product, a person's face,
a lab coat, a clipboard, any word, price or logo baked into the picture
```
**The number ban is the type's whole legality and it is not stylistic.** A readable
measurement in the frame is `argument-faults.md` A15 — a figure the picture cannot
substantiate — and it is the fault three proposals (`04-proof-stat`,
`04-proof-instrument`, `04-proof-interface`) are already blocked behind. This type exists
BECAUSE the argument survives without the number: the apparatus and the hands carry it.
The moment a reading is legible, this type has become one of those three and must wait
for the same decision.

**No lab coat, no clipboard.** They are the costume of a credential this page does not
have, and a credential is what G16 refuses at its `named expert` row. **Contradicted once
by the corpus** — observation 25 of batch 2026-09-09-B is a technician in a white coat at
a real bench — and left standing at 1 observation against a clause with none, for
curation to settle rather than this diff.

**This type carries no text, on its own evidence** (ADR-071 permits a layer where a type
earns one): **10 of 11** corpus observations carry no words, and the single exception is
a video thumbnail rather than a page lede.

## CHANGELOG
- 0.5 (2026-09-17): copied from `lede-testing` at 0.4 (commit `3828758`), on the owner's
  instruction that types from other page kinds may be copied into LP2 and changed. TRIGGER
  rewritten for LP2's router, with the parent's BOUNDARY folded in; `LP2 LAW` added. PURPOSE,
  SKELETON, PARTS and NEGATIVE are the parent's text. Device `testing` is new. ADR-097.

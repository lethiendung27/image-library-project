---
id: 03-mechanism-diagram
step: 3
job: mechanism
device: diagram
version: "0.1"
status: reserved
replaced_by: null
channels: [landing-page]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [badge]
variants: []
exempt_from: [G7]
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: "Criterion 3: no render, and the verdict SPEC 6.3 asks for is the owner's; set section-01 is its first. Criterion 1: no corpus record carries this id, because the type is written from the owner's image instruction of 2026-09-18 rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-110."
---

# 03-mechanism-diagram — PDP-DR SECTION TYPE, DRAFT

**The HOW IT WORKS mode of the owner's image instruction** (`~/Downloads/images prompt.txt`,
2026-09-18, ADR-110). One of six section types, for the images outside the product card's gallery;
`registry/pdp-dr-instruction.md`, *The section form*, carries the form and the law all six share.

The owner's rules for this mode, word for word:

```
- Use clean 2D/3D visualization or cutaway diagrams
- Arrows, icons, particles, signal paths, soundwaves allowed
- Minimal technical labels allowed (no marketing text)
- Human faces allowed only if absolutely essential, otherwise avoid
- Only text for annotation
```

It is also the file the instruction's **Principle** form never had (ADR-094): *one clean 2D or 3D
diagram beside the product or in an inset, never painted onto the product*.

## PURPOSE
Explain how the product works, as one clean technical visualisation: what it sends, moves or
changes, where that goes, and what it does there. The register is a drawn one — a 2D or 3D
render, or a drawn cutaway — so nothing photographic is opened and nothing can look broken. The
image sits beside its own HTML copy, which names the steps; the picture shows the one principle
those steps share, in three seconds.

## TRIGGER
use_when: >
  An LP2 image outside the product card's gallery whose section explains a working
  principle: a how-it-works block whose steps happen inside the product, the body or
  the material rather than in the buyer's hands; a feature item that names a process;
  an expert block whose quoted claim is a mechanism. Take 03-use-demo when the steps
  are the buyer's own actions; 03-spec-overlay when the claim is one capability shown
  on the product in use rather than a process explained; 03-mechanism-ghostbody,
  03-mechanism-xray or 03-mechanism-contact for a gallery mechanism tile, which this
  type never fills.

## SKELETON
The section form: one concise natural paragraph, no labels, in this order. Each arrow names an
entry in PARTS or MARKS; the fixed sentences are the form's and are written word for word.

```
TYPE: 03-mechanism-diagram v0.1

  1. The picture: a clean technical visualisation, 2D or 3D, its view and
     its ground, and the product BY NAME in it.                     -> PARTS/view
  2. What is opened, where the principle is inside something: the body,
     the material or the building, drawn as a clean section.        -> PARTS/section
  3. The principle, in a sentence of its own: what is drawn, in its own
     form, where it starts and what it lands on.                    -> MARKS/flow
  4. The light: clean, even studio light with a soft shadow.
  5. The words: the labels sentence, or the form's no-words sentence. -> SLOT CONSTRAINTS
  6. The form's reference sentence, then its closing sentence.
```

## PARTS

**`view`** — one view, chosen for the principle: a side section for something that passes through
layers, a three-quarter view for something that flows around the product, a plan view for reach
across rooms. The ground is quiet and light, with a floor plane and a soft shadow, never a flat
void and never pure white (ADR-094). The product is named as the page names it, placed and never
described (G2), and drawn whole at the working end of the diagram.

**`section`** — only where the principle is inside something, and always DRAWN: skin as a clean
cross-section, foam as a cut block, a house as a plan or a section. **A drawn register opens
nothing anyone owns**, which is the line ADR-109 draws — the 3 of 4 cuts that came back as damage
were holes in photographed possessions, and the rendered body types were never touched by it. The
product itself is opened only where the page names the parts inside it, as
`03-mechanism-xray`'s LP2 law already says; a cushion, a mat or a garment has no interior to show.
No person where a body region is enough; a face only where the principle cannot be read without
one.

## MARKS

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `flow` | the thing that moves, in its own form: light as a beam or pulses, heat as a soft gradient inside the section, air as smooth streams, sound as waves, a signal as arcs, load as arrows into a surface. It starts at the product's working end and LANDS on what it acts on | one family, one colour: luminous blue or cyan for a working flow (G3); a warm glow where the thing itself is warm, as the owner's `525f1c50` halo is; red only on a wrong state | one family to a frame | the owner's twelve feature frames: the mark is the thing itself 12 of 12 and a generic glowing arc 0 of 12 (ADR-106, borrowed); **no render of this type** |

- **Beside or inside the section, never painted on the product's surface**: the owner's runs
  painted a heat map, waves or light lines onto the product 4 times (ADR-094).
- **Never along a cable**: a mark drawn along a wire became the wire 2 of 2 (ADR-109, borrowed).
- No rainbow gradient, no lightning bolt, no bars and no readings on the mark (A15, G6).

## SLOT CONSTRAINTS
- **One frame, one principle.** A block of three steps is still one principle; where the steps
  are three different principles the block's items take three frames. No panels.
- **Words: technical labels only**, as the owner's rule says — one to three words naming a part
  or a stage, **at most three** (the namespace's limit for call-out lines outside
  `03-spec-callout`), each beside the thing it names and never on an arrow or a line. No title,
  no sentence, no marketing word, and no figure unless the page supplies it (A15, ADR-095). The
  labels take this type's `badge` slot, so G16 binds them. The labels sentence ends: *nothing else
  in the picture carries text, and the bottom-right corner stays clear.*
- **A drawn figure must be true of the frame it sits in** (ADR-109).
- **Health and medical outcomes are never drawn as fact** (the instruction's text section): the
  diagram shows what the product sends and where it goes, in the page's own words.
- **One mechanism variant to a page** unless the page asks for two (`mapping/pdp-dr-rules.md`,
  rule 3).
- **Length and ratio** are the form's: at most 1,200 characters, and no frame shape in the prompt.

## NEGATIVE
```
[G6] + a photograph with a hole cut in it, a torn or damaged object, a mark painted on the
product's surface, a mark running along a cable, a rainbow gradient, lightning bolts,
bars or readings on the mark, a marketing word, a sentence of copy, more than three labels,
a label set along an arrow, an invented interior, a face that is not needed, a flat white void
```

## BLOCK
**Criterion 3 has no render.** The owner's statement of 2026-09-18 — that the instruction's own
results *"vượt xa các types hiện tại trong pdp-dr"* — is a verdict on the instruction, not on this
skeleton, and no repo prompt made those renders. `sets/section-01/` is the first set; its image 3
is this type's. The Principle form it succeeds has no passing render either: the owner's runs
tried it three times and painted all three onto the product (ADR-094).

**Criterion 1 cannot be met from the ledger as it stands**: no corpus record carries this id. The
type comes from the owner's tested instruction, so the count is the owner's to waive, as ADR-057
waived it for `03-spec-macro`.

**Criterion 2, run on paper in ADR-110**: of the four templates' fields this type takes a `how`
block whose steps are not the buyer's actions — Aure's — and an item or an expert claim that names
a process. It contests no gallery tile. Its neighbours are all reserved or gallery types, and the
line against each is in the trigger.

## CHANGELOG
- 0.1 (2026-09-18): drafted from the owner's image instruction, the HOW IT WORKS mode, with the
  section form as its skeleton (ADR-110). New device `diagram`. No render.

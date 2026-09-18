---
id: 03-mechanism-diagram
step: 3
job: mechanism
device: diagram
version: "0.4"
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
blocked_by: "Criterion 3: two rounds on the owner's page v17 — section-02 failed by the owner on quality, section-03 (the instruction as it stands) graded by the harness after the owner's word on the size of its words and marks (ADR-112); 0.4 adds the owner's design rules (ADR-113) and has no render; set section-06 is its first, and the verdict SPEC 6.3 asks for is the owner's. Criterion 1: no corpus record carries this id, because the type is written from the owner's image instruction of 2026-09-18 rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-110."
---

# 03-mechanism-diagram — PDP-DR SECTION TYPE, DRAFT

**The HOW IT WORKS mode of the owner's image instruction** (`~/Downloads/images prompt.txt`,
2026-09-18, ADR-110). One of the seven section types, for the images outside the product card's gallery;
`registry/pdp-dr-instruction.md`, *The section form*, carries the form and the law they all share.

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
The section form since ADR-112: the owner's image instruction as it stands. Its Image_Type is this
type's mode and its Description the field's own page values; the prompt is one concise natural
paragraph with no labels, in this order. Each arrow names an entry below or in *The section form*.

```
TYPE: 03-mechanism-diagram v0.4
Image_Type: HOW IT WORKS

  1. The register and the view: "Clean 3D technical cutaway" (or 2D), the view,
     the lock's seamless ground, and the product BY NAME in it.     -> PARTS/view
  2. What is opened, drawn as a clean section.                       -> PARTS/section
  3. The principle, in a sentence of its own: what is drawn, in its own
     form, bold, where it starts and what it lands on.               -> MARKS/flow
  4. The labels: each named with the part its line touches, set large in the
     lock's typeface and text colour, in its chip over a busy part.  -> SLOT CONSTRAINTS
  5. "Clean even lighting, balanced contrast, no marketing text."
  6. G1 in one sentence: "Use the attached product photo as the exact reference."
```

## PARTS

**`view`** — one view, chosen for the principle: a side section for something that passes through
layers, a three-quarter view for something that flows around the product, a plan view for reach
across rooms. The ground is the lock's seamless treatment, in its words (owner, ADR-113): quiet and light,
with a floor plane and a soft shadow, never a flat void and never pure white (ADR-094). The product is named as the page names it, placed and never
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
| `flow` | the thing that moves, in its own form: light as a beam or pulses, heat as a soft gradient inside the section, air as smooth streams, sound as waves, a signal as arcs, load as arrows into a surface. It starts at the product's working end and LANDS on what it acts on | **the lines, arrows, leaders and labels in ONE neutral colour, the lock's text colour** (the owner's Principle rule, ADR-113); the phenomenon itself — light, heat, air — may keep one colour of its own where it has one: luminous blue or cyan for a working flow (G3), warm where it is warm; never a rainbow; red only on a wrong state | one family to a frame | the owner's twelve feature frames: the mark is the thing itself 12 of 12 and a generic glowing arc 0 of 12 (ADR-106, borrowed); **no render of this type** |

- **Beside or inside the section, never painted on the product's surface**: the owner's runs
  painted a heat map, waves or light lines onto the product 4 times (ADR-094).
- **Never along a cable**: a mark drawn along a wire became the wire 2 of 2 (ADR-109, borrowed).
- No rainbow gradient, no lightning bolt, no bars and no readings on the mark (A15, G6).
- **Any icon is drawn in the lock's icon style** (ADR-113), and no line or arrow takes the accent.

## SLOT CONSTRAINTS
- **One frame, one principle.** A block of three steps is still one principle; where the steps
  are three different principles the block's items take three frames. No panels.
- **Words: technical labels only**, as the owner's rule says — one to three words naming a part
  or a stage, **at most three** (the namespace's limit for call-out lines outside
  `03-spec-callout`), each beside the thing it names and never on an arrow or a line. No title,
  no sentence, no marketing word, and no figure unless the page supplies it (A15, ADR-095). The
  labels take this type's `badge` slot, so G16 binds them. **The prompt says what each label's line
  touches**: one line in each round ended off its part, 2 of 2 (`section-02`'s *Seat gap*,
  `section-03`'s *Pelvis upright*). A line exists only where a label needs one. The labels are set
  large in the lock's typeface and text colour on the light ground, sized for a phone (*Words and
  marks on a phone*); a label that must sit over a busy part sits in the lock's chip (*The owner's
  design rules*).
- **A drawn figure must be true of the frame it sits in** (ADR-109).
- **Health and medical outcomes are never drawn as fact** (the instruction's text section): the
  diagram shows what the product sends and where it goes, in the page's own words.
- **One mechanism variant to a page** unless the page asks for two (`mapping/pdp-dr-rules.md`,
  rule 3).
- **Ratio** never goes into the prompt (ADR-016); the owner renders the field at the frame its
  template shows (*The section form*, *The frame*).

## NEGATIVE
```
[G6] + a photograph with a hole cut in it, a torn or damaged object, a mark painted on the
product's surface, a mark running along a cable, a rainbow gradient, lightning bolts,
bars or readings on the mark, a marketing word, a sentence of copy, more than three labels,
a label set along an arrow, an invented interior, a face that is not needed, a flat white void,
lines or arrows in several colours, a label in a second typeface
```

## BLOCK
**Criterion 3: two rounds, and 0.3 is what they left.** Set `section-02` wrote the owner's page v17
in 0.1's form, and the owner failed it on quality against the instruction (ADR-111). Set
`section-03` wrote the same fields by the instruction as it stands, image 6 here, and the owner's
word narrowed to the size of the drawn words and marks; the harness graded it partial (ADR-112). 0.3
is the instruction as it stands plus what the two rounds earned. It has no render: `sets/section-04/`
was written for it. **0.4 adds the owner's design rules of 2026-09-18** (ADR-113); `sets/section-06/`
is its first set, and the verdict SPEC §6.3 asks for is the owner's.

**Criterion 1 cannot be met from the ledger as it stands**: no corpus record carries this id. The
type comes from the owner's tested instruction, so the count is the owner's to waive, as ADR-057
waived it for `03-spec-macro`.

**Criterion 2, run on paper in ADR-110**: of the four templates' fields this type takes a `how`
block whose steps are not the buyer's actions — Aure's — and an item or an expert claim that names
a process. It contests no gallery tile. Its neighbours are all reserved or gallery types, and the
line against each is in the trigger.

## KNOWN-FLAKY
Single observations; what recurred across both rounds is written into 0.3, and the rest waits here.

- **Set `section-02`, image 6** (the known risk, predicted partial; harness partial). It read at
  once: three labels spelled right, the blue band on the line where body meets cushion, and no
  face. But the *Seat gap* leader ended mid-seat under the thigh — the label named what the cushion
  removes, so there was nothing for its leader to end on; the crop was ignored, a full figure with
  the lower head in frame, and the no-face law held only because the figure is featureless; and the
  cushion came back as a plain L, without the reference's ribs or the slot at its joint.

- **Set `section-03`, image 6** (harness partial). Clean, with blue support arrows along the back
  and under the pelvis, a featureless figure, three labels spelled right. The *Pelvis upright* line
  ended on the cushion's back edge, not on the pelvis — one leader off its part in each round, 2
  of 2. **On a phone the labels' capitals measure 7.2–7.5 px and the lines 0.6 px** — the owner:
  *"chữ và các yếu tố đồ hoạ cần to rõ ràng hơn. mobile first"*.

## CHANGELOG
- 0.4 (2026-09-18): the owner's design rules (ADR-113) — lines, arrows, leaders and labels in one
  neutral colour, the lock's text colour, with the phenomenon keeping its own; labels in the
  lock's typeface, in its chip over a busy part; icons in its icon style; the lock's seamless
  ground.
- 0.3 (2026-09-18): the skeleton is the owner's image instruction as it stands, arm B of ADR-111,
  with G1 in one sentence (ADR-112). The two rounds' earned clauses are written in.
- 0.2 (2026-09-18): first render — set `section-02`, the owner's page v17 — failed by the owner on
  quality against the instruction (ADR-111). No clause added: the harness's observations wait in
  KNOWN-FLAKY while `section-03` tests the instruction as written against this form.
- 0.1 (2026-09-18): drafted from the owner's image instruction, the HOW IT WORKS mode, with the
  section form as its skeleton (ADR-110). New device `diagram`. No render.

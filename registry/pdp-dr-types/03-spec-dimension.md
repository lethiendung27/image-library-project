---
id: 03-spec-dimension
step: 3
job: spec
device: dimension
version: "0.1"
status: reserved
replaced_by: null
ratios: ["1:1", "4:3"]
channels: [landing-page, marketplace]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [title, copy]
variants: []
exempt_from: [G7]
pairs_with: []
never_with: []
avoid_adjacent: [03-spec-callout]
requires_pair: null
blocked_by: "Criterion 2, the router-confusion test against 03-spec-callout, and criterion 3, which has no render. Criterion 1 is cleared at seven distinct sources."
---

# 03-spec-dimension — PDP-DR DRAFT

Promotion status (2026-09-11): **7 distinct sources — criterion 1 CLEARED, and by two.**
The best-evidenced new cluster in the 157-image drop.

| source | what it dimensions |
|---|---|
| capix-mat | the inflated mat, three edges plus a tape-measure inset and a packed-size shot |
| clou-diaxi | the humidifier, height and two base edges, nothing else in frame |
| fosen-ring | the device AND its strap, six lines, metric and imperial |
| glowy-liff | the wand, five lines, **fused with a specification table below it** |
| gripi-mata | a flat DIAGRAM of the mat, three lines, plus a declared error band |
| moisosat | the dehumidifier twice, three lines, **fused with a specification table** |
| pawdi-cas | the camera twice, three lines, metric and imperial |

Criterion 2 is UNRUN and is the binding gap. Criterion 3 has no render. **Not routable.**
Device `dimension` is new vocabulary and ships in the same diff.

## PURPOSE
Answer "how big is it" with a number drawn onto the object. A dimension line spans a
distance and labels it; the reader checks the number against the thing it measures, in one
frame, with no paragraph. This is the tile a buyer of a desk appliance, a mat or a worn
device opens second.

## TRIGGER
use_when: >
  The buyer's doubt is dimensional and the product's size is not inferable from any other
  tile — a desk appliance, a mounted device, a mat, anything sold by fit. The gallery tile
  after the packshot, a marketplace size tile, or the tile a spec block refers to. Choose
  03-spec-callout when the labels name PARTS and what they do: a callout's leader points at
  a part, a dimension line measures a span, and that is the whole boundary between them.
  Choose 07-identity-inhand when a hand would answer the question better than a number,
  which is true for anything small enough to hold. NEVER where the measurement is not
  published — this type states figures and has nothing else to say.

## SKELETON
```
TYPE: 03-spec-dimension v0.1
REGISTER: commercial product photograph, knockout. One frame, no panels, no insets.

[PRODUCT REFERENCE]  the attached photo is the exact reference.   -> G1
[PRESENTATION]       the views the dimensions need, and no more.  -> PARTS/presentation
[SETTING]            a quiet ground with room for the lines.      -> PARTS/setting
[LIGHT]              broad and even; no shadow crosses a line.
[DIMENSIONS]         each line spans a real edge and is labelled. -> PARTS/dimensions

[TITLE]              what is being measured. Optional.            -> G16/title
```

## PARTS

**`presentation`** — the product shown ONCE where one view carries every dimension, TWICE
where it does not. Five of the seven sources show one view; two show two, and both of those
are objects whose depth is invisible head-on. **A third view is a decision to justify, not a
default:** more views mean smaller objects and smaller labels in the same square.

**`setting`** — a quiet ground: light in value, close to neutral in colour. Six of seven
sources use a plain white or near-white knockout, which is at the very top of the corpus's
own distribution (ADR-068, median value 0.89). This type has less reason than any other to
depart from it, because a dimension line is a thin graphic and a busy ground eats it.

**`dimensions`** — two to six lines. Each is a straight line with an arrowhead at both ends,
spanning a REAL edge of the object, labelled with a figure. Beyond six the labels collide
with the object they measure, which fosen-ring's six-line frame already shows at tile size.

**Give both units where the page sells across territories.** fosen-ring and pawdi-cas give
metric and imperial; capix-mat gives both; clou-diaxi, gripi-mata and moisosat give metric
alone. The dual form costs a longer label and answers a real question.

**The object may be a DIAGRAM rather than a photograph.** gripi-mata dimensions a flat grey
rounded rectangle standing in for a mat. That is legal and it is the right choice when the
product has no features worth showing at the size a dimension tile needs — but it teaches
nothing about the product, so it is the weaker form.

## SLOT CONSTRAINTS
- **Every figure must be published.** This type has no argument except its numbers, and a
  number nobody can check is `argument-faults.md` A15 with a line drawn under it. Where
  `content.json` carries no measurement, this type does not route.
- **A dimension is the A15-benign class and the reason is worth stating.** A line drawn on an
  object is substantiated BY the object: a reader compares the label to the thing it spans.
  That is not true of a performance percentage, and it is why this type may carry figures
  where `04-proof-stat` may not.
- **State the tolerance where the page has one.** gripi-mata prints *"Manual Measurement May
  Result In An Error Of 1-3 Cm / This Will Not Affect Usage"* under its three lines. A
  declared error band is worth more than a decimal place and is the honest form of this
  type's only claim.
- **G16 governs the labels.** They are the smallest type in the frame and the only content,
  so the mobile floor binds here harder than anywhere.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a person, a hand, a room, a prop for scale, a second product,
a leader pointing at a part rather than spanning an edge, a curved or angled
dimension line, a figure with no unit, a percentage, a duration, a weight the
page has not published, a dark or saturated ground, a cast shadow crossing a line
```

## BLOCK
**Waiting on criterion 2 and criterion 3.** Criterion 1 is cleared at seven distinct sources
across seven product categories — camping, appliance, wearable, beauty, homeware, appliance,
security — which is the widest category spread of any proposal this library holds.

**Criterion 2 is a real test, not a formality.** The boundary with `03-spec-callout` is drawn
in this file's own `use_when` — a callout's leader points at a PART and names it, a dimension
line spans an edge and measures it — and that sentence has never been tested against a
router. Both types put labelled graphics on a plain product on a quiet ground; the pictures
are close enough that a router reading only `use_when` may not separate them.

**Criterion 3 has no render.** No prompt has been written from this file.

**And one structural question the promotion diff has to answer.** Two of the seven sources
ship the dimension device FUSED with a specification table as two zones of one tile
(`glowy-liff`, `moisosat`). Either that is a variant of this type, or the table is a second
type that commonly pairs with it — `03-spec-table` stands at 2 sources and cannot decide it
alone. The fusion is recorded here rather than legislated.

## KNOWN-FLAKY
- **Nothing observed.** No prompt and no render exist for this file.
- Predicted from the corpus rather than measured: **six lines is where labels start to
  collide** with the object they measure. fosen-ring's frame dimensions a device and a strap
  with six lines and two of the labels touch the objects. Recorded as the first thing to
  watch in a founding round, not as a rule.

## CHANGELOG
- 0.1 (2026-09-11): drafted from eleven observations across seven distinct sources, batches
  2026-09-11-A, B, C, D, E, G and I. Criterion 1 cleared at seven; criteria 2 and 3 unrun.
  New device value `dimension`, which names how the argument is made rather than what is
  photographed — the test ADR-065 applied when it renamed `ingredient` to `stilllife`.
  Raised and evidenced by the curation analysis in `_CURATION-2026-09-11.md`. ADR-078.

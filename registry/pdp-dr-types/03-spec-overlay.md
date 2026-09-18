---
id: 03-spec-overlay
step: 3
job: spec
device: overlay
version: "0.3"
status: reserved
replaced_by: null
channels: [landing-page]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [title, badge]
variants: []
exempt_from: []
pairs_with: []
never_with: []
avoid_adjacent: []
requires_pair: null
blocked_by: "Criterion 3: two rounds on the owner's page v17 — section-02 failed by the owner on quality, section-03 (the instruction as it stands) graded by the harness after the owner's word on the size of its words and marks (ADR-112); 0.3 has no render, set section-04 is its first, and the verdict SPEC 6.3 asks for is the owner's. Criterion 1: no corpus record carries this id, because the type is written from the owner's image instruction of 2026-09-18 rather than from the ledger, so the count is the owner's to waive as ADR-057 did. Criterion 2 was run on paper in ADR-110, and its three reserved neighbours are named in BLOCK."
---

# 03-spec-overlay — PDP-DR SECTION TYPE, DRAFT

**The FEATURES mode of the owner's image instruction** (`~/Downloads/images prompt.txt`,
2026-09-18, ADR-110). One of six section types, for the images outside the product card's gallery;
`registry/pdp-dr-instruction.md`, *The section form*, carries the form and the law all six share.

The owner's rules for this mode, word for word:

```
- Depict the feature or problem described in the input
- Product is visible and clearly presented
- Icons, supporting symbols, and concise text overlays allowed
  (infographic-style, functional information only)
- Human faces allowed, but keep expressions neutral and contextual
```

It is the type the instruction's **feature image** was waiting for (ADR-106): a section image
whose block argues ONE named feature, which may carry one short line.

## PURPOSE
Show one named feature at work, as one realistic photograph of the product clearly presented —
in use wherever the feature acts on something — under a small functional drawn layer: the
feature's own mark, an icon, a figure, or one short tag in the page's own words. It answers *"what
does this do to the thing it is for"*. The image sits beside its own HTML copy; the picture makes
that one feature line visible in three seconds.

## TRIGGER
use_when: >
  An LP2 image outside the product card's gallery whose section argues one named
  feature: an item of a features or modes block, a safety or quality block naming what
  the product is built with, any line whose claim is a part, a figure or a capability.
  It is also the type for a claim nobody can see and a camera cannot catch, drawn as
  its own mark over the product in use. Take 03-use-demo when the item is an act of
  the buyer's hands; 06-relief-after when the item is a benefit state a camera can
  catch; 03-mechanism-diagram when the item explains a process rather than shows a
  capability; 03-spec-macro, 03-spec-callout or 04-proof-stat for a gallery tile,
  which this type never fills.

## SKELETON
The section form since ADR-112: the owner's image instruction as it stands. Its Image_Type is this
type's mode and its Description the field's own page values; the prompt is one concise natural
paragraph with no labels, in this order. Each arrow names an entry below or in *The section form*.

```
TYPE: 03-spec-overlay v0.3 [overlay: mark | icon | figure | tag | callout | view]
Image_Type: FEATURES

  1. The register and the camera: "Editorial realism product feature image",
     the angle and distance, the real place the feature matters in.   -> PARTS/scene
  2. The product BY NAME, fully visible and clearly presented; on a seat
     of a clearly different tone where it is sat on.                   -> PARTS/product
  3. The feature at work: what it is doing, to what.                   -> PARTS/feature
  4. The drawn layer, in a sentence of its own: what is drawn, what it
     lands on, and that it is bold and large enough to read on a phone. -> MARKS/overlay
  5. The words: the page's own tag, set once, large and bold, on a plain
     ground of the opposite value, in the middle of the picture.       -> SLOT CONSTRAINTS
  6. The light and the instruction's tone.
  7. G1 in one sentence: "Use the attached product photo as the exact reference."
```

## PARTS

**`scene`** — the place the feature matters in, named so that it carries no signage (ADR-109:
2 of 6 frames brought shop signs or labelled packaging into a frame whose only words were its
own line). A person appears where the feature acts on one; the expression is neutral and
contextual, as the owner's rule says, and never poses.

**`product`** — named as the page names it, placed and never described (G2). **Clearly presented**
is the owner's word and it is the difference from `06-relief-after`: here the product is the
subject, the nearest and sharpest thing in the frame. **Scale comes from the host**, never from a
share of the frame, and the prompt moves the camera: *shot close enough that the product reads
whole* (ADR-106; held 6 of 6 in `03-mechanism-signal`'s set 04). A thin product is framed on its
working end (ADR-109). **A seated product sits on a seat of a clearly different tone**, asked as a
relation, never as a colour: arm B of ADR-111 left the sentence out and 2 of its 3 seated frames put
the cushion on a black seat of its own tone, where arm A carried it 4 of 4 (ADR-112). A share of the
frame, 40–60%, is named only on a studio or a graphic ground, where nothing fixes the size.

**`feature`** — the one feature the item names, doing its work on the thing it is for. Where the
feature is a part, the camera shows that part in use; where it is a capacity or a rating, the
frame shows the thing in use that the figure is about: a hold on a joint that is holding, a size
beside the hand that holds it (ADR-109).

## MARKS

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `overlay` | a parameter, and the item's line picks it. `mark`: the invisible thing in its OWN form — sound as notes or a spoken bubble, a frequency as a chart keyed to what it targets, a lure as the paths the insects fly, a signal as the known symbol a buyer already reads. `icon`: one to three plain supporting symbols beside the product. `figure`: the page's figure with its unit. `tag`: two to five words naming the feature. `callout`: up to three labels on thin leaders, each ending ON its part. `view`: an inset shaped like the optic, showing what the user sees | the session lock's one accent, or luminous blue for a working signal (G3); never red, never a flat green | one form to a frame, and the one short line beside it | the owner's twelve feature frames: the mark is the thing itself 12 of 12, lands on or inside the subject 8 of 12, a generic glowing arc 0 of 12, words in frame 10 of 12, a sentence 0 of 12 (ADR-106) · `03-mechanism-signal` set 04: one short line spelled right 3 of 3, the view on a product's own screen 1 of 1 · this type's first three renders: `section-02`, under KNOWN-FLAKY |

- **The mark LANDS on the subject the feature acts on** and never floats beside the product
  touching nothing; it never covers the product's own face or repaints it (ADR-094, ADR-106).
- **Never along a cable**: a mark drawn along a wire became the wire 2 of 2 (ADR-109).
- **A mark that asserts a relation — level, straight, aligned — is drawn where the frame makes it
  true** (ADR-109). A driving posture puts the knees above the hips, and a level line over those
  thighs came back false in both rounds, 2 of 2. Draw it where the frame can hold it: along the
  product's own top surface, which stays level on a sloping seat.
- **Never a hole in a thing the buyer owns** (ADR-109): where the inside matters, the `view`
  inset, the product's own screen, or a real opened state the object has.
- Bold with a clean edge, never thin and flat and never a soft edgeless glow; no bars and no
  readings drawn on a mark (A15, G6).

## SLOT CONSTRAINTS
- **One frame, one feature.** A block of three items is three frames, each on its own item's
  line, differing on a dimension each prompt names (`mapping/pdp-dr-rules.md`, rule 10).
- **Words: the feature image's one short line, and nothing else** (ADR-106) — a figure with its
  unit as the page states it (`badge` slot), and/or a tag of two to five words in the page's own
  words (`title` slot), and the one-to-three-word labels an icon row, a chart or a call-out
  needs. Never a sentence, never a second line, never a brand or a price, never a superlative or a
  verdict word the page does not supply (the instruction's text section). G16 binds both slots.
  The tag is set once, large and bold, on a plain ground of the opposite value, sized for a phone
  (*The section form*, *Words and marks on a phone*). A feature that needs no naming carries no
  words.
- **A drawn figure must be true of the frame it sits in** (ADR-109): a distance, a time or a
  count matches what the frame draws, or the figure stays in the page's HTML.
- **A certification, award, rating, press or platform mark** only where `content.json` names it
  (ADR-095).
- **Any screen at the far end** names its device and shows a picture, never interface text,
  notifications, bars or numbers (G6; `03-mechanism-signal` lost this 5 times).
- **G13 binds**, casting follows the namespace, and a block that names a person shows no face.
- **Ratio** never goes into the prompt (ADR-016); the owner renders the field at the frame its
  template shows (*The section form*, *The frame*).

## NEGATIVE
```
[G6] + a sentence of copy, a second line of words, a marketing word, a mark floating beside the
product and touching nothing, a mark painted on the product, a mark running along a cable,
a generic glowing arc where the thing has a form of its own, red or green marks,
bars or readings on a mark, a hole cut in anything the buyer owns, a figure that contradicts
the frame, the product small or far off, the product enlarged against the hand or body beside it,
the product set out on display with nobody using it, a well-known brand's product or wordmark,
shop signs or labelled packaging in the background, a soft edgeless glow
```

## BLOCK
**Criterion 3: two rounds, and 0.3 is what they left.** Set `section-02` wrote the owner's page v17
in 0.1's form, and the owner failed it on quality against the instruction (ADR-111). Set
`section-03` wrote the same fields by the instruction as it stands, images 3 to 5 here, and the
owner's word narrowed to the size of the drawn words and marks; the harness graded them partial,
fail and partial (ADR-112). 0.3 is the instruction as it stands plus what the two rounds earned. It
has no render: `sets/section-04/` is its first, and the verdict SPEC §6.3 asks for is the owner's.

**Criterion 1 cannot be met from the ledger as it stands**: no corpus record carries this id. The
type comes from the owner's tested instruction, so the count is the owner's to waive, as ADR-057
waived it for `03-spec-macro`.

**Criterion 2, run on paper in ADR-110**: of the four templates' fields this type takes the
`features.*` and `modes.*` items that are not an act and not a photographable state, and
`safety.image`. It contests no gallery tile. **Three reserved drafts share its ground and are the
open question**: `03-mechanism-signal`, `04-proof-stat` and `03-spec-callout`, the three
constructions ADR-106 sorted the owner's feature frames into. Here each is an overlay FORM, a
parameter, on the absorption ladder's first rung. Whether the three retire into this type is not
decided: the owner failed every render of `03-mechanism-signal`'s sets 01, 02 and 04, and this
type's first set is the evidence that decision waits for.

## KNOWN-FLAKY
Single observations; what recurred across both rounds is written into 0.3, and the rest waits here.

- **Set `section-02`, image 3** (harness pass). The words set once and spelled right, the leader
  ending on the joint, and the one frame of seven whose cushion carried the reference's ribbed back
  and two-tone shell. Book covers in the background carried pseudo-lettering, and the room was beige:
  92% of its saturated pixels in the orange band (`scripts/frame-colour.py`).
- **Image 4** (harness fail). The words drawn twice — *Raises Hips* in the window and *Raises Hips
  Level* above the thighs; a cobalt outline traced around the whole cushion, never asked for and
  barred by the namespace's accent law; and a level line over thighs that sloped down from knee to
  hip, after the sentence putting the body level had been cut to meet the 1,200-character gate.
- **Image 5** (harness partial). The words once and right, but the claim did not read: he was still
  on the cushion's front edge, so nothing showed it staying put; his other hand rested at his lower
  back as he rose, a pain cue on a relief-side frame; and the cushion's face came back light grey,
  the reverse of the reference.

- **Set `section-03`, images 3–5** (the instruction as it stands). The owner: *"chữ và các yếu tố
  đồ hoạ cần to rõ ràng hơn. mobile first"* — and `scripts/text-size.py` agrees on every
  frame: the tags' capitals 9.6, 8.4 and 14 px on a 390-px phone against 18, the lines 1.2 and
  2.4 px against 3, and image 3's white tag on a pale wall at 2.7:1. The prompts had asked for a
  *concise text overlay*, a *thin* pointer line and a *small* grip icon, and got exactly those.
- **Image 4** (harness fail): the level line lay over thighs sloping down from knee to hip
  again, 2 of 2 across both arms, and the cushion sat on a black seat of its own tone.
- **Image 5** (harness partial): the claim read — a hand pressing, the cushion still — but the
  icon sat at the left edge, in the band a square field's crop removes (a 1,200 × 896 render).

## CHANGELOG
- 0.3 (2026-09-18): the skeleton is the owner's image instruction as it stands, arm B of ADR-111,
  with G1 in one sentence (ADR-112). The two rounds' earned clauses are written in.
- 0.2 (2026-09-18): first render — set `section-02`, the owner's page v17 — failed by the owner on
  quality against the instruction (ADR-111). No clause added: the harness's observations wait in
  KNOWN-FLAKY while `section-03` tests the instruction as written against this form.
- 0.1 (2026-09-18): drafted from the owner's image instruction, the FEATURES mode, with the
  section form as its skeleton and ADR-106's feature-image law as its words (ADR-110). New device
  `overlay`. No render.

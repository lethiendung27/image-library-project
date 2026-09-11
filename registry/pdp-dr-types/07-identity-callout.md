---
id: 07-identity-callout
step: 7
job: identity
device: callout
version: "0.2"
status: deprecated
replaced_by: 03-spec-callout
ratios: ["1:1", "4:3"]
channels: [landing-page, marketplace]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [title, copy, badge]
variants: []
exempt_from: [G7]
pairs_with: []
never_with: []
avoid_adjacent: [03-spec-callout, 07-identity-pack]
requires_pair: null
blocked_by: null
---

# 07-identity-callout — RETIRED, replaced by 03-spec-callout

Promotion status (2026-09-10): **5 distinct sources on paper — and the count is the problem,
not the achievement.**

| source | frame | is it this device? |
|---|---|---|
| pendulum-cravings | capsule bottle centred; gold shield upper right, three labelled pill graphics at the left | **yes** — satellites around the object |
| trybello-hairspray | pump bottle on petals; scalloped seal upper left, three line-icon circles down the right | **yes** — satellites around the object |
| feicemat-v2 | neck device on a glass disc; two-line headline at the left, three ticked claims below it | no — that is `06-relief-claimstack`'s layout with the product as subject |
| lp3-12northfold-washno1 | one capsule centred; serif headline above, sans support line below | no — `07-identity-pack` with a text layer |
| lp3-12northfold-washno1 | carton and bottle side by side; two-line headline above | no — `07-identity-pack` with a text layer |
| lp3-7-redpine-tileno40 | tub with lid propped, one chew at its foot; one white rounded badge upper right | no — a packshot carrying one badge |

**Two of six.** Criterion 1 counts distinct sources and this proposal has five of them; what it
does not have is five frames making the same argument. `ADR-065` met this exactly once before
and wrote the remedy into `07-identity-inhand`: *the first job is re-filing rather than
hunting*, and **a batch summary naming a pattern three times is not a count.** This file is
that sentence applied a second time, and it is the reason the type is reserved rather than
drafted at five.

**One source is already spoken for.** `feicemat-v2` sits in `03-spec-callout`'s own founding
table — a different frame from the same page, filed as four labelled mode thumbnails with no
leaders. Two types drawing from one page is not itself a fault; two types that cannot be told
apart drawing from one page is, and that is criterion 2 stated as a fact rather than as a risk.

## PURPOSE
Argue what the object IS by ringing it with the marks that identify it — an origin, a seal, a
format, a count — each sitting on empty ground beside the part or the fact it names. Job 7 is
not a Trust Ladder rung (`vocabulary.yaml`, ADR-065): this frame answers *what is this thing*,
and it stops there. It never argues that the thing works.

## TRIGGER
use_when: >
  The gallery has already shown the pack and the buyer's next question is what the
  object is certified as, made of, or counted in — not what it does. A gallery tile
  after the packshot, a marketplace tile that must carry an origin or a format at
  thumbnail size. Choose 03-spec-callout when the labels name PARTS and what they do,
  which is a spec argument and a different job under SPEC 3.1. Choose
  06-relief-claimstack when a headline and stacked claim lines fill one side of the
  frame — that is a layout, not a ring of satellites. Choose 07-identity-pack when the
  words are a headline over the product rather than marks placed around it. NEVER for
  a slot whose copy argues a symptom, a mechanism, a comparison or a result.

## SKELETON
```
TYPE: 07-identity-callout v0.1
REGISTER: commercial product photograph. One frame, no panels, no insets.

[PRODUCT REFERENCE]  the attached photo is the exact reference.   -> G1
[PRESENTATION]       the object centred, taking 40-60% of frame.  -> 03-spec-callout PARTS/presentation
[SETTING]            one quiet ground the satellites can live on. -> 03-spec-callout PARTS/setting
[LIGHT]              broad and even; nothing a mark names is dark.
[SATELLITES]         two to four marks, each on empty ground,
                     each nearest the fact it names.              -> MARKS

[TITLE]              what the object is, in the reader's words. Optional. -> G16/title
```

**The skeleton is deliberately thin and it stays thin until a render fails.** This library's
own rule is that a clause belongs in a prompt only where a render failed without it; this type
has no renders, so every line above is either G1, a call into a sibling type's measured part,
or a count taken from the two frames that actually are this device. Nothing here is invented
craft advice.

## PARTS

**`presentation`, `setting`** — called from `03-spec-callout`, not restated. That type measured
its 40–60% band and its quiet-ground correction against 119 corpus frames (ADR-068) and the
geometry is the same geometry. **If that file moves, this call goes stale** — the namespace
carries no copy and no drift instrument, by design (see `registry/pdp-dr-instruction.md`).

**`satellites`** — **two to four**, against `03-spec-callout`'s three to six. The lower ceiling
is not a style preference: an identity mark is read at thumbnail size on a marketplace tile,
and the two real exemplars carry three and four. Above four the frame stops being an identity
tile and becomes a spec tile, which is the other type.

## MARKS
This type owns its own mark library (ADR-012) and it is **not written yet**, because the two
real exemplars carry the two mark classes this repo has refused to legislate:

- a **gold shield** reading *number one GI doctor recommended* — a named-profession endorsement;
- a **scalloped seal** reading *dermatologist approved* around a caduceus — the same;
- and in a third frame, *MANUFACTURED IN THE USA* over a flag — an origin claim.

G16's two LAW rows stand over all three: a named-person or named-profession endorsement is what
G14 calls illegal, and a certification or press mark is the trademark question the owner
declined on 2026-08-18. **A mark library written now would legislate the one thing the type is
not allowed to draw**, so it is not written. What is left after those are removed — a format
count, a net weight, a capsule count — runs straight into `A15`, because a number set legibly
on or beside an object is a claim the frame cannot substantiate, and `07-identity-pack`'s own
founding render produced exactly that fault unprompted.

## SLOT CONSTRAINTS
- **G1 is load-bearing** for the same reason it is in `03-spec-callout`: a mark placed beside a
  redesigned object is a claim about a thing that does not exist.
- **G16 governs every word.** A title plus four satellites is five clusters, which is the count
  G16's founding rounds actually measured rather than the eight `03-spec-callout` proved later.
- **G7 exemption, narrow** — an object arranged on plain ground to be annotated exists to be
  photographed. Arrangement only, per G7's scope as amended by ADR-064.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a person, a hand, a room with objects in it, a second product,
a certification seal, an award, a rating, a press mark, a named profession,
a claim about what the product does, more than four satellites,
a leader line carrying a reading order between satellites
```

## RETIRED — 2026-09-11

**This type is deprecated and replaced by `03-spec-callout`.** It is kept rather than deleted
because the ledger carries six observations under this id and a reader has to be able to follow
them.

**The question was answered from two directions on the same day, and both said the same thing.**

**A render answered it.** Set `clip-fan-01` declared this type its CONTROL and predicted, before
the render, that it would come back indistinguishable from `03-spec-callout` — because with the
style lock in force ground, light, grade, type and accent were identical between the two prompts,
leaving only the argument to tell them apart. It came back indistinguishable. That is the
router-confusion evidence this file's `blocked_by` was waiting for, arriving from a render
instead of from an argument.

**And a corpus answered it.** The 157-image drop of 2026-09-11 put `03-spec-callout` at ten
distinct sources and found not one new frame for this id. `hydrovia` img-04 is the test case:
five labelled pills ringing a bottle, naming *Stainless Steel*, *Durable Glass Body*, *USB
Rechargeable* — materials and capabilities, which is what `03-spec-callout`'s own `use_when`
claims. It filed there without difficulty.

**What the original file said, which stands as the reason.** Six observations across five
sources cleared criterion 1 on paper; re-reading the breakdowns, only two were unambiguously
this device and the other four read as `06-relief-claimstack`, as `07-identity-pack` with a text
layer, or as a badge on a packshot. The count was never the evidence.

**The two blockers behind it are not resolved and do not need to be.** G16's two LAW rows still
refuse a named-profession endorsement and a certification mark, which were three of the six
exemplars' only marks; and `A15` still has no rule for where a figure in a frame comes from.
Both now bind `03-spec-callout` instead, where they belong.

## KNOWN-FLAKY
- **Nothing observed.** No prompt has been written from this file and no render exists. Every
  clause above is a proposal, which is the state ADR-065 named for a staging draft and the only
  honest label for a file one day old.

## CHANGELOG
- 0.2 (2026-09-11): **RETIRED**, `status: deprecated`, `replaced_by: 03-spec-callout`.
  Answered from two directions on one day — clip-fan-01's control render came back
  indistinguishable from a `03-spec-callout` prompt under an identical style lock, and the
  157-image drop put that type at ten distinct sources while finding not one new frame for
  this id. `BLOCK` becomes `RETIRED`; the file is kept because the ledger carries six
  observations under this id. ADR-078.
- 0.1 (2026-09-10): drafted from six observations across five distinct sources in batches
  2026-09-03-C, D, F and H. Filed reserved rather than at criterion 1, because re-reading the
  breakdowns puts four of the six with other types — the `07-identity-inhand` finding of
  ADR-065 arriving a second time. Job `identity` with the existing device `callout`; no
  vocabulary addition. First file of the `registry/pdp-dr-types/` namespace to be written
  rather than moved. ADR-077.

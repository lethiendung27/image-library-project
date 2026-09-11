---
id: 04-proof-stat
step: 4
job: proof
device: stat
version: "0.1"
status: reserved
replaced_by: null
channels: [landing-page]
requires_product_photo: false
generation_mode: single-pass
axes: {}
text_layer: [title, copy, badge]
variants: []
exempt_from: [G7]
pairs_with: []
never_with: []
avoid_adjacent: [06-relief-claimstack]
requires_pair: null
blocked_by: "A15 and the owner substantiation decision behind it. A skeleton has to say where the number comes from, and no rule in this repo does. ADR-066 blocked this proposal by name on 2026-09-03 and nothing has moved since."
---

# 04-proof-stat — PDP-DR DRAFT

Promotion status (2026-09-10): **4 observations, 4 distinct sources. Criterion 1 not met, and
that is the LEAST of what is wrong with promoting it.**

| source | the figure | what stood behind it in the frame |
|---|---|---|
| lp3-7-redpine-tileno40 | 89% seeing results after ninety days | **a footnote naming a September 2025 survey, n=307** |
| pendulum-cravings | 91% and 88% craving reduction | a consumer survey, 274 participants, six weeks |
| trybello-hairspray | 73%, 88.9% and a third, in donut charts | an asterisk, and no footnote anywhere in the frame |
| neuaura-achefree | three percentages beside a portrait | **nothing at all** |

**The direction is the finding, and it is already law.** `argument-faults.md` A15 measured this
degradation across seven frames in five sources and filed it as an argument fault rather than a
style note: *a statistic set into an image reads as verified; nothing in the picture verifies
it, the reader cannot check it, and the file outlives the page that could have.*

**One frame in the whole corpus does it correctly** and is the shape any rule would have to
legislate: a women's multivitamin tile naming a third-party consumer perception study — 31
women aged 18+, two capsules daily for twelve weeks — set in the frame beside the claims it
supports (`sha256:8e885077254e2…`).

## PURPOSE
Make one measured figure the subject of the frame, with its source set beside it, so a sceptic
can see both at once. The argument is not that the number is large; it is that somebody
counted, and that the counting is named where the number is.

## TRIGGER
use_when: >
  NOT YET ROUTABLE — see BLOCK. When it is: the proof beat of a product page where
  content.json carries BOTH a figure and its source, and the buyer's doubt is whether
  anyone has measured the claim. Choose 04-proof-lockedframe when the proof is
  something the reader can watch happen; that type shows, this one cites. Choose
  06-relief-claimstack when the frame's words are benefit claims rather than one
  measured figure with an attribution.

## SKELETON
**There is no skeleton and that is the decision, not an omission.** ADR-066 stated the reason
in one line and it has not changed: *none of them can be given a skeleton, because a skeleton
has to say where the number comes from and no rule in this repo does.*

What a skeleton would have to legislate, written down so the eventual one is not re-derived:

```
TYPE: 04-proof-stat v0.1                                  [NOT WRITTEN]

[FIGURE]        the one number, large. From content.json, never composed.
[WHAT IT SAYS]  the claim the number is about, in the reader's words.
[SOURCE]        who measured, how many, over how long — IN THE FRAME,
                set beside the figure and not in a footnote the crop can lose.
[GROUND]        quiet: light, close to neutral.        -> ADR-068
```

**Two shapes are already known to fail and neither needs a render to know it.**

- **A chart.** Three of the four exemplars draw the figure as a donut or a ring. This library
  has measured what happens when a renderer is given a chart idiom: N shapes each bigger than
  the last came back as a bar chart 5 of 5, and the remedy was to ask for ONE tapering shape.
  A percentage does not need a chart at all — the numeral is the picture.
- **A figure with no source.** Two of the four exemplars carry none, and one of those carries
  two decimal places, which is precision standing in for provenance. A15's working position is
  narrow and it is the whole of what this type may do: **a figure enters a frame only where
  `content.json` carries the figure AND its source, and the source is set beside it.**

## SLOT CONSTRAINTS
- **G16 governs every word**, and the source line is the one that must survive the mobile
  floor. G16's round 3 measured four instruments at text size and all four failed; the lever it
  named as untried is **fewer words**, and a source line is where a writer will be tempted to
  spend them.
- **G14 is engaged whenever the figure is an endorsement percentage** — *91% of users
  recommend* is a claim about people, and if the slot sits beside names, avatars, a star row or
  a review count it takes a real customer photograph or it takes nothing.
- **A15 binds twice.** Once on the text layer, which this type is entirely made of, and once on
  anything printed on an object in frame — `07-identity-pack`'s founding render wrote
  `NET WT. 8 OZ (227g)` onto a pouch unprompted, and the better the lettering renders the less
  anything in the frame says the number is invented.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a donut chart, a ring chart, a bar, a pie, a gauge, a graded row of shapes,
a percentage with no source in the same frame, a decimal place,
an asterisk with no footnote, a person, a product
```

## BLOCK
**Waiting on the owner's substantiation decision**, named in `argument-faults.md` A15 and in
ADR-066 §4. A15 is deliberate about what it does and does not decide: it names the fault,
measures it, and states a narrow working position; **what it does not do is bind the library by
law, because a rule about what claims may be printed is a commercial and regulatory decision
rather than a craft one, and it is the owner's.**

Three proposals are blocked behind that one decision — this file, `04-proof-instrument` and
`04-proof-interface`. `04-proof-interface` carries 8 observations from a single source and is
not drafted here for that reason; it is the largest observation count in this corpus with the
smallest source count, which is what a single page's gallery looks like in a ledger.

**What would unblock it.** A rule saying where a figure comes from and what must sit beside it.
The one corpus frame that does it right is the shape to legislate from.

## KNOWN-FLAKY
- **Nothing observed.** No prompt, no render. The two failure shapes above are transferred from
  measurements taken elsewhere in this repo, not from this type — and a rule measured on one
  corpus does not govern another until it is re-measured here.

## CHANGELOG
- 0.1 (2026-09-10): drafted from four observations across four distinct sources in batches
  2026-09-03-C, D, F and G. Filed reserved with NO SKELETON, which is the state ADR-066 §4 put
  this proposal in on 2026-09-03 and the honest carry-over of it. New device value `stat`.
  ADR-077.

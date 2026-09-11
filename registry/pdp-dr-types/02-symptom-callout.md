---
id: 02-symptom-callout
step: 2
job: symptom
device: callout
version: "0.1"
status: reserved
replaced_by: null
ratios: ["1:1", "4:3"]
channels: [landing-page, advertorial]
requires_product_photo: false
generation_mode: single-pass
axes:
  register: [commercial]
text_layer: [title, copy]
variants: []
exempt_from: [G4]
pairs_with: []
never_with: []
avoid_adjacent: [02-symptom-rail, 03-spec-callout]
requires_pair: null
blocked_by: "Criterion 1 by two sources — three of five — and criterion 2, the router-confusion test against 02-symptom-rail, which argues the same beat with a different geometry."
---

# 02-symptom-callout — PDP-DR DRAFT

Promotion status (2026-09-11): **3 distinct sources.** ADR-066 renamed this proposal from
`02-symptom-halo`, recorded it at two, and said in as many words that it *"gets no file until
it has three."* It has three, so this is that file.

| source | the subject at the centre | the satellites |
|---|---|---|
| hydroh-adv1 | a body | eight magnified complaints on leader lines |
| lp3-7-redpine-tileno40 | an animal | symptoms ringing the subject on a drawn circle |
| glowy-liff | a woman holding the product | eight photographic complaint vignettes, **no leaders at all** |

Criterion 1 needs two more sources. Criterion 2 is unrun. Criterion 3 has no render.
**Not routable.**

## PURPOSE
Widen a problem across complaints by ringing one subject with the things that go wrong. The
reader finds their own complaint somewhere in the ring, which is what makes the tile work: it
does not name the reader's problem, it offers eight and lets them pick.

## TRIGGER
use_when: >
  The page's problem is not one pain but a SPREAD of them, and no single frame could carry
  the breadth — dryness across skin, nose, throat and sleep; damp across mould, clothes,
  condensation and wood; ageing across eyes, pores, lines and tone. The problem-agitation
  beat of a product page or an advertorial. Choose 02-symptom-rail when the complaints run as
  a BAND with a hero photograph rather than ringing a subject: a rail lists, a ring surrounds.
  Choose 03-spec-callout when the satellites name parts of a PRODUCT — that is a different job
  and SPEC 3.1 makes two jobs two types however alike the picture.

## SKELETON
```
TYPE: 02-symptom-callout v0.1
REGISTER: commercial photography. One frame, no panels.

[SUBJECT]     one body, or one person, at the centre.        -> PARTS/subject
[SETTING]     a quiet ground the satellites can live on.     -> PARTS/setting
[LIGHT]       broad and even; nothing a satellite names is dark.
[SATELLITES]  four to eight complaints, each nearest the place it concerns. -> PARTS/satellites

[TITLE]       the question the ring answers.                 -> G16/title
```

## PARTS

**`subject`** — one body, one person, or one animal, at the centre, occupying 30–45% of the
frame so the ring has room. The subject is NOT the product: this is a step-2 tile and the
product has not been introduced yet. `glowy-liff` puts the product in the subject's hand,
which weakens the tile — see KNOWN-FLAKY.

**`setting`** — a quiet ground: light in value, close to neutral in colour (ADR-068). The
satellites are the content and a busy ground competes with eight of them at once.

**`satellites`** — **four to eight**, each a short label, each sitting nearest the part of the
subject it concerns. Counted: eight, eight, and a ring of symptom names. Above eight nothing
is legible at tile size; below four the tile is not arguing breadth and a rail would do.

**What joins a satellite to its place is a PARAMETER**, exactly as ADR-066 legislated for the
spec-job sibling. Three forms are observed here: a leader line, a drawn circle, and **nothing
at all** — `glowy-liff` places eight vignettes with no leaders and lets proximity do the work.

**A satellite may be a LABEL or a PHOTOGRAPH.** `hydroh-adv1` magnifies the complaint;
`glowy-liff` shows a stock vignette of it. The photographic form is stronger and is the one
worth writing a skeleton around, because a named complaint is an assertion and a photographed
one is at least a depiction.

## SLOT CONSTRAINTS
- **G11 is this type's best instrument and two of three sources leave it on the table.**
  `clou-diaxi`'s symptom RAIL desaturates everything but the afflicted area, so the eye lands
  on the complaint without a leader. Neither of this type's photographic sources does it. A
  founding round should test the spot-tint ring against the flat-colour ring.
- **A3 binds every satellite.** The effect must be LOCATABLE: a satellite that names something
  with no place on the subject has nothing to sit nearest to, and the ring's whole geometry
  fails for that one. `clou-diaxi`'s rail already showed this failing with a mood — "Be
  depressed" cannot be tinted because nothing about it is anywhere.
- **G9 outranks expression.** A performed grimace is not evidence; the complaint itself is.
  Where a satellite shows a person, it shows the physical fact rather than a reaction to it.
- **G4 is exempt**, declared: there is no correct side in frame. This is a problem tile.
- **No product claim anywhere.** The tile argues the problem and stops. A satellite naming a
  benefit turns it into a claim stack.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + the product, packaging, a benefit claim, a solution, a brand mark,
more than eight satellites, a satellite naming something with no place on the
subject, a performed grimace, a tearful face, a clinical setting, a uniform,
red used anywhere except on the afflicted area
```

## BLOCK
**Waiting on two more distinct sources for criterion 1, and on criterion 2 against
`02-symptom-rail`.** Both types argue the same beat — widening a problem across complaints —
and differ only in geometry: a rail LISTS complaints in a band beside a hero, a ring
SURROUNDS a subject with them. That sentence is in both files' `use_when` and has never been
tested against a router.

The rail stands at 4 distinct sources on this corpus and this at 3, so a promotion decision
will have to take them together rather than separately.

**Criterion 3 has no render.** No prompt has been written from this file.

## KNOWN-FLAKY
- **Nothing observed.** No prompt and no render exist for this file.
- One fault is already visible in the corpus and is recorded rather than legislated:
  `glowy-liff` rings a SMILING, unafflicted woman holding the product with eight complaints,
  so the tile's own subject contradicts its headline. The subject of a symptom ring should
  carry the state the ring is about, or carry nothing — and it should not carry the product,
  which has not been introduced at this beat.

## CHANGELOG
- 0.1 (2026-09-11): drafted from three observations across three distinct sources — two
  carried in the ledger under the old id `02-symptom-halo`, renamed by ADR-066, and one from
  batch 2026-09-11-D. This is the file ADR-066 deferred with the words *"gets no file until it
  has three"*. Job `symptom` with the existing device `callout`; no vocabulary addition.
  Raised and evidenced by `_CURATION-2026-09-11.md`. ADR-078.

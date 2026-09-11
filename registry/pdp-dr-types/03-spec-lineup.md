---
id: 03-spec-lineup
step: 3
job: spec
device: lineup
version: "0.1"
status: reserved
replaced_by: null
channels: [landing-page, marketplace]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [title, badge]
variants: []
exempt_from: [G7]
pairs_with: []
never_with: []
avoid_adjacent: [03-use-grid, 05-persona-grid]
requires_pair: null
blocked_by: "Three more distinct sources - 2 of 5 today. Criterion 3 is met at partial with the owner's verdict outstanding."
---

# 03-spec-lineup — STAGING DRAFT

Promotion status (2026-09-03): **2/5 exemplars** — `sha256:a8d80295d82a894…` (three carded
sock packs fanned in front of a model on a white knockout) and `sha256:9ac921bdaaa02fa…`
(five coffee pouches in a shallow arc on a pale gradient, two made drinks among them).
Criterion 3 now MET at `partial` — one render, owner-verdict pending. Not routable. Device
`lineup` is new vocabulary and ships in the same diff.

## PURPOSE
Argue breadth of choice by putting the range in ONE frame as a physical lineup. The claim is
"there is a version of this for you", and it is made by the objects standing together rather
than by cells in a grid. One variable changes across the units and nothing else does.

## TRIGGER
use_when: >
  The product ships in several real variants — flavours, colourways, sizes, strengths
  — and the buyer's question is how wide the choice is. A gallery tile after the
  packshot, a variant tile beside a picker, or the closing tile of a range page. Use
  when the variants are genuinely different to look at, so the breadth is legible
  without reading a label. Choose 03-use-grid instead when the argument is that ONE
  unit does many jobs, and 05-persona-grid when the breadth is people rather than
  product.

## SKELETON
```
TYPE: 03-spec-lineup v0.1
REGISTER: commercial product photograph. One frame, no panels, no insets.

[PRODUCT REFERENCE]  the attached photo is the exact reference; every unit in
  the frame is that same product, identical in build.            -> G1
[LINEUP]             how many units, and how they stand.         -> PARTS/lineup
[VARIABLE]           the ONE thing that differs, named per unit.  -> PARTS/variable
[SETTING]            one plain ground the units sit on or against. -> PARTS/setting
[LIGHT]              one direction across the whole row.          -> PARTS/light

[TITLE]              the claim.                                   -> G16/title
[BADGE]              one short stamp. Bottom LEFT.                -> G16/badge
```

## PARTS

**`lineup`** — **three to five units.** Fewer than three does not read as a range; more than
five and each unit is too small to show its own difference. State how they stand: a straight
row square to the camera, a shallow arc with the centre unit nearest, or an overlapping fan.
One arrangement, named.

**At 1:1 the lineup is a PACK, not a stripe** — G15. Five units in a row across a square give
each a fifth of the width, which is the exact starvation G15 exists to prevent. At 1:1 take
three units in a shallow arc, or a 2-over-3 stack. The straight row belongs to 16:9.

**`variable`** — **exactly ONE thing differs across the units, and the prompt names each unit's
value.** Colour, or flavour, or size — never two at once. A lineup that changes colour AND size
argues nothing, because the reader cannot tell which axis the range runs along. The values come
from `product.attributes.colorways` and from `product.raw_features`, never invented: G2's
fabricated-colourway rule binds every unit in the frame at once, so this type multiplies the
cost of getting it wrong by the number of units.

**`setting`** — one plain ground, no room, no props, no second product class. A ground tone is a
runtime value (`parameters: environment`) and changes nothing about what the type is. A real
surface is legal where the category expects one; a real ROOM is not, because a room gives each
unit a different context and the comparison stops being clean.

**`light`** — one direction across the whole row, identical on every unit. **This is the type's
G5 equivalent:** if one unit is lit differently it reads as favoured, and a range image that
favours one variant has argued for that variant instead of for the range.

## SLOT CONSTRAINTS
- **G1 gains its multi-layer sentence and it is load-bearing here.** *The product must be
  identical in every layer of this image* becomes *identical in every unit except the named
  variable*. `adapters/nano-banana.md` Rule 5 names multi-region consistency as the hardest
  thing this renderer holds in one pass, and a five-unit lineup is five regions. Name the
  invariants BEFORE the units are described — the route `01-pain-split` records at 1 of 1.
- **No person.** A model holding the range is a different frame and it is
  `07-identity-inhand`'s: there the hand is a ruler, here the units are the argument. The sock
  exemplar has a person in it and that is the observation's deviation, not this type's law.
- **G7 exemption, narrow** — a row of units on a plain ground is an arrangement that exists
  only for the photograph. Covers the arrangement only.
- **G11 is not engaged**; no state is depicted. **G3 is not engaged**; each unit carries its own
  real colourway and no signal colour appears.
- **`avoid_adjacent`** both grid types: three breadth arguments on one page is a catalogue,
  not a page.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a person, a hand, a room, props between the units, a different
product class in the row, one unit lit or angled differently from the rest,
a unit in a colourway the product does not really have, reflections that
break at one unit, more than five units
```

## FOUNDING RENDER ROUND — 2026-09-03
One render, ratio 1:1, the carbide shaping pad attached. Verdict proposed **partial** (ADR-011).

**Count held: three units, evenly spaced, none overlapping, centre nearest.** The arc read as
asked and no fourth unit appeared — worth noting against `06-relief-hero`'s finding that a
drawn mark's stated COUNT does not survive. A count of physical objects is apparently not the
same problem as a count of drawn marks.

**The one-variable law BROKE, and it broke in the invariants rather than in the variable.**
The prompt's INVARIANTS block named "same mounting hub" first, before anything else was
described, which is the route `01-pain-split` records at 1 of 1. It did not hold: the three
units came back with visibly different hub bores — the left narrow, the centre wide, the right
between them. So the frame changes TWO things across the row, and a reader cannot tell which
axis the range runs along. That is the exact defect PARTS/variable exists to prevent.

**And only one of the two profile distinctions reads.** Left flat against centre domed is
clear at a glance; centre against right is not. Three profiles were asked for and two are
legible, which for a type whose whole argument is "there is a version for you" is half an
argument.

Text 3 of 3 exact, badge clean bottom LEFT, one light direction across all three units with no
unit favoured — the G5-equivalent clause held.

**What this changes.** Naming invariants first is necessary and not sufficient here. The next
round tests two units rather than three: if two hold identity, the risk is unit COUNT and the
type ships with a lower ceiling; if two also drift, the risk is multi-instance identity itself
and this argument belongs in a grid where each cell is its own frame.


## KNOWN-FLAKY
- **One render, verdict partial.** The count clause held; the one-variable clause did not.
- **Multi-unit identity is the biggest risk and the founding render CONFIRMED it**, on the
  hub rather than on the profile: the invariants block named "same mounting hub" first and the
  three units still came back with three different bores. If units drift on ≥2 of the next 3,
  the fallback is
  three units rather than five, and if that fails the argument goes back to a grid type where
  each cell is its own frame.
- **`sha256:a8d80295d82a894…` is cited by two proposals**, here and by `07-identity-inhand`.
  The boundary is the count — one unit presented is that type, several compared is this one —
  and curation should assign the observation to one rather than letting both count it.

## BLOCK
**Waiting on three more distinct sources** — two of five today, and the two are a sock page
and a coffee page. Criterion 3 is met at `partial` with the owner's verdict outstanding.

`lede-lineup` in `registry/toplist-types/` carries the SAME device name for a different
argument — several units of one product here, a field of rival makers there — and that
separation is recorded in ADR-069 rather than in either file.

## CHANGELOG
- 0.1 (2026-09-03): drafted from two hash-verified observations across two batches. Proposed
  in batch 2026-08-31-B as `03-spec-range`; renamed here because `lineup` names the visual
  mechanism — units standing together — while `range` names the subject, and SPEC §3.1 makes
  the device the mechanism. New device value `lineup`.

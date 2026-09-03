---
id: 03-spec-callout
step: 3
job: spec
device: callout
version: "0.1"
status: reserved
replaced_by: null
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
avoid_adjacent: [03-spec-explode, 03-spec-macro]
requires_pair: null
---

# 03-spec-callout — STAGING DRAFT

Promotion status (2026-09-03): **5 distinct sources — criterion 1 CLEARED.**

| source | what it annotates |
|---|---|
| hume-band | a worn fitness band, three leader lines to short labels |
| trybello-hairspray | a bottle mid-spray, five icon roundels on right-angled leaders |
| neuaura-achefree | loose capsules, six ingredient roundels RINGING them on dashed leaders |
| feicemat-v2 | an LED device, four mode thumbnails at the corners, **no leaders at all** |
| snif-rect | a detector, four labels down one side plus one magnified circular inset |

Five sources across four verticals — wearables, personal care, supplements, consumer
electronics. Criterion 2 (router-confusion) UNRUN and criterion 3 (a rendered worked example)
UNMET. **Not routable.** Device `callout` is new vocabulary and ships in this diff.

**This file absorbs the `02-symptom-halo` proposal's LAYOUT and not its job.** That proposal
was raised on two observations of a subject ringed by labelled satellites — a dog ringed by
symptom names, an anatomical figure ringed by magnified joints. The feicemat frame settles
what they share: it places four labelled satellites around a central product **with no leader
lines**, so the leader is a parameter of the layout rather than its identity. What makes the
construction is a subject at the centre and labelled satellites around it. Halo and callout
are ONE DEVICE.

They are not one type. `02-symptom-halo`'s job is `symptom` — widening a problem across
complaints — and this type's job is `spec`. Under SPEC §3.1 two jobs are two types however
alike the picture, exactly as `split` already serves both `01-pain-split` and `03-spec-split`.
So the halo proposal survives, renamed `02-symptom-callout`, at 2 sources, sharing this
device. It gets no file until it has three.

## PURPOSE
Argue a specification by pinning claims to the places they belong. One product at the centre,
each claim attached to the part of it the claim is about. The reader learns what the object
does without reading a paragraph, because each fact has an address.

## TRIGGER
use_when: >
  The product's value is several distinct capabilities and the buyer needs to know
  which part does which. A gallery tile after the packshot, a spec tile beside a
  feature list, or the tile a page uses to replace a bulleted paragraph. Use when the
  claims genuinely belong to PLACES on the object — a sensor, a nozzle, a control, a
  chamber, an ingredient. Choose 03-spec-explode when the argument is what is inside;
  03-spec-macro when it is how one surface is made; and 06-relief-claimstack when the
  claims are about the buyer's life rather than about parts of the product.

## SKELETON
```
TYPE: 03-spec-callout v0.1
REGISTER: commercial product photograph. One frame, no panels, no insets.

[PRODUCT REFERENCE]  the attached photo is the exact reference.   -> G1
[PRESENTATION]       how the object sits, and how much frame it takes. -> PARTS/presentation
[SETTING]            one plain ground the callouts can live on.   -> PARTS/setting
[LIGHT]              even enough that every annotated part reads.  -> PARTS/light
[CALLOUTS]           where each label sits and what joins it.      -> PARTS/callouts

[TITLE]              the claim the whole frame makes. Optional.    -> G16/title
[BADGE]              one short stamp. Bottom LEFT. Optional.      -> MARKS
```

## PARTS

**`presentation`** — the object centred or slightly offset, occupying **40–60% of the frame**,
turned so every annotated part is visible at once. That band is the whole geometry of the
type: below it the parts stop reading, above it there is no ground left for the labels. Choose
the angle from what has to be labelled, never the reverse.

**`setting`** — a ground with room around the object for the labels to sit on, and **the
ground is chosen per product rather than defaulted**. A flat tone; a soft gradient; a heavily
blurred surface; a dark technical ground for a device whose argument is precision; a warm
material ground for something domestic. What is forbidden is a real room with objects in it —
a callout needs empty ground the way a text block does, and a room fills it — and what is
discouraged is reaching for pale grey every time. The corpus builds these on dark circuit
board, on warm beige, on flat blue and on pale lilac; four products, four grounds, one
construction.

**`light`** — broad and even. **This type cannot use dramatic light**, because a part in shadow
is a part whose label points at nothing. Where one annotated part needs separating, lift it
with a soft accent rather than by darkening its neighbours.

**`callouts`** — three to six, and this is the type's own count rule. Fewer than three is a
claim stack with a picture; more than six and each label is too small to read at tile size.
Each callout is **one short label, optionally with one simple line glyph**, and it sits on
empty ground.

**What joins a label to its part is a PARAMETER, not the identity.** Three forms, all observed:

- **leader line** — a thin line, straight or right-angled, from the label to the point it
  names. The most explicit and the most common.
- **ring** — the labels placed around the object with no line at all, each nearest the part it
  belongs to. Observed once, clean, and it is the observation that settled halo and callout as
  one device.
- **dashed leader** — the same as a leader line, drawn broken. A styling choice.

**Every label must point at something the frame actually shows.** A label naming a part that is
not visible is argument-fault A2 wearing a line: a mark states, it cannot suppose. Where a claim
has no place on the object — a warranty, a certification, a feeling — it does not belong in
this type at all.

**`inset`** — optional, at most ONE, a magnified circle joined to the object by a taper,
showing a part too small to read at product scale. Observed once. `06-relief-hero --detail`
legislates the same device for a different type at 30–40% of frame width and that band is the
starting point here, not a separate invention.

## MARKS

**A badge is a mark and this type owns its forms** (ADR-012, ADR-043, G16's badge note). The
skeleton calls `badge` by name; the prompt names WHICH form, and the choice is made per
product from what its register can carry. **Three forms minimum, and none of them is a
default** — six test prompts written before this section existed produced six identical flat
rectangles, which is the monotony that put this section here.

| form | shape | the register it belongs to |
|---|---|---|
| `tag` | a flat rectangle, square or lightly rounded, one flat fill, capitals cut out of it | technical, tools, anything that reads as engineered |
| `roundel` | a filled circle carrying a short figure or a two-word fact | a number that should feel like a stamp — a count, a rating, a spec |
| `chip` | a small line icon in a circle with one short label beneath it | a capability, where the icon does half the reading |
| `flash` | a corner triangle or ribbon crossing one corner of the frame | urgency and offers. **Carries the highest going-stale cost**, since what a flash usually says is a price or a date |

**One badge per frame.** Two stamps compete and neither is read.
**The badge sits bottom LEFT** — the generation tool's watermark holds the bottom-right corner
and struck through three of three badges placed there (`adapters/nano-banana.md` Rule 7).
**Untested on this type**: no render exists, so every form here is a proposal whose first
render is its founding evidence, the treatment ADR-012 gave a MARKS entry with nothing behind
it.

## SLOT CONSTRAINTS
- **G1 is load-bearing.** Every label is a claim about a real part, so a redesigned or
  invented feature makes every callout false at once. This type multiplies the cost of a bad
  reference by the number of labels.
- **The parts and their claims come from `product.specification` and `product.raw_features`
  and from nowhere else** — the same law those fields already carry for component names. A
  callout naming a sensor the product does not contain is not a bad render, it is a published
  claim on a part that does not exist.
- **G16 governs every word**, and this type carries more of them than any other in the
  registry: a title, up to six labels, and a badge. That is past the five-cluster budget the
  founding rounds measured, and **the count rule above is therefore provisional on G16**:
  if six labels will not hold, this type's ceiling is whatever does.
- **G7 exemption, narrow** — an object arranged on a plain ground for annotation exists only
  to be photographed. Covers the arrangement only, per G7's scope note as amended by ADR-064.
- **G3 is engaged more often than it is honoured**, and the corpus says so: four frames in one
  batch used colour for the product's own LED modes, for an improved audio signal, for
  corrected airflow and for an active sensing field. None is a signal in the library's sense.
  Where this type uses colour on a callout it uses ONE neutral, and where the product's own
  colours name its modes they are the product's, not marks.
- **G8 is not engaged** unless the product visibly emits; where it does, the emission is the
  subject and the callouts sit around it.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a person, a hand, a room with objects in it, a second product,
a label pointing at a part not visible in frame, more than six labels,
more than one magnified inset, arrows carrying a reading order between labels,
dramatic side light, a part in shadow
```

## KNOWN-FLAKY
- **No render exists.** Every clause is a proposal, including the 40–60% band and the three-to-
  six count, which are read off five market frames rather than measured on this library's own
  output.
- **Six labels is past the measured text budget.** G16's founding rounds hold five clusters;
  this type asks for up to eight. That is the first thing a render round should test, and until
  it is tested no prompt from this type should ship more than five.
- **The ring form has ONE observation.** If it fails, the type falls back to leader lines and
  the halo proposal's layout claim goes with it.
- **The inset has ONE observation** and borrows its geometry from another type.

## NOTES
**Boundary against the four nearest frames.** `03-spec-explode` separates the object into its
component groups; nothing is labelled and nothing is annotated. `03-spec-macro` magnifies one
surface to argue how it is made. `07-identity-callout` stamps ACCOLADES beside a product —
an award, a certification, a best-seller flag — which are claims about the product's standing
rather than about its parts, and which G16 refuses. `06-relief-claimstack` puts claims beside a
subject without attaching them to anything, and that is the real line: **a claim-stack claim is
about the buyer's life, a callout claim is about a place on the object.**

## CHANGELOG
- 0.1 (2026-09-03): drafted from five observations across five distinct sources and four
  verticals, gathered in batches 2026-09-03-E, F, G and H. Absorbs the LAYOUT of the
  `02-symptom-halo` proposal on the strength of the feicemat frame, which places labelled
  satellites with no leader line and so proves the leader is a parameter; that proposal keeps
  its `symptom` job, is renamed `02-symptom-callout`, and shares this device. New device value
  `callout`. ADR-066.

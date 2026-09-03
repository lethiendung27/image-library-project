---
id: 03-spec-callout
step: 3
job: spec
device: callout
version: "0.2"
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
electronics. Criterion 2 (router-confusion) UNRUN. **Criterion 3 has its renders** — two,
both examined, both graded by eye under ADR-011 — but §6.3(3) wants the OWNER's verdict and
that is outstanding. **Not routable.** Device `callout` is new vocabulary.

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
TYPE: 03-spec-callout v0.2
REGISTER: commercial product photograph. One frame, no panels, no insets.

[PRODUCT REFERENCE]  the attached photo is the exact reference.   -> G1
[PRESENTATION]       how the object sits, and how much frame it takes. -> PARTS/presentation
[SETTING]            one plain ground the callouts can live on.   -> PARTS/setting
[LIGHT]              even enough that every annotated part reads.  -> PARTS/light
[CALLOUTS]           where each label sits and what joins it.      -> PARTS/callouts

[TITLE]              the claim the whole frame makes. Optional.    -> G16/title
[BADGE]              one short stamp, in a named corner. Optional. -> MARKS
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
**Three corners are open and the bottom-right is not** — that one carries the generation
tool's watermark (`adapters/nano-banana.md` Rule 7). The founding round asked for `roundel`
upper right and `tag` lower left and got both, 2 of 2, so the corner is a per-product choice
rather than a constant.
**Tested: `roundel` and `tag`, 1 render each, both clean.** `chip` and `flash` have no render
and their first is their founding evidence, the treatment ADR-012 gave a MARKS entry with
nothing behind it.
**A badge is sized by the anchor and the anchor WORKS on a badge** — 0.51 and 0.59 of the
object named, against 0.24 and 0.23 for the headline in the same two frames. See FOUNDING
RENDER ROUND; the distinction now lives in G16.

## SLOT CONSTRAINTS
- **G1 is load-bearing.** Every label is a claim about a real part, so a redesigned or
  invented feature makes every callout false at once. This type multiplies the cost of a bad
  reference by the number of labels.
- **The parts and their claims come from `product.specification` and `product.raw_features`
  and from nowhere else** — the same law those fields already carry for component names. A
  callout naming a sensor the product does not contain is not a bad render, it is a published
  claim on a part that does not exist.
- **G16 governs every word**, and this type carries more of them than any other in the
  registry: a title, up to six labels, and a badge. That was past the five-cluster budget
  G16's own founding rounds measured, and the count rule was provisional on it. **It is no
  longer**: eight clusters were asked for and eight came back, once each. The band stands.
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

## WORKED EXAMPLES
### example: translation-earbuds-four-callouts — skeleton@0.1, run: partial
Four callouts, `roundel` badge upper right, dark technical ground. Six clusters asked and six returned, 7 of 7 lines exact. Two faults: the label written for the open lid has its leader on the case body, and the lower-right callout is abutted by the tool's watermark. `sha256:b135d5d6ffb72ba1…`

```
TYPE: 03-spec-callout v0.1
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the wireless translation
earbuds and case. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: the open case slightly left of centre, one earbud resting in it, the other standing
beside it turned so its outer face and inner contacts both show. Together about half the
picture's width.

SETTING: a dark charcoal ground with a faint cool sheen, empty on all four sides.

LIGHT: broad and frontal, soft enough that no part of either object falls into shadow.

CALLOUTS: four labels in flat white sans-serif on the empty ground, each joined to its part by
one thin white line:
outer face of the standing earbud — Tap it and it listens
inner face of the standing earbud — The mic that hears you first
the earbud in the case — Drops in, charges, forgets nothing
the open lid — Pocket-sized, so it comes with you

TEXT: across the top, two lines of white sans-serif, each starting the same distance from the
left edge as the upper-left label. Each capital is as tall as one earbud is long, so the
headline is the first thing read:
UNDERSTAND EACH OTHER
BEFORE THE SENTENCE ENDS
Each callout label is half the height of those capitals.

BADGE: UPPER RIGHT, overlapping nothing but the ground. A filled circle in a bright signal
green, as wide as the charging case, with a white line icon of two speech bubbles in its upper
half and TWO LANGUAGES in white capitals across its lower half.

Nothing comes within a tenth of the picture's width of any edge. The words above are the only
words in the picture; no logo, no watermark, no person, no room.
```

### example: electric-scissors-six-callouts — skeleton@0.1, run: partial
The cluster ceiling test — eight clusters against G16's measured five — and it held: 8 asked, 8 returned once each, 9 of 9 lines exact. Two faults: at six labels two leaders cross, and the badge sits 4.10% from the left edge against a 5.66% text block. `sha256:afb22a55516bc06b…`

```
TYPE: 03-spec-callout v0.1 — CLUSTER CEILING TEST
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the cordless electric
scissors. Preserve shape, proportions, material, finish and colour exactly.

SUBJECT: the scissors lying at a slight diagonal across the centre, blade upper right, grip
lower left, turned so blade, guard, trigger, switch and charging port all show. About half
the picture's width.

SETTING: a warm mid-brown worn workbench surface, softly out of focus, empty around the tool.

LIGHT: broad and even. No part in shadow.

CALLOUTS: six labels in flat cream sans-serif on the empty surface, each joined to its part
by one thin cream line, none touching another:
Cuts what scissors would fight · The guard your other hand thanks ·
One finger does the whole job · Slow for card, fast for fabric ·
Charges where your phone charges · Shaped for hands that ache after ten minutes

TEXT: across the top, two lines of cream sans-serif starting the same distance from the left
edge as the leftmost label. Each capital is as tall as the scissor blade is long:
YOUR HAND STOPS ACHING
HALFWAY THROUGH THE ROLL
Each callout label is half the height of those capitals.

BADGE: LOWER LEFT, a hard-edged rectangle in a hot signal red, as wide as the scissors' grip
is long, tilted a few degrees off square, with CORDLESS in white capitals filling it.

Nothing comes within a tenth of the picture's width of any edge. The words above are the only
words in the picture; no logo, no watermark, no person, no room.
```

## KNOWN-FLAKY
- **Eight clusters HELD and the ceiling worry is answered.** 8 asked, 8 returned, once each,
  nothing duplicated. The three-to-six count rule stands as drafted.
- **At six labels the leaders CROSS**, 1 of 1, and that is the real cost the count rule did
  not know about. Every label stayed legible; which label owned which line did not. At four
  labels nothing crossed. Six is legal and four is safe.
- **A leader can land beside the named part rather than on it**, 1 of 10 across the two
  renders: a label written for the open lid landed on the case body. That is A2 wearing a
  line — a mark states, and a leader that lands next door states something else.
- **The bottom-right corner has to be barred to every prompted element, not only a badge**,
  2 of 2. Both renders put a callout there and in both the watermark abuts the last word.
- **The ring form has ONE observation and still no render.** If it fails, the type falls back
  to leader lines and the halo proposal's layout claim goes with it.
- **The inset has ONE observation** and borrows its geometry from another type.
- **The 40–60% presentation band is still unmeasured** — neither render was measured against
  it, because nothing in either frame suggested it was the binding constraint.

## FOUNDING RENDER ROUND — 2026-09-03
Two renders, ratio 1:1, prompts 1 and 2 of `_staging/ready-to-push/prompts.md`. Both products
come from `query/product-slugs.yaml` and **neither appears in this type's source list** —
wireless translation earbuds at four callouts, cordless electric scissors at six. Verdicts by
eye under ADR-011; SPEC §6.3(3) still wants the owner's own.

| | 1 · earbuds, 4 callouts | 2 · scissors, 6 callouts |
|---|---|---|
| verdict by eye | **partial** | **partial** |
| clusters asked / returned | 6 / 6 | **8 / 8** |
| words exact | 7 of 7 lines | 9 of 9 lines |
| headline cap | 44 px = 4.30% of frame | 48 px = 4.69% |
| headline ÷ the object it was anchored to | **0.24** | **0.23** |
| badge form, corner asked / got | `roundel`, upper right / upper right | `tag`, lower left / lower left |
| badge fill | 2.96% of frame | 2.41% |
| badge ÷ the object it was anchored to | **0.51** | **0.59** |
| closest prompted ink to an edge | 5.37% text · 5.47% badge | 5.66% text · **4.10% badge** |
| output | `sha256:b135d5d6ffb72ba1…` | `sha256:afb22a55516bc06b…` |

**The ceiling test was the point of the round and it passed.** Prompt 2 asked for eight text
clusters — a two-line title, six labels and a badge — against the five G16's founding rounds
had measured. All eight came back once each, nothing duplicated and nothing dropped. This
type's own biggest risk is answered in its favour.

**What six labels costs is not legibility, it is ATTACHMENT.** Two leaders cross near the
grip in render 2, so which label owns which line stops being readable while every label stays
perfectly readable. Four labels crossed nothing. The count rule keeps its band and carries
the crossing.

**The size anchor split in two, and the split is the round's most useful finding.** The same
instrument — *as tall as / as wide as a named thing in the frame* — returned 0.51 and 0.59 on
the BADGE and 0.24 and 0.23 on the HEADLINE. A badge is an object and the renderer sizes an
object against another object; a capital is a glyph inside a type system, and the comparison
does not reach it. G16 carries the general form of this; what it means here is that the badge
clauses can be trusted and the headline clause cannot.

**The badge is where G10 breaks, not the text.** Render 2's `tag` came within 4.10% of the
left edge while its text block held 5.66%. Nothing was cut. A badge is placed and sized by
the prompt, so it goes exactly where it is told — including closer to the edge than the
renderer's own house margin would ever have put a line of type.

## NOTES
**Boundary against the four nearest frames.** `03-spec-explode` separates the object into its
component groups; nothing is labelled and nothing is annotated. `03-spec-macro` magnifies one
surface to argue how it is made. `07-identity-callout` stamps ACCOLADES beside a product —
an award, a certification, a best-seller flag — which are claims about the product's standing
rather than about its parts, and which G16 refuses. `06-relief-claimstack` puts claims beside a
subject without attaching them to anything, and that is the real line: **a claim-stack claim is
about the buyer's life, a callout claim is about a place on the object.**

## CHANGELOG
- 0.2 (2026-09-03): founding render round, 2 renders — `sha256:b135d5d6ffb72ba1…`,
  `sha256:afb22a55516bc06b…`. Eight clusters held 8/8, so the three-to-six count rule stops
  being provisional on G16. Leaders cross at six labels, 1/1 → KNOWN-FLAKY. MARKS: the
  bottom-left constant becomes three open corners, 2/2 obeyed; `roundel` and `tag` tested.
  The watermark corner is barred to every prompted element, 2/2.
- 0.1 (2026-09-03): drafted from five observations across five distinct sources and four
  verticals, gathered in batches 2026-09-03-E, F, G and H. Absorbs the LAYOUT of the
  `02-symptom-halo` proposal on the strength of the feicemat frame, which places labelled
  satellites with no leader line and so proves the leader is a parameter; that proposal keeps
  its `symptom` job, is renamed `02-symptom-callout`, and shares this device. New device value
  `callout`. ADR-066.

---
id: 03-spec-claimstack
step: 3
job: spec
device: claimstack
version: "0.1"
status: reserved
replaced_by: null
channels: [landing-page, marketplace]
requires_product_photo: true
generation_mode: single-pass
axes: {}
text_layer: [title, copy, badge]
variants: []
exempt_from: [G7]
pairs_with: []
never_with: []
avoid_adjacent: [06-relief-claimstack]
requires_pair: null
blocked_by: "Criterion 2, the router-confusion test against 06-relief-claimstack. The two are the same picture with a different job, both clear criterion 1, and that test has never been run. Criterion 3 has no render."
---

# 03-spec-claimstack — PDP-DR DRAFT

Promotion status (2026-09-11): **8 distinct sources — criterion 1 CLEARED.**
The most widely-sourced new cluster in the 157-image drop.

| source | the subject | the claims |
|---|---|---|
| clou-diaxi | the humidifier in a room, twice across two colourways | four icon-and-label features |
| fosen-ring | a woman wearing the device, cyan arcs at the contact rings | five intensity levels, three frequency modes |
| glowy-liff | a woman holding the wand, twice | five modalities as bare nouns; and a variant where **each claim carries a macro photograph** |
| hydrovia | the bottle bubbling, twice | three and four icon claims on a dotted connector |
| moisosat | a woman asleep, the product in a rainbow light arc | three icon claims |
| mozzapx | the solar panel at three ghosted angles | four figure-and-support pairs |
| pawdi-cas | the camera on a desk | four icon claims, **plus a compatibility bar of six third-party marks** |
| snapi-stud | the detector, four frames across two settings and two display types | three to six claims, one as a ticked checklist |

Criterion 2 is the binding gap and it is a real one. Criterion 3 has no render.
**Not routable.**

## PURPOSE
A subject holds one side of the frame and a headline with short claim lines fills the other,
and the claims name what the product IS or DOES — capabilities, settings, materials, modes.
The reader gets four or five facts in one glance without a paragraph. It is the workhorse
tile of a direct-response product gallery.

## TRIGGER
use_when: >
  The page needs one tile to carry several distinct FEATURES, and the features are short
  enough to name in three or four words each. A gallery tile after the packshot, a feature
  tile beside a spec block, or the tile a page uses to replace a bulleted paragraph.
  Choose 06-relief-claimstack when the claim lines describe a FELT STATE rather than a
  capability — energy, calm, comfort, a night's sleep — because that is a different job and
  SPEC 3.1 makes two jobs two types however alike the picture. Choose 03-spec-callout when
  the claims belong to PLACES on the object and can be pinned to them. Choose
  03-spec-dimension when the content is measurements.

## SKELETON
```
TYPE: 03-spec-claimstack v0.1
REGISTER: commercial product photograph. One frame, no panels, no insets.

[PRODUCT REFERENCE]  the attached photo is the exact reference.   -> G1
[SUBJECT]            the product, or a person using it.           -> PARTS/subject
[OFFSET]             the subject holds one side, the words the other. -> PARTS/offset
[SETTING]            a quiet ground, or the place the product works in. -> PARTS/setting
[LIGHT]              broad and even across the subject.

[TITLE]              what the tile is about.                      -> G16/title
[CLAIMS]             three to six short lines, each with a glyph. -> PARTS/claims
[BADGE]              one short stamp. Optional.                   -> MARKS
```

## PARTS

**`subject`** — the product, or a person using it. Six of the eight sources put the PRODUCT
there; two put a person with the product on them. Unlike the relief-job sibling, this type
has no reason to prefer a person, and the product form is simpler: **where the subject is the
product, G9 is not engaged at all.**

**`offset`** — the subject occupies 40–60% of the frame on one side, the text block the rest.
Seven of eight sources split left-right. `snapi-stud` and `gripi-mata` run the claims as a
RAIL along the bottom edge instead, which lets the photograph keep the whole frame — a real
alternative layout rather than a failure of the split.

**`setting`** — a quiet ground by default: light in value, close to neutral in colour
(ADR-068). A real room is legal and four sources use one; the ground is then the place the
product actually works in, which buys context the flat field throws away.

**`claims`** — **three to six**, each one short line, each with one simple glyph or a small
line icon. Below three the tile is a hero with decoration; above six no line is legible at
tile size. Counted across the corpus: three, four, four, four, five, six.

**One variant is confirmed at two sources and belongs to the CONSTRUCTION rather than to
either job: claims that carry PHOTOGRAPHS.** `glowy-liff` puts a macro of the treatment head
lit in each colour beside each mode it names; `hydrovia` puts a lifestyle vignette beside each
outcome. A photograph beside a claim is the cheapest substantiation a page can offer, and it
is the only thing separating these tiles from assertion. The same decision appears on the
relief-job sibling, which is what makes it a property of the claim stack and not of this type.

## MARKS
This type owns its mark library (ADR-012) and it is **not written yet**, for one reason worth
stating rather than deferring: the badge this construction actually carries in the corpus is
a **COMPATIBILITY BAR** — `pawdi-cas` runs Alexa, Google Assistant, MOES, Smart life, WiFi and
Tuya across the foot of two frames. That is a third mark class this library has never named.
It is not a certification seal and not a press mark, the two the trademark question of
2026-08-18 refused; it confers no authority and states an interoperability fact a buyer can
verify by trying it. **G6 bans logos outright and nothing exempts this.** Until that is
decided, this type ships with no mark library and a badge is optional and plain.

## SLOT CONSTRAINTS
- **The claims come from `product.specification` and `product.raw_features` and from nowhere
  else** — the same law `03-spec-callout` already carries. A claim line naming a capability
  the product does not have is a published claim, not a bad render.
- **No figure without a source.** Four sources put a bare percentage or a bare duration in a
  claim line. A15 binds: a figure enters only where `content.json` carries the figure AND its
  source, and the source sits beside it.
- **G16 governs every line.** Six claims plus a title plus a badge is eight clusters, which is
  the count G16's own founding rounds tested and held at exactly eight.
- **G7 exemption, narrow** — an object arranged on a plain ground beside a text block exists to
  be photographed. Arrangement only, per G7's scope as amended by ADR-064.
- **A product's own indicator colours are not signal marks.** Three sources carry LED arcs,
  ring codes or lit displays inside this construction. G3 does not reach them and a reader
  counting colour usage must hold the distinction.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a paragraph, more than six claim lines, a claim line longer than one line,
a second text block, a certification seal, an award, a press mark, a third-party
platform logo, a bare percentage, a bare duration, a gradient behind the words,
a claim about a felt state rather than a capability
```

## BLOCK
**Waiting on criterion 2, and it is the most consequential router-confusion test this library
has ever had to run.** This type and `06-relief-claimstack` are the same picture with a
different job. That one stands at 10 distinct sources and this one at 8; both clear criterion
1; both would be candidates for every feature and outcome slot on every product page. ADR-066
already refused to promote the relief-job type on exactly this basis, before this sibling
existed to make the test concrete.

The boundary as drafted is the CLAIM CONTENT — a capability against a felt state — and it is
written into both files' `use_when`. Whether a router can hold it is unknown.

**Criterion 3 has no render.** And the mark library is unwritten pending the compatibility-bar
decision above.

## KNOWN-FLAKY
- **Nothing observed.** No prompt and no render exist for this file.
- Carried from the corpus rather than measured here: `mozzapx` fuses this construction with
  dimension lines, an accessory inventory and a five-chip icon rail in one square — seventeen
  separate text elements, past every count this library has measured. Recorded as the failure
  mode this type drifts toward, which is accretion rather than any single bad clause.

## CHANGELOG
- 0.1 (2026-09-11): drafted from fifteen observations across eight distinct sources, batches
  2026-09-11-B, C, D, F, G, H, I and J. Criterion 1 cleared at eight; criterion 2 is the
  binding gap against `06-relief-claimstack` and criterion 3 is unrun. Filed as a spec-job
  sibling rather than merged, under SPEC 3.1. Device `claimstack` already exists. Raised and
  evidenced by `_CURATION-2026-09-11.md`. ADR-078.

---
id: 07-identity-pack
step: 7
job: identity
device: pack
version: "0.3"
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
avoid_adjacent: []
requires_pair: null
blocked_by: "One more distinct source for criterion 1, and criterion 2 is unrun. Criterion 3 has two renders and one is a fail by this type's own definition."
---

# 07-identity-pack — STAGING DRAFT

Promotion status (2026-09-03): **4/5 exemplars**, the highest any proposal in this ledger
has reached, and the four cover four different pack formats rather than repeating one:

| source | format | hash |
|---|---|---|
| millbrook-barrierbalm | stand-up pouch, plain ground | `sha256:95e174727db66ff2a…` |
| halden-densifol | carton plus one single-dose sachet | `sha256:3eb7c72d9fdf2943e…` |
| standfast-heelno1 | amber jar — on a built set, among rendered props, and cut out | `sha256:8f25531536fe6e340…`, `4dd1f5e6b5d780d40…`, `c3f96df477a2dafb9…` |
| redpine-tileno40 | pouch with its contents spilled at the foot | `sha256:d36212947ae4ebb2f…` |

**Criterion 1 needs one more source and criterion 2 is UNRUN.** Criterion 3 now has two
renders and **one of them is a `fail` by this type's own definition** — see FOUNDING RENDER
ROUND. Verdicts by eye under ADR-011; §6.3(3) wants the owner's own. Not routable.

**Step 7 and job `identity` are new vocabulary and ship in this diff.** This is the owner's
Q2b decision of 2026-09-03 taking form: a family whose argument is the object itself rather
than a funnel beat. **Staging defers the routing question rather than answering it** —
nothing under `_staging/` is routable, so the choice between keeping this family in
`registry/types/` under a new step and giving it its own namespace like
`registry/gif-types/` is still open and belongs to the promotion diff. It matters, because
since ADR-060 there is no admission test left: an active type in this registry is a
candidate for every slot on every page, and `use_when` is the only thing that would keep a
packshot out of a pain slot.

**The choice was made on 2026-09-10 and this file moved** (ADR-077). Two sentences above are
now history rather than instruction: this file is no longer under `_staging/`, and the home
question is settled in favour of a namespace — `registry/pdp-dr-types/`. What has NOT changed
is the consequence the paragraph names: the namespace is a wall where `use_when` was only a
sentence, and **that is one of the three reasons the namespace exists**. Nothing here routes,
so the admission problem ADR-060 left open is still held rather than solved.

## PURPOSE
Show the object as it arrives. This frame answers "what am I actually buying" — the pack,
its format, and what comes out of it — and answers nothing else. No use, no result, no
person, no place.

## TRIGGER
use_when: >
  The slot's job is to identify the product rather than to argue for it: the first
  or second gallery tile, a cart or checkout thumbnail, a variant swatch, a format
  tile beside a subscription picker. Use when the buyer needs to recognise the thing
  on arrival, or to see what a pack contains without opening it. NEVER for a slot
  whose copy argues anything — a symptom, a mechanism, a comparison, a result or an
  audience. A packshot in an argument slot answers a question nobody asked, and this
  sentence is the only thing standing between this type and every slot in the library.

## SKELETON
```
TYPE: 07-identity-pack v0.3
REGISTER: commercial product photograph. One frame, no panels, no insets.

[PRODUCT REFERENCE]  the attached photo is the exact reference.   -> G1
[FORM]               closed, open, or with its contents out.      -> PARTS/form
[PRESENTATION]       which face meets the lens, and at what turn. -> PARTS/presentation
[SETTING]            plain ground, knockout, or a built set.      -> PARTS/setting
[LIGHT]              broad, and the label stays legible.          -> PARTS/light

[TITLE]              the claim. Optional.                          -> G16/title
[BADGE]              one short stamp. Bottom LEFT. Optional.      -> MARKS
```

## PARTS

**`form`** — choose ONE. `closed`: the pack alone as it sits on a shelf. `open`: the pack
with its own lid or cap detached and propped beside it, embossed side out. `with contents`:
the pack plus one or a few of what is inside — a sachet, a capsule, a chew, a stick — laid
at its foot. The contents are **the product's own**, never a garnish and never an
ingredient: an ingredient beside a pack is `03-spec-stilllife`'s frame or
`03-spec-flatlay`'s, and it makes a composition claim this type does not.

**`presentation`** — the face carrying the brand mark and the product name meets the lens,
square or turned a few degrees. Where a second face carries information the buyer needs — a
supplement-facts panel, a dosage line — it may show in profile at the same time, and the
prompt says which face is which. Never a back panel alone: a back panel with claim roundels
composited beside it is the shape this ledger has rejected twice.

**`setting`** — one of three, named in the prompt, and all three are runtime values rather
than identity (`vocabulary.yaml` `parameters: environment`):

- **plain ground** — one flat tone with a soft contact shadow. The simplest, and **the one
  that goes monotonous fastest**: pick the HUE from the pack's own palette or from the
  category's, and keep it **light and low in saturation**. A pale grey ground under every
  product in a gallery is a gallery that looks like a spreadsheet — but the cure is a chosen
  hue, not a heavy one. Corrected 2026-09-03 (G16 round 4): "never a house grey" was read as
  licence for depth, and this type's two founding renders came back at 0.96 and 0.30 in
  value against a corpus median of 0.89 over 119 frames. The dark slate under the pouch is
  the one to look at twice; the light citrus under the cup is what the corpus actually
  does.
- **knockout** — no ground at all, a faint contact shadow, cut to composite onto any page
  colour. **This is the only form that needs no G7 exemption**: G7's scope note already
  reads a product cut-out as a graphic layer.
- **built set** — a constructed arrangement of plinths, arches or coloured blocks. Legal,
  and observed twice, but it costs the most: it is furthest from G7 and it dates fastest.

**`light`** — broad and even enough that **every word printed on the pack stays legible**.
This is the type's hardest constraint and the one most likely to fail. A pack's own printing
is diegetic and permitted under G6's scope note, but a renderer draws printed surfaces
badly: one observation in batch 2026-09-03-D is a generated frame whose labels are legible
as shapes and malformed as letters. **A render whose pack lettering is gibberish is a total
failure of this type**, not a flaw in it, because identity is the whole deliverable.

**Measured, 2026-09-03: 1 of 2.** A stand-up pouch came back with nine lines of printed copy
and every word a real word. A juicer cup came back with three invented strings — `batglie`,
`BRELLING THAT JUICER CUP`, `NONJHUTIVE SUPPORTS` — and is a `fail`. **Two renders is not a
rule and the difference between them is a HYPOTHESIS**: the pouch carries large flat type on
an opaque high-contrast panel, the cup carries small type curved around a translucent body
with juice behind it. If that is the discriminator, this type's `presentation` part should
prefer the flattest labelled face and its `setting` should refuse anything that puts colour
behind the lettering. Two more renders decide it; nothing is legislated yet.

## MARKS

**A badge is a mark and this type owns its forms** (ADR-012, ADR-043, G16's badge note). The
skeleton calls `badge` by name; the prompt names WHICH form, and the choice is made per
product from what its register can carry. **Three forms minimum, and none of them is a
default** — six test prompts written before this section existed produced six identical flat
rectangles, which is the monotony that put this section here.

| form | shape | the register it belongs to |
|---|---|---|
| `tag` | a flat rectangle, capitals cut out of the fill | tools, hardware, anything engineered |
| `seal` | a scalloped rosette or a shield | a guarantee or a standard about the seller. Note G16 refuses a certification mark inside one |
| `pill` | a rounded capsule | supplements, personal care, food |
| `roundel` | a filled circle carrying a figure — a count, a size, a quantity | a pack fact the label already carries and the eye should not have to hunt for |
| `flash` | a corner ribbon | an offer. **Highest going-stale cost of the five** |

**One badge per frame.** A packshot with two stamps has stopped being a packshot.
**Three corners are open and the bottom-right is not** (`adapters/nano-banana.md` Rule 7).
Asked for lower left and upper left, got both, 2 of 2.
**Tested: `roundel` 1 of 1 clean, `flash` 1 of 1 CUT.** The `flash` is the problem form and
its geometry is why: a ribbon crossing a corner is *defined* by reaching two edges, so it
cannot also honour G10's safe area. Measured — the ribbon's own fill reached 0.00% of both
edges and its words came within 1.07% of the top and 1.66% of the left. The words were
complete and nothing was cut, so this is a rule breach rather than a render failure, and it
is structural rather than incidental. **Until a form of `flash` exists that stops short of
the corner, this type should not ship one**, and `tag`, `seal`, `pill` and `roundel` all do
the job without the exposure.

**A badge is not FLAT and it is not ONE WORD AT ONE SIZE** (G16, round 4, 2026-09-03). The
table above describes an OUTLINE; it said nothing about the interior, and five of six
founding-round badges came back with a value spread of 0.02–0.09 — dead flat — against
0.10–0.35 on four corpus badges. The only render that was not flat is the only one whose
prompt named a second tone. What every badge in this type owes:

- **at least one internal tone step** — a rim, a concentric ring, an outline inset from the
  edge, or a sheen across the fill;
- **at least two type sizes** — corpus badges run 2 to 4; the six renders ran 1 to 2, and
  3 of 6 carried a single line of type at a single size.

A figure large, its label smaller, a qualifier smaller still, and often a glyph. That is a
small composition, and it is what makes a stamp read as a stamp rather than as a label.

## SLOT CONSTRAINTS
- **G1 is the entire frame rather than a preamble.** A reference-faithful pack IS the
  output. Where the reference photograph is poor, this type cannot rescue it.
- **No person, no hand, no room, no use.** A hand holding the pack up is
  `07-identity-inhand`; a person using it is a relief type's frame.
- **One product, or one product and its own contents.** Several variants side by side is
  `03-spec-lineup`, whose whole law is that exactly one thing differs across the units.
- **G7 exemption, narrow.** Covers the arrangement only, per G7's scope note as amended by
  ADR-064. Every other G7 test still binds: the pack is complete, nothing is cut open that
  the product does not open, no component is missing.
- **G8, G9 and G11 are not engaged** — no output, no symptom, no state.
- **G16 governs any text.** In practice a title and a badge at most, and the classes G16
  refuses are exactly the ones this corpus stamps onto packshots most often: an accolade, a
  certification seal, a best-seller flag, a discount. An origin claim sits close to the same
  line and is not yet listed there.
- **The pack's OWN printing is a text surface this type does not govern, and that is the
  sharpest exposure it has.** `text_layer` declares `[title, badge]`; the words on the object
  are diegetic and G16 does not reach them. The 2026-09-03 round returned a pouch printed
  with `Active Ingredients: Peppermint Oil, Cedarwood Oil` and `NET WT. 8 OZ (227g) ·
  Contains 12 Repellent Balls` — a composition claim and two quantity claims, rendered
  legibly, none of them written by anybody. **Gibberish lettering is a visible failure; a
  well-rendered invented net weight is an invisible one**, and it is `argument-faults.md`
  A15 arriving inside the one type whose whole deliverable is the printed object. A frame
  from this type is only publishable where its printed surface is checked against the
  reference word by word.
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a person, a hand, a room, a table setting, a second product class,
an ingredient or garnish beside the pack, a variant of the same product,
a certification seal, a discount flash, a torn or opened pack the product
does not open, a reflection that breaks the label
```

## WORKED EXAMPLES
### example: repellent-pouch-with-contents — skeleton@0.1, run: partial
The `with contents` form. Nine lines of the pack's own printing came back with every word a real word — the answer `PARTS/light` was waiting for. Two faults: the `flash` ribbon reaches 0.00% of two edges, and the printing carries an invented net weight, count and ingredient list. `sha256:124978745b7088e0…`

```
TYPE: 07-identity-pack v0.1
REGISTER: commercial product photograph, one frame.

PRODUCT REFERENCE: the attached photo is the exact reference for the rodent repellent balls
and their pack. Preserve shape, proportions, material, finish, colour and every word printed
on the pack exactly.

FORM: with contents. The pack upright and closed, four of the balls loose on the ground at its
lower left, none touching it.

SUBJECT: the face carrying the brand mark meets the lens. The pack takes about half the
picture's height; the loose balls sit small in front and give it its scale.

SETTING: a dark slate-grey ground with a faint stone texture, a soft contact shadow under the
pack and a fainter one under each ball. No room, no prop.

LIGHT: broad and even from the front and slightly above, strong enough that the pack's printed
words and the balls' surface both read.

TEXT: across the upper empty ground, two lines of flat white sans-serif starting a tenth of the
picture's width from the left edge. Each capital is as tall as one of the loose balls:
NOTHING SNAPS. NOTHING DIES.
THEY JUST STOP COMING BACK.

BADGE: a ribbon in a deep signal green crossing the UPPER LEFT corner at forty-five degrees,
as wide across as the pack, with DROP AND WALK AWAY in white capitals along it.

Nothing comes within a tenth of the picture's width of any edge. The two lines and the ribbon
are the only added words; the pack's own printed label is part of the object and stays exactly
as the reference shows it. No logo, no watermark, no person, no hand, no room.
```

### example: juicer-cup-closed — skeleton@0.1, run: fail
Portable juicer cup · `closed` form · 1:1 · badge `roundel` lower left · citrus-toned ground.
Stored diff-only: SPEC 3.3 keeps full prompt text only for an example that passed or partly
passed. `sha256:700ba34a50ba7279…`

- `FORM` — closed, lid on, nothing detached, nothing beside it
- `PRESENTATION` — the brand face to the lens, turned a few degrees, about half the frame's height
- `SETTING` — pale citrus-yellow ground, gentle vertical gradient, soft contact shadow
- `LIGHT` — broad and even, front and slightly above, every printed word legible
- `TITLE` — BREAKFAST THAT FITS / IN THE CUP HOLDER
- `BADGE` — filled coral circle, lower left, as wide as the lid, `400ml`

**Why it failed, and it is the type's own definition rather than a judgement call.** Three
strings printed on the object are not words: `batglie` on the grip band, `BRELLING THAT
JUICER CUP` on the body, `NONJHUTIVE SUPPORTS` beneath it. `PARTS/light` says a render whose
pack lettering is gibberish is a total failure rather than a flaw, because identity is the
whole deliverable. Everything else in the frame was clean, which is what makes it worth
keeping: the two clusters returned once each and the three added lines were exact, so nothing
about the TEXT LAYER caused this. The object did.

## KNOWN-FLAKY
- **Pack lettering fails 1 of 2 and the failure is total.** `batglie`, `BRELLING THAT JUICER
  CUP`, `NONJHUTIVE SUPPORTS` — three invented strings on one object. The other render
  printed nine lines correctly. This is the clause the type lives or dies on and it now has
  a denominator instead of a warning.
- **A CORRECT-looking print can still be invented.** The clean render carries a net weight,
  a count and an ingredient list that no brief supplied. Worse than gibberish, because
  nothing in the frame says it is wrong.
- **The `flash` badge form cannot honour G10** — 1 of 1, ink at 0.00% of two edges. Structural,
  not incidental: a corner ribbon is defined by reaching the corner.
- **The round cannot tell a missing reference from an ignored one.** Neither render log
  records whether a reference photograph was attached, and for a type whose whole frame is
  G1 that is a hole in the test rather than in the type. Record it next time.
- **The built-set form has two observations and no rule for how far a set may go.** Arches
  and plinths were observed; nothing says where a set stops being a ground and starts being
  a scene G7 must judge.
- **The routing question is unanswered by design** — see the header. Promotion cannot happen
  without answering it.

## FOUNDING RENDER ROUND — 2026-09-03
Two renders, ratio 1:1, prompts 5 and 6 of `registry/pdp-dr-types/ready-to-push/prompts.md` — the `closed`
form on a portable juicer cup and the `with contents` form on a rodent-repellent pouch. Both
products come from `query/product-slugs.yaml` and neither is in this type's source list. Both
frames carry the minimum text this type allows, a title and a badge, so the round is about the
OBJECT and not about the text layer.

| | 5 · `closed`, juicer cup | 6 · `with contents`, repellent pouch |
|---|---|---|
| verdict by eye | **fail** | **partial** |
| the pack's own printed words | **3 invented strings** | **9 lines, every word real** |
| clusters asked / returned | 2 / 2, no duplication | 2 / 2, no duplication |
| added words exact | 3 of 3 lines | 3 of 3 lines |
| headline cap | 62 px = 6.05% of frame | 50 px = 4.88% |
| headline ÷ its anchor | **0.45** | **0.64** |
| badge form, corner asked / got | `roundel`, lower left / lower left | `flash`, upper left / upper left |
| badge ÷ its anchor | **0.78** | **0.69** |
| closest prompted ink to an edge | 8.01% text · 5.37% badge | 10.16% text · **0.00% badge** |
| output | `sha256:700ba34a50ba7279…` | `sha256:124978745b7088e0…` |

**The type's central question is answered "sometimes", which is the worst available answer
and the most useful one.** `PARTS/light` said a gibberish pack is a total failure rather than
a flaw; render 5 is that failure and render 6 is a clean pass on the same clause. One of each
is not a rule — it is a denominator, and it says this type cannot be promoted on a source
count alone.

**The clean render is the one that should worry a reader.** It printed a net weight, a unit
count and an ingredient list, all legible, all invented. Gibberish announces itself; an
invented `NET WT. 8 OZ (227g)` does not. That is A15 landing inside the type least able to
absorb it, and it is now a SLOT CONSTRAINT rather than a note.

**Two clusters did not duplicate, in either frame.** G16's round-2 finding was that a
two-cluster frame drew its whole block a second time. These two did not, and the difference
is the one G16 already names: both headlines FILL the band they were given — 83.6% and 65.0%
of the frame's width — where the duplicating frame put a short block in a large reservation.
Cross-type confirmation of the fill rule, from the opposite direction.

**The `flash` badge is the one form this round rules out.** It went where it was asked and
reached both edges doing it, because a corner ribbon is defined by reaching the corner. The
words survived; G10 did not.

## NOTES
**Boundary against the four nearest frames.** `07-identity-inhand` puts the pack in a hand
to give it scale; here nothing gives it scale and that is the trade. `03-spec-lineup` shows
several units to argue breadth. `03-spec-flatlay` rings the pack with its ingredients to
argue composition. `03-spec-macro` magnifies a region of the product to argue material. All
four have a product in frame and only this one argues nothing beyond identity.

## BLOCK
**Waiting on one more distinct source for criterion 1, and on criterion 2, which is unrun.**
Criterion 3 has two renders and one of them is a `fail` by this type's own definition.

A15 arrived through this type and the entry says so: the founding render returned a stand-up
pouch whose printed surface read `Active Ingredients: Peppermint Oil, Cedarwood Oil` and
`NET WT. 8 OZ (227g)` — a composition claim and two quantity claims, set legibly on the object,
written by nobody. A frame from this type is publishable only where the pack's printing is
checked against the reference word by word.

## CHANGELOG
- 0.3 (2026-09-03): owner audit of the founding round — colour. `PARTS/setting`: the ground's
  HUE comes from the pack, its VALUE and SATURATION do not — light and quiet by default.
  Measured against a corpus ground-value median of 0.89 over 119 frames. `MARKS` gains the
  badge INTERIOR: one internal tone step and two type sizes minimum; both badges here were
  flat, at 0.02 and 0.03 spread, and both carried a single line of type. ADR-068.
- 0.2 (2026-09-03): founding render round, 2 renders — `sha256:700ba34a50ba7279…` (fail),
  `sha256:124978745b7088e0…` (partial). Pack lettering 1/2; the failure is total by
  `PARTS/light`'s own words. New SLOT CONSTRAINT: the pack's own printing is an ungoverned
  text surface and the clean render invented a net weight, a count and an ingredient list —
  A15 inside this type. MARKS: three open corners, 2/2 obeyed; `roundel` clean; `flash`
  breaches G10 at 0.00% and should not ship.
- 0.1 (2026-09-03): drafted from six observations across four distinct sources, gathered in
  batches 2026-09-03-C and 2026-09-03-D. The C observations were recorded against the
  library's older standard, which rejected packshots outright as raw product photos; the
  owner's Q2b decision of 2026-09-03 moved them, and each record says so. First type to
  propose step 7 and job `identity`; new device `pack`. ADR-065.

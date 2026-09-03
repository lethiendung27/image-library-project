---
id: 07-identity-pack
step: 7
job: identity
device: pack
version: "0.1"
status: reserved
replaced_by: null
ratios: ["1:1", "4:3"]
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

**Criterion 1 needs one more source; criteria 2 and 3 are UNMET** — no router-confusion
test and no render. Not routable.

**Step 7 and job `identity` are new vocabulary and ship in this diff.** This is the owner's
Q2b decision of 2026-09-03 taking form: a family whose argument is the object itself rather
than a funnel beat. **Staging defers the routing question rather than answering it** —
nothing under `_staging/` is routable, so the choice between keeping this family in
`registry/types/` under a new step and giving it its own namespace like
`registry/gif-types/` is still open and belongs to the promotion diff. It matters, because
since ADR-060 there is no admission test left: an active type in this registry is a
candidate for every slot on every page, and `use_when` is the only thing that would keep a
packshot out of a pain slot.

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
TYPE: 07-identity-pack v0.1
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
  that goes monotonous fastest**: pick the tone from the pack's own palette or from the
  category's, never a house grey. A pale grey ground under every product in a gallery is a
  gallery that looks like a spreadsheet.
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

## MARKS

**A badge is a mark and this type owns its forms** (ADR-012, ADR-043, G16's badge note). The
skeleton calls `badge` by name; the prompt names WHICH form, and the choice is made per
product from what its register can carry. **Three forms minimum, and none of them is a
default** — six test prompts written before this section existed produced six identical flat
rectangles, which is the monotony that put this section here.

| form | shape | the register it belongs to |
|---|---|---|
| `tag` | a flat rectangle, one flat fill, capitals cut out of it | tools, hardware, anything engineered |
| `seal` | a scalloped rosette or a shield | a guarantee or a standard about the seller. Note G16 refuses a certification mark inside one |
| `pill` | a rounded capsule, one flat fill | supplements, personal care, food |
| `roundel` | a filled circle carrying a figure — a count, a size, a quantity | a pack fact the label already carries and the eye should not have to hunt for |
| `flash` | a corner ribbon | an offer. **Highest going-stale cost of the five** |

**One badge per frame.** A packshot with two stamps has stopped being a packshot.
**The badge sits bottom LEFT** (`adapters/nano-banana.md` Rule 7).
**Untested**: no render exists on this type at all.

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
- Never state the frame's shape or ratio in a prompt (ADR-016, adapter Rule 4).

## NEGATIVE
```
[G6] + a person, a hand, a room, a table setting, a second product class,
an ingredient or garnish beside the pack, a variant of the same product,
a certification seal, a discount flash, a torn or opened pack the product
does not open, a reflection that breaks the label
```

## KNOWN-FLAKY
- **No render exists.** Every clause is a proposal.
- **Pack lettering is the risk and it is not hypothetical.** The corpus already contains a
  generated packshot with malformed label text. Until a render proves otherwise, treat this
  type as the one most dependent on the quality of the attached reference.
- **The built-set form has two observations and no rule for how far a set may go.** Arches
  and plinths were observed; nothing says where a set stops being a ground and starts being
  a scene G7 must judge.
- **The routing question is unanswered by design** — see the header. Promotion cannot happen
  without answering it.

## NOTES
**Boundary against the four nearest frames.** `07-identity-inhand` puts the pack in a hand
to give it scale; here nothing gives it scale and that is the trade. `03-spec-lineup` shows
several units to argue breadth. `03-spec-flatlay` rings the pack with its ingredients to
argue composition. `03-spec-macro` magnifies a region of the product to argue material. All
four have a product in frame and only this one argues nothing beyond identity.

## CHANGELOG
- 0.1 (2026-09-03): drafted from six observations across four distinct sources, gathered in
  batches 2026-09-03-C and 2026-09-03-D. The C observations were recorded against the
  library's older standard, which rejected packshots outright as raw product photos; the
  owner's Q2b decision of 2026-09-03 moved them, and each record says so. First type to
  propose step 7 and job `identity`; new device `pack`. ADR-065.

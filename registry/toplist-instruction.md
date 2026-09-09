# Toplist instruction — law shared by every toplist type

Stated once here and **never restated in a type file**, exactly as
`registry/gif-instruction.md` treats the motion registry and as SPEC §5 treats the
global rules. A toplist type file carries what is different about that type and
nothing else.

Read this before `registry/toplist-types/<id>.md`. SPEC §3.7 is the contract; this
file is the working law under it.

## What this namespace is for

**One image.** A top-N listicle — "the best 5 X of 2026" — carries a single lede image
(lead image, featured image, hero) and then goes to text. Everything else on the page is
a product card, and product cards are not this library's business.

That single fact is the whole reason for a third namespace. With one slot, over half of
SPEC §7 has nothing to act on:

| SPEC §7 step | in a top-N page |
|---|---|
| 2 · Stage 1 shortlist by role affinity | **dead** — one slot, one role, so affinity is a constant |
| 3 · Stage 2 portfolio, cross-slot rules | **dead** — `never_with`, `avoid_adjacent`, `pairs_with`, one-type-once all need a second slot |
| 5 · coverage pass over Trust Ladder rungs | **dead** — one image cannot cover a ladder |
| 4 · three options, three distinct types | **alive and still the deliverable** |
| 6 · at least two variations | **alive** |
| 8 · adapters at render time | **alive, unchanged** |
| 9 · picks ledger | **alive, and see SELECTION below** |

Keeping the dead half alive in a one-slot format is machinery that cannot run. That is
the same reasoning SPEC §3.6 gives for gif types reaching their registry by id rather
than through a shortlist.

## Input is the PRODUCT block, not `content.json`

`content.json` is `{ product, page }`. A top-N page has no `page.sections` to route and,
since ADR-059, `page.channel` admits nothing. So this namespace consumes the `product`
half alone, extended.

**What the product block already carries** and every type may read:

| field | what it is | machine-readable |
|---|---|---|
| `attributes` | 8 keys, mostly closed enums | **yes** — the gates below run on it |
| `problems_solved[]` | what the buyer suffers | no, prose |
| `personas[]` | who the buyer is | no, prose |
| `specification` | the manufacturer's own line, verbatim | no, prose |
| `raw_features[]` | feature claims as the brief states them | no, prose |
| `reference_photos[]` | sha256 hashes; **empty is a statement, not a gap** | yes |
| `name`, `category` | identity | yes |

**What a top-N page needs that the block does not have yet**, named here so a reader is
not surprised by an absence:

1. `products[]` — the schema carries exactly ONE product. A top-N is N. Every type
   declaring `products_in_frame: many` is blocked on this and is `status: reserved`.
2. a rank or verdict per product — "Best Overall", "Best Budget". Nothing carries it.
3. test facts — what was measured, with what. `lede-testing` works without them and
   would be better with them.
4. `category` is one coarse string (`home`); a top-N is about a narrow category.

`awareness` IS carried on the input. See SELECTION for how little it is trusted.

## SELECTION — four layers, and only one of them uses awareness

The owner's instruction of 2026-09-09 was to carry awareness but not to lean on it. This
is the shape that obeys it: the two layers that can REFUSE a type are mechanical and
awareness-free, and awareness only orders what survives.

**Layer 1 — mechanical admission. Refuses. No judgement, no awareness.**

- `status: reserved` → not routable, ever.
- `products_in_frame: many` → needs `products[]` with ≥3 entries AND the reference-photo
  decision below. Until then, refused.
- `requires_product_photo: true` with `reference_photos` empty → refused, and say so in
  the session notes rather than shipping a prompt the owner cannot run.
- The `product.attributes` gates of `mapping/toplist-rules.md`, which **restate by
  toplist id** every gate a copied type should carry. A gate in `mapping/slot-rules.md`
  names the parent and does not reach a copy — see *Copying* below. Live example:
  `result_visibility: invisible` drops `06-relief-scene` there and `lede-inuse` here, and
  the second line exists because the first one cannot do the work.

**Layer 2 — preference order. Orders. This is the only place awareness is read**, and
`mapping/toplist-rules.md` says in its own first paragraph that it is a hypothesis with
no evidence behind it.

**Layer 3 — FIT, by judgement, on `use_when` and `BOUNDARY` against the product prose.**
This is what actually decides, and the library has known since ADR-059 that "judgement
does not scale and no regex audits it". The mitigation ADR-059 named is the one this
namespace adopts as law: **every choice cites the sentence of product copy that decided
it**, which turns a judgement into a record somebody can audit later.

**Layer 4 — pick rate.** `feedback/picks.jsonl` per SPEC §7.7, at ≥20 contested
observations per cell. It holds 0 records today. One slot per page means one record per
page and a cell keyed on the type alone, so **20 pages make this real** — the fastest
this prior can fill anywhere in the library, and the reason this format is worth
measuring rather than arguing.

## Text: some types carry one, and G16 binds them

**A toplist type MAY bake words and a badge into the frame** — owner decision, 2026-09-09
(ADR-071), reversing the constraint of the same day that this file was first written on.
The corpus classified in batches 2026-09-09-A/B agrees: **7 of 32 reference frames carry
baked text**, including both forms the owner named — a winner packshot under a verdict
band, and a cut-out collage under a "BEST X" line.

**Which types carry one is decided by evidence, not by permission.** Two do:

| type | `text_layer` | why |
|---|---|---|
| `lede-winner` | `[title, badge]` | the verdict mark IS the type — strip it and `07-identity-pack` already does the picture |
| `lede-collage` | `[title, badge]` | the market form the owner named, and **2 of the 3** corpus collages that are actually several products carry an award badge |

The other five do not, and that is the corpus talking rather than a rule: **5 of 5**
`lede-lineup` observations carry no text at all, and **10 of 11** `lede-testing`
observations carry none — the single exception is a video thumbnail rather than a page
lede. Adding a text layer to those two would be a clause with one observation against ten.

**So G16 binds this namespace after all**, on exactly the types that declare the key —
four rounds of measured work on line caps, the badge interior, the mobile floor, the
size anchor and the watermark corner arrive intact and are not restated here. No ground rule is imported from
that work: this namespace measures its own, below.

**What is still refused, and it was not part of the instruction.** The owner permitted the
PAGE'S OWN verdict about its own ranking. Two of G16's content rows are marked `LAW, not
taste` and neither was addressed:

- **another party's mark** — a certification seal, a press logo, a third-party award. The
  corpus carries these (`CNET LAB TEST WINNER`, `CNET PEOPLE'S PICKS`) because on CNET's
  own page CNET is the issuing body. On a page that is not theirs it is a trademark
  question, and the library declined to answer that one on 2026-08-18.
- **a fabricated endorsement** — a customer's name, star row, review count or verified
  mark. G14 calls it illegal under FTC endorsement rules and binds the SLOT rather than
  the type, so there is nothing here to waive.

A publisher's own SCORE sits between them and is permitted with a leash: it is a figure,
so `argument-faults.md` A15's working position holds — **the number enters the frame only
where the product input carries it**, never where a prompt invents one.

## Ground: built from this corpus, and from nothing else

**No ground rule is imported into this namespace** (owner instruction, 2026-09-09;
ADR-073). ADR-068's finding was measured on 119 direct-response product-page frames and
was carried in here twice — once whole, once half-corrected — and both times it was a rule
about a different kind of picture. What follows is measured on the 32 frames of
`stills/top list/`, classified in batches 2026-09-09-A/B, and on nothing else.

**One measurement splits the namespace in two, and it is not colour.** The mean
adjacent-pixel difference in the outer 8% ring — call it TEXTURE — separates a ground that
was DESIGNED from one that was PHOTOGRAPHED, with no overlap:

| family | n | texture | value | saturation | ring spread |
|---|---|---|---|---|---|
| `lede-winner` | 1 | **0.8** | 0.91 | 0.60 | 0.15 |
| `lede-collage` | 5 | **1.9** | 0.90 | 0.49 | 0.25 |
| `lede-lineup` | 5 | **2.9** | 0.81 | 0.26 | 0.33 |
| *proposed* `lede-mosaic` | 3 | **2.8** | 0.76 | 0.43 | 0.35 |
| `lede-authority` | 3 | 7.0 | 0.67 | 0.15 | 0.51 |
| `lede-testing` | 11 | 7.1 | 0.65 | 0.13 | 0.67 |
| `lede-inuse` | 1 | 10.0 | 0.16 | 0.26 | 0.34 |

Everything at or under 2.9 is a made surface; everything at 7.0 and over is a room. There
is nothing between 2.9 and 7.0 in 32 frames.

**`lede-lineup` is on the DESIGNED side, and that corrects what its own file assumed.**
It reads 2.9, with the group, not 7. Four of its five stand on a smooth studio sweep rather
than in a place. What is real in a lineup is the SURFACE the units stand on and the contact
shadows it takes; the backdrop behind it is not.

Three ground clauses follow, and each type file carries the one that is its own.

### Designed, gradient — `lede-collage`, `lede-winner`, and the proposed `lede-mosaic`

Perfectly smooth: no grain, no texture, no paper, no vignette. **Light AND strongly
coloured** — value about 0.90 with saturation about 0.50, both together, since a dark
saturated field and a light quiet field are each only half of what the corpus does.

**Either a two-hue gradient running diagonally, or one flat tone. Nothing between the two
was observed.** Three of the five collages travel roughly half the colour wheel corner to
corner — measured at 177°, 175° and 177° of hue spread on a diagonal axis, which is green
to red, purple to teal, magenta to orange. The other two hold a single tone at under 13°
of spread. `lede-winner`'s one frame is a diagonal at 179°.

### Designed, seamless — `lede-lineup`

A studio sweep, not a room. **Saturation here is bimodal and the median hides it**: the
five measure 0.03, 0.21, 0.26, 0.66 and 0.71 — three near-white sweeps and two strongly
coloured ones, with nothing at all between 0.26 and 0.66. So this is a CHOICE a prompt
makes rather than a band it lands in. Value runs 0.68 to 0.96.

**No gradient.** Hue spread is small on every frame whose ring is actually ground. The one
reading 175° is a garment flat-lay filling the frame edge to edge, so the metric measured
the subject rather than the backdrop — which is the honest limit of measuring a ground from
a ring, and the reason this clause does not claim a clean 5 of 5.

### Photographed — `lede-testing`, `lede-authority`, and the two copied types

A real place, and measurably so. **Texture ~7.0.** **Mid, not light** — value 0.65 against
0.90, because a bench under working light is not a sweep. **Quiet** — saturation 0.13, with
2 of 11 above 0.25: the colour in these frames is in the apparatus and the product, never
in the room. **Unevenly lit** — value spread 0.67 across the ring, because real light falls
off; a prompt asking for even illumination across the background is asking for a studio.

`lede-inuse` has one observation and it is dark (0.16). `lede-pain` has **none**: this
corpus is editorial review publishing and carries no pain lede at all, so that type's
ground stays whatever its parent gives it and is not written here.

## Copying: verbatim, and made auditable

**Owner decision, 2026-09-09 (ADR-070): a toplist type that reuses an argument carries the
parent's text, not a pointer to it.** Where `copied_from` names an image type, everything
from `PURPOSE` to `KNOWN-FLAKY` in that file is the parent's own text, spliced by script
rather than retyped, and the file stands alone.

Two sections are deliberately NOT copied, for correctness rather than for brevity:

- the parent's **`WORKED EXAMPLES`** — SPEC §3.3 keeps a rendered example's full prompt
  text as the record of what actually rendered, and those renders were the parent's at the
  parent's version. Reprinting them under a toplist id would be a false claim about what
  was rendered.
- the parent's **`CHANGELOG`** — its evidence trail and commit hashes. This file has its
  own.

**`copied_at_version` is what makes the choice auditable.** It records the parent's
version at the moment of the copy, and `scripts/validate.py` **warns** when the parent
moves past it. A copy cannot be stopped from drifting; it can be made to say so. The
warning names the remedy: re-copy, or write into this file's CHANGELOG why the divergence
is intended.

The exposure is recorded rather than argued away. `registry/types/_staging/ready-to-push/`
once shipped byte copies of four type files and they were deleted on 2026-09-03 with the
finding written into that folder's README — *two copies of one file drift, and the stale
one is the one somebody reads*. That remains true here. What is different is that this
namespace has an instrument pointed at it.

**A copy is NOT reached by a rule keyed on the parent's id, and that is the part most
likely to be forgotten.** `mapping/slot-rules.md` says *"drop `06-relief-scene`"* when
`result_visibility: invisible`; nothing in it says `lede-inuse`. Every gate a copied type
should carry is therefore restated by id in `mapping/toplist-rules.md`, and adding one to
the parent later does not add it here.

## Global rules

Every rule in `registry/rules.md` binds unless a type declares `exempt_from`, exactly as
for image types. Three deserve naming because a top-N page walks into them:

- **G1** is load-bearing everywhere here: a lede image whose product is wrong is a lede
  image for a different page.
- **G14** binds the SLOT. A lede image that reads as a customer's own photograph, beside
  a ranking the page presents as editorial, is the shape G14 exists to refuse.
- **SPEC §6.4** — *competitor brand marks never appear in prompts*. A "best 5" frame is
  by definition about five named brands, which is why `lede-lineup` and `lede-collage`
  are reserved rather than drafted-and-hoped.

**Ratio is not declared by these types.** The owner's app resolves the lede ratio
(2026-09-09), so a toplist type carries no `ratios` key and no prompt states one — the
ban on writing a ratio into prompt text (ADR-016, adapter Rule 4) is unchanged.

## The two decisions this namespace is waiting on

1. **The reference-photo limit.** ADR-021 allows one attached photo per prompt; a five-product
   frame needs five. The model accepts several (adapter, Rule 2 note); the limit is a number
   in our law, not a capability of the renderer, and its principle — one generation call — is
   not threatened by attaching five. Until decided: `lede-lineup` and `lede-collage` reserved.
2. **The two `LAW, not taste` rows of G16** — an award or a rating, and a named expert.
   Until decided: `lede-winner` and `lede-authority` reserved.

Neither is a craft question and neither is the harness's to take.

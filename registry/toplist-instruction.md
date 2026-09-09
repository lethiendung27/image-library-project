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
- The `product.attributes` gates of `mapping/slot-rules.md` still bind wherever a type
  `inherits` an image type that they name. Live example: `result_visibility: invisible`
  drops `06-relief-scene`, and therefore drops `lede-inuse`.

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

## Text: this namespace does not carry one

**No words are baked into a lede image.** The owner's constraint, 2026-09-09: the file is
scraped as `og:image` for social previews and is checked at L21, and baked text is
cropped, duplicated by the page's own headline, or both.

So **no toplist type declares `text_layer`**, and G16 — four rounds of work on caps,
badges, mobile floors and size anchors — **does not bind here at all**. What does carry
over from that work is ADR-068's finding about the GROUND, because that is a fact about
the photograph rather than about the text: the direct-response corpus sits at a ground
value median of 0.89 and saturation 0.06 over 119 frames, and a dark or saturated ground
is a choice a prompt justifies rather than a default.

A type whose only distinguishing feature is a word — a "Best Overall" band, a "BEST X"
overlay — therefore does not exist in this namespace until that is decided by ADR.

## Inheritance: cite the parent, never copy it

Where a toplist type declares `inherits: <image-type-id>`, the argument is already owned
by the image registry and this file exists to place it in a lede slot. Such a file:

- **calls the parent's `PARTS` and `MARKS` entries by name and never restates them**,
  which is the grammar SPEC §3.3 already uses for a call-map and `VARIANTS` already uses
  for a diff;
- carries only what differs — the slot, the trigger, the boundary, the extra negatives;
- inherits the parent's attribute gates and its own laws.

The reason is recorded and recent. `registry/types/_staging/ready-to-push/` once shipped
byte copies of four type files so they could be read without opening the repo, and they
were deleted on 2026-09-03 with the finding written into that folder's README: *two
copies of one file drift, and the stale one is the one somebody reads*. A namespace built
on copies would inherit that defect seven times over.

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

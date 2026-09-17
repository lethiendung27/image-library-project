# PDP-DR rules — routing a direct-response product gallery

Law for the namespace is `registry/pdp-dr-instruction.md`; the contract is `SPEC.md` §3.8.
This file is the routing half: which types a product-gallery slot prefers, what refuses,
and what nothing checks.

**An LP2 page routes ONE folder, `registry/pdp-dr-types/`, and never opens
`registry/types/`** (ADR-091; owner instruction, 2026-09-15: each page kind routes one
folder, and that folder holds every type the page may use). Its routing surface is
`registry/pdp-dr-index.yaml`, generated from the folder's active files. Three kinds of file
live there:
- a verbatim copy of every active image type, under the parent's id;
- a copy of a fitting type from another page kind's folder, under an LP2 id (ADR-097);
- LP2's own drafts, every one `reserved` or `deprecated`, which route nowhere until one is
  promoted in place.

The two kinds of copy are what route today.

## Slot kinds — what each image field of a template is

**Owner decisions, 2026-09-17** (ADR-096), taken on the four LP2 templates of that day —
`t1-deal`, `t2-eco`, `wiboofy` and `aure-toplaser` — and binding any template added later:
**only the product card's image gallery carries words**; buyer-photo tiles and
before-and-after pairs are **always generated**; and the gallery keeps this namespace's one
text law, with no second law by look.

A template marks each image field with `data-field-type="image"`, a dotted `data-field` path,
`data-locked` and an enclosing `data-block-key`. **The kind is read from the path, and the first
matching row wins.** `python3 scripts/pdp-dr-slots.py TEMPLATE.html` applies this table as
written: it parses the table and owns no rule of its own, so a template added later needs no
edit anywhere, and a field no row matches fails the script rather than being guessed.

| field path | kind | words | the image |
|---|---|---|---|
| `@locked` | chrome | — | the template's own asset — a guarantee seal, an award, a press logo, the payment cards. Never generated |
| `cart.*` `sticky.*` `notify.*` `toast.*` `*.product_image` | thumb | — | gallery image 1, reused |
| `buy.thumbs.*` | thumb | — | the gallery tile it stands for, reused |
| `buy.gallery.0.*` | packshot | — | the standard product shot, out of library scope (cross-rule 6) |
| `buy.gallery.*` | gallery | the LP2 text law | a gallery tile, routed by Layer 2 and the cross-slot rules below |
| `hero.*` | hero | none | a banner the template crops — the instruction's section of that name |
| `proof.items.*` `demo.items.*` | gif | none | a loop, routed by `registry/gif-types/` off the slot's own verdict (ADR-023) |
| `*avatar*` `@portrait` | portrait | — | a person's face beside their name, out of library scope (`mapping/slot-rules.md`, `author`) |
| `*before_image` `*after_image` | pair | none | one state of a before-and-after pair. Generated — cross-slot rules 11 and 12 |
| `reviews.*` `ugc.*` `trusted.*` `testimonials.*` | buyer-wall | none | a buyer-photo tile. Generated, `05-social-snapshot` first — rule 12 |
| `expert.*` | section | none | routed by the block's copy, and never a face — rule 12 |
| `*chart*` | chart | — | a data chart, built in HTML: without words a chart says nothing |
| `close.*` `offer.*` `bundle.*` | closing | none | gallery image 1 by default; generated only where the block's copy argues what the packshot does not |
| `*` | section | none | routed by its block's copy — rule 10 |

`@locked` is a field whose `data-locked` is `true`. `@portrait` is a field in `reviews`,
`expert`, `testimonials` or `trusted` whose `width` is 160 or less. The script also reports the
frame each image is shown in, read from its sizing classes, so the owner can set the ratio at
render time. The frame never goes into a prompt (ADR-016).

**Measured on the four templates, 2026-09-17**, every image field matched a row, and the rows
decide what the library does with 171 fields. On those four the library generates the hero, the
gallery from image 2, the section images, the pairs and the buyer tiles. It generates nothing
for the chrome, the thumbnails, the portraits or the chart. `python3 scripts/pdp-dr-slots.py`
prints the per-template counts.

## Layer 1 — mechanical admission

| condition | effect |
|---|---|
| type is not in `registry/pdp-dr-index.yaml` | **not routable.** The index carries the folder's `active` files only; a draft's `reserved` or `deprecated` status keeps it out, and a reserved draft carries a `blocked_by` and a `BLOCK` saying why |
| `requires_product_photo: true` and no reference photo for the product | refuse, and say so in the session notes rather than shipping a prompt the owner cannot run |
| the gallery is syndicated to a marketplace | drop the ugc register, drop `01-pain-scene`, forbid `04-proof-lockedframe --rivals` (`mapping/slot-rules.md` cross-rule 5) |
| slot is gallery image 1 | out of library scope — a standard product shot (cross-rule 6) |

Every attribute gate in `mapping/slot-rules.md` applies unchanged. They are keyed on ACTIVE
type ids, and this folder's copies keep their parent's id, so unlike the toplist namespace
**nothing has to be restated here** — ADR-070's finding was about gates keyed on a parent
whose COPY had a different id. A draft promoted here brings no gate with it; if one should
apply, the promotion diff writes it, as it would for a new image type.

## Layer 2 — preference order, MEASURED

Unlike `mapping/toplist-rules.md`, which declares itself a hypothesis in its own first
paragraph, this table is counted from the ledger: **159 observations across 26 source pages**,
batches `2026-08-31-A`/`-B` and `2026-09-03-C` through `-H`. The number beside each type is
its **distinct source count on this corpus**, not its observation count — the two diverge
badly and SPEC §6.3 counts sources for that reason.

| role | preferred, best first (distinct PDP sources) |
|---|---|
| hero | `06-relief-hero` (16) |
| problem-agitation | `02-symptom-rail` (2) |
| cause | `02-cause-anatomy` (3) |
| mechanism | `03-spec-macro` (13), `03-mechanism-ghostbody` (2), `03-mechanism-xray` (1) |
| proof | `04-proof-lockedframe` (5), `04-proof-testing` (0 — copied from the toplist namespace, ADR-097) |
| social-proof | `05-social-snapshot` (7), `05-social-handoff` (1) |
| personas | `05-persona-grid` (1) |
| how-to-use | `03-use-sequence` (4), `03-use-grid` (2) |
| comparison | `04-proof-lockedframe--verdict`, `03-spec-split` — **neither observed here**; the row falls back to `mapping/slot-rules.md` |
| outcome | `06-relief-hero` (16), `06-relief-scene` (4) |
| cta, author | — (out of library scope) |

This is a PREFERENCE ORDER and not the candidate pool (ADR-058). The pool is every active
type in `registry/pdp-dr-index.yaml`, for every slot; a type outside a row is a candidate, not
a violation.

**One tile carries one message** (owner instruction, 2026-09-16). A section whose copy names
three unrelated features is not one slot's worth of argument: the page arc decides which
feature this tile makes, and the others belong to other tiles or to a claim stack whose lines
all support the same message. Routing a three-feature paragraph into one tile is how a gallery
ends up with a frame nobody can summarise. A set counts messages as feature keys, and a new
tile needs a key the set has not used (`registry/pdp-dr-instruction.md`, ADR-094).

### The finding this table exists to record: step 1 is EMPTY

**Four active types appear on no page in this corpus**, and two of them are the whole of the
Trust Ladder's first rung:

| absent from all 26 PDP sources | present in the advertorial/listicle corpus |
|---|---|
| `01-pain-scene` | yes |
| `01-pain-split` | yes |
| `03-spec-explode` | yes |
| `03-spec-split` | yes |

And the reverse, once: **`06-relief-scene` appears here and nowhere in the older corpus.**

`mapping/slot-rules.md` prefers `01-pain-scene` for both `hero` and `problem-agitation`. On a
product gallery that preference points at a type the format does not use — a buyer on a
product page has already been sold the problem by the ad that brought them, and the gallery
opens on the object or on the outcome. That is why the `hero` row above names one type and it
is a relief type.

**What this does NOT prove.** The owner selects what enters a batch and the harness classifies
it; 26 pages is what was filed, not a random sample of the format, so this is *absent from what
was filed* rather than *absent from the format*. `03-spec-explode` in particular is a
plausible gallery tile that simply did not turn up. The rows stay as measured and the limit
stays written next to them — the alternative is a rule that feels obvious, which is the exact
shape ADR-068 caught moving a whole render set off the market.

## Cross-file call register — the thing nothing checks

Since ADR-091 this namespace ships verbatim copies too, and pays for them the way the
toplist namespace does: `copied_at_version` and a validator warning when the parent moves
(ADR-070). That instrument watches whole files. It does not reach a smaller exposure of the
same kind: **a skeleton that calls a part defined in another file is a reference nothing
validates.** Every one of them lives here:

| the caller | calls | defined in | status |
|---|---|---|---|
| ~~`07-identity-callout` `[PRESENTATION]`~~ | `PARTS/presentation` | `03-spec-callout` | **dead — caller deprecated 2026-09-11** |
| ~~`07-identity-callout` `[SETTING]`~~ | `PARTS/setting` | `03-spec-callout` | **dead — caller deprecated 2026-09-11** |

**Zero live calls today.** Both rows are struck rather than deleted: the caller was retired
by ADR-078 in favour of the type it was calling into, which is the cleanest way a
cross-file call can end, and a reader following the deprecation needs to see that the calls
went with it.

**Adding a call without adding a row here is the failure this register exists to prevent**,
and the register is the whole instrument — the validator does not read skeleton prose. The
three files written on 2026-09-11 (`03-spec-claimstack`, `03-spec-dimension`,
`03-spec-hero`) deliberately restate their own parts rather than calling a sibling's, so the
register stays empty.

`06-relief-animal`, retired on 2026-09-17 (ADR-095), cited `06-relief-scene`'s `PARTS/subject`
and `pairs_with` in prose rather than calling it from a skeleton; that was an argument, not a
reference, and it was never in the table above.

## Cross-slot rules — where a gallery differs from an advertorial

All of `mapping/slot-rules.md`'s portfolio constraints apply. Twelve do more work here — three
because of the page's shape, six the owner added on 2026-09-16 (ADR-093, ADR-094), and three
for the images outside the gallery, after the owner's decisions of 2026-09-17 (ADR-096). **Rules
1, 2, 7, 8 and 9 and rule 3's budget bind the gallery**; rules 4–6 and rule 3's one-variant
clause bind every image a session emits for the page.

1. **One type at most once in the gallery**, and a type's variant or form counts as the type. A
   twelve-tile gallery is **not** a repeating section in cross-rule 2's sense. A roundup's
   ranked entries are equivalent list items; a gallery's tiles are a linear argument, and
   repeating a type across a linear funnel repeats an argument. The exception stays available to
   a review wall inside the page, which is a genuine repeating section.
2. **Page arc, G4 at page level, with places named.** Image 1 is the standard packshot and out of
   scope. **Problem tiles sit at images 2–3 and never after the first Outcome Hero** — a split
   before a rail, a cause anatomy after either and before the mechanism tile. **The mechanism
   tile sits at 3–4**, after the problem tiles and before the use steps; **use steps at about
   4–5**; **an Outcome Hero at 2–3 or closing**, the first one closing the problem phase. With
   twelve slots there is room to break this without noticing.
3. **The mechanism-class budget** (ADR-094, widening the step-3 trio). **At most two gallery
   tiles** from three groups: any mechanism (`03-mechanism-*`, and the Principle and Demonstrated
   forms once they have files); any comparison or proof (`04-proof-lockedframe`, `04-proof-testing`,
   `04-proof-stat`, `03-spec-split`); any use steps (`03-use-sequence`, `03-use-grid`). **One mechanism variant
   per page** unless the page asks for two. `mapping/slot-rules.md`'s trio — at most two of
   `03-mechanism-ghostbody`, `03-spec-split` and `03-use-sequence` — sits inside this budget and
   still holds. `03-spec-macro` is outside it: the corpus's commonest mechanism tile at 13
   sources, a feature tile in the owner's taxonomy, and one to a gallery whatever the surface.
4. **One style lock per session.** Every image a session emits for a page — gallery tiles and
   section images alike — shares the lock's two grounds, its text colours, its one accent, its
   typography, its chip form, its design language and its lighting family, named once and then
   repeated in every prompt in the same words. The fields are in
   `registry/pdp-dr-instruction.md`.
5. **Composition varies tile to tile.** Layout, camera angle, crop and the product's share of
   frame are where a gallery shows design, and the style lock is not a licence to repeat one
   frame twelve times. **No tile repeats the previous tile's angle, and no angle family appears
   more than twice in twelve.** A routed SET whose options all resolve to the same camera is a
   set to re-route, not a page to ship.
6. **One product variant per page** — the first photograph attached, or the one the page names.
   Another variant appears only in a Lineup tile, or where the page asks.
7. **A Lineup and a Grid are never adjacent.** `03-spec-lineup` already names both grid types in
   `avoid_adjacent`.
8. **At most two "use it in a place" scenes in the gallery** — office, car, truck, gaming, wheelchair,
   pregnancy — unless the page asks for a persona series; `06-relief-scene` always counts. At
   two, the idea is re-cut as a feature, an outcome or a grid tile.
9. **The words are counted over the gallery**, the only images on the page that carry any. Per
   twelve tiles, scaled to any other count: copy on at most 6, a chip on at most 4, at least 4
   tiles carrying a title alone, at least 1 carrying no words. The law, and what a line may
   never say, are in the instruction's text section.
10. **An image outside the gallery routes by its own block's copy** — ADR-090's content-first
    pool — and the template fixes its place, which is why the gallery's rules leave it alone. The
    items of one block route item by item. One type may serve every item where the items are
    equivalent — the modes of one device, the stages of one result — and the images then differ
    on a named dimension (`mapping/slot-rules.md` cross-rule 2). A section image never repeats a
    gallery tile's type AND its message: that is one tile shown twice.
11. **A before-and-after pair is one argument in two files.** Route it once: both files take
    one type — `04-proof-lockedframe --timelapse` where the change happens over time, the two
    halves of `01-pain-split` where it is the old way against the new — and both prompts are
    written from one locked description (the instruction, *A pair shares one description*).
12. **Buyer-photo tiles and pairs are always generated** (owner decision, 2026-09-17, ADR-096).
    G14's attribution test still runs on each. Where it fires, the prompt ships with its
    `compliance` flag and note (ADR-089), and no LP2 session refuses. **A section image in a
    block that names a person never shows a face** — the `expert` blocks today. A face beside a
    name is that person's portrait, the `author` row, and an invented person there is the
    endorsement ADR-094 refused; the product, a pair of hands or a test (`04-proof-testing`) carries that block.

**The set keeps a ledger, and every tile reads it before it chooses anything.** Tile by tile and
cumulatively: the types used, the message keys used (feature keys, not sentences), the angle
families used across every image, and the gallery's copy, chip, title-only, wordless and
place-scene counts. A new tile takes
a type, a key and an angle the ledger does not already hold; a set whose ledger breaks a count
above is re-routed rather than shipped. The ledger is what a set's `check.py` checks.

## What happens when the reserved files unblock

A draft is promoted **in place**: its `status` becomes `active` and its `blocked_by` null,
and `scripts/validate.py --write-index` writes it into `registry/pdp-dr-index.yaml`. It does
NOT move to `registry/types/` — that would take it out of the one folder an LP2 page routes
(ADR-091); a type in the register below is also WRITTEN there — and it gains a row in the
Layer 2 table above under its role. **This file grows
as the namespace succeeds.** ADR-077 wrote the opposite, that promotion was a `git mv` and
this file would shrink; that was the co-registry, and ADR-091 retired it.

### LP2 drafts LP1 routes too — a register

**Whether LP1 routes a promoted LP2 type as well is the owner's decision, type by type, and
each answer is a row here** (ADR-095). Like the call register above, this table is the whole
instrument: nothing reads it but the promotion diff, and a draft with no row routes on LP2
alone.

| LP2 draft | LP1 routes it | decided | what its promotion diff owes |
|---|---|---|---|
| `03-mechanism-contact` | **yes** | owner, 2026-09-16, ADR-095 | see below |

**What a promotion on this register owes**, so the pair is watched by the instrument that
already exists rather than by a new one:
- **The file is written into `registry/types/` as the PARENT**, without `text_layer` and without
  the LP2 law, since no LP1 type declares a text layer. Its rendered WORKED EXAMPLES and its
  CHANGELOG go with it: the id's render lines and ledger records are the parent's evidence.
- **The LP2 file becomes its declared copy** — `copied_from`, `copied_at_version`, and every
  LP2 difference gathered in `## LP2 LAW` beside its `text_layer` — so the drift warning
  `scripts/validate.py` already runs covers the pair. Nothing moves out of this folder.
- **LP1's own bar binds the parent.** Criterion 3 wants a render under LP1's law, which carries
  no words; the router-confusion test is LP1's anyway, since both siblings are LP1 types; and
  the session and golden checks learn the LP2 folder in the same diff (ADR-091).

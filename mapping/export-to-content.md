# Export → `content.json`

The step between a live flunnel page export and the QUERY operation's input.
`scripts/export-to-content.py` implements it; this file is its law. SPEC §1 makes
`content.json` QUERY's input; a real export satisfies none of that contract, and until
2026-09-11 nothing in this repo said how to get from one to the other.

Measured against the **57 flunnel page exports on disk** — 33 `advertorial`, 23 `listicle`,
1 `pdp_dr`, all `kind: flunnel-page-export`, `schemaVersion: 1`. Every one scaffolds without
error, and 847 in-scope image slots are placed between them.

**An earlier draft of this file said "two exports is what exists on disk" and generalised from
those two.** It was wrong on the count and wrong in two conclusions drawn from it — both
corrected below and recorded in ADR-083. The converter still refuses an unknown
`schemaVersion` rather than extrapolating past what has been measured.

## Where the structure actually is

The section structure is in `page.htmlCompiled`, and it is explicit:

```html
<section data-block-key="why" data-visible="true" data-locked="false" id="why">
  …<img data-field="why.cards.0.image" data-field-type="image" data-field-attr="src" …>
```

| | A | B |
|---|---|---|
| `data-field` occurrences / distinct | 141 / 139 | 245 / 245 |
| `<section data-block-key=…>` | 14 | 15 |
| `page.content` non-meta keys | 138 | 245 |
| **content keys carrying no marker** | **0** | **0** |
| `data-field-type="image"` | 24 | 28 |

That last row of zeroes is load-bearing: every addressable field is marked, so walking the
sections cannot miss one. The converter re-checks it on every run and warns if it stops
holding.

**Three things are NOT where the 2026-09-10 measurement put them**, and a converter written
to that measurement fails on the first call:

- **There is no `page.sections`.** The empty `sections` array is at the export's TOP level.
  `page["sections"]` raises `KeyError`; it does not return an empty list.
- **`htmlCompiled` is not unmarked.** It carries no `data-fl-key`, no `data-slot` and no
  mustache — three names it does not use. It uses `data-field`.
- `lpTypeId` — confirmed as measured, and now has a home (below).

## What is mechanical

Taken from the export, never invented:

- **`sections[].id`** ← **ADR-050's arithmetic on the slot id**, ordered by first appearance
  in the document — **not** `data-block-key`. The rule: the top-level prefix, plus the next
  segment when that segment is a number. Since ADR-087, `query/runbook.md` no longer derives
  sections from the slot id: Step 5d counts in the sections `content.json` DECLARES. So the
  grouping written here, split or not, is the grouping the motion rules count in. Across all 57 exports
  the markup and ADR-050 give the **same grouping on 27 and a different one on 30**, and where
  they differ the markup is coarser: the advertorial template wraps seven argument cards, a
  product shot, a closing card and four review photos in ONE
  `<section data-block-key="features">`. ADR-050 exists precisely to stop a template's
  packaging being read as the page's argument structure. Grouping by slot id also places an
  image that sits outside every `<section>`, so the "unplaced" case is gone.

  **A reader may SPLIT a section further, and should wherever an entry carries its own copy.**
  ADR-050 is the coarsest grouping the cross-slot rules allow, not the finest that is right.
  Since ADR-087, an entry with its own heading and body IS a section for Step 5d:
  `advertorial-cord-tensioner-cam-lock-v01` split `content.items.0` … `.6` into **seven**
  sections carrying **six** roles, because each card argues something different. Merging two
  is never right.
- **ORDER** ← the document's. `page.content` key order is not page order: grouped by prefix in
  stored order it gives **60 runs** over 15 blocks, because the keys are stored by string
  length; the same grouping over DOM order gives **17**.
- **`image_slots[].slot_id`** ← the `data-field` of each `data-field-type="image"` element.
  This is already the vocabulary sessions use by hand:
  `advertorial-cord-tensioner-cam-lock-v01/content.json` carries `hero.image`,
  `content.items.0.image`, `reviews.shots.0.image`.
- **`image_slots[].ratio`** ← the rendered box the markup states — `aspect-[a/b]` (435
  occurrences on image fields), `aspect-square` (695), `aspect-video` (6) — in preference to
  the `<img>` `width`/`height` attributes, then snapped to ADR-016's five and reported.
  `aspect-auto` (2) is not a ratio and is not read as one. **845 of 847 in-scope slots
  resolve.** The two that do not are `hero.image` on two seat-cushion pages carrying only
  `w-full rounded-md object-cover`; the scaffold names them and refuses to invent one. The
  only near-tie met so far is `how.poster` at 278:179 — 4:3 by 0.220, 16:9 by 0.225 — and it
  is a video poster, out of scope.
- **`product.name`, `personas`, `raw_features`, `specification`** ← `brief`.

**The markup does NOT encode ADR-050, and an earlier draft of this file said it did.** On the
two exports first examined the two rules happened to coincide, 30 slots out of 30. Across all
57 they coincide on 27 exports and diverge on 30 — 313 slots of 934. The coincidence was the
sample, not the rule. ADR-050 is authoritative here because it is the library's own answer to
this exact question, written from routed pages; `data-block-key` is kept in the worksheet as
`_block_keys`, provenance a reader can see and nothing routes on.

## What is judgement, and why each one is

Never guessed by the converter. It refuses to emit until each is answered.

- **`role` and `copy_summary`.** Role follows what a section's COPY argues, not which block it
  sits in. Measured: in `advertorial-cord-tensioner-cam-lock-v01`, **seven** sibling cards of
  ONE repeating block — `content.items.0` … `.6` — carry **six different roles**
  (problem-agitation, comparison, cause, mechanism, how-to-use, outcome, comparison). A
  block → role table collapses all seven into one and destroys the page arc
  `mapping/slot-rules.md` cross-rule 3 enforces. The worksheet carries each section's own copy
  so the assignment is made by reading it.
- **`page.channel`.** The export does not carry it. The router learned it by GUESSING from
  `lpTypeId` for five sessions running, which is half of why ADR-059 removed channel as an
  admission test. The converter will not repeat that guess.
- **The eight `product.attributes`.** Owner decision, 2026-09-11: **the app supplies them.**
  The converter validates and never derives. This is `query/runbook.md` Step 1's standing
  rule — *"Do not infer missing attributes — ask; inference here is the G7-X failure path"* —
  and the reason it is right is measurable. In export A the only colour words anywhere in the
  brief and page copy are *black*, *white* and *green*, and all three sit inside one sentence
  the brief itself labels *"buyer doubts to answer, **not facts about this product**"*. A
  keyword derivation harvests three colorways from a sentence that disclaims being about the
  product, and `colorways`'s own contract calls a fabricated one a G2 violation.
- **`product.category` and `problems_solved`.** Category is optional (ADR-085): a work file
  that leaves it undecided builds a `content.json` without it. Before ADR-085 `build` shipped
  the scaffold's placeholder sentence as the category, because the schema accepts any
  non-empty string.

## `page.lpTypeId`

Optional, provenance only, added to `mapping/content.schema.json` by ADR-081. **Nothing reads
it to route.** The converter reads it upstream, because it must: the two exports share no
argued block key at all —

```
A  hero trust why press product tank how reviews guarantee faq cta legal_privacy legal_terms legal_about
B  disclosure header content.0 content.1 content.2 content.3 compare reviews comments scarcity faq closing guarantee legal_privacy legal_terms
```

— so whatever maps a block to a page structure is per-`lpTypeId`. Measured over all 57:
listicle∩advertorial = 15 blocks (Jaccard **0.33**), listicle∩pdp_dr **0.14**,
advertorial∩pdp_dr **0.17**. The two LP1 members are about twice as close to each other as
either is to LP2, and what all three share is only furniture — `faq`, `guarantee`, `hero`,
`legal_*`, `reviews`. **So `lpTypeId` is finer than the page kind** (SPEC §3.0: LP1 has two
of them) and it is `lpTypeId`, not the page kind, that a block map is keyed on.

Recording which one ran is not the same as gating on it, and this is the treatment `channels`
already has: kept as a record of where something came from, read by nothing that admits or
refuses.

## Out of library scope

Dropped from the slot list, each against a written rule, not against the picture:

| pattern | rule |
|---|---|
| `*.logo`, `*.logos.N` | G6 bans logos outright |
| `*.avatar`, `*_avatar`, `*.bio_image` | `mapping/slot-rules.md`'s `author` row is empty by decision — its rationale names "a byline avatar, an About-the-author image, a comment thread of faces" |
| `product.gallery.0` | cross-rule 6 — the standard product shot |
| `*.poster` | a video poster frame, not an argued image |
| `*badge*` | a trust badge, not an argued image |

Across the 57 exports: **1392 image fields → 847 in scope, 545 dropped** (439 portrait of a named person; 87 brand or press logo; 17 trust badge, not an argued image; 1 first gallery image; 1 video poster frame, not an argued image). The `cta` block's
image is KEPT: `cta` is a ROLE that carries no image by definition, and SPEC §7.4 leaves that
to routing's `out_of_scope_reason`. The converter does not pre-empt a routing decision.

## Running it

```
python3 scripts/export-to-content.py scaffold EXPORT.json -o work.json
# fill every NEEDS-DECISION in work.json — channel, the eight attributes,
# category, problems_solved, and a role per section with images
python3 scripts/export-to-content.py build EXPORT.json -d work.json -o content.json
```

`build` validates its own output against `mapping/content.schema.json` using
`scripts/validate.py`'s own `schema_errors` — imported, not reimplemented, because two
validators drift and the one in the validator is the one CI runs — and exits 2 without writing
if it does not pass.

## What it refuses, proven

Nineteen faults were injected and **all nineteen fired**, with two clean controls, on
2026-09-11. Export-level: wrong `kind`; `schemaVersion` ≠ 1; no `page`; empty `htmlCompiled`;
a file that is not JSON. Scaffold: a `page.content` key with no marker; an image that sits
outside every `<section>` still being placed (real — `rail.image` in the mini-steam-iron
listicle lands in section `rail`); an image with no derivable ratio. Build: `channel` unanswered; no `product`; `attributes` left as the placeholder; `attributes`
missing 2 of the 8; a section with image slots and no role; two sections sharing an id; a slot
with no ratio; no section surviving; an empty `problems_solved`; a role outside the contract's
twelve. One warns rather than refuses: prose in `visible_output`.

**`visible_output` is the one gap the contract cannot close.** It is the only one of the eight
typed as an open `string`, and 4 of the repo's 15 `content.json` files carry 49–140 characters
of prose in it. `mapping/slot-rules.md` gates on `visible_output ≠ none`, which prose
satisfies — so G8 binds and the output becomes the primary subject by accident. Warned here;
making it an enum would fail four existing files and is a separate decision.

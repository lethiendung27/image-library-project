# Image Prompt Library — Specification

**Registry version: 2.0.0** · This file is the source of truth for how the library is
structured and consumed. Any harness (Claude Code, another LLM agent, an app, an API)
that follows this contract can operate the library. `CLAUDE.md` is only a thin adapter
for one client and must never contain logic that is not specified here.

The library turns a landing page's `content.json` into ranked, ready-to-run image
generation prompts, by routing page sections to **image types** — reusable, versioned
argument structures for e-commerce product imagery.

---

## 1. Consumption contract

A conforming harness implements five operations. **An app consuming `dist/app-bundle/`
normally implements QUERY alone** — the bundle is that operation's view of the library, and
the other four are the library's own loops.

| Operation | Input | Procedure | Output |
|---|---|---|---|
| **INGEST** | source images (outside repo) | `ingestion/runbooks/classify-batch.md` | appended records in `ingestion/observations.jsonl` |
| **CURATE** | observation ledger | `ingestion/runbooks/curate.md` | patches / staging candidates via PR (human gate) |
| **QUERY** | `content.json` valid against `mapping/content.schema.json` | `query/runbook.md` | JSON valid against `query/output.schema.json` |
| **LEDE** | the `product` block alone, extended — NOT `content.json` (§3.7) | `registry/toplist-instruction.md`, then `mapping/toplist-rules.md` | one prompt for the single lede image of a top-N page |
| **RENDER-TEST** | a filled prompt + the target model | `eval/render-test.md` | appended records in `eval/render-tests.jsonl`; patches via the evidence rule |

**LEDE is a fifth operation and it was missing from this table until 2026-09-11.** It takes a
different input from QUERY, runs a different procedure, and emits one image rather than a
routed page, which is why `registry/toplist-types/` is absent from `dist/app-bundle/` — the
bundle is the app's view of the QUERY operation, and until an app implements LEDE it would be
shipping law it cannot act on. `registry/pdp-dr-types/` is absent for the opposite reason: it
is INSIDE QUERY (§3.8), and promotion out of it is a `git mv` into `registry/types/`, so a
promoted type enters `index.yaml` and the bundle by itself.

Invariants any harness must respect:

1. `registry/index.yaml` is **generated** by `scripts/validate.py --write-index`. Never hand-edit it.
2. Routing reads **only** `registry/index.yaml` + `mapping/slot-rules.md`. Full type files are
   loaded only for the types selected for a slot (progressive disclosure).
3. `ingestion/observations.jsonl` and `feedback/picks.jsonl` are **append-only**. Corrections
   are new records, never edits.
4. Anything under `registry/types/_staging/` is **not routable**, and so is anything under
   `registry/pdp-dr-types/` while its `status` is `reserved` — which today is every file in
   it (§3.8, ADR-077).
5. Every change under `registry/` is validated by `scripts/validate.py` before commit.
   The human gate is the owner's explicit inputs — image feeds, picks, direct
   commands, and render verdicts where the owner gives them; once given, the harness
   curates and **commits autonomously**, one commit per operation with evidence cited
   in the message (ADR-007). Git history is the audit surface; rollback is
   `git revert`. Since ADR-011 the harness may also assign a render verdict itself,
   but **only for a render it has actually examined**, and never for promotion
   criterion §6.3(3), which still requires the owner's own verdict.
6. A harness that cannot read this repo directly consumes it through
   `dist/app-bundle/`, which is **generated** by `scripts/build-app-bundle.py`.
   Never hand-edit a file in it. The routing surface is shipped WHOLE:
   `index.yaml` already exists so routing never opens a type file (invariant 2),
   and a second reduction on top of it drops the fields the cross-slot rules of
   §7.3 need. `MANIFEST.json` records the source commit and a sha256 per file, so
   a stale vendor copy is a hash mismatch rather than a silently wrong answer.
   `eval/golden/` is the conformance contract between any two harnesses: both
   must derive the same Stage 1 shortlist for every fixture slot.

## 2. Data tiers

```
TIER 1  raw evidence      ingestion/observations.jsonl, feedback/picks.jsonl,
                          eval/render-tests.jsonl                              append-only
TIER 2  curated knowledge registry/ (types, vocabulary, rules)                 versioned, human-gated
TIER 3  routing surface   registry/index.yaml                                  generated from tier 2 (+ derived stats from tier 1)
```

Derived numbers (`evidence_count`, pick statistics) live **only in the generated index**,
computed from tier 1 at generation time. Type files never carry derived fields, so the
validator never mutates source files.

## 3. Registry model

### 3.0 Page kinds, and which corpus each registry was measured on

Owner statement, 2026-09-11. The repo used "LP2" in six places and had never said what LP1
was, which left a reader no way to know which corpus `registry/types/` came from.

| page kind | `lpTypeId` in an export | registry | notes |
|---|---|---|---|
| **LP1** | `listicle`, `advertorial` | `registry/types/` | **two `lpTypeId`s, one page kind** |
| **LP2** | `pdp_dr` | `registry/pdp-dr-types/` + `registry/types/` | the direct-response product detail page (§3.8) |
| **top-N listicle** | — | `registry/toplist-types/` | **a different kind, not LP-numbered** (§3.7) |

Three things follow, and the third is the one that bites.

**`lpTypeId` is not 1:1 with a page kind.** LP1 has two of them. Anything keyed on
`lpTypeId` — the converter's block map, for instance — is keyed finer than the page kind.

**A registry's corpus is not its routing scope.** `registry/types/` was MEASURED on LP1 and
is USED by every page kind: ADR-059 made the library a set of image types usable on any page,
and an LP2 page routes to both registries (ADR-077 answer 1). Where a clause in a type file
cites renders, those renders are LP1's unless the file says otherwise — which is what
ADR-073 proved matters when a ground rule measured on one corpus had to be re-measured for
another and split the namespace in two.

**Measured, so the grouping is not taken on faith.** Across the 57 flunnel exports on disk
(33 `advertorial`, 23 `listicle`, 1 `pdp_dr`), comparing the set of `data-block-key` values
each kind uses: listicle∩advertorial = 15 blocks, Jaccard **0.33**; listicle∩pdp_dr **0.14**;
advertorial∩pdp_dr **0.17**. The two LP1 members are about twice as close to each other as
either is to LP2 — and what they share includes argued blocks (`content.items.0`…`.5`),
while all three share only furniture (`faq`, `guarantee`, `hero`, `legal_*`, `reviews`).
**They are one kind by family resemblance, not by a common template**, and a converter still
needs a block map per `lpTypeId`.

### 3.1 Type identity

A type's identity is its **argument structure**: `{step}-{job}-{device}`, lowercase,
hyphenated (e.g. `01-pain-split`). `job` and `device` must exist in
`registry/vocabulary.yaml`. Two images with the same argument structure are the same
type regardless of subject matter; two images with different jobs are different types
regardless of visual similarity.

### 3.2 Absorption ladder (anti-explosion rule)

Every new image is absorbed at the **cheapest level that fits**, tried strictly in order:

1. **Parameter** — runtime value (ratio, colorway, panel count). Changing it does not change the argument.
2. **Axis value** — a cross-cutting presentation dimension defined globally in `vocabulary.yaml`
   (e.g. `register: ugc`). Same argument, different presentation, applicable to several types.
3. **Variant** (`--slug`) — same job+device, exactly **one** structural decision differs.
   Defined inside the parent type file as a diff-only block.
4. **New type** — different job or device; a genuinely new argument. Goes to `_staging/`,
   or to `registry/pdp-dr-types/` where the cluster was measured on the LP2 product-gallery
   corpus (§3.8). The corpus a cluster came from decides which, and a draft never sits in
   both.

A classifier may only escalate a level after the lower level demonstrably fails.

### 3.3 Anatomy of a type file

Required sections, in order: `PURPOSE`, `TRIGGER`, `SKELETON`, `NEGATIVE`, `CHANGELOG`.
Optional sections: `PARTS`, `MARKS`, `SLOT CONSTRAINTS`, `VARIANTS`,
`WORKED EXAMPLES`, `KNOWN-FLAKY`, `NOTES`. `PARTS` and `MARKS` are a type's own
callable definitions: the skeleton names an entry and the definition lives in the
section once, never restated in the skeleton. At render time a called definition is
**expanded into the prompt** and carried there once — the model never reads the type
file, so a name that is not expanded reaches it as a bare word. This is the same
treatment global rules already get (`adapters/` Rule 6.2): referenced by ID in the type
file, expanded at render time. A type's mark library is its own (ADR-012); a mark that
looks the same in two types is noted in both rather than owned centrally.

- `TRIGGER` contains a `use_when: >` folded block written in **router
  language** (section roles, buyer state, channel). It is extracted verbatim into the index.
- `SKELETON` and `SLOT CONSTRAINTS` are written in **filler language** (instructions to the
  image model). Slots use `[brackets]`.
- `VARIANTS` blocks contain **diffs only** — never restate the whole skeleton.
- `WORKED EXAMPLES`: hard cap **2** per type, curated. Header format (enforced):
  `### example: <slug> — skeleton@<version>, run: <untested|pass|partial|fail>`.
  An example whose skeleton major version lags the type's current major is flagged stale.
  **Form follows evidence.** An example with `run: pass|partial` keeps its FULL prompt
  text: that text is the only record of what actually rendered, since the render ledger
  stores verdicts and not prompts. Every other example is stored **diff-only** — a
  product-and-parameter line, then one line per skeleton slot carrying only the fill.
  The skeleton supplies the structure, the example supplies the values, and neither
  repeats the other (the same rule VARIANTS already follow). An example that is later
  rendered is rewritten to full text in the same diff that records its verdict.
- `KNOWN-FLAKY` holds one-off observed failures. Promotion into `SKELETON`/`NEGATIVE`
  requires the ≥2/3 recurrence rule with observation evidence (see 6.2).
- `CHANGELOG` entries must cite evidence: observation hashes, or for the founding corpus,
  the seed document (see `decisions/log.md`, ADR-001).

### 3.4 Frontmatter schema

```yaml
id: 01-pain-split            # required; must equal filename and match {NN}-{job}-{device}
step: 1                      # required; integer, must match id prefix
job: pain                    # required; in vocabulary.jobs
device: split                # required; in vocabulary.devices
version: "1.2"               # required; semver-ish "MAJOR.MINOR"
status: active               # required; active | reserved | deprecated
replaced_by: null            # required non-null when status: deprecated
channels: [marketplace]      # required; subset of vocabulary.channels
requires_product_photo: true # required
generation_mode: single-pass # required; the ONLY legal value, ADR-067
axes: {}                     # optional; map axis → supported values (subset of vocabulary.axes)
variants: []                 # optional; list of --slug names defined in VARIANTS section
exempt_from: []              # optional; rule IDs from registry/rules.md
pairs_with: []               # optional; type ids
never_with: []               # optional; type ids
avoid_adjacent: []           # optional; type ids (spacing rule within one page/gallery)
requires_pair: null          # optional; type id that must co-exist on the page
```

**YAML subset (enforced by the validator — anything outside it is a validation error):**
scalars (plain or double-quoted strings, integers, booleans, `null`), flow lists
`[a, b, "c"]`, block lists (`- item`), and one level of nested mapping (2-space indent,
used for `axes:`). No anchors, no multi-line scalars in frontmatter, no deeper nesting.

### 3.5 Versioning

- **MINOR** bump: slot patch, constraint change, variant added, negative changed.
- **MAJOR** bump: layer structure changes (panels added/removed, zones restructured).
- Registry-wide `registry_version` lives in the generated index and in `vocabulary.yaml`.
- Deprecated types stay in the registry with `replaced_by`; nothing is ever deleted.

### 3.6 GIF types

A second, smaller registry governs motion (ADR-023). It is a **separate namespace** from
image types: ids are arguments rather than `{step}-{job}-{device}`, and it is never
written into `index.yaml` because routing reaches a gif type by id off a slot's own `gif`
verdict, not through a shortlist.

- Files live in `registry/gif-types/<id>.md`; ids are the closed list `vocabulary.gif_types`.
- Required sections, in order: `PURPOSE`, `TRIGGER`, `BOUNDARY`, `BRIEF`, `NEGATIVE`,
  `CHANGELOG`. `BOUNDARY` is the anti-overlap section: it states how this type is told
  apart from each adjacent one, and a type without it cannot be filed against.
- Frontmatter: `id`, `kind` (a `jobs` value, or `null` where the type never reaches a
  routed slot), `group` (`working | result | none`, which half of the motion floor it
  serves), `rung`, `version`, `status`, `channels`, `duration_s`, `beats`.
- **One type, one message.** A GIF with several beats is filed by its dominant argument.
  The absorption ladder of §3.2 applies with one substitution: in motion, beat count is a
  PARAMETER, so a single act and a multi-step sequence are one type.
- Law shared by every type is stated once in `registry/gif-instruction.md` and never
  restated in a type file, exactly as §5 treats global rules.
- Assets live **outside the repo** and are indexed by `ingestion/gifs.jsonl`, append-only,
  one record per file: `ts`, `sha256`, `type`, `file`, and the description line. A loop has
  ONE name, page-side and library-side alike —
  `{page-type}-{gif-type}-{product-slug}-v{NN}.mp4` (ADR-037, restored at ADR-056) — and a
  filed file is never renamed. What keeps it unique is a rule rather than a field: **one loop
  per gif type per page**, restored with the name it protects. The type in the name says which
  library folder the file belongs in; the slot it fills lives in `prompts.json` and on the
  plate. Delivery is mp4 or webm, muted; `.gif` never ships.
- The folder cards an editor browses are **generated** from the type files by
  `scripts/gen-gif-cards.py`. Like `index.yaml`, a card is a view and is never hand-edited.
  Each folder carries two: `README.md` in English and `README.vi.md` in Vietnamese. The
  Vietnamese card is the one **named exception** to the English-artifact rule, because its
  reader is an editor filing files rather than a harness reading law; its copy lives in
  `registry/gif-cards-vi.md` and the validator fails a gif type that has no entry there
  (ADR-044).
- How many loops a page may carry, and how a shortfall is handled, is `query/runbook.md`
  Step 5d. Whether a given slot earns one is Step 5c.

### 3.7 Toplist types

A third registry governs the **single lede image of a top-N listicle** (ADR-069) — the
lead, featured or hero image of a "best 5 X" page. It is a **separate namespace** from
image types for the reason §3.6 gives for gif types: that page carries ONE image slot, so
the role shortlist of §7.2, the cross-slot pass of §7.3, the coverage pass of §7.5 and
one-type-once have nothing to act on, and it is never written into `index.yaml`.

- Files live in `registry/toplist-types/<id>.md`; ids are the closed list
  `vocabulary.toplist_types` and are **arguments** rather than `{step}-{job}-{device}`.
- Required sections, in order: `PURPOSE`, `TRIGGER`, `BOUNDARY`, `SKELETON`, `NEGATIVE`,
  `CHANGELOG`. `BOUNDARY` is the anti-overlap section and carries the same weight it does
  for gif types: with one slot the whole namespace competes for one image, so a type that
  cannot be told from its neighbour cannot be chosen against it. A `reserved` type also
  owes a `BLOCK` section naming the decision it waits on.
- Frontmatter: `id`, `version`, `status`, `replaced_by`, `products_in_frame`
  (`one | many | none`), `requires_product_photo`, `awareness` (values from
  `vocabulary.toplist_awareness`), `copied_from` (an ACTIVE image type id, or null),
  `copied_at_version` (non-null exactly when `copied_from` is), `blocked_by` (non-null
  exactly when `status: reserved`), `exempt_from`.
- **Input is the `product` block, not `content.json`.** `content.json` is
  `{ product, page }`; a top-N page has no `page.sections` to route and, since ADR-059,
  `page.channel` admits nothing. This namespace consumes the product half alone, extended
  with the fields `registry/toplist-instruction.md` lists as missing.
- **A toplist type MAY declare `text_layer`** (ADR-071), from the same closed slot list
  as an image type, and **G16 binds the types that do**. Which types carry one is settled
  by corpus evidence rather than by permission: today `lede-winner` and `lede-collage` do,
  and the other five do not because their observations carry no text. What stays refused
  is another party's mark and a fabricated endorsement, neither of which the permission
  covered. The ground rule is this namespace's own, measured on its own corpus
  (ADR-073); nothing is imported from the product-page registry.
- **Ratio is not declared.** The consuming app resolves the lede ratio, so these types
  carry no `ratios` key; ADR-016's ban on writing a ratio into prompt text is unchanged.
  **This stopped being peculiar to this namespace on 2026-09-11**: ADR-082 removed `ratios`
  from every image type too, on the same reasoning one registry had already proved.
- **Copying, made auditable** (ADR-070). A type declaring `copied_from` carries the
  parent's text verbatim rather than pointing at it, so the file stands alone. The
  parent's `WORKED EXAMPLES` and `CHANGELOG` are not copied: an example's prompt text is
  the record of what actually rendered, and those renders were the parent's.
  `copied_at_version` records the parent's version at the copy, and the validator warns
  when the parent moves past it — two copies of one file drift, and this is the instrument
  that makes the drift say so. A gate keyed on the parent's id does not reach a copy, so
  every such gate is restated by toplist id in `mapping/toplist-rules.md`.
- Law shared by every toplist type is stated once in `registry/toplist-instruction.md`
  and never restated in a type file, exactly as §5 treats global rules.
- Selection runs in four layers, of which only the second reads the reader's awareness
  stage: mechanical admission, then the preference order in `mapping/toplist-rules.md`
  (declared a hypothesis), then FIT by judgement citing the sentence of product copy that
  decided it (ADR-059's own mitigation), then the pick-rate prior of §7.7.

### 3.8 PDP-DR types

A fourth registry governs the **image gallery of a direct-response product detail page**,
LP2 (ADR-077). It is a **separate namespace** from image types, and it is separate for
none of the reasons §3.6 and §3.7 give: a product gallery carries about twelve slots, so
the role shortlist of §7.2, the cross-slot pass of §7.3, the coverage pass of §7.5 and
one-type-once all apply to it, harder than they apply to an advertorial. It stands on
three differences of LAW instead — text baked into the image (owner decision 2026-08-31),
a ground rule measured on its own corpus (ADR-068), and marketplace legality gating every
tile. Like the other two namespaces it is never written into `index.yaml`.

- Files live in `registry/pdp-dr-types/<id>.md`; ids are the closed list
  `vocabulary.pdp_dr_types`.
- **Ids keep the `{step}-{job}-{device}` grammar**, unlike gif and toplist ids, which are
  arguments. This namespace is a **co-registry**: a PDP page routes to `registry/types/`
  and to this folder in one pass, and two id grammars in one pass is how a reader loses
  track of which law applies. Promotion out is a `git mv` and a status change, never a
  rewrite.
- **Anatomy and frontmatter are an image type's** (§3.3, §3.4) — same required sections,
  same keys — plus `blocked_by`, which is non-null exactly when `status: reserved`. A
  reserved type also owes a `BLOCK` section naming the decision or the evidence it waits
  on. There is no separate `BOUNDARY` section: an image type carries its discriminator
  inside `use_when`, which is where ADR-060 put the whole trigger, and a second home for it
  would be a second place to go stale.
- **No copies, and therefore no drift instrument.** ADR-070 gave `registry/toplist-types/`
  `copied_from` + `copied_at_version` and a validator warning because the owner had chosen
  verbatim copies. Nothing here is a copy of an active type, so that machinery is absent.
  The residual exposure is a skeleton CALLING a part defined in another file, which nothing
  validates; every such call is registered in `mapping/pdp-dr-rules.md` and the register is
  the whole instrument.
- **Input is the whole `content.json`**, unlike §3.7. A product gallery has
  `page.sections`, the slots are real, and §7 runs unchanged. The first gallery image is out
  of library scope — a standard product shot (`mapping/slot-rules.md`, cross-rule 6).
- **A PDP-DR type MAY declare `text_layer`** and G16 binds the types that do. Two rows of
  G16 are LAW rather than taste and no type-scoped permission reaches them: a named-person
  or named-profession endorsement (G14 binds the SLOT), and a certification, award, rating
  or press mark (the trademark question, put to the owner 2026-08-18 and declined).
- Law shared by every type is stated once in `registry/pdp-dr-instruction.md` and never
  restated in a type file, exactly as §5 treats global rules. Routing is
  `mapping/pdp-dr-rules.md`, whose preference table is **measured** from the 159-observation
  corpus rather than declared a hypothesis.
- **Every file is `status: reserved` at the namespace's founding** and nothing in it routes.
  What routes on a PDP page today is the shared active types in `registry/types/`.

## 4. Vocabulary governance

`registry/vocabulary.yaml` holds **closed lists**: steps, jobs, devices, axes, channels,
generation modes, statuses, section roles, observation verdicts. Adding a value is a
taxonomy decision of the same weight as adding a type: PR + human review. The validator
fails on any value not in the vocabulary.

## 5. Rules and exemptions

`registry/rules.md` defines global laws with stable IDs (`G1`…). Each rule declares its
**scope** (which registers/layers it binds). Types opt out only via `exempt_from`, and
only where the rule's own scope notes permit it. Types reference rules by ID and never
copy rule text.

## 6. Ingestion protocol (runbook-only)

### 6.1 Classification

- Batch sessions of ~15–25 images (full-breakdown records; measure and adjust).
- The ledger is the checkpoint: `to-do = manifest hashes − hashes already in observations.jsonl`.
- The classifier context contains **only** `registry/index.yaml` + `registry/vocabulary.yaml`
  + the template `ingestion/prompts/classify.md`. Full type files are loaded only to
  compare slots on a suspected match.
- Every record carries `template_version`. Template changes bump it; curation discounts
  records from older templates.
- Calibration: re-classify the anchor set every ~5 batches
  (`ingestion/runbooks/calibrate.md`). Drift → fix the template, never the session.

### 6.2 Curation and the evidence rule

- A skeleton/negative patch requires the deviation to appear in **≥2/3 of runs or ≥3
  distinct observations** for that type. One-off issues go to `KNOWN-FLAKY`.
- Render-test results (`eval/render-test.md` → `eval/render-tests.jsonl`) are the
  second evidence stream and feed the same rule — a tested library is the product;
  worked-example `run:` statuses advance only through this loop.
- Model-weakness failures (hands, text, faces) are pushed to `NEGATIVE`, not into
  longer descriptions.
- Failures of ARGUMENT — where a render is correct in every slot and wrong in what it
  says — go to `registry/argument-faults.md`, not into the type that found them. They
  recur across types and are read before the first prompt of any new type (ADR-014).
- Ambiguous slots are split into two specific slots rather than padded.

### 6.3 Promotion (staging → active)

All four required: (1) **≥5 distinct exemplars** (distinct sources, non-near-duplicate)
in the ledger; (2) passes the **router-confusion test** — with the candidate's trigger
added to the index, 5 fixture briefs route without stealing an existing type's cases;
(3) **≥1 worked example** actually rendered (`run:` pass or partial, always an
owner-confirmed verdict); (4) the ADR-007 gate: criterion 3's owner verdict plus the
standing autopilot authorization — the assembled promotion commits autonomously and
is reported prominently with its revert path.
Demotion: `deprecated` requires `replaced_by`; a type with no new evidence and no picks
for 6 months is flagged `review-for-merge` (in curation, not automated).

### 6.4 Source images

Images live **outside the repo** (local folder / drive / bucket), identified by
`sha256`. One asset folder holds three siblings that must not be conflated:
`stills/` is the market corpus and the ONLY thing the classification manifest reads,
`feedback/` is this library's own render output, and `gifs-library/` is the GIF
library (§3.6). Classifying the library's own renders as market observations would corrupt
§6.2's evidence rule — ADR-025. Observation records reference the hash; an optional `source_ref` field is
machine-specific and non-authoritative. Never commit source images. Policy: the library
learns **structure, not pixels** — no prompt may aim to reproduce a specific source
image, and competitor brand marks never appear in prompts.

**One named exception: the toplist namespace of §3.7** (owner instruction, 2026-09-09,
ADR-075). A top-N listicle is by definition about several named competing products, so the
clause would refuse the format's whole subject. It does not bind
`registry/toplist-types/`. The other half of this policy — no prompt may aim to reproduce a
specific source image — binds there as it binds everywhere.

## 7. Query protocol

1. **Validate** `content.json` against `mapping/content.schema.json`.
2. **Stage 1 — shortlist** (mechanical, DERIVED): per slot, take **every active type**
   in `registry/index.yaml` and drop only those the **attribute gates** in
   `mapping/slot-rules.md` kill, then rank by **role affinity**, read from the type's
   `step` and `job` (both already in the index). `mapping/slot-rules.md`'s table is a
   human-readable **view** of the preference order, not the pool.

   **Channel is not an admission test** (ADR-059). It was, until 2026-08-26: a type
   whose `channels` did not contain the page's channel was killed at any rank. Two
   things broke that. The library is now a set of image types usable on ANY page kind
   — a customer may take an advertorial template and write listicle copy into it — so
   the page's kind is not knowable from the template. And the router only ever learned
   the channel by GUESSING it from `lpTypeId` (`listicle` → `advertorial`, five
   sessions running), so the gate was keyed on a derived guess. **What the copy argues
   decides; the surface it will sit on does not.** `channels` stays in frontmatter as
   provenance — where a type's register has been proven — and is still validated
   against the vocabulary, but nothing reads it to admit or refuse an image type.
   Deriving rather than looking up is what makes the shortlist non-empty: every active
   type is a candidate, so a slot runs out only if every one of them is gated out,
   which the gates make explicit rather than silent.
3. **Stage 2 — portfolio** (judgment, one pass over the whole page): apply
   `product.attributes` against skeleton conditionals; enforce
   cross-slot constraints (`pairs_with`, `never_with`, `avoid_adjacent`,
   `requires_pair`, pain→relief arc). The page is selected as a **set**, never
   slot-by-slot greedily.
4. **Options**: **3 per slot, each a DISTINCT active type** — the three best fits for
   that slot's content, ranked. `varies_on` labels each: A is `baseline`, B and C are
   `type: <id>`. Axis and execution are how an option is EXECUTED, never how the pool is
   filled — a slot that returns one type three ways has answered a different question
   than the one asked. Options carry `composition_notes` so a human picking per-slot
   cannot silently violate a cross-slot rule.
   **Never-empty rule**: an image slot ALWAYS returns at least one renderable option,
   and every option is a real active type carrying that type's laws. There is no
   fallback tier and no unrouted image: Stage 1 derives from the whole channel-legal
   set, not from one table cell, so exhausting a cell is not exhausting the registry.
   When the obvious type is spent by one-type-once, take the next by role affinity and
   say so in `varies_on`. `out_of_scope_reason` survives only for slots that carry no
   image by definition — the `cta` cell and text furniture (comment threads, pricing
   tables). Refusing to route a *wrong* type is still correct; refusing to deliver an
   image is not, and the two were conflated.
5. **Coverage pass** (product-driven, after the sections are routed): compute which
   Trust Ladder rungs the routed slots cover and which are absent, then weigh each
   absence against the reader's awareness stage — **read from the page's own copy, not
   declared as an input field** — because **an absent rung is not automatically a
   gap**. Rungs the stage says matter become `recommended[]`: additive proposals, each
   naming the rung it fills and where it would sit, bound by the same admission tests
   and cross-slot rules as any option. Never keyed on page format: two listicles at
   different awareness stages need different rungs, so no format → rungs table exists.
   Every image slot also carries a `gif` verdict, positive or negative, per
   `query/runbook.md` Step 5c.
6. **Variations**: every image slot offers **at least 2** options. The floor is met by
   execution when no second type or axis is legal — a different staging of the same
   argument is a real named dimension, unlike a reroll of the same prompt, which stays
   banned.
7. **Tie-breaker**: pick-rate per (type × section role) from `feedback/picks.jsonl` is a
   soft prior, consulted **only** when a (type × role) cell has **≥20 contested
   observations**. A slot counts toward a cell only where it offered **more than one
   distinct type**, and it counts **once per distinct type on offer**, never once per
   option: several executions of one type is a real choice but not a choice between
   types, and a single-option repeating tile is no choice at all. Counting per option
   let one review wall fill a cell six times from one decision, so the first cell to
   go live would have been the one where nothing was ever chosen (ADR-026). The prior
   never overrides an attribute gate or a composition rule.
8. **Render**: fill skeletons (worked examples serve as few-shot), then apply
   `adapters/<model>.md` at render time. Canonical NEGATIVE lists are model-agnostic;
   adapters translate them (e.g. semantic negatives for nano banana).
9. **Feedback**: after the human picks, append one record per slot to
   `feedback/picks.jsonl` with a one-line reason.

## 8. Validation contract

`python3 scripts/validate.py` (stdlib only, Python ≥3.9):

- default: validate everything, print report, exit non-zero on errors;
- `--write-index`: additionally regenerate `registry/index.yaml`;
- `--check`: fail if the committed index differs from what would be generated (CI mode).

Checks: frontmatter schema + YAML subset; id/filename/step/job/device coherence;
vocabulary closure; referential integrity (`pairs_with`, `never_with`, `replaced_by`,
`requires_pair`, `avoid_adjacent`, `exempt_from`); required sections; trigger
extraction; worked-example count and staleness; ledger line validity; JSON schema files
parse; **every `content.json` against `mapping/content.schema.json`** — each session's and
each golden fixture's, the contract §1 says the QUERY input satisfies (ADR-035); index
freshness.

Run it after **every** edit under `registry/`.

**Commit policy (ADR-007):** a completed operation (classify batch, curation pass,
promotion, render-test session) auto-commits when the validator reports 0 errors;
warnings are allowed but must be surfaced in the commit message. One commit per
operation; never auto-push; every commit is reported with its hash and revert path.

## 9. Repo map

```
SPEC.md                  this contract
CLAUDE.md                thin Claude Code adapter
registry/                tier 2 + generated tier 3 (index.yaml)
registry/argument-faults.md  cross-type catalogue of argument faults (ADR-014)
registry/gif-types/      motion registry — one file per gif type (SPEC 3.6, ADR-023)
registry/gif-instruction.md  law shared by every gif type; never restated in one
registry/toplist-types/  top-N lede registry — one file per type (SPEC 3.7, ADR-069)
registry/toplist-instruction.md  law shared by every toplist type; never restated in one
mapping/toplist-rules.md selecting the lede image; layer 2 is a declared hypothesis
registry/pdp-dr-types/   LP2 product-gallery registry — a CO-REGISTRY, same id grammar
                         and anatomy as registry/types/ (SPEC 3.8, ADR-077)
registry/pdp-dr-instruction.md  law shared by every pdp-dr type; never restated in one
mapping/pdp-dr-rules.md  routing a product gallery; preference table is MEASURED, and it
                         carries the cross-file CALL REGISTER nothing else validates
ingestion/               classify template, runbooks, observations ledger
ingestion/gifs.jsonl     append-only index of the external GIF library
scripts/gen-gif-cards.py generates the library's folder cards from the gif type files
scripts/build-app-bundle.py  generates dist/app-bundle/ — the library as an app vendors it
dist/app-bundle/         generated; never hand-edited (SPEC 1, invariant 6)
mapping/                 content.json schema + role→type routing table
mapping/export-to-content.md  the step from a live flunnel page export to a content.json
                         (ADR-081). NOT a sixth operation: it PRODUCES QUERY's input rather
                         than consuming the library's rules, so no harness implements it
scripts/export-to-content.py  implements that step — `scaffold`, then `build`
query/                   query runbook + output schema
adapters/                per-model rendering transforms
feedback/                picks ledger
eval/golden/             routing regression fixtures (update in the same PR as intended route changes)
eval/render-test.md      the skeleton test loop; results in eval/render-tests.jsonl
decisions/log.md         append-only ADR log
scripts/validate.py      validator + index generator
```

Seed corpus: `conversation.md` (authoritative end state) and
`aif-image-type-registry-v1.2.md` (earlier snapshot, superseded — see ADR-002).

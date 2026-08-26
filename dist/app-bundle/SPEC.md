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

A conforming harness implements three operations:

| Operation | Input | Procedure | Output |
|---|---|---|---|
| **INGEST** | source images (outside repo) | `ingestion/runbooks/classify-batch.md` | appended records in `ingestion/observations.jsonl` |
| **CURATE** | observation ledger | `ingestion/runbooks/curate.md` | patches / staging candidates via PR (human gate) |
| **QUERY** | `content.json` valid against `mapping/content.schema.json` | `query/runbook.md` | JSON valid against `query/output.schema.json` |
| **RENDER-TEST** | a filled prompt + the target model | `eval/render-test.md` | appended records in `eval/render-tests.jsonl`; patches via the evidence rule |

Invariants any harness must respect:

1. `registry/index.yaml` is **generated** by `scripts/validate.py --write-index`. Never hand-edit it.
2. Routing reads **only** `registry/index.yaml` + `mapping/slot-rules.md`. Full type files are
   loaded only for the types selected for a slot (progressive disclosure).
3. `ingestion/observations.jsonl` and `feedback/picks.jsonl` are **append-only**. Corrections
   are new records, never edits.
4. Anything under `registry/types/_staging/` is **not routable**.
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
4. **New type** — different job or device; a genuinely new argument. Goes to `_staging/`.

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

- `TRIGGER` contains `use_when: >` and `avoid_when: >` folded blocks written in **router
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
ratios: ["1:1", "4:5"]       # required; runtime parameters, never identity
channels: [marketplace]      # required; subset of vocabulary.channels
requires_product_photo: true # required
generation_mode: single-pass # required; multi-pass is DEPRECATED, ADR-041
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

## 7. Query protocol

1. **Validate** `content.json` against `mapping/content.schema.json`.
2. **Stage 1 — shortlist** (mechanical, DERIVED): per slot, take every active type in
   `registry/index.yaml` that satisfies, in order:
   (a) **channel legality** — the slot's channel appears in the type's own `channels`;
   (b) **attribute gates** — the deterministic kill-rules in `mapping/slot-rules.md`;
   then rank by **role affinity**, read from the type's `step` and `job` (both already
   in the index). `mapping/slot-rules.md`'s shortlist table is a human-readable **view**
   of the same derivation, and `scripts/validate.py` fails if the two disagree — the
   table may never claim a channel a type does not declare. Deriving rather than
   looking up is what makes the shortlist non-empty: on any channel several types are
   legal, so a slot runs out only if every one of them is gated out on attributes,
   which the gates make explicit rather than silent.
3. **Stage 2 — portfolio** (judgment, one pass over the whole page): apply
   `product.attributes` against skeleton conditionals and `avoid_when`; enforce
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
   never overrides `avoid_when` or composition rules.
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
ingestion/               classify template, runbooks, observations ledger
ingestion/gifs.jsonl     append-only index of the external GIF library
scripts/gen-gif-cards.py generates the library's folder cards from the gif type files
scripts/build-app-bundle.py  generates dist/app-bundle/ — the library as an app vendors it
dist/app-bundle/         generated; never hand-edited (SPEC 1, invariant 6)
mapping/                 content.json schema + role→type routing table
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

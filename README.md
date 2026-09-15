# Image Prompt Library

**This repo is a data library, not an app.** It holds the rules for generating
direct-response product imagery — what each kind of image argues, how it is built, and what
it may not claim — together with the evidence behind every rule.

Nothing here runs a model. An application *consumes* this library and does the generating.

## Start here

| you are… | read, in this order |
|---|---|
| **building the consuming app** | this file → `SPEC.md` §1 (the contract) → §7 (routing) → `dist/app-bundle/` |
| **adding or editing a rule** | `SPEC.md` §3 (registry model) → §6 (evidence) → the type file → `decisions/log.md` |
| **running Claude Code here** | `CLAUDE.md` — a thin adapter, entry points only, no logic |
| **wondering why a rule exists** | `decisions/log.md`, append-only, 91 ADRs, every one cites its evidence |

## What an app actually consumes

**`dist/app-bundle/` — generated, never hand-edited.** 42 files as of 2026-09-15, each with a
sha256 in `MANIFEST.json`, which is the live count — this line said 34 through two bundle
changes. An app vendors a copy and compares `source_commit` plus the per-file hashes
against what it vendored; a mismatch means the vendor copy is stale rather than silently
wrong.

```
python3 scripts/build-app-bundle.py            # regenerate
python3 scripts/build-app-bundle.py --check    # fail if stale (CI)
```

The bundle is grouped by the call that reads it — `route`, `fill`, `contract`, `gif`, `input`
(the export converter and its law) and `conformance` (the golden fixtures) — and
`scripts/build-app-bundle.py` explains at the top why each file is in it and why two
namespaces are deliberately not.

## The five operations

`SPEC.md` §1 is the contract and defines all five with input, procedure and output. In brief:

| | input | output |
|---|---|---|
| **INGEST** | source images (outside the repo) | records in `ingestion/observations.jsonl` |
| **CURATE** | the observation ledger | staging candidates, via a human gate |
| **QUERY** | `content.json` | JSON valid against `query/output.schema.json` |
| **LEDE** | the `product` block alone | one prompt for a top-N page's lede image |
| **RENDER-TEST** | a filled prompt + the model | records in `eval/render-tests.jsonl` |

**An app implementing QUERY is the common case.** It reads `content.json`, routes each slot
against `registry/index.yaml` + `mapping/slot-rules.md`, opens only the selected type files,
and emits prompts. `query/runbook.md` is the procedure, step by step.

## Feeding it from a real page

**A live page export does not satisfy the QUERY input contract, so there is a step in
between — and since 2026-09-11 this repo specifies it.** `mapping/export-to-content.md` is the
law and `scripts/export-to-content.py` runs it:

```
python3 scripts/export-to-content.py scaffold EXPORT.json -o work.json
python3 scripts/export-to-content.py build EXPORT.json -d work.json -o content.json
```

It is mechanical about structure and refuses to guess judgement. Slot ids, ratios and their
order come out of `page.htmlCompiled`, which carries a `data-field` on every bound element —
every addressable key marked, across all 57 exports on disk. Sections are ADR-050's grouping
of the slot ids, **not** the markup's `<section>` elements: the two agree on 27 exports and
differ on 30, and where they differ the markup packages several argument beats into one
styling container (ADR-083). That grouping is what the converter declares, and the declared
sections are what the motion rules count in (ADR-087). What it will not invent: `role` and `copy_summary`
(measured: seven sibling cards of one repeating block carry six different roles, so no
block → role table is safe), `page.channel` (ADR-059 — the router used to guess it from
`lpTypeId`), and the eight `product.attributes`, **which the app supplies** (owner decision,
2026-09-11). `page.lpTypeId` now has a home in `mapping/content.schema.json` as provenance
that nothing routes on (ADR-081).

The correction worth carrying: the 2026-09-10 reading of this problem put two of its three
findings in the wrong place. There is no `page.sections` at all — the empty array is
top-level — and `htmlCompiled` is fully marked up, just not under any of the three attribute
names that were searched for.

## Validate everything

```
python3 scripts/validate.py            # report; non-zero exit on errors
python3 scripts/validate.py --check    # CI: also fail if index.yaml is stale
```

Stdlib only, Python ≥3.9. It checks frontmatter schema, id coherence, vocabulary closure,
referential integrity, required sections, ledger validity, and **every `content.json` in the
repo against `mapping/content.schema.json`** — each session's and each golden fixture's.

Run it after every edit under `registry/`. `eval/golden/` holds routing regression fixtures;
update them in the same commit as an intended route change.

## How this library decides things

Four habits explain most of what looks unusual here, and a consumer is better off knowing
them than inferring them:

1. **A clause belongs in a rule only when a render failed without it.** Rules cite the
   renders that produced them, with counts. Where a clause is untested, it says so.
2. **Evidence is counted in distinct SOURCES, not observations.** Five frames from one page
   are one source. `SPEC.md` §6.3 is the promotion bar.
3. **Generated views are never hand-edited** — `registry/index.yaml`, the app bundle, the GIF
   folder cards. Edit the source, regenerate.
4. **Append-only ledgers.** `ingestion/observations.jsonl` and `feedback/picks.jsonl` take
   corrections as new records, never edits.

## Known gaps, as of 2026-09-11

Stated rather than left to be found:

- **`visible_output` is an open string, not an enum** — the only one of the eight, and 4 of
  the repo's 15 `content.json` files carry prose in it. `mapping/slot-rules.md` gates on
  `≠ none`, which prose satisfies, so G8 binds by accident. The converter warns; closing it
  would fail those four files and is a separate decision
- **`feedback/picks.jsonl` is empty**, so `SPEC.md` §7.7's pick-rate prior has no data and
  one of the five ranking criteria is inert
- **`registry/pdp-dr-types/` routes nothing** — fifteen files, all `reserved`, three of them
  past the evidence bar and blocked on router-confusion tests that have not been run
- **no app implements LEDE**, which is why `registry/toplist-types/` is not in the bundle

## Layout

`SPEC.md` §9 is the full repo map. The short version: `registry/` holds the rules,
`mapping/` the schemas and routing tables, `query/` the procedure and output contract,
`ingestion/` and `eval/` the evidence, `decisions/` the reasoning, `scripts/` the generators
and the validator, `dist/` the generated bundle.

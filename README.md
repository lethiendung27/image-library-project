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
| **wondering why a rule exists** | `decisions/log.md`, append-only, 79 ADRs, every one cites its evidence |

## What an app actually consumes

**`dist/app-bundle/` — generated, never hand-edited.** 34 files, each with a sha256 in
`MANIFEST.json`. An app vendors a copy and compares `source_commit` plus the per-file hashes
against what it vendored; a mismatch means the vendor copy is stale rather than silently
wrong.

```
python3 scripts/build-app-bundle.py            # regenerate
python3 scripts/build-app-bundle.py --check    # fail if stale (CI)
```

The bundle is grouped by the call that reads it — `route`, `fill`, `contract`, `gif` — and
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

## Before you write the converter

**The QUERY input contract is strict and a real page export does not satisfy it.** Measured
2026-09-10 against a live Shopify/flunnel export:

- `page.sections` came back empty — the slots live in `htmlCompiled`
- **all eight required `product.attributes` were absent** and must be derived, and
  `mapping/slot-rules.md` runs nine attribute gates on exactly those eight
- `lpTypeId` is carried by the export and has no home in `mapping/content.schema.json`

So there is an export → `content.json` step between a real page and this library, and **this
repo does not yet specify it.** That is the largest piece of work facing a new consumer and
it is named here rather than discovered.

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

- **the export → `content.json` step does not exist** (above) — the blocking one
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

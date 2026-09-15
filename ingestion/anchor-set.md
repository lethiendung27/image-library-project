# Anchor set — classification calibration

Built 2026-08-11 from batches A–C (SPEC §6.1, `ingestion/runbooks/calibrate.md`).
Ten anchors covering six clean matches across five types, one variant-candidate, two
new-candidates, and one reject. Anchors are never removed, only superseded: append a
new row and mark the old one `superseded`.

**Duplicate coverage — this gap has half-closed.** When the set was built, 97
observations had produced zero `duplicate` verdicts: the to-do diff removes exact-hash
repeats before classification ever sees them, so the verdict fires only on a
near-duplicate a classifier notices by eye. The ledger has since produced `duplicate`
verdicts — count them from `ingestion/observations.jsonl`, not from this sentence, which
once carried a number and went stale — but **no anchor row has been added for one**. The
path is exercised and still uncalibrated; add the anchor at the next calibration pass.

**How to use this table.** Classify each image fresh with the current template WITHOUT
reading the expected columns or the image's own ledger record first, then score. The
expected values below are the frozen ledger verdicts, not a fresh opinion.

| # | hash | local path hint | expected verdict | expected type | expected axes | status |
|---|---|---|---|---|---|---|
| A1 | `sha256:141bf8af1c7c8…` | `w1000.avif` | match | 01-pain-scene | gaze=confront | active |
| A2 | `sha256:4b5053f8af57a…` | `w1000 (4).avif` | match | 01-pain-scene | gaze=confront | active |
| A3 | `sha256:6a075900a4297…` | `w1000 (3).avif` | match | 06-relief-hero | register=ugc, inset_mode=context | active |
| A4 | `sha256:56659f0048728…` | `w500 (1).avif` | match | 06-relief-hero | register=commercial, inset_mode=vsinset | active |
| A5 | `sha256:b63e19b7eb9ab…` | `w1000 (9).avif` | match | 06-relief-hero | register=commercial, inset_mode=none | **superseded 2026-08-12** |
| A6 | `sha256:62797f53c0081…` | `w1000 (15).avif` | variant-candidate | 03-use-sequence | — | active |
| A7 | `sha256:d4165b5fb3b40…` | `w500.avif` | variant-candidate | 03-spec-split (--products) | — | **superseded 2026-08-12** |
| A8 | `sha256:a2ad520c55024…` | `w1000 (1).avif` | new-candidate | nearest 03-mechanism-ghostbody → 03-mechanism-xray | — | **superseded 2026-08-11** |
| A9 | `sha256:af4d061a14c17…` | `w1000 (7).avif` | new-candidate | nearest 02-cause-anatomy → 02-cause-aura | — | active |
| A10 | `sha256:e37c7a634bf2e…` | `hero-banner-desktop.jpg` | reject | — | — | active |

## Superseded rows

**A8** — `sha256:a2ad520c55024…` was the founding exemplar of the `03-mechanism-xray`
candidate. That type was **promoted to active v1.0 on 2026-08-11**, so its correct
verdict today is `match` on `03-mechanism-xray`, not `new-candidate`. The row is kept
for the record and replaced by:

| # | hash | local path hint | expected verdict | expected type | expected axes | status |
|---|---|---|---|---|---|---|
| A8b | `sha256:a2ad520c55024…` | `w1000 (1).avif` | match | 03-mechanism-xray | — | active |

This is exactly the case calibrate.md §5 describes: a legitimate taxonomy change moved
an anchor's expected verdict, so the row is updated alongside it. It also makes A8b the
most informative anchor in the set — if a future run still answers `new-candidate`
there, the classifier is reading a stale index rather than drifting.

**A5** — the expected `inset_mode=none` was never right. The founding record (batch
2026-08-10-D) called the magnified-display panel a finding that "no existing inset_mode
covers", but `detail` has been in `vocabulary.yaml` since the scaffold commit
(`145f9f9`) and describes exactly that: magnify the product's own feature. The frozen
value froze a classification error rather than a superseded taxonomy. The 2026-08-12
run answered `detail` and was right, which is calibration catching a ledger mistake in
the direction nobody designs for. Replaced by:

| # | hash | local path hint | expected verdict | expected type | expected axes | status |
|---|---|---|---|---|---|---|
| A5b | `sha256:b63e19b7eb9ab…` | `w1000 (9).avif` | match | 06-relief-hero | register=commercial, inset_mode=detail | active |

**A7** — `variant-candidate` was correct when the row was built: the record PROPOSED the
whole-product comparison that became `03-spec-split --products`. That variant is now
declared in the type's frontmatter, so the image matches an existing variant and today's
correct verdict is `match`. Same mechanism as A8, one rung lower — a variant's creation
moves an anchor exactly as a promotion does. Replaced by:

| # | hash | local path hint | expected verdict | expected type | expected axes | status |
|---|---|---|---|---|---|---|
| A7b | `sha256:d4165b5fb3b40…` | `w500.avif` | match | 03-spec-split (--products) | — | active |

**Note on A6, deliberately NOT superseded.** The 2026-08-12 run answered
`new-candidate → 03-use-rail` where the row expects `variant-candidate` on
`03-use-sequence`, and `03-use-rail` does now exist in `_staging/`. It is still a miss,
not a stale row: that candidate's PURPOSE is a band that EXHIBITS breadth — outputs,
places, movements, zones — while this image's band is a four-step operation loop with
directional arrows enforcing order. Ordered steps are the `sequence` device's content in
rail geometry, which is the deviation the founding record already named. The row stands.

## Scoring

Agreement = (verdict matches + type matches + axis-value matches) / total checks.
≥80% → note the score in `decisions/log.md`, done. <80% → diagnose which ladder level
flipped, fix `ingestion/prompts/classify.md`, bump `template_version`, log an ADR.

## Run history

| date | template | agreement | note |
|---|---|---|---|
| — | c1.0 | not yet run | Set built 2026-08-11; the first scored run is due before the batch after 2026-08-11-F. Building the table from the ledger and re-classifying in the same session would score a classifier that has just read the answers, so the first honest run is a later session. |
| 2026-08-12 | c1.0 | **82%** (23/28: verdict 8/10, type 9/10, axis-values 6/8) | First scored run — ADR-009. Above the 80% bar, so no template change and no `template_version` bump. Run in an isolated classifier context (index + vocabulary + template + the images, nothing else) because the maintainer session had already read this file; scoring happened outside that context. Two genuine misses, A6 and A7, share one shape: device and job read off surface geometry instead of argument structure. Two rows superseded as stale (A5, A7). Against the corrected expectations the same run scores 25/28 = 89%. |

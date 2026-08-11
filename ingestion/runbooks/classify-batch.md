# Runbook — classify a batch of images

Runbook-only ingestion (ADR-000 G2). One session ≈ one batch of **15–25 images**
(full-breakdown records; adjust from measured context use — first batches should
report actual throughput in `decisions/log.md`).

## Interactive mode — one image at a time, approval-first

When the user feeds images individually and wants to review each result, run this
instead of the batch flow (steps 1–2 below still define hashing and classification):

1. Hash the image; skip if the hash is already ledgered.
2. Classify per `ingestion/prompts/classify.md` and SHOW the full record to the user
   — verdict, matched type, axes, deviations, breakdown. **Do not append yet.**
3. Wait for the user: `ok` → append to `observations.jsonl` and run
   `python3 scripts/validate.py --write-index`. A correction ("this is X") → fix the
   record (note the correction in `notes`), then append.
4. On request, continue the chain for the same image: show the matched type's
   SKELETON / fill a prompt for a named product (query runbook Step 5 + adapter) /
   log a render-test result (`eval/render-test.md`).

Approval points, in both modes: observation records are evidence and normally
append-by-agent (interactive mode adds the optional pre-append check); every change
under `registry/` is ALWAYS a git diff the user reviews and commits; render-test
verdicts are always the user's call.

## 0. Preconditions

- Source images live OUTSIDE the repo (SPEC §6.4). Canonical local folder:
  `/Users/lethiendung/Downloads/image-library-assets/` (ADR-006).
- `registry/index.yaml` is fresh (`python3 scripts/validate.py --check`).

## 1. Build the to-do list (ledger = checkpoint)

```sh
# manifest of all source image hashes (recursive, common formats)
find /Users/lethiendung/Downloads/image-library-assets -type f \
  \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.webp' -o -iname '*.avif' \) \
  -exec shasum -a 256 {} + | awk '{print "sha256:" $1 "  " $2}' > /tmp/manifest.txt
# hashes already ledgered
grep -o '"hash": *"sha256:[0-9a-f]*"' ingestion/observations.jsonl | grep -o 'sha256:[0-9a-f]*' | sort -u > /tmp/done.txt
# to-do = manifest − done
```

Pick the next 15–25 undone images as this batch. Batch id: `YYYY-MM-DD-<letter>`.

## 2. Classify

Load `registry/index.yaml` + `registry/vocabulary.yaml` +
`ingestion/prompts/classify.md`. For each image in the batch: read the image, walk
the absorption ladder, append ONE record line to `ingestion/observations.jsonl`
exactly per the template's record format. Exact-duplicate hashes are skipped by the
to-do diff; near-duplicates you notice get verdict `duplicate` pointing at the
earlier hash in `deviations`.

## 3. Close the batch

- [ ] Every batch image has exactly one record (`wc -l` delta equals batch size).
- [ ] `python3 scripts/validate.py` passes (ledger lines parse, verdicts legal).
- [ ] Note the batch id + count + anything odd in the session summary for the user.
- [ ] Do NOT touch `registry/` from this runbook — patches and candidates are
      curation's job (`curate.md`), with the evidence rule.
- [ ] Commit the batch as ONE commit (ledger append + regenerated index) once the
      validator is clean; report hash + revert path (ADR-007).
- [ ] Every ~5 batches: run `calibrate.md` before the next batch.

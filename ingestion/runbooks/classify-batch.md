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

```python
# manifest + to-do in one pass. Build it in PYTHON, not shell — see the warning below.
import hashlib, io, json, os
ROOT = "/Users/lethiendung/Downloads/image-library-assets/stills"
EXT = {".png", ".jpg", ".jpeg", ".webp", ".avif"}
rows = []
for dp, _, fns in os.walk(ROOT):
    for fn in fns:
        if os.path.splitext(fn)[1].lower() in EXT:
            p = os.path.join(dp, fn)
            rows.append((f"sha256:{hashlib.sha256(io.open(p,'rb').read()).hexdigest()}", p))
done = {json.loads(l)["hash"] for l in io.open("ingestion/observations.jsonl", encoding="utf-8") if l.strip()}
todo = [(h, p) for h, p in rows if h not in done]
```

**The shell one-liner this replaced was BROKEN and silently so (2026-08-31).** It piped
`find … -exec shasum` through `awk '{print "sha256:" $1 "  " $2}'`, and `$2` is the first
whitespace-delimited token of the path — so every file under a folder whose NAME contains a
space came back truncated at that space. Measured: a folder named `LP3 assets learn` holding
653 files produced a to-do list saying **0 outstanding**, because all 653 paths collapsed to
`…/stills/LP3`. Rebuilt in Python the same corpus gave 701 files, 666 unique hashes, 588
outstanding. A to-do list that comes back suspiciously empty is the symptom; check for spaces
in directory names before believing it.

Pick the next 15–25 undone images as this batch. Batch id: `YYYY-MM-DD-<letter>`.

**Format note (2026-08-12).** The manifest above includes `.avif`, and much of the corpus
is AVIF — but the harness image reader used in this session could not render it and
returned the file as binary. Decode before classifying, keeping the hash of the ORIGINAL
file as the record's identity (the PNG is a working copy, never a source):

```sh
sips -s format png "<source>.avif" --out "<scratch>/<name>.png"
```

Never classify an image you could not actually see; a filename is not evidence. Formats
outside the manifest list are outside the to-do by definition — `.gif` in particular is
not a manifest format, so motion assets are not batch input.

**A filename is not evidence for SCOPING either, and this cost two batches.** Selecting a
batch by filename pattern — excluding `icon|logo|badge|avatar`, or preferring `benefit-*` —
let an avatar through twice: `…__gallery-14-vet-quote-dr.jpg` and
`…__benefit-6-banner-review.png` are both quote-attribution portraits and neither name says
so. Filename patterns are fine for ORDERING a to-do list and useless for deciding what an
asset is. Budget for a few rejects per batch rather than trusting the filter.

**Selecting rather than taking the next N is legitimate and must be stated.** A market corpus
folder is often two-thirds page furniture, and twenty sequential files can be twenty rejects
that teach nothing. Batches 2026-08-31-A and -B both selected argument-carrying assets
round-robin across products, and both said so in their commit message. What is not legitimate
is selecting silently: the reader of the ledger has to know the sample was shaped.

**The manifest points at `stills/`, and that is load-bearing (2026-08-19, ADR-025).** The
asset folder now holds `stills/` (the market corpus), `feedback/` (this library's own
render outputs) and `gifs/` (the GIF library) side by side. Until today the manifest was
rooted one level up and recursive, so it swept `feedback/` too: measured on 2026-08-19,
that produced a to-do list of **324 items, every one of them a render this library
produced**, while the real corpus was already fully classified — 108 unique hashes at the
root, all 108 ledgered, 0 outstanding. A session following the runbook literally would
have spent a batch teaching the library its own output back to itself, and §6.2's evidence
rule would have counted those as independent observations. Keep the manifest pointed at
`stills/`. If the to-do list comes back empty, the corpus is genuinely exhausted and the
answer is new source images, not a wider `find`.

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

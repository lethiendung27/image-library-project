# Runbook — calibrate classification drift

Sessions vary; the template must not. Every ~5 batches (or after any template edit),
re-classify the anchor set and compare against its frozen expected verdicts.

## Anchor set

`ingestion/anchor-set.md` lists ~10 images (by sha256 + local path hint) with
expected `verdict`/`type`/`axes`. Build it from the first two batches: pick clean
matches, one variant-candidate, one new-candidate, one duplicate, one reject.
Anchors are never removed, only superseded (append a new row, mark the old one).

## Procedure

1. Classify each anchor image fresh with the CURRENT template — do not look at the
   expected values or prior records first. Do not append these runs to the ledger.
2. Score agreement: verdict match, type match, axis-values match.
3. **Agreement ≥ ~80%**: note the score in `decisions/log.md`; done.
4. **Agreement < ~80%**: the template is drifting or under-specified.
   - Diagnose from the misses: which ladder level flipped? Which wording invited it?
   - Fix `ingestion/prompts/classify.md`, bump `template_version` (c1.0 → c1.1) in
     the same diff, and log an ADR entry with the miss analysis.
   - Never "fix" a session by ad-hoc extra instructions — if it needed saying, it
     belongs in the template.
5. If a legitimate taxonomy change (new type promoted, trigger rewritten) changes an
   anchor's expected verdict, update the anchor row in the SAME PR as that change.

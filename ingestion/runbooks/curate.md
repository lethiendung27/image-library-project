# Runbook — curate the ledger into patches and candidates

Run after every ~200 new observations (or when the user asks). This is the ONLY path
by which ingestion changes `registry/` — always as a reviewable diff for the human
gate, never committed by the agent.

## 1. Aggregate

From `ingestion/observations.jsonl` (discounting records whose `template_version` is
older than the current template — weigh them lower, note when they dominate a count):

- per type: distinct-hash evidence count, axis-value distribution;
- per type × slot: recurring `deviations` with counts;
- `variant-candidate` clusters (same ONE decision observed repeatedly);
- `new-candidate` clusters (similar proposed ids / breakdowns).

## 2. Patch existing types (the evidence rule, SPEC §6.2)

For each recurring deviation with **≥2/3 recurrence among that type's relevant runs,
or ≥3 distinct observations**:

1. Decide the layer: slot ambiguity → split the slot; model weakness (hands, text,
   faces) → NEGATIVE, not longer prose; structural → skeleton (major bump).
2. Edit the type file; bump MINOR (or MAJOR for layer changes); add a CHANGELOG entry
   citing the observation hashes.
3. Below threshold → add to the type's KNOWN-FLAKY with hashes; do not touch the
   skeleton.

## 3. Variant and type candidates

- Variant cluster with ≥3 distinct observations → draft the `### --slug` diff block in
  the parent type; bump MINOR; cite hashes.
- New-type cluster → draft a full type file with `status: reserved`. **Which folder is
  decided by the CORPUS the cluster was measured on**, not by the argument: a cluster from
  the LP2 product-gallery batches goes to `registry/pdp-dr-types/` and owes a `blocked_by`
  and a `BLOCK` section (SPEC §3.8, ADR-077); everything else goes to
  `registry/types/_staging/`. A draft never sits in both, and the validator errors on an id
  that does — the one legal shared id is a declared verbatim copy (ADR-091). New job/device values ship in `vocabulary.yaml` in the same diff, and a
  `pdp-dr` draft ships in `vocabulary.pdp_dr_types` too. Check promotion readiness against
  SPEC §6.3 (≥5 exemplars, router-confusion test, rendered worked example) — promotion
  itself is a separate, later diff, and in `pdp-dr-types` it is a status change in place:
  that folder is the one an LP2 page routes (ADR-091), so a promoted LP2 type stays in it.

## 4. Router-confusion test (for any trigger you added or edited)

Regenerate the index in a scratch copy, then route 5 briefs that today's index routes
correctly (use `eval/golden/` fixtures). Any flip that is not an intended improvement
→ rewrite the trigger before proposing the diff.

## 5. Close

- [ ] `python3 scripts/validate.py --write-index` clean (index regenerated with the
      proposed registry changes).
- [ ] Every CHANGELOG entry cites observation hashes (or `seed: conversation.md` for
      grandfathered content — ADR-001).
- [ ] Commit the curation as ONE commit once the validator is clean — per-change
      evidence counts in the message — then report the commit hash, the evidence
      counts, and the revert path (`git revert <sha>`). ADR-007: the owner's standing
      inputs are the gate; no pre-commit review round.

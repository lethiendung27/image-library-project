# Staging — candidate types

Files here are **not routable**: the router never reads this folder, the validator
excludes it from `index.yaml`, and nothing here may be referenced by
`pairs_with`/`never_with` of active types.

A candidate is promoted to `registry/types/` only when ALL of SPEC §6.3 holds:

1. ≥5 distinct exemplars in `ingestion/observations.jsonl` (distinct sources, no near-dups);
2. passes the router-confusion test against the current index;
3. has ≥1 worked example actually rendered (`run: pass` or `partial`);
4. the promotion diff is reviewed and committed by the human gate.

Candidates use the same anatomy as active types, with `status: reserved` until
promoted. Naming follows the same `{NN}-{job}-{device}` grammar; if the job or device
is new, the `vocabulary.yaml` addition ships in the same PR.

## `ready-to-push/` — moved out on 2026-09-10

That subdirectory held the test materials for candidates blocked on criterion 3 alone. All
three types it served were measured on the LP2 product-gallery corpus, so it moved with them
to `registry/pdp-dr-types/ready-to-push/` (ADR-077) and its README carries the convention.

**The convention is not folder-specific and a future `_staging/ready-to-push/` follows it**: a
README naming what each type is still missing, a `prompts.md` of paste-and-run prompts, and
**no copies of the type files** — those live beside this README and are the law. A
subdirectory rather than a file, so it can be emptied and refilled. The directory enumerator
filters on `.md`, so a subdirectory is invisible to it and the staging count does not move.

Products in those prompts are drawn from `query/product-slugs.yaml` and are deliberately ones
that appear in NO candidate's source list. A rule that holds on a product it has never seen is
a rule.

## Which folder a new draft goes to

The CORPUS a cluster was measured on decides it, not the argument. A cluster from the LP2
product-gallery batches goes to `registry/pdp-dr-types/` and owes a `blocked_by` and a
`BLOCK`; everything else comes here. **Two of the nine files that used to be here stayed** —
`02-cause-scene` and `03-use-rail`, the two that appear on no page in that corpus.

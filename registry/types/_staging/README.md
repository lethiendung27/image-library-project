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

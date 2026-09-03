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

## `ready-to-push/`

A subdirectory holding the test materials for whichever candidates are blocked on criterion 3
alone — a rendered worked example with the owner's verdict. It carries a README naming what
each type is still missing and a `prompts.md` of paste-and-run prompts, and **no copies of the
type files**: those live in this directory and are the law.

It is a subdirectory rather than a file so it can be emptied and refilled as the set of
blocked-on-a-render candidates changes. Both scripts that read `_staging/` enumerate it with
`os.listdir` and filter on `.md`, so a subdirectory is invisible to them; the staging count
does not move when this folder does.

Products in those prompts are drawn from `query/product-slugs.yaml` and are deliberately ones
that appear in NO candidate's source list. A rule that holds on a product it has never seen is
a rule.

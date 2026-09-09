# Classify template — toplist lede images · `t1.0`

The sibling of `classify.md` for the third namespace (SPEC §3.7). Same ledger, same
append-only rules, same verdicts. What changes is the candidate set and one question.

**Context loaded:** `registry/toplist-instruction.md` + `registry/toplist-types/*.md` +
`registry/vocabulary.yaml`. Not `index.yaml` — the toplist namespace is never written into
it, so the shortlist a classifier uses for image types does not exist here.

## The candidate set

The seven ids of `vocabulary.toplist_types`, and nothing else. A frame that argues
something the seven do not is `new-candidate` with a `proposed_id`, never forced into the
nearest one.

## The one question that decides most frames

**What does this frame claim, and how would the reader check it?**

| the claim | the type |
|---|---|
| here is the problem you have | `lede-pain` |
| here is the thing working, in a life | `lede-inuse` |
| we had all of them in one room | `lede-lineup` |
| we measured it | `lede-testing` |
| this one won | `lede-winner` |
| here are the five, as an index | `lede-collage` |
| a person you should believe judged it | `lede-authority` |

Two boundaries carry most of the disagreements and both are checkable rather than felt:

- **`lede-lineup` against `lede-collage`** — photographed together under one light with
  real contact shadows, or assembled from cut-outs with no shared light. Possession
  against enumeration.
- **`lede-inuse` against `lede-testing`** — an instrument in frame, or none. Where neither
  an instrument nor a bench is present and only the ROOM suggests a lab, say so in
  `deviations`: the boundary is not carried by the place alone and that is a finding about
  the type file, not about the image.

## Record

Exactly the format `classify.md` prescribes, with `template_version: "t1.0"` and `type`
holding a toplist id. `scripts/validate.py` counts these per type and warns where an
ACTIVE type sits under SPEC §6.2's three observations.

## What this template does NOT ask

**Do not record ratio.** The consuming app resolves the lede ratio (2026-09-09) and no
toplist type declares one, so a ratio measured off a reference frame is provenance about
the publisher rather than evidence about the type.

**Do not treat baked text as disqualifying.** This namespace bakes none, and the market
bakes plenty. A frame carrying a headline is still an observation of its argument; note
the text in `deviations` and classify the picture underneath it.

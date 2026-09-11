# PDP-DR rules — routing a direct-response product gallery

Law for the namespace is `registry/pdp-dr-instruction.md`; the contract is `SPEC.md` §3.8.
This file is the routing half: which types a product-gallery slot prefers, what refuses,
and what nothing checks.

**A PDP page routes to TWO folders in one pass.** `registry/types/` supplies everything
that routes today; `registry/pdp-dr-types/` supplies nothing yet, because every file in it
is `status: reserved`. That is the honest state of the namespace on 2026-09-10 and this
table is written so it stays visible rather than being inferred from an empty result.

## Layer 1 — mechanical admission

| condition | effect |
|---|---|
| type is in `registry/pdp-dr-types/` | **not routable, all eleven.** Every file carries `status: reserved`, a `blocked_by` and a `BLOCK`. None enters `registry/index.yaml` |
| `requires_product_photo: true` and no reference photo for the product | refuse, and say so in the session notes rather than shipping a prompt the owner cannot run |
| the gallery is syndicated to a marketplace | drop the ugc register, drop `01-pain-scene`, forbid `04-proof-lockedframe --rivals` (`mapping/slot-rules.md` cross-rule 5) |
| slot is gallery image 1 | out of library scope — a standard product shot (cross-rule 6) |

Every attribute gate in `mapping/slot-rules.md` applies unchanged. They are keyed on ACTIVE
type ids and every type they name is active, so unlike the toplist namespace **nothing has
to be restated here** — ADR-070's finding was about gates keyed on a parent whose COPY had a
different id, and this namespace holds no copies.

## Layer 2 — preference order, MEASURED

Unlike `mapping/toplist-rules.md`, which declares itself a hypothesis in its own first
paragraph, this table is counted from the ledger: **159 observations across 26 source pages**,
batches `2026-08-31-A`/`-B` and `2026-09-03-C` through `-H`. The number beside each type is
its **distinct source count on this corpus**, not its observation count — the two diverge
badly and SPEC §6.3 counts sources for that reason.

| role | preferred, best first (distinct PDP sources) |
|---|---|
| hero | `06-relief-hero` (16) |
| problem-agitation | `02-symptom-rail` (2) |
| cause | `02-cause-anatomy` (3) |
| mechanism | `03-spec-macro` (13), `03-mechanism-ghostbody` (2), `03-mechanism-xray` (1) |
| proof | `04-proof-lockedframe` (5) |
| social-proof | `05-social-snapshot` (7), `05-social-handoff` (1) |
| personas | `05-persona-grid` (1) |
| how-to-use | `03-use-sequence` (4), `03-use-grid` (2) |
| comparison | `04-proof-lockedframe--verdict`, `03-spec-split` — **neither observed here**; the row falls back to `mapping/slot-rules.md` |
| outcome | `06-relief-hero` (16), `06-relief-scene` (4) |
| cta, author | — (out of library scope) |

This is a PREFERENCE ORDER and not the candidate pool (ADR-058). The pool is every active
type for every slot; a type outside a row is a candidate, not a violation.

### The finding this table exists to record: step 1 is EMPTY

**Four active types appear on no page in this corpus**, and two of them are the whole of the
Trust Ladder's first rung:

| absent from all 26 PDP sources | present in the advertorial/listicle corpus |
|---|---|
| `01-pain-scene` | yes |
| `01-pain-split` | yes |
| `03-spec-explode` | yes |
| `03-spec-split` | yes |

And the reverse, once: **`06-relief-scene` appears here and nowhere in the older corpus.**

`mapping/slot-rules.md` prefers `01-pain-scene` for both `hero` and `problem-agitation`. On a
product gallery that preference points at a type the format does not use — a buyer on a
product page has already been sold the problem by the ad that brought them, and the gallery
opens on the object or on the outcome. That is why the `hero` row above names one type and it
is a relief type.

**What this does NOT prove.** The owner selects what enters a batch and the harness classifies
it; 26 pages is what was filed, not a random sample of the format, so this is *absent from what
was filed* rather than *absent from the format*. `03-spec-explode` in particular is a
plausible gallery tile that simply did not turn up. The rows stay as measured and the limit
stays written next to them — the alternative is a rule that feels obvious, which is the exact
shape ADR-068 caught moving a whole render set off the market.

## Cross-file call register — the thing nothing checks

The toplist namespace ships verbatim copies and pays for them with `copied_at_version` and a
validator warning (ADR-070). This namespace ships no copies, so it has no such instrument —
and it has a smaller exposure of the same kind. **A skeleton that calls a part defined in
another file is a reference nothing validates.** Every one of them lives here:

| the caller | calls | defined in | status |
|---|---|---|---|
| ~~`07-identity-callout` `[PRESENTATION]`~~ | `PARTS/presentation` | `03-spec-callout` | **dead — caller deprecated 2026-09-11** |
| ~~`07-identity-callout` `[SETTING]`~~ | `PARTS/setting` | `03-spec-callout` | **dead — caller deprecated 2026-09-11** |

**Zero live calls today.** Both rows are struck rather than deleted: the caller was retired
by ADR-078 in favour of the type it was calling into, which is the cleanest way a
cross-file call can end, and a reader following the deprecation needs to see that the calls
went with it.

**Adding a call without adding a row here is the failure this register exists to prevent**,
and the register is the whole instrument — the validator does not read skeleton prose. The
three files written on 2026-09-11 (`03-spec-claimstack`, `03-spec-dimension`,
`03-spec-hero`) deliberately restate their own parts rather than calling a sibling's, so the
register stays empty.

`06-relief-animal` cites `06-relief-scene`'s `PARTS/subject` and `pairs_with` in prose rather
than calling it from a skeleton; that is an argument, not a reference, and it is deliberately
not in the table above.

## Cross-slot rules — where a gallery differs from an advertorial

All of `mapping/slot-rules.md`'s portfolio constraints apply. Three do more work here:

1. **One type at most once per page.** A twelve-tile gallery is **not** a repeating section in
   cross-rule 2's sense. A roundup's ranked entries are equivalent list items; a gallery's
   tiles are a linear argument, and repeating a type across a linear funnel repeats an
   argument. The exception stays available to a review wall inside the page, which is a
   genuine repeating section.
2. **Page arc, G4 at page level.** Cause tiles precede relief and outcome tiles; a problem
   tile never reappears after the first relief tile. With twelve slots there is room to break
   this without noticing.
3. **Step-3 budget.** At most two of `03-mechanism-ghostbody`, `03-spec-split`,
   `03-use-sequence`. `03-spec-macro` is the corpus's commonest mechanism tile at 13 sources
   and is **not** in that trio, so a gallery can carry it alongside two of the three — which
   is what the corpus does.

## What happens when the reserved files unblock

Nothing here changes shape. A file promoted out of `registry/pdp-dr-types/` moves to
`registry/types/` by `git mv` with a status change, enters `registry/index.yaml` through
`scripts/validate.py --write-index`, and appears in `mapping/slot-rules.md`'s preference table
under its role — at which point its row here becomes a duplicate and is deleted rather than
maintained. **This file shrinks as the namespace succeeds.** That is the intended direction and
it is the difference between a co-registry and a fork.

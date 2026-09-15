# PDP-DR rules — routing a direct-response product gallery

Law for the namespace is `registry/pdp-dr-instruction.md`; the contract is `SPEC.md` §3.8.
This file is the routing half: which types a product-gallery slot prefers, what refuses,
and what nothing checks.

**An LP2 page routes ONE folder, `registry/pdp-dr-types/`, and never opens
`registry/types/`** (ADR-091; owner instruction, 2026-09-15: each page kind routes one
folder, and that folder holds every type the page may use). Its routing surface is
`registry/pdp-dr-index.yaml`, generated from the folder's active files. Two kinds of file
live there: a verbatim copy of every active image type, under the parent's id, which is
what routes today; and LP2's own drafts, every one `reserved` or `deprecated`, which route
nowhere until one is promoted in place.

## Layer 1 — mechanical admission

| condition | effect |
|---|---|
| type is not in `registry/pdp-dr-index.yaml` | **not routable.** The index carries the folder's `active` files only; a draft's `reserved` or `deprecated` status keeps it out, and a reserved draft carries a `blocked_by` and a `BLOCK` saying why |
| `requires_product_photo: true` and no reference photo for the product | refuse, and say so in the session notes rather than shipping a prompt the owner cannot run |
| the gallery is syndicated to a marketplace | drop the ugc register, drop `01-pain-scene`, forbid `04-proof-lockedframe --rivals` (`mapping/slot-rules.md` cross-rule 5) |
| slot is gallery image 1 | out of library scope — a standard product shot (cross-rule 6) |

Every attribute gate in `mapping/slot-rules.md` applies unchanged. They are keyed on ACTIVE
type ids, and this folder's copies keep their parent's id, so unlike the toplist namespace
**nothing has to be restated here** — ADR-070's finding was about gates keyed on a parent
whose COPY had a different id. A draft promoted here brings no gate with it; if one should
apply, the promotion diff writes it, as it would for a new image type.

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
type in `registry/pdp-dr-index.yaml`, for every slot; a type outside a row is a candidate, not
a violation.

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

Since ADR-091 this namespace ships verbatim copies too, and pays for them the way the
toplist namespace does: `copied_at_version` and a validator warning when the parent moves
(ADR-070). That instrument watches whole files. It does not reach a smaller exposure of the
same kind: **a skeleton that calls a part defined in another file is a reference nothing
validates.** Every one of them lives here:

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

A draft is promoted **in place**: its `status` becomes `active` and its `blocked_by` null,
and `scripts/validate.py --write-index` writes it into `registry/pdp-dr-index.yaml`. It does
NOT move to `registry/types/` — that would take it out of the one folder an LP2 page routes
(ADR-091) — and it gains a row in the Layer 2 table above under its role. **This file grows
as the namespace succeeds.** ADR-077 wrote the opposite, that promotion was a `git mv` and
this file would shrink; that was the co-registry, and ADR-091 retired it.

Whether LP1 should route a promoted LP2 type as well is a separate decision. No instrument
watches a copy in that direction yet; the first diff that makes one builds it.

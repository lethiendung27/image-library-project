# Slot rules — role → preferred types

Stage 1 of routing (SPEC §7): a mechanical lookup producing the per-slot shortlist.
Stage 2 (the portfolio pass in `query/runbook.md`) then applies the attribute gates to the
pool and the cross-slot rules below to the recommended set (ADR-090). No type declares a
ratio any more (ADR-082; ADR-086 missed this sentence). This table proposes; it never
decides.

**This is a PREFERENCE ORDER, not the candidate pool** (ADR-058). The pool is every
active type — all 17, for every slot. Types named in a row outrank types outside it at
equal fit; a type outside the row is a candidate, not a violation. An empty row means no
type is PREFERRED for that beat, never that the slot goes unrouted — only `cta` and
`author` carry no image by definition.

**The four channel columns collapsed into one on 2026-08-26** (ADR-059). Channel stopped
being an admission test, so the columns were the same preference written four times, and
48 cells became 12 rows. A type preferred for `mechanism` is preferred for `mechanism`
wherever that beat appears. The reason channel stopped gating: this library serves image
types to ANY page kind — a customer may take an advertorial template and write listicle
copy into it — so the page's kind is not knowable from its template, and the router only
ever learned the channel by guessing it from `lpTypeId`. What the copy argues decides.

## Preference table

| Role | preferred types, best first |
|---|---|
| hero | `06-relief-hero`, `01-pain-scene` |
| problem-agitation | `01-pain-scene`, `01-pain-split`, `02-symptom-rail` |
| cause | `02-cause-anatomy` |
| mechanism | `03-mechanism-ghostbody`, `03-mechanism-xray`, `03-spec-explode`, `03-spec-macro`, `03-spec-split` |
| proof | `04-proof-lockedframe` |
| social-proof | `05-social-handoff`, `05-social-snapshot`, `05-persona-grid` |
| personas | `05-persona-grid` |
| how-to-use | `03-use-sequence`, `03-use-grid` |
| comparison | `04-proof-lockedframe--verdict`, `03-spec-split`, `01-pain-split` |
| outcome | `06-relief-hero`, `06-relief-scene`* |
| cta | — (standard product shot, out of library scope) |
| author | — (a portrait of a named person, out of library scope) |

Every one of the 17 active types appears in exactly one row or more, and
`scripts/validate.py` fails if one does not — this table is now the ONLY place a type
declares which beat it belongs to, so a type missing from it is a type no slot will ever
prefer. That gate did not exist before ADR-059; `03-spec-macro` and `03-use-grid` went
active on 2026-08-26 with no entry at all and nothing noticed.

`*` `06-relief-scene` only when its `requires_pair` (`01-pain-scene`, same person) is
also on the page.

**Where the two 2026-08-11 channel trims went.** Two cells were TRIMMED rather than
widened that day because the type argued against itself being there, and both survive as
what they always were — statements about the CASE, not walls around a surface:

- `02-symptom-rail` was cut off advertorial because the infographic-tile aesthetic
  "signals cheap goods off-marketplace". It moved into that type's own `avoid_when` on
  2026-08-26 and lasted one day: **ADR-060 removed `avoid_when` from every type**, so
  the rule now has to live in `use_when` or not at all. It is not a refusal any more —
  a rail on an editorial page is out-ranked by FIT rather than barred.
- `06-relief-scene` was cut off landing-page because its `use_when` names only "an
  advertorial or final frame of an ads creative". **That one survives untouched**:
  `use_when` is criterion 1 of the ranking, so the beat scores low on FIT by the type's
  own words. It was always the right place for it.

`author` was added on 2026-08-18 with every cell empty, which is the point of adding it.
Bylined advertorials carry portrait slots — a byline avatar, an About-the-author image,
a comment thread of faces — and two routed pages carried nine of them between them. No
library type produces a portrait of a named person, and generating a face to sit under a
real byline is a disclosure decision rather than an image one. Before this row a session
had to re-derive that every time, and `content.json` had no legal role to declare those
slots under at all, so they were either mislabelled `cta` or left out of the contract
entirely. An empty row records the decision once; a missing row makes it a judgement call
forever.

## Attribute gates (deterministic kill-rules, applied in Stage 2)

| Attribute condition | Effect |
|---|---|
| `symptom_visibility: invisible` | drop `01-pain-split`; `02-symptom-rail` only if downstream symptoms are photographable (then vignette mode `visible-symptom`) |
| `visible_output` ≠ `none` | G8 binds: hero options must use the backlight branch; the output is the primary subject |
| static frame cannot show the product difference | `04-proof-lockedframe`: forbid `--rivals`/`--verdict`, require `--timelapse`/`--capture` (VARIANT SELECTION RULE — verified) |
| `mounting: fixed-installed` | G7-X: installed mode in every layer; ugc register needs the low-angle reframe (product + output as subject). The field is a free string since ADR-121, so this row fires on that token and a writer reads any other wording |
| `operation: active` / `passive` | POSE branch: mid-action vs relaxed |
| `body_contact: false` | drop `03-mechanism-ghostbody`; mechanism slots fall to `03-mechanism-xray` (its `avoid_when` went at ADR-060, so trivial interiors and anti-tech-render categories are a FIT judgement now, not a refusal) |
| `result_visibility: invisible` | drop `06-relief-scene` (close with `06-relief-hero` instead) |
| `multi_step_usage: false` | drop `03-use-sequence` |
| `colorways` has 1 entry | Zone B of `06-relief-hero` shows 1 unit only (fabricating a second colorway violates G2) |

**Four of these nine rows EXECUTE; five are prose.** `scripts/validate.py`'s
`parse_attribute_gates()` reads this table rather than restating it in code, and it takes a
row only where the condition cell is exactly `` `attribute: value` `` and the effect cell
contains ``drop `type` ``. So the executable set is `symptom_visibility`, `body_contact`,
`result_visibility` and `multi_step_usage` — the four that KILL a type. The other five
change how a chosen type is EXECUTED and no code applies them: a not-equals condition
(`visible_output`), a condition naming no attribute (the static-frame row), a slash in the
value (`operation`), a prose quantity (`colorways` has 1 entry), and an effect with no
`drop` in it (`mounting`). **A constraint that is not applied does not refuse a prompt — it
returns one that renders and argues the wrong thing**, which is the harder failure to see.

**`multi_step_usage` lost an "unless" on 2026-09-11 and the deletion is the fix, not a
trim.** The row read *"drop `03-use-sequence` unless buyers plausibly assume complexity"*
while the code dropped it unconditionally, so the executable rule was STRICTER than the
written one at the gate that fires most — 7 of the 14 `content.json` files in this repo. No
attribute carries "buyers plausibly assume complexity", so the clause could never execute;
leaving it written invited a reader to apply it by hand and diverge from the router. If the
judgement is worth keeping it needs a ninth attribute, which is a schema change and an owner
decision. Until then the table says what the router does. `eval/golden/fixture-003` holds
this gate to the code's behaviour.

## Cross-slot rules (portfolio constraints)

**Rules 1–4 bind an LP1 page only.** An LP2 page (`pdp_dr`) runs rules 5 and 6 from this list
and its own cross-slot rules in `mapping/pdp-dr-rules.md`. There, no rule refuses a type because
of the type another slot holds (owner decision, 2026-09-17, ADR-102).

1. Honor `never_with`, `pairs_with`, `avoid_adjacent`, `requires_pair` from the index.
   Known hard pairs: `01-pain-scene` × `01-pain-split` never share a page;
   `06-relief-scene` requires `01-pain-scene`; `05-social-handoff` not adjacent to
   `05-persona-grid`.
2. One type appears at most once per page (different variants do not lift this) —
   **except inside a repeating section**, where the page's own structure is a list of
   equivalent entries (a roundup, a review wall, a gallery of cells). There the type
   may serve every entry, provided the instances differ on a **named dimension**, the
   same honesty `varies_on` demands of options. Repeating a type across a linear funnel
   repeats an argument; repeating it across list entries IS the format.
   Evidence, two independent collisions: a listicle whose five ranked entries each
   indict one alternative, and `05-social-snapshot`, whose own SLOT CONSTRAINTS
   legislate a SET ("when a page requests more than one snapshot, every image must
   differ COMPLETELY") that the unqualified rule forbade.
3. Page arc (G4 at page level): pain/cause sections precede relief/outcome sections;
   pain never reappears after the first relief image.
4. Step-3 budget: at most two of {`03-mechanism-ghostbody`, `03-spec-split`,
   `03-use-sequence`} on one page — they answer different questions; three is a lecture.
5. Marketplace legality: `--rivals` (no product in frame) and ugc register never on
   marketplace; `01-pain-scene` never in marketplace galleries.
6. The main/first gallery image is out of library scope (standard product shot) — the
   library covers images 2+.

### Which of these bind the SET, and which bind the POOL

**Decided 2026-09-15: the pool is content-first** (owner instruction, ADR-090). Every rule
above except rule 5 constrains the page that is RECOMMENDED. **None of those constrains which
types may be OFFERED for a slot**, and the distinction has already cost this library one
correction. `query/runbook.md` states it for rule 2 in its own words — *"So `one-type-once`
binds the recommended SET, never the option pool"* — and records what the other reading did:
read as a pool rule, every second type on a seven-slot body looked spent and B fell back to
an execution every time. **Measured before that correction: 83 of 101 non-A options varied on
execution, 11 on axis, and 7 on type.**

That sentence exists for rule 2 alone. It is written here for all six, because the same
misreading is available for each:

| rule | binds | so an option may… |
|---|---|---|
| 1 `never_with` | the SET | be offered on a slot even though the page already recommends its partner — the SET may contain only one of them |
| 1 `pairs_with` | the SET, as a PREFERENCE | always be offered; this field never refuses |
| 1 `avoid_adjacent` | the SET's ORDER | always be offered; adjacency is decided when the page is assembled |
| 1 `requires_pair` | the SET | be offered before its precondition is on the page |
| 2 one-type-once | the SET | carry a type recommended elsewhere; name the displaced slot in `composition_notes` |
| 3 page arc | the SET's ORDER | always be offered |
| 4 step-3 budget | the SET | always be offered; the budget is counted over what is chosen |
| 5 marketplace legality | the POOL | **not** be offered where the channel forbids it — one of the three removers, with the attribute gates and the global rules, and the only one about the SURFACE rather than the argument |

**Two things this table left open. The second is now settled.**

**`requires_pair` is `null` on all 17 active types and nothing in this repo reads it.**
Rule 1 above says `06-relief-scene` *requires* `01-pain-scene`; `registry/index.yaml` carries
that dependency as `pairs_with`, which this table calls a preference, and `requires_pair:
null`. So a hard precondition is recorded in a soft field, and the only enforcement anywhere
is whatever a consuming app does at Stage 2. Deciding it means either populating the field —
which changes nothing here until something reads it — or deleting it and rewording rule 1.
Not decided; stated so the next reader does not have to rediscover the disagreement.

**`01-pain-split` has never been offered as an option in any routed session, and the
measurement now points at one explanation.** Fourteen sessions, 171 image slots, and a type
among the library's better performers (18 passes of 29 renders, second-best of the high-n
types) appears in no option pool at all. Its attribute gate explains one page of fourteen.

Measured 2026-09-11: **`01-pain-scene` is offered in 14 of 14 sessions; `01-pain-split` in
0 of 14.** The two are `never_with` each other. On the ONE session routed after ADR-058 —
`advertorial-cord-tensioner-cam-lock-v01`, the only one where a slot is required to carry
three DISTINCT types — the `problem-agitation` slot came back as `04-proof-lockedframe`,
`01-pain-scene`, `06-relief-hero`. **Two of those three are from outside the
`problem-agitation` row, while the row's own second entry, `01-pain-split`, is absent.**
SPEC §7.2 says types named in a row outrank types outside it at equal fit, so a row member
losing to two non-members on its own beat is what EXCLUSION looks like, not what ranking
looks like.

That is consistent with `never_with` being applied to the POOL — the same misreading the top
of this section describes, on a different field, uncorrected — and it is **n=1 for the
post-ADR-058 case**, which is why the rule is recorded here rather than changed. What would
settle it: route one more page whose copy argues a before/after, with `01-pain-scene` already
recommended elsewhere, and see whether `01-pain-split` reaches the option pool for the
problem beat. If it does not, `never_with` is gating the pool and the fix is a scope sentence,
not a weaker rule.

**Settled by decision, 2026-09-15** (owner instruction, ADR-090). The pool is content-first, so
`never_with` binds the SET. `01-pain-split` may be offered on a slot while `01-pain-scene` is
recommended elsewhere on the page: the recommendation holds one of them, and the options may
hold both. That is the scope sentence above, written as law.

The measurement stays as the record of what the pool reading cost. The routing it proposed is no
longer needed to decide the rule, only to confirm that routers now follow it.

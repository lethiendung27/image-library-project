# Slot rules — role × channel → candidate types

Stage 1 of routing (SPEC §7): a mechanical lookup producing the per-slot shortlist.
Stage 2 (the portfolio pass in `query/runbook.md`) then applies attribute gates,
`avoid_when`, and the cross-slot rules below. This table proposes; it never decides.

## Shortlist table

| Role | marketplace | landing-page | paid-social | advertorial |
|---|---|---|---|---|
| hero | `06-relief-hero` (commercial) | `06-relief-hero` (commercial) | `06-relief-hero` (ugc), `01-pain-scene` | `01-pain-scene` (header) |
| problem-agitation | `01-pain-split`, `02-symptom-rail` | `01-pain-split`, `02-symptom-rail`, `01-pain-scene` (confront) | `01-pain-scene` | `01-pain-scene` |
| cause | `02-cause-anatomy` | `02-cause-anatomy` | — | `02-cause-anatomy` |
| mechanism | `03-mechanism-ghostbody`, `03-spec-split`, `03-mechanism-xray`, `03-spec-explode` | `03-mechanism-ghostbody`, `03-mechanism-xray`, `03-spec-explode` | — | `03-mechanism-ghostbody`, `03-mechanism-xray` |
| proof | `04-proof-lockedframe` (verdict / timelapse) | `04-proof-lockedframe` (verdict / timelapse / capture) | `04-proof-lockedframe` (rivals / timelapse) | `04-proof-lockedframe` (all variants) |
| social-proof | `05-persona-grid` | `05-social-handoff`, `05-persona-grid`, `05-social-snapshot` | `05-social-handoff` | `05-social-handoff`, `05-social-snapshot` |
| personas | `05-persona-grid` | `05-persona-grid` | — | — |
| how-to-use | `03-use-sequence` | `03-use-sequence` | — | `03-use-sequence` |
| comparison | `04-proof-lockedframe--verdict`, `03-spec-split`, `01-pain-split` | `04-proof-lockedframe--verdict` | — | `04-proof-lockedframe--verdict` |
| outcome | `06-relief-hero` | `06-relief-hero` | `06-relief-hero` (ugc), `06-relief-scene`* | `06-relief-scene`*, `06-relief-hero` |
| cta | — (standard product shot, out of library scope) | — | — | — |

Two cells were TRIMMED rather than widened on 2026-08-11, because the type argued
against itself being there: `02-symptom-rail` off advertorial (03-spec-split's
avoid_when already rules that this infographic-tile aesthetic "signals cheap goods
off-marketplace", and the rail shares the register), and `06-relief-scene` off
landing-page (its use_when names only "an advertorial or final frame of an ads
creative"). Every other disagreement was resolved by widening the type — see each
type's CHANGELOG for the evidence.

`*` `06-relief-scene` only when its `requires_pair` (`01-pain-scene`, same person) is
also on the page.

## Attribute gates (deterministic kill-rules, applied in Stage 2)

| Attribute condition | Effect |
|---|---|
| `symptom_visibility: invisible` | drop `01-pain-split`; `02-symptom-rail` only if downstream symptoms are photographable (then vignette mode `visible-symptom`) |
| `visible_output` ≠ `none` | G8 binds: hero options must use the backlight branch; the output is the primary subject |
| static frame cannot show the product difference | `04-proof-lockedframe`: forbid `--rivals`/`--verdict`, require `--timelapse`/`--capture` (VARIANT SELECTION RULE — verified) |
| `mounting: fixed-installed` | G7-X: installed mode in every layer; ugc register needs the low-angle reframe (product + output as subject) |
| `operation: active` / `passive` | POSE branch: mid-action vs relaxed |
| `body_contact: false` | drop `03-mechanism-ghostbody`; mechanism slots fall to `03-mechanism-xray` (whose own `avoid_when` still gates trivial interiors and anti-tech-render categories) |
| `result_visibility: invisible` | drop `06-relief-scene` (close with `06-relief-hero` instead) |
| `multi_step_usage: false` | drop `03-use-sequence` unless buyers plausibly assume complexity |
| `colorways` has 1 entry | Zone B of `06-relief-hero` shows 1 unit only (fabricating a second colorway violates G2) |

## Cross-slot rules (portfolio constraints)

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

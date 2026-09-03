# Decision log (append-only)

Format: `ADR-NNN · date · title` — context, decision, consequences. Never edit past
entries; supersede with a new one.

---

## ADR-000 · 2026-08-10 · Architecture decision register (advisory session)

User-confirmed via gated advisory (full reasoning in the advisory transcript):

- **Runtime**: file-first, harness-agnostic. `SPEC.md` is the contract; `CLAUDE.md` is a thin adapter.
- **Governance**: controlled growth — match-first via job×device grammar; `_staging/`;
  promotion needs ≥5 distinct exemplars + router-confusion test + ≥1 rendered worked example + PR.
- **Scope**: single vertical (e-commerce physical products); user controls `content.json`
  schema (capability profile + image_slots).
- **Feedback**: human pick only → `feedback/picks.jsonl`.
- **G1** Source images outside git; sha256 identity; repo stores observation records.
- **G2** Ingestion is runbook-only (no classification scripts; shell one-liners like
  `shasum` are fine). Designed so migration to a script harness later is cheap: the
  classify template doubles as the script's prompt template.
- **G3** Full breakdown for every observation record (~15–25 images/session expected).
- **G4** Worked examples per type: hard cap 2, stale-flagged by validator.
- **G5** 3 options per slot, each varying on a named dimension (type / axis / execution).
- **G6** Pick-rate is a soft tie-breaker, active only at ≥20 picks per (type × role) cell.

## ADR-001 · 2026-08-10 · Grandfather clause for the founding corpus

The 12 seed types are `status: active` with `evidence_count: 0` — they predate the
observation ledger. Their evidence is the seed conversation (`conversation.md`), cited
in each CHANGELOG as `seed: conversation.md`. Promotion criteria (SPEC §6.3) apply to
**future** types only; founding types earn ledger evidence organically as ingestion runs.

## ADR-002 · 2026-08-10 · Registry v2.0.0 supersedes the v1.2 document

`aif-image-type-registry-v1.2.md` (5 types, single file) is superseded. The migration
seed is the **end state of `conversation.md`** (12 types, G7, axes, variants), which is
strictly ahead of the v1.2 snapshot. Both documents are kept at repo root as corpus,
never edited.

## ADR-003 · 2026-08-10 · G8 and G9 promoted to global rules

The conversation itself generalized two principles beyond their originating types:
visible mechanism ("if the product emits anything visible, light for it — it is the only
proof the image carries") and physical evidence ("expression is not evidence"). Encoded
as G8 and G9 in `registry/rules.md`, scoped to photographic-scene registers, instead of
duplicating them per type.

## ADR-004 · 2026-08-10 · Derived fields live only in the generated index

Supersedes one detail of the advisory Part 2 template: `evidence_count` (and pick
statistics) are **not** stored in type frontmatter. They are computed from the ledgers at
index generation. Reason: the validator must never mutate source files; a hand-editable
derived field is a decorative number waiting to lie.

## ADR-005 · 2026-08-10 · Version numbers assigned at migration

Versions reflect the conversation's final state plus structurally honest bumps:
`01-pain-split` → 1.2 (adding `--mirror` was a structural addition the conversation did
not bump); `04-proof-lockedframe` → 1.3 (v1.2 four-variant state + handheld-continuity
patch, which was evidence-based). All other types keep their last stated version.

## ADR-006 · 2026-08-10 · Render-test evidence stream; canonical assets path

The user set the library's primary goal explicitly: **tested** skeletons, not just
structured ones. Added the fourth operation RENDER-TEST (`eval/render-test.md` →
`eval/render-tests.jsonl`, validated by the validator) so worked-example `run:`
statuses advance only through recorded generation tests, under the same ≥2/3 evidence
rule as ingestion. Also fixed the canonical source-image folder (outside the repo,
per gate G1-B): `/Users/lethiendung/Downloads/image-library-assets/`.

## ADR-007 · 2026-08-11 · Verdict-gated autopilot: curation and commits run without manual review

Context: through batches B–E the owner's real touchpoints were two — feeding images
and confirming verdicts — while reviewing-and-committing accumulated diffs became the
bottleneck (five operations sat uncommitted in the working tree). Decision, stated by
the owner ("sau khi confirm pass … hệ thống sẽ tự chạy curate, commit … tôi không
cần đụng"): the **human gate is redefined as the owner's explicit inputs** — image
feeds, render verdicts (`pass | partial | fail`), picks, and direct commands. Once
such an input exists, the harness runs the consequent pipeline autonomously: ledger
appends → curation under the UNCHANGED evidence rules (≥2/3 · ≥3 · §6.3) →
`scripts/validate.py` → `git commit`. One commit per operation, evidence cited in the
message. Auto-commit requires **0 validator errors** (warnings allowed but surfaced).
Promotions still need all §6.3 criteria; criterion 4 is satisfied by the
owner-confirmed render verdict the package carries plus this standing authorization.
Commits stay **local** — no auto-push. Verdicts are never fabricated or assumed: no
owner verdict, no `run:` advancement, ever.
Consequences: git history becomes the audit surface (rollback = `git revert <sha>`,
reported with every commit); SPEC §1 invariant 5, §6.3(4), §8, `CLAUDE.md` rule 7 and
the close sections of `classify-batch.md`, `curate.md`, `render-test.md` updated in
this same diff; a local `.git/hooks/pre-commit` runs the validator as a safety net.
Supersedes the review-and-commit clauses of ADR-000's governance line.

## ADR-008 · 2026-08-11 · Graphic marks are model-drawn (integration approach A)

Context: the library legislates plenty of marks — 9 of 20 types declare a graphic slot,
another 4 carry marks inside other slots — but never said HOW they get produced. Three
architectures were built out as complete prompt sets in
`~/Downloads/mark-integration-test-v3.md` (21 prompts, 7 types, every mark family):
**A** the model draws them, **B** every mark is stamped after a clean render, **C** the
split — integrated marks rendered, geometric marks stamped.

Decision, by the owner: **A**. Marks are described in the prompt and drawn by the model.
No compositing pipeline, no `marks[]` field, no schema change. `adapters/nano-banana.md`
Rule 7 carries the production detail.

This was NOT the recommendation. C was, on the grounds that a baked mark cannot be A/B
tested and that precision-dependent classes are unreliable when model-drawn. A was
chosen anyway on defensible grounds: it works today with zero tooling, the editor stage
does not exist yet, and no render evidence yet contradicts it. Recording the
disagreement is the point — the decision stays auditable.

Consequences, stated so they stay visible rather than being discovered later:
- optimising marks empirically is off the table while this stands: changing a mark
  means re-rendering the image, so the base changes with it and no comparison is clean;
- a marks-free marketplace image and a marked landing-page image are two renders;
- three classes are at known risk — paired dashed reference lines, exact counts, and
  badge position/colour — all named in Rule 7.

What flips it: the standing evidence rule, unchanged. If one mark class fails on ≥2/3
runs or ≥3 observations, **that class alone** moves to post-composite as a Rule 7
exception with its evidence cited. A is a default, not a prohibition. Whole-scale
reversal to C needs the same kind of evidence, not a change of taste.

Not decided here: WHICH mark an image may carry. That is an argument decision — the six
mark families, the instrument and subtraction gates, and the one-class-per-image budget
were proposed but are the owner's to write, per the standing instruction that the
graphic-element rules are authored by hand, element by element.

## ADR-009 · 2026-08-12 · First scored calibration: 82%, no template change

Context: the anchor set was built 2026-08-11 but never scored, while 14 batches had run
against a rule of every ~5 (SPEC §6.1). The set's own note deferred the first run to a
later session, because building the table from the ledger and re-classifying in the same
session scores a classifier that has just read the answers. That trap bit again here in a
new form: the maintainer session had read `anchor-set.md` in full during orientation, so
it could no longer classify anything honestly. Method, owner-authorised: the 10 anchors
were classified in an **isolated classifier context** given exactly what SPEC §6.1
prescribes — `index.yaml`, `vocabulary.yaml`, `classify.md`, the images — and explicitly
denied `anchor-set.md` and `observations.jsonl`. Scoring then happened outside that
context. This separation is now the standing shape for calibration: whoever holds the
expected values may not produce the classifications.

Result, by the formula in `anchor-set.md`: **23/28 = 82%** — verdict 8/10, type 9/10,
axis-values 6/8. Above the 80% bar, so `calibrate.md` step 3 applies: record the score,
change nothing. `ingestion/prompts/classify.md` is **untouched** and `template_version`
stays `c1.0`, which matters more than the score does — a bump would discount all 104
existing records (curate.md §1) and every staging exemplar count rests on them.

Findings, in order of what they cost:

1. **Two genuine misses, one shape.** A6 answered `new-candidate → 03-use-rail` where the
   band is a four-step operation loop with ordering arrows; `03-use-rail` exhibits
   BREADTH (outputs, places, movements, zones), so ordered steps in rail geometry are
   still the `sequence` device. A7 answered `match → 01-pain-split --oldway` on a
   whole-product comparison with a gold VS at the seam; `--oldway` requires a person
   struggling with the legacy product and that panel has no person, while
   `03-spec-split --products` describes the image clause for clause. Both misses read the
   device and the job off surface geometry instead of argument structure — the one thing
   `classify.md` opens by forbidding. The invitation is partly in `vocabulary.yaml`: the
   `rail` gloss is geometric plus symptom content, and the index carries variant NAMES
   without their definitions, so `oldway` is guessable from the word alone. Proposed and
   NOT taken, because 82% does not authorise it and the cost is the whole corpus:
   a `classify.md` clause requiring the variant's own definition to be read before
   `match` is declared on it, plus an explicit rung for "matches an EXISTING declared
   variant → `match`", which the ladder currently omits.
2. **Two anchor rows were stale, and one of them was simply wrong.** A7 froze a
   `variant-candidate` whose proposal has since become the `--products` variant, so
   `match` is correct today — the A8 mechanism one rung lower. A5 froze
   `inset_mode=none` on the claim that no value covered a magnified-display inset, but
   `detail` has been in the vocabulary since the scaffold commit; the fresh run answered
   `detail` and corrected a ledger error. Calibration is designed to catch the classifier
   drifting from the anchors; it caught an anchor instead, which is worth knowing is
   possible. Both rows superseded per calibrate.md §5. Against the corrected expectations
   the same run scores 25/28 = 89%.
3. **The `gaze` axis has a hole.** A2 disagreed (`candid` vs frozen `confront`) on an
   image where the subject's face is squarely presented to camera with his eyes just off
   the lens axis — neither `--candid` ("unaware of the camera, gaze on their task or the
   ground") nor `--confront` ("looking directly into the lens") fits. `vocabulary.yaml`
   already carries a third value, `reflect`, which `01-pain-scene` does not declare. The
   founding record independently flagged the same slot (gaze hard-bundled with lighting).
   Two pieces of evidence, below the §6.2 threshold: proposed, not taken.
4. **The runbook could not be executed literally.** The manifest includes `.avif` and
   most of the corpus is AVIF, but the image reader returned AVIF as binary. A decode
   step is now in `classify-batch.md` §1, with the original file's hash kept as identity.
   A runbook fix, not a template fix, so no version bump. Also recorded there: formats
   outside the manifest list are outside the to-do by definition, which is what excludes
   `.gif` motion assets from batch input.

Consequences: `duplicate` remains uncalibrated (still zero such verdicts in 104
records). A9's proposed id diverged (`02-cause-cutaway` vs `02-cause-aura`) with neither
device value in the vocabulary, so both need a taxonomy addition and the divergence
decides nothing yet. Next calibration is due after ~5 further batches, and must again be
run by a context that has not read the expected values.

## ADR-010 · 2026-08-12 · G11: the saturation convention becomes a global rule

Context: an aggregation pass over all 110 observations (curate.md §1) surfaced three
deviation clusters at or past the §6.2 threshold. Two survived inspection; the third did
not, and how it failed is worth recording because the same trap will recur.

**The trap.** Raw deviation counts include deviations that have ALREADY been promoted into
a skeleton. The ledger is append-only, so a patched deviation keeps counting forever. The
`06-relief-hero [ZONE C]` cluster — `recall` executed as a two-cell transition with one
arrow, three observations, one of them literally annotated "THIRD observation, threshold
reached, patch due" — was already shipped as `FORM 2, transition pair` in **v1.5 on
2026-08-10**, citing those exact three hashes. Any future aggregation must diff candidate
clusters against the CHANGELOG before calling anything due. Nothing was changed for it.

**Cluster that did hold, and was split.** `06-relief-hero [ZONE A]` had five observations
of the human subject being reduced or absent, which is TWO decisions and not one:
`reduced` (present as hands, forearms or a shoulder) at 3 distinct observations, and
`absent` (no person at all) at 2. The first met the bar and is now a SUBJECT form choice
in the skeleton (v1.8) with the guardrail that a faceless subject needs a visible output
or finished state to carry what the expression would have. The second is a variant
cluster — its founding record proposes a `--product` hero — and at 2/3 it went to
KNOWN-FLAKY with both hashes and an explicit instruction not to ship a person-free hero
until a third distinct observation drafts the variant.

**Decision: G11.** The saturation convention — unresolved states desaturated, resolved
states high-key — is now a global rule in `registry/rules.md`. It was practised in seven
types and stated in none, and `04-proof-lockedframe` v1.5's CHANGELOG proposed exactly
this and deliberately declined it because it binds so many types. The owner authorised it
this session.

Two things make it safe to write at this scope rather than expensive:

- **Scope, not sweep.** SPEC §5 binds a rule by its own declared scope, so no type file
  needed editing to come under G11 — the G8/G9 precedent (ADR-003) promoted a practice
  without rewriting the types that originated it. Scope is photographic state-bearing
  layers; technical registers are out by construction, so `03-mechanism-*` and the
  `_staging` render types need no exemption flag and no version bump. Exactly one type
  declares `exempt_from: [G11]`: `04-proof-lockedframe` (v1.6), whose `[JUDGEMENT RULE]`
  and `--verdict` `[FAIRNESS RULE]` forbid the between-state difference G11 requires.
- **The substitution clause.** G11 lets a type mark an unresolved state with an explicit
  signal instead of desaturation where its own skeleton says so — `02-symptom-rail`'s
  red-glow vignettes and `06-relief-hero --recall`'s desaturate-or-X both already work
  that way. Without that clause G11 would have silently re-legislated types no evidence
  was collected about. What it forbids is an unresolved state carrying no marking at all,
  which is the actual observed failure.

**Evidence, stated in the direction it actually points.** The three ledger observations in
this cluster (`sha256:4f24b8…`, `sha256:6ab523…`, `sha256:cf4c74…`, all `01-pain-split`)
show source images DECLINING to desaturate the wrong panel — full colour, only duller and
flatter. They met the ≥3 threshold pointing the opposite way from the rule. So they are
not the warrant for G11; they are the proof that market imagery will not teach it, which
is the same shape as the VS-badge dialect the type refuses at nine observations. The
warrant is the library's own failure: the `--rivals` triptych of 2026-08-12 came back
cheerful on three panels all meant to read as unsolved. No practising type's skeleton was
weakened, and `01-pain-split` in particular keeps its desaturation law intact.

Consequences: G4 and G11 now split a boundary that used to have a hole in it — G4 governs
relative brightness between the sides of a comparison, G11 governs absolute grade
including the single-state image G4 never spoke about. Six of the seven practising types
still carry the convention as loose skeleton wording rather than a G11 reference; only
`06-relief-hero`'s Zone A grade line was annotated, because it was already being edited.
Annotating the rest is bookkeeping for whenever each is next touched, not a sweep to run
now.

## ADR-011 · 2026-08-12 · Render verdicts may be harness-assigned, for renders it has seen

Context: the owner's instruction, verbatim — "hãy tự gán nhãn cho ảnh, tôi sẽ không gán
nhãn. đã duyệt pass". Until now four separate places on disk said the verdict is the
owner's and must never be assumed: ADR-007, `eval/render-test.md` §6, `CLAUDE.md` rule 7,
and SPEC §6.3(3). This entry changes three of them and deliberately leaves the fourth.

**What made the old rule right, and what changed.** The rule existed because the owner
renders the images and the harness could not see them, so any harness verdict would have
been a claim about an image it had never opened. That is fabrication and the ban on it
stands. What changed is factual: since 2026-08-12 the owner drops every render into
`/Users/lethiendung/Downloads/image-library-assets/feedback/`, and the harness reads them.
Across seven renders that day its independent reading matched the owner's report every
time — it found the white border on all three `01-pain-split` frames, the absent exertion
on the first jar frame, and the packshot drift on the steamer frame before being told.
Assessing an image in hand is not assuming a verdict.

**Decision.** The harness assigns the verdict where the owner does not, under three
binding conditions:

1. **The render must be in hand.** No file in the feedback folder, no verdict. This is
   the anti-fabrication core and it is not negotiable.
2. **The label measures skeleton fidelity, and it is attributed.** Every self-assigned
   record carries `verdict_by: "harness"` in `notes` and states what was checked. `pass`
   keeps its defined meaning — an empty `failures` list — so a render with a visible
   defect is `partial` even when the owner has approved the set. Recording an approved-but
   -defective render as `pass` would delete the defect from the evidence base that
   justifies patching it, which is self-defeating: the white border that produced
   `01-pain-split` 1.5 is exactly such a defect.
3. **Promotion is excluded. SPEC §6.3(3) is left untouched** and still requires the
   owner's own verdict. A self-assigned label can support a §6.2 patch; it can never make
   a staging type routable. This is where the old rule's protection actually matters —
   a patch is one file and a `git revert`, while a promotion makes a type routable for
   every future page.

**The cost, stated rather than discovered later.** A harness label measures fidelity to
the skeleton. The owner's label measures fitness for purpose, and the two diverge. Today
gave the clean example: the second jar render was faithful on every slot and the harness
would have passed it, yet the owner's real objection was that a buyer still had to study
the frame to find the problem — and that objection is what produced the `--marked` variant
and the whole `01-pain-scene` 1.3/1.4 line. A harness-only loop would have missed it. So
the useful shape is not delegation-in-full: the harness carries the labelling, and the
owner keeps saying what the images have to DO.

Consequences: `SPEC.md` §1 invariant 5, `eval/render-test.md` §6 and `CLAUDE.md` rule 7
updated in this same diff; SPEC §6.3(3) deliberately unchanged. The owner keeps the veto,
and since the ledger is append-only a disputed label is corrected by a new record rather
than an edit. Supersedes the never-assume-a-verdict clause of ADR-007 only as to WHO may
label a render that has been examined; the ban on inventing a verdict for an unseen image
is unchanged.

## ADR-012 · 2026-08-12 · Each type owns its own mark library; the skeleton calls by name

Context: after five versions in one day, two skeletons had grown while the owner asked
repeatedly for shorter — `02-cause-anatomy` from 1962 to 2822 characters, `02-symptom-rail`
from 1587 to 2160. Every rule added had evidence; they were simply being written INSIDE the
skeleton. The owner then asked two questions: does an if/else in a skeleton consume prompt
context without engaging any reasoning, and should a type carry a small callable library
instead.

**On the first question, the contract already had the answer.** `query/runbook.md` Step 5
requires every conditional branch to be resolved before a prompt ships — "no branch may
remain unresolved in the output prompt" — so a branch never reaches the model at all. It is
a decision table for the writer. What branches cost is therefore not context but
correctness, and this session proved it twice: the dehumidifier arrow pointed out instead
of in, and the heat mark was amber where G3 reserves orange for wrong heat. Both were
branches resolved cleanly and chosen wrongly. The lesson is that a branch which states a
checkable condition defends itself, and a branch that only says "pick one of three" does
not.

**Decision, by the owner: each type gets its OWN mark library.** Not a central one. Two new
optional sections, added to SPEC §3.3 in the same diff: `PARTS` for a type's non-mark
building blocks, `MARKS` for its mark library. The skeleton becomes a call-map that names
entries; definitions live in the section once and are never restated in the skeleton or in a
rendered prompt.

I had proposed the opposite for one case — lifting the X/check verdict badge into
`rules.md` as a global rule, on the evidence that four types state that same law in four
different wordings (`01-pain-split`, `02-cause-anatomy`, `03-mechanism-ghostbody`,
`06-relief-hero`). The owner chose per-type ownership, and there is a real argument for it
that my proposal missed: a mark that looks identical can MEAN different things per type. The
X/check pair delivers a verdict in `01-pain-split`, where the whole image is a judgement,
and merely labels which panel is which in `02-cause-anatomy`, where the argument is a
measurement. Centralising the form would have implied a shared meaning that does not exist.
Per-type ownership also keeps a type self-contained, which costs nothing under progressive
disclosure since the type file is loaded whole at fill time anyway.

**The cost, accepted rather than argued away:** drift. Four types will keep describing the
same-looking badge four ways, and nothing forces them to converge. Mitigation, cheap and
non-centralising: each library entry carries an `also in` note listing the other types
where a same-looking mark lives, so drift stays visible from inside each file instead of
being invisible everywhere.

Consequences: `02-cause-anatomy` is the model implementation at v1.7 — file 25455 → 14171
characters, skeleton 1926 → 966, with ten marks carrying form, colour, count and evidence
status. Four of those ten have no render evidence (`baseline`, `axis`, `pressure`, `range`)
and are labelled proposals whose first render is their founding evidence. Whether to repeat
the structure on the other fourteen types is a decision to take after the model type has
been rendered against, not before.

## ADR-013 · 2026-08-13 · A type file states current law; git holds the reasoning

Context: three type files went from roughly 10k characters to 28774, 32409 and 32678 in a
single day of render-loop work. Measured at the point the owner called it: CHANGELOG entries
written before 2026-08-12 have a median of 240 characters, those written after it a median of
934 — 4.3x — and in `02-symptom-rail` the CHANGELOG reached 36% of the file. A second
measure isolated the same fault inside MARKS: `02-cause-anatomy` spent 337 characters per
mark, `02-symptom-rail` 2899, both written the same day by the same author. The difference in
both cases is not rules. It is the reasoning BEHIND the rules, written into the type file even
though ADR-007 already makes the commit message this project's audit surface — so every "why"
was being written twice, and the second copy is the one nobody ever deletes.

**Decision, owner-approved.** A type file carries current law only. Every explanation of how a
rule was arrived at is a pointer to the commit that made it. Concretely: a CHANGELOG entry
states the decision in a sentence or two and cites its commit; `MARKS` and `PARTS` carry
definitions and their own rules, not case histories; superseded wording is deleted rather than
kept beside its replacement, because git already holds it.

**Enforced as warnings, never errors.** `scripts/validate.py` gains two soft limits — a type
file over 22000 characters, and a single CHANGELOG entry over 600. Warnings only, deliberately:
ADR-007 blocks an auto-commit on errors, and a size guard that could block a commit would put
tidiness above evidence. The thresholds are derived rather than chosen — 22000 sits above every
untouched type file and below all three bloated ones, and only 4 of 44 pre-2026-08-12 CHANGELOG
entries exceed 600.

Consequences: 33 warnings on the day it was added, most of them earned. Types the render loop
has not reached are largely unaffected. `01-pain-scene` is over both limits and is owned by a
concurrent session; the warning is how it finds out, which is the guard doing its job rather
than one session editing another's file.

## ADR-014 · 2026-08-13 · Argument faults are catalogued centrally; the avoid line is dropped

Two owner decisions in one instruction, both from the same observation: the faults that keep
costing renders are not about wording, and they are not about the model.

**Argument faults get their own file.** Over four types the owner repeatedly caught images
that were correct in every slot and wrong in what they said — a pillow whose red mark read as
the pillow hurting the shoulder, a diffuser whose vapour read as causing a sore nose, a mark
that landed where nothing was claimed to be wrong. Each was recorded in the type that found
it, so each cost the next type the same discovery. `registry/argument-faults.md` now holds
them as a cross-type catalogue with observation counts, read before the first prompt of any
type and again when auditing one. SPEC §9's repo map and §6.2 name it in this diff. It is
deliberately NOT `registry/rules.md`: these are descriptive failures with evidence counts, not
prescriptive laws with scopes, and folding them into G-rules would give them a bindingness the
evidence does not yet support.

**The `avoid` sentence leaves the prompt.** Measured, not argued: the owner removed
`Strictly avoid: …` from a prompt set by hand, re-rendered, and the output did not change. The
line had been inherited by habit and never tested in isolation — which is the earn-its-place
rule the library already applies to every other clause. `adapters/nano-banana.md` Rule 1
step 2 is rewritten. The canonical NEGATIVE list stays in each type file and the `avoid` field
stays in the query output, so a future model with a real negative channel loses nothing.

One observation against it is recorded in the adapter rather than suppressed: a ghostbody
render with no avoid line returned dimension arrows labelled `W` and `L`, which G6 bans. The
likelier cause is the `dims` mark attracting a label, and the letter ban now lives in that
mark. If such leaks recur across types, the rule returns with evidence behind it.

Consequences: a concurrent session is writing prompts against Rule 1 right now, so this change
reaches it immediately — which is the reason it is recorded here rather than left as a habit.

## ADR-015 · 2026-08-13 · A clause is cut only when a render has done without it

Supersedes one clause of ADR-013. That entry gave the prompt budget as "a clause earns its
place in a rendered prompt only if a render has failed without it", and the wording is right
read forwards and wrong read backwards. Applied to an existing prompt it becomes "a clause
that has never coincided with a failure may go" — which is a different test, and a false one,
because a clause that has always been present has never been tested at all.

Measured on `03-mechanism-ghostbody` 2.0. Five clause groups were cut on the strength of ten
renders that had "held them without failing"; all ten renders carried them. Three cuts held.
Two broke on the very next render: `support` ran the whole thoracic spine once its length
limit was gone, and a defined face appeared in 2 of 3 mannequins once the ghost's negatives
were gone.

**Decision.** A clause may be removed only when a render has ALREADY done without it and come
back correct. Absent that, removing it is an experiment, not a cleanup, and is recorded as
one: cut it in a single prompt, keep it in the others, and let the pair decide. The
earn-its-place rule is unchanged for ADDING a clause; this governs removal only.

Consequences: the ADR-013 size guards stand — they measure the file, not the prompt, and
nothing here weakens them. What changes is the pace of compression: prompts get shorter one
tested clause at a time rather than in a sweep, which is slower and is the reason the sweep
looked attractive.

## ADR-016 · 2026-08-13 · Only five aspect ratios, and a type declares from that set

Owner instruction, system-wide and not scoped to one type: **only 16:9, 4:3, 1:1, 3:4 and
9:16 may be used. No other aspect ratio.**

**What this invalidates today.** `03-use-sequence` declared `ratios: ["1:1", "4:5"]` and every
prompt it has shipped asked for 4:5, which is not in the set; it moves to `["1:1", "3:4"]`.
`04-proof-lockedframe` declares `["5:3", "16:9", "1:1", "3:2"]`, of which **5:3 and 3:2 are
outside the set** — that file belongs to a concurrent session and is not touched here, which is
the reason this is written down centrally rather than fixed in passing. Any other type
declaring a ratio outside the five is wrong from now on and is corrected when it is next
opened.

**Why it is worth an entry rather than a habit.** A ratio is not decoration for this library, it
is the thing a multi-panel layout has to survive. Measured on `03-use-sequence` the same day:
with a 1200x896 frame, 4 of 6 renders kept the three panels stacked as instructed; with a
1376x768 frame, 2 of 16 did. The layout wording did not weaken between those two batches, it
got stronger. Three stacked panels inside 16:9 gives each panel a 5.4:1 strip, and every
arrangement the model substituted — side by side, 2x2, one large panel with two small — fits a
wide frame better than the instruction does. One product settled it: the soap dispenser ran
twice on identical text and came back stacked once and side by side once.

So a declared ratio has to be a ratio the renderer will actually produce, and a short closed
set is what makes that checkable. A type whose layout needs height declares `3:4` or `9:16` and
stops asking for something in between.

**Consequences.** `scripts/validate.py` has no ratio check today; adding one would make this
enforceable rather than remembered, and it is proposed rather than done here because the
validator is shared and a second session is live. Until then it is a reading rule. The standing
`RATIO:` sweep already owed on five active types and five staging files should apply this set
when it happens, rather than preserving whatever each file currently names.

## ADR-017 · 2026-08-14 · What a slot label may name, and where a called definition is expanded

Two contradictions surfaced by `05-social-handoff`'s first render round, both delegated by the
owner with the instruction to decide for the system rather than for the type.

**1. Rule 6 taught authors to write the fault Rule 1b bans.** Rule 6's worked example of house
slot form was `SCENE right 58%:` — a region name carrying a frame share — and Rule 1b bans
exactly that shape, measured drawn into frames on two types. An author following the house style
therefore produced the leak the adapter's own rule forbids, which is how `06-relief-hero` 1.9
reached ten instances in one prompt set before a gate caught them (`42b2dea`).

Slot form was never what leaked; the LABEL was. Rule 1b now states the three tiers the evidence
supports — whole-image headings and subject headings have never been drawn, region headings have
been drawn on every type that used them — and Rule 6 item 4 keeps slot form with a legal example.
Frame share and offset stay a real prompt job under Rule 4 and move from the label into the block
body. Nothing measured is weakened: Rule 6's 57% compression stands, and Rule 1b's ban narrows
from "any slot name" to the class that actually leaks, which makes it enforceable by a gate.

The distinction itself is not new — it was found and used when `06-relief-hero` 1.10 rewrote its
zone names — but it existed only in a commit message, so the file kept teaching the fault. That
is the reason this is worth an entry: an unwritten refinement cannot reach the other lane. The
subject tier is new evidence, and thin: `05-social-handoff` shipped `[ADVOCATE]`, `[LISTENER]`,
`[PRODUCT]`, `[ENVIRONMENT]` and `[COMPOSITION]` three times with nothing drawn (`27f19e3`),
recorded as three runs rather than generalised.

**2. SPEC §3.3 forbade what every working prompt in this library does.** It said a `PARTS` or
`MARKS` definition is "never restated in the skeleton or in a rendered prompt". The first half is
ADR-012's actual decision and stands. The second half was never true and cannot be: the model
never reads the type file, so a called name that is not expanded arrives as a bare word. Every
rendered prompt this library has shipped expands its definitions in full, and must.

The contract already held the correct pattern one file away — adapter Rule 6 item 2 gives global
rules precisely this treatment: referenced by ID in the type file, expanded at render time,
carried once in the prompt. §3.3 now gives `PARTS` and `MARKS` the same law. This corrects a
false statement rather than changing practice: no type file and no prompt changes.

**Why an ADR and not a passing fix.** Both files are global law and a second session is live in
this repo, so the log is how the other lane finds out — the precedent ADR-014 set for the same
reason. `scripts/validate.py` encodes neither wording, so nothing enforces or breaks, and
`registry_version` is unchanged because no data or structure moves.

Consequences: `adapters/nano-banana.md` Rules 1b and 6, and `SPEC.md` §3.3, edited in this diff.

## ADR-018 · 2026-08-14 · A GIF is a reserved cell in an existing layer, not a new mark

The owner composites the loop into the still by hand, and asked for the GIF to become a
mark on the types that already carry a layer. Owner's call taken; the shape it is given
here is narrower than "a mark", for two reasons the evidence forced.

**A mark is the wrong unit.** A MARKS entry would repeat one definition across the four
types that host a layer — `06-relief-hero`, `02-symptom-rail`, `03-spec-split`,
`05-social-handoff` — take a slot in each one's mark budget, and need a G3 colour that
motion does not have. What the loop actually occupies is a layer those types already
legislate, so it costs one axis token, `inset_motion: still | loop`, and one rule. The
argument-level reading stays intact: the cell is bounded, anchored and counted, and A11
holds — a photograph does not contain a bounded macro of itself.

**Six renders on 2026-08-14 settled the FORM before any law was written.** Four wrote the
brief into the frame as a text card and all four faulted; one of them rendered its
markdown asterisks literally, which is G6's own argument made in the plainest possible
way. Two drew a cell instead and both read as a hole. G12 is written from that split and
from nothing else — it governs the reservation, not the motion.

**What is still unknown.** No loop exists in `eval/render-tests.jsonl`, so `--loop` ships
with `06-relief-hero` alone and its first render is founding evidence. The other three
hosts inherit G12 by reference when a page needs them; none is edited here.

**A capability claim four type files are currently guessing at.** `05-social-handoff`
gates its inset off as "unavailable without compositing", `01-pain-split` and
`03-spec-split` each reason from "a renderer who does not composite", and
`04-proof-lockedframe` drops its `strict` camera for the same stated reason. The owner
composites. The capability is narrower than full compositing — an overlay dropped into a
reserved area — but it is not absent, and four files inferring it separately is how one of
them ends up wrong. Flagged here rather than fixed: two of those files belong to a
concurrent session, and the claim should be measured once and recorded once.

Consequences: `registry/rules.md` gains G12; `registry/types/06-relief-hero.md` goes to
1.13; `query/runbook.md` Step 5c states where the reservation clause is emitted.
`registry_version` is unchanged — an axis value moves, no structure does.

## ADR-019 · 2026-08-14 · Supersedes ADR-018: the cell carries the brief, and an editor fills it

ADR-018 was written the same day from a premise I invented and the owner corrected within
the hour. It said the owner composites the loop by hand, and concluded that the cell should
be a mask-free HOLE holding the loop's first frame, with no text anywhere near it. Both
halves are wrong.

**An editor builds the loop.** The render is not a hole for the owner to fill, it is a
**work order** for someone else: the loop's five-field brief drawn INTO the frame, inside a
plate whose shape the slot declares — square, circle or rounded rectangle. Where the
verdict is `whole-frame` the plate IS the delivered image and no photograph is made,
because the whole frame gets replaced anyway.

**So the text belongs in the picture.** ADR-018's "no text, no digits and no glyph" was the
load-bearing clause of the old G12 and it is now inverted. The owner's grounds, and they
are his to give: the model writes text well enough in his hands, and an editor who has to
open a JSON to find the brief is an editor who will not. G6 is not breached because the
plate is **production-only** and never reaches a page — a render carrying one takes the
`--brief` suffix so it cannot be mistaken for the slot's asset.

**What survives from ADR-018, unchanged.** The unit: an axis value on a layer four types
already legislate, not a MARKS entry repeated four times with a G3 colour motion does not
have. The scope: `06-relief-hero` only, the other three hosts inheriting G12 by reference.
The capability finding: four type files still each guess separately at whether this
pipeline composites, and it does — an editor is the compositing step, which strengthens
rather than weakens that flag.

**What the six renders of 2026-08-14 actually taught,** now that the plate is the
deliverable. The dominant fault was never the lettering: two of four plates described
motion the frame could not support, which is G7 applied to a caption, and a caption
describing a different picture cannot be checked against the picture it sits on. One
rendered its markdown asterisks literally, so the brief goes in as plain words. Two took
55% of the frame width, so a plate that will not fit its host drops lines rather than
growing. Five of six bled to an edge, so G10 binds as it always did. Circle and rounded
rectangle both rendered clean, which is why shape is now free.

**Why supersede rather than edit.** This file's own header forbids editing past entries,
and a second session reads it. The wrong version cost one commit, `2458407`, and is left
standing so the correction is legible rather than silent.

Consequences: `registry/rules.md` G12 rewritten; `registry/types/06-relief-hero.md` at
1.14; `query/runbook.md` Step 5c. `registry_version` unchanged.

## ADR-020 · 2026-08-17 · A gif slot emits a plate render, never a motion prompt, and it sits as a fourth option

ADR-019 settled that an editor builds the loop and the work order is drawn INTO the
render. Two files kept the superseded premise anyway, and neither was caught because both
read as law. `query/output.schema.json` told every session that `gif.prompt` is "a
runnable motion prompt ... written against the STILL the slot's recommended option
produces — animate that frame, never regenerate it". `query/runbook.md` Step 5c described
the same field as the brief "written out", naming what moves "so the loop cannot drift
from the frame it lands in". Both describe a pipeline that composites, which ADR-019
records the owner correcting within the hour of ADR-018.

Page 58 was built from those two descriptions and shipped two prompts beginning "Animate
the supplied render". The owner corrected it today. A session that reads the schema and
the runbook and follows both faithfully still gets this wrong, so the fix belongs in the
files rather than in a session's care.

**A positive `gif` verdict emits exactly one prompt, and that prompt renders the plate.**
Two shapes and only these two, both already in G12. `whole-frame`: the plate IS the
delivered image, a flat card of text with no scene and no product — the form that passed
1 of 1 in `eval/render-tests.jsonl` record 209, the case that proved the model writes the
brief reliably. `inset`: the host type's own prompt sets the layer its SKELETON already
legislates to `--loop` and draws the plate there, geometry inherited. No motion prompt is
emitted anywhere in the pipeline.

**The gif renders alongside the recommended still, not instead of it.** Step 5c's "emit
the brief, not three photographic options for a frame that gets replaced" is about the
plate, which gets one brief rather than three executions of itself. A card reading "left
sled shakes, its beam wanders" hands an editor nothing to move; record 209 flagged
exactly that as the highest-risk case in its set. So in `prompts.md` the gif is a fourth
option below C with the options' own anatomy, which is where the owner put it.

**The brief's header line is `GIF SLOT`, not `GIF`.** G12 writes `GIF SLOT` and 4 of 4
passing renders drew it; Step 5c's template had dropped the word.

Consequences: `query/output.schema.json` `gif.prompt` and `gif.asset` descriptions
rewritten; `query/runbook.md` Step 5c rewritten and its template line corrected;
`query/sessions/58-how-i-rescued-trapped-family-dvds/` rebuilt. `registry/rules.md` G12 is
unchanged — it was already right, and that is the point. `registry_version` unchanged.

## ADR-021 · 2026-08-17 · The render capability is declared once, and multi-pass is never emitted

ADR-019 flagged it and did not fix it: "four type files still each guess separately at
whether this pipeline composites". They guess because nothing in the repo answers. Four
type files carry a clause of the form "where the renderer cannot composite", and a session
routing a page has no way to evaluate it, so it evaluates it by feel.

Owner instruction, 2026-08-17: **this pipeline is paste-and-run — one prompt, one
generation call, at most one reference photo attached. No compositing, no edit chains, no
post assembly.** `adapters/nano-banana.md` records that the model supports conversational
editing and that multi-pass is "officially viable"; that is a fact about the MODEL. The
constraint is the operator, and the two were never distinguished.

**Declared in `query/runbook.md` Step 3**, beside the other gates, because Step 3 is the
pass that evaluates them. Not a new file: a capability nothing reads goes stale, and the
routing pass is the only reader there is.

**No type becomes unavailable.** Each affected execution takes the single-pass route its
own file already records, which is the useful finding here — the library had already
solved this three times and no one had collected it. `04-proof-lockedframe`: `strict`
needs compositing, so the panels run `handheld`, `--verdict` included. `01-pain-split
--mirror`: the invariants block, which that file calls "the only route available to a
renderer who does not composite" and which passed 1 of 1 against multi-pass's 1 of 1.
`05-social-handoff`: the `inset` is dropped, not the type, and the file calls the
inset-free route "the safer route" on its own grounds.

**The consequence worth naming.** Single-pass handheld does not hold identity on its own —
`04-proof-lockedframe` says so at its own line 111. What replaces the edit step is words:
an invariants block naming the object before the panels. So this declaration moves a
guarantee from the pipeline into the prompt, and identity drift across panels becomes the
thing to watch in the ledger rather than a thing that cannot happen.

Where a type offers no single-pass route at all, it is unavailable and the slot takes its
next candidate, said out loud in `page_composition_notes`. An option whose `pipeline` is
not `single-pass` is now a routing defect.

Consequences: `query/runbook.md` Step 3 gains the declaration and the gate;
`registry/vocabulary.yaml` `generation_modes` gains a pointer to it, and its stale
`inset_motion` comment is corrected from ADR-018 to ADR-019 in the same pass;
`query/sessions/58-.../` reports run-state per option. No type file is edited — every
fallback cited above was already written. `registry_version` unchanged.

## ADR-022 · 2026-08-18 · A repeating section emits one option per slot, and the SET is the unit of variation

G5 has said "3 options per slot" since ADR-000 and it is right for a linear funnel,
where a slot is a decision and three options are three ways to make it. A repeating
section is not that. Its slots are siblings, and what varies is the SET.

Owner instruction, 2026-08-18, on page 65's six-tile review wall: **one option per
slot for a repeating section.** The grounds were already in the library and nobody
had connected them. Cross-slot rule 2 exempts repeating sections from one-type-once
"provided the instances differ on a named dimension". `05-social-snapshot`'s own SLOT
CONSTRAINTS legislate a SET DIVERSITY LAW: "when a page requests more than one
snapshot, every image must differ COMPLETELY — different room class, surface, light
temperature, camera distance, and content mode where possible." Both rules put the
variation between tiles. Three options inside one tile spend it in the dimension
where it buys nothing.

**The harm is not waste, it is a door no check can close.** Options are individually
legal but not necessarily legal in COMBINATION, and the runbook says so. On a six-tile
wall with three options each, a reader picking one register on three tiles and another
on three gets a set that is legal option-by-option and broken as a wall: some tiles
anonymous phone snapshots, others two-person documentary scenes. That reads as two
shoots, and the type's own words are that one shoot reads as fake. Nothing in the
checks caught it, because every check ran per option.

**Dropping to one option exposed a defect three options had been masking.** Page 65's
six first-drafted A-variants gave two bedrooms AND two kitchens across four at-rest
modes — a straight breach of the SET law that nobody would have seen while B and C
sat beside them. Tile 4 now keeps what was drafted as C, and the set runs bedroom,
bedroom, landing, bathroom, living room, kitchen across three content modes. Which
execution a tile keeps is decided by the set law, not by the letter A.

**"Where possible" is a real qualifier, not a hedge.** Two of the six quotes are
intrinsically about a mattress; moving one into a kitchen would buy a diversity axis
by breaking FIT. The repeat stands and the option states which of the four remaining
axes carry the difference instead.

Consequences: `query/runbook.md` Step 4 gains the rule; `query/sessions/65-.../`
emits 30 prompts rather than 42 and checks its own set diversity on every run, with
the room classifier picking by earliest occurrence rather than vocabulary order —
"a landing between two bedrooms" is a landing, and order-scanning called it a
bedroom. G5 is unchanged for linear slots. `registry_version` unchanged.

## ADR-023 · 2026-08-19 · The GIF library: six types, a page motion floor, and a static review wall

The owner asked for a classified GIF library: folders by gif type, a human filing each
file, AI proposing the type, and a mapping the harness can call. Three things were
already true and none of them had been connected. ADR-019 had settled that an editor
builds every loop, ADR-020 that a positive `gif` verdict emits a plate and sits as a
fourth option, and Step 5c had been asking `gif.kind` from the `jobs` vocabulary since
then — so a consumer of a GIF library existed, with no library behind it.

**The taxonomy is the one already in the repo.** A first pass proposed nine gif types
with a new device word each (`use-howto`, `use-interaction`, `spec-transform`,
`spec-unboxing`, `pain-failure`, …), which would have needed nine vocabulary additions
and a second name for every idea `jobs` already names. The owner pushed back on whether
`howto` and `transform` earn separate folders. They do not, and applying SPEC §3.2's
absorption ladder to motion is what collapses them:

- **Beat count is a PARAMETER.** In a still, one frame against three stacked panels is
  structural and names two devices. In a loop it is duration. One continuous act and a
  three-step sequence argue the same thing — you can operate this — so `use-howto` and
  `use-interaction` are one type with a beat band.
- **`spec-transform` was an act wearing a spec label.** Take the hands out of a folding
  umbrella and the argument collapses; the act is `use` and the "packs to a third" claim
  is `proof`.
- **Enumeration is not change.** Laying a kit out reveals what exists, and Step 5c has
  always refused motion to a slot that reveals rather than changes. That removes `spec`
  from the page entirely and leaves `unboxing` alive only where a reveal is a legitimate
  hook, which is the ad channel — enforced by `channels: [paid-social]`, not by prose.
- **`pain-failure` is an execution of `cause`.** A hand slipping and a weave shedding
  grains make one argument; subject class is what `varies_on` is for, and page 65's
  rung-2 route already ran `01-pain-scene` object-only on exactly that reasoning.

What survives is **`use`, `mechanism`, `cause`, `proof`, `relief`** for pages plus
**`unboxing`** for ads. Five of the six ids are `jobs` values, so `gif.kind` needs no new
enum member and the page side of this ADR costs zero vocabulary — the leaner list is also
the cheaper one, which is the signal the merge was right rather than merely tidy.

**Five boundaries do the work the names cannot.** `use` against `mechanism` is decided by
framing, not subject — hand plus whole product against the working part magnified with no
person. `mechanism` against `proof` is cause against effect. `cause` against `proof` is
the product's absence, and that absence is the whole test. `proof` against `relief` is
measured against lived. And `relief` earns motion only where the motion IS the thing the
problem used to block — the tightest rule in the set, written to stop `relief` becoming
the bucket every unearned loop falls into, and explicitly untested against any render.

**The floor is the owner's number, and the evidence says it is not a stretch.** Standing
instruction: at least 2 loops per page, ceiling 5, at most one per section, never two
adjacent. Measured across the five routed sessions — 60 image slots, 19 positive verdicts
— every page already clears 2 on rung 1 alone (5, 6, 4, 2, 2). Against the market the
number is deliberately one notch high: of eight live pages scanned on 2026-08-18, the
advertorial and listicle formats carry 0–2 argued motion elements and only brand product
pages run 4–8. So the floor asks these pages to be slightly richer in motion than their
format's norm, which is the owner's call to make and is recorded here as such: the
premise that GIF converts best is the owner's commercial experience, `feedback/picks.jsonl`
is still empty, and nothing in this repo verifies it. The `motion` block exists so the
claim can be checked later instead of assumed.

**The backup ladder fills a shortfall without lowering the bar.** Rung 1 is the 5c verdict
as it stands. Rung 2 re-executes: a `proof` slot routed to a locked multi-panel still is
correctly refused motion — "inspected, not watched", 0 of 13 such slots earned a verdict —
but that is a fact about the panels, not the argument, and one continuous frame in which
one variable changes earns motion on the same claim. Page 65's own copy carries the case
the session passed over: an indicator turning red to blue as the head passes, filed as "a
state, not a transition". Rung 3, ambient, is **off**, and may never be used to reach the
floor; a page that cannot argue in motion reports a shortfall instead. Grounds: every
ambient element found across the eight market pages was a theme's own CSS, not a produced
asset.

**The review wall is static, and this supersedes a shipped verdict.** Owner instruction.
Session 13 called a customer's phone clip more authentic than a customer's photo and gave
`social-viral` a positive verdict; sessions 37, 58 and 65 refused all 14 of their
`social`-role tiles on the opposite reasoning, and nothing in the repo adjudicated the
split. It is adjudicated now in favour of static. Page 13 is left standing and is not
re-routed, so the correction is legible rather than silent — the same treatment ADR-019
gave ADR-018. Three of three review walls among the market pages scanned are static.

**Why the library lives half outside the repo.** SPEC §6.4 keeps source images out and
references them by sha256; motion assets are larger and the rule binds harder. So
`registry/gif-types/` holds the law, `ingestion/gifs.jsonl` holds the index, and the files
sit in a folder tree outside the repo whose cards are GENERATED from the type files by
`scripts/gen-gif-cards.py` — a card is a view, like `registry/index.yaml`, and hand-editing
one is the same error as hand-editing the index. Naming is
`{gif-type}_{product-slug}_{seq}.mp4`, with the sequence issued by the ledger so two people
cannot collide, and no provenance field: the owner audits the library himself and declined
to carry a ref/made split. The consequence is stated rather than hidden — nothing in a
filename now separates a collected reference from an owned asset, and that boundary lives
in the owner's own review. Revisit it the day a second person files into the library.

**The asset a slot returns is named twice, on purpose.** `gif.output` is the slot's own
`asset` with the extension changed to `.mp4`, because a page numbers its assets by page and
an editor tracks by slot. The library name is issued separately when the finished loop is
filed back, because the library numbers by type. The ledger maps the two through the
sha256, and one asset therefore serves every clone of a product — the catalogue the owner
supplied runs 179 landing pages over 70 products, 2.6 per product and up to 7, across
English, German and UK domains. That reuse is also the operational reason G6's ban on text
in frame binds a loop exactly as it binds a still: one English word destroys it.

Consequences: `registry/vocabulary.yaml` gains `gif_types` and `gif_groups`;
`registry/gif-types/` and `registry/gif-instruction.md` are new; `ingestion/gifs.jsonl` is
a new append-only ledger; `scripts/gen-gif-cards.py` is new; `scripts/validate.py` gains a
gif type pass, a ledger pass and a check that the floor is satisfiable at all;
`query/runbook.md` gains Step 5d; `query/output.schema.json` gains `motion`,
`recommended_media`, and `type_id` / `rung` / `refs` / `output` on `gif`; `SPEC.md` §3.6
and §9. No existing session is re-routed and no image type file is touched.
`registry_version` unchanged — no image structure moves.

## ADR-024 · 2026-08-19 · Corrects ADR-023: the wall rule never touched page 13, and never-adjacent breaks the floor

Step 5d shipped in ADR-023 without ever having been executed. Running it dry against all
five routed sessions the same day — no session re-routed, only what the rule WOULD say —
returned two defects and one finding. This is the case for running a rule before trusting
it: both defects are invisible to a reading and obvious to an execution.

**Defect 1: ADR-023 credits the wrong rule for page 13.** It says the static-wall
instruction supersedes that session's `social-viral` verdict. It does not.
`social-viral` is a STANDALONE social-proof slot with three `05-social-snapshot`
options; page 13 has no repeating review section at all, and its `comments-thread` slot
carries no image. The wall rule governs tiles in a repeating review section and this is
not one, so it never reaches this slot.

The verdict still cannot recur, for a stronger reason that ADR-023 established two
paragraphs earlier and then failed to connect: **the six-type set carries no `social`
type.** A social-proof slot has nothing to file a loop under, wall tile or standalone.
That is the mechanism a router actually hits, and it makes the consequence wider than
the owner's instruction reads on its face — ALL social-proof motion is out, not only the
wall. Recorded here so it is a stated consequence rather than a surprise the first time
a session refuses a UGC clip that looks perfectly good.

**Defect 2: the spacing clause breaks the owner's own floor.** ADR-023 wrote "at most one
per section; never two in adjacent slots" as if the two were one rule. They are not, and
the second is wrong. Page 58's two eligible loops sit at consecutive slot indices —
`problems.items.1.image` then `features.items.0.image` — but across a section boundary,
with a heading and a block of copy between them. Enforcing never-adjacent drops that page
to one loop, below the floor of 2, to prevent a collision no reader can see. Measured over
the five sessions, the clause as written meets the floor on 4 of 5 pages; the revision
below meets it on 5 of 5.

**Resolution: one spacing rule, and a repeating list is ONE section.** At most one moving
item per section, with a reason list, a feature list or a review wall counting as a single
section rather than one per item. This is ADR-022's SET-is-the-unit applied to motion, and
the dry run shows the same failure ADR-022 found in options: page 31 drafted four moving
tiles inside one `features` list and page 37 three inside one `story` list — the fairground
the rule exists to prevent, invisible while each tile was judged alone. Which item keeps
the motion is decided by the section's own set law, not by position. The never-adjacent
clause is dropped: inside a section it is redundant, across one it is harmful.

**The finding, which changes no rule but changes where the work is.** The coverage
preference — one `working` loop and one `result` loop — is met on 2 of 5 pages. Three
pages are working-only: 58 and 65 carry `cause` + `mechanism`, and 31 carries hero, cause,
mechanism and use with nothing on the result half. So `result` is systematically
underserved by rung 1, and rung 2's restaging of a locked multi-panel `proof` is not an
edge case for thin pages — it is the main route to the second half of the floor on a
majority of pages. ADR-023 called it a backup. It is closer to a default.

Floor and ceiling themselves need no change: 2 is met by every session before spacing and,
under the revised rule, after it; 5 is never approached (the busiest page carries 5 before
spacing and 4 after, once `social-viral` loses its type).

Consequences: `query/runbook.md` Step 5d rewritten in two places — the spacing paragraph
and the social-proof paragraph. ADR-023 stands unedited, as this file's header requires;
the wrong sentence is left legible rather than silently repaired, the treatment ADR-019
gave ADR-018. No session is re-routed, no type file changes, no schema field moves.
`registry_version` unchanged.

## ADR-025 · 2026-08-19 · One asset folder with three siblings, and the manifest reads only one of them

The owner asked for the project's scattered local files to be gathered into one folder.
Doing it surfaced a latent defect in the INGEST operation that had nothing to do with
tidiness, and that is the reason this is an ADR rather than a path edit.

**The classification manifest was eating the library's own renders.** `classify-batch.md`
§1 rooted its `find` at the asset folder and recursed. That folder also held `feedback/`,
where render outputs land. Measured 2026-08-19: 108 unique image hashes at the root, all
108 already in `observations.jsonl`, 0 outstanding — the market corpus is **fully
classified**. The `feedback/` folder held 324 further images, **none** ledgered. So the
runbook's to-do list was 324 items, every one a picture this library produced, and a
session following it literally would have spent a batch teaching the library its own
output back to itself. SPEC §6.2 counts observations toward the ≥2/3 deviation rule, so
those records would have become self-generated evidence for changing the very types that
made them. Nothing in the repo would have flagged it: the records would have been
well-formed, and the verdicts plausible.

It also hid a fact worth stating plainly: **the corpus is exhausted.** The honest to-do
list is 0, and the answer to that is new source images, not a wider `find`.

**The fix is structural, not a warning.** The asset folder now holds three siblings —
`stills/` (the market corpus), `feedback/` (this library's renders), `gifs/` (the GIF
library, §3.6) — and the manifest points at `stills/`. Contamination is then impossible by
construction rather than avoided by care, which is the same reason `_staging/` is a
directory rather than a status field.

**Why the GIF library moved in as a sibling and not inside the stills.** Both are source
media outside the repo, identified by hash, and one folder is one thing to back up. But
nesting the typed GIF tree inside the flat stills bucket would have put every reference
still an editor drops beside a loop — a poster frame, a grade reference — straight into the
image to-do list, which is the defect above with a new door. As siblings they share a
parent and share nothing else. The two libraries also keep their opposite organising
principles intact: `stills/` is flat and its classification lives in the ledger, `gifs/` is
typed and the folder IS the classification (ADR-023).

**The repo did not move.** It is already a single self-contained folder, and relocating it
mid-session would break this session's working directory and any parallel session on the
same repo — the owner's normal working pattern is more than one session at a time. If it
should live under the same parent, that is a deliberate step to take when nothing else is
running, not a side effect of a tidy-up.

Consequences: `ingestion/runbooks/classify-batch.md` §1 manifest path and a new paragraph
stating why it is load-bearing; `SPEC.md` §6.4 names the three siblings;
`scripts/gen-gif-cards.py` default root follows the move. `observations.jsonl` is untouched
— no record was wrong, the to-do derivation was. `registry_version` unchanged.

## ADR-026 · 2026-08-19 · The pick-rate denominator counts options, so one review wall fills a cell six times over

The owner confirmed today that they do compare options A, B and C and choose between
them, rather than rendering A and ignoring the rest. That answer makes SPEC §7.7 the live
consumer of `feedback/picks.jsonl` and turns the never-executed logging loop into the next
piece of work. Before building it, §7.7 was run dry against the six routed sessions — the
ADR-024 method, no session re-routed, only what the rule WOULD say — and the rule is wrong
in both directions at once.

**The denominator counts options, and most options are not a choice between types.**
`pick_stats` increments a cell's `shown` once per entry in `options_shown`. Measured over
the corpus: 74 slots carry options and 179 options were emitted, but only **20 of those 74
slots offered more than one distinct type**. Forty-two offered two or three executions of a
single type, where `varies_on` names an axis or an execution and the type never changes;
twelve offered one option only, the repeating tiles ADR-022 cut to a single option. So 179
increments stand in for at most 20 type-level choices, and a rate whose whole job is to
compare types against each other is computed over a denominator that is mostly not a
comparison.

**The consequence is not academic — it lands on exactly the wrong cell first.** The only
cell in the corpus that reaches the threshold of 20 is `05-social-snapshot × social-proof`,
at 45. Of the 24 social-proof slots across the six pages, **exactly one** offered a choice
between types. A review wall is four to seven tiles of one type in one role, and since
ADR-022 each tile carries a single option, so one page-level decision enters the statistic
four to seven times. The first cell that would ever have started steering the router
accumulated 45 observations from one real choice, and it would have started steering it
toward the type that had never once been chosen over another.

**The fix is the derivation, not the record.** A slot counts toward a cell only where more
than one distinct type was on offer — where the type could have lost — and then once per
distinct type, never once per option. This needs no schema change: `options_shown` already
carries `type` per option, so contest is derivable from the record exactly as it was
already specified, which is the strongest evidence available that the record shape was
right and only the reading of it was wrong. The record therefore stays **one per slot**,
walls included: tier 1 is raw evidence and is never thinned, ADR-004 puts derived numbers
only in the generated index, and the log is also the audit trail of what the owner was
shown. `query/runbook.md` Step 7.2 now says so, because the obvious economy — stop logging
the wall, it counts for nothing — is the wrong one.

**The second half of the finding is stated and deliberately not fixed.** Under the
corrected denominator the busiest contested cells stand at 3 after six pages
(`02-cause-anatomy × mechanism` and `06-relief-hero × outcome`), which reaches 20 at
roughly 40 pages against 33 landing-page exports in hand. The threshold as written is
therefore unreachable on the present corpus, and it is left at 20 anyway: `picks.jsonl`
holds 0 records, so any replacement number would be chosen on paper, which is the error
this repo already declined to make when it held back the GIF evidence ledger until a real
loop comes back. Borrowing `MEASURE_MIN = 3` from `gen-gif-cards.py` would be the same
error wearing provenance. Revisit the number when the ledger holds real records, and let
those records decide it.

**Verified against known-bad input before it was written.** A harness exercising
`pick_stats` directly failed 3 of 5 real cases under the old code — the six-tile wall
returned `shown: 6, picked: 6`, three executions of one type returned `shown: 3`, and a
genuinely contested slot double-counted the type that appeared twice — and passes 5 of 5
under the new code, with a deliberately wrong liveness case that still fails, so a green
run proves something rather than proving the harness is inert.

Nothing generated moves today. With `picks.jsonl` empty, `render_index` emits `picks: {}`
for every type under both implementations; the fix changes what the FIRST record will mean,
not what the index says now. One thing is knowingly left undone: a record whose `picked`
names a type absent from `options_shown` is malformed and nothing detects it. The first
real records will show whether that happens, and designing the check before then would
repeat the mistake this ADR is about.

Consequences: `scripts/validate.py` `pick_stats` gated on contest and documented;
`SPEC.md` §7.7 restated with what counts toward the threshold; `query/runbook.md` Step 7.2
gains the log-everything paragraph. `SPEC.md` §7.9 is unchanged — the record shape was
correct as specified. No session is re-routed, no type file is touched, no ledger record is
written, `registry_version` unchanged.

## ADR-027 · 2026-08-19 · The repo is the source; an app consumes a generated bundle, and eval/golden is the contract between them

An app routes the same library through three model calls and vendors its own copy
of the registry under `docs/ai-instructions/image-library/`. Comparing that
pipeline against this repo found seven divergences, and all seven are one thing:
**a copy of the law shaped by hand at vendoring time, which nothing compares back
to the source.** Owner decision: the repo stays the source, the copy becomes a
generated artifact, and the two harnesses prove they agree rather than assume it.

**The routing surface ships WHOLE, and this is the reversal worth stating.** The
app's vendored index carried twelve fields against the real index's twenty. The
four that matter are `status`, `requires_pair`, `avoid_adjacent` and
`generation_mode` — between them they decide whether a routed SET is legal at
all, so a Call 1 that cannot see them emits pages that are legal slot by slot and
broken as a page, which is the exact defect class §7.3's cross-slot rules exist to
prevent. What the reduction bought was measured before it was removed:
`registry/index.yaml` is **17,350 characters**. It is already the slim view —
invariant 2 exists so routing never opens a type file — and slimming the slim view
saved nothing worth four cross-slot rules.

**Generated, not copied.** `scripts/build-app-bundle.py` writes `dist/app-bundle/`:
32 files, 474 KB, grouped by the call that reads them, plus `MANIFEST.json`
carrying the source commit and a sha256 per file. Two checks guard it from
opposite sides and neither can drift into agreeing with the other while both are
wrong — the script's own `--check` verifies COMPOSITION (every file the repo
should ship is present and matches), and `validate.py` verifies FRESHNESS by
re-hashing every source path the manifest names, warning on a normal run and
failing under `--check`. The bundle also closes the missing-input gap: the app's
Call 2 did not carry `registry/argument-faults.md`, which ADR-014 requires be read
before the first prompt of any new type.

**`eval/golden` becomes the conformance contract, because it finally runs.** SPEC
§9 has called those fixtures routing regression fixtures since they were written
and nothing ever read them — `check_json_files` proved the JSON parsed, and
`expected-routes.yaml` had never been opened by any code. Fourteen slot assertions,
inert. `check_golden` now runs Stage 1 against them: role × channel from
`slot-rules.md`, the type's own channel declaration, active status, and the
deterministic attribute gates. Stage 2 is judgement and is deliberately not
asserted. Any second harness that derives the same shortlist for those fourteen
slots is conformant, whatever it stores internally — which is what makes this a
contract rather than a copy discipline.

**The gates are parsed from the table that documents them.** The effect cell
already says `` drop `<type>` `` in plain text. Restating four kill-rules in Python
would have created the same defect the check exists to catch, one level down.

**It found two stale contracts on its first run, both the same event.**
fixture-001 asserted `06-relief-scene` legal at `outcome-1` on landing-page and
fixture-002 asserted `02-symptom-rail` at `story-0-problem` on advertorial; both
types were trimmed off those columns on 2026-08-11 with the reasoning recorded in
`slot-rules.md`, and the fixtures' own headers require an intended change to update
them in the SAME commit. Eight days passed. Both are now corrected to what current
law derives, with the supersession written into the fixture rather than silently
rewritten — and both turn out to be one-type-once conflicts on a single-type cell,
resolved at rung 4 of the Step 4 ladder.

**`content.json` gains what it could not carry.** SPEC §1 says the QUERY input IS
`content.json`, and it was not true: page 73's prompts name an air pump, an
inflatable bladder, a pressure sensor board and a backlight panel, all read from
the export's `rawFeatures` and `specification`, neither of which had a home in the
schema. That page could not reproduce its own prompts from its own contract. The
schema gains `product.specification` and `product.raw_features`, and page 73 is
backfilled. Only those two of the app's ten context fields are added: the other
four that images never use — `offerMechanics`, `brandContext`, `targetLanguage`,
`productType` — stay copy material and out of the image contract.

**Two divergences are left open on purpose, because they are the app's to answer.**
The app infers `role` and never emits it, so the single most consequential routing
input has no auditable value — the fix is for the app to emit `content.json` as an
intermediate artifact, at which point this repo's validator checks the app's output
for free. And the app pads galleries with virtual slots "to meet a floor" that
exists nowhere in SPEC; §7.4's never-empty rule is about options per slot, not slots
per page. Both are recorded here rather than guessed at.

Consequences: `scripts/build-app-bundle.py` and `dist/app-bundle/` are new;
`scripts/validate.py` gains `check_golden`, `parse_attribute_gates`,
`check_app_bundle`, and `check_slot_rules` now returns the shortlist it was already
parsing; `mapping/content.schema.json` gains two product fields;
`eval/golden/fixture-001` and `-002` corrected; `SPEC.md` §1 invariant 6 and §9;
`CLAUDE.md` hard rule 1. `registry_version` unchanged — no type structure moves.

## ADR-028 · 2026-08-19 · The motion brief is four fields, and the plate is generated rather than drawn

Owner instruction: the plate carries a filename that includes the gif type, a duration, a
ratio, and one brief describing what the loop has in it and what moves. Four fields. The
five-line `GIF SLOT` / `SHOT` / `ACTION` / `RESULT` / `MATCH` card is retired.

**The quartet's real defect was not its length — it had no field for the setting.** Page 73
shipped a brief whose `MATCH` line read "same room and light as still" over a still that is
a see-through technical render standing on a plain deep slate ground, explicitly not
photography. There is no room. Two of its other three lines are also unsatisfiable by that
frame: `SHOT` says "side on" where the still puts the monitor three-quarters on to the
camera, and `ACTION` says "hands stay away" in a frame that never had hands in it. One of
that page's two loops, found by reading each line against its own still after the fact.

The mechanism is worth stating because it explains why a careful writer produced it. With no
field for WHERE, the setting had nowhere to go but `MATCH`, and `MATCH` then filled with
boilerplate — "same room and light as still" is the sentence you write when the field is
asking you a question the image has not made you answer. A prose brief that must name what
is in frame, where it is, what moves and the register to match cannot be filled in without
looking at the still. The G12 satisfiability rule did not change; the field list is what
makes it checkable.

**Cutting `RESULT`, `MATCH` and the negatives loses nothing, because the folder card already
carries them.** `gifs-library/<type>/README.md` is generated from the type file and holds
the type's NEGATIVE list, its declared duration and beat band, its channels, which half of
the motion floor it serves, and the filing convention. An editor browsing the folder meets
all of it. The plate only ever needed what is specific to THIS slot, which is the same
principle `registry/gif-instruction.md` already applies to the type files: law stated once,
never restated.

**The owner's own spec settles the question the plate had been avoiding.** A prose brief
means wrapped lines, and a wrapped line is the single failure the old G12 had actually
measured — one render broke the block's alignment, which is where the seven-word ceiling
came from. So the four fields are not compatible with a plate an image model draws. They are
compatible with one that is typeset, and `scripts/gen-plate.py` writes it: SVG, stdlib, no
generation call, drawn at the slot's ratio so the card is the shape of the deliverable.

This is also the more consistent position. `registry/index.yaml` is generated, the GIF
library's folder cards are generated, and `gif-instruction.md` already says in its own words
that a card is a view and hand-editing one is the same error as hand-editing the index. The
plate was the last card in the system still being drawn by a model, and it was being drawn
by the one tool in the pipeline that is worst at text — the repo has the receipts: a render
that returned `**GIF SLOT · 2s · seamless loop**` with its asterisks intact, and a seven-word
cap that existed for no other reason.

**The filename carries the argument.** `{page}-{seq}-{gif-type}-{slot-slug}.mp4`. ADR-023
gave the page-side name the slot and the page, deliberately, because a page numbers by page
and an editor tracks by slot; what it did not carry was what the loop ARGUES. An inset loop
inside `06-relief-hero --recall` does `pain` work and used to arrive called relief-hero,
which is the wrong word for the one person who has to file it. The library name
(`{type}_{product-slug}_{seq}`) is still issued separately when the finished loop is filed
back, and the ledger still maps the two through the sha256.

**The ratio is the SLOT's, not the still type's.** On `whole-frame` the loop IS the delivered
image, so it owes the page's shape. Where the routed still renders at a different ratio and
the layout crops it — `03-mechanism-ghostbody` at 1:1 into a 16:9 slot on page 77 — the loop
still owes 16:9, because nothing crops it on the way in. Until now nothing in the gif block
said what shape to deliver at all: page 73 carried two loops replacing stills at 1:1 and 3:4
and named neither.

**Retired with the model-drawn plate, and recorded rather than deleted:** the seven-word line
cap, the plain-words rule against markup, the corner and footprint inheritance, the
one-third-to-one-half size band, and the name-where-it-stops clause. Each was earned by a
render and each is a property of a renderer no longer involved. They are in `git log` for the
day a model draws reliable lettering.

**`form: inset` changes with it.** The host type's own prompt now reserves its legislated
layer as a flat empty block carrying no text, and the plate travels beside the still as its
own file. ADR-019 required the work order to reach the editor rather than sit in a document
nobody opens; a file named after the slot, in the render folder next to the frame it
describes, satisfies that without putting model-drawn lettering into a frame G6 bans text
from. No routed page carries an inset loop, so nothing is regenerated by this clause.

**Earlier sessions stand unmigrated.** Pages 13, 37, 58, 65 and 73 keep their five-line plate
prompts, the treatment ADR-024 gave page 13 and ADR-019 gave ADR-018: the correction stays
legible rather than being applied backwards over work that was correct under the law of its
time. `gen-plate.py` skips them by construction and says so on every run, because the first
version did not and wrote SVG into filenames claiming to be renders. Page 73's defective
brief is a separate item and is NOT fixed here — it needs a re-brief against its own still,
not a format change.

Consequences: `registry/rules.md` G12 rewritten; `query/runbook.md` Step 5c rewritten and
Step 5d's library-pointers paragraph updated; `query/output.schema.json` gains `ratio` and
`brief` on the gif block and drops `shot`, `action`, `result`, `match` and `prompt`;
`registry/gif-instruction.md` gains the page-side naming rule; all six files in
`registry/gif-types/` have their BRIEF section rewritten and go to 1.1;
`scripts/gen-plate.py` is new; `CLAUDE.md` lists it among the generated views. Page 77 is
rebuilt in the new form and is the only session that moves. `registry_version` unchanged —
no image structure moves.

## ADR-029 · 2026-08-20 · The brief is two sentences, and the routing argument is not one of them

ADR-028 shipped the brief as one prose paragraph the day before. The owner read the first
two it produced and said they were long and hard to understand. Both halves of that are
right and they have different causes, which is why the fix is not simply "shorter".

**Four lengths were written out on ONE loop and the owner picked.** Same loop, same content,
only the writing changed — page 77's `cause` verdict, put in Vietnamese so the owner could
compare them as a reader rather than as a spec. Measured: one sentence at 17 words, two
sentences at 38, three labelled lines at 52, the shipped paragraph at 113. The English
paragraph it was translated from ran 106. The owner chose **two sentences**.

**The shape: sentence one is the FRAME, sentence two is the MOTION.** What is in it, where
that is, and the light and register it owes the still; then what moves, in the order it
moves. Band 25 to 55 words, checked by the build.

**One adjustment inside the owner's choice, made rather than asked about.** The two-sentence
option was offered with its cost stated — it had no room for the register, so an editor would
have to infer the light from the still. Putting the light into sentence one costs about four
words and keeps the sentence count, so the cost is not paid. A brief that ignores the still's
grade and light reads as pasted in, which ADR-023 recorded before any loop existed, and it
was not worth losing to save four words.

**The second finding, which no length would have fixed.** Prose invites the writer to explain
themselves, and page 77's first brief did: it closed on "The product is absent and not
implied; this indicts the objects." That is a sentence for the router. An editor holding a
camera cannot act on it, and `gif.reason` already carries it for the reader who wants it.
The rule now says so in G12, in Step 5c and in the schema, because the paragraph form drifted
there within one page of shipping and two sentences will drift there just as fast if nothing
names it.

**Why not the three labelled lines, which measured as the most readable.** They were 52 words
against 38 and they read faster, because the eye jumps to the label it wants. The owner chose
otherwise and the choice is theirs to make; recorded here so the option is not re-derived
from scratch the next time someone finds a brief hard to scan. Its real advantage was
structural rather than typographic — a missing field in a labelled block is visible, and a
missing clause in a sentence is not. That check now lives in the build instead: word band,
sentence count, and the six per-type BRIEF sections saying what each sentence must name.

**Effect, measured on page 77:** 106 words to 52 and 98 to 50, a 50% and a 48% cut, with the
frame, the place, the light and the motion all still named. Nothing else about the plate
moves — the four fields, the generated SVG, the filename carrying the gif type and the
slot's ratio are all ADR-028 and unchanged.

Earlier sessions still stand unmigrated for the reason ADR-028 gave. Page 73's defective
brief is still a separate item and is still not fixed here.

Consequences: `registry/rules.md` G12's field block and one paragraph; `query/runbook.md`
Step 5c; `query/output.schema.json` `gif.brief` description; all six `registry/gif-types/`
BRIEF sections rewritten to say what each of the two sentences must name, and each type to
1.2; page 77's two briefs rewritten and its plates regenerated; the build gains a sentence
count and a word band. `registry_version` unchanged.

## ADR-030 · 2026-08-20 · The brief names who, what and what they are doing — and nothing about light

Owner instruction, on reading the two-sentence briefs ADR-029 shipped: drop the light, the
brief describes who or what is in frame and what they are doing. Also: show it working on a
loop with several scenes.

**This supersedes a judgement call I made inside the owner's own choice.** ADR-029 offered
two sentences with its cost stated — no room for the register — and then paid four words to
keep the light in sentence one anyway, on the grounds that a loop ignoring the still's grade
reads as pasted in. The owner has reversed that, and the reversal is better than the reason
I gave for it: the still the loop accompanies sits in the same render folder and carries the
light, the grade and the register in full. Restating them in the brief buys nothing and it
is exactly what produced the page 73 fault — a boilerplate "same room and light as still"
line over a see-through render standing on a plain slate ground. **Removing the field removes
that fault class by construction**, which is the same move `_staging/` makes as a directory
rather than a status field.

So the shape is now: **sentence one names who or what is in frame and where it is; sentence
two names what they are doing, in the order it happens.** Band unchanged at 25 to 55 words.
Enforced rather than trusted — the build fails a brief containing any of eighteen register
words, and the check was mutation-tested by putting the old daylight clause and a grade
clause back.

**A multi-scene loop needs no second format, and that is measured rather than assumed.** The
question is real: `use` declares beats [1, 4] and a three-step sequence was already routed on
page 73. Written out at one, two, three and four beats, the beats run inside sentence two in
order, separated by commas with a final `then`, and the two sentences came to 43, 37, 42 and
40 words in English — every one inside the band, with the four-beat case the shortest but one.

**Four is the ceiling any routed slot can reach.** `use` is [1, 4]; `proof` is [2, 3]; `cause`,
`mechanism` and `relief` are all [1, 2]. `unboxing` alone goes to [3, 6] and it is
`kind: null` and `paid-social` only, so it never reaches a routed page slot and never writes
a page brief at all. The band was therefore set from the routable types, and that is now
recorded in `unboxing`'s own BRIEF section so nobody re-derives it from the wider number.

**Effect on page 77:** 52 words to 49 and 50 to 43. Small, because ADR-029 had already done
the large cut; the value here is not length but that a whole class of unsatisfiable claim can
no longer be written.

Earlier sessions still stand unmigrated. Page 73's defective brief is still a separate item —
and worth noting that under this rule the sentence that made it defective is now unwritable.

Consequences: `registry/rules.md` G12's field block and two paragraphs; `query/runbook.md`
Step 5c; `query/output.schema.json` `gif.brief` description; all six `registry/gif-types/`
BRIEF sections, each to 1.3, with the multi-beat rule landing in `use` and the beat ceiling
recorded in `unboxing`; page 77's two briefs and their plates; the build gains a register-word
check. `registry_version` unchanged.

## ADR-031 · 2026-08-20 · The brief is a shot description in plain words, and an object does not move on its own

The owner asked for something more practical and, instead of a rule, wrote two briefs. That
was the clearer instruction, and three things separate them from what ADR-030 had shipped.

**There is a person in the shot.** Both examples open on someone — a driver using an old
cushion, a person sitting on the new one. The briefs they replaced opened on "the driver's
seat from the open door" and "one continuous frame and no panels": an object study and a
layout note.

**Everyday words.** "Khe hở lưng" and "đàn hồi lại độ dày ban đầu" — the gap behind the back,
springs back to its original thickness. What shipped said "the front lip of the base", "the
seat-corner crack", "the slow-rebound contour rises back to full depth". Those are this
repo's own vocabulary, correct and unreadable, a type file talking to itself. The editor is
the reader and the test is whether you could say it out loud to someone about to shoot it.

**The upshot is back**, and it is not the thing ADR-029 banned. "Lâu dài sẽ gây đau lưng" —
sitting in that gap day after day is what starts the ache — is the point of the shot, and an
editor frames for it. What ADR-029 threw out was the ROUTING argument: "the declared reason
this section exists is temporal, so the slot earns a loop", or page 77's own draft closing on
"this indicts the objects". That is why the pipeline picked the slot, it lives in
`gif.reason`, and no editor opens it. The line is thin and it is now drawn in G12, in Step 5c
and in the schema rather than left to judgement.

**Putting the person in surfaced a defect in a verdict I wrote two days ago.** Page 77's
`cause` loop was filed `rung: natural` — the still is `01-pain-scene` in its object-only
execution, so the loop was briefed as objects on an empty seat. **A pad does not creep forward
across an empty seat.** It creeps because a body is on it and the car brakes. The rung-1
staging was not merely thin, it was not buildable, and nothing in the pipeline noticed because
every check asked whether the brief matched the still and none asked whether the loop could
exist. The gif library's own `cause` type says it in its PURPOSE line — "a pad creeping
forward under a body" — and the brief had dropped the body.

So the verdict moves to `rung: re-execution` and `gif.reason` names the move. **Name the
force** is now a rule in G12: an object does not move on its own, and where the loop needs a
person the routed still does not have, that is rung 2 and it is declared.

**Both of page 77's loops are now rung-2 re-executions and rung 1 delivers nothing on that
page.** ADR-024 found rung 2 "closer to a default than a backup" from the coverage side; this
is the same finding from the buildability side, and it is the strongest case so far. Both
slots earn motion on the argument. Neither can be built from the still as routed —
`features.items.2`'s still is a three-panel locked comparison and panels are inspected rather
than watched; `problems.items.0`'s still has nobody in it.

**ADR-029's two-sentence count is dropped.** The owner's examples are single flowing
descriptions and the count was never the thing that made them readable. The 25-55 word band
stays, the ban on light and register (ADR-030) stays with its eighteen-word check, and the
multi-beat rule (ADR-030) is unchanged: beats in order inside the description, at most four,
which is the ceiling any routed slot can reach.

Consequences: `registry/rules.md` G12's field block and five paragraphs; `query/runbook.md`
Step 5c; `query/output.schema.json` `gif.brief` description; all six `registry/gif-types/`
BRIEF sections to 1.4, with **Name the force** landing in `cause`; page 77's two briefs, its
`cause` rung and reason, its `proof` reason and its motion notes; the build drops the
sentence-count check. `registry_version` unchanged. Earlier sessions still stand unmigrated,
and page 73's defective brief is still a separate item.

## ADR-032 · 2026-08-20 · The motion floor had no margin, and three mechanisms give it one

Owner's brief: a landing page carries at least two GIFs, and the suggested spots need backup
options for when a given loop cannot be made. Page 77 carried exactly two, so the question
was what happens when one of them fails.

**The finding is worse than the question.** Measured across every page routed under the
unamended spacing rule — 58, 65, 73 and page 77's first routing — loop-capable sections came
to exactly **2** and delivered loops came to exactly **2**, on all four. The floor is not a
target these pages aim at, it is their structural ceiling. An advertorial of hero + problems
+ features + reviews has its hero refused (recognition, a held state, consistent across four
pages) and its review wall barred (the six-type set carries no `social` type), which leaves
two sections, and one loop per section leaves two loops. **Margin was zero everywhere, and
nothing said so.** Pages 13, 31 and 37 show 5, 5 and 4 delivered against 8, 2 and 1
loop-capable sections — they predate ADR-024 and are the fairground it was written against.

So "route a backup loop" was not available: there was nowhere to put it. Three mechanisms
were proposed and the owner took all three. They interact, and the interaction is the part
worth recording.

**1. The spacing rule is relaxed, and this amends ADR-024.** At most one loop per section,
plus ONE more where the section carries five items or more and the two are not adjacent.
ADR-024 set one-per-section against a measured case — page 31 drafted four moving tiles
inside one feature list — and two loops with a static item between them in a list of five is
not that image. The not-adjacent clause is what stops it becoming one. Note the direction of
travel: ADR-024 also DROPPED a never-adjacent clause, but that one governed slots across a
section boundary, where a heading and a block of copy sit between them. Inside one list there
is nothing between them, so adjacency binds here and only here.

**2. Every delivered loop carries `gif.alt`**, a second way to shoot the same argument in the
same slot, in the same format and band as the brief. It drops whatever the primary is most
likely to be blocked on — an actor, a moving car, an interior — and keeps the claim. It is
printed on the plate under the primary beneath an `IF THAT CANNOT BE SHOT` rule, so the
editor holds both without opening a file, which is the same reasoning ADR-019 applied to the
work order itself.

**3. `motion.reserves` lists the slots that lost to the budget.** A reserve is a slot that
earned motion on the argument, was refused by spacing or ceiling, and could legally replace a
named primary in its own section. It REPLACES; it never adds, so promoting one leaves the
spacing rule satisfied.

**Mechanisms 1 and 3 compete for the same slots, and on a maximised page 3 wins.** Once a
section is carrying the two loops the relaxed rule allows, there is no slot left that could
legally substitute — which is why page 77 emits `reserves: []` and says so in
`motion.notes` rather than leaving an empty field to be read as an oversight. The reserve
list is for pages that do not maximise; `gif.alt` is the cover that always exists.

**Page 77 re-routed from two loops to three, and the arrangement is forced rather than
chosen.** Among the `features` list's loop-capable slots — items.1, items.2 and items.3 —
the only non-adjacent pair is items.1 with items.3. items.0 is refused on its own grounds (two
technical panels are inspected, not watched) and items.4 carries no image. So items.1 takes a
`proof` loop and items.3 takes a `relief` one, and **items.2 loses the loop it held in the
first routing** with its argument entirely intact: slow-rebound foam recovering is a state
changing that its three-panel still cannot show. It cannot even serve as a reserve, because it
sits BETWEEN the two delivered loops and promoting it would put two side by side.

**features.items.3 is the first slot in this library to meet the `relief` type's tightest rule
head on** — motion earned only where the motion IS the thing the problem used to block.
Standing straight up out of a car seat after a long drive is exactly what the ache took away.
ADR-023 recorded that rule as explicitly untested and it has stayed untested since; this is
its first real case, and the first `relief` loop the library has ever routed.

Margin is now a field: `motion.margin`, delivered minus floor, emitted on every page. Page 77
reads 1 — losing any one loop still leaves it at the floor.

Six checks, all mutation-tested: two loops adjacent inside a section, a second loop in a
section shorter than five items, a delivered loop with no alternate, an alternate that repeats
the brief, an alternate carrying a register word, and `motion.margin` disagreeing with the
count. The first two had to be tested in-process, because the obvious source mutation changed
a filename rather than a position and passed while proving nothing.

Consequences: `query/runbook.md` Step 5d's spacing, reserve, alternate and margin rules, and
the adjacency paragraph reconciled with ADR-024; `query/output.schema.json` gains `gif.alt`,
`motion.margin` and `motion.reserves`; `scripts/gen-plate.py` draws the alternate under the
primary; page 77 re-routed to three loops with three alternates, its plates regenerated and
its motion notes rewritten. Earlier sessions still stand unmigrated and are all at margin 0,
which is now a stated fact about them rather than an invisible one. `registry_version`
unchanged.

## ADR-033 · 2026-08-20 · The first inset loop, and the two rules ADR-028 and ADR-032 left behind it

The owner asked for a page whose prompts.md uses a gif INSET. Every loop the library had
routed until now was `whole-frame`, and pages 77 and 97 both recorded the same reason in
`motion.notes`: no type at a slot that earned motion legislated a layer a loop could occupy.
Page 104 is the first where one does, and routing it surfaced two pieces of law that were
written for whole-frame and quietly wrong for inset.

**Defect 1: `06-relief-hero`'s own `--loop` block still described the pre-ADR-028 plate.** It
said the render "owes a legible work order sitting in the layer's own footprint" and that
"the plate's lettering is settled at 20 of 20 lines exact". ADR-028 made the plate a
generated file two days earlier and took the lettering out of the frame entirely, and this
block was not updated with it. Nothing caught it because no page had routed `--loop` since,
which is the honest reason a stale rule survives: it is only load-bearing the day someone
uses it. Corrected at 1.16 — the layer is reserved as a flat empty block of one flat tone,
carrying no text, and the plate travels beside the still.

**Defect 2: `gif.ratio` was defined for a form that is not the only form.** ADR-032 wrote it
flatly — the slot's declared ratio, because on whole-frame the loop IS the delivered image
and owes the page's shape. An inset loop fills a panel INSIDE the frame, so the page's aspect
is the one thing it does not owe. `06-relief-hero` draws `--detail` as a rounded rectangle or
circle at 15-25% of frame width, which is square, so a `--detail` loop delivers 1:1 whatever
the slot is. The rule now branches on form and the build fails an inset loop that carries the
slot's own ratio — the specific mistake of confusing the layer with the frame.

**The new risk, named rather than removed.** Under the old plate rule a render carrying one
took the `--brief` suffix and never the slot's asset filename, because a frame covered in
lettering is one no page can use by accident. A reserved layer is a flat empty grey block,
and that CAN ship unnoticed as a design choice. So the host render keeps the slot's own asset
filename — it is the frame the loop lands in — and the option that emits it says on its own
face that it is unfinished until the loop is dropped in. The build fails an
`inset_motion: loop` option whose prompt does not reserve the layer as an empty block, and
fails one that carries no such note.

**Why this slot, and why it is not a stretch.** `features.items.1` claims the textured base
held its ground against smooth leather when he braked at highway speeds. Holding against a
force is temporal and no static frame carries it. `--detail`'s stated trigger is a feature
too small to read at scene scale, which the grip pattern is; `--loop` is legal on every
`inset_mode` except `--none` and requires the layer's content to be TEMPORAL, which a
magnified mechanism under load is. Nothing is restaged, so it is rung 1 — the first rung-1
loop on a page since page 97's how-to, and the first inset one anywhere.

**Page 104 also routes four slots with a single option each**, which is worth recording
because it looks like under-delivery and is not. SPEC §7.4 asks for three where three legal
possibilities exist and bars padding with rerolls where they do not:
`features.items.0` (the mechanism cell holds one legal type here and it has no axes),
`features.items.2` (the VARIANT SELECTION RULE fixes the variant, and a second execution of
the same seat on the same day is a reroll), `features.items.3` (the outcome cell's other type
is spent and this type's only axis has one legal value, the other being banned outright), and
the four review tiles (ADR-022). Each says so in its own `recommendation_basis`.

Page 104 is the same product as page 77 on a different template and a different narrator —
29 of 192 content keys match and all of them are boilerplate. It was routed on its own copy
rather than cloned, and the pages diverge at four slots. `imageBriefs` is null on this export,
so `htmlCompiled` was the only slot source, which is the case earlier pages established it can
carry.

Consequences: `registry/types/06-relief-hero.md` `inset_motion: --loop` rewritten, to 1.16;
`registry/rules.md` G12 gains the form-dependent ratio rule and the unshippable-host rule;
`query/runbook.md` Step 5c the same; `query/output.schema.json` `gif.ratio` description;
`query/sessions/104-…` is new. Five checks mutation-tested in-process, 5 of 5 fired.
`registry_version` unchanged.

## ADR-034 · 2026-08-21 · Session directories are {page-type}-{product-slug}-v{NN}, and the slug comes from a closed list

Session directory names had no format. The owner asked for one that makes the product clear,
carries a number, and names the page type, and said explicitly not to bother with the page
title. Auditing the nine existing names first turned up four things, one of which is a data
defect rather than a naming one.

**The page 13 session has no page id.** Its `prompts.json` records
`"page_id": "13-inch-portable-wall-mounted-air-cooler-cool-your-space"` — the source HANDLE
written into the id field. The `13` at the front of the directory was never an id either; it
is the `13-inch` of the product name, which happens to look like one. No handle among the 62
source exports matches it, so the real id is unrecovered. This is why the directory could not
simply be renamed from its own data.

**Sorting was already broken.** `104` sorts before `13`, and with ids running to three digits
it only gets worse. **The product was invisible in four of nine names** —
`58-how-i-rescued-trapped-family-dvds` never says it is a USB optical drive. And **four of the
nine sessions were the same product** with nothing grouping them.

**The scale is what decided the field order.** Measured across the source exports: 62 files,
11 products, and the ergonomic seat cushion alone has **27 pages**. The massage comb has 10
and the optical drive 9. A name whose first sort key is anything but the product scatters 27
siblings across the directory, and seeing a product's pages together is the reuse question
ADR-023 built the library around — one asset serves every clone of a product.

**Two corrections from the owner, both taken.** First, I argued against putting page type
first partly because it holds two values across the catalogue; the owner corrected that — the
source system has more page types and the library simply has not met them yet, so the field
carries real information and my cardinality argument was about a snapshot rather than the
system. Second, the number: I recommended the source `pageId` because it is the join key back
to the export; the owner chose a **self-assigned version**, and that choice solves something
`pageId` could not — page 13 has no id and still gets a name. The `pageId` is not lost; it
stays in `prompts.json.page_id`, which is where a join key belongs.

**The version is placed at the END rather than the middle, and that is my call rather than the
owner's.** Their sketch read `[page-type]-[version]-[product]`; with the version in the middle,
every product's `v01` sorts together and the 27 cushion pages break into 27 version groups —
the exact scatter the convention exists to stop. At the end it groups, and it matches the
owner's own first sketch, which put the product before the variant. It is one command to swap
back.

**Version semantics, stated because an unstated one is ambiguous the first time two pages
compete for it:** the Nth page routed for that PRODUCT, counted across all page types,
assigned once and never reused. If a page is retired its version is retired with it. Within a
product group the sequence is then readable from the listing without anyone maintaining it.

**The slug comes from `query/product-slugs.yaml`, a closed list, and not from the product
name.** The evidence is already in the repo: page 73's `content.json` calls the product
"Automatic Upper Arm Blood Pressure Monitor" while its source export calls it "Hospital Grade
Blood Pressure Monitor CE MDR Approved". A derived slug gives one product two slugs and breaks
the grouping the whole convention exists to create, so the file maps one slug to every name
that means it. Adding a name is cheap; adding a SLUG is a decision, because it claims two
pages are not the same product.

**Renaming had one consequence nothing would have caught.** `scripts/validate.py` hardcoded
`"37-how-one-l-shaped-cushion-ended-my-sitting-pain-ergonomic-support"` in
`GRANDFATHERED_MULTIPASS`. Renaming that session without updating the constant would have
silently un-grandfathered it and turned three warnings into three errors. `decisions/log.md`
also names a session path, and it is left alone: the log is append-only and that reference is
historical.

`check_session_names` enforces the format, the closed slug list, the uniqueness of
(product, version), and the match between a directory's slug and its own `content.json`
product name. It also warns where a `page_id` is not a number, which is how the page 13 defect
stays visible instead of being buried by a tidy new name. Four checks, mutation-tested against
throwaway directories, 4 of 4 fired.

**Written while another session was editing the same file.** `scripts/validate.py` in the
working tree carried both lanes' work — this ADR's `check_session_names` and another lane's
in-progress content-contract checker, which was surfacing 23 pre-existing defects in the older
sessions. Only this lane's hunks are in this commit; the other lane's functions,
`mapping/content.schema.json` and the app bundle are left untouched and unstaged. That is the
parallel-session discipline the repo already assumes, applied to a file rather than a
directory.

Consequences: nine directories renamed under `query/sessions/`; `query/product-slugs.yaml` is
new; `scripts/validate.py` gains `check_session_names` and has its grandfather key corrected.
No session content changes, no prompt moves, `registry_version` unchanged. Page 13 keeps its
handle-shaped `page_id` until the owner supplies the real one.

## ADR-035 · 2026-08-21 · The QUERY input contract is enforced, and enforcing it found the contract wrong

SPEC §1 says the QUERY operation's input IS a `content.json` valid against
`mapping/content.schema.json`, and `query/runbook.md` Step 1 opens by telling a session to
check it. Nothing ever did. `check_json_files` proved the schema file itself parsed;
`check_golden` opened the two fixtures' `content.json` but only to read `page.channel` and
`product.attributes` off them, so a malformed fixture would have raised a `KeyError` rather
than produced an error message. A routed session's own contract had never been opened by any
code at all. That is the state `expected-routes.yaml` sat in for eight days before ADR-027 —
named as a contract, inert in fact, and reported as green.

**Run once, it failed six of the eight sessions that have a `content.json`, every one on the
same line, and the line is the contract's fault.** All six carry
`product.reference_photos: []` and the schema declared `minItems: 1`. The empty array is not a
lapse — it is what ADR-021 and Step 5 require. An export carrying `imageBriefs: null` supplies
no product photograph, there is nothing to hash, and SPEC §6.4 forbids inventing one; the
prompts keep their G1 reference block and the owner attaches the photo by hand in the
generation tool. So the schema was demanding the one thing the rest of the repo forbids, and
the only two documents that satisfied it were the golden fixtures, which pass because they
carry a placeholder hash of sixteen zeros.

`minItems` moves to `0`, with the reason written into the field's own description so the next
reader meets it there rather than deriving it from a log entry. The item pattern is untouched
and still binds — `["not-a-hash"]` is caught, `[]` is not — and both were tested, because
relaxing a bound is the easiest way to disable the rule underneath it by accident.

**Three sessions predate the contract and are warned rather than failed.**
`listicle-air-cooler-wall-mounted-v01` carries no `content.json` at all;
`advertorial-seat-cushion-l-shaped-v01`'s file is the raw Shopify export saved under that
name (22 violations, no `product` key); `advertorial-optical-drive-7in1-v01`'s is an earlier
hand-rolled shape (103 violations). Failing them would hold the repo at non-zero errors for
every parallel lane, to punish work that was correct under the law of its time — the treatment
ADR-024 gave page 13 and ADR-028 gave the five pre-plate sessions. A legacy session reports one
summary line rather than its full list: 103 violations out of one file would drown the live
ones.

**An unknown schema keyword is an error, not a skip.** The validator implements the nine
keywords the schema actually uses, measured from the file rather than assumed: `type`,
`properties`, `required`, `additionalProperties`, `items`, `enum`, `minItems`, `minLength`,
`pattern`. A schema that grows a tenth — a `oneOf`, an `anyOf`, a `$ref` — makes the checker
say so and stop, rather than validate the parts it recognises and report green. `jsonschema`
is not a dependency this repo carries, and the subset is small enough that implementing it
costs less than adding one. The bool case earns its own line: `True` is an `int` in Python, so
a naive `isinstance` admits `true` for `type: integer`. JSON keeps them apart and so does this.

**Mutation-tested before it was trusted: 15 known-bad documents against a hand-built valid
baseline**, built rather than copied from a session so that it inherits no session's own
defects. Caught 15 of 15 — a missing key at the top level and one three levels down, an
undeclared key at both levels, a channel and a role outside their enums, a reference photo that
is not a sha256, a ratio that is not `W:H`, a string where a boolean belongs and a boolean
where a string belongs, an empty string against `minLength`, two empty arrays against
`minItems`, an object where an array belongs, and an image slot missing its `ratio`. A liveness
case asserting the valid baseline is invalid FAILED, as it must: a board on which every line is
green proves nothing until one line is green for a reason.

**The parallel-lane collision, recorded because it produced a rule.** ADR-034 landed in another
session while this one was being written, renaming all nine session directories. This ADR's
`PRE_CONTRACT_SESSIONS` was keyed on the old names and uncommitted in the same working tree, so
it was invisible to ADR-034's audit — which had caught the identical hazard in
`GRANDFATHERED_MULTIPASS` and fixed it by hand. The tree went from 0 errors to 23 in the
seconds between the rename and the next validator run, and the three sessions the set exists to
protect began erroring for a reason that had nothing to do with them.

So `check_grandfather_sets` makes it loud: a name in either set that is not a live session
directory is an error. **A set that protects nothing is as wrong as one that protects too much,
and only one of the two announces itself.** Mutation-tested 6 of 6, including today's exact
failure (the pre-contract set left on pre-ADR-034 names, 3 errors), the hazard ADR-034 caught
by hand (1 error), one stale name hidden among live ones, and a name matching a file rather
than a directory — plus a liveness case that failed as required.

**What this does not check, deliberately.** Whether a session's `content.json` agrees with its
own `prompts.json` — the slot ids, the ratios and the roles could differ between the two and
both would pass. Page 65's `build.py` checks that for itself, one session at a time. Lifting it
into the validator is real work, and inventing it today against one page's implementation would
repeat the error ADR-026 declined to make.

Consequences: `scripts/validate.py` gains `schema_errors`, `check_content_contracts`,
`check_grandfather_sets`, `PRE_CONTRACT_SESSIONS` and a `content contracts` count in the
summary line; `mapping/content.schema.json` `reference_photos.minItems` 1 → 0 with its
description rewritten; `SPEC.md` §8's check list; `query/runbook.md` Step 1 gains the
enforcement note and the empty-`reference_photos` rule. `dist/app-bundle/` is rebuilt, because
`SPEC.md`, `query/runbook.md` and the schema are all vendored in it (CLAUDE.md hard rule 1).
Errors stay at 0; warnings go 12 → 15, all three additions being the pre-contract sessions now
saying so on every run. No session is re-routed, no type file is touched, `registry_version`
unchanged.

## ADR-036 · 2026-08-21 · A loop's filename is its session's name plus two fields, and it ships as animated WebP

Two questions were open after ADR-034 named the session directories. The owner settled both:
the version goes at the END, and a loop ships as `.webp`.

```
{page-type}-{gif-type}-{product-slug}-v{NN}-{slot}.webp
advertorial-mechanism-seat-cushion-l-shaped-v04-features1.webp
```

**It is the session directory with two fields added, and that is the point.** ADR-034 made a
session `{page-type}-{product-slug}-v{NN}`. Insert the gif type after the page type, append
the slot, and the loop's name falls out. A reader gets what it argues, for which product, on
which page of that product, and which slot it fills, without opening anything — and the build
does not type it. `gif_name()` composes it from constants that are asserted against
`os.path.basename(HERE)`, so the filename and the directory cannot drift apart.

**Version last, because a version is not a number that stands alone.** Under ADR-034 it counts
pages of one PRODUCT, so `v04` of the cushion and `v04` of the comb are unrelated numbers that
happen to match. A field meaningless without its parent belongs beside its parent. Written out
as a library folder listing — where `gif-type` is constant because the folder IS the type —
version-early split one product's three loops across three separate groups and sat two
unrelated `v01`s next to each other; version-last put the product's loops in one block running
v01, v03, v04 in order. The same reasoning applies to the session directory, which already
carries the version last.

**Page type stays, on the owner's call.** I proposed dropping it: under ADR-034's semantics
`product + version` already identifies a page uniquely, so the page type is derivable and was
costing characters. The owner keeps it, and the standing reason is the one they gave for the
directory name — the source system has more page types than the two the library has met, so
the field will discriminate even where it does not yet.

**The slot is what makes the name unique, and it is derived.** Two loops on one page may carry
the same gif type: ADR-032 allows five loops and there are five routable types, so a collision
is legal rather than hypothetical. Without the slot those two produce the same filename. It
comes from the `slot_id` — drop `.image`, drop the container segments `items`, `shots`,
`photos`, join what is left — so `features.items.1.image` becomes `features1` and nobody
invents a label.

**The page id is deliberately absent.** It identifies the source export rather than the loop,
it lives in `prompts.json.page_id` where a join key belongs, and one routed session has none
at all — a naming rule that depended on it could not have named that session. ADR-034 made
the same call for the directory and this follows it.

**Delivery becomes animated WebP, and this completes ADR-023's reasoning rather than
contradicting it.** That ADR ruled `.gif` out with a specific complaint — "a 20 MB `.gif`
costs more conversion than the motion buys" — and settled on mp4/webm. WebP is the modern
answer to exactly that complaint, and it buys the thing this library actually needs: it sits
in an `<img>` where a still already sits. Every gif verdict in this system occupies an IMAGE
slot in a page template. An mp4 needs a `<video>` element with autoplay, muted, playsinline
and loop attributes that the template does not have; a WebP is a src swap. That is what makes
a loop and a still interchangeable, which is the assumption Step 5c has been running on since
ADR-020 without anything guaranteeing it.

It carries no audio track by format, so nothing has to be muted and the `delivery` string
stops saying so. The cost is real and is taken knowingly: WebP runs larger than mp4 at the
same quality, so the size ceiling binds harder than it did. That is the trade for keeping the
slot interchangeable.

**Both names still stand.** ADR-023's library name becomes `{gif-type}_{product-slug}_{seq}
.webp` and the page name is the one above. The new page name happens to be unique across the
whole library, so collapsing the two into one is now possible where it was not before — but
that would retire the ledger's sequence issuance and it is not what was asked, so it stays a
separate decision.

Migrated: the three sessions routed under ADR-028 or later —
`advertorial-seat-cushion-l-shaped-v03`, `-v04` and `listicle-massage-comb-spray-v01`, nine
loops between them, plates regenerated. The pre-ADR-028 sessions keep their old five-line
plates and their old `.mp4` names, the treatment ADR-024 gave page 13.

Four checks mutation-tested in-process, 4 of 4 fired: a stray `.mp4`, a missing slot field, the
version put back in the middle, and a gif type in the name that does not match `type_id`.

Consequences: `registry/rules.md` G12; `query/runbook.md` Step 5c and the delivery paragraph;
`query/output.schema.json` `gif.output` and `gif.delivery`; `registry/gif-instruction.md` §4
naming and delivery; three `build.py` files gain `PAGE_TYPE`/`PRODUCT_SLUG`/`VERSION`,
`slot_slug()` and `gif_name()` with the directory assert, and their nine `gif.output` values
are now computed rather than written. `registry_version` unchanged.

## ADR-037 · 2026-08-21 · A loop has one name, and one loop per gif type per page is what keeps it unique

Owner instruction: no `{seq}` and no `{slot}` in a gif name. Both fields go, and removing them
settles something ADR-036 had left open.

```
{page-type}-{gif-type}-{product-slug}-v{NN}.webp
advertorial-mechanism-seat-cushion-l-shaped-v04.webp
```

**A loop now has ONE name.** ADR-023 gave it two — a page-side name numbered by slot and a
library name numbered by a sequence the ledger issued — because the page tracked by slot and
the library tracked by type. This instruction removes both numbering fields at once, and what
is left is unique on both sides simultaneously. So the second name goes with them, the
sequence issuance goes with it, and `ingestion/gifs.jsonl` records the same string the routing
commissioned. Nothing is mapped through a sha256 any more to know that two references mean one
file. ADR-036 noted the collapse had become possible and left it as a separate decision; this
is that decision, forced by the field removal rather than chosen for tidiness.

**What makes the name unique is now a rule instead of a field: one loop per gif type per
page.** With no slot and no sequence, two loops arguing the same thing on one page would be the
same file. So a page carries at most one `cause`, one `proof`, one `mechanism`, one `relief`,
one `use`. This costs nothing that was in use — all four pages with routed loops already
satisfied it before it was written down — and it states something true anyway: a page making
the same kind of motion argument twice is repeating itself. The build fails a page that breaks
it, and the failure names the collision rather than the rule.

**A latent defect from ADR-036, found while doing this.** That ADR moved delivery to WebP
everywhere it was written in prose, but `scripts/validate.py`'s `GIF_FILE_RE` still read
`{type}_{product-slug}_{seq}\\.(mp4|webm)` — the ledger would have rejected every filename the
new law produces. It fired on nothing because the ledger holds zero records, which is exactly
how a rule that nothing runs stays wrong. The regex is now the single name, and its split is
unambiguous because the gif type is a closed list sitting between two free fields. Tested
against six filenames, 6 of 6 as expected: the two live names accepted with the right type
extracted, and the old library name, a stray `.mp4`, a leftover slot field and an invented gif
type all rejected.

Nine loops renamed across the three sessions routed under ADR-028 or later. Plates
regenerated. The pre-ADR-028 sessions keep their old names, the treatment ADR-024 gave page 13.

Two checks mutation-tested in-process, 2 of 2 fired: two loops sharing a gif type on one page,
and a slot field left in the filename.

Consequences: `registry/rules.md` G12 trades the slot paragraph for the one-per-type rule;
`query/runbook.md` Step 5c the same; `query/output.schema.json` `gif.output`;
`registry/gif-instruction.md` §4 rewritten around a single name and no ledger sequence;
`scripts/validate.py` `GIF_FILE_RE` and the ledger's error message; three `build.py` files drop
`slot_slug()` and gain the duplicate-type check. `registry_version` unchanged.

## ADR-038 · 2026-08-21 · The cutaway gains a bound, a second geometry, and a word for soft tissue

Owner verdict on two `03-mechanism-ghostbody` renders of a scalp-LED comb: *sai logic, sai khoa
học* — the cutaway is cutting into the head when the product only reaches the scalp and the hair
roots. Reading the type file afterwards shows the renders obeyed it exactly.

**The bound was circular, so there was no bound.** `cutaway` said the structure is
`Anatomically accurate` and declared no extent. The `structure` mark's count read **"as much as
the cutaway shows"**. So the cutaway's extent was set by the structure and the structure's
extent was set by the cutaway, and the only thing left standing was an adjective. G10 already
recorded what happens next in its own words — a rule without a sanctioned resolution "is
resolved by the model in whichever direction it likes" — and here the direction is whatever
reads as a medical illustration: deeper and larger. Measured by eye against the renders, the
opened slab is about a quarter of the head's height where a scalp is about three percent of it,
and in both the crown of the skull is removed to make room.

**Depth is derived, never chosen.** Name the layers as a closed list from the surface, ending
one below the deepest structure the product reaches, and draw nothing past it. Scalp LEDs: hair
shaft, epidermis, dermis with the follicle bulbs, stop — the skull never appears. Seat cushion:
skin, subcutaneous, then pelvis, sacrum and lumbar spine, stop. This is the move the repo makes
everywhere else and had not made here: a closed list instead of an open adjective, the same
shape as `vocabulary.yaml`, the six gif types and ADR-016's five ratios.

**The silhouette clause read as permission.** `cutaway` already said the structure is `rendered
INSIDE the body silhouette and never floating on top of it`, and that sentence was written at
1.x to stop the anatomy floating ON TOP of the body. It says nothing about the body's own
outline, and both renders removed the crown of a head while satisfying it. Now stated
separately: the outline stays unbroken and the cutaway is a WINDOW within it, never a bite out
of it.

**Two cut geometries, as a PARAMETER rather than a variant.** SPEC §3.2's ladder decides this:
the argument does not change — the sentence is still "this shape exists for a reason" — only
where the body is opened, which is a runtime value. So it is level 1, it lives in the type file,
and it costs no vocabulary entry, no frontmatter field and no validator change.

- `section` — a plane through the body's volume. For a structure living inside it: spine,
  joint, pelvis, cervical vertebrae. This is what the type did at 2.2 and every render behind
  it.
- `window` — a shallow opening in the surface layers only, no deeper than the last named layer,
  the part's outline intact. For a structure at or just beneath the surface: scalp and follicle,
  skin, nail bed, gum margin.

**And the choice is already made by the time you make it.** Write the layer list first and the
geometry falls out: a stack ending in the dermis cannot be drawn as a plane through a skull.
That is why this is one rule in two halves rather than two rules that can disagree.

**`structure` had no word for soft tissue, and that is why the model invented one.** The mark
is defined as `bone, cartilage, the body's own framework`; `support` is specified as a band
`beside a bone`, and it `sits ON the bone`; every proven render behind this type is skeletal —
cervical vertebrae, metatarsals under a shoe, an insole. A hair follicle in the dermis is none
of those. **The comb is the first product ever routed to this type whose target is not a
skeleton**, so the model had to improvise both the tissue and its depth, and it improvised
toward illustration. `structure` now names soft tissue explicitly, and its count is the closed
layer list rather than the circular clause.

**What this does NOT fix, and it is the larger half.** The same two renders put RED on the
CORRECT panel, because the product's real specification is `6-LED Red Light Therapy`: G8 makes a
visible emission the primary subject and names `light` in its own list, G3 locks red to problem
areas, and this type's `stress` mark is red and left-panel-only. That collision is untouched
here and no legal render of this product exists on this type until it is resolved. It is a
change to a GLOBAL rule and it is left for its own decision rather than folded into a type
patch.

**Evidence, stated with its own limit.** 2 of 16 records for this type, 12% of runs and 2
distinct observations, so SPEC §6.2's ≥2/3-of-runs and ≥3-observations arms are BOTH unmet and
this is not a patch the ledger licensed. The authorisation is the owner's own verdict, which
ADR-007 names as part of the human gate — "render verdicts where the owner gives them". Recorded
this way round so nobody later reads the ledger as having cleared it.

Consequences: `registry/types/03-mechanism-ghostbody.md` `cutaway` gains the depth rule, the
silhouette rule, the two geometries and the continuity rule, `ghost` stops saying `cross-
sectioned at a named plane`, the SKELETON `[CUTAWAY]` line names the layer list and the cut, and
`structure` gains soft tissue and a real count — to 2.3. `registry/argument-faults.md` gains
**A13**, because an extent nobody bounded becoming a claim nobody made is not about anatomy and
recurs wherever a prompt names a thing to reveal without naming where the revealing stops. No
page is re-routed, no other type is touched, `registry_version` unchanged.

## ADR-039 · 2026-08-24 · The multi-pass ban reaches the three files ADR-021 left teaching it

The owner tested the system and it still returned multi-pass. It does not EMIT it — every
page routed after ADR-021 carries zero, and `check_prompt_sets` errors on any that would.
What it still did was TEACH it, in three places ADR-021's own Consequences list never named.

**`query/runbook.md` contradicted itself four steps apart.** Step 3 carries the ban:
"So `generation_mode: multi-pass` is never emitted." Step 6 ended: "and — for
`generation_mode: multi-pass` — expand `steps[]` with the adapter's edit-script template." A
session that read Step 3 and then followed Step 6 was instructed to do both, in one file.

**`adapters/nano-banana.md` Rule 3 was live instruction for the banned thing**, titled
"Multi-pass expansion" and carrying three generate/edit/composite templates. Step 6 pointed
here for them. Rule 6 reinforced it twice more — "do not fight it in one pass, that is exactly
what Rule 3 exists for" for multi-region consistency, and "add layers via edit steps one at a
time" for layered composites. The adapter is the file Step 6 applies at render time, so this
was the closest of the three to a delivered prompt.

**`query/output.schema.json` still declared it legal**, with `pipeline` enumerating
`multi-pass` and `steps` described as "Required when pipeline is multi-pass".

**And the app bundle carried all of it.** `dist/app-bundle` shipped the ban in
`vocabulary.yaml` and `runbook.md` alongside the instruction in `nano-banana.md` and
`output.schema.json` — internally contradictory law, which is what an app consuming the
bundle reads.

**This is ADR-020's failure repeating, and it is worth naming as a pattern rather than as an
incident.** ADR-020 was written because a superseded premise survived in a schema description
and a runbook paragraph after the ADR that killed it. ADR-021 then made the same shape of
mistake: it listed its consequences as Step 3, `vocabulary.yaml` and one session, and never
swept for the other readers. **An ADR's Consequences list is a claim about blast radius, and
nothing checks it.** A grep for the banned term at the time of writing would have found all
three in one command.

**What is fixed.** Step 6 stops expanding anything and says why the line was there. Rule 3 is
retired in place — kept, because one pre-ADR-021 page's `steps[]` are read against its
templates, and marked so nothing new is written against it. Rule 6's two clauses are rewritten
to the single-pass answers the library already records: name the invariants before the regions
for multi-region consistency, which is `01-pain-split`'s own 1-of-1 route, and fix a dropped
layer in the prompt rather than in a second pass. `pipeline` narrows to `single-pass`.

**Stated so it is not over-trusted: narrowing the enum enforces nothing.** No code validates a
`prompts.json` against `output.schema.json` — `check_json_files` only proves the schema itself
parses. The rule is enforced by `check_prompt_sets`, which already errors. The enum change
stops the contract declaring something the pipeline will not do; it does not catch a future
breach.

**Deliberately not touched.** The three type files that declare `generation_mode: multi-pass`
— `04-proof-lockedframe`, `05-social-handoff`, `01-pain-split --mirror` — keep it: it is a true
statement about what the PICTURE needs, `registry/vocabulary.yaml` already carries the pointer
to this ban at the point the field is defined, and those files belong to render-refinement
lanes. The pre-ADR-021 page keeps its three multi-pass options and its grandfathered warning;
the owner's instruction was to fix forward against the newest page and not to edit old sessions
to suit a new rule. `eval/render-tests.jsonl` and this log keep their historical mentions.

Consequences: `query/runbook.md` Step 6; `adapters/nano-banana.md` Rules 3 and 6;
`query/output.schema.json` `pipeline` and `steps` in both `slots` and `recommended`;
`dist/app-bundle` regenerated. No prompt, no session artifact and no script behaviour changes.
`registry_version` unchanged.

## ADR-040 · 2026-08-24 · ADR-016 gets its checker, and the drift that outran two ADRs gets a sweep

Two enforcement gaps, closed together because they are the same shape: a decision was
made, written down, and then nothing read it.

**ADR-016 deferred its own checker and the deferral cost eleven days.** It declared five
legal ratios on 2026-08-13, named the types that were already wrong, and closed with
"adding one would make this enforceable rather than remembered, and it is proposed rather
than done here because the validator is shared and a second session is live." Measured
today: **10 of 15 type entries still declare `4:5`, `5:3` or `3:2`**, and **three delivered
pages emitted an illegal ratio** — one of them page 73, routed six days AFTER the ADR.

`check_ratios` splits the two surfaces on purpose. A **delivered prompt** is the
deliverable, so an illegal ratio there is an ERROR for anything routed from now on; the
three existing offenders are named in `GRANDFATHERED_RATIOS` **with their reasons**, because
a bare name in an exemption set is a decision nobody can audit later. A **type file** only
warns: ADR-016 itself said those are "corrected when it is next opened", the files belong to
render-refinement lanes, and erroring ten types nobody is editing today would block every
lane's ADR-007 autopilot for a rule none of them broke. The new set is registered with
`check_grandfather_sets`, so it cannot rot silently the way ADR-035 records
`PRE_CONTRACT_SESSIONS` doing.

Result: 0 errors, warnings 15 → 28, all thirteen new ones naming ADR-016. Proved against
known-bad before being believed — emptying the grandfather set returns 3 errors on the same
files, and a synthetic type declaring `4:5` warns while one declaring `16:9, 1:1` does not.

**The second gap has no gate, and saying so is the point.** ADR-020 and ADR-039 are the same
failure twice: a decision landed and the files TEACHING the opposite were left standing —
a schema description and a runbook paragraph the first time, `runbook.md` Step 6, the
adapter's Rule 3 and `output.schema.json` the second, three days and eleven ADRs late. An
ADR's Consequences list is a claim about blast radius and nothing verifies it.

A lexical gate would be false comfort. `multi-pass` legitimately appears in 42 tracked files:
this log records it, the render ledger carries historical verdicts, three types declare it as
a true statement about what a PICTURE needs, and `CLAUDE.md` states the ban itself. No regular
expression separates "emit `steps[]`" from "`steps[]` is retired". So the answer is a
checklist generator, not a check: `scripts/adr-sweep.py <term>` groups every hit into
TEACHES, RECORDS, GENERATED and UNCLASSIFIED, and `CLAUDE.md` rule 6c requires it before an
ADR's Consequences list is written.

**It earned itself on first run.** Swept against `multi-pass` it surfaced two teaching hits
ADR-039 had missed one commit earlier: `adapters/nano-banana.md` line 18, "multi-pass
pipelines are officially viable", stated with no pointer to the ban — now corrected to say
that is a fact about the MODEL and this pipeline does not use it — and
`registry/types/03-mechanism-xray.md` line 235, "If it recurs, the fallback is multi-pass",
which is a live instruction for the banned thing inside a type file. That one is LEFT
STANDING and named here instead: the file belongs to a render-refinement lane, and the
owner's standing instruction is to fix forward rather than edit another lane's work. It is
the first item for whoever next opens that type.

Consequences: `scripts/validate.py` gains `LEGAL_RATIOS`, `GRANDFATHERED_RATIOS` and
`check_ratios`, wired into `main` and into `check_grandfather_sets`; `scripts/adr-sweep.py`
is new; `CLAUDE.md` gains rule 6c; `adapters/nano-banana.md` line 18 gains the pointer;
`dist/app-bundle` regenerated. No type file is edited, no session is re-routed, no prompt
moves. `registry_version` unchanged.

## ADR-041 · 2026-08-24 · multi-pass is deprecated, and the field was never describing the pipeline

Owner instruction: clean multi-pass out of the system, and hand back the type files for
their own audit. This closes the system side and produces that worklist.

**The measured fact that decides the shape: no code has ever branched on the value.**
`scripts/validate.py` requires the key (REQUIRED_KEYS), checks it against
`registry/vocabulary.yaml` and writes it into `registry/index.yaml`. Nothing else reads it.
Since ADR-021 the pipeline has not acted on it at all, and since ADR-039 nothing teaches it.
It is a required, validated, indexed field that changes nothing.

**The name is the actual defect.** `generation_mode` reads as a statement about the
PIPELINE and is a statement about what the PICTURE needs — whether the image requires
compositing. ADR-021 separated those two ideas in prose and left the field carrying both.
That is why the owner tested the system, read `generation_mode: multi-pass` back, and
correctly reported that it still returned multi-pass. The report was right; the field was
lying about its own subject.

**Deprecated rather than deleted, and the sequencing is the point.** `multi-pass` stays in
`generation_modes` until the type files that declare it are cleared. Deleting it from the
vocabulary first makes `validate.py` line 310 error on those files immediately, turning the
tree red for every lane over a rule none of them broke today — the same reasoning ADR-040
used to warn rather than error the ratio declarations. `check_multipass_declarations` warns
one line per remaining declaration plus a countdown line on the vocabulary; when the count
reaches 0 the value comes out of the list in a one-line change and this is finished.

**Frontmatter only, and refusing to guess at the prose is deliberate.** A type that discusses
multi-pass in its body — a variant override, a recorded fallback, a CHANGELOG entry — is not
mechanically separable from one that merely records history, and no regex distinguishes an
instruction from a record. That is the false comfort ADR-040 declined to build.
`scripts/adr-sweep.py multi-pass` is the tool, and its TEACHES bucket is the list below.

**THE OWNER'S AUDIT LIST — five type files, and what is in each.**

- `registry/types/04-proof-lockedframe.md` line 12 — frontmatter `generation_mode:
  multi-pass`. Its capability gate already routes `strict` to `handheld` where the renderer
  cannot composite, so the working route does not depend on the declaration.
- `registry/types/05-social-handoff.md` line 12 — frontmatter `generation_mode: multi-pass`.
  Its `inset` is the part that needs compositing and the file already drops the inset rather
  than the type.
- `registry/types/01-pain-split.md` lines 151, 155, 278, 297, 324 — frontmatter is
  `single-pass`; the declaration is a `--mirror` variant override in prose, and the ledger
  records 1 of 1 each way: one single pass returned two different people (2026-08-12, hair
  mismatch between panels), one held identity using an explicit invariants block naming face,
  hair, beard, clothes, camera height, distance and framing before either panel (2026-08-13,
  pass). Whatever replaces the declaration has to keep that evidence.
- `registry/types/03-mechanism-xray.md` line 235 — "If it recurs, the fallback is multi-pass
  — generate the opaque product, then edit". This is a LIVE INSTRUCTION for the banned thing,
  the one ADR-040's sweep surfaced and left standing. It is the sharpest item on this list.
- `registry/types/_staging/03-use-grid.md` line 118 — "switch to multi-pass edit chains".
  Staging, never routable, lowest priority.

**Not touched here, on purpose:** no type file is edited. The owner takes them, and the
one-type-one-session rule is what makes that the right split — five files could belong to
five render-refinement lanes.

**The rename this points at is NOT done here.** Renaming `generation_mode` to something that
says what it means — `needs_compositing`, or similar — touches all 15 type frontmatters,
`vocabulary.yaml`, three lines of `validate.py`, `SPEC.md` §3.4, `index.yaml` and the bundle.
It is the only change in this repo that needs every other lane stopped first, so it is
recorded as available rather than taken.

Consequences: `registry/vocabulary.yaml` marks the value deprecated with the exit condition;
`SPEC.md` §3.4's field comment says so; `scripts/validate.py` gains
`check_multipass_declarations`, wired into `main`; `dist/app-bundle` regenerated. Warnings
28 → 33. No type file edited, no session re-routed, no prompt moved, 0 errors.

## ADR-042 · 2026-08-24 · The emoji badge, and why green could not be honoured

Owner decision, 2026-08-24, taken with the conflicts on the table: `01-pain-split` may draw its
verdict badges as **font emoji** — a full-colour cartoon face — rather than as a glyph cut out
of a signal-coloured disc. Four pieces of standing law had to be weighed and the owner chose
this against all four.

**What it supersedes, and it is a decision rather than an omission.** `01-pain-split` MARKS
records *"Source exemplars used VS badges and emoji; market habits, deliberately not
imported"*, and its CHANGELOG 1.3 records *"Market badge habits (VS, emoji, money props)
observed and explicitly excluded"* with four observation hashes behind it — `sha256:0b0260…`,
`3b4499…`, `f53928…`, `9ae982…`. That exclusion stood from 1.3 to 1.8. It is now overruled by
the owner, and it is written here rather than quietly edited so the reversal is legible.

**G6 gets an exception, narrowly.** G6 bans `text, letters, numbers` in every prompt, and its
scope note aims at overlay text — which a corner badge is. The X and the check survive that ban
because they are described as SHAPES, not as characters. An emoji is a character. The exception
is therefore explicit rather than implied, and it is bounded to the badge: nothing else in the
frame may carry a glyph.

**The finding that made a G3 amendment unavoidable, and it is not the one I expected.** Going
in, the objection to emoji looked like "they are yellow and G3 says yellow is neutral
structure". The real collision is narrower and sharper. **The angry face is RED, which agrees
with G3 exactly.** Only the confirming half conflicts — and it cannot be fixed by asking for a
green one, because **a green face in emoji vocabulary reads as NAUSEATED**. Honouring
"green = confirmation badge only" would invert the meaning of the half that confirms.

So the two symbol systems cannot both be obeyed by choosing colours more carefully. One has to
yield inside the badge, and the carve-out in `registry/rules.md` is written as narrowly as the
collision is: it binds only inside a badge a type has declared as emoji-form, only to that
badge's own fill, and it changes nothing about marks, structures or any other colour in the
frame. Yellow outside such a badge still means neutral structure, which is what
`02-cause-anatomy` and `03-mechanism-ghostbody` draw their anatomy in.

**The post-composite escape hatch does not exist here and that is worth stating.**
`01-pain-scene` records that *"a glyph is text, which G6 routes out of the render and into
post"*. ADR-021 removed post: this pipeline is paste-and-run. So the sanctioned route for a
glyph is closed, and the badge is model-drawn or it does not exist. That is a real added risk,
not a technicality.

**What the evidence says about whether it will render.** `06-relief-hero`'s `vs` badge rendered
**2 of 2 once the glyph was named**, and came back a blank disc before that — so naming the
glyph is what works. Round 3 of the `01-pain-split` audit rendered geometric faces clean 2 of 2,
with and without a human face in the frame, which settles the competition question the pairing
was built to test. Neither is evidence about a FONT emoji: a diffusion model has no font, so what
it returns is its own rendering of the idiom and it will vary between runs. Consistency across a
set is the thing to watch.

Consequences: `registry/rules.md` G3 gains the scoped carve-out. `registry/types/01-pain-split.md`
MARKS line 108 and CHANGELOG 1.3 still record the old exclusion and are LEFT STANDING for the
owner's audit of that file — they own the type files in this pass, and a supersede recorded here
is what reaches the other lanes. `dist/app-bundle` regenerated. No other type is touched; no
session is re-routed. `registry_version` unchanged.

## ADR-043 · 2026-08-24 · The verdict badge becomes a library of five forms, not one

ADR-042 recorded the emoji badge and stopped there, which left the record narrower than the
owner's actual decision. They approved **four** alternatives to the X/check pair — thumbs,
warning triangle, no badge at all, and emoji — and all five have now rendered. This records the
set so the badge is a choice with a menu rather than a constant with an exception.

**`01-pain-split` MARKS legislates exactly one form:** *"`verdict` | flat solid disc with the
glyph cut out of it, in a TOP corner, both the same diameter | red X left, green check right |
exactly 2"*. Shipping five forms against a file that names one is the gap this closes.

**All five rendered clean in round 3 of the audit, one product each:**

| form | result |
|---|---|
| `verdict-glyph` — red X disc → green check disc | clean. ~32 renders behind it across four types |
| `verdict-thumb` — thumbs-down disc → thumbs-up disc | clean: solid silhouette, no lumpy fist, no separate fingers |
| `verdict-hazard` — red warning triangle → green check disc | clean, and the fastest read of the six |
| `verdict-emoji` — angry face → smiling face | clean, with and without a human face in the frame |
| `verdict-none` — no badge | the grade split plus the red/blue mark pair still carried the verdict |

**Two findings the set produced that no single form would have.**

The thumb survived **because of how it was written**, not because hands became easier. G6 bans
`deformed hands, extra fingers` in every prompt. Writing it as *a flat pictogram cut out of the
disc, a solid silhouette, never a photographed or three-dimensional hand* is what kept it
geometry. That sentence is part of the form, not decoration on it.

The emoji form is **not consistent between renders**, and this is its one real limit. Across
round 5 the angry face came back flat red, then orange-red with a gradient, then rounder with
heavier brows; the smiling face varied between a closed grin and an open one with teeth. Same
idiom every time, different artwork every time — because a diffusion model has no font, so a
glyph that is identical everywhere in a typeface cannot be identical here. **`verdict-emoji`
therefore suits a single page and not a product family across many pages**, where
`verdict-glyph` holds its look and it does not. That is a scoping note, not a demotion.

**Why the pairing test mattered.** `verdict-emoji` ran twice in round 3, once with a human face
in frame and once with the subject cropped to hands, because a drawn face beside a real one
looked like it would compete. It did not: the badge sits in a corner, the face sits centre
frame, and the eye takes them in sequence. Without the pair the clean result would have been
one product's luck.

**The forms are interchangeable by construction.** Each is written as a drop-in `[BADGES]`
block of the same shape, so any form can be swapped into any prompt without touching another
line. `verdict-none` is the exception that proves it: it is a block that says no badge, rather
than an absent block, because a missing block reads as an oversight and a stated one reads as a
decision.

Consequences: this ADR is the record; **`registry/types/01-pain-split.md` MARKS still names one
form and is LEFT STANDING for the owner's audit of that file**, along with the multi-pass,
dropped-marks, blue-mark and ratio findings the five rounds produced. No rule file changes —
G3's carve-out from ADR-042 already covers the only colour question, and the other four forms
use red and green exactly as G3 assigns them. No other type is touched. `registry_version`
unchanged.

## ADR-044 · 2026-08-24 · The folder cards get short, get current, and get a Vietnamese twin

Owner asked for the folder cards to be cleaned up, kept as short as possible, and given a
Vietnamese version beside the English one. Opening them found they were not merely long.

**They were teaching three retired rules.** The cards still carried
`SHOT`/`ACTION`/`RESULT`/`MATCH` as what a brief must name — retired at ADR-031 — and told an
editor to file `proof_<product-slug>_<seq>.mp4` and "deliver mp4/webm and muted", both retired
at ADR-036 and ADR-037. Two different failures produced that. The type files' BRIEF sections
were rewritten and nobody re-ran the generator, so a generated view sat stale through six
ADRs. And the filing line was never read from anything: it was a hardcoded f-string inside
`card()`, so the generator itself was the thing teaching the old law. A sweep at ADR-036 would
have found the second; CLAUDE.md rule 6c exists because of exactly this shape of miss, and
this one is mine.

**`SPEC.md` §3.6 was teaching it too**, found by the rule 6c sweep rather than by reading:
"Filenames are `{gif-type}_{product-slug}_{seq}.mp4|webm`, the sequence issued by the ledger
… Delivery is mp4/webm". That is the two-name system ADR-037 collapsed and the extension
ADR-036 replaced, sitting in the specification eight days after both. Corrected here.

**The English card is now built from first sentences, and that is what keeps it honest.**
Every line is one sentence lifted mechanically from the type file — `PURPOSE`, `use_when`,
`avoid_when`, `NEGATIVE` — plus the `Against …` lines of `BOUNDARY` and the frontmatter band.
Nothing is authored twice, so the card cannot say something the law does not. The type files
were written with the whole point in the opening sentence of each section, which is why this
works at all rather than truncating mid-argument. 50 lines became 16.

**The Vietnamese card is authored, not translated at build time**, in
`registry/gif-cards-vi.md`. A machine translation of a rule is a rule nobody can check, and
the alternative — deriving Vietnamese from English at generation time — would put an
unreviewable sentence in front of the one person whose job depends on reading it correctly.
The numbers are the exception and are generated: a band and a file count need no translator.

**This is the one place in the repo where artifact content is not English**, and it is named
as such in CLAUDE.md rule 5 and SPEC §3.6 rather than left as an anomaly a later session
"fixes" by deleting. What makes it safe is that the Vietnamese card is a VIEW: everything that
binds stays in English in `registry/gif-types/`. What keeps it from drifting is
`check_gif_cards_vi`, which fails a gif type with no entry, an entry missing any of the five
fields, or an entry for a type that does not exist — because the failure mode is silent, a
card shipping a dash where a rule belongs. Three checks mutation-tested, 3 of 3 fired.

Consequences: `scripts/gen-gif-cards.py` rewritten around `lede()`, `against()`, `card()`,
`card_vi()` and `measured_vi()`, and now writes two files per folder; `registry/gif-cards-vi.md`
is new; `scripts/validate.py` gains `check_gif_cards_vi`; `SPEC.md` §3.6's filename and
delivery sentence corrected and the two cards declared; `CLAUDE.md` rule 5 names the
exception; `registry/gif-instruction.md` describes both cards. Twelve cards regenerated
outside the repo. The rule 6c sweep ran on `gen-gif-cards`, `product-slug}_`, `SHOT`, `muted`
and `artifact content is`; the `SHOT` and `muted` hits are legitimate — type files describing
photographic grade and a relief-hero worked example — and stand.

## ADR-045 · 2026-08-24 · The Vietnamese card is explanation, not translated law

ADR-044 shipped the Vietnamese folder cards a day earlier. The owner read them and said the
language was stiff and hard to follow, and asked for description with context — English
keywords left standing, only the prose in Vietnamese.

**The fault was structural, not stylistic.** ADR-044 built the English card by lifting the
first sentence of each section from the type file, which is right for English: those sentences
are the law's own opening clauses and the card cannot drift from what it summarises. Then the
Vietnamese file was authored to mirror them line for line. Mirroring a terse legal sentence
produces a terse legal sentence, so the Vietnamese card became a second copy of the
specification for a reader who does not need a specification — an editor deciding which folder
a file goes in. "Bằng chứng là những trạng thái đặt cạnh nhau để soi — bảng nhiều ô khoá cứng"
is accurate and teaches nothing to someone who has never seen a locked multi-panel still.

**So the two cards now do different jobs, and that is the point rather than a compromise.**
The English card stays the terse summary, mechanically derived, uncheatable. The Vietnamese
card is the working explanation: the situation first, then an example, then why the rule
exists. `proof` no longer says "physical evidence is a measurable change" — it says the loop
exists so the viewer sees the change and concludes for themselves, that a fabric lane goes
from grey to clean and an indicator from red to blue, and that the frame never cuts because a
cut is you asserting it on their behalf.

**Every English keyword stays as it stands** — type ids, `channels` values, `group`, `kind`,
field names, file paths. Translating `landing-page` would sever the card from every other
surface the editor touches, and translating `proof` would make the folder name and the card
disagree with each other.

**The field format changes from one line to a block**, because explanation with an example
does not fit a line and the previous format silently truncated at the newline. A field is now
`<key>:` alone on a line and everything after it belongs to that field until the next key or
the next type, blank lines kept. Both readers — `scripts/gen-gif-cards.py` and
`scripts/validate.py` — parse it the same way, from the same shape of loop, because two
parsers for one file is how a file starts meaning two things.

The card layout follows: `## ` headings rather than bold run-ins, since the values are now
paragraphs. It is longer than ADR-044's sixteen lines and that is the trade taken knowingly —
the owner asked for shortest first and, having read the result, asked for readable instead.
Short was never the goal; a card an editor can act on was.

Four checks mutation-tested after the parser change, 4 of 4 fired: a missing type, a missing
field, a field left empty, and an entry for a type that does not exist. The empty-field case
needed a second attempt — the first mutation inserted a key the parser does not recognise, so
the text simply joined the previous block and nothing was empty. A mutation that does not
create the state it names proves nothing about the check.

Consequences: `registry/gif-cards-vi.md` rewritten in full and its header now states the
writing rule rather than only the mechanics; `scripts/gen-gif-cards.py` gains
`_parse_vi_blocks()` and `card_vi()` is rebuilt around headings; `scripts/validate.py` parses
the same block form. Twelve cards regenerated outside the repo; the English six are byte
identical, which is the check that this changed only what it claimed to.

## ADR-046 · 2026-08-24 · An example names its product and its page, or it explains nothing

ADR-045 made the Vietnamese card explanation rather than translated law. The owner read the
result and found the examples still unusable: no context, no clear meaning. They also asked
for the example to come AFTER the definition, and for two sections to go.

**The examples were borrowed, and a borrowed example carries its context with it — somewhere
else.** ADR-045 kept the illustrations from the English type files: a lane of fabric going
grey to clean, a stack of bags collapsing to a third, an indicator turning red to blue. Those
sentences work inside `registry/gif-types/proof.md`, where the reader has the whole type file
around them. Lifted onto a folder card they name no product, no page and no situation, so an
editor holding a file learns nothing from them. The failure is the same one ADR-045 diagnosed
one level down: the card was still assembled from material written for a different reader.

**Every example is now a real loop this library has commissioned, named with its product.**
The `cause` card describes the seat cushion page's loop — a driver on an old flat pad, the car
brakes, the pad slides forward under him and the gap opens behind his lower back, and the
cushion being sold is nowhere in frame. `proof`, `mechanism` and `use` all draw from the
massage comb page, which is the strongest teaching accident available: **one product, three
loops, three folders.** The `use` card says so outright — hands combing through is `use`, the
teeth retracting to release the hair mat is `mechanism`, the static halo collapsing after one
pass is `proof` — because an editor who sees those three side by side has learned the
distinction in a way no definition delivers.

**Definition first, then the example.** ADR-045 ran them together in one paragraph, so the
illustration read as part of the definition and the definition never landed. Each `message`
now closes its thought, breaks, and opens with "Ví dụ, trang bán…".

**`no` gains an example too, and that is where it was weakest.** Telling an editor not to file
a held state here is abstract; showing them that a stripped mattress lying there is a still
while dust lifting out of the weave under someone sitting down is a loop is not. The
mechanism card now uses the comb's six red LEDs: the lamp is filmable, its effect on a scalp
is not, which is the invisible-claim rule in one concrete pair.

**Two sections cut on the owner's instruction:** "Cấm xuất hiện trong khung" and "Chuẩn nhà".
The negatives and the band still bind and still sit on the English card and in the type file;
what they were doing on the Vietnamese card was turning an explanation back into a
specification. The `never` field goes from the source file and from both parsers with them,
and `measured_vi()` — written at ADR-044 to translate a file count — is deleted as dead code
rather than left for someone to wonder about.

Four checks mutation-tested against the four-field form, 4 of 4 fired. The English cards
regenerate byte-identical, which is the evidence this changed only the half it claimed to.

Consequences: `registry/gif-cards-vi.md` rewritten, its header now carrying the three writing
rules rather than one; `scripts/gen-gif-cards.py` drops `never` from `VI_FIELDS`, drops the two
sections, and `card_vi()` no longer takes the ledger or the frontmatter because it no longer
prints a number; `scripts/validate.py` follows on the field list. Twelve cards regenerated
outside the repo.

Addendum, same day: rule 3's keyword list was scoped to ids, channels, fields and paths, and
the prose it protected still translated the craft vocabulary — "quay cận" for close-up, "cắt
bổ" for cutaway, "khung hình" for frame — so the Vietnamese card and the English law beside it
described the same shot in two vocabularies. Rule 3 now names the craft terms (frame,
close-up, cutaway, loop, motion, rotor) and the ten translated occurrences are swapped in
place. Four cards regenerated.

## ADR-047 · 2026-08-24 · Delivery goes back to mp4, and G12 stops contradicting itself

Owner instruction: every gif file is mp4 now. This reverses the delivery half of ADR-036 and
leaves its naming half standing.

**The reason ADR-036 gave for WebP was real, and reversing it does not make it false — it
relocates it.** WebP sits in an `<img>`, exactly where a still already sits, and that is what
made a loop and a still interchangeable in a page template. mp4 needs a `<video>` with
`autoplay`, `muted`, `playsinline` and `loop`. So the interchangeability is now a **template
dependency outside this repo** rather than a property of the file: a slot that earns motion
needs its template to carry a `<video>`. That is recorded in G12, in Step 5c, in
`gif-instruction.md` and in the schema rather than left for someone to discover on the day a
loop is dropped into an `<img>` and does not play. It is the owner's call to make — the files
the editors actually produce are mp4, and a naming law that disagrees with what arrives is a
law that gets worked around rather than followed.

**Muted becomes a stated requirement again.** ADR-036 removed it from the `delivery` string
because WebP carries no audio track by format, so there was nothing to mute. mp4 does, so the
rule comes back rather than being assumed.

**The rule 6c sweep found G12 contradicting itself, which is the finding this ADR would not
otherwise have produced.** Two paragraphs of G12 gave two different filename patterns: the
field block and the one-per-type rule had been updated at ADR-037 when the slot was removed,
but the paragraph in between still read `{page-type}-{gif-type}-{product-slug}-v{NN}-{slot}
.webp` and still instructed a reader to "append the slot". A rule that states its own pattern
twice will drift at one of them, and this one had — for ten days, in the file that is supposed
to be the single statement of the law. Rewritten to one pattern.

The sweep's only other surviving `webp` in a teaching file is
`ingestion/runbooks/classify-batch.md`, whose `find` includes `*.webp` among the image
extensions of the market corpus. That is a still-image format for `stills/` and has nothing to
do with the GIF library; it stands.

Seventeen loops across six sessions renamed, plates and folder cards regenerated. The
seventh session, `listicle-bp-monitor-upper-arm-v01`, keeps its pre-ADR-028 names and is
untouched. `GIF_FILE_RE` tested against five filenames, 5 of 5 as expected — both live forms
accepted with the right type extracted, and a leftover `.webp`, the retired library name and a
leftover slot field all rejected. Two build checks mutation-tested, 2 of 2 fired.

Consequences: `registry/rules.md` G12 loses the stale slot paragraph and moves to mp4;
`query/runbook.md` Step 5c and the delivery paragraph; `SPEC.md` §3.6; `query/output.schema.json`
`gif.output` and `gif.delivery`; `registry/gif-instruction.md` §4;
`scripts/validate.py` `GIF_FILE_RE` and its error message; `scripts/gen-gif-cards.py` in both
the English and Vietnamese filing lines; six `build.py` files and their emitted
`gif.output` and `gif.delivery`. `registry_version` unchanged.

## ADR-048 · 2026-08-25 · `verdict-emoji` loses its scope note, and the measurement behind it stands

Owner decision, 2026-08-25, taken with ADR-043's finding on the table: **`verdict-emoji` ships
with no scope limit.** ADR-043 closed with a restriction and this removes it.

**What is overruled, and it is one sentence rather than a finding.** ADR-043 recorded that the
emoji badge "suits a single page and not a product family across many pages", and called that a
scoping note rather than a demotion. The owner has now scoped it to nothing: any page, any
family, decided by whoever routes.

**What is NOT overruled, and separating the two is the whole point of this entry.** The
measurement that produced the scope note stands exactly as recorded. Across round 5 of the
`01-pain-split` audit the angry face came back flat red, then orange-red with a gradient, then
rounder with heavier brows; the smiling face varied between a closed grin and an open one with
teeth. Same idiom every time, different artwork every time, because a diffusion model has no
font and a glyph that is identical everywhere in a typeface cannot be identical here. That is a
fact about the renderer and no decision reaches it. What changed is what the library DOES about
it: it used to refuse the case, and now it lets the router weigh it.

**So the honest statement of the risk, since nothing in the repo will state it after today.**
`verdict-glyph` holds its look across a family and `verdict-emoji` does not. With the scope
note gone there is no gate, no warning and no field that will stop ten pages of one product
family from carrying ten different angry faces. The mitigation exists and is NOT taken here — a
per-type declaration bounding which badge forms a type may use — because `01-pain-split`'s MARKS
still names exactly one form and belongs to the owner's audit pass, and adding a field to a file
this lane may not edit is not available. It is recorded as available rather than done.

**Rule 6c sweep, run before this list was written.** `scripts/adr-sweep.py verdict-emoji`
returns 4 hits across 2 tracked files, and **both are RECORDS**: `decisions/log.md` and
`eval/render-tests.jsonl`. **The TEACHES bucket is empty.** That is the useful result rather
than a formality — it means the scope note never reached a rule file, a type file, a runbook or
a schema, so removing it corrects nothing and leaves nothing standing. The three teaching hits
ADR-040 and ADR-039 each found late do not have an analogue here, and the reason is that
ADR-043 already declined to write the five forms into any type file.

**Two neighbours checked and left alone, stated so nobody re-opens them.** G3's emoji-badge
carve-out (ADR-042) governs COLOUR inside a declared emoji badge and says nothing about how many
pages may carry one, so it is untouched. G6's exception admitting the badge as the one glyph in
frame is likewise about the frame, not the page. Neither needed a word changed.

**The context worth stating once.** `feedback/picks.jsonl` is still empty at 0 picks, so SPEC
§7.7's twenty-pick tie-breaker has never fired and no routing recommendation this library has
made has ever been measured against an outcome. A decision like this one has no data to beat —
the owner's judgement is the only input available, which is an argument for recording it
plainly rather than for deferring it.

Consequences: this entry is the whole change. `decisions/log.md` only — and it is not a bundled
file, so `dist/app-bundle` does not move. No rule file, no type file, no schema, no runbook and
no session is touched; `registry/types/01-pain-split.md` MARKS still names one badge form and
remains on the owner's audit list where ADR-042 and ADR-043 put it. `registry_version`
unchanged. 0 errors.

## ADR-049 · 2026-08-25 · `01-pain-scene` stops asking for a film still, and takes a narrow G11 exemption

Owner instruction across three turns: the frames look like film stills rather than photographs,
the colour is not true, and this type should attend to the pain and not to the surroundings —
which may be bright, dark or any weather. He rejected the look twice and then asked for the type
to be committed. This records the law change that reaching his instruction required.

**The complaint was about TONE, and the measurement is what separates that from hue.** The set he
rejected returned a mean midtone share of **28.4% of frame** with **70.1% crushed to near-black**.
The same formula with `low-key`, crushed blacks and deep-shadow replaced by "the real light of the
place" plus an ordinary-exposure clause returned **61.0% midtones** across three rounds and
eighteen renders, against a reference set at 65.5%. Colour CAST was never the difference — midtone
|b−r| measured 25.4 against 23.9, and a synthetic teal push on a reference frame moved that metric
from −18.6 to +41.8, so the instrument would have found a grade had one been there. **The frames
read false because there was almost no midtone left for any colour to live in.**

**The old grade also ate the mark, which is the part no style argument would have caught.** The
darkest frame of the rejected set, mean luminance 29.2, returned its red glow at peak R−G **45** —
the weakest signal any marked frame of this type has produced, against 111 to 203 elsewhere in the
same set. A grade that desaturates the frame desaturates the mark inside the frame.

**`REGISTER` had a clean A/B sitting inside the type's own vocabulary.** Line 48 said `cinematic
film still`; the STYLE line said `editorial photojournalism, cinematic film still, natural and
unstaged`. Sets using the photojournalism half alone came back looking like photographs; the set
using `cinematic film still` came back looking like film stills. The type now uses its own other
half, so nothing foreign was imported to fix this.

**THE G11 EXEMPTION, AND WHY IT IS NARROW.** G11 is titled *Saturation carries the state* and its
instrument is "reduced saturation or grayscale, cool or neutral, never warm". The muted half is
kept in the new `grade`: colour is true to life and **muted rather than vivid**. What is dropped
is everything G11 never asked for — G11 does not require DARKNESS, and darkness is what the
withdrawn wording actually produced. The exemption is taken by ID rather than by quiet divergence,
following `04-proof-lockedframe`, which G11's own text names as the precedent for a type whose
`[GRADE]` slot legislates saturation differently and on purpose.

**Recorded with it, because it should not be found later: G11's "never warm" was already breached
by every render this type has ever produced.** Measured midtone b−r ran warm in 6 of 6 of one set
and 4 of 6 of another. The exemption regularises a divergence that predates it rather than
creating one. Whether G11's "never warm" clause is right for the library at all is a question for
whoever next opens `registry/rules.md`; it is not answered here and no other type's relationship
to G11 changes.

**What carries the unresolved state instead of the palette.** The `cost` block, which says what
the pain is taking away, and the mark where one is used. Both were measured working across the
same rounds, and both are stronger instruments for this type's job than a desaturation the owner
rejects on sight.

**Six other rules landed in 1.17 in the same pass, each paid for by a render** and each recorded
in the type file with its evidence: the cost is LOCKED to the body part being refused; a failure
must be FINISHED and its residue a DISPLACED OBJECT, never a state and never an interruption; the
mark goes where the subject's HAND already is; a POINT landmark binds placement and a span does
not; the exclusion sentence is REFUTED and must not be written; rank-2 residue carries a mark-free
frame alone, 2 of 2; and a symptom described as a COMPARISON does not render.

**Rule 6c sweep, run before this list.** `adr-sweep.py G11` returns 43 hits across 15 files, four
of them TEACHING: `registry/rules.md` (the rule and its exemption mechanism — **used as designed,
not edited**), `registry/types/01-pain-scene.md` (this ADR's subject), `registry/types/
04-proof-lockedframe.md` (the precedent, **left standing**) and `registry/types/06-relief-hero.md`
(a high-key neutral grade citing G11 by ID — a different type, not exempt, **left standing**).
`adr-sweep.py "crushed blacks"` returns one teaching file, this type, at three lines: two are
rewritten and **the third is inside a WORKED EXAMPLE and is deliberately left verbatim** — SPEC
§3.3 keeps those as the record of what actually rendered, and the note above them now says their
`REGISTER`, `[LIGHT]` and `[GRADE]` lines are superseded and must not be copied.

Consequences: `registry/types/01-pain-scene.md` → **1.17**, sixteen edits — frontmatter version and
`exempt_from`, the SKELETON's `REGISTER`, `[GRADE]` and `STYLE` lines, `PARTS/light`, `PARTS/grade`,
`PARTS/cost`, `PARTS/evidence`, the `glow` evidence row, admission gates 2 and 3, a new gate 4, the
`--candid` diff, the WORKED EXAMPLES note and a CHANGELOG entry. `registry/index.yaml` regenerated;
`dist/app-bundle` rebuilt. No rule file, no other type, no schema and no session is touched.
`registry_version` unchanged. 0 errors.

**Lane note, stated rather than assumed:** this session's standing scope excluded
`registry/types/`. The owner instructed the commit directly, which is the human gate ADR-007
names, and the type file had already been taken to 1.16 by another lane whose work is preserved
intact — 1.17 edits it forward and reverts none of it.
## ADR-050 · 2026-08-25 · A section is a block, not a prefix — the spacing rule stops merging editorial blocks

Owner instruction, 2026-08-25: **the `content.x.image` blocks are different sections, the same
way `reason.0`, `reason.1`, `reason.2` are.** It is a template change with no effect on what any
picture contains, and its purpose is that generated content stops being bound to the shape of a
reason list. The reading mechanism is corrected here to match.

**The defect, stated as arithmetic rather than as a policy disagreement.** Step 5d has said "at
most one loop per section" since ADR-024, and every routing computes that section as
`slot_id.split(".")[0]` — the top-level prefix and nothing else. On the export shape the owner is
moving to, one page numbers three separate editorial blocks under one prefix: `content.0.image`
is the article opener, `content.1.items.0` through `content.1.items.4` are five cards, and
`content.3.items.0` and `content.3.items.1` are two more. All three collapse to a single section
named `content` carrying 8 image slots, and the whole body of the page is therefore allowed
**2 loops** — one, plus the ADR-032 relaxation for a section of five items or more. The rule was
written about editorial sections and is being applied to a string prefix; nowhere did anyone
decide that an opener, a five-card list and a two-card list are one section.

**The definition, because the rule is arithmetic on the slot id and should be readable as such.**
A section is the slot id's top-level prefix, plus its next segment when that segment is a NUMBER.
A number sitting directly after the prefix is a BLOCK index, and each block is its own section; a
number sitting after a container word — `items`, `photos`, `shots`, `quotes` — is an ITEM index,
and the list stays one section.

    def section(slot_id):
        p = slot_id.split(".")
        return f"{p[0]}.{p[1]}" if len(p) > 1 and p[1].isdigit() else p[0]

So `content.1.items.3.image` and `content.3.items.0.image` are two sections; `reason.0.image` and
`reason.4.image` are two sections; `features.items.0.image` through `features.items.4.image`
remain one, which is the case ADR-024 was actually written against and which this does not touch.

**Measured before it was written, dry, across all twelve routed sessions.** Section counts change
on exactly two: `advertorial-seat-cushion-l-shaped-v02` goes 4 to 9 (`story.N`) and
`listicle-massage-comb-spray-v01` goes 5 to 10 (`reason.N`). No session that is legal today
becomes illegal. One session carries 4 loops in one section under the new reading —
`advertorial-seat-cushion-l-shaped-v01`, page 31 — and it is the page ADR-024 was written against,
routed before the rule existed and already grandfathered.

**The honest size of the gain, because the tempting number is the wrong one.** Of the 11 slots
across the twelve sessions that earned motion on the temporal test and were refused by the
spacing rule, this frees **2** — both in `listicle-massage-comb-spray-v01`, whose cards are
numbered `reason.N`. The other 9 sit in `X.items.N` lists that stay one section, correctly. The
gain is not on the pages already routed; it is on the shape being routed next. On
`landing-page-listicle-7-in-1-external-usb-dvd-v03`, the page body goes from **2 loops to 4**
against a ceiling of 5.

**Rule 6c sweep, run before this list was written.** `scripts/adr-sweep.py "one per section"`
returns 3 hits across 3 files: **1 TEACHES** — `query/output.schema.json:574` — plus the
generated bundle copy and the decision log. `scripts/adr-sweep.py 'split(".")[0]'` returns 15
hits, **0 TEACHES**: six session `build.py` files, which are RECORDS of completed routings, and
one hit in `scripts/validate.py` that parses a version string and is unrelated.

**The sweep missed one teaching file and it is worth recording why.** `query/runbook.md` states
the rule as "at most one per / section" across a line break, and the sweep matches line by line,
so the file the rule actually lives in did not appear in any bucket. It was found by reading Step
5d directly. A sweep is a checklist generator and not a proof; this is the second mechanism —
after ADR-020's and ADR-039's — by which a teaching file stays invisible to it.

**Consequences.**

1. `query/runbook.md` Step 5d carries the definition and the function above. This is the file the
   rule lives in and the one the sweep could not see.
2. `query/output.schema.json`'s `motion.ceiling` description is rewritten. It was stale on two
   counts independent of this decision: it still taught the pre-ADR-032 rule with no five-item
   relaxation, and it still carried ADR-024's general never-adjacent clause, which ADR-024 itself
   dropped. Both are corrected in the same edit, and the drift is named here so it is not
   rediscovered as new.
3. The six session `build.py` files keep `split(".")[0]` and are NOT migrated. They are records of
   completed routings whose outputs were correct under the rule in force, and rewriting them would
   change delivered artefacts to no reader's benefit — the treatment ADR-024 gave page 13 and
   ADR-034 gave the pre-ADR-028 gif blocks. The next routing writes the new function.
4. No validator gate is added. A full check needs each section's ITEM COUNT to test the five-item
   relaxation, and `prompts.json` records only the slots that were routed rather than every item
   in a list, so the denominator is not on disk. A partial gate that checks the ceiling but not
   the relaxation would report a green it has not earned.
5. `motion.floor` and `motion.ceiling` are untouched. The measurement says pages hold 4 to 5
   loop-worthy slots and the binding constraint was never the ceiling, so changing either would be
   moving the wrong number.
## ADR-051 · 2026-08-25 · The loop replaces the slot, not a layer — the empty block is retired and the filename carries the slot

Owner instruction, 2026-08-25, in three parts. **One:** the option prompts may span several
image types or stay on one across A/B/C, and an inset that belongs in the picture is rendered
NORMALLY. **Two:** where a slot carries a loop the editor learns it from the app, which already
marks that slot; the editor builds the loop and drops it in, and **the still is not to be drawn
with an empty block**. **Three:** the delivered gif spec takes a stated shape, and its filename
carries the SLOT rather than the gif type.

**What this reverses, named so the reversal is legible.** ADR-033 made a `form: inset` loop
reserve its host type's legislated layer as a flat empty block of one tone, and accepted the
consequence that the host render keeps the slot's asset filename and **is not shippable until the
loop is in it**. That consequence was recorded at the time as "a change of risk rather than a
removal of one", and rules.md says plainly why: a flat empty block ships unnoticed as a design
element, where the old plate covered in lettering could not. The owner has removed the risk at
the source. A still now renders complete, ships on its own, and the loop is an upgrade to it
rather than a component of it.

**So `inset` leaves the gif verdict and stays everywhere else.** The `form` enum keeps
`whole-frame` and `none`. A loop replaces the whole slot asset, which is what "the editor drops
the gif into the slot" means, and its `ratio` is therefore always the SLOT's declared ratio from
`content.json` — the layer-shape branch ADR-033 wrote into the schema has nothing left to
describe. This touches the gif verdict ONLY. An inset is a compositional device in 79 tracked
files and every one of them is untouched: insets in pictures are wanted, and the owner asked for
them explicitly.

**The filename.** `{page-type}-{product-slug}-v{NN}-{slot-id}.mp4`, where the slot id is its dots
turned to dashes — the session directory (ADR-034) with the slot appended:

    advertorial-seat-cushion-l-shaped-v04-content-items-3-image.mp4

The gif type comes out and the slot goes in. What each choice buys: a slot id is unique on a page
by construction, so the file is unique without a rule protecting it, and a reader can join the
file back to the exact slot it fills without opening anything. What it costs: the argument the
loop makes is no longer readable from the name, and it moves to `gif.type_id`, which is what
decides the library folder and was always the field that did.

**Therefore one-loop-per-gif-type stops being a rule (ADR-037) and becomes a preference.** That
rule existed because the filename had no slot and no sequence, so two loops arguing the same
thing would collide — it says so in its own sentence, in `rules.md`, in `SPEC.md` and in
`gif-instruction.md`. The collision is gone, and with ADR-050 splitting numbered blocks into
separate sections a page can now legitimately carry a `mechanism` loop on `content.1` and another
on `content.3`, which the rule would have refused for a reason that no longer exists. The second
justification ADR-037 offered — that a page arguing the same thing twice is repeating itself —
survives as a preference recorded in `motion.notes`, on the same footing as the working/result
coverage pair, which SPEC §7 already treats as a preference and not a gate.

**Delivery becomes `mp4/webm`.** ADR-047 settled on mp4 against WebP and the reasoning is
untouched: both sit in a `<video>`, so the template dependency that ADR-047 named — `autoplay`,
`muted`, `playsinline`, `loop` — is unchanged, and adding webm changes nothing about it. Muted
stays a stated requirement for the reason ADR-047 gave: these containers carry an audio track
where WebP could not.

**Rule 6c sweep, five terms, run before this list was written.**

| term | hits / files | TEACHES |
|---|---|---|
| `flat empty block` | 12 / 7 | 3 — runbook, rules.md, 06-relief-hero |
| `one loop per gif type` | 14 / 10 | 2 — SPEC.md, gif-instruction.md |
| `gif-type}-{product-slug` | 16 / 12 | 5 — SPEC.md, schema (×2 sites), runbook, gif-instruction, rules.md |
| `not shippable` | 8 / 8 | 2 — rules.md, 06-relief-hero |
| `whole-frame` | 221 / 45 | 4 — schema, runbook, gif-instruction, 02-cause-anatomy |

**Consequences — every teaching file above, accounted for.**

1. `query/runbook.md` Step 5c: the two-forms block loses `inset`; the four-field display becomes
   the owner's stated spec block; the naming paragraph, the one-per-type paragraph and the
   delivery paragraph are rewritten; the sentence reserving the layer as an empty block is cut.
2. `registry/rules.md` G12: the naming block is rewritten, the one-per-type rule is demoted to a
   preference, and the paragraph declaring the host render unshippable is removed with ADR-033
   named as what it reverses.
3. `SPEC.md` §3.6: the naming line and the one-loop-per-gif-type sentence; delivery becomes
   mp4/webm.
4. `registry/gif-instruction.md` §4: the same three, plus §7's pointer, which named the form pair
   `whole-frame` / `inset`.
5. `query/output.schema.json`: `form` drops `inset` at BOTH sites — `slots.items.gif` and
   `recommended.items.gif` carry duplicate definitions and the sweep caught the second, which is
   the failure mode ADR-039 recorded. `output` and `ratio` descriptions are rewritten at both.
6. `registry/types/06-relief-hero.md`: the `[INSET MOTION] --loop` block stops reserving an empty
   block; the layer renders normally and the still ships on its own. CHANGELOG 1.17.
7. `registry/types/02-cause-anatomy.md:361` is **left standing**. Its hit is a CHANGELOG line
   about a "whole-frame formula" holding across 6 renders — the compositional sense of the words,
   not the gif verdict's `form`. Nothing there instructs anything this decision changes.
8. The three routed sessions carrying `form: inset` — `advertorial-seat-cushion-l-shaped-v02`,
   `-v04` and `listicle-air-cooler-wall-mounted-v01` — are NOT migrated. They are records of
   completed routings, `prompts.json` is not validated against `output.schema.json` (only
   `content.json` is, and only against `mapping/content.schema.json`), so nothing reports an
   error and nothing needs one. This is the treatment ADR-024 gave page 13.
9. `scripts/gen-plate.py` is NOT changed and keeps working: it reads `output`, `duration_s`,
   `ratio`, `loop`, `brief`, `alt` and `refs`, all of which survive. It is now a second view of
   the same fields the spec block carries, and with the app marking gif slots its original
   justification (ADR-019, the work order must reach the editor rather than sit in a document
   nobody opens) is weaker than it was. Retiring it is recorded as AVAILABLE and not taken —
   nothing the owner said requires deleting a generator, and 17 plates across the routed sessions
   are correct output.

**What is deliberately NOT done.** `06-relief-hero`'s `inset_motion: [still, loop]` axis is kept
rather than retired. Under this decision `--loop` no longer renders differently from `--still`,
which makes the axis vestigial at render time, but it still records that a slot was commissioned
as a loop, the type file carries four founding renders against it with ledger sha256s (1.15), and
retiring an axis is a taxonomy change of a different weight than this instruction. It is named
here so it is not rediscovered as drift: the axis is vestigial by decision, not by oversight.
`motion.floor` and `motion.ceiling` are untouched for the reason ADR-050 gave.
## ADR-052 · 2026-08-25 · The pool-diversity rule becomes a gate, because it was breached with itself already in force

Owner instruction, 2026-08-25: every slot's A/B/C must span at least two image types, so the
pictures offered for a slot stop repeating one type. The instruction is not new law. Runbook
Step 4 has said exactly this since `e7dfe8c` — "one-type-once binds the recommended SET, never
the option pool" — and recorded the measurement that motivated it: read the other way, 83 of
101 non-A options across the first four routed pages varied on execution, 11 on axis, and 7 on
type, so pages shipped with no type variation at all.

**What makes this entry necessary is HOW the rule failed.** Page 193's first routing shipped
8 of 8 multi-option slots single-type. The session that routed it had read Step 4's paragraph
during preparation — the grep that surveyed the section is in the transcript — and applied
one-type-once to the pool anyway. That is the strongest possible evidence that prose alone
cannot hold this rule: it failed not through ignorance but through the exact misreading it was
written to correct, in a session that had the correction in front of it. The repo's own
maxim, written into the ADR-021 gate: a rule nothing runs is a rule nobody keeps.

**The gate.** A multi-option slot whose options all carry one type is an ERROR unless the slot
declares `single_type_basis` — a new string field at the schema's slots site naming the
exhausted cell: which role×channel cell it was and what the attribute gates left, or which
set law makes the tile the unit of variation. The two legitimate cases are the ones Step 4
already names: the cell genuinely holds one type after the gates, and a repeating section
whose type legislates a SET (each review tile emits one option; the variation lives across
tiles). The declaration is the statement Step 4 asked `varies_on` to carry, made
machine-readable, because a string marker inside a per-option field is exactly the kind of
prose that drifted the first time.

**Where it runs.** `scripts/validate.py` (`check_option_pools`), binding every session routed
after 2026-08-25; and page 193's `build.py` carries the same check plus one the validator
cannot run — check 19 fails the build when a B repeats a type recommended elsewhere without
naming the displaced slot, which needs the recommended set and is per-session knowledge.

**Grandfathering.** The 12 sessions routed before this gate carry 57 single-type pools between
them; they are records of completed routings, legal output under the practice of their day,
and are not migrated — the treatment ADR-024 gave page 13. They stand in
`GRANDFATHERED_SINGLE_TYPE`, registered with `check_grandfather_sets` so a renamed session
directory errors instead of silently shedding its exemption (the ADR-035 mechanism), and
surface as ONE aggregate warning rather than twelve — the vocabulary.yaml pattern, chosen
because twelve standing warnings would drown the live signal the warning list exists to carry.

**Verified against known-bad input before the exemption was wired.** The gate was first
installed with an EMPTY grandfather set and run against the repo: it flagged exactly the 12
known-bad sessions and passed the re-routed page 193, then the set was populated and the tree
returned to 0 errors with the one warning. The ADR-035 registration was mutation-tested by
naming a nonexistent session in the set and watching the error fire. In the build, checks 18
and 19 were proved live the same way, each mutation printing the state it created.

**Rule 6c sweep.** `"binds the recommended SET"`: 1 TEACHES — `query/runbook.md:137`, the rule
itself, which gains the enforcement paragraph rather than losing anything. `"no second type
survives"`: 1 TEACHES — `query/runbook.md:94`, the B-option definition, LEFT STANDING as
written: it stays true that B falls to an axis when no second type survives the gates, and
what changes is that the slot must now also declare that fact in `single_type_basis`, which
the enforcement paragraph states. `"single_type_basis"`: 0 TEACHES outside the surfaces this
ADR edits (the term existed only in page 193's re-route, committed one commit earlier).

**Consequences.**

1. `scripts/validate.py`: `check_option_pools`, `GRANDFATHERED_SINGLE_TYPE`, and the set's
   registration in `check_grandfather_sets`.
2. `query/output.schema.json`: `single_type_basis` added at the SLOTS site only. There is no
   duplicate-definition trap this time, and that is stated so nobody hunts for it: the
   `recommended[]` item shape differs (additive proposals, `earns_its_place`) and the gate
   does not bind it, so no second site exists to miss.
3. `query/runbook.md` Step 4: the enforcement paragraph, immediately after the `e7dfe8c`
   citation it enforces. Line 94's axis-B definition is left standing (see sweep).
4. Session `build.py` files before page 193's are NOT retrofitted with check 18 — they are
   records, and the validator now covers their outputs' future siblings.
5. What the gate deliberately does NOT demand: three distinct types, or any minimum on
   single-option slots. A repeating-section tile emits one option by set law, and two types
   across three options is what the owner asked for and what Step 4's B-slot provides.
   Raising the bar further is a separate decision with its own costs in prompt-writing time.

## ADR-053 · 2026-08-26 · `05-social-handoff` had two gazes and no act, and its inset never needed compositing

Owner feedback on four rendered frames: the image logic is poor, no story is told, and nothing is
being handed to the other person through expression, gesture or action. Separately: the inset
should vary in shape and proportion rather than always being a circle. Both are acted on here, and
the first one turns out to be a gap in the type rather than a weakness in the frames.

**All four renders obeyed the skeleton exactly, and that is the finding.** `[ADVOCATE] just used
it, eyes on the listener` and `[LISTENER] face NOT visible, attention on the moment` are correct
in 4 of 4. The type legislates two EYE DIRECTIONS and no ACT: no slot asks the advocate to offer,
point at, pass, hold out or demonstrate anything. **The word handoff was in the type's name and in
none of its slots**, so nothing was handed over and the frames read as two people standing near a
product. This is the shape `01-pain-scene` was in before `cost` — every slot correct, the argument
absent, because the block carrying the argument did not exist.

`handoff` is therefore a new REQUIRED part with four forms — `offer`, `take`, `point`, `show` —
and one law borrowed rather than paid for twice: **the act must be a STATE a still frame can hold,
never a movement in progress.** Two hands on one object reads; one hand reaching toward an object
does not, because a still cannot say whether it is arriving or leaving. `01-pain-scene` bought
that finding with two dead frames — a stalled reach that rendered as an ordinary reach, an
arrested turn that rendered as no turn.

**THE INSET NEVER NEEDED COMPOSITING, AND THE FILE'S OWN RECORD IS WHY.** It said the inset "needs
compositing, so where the renderer cannot composite it is unavailable", which under ADR-021 made
it dead. But the founding failure it cites is not a compositing failure: *"the founding exemplar
failed on that alone, beige in scene and charcoal in inset, which reads as two products."* That is
a colourway mismatch, and a clause binds it — which `06-relief-hero` already proved by carrying
five inset modes single-pass with `inset from a different photographic source` among its
negatives.

Tested with one clause in identical words across four frames, it held **4 of 4, and beyond its own
terms**: a two-tone spot cleaner reproduced the same brown dirty water at the same level in the
same two chambers as the unit in the scene — product STATE, not merely colour — and a metallic
lopper matched on FINISH rather than on hue. So `generation_mode` becomes `single-pass` and this
type leaves ADR-041's audit list, whose countdown goes 2 to 1 with only `04-proof-lockedframe`
behind it.

**Shape and proportion are freed; size and position are not.** Circle, square or rectangle at 1:1,
3:4, 4:5 or wider, on the owner's instruction — four circular renders in one set is a sameness the
type does not need. What stays fixed is what a render actually cost: 15-20% of frame width, a
corner or edge near the moment, nothing bridging it to the scene. A disc at 24% over dense foliage
read as a hole punched in the garden. **An inset's own proportion is not the FRAME's ratio**, which
ADR-016 continues to govern — 4:5 is legal for an inset shape and remains illegal as a frame.

**Rule 6c sweep, and it earned itself again.** `adr-sweep.py 05-social-handoff` returns 187 hits
across 36 files, 8 of them TEACHING, and two were still teaching the withdrawn law:
`adapters/nano-banana.md`'s **Template B**, a generate-then-composite recipe naming this type, and
`query/runbook.md` line 81, *"the `inset` is omitted, not the type"*. Both are corrected here.
Template B is **narrowed rather than deleted** — it still covers any other reference-true inset
with no render behind it — and the standing tension is recorded in it rather than silently fixed:
ADR-021 removed post from this pipeline, so a `composite` step has no sanctioned route at all, and
this is one of six teaching files that still describe one. That sweep is a separate decision.

The other six teaching hits are left standing and named: `mapping/slot-rules.md` (routing tables),
`registry/argument-faults.md` (a recorded fault), `registry/types/05-persona-grid.md`
(`avoid_adjacent`), and the type's own file, its CHANGELOG and its worked example at v2.3, which
SPEC §3.3 keeps verbatim as the record of what rendered.

Consequences: `registry/types/05-social-handoff.md` → **2.6** — `version`, `generation_mode`,
the SKELETON's `[HANDOFF]` and `[INSET]` lines, new `PARTS/handoff`, `PARTS/inset` rewritten, and a
CHANGELOG entry. `adapters/nano-banana.md` Template B narrowed; `query/runbook.md` Step 3's
single-pass note corrected. `registry/index.yaml` regenerated, `dist/app-bundle` rebuilt. Warnings
31 → 30; the vocabulary countdown reads 1. No other type is touched, no session is re-routed,
`registry_version` unchanged, 0 errors.

## ADR-054 · 2026-08-26 · `03-spec-macro` may carry an inset, and the boundary with `--detail` is direction

Owner instruction, twice: this type may have an inset. Its own file forbade one — `insets` sat in
the NEGATIVE list and the NOTES carried a 0.1 SCOPE RULING that deliberately EXCLUDED the
macro-as-inset observation `sha256:290dd7…` as belonging between this type and
`06-relief-hero --detail`, parked rather than merged. That is a recorded decision, so it is
reversed here with a render in front of it rather than edited away.

**The render says the two are not the same picture.** A knife-sharpener V-slot at macro scale with
a circular locator inset in the lower right: the macro keeps roughly three quarters of the frame
and the inset is a small whole-product view so the magnified region can be placed on it.
`relief-hero --detail` is the exact opposite — the SCENE keeps the frame and the magnified detail
lives inside the inset. Same two elements, opposite dominance. **The boundary was never furniture,
it was DIRECTION**, and the 0.1 ruling parked the observation because it could not name that.

**What the reversal does not do, checked rather than assumed.** It does not supply the fifth
exemplar promotion criterion 1 needs. `sha256:290dd7…` is already counted inside this type's four,
so un-excluding it from the scope ruling adds nothing to the count. Criterion 1 stays at 4 of 5 and
that gap closes only through `ingestion/runbooks/classify-batch.md` over the market corpus, never
through this library's own output (SPEC §6.4, ADR-025).

**The same round closed the gap that mattered more.** The three 0.1 exemplars were single
homogeneous surfaces — braided steel, ground steel, diamond grit — where the LIGHT BEHAVIOR LAW
alone carries the frame. Build quality is a claim about ASSEMBLY and none of them had one. Three
renders on complex products all read as a fit between materials: a machined housing meeting gear
steel along a visible line, three distinct finishes on one chain link so it reads as parts rather
than a stamping, and the carbide-to-polymer join above. That is the type's PURPOSE tested for the
first time.

**Rule 6c sweep.** `adr-sweep.py 03-spec-macro` returns 21 hits across 6 files, ONE of them
teaching — this type's own file, which is the subject. One UNCLASSIFIED hit,
`eval/golden/fixture-002/expected-routes.yaml` line 110, reads "03-spec-macro is staging at 4/5
exemplars" and **is still true**, so it stands. The rest are records: the ledger, the observation
corpus and a routed session.

Consequences: `registry/types/_staging/03-spec-macro.md` → **0.2** — `insets` leaves the NEGATIVE
list, the NOTES gain the direction rule, the 0.1 SCOPE RULING is marked superseded, version and
skeleton bumped, CHANGELOG entry. No active type is touched and `06-relief-hero` is not edited:
its `--detail` mode is unchanged and the distinction is stated from this side only. Nothing is
promoted — SPEC §6.3(3) still wants the owner's verdict. `registry_version` unchanged.

## ADR-055 · 2026-08-26 · An inset is sized by maximisation, because two fixed numbers failed at it

Owner rule, stated as general: an inset must be size-optimised — as large and as clear as possible
without covering the subject. It goes into **G10** rather than into the three type files that
carry insets, because it is medium-independent and type-independent, which is G10's own stated
reason for existing.

**Two fixed numbers already failed, one round apart, in the same type.** `05-social-handoff` 2.6
bound the PANEL at 15-20% of frame width. 2.7 moved the bound to the PRODUCT inside the panel, for
the correct reason that a panel carries margin. Measured with a detector calibrated before any
live number was believed — planted discs at 10, 20 and 30% of frame width read back as 10.0, 20.1
and 30.1 — six panels then rendered between 16.6% and 31.1%, broadly compliant with both versions,
and the owner still read several as too small.

**So panel size does not predict legibility, and the thing that does cannot be measured.** What
separates a legible inset from a small one is whether the product FILLS its panel: a circle whose
product filled the disc read at 25.4%, while a compliant 16.6% rectangle carried a sliver between
wide margins and a 21.2% disc carried a small silhouette. The obvious instrument would be a
product-to-panel ratio, and it is not available — two attempts to measure it failed their own
controls in earlier rounds and are recorded there as failures rather than as evidence.

**Maximisation needs no measurement, which is why it is the rule.** It is also directionally
supported: across ten inset renders every miss was too small except one panel that was too large
AND misplaced, which this clause forbids anyway because covering the subject stops the growth.

**It composes with G10 rather than contradicting it.** G10 already says that when content does not
fit the safe area, make it SMALLER — that is what to do when it does not fit. This says what to do
with the space you have. Grow until the subject, a face or the safe area stops you; if it still
does not fit, shrink rather than move.

**Type-level bounds are not overridden.** `06-relief-hero` line 266 states 15-25% of frame width
and `03-spec-explode` line 115 states 30-40% for its `inset` FRAMING mode, which is a packshot
layout rather than a locator. Neither is edited: this clause tells a writer how to choose within a
range, not what the range is. `06-relief-hero` belongs to another lane and its insets have their
own evidence; nothing here asks that lane to change.

**Rule 6c sweep.** `adr-sweep.py inset` returns 1541 hits across 80 files, 15 of them teaching —
too many to correct and, since this is an ADDITION rather than a withdrawal, none of them made
wrong by it. The targeted question is which files state a FIXED inset size that this clause would
contradict, and a scan of every type file, `rules.md`, the adapter and the runbook finds exactly
the two named above. Both stand.

Two type files change in the same commit for reasons this clause creates.
`05-social-handoff` → **2.8** drops its own number and points at G10, and states that BOTH
placement conditions bind: 2.7's relationship wording worked, 2 of 4 clean against 3 of 4
misplaced at 2.6, and each of the two misses honoured quiet ground while dropping "beside the
moment". `_staging/03-spec-macro` → **0.3** applies it to the locator, whose only job is to let a
reader place the magnified region and which failed at that twice while the macro around it was
correct.

Consequences: `registry/rules.md` G10 gains the sizing clause; `registry/types/05-social-handoff.md`
→ 2.8; `registry/types/_staging/03-spec-macro.md` → 0.3; `registry/types/_staging/03-use-grid.md`
→ 0.4 for an unrelated finding in the same round. `registry/index.yaml` regenerated,
`dist/app-bundle` rebuilt. No other type edited, no session re-routed, `registry_version`
unchanged, 0 errors.
## ADR-056 · 2026-08-26 · The gif type goes back into the filename, and one-per-type goes back to being a rule

Owner instruction, 2026-08-26: the gif filename is `{page-type}-{gif-type}-{product-slug}-v{NN}.mp4`.
This reverses the NAMING half of ADR-051 and restores ADR-037's form. Everything else ADR-051
decided stands untouched: the loop replaces the whole slot asset, no still reserves an empty
block, `form` is `whole-frame` or `none`, `kind` equals `type_id`, delivery is mp4/webm muted,
and the spec block is the delivery format.

**What the two names trade, stated once so the next reversal can weigh it.** The type-name
tells the reader the ARGUMENT and — since the library folders are named by type — tells the
editor which folder the file belongs in without opening anything; the slot join lives in
`prompts.json` and on the plate. The slot-name told the reader which slot the file fills and
made the name unique by construction; the argument lived in `gif.type_id`. The owner has
chosen the argument and the folder over the slot join. The reversal is cheap today for a
reason worth recording: `ingestion/gifs.jsonl` holds 0 records and 0 loop files exist, so no
filed file is renamed — the no-rename law is not touched, because nothing has ever been filed.

**The uniqueness consequence is not optional.** With the slot out of the name, two loops of
one gif type on one page produce the same file. ADR-037's protection therefore returns with
ADR-037's name: **one loop per gif type per page is a RULE again**, demoted to a preference
for two days by ADR-051 and restored here. A page 193 build check enforces it, and the ADR-050
interaction ADR-051 celebrated — a `mechanism` loop on `content.1` and another on `content.3`
— is again illegal on one page. Page 193 itself is unaffected: its three loops are three
distinct types.

**ADR-051 left a teaching contradiction, found by this reversal's sweep.** `registry/rules.md`
G12's header block still showed `{page-type}-{gif-type}-{product}-v{NN}.mp4` — the old form,
using `{product}` where every other surface writes `{product-slug}`, which is why ADR-051's
sweep term `gif-type}-{product-slug` never matched it. For one day rules.md taught the type
name in its header and the slot name three paragraphs down. The header becomes correct again
today by accident of direction; the variance that hid it is normalised to `{product-slug}` so
the next sweep matches. This is the fourth distinct mechanism by which a teaching line has
survived a sweep (ADR-020 schema description, ADR-039 duplicate definition, ADR-050 line-wrap,
now placeholder variance), and the lesson is unchanged: the sweep is a checklist generator,
and reading the section top to bottom is the check.

**Rule 6c sweep.** `slot-id}.mp4`: 5 TEACHES — SPEC.md:177, schema (both `output` sites, which
carry an identical description; both edited), runbook:336, gif-instruction:52, rules.md:330.
`SLOT appended`: the same surfaces. `one loop per gif type`: 5 TEACHES — the PREFERENCE
sentences in SPEC.md:180, runbook:346, rules.md:341, gif-instruction:72, and the schema
descriptions. Every hit is edited by this ADR; the RECORDS (decisions/log.md, page 193's
first-form build.py history) stand as history.

**Consequences.**

1. `registry/gif-instruction.md` §4: the name template, the example, the ONE-name paragraph
   and the uniqueness paragraph — rule restored, slot out, type in.
2. `SPEC.md` §3.6: the naming sentence and the one-per-type sentence.
3. `registry/rules.md` G12: the filename paragraph, the two-things-not-in-it paragraph (the
   slot joins the page id on that list), the one-per-type paragraph, and the header block's
   `{product}` normalised to `{product-slug}`.
4. `query/runbook.md` Step 5c: the `gif.output` paragraph, the one-per-type paragraph, and
   the spec-block example filename.
5. `query/output.schema.json`: the `output` description at BOTH gif sites (slots and
   recommended — the ADR-039 duplicate is real here and both are edited).
6. `query/sessions/listicle-arm-trainer-hydraulic-v01`: `gif_name()` takes the gif type
   again, the three outputs rename, check 13 follows, and a new check fails two loops of one
   type on the page. The three plates regenerate with the new names. This session is
   migrated rather than grandfathered because its names lived under ADR-051 for two days,
   reference no filed file, and leaving them would teach the retired form from the newest
   session in the repo.
7. `scripts/gen-plate.py` and `scripts/gen-gif-cards.py` are untouched: neither parses the
   filename, both carry it as an opaque string.

---

## ADR-057 · 2026-08-26 · `03-spec-macro` promotes at 4 exemplars, because the owner overrode the count

**Context.** SPEC §6.3 opens with "All four required" and criterion 1 is "≥5 distinct
exemplars (distinct sources, non-near-duplicate) in the ledger". `03-spec-macro` has 4,
measured from `ingestion/observations.jsonl` at promotion time: `sha256:1fe139…` (10-F),
`sha256:ffcabb…` (11-A), `sha256:290dd7…` (11-E), `sha256:3ca14a…` (11-F) — 4 hashes across
4 distinct batches. Earlier this session I checked whether reversing the type's own SCOPE
RULING would admit a 5th and it does not: the contested inset-form exemplar `sha256:290dd7…`
is already inside the four. The count could not be raised by any reading of the evidence.

The owner tested the type and instructed: promote it.

**Decision.** `03-spec-macro` goes to 1.0 active. Criterion 1 is **waived by the human gate,
not met.** The type file says so in its own header and CHANGELOG, in the words "the owner's
explicit override", so that a curator reading the file in six months does not infer that five
exemplars were found.

**What the override does not touch.** SPEC §6.3 is unchanged and still reads "All four
required" — this is one type's exception, recorded, not a new bar for the library. The next
staging type at 4 exemplars is still short. Criteria 2, 3 and 4 were not waived and were run:

- **(2) router-confusion** — 0 of 14 routed slots stolen across both golden fixtures. **This
  is a hollow green and is recorded as one.** `03-spec-macro` is `channels: [marketplace]`;
  the fixtures are landing-page and advertorial. It could not contest a slot because it was
  never eligible for one. The criterion is satisfied as written and untested in substance.
- **(3) ≥1 rendered worked example** — six renders exist. WORKED EXAMPLES now carries the
  ratcheting-screwdriver pawl-and-gear fit, owner verdict `pass`, replacing a
  `drill-shear-gearhead` draft that was written but never rendered.
- **(4) ADR-007 autopilot** — this commit.

**The precedent this is NOT.** `03-spec-explode` promoted 2026-08-12 with criterion 1
"recorded MET at 5 exemplars by owner ruling over the caveat two of them carry" (ADR-014,
that file's 0.2 CHANGELOG). There the owner ruled on the QUALITY of two borderline exemplars
and the count reached five. Here the count stays at four and the criterion itself is set
aside. A reader comparing the two should not flatten them into one habit: one is a judgement
about evidence, this is a waiver of a requirement.

**A gap this promotion was expected to close and did not.** `eval/golden/fixture-002/expected-routes.yaml`
carried `known_gap`: "story-4 (durability, ABS housing) has no slot here because no active type
argues build quality; 03-spec-macro is staging at 4/5 exemplars. Add a durability slot to this
fixture when it promotes." That instruction cannot be followed. The fixture is advertorial and
this type is marketplace-only, so a durability slot added there would route to nothing. The note
has been rewritten to say what the gap actually needs. **This is the second time a channel field
has silently voided a routing expectation** and it is worth watching for a third: a fixture note
that names a type by id, without checking that type's `channels` against the fixture's own, is
writing a cheque the router cannot cash.

**Consequences** — rule 6c sweep on `"exemplars"`: 84 hits, 32 files, 14 in TEACHES. Accounted:

- `SPEC.md:236` and `ingestion/runbooks/curate.md:35` teach "≥5 exemplars" as the promotion
  bar. **Both stand unchanged** — this ADR overrides one application, not the rule. Changing
  SPEC here would convert a one-off owner call into library law, which is exactly what the
  override was not.
- `decisions/log.md` ADR-000 records the same "≥5 distinct exemplars" in the founding
  governance decision. Stands, same reason; append-only besides.
- `registry/types/03-spec-macro.md` was the one file teaching the opposite: its header read
  "STAGING DRAFT … 3 exemplars ledgered … Not routable" while the type went active. Rewritten
  in this commit. This is the miss rule 6c exists to catch and the sweep caught it.
- `03-spec-explode.md`, `03-mechanism-xray.md`, `05-social-snapshot.md`, `03-use-grid.md`,
  `01-pain-split.md`, `03-spec-split.md` and the `_staging/` files record their own exemplar
  counts as history or as their own pending state. Untouched, none made false by this.
- GENERATED (`registry/index.yaml`, the app bundle) regenerates in this commit.

---

## ADR-058 · 2026-08-26 · Every image slot carries three options of three DISTINCT types

**Owner instruction, 2026-08-26:** "đối với mỗi slot ảnh, cần đúng 3 type ảnh khác nhau,
phù hợp nhất với content của slot đó" — every image slot carries exactly three different
image types, the three that fit that slot's content best.

**Context: the old model spent B and C on the same type as A.** Step 4 since ADR-000 read
A = baseline, B = a different type OR an axis, C = *the same type and axes as A in a
different execution*. C was defined as a re-execution, and it was the option that made the
"3 per slot" guarantee cheap to keep. Measured across all 13 routed sessions before this
decision — **161 image slots: 111 carried one distinct type, 50 carried two, and not one
slot in the library's history carried three.** Across every option ever emitted,
`varies_on` was `execution` 103 times, `baseline` 90, `type` 44, `axis` 28. A slot that
returns one type three ways has answered a different question than the one the owner asks
when he picks.

**Decision.** A, B and C become a RANKING, not three dimensions of variation. Rank the
whole channel-legal candidate set by the five Step 4 criteria, FIT first, and take the top
three DISTINCT types. Each option then chooses its own best variant, axes and execution —
those are how an option is built, never how the pool is filled. `varies_on` is `baseline`
for A and `type: <id>` for B and C.

**The pool was never the table cell, and this repo said so in two places at once.**
SPEC §7.4 has always read "Stage 1 derives from the whole channel-legal set, not from one
table cell, so exhausting a cell is not exhausting the registry", while `query/runbook.md`
Step 2 read "That cell is the candidate list." The second sentence is why three types
looked impossible: **43 of the 48 role×channel cells hold fewer than three types.** The
cell is now written as what it always was — a PREFERENCE ORDER. Cell members outrank
non-members at equal fit; a non-member is a candidate, not a violation. This resolves a
contradiction rather than creating one.

Per-channel ceilings, measured from the index at decision time: landing-page 14 active
types legal, marketplace 13, advertorial 10, **paid-social 5**. Three of four channels
carry the rule comfortably. Paid-social will produce real shortfalls.

**A shortfall is a declared state, not a failure.** Fewer than three surviving types →
emit what exists and set `pool_basis` on the slot, naming which gates fired, which
`avoid_when` excluded a candidate, and how wide the channel was. Naming a cell is not
sufficient, because the cell is not the pool. `single_type_basis` is the retired name for
the same field, still read so the thirteen existing sessions parse.

**The cost, stated now rather than discovered later.** On a slot whose cell holds one type,
B and C will be types the table never proposed for that beat: legal — the admission test
never bends, `channels` must contain the channel and `avoid_when` must not exclude the case
— but a weaker argument for it. That is the trade the instruction buys, and it is the right
way round: a weaker third type the owner can reject beats a third camera angle on the same
type he cannot compare.

**ADR-022 is amended by a distinction, not reversed.** A repeating section — a review wall,
a roundup, a gallery of equivalent cells — emitted ONE option per slot because three options
per tile opened a door no check can close: each option is legal alone, and a reader picking
one register on three tiles and another on three gets a wall that reads as two shoots, which
reads as fake. **That harm is mixing types WITHIN one set, and offering three types FOR the
whole set does not cause it.** So the SECTION carries the three type options, every tile
follows whichever the owner picks, and no tile is individually switchable. ADR-022's evidence
and its reasoning both survive intact.

**The ladder now runs until three types stand, not until one does.** Its old rungs 3 and 4 —
"a repeating-section repeat" and "another execution of a type already on the page" — yield no
NEW type, so neither can fill a three-distinct-types pool. They are removed from the pool
ladder and kept where they belong: the honest way to satisfy `one-type-once` in the recommended
SET when a page needs the same type twice. Rung 3 is now "the rest of the channel-legal set,
ranked by fit", which is where the third type will usually come from.

**Two active types had no cell in the table at all.** `03-spec-macro` and `03-use-grid`
promoted this same day and were never added to `mapping/slot-rules.md`, so under the
cell-as-pool reading they were **unroutable from the moment they went active** — promoted
types no slot could propose. Found by counting cell widths for this decision, not by any
gate; nothing checks that an active type appears in the table. Both are now placed:
`03-spec-macro` in mechanism/marketplace, `03-use-grid` in how-to-use/marketplace and
landing-page. **A gate for this is the obvious next thing to build and is not built.**

**Enforcement.** `scripts/validate.py` `check_option_pools` moves its threshold from one
distinct type to three, reading `pool_basis` or the legacy `single_type_basis` as the
declaration. It was fed six known-bad and known-good inputs before being believed — 1 type
no basis, 2 types no basis, **3 options carrying only 2 types** (the case the old gate
passed), 3 distinct types, 1 type with `pool_basis`, 1 type with the legacy field — and it
discriminated on all six. All 13 existing sessions are grandfathered: they carry 155 slots
below three types between them and every one would fail.

**Consequences** — rule 6c sweep on `"varies_on"`: 523 hits, 48 files, 7 in TEACHES, 2
UNCLASSIFIED. Accounted:

- `SPEC.md:278` taught "3 per slot, each differing on a named dimension — `type`, `axis`,
  or `execution`". **Rewritten**: three per slot, each a distinct type. The never-empty
  rule beside it is unchanged and now names three as the target.
- `query/runbook.md` — Step 2, Step 4, the ADR-022 paragraph, the one-type-once paragraph,
  the enforcement paragraph and the ladder. **All six rewritten in this commit.**
- `query/output.schema.json` — `varies_on` guidance, the never-empty description, and the
  field rename. **Rewritten.**
- `mapping/slot-rules.md:69` teaches cross-slot rule 2, that a type may repeat across a
  repeating section's entries. **Stands** — it is about the recommended set, not the pool,
  and the ADR-022 amendment leans on it.
- `eval/golden/fixture-001` and `fixture-002` (the sweep's two UNCLASSIFIED hits) asserted
  the old model in five places, including `cause-1`'s "options B/C must vary on execution …
  not type" — the exact instruction this ADR reverses. **All five rewritten in this commit
  per SPEC §9.** The fixtures did their job before any prompt was written: adding
  `03-use-grid` to the how-to-use cell failed `howto-1`'s `only_legal_type` assertion
  immediately. That key is renamed `only_preferred_type`, because it checks the CELL and
  "only legal" is now false of every cell.
- `registry/gif-instruction.md:42`, `registry/gif-types/cause.md:37`, `gif-types/proof.md:42`
  use `varies_on` for the GIF layer, where it names how a motion execution differs and
  argues AGAINST minting a new gif type for a subject-class change. **Untouched and still
  true** — a gif is a work order sitting below option C, not an option in the pool. The
  `cause.md` note citing "page 65's rung-2 route" stays valid: rung 2 survives.
- GENERATED (`dist/app-bundle/`, `registry/index.yaml`) regenerates in this commit.

---

## ADR-059 · 2026-08-26 · Channel stops being an admission test; the copy decides

**Owner instruction, 2026-08-26:** "bỏ các giới hạn của channels, tôi đang xây hệ thống
library: image types để sử dụng cho tất cả các loại trang, khách có thể dùng template của
advertorial nhưng viết nội dung cho listicle. chính vì thế nên copy sẽ là thứ quyết định."

**Context.** `channels` was one half of the admission test the runbook said never bends: a
type whose `channels` did not contain the page's channel was refused at any rank. Two facts
killed that.

The first is the owner's design: this is a library of image types for ANY page kind, and a
customer may take an advertorial template and write listicle copy into it. The page's KIND is
therefore not knowable from its template.

The second was already true and nobody had said it. **The router never read a channel; it
guessed one.** `content.json` carries `channel`, but the export carries `lpTypeId`, and the
mapping `listicle → advertorial` is a convention held by five sessions running, not a
declaration. So the one test that "never bends" was keyed on a derived guess about a surface,
while `avoid_when` — the other half — is keyed on the CASE, which is what the copy carries.

**Measured cost of the gate, on one real page.** The angle-grinder listicle (TPL-ADV21/19)
has four slots whose copy names an argument the library owns and the gate refused:

| slot | what the copy argues | type that fits | why it was refused |
|---|---|---|---|
| reason #4 | cheap resinoid wheels chip and crack under side load | `03-spec-macro` | `channels: [marketplace]` |
| reason #3 | flat pads dig rings on a curve; separate profiles exist | `03-use-grid` | not on advertorial |
| `product_end` | Flat, Bevel, Bow · 100mm and 85mm | `03-use-grid` | not on advertorial |
| `product` | Solid Wear-Resistant Steel · Tungsten Carbide Teeth | `03-spec-macro` | `channels: [marketplace]` |

Four slots, two types, one ordinary page.

**Decision.** Admission is ONE test: `avoid_when`. The candidate pool is **every active
type** — all 17, for every slot on every page. `channels` stays in frontmatter as
PROVENANCE (where a type's register has been proven) and is still validated against the
vocabulary; nothing reads it to admit or refuse an image type.

**`mapping/slot-rules.md` collapses from 48 cells to 12 rows.** With channel out of the
admission test the four columns were the same preference written four times. One row per
role, best type first. This is also what makes the library scale: a new type joins ONE row,
not four columns.

**The two 2026-08-11 channel trims are preserved, not deleted.** Both were real decisions
with evidence, and both were statements about the CASE wearing a channel's clothes:

- `02-symptom-rail` off advertorial, because the infographic-tile aesthetic "signals cheap
  goods off-marketplace". Moved into **that type's own `avoid_when`**, phrased against the
  page in hand — an EDITORIAL page, prose rather than a product listing — where FIT reads it.
- `06-relief-scene` off landing-page, because its `use_when` names only "an advertorial or
  final frame of an ads creative". **No edit needed**: `use_when` IS criterion 1 of the
  ranking, so that beat scores low on FIT by the type's own words. The wall was redundant.

**GIF types keep their `channels` and are untouched.** There it does a different job:
`registry/gif-types/unboxing.md` states "This type is not routable to a page slot, and its
`channels` list is the enforcement." Removing it there would make an unroutable type
routable. This ADR is about image types only.

**What gets worse, stated rather than discovered.** `channels` was the last cheap mechanical
filter. Every slot now ranks 17 types by judgement, and judgement does not scale and no regex
audits it. Two mitigations, both cheap: `use_when` becomes the load-bearing sentence in every
type file and is worth an audit pass of its own; and every role assignment should cite the
sentence of copy that decided it, which turns a judgement into a record. `pool_basis` becomes
nearly dead — with 17 candidates, three distinct types is always available.

**Enforcement, and the check that was missing.** `check_slot_rules` loses the
channel-vs-frontmatter comparison (a type can no longer contradict its own frontmatter by
being listed under a role) and gains the opposite check: **every active type must appear in
at least one row of the preference table.** That table is now the only place a type declares
which beat it belongs to. The gate was fed known-bad input before being believed — a live
file (silent), one type removed (fires, names it, count 1), a second removed (count 2),
restored (silent). An earlier control run reported a false mismatch: it removed
`04-proof-lockedframe` from `proof`, which left it listed under `comparison` as
`--verdict`, so the gate was right and the control was wrong.

**Consequences** — rule 6c sweep on `"channels"`: 188 hits, 88 files, 31 in TEACHES, all read:

- `SPEC.md:263` taught "(a) channel legality — the slot's channel appears in the type's own
  `channels`". **Rewritten.** `SPEC.md:131/168/194` describe the frontmatter field and the
  closed vocabulary; both **stand** — the field still exists and is still validated.
- `query/runbook.md:47/116/217` — the pool, the admission rule, and the ladder's admission
  line. **All three rewritten.**
- `query/output.schema.json:4` — the NEVER-EMPTY description named "channel legality from
  each type's own channels". **Rewritten.**
- `mapping/slot-rules.md` — table collapsed, the trims rehomed, the new gate documented.
- `registry/gif-types/*.md` (6 files) — **untouched by design**, see above.
- `registry/types/*.md:10` — every type's `channels:` frontmatter **stands unchanged**. Zero
  type files edited for the gate itself; `02-symptom-rail` was edited to receive its own
  register rule, and `03-spec-macro`'s promotion note was updated because it explained
  criterion 2's green result BY the exclusion this ADR removes.
- Every `channels gain …` line in a type CHANGELOG — history, append-only, **stands**.
- `adapters/nano-banana.md:293` — "One base cannot serve two channels" is a RENDER note: a
  marketplace image without marks and a landing-page image with them are two renders. It is
  about producing images, not admitting types. **Stands.**
- `eval/golden/fixture-001` and `fixture-002` — three `only_preferred_type` assertions became
  false the moment the columns merged, and the fixtures caught all three on the first run.
  **All three rewritten in this commit per SPEC §9**, each recording where the old exclusion
  now lives. `story-3-howto` is the first assertion in either fixture that this change turns
  from a refusal into a choice: `03-use-grid` is now a real alternative to `03-use-sequence`.
- GENERATED (`registry/index.yaml`, `dist/app-bundle/`) regenerates.

---

## ADR-060 · 2026-08-27 · `avoid_when` is removed from every image type; `use_when` carries the whole trigger

**Owner instruction, 2026-08-27:** "tôi muốn bỏ hết avoid_when của các type do content sẽ
linh hoạt, ảnh sẽ route/bắt theo content thay vì landing page type."

**Decision.** `avoid_when` is deleted from all 20 image type files — 17 active and 3 staging,
6534 characters removed. `TRIGGER` now carries `use_when` alone. `scripts/validate.py` no
longer requires the block and still reads one if a file carries it, so a lane mid-edit does
not break. **GIF types keep theirs and are untouched**, the same carve-out ADR-059 made for
`channels`: the gif layer routes by a different mechanism and nothing here was measured
against it.

**What this means, stated plainly: there is no admission test left.** ADR-059 removed
`channels` and left `avoid_when` as the last one; a day later that is gone too. Every active
type is a candidate for every slot on every page, and what a type is FOR is argued entirely
by `use_when` through FIT. A type is no longer refused — it is out-ranked.

**Four things still remove a candidate, and the routing does not become lawless:**

1. **Attribute gates** — deterministic kill-rules on `product.attributes`. On the first page
   routed after this, `body_contact: false` dropped `03-mechanism-ghostbody`.
2. **Ratio** — a type that does not declare the slot's ratio cannot serve it. Nine of ten
   slots on that page were 16:9 and the field fell from seventeen types to nine. Nothing in
   the repo enforces this yet, which is now the most valuable gate left unbuilt.
3. **Cross-slot frontmatter** — `never_with`, `pairs_with`, `avoid_adjacent`, one-type-once.
   All verified present in frontmatter before the deletion: `03-spec-explode`'s
   `avoid_adjacent: [03-mechanism-xray]`, `01-pain-scene`'s `never_with: [01-pain-split]` and
   `06-relief-scene`'s `pairs_with: [01-pain-scene]` are the three the live routing used, and
   all three were in the frontmatter, not only in the prose being deleted.
4. **`registry/rules.md`** — the global rules.

**What the deleted prose actually contained, measured before deleting it.** 20 types, and
most clauses were not about page type at all: `02-cause-anatomy`'s "the harm PERSISTS after
the culprit is taken away", `04-proof-lockedframe`'s "the difference is invisible or only felt
in use", `03-use-grid`'s "the product does one thing — the grid becomes padding". Those were
craft warnings and they go. The library's answer to a badly-fitted type is now a low FIT score
and an owner who can see all three options, rather than a silent refusal.

**Two clauses did not go, because the files themselves call them illegal.** They are rehomed
as **G14** in `registry/rules.md`:

- `05-social-snapshot`: "NEVER pair a generated snapshot with a reviewer name, avatar, star
  row or verified badge … that is a fabricated endorsement (FTC)."
- `05-social-card`: "NEVER fabricate a quote, name, rating or counter — fabricated
  endorsements are illegal (FTC endorsement rules and equivalents)."

G14 is written to bind **the slot, not the type**, which is what the evidence says it always
was: what makes an image a fabricated endorsement is the furniture around it. A review block
carrying names and `Verified Purchase` badges turns any generated image into a claim a
customer took it. Measured the same day on `advertorial-cord-and-rope-tightening-and-cinching-tool-v01`:
four `reviews.shots.*` slots sit beside three named "Verified Purchase" quotes and route to
nothing, while TPL-ADV21's six review photo slots carry no name and no badge and are legal.
The slot decides.

**Consequences** — rule 6c sweep on `"avoid_when"`: 241 hits, 100 files, 30 in TEACHES:

- `SPEC.md:100` said TRIGGER contains both folded blocks — **rewritten** to name `use_when`
  alone. `SPEC.md:281` listed `avoid_when` in Stage 2 and `:322` said the picks prior never
  overrides it — **both rewritten**.
- `query/runbook.md` — the Step 4 admission paragraph and the ladder's admission line, the
  two places that made it a wall. **Both rewritten**, and Step 4 now lists the four things
  that do still remove a candidate.
- `mapping/slot-rules.md:5` named it in the Stage 2 sequence — **rewritten**, and the record
  of the two 2026-08-11 channel trims is corrected: `02-symptom-rail`'s rule lived in
  `avoid_when` for exactly one day.
- `scripts/validate.py` — the required-block check is now conditional for image types and
  unchanged for gif types; the index writer skips an empty field.
- `registry/gif-types/*.md` (6 files) — **untouched by design.**
- Every type CHANGELOG line mentioning `avoid_when` — history, append-only, **stands**.
- GENERATED (`registry/index.yaml`, `dist/app-bundle/`) regenerates in this commit.

---

## ADR-061 · 2026-08-27 · `06-relief-hero --detail` moves to 30-40%, and a bound no render obeyed stops being deferred to

**Owner instruction, 2026-08-27:** "sửa inset của 06-relief-hero --detail, tăng lên khoảng
30-40%."

**Context: the band was written, not measured.** `--detail` declared "15-25% of frame width"
and this type's own ledger contains every `--detail` render it has ever produced — three, all
2026-08-14, all `partial`. Their measured widths:

| render | width | the record's own words |
|---|---|---|
| automatic pet water fountain | 26% | "the smallest of the set and **the tightest to read**" |
| electric wine opener | 32% | "rendered as a slightly wide rectangle" |
| robot window cleaner | 42% | "the largest and **by far the most legible** of the three, and it costs the picture nothing because it sits in dead space" |

**Not one of them landed inside the declared band**, the band's ceiling sat below the width
already recorded as tightest to read, and legibility rose monotonically with size across the
set. None of the three `partial` verdicts was about inset size — all three failed on `[PLATE]`,
the reserved empty block ADR-051 has since retired.

**It also had to move for a second reason.** G10 gained a floor on 2026-08-26: the product
inside an inset is never smaller than a QUARTER of frame width, and "a type may raise that
floor and may not lower it". A 15-25% panel holding a product with a thin margin puts that
product under the floor, so the type was lowering a floor it may only raise. This was found
while routing page 219, where the contradiction forced `--context` and `--recall` to be used
instead of `--detail` and was recorded in that session's `page_composition_notes` rather than
quietly worked around.

**Decision.** `06-relief-hero` 1.18: `--detail` is 30-40% of frame width. That is where the
two readable renders sit, and it clears G10's floor with room for the thin even margin G10
asks for. It also matches `03-spec-explode`'s `inset` FRAMING band exactly, which was reached
independently.

**This corrects two places that cited the old number as settled law.**

- `registry/rules.md` G10 said "`06-relief-hero` line 266 says 15-25% … Neither is edited here:
  this clause tells a writer how to choose within a range, not what the range is." **Rewritten.**
  The deference was right in principle and wrong in this instance, and the paragraph now says
  why: a type bound that no render obeys is not evidence, and G10 was deferring to one.
- **ADR-055 stands as written and is superseded in effect.** It said "Type-level bounds are not
  overridden … `06-relief-hero` belongs to another lane and its insets have their own evidence;
  nothing here asks that lane to change." That was true on 2026-08-26 — the lane had not been
  asked. It has now, by the owner, and the evidence turned out to point the other way. The log
  is append-only and a later reader should see both.

**Untouched, and checked rather than assumed.** The gif-ratio decision at ADR-045 reasons that
"`06-relief-hero` draws `--detail` as a rounded rectangle or circle at 15-25% of frame width,
**which is square**, so a `--detail` loop delivers 1:1 whatever the slot is". The reasoning
rests on the SHAPE, not the percentage, and 30-40% is square in exactly the same way. That
decision is unaffected; only its cited number is stale, and it is a record rather than an
instruction.

**Consequences** — targeted sweep on `"15-25"` across `registry/`, `mapping/`, `query/` and
`SPEC.md`: after this commit every surviving hit is a RECORD of the band being retired — the
type's own note and CHANGELOG, and G10's correction. `SPEC.md:210` and `decisions/log.md:22`
match on "~15–25 images" per batch session and are unrelated. No instruction anywhere still
teaches the old band. `registry/index.yaml` and the bundle regenerate.

---

## ADR-062 · 2026-08-27 · G15 — a multi-frame layout packs a square instead of striping it

**Owner instruction, 2026-08-27, with a diagram:** for any image type with several frames — a
split, a sequence, a rail, a grid — at ratio 1:1 use a grid, a four-frame grid, or one
rectangle with two squares, the rectangle free to sit on any side, standing or lying.

**Decision.** G15 in `registry/rules.md`. At 1:1: two frames are HALVES, three are **1 + 2**
(one rectangle, two squares), four are **2×2**. Never N equal stripes.

**Why it is a real defect and not a preference.** Three equal vertical panels in a 1024 square
are 341px wide each, and everything this library draws — a person, a product on a surface, a
hand at a fastening — is wider than it is tall. `02-cause-anatomy` arrived at the same place
from the opposite direction: its KNOWN-FLAKY records two renders that duplicated a canvas into
a 2×2 grid when asked for a wide ratio on wide-and-short content, and its conclusion was
"compose wide-and-short subjects to fill a square frame".

**It names a family two types already belonged to.** `02-symptom-rail` is a hero at 72% with
three vignettes down the right edge; `05-persona-grid --1plus3` is one large cell with three
stacked beside it. Both are packs. G15 gives the vocabulary and makes it the default rather
than a per-type invention.

**Reading order and the side lock both survive.** The 1 + 2 form reads rectangle first, then
the two squares left to right, so a sequence keeps its order. Types that lock a side —
`02-cause-anatomy` and `01-pain-split`, wrong on the LEFT and correct on the RIGHT, locked
library-wide — carry two frames and take the halves form, where the lock is untouched.

### Two exemptions, and neither is a carve-out I invented

**`04-proof-lockedframe` cannot take the 1 + 2 form.** Its law is "no panel may be favoured —
no badge, no glow, no colour cue, no brighter exposure", stated four times in the file, and
line 137 says **the judgement rule IS the type**. A larger frame favours its panel by size,
which is the same defect in a different currency. At 1:1 it uses equal frames only: halves at
two, three equal HORIZONTAL BANDS at three, 2×2 at four.

**`03-use-sequence` is exempt from describing geometry at all.** Its `layout` part says "Never
describe the frame's shape or ratio", and gives a measured reason: "a prompt that reasons
about frame geometry leaves the model space to reconcile, and it fills that space with extra
small panels." A rule telling its prompt to draw a rectangle and two squares would cause the
exact fault that sentence exists to prevent. Its three stacked photographs already pack a
square as three wide bands. G15 asks nothing of it.

**`04-proof-lockedframe` 1.14 in the same commit.** Its `layout` said "N equal VERTICAL
panels" in the skeleton and in PARTS. That word was written when the type only reasoned about
wide ratios, where vertical is correct — every render it has ever produced ran wide. It now
says panels stripe across the frame's LONG axis, and that at 1:1 the orientation turns over.

**Consequences** — rule 6c sweep on `"vertical panels"`: 145 hits, 42 files, and **exactly one
in TEACHES**, which is the type corrected here. Its 4 hits split two ways: lines 47 and 61 are
law and are rewritten; lines 232 and 279 are inside worked examples and are **left standing**,
because those are records of renders that happened at wide ratios where "vertical" was right.
The 40 RECORDS files keep the term as history. `query/sessions/advertorial-cord-tensioner-cam-lock-v01`
carries it five times in the page-219 lockedframe prompts, all at 16:9, all still correct.
`registry/index.yaml` and the bundle regenerate.

**What this does not do.** It does not touch any type's frame COUNT, only the arrangement at
one ratio, and it does not enter a prompt as a ratio — the ratio stays a generation parameter
(adapter Rule 4). What a prompt names is the layout: "2×2 grid", "one rectangle above two
squares".

---

## ADR-063 · 2026-08-27 · No type is exempt from G15 at 1:1; the two carve-outs were 16:9 reasoning

**Owner correction, 2026-08-27:** "hai type được miễn là đối với 16:9, 1:1 thì bắt buộc dùng
layout khác để ảnh đủ thông tin."

**What ADR-062 got wrong.** It exempted `04-proof-lockedframe` and `03-use-sequence` from G15.
Both exemptions were reasoning about wide ratios wearing the clothes of a general rule. The
reason G15 exists is that a square starves each frame of information, and that reason does not
care which type is doing the striping.

**`04-proof-lockedframe` was never really exempt and the wording overstated it.** ADR-062
already had it changing layout at 1:1 — halves, three horizontal bands, or 2×2. What it may
not take is the UNEQUAL 1 + 2, because its own law is "no panel may be favoured" and the file
says the judgement rule IS the type; a larger frame favours its panel by size. That is a
NARROWER FORM of G15, not an exemption from it, and it is now written that way.

**1.15 adds what the correction actually asks for**: at 1:1, **two panels are the preferred
count**. Each half of a square carries four times the area of a third band, and this type's
argument is usually one variable across a before and an after. Three only when the argument
needs a third state. That is where "đủ thông tin" is won for this type — in the panel COUNT,
because the equal-frames constraint leaves no room to win it in the shape.

**`03-use-sequence` was a misreading of its own rule, and mine.** Its layout part says "Never
describe the frame's shape or ratio", with a measured reason — a prompt reasoning about frame
geometry "fills that space with extra small panels". I read that as forbidding any layout
statement. But the same part's FIRST clause names an arrangement: "three photographs stacked
one above another". Naming an arrangement is what this part has always done. What the ban is
about is naming the FRAME — "square", "1:1", "a tall image" — which is the thing that leaves
the model something to reconcile.

**1.10 therefore takes the 1 + 2 pack at 1:1**: PREPARE across the top, USE and RESULT side by
side below, left to right. The order survives, which is this type's entire discipline. The
geometry ban is clarified rather than weakened, and the distinction is written into the part so
the next reader does not repeat the misreading.

**Nothing already routed changes.** The one 1:1 multi-frame option in
`advertorial-cord-tensioner-cam-lock-v01` is `05-persona-grid --2x2` at `product.image`, which
is a G15 pack already. Every `04-proof-lockedframe` prompt in that session sits on a 16:9 slot
where vertical panels are correct. Checked rather than assumed; no re-export.

**Consequences.** `registry/rules.md` G15's exemption section is replaced. Both type files are
edited and versioned. ADR-062 stands as written — the log is append-only and a later reader
should be able to see the correction as a correction. `registry/index.yaml` and the bundle
regenerate.

## ADR-064 · 2026-09-03 · G16: a type may declare a text layer, and G6 narrows for that type alone

**Owner decision Q1b, 2026-09-03:** advertising images for product pages carry their text
INSIDE the file rather than as page HTML overlaid on a clean render. This ADR is that
decision landing as law, built on two founding render rounds rather than on the market
corpus.

**The recommendation was the opposite and it is recorded rather than smoothed over.** The
advisory case for HTML overlay was the catalogue: 179 pages over 70 products across English,
German and UK domains, and a still with words serves only the pages in its own language. The
owner chose baked text with that on the table. G16 carries the cost as a stated clause
instead of hiding it, the same treatment ADR-008 gave a decision taken against advice.

**What the two rounds measured.** Seven renders, four types, 2026-09-03.

- **Spelling is not the problem.** 12 of 12 lines exact, then 13 of 13. With G12's retired
  20 of 20 the seven-word line cap now rests on 45 lines and none has ever misspelled.
- **The old G12 fault does not recur.** Every plate the library produced under model-drawn
  G12 was cut by a frame edge, 3 of 3. Here 0 of 7 are cut. Naming the empty region the
  words sit on, rather than telling the model to avoid the edges, is what the old prompts
  were missing.
- **The cluster budget was set far too low and the correction inverted the hypothesis.**
  Round 2 ran one type at two budgets on two products. The FIVE-cluster frame returned all
  five once each; the TWO-cluster frame drew its whole block a second time, seven ink bands
  where four were asked for. What binds is not the count, it is whether the reserved area is
  filled — the mechanism `adapters/nano-banana.md` Rule 4 already records for panels.
- **"Left aligned" is a term of art the renderer ignores.** 1 of 3 in round 1. Written as an
  observable — every line begins at the same distance from the left edge — 4 of 4 in round 2.
- **The bottom-right corner belongs to the tool's watermark** (ADR settled at `4eb327b`).
  Three of three badges placed there were struck through; four of four bottom-left were clean.

**G10 is breached and G16 says so out loud.** Round 1 asked politely and eight inked edges
measured 5.3–7.4%. Round 2 asked for a tenth of the picture clear and nine edges measured
6.7–7.3%. Over-asking moved the floor from 5.3% to 6.7% and moved nothing else; this renderer
holds a house margin near 7%. Nothing was cut either round. G16 keeps asking for a tenth
because that is what produced the higher floor, and states the breach rather than quietly
lowering a global rule a type may only raise. Two ways out are named and neither is taken:
ask for a sixth, or amend G10 for text blocks on 17 measured edges. This is ADR-061's shape —
a bound no render obeys is not evidence.

**The content half is the half a re-render cannot fix**, and it is where G16 spends most of
its words. Text comes from `content.json` and nowhere else, the same law `specification` and
`colorways` already carry. Five classes are refused by name: an endorsement (G14), a
certification mark or expert byline (G6's logo ban plus the empty `author` row), a price or
date, a claim the page's own copy does not make, and a second language.

**Consequences** — rule 6c sweep on `"G6"`: 244 hits, 79 files, **30 in TEACHES, all read**.

The narrowing is conditional on a frontmatter key, and **no type in the registry declares
`text_layer` today**, so every existing statement of G6 is still true as written:

- `registry/rules.md` — G6 itself. **Rewritten**, with a second scope note bounding the
  narrowing and naming `watermark`/`logo`/the product clauses as unbendable. G7's scope note
  is **rewritten** too, to permit `exempt_from: [G7]` for arranged product photography where
  the arrangement is the argument.
- `registry/types/*.md` (17 files) and `registry/types/_staging/*.md` (3) — every one states
  G6 in its own `NEGATIVE` block or in a slot note. **All stand**: none declares a text layer,
  so none is narrowed. `05-social-card` is the interesting case and it stands too — it is
  G6-exempt outright for its review card, which predates G16 and is a broader carve-out than
  G16 grants; converting it is a separate decision on that file's own audit.
- `registry/gif-types/*.md` (6) and `registry/gif-instruction.md` — **untouched by design**,
  the same carve-out ADR-059 and ADR-060 made. A loop carries no words and `text_layer` is an
  image-type key; a motion asset that reaches every clone of a product in every language is
  exactly where baked text costs most.
- `adapters/nano-banana.md` — 6 hits. Rules 1, 1a, 5 and 7 describe how the negative list is
  translated and what this renderer does with characters. **All stand**; the adapter is about
  production and G16 is about permission. Rule 7's "a mark that needs a word is not a mark, it
  is a callout, and it leaves the render" is the one line that will need revisiting when a
  type actually ships a text layer, and it is left standing today because none does.
- `query/runbook.md` — 3 hits: the tie-breaker's own G6 label (unrelated, a decision id), the
  NEGATIVE composition line, and the plate note. **All stand.**
- `dist/app-bundle/` (11 mirrored files) — **generated**, regenerated in this commit.

`scripts/validate.py` gains `text_layer` in `OPTIONAL_KEYS` and checks each slot against
`title | copy | badge`. The gate was fed known-bad input before being believed: an illegal
slot fired and named it, a legal list was silent, and the borrowed file was restored.

`registry_version` unchanged — no type file, no data and no structure moves in this commit.
G16 binds nothing until a type declares the key, which is the next commit's business.

## ADR-065 · 2026-09-03 · Five product-page candidates enter staging, and step 7 is not a Trust Ladder rung

A curation pass over 204 observations, run after batches C and D added 54 records from the
direct-response corpus. Five new-type clusters clear `curate.md` §3's bar for a staging
draft. Nothing here is routable and no active type is touched.

**The five, with the counts generated from the ledger rather than typed:**

| id | obs | distinct sources | renders |
|---|---|---|---|
| `07-identity-pack` | 6 | **4** — millbrook, halden, standfast, redpine | 0 |
| `03-spec-stilllife` | 8 | 3 — millbrook, halden, standfast | 3 |
| `03-spec-lineup` | 2 | 2 — holloway, hushedsocks | 1 |
| `06-relief-claimstack` | 2 | 2 — mida-fernwell, redpine | 2 |
| `07-identity-inhand` | 1 | 1 — supply-se | 1 |

**`07-identity-pack` at four sources is the furthest any proposal in this ledger has
reached**, and the four cover four pack formats — carton with sachet, amber jar, capsule
bottle, stand-up pouch — rather than four photographs of one idea. One more source clears
criterion 1.

**Step 7 is new and it is deliberately NOT a Trust Ladder rung.** `vocabulary.yaml` says the
step number sorts the gallery and names a beat in the persuasion arc; identity is not a beat,
it is what the object is. The comment in the vocabulary says so and names the consequence:
`query/runbook.md` Step 5b's coverage pass counts rungs 1-6, and it must not read an absent
step 7 as a gap. An advertorial with no packshot is not missing anything.

**Staging defers the routing question rather than answering it, and that is the point.**
Since ADR-060 there is no admission test left: an active type is a candidate for every slot
on every page, and `use_when` is the only thing keeping a packshot out of a pain slot. Both
identity files therefore carry a `use_when` written to refuse rather than to attract — *"NEVER
for a slot whose copy argues anything"* — and both say in their header that the choice between
`registry/types/` under a new step and a separate namespace like `registry/gif-types/` belongs
to the promotion diff. Nothing under `_staging/` routes, so the decision costs nothing today
and cannot be skipped later.

**Three renaming and re-filing decisions, recorded so a reader of the ledger is not confused
by two names for one thing:**

- The ledger's `03-spec-ingredient` and this file's `03-spec-stilllife` are ONE proposal. A
  `device` is the visual MECHANISM, not the subject: "ingredient" names what is photographed,
  "still life" names how the argument is made. The rename earns the vocabulary entry twice,
  because batch B also proposed `02-cause-stilllife` — same mechanism, different job, exactly
  as `split` already serves both `01-pain-split` and `03-spec-split`.
- `03-spec-range` becomes `03-spec-lineup` on the same reasoning.
- `07-identity-inhand` is drafted on **one** filed observation. Two further frames read as its
  argument and the ledger files them elsewhere — one as a `05-social-snapshot` variant, one to
  `03-spec-lineup`, which cites it too. The file says so and says the first job is re-filing
  rather than hunting. **A batch summary naming a pattern three times is not a count**, and
  writing 3/5 on the strength of one would have been the kind of number this repo has learned
  to distrust.

**What the render rounds already put into these files.** Four of the five carry a FOUNDING
RENDER ROUND section with measurements rather than intentions: hands held 1 of 1 on
`07-identity-inhand` against the adapter's warning; `03-spec-lineup`'s one-variable law broke
in its INVARIANTS block, with three different hub bores across three units that were told to
share one; `06-relief-claimstack` failed at two clusters and passed at five, which is what
produced G16's fill rule (ADR-064). A staging draft that already knows how it fails is worth
more than one that does not.

**One finding is a correction to a file in this very diff.** `06-relief-claimstack` was
written around a person carrying a felt state because its single exemplar had one. Batch D's
second source builds the identical layout with the PRODUCT in that position and no person at
all, so `PARTS/subject` is too narrow as drafted. The file ships with the fault named in its
own KNOWN-FLAKY rather than silently widened, because widening it now would be a guess and
the evidence rule wants a third observation.

**Consequences.**

- `registry/types/_staging/` gains five files; `_staging` count 3 → 8.
- `registry/vocabulary.yaml` gains step `7`, job `identity`, and devices `stilllife`,
  `lineup`, `claimstack`, `inhand`, `pack`. Seven taxonomy additions, each used by a file in
  this diff and none speculative.
- All five declare `text_layer` and are therefore **the first types G16 binds** (ADR-064,
  `458a544`). Until this commit G16 governed nothing.
- All five take `exempt_from: [G7]` except where a knockout makes it unnecessary, under the
  arranged-product exception ADR-064 added to G7's scope.
- `mapping/slot-rules.md` is **untouched**: its preference table binds ACTIVE types and the
  validator's every-type-in-a-row gate reads the index, which excludes staging. A row for
  identity is a promotion-diff problem and naming it now would imply a routing decision this
  ADR explicitly defers.
- `registry/index.yaml` and `dist/app-bundle/` regenerate; neither gains a staging type.
- `registry_version` unchanged — no active structure moves.

**What is NOT drafted, and why.** Six further proposals sit at 2 sources or fewer —
`02-symptom-halo`, `03-spec-flatlay`, `04-proof-stat`, `07-identity-callout`,
`02-cause-stilllife`, `05-persona-scene` — and each is one clean observation away from being
worth a file. `04-proof-stat` is held back for a second reason worth stating: both its
observations argue from a survey percentage with a substantiation footnote, and this library
has no rule about substantiation anywhere. G14 covers a fabricated endorsement; nothing covers
a fabricated statistic. That rule has to exist before a statistic type can have a skeleton.

## ADR-066 · 2026-09-03 · Curation pass: the claim stack is the corpus's commonest argument, and halo is callout

A curation pass over 269 observations, run after batches E through H added 65 records from
eight further direct-response product pages. Four changes, each carrying its evidence.

**1. `06-relief-claimstack` reaches NINE distinct sources and two of its clauses were wrong.**

The proposal was drafted from one observation and its own KNOWN-FLAKY named both faults before
the evidence arrived. Both are now past the rule twice over and are corrected in the file:

- `PARTS/subject` was written around **a person carrying a felt state**, because the single
  exemplar had one. Four of the nine sources put the PRODUCT there instead — capsules, a neck
  device, a mouthpiece, a headset — and the argument is unchanged. The slot now takes a person,
  the product, or the product in use, and states the consequence: **where the subject is the
  product, G9 is not engaged at all**, which makes the product form the safer of the two.
- `PARTS/field` demanded **one flat tone, no room**. Three sources in batch H put a real room
  behind the words and one sets them into the room's own wall with no panel. The clause existed
  to keep words legible and a blurred room does that; a real room also buys context the flat
  field throws away. Three forms are legislated and the binding clause becomes legibility.

Nine sources across supplements, coffee, personal care, audio and consumer electronics makes
this **the best-evidenced proposal this library has ever held, active types included**. The
finding behind the number is worth stating plainly: a subject to one side with a headline and
short claim lines filling the other is the single most common argument image on a
direct-response product page. Criterion 2 becomes the binding gap and it is a real one — a
type this common will contest every outcome slot with `06-relief-hero`, and the
router-confusion test has to run before promotion rather than after.

**2. `03-spec-callout` reaches five sources and is drafted. Halo and callout are ONE DEVICE.**

Batch G raised the question and a batch H frame settles it: the feicemat tile places four
labelled satellites around a central product **with no leader lines at all**. So the leader is
a parameter of the layout, not its identity, and what makes the construction is a subject at
the centre with labelled satellites around it. Three joining forms are observed — leader line,
dashed leader, nothing — and the file legislates them as parameters.

**They are one device and not one type.** `02-symptom-halo`'s job is `symptom`; this one's is
`spec`. SPEC §3.1 makes two jobs two types however alike the picture, exactly as `split`
already serves `01-pain-split` and `03-spec-split`. The halo proposal therefore survives,
renamed **`02-symptom-callout`**, at two sources, sharing the new device. It gets no file until
it has three, and the rename is recorded here because the ledger carries eight records under
the old id and a reader has to be able to follow them.

New device `callout` in `vocabulary.yaml`. **The file states its own biggest risk in
KNOWN-FLAKY**: it asks for up to eight text clusters where G16's founding rounds measured five,
so its count rule is provisional on a render round it has not had.

**3. `03-use-sequence` gains `--labelled`, its first variant, on three distinct observations.**

The base type forbids numbers, step markers and text outright, because the order is meant to be
read from the actions. Three products broke exactly that one clause: a pet-food page numbering
its steps, a coffee page numbering three panels, and an anti-snoring page CAPTIONING four
panels with no numbers at all. The third is why the variant is `--labelled` rather than
`--numbered` — a caption breaks the same clause a numeral does.

**The base discipline is not weakened and the boundary is stated in the block**: a label NAMES
a panel; an arrow CARRIES the reading order between panels; only the second does the job the
actions are supposed to do, and it stays banned. Panel count moves to four with the 2x2
observation, which SPEC §3.2 already makes a parameter.

A FOURTH variant-candidate on this type — a four-cell vertical rail from the older corpus,
`sha256:62797f53c0081926…` — is a DIFFERENT single decision and is deliberately not folded in.
Folding two decisions into one variant is how a variant stops meaning anything.

**4. `argument-faults.md` gains A12: a number in a frame is a claim the frame cannot
substantiate.**

Seven frames across five sources argue from a figure and the substantiation attached to them
**degrades in one direction**: a named survey with n=307, then a survey with 274 participants,
then a bare asterisk with no footnote, then nothing, then nothing to two decimal places, then a
clinical blood-pressure range with nothing. One frame in the whole corpus does it correctly and
is the shape a rule would have to legislate.

**This is filed as an argument fault rather than written as a global rule, and that is a
deliberate limit on what this pass decides.** A12 names the fault, measures it, and states a
narrow working position — a figure enters a frame only where `content.json` carries the figure
AND its source, and the source is set beside it. What A12 does not do is bind the library by
law, because a rule about what claims may be printed is a commercial and regulatory decision
rather than a craft one, and it is the owner's. **Three proposals are blocked behind that
decision** — `04-proof-stat` at 4/5 sources, `04-proof-instrument`, and `04-proof-interface` —
and none of them can be given a skeleton until it is made, because a skeleton has to say where
the number comes from.

**Consequences.**

- `registry/types/03-use-sequence.md` 1.10 → **1.11**, the only ACTIVE type touched. Its
  `use_when` is unchanged, so no trigger moves; the router-confusion test of `curate.md` §4 is
  satisfied by that and confirmed by 14 golden slots still deriving with 0 errors.
- `registry/types/_staging/06-relief-claimstack.md` 0.1 → 0.2.
- `registry/types/_staging/03-spec-callout.md` is new; `_staging` count 8 → 9.
- `registry/vocabulary.yaml` gains device `callout`.
- `registry/argument-faults.md` gains A12.
- `registry/index.yaml` and `dist/app-bundle/` regenerate. The index delta is two lines — the
  version and the variants list of one type.
- `registry_version` unchanged: no active structure moves and no vocabulary value is removed.

**What this pass deliberately did NOT do.** It did not promote anything: `06-relief-claimstack`
and `03-spec-callout` both clear criterion 1 and both fail criteria 2 and 3, and a promotion
that skips a router-confusion test on the two most contested types in the registry would be
the expensive kind of shortcut. It did not write the substantiation rule. And it did not merge
`02-symptom-callout` into this file, because two jobs are two types and the grammar already
says so.

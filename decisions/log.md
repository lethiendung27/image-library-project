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

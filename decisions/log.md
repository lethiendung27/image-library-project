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

---

## ADR-067 · 2026-09-03 · `multi-pass` is removed from the vocabulary, and every case it covered gets a named single-pass mechanism

**Owner instruction, 2026-09-03:** "bỏ multi pass triệt để."

**Three ADRs had already banned it and the value was still there.** ADR-021 stopped a
multi-pass option reaching a prompt set. ADR-039 retired `adapters/nano-banana.md` Rule 3
and the `steps[]` field, having found the ban "still taught by `runbook.md` Step 6, the
adapter's Rule 3 and `output.schema.json` — three days and eleven ADRs late". ADR-041
deprecated the value and wrote a countdown into `vocabulary.yaml`: when the number of type
files declaring it reaches 0, delete it. It never reached 0, because clearing the last one
meant deciding what `04-proof-lockedframe`'s `strict` camera lock does without compositing,
and that decision kept being deferred as an audit.

**What the deferral actually cost, measured rather than asserted.** `strict` is defined as
identical camera, framing and light across panels, and its route was "Multi-pass is
mandatory: generate one panel, edit-swap the variable, composite". A CAPABILITY gate under
it said `strict` is unavailable "where the renderer cannot composite". After ADR-021 that
condition was permanently true, so for **twenty days `strict` was a value no route could
select**, while `eval/golden/fixture-002` went on asserting it as the expected option A for
a slot. A conditional that is always true is a refusal wearing a condition's clothes.

### The decision

`multi-pass` leaves `registry/vocabulary.yaml`. A type declaring it is a validation ERROR,
not a warning, and the error names the replacement rather than reporting that a string is
not in a list. Adapter Rule 3's three templates are DELETED, which reverses ADR-039's choice
to keep them as a record — on the owner's instruction, and because a worked script for a
banned capability is the exact thing CLAUDE.md rule 6c exists to catch.

**Every case the templates covered keeps a mechanism, and each is measured or is marked
untested.** The general form is an **invariants block**: state what must not change ONCE,
before any panel or frame is described, rather than restating it inside each.

- **Locked-frame panel series.** `01-pain-split --mirror` measured both ways: the person
  described inside each panel returned two different people; an invariants block naming
  face, hair, clothes, camera height, distance and framing before either panel returned one.
  1 of 1 each way, and its `run: pass` worked example is a single-pass render. That is the
  route `04-proof-lockedframe` `strict` now takes.
- **Reference-true inset.** A clause, not a compositing step. `05-social-handoff`'s inset is
  model-drawn single-pass, 4 of 4 (ADR-053). An inset a clause cannot bind is dropped and
  the type ships without it.
- **Same-person pair across two frames** (`01-pain-scene` + `06-relief-scene`). The same
  invariants block written identically into both prompts, two independent generation calls.
  **Untested** — no bookend pair has been rendered this way, and this ADR says so rather
  than implying the deletion cost nothing.

**Why `strict` was not deleted instead.** Deleting it would have left `camera_lock` with one
value, which is not an axis, and would have falsified a golden fixture's assertion. It would
also have thrown away a picture requirement over a route, when the library already owns a
measured route for exactly that requirement in another type. The invariants block is not a
promise: `03-spec-lineup`'s founding round broke its own one-variable law inside one, three
different hub bores across three units told to share a spec. Both observations are recorded
in the type file. `strict` is now selectable and carries a stated risk, which is better than
being permanently unselectable and carrying none.

### Consequences — rule 6c sweep on `"multi-pass"`: 131 hits, 42 files, 10 in TEACHES

All ten read, plus one the tool did not find.

- `registry/vocabulary.yaml` — the value **deleted**, the countdown comment replaced by the
  reason it ended.
- `registry/types/04-proof-lockedframe.md` 1.15 → **1.16** — the registry's last
  declaration. `generation_mode: single-pass`; `strict` takes the invariants block; the
  CAPABILITY gate is retired. `ratios` corrected to ADR-016's five in the same edit: `5:3`
  and `3:2` dropped, unaskable since 2026-08-13.
- `registry/types/01-pain-split.md` 1.8 → **1.9** — `--mirror`'s `generation_mode override:
  multi-pass` **removed**. It had been contradicted by the type's own passing single-pass
  worked example since 1.8. KNOWN-FLAKY reworded: the identity break is about WHERE the
  person is described, not about pass count. `ratios`: `4:5` dropped, leaving `1:1`.
- `registry/types/03-mechanism-xray.md` 1.3 → **1.4** — a KNOWN-FLAKY prediction whose
  remedy was "the fallback is multi-pass ... (adapter Rule 3)": a prediction with an illegal
  remedy attached, pointing at a rule retired eleven days earlier. The remedy becomes SPEC
  §6.2's ordinary route. `ratios`: `4:5` dropped.
- `adapters/nano-banana.md` — Rule 3's **templates deleted**, replaced by the three-step
  retirement and the single-pass mechanism for each case. Its intro note keeps the MODEL
  fact — conversational editing is real — and drops the invitation to reach for it. It also
  carried a stale claim that `05-social-handoff` declares multi-pass; that type moved to
  `single-pass` at 2.6 and the adapter never noticed.
- `query/runbook.md` — Step 3's affected-executions list and Step 6's `steps[]` paragraph.
  Both **rewritten**: there is no longer "the type's multi-pass route" to fall back from.
- `query/output.schema.json` — 4 descriptions **rewritten**. The `pipeline` enum was already
  narrowed to `single-pass` at ADR-039; the `steps` field **stays**, because one delivered
  page carries it and must still parse.
- `SPEC.md:133` — the frontmatter comment said "multi-pass is DEPRECATED, ADR-041".
  **Rewritten** to name `single-pass` as the only legal value.
- `eval/golden/fixture-001` — the prose note "strict variants would be multi-pass".
  **Rewritten.** Not an assertion `check_golden` reads, which is why it survived ADR-039.
- `CLAUDE.md` — rule 6b bans emitting a multi-pass option and rule 6c cites ADR-039's miss.
  **Both stand**; they teach the ban, which is now enforced rather than asserted.
- `registry/types/03-use-grid.md:182` — a CHANGELOG line recording an earlier removal.
  **History, stands.**

**The sweep missed a file, and that is worth more than the file.** `eval/render-test.md`
Step 2 said "Multi-pass types follow their `steps[]` script — testing the script is part of
the test", and `scripts/adr-sweep.py` did not report it: the term was **capitalised**, and
the tool matches case-sensitively. Rule 6c exists because a banned term keeps being taught
by files nobody swept, and its own instrument has a blind spot that hides exactly the
sentence most likely to be an instruction — a step heading. The file is **rewritten**, and
the finding is written into `check_multipass_declarations`'s docstring where the next person
running a sweep will read it. Fixing the script is not done here; it is a change to a shared
tool and belongs in its own diff.

**GENERATED** — `registry/index.yaml` and `dist/app-bundle/` (11 mirrored files) regenerate.

**RECORDS** — 20 files keep the term: `decisions/log.md` (26 hits, this entry included),
`conversation.md`, `eval/render-tests.jsonl`, and the session directories. Nothing is
rewritten. `query/sessions/advertorial-seat-cushion-l-shaped-v02` (page 37) still carries
three `multi-pass` options on `story.1.image` and stays grandfathered by name in
`scripts/validate.py`, warned on every run. **It is not re-rendered and not reconstructed**:
if that page is ever rebuilt it is re-routed under today's law.

**Enforcement, fed known-bad input before being believed.** `04-proof-lockedframe` was set
back to `multi-pass` and the validator returned two errors — vocabulary closure, and the new
message naming the invariants route — then the file was restored and the tree returned to 0
errors. A checker that has only ever seen good input is not evidence.

`registry_version` unchanged. No skeleton, no argument and no routing outcome moves: the
only option pool affected is one whose `strict` value nothing could select.

---

## ADR-068 · 2026-09-03 · The ground is quiet and the badge has an interior — both measured against the corpus, not argued

**Owner audit of the six founding renders, 2026-09-03:** "các prompt chưa tốt ở việc chọn
màu, cũng như badge chưa phong phú như các badge corpus." Both complaints were checked
against the market before anything was rewritten, because three previous passes had answered
the badge complaint by adding rules and the verdict had not moved.

### The ground: measured on 119 corpus frames against 6 renders

The outer 8% ring of the frame, taken as the ground, over every direct-response corpus frame
the 2026-09-03 batches classified:

| | corpus, n=119 | the six renders |
|---|---|---|
| ground VALUE, median | 0.89 | 0.46 |
| ground SATURATION, median | 0.06 | 0.38 |
| darker than 0.70 value | 35% | 83% — 5 of 6 |
| more saturated than 0.25 | 24% | 67% — 4 of 6 |

**The market's ordinary ground is light and almost colourless; ours was dark and six times
more saturated.** No single frame is wrong. The SET sits off the distribution of the thing it
is copying, which is a fault only a distribution can show.

**The cause is a rule this library wrote the same day, to cure the opposite fault.** Three
type files tell the writer to take the ground from the product's own register — *"never a
house grey"*, *"chosen from the product's own register rather than reached for"*, *"what is
discouraged is reaching for pale grey every time"*. All three were written in the second pass
of 2026-09-03 to cure six frames of identical pale grey. They cured it. Nobody measured the
corpus first, so the cure had no idea where it was aiming.

**The fix is a distinction, not the opposite.** Going back to pale grey every time is the
fault those clauses fixed. The ground is now QUIET BY DEFAULT — light, near-neutral — and a
dark or saturated ground stays legal as a CHOICE the prompt justifies, because the corpus
builds one about a third of the time. Deriving the hue from the product's register survives
and is right; what it never licensed was depth and intensity. Variety is spent where the
corpus spends it: on the marks, the product and the chips.

### A hypothesis that the corpus REFUTED, recorded because it nearly became a rule

The first measurement taken was product-to-ground separation, and it looked decisive: 5 of 6
renders under 0.20 in value separation, the scissors frame at 0.02. A rule was half-drafted
requiring a value step between product and ground.

**Then the same measure was run on the corpus and it came back 2 of 4 under 0.20** — a white
bottle on light grey at 0.04, a blue pack on white at 0.06. The market does the thing the
draft rule was about to ban. What those frames have instead is a saturated cap, a hard cast
shadow or dark label type doing the separating. **The rule was dropped.** It is written here
because a measured-looking number on six of our own frames, with no corpus baseline beside
it, is exactly how the ground clauses being corrected in this ADR got written in the first
place.

### The badge: the three previous passes were all aimed at its OUTSIDE

Pass one gave the badge eight FORMS. Pass two gave it SIZE, POSITION and COLOUR. Pass three
put six badges in four corners in six colours. The verdict did not move, and the reason is
that every one of those is a property of the badge's outline.

Value spread inside the badge's own fill, p10 to p90, text ink excluded:

```
the six renders     0.06  0.09  0.03  0.31  0.02  0.03     5 of 6 DEAD FLAT
four corpus badges  0.12  0.35  0.16  0.10               3 of 4 carry a tone step
```

**The one render that is not flat is the only one whose prompt named a second tone** — *"a
scalloped rosette in deep gold with a darker gold rim"*. Nothing about the renderer resists
this. Five prompts asked for one flat colour and got one.

Two clauses in this repo put it there, and finding them is the whole of the decision. **G16's
own Style paragraph** says *"Flat solid colour. No gradient, outline, drop shadow, ribbon or
gradient bar"* — correct for the text block it was written for, and read as binding the badge.
And **the three MARKS tables say "one flat fill" five times between them**, which
`scripts/adr-sweep.py "flat fill"` located exactly.

**A badge carries at least one internal tone step and at least two type sizes.** A rim, a
concentric ring, an outline inset from the edge, or a sheen; a figure at one size, a label at
another, often a glyph.

**The type-size half of that is the weaker half and is stated at its measured strength.** By
eye the corpus badges looked far richer than ours; counted mechanically as distinct ink bands
they run 2–4 sizes against our 1–2, and **3 of 6 renders carried a single band where 0 of 4
corpus badges did**. Real, and smaller than it looked. The tone step is the strong finding;
the type hierarchy is the supporting one.

### Consequences — rule 6c sweep on `"flat fill"`: 39 hits, 28 files, 4 in TEACHES

- `registry/rules.md` — G16 gains **round 4** (the ground table, the badge interior) and its
  **Style paragraph is scoped**: it says out loud that it governs the text block and not the
  badge, which is the misreading that produced 5 of 6 flat badges.
- `registry/types/_staging/03-spec-callout.md` 0.2 → **0.3** — `PARTS/setting` ground clause
  corrected, `MARKS` gains the interior, `tag` loses "one flat fill".
- `registry/types/_staging/06-relief-claimstack.md` 0.3 → **0.4** — `PARTS/field` corrected:
  the product's register governs HUE, not depth. `tag` and `pill` lose "one flat fill".
- `registry/types/_staging/07-identity-pack.md` 0.2 → **0.3** — `PARTS/setting` corrected the
  same way. `tag` and `pill` lose "one flat fill".
- `registry/types/02-cause-anatomy.md:54` — the fourth TEACHES hit, *"`flat-vector`: flat
  fills, hard edges, no gradients"*. **Stands.** That is a STYLE AXIS describing a whole
  rendering register, not a badge interior, and it is the one place in the registry where flat
  fills are the argument.
- `registry/types/_staging/ready-to-push/prompts.md` — **rewritten, six new prompts on six
  products none of these three types has seen.** Re-running the same six to A/B a fix would
  test a clause against a product it already knows, which is the one thing it cannot do.
- GENERATED — `registry/index.yaml` and `dist/app-bundle/` regenerate.

**One corpus habit observed and deliberately NOT legislated.** *One badge per frame* is
contradicted 1 of 4 — a benefits tile carrying two credential stamps side by side, and a
bottle carrying a shield plus three stacked claim chips. Two of four still carry one. Below
the evidence rule, so the rule stands and G16 now records where it will break first.

**What this ADR does not settle.** Whether the interior was the missing variable is a question
for the next render round, not for this diff: three passes have now been confident about the
badge and three have been wrong. The prompts are written so the answer is legible either way,
and if round 2 comes back monotonous again then the problem is not any property of the badge
and this library should stop guessing at it and ask the owner to point at a corpus badge and
say *that one*.

`registry_version` unchanged. No skeleton, no argument and no routing outcome moves.

---

## ADR-069 · 2026-09-09 · A third namespace for the top-N lede, and the count that came back as three

**Owner instructions, 2026-09-08 and 2026-09-09**, in order: build seven image types for a
new page kind, a top-N listicle; that page has one image slot and is driven by product
input rather than `content.json`; duplicate the types it already owns under new names, on
the `gif-types` precedent, into `toplist-types`; the input carries an awareness stage but
do not lean on it; build to the recommendation.

### The seven, checked against the registry before anything was written

The owner supplied the taxonomy: pain shot, lifestyle in-use, lineup, testing shot, winner
packshot with a badge, composite collage, author/expert. Checking each against what the
library already owns changed the size of the job more than any other step:

| # | owner's type | what it turned out to be |
|---|---|---|
| 1 | pain point | **already owned.** `01-pain-scene`'s `use_when` reads *"Cold traffic that does not know the product yet. Advertorial header image, Facebook/native ad creative, opening image of a story"* — the owner's type 1, including its cold-traffic reasoning |
| 2 | lifestyle / after | **already owned** — `06-relief-scene`, which even declares `pairs_with: [01-pain-scene]` |
| 3 | lineup | **genuinely new.** `03-spec-lineup` is several units of ONE product where exactly one thing differs; this is a field of rival makers |
| 4 | testing / process | **genuinely new, and the only one of the seven blocked by nothing** |
| 5 | winner packshot | **blocked.** Strip the verdict mark and `07-identity-pack` already does it, so the mark IS the type — and G16 marks *an award* and *a rating* `LAW, not taste` |
| 6 | collage | **new, and nearly an axis of 3** — see below |
| 7 | author / expert | **already declared out of scope.** `mapping/slot-rules.md`'s `author` row: *"a portrait of a named person, out of library scope"* |

So the brief was not seven new types. It was **three active files, three reserved on
owner decisions, one placeholder recording why the seventh has no skeleton.**

### Why a namespace rather than seven more image types

One slot. Over half of SPEC §7 has nothing to act on: the Stage 1 shortlist ranks by role
affinity and there is one role, so affinity is a constant; the Stage 2 cross-slot pass
needs a second slot for `never_with`, `avoid_adjacent` and one-type-once to mean anything;
the coverage pass counts Trust Ladder rungs a single image cannot cover. That is the same
reasoning SPEC §3.6 gives for gif types, and it is why this is `registry/toplist-types/`
and never enters `index.yaml`.

The second reason is the one ADR-065 already named for the identity family: since ADR-060
there is no admission test left, so an active image type is a candidate for every slot on
every page and `use_when` is the only thing keeping a packshot out of a pain slot. A
namespace is a wall; a sentence is not.

### Inheritance rather than duplication — a departure, stated

The instruction was to duplicate. What shipped is `inherits`: `lede-pain` and `lede-inuse`
are real standalone files with their own ids, `use_when` and `BOUNDARY`, and their
skeletons **call the parent's `PARTS` by name instead of restating them**.

The reason is six days old and in this repo. `registry/types/_staging/ready-to-push/` once
shipped byte copies of four type files so they could be read without opening the repo;
they were deleted on 2026-09-03 with the finding written into that folder's README — *two
copies of one file drift, and the stale one is the one somebody reads*. A namespace built
on copies inherits that defect seven times. Concretely: `01-pain-scene` carries A14's
`cost` block, which took a set from 0 pass to 3 pass / 3 partial; a copy would silently
hold the pre-A14 version the first time the parent improves.

**The `gif-types` precedent the instruction cited does not actually support copying** —
nothing in that namespace is a copy of an image type; its ids and sections differ because
its arguments differ. What it supports is a separate namespace, which is what it got. If
the owner wants literal copies the change is one field per file and this ADR is the record
of why it was not done that way first.

### Selection: four layers, and awareness carries one of them

The instruction was to carry awareness and not lean on it. The shape that obeys it puts
every REFUSAL in awareness-free machinery and lets awareness only order what survives:

1. **Mechanical admission** — `status`, `products_in_frame` against the input's product
   count, `requires_product_photo` against an empty `reference_photos`, and the
   `product.attributes` gates a type inherits. Refuses. No awareness.
2. **Preference order**, `mapping/toplist-rules.md`, keyed on awareness and **declared in
   its own first paragraph as a hypothesis with no evidence behind it**.
3. **FIT by judgement** on `use_when` and `BOUNDARY`, and — adopting ADR-059's own
   mitigation as law here — **every choice cites the sentence of product copy that decided
   it**.
4. **Pick rate**, SPEC §7.7. It holds 0 records. One slot per page means one record per
   page and a cell keyed on the type alone, so **twenty pages make this prior live** — the
   fastest any cell in this library can fill, and the reason this format is where
   judgement can be replaced by measurement rather than argued about.

A second, awareness-free signal was available — the balance of `problems_solved` against
`specification` and `raw_features` tells whether a brief is written problem-first or
feature-first — and is deliberately **left unbuilt**. Writing a second unmeasured rule
beside the first is exactly how ADR-068's ground clauses happened four days ago.

### No text, so G16 does not bind here

A lede is scraped as `og:image` and sits beside the page's own headline; the owner's
constraint is that no words are baked in. **No toplist type declares `text_layer`**, the
validator errors on one that tries, and G16 — four rounds of work on caps, badges, mobile
floors and size anchors — governs nothing in this namespace. ADR-068's finding about the
GROUND does carry over, being a fact about the photograph rather than about text.

### Two boundary calls worth recording

**`lede-lineup` and `lede-collage` were nearly merged** into one type with a `staging`
axis, since SPEC §3.2 makes an execution difference an axis rather than a type. They are
kept apart on SPEC §3.1: a lineup is photographed on one surface under one light and
claims the units were TOGETHER; a collage is assembled from cut-outs and claims only that
these are the five. Possession against enumeration. **The merge condition is written into
`lede-lineup`**: if a render round shows readers take the same meaning from both, they
merge and `lede-collage` is the file that goes.

**`lede-winner` collapses into `07-identity-pack` without its verdict mark**, and its file
says so. That is the absorption ladder working, not a defect in the draft — and it is why
the type is reserved rather than shipped without the badge.

### Consequences — rule 6c sweep on `"namespace"`: 19 hits, 7 files, 4 in TEACHES

- `SPEC.md` — **§3.7 added** (3 of the 4 TEACHES hits are the new section). `SPEC.md:157`,
  *"A second, smaller registry governs motion"*, **stands**: gif is still the second, and
  the word counts its ordinal rather than the registries.
- `registry/types/_staging/07-identity-inhand.md:42` and `07-identity-pack.md:43` —
  both say the identity family's home is undecided between a new step in
  `registry/types/` and *"its own namespace like `registry/gif-types/`"*. **Both stand and
  neither is decided here**, but the option is no longer hypothetical: there is now a
  second worked precedent for a third namespace, including a validator, a required-section
  list and an instruction file. That decision got cheaper without being taken.
- `registry/vocabulary.yaml` — `toplist_types`, `toplist_frame_populations`,
  `toplist_awareness`.
- `registry/toplist-types/` — 7 files: `lede-pain`, `lede-inuse`, `lede-testing` active;
  `lede-lineup`, `lede-collage`, `lede-winner`, `lede-authority` reserved, each naming its
  blocker in a `BLOCK` section.
- `registry/toplist-instruction.md`, `mapping/toplist-rules.md` — new.
- `scripts/validate.py` — the namespace is validated: id closure, version, status,
  `products_in_frame`, awareness values, `inherits` resolving to an ACTIVE image type,
  `blocked_by` present exactly when reserved, a `BLOCK` section on a reserved type, no
  `text_layer`, and a floor of three active types because ADR-058 asks a slot for three.
- `CLAUDE.md` — two entry-point rows.
- GENERATED — `registry/index.yaml` and `dist/app-bundle/` regenerate; **neither gains a
  toplist type**, which is the namespace doing its job.

**Enforcement fed known-bad input before being believed.** Five injected faults, five
fired, control clean at 0 errors: a reserved type with `blocked_by: null`; an active type
carrying a blocker; a declared `text_layer`; `inherits` pointing at a type that does not
exist; an awareness value off the closed list. The `text_layer` message was initially
unreachable behind the unknown-key check and was moved ahead of it, because *"unknown
frontmatter key"* does not tell a reader why this namespace has no text.

### What is NOT done

No prompt has been written from any of these types and no render exists — every clause in
all seven files is a proposal, which is the state ADR-065 called a staging draft and the
honest label for a namespace one day old. The product-input schema is **not** built: the
four missing fields are named in `toplist-instruction.md` (`products[]`, a rank or verdict,
test facts, a narrower `category`) and `products[]` is what gates two of the four reserved
types. The two owner decisions — the one-reference-photo limit and G16's two `LAW` rows —
are untouched and are what unblock four of the seven.

`registry_version` unchanged: no image type, no active structure and no routing outcome
moves.

---

## ADR-070 · 2026-09-09 · Toplist types copy their parent verbatim, and the copy is made to say when it has drifted

**Owner decision, 2026-09-09: "chép nguyên văn."** ADR-069 shipped `inherits` — a toplist
type citing its parent's `PARTS` by name — after the instruction had been to duplicate.
The concern was put to the owner in one paragraph, the owner reaffirmed, and this ADR is
that decision landing. ADR-069 stands as written; the log is append-only and a later
reader should be able to see the reversal as a reversal.

**What shipped.** `lede-pain` carries `01-pain-scene` at 1.18 and `lede-inuse` carries
`06-relief-scene` at 3.7 — PURPOSE, SKELETON, PARTS, THE RELIEF, MARKS, SLOT CONSTRAINTS,
NEGATIVE and KNOWN-FLAKY, spliced out of the parent **by script rather than retyped**, so
"nguyên văn" means byte-identical rather than nearly.

**Two sections are not copied, for correctness rather than for brevity.** The parent's
`WORKED EXAMPLES`, because SPEC §3.3 keeps a rendered example's full prompt text as the
record of what actually rendered and those renders were the parent's at the parent's
version — reprinting them under a toplist id would be a false claim about what was
rendered. And the parent's `CHANGELOG`, which is its own evidence trail and commit hashes.

### The mitigation, because the objection was real and does not go away

A copy cannot be stopped from drifting. It can be made to **say** so.

`inherits` becomes `copied_from` plus **`copied_at_version`**, which records the parent's
version at the moment of the copy. `scripts/validate.py` compares the two on every run and
**warns** when the parent has moved, naming the remedy: re-copy, or write into the copy's
CHANGELOG why the divergence is intended. Fed known-bad input before being believed —
`01-pain-scene` was bumped to 1.19 and the warning fired against `lede-pain`; a
`copied_at_version` of null beside a set `copied_from` errored; a `copied_at_version` set
beside a null `copied_from` errored; control clean at 0 errors.

This is strictly better than what ADR-069 had. Inheritance made drift impossible and
therefore invisible; copying makes it possible and now visible. The owner's choice is not
worse for having an instrument pointed at it — it is the first version of this that has
one.

### What the sweep caught, and it is the part that would have bitten

**A rule keyed on the parent's id does not reach a copy.** `mapping/slot-rules.md` says
*"drop `06-relief-scene`"* when `result_visibility: invisible`; nothing in it says
`lede-inuse`. Under ADR-069's `inherits` the gate carried for free and the instruction
file said so. Under a copy it does not carry at all, and the gate would have gone silently
missing on the first page routed with an invisible result.

Every gate a copied type should carry is therefore **restated by toplist id** in
`mapping/toplist-rules.md`, and the instruction file says in the same breath that adding a
gate to the parent later does not add it here. That is the cost of the decision, paid
explicitly rather than discovered.

### The sweep tool did not know the namespace existed

`scripts/adr-sweep.py "inherit"` filed `registry/toplist-instruction.md` and every file in
`registry/toplist-types/` under **UNCLASSIFIED** — its own output says *"classify it, then
extend this script's TEACHES/RECORDS tuples"*. ADR-069 created that gap yesterday by adding
a namespace the tool's tuples had never heard of, which means every future sweep on any
term would have misclassified the whole new registry. The three paths are added to
`TEACHES`. This is the second time in a week the rule-6c instrument has been found with a
blind spot — ADR-067 found it matching case-sensitively — and both were found only because
something else was being swept at the time.

### Consequences — rule 6c sweep on `"inherit"`: 60 hits, 29 files, 12 in TEACHES + 3 UNCLASSIFIED

- `SPEC.md` §3.7 — the frontmatter key list and the *Inheritance rather than copying*
  bullet, **both rewritten**.
- `registry/toplist-instruction.md` — *Inheritance* becomes **Copying: verbatim, and made
  auditable**, and layer 1 of SELECTION is corrected to point at `toplist-rules.md`'s
  restated gates rather than at the parent's.
- `mapping/toplist-rules.md` — the `result_visibility` row no longer claims to inherit.
- `registry/toplist-types/lede-pain.md` 0.1 → **0.2**, `lede-inuse.md` 0.1 → **0.2**; the
  other five carry the renamed key with both values null.
- `scripts/validate.py` — `copied_from` + `copied_at_version`, the drift warning, and the
  null-pairing errors.
- `scripts/adr-sweep.py` — three paths into `TEACHES`.
- The nine other TEACHES hits — `adapters/nano-banana.md:36`, `registry/rules.md` ×5,
  `02-symptom-rail`, `03-mechanism-ghostbody`, `03-mechanism-xray`, `03-spec-split`,
  `05-persona-grid`, `05-social-handoff`, `_staging/03-use-rail` — are the ordinary English
  word *inherited* in craft prose ("inherited by habit", "left to inherit from the main
  frame"). **All stand**; none is about this mechanism.
- The 0.1 CHANGELOG lines in both files still say *"inheriting"*. **They stand** — 0.1
  shipped at `c89aa48` and is real history.

**What this does not change.** No prompt and no render exists for any toplist type; all
seven remain proposals. The four reserved types are still reserved on the same two owner
decisions. `registry_version` unchanged.

---

## ADR-071 · 2026-09-09 · Toplist ledes may bake text, and G16 follows them in

**Owner instruction, 2026-09-09:** "ảnh cho toplist có thể nướng chữ, badge vào", with two
named forms — a winner packshot under a "Best Overall" band or a score, and a cut-out
collage under a "BEST X" line.

**This reverses the owner's own constraint of the same day**, on which ADR-069 built the
namespace: *"Cần tránh: ảnh có chữ nướng sẵn (og:image và L21 kiểm tra)"*. Recorded as a
reversal rather than smoothed over, and the corpus is on the new side of it — **7 of the
32 reference frames classified in batches 2026-09-09-A/B bake text**, including both forms
named above.

### Which types carry a text layer is decided by evidence, not by the permission

The permission is namespace-wide; the implementation is not. Two types take a layer:

| type | `text_layer` | evidence |
|---|---|---|
| `lede-winner` | `[title, badge]` | the verdict mark IS the type — strip it and `07-identity-pack` already makes the picture, which 0.1 said in its own BLOCK |
| `lede-collage` | `[title, badge]` | the owner's named market form, and 2 of 5 corpus collages carry an award badge over the cut-outs |

The other five take none, and that is the corpus rather than a rule: **5 of 5**
`lede-lineup` observations carry no words — and a badge there would breach that type's own
no-favoured-unit law by marking one — and **10 of 11** `lede-testing` observations carry
none, the single exception being a video thumbnail rather than a page lede. Giving those
two a layer would be a clause with one observation against ten.

**So G16 binds this namespace after all.** Four rounds of measured work — the seven-word
line cap now resting on 79 lines, the badge interior of ADR-068, the mobile floor, the
size anchor that ADR-068 measured failing at 0.13–0.64, the watermark corner, the fill
rule — arrive intact on the types that declare the key. ADR-069 wrote that G16 "does not
bind here at all"; that sentence is now false and is rewritten.

### `lede-winner` unblocks, and the distinction that unblocked it was already in the file

0.1 shipped `reserved` with its BLOCK naming the question rather than answering it:
*"'Best Overall' on a top-N page is not an award issued by an outside body; it is the
page's own editorial verdict about its own ranking."* The owner took that distinction.

`lede-winner` 0.1 → **0.2, reserved → active**, and its BLOCK becomes SLOT CONSTRAINTS.
`lede-collage` gains the layer and **stays reserved** — its blocker was never the text, it
is the one-reference-photo limit against `products_in_frame: many`.

### What was NOT permitted, and is refused in the same breath

The instruction covered the page's own verdict about its own ranking. Two of G16's content
rows are marked `LAW, not taste` and neither was addressed:

- **another party's mark** — a certification seal, a press logo, a third-party award. The
  corpus carries `CNET LAB TEST WINNER` and `CNET PEOPLE'S PICKS` precisely because on
  CNET's own page CNET is the issuing body; on a page that is not theirs it is the
  trademark question the library declined to answer on 2026-08-18.
- **a fabricated endorsement** — a customer's name, star row, review count or verified
  mark. G14 calls it illegal under FTC endorsement rules and binds the SLOT, so G16 has
  nothing to waive.

**A publisher's own score sits between them and is permitted with a leash.** It is a
figure, so `argument-faults.md` A15's working position holds: the number enters the frame
only where the product input carries it, never where a prompt chooses one.

**That leash has a consequence with teeth.** The input has no rank or verdict field — item
2 of the missing list in `toplist-instruction.md` — so `mapping/toplist-rules.md` layer 1
gains a condition that **refuses `lede-winner` on every page until the field exists**. The
type is active and unroutable, which is the same shape as `requires_product_photo: true`
meeting an empty `reference_photos`: a mechanical precondition, not a block.

### Consequences — rule 6c sweep on `"og:image"`: 6 hits, 5 files, 2 in TEACHES

- `SPEC.md` §3.7's `text_layer` bullet — **rewritten**, and it was one of the two TEACHES
  hits.
- `registry/toplist-instruction.md` — *Text: this namespace does not carry one* becomes
  **Text: some types carry one, and G16 binds them**; the other TEACHES hit.
- `scripts/validate.py` — the error that refused any `text_layer` is replaced by the same
  closed-slot check image types get, and `text_layer` joins the optional keys. Fed
  known-bad input: an illegal slot fired, an empty list fired, the legal list was silent.
- `registry/toplist-types/lede-winner.md` 0.1 → **0.2**, reserved → **active**, layer
  declared, BLOCK → SLOT CONSTRAINTS, NEGATIVE gains the third-party mark and the invented
  placing.
- `registry/toplist-types/lede-collage.md` 0.1 → **0.2**, layer declared, the "no words"
  clauses removed, `[TITLE]` and `[BADGE]` added to the skeleton. Still reserved.
- `registry/toplist-types/lede-lineup.md` and `lede-testing.md` 0.1 → **0.2** — each keeps
  its word ban and now says whose evidence it is, 5 of 5 and 10 of 11.
- `mapping/toplist-rules.md` — layer 1 gains the rank condition; the preference rows drop
  `lede-winner`'s reserved asterisk.
- GENERATED — `dist/app-bundle/` regenerates for SPEC.md.

**One thing this ADR deliberately does not do.** Batch 2026-09-09-B recorded two findings
that contradict `lede-testing` — a lab coat in the corpus against a clause banning one,
and 2 of 2 frames carrying the testing argument on the setting alone against a BOUNDARY
that calls the instrument test "checkable at a glance". Both are marked in the file and
left for a curation pass, because `classify-batch.md` makes patches curation's job and
this is a permission decision, not a curation one.

---

## ADR-072 · 2026-09-09 · The ground rule transfers on value and not on saturation, and two type files owned a badge with no form library

**Owner audit, 2026-09-09: "led winner và collage chưa tốt."** Three passes on the
direct-response badges were answered by guessing at the wrong axis, so this one measured
the namespace's own corpus before touching anything. Both files were wrong, in two
different ways, and one of the errors was shipped this morning.

### Finding 1 — half of ADR-068's ground rule was imported into a namespace that contradicts it

`registry/toplist-instruction.md` told all seven types to take ADR-068's ground: light and
low in saturation, measured on **119 direct-response product-page frames** at value 0.89
and saturation 0.06. The toplist corpus was classified at `78ab907` and never consulted.
Measured now, outer 8% ring, per family:

| family | n | value median | saturation median | saturated > 0.25 |
|---|---|---|---|---|
| `lede-winner` | 1 | 0.91 | **0.60** | 1 of 1 |
| `lede-collage` | 5 | 0.90 | **0.49** | 5 of 5 |
| `lede-lineup` | 5 | 0.81 | 0.26 | 3 of 5 |
| `lede-authority` | 3 | 0.67 | 0.15 | 1 of 3 |
| `lede-testing` | 11 | 0.65 | **0.13** | 2 of 11 |
| direct-response (ADR-068) | 119 | 0.89 | **0.06** | 24% |

**It transfers on VALUE and not on SATURATION.** Light is right at 0.81–0.91. Quiet is
wrong by a factor of ten for the two assembled types, and **6 of 6 of their frames sit
above the 0.25 line ADR-068 treats as loud**.

**The discriminator is whether the ground is DESIGNED or PHOTOGRAPHED**, which is the line
`lede-lineup` and `lede-collage` were already told apart by. A cut-out unit carries no
scene, so the ground is the only place colour can live; a bench is a bench. `lede-lineup`
sits between at 0.26 — photographed, but often onto a chosen seamless.

**This is ADR-068's own failure repeated four days later.** That ADR was written because
three type files took the ground from the product's own register and nobody measured the
corpus first. Here a rule measured on one corpus was applied to another whose data was
already in the ledger. The instrument was right and it was pointed at the wrong family.

### Finding 2 — both files declared a badge and owned no form library

`lede-winner` and `lede-collage` both carry `text_layer: [title, badge]` since ADR-071 and
**neither had a `MARKS` section**. G16 governs a badge's WORDS and the type governs its
FORM (ADR-012, ADR-043, ADR-068) — so the form was left to each prompt to invent, which is
precisely the monotony that took three passes to find on the direct-response types and
that ADR-068 closed by giving each of them a form table plus an interior spec.

Both now carry `MARKS`, with **observation counts against every form** so nobody mistakes a
borrowed shape for an attested one: `plaque` has 2, `sticker` has 1, `band` — the owner's
own named form, "dải Best Overall" — has **0**, and `roundel` is borrowed outright.

### Finding 3 — a number this library shipped this morning was wrong

ADR-071 wrote *"2 of 5 corpus collages carry an award badge"*. Five records name
`lede-collage`, but two are `variant-candidate` records of a different shape — two views of
ONE product, and three outfits on one person. The denominator for the type as defined is
**three**, so it is **2 of 3**. Corrected in both the instruction file and the type file.

### Finding 4 — the badge may sit over one unit, against a law borrowed from another type

`lede-collage`'s `ARRANGEMENT` says no unit is favoured, borrowed from `lede-lineup`, which
borrowed it from `04-proof-lockedframe`. **Both corpus badges sit over a unit** — one over
the centre vacuum. Resolved as a distinction rather than a reversal: the law governs SIZE,
HEIGHT, POSITION and LIGHT, which would decide the comparison before the reader does; a
mark placed over one unit is the page saying which won, which is this type's job in a way
it is not `lede-lineup`'s. **That is 1 of 1 reasoning against 2 of 2 observations**, so the
file says it is the first thing a render round should check, and round 1 asks it as
question 9.

### Finding 5 — two smaller ones, both recorded rather than smoothed

- `lede-winner`'s BOUNDARY still read *"this boundary is the reason the file is reserved
  rather than active"* after ADR-071 made it active this morning. Stale, corrected.
- **`lede-winner` is ACTIVE on one corpus observation, and that observation is not a
  winner.** Its own ledger deviation says the mark is *"a promotion, not a rank — no
  ordinal and no award body"*. So the type has **zero** observations of its own argument,
  and `PARTS/ground` is a clause at n=1. The file now says so in its own words.
- `lede-collage` gains `PARTS/title` recording a second observed form: **oversized type
  BEHIND the cut-outs**, which overlap and crop it. Observed once, untested, named so a
  prompt asks for it deliberately rather than producing it by accident.

### Consequences — rule 6c sweep on `"ADR-068 ground"`: 4 hits, 4 files, all 4 in TEACHES

- `registry/toplist-types/lede-winner.md` 0.2 → **0.3** — `PARTS` and `MARKS` added, the
  ground pointer replaced, BOUNDARY corrected, the n=1 evidence stated.
- `registry/toplist-types/lede-collage.md` 0.2 → **0.3** — `PARTS/ground`, `PARTS/title`,
  `MARKS`, the 2-of-3 correction, the badge-over-a-unit distinction.
- `registry/toplist-types/lede-lineup.md` and `lede-testing.md` — **their pointers stand**.
  Both are photographed types and the imported rule is right for them: 0.26 and 0.13
  against ADR-068's 0.06, and the instruction file now says which families it binds.
  Their skeleton lines are left as they are rather than churned.
- `registry/toplist-instruction.md` — a new **Ground** section carrying the table and the
  designed/photographed split; the Text section's pointer corrected; the 2-of-5 fixed.
- `registry/toplist-types/round-1/prompts.md` — prompts 5 and 6 rewritten onto saturated
  designed grounds, both badges named by form, prompt 6's badge moved over a unit to test
  finding 4, and grading question 9 added. Lengths 1029–1632 against adapter Rule 6's
  1450–1600, reported rather than padded.

**What this ADR does not do.** It does not touch `lede-pain`, `lede-inuse`,
`lede-authority` or the two photographed types beyond the instruction file, and it renders
nothing. `PARTS/ground` on both audited types rests on 1 and 5 observations and no render
at all — the correction is better-evidenced than what it replaced, which is not the same as
being evidenced.

---

## ADR-073 · 2026-09-09 · The toplist ground rule is measured from the toplist corpus, and TEXTURE splits the namespace in two

**Owner instruction, 2026-09-09:** "không sử dụng Luật nền của ADR-068. tự audit, classify
các ảnh trong folder toplist để phát triển prompt cho nền của một số loại ảnh."

ADR-068's ground finding was measured on 119 direct-response product-page frames. It was
carried into this namespace twice — whole at ADR-069, half-corrected at ADR-072 — and both
times it was a rule about a different kind of picture being asked to govern this one. **It
is now removed rather than corrected.** Everything below is measured on the 32 frames of
`stills/top list/`, classified in batches 2026-09-09-A/B, and on nothing else.

### The measurement that mattered was not colour

Six quantities were taken from the outer 8% ring of every frame: median value, median
saturation, hue spread across eight patches, value spread across the same eight, the axis
of the largest value change, and **TEXTURE — the mean absolute difference between adjacent
pixels**. Texture is the one that split the corpus, and it split it cleanly:

| family | n | **texture** | value | saturation | ring spread |
|---|---|---|---|---|---|
| `lede-winner` | 1 | **0.8** | 0.91 | 0.60 | 0.15 |
| `lede-collage` | 5 | **1.9** | 0.90 | 0.49 | 0.25 |
| *proposed* `lede-mosaic` | 3 | **2.8** | 0.76 | 0.43 | 0.35 |
| `lede-lineup` | 5 | **2.9** | 0.81 | 0.26 | 0.33 |
| `lede-authority` | 3 | 7.0 | 0.67 | 0.15 | 0.51 |
| `lede-testing` | 11 | 7.1 | 0.65 | 0.13 | 0.67 |
| `lede-inuse` | 1 | 10.0 | 0.16 | 0.26 | 0.34 |

**Nothing in 32 frames sits between 2.9 and 7.0.** A toplist ground is either a made
surface or a room, and the boundary is not a judgement call.

**`lede-lineup` is on the DESIGNED side, and that corrects its own file.** It reads 2.9,
with the assembled types, not 7 with the photographed ones: four of its five stand on a
smooth studio sweep rather than in a place. What is real in a lineup is the SURFACE under
the units and the contact shadows it takes; the backdrop is not. The file had assumed a
real room and said so in its skeleton.

### Three clauses, each written from its own family

**Designed, gradient — `lede-collage`, `lede-winner`.** Perfectly smooth. Light AND
strongly coloured, about 0.90 value with about 0.50 saturation, both together rather than
either. **Either a two-hue diagonal gradient or one flat tone, and nothing between them
was observed**: three of five collages travel roughly half the colour wheel corner to
corner at 177°, 175° and 177° of hue spread on a diagonal axis, and the other two hold a
single tone under 13°. `lede-winner`'s one frame is a diagonal at 179°.

**Designed, seamless — `lede-lineup`.** A studio sweep. **Saturation is bimodal and the
median hides it**: 0.03, 0.21, 0.26, 0.66, 0.71 — three near-white and two strongly
coloured, with nothing between 0.26 and 0.66. So this is a CHOICE a prompt names, not a
band it aims at: near-white when the units are dark or coloured, strongly coloured when
they are pale or metallic. No gradient.

**Photographed — `lede-testing`, `lede-authority`.** Real detail at texture 7.0.
**Mid, not light** at 0.65 against 0.90, because a bench under working light is not a
sweep. **Quiet** at 0.13 saturation with 2 of 11 above 0.25 — the colour lives in the
apparatus and the product, never in the room. **Unevenly lit**, ring spread 0.67: real
light falls off, and a prompt asking for even background illumination is asking for the
studio this type is not.

### What the measurement could not do, stated rather than hidden

One `lede-lineup` frame reads texture 18.2 and a hue spread of 175° — a garment flat-lay
filling the frame edge to edge, so the ring sampled the subject rather than the backdrop.
**Measuring a ground from a ring fails when the subject reaches the edge**, and that is why
the seamless clause says "every frame whose ring is actually ground" instead of claiming a
clean 5 of 5.

`lede-pain` has **zero** observations in this corpus — editorial review publishing carries
no pain lede — so no ground clause is written for it and its copied parent's stays.
`lede-inuse` has one, and it is dark at 0.16; too thin to legislate and recorded as such.

### Consequences — rule 6c sweep on `"ADR-068"`: 38 hits, 13 files, 11 in TEACHES

- `registry/toplist-instruction.md` — the **Ground** section is rebuilt from this corpus
  and no longer cites ADR-068 for anything; the Text section's pointer to it is removed.
- `SPEC.md` §3.7 — the sentence saying ADR-068's ground finding binds every type is
  **rewritten** to say the namespace measures its own.
- `lede-winner.md` 0.3 → **0.4**, `lede-collage.md` 0.3 → **0.4** — `PARTS/ground`
  rewritten with smoothness as a measurement and the gradient's form named.
- `lede-lineup.md` 0.2 → **0.3** and `lede-testing.md` 0.2 → **0.3** — each gains a real
  `PARTS/ground` in place of the pointer it carried.
- `mapping/toplist-rules.md` — its two ADR-068 hits **stand**: they cite it as the
  precedent for writing an unmeasured rule, which is exactly what this ADR is another
  instance of, and neither is a ground rule.
- The remaining ADR-068 references in `lede-collage.md` and `lede-winner.md` are to the
  **badge interior** finding, not the ground. **They stand**, with the caveat now worth
  stating: that finding was also measured on the direct-response corpus, and this ADR is
  the second time an import from there has turned out to govern a different picture. It is
  not re-measured here and is the obvious next thing to check.
- `registry/toplist-types/round-1/prompts.md` — prompts 3, 4, 5 and 6 rewritten onto their
  own family's ground, and **5 and 6 deliberately take the two different designed forms**
  — 5 the diagonal two-hue gradient, 6 the single flat tone — so one round tests both
  rather than the same form twice. Four grading questions added.

**Nothing is rendered.** Every clause here is measured off market frames and has no render
behind it, which is a better position than the imported rule it replaces and is not the
same as being tested.

---

## ADR-074 · 2026-09-09 · `lede-winner` is a designed promotional hero, and the discriminator against `lede-collage` is WORDS rather than product count

**Owner instruction, 2026-09-09:** three frames named as examples of `lede-winner` — a
television under `TV DEALS`, AirPods with a `TOP DISCOUNTS` sticker, and three laptops under
an oversized `LAPTOPS` with a `CNET PEOPLE'S PICKS 2026` plaque. **Two of the three had been
filed elsewhere by this session**: the television as `reject` ("a deals banner, not a
ranking lede") and the laptops as `match lede-collage`.

**What the three have in common is not what the type file said.** It was drafted as *"the
number one alone, presented as chosen — a packshot carrying a verdict"*, `products_in_frame:
one`, with the mark mandatory. Against the examples: the laptops frame carries THREE
products, and the television frame carries NO mark at all. Both halves of the definition
were wrong.

**Measured, the three are one of the tightest clusters in the corpus:**

| | TV DEALS | AirPods | LAPTOPS |
|---|---|---|---|
| ground value | 1.00 | 0.91 | 0.99 |
| ground saturation | 0.55 | 0.60 | 0.60 |
| hue spread | 138.6° | 179.3° | 176.7° |
| products | 1 | 1 | 3 |
| display type | huge | none | huge |
| mark | none | sticker | plaque |

**So the type is a DESIGNED PROMOTIONAL HERO**: cut-out product on a loud designed ground,
carrying oversized display type, a verdict mark, or both — and **at least one of the two is
always present**.

### The boundary against `lede-collage` is words, not count

A winner frame carries display type or a mark; a collage carries neither and argues with
the units alone. Checkable at a glance, and it survives a frame having several products.
The old boundary was product count, which is exactly why two of the owner's three were
misfiled.

**Applying that boundary re-files a fourth frame**: the five robot vacuums under a
`CNET LAB TEST WINNER 2025` plaque, filed `match lede-collage` in batch A. It is the same
construction as the laptops frame. Re-filed by the owner's own rule rather than by a new
judgement, and flagged as such in the ledger.

**And it demotes a fifth.** A near-white sheets packshot with a small `GOOD HOUSEKEEPING`
badge was filed `match lede-winner` by this session in batch C. It measures 0.03 saturation
and 0° of hue spread against the owner's three at 0.55–0.60 and 138–179° — a quiet packshot,
not a loud promotional hero. Demoted to `variant-candidate`; whether it belongs here or with
`07-identity-pack` plus an accolade is the owner's call.

**The "bimodal ground" reported this morning was my own misclassification, not a property
of the type.** It existed only because that quiet frame was counted as a match. With it
demoted, the five frames read value 0.99, saturation 0.55, texture 1.5 — one mode.

### `PARTS/title` is new and it is the centre of the type

Display type in this corpus is **set larger than any word elsewhere in the namespace, sits
BEHIND or ACROSS the cut-out units, and is routinely CROPPED by the frame edge** — `LAPTOPS`
runs off both sides. **This is the one place in the library where type may be cut by the
edge**, and it is deliberate: G10's safe area governs words that must be READ, and a display
word running off the frame is being used as a graphic. The mark's own words still keep the
margin.

### The instruments were counting corrections twice

These are the first corrections the toplist namespace has taken, and both
`check_toplist_evidence` in `scripts/validate.py` and `scripts/ground_audit.py` were
counting every ledger record. An append-only ledger records a correction as a NEW record, so
a re-filed frame appeared under **both** the old family and the new one. Both now read the
LAST record per hash, which is what an append-only ledger means. `lede-winner` reads 5 and
`lede-collage` 6, not 6 and 8.

### A consequence worth stating plainly

With the two loud frames gone, **`lede-collage` has ONE observation of the type as it is
defined** — several distinct products, cut out, on one ground. Its other five are two other
shapes it had been absorbing: three of "several VIEWS of one product" and two of "one
subject in several states". That is a curation problem this ADR does not solve.

**Consequences.** `registry/toplist-types/lede-winner.md` 0.4 → **0.5**, rewritten:
PURPOSE, TRIGGER, BOUNDARY, SKELETON, `PARTS/subject`, `PARTS/ground`, `PARTS/title`,
`MARKS` (gaining `none` as an observed form), SLOT CONSTRAINTS, NEGATIVE. Four correction
records appended to `ingestion/observations.jsonl` — append-only, the superseded records
stay. `scripts/validate.py` and `scripts/ground_audit.py` read the latest record per hash.
`round-1/prompts.md` prompt 5 rewritten onto display type and a `plaque`.

**Not done.** `lede-collage` is not rewritten and the two absorbed shapes are not split out.
Nothing is rendered.

---

## ADR-075 · 2026-09-09 · SPEC §6.4's competitor brand-mark clause does not bind the toplist namespace

**Owner instruction, 2026-09-09:** "riêng với top list, không giới hạn *competitor brand
marks never appear in prompts*."

**Why the clause could not survive contact with this format.** SPEC §6.4's policy has two
halves: no prompt may aim to reproduce a specific source image, and competitor brand marks
never appear in prompts. The second half was written for a product page, where the library
argues for ONE product and a rival's logo has no business in the frame. A top-N listicle is
by definition about several named competing products, so applied there the clause refuses
the format's whole subject rather than a detail of it.

It had already cost something. `lede-lineup` and `lede-collage` shipped `reserved` at
ADR-069 with TWO blockers named in their BLOCK sections, and this was the second.

**The first half still binds**, here as everywhere: no prompt may aim to reproduce a
specific source image. Nothing about depicting a real product licenses copying a
photograph of it.

### The narrower rule that replaces it, and it is easy to miss

**A real brand may be DEPICTED. A brand may not be INVENTED.**

Depiction comes from the reference photo the owner attaches, which is what G1 already
governs. Invention is what happens when a prompt with NO reference asks for branded units:
the renderer produces a plausible logo belonging to nobody. That is a fabricated brand, a
different fault from a competitor's real one, and no permission in this ADR covers it.

The consequence is immediate and slightly counter-intuitive: `lede-lineup` and
`lede-collage` still specify unbranded units, and `round-1/prompts.md` 3 and 6 still say
so — but for a new reason. While the one-photo limit stands those prompts attach nothing,
so branded units could only be invented ones.

### What is NOT covered, stated because the two are easy to conflate

**A certification seal, a press logo and a third-party AWARD mark stay refused.** G16 marks
those `LAW, not taste`. The reason is different in kind: a competitor's brand mark is the
mark of the thing being depicted, while an award mark is the mark of a body vouching for
it, and reproducing that is a claim about the issuer rather than about the product. Three
of `lede-winner`'s five corpus frames carry one — `CNET LAB TEST WINNER`, `CNET PEOPLE'S
PICKS`, `GOOD HOUSEKEEPING BEDDING AWARDS` — which makes it the most-breached refusal in
the namespace and the obvious next decision, but it is not this one.

### Consequences — rule 6c sweep on `"brand mark"`: 61 hits, 23 files, 7 in TEACHES

- `SPEC.md` §6.4 — the policy gains **one named exception**, pointing at §3.7, in the same
  shape §3.6 already uses for the Vietnamese GIF cards.
- `registry/toplist-instruction.md` — its *Global rules* entry is **rewritten**: the clause
  does not bind, the depict/invent distinction replaces it, and the award-mark refusal is
  named as still standing.
- `registry/toplist-types/lede-lineup.md` — BLOCK goes from **two decisions to one**.
- `registry/toplist-types/lede-collage.md` — the same.
- `registry/toplist-types/round-1/prompts.md` — the paragraph explaining why 3 and 6 carry
  no brands is **rewritten to the new reason**.
- `registry/toplist-types/lede-testing.md` and `lede-winner.md` both bar *a competitor's
  product* in their NEGATIVE blocks. **Both stand.** Those are composition rules — one unit
  under test, one winner — not the §6.4 policy, and neither would be improved by a rival in
  the frame.
- `registry/types/03-spec-split.md` and `_staging/07-identity-pack.md` carry the remaining
  TEACHES hits. **Both stand**: they are image types, and this exception is named to §3.7
  alone.

**Nothing becomes routable.** `lede-lineup` and `lede-collage` stay `reserved` on the
one-reference-photo limit, which is now their only blocker.

---

## ADR-076 · 2026-09-09 · A prompt may attach one reference photo per product; the cap was the app's, the rule was about the CALL

**Owner instruction, 2026-09-09:** "đối với các loại ảnh cần nhiều input trong khi app chỉ
tham chiếu 1 ảnh product, hãy cứ xuất prompt đầy đủ, tôi sẽ mang prompt đi gen ảnh ở chỗ
khác (google flow)."

**ADR-021 declared the render capability on 2026-08-17: "one prompt, one generation call, at
most one reference photo attached. No compositing, no edit chains, no post assembly."** Two
different things were bundled into one sentence and only one of them was ever the point.

- **One generation call, nothing assembled afterwards.** That is the rule. It is why
  `multi-pass` died at ADR-021, why `steps[]` was retired at ADR-039, and why the value was
  deleted from the vocabulary at ADR-067. **Unchanged.**
- **At most one attached photo.** That was a fact about the owner's own app, written into
  the library as if it were a fact about rendering. It is now lifted.

**A prompt may attach one reference photo per product in frame, and it still makes one
call.** Where the owner's app takes fewer than the prompt needs, **the prompt still ships in
full** and is rendered in a tool that takes several. A prompt is never trimmed to fit a
tool — which is the part of the instruction worth quoting back, because trimming is exactly
what this library did for three weeks.

### What it unblocks, and what it does not

`lede-lineup` **0.3 → 0.4** and `lede-collage` **0.4 → 0.5**, both `reserved` → **active**.
Their BLOCK sections become `ATTACHMENTS`. **Nothing about either picture changed** — they
were drafted, measured, given grounds and marks, and held back by an attachment count.
Six of the seven toplist types are now active; only `lede-authority` is reserved, and it is
reserved behind G16's *named expert* row and `mapping/slot-rules.md`'s own out-of-scope
declaration rather than behind anything this ADR touches.

**It does not license invention.** ADR-075 permitted depicting a real brand from an attached
reference; with references now attachable per unit, a lineup carries the real named products.
A prompt with no reference still may not ask for branded units, because that produces a
fabricated logo.

**It does not reopen multi-pass.** One call. Nothing assembled. `scripts/validate.py` still
errors on `generation_mode: multi-pass`, which is the check ADR-067 left behind.

### Consequences — rule 6c sweep on `"one reference photo"`: 14 hits, 12 files, 7 in TEACHES

- `CLAUDE.md` rule 6b — **rewritten**. It is the thin adapter's statement of ADR-021 and it
  carried the cap.
- `query/runbook.md` Step 3's RENDER CAPABILITY — **rewritten**, with the distinction
  between the count and the call stated in the place types are told to read.
- `query/output.schema.json` — both `pipeline` descriptions, **rewritten**. The
  `attachments` array already permitted several and needed no change.
- `eval/render-test.md` Step 2 — **rewritten**.
- `registry/vocabulary.yaml` — the `toplist_frame_populations` comment said `many` reserves
  a type. **Rewritten**; it no longer does.
- `registry/toplist-instruction.md` — layer 1 of SELECTION, and *The two decisions* becomes
  *What this namespace is still waiting on*, which is now one: G16's third-party award row,
  breached by 3 of `lede-winner`'s 5 corpus frames.
- `mapping/toplist-rules.md` — the reserved list, the `many` gate, the live-pool paragraph
  and both preference rows.
- `registry/toplist-types/lede-testing.md:115` — a CHANGELOG line reading "one product, one
  reference photo". **History, stands.**

**`registry/toplist-types/round-2/prompts.md` is new**: seven prompts, one per type, on
seven products none of round 1 used, at the live version of every type. Prompts 3 and 6 ask
for five and four attachments and carry real brand marks — the first prompts this library
has ever written that its own app cannot run, which is the point of the instruction. Round 1
is superseded and kept as the record.

**Nothing is rendered.** Six active types, and not one of them has a render behind a single
clause.

---

## ADR-077 · 2026-09-10 · A fourth namespace for the LP2 product gallery, built as a CO-REGISTRY because its page has twelve slots and not one

**Owner instructions, 2026-09-10**, in order: the project is pivoting the way the top-N
listicle already did — toplist is one landing-page type, advertorial and listicle are two
more, and landing-page types can SHARE image types; create `registry/pdp-dr-types/` holding
the image types of LP2, the product page; and ask before building. Four questions were put
and four were answered, and the answers are what this ADR implements rather than what the
first instruction implied.

**The LP number was corrected in the same exchange.** The owner's first message called this
corpus LP3; the second called it LP2; asked which, the owner answered *"trước đây tôi quy
định nhầm, đúng ra phải là LP2 chứ không phải LP3."* So **LP2 is the product page**, and the
`lp3-` prefix on ten of this corpus's eleven prefixed source slugs is the old mistake
preserved in an append-only ledger. `ingestion/observations.jsonl` cannot be rewritten and
is not; `ingestion/runbooks/classify-batch.md` still names the folder `LP3 assets learn`
because that is what the folder was called. **A reader who follows an `lp3-` slug to this
namespace has followed it correctly.**

### The four answers

| question | answer |
|---|---|
| what does the folder contain | **only types the shared registry does not have.** The 13 ACTIVE types this corpus already uses stay in `registry/types/` and a PDP page routes to both |
| evidence bar for a NEW file | **≥3 distinct sources** on this corpus — 15 ids clear it |
| the 7 `_staging/` types built from this corpus | **move**, wholesale |
| the LP number | **LP2**; the earlier LP3 was the owner's own mis-numbering |

**Answers 2 and 3 collide and the resolution is stated rather than assumed.** The threshold
governs which files are WRITTEN; it does not govern which are MOVED. All seven staging files
move, and the three below the bar — `03-spec-lineup` at 2 sources, `05-social-card` at 1,
`07-identity-inhand` at 1 — arrive `status: reserved`, which is what they already were. The
folder is therefore **7 moved + 4 written = 11 files**.

### Why a namespace, when the reason the other two have one does not apply here

This is the part that had to be got right, because copying ADR-069's justification would
have been wrong. **SPEC §3.6 and §3.7 both rest on the same fact: that page has ONE image
slot**, so the role shortlist of §7.2, the cross-slot pass of §7.3, the coverage pass of
§7.5 and one-type-once have nothing to act on.

**A product gallery carries about twelve slots.** Every one of those passes applies to it,
and applies harder than to a six-slot advertorial, because twelve slots is more places for
one argument to appear twice. The one-slot reasoning transfers not at all.

Three differences of LAW carry it instead, and each is measured or minuted rather than
argued:

1. **Text is baked into the image.** Owner decision of 2026-08-31, taken against the
   advisory recommendation of the session that raised it. Every type here may declare
   `text_layer`; advertorial and listicle types overwhelmingly do not.
2. **The ground rule is measured on this corpus.** ADR-068: the outer 8% ring of 119 frames,
   VALUE median **0.89**, SATURATION median **0.06**. ADR-073 already proved this class of
   rule does not travel — it had to be re-measured for the toplist corpus, where TEXTURE
   split the namespace in two.
3. **Marketplace legality gates every tile.** `mapping/slot-rules.md` cross-rule 5 bars the
   ugc register and `01-pain-scene` from marketplace galleries and bars `--rivals` outright.
   An advertorial never meets that gate; a syndicated gallery meets it twelve times.

### CO-REGISTRY, not a fork — and the id grammar follows from the owner's answer

`registry/gif-types/` and `registry/toplist-types/` abandoned `{step}-{job}-{device}` because
their ids are ARGUMENTS. **This namespace keeps the grammar**, and that is a consequence of
answer 1 rather than a preference: the folder holds only what the shared registry lacks, so a
PDP page reads `registry/types/` and `registry/pdp-dr-types/` **in one pass**, and two id
grammars in one pass is how a reader loses track of which law applies. Anatomy and frontmatter
are an image type's, plus `blocked_by`. Promotion out is a `git mv` and a status change.

**No copies here, therefore no drift instrument.** ADR-070 gave the toplist namespace
`copied_from` + `copied_at_version` and a validator warning because the owner had chosen
verbatim copies. Nothing here is a copy, so that machinery is absent — **and the residual
exposure is named instead of discovered**: a skeleton may CALL a part defined in another file
and nothing validates that call. Two such calls exist — `07-identity-callout`'s
`[PRESENTATION]` and `[SETTING]` both reach into `03-spec-callout`'s `PARTS` — and both are
registered in `mapping/pdp-dr-rules.md`. The register is the whole instrument, and this
sentence is its weakness stated in advance rather than found later.

**ADR-070's other finding does NOT bite here, and checking that was the point.** A gate keyed
on a parent's id does not reach a copy, so every gate had to be restated by toplist id. This
namespace holds no copies and every gate in `mapping/slot-rules.md` names an ACTIVE type that
is still active under the same id, so **nothing is restated** and `mapping/pdp-dr-rules.md`
says so rather than leaving a reader to wonder.

### The four new files, and why every one of them is reserved

The evidence bar admitted 15 ids at ≥3 distinct sources. Seven are ACTIVE and stay put; four
are among the movers; **four had no file and got one.** Not one of them got a promotion.

| new file | obs / sources | what it is blocked on |
|---|---|---|
| `07-identity-callout` | 6 / **5** | a re-filing pass — see below |
| `04-proof-stat` | 4 / 4 | A15 and the owner substantiation decision |
| `05-social-testimony` | 3 / 3 | G14, which no evidence unblocks |
| `06-relief-animal` | 3 / 3 | the absorption ladder |

**`07-identity-callout` cleared criterion 1 on paper and is reserved anyway**, which is the
finding of this pass. Five distinct sources is what the ledger says; re-reading the six
breakdowns, **two are unambiguously a subject ringed by labelled satellites** and the other
four read as `06-relief-claimstack`, as `07-identity-pack` with a text layer, or as a
packshot carrying one badge. ADR-065 wrote the remedy into `07-identity-inhand` and it is
applied here a second time: *the first job is re-filing rather than hunting*, and **a batch
summary naming a pattern three times is not a count.** One of its five sources, `feicemat-v2`,
already sits in `03-spec-callout`'s own founding table — so criterion 2 is a demonstrated
fact here rather than an unrun test.

**`06-relief-animal` argues against its own existence and ships anyway.** Three exemplars, three
registers — a studio seamless, a panning documentary frame, a phone snapshot. What they share
is that the beneficiary is an animal, which is a SUBJECT and which SPEC §3.2 absorbs as an
axis before it will absorb a type. The file says so, names the `beneficiary` axis as the
likely answer, and states why this namespace cannot take that decision: settling it means
widening `PARTS/subject` on three ACTIVE types, which answer 1 puts outside this folder's
charter. Its device value `animal` names WHAT is photographed rather than HOW the argument is
made — the exact fault ADR-065 corrected twice — and `vocabulary.yaml` marks it reserved and
provisional for that reason.

**`04-proof-stat` ships with NO SKELETON**, which is the state ADR-066 §4 put it in and the
honest carry-over. A skeleton has to say where a number comes from and no rule in this repo
does.

**`05-social-testimony` is blocked by something no evidence can move.** G14 binds the SLOT,
and a testimonial thumbnail sits beside a name by definition, so there is no page arrangement
under which the type is both itself and legal. The file exists to record that the corpus
contains the pattern, not to offer a way to draw it.

### The measured finding the routing table exists to carry: step 1 is EMPTY

Counted from the ledger over **159 observations across 26 source pages**, batches
`2026-08-31-A`/`-B` and `2026-09-03-C` through `-H`, filed against 41 distinct ids. Four
ACTIVE types appear on **no page** in this corpus, and two of them are the whole of the Trust
Ladder's first rung:

| absent from all 26 PDP sources | present in the advertorial/listicle corpus |
|---|---|
| `01-pain-scene` | yes |
| `01-pain-split` | yes |
| `03-spec-explode` | yes |
| `03-spec-split` | yes |

And the reverse once: **`06-relief-scene` appears here and nowhere in the older corpus.**

`mapping/slot-rules.md` prefers `01-pain-scene` for both `hero` and `problem-agitation`. On a
product gallery that points at a type the format does not use. So `mapping/pdp-dr-rules.md`'s
`hero` row names one type and it is a relief type — and unlike `mapping/toplist-rules.md`,
which declares itself a hypothesis in its own first paragraph, **this table is counted.**

**What it does not prove, written beside it.** The owner selects what enters a batch and the
harness classifies it, so 26 pages is what was FILED, not a sample of the format. This is
*absent from what was filed*. `03-spec-explode` in particular is a plausible gallery tile that
did not turn up. The limit is written next to the rows because the alternative is a rule that
feels obvious, which is precisely the shape ADR-068 caught moving a whole render set off the
market.

### Enforcement fed known-bad input before being believed

Seven injected faults, **seven fired**, control clean at 0 errors and the tree restored to 0
errors afterwards: a reserved type with `blocked_by: null`; `blocked_by` on a type whose status
is `active`; a reserved type with its `## BLOCK` section renamed; `blocked_by` on a file in
`registry/types/`; a file whose id is absent from `vocabulary.pdp_dr_types`; a
`pdp_dr_types` entry with no file; and an id present in both `registry/types/` and
`registry/pdp-dr-types/`.

Two of those are worth naming. **The id-collision check exists only in this namespace**, because
this is the only one that shares an id grammar with `registry/types/` — and a collision is
exactly what a half-finished promotion looks like. And the **`blocked_by`-in-the-wrong-registry
message is placed AHEAD of the generic unknown-key error**, which is ADR-069's own lesson
applied without having to relearn it: *"unknown frontmatter key" does not tell a reader why
this namespace has no text* — or here, which namespace the key belongs to.

**A fourth membership list was found not knowing about a namespace, and this time in the same
diff that created it.** `scripts/validate.py`'s render-ledger check tests `types`, `staging` and
`toplist_types`; three of the seven moved files carry founding renders in
`eval/render-tests.jsonl`, so **every one of those records would have warned as an unknown type
the moment the files moved.** ADR-070 found the same class of gap in `adr-sweep.py`'s tuples a
day after ADR-069 opened it; this one was caught before it landed.

### Consequences — rule 6c sweeps on `"namespace"` (218 hits, 41 files, 32 TEACHES) and `"_staging"` (46 hits, 15 files, 9 TEACHES + 1 UNCLASSIFIED)

- `registry/pdp-dr-types/` — **new**, 11 files. Seven moved by `git mv` from
  `registry/types/_staging/` with their history intact, four written. Every one is
  `status: reserved` with a `blocked_by` and a `BLOCK`. `ready-to-push/` moved with them: all
  three types it carries prompts for are LP2 types.
- `registry/types/_staging/` — 9 files → **2**, `02-cause-scene` and `03-use-rail`, which are
  the two that appear on no page in this corpus. Its README is **rewritten**: the
  `ready-to-push/` section becomes a convention that is not folder-specific, and a section is
  added saying the CORPUS decides which folder a draft goes to.
- `registry/pdp-dr-instruction.md`, `mapping/pdp-dr-rules.md` — new.
- `SPEC.md` — **§3.8 added.** `SPEC.md:32` (the not-routable clause of §1) and `SPEC.md:85`
  (absorption ladder step 4, *"Goes to `_staging/`"*) both **rewritten**: the second was
  teaching every future curation pass to file an LP2 cluster in the wrong folder.
  `SPEC.md:157`, *"A second, smaller registry governs motion"*, **stands** on ADR-069's own
  reading — the word counts its ordinal, not the registries.
- `ingestion/runbooks/curate.md:33` — **rewritten** for the same reason as the ladder.
- `registry/vocabulary.yaml` — `pdp_dr_types` (11 ids), and devices `stat`, `testimony`,
  `animal`. The `animal` entry ships with its own objection in a comment.
- `scripts/validate.py` — `validate_pdp_dr_type_file`, the `blocked_by`/`BLOCK` pairing, the
  vocabulary closure both ways, the id-collision check, the specific wrong-registry message,
  `pdp_dr` in `check_multipass_declarations` and in the render-ledger membership list, and the
  count in the summary line. `validate_type_file` gains `where_prefix` and `extra_optional` so
  the co-registry reuses it rather than owning a second copy of those checks.
- `scripts/adr-sweep.py` — the three new paths into `TEACHES`, in the same diff that created
  them. **And `ingestion/prompts/` too**, which this sweep found UNCLASSIFIED: those files tell
  a harness how to classify, so a hit in one is an instruction somebody follows.
- `CLAUDE.md` — two entry-point rows and rule 4.
- `registry/toplist-instruction.md:308` — **rewritten**: it cited the `ready-to-push/` folder
  by a path that no longer exists, and it now also records that the fourth namespace took the
  other road on copying.
- `registry/pdp-dr-types/07-identity-inhand.md:43` and `07-identity-pack.md:44` — both said the
  identity family's home was undecided between `registry/types/` under a new step and *"its own
  namespace like `registry/gif-types/`"*. ADR-069 left both standing and said the option had
  got cheaper. **The decision is taken here and both are annotated rather than deleted**, because
  the paragraph is the reasoning the decision was taken against, and because each is still half
  right: this is a namespace, but a co-registry.
- `registry/pdp-dr-types/03-spec-callout.md`, `06-relief-claimstack.md`, `07-identity-pack.md`
  — three stale `_staging/ready-to-push/prompts.md` paths **rewritten**.
- `registry/pdp-dr-types/ready-to-push/README.md` — the *Where this folder sits* section
  **rewritten**; it described a folder it is no longer in.
- `ingestion/anchor-set.md:71`, *"`03-use-rail` does now exist in `_staging/`"* — **stands**;
  `03-use-rail` is one of the two that stayed.
- GENERATED — `registry/index.yaml` and `dist/app-bundle/` regenerate; **neither gains a
  pdp-dr type**, which is the namespace doing its job.
- `registry_version` unchanged: no active type, no active structure and no routing outcome
  moves.

### What is NOT done

**Nothing in this folder routes and no prompt has been written against this namespace's law.**
Three of the eleven carry FOUNDING RENDER ROUND sections from their time in `_staging/`; those
renders are real, their measurements stand, and they were taken before any of this existed.

Four decisions gate the folder and three are the owner's: the **substantiation rule** behind
A15 (blocks `04-proof-stat`, `04-proof-instrument`, `04-proof-interface`); the **trademark
question** of 2026-08-18 (blocks `07-identity-callout`'s mark library); the **`beneficiary`
axis** (blocks `06-relief-animal`, and settling it touches three active types). The fourth is
**criterion 2**, the router-confusion test, which no owner decision unblocks and which is the
binding gap on the two best-evidenced files here.

The **re-filing pass** `07-identity-callout` and `07-identity-inhand` both ask for is not run.
It is a curation operation, it moves observations between ids in an append-only ledger by
adding correction records, and folding it into a namespace diff would have made two decisions
look like one.

---

## ADR-078 · 2026-09-11 · Three types the corpus earned, one it retired, and the six findings that belong to the namespace rather than to any file

**Owner instruction, 2026-09-11: "sửa theo khuyến nghị."** The recommendations were the four
at the foot of `registry/pdp-dr-types/_CURATION-2026-09-11.md`, written after the 157-image
drop was classified across batches A–J. This ADR is all four landing.

### What the recommendations were, and what each cost

| | recommendation | what shipped |
|---|---|---|
| 1 | write the three Tier-1 files | `03-spec-claimstack`, `03-spec-dimension`, `03-spec-hero` |
| 2 | retire `07-identity-callout` | `status: deprecated`, `replaced_by: 03-spec-callout` |
| 3 | `02-symptom-callout` has its third source | a file, reserved, blocked on criterion 1 |
| 4 | the six findings into the instruction | a new section, and three corrections elsewhere |

`registry/pdp-dr-types/` goes **11 → 15 files**. Tier 2 (eight ids at 3–4 sources) and Tier 3
(twenty-three ids below three) are deliberately NOT drafted: the recommendation was the three
that clear criterion 1, and drafting eight more on 3 sources would repeat the mistake
`07-identity-callout` was just retired for.

### The three Tier-1 files, and why each is still reserved

| id | sources | obs | blocked on |
|---|---|---|---|
| `03-spec-claimstack` | **8** | 15 | criterion 2 against `06-relief-claimstack` |
| `03-spec-dimension` | **7** | 11 | criterion 2 against `03-spec-callout` |
| `03-spec-hero` | **6** | 18 | criterion 2 against `06-relief-hero` |

**All three clear criterion 1 and all three are blocked on the same test, which is the finding
rather than a coincidence.** Each is a JOB SIBLING of something that already exists: the same
device, the same picture, a different job. SPEC §3.1 says two jobs are two types however alike
the picture, and it is right — but it produces three pairs a router has never been asked to
separate, on a page kind where both members of every pair are plausible for the same slot.

**That is now the single largest piece of unfinished work in the namespace**, and
`registry/pdp-dr-instruction.md` says so in those words.

`03-spec-hero` is the sharpest case. Counting it with `06-relief-hero` (ACTIVE, 19 sources)
and `03-use-hero` (1 source, deliberately no file), **one photograph carrying a baked headline
appears in 23 of the corpus's 36 sources.** It is the commonest construction on a
direct-response product page and the registry half-owns it already.

### `07-identity-callout` is retired, and it was answered twice on one day

Deprecated rather than deleted: the ledger carries six observations under that id and a reader
has to be able to follow them. `status: deprecated`, `replaced_by: 03-spec-callout`,
`blocked_by: null`, and the `BLOCK` section becomes `RETIRED` — which the validator enforces,
since it errors on a `BLOCK` that no longer blocks.

**A render answered it.** Set `clip-fan-01` declared this type its CONTROL and predicted,
before the render, that it would come back indistinguishable from a `03-spec-callout` prompt —
because with the style lock in force, ground, light, grade, type and accent were identical
between the two, leaving only the argument to tell them apart. It came back indistinguishable.

**And a corpus answered it.** The 157-image drop put `03-spec-callout` at ten distinct sources
and found **not one new frame** for `07-identity-callout`. `hydrovia` img-04 is the worked
case: five pills ringing a bottle naming *Stainless Steel*, *Durable Glass Body*, *USB
Rechargeable* — materials and capabilities, which is what the spec callout's own `use_when`
claims. It filed there without difficulty.

**What the file already said is the reason, and it stands as the record.** Six observations
across five sources cleared criterion 1 on paper; re-reading the breakdowns, only two were
unambiguously that device. The count was never the evidence. That is `ADR-065`'s
`07-identity-inhand` finding arriving a second time, and this is the first time this library
has retired a type for it rather than deferring.

### `02-symptom-callout` gets the file ADR-066 deferred

ADR-066 renamed it from `02-symptom-halo`, recorded it at two sources, and said *"gets no file
until it has three."* `glowy-liff` is the third. The file ships reserved, blocked on criterion
1 by two and on criterion 2 against `02-symptom-rail` — a rail LISTS complaints in a band, a
ring SURROUNDS a subject with them, and the two stand at 4 and 3 sources on this corpus, so a
promotion decision will have to take them together.

### The six findings, and where each went

They went into `registry/pdp-dr-instruction.md` rather than into any type file, because each
binds every type in the namespace.

1. **G3 does not hold uniformly, and the split is precise.** It HOLDS for pressure, verdicts
   and states; it INVERTS for heat, lift and detection. **The market reaches for the colour of
   the PHENOMENON, not the colour of the judgement.** One source states its own inverted code
   in words and then contradicts itself on the same device. — *And the distinction nothing in
   this repo had stated: a product's OWN indicator colours are not signal marks. G3 does not
   reach an LED wavelength, a status strip or a charging glow, and four sources would be
   miscounted by a reader who did not hold that.*
2. **Five honest-substantiation behaviours, found in the wild** — the instrument in shot, the
   declared error band, the comparison scale, the approximation sign, the stated limitation.
   All five are better models than the footnote shape A15 proposes from a single frame.
   **A maximum is falsifiable; a point figure on a render is not** — which is the whole of what
   A13 and A15 are each trying to say, in one sentence.
3. **The slot-spending habit, 7 of 10 sources.** The standing argument for `03-spec-lineup`,
   recorded with its own counter-argument: compressing costs the scale cue.
4. **Two rules the corpus breaks on purpose.** G7 impossible settings, twice. And **G13 names a
   configuration this library cannot render at all** — a crying infant in a cot — so a
   baby-monitor category has a gallery slot no prompt craft can fill.
5. **Motion in a still**: three instances, two sources, no device name.
6. **A third mark class**, the compatibility bar, reached by nothing in G16, G14 or the two LAW
   rows, and banned outright by G6 which bans logos.

### Consequences — rule 6c sweeps on `"identity-callout"` (28 hits, 10 files, 7 TEACHES), `"claimstack"` (76, 14, 10) and `"deprecated"` (32, 13, 7)

The sweeps found four files teaching the opposite and all four are corrected here.

- `mapping/pdp-dr-rules.md` — the **cross-file call register** listed two LIVE calls from
  `07-identity-callout` into `03-spec-callout`. The caller is retired, so both rows are STRUCK
  rather than deleted and the register now reads **zero live calls**. This is the register
  doing exactly the job it was built for: it is the only instrument watching those calls, and
  without the sweep it would have gone on describing a dead dependency as live.
- `registry/pdp-dr-instruction.md` — three corrections. The call-cost paragraph cited the same
  dead call; the trademark-question blocker named the retired type; and the
  still-waiting-on list was counted at eleven reserved files.
- `registry/pdp-dr-types/03-spec-callout.md` — its BLOCK said criterion 2 was *"unrun and no
  longer hypothetical"* against a sibling. **That test has now been run and that sibling lost**,
  so the passage is rewritten to say so and to name the two confusion tests that remain —
  against `02-symptom-callout`, which now has a file, and against `03-spec-dimension`, which
  puts labelled graphics on a plain product exactly as it does.
- `registry/pdp-dr-types/06-relief-claimstack.md` — gains `avoid_adjacent: [03-spec-claimstack]`
  and a note that its criterion 2 is now a NAMED PAIR rather than a risk in the abstract.
- `registry/vocabulary.yaml` — `pdp_dr_types` 11 → 15, and one new device `dimension`, which
  names how the argument is made rather than what is photographed (the test ADR-065 applied
  when it renamed `ingredient` to `stilllife`).
- `SPEC.md:340`, *"Demotion: `deprecated` requires `replaced_by`"* — **stands, and is
  satisfied**; this is the first demotion in the pdp-dr namespace and the first time that
  clause has been exercised there.
- `ingestion/runbooks/classify-batch.md:114` and `mapping/slot-rules.md:59` — ordinary uses of
  "criterion 1" in craft prose. **Both stand.**
- GENERATED — `registry/index.yaml` and `dist/app-bundle/` regenerate; **neither gains a
  pdp-dr type**, which is the namespace doing its job.
- `registry_version` unchanged: no ACTIVE type, no active structure and no routing outcome
  moves.

**One soft-limit warning was worked rather than ignored.** `06-relief-claimstack` sat at 21,883
discretionary characters against ADR-013's 22,000 soft limit, so the sibling note pushed it
over. The warning's own remedy is *"move workings to the commit message"*, and that is what
happened: the note in the file is now two sentences and the reasoning is in this ADR.

### What is NOT done

**Nothing in the folder routes.** Fourteen reserved files and one deprecated; `index.yaml`
gains none. The three Tier-1 files have no render and no prompt.

**The three router-confusion tests are not run**, and they are the same test three times.

**Tier 2 is not drafted** — eight ids at 3–4 sources, each one or two sources short.

**The re-filing pass is still not run.** Retiring `07-identity-callout` does not re-file the
four observations that belong to `06-relief-claimstack` and `07-identity-pack`; it only stops
them being counted toward a type that no longer exists.

---

## ADR-079 · 2026-09-11 · LEDE is the fifth operation, `source_dirty` is scoped to what the bundle carries, and the repo gets a front door

**Owner question, 2026-09-11: "repo này đã sẵn sàng để gửi dev chưa?"** The audit found four
things and the owner asked for three of them fixed. This is those three. The fourth — the
export → `content.json` step — is not done and is named in the README as the blocking one.

### 1. `registry/toplist-types/` is absent from the bundle because LEDE is a fifth OPERATION

The audit read the absence as an oversight, which is exactly how it looks. It is not, and the
reason had never been written down anywhere.

`scripts/build-app-bundle.py` says in its own header that *"anything missing is a rule the app
cannot apply and will silently skip"*, and it ships `gif-types/` while omitting
`toplist-types/`. Both namespaces sit outside `index.yaml`, so the apparent rule — *outside
the index, outside the bundle* — does not explain the difference.

**The difference is the operation.** Gif suggestion is a STEP of QUERY, `query/runbook.md`
Step 5c and 5d, so a page routed from `content.json` gets gif verdicts and needs gif law in the
bundle. Toplist is not a step of anything: SPEC §3.7 says its input is the `product` block and
not `content.json`, which is QUERY's input by definition. **It is a fifth operation, and
`SPEC.md` §1 did not have a row for it.**

So the fix is not to add files to the bundle. It is to name the operation:

- `SPEC.md` §1 gains a **LEDE** row — input, procedure, output — and a paragraph saying why
  `registry/toplist-types/` is therefore absent from the bundle, and why
  `registry/pdp-dr-types/` is absent for the opposite reason: pdp-dr is INSIDE QUERY (§3.8) and
  promotion out of it is a `git mv` into `registry/types/`, so a promoted type enters
  `index.yaml` and the bundle by itself.
- `scripts/build-app-bundle.py` gains the same reasoning at the point a reader would ask.

**Ship toplist the day an app implements LEDE, and not before.** Shipping law an app cannot act
on is worse than omitting it, because the manifest would then assert coverage that does not
exist.

**The sweep caught a second error while checking the first.** `SPEC.md:16` read *"A conforming
harness implements three operations"* over a table of FOUR, and this change would have made it
five. Corrected, with the sentence a consuming dev actually needs: an app on the bundle
normally implements QUERY alone.

### 2. `source_dirty` was measuring the wrong tree

`bool(git status --porcelain)` over the WHOLE repo. The flag's job is to tell a vendoring app
that the sources behind its copy were uncommitted, and a dirty file the bundle does not carry
says nothing about that.

**Measured: four consecutive bundle commits — `4cebcbe`, `108ef97`, `4f1cf19` and the one
before this — reported DIRTY TREE on account of one unrelated toplist lane that touched no
bundled file.** A flag that is true whenever any parallel session has uncommitted work is a
flag that has stopped carrying information, and this repo runs parallel lanes by design.

Now scoped to the bundle's own sources: every path in `FILES`, plus the source DIRECTORIES in
`DIRS` so a new or deleted type file counts.

**Fed known-bad input before being believed**, three cases:

| case | want | got |
|---|---|---|
| only the unrelated toplist lane dirty | False | False |
| `registry/rules.md` dirty — a vendored file | True | True |
| a NEW file appears in `registry/types/` | True | True |

Restored clean at False. This is the fourth instrument in this repo to be scoped after it was
found reporting on something other than its subject, and the first where the fault was breadth
rather than a blind spot.

### 3. `README.md` — the repo had no front door

`SPEC.md` is a contract and `CLAUDE.md` says of itself that it is a *thin Claude Code adapter*.
Neither is a place to start. The README is written for four readers, says which four files each
should open, and does three things a contract cannot:

- **states the known gaps up front** — the missing export converter, the empty picks ledger, a
  namespace that routes nothing, and an operation no app implements
- **warns before the converter is written** that a real page export satisfies none of the QUERY
  input contract: empty `sections`, all eight `product.attributes` absent against nine gates
  that read them, and `lpTypeId` with no home in the schema
- **names the four habits** that explain most of what looks unusual here — a clause needs a
  failed render, evidence counts SOURCES, generated views are regenerated, ledgers are
  append-only

### Consequences — rule 6c sweeps on `"operations"` (3 hits, 3 files, 1 TEACHES) and `"source_dirty"` (3, 2)

- `SPEC.md` — §1 gains the LEDE row and the bundle-absence paragraph; line 16's *"three
  operations"* corrected to five. **This is a contract change**: a conforming harness now has
  five operations to implement, and an app on the bundle is told it needs one of them.
- `scripts/build-app-bundle.py` — `sources_dirty()` replaces the unscoped check, and the
  two-namespace absence is documented where a reader would ask.
- `README.md` — new.
- GENERATED — `dist/app-bundle/` regenerates; `SPEC.md` inside it moves with the source.
  **`source_dirty` is now False**, which is the first honest reading that field has carried in
  four bundle commits.
- `registry_version` unchanged: no type, no vocabulary value and no routing outcome moves.

### What is still NOT done, and it is the one that matters

**The export → `content.json` step does not exist and this repo does not specify it.** A live
Shopify/flunnel export carries empty `sections`, none of the eight required
`product.attributes`, and an `lpTypeId` the schema has no field for. Until that step is
written, an app cannot be fed by the owner's own system — which is the difference between a
library that validates and a library that ships.

---

## ADR-080 · 2026-09-11 · The bundle never deleted anything, so a retired type stayed in it forever

**Found by leaking a test fixture into a commit**, which is a poor way to find it and the
only way it had been found in 34 builds. The provenance is recorded because it is the honest
one: the bug was not reasoned to, it was tripped over.

### What happened

ADR-079's known-bad-input probe for the `source_dirty` fix created
`registry/types/zz-probe-type.md`, rebuilt the bundle, then removed the source. The next
bundle commit carried `dist/app-bundle/types/zz-probe-type.md` — **a type file with no source,
committed into the generated directory.**

### What it revealed, which is the actual defect

`build()` imported `shutil` and only ever called `copyfile`. There was **no step that removed
a destination file whose source had gone.** So:

- a type DELETED from `registry/types/` stayed in `dist/app-bundle/types/` permanently
- a type RENAMED left its old name behind beside its new one
- **the manifest did not list the orphan**, because the manifest is built from the sources —
  so the file was in the directory and absent from the index of the directory

**An app that enumerates `types/` rather than reading `MANIFEST.json` would load a type this
library had retired.** That is precisely the failure the bundle's own header says it exists to
prevent: *"a copy shaped by hand is how a rule and its documentation drift, and the drift is
invisible because nothing compares the two."* An unlisted orphan is invisible drift, and the
hash manifest cannot catch it — a hash check compares files it knows about.

**It was not hypothetical for this repo.** Promotion out of `registry/pdp-dr-types/` is a
`git mv` into `registry/types/` (SPEC §3.8), and renames are how this library has moved types
before — `03-spec-ingredient` to `03-spec-stilllife`, `03-spec-range` to `03-spec-lineup`,
`02-symptom-halo` to `02-symptom-callout`. Every one of those, had it happened to an ACTIVE
type after the bundle existed, would have left a ghost.

### The fix

`prune(out_dir, manifest)` walks the output directory and deletes anything not in
`manifest["files"]` plus `MANIFEST.json` itself. It runs before the manifest is written, and
every removal is printed:

```
PRUNED types/zz-probe-type.md — no source; it had been orphaned in the bundle
```

**Silent pruning would have been the wrong fix.** A generated directory that quietly deletes
files is as hard to reason about as one that quietly keeps them; the line makes a removal a
thing a reader sees in the build output and in the commit diff.

**Fed known-bad input before being believed.** A fresh orphan, `types/zz-orphan.md`, was
written into the bundle by hand and the next build reported `PRUNED` and removed it. The
directory now holds 35 files against a manifest of 34 — exactly the manifest plus
`MANIFEST.json` — which is the invariant that was never checked and now holds.

### Consequences

- `scripts/build-app-bundle.py` — `prune()` added, called from `build()` when writing, with
  every removal reported on stdout.
- `dist/app-bundle/types/zz-probe-type.md` — **deleted**, having been committed one commit
  earlier. It is left in history rather than amended away: the log is append-only in spirit
  and a reader tracing this ADR should be able to see the leak that produced it.
- No source file, no rule and no type moves. `registry_version` unchanged.

**What this does not fix.** `--check` compares the manifest against the sources; it does not
yet fail on an orphan in the output directory. The invariant is now enforced at build time
and unenforced at check time, which is the weaker half. Recorded rather than built, because
the build is the only path that writes the directory and a second gate has not earned itself.

## ADR-081 · 2026-09-11 · The export → `content.json` step exists, and the structure was never missing — it was looked for under three names it does not use

**Owner question, 2026-09-11**, on the last open item of ADR-079's dev-readiness audit. Three
decisions were put and three were answered:

| question | answer |
|---|---|
| where do the eight `product.attributes` come from | **the app supplies them** — *"đã có phương án xử lí phần này từ app, đảm bảo tin cậy"* |
| does `lpTypeId` enter the schema | **yes, as a flat optional `page.lpTypeId`** |
| how is `page.sections` reconstructed | **from `htmlCompiled`; `role` read from the copy** |

Measured against the two exports that exist on disk: `pdp-dr-360-surround-view-4-channel-dash-cam-v01.json`
(400,050 bytes, `lpTypeId: pdp_dr`) and `listicle-mini-steam-iron-v01.json` (314,239 bytes,
`listicle`). **Two exports is what exists, not a sample of the format**, and the converter
refuses an unknown `schemaVersion` rather than extrapolating from them.

### Two of the three findings this was built on were in the wrong place

ADR-079 and `README.md` were right that a real export satisfies none of the QUERY input
contract. They were wrong about where the problem sits, and a converter written to that
description fails on its first call.

**There is no `page.sections`.** The empty `sections` array is at the export's TOP level;
`'sections' in page` is `False` in both files. Code reading `page["sections"]` raises
`KeyError` — it never reaches the empty list it was told to handle.

**`htmlCompiled` is not unmarked.** It carries no `data-fl-key`, no `data-slot` and no
mustache; all three true, all three names it does not use. What it carries:

| | pdp_dr | listicle |
|---|---|---|
| `data-field` occurrences / distinct | 141 / 139 | 245 / 245 |
| `<section data-block-key=…>` | 14 | 15 |
| `page.content` non-meta keys | 138 | 245 |
| **content keys carrying no marker** | **0** | **0** |
| `data-field-type="image"` | 24 | 28 |

Every bound element also carries `data-field-type`, `data-field-attr`, `data-visible` and
`data-locked`. The page structure was never lost. **The lesson is narrower than "check your
work": a negative finding about markup is only as good as the list of names searched**, and
three names were searched where one more would have closed the whole question a day earlier.

Only the third finding survives intact — `lpTypeId` had no home, and now has one.

### The line the converter draws, and why it is drawn there

MECHANICAL, taken from the export: the section list and its ORDER from `data-block-key` in DOM
order; each section's image slots from `data-field-type="image"`, whose `data-field` IS the
slot id; each ratio from the rendered box the markup states in preference to the asset's own
`width`/`height`, snapped to ADR-016's five and reported; `product.name`, `personas`,
`raw_features` and `specification` from `brief`.

JUDGEMENT, refused rather than guessed — each for a measured reason:

- **`role`.** In `advertorial-cord-tensioner-cam-lock-v01`, **seven** sibling cards of ONE
  repeating block (`content.items.0` … `.6`) carry **six different roles**. A block → role
  table collapses all seven into one and destroys the page arc `mapping/slot-rules.md`
  cross-rule 3 enforces. The worksheet carries each section's own copy so the assignment is
  made by reading it, which is SPEC §7.5's own position on awareness stage.
- **`page.channel`.** The export does not carry it, and the router learned it by GUESSING from
  `lpTypeId` for five sessions running — half of why ADR-059 removed channel as an admission
  test. Repeating that guess inside the converter would have re-opened a closed decision one
  layer down, where nobody would look for it.
- **The eight attributes.** The owner's answer, and `query/runbook.md` Step 1 already demanded
  it: *"Do not infer missing attributes — ask; inference here is the G7-X failure path."* The
  measurement that shows why: in the dash-cam export the only colour words anywhere in the
  brief and page copy are *black*, *white* and *green*, and **all three sit inside one
  sentence** the brief itself labels *"buyer doubts to answer, **not facts about this
  product**"* — a side channel showing a green screen, everything recording in black and
  white. A keyword derivation harvests three colorways from a sentence that disclaims being
  about the product, and `colorways`'s own contract calls a fabricated one a G2 violation.

### The section walk independently reproduces ADR-050, 30 of 30

`query/runbook.md` derives a section from the slot id arithmetically — top-level prefix, plus
the next segment when it is a number. That rule was worked out by hand from routed pages.
Applied to every in-scope slot in both exports and compared against `data-block-key`, the two
**agree 30 of 30, with no disagreement.** The export's own markup and the rule this repo
derived independently say the same thing, so the converter does not restate ADR-050 — the
markup already encodes it. A cheap check that could have contradicted the design and did not.

### `page.lpTypeId` is provenance, and the distinction is the whole of it

The converter MUST read `lpTypeId`: the two exports share no argued block key at all —
`hero trust why press product tank …` against `disclosure header content.0 … compare
scarcity closing …` — so whatever maps a block to a page structure is per-`lpTypeId`. The
router must NOT. ADR-059 forbids it as an admission test and says nothing against recording
it; this is the treatment `channels` already has, kept as a record of where something came
from and read by nothing that admits or refuses. The field's own description says so at
length, because the next reader to find it will be looking for permission to gate on it.

**A latent trap was found and stepped around rather than sprung.** The first draft carried a
`$comment` key beside the description. `scripts/validate.py`'s `schema_errors` errors on a
schema keyword it does not implement — and it did not fire, because it only recurses into a
sub-schema for keys PRESENT IN THE DOCUMENT, and no `content.json` carried `lpTypeId` yet. The
unknown keyword would have detonated on the converter's first real output. `$comment` was
dropped and the note folded into the description. **The blind spot itself is left standing and
recorded here:** any annotation added to a sub-schema for an optional field is unchecked until
some document uses that field. Fixing it is a change to the validator and belongs to whoever
opens it next.

### Enforcement fed known-bad input before being believed

**Nineteen injected faults, nineteen fired, two clean controls**, tree restored afterwards.
Export-level: wrong `kind`; `schemaVersion` ≠ 1; no `page`; empty `htmlCompiled`; a file that
is not JSON. Scaffold: a `page.content` key with no marker; an in-scope image outside every
`<section>` — which is REAL, not injected, `rail.image` in the listicle export; an image with
no derivable ratio. Build: `channel` unanswered; no `product`; `attributes` left as the
placeholder string; `attributes` missing 2 of the 8; a section with image slots and no role;
two sections sharing an id; a slot with no ratio; no section surviving; an empty
`problems_solved`; a role outside the contract's twelve.

**One warns rather than refuses, and it is the gap the contract cannot close.**
`visible_output` is the only one of the eight typed as an open `string`, and **4 of the repo's
15 `content.json` files carry 49–140 characters of prose in it.** `mapping/slot-rules.md`
gates on `visible_output ≠ none` — which prose satisfies — so G8 binds and the output becomes
the primary subject by accident, in four pages already routed. Failing on it here would reject
files the contract accepts, so it warns. Making it an enum is a separate decision that breaks
those four.

`schema_errors` is IMPORTED from `scripts/validate.py` rather than reimplemented: two
validators drift, and the one in the validator is the one CI runs.

### Consequences — rule 6c sweeps on `"lpTypeId"` (4 TEACHES), `"content.json"` (19) and `"export"` (9)

- `mapping/content.schema.json` — **`page.lpTypeId` added**, optional, provenance. This is a
  contract change, and the only one here: every `content.json` written before it stays valid.
- `mapping/export-to-content.md` — **new**, 159 lines. The step's law.
- `scripts/export-to-content.py` — **new**, 558 lines. `scaffold` then `build`.
- `README.md` — *"Before you write the converter"* becomes *"Feeding it from a real page"*,
  and the known-gaps list loses the converter and gains the `visible_output` gap in its place.
- `SPEC.md` §9 — the repo map gains both new files, **and says the converter is NOT a sixth
  operation**: it produces QUERY's input rather than consuming the library's rules, so no
  harness implements it. Named explicitly because ADR-079 had just finished establishing that
  there are five, and a reader meeting a new entry point deserves to be told which side of
  that line it sits on. §1's five-operation table is untouched.
- `query/runbook.md` Step 1 — gains a pointer to where a `content.json` comes from when the
  page is a live one. Its own *"do not infer missing attributes"* rule is now enforced one step
  earlier, and the paragraph says so.
- `SPEC.md:386` and `mapping/slot-rules.md:20` — both teach that the router guessed the channel
  from `lpTypeId`, which is ADR-059's reasoning. **Both stand**: recording the value is not
  gating on it, and nothing in this diff lets a router read it.
- `query/runbook.md:407`, `registry/gif-instruction.md:79`, `registry/rules.md:359` — all three
  teach that the page id identifies the source export and lives in `prompts.json.page_id`.
  **All three stand**, and the owner's choice of a flat `lpTypeId` over a richer `page.source`
  block is what keeps them true: no second home for a page id was created.
- `query/runbook.md:37` — *"`product.reference_photos` may be an empty array, and that is a
  statement"*. **Stands, and is now produced mechanically**: the converter emits `[]`.
- The remaining `content.json` TEACHES hits are the A15 substantiation rule
  (`registry/argument-faults.md`, `registry/pdp-dr-instruction.md`, `03-spec-claimstack`,
  `03-spec-dimension`, `04-proof-stat`), `mapping/toplist-rules.md`'s one-product note, and
  `query/output.schema.json`'s two ratio descriptions. **All stand**: each is about what a
  `content.json` must CARRY, and an optional provenance field changes none of them.
- `scripts/adr-sweep.py` — **three paths added to `TEACHES`**, and this is the **fifth** time
  these tuples have been caught not knowing about a file. The worst of the five: **`README.md`
  was created by ADR-079 one day earlier and not added**, so the repo's own front door — the
  file a new consumer is told to open first — was invisible to the instrument whose whole job
  is finding files that teach the opposite of a new decision. Also added:
  `query/product-slugs.yaml`, which carries the rule for when to extend its own map, and
  `eval/golden/`, which SPEC §1 invariant 6 calls *"the conformance contract between any two
  harnesses"* — a fixture states the right answer rather than recording a past one. Proven live
  afterwards by planting a term in `README.md` and watching it classify as TEACHES.
- GENERATED — `registry/index.yaml` and `dist/app-bundle/` regenerate; the bundle carries
  `content.schema.json` and `SPEC.md`, so both move with their sources. **The converter and its
  spec are deliberately NOT bundled**: the bundle is the app's view of QUERY, and this step
  runs before QUERY begins.
- `registry_version` unchanged: no type, no vocabulary value and no routing outcome moves.

### What is NOT done

**No page has been routed through it.** The converter was exercised on both exports and its
output validated against the contract, but turning that into a `query/sessions/` entry is a
QUERY operation and needs the app's eight attributes and the owner's channel — neither of
which is a converter problem.

**`visible_output` stays an open string.** Four existing files depend on that.

**The eight attributes have no schema-level check beyond the contract's own.** The app
guarantees them; the converter checks presence, the contract checks the seven enums, and
nothing checks that the values describe the product. That is the same trust boundary
`query/runbook.md` Step 1 has always drawn.

---

## ADR-082 · 2026-09-11 · `ratios` leaves every type file, and the bundle starts shipping the two things a dev was told to use and never given

**Owner instruction, 2026-09-11: *"sửa chỗ ratio, xoá ratio. dev chạy."*** Two decisions in
one line, both taken against a readiness audit run the same day. Fix the ratio problem by
DELETING the ratio; and the dev — not the owner — runs the export → `content.json` converter.

### 1. A required field that nothing read, wrong in a third of the files

Measured before the change:

| registry | files with `ratios` | ratio values | files carrying an illegal value |
|---|---|---|---|
| `registry/types/` | 17 | 36 | 5 |
| `registry/types/_staging/` | 2 | 6 | 2 |
| `registry/pdp-dr-types/` | 15 | 33 | 3 |
| **total** | **34** | **75** | **10 files, 12 values** |

**Nothing read it to route.** SPEC §1 invariant 2 says routing reads `registry/index.yaml` plus
`mapping/slot-rules.md`; neither consults a type's ratios, and `query/output.schema.json` says
the delivered aspect *"is always the SLOT's declared ratio from content.json"*. The field was a
second source of truth for a value the page already carries, and a second source of truth is a
thing that drifts.

**And half the drift was unmonitored.** `check_ratios` warned on `registry/types/` only, so the
five illegal declarations there had been reported for weeks under the message *"correct it when
this file is next opened"* — while the other five, in `_staging/` and `pdp-dr-types/`, were
never looked at by anything. `05-social-card` carried `3:2` AND `4:5`, two ratios ADR-016 has
banned system-wide since 2026-08-13, and no run of the validator ever said so.

**A warning that defers to the next person to open the file only works if somebody opens the
file.** Nobody did, for five files, for a month.

### The precedent was already set twice, and this completes it rather than inventing it

`registry/gif-types/` (6 files) and `registry/toplist-types/` (7 files) already carry no
`ratios` key. `registry/toplist-instruction.md` states the reasoning in its own words: *"The
owner's app resolves the lede ratio (2026-09-09), so a toplist type carries no `ratios` key."*
SPEC §3.7 says the same. **The argument was never specific to the lede image** — it is that the
consumer resolves the shape — and what made it newly true for image types is ADR-081, one
commit earlier: the converter now derives each slot's ratio from the page's own markup and
snaps it to ADR-016's five. The shape arrives with the slot. The type has nothing to add.

`SPEC.md` §3.7's bullet is kept and annotated rather than deleted, because it is where the
reasoning was first written down; it now records that the peculiarity ended.

**What replaces the check is stronger than the check.** `ratios` is in neither `REQUIRED_KEYS`
nor `OPTIONAL_KEYS`, so re-adding it is an `unknown frontmatter key` ERROR rather than a
warning about its contents. The type-file half of `check_ratios` is gone; the
`prompts.json` half stays untouched, because a DELIVERED prompt is the deliverable and an
illegal ratio there is still an error.

### 2. The bundle was missing the conformance contract it describes

`SPEC.md` §1 invariant 6 — the invariant that DEFINES this bundle — promises: *"`eval/golden/`
is the conformance contract between any two harnesses: both must derive the same Stage 1
shortlist for every fixture slot."*

The bundle shipped **0** golden files, and `scripts/build-app-bundle.py` mentioned `golden`
**zero times**: not a reasoned omission like `toplist-types/` and `pdp-dr-types/`, which the
script argues at length, but a gap nobody had looked at. A dev vendoring the bundle got the
description of the contract without the contract, and could not check that their router agreed
with this library's. Four files now ship as group `conformance`.

**And the converter ships, because the dev runs it.** The owner's *"dev chạy"* settles what
ADR-081 left open. If the app ingests exports itself, then `mapping/export-to-content.md` and
`scripts/export-to-content.py` have to travel with the bundle — otherwise the dev is asked to
reimplement a step from a file they were never sent. They ship as group `input`, and the `.py`
goes beside the `.md` deliberately: it is the executable statement of the same rules and the
reference a reimplementation is checked against. ADR-081 reasoned the converter out of the
bundle on the grounds that it runs before QUERY begins; that reasoning was sound and the
premise was wrong — it assumed the owner would run it.

Bundle: **34 → 40 files**, `conformance: 4 · contract: 5 · fill: 20 · gif: 7 · input: 2 ·
route: 2`.

**`DIRS` learned to walk.** `eval/golden/` nests one directory per fixture and holds two
extensions, and the loop was flat with a mandatory suffix — `fn.endswith(None)` would have
raised. An `ext` of `None` now means *every file, at any depth*. **Walked rather than listed by
name on purpose**: a `fixture-003` added later must ship without anyone remembering to edit the
build script, which is ADR-080's failure in the other direction — that one kept a file whose
source had gone, this one would have missed a file whose source had arrived.

### Enforcement fed known-bad input before being believed

**Six cases, six as specified**, tree restored, both gates clean at 40 files afterwards:
a clean control; re-adding `ratios` to a type file (caught as `unknown frontmatter key`, an
ERROR where it used to be a warning); the tree restored to 0 errors; a new fixture
`fixture-zz-probe` shipping with no edit to the build script; that fixture's removal being
PRUNED out of the bundle from a NESTED path; and both gates clean at the end.

Warnings **31 → 26**: the five `4:5` type-file warnings are gone because the declarations are.

### Consequences — rule 6c sweeps on `"ratios"` (17 TEACHES), `"eval/golden"` (8) and `"conformance"` (1)

- **34 type files** — the `ratios:` frontmatter line removed. 17 in `registry/types/`, 2 in
  `registry/types/_staging/`, 15 in `registry/pdp-dr-types/`. No other line moves in any of
  them.
- `scripts/validate.py` — `ratios` out of `REQUIRED_KEYS`; the W:H format loop deleted with a
  note saying why no check replaces it; the index generator stops emitting the field;
  `check_ratios` loses its type-file half and its docstring says what the remaining half is for.
- `scripts/build-app-bundle.py` — the `input` group, the `eval/golden` DIRS entry, and the
  recursive walk for `ext=None`.
- `SPEC.md` — the `ratios:` line leaves the §3.3 frontmatter spec, **which is also the sixth
  place that was teaching `4:5`**: the spec's own example declared a banned ratio. §3.7's
  ratio-not-declared bullet gains one sentence saying the peculiarity ended.
- `registry/types/03-spec-explode.md:113` — **the one live instruction the sweep found**:
  *"`4:5` stays in `ratios` for the page's layout, not for the composition"*, body prose rather
  than CHANGELOG, teaching a reader about a field that no longer exists. Rewritten to say the
  shape arrives from the slot. Its line 341 is a CHANGELOG entry and **stands**.
- `registry/types/01-pain-split.md:293`, `03-mechanism-xray.md:250`, `03-use-grid.md:179`,
  `04-proof-lockedframe.md:353` and `:362` — all CHANGELOG entries recording past corrections
  to the field. **All stand**: history is what the CHANGELOG is for, and a correction that was
  right on the day stays legible.
- `registry/types/02-cause-anatomy.md:222`, `04-proof-lockedframe.md:69`,
  `registry/rules.md:792`, and the two `ready-to-push/` hits — **all stand**: every one uses
  "ratios" to mean image proportions or measured size relations, not the frontmatter key.
- `registry/toplist-instruction.md:383` — **stands, and is still true.** A toplist type does
  carry no `ratios` key. It no longer marks a distinction, which costs a reader nothing, and
  that file belongs to another lane's write territory.
- `README.md:61` and `query/runbook.md:32` — both describe the converter deriving slot ratios.
  **Both stand and are now the only place a ratio is discussed as an input.**
- `ingestion/runbooks/curate.md:46` — tells a curator to check routing against `eval/golden/`
  fixtures. **Stands**, and is the reason those fixtures had to reach a second harness.
- GENERATED — `registry/index.yaml` regenerates **without the `ratios` line on all 17 types**;
  `dist/app-bundle/` regenerates at 40 files.
- `registry_version` unchanged. This removes a RUNTIME PARAMETER, which SPEC §3.2 step 1 calls
  the cheapest level of absorption and §3.3 already called *"never identity"*. No type's
  argument, no vocabulary value and no routing outcome moves — the same shortlist comes back
  for every fixture slot, which the golden fixtures assert on every run.

### What is NOT done

**No fixture was added.** Two is what `eval/golden/` holds, 14 slots between them, and a
conformance contract that thin is a thing the next dev will find out about. Shipping the two
that exist beats shipping none; it does not make two enough.

**`05-social-card`'s illegal ratios were deleted, not adjudicated.** `3:2` and `4:5` were in
that file for a reason nobody wrote down, and removing the field removes the question rather
than answering it. If that type ever needs a shape the page cannot give it, the argument has to
be made in `SLOT CONSTRAINTS` as prose, where a reader can weigh it.

---

## ADR-083 · 2026-09-11 · LP1 gets a name, and the converter's section rule was right twice by luck

**Owner statement, 2026-09-11: *"lp1 là listicle và advertorial (trong corpus), lp2 là product
page direct response, top list là 1 loại khác."*** A taxonomy note. Checking whether the repo
already held it turned up a gap, and checking the gap turned up three false claims in ADR-081,
written four commits earlier in this same session.

### 1. The taxonomy, and the gap it closed

`LP2` appeared in **six** places across `SPEC.md`, `CLAUDE.md`, `vocabulary.yaml`,
`validate.py` and two runbooks. **`LP1` appeared nowhere** — no file said which corpus
`registry/types/` was measured on, and the top-N listicle had never been placed in the scheme
at all. `SPEC.md` §3.0 now carries the table.

| page kind | `lpTypeId` | registry |
|---|---|---|
| **LP1** | `listicle`, `advertorial` | `registry/types/` |
| **LP2** | `pdp_dr` | `registry/pdp-dr-types/` + `registry/types/` |
| **top-N listicle** | — | `registry/toplist-types/`, not LP-numbered |

Three consequences are written beside it. **`lpTypeId` is not 1:1 with a page kind** — LP1 has
two — so anything keyed on `lpTypeId` is keyed finer than the kind. **A registry's corpus is
not its routing scope**: `registry/types/` was measured on LP1 and is used by every kind
(ADR-059, and ADR-077 answer 1), so a clause citing renders cites LP1's renders unless it says
otherwise — which is exactly what ADR-073 proved matters. And the grouping is **measured**
rather than accepted: over the 57 exports, listicle∩advertorial = 15 blocks, Jaccard **0.33**,
against **0.14** and **0.17** for either against `pdp_dr`. What the two LP1 members share
includes argued blocks (`content.items.0`…`.5`); what all three share is only furniture. **One
kind by family resemblance, not by a common template.**

### 2. There are 57 exports on disk, not 2

ADR-081 said *"two exports is what exists on disk"* and `mapping/export-to-content.md` repeated
it. Both were wrong: `~/Downloads` holds **57** flunnel page exports — 33 `advertorial`, 23
`listicle`, 1 `pdp_dr`. The session had looked for the two files its own handover block named
and stopped, and then wrote the negative claim as if it had searched. **A count is a
measurement and has to be taken like one.**

All 57 now scaffold with zero failures, placing **847 in-scope slots** out of 1,392 image
fields.

### 3. The section rule agreed 30 of 30 because the sample was two

ADR-081's convergence check — *"the `data-block-key` section walk independently reproduces
ADR-050, 30 of 30, no disagreement"* — was reported as a cheap check that could have
contradicted the design and did not. **Across all 57 exports the two rules agree on 27 and
disagree on 30**, 313 slots out of 934.

Where they differ the markup is coarser, and the case is the commonest template in the corpus:
the advertorial wraps seven argument cards, a product shot, a closing card and four review
photos in ONE `<section data-block-key="features">`. ADR-050's arithmetic splits that into
`content`, `product`, `product_end` and `reviews`.

**ADR-050 is right and the markup is wrong for this purpose**, and the runbook says why in its
own words: the rule that read the prefix alone *"merged every editorial block a template
numbers under one name"*. A `<section>` is a styling container; ADR-050 was derived from routed
pages to recover the argument structure a template packages away. Reading the container as the
structure hands `mapping/slot-rules.md` cross-rule 2 a thirteen-slot "repeating section" whose
members are not equivalent entries, and gives cross-rule 3's page arc one beat where the page
has four.

So the converter now sections by `section_of()` — ADR-050, verbatim — ordered by first
appearance in the document. `data-block-key` is kept in the worksheet as `_block_keys`,
provenance a reader sees and nothing routes on.

**Two things fell out of the fix.** An image outside every `<section>` is now placed like any
other, because the section comes from the slot id — the "unplaced" warning is gone, and with it
26 real instances across the corpus (`rail.image` ×17, `hero.image` ×9). And the worksheet now
says what ADR-050 cannot: **a reader may SPLIT a section further and often should.** ADR-050 is
the coarsest grouping the cross-slot rules allow, not the finest that is right —
`advertorial-cord-tensioner-cam-lock-v01` split `content.items.0`…`.6` into seven sections
carrying six roles. Merging two is never right.

### 4. Two more claims that did not survive the corpus

**`aspect-video` is a ratio and the converter did not know it.** ADR-081 said every in-scope
slot resolves. Across 57 exports, 12 did not — and 8 of those were `hero.image`, the most
important slot on a page, wearing Tailwind's `aspect-video` (16/9). Handled now, along with
`aspect-auto`, which is NOT a ratio and must not be read as one. **845 of 847 resolve**; the
two that do not carry `w-full rounded-md object-cover` and nothing else, and are named rather
than invented.

**`closing.bio_image` is an author portrait.** `mapping/slot-rules.md`'s `author` row is empty
by decision and its rationale names the exact thing — *"a byline avatar, an About-the-author
image, a comment thread of faces"*. Verified from the page rather than from the field name:
`closing.bio_image` sits beside `closing.bio_title` *"About the specialist"* and a signed
`closing.signature`. Out of scope, 4 instances.

### The pattern, since this is the second time in one session

ADR-081 found ADR-079's negative finding about markup wrong because it had searched three
attribute names and reported the absence as a fact about the file. This ADR finds ADR-081's
claims wrong because it measured two files and reported the agreement as a fact about the
format. **Both are the same error at different scales: a search that stopped at the first
answer, written up as a property of the thing searched.** The instrument that caught it both
times was widening the input, not re-reading the conclusion.

### Consequences — rule 6c sweeps on `"LP2"` (32 hits, 13 files, 8 TEACHES), `"data-block-key"` (32, 13, 2) and `"section"` (2337, 148, 50)

- `SPEC.md` — **§3.0 added**, the page-kind table plus the three consequences. This is a
  documentation change, not a contract change: no operation, invariant or field moves.
- `scripts/export-to-content.py` — `section_of()` added and used for grouping; `aspect-video`
  understood, `aspect-auto` explicitly not; `bio_image` out of scope; the "unplaced" warning
  replaced by one that names slots with no derivable ratio; the worksheet README gains the
  split note; the module docstring corrected where it said sections come from `data-block-key`.
- `mapping/export-to-content.md` — head, sectioning, ratio and scope sections rewritten to the
  57-export measurement; the false convergence claim replaced by what the corpus says; the
  `lpTypeId` section now carries the Jaccard figures and points at §3.0.
- `README.md` — the converter paragraph said sections "come out of `page.htmlCompiled`,
  which carries a `<section data-block-key=…>` per block". **The `data-block-key` sweep caught
  it**, one commit after that sentence was written, teaching the rule this ADR supersedes.
  Rewritten, and the "two exports measured" count with it.
- `scripts/adr-sweep.py` — `registry/gif-cards-vi.md` into `TEACHES`, found UNCLASSIFIED by the
  `"section"` sweep. It is the SOURCE the Vietnamese folder cards are generated from
  (`CLAUDE.md` rule 5's one named exception) and it states its own format rules. **Sixth file
  these tuples did not know about**, and the second found in this session.
- `decisions/log.md` — ADR-081's three claims stand as written, and are corrected HERE rather
  than edited there. The log is append-only in spirit; a reader tracing the converter should be
  able to see what was believed on the way.
- `query/runbook.md`'s ADR-050 block — **stands, and is now load-bearing in a second place.**
  It was written for the gif loop-spacing rule; it is now also what a converter sections by.
- `mapping/slot-rules.md` cross-rules 2, 3 and 6 — **all stand.** Nothing about them changes;
  what changes is that the converter now feeds them the grouping they were written against.
- `registry/vocabulary.yaml`'s pdp-dr comment and `CLAUDE.md`'s two LP2 rows — **stand.** They
  use LP2 correctly and §3.0 now defines the term they were leaning on.
- GENERATED — `dist/app-bundle/` regenerates; `SPEC.md`, `export-to-content.md` and
  `export-to-content.py` are all bundled, so all three move with their sources. The bundle's
  own check caught them stale, which is the `input` and `contract` groups doing their job one
  commit after being added.
- `registry_version` unchanged: no type, no vocabulary value, no routing outcome.

### What is NOT done

**No content.json in `query/sessions/` was regenerated.** The fifteen that exist were routed by
hand against the old grouping where a converter was involved at all; none is known to be wrong,
and none has been re-derived. A page re-routed from today gets the ADR-050 grouping.

**The 57 exports were scaffolded, not built.** `build` needs a channel, eight attributes and a
role per section — none of which is a converter problem — so what is proven is that the
mechanical half holds across the corpus, not that 57 valid `content.json` files exist.

**`hero.image` on two seat-cushion pages still has no ratio.** The markup states none. It is a
human decision and the scaffold says so.

---

## ADR-084 · 2026-09-15 · The evidence counter could not see the promotion queue, and now every source count is generated

**Owner instruction, 2026-09-15: *"hãy thực hiện theo khuyến nghị."*** The recommendation came
out of an audit of the classification mechanism the owner asked about: write the pdp-dr
evidence check the toplist namespace already had, and make the counter read `proposed_id` for
an id that has a file. Doing it turned up two more things the counter needed and one it must
not do.

### What the counter could see

`evidence_counts()` read `rec["type"]` alone and credited only ids with a file in
`registry/types/`. Three kinds of evidence fell outside it:

- **66 records filed `match` with `type: null` and a `proposed_id`** — a match to a proposal
  made earlier in the same batch. `ingestion/prompts/classify.md` does not describe this shape;
  classifiers produced it anyway, and it is semantically sound.
- **Founding observations.** A `new-candidate` names its proposal in `proposed_id`. When the
  proposal becomes a file, those records ARE its exemplars, and they stayed invisible.
- **The whole pdp-dr namespace.** `check_toplist_evidence` exists because a record naming a
  toplist id counted toward nothing. The identical gap stood for pdp-dr and it was larger —
  123 ledger references named a pdp-dr id and no function read one — while every file in that
  folder states its criterion-1 source count in prose.

### Calibrated against the hand counts before a line was written

`registry/pdp-dr-types/_CURATION-2026-09-11.md` holds six source counts made by hand. Rule
variants were run against them:

| rule | source counts reproduced |
|---|---|
| `type` alone, any verdict set | **0 of 6** |
| `type` + `proposed_id`, match and variant only | 0 of 6 |
| `type` + `proposed_id`, plus `new-candidate` | **6 of 6** |

Taking the last record per hash changed nothing today; stripping the old `lp3-` slug prefix
changed nothing and was not adopted. Observation counts reproduce 4 of 6 — `03-spec-dimension`
measures 10 against 11 and `03-spec-hero` 19 against 18, off by one in opposite directions,
and nothing in the ledger says which side is wrong. Criterion 1 reads sources, which agree.

**One refinement the calibration could not show and the template makes mandatory:** on a
`new-candidate`, `type` is the NEAREST existing type, not a match. So `type` counts only on
`match` and `variant-candidate`, and `new-candidate` counts only through `proposed_id` —
otherwise every new-candidate filed near `06-relief-hero` would inflate it.

### Two findings the generated counts surfaced at once

Running the rule over the fifteen pdp-dr files disagreed with five typed counts. Each was
chased to a cause before anything was recorded.

**Renames split the evidence, 3 of 3.** The ledger is append-only and a rename is not a
re-filing, so observations stay under the old id:

| file | new id | old id | union | the file records |
|---|---|---|---|---|
| `03-spec-stilllife` | 2 | `03-spec-ingredient` 2 | **3** | 3 |
| `03-spec-lineup` | 1 | `03-spec-range` 2 | **2** | 2 |
| `02-symptom-callout` | 1 | `02-symptom-halo` 2 | **3** | 3 |

All three explained exactly. `FORMER_IDS` in `scripts/validate.py` now carries these renames,
cited to ADR-065 and ADR-066, and **reports on itself** — an old id with a file again, or a new
id with no file, is an error — because a name-keyed constant goes stale silently otherwise, the
lesson this repo already paid for once when a directory rename orphaned an exemption set.
A deprecation is not a rename: `07-identity-callout`'s observations are not credited to its
`replaced_by`, because ADR-078 says retiring it did not re-file them.

**Typed numbers drifted, 2 of 2.** `07-identity-pack` had 4 distinct sources before the
157-image drop of 2026-09-11 and gained 6 in it; its undated `blocked_by` still reads *"One more
distinct source for criterion 1"*, written at 4, now at 10. `06-relief-claimstack` had 9 and
gained one (`hydrovia`); its BLOCK reads *"nine"*. **Neither file is edited here** — type files
are a diff the owner reviews — but this is exactly the failure the rule *generate numbers, never
type them* exists for, and it is now visible to anyone who runs `--evidence`.

### What was built, and what was deliberately not

- **`ledger_evidence(observations, ids)`** — the one reading every count now shares: last
  record per hash, `type` on match/variant, `proposed_id` on all three, former ids followed, and
  a source taken from the slug before `__` in a `source file:` note. A record with no such note
  counts as an observation and is reported `unsourced`, never guessed into a source.
- **`evidence_counts`** keeps its contract — distinct observations per image type, SPEC 6.2's
  number, the `evidence_count` the index has always carried.
- **`check_toplist_evidence`** reads through the same function. Counts identical to before on
  every toplist id; its old last-record logic filtered to toplist ids before picking the last
  record, which let a frame re-filed away from toplist keep counting — the comment above it
  said the opposite. Now it does what the comment said.
- **`check_pdp_dr_evidence`** — one warning, for the fault a count proves without reading
  prose: a non-deprecated file whose id and former ids resolve to no observation at all.
- **`--evidence`** prints observations, sources and unsourced records for every classified
  namespace.

**Not built: a parser for the typed counts.** The obvious check compares each file's written
number against the measured one. It would be wrong on the first run: the counts mix digits and
words (*"2 of 5"*, *"three of five"*, *"Three today"*), and `03-spec-hero`'s `blocked_by` says
*"19 sources"* about `06-relief-hero`. A checker that warns on correct text teaches people to
ignore it.

### Enforcement fed known-bad input before being believed

**Fifteen cases, fifteen as specified**, run in memory — the append-only ledger was never
touched, verified by line count. The hand counts reproduce; deleting one `FORMER_IDS` entry drops
`03-spec-stilllife` from 3 to 2; an old id with a file again errors; a new id with no file
errors; real ids stay silent; a correction record moves one hash from `03-spec-claimstack` to
`03-spec-callout` without double-counting; a `new-candidate` whose `type` is only the nearest
type credits nothing; `duplicate` and `reject` credit nothing while a real `match` credits one;
the zero-evidence guard fires on an empty pdp-dr id and stays silent on a deprecated one; toplist
counts equal the pre-change baseline; an unknown verdict still errors; and the old and new
`evidence_counts` differ on exactly five image types, every one upward.

### What moved

**328 of 468** unique hashes in the ledger now resolve to an id that has a file.
`registry/index.yaml` changes on five rows, every one a type whose founding observations sat
under `proposed_id`:

| type | before | after |
|---|---|---|
| `03-mechanism-xray` | 0 | 5 |
| `03-spec-explode` | 3 | 8 |
| `03-spec-macro` | 10 | 14 |
| `03-use-grid` | 10 | 15 |
| `05-social-snapshot` | 4 | 16 |

`03-mechanism-xray` from 0 to 5 is anchor A8's case: its founding exemplar was filed
`new-candidate` before the type existed, and the index had reported it as having no evidence
for five weeks. **Nothing routes on `evidence_count`** — SPEC §2 is the only file that teaches
it — so no routing outcome moves and `registry_version` is unchanged.

### Consequences — rule 6c sweeps on `"evidence_count"` (1 TEACHES), `"proposed_id"` (2), `"distinct source"` (22), `"FORMER_IDS"` (1) and `"unsourced"` (1)

- `scripts/validate.py` — `ledger_evidence`, `FORMER_IDS`, `check_pdp_dr_evidence`,
  `check_former_ids`, `evidence_report`; `evidence_counts` and `check_toplist_evidence` rewritten
  to read through the shared function; `--evidence` wired into `main`.
- `SPEC.md` §2 — gains the definition of `evidence_count` and names `--evidence` as where
  criterion 1's source count comes from. **This is the `evidence_count` TEACHES hit, updated.**
  The `FORMER_IDS` and `unsourced` hits are this same paragraph.
- `ingestion/anchor-set.md` — its duplicate-coverage paragraph said *"97 observations have
  produced zero `duplicate` verdicts"*; the ledger has since produced them. Rewritten to say the
  path is exercised and its anchor still owed — **without a number**, because the number is what
  went stale.
- `ingestion/prompts/classify.md:44` — `"proposed_id": "<only for new-candidate>"` **teaches
  against 66 records the counter now honours, and stands.** Correcting it is a template edit, and
  that file's own rule bumps `template_version`, after which `ingestion/runbooks/curate.md`
  discounts the 425 records made under c1.0. An owner decision, not a sweep fix.
- `ingestion/prompts/classify-toplist.md:13` — `new-candidate` with a `proposed_id` for a toplist
  frame. **Stands**; consistent with the rule.
- The 22 `"distinct source"` TEACHES hits — SPEC §6.3's criterion, `mapping/pdp-dr-rules.md:31`
  ranking by source count, `registry/pdp-dr-instruction.md:296`'s 8/7/6, and a dated
  *"Promotion status (date): N distinct sources"* line in every pdp-dr file. **All stand.** The
  dated lines were true on their dates; the instruction's 8/7/6 is now reproduced by script. The
  two that are not dated and are no longer true — `07-identity-pack`'s `blocked_by` and
  `06-relief-claimstack`'s *"nine"* — are recorded above and left for the owner's review.
- GENERATED — `registry/index.yaml` on five `evidence_count` rows; `dist/app-bundle/` carries
  that index and SPEC.md.

### What is NOT done

**No typed count in a type file was corrected.** Two are stale and the owner reviews type files.

**The records with no source note stay unsourced.** Every toplist record and the earliest
batches of 2026-08-10 and -11 carry no page slug, so their source counts read 0. That is an
absence of data, stated as one — not a finding that those types have no sources.

**The ±1 on `03-spec-dimension` and `03-spec-hero` observations is unexplained.** The two share
five source pages and no hash moved between them.

**The `duplicate` anchor is still owed**, and so is an owner decision on documenting the
`match`-plus-`proposed_id` shape in the classification template.

---

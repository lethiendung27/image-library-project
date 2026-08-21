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

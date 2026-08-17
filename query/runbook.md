# Query runbook — content.json → prompt options

Harness-neutral procedure for the QUERY operation (SPEC §7). Output must validate
against `query/output.schema.json`.

## Context budget

Load into context: `registry/index.yaml` + `mapping/slot-rules.md` + the input
`content.json`. Do NOT load type files yet. After Step 3, load ONLY the selected
type files (typically 2–4) plus `adapters/<model>.md`. The full library never enters
context.

## Step 1 — Validate input

Check `content.json` against `mapping/content.schema.json`. Reject with a precise
message on: missing `product.attributes` fields, fabricated-looking colorways, roles
outside the vocabulary, missing `image_slots`. Do not infer missing attributes —
ask; inference here is the G7-X failure path.

## Step 2 — Stage 1 shortlist (mechanical)

For each `image_slot`, read the `role × page.channel` cell of the slot-rules table.
That cell is the candidate list. Empty cell → the slot gets no library options;
report it as out-of-scope rather than forcing a type.

## Step 3 — Stage 2 portfolio (one judgment pass over the WHOLE page)

With the index + shortlist + `product.attributes` + ALL sections visible at once:

1. Apply every attribute gate from `mapping/slot-rules.md` (deterministic kills).
2. Apply each candidate's `avoid_when` from the index against the section's
   `copy_summary` and the product.
3. Enforce cross-slot rules: `never_with`, `requires_pair`, `avoid_adjacent`,
   one-type-once, pain-before-relief arc, step-3 budget.
4. Select the page as a SET — never slot-by-slot greedily. If two slots compete for
   one type, the type goes where its `use_when` fits best and the other slot takes
   its next candidate.
5. Tie-breaker (G6 decision): consult `picks` in the index for the (type × role)
   cell ONLY if that cell's `shown` ≥ 20. Soft prior only — it never overrides an
   `avoid_when` or a cross-slot rule.

## Step 4 — Build 3 options per slot (G5 decision)

Each option differs from A on a NAMED dimension, recorded in `varies_on`:

- **A — baseline**: the best-fit type/variant/axes.
- **B — varies on `type`** (a different shortlisted type) OR on an **`axis`**
  (e.g. `register: ugc`) when no second type survives the gates.
- **C — varies on `execution`**: same type+axes as A, different persona /
  environment / camera execution of the skeleton.

Rules: an option that requires a pair or has channel restrictions carries that in
`composition_notes`. Options must all be legal — never present a gated-out type as
an option. Fewer than 3 legal possibilities → emit fewer, never pad with rerolls.
**C is always available** — it is a different execution of A, so a slot falls below
three only when its own law forbids one.

**Name one of them.** Every slot with options sets `recommended_opt` and explains it
in `recommendation_basis`, against these five criteria in this order:

1. **FIT** — does the type's own `use_when` name this beat, in the copy's own words.
2. **PAGE LEGALITY** — does it keep the whole recommended SET legal under
   `one-type-once`, `never_with`, `requires_pair` and the page arc.
3. **EVIDENCE** — how many renders stand behind the variant, the style and every
   mark it uses, counted from the type file and `eval/render-tests.jsonl`.
4. **PRODUCT PRESENCE** — is the product in frame where this section's argument
   needs it.
5. **PROMPT RISK** — characters against that type's own ceiling, and how many
   clauses in it have never been rendered.

Where two criteria disagree the basis says which decided and why. A recommendation
is a suggestion and nothing more: `feedback/picks.jsonl` records what the human
chose, never what was suggested, or the loop starts learning from itself. Options
are individually legal but not necessarily legal in COMBINATION — where picking one
option forces another slot to change, say so in that option's `composition_notes`.

**The table cell is exhausted → widen the derivation, never empty the slot.** An image
slot with no options is a contract violation (SPEC §7.4). Work down this ladder and
stop at the first rung that yields a legal type:

1. **The role's own cell.** The normal case.
2. **Adjacent steps.** Role affinity is a preference, not a wall: a `comparison` slot
   may take a step-3 or step-4 type; a roundup entry that indicts an object may take a
   step-1 `job: pain` type. Say which step you moved to in `varies_on`.
3. **A repeating-section repeat.** Cross-slot rule 2 permits one type to serve every
   entry of a list section, provided the instances differ on a named dimension.
4. **Another execution of a type already on the page.** Different subject class, same
   type, named in `varies_on` — this is not one-type-once evasion, it is the honesty
   the rule asks for.

The only test that never bends is the type's own admission: `channels` must contain
the slot's channel and `avoid_when` must not exclude the case. A type that fails
either is not a candidate at any rung — that is refusing a *wrong* type, which stays
correct. Every option emitted is a real active type carrying its own laws; there is no
fallback tier, and no image ships unrouted.

Worked precedent: a listicle's five ranked entries, each indicting one alternative, had
no comparison type left after one-type-once spent `04-proof-lockedframe`. Rung 2 plus
rung 3 resolved it to `01-pain-scene` in its object-only execution — an execution the
ledger already records twice (obs `sha256:30c9568…`, `sha256:4e8f238…`, both filed as
pain-scene with "no person as subject, only the indicted OBJECT").

## Step 5 — Fill skeletons

Load the selected type files now. For each option:

1. Copy the SKELETON; resolve every conditional branch using `product.attributes`
   (operation → POSE, visible_output → LIGHT/G8, mounting → G7-X mode, colorways →
   Zone B units). No branch may remain unresolved in the output prompt.
2. Fill slots within SLOT CONSTRAINTS; the product slot carries only G2's four
   kinds of information.
3. Imitate the type's WORKED EXAMPLES for diction and structure (they are few-shot,
   and they passed or encode known failure modes — read their annotations).
4. Compose NEGATIVE = `[G6 expansion] + type NEGATIVE + variant additions`.
5. Set `attachments` to `product.reference_photos` whenever the type has
   `requires_product_photo: true` (and note the `--rivals` exception).

## Step 6 — Render through the adapter

Apply `adapters/nano-banana.md` (or the target model's adapter): negative
translation, reference-image phrasing, ratio parameter, and — for
`generation_mode: multi-pass` — expand `steps[]` with the adapter's edit-script
template. The canonical prompt stays model-agnostic in the type file; only the
rendered output is model-specific.

## Step 5b — COVERAGE PASS (product-driven, runs after the sections are routed)

The section pass answers "what does the page ask for". This pass answers a different
question: **what does this product have to prove that nothing on the page proves yet.**
Its output is `recommended[]` — additive proposals, never replacements, kept out of
`slots[]` so the page's real section count stays honest.

**Awareness stage is the weight, not the page format — and you READ it, you do not ask
for it.** The content already says where the reader stands: what the hero assumes they
believe, whether the page spends words re-establishing the problem or goes straight to
comparing solutions, whether the copy names competitor classes or the product itself.
There is deliberately no `awareness_stage` field in the content contract: a declared
field is one more thing to fill, one more thing to go stale against the copy it
describes, and one more chance to constrain a judgement the copy already supports.
State the stage you read and the basis for it in `page_composition_notes`, then judge
each absent rung against where that reader stands:

- **unaware** — does not yet believe there is a problem. Recognition and amplification
  carry the page; proof of a solution they have not asked for is wasted.
- **problem-aware** — feels it, cannot name the fix. The cause and the mechanism are
  what move them.
- **solution-aware** — knows solution classes exist and is comparing them. Mechanism
  and **physical proof** are what decide it; re-amplifying the problem insults them.
- **product-aware** — knows this product, not yet convinced. Proof, social evidence and
  the after-state.
- **most-aware** — ready. Almost nothing but the after-state and the offer.

**An absent rung is NOT automatically a gap.** That is the whole reason this pass is
keyed on awareness and not on page type: a listicle for a solution-aware reader is
*right* to skip step 2, and *wrong* to skip step 4, while the same format for an
unaware reader inverts both. Do not build a lookup of format → rungs; there is none,
and hard-coding one would replace judgment with a table that is wrong half the time.

Rules for what may be proposed:

1. Same admission tests as any option — channel legality, attribute gates, `avoid_when`.
2. Same cross-slot rules — one-type-once, step-3 budget, `avoid_adjacent`, page arc.
   Coverage is not a licence to bloat; those rules exist because more explanation is
   not more persuasion.
3. Every proposal states **which rung it fills** and **where it would sit**. A proposal
   that cannot name its rung is decoration and does not ship.
4. Cap: at most one proposal per absent rung that the awareness stage says matters.

**Honest limit:** this pass makes a page *argument-complete*. It cannot make it
*conversion-optimised* — `feedback/picks.jsonl` has no records, so the ≥20-pick prior
in Step 6 never fires. Say so in `page_composition_notes` rather than implying the
recommendations are performance-backed.

## Step 5c — GIF suggestion (per slot)

Every image slot carries a `gif` verdict, including a negative one — silence is harder
to act on than a stated "no". Two forms:

- **whole-frame** — the entire image becomes a short silent loop. Available to ANY
  type, because it adds no layer to the frame. This is the default suggestion.
- **inset** — the motion replaces a layer the type's own SKELETON already legislates
  (a Zone B/C inset, a rail vignette). Only offered where that layer already exists;
  proposing a new layer is a graphic-overlay decision this runbook does not make.
  **Check for the layer before defaulting to whole-frame** — a page can go a whole
  routing without one and that is normal, since most types ban layers outright, but
  where a legislated layer DOES exist and the still is a held state, the layer is
  usually the half that should move. Say in `reason` which of the two applied.
  When the form IS `inset`, the option's own prompt must set that layer to `--loop`
  and carry G12's plate — the editor's work order has to be IN the render, not in a
  file they will not open (ADR-019). A `form: inset` verdict beside a prompt that
  draws no plate is the one inconsistency to check for. When the form is
  `whole-frame`, the plate is the whole delivered image and no photograph is made:
  emit the brief, not three photographic options for a frame that gets replaced.

A slot earns motion when its declared reason to exist is **temporal** — a transition, a
sequence, a state changing, an output flowing. A slot that exists to reveal an angle, a
place or a colorway does not, and gets `eligible: false` with that reason.

**Then say what the loop ARGUES: `gif.kind`, from the `jobs` vocabulary.** It is the job of
the LAYER the loop lives in, and that is often **not** the type's own job — an inset is not
a pain slot. `06-relief-hero --recall` holds the past, so a loop there does `pain` work
inside a type whose job is `relief`. `--context` holds the product where it lives, so its
loop does `use`. `--detail` holds one magnified feature, so its loop does `mechanism`, or
`output`-driven `mechanism` where G8 applies. `--vsinset` holds two states, so `proof`.
For `whole-frame` there is no layer and the kind is the type's own job.

Where a layer admits more than one kind, take the one **the section's copy is already
arguing**, and say which and why in `reason` — this is the same judgement as choosing a
type, made one level down. The kind sets what `SHOT`, `ACTION` and `RESULT` name; nothing
else about the plate changes with it.

Every GIF carries the same five-field brief, each line ≤ 7 words:

```
GIF SLOT · <duration> · <loop behaviour>
SHOT     <camera and framing>
ACTION   <what moves, in order>
RESULT   <what the viewer is left holding>
MATCH    <the register law it must obey>
```

`MATCH` is not filler: a loop that ignores the still's grade and light reads as pasted
in. Delivery is mp4/webm with a size ceiling — a 20 MB `.gif` costs more conversion
than the motion buys.

**The brief is what the editor reads off the plate, and `prompt` is what RENDERS that
plate.** It is never a prompt that animates a supplied still: ADR-019 settled that an
editor builds the loop, so the pipeline's job is to hand them a legible work order drawn
into a frame. Two shapes, and only these two. For `form: whole-frame` the plate IS the
delivered image — a flat card carrying the five lines and nothing else, no scene and no
product; it passed 1 of 1 and is the case that proved the model writes the brief
reliably. For `form: inset` the host type's own prompt sets its legislated layer to
`--loop` and draws the plate there, geometry inherited from that layer.

Every line must be satisfiable by the still the plate accompanies (G12) — a brief
promising something the frame does not contain sends the editor to build the wrong loop,
and that is the dominant fault at 2 of 4. The plate never ships: its render takes the
`--brief` suffix and never the slot's own asset filename.

**In `prompts.md` the gif is a fourth option below C**, carrying the same anatomy the
options carry. It is not an alternative to A–C — it is rendered alongside the recommended
still, because a card that says what moves is useless to an editor who has no frame to
move.

## Step 7 — Emit and log

Where the session lives: `query/sessions/<page_id>/` holds `content.json` (the
contract as assembled from the source export), `prompts.json` (the machine artifact,
valid against `query/output.schema.json`) and `prompts.md` (the human view). The JSON
is the single source of truth; the Markdown is **generated from it**, never
hand-edited, so the two cannot drift. Every slot in both carries an `asset` filename
and a `placement` line, so an editor never has to guess which image goes where.

1. Emit JSON per `query/output.schema.json`, including `page_composition_notes`
   (page-level warnings: pairs chosen, arcs enforced, fallbacks emitted and why).
2. After the human picks: append ONE record per slot to `feedback/picks.jsonl`:

```json
{"ts": "<ISO date>", "page_id": "<id>", "slot_id": "<slot>",
 "section_role": "<role>",
 "options_shown": [{"opt": "A", "type": "...", "variant": null, "varies_on": "baseline"}],
 "picked": "<type id of the chosen option>",
 "reason": "<the reviewer's one line>"}
```

No pick yet is a valid state — log nothing, never fabricate a record.

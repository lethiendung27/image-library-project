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

# Query runbook — content.json → prompt options

Harness-neutral procedure for the QUERY operation (SPEC §7). Output must validate
against `query/output.schema.json`.

## Context budget

Load into context: `registry/index.yaml` + `mapping/slot-rules.md` + the input
`content.json`. Do NOT load type files yet. After Step 3, load ONLY the selected
type files (typically 2–4) plus `adapters/<model>.md`. The full library never enters
context.

**And load only the SECTIONS you fill from.** A seven-reason listicle forces eight
distinct types under one-type-once, so "typically 2–4" understates the worst case and
the cost lands here. Measured across the nine type files page 73 needed: `SKELETON`,
`PARTS` and `SLOT CONSTRAINTS` are the fill surface and total about 51k characters;
`WORKED EXAMPLES` and `CHANGELOG` add 71k and are read only when a type's diction is
unfamiliar. Two are pure waste and were read anyway on that page — `NEGATIVE`, because
no avoid line has been rendered into a prompt since ADR-014 and the canonical list is
already in the type file for the `avoid` field, and `MARKS`, which is worth loading only
for a type whose prompt will actually carry a mark.

## Step 1 — Validate input

Check `content.json` against `mapping/content.schema.json`. Reject with a precise
message on: missing `product.attributes` fields, fabricated-looking colorways, roles
outside the vocabulary, missing `image_slots`. Do not infer missing attributes —
ask; inference here is the G7-X failure path.

**`scripts/validate.py` now enforces this on every run** (ADR-035), over each session's
`content.json` and each golden fixture's, so a contract that drifts from the schema is
caught in the repo rather than in a prompt. Writing the session's `content.json` is
therefore part of routing the page and not a courtesy: a session whose directory holds a
`prompts.json` and no `content.json` is an error, and SPEC §1's claim that the page can
reproduce its own prompts is false without it.

**`product.reference_photos` may be an empty array, and that is a statement.** The export
carried no product photograph, there is nothing to hash, and SPEC §6.4 forbids inventing
one. The prompts still carry their G1 reference block and stay paste-and-run — the owner
attaches the photo by hand in the generation tool, which is Step 5's rule read one level
up. Say "attach the product photo", never "cannot run".

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

**RENDER CAPABILITY, declared once here so no type has to guess it.** Several type
files gate on "where the renderer cannot composite", and until now nothing in the repo
said whether it can. It cannot. Owner instruction, 2026-08-17: **this pipeline is
paste-and-run — one prompt, one generation call, at most one reference photo attached.
No compositing, no edit chains, no post assembly.** The adapter's note that the model
supports conversational editing is about the MODEL; this is about the operator, and it
is the operator who is the constraint.

So `generation_mode: multi-pass` is never emitted. Every affected execution takes the
single-pass route its own type already records, and no type becomes unavailable:

- `04-proof-lockedframe` — `strict` needs compositing, so the panels run `handheld`,
  `--verdict` included. Its capability gate already says this.
- `01-pain-split --mirror` — the invariants block, named face, hair, clothes, camera
  height and framing BEFORE either panel is described. The type calls it "the only
  route available to a renderer who does not composite" and it passed 1 of 1.
- `05-social-handoff` — the `inset` is omitted, not the type. The type calls the
  inset-free route "the safer route" on its own grounds.

Where a type offers NO single-pass route, it is unavailable and the slot takes its next
candidate — say so in `page_composition_notes` rather than emitting a prompt the owner
cannot run. **An option whose `pipeline` is not `single-pass` is a routing defect.**

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

**A REPEATING SECTION EMITS ONE OPTION PER SLOT** (ADR-022). Where cross-slot rule 2
applies — a review wall, a roundup, a gallery of equivalent cells — the SET is the
unit of variation, not the cell. Three options inside one tile spend the variation
budget in the dimension that buys nothing, and they open a door no check can close:
each option is legal alone, and a reader picking one register on some tiles and
another on the rest gets a wall that reads as two shoots, which reads as fake. So
emit A only, and let `varies_on` carry the tile's place in the SET — how it differs
from its siblings, not from a B and C that do not exist. Where the type legislates
its own set law, that law decides which execution each tile keeps:
`05-social-snapshot`'s SET DIVERSITY LAW asks for a different room class, surface,
light temperature, camera distance and content mode across the set, and its "where
possible" is a real qualifier — a repeat is allowed when moving the tile would break
FIT, and then the option says which of the other axes carry the difference instead.

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

**So `one-type-once` binds the recommended SET, never the option pool.** The sentence
above is meaningless otherwise: an option can only force another slot to change if it
is allowed to carry a type recommended elsewhere on the page. Read the other way — and
it was, through page 65 — every second type on a seven-slot body looks spent, B falls
back to an axis or an execution every time, and a page ships with no type variation at
all. Measured across the first four routed pages before the correction: 83 of 101
non-A options varied on execution, 11 on axis, and 7 on type. When B does carry a type
recommended elsewhere, name the displaced slot in `composition_notes` and move on. The
only slots that legitimately stay single-type are the ones whose role cell holds one
type after the attribute gates — say that in `varies_on` so the reason is on the record
rather than inferred. `e7dfe8c`

**Enforced since ADR-052, because this paragraph was breached with itself already in
force.** Page 193's first routing shipped 8 of 8 multi-option slots single-type — the
routing session had read the paragraph above during preparation and applied one-type-once
to the pool anyway, which is the page-65 failure recurring with the correction on the
books. So the rule now runs: `scripts/validate.py` fails a session routed after
2026-08-25 whose multi-option slot carries one type across its options, and a session's
own build carries the same check. The legitimate single-type case declares itself in
`single_type_basis` on the slot — the statement this paragraph asked `varies_on` to
carry, made machine-readable: which cell was exhausted, or which set law makes the tile
the unit of variation. Twelve sessions predate the gate and stand as grandfathered
records under one aggregate warning.

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
   `requires_product_photo: true` (and note the `--rivals` exception). Read the
   flag off the EXECUTION, not the type: `02-cause-anatomy --diagnostic` and
   `04-proof-lockedframe --rivals` both override it, and a type-level read calls
   runnable prompts blocked.

**An empty `attachments` is not a blocked prompt.** Owner instruction,
2026-08-17: the reference photo is uploaded by hand in the generation tool.
`attachments` records a sha256 only when the source export supplied one, and
where it did not the field is omitted rather than invented — but the prompt still
keeps its G1 reference block and is still paste-and-run. Say "attach the product
photo", never "cannot run". The one case that IS blocked is a prompt with no
reference block where the type demands one, because then nothing binds the
render to the real product.

## Step 6 — Render through the adapter

Apply `adapters/nano-banana.md` (or the target model's adapter): negative
translation, reference-image phrasing, ratio parameter. The canonical prompt stays
model-agnostic in the type file; only the rendered output is model-specific.

**Nothing is expanded into `steps[]`, ever.** This step used to end "and — for
`generation_mode: multi-pass` — expand `steps[]` with the adapter's edit-script
template", which is the exact thing Step 3 forbids, in the same file, four steps
apart. ADR-021 declared the capability and corrected Step 3 and
`registry/vocabulary.yaml`; it never came back for this line or for the adapter's
Rule 3, so a session that read Step 3 and then followed Step 6 was told to do both.
A type's `generation_mode: multi-pass` is a fact about what the PICTURE needs, and
it stays true in the type file — what it never does is reach a delivered option.
Take the type's own single-pass route (ADR-021, ADR-039).

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
to act on than a stated "no". One form:

- **whole-frame** — the loop replaces the WHOLE slot asset and takes the slot's own
  declared ratio. Available to any type, because it adds no layer to any frame. `none`
  is the only other value and it is what a negative verdict carries.

**The still is always a complete picture, and it ships on its own** (ADR-051). It renders
everything the type legislates, insets included, and nothing in it is reserved, blanked or
left empty for a loop to land in. A loop is an UPGRADE to that slot, never a component the
render is missing: the editor learns which slots carry one from the app, which marks them
already, and builds the loop to drop in. ADR-033 did the opposite — it reserved the host
type's legislated layer as a flat empty block — and its own recorded consequence was that
the render could not ship until the loop arrived. That risk is removed at the source here
rather than managed, and the three options a slot carries are photographs in every case.

A slot earns motion when its declared reason to exist is **temporal** — a transition, a
sequence, a state changing, an output flowing. A slot that exists to reveal an angle, a
place or a colorway does not, and gets `eligible: false` with that reason.

**Then say what the loop ARGUES: `gif.kind`, from the `jobs` vocabulary.** The loop replaces
the whole slot, so its kind is the SLOT's own job — the job the routed type was chosen to do
there. Where the section's copy argues more than one of them, take the one **the copy is
already making**, and say which and why in `reason`: this is the same judgement as choosing a
type, made one level down. The kind sets what the brief describes and what the loop has to
leave the viewer holding, and nothing else changes with it.

Before ADR-051 this field read the job of the LAYER a loop lived in, which could differ from
the type's own job — an inset inside `06-relief-hero --recall` did `pain` work. There are no
layer-bound loops now, so that split is gone and `kind` equals `type_id` for every routable
type, which is what ADR-023 said it would in the first place.

Every GIF is delivered as this spec block, and `scripts/gen-plate.py` draws the same fields
as an SVG beside the still (G12, ADR-028, ADR-051):

```
output: advertorial-seat-cushion-l-shaped-v04-content-items-3-image.mp4
ratio: 16:9
duration_s: 2.5
loop: seamless loop

brief: Inside a car during a sharp turn, a generic cushion slides several inches across
the slick leather seat, then the reference cushion stays completely locked to the seat
leather without shifting an inch.

alt: Camera locked onto a tilted car seat base while a hand pulls a generic pad that
slides freely, contrasted with the reference cushion resisting lateral pull completely.

delivery: mp4/webm
```

`duration_s` is a number and fractional values are legal — 2.5 is a real answer where the
beats need it, and the type's declared band is a band rather than a set of integers.

**`gif.output` is the session's own name with the SLOT appended** (ADR-051):
`{page-type}-{product-slug}-v{NN}-{slot-id}.mp4`, the slot id with its dots turned to dashes.
Take the session directory, `{page-type}-{product-slug}-v{NN}` (ADR-034), and add the slot.
The page id stays out — it identifies the source export rather than the loop and lives in
`page_id`, and one routed session has none at all. It is the ONLY name a loop has, and the
library files it under the same string.

The gif TYPE is no longer in the name. It moved to `gif.type_id`, which is the field that
decides the library folder and always was; what the name buys instead is a join back to the
exact slot the loop fills, without opening anything.

**At most one loop per gif type is a PREFERENCE, not a rule** (ADR-051 demoting ADR-037). It
was a rule because the old filename had no slot and no sequence, so two loops arguing the
same thing collided; the slot id is unique on a page by construction and the collision is
gone. A page carrying two `mechanism` loops in two different blocks is legal — say so in
`motion.notes`, on the same footing as the working/result coverage pair, and prefer two
different arguments where the copy offers them.

**Delivery is `mp4/webm`** (ADR-051 amending ADR-047), muted. Both containers carry an audio
track where WebP could not, so muted stays a stated requirement rather than a property of the
format. Where a slot earns motion the page template needs a `<video>` element with
`autoplay`, `muted`, `playsinline` and `loop` — a still sits in an `<img>` and neither of
these does — so the template dependency ADR-047 named is unchanged by adding webm.

**Every claim in the brief must be satisfiable by the still the slot routed (G12).** A brief
promising something the frame does not contain sends the editor to build the wrong loop, and
that is the dominant fault at 2 of 4 plus the page 73 case found after shipping. Write the
brief against the recommended option's own prompt, and check it line by line against that
prompt before it ships — the setting field exists so that check has something to catch.

**The plate is a file, not a prompt.** `python3 scripts/gen-plate.py <session-dir>` writes
one SVG per positive verdict, drawn at `gif.ratio`, carrying the four fields plus the
library folder from `gif.refs`. It is a generated view like `registry/index.yaml` and the
GIF library's folder cards, and it is never hand-edited. There is no `gif.prompt`: a plate
is text, and generating text through an image model is the least reliable way to produce it
— the seven-word line cap, the ban on markup and the whole geometry block of the old G12
were all workarounds for a renderer that is no longer involved.

**The plate never ships.** It takes the `--brief` suffix and a `.svg` extension and never the
slot's own asset filename; a page asset carrying one is a defect. It travels beside the still
as its own file, which satisfies ADR-019 — the work order reaches the editor rather than
sitting in a document nobody opens — without putting model-drawn lettering into a frame G6
bans text from. Since ADR-051 it is a second view of the spec block above rather than the only
carrier of it.

Delivery is mp4 or webm, muted, with a size ceiling — a 20 MB `.gif` costs more conversion
than the motion buys, and that was the complaint ADR-023 settled on mp4 for in the first place.

**In `prompts.md` the gif sits below option C**, carrying the four fields and naming its
plate file. It is not an alternative to A–C — the recommended still is still rendered,
because a loop is an order to an editor with a lead time and the page has to ship today
(ADR-020). What changed at ADR-028 is that there is no fourth PROMPT to paste: the still
options are prompts, and the gif is a work order.

## Step 5d — MOTION BUDGET (page-level, runs once every slot has a 5c verdict)

Step 5c asks whether a slot earns motion. This pass asks how many loops the PAGE
carries, and it is the only place a shortfall may be filled. Its output is the
`motion` block, emitted on every routed page including pages that carry no motion —
a stated zero is actionable and a missing block is not.

**Owner standing instruction, 2026-08-19: floor 2, ceiling 5.** The floor is a real
floor: a page below it is not finished, it is reported. All five routed sessions
already clear it on rung 1 alone (5, 6, 4, 2, 2 positive verdicts), so the ladder
below exists for the thin pages that have not been routed yet, not for the ones that
have.

**Coverage is a preference, not a gate.** Aim for one loop from a `working` type
(`use`, `mechanism`, `cause`) and one from a `result` type (`proof`, `relief`), read
off each type's `group`. Where a page's natural pair is two `working` loops, keep it
and say so in `motion.notes`: restaging a strong slot to fill a column buys a tidy
table and loses the better argument.

**The ladder. Work down it only until the floor is met, and never past rung 2.**

1. **Natural** — the 5c verdict as it stands. Nothing is re-argued.
2. **Re-execution** — a slot whose STILL execution earns no motion, where a different
   staging of the same argument does. The library's main case is a `proof` slot routed
   to a locked multi-panel comparison: the panels are inspected rather than watched and
   correctly get `eligible: false`, while one continuous frame in which one variable
   changes earns motion on the same claim. Page 65 carries the unrouted example — an
   indicator that turns red to blue as the head passes, filed by that session as "a
   state, not a transition". The job never changes; name the move in `varies_on` and in
   `gif.reason`, and set `gif.rung: "re-execution"`.
3. **Ambient** — pleasant movement that argues nothing: steam curling, a curtain
   breathing, dust in a sunbeam. **Off by default and never used to reach the floor.**
   It ships only when the owner switches it on for a named page. Grounds: of the eight
   market pages scanned on 2026-08-18, every ambient element found was a theme's own CSS
   (a marquee, a wave, an animated badge border) and none was a produced asset — nobody
   pays an editor for motion that carries no argument.

**Below the floor after rung 2, report it.** Set `motion.shortfall_reason` naming which
slots were examined at rung 2 and why each failed. This is SPEC §7.5's rule — an absence
is not automatically a gap — applied to motion. Never reach the floor by switching
ambient on, and never by lowering the temporal test.

**Ceiling and spacing, both binding:** at most 5 loops on a page, and **at most one per
section — plus ONE more where the section carries five items or more and the two are not
adjacent** (ADR-032 amending ADR-024). A repeating list still counts as one section, not one
per item, and which items keep the motion is decided by the section's own set law rather than
by position.

**What a section IS, because the rule is arithmetic on the slot id** (ADR-050). A section is the
slot id's top-level prefix, plus its next segment when that segment is a NUMBER. A number sitting
directly after the prefix is a BLOCK index and each block is its own section; a number sitting
after a container word — `items`, `photos`, `shots`, `quotes` — is an ITEM index and the list
stays one section.

```python
def section(slot_id):
    p = slot_id.split(".")
    return f"{p[0]}.{p[1]}" if len(p) > 1 and p[1].isdigit() else p[0]
```

So `content.1.items.3.image` and `content.3.items.0.image` are two sections, `reason.0.image` and
`reason.4.image` are two sections, and `features.items.0.image` through `features.items.4.image`
remain one — the case ADR-024 was written against, untouched. The rule used to read the prefix
alone, which merged every editorial block a template numbers under one name: on the exports now
arriving, an opener at `content.0`, a five-card list at `content.1` and a two-card list at
`content.3` were one section between them and the page body was allowed 2 loops for all three. It
is allowed 4.

The relaxation exists because the floor had no margin. Measured across every page routed
under the unamended rule — 58, 65, 73 and 77 — loop-capable sections came to exactly 2 and
delivered loops came to exactly 2. The floor equalled the structural ceiling on all four, so
a single loop that could not be built put the page below the owner's standing floor. ADR-024
set one-per-section against a measured fairground (page 31 drafted four moving tiles inside
one feature list); two loops with a static item between them in a list of five is not that
image, and the not-adjacent clause is what keeps it from becoming it.

**Every delivered loop carries `gif.alt`**, a second way to shoot the same argument in the
same slot. It drops whatever the primary is most likely to be blocked on — an actor, a moving
car, an interior — and keeps the claim. It is printed on the plate under the primary, so the
editor holds both.

**`motion.reserves` lists the slots that lost.** A slot that earned motion on the argument and
was refused by the budget or the spacing rule is a reserve for a named primary in the same
section, provided promoting it would leave the spacing rule satisfied. A reserve REPLACES its
primary; it never adds to one. A section already carrying its maximum has no legal reserve and
says so — that is the case `gif.alt` covers, and on a maximised page it is the only cover
there is.

**`motion.margin` is delivered minus floor, emitted on every page.** Zero margin is the state
every page routed before ADR-032 was in, and it is a number rather than something a reader has
to derive.

**Adjacency binds inside a section and nowhere else.** ADR-024 dropped the general
never-adjacent clause because across a section boundary a heading and a block of copy sit
between the two slots, and enforcing adjacency there dropped page 58 below the owner's floor
for no reader-visible gain. That still holds: two loops in consecutive sections are fine.
What ADR-032 added is narrower — the SECOND loop inside one long section may not sit next to
the first, because there the two really are in the same eyeful with nothing between them.

Where the ceiling or the spacing rule kills a positive 5c verdict, flip that slot to
`eligible: false`, say in its `reason` that the budget and not the argument decided it,
and record the conflict in `motion.notes`.

**No social-proof slot carries motion, and the review wall is the strictest case.**
Owner instruction, 2026-08-19: no tile in a repeating review section carries motion,
whatever its quote says. The mechanism is wider than the wall, and stating it plainly is
what a router actually hits — **the six-type set carries no `social` type**, so a
social-proof slot has no gif type to file under, wall tile or standalone.

Three of three review walls on the market pages scanned are static, and 14 of 15
`social`-role slots across the routed sessions already refused motion on the type's own
grounds. The fifteenth, page 13's `social-viral`, is a **standalone** slot and not a wall
tile — page 13 has no repeating review section at all. ADR-023 named the wall rule as
what supersedes that verdict and was wrong on the point; it is the absent type that does
(ADR-024). Page 13 stands and is not re-routed.

**Then name the medium.** Every slot carrying options sets `recommended_media`. It is
`still` unless the slot's argument is carried better by the loop than by any of A/B/C,
and `gif` says exactly that — it does NOT withdraw the still. The recommended still is
emitted and rendered as always, because the loop is an order to an editor with a
lead time and the page has to ship today (ADR-020). Explain the call in
`recommendation_basis` like any other.

**Each positive verdict also carries its library pointers**, so an editor never has to
be told where to look: `gif.type_id` (the folder), `gif.refs` (that folder plus one or
two filenames from it) and `gif.output` (the returned filename, which now carries the gif
type). Since ADR-028 the plate is generated rather than drawn, so `refs` and `output` are
PRINTED ON IT along with the brief — nothing about a gif slot lives only in a file the
editor will not open.

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

**Log every slot, including the ones that offered no choice.** The record stays one
per slot because it is raw evidence and tier 1 is never thinned; what changes is the
DERIVATION, which counts a slot toward SPEC §7.7's threshold only where more than one
distinct type was on offer (ADR-026). So a six-tile review wall is logged in full and
weighs nothing, and the temptation to skip logging it is the wrong economy: the record
is also the audit trail of what the owner was shown.

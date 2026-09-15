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

**Where a `content.json` comes from when the page is a live one:**
`mapping/export-to-content.md`, run by `scripts/export-to-content.py` (ADR-081). It is
mechanical about sections, slot ids and ratios and refuses to guess `role`,
`page.channel` or the eight attributes — the same rule as the paragraph above, enforced
one step earlier. A page routed from a hand-written `content.json` is unaffected.

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

For each `image_slot`, read the slot-rules row for its `role`.
**That row is a PREFERENCE ORDER, not the candidate list.** The candidate list is
**every active type** — 17 of them, for every slot on every page. Row members outrank
non-members at equal fit; a non-member is a candidate, not a violation.

**The row has one column since ADR-059**, because channel stopped being an admission
test. A type preferred for `mechanism` is preferred for `mechanism` wherever the beat
appears, and the four channel columns were the same list written four times.

The distinction is not cosmetic. 43 of the 48 role×channel cells hold fewer than
three types, so a cell-as-pool reading caps most slots at one or two options —
measured across the 13 sessions routed before this rule: **161 image slots, 111 on a
single type, 50 on two, and not one slot in the library's history carrying three.**
An empty cell is not an empty slot: it means no type is PREFERRED here, and the
channel-legal set still decides. Report out-of-scope only where the role itself
carries no image by definition (`cta`, `author`).

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
paste-and-run — one prompt, one generation call. No compositing, no edit chains, no post
assembly.**

**The attachment COUNT was capped at one and is not any more** (owner instruction,
2026-09-09, ADR-076). A prompt may ask for as many reference photos as it has products in
frame. What has not changed is the thing the rule was actually about: ONE generation call,
and nothing assembled afterwards. Where a prompt needs more attachments than the owner's
own app accepts, **it still ships in full** — the owner renders it in a tool that takes
several. A prompt is never trimmed to fit a tool. The adapter's note that the model
supports conversational editing is about the MODEL; this is about the operator, and it
is the operator who is the constraint.

So no option is anything but single-pass. **Since ADR-067 the `multi-pass` value does
not exist**: it is gone from `registry/vocabulary.yaml`, no type declares it, and a file
that tries to is a validation error. Every execution that used to want it takes the
single-pass route its own type records, and no type is unavailable:

- `04-proof-lockedframe` — `strict` states its cross-panel invariants once, before any
  panel is described. Its CAPABILITY gate is retired: it sent `strict` to `handheld`
  wherever the renderer could not composite, which after ADR-021 was everywhere, so it
  was a permanent refusal written as a condition.
- `01-pain-split --mirror` — the invariants block, named face, hair, clothes, camera
  height and framing BEFORE either panel is described. The type calls it "the only
  route available to a renderer who does not composite" and it passed 1 of 1.
- `05-social-handoff` — **no longer a single-pass problem since 2.6.** The inset is
  model-drawn and renders in one pass, 4 of 4 (ADR-053), so neither the inset nor the type is
  omitted. `generation_mode` is now `single-pass`.

Where a type offers NO single-pass route, it is unavailable and the slot takes its next
candidate — say so in `page_composition_notes` rather than emitting a prompt the owner
cannot run. **An option whose `pipeline` is not `single-pass` is a routing defect.**

## Step 4 — Build 3 options per slot, one DISTINCT TYPE each

Owner instruction, 2026-08-26: **every image slot carries exactly three different
image types, the three that fit that slot's content best.** A, B and C are a ranking,
not three dimensions of variation.

- **A — `baseline`**: the best-fit type, with its own best variant and axes.
- **B — `type: <id>`**: the second-best fit. A different type, always.
- **C — `type: <id>`**: the third-best fit. A different type, always.

Rank the whole channel-legal candidate set by the five criteria below, FIT first, and
take the top three. Each option then picks its OWN best variant, axes and execution —
those are how an option is built, never how the pool is filled.

Rules that do not move: an option requiring a pair or carrying channel restrictions
says so in `composition_notes`; never present a gated-out type as an option; never pad
with rerolls. **There is no admission test left, and that is deliberate** (ADR-060).
`channels` went at ADR-059 and `avoid_when` went the day after: every active type is a
candidate for every slot, and what a type is FOR is now argued entirely by `use_when`
through FIT. A type is not refused, it is out-ranked.

Three things still remove a candidate, and none of them is a preference:

1. **The attribute gates** in `mapping/slot-rules.md` — deterministic kill-rules read
   off `product.attributes`.
2. **The cross-slot fields** — `never_with`, `pairs_with`, `avoid_adjacent` and
   one-type-once, all frontmatter, all still binding.
3. **`registry/rules.md`** — the global rules, G14 among them: a generated image may
   never pose as a customer's own. A tile attributed to a customer, on the tile or by its
   wall's lead, takes a real photograph or nothing (ADR-088). A harness that renders routes
   it anyway and ships the prompt flagged for the merchant (ADR-089).

**Ratio is not one of them** (ADR-082, and ADR-086 for this paragraph). No type declares a
ratio, so there is nothing to test a slot's shape against. The slot's ratio arrives from
`content.json` and is passed to the renderer as the aspect-ratio parameter
(`query/output.schema.json`); a type's `SLOT CONSTRAINTS` and G15 say how it composes at that
shape. This list said "four" and still carried a ratio gate after ADR-082 deleted the field
it read: that sweep searched `ratios`, and this item said `ratio`.

**What this rule costs, stated rather than discovered later.** B and C are lower-ranked
by construction, so on a slot whose cell holds one type they will be types the table
never proposed for this role. They are legal — admission never bends — but they are a
weaker argument for this beat, and the recommendation exists to say so. The old model
hid this cost by spending B and C on re-executions of A, which is why the library shipped
161 slots without ever offering a genuine second choice. A weaker third type the owner
can reject beats a third camera angle on the same type he cannot compare.

**Fewer than three surviving types is a real state and declares itself.** Emit what
exists and set `pool_basis` on the slot naming what ran out: which gates fired and how
many types the channel had to begin with. It is not rare on `paid-social`, where only 5
active types are legal at all against 14 on `landing-page`. A shortfall stated is a
record; a shortfall padded is a lie about the library's width.

**A REPEATING SECTION IS ONE SLOT FOR THIS PURPOSE, AND THE SET TAKES THE THREE
TYPES** (ADR-022, amended 2026-08-26). Where cross-slot rule 2 applies — a review wall,
a roundup, a gallery of equivalent cells — the SET is the unit of variation, not the
tile. ADR-022's harm is exact and still stands: each option is legal alone, and a reader
picking one register on some tiles and another on the rest gets a wall that reads as two
shoots, which reads as fake. **That harm comes from mixing types WITHIN one set, and it
is untouched by offering three types FOR the whole set.** So the section carries three
type options at the SECTION level, every tile follows whichever the owner picks, and no
tile is individually switchable. Per tile, `varies_on` still carries the tile's place in
the SET — how it differs from its siblings, not from a B and C that do not exist there. Where the type legislates
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
only slots that legitimately fall short of three types are the ones where the CHANNEL —
not the role cell — runs out after the attribute gates and `avoid_when`. Say that in
`pool_basis` so the reason is on the record rather than inferred. `e7dfe8c`

**Enforced since ADR-052, because this paragraph was breached with itself already in
force.** Page 193's first routing shipped 8 of 8 multi-option slots single-type — the
routing session had read the paragraph above during preparation and applied one-type-once
to the pool anyway, which is the page-65 failure recurring with the correction on the
books. So the rule runs in `scripts/validate.py` rather than on trust.

**Its threshold moved from two to three on 2026-08-26** (ADR-058). The gate used to fail
a multi-option slot carrying ONE type across its options; it now fails one carrying fewer
than THREE distinct types. The shortfall declares itself in `pool_basis` on the slot,
naming which gates fired and how wide the channel was — `single_type_basis` is the
retired name for the same field and is still read, because thirteen sessions carry it.
Those thirteen predate the three-type rule and every one of them would fail it: they hold
161 image slots between them and not one carries three types. They stand as grandfathered
records of completed routings under one aggregate warning, exactly as the twelve before
them did.

**Ranking order, and it runs until THREE distinct types stand — not until one does.**
An image slot with no options is a contract violation (SPEC §7.4); a slot with fewer
than three is a declared shortfall. Work down and keep collecting:

1. **The role's own cell.** The preferred types for this beat. Usually 1-2 of the three.
2. **Adjacent steps.** Role affinity is a preference, not a wall: a `comparison` slot
   may take a step-3 or step-4 type; a roundup entry that indicts an object may take a
   step-1 `job: pain` type. Say which step you moved to in `varies_on`.
3. **The rest of the channel-legal set, ranked by FIT.** Any active type legal on this
   channel whose `avoid_when` does not exclude the case. This rung is where the third
   type usually comes from and it is not a fallback tier — SPEC §7.4 always derived from
   here; only this runbook narrowed it to a cell.

**Rungs 3 and 4 of the old ladder are gone from the POOL and kept for the SET.** They
were "a repeating-section repeat" and "another execution of a type already on the page",
and neither yields a NEW type, so neither can fill a three-distinct-types pool. They
remain what they always were — the honest way to satisfy `one-type-once` in the
recommended set when a page needs the same type twice. Cross-slot rule 2 and
`composition_notes` carry them now, not this ladder.

Nothing on this ladder is an admission test any more (ADR-060). Every rung yields
candidates and the ranking sorts them; what removes a type is an attribute gate, a
ratio it does not declare, a cross-slot field, or a global rule. Every option emitted
is a real active type carrying its own laws; there is no fallback tier, and no image
ships unrouted.

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
**ADR-067 closes it at the source**: `multi-pass` is no longer a value a type can
declare, adapter Rule 3's templates are deleted, and there is no longer such a thing
as "the type's multi-pass route" to fall back from. Every type's route is
single-pass, and where a picture needs the same thing held across two frames the
mechanism is an invariants block stated once, before either frame.

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
output: advertorial-mechanism-seat-cushion-l-shaped-v04.mp4
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

**`gif.output` is the session's own name with the gif type inserted** (ADR-056 restoring
ADR-037): `{page-type}-{gif-type}-{product-slug}-v{NN}.mp4`. Take the session directory,
`{page-type}-{product-slug}-v{NN}` (ADR-034), and put the gif type after the page type. The
page id stays out — it identifies the source export rather than the loop and lives in
`page_id`, and one routed session has none at all. The SLOT stays out too: it went in at
ADR-051 and came out two days later on the owner's instruction, and the join back to the
frame lives in `prompts.json` and on the plate. It is the ONLY name a loop has, the library
files it under the same string, and the type in it names the destination folder.

**One loop per gif type per page** (ADR-056 restoring ADR-037, after a two-day demotion at
ADR-051). With no slot and no sequence in the name, two loops that argue the same thing on
one page would produce the same file, so a page carries at most one of each type — and it
says something true anyway: a page making the same kind of motion argument twice is
repeating itself. Where separate declared sections (ADR-087) tempt a second loop of one type
(`mechanism` on `content.1` and again on `content.3`), the second slot takes a different
argument or no loop, and `motion.notes` records the call.

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
adjacent** (ADR-032 amending ADR-024). A list of equivalent entries under one lead still counts
as one section, not one per item, and which items keep the motion is decided by the section's
own set law rather than by position.

**What a section IS: the section `content.json` declares** (ADR-087, superseding ADR-050's
arithmetic on the slot id). Every `image_slots` entry belongs to exactly one entry of
`page.sections[]`, and that entry is the unit counted by all three: the spacing rule, the
ceiling's per-section clause, and cross-slot rule 2's repeating-section exception. A section is
one block of the page carrying one role and one `copy_summary`:

- **An entry that carries its OWN copy is its own section**, even when the template numbers it
  inside a list. The seven reason cards of page 219 (`content.items.0` … `.6`, each with a
  heading and a body) are seven sections carrying six different roles.
- **Entries that carry no copy of their own are ONE section with N entries.** These are
  equivalent tiles under one lead: a review wall's `reviews.shots.0-3`, a gallery of cells, a
  feature list whose items are images and nothing else.

The slot id is never consulted for this. The same key shape, `content.items.N.image`, is seven
sections on one template and one section on another, and only the declared structure can say
which. So whoever assembles `content.json` decides the count by how it groups slots into
sections: a session by hand, the worksheet of `scripts/export-to-content.py`, or the consuming
app. Step 1 validates that document before anything is routed.

ADR-050 read the id arithmetically. Page 219 was nonetheless routed on 2026-08-26 under the
declared reading, with four loops across `content.items.0` … `.5`, two of them on adjacent cards,
while this step still taught the arithmetic one.

**Adjacency binds between the ENTRIES of one declared section and nowhere else.** Two loops on
consecutive cards that are separate sections are fine, the same way two loops in consecutive
named sections always were.

The relaxation exists because the floor had no margin. Measured across every page routed
under the unamended rule — 58, 65, 73 and 77 — loop-capable sections came to exactly 2 and
delivered loops came to exactly 2. The floor equalled the structural ceiling on all four, so
a single loop that could not be built put the page below the owner's standing floor. ADR-024
set one-per-section against a measured fairground (page 31 drafted four moving tiles inside
one feature list); two loops with a static item between them in a list of five is not that
image, and the not-adjacent clause is what keeps it from becoming it.

**Since ADR-087 that clause guards a list of equivalent entries, not a list of cards.** Page
31's five feature cards each carry a heading and a body, so under the definition above they are
five sections. Its four moving cards, three of them adjacent, would pass the spacing rule, and
only the page ceiling bounds them. The owner accepted that cost knowingly on 2026-09-15.

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

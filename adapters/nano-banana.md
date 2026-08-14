# Adapter — nano banana (Gemini image generation)

Transforms the library's model-agnostic canonical form into prompts for nano banana
(Gemini 2.5 Flash Image family). Applied at render time (query/runbook.md Step 6);
type files never store model-specific output. Model churn is absorbed HERE — new model
version, new adapter file, zero type-file edits.

Verified facts this adapter is built on (Google Developers Blog, "How to prompt Gemini
2.5 Flash Image Generation for the best results", fetched 2026-08-10):

- **No negative-prompt parameter.** Official guidance is "semantic negative prompts":
  describe the desired state positively ("an empty, deserted street with no signs of
  traffic" instead of "no cars").
- **Reference images**: one or more images may accompany the text prompt for editing,
  composition and style transfer; the model analyzes the original's style, lighting
  and perspective.
- **Conversational editing** is supported ("Keep everything the same, but…") —
  multi-pass pipelines are officially viable.

## Rule 1 — Negative translation

The canonical NEGATIVE list (G6 + type + variant additions) has no channel of its own.
Transform it:

1. **Positive assertions first**: where the skeleton already asserts the positive form
   ("clean uncluttered background", "flat solid badges"), the matching negative token
   is DROPPED (it is already covered semantically).
2. **No closing `avoid` sentence.** Owner decision, 2026-08-13, measured: he removed
   `Strictly avoid: text, letters, circled letters, watermark, deformed hands, extra
   fingers` from a prompt set by hand and re-rendered, and the output did not change. The
   line had never been tested in isolation because it was inherited by habit. Prompts for
   every type now ship without it.

   What that leaves: the canonical NEGATIVE list stays in each type file, model-agnostic,
   and the `avoid` field stays in the query output for a future model with a real negative
   channel. Nothing is emitted into the prompt text.

   One observation on the other side, recorded rather than argued away: a
   `03-mechanism-ghostbody` render with no avoid line came back with dimension arrows
   labelled `W` and `L`, which G6 bans. The likelier cause is the `dims` mark itself — a
   dimension arrow attracts a label the way a slot named ZONE A attracted a printed A — and
   the letter ban now lives in that mark's own definition. If letters, watermarks or
   malformed hands recur across types, this rule comes back with evidence behind it.
3. **Drop SD-idiom tokens** that carry no semantics for this model: quality boilerplate
   ("low resolution", "blurry" as generic tokens), style-negation stacks. Keep concrete
   content exclusions (e.g. "no VS badge", "no red glow on the right panel") — phrase
   them into the relevant scene sentence where possible.

The rendered `avoid` line is emitted separately in the output JSON (`avoid` field) so a
future model with a real negative channel can consume the canonical list instead.

### Rule 1a — Never put a REQUIRED element in the avoid line (measured 2026-08-12)

**Scope after 2026-08-13:** no avoid line reaches the model any more (step 2 above), so this
rule no longer guards a rendered prompt. It still governs the canonical NEGATIVE list and the
`avoid` field in the query output, and it is kept in full because it is the reason the field
must never be pasted anywhere verbatim. If the line ever returns, it returns under this rule.

The `avoid` line is prose to this model: no negative channel, no logical operators. A
qualifier therefore does not survive. "No third badge" in a prompt that mandates two
badges reads as "no badge", and the badges do not render. Owner report that opened this:
"model chưa thực hiện đủ dấu, có những image trả về không có bất kì dấu gì."

The trap is worse than it looks, because the natural fix fails the same way — rephrasing
keeps the token and keeps the bleed. Six instances caught by script across four prompt
sets in one session, every one written by an author who already knew the rule:

| written in `avoid` | element it suppressed |
|---|---|
| `a second badge` | the mandated centre VS badge |
| `a fourth badge` | the three mandated rail badges |
| `an arc in the right panel` | the mandated left-panel angle arc |
| `a smooth featureless coating` | the mandated amber coating |
| `brand logos on the old filter` | the reference filter itself |
| `one panel brighter than the others` | the required exposure drift |

**The rule is DROP, not rephrase.** Any `avoid` phrase that uses an adjective to qualify
a noun the prompt requires will bleed. Assert the bound positively in the slot instead —
"exactly two badges, both in the top corners, the only badges present" — and delete the
token from `avoid` entirely. This is Rule 1 step 1 applied strictly; the additions above
are all cases where step 1 was skipped because the negative *felt* more precise.

Mechanical gate before shipping any prompt: for every token in `avoid`, search the prompt
body for the same lemma. A hit that is not a deliberate prohibition is a bug. Match
lemmas exactly — a `stain\w*` pattern matches "stainless" and yields false positives, and
layout vocabulary (`panel`, `framing`) is not at suppression risk because the layout is
restated every line.

### Rule 1b — A heading that names a REGION gets drawn into that region (measured, 3 types)

The model draws headings it is shown — but not all of them, and the difference is what the
heading is attached to. `02-symptom-rail` printed large circled A, B and C into a frame because
its prompt carried `ZONE A`, `ZONE B`, `ZONE C` as headings, and G6 plus an avoid line
containing `text` did not stop it. `03-mechanism-ghostbody` then printed `XCHECK` in capitals
above an inset. `06-relief-hero` 1.9 carried ten instances — `HERO:`, `INSET,`, `LEFT`, `RIGHT`,
`FIRST`, `SECOND` — and was caught by a gate before rendering (`42b2dea`).

Three tiers of heading, and only the third has ever leaked:

| tier | examples | evidence |
|---|---|---|
| whole-image | `REGISTER`, `PRODUCT REFERENCE`, `LIGHT` | shipped alongside every measured leak on 3 types, never drawn |
| subject | `[ADVOCATE]`, `[LISTENER]`, `[PRODUCT]`, `[ENVIRONMENT]` | `05-social-handoff`, 3 of 3 renders clean (`27f19e3`) — three runs, recorded as three |
| **region** | `ZONE A`, `LEFT:`, `HERO:`, `SCENE right 58%:` | drawn on 2 types, caught pre-render on a third |

**A rendered prompt describes a region; it never names one.** "A small two-panel inset in the
top-left corner" or "the half on the left", not `XCHECK:` or `LEFT:`. A region's position and
frame share are still a real prompt job (Rule 4) — they belong in the block's BODY, never in its
label. Banning letters does not fix this, because the leak comes from the prompt's own structure
rather than from an instruction.

## Rule 2 — Product reference (G1)

When `requires_product_photo: true`: attach `product.reference_photos` and keep the G1
block verbatim as the FIRST paragraph of the prompt. With multiple layers showing the
product, keep the "identical in every layer" sentence. Never describe the product's
appearance in text (G2) — the reference image carries it.

## Rule 3 — Multi-pass expansion

For `generation_mode: multi-pass` (or a variant override), emit `steps[]`:

**Template A — locked-frame panel series (`04-proof-lockedframe` strict, `01-pain-split--mirror`):**
1. `generate` — one panel only, at the panel's own aspect ratio, from the panel-1
   portion of the prompt.
2. `edit` — "Keep everything in this image exactly the same — camera, framing,
   lighting, background, every fixed object — and change ONLY [the variable]:
   [panel-2 state]." Repeat per remaining panel.
3. `composite` — assemble panels with the gutters/borders from the skeleton in an
   image editor; do not ask the model to draw the multi-panel frame.

**Template B — reference-true inset (`05-social-handoff`, any inset that must match a
real product):**
1. `generate` — the scene WITHOUT the inset.
2. `composite` — place the inset in post using the actual reference photo (cutout on
   white), per the skeleton's position/size. The model never repaints the inset.

**Template C — same-person pair (`01-pain-scene` + `06-relief-scene` bookends):**
1. `generate` — the pain scene.
2. `edit` — "Same person, same palette and grain: [relief-scene prompt]" using the
   pain output as reference input.

## Rule 4 — Ratio and framing

Pass the slot's `ratio` as the generation aspect-ratio **parameter**. Do NOT state it
in the prompt text: this model ignores a written ratio, so the words cost tokens and
buy nothing.

**Evidence (supersedes the earlier belt-and-suspenders instruction), 2026-08-11 —
6 of 6 renders across three sessions, every one off the requested ratio:**

| session | prompt asked | render returned |
|---|---|---|
| GIF-inset v1 | 2:1 (2.00) | 1376x768 = 1.79:1 |
| GIF-inset v2 | 5:3 (1.67) | 1200x896 = 1.34:1 |
| GIF-inset v3/v4 | 5:3 (1.67) | 1200x896 = 1.34:1 |

Recurrence 6/6, far past the >=2/3 rule, and the owner's verdict on those renders was
`pass` — the outputs were usable at whatever aspect the model chose. The written ratio
was never doing the work the old rule claimed. Ratio remains a real slot requirement:
it lives in slot metadata and in the render parameter, and the page layout depends on
it. It simply stops being prompt text.

**A two-panel comparison in a square canvas may duplicate into a 2×2 grid** — 3 observations
across 2 types. The earlier reading, that this followed from asking a WIDE ratio on
wide-and-short content, is superseded: the third case asked 1:1, received 1:1, and still
repeated its two panels as a second row with the badges on the top row only. The common factor
is a two-panel comparison in a square frame, where the model fills the vertical space it has by
repeating what it already drew. Mitigation: state that each panel occupies the FULL HEIGHT of
the frame and that the frame contains nothing else. Untested.

Corollary for framing: what a prompt CAN control is composition — the share of frame a
subject occupies, which side it is offset to, layer footprints in percent. Those
survive any aspect the model returns, and they are what the framing sentences should
spend their words on. The register still opens the prompt ("a cinematic film still",
"an e-commerce lifestyle banner"); only the numeric ratio is dropped.

## Rule 6 — Prompt economy (house style)

Measured 2026-08-11 on the GIF-inset test set: a rendered prompt written as flowing
prose carried ~57% waste against the same prompt written in slot form, with every
functional constraint intact. Compression is not a stylistic preference here — the
waste came from four repeatable mistakes, so the rules are mechanical:

1. **Never invent a block a slot already covers.** Density belongs in the skeleton's
   own `Setting:` slot, not in a new `ENVIRONMENT DENSITY` heading beside it. A new
   block where a slot fix was needed is how skeletons rot.
2. **Never restate a global rule.** Rules are referenced by ID in the type file and
   expanded here at render time — G6 and G10 both work this way. A prompt carries the
   expansion once; the type file never carries the text.
3. **Enforce Rule 1 above.** 63% of the avoid tokens in the pre-compression set were
   already asserted positively in the prompt body. Drop them; the remainder is usually
   5-7 tokens, not 16.
4. **Slot form, not prose.** A labelled block, then the fills. Connectives, restated
   negatives and hedging words cost tokens and buy nothing from this model. **Label the
   block for its subject or for the whole image, never for a region of the frame** —
   `[ADVOCATE]`, not `SCENE right 58%:`, per Rule 1b. Slot form was never what leaked; the
   label was, and frame share belongs in the block body.

Reference numbers from that set: a GIF-inset prompt lands at ~1450-1600 characters and
~225 words. A prompt past ~2500 characters should be re-read for a duplicated block.

**Render-verified 2026-08-11** (`eval/render-tests.jsonl`, 06-relief-hero v1.6, user
verdict pass): slot-form prompts at this size render correctly. Single run, so the
style is confirmed workable rather than proven recurrent — treat a degraded render on
a compressed prompt as new evidence, not as a settled failure.

## Rule 5 — Known weaknesses (emphasize, don't fight)

- **Hands at close range**: highest failure rate (03-use-sequence, knife examples).
  Keep hand descriptions short and functional; put `deformed hands, extra fingers` in
  the avoid line; expect retries.
- **Text in image**: this model renders SHORT text well (user-verified 2026-08-10) —
  sanctioned generated text: `05-social-card`'s review card (≤12-word quotes,
  glyph-check shipping gate) and `03-spec-split`'s VS badge (composite in post
  remains the fallback whenever a render misses). Long text and dense UI digits
  stay composited (screens, memory logs — see G6 scope note).
- **Multi-region consistency** (same face, same colorway across regions of one image):
  do not fight it in one pass — that is exactly what Rule 3 exists for.
- **Layered composites** (hero + inset + product view): if a layer drops out, generate
  the base scene first, then add layers via edit steps one at a time.

## Rule 7 — Marks are model-drawn (ADR-008)

Graphic marks — arrows, glows, hotspots, badges, reference lines, signal arcs, auras,
squiggles — are **described in the prompt and drawn by the model**. There is no
compositing pipeline for them and no `marks[]` field in the query output. The mark
belongs in the prompt text, in the slot its type's SKELETON assigns it.

This settles PRODUCTION only. **Which** mark an image carries is still decided at
prompt-creation time and is not this adapter's business — that is an argument decision
governed by the type and by whatever mark rule the registry grows.

Two existing exceptions stand and are NOT marks:

- **Text** — labels, numerals, spec callouts, screen digits. G6's production law already
  routes these to post-composite. A mark that needs a word is not a mark, it is a
  callout, and it leaves the render.
- **Reference-true insets** — Template B above. The model never repaints an inset that
  must match a real product.

### What this costs, so the cost stays visible

1. **A baked mark cannot be A/B tested.** Changing a mark's colour, count or position
   means re-rendering the whole image, and the base changes with it — so the comparison
   is never clean. Optimising marks empirically is off the table while Rule 7 stands.
2. **One base cannot serve two channels.** A marketplace image without marks and a
   landing-page image with them are two renders, not one render and one stamp.
3. **Precision-dependent classes are at the model's mercy.** Named by risk:
   - paired dashed reference lines (`02-cause-anatomy`) — the `[MEASUREMENT RULE]`
     demands two lines identical in everything but angle; a model draws two lines that
     merely resemble each other,
   - exact counts — "exactly 3 hotspots" (`01-pain-split`), "3 vignettes not 4"
     (`02-symptom-rail`), "ONE directional arrow" (`06-relief-hero --recall`),
   - badge position and colour, which the badge law fixes together precisely because
     the market gets all three wrong and the model has seen a lot of market.

### Omission is the third failure mode (2026-08-12)

The risk list above is entirely about drawing marks WRONG. Owner reports add a mode it
did not anticipate: marks **absent altogether**. Under approach A nothing downstream can
add a missing mark, so an omission costs exactly what a malformed one costs — a re-render.

Two causes, one confirmed present and one hypothesised:

- **negative bleed** (Rule 1a) — confirmed by inspection in the prompts that produced the
  reports and fixed there; re-rendered 2026-08-12 (see below) but never in isolation, so
  its individual share of the blame is still unmeasured;
- **burial** — a mark written as a sub-clause inside a photographic slot competes with a
  register stated first and reinforced every line. Marks that own a named slot
  (`[BADGES]`, `[CENTER BADGE]`) are hypothesised to survive where buried ones drop.
  Untested; the cheapest test is a prompt pair differing only in slot structure.

The reverse mode — the model ADDING a mark nobody asked for — now has **6 observations** of
one glyph: a four-pointed sparkle in the corner. Five of them arrived together in the
`02-cause-anatomy` MARKS batch of 2026-08-12, and the consistency is the finding — same
bottom-right corner, same form, same neutral grey, across two illustration styles, five
different grounds and mark counts of four and five. A drawn element would vary with style,
and every one of those prompts closed its mark block with "nothing in the frame is marked
that is not named here", which did not suppress it.

That reads as a platform watermark rather than a drawn element, and no prompt can remove
one. It is **not settled**, and the reason is on this page: the four mark-free controls of
the restraint test below were explicitly clean, so the glyph is not on every render this
model returns. Two cheap things would settle it — whether the render tool has a watermark
setting, and whether the glyph survives a prompt that names the bottom-right corner as
deliberately empty. Until then, treat it as a platform artefact rather than a Rule 7
failure, and crop it in post on any channel that cannot carry it.

### First re-render after both fixes: marks present in 10 of 10 (2026-08-12)

`~/Downloads/mark-restraint-test.md` was rendered in full — 10 prompts, 6 mark cases
across the BADGE and GRAPH families, 4 mark-free controls — every one owner-verdict
`pass` (`eval/render-tests.jsonl`, ts 2026-08-12). What that does and does not settle:

- **Omission did not recur.** Every mark the six mark cases asked for was drawn. But
  both fixes were applied to every prompt TOGETHER, so the session cannot apportion
  credit between them. That file's own claim — that cases 1 and 4 isolate the
  negative-bleed fix — is wrong: those prompts carry the named-slot rewrite too. The
  burial test named above, a prompt pair differing ONLY in slot structure, is still unrun.
- **The three at-risk classes each survived one run**: paired dashed reference lines
  (case 6), exact counts (case 1 — two badges and three hotspots; case 4 — three diagram
  badges where the ledger's exemplar showed six), badge position and colour (cases 1–3).
  One run per class is breadth, not a denominator; the risk list above stands unchanged.
- **No spurious mark appeared** in any of the four controls, against the single prior
  observation of an unrequested sparkle glyph. It did not recur in this batch — and that
  clean result is now the main evidence AGAINST the watermark reading above, which five
  further observations on 2026-08-12 otherwise support.
- **No class has earned the post-composite exception.** ADR-008's approach A survives its
  first real test. Nothing here flips it — and nothing here proves it either, at one run
  per class.

### When a class fails, do this rather than abandon Rule 7

Log the failure to `eval/render-tests.jsonl` like any other. If the SAME class fails on
≥2/3 runs or across ≥3 observations, that class — and only that class — moves to
post-composite, recorded as an exception here with its evidence. Rule 7 is the default,
not a prohibition on ever compositing anything.

Reference material: `~/Downloads/mark-integration-test-v3.md` holds seven skeleton-
faithful A prompts covering every mark family the registry uses. Rendering the A column
is the cheapest way to find out which classes, if any, need the exception above.

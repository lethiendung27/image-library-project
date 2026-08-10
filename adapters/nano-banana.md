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
2. **Hard exclusions** become one closing `avoid` sentence appended to the prompt:
   `Strictly avoid: text, letters, numbers, watermarks, logos, deformed hands, extra fingers.`
   Keep it to the tokens that matter for this render (cap ~12 items); prioritize
   G6 items + the type's highest-risk items (from worked-example annotations).
3. **Drop SD-idiom tokens** that carry no semantics for this model: quality boilerplate
   ("low resolution", "blurry" as generic tokens), style-negation stacks. Keep concrete
   content exclusions (e.g. "no VS badge", "no red glow on the right panel") — phrase
   them into the relevant scene sentence where possible.

The rendered `avoid` line is emitted separately in the output JSON (`avoid` field) so a
future model with a real negative channel can consume the canonical list instead.

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

Pass the slot's `ratio` as the generation aspect-ratio parameter where the surface
exposes one; ALSO state it in the first prompt line ("A wide 2:1 e-commerce banner…")
— belt and suspenders, and it survives surfaces without the parameter.

## Rule 5 — Known weaknesses (emphasize, don't fight)

- **Hands at close range**: highest failure rate (03-use-sequence, knife examples).
  Keep hand descriptions short and functional; put `deformed hands, extra fingers` in
  the avoid line; expect retries.
- **Text in image**: unreliable — the only sanctioned text is `03-spec-split`'s VS
  badge, and the plan of record is compositing it in post.
- **Multi-region consistency** (same face, same colorway across regions of one image):
  do not fight it in one pass — that is exactly what Rule 3 exists for.
- **Layered composites** (hero + inset + product view): if a layer drops out, generate
  the base scene first, then add layers via edit steps one at a time.

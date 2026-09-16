---
id: 06-relief-hero
step: 6
job: relief
device: hero
version: "1.19"
status: active
replaced_by: null
channels: [landing-page, marketplace, paid-social, advertorial]
requires_product_photo: true
generation_mode: single-pass
axes:
  register: [commercial, ugc]
  inset_mode: [vsinset, recall, context, detail, none]
  inset_motion: [still, loop]
variants: []
exempt_from: []
pairs_with: [01-pain-split, 01-pain-scene]
never_with: []
text_layer: [title, copy]
copied_from: 06-relief-hero
copied_at_version: "1.18"
blocked_by: null
---

# 06-relief-hero

## PURPOSE
Sell the state after buying, with the product in frame. Configured on three independent
axes — `register` (commercial | ugc), `inset_mode` (vsinset | recall | context | detail |
none) and `inset_motion` (still | loop) — named `06-relief-hero--{register}--{inset_mode}`.

**Copied verbatim from `registry/types/06-relief-hero.md` at version 1.18** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## LP2 LAW
Added 2026-09-16 (ADR-094): the owner's gallery instruction for Outcome Hero. This section is
this copy's own and a re-copy keeps it; `registry/pdp-dr-instruction.md` binds the rest.

- **The words.** A title of 2–5 words — the relief state as the reader feels it. Copy of 6–10
  words only where earned, by a timeframe or a mechanism. At most one chip, and only where
  earned. The setting's text ban stands for every prop.
- **The text block or the inset occupies 70–85% of the space the subject is offset from**, as
  `offset` already says, and nothing else is reserved there.
- **No inset in the bottom-right corner** — `--detail` "at a corner" means one of the other
  three. One of the owner's two vsinset renders sat there.
- **A seated product is seen whole** (the instruction's product section): a side profile or a rear
  three-quarter, at least 15% of the frame, on a host of a clearly different tone.
- **Place:** image 2 or 3, or the closing tile; the first one closes the problem phase.
- Commercial by default, and `--ugc` never in a marketplace gallery.

Slots an LP2 prompt adds to the SKELETON above:
```
[TITLE]  the relief state, 2–5 words, in the offset space. -> LP2 LAW
[COPY]   only where earned.                         -> LP2 LAW
```

## TRIGGER
use_when: >
  The product solves a problem the buyer already feels but has not named. One
  image must prove wrong/right, show the product, and sell the relief state.
  Amazon A+ secondary images, landing-page banners, gallery images 2-3.
  Register: commercial for marketplace/LP polish, ugc for cold paid-social
  trust. Inset: vsinset when the argument is wrong-vs-right; recall when one
  reminder of the problem is enough; context when the hero shows the product in
  hand and the buyer still needs to see where it lives; none when the scene
  carries everything.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 06-relief-hero v1.15
REGISTER: commercial | ugc                                    -> PARTS/register

[PRODUCT REFERENCE] the attached photo is the exact reference,
  identical in every layer.
[SUBJECT] one person, full or reduced to hands and forearms.  -> PARTS/subject
[POSE] operated: mid-action. passive: relaxed, gaze away.     -> PARTS/pose
[SETTING] one real room, filled to the edges, never blank.    -> PARTS/setting
[LIGHT] set by whether an output has to carry.                -> PARTS/light
[OFFSET] subject to one side; a layer occupies that space.    -> PARTS/offset
[PRODUCT VIEW] only if the hero cannot show the product.      -> PARTS/product-view
[INSET] content by inset_mode, state by inset_motion.         -> VARIANTS-BY-AXIS

[MARKS]                                                       -> MARKS
  output   the hero, required if the product emits (G8)
  past     a recall inset, on the past cell
  step     a recall inset, one arrow, transition form only
  vs       a vsinset seam        hotspot  a vsinset left half
  path     a vsinset right half
```

## PARTS

**`register`** — `commercial` is a professional camera, controlled light, deliberate negative
space. `ugc` is a phone in an ordinary person's hand: slightly off exposure, mild overexposure
on skin and windows, no rim light, no negative space, framing casual and a little too close,
the room left exactly as it is. **This register buys trust, not beauty; do not clean it up.**

**`subject`** — choose ONE form. `full person`: age, gender, wardrobe toned to the background,
a pose from `pose`, a warm expression. `reduced`: present only as working hands, forearms or a
shoulder — no face, and so no expression available to carry the relief.

**`reduced` is a general form on both registers, not a rescue.** Choose it when the RESULT is
more legible than the user. A reduced subject with nothing finished in frame argues nothing, so
**name what makes finished look different from unfinished** and **tie what it is compared
against to the action** — described that way it read; merely listed, one run dropped it. The
persona, wardrobe and expression slots are then simply not exercised. Distinct from the `--ugc` fixed-installation fallback, whose trigger is distance
rather than legibility.

**`pose`** — if the user actively operates the product: mid-action, hands engaged, gaze on the
point of use, focused satisfaction rather than repose. If the product works passively while
the user does something else: relaxed, gaze away from the product.

**The pose must leave the product's contact point visible, and that constrains the pose before
anything else does.** Ask for a lower-back product on a body sunk into a sofa and the model
moves the product somewhere it can be seen. The passive branch is where this bites: relaxed
positions are the ones that put the body against furniture. Choose the pose from where the
product has to sit, not the reverse.

**Say where the person stands relative to the work.** A pressure washer given the jet and the
slabs but no working distance sprayed at its operator's own feet and soaked his trousers; one
sentence putting the whole jet between the person and the surface fixed it 2 of 2 on a steam
cleaner. Without it the wet-dry boundary replaces the clean-dirty one the frame exists to prove.

**`setting`** — one real room filled to the edges with 6-8 objects that genuinely belong there.
Background blurred but **never blank: no bare wall or floor area larger than the product**.
High-key neutral grade (G11).

**None of those objects may carry printed text.** Newspaper, packaging, letters, labelled boxes:
model-drawn text arrives as gibberish and this type bans text outright. Sheets of newspaper
named in a setting filled a large part of both runs with nonsense newsprint. Diegetic text on
the product itself is a separate question (G6 scope note); incidental props are not.

**`light`** — if `output` is present: backlight or hard side light, strong enough to make the
output glow against a darker part of the frame. Accept lens flare and blown highlights, they
read as real. Otherwise: soft even window light, background blurred, high-key.

**`offset`** — the subject sits to one side. **When a layer is present it OCCUPIES that offset
space.** Do not also reserve empty mid-frame; two reservations for one area render as dead air,
measured 2 of 2 on 2026-08-11. A layer takes 70-85% of the space the subject is offset from.
Page copy sits outside the image.

**`product-view`** — an optional bottom-left foreground layer, front z-layer, **included only if
the hero cannot show the product clearly** and skipped when it is held in hand, centred and
legible small. It exists to reveal the side the hero hides, so its angle MUST differ; a layer
repeating information costs space and buys nothing. 20-30% of frame width, studio light, soft
contact shadow, clean cutout. Real colorways only (G2).

## MARKS

**Six entries, counted off the 37 classified observations** and now carrying render results
too.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `output` | whatever the product emits — mist, spray, steam, foam, water, particles, light — made of the substance itself | the substance's own real colour | 1, in the hero | 6 obs, 0 against |
| `step` | one directional arrow joining the past cell to the resolved cell | neutral or a single flat colour | 1, transition form only | 7 obs; **2/2 rendered** when described by its two endpoints |
| `past` | the marking that flags a recall cell as the past: desaturation to grey, or a small X badge | grey, or red for the badge | 1, on the past cell only | 5 obs, 0 against |
| `path` | a translucent overlay following **a named physical feature** — a groove, a seam, a duct | blue or cyan | 1 | 4 obs, 4 against; 2/2 rendered on a named curve, but as a tint over the whole part |
| `vs` | a circular badge at the seam of a split inset, **carrying the letters VS** | red, white glyph | 1 | **2/2 rendered** once the glyph was named; blank disc before that |
| `hotspot` | glowing points on the wrong state, each on a named place | red | one per named place | 1 obs; **1/2 rendered** — anchoring cured an over-count and produced a zero |

**`output` is required whenever the product emits (G8) and outranks everything in the frame** —
not the person, not the product. Frame, light and expose for it; at least 15% of the frame,
readable at thumbnail size. **If the product emits nothing visible, do not invent an effect.**
It is the only entry here made of real substance rather than drawn, and the only one that has
never needed a rule: 4/4.

**`past` is what stops a recall inset inverting the message** — an unmarked past cell reads as a
result. Either form carries it; 2/2 rendered.

**`step` is the only sanctioned arrow in this type** and it exists solely to join a past cell to
a resolved one inside a recall inset. It never points from now to past, there is never more than
one, and it never appears in the hero. With 7 observations it is the best-evidenced mark here —
which is worth noticing, because until 1.9 the skeleton confined it to a sub-form of one variant
while mandating `vs` and `hotspot`, the two entries with one observation each.

**`vs` and `hotspot` are kept but thin.** One observation apiece is below the SPEC 6.2 bar and
neither would be promotable on this type's own evidence. `vs` is retained because the same
badge rendered 2 of 2 on `03-spec-split` without falling back to post-composite, and ADR-012
says a mark shared by two types is noted in both. `hotspot` is retained because A1 in
`registry/argument-faults.md` requires the wrong state to have somewhere to live, and the inset
is that somewhere — a hotspot there cannot read as harm the product causes. **Neither should be
mandated by a prompt that has not earned it.**

**`path` is contested at 4 for and 4 against** and is the entry most likely to be cut. Ship it
only where the mechanism genuinely has a path to trace.

**Pain exists ONLY inside the inset. The hero is 100% relief, never mixed.** No mark of any kind
appears in the hero except `output`.

**A drawn mark's stated COUNT does not survive; an anchored instance mostly does.** Two renders
that named a number both got it wrong. Anchoring instead — naming the two cells the one arrow
joins, naming the three places the points sit on — put `step` at 2/2 and `hotspot` at 1/2, the
miss being a zero rather than an excess. Anchor, and expect a mark still to be droppable.

**A badge returns empty unless its glyph is named** — asked for `a red circular badge` it comes
back a blank red disc, and 2/2 once the letters were named. Settled.

**A mark that follows something must be told what to follow.** Name the physical feature — this
groove, this seam, this duct — or the overlay lands as a highlighter stroke across everything.

## SLOT CONSTRAINTS
- **The prompt budget.** A clause earns its place only if a render has failed without it, and
  is removed only once a render has done without it and come back correct (ADR-013, ADR-015).
  Length costs composition: on single-layer `03-use-sequence` a 55% longer prompt took its
  layout from 4-in-6 to 1-in-4. This type is multi-layer, so that is a floor not a ceiling.
- **Never describe the frame's shape or ratio in a prompt.** The owner sets the ratio at render
  time (ADR-016); a prompt that reasons about frame geometry leaves the model something to
  reconcile and it fills the leftover with extra small panels.
- G10 (frame safety) binds every layer — safe area, bleed cap, shrink-never-move. Referenced by
  ID, never restated in a prompt.
- G7-X binds hard: one mode of use across hero, inset and product view. The humidifier ugc
  exemplar failed exactly this — wall-mounted inset, handheld hero.
- Pain exists ONLY inside the inset. The hero is 100% relief, never mixed.
- **The zone names never reach the model** — `HERO`, `INSET`, `ZONE A/B/C`, `LEFT`, `RIGHT`,
  `FIRST`, `SECOND` are this file's vocabulary, not the prompt's. Region labels are the tier
  that leaks; whole-image and subject labels do not (adapter Rule 1b, tiers set by ADR-017).
  Describe the region instead: "in the upper left corner sits a small rectangular panel".

## NEGATIVE
```
[G6] + cluttered background, dark moody lighting, pain cues in main scene,
blurry product, inconsistent product between layers, same angle repeated,
fabricated colorways, mixed illustration and photo inside one inset half,
invented spray or mist, fake steam
```

## VARIANTS-BY-AXIS
### register: --commercial (default)
Professional camera, controlled light, clean composition, deliberate negative space.
Channels: marketplace, landing-page, A+ content.

### register: --ugc
```
[REGISTER OVERRIDE] shot on a phone by an ordinary person.   -> PARTS/register
```

Channels: paid-social, advertorial header.
Negative additions: `professional lighting, studio setup, clean composition,
styled interior, negative space, color graded, retouched skin, magazine look,
glossy, symmetrical framing`
Fixed-installation caveat: at ugc distances an installed product may shrink below
recognition — reframe low-angle with the product + output as subject, person reduced
to a shoulder in frame.

### inset_mode: --vsinset
```
[INSET] top-left, white 3px border, split 50/50.       -> MARKS/vs at the seam
LEFT   the wrong state.                                -> MARKS/hotspot
RIGHT  the correct state, brighter and cleaner.        -> MARKS/path
Both halves share ONE register: both photographic, or both illustrated.
```
`hotspot` is the thin entry here and still unreliable at 1/2; see MARKS.


### inset_mode: --recall
```
[INSET] choose ONE form.
FORM 1  one cell, the problem state, 12-18% of frame width.   -> MARKS/past
FORM 2  the past cell, then the resolved cell, 15-22% total.  -> MARKS/past, step
Inset photos match the hero in resolution, grade and light quality.
```
A darker or lower-resolution inset reads as pasted in. Best-evidenced inset mode here: `step`
has 7 observations and `past` 5.

**The two cells change ONE thing: the product.** Hold the activity, the place and the person
constant and let the brace, the tool, the machine be the only difference. A pair that also
changes what the person is doing isolates nothing — a knee brace shown struggling on stairs and
then sitting on a sofa argues that the product lets you sit down. 2 of 2, and the fault was in
the prompt rather than in the render.

Negative additions: `unlabelled before-state inset, low resolution inset,
inset darker than hero, inset from a different photographic source,
more than one arrow, arrow pointing from now to past`

### inset_mode: --context
```
[INSET] rectangular, thin white border. A plain closer shot of the same product
in its real installed position, from a step back so the whole fitting is clear.
```
G7-X binds: installed in the inset while handheld in the hero contradicts itself.


### inset_mode: --detail
```
[INSET] rounded rectangle or circle, 30-40% of frame width, at a corner.
ONE magnified product detail the hero cannot show at scene scale.
Linked to the in-scene product by proximity: no arrows, no glow borders.
```
A screen or UI is never model-drawn (G12,
G6 scope note). An internal mechanism stays in a clean technical register inside the inset: internals bleeding
into the photographic hero break G5.

Use when the buying argument depends on a feature too small to read in scene
(memory log, measurement display, mechanism quality).

**The band was 15-25% until 1.18 and no render obeyed it.** The three `--detail` renders
measured 26%, 32% and 42% of frame width, and the ledger ranks them tightest-to-read,
slightly wide, and "by far the most legible … costs the picture nothing". The old ceiling
sat below the width already noted as tightest. 30-40% is also the only band that clears
G10's quarter-width floor, which a 15-25% panel cannot — a type may raise that floor and
may not lower it.

### inset_mode: --none
No inset layer at all. Use when the scene carries the whole argument.

### inset_motion: --still (default)
The layer is the finished picture; nothing is reserved.

### inset_motion: --loop
```
[INSET MOTION] the layer renders IN FULL; the loop replaces the slot.  -> G12
```
The render owes the layer a finished picture exactly as `--still` does: nothing is reserved or
left empty for a loop to land in, and the still ships on its own (ADR-051). What `--loop`
records is that the slot is ALSO commissioned as a motion asset — the editor is told which
slots those are by the app, and returns a loop replacing the whole slot at its own ratio. The
work order is the spec block in `prompts.md` plus the generated plate beside the still, so no
lettering enters the frame and G6 needs no exception here.

Legal on every `inset_mode` except `--none`, which has no layer to host it, and only where
the layer's content is TEMPORAL — a state changing, an output flowing, a mechanism
travelling. What the brief promises must be visible in the frame the layer sits on.

Four founding renders under the old plate rule, 1 pass and 3 partial; G12's geometry findings
carry over, the lettering ones do not.

## KNOWN-FLAKY
- **`hotspot` is 1 observation and 1 of 2 renders** — anchoring it to named places cured an
  over-count on one run and produced a zero on the other. It is kept because A1 requires the
  wrong state to have somewhere to live and the inset is that somewhere. `vs` is no longer
  flaky: 2/2 once its glyph was named.
- **`path` is contested, 4 observations for and 4 against.** The entry most likely to be cut.
- **Subject ABSENT entirely — variant candidate at 2/3, deliberately not in the skeleton.**
  Two observations show no person at all, the product carrying the hero zone: obs
  `sha256:61118d…` (10-H, purifier bottle on a marble poolside) and `sha256:c28dac…`
  (11-C, a campsite rigged drum-tight with the product's ropes). The first proposes it as
  a `--product` hero, so this is a VARIANT cluster rather than a slot patch, and at 2 it
  is below both the ≥3 bar and curate.md §3's variant bar. `reduced` (v1.8) is a different form and does not
  cover it: a steadying hand still puts a user in frame. A third distinct observation
  drafts `### --product`; until then no prompt should ship a person-free hero on this type.

## CHANGELOG
- 1.19 (2026-09-16): `LP2 LAW` added: the owner's gallery instruction for this type — its words, no inset in the bottom-right, a seated product seen whole, its place in the gallery. `text_layer` declared. First LP2 edit; `copied_at_version` stays 1.18. ADR-094.
- 1.18 (2026-09-15): copied verbatim from `registry/types/06-relief-hero.md` at 1.18, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.

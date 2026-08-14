---
id: 06-relief-hero
step: 6
job: relief
device: hero
version: "1.11"
status: active
replaced_by: null
ratios: ["16:9", "1:1"]
channels: [landing-page, marketplace, paid-social, advertorial]
requires_product_photo: true
generation_mode: single-pass
axes:
  register: [commercial, ugc]
  inset_mode: [vsinset, recall, context, detail, none]
variants: []
exempt_from: []
pairs_with: [01-pain-split, 01-pain-scene]
never_with: []
---

# 06-relief-hero

## PURPOSE
Sell the state after buying, with the product in frame. Configured on two independent
axes — `register` (commercial | ugc) and `inset_mode` (vsinset | recall | context |
detail | none) — named `06-relief-hero--{register}--{inset_mode}`.

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
avoid_when: >
  The product has no visible "wrong state" (use 03-mechanism-ghostbody for
  internal mechanisms). ugc register never on marketplace galleries.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 06-relief-hero v1.11
REGISTER: commercial | ugc                                    -> PARTS/register

[PRODUCT REFERENCE] the attached photo is the exact reference,
  identical in every layer.
[SUBJECT] one person, full or reduced to hands and forearms.  -> PARTS/subject
[POSE] operated: mid-action. passive: relaxed, gaze away.     -> PARTS/pose
[SETTING] one real room, filled to the edges, never blank.    -> PARTS/setting
[LIGHT] set by whether an output has to carry.                -> PARTS/light
[OFFSET] subject to one side; a layer occupies that space.    -> PARTS/offset
[PRODUCT VIEW] only if the hero cannot show the product.      -> PARTS/product-view
[INSET] content set by inset_mode.                            -> VARIANTS-BY-AXIS

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
more legible than the user: the product's output, a finished surface, a loaded container. A
reduced subject with nothing finished in frame argues nothing, and its first render proved the
rule needs an operational half: **name what makes finished look different from unfinished**, or
the result is in the prompt and absent from the photograph. When
`reduced` is chosen the persona,
wardrobe and expression slots are simply not exercised — do not fill them with a face that is
not in shot. Distinct from the `--ugc` fixed-installation fallback, whose trigger is distance
rather than legibility.

**`pose`** — if the user actively operates the product: mid-action, hands engaged, gaze on the
point of use, focused satisfaction rather than repose. If the product works passively while
the user does something else: relaxed, gaze away from the product.

**The pose must leave the product's contact point visible, and that constrains the pose before
anything else does.** Ask for a lower-back product on a body sunk into a sofa and the model
moves the product somewhere it can be seen. The passive branch is where this bites: relaxed
positions are the ones that put the body against furniture. Choose the pose from where the
product has to sit, not the reverse.

**`setting`** — one real room filled to the edges with 6-8 objects that genuinely belong there.
Background blurred but **never blank: no bare wall or floor area larger than the product**.
High-key neutral grade (G11).

**`light`** — if `output` is present: backlight or hard side light, strong enough to make the
output glow against a darker part of the frame. Accept lens flare and blown highlights, they
read as real. Otherwise: soft even window light, background blurred, high-key.

**`offset`** — the subject sits to one side. **When a layer is present it OCCUPIES that offset
space.** Do not also reserve empty mid-frame; two reservations for one area render as dead air,
measured 2 of 2 on 2026-08-11. A layer takes 70-85% of the space the subject is offset from.
Page copy sits outside the image.

**`product-view`** — the optional bottom-left foreground layer, front z-layer. **Include it only
if the hero scene cannot show the product clearly**, and skip it entirely when the product is
held in hand, centred and legible at thumbnail size. It exists to reveal the side the hero
hides, so its angle MUST differ from the hero's; a layer repeating information costs frame
space and buys nothing. 20-30% of frame width, studio light, soft contact shadow, razor sharp,
clean cutout. Real colorways only (G2): two units if the product genuinely has two, otherwise
one.

## MARKS

**Six entries. The counts are of the 37 classified observations of this type**, read for
whether the mark was seen rather than merely mentioned.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `output` | whatever the product emits — mist, spray, steam, foam, water, particles, light — made of the substance itself | the substance's own real colour | 1, in the hero | 6 obs, 0 against |
| `step` | one directional arrow joining the past cell to the resolved cell | neutral or a single flat colour | 1, transition form only | 7 obs, 2 against |
| `past` | the marking that flags a recall cell as the past: desaturation to grey, or a small X badge | grey, or red for the badge | 1, on the past cell only | 5 obs, 0 against |
| `path` | a translucent overlay following **a named physical feature** — a groove, a seam, a duct — where the mechanism acts | blue or cyan | 1 | 4 obs, 4 against — contested |
| `vs` | a circular badge at the seam of a split inset, **carrying the letters VS** | red, white glyph | 1 | 1 obs here; 2/2 on `03-spec-split`, which names its glyph |
| `hotspot` | glowing points on the wrong state | red | 3 | **1 obs** |

**`output` is required whenever the product emits (G8), and it outranks everything.** If the
product produces anything visible, that output is the PRIMARY subject of the frame — not the
person and not the product. Frame, light and expose for it; it occupies at least 15% of the
frame and reads at thumbnail size. **If the product produces nothing visible, do not invent an
effect.** Three exemplars in a row proved a badly-shot frame with visible mist beats a clean
frame without it. It is also the only mark here made of real substance rather than drawn, which
is the class that renders most reliably in a photographic register.

**`past` is what stops a recall inset inverting the message.** An unmarked past cell reads as a
result. Either form carries it; the observations show both and neither has a case against it.

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

**A drawn mark renders, but its stated COUNT does not survive** — 2 of the 2 renders that named
one got it wrong. Where the count carries meaning, give each instance its own anchor: name the
three places, name the two cells the one arrow joins, so the count follows from the description
instead of being an instruction to obey.

**A badge returns empty unless its glyph is named.** Asked for `a red circular badge` it comes
back a blank red disc. `vs` names its letters in the prompt, as `03-spec-split` does.

**A mark that follows something must be told what to follow.** Name the physical feature — this
groove, this seam, this duct — or the overlay lands as a highlighter stroke across everything.

## SLOT CONSTRAINTS
- **The prompt budget.** A clause earns its place only if a render has failed without it, and
  is removed only once a render has done without it and come back correct (ADR-013, ADR-015).
  Measured on `03-use-sequence`, whose prompts are single-layer and so a floor rather than a
  ceiling for this one: 1533 characters average held its layout 4 times in 6, and 2368 held it
  1 in 4. This type carries more layers and will run longer, but length is a cost that buys
  something and every added clause is paid for out of composition.
- **Never describe the frame's shape or ratio in a prompt.** The owner sets the ratio at render
  time (ADR-016); a prompt that reasons about frame geometry leaves the model something to
  reconcile and it fills the leftover with extra small panels.
- G10 (frame safety) binds every layer — safe area, bleed cap, shrink-never-move. Referenced by
  ID, never restated in a prompt.
- G7-X binds hard: one mode of use across hero, inset and product view. The humidifier ugc
  exemplar failed exactly this — wall-mounted inset, handheld hero.
- Pain exists ONLY inside the inset. The hero is 100% relief, never mixed.
- **The zone names never reach the model.** `HERO`, `INSET`, `ZONE A/B/C`, `LEFT`, `RIGHT`,
  `FIRST`, `SECOND` are this file's vocabulary. Adapter Rule 1b is measured on three types: a
  name attached to a REGION of the frame gets printed into that region, while whole-image
  headings — `REGISTER`, `PRODUCT REFERENCE`, `LIGHT` — shipped alongside every one of those
  leaks and were never drawn. The 1.8 skeleton carried `[ZONE A: HERO, right 60%]` and
  `LEFT:` / `RIGHT:` verbatim, which is the exact shape that printed `ZONE A/B/C` into a
  02-symptom-rail frame. Describe instead: "in the upper left corner sits a small rectangular
  panel with a thin white border", "the half on the left". The first draft of the 1.9 prompt
  set reproduced the fault in 10 places before a gate caught it.

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
Thin on this type's own evidence — `vs` and `hotspot` have one observation each. Do not mandate
either in a prompt that has not earned it; see MARKS.


### inset_mode: --recall
```
[INSET] choose ONE form.
FORM 1  one cell, the problem state, 12-18% of frame width.   -> MARKS/past
FORM 2  the past cell, then the resolved cell, 15-22% total.  -> MARKS/past, step
Inset photos match the hero in resolution, grade and light quality.
```
A darker or lower-resolution inset reads as pasted in. Best-evidenced inset mode here: `step`
has 7 observations and `past` 5.

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
[INSET] rounded rectangle or circle, 15-25% of frame width, at a corner.
ONE magnified product detail the hero cannot show at scene scale.
Linked to the in-scene product by proximity: no arrows, no glow borders.
```
Use when the buying argument depends on a feature too small to read in scene. If the detail is
a screen or UI it is **never model-drawn** — render or photograph the real interface and
composite it in post; model-drawn digits come back as gibberish, and screen digits are diegetic
product UI rather than overlay copy (G6 scope note). If it is an internal mechanism, keep the
cutaway in a clean technical register and confine it to the inset: internals bleeding into the
photographic hero break G5.

Use when the buying argument depends on a feature too small to read in scene
(memory log, measurement display, mechanism quality).

### inset_mode: --none
No Zone C. Use when the scene carries the whole argument.

## WORKED EXAMPLES
### example: shower-filter-commercial-vsinset — skeleton@1.1, run: untested
Product: metal shower filter · ratio 2:1 · axes: register=commercial, inset_mode=vsinset
- ZONE A — woman late 20s, long dark hair, under a running shower, head tilted back, eyes closed, calm satisfied, water streaming over her shoulders; the filter installed above her between hose and showerhead, low three-quarter angle, unobstructed
- SETTING — bright modern bathroom filled to the edges: white marble tile, glass partition, eucalyptus bundle, frosted window; background blurred, high-key white and warm grey, steam catching the light; subject offset right, the inset occupying the offset space
- ZONE B — the same filter top-down looking into the inlet, floating, about 25% of frame width, studio light, soft contact shadow, razor sharp, clean cutout; one unit only
- ZONE C (top-left, white 3px border, split 50/50, red circular VS badge at the seam) — LEFT: desaturated grayscale macro of a nozzle plate caked with white limescale, dull uneven dripping, red hotspots at three clogged nozzles. RIGHT: full-color macro of a clean plate spraying clear even jets, cyan translucent overlay tracing the water path. Both halves photographic, right brighter and cleaner
Predicted failure: Zone C right half slipping into 2D illustration against the photo
macro (register mismatch inside the inset).

### example: shower-filter-ugc-context — skeleton@1.3, run: untested
Product: metal shower filter · ratio 2:1 · axes: register=ugc, inset_mode=context
- ZONE A — man early 40s standing in his own bathroom, eyes closed, face tilted up under the running shower, water hitting his shoulders, unguarded relaxed expression; the reference filter fitted above him between arm and shower head, clearly visible in the upper frame; installed in every layer, never handheld
- VISIBLE MECHANISM — the spray is the primary subject: dense individual streams and fine mist backlit by a window behind him, filling a large part of the frame and readable at small size
- REGISTER OVERRIDE — shot on a phone: slightly overexposed on tiles and window, no rim light, no negative space, framing casual and a little too close, tilted a few degrees; the bathroom left as it is — shampoo bottles crowded on the corner shelf, a razor on the ledge, towels bunched on the rail, water spots on the glass
- ZONE C (top-left, rectangular, thin white border) — a plain closer shot of the same filter installed on the same shower arm, taken a step back so the whole fitting is clear; same mode of use, same room, same daylight
Predicted failure: distance — an installed filter high in frame may render at
unrecognizable size; fallback framing is low-angle, filter + water jet as subject,
person reduced to a shoulder.

## KNOWN-FLAKY
- **`vs` and `hotspot` sit on one observation each**, below the SPEC 6.2 bar, and both are
  mandated by the `--vsinset` block. `vs` is carried on borrowed evidence from `03-spec-split`
  (2/2 rendered, no post-composite fallback); `hotspot` is carried because A1 requires the wrong
  state to have somewhere to live. Neither has been rendered on this type. A `--vsinset` render
  is the cheapest way to settle both.
- **`path` is contested, 4 observations for and 4 against.** The entry most likely to be cut.
- **Subject ABSENT entirely — variant candidate at 2/3, deliberately not in the skeleton.**
  Two observations show no person at all, the product in its finished situation carrying
  the hero zone: obs `sha256:61118d…` (batch 10-H, purifier bottle posed on a marble
  poolside) and `sha256:c28dac…` (batch 11-C, a campsite rigged drum-tight with the
  product's ropes). The first record proposes it as a `--product` hero decision, so this
  is a VARIANT cluster, not a slot patch — and at 2 observations it is below both the ≥3
  bar and curate.md §3's variant bar. `reduced` (v1.8) is a different form and does not
  cover it: a steadying hand still puts a user in frame. A third distinct observation
  drafts `### --product`; until then no prompt should ship a person-free hero on this type.

## CHANGELOG
- 1.11 (2026-08-14): first four renders, 0 pass. A drawn mark's stated COUNT does not survive
  (2/2 runs that named one), a badge returns empty unless its glyph is named, and `path` needs a
  named physical feature to follow. `pose` gains the constraint that it must leave the contact
  point visible — asking for a lower-back product on a man sunk into a sofa put the massager on
  his abdomen. `reduced` gains its operational half: name what makes finished look different.
  `output` needed nothing and was the one unqualified success. `2df3c2f`
- 1.10 (2026-08-14): SLOT CONSTRAINTS gains adapter Rule 1b — the zone names never reach the
  model. The 1.8 skeleton shipped `[ZONE A: HERO]` and `LEFT:` as headings, the shape measured
  printing `ZONE A/B/C` into an 02-symptom-rail frame. Whole-image headings are unaffected. `42b2dea`
- 1.9 (2026-08-14): restructured into a call-map plus PARTS and MARKS (ADR-012); skeleton
  3398 → 1229. First MARKS library, counted off the 37 observations rather than off the
  skeleton: `step` 7, `output` 6, `past` 5, `path` 4-for-4-against, `vs` and `hotspot` 1 each —
  so the skeleton had mandated the two thinnest and confined the strongest to a sub-form.
  `ratios` move to ADR-016: 5:3 and 2:1 become `16:9`, `1:1` kept on 5 observations. `RATIO:`
  dropped (adapter Rule 4); the skeleton header had read v1.3 against a 1.8 file. `28b384d`
- 1.8 (2026-08-12): `[ZONE A]` gains an explicit SUBJECT form choice — `full person` or
  `reduced` (hands, forearms or a shoulder, no face), with the guardrail that a reduced
  subject requires a visible output or finished state to carry what the expression would
  have carried. Evidence: 3 distinct observations, all on this type — obs
  `sha256:5ea857…` (batch 10-F, hands and forearms working the tool, action-crop),
  `sha256:2a8cda…` (11-A, person reduced to a steadying hand, persona/wardrobe/pose
  slots unexercised), `sha256:d186f6…` (11-A, a presenting hand tilting the loaded
  bowl). The skeleton had mandated `[age/gender] … [warm expression]` outright, so every
  one of these read as a violation of a slot the market simply does not fill that way.
  The person-ABSENT form is a separate decision at 2/3 and went to KNOWN-FLAKY, not
  here. Also: the Zone A grade line now cites G11 by ID rather than carrying the law as
  loose wording (G8/G9 precedent, ADR-003; the rule itself is ADR-010).
- 1.7 (2026-08-11): channels gain `advertorial`. Proved by a sibling: 06-relief-scene's
  avoid_when says that for invisible results "the closing image must be 06-relief-hero
  with the product in frame" — and relief-scene lives on advertorial, so relief-hero
  had to be legal there for its own escape hatch to exist. Two real advertorial pages
  demanded it independently.
- 1.6 (2026-08-11): Setting slot rewritten for density (6-8 objects, no bare area
  larger than the product) and the headline reservation removed when a layer is
  present — the offset space belongs to the layer. G10 (frame safety) adopted by
  reference. Evidence: render tests 2026-08-11, wet-dry floor washer and travel
  stroller — 2/2 runs returned a dead mid-frame with `Subject offset right, empty
  mid-frame for headline` combined with a corner layer, and 2/2 bleeding-shape runs
  cropped their content. Both faults are compositional, not product-specific.
- 1.5 (2026-08-10): --recall gains the transition-pair execution form (past-cell
  marked + one arrow + now-cell). Evidence: 3 observations across 3 domains — obs
  sha256:cd8e0e…, sha256:5ea857…, sha256:61118d… (batches D, F, H).
- 1.4 (2026-08-10): inset_mode value `detail` added (magnified product detail: UI
  screen or internal mechanism; composite screens in post, never model-drawn).
  Evidence: 3 observations across 2 domains — obs sha256:b63e19…, sha256:611850…,
  sha256:d51192… (batches D-E). Vocabulary axis updated in the same change.
- 1.3 (2026-08-10): register axis (commercial/ugc) and inset_mode axis
  (vsinset/recall/context/none) separated; VISIBLE MECHANISM promoted to required
  (→G8); G7-X cross-layer rule adopted. Evidence: humidifier ugc exemplar (stronger
  proof despite worse photography; mounted-vs-handheld contradiction).
  seed: conversation.md.
- 1.2 (2026-08-10): Zone B made conditional; visible-mechanism and pose/light
  conditionals added. Evidence: spray-brush exemplar outperformed the 3-layer original
  on argument and thumbnail legibility. seed: conversation.md.
- 1.1 (2026-08-10): Zone B rebuilt as complementary view (real colorways only, must
  reveal a hidden side); G1 block added. seed: conversation.md.
- 1.0 (2026-08-10): initial as BNR-RELIEF-VSINSET from the S-cushion office exemplar.
  seed: conversation.md.

---
id: 01-pain-split
step: 1
job: pain
device: split
version: "1.9"
status: active
replaced_by: null
ratios: ["1:1"]
channels: [marketplace, landing-page]
requires_product_photo: true
generation_mode: single-pass
variants: [object, mirror, oldway]
exempt_from: []
pairs_with: [06-relief-hero]
never_with: [01-pain-scene]
---

# 01-pain-split

## PURPOSE
Stop the scroll with pain in a 0.5-second glance. Structurally this is a **before and
after**: the same situation wrong on the left, resolved on the right, judged by badges.
Image 2 on Amazon, ad thumbnails, tiles in a landing-page grid.

## TRIGGER
use_when: >
  Need to stop the scroll with pain, or occupy one tile in a gallery/grid where
  the viewer glances for half a second. Use when the wrong state is visible to
  the naked eye. Use --object when the product is the obvious answer (small
  frames, thumbnails); use --mirror when the problem is a body state and the
  change must be shown on the person.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once.

```
TYPE: 01-pain-split v1.8 [--object | --mirror | --oldway]

[LAYOUT] two panels, hard vertical 50/50, both running to the frame edge.
                                                              -> PARTS/layout
[PRODUCT REFERENCE] attached photo is the exact reference.
[BEFORE] left panel: the wrong state, desaturated.            -> PARTS/before
[AFTER] right panel: the SAME setting resolved, in colour.    -> PARTS/after
[PRODUCT] in the AFTER panel only.                            -> PARTS/product
[MARKS] verdict always; hotspot + jag on the BEFORE panel.    -> MARKS

STYLE: e-commerce comparison tile, high contrast, sharp. Both panels share one
lighting register and one shooting style (G5).
```

## PARTS

**`layout`** — two panels, a hard vertical split at 50/50, each panel running all the way to
the frame edge. **No outer border and no drawn border line.** Assert it positively and say the
prohibition once: this model does not render a border as a margin, it draws a thin white
rectangle INSET from the edges, floating over the photograph and cutting through whatever is
behind it. 3 of 3 renders, one per variant. The split line itself is the argument's divider
and has rendered correctly every time.

**`before`** — left panel, desaturated grayscale: [age/gender] in [wardrobe], [the wrong
posture, state or struggle] on [surface], face showing [the discomfort, named by muscle].
Neutral cropped background, subject fills the frame.

**`after`** — right panel, full colour: **the SAME situation resolved.** Same room, same
surface, and the same person wherever a person is in frame.

**The AFTER keeps the room, and this is the type's most-lost rule.** The slots used to be
called THE PROBLEM and THE ANSWER, and "answer" is what invited a product photo — a product on
a clean ground answers the question without being an after of anything. One render proved it:
the right panel came back as an isolated shirt on a bare white wall against a lived-in left
panel, which breaks G5 and drops the comparison. G4 still binds — brighter and airier than the
left — but by light and calm, **never by deleting the room**.

**`product`** — ONE unit, in the AFTER panel only, in use, placed per G2: position, angle, scale in frame,
relation to other objects. Never described. It keeps its own reference colours and **carries
no signal colour at all** (`argument-faults.md` A5).

## MARKS

This type's own mark library. Every mark obeys G3 and carries a count.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `verdict` | flat solid disc with the glyph cut out of it, in a TOP corner, both the same diameter | red X left, green check right | exactly 2 | 4 renders · also in `02-cause-anatomy`, `03-mechanism-ghostbody`, `06-relief-hero` |
| `hotspot` | a soft red radial glow on one named structure | red only | one per structure, BEFORE panel only | 4 renders · a glow blooms and cannot be held to a boundary |
| `jag` | short red jagged strokes running ALONG one named structure | red only | 1 structure, BEFORE panel only | 4 renders |

**Name the SIDE as well as the structure.** Naming a structure binds the structure; on a
symmetric body it does not bind the side, and one render put every mark on both arms. Say
"the near wrist" and then say the marks appear on that arm only.

**Name structures, not counts.** "Exactly 3 hotspots" does not bind — a restated number never
has, in this library or in `02-cause-anatomy`. Name the three structures the glows sit on and
the count follows: wrist, forearm, shoulder. This also gives each glow something bounded to
sit on, which is the only thing that governs a mark's extent.

**All marks live in the BEFORE panel.** A mark in the AFTER panel sits in a frame where the
product is working, so it reads as harm the product CAUSES (`argument-faults.md` A1). The
badges are the single exception, because a verdict is not a harm.

**Badges: TOP corners only.** The eye reads top-down; a bottom badge arrives after the verdict
is already formed. Never add a VS badge on top of the X/check pair — one binary argument, one
pair of markers. Source exemplars used VS badges and emoji; market habits, deliberately not
imported.

## SLOT CONSTRAINTS
- **The wrong state must be visible to the naked eye.** This type argues in half a second; a
  problem that needs explaining belongs in `02-cause-anatomy` or `03-mechanism-*`.
- **A comparison must be of a switchable state** (`argument-faults.md` A6): take the product
  away and the wrong state must come back. If the harm persists it is accumulated damage, and
  the AFTER panel claims a repair the product cannot perform.
- Both panels share ONE register (G5): same lighting character, same shooting style. The
  register break is this type's recorded failure mode, always in the same direction — the
  right panel drifting to catalogue lighting the moment it holds a product and nothing else.
- **The prompt budget.** A clause earns its place only if a render has failed without it.
  Since ADR-014 no `Strictly avoid:` line is rendered at all.

## NEGATIVE
```
[G6] + cluttered background on right panel, dim right panel,
mismatched photo style between panels, visible test rigs or props,
red cues on right panel, distorted face, blood, injury,
inset white rectangle, drawn border line
```
Canonical and model-agnostic. Since ADR-014 it is **not rendered into the prompt at all**;
it stays here and in the query output's `avoid` field for a future model with a real negative
channel. `inset white rectangle` and `drawn border line` are kept in the list despite the
skeleton asserting the positive form, because a bordered comparison tile is a strong market
prior and it is this type's only 3/3 failure.

## VARIANTS
Diffs only. Each variant names the PARTS and MARKS it changes.

### --object (default)
The BEFORE is a person with the symptom; the AFTER is the same person and the same room with
the product doing its job. Baseline `before`, `after`, `product` and all three marks.
This is where the same-setting rule is easiest to lose, because the product is the most
interesting thing in the AFTER panel and the model will happily give it a studio.

### --mirror
The strongest comparison form — same person, same shot, only the state changes.
Diff vs base: `after` additionally holds the SAME camera angle, distance, wardrobe and
framing, and only posture, expression, presence of the product and colour grade may differ ·
`hotspot` and `jag` are DROPPED, posture and expression carry the problem · lighting setup and
time of day are identical, only the grade differs.
- **The route is an INVARIANTS BLOCK, single-pass** (ADR-067). Name face, hair, beard,
  clothes, camera height, distance and framing ONCE, BEFORE either panel is described. A
  single pass has been tried both ways: describing the person inside each panel returned two
  different people, and the invariants block returned one, 1 of 1 each way. This variant used
  to declare a `multi-pass` override on top of that finding; it is gone, and the worked
  example below — `wrist-brace-mirror`, `run: pass` — is a single-pass render where the
  identity held. The block is not a formality: without it this variant does not work.
- Negative additions: `different person between panels, different camera angle between panels,
  different wardrobe, different time of day, golden hour on one side only, VS badge, third
  badge, badges at bottom of frame`

### --oldway
The wrong state is the OLD SOLUTION IN USE — a person struggling with the legacy product class
— instead of a symptom on a body. Use when the buyer's real pain is the friction of what they
already own.
Diff vs base: `before` becomes a person struggling with a GENERIC, UNBRANDED legacy device,
ordinary and plausible, never broken, dirty or mocked (the fairness logic of
`04-proof-lockedframe`), with 2-3 friction details · `hotspot` and `jag` are optional, since
the friction is the evidence · the same-setting rule binds hardest here, because the BEFORE
panel is a room with a person struggling in it.
- Never imply the legacy device is a specific competitor.
- Negative additions: `brand logos on the legacy device, damaged or mocked legacy device,
  emoji, money props, price-claim imagery`

## WORKED EXAMPLES
Both rendered at 1.7 and owner-passed, kept in FULL text per SPEC §3.3.

### example: lumbar-cushion-mirror — skeleton@1.7, run: pass
```
TYPE: 01-pain-split v1.7 --mirror

[LAYOUT]
Two panels side by side, hard vertical split at exactly 50/50. Each panel runs all the
way to the frame edge. No outer border and no drawn border line anywhere in the image.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the product.
Preserve its shape, proportions, material, finish and color exactly as shown.
Do not redesign, restyle, simplify or add features.
Render it from the same side-on angle as the scene, at roughly a quarter of the right
panel's height, integrated with the scene lighting.

[THE SAME PERSON IN BOTH PANELS]
One man, mid 40s, short dark hair cut close at the sides, a trimmed beard, a plain
charcoal sweatshirt and dark jeans. He is identical in both panels: same face, same hair
length, same beard, same clothes, same body. Both panels are shot from the same side-on
camera at the same distance and the same height, framing him from the knees up on the same
grey two-seat sofa in the same room, with the same lamp and the same window behind him.

[BEFORE — left panel]
Desaturated grayscale. He is slumped back into the sofa with his lower back hollow and
unsupported, the pelvis slid forward, the spine curved into a long C and the head carried
in front of his shoulders. Face: mouth set, brow drawn.

[AFTER — right panel]
Full colour. The SAME man, same sofa, same camera, same clothes, sitting upright with the
lower back filled and the pelvis under him, the spine long, the head over his shoulders.
Face relaxed. The reference lumbar cushion is between his lower back and the sofa back,
secondary to him. Same lighting setup and the same time of day as the left panel — only
the posture, the expression, the cushion and the colour grade differ.

[MARKS]
No glows and no jagged marks in either panel: the posture carries the problem.

[BADGES]
A flat solid red disc with a white X cut out of it in the TOP-LEFT corner of the left
panel. A flat solid green disc with a white check cut out of it in the TOP-RIGHT corner of
the right panel. Same diameter, no other badge.

STYLE: e-commerce comparison tile, high contrast, sharp. Both panels share one lighting
register and one shooting style.
```
Rendered in a SINGLE pass and the identity held. The invariants block before the panels is
what this example exists to preserve.

### example: spin-mop-oldway — skeleton@1.7, run: pass
```
TYPE: 01-pain-split v1.7 --oldway

[LAYOUT]
Two panels side by side, hard vertical split at exactly 50/50. Each panel runs all the
way to the frame edge. No outer border and no drawn border line anywhere in the image.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the product.
Preserve its shape, proportions, material, finish and color exactly as shown.
Do not redesign, restyle, simplify or add features.
Render it from a front three-quarter angle at roughly a third of the right panel's height,
integrated with the scene lighting.

[BEFORE — left panel]
Desaturated grayscale. Man early 50s in an old t-shirt with the sleeves pushed up,
crouched on a kitchen floor wringing out a plain grey string mop head with both bare
hands over an ordinary plastic bucket: grey water running back off his forearms, the mop
head twisted and dripping, a wet trail and splashes spread across the tiles around the
bucket. The bucket and mop are generic and unbranded, ordinary and in good condition.
Face: mouth pressed flat, brow drawn in.

[AFTER — right panel]
Full colour. The SAME kitchen — same tiles, same units, same window, same man — now
standing upright, one hand on the handle, pressing the reference spin mop down into its
own wringer basket. The floor behind him is finished and dry, his hands and forearms are
dry. Brighter and airier than the left panel by light and by calm; the kitchen stays
exactly where it is and nothing is removed from it.

[MARKS]
No glows and no jagged marks: the friction on the left carries the problem.

[BADGES]
A flat solid red disc with a white X cut out of it in the TOP-LEFT corner of the left
panel. A flat solid green disc with a white check cut out of it in the TOP-RIGHT corner of
the right panel. Same diameter, no other badge.

STYLE: e-commerce comparison tile, high contrast, sharp. Both panels share one lighting
register and one shooting style.
```
The same-setting rule on the variant that invites breaking it: same kitchen, same man, only
the job and the grade change.

## KNOWN-FLAKY
- **The product rendered TWICE in the AFTER panel, 1 of 1, 2026-08-13.** Once in use as
  placed, and again as a second unit lying alone in the foreground under packshot light. Same
  instinct as the register split below — the model reaches for a catalogue shot the moment
  the right panel holds a product — but here it ADDS one instead of replacing the room.
  `PARTS/product` now says ONE unit, in use.
- **Identity breaks across panels when the person is described INSIDE each panel**, 1 of 1,
  2026-08-12. Hair dark and long on the left, lighter and shorter on the right — two people,
  so no comparison. That render is what the invariants block exists to prevent, and the
  worked example is the positive control at 1 of 1. Two renders, opposite results, one
  variable: where the identity is stated matters more than how many passes are used.
- **Register split between panels on `--oldway`, 1/3 renders, 2026-08-12 — addressed at
  v1.6, watch for recurrence.** The garment steamer run put a lived-in room on the left and
  what reads as a studio packshot on the right: an isolated shirt on a plain white wall, no
  room around it. G5 and the base NEGATIVE already barred it, so no law was missing; the
  model reached for catalogue lighting the moment the right panel held a product and
  nothing else. At one observation this sat below the §6.2 threshold and the skeleton was
  left alone. v1.6 then patched it anyway, for a different reason — the owner's naming
  decision required the AFTER panel to keep the setting — so this render is corroboration
  rather than the trigger. If a packshot right panel appears again under v1.6, the
  same-setting rule is not strong enough and the next step is to require the left panel's
  room to be named a second time inside the AFTER slot.

## CHANGELOG
- 1.9 (2026-09-03): `--mirror`'s `generation_mode override: multi-pass` is **removed**
  (ADR-067, owner instruction). The invariants block was already the recorded alternative,
  already the only route open to this operator since ADR-021, and already carried a `pass`
  worked example rendered in one pass. The override contradicted the type's own evidence.
  KNOWN-FLAKY reworded: the 2026-08-12 identity break is about WHERE the person is described,
  not about pass count. `ratios` corrected to ADR-016's legal set: `4:5` dropped, unaskable
  since 2026-08-13, which leaves the one ratio this type has actually rendered at.
- 1.8 (2026-08-13): **type PASSED by the owner; file finalised.** Three renders, one per
  variant: `--mirror` and `--oldway` pass, `--object` partial. WORKED EXAMPLES returns with
  the two passes in full text. Two findings patched: naming a structure does not bind the
  SIDE on a symmetric body, and `product` is ONE unit in use — a render placed a second one
  beside it as a packshot. `--mirror`'s multi-pass declaration now records the single-pass
  alternative that worked, an explicit invariants block, which is the only route open to a
  renderer who does not composite. · this commit
- 1.7 (2026-08-13): **restructured into a call-map plus two libraries** (ADR-012), owner
  instruction. `PARTS` owns `layout`, `before`, `after`, `product`; `MARKS` owns `verdict`,
  `hotspot`, `jag`. Three laws carried in from `01-pain-scene` and `argument-faults.md`: name
  the STRUCTURES a glow sits on rather than a count; every mark stays in the BEFORE panel (A1);
  the product carries no signal colour (A5). ADR-014 adopted. WORKED EXAMPLES removed, both
  untested and predating this shape. · this commit
- 1.6 (2026-08-12): **the panels are renamed BEFORE and AFTER, and the AFTER keeps the room.**
  Owner naming decision; "THE ANSWER" was inviting a product photo, and one render had already
  come back with an isolated shirt on a bare wall against a lived-in left panel. G4 narrowed:
  brighter by light and calm, never by deleting the room. The type id does not change —
  `{step}-{job}-{device}` records where an image sits in the funnel, not what is in every
  pixel. · 4af89f6
- 1.5 (2026-08-12): **the outer border leaves the render**, 3 of 3, one per variant — this
  model draws it as a white rectangle inset from the edges, cutting through the photograph.
  The line now asserts the positive and names the prohibition once. `RATIO:` dropped in the
  same block per adapter Rule 4. · 9d060dd
- 1.4 (2026-08-11): channels gain `landing-page`. use_when already scopes the type to
  "one tile in a gallery/grid where the viewer glances for half a second", which a
  landing-page grid is; nothing in avoid_when was channel-specific. The routing table
  had listed it on landing-page all along — this reconciles the two.
- 1.3 (2026-08-10): --oldway variant added (wrong side = legacy solution in use).
  Evidence: 4 observations across 2 domains — obs sha256:0b0260…, sha256:3b4499…,
  sha256:f53928…, sha256:9ae982… (batches D-E). Market badge habits (VS, emoji,
  money props) observed and explicitly excluded.
- 1.2 (2026-08-10): --mirror variant added (same person, state-only change; multi-pass);
  badge law tightened (top corners, no VS). Evidence: seed conversation.md
  (driver-seat mirror exemplar).
- 1.1 (2026-08-10): [PRODUCT REFERENCE] block added (G1); right panel rewritten to G2
  (no invented product details). seed: conversation.md.
- 1.0 (2026-08-10): initial as SQR-PAIN-XCHECK, from the neck-pain vs pink-cushion
  exemplar; register-mismatch and dim-right-panel faults of the exemplar encoded as
  negatives. seed: conversation.md.

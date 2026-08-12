---
id: 01-pain-split
step: 1
job: pain
device: split
version: "1.6"
status: active
replaced_by: null
ratios: ["1:1", "4:5"]
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
avoid_when: >
  Main image, or any position that needs goodwill before pain. Not when the
  problem is invisible or the "wrong" scene cannot be photographed. Never in the
  same set as 01-pain-scene.

## SKELETON
```
TYPE: 01-pain-split v1.6 [--object | --mirror | --oldway]
LAYERS: 2 panels, hard vertical split 50/50. Each panel runs all the way to the
frame edge. No outer border, no drawn border line anywhere in the image.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly. Do not redesign or add features.

[LEFT PANEL: BEFORE]
Desaturated grayscale photo of [age/gender] in [wardrobe],
[wrong posture/behavior] on [surface], face showing [discomfort expression].
Glowing red hotspots at [3 points], soft red radial glow,
[red jagged marks] along [affected structure].
Neutral cropped background, subject fills frame.

[RIGHT PANEL: AFTER]
The SAME situation resolved — same room, same surface, and the same person
wherever a person is in frame. Full-colour, with the reference product
[in place / in use] in that same [context], seen from [angle], occupying [X%]
of the panel.
Brighter and airier than the left panel (G4): cleaner by light and by calm,
never cleaner by deleting the room. If the setting disappears, this stops being
an AFTER and becomes a product photo.

[BADGES]
Red circle with white X, top-left corner of left panel.
Green circle with white check, top-right corner of right panel.
Both flat, solid, same diameter.

STYLE: e-commerce comparison tile, high contrast, sharp.
Both panels must share the same lighting register and shooting style.
NO text, no logo, no watermark.
```

## SLOT CONSTRAINTS
- [LEFT PANEL] hotspots: exactly 3, anatomically plausible, red only (G3).
- [RIGHT PANEL] product per G2 (position / angle / scale / relation only); must be
  brighter and cleaner than left (G4).
- Both panels share one register (G5): same lighting character, same shooting style.
- [BADGES] top corners only — the eye reads top-down; a bottom badge arrives after the
  verdict is already formed. Never add a VS badge on top of X/check (one binary
  argument, one pair of markers).
- **The panels are BEFORE and AFTER, and the AFTER keeps the room** (v1.6). The slots used
  to be called THE PROBLEM and THE ANSWER, and "answer" is what invited a product photo:
  a product on a clean ground answers the question without being an after of anything. One
  render proved it — the `--oldway` garment steamer came back with the left panel a
  lived-in room and the right panel an isolated shirt on a bare wall, which breaks G5 and
  drops the comparison. Renaming the slots is the fix at the source, and the AFTER panel
  now states the same-setting rule outright.
  **Why the type is still `01-pain-split` and not renamed to something with "before" in
  it:** the id is `{step}-{job}-{device}`, and `job` records where the image sits in the
  funnel, not what is in every pixel. This lives at step 1 on cold traffic where the pain
  half carries the work, so job=pain. `06-relief-hero --vsinset` carries the same
  before/after and is filed as job=relief at step 6, because there the pain is one small
  inset and the relief state is the frame. Same structure, two different jobs, and the
  difference is which half dominates. Renaming the type would also mean a new device value
  plus a deprecate-and-replace cycle, which buys nothing the slot names do not already fix.
- **No outer border, and say so in the prompt** (v1.5). A border is layout furniture: a
  page adds it in CSS for nothing, while a rendered one costs frame area and competes with
  G10's safe margin. Worse, this model does not render a border as a margin — it draws a
  thin white rectangle INSET from the edges, floating over the photograph and cutting
  through whatever is behind it. 3/3 renders on 2026-08-12 did exactly that, on all three
  variants. The four other multi-panel types in the library (`03-use-sequence`,
  `04-proof-lockedframe`, `05-persona-grid`, `03-use-grid` in staging) have said "no outer
  border" all along; this type was the only one still asking for one, and it was an
  oversight rather than a decision. The 50/50 split line stays — it is the argument's
  divider, and it rendered correctly every time.

## NEGATIVE
```
[G6] + cluttered background on right panel, dim right panel,
mismatched photo style between panels, visible test rigs or props,
red cues on right panel, distorted face, blood, injury,
inset white rectangle, drawn border line
```
The last two are kept even though the skeleton now asserts the positive form ("each panel
runs to the frame edge"), which Rule 1 step 1 would normally have dropped. They stay
because a bordered comparison tile is a strong market prior and this was the type's only
3/3 failure. Neither token shares a lemma with anything a prompt here requires.

## VARIANTS
### --object (default)
Baseline skeleton as above. The BEFORE is a person with the symptom; the AFTER is the same
person and the same room with the product doing its job. This is the variant where the
same-setting rule is easiest to lose, because the product is the most interesting thing in
the AFTER panel and the model will happily give it a studio.

### --mirror
The strongest comparison form — same person, same shot, only the state changes.
Diff vs base:
```
[RIGHT PANEL: AFTER, replaces the base block]
Full-color photo of THE SAME PERSON in THE SAME setting,
same camera angle, same distance, same wardrobe, same framing,
now in [correct posture/state], [relaxed expression], hands [released position].
The reference product visible at [contact point], secondary to the person.
Brighter, warmer and cleaner than the left panel,
but the SAME lighting setup and time of day. Only the grade differs.

[MIRROR RULE]
Left and right must be the same person, same shot, same everything.
The ONLY differences permitted: posture, expression, presence of the product,
and color grade. Any other change breaks the comparison.

[LEFT PANEL adjustment]
Drop the glowing hotspots — posture and expression carry the problem.
```
- generation_mode override: **multi-pass** (generate the left panel first, then use
  edit mode to change posture/expression/grade while keeping the person; composite the
  split in post — single-pass will produce two different faces).
- Negative additions: `different person between panels, different camera angle between
  panels, different wardrobe, different time of day, golden hour on one side only,
  VS badge, third badge, badges at bottom of frame`

### --oldway
The wrong state is the OLD SOLUTION IN USE — a person struggling with the legacy
product class — instead of a symptom on a body. Use when the buyer's real pain is
the friction of what they already own.
Diff vs base:
```
[LEFT PANEL: BEFORE, replaces the base block]
Desaturated grayscale photo of [age/gender] struggling with [generic legacy
solution class]: [2-3 friction details — tangled tubes, squinting at a tiny
display, scattered discs and manuals], face showing [strain/confusion].
The legacy device must be GENERIC and UNBRANDED, ordinary and plausible,
never broken, dirty or mocked (same fairness logic as 04-proof-lockedframe).

[RIGHT PANEL: AFTER]
Unchanged from base, and the same-setting rule binds hardest here: the BEFORE
panel is a room with a person struggling in it, so the AFTER must be that room
with the job going smoothly — the same wall, the same floor, the same hands.
A hanging garment on a bare wall is the failure this variant invites.
```
- Badges stay the library's X/check top-corner pair. Source exemplars used
  VS badges and even emoji — market habits, deliberately not imported.
- Never imply the left device is a specific competitor (unbranded rule above).
- Negative additions: `brand logos on the legacy device, damaged or mocked
  legacy device, emoji, money props, price-claim imagery`

## WORKED EXAMPLES
### example: knife-sharpener-object — skeleton@1.1, run: untested
Product: rolling knife sharpener · ratio 1:1 · variant --object
- LEFT PANEL — desaturated grayscale close-up of a woman's hands pressing hard with a dull knife into a ripe tomato on a wooden board, skin tearing, juice and seeds squeezed out, knuckles white; hands fill the frame, neutral cropped background
- HOTSPOTS — 3: crushed tomato flesh, knife edge, straining wrist; soft red radial glow, red jagged marks along the blade edge
- RIGHT PANEL — full-color close-up of the same hands gliding through a tomato in one pass, paper-thin uniform slices fanned on light wood; the reference sharpener beside the board in soft focus; clean marble counter, bright even daylight, brighter and cleaner than the left
- BADGES — red circle with white X top-left of left panel, green circle with white check top-right of right panel, flat, solid, identical diameter
Predicted failures: close-up hands holding a knife in both panels (weakest model
skill); "3 points" degrading into scattered hotspots; knife + red possibly tripping
safety filters.

### example: mouth-tape-mirror — skeleton@1.2, run: untested
Product: mouth tape · ratio 1:1 · variant --mirror · multi-pass
- LEFT PANEL — desaturated grayscale, man late 30s in a plain grey t-shirt lying on his back in bed, head on the pillow, mouth hanging open, brow furrowed, neck slightly strained, one arm thrown across the duvet; high three-quarter angle above the pillow; hotspots dropped per the variant
- RIGHT PANEL — the same man, same bed, same t-shirt, same pillow, same angle, distance and framing, now relaxed with mouth closed, jaw soft, brow smooth, both arms resting; the reference tape on his lips, secondary to him; brighter, warmer, cleaner, same lighting setup and time of day, only the grade differs
- MIRROR RULE — only posture, expression, presence of the product and grade may differ
- BADGES — X top-left, check top-right, flat, solid, same diameter; no VS, no third marker
Predicted failure: same-face consistency across independently generated panels — this
is why the variant is multi-pass (generate left, edit into right, composite).

## KNOWN-FLAKY
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
- 1.6 (2026-08-12): **the panels are renamed BEFORE and AFTER, and the AFTER keeps the
  room.** Owner observation: the naming was not logical, because this type is a before and
  after at heart. Correct, and the old names had a cost. THE ANSWER is what invited a
  product photo - a product on a clean ground answers the question without being an after
  of anything - and one render had already shown it: the `--oldway` garment steamer came
  back with a lived-in room on the left and an isolated shirt on a bare wall on the right,
  breaking G5. That render is logged in KNOWN-FLAKY at 1/3, below the patch threshold, so
  the trigger for this change is the owner's naming decision and the render is
  corroboration.
  The AFTER slot now states the same-setting rule outright - same room, same surface, same
  person wherever a person is in frame - and says what happens if it is broken: the panel
  stops being an after and becomes a product photo. G4 is preserved but narrowed: brighter
  and airier by light and calm, never cleaner by deleting the room. `--mirror` and
  `--oldway` had their panel references updated, and `--oldway` carries the rule hardest
  because its BEFORE panel is a room with a person struggling in it.
  PURPOSE now says the structure out loud.
  **The type id does not change.** `{step}-{job}-{device}` records where an image sits in
  the funnel, not what is in every pixel: this lives at step 1 on cold traffic where the
  pain half carries the work, so job=pain. `06-relief-hero --vsinset` carries the same
  before/after and is filed job=relief at step 6, because there the pain is one small inset
  and the relief state is the frame. Same structure, two jobs, and which half dominates is
  the difference. Renaming would also require a new device value and a
  deprecate-and-replace cycle, buying nothing the slot names do not already fix.
- 1.5 (2026-08-12): **the outer border leaves the render.** `LAYERS` asked for a "thin
  white outer border"; this model does not render that as a margin, it draws a thin white
  rectangle inset from the frame edges, floating over the photograph and cutting through
  the content behind it. Evidence 3/3, well past the §6.2 threshold, one render per
  variant: `--object` (under-desk footrest, the line crosses the subject's arm),
  `--mirror` (cervical pillow, it crosses the sleeper's body), `--oldway` (garment steamer,
  it crosses the ironing board). Owner report: "always a white frame in the image".
  The line now asserts the positive — each panel runs to the frame edge — and names the
  prohibition once. Two tokens added to NEGATIVE despite the positive assertion, because a
  bordered comparison tile is a strong market prior and this is the type's only 3/3 fault.
  Worth recording WHY this survived so long: the four other multi-panel types
  (`03-use-sequence`, `04-proof-lockedframe`, `05-persona-grid`, `03-use-grid` in staging)
  have all said "no outer border" since they were written. This type was the sole outlier,
  and nothing in its own history argued for the border — it was inherited from the founding
  exemplar and never questioned. A border is layout furniture: the page adds it in CSS for
  free, while a rendered one costs frame area and fights G10's safe margin.
  The 50/50 split line is untouched — it is the argument's divider and rendered correctly
  in all three.
  The `RATIO:` line goes too, in the same block and for the same reason it went from
  `01-pain-scene` at 1.4: adapter Rule 4 has 6/6 renders ignoring a written ratio, so the
  line taught every filler to write something the adapter then stripped. Ratio stays a
  render parameter and a slot requirement; it stops being prompt text.
  Also logged: KNOWN-FLAKY gains a register split on `--oldway` at 1/3, where the right
  panel came back as a studio packshot against a lived-in left panel. Below threshold, so
  the skeleton is not patched for it.
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

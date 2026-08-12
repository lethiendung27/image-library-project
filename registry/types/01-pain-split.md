---
id: 01-pain-split
step: 1
job: pain
device: split
version: "1.5"
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
Stop the scroll with pain in a 0.5-second glance: wrong state left, answer right,
judged by badges. Image 2 on Amazon, ad thumbnails, tiles in a landing-page grid.

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
TYPE: 01-pain-split v1.5 [--object | --mirror | --oldway]
LAYERS: 2 panels, hard vertical split 50/50. Each panel runs all the way to the
frame edge. No outer border, no drawn border line anywhere in the image.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly. Do not redesign or add features.

[LEFT PANEL: THE PROBLEM]
Desaturated grayscale photo of [age/gender] in [wardrobe],
[wrong posture/behavior] on [surface], face showing [discomfort expression].
Glowing red hotspots at [3 points], soft red radial glow,
[red jagged marks] along [affected structure].
Neutral cropped background, subject fills frame.

[RIGHT PANEL: THE ANSWER]
Full-color shot of the reference product [in place / in use] at [context],
seen from [angle], occupying [X%] of the panel.
Clean uncluttered background, bright even lighting,
noticeably brighter and cleaner than the left panel.

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
Baseline skeleton as above: person with problem vs product as answer.

### --mirror
The strongest comparison form — same person, same shot, only the state changes.
Diff vs base:
```
[RIGHT PANEL, replaces THE ANSWER]
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
[LEFT PANEL, replaces THE PROBLEM]
Desaturated grayscale photo of [age/gender] struggling with [generic legacy
solution class]: [2-3 friction details — tangled tubes, squinting at a tiny
display, scattered discs and manuals], face showing [strain/confusion].
The legacy device must be GENERIC and UNBRANDED, ordinary and plausible,
never broken, dirty or mocked (same fairness logic as 04-proof-lockedframe).

[RIGHT PANEL]
Unchanged from base: the reference product [in place / in use], brighter and
cleaner (G4).
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
- **Register split between panels on `--oldway`, 1/3 renders, 2026-08-12.** The garment
  steamer run put a lived-in room on the left and what reads as a studio packshot on the
  right — an isolated shirt on a plain white wall, no room around it. The base NEGATIVE
  already bars `mismatched photo style between panels` and G5 binds here, so this is not a
  missing law; it is the model reaching for catalogue lighting the moment the right panel
  holds a product and nothing else. One observation, below the §6.2 threshold, so the
  skeleton is untouched. If it recurs, the fix is a slot patch: name the right panel's room
  as explicitly as the left panel's.

## CHANGELOG
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

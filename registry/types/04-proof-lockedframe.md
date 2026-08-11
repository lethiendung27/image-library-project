---
id: 04-proof-lockedframe
step: 4
job: proof
device: lockedframe
version: "1.4"
status: active
replaced_by: null
ratios: ["5:3", "16:9", "1:1", "3:2"]
channels: [advertorial, landing-page, marketplace, paid-social]
requires_product_photo: true
generation_mode: multi-pass
axes:
  camera_lock: [strict, handheld]
  context_mode: [natural-use, declared-test]
variants: [rivals, verdict, timelapse, capture]
exempt_from: [G3, G4]
pairs_with: [02-cause-anatomy, 06-relief-hero, 01-pain-scene]
never_with: []
---

# 04-proof-lockedframe

## PURPOSE
Physical proof the skeptic inspects for themselves: multiple panels, everything held
constant, exactly one variable changes. No badges, no glow, no winner declared — it
does not ask for belief, it invites a look.

## TRIGGER
use_when: >
  The buyer already understands the problem and mechanism, is now skeptical and
  wants to see for themselves. The "I tried three things" beat of an
  advertorial, or a comparison image in the gallery. Use ONLY when the
  difference is visible to the naked eye inside a static frame — otherwise
  switch variants (see VARIANT SELECTION RULE).
avoid_when: >
  The difference is invisible or only felt in use (then the object variants
  produce pretty-but-empty images — verified failure). Never as a
  scroll-stopper; this type is slow and needs an already-attentive viewer.
  --rivals never on marketplace (no product in frame violates gallery rules).

## SKELETON
```
TYPE: 04-proof-lockedframe v1.3
RATIO: [5:3 / 16:9 / 1:1]
LAYOUT: [N] equal vertical panels, thin white gutters, no outer border.
REGISTER: documentary photography. NO graphic overlays, badges, arrows or text.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the item in panel [N].
Preserve shape, proportions, material, finish and color exactly.

[CAMERA — choose ONE mode, see CAMERA LOCK SELECTION]

[LOCKED CAMERA — camera_lock: strict]
Identical camera position, focal length, height and angle in every panel.
Every fixed element in the frame must align pixel for pixel across all panels:
[list 3-4 anchor objects that must not move].
Identical lighting, identical exposure, identical white balance in every panel.

[HANDHELD CONTINUITY — camera_lock: handheld]
Same room, same surface, same light direction, same rough shooting distance.
Shot by the same person on a phone on different days, not on a tripod.
MUST VARY between panels, naturally and independently:
  camera position shifted 10-20cm in any direction,
  camera angle differing by 5-10 degrees,
  the object rotated 15-30 degrees, resting at a different tilt,
  the object placed a few centimetres from where it sat before,
  incidental details different (droplets, towel folds, a different item at frame edge),
  slight exposure and white balance drift, as if shot under different daylight.
MUST STAY CONSTANT: the room, the surface, the light direction,
the identity of the object, the single variable being compared.
The panels must look like photographs a person took, not renders from one
scene file. Perfect alignment reads as CGI and destroys the evidence.

[SCENE, constant across all panels]
[specific environment], [surface the variable sits on].
Deliberate real-world clutter: [2-3 mundane untidy details].
Flat [light quality], no strong shadows, no sunlight, no styling.

[THE VARIABLE, the only thing that changes]
Panel 1: [state/item 1].
Panel 2: [state/item 2].
Panel 3: [state/item 3].

[JUDGEMENT RULE]
No panel may be favoured. No badge, no glow, no color cue, no brighter exposure.
The viewer decides. All panels equally lit and equally neutral.

STYLE: honest documentary product test photography, unstyled, natural, sharp.
NO text, no logo, no watermark.
```

## SLOT CONSTRAINTS
- **CAMERA LOCK SELECTION** (evidence-based, v1.3): `strict` when all panels belong to
  one session and the variable is an object swapped in and out; `handheld` when panels
  are separated by time. A pixel-locked frame across "six months" is proof of staging,
  not of process — it betrays its own argument.
- **VARIANT SELECTION RULE** (verified on shower filter): if the difference between
  products does NOT appear inside a static frame, do not use --rivals or --verdict.
  Switch the variable from "which product" to "which state of the same object"
  (--timelapse / --capture). Applies to every invisible-mechanism product: filters,
  supplements, skincare, software.
- G7 applies at its strictest here (natural-use), except --capture which runs as
  `context_mode: declared-test`.
- Multi-pass is mandatory for `strict` (generate one panel, edit-swap the variable,
  composite); `handheld` may run single-pass.

## NEGATIVE
```
[G6] + badges, arrows, glows, checkmarks, one panel brighter,
inconsistent lighting between panels, studio background, clean styled set,
staged perfection, saturated colors, red or green cues, motion blur,
people, hands, brand logos, recognizable trademarks
```
For `strict` add: `different camera angle between panels, shifted background elements`.
For `handheld` add: `identical framing between panels, pixel-perfect alignment,
tripod shot, 3D render look, CGI, product visualization,
identical water droplets between panels`.

## VARIANTS
### --rivals
Three common existing alternatives, unbranded; our product absent. The "I tried three
things, none worked" beat. Diff:
```
[PRODUCT REFERENCE] Not applicable. No reference product appears in this image.
[THE VARIABLE] Panel 1-3: [generic alternative type], unbranded, placed on [surface].
All three are common existing solutions people already try.
They must look ordinary and plausible, not deliberately broken or dirty.
[JUDGEMENT RULE addition] None of them wins. The image makes no claim.
```
- Channels: advertorial, paid-social only (no product in frame → not marketplace-legal).
- Trap: uglifying the alternatives confesses staging — they must look like things the
  viewer owns.
- Negative additions: `damaged or dirty items, exaggerated flaws, one item obviously better`

### --verdict
Two unbranded alternatives + the reference product in the LAST panel. Diff:
```
[PRODUCT REFERENCE] ...for the item in panel 3 ONLY. Panels 1 and 2 contain
generic unbranded alternatives, not the reference product.
[ORDER RULE] The reference product is always in the LAST panel.
Left-to-right reading ends on it, which is the resolution position.
[FAIRNESS RULE, replaces JUDGEMENT RULE]
Panels 1 and 2 must be given exactly the same photographic respect as panel 3:
identical exposure, identical background tidiness, identical framing generosity.
The alternatives must look like reasonable products someone would genuinely buy.
The difference between panels must be VISIBLE IN THE OBJECTS THEMSELVES,
never in how they are lit, styled, cropped or graded.
No badge, no glow, no arrow, no color cue on any panel.
```
- May only win by physics, never by image treatment — otherwise it collapses into a
  long 01-pain-split and loses all evidentiary value.
- Pick the two MOST COMMON alternatives buyers already own, never the worst.
- Negative additions: `last panel brighter or cleaner than the others, hero lighting
  on the final panel, alternatives made to look broken, cluttered first panels`

### --timelapse (camera_lock: handheld)
Same object across time; the variable is its condition. Diff:
```
[THE VARIABLE] the color/condition of [the same component] at different points of use:
Panel 1: clean/new state. Panel 2: partial state. Panel 3: saturated state,
[texture must remain readable as what it is — e.g. granules stay granular].
[CONTEXT INTEGRITY] an ordinary inspection moment ([how a real person would
actually see this state]). Nothing cut open, propped up or arranged for the camera.
```
- Strongest proof for invisible-mechanism products: the viewer already believes
  something is in the water/air — this shows it, without touching any competitor.
- Legal: no day counts, no captured-substance claims in text. The image only shows.
- Negative additions: `cut-open product, cross-section, product standing upright
  unnaturally, staged arrangement, mold, slime, blood-like color, mud,
  texture losing its granular structure`

### --capture (context_mode: declared-test, 2 panels, ratio 3:2)
Output filtered vs unfiltered through an intermediate medium (white cloth). Diff:
```
[SCENE addition] A declared at-home test, staged the way an ordinary person would:
[cloth tied with a rubber band, slightly crooked, a basin underneath] —
amateur staging reads truer than neat staging.
[THE VARIABLE] Panel 1: no product fitted, [medium] marked with [residue pattern].
Panel 2: the reference product fitted, the same [medium] clean and evenly damp.
```
- Channels: advertorial only. Weaker than --timelapse (viewer never sees the process);
  if both run, --timelapse first so it vouches for --capture.
- Negative additions: `laboratory equipment, clinical setup, cloth in different
  position between panels, dramatic staining, black mold, cartoonish contrast`

## WORKED EXAMPLES
### example: shower-filter-timelapse-handheld — skeleton@1.3, run: untested
Product: metal shower filter cartridge · ratio 5:3 · 3 panels · variant --timelapse · axes: camera_lock=handheld, context_mode=natural-use
- HANDHELD CONTINUITY — same bathroom counter, basin, daylight from the left and rough shooting distance; shot on a phone on three separate occasions, never a tripod. VARY: camera position 10-20cm, angle 5-10°, cartridge rotated 15-30° at a different tilt and a few cm from where it sat, droplets scattered differently, towel folded differently, slight exposure and white-balance drift. CONSTANT: room, surface, light direction, identity of the cartridge, and the single variable
- SCENE — the cartridge just removed and laid on its side, still faintly wet, open threaded end angled to camera so the packed media shows at the opening; water spots on the counter, a damp ring under it, a towel at frame edge; overcast daylight from the left
- THE VARIABLE — colour of the media visible inside the open end. Panel 1: clean, uniform white and pale grey granules, evenly packed. Panel 2: partly discoloured, dull ochre and light rust across the exposed surface, uneven, pale granules still showing. Panel 3: heavily discoloured, deep rust brown across the whole surface, granule texture still clearly readable AS granules, darker staining at the rim, light rust creeping onto the shell near the threads
- CONTEXT INTEGRITY — an ordinary inspection moment; nothing cut open, propped or arranged for the camera
- JUDGEMENT — no badge, glow, colour cue or arrow; all panels equally neutral
Evidence chain: the strict-camera predecessor of this prompt was rendered and READ AS
CGI (identical droplets, identical tilt across "months") — that run produced the
handheld mode (v1.3). Panel 3 of that run also drifted into mud; the granularity
constraint above is the fix.

### example: shower-filter-verdict — skeleton@1.2, run: fail
Full prompt in seed conversation.md (three filters on one shower arm, locked camera).
The lock held perfectly — and the image argued nothing: three filters merely LOOK
different; better-looking is not better-filtering, and buyers know it. Kept as the
boundary case that produced the VARIANT SELECTION RULE. Secondary fault: panel 3
mounted the filter with no shower head behind it — half-installed device, the G7
completeness violation that helped produce G7.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.4 (2026-08-11): channels gain `paid-social`. Self-contradiction: the --rivals
  variant already declares "Channels: advertorial, paid-social only" while the
  frontmatter excluded paid-social. The type-level avoid_when ("never as a
  scroll-stopper") still gates the slow variants there — that is a Stage 2 judgment,
  not a channel ban.
- 1.3 (2026-08-10): camera_lock axis (strict/handheld) with time-gap selection rule;
  granularity constraint on saturated media. Evidence: rendered strict-timelapse output
  read as CGI (user test, seed conversation.md).
- 1.2 (2026-08-10): --timelapse and --capture variants + VARIANT SELECTION RULE.
  Evidence: rendered --rivals/--verdict on shower filter judged "pretty but empty"
  (user test — object variants carry no proof for invisible mechanisms).
- 1.1 (2026-08-10): split into --rivals / --verdict with order and fairness rules.
  seed: conversation.md.
- 1.0 (2026-08-10): initial from the three-car-seat-cushions exemplar. seed: conversation.md.

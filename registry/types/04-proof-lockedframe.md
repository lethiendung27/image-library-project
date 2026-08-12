---
id: 04-proof-lockedframe
step: 4
job: proof
device: lockedframe
version: "1.5"
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
TYPE: 04-proof-lockedframe v1.5
RATIO: [5:3 / 16:9 / 1:1]
LAYOUT: [N] equal vertical panels, thin white gutters, no outer border.
REGISTER: documentary photography. NO graphic overlays, badges, arrows or text.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference for the item in panel [N].
Preserve shape, proportions, material, finish and color exactly.

[PRODUCT PROMINENCE — required whenever a product is in frame]
The product is the SUBJECT of the panel it appears in and fills at least [X%]
of that panel. It is never a small object resting at the edge of a scene the
viewer is actually looking at.

[CAMERA — choose ONE mode, see CAMERA LOCK SELECTION]

[LOCKED CAMERA — camera_lock: strict]
Identical camera position, focal length, height and angle in every panel.
Every fixed element in the frame must align pixel for pixel across all panels:
[list 3-4 anchor objects that must not move].
Identical lighting, identical exposure, identical white balance in every panel.

[HANDHELD CONTINUITY — camera_lock: handheld]
Shot by the same person on a phone on different days, not on a tripod.
Describe ONE framing, once, for every panel: [where the subject sits in frame],
[camera height and distance], [what occupies the upper and lower thirds].
Then state the band: it reads as one shot taken [N] times, never as [N]
different shots — drift is a few degrees of tilt and a few centimetres of
position, no more.
Put most of the variation on the PROPS rather than the camera, named per panel:
  Panel 1: [prop state]. Panel 2: [prop state]. Panel 3: [prop state].
  (a towel refolded, an item moved, one thing missing, a new incidental mark)
Their light differs only in exposure, never in warmth.
MUST STAY CONSTANT: the room, the surface, the light direction,
the identity of the object, the single variable being compared.
The panels must look like photographs a person took, not renders from one
scene file. Perfect alignment reads as CGI and destroys the evidence.

[WORDING LAW — camera_lock: handheld, evidence-based v1.5]
Never write the drift as a delta: "shifted 10-20cm", "a few centimetres from
where it sat before". A relative instruction needs a reference point the model
does not have inside one canvas, so it renders a single background and swaps the
object — the observed failure. But giving each panel a fully independent framing
overshoots into three unrelated photographs. One shared framing plus one small
named per-panel deviation is the only wording that lands in the band.

[SCENE, constant across all panels]
[specific environment], [surface the variable sits on].
Deliberate real-world clutter: [2-3 mundane untidy details].
Flat [light quality], no strong shadows, no sunlight, no styling.

[GRADE — set by variant, never polarised BETWEEN panels]
One grade across every panel, coming from the room and the weather rather than
a filter. Still colour, never black and white — a mono conversion on a
documentary register reads as edited and destroys the credibility it is selling.
--rivals: muted and cool, low saturation, no warm tone anywhere. Every panel is
  an unsolved state, so one shared unresolved tone favours none of them. This is
  the only variant whose grade carries polarity, and it carries it for the WHOLE
  image, never between panels.
--verdict / --timelapse / --capture: neutral, with no panel warmer, brighter or
  more saturated than the others. If the resolved panel also looks better graded,
  the image has won by treatment and the argument is void.

[THE VARIABLE, the only thing that changes]
Panel 1: [state/item 1].
Panel 2: [state/item 2].
Panel 3: [state/item 3].

[JUDGEMENT RULE]
No panel may be favoured. No badge, no glow, no color cue, no brighter exposure.
The viewer decides. All panels equally lit and equally neutral IN JUDGEMENT:
"neutral" here means no panel is argued for, NOT that the image carries no
grade. The grade is set by [GRADE] above and applies to every panel alike.

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
- **`handheld` single-pass is conditional on the WORDING LAW** (v1.5). It is viable
  only when the framing is written once and shared with small named per-panel
  deviations. Written as relative deltas it produces one repeated background;
  written as independent per-panel framings it produces unrelated photographs.
  Multi-pass (three renders, composited) remains the fallback when a single pass
  will not land in the band.
- **Product prominence** (v1.5): the type carried no size or placement rule for the
  product, the only product-bearing type in the registry without one — so the product
  drifted to the frame edge while a background object held the eye. `[PRODUCT
  PROMINENCE]` now fixes a floor. Note the deeper constraint it does not lift: the
  JUDGEMENT and FAIRNESS rules forbid winning by image treatment, so this type can
  make a product the SUBJECT but can never make it the HERO. When the brief is
  "emphasise the product", route to a type whose law lets it win — `01-pain-split`
  (G4) or `06-relief-hero` — instead of stretching this one.
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
- 1.5 (2026-08-12): `[WORDING LAW]`, `[GRADE]`, `[PRODUCT PROMINENCE]`; `[JUDGEMENT
  RULE]` disambiguated. Evidence: owner-reported failed render of a `--rivals`
  drain-unblocker triptych — pixel-identical background across all three panels
  (one brown chip at one coordinate), no object emphasised, and full-colour grade
  on three panels that were all meant to read as failures. Three findings, each
  fixed above. (a) The handheld slot was written in relative deltas, unusable in a
  single canvas; the second attempt overcorrected into three unrelated framings, so
  the law now names the band. (b) The type was the only product-bearing type with no
  prominence rule at all. (c) `exempt_from: [G3, G4]` was read as exemption from all
  tonal grammar — G4 governs brightness BETWEEN panels, and nothing governed the
  absolute grade of the image, so `--rivals` rendered cheerful while the library's
  own unwritten convention marks unsolved states desaturated (`01-pain-scene`,
  `01-pain-split` left, `03-spec-split` left). Still open: that convention is
  practised in five types and written in none — a global saturation rule is proposed
  and NOT taken here, since it would bind sixteen types.
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

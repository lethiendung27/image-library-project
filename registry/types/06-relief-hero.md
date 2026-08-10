---
id: 06-relief-hero
step: 6
job: relief
device: hero
version: "1.4"
status: active
replaced_by: null
ratios: ["2:1", "4:5"]
channels: [landing-page, marketplace, paid-social]
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
none) — named `06-relief-hero--{register}--{inset_mode}`.

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
```
TYPE: 06-relief-hero v1.3
RATIO: [2:1 / 4:5]
LAYERS: hero base + optional inset panel + optional product view

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and color exactly. Do not redesign or add features.
The product must be identical in every layer of this image.

[ZONE A: HERO, right 60%]
[age/gender] in [wardrobe, tone matching background],
[pose — see POSE], while [activity], [warm expression].
The product visible at [contact point], seen from [angle A], unobstructed,
in [ONE mode of use — G7-X: the same mode in every layer].
Setting: [environment], [3 props], [light source — see LIGHT]. Background blurred,
high-key [neutral palette] grade. Subject offset right, empty mid-frame for headline.

[VISIBLE MECHANISM — required slot, G8]
If the product emits, produces or moves anything visible (mist, spray, steam,
foam, water, particles, light), that output is the PRIMARY subject of the frame,
not the person and not the product. Frame, light and expose for the output.
It must occupy at least 15% of the frame and read at thumbnail size.
If the product produces nothing visible, do NOT invent an effect.

[POSE]
IF the product is actively operated by the user: mid-action, hands engaged,
gaze on the point of use, expression of focused satisfaction rather than repose.
IF the product works passively while the user does something else:
relaxed pose, [relief position], gaze away from the product.

[LIGHT]
IF visible mechanism present: [backlight / hard side light] from [source],
strong enough to make the output glow against a darker background area.
Accept lens flare and blown highlights, they read as real.
ELSE: soft even [natural window light], background blurred, high-key grade.

[ZONE B: PRODUCT VIEW, bottom-left foreground, front z-layer]
INCLUDE THIS LAYER ONLY IF the hero scene cannot show the product clearly.
Skip it entirely when the product is held in hand, centered, and legible at
thumbnail size.
The same product from the reference, shown from [angle B, MUST differ from angle A
and reveal the side hidden in Zone A], floating above the surface,
occupying [20-30%] of the frame width.
Studio lighting, soft contact shadow, razor sharp, clean cutout edge.
[IF product has multiple real colorways: show 2 units, colorways: [c1], [c2].
 IF single colorway: show 1 unit only.]

[ZONE C: INSET — content set by inset_mode, see VARIANTS-BY-AXIS]

STYLE: clean commercial e-commerce banner, bright airy, sharp focus, 4K.
NO text, no logo, no watermark.
```

## SLOT CONSTRAINTS
- Pain exists ONLY inside the inset (when present). Zone A is 100% relief. Never mixed.
- [ZONE B] exists only to reveal an angle Zone A hides (its reason to exist); a layer
  repeating information costs frame space and buys nothing.
- Colorways in Zone B: only real ones (G2 — fabricated colorways was the original
  exemplar-era failure).
- G7-X binds hard here: one mode of use across hero, inset and product view. The
  humidifier ugc exemplar failed exactly this (wall-mounted inset, handheld hero).
- G8 evidence note: three exemplars in a row proved the visible output outweighs image
  polish — a badly-shot frame with visible mist beats a clean frame without it.

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
[REGISTER OVERRIDE]
Shot on a phone by an ordinary person. Slightly off exposure,
mild overexposure on skin or windows, no rim light, no negative space,
the room behind left exactly as it is: furniture, cables, books, clutter.
Framing casual and a little too close. Subject not styled.
This register buys trust, not beauty. Do not clean it up.
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
[ZONE C: INSET, top-left, white 3px border, split 50/50, red circular VS badge at seam]
LEFT: desaturated grayscale [wrong state], glowing red hotspots at [3 points].
RIGHT: full-color [correct state] with [blue/cyan] overlay showing [mechanism].
Both halves must share the same register (both photographic, or both illustrated).
Right half brighter and cleaner than left half.
```

### inset_mode: --recall
```
[ZONE C: INSET, single circle]
One circular cutout containing a photograph of [the problem state],
positioned [corner], occupying [12-18%] of frame width.
The inset MUST be visually marked as the past state, either desaturated,
or carrying a small red X badge. An unlabelled inset reads as a result,
which inverts the entire message.
REGISTER: the inset photo must match the hero in resolution, grade and
light quality — a darker or lower-resolution inset reads as pasted in.
```
Negative additions: `unlabelled before-state inset, low resolution inset,
inset darker than hero, inset from a different photographic source`

### inset_mode: --context
```
[ZONE C: INSET, rectangular, thin white border]
A plain closer shot of the same product in its real installed position or real
place of use, taken from a step back so the whole fitting is clear.
HARD CONSTRAINT (G7-X): the mode of use in the inset and in the hero must be
the SAME. Installed in the inset while handheld in the hero contradicts itself.
```

### inset_mode: --detail
```
[ZONE C: INSET, rounded rectangle or circle]
A MAGNIFIED view of ONE product detail the hero cannot show at scene scale:
the display/UI, an internal mechanism, or a port array.
Occupying [15-25%] of frame width, positioned [corner], linked to the
in-scene product by proximity — no arrows, no glow borders.
IF the detail is a screen/UI: NEVER model-drawn. Render or photograph the
real interface and composite it in post (screen digits are diegetic product
UI — see the G6 scope note). Model-drawn digits will be gibberish.
IF the detail is an internal mechanism: keep the cutaway in a clean technical
register and confine it to the inset — internals bleeding into the
photographic hero break G5.
```
Use when the buying argument depends on a feature too small to read in scene
(memory log, measurement display, mechanism quality).

### inset_mode: --none
No Zone C. Use when the scene carries the whole argument.

## WORKED EXAMPLES
### example: shower-filter-commercial-vsinset — skeleton@1.1, run: untested
```
A wide 2:1 e-commerce banner.

Use the attached product photo as the exact reference for the shower filter. Preserve
its shape, proportions, material, finish and color exactly. Do not redesign or add
features. The product must be identical in every layer of this image.

MAIN SCENE (right two-thirds): A woman in her late 20s with long dark hair stands under
a running shower, head tilted back, eyes closed, calm satisfied expression, water
streaming over her shoulders. The filter is installed above her between the hose and
the showerhead, seen from a low three-quarter angle, unobstructed. Setting: bright
modern bathroom, white marble tile, glass partition, a small eucalyptus bundle, soft
daylight from a frosted window. Background blurred, high-key white and warm grey grade,
steam catching the light. Subject offset right, empty mid-frame.

PRODUCT VIEW (bottom-left foreground): The same filter from the reference, shown from a
top-down angle looking into the inlet, floating above the surface, occupying about 25
percent of the frame width. Studio lighting, soft contact shadow, razor sharp, clean
cutout edge. Show one unit only.

INSET PANEL (top-left, white 3px border, split 50/50, red circular VS badge at the
seam): LEFT: desaturated grayscale macro photo of a showerhead nozzle plate caked with
white limescale, dull uneven dripping water, glowing red hotspots at three clogged
nozzles. RIGHT: full-color macro photo of a clean nozzle plate spraying clear even
jets, with a cyan translucent overlay tracing the water path. Both halves photographic,
right half brighter and cleaner.

STYLE: clean commercial e-commerce banner, bright airy, sharp focus, 4K.
NO text, no logo, no watermark.
```
Predicted failure: Zone C right half slipping into 2D illustration against the photo
macro (register mismatch inside the inset).

### example: shower-filter-ugc-context — skeleton@1.3, run: untested
```
A photograph taken on a phone by an ordinary person, 2:1 ratio.

Use the attached product photo as the exact reference for the shower filter. Preserve
shape, proportions, material, finish and color exactly. It appears installed in both
the main scene and the inset. Never handheld.

MAIN SCENE (right two-thirds): A man in his early 40s standing in his own bathroom with
his eyes closed and his face tilted up under the running shower, water hitting his
shoulders, an unguarded relaxed expression. The reference filter is fitted above him
between the arm and the shower head, clearly visible in the upper part of the frame.
The water spray is the primary subject: dense individual streams and fine mist backlit
by a window behind him, occupying a large part of the frame and clearly readable at
small size.

REGISTER: shot on a phone. Slightly overexposed on the tiles and the window, no rim
light, no negative space. Framing casual and a little too close, tilted a few degrees.
The bathroom left exactly as it is: shampoo bottles crowded on the corner shelf, a
razor on the ledge, towels bunched on the rail, water spots on the glass. Not styled,
not cleaned up.

INSET (top-left corner, rectangular, thin white border): a plain closer shot of the
same filter installed on the same shower arm, taken from a step back so the whole
fitting is clear. Same mode of use as the main scene: installed, never in hand. Same
room, same daylight.

STYLE: casual phone photography, natural, unstyled, honest.
NO text, no logo, no watermark, no badges, no arrows.
```
Predicted failure: distance — an installed filter high in frame may render at
unrecognizable size; fallback framing is low-angle, filter + water jet as subject,
person reduced to a shoulder.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
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

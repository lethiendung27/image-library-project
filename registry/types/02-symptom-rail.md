---
id: 02-symptom-rail
step: 2
job: symptom
device: rail
version: "1.3"
status: active
replaced_by: null
ratios: ["1:1", "4:5"]
channels: [marketplace, landing-page]
requires_product_photo: true
generation_mode: single-pass
variants: []
exempt_from: []
pairs_with: [01-pain-split, 03-mechanism-ghostbody]
never_with: []
---

# 02-symptom-rail

## PURPOSE
One product, many problems: a calm hero scene plus a vertical rail of symptom vignettes.
Argues by breadth of the problem — it does not prove, it counts.

## TRIGGER
use_when: >
  The product solves several problems at once and one image must show the
  coverage. Image 2 or 3 in the gallery, right after the scroll-stopper. Fits a
  broad audience where each buyer hurts in a different way.
avoid_when: >
  The product solves exactly one problem — the rail becomes padding. Never as a
  main image. Not when the symptoms cannot be photographed.

## SKELETON
```
TYPE: 02-symptom-rail v1.3
LAYERS: photographic hero + optional action layer + vignette rail on the right edge.

[PRODUCT REFERENCE]
Use the attached product photo as the exact reference. Preserve shape,
proportions, material, finish and colour exactly. Do not redesign or add features.

[HERO, left 72%]
[age/gender] in [wardrobe, muted neutral tones], [correct posture/behaviour] while
[everyday activity], calm content expression, [gaze direction].
The reference product AT ITS REAL MOUNTING POINT and actually working — the thing
it mounts to is present and whole in the frame (G7). Seen from [angle],
unobstructed, at least [X%] of the hero height. It is part of the scene, never a
cutout floating over it.
Setting: [environment], [3 props], soft natural window light, background blurred.
Bright high-key [neutral palette] grade. Subject offset left.

[ACTION — include ONLY if the product moves something visible]
The moving substance itself, gathered into a directional form: [N] streams of
[the real material — moist air, water, steam, dust, foam, light], evenly spaced,
thinning and fading where the substance disperses.
DIRECTION IS PHYSICAL TRUTH: if the product draws in, the substance converges INTO
its intake; if it emits, it leaves the outlet. One direction only, never both.
The substance keeps its own real colour. Red is reserved for the rail.
If the product moves nothing visible, OMIT this block — inventing an effect is
what G8 forbids.

[RAIL, right 25-28%, vertical band, [straight / soft S-curved] left edge]
Pale [tint] gradient panel. [3] circular vignettes stacked evenly, white ring
border, equal diameter, generous spacing.
Each vignette: tight crop of [same-role person or object], no face visible,
showing [pain gesture at body zone / visible symptom], red radial glow centred on
that point.
Ordered top to bottom: [item1], [item2], [item3].
All vignettes share the hero's lighting, wardrobe tone and photographic style.

STYLE: clean e-commerce infographic tile, bright airy, sharp focus, 4K.
NO text, no letters, no logo, no watermark.
```

## SLOT CONSTRAINTS
- **The arrow is made of the substance, or there is no arrow** (v1.3). Owner rule, and it
  fixes a logic error the old wording invited. `[ZONE B]` used to ask for "[N] [color]
  rounded arrows overlaid on the product pointing [direction], flat vector style" — an
  abstract graphic that CLAIMS a direction. Two of three renders on 2026-08-12 got the
  claim wrong or made it meaningless: a dehumidifier drew three blue arrows pointing UP AND
  OUT of its top, which inverts what a dehumidifier does, and a heating pad drew amber
  arrows for heat, which is not visible at all. Making the arrow out of the moving substance
  fixes both at once, because a stream of water droplets converging into an intake cannot
  point the wrong way without looking absurd, and a substance that does not exist cannot be
  drawn.
  The omit branch is G8's own logic, one type over: if the product produces nothing visible,
  do not invent an effect. It also retires the amber-arrow problem, where a warm arrow for
  GOOD heat collided with G3's `orange = wrong heat`.
- **Zone names must not be single letters** (v1.3). One render printed large blue circled
  letters A, B and C into the image — the prompt carried `ZONE A`, `ZONE B`, `ZONE C` as
  headings and the model drew the headings it was shown. G6 bans letters, and the avoid line
  carried `text`, and it still happened, because the leak came from the slot names rather
  than from an instruction. The zones are now HERO, ACTION and RAIL. `06-relief-hero` still
  uses ZONE A/B/C and carries the same risk; it is not changed here, but it should be when
  that type is next opened.
- **G7 binds the hero and the old wording never said so** (v1.3). `[ZONE A]` asked for the
  product "at [contact point]" and one render put a shower filter on a disembodied shower
  arm hovering over a bathroom sink, in a scene with no shower in it — the product mounted
  to nothing, in a moment where it could not be working. G7's completeness test covers
  exactly this ("if the product mounts onto something, that something is present and
  whole"), and the hero is a photographic scene layer, so G7 was always binding; the type
  simply never reminded anyone. The slot now says it, and adds that the product is part of
  the scene rather than a cutout floating over it.
- [RAIL] vignette mode — choose ONE and state it explicitly in the prompt:
  - `pain-gesture` (hand pressing the hurting zone): when the symptom is a feeling.
  - `visible-symptom` (a visible manifestation on body or object): when the symptom is
    a consequence you can see.
- 3 vignettes, not 4 — at mobile size a 4-vignette rail drops below legibility.
- Vignette order follows anatomy top-to-bottom (or severity); never shuffled.
- The ACTION substance must not read red: red belongs to the rail (G3), and a red stream
  on the product reads as a heating feature.
- Vignettes must share the hero's register (G5) — a stock-photo rail on a lifestyle
  hero reads as two sources.

## NEGATIVE
```
[G6] + letters, circled letters, zone labels, faces inside vignettes,
mismatched lighting between hero and vignettes, heat or warming cues,
cluttered background, dark grade, vignettes too small, overlapping circles,
floating product cutout, product mounted to nothing
```
`red arrows on product` was dropped at v1.3: the ACTION block now names its substance and
its colour positively, and with an arrow made of water or air the token risked suppressing
the stream itself. `letters` and `circled letters` were added after a render printed A, B
and C into the frame.

## WORKED EXAMPLES
### example: shower-filter — skeleton@1.1, run: untested
Product: metal shower filter · ratio 1:1 · vignette mode: visible-symptom
- ZONE A (left 72%) — woman late 20s, long dark hair, under a running shower in a bright modern bathroom, head tilted back, eyes closed, calm content; the reference filter screwed between hose and showerhead above her, unobstructed; white marble tile, glass partition, a eucalyptus bundle, soft daylight from a frosted window, background blurred; bright high-key white and warm grey; subject offset left
- ZONE B — three BLUE rounded arrows on the water stream below the filter, pointing down, evenly spaced, semi-transparent, fading at the tips, flat vector
- ZONE C (right 26%, soft S-curved left edge) — pale aqua gradient panel; three circular vignettes, white ring border, equal diameter, no face visible, sharing the hero's light and style: top, a hand through dry brittle hair with strands breaking, red glow at the ends; middle, a forearm with flaky irritated skin, red glow on the patch; bottom, fingers scratching a scalp at the hairline, red glow at the scalp
Predicted failure: the model regressing to pain-gesture (hands clutching) even in
visible-symptom mode — the reason the two modes must be named explicitly in the prompt.

## KNOWN-FLAKY
(populated from observation evidence only)

## CHANGELOG
- 1.3 (2026-08-12): **the arrow is made of the substance the product moves, or there is no
  arrow.** Owner rule, given as: for a dehumidifier the arrow must be formed by the water
  droplets being drawn back in. It repairs a logic error the old wording invited, and the
  renders show why. `[ZONE B]` asked for "[N] [color] rounded arrows overlaid on the product
  pointing [direction], flat vector style" — an abstract graphic that CLAIMS a direction —
  and two of three renders on 2026-08-12 got the claim wrong: a dehumidifier drew three blue
  arrows pointing UP AND OUT of its top, inverting what the machine does, and a heating pad
  drew amber arrows for heat, which nobody can see. The block is now the moving substance
  itself gathered into a directional form, direction is physical truth, the substance keeps
  its real colour, and the block is OMITTED when the product moves nothing visible — which
  is G8's rule about not inventing an effect, and which also retires the amber-for-good-heat
  collision with G3.
  **Zone names stop being single letters.** One render printed large circled A, B and C into
  the image. G6 bans letters and the avoid line carried `text`, yet it happened anyway,
  because the leak came from the slot NAMES: the prompt showed the model headings called
  ZONE A, ZONE B, ZONE C and the model drew them. The zones are HERO, ACTION and RAIL now.
  `06-relief-hero` still uses ZONE A/B/C and carries the same risk; flagged there for when
  that type is next opened rather than changed blind.
  **G7 now binds the hero out loud.** One render put a shower filter on a disembodied shower
  arm hovering over a bathroom sink, in a scene containing no shower — a product mounted to
  nothing, in a moment where it could not be working. G7's completeness test always covered
  this and the type never referenced it. The slot now requires the real mounting point,
  present and whole, with the product part of the scene rather than a cutout floating over
  it.
  Skeleton 1587 -> 2069 characters.
- 1.2 (2026-08-11): channels gain `landing-page` (the routing table already assumed
  it). Deliberately NOT advertorial: 03-spec-split's avoid_when sets the precedent
  that this infographic-tile aesthetic "signals cheap goods off-marketplace", and the
  rail shares that register. The advertorial cell is trimmed instead of widened.
- 1.1 (2026-08-10): vignette slot split into pain-gesture / visible-symptom modes
  (Test D exposed that a hard-coded "hand pressing" does not generalize); rail reduced
  to 3 vignettes; G1 block added; hero product slot rewritten to G2.
  seed: conversation.md.
- 1.0 (2026-08-10): initial as SQR-SCOPE-PAINRAIL from the office-chair exemplar;
  exemplar faults encoded (red arrows on product, 4 undersized vignettes, decorative
  S-curve). seed: conversation.md.

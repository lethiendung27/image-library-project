---
id: 02-symptom-rail
step: 2
job: symptom
device: rail
version: "1.5"
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
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 02-symptom-rail v1.5
LAYERS: photographic hero on the left, vignette rail down the right edge.

[PRODUCT REFERENCE] the attached photo is the exact reference.
[HERO] left 72%.                                          -> PARTS/hero
[RAIL] right 25-28%. Name the vignette mode.              -> PARTS/rail
[MARKS] name each one used, with its count:               -> MARKS
  required: symptom-glow
  then substance OR field — only if the product truly does it
  nothing in the frame is marked that is not named here
[STYLE]                                                   -> PARTS/style
```

## PARTS

**`hero`** — a photographic scene, not a product shot. `[age/gender]` in muted neutral
wardrobe, in the correct posture, doing an everyday activity, calm and content, gaze
named. Setting, three props, soft natural window light, background blurred, bright
high-key neutral grade, subject offset left.

The product is **part of the scene and actually working**, at its real mounting point with
the thing it mounts to present and whole (G7). Unobstructed, from a named angle, at least
a named share of the hero height. G7 always bound this layer and the type simply never
said so: one render put a shower filter on a disembodied shower arm over a bathroom sink,
in a scene containing no shower — a product mounted to nothing, in a moment when it could
not be working.

**`rail`** — a vertical band with a pale tint gradient panel and a straight or soft
S-curved left edge. Exactly **3** circular vignettes stacked evenly, white ring border,
equal diameter, generous spacing, sharing the hero's light and style (G5 — a stock-photo
rail on a lifestyle hero reads as two sources). Each vignette is a tight crop of the same
role of person or object, no face visible. Order follows anatomy top to bottom, or
severity; never shuffled. Three and not four: at mobile size a fourth drops below
legibility.

**`vignette mode`** — one, named explicitly in the prompt. `pain-gesture`: a hand pressing
the hurting zone, when the symptom is a feeling. `visible-symptom`: a visible manifestation
on body or object, when the symptom is a consequence you can see. Naming it matters because
the model regresses to pain-gesture unless told otherwise.

**`style`** — clean e-commerce infographic tile, bright and airy, sharp focus.

## MARKS

This type's own mark library, called by name from the skeleton. `also in` notes keep a
same-looking mark in another type visible from here.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `symptom-glow` | a soft radial glow centred on the symptom inside a vignette | red only | exactly 3, one per vignette | 4 renders · also in `01-pain-split` as hotspots |
| `substance` | the matter the product moves, gathered into a directional form and thinning where it disperses — the mark is MADE of that matter | the substance's own real colour, never red | N streams, on the product | 1 render |
| `field` | contour lines or a soft radiating envelope that WRAPS the receiving surface and shows which way the transfer runs | neutral warm-white or translucent, no signal colour | N contours, on the receiving surface | **none** |

**The mark shows what the product actually does, and its FORM follows the kind of thing
that is.** The test is not whether a camera could see it — it is whether the product
genuinely does it. Matter that moves gets a mark made of the matter. A field that transfers
gets contours or an envelope wrapping what receives it. Marking something the product does
not do stays forbidden, and that is the whole of what G8 asks.

Two failures wrote this rule. An abstract arrow "pointing" a direction is a CLAIM, and a
dehumidifier render drew three blue arrows pointing up and out of its top, inverting what
the machine does; a stream of droplets converging into an intake cannot point the wrong way
without looking absurd. Separately, v1.3 made the test visible-versus-invisible and told
writers to omit the block for anything unseeable — wrong, because heat is unseeable and also
real, and this library already marks invisible-but-real things (`02-cause-anatomy` draws an
arrow for force, `01-pain-split` draws hotspots for pain).

**`field` carries no signal colour.** The heating-pad render used amber, which collides with
G3, where orange means wrong heat. Read strictly, G3 would give blue for a working mechanism,
but blue heat fights the stronger prior that blue means cold. Letting the FORM carry the
meaning in neutral warm-white leaves G3 untouched instead of seeking an exemption from it —
the cheaper of two paths, and one the owner may want to revisit.

**`substance` must not read red.** Red belongs to the rail; a red stream on the product
reads as a heating feature.

## SLOT CONSTRAINTS
- **Zone names must never be single letters.** One render printed large circled A, B and C
  into the image: the prompt carried `ZONE A`, `ZONE B`, `ZONE C` as headings and the model
  drew the headings it was shown. G6 bans letters and the avoid line carried `text`, and it
  happened anyway, because the leak came from the slot NAMES. The zones are HERO, RAIL and
  MARKS. `06-relief-hero` still uses ZONE A/B/C and carries the same latent leak; fix it
  when that type is next opened.
- **The prompt budget** (lesson from `02-cause-anatomy`, 2026-08-13): a clause earns its
  place in a rendered prompt only if a render has failed without it. Everything else is a
  rule for the writer and stays in this file.
- The hero is the argument's calm half; the rail is its count. Neither may be cropped away.
- G5 binds hero and vignettes to one register; G7 binds the hero's mounting point.

## NEGATIVE
```
[G6] + letters, circled letters, zone labels, faces inside vignettes,
mismatched lighting between hero and vignettes, heat or warming cues,
cluttered background, dark grade, vignettes too small, overlapping circles,
floating product cutout, product mounted to nothing
```
This list is canonical and model-agnostic; the adapter drops from it at render time.
`red arrows on product` was dropped at v1.3 — with an arrow made of water or air the token
risked suppressing the stream itself, which is Rule 1a. `letters` and `circled letters` were
added after a render printed A, B and C into the frame. Note that `heat or warming cues`
becomes a Rule 1a bleed in any prompt whose `field` mark is heat, and must be dropped from
that prompt's avoid line rather than rephrased.

## WORKED EXAMPLES
(none rendered yet — the three renders of 2026-08-12 all predate v1.4 and every one of them
produced a rule rather than an example)

## KNOWN-FLAKY
- **The model regresses to pain-gesture** in the rail even when visible-symptom is intended.
  This is why the mode is named explicitly in the prompt.
- **Single-letter slot names leak into the image**, 1 observation — see SLOT CONSTRAINTS.

## NOTES
Distinction from `01-pain-split`: that type judges one problem in two states; this one
counts several problems around one product and proves none of them. They pair on a page,
and `02-symptom-rail` must come second, because a count reads as padding before a proof.

Open: `field` has no render evidence at all. Its first render is its founding evidence, and
the amber-versus-neutral question above is the thing to watch.

## CHANGELOG
Evidence for every entry is in `eval/render-tests.jsonl` and in the commit that made it;
git is the audit surface, so decisions are recorded here and workings are not.
- 1.5 (2026-08-13): **restructured into a call-map plus two libraries** (ADR-012), and the
  file compressed on the same shape `02-cause-anatomy` proved at 1.7. `PARTS` holds the
  non-mark building blocks (hero, rail, vignette mode, style); `MARKS` holds this type's
  three marks with form, colour, count and evidence status; the skeleton became a map naming
  them. The `[ACTION]` if/else is gone as a branch and lives as two named marks the writer
  calls, which is the point ADR-012 makes — a branch never reached the model anyway, since
  `query/runbook.md` Step 5 resolves it before shipping, so what a branch cost was
  correctness rather than context. Skeleton 2160 → 592 characters; the whole file shrank
  while every rule survived, because what left was the workings and those live in git.
  `symptom-glow` is named as a mark for the first time — it was always there, buried inside
  the rail block, uncounted and unowned.
- 1.4 (2026-08-12): **the visible-versus-invisible test was wrong; the test is whether the
  product actually does it.** Owner correction. The block now branches on the KIND of
  phenomenon: SUBSTANCE keeps the mark-made-of-the-matter rule, FIELD gets contours or a
  wrapping envelope in neutral warm-white. A field mark carries no signal colour, because
  the heating-pad render's amber collided with G3's orange-means-wrong-heat.
- 1.3 (2026-08-12): **the arrow is made of the substance the product moves, or there is no
  arrow.** Owner rule, after a dehumidifier render drew three blue arrows pointing up and
  out of its top, inverting what the machine does. Also: zone names stop being single
  letters, after a render printed circled A, B and C into the image; and G7 now binds the
  hero out loud, after a shower filter appeared on a disembodied arm in a room with no
  shower.
- 1.2 (2026-08-11): channels gain `landing-page` (the routing table already assumed it).
  Deliberately NOT advertorial: `03-spec-split`'s avoid_when sets the precedent that this
  infographic-tile aesthetic signals cheap goods off-marketplace, and the rail shares that
  register.
- 1.1 (2026-08-10): vignette slot split into pain-gesture / visible-symptom modes (Test D
  showed a hard-coded "hand pressing" does not generalise); rail reduced to 3 vignettes; G1
  block added; hero product slot rewritten to G2. seed: conversation.md.
- 1.0 (2026-08-10): initial as SQR-SCOPE-PAINRAIL from the office-chair exemplar; exemplar
  faults encoded (red arrows on product, 4 undersized vignettes, decorative S-curve).
  seed: conversation.md.

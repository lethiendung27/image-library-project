---
id: 02-symptom-rail
step: 2
job: symptom
device: rail
version: "1.12"
status: active
replaced_by: null
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

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 02-symptom-rail v1.12
LAYERS: photographic hero on the left, vignette rail down the right edge.

[PRODUCT REFERENCE] the attached photo is the exact reference.
[HERO] left 72%.                                          -> PARTS/hero
[RAIL] right 25-28%. Name the vignette mode.              -> PARTS/rail
[MARKS] name each one used, with its count:               -> MARKS
  required: symptom-glow
  then substance OR field — only if the product truly does it,
  and it must LAND on a zone the rail counts
  add transform when the product's benefit is the substance's QUALITY
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
| `symptom-glow` | a soft radial glow centred on the symptom inside a vignette | red only | exactly 3, one per vignette | 12 renders · also in `01-pain-split` as hotspots |
| `field` | contour lines or a soft radiating envelope that WRAPS the receiving surface and shows which way the transfer runs | neutral warm-white or translucent, no signal colour | N contours, on the receiving surface | 4 renders · vibration, support, heat, pressure |
| `substance` | the matter the product moves, gathered into a directional form and thinning where it disperses — the mark is MADE of that matter | the substance's own real colour, never red | N streams, on the product | 3 renders · shows presence and place only |
| `transform` | PROGRESS across one continuous surface or flow: the product sits ON the boundary, done behind it and not-yet-done ahead | the surface's own colour on both sides, differing only in how clean — no signal colour | one boundary, at the product's own edge | 2 of 6 · needs a boundary, never side-by-side containers |

**The mark shows what the product actually DOES, and its form follows the kind of thing that
is.** The test is not whether a camera could see it but whether the product genuinely does it.
Matter that moves gets a mark made of the matter; a field that transfers gets contours or an
envelope wrapping what receives it. Marking something the product does not do stays forbidden,
and that is the whole of what G8 asks.

**A field is not only heat.** `field` covers heat, SUPPORT, vibration and PRESSURE, so a
mattress topper, cushion, insole, brace or pillow is a `field` case and never a no-mark case.
Read narrowly the mark looks like it is only for machines; read as written it covers most of
the passive products this type routes.

**`field` carries no signal colour** — amber for good heat collides with G3, where orange means
wrong heat, and blue fights the stronger prior that blue means cold. Let the FORM carry the
meaning. **`substance` must not read red**: red belongs to the rail, and a red stream on the
product reads as a heating feature.

**The action mark must LAND where the rail complains.** Pre-flight test, the last thing before
a prompt ships: name the three zones the rail counts, name the zone the mark lands on, and if
it is not one of the three the frame does not join. Either the product moves to a counted zone
or the rail counts the zone the product treats.

**But it may never be drawn ARRIVING AT a symptom.** Where the product touches the body,
landing and treating are the same act and the mark reads as relief. Where it acts through the
air, a plume flying into a face beside a red-marked nostril reads as the product CAUSING the
symptom.

**`substance` is presence and place; `transform` is QUALITY.** A substance mark can say water
is here and falling on her hair; it cannot say what kind of water it is.

**`transform` must read as PROGRESS, not as two co-present states.** Put the product ON the
boundary of one continuous surface or flow: done behind, not-yet-done ahead, with the product
visibly the agent. Two containers side by side are two objects — nothing says one becomes the
other. **Never attach the dulled state to what the person RECEIVES**: it may sit in a sealed
housing, a tank, or a surface not yet reached, never in the hands, on the skin, or in the air
of the person using the product. **The rail should ECHO it** — give one vignette the same
object the hero shows transformed.

**A product whose output arrives everywhere at once cannot carry `transform` at all**, having
no container to judge and no boundary to cross. A shower filter is that case; so are the air
products, for the same reason.

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
- Before shipping: name the three rail zones, name where the action mark lands, and check
  that it is one of them — see MARKS.
- The reference product appears ONCE. One render drew two humidifiers in the same frame.
- **No face inside a vignette, and a nose or an eye in close crop IS a face.** Two vignettes
  in one render showed a nostril and an eye socket; both read as portrait fragments and both
  broke the rule the type has carried since 1.1.
- **A symptom is a discomfort, not an injury.** The same render drew a nostril raw and
  scarlet, which reads as a wound rather than as dry air. The rail counts what a buyer
  recognises in themselves, and nobody recognises themselves in a medical photograph.
- G5 binds hero and vignettes to one register; G7 binds the hero's mounting point.

## NEGATIVE
```
[G6] + letters, circled letters, zone labels, faces inside vignettes,
mismatched lighting between hero and vignettes, heat or warming cues,
cluttered background, dark grade, vignettes too small, overlapping circles,
floating product cutout, product mounted to nothing
```
**Measured 2026-08-13: this type's prompts carry NO avoid line at all.** The owner removed
`text, letters, circled letters, watermark, deformed hands, extra fingers` from a prompt set
by hand and re-rendered: no difference in the output. That is the earn-its-place test run
properly — a clause belongs in a prompt only if a render has failed without it, and this one
had never been tested in isolation because it was inherited by habit. The bounds it claimed
to hold are held elsewhere: G6 lives in the model's own behaviour on this register, and the
one render that ever printed letters did so because the SLOT NAMES were single letters, which
1.3 fixed at the source. Two consequences worth flagging rather than acting on alone: this
bears on adapter Rule 1 step 2, which assumes every prompt closes with an avoid sentence, and
on Rule 5, which mandates `deformed hands, extra fingers` wherever hands are close. Both are
global law and a parallel session is writing prompts against them right now, so the finding
goes to the owner rather than into the adapter from here.

The list below stays canonical and model-agnostic; **the adapter TRANSFORMS it at render time
and a prompt must never carry it verbatim.** Measured 2026-08-13: pasting this list straight into
three prompts produced 27 Rule 1a hits, because almost every token here qualifies a noun a
rendered prompt requires — `faces inside the vignettes` against a hero who has a face,
`mismatched lighting between hero and vignettes` against three nouns the prompt cannot do
without, `cluttered background` against a background, `dark grade` against a grade,
`overlapping circles` against the three circles that ARE the rail, `product mounted to
nothing` against the product itself. Every one of those bounds is asserted positively in the
skeleton already, which is exactly the case adapter Rule 1 step 1 says to drop. A rendered
avoid line for this type is usually G6's core — text, letters, circled letters, watermark —
plus the two hand descriptors Rule 5 mandates when hands are close.

`red arrows on product` was dropped at v1.3: with an arrow made of water or air the token
risked suppressing the stream itself. `letters` and `circled letters` were added after a
render printed A, B and C into the frame. `heat or warming cues` is a Rule 1a bleed in any
prompt whose `field` mark is heat, and is dropped from that prompt rather than rephrased.

## WORKED EXAMPLES
Two renders that happened, kept in full because that text is the only record of what actually
drew (SPEC §3.3). Both `pass` — an empty failures list — and between them they carry the two
marks this type took eleven versions to get right.

### example: heated-shoulder-wrap — skeleton@1.7, run: pass
The type's first pass. `field` on HEAT under the no-signal-colour rule that heat itself
produced at 1.4 and had never been tested against: warm-white contours over the shoulders and
neck, no orange, no amber, no red, landing on all three zones the rail counts.
```
TYPE: 02-symptom-rail v1.7
LAYERS: photographic hero on the left, vignette rail down the right edge.

PRODUCT REFERENCE: the attached photo is the exact reference for the heated
shoulder wrap. Preserve shape, proportions, material, finish and colour exactly.
It appears once in the frame.

HERO, left 72%: a woman in her forties in a soft grey lounge set, sitting
sideways on a sofa in the evening with a mug in both hands, calm and content,
gaze down into the mug. The reference wrap is worn over both shoulders and around
the base of her neck, sitting on her shoulders with its own weight and its strap
fastened at the front, part of the scene and in use, unobstructed, seen from the
side, at least 25% of the hero height. Setting: a warm living room, a folded
blanket, a floor lamp, a low table. Soft natural window light, background
blurred, bright high-key neutral grade, subject offset left.

RAIL, right 26%, soft S-curved left edge: pale clay gradient panel. Three
circular vignettes stacked evenly, white ring border, equal diameter, generous
spacing, sharing the hero's light and style. These are a DIFFERENT MOMENT from
the hero: the same woman earlier, at a laptop at her desk, in a work shirt, no
wrap. Vignette mode is pain-gesture, each a tight crop from the chest down or
from behind, no face and no part of a face in any of them. Top to bottom: her
hand reaching back to press the base of her neck; her hand pressing the top of
her shoulder; her hand pressing the upper back beside her spine.

MARKS, two, nothing else in the frame is marked:
- field: the heat the wrap transfers into her shoulders and neck, drawn as four
  thin contour lines that WRAP the shoulders and the base of the neck beneath the
  wrap, following the curve of the body, closest together where the wrap sits
  against her and loosening outward as they travel down toward the shoulder
  blades. Neutral warm-white and translucent, carrying no colour of its own -
  no orange, no amber, no red. Not an arrow, not a glow, not a haze.
- symptom-glow: one soft red radial glow centred on the aching zone inside each
  of the three vignettes, three in total.

STYLE: clean e-commerce infographic tile, bright and airy, sharp focus.
```

### example: cordless-vacuum — skeleton@1.10, run: pass
`transform` as PROGRESS, the form the type spent six versions finding. A cleaned strip behind
the head against matted pile ahead of it, the boundary along the head's own edge, so the
machine is visibly the agent and the dirty half reads as what is left to do.
```
TYPE: 02-symptom-rail v1.10
LAYERS: photographic hero on the left, vignette rail down the right edge.

PRODUCT REFERENCE: the attached photo is the exact reference for the cordless
vacuum. Preserve shape, proportions, material, finish and colour exactly. It
appears once in the frame.

HERO, left 72%: a man in his thirties in a plain olive tee, vacuuming a pale wool
rug, calm and content, gaze down at the rug ahead of the head. He holds the
reference vacuum with its floor head flat on the rug and the rug and floor
present and whole beneath it, part of the scene and running, unobstructed, seen
from the side, at least 25% of the hero height. Setting: a bright living room, a
low sofa, a floor plant, a stack of books. Soft natural window light, background
blurred, bright high-key neutral grade, subject offset left.

RAIL, right 26%, soft S-curved left edge: pale stone gradient panel. Three
circular vignettes stacked evenly, white ring border, equal diameter, generous
spacing, sharing the hero's light and style. These are a DIFFERENT MOMENT from
the hero: the same home before cleaning, with no person in any of them. Vignette
mode is visible-symptom, each a tight crop of an object. Top to bottom: the same
pale wool rug, its pile dulled grey and matted with settled dust; pet hair worked
deep into the weave of a sofa cushion; crumbs and grit in the seam of a car seat.

MARKS, two, nothing else in the frame is marked:
- transform: two bodies of the SAME RUG SURFACE in one frame, meeting at the
  cleaning head, differing only in how clean they are. BEHIND the head, a broad
  strip of rug the machine has already passed over - pale, bright, its pile
  lifted and even. AHEAD of the head, the untouched rug - the same wool dulled
  grey, its pile flattened and dust settled in it. The boundary between them runs
  straight along the edge of the head. No loose dust anywhere in the air or the
  room.
- symptom-glow: one soft red radial glow centred on the symptom inside each of
  the three vignettes, three in total.

STYLE: clean e-commerce infographic tile, bright and airy, sharp focus.
```

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
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.12 (2026-08-13): type passed by the owner; file finalised with two rendered worked
  examples in full text per SPEC §3.3 — the heated shoulder wrap for `field` and the cordless
  vacuum for `transform`. Closing state: four marks, all with render evidence; `field` the
  best-evidenced at 4 renders across vibration, support, heat and pressure. Air products and
  the shower filter are excluded by the locatable-effect test.
- 1.11 (2026-08-13): `transform` is PROGRESS, not co-presence — the product sits ON the
  boundary of one continuous surface, done behind and not-yet ahead, and the dulled state never
  attaches to what the person receives. A product whose output arrives everywhere at once
  cannot carry the mark at all. 3 records, 1 pass. `46418c9`
- 1.10 (2026-08-13): `transform` needs two judgeable bodies, and the rail should echo it.
  3 records, 1 pass. `7b396c2`
- 1.9 (2026-08-13): `transform` added — the mark of QUALITY, after `substance` proved able to
  show that water arrives but not what kind it is. 2 records, 1 pass. `0d065cf`
- 1.8 (2026-08-13): a locatable effect becomes an admission test; air products leave the type,
  and a `substance` mark may only draw matter the product ADDS. 3 records, 1 pass. `e8a4fdf`
- 1.7 (2026-08-13): the mark may not be drawn arriving at a symptom, and the rail is a
  DIFFERENT MOMENT from the hero. Prompts stop carrying an avoid line, measured. 2 records.
  `9435cda`
- 1.6 (2026-08-13): the action mark must land where the rail complains, as a pre-flight test.
  `field` covers support and pressure, not only heat. `92cb123`
- 1.5 (2026-08-13): restructured into a call-map plus PARTS and MARKS (ADR-012); skeleton
  2161 → 592. `symptom-glow` named as a mark for the first time. `3d660f0`
- 1.4 (2026-08-12): the test is whether the product actually does it, not whether a camera
  could see it. SUBSTANCE and FIELD split on the kind of phenomenon; a field mark carries no
  signal colour. `4fd7641`
- 1.3 (2026-08-12): the arrow is made of the substance the product moves, or there is no
  arrow. Zone names stop being single letters; G7 binds the hero out loud. `9aa1de1`
- 1.2 (2026-08-11): channels gain `landing-page`. Deliberately not advertorial — the
  infographic-tile register signals cheap goods off-marketplace, per `03-spec-split`.
- 1.1 (2026-08-10): vignette slot split into pain-gesture / visible-symptom modes; rail reduced
  to 3 vignettes; G1 block added; hero product slot rewritten to G2. seed: conversation.md.
- 1.0 (2026-08-10): initial as SQR-SCOPE-PAINRAIL from the office-chair exemplar; exemplar
  faults encoded. seed: conversation.md.

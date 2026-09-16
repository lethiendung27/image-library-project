---
id: 02-symptom-rail
step: 2
job: symptom
device: rail
version: "1.13"
status: active
replaced_by: null
channels: [marketplace, landing-page]
requires_product_photo: true
generation_mode: single-pass
variants: []
exempt_from: []
pairs_with: [01-pain-split, 03-mechanism-ghostbody]
never_with: []
text_layer: [title]
copied_from: 02-symptom-rail
copied_at_version: "1.12"
blocked_by: null
---

# 02-symptom-rail

## PURPOSE
One product, many problems: a calm hero scene plus a vertical rail of symptom vignettes.
Argues by breadth of the problem — it does not prove, it counts.

**Copied verbatim from `registry/types/02-symptom-rail.md` at version 1.12** (owner instruction, 2026-09-15, ADR-091: each page kind routes ONE folder, and that folder holds every type the page may use). Every section below is that file's text at commit `3cabeab`, spliced by script rather than retyped. `copied_at_version` is what makes the copy auditable: `scripts/validate.py` warns when the parent moves past it. Not copied: the parent's WORKED EXAMPLES, whose prompt text is the record of renders that were the parent's, and its CHANGELOG, which is the parent's own evidence trail. Where a clause below cites renders or a corpus, those were LP1's; `registry/pdp-dr-instruction.md` binds this file as it binds every file in the folder.

## LP2 LAW
Added 2026-09-16 (ADR-094): the owner's gallery instruction for Problem Tile · Symptom Rail. This section is
this copy's own and a re-copy keeps it; `registry/pdp-dr-instruction.md` binds the rest.

- **The words.** A title, and one SYMPTOM label of 1–2 words beside each vignette — **never
  "relief"**, which names the product's job instead of the reader's complaint. No copy. The
  message is the coverage, and the three vignettes are its proof.
- **The vignettes are photographs.** Three circles of equal diameter, each in a thin WHITE ring —
  the set's accent never on a ring — with no x-ray, skeleton or rendered overlay inside, on a
  pale tinted panel with a straight or soft-S left edge. The owner's three rail renders broke
  this three ways: rectangles with a pelvis x-ray in one of them; rendered skeletons inside
  accent-blue rings; a label reading "Tailbone Relief".
- **The hero is calm, and the product is WORKING in it** — PARTS/hero already says so. The one
  rail render that met every form rule set a frowning woman in the hero, brushing with the
  product, which argues that the product is the struggle.
- **Marks:** one soft red glow per vignette — a discomfort, never an injury.
- **Place:** image 2 or 3, after any split.

Slots an LP2 prompt adds to the SKELETON above:
```
[TITLE]   the coverage, 2–5 words.                  -> LP2 LAW
[LABELS]  one 1–2 word symptom beside each vignette. -> LP2 LAW
```

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
- 1.13 (2026-09-16): `LP2 LAW` added: the owner's gallery instruction for this type — a title and three symptom labels, photographic vignettes in white rings with no overlay, and the three ways its three rail renders broke that. `text_layer` declared. First LP2 edit; `copied_at_version` stays 1.12. ADR-094.
- 1.12 (2026-09-15): copied verbatim from `registry/types/02-symptom-rail.md` at 1.12, commit `3cabeab` — owner instruction, ADR-091. Every section except WORKED EXAMPLES and CHANGELOG is that file's text. The version is the parent's; this file's own edits bump it from here.

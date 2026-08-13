---
id: 02-symptom-rail
step: 2
job: symptom
device: rail
version: "1.11"
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
  main image. Not when the symptoms cannot be photographed, and **not when the
  product's effect has no location you can point at** — an air purifier, a
  humidifier, a diffuser change the medium rather than a body zone, and no mark
  can show a medium changing. Route those to a mechanism type instead.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 02-symptom-rail v1.11
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
| `symptom-glow` | a soft radial glow centred on the symptom inside a vignette | red only | exactly 3, one per vignette | 4 renders · also in `01-pain-split` as hotspots |
| `substance` | the matter the product moves, gathered into a directional form and thinning where it disperses — the mark is MADE of that matter | the substance's own real colour, never red | N streams, on the product | 3 renders · shows presence and place only |
| `transform` | PROGRESS across one continuous surface or flow: the product sits ON the boundary, done behind it and not-yet-done ahead | the substance or surface's own real colour on both sides, differing only in how clean — no signal colour | one boundary, at the product's own edge | 2 of 6 · needs a boundary, never two side-by-side containers |
| `field` | contour lines or a soft radiating envelope that WRAPS the receiving surface and shows which way the transfer runs | neutral warm-white or translucent, no signal colour | N contours, on the receiving surface | 2 renders · works on powered AND passive products |

**A field is not only heat.** `field` covers heat, SUPPORT, vibration and PRESSURE, so a
mattress topper, a cushion, an insole, a brace or a pillow is a `field` case and never a
no-mark case: it transfers support into the body and that transfer is what the buyer is
paying for. Read narrowly, this mark looks like it is only for machines; read as written, it
covers most of the passive products this type routes. Two renders were spent on a topper
prompt that declared it had no field at all.

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

**`substance` is a mark of presence and place. `transform` is the mark of QUALITY.** The
filtered-shower render is why this distinction exists: the water arrived, it landed on the
hair the rail complained about, and a plain shower head would have produced an identical
stream. Filtration is the whole benefit and nothing in the frame carried it. A substance mark
can say water is here and falling on her; it cannot say what kind of water it is.

**`transform` must read as PROGRESS, not as two co-present states.** This is the owner's
finding and it supersedes the two-bodies wording below, which was the right observation with
the wrong cause. The vacuum works because a pale cleaned strip lies behind the head against
matted pile ahead of it and the boundary runs along the head's own edge — the machine is
visibly the agent, the dirty half is what is LEFT TO DO, and direction is unambiguous. The
floor washer failed with the same substance and the same product class because two tanks side
by side are two objects: nothing says one becomes the other.

So: **put the product ON the boundary of one continuous surface or one continuous flow.** Done
behind, not-yet-done ahead. That is what the tap did too — the flow ran down through the
housing into the glass, so before and after lay along one path with the filter between them.

**And never attach the dulled state to what the person RECEIVES.** The shower render pooled
unclear water in the woman's cupped hands while the rail showed the same hands holding cloudy
water: it reads as bathing in dirty water, whatever the prompt says. A dirty body may sit in a
sealed housing, in a tank, or on a surface not yet reached. It may never sit in the hands, on
the skin, or in the air of the person using the product.

**A product whose output arrives everywhere at once cannot carry this mark at all** — no
container to judge, no boundary to cross, and the only available body belongs to the person
being treated. A shower filter is that case, confirmed over three renders and three different
failures, and it is the same class as the air products for the same reason.

The earlier wording, kept because the observation under it still holds: Three renders decided this in
one batch: the tap worked and the shower and the vacuum failed, and the difference is not
wording. The tap put a dulled grey column inside a transparent housing and a crystal-clear
column falling into a held glass — two volumes with edges, side by side, judgeable by eye. The
shower's output was a SPRAY, and a fine stream has no body to look through, so clarity had
nowhere to live. The vacuum's flowing substance was AIR, which has no body at all, and its
trap rendered empty.

So the test before using this mark: **name the two bodies.** If you cannot point at two
volumes or two surfaces of the same substance that a viewer can compare in one frame, the mark
will not render, whatever the prompt says. A glass beside a housing. A dirty-water tank beside
a clean-water tank. A cleaned strip of floor beside an untouched one. Where a product's output
is a spray or a gas, find the body elsewhere — hands cupped under the water, a tank, a treated
surface — or accept that the mark does not apply.

**The rail should ECHO the transform.** Undesigned and probably half the reason the tap render
lands: its middle vignette is a drinking glass dulled with cloudy film while the hero's hand
holds a clear one. The same object in its bad state and its good state, across the two halves
of the image. When a type carries `transform`, give one vignette the object the hero shows
transformed.

`transform` shows the change at the one place it happens — at or from the product. This is also the ONLY place this type permits drawing matter the product removes:
sediment inside a filter housing reads as CAUGHT, whereas the same sediment loose in the room
reads as dirt, which is what ruined the purifier render. Keep the clouded half inside the
housing or at the inlet and let the outlet run clear; never let the before-state spread into
the scene.

It follows that a product whose transformation happens inside an OPAQUE body — an air
purifier, most water softeners — still cannot use this mark and still fails the locatable
test. The transformation has to be visible at the product, not merely true of it.

**`substance` must not read red.** Red belongs to the rail; a red stream on the product
reads as a heating feature.

**THE ACTION MARK MUST LAND WHERE THE RAIL COMPLAINS.** Owner decision, 2026-08-13. Both
action marks answer what the product EMITS and neither answers where that arrives, so an
image can show a product working and a rail counting pains and never join the two — which is
what four renders did. The frame then states a problem and stands a product beside it.

The test is checkable, and it is the last thing to run before a prompt ships. Name the three
zones the rail counts. Name the zone the action mark lands on. **If that zone is not one of
the three, the frame does not join and the prompt is not ready.** The massage-gun render
fails it outright: the contours wrapped the thigh while the rail counted shoulder, knee and
calf, so the product was drawn treating a zone the image never claimed hurt. Either the
product moves to a counted zone or the rail counts the zone the product treats — both are
legitimate, and choosing is the writer's job.

**But the mark may never be drawn ARRIVING AT a symptom.** The rule above has one failure
mode and the owner found it on its first outing. Where the product touches the body, landing
and treating are the same act — a gun head on a shoulder, foam under a hip — and the mark
reads as relief. Where the product acts through the air, a plume drawn flying INTO a face
beside a rail showing a raw red nostril reads as the product CAUSING the symptom. His words:
it looks like she breathes the oil in and then her nose, throat and face hurt.

So for an airborne product the substance fills the air the person is IN, as an ambient state,
and is not aimed at a body part the rail has marked red.

**The rail is a DIFFERENT MOMENT from the hero.** This was never stated and every render has
had rail and hero as the same person in the same setting. It survived only by accident: in
the renders that read correctly the vignette person is in a different posture — pressing a
sore shoulder, gripping a back — which carries "this is my ongoing problem" on its own. The
diffuser's vignettes were static close-ups of skin in the same room in the same moment, so
nothing said BEFORE and the eye supplied AFTER. Give the vignettes a different context:
another room, another time of day, dressed differently. The hero is life with the product;
the rail is life without it.

**A LOCATABLE EFFECT IS AN ADMISSION TEST, and it is the one this type failed three times.**
Point at where the product's effect arrives. If you can — a shoulder under a heated wrap, a
hip sunk into foam, a calf under compression — the mark occupies that place and the image
needs no prior knowledge from the viewer. If you cannot, no wording saves it. Three renders
across three different wordings proved that: the vapour aimed at her face read as causation,
the vapour filling the room read as nothing, and both were obeying their instructions
exactly. An air product's effect is everywhere and nowhere, and the viewer has to already
know that vapour in a room relieves a dry throat — which is the one thing an image must not
require.

**A `substance` mark may only draw matter the product ADDS.** The purifier render is the
proof: dust motes thickening toward the intake rendered faithfully, and the result is a room
that looks dirty beside a man and his dog. The more honest the mark, the worse the frame
looks. Matter a product takes away has no positive form, so a removal product gets no
substance mark — and, by the test above, usually does not belong in this type at all.

**Products that act on the environment rather than on the body** — a diffuser, a humidifier,
an air purifier — pass the test differently. Their `substance` must travel TOWARD the person
rather than dispersing into empty room air, and the rail must count symptoms that the
environment causes: a dry throat, a stuffy nose, dry skin. The humidifier render failed on
both halves at once, sending mist up into the room while the rail counted a cracked heel.

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
- 1.11 (2026-08-13): **`transform` is PROGRESS, not co-presence.** Owner finding, and it
  supersedes 1.10's two-bodies wording — the right observation with the wrong cause. Three
  renders: the vacuum passed, the floor washer and the shower failed.
  The vacuum works because a pale cleaned strip lies behind the head against matted pile ahead
  of it, with the boundary along the head's own edge: the machine is visibly the agent, the
  dirty half is what is LEFT TO DO, and direction is unambiguous. The floor washer failed with
  the same substance and the same product class, because two tanks side by side are two
  objects and nothing says one becomes the other. So the product goes ON the boundary of one
  continuous surface or flow — which is what the tap did too, the flow running down through
  the housing into the glass with the filter between.
  Second clause, from the shower: **never attach the dulled state to what the person
  RECEIVES.** Unclear water pooled in her cupped hands, with the rail showing the same hands
  holding cloudy water, reads as bathing in dirty water whatever the prompt says. A dirty body
  may sit in a sealed housing, a tank, or a surface not yet reached — never in the hands, on
  the skin, or in the air of the person using the product.
  Third: **a product whose output arrives everywhere at once cannot carry this mark.** No
  container, no boundary, and the only body available belongs to the person being treated. The
  shower filter is that case across three renders and three different failures, and it is the
  same class as the air products for the same reason. Recorded so it is not attempted a fourth
  time.
- 1.10 (2026-08-13): **`transform` needs two BODIES.** Three renders in one batch settled it,
  the owner confirming the tap as the one that works: a dulled grey column inside a transparent
  housing beside a crystal-clear column falling into a held glass — two volumes with edges,
  comparable by eye. The shower failed because its output is a SPRAY and a fine stream has no
  body to look through; the vacuum failed because its substance is AIR, which has no body at
  all, and its trap rendered empty. Wording was identical in shape across all three, so the
  form of the substance is the variable. Pre-flight test added: name the two bodies, and if you
  cannot point at two volumes or surfaces a viewer can compare in one frame, the mark will not
  render. This also closes the extension question 1.9 left open — `transform` does NOT stretch
  to cover a visible trap alone.
  Second finding, undesigned: **the rail should ECHO the transform.** The tap render's middle
  vignette is a glass dulled with cloudy film while the hero holds a clear one — the same
  object in both states across the two halves of the image, which is probably half of why it
  reads. When a type carries `transform`, give one vignette the object the hero shows
  transformed.
- 1.9 (2026-08-13): **`transform` added — the mark of QUALITY.** Owner report: there is no
  mark for showing the water is clean and clear. He is right, and the filtered-shower render
  is the clean proof: the water arrived, landed on the hair the rail counts, and a plain
  shower head would have produced an identical stream. `substance` is a mark of PRESENCE AND
  PLACE; purity is a quality of the substance and the library had no instrument for a quality.
  `transform` shows the change where it happens — a short before-and-after along the flow at
  the product's own housing or outlet, dulled or speckled entering and glass-clear leaving,
  the substance's real colour on both sides differing only in clarity. This is also the only
  place the type permits drawing matter the product REMOVES: sediment inside a filter housing
  reads as caught, while the same sediment loose in a room reads as dirt and ruined the
  purifier render. It follows that a product transforming inside an opaque body still fails
  the locatable test, since the change must be visible at the product and not merely true.
  Evidence in the same batch: two records, one `partial` and the type's **second `pass`** —
  the compression sleeves, where `field` on PRESSURE read as graduated squeeze without an
  arrow. `field` now has four renders across vibration, support, heat and pressure and is the
  best-evidenced mark this type owns.
- 1.8 (2026-08-13): **a locatable effect becomes an admission test, and this type stops
  taking air products.** Evidence: three records at ts 2026-08-13 — one `pass`, two `fail`.
  Owner report after the third attempt: the purifier and diffuser images still do not express
  what the product does.
  Every 1.7 fix worked and the images were still empty, which is the cleanest possible proof
  that the fault was never the wording. Point at where the effect arrives: if you can, the
  mark occupies that place and no prior knowledge is required of the viewer; if you cannot,
  nothing saves it. An air product changes the medium, which is everywhere and nowhere. That
  clause is now in `avoid_when`, and such products should route to a mechanism type.
  Second rule from the same batch: **a `substance` mark may only draw matter the product
  ADDS.** Dust thickening toward an intake rendered faithfully and made the room look dirty —
  the more honest the mark, the worse the frame. Matter a product removes has no positive
  form, which also explains the dehumidifier that started this line.
  My error, recorded: an aroma diffuser was the wrong product for this type on its own
  `avoid_when` — scent and mood is ONE problem and the rail becomes padding — and the symptom
  list I gave it was a humidifier's argument. Two products conflated, three renders spent.
  **First `pass` this type has earned**: the heated shoulder wrap, with `field` on HEAT under
  the no-signal-colour rule that heat itself produced at 1.4 and had never been tested against.
- 1.7 (2026-08-13): **the mark must not be drawn arriving at a symptom, and the rail is a
  different moment.** Two owner findings on the 1.6 set.
  The landing rule added at 1.6 has one failure mode and the first render found it. Where the
  product touches the body, landing and treating are the same act and the mark reads as
  relief. Where it acts through the air, a plume flying INTO a face beside a rail showing a
  raw red nostril reads as the product CAUSING the symptom — the owner's reading was that she
  breathes the oil in and then her nose, throat and face hurt. So an airborne substance now
  fills the air the person is in rather than aiming at a marked body part.
  Underneath that sits something the type never said: **the rail is a different moment from
  the hero.** Every render has had both as the same person in the same room, and it survived
  only because the vignette person was usually in a different posture, which carries "ongoing
  problem" by itself. The diffuser's vignettes were static skin close-ups in the same room in
  the same moment, so nothing said BEFORE and the eye supplied AFTER.
  **The avoid line is gone from this type's prompts**, measured rather than argued: the owner
  removed it by hand and re-rendered with no difference. It had never been tested in isolation
  because it was inherited by habit. Flagged, not acted on: this bears on adapter Rule 1 step
  2 and Rule 5, which are global law with a parallel session writing against them.
  Also: a nose or an eye in close crop IS a face inside a vignette; and a symptom is a
  discomfort, not an injury — a scarlet raw nostril reads as a wound, and nobody recognises
  themselves in a medical photograph. `field` reaches 2 renders and now works on a passive
  product as well as a powered one: white contours wrapped a sleeping body at shoulder and
  hip, the three zones the rail counted.
- 1.6 (2026-08-13): **the action mark must land where the rail complains.** Owner decision
  after four renders in which the hero's mark and the rail's symptoms never met — contours on
  a thigh while the rail counted shoulder, knee and calf; mist into empty room air while the
  rail counted a cracked heel. Both action marks answer what the product emits and neither
  answered where it arrives, so the frame stated a problem and stood a product beside it. The
  rule is a checkable pre-flight test rather than a new mark: name the three rail zones, name
  where the mark lands, and if it is not one of them the prompt is not ready. Products acting
  on the environment pass it differently — the substance travels toward the person and the
  rail counts what the environment causes.
  Also corrected: `field` covers heat, SUPPORT, vibration and PRESSURE, so a topper, cushion,
  insole, brace or pillow is a `field` case and never a no-mark case. Reading it as machines-
  only cost two renders on a prompt that declared a mattress topper had no field at all.
  `field` gains its founding evidence in the same batch and it is positive: warm-white
  contours wrapping the thigh around the massage-gun head, carrying no signal colour, exactly
  as v1.4 specified. Added to SLOT CONSTRAINTS: the reference product appears once, after a
  render drew two humidifiers.
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

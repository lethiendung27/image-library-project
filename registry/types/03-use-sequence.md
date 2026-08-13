---
id: 03-use-sequence
step: 3
job: use
device: sequence
version: "1.7"
status: active
replaced_by: null
ratios: ["3:4", "1:1"]
channels: [marketplace, landing-page, advertorial]
requires_product_photo: true
generation_mode: single-pass
axes:
  camera_lock: [handheld]
variants: []
exempt_from: [G3, G4]
pairs_with: [03-mechanism-ghostbody]
never_with: []
---

# 03-use-sequence

## PURPOSE
Reassure about operation: three stacked panels, one action each, read by action logic
alone — nothing in the frame numbers the steps or points from one panel to the next.
Answers "can I actually use this?" without looking like an instruction manual.

## TRIGGER
use_when: >
  The product has more than one operation step, or buyers may assume it is
  complicated. Image 4-5 in the gallery. Answers the question "will I manage to
  use this".
avoid_when: >
  The product has one obvious action. Never as a main image, never as a
  scroll-stopper.

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 03-use-sequence v1.7
REGISTER: a real home, close range, available light.          -> PARTS/register

[PRODUCT REFERENCE] the attached photo is the exact reference, in every panel.
[LAYOUT] three panels stacked, thin white gutters.            -> PARTS/layout
[CONTINUITY] one pair of hands, one place, one light.         -> PARTS/continuity
[PANELS] prepare, then use, then result.                      -> PARTS/panels
[ENVIRONMENT] one ordinary room, named once.                  -> PARTS/environment
[MARKS] emission only, in the USE panel, if the product     -> MARKS
        visibly emits. Nothing is ever drawn over the photo.
```

## PARTS

**`register`** — a real home photographed plainly at close range, on available light, with
ordinary surfaces and nothing propped or colour-matched. Not a diagram and not a manual.

**The look is not fixed, and fixing it is how this type produced slop.** Sixteen renders came
back as one beige room in one soft light because `register` prescribed a warm neutral palette
and every prompt repeated it: in a single four-prompt set, "warm neutral palette" appears 4
times and "soft daylight" 8. The register fixes the KIND of photograph. The home, the palette,
the light and the person are chosen per prompt, and **two prompts in one set may not share
them** — a set that comes back as one look is a fault in the set, not in the model.

**`layout`** — three photographs stacked one above another, filling the whole image, thin white
gutters, no outer border, and no panel other than those three. **Never describe the frame's
shape or ratio**: the owner sets the ratio at render time, and a prompt that reasons about frame
geometry leaves the model space to reconcile, and it fills that space with extra small panels.

**No numbers, no step markers, no text of any kind, and nothing that points from one panel to
another.** The order is read from the actions themselves, which is this type's entire discipline.

**`continuity`** — the make-or-break. The SAME hands in every panel: same skin tone, same
nails, same wrists, same sleeves. The same subject or surface throughout. **One palette and one
light direction held across all three panels — whichever palette and light this image was
given.** Continuity governs sameness INSIDE one image; `register` governs difference BETWEEN
images, and confusing the two is what produced sixteen identical rooms. Get continuity wrong
and the image reads as three stock photos rather than one sequence.

Camera distance and framing may shift naturally between panels — the `camera_lock: handheld`
axis is definitional here, because pixel-locked framing would read as renders rather than as
someone's hands.

**`panels`** — one action per panel, never two. The original exemplar packed two actions into
its first panel and lost a beat.

- **PREPARE**: the single setup action, hands in frame, and the readiness signal visible — an
  indicator light, an opened part, a loaded state.
- **USE**: the core action in progress, mid-motion.
- **RESULT**: the action finishing, plus a second hand or gesture expressing the outcome.
  Warmer light than the previous panels, and **no new mechanics** — this panel closes on the
  relationship, not on more machinery, which is what separates the type from a dry manual.

The product sits near the centre of every panel and is never cropped out.

**These three names are the type file's vocabulary and never reach the model.** A prompt that
carried `PANEL 1, PREPARE:` as a heading had PREPARE, USE and RESULT printed in white capitals
into the frame — adapter Rule 1b, now measured on a third type. Describe each panel in prose:
the top panel, the middle panel, the bottom panel. The whole-image headings shipped in that
same prompt and were not drawn, so what leaks is a name attached to a REGION of the frame, not
capitals as such.

**If the closing action removes a part from the product, the panel must describe the product
without that part.** Asked for a catch jar poured into a filter and told nothing about the
grinder it came off, the model duplicated the jar in one run and dropped the grinder in the
other. 2 of 2. Setting the WHOLE product down needs no such wording — proven on the steamer and
on both wine-opener runs.

**Any part of the product whose state visibly changes must be named in every panel, including
the one where it is still empty.** `continuity` declares hands, place and light identical
across the three panels and the model extends that to the product's own state: a cork named
only in the middle panel was already inside the opener's window in the first, so the first two
panels showed one state and the middle beat was empty. 2 of 2.

**`environment`** — one ordinary domestic setting with one or two incidental details, named
once and identical in all three panels.

## MARKS

**No mark here may carry the reading order.** Every other step-3 type argues with graphic
marks; this one argues with actions in sequence, and a step number or an arrow running between
panels would turn it into the instruction manual its PURPOSE exists to avoid. What a mark may
do is state, inside one panel, something the action alone leaves ambiguous. **One entry,**
and the second was cut on evidence rather than never tried — see below.

| name | form | colour | count | evidence |
|---|---|---|---|---|
| `emission` | whatever the product visibly puts out — spray, steam, light, foam — lit so it reads, made of the substance itself | the substance's own real colour | 1, in the USE panel only | 7/7 — steam, foam, a water jet, falling ground pepper |

**`fit` is cut at 1.7, 0 of 8.** It was tried in the gap beside the junction and then respecified
onto the contact line; the second form placed correctly once, as a hairline that ran past the
junction and vanished at full size, and was absent entirely the other time. The owner's verdict
across both attempts: the marks either do not appear or cannot be seen.

**What the eight renders actually say is a rule about form, not about this one mark.** In this
register a mark made OF something physically in the scene renders every time — `emission` is 7
for 7 across steam, foam, a water jet and falling ground pepper. A mark DRAWN over the
photograph, small and at a junction, rendered usably 0 times in 8. A11 in
`registry/argument-faults.md` says drawn geometry does read in a photographic register, and it
still holds: its evidence is `01-pain-scene`, where the drawn marks were rings and glows sized
to the frame. The refinement this type pays for is scale — a drawn mark the size of a seam is
below what survives. **If this type needs to say how a thing fits, the action has to say it:
hands seating the part, in contact, with nothing drawn.**

**`emission` exists only if the product genuinely emits** (G8). It is not a mark laid over the
photograph; it is a real thing in the scene, lit to be visible. Never invent an emission so a
panel looks active — G8's whole subject is not faking an effect so a PHOTO looks like it is
working, and a photographic register is where that is easiest to do and hardest to forgive.

The type is `exempt_from: [G3, G4]`: no signal colours, no correct-versus-wrong grading. There
is no wrong state here at all — nobody is doing it badly, because the argument is "this is
easy", not "this is better".

## SLOT CONSTRAINTS
- **The prompt budget is this type's hardest constraint, and length is what breaks the layout.**
  Measured across four sets into the same renderer: 1533 characters average and the stack held
  4 of 6; 2054 and it held 1 of 8; 2296, 1 of 8; 2368, 1 of 4. The last set rendered into
  1200x896, the identical frame the first set used, so the frame is not the variable — the
  wording is. Every clause added to fix a content fault was paid for out of the layout. **Keep a
  rendered prompt under about 1500 characters**, and when a new clause is earned, find its cost
  somewhere else in the prompt rather than appending it.
- A clause earns its place only if a render has failed without it, and is removed only once a
  render has done without it and come back correct (ADR-013, ADR-015).
- One action per panel; the order readable without numbering.
- Continuity of hands before everything else.
- **Hands at close range are this type's highest model risk** — adapter Rule 5 names hands as
  the worst failure class in the library, and every panel here is hands. Expect retries.

## NEGATIVE
```
[G6] + step numbers, arrows carrying the reading order, arrows between panels,
badges, different hands between panels,
different subject between panels, two actions in one panel,
product off-center, product cropped out, instruction manual look,
technical diagram, cold clinical lighting, different location between panels,
inconsistent palette, staged perfection
```
Canonical and model-agnostic; the adapter transforms it and no avoid line ships (ADR-014).

## WORKED EXAMPLES
### example: shower-filter-install — skeleton@1.0, run: untested
Product: metal shower filter · ratio 1:1 · camera_lock=handheld
- CONTINUITY — the same pair of hands throughout, the same chrome shower arm and white tiled
  wall, soft daylight from the left
- PREPARE — both hands unscrewing the existing shower head, the bare threaded arm visible
- USE — one hand holding the reference filter to the thread, the other turning it, mid-motion
- RESULT — filter fitted, water running in a clean even spray backlit so the streams read; one
  hand held open under the flow, palm up; warmer light
- ENVIRONMENT — ordinary home bathroom, a folded towel, a plant on the sill
Predicted failures: close-range hands on hardware, the library's highest extra-finger risk;
and a RESULT panel asked for both a visible result and a centred product, which compete for
space — if it breaks, choose one. The second prediction was confirmed on the grinder before
this example was ever rendered; see `panels`.

### example: garment-steamer-shirt — skeleton@1.2, run: partial
Product: handheld garment steamer · ratio param 4:5 · camera_lock=handheld
Kept in full because it is this type's founding `emission` evidence and the ledger stores
verdicts, not prompts. **Do not copy the panel headings** — they are the Rule 1b fault `panels`
now bans, and the sibling run of this same text printed them into the frame.

```
TYPE: 03-use-sequence v1.2
REGISTER: warm lifestyle photography, close range, natural and unstyled, soft
daylight.

PRODUCT REFERENCE: the attached photo is the exact reference for the handheld
garment steamer, in every panel. Preserve shape, proportions, material, finish and
colour exactly.

LAYOUT: three horizontal panels stacked vertically, thin white gutters, no outer
border.

CONTINUITY: the SAME pair of hands in all three panels - same skin tone, same
nails, same wrists, same rolled sleeves. The same pale blue linen shirt hanging on
the same wooden rail throughout. The same warm neutral palette and the same soft
daylight from the left in every panel. Camera distance and framing shift naturally
between panels.

PANEL 1, PREPARE: both hands twisting the filled water tank back onto the body of
the steamer, the tank's water level visible through it.
PANEL 2, USE: one hand holding the shirt taut by its hem, the other drawing the
steamer head upward across the fabric, mid-motion.
PANEL 3, RESULT: the steamer lowered and held at rest in one hand, the other hand
running flat down the now-smooth shirt panel. Warmer light than the panels above,
and no new mechanics.

The steamer sits near the centre of every panel and is never cropped out.

MARK, one, in PANEL 2 only: emission - real steam leaving the steamer head into
the fabric, backlit from the left so the plume reads clearly against the shirt. It
is steam in the room, not a graphic.

ENVIRONMENT: an ordinary bedroom corner, a woven basket on the floor, a folded
towel over the rail. The same location in all three panels.
```
Held: the stack, the gutters, one pair of hands across all three panels, one room, one light
direction, a warmer close, and `emission` as real backlit steam in the middle panel only, twice.
Broke: the run above printed the three beat names into the frame; this run did not, so the leak
is intermittent. This run also cropped the steamer to its water tank in the opening panel and
parked it at the far left edge of the closing one, against the centred-and-uncropped rule.

## KNOWN-FLAKY
Below the §6.2 bar, not promoted.

- **The stack reflows.** 2 of 6 renders on 2026-08-13 ignored three-panels-stacked — one came
  back a 2x2 grid of four with the USE beat drawn twice, one a tall left panel with two stacked
  at the right. 4 of 6 held. Untested hypothesis: all six frames arrived 1200x896 landscape
  whatever ratio was asked, and a three-high stack in a landscape frame gives very wide short
  panels that both alternative arrangements fit better.
- **The last panel opens onto new ground.** 1 of 6: a steamer RESULT stood the product on a
  side table that `environment` never named and no panel above it showed. Prompts now state
  that the named details are the whole of the room. One observation is not a rule.

## NOTES
**The corner sparkle is a generator watermark, not a render fault.** 1.3 recorded it here as an
unrequested mark on 2 of 6 renders. That was wrong. Stacking the bottom-right corner of 19
renders across two types, five products and three batches — content cancels, a fixed overlay
survives — leaves a clean 48x48 four-point star whose centre sits 100 px in from the right edge
and 100 px up from the bottom of a 1200x896 frame. A shuffled-offset control of the same 19
leaves nothing, and the bottom-left corner leaves nothing. Round numbers and a fixed position
across unrelated prompts make it an overlay stamped on the output. It is on every render this
library has, faint over light ground and obvious over dark. **No prompt clause can remove it and
none should try** — naming it would spend budget on a thing the model never drew. Whether the
adapter should carry this for all types is with the owner.

Distinction within step 3: `ghostbody` and `xray` explain WHY a product works, `spec-split`
argues what is better inside, and this type answers "can I operate it". A gallery rarely needs
more than two step-3 answers, and this one is usually the second.

## CHANGELOG
A decision and its evidence pointer. The reasoning is in the commit (ADR-013).
- 1.7 (2026-08-13): `fit` cut at 0/8. Substance marks are 7/7 and drawn overlay at seam scale
  is 0/8, so this type argues with things in the scene, never with overlay. `layout` stops
  describing frame geometry — the owner sets the ratio, and reasoning about the frame buys
  extra small panels. SLOT CONSTRAINTS gains the measurement: prompt length breaks the stack,
  1533 characters held 4/6 and 2368 held 1/4 into the same frame.
- 1.6 (2026-08-13): three owner corrections. Ratios move to the five allowed by ADR-016, so
  `4:5` becomes `3:4`. `register` stops prescribing one look — it was the source of the slop,
  4 mandated palettes and 8 mandated lights in one four-prompt set — and now varies per prompt,
  while `continuity` keeps sameness inside an image. `fit` is recorded as 0/6 as first
  specified: told to sit in the gap touching neither part, it landed in background air stating
  nothing. Respecified onto the contact line, with one attempt before it is cut. `6936cf6`
- 1.5 (2026-08-13): the type gains a second mark, by the owner's decision. `fit` states the
  junction where the product seats onto what it acts on, PREPARE only, form still under test.
  The blanket ban on arrows is replaced by the distinction that carries the type's actual
  argument: no mark may carry the reading order, and a mark inside one panel may state what
  the action leaves ambiguous. `emission` and NEGATIVE unchanged in substance. `8432ba6`
- 1.4 (2026-08-13): retraction. The sparkle 1.3 filed as an unrequested mark is a generator
  watermark on every output — measured by stacking 19 corners across two types against a
  shuffled control and a bottom-left control. Moved out of KNOWN-FLAKY into NOTES, and the two
  ledger records that listed it as a failure are corrected by new records, not edited. Neither
  verdict changes: both wine renders keep their other failures. `c2624ee`
- 1.3 (2026-08-13): first render evidence for this type — six renders, three products, 0 pass /
  4 partial / 2 fail. `emission` gains its founding evidence, 2/2 as real backlit steam. Three
  rules earned in `panels`: the beat names never reach the model (Rule 1b, third type), a
  removed part must be described as absent, and a changing product state must be named in every
  panel. Stack reflow and an unrequested sparkle go to KNOWN-FLAKY, both under the §6.2 bar.
  `f225ba2`
- 1.2 (2026-08-13): restructured into a call-map plus PARTS and MARKS (ADR-012); skeleton
  1645 → 608. `emission` named as the type's only mark, and the MARKS section states plainly
  that the near-absence is the design: this type argues with actions rather than graphics, and
  an arrow or a number would make it the manual its PURPOSE avoids. `RATIO:` dropped per
  adapter Rule 4. `e8ca963`
- 1.1 (2026-08-11): channels gain `advertorial`. Demand evidence: two real advertorial pages
  for the wall cooler carry explicit numbered step sections, which is what this type serves.
- 1.0 (2026-08-10): initial from the pet-brush three-panel exemplar; exemplar fault encoded —
  two actions crowded into panel 1. seed: conversation.md.

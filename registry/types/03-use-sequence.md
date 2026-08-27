---
id: 03-use-sequence
step: 3
job: use
device: sequence
version: "1.9"
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

## SKELETON
A call-map. Each arrow names an entry in PARTS or MARKS; the definition lives there once
and is never restated here or in a rendered prompt.

```
TYPE: 03-use-sequence v1.9
REGISTER: a real home, close range, available light.          -> PARTS/register

[PRODUCT REFERENCE] the attached photo is the exact reference, in every panel.
[LAYOUT] three panels stacked, thin white gutters.            -> PARTS/layout
[CONTINUITY] one pair of hands, one place, one light.         -> PARTS/continuity
[PANELS] prepare, then use, then result.                      -> PARTS/panels
[ENVIRONMENT] one ordinary room, named once.                  -> PARTS/environment
[MARKS] made of real substance, never drawn.                  -> MARKS
  fill, all three panels     trace, the USE panel
  emission, the USE panel    residue, the RESULT panel
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
- **RESULT**: the action finishing, plus a second hand or gesture expressing the outcome, and
  **no new mechanics** — this panel closes on the relationship, not on more machinery, which is
  what separates the type from a dry manual.

**The closing panel is lit exactly like the two above it.** It carried "warmer light than the
previous panels" from 1.0 until 1.8 and shipped that way 15 times across four sets, in flat
contradiction of `continuity` on the same page: one light direction and one palette across all
three. The owner caught it on the images — the last panel always came back a different colour,
which is three photographs of three moments, and this type has exactly one moment. What
resolves the closing panel is `residue`, not a grade.

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

**Any part of the product whose state visibly changes is named in every panel, including the
one where it is still empty** — that is `fill` in MARKS. `continuity` declares hands, place and
light identical across the three panels and the model extends that to the product's own state:
a cork named only in the middle panel was already inside the opener's window in the first, so
the first two panels showed one state and the middle beat was empty. 2 of 2.

**`environment`** — one ordinary domestic setting with one or two incidental details, named
once and identical in all three panels.

## MARKS

**Every mark in this type is made of something physically in the scene, and nothing is ever
drawn over the photograph.** That is measured, not a preference: a mark made of real substance
has rendered correctly 7 times out of 7, and a drawn mark at the scale of a seam rendered
usably 0 times out of 8 before `fit` was cut at 1.7. A11 in `registry/argument-faults.md` is
not contradicted — drawn geometry does read in a photographic register at the scale of rings
and glows sized to the whole frame, and that is not a scale this type has any use for.

**No mark carries the reading order**, and nothing points from one panel to another. A step
number or a linking arrow would make this the instruction manual its PURPOSE exists to avoid.

The four entries are the four things a plain photograph of someone using a product does not say
on its own, and between them they carry the type's whole argument.

| name | made of | panel | evidence |
|---|---|---|---|
| `fill` | the level of a real substance inside a transparent part of the product | all three | ~6 correct, no failure attributable to it |
| `emission` | whatever the product visibly puts out — steam, spray, foam, a jet, a falling solid | USE | 7/7 |
| `trace` | the acted-on surface itself: done behind the head, not-yet-done ahead of it | USE | 2, both correct in frames that failed on layout |
| `residue` | what the product removed or produced, collected and visible | RESULT | 2 |

**`fill` is the through-line, and it is what makes three photographs one event.** A tank going
down, a jar filling with grounds, a cork rising into a window, a chamber greying with lint. It
is named in every panel including the one where it is still empty, because `continuity` tells
the model everything is identical across panels and it applies that to the product's own state
unless the state is named each time. It is the only mark that appears in all three panels, and
it is the one to reach for first: it needs no substance leaving the product and no mess left
behind, so it is available on almost every product.

**`emission` exists only if the product genuinely emits** (G8). Never invent one so a panel
looks active — G8's subject is exactly not faking an effect so a photograph looks like it is
working, and a photographic register is where that is easiest and least forgivable. It is a
real thing in the room, lit to be visible, in its own real colour.

**`trace` is A8 applied to this type.** A change of state needs a boundary rather than two
states side by side, so the product sits ON the boundary of one continuous surface: cleared
carpet behind the head and grit ahead of it, wet floor behind the mop and dry ahead, stitched
hem behind the foot and torn ahead. It costs nothing to render because it is the surface
itself, and it is the cheapest proof in the library that the product does something.

**`residue` is how the closing panel resolves.** Lint tipped into a bin, scale rinsing off a
filter, grounds sitting in the paper, the open tin. It replaces the warmer light that used to
close these images and that contradicted `continuity` for eight versions: the last panel is
lit like the others and earns its ending by showing what came out. It is the only mark that may
appear after the action has finished.

**Marks are optional and a bare sequence is not a defect.** The clearest render this type has
produced carried none: three panels, one kettle, no mark of any kind. A mark is added when the
action alone leaves the argument short, never to fill the library.

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
The two renders that passed with an empty `failures` list, kept in full because that text is
the only record of what actually rendered — the ledger stores verdicts, not prompts (SPEC 3.3).

**Both predate 1.7 and 1.8 and each contains three clauses that are now removed law**: a
`ratio param` line, a LAYOUT sentence reasoning about the shape of the frame, and a closing
panel lit warmer than the two above it. They are records, not templates. Current law is in
PARTS; copy from there.

### example: foam-soap-dispenser — skeleton@1.4, run: pass
Product: touchless foam soap dispenser · camera_lock=handheld
Three panels stacked as asked. `emission` on foam, the second substance after steam and the
render that took the mark beyond a single product. The reservoir is named in all three panels,
which is `fill` before it had a name.

```
TYPE: 03-use-sequence v1.4
REGISTER: warm lifestyle photography, close range, natural and unstyled, soft
daylight.

PRODUCT REFERENCE: the attached photo is the exact reference for the touchless foam
soap dispenser, in every panel. Preserve shape, proportions, material, finish and
colour exactly.

LAYOUT: exactly three photographs, one above another, each the full width of the
frame and all three the same height, separated by thin white gutters, no outer
border.

CONTINUITY: the SAME pair of hands in all three panels - same skin tone, same
nails, same wrists, same cuffs. The same white basin and the same brushed tap
throughout. The same warm neutral palette and the same soft daylight from the left
in every panel. Camera distance and framing shift naturally between panels.

At the top, the dispenser's lid is hinged open and still attached, and one hand
pours soap from a refill bottle into the reservoir, the liquid rising to fill the
translucent body.

In the middle, the lid is closed and the reservoir is full, and one open palm is
held flat and still beneath the nozzle with no contact anywhere on the dispenser.

At the bottom, the reservoir is still full and the dispenser stands untouched on
the ledge while both hands rub the lather together, in warmer light than the two
photographs above, with no new mechanics.

The dispenser sits near the centre of all three photographs, whole and uncropped in
each.

Only the middle photograph carries foam: a real dose of white foam leaving the
nozzle and landing on the open palm, lit from the left so its texture reads against
the skin. It is foam in the room, not a graphic.

ENVIRONMENT: an ordinary bathroom basin, a folded hand towel, a small plant. The
same location in all three panels, and the details named here are the only
furniture and surfaces that appear in any of them. Nothing is set down on a
surface not named here.
```

### example: descaling-kettle — skeleton@1.6, run: pass
Product: electric kettle · camera_lock=handheld
The clearest render this type has produced, and it carries no marks at all. Three panels
stacked, the limescale filter named in all three, and a closing panel that removes a part and
says what the kettle looks like without it. It is also the shortest prompt of its set and the
only one in it that stacked, which is the observation that became the prompt-budget rule.

```
TYPE: 03-use-sequence v1.6
REGISTER: a real home photographed plainly at close range on the light that is
there. Not a diagram and not a manual.

PRODUCT REFERENCE: the attached photo is the exact reference for the electric
kettle, in every panel. Preserve shape, proportions, material, finish and colour
exactly.

LAYOUT: exactly three photographs, one above another, each the full width of the
frame and all three the same height, separated by thin white gutters, no outer
border.

CONTINUITY: the SAME pair of hands in all three panels - pale freckled hands,
short nails, a grey t-shirt sleeve at the shoulder. The same bare white laminate
worktop and the same white tiled wall throughout. A plain utilitarian kitchen at
midday with hard direct sun coming through an uncurtained window on the right,
throwing sharp-edged shadows and blowing the white surfaces bright. That same hard
sun and those same sharp shadows in all three panels. Camera distance and framing
shift naturally between panels.

At the top, one hand holds the kettle by its handle while the other swings the lid
open, the limescale filter visible clipped in behind the spout and furred pale
white with scale.

In the middle, the kettle is set down on its base and one hand presses the switch,
the lid closed, the water going cloudy as it comes up to the boil, the same furred
filter still clipped in behind the spout.

At the bottom, the filter has been unclipped and is held in one hand under the
running tap with the scale rinsing off it, while the kettle stands on its base
beside them with the lid open and the empty slot behind the spout plainly visible.
There is exactly one filter in this photograph. Warmer light than the two
photographs above, with no new mechanics.

The kettle sits near the centre of all three photographs, whole and uncropped in
each, its filter included in the frame.

Nothing is drawn onto the photographs. This product emits nothing visible and
nothing seats onto anything, so the actions carry the sequence on their own. Each
frame is a plain unretouched photograph and everything visible in it is a real
object in the room.

ENVIRONMENT: a plain kitchen worktop, a single mug waiting beside the kettle, a
box of teabags. The same location in all three panels, and the details named here
are the only furniture and surfaces that appear in any of them. Nothing is set down
on a surface not named here.
```

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
- 1.9 (2026-08-13): type passed by the owner; file finalised. WORKED EXAMPLES replaced with the
  two renders that passed with an empty failures list — the foam soap dispenser and the
  descaling kettle — both in full prompt text, both labelled for the three clauses in them that
  1.7 and 1.8 removed. The untested shower-filter example and the `partial` steamer are dropped. `ffee670`
- 1.8 (2026-08-13): a mark library built to what this register actually renders. Four entries,
  every one made of real substance: `fill`, `emission`, `trace`, `residue`. The closing panel
  stops being lit warmer — that clause contradicted `continuity` since 1.0 and shipped 15 times,
  and the owner caught it as the last panel always changing colour. `residue` closes the
  sequence instead. `0defcb8`
- 1.7 (2026-08-13): `fit` cut at 0/8. Substance marks are 7/7 and drawn overlay at seam scale
  is 0/8, so this type argues with things in the scene, never with overlay. `layout` stops
  describing frame geometry — the owner sets the ratio, and reasoning about the frame buys
  extra small panels. SLOT CONSTRAINTS gains the measurement: prompt length breaks the stack,
  1533 characters held 4/6 and 2368 held 1/4 into the same frame. `0f256e2`
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
